---
Date Generated: April 08, 2024
Transcription Model: whisper medium 20231117
Length: 11961s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'elon musk', 'joe rogan', 'lee cronin', 'lex ai', 'lex fridman', 'lex friedman', 'lex jre', 'lex mit', 'lex pod', 'lex podcast']
Video Views: 1233622
Video Rating: None
---

# Lee Cronin: Controversial Nature Paper on Evolution of Life and Universe | Lex Fridman Podcast #404
**Lex Fridman:** [December 09, 2023](https://www.youtube.com/watch?v=CGiDqhSdLHk)
*  every star in the sky probably has planets and life is probably emerging on these planets.
*  But I think the commentarial space associated with these planets is so different. Our causal
*  cones are never going to overlap or not easily. And this is the thing that makes me sad about
*  alien life, why it's why we have to create alien life in the lab as quickly as possible. Because
*  I don't know if we are going to be able to be able to build
*  architectures that will intersect with alien intelligence architectures.
*  And intersect, you know, I mean in time or space.
*  Time and the ability to communicate.
*  The ability to communicate.
*  Yeah. My biggest fear in a way is that life is everywhere,
*  but we become infinitely more lonely because of our scaffolding in that commentarial space.
*  The following is a conversation with Lee Cronin, his third time on this podcast. He is a chemist
*  from University of Glasgow, who is one of the most fascinating, brilliant and fun to talk to
*  scientists I've ever had the pleasure of getting to know. This is the Lex Friedman podcast. To
*  support it, please check out our sponsors in the description. And now, dear friends, here's Lee
*  Cronin. So your big assembly theory paper was published in Nature.
*  Congratulations.
*  Thanks.
*  It created, I think it's fair to say a lot of controversy, but also a lot of interesting
*  discussion. So maybe I can try to summarize assembly theory and you tell me if I'm wrong.
*  Go for it.
*  So assembly theory says that if we look at any object in the universe, any object, that we can
*  quantify how complex it is by trying to find the number of steps it took to create it. And also,
*  we can determine if it was built by a process akin to evolution by looking at how many copies
*  of the object there are.
*  Yeah, that's spot on.
*  Spot on. I was not expecting that. Okay. So let's go through definitions.
*  So there's a central equation I'd love to talk about, but definition wise, what is an object?
*  Object, so if I'm going to try to be as meticulous as possible, objects need to be finite and they
*  need to be decomposable into subunits. All human-made artifacts are objects. Is a planet an object?
*  Probably yes, if you scale out. So an object is finite and countable. So if you look at the
*  probably yes, if you scale out. So an object is finite and countable and decomposable,
*  I suppose mathematically. But yeah, I still wake up some days and go to think to myself,
*  what is an object? Because it's a non-trivial question.
*  It persists over time. I'm quoting from the paper here. An object that's finite is distinguishable.
*  Sure, that's a weird adjective. Distinguishable.
*  We've had so many people offering to rewrite the paper after it came out. You wouldn't believe it's
*  so funny. Persists over time and is breakable such that the set of constraints to construct it
*  from elementary building blocks is quantifiable. Such that the set of constraints to construct it
*  from elementary building blocks is quantifiable.
*  The history is in the object. It's kind of cool, right?
*  What defines the object is its history or memory, whichever is the sexier word.
*  I'm happy with both, depending on the day.
*  The set of steps it took to create the object. There's a sense
*  in which every object in the universe has a history.
*  Yep.
*  That is part of the thing that is used to describe its complexity. How complicated it is.
*  What is an assembly index?
*  The assembly index, if you're to take the object apart and be super lazy about it or minimal,
*  it's like you've got a really short-term memory. What you do is you lay all the parts on the path
*  and you find the minimum number of steps you take on the path to add the parts together
*  to reproduce the object. That minimum number is the assembly index. It's a minimum bound.
*  It was always my intuition the minimum bound in assembly theory was really important. I only
*  worked out why a few weeks ago, which is kind of funny. I was just like, no, this is sacrosanct.
*  I don't know why. It will come to me one day. Then when I was pushed by a bunch of mathematicians,
*  we came up with the correct physical explanation, which I can get to, but it's the minimum. It's
*  really important. It's the minimum. The reason I knew the minimum was right is because we could
*  measure it. Almost before this paper came out, we published papers explaining how you can measure
*  the assembly index of molecules. That's not so trivial to figure out. When you look at an object,
*  we could say a molecule, we could say object more generally, to figure out the minimum
*  number of steps it takes to create that object. That doesn't seem like a trivial thing to do.
*  With molecules, it's not trivial, but it is possible because what you can do, and because I'm
*  a chemist, I'm kind of like I see the lens of the world for just chemistry, I break the molecule
*  apart and break bonds. If you take a molecule and you break it all apart, you have a bunch of atoms
*  and then you say, okay, I'm going to then take the atoms and form bonds and go up the chain
*  of events to make the molecule. That's what made me realize, take a toy example, literally toy
*  example, take a Lego object, which is broken up of Lego blocks. You could do exactly the same thing.
*  In this case, the Lego blocks are naturally the smallest, they're the atoms in the actual composite
*  Lego architecture. But then if you maybe take a couple of blocks and put them together in a
*  certain way, maybe they have an offset in some way, that offset is on the memory. You can use
*  that offset again with only a penalty of one and you can then make a square triangle and keep going.
*  You remember those motifs on the chain, so you can then leap from the start with all the Lego
*  blocks or atoms just laid out in front of you and say, right, I'll take you, you connect and do the
*  least amount of work. It's really like the smallest steps you can take on the graph to make the object.
*  For molecules, it came relatively intuitively and then we started to apply it to language.
*  We've even started to apply it to mathematical theorems, but I'm so well out of my depth,
*  but it looks like you can take minimum set of axioms and then start to build up
*  mathematical architectures in the same way. Then the shortest path to get there is something
*  interesting that I don't yet understand. What's the computational complexity of figuring out
*  the shortest path with molecules, with language, with mathematical theorems?
*  It seems that once you have the fully constructed Lego castle,
*  or whatever your favorite Lego world is, figuring out how to get there from the
*  basic building blocks, is that an MP hard problem? It's a hard problem.
*  It's a hard problem, but actually if you look at it, the best way to look at it,
*  let's take a molecule. If the molecule has 13 bonds, first of all, take 13 copies of the molecule
*  and just cut all the bonds, so take 12 bonds, and then you just put them in order. Then that's how
*  it works. You keep looking for symmetry or copies, so you can then shorten it as you go down,
*  and that becomes commentorially quite hard. For some natural product molecules,
*  it becomes very hard. It's not impossible, but we're looking at the bounds on that at the moment.
*  As the object gets bigger, it becomes really hard. That's the bad news, but the good news is there
*  are shortcuts. We might even be able to physically measure the complexity without computationally
*  calculating it, which is kind of insane. How would you do that?
*  Well, in the case of molecule, if you shine light on a molecule, let's take an infrared,
*  the molecule has each of the bonds absorbs the infrared differently in what we call the
*  fingerprint region. It's a bit like, because it's quantized as well, you have all these discrete
*  absorbances. My intuition after we realized we could cut molecules up in mass spec, that was
*  the first go at this. We did it with using infrared, and the infrared gave us an even better
*  correlation assembly index, and we used another technique as well in addition to infrared called
*  NMR, nuclear magnetic resonance, which tells you about the number of different magnetic environments
*  in a molecule, and that also worked out. We have three techniques, which each of them independently
*  gives us the same or tending towards the same assembly index for molecule that we can calculate
*  mathematically. Okay, so these are all methods of mass spectrometry, mass spec. You scan a molecule,
*  it gives you data in the form of a mass spectrum, and you're saying that the data correlates to the
*  assembly index. Yeah. How generalizable is that shortcut, first of all, to chemistry,
*  and second of all, beyond that, because that seems like a nice hack, and you're extremely
*  knowledgeable about various aspects of chemistry, so you can say, okay, it kind of correlates.
*  But the whole idea behind assembly theory paper, and perhaps why it's so controversial,
*  is that it reaches bigger. It reaches for the bigger general theory of objects in the universe.
*  Yeah, I'd say so. I'd agree. So I've started assembly theory of emoticons with my lab,
*  believe it or not. So we take emojis, pixelate them, and work out the assembly index emoji,
*  and then work out how many emojis you can make on the path of emoji. So there's the uber emoji
*  from which all other emojis emerge, and then you can then take a photograph, and by looking at the
*  shortest path by reproducing the pixels to make the image you want, you can measure that. So then
*  you start to be able to take spatial data. Now there's some problems there. What is then the
*  definition of the object? How many pixels? How do you break it down? And so we're just learning
*  all this right now. So how do you compute the, how would you begin to compute the assembly index
*  of a graphical, like a set of pixels on a 2G plane that form a thing?
*  So you would first of all determine the resolution. So then what is your x,
*  y, and what number on the x and y plane, and then look at the surface area, and then you take all
*  your emojis and make sure they're all looked at the same resolution. And then we would basically then
*  do the exactly the same thing we would do for cutting the bonds. You'd cut bits out of the emoji
*  and look at them. You'd have a bag of pixels, and you would then add those pixels together
*  to make the overall emoji. But like, first of all, not every pixel is, I mean, this is at the core
*  sort of machine learning and computer vision. Not every pixel is that important. And there's like
*  macro features, there's micro features and all that kind of stuff. Exactly. Like, you know,
*  the eyes appear in a lot of them. The smile appears in a lot of them.
*  So in the same way in chemistry, we assume the bond is fundamental. What we do in there here is we
*  assume the resolution at the scale at which we do it is fundamental. And we're just working that
*  out. And that you're right, that will change, right? Because as you take your lens out a bit,
*  it will change dramatically. But it's just a new way of looking at not just compression,
*  what we do right now in computer science and data. One big kind of
*  misunderstanding is assembly theory is telling you about how compressed the object is.
*  That's not right. It's a how much information is required on a chain of events. Because the nice
*  thing is if when you do compression in computer science, we're wandering a bit here, but it's
*  kind of worth wandering, I think, in you, you assume you have instantaneous access to all the
*  information in the memory. Yeah, assembly theory, you say, No, you don't get access to that memory
*  until you've done the work. And then you don't access that memory, you can have access, but not
*  to the next one. And this is how in assembly theory, we talk about the four universes, the
*  assembly universe, the assembly possible, and the assembly contingent, and then the assembly
*  observed. And they're all, all scales in this combinatorial universe. Yeah, can explain each
*  one of them? Yep. So the assembly universe is like anything goes, just is just combinatorial kind of
*  explosion in everything. That's the biggest one. That's the biggest ones massive assembly universe,
*  assembly possible assembly contingent assembly observed. And on the y axis is assembly steps in
*  time. Yeah. And, you know, in the x axis, as the thing expands through time, more and more unique
*  objects appear. So yeah, so assembly universe, everything goes. Yep. Assembly possible laws of
*  physics come in, in this case, in chemistry bonds, in assembly. So that means those are actually
*  constraints, I guess. Yes. And they're the only constraints are the constraints of the base. The
*  way to look at it, you've got all your atoms, they're quantized, you can just bung them together.
*  So then you can become a kind of so in the way in computer science speak, I suppose the assembly
*  universe is just like no laws of physics, things can fly through mountains beyond the speed of light.
*  In in the assembly possible, you have to apply the laws of physics, but you can get access to
*  all the motifs instantaneously with no effort. So that means you could make anything, then the
*  assembly contingent says no, you can't have access to the highly assembled object in the future until
*  you've done the work in the past on the causal chain. And that's really the really interesting
*  shift where you go from assembly possible to assembly contingent. That is really the key thing
*  in assembly theory that says you cannot just have instantaneous access to all those memories,
*  you have to have done the work somehow, the universe has to have somehow built a
*  a system that allows you to select that path rather than other paths. And then the final thing
*  the assembly observed is basically are saying, oh, these are the things we actually see, we can go
*  backwards now and understand that they have been created by this, this causal process.
*  Wait a minute. So when you say the universe has to construct the system that does the work,
*  is that like the environment that that that allows for like selection?
*  Yeah, yeah, yeah.
*  That's the thing that does the selection.
*  You could think about in terms of a von Neumann constructor versus selection, a ribosome,
*  Tesla, a plant assembling Teslas, you know, the difference between the assembly universe in
*  Tesla land and the factory is everyone says no, Teslas are just easy, they just spring out,
*  you know how to make them all the Tesla factory, you have to put things in sequence,
*  and out comes a Tesla.
*  So you're talking about the factory?
*  Yes, this is this is really nice. Super important point is that when I talk about the universe
*  having a memory, or there's some magic, it's not that it's that tells you that there must be a
*  process encoded somewhere in physical reality, be it a cell, a Tesla factory, or something else is
*  making that object. I'm not saying there's some kind of woo woo memory in the universe,
*  you know, morphic resonance or something, I'm saying that there is an actual causal
*  process that is being directed constrained in some way. So it's not kind of just making everything.
*  Yeah, but Lee, what's the factory, they made the factory.
*  So what is the so first of all, you assume the laws of physics is just sprung to
*  existence at the beginning. Those are constraints. But what makes the factory the environment that
*  does the selection? This is the question or well, it's the first interesting question that I want
*  to answer out of four. I think the factory emerges in the environment, the interplay between the
*  environment, and the objects that are being built. And, and here, let me, I'll have a go explain to
*  you the shortest path. So why is the shortest path important? Imagine you've got, I'm gonna have to
*  go chemistry for a moment, then abstract it. So imagine you've got an environment, a given
*  environment that that you have a budget of atoms, you're just flinging together. Yep. And the the
*  objective of those atoms that being flung together and say molecule A have to make that they have
*  decomposed. So molecules decompose over time. So the molecules in this environment in this magic
*  environment have to not die. But they do die. There's a there's a they have a half life. So
*  the only way the molecules can get through that environment out the other side, let's pretend
*  the environment is a box and go in and out without dying. And there's a there's just an infinite
*  supply of atoms coming or a well, a large supply. The molecule gets built. But the molecule that
*  is able to template itself being built and survives in the environment will will basically
*  reign supreme. Now, let's say that molecule takes 10 steps. Now, and it is using a finite set of
*  atoms, right? Or now let's say another molecule smart ass molecule will call it comes in,
*  and can survive in that environment. And can copy itself, but it only needs five steps.
*  The molecule that only needs five steps because it's continued, both molecules have been destroyed,
*  but they're creating themselves faster, they can be destroyed. You can see that the shortest path
*  reigns supreme. So the shortest path tells us something super interesting about the minimal
*  amount of information required to propagate that motif in time and space. And it's just like a kind
*  of, it seems to be like some kind of conservation law. So one of the intuitions you have,
*  is the propagation of motifs in time will be done by the things that can construct themselves
*  in the shortest path. So like, you can assume that most of the objects in the universe are built
*  in the shortest, in the most efficient way. That the so big leap I just took there. Yeah,
*  no, yeah, yes and no, because there are other things. So in the limit, yes, because you want
*  to tell the difference between things that have required a factory to build them and just random
*  processes. But you can find instances where the shortest path isn't taken for an individual object,
*  individual function. And people go, ah, that means the shortest path isn't right. And then I say,
*  well, I don't know, I think it's right still. Because, so of course, because there are other
*  driving forces, it's not just one molecule. Now when you start to consider two objects,
*  you have a joint assembly space. And it's not, now it's a compromise between not just making A and
*  B in the shortest path. You want to make A and B in the shortest path, which might mean that A is
*  slightly longer, you have a compromise. So when you see slightly more nesting in the construction,
*  when you take a given object, that can look longer. But that's because the overall function
*  is the object is still trying to be efficient. Yeah. And this is still very hand wavy.
*  Maybe I have no leg to stand on. We think we're getting somewhere with that. And there's probably
*  some parallelization. Yeah, right. So this is all this not sequential. The building is,
*  I guess, when you're talking about complex objects, you don't have to work sequentially,
*  you can work in parallel, you can get your friends together and they can. Yeah. These and the thing
*  we're working on right now is how to understand these parallel processes. Now there's a new
*  thing we've introduced called assembly depth. And assembly depth can be lower than the assembly
*  index for a molecule when they're cooperating together, because exactly this parallel processing
*  is going on. And my team have been working this out in the last few weeks, because we're looking at
*  what compromises does nature need to make when it's making molecules in a cell.
*  And I wonder if, you know, I may be like, well, I'm always leaping out of my competence.
*  But in economics, I'm just wondering if you could apply this in economic processes seems like
*  capitalism is very good at finding the shortest path, you know, every time, but there are
*  ludicrous things that happen because actually the cost function has been minimized. And so I keep
*  seeing parallels everywhere where they're complex nested systems, where you give it enough time,
*  and you introduce a bit of heterogeneity, the system readjusts and finds a new shortest path.
*  But the shortest path isn't fixed on just one molecule. Now, it's in the actual existence of
*  the object over time. And that object could be a city, it could be a cell, it could be a factory.
*  But I think we're going way beyond molecules. And my competence, I probably should go back
*  to molecules. But hey, I before we get too far, let's talk about the assembly equation.
*  Okay, how should we do this? Now, let me just even read that part of the paper.
*  We define assembly as the total amount of selection necessary to produce an ensemble
*  of observed objects, quantified using equation one. The equation basically has a on one side,
*  which is the assembly of the ensemble. And then a sum from one to n, where n is the total number
*  of unique objects. And then there is a few variables in there that include the assembly index,
*  the copy number, which we'll talk about. That's an interesting, I don't remember you talking about
*  that. That's an interesting addition. And I think a powerful one has to do with what that you can
*  create pretty complex objects randomly. And in order to know that they're not random, that there's
*  a factory involved, you need to see a bunch of them. Yeah, that's, that's a good point.
*  That's the intuition there. It's an interesting intuition. And then some normalization. What else
*  is it? And minus one, just to make sure that I'm more than one object, one object could be a one
*  off and random. Yep. And then you have more than one identical object. That's interesting.
*  When there's two of a thing, two of a thing is super important, especially if the index assembly
*  index is high. So we could say several questions here. One, let's talk about selection. What is
*  this term selection? What is this term evolution that we're referring to? Which aspect of Darwinian
*  evolution are we referring to? That's interesting here. So yeah, so this is probably what you know,
*  the paper, we should talk about the paper second, the paper did what it did is it kind of annoyed.
*  We didn't know. I mean, it got attention. And obviously, angry people, the angry people were
*  annoyed. There's angry people in the world. That's good. So what happened is the evolutionary biologist
*  got angry. We were not expecting that because we thought evolutionary biologists would be cool.
*  I knew that some, not many computational complexity people will get angry because I've
*  kind of been poking them and maybe I deserved it. But I was trying to poke them in a productive way.
*  And then the physicist kind of got grumpy because the initial conditions tell everything.
*  The pre-biotic chemist got slightly grumpy because there's not enough chemistry in there.
*  Then finally, when the creationist said it wasn't creationist enough, I was like,
*  I've done my job. You're saying the physics they say, because you're basically saying that physics
*  is not enough to tell the story of how biology emerges. I think so. And then they said,
*  a few physics is the beginning and the end of the story. Yeah. So what happened is the reason why
*  people put the phone down on the call of the paper. If you view the reading the paper like a phone
*  call, they got to the abstract. And in the abstract, it's per sentence is pretty,
*  the first two sentences caused everybody's scientists have grappled with reconciling
*  biological evolution with the immutable laws of the universe defined by physics.
*  True. Right. There's nothing wrong with that statement. Totally true.
*  Yeah. These laws underpin life's origin, evolution and the development of human culture
*  and technology, yet they do not predict the emergence of these phenomena. Wow. First of all,
*  we should say the title of the paper. This is paper was accepted and published in nature.
*  The title is assembly theory explains and quantifies selection and evolution. Very humble title.
*  And the entirety of the paper, I think presents interesting ideas, but reaches high.
*  I am not, I would do it all again. This paper was actually on the preprint server for over a year.
*  You regret nothing.
*  Yeah. I think, yeah, I don't regret anything.
*  Frank Sinatra did it your way.
*  What I love about being a scientist is kind of sometimes I'm, because I'm a bit dim, I'm like,
*  and I don't understand what people telling me. I want to get to the point. This paper says, hey,
*  laws of physics are really cool. The universe is great, but they don't really, it's not intuitive
*  that you just run the standard model and get life out. I think most physicists might go, yeah,
*  there's this, you know, it's not just, we can't just go back and say that's what happened because
*  physics can't explain the origin of life yet. That doesn't mean it won't or can't. Okay. Just
*  to be clear, sorry, intelligent designers. We are going to get there. Second point, we say that
*  evolution works, but we don't know how evolution got going. So biological evolution and biological
*  selection. So for me, this seems like a simple continuum. So when I mentioned selection and
*  evolution in the title, I think, and in the abstract, we should have maybe prefaced that and
*  said non-biological selection and non-biological evolution. And then that might have made it even
*  more crystal clear, but I didn't think that biology, evolutionary biology should be so bold
*  to claim ownership of selection and evolution. And secondly, a lot of evolutionary biologists
*  seem to dismiss the origin of life questions. I say it's obvious. And that causes a real problem
*  scientifically because when two different, when the physicists are like, we own the universe,
*  universe is good. We explain all of it. Look at us. And even biologists say we can explain biology
*  and the poor chemistry in the middle going, but hang on. And this paper kind of says, hey,
*  there is an interesting disconnect between physics and biology. And that's at the point
*  at which memories get made in chemistry through bonds. And hey, let's look at this close and see
*  if we can quantify it. So yeah, I mean, I never expected the paper to kind of get that much
*  interest. And still, I mean, it's only been published just over a month ago now.
*  So just to link on the selection, what is the broader sense of what selection means?
*  Yeah, that's a really good for selection, selection. So I think for selection, you need,
*  so this is where for me, the concept of an object is something that can persist in time and not die,
*  but basically can be broken up. So if I was going to kind of bolster the definition of objects, so
*  so if something can form and persist for a long period of time under an existing environment that
*  could destroy other, and I'm going to use anthropomorphic terms, I apologize, weaker objects
*  or less robust, then the environment could have selected that. So good chemistry examples, if you
*  took some carbon and you made a chain of carbon atoms, whereas if you took some, I don't know,
*  some carbon, nitrogen and oxygen and made change from those, you start to get different reactions
*  and rearrangements. So a carbon, a chain of carbon atoms might be more resistant to falling apart
*  under acidic or basic conditions versus another set of molecules. So survives in that environment.
*  So the acid pond, the molecule, the resistant molecule can get through, and then that molecule
*  goes into another environment. So that environment now maybe being an acid pond is a basic pond,
*  or maybe it's an oxidizing pond. And so if you've got carbon and it goes in oxidizing pond, maybe
*  the carbon starts to oxidize and break apart. So you go through all these kind of obstacle courses,
*  if you like, given by reality. So selection is the ability happens when an object survives in
*  the environment for some time. But, and this is a thing that's super subtle, the object has to be
*  continually being destroyed and made by process. So it's not just about the process, the object now
*  is about the process and time that makes it because a rock could just stand on the mountain
*  side for four billion years and nothing happened to it. And that's not necessarily really advanced
*  selection. So for selection to get really interesting, you need to have a turnover in time,
*  you need to be continually creating objects, producing them, what we call discovery time.
*  So there's a discovery time for an object. When that object is discovered, if it's a molecule
*  that can then act on itself, or the chain of events that caused itself to bolster its formation,
*  then you go from discovery time to production time, and suddenly you have more of it in the
*  universe. So it could be a self replicating molecule. And the interaction of the molecule
*  in the environment in the warm little pond or in the sea or wherever in the bubble,
*  could then start to build a proto factory, the environment. So really, to answer your question,
*  what the factory is, the factory is the environment, but it's not very autonomous.
*  It's not very redundant. There's lots of things that could go wrong. So once you get high enough
*  up the hierarchy of networks of interactions, something needs to happen that needs to be
*  compressed into a smaller volume and made resistant robust. Because in biology, selection
*  and evolution is robust. You have error correction built in, you have really, you know, there's good
*  ways of basically making sure propagation goes on. So really the difference between inorganic
*  abiotic selection and evolution, and evolution and stuff in biology is robustness,
*  the ability to kind of propagate over, the ability to survive in lots of different environments.
*  Whereas our poor little inorganic, so molecule, whatever, just dies in lots of different
*  environments. So there's something super special that happens from the inorganic
*  molecule in the environment that kills it to where you've got evolution and cells can survive
*  everywhere. How special is that? How do you know those kinds of evolution factors aren't everywhere
*  in the universe? I don't, and I'm excited because I think selection isn't special at all. I think
*  what is special is the history of the environments on earth that gave rise to the first cell that now
*  has, you know, has taken all those environments and is now more autonomous. And I would like to
*  think that, you know, this paper could be very wrong. But I don't think it's very wrong. It's
*  certainly wrong, but it's less wrong than some other ideas, I know, right? And if this allow,
*  inspires us to go and look for selection in the universe, because we now have an equation where
*  we can say, we can look for selection going on and say, Oh, that's interesting. We seem to have a
*  process that's giving us high copy number objects also are highly complex. But that doesn't look like
*  life as we know it. And we use that so there's a hydrothermal vent. Oh, there's a process going on
*  as molecular networks, because the assembly equation is not only meant to identify at the
*  higher end, advanced selection, what you get, I would call it in biology, you super advanced
*  selection. And even, I mean, you could use the assembly equation to look for technology and
*  God forbid, we could talk about consciousness and abstraction, but let's keep it primitive
*  molecules and biology. So I think the real power of the assembly equation is to is to say how much
*  selection is going on in this space. And there's, there's a really simple thought experiment I could
*  do is you, you know, have a little petri dish and on that petri dish, you put some simple food.
*  So the assembly index of all the sugars and everything is quite low. So then and you put
*  a single echo cell of a E. coli cell. And then you say, I'm gonna, I'm gonna measure the assembly in
*  this amount of assembly in the box. So it's quite low. But the rate of change of assembly,
*  dA dt will go vum sigmoidal as it eats all the food. And the number of coli cells will replicate,
*  because they take all the food, they copy themselves, the assembly index of all the
*  molecules goes up, up, up and up until the food is exhausted in the box. So now the now the coli is
*  stopped. I mean, die is probably a strong word, they stop respiring, because all the food is gone.
*  But suddenly the amount of assembly in the box has gone up gigantically because of that one E. coli
*  factory has just eaten through milled lots of other E. coli factory has run out of food and stopped.
*  And so that looking at that, so in the initial box, although the amount of assembly was really
*  small, it was able to replicate and use all the food and go up. And that's what we're trying to
*  do in the lab, actually, is kind of make those kind of experiments and see if we can spot the
*  emergence of molecular networks that are producing complexity, as we feed in raw materials, and we
*  feed a challenge and environment, you know, we try and kill the molecules. And, and really, that's
*  the main kind of idea for the entire paper. And see if you can measure the changes in the
*  assembly index throughout the whole system. Yeah. Okay, what about if I show up to a new planet,
*  we'll go to Mars or some other planet from a different solar system. And how do we use
*  assembly index there to discover alien life? In very simply, actually, if we let's say we'll
*  go to Mars with a mass spectrometer with a sufficiently high resolution. So what you have
*  to be able to do. So good thing about mass spec is that you can select the molecule from the mass.
*  And then if it's high enough resolution, you can be more and more sure that you're just
*  seeing identical copies, you can count them. And then you fragment them and you count the
*  number of fragments and look at the molecular weight and the higher the molecular weight,
*  and the higher the number of fragments, the higher the assembly index. So if you go to Mars,
*  and you take a mass spec or high enough resolution, and you can find molecules,
*  I'll give a guide on Earth, if you could find molecules, say, greater than 350 molecular weight
*  with more than 15 fragments, you have found artifacts that can only be produced, at least on
*  Earth, by life. Now you would say, oh, well, maybe the geological process, I would argue very
*  that that is not the case. But we can say, look, if you don't like the cutoff on Earth,
*  go up higher, 30, 100, right? Because there's going to be a point where you'll find a molecule
*  so many different parts, the chances of you getting a molecule that has 100 different parts
*  and finding a million identical copies, you know, that's just impossible, that could never happen
*  in an infinite set of universes. Can you just linger on this copy number thing?
*  A million different copies. What do you mean by copies? And why is the number of copies important?
*  Yeah, that was so interesting. And I always understood the copy number is really important,
*  but I never explained it properly for ages. And I kept having this, it goes back to this,
*  if I give you a, I don't know, a really complicated molecule, and I say it's complicated,
*  you could say, hey, that's really complicated. But is it just really random? And so I realized
*  that ultimate randomness and ultimate complexity are indistinguishable until you can see a structure
*  in the randomness. So you can see copies. So copies implies structure. Yeah.
*  The fact that there's a deep profound thing in there. Because if you just have a random
*  random process, you're going to get a lot of complex, beautiful, sophisticated things.
*  What makes them complex in the way we think life is complex or, yeah, something like a factory
*  that's operating under a selection processes, there should be copies. Is there like some
*  looseness about copies? Like, what does it mean for two objects to be equal?
*  It's all to do with the telescope or the microscope you're using. And so at the maximum
*  resolution, so in the nice thing about chemists is they have this concept of the molecule,
*  and they're all familiar with the molecule. And molecules you can hold, you know, in your hand,
*  lots of them, identical copies. A molecule is actually a super important thing in chemistry
*  to say, look, you can have a mole of a molecule, an Avogadro's number of molecules, and they're
*  identical. What does that mean? That means that the molecular composition, the bonding and so on,
*  the configuration is indistinguishable. You can hold them together. You can overlay them.
*  So the way I do it is if I say, here's a bag of 10 identical molecules, let's prove they're
*  identical. You pick one out of the bag and you basically observe it using some technique,
*  and then you put it, you take it away, and then you take another one out. If you observe it using
*  technique, you see no differences. They're identical. It's really interesting to get right
*  because if you take say two molecules, molecules can be in different vibrational rotational states.
*  They're moving all the time. So with this respect, identical molecules have identical bonding.
*  In this case, we don't even talk about chirality because we don't have a chirality detector.
*  So two identical molecules in one conception assembly theory basically considers both hands
*  as being the same. But of course, they're not. They're different. As soon as you have a chiral
*  distinguisher to detect the left and the right hand, they become different.
*  And so it's to do with the detection system that you have and the resolution.
*  I wonder if there's an art in science to which detection system is used when you show up to a
*  new planet. So you're talking about chemistry a lot today. We have standardized detection systems
*  of how to compare molecules. So when you start to talk about emojis and language and
*  mathematical theorems and I don't know, more sophisticated things at a different scale,
*  at a smaller scale than molecules, at a larger scale than molecules,
*  like what detection, if we look at the difference between you and me,
*  like suddenly, are we the same? Are we different?
*  Sure. I mean, of course we're different close up, but if you zoom out a little bit,
*  it will morphologically look the same. High in characteristics, hair length, stuff like that.
*  Well, also like the species and also there's a sense why we're both from Earth.
*  Yeah, I agree. I mean, this is the power of assembly theory in that regard.
*  So the way to look at it, if you have a box of objects, if they're all indistinguishable,
*  then using your technique, what you then do is you then look at the assembly index.
*  Now, if the assembly index of them is really low, and they're all indistinguishable, then
*  it's telling you that you have to go to another resolution.
*  It's kind of a signing scale. It's kind of nice.
*  So those two are a tension with each other. The number of copies in the assembly index.
*  That's really, really interesting. So, okay, so you show up to a new planet,
*  you'll be doing what?
*  I would do mass spec.
*  I would bring in a sample of what? First of all, how big of a scoop do you take?
*  Do you just take the scoop? So we're looking for primitive life.
*  I would look, yeah. So if we're just going to Mars or Titan or Enceladus or somewhere,
*  so a number of ways of doing it. So you could take a large scoop or you go for the atmosphere
*  and detect stuff. You could make a life meter. One of Sarah's colleagues at ASU,
*  Paul Davis, keeps calling it a life meter, which is quite a nice idea because you think about it.
*  If you've got a living system that's producing these highly complex molecules and they drift
*  away and they're in a highly kind of demanding environment, they could be burnt, right? So they
*  could just be falling apart. So you want to sniff a little bit of complexity and say warmer, warmer,
*  warmer. Oh, we've found life. We've found the alien. We've found the alien Elon Musk smoking
*  a joint in the bottom of the cave on Mars or Elon himself, whatever, right? You say, okay, found it.
*  So what you can do is a mass spectrometer, you could just look for things in the gas phase
*  or you go on the surface, drill down because you want to find molecules that are, well, you've
*  either got to find the source living system because the problem with just looking for complexity
*  is it gets burnt away. So in a harsh environment on say on the surface of Mars, there's a very
*  low probability that you're going to find really complex molecules because of all the radiation
*  and so on. If you drill down a little bit, you could drill down a bit into soil that's billions
*  of years old. Then I would put in some solvent, water, alcohol or something, or take a scoop,
*  make it volatile, put it into the mass spectrometer and just try and detect
*  high complexity, high abundant molecules. And if you get them, hey presto, you can have evidence
*  of life. Wouldn't that then be great if you could say, okay, we've found evidence of life.
*  Now we want to keep the life meter, keep searching for more and more complexity until you actually
*  find living cells. You can get those new living cells and then you could bring them back to Earth
*  or you could try and sequence them. You could see that they have different DNA and proteins.
*  Go along the gradient of the life meter. How would you build a life meter? Let's say we're together
*  starting a new company and launching a life meter.
*  Mass spectrometer would be the first way of doing it.
*  No, no, no, but that's one of the major components of it. But I'm talking about
*  if it's a device and branding logo, we've got to talk about that later. But what's the input?
*  How do you get to the metered output?
*  I would take a life meter, our life meter.
*  Thank you.
*  You're welcome. It would have both infrared and mass spec. It would have two ports so it could
*  shine a light. What it would do is you would have a vacuum chamber and you would have an
*  electrostatic analyzer and you'd have a monochromator to producing infrared. You'd
*  add the sample. You'd take a scoop of the sample, put it in the life meter. It would then add a
*  solvent or heat up the sample so some volatiles come off. The volatiles would then be put into
*  the mass spectrometer, into the electrostatic trap and you'd weigh the molecules and fragment them.
*  Alternatively, you'd shine infrared light on them and you count the number of bands. But you'd have
*  to, in that case, do some separation because you want to separate. In mass spec, it's really
*  nice and convenient because you can separate electrostatically, but you need to have that.
*  Can you do it in real time?
*  Yeah, pretty much. Let's go all the way back. We're really going to get this.
*  Lex's life meet. Lex and Lee's life meet.
*  It's a good ring to it.
*  All right. You have a vacuum chamber. You have a little nose. The nose would have
*  a packing material. You would take your sample, add it onto the nose, add a solvent or a gas.
*  It would then be sucked up the nose and that would be separated using what we call chromatography.
*  As each band comes off the nose, we would then do mass spec and infrared. In the case of the
*  infrared, count the number of bands. In the case of mass spec, count the number of fragments and
*  weigh it. Then the further up in molecular weight range for the mass spec and the number of bands,
*  you go up and up and up from the dead, interesting, interesting, over the threshold, oh my gosh,
*  earth life. Then right up to batshit crazy, this is definitely alien intelligence that's made this
*  life. You could almost go all the way there, same in the infrared. It's pretty simple.
*  The thing that is really problematical is that for many years, decades, what people have done,
*  and I can't blame them, is they've been obsessing about small biomarkers that we find on earth,
*  amino acids like single amino acids or evidence of small molecules and these things and looking
*  for those, run looking for complexity. The beautiful thing about this is you can look for
*  complexity without earth chemistry bias or earth biology bias. Assembly theory is just a way of
*  saying, hey, complexity and abundance is evidence of selection. That's how our universal life meter
*  will work. Complexity and abundance is evidence of selection. Okay, so let's apply our life meter to
*  earth. If we were to just apply assembly index measurements to earth, what kind of stuff are
*  going to get? What's impressive about some of the complexity on earth?
*  We did this a few years ago when I was trying to convince NASA and colleagues that this
*  technique could work. Honestly, it's so funny because everyone's like, no, it ain't going to work.
*  I was just like, because the chemists were saying, of course there are complicated molecules out
*  there you can detect that just form randomly. I was like, really? That was like, it's a bit like
*  I don't know, someone saying, of course, Darwin textbook was just written randomly by some monkeys
*  and typewriters. Just for me, it was like, really? I pushed a lot on the chemists now and I think
*  most of them are on board, but not totally. It really had some big arguments, but the copy number
*  caught there because I think I confused the chemists by saying one off and then when I made
*  clear about the copy number, I think that made it a little bit easier. Just to clarify,
*  a chemist might say that of course, out there outside of earth, there's complex molecules.
*  Yes. Okay. Then you're saying, wait a minute, that's like saying, of course,
*  there's aliens out there. Exactly that. You're saying you clarify that
*  that's actually a very interesting question and we should be looking for complex molecules
*  of which the copy number is two or greater. Yes, exactly. On earth, coming back to earth,
*  what we did is we took a whole bunch of samples and we were running pre-biotic chemistry
*  experiments in the lab. We took various inorganic minerals and extracted them, look at the volatile
*  because there's a special way of treating minerals and polymers in assembly theory.
*  In our life machine, we're looking at molecules. We don't care about polymers
*  because they don't volatile, you can't hold them. If you can't assert that they're identical,
*  then it's very difficult for you to work out if there's undergone selection or they're just
*  a random mess. Same with some minerals, but we can come back to that. Basically, what you do,
*  we got a whole load of samples, inorganic ones. We got Scotch whiskey and also took Ardberg,
*  which is one of my favorite whiskeys, which is very peaty. The way that in Scotland in Islay,
*  which is a little island, the whiskey is let to mature in barrels and it's said that the peak,
*  the complex molecules in the peat might find their way through into the whiskey and that's
*  what gives it this intense brown color and really complex flavor. It's literally molecular complexity
*  that does that. Volcker's the complete opposite, it's just pure. The better the whiskey, the higher
*  the assembly index, the higher the assembly index, the better the whiskey. I really love
*  deep peaty Scottish whiskeys. Near my house, there is one of the lowland distilleries called
*  Glen Goyne. It's still beautiful whiskey, but not as complex. For fun, I took some Glen Goyne whiskey
*  in Ardberg and put them into the mass spec and measured the assembly index. I also got E. coli.
*  The way we do it, take E. coli, break the cell apart, take it all apart. Also got some beer.
*  And people were ridiculing us saying, oh, beer is evidence of complexity. One of the computational
*  complexity people was just throwing... Yeah, kind of he's very vigorous in his disagreement
*  of assembly theory was just saying, you don't know what you're doing, even beer is more
*  complicated than human. We didn't realize is that it's not beer per se, it is taking the yeast
*  extract, breaking the cells, extracting the molecules and just looking at the profile of
*  the molecules, see if there's anything over the threshold. We also put in a really complex molecule
*  taxol. We took all of these, but also NASA gave us, I think, five samples. They wouldn't tell us
*  what they are. They said, no, we don't believe you can get this to work. They gave us some super
*  complex samples. They gave us two fossils, one that was a million years old and one was at 10,000
*  years old. Something from Antarctica, seabed. They gave us a Mershwissen-Mieter and a few others.
*  Put them through the system. We took all the samples, treated them all identically,
*  put them into mass spec, fragmented them. In this case, implicit in the measurement was
*  in mass spec, you only detect peaks when you've got more than, let's say, 10,000 identical
*  molecules. The copy number is already baked in, but wasn't quantified, which is super important
*  there. This is in the first paper because it's abundant, of course. When you then took it all
*  out, we found that the biological samples gave you molecules that had an assembly index greater than
*  15. All the abartic samples were less than 15. Then we took the NASA samples and we looked at
*  the ones that were more than 15, less than 15, and we gave them back to NASA. They're like,
*  oh gosh, yep, dead, living, dead, living. You got it. That's what we found on Earth.
*  That's a success.
*  Yeah. Oh yeah. Resounding success.
*  Can you just go back to the beer and the E. coli? What's the assembly index on those?
*  So what you were able to do is like the assembly index of, we found high assembly index molecules
*  originating from the beer sample and the E. coli sample.
*  I didn't know which one was higher. We wouldn't really do any detail there because
*  now we are doing that because one of the things we've done, it's a secret, but I can tell you.
*  Nobody's listening.
*  Is that we've just mapped the tree of life using assembly theory because everyone said that you
*  can't do it from biology. What we were able to do is, I think there's three ways, two ways of doing
*  tree of life traffic. Well, three ways actually.
*  What's the tree of life?
*  The tree of life is basically tracing back the history of life on Earth, all the different
*  species going back, who evolved from what. It all goes all the way back to the first
*  life forms and they branch off. You have plant kingdom, the animal kingdom, the fungi kingdom,
*  and different branches all the way up. The way this was classically done, and I'm no
*  evolutionary biologist, the evolutionary biologists tell me every day at least 10 times.
*  I want to be one though. I kind of like biology. It's kind of cool.
*  Yeah, it's very cool.
*  What Darwin and Mendeleev and all these people do is just they draw pictures.
*  They tax it. They were able to draw pictures and say, oh, these look like common classes.
*  They're artists really.
*  They were able to find out a lot in looking at vertebrates, invertebrates,
*  camera and explosion, all this stuff. Then came the genomic revolution and suddenly everyone used
*  gene sequencing. Craig Venter is a good example. I think he's gone around the world in his yacht
*  just picking up samples, looking for new species, where he's just found new species of life
*  just from sequencing. It's amazing. You have taxonomy. You have sequencing. Then you can also
*  do a little bit of molecular archaeology, like measure the samples and form some inference.
*  What we did is we were able to fingerprint. We took a lot of random samples from all of biology
*  and we used mass spectrometry. What we did now is not just look for individual molecules, but we
*  looked for coexisting molecules where they had to look at their joint assembly space and where we
*  were able to cut them apart and undergo recursion in the mass spec and infer some relationships.
*  We were able to recapitulate the tree of life using mass spectroscopy. No sequencing and no drawing.
*  All right. Can you try to say that again with a little more detail? What does it take to recreate
*  the tree of life? What does the reverse engineering process look like here?
*  What you do is you take an unknown sample, you put it into the mass spec.
*  This comes from what you asked me, what do you see in E. coli? In E. coli, you don't just see,
*  it's not that the most sophisticated cells on Earth make the most sophisticated molecules.
*  It is the coexistence of lots of complex molecules above a threshold. What we realized is you could
*  fingerprint different life forms. Fungi make really complicated molecules. Why? Because they can't
*  move. They have to make everything on site. Whereas some animals are lazy. They can just
*  go eat the fungi. They don't need to make very much. What you do is you look at the... You take,
*  the fingerprint, maybe the top number of high molecular weight molecules you find in the sample,
*  you fragment them to get their assembly indices. Then what you can do is you can infer
*  common origins of molecules. You can do a molecular... When the reverse engineering of
*  the assembly space, you can infer common roots and look at what's called the joint assembly space.
*  But let's translate that into the experiment. Take a sample, bung it in the mass spec,
*  take the top say 10 molecules, fragment them, and that gives you one fingerprint.
*  Then you do it for another sample, you get another fingerprint. Now the question is you say,
*  hey, are these samples the same or different? That's what we've been able to do.
*  By basically looking at the assembly space these molecules create,
*  without any knowledge of assembly theory, you are unable to do it.
*  With a knowledge of assembly theory, you can reconstruct the tree.
*  How does knowing if they're the same or different give you the tree?
*  Let's go to two leaves on different branches on the tree. What you can do by counting the
*  number of differences, you can estimate how far away their origin was. That's all we do.
*  And it just works. But when we realized you could even use assembly theory to
*  recapitulate the tree of life with no gene sequencing, we were like, huh.
*  So this is looking at samples that exist today in the world. What about things that are no longer
*  exist? I mean, the tree contains information about the past. Some of it is gone.
*  Yeah, absolutely. I would love to get old fossil samples and apply assembly theory, mass spec,
*  and see if we can find new forms of life that are no longer amenable to gene sequencing because the
*  DNA is all gone. Because DNA and RNA is quite unstable. But some of them are complex molecules
*  might be there. I might give you a hint something new. Or wouldn't it be great if you find a sample
*  that's worth really persevering and doing the proper extraction to PCR and so on and then
*  sequence it and then put it together. So when a thing dies, you can still get
*  some information about its complexity. Yeah. And it appears that you can
*  do some dating. Now, there are really good techniques. There's radiocarbon dating. There
*  is longer dating going looking at radioactive minerals and so on. And you can also in bone,
*  you can look at what happens after something dies. You get what's called rassomization where the
*  chirality in the polymers basically changes and you get decomposition. And the rate of
*  the deviation from the pure enantiomer to the mixture, it gives you a time
*  time scale on it, half life. So you can date when it died. I want to use assembly theory to
*  see if I can use it, date death and things and trace the tree of life and also decomposition
*  of molecules. Do you think it's possible? Oh yeah, without a doubt. It may not be better than
*  what, because I was just at a conference where some brilliant people were looking at isotope
*  enrichment and looking at how life enriches isotopes and they're really sophisticated stuff
*  that they're doing. But I think there's some fun to be had there because it gives you another
*  dimension of dating. How old is this molecule in terms of, or more importantly, how long ago
*  was this molecule produced by life? The more complex the molecule, the more prospect for
*  decomposition, oxidation, reorganization, loss of chirality and all that jazz. But what life also
*  does is it enriches, as you get older, the amount of carbon-13 in you goes up because of the way
*  the bonding is in carbon-13. So it has a slightly different bond strength and it's called a kinetic
*  isotope effect. So you can literally date how old you are or when you stop metabolizing. So you
*  could date someone's death, how old they are, I think. I'm making this up. This might be right.
*  But I think it's roughly right. The amount of carbon-13 you have in you,
*  you can estimate how old you are. How old living organs, humans are?
*  Yeah, yeah. You could say, oh, this person is 10 years old and this person is 30 years old
*  because they've been metabolizing more carbon and they've accumulated it. That's the basic idea.
*  It's probably completely wrong time scale. Signatures of chemistry are fascinating.
*  So you've been saying a lot of chemistry examples for assembly theory. What if we zoom out and look
*  at a bigger scale of an object, like really complex objects like humans or living organisms
*  that are made up of millions or billions of other organisms? How do you try to apply assembly
*  theory to that? At the moment, we should be able to do this to morphology in cells. So we're looking
*  at cell surfaces and really trying to extend further. It's just that we work so hard to get
*  this paper out and people to start discussing the ideas. But it's kind of funny because I think the
*  penny is falling on this. What does that even mean? What does it mean for a penny to be falling?
*  The penny's dropped because a lot of people are like, it's rubbish, it's rubbish. You've insulted
*  me. It's wrong. The paper got published on the 4th of October. It had 2.3 million engagements on
*  Twitter and has been downloaded over a few hundred thousand times. Someone actually wrote to me and
*  said, this is an example of really bad writing and what not to do. I was like, if all of my papers
*  got read this much, because that's the objective of I have a publishing a paper on people to read
*  it, I want to write that badly again. I don't know what's the deep insight here about the
*  negativity in the space. I think it's probably the immune system of the scientific community
*  making sure that there's no bullshit that gets published. It can overfire, it can do a lot of
*  damage, it can shut down conversations in a way that's not productive. I'll go back, I mean,
*  I'll answer your question about the hierarchy in assembly, but let's go back to the perception.
*  People saying the paper was badly written, I mean, of course we could improve it. We could
*  always improve the clarity. Let's go there before we go to the hierarchy. It has been criticized
*  quite a bit, the paper. What has been some criticism that you found most powerful,
*  that you can understand and can you explain it? Yes, the most exciting criticism came from the
*  evolutionary biologists telling me that they thought that origin of life was a solved problem.
*  I was like, whoa, we're really onto something because it's clearly not. When you poked them
*  on that, they just said, no, you don't understand evolution. I said, no, no, I don't think you
*  understand that evolution had to occur before biology and there's a gap. That was really,
*  for me, that misunderstanding and that did cause an immune response, which was really interesting.
*  The second thing was the fact that physicists were actually really polite,
*  really nice about it, but they just said, we're not really sure about the initial conditions thing,
*  but this is a really big debate that we should certainly get into because the emergence of life
*  was not encoded in the initial conditions of the universe. I think assembly theory shows why it
*  can't be. Sure, if you could say that again. The emergence of life was not and cannot in principle
*  be encoded in the initial conditions of the universe. Just to clarify what I mean by life
*  is like what high assembly index objects? Yeah, and this goes back to your favorite subject.
*  What's that? Time.
*  Right, so why? What does time have to do with it?
*  Probably we can come back to it later, but I think it might be if we have time. I think I now
*  understand how to explain how lots of people got angry with the assembly paper, but also the
*  ramifications of this is how time is fundamental in the universe and this notion of commentarial
*  spaces. There are so many layers on this, but I think you have to become an intuitionist
*  mathematician and you have to abandon platonic mathematics. Also, platonic mathematics has left
*  physics astray, but there's a lot to unpack there. Platonic mathematics, okay, it's okay.
*  Evolutionary biologists criticize because the origin of life is understood and doesn't require
*  an explanation that involves physics. That's their statement. Well, I mean, I think they said lots of
*  confusing statements. Basically, I realized the evolutionary biology community that were vocal,
*  and some of them were really rude, really spiteful, and needlessly so, right? Because, look,
*  I didn't... People misunderstand publication as well. Some of the people have said,
*  how dare this be published in Nature? This is, you know, what a terrible journal.
*  And I said to people, look, this is a brand new idea that's not only potentially going to change
*  the way we look at biology, it's going to change the way we look at the universe. And everyone's
*  like saying, how dare you? How dare you be so grandiose? I'm like, no, no, no, this is not hype.
*  We're not like saying we've invented some, I don't know, we've discovered an alien in a closet
*  somewhere just for hype. We genuinely mean this to genuinely have the impact or ask the question.
*  And the way people jumped on that was a really bad precedent for young people who want to actually
*  do something new, because this makes a bold claim. And the chances are that it's not correct.
*  But what I wanted to do is a couple of things, is I wanted to make a bold claim that was precise
*  and testable and correctable, not a woolly, another woolly information in biology argument,
*  information, Turing machine, blah, blah, blah, blah, blah, a concrete series of statements
*  that can be falsified and explored. And either the theory could be destroyed or built upon.
*  Well, what about the criticism of you're just putting a bunch of sexy names on something
*  that's already obvious? Yeah, that's really good. So the assembly index of a molecule is not obvious,
*  no one had measured it before. And no one has thought to quantify selection,
*  complexity and copy number before in such a primitive, quantifiable way. I think the nice
*  thing about this paper, this paper is a tribute to all the people that understand that biology
*  does something very interesting. Some people call it negentropy, some people call it think about
*  organizational principles, that lots of people were not shocked by the paper because they'd done it
*  before. A lot of the arguments we got, some people said, oh, it's rubbish. Oh, by the way,
*  I had this idea 20 years before. I was like, which one? Is it the rubbish part or the really
*  revolutionary part? So this kind of plucked two strings at once. There is something interesting
*  that biology is as we can see around this, but we haven't quantified yet. And what this is,
*  the first stab at quantifying that. So the fact that people said, this is obvious, but it's also,
*  so if it's obvious, why have you not done it? Sure, but there's a few things to say there.
*  One is, this is in part of a philosophical framework because it's not like you can apply
*  this generally to any object in the universe. It's very chemistry focused. Yeah, well, I think
*  you will be able to, we just haven't got there robustly. So if we can say, how can we, let's go
*  up a level. So if we go up from level, let's go up from molecules to cells, because you jump to people
*  and I jumped from motorcons and both are good and they will be assemblers.
*  So if we go from molecules to assemblies, and let's take a cellar assembly, a nice thing about a cell
*  is you can tell the difference between a eukaryote and a prokaryote. The organelles
*  are specialized differently. When they look at the cell surface, the cell surface has different
*  glycosylation patterns and these cells will stick together. Now let's go up a level with
*  multicellular creatures. You have cellular differentiation. Now, if you think about how
*  embryos develop, you go all the way back, those cells undergo differentiation in a causal way
*  that's biomechanically a feedback between the genetics and biomechanics. I think we can use
*  assembly theory to apply to tissue types. We can even apply it to different cell disease types.
*  So that's what we're doing next. But we're trying to walk, you know, the thing is I'm trying to
*  leap ahead. I want to leap ahead to go, well, we apply it to culture. Clearly you can apply it to
*  memes and culture. And we've also applied assembly theory to CAs. And not as you think.
*  Cellular automata.
*  Yeah, yeah. Not just as you think. Different CA rules were invented by different people
*  at different times. And one of my coworkers, very talented chap, basically was like, oh,
*  I can realize that different people had different ideas or different rules and they copied each
*  other and made slightly different cellular automata rules and looked at them online.
*  And so he was able to refer an assembly index and copy number of rule whatever doing this thing.
*  But I digress. But it does show you can apply it at a higher scale. So what do we need to do to
*  apply assembly theory to things? We need to agree there's a common set of building blocks. So in a
*  cell, well, in a multi-cellular creature, you need to look back in time. So there is the initial
*  cell, which the creature is fertilized and then starts to grow. And then there is cell differentiation
*  and you have to then make that causal chain both on those. That requires
*  development of the organism in time. Or if you look at the cell surfaces and the cell types,
*  they've got different features on the cell, what's the walls and inside the cell. So we're building
*  up. But obviously, I want a leap to things like emoticons, language, mathematical theory.
*  But that's a very large number of steps to get from a molecule to the human brain.
*  And I think they are related, but in hierarchies of emergence. So you shouldn't compare them.
*  The assembly index of a human brain, what does that even mean? Well, maybe we can look at the
*  morphology of the human brain, say all human brains have these number of features in common.
*  If they have those numbers, and then let's look at a brain in a whale or a dolphin or a chimpanzee
*  or a bird and say, okay, let's look at the assembly indices, number of features in these.
*  And now the copy number is just a number of how many birds are there? How many chimpanzees are
*  there? How many humans are there? Then you have to discover for that, the features that you would
*  be looking for. Yeah. And that means you need to have some idea of the anatomy. Is there an
*  automated way to discover features? I guess so. I mean, and I think this is a good way to apply
*  machine learning and image recognition to basically characterize things. To apply
*  compression to it to see what emerges and then use the thing, the features used as part of the
*  compression as the measurement of, as the thing that is searched for when you're measuring assembly
*  index and copy number. And the compression has to be, remember the assembly universe,
*  which is you have to go from assembly possible to assembly contingent. And that jump from,
*  because assembly possible, all possible brains, all possible features all the time. But we know
*  that on the tree of life and also on the lineage of life, going back to Luca, the human brain
*  just didn't spring into existence yesterday. It is a long lineage of brains going all the way back.
*  And so if we could do assembly theory to understand the development, not just in evolutionary history,
*  but in biological development as you grow, we are going to learn something more.
*  What would be amazing is if you can use assembly theory, this framework to show the increase in
*  the assembly index associated with, I don't know, cultures or pieces of text like language or
*  images and so on, and illustrate without knowing the data ahead of time, just kind of like you did
*  with NASA, that you were able to demonstrate that it applies in those other contexts. I mean,
*  and that probably wouldn't at first, and you have to evolve the theory somehow,
*  you have to change it, you have to expand it. I think so. But like that, I guess this is as a
*  paper, a first step in saying, okay, can we create a general framework for measuring complexity
*  of objects, for measuring life, the complexity of living organisms?
*  Yeah.
*  That's what this is reaching for.
*  That is the first step. And also to say, look, we have a way of quantifying selection and evolution
*  in a fairly, not mundane, but a fairly mechanical way. Because before now, the ground truth for it
*  was very subjective. Whereas here, we're talking about clean observables. And there's going to be
*  layers on that. I mean, with collaborators right now, we already think we can do assembly theory
*  on language. And not only that, wouldn't it be great if we can figure out how under pressure
*  language is going to evolve and be more efficient, because you're going to want to transmit things.
*  And again, it's not just about compression. It is about understanding how you can make the most of
*  the architecture you've already built. And I think this is something beautiful that evolution does.
*  We're reusing those architectures. We can't just abandon our evolutionary history.
*  And if you don't want to abandon your evolutionary history, and you know that evolution has been
*  happening, then assembly theory works. And I think that's a key comment I want to make is that
*  assembly theory is great for understanding where evolution has been used. The next jump
*  is when we go to technology. Because of course, if you take the M3 processor,
*  I want to buy it. I haven't bought one yet. I can't justify it, but I want it at some point.
*  The M3 processor, arguably, there's quite a lot of features, a quite large number.
*  The M2 came before it, then the M1 all the way back. You can apply assembly theory to
*  microprocessor architecture. It doesn't take a huge leap to see that.
*  I'm a Linux guy, by the way. So your examples go way over my head.
*  Well, whatever.
*  Is that like a fruit company of some sort? I don't even know.
*  Yeah, there's a lot of interesting stuff to ask about language. Like you could look at,
*  how would that work? You could look at GPT-1, GPT-2, GPT-3, 3, 5, 4, and try to analyze the kind of
*  language it produces. I mean, that's almost trying to look at assembly index of intelligent systems.
*  Yeah, I mean, I think the thing about large language models, and this is a whole hobby
*  horse I have at the moment, is that obviously they're all about the evidence of evolution
*  in the large language model comes from all the people that produced all the language.
*  That's really interesting, and all the corrections in the mechanical Turk.
*  That's part of the history, part of the memory of the system.
*  Exactly. So it would be really interesting to basically use an assembly-based approach to
*  making language in a hierarchy. My guess is that we might be able to build a new type of large
*  language model that uses assembly theory that has more understanding of the past and how things were
*  created. Basically, the thing with LLMs is they're like everything, everywhere, all at once,
*  splat and make the user happy. So there's not much intelligence in the model. The model is how the
*  human interacts with the model, but wouldn't it be great if we could understand how to embed more
*  intelligence in the system? What do you mean by intelligence there? Like you seem to associate
*  intelligence with history. Yeah, well, I think selection produces intelligence.
*  You're almost implying that selection is intelligence? No.
*  Kind of. I would go out and live and say that, but I think it's a little bit more. Human beings have
*  the ability to abstract, and they can break beyond selection. This is like Darwinian selection,
*  because a human being doesn't have to basically do trial and error.
*  They can think about it and say, oh, that's a bad idea. We'll do that, and then technologies and so
*  on. So we escaped Darwinian evolution, and now we're onto some other kind of evolution, I guess.
*  Higher, higher level. And assembly theory will measure that as well, right? Because it's all a
*  lineage. Okay. Another piece of criticism, or by way of question, is how is assembly theory,
*  or maybe assembly index, different from comagraph complexity? So for people who don't know,
*  comagraph complexity of an object is the length of a shortest computer program that produces the
*  object as output. Yeah, there seems to be a disconnect between the computational approach.
*  So yeah, so a comagraph measure requires a Turing machine, requires a computer, and that's one thing.
*  And the other thing is assembly theory is supposed to trace the process by which life
*  evolution emerged. There's a main thing there. There are lots of other layers. So
*  comagraph complexity, you can approximate comagraph complexity, but it's not really telling you very
*  much about the actual, it's really telling you about like your data set, compression of your data
*  set. And so that doesn't really help you identify the turtle, in this case, is the computer.
*  And so what assembly theory does is, I'm going to say, it's a trigger warning for anyone listening
*  who loves complexity theory, I think that we're going to show that AIT is a very important subset
*  of assembly theory, because here's what happens. I think that assembly theory allows us to build,
*  understand when we're selections occurring, selection produces factories and things,
*  factories in the end produce computers, and you can go, then algorithmic information theory comes
*  out of that. The frustration I've had with looking at life through this kind of information theory is
*  it doesn't take into account causation. So the main difference between assembly theory and all
*  these complexity measures is there's no causal chain. And I think that's the main-
*  That's the causal chain is at the core of assembly theory.
*  Exactly. And if you've got all your data in a computer memory, all the data is the same,
*  you can access it in the same way. You don't care, you just compress it and you either look
*  at the program runtime or the shortest program. And that, for me, is absolutely
*  not capturing what it is, what its selection does.
*  But assembly theory looks at objects, it doesn't have information about
*  the object history, it's going to try to infer that history by looking for the shortest history.
*  The object doesn't have a Wikipedia page that goes with it.
*  Oh, I would say it does in a way, and it is fascinating to look at. So you've just got the
*  objects and you have no other information about the object. What assembly theory allows you to do
*  with just with the object is to- and the word infer is correct, I agree with infer. You say,
*  well, that's not the history, but something really interesting comes from this. The shortest path
*  is inferred from the object. That is the worst case scenario if you have no machine to make it.
*  So that tells you about the depth of that object in time. And so what assembly theory allows you
*  to do is without considering any other circumstances to say from this object, how deep is this object in
*  time if we just treat the object as itself without any other constraints. And that's super powerful
*  because the shortest path then allows you to say, oh, this object wasn't just created randomly,
*  there was a process. And so assembly theory is not meant to one-up AIT or to ignore the factory.
*  It's just to say, hey, there was a factory. How big was that factory and how deep in time is it?
*  But it's still computationally very difficult to compute that history for complex objects.
*  It is and becomes harder. But one of the things that's super nice is that it constrains your
*  initial conditions. It constrains where you're going to be. So if you take, say, imagine,
*  so one of the things we're doing right now is applying assembly theory to drug discovery.
*  Now, what everyone's doing right now is taking all the proteins and looking at the proteins and
*  looking at molecules, Dr. Proteins. Why not instead look at the molecules that are involved in
*  interacting with the receptors over time rather than thinking about and use the molecules evolve
*  over time as a proxy for how the proteins evolved over time and then use that to constrain your drug
*  discovery process. You flip the problem 180 and focus on the molecule evolution rather than the
*  protein. And so you can guess in the future what might happen. So that so that so you rather than
*  having to consider all possible molecules, you know where to focus. And that's the same thing
*  if you're looking at in assembly spaces for an object where you don't know the entire history,
*  but you know that, you know, in the history of this object is not going to have some other motif
*  that there that it doesn't apply. It doesn't appear in the past.
*  But just even for the drug discovery point you made,
*  don't you have to simulate all of chemistry for to figure out how to come up with constraints?
*  No.
*  The molecules and the
*  No.
*  I mean, I don't I don't know enough about proteins.
*  Well, this is another thing that I think causes because this paper goes across so many boundaries.
*  So chemists have looked at this and said, this is not a this is not a react. This is
*  not correct reaction. It's like, no, it's a graph.
*  Sure, there's there's a assembly index and shortest path examples here on chemistry.
*  Yeah. And so what you do is you look at the minimal constraints on that graph.
*  Of course, it has some mapping to the synthesis. But actually, you don't have to know all of
*  chemistry, you just have to understand you can build up the constraint space rather nicely.
*  But this is just at the beginning, right? There are so many directions this could go in.
*  It could all be wrong, but hopefully it's less wrong.
*  What about the little criticism I saw of do you
*  by way of question, do you consider the different probabilities of each reaction in the chain?
*  So like that there could be different.
*  When you look at a chain of events that led up to the creation of an object,
*  doesn't it matter that some parts in the chain are less likely than others?
*  No.
*  It doesn't matter.
*  Well, let's go back. So no, not less likely, but react. So,
*  no. So let's go back to what we're looking at. So the assembly index is the minimal path
*  that could have created that object probabilistically. So imagine you have
*  all your atoms in a plasma, you've got enough energy, you've got enough collisions. What is
*  the quickest way you could zip out that molecule with no reaction constraints?
*  How do you define quickest there then?
*  It's just basically what walk on a random graph. So we make an assumption that basically
*  the time scale for forming the bonds. So no, I don't want to say that because it's going to
*  have people getting obsessing about this point and your criticism is really good one.
*  What we're trying to say is like, this puts a lower bound on something. Of course,
*  some reactions are less possible than others, but actually I don't think chemical reactions exist.
*  Oh boy. What does that mean? Why don't chemical reactions exist?
*  I'm writing a paper right now that I keep being told I have to finish and it's called
*  The Origin of Chemical Reactions. And it merely says that reactivity exists as controlled by the
*  laws of quantum mechanics and chemists put names on reactions. So you could have like,
*  I don't know, the Wittich reaction, which is by Wittich. You could have the Suzuki reaction,
*  which is by Suzuki. Now, what are these reactions? So these reactions are constrained by the
*  following. They're constrained by the fact they're on planet earth, 1G, 298 Kelvin, one bar.
*  So these are constraints. They're also constrained by the chemical composition of earth, oxygen,
*  availability, all this stuff. And that then allows us to focus in our chemistry. So when a chemist
*  does a reaction, that's a really nice compressed shorthand for constraint application, glass flask,
*  pure reagent, temperature, pressure, bomb, bomb, bomb, bomb, bomb, control, control, control,
*  control. So of course, we have bond energies. So the bond energies are kind of intrinsic in a vacuum.
*  So the bond energy, you have to have a bond. And so for assembly theory to work, you have to have
*  a bond, which means that bond has to give the molecule certain life, a half life. So you're
*  probably going to find later on that some bonds are weaker, and that you are going to miss in mass
*  spectra. When you count, look at the assembly of some molecules, you're going to miscount the
*  assembly of the molecule because it falls apart too quickly because the bonds just fall. But you
*  can solve that with looking at infrared. So when people think about the probability, they're kind
*  of misunderstanding. Assembly theory says nothing about the chemistry, because chemistry is chemistry,
*  and the constraints are put in by biology. There was no chemist in the origin of life,
*  unless you believe in the chemist in the sky. And they were, you know, it's like Santa Claus,
*  they had a lot of work to do. But chemical reactions do not exist in the constraints that
*  allow chemical transformations to occur do exist. Okay, so it's constraint application. So there's
*  no chemical reactions. It's all constraint application, which enables the emergence
*  of react. What's a different word for chemical reaction? Transformation. Transformation. Yeah,
*  like a function. It's a function. But no, but I love chemical reactions in the shorthand. And
*  so the chemists don't all go mad. I mean, of course, chemical reactions exist on Earth.
*  It's a shorthand for these constraints. Right. So assuming all these constraints that we've been
*  using for so long, we just assume that that's always the case in natural language conversation.
*  Exactly. And the grammar of chemistry, of course, emerges in reactions, and we can use them reliably.
*  But I do not think the Wittek reaction is accessible on Venus. Right. And this is useful
*  to remember, you know, to frame it as constraint application is useful for when you zoom out to the
*  bigger picture of the universe and looking at the chemistry of the universe and then starting
*  to apply assembly theory. That's interesting. That's really interesting. But we've also pissed
*  off the chemists now. Oh, okay. That's pretty happy. But well, most of them. Everybody,
*  everybody deep down is happy. I think they're just sometimes feisty. That's how they show.
*  That's how they have fun. Everyone is grumpy on some days when you challenge the problem with
*  this paper. It's almost like I went to a party. It's like you used to do this occasionally when
*  I was young. Go to a meeting and just find a way to offend everyone at the meeting simultaneously.
*  Even the factions that don't like each other, they're all unified in their hatred of you just
*  offending them. This paper, it feels like the person that went to the party and offended
*  everyone simultaneously, so stop fighting with themselves and just focused on this paper.
*  Maybe just a little insider, interesting information. What were the editors of Nissur,
*  the reviews and so on, how difficult was that process? This is a pretty big paper.
*  When we originally sent the paper, we sent the paper and the editor said,
*  this is quite a long process. We sent the paper and the editor gave us some feedback
*  and said, I don't think it's that interesting. It's hard. It's a hard concept. The editor gave
*  us some feedback and Sarah and I took a year to rewrite the paper. Was the nature of the feedback
*  very specific on this part, this part, or was it like, what are you guys smoking?
*  Yeah, it was kind of the latter, what are you smoking?
*  But polite and there's promise.
*  Yeah. The thing is, the editor was really critical, but in a really professional way.
*  I mean, for me, this was the way science should happen. When it came back, we had too many
*  equations in the paper. If you look at the preprint, they're just equations everywhere,
*  23 equations. When I said to Abhishek, who was the first author, we've got to remove all the
*  equations. But my assembly equations thing, Abhishek was like, no, we can't. I said, well,
*  look, if we want to explain this to people, it's a real challenge. Sarah and I went through the,
*  I think it was actually 160 versions of the paper, but we basically got to version 40 or something.
*  We said, right, zero, let's start again. We wrote the whole paper again. We knew the entire-
*  Amazing.
*  And we just went bit by bit by bit and said, what is it we want to say? And then we sent the paper
*  in and to ask, we expected it to be rejected and not even go to review. And then we got notification
*  back, it had gone to review and we were like, oh my God, it's so going to get rejected. How's
*  it going to get rejected? Because the first assembly paper that on the mass spec we sent to
*  nature got, went through six rounds of review and rejected. Right. And there's biochemist just said,
*  I don't believe you, you must be committing fraud. Long story, probably a boring story.
*  But in this case, it went out to review, the comments came back and the comments were
*  incredibly, there were very deep comments from all the reviewers. There were,
*  but the nice thing was the reviewers were kind of very critical, but not dismissive. They were
*  like, oh really? Explain this, explain this, explain this, explain this. Are you sure it's
*  not common goller off? Are you sure it's not this? And we went through, I think three rounds of review
*  pretty quick. And the editor went, yeah, it's in.
*  But maybe you could just comment on the whole process. You've published some pretty huge
*  papers on all kinds of topics within chemistry and beyond. Some of them have some little spice in
*  them, a little spice of crazy. Like Tom Way says, I like my town with a little drop of poison.
*  So it's not a mundane paper. So where, what's it like psychologically to go through all this
*  process to keep getting rejected, to get reviews from people that don't get the paper or
*  all that kind of stuff, just from a question of a scientist. Like what is that like?
*  I mean, this paper for me, because this wasn't the first time we tried to publish assembly theory
*  at the highest level. The nature communications paper, we on the mass spec, on the idea,
*  went through, went to nature and got rejected, went through six rounds of review and got rejected.
*  And it's, and I just was so confused when the chemist said, this can't be possible. I do not
*  believe you can measure complexity using mass spec. And also by the way, molecules,
*  complex molecules can randomly form. And we're like, but look at the data, the data says,
*  they said, no, no, we don't believe you. And we went and I just wouldn't give up.
*  The editor and the editor in the end was just like the different editors actually.
*  What's behind that never giving up is like when you're sitting there, 10 o'clock in the evening,
*  there's a melancholy feeling that comes over you. You're like, okay, this is rejection number five.
*  Or it's not rejection, but maybe it feels like a rejection because the comments are
*  that you totally don't get it. Like what gives you strength to keep going there?
*  Yeah, I don't know.
*  I don't normally get emotional about papers, but
*  it's not about giving up because we want to get it published because we want the glory or anything.
*  It's just like, why don't you understand? And so,
*  so what I did, so what I would just try to be as
*  possible and say, yeah, you didn't like it. Tell me why? And then end.
*  Sorry
*  Hello.
*  Hello.
*  And then, sorry, silly.
*  Never get emotional about papers normally,
*  but I think what we do is you just compress
*  like five years of angst from this.
*  So it's been rough.
*  It's not just rough, it's like, it happened,
*  you know, I came up with the assembly equation,
*  you know, remote from Sarah in Arizona and the people SFI.
*  I felt like I was a mad person, like, you know,
*  the guy depicted in a beautiful mind.
*  He was just like, not the actual genius part,
*  but just the crazy part.
*  Because I kept writing expanded
*  and I have no mathematical ability.
*  Oh, and I was expanding.
*  I was making these mathematical expansions
*  where I kept seeing the same motif again.
*  I was like, oh, I think this is a copy number.
*  The same string is going again and again and again.
*  I couldn't do the math.
*  And then I realized the copy number fell out
*  of the equation and everything collapsed down.
*  I was like, oh, that works kind of.
*  So we submitted the paper.
*  And then when it was almost accepted, right,
*  the mass spec one, and it was astrobiologist,
*  a great, you know, mass spectroscopist,
*  a great and the chemist went nonsense,
*  like biggest pile of nonsense ever fraud, you know?
*  And I was like, but why fraud?
*  And they just said, just because.
*  And I was like, well, and so, and I could not convince
*  the editor in this case, the editor was just so pissed off
*  because they see it as like a kind of, you know,
*  you're wasting my time and I would not give up.
*  I wrote, I went and dissected, you know, all the parts.
*  And I think, although, I mean, I got upset about it,
*  you know, it was kind of embarrassing actually,
*  but I guess.
*  Beautiful.
*  But it was just trying to understand
*  why they didn't like it.
*  So they were part of me was like really devastated
*  and a part of me was super excited because I'm like,
*  huh, they can't tell me why I'm wrong.
*  And this kind of goes back to, you know,
*  when I was at school, I was in a kind of learning
*  difficulties class and I kept going to the teacher
*  and say, you know, how, what do I do today
*  to prove I'm smart?
*  And they were like, nothing, you can't.
*  I was like, give me a job, you know,
*  give me something to do, give me a job to do,
*  something to do as we, and I kind of felt like that a bit
*  when I was arguing with the, and not arguing,
*  there was no ad hominem, I wasn't telling the editor,
*  they were idiots or anything like this,
*  or the reviewers, I kept it strictly like factual.
*  And all I did is I just kept knocking it down
*  bit by bit by bit by bit by bit.
*  It was ultimately rejected and it got published elsewhere.
*  And then the actual experimental data.
*  So this is kind of, in this paper,
*  the experimental justification was already published.
*  So when we did this one and we went through the versions
*  and then we sent it in,
*  and in the end it just got accepted.
*  We were like, well, that's kind of cool, right?
*  This is kind of like, you know, some days you have,
*  you know, the student, sorry, the first author was like,
*  I can't believe it got accepted, like, nor am I.
*  But it's great, it's like, it's good.
*  And then when the paper was published,
*  I was not expecting the backlash.
*  I was expecting computational,
*  well, no, actually I was just expecting one person
*  who'd been trolling me for a while about it,
*  just to carry on trolling,
*  but I didn't expect the backlash.
*  And then I wrote to the editor and apologized.
*  And the editor was like,
*  what are you apologizing for?
*  It was a great paper.
*  Of course it's gonna get backlash.
*  You said some controversial stuff, but it's awesome.
*  I think it's a beautiful story of perseverance.
*  And the backlash is just a negative word for discourse,
*  which I think is beautiful.
*  I think you, as I said to, you know,
*  when it got accepted and people were saying,
*  we're kind of like hacking on it.
*  And I was like, papers are not gold medals.
*  The reason I wanted to publish that paper in nature
*  is because it says, hey,
*  there's something before biological evolution.
*  You have to have that if you're not a creationist,
*  by the way, this is an approach.
*  First time someone has put a concrete mechanism or sorry,
*  a concrete quantification.
*  And what comes next you're pushing on is a mechanism.
*  And that's what we need to get to is an autocolletic set,
*  self-replicating molecules, some other features that come in.
*  And the fact that this paper has been so discussed,
*  for me is a dream come true.
*  Like it doesn't get better than that.
*  If you can't accept a few people hating it.
*  And the nice thing is, the thing that really makes me happy
*  is that no one has attacked the actual physical content.
*  You can measure the assembly index,
*  you can measure selection now.
*  So either that's right or it's, well,
*  either that's helpful or unhelpful.
*  If it's unhelpful, this paper will sink down
*  and no one will use it again.
*  If it's helpful, it'll help people build scaffold on it
*  and we'll start to converge to a new paradigm.
*  So I think that that's the thing that I wanted to see,
*  my colleagues, authors, collaborators,
*  and people who are like,
*  you've just published this paper, you're a chemist.
*  Why have you done this?
*  Like, who are you to be doing evolutionary theory?
*  Like, well, I don't know.
*  I mean, sorry, did I need to get-
*  Who is anyone to do anything?
*  Well, I'm glad you did.
*  Let me just before coming back to origin of life
*  and these kinds of questions,
*  you mentioned learning difficulties.
*  I didn't know about this.
*  So what was it like?
*  I wasn't very good at school, right?
*  This is when you were very young?
*  Yeah, yeah, but in primary school,
*  my handwriting was really poor
*  and apparently I couldn't read
*  and my mathematics was very poor.
*  So they just said, this is a problem.
*  They identified it.
*  My parents kind of at the time were confused
*  because I was busy taking things apart,
*  buying electronic junk from the shop,
*  trying to build computers and things.
*  And then once I got out of,
*  when I was, I think about the major transition
*  in my stupidity, like, you know,
*  everyone thought I wasn't that stupid when I was,
*  basically everyone thought I was faking,
*  I like stuff and I was faking wanting to be it.
*  So I always want to be a scientist.
*  So five, six, seven years old,
*  I'll be a scientist, take things apart.
*  And everyone's like,
*  yeah, this guy wants to be a scientist,
*  but he's an idiot.
*  Mm-hmm.
*  And so everyone was really confused,
*  I think at first,
*  that I wasn't smarter than I was claiming to be.
*  And then I just basically didn't do well in the test.
*  I went down and down and down and down.
*  And then, and I was kind of like,
*  huh, this is really embarrassing.
*  I really like maths and everyone says I can't do it.
*  I really like kind of, you know, physics and chemistry
*  and all that and science.
*  And people say, you can't read and write.
*  And so I found myself in a learning difficulties class
*  at the end of primary school
*  and the beginning of secondary school in the UK.
*  Secondary school is like 11, 12 years old.
*  And I remember being put in the remedial class
*  and the remedial class was basically full of,
*  well, two types, three types of people.
*  There were people that had quite violent, right?
*  Yeah.
*  And there were people who couldn't speak English
*  and there were people that really had learning difficulties.
*  So...
*  The one thing I can objectively remember was,
*  I mean, I could read.
*  I like reading.
*  I read a lot.
*  But something in me, I'm a bit of a rebel.
*  I refused to read while I was told to read.
*  And I found it difficult to read individual words
*  in the way they were told.
*  But anyway, I got caught one day teaching someone else
*  how to read and I was like,
*  anyway, I got caught one day teaching someone else to read
*  and they said, okay, we don't understand this.
*  I always knew what to be a scientist
*  but didn't really know what that meant.
*  And I realized you had to go to university
*  and I thought I can just go to university.
*  It's like curious people like, no, no, no,
*  you need to have these,
*  you have to be able to enter these exams
*  to get this grade point average.
*  And the fact is the exams you've been entered into,
*  you're just gonna get C, D or E.
*  You can't even get A, B or C, right?
*  This is the UK GCSEs.
*  I was like, oh shit.
*  And I said, can you just put me into the higher exams?
*  They said, no, no, you're gonna fail.
*  There's no chance.
*  So my father kind of intervened and said,
*  just let him go in the exams.
*  And they said, he's definitely gonna fail.
*  It's a waste of time, waste of money.
*  And he said, well, what if we paid?
*  So they said, well, okay.
*  So you didn't actually have to pay.
*  I had to pay if I failed.
*  So I took the exams and passed them, fortunately.
*  I didn't get the top grades, but I got into A levels.
*  But then that also kind of limited
*  what I could do at A levels.
*  I wasn't allowed to do A level maths.
*  What do you mean you weren't allowed to?
*  Because I had such a bad math grade from my GCSE,
*  I only had a C,
*  but they wouldn't let me go into the ABC for maths
*  because of some kind of coursework requirement back then.
*  So the top grade I could have got was a C,
*  so C, D or E.
*  So I got a C, and they let me do kind of A S level maths,
*  which is the half intermediate, but I get to go to university.
*  But in the arc of light chemistry,
*  I had a good chemistry teacher.
*  So in the end, I got to university to do chemistry.
*  So through that kind of process,
*  I think for kids in that situation,
*  it's easy to start believing that you're not,
*  well, how do I put it?
*  That you're stupid and basically give up,
*  that you're just not good at math,
*  you're not good at school.
*  So this is by way of advice for people,
*  for interesting people,
*  for interesting young kids right now
*  experiencing the same thing.
*  Where was the place,
*  what was the source of you not giving up there?
*  I have no idea other than,
*  I was really, I really like not understanding stuff.
*  For me, when I not understand something,
*  I didn't understand,
*  feel like I don't understand anything,
*  but now, but back then I was so,
*  I remember when I was like, I don't know,
*  I tried to build a laser when I was like eight.
*  And I thought, how hard could it be?
*  And I basically, I was gonna build a CO2 laser.
*  I was like, right,
*  I think I need some partially coated mirrors
*  and need some carbon dioxide
*  and I need a high voltage.
*  So I kind of, and I was like,
*  I didn't have a,
*  and I was so stupid, right?
*  I was kind of so embarrassed.
*  I had to make enough CO2,
*  I actually set a fire and try to filter the flame.
*  Oh, nice.
*  To crap enough CO2.
*  And I was like, completely failed
*  and I burnt half the garage down.
*  So my parents were not very happy about that.
*  But so that was one thing.
*  I was like, I really like first principle thinking.
*  And so, you know,
*  so I remember being super curious
*  and being determined to find answers.
*  And so the kind of, when people do give advice about this,
*  well, I asked for advice about this.
*  I don't really have that much advice
*  other than don't give up.
*  And one of the things I try to do
*  as a chemistry professor in my group
*  is I hire people that I think that, you know,
*  I'm kind of, who am I, if they're persistent enough,
*  who am I to deny them the chance?
*  Because, you know, people gave me a chance
*  and I was able to do stuff.
*  Do you believe in yourself, essentially?
*  I like, so I love being around smart people
*  and I love confusing smart people.
*  And when I'm confusing smart people,
*  and you know, not by stealing their wallets
*  and hiding it somewhere,
*  but if I can confuse smart people,
*  that is the one piece of hope
*  that I might be doing something interesting.
*  Wow, that's quite brilliant.
*  Like as a gradient to optimize.
*  Hang out with smart people and confuse them.
*  And the more confusing it is,
*  the more there's something there.
*  And as long as they're not telling you
*  just a complete idiot
*  and they give you different reasons.
*  And I mean, I'm, you know, if everyone,
*  it's like with assembly theory and people said,
*  oh, it's wrong.
*  And I was like, why?
*  And they're like,
*  and no one could give me a consistent reason.
*  They said, oh, because it's to be number four
*  or it's just comma, goller off
*  or it's just there, that and the other.
*  So I think the thing that I like to do
*  is in academia, it's hard, right?
*  Cause people are critical,
*  but I mean, you know, the criticism,
*  I mean, although I got kind of upset about it earlier,
*  which is kind of silly, but not silly,
*  because obviously it's hard work being on your own
*  or with a team, spacey separated,
*  like during lockdown and try to keep everyone on board
*  and have some faith that
*  I've always wanted to have a new idea.
*  And so, you know, I like a new idea
*  and I wanna nurture it as long as possible.
*  And if someone can give me actionable criticism,
*  that's why I think I was trying to say earlier
*  when I was kind of like stuck for words,
*  give me actionable criticism, you know, it's wrong.
*  Okay, why is it wrong?
*  So it doesn't, your equation is incorrect for this
*  or your method is wrong.
*  And then so what I try and do is get enough criticism
*  from people to then triangulate and go back.
*  And I've been very fortunate in my life
*  that I've got great colleagues, great collaborators,
*  funders, mentors, and people that will take the time
*  to say, you're wrong because,
*  and then what I have to do is integrate the wrongness
*  and go, oh, cool, maybe I can fix that.
*  And I think criticism is really good.
*  People have a go at me because I'm really critical.
*  I'm like, but I'm not criticizing, you know,
*  you as a person, I'm just criticizing the idea
*  and trying to make it better and say, well, what about this?
*  And, you know, and sometimes I'm kind of, you know,
*  my filters are kind of, you know, truncated in some ways.
*  I'm just like, that's wrong, that's wrong, that's wrong.
*  What did they say?
*  People are like, oh my God, you just told me,
*  you destroyed my life's work.
*  I'm like, relax, no, I'm just like, let's make it better.
*  And I think that we don't do that enough
*  because we're either personally critical,
*  which isn't helpful, or we don't give any criticism at all
*  because we're too scared.
*  Yeah, I've seen you be pretty aggressively critical,
*  but it's, every time I've seen it,
*  it's the idea, not the person.
*  I'm sure I make mistakes on that.
*  I mean, I argue lots with Sarah and she's like,
*  kind of shocked, I've argued with Yashner in the past,
*  and he's like, you're just making Yashner back,
*  and you're like, you're just making that up.
*  I'm like, no, not quite.
*  But kind of.
*  I've had a big argument with Sarah about time,
*  and she's like, no, time doesn't exist.
*  I'm like, no, no, time does exist.
*  And now, as she realized that her conception
*  of assembly theory, and my conception of assembly theory
*  was the same thing, necessitated us to abandon
*  the fact that time is eternal,
*  to actually really fundamentally question
*  how the universe produces combinatorial novelty.
*  So time is fundamental for assembly theory?
*  I'm just trying to figure out
*  where you and Sarah converge.
*  I think assembly theory is fine in this time right now,
*  but I think it helps us understand
*  that something interesting is going on.
*  So there's, and I'm really inspired
*  by a guy called Nick Gizen.
*  I'm gonna butcher his argument,
*  but I love his argument a lot,
*  so I hope he forgives me if he hears about it.
*  But basically, if you want free will,
*  time has to be fundamental.
*  And we can go, and if you want time to be fundamental,
*  you have to give up on platonic mathematics,
*  and you have to use intuition as mathematics.
*  By the way, and again, I'm gonna butcher this,
*  but basically, Hilbert said that infinite numbers
*  are allowed.
*  And I think it was Brouwer said no,
*  you can't, all numbers are finite.
*  So it's kind of like, so let's go back a step,
*  because it was like people gonna say,
*  assembly theory seems to explain
*  that large combinatorial space
*  allows you to produce things like life and technology.
*  And that large combinatorial space is so big,
*  it's not even accessible to a Sean Carroll,
*  David Deutsch multiverse.
*  The physicist saying that all of the universe
*  already exists in time is probably,
*  provably, strong word, not correct.
*  That we are gonna know that the universe as it stands,
*  the present, the way the present builds the future,
*  so big, the universe can't ever contain the future.
*  And this is a really interesting thing.
*  I think Max Tegmark has this mathematical universe,
*  he says, the universe is kind of like a block universe,
*  and I apologize to Max if I'm getting it wrong,
*  but people think you can just move,
*  you have the stat, you have the initial conditions,
*  and you can run the universe right to the end,
*  and go backwards and forwards in that universe.
*  That is not correct.
*  Yeah, let me load that in.
*  The universe is not big enough to contain the future.
*  Yeah, that's why.
*  That's another, that's a beautiful way of saying
*  that time is fundamental.
*  Yes, and that you can have, and that's what,
*  this is why the law of the excluded middle,
*  something is true or false, only works in the past.
*  Is it gonna snow in New York next week, or in Austin?
*  You might, in Austin, say probably not.
*  In New York, you might say yeah.
*  If you go forward to next week and say,
*  did it snow in New York last week, true or false,
*  you can answer that question.
*  The fact that the law of the excluded middle
*  cannot apply to the future
*  explains why time is fundamental.
*  Well, I mean, that's a good example, intuitive example,
*  but it's possible that we might be able to predict,
*  whether it's gonna snow if we had perfect information.
*  I think we,
*  You're saying not.
*  Impossible, impossible.
*  So here's why.
*  I'll make a really quick argument,
*  and this argument isn't mine,
*  it's Nick's and a few other people.
*  Can you explain his view on fundamental,
*  on time being fundamental?
*  Yeah, so I'll give my view,
*  which kind of resonates with his,
*  but basically, it's very simple, actually.
*  It would say that free will,
*  that your ability to design and do an experiment
*  is exercising free will.
*  So he used that thought process,
*  but I never really thought about it that way,
*  and that you actively make decisions.
*  I do think that,
*  I used to think that free will was a kind of consequence
*  of just selection,
*  but I'm kind of understanding that human free will
*  is something really interesting,
*  and he very much inspired me.
*  But I think that,
*  what Sarah Walker said that inspired me as well,
*  that these will converge,
*  is that I think that the universe,
*  and the universe is very big, huge,
*  but actually, the place is largest in the universe right now,
*  the largest place in the universe is Earth.
*  Yeah, I've seen you say that,
*  and boy, does that,
*  that's an interesting one to process.
*  What do you mean by that?
*  Earth is the biggest place in the universe.
*  Because we have this combinatorial scaffolding,
*  going all the way back from Luca,
*  so you've got cells that can self-replicate,
*  and then you go all the way to terraforming the Earth,
*  you've got all these architectures,
*  the amount of selection that's going on,
*  biological selection, just to be clear,
*  biological evolution,
*  and then you have multicellularity,
*  then animals and abstraction,
*  and with abstraction, there was another kick,
*  because you can then build architectures and computers,
*  and cultures and language,
*  and these things are the biggest things
*  that exist in the universe,
*  because we can just build architectures
*  that couldn't naturally arise anywhere,
*  and the further that distance goes in time,
*  and it's just gigantic.
*  And from a complexity perspective.
*  Yeah.
*  Okay, wait a minute, but I mean, I know you're being poetic,
*  but how do you know there's not other Earth-like,
*  like how do you know,
*  you're basically saying Earth is really special,
*  it's awesome stuff as far as we look out,
*  there's nothing like it going on,
*  but how do you know there's not nearly infinite
*  number of places where cool stuff like this is going on?
*  I agree, and I would say,
*  I'll say again that Earth is the most gigantic thing
*  we know in the universe, commentarily, we know.
*  We know.
*  Now, I guess, this is just purely a guess,
*  I have no data, but other than hope,
*  well, maybe not hope, maybe, no, I have some data,
*  that every star in the sky probably has planets,
*  and life is probably emerging on these planets,
*  but the amount of contingency that is associated
*  with the evolution of life is I think the commentorial space
*  associated with these planets is so different,
*  our causal cones are never gonna overlap or not easily,
*  and this is the thing that makes me sad about alien life,
*  why it's why we have to create alien life in the lab
*  as quickly as possible, because I don't know
*  if we are gonna be able to build architectures
*  intersect with alien intelligence and architectures.
*  And intersect, you know what I mean, in time or space?
*  Time and the ability to communicate.
*  The ability to communicate.
*  Yeah, my biggest fear in a way is that life is everywhere,
*  but we become infinitely more lonely
*  because of our scaffolding in that commentorial space,
*  because it's so big.
*  And because-
*  So you're saying the constraints created by the environment
*  that led to the factory of Darwinian evolution
*  are just like this little tiny cone
*  in a nearly infinite commentorial space.
*  Exactly.
*  And so there's other cones like it,
*  and why can't we communicate with other,
*  like just because we can't create it
*  doesn't mean we can't appreciate the creation, right?
*  Like that, sorry, detect the creation.
*  I truly don't know, but it's an excuse for me
*  to ask for people to give me money
*  to make a planet simulator.
*  Yeah, right.
*  If I can make-
*  With a different kind of-
*  Like another shameless, like give me money, I need money.
*  This was all a long plug for a planet simulator.
*  It's like, you know-
*  Hey, I won't be the first in line to do it.
*  My Rick garage has run out of room, you know?
*  No.
*  And is this a planet simulator,
*  you mean like a different kind of planet?
*  Yeah.
*  Well, different sets of environments and pressures.
*  Exactly, if we could basically recreate
*  the selection before biology as we know it,
*  that gives rise to a different biology,
*  we should be able to put the constraints
*  on where I look in the universe.
*  So here's a thing, here's my dream.
*  My dream is that by creating life in the lab,
*  based upon constraints we understand,
*  so let's go for Venus type life
*  or Earth type life or something again, do Earth 2.0.
*  Screw it, let's do Earth 2.0.
*  And Earth 2.0 has a different genetic alphabet.
*  Fine, that's fine.
*  Different protein alphabet, fine.
*  Have cells and evolution, all that stuff.
*  We will then be able to say, okay,
*  life is a more general phenomena.
*  Selection is more general than what we think
*  is the chemical constraints on life.
*  And we can point to James Webb and other telescopes
*  at other planets that we are in that zone
*  we are most likely to conventorially overlap with.
*  Right, so, because you know, we basically,
*  so there are chemistry.
*  You're looking for some overlap.
*  And then we can then basically shine light on them
*  literally and look at light coming back
*  and apply advanced assembly theory
*  to general theory of language that we will get
*  and say, huh, in that signal, it looks random,
*  but there's a copy number.
*  Oh, this random set of things that shouldn't be,
*  that looks like a true random number generator
*  has structure as a not common goller of AIT type structure
*  but evolutionary structure given by assembly theory.
*  And we start to, but I would say that
*  because I'm a shameless assembly theorist.
*  Yeah, it just feels like the cone,
*  I might be misusing the word cone here,
*  but the width of the cone is growing faster.
*  It's growing really fast to where eventually
*  all the cones overlap.
*  Even in a very, very, very large combinatorial space.
*  It just, but then again, if you're saying the universe
*  is also growing very quickly in terms of possibilities.
*  That's right.
*  I hope that as we build abstractions,
*  the main, I mean, one idea is that as we go to intelligence,
*  intelligence allows us to look at the regularities
*  around us in the universe.
*  And that gives us some common grounding
*  to discuss with aliens.
*  And you might be right that we will overlap there
*  even though we have completely different chemistry,
*  literally completely different chemistry,
*  that we will be at a past information from one another,
*  but it's not a given.
*  And I have to kind of try and divorce hope and emotion
*  away from what I can logically justify.
*  But it's just hard to intuit a world, a universe,
*  where there's nearly infinite complexity objects
*  and they somehow can't detect each other.
*  But the universe is expanding,
*  but the nice thing is that I would say,
*  I would look, you see, I think Carl Sagan did the wrong,
*  well, not the wrong thing.
*  He flicked the Voyager probe around in a pale blue dot,
*  said, look how big the universe is.
*  I would have done it the other way around
*  and said, look at the Voyager probe
*  that came from the planet Earth, that came from Luca.
*  Look at how big Earth is.
*  They produced that.
*  It produced that.
*  Yeah.
*  And that I think is like completely amazing.
*  And then that should allow people on Earth to think about,
*  well, probably we should try and get causal chains off Earth
*  onto Mars, onto the moon, wherever.
*  Well, it's human life or Martian life that we create.
*  It doesn't matter.
*  But I think this commentorial space tells us something
*  very important about the universe.
*  And that I realized in assembly theory
*  that the universe is too big to contain itself.
*  And I think this is, and now I'm coming back
*  and I want to kind of change your mind about time
*  because I'm guessing that your time is just a coordinate.
*  Yeah.
*  I'm going to change.
*  I'm guessing you're one of those.
*  I'm going to change your mind in real time,
*  or at least attempt.
*  Oh, in real time.
*  There you go.
*  I already got the tattoo, so this is going to be embarrassing
*  if you change my mind.
*  But you can just add an arrow of time onto it, right?
*  True.
*  Just modify it.
*  Or erase it a bit.
*  So, and the argument that I think
*  that is really most interesting is like,
*  people say the initial conditions
*  specify the future of the universe.
*  Okay, fine.
*  Let's say that's the case for a moment.
*  Now let's go back to Newtonian mechanics.
*  Now, the uncertainty between principle
*  and Newtonian mechanics is this.
*  If I give you the coordinates of an object moving in space
*  and the coordinates of another object
*  and they collide in space,
*  and you know those initial conditions,
*  you should know exactly what's going to happen.
*  However, you cannot specify these coordinates
*  to infinite precision.
*  Now everyone said, you know,
*  oh, this is kind of like, you know,
*  the chaos theory argument.
*  No, no, it's deeper than that.
*  Here's a problem with numbers.
*  This is how, this is where Hilbert and Brouwer fell out.
*  To have the coordinates of this object,
*  a given object, they're colliding,
*  you have to have them to infinite precision.
*  That's what Hilbert says.
*  He says, no problem, infinite precision is fine.
*  Let's just take that for granted.
*  But when the object is finite
*  and it can't store its own coordinates, what do you do?
*  So in principle, if a finite object
*  cannot be specified to infinite precision,
*  in principle, the initial conditions don't apply.
*  Well, how do you know it can't store its...
*  Well, how do you store an infinitely long number
*  in a finite size?
*  Well,
*  we're using infinity very loosely here.
*  No, no, we're using...
*  Infinite precision, I mean, not loosely, but...
*  Very precisely.
*  So you think infinite precision is required.
*  Well, let's take the object.
*  Let's say the object is a golf ball.
*  Golf ball is a few centimeters in diameter.
*  We can work out how many atoms are on the golf ball.
*  And let's say we can store numbers
*  down to atomic dislocations.
*  So we can work out how many atoms there are in the golf ball
*  and we can store the coordinates in that golf ball
*  down to that number, but beyond that, we can't.
*  Let's make the golf ball smaller.
*  And this is where I think that we think
*  that we get randomness in quantum mechanics.
*  And some people say you can't get randomness
*  in quantum mechanics deterministic, but aha,
*  this is where we realize that classical mechanics
*  and quantum mechanics suffer
*  from the same uncertainty principle.
*  And that is the inability to specify the initial conditions
*  to a precise enough degree to give you determinism,
*  the universe is intrinsically too big.
*  And that's why time exists.
*  It's non-deterministic.
*  Looking back into the past, you can look at the,
*  you can use logical arguments because you can say,
*  was it true or false?
*  You already know, but this is the fact we are unable
*  to predict the future with the precision
*  is not evidence of lack of knowledge.
*  It's evidence the universe is generating new things.
*  Okay, so to you, first of all, quantum mechanics,
*  you can just say statistically what's gonna happen
*  when two golf balls hit each other.
*  Statistically, but sure, I can say statistic
*  what's gonna happen, but then when they do happen
*  and then you keep nesting it together, you can't,
*  I mean, it goes almost back to look at,
*  let's think about entropy in the universe.
*  So how do we understand entropy change?
*  Well, we could do the look at, or process,
*  we can use the agurdic hypothesis.
*  We can also have the counterfactuals
*  where we have all the different states
*  and we can even put that in the multiverse, right?
*  But both those are kind of, they're non-physical.
*  The multiverse kind of collapses back to the same problem
*  about the precision.
*  So all that, if you accept you don't have to have
*  true and false going forward into the future,
*  the real numbers are real.
*  They're just, they're observables.
*  We're trying to see exactly where time being fundamental
*  sneaks in, in this difference between the golf ball
*  can't contain its own position perfectly precisely
*  how that leads to time needing to be fundamental.
*  Let me, do you believe or do you accept you have free will?
*  Yeah, I think at this moment in time,
*  I believe that I have free will.
*  So then you have to believe that time is fundamental.
*  I understand that's a statement you've made.
*  Well, no, that we can logically follow
*  because if you don't have free will,
*  if you're in a universe that has no time,
*  the universe is deterministic.
*  If it's deterministic, then you have no free will.
*  I think the space of how much we don't know is so vast
*  that saying the universe is deterministic
*  and from that jumping there's no free will
*  is just too difficult of a leap.
*  No, I logically follow.
*  No, no, I don't disagree.
*  I'm not saying any, I mean, it's deep and it's important.
*  All I'm saying and it's actually different
*  to what I've said before
*  is that if you don't require Platonistic mathematics
*  and accepts that non-determinism is how the universe looks
*  and that gives us our creativity
*  in the way the universe is getting novelty,
*  it's kind of really deeply important in assembly theory
*  because assembly theory starts to actually give you
*  a mechanism why you go from boring time,
*  which is basically initial conditions specify everything,
*  to a mismatch in creative time.
*  And I hope we'll do experiments.
*  I think it's really important to,
*  I would love to do an experiment
*  that prove that time is fundamental
*  and the universe is generating novelty.
*  I don't know all the features of that experiment yet,
*  but by having these conversations openly
*  and getting people to think about the problems
*  in a new way, better people, more intelligent people
*  with good mathematical backgrounds can say,
*  oh, hey, I've got an idea.
*  I would love to do an experiment
*  that shows that the universe,
*  I mean, universe is too big for itself going forward in time.
*  And I really, this is why I really hate the idea
*  of the Boltzmann brain.
*  The Boltzmann brain makes me super kind of like,
*  everyone's having a free lunch.
*  It's like saying, it's like,
*  let's break all the laws of physics.
*  So a Boltzmann brain is this idea
*  that in a long enough universe,
*  a brain will just emerge in the universe as conscious.
*  And that neglects the causal chain of evolution
*  required to produce that brain.
*  And this is where the computational argument
*  really falls down because the computationists could say,
*  I can calculate the probability of a Boltzmann brain.
*  And I can, and they'll give you a probability,
*  but I can calculate probability of a Boltzmann brain, zero.
*  Just because the space of possibilities is so large.
*  Yeah, it's like when we start fooling ourselves with numbers
*  that we can't actually measure
*  and we can't ever conceive of,
*  I think it doesn't give us a good explanation.
*  And I've become, I want to explain
*  why life is in the universe.
*  I think life is actually novelty minor.
*  I mean, life basically mines novelty
*  almost from the future and makes it actualize
*  in the present.
*  Okay, life is a novelty minor
*  from the future that is actualized in the present.
*  Yep.
*  I think so.
*  Novelty minor, first of all, novelty.
*  What's the origin of novelty
*  when you go from boring time to creative time?
*  Where's that, is it as simple as randomness
*  like you're referring to?
*  I'm really struggling with randomness
*  because I had a really good argument
*  with Yasha Bach about randomness.
*  And he said, randomness doesn't give you free will.
*  That's insane because you'd just be random.
*  And I think he's right at that level.
*  But I don't think he is right on another level.
*  And it's not about randomness.
*  It's about constrained, I'm gonna sound like,
*  constrained opportunity, I'm making this up
*  as I go along, so making this up, constrained opportunity.
*  So what I mean is like, so you have to have,
*  so the novelty, what is novelty?
*  This is why I think it's a funny thing.
*  You ever wanna discuss AI,
*  why I think everyone's kind of gone AI mad
*  is that they're misunderstanding novelty.
*  But let's think about novelty.
*  Yes, what is novelty?
*  So I think novelty is a genuinely new configuration
*  that is not predicted by the past, right?
*  And that you discover in the present, right?
*  And that is truly different, right?
*  Now everyone says that some people say
*  that novelty doesn't exist.
*  It's always with precedent.
*  I want to do experiments that show
*  that that is not the case.
*  And it goes back to a question you asked me
*  a few moments ago, which is, where is the factory?
*  Right?
*  Because I think the same mechanism
*  that gives us a factory gives us novelty.
*  And I think that that is why I'm so deeply hung up on time.
*  I mean, of course I'm wrong, but how wrong?
*  And I think that life opens up that commentorial space
*  in a way that our current laws of physics,
*  as contrived, in a deterministic initial condition universe,
*  even with the get out of the multiverse, David Deutsch style,
*  which I love, by the way, but I don't think is correct.
*  But it's really beautiful.
*  Multiverse.
*  The David Deutsch's conception of the multiverse
*  is kind of like given.
*  But I think that the problem with wave particle duality
*  and quantum mechanics is not about the multiverse.
*  It's about understanding how determined the past is.
*  Well, I don't think just think that actually,
*  this is a discussion I was having with Sarah about that.
*  Right?
*  She was like, oh, I think we've been debating this
*  for a long time now about how do we reconcile novelty,
*  determinism, indeterminism.
*  So, just to clarify, both you and Sarah think
*  the universe is not deterministic.
*  I won't speak for Sarah, but I roughly,
*  I think that the universe,
*  I think the universe is deterministic looking back
*  in the past, but undetermined going forward in the future.
*  So I'm kind of having my cake and eating it here.
*  This is because I fundamentally don't understand randomness,
*  right, as Yasha told me or other people told me.
*  But if I adopt a new view now, which the new view
*  is the universe is just non-deterministic,
*  but I'd like to refine that and say,
*  the universe appears deterministic going back in the past,
*  but it's undetermined going forward in the future.
*  So how can we have a universe
*  that has deterministically looking rules
*  that's non-determined going in the future?
*  It's this breakdown in precision in the initial conditions.
*  And we have to just stop using initial conditions
*  and start looking at trajectories
*  and how the commentorial space behaves
*  in expanding universe in time and space.
*  And assembly theory helps us quantify
*  the transition to biology.
*  Biology appears to be novelty mining
*  because it's making crazy stuff.
*  That we are unique to earth, right?
*  There are objects on earth that are unique to earth
*  that will not be found anywhere else
*  because you can do the commentorial math.
*  What was that statement you made about life
*  is novelty mining from the future?
*  What's the little element of time that you're introducing?
*  So what I'm kind of meaning is,
*  because the future is bigger than the present,
*  in a deterministic universe, how do you go from the,
*  how do the states go from one to another?
*  I mean, there's a mismatch, right?
*  So that must mean that you have a little bit
*  of indeterminism, whether that's randomness
*  or something else, I don't understand.
*  I want to do experiments to formulate a theory
*  to refine that as we go forward.
*  That might help us explain that.
*  And I think that's why I'm so determined
*  to try and crack the non-life to life transition,
*  looking at networks and molecules,
*  and that might help us think about it, the mechanism.
*  But certainly the future is bigger than the past
*  in my conception of the universe
*  and some conception of the universe.
*  By the way, that's not obvious, right?
*  That's what it was just kind of,
*  the future being bigger than the past.
*  Well, that's one statement, and the statement
*  that the universe is not big enough
*  to contain the future is another statement.
*  Yeah, yeah, yeah, yeah.
*  That one is a big one.
*  That one's a really big one.
*  I think so, but I think it's entirely,
*  because look, we have the second law.
*  And right now, I mean, we don't need the second law
*  if the future's bigger than the past.
*  It follows naturally.
*  So why are we retrofitting all these sticking plasters
*  onto our reality to hold onto a timeless universe?
*  Yeah, but that's because it's kind of difficult
*  to imagine the universe that can't contain the future.
*  But isn't that really exciting?
*  It's very exciting, but it's hard.
*  I mean, we're humans on Earth,
*  and we have a very kind of four-dimensional conception
*  of the world of 3D plus time.
*  It's just hard to intuit a world where,
*  what does it even mean?
*  A universe that can't contain the future.
*  Yeah, it's kind of crazy, but obvious.
*  I mean, I suppose it sounds obvious, yeah, if it's true.
*  But the nice thing is you can,
*  so why, I mean, so the reason why assembly theory
*  turned me onto that was that,
*  let's just start in the present
*  and look at all the complex molecules
*  and go backwards in time
*  and understand how evolutionary processes gave rise to them.
*  It's not at all obvious that taxol,
*  which is one of the most complex natural products
*  produced by biology, was gonna be invented by biology.
*  It's an accident.
*  Taxol is unique to Earth.
*  There's no taxol elsewhere in the universe.
*  And taxol was not decided by the initial conditions.
*  It was decided by this kind of,
*  this interplay between the,
*  so the past simply is embedded in the present.
*  It gives some features,
*  but why the past doesn't map to the future one-to-one
*  is because the universe is too big to contain itself.
*  That gives space for creativity, novelty,
*  and some things which are unpredictable.
*  Okay, so given that you're disrespecting the power
*  of the initial conditions, let me ask you about,
*  so how do you explain that cellular automata
*  are able to produce such incredible complexity
*  given just basic rules and basic initial conditions?
*  I think that this falls into the Brouwer-Hilbert trap.
*  So how would you get a cellular automata
*  produce a complexity?
*  You have a computer, you generate a display,
*  and you map the change of that in time.
*  There are some CAs repeat, like functions.
*  It's fascinating to me that for pi,
*  there is a formula where you can go
*  to the millionth decimal place of pi
*  and read out the number without having to go there.
*  But there are some numbers where you can't do that.
*  You have to just crank through this,
*  whether it's Wolframian computational irreducibility
*  or some other thing, that doesn't matter.
*  But these CAs, that complexity,
*  is that just complexity or a number
*  that is basically you're mining that number in time?
*  Is that just a display screen for that number, that function?
*  Well, can't you say the same thing
*  about the complexity on Earth, then?
*  No, because the complexity on Earth has a copy number
*  and an assembly index associated with it.
*  That CA is just a number running.
*  You don't think it has a copy number?
*  Wait a minute.
*  Well, it does in the human,
*  where we're looking at humans producing different rules,
*  but then it's nested on selection.
*  So those CAs are produced by selection.
*  I mean, the CA is such a fascinating
*  pseudo complexity generator.
*  What I would love to do is understand,
*  quantify the degree of surprise in a CA
*  and write it long enough.
*  But what that, I guess that means
*  is we have to instantiate,
*  we have to have a number of experiments
*  where we're generating different rules
*  and running them time steps.
*  Oh, got it.
*  CAs are mining novelty in the future by iteration, right?
*  And you're like, oh, that's great, that's great.
*  You didn't predict it.
*  Some rules you can predict what's gonna happen.
*  Other rules you can't.
*  So for me, if anything, CAs are evidence
*  that the universe is too big to contain itself.
*  Because otherwise you'd know what the rules
*  are gonna do forever more.
*  Right.
*  I guess you were saying that the physicist
*  saying that all you need is the initial conditions
*  and the rules of physics
*  is somehow missing the bigger picture.
*  And if you look at CA's,
*  all you need is the initial condition and the rules
*  and then run the thing.
*  You need three things.
*  You need the initial conditions, you need the rules,
*  and you need time iteration to mine it out.
*  Without the coordinate, you can't get it out.
*  Sure, and that's that to use fundamentals.
*  And you can't predict it from initial conditions.
*  If you could, then you'd be fine.
*  And that time is a resource.
*  It's the foundation of, this is the history,
*  the memory of each of the things that created it.
*  It has to have that memory
*  of all the things that led up to it.
*  I think it's, yeah, you have to have the resource.
*  Yeah.
*  Because time is a fundamental resource.
*  And yeah, I'm becoming, I think I had a major
*  epiphany about randomness,
*  but I keep doing that every two days
*  and then it goes away again, it's random.
*  You're a time fundamentalist.
*  You should be as well.
*  If you believe in free will,
*  the only conclusion is there is time is fundamental.
*  Otherwise, you cannot have free will.
*  It logically follows.
*  Well, the foundation of my belief in free will
*  is just,
*  is observation driven.
*  But that's-
*  If you use logic, it's like,
*  logically it seems like the universe is deterministic.
*  Looking backwards in time, and that's correct.
*  The universe is.
*  And then everything else is a kind of leap.
*  It requires a leap.
*  I mean, I think that,
*  it's kind of, this is what,
*  I think machine learning is gonna provide a big,
*  a chunk of that, right?
*  Because it helped us explain this.
*  So the way I'd say, if you take-
*  That's interesting.
*  Why?
*  Well, let's just,
*  my favorite one is,
*  because I'm, the AI do-mers are driving me mad.
*  And the fact that we don't have any intelligence yet.
*  I call AI autonomous informatics
*  just to make people grumpy.
*  Yeah.
*  And then-
*  You're saying we're quite far away from AGI.
*  I think that we have no conception of intelligence.
*  And I think that we don't understand
*  how the human brain does what it does.
*  I think that we are,
*  neuroscience is making great advances,
*  but I think that we have no idea about AGI.
*  So I am a technological, I guess, optimist.
*  I believe we should do everything.
*  The whole regulation of AI is nonsensical.
*  I mean, why would you regulate Excel,
*  other than the fact that Clippy should come back,
*  and I love Excel 97,
*  because we can play,
*  we can do the flight simulator.
*  I'm sorry, in Excel?
*  Yeah, have you not played the flight simulator in-
*  In Excel, 97?
*  Yeah.
*  What does that look like?
*  It's like wireframe, very, very basic,
*  but basically I think it's X zero, Y zero, shift,
*  and it opens up and you can play the flight simulator.
*  Oh wow.
*  Wait, wait, is it using Excel?
*  Excel, Excel 97.
*  Okay.
*  I resurrected it the other day
*  and saw Clippy again for the first time in a long time.
*  Well, Clippy is definitely coming back,
*  but you're saying we don't have a great understanding
*  of what is intelligence, what is the intelligence-
*  I am very frustrated-
*  Underpinning the human mind.
*  I'm very frustrated by the way
*  that we're AI dooming right now,
*  and people are bestowing some kind of magic.
*  Now, let's go back a bit.
*  So you said about AGI, are we far away from AGI?
*  Yes, I do not think we're gonna get to AGI anytime soon.
*  I've seen no evidence of it.
*  And the AI doom scenario is nonsensical and extreme.
*  And the reason why I think it's nonsensical,
*  but it's not-
*  And I don't think there isn't things we should do
*  and be very worried about, right?
*  I mean, there are things we need to worry about right now,
*  what AI doing, whether it's fake data, fake users, right?
*  I want authentic people or authentic data.
*  I don't want everything to be faked.
*  And I think it's a really big problem.
*  And I absolutely wanna go on the record to say,
*  I really worry about that.
*  What I'm not worried about is that some fictitious entity
*  is going to turn us all to paper clips
*  or detonate nuclear bombs.
*  I don't know, maybe, I don't know,
*  anything you can't think of.
*  Why is this?
*  I'll take a very simple series of logical arguments.
*  The AI do-mers have not had the correct,
*  they do not have the correct epistemeology.
*  They do not understand what knowledge is.
*  And until we understand what knowledge is,
*  they're not gonna get anywhere
*  because they're applying things falsely.
*  So let me give you a very simple argument.
*  People talk about the probability P-Doom AI.
*  We can work out the probability
*  of an asteroid hitting the planet.
*  Why?
*  Because it's happened before.
*  We know the mechanism.
*  We know that there's a gravity well,
*  or that space time is banned and stuff falls in.
*  We don't know the probability of AGI
*  because we have no mechanism.
*  So let me give you another one,
*  which is like, I'm really worried about AG.
*  What's AG?
*  AG is anti-gravity.
*  One day we could wake up and anti-gravity is discovered.
*  We're all gonna die.
*  The atmosphere is gonna float away.
*  We're gonna float away.
*  We're all doomed.
*  What is the probability of AG?
*  We don't know because there's no mechanism for AG.
*  Do we worry about it?
*  No.
*  And I don't understand the current reason
*  for certain people in certain areas
*  to be generating this nonsense.
*  I think they're not doing it maliciously.
*  I think we're observing the emergence of new religions,
*  how religions come,
*  because religions are about kind of some controls.
*  You've got the optimist saying AI is gonna cure us all
*  and AI is gonna kill us all.
*  What's the reality?
*  Well, we don't have AI.
*  We have really powerful machine learning tools
*  and they will allow us to do interesting things.
*  We need to be careful about how we use those tools
*  in terms of manipulating human beings
*  and faking stuff, right?
*  Right.
*  Let me try to sort of steal man the AI-doomers argument.
*  Actually, I don't know.
*  Are AI-doomers in the Yudkowsky camp saying,
*  it's definitely gonna kill us?
*  Because there's a spectrum.
*  95%, I think, is the limit.
*  95% plus.
*  Not plus.
*  I don't know.
*  I was seeing on Twitter today various things,
*  but I think Yudkowsky is at 95%.
*  But to belong to the AI-doomer club,
*  is there a threshold?
*  I don't know what the membership is.
*  Maybe.
*  And what are the fees?
*  I think, well, I think Scott Aronson,
*  I was quite surprised how it put two,
*  I saw this online, so it could be wrong.
*  So sorry if it's wrong.
*  Says 2%.
*  But the thing is, if someone said there's a 2% chance
*  you're gonna die going into the lift,
*  would you go into the lift?
*  In the elevator for the American English-speaking audience.
*  Well, no, not for the elevator.
*  So I would say anyone higher than 2%,
*  I mean, I think there's a 0% chance of AGI-do.
*  Zero.
*  Just to push back on the argument
*  where the N of zero on the AGI.
*  We could see on Earth that there's increasing levels
*  of intelligence of organisms.
*  We could see what humans with extra intelligence
*  were able to do to the other species.
*  So that is a lot of samples of data
*  what a delta in intelligence gives you.
*  When you have an increase in intelligence,
*  how you're able to dominate a species on Earth.
*  And so the idea there is that if you have a being
*  that's 10x smarter than humans,
*  we're not gonna be able to predict what that's going to do.
*  What that being is gonna be able to do,
*  especially if it has the power to hurt humans.
*  Which you can imagine a lot of trajectories
*  in which the more benefit AI systems give,
*  the more control we give to those AI systems
*  over our power grid, over our nuclear weapons,
*  or weapons of any sort.
*  And then it's hard to know what a ultra-intelligent system
*  would be able to do in that case.
*  You don't find that convincing.
*  I think this is, I would fail that argument 100%.
*  Here's a number of reasons to fail it on.
*  First of all, we don't know where the intention comes from.
*  The problem is that people think they keep,
*  you know, I've been watching all the hucksters online
*  with a prompt engineering and all this stuff.
*  Where, when I talk to a typical AI computer scientist,
*  they keep talking about the AI
*  as having some kind of decision-making ability.
*  That is a category error.
*  The decision-making ability comes from human beings.
*  We have no understanding of how humans make decisions.
*  We've just been discussing free will
*  for the last half an hour, right?
*  We don't even know what that is.
*  So the intention, I totally agree with you.
*  People who intend to do bad things can do bad things
*  and we should not let that risk go.
*  That's totally here and now.
*  I do not want that to happen.
*  And I'm happy to be regulated
*  to make sure that systems I generate,
*  whether they're like computer systems
*  or, you know, I'm working on a new project
*  called Chem Machina.
*  Nice, well done.
*  Yeah, yeah, which is basically a...
*  For people who don't understand the pun,
*  the X Machina is a great film about, I guess,
*  AGI embodied and chem is the chemistry version of that.
*  And I only know one way to embody intelligence,
*  that's in chemistry in human brains.
*  So category error number one is agents, they have agency.
*  Category error number two is saying that,
*  assuming that anything we make
*  is gonna be more intelligent.
*  Now you didn't say super intelligent.
*  I'll put the words into our mouths,
*  here's super intelligent.
*  That I think that there is no reason to expect
*  that we are gonna make systems that are more intelligent,
*  more capable, you know, when people play chess computers,
*  they don't expect to win now, right?
*  The chess computer is very good at chess.
*  That doesn't mean it's super intelligent.
*  So I think that super intelligence,
*  I mean, I think even Nick Bostrom is pulling back on this now
*  because he invented this.
*  So I see this a lot.
*  When does this first happen?
*  Eric Drexler, nanotechnology, atomically precise machines.
*  He came up with a world where we had these atom cogs
*  everywhere, they were gonna make self replicating nanobots.
*  Not possible, why?
*  Because there's no resources
*  to build these self replicating nanobots.
*  You can't get the precision, it doesn't work.
*  It was a major category error
*  in taking engineering principles down to the molecular level.
*  The only functioning molecular technology we know,
*  sorry, the only functioning nanomolecular technology
*  we know produced by evolution, there.
*  So now let's go forward to AGI.
*  What is AGI?
*  We don't know, it's super, it can do this,
*  or humans can't think.
*  I would argue the only AGI's that exist in the universe
*  are produced by evolution.
*  And sure, we may be able to make our working memory better.
*  We might be able to do more things.
*  The human brain is the most compact computing unit
*  in the universe, uses 20 watts,
*  uses a really limited volume.
*  It's not like a chat GPT cluster
*  which has to have thousands of watts model that's generated
*  and it has to be corrected by human beings.
*  You are autonomous and embodied intelligence.
*  So I think that there are so many levels
*  that we're missing out.
*  We've just kind of went, oh, we've discovered fire.
*  Oh gosh, the planet's just gonna burn one day randomly.
*  I mean, I just don't understand that leap.
*  There are bigger problems we need to worry about.
*  So what is the motivation?
*  Why are these people, let's assume they're earnest,
*  have this conviction?
*  Well, I think it's kind of, they're making leaps
*  that they're trapped in a virtual reality
*  that isn't reality.
*  Well, I mean, I can continue this type of arguments here,
*  but also it is true that ideologies
*  that fear monger are dangerous
*  because you can then use it to control,
*  to regulate in a way that halts progress,
*  to control people, to cancel people, all that kind of stuff.
*  So you have to be careful
*  because reason ultimately wins, right?
*  But there is a lot of concerns
*  with super intelligent systems, very capable systems.
*  I think when you hear the word super intelligent,
*  you're hearing like it's smarter than humans
*  in every way that humans are smart.
*  But the paperclip manufacturing system
*  doesn't need to be smart in every way.
*  It just needs to be smart in a set of specific ways.
*  And the more capable the AI systems become,
*  you could see us giving them control over,
*  like I said, our power grid,
*  a lot of aspects of human life.
*  And then that means they will be able
*  to do more and more damage
*  when there's unintended consequences that come to life.
*  I think that that's right,
*  the unintended consequences we have to think about.
*  And that I fully agree with.
*  But let's go back a bit.
*  Sentient, I mean, again, I'm far away from my comfort zone
*  and all this stuff, but hey, let's talk about it
*  because I give myself a qualification.
*  We're both qualified sentience, I think,
*  as much as anyone else.
*  I think the paperclip scenario is just such a poor one
*  because let's think about how that would happen.
*  And also let's think about we are being so unrealistic
*  about how much of the Earth's surface we have commandeered.
*  For paperclip manufacturing to really happen,
*  I mean, do the math.
*  It's like, it's not gonna happen.
*  There's not enough energy, there's not enough resource
*  where they're all gonna come from.
*  What happens in evolution is really,
*  why is a killer virus not killed all life on Earth?
*  Well, what happens is, sure, super killer viruses
*  that kill the ribosome have emerged,
*  but you know what happens?
*  They nuke a small space because they can't propagate.
*  They all die.
*  So there's this interplay between evolution
*  and propagation and death.
*  And so-
*  In evolution.
*  You don't think it's possible to engineer, for example,
*  I'm sorry to interrupt, but a perfect virus
*  that's deadly enough?
*  No, nonsensical.
*  I think that just wouldn't, again, it wouldn't work
*  because it was too deadly.
*  It would just kill the radius and not replicate it.
*  Yeah.
*  I mean, you don't think it's possible to get a-
*  I mean, if you were super, I mean, if you were-
*  Not kill all of life on Earth, but kill all humans.
*  There's not many of us.
*  There's only like eight billion.
*  There's so much more ants.
*  I mean, I don't-
*  There's so many more ants.
*  And they're pretty smart.
*  I think the nice thing about where we are,
*  I would love for the AI crowd to take a leaf out of the book
*  of the bio warfare, chemical warfare crowd.
*  I mean, not love, because actually people have been killed
*  with chemical weapons in the first and second world war
*  and bio weapons have been made.
*  And we can argue about COVID-19 and all this stuff.
*  Let's not go there just now.
*  But I think there is a consensus that some certain things
*  are bad and we shouldn't do them.
*  Right?
*  And sure, it would be possible for a bad actor
*  to engineer something bad, but the damage would be,
*  we would see it coming and we would be able
*  to do something about it.
*  Now, I guess what I'm trying to say is
*  when people talk about doom and they just,
*  when you ask them for the mechanism, they just say,
*  you know, they just make something up.
*  I mean, in this case, I'm with Jan LeCun.
*  I think he put out a very good point about trying
*  to regulate jet engines before we've even invented them.
*  And I think that's what I'm saying.
*  I'm not saying we should, I just don't understand
*  why these guys are going around making,
*  literally making stuff up about us all dying.
*  When basically we need to actually really focus on.
*  Now, let's say there's some actors are earnest.
*  Let's say Yudekowski is being earnest, right?
*  And he really cares, but he loves it.
*  It goes, and then you're all gonna die.
*  It's like, you know, why don't we try and do the same thing
*  and say, you could do this,
*  and then you're gonna be happy forever after.
*  Yeah.
*  Well, I think there's several things to say there.
*  One, I think there is a role in society for people
*  that say we're all gonna die.
*  As I think it filters through as a message,
*  as a viral message that gives us
*  the proper amount of concern.
*  Okay, all right.
*  Meaning not the, it's not 95%, but when you say 95%
*  and it filters through society,
*  it'll give an average of like a .03%, an average.
*  So it's nice to have people that are like,
*  we're all gonna die, then we'll have a proper concern.
*  Like for example, I do believe we're not properly concerned
*  about the threat of nuclear weapons currently.
*  Like that it just seems like people have forgotten
*  that that's a thing.
*  And you know, there's a war in Ukraine
*  with nuclear power involved.
*  There's nuclear power throughout the world
*  and it just feels like we're on the brink
*  of a potential world war to a percentage
*  that I don't think people are properly calibrating,
*  like in their head.
*  We're all thinking it's a Twitter battle
*  as opposed to like actual threat.
*  So like, it's nice to have that kind of level of concern.
*  But to me, like when I hear AI do-mers,
*  what I'm imagining is with unintended consequences,
*  a potential situation where,
*  let's say 5% of the world suffers deeply
*  because of a mistake made of unintended consequences.
*  I don't imagine the entirety of human civilization dying,
*  but there could be a lot of suffering if this is done.
*  I understand that.
*  And I'm, I kind of, I guess, I mean,
*  I'm involved in the whole hype cycle.
*  Like why, I would like us to,
*  I don't want us to, so what's happening right now
*  is there seems to be, so let me,
*  let's say having some people saying AI doom is a worry.
*  Fine, let's give them that.
*  But what seems to be happening is there seems to be people
*  who don't think AI is doing,
*  they're trying to use that to control regulation
*  and to push people to regulate
*  where, which stops humans generating knowledge.
*  And I am an advocate for generating
*  as much knowledge as possible.
*  When it comes to nuclear weapons,
*  I grew up in the seventies and eighties
*  where the nuclear doom,
*  a lot of adults really had existential threat,
*  almost as bad as now with AI doom.
*  They were really worried, right?
*  There was some great, well, not great,
*  there was some horrific documentaries.
*  I think there's one called Fred's
*  that was generated in the UK, which was like,
*  it was terrible, it was like so scary.
*  And I think that the correct thing to do
*  is obviously get rid of nuclear weapons,
*  but let's think about unintended consequences.
*  We've got rid of,
*  we got rid of all the sulfur particles in the atmosphere,
*  right, all the soot.
*  And what's happened in the last couple of years
*  is global warming has accelerated
*  because we've cleaned up the atmosphere too much.
*  So-
*  Sure, I mean, the same thing,
*  if you get rid of nuclear weapons, you're gonna-
*  Exactly, that's my point.
*  So what we could do is if we actually started
*  to put the AI in charge,
*  which is I really like an AI
*  to be in charge of all world politics,
*  and this sounds ridiculous for a second, hang on.
*  But if we could all agree on the-
*  The AI just woke up.
*  Yeah, yeah, yeah.
*  On that statement.
*  But I really don't like politicians
*  who are basically just looking at local sampling.
*  But if you could say globally,
*  look, here's some game theory here.
*  What is the minimum number of nuclear weapons
*  we need to distribute around the world to everybody
*  to basically reduce war to zero?
*  I mean, just the start experiment
*  of the United States and China and Russia
*  and major nuclear powers get together and say,
*  all right, we're gonna distribute nuclear weapons
*  to every single nation on earth.
*  Yeah.
*  Oh boy, I mean, that has a probably greater
*  than 50% chance of eliminating major military conflict.
*  Yeah.
*  Yeah, but it's not 100%.
*  But I don't think anyone will use them
*  because I think, and look, what you've got to try and do
*  is to qualify for these nuclear weapons.
*  This is a great idea.
*  The game theorists could do this, right?
*  I think the question is this.
*  I really buy your question, we have too many nukes.
*  Just from a feeling point of view
*  that we've got too many of them.
*  So let's reduce the number, but not get rid of them
*  because we'll have too much conventional warfare.
*  So then what is the minimum number of nuclear weapons
*  we can distribute around to remove?
*  Humans hurting each other is something we should stop doing.
*  It's in, it's not out with our conceptual capability.
*  But right now, what about the nations,
*  certain nations that are being exploited
*  for their natural resources in the future,
*  because for a short term gain,
*  because we don't want to generate knowledge.
*  And so if everybody had an equal doomsday switch,
*  I predict the quality of life of average human
*  will go up faster.
*  I am an optimist and I believe that humanity
*  is gonna get better and better and better,
*  that we're gonna eliminate more problems.
*  But I think, yeah.
*  But the probability of a bad actor
*  of one of the nations setting off a nuclear weapon.
*  I mean, you have to integrate that into the.
*  But we just give you the nukes like population, right?
*  We give, what we do is we,
*  but anyway, let's just go there.
*  So if a small nation with a couple of nukes uses one
*  because they're a bit bored or annoyed,
*  they're gonna, the likelihood that they are gonna be
*  pummeled out of existence immediately is 100%.
*  And yet they've only nuked one other city.
*  I know this is crazy and I apologize for.
*  Well, no, no, I think it's just to be clear,
*  we're just having a thought experiment that's interesting,
*  but there's terrorist organizations that would take that,
*  would take that trade.
*  Yeah, I mean, look, I'm.
*  We have to ask ourselves the question of how many,
*  which percentage of humans would be suicide bombers,
*  essentially, where they would sacrifice their own life
*  to, because they hate another group of people.
*  And I believe it's a very small fraction,
*  but is it large enough to, if you give out nuclear weapons.
*  I can predict a future where we take all nuclear material
*  and we burn it for energy, right?
*  Because we're getting there.
*  And the other thing you could do is say, look,
*  there's a gap.
*  So if we get all the countries to sign up
*  to the virtual nuclear agreement where we all exist,
*  we have a simulation where we can nuke each other
*  in the simulation and the economic consequences
*  are catastrophic.
*  Sure, in the simulation, I love it.
*  It's not gonna kill all humans,
*  it's just going to have economic consequences.
*  Yeah, I don't know, I just made it up.
*  It seems like.
*  No, it's interesting.
*  I mean, but it's interesting whether that would have
*  as much power in human psychology
*  as actual physical nuclear exposure.
*  I think so.
*  It's possible, but people don't take economic consequences
*  as seriously, I think, as actual nuclear weapons.
*  I think they do in Argentina and they do in Somalia
*  and they're doing a lot of these places where,
*  no, I think this is a great idea.
*  I'm a strong advocate now for, so what have we come up with?
*  Burning all the nuclear material to have energy.
*  And before we do that, because MAD is good,
*  mutually assured destruction is very powerful,
*  let's take it into the metaverse
*  and then get people to kind of subscribe to that
*  and if they actually nuke each other,
*  even for fun in the metaverse, there are dire consequences.
*  Yeah, yeah, so it's like a video game.
*  We all have to join this metaverse video game.
*  Yeah, I can't believe we just.
*  And then there's dire economic consequences.
*  I don't know how, and it's all run by AI, as you mentioned,
*  so the AI do-mers are really terrified at this point.
*  No, they're happy, they have a job
*  for another 20 years, right?
*  Oh, fear mongering.
*  Yeah, yeah, yeah.
*  I'm a believer in equal employment.
*  You've mentioned that, what'd you call it?
*  Chem machina?
*  Yeah. Yeah.
*  So you've mentioned that a chemical brain
*  is something you're interested in creating
*  and that's a way to get conscious AI soon.
*  Can you explain what a chemical brain is?
*  I wanna understand the mechanism of intelligence
*  that's gone through evolution, right?
*  Because the way that intelligence was produced
*  by evolution appears to be the following,
*  origin of life, multicellularity, locomotion, senses.
*  Once you can start to see things coming towards you
*  and you can remember the past and interrogate the present
*  and imagine the future, you can do something amazing, right?
*  So, and I think only in recent years
*  did humans become Turing complete.
*  Yeah.
*  Yeah.
*  Right, and so that Turing completeness
*  kind of gave us another kick up.
*  But our ability to process that information
*  is produced in a wet brain.
*  And I think that we are not getting,
*  we do not have the correct hardware architectures
*  to have the domain flexibility
*  and the ability to integrate information.
*  And I think intelligence also comes
*  at a massive compromise of data.
*  Right now, we're obsessing about getting more and more data,
*  more and more processing, more and more tricks
*  to get dopamine hits.
*  So when we look back on this, going,
*  oh yeah, that was really cool.
*  Because when I asked chat GPT,
*  it made me feel really happy.
*  I got a hit from it, but actually it just exposed
*  how little intelligence I use in every moment
*  because I'm easily fooled.
*  So what I would like to do is to say,
*  well, hey, hang on, what is it about the brain?
*  So the brain has this incredible connectivity
*  and it has the ability to,
*  as I said earlier about my nephew,
*  I went from Bill to Billy and he went, all right, Leroy.
*  How did he make that leap?
*  That he was able to basically, without any training,
*  I extended his name, he went gay and he doesn't like,
*  he wants to be called Bill.
*  He went back and said, you like to be called Lee?
*  I'm gonna call you Leroy.
*  So human beings have a brilliant ability
*  or intelligent beings appear to have a brilliant ability
*  to integrate across all domains all at once
*  and to synthesize something
*  which allows us to generate knowledge
*  and becoming Turing complete on our own,
*  although AIs are built in Turing complete things,
*  their thinking is not Turing complete
*  in that they are not able to build universal explanations.
*  And that lack of universal explanation
*  means that they're just inductivists.
*  Inductivism doesn't get you anywhere.
*  It's just basically a party trick.
*  It's like, I like the,
*  I think it's in the fabric of reality from David Deutsch
*  where basically the farmer is feeding the chicken every day
*  and the chicken's getting fat and happy
*  and the chicken's like, I'm really happy.
*  Every time the farmer comes in and feeds me
*  and then one day the farmer comes in
*  and instead of feeding the chicken, just rings its neck.
*  And that's kind of, and had the chicken
*  had an alternative understanding
*  of why the farmer was feeding it.
*  It's interesting though, because we don't know
*  what's special about the human mind
*  that's able to come up with these kind of generalities,
*  this universal theories of things
*  and who come up with novelty.
*  I can imagine, because you gave an example
*  about William and Leroy.
*  I feel like
*  example like that will be able to see
*  in future versions of large language models
*  will be really, really, really impressed
*  by the humor, the insights, all of it,
*  because it's fundamentally trained
*  on all the incredible humor and insights
*  that's available out there on the internet, right?
*  So we'll be impressed.
*  I think we'll be impressed.
*  Oh, I'm impressed.
*  I'm impressed.
*  Increasingly so.
*  But we're mining the past.
*  Yes.
*  And what the human brain appears to be able to do
*  is mine the future.
*  Yes.
*  So novelty, it is interesting
*  whether these large language models
*  will ever be able to come up with something truly novel.
*  I can show on the back of a piece of paper
*  why that's impossible.
*  And it's like the problem is that,
*  and again, these are domain experts
*  kind of bullshitting each other.
*  The term generative, right?
*  Average person, oh, it's generative.
*  No, no, no.
*  If look, if I take the numbers between zero and 1000,
*  and I train a model to pick out the prime numbers
*  by giving them all the prime numbers between zero and 1000,
*  he doesn't know what prime number is.
*  Occasionally, if I can cheat a bit,
*  it will start to guess.
*  It never will produce anything out with the data set
*  because you're mining the past.
*  The thing that I'm getting to is I think that actually
*  current machine learning technologies
*  might actually help reveal why time is fundamental.
*  It's like kind of insane
*  because they tell you about what's happened in the past,
*  but they can never help you understand
*  what's happening in the future without training examples.
*  Sure, if that thing happens again, it's like,
*  so I think, so let's think about
*  what large average models are doing.
*  We have the, we have the,
*  we have all the internet as we know it, you know, language,
*  but also they're doing something else.
*  We're having human beings correcting it all the time.
*  Those models are being corrected.
*  Steered.
*  Corrected.
*  Modified.
*  Tweaked.
*  It's cheating.
*  Well, you could say that training on human data
*  in the first place is cheating.
*  Well, let me, humans in the loop, sorry to interrupt.
*  Yes, so human is definitely in the loop,
*  but it's not just human that's in the loop.
*  A very large collection of humans is in the loop.
*  Look, I totally.
*  And that could be,
*  I mean, to me, it's not intuitive that,
*  you said prime numbers,
*  that the system can't generate an algorithm, right?
*  That the algorithm that can generate prime numbers
*  or the algorithm that can tell you
*  if a number is prime and so on,
*  and generate algorithms that generate algorithms
*  that generate algorithms that start to look a lot
*  like human reasoning, you know?
*  I don't think, I think again,
*  we can show that on a piece of paper.
*  That's sure.
*  I think there has to, you have to have,
*  so this is the failure in epistemeology.
*  Like I'm glad I even can say that word,
*  let me know what it means.
*  It's impressive, you said it multiple times.
*  I know, it's like three times now.
*  Without failure.
*  Quit while you're ahead.
*  Stop saying it again, because you did really well.
*  Thanks.
*  So, but I think, so what is reasoning?
*  So coming back to the chemical brain,
*  if I could basically, if I could show that in a,
*  because I mean, I'm never gonna make an intelligence
*  in Chem Machina, because if we don't have brain cells,
*  they don't have glial cells, they don't have neurons,
*  but if I can make, if I can take a gel
*  and engineer the gel to have it be a hybrid hardware
*  for reprogramming, which I think I know how to do,
*  I will be able to process a lot more information
*  and train models billions of times cheaper
*  and use cross-domain knowledge.
*  And there's certain techniques I think we can do,
*  but they're still missing, though the abilities
*  that human beings have had to become true and complete.
*  And so I guess the question to give back at you
*  and I, it's like, how do you tell the difference
*  between trial and error and the generation of new knowledge?
*  I think the way you can do it is this,
*  is that you come up with a theory, an explanation,
*  inspiration comes from out, yeah,
*  and then you then test that,
*  and then you see that's going towards a truth.
*  And human beings are very good at doing that
*  and the transition between philosophy, mathematics,
*  physics and natural sciences where,
*  and I think that we can see that.
*  Where I get confused is why people misappropriate
*  the term artificial intelligence to say,
*  hey, there's something else going on here
*  because I think you and I both agree,
*  machine learning is really good.
*  It's only gonna get better,
*  we're gonna get happier with the outcome.
*  But why would you ever think the model was thinking
*  or reasoning?
*  Reasoning requires intention.
*  And the intention, if the model isn't reasoning,
*  the intentions come from the prompter
*  and the intention has come from the person
*  who programmed it to do it.
*  So I...
*  But don't you think you can prompt it to have intention?
*  Basically start with the initial conditions and get it going
*  where the, you know, currently large language models,
*  Chad GPT only talks to you when you talk to it.
*  There's no reason why you can't just start it talking.
*  But those initial conditions came from someone starting it
*  and that causal chain in there.
*  So that intention comes from the outside.
*  I think that there is something in that causal chain
*  of intention that's super important.
*  I don't disagree we're gonna get to AGI.
*  It's a matter of when and what hardware.
*  I think we're not gonna do it in this hardware.
*  And I think we're unnecessarily fetishizing
*  really cool outputs and dopamine hits
*  because obviously that's what people wanna sell us.
*  Well, but there could be, I mean, AGI is a loaded term,
*  but there could be incredibly super impressive
*  intelligence systems on the way to AGI.
*  So these large language models, I mean,
*  if it appears conscious, if it appears super intelligent,
*  who are we to say it's not?
*  I agree.
*  But the super intelligence I want,
*  I want to be able to have a discussion with it
*  about coming up with fundamental new ideas
*  that generate knowledge.
*  And if the super intelligence we generate
*  can mine novelty from the future that I didn't see
*  in its training set in the past,
*  I would agree that something really interesting
*  is coming on.
*  I'll say that again, if the intelligence system,
*  be it a human being, a chat bot, something else,
*  is able to produce something truly novel
*  that I could not predict,
*  even having full audit trail from the past,
*  then I would be sold.
*  Well, so we should be clear that it can currently produce,
*  it can currently produce things that are
*  in a shallow sense novel,
*  that are not in the training set.
*  But you're saying truly novel.
*  I think they are in the training set.
*  I think everything it produces comes from a training set.
*  They might be inter, there's a difference
*  between novelty and interpolation.
*  We do not understand where these leaps come from yet.
*  That is what intelligence is, I would argue.
*  Those leaps, and some people say, no,
*  it's actually just what will happen
*  if you just do cross domain training and all that stuff.
*  And that may be true.
*  And I may be completely wrong.
*  But right now, the human mind is able to mine novelty
*  in a way that artificial intelligence systems cannot.
*  And this is why we still have a job
*  and we're still doing stuff.
*  And I used chat GPT for a few weeks,
*  well, this is cool.
*  And then it took me too, I had to,
*  well, what happened is it took me too much time
*  to correct it, then it got really good.
*  And now they've done something to it.
*  It's not actually that good.
*  Yeah, right.
*  I don't know what's going on.
*  Some censorship, yeah.
*  I mean, that's interesting,
*  but it will push us humans to characterize novelty better.
*  Like characterize the novel, like what is novel?
*  What is truly novel?
*  What's the difference between novelty and interpolation?
*  I think that this is the thing that makes me most excited
*  about these technologies,
*  is they're gonna help me demonstrate to you
*  that time is fundamental
*  and you know future is bigger than the present,
*  which is why we are,
*  human beings are quite good at generating novelty
*  because we have to expand our data set
*  and to cope with unexpected things in our environment.
*  Our environment throws them all at us.
*  Again, we have to survive in that environment.
*  I mean, I never say never.
*  I would be very interested in how we can get
*  cross domain training cheaply in chemical systems
*  because I'm a chemist and the only sent in thing
*  I know of is human brain,
*  but maybe that's just me being boring,
*  predictable and not novel.
*  Yeah, you mentioned GPT for electron density.
*  So a GPT like system for generating molecules
*  that can bind to host automatically.
*  I mean, that's interesting.
*  That's really interesting.
*  Applying this same kind of transformer mechanism.
*  Yeah.
*  I mean, this is one of,
*  it goes my team, I try and do things that are non-obvious
*  but non-obvious in certain areas.
*  And one of the things I was always asking about
*  in chemistry, people like to represent molecules as graphs
*  and it's quite difficult.
*  It's really hard in a,
*  if you're doing AI in chemistry,
*  you really want to basically have good representations.
*  You can generate new molecules are interesting.
*  And I was thinking, well, molecules aren't really graphs
*  and they're not continuously differentiable.
*  Could I do something that was continuously differentiable?
*  I was like, well, molecules are actually made up
*  of electron density.
*  So then I got thinking and say, well, okay,
*  could there be a way where we could just basically take
*  a database of readily solved electron densities
*  for millions of molecules.
*  So we took the electron density for millions of molecules
*  and just train the model
*  to learn what electron density is.
*  And so what we built was a system
*  that you literally could give it a,
*  let's say you could take a protein
*  that has a particular active site
*  or a cup with a certain hole in it,
*  you pour noise into it.
*  And with a GPT, you turn the noise into electron density.
*  And then in this case, it hallucinates like all of them do,
*  but the hallucinations are good
*  because it means I don't have to train
*  on such a large number, such a huge dataset,
*  because these datasets are very expensive
*  because how do you produce it?
*  So go back a step.
*  So you've got all these molecules in this dataset,
*  but what you've literally done
*  is a quantum mechanical calculation
*  where you produce electron densities for each molecule.
*  So you say, oh, this representation of this molecule
*  has these electron densities associated with it.
*  So you know what the representation is
*  and you train the neural network
*  to know what electron density is.
*  So then you give it an unknown pocket.
*  You pour in noise and you say, right,
*  produce me electron density,
*  produces electron density that doesn't look ridiculous.
*  And what we did in this case
*  is we produce electron density
*  that maximizes the electrostatic potential,
*  so the stickiness,
*  but minimizes what we call the steric hindrance.
*  So the overlaps, it's repulsive.
*  So make the perfect fit.
*  And then we then use the kind of like a chat GPT type thing
*  to turn that electron density into what's called a smile.
*  A smile string is a way of representing a molecule
*  in letters.
*  And then we can then-
*  So it just generates them then.
*  Just generates them.
*  And then the other thing is then we bung that
*  into the computer and then it just makes it.
*  Yeah, the computer being the thing that, right.
*  The robot that we've got that can basically
*  just do chemistry.
*  Create a new EES.
*  So kind of, we've kind of got this end to end
*  drug discovery machine where you can say,
*  oh, you want to bind to this active site, here you go.
*  I mean, it's a bit leaky and things kind of break,
*  but it's a proof of principle.
*  Well, were the hallucinations,
*  are those still accurate?
*  Well, the hallucinations are really great in this case
*  because in the case of a large-diamond model,
*  the hallucinations just like just make everything up to,
*  when it doesn't just make everything up,
*  but it gives you an output
*  that you're plausibly comfortable with.
*  It thinks you're doing probabilistically.
*  The problem on these electron density models is
*  it's very expensive to solve a Schrodinger equation
*  going up to many heavy atoms and large molecules.
*  And so we wondered if we trained the system
*  on up to nine heavy atoms, whether it would go beyond nine.
*  And it did.
*  It started to generate molecules of 12.
*  No problem.
*  They look pretty good.
*  And I was like, well, this hallucination,
*  I will take for free.
*  Thank you very much.
*  Cause it just basically,
*  this is a case where interpolation, extrapolation
*  worked relatively well.
*  And we were able to generate the really good molecules.
*  And then what we were able to do here is,
*  and this is a really good point
*  of what I was trying to say earlier,
*  that we were able to generate new molecules
*  from the known dataset that would bind to the host.
*  So a new guest would bind.
*  Were these truly novel?
*  Not really, because they were constrained by the host.
*  Were they new to us?
*  Yes.
*  So I do understand,
*  I can concede that machine learning systems,
*  artificial intelligence systems can generate new entities,
*  but how novel are they?
*  It remains to be seen.
*  Yeah.
*  And how novel the things that humans generate
*  is also difficult to quantify.
*  They seem novel.
*  That's what a lot of people say.
*  Like, you know, so the way to really get to genuine novelty
*  and assembly theory shows you the way
*  is to have different causal chains overlap.
*  And this really resonates with the time is fundamental argument.
*  And if you're bringing together a couple of objects
*  with different initial conditions coming together,
*  when they interact, the more different their histories,
*  the more novelty they generate in time going forward.
*  And so it could be that genuine novelty
*  is basically about mix it up a little,
*  and the human brain is able to mix it up a little,
*  and all that stimulus comes from the environment.
*  But all I think I'm saying is the universe is deterministic
*  going back in time,
*  non-deterministic going forward in time
*  because the universe is too big in the future
*  to contain in the present.
*  Therefore, these collisions of known things
*  generate unknown things that then become part of your data set
*  and don't appear weird.
*  That's how we give ourselves comfort.
*  The past looks consistent with this initial condition
*  hypothesis, but actually we're generating more and more novelty.
*  And that's how it works. Simple.
*  So it's hard to quantify novelty looking backwards.
*  I mean, the present and the future are the novelty generators.
*  But I like this whole idea of mining novelty.
*  I think it is going to reveal why the limitations of current AI
*  is a bit like a printing press, right?
*  Everyone thought that when the printing press came
*  that writing books is going to be terrible,
*  that you had evil spirits and all this, they were just books.
*  And the same with AI.
*  But I think just the scale you can achieve in terms of impact
*  with AI systems is pretty nerve-racking.
*  But that's what the big companies want you to think.
*  But not like in terms of destroy all humans,
*  but you can have major consequences
*  in the way social media has had major consequences,
*  both positive and negative.
*  And so you have to kind of think about and worry about it.
*  But yeah, people that fear monger, you know...
*  My pet theory for this, you want to know?
*  Yeah.
*  Is I think that a lot of... And maybe I'm being...
*  And I think I really do respect, you know,
*  a lot of the people out there who are trying to have discourse
*  about the positive future.
*  So open AI guys, meta guys and all this.
*  What I wonder if they're trying to cover up for the fact
*  that social media has had a pretty disastrous effect
*  at some level.
*  And they're just trying to say,
*  oh yeah, we should do this.
*  Because covering up for the fact that we have got
*  some problems with teenagers and Instagram and Snapchat
*  and all this stuff.
*  And maybe they're just overreacting now.
*  Yeah.
*  It's like, oh yeah, sorry, we made the bubonic plate
*  and gave it to you all and you're all dying.
*  And oh yeah, but look at this over here, it's even worse.
*  Yeah, there's a little bit of that,
*  but there's also not enough celebration
*  of the positive impact that all these technologies have had.
*  We tend to focus on the negative and tend to forget
*  that in part because it's hard to measure.
*  Like it's very hard to measure the positive impact
*  social media had on the world.
*  Yeah, I agree.
*  But what I worry about right now is like,
*  I'm really, I do care about the ethics of what we're doing.
*  And one of the reasons why I'm so open about
*  the things we're trying to do in the lab, make life,
*  look at intelligence, all this.
*  Is so people say, what are the consequences of this?
*  And you say, what are the consequences of not doing it?
*  And I think that what worries me right now in the present
*  is lack of authenticated users and authenticated data.
*  Human users.
*  Yeah, human.
*  I still think that there will be AI agents
*  that appear to be conscious,
*  but they would have to be also authenticated
*  and labeled as such.
*  Because there's too much value in that,
*  like friendships with AI systems.
*  There's too much meaningful human experiences
*  to have with AI systems that I just.
*  But that's like a tool, right?
*  It's a bit like a meditation tool, right?
*  Some people have a meditation tool,
*  it makes them feel better.
*  But I'm not sure you can ascribe sentience and legal rights
*  to a chat bot that makes you feel less lonely.
*  Sentience, yes.
*  I think legal rights, no.
*  I think it's the same.
*  You can have a really deep meaningful relationship
*  with a dog.
*  And with a pet. With a dog sentient?
*  Yes.
*  The chat bot's not, right now,
*  using the technology we use, it's not gonna be sentient.
*  Ah, this is gonna be a fun continued conversation
*  on Twitter that I look forward to.
*  Since you've had also, from another place,
*  some debates that were inspired
*  by the Assembly Theory paper,
*  let me ask you about God.
*  Is there any room for notions of God in Assembly Theory?
*  In Assembly Theory?
*  Who's God?
*  Yeah, I don't know what God is.
*  I mean, so God exists in our minds, created by selection.
*  So the human beings have created the concept of God
*  in the same way that human beings
*  have created the concept of superintelligence.
*  Sure, but does it mean, does it not,
*  it still could mean that that's a projection
*  from the real world,
*  where we're just assigning words and concepts
*  to a thing that is fundamental to the real world,
*  that there is something out there
*  that is a creative force underlying the universe?
*  I think the universe,
*  there is a creative force in the universe,
*  but I don't think it's sentient.
*  I mean, I think the, so, I do not understand the universe.
*  So who am I to say, you know,
*  that God doesn't exist?
*  I am an atheist, but I'm not an angry atheist, right?
*  I have lots of, I have lots of,
*  there's some people I know that are angry atheists,
*  and say, you know,
*  say that religious people are stupid.
*  I don't think that's the case.
*  I have faith in some things,
*  because I don't, I mean, when I was a kid,
*  I kept like, you know, I was like,
*  well, I need to know what the charge of electron is.
*  And I'm like, I can't measure the charge of electron.
*  That was, you know, I just gave up and had faith, okay?
*  You know, resistors worked.
*  So when it comes to,
*  I want to know why the universe is growing in the future
*  and what humanity is gonna become.
*  And I've seen that the acquisition of knowledge
*  via the generation of novelty to produce technology
*  has uniformly made humans' lives better.
*  I would love to continue that tradition.
*  And...
*  You said that there's that creative force.
*  Do you think, just to think on that point,
*  do you think there's a creative force?
*  Is there like a thing, like a driver
*  that's like, that's creating stuff?
*  Yeah, I think that, so I think that...
*  And where?
*  What is it?
*  Can you describe it like mathematically?
*  Well, I think selection.
*  I think selection...
*  Selection is the force.
*  Selection is the force in the universe
*  that creates novelty.
*  So is selection somehow fundamental?
*  Like what?
*  Yeah.
*  Yeah, I think persistence of objects
*  that could decay into nothing
*  through operations that maintain that structure.
*  I mean, think about it.
*  If it's amazing that things exist at all,
*  that we're just not a big commentarial mess.
*  Yes.
*  So the fact that...
*  And exist, a thing that exists persists in time.
*  Yeah.
*  I mean, let's think maybe the universe is actually
*  in the present, the things,
*  everything that can exist in the present does exist.
*  Well, that would mean it's deterministic, right?
*  No, I think the universities might,
*  so the universe started super small.
*  The past was deterministic.
*  There wasn't much going on.
*  And it was able to mine, mine, mine, mine, mine.
*  And so the process, I mean,
*  is somehow generating...
*  The universe is basically...
*  I'm trying to put this into words.
*  Did you just say there's no free will though?
*  No, I didn't say that.
*  As if everything that can exist...
*  I said there is free will.
*  I think I'm saying that free will
*  occurs at the boundary between the...
*  Past and the future.
*  The past and the future.
*  Yeah, I got you.
*  But everything that can exist does exist.
*  Everything that is...
*  So everything that's possible to exist at this...
*  So no, I'm really pulling...
*  There's a lot of loaded words there.
*  And there's a time element loaded into that statement.
*  I think that the universe is able to do
*  what it can in the present, right?
*  And then I think in the future,
*  there are other things that could be possible.
*  We can imagine lots of things,
*  but they don't all happen.
*  Sure.
*  That's where you sneak in free will right there.
*  Yeah.
*  So I guess what I'm saying is what exists
*  is a convolution of the past with the present
*  and the free will going into the future.
*  But we can still imagine stuff, right?
*  We can imagine stuff that will never happen.
*  And it's an amazing force.
*  Because you're imagining...
*  This is the most important thing that we don't understand
*  is our imaginations can actually change the future
*  in a tangible way,
*  which is what the initial conditions in physics
*  cannot predict.
*  Your imagination has a causal consequence in the future.
*  Isn't that weird too?
*  Yeah.
*  It breaks the laws of physics as we know them right now.
*  Yeah.
*  So you think the imagination has a causal effect
*  on the future.
*  Yeah.
*  But it does exist in there in the head.
*  And there must be a lot of power in whatever's going on.
*  There could be a lot of power
*  in whatever's going on in there.
*  If we then go back to the initial conditions,
*  and it's simply not possible that can happen.
*  But if we go into a universe where we accept
*  that there is a finite ability to represent numbers
*  and you have rounding,
*  well, not rounding errors,
*  you have the sum of what happens.
*  Your ability to make decisions, imagine and do stuff
*  is at that interface between the certain and the uncertain.
*  It's not as Yasha was saying to me,
*  randomness goes and you just randomly do random stuff.
*  It is that you are set free a little on your trajectory.
*  Free will is about being able to explore
*  on this narrow trajectory that allows you to build.
*  You have a choice about what you build.
*  Or that choice is you interacting
*  with a future in the present.
*  What to you is most beautiful about this whole thing?
*  The universe.
*  The fact it seems to be very undecided, very open.
*  The fact that every time I think I'm getting
*  towards an answer to a question,
*  there are so many more questions that make the chase.
*  Do you hate that it's gonna be over at some point?
*  No, well for me, so I think if you think about it,
*  is it over for Newton now?
*  Newton has had causal consequences in the future.
*  We discuss him all the time.
*  His ideas, but not the person.
*  The person just had a lot of causal power when he was alive,
*  but oh my God, one of the things I wanna do
*  is leave as many Easter eggs in the future when I'm gone
*  to go, oh, that's cool.
*  Would you be very upset if somebody made a good
*  large language model that's fine tuned to Lee Conner?
*  It would be quite boring, because I mean,
*  I mean, I'm a- Novelty generation?
*  I mean, if it's a faithful representation
*  of what I've done in my life, that's great.
*  That's an interesting artifact,
*  but I think the most interesting thing
*  about knowing each other is we don't know
*  what we're gonna do next.
*  Sure.
*  Sure.
*  I mean, within some constraints, I've got, you know,
*  I can predict some things about you,
*  you can predict some things about me,
*  but we can't predict everything.
*  Everything.
*  And it's because we can't predict everything
*  is why we're excited to come back and discuss and see it.
*  So yeah, I'm kind of happy that it'll be interesting
*  that some things that I've done can be captured,
*  but I'm pretty sure that my
*  angle on mining novelty from the future
*  will not be captured.
*  Yeah.
*  Yeah.
*  That's what life is, is just some novelty generation
*  and then you're done.
*  Each one of us just generate a little bit,
*  or have the capacity to at least.
*  I think life is a selection produces life
*  and life affects the universe.
*  Universes with life in them are materially, physically,
*  fundamentally different than universes without life.
*  And that's super interesting.
*  And I have no beginnings of understanding.
*  I think maybe this is like in a thousand years,
*  there'll be a new discipline in humans.
*  But yeah, of course, this is how it all works.
*  And.
*  In retrospect, it will all be obvious, I think.
*  I think assembly theory is obvious.
*  That's why a lot of people got angry, right?
*  They were like, oh my God, this is such nonsense.
*  Yeah.
*  And like, oh, actually it's not quite.
*  But the writing's really bad.
*  Well, I can't wait to see where it evolves, Lee.
*  And I'm glad I get to exist in this universe with you.
*  You're a fascinating human.
*  This is always a pleasure.
*  I hope to talk to you many more times.
*  And I'm a huge fan of just watching you create stuff
*  in this world.
*  And thank you for talking to me.
*  It's a pleasure as always, Lex.
*  Thanks for having me on.
*  Thanks for listening to this conversation with Lee Cronin.
*  To support this podcast,
*  please check out our sponsors in the description.
*  And now let me leave you with some words from Carl Sagan.
*  We can judge our progress by the courage of our questions
*  and the depth of our answers.
*  Our willingness to embrace what is true
*  rather than what feels good.
*  Thank you for listening and hope to see you next time.

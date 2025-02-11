---
Date Generated: September 05, 2024
Transcription Model: whisper medium 20231117
Length: 4835s
Video Keywords: []
Video Views: 10943
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2024/08/19/286-blaise-aguera-y-arcas-on-the-emergence-of-replication-and-computation/

Understanding how life began on Earth involves questions of chemistry, geology, planetary science, physics, and more. But the question of how random processes lead to organized, self-replicating, information-bearing systems is a more general one. That question can be addressed in an idealized world of computer code, initialized with random sequences and left to run. Starting with many such random systems, and allowing them to mutate and interact, will we end up with "lifelike," self-replicating programs? A new paper by Blaise Agüera y Arcas and collaborators suggests that the answer is yes. This raises interesting questions about whether computation is an attractor in the space of relevant dynamical processes, with implications for the origin and ubiquity of life.

Blaise Agüera y Arcas received a B.A. in physics from Princeton University. He is currently a vice-president of engineering at Google, leader of the Cerebra team, and a member of the Paradigms of Intelligence team. He is the author of the books Ubi Sunt and Who Are We Now?, and the upcoming What Is Intelligence?

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel: https://www.youtube.com/c/seancarroll

#podcast #ideas #science #philosophy #culture
---

# Mindscape 286  Blaise Agüera y Arcas on the Emergence of Replication and Computation
**Mindscape Podcast:** [August 19, 2024](https://www.youtube.com/watch?v=7lwOpwh-FXM)
*  Hello everyone and welcome to the Mindscape Podcast. I'm your host Sean Carroll.
*  Today's podcast has a good news, bad news situation.
*  The bad news is there will be bad language in this podcast. Not because we're getting especially salty or
*  profane or anything like that, but because we're going to be talking about computer simulations
*  that were written and run using a language called brainfuck.
*  Sorry about that if you have sensitive ears, but this is a very real computer language that was given that name brainfuck.
*  And so we're gonna have to say the phrase brainfuck over and over again.
*  That's why I'm saying it right now just to loosen you up and get you to know that this is what is going to be coming.
*  The good news is it's gonna be worth it. This is a really fascinating conversation about a super important topic
*  which is in some sense the topic is the origin of life,
*  but there's not a lot of chemistry or biology or geology or anything like that in the talk in the conversation.
*  It's a model for the origin of life or a simulation of the origin of life done on a computer.
*  Today's guest is Blaise Aguera y Arcas who is a very successful computer scientist like a real-world
*  computer scientist. He works, he has worked for Microsoft, he now works for Google doing things like AI of course,
*  but also visualization, augmented reality, questions about how machines can be creative and artistic things like that
*  with real-world applications, but it's led him to think more broadly about what is intelligence? What is life?
*  What is, you know, if you're a naturalist, a physicalist, like I definitely am and I think Blaise also is, then you think that
*  things like life and thought are outcomes of physical things bumping into each other in
*  particular but especially complicated ways and then there's an emergent higher level description of this thing that we call life.
*  So clearly going back to people like
*  Schrödinger and von Neumann and others, there's a statistical mechanics of this, right?
*  You want to know
*  in the ways, all the different ways you could organize atoms and molecules and so forth,
*  how likely is it that you would get life? You know, there's, and you immediately say, well look,
*  of all the ways that I could take a given set of atoms or molecules and organize them,
*  most of them don't look like living beings at all, right? Living beings are clearly a very very organized tiny subset in the space of all possible
*  configurations.
*  True,
*  that's the old sort of quasi-creationist argument that you're not going to get life just by randomly throwing things together.
*  In an infinitely old universe, maybe you would, that's the Boltzmann-Reyn paradox,
*  but our universe is not nearly old enough to make that relevant. But it's also not the right question, right?
*  We don't just throw some molecules together randomly. Maybe we start with some semi-random
*  configuration. It's not really random because it's low entropy,
*  but we start with some specific configuration and then we evolve it for a very long time and that evolution is sort of
*  interesting and explores this
*  gigantically big space of possibilities. And then the much more sophisticated and important question is, do
*  trajectories in that kind of setup have little subregions that are likely
*  to look like life in some way? Now the space of possibilities is so large
*  you can't be very realistic in exploring that, but you can start with a little toy model. And so what Blaise and his
*  collaborators have done is write programs, not even write programs, sorry I shouldn't say that, they've explored
*  a system where you have little programs written in this language, BrainFuck, and there's many, many, many programs,
*  and the programs are starting literally with random symbols. Okay, imagine if you went into your
*  Python compiler or HTML for that matter and just typed in random symbols, it would just be a mess, nothing would happen.
*  But BrainFuck is so small as a computer language that sometimes things are going to happen.
*  And what they show with their specific set of rules, which is not, you know, they didn't cook in the answer,
*  they let the different computer programs kind of talk to each other and
*  influence each other, interact with each other, and they find the spontaneous emergence of replication.
*  That is to say, you generate, eventually after sort of fumbling around randomly for a little while,
*  you find little bits of computer programs that reproduce themselves and in some sense, which we'll talk about in the podcast,
*  hand down their genetic information to later
*  generations. And in fact, those
*  particular self-reproducing computer programs take over. They win, right?
*  They, because they can replicate themselves not only where they are, but in their next-door neighbors,
*  they can fill the space in a finite period of time. So
*  that's a kind of origin of life. No real laws of physics there, certainly no real chemistry or anything like that.
*  But if you think that the fundamental essence of the origin of life is sort of reproduction and
*  handing down your genetic information to your successors,
*  then there's something like that going on. And it's not put in by hand like a lot of
*  simulations and things do. You can easily simulate
*  evolution once you already have
*  replication and genetic information, etc.
*  But here is a simulation that actually starts from nothing and the replication and the information you need to make it happen
*  pop up just through the dynamics of the system.
*  What are the implications of that for the origin of life in the real world, for looking for life, for thinking about what life is?
*  Well, you will have to listen to this podcast because we're gonna address all those questions.
*  And with that, let's go.
*  Ladies and gentlemen, welcome to the Mindscape podcast. Thank you, Sean. I'm really glad to be here. So you are
*  an author. I don't know whether, I mean you are the first author,
*  I don't know whether it's an alphabetical order thing or an order of importance thing in your field.
*  How do you list the authors for your publications?
*  Well, it varies. But if you mean the abiogenesis paper,
*  that was work that I started kind of on my own in October and then pulled some other teammates into.
*  And I feel it's a legit first author.
*  Okay, good. Yeah, I mean I get to be first author all the time just because I'm early in the alphabet.
*  So I get more credit than I deserve. I know what it's like.
*  You know, I feel a little bit guilty, but we will get at the end of the podcast to other things you're working on.
*  I mean, you're at Google, you have a job, etc.
*  And does it seem crazy to say that this particular paper we're going to talk about is a little bit outside of what you usually do?
*  Well, yes and no. So for the last year, so starting in October, November of last year,
*  I've kind of changed what I'm doing.
*  So I used to run a pretty large chunk of Google research.
*  I had hundreds of people reporting to me and I was operating more like a VP and had a lot of administrative duties,
*  which were pulling me away from a lot of the things that give me the most joy, the actual work and the thinking.
*  And it also seemed to me that over the past 10 years, a lot of our bets in AI were really starting to pay off.
*  And there's been a rush to really milk the cow, as it were, to really develop transformers and build this generation of AI and make it as useful as possible.
*  And that's wonderful. I'm actually really excited to see that happening.
*  But I didn't want to continue to focus on just developing that.
*  I was really keen to go back to basics and rethink some of the more fundamental aspects of computing and AI.
*  So I started this new group and Google was very generous in supporting me in that.
*  And it's called Paradigms of Intelligence.
*  And it really kind of is going after fundamental stuff, including all the way back to origins of life.
*  That's great. I love it. And am I correct in remembering that you have an undergraduate degree in physics?
*  Yes.
*  This is a long running joke at Mindscape is that I have guests on who do all sorts of different things, but they always started out as physicists before I went into the field.
*  It's probably no coincidence.
*  Probably no coincidence. Exactly right.
*  OK, so the I mean, there's a lot going on in the paper.
*  So maybe talk about what is in your mind when someone says the origin of life.
*  Like, what are the challenges that we have to try to understand?
*  Sure. Well, the first challenge is how did life begin here on Earth?
*  You know, there is a specific story about that, and we may never know all of those details because they're lost to deep time.
*  This all happened four billion years ago.
*  And I've always been very interested in in the work in biology that really tries to unpack that.
*  There are theories about maybe it having been RNA first and RNA world or or maybe a metabolism first that might have spun up in black smokers on the bottom of the sea, where there are these
*  hydrogen and carbon dioxide vents coming, you know, bubbling, bubbling through these porous rock chimneys.
*  But there's a more fundamental question, which is how is it possible for life to arise?
*  In the traditional view of evolution, you need life in order to beget life.
*  There was a lot of work in the 19th century trying to figure out whether life could spontaneously generate and they never got it to happen.
*  You know, you could only get life if life went in.
*  And then if you look at it from a physicist's point of view, you know, I think this this perspective is really well articulated by Schrodinger in his beautiful book from 1944, What is Life, which has been quite inspirational to me.
*  And his perspective was more thermodynamic.
*  You know, if you if you have normal second law of thermodynamics says things get more random over time, life is incredibly ordered and structured.
*  And there's no strict violation of the second law of thermodynamics there because energy has to go in.
*  We need to metabolize.
*  But, you know, while it's permitted by thermodynamics, it doesn't seem exactly encouraged by thermodynamics.
*  There's something mysterious there.
*  I've made that exact same point many times.
*  And I love how you just said it there, encouraged by thermodynamics.
*  It is a little bit mysterious.
*  Right.
*  And so but you see, you're this paper is not delving into the role of chemical catalysts or even entropy and things like that.
*  You're purely on a computer letting code evolve itself.
*  Yes, it doesn't directly speak to that, but it does indirectly speak to it.
*  And, you know, in the in the book that that I'm going to release next year with with MIT Press, what is intelligence part one is all about a biogenesis about about this work.
*  And it does connect it much more explicitly, both with the physics and and with the biology.
*  So there is there is a real connection.
*  It's not it's not arbitrary.
*  I should say there is this field and you refer to it about a life, artificial life different than a.
*  And I think, as you say, I forget exactly where I read this, but it's certainly true.
*  They usually start with something they can already replicate, et cetera.
*  And they're asking, how does complexity grow?
*  How does the effect of genome grow or whatever?
*  But this the idea of doing simulations that in some sense mimic the actual beginning of life is a somewhat understudied field.
*  I get the impression.
*  Totally.
*  I think it's it's never or very rarely probably not really happened before.
*  Right.
*  That we that we begin with just noise or randomness and get replicators, get to get life.
*  And I think the reasons are similar to the puzzles we were just talking about from the biology or physics standpoint.
*  You know, maybe it's partly a mental block.
*  Maybe it's an actual block.
*  But but the idea of like, well, you know, of starting from nothing, it has been understudied.
*  And I don't think it's really it's really been shown before in the field of a life.
*  There is a tension.
*  And I'm entirely on your side vis a vis this tension.
*  But there will be some people who say, look, unless you're really doing chemistry, you're not going to teach us anything about the origin of life.
*  And there's others more physics inclined who will say, I can build kind of a spherical cow model that gets at something, even if it's not ultimately telling me precisely how the biochemistry work at early times.
*  Yeah.
*  Now, obviously, I'm very interested in the real biochemistry, too.
*  So I don't I don't want to discount any investigation into into that kind of work.
*  But I also do think about this like a physicist and and dare I say, like a computer scientist, I'm thinking about life as a phenomenon that is more general than the particular substrate of chemistry and chemistry on Earth.
*  And and in that, by the way, I think I'm very much on the same page as the founders of artificial life, who also happen to have been the same people who founded computer science and who founded artificial intelligence.
*  So I'm thinking especially about Turing and John von Neumann.
*  So is part of the inspiration, even if it's way in the background, the idea that ultimately I'm going to want to ask, here's a thing.
*  Is it alive?
*  It might be on a computer. It might be a physical thing.
*  But like, what are the rules for when I call it life or not?
*  Yeah, I mean, up to a point, life is, you know, whether you call something alive or not is a matter of definition.
*  And we we we have a lot of fuzzy areas, you know, even in biology, is a virus alive or not?
*  Yeah.
*  And so on. So seeking a more rigorous and more functional definition of life is is part of the point.
*  When I say functional, I mean, in the same spirit as Turing's functionalism and von Neumann's functionalism.
*  So, you know, the famous Turing test about about intelligence, you know, it's all about, you know, well, if you if it quacks like a duck, it's a duck.
*  You know, if you if you are talking to a computer, you can't and you and you think that it's intelligent and you can pass all of your tests, then if it functions intelligently, it is intelligent.
*  And I think there's a there's a similar functional way of thinking about about life that that kind of goes beyond the details of which which molecules are are being used or whether they're molecules at all.
*  Good. I mean, like I said, I'm 100 percent I'm not even going to give you a hard time about that.
*  Like, I could not possibly agree with you more.
*  So you're going to do it by running a bunch of computer simulations.
*  And like you said, the the the objective is to really start with nothing or just with randomness and kind of under some set of rules, let it go and see if something lifelike arises.
*  That's the that's the basic aspiration.
*  That's the goal. And to have as little as possible in the beginning, to have as few givens as possible.
*  And then one of the obstacles you run up against is that the best computer language to use for this is something called brainfuck, which apparently is even hard to search for on the Internet because people like to misspell it or something like that to make it sound less bad.
*  But tell us about it.
*  Like put Grolickses or asterisks.
*  Exactly right. So tell us about that language and why you chose it.
*  Yeah, I had to check with MIT's contract whether whether if it was obscene or or something, whether this would would pass.
*  And it's not your fault. It's a free system.
*  Not my fault. Yeah, no, no, it was invented 40 years ago or 30 years ago.
*  Sorry. By Urban Miller, a German, actually, physics student.
*  There you go. Go figure.
*  And amateur juggler, apparently.
*  So so yeah, brainfuck is not the only language one can use for doing this for sure.
*  And we've now tested it on many other languages as well.
*  Our the our latest demo, which is very beautiful, made by Alex Mordvintsev, actually uses the Z80, the Zilog Z80 processor.
*  OK. Which was I had no idea what this is.
*  Well, it came out in 1976.
*  Wow. So it's been around for a long time.
*  And it powered the Osborne computers, TRS 80 and all of that.
*  So like now that's my era now. OK.
*  Yeah, exactly. So it's a bit of a nostalgia trip.
*  And it works just as well in in Zilog assembly language.
*  So it's not it's not required that that it be brainfuck.
*  But the reason that I began with brainfuck is because it's very, very close to a Turing machine.
*  So its its design is is extremely minimal.
*  It has eight instructions.
*  I actually only used seven of them for the first simulations.
*  OK. And it works on a tape that looks just like a Turing tape.
*  So, you know, it's just super minimal.
*  I think Urban Muller made a compiler for it that compiled it to, you know, to assembly language or whatever in one hundred and seventy three bytes.
*  So it's really minimal.
*  So I will remind us because it's a broad audience.
*  What is what is going on in your mind when you say the words Turing machine?
*  Yeah. So the Turing machine is a notional machine.
*  It's a it's a conceptual machine invented in the 1930s by Alan Turing.
*  In many people's minds, mine included, that was kind of the beginning of real computer science.
*  So it was a wonderful paper in which he was trying to not trying.
*  He succeeded in cracking one of Hilbert's big math problems that he had posed in the previous century, which is
*  can one figure out a mechanical way to decide on the truth of a mathematical statement?
*  So this this problem is is one that requires that you actually formulate what computation is.
*  And it turns out that his definition of what computation is turned out to be the much more important part of that paper than the actual result, which was, no, you can't decide a priori on the truth or falsehood of a mathematical statement.
*  But but he he he had a very creative way of of of cracking that that not which was to design a machine that would involve a tape with cells on it that you could write symbols on and a read right head that would be able to step left and right along the tape
*  and a table of rules that would say, you know, based on the state of the of the head and what character is on that cell, whether one should erase, write a new character, step left, step right.
*  And and so that was that's a Turing machine.
*  And then the the next move, the really brilliant move was the universal Turing machine.
*  The idea being that he first showed a Turing machine can compute anything that can be computed by, say, a person with pencil and paper.
*  And then he showed that if you write the rules, if you write that table of rules on the tape itself, then there exists certain tables of rules that will allow you to interpret the table of rules on the tape and carry out the computation that it specifies.
*  And that's that's sort of like, you know, snake eating its tail move gives you a general purpose computer.
*  That's sort of the definition of general purpose computation.
*  And when you say brainfuck is kind of like a Turing machine, it is, in fact, Turing capable, right?
*  It can do anything a Turing machine can do.
*  Right. So this idea of Turing completeness is, you know, does a given machine or a given mathematical system, can you can you map it to a Turing machine?
*  If you can map it to a Turing machine, then by construction, it can compute anything that can be computed.
*  And and brainfuck consists of eight instructions because it's so few, I can actually just say what they are.
*  Please. It's so there's there's a head.
*  The head can step left, step right.
*  It can increment or decrement the byte that it's looking at right now.
*  So it's the tape is a tape of bytes that can range in value from zero to 25.
*  If you increment 25, it goes back to zero.
*  If you decrement zero, it goes up to 25, kind of wraps around.
*  There is an input and output operation.
*  So there's a there's a console in the original brainfuck.
*  So output will, you know, will just emit the byte that is under the head.
*  And input will read a byte into into that position.
*  And then the final two instructions are open bracket and closed bracket, which are looping instructions.
*  So it turns out that for a Turing machine, you need branching in order to be able to implement loops.
*  You need if then. And and so the brackets just say at the open bracket,
*  if the byte under the data pointer is non zero, then continue.
*  If it's zero, then jump to the matching closed bracket at the closed bracket.
*  If the byte under the under the head is non zero, then jump back to the open bracket.
*  Else continue. And that's it. That's the whole language.
*  And with that, you can feed it a tape and well, sorry, because you have the tape
*  and the program in the original brainfuck thing.
*  You're going to you're going to modify that.
*  But in the original thing, so there's instructions for the program.
*  And then there's a tape and the head will just bop back and forth, reading the tape, writing to the tape.
*  And that in principle can do any computation we know how to do.
*  Right. With a with a long enough program, long enough tape and enough time,
*  you could implement Windows on that or whatever you want.
*  Although it would be an absolute nightmare.
*  The reason that that that urban named the brainfuck is because it is very, very hard to program it.
*  So, you know, you look at a Hello World program and it's just this incomprehensible jumble of characters.
*  It's hard to program, but even harder to read, because, like you said, it's all just like plus bracket dot dot dot dot.
*  And you have no idea what's going on.
*  Right. And not a very user friendly language, but a Turing complete one.
*  And good for your purposes, precisely because the set of symbols is so tiny.
*  Right. Exactly. It's a tiny set of symbols.
*  It's not the smallest Turing complete language, but it's it's down there.
*  It's it's it's among the smallest Turing complete languages you can make.
*  So one can both simulate it really fast and one can do a lot of interesting mathematical analysis on it.
*  That would be harder with a more complex language.
*  Right. And you do.
*  And in fact, what you folks implement is a variant of this, which I already sort of spoiled.
*  But the tape and the program are in the same place.
*  Yes. So the the thing that needed to be changed about the original brainfuck is that it has a separate.
*  In effect, it's really two tapes, even though that's not the way Urban put it, you know, in the specification.
*  Yeah. So there's a there's a program tape and a data tape.
*  And the program tape has its own read head, which just kind of steps along.
*  You know, and occasionally jumps back with those loops and the data.
*  The data tape is separate.
*  We wanted to make it self modifying.
*  So self modifying code means that the code itself is actually in the data space
*  and it can be manipulated just as just as well as as as data can be.
*  And why did we want to do that?
*  Well, because I had a hunch that self modification was actually the key to a biogenesis,
*  the creation of life.
*  And I can explain a little bit more about about why.
*  But maybe I'll save that for a bit later.
*  So anyway, there's there's now just one tape and that tape contains both code and data.
*  And this means that you have to imagine that there are actually not two, but three heads now.
*  OK, because the other thing the other thing that was on the original brainfuck was a console.
*  And we didn't want to have a console that is separate from, you know, from the tape.
*  So everything has to be self contained.
*  So now you have a an instruction pointer that walks along the tape.
*  You have a data pointer that can be moved anywhere along the tape.
*  And you have a console pointer, which says if you're going to print or input like
*  where in the tape are you going to are you going to print an input?
*  So everything is all in the same, you know, in the same tape.
*  Right. Good. And then so this gives you a toolbox or a sandbox, I suppose, in which you can play.
*  And you're going to play by starting, like you said, with nothing and let it rip.
*  See what happens. But there's some details there.
*  You can't just let one program go. That would be uninteresting.
*  Right. So so the other the other trick and we called we called this environment BFF, by the way,
*  for reasons that might might become obvious soon.
*  But but the the trick is that we began with a soup of tapes and these tapes are a fixed length.
*  They're of length 64. OK.
*  And and rather than just running one tape, tapes are actually run in pairs.
*  So you grab two tapes out of the soup and you stick them end to end.
*  And then you think of that as the tape and you run it.
*  It's everything is self-contained. So it could modify itself.
*  Then you break those tapes back apart and you put them back in the soup.
*  And that's it. And you do that over and over.
*  You also occasionally, you know, there's a mutation rate.
*  If if if you allow mutations to happen, then once in a while, a bite in that soup will get randomized.
*  It'll just get something random.
*  And there's one more detail, which is that since it's possible for a program to get stuck in an infinite loop,
*  you need to have either some maximum number of instructions that are allowed to run
*  or have some probability, which is the way I prefer per unit time, that that any given tape will just stop running wherever it is.
*  So so those are the extra bits. There's no fitness function.
*  In other words, there's no specific, you know, function that is saying any tape is better than any other tape.
*  You're just plucking them out of the soup, sticking them into and running, putting them back and repeating millions of times.
*  And when you stick them in, and so it's not like you take the first half of one and the second half of the other.
*  You just you have I'm trying to get in my brain what the specifics are.
*  So you just run the two of them next to each other.
*  And there's some topology on the graph. There's some meaningfulness to nearest neighbors.
*  Right. So each of each tape is 64 bytes.
*  If you stick them into and you have 128 bytes.
*  Yeah. And that's and you think of that as the tape that you run.
*  Now, this may seem a little arbitrary, but the reason that that was important is because in addition to self modification,
*  life relies on interactions.
*  Yes. So, you know, you have to have stuff that is interacting.
*  You know, if you if nothing interacts with anything, nothing can happen.
*  So, you know, in chemistry, that would be molecules interacting with each other.
*  So you could think about those those those tapes as being like molecules.
*  Yeah. So and so the tapes are modifying themselves and their neighbors, just like people or real organisms actually do.
*  OK. And so starting give us a give us an intuition for what a random code in brain fuck would do.
*  I presume we just crash or maybe it would be an infinite loop.
*  Usually, I don't know. It's actually quite hard to make an infinite loop from just random noise.
*  That's probably right. OK. Because, you know, remember,
*  so in my version of brainfuck and BFF, there are seven instructions.
*  Every byte can have 256 values.
*  So only seven two hundred and fifty six of the bytes even code for an instruction at all.
*  If something doesn't code for instruction, it just gets skipped over.
*  So it's just because it's a it's a no up, as you call it in computer science.
*  So so what that means, I mean, that's roughly one one in thirty two.
*  That means that out of the 128 bytes in a tape, you'll you'll only have a small handful, you know, two, three, four,
*  you know, working, working bytes, your bytes that actually have an instruction on them.
*  So what might those bytes be like, you know, move the move the head two times to the left and one time to the right.
*  Done. OK. And no change.
*  So in the beginning, very, very little computation is happening.
*  And, you know, it just seems like a very unpromising start.
*  So I shouldn't say crash, but it does.
*  It moves around and then fizzles out.
*  It just stops and nothing interesting happens.
*  Right. Yeah. So it is it is possible for it to crash.
*  If you get to a closed bracket and there was no matching open bracket, that's a crash.
*  But but I think that's the only way it can crash.
*  Good. I mean, that's it's so it's harder to crash in brainfuck than it is in just regular program languages.
*  Yeah. Yeah. Which was also part of the point that it was, you know, it's kind of open ended enough that it's a little robust.
*  Almost anything will do something, even though very little of that something will be useful.
*  And well, how quantitative can we be about that?
*  I mean, what fraction of things that those bytes could be doing will give us interestingness in some well defined way?
*  Well, out of those seven instructions, only three of them actually result in a change to the tape.
*  There's plus and minus, which increment and decrement whatever byte the data pointer is on.
*  And there's comma, which is the copy instruction.
*  So that that was originally input, the input from the console.
*  But if you think about, you know, print and input, they're really the same thing.
*  They're just copy from one place to the tape to the other place, another place in the tape.
*  Sure. Since the console and the data pointer are just different spots, the same tape.
*  So that's why we could reduce it from eight instructions to seven.
*  So only those three instructions can result in changes at all.
*  So that tells you that, you know, if you don't have loops and, you know, you're understaffed,
*  you know, you're unlikely to get a good loop because that requires matching open bracket and close brackets
*  somewhere that enclose, you know, one of one of these right statements.
*  So, you know, in the beginning, yeah, you can be very quantitative and you can calculate the probabilities that anything will change.
*  And they're not high. You know, it's it's it's you know, the majority of interactions result in nothing.
*  OK, very good. And then how many see basically you're doing parallel, many tapes, many programs,
*  whatever you want to call them at once. How many were you doing in your simulations?
*  So we well, in the first ones, I did eight thousand one hundred ninety two tapes in some of my later ones.
*  I only use one thousand one thousand twenty four.
*  So one thousand twenty four tapes is plenty to get all of the interesting phenomena.
*  Right. And then so I don't want to put words in your mouth.
*  Tell the audience what happened. You put in some primordial soup and you let it percolate.
*  Yes. So in the beginning, you know, there are about two operations run per interaction and nothing much happens.
*  And it looks it looks boring unless you look very closely, but we didn't look closely to later.
*  And and then at some point, a few million interactions in typically.
*  Everything will start to change and it's very, very sudden.
*  So on my computer, you know, when I when I first ran this, you know, it was just sort of things were scrolling by really fast.
*  And suddenly the scrolling stopped and it was sort of going chunk, chunk, chunk.
*  And the fan turned on. You know, it's like suddenly a lot of computing was happening.
*  And the number of operations running per interaction just leaps from, you know, very small numbers to thousands.
*  And if you look at the contents of the tapes, suddenly they are full of instructions.
*  They're dense with instructions and they're very complex.
*  And moreover, they're replicating.
*  So, you know, you find a bunch of copies of different programs and these programs are interacting in complex ways.
*  So, you know, it's really quite dramatic.
*  What does I think this is implicit in what you said already, but what is replicating mean in this context?
*  Is it one program is writing itself onto its neighbor?
*  That's actually a more profound question than it sounds like.
*  So the simple definition of replicating is, I mean, the simplest version, I guess, of replication is, you know, you start running a tape and the first 64 bytes copies itself onto the second 64 bytes, for instance.
*  If that happens, then when you pull them apart, regardless of what was in the second half, you know, you now have two copies of what was in the first half.
*  That's replication. And that will definitely take off exponentially when it happens.
*  But the reason it's a it's a subtler question than it sounds like is that you can also have little bits of the tape replicating themselves, which which it turns out happens earlier in the process.
*  And you can even have situations where, for instance, you know, one thing creates another thing, which creates another thing, which creates another thing, which eventually comes back around and sometimes creates the original.
*  So you can have these complex life cycles.
*  And that's a form of replication to anything that that ultimately comes back around and generates more of you than would happen in the in the null case.
*  You know, if there's if nothing is going on, is replication, however weak.
*  I think that actually that is reminiscent of a finding in the sort of more chemically based origin of life context, where it turns out my recollection back when I wrote my book, The Big Picture,
*  you know, mumbly mumble years ago was that they had not built a single molecule that could sort of auto catalyze itself, but they could build two molecule pairs where A could make B and B would make a and would keep going.
*  Exactly. So you finding things like that, basically.
*  Exactly. Which is the same way that the DNA replication works, by the way.
*  Right. You have you have base pairs that are that are that are conjugate.
*  And right. And you know, you pull them apart.
*  One of them makes the other one.
*  And then, you know, and then they conjugate.
*  So so, yeah, that's that's called in a biogenesis.
*  That's called an auto catalytic set of chemicals.
*  And and again, I think that that's a more basic concept than chemistry.
*  There's there's something there's something pretty deep about that.
*  And what we see is exactly the same.
*  And from a pure statistics point of view, is it am I correct to rephrase it as saying that the kind the set of instruction lists, the set of tapes that that act this way is tiny.
*  And the set of all possible tapes, but tends to take over is more robust in some way that I'm still struggling to quite articulate.
*  Yeah. So one of the one of the people who really kind of informed my thinking about all of this is Adi Pras, who is an emeritus professor of chemistry at Ben Gurion University of the Negev in Israel.
*  And he spent many years studying the chemistry of of the origins of life, and he coined this term dynamic kinetic stability.
*  So what he means by that is that normally in thermodynamics, we think about matter
*  arriving at a more and more stable state or in general, some some the statistics of some ensemble becoming more and more stable, meaning that meaning that, you know, if they start out very out of equilibrium, they'll move toward equilibrium.
*  And the closer to equilibrium, the more stable that that configuration is.
*  But but what what Adi Pras realized is that if you have replicators, then you have a new form of stability that arises, which he calls dynamic kinetic stability.
*  If A makes B, B makes C and C makes A, then that has a stability that is actually even greater than the stability of something that takes a long time to degrade, but still ultimately degrades.
*  You know that that replicator can last forever.
*  You have a fragile thing like a soap bubble, or you can have a really robust thing like granite.
*  But, you know, no matter how robust it is, if it's passive, every interaction it has with the world can only degrade it.
*  Right. Whereas whereas the special thing about life and about replicators generally is that they can push back actively against the forces of of of entropy and they can last forever.
*  So that's very evocative.
*  Does it do you see that in the simulations?
*  Is some kind of self repair?
*  Do you see like what would be replicator kind of get influenced by its environment in a negative way and then bounce back?
*  Absolutely. We do see that.
*  But, you know, the very trivial way in which we see that is just that once you have a population of replicators, that's more robust than than than one of them.
*  Right. It's replicating.
*  Then if one of them gets damaged, well, there's another one that can still replicate.
*  So population is the first way that robustness happens.
*  You know, there's there's a force actively making it expand.
*  And so if you damage it, it still comes back.
*  Now you can go further and they can become actually robust and repair themselves.
*  And we do see that kind of stuff happen as well.
*  But but even replication alone is already dynamically stable.
*  And you said that you didn't put in a fitness landscape or fitness function.
*  You didn't sort of rank the success a priori.
*  But isn't there effectively a fitness function or is it just that you sort of well, let me ask you.
*  The phrase is a question. Have you rediscovered natural selection?
*  Yes. We have absolutely rediscovered natural selection.
*  You know, and this goes back to Adi Pras as well.
*  The way he puts it is that dynamic kinetic stability.
*  Sorry, I just go ahead.
*  Yeah.
*  The way Adi Pras puts it is that dynamic kinetic stability is Darwinian selection.
*  And Darwinian selection is just is just another way of putting thermodynamic stability in that
*  in that dynamic setting where you have replicator dynamics in addition to just the normal dynamics of entropy.
*  So yes, there's a fitness function there in the sense that if you if you see a replicator there,
*  at one moment, and you see another string that is not a replicator, and then you look again later on,
*  you're likely to still find the replicator and you're likely not to find the string that wasn't a
*  replicator because it will have been either destroyed by entropy, by random mutation or overwritten by the replicator.
*  So when I think about, I don't know, I want to understand this for my own selfish purposes.
*  I'm doing research in closely connected areas here, and you're very, very helpful right now.
*  Is it really natural selection in the sense that when I think of natural selection, I think of like
*  a handing down of a genome from organ organism to organism and sharing those and mutating them.
*  But I guess you're going to tell me that the whole tape is kind of like a genome.
*  This is also a great and profound question, because there is actually a big change that happens at
*  some magical point in this kind of abiogenesis process, where you go from just an autocatalytic set,
*  meaning just things that tend to kind of sort of make something else that makes something else that makes you
*  to something that has a genome. And what having a genome means is that you now have a list of instructions
*  for making yourself. And if those instructions are changed in any way, that means that you're going to be
*  and if those instructions are changed in any way, that change is preserved in the descendants.
*  In other words, you have heritability. So this goes back to some of the, I think, most foundational work
*  in biology that is not generally acknowledged as work in biology. And it's by John von Neumann,
*  one of the founders of computer science. So when he was messing around at Los Alamos with Stan Ulam
*  and they invented cellular automata. One of the applications that he invented for cellular automata
*  was self-reproduction. And he designed this amazing self-reproduction system using cellular
*  automata that was only simulated on a computer for the first time in the mid-90s, because
*  it's actually very hard to actually make it, like running it is very computationally intensive.
*  We finally caught up to the brain of von Neumann in our computer architecture.
*  I'm not sure if we've caught up, but we got closer. But his insight is actually very easy
*  to express, but very profound. So he said, if you want something that is able to evolve in an
*  open-ended way, replicate and evolve, it needs to have something like a genome. And basically,
*  he was asking, how does something like a bacterium, how does life exist? How is it possible that it
*  can build another copy of itself that is just as complex as it itself is? That seems like
*  pulling yourself up by your own bootstraps. It doesn't make any sense. And what he realized
*  is that you can do it if you have the following things. First, you need a tape, like a Turing
*  tape that has the instructions for building yourself. And then you need a machine A, which
*  will chunk along on that tape and follow the instructions and build whatever the tape says.
*  And then you need a machine B, which can copy the tape, assuming that the tape itself is also made
*  out of stuff that you can find in your environment. If the instructions for making machine A and
*  machine B are on the tape, then you have a replicator. And what's so cool about this
*  realization is he wrote this all up in 1951. This was before the structure and function of DNA.
*  Yeah, it's an obvious thing you think of when you say those words out loud. Like, yeah, that's what
*  DNA does, right? Exactly. So he called it. He totally called it. His machine A is what ribosomes
*  do. His machine B is what DNA polymerase does. And of course, the tape is DNA. And the instructions
*  for building ribosomes and DNA polymerase are encoded on DNA. So it's exactly right.
*  It is one of those events in the history of science that gives you hope for the efficacy
*  of pure thought, right? Like, you wanted something to work out in a certain way, how could it possibly
*  do it? And you figured it out. But, you know, it wasn't that many years before we figured out DNA.
*  I do wonder how influenced he was by people like Schrödinger talking about these things.
*  I'm sure he was. And Schrödinger did also anticipate DNA, although von Neumann went a
*  little further in that he separated, if you like, the machine A and machine B. Like, he realized that
*  there had to be something different about the tape versus the ribosome, which Schrödinger didn't quite
*  connect in 1944. But yeah, it was very profound. And that is more than an autocatalytic set for two
*  reasons. One is heritability. But the other, which is, I think, even deeper, is that this is a Turing
*  machine. What von Neumann described is a computer. Machine A and machine B have to be computers. And
*  the reason is you can't execute the instructions on a tape without having a loop, right? That says,
*  like, if this, then add that. And, you know, at the end, stop. Right? So there's a loop there.
*  You have all of the requirements of a Turing completeness of a computer. So what von Neumann
*  really said is nothing can be life without computing, or rather that life is computation
*  at a very deep level. I love that. I wonder if I've ever heard that phrase that way before,
*  but I don't think I have. It has finally stuck in. Maybe I'm at the right point of my education to
*  appreciate something like that. You know, I don't think that this has actually really been said
*  before. I could be wrong. I mean, it's, you know, people are always, right? These ideas are always
*  bubbling around, and I feel like they're in the air. But I at least have felt like this has come
*  as an aha moment for me just in the past few months. Good. Yeah. No, no, no. When you say it
*  out loud, you're like, oh, yeah, of course. But I've never heard anyone say that out loud before.
*  So that is wonderful. So, okay. So back to the reality of this computer program you're running,
*  how do you know when this happens? You said you were looking at an output, but probably there's
*  something more sophisticated going on. Yeah. It's not just listening for the fan to turn on.
*  Well, so the first, the most obvious thing that happens is you can visualize it very beautifully
*  if you just draw a dot on a graph for every interaction where the X axis is time and the
*  Y axis is how many operations ran in that interaction. So for a long time, you just see,
*  it's low, there aren't many operations happening. And then suddenly at some point, which depending
*  on randomness, it could be after a million, it could be after 10 million interactions,
*  suddenly there's this wall of blackness. The thing is computing really hard. All of these
*  interactions are resulting in thousands of operations running. So that's the tell that
*  something has happened. You can also measure the Kolmogorov complexity of the soup. So Kolmogorov
*  complexity is very simple to approximate. You can just zip the soup. So you just take all the
*  bites in the soup and you think about it as a file and you zip it. And then you take the ratio of the
*  zipped file size to the original, that gives you a sense of how compressible it is. And in the
*  beginning, when you start off with just noise, it is incompressible. Random bites are incompressible.
*  Try it at home. If you make a file full of random numbers and you zip it, it will stay the same size.
*  It will actually grow a little bit because there's a header. But the moment you start to
*  have replicators in there, you expect that it's going to suddenly become a lot more compressible
*  because many of those strings, many of those tapes can be expressed as pasted together parts
*  of other tapes. And that's what you see. You see this dramatic transition from incompressible,
*  it's like a gas, to it's like a crystal. Not quite like a crystal because there's still
*  whole ecology of different tapes, but its complexity drops way, way down.
*  **Matt Stauffer** So there's a phase transition. And the order parameter could be either the number
*  of computations being done or the algorithmic complexity of the soup.
*  **Senghor Nohri** Yes. That's right. It looks exactly like a phase transition. And usually,
*  when a physicist talks about phase transitions, we think about correlation functions. So in a gas,
*  the correlation function is just a delta function. The other particles could be anywhere.
*  If it's ice, then it's this very crystalline structure. Well, compressibility and that
*  correlation function are obviously much the same thing. Gas is incompressible because the position
*  of one particle doesn't tell you anything about the positions of the other particles. So you could
*  call that first stage a Turing gas, which is what Walter Fontana, who is also a pioneer in
*  abiogenesis on computer called it. But then after that phase transition, it's something else. It's
*  no longer a gas. I would call what you get afterward computronium, meaning it is a new phase of matter,
*  if you like, that is all about computation, which I think another word for that is life.
*  **Matt Stauffer** Yeah. No, I mean, I'm on the train. I guess the one thing that I don't,
*  if I wanted to be the skeptic or at least the curmudgeon worrying about chemistry and things
*  like that, a computer program where you have some instructions to change what's on the tape
*  seems to be lacking some notion of energy or a Hamiltonian or dissipation or entropy or something
*  like that. So ordinarily when I have a phase transition, I'm thinking of, oh, the system has
*  found a lower energy configuration it can be in, but you don't have energy or do you?
*  **Matt Stauffer** Not in any obvious sense. So nothing is conserved in BFF. Bites aren't conserved.
*  Everything is just pure information. So one can talk about entropy, but one can't talk about energy.
*  However, there is, I think, a deep connection with energy in the real world, which is that
*  we know that computation requires energy. Now there is this whole field of reversible,
*  so-called reversible computation, but the way you get reversibility in computation is by
*  having these so-called ancillabits, extra information that comes out that you have
*  to store somewhere. **Matt Stauffer** Right. You make the system bigger.
*  **Matt Stauffer** Yeah, exactly. So in a way, it's just saying we shrink the part of the system we
*  look at in such a way that we're not looking at the extra information. So I think to make a long
*  story short, I think there is something profound about computation that requires energy use because
*  of its irreversibility, because computational operations involve these irreversible steps.
*  **Matt Stauffer** That makes perfect sense to me, but I can't quite in my brain connect it to the
*  robustness and survivability and hegemonic aspirations of your reproducing codes. Is there
*  a physics-based way of saying why they want to take over? There need not be, but I'm just wondering.
*  **Matt Stauffer** Well, I think that the reasons they want to take over are purely statistical.
*  So in that sense, you don't have to invoke energy. You can just invoke statistics,
*  likelihoods of finding something later if you find it in the present. But in real life, because
*  heritable replication requires computation, in other words, you can't have a von Neumann
*  replicator without it being made out of Turing machines that are computing. That means that you
*  need an energy input in order to get a replicator. So that's why metabolism is required in real life
*  to have replicators. **Matt Stauffer**
*  Maybe this is a weird out of the field question, but maybe I'm answering myself in my brain because
*  you already said there's no conserved quantities here, but ordinarily when I take a physical system
*  and just let it go, eventually it will reach equilibrium. It loses all structure. I wrote a
*  paper with Scott Aronson once where we showed that complexity can grow for a while and then
*  eventually it's got to fade away because you're going to equilibrate. But I'm thinking that in
*  your thing, it's going to remain in this fun complex phase more or less forever. **Matt Stauffer**
*  It will. And the reason is that it's a dissipative system. So the fact that it's computing, the fact
*  that you're constantly computing means that effectively there is energy constantly going in.
*  **Matt Stauffer** So you have a resource. You have the sun.
*  **Matt Stauffer** Yeah. That's why the fan is going on my computer when I'm running DFF.
*  But it won't. So yeah, it won't. The order will not go away. The structure will not go away,
*  but neither will it stabilize to just one thing. So it's this very complex ecology. And what is
*  so wonderful about what happens after this transition to life is that you might think
*  naively, oh, one replicator takes over and that's it. It's just a crystal of that one thing. It's
*  not. You have this whole kind of power law distribution of different replicators all
*  interacting with each other and they keep evolving forever and changing.
*  **Matt Stauffer** Wonderful. And it does remind me that it's probably now time for you to tell us
*  what BFF stands for. **Matt Stauffer**
*  Well, the first BFF still stands for brainfuck. So given that it's interactions between two tapes,
*  you might be able to guess what the second F stands for as well. Or we could just say
*  best friends forever. **Matt Stauffer**
*  Best friends forever. That's even better. Okay, good. Now let's try to relate this to questions
*  that are sometimes raised about the origin of life. Does it require fine tuning of the laws
*  of physics? Are there free parameters in your process that could have been changed and made
*  the results different? **Matt Stauffer**
*  Yes. So there is one thing that went in, which is the design of the language. And we do know
*  that different designs of language result in either very different times to abiogenesis,
*  or in some cases, we don't see biogenesis at all, which I think means just that the time is
*  so long that we're not able to see it happen. So one could almost write a theorem. In fact,
*  one could write a theorem that just abiogenesis will happen in this kind of environment. In an
*  environment, in other words, where computation is possible and where there's a noise source
*  and where there are interactions, it will happen. But the question is, how long statistically will
*  it take? And details of exactly what the instruction set is can make that vary quite a lot.
*  One of the really profound results of this that is not in the original paper, but that I feel like
*  we've just figured out, again, in the last few weeks, actually, is that there's a classic view
*  of evolution, that it all happens via Darwinian selection. Jacques Monod, one of the winners of
*  the Nobel Prize, is famous for saying it's just chance and necessity. You just have random
*  mutations and the Darwinian selection, whatever sticks. It's spaghetti being thrown at the wall,
*  it's a million monkeys and a million typewriters, and eventually things stick and there's a ratchet.
*  So we now know that that's not how this works. And there's been a rising tide of skepticism about
*  that very reductive Darwinian view for many years, but I think we now have the receipts.
*  So what is actually going on, and well, I should say, what are the receipts? The most obvious
*  receipts are that if you turn the mutation rate all the way down to zero in BFF and you just start
*  with a thousand random tapes of length 64 and you let it go without any mutation, you still get
*  complex life arising. And that's kind of mind blowing because a thousand times 64,000 random
*  bytes, that's just not a lot of monkeys and not a lot of typewriters. There aren't enough
*  characters there. You can barely find three working instructions in a row.
*  So sorry, there's still randomness in the sharing between nearest neighbors, but there's not
*  randomness in mutations. Right. So there's randomness in the initialization. You start
*  off with random bytes and there's still randomness in choosing neighbors to interact, in choosing
*  which ones to interact with. Although frankly, I'm pretty sure you could get away with that too.
*  I mean, you could just say everybody interacts with everybody and we just go on that way. That
*  would work just as well for sure. So the only randomness would be in the initial configuration.
*  Yes. Yes. And that just doesn't seem like enough randomness to generate these very complex programs
*  that come out. So what's going on? Well, when you look closely at what's going on, what you see is
*  the following. First of all, even from the very beginning, before a replicator arises,
*  you already have individual instructions forming autocatalytic sets. Meaning if you have a copy
*  instruction, for instance, then there is some possibility that what it generates is also an
*  instruction. If there's a no-op, if there's a non-instruction, there's no possibility for it
*  to make anything. But if it's an operation, then there's a possibility that what it will make is
*  another instruction and maybe that other instruction will come back around and eventually make another
*  of it. So in other words, you already have the makings. The most primitive life forms in a sense
*  are literally just single instructions. And they begin to beget each other. Instructions
*  beget instructions. You start to see the number of computations rising, if you look closely,
*  right from the very beginning. And so you begin to see more instructions coming in and they're
*  kind of moving around at random. They're copying themselves into random spots. And it's a creative
*  process because once in a while, if a couple of them end up in conjunction and together,
*  they can replicate more effectively than they could separately, then they're likelier to survive.
*  So you get symbiosis really as the driver of evolution. The symbiosis between instructions
*  to make little tiny programs, symbiosis between those little tiny programs to make
*  bigger imperfect replicators. And eventually, those bigger imperfect replicators, which are all
*  madly writing over each other, competing, cooperating, will eventually fuse into a stable
*  whole tape replicator. So it's symbiosis all the way down.
*  Right. Okay, good. So if the audience will indulge me in being a little specific here,
*  because you're provoking me to think of new theorems to prove, because in that case that you
*  thought about where there's no randomness in the interactions, there's only randomness in the
*  initial conditions, then the evolution is deterministic. So in that case, if you think
*  that that will, with high probability, lead to this takeover by replicators, then there is some
*  statistical mechanics statement, right? It's not saying that most instruction sets are
*  replicators, but the future trajectories of most instruction sets will end up in this
*  replicator dominated regime. Yes. It's telling you that computing is a dynamical
*  attractor. Yes. And it's a dynamical attractor because only by having computing can you get
*  replication and replication is a dynamically, kinetically stable state.
*  Because the evolution is not reversible, right?
*  Right.
*  Okay. So you can get attractors and you do. Good. I would like to see that theorem. That
*  would be good. I'm looking forward to that coming out.
*  If you are a game to work on the theoretical physics of this, we would love that.
*  Let's talk. I don't know whether I'm competent, but I'm super duper interested. So good. Well,
*  that's very good.
*  It's very Santa Fe for sure.
*  It is. Absolutely. Right. So what, at the end of the day, how grandiose can we be about
*  drawing implications from this study? For example, for how easy it is for life to form in the more
*  conventional, wet and sloppy biological sense.
*  Well, I think that there are a lot of pretty grandiose conclusions, which is why this is a
*  whole book. So first of all, it seems to me that life wants to form. It's the very opposite of
*  what Francis Crick once said about life being like a miracle. It's hard to imagine how it could
*  possibly happen. I think it's the opposite. Because computation is a dynamical attractor,
*  I think that it will form whenever it has a chance to. And I guess as we start to explore
*  the moons of Jupiter or have better telescopes or whatever, maybe we'll start to see real evidence
*  of that. Furthermore, I think we can say that because symbiosis is the driver of evolution,
*  there's this kind of ladder wherein more complex entities form out of simpler entities. And I think
*  that's a very general property as well. Lynn Margulis famously thought that this was the way
*  evolution worked. She was the discoverer of mitochondria, having been endosymbiotic and
*  thereby forming eukaryotes. She believed that all sorts of things, all of the organelles of the cell
*  had been free swimming originally. She was wrong, probably. But I think she was right at a deeper
*  level in the sense that the idea of an organelle evolving inside a cell, it's still an evolutionary
*  step of a symbiotic character, whether or not it began on the outside. The inside of a cell is just
*  as fertile an evolutionary landscape as the outside. And in fact, I'm realizing I haven't
*  mentioned this, but even after that transition to full tape replication, we see the amount of
*  computation continuing to rise. The number of characters that compute still continue to rise.
*  And the reason is that when the whole tape is getting replicated, not all of it is needed
*  for the instructions that do the replication. So it's an ecology, if you like, where this whole
*  process can repeat. And you get replicators inside replicators, and sometimes those will
*  confer resistance to mutation to the larger replicator and so on. So I think that I would
*  tentatively conclude that we haven't learned much about the robustness of the origin of life to
*  changes in the laws of physics. Because if you change the laws of physics of our world, that'd
*  be like changing the instruction list or whatever, and maybe you would just get something that
*  produces nonsense or only has one instruction. But given that we know the laws of physics,
*  I think you're making a strong but plausible claim that this should increase our credence that
*  life's going to pop up everywhere. Some kind of life, maybe not intelligent technological life,
*  but some kind of complex computing life. Right. I mean, there are barriers to every
*  symbiotic genetic transition, and they're statistical. And they could be of varying
*  sizes. Those steps can be of varying sizes. So you're not guaranteed that you'll make your way
*  all the way up the staircase, as it were. But there is a real tendency to go up the staircase.
*  And every time you go up to the next step, you have a chance to get to the next step.
*  Now, as for the laws of physics, I mean, we know that the laws of physics in our universe allow
*  computation. So that means that if you like, there are many no ops in the universe, many interactions
*  that are not part of a set of operations that form a Turing complete set, and thereby also
*  form an autocatalytic set. But if there is an autocatalytic set in there that is Turing complete,
*  that's sufficient. And we know that you can make a computer out of almost anything, right?
*  Right. We've done it. We've made computers out of things. That's an existence proof. Yeah. Okay.
*  Does it, this is probably unfair, but does it give us any inspirations for how to look
*  for life elsewhere? That's a great question. And it's definitely something I've been thinking about.
*  There are relationships between these ideas and some of the ideas of Lee Cronin, Sarah Walker,
*  constructor theory or assembly theory. Assembly theory.
*  Might also be connections to constructor. Constructor theory too. Yeah.
*  Which is a little, yeah. That's right. So Chiara Marletto's work with
*  constructor theory also very relevant here. So yeah, those are connections that have yet to be
*  really fleshed out. So Sarah and Lee believe that there are implications for how to look for
*  complexity elsewhere. I think that assembly theory is quite compatible with what I'm describing.
*  I don't know if what I'm describing adds more meat to what we should be looking for
*  observationally. It might. Okay. Fair enough. And I would be remiss if I didn't give you a chance
*  to talk about the many other things you do. I mean, this is kind of not your, it has not been
*  like your main job title and you're writing books about all sorts of things. I mean, how should we
*  segue into this? Should we talk about what is intelligence? And so you talked about what is life?
*  Sure. So I mean, there is a reason that, and you're right, abiogenesis and origins of life
*  are definitely not my field. And I've been working on it for less than a year.
*  However, our group has been working in a life related stuff for a while. So Alex Morvincev,
*  who I mentioned earlier, is also the inventor of neural cellular automata, for instance,
*  which were a very beautiful kind of mashup of cellular automata as invented by von Neumann
*  and neural nets and also morphogenesis, which really was pioneered by Alan Turing. So the idea
*  behind NCAs, behind neural cellular automata is that you have a grid of pixels and in every pixel,
*  you have a neural net. It's the same neural net everywhere. And it senses and modifies the local
*  concentrations of a handful of channels. Those channels are scalar values. You could think about
*  them as morphogens, you can use chemicals that allow cells to communicate with each other.
*  And you can train one of these NCAs to make any image you want. The first one that I ever saw was
*  like a lizard emoji and you could like wipe out its head as well as its tail and it would
*  regenerate itself. So it's essentially a model for morphogenesis that combines cellular automata
*  with neural nets. So we've been thinking quite a lot about local computation, both because it's a
*  way to attack efficiency in AI computing and ultimately all computing has to be primarily
*  local or it's going to be inefficient. And also as a way of thinking more broadly about learning.
*  Because obviously life is all about learning in some sense. The whole point of a replicator
*  is to produce more of itself in its environment. And as that environment becomes more complex and
*  includes many other replicators, this kind of dynamical modeling starts to become more and
*  more a part of it. So if you just keep walking along this symbiotic path, you get eventually to
*  brains and to AI. I guess in your model, in the model we've been talking about in the paper so
*  far, the quote unquote environment is just sort of the nearest neighbors of each tape. But a possible
*  next step would be to like throw in an environment, like to have just different,
*  I don't even know what they would be, but how would you model being on a planet versus not being on
*  a planet or being in the ocean versus being on land? I don't know. It's a great question.
*  And we've definitely sort of thought about and tried out a little bit some approaches like
*  particle NCAs plus BFF. Particle NCAs is like a neural cellular automaton except that there are
*  particles that can move around rather than just pixels that stay put. So yeah, those are all
*  exactly the kinds of mashups that we'd like to try. Actually the Z80 simulation that doesn't use
*  brainfuck but uses the Z80 assembly language instead, it actually works on a grid. So it's
*  a grid of 200 by 200 processors and their interactions are all nearest neighbor rather
*  than random. And you get these spreading waves of replicators of different species and stuff.
*  Right. And is there a video? There is. Yeah. Okay, good. I'll have to look for that.
*  Yeah. I think Alex is just putting it up on the web now. So yeah, I'll send you the URL.
*  Yeah. I mean, there is this remarkable universality in these kinds of videos but also just the concepts
*  behind them of phase transitions and domains of things growing, whether it's the Ising model
*  or the Schelling model in social sciences and everything, you know, that it does attract a
*  certain Santa Fe Institute kind of person to think there must be connections. It can't all just be
*  coincidence, right? There must be ways of thinking about this that are higher level and bring
*  everything together. Yeah, I think so. I mean, I've thought for a long time that intelligence
*  is fundamentally symbiotic in the sense that the social intelligence hypothesis holds that, you
*  know, we are smart because our environment is each other. And because you're constantly trying to
*  model others, you know, and thereby also model yourself and how others see you and so on,
*  you end up with these intelligence explosions precisely because our environment is each other.
*  So I think there's a deep continuity between these very, very primitive, you know, replicating
*  programs and that perspective. Of the many previous podcasts that I've had that are relevant to what
*  you just said, Hugo Mercier, do you know his work? Yeah, I do. Yeah, the Mercier and Sperber book,
*  The Enigma of Reason, is, you know, it's one that I cite in my book and I very much agree with
*  their ideas about language. And so you're pointing in the direction of saying that not only life but
*  intelligence might be more ubiquitous than we think with obvious connections to, we're building
*  intelligent like things. So what is your take on the intelligence of modern AI models?
*  Well, you know, when we first began working on AI, you know, I think a lot of people were
*  thinking about social intelligence and they were just thinking about tasks. And so there was this
*  long period, well, I don't want to go through the whole history of AI, but the supervised learning
*  era was all about, you know, training models to optimize something. And I mean, you might notice
*  that BFF is not optimizing for anything. Yes, it tends statistically right toward like what persists
*  exists, but there's not a, we haven't defined a task. And the interesting thing about AI that
*  was specific to doing a task is that the best it can do is to do that task. You know, so that's why
*  we needed the term AGI. You know, originally AI meant, you know, something you could have a
*  conversation with that could do all the various kinds of things that we do. They could fold the
*  laundry, walk the dog. And, you know, and then people started talking about AI as speech recognition,
*  face recognition, you know, character recognition. And I was like, that's not, that's not AI, you
*  know, that's just, and the moment we actually came up with real AI was the moment we stopped
*  optimizing for specific tasks and started to just model free form text on the internet. Now,
*  text on the internet is obviously not everything, but language is special in the sense that it
*  represents everything in our Umwelt that we care about enough to talk to each other about.
*  Right. So, you know, it's a microcosm, right, of everything. And it's just modeling that it's just
*  trying to predict next tokens, which amounts to building a model of that entire distribution.
*  And that was intelligent. I am, you know, I'm definitely not in the majority on this,
*  but I believe that today's AI models are absolutely intelligent. You know, there's a lot of talk about
*  this, you know, it's just next token prediction. It's just this, just that. I mean, I think brains
*  fundamentally are about predicting the future. And the moment we just started to try and model
*  that, you know, lo and behold, we got out stuff that is smart. Right. So your attitude is not that
*  large language models, you know, mystically are more than next token prediction, but rather that
*  our brains are secretly next token prediction. Yeah. Although the just, you know, it conceals a
*  lot of beauty and complexity. Right. I mean, in order to do a good job of predicting the future,
*  you have to generalize and, and, you know, generalizing means building internal representations,
*  doing all sorts of very sophisticated modeling. So my line has always been that LLMs in particular
*  are not designed to think in the same way as human beings do, but rather to sort of mimic the output
*  of human thought. And maybe it is possible that in the process of mimicking the output of human
*  thought, they end up thinking like us. To me, there are enough counter examples of, you know,
*  simple questions you can ask that any human could answer, but the LLMs fail at to assure me that
*  that's not what's going on right now. But I don't know, you know, this game a lot better than I do.
*  Well, it's, it's very much a moving target. You know, I, I mean, there's, there's a lot of
*  gotcha-ing happening on the internet in the last year. Like, Oh, look at the stupid thing that the
*  LLMs said, you know, I, to be honest, you know, one of my first reactions when I started to see
*  that kind of stuff is, boy, these, these models are getting hammered. I can only imagine what would be
*  happening if I were somehow able to be replicated a billion times and, you know, get hammered with
*  questions and need to respond immediately. And like how many gotchas you would find in that,
*  the null distribution, let's put it this way, has not been well explored. But, but, but I think the
*  point is, is nonetheless, right. That, you know, they're the, the profile of competencies and
*  incompetencies looks pretty different from the average persons. Right. And, and of course, I'm
*  not arguing that everything, everything about the way they work is the same as the way brains work.
*  Not at all. You know, right. We have, we have a very different architecture. You know, neurons are
*  not the same thing as, as artificial neurons in neural nets. The way we've evolved has a lot of
*  path dependence, but nonetheless, I think that there is something profound about the functional
*  standpoint, just as with life, you know, there's something deep that is going on, which is about,
*  about modeling your environment and predicting it and active, doing active inference on it,
*  meaning that you're, you're, you're actively bringing about your own future as part of your
*  actions. And, and it was only when we started to, to in effect, implement that kind of active
*  inference that we began to get models that, that started to pass the turning test. And the whole
*  point of the turning test is, you know, if right, if, if the model behaves in all of these ways,
*  then then she can't, is right. Yeah. Right. I mean, are we, I think the answer is yes, but are
*  we going to have to sooner rather than later confront the question of agency and rights to
*  AI programs? Well, I think the two are very different questions. So, agency, yes, I think
*  that, I think that we tend to reserve the term agency for humans and even withhold it from,
*  you know, animals and plants and so on for reasons that are quite arbitrary and that don't have a
*  lot to do with anything you can really measure or study. So, you know, do plants have agency? Do mice
*  have agency? Yes. Do AI models have agency? Yes. You know, in particular, you know, if you, if you
*  start to have them, you know, I mean, many of the respects in which they have little agency at the
*  moment have more to do with how we have deployed them than they have to do with the models themselves.
*  You know, if it can only respond to a chat interaction, you know, and not make any moves
*  of its own, as it were, then its agency is very limited. But that's not about, about the model.
*  It's about, it's about how it's, how it's been embedded in the socio-technical environment.
*  I think that's fair. I mean, I asked the question because I really don't know what the answer is.
*  And I am curious. I would, I'd be very happy to attribute more agency to a good
*  modern AI program than to a tree. But I think that it might be low in either case. I'm not sure yet.
*  I could be convinced. Well, you know, there's, there's a, there's a wonderful book that I read
*  years ago by James C. Scott, the agronomist, the late James, James C. Scott, unfortunately,
*  I think he's just died recently, but, but it's called Against the Grain. And, you know, he,
*  he questions whether we really domesticated wheat and, and other agricultural plants.
*  You know, the, the basic observation being human life got a lot worse after we began farming and
*  it has only recovered very recently, like very recently, since 1900 or so. And there's a way
*  of thinking about what happened in, in, in plant domestication that looks more like
*  plants domesticated and even concentration farmed us essentially, you know, they enslaved a lot of
*  humans to do, to plant massive, you know, massive fields of them and take care of all of their,
*  of all of their needs, you know, at great expense to, to human health and wellbeing.
*  So, I mean, I say this not because I'm necessarily, you know, strongly advocating that point of view,
*  but because I think it's like a necro cube. You can look at it both ways. You know, agency is not
*  simple. Well, it's the selfish gene idea, right? I mean, and, and if we try to be a little bit less
*  judgy about it and we start thinking in terms of the statistical mechanics of trajectories, then
*  maybe it makes perfect sense that this sort of symbiotic relationship was, you can't attribute
*  the causal agency to either one or the other by themselves. Exactly. And one of, one of the points
*  that Mercier and Sperber make in their book, also Sloman et al. in the knowledge illusion,
*  is that we tend to over attribute, if you like, agency to ourselves in a big, big way. And not
*  only over attribute agency, but, but over attribute knowledge, understanding, like, oh, humans can do
*  this, humans can, your humanity is great at this, that and the other, you know, I mean, the average
*  New Yorker doesn't know how a toilet works, right? Right. And, and would be, you know, useless,
*  right? If actually, you know, put out in the, in the jungle, you know, to, right, defend, defend
*  for themselves. So, you know, I think that, I think that it's, it's useful to rethink all of this. I'm
*  not arguing for robot rights. I do want to be clear about this. Well, no, but at some point,
*  we're going to have to have a serious conversation about it, right? I mean, I guess that's the only,
*  only as far as I would be willing to go. I do think that we're going to have to have serious
*  conversations about, about how we think about the relationship between, between human rights
*  and the various things that we have reserved, kind of to humanity as kind of copyrighted,
*  you know, that only we've got, only we've got agency, only we're intelligent, only we this and
*  that. I mean, I'm okay with us making, you know, various political decisions about, you know, how
*  we want humans to be treated as distinct from various other kinds of entities, but I think we
*  should be honest with ourselves that a lot of that has to do with the fact that we are humans,
*  you know, who make these decisions. It's not, it's not, it's not some view from above,
*  wherein we deserve that because we've got souls and nothing else has a soul.
*  Well, maybe that's a perfect segue to like, just the wrapping up kind of thing I wanted to ask
*  about, which is your other book, Who Are We Now? Great title. We human beings, right? And comparing
*  who we are now to maybe who we used to be, who are, who are we now? What's the answer?
*  Well, you know, there's a connection between that book and everything we've been talking about,
*  which is that, you know, my view of the change in human identity that we have undergone over recent
*  times, especially since the melting of the glaciers in the last 10,000 years been accelerating,
*  is that it's all about urbanization. This is also a very Santa Fe idea. And that we have become a
*  collective superorganism. You know, human intelligence is, if you like, a kind of
*  superintelligence that has come about through us symbiotically working together in a new way
*  that we didn't for, you know, the first couple of hundred thousand years that we've been around.
*  So, you know, I think it's another, it's exactly another of those transitions of the kind that we
*  see in BFF, if you like. And we, in not understanding that we've undergone that transition,
*  we continue to confuse what human means, you know, by attributing that larger collective thing to
*  individuals when in fact, it's something new. I guess the only edit I would do there is you say
*  having undergone the transition, I think we're in the middle of the transition. We're nowhere close
*  to the end, which makes it even harder to figure out what the truth, how to deal with it, I suppose.
*  I agree. I think we're in, yes, I overstated we are in the middle of it. And I think a lot of our
*  agita right now comes from being in the middle of it. So, you know, even for instance, you know,
*  to bring a little bit of geopolitics into it, when you and I were growing up, we were in the
*  middle of a hemispheric Cold War of, you know, USSR versus the West. And you could imagine
*  one of those collapsing and the other one winning, right? There was a zero sum kind of thing there.
*  And that's what happened. So, you know, the economy of the USSR could collapse, and that would mean
*  that the West had won. Now, if you look at the rhetoric of, you know, say China versus the US,
*  it is completely different, because their two economies are intimately intertwined.
*  You can't have the Chinese economy fail and that be a good thing for the US or vice versa. So,
*  you know, we're kind of in it now at planetary scale. And yet we haven't quite understood that
*  we have to be operating at planetary scale yet. A different former guest of mindscape is Henry
*  Farrell. And his phrase for that is weaponized interdependence. We have to learn to live along.
*  It's not mutually assured destruction, but it's, you know, if we don't all succeed, then it's going
*  to be bad for everybody. Right. Well, I think what we have is mutually assured survival.
*  And if we choose wisely, and if we don't choose wisely, then, you know, we're, yeah,
*  we kind of can only go forward or back. Right. We can't, I think we can't quite stay where we are.
*  That's a very set of wise words, very wise set of words to end on. I can't do any better than that.
*  So, blazagera i arkas. Thanks very much for being on the Winescape podcast.
*  Sean, thank you so much. Wonderful, wonderful questions and insights and thoughts. And yeah,
*  the door is wide open if you're interested in working on this stuff.
*  Let me think and let's talk. I'm very interested. So, all right. Thanks.
*  Take care.

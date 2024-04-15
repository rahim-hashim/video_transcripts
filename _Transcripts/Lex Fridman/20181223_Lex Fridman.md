---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 4798s
Video Keywords: []
Video Views: 123455
Video Rating: None
---

# Juergen Schmidhuber: Godel Machines, Meta-Learning, and LSTMs | Lex Fridman Podcast #11
**Lex Fridman:** [December 23, 2018](https://www.youtube.com/watch?v=3FIo6evmweo)
*  The following is a conversation with Jürgen Schmidhuber. He's the co-director of the CS
*  Swiss AI Lab and a co-creator of long-short-term memory networks.
*  LSDMs are used in billions of devices today for speech recognition, translation, and much more.
*  Over 30 years, he has proposed a lot of interesting, out-of-the-box ideas on meta-learning,
*  adversarial networks, computer vision, and even a formal theory of quote,
*  creativity, curiosity, and fun. This conversation is part of the MIT course on artificial general
*  intelligence and the artificial intelligence podcast. If you enjoy it, subscribe on YouTube,
*  iTunes, or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D. And now,
*  here's my conversation with Jürgen Schmidhuber. Early on, you dreamed of AI systems that
*  self-improve recursively. When was that dream born?
*  When I was a baby? No, that's not true. When I was a teenager.
*  And what was the catalyst for that birth? What was the thing that first inspired you?
*  When I was a boy, I was thinking about what to do in my life, and then I thought the most
*  exciting thing is to solve the riddles of the universe, and that means you have to become a
*  physicist. However, then I realized that there's something even grander. You can try to build
*  a machine that isn't really a machine any longer, that learns to become a much better physicist than
*  I could ever hope to be. And that's how I thought maybe I can multiply my tiny little bit of
*  creativity into infinity. But ultimately, that creativity will be multiplied to understand the
*  universe around us? That's the curiosity for that mystery that drove you?
*  Yes. So if you can build a machine that learns to solve more and more complex problems, and more
*  and more general problem solver, then you basically have solved all the problems,
*  at least all the solvable problems. So how do you think, what is the mechanism for that kind of
*  general solver look like? Obviously, we don't quite yet have one or know how to build one,
*  but we have ideas and you have had throughout your career several ideas about it. So how do
*  you think about that mechanism? So in the 80s, I thought about how to build this machine that
*  learns to solve all these problems that I cannot solve myself. And I thought it is clear it has to
*  be a machine that not only learns to solve this problem here and this problem here, but it also
*  has to learn to improve the learning algorithm itself. So it has to have the learning algorithm
*  in a representation that allows it to inspect it and modify it, such that it can come up with a
*  better learning algorithm. So I call that meta-learning, learning to learn, and recursive
*  self-improvement. That is really the pinnacle of that, where you then not only learn
*  how to improve on that problem and on that, but you also improve the way the machine improves,
*  and you also improve the way it improves itself. And that was my 1987 diploma thesis, which was
*  all about that hierarchy of meta-learners that have no computational limits except for the
*  well-known limits that Gödel identified in 1931 and for the limits of physics.
*  In the recent years, meta-learning has gained popularity in a specific kind of form.
*  You've talked about how that's not really meta-learning
*  with neural networks that's more basic transfer learning. Can you talk about the difference
*  between the big general meta-learning and a more narrow sense of meta-learning the way it's used
*  today, the way it's talked about today? Let's take the example of a deep neural network that has
*  learned to classify images. And maybe you have trained that network on 100 different databases
*  of images. And now a new database comes along, and you want to quickly learn the new thing as well.
*  So one simple way of doing that is you take the network, which already knows 100
*  types of databases, and then you just take the top layer of that and you retrain that
*  using the new label data that you have in the new image database. And then it turns out that it
*  really, really quickly can learn that to one shot basically, because from the first 100 datasets,
*  it already has learned so much about computer vision that it can reuse that, and that is then
*  almost good enough to solve the new task, except you need a little bit of adjustment on the top.
*  So that is transfer learning, and it has been done in principle for many decades. People have
*  done similar things for decades. Meta-learning, true meta-learning, is about having the learning
*  algorithm itself open to introspection by the system that is using it, and also open to
*  modification, such that the learning system has an opportunity to modify any part of the learning
*  algorithm, and then evaluate the consequences of that modification, and then learn from that
*  to create a better learning algorithm, and so on, recursively. So that is a very different animal
*  where you are opening the space of possible learning algorithms to the learning system itself.
*  Right. So you've, like in the 2004 paper, you describe Gaito machines, programs that rewrite
*  themselves. Philosophically, and even in your paper, mathematically, these are really compelling
*  ideas, but practically, do you see these self-referential programs that are being used
*  in the near term, to having an impact where it demonstrates to the world that this direction
*  is a good one to pursue in the near term? Yes. We had these two different types of
*  fundamental research, how to build a universal problem solver. One, basically, exploiting
*  proof search, and things like that, that you need to come up with asymptotically optimal,
*  theoretically optimal self-improvers and problem solvers. However, one has to admit that through
*  this proof search comes in an additive constant, an overhead, an additive overhead that vanishes
*  in comparison to what you have to do to solve large problems. However, for many of the small
*  problems that we want to solve in our everyday life, we cannot ignore this constant overhead,
*  and that's why we also have been doing other things, non-universal things such as recurrent neural
*  networks, which are trained by gradient descent, and local search techniques, which aren't universal
*  at all, which aren't provably optimal at all, like the other stuff that we did, but which are much
*  more practical, as long as we only want to solve the small problems that we are typically trying
*  to solve in this environment here. So the universal problem solvers, like the Gödel machine,
*  but also Markus Hutter's fastest way of solving all possible problems, which he developed around
*  2002 in my lab, they are associated with these constant overheads for proof search, which guarantees
*  that the thing that you're doing is optimal. For example, there is this fastest way of solving
*  all problems with a computable solution, which is due to Markus Hutter, and
*  to explain what's going on there, let's take traveling salesman problems.
*  With traveling salesman problems, you have a number of cities, n cities, and you try to find
*  the shortest path through all these cities without visiting any city twice. And nobody knows the
*  fastest way of solving traveling salesman problems, TSPs, but let's assume there is a method of
*  solving them within n to the 5 operations, where n is the number of cities. Then the universal method
*  of Markus is going to solve the same traveling salesman problem also within n to the 5 steps.
*  Plus, all of one, plus a constant number of steps that you need for the proof searcher,
*  which you need to show that this particular class of problems, the traveling salesman problems,
*  can be solved within a certain time bound, within order n to the 5 steps, basically.
*  And this additive constant doesn't care for n, which means as n is getting larger and larger,
*  as you have more and more cities, the constant overhead pales in comparison. And that means that
*  almost all large problems are solved in the best possible way. Already today, we already have a
*  universal problem solver like that. However, it's not practical because the overhead,
*  the constant overhead is so large that for the small kinds of problems that you want to solve
*  in this little biosphere. By the way, when you say small, you're talking about things that fall
*  within the constraints of our computational systems. They can seem quite large to us mere humans.
*  That's right. Yeah. So they seem large and even unsolvable in a practical sense today,
*  but they are still small compared to almost all problems because almost all problems are
*  large problems, which are much larger than any constant. Do you find it useful as a person
*  who has dreamed of creating a general learning system, has worked on creating one, has done a
*  lot of interesting ideas there to think about P versus NP, this formalization of how hard problems
*  are, how they scale this kind of worst case analysis type of thinking. Do you find that useful
*  or is it only just a mathematical, it's a set of mathematical techniques to give you intuition
*  about what's good and bad? So P versus NP, that's super interesting from a theoretical point of view
*  and in fact, as you are thinking about that problem, you can also get inspiration for better
*  practical problem solvers. On the other hand, we have to admit that at the moment the best
*  practical problem solvers for all kinds of problems that we are now solving through what is called AI
*  at the moment, they are not of the kind that is inspired by these questions. There we are using
*  general purpose computers such as recurrent neural networks, but we have a search technique which is
*  just local search, gradient descent, to try to find a program that is running on these recurrent
*  networks such that it can solve some interesting problems such as speech recognition or machine
*  translation and something like that. And there is very little theory behind the best solutions
*  that we have at the moment that can do that. Do you think that needs to change? Do you think
*  that will change? Or can we go, can we create a general intelligence systems without ever really
*  proving that that system is intelligent in some kind of mathematical way? Solving machine
*  translation perfectly or something like that within some kind of syntactic definition of a language?
*  Or can we just be super impressed by the thing working extremely well and that's sufficient?
*  There's an old saying and I don't know who brought it up first, which says there's nothing more
*  practical than a good theory. And a good theory of problem solving
*  under limited resources like here in this universe or on this little planet
*  has to take into account these limited resources. And so probably there is locking
*  a theory which is related to what we already have, these asymptotically optimal problem solvers,
*  which tells us what we need in addition to that to come up with a practically optimal problem
*  solver. So I believe we will have something like that and maybe just a few little tiny twists
*  unnecessary to change what we already have to come up with that as well. As long as we don't have
*  that we admit that we are taking suboptimal ways and recurrent neural networks and long
*  short-term memory equipped with local search techniques. And we are happy that it works better
*  than any competing method, but that doesn't mean that we think we are done.
*  You've said that an AGI system will ultimately be a simple one. A general intelligence system
*  will ultimately be a simple one, maybe a pseudocode of a few lines to be able to describe it. Can you
*  talk through your intuition behind this idea, why you feel that
*  at its core intelligence is a simple algorithm?
*  Experience tells us that the stuff that works best is really simple. So the asymptotically
*  optimal ways of solving problems, if you look at them, they're just simple.
*  If you look at them, they're just a few lines of code. It's really true. Although they are
*  these amazing properties, just a few lines of code. Then the most promising and most useful
*  practical things maybe don't have this proof of optimality associated with them. However,
*  they are also just a few lines of code. The most successful recurrent neural networks,
*  you can write them down and five lines of pseudocode.
*  That's a beautiful, almost poetic idea. But what you're describing there is the lines of pseudocode
*  are sitting on top of layers and layers of abstractions in a sense. So you're saying at
*  the very top, it'll be a beautifully written algorithm. But do you think that there's many
*  layers of abstractions we have to first learn to construct?
*  Of course, we are building on all these great abstractions that people have invented over the
*  millennia, such as matrix multiplications and real numbers and basic arithmetics and calculus
*  and derivations of error functions and derivatives of error functions and stuff like that.
*  Without that language that greatly simplifies our way of thinking about these problems,
*  we couldn't do anything. In that sense, as always, we are standing on the shoulders of the giants who
*  in the past simplified the problem of problem solving so much that now we have a chance to
*  do the final step. The final step will be a simple one. If we take a step back through all of human
*  civilization and just the universe in general, how do you think about evolution? And what if
*  creating a universe is required to achieve this final step? What if going through the very painful
*  and inefficient process of evolution is needed to come up with this set of abstractions that
*  ultimately lead to intelligence? Do you think there's a shortcut or do you think we have to create
*  something like our universe in order to create something like human level intelligence?
*  Hmm. So far the only example we have is this one, this universe.
*  Do you think you can do better?
*  Maybe not, but we are part of this whole process. So it might be the case that the code that runs
*  the universe is really, really simple. Everything points to that possibility because gravity and
*  other basic forces are really simple laws that can be easily described also in just a few lines
*  of code basically. And then there are these other events, the apparently random events in the history
*  of the universe, which as far as we know at the moment don't have a compact code, but who knows,
*  maybe somebody in the near future is going to figure out the pseudo-random generator which
*  is computing whether the measurement of that spin up or down thing here is going to be positive
*  or negative. Underlying quantum mechanics. Yes. Do you ultimately think quantum mechanics is a
*  pseudo-random number generator? So it's all deterministic. There's no randomness in our
*  universe. Does God play dice? So a couple of years ago, a famous physicist, quantum physicist,
*  Anton Zeilinger, he wrote an essay in Nature and it started more or less like that.
*  But one of the fundamental insights of the 20th century was that
*  the universe is fundamentally random on the quantum level. And that whenever
*  you measure spin up or down or something like that, a new bit of information enters the history of
*  the universe. And while I was reading that, I was already typing the response and they had to
*  publish it because I was right. That there is no evidence, no physical evidence for that. So there's
*  an alternative explanation where everything that we consider random is actually pseudo-random, such
*  as the decimal expansion of pi, 3.141 and so on, which looks random but isn't. So pi is interesting
*  because every three-digit sequence, every sequence of three digits appears roughly one in a thousand
*  times and every five-digit sequence appears roughly one in ten thousand times. What do you
*  would expect if it was random? But there's a very short algorithm, a short program that computes all
*  of that. So it's extremely compressible. And who knows, maybe tomorrow some grad student at CERN
*  goes back over all these data points, better decay and whatever, and figures out, oh, it's
*  the second billion digits of pi or something like that. We don't have any fundamental reason at the
*  moment to believe that this is truly random and not just a deterministic video game. If it was a
*  deterministic video game it would be much more beautiful because beauty is simplicity. And many
*  of the basic laws of the universe, like gravity and the other basic forces, are very simple. So
*  very short programs can explain what these are doing. And it would be awful
*  and ugly. The universe would be ugly. The history of the universe would be ugly if, for the extra
*  things, the seemingly random data points that we get all the time, that we really need a huge
*  number of extra bits to describe all these extra bits of information.
*  So as long as we don't have evidence that there is no short program that computes the entire history
*  of the entire universe, we are, as scientists, compelled to look further for that shortest program.
*  Your intuition says there exists a program that can backtrack to the creation of the universe.
*  So compute the shortest path to the creation of the universe.
*  Yes, including all the entanglement things and all the spin up and down measurements
*  that have been taken place since 13.8 billion years ago.
*  We don't have a proof that it is random. We don't have a proof that it is compressible to a short
*  program. But as long as we don't have that proof, we are obliged, as scientists, to keep looking for
*  that simple explanation. Absolutely. So you said simplicity is beautiful or beauty is simple
*  either one works. But you also work on curiosity, discovery, you know, the romantic notion of
*  randomness, of serendipity, of being surprised by things that are about you. Kind of in our poetic
*  notion of reality, we think as humans require randomness. So you don't find randomness beautiful.
*  You find simple determinism beautiful. Yeah. Okay. So why? Why? Because the explanation
*  becomes shorter. A universe that is compressible to a short program is much more elegant and much
*  more beautiful than another one, which needs an almost infinite number of bits to be described.
*  As far as we know, many things that are happening in this universe are really simple in terms of
*  short programs that compute gravity and the interaction between elementary particles and so
*  on. So all of that seems to be very, very simple. Every electron seems to
*  reuse the same sub program all the time as it is interacting with other elementary particles.
*  If we now require an extra oracle injecting new bits of information all the time for these
*  extra things which are currently not understood, such as better decay,
*  then the whole description length of the data that we can observe of the history of the universe
*  would become much longer and therefore uglier. And uglier. Again, simplicity is elegant and
*  beautiful. The history of science is a history of compression progress.
*  Yeah. So you've described sort of as we build up abstractions and you've talked about the idea of
*  compression. How do you see this? The history of science, the history of humanity, our civilization,
*  and life on earth as some kind of path towards greater and greater compression? What do you mean
*  by that? How do you think about that? Indeed, the history of science is a history of compression
*  progress. What does that mean? Hundreds of years ago, there was an astronomer whose name was Kepler
*  and he looked at the data points that he got by watching planets move and then he had all these
*  data points and suddenly it turned out that he can greatly compress the data by predicting it
*  through an ellipse law. So it turns out that all these data points are more or less on ellipses
*  around the sun. And another guy came along whose name was Newton and before him Hooke. And they
*  said the same thing that is making these planets move like that is what makes the apples fall down.
*  And it also holds for stones and for all kinds of other objects. And suddenly many, many of these
*  observations became much more compressible because as long as you can predict the next thing,
*  given what you have seen so far, you can compress it. You don't have to store that data extra.
*  This is called predictive coding. And then there was still something wrong with that theory of the
*  universe and you had deviations from these predictions of the theory. And 300 years later,
*  another guy came along whose name was Einstein and he was able to explain away all these deviations
*  from the predictions of the old theory through a new theory which was called the general theory
*  of relativity, which at first glance looks a little bit more complicated and you have to warp
*  space and time, but you can't phrase it within one single sentence, which is no matter how fast you
*  accelerate and how fast or how hard you decelerate and no matter what is the gravity in your local
*  framework, light speed always looks the same. And from that you can calculate all the consequences.
*  So it's a very simple thing and it allows you to further compress all the observations because
*  suddenly there are hardly any deviations any longer that you can measure from the predictions
*  of this new theory. So art of science is a history of compression progress. You never arrive
*  immediately at the shortest explanation of the data, but you're making progress. Whenever you
*  are making progress, you have an insight. You see, oh, first I needed so many bits of information to
*  describe the data, to describe my falling apples, my video of falling apples. I need so many data,
*  so many pixels have to be stored. But then suddenly I realized, no, there is a very simple way of
*  predicting the third frame in the video from the first tool. And maybe not every little detail can
*  be predicted, but more or less most of these orange blobs that are coming down, they accelerate in the
*  same way, which means that I can greatly compress the video. And the amount of compression
*  progress that is the depth of the insight that you have at that moment. That's the fun that you
*  have, the scientific fun, the fun in that discovery. And we can build artificial systems that do the
*  same thing. They measure the depth of their insights as they are looking at the data, which
*  is coming in through their own experiments. And we give them a reward, an intrinsic reward
*  in proportion to this depth of insight. And since they are trying to maximize the rewards they get,
*  they are suddenly motivated to come up with new action sequences, with new experiments that have
*  the property that the data that is coming in as a consequence of these experiments has the property
*  that they can learn something about, see a pattern in there, which they hadn't seen yet before.
*  So there's an idea of power play you've described, a training a general problem solver in this kind
*  of way of looking for the unsolved problems. Yeah. Can you describe that idea a little further?
*  It's another very simple idea. So normally what you do in computer science, you have, you have
*  some guy who gives you a problem, and then there is a huge search space of potential solution candidates.
*  And you somehow try them out and you have more less sophisticated ways of
*  moving around in that search space until you finally found a solution which you consider
*  satisfactory. That's what most of computer science is about. Power play just goes one little step
*  further and says, let's not only search for solutions to a given problem, but let's search
*  to pairs of problems and their solutions where the system itself has the opportunity to
*  phrase its own problem. So we are looking suddenly at pairs of problems and their solutions or
*  modifications of the problem solver that is supposed to generate a solution to that new problem.
*  And this additional degree of freedom allows us to build
*  career systems that are like scientists in the sense that they not only try to solve
*  try to find answers to existing questions, no, they are also free to pose their own questions.
*  So if you want to build an artificial scientist, we have to give it that freedom and power play is
*  exactly doing that. So that's that's a dimension of freedom that's important to have. But how do you
*  think that how multi dimensional and difficult the space of then coming up with your own questions
*  is? Yeah, so as it's one of the things that as human beings, we consider to be the thing that
*  makes us special, the intelligence that makes us special is that brilliant insight. Yeah,
*  that can create something totally new. Yes. So now let's look at the extreme case. Let's look
*  at the set of all possible problems that you can formally describe, which is infinite,
*  which should be the next problem that a scientist or power play is going to solve. Well, it should be
*  the easiest problem that goes beyond what you already know.
*  So it should be the simplest problem that the current problem solver that you have, which can
*  already solve 100 problems that he cannot solve yet by just generalizing. So it has to be new.
*  So it has to require a modification of the problem solver such that the new problem solver can solve
*  this new thing, but the old problem solver cannot do it. And in addition to that, we have to make
*  sure that the problem solver doesn't forget any of the previous solutions. Right. And so by
*  definition, power play is now trying always to search in this pair of in the set of pairs of
*  problems and problems over modifications for a combination that minimize the time to achieve
*  these criteria. So it's always trying to find the problem, which is easiest to add to the repertoire.
*  So just like grad students and academics and researchers can spend their whole career in a
*  local minima stuck trying to come up with interesting questions, but ultimately doing very little.
*  Do you think it's easy in this approach of looking for the simplest unsolvable problem to get stuck
*  in a local minima is not never really discovering new, you know, really jumping outside of the 100
*  problems that you've already solved in a genuine creative way? No, because that's the nature of
*  power play that it's always trying to break its current generalization abilities by coming up
*  with a new problem, which is beyond the current horizon, just shifting the horizon of knowledge
*  a little bit out there, breaking the existing rules, such that the new thing becomes solvable,
*  but wasn't solvable by the old thing. So like adding a new axiom, like what Godel did when he
*  he came up with these new sentences, new theorems that didn't have a proof in the formal system,
*  which means you can add them to the repertoire, hoping that that they are not going to damage
*  the consistency of the whole thing. So in the paper with the amazing title, formal theory of
*  creativity, fun and intrinsic motivation, you talk about discovery as intrinsic reward.
*  So if you view humans as intelligent agents, what do you think is the purpose and meaning of life
*  for us humans? You've talked about this discovery. Do you see humans as an instance of power play?
*  Agents? Yeah, so humans are curious. And that means they behave like scientists,
*  not only the official scientists, but even the babies behave like scientists, and they play around
*  with their toys to figure out how the world works and how it is responding to their actions. And
*  that's how they learn about gravity and everything. And yeah, in 1990, we had the first systems like
*  that would just try to, to play around with the environment and come up with situations that
*  go beyond what they knew at that time, and then get a reward for creating these situations and
*  then becoming more general problem solvers and being able to understand more of the world.
*  So yeah, I think in principle that that curiosity strategy,
*  or more sophisticated versions of what I just described, they are what we have built in as well,
*  because evolution discovered that's a good way of exploring the unknown world. And a guy who
*  explores the unknown world has a higher chance of solving problems that he needs to survive in
*  this world. On the other hand, those guys who were too curious, they were weeded out as well. So you
*  have to find this trade off. Evolution found a certain trade off. Apparently in our society,
*  there is a certain percentage of extremely exploitive guys. And it doesn't matter if they
*  die because many of the others are more conservative. And so yeah, it would be surprising to me if
*  that principle of artificial curiosity
*  wouldn't be present in almost exactly the same form here.
*  In our brains. So you're a bit of a musician and an artist. So continuing on this topic of creativity,
*  what do you think is the role of creativity in intelligence? So you've kind of implied that
*  it's essential for intelligence if you think of intelligence as a problem solving system,
*  as ability to solve problems. But do you think it's essential, this idea of creativity?
*  We never have a program, a sub program that is called creativity or something. It's just a side
*  effect of what our problem solvers do. They are searching a space of problems or a space of
*  candidates, of solution candidates, until they hopefully find a solution to a given problem.
*  But then there are these two types of creativity. And both of them are now present in our machines.
*  The first one has been around for a long time, which is
*  human gives problem to machine, machine tries to find a solution to that. And this has been
*  happening for many decades. And for many decades, machines have found creative solutions to
*  interesting problems, where humans were not aware of these particularly creative solutions,
*  but then appreciated that the machine found that. The second is the pure creativity that I would
*  call what I just mentioned, I would call the applied creativity, like applied art, where
*  somebody tells you now make a nice picture of, of this Pope, and you will get money for that. Okay,
*  so he is the artist and he makes a convincing picture of the Pope and the Pope likes it and
*  gives him the money. And then there is the pure creative creativity, which is more like the power
*  play and the artificial curiosity thing, where you have the freedom to select your own problem,
*  like a scientist who defines his own question to study. And so that is the pure creativity,
*  if you will, as opposed to the applied creativity, which serves another.
*  And in that distinction, there's almost echoes of narrow AI versus general AI. So this kind of
*  constrained painting of a Pope seems like the approaches of what people are calling narrow AI.
*  And pure creativity seems to be, maybe I'm just biased as a human, but it seems to be
*  an essential element of human level intelligence. Is that what you're implying?
*  To a degree. If you zoom back a little bit, and you just look at a general problem solving machine,
*  which is trying to solve arbitrary problems, then this machine will figure out in the course
*  of solving problems, that it's good to be curious. So all of what I said just now,
*  about this pre-wired curiosity, and this will to invent new problems that the system doesn't know
*  how to solve yet, should be just a byproduct of the general search. However, apparently,
*  evolution has built it into us, because it turned out to be so successful, a pre-wiring,
*  a bias, a very successful exploratory bias that we are born with.
*  And you've also said that consciousness in the same kind of way may be a byproduct of
*  problem solving. Do you think, do you find this an interesting byproduct? Do you think it's a useful
*  byproduct? What are your thoughts on consciousness in general? Or is it simply a byproduct of greater
*  and greater capabilities of problem solving that's similar to creativity in that sense?
*  Yeah, we never have a procedure called consciousness in our machines. However,
*  we get as side effects of what these machines are doing, things that seem to be closely related
*  to what people call consciousness. So for example, already in 1990, we had simple systems, which were
*  basically recurrent networks and therefore universal computers, trying to map incoming data
*  into actions that lead to success. Maximizing reward in a given environment, always finding
*  the charging station in time whenever the battery is low and negative signals are coming from the
*  battery, always find the charging station in time without bumping against painful obstacles on the
*  way. So complicated things, but very easily motivated. And then we give these little guys
*  a separate recurrent network, which is just predicting what's happening if I do that and that.
*  What will happen as a consequence of these actions that I'm executing? And it's just trained on the
*  long and long history of interactions with the world. So it becomes a predictive model of the
*  world basically. And therefore also a compressor of the observations of the world, because whatever
*  you can predict, you don't have to store extra. So compression is a side effect of prediction.
*  And how does this recurrent network compress? Well, it's inventing little sub-programs,
*  little sub-networks that stand for everything that frequently appears in the environment,
*  like bottles and microphones and faces, maybe lots of faces in my environment. So I'm learning to
*  create something like a prototype face and a new face comes along and all I have to encode are the
*  deviations from the prototype. So it's compressing all the time the stuff that frequently appears.
*  There's one thing that appears all the time, that is present all the time, when the agent is
*  interacting with its environment, which is the agent itself. So just for data compression reasons,
*  it is extremely natural for this recurrent network to come up with little sub-networks
*  that stand for the properties of the agents, the hand, the other actuators and all the stuff that
*  you need to better encode the data which is influenced by the actions of the agent. So there,
*  just as a side effect of data compression during problem solving, you have internal self-models.
*  Now you can use this model of the world to plan your future and that's what you also have done
*  since 1990. So the recurrent network, which is the controller, which is trying to maximize reward,
*  can use this model of the network of the world, this model network of the world, this predictive
*  model of the world to plan ahead and say let's not do this action sequence, let's do this action
*  sequence instead because it leads to more predicted reward. And whenever it's waking up these little
*  sub-networks that stand for itself, then it's thinking about itself, then it's thinking about
*  itself and it's exploring mentally the consequences of its own actions and
*  now you tell me why it's still missing.
*  Missing the next, the gap to consciousness. There isn't, that's a really beautiful idea that
*  if life is a collection of data and life is a process of compressing that data to act
*  efficiently, in that data you yourself appear very often so it's useful to form compressions of
*  yourself. It's a really beautiful formulation of what consciousness is, is a necessary side effect.
*  It's actually quite compelling to me. You've described RNN's developed LSTM's long short-term
*  memory networks, their type of recurrent neural networks, they have gotten a lot of success
*  recently. So these are networks that model the temporal, the temporal, the temporal, the
*  temporal aspects in the data, temporal patterns in the data and you've called them the deepest
*  of the neural networks, right? So what do you think is the value of depth in the models that we use to learn?
*  Since you mentioned the long short-term memory and the LSTM, I have to mention the names of
*  the brilliant students who made that possible. First of all, my first student ever, Sepp Hochreiter,
*  who had fundamental insights already in his diploma thesis, then Felix Geers, who had
*  additional important contributions, Alex Gray, a guy from Scotland, who is mostly responsible for
*  this CTC algorithm, which is now often used to train the LSTM to do the speech recognition on all
*  the Google Android phones and whatever and CRE and so on. So these guys, without these guys,
*  I would be nothing. It's a lot of incredible work. What is now the depth? What is the importance of
*  depth? Well, most problems in the real world are deep in the sense that the current input
*  doesn't tell you all you need to know about the environment. So instead, you have to have a memory
*  of what happened in the past and often important parts of that memory are dated. They are pretty
*  old. So when you're doing speech recognition, for example, and somebody says 11, then that's about
*  half a second or something like that, which means it's already 50 time steps. And another guy or the
*  same guy says seven. So the ending is the same, seven. But now the system has to see the distinction
*  between seven and 11. And the only way it can see the difference is it has to store that 50 steps ago,
*  there was an 11 or seven. So there you have already a problem of depth 50. Because for each
*  time step, you have something like a virtual layer and the expanded and old version of this
*  recurrent network, which is doing the speech recognition. So these long time lags, they
*  translate into problem depth. And most problems in this world are such that you really have to
*  look far back in time to understand what is the problem and to solve it. But just like with LSTM,
*  you don't necessarily need to, when you look back in time, remember every aspect, you just need to
*  remember the important aspects. That's right. The network has to learn to put the important stuff in
*  into memory and to ignore the unimportant noise. So but in that sense, deeper and deeper is better,
*  or is there a limitation? Is there I mean, LSTM is one of the great examples of architectures
*  that do something beyond just deeper and deeper networks. There's clever mechanisms for
*  filtering data for remembering and forgetting. So do you think that that kind of thinking is
*  necessary? If you think about LSTM is a leap, a big leap forward over traditional vanilla RNNs,
*  what do you think is the next leap within this context? So LSTM was a very clever improvement,
*  but LSTM still don't have the same kind of ability to see far back in the future in the past
*  as us humans do the credit assignment problem across way back, not just 50 times steps or 100
*  or 1000, but millions and billions. It's not clear what are the practical limits of the LSTM when it
*  comes to looking back. Already in 2006, I think we had examples where not only looked back tens
*  or thousands of steps, but really millions of steps. And Juan Perez, artist in my lab,
*  I think was the first author of a paper where we really was in 2006 or something,
*  had examples where it learned to look back for more than 10 million steps. So
*  for most problems of speech recognition, it's not necessary to look that far back. But there are
*  examples where it does. Now, the looking back thing, that's rather easy because there is only
*  one past, but there are many possible futures. And so a reinforcement learning system, which is
*  trying to maximize its future expected reward and doesn't know yet which of these many possible
*  futures should I select given this one single past, is facing problems that the LSTM by itself
*  cannot solve. So the LSTM is good for coming up with a compact representation of the history
*  so far of the history and observations and actions so far. But now how do you plan in an efficient
*  and good way among all these? How do you select one of these many possible action sequences
*  that a reinforcement learning system has to consider to maximize reward in this unknown future?
*  So again, we have this basic setup where you have one Rikha network, which gets in the video and the
*  speech and whatever, and is executing actions and is trying to maximize reward. So there is no teacher
*  who tells it what to do at which point in time. And then there's the other network, which is
*  just predicting what's going to happen if I do that and that. And that could be an LSTM network,
*  and it learns to look back all the way to make better predictions of the next time step. So
*  essentially, although it's predicting only the next time step, it is motivated to learn to put
*  into memory something that happened maybe a million steps ago, because it's important to memorize
*  that if you want to predict that at the next time step, the next event. Now, how can a model of the
*  world like that, a predictive model of the world, be used by the first guy? Let's call it the
*  controller and the model, the controller and the model. How can the model be used by the controller
*  to efficiently select among these many possible futures? It's a naive way. We had about 30 years
*  ago was let's just use the model of the world as a stand-in, as a simulation of the world. And
*  millisecond by millisecond, we plan the future. And that means we have to roll it out really in
*  detail. And it will work only if the model is really good. And it will still be inefficient
*  because we have to look at all these possible futures. And there are so many of them. So instead,
*  what we do now, since 2015, in our CM systems, controller model systems, we give the controller
*  the opportunity to learn by itself how to use the potentially relevant parts of the model network to
*  solve new problems more quickly. And if it wants to, it can learn to ignore the M. And sometimes
*  ignore the M because it's really bad. It's a bad predictor in this particular situation of life
*  where the controller is currently trying to maximize reward. However, it can also learn to
*  address and exploit some of the subprograms that came about in the model network through compressing
*  the data by predicting it. So it now has an opportunity to reuse that code, the algorithmic
*  information in the model network to reduce its own search space, such that it can solve a new
*  problem more quickly than without the model. Compression. So you're ultimately optimistic
*  and excited about the power of reinforcement learning in the context of real systems.
*  Absolutely. Yeah. So you see RL as a potential having a huge impact beyond just sort of the M part
*  is often developed on supervised learning methods. You see RL as a for problems of
*  self-driving cars or any kind of applied side robotics. That's the correct interesting direction
*  for research in your view. I do think so. We have a company called Naysense, which has applied
*  reinforcement learning to little Audis, which learn to park without a teacher. The same principles
*  were used, of course. So these little Audis, they are small, maybe like that. So much smaller
*  than the real Audis, but they have all the sensors that you find in the real Audis. You find the
*  cameras, the LiDAR sensors. They go up to 120 kilometers an hour if they want to. And they have
*  pain sensors basically, and they don't want to bump against obstacles and other Audis. And so they
*  must learn like little babies to park. Take the raw vision input and translate that into actions
*  that lead to a successful parking behavior, which is a rewarding thing. And yes, they learn that.
*  They learn. So we have examples like that. And it's only in the beginning. This is just the tip of
*  the iceberg. And I believe the next wave of AI is going to be all about that. So at the moment,
*  the current wave of AI is about passive pattern observation and prediction. And that's what you
*  have on your smartphone and what the major companies on the Pacific Rim are using to sell you
*  ads to do marketing. That's the current source of profit in AI. And that's only one or two percent
*  of the world economy, which is big enough to make these companies pretty much the most valuable
*  companies in the world. But there's a much, much bigger fraction of the economy going to be affected
*  by the next wave, which is really about machines that shape the data through their own actions.
*  Do you think simulation is ultimately the biggest way that those methods will be successful in the
*  next 10, 20 years? We're not talking about 100 years from now. We're talking about sort of the
*  near term impact of RL. Do you think really good simulation is required? Or is there other
*  techniques like imitation learning, observing other humans operating in the real world?
*  Where do you think this success will come from? So at the moment, we have a tendency of using
*  physics simulations to learn behavior for machines that learn to solve problems that
*  humans also do not know how to solve. However, this is not the future, because the future is
*  in what little babies do. They don't use a physics engine to simulate the world. No, they learn a
*  predictive model of the world, which maybe sometimes is wrong in many ways, but captures
*  all kinds of important abstract high level predictions, which are really important to
*  be successful. And that's what was the future 30 years ago when you started that type of research,
*  but it's still the future. And now we know much better how to go there, to move forward, and to
*  really make work in systems based on that, where you have a learning model of the world,
*  a model of the world that learns to predict what's going to happen if I do that and that.
*  And then the controller uses that model to more quickly learn successful action sequences.
*  And then of course, always this curiosity thing. In the beginning, the model is stupid, so the
*  controller should be motivated to come up with experiments with action sequences that lead to
*  data that improve the model. Do you think improving the model, constructing an understanding of the
*  world in this connection is now the popular approaches have been successful or grounded
*  in ideas of neural networks. But in the 80s with expert systems, there's symbolic AI approaches,
*  which to us humans are more intuitive in the sense that it makes sense that you build up knowledge
*  and knowledge representation. What kind of lessons can we draw into our current approaches
*  from expert systems, from symbolic AI? So I became aware of all of that in the 80s.
*  And back then, logic programming was a huge thing. Was it inspiring to you yourself? Did you find it
*  compelling? Because a lot of your work was not so much in that realm, right? It was more in the
*  learning systems. Yes and no, but we did all of that. So my first publication ever actually was
*  1987, was the implementation of genetic algorithm of a genetic programming system in Prolog.
*  So Prolog, that's what you learned back then, which is a logic programming language.
*  And the Japanese, they have this huge fifth generation AI project, which was mostly about
*  logic programming back then, although neural networks existed and were well known back then.
*  And deep learning has existed since 1965, since this guy in the Ukraine, Ivanknenko, started it.
*  But the Japanese and many other people, they focused really on this logic programming.
*  And I was influenced to the extent that I said, okay, let's take these biologically inspired
*  algorithms like evolution programs and implement that in the language which I know, which was
*  Prolog, for example, back then. And then in many ways, this came back later because the
*  Google machine, for example, has a proof searcher on board. And without that, it would not be optimal.
*  While Marcus Hutte's universal algorithm for solving all well-defined problems has a proof
*  searcher on board. So that's very much logic programming. Without that, it would not be
*  asymptotically optimal. But then on the other hand, because we have very pragmatic guys also,
*  we focused on recurrent neural networks and suboptimal stuff such as gradient-based search
*  and program space rather than provably optimal things.
*  So logic programming certainly has a usefulness when you're trying to construct something
*  provably optimal or provably good or something like that. But is it useful for practical problems?
*  It's really useful for our theory improving. The best theory improvers today are not neural networks.
*  No, they are logic programming systems and they are much better theory improvers than most
*  math students in the first or second semester.
*  But for reasoning for playing games of Go or chess or for robots, autonomous vehicles that
*  operate in the real world or object manipulation, you think learning...
*  As long as the problems have little to do with theory improving themselves, then as long as that
*  is not the case, you would just want to have better pattern recognition. So to build a self-driving
*  car, you want to have better pattern recognition and pedestrian recognition and all these things.
*  And you want to minimize the number of false positives, which is currently slowing down
*  self-driving cars in many ways. And all of that has very little to do with logic programming.
*  What are you most excited about in terms of directions of artificial intelligence at this
*  moment in the next few years in your own research and in the broader community?
*  So I think in the not so distant future, we will have for the first time
*  little robots that learn like kids. And I will be able to say to the robot,
*  look here robot, we are going to assemble a smartphone. Let's take this slab of plastic
*  and the screwdriver and let's screw in the screw like that. No, not like that. Like that.
*  Not like that. Like that. Not like that. Like that. And I don't have a data glove or something. He
*  will see me and he will hear me and he will try to do something with his own actuators, which will
*  be really different from mine, but he will understand the difference and will learn to
*  imitate me, but not in the supervised way where a teacher is giving target signals for all his
*  muscles all the time. No, by doing this high level imitation where he first has to learn to imitate
*  me and then to interpret these additional noises coming from my mouth as helping, helpful signals
*  to do that. And then it will by itself come up with faster ways and more efficient ways of doing
*  the same thing. And finally, I stop his learning algorithm and make a million copies and sell it.
*  And so at the moment, this is not possible, but we already see how we are going to get there.
*  And you can imagine to the extent that this works economically and cheaply, it's going to change
*  everything. Almost all of production is going to be affected by that. And a much bigger wave,
*  a much bigger AI wave is coming than the one that we are currently witnessing, which is mostly about
*  passive pattern recognition on your smartphone. This is about active machines that shape the data
*  through the actions they are executing. And they learn to do that in a good way.
*  So many of the traditional industries are going to be affected by that. All the companies that
*  are building machines will equip these machines with cameras and other sensors, and they are going
*  to learn to solve all kinds of problems through interaction with humans, but also a lot on their
*  own to improve what they already can do. And lots of old economy is going to be affected by that.
*  And in recent years, I have seen that old economy is actually waking up and realizing that there's
*  the case. And- Are you optimistic about that future? Are you concerned? There's a lot of
*  people concerned in the near term about the transformation of the nature of work. The kind
*  of ideas that you just suggested would have a significant impact of what kind of things could
*  be automated. Are you optimistic about that future? Are you nervous about that future?
*  And looking a little bit farther into the future, there's people like Gail Almask,
*  Stuart Russell concerned about the existential threats of that future. So in the near term, job
*  loss in the long term existential threat, are these concerns to you or are you ultimately optimistic?
*  So let's first address the near future. We have had predictions of job losses for many decades.
*  For example, when industrial robots came along, many people predicted that lots of jobs are going
*  to get lost. And in a sense, they were right. Because back then there were car factories and
*  hundreds of people in these factories assembled cars. And today the same car factories have
*  hundreds of robots and maybe three guys watching the robots.
*  On the other hand, those countries that have lots of robots per capita, Japan, Korea, Germany,
*  Switzerland, a couple of other countries, they have really low unemployment rates.
*  Somehow all kinds of new jobs were created. Back then, nobody anticipated those jobs.
*  And decades ago, I already said it's really easy to say which jobs are going to
*  get lost, but it's really hard to predict the new ones.
*  30 years ago, who would have predicted all these people making money as YouTube bloggers, for example?
*  200 years ago, 60% of all people used to work in agriculture. Today, maybe 1%. But still,
*  only, I don't know, 5% unemployment. Lots of new jobs were created and Homo Ludens, the playing man,
*  is inventing new jobs all the time. Most of these jobs are not existentially necessary
*  for the survival of our species. There are only very few existentially necessary jobs,
*  such as farming and building houses and warming up the houses. But less than 10% of the population
*  is doing that. And most of these newly invented jobs are about interacting with other people in
*  new ways, through new media and so on, getting new types of kudos in forms of likes and whatever,
*  and even making money through that. So Homo Ludens, the playing man, doesn't want to be
*  unemployed, and that's why he's inventing new jobs all the time. And he keeps considering these jobs
*  as really important and is investing a lot of energy and hours of work into those new jobs.
*  That's quite beautifully put. We're really nervous about the future because we can't predict what
*  kind of new jobs will be created. But you're ultimately optimistic that we humans are so
*  restless that we create and give meaning to newer and newer jobs, totally new
*  things that get likes on Facebook or whatever the social platform is. So what about long-term
*  existential threat of AI, where our whole civilization may be swallowed up by this
*  ultra-superintelligent systems? Maybe it's not going to be swallowed up, but
*  I'd be surprised if we humans were the last step in the evolution of the universe.
*  You've actually had this beautiful comment somewhere that I've seen saying that artificial
*  intelligence systems, just like us humans, will likely not want to interact with humans. They'll
*  just interact amongst themselves, just like ants interact amongst themselves and only
*  tangentially interact with humans. It's quite an interesting idea that once we create AGI,
*  they will lose interest in humans and compete for their own Facebook likes and their own
*  social platforms. So within that quite elegant idea, how do we know in a hypothetical sense
*  that there's not already intelligence systems out there? How do you think broadly of
*  general intelligence greater than us? How would we know it's out there? How would we know it's
*  around us? And could it already be? I'd be surprised if within the next few decades or something like
*  that, we won't have AIs that are truly smart in every single way and better problem solvers and
*  almost every single important way. And I'd be surprised if they wouldn't realize what we have
*  realized a long time ago, which is that almost all physical resources are not here in this biosphere,
*  but for that, the rest of the solar system gets two billion times more solar energy than
*  our little planet. There's lots of material out there that you can use to build robots and
*  self-replicating robot factories and all this stuff. And they are going to do that. And they
*  will be scientists and curious and they will explore what they can do. And in the beginning,
*  they will be fascinated by life and by their own origins in our civilization. They will want to
*  understand that completely, just like people today would like to understand how life works and
*  and also the history of our own existence and civilization, but then also in the physical laws
*  that created all of that. So in the beginning, they will be fascinated by life once they understand
*  it. They lose interest, like anybody who loses interest in things he understands.
*  And then, as you said, the most interesting sources of
*  information for them will be others of their own kind.
*  So at least in the long run, there seems to be some sort of protection
*  through lack of interest on the other side. And now it seems also clear, as far as we understand
*  physics, you need matter and energy to compute and to build more robots and infrastructure and
*  more AI civilization and AI ecologies consisting of trillions of different types of AIs.
*  And so it seems inconceivable to me that this thing is not going to expand. Some AI ecology,
*  not controlled by one AI, but by trillions of different types of AIs competing in all kinds of
*  ecological niches in ways that we cannot fathom at the moment. But it's going to expand, limited by
*  light speed and physics, but it's going to expand. And now we realize that the universe is still young.
*  It's only 13.8 billion years old. And it's going to be a thousand times older than that.
*  And so we need to be able to understand that. And so we need to be able to understand that.
*  And it's going to be a thousand times older than that.
*  So there's plenty of time to conquer the entire universe and to fill it with intelligence. And
*  senders and receivers such that AIs can travel the way they are traveling in our labs today,
*  which is by radio from sender to receiver. And let's call the current age of the universe one
*  eon. One eon. Now it will take just a few eons from now and the entire visible universe is going
*  to be full of that stuff. And let's look ahead to a time when the universe is going to be 1,000 times
*  older than it is now. They will look back and they will say, look, almost immediately after the big
*  bang, only a few eons later, the entire universe started to become intelligent. Now to your question,
*  how do we see whether anything like that has already happened or is already in a more advanced
*  stage in some other part of the universe, of the visible universe? We are trying to look out there
*  and nothing like that has happened so far. Or is that true? Do you think we would recognize it?
*  How do we know it's not among us? How do we know planets aren't in themselves intelligent beings?
*  How do we know ants seen as a collective are not much greater intelligence than our own? These kinds
*  of ideas. When I was a boy, I was thinking about these things. And I thought, maybe it has already
*  happened. Because back then, I knew, I learned from popular physics books, that the large-scale
*  structure of the universe is not homogeneous. And you have these clusters of galaxies, and then in
*  between there are these huge empty spaces. And I thought, maybe they aren't really empty. It's just
*  that in the middle of that, some AI civilization already has expanded and then has covered a bubble
*  of a billion light-years diameter and is using all the energy of all the stars within that bubble for
*  its own unfathomable purposes. And so it already has happened and we just failed to interpret the
*  signs. But then I learned that gravity by itself explains the large-scale structure of the universe
*  and that this is not a convincing explanation. And then I thought, maybe it's the dark matter.
*  Because as far as we know today, 80% of the measurable matter is invisible. And we know
*  that because otherwise our galaxy or other galaxies would fall apart. They are rotating too quickly.
*  And then the idea was, maybe all of these AI civilizations that are already out there, they
*  are just invisible because they are really efficient in using the energies of their own
*  local systems. And that's why they appear dark to us. But this is also not a convincing explanation
*  because then the question becomes, why are there still any visible stars left in our own galaxy,
*  which also must have a lot of dark matter? So that is also not a convincing thing. And today,
*  I like to think it's quite plausible that maybe the first, at least in our local light cone, within
*  the few hundreds of millions of light years that we can reliably
*  observe. Is that exciting to you? Who might be the first? And it would make us much more important
*  because if we mess it up through a nuclear war, then maybe this will have an effect on the
*  development of the entire universe. So let's not mess it up. Let's not mess it up.
*  Jürgen, thank you so much for talking today. I really appreciate it. It's my pleasure.

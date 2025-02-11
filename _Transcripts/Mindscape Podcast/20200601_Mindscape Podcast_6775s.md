---
Date Generated: June 09, 2024
Transcription Model: whisper medium 20231117
Length: 6775s
Video Keywords: ['complexity', 'computation', 'quantum computers', 'quantum gravity']
Video Views: 34242
Video Rating: None
Video Description: Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2020/06/01/99-scott-aaronson-on-complexity-computation-and-quantum-gravity/

Patreon: https://www.patreon.com/seanmcarroll

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x

There are some problems for which it’s very hard to find the answer, but very easy to check the answer if someone gives it to you. At least, we think there are such problems; whether or not they really exist is the famous P vs NP problem, and actually proving it will win you a million dollars. This kind of question falls under the rubric of “computational complexity theory,” which formalizes how hard it is to computationally attack a well-posed problem. Scott Aaronson is one of the world’s leading thinkers in computational complexity, especially the wrinkles that enter once we consider quantum computers as well as classical ones. We talk about how we quantify complexity, and how that relates to ideas as disparate as creativity, knowledge vs. proof, and what all this has to do with black holes and quantum gravity.

Scott Aaronson received his Ph.D. in computer science from the University of California, Berkeley. He is currently the David J. Bruton Jr. Centennial Professor of Computer Science at the University of Texas at Austin, and director of the Quantum Information Center there. He specializes in quantum computing and computational complexity theory, but has written on topics from free will to the nature of consciousness. Among his awards are the Tomassoni-Chisesi Prize in Physics (Italy) and the Alan T. Waterman Award from the National Science Foundation. His blog Shtetl-Optimized is known both for its humor and as the most reliable source of information on news in quantum computing. He is the author of Quantum Computing Since Democritus.

#podcast #ideas #science #philosophy #culture
---

# Mindscape 99 | Scott Aaronson on Complexity, Computers, and Quantum Gravity
**Mindscape Podcast:** [June 01, 2020](https://www.youtube.com/watch?v=qD4XkFndaFk)
*  Hello everyone, welcome to the Mindscape Podcast. I'm your host Sean Carroll. Here's a question
*  of interest. How hard is it to solve a problem? That seems like a very important question,
*  right? Especially when we're faced with all sorts of very difficult problems socially,
*  biologically, planetarily, and so forth. But it's also a very hard question to answer
*  in itself, right? Like, what do you mean how hard it is? What kind of problems are you
*  talking about? Happily, computer scientists have a very specific field of problems, a specific kind
*  of problems, and they care a lot about how hard they are to solve. There's a whole field of endeavor
*  called theoretical computer science. You can be a world-leading theoretical computer scientist and
*  never actually program a computer, although today's guest is not in that category. One of the things
*  that theoretical computer scientists worry about is if you have a certain kind of problem, like
*  sorting a list into alphabetical order, how many steps does your computer program have to take to
*  solve that problem? And how do the number of steps depend on the size of the list? This is the problem
*  known as computational complexity, and today's guest, Scott Aronson, is one of the world's
*  experts in this field. In fact, I feel bad even about saying this. Scott is a computer scientist
*  at the University of Texas at Austin who is not only one of the world's experts in theoretical
*  computer science and computational complexity, but seems to be the world's expert in many different
*  fields. So today we're going to dive into things like P versus NP, right? This is a famous problem
*  about whether or not a problem that is easy to check the solution for is also easy to solve. Almost
*  no one thinks it's true, yet it turns out to be really, really hard to show it. We're going to go
*  into quantum complexity theory, which then gets you into the question of if you built a quantum
*  computer, would it be able to speed up hard problems that we know about, like factoring large
*  numbers? As Scott will tell us, many of the claims you may have heard about the potential for quantum
*  computers speeding things up tend to be a little bit exaggerated. There really are speed ups
*  available, but maybe not as many as you've heard about. And on the other hand, we've had a real
*  difficulty in proving any of these results. There's a long list of things that we believe are true and
*  haven't yet proven. It's a very fruitful area to go in for a young person who really wants to make
*  a mark on a new and emerging field. But also, once you get into quantum mechanics, you're going to
*  become interested in things like quantum gravity, right? I mean, who could possibly avoid that? So
*  with Scott, I talk about black holes and the holographic principle and complementarity and
*  how we've somehow gotten quantum information into the game of trying to understand the fundamental
*  makeup of the universe. Scott is a long term friend of mine, a collaborator on fun papers,
*  and everyone's favorite go-to guy when you talk about these issues. And if you listen to this
*  podcast, you will find out why. If you don't know, let me remind you that here during our lockdown,
*  as long as it's still going on, I'm doing a set of weekly videos called the biggest ideas in the
*  universe. Right now we're about 10 videos in and we're in the middle of a pretty intense couple
*  of weeks trying to understand quantum field theory, Feynman diagrams, stuff like that. There's no
*  mathematical background, presumed, but you have to be willing to go along with me on some pretty
*  heady ideas. So check those out. They're on YouTube. Just go to YouTube and search for my name or
*  biggest ideas in the universe. We're going to be getting to some even bigger ideas. The idea is
*  just getting bigger and bigger. That's what we're going to do. So we haven't done gravity or quantum
*  gravity yet, but believe me, we will get there before too long. I hope you're enjoying them.
*  Hope that everyone is staying healthy and sane and safe during this weird situation we're in.
*  Scott Aaronson, welcome to the Lionsgate Podcast. Thanks. It's great to be here.
*  You know, I recently became an external professor at the Santa Fe Institute for their focus is
*  complexity studies. And I remember like back in the 90s, this used to be a huge thing defining
*  what a complex system actually was. And it took me a while to catch on that people like you have a
*  way of using the word complexity that doesn't have anything to do with any of the complex systems
*  that they're talking about. So what do you mean when you talk about complexity?
*  Yes, it's an overloaded term, right? The definition of complexity is complex. It's one of these
*  self-describing words, like, you know, short's a short word. Okay. But in theoretical computer
*  science, what people mean by complexity, let's say by computational complexity, is the resources
*  that are needed to solve some problem. And specifically, what we care about is the scaling
*  of the resources. So the most common resources that you might worry about are how much time does
*  your program take? And how much memory does it use? Right? Time and space, right? Those are pretty
*  fundamental. You could worry about other things also, like how much random how many random bits
*  do you need? How many parallel processors do you need? Do you need a quantum computer? You know,
*  what kind of what's the physical substrate of your computer? How many qubits? How many classical
*  bits? But, you know, we're not so interested in just giving answers like, oh, you know, I can,
*  I can solve problems of size 1000 using 30k of RAM, let's say, and solve problems of size 2000
*  using 50k. You know, because that's kind of like, okay, great. But, you know, tomorrow, someone
*  might have a slightly better idea, and it'll just cut that number by a factor of 10. Right? Or, you
*  know, I mean, I mean, these numbers are, you know, they're not fundamental features of the universe,
*  right? Or math there, you know, they depend enormously on details of what machine you're using,
*  right? Of course, a faster computer will be able to do the same thing, but faster. And, you know,
*  so forth. What we really care about is, you know, how is the how are the resources like time or
*  memory growing as you go to larger and larger problem sizes? Okay, so, for example, if I ask you
*  to tell me, you know, whether a number is prime or composite, right, then we could say the input
*  size is just the length of the number, right? How many digits it takes to write it down. And
*  what we really like is to have an algorithm to solve that kind of problem that would use resources,
*  time and memory that grow only like the size of the problem raised to some fixed power. Okay,
*  so like the number of digits cubed, something that's actually state of the art algorithms for
*  primality testing, that's about how much time they do use. Okay, what we don't want is an algorithm
*  that uses resources that grow exponentially with the size of the problem, right? And the reason,
*  I mean, I mean, I have this whole mini lecture about, you know, explaining exponential growth,
*  but I feel like in the age of coronavirus, that might not even be necessary. You know, now, you
*  know, maybe, you know, if there's one good thing to come out of this, maybe people now understand
*  it. Yeah, exactly. That an exponential will, you know, by the time you're at problems of size a
*  thousand or thousand digit numbers, then you'd already be talking like, you know, longer than the
*  age of the universe to solve it, you know, even if you got had every atom in the observable universe,
*  you know, working on your problem in parallel. So if something is exponentially hard, then we say
*  it's really, really hard. And if it's only exactly polynomial, then we say it's easy. Yeah, so in
*  practice, this tends to be the dividing line that we focus on, you know, is your problem solvable
*  by some algorithm that has only polynomial scaling, or does every possible algorithm require
*  exponential scaling? Right now, there are intermediate possibilities, you know, there are functions
*  that grow faster than polynomial and slower than exponential. There are, you know, and of course,
*  even among, you know, polynomials, if it grew like the problem size to the 1000 power, well, that's
*  technically polynomial, but that's not very good. Right. But, you know, but it but it but in practice,
*  you know, usually, if you can solve your problem by some method with exponentials, sorry, by some
*  algorithm with polynomial scaling, then usually, you know, if you put enough effort into it, you
*  know, if you care enough that like, problem size to the 100 can become problem size to the 10 can
*  become problem size to the three or to the four. Whereas if every algorithm you can find has
*  exponential scaling, then you're just kind of host. That's kind of saying that like, you don't know
*  anything better than some brute force approach that involves just trying every possible answer
*  from some astronomically large space of possibilities. And you've got a polynomial algorithm. Yeah. So
*  it seems to me that a lot of the bread and butter of a working complexity theorist in your sense in
*  the theoretical computer science sense is the best existing algorithm takes n bits and solves the
*  problem in n to the 2.4 power steps, but I can find an algorithm that does it in n to the 2.3 power
*  steps. So now I am the winner. Yeah, that is certainly a game that people play, right? Or even
*  to improve n to the 2.4 divided by log of n or something like that, right? That is, you know,
*  that's a little bit looked down upon just shaving logs off. But so, yeah, so basically we want to
*  know, you know, for various important problems, you know, by important problems, like, let's say,
*  multiplying numbers, right? Yeah. Multiplying matrices, you know, telling whether a number is
*  prime, deciding the truth or falsehood of a sentence in mathematical logic or, you know,
*  a scheduling, right? Scheduling airline flights, you know, not that anyone's doing that right now,
*  right? But, you know, figuring out how a protein will fall that might, you know, fight the coronavirus
*  or something where the size of the input would be the number of bases, the number of amino acids
*  in the protein. Okay, so these are all, you know, the sorts of problems that, you know, people might
*  care about and you want to know sort of what is the inherent difficulty of each one. So in a way that,
*  you know, does not depend on the details of are you using a Mac or a PC, but that really just
*  ultimately depends on what are the laws of physics that underlie your computer. And, you know, so on
*  the one hand, that means finding the fastest algorithm that you can, but on the other hand,
*  that also means trying to rule out that, you know, you can do any better than some limit, right? So
*  trying to prove that some algorithm is the best one. Now that is a lot harder. You know,
*  it's a lot harder to prove a negative than to, you know, prove that nothing can solve some problem
*  than to just find a way to solve it. But often what we can do is we can at least pass the blame
*  to someone else. Okay, in the following sense that, you know, so let's say that, you know,
*  the best algorithm is end to the 2.4 and let's say that you work on it and work on it for,
*  you know, months and months and you just cannot get it down to end to the 2.3, right? Okay,
*  so you could just give up, you know, admit that you're just not very good. Okay, but sometimes
*  what you can do is you can say, well, I can prove a theorem that says if you could improve that to
*  end to the 2.3, then here are 1000 other problems where you could also improve over the best that
*  anyone knows. Okay, so, you know, it's kind of it's not my fault that I'm stuck at end to the 2.4,
*  right? And I can prove that, right? It's a it's the you know, there's a more fundamental difficulty.
*  So in other words, we have this sort of set of problems that are computer friendly, right? We
*  can state them precisely. It's not like autonomous driving where we're not quite sure what we're
*  doing. There's a set of input bits and what we're discovering, what you're discovering is
*  that there is structure in the space of how hard these problems are. Yes. And you're trying to
*  figure out which problems sort of fit into different classes. So you become sort of,
*  oh, what's the word? Not botanist, but you know, someone who divides things into species and
*  things like that. taxonomous. Yes, that's what you are. Yeah. Yeah. Yeah. I mean, you know,
*  yeah. And I would say that like any other kind of taxonomy, right? Well, you know, what you what
*  you're really after are sort of like the general laws, the general principles, right? I mean,
*  like no one goes into particle physics, probably because they just want to classify, you know,
*  every type of meson, you know, or every every type of baryon, right? You know, but that what
*  you hope is that by classifying things, you know, you will notice patterns and then you'll notice
*  a deeper structure there. If you're interested in the kind of intellectual topics we talk about
*  here at mindscape, you might want to contemplate digging deeper by checking out the great courses
*  plus this is a streaming service that brings you introductory college level courses taught by some
*  of the best teachers out there direct to whatever device is most convenient for you. The topics
*  covered are a great variety. You can learn about history, you can learn about music, even food and
*  drink. But of course, there's also a lot of science and math courses being taught. For example,
*  if you're enjoying what we're talking about on today's podcast, you might want to check out a
*  course by Benjamin Schumacher called the science of information from language to black holes.
*  The course covers information in a variety of contexts from communication to computers to DNA
*  and genetics from Turing machines and computational complexity all the way up to quantum computers.
*  And the great thing is they're offering my listeners a free trial of unlimited access to
*  the entire library. If you sign up for the great courses plus today, you can get that by going to
*  the great courses plus.com slash mindscape. That's th great courses pl us.com slash mindscape.
*  You get a free trial where you can try out the entire library. Check it out today.
*  Yeah, I mean, I don't want to zoom over this too quickly, because it's something that to me is on
*  the one hand, both perfectly obvious in retrospect, but also really kind of profound the idea that
*  the kinds of questions we ask come along with a different set of difficulties when it comes to
*  trying to solve them. Yeah, yeah, absolutely. Look, the theory of computation, as we understand it
*  today, you could say it really started with Alan Turing in the 1930s, right? Writing down a
*  mathematical definition of what we mean by a computer, right? He had this concept of a Turing
*  machine. But if you don't know what a Turing machine is, that's fine, because your iPhone,
*  or your Android, or your desktop PC, these are all equivalent to Turing machines.
*  In the sense that they're just sort of sufficiently powerful computers to do the
*  kinds of questions. Exactly. In the specific sense that they can all emulate one another.
*  Merely some are faster, some are slower, some will run out of memory a little sooner than others will.
*  In principle, in the limit where you give them enough time and enough memory, they can all compute
*  the same set of functions. Then mathematicians, logicians spent decades just understanding the
*  boundary between what is computable and what is not computable. One of Turing's great discoveries,
*  of course, along with the invention of the Turing machine, was the discovery that not everything is
*  computable. There are problems where you can just prove that there is no algorithm to solve them.
*  Infinite complexity limit. There's no number of steps that is guaranteed to give you an answer.
*  Precisely. What's a question that falls into that category?
*  The most famous example is, I give you a computer program. Now the question is just,
*  does this program ever stop running? The famous halting problem. That may sound like a kind of
*  boring question for debugging some code, but that question actually encodes a large fraction of all
*  of mathematics. We could write a program that just will enumerate over all the zeros of the
*  Riemann zeta function and will halt only if there is one that is not on the critical line.
*  That is a program where to determine whether that program halts or runs forever is equivalent to
*  solving the Riemann hypothesis. You could do the same for many, many of the great unsolved problems
*  of math. That's a really profound question. Maybe it shouldn't shock us too much that there is no
*  general algorithm to solve it. Math does depend on creativity. Who would have thought?
*  Which doesn't mean, by the way, that human mathematicians could never be beaten by machines.
*  It just means that if they are, then the machines won't be perfect either.
*  I mean, this is a big, big difficult set of ideas.
*  It is.
*  When we talk about the halting problem, I guess I have many questions here.
*  I mean, you use the word creativity. What does that mean?
*  Well, okay. It is much easier to say what creativity is not. If something can be done
*  by a completely mechanical algorithm that we completely understand, then maybe we would say
*  that there is no creativity there. A multiplying of two integers, for example. You might choose to
*  do it in a creative way, but it doesn't require creativity.
*  But now we're skating into Penrose-ian waters, right? Where he's going to say that there's
*  something... Excuse me?
*  We're skating into Penrose-ian waters, where Roger Penrose is going to say there's something
*  about the human brain that can't be a computer because we are creative and they're not.
*  Yeah. Well, so I don't agree with him. To get to where Penrose goes, you have to take this
*  further step. Furthermore, I am in some sense a perfect mathematician. I can just see that
*  formal systems are consistent. When I make a statement like that or maybe when I make it
*  ex-cathedra or something, like wearing my official hat, then I am never mistaken.
*  Wait, sorry. I think we need to slow down and unpack that a little bit.
*  Why don't you tell us in your words what Penrose is trying to say?
*  Yeah. So he famously gave an argument, which was really an updating of an earlier argument due to
*  Lucas, that said that human creativity can never be even simulated by a machine.
*  And the argument... Well, we could actually make the argument in terms of the halting problem,
*  as he sometimes does. And there are certain algorithmic problems that we know just kind
*  of cannot be solved by computer using any amount of resources. But then he would say,
*  but in these cases, humans can just see the truth or falsehood of the relevant statement,
*  maybe even by introducing new axioms if needed. It's that second part that I have problems with.
*  Well, I'm totally on your side here, but I get why he would say that because I have in my mind
*  a vision of staring at a computer screen with a simple algorithm, with a loop in it, and going,
*  oh yeah, that's not going to terminate or oh yeah, that is. And so why can't I put... I mean,
*  somehow if you prove that I can't do that by a computer, then it sounds like you're proving
*  that humans are better. Right. Well, I think the main issue is that when we talk about algorithms
*  in theoretical computer science, we're typically talking about algorithms that always have to be
*  correct. I mean, you can relax that, but even then you'll have some specific condition, like
*  correct at least 99% of the time on inputs that are chosen from this distribution or something
*  like that. You have a formal criterion of whether your algorithm succeeds or fails.
*  And humans are not like that. When we try to do science, try to do math, there's no a priori
*  guarantee that we have to succeed. Andrew Wiles, when he started working on Fermat's Last Theorem,
*  he had no guarantee of success. I mean, we can look back and we can count the...
*  By confirmation bias, we can count the successes only, but there are lots of other big math
*  problems that no one has solved and for which we don't even know whether they are solvable.
*  And so as soon as you grant a machine the same liberty that it can try to learn from experience,
*  it can make mistakes sometimes, it can sometimes just give up and say, I don't know,
*  then there is no longer anything that math or logic can say against the machine
*  doing just as well as a human does or better than the human does. And if you want to say that the
*  computer is somehow not as good, I think you're forced at some point to retreat to internal
*  criteria. Like you could say, well, the computer is just saying that it understands why
*  set theory is consistent, but I just really, really feel its consistency.
*  But at that point, I think you might as well... Why even talk about something as
*  abstruse as set theory? You might as well just say, but when I taste the strawberry,
*  I really taste the strawberry. Oh, there are people who say that.
*  The full quality of strawberry-ness, and the machine could only be programmed to pretend that.
*  And then it just reduces to the usual debate that everyone always goes in circles with and
*  doesn't get anywhere. But this is very good because I think the point is that when we are
*  able to prove these theorems about what computers can't do, it's because we're sort of restricting
*  our notion of computer to something very, very specific that it would be easy to jump out of.
*  If you give computers some randomness, some fallibility, some give-up ability, then there's
*  no reason to think they can't be just as good as us and vice versa.
*  Well, it's not so much that we're restricting the computer as we're restricting what counts as
*  success. We're saying that you really have to guarantee me that you will get the right answer,
*  you will halt and return the right answer on all the inputs of this type, for example.
*  Got it. Yeah. And as soon as you're allowed to be
*  heuristic, well, then many more possibilities open up. But this is a whole fascinating discussion
*  that you can have just about computability. Where I wanted to go was that when people started
*  building actual computers in the 50s and 60s, they realized that most of what they really wanted to
*  do was computable in Turing sense. But computable could mean computable, but taking an amount of
*  time that grows like two to the two to the two to the two to the N, where N is the size of the
*  input. Right. And then if N is greater than one, you're completely hosed. So I think it was the
*  actual digital computer revolution that made people realize that often the much more important
*  question than just is something computable at all is, is it efficiently computable?
*  Is it computable in a way that avoids a brute force checking of astronomically many possibilities?
*  And so this is where we get into polynomial versus exponential.
*  Exactly. Exactly. Yeah. And I think that is sort of maybe the main insight that Turing and von
*  Neumann were kind of missing. I mean, well, maybe they sort of understood it, but I guess they had
*  a lot of other stuff on their plate. It was an exciting time back then. They were not under
*  lockdown, so they could really think about these things. Okay. So give us more of a lay of the land
*  explanation for what these computability classes are. There are things that take exponentially
*  long, things that take polynomial long. What else do we got? Yes. Okay. So you could say the most
*  basic thing you could do is just try to classify problems by how much time they take, how much
*  memory they take. So what can be done with a polynomial amount of time? This is a class that
*  we call P or polynomial. Physicists have much better names for things, right? But also Big Bang,
*  Black Hall. To the audience, they should not get sanguine because that's the only label that's
*  going to even make sense in what's to come. At least P makes sense. Well, I mean, look,
*  then there's everything you can do with a polynomial amount of space or memory. That's
*  called P-space. That's pretty intuitive, isn't it? Okay. And that's a potentially larger class
*  because you could use the same memory over and over, but for an exponential amount of time.
*  So you could say polynomial time is contained in polynomial space, which is contained in
*  exponential time. And the reason polynomial space is contained in exponential time is that, well,
*  if I have, let's say, n bits of memory, then my computer can pass through at most two to the n
*  power possible states before either it halts or else it gets into an infinite loop, right? An
*  infinite recurrence, right? So you can relate time and space to each other in that kind of way.
*  Now, already here, we encounter some of the most enormous open problems in mathematics. So, for
*  example, is polynomial time equal to polynomial space? No one knows. We expect that the answer is
*  no, but no one has proven that. So sorry, let's not let that go by too quickly. So you said before
*  it's contained in, but you didn't say you didn't mean that it's properly, we're not sure whether
*  it's the same size. That's right. Exactly. Exactly. Everything you can do in polynomial time, you can
*  also do in polynomial memory. And that's because each, at least if I have a serial computer,
*  each time step is accessing at most one memory location, right? So after t time, I can access
*  at most t memory. But we don't know whether everything you can do in polynomial memory can
*  also be done in polynomial time. We would expect no, because if the answer were yes,
*  that would mean that, for example, there was just some super duper algorithm to play chess
*  perfectly, or Go, or any other game. Not merely as well as let's say AlphaGo plays it, but to play
*  it perfectly. You got to fill in the details there. You mean because we could just give it enough
*  memory? Well, because it is known that you could perfectly play any of these games, like two player
*  games of perfect information using a small amount of memory. Because all you need to do is evaluate
*  what's called the game tree. The game tree is the thing that says, is there a move I can make such
*  that for every move that the opponent makes, there is a move I can make and so on such that I win.
*  And that's a tree where you can basically just traverse that tree. It's an exponentially large
*  tree, but you can reuse the same memory over and over. So playing games is a problem you can do in
*  small memory. Now, if p were equal to p space, that would mean that perfectly playing all these games
*  would also be a problem that you could solve in a small amount of time. And that would be amazing.
*  Right. So, okay, but then is p space equal to exponential time? So everything that you can do
*  in exponential time, can you also do it with small memory? Again, no one knows. We expect that the
*  answer is no. No one has proven it. Okay, now I don't want to give the impression that we're
*  complete ignoramuses. Okay. So, you know, as one example, we do know that exponential time
*  is bigger than polynomial time. Okay. That we know. Okay. So you can prove that more time,
*  when you've got more time, then you can solve more problems that you couldn't solve with less time.
*  Likewise, when you've got more memory, you can solve more problems that you couldn't solve with
*  less memory. Okay, but when you're comparing different resources, like time against space,
*  then it becomes very hard. So just to translate that, you're saying that we know there are problems
*  that cannot be solved in polynomial time, but can be solved in exponential time and likewise,
*  for space. Precisely. Yes. And even more fine grained than that, like we know that there are
*  problems that can be solved in n to the 2.4 time that cannot be solved in n to the 2.3 time, for
*  example. Let me pause for a second to talk about Grammarly. This is an app that can help you improve
*  as a writer. It's not something very simple that just corrects your spelling mistakes.
*  Grammarly is a digital writing assistant that actually improves your style. I personally found
*  it very useful because not only does it say, well, you made a grammatical mistake here,
*  it offers suggestions for vocabulary improvements or the tone of what you're writing, or even ways
*  to make your writing more vivid. Grammarly works across a variety of different apps.
*  Whether you're typing a document in Word, or whether you're on Twitter or Gmail or whatever,
*  Grammarly can step in and offer extremely useful advice to raise your writing to the next level.
*  With Grammarly Premium, you can set goals, you can get an overall writing score,
*  vocabulary suggestions, concision checks, and more. And right now you can get 20% off Grammarly
*  Premium if you go to sign up at grammarly.com slash mindscape. That's a special offer for
*  mindscape listeners, 20% off at grammarly.com slash mindscape, g-r-a-m-m-a-r-l-y dot com slash
*  mindscape. It is an interesting feature of this field that I'm not going to give you a hard time
*  for not having proven anything yet. That's okay. Everything, everything. I have proven something.
*  Maybe exactly.
*  Not the things that we most want.
*  There is this thing that comes up over and over again where here's something we haven't proven yet,
*  but every person has the same opinion about what the answer is eventually going to be,
*  because it would lead to this very, very strange thing if it turned out not to be true.
*  How reliable is that sort of quasi-argument in your mind?
*  Well, I think that we need to be prepared for the possibility of surprises. I would say that there
*  already have been surprises. There have been cases where people thought that two complexity
*  classes were different that then turned out to be the same. I would say that none of those were
*  nearly as surprising as let's say p equals p space would be. But there were things that
*  I mean, look, if there were no surprises, then you could say, well, why even do it?
*  Yes, there have been surprises, but I think that the right way to think about it is that
*  even though this is pure math, the way that we approach it has some elements of empirical science
*  also. I mean, physicists don't prove that there's no superluminal signaling.
*  They don't prove that quantum mechanics is correct. I mean, these are taken as very well
*  supported assumptions relative to our present state of knowledge, let's say. And then much more fine
*  grained things than that, like that there's CPT symmetry and on and on. And you could have sort of
*  a hierarchy of surprisingness, right? If you could send, if let's say the opera experiment had been
*  correct and you could really send the neutrinos faster than light, well then that is sort of at
*  the top of the hierarchy of surprisingness, right? And there are many other things that could happen
*  in physics that are not quite as surprising as that, a new particle at the LHC, but still,
*  you would take it, right? It would still overturn something that had been previously believed.
*  It's amazing to me how many people bring up those damn superluminal neutrinos as something that
*  is in everyone's head as something you guys almost believed that for a while.
*  Well, no, I mean, look, the physicists who I knew, I mean, none of them thought it was very likely
*  that it was correct. We have priors, we're good Bayesians, so that's the point. Exactly, exactly.
*  And I would say it's exactly the same with us, right? We're just trying to be Bayesians and have
*  priors on things. And you can say if two complexity classes, let's say, if they have
*  been enormously studied for like 60 years and again and again people did things that if they
*  had turned out slightly differently, then these two classes would have been equal. And yet every
*  single time, it just miraculously avoids whatever theorem they prove, just miraculously avoids the
*  thing that would make those classes equal. Then you start to suspect that, well, maybe there's
*  a deep reason why they're different. Do you begin to anthropomorphize your complexity classes as you
*  learn more and more about them? Do you say they don't want this to happen? Oh, absolutely.
*  Oh, absolutely. I mean, you know, I mean, this is the thing, like, each one has a personality,
*  right? They're like comic book superheroes, right? Each one has a different set of powers,
*  right? And like, sometimes, some are just clearly better, more powerful than others. Other times,
*  you get two classes with just, you know, bizarrely incomparable powers, right? And so then you try to
*  compare them to each other. But it's just kind of like asking, you know, like, I don't know,
*  it's like one of these internet memes of, you know, who would win in a fight, like, you know,
*  Godzilla or Batman or something. I know, sorry, just they're from different universes.
*  Exactly.
*  But yeah, but so, you know, the sort of less, you know, obvious, maybe slightly less obvious thing
*  you can do, but that turns out to be of absolutely central importance is you define complexity
*  classes in terms of what is provable, okay? Or like what has a short proof, right? And this is
*  what leads to, I would say the next, you know, most famous complexity class along with P,
*  which is called NP. Okay, now, NP doesn't stand for not polynomial.
*  See?
*  Okay, stands for stands for non deterministic polynomial. But don't worry about what that means.
*  It's, you know, I can, I like I can say what it means in plain language. Okay, a problem is in NP,
*  if whenever the answer to it is yes, meaning like, yes, there is a solution, then someone can show
*  you the solution. And you could check the solution using a polynomial time algorithm. Okay, so,
*  so let me give an example, like a jigsaw puzzle. Okay, you know, like, especially if there's no
*  picture on the jigsaw puzzle, it could be, you know, it could take quite a while to do one,
*  right? But once it's done, and you know, you've made some neat square, well, then, you know, you
*  can, anyone who doesn't believe that you did it, you just show them that you did it, right? Similarly,
*  you know, finding the prime factors of a gigantic number, right? This is a, you know, well, well,
*  you know, for better or worse, most of the encryption that we use on the internet is based
*  on the belief that this problem is hard. You know, this and a few closely related problems,
*  that finding the prime factors of a gigantic number is a hard problem. But if you did find the
*  factors, then, well, you know, you might not want to multiply them, but your computer could very
*  easily multiply them and check that those factors, you know, were the correct ones. Likewise, with a
*  Sudoku puzzle, likewise, you know, with optimization problems, I mean, it might be hard to prove that
*  you found the best solution. But, you know, if you just want to convince, let's say you're a
*  consultant, you know, you want to convince your client that you found a solution that will only
*  cost them this much money, right? Well, you just show them your solution. Okay, so these are all
*  examples of NP problems. And the way things fit together is that P is contained in NP,
*  which is contained in P space. By the way, I just want to make it clear so everyone knows.
*  Yeah, absolutely. Absolutely. The picture that we have, you know, there's like this
*  big space of problems, and we draw some kind of Venn diagram of these complexity classes. But they
*  don't need to be nested, right? Like two complexity classes can have some intersection, but some
*  non-intersection also, and a third one might intersect with some of them, but not others,
*  right? Is that fair? Absolutely. They don't all live right inside each other. All of these things happen.
*  Right. So I mean, some of them do fit in a linear order, you know, as I was saying before,
*  but probably not well, right? Some of them do fit that way. Like P is contained in NP,
*  is contained in P space, is contained in X, meaning exponential time. And, you know, we believe that
*  each one is strictly more powerful than the last, but all we know so far is that X is larger than P.
*  So, you know, which means that either P is different from NP, or NP is different from P space,
*  or P space is different from X, right? At least one of those three has to be true.
*  We think all three of them, but we only know that at least one is true.
*  And you mentioned-
*  Now the most-
*  Yeah.
*  You mentioned about factoring that you believe it's hard, but you didn't say that we know it's hard.
*  That's right. That's right. So right. So now, you know, we can go in and now, you know, I mean,
*  for, in fact, we don't know that any NP problem is hard, right? I mean, this is the,
*  you know, this has been the situation for the last half century, that, you know, we, you know,
*  famously, we cannot prove that P is not equal to NP.
*  So NP, sorry, sorry. NP problems are those that we can easily check the answers to.
*  Exactly.
*  And you're saying that we believe there are problems that are hard to solve, but easy to check,
*  but we can't prove it yet.
*  Exactly.
*  We cannot prove it yet.
*  Exactly. Exactly. That is if you've heard, yeah, if listeners have heard of the famous P versus NP
*  question, that is that question. And now factoring is an NP problem, but, you know, but factoring,
*  we think is a very special problem. Okay. So it could be that someone just discovers a fast
*  algorithm for factoring, you know, and then, you know, that would break most of the security
*  of electronic commerce, but it wouldn't necessarily mean that P would equal NP, right? Because maybe
*  they just solve that one special problem. Okay. Now the surprising part, the big surprise to people
*  in the early 1970s was that most of the hard problems in NP are not like that. Most of them
*  have an amazing property of universality, a property that we call NP completeness.
*  Okay. And what NP completeness means is that you show that your one specific problem has the
*  property that if anyone could solve it in polynomial time, then P would equal NP. Then you could solve
*  every NP problem in polynomial time.
*  So this goes back to that game that you mentioned before, where you just relate the hardness of
*  problems to each other, even though you don't-
*  Exactly.
*  You might not know what the hardness of any of them are, but you can say that they're equally
*  hard.
*  Yeah. You know, it's all the same. Yeah. So, and this is exactly what I was talking about before,
*  about, you know, you may start out as a taxonomist, but ultimately you want to discover
*  something deeper, right? And what you discover is that, you know, there is this huge class of easy
*  problems, you know, the P problems. Then, you know, then there's this huge metropolis of
*  hardness, if you like, these NP complete problems, right? You know, which includes just
*  literally thousands of the problems that sort of engineers and scientists, you know, would care
*  about, you know, airline scheduling, you know, traveling salesperson problem, you know,
*  just about any kind of combinatorial optimization problem that, you know, you could imagine
*  involving, you know, a whole bunch of variables, a whole bunch of constraints, you know, sort of
*  problems like that will be NP complete unless they have good reasons not to be.
*  Is this one of those ones where packing luggage into your trunk is one of them?
*  Yeah, fitting, fitting luggage into the trunk of your car. That might be one that many people
*  have experience with. There's a there's a there's a beautiful paper from a decade ago that proves
*  that Super Mario is NP complete. Yes. You have to create these crazy levels with like these weird
*  patterns of these Koopas that you stomp on, you know, that encode the logic problem, but you can
*  you can do that. So basically you get the luggage in your trunk is a good is a good reminder because
*  even though we say NP complete means super duper hard, people have put luggage in their trunk.
*  What we mean is that as their trunks have, if you imagine larger and larger trunks and more and more
*  luggage, it just becomes very unwieldy very quickly. That's right. That's right. What it what it means
*  is that if I wanted to, I could, you know, give you a very, very hard time figuring out how to fit
*  some luggage into your trunk. Like I could even in principle, I could design some, you know, millions
*  of boxes of different dimensions, you know, that would have the property that you can fit, you know,
*  these boxes into your trunk and have it closed if and only if there is a proof of the Riemann hypothesis
*  of it most assert next. Right. Okay. Or for example, that in order to fit them in your trunk,
*  you would have to break some cryptographic code. I could also do that. But if someone showed you a way
*  to put them in your trunk, you would be easily enough to be able to say, yep, that worked. It was
*  easy to check. Yep. Exactly. Exactly. Yeah. So there's these NP complete problems, you know,
*  and it's sort of a priori. It didn't have to be that way. But you know, this is a substantive
*  discovery, right? That, you know, these most of these hard NP problems are actually all equivalent
*  to one another. Yeah. In the sense that a fast algorithm for any one of them implies a fast
*  algorithm for all the rest. And then there are a few outliers, right? Factoring is one of the weird
*  ones. Okay, that might be sort of somewhere in between P and NP complete in some no man's land.
*  Besides the anthropomorphization and the personalities, does thinking about the stuff
*  tend to turn you into a mathematical Platonist? Thinking that there really is a mathematical
*  reality out there because of all the structure that you wouldn't have imagined existing before
*  finding it? Yeah, I mean, I mean, I feel like probably every mathematician, we know, while
*  they're actually doing their work is in practice a Platonist, right? You know, they might claim
*  later that they're not one, right? But I mean, to do math is to, you know, you know,
*  push back against something that can tell you that you were wrong, right? It's not just, you know,
*  a thing that you were making up, right? It is a thing that has constraints that are external to
*  you. And in that way, you know, you know, it is like empirical science. Well, you made that point
*  before. It's really interesting because you I think you've made the point like in comments on
*  my blog that this kind of discovery, I will mention in the introduction that you are a world
*  famous blogger and stuff like that. But you that the kinds of things we learn about the real world
*  by these purely mathematical discoveries are, you know, at least rubbing shoulders with the
*  kinds of things we learn about the real world by doing empirical science, like the universe could
*  have been expanding or contracting, and we had to go out and look at it to find out which way it was.
*  But it's really, really hard to put boxes into your trunk in the most efficient way. And you
*  want to sort of say that one of those is comparable to the other in terms of important insights about
*  the universe. Yeah, I mean, you know, it's funny because, you know, I've, you know, I am often in
*  conversations with my many, many physicists friends where, you know, we are ribbing each other. And,
*  you know, and they will point out that, oh, you know, I'm just a Platonist in some abstract,
*  la la land while they're dealing with the real world. And then, you know, if these are theoretical
*  physicists, I can reply that I've actually, I'm an author on more experimental papers than they are.
*  Safe bet. Yeah. But, you know, I mean, look, I mean, you know, even in physics, right, you know,
*  you are a theoretical physicist and a cosmologist, right? You know, you are not, you know, on a
*  typical day out at the observatory, you know, peering through a lens, right? You are thinking.
*  You are, you know, thinking hard about things that we already know and trying to deduce the
*  consequences of those things or trying to build models that explain something.
*  And that's also what we do in math and in theoretical computer science.
*  Yeah, no, I'm on your side. I just want to give you a chance to put into your work.
*  Yeah, yeah. Yeah, yeah, sure. But no, I have described my position as not so much a Platonist,
*  but an anti-anti-Platonist. OK, because, you know, look, look, I mean, I mean, I mean,
*  Plato wrote all kinds of, you know, really weird trippy stuff, right? And I, you know, I don't want
*  to like give him a blank check that I agree with whatever he said. You know, I haven't even read
*  enough of Plato to know, you know, if I, if I agree with everything he said, right? And it sounds
*  quasi-mystical and weird to be talking about this world of, you know, perfect triangles and, you know,
*  perfect squares or whatever, right? You know, I don't, I don't know if it has a metaphysical
*  existence, but I will say this, that, you know, if we ever encounter an extraterrestrial civilization,
*  and, you know, we are able to communicate with them, I think that they will agree with us about
*  the Pythagorean theorem. I think that they will, you know, have discovered much of the same math
*  as we have discovered, because I think that it is not just an arbitrary cultural creation. I mean,
*  it has cultural aspects, but, you know, it is sort of constrained by, you know, the, well, by logic,
*  by truth. Well, yeah, okay. I mean, let me push back a little bit on that in my role as a devil's
*  advocate on the podcast. The Pythagorean theorem is true in Euclidean geometry, so it's sort of,
*  it's a conditional statement that says if you accept the following set of axioms, then you
*  prove the Pythagorean theorem. And every statement in math is like that. If the axioms are true,
*  then the conclusions follow. But, so one could say we will never learn anything exclusively about
*  the actual world that way, because we don't know what axioms are true. Yeah, I mean, you know,
*  there are really two questions, right? One is, you know, which we could call the easy question,
*  you know, if we can agree on the same axioms with the aliens, will we agree about the consequences
*  of those axioms? Right. Right. And I hope most people would agree that the answer is yes,
*  that, you know, we'll agree about what are the laws of logic, or sort of what are the rules of
*  inference that we can use to validly draw conclusions from axioms, right? But then there's
*  sort of a broader question, maybe a harder question, you know, will we and the aliens have
*  thought of the same axioms, right? Will we have thought about similar mathematical objects,
*  such as Euclidean space, you know, the space where the Pythagorean theorem holds, or such as
*  the positive integers, right? And I think, you know, that, okay, so there certainly are some,
*  you know, mathematical objects that, you know, we have invented that probably the aliens will not
*  will not have invented. Chess would be an example of such an object, you know, maybe like, you know,
*  particular cryptographic codes that we happen to use, like AES, you know, I doubt the aliens will
*  have that. But, you know, I'd be willing to wager a lot that the aliens will have a concept of
*  integers, that they will have a concept of Euclidean space, you know, and even more than that,
*  they will have a concept of complex numbers, you know, and things of that kind, right? There
*  are certain things that are just really, really fundamental to the mathematical universe, where
*  even if you started out in a different direction, you would eventually have to reinvent those
*  concepts, because they're so ubiquitous. If I were really being the devil's advocate,
*  I would say that maybe the reason why certain sets of axioms seem so natural to us is because,
*  not of math, but because of physics, of the particular way that the physical world around
*  us has arranged itself to make certain things more natural for us to describe it. Yeah, okay,
*  well, well, then it becomes an even more interesting question, right? Like, let's say,
*  okay, so, you know, I was imagining talking to aliens who live in the same universe as we do,
*  even though they had a completely separate evolutionary history. But now we could also
*  imagine some aliens in a parallel universe with completely different laws of physics, right?
*  Maybe, you know, it's not even quantum mechanics, maybe they don't even have a
*  space-time, even approximately, I don't know, maybe they're all just sitting on top of each
*  other or something. But, you know, I mean, one thing that we can say is that, you know, we can
*  imagine many ways that the laws of physics could have been different, but where, you know, we would
*  have invented much the same math in order to think about it, right? So, I mean, you know, we,
*  and in fact, it has happened again and again in the history of math and physics that, you know,
*  mathematicians have invented a certain concept well in advance of that concept being needed by
*  physics, right? They had their own reasons for inventing it, you know, that were not in any
*  direct way motivated by physics, but then they just turned out to be, you know, very handy,
*  you know, when physics had reached a certain point. And I think, you know, if you look at
*  examples like that, you know, you could say maybe that is just because these concepts are so
*  fundamental that, you know, sort of any laws of physics, if you go deep enough into them,
*  you want to understand them deeply enough, you know, you might be tempted to reinvent those concepts.
*  I think, for example, concepts of symmetry groups would be an example. Yeah, I think that this is a
*  rabbit hole we could probably dig even deeper, but I do want to switch topics onto your opinion of
*  what I've heard on the internet, which is that once we build quantum computers,
*  all of these hard problems will become suddenly easy.
*  Ah, okay. Yeah. So this actually feeds beautifully into the discussion that we were having earlier
*  about, you know, could there be like different classes of problems with different incomparable
*  powers, right? Now, a perfect example of that is provided by quantum computers. Okay, so
*  you know, the once we ask sort of what is efficiently computable, right? What is
*  computable in polynomial time? You know, you might worry that the answer to that might depend
*  somewhat on physics, right? And, you know, and actually, you know, apparently, it was asking
*  that question that sort of led David Deutsch to the idea of quantum computing in the first place
*  in the early 1980s. So the way that it could potentially depend on physics is because what it
*  means to do a computation depends on what kind of physical things you're pushing around.
*  Precisely, precisely. Now, Turing's definition of computability in the 1930s had this sort of
*  amazing invariance to the details of physics. Like it just it doesn't care whether the universe is
*  classical or quantum or you know, how many spatial dimensions there are, right? You just get the same
*  notion of computability. Okay, but once we ask about efficient computability, polynomial time
*  computability, well, then, you know, it's still very, very insensitive to a lot of the details
*  of physics. You know, and that's that's sort of why we like this notion, you know, that it gives
*  you a nice elegant theory doesn't depend on, you know, your specific model of computer. But
*  the really cool thing that emerged in the 80s and 90s is that while changing the laws of physics
*  from classical to quantum, that does seem to be enough to enlarge what is computable in polynomial
*  time. Okay, once again, this shouldn't surprise you at this point. No one can no one has proven that.
*  Okay, but we think so. Okay, so, so the way that, you know, to say this in complexity language
*  is that there is a class of all the problems that are solvable in polynomial time using a quantum
*  computer, which, you know, we could get into exactly what that means. But you know, it's a computer
*  that could have not just bits in its memory, but quantum bits, what we call qubits, bits that can
*  be in superposition states, and that can even be entangled with each other. Right. And so the the
*  sort of key property here is that if I have, let's say 1000 qubits, 1000 quantum bits, then just to
*  describe their state, I need a list of two to the 1000 complex numbers. Okay, I need a quantum
*  mechanical amplitude for every possible configuration of all of these bits. So we're, we're,
*  we're talking about enormously larger objects here. Right. And so that at least opens up the
*  potential that we could compute more things in polynomial time. You know, it will take work to
*  see whether that potential is realized. But we can define a class of problems that is called BQP,
*  bounded error quantum polynomial time. This was defined in 93 by Mesh Vazirani, who was my advisor
*  at Berkeley and his student then, Ethan Bernstein. And they basically just defined it as a quantum
*  mechanical generalization of P. So it's like what you can do in polynomial time with a quantum
*  computer. The B for bounded error, that's just saying that, well, the you know, the the computer
*  doesn't always have to output a right answer. It's just for every input, you know, the you should
*  have, let's say, at least a 90% chance of getting the right answer. Yeah, because the you know,
*  and we're and we're, we're, we're happy with that. Because if you don't like 90%, well, then just
*  repeat the computation a whole bunch of times and take the majority vote among among the answers.
*  Yeah, right. So, so so that's BQP. Now it's, you know, it was it's, it's pretty easy to show
*  that BQP contains classical P. Or in other words, a quantum computer can always efficiently simulate
*  a classical computer. That makes sense. Right. The way I like to describe that is like you could use
*  a space shuttle to taxi around the parking lot. It wouldn't be very smart wouldn't be, you know,
*  very useful, but you could do it. Right. The interesting question is, you know, is BQP larger
*  than P? That is, are there things that you could solve in polynomial time with a quantum computer,
*  but you can't solve in polynomial time with a classical computer that would even take exponential
*  time for a classical computer. Right. Okay, so and, you know, we don't know the answer. I mean, the
*  when Richard Feynman talked about this in the early 80s, you know, he suggested the problem,
*  well, what about the problem of simulating quantum mechanics itself? Right. And, you know, and that
*  is one of our best candidates to this day, for what a quantum computer will be useful for, you know,
*  if and when we can really make it practical. Okay. But, you know, maybe some people would like a less
*  tautological example of, you know, what a quantum computer could do or sort of an example that is
*  not itself about quantum mechanics. So that came by, you know, and now super famous discovery in
*  1994. And this was when Peter Shor discovered Shor's algorithm for factoring. Okay. So what Shor
*  discovered was that the problem of factoring huge numbers, the one that we talked about before,
*  right, the one that most modern encryption is based upon, and that, you know, that's an NP problem,
*  but it's kind of special. We don't know whether it's in P or not. Shor showed that the factoring
*  problem is in BQP. Okay. So we showed that if you could build a quantum computer, then you could
*  factor an n-digit number using a number of elementary operations that only scales like
*  n squared, roughly. Right. Okay. And so this means that, excuse me? Whereas the classical
*  belief? The best known classical algorithm takes time that grows like exponentially in roughly
*  the cube root of n. Okay. It's something fancy called the number field sieve. But we count that
*  as exponential, even though it's the exponential. Yeah, yeah. We'll count that as exponential. And,
*  you know, I am sure that the NSA, you know, cares enormously about, you know, the exact
*  pre-factors in that exponential and so forth. But, you know, we'll count that as exponential.
*  Yeah. Yeah. But we don't know that there isn't a better one classically. That's the issue.
*  That's right. We absolutely do not know that. And, you know, in fact, we don't know,
*  you know, it could be for all we know today that P equals BQP. Right. In other words,
*  maybe everything that a quantum computer can efficiently solve could also be efficiently
*  solved by a classical computer. Right. Right. So, you know, what Shor showed, you know, again,
*  is to sort of, you know, relating our different, you know, domains of ignorance. Right. He showed,
*  you know, if you wanted a general way to simulate quantum mechanics with a classical computer,
*  then you would also have to invent a fast classical algorithm for factoring. Yeah.
*  And it is true. I think we do know that there are problems for which
*  there is a quantum algorithm that is provably faster than any classical algorithm, but not in
*  an entirely different complexity class. Is that right? Yes. Right. So this is OK. Good. Good. Now
*  we're getting to something that is, you know, when I teach my undergraduate class, this is always,
*  you know, one of the more subtle points. But I'm glad you're asking about it. There is a thing
*  called the black box model. OK, where it's sort of a different game, a different domain, where you
*  just ask the question, suppose that I have a black box that, you know, just evaluate some function
*  for free. Right. And now, you know, like maybe it's a subroutine or I don't know its inner workings,
*  for example. OK. And now I just ask how many questions do I need to ask to this black box
*  in order to learn something that I want? OK. So, you know, as an example, like I love, you know,
*  playing a game, you know, playing the game with my seven year old daughter where, you know, she
*  shall think of a number from, you know, one to one hundred. And, you know, and then I say, you know,
*  is it bigger or smaller than fifty? Is it bigger or smaller than seventy five? You know, and with
*  seven questions, you can find a number. Right. So she would then be the, you know, a black box.
*  And we could say that the query complexity of this problem is like seven queries. Right. But now,
*  you know, you could you could ask and people have asked, well, what changes if I could somehow ask
*  my daughter many questions in quantum superposition and get back a superposition of answers?
*  If anyone can do it, Scott, I think it's going to be you. What? If anyone can do it,
*  I think you're the best bet. OK. All right. All right. Anyway, you know, in this model of
*  of query complexity, here we really do have proven advantages of quantum computers over
*  classical ones. And some of these advantages are exponential. Some of them are even more than
*  exponential, by the way, like there are problems that involving end bits of input where it takes
*  a square root of about square root of n queries to solve them classically. And they can be solved
*  with only one query with a quantum computer. OK. Literally one that that's, by the way, a paper that
*  my colleague, Andreus and Bionis, and I wrote five years ago. And we also prove that that gap is the
*  largest possible one between classical and quantum. OK, good. But just just, you know, just plug in my
*  own. Yeah, that's why we're here. OK. But yeah, yeah. But so in this, you know, in the setting of
*  query complexity, we do know how to prove that quantum computers are are strictly better than
*  classical ones for some problem. But now you could say, you know, in the real world, you know, so
*  so so so so query complexity is like a very, very useful playground for sort of figuring out what
*  might be true, sort of like if you can't even get a separation in query complexity, then probably you
*  have no chance to get a separation in the real world right between one type of computer and
*  another type. OK, but, you know, ultimately you do want, you know, you do want an advantage of
*  quantum computers that will persist even in the real world where where you don't have these magic
*  boxes for answering questions. Right. So, you know, I've I've I often explain it to physicists by
*  saying, you know, query complexity is our perturbation theory. Like, you know, it is it is it is it is this
*  streetlight to look for your keys on. Right. Where you can actually answer the questions. But OK,
*  so so in this sort of quote unquote real world there, you know, what we know is that P is contained
*  in BQP, meaning everything a classical computer can do. So can a quantum computer. We also know
*  that BQP is contained in peace space, which means anything that you can do in polynomial time with
*  a quantum computer, you can also do in polynomial space with a classical computer. OK, so that means
*  that means several things. That means that, you know, in terms of like running time in the real
*  world, quantum computers could at most give you an exponential advantage over classical ones.
*  Right. So they're not going to solve the halting problem. They're not going to solve anything that
*  is literally uncomputable for a classical computer, but they could solve certain things up to
*  exponentially faster. And it all it also means that we have a very good excuse for why we cannot
*  prove today that quantum computers are are better than classical computers in the real world.
*  There and the reason is if you wanted to prove that P is not equal to BQP, well, then you would
*  also have to prove that P is not equal to peace space. That's a famous unsolved problem. That's
*  like as big a problem as P versus NP. Yep. Right. You said you make money for solving it.
*  Yeah. Well, yeah, right. Right. It happens not to have a million dollar prize. But, you know,
*  you know, you know what I say about this, by the way, you know, so so there are these
*  from people who don't know there are these seven million dollar clay challenge problems. You know,
*  the first one is P versus NP. And then there's the Riemann hypothesis. There's the Pankarae
*  conjecture, which was solved by Perelman, although he refused the prize. I wouldn't have done that.
*  I would. OK. Yeah. And there are four other problems. You know, I like to say that P versus
*  NP is just clearly the most important of the seven. Right. And, you know, and I have several
*  reasons for that. One of them is that, well, if P, you know, if you could prove that P were equal
*  to NP and furthermore, your algorithm was actually efficient in practice. So now like end to the one
*  thousand. But, you know, let's say N squared or something like that. Well, then, you know, you
*  could not only collect a million dollars for solving that problem, but you could also solve
*  the other six problems because you would just program your computer to say, you know, is there
*  a proof of, you know, at most a million characters written in some formal language that a computer
*  can check? Right. Right. And because, you know, computer can easily check the proof, that means
*  that if it's there, then if P equals NP, the computer can also easily find the proof. OK. But
*  not only that, I mean, forget about these measly million dollars. Right. You know, if P equals NP.
*  Well, I mean, you know, you could start by stealing two hundred billion dollars worth of Bitcoin.
*  And I guess then decide what to do next in your quest for world domination. OK. But I think
*  it's important because it really is driving home the reason why when mathematicians say things like
*  even though we haven't proven that P is different from NP, we're all sure it's not true because NP
*  is this collection of problems, some of which seem so hard that if you show that they were really
*  easy, you'd be axiomatizing all sorts of things that we think are just preposterously difficult.
*  Exactly. So, yeah. So I mean, some people, you know, they may have an intuition that, well,
*  you know, like when I run across NP complete problems in my application domain, which might
*  be some machine learning, some AI optimization, oh, you know, they tend not to be so hard. I just
*  run some heuristic algorithm and it does perfectly well. So, you know, so while you know,
*  what makes you so sure that P is different from NP? And, you know, my response tends to be, well,
*  you know, why haven't you made billions of dollars from mining Bitcoin? Right. I mean,
*  you know, you could say, you know, since since 2008, that's been the easiest answer. Right.
*  I mean, you know, you I mean, I mean, yes, if you only try to solve easy instances of your problem,
*  then they will be easy. But, you know, the the point of a problem being NP complete is that you
*  can encode these enormities into it, like finding a proof of the Riemann hypothesis, like, you know,
*  mining billions of dollars of Bitcoin and, you know, and so forth. You know, anything for which
*  an answer could be easily checked. Or, you know, another example would be compressed Wikipedia,
*  you know, into like the best, you know, the best like, you know, the smallest file you can,
*  where it could then be easily decompressed. Okay, that's another example of an NP problem,
*  where, you know, in order to solve that problem, it is, you know, at least a plausible speculation
*  that the computer would have to sort of understand human knowledge in a very, very deep way,
*  and solve a lot of the problems of artificial intelligence. But, you know, again, if P equals
*  NP, it would just, you know, you would just type with a few keystrokes, you would do that.
*  And likewise, this is why we, our intuition tells us that even quantum computers are not going to
*  be able to solve NP complete problems. Exactly. Yes. So now we're good. So now we come to, you know,
*  a wonderful example of two complexity classes, two models of computation that we really do think are
*  incomparable. And those are, or that as far as we know, are incomparable. And those are NP and BQP.
*  Okay, so, you know, the easily checkable problems, and the problems that are easily
*  solvable by a quantum computer. Now, you know, the the in some sense, the biggest mistake that
*  popular writers make when they write about quantum computers, you know, and, you know,
*  and then this has been true for like 25 years by now, okay, is that they sort of they conflate NP
*  with BQP. Right? They write as if a quantum computer would just be a magical machine for
*  solving NP problems. They say, Well, look, a quantum computer just has to try each possible answer
*  in a different parallel universe, you know, a different branch of the wave function,
*  then the you know, and in some sense, you know, it is actually true that a quantum computer can do
*  that. Yeah, that's not even a hard thing to do, to program your quantum computer to create a
*  superposition over every possible answer. The hard part is reading out the answer that you want. Okay.
*  So, you know, if I just, you know, I mean, I mean, you know this, Sean, but you know,
*  for the benefit of our listeners, right? If you if I just create an equal superposition over every
*  possible answer to some, you know, super hard problem, like, you know, all possible keys for,
*  you know, breaking a cryptographic code, let's say, and then I just measure it, not having done
*  anything else, the rules of quantum mechanics tell me that what I will see will just be a random
*  key, a random answer. Yeah. Well, if I just wanted a random key, I could have picked one myself with
*  a lot less trouble, right? I didn't need to build a quantum computer for that. Okay, so,
*  you know, but then, you know, that makes it sound like, well, then maybe quantum computers are not
*  really useful for anything at all, you know, if all they can do is pick random answers. But no,
*  you know, it is a little more than that, that they can do. And the reason why we say why they can do
*  more is that the quantum rules of probability are different from the classical rules of probability.
*  Okay, so in quantum mechanics, each possible configuration that your system could be in
*  gets assigned this number called an amplitude, right, which is very closely related to, you know,
*  the probability that you see the system in that configuration when you look at it, but it's not
*  a probability. So unlike probabilities, amplitudes can be negative, they can even be complex numbers.
*  Okay, and in some sense, the central trick in quantum computing, sort of the trick, you know,
*  behind every single quantum algorithm is this, that you are trying to choreograph a pattern
*  of interference of these amplitudes, okay, where for each wrong answer, what you would like is for
*  the amplitude of that wrong answer to be a sum of many contributions, potentially, but some of those
*  contributions should have positive amplitude and some should have negative amplitude, or, you know,
*  they should point in every which way in the complex plane, and so they mostly just cancel each other out.
*  Whereas for the right answer, the answer that you do want to see, you would like all of the
*  contributions to its amplitude to be pointing the same way, or mostly the same way. Okay, so you would
*  like constructive interference. It's like a resonance. Yeah, exactly, for the amplitude of the right answer.
*  If you can arrange that, then when you measure, the right answer will be seen with high probability,
*  and of course, if it's not seen, you can just try again until it is, right, but you're trying to
*  exploit interference to boost the probability of seeing the right answer to way, way more than it
*  would have been with any similarly efficient classical algorithm. Now, you know, the tricky
*  parts here are that, well, you know, you've got to do all of this despite not knowing yourself which
*  answer is the right one in advance, right, because, you know, if you knew that, then there would kind of be
*  no point, right, so, you know, you need to sort of arrange this interference pattern where you know
*  for some mathematical reason that it's going to concentrate the amplitude on the right answer,
*  even though you don't know yet which one that is, right, and you've got to do it fast. You've got to
*  do it, you know, much faster than just a classical brute force method could have found that same
*  answer, or else, you know, the quantum computer is not winning, right, so, you know, it was, you know,
*  it is a really bizarre hammer that nature gives us for sort of extending computation, you know,
*  beyond what Turing knew about, right, and it is sort of, it is a happy miracle that we can
*  occasionally find some nails for that hammer to hit, okay, you know, factoring was a very famous
*  example of such a nail, right, you know, but now it is very important for people to understand
*  that to design his fast quantum algorithm for factoring, Peter Shor really had to exploit some
*  very special structure in the factoring problem, stuff that comes from, you know, from group theory,
*  from number theory, from the Fourier transform, you know, it's just a beautiful set of ideas
*  that goes into it, but it is not something as simple as just I try every possible divisor in
*  a different, you know, parallel universe, you know, if it were that simple, you wouldn't have needed
*  Peter Shor to think of it, okay, and it is not, and as far as we know, it is not something that
*  extends, generalizes to the NP-complete problems, right, it is, you know, I said before that factoring
*  is not believed to be NP-complete, right, it has a lot of very, very special structure, I mean, just
*  one simple example is, you know, if I gave you a, you know, some boxes to fit into your trunk,
*  a priori they might not fit at all, or there might be only one way to fit them, or there might be a
*  thousand ways to fit them, right, you don't know, but if I give you some huge composite number,
*  then no matter how hard it is to factor, you know in advance that it has one and only one prime
*  factorization, right, because you could prove that 300 BC, right, so factoring is special in a whole
*  bunch of ways, and you know, its specialness on the one hand is what makes it so useful for cryptography,
*  right, you use the structure of factoring to do all the beautiful things that enable modern
*  cryptography, but the other side of the coin is that that structure is what Shor was able to exploit
*  in order to sort of choreograph this interference pattern with a quantum computer
*  that reveals the factors of your number. But this does sound a little deflationary in the sense that,
*  I'm sure you'll correct this, but it sounds like factoring, we sort of lucked into it in the sense
*  that it is a hard problem, but one that quantum computers are very good at, typical exponentially
*  hard problems will still be exponentially hard on a quantum computer, is that a safe thing to say?
*  That is what we think, that is what we think, and this is, by the way, this is something that, you
*  know, I have been, you know, I've been trying to, I mean, you know, it is not controversial, by the
*  way, within the field, and I've been trying to explain it to, you know, people for 15 or 20 years.
*  It used to be the tagline of my blog, because I found myself just explaining the same thing to
*  journalists, like week after week after week, like no, we do not expect that quantum computers will
*  just exponentially speed up everything, you know, it depends on the structure of your problem, and
*  you know, because, you know, this is often not what people want to hear, but, you know,
*  I feel like we should be telling the truth. This podcast will do it, now that you're on Mindscape,
*  I think that everyone will be educated. That's right, that's right, yeah, yeah, yeah, no, I mean,
*  well, you know, I love, you know, having a forum that is so devoted to truth, as I know that you are.
*  Okay, but now I should say that for, even for NP-complete problems, we don't expect an exponential
*  speed up from a quantum computer, you know, like once again, we can't prove that, you know, which
*  is no great surprise, you know, we can't even prove that P is different from N, right, we can't
*  even prove that classical computers can't solve these problems quickly, I mean, far less can we
*  prove that quantum computers can't do it, but what we generally think is that quantum computers
*  would give you more modest speed ups for these problems, okay, so after Shor's algorithm,
*  maybe the second most famous quantum algorithm is called Grover's algorithm, okay, it was discovered
*  just shortly afterward, Grover, by the way, was like, like, worked down the hall from Peter Shor
*  then at Bell Labs, so, you know, these ideas were in the air then, and I actually started in the field
*  doing a summer internship with Grover, okay, but what he discovered was that there is a quantum
*  algorithm that can search a list, any like list of N possibilities in only about the square root
*  of N steps, okay, where, you know, classically, if I just told you here are N boxes and inside one of
*  them is a golden nugget, well, you know, you're gonna, on average, you're gonna have to open about
*  N over two of the boxes until you find that nugget, right, there's just, you know, I've just sort of,
*  by fiat, I have told, you know, I have ruled out any other structure that you get to exploit here,
*  right, but what Grover showed is that if I can ask about every box in quantum superposition
*  and then, you know, take my superposition of answers, you know, do some quantum mechanical
*  transformation to it, what we call a unitary transformation, then ask another question and
*  so on and so on, then there is a way to get all or almost all of the amplitude onto the right answer,
*  that is, onto the box with the golden nugget in it by asking only about square root of N questions,
*  okay, so what this means is that, for example, if you had some combinatorial search problem,
*  say an NP-complete problem, if previously it would have taken you, let's say, two to the 100 steps
*  to solve with your classical computer, well, by layering Grover's algorithm on top of what you
*  were doing classically, typically you would be able to solve it in about two to the 50 steps
*  with a quantum computer, okay, and that's something, I mean, that will sort of expand the frontier
*  of, you know, the sizes of problems that you can handle and I think that absolutely would have
*  applications in a world with fully scalable, you know, and useful quantum computers,
*  it's not the exponential speed up that you get for factoring.
*  For anyone out there who knows a little bit of quantum mechanics,
*  studying and understanding Grover's algorithm is way easier than Shor's algorithm,
*  it's actually pretty straightforward. That is true, that is true, and actually the
*  reason for that is that Shor's algorithm, like, two-thirds of it is just classical number theory
*  that's got nothing to do with quantum mechanics, right, it's just getting it into the form where
*  you can then do something quantum, right, Grover's, you know, so I do teach all of these things in an
*  undergraduate course, you know, for which the only prerequisites are like linear algebra and some,
*  you know, classical, you know, programming or, you know, like, let's say a semester of classical
*  algorithms, you know, I teach all the quantum mechanics that we need for the class and we do
*  Shor's and Grover's algorithm, but typically, yeah, Shor's algorithm would be three lectures,
*  Grover's algorithm would be one lecture. And we should also plug your book on this.
*  Oh yeah, yeah, yeah, I do have a book, it's called Quantum Computing Since Democritus,
*  yeah, it was published seven years ago. It is not a popular book, it is also not a textbook,
*  it is in some, you know, intermediate complexity class in between. I don't know exactly what it is,
*  but, you know, when I wrote the prospectus for the publisher, I told them, well,
*  you know, kind of like the whatever audience is buying Penrose's books,
*  I'm hoping that they would also buy this book. Some subset thereof, yes. Yeah, yeah, yeah,
*  yeah, that's right. Okay, so obviously, there's a large terrain of questions about the reality
*  of quantum computing and things like that, but that's for lesser minds, we have other fish to
*  fry, I would like to start talking to you about the nature of space and time and stuff like that.
*  So, I mean, it's, again, maybe a little bit of a surprise that people, famous physicists like John
*  Preskill and Lenny Suskind, who grew up doing particle physics and quantum field theory and
*  cosmology have taken to quantum computing and quantum information in such a strong way. I mean,
*  why do you think that this set of ideas that started by, you know, how can we improve the
*  speed at which a computer can answer a certain kind of question suddenly seems to be everywhere
*  in discussions of the nature of space time itself? Yeah, well, okay. So, I mean, I have several
*  thoughts. The first one is, you know, you're the one asking me about the nature of space and time.
*  Yeah, but my second thought was, you know, the specific people you mentioned,
*  John Preskill, Eddie Farhi, we could add Ray LaFlamme, by the way, right? You know, these were
*  all people who started out in high energy physics, but then, you know, very early, so back in the
*  mid-90s, kind of switched to quantum computing and quantum information, you know, basically,
*  you know, after Shor's algorithm came along. And, you know, I mean, I know all of them, so,
*  you know, I've talked to them about what some of their reasons were. And I think mostly just it
*  was something that was new and exciting, and where, you know, the knowledge that they had,
*  you know, was relevant. It was not the only thing that was relevant, you know, computer science and,
*  you know, information also was, but, you know, these were people who knew quantum mechanics
*  really, really well. And, you know, high energy physics, I mean, it is a, you know, it is one of
*  the great pursuits of the human species. But, you know, if I'm advising a student, you know,
*  on what they should specialize in, and they don't really, really have their heart set on doing high
*  energy physics, well, you know, I mean, there is an immense amount of brain power, you know,
*  that is sort of being expended on, you know, not a huge set of questions on sort of a, you know,
*  a very, you know, narrow, you know, I will say a very tall and narrow tower of knowledge, right?
*  And, you know, and there was an, you know, unbelievable success over, you know, the course
*  of the 20th century in building up that tower, you know, and now that, you know, we're in this world
*  where, you know, the LHC has found the Higgs boson, it hasn't found anything else, you know,
*  you know, one could ask the question of, you know, is, you know, should we just continue trying to,
*  you know, add a millimeter to this tower, you know, sort of in the way that we knew, or should we,
*  you know, go down to the land and look for what else is being built somewhere else?
*  You know, there is no one right answer to these questions, right? There is an answer for each
*  individual to make for themselves, but, you know, but I think it is, you know, it is, you know,
*  quantum computing, especially in the 90s, was a field that was just full of low-hanging fruit,
*  and, you know, and I think really, you know, fundamental questions, right? I think that to
*  someone like Presko, right, it was clear that this is not just a technological question, right? This
*  is not just like an engineering design problem of build this quantum computer. This is a fundamental
*  question of, you know, does, is nature going to allow this at all, right? You know, can a scalable
*  quantum computer be built, or, you know, is this so ridiculous that, you know, we should just suppose
*  that there is something about quantum mechanics that we have not yet understood that is going to
*  prohibit, you know, getting an exponential computational speed up in this way, right?
*  Yeah, I mean, I think I understand, you know, I understand your point. In fact, I think you're
*  being diplomatic about it. I mean, as amazing as high energy physics is, and I'm a big fan myself,
*  it's a mature field that has slowed down a little bit, the rate of progress,
*  but I'm asking less about people who have switched from high energy to quantum computers,
*  versus people who like, the thing they want to understand is still why black holes evaporate
*  in a certain way. And they've decided that ideas from quantum information theory are relevant to
*  that somehow. Yes, right. Well, now that now that is a newer thing that has happened. And that's
*  actually right where I was headed next. Because, you know, you know, in the 90s, you know, you know,
*  people went into quantum computing. I mean, I went into it in the 90s, you know, and, you know,
*  did not expect that it was going to say anything about, you know, about string theory about, you
*  know, black holes about space time. I mean, maybe even then I secretly hoped it would, but I had no
*  basis for that. Yeah, right. And, and I would say that within the last eight or nine years,
*  you know, something really amazing has happened, which is that, you know, the, the, the, the, the,
*  the things really have circled back. And, you know, the people who talk about, you know, the
*  quantum gravity these days about, you know, the black hole information problem, and, you know,
*  about the ADS CFT. So, you know, about a sort of holographic space time. You know, at least the
*  ones who I talked to, they are talking about it largely in a language of qubits and, you know,
*  qubits, you know, quantum circuits acting on those qubits and entanglement, you know, and the, the
*  entanglement structure of the quantum states that you get. And, you know, even, even complexity,
*  the, the complexity of doing various tasks to these qubits. And this has been an amazing
*  development for me because I'm like, well, now I can actually talk to you about this stuff.
*  Yeah.
*  You know, this is, this is a language that, you know, I, you know, I can, I can, I can parse
*  at least half of what you're saying now. Right. And I mean, you know, I mean, if you look at the
*  list of talks of the strings conference, right, in recent years, I mean, it is quite remarkable
*  to an outsider like me, you know, how much of it is not explicitly about strings at all.
*  Right. But is about sort of ideas that are just as much quantum information. So, you know, if I had
*  to speculate, I mean, I mean, I mean, the, the, the way that this happened was sort of, you know,
*  it's sort of a long story. But you could say, you know, in some sense, it goes back to, to Hawking
*  in the seventies, you know, and, and Bekenstein, right. The story goes back to the black hole
*  information problem that said, you know, there is this fundamental conceptual problem about black
*  holes. And this problem is information theoretic in character in some sense, right? This, you know,
*  the, the problem is, you know, explain how information can come out of a black hole,
*  you know, as it needs to do in order for the evolution of a black hole to be unitary,
*  that is, you know, to be fully compatible with quantum mechanics as we understand it. And
*  it was, you know, thinking about matters like those that, you know, people in the seventies
*  and eighties were led to the realization that a black hole has an entropy. Not only does it
*  have an entropy, but it has sort of the largest entropy of any object in the universe of a similar
*  size. Okay. You know, you could say a black hole is sort of the highest density hard disk that is
*  allowed by the laws of physics, right? Specifically, it stores about 10 to the 69 bits or rather 10 to
*  the 69 qubits per square meter of surface area of its event horizon. I mean, you know, roughly one.
*  They're in their highest entropy state. So it's not a very useful hard disk.
*  That's right. That's right. So it's, well, you know, it's really not great for retrieving the bits.
*  That's the other problem with it. You know, I mean, you know, you'd have to wait for these bits to
*  fizzle out and hawking radiation, which, you know, might take 10 to the 70th years or something like
*  that. And then, you know, and then they'd be in some completely scrambled form. So, you know,
*  so it's not a very useful hard disk, but, you know, like even just purely in a by the lights of
*  like information theory or computer science, black holes are interesting, right? Black holes
*  are an extremal object. And so, you know, these were realizations that people started to have in
*  the 70s and 80s. You know, I would say it was not really connected yet to computer science. I mean,
*  it was certainly something that enormously intrigued me. You know, even in like 2002,
*  2003, you know, I talked to Raphael Busso at that time. You know, I talked to Juan Maldicena.
*  Maldicena was like joking with me about it, you know, a couple of years ago. I go, yeah,
*  you were this crazy kid who was saying that like complexity was somehow going to be relevant for
*  quantum gravity. I was trying to be polite to you, but, you know,
*  yeah, but, you know, I would say that what really made it click, what really sort of made this
*  connection happen in a deep way, a lot of it started in 2012, which is when there was this now
*  famous paper, the Amps paper, you know, Almhery, Marov, Polchinski and Sully that pointed out this
*  thing called the firewall paradox. Okay. And, you know, this was, well, it's a long story,
*  this firewall paradox. Okay. But basically, you know, you can, you know, if you're worried about
*  how information can come out of a black hole, you're sort of led from there to the idea that,
*  well, you know, the information, it couldn't have gotten out from the singularity. And, you know,
*  so like really what you would like for it to have happen is that it's sort of just fizzling off from
*  the, you know, on or very near the event horizon. Right. And in fact, if you're an observer outside
*  of a black hole, well, you never even see anything fall into the black hole in the first place.
*  Right. You just see it get slower and slower and, you know, pancaked over the event horizon and
*  scrambled there. And so, so an observer who's outside of a black hole ought to have a description
*  of what's going on where all the bits of information that are dropped into the black hole
*  are just sort of pancaked on its horizon, scrambled on the event horizon, and then come off from there.
*  And yet, an observer who falls into the black hole has to have a completely different picture
*  of the same physics. Right. For them, they have to see that the information really has fallen in
*  and that there is an interior of the black hole, you know, in the middle of which is a singularity.
*  And so then these two completely different sounding descriptions have to be somehow dual to each other.
*  Right. They have to be two different ways of describing the same thing. So then that leads
*  in the 90s to this, you know, idea of the holographic principle that you can have
*  different physical theories with different numbers of spatial dimensions, but that are somehow,
*  somehow one is just an encoding of the other one. So, you know, you can encode everything that
*  happens in a given region of space by some hologram that lives on the boundary of that region.
*  And then, you know, people were, you know, I wouldn't say like 100% satisfied by all of this,
*  but, you know, they thought they had kind of the broad outlines of a solution to the black hole
*  information problem. And then basically in 2012, this Amps paper came along and it broke everything
*  again. It said that, you know, if you, you know, write down certain postulates that seem like they
*  should be clearly true, like an observer who was falling into a black hole, you know, notices
*  nothing special as they cross the event horizon. And, you know, black holes, you know, from the
*  outside observer's perspective, they quickly scramble information, you know, and a few other
*  postulates, then you could write down an experiment, you know, that like in principle,
*  some observer who was outside of a black hole could do. So here's how the experiment would work.
*  Let's say you're Alice, right? So you drop some stuff into a black hole, you keep track of its
*  exact quantum state with some super duper powerful quantum computer, right? And now you
*  wait for the black hole to mostly but not completely evaporate. Okay, you know, for a black
*  hole, the, you know, the mass of a star, this might take 10 to the 67 years, you know, we assume that
*  you have a really long grant, okay? You collect all of the photons of Hawking radiation that come out
*  of the black hole, you route them all into your quantum computer for analysis, then you do a
*  certain measurement on those photons that proves that they are that they were not in a completely
*  thermal state. In other words, you know, what, you know, and one can argue that once the black hole
*  has more than 50% evaporated, then something special happens, where you can actually detect
*  very subtle correlations in the Hawking radiation that shows that, you know, they were, you know,
*  they actually do encode the information that fell in to create the black hole.
*  Yeah, sorry, just so you're clear about this, the phrase, the phrase, the phrase not completely in
*  a thermal state in this, in this sentence that you just said, means that it's not completely random
*  that there is some information encoded there that is related to what fell in.
*  Precisely, precisely, you detect some correlation with the stuff that fell in. And again, this is
*  something that in principle, you can do after the black hole has more than halfway evaporated.
*  Yeah, okay.
*  And then having done that, you then immediately jump into the black hole,
*  and you see what's on the other side. And now for reasons of quantum field theory that, you know,
*  I don't, well, you know, I don't, you know, I'm A, not expert on, and B, not sure if we have time
*  to go into. But because of the correlations that you saw outside of the black hole, you now, you
*  know, you either, you know, see a complete breakdown of the rules of quantum mechanics, as you, right
*  as you cross the event horizon, or else, if you know, you want quantum mechanics to still work,
*  then you have to see a wall of ultra high energy photons that are so high energy that you just
*  disintegrate as soon as you hit the event horizon. This is what is called the famous firewall.
*  And of course, no one has actually ever fallen into a black hole. But we, this is one of the
*  times where physicists have a strong belief that we have no empirical justification for, namely that
*  nothing special happens when you cross the black holes of enterizing.
*  That's right. That's right. And you know, and like in some sense, you know, you could take the
*  position that just, you know, what happens in a black hole stays in a black hole, right? It could
*  be any, you know, it could be that like, like in that movie Interstellar, that, you know, you meet
*  your long lost relatives or something, right? You know, you know, and, and, you know, this would,
*  you know, just like beliefs about the afterlife, this would have no consequences that at least we
*  could publish journal papers about here on earth, right? Because, you know, everything is just inside
*  the black hole. Okay. But, you know, physicists, I think very understandably, you know, have,
*  have high aspirations, right? They would like to describe even regions of the universe from which
*  we can never receive a signal. Okay. And, you know, at least classical general relativity, you know,
*  paints this very nice picture where you sail right past the event horizon and nothing very special
*  seems to happen. Now, to be clear, you know, you do die, you know, after you jump into a black hole,
*  but you're only supposed to die when you hit the singularity, right? You're not supposed to, you
*  know, so, you know, you're supposed to have like another second or whatever after you've crossed the
*  event horizon, right? You're not supposed to die right at the event horizon. But this firewall paper
*  was saying, well, from these assumptions, it appears that you would. And, you know, and this
*  was not just some, some, you know, completely, you know, formal question about, say, the structure of
*  the state space, right? What I liked about it is what they said here, very explicitly, here is the
*  experiment that would lead to the problem, right? And, you know, okay, fine, it's not an experiment
*  that maybe we could ever practically carry out within the lifetime of the universe, but nevertheless,
*  here is the experiment. And if you claim to understand this, then you have to be able to say
*  what happens if someone did that experiment, right? And, and this was, I would say that this was
*  really the watershed thing that brought quantum information ideas into quantum gravity, you know,
*  in a really deep way. And in particular, you know, a year later, my friends, Daniel Harlow and Patrick
*  Hayden wrote an amazing paper about the firewall paradox, where they said, well, you know, it might
*  be true that if you do this crazy experiment, you know, that, you know, and then try to jump into a
*  black hole to see what happened that you would experience a firewall, but how hard would it be
*  to do that experiment? And they gave evidence that to actually do the quantum computation
*  on the Hawking radiation that would detect those correlations, so detect that it's not in completely
*  a thermal state, would require a quantum computation that, you know, that would use a number of steps
*  that is exponential in the size of the black hole, meaning in the number of qubits of the black hole.
*  So in other words, we'd be talking about a problem that would take your quantum computer,
*  not a mere 10 to the 67 years to solve, right? That is, that is, but by our new standard, that's
*  going to be easy, okay? 10 to the 67 years is an easy problem, okay? But this would be a hard problem,
*  meaning one that takes two to the 10 to the 67 years to solve. So it's really a very nice example
*  because it takes us back to the sort of realization post-touring that the question is not just the
*  distinction between solvable and unsolvable, but how long it takes to solve things. And so
*  once you appreciate that, you know, you might have some really strong beliefs in something,
*  but if those beliefs could in principle be violated, but only by things that would take
*  way, way, way longer than the age of the universe to happen, maybe you're not bothered so much.
*  And that's exactly what complexity theory is all about. Exactly. Now, this is, you know,
*  this is somewhat controversial, right? So I mean, some people said, well, who cares if the computation
*  takes this, you know, huge amount of time? That's merely a practical issue, right? But as Harlow
*  and Hayden pointed out, one thing that it means is that you could not have made a dent in this
*  computation before the black hole would have long ago evaporated anyway. Yeah. Right. Which means
*  that then there's nothing to jump into, which means that maybe then there's no paradox, right?
*  And, you know, you could think about, well, what if you did it for a really, really tiny black hole
*  for which, you know, this exponential scaling wouldn't matter, but for a really, really tiny
*  black hole, we didn't really expect classical general relativity and quantum field theory to
*  work well anyway, right? So, you know, I think it is plausible that that sort of, you know, the,
*  you know, like, you know, I think, okay, well, let me put it this way. You know, if someone said,
*  it's okay for there to be a contradiction in the laws of physics, as long as it takes exponential
*  time to discover it, I would not agree with that, right? I would say that that sounds like nonsense.
*  Okay. But that's not what Harlow and Hayden were saying. Okay. They were saying something more
*  subtle, that, you know, there are contradictions in the effective theories that we, you know,
*  normally work, but that we know have to ultimately be superseded by a quantum theory of gravity,
*  right? And it might be that some of these, you know, problems with effective field theories,
*  you would find them not by going to an enormously high energy or to an enormously tiny distance,
*  but by going to a regime of extreme computational complexity. Okay. But, you know, if it would take
*  an exponential computation to uncover the breakdown of effective field theory, then, you know, we have,
*  we do have a reason, you know, for sort of trusting our effective field theory in,
*  quote unquote, normal situations. Yeah. And I don't think sadly, we don't have time to go into
*  into the details. But I think that since then, since that watershed moment, there's really been
*  this wonderful importing of all sorts of ideas from quantum information and just sort of theoretical
*  computer science. I mean, I know, even I've written papers involving things like quantum circuits and
*  tensor networks and stuff like that. And it's really really big, a mature field. I know. Yeah.
*  Right. So then, I mean, I mean, I mean, I'm Lenny Susskind, you know, became sort of a,
*  a sort of prophet of this movement, right? And, you know, as he as he's often a prophet for
*  whatever he believes in at the given moment, right? But, you know, I would say he became far
*  more gung ho than I am about, you know, complexity is the future of physics. You know, I was the one
*  saying, like, you know, slow down, you know, I wouldn't go that far, right. But, you know,
*  the connection has gone a lot further now, like in this, this ADS CFT correspondence,
*  where you literally use circuit complexity as sort of the thing that is holographically dual
*  to some geometric quantity, like the volume of a wormhole, you know, and that might not that that
*  might be because, you know, Lenny thinks that it's because circuit complexity really does have
*  fundamental importance in physics, you know, just like entropy or like energy, I'm not willing to go
*  as far as he does there. But I say that, you know, nevertheless, it is the best placeholder that
*  anyone can come up with, you know, whatever quantity really is dual to these volumes of
*  wormholes and things like that. It is great stuff. It's right there on the cutting edge. And
*  I think we're gonna have to end because the other topics I wanted to talk about include words like
*  free will and consciousness. And I can't imagine that we would get anything interesting said in
*  less than an hour each. So we'll save that for a future episode. And let people let people absorb
*  the complexity and quantumness of what we already talked about. Awesome. If you invite me for a
*  podcast about free will, I will I will choose to participate. So you say this is the universe that
*  gets to decide. All right, Scott Anderson, thanks for being on the mindscape. All right.
*  Thanks a lot, Sean. Pleasure as always.

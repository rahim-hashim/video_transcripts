---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 7652s
Video Keywords: ['richard karp', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 143015
Video Rating: None
Video Description: Richard Karp is a professor at Berkeley and one of the key figures in the history of theoretical computer science. In 1985, he received the Turing Award for his research in the theory of algorithms, including the development of the Edmonds–Karp algorithm for solving the maximum flow problem on networks, Hopcroft–Karp algorithm for finding maximum cardinality matchings in bipartite graphs, and his landmark paper in complexity theory called "Reducibility Among Combinatorial Problems", in which he proved 21 problems to be NP-complete. This paper was probably the most important catalyst in the explosion of interest in the study of NP-completeness and the P vs NP problem.

Support this podcast by signing up with these sponsors:
- Eight Sleep: https://eightsleep.com/lex
- Cash App - use code "LexPodcast" and download:
- Cash App (App Store): https://apple.co/2sPrUHe
- Cash App (Google Play): https://bit.ly/2MlvP5w

EPISODE LINKS:
Richard's wikipedia: https://en.wikipedia.org/wiki/Richard_M._Karp

PODCAST INFO:
Podcast website:
https://lexfridman.com/podcast
Apple Podcasts:
https://apple.co/2lwqZIr
Spotify:
https://spoti.fi/2nEwCF8
RSS:
https://lexfridman.com/feed/podcast/
Full episodes playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

OUTLINE:
0:00 - Introduction
3:50 - Geometry
9:46 - Visualizing an algorithm
13:00 - A beautiful algorithm
18:06 - Don Knuth and geeks
22:06 - Early days of computers
25:53 - Turing Test
30:05 - Consciousness
33:22 - Combinatorial algorithms
37:42 - Edmonds-Karp algorithm
40:22 - Algorithmic complexity
50:25 - P=NP
54:25 - NP-Complete problems
1:10:29 - Proving P=NP
1:12:57 - Stable marriage problem
1:20:32 - Randomized algorithms
1:33:23 - Can a hard problem be easy in practice?
1:43:57 - Open problems in theoretical computer science
1:46:21 - A strange idea in complexity theory
1:50:49 - Machine learning
1:56:26 - Bioinformatics
2:00:37 - Memory of Richard's father

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Richard Karp Algorithms and Computational Complexity  Lex Fridman Podcast #111
**Lex Fridman:** [July 26, 2020](https://www.youtube.com/watch?v=KllCrlfLuzs)
*  The following is a conversation with Richard Karp, a professor at Berkeley and one of the most
*  important figures in the history of theoretical computer science. In 1985, he received the Turing
*  Award for his research in the theory of algorithms, including the development of the Admirant's Karp
*  algorithm for solving the max-flow problem on networks, Hopcroft's Karp algorithm for finding
*  maximum cardinality matchings in bipartite graphs, and his landmark paper in complexity
*  theory called Reducability Among Combinatorial Problems, in which he proved 21 problems to be
*  NP-complete. This paper was probably the most important catalyst in the explosion of interest
*  in the study of NP-completeness and the P versus NP problem in general.
*  Quick summary of the ads. Two sponsors, 8 Sleep Mattress and Cash App. Please consider
*  supporting this podcast by going to asleep.com slash Lex and downloading Cash App and using
*  code LexPodcast. Click the links, buy the stuff. It really is the best way to support this podcast.
*  If you enjoy this thing, subscribe on YouTube, review it with 5 stars on our podcast,
*  support it on Patreon, or connect with me on Twitter at Lex Friedman. As usual, I'll do a
*  few minutes of ads now and never any ads in the middle that can break the flow of the conversation.
*  This show is sponsored by 8 Sleep and its Pod Pro mattress that you can check out at
*  8sleep.com slash Lex to get $200 off. It controls temperature with an app. It can cool down to as
*  low as 55 degrees on each side of the bed separately. Research shows that temperature has a big impact
*  on the quality of our sleep. Anecdotally, it's been a game changer for me. I love it. It's been a
*  couple of weeks now. I've just been really enjoying it, both in the fact that I'm getting
*  better sleep and that it's a smart mattress, essentially. I kind of imagine this being the
*  early days of artificial intelligence being a part of every aspect of our lives and certainly
*  infusing AI in one of the most important aspects of life, which is sleep, I think has a lot of
*  potential for being beneficial. The Pod Pro is packed with sensors that track heart rate,
*  heart rate variability, and respiratory rate, showing it all in their app. The app's health
*  metrics are amazing, but the cooling alone is honestly worth the money. I don't always sleep,
*  but when I do, I choose the 8 Sleep Pod Pro mattress. Check it out at 8sleep.com slash Lex
*  to get $200 off. And remember, just visiting the site and considering the purchase
*  helps convince the folks at 8 Sleep that this silly old podcast is worth sponsoring in the future.
*  This show is also presented by the great and powerful Cash App, the number one finance app
*  in the app store. When you get it, use code LexPodcast. Cash App lets you send money to
*  friends, buy Bitcoin, and invest in the stock market with as little as $1. It's one of the
*  best designed interfaces of an app that I've ever used. To me, good design is when everything is
*  easy and natural. Bad design is when the app gets in the way, either because it's buggy
*  or because it tries too hard to be helpful. I'm looking at you Clippy from Microsoft,
*  even though I love you. Anyway, there's a big part of my brain and heart that loves to design things
*  and also to appreciate great design by others. So again, if you get Cash App from the app store
*  Google Play and use the code LexPodcast, you get $10. Cash App will also donate $10 to First,
*  an organization that is helping to advance robotics and STEM education for young people
*  around the world. And now here's my conversation with Richard Karp. You wrote that at the age of
*  13, you were first exposed to plain geometry and was wonder struck by the power and elegance of
*  form of proofs. Are there problems, proofs, properties, ideas in plain geometry that from
*  that time that you remember being mesmerized by or just enjoying to go through to prove
*  various aspects? So Michael Rabin told me this story
*  about an experience he had when he was a young student who was tossed out of his classroom
*  for bad behavior and was wandering through the corridors of his school
*  and came upon two older students who were studying the problem of finding the shortest
*  distance between two non-overlapping circles. And Michael thought about it and said,
*  you take the straight line between the two centers and the segment between the two circles is the
*  shortest because a straight line is the shortest distance between the two centers
*  and any other line connecting the circles would be on a longer line. And I thought,
*  and he thought, and I agreed that this was just elegant, the pure reasoning could come up with
*  such a result. Certainly the shortest distance from the two centers of the circles
*  is a straight line. Could you once again say what's the next step in that proof?
*  Well, any segment joining the two circles, if you extend it by taking the radius on each side,
*  you get a segment with a path with three edges which connects the two centers.
*  And this has to be at least as long as the shortest path, which is the straight line.
*  The straight line. Yeah. Wow. Yeah. That is, that's quite simple. So what is it about that elegance
*  that you just find compelling? Well, just that you could establish a fact about geometry beyond
*  dispute by pure reasoning. I also enjoy the challenge of solving puzzles in plain geometry.
*  It was much more fun than the earlier mathematics courses, which were mostly about
*  arithmetic operations and manipulating them. Was there something about geometry itself,
*  the slightly visual component of it? Oh, yes. Absolutely. Although
*  I lacked three-dimensional vision. I wasn't very good at three-dimensional vision.
*  You mean being able to visualize three-dimensional objects.
*  Three-dimensional objects or surfaces, hyperplanes and so on. So there I didn't have an intuition,
*  but for example, the fact that the sum of the angles of a triangle is 180 degrees
*  is proved convincingly. And it comes as a surprise that that can be done.
*  Why is that surprising? Well, it is a surprising idea, I suppose. Why does that prove difficult?
*  It's not. That's the point. It's so easy and yet it's so convincing.
*  Do you remember what is the proof that it adds up to 180?
*  You start at a corner and draw a line parallel to the opposite side.
*  And that line sort of trisects the angle between the other two sides. And you get a half plane,
*  which has to add up to 180 degrees. And the angles by the equality of alternate angles,
*  what's it called? You get a correspondence between the angles created along the side of the
*  triangle and the three angles of the triangle.
*  Has geometry had an impact on when you look into the future of your work with combinatorial
*  algorithms? Has it had some kind of impact in terms of the puzzles, the visual aspects
*  that were first so compelling to you? Not Euclidean geometry particularly. I think
*  I use tools like linear programming and integer programming a lot. But those require
*  high dimensional visualization. And so I tend to go by the algebraic properties.
*  Right. You go by the linear algebra and not by the visualization.
*  Well, the interpretation in terms of, for example, finding the highest point on a polyhedron,
*  as in linear programming, is motivating. But again, I don't have the high dimensional intuition
*  that would particularly inform me. So I sort of lean on the algebra.
*  So to linger on that point, what kind of visualization
*  do you do when you're trying to think about, well, get to combinatorial algorithms,
*  but just algorithms in general? What's inside your mind when you're thinking about designing
*  algorithms? Or even just tackling any mathematical problem?
*  Well, I think that usually an algorithm involves a repetition of some inner loop. And so I can sort
*  of visualize the distance from the desired solution as iteratively reducing until you
*  finally hit the exact solution. And try to take steps that get you closer to the...
*  Try to take steps that get closer and having the certainty of converging. So it's basically the
*  mechanics of the algorithm is often very simple. But especially when you're trying something out
*  on the computer. So for example, I did some work on the traveling salesman problem. And
*  I could see there was a particular function that had to be minimized. And it was fascinating to
*  see these successive approaches to the optimum. You mean, so first of all, traveling salesman
*  problem is where you have to visit every city without ever... The only ones. Yeah, that's right.
*  Find the shortest path through a set of cities. Yeah. Which is sort of a canonical, a standard,
*  a really nice problem that's really hard. Right. Exactly. So can you say again, what was nice about
*  being able to think about the objective function there and maximizing it or minimizing it?
*  Well, just that as the algorithm proceeded, you were making progress, continual progress,
*  and eventually getting to the optimum point. So there's two parts, maybe. Maybe you can
*  correct me. But first is getting an intuition about what the solution would look like.
*  And, or even maybe coming up with a solution. And two is proving that this thing is
*  actually going to be pretty good. What part is harder for you? Where does the magic happen?
*  Is it in the first sets of intuitions or is it in the detail, the messy details of actually showing
*  that it is going to get to the exact solution and it's going to run at a certain complexity?
*  Well, the magic is just the fact that the gap from the optimum decreases monotonically and you can
*  see it happening. And various metrics of what's going on are improving all along until finally
*  you hit the optimum. Perhaps later we'll talk about the assignment problem and I can illustrate.
*  Illustrate a little better. Now zooming out again, as you write, Don Knuth has called attention to a
*  breed of people who derive great aesthetic pleasure from contemplating the structure of
*  computational processes. So Don calls these folks geeks. And you write that you remember the moment
*  you realized you were such a person, you were shown the Hungarian algorithm to solve the
*  assignment problem. So perhaps you can explain what the assignment problem is and what the
*  Hungarian algorithm is. So in the assignment problem you have N boys and N girls and you are
*  given the desirability of or the cost of matching the i-th boy with the j-th girl for all i and j.
*  You're given a matrix of numbers and you want to find the one-to-one matching of the boys with the
*  girls such that the sum of the associated costs will be minimized. So the best way to match the
*  boys with the girls or men with jobs or any two sets. Any possible matching is possible?
*  Or yeah all one-to-one correspondences are permissible. If there is a connection that
*  is not allowed then you can think of it as having an infinite cost.
*  So what you do is to depend on the observation that the identity of the optimal assignment
*  or as we call it the optimal permutation is not changed if you subtract
*  a constant from any row or column of the matrix. You can see that the comparison
*  between the different assignments is not changed by that. Because your penile,
*  if you decrease a particular row all the elements of a row by some constant all solutions decrease
*  by the cost of that by an amount equal to that constant. So the idea of the algorithm is to
*  start with a matrix of non-negative numbers and keep subtracting from rows or entire columns
*  in such a way that you subtract the same constant from all the elements of that row or column
*  while maintaining the property that all the elements are non-negative.
*  Simple.
*  Yeah and so what you have to do is find small moves which will decrease the total cost
*  while subtracting constants from rows or columns and there's a particular way of doing that by
*  computing the kind of shortest path through the elements in the matrix. And you just keep going
*  in this way until you finally get a full permutation of zeros while the matrix is
*  non-negative and then you know that that has to be the cheapest.
*  Is that as simple as it sounds?
*  So the shortest path through the matrix part.
*  Yeah the simplicity lies in how you find the what I oversimplified slightly what you
*  you will end up subtracting a constant from some rows or columns and adding the same constant back
*  to other rows and columns so as not to reduce any of the zero elements. You leave them unchanged
*  but each individual step modifies several rows and columns by the same amount but overall decreases
*  the cost.
*  So there's something about that elegance that made you go, aha this is a beautiful like it's
*  amazing that something like this something so simple can solve a problem like this.
*  Yeah it's really cool. If I had mechanical ability I would probably like to do woodworking or
*  other activities where you sort of shape something into something beautiful and orderly and
*  something about the orderly systematic nature of that iterative algorithm.
*  So what do you think about this idea of geeks as Don Knuth calls them?
*  What do you think of is it something specific to a mindset that allows you to
*  discover the elegance in computational processes or is this all of us?
*  Can all of us discover this beauty? Were you born this way?
*  I think so. I always like to play the game of the game.
*  I used to amuse myself by multiplying four digit decimal numbers in my head and putting myself to
*  sleep by starting with one and doubling the number as long as I could go and testing my memory,
*  my ability to retain the information.
*  And I also read somewhere that you wrote that you enjoyed showing off to your friends by
*  I believe multiplying four digit numbers. Right.
*  A couple of four digit numbers. Yeah I had a summer job at a beach resort outside of Boston
*  and I was the barker at a skeeball game. I used to sit at a microphone saying
*  come one, come all, come in and play skeeball, five cents to play, nickel to win and so on.
*  That's what a barker, I wasn't sure if I should know but barker, you're the
*  charming outgoing person that's getting people to come in.
*  Well I wasn't particularly charming but I could be very repetitious and loud.
*  The other employees were sort of juvenile delinquents who had no academic bent but somehow
*  I found that I could impress them by performing this mental arithmetic.
*  You know there's something to that, some of the most popular videos on the internet
*  is there's a YouTube channel called Numberphile that shows off different mathematical ideas.
*  There's still something really profoundly interesting to people about math, the beauty of
*  it. Something even if they don't understand the basic concept even being discussed, there's
*  something compelling to it. What do you think that is? Any lessons you drew from the early
*  teen years where you were showing off to your friends with the numbers? What is it that attracts
*  us to the beauty of mathematics do you think? The general population, not just the computer
*  scientists and mathematicians. I think that you can do amazing things. You can test whether
*  large numbers are prime. You can solve little puzzles about cannibals and missionaries.
*  There's a kind of achievement, it's puzzle solving. At a higher level the fact that you can
*  do this reasoning, that you can prove in an absolutely ironclad way that some of the
*  angles of the triangle is 180 degrees. Yeah, it's a nice escape from the messiness of the real world
*  where nothing can be proved. We'll talk about it but sometimes the ability to map the real
*  world into such problems where you can't prove it is a powerful step. It's amazing that we can do it.
*  Of course another attribute of geeks is they're not necessarily end out with emotional intelligence.
*  It's so they can live in a world of abstractions without having to
*  master the complexities of dealing with people.
*  Just to link on the historical note, as a PhD student in 1955 you joined the computational lab
*  at Harvard where Howard Aiken had built the Mark I and the Mark IV computers.
*  Just to take a step back into that history, what were those computers like?
*  The Mark IV filled a large room, much bigger than this large office that we're talking in now.
*  You could walk around inside it. There were rows of relays. You could just walk around the interior
*  and the machine would sometimes fail because of bugs, which literally meant
*  flying creatures landing on the switches. I never used that machine for any practical purpose.
*  The lab eventually acquired one of the earlier commercial computers.
*  This was already in the 60s?
*  No, in the mid-50s.
*  Late 50s.
*  There were already commercial computers in the...
*  Yeah, we had a UNIVAC with 2,000 words of storage. You had to work hard to allocate the
*  memory properly. Also, the access time from one word to another depended on the
*  number of the particular words. There was an art to arranging the storage allocation to
*  make fetching data rapid.
*  Were you attracted to this actual physical world implementation of mathematics?
*  Is it a mathematical machine that's actually doing the math physically?
*  No, not at all. I was attracted to the underlying algorithms.
*  Did you draw any inspiration? What did you imagine was the future of these giant computers?
*  Could you imagine that 60 years later, we'd have billions of these computers all over the world?
*  I couldn't imagine that, but there was a sense in the laboratory that this was the wave of the
*  future. In fact, my mother influenced me. She told me that data processing was going to be really
*  big and I should get into it.
*  She's a smart woman.
*  Yeah, she was a smart woman. There was just a feeling that this was going to change the world,
*  but I didn't think of it in terms of personal computing. I had no anticipation that we would
*  be walking around with computers in our pockets or anything like that.
*  Did you see computers as tools, as mathematical mechanisms to analyze theoretical computer science,
*  or as the AI folks, which is an entire other community of dreamers, as something that could
*  one day have human-level intelligence?
*  Well, AI wasn't very much on my radar. I did read Turing's paper about the...
*  The Turing test computing and intelligence?
*  Yeah, the Turing test.
*  What did you think about that paper? Was that just like science fiction?
*  I thought that it wasn't a very good test because it was too subjective.
*  I didn't feel that the Turing test was really the right way to calibrate how intelligent
*  an algorithm could be.
*  To linger on that, do you think it's part... Because you've come up with some incredible
*  tests later on, tests on algorithms, right? That are strong, reliable, robust across
*  a bunch of different classes of algorithms. But returning to this emotional mess that is
*  intelligence, do you think it's possible to come up with a test that's as ironclad as
*  some of the computational complexity work?
*  Well, I think the greater question is whether it's possible to achieve human-level intelligence.
*  Right. First of all, let me... At the philosophical level, do you think it's possible to create
*  algorithms that reason and would seem to us to have the same kind of intelligence as human beings?
*  It's an open question. It seems to me that most of the achievements have
*  to operate within a very limited set of ground rules and for a very limited, precise task,
*  which is a quite different situation from the processes that go on in the minds of humans,
*  which... Where they have to sort of function in changing environments. They have emotions, they
*  have physical attributes for exploring their environment. They have intuition, they have
*  desires, emotions, and I don't see anything in the current achievements of what's called
*  AI that come close to that capability. I don't think there's any
*  computer program which surpasses a six-month-old child in terms of comprehension of the world.
*  Do you think this complexity of human intelligence, all the cognitive abilities we have,
*  all the emotion, do you think that could be reduced one day or just fundamentally,
*  can it be reduced to a set of algorithms or an algorithm? Can a Turing machine
*  achieve human-level intelligence? I am doubtful about that. I guess the argument in favor of it
*  is that the human brain seems to achieve
*  what we call intelligence, cognitive abilities of different kinds.
*  If you buy the premise that the human brain is just an enormous interconnected set of switches,
*  so to speak, then in principle, you should be able to diagnose what that interconnection
*  structure is like, characterize the individual switches, and build a simulation outside.
*  But while that may be true in principle, that cannot be the way we're eventually going to
*  tackle this problem. That does not seem like a feasible way to go about it.
*  So there is, however, an existence proof that
*  if you believe that the brain is just a network of neurons operating by rules,
*  I guess you could say that that's an existence proof of the ability to build
*  the capabilities of a mechanism. But it would be almost impossible to acquire the information
*  unless we got enough insight into the operation of the brain.
*  There's so much mystery there. What do you make of consciousness, for example?
*  As an example, something we completely have no clue about, the fact that we have this subjective
*  experience. Is it possible that this network of this circuit of switches is able to create
*  something like consciousness? To know its own identity.
*  Yeah, to know the algorithm, to know itself.
*  To know itself. I think if you try to define that rigorously, you'd have a lot of trouble.
*  So I know that there are many who believe that general intelligence can be achieved,
*  and there are even some who feel certain that the singularity will come and we will be surpassed
*  by the machines, which will then learn more and more about themselves and reduce humans to an
*  inferior breed. I am doubtful that this will ever be achieved. Just for the fun of it,
*  could you linger on what's your intuition, why you're doubtful? So there are quite a few people
*  that are extremely worried about this existential threat of artificial intelligence, of us being
*  left behind by this super intelligent new species. What's your intuition why that's not quite
*  likely? Just because none of the achievements in speech or robotics or
*  natural language processing or creation of flexible computer assistants or any of that comes
*  anywhere near close to that level of cognition. What do you think about ideas as sort of, if we
*  look at Moore's law, and exponential improvement to allow us to, that would surprise us.
*  Sort of our intuition fall apart with exponential improvement because, I mean, we're not able to
*  kind of think in linear improvement. We're not able to imagine a world that goes from the
*  Mark I computer to an iPhone X. So do you think we could be really surprised by the exponential growth?
*  Or on the flip side, is it possible that also intelligence is actually way, way, way, way harder,
*  even with exponential improvement, to be able to crack? I don't think any constant factor improvement
*  could change things. Given our current comprehension of what cognition requires, it seems to me that
*  it seems to me that multiplying the speed of the switches by a factor of a thousand or a million
*  will not be useful until we really understand the organizational principle behind
*  the network of switches. Well, let's jump into the network of switches and talk about combinatorial
*  algorithms, if we could. Let's step back for the very basics. What are combinatorial algorithms?
*  What are some major examples of problems they aim to solve? A combinatorial algorithm is one which
*  deals with a system of discrete objects that can occupy various states or take on various
*  values from a discrete set of values and need to be arranged or
*  selected in such a way as to achieve some, to minimize some cost function,
*  or to prove the existence of some combinatorial configuration. So an example would be
*  coloring the vertices of a graph. What's a graph? Let's step back. It's fun to ask one of the
*  greatest computer scientists of all time the most basic questions in the beginning of most books.
*  But for people who might not know, but in general, how you think about it, what is a graph?
*  A graph, that's simple. It's a set of points, certain pairs of which are joined by lines called
*  edges. And they sort of represent the, in different applications, represent the interconnections
*  between discrete objects. So they could be the interactions, interconnections between switches
*  in a digital circuit or interconnections indicating the communication patterns of
*  a human community. And they could be directed or undirected. And then, as you mentioned before,
*  might have costs. Right. They can be directed or undirected. You can think of them as, if you think,
*  if a graph were representing a communication network, then the edge could be undirected,
*  meaning that information could flow along it in both directions, or it could be directed with
*  only one way communication. A road system is another example of a graph with weights on the edges.
*  And then a lot of problems of optimizing the efficiency of such networks or learning about
*  the performance of such networks are the object of combinatorial algorithms. So it could be
*  scheduling classes at a school where the vertices, the nodes of the network are the individual
*  classes and the edges indicate the constraints, which say that certain classes cannot take place
*  at the same time or certain teachers are available only for certain classes, etc.
*  Or I talked earlier about the assignment problem of matching the boys with the girls,
*  where you have there a graph with an edge from each boy to each girl
*  with a weight indicating the cost. Or in logical design of computers, you might want to
*  find a set of so-called gates, switches that perform logical functions, which can be interconnected
*  to realize some function. So you might ask, how many gates do you need in order to
*  for a circuit to give a yes output if at least a given number of inputs are ones and no if not,
*  if fewer are present? My favorite is probably all the all the work with network flows. So anytime you
*  have, I don't know why it's so compelling, but there's something just beautiful about it. It
*  seems like there's so many outputs that you can get from a network. And I think that's
*  applications and communication networks and traffic flow that you can map into these.
*  And then you can think of pipes and water going through pipes and you can optimize it in different
*  ways. There's something always visually and intellectually compelling to me about it. And
*  of course, you've done work there. Yeah. So there, the edges represent channels along which
*  some commodity can flow. It might be gas, it might be water, it might be information.
*  It could be supply chain as well, like products being...
*  Products flowing from one operation to another. And the edges have a capacity,
*  which is the rate at which the commodity can flow. And a central problem is to determine,
*  given a network of these channels, in this case, the edges are communication channels.
*  The challenge is to find the maximum rate at which the information can flow along these channels to
*  get from a source to a destination. And that's a fundamental combinatorial problem that I've
*  worked on. Jointly with the scientist Jack Edmonds, we, I think, were the first to give
*  a formal proof that this maximum flow problem through a network can be solved in polynomial time.
*  Which I remember the first time I learned that, just learning that in maybe even grad school.
*  I don't think it was even undergrad. No. Algorithm, yeah. Do network flows get taught in
*  basic algorithms courses? Yes, probably.
*  Okay. So yeah, I remember being very surprised that max flow is a polynomial time algorithm.
*  Yeah. That there's a nice fast algorithm that solves max flow. But, so there is an algorithm
*  named after you and Edmonds, the Edmond Karp algorithm for max flow. So what was it like
*  tackling that problem and trying to arrive at a polynomial time solution?
*  And maybe you can describe the algorithm. Maybe you can describe what's the running time complexity
*  that you showed. Yeah. Well, first of all, what is a polynomial time algorithm? Perhaps we could
*  discuss that. So yeah, let's actually just even, yeah,
*  what is algorithmic complexity? What are the major classes of algorithm complexity?
*  So in a problem like the assignment problem or scheduling schools or any of these applications,
*  you have a set of input data, which might, for example, be
*  the set of vertices connected by edges with, you're given for each edge the capacity of the edge.
*  And you have algorithms which are, think of them as computer programs with operations such as
*  addition, subtraction, multiplication, division, comparison of numbers and so on. And you're trying
*  to construct an algorithm based on those operations, which will determine in a minimum
*  number of computational steps the answer to the problem. In this case, the computational step
*  is one of those operations. And the answer to the problem is, let's say, the
*  configuration of the network that carries the maximum amount of flow.
*  And an algorithm is said to run in polynomial time if, as a function of the size of the input,
*  the number of vertices, the number of edges and so on, the number of basic computational steps
*  grows only as some fixed power of that size. A linear algorithm would
*  execute a number of steps linearly proportional to the size. Quadratic algorithm would be steps
*  proportional to the square of the size and so on. And algorithms whose running time is bounded by
*  some fixed power of the size are called polynomial algorithms. And that's supposed to be a relatively
*  fast class of algorithms.
*  That's right. Theoreticians take that to be the definition of an algorithm being efficient. And
*  we're interested in which problems can be solved by such efficient algorithms. One can argue whether
*  that's the right definition of efficient because you could have an algorithm whose running time is
*  the 10,000th power of the size of the input and that wouldn't be really efficient.
*  And in practice, it's oftentimes reducing from an n squared algorithm to an n log n or linear time
*  is practically the jump that you want to make to allow a real world system to solve a problem.
*  Yeah, that's also true because especially as we get very large networks, the size can be
*  in the millions and then anything above n log n where n is the size would be too much for
*  practical solution.
*  Okay, so that's polynomial time algorithms. What other classes of algorithms are there?
*  So that usually they designate polynomials as the letter P. There's also NP, NP complete and NP hard.
*  Yeah.
*  So can you try to disentangle those by trying to define them simply?
*  Right. So a polynomial time algorithm is one whose running time is bounded by a polynomial
*  in the size of the input. Then the class of such algorithms is called P.
*  In the worst case, by the way, we should say, right?
*  Yeah.
*  So for every case of the problem.
*  And that's very important that in this theory, when we measure the complexity of an algorithm,
*  we really measure the number of steps, the growth of the number of steps in the worst case.
*  So you may have an algorithm that runs very rapidly in most cases, but if there's
*  any case where it gets into a very long computation, that would increase the
*  computational complexity by this measure. And that's a very important issue because there,
*  as we may discuss later, there are some very important algorithms which don't have a good
*  standing from the point of view of their worst case performance and yet are very effective.
*  So theoreticians are interested in P, the class of problem solvable in polynomial time.
*  Then there's NP, which is the class of problems which may be hard to solve, but where when
*  confronted with a solution, you can check it in polynomial time. Let me give you an example there.
*  So if we look at the assignment problem, so you have N boys, you have N girls,
*  the number of numbers that you need to write down to specify the problem instances, N squared,
*  and the question is how many steps are needed to solve it. And Jack Edmonds and I were the first
*  to show that it could be done in time N cubed. Earlier, algorithms like this were very, very
*  very fast. Earlier, algorithms required N to the fourth. So as a polynomial function of the size
*  of the input, this is a fast algorithm. Now, to illustrate the class NP, the question is how long
*  would it take to verify that a solution is optimal? So for example, if the input was a graph,
*  it would take a long time. So you would want to find the largest clique in the graph, or a clique
*  is a set of vertices such that any vertex, each vertex in the set is adjacent to each of the others.
*  So the clique is a complete subgraph. Yeah, so if it's a Facebook social network,
*  it's called a complete graph. It would be within that clique. Within that clique, yeah.
*  They're all friends. So a complete graph is when everybody is friends with everybody.
*  Yeah. So the problem might be to determine whether in a given graph there exists a clique
*  of a certain size. Now that turns out to be a very hard problem, but if somebody hands you a clique
*  and asks you to check whether it is, hands you a set of vertices and asks you to check whether
*  it's a clique, you could do that simply by exhaustively looking at all of the edges
*  between the vertices and the clique and verifying that they're all there.
*  And that's a polynomial time algorithm.
*  That's a polynomial. So the problem of finding the clique
*  appears to be extremely hard, but the problem of verifying a clique
*  to see if it reaches the target number of vertices is easy to verify. So finding the clique is hard,
*  checking it is easy. Problems of that nature are called non-deterministic polynomial time
*  algorithms, and that's the class NP. And what about NP complete and NP hard?
*  Okay. Let's talk about problems where you're getting a yes or no answer rather than a numerical
*  value. So either there is a perfect matching of the boys with the girls or there isn't.
*  It's clear that every problem in P is also in NP. If you can solve the problem exactly, then you
*  can certainly verify the solution. On the other hand, there are problems in the class NP.
*  This is the class of problems that are easy to check, although they may be hard to solve.
*  It's not at all clear that problems in NP lie in P. So for example, if we're looking at scheduling
*  classes at a school, the fact that you can verify when handed a schedule for the school,
*  whether it meets all the requirements, that doesn't mean that you can find the schedule rapidly.
*  So intuitively, NP, non-deterministic polynomial checking rather than finding,
*  is going to be harder than, is going to include, is easier. Checking is easier and therefore the
*  class of problems that can be checked appears to be much larger than the class of problems
*  that can be solved. And then you keep adding appears to and sort of the, the, the, the
*  these additional words that designate that we don't know for sure yet.
*  We don't know for sure. So the theoretical question, which is considered to be the
*  most central problem in theoretical computer science, or at least computational complexity theory,
*  combinatorial algorithm theory, the question is whether P is equal to NP.
*  If P were equal to NP, it would be amazing. It would mean that every
*  problem where a solution can be rapidly checked can actually be solved in polynomial time.
*  We don't really believe that's true. If you're scheduling classes at a school,
*  it's, we expect that if somebody hands you a satisfying schedule, you can verify that it works.
*  That doesn't mean that you should be able to find such a schedule.
*  So intuitively, NP encompasses a lot more problems than P.
*  So can we take a small tangent and break apart that intuition? So do you first of all think that
*  the biggest sort of open problem in computer science, maybe mathematics, is whether P equals NP?
*  Do you think P equals NP or do you think P is not equal to NP? If you had to bet all your money on it.
*  I would bet that P is unequal to NP simply because there are problems that have been around for
*  centuries and have been studied intensively in mathematics and even more so in the last
*  50 years since the P versus NP was stated. And no polynomial time algorithms have been found for these
*  easy to check problems. So one example is a problem that goes back to the mathematician Gauss,
*  who was interested in factoring large numbers. So we know what a number is prior to the number
*  we know what a number is prime if it cannot be written as the product of two or more
*  numbers unequal to one. So if we can factor the number like 91, it's seven times 13.
*  But if I give you 20 digit or 30 digit numbers, you're probably going to be at a loss to
*  have any idea whether they can be factored. So the problem of factoring very large numbers
*  is does not appear to have an efficient solution. But once you have found the factors,
*  express the number as a product, the two smaller numbers, you can quickly verify that they are
*  factors of the number. And your intuition is a lot of people finding, you know, this a lot of
*  brilliant people have tried to find algorithms for this one particular problem. There's many others
*  like it that are really well studied and it would be great to find an efficient algorithm for.
*  Right. And in fact, we have some results that I was instrumental in obtaining following up on work
*  by the mathematician Stephen Cook to show that within the class NP of easy to check problems,
*  there's a huge number that are equivalent in the sense that either all of them or none of them lie
*  in P. And this happens only if P is equal to NP. So if P is unequal to NP, we would also know that
*  virtually all the standard combinatorial problems, if P is unequal to NP, none of them can be solved
*  in polynomial time. Can you explain how that's possible to tie together so many problems
*  in a nice bunch that if one is proven to be efficient, then all are? The first and most
*  important stage of progress was a result by Stephen Cook, who showed that a certain problem
*  called the satisfiability problem of propositional logic is as hard as any problem in the class P.
*  So the propositional logic problem is expressed in terms of expressions involving the logical
*  operations and or and not operating on variables that can be either true or false. So an instance
*  of the problem would be some formula involving and or and not. And the question would be whether
*  there is an assignment of truth values to the variables in the problem that would make the
*  formula true. So for example, if I take the formula A or B and A or not B and not A or B and not A or
*  not B and take the conjunction of all four of those so-called expressions, you can determine
*  that no assignment of truth values to the variables A and B will allow that conjunction of
*  what are called clauses to be true. So that's an example of a formula in
*  in propositional logic involving expressions based on the operations and or and not.
*  That's an example of a problem which is not satisfiable. There is no solution that satisfies
*  all of those constraints. And that's like one of the cleanest and fundamental problems in computer
*  science. It's like a nice statement of a really hard problem. It's a nice statement of a really
*  hard problem. And what Cook showed is that every problem in NP
*  can be re-expressed as an instance of the satisfiability problem. So to do that, he
*  used the observation that a very simple abstract machine called the Turing machine
*  can be used to describe any algorithm. An algorithm for any realistic computer can be translated
*  into an equivalent algorithm on one of these Turing machines which are extremely simple.
*  So a Turing machine, there's a tape and you can walk along that tape.
*  You have data on a tape and you have basic instructions, a finite list of instructions
*  which say if you're reading a particular symbol on the tape and you're in a particular state,
*  then you can move to a different state and change the state of the number that you
*  or the element that you were looking at, the cell of the tape that you were looking at.
*  And that was like a metaphor and a mathematical construct that Turing put together to represent
*  all possible computation. All possible computation. Now one of these so-called Turing machines is too
*  simple to be useful in practice, but for theoretical purposes we can depend on the fact that an
*  algorithm for any computer can be translated into one that would run on a Turing machine.
*  And then using that fact, he could sort of describe any possible non-deterministic polynomial time
*  algorithm. Any algorithm for a problem in P could be expressed as a sequence of
*  moves of the Turing machine described in terms of reading a symbol on the tape
*  while you're in a given state and moving to a new state and leaving behind a new symbol.
*  And given that fact that any non-deterministic polynomial time algorithm can be
*  described by a list of such instructions, you could translate the problem into the language of
*  the satisfiability problem. Is that amazing to you by the way if you take yourself back when you were
*  first thinking about the space of problems? How amazing is that? It's astonishing when you look at
*  Cook's proof. It's not too difficult to sort of figure out why this is so,
*  but the implications are staggering. It tells us that this of all the problems in
*  NP, all the problems where solutions are easy to check, they can all be rewritten in terms of
*  the satisfiability problem.
*  Yes, in adding so much more weight to the P equals NP question because all it takes is to show that one
*  algorithm in this class. So the P versus NP can be re-expressed as simply asking whether the
*  satisfiability problem of propositional logic is solvable in polynomial time.
*  In real time. But there's more. I encountered Cook's paper when he published it in a conference
*  in 1971. Yeah, so when I saw Cook's paper and saw this reduction of each of the problems in NP
*  by a uniform method to the satisfiability problem of propositional logic,
*  that meant that the satisfiability problem was a universal combinatorial problem.
*  And it occurred to me through experience I had had in trying to solve other combinatorial problems
*  that there were many other problems which seemed to have that universal structure.
*  And so I began looking for reductions from the satisfiability to other problems.
*  One of the other problems would be the so-called integer programming problem of
*  solving a determining whether there's a solution to a set of linear inequalities involving
*  integer variables.
*  Just like linear programming, but there's a constraint that the variables must remain
*  integers.
*  Integers, in fact, must be the zero or the one that's going to be the solution.
*  In fact, must be the zero or one that could only take on those values.
*  And that makes the problem much harder.
*  Yes, that makes the problem much harder. And it was not difficult to show that the
*  satisfiability problem can be restated as an integer programming problem.
*  Can you pause on that? Was that one of the first mappings that you tried to do?
*  And how hard is that mapping? You said it wasn't hard to show, but
*  you know, that's a big leap.
*  It is a big leap, yeah. Well, let me give you another example.
*  Another problem in NP is whether a graph contains a clique of a given size.
*  And now the question is, can we reduce the propositional logic problem to
*  the problem of whether there's a clique of a certain size?
*  Well, if you look at the propositional logic problem, it can be expressed as a number of
*  clauses, each of which is of the form A or B or C, where A is either one of the variables
*  in the problem or the negation of one of the variables.
*  And an instance of the propositional logic problem can be rewritten using operations of Boolean logic.
*  It can be rewritten as the conjunction of a set of clauses, the and of a set of ors,
*  where each clause is a disjunction, an or of variables or negated variables.
*  So the question in the satisfiability problem is whether those clauses can be simultaneously
*  satisfied. Now, to satisfy all those clauses, you have to find one of the terms in each clause,
*  which is going to be true in your truth assignment, but you can't make the same
*  variable both true and false. So if you have the variable A in one clause and you want to
*  satisfy that clause by making A true, you can't also make the complement of A true in some other
*  clause. And so the goal is to make every single clause true if it's possible to satisfy this.
*  And the way you make it true is at least... One term in the clause must be, must be true.
*  Got it.
*  So now we... To convert this problem to something called the independent set problem,
*  where you're just sort of asking for a set of vertices in a graph such that no two of them
*  are adjacent, sort of the opposite of the clique problem. So we've seen that we can now express
*  that as finding a set of terms, one in each clause, without picking both the variable and
*  the negation of that variable. Because if the variable is assigned the truth value,
*  the negated variable has to have the opposite truth value.
*  Right.
*  And so we can construct a graph where the vertices are the terms in all of the clauses.
*  And you have an edge between two terms if... An edge between two occurrences
*  of terms, either if they're both in the same clause, because you're only picking one
*  element from each clause. And also an edge between them if they represent opposite values
*  of the same variable, because you can't make a variable both true and false. And so you get
*  a graph where you have all of these occurrences of variables. You have edges, which mean that you're
*  not allowed to choose both ends of the edge, either because they're in the same clause or they're
*  negations of one another.
*  Right. And that's a... First of all, sort of to zoom out, that's a really powerful idea that you
*  can take a graph and connect it to a logic equation somehow, and do that mapping for all
*  possible formulations of a particular problem on a graph.
*  Yeah.
*  I mean, that still is hard for me to believe that that's possible. What do you make of that?
*  There's such a union of... There's such a friendship among all these problems across
*  that somehow are akin to combinatorial algorithms, that they're all somehow related.
*  I know it can be proven, but what do you make of it, that that's true?
*  Well, that they just have the same expressive power. You can take any one of them and
*  translate it into the terms of the other.
*  The fact that they have the same expressive power also somehow
*  means that they can be translatable.
*  Right. And what I did in the 1971 paper was to take 21 fundamental problems,
*  commonly occurring problems of packing, covering, matching, and so forth,
*  lying in the class NP, and show that the satisfiability problem can be re-expressed
*  as any of those, that any of those have the same expressive power.
*  And that was like throwing down the gauntlet or saying,
*  there's probably many more problems like this.
*  Right.
*  But that's just saying that, look, that they're all the same.
*  They're all the same, but not exactly. They're all the same in terms of whether they are
*  rich enough to express any of the others.
*  But that doesn't mean that they have the same computational complexity.
*  But what we can say is that either all of these problems or none of them are solvable in polynomial
*  time.
*  Yeah. So where does NP completeness and NP hard as classes say?
*  Oh, that's just a small technicality. So when we're talking about decision problems,
*  that means that the answer is just yes or no. There was a clique of size 15 or there's not
*  a clique of size 15. On the other hand, an optimization problem would be asking,
*  find the largest clique. The answer would not be yes or no, it would be 15.
*  So when you're asking for the... When you're putting a valuation on the different solutions
*  and you're asking for the one with the highest valuation, that's an optimization problem.
*  And there's a very close affinity between the two kinds of problems.
*  But the counterpart of being the hardest decision problem, the hardest yes-no problem,
*  the counterpart of that is to minimize or maximize an objective function.
*  And so a problem that's hardest in the class when viewed in terms of optimization,
*  those are called NP hard rather than NP complete.
*  And NP complete is for decision problems.
*  And NP complete is for decision problems.
*  So if somebody shows that P equals NP, what do you think that proof will look like
*  if you were to put on yourself? If it's possible to show that as a proof or to demonstrate an
*  algorithm?
*  All I can say is that it will involve concepts that we do not now have and approaches that we
*  don't have.
*  Do you think those concepts are out there in terms of inside complexity theory,
*  inside of computational analysis of algorithms? Do you think there's concepts that are totally
*  outside of the box that we haven't considered yet?
*  I think that if there is a proof that P is equal to NP or that P is not equal to NP,
*  it'll depend on concepts that are now outside the box.
*  Now if that's shown either way, P equals NP or P not, well actually P equals NP, what impact,
*  you kind of mentioned a little bit, but can you can you linger on it?
*  What kind of impact would it have on theoretical computer science and perhaps
*  software systems in general?
*  Well I think it would have enormous impact on the world in either way case.
*  If P is unequal to NP, which is what we expect, then we know that for the great majority of the
*  combinatorial problems that come up, since they're known to be NP complete, we're not going to be
*  able to solve them by efficient algorithms.
*  However, there's a little bit of hope in that it may be that we can solve most instances.
*  All we know is that if a problem is not in P, then it can't be solved efficiently on all instances.
*  But basically it will, if we find that P is unequal to NP, it will mean that we can't
*  expect always to get the optimal solutions to these problems, and we have to depend on
*  heuristics that perhaps work most of the time or give us good approximate solutions.
*  So we would turn our eye towards the heuristics with a little bit more acceptance and comfort
*  on our hearts.
*  Exactly.
*  Okay, so let me ask a romanticized question.
*  What to you is one of the most or the most beautiful combinatorial algorithm
*  in your own life or just in general in the field that you've ever come across
*  or have developed yourself?
*  I like the stable matching problem, the stable marriage problem, very much.
*  What's the stable matching problem?
*  Yeah.
*  Imagine that you want to marry off N boys with N girls.
*  And each boy has an ordered list of his preferences among the girls,
*  his first choice, his second choice through her Nth choice.
*  And each girl also has an ordering of the boys, first choice, second choice, and so on.
*  And we'll say that a matching, a one-to-one matching of the boys with the girls is stable
*  if there are no two couples in the matching such that the boy in the first couple prefers
*  the girl in the second couple to her mate and she prefers the boy to her current mate.
*  In other words, if there is, the matching is stable if there is no pair who want to
*  run away with each other leaving their partners behind.
*  Gotcha.
*  Actually, this is relevant to matching residents with hospitals and some other real life problems,
*  although not quite in the form that I described.
*  So it turns out that there is, that a stable, for any set of preferences,
*  a stable matching exists. And moreover, it can be computed by a simple algorithm
*  in which each boy starts making proposals to girls. And if a girl receives a proposal,
*  she accepts it tentatively, but she can drop it later if she gets a better proposal from her
*  point of view. And the boys start going down their lists proposing to their first, second,
*  third choices until stopping when a proposal is accepted. But the girls, meanwhile, are watching
*  the proposals that are coming into them and the girl will drop her current partner
*  if she gets a better proposal.
*  And the boys never go back through the list.
*  They never go back. Yeah. So once they've been denied,
*  They don't try again.
*  They don't try again because the girls are always improving their status as they receive
*  better and better proposals. The boys are going down their list, starting with their top preferences.
*  And one can prove that the process will come to an end where everybody will get matched with somebody
*  and you won't have any pair that want to abscond from each other.
*  Do you find the proof or the algorithm itself beautiful? Or is it the fact that with the
*  simplicity of just the two marching, I mean, the simplicity of the underlying rule of the algorithm,
*  is that the beautiful part?
*  Both, I would say. And you also have the observation that you might ask, who is better
*  off, the boys who are doing the proposing or the girls who are reacting to proposals?
*  It turns out that it's the boys who are doing the best.
*  That is, each boy is doing at least as well as he could do in any other staple matching.
*  So there's a sort of lesson for the boys that you should go out and be proactive and make those
*  proposals go for broke.
*  I don't know if this is directly mappable philosophically to our society, but certainly
*  seems like a compelling notion. And like you said, there's probably a lot of actual real
*  world problems that this could be mapped to.
*  Yeah, well, you get complications. For example, what happens when a husband and wife want to be
*  assigned to the same hospital? So you have to take those constraints into account.
*  And then the problem becomes NP-hard.
*  Why is it a problem for the husband and wife to be assigned to the same hospital?
*  No, it's desirable. Or at least go to the same city. So you can't, if you're assigning residents
*  to hospitals.
*  And then you have some preferences for the husband and the wife or for the hospitals?
*  The residents have their own preferences. Reference is residents, both male and female,
*  have their own preferences.
*  Residents, both male and female, have their own preferences. The hospitals have their
*  preferences. But if Resident A, the boy, is going to Philadelphia, then you'd like his wife
*  also to be assigned to a hospital in Philadelphia.
*  So which step makes it a NP-hard problem?
*  The fact that you have this additional constraint. That it's not just the preferences of individuals,
*  but the fact that the two partners to a marriage have to be assigned to the same place.
*  I'm being a little dense. The perfect matching, no, not the perfect, stable matching,
*  is what you referred to. That's when two partners are trying to...
*  Okay. What's confusing you is that in the first interpretation of the problem,
*  I had boys matching with girls.
*  In the second interpretation, you have humans matching with institutions.
*  With institutions. And there's a coupling between within the... Gotcha, within the humans.
*  Any added little constraint will make it an NP-hard problem.
*  Well, yeah.
*  Okay. By the way, the algorithm you mentioned, was it one of yours?
*  No, no, that was due to Gale and Shapley. My friend David Gale passed away before he could
*  get part of a Nobel Prize, but his partner Shapley shared in a Nobel Prize with somebody else for...
*  Economics?
*  For economics. For ideas stemming from the stable matching idea.
*  So you've also have developed yourself some elegant, beautiful algorithms. Again,
*  picking your children. So the Robin Karp algorithm for string searching, pattern matching,
*  Edmund Karp algorithm for max flows we mentioned, Hopcroft Karp algorithm for finding
*  maximum cardinality matchings in bipartite graphs. Is there ones that stand out to you as
*  ones you're most proud of or just whether it's beauty, elegance, or just being the right
*  discovery development in your life that you're especially proud of?
*  I like the Rabin Karp algorithm because it illustrates the power of randomization.
*  So the problem there is to decide whether a given long string of symbols from some alphabet
*  contains a given word, whether a particular word occurs within some very much longer word.
*  And so the idea of the algorithm is to associate with the word that we're looking for,
*  a fingerprint, some number or some combinatorial object that
*  describes that word, and then to look for an occurrence of that same fingerprint as you slide
*  along the longer word. And what we do is we associate with each word a number. So we first
*  of all, we think of the letters that occur in a word as the digits of let's say, decimal or
*  whatever base here, whatever number of different symbols there are.
*  That's the base of the numbers.
*  Yeah.
*  Right. So every word can then be thought of as a number with the letters being the digits of that
*  number. And then we pick a random prime number in a certain range, and we take that word viewed as
*  a number and take the remainder on dividing that number by the prime.
*  So coming up with a nice hash function.
*  It's a kind of hash function.
*  It gives you a little shortcut for that particular word.
*  Yeah. So that's the...
*  It's very different than any other algorithms of its kind that we're trying to do search,
*  string matching.
*  Yeah, which usually are combinatorial and don't involve the idea of taking a random fingerprint.
*  And doing the fingerprinting has two advantages. One is that as we slide along the long word,
*  digit by digit, we keep a window of a certain size, the size of the word we're looking for.
*  And we compute the fingerprint of every stretch of that length.
*  And it turns out that just a couple of arithmetic operations will take you from
*  the fingerprint of one part to what you get when you slide over by one position.
*  So the computation of all the fingerprints is simple.
*  And secondly, it's unlikely if the prime is chosen randomly from a certain range,
*  that you will get two of the segments in question having the same fingerprint.
*  And so there's a small probability of error, which can be checked after the fact.
*  And also the ease of doing the computation because you're working with these fingerprints,
*  which are remainders, modulo, some big prime.
*  So that's the magical thing about randomized algorithms is that if you add a little bit
*  of randomness, it somehow allows you to take a pretty naive approach,
*  a simple looking approach, and allow it to run extremely well.
*  So can you maybe take a step back and say, what is a randomized algorithm, this category of algorithms?
*  Well, it's just the ability to draw a random number from such,
*  from some range or to associate a random number with some object, or to draw that random from some set.
*  So another example is very simple. If we're conducting a presidential election,
*  and we would like to pick the winner, in principle, we could draw a random sample of all of the voters in the country.
*  And if it was of substantial size, say a few thousand, then the most popular candidate
*  in that group would be very likely to be the correct choice that would come out of counting
*  all the millions of votes. Now, of course, we can't do this because first of all, everybody has to
*  feel that his or her vote counted. And secondly, we can't really do a purely random sample,
*  from that population. And I guess thirdly, there could be a tie in which case,
*  we wouldn't have a significant difference between two candidates.
*  But those things aside, if you didn't have all that messiness of human beings,
*  you could prove that that kind of random picking would come up.
*  Just that random picking would solve the problem with a very low probability of being wrong.
*  Another example is testing whether a number is prime. So if I want to test whether 17 is prime,
*  I could pick any number between 1 and 17, raise it to the 16th power, module 017,
*  and you should get back the original number. So that's a very simple example.
*  And you should get back the original number. That's a famous formula due to Fermat.
*  It's called Fermat's Little Theorem. If you take any number a in the range
*  0 through n minus 1, and raise it to the n minus 1th power, module o n, you'll get back the number
*  a if a is prime. So if you don't get back the number a, that's a proof that a number is not prime.
*  And you can show that, suitably define the probability that you will get
*  a value unequaled. You will get a violation of Fermat's result is very high, and so this gives
*  you a way of rapidly proving that a number is not prime. It's a little more complicated than that
*  because there are certain values of n where something a little more elaborate has to be done,
*  but that's the basic idea. Taking an identity that holds for primes and therefore,
*  if it ever fails on any instance for a non-prime, you know that the number is not prime. It's a
*  fast choice, fast proof that a number is not prime. Can you maybe elaborate a little bit more
*  of what's your intuition why randomness works so well and results in such simple algorithms?
*  Well, the example of conducting an election where you could take, in theory, you could take a sample
*  and depend on the validity of the sample to really represent the whole is just the basic
*  fact of statistics, which gives a lot of opportunities. And I actually exploited that
*  sort of random sampling idea in designing an algorithm for counting the number of solutions
*  that satisfy a particular formula and propositional logic.
*  So some version of the satisfiability problem?
*  A version of the satisfiability problem.
*  Is there some interesting insight that you want to elaborate on? Like what some aspect of that
*  algorithm that might be useful to describe? So you have a collection of
*  of formulas and you want to count the number of solutions that satisfy
*  at least one of the formulas. And you can count the number of solutions that satisfy
*  any particular one of the formulas, but you have to account for the fact that that
*  solution might be counted many times if it solves more than one of the formulas.
*  And so what you do is you sample from the formulas according to the number of solutions that satisfy
*  each individual one. In that way, you draw a random solution, but then you correct by looking at
*  the number of formulas that satisfy that random solution and don't double count.
*  So you can think of it this way. So you have a matrix of zeros and ones, and you want to know
*  how many columns of that matrix contain at least one one. And you can count in each row how many
*  ones there are. So what you can do is draw from the rows according to the number of ones. If a
*  row has more ones, it gets drawn more frequently. But then if you draw from that row, you have to
*  go up the column and looking at where that same one is repeated in different rows and only count
*  it as a success or a hit if it's the earliest row that contains the one. And that gives you a
*  robust statistical estimate of the total number of columns that contain at least one of the ones.
*  So that is an example of the same principle that was used in studying random sampling.
*  Another viewpoint is that if you have a phenomenon that occurs almost all the time,
*  then if you sample one of the occasions where it occurs, you're most likely to find,
*  and you're looking for an occurrence, a random occurrence is likely to work.
*  So that comes up in solving identities, solving algebraic identities. You get
*  two formulas that may look very different. You want to know if they're really identical.
*  What you can do is just pick a random value and evaluate the formulas at that value and see if
*  they agree. And you depend on the fact that if the formulas are distinct,
*  then they're going to disagree a lot. And so therefore a random choice will
*  exhibit the disagreement. If there are many ways for the two to disagree
*  and you only need to find one disagreement, then random choice is likely to yield it.
*  And in general, so we've just talked about randomized algorithms, but we can look at the
*  probabilistic analysis of algorithms. And that gives us an opportunity to step back. And as we
*  said, everything we've been talking about is worst case analysis. Could you maybe comment on
*  the usefulness and the power of worst case analysis versus best case analysis, average case,
*  probabilistic? How do we think about the future of theoretical computer science, computer science
*  in the kind of analysis we do of algorithms? Does worst case analysis still have a place,
*  an important place, or do we want to try to move forward towards kind of average case analysis?
*  Yeah.
*  And what are the challenges there?
*  So if worst case analysis shows that an algorithm is always good, that's fine.
*  If worst case analysis is used to show that the problem, that the solution is not always good,
*  then you have to step back and do something else to ask how often will you get a good solution?
*  Just to pause on that for a second, that's so beautifully put because I think we tend to judge
*  I think we tend to judge algorithms. We throw them in the trash
*  the moment their worst case is shown to be bad.
*  Right. And that's unfortunate. I think a good example is going back to the satisfiability
*  problem. There are very powerful programs called SAT solvers, which in practice fairly reliably
*  solve instances with many millions of variables that arise in digital design or in proving
*  programs correct in other applications. And so in many application areas, even though
*  satisfiability as we've already discussed is NP-complete, the SAT solvers will work so well
*  that the people in that discipline tend to think of satisfiability as an easy problem.
*  So in other words, just for some reason that we don't entirely understand,
*  the instances that people formulate in designing digital circuits or other applications are such
*  that satisfiability is not hard to check.
*  And even searching for a satisfying solution can be done efficiently in practice. And there are
*  many examples. For example, we talked about the traveling salesman problem. So just to refresh
*  our memories, the problem is you've got a set of cities, you have pairwise distances between cities,
*  and you want to find a tour through all the cities that minimizes the total cost of all
*  the edges traversed, all the trips between cities. The problem is NP-hard, but people using integer
*  programming codes together with some other mathematical tricks can solve
*  geometric instances of the problem where the cities are, let's say, points in the plane
*  and get optimal solutions to problems with tens of thousands of cities.
*  Actually, it'll take a few computer months to solve a problem of that size, but for problems
*  of size a thousand or two, it'll rapidly get optimal solutions, provably optimal solutions,
*  even though, again, we know that it's unlikely that the traveling salesman problem can be solved in
*  polynomial time. Are there methodologies, like rigorous systematic methodologies for,
*  you said in practice. In practice, this algorithm sounds pretty good. Are there systematic ways of
*  saying, in practice, this one's pretty good? So in other words, average case analysis,
*  or you've also mentioned that average case kind of requires you to understand what the typical
*  case is, typical instances, and that might be really difficult.
*  That's very difficult. So after I did my original work on showing all these problems,
*  showing all these problems to be NP-complete, I looked around for a way to shed some positive
*  light on combinatorial algorithms. What I tried to do was to study problems, behavior on the average
*  or with high probability, but I had to make some assumptions about what's the probability space,
*  what's the sample space, what do we mean by typical problems. That's very hard to say.
*  So I took the easy way out and made some very simplistic assumptions. So I assumed, for example,
*  that if we were generating a graph with a certain number of vertices and edges,
*  then we would generate the graph by simply choosing one edge at a time at random until we
*  got the right number of edges. That's a particular model of random graphs that
*  has been studied mathematically a lot. And within that model, I could prove all kinds of wonderful
*  things, I and others who also worked on this. So we could show that we know exactly how many
*  edges there have to be in order for there to be a so-called Hamiltonian circuit. That's a
*  cycle that visits each vertex exactly once. We know that if the number of edges is a little
*  bit more than n log n, where n is the number of vertices, then such a cycle is very likely to
*  exist and we can give a heuristic that will find it with high probability. And we got the community
*  in which I was working got a lot of results along these lines.
*  But the field tended to be rather lukewarm about accepting these results as meaningful
*  because we were making such a simplistic assumption about the kinds of graphs
*  that we would be dealing with. So we could show all kinds of wonderful things. It was a great
*  playground. I enjoyed doing it. But after a while, I concluded that it didn't have a lot of bite
*  in terms of the practical application. Okay. So there's too much into the world of toy problems.
*  Yeah. Okay. But all right. Is there a way to find nice representative real world impactful instances
*  of a problem on which demonstrate that an algorithm is good? So this is kind of like
*  the machine learning world. That's kind of what they at its best tries to do is find a data set
*  from the real world and show the performance. All the conferences are all focused on beating the
*  performance of on that real world data set. Is there an equivalent in complexity analysis?
*  Not really. Don Knuth started to collect examples of graphs coming from various places. So he would
*  have a whole zoo of different graphs that he could choose from. And he could could study the
*  performance of algorithms on different types of graphs. But there it's really important and
*  compelling to be able to define a class of graphs. The actual act of defining a class of graphs that
*  you're interested in, it seems to be a non-trivial step if we're talking about instances that we
*  should care about in the real world. Yeah. There's nothing available there that would be analogous
*  to the training set for supervised learning, where you sort of assume that the world has
*  given you a bunch of examples to work with. We don't really have that for problems,
*  for combinatorial problems on graphs and networks. You know, there's been a huge growth,
*  a big growth of data sets available. Do you think some aspect of theoretical computer science
*  might be contradicting my own question while saying it, but will there be some aspect,
*  an empirical aspect of theoretical computer science, which will allow the fact that these
*  data sets are huge, we'll start using them for analysis? If you want to say something about
*  a graph algorithm, you might take a social network like Facebook and looking at sub graphs of that
*  and prove something about the Facebook graph and be respected and at the same time be respected
*  in the theoretical computer science community. That hasn't been achieved yet, I'm afraid.
*  Is that P equals NP? Is that impossible? Is it impossible to publish a successful paper in the
*  theoretical computer science community that shows some performance on a real world data set? Or is
*  that really just those two different worlds? They haven't really come together. I would say that
*  there is a field of experimental algorithmics where people sometimes are given some family
*  of examples. Sometimes they just generate them at random and they report on performance.
*  But there's no convincing evidence that the sample is representative of anything at all.
*  So let me ask, in terms of breakthroughs and open problems, what are the most compelling open problems
*  to you and what possible breakthroughs do you see in the near term in terms of theoretical computer science?
*  Theoretical computer science.
*  Well, there are all kinds of relationships among complexity classes that can be studied.
*  Just to mention one thing, I wrote a paper with Richard Lipton in 1979
*  where we asked the following question.
*  If you take a problem, a combinatorial problem in NP, let's say, and you
*  choose a, and you pick the size of the problem, I say it's a traveling salesman problem, but
*  I say it's a traveling salesman problem, but of size 52. And you ask, could you get an efficient,
*  a small Boolean circuit tailored for that size 52 where you could feed the edges of the graph
*  in as Boolean inputs and get as an output the question of whether or not there's a tour of a
*  certain length. And that would, in other words, briefly what you would say in that case
*  is that the problem has small circuits, polynomial size circuits.
*  Now, we know that if P is equal to NP, then in fact these problems will have small circuits.
*  But what about the converse? Could a problem have small circuits, meaning that it's,
*  that an algorithm tailored to any particular size could work well
*  and yet not be a polynomial time algorithm? That is, you couldn't write it as a single
*  uniform algorithm good for all sizes. Just to clarify, small circuits for
*  problem of particular size or even further constraint, small circuit for a particular?
*  No, for all the inputs of that size. Of that size. Is that a trivial
*  problem for a particular instance? So coming up an automated way of coming up with a circuit,
*  I guess that's just an instance. That would be hard, yeah. But there's the existential question.
*  Everybody talks nowadays about every existential questions, existential challenges.
*  Yeah.
*  You could ask the question, does the Hamiltonian circuit problem have a small circuit for every
*  size, for each size a different small circuit? In other words, could you tailor solutions
*  depending on the size and get polynomial size? Even if P is not equal to NP.
*  Right. That would be fascinating if that's true.
*  Yeah. What we proved is that if that were possible, then something strange would happen
*  in complexity theory. Some high level class, which I could briefly describe,
*  something strange would happen. So I'll take a stab at describing what I mean.
*  Sure. Let's go there.
*  We have to define this hierarchy in which the first level of the hierarchy is P
*  and the second level is NP. What is NP? NP involves statements of the form,
*  there exists a something such that something holds. For example, there exists a coloring such
*  that a graph can be colored with only that number of colors or there exists a Hamiltonian circuit.
*  There's a statement about this graph.
*  Yeah. So the NP deals with statements of that kind, that there exists a solution.
*  Now, you could imagine a more complicated expression which says for all X, there exists a Y
*  such that some proposition holds involving both X and Y. So that would say, for example,
*  in game theory, for all strategies for the first player, there exists a strategy for the second
*  player such that the first player wins. That would be at the second level of the hierarchy.
*  The third level would be there exists an A such that for all B, there exists a C
*  that something holds. And you can imagine going higher and higher in the hierarchy.
*  And you'd expect that the complexity classes that correspond to those different cases
*  would get bigger and bigger.
*  What do you mean by bigger and bigger?
*  Sorry. Sorry. They'd get harder and harder to solve.
*  Harder and harder, right.
*  Harder and harder to solve. And what Lipton and I showed was that if
*  NP had small circuits, then this hierarchy would collapse down to the second level.
*  In other words, you wouldn't get any more mileage by complicating your
*  expressions with three quantifiers or four quantifiers or any number.
*  I'm not sure what to make of that exactly.
*  Well, I think it would be evidence that NP doesn't have small circuits because
*  something so bizarre would happen. But again, it's only evidence, not proof.
*  Well, yeah, that's not even evidence because you're saying P is not equal to NP because
*  something bizarre has to happen. I mean, that's proof by the lack of bizarreness in our science.
*  But it seems like just the very notion of P equals NP would be bizarre. So any way you arrive at
*  there's no way you have to fight the dragon at some point.
*  Yeah. Okay. Well, anyway, for whatever it's worth, that's what we proved.
*  Awesome. So that's a potential space of open interesting problems.
*  Yeah. Let me ask you about this other world of machine learning, of deep learning.
*  What's your thoughts on the history and the current progress of machine learning field
*  that's often progressed sort of separately as a space of ideas and space of people
*  than the theoretical computer science or just even computer science world?
*  Yeah, it's really very different from the theoretical computer science world because
*  the results about it, algorithmic performance tend to be empirical. It's more akin to
*  the world of SAT solvers where we observe that for formulas arising in practice,
*  the solver does well. So it's of that type. We're moving into the empirical evaluation of
*  algorithms. Now it's clear that there have been huge successes in image processing, robotics,
*  natural language processing, a little less so, but across the spectrum of
*  game playing is another one. There have been great successes.
*  And one of those effects is that it's not too hard to become a millionaire if you can get a
*  reputation in machine learning and there'll be all kinds of companies that will be willing to
*  offer you the moon because they think that if they have AI at their disposal, then they can
*  solve all kinds of problems. But there are limitations. One is that the solutions that
*  you get to supervised learning problems through convolutional neural networks
*  seem to perform amazingly well even for inputs that are outside the training set.
*  But we don't have any theoretical understanding of why that's true.
*  And secondly, the solutions, the networks that you get are very hard to understand. And so very
*  little insight comes out. So yeah, yeah, they may seem to work on your training set and you may be
*  able to discover whether your photos occur in a different sample of inputs or not. But we don't
*  really know what's going on. We don't know the features that distinguish the photographs or the
*  objects are not easy to characterize. Well, it's interesting because you mentioned coming up with
*  the small circuit to solve a particular size problem. It seems that neural networks are kind
*  of small circuits. In a way, yeah. But they're not programs. Sort of like the things you've
*  designed are algorithms, programs, right? Algorithms. Neural networks aren't able to
*  develop algorithms to solve a problem. Well, they are algorithms. It's just that they're...
*  But sort of, yeah, it could be a semantic question, but there's not
*  a algorithmic style manipulation of the input. Perhaps you could argue there is.
*  Yeah, well... It feels a lot more like a function of the input.
*  Yeah, it's a function. It's a computable function. Once you have the network, you can
*  simulate it on a given input and figure out the output. But if you're trying to recognize
*  images, then you don't know what features of the image are really being
*  determinant of what the circuit is doing. The circuit is sort of very intricate,
*  and it's not clear that the simple characteristics that you're looking for, the edges of the objects
*  or whatever they may be, they're not emerging from the structure of the circuit.
*  Well, it's not clear to us humans, but it's clear to the circuit.
*  Yeah, well, right.
*  I mean, it's not clear to sort of the elephant how the human brain works, but it's clear to us
*  humans, we can explain to each other our reasoning, and that's why the cognitive
*  psychology field exists. Maybe the whole thing of being explainable to humans is a little bit
*  overrated.
*  Oh, maybe, yeah. I guess you can say the same thing about our brain, that when we perform
*  acts of cognition, we have no idea how we do it really. We do, though. I mean,
*  at least for the visual system, the auditory system and so on, we do
*  get some understanding of the principles that they operate under, but for many deeper cognitive
*  tasks, we don't have that.
*  That's right. Let me ask. You've also been doing work on bioinformatics. Does it amaze you that
*  the fundamental building blocks, if we take a step back and look at us humans, the building blocks
*  used by evolution to build us intelligent human beings is all contained there in our DNA?
*  It's amazing, and what's really amazing is that we are beginning to learn how to edit
*  DNA, which is very, very, very fascinating, this
*  ability to take a sequence, find it in the genome, and do something to it.
*  I mean, that's really taking our biological system towards the worlds of algorithms.
*  Yeah, but it raises a lot of questions. You have to distinguish between doing it on an individual
*  or doing it on somebody's germline, which means that all of the descendants will be affected.
*  So that's like an ethical...
*  Yeah, so it raises very severe ethical questions.
*  And even doing it on individuals, there's a lot of hubris involved that you can assume that
*  knocking out a particular gene is going to be beneficial because you don't know what the side
*  effects are going to be. So we have this wonderful new world of gene editing,
*  which is very, very impressive. And it could be used in agriculture. It could be used in
*  medicine in various ways. But very serious ethical problems arise.
*  What are, to you, the most interesting places where algorithms...
*  The ethical side is an exceptionally challenging thing that I think we're going to have to tackle
*  with all of genetic engineering. But on the algorithmic side, there's a lot of benefit
*  that's possible. So is there areas where you see exciting possibilities for algorithms to help
*  model, optimize, study biological systems?
*  Yeah, I mean, we can certainly analyze genomic data to figure out
*  which genes are operative in the cell and under what conditions and which proteins affect one
*  another, which proteins physically interact. We can sequence proteins and modify them.
*  Is there some aspect of that that's a computer science problem,
*  or is that still fundamentally a biology problem?
*  Well, it's a big data. It's a statistical big data problem for sure. So the biological data
*  sets are increasing. Our ability to study our ancestry, to study the tendencies towards disease,
*  to personalize treatment according to what's in our genomes and what tendencies for disease we have,
*  to be able to predict what troubles might come upon us in the future and anticipate them,
*  to understand whether you, for a woman, whether her proclivity for
*  breast cancer is strong enough that you would want to take action to avoid it.
*  You dedicate your 1985 Turing Award lecture to the memory of your father.
*  Mm-hmm.
*  What's your fondest memory of your dad?
*  Seeing him standing in front of a class at the blackboard, drawing perfect circles
*  by hand and showing his ability to attract the interest of the motley collection of eighth grade
*  students that he was teaching.
*  When did you get a chance to see him draw the perfect circles?
*  On rare occasions, I would get a chance to sneak into his classroom and observe it.
*  I think he was at his best in the classroom. I think he really came to life
*  and had fun not only teaching but engaging in chit chat with the students and engaging in
*  chit chat with the students and ingratiating himself with the students. What I inherited from
*  that is a great desire to be a teacher. I retired recently and a lot of my former students came,
*  students with whom I had done research or who had read my papers or who had been in my classes.
*  When they talked about me, they talked not about my 1979 paper or my 1992 paper but about what came
*  away in my classes and not just the details but just the approach and the manner of teaching.
*  I take pride in the, at least in my early years as a faculty member at Berkeley,
*  I was exemplary in preparing my lectures and I always came in prepared to the teeth and able
*  therefore to deviate according to what happened in the class and to really provide a model for
*  the students. Is there advice you can give out for others on how to be a good teacher?
*  Preparation is one thing you've mentioned, being exceptionally well prepared. Are there other
*  things, pieces of advice that you can impart? The top three would be preparation, preparation,
*  and preparation. Why is preparation so important I guess? It's because it gives you the ease to
*  deal with any situation that comes up in the classroom and if you discover that you're not
*  getting through one way, you can do it another way. If the students have questions, you can
*  handle the questions. Ultimately, you're also feeling the crowd, the students of what they're
*  struggling with, what they're picking up, just looking at them through the questions but even
*  just through their eyes. Because of the preparation, you can dance. You can dance. You can
*  say it another way or give another angle. Are there in particular ideas and algorithms that
*  computer science do you find were big aha moments for students? Were they, for some reason once they
*  got it, it clicked for them and they fell in love with computer science? Or is it individual,
*  is it different for everybody? It's different for everybody. You have to work differently with
*  students. Some of them just don't need much influence. They're just running with what they're
*  doing and they just need an ear now and then. Others need a little prodding. Others need to
*  be persuaded to collaborate among themselves rather than working alone. They have their personal
*  ups and downs. You have to deal with each student as a human being and bring out the best.
*  Humans are complicated. Perhaps a silly question. If you could relive a moment in your life outside
*  of family because it made you truly happy or perhaps because it changed the direction of
*  your life in a profound way, what moment would you pick?
*  I was kind of a lazy student as an undergraduate and even in my first year in graduate school.
*  I think it was when I started doing research. I had a couple of summer jobs where I was able
*  to contribute and I had an idea. Then there was one particular course on mathematical methods
*  and operations research where I just gobbled up the material and I scored 20 points higher than
*  anybody else in the class. Then came to the attention of the faculty and it made me realize
*  that I had some ability that was going somewhere. You realize you're pretty good at this thing.
*  I don't think there's a better way to end it, Richard. It was a huge honor. Thank you for
*  decades of incredible work. Thank you for talking to me.
*  Thank you. It's been a great pleasure. You're a superb interviewer.
*  Stop it. Thanks for listening to this conversation with Richard Karp. Thank you to our sponsors,
*  8 Sleep and Cash App. Please consider supporting this podcast by going to 8sleep.com
*  Lex to check out their awesome mattress and downloading Cash App and using code Lexpodcast.
*  Click the links, buy the stuff, even just visiting the site, but also considering the purchase helps
*  them know that this podcast is worth supporting in the future. It really is the best way to support
*  this journey I'm on. If you enjoy this thing, subscribe on YouTube, review it with 5 stars
*  on Apple Podcast, support it on Patreon, or connect with me on Twitter at Lex Friedman if you can
*  figure out how to spell that. And now let me leave you with some words from Isaac Asimov.
*  I do not fear computers. I fear lack of them. Thank you for listening and hope to see you next time.
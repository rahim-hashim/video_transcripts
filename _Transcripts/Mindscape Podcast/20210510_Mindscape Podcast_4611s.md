---
Date Generated: June 09, 2024
Transcription Model: whisper medium 20231117
Length: 4611s
Video Keywords: ['math', 'mathematics', 'topology']
Video Views: 23822
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2021/05/10/146-emily-riehl-on-topology-categories-and-the-future-of-mathematics/

“A way that math can make the world a better place is by making it a more interesting place to be a conscious being.” So says mathematician Emily Riehl near the start of this episode, and it’s a good summary of what’s to come. Emily works in realms of topology and category theory that are far away from practical applications, or even to some non-practical areas of theoretical physics. But they help us think about what is possible and how everything fits together, and what’s more interesting than that? We talk about what topology is, the specific example of homotopy — how things deform into other things — and how thinking about that leads us into groups, rings, groupoids, and ultimately to category theory, the most abstract of them all.

Emily Riehl received a Ph.D in mathematics from the University of Chicago. She is currently an associate professor of mathematics at Johns Hopkins University. Among her honors are the JHU President’s Frontier Award and the Joan & Joseph Birman Research Prize. She is author of Categorical Homotopy Theory, and co-author of the upcoming Elements of ∞-Category Theory. She competed on the United States women’s national Australian rules football team, where she served as vice-captain.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x

#podcast #ideas #science #philosophy #culture
---

# Emily Riehl on Topology, Categories, and the Future of Mathematics
**Mindscape Podcast:** [May 10, 2021](https://www.youtube.com/watch?v=PfAENWzgIes)
*  Hello everyone, welcome to the Mindscape Podcast. I'm your host, Sean Carroll.
*  We've done a lot of sort of science on the podcast over the years, as it were.
*  The podcast is old enough, I can now say over the years. Wow, that's pretty impressive.
*  And doing science, when you try to talk about science to an audience which is not necessarily
*  full of specialists in that particular kind of science, what do you do? How do you talk about
*  science to non-scientists? Well, the very first thing you do is you strip out all the math,
*  right? You assume that the people listening are not necessarily familiar with the equations,
*  the symbols, the manipulations that the professional scientists have to go through
*  to understand their field. But you can nevertheless, even without the math,
*  you can talk about the concepts that the scientists are dealing with.
*  This raises a puzzle when the thing you want to talk about is math. We haven't talked about math
*  as a pure subject that much here on Mindscape. We did talk to Stephen Strogatz, who's a professional
*  mathematician, but he's very close to being a physicist in many ways. We haven't quite ascended
*  to the truly abstract realms of very pure mathematics. So that's what we're doing here
*  today. Pure mathematics, no equations, but we're going to try to talk about the concepts that you
*  come across at the most elevated realms of mathematical thought. Our guest today is Emily
*  Reel, who is a topologist at Johns Hopkins. And she's a very big believer in being able to
*  conceptualize these deep mathematical ideas in the simplest and best way possible. So she's a
*  great person to guide us on this tour. And the foundational idea we're going to be talking about
*  is topology. Topology is the study of the properties of mathematical spaces that are invariant when you
*  smush them, when you smoothly deform them a little bit, right? Like if you have some clay that is
*  molded into a shape, you can talk about the number of holes in the shape of clay that you have. And
*  then if you move around the clay a little bit, if you don't rip it, the number of holes will remain
*  constant. So that's a topological invariant. It turns out, and this is where the fun part comes,
*  that as a mathematician you want to say, okay, what do we mean by characterizing the qualities
*  of a mathematical space that are invariant under smooth deformations? Well, you can count the holes,
*  you can also say, well, how many times can I make a path that wraps around the holes in this
*  particular system? Those kinds of structures turn out to be numbers or transformations or other
*  things that we can add together and multiply together. And we build these mathematical algebraic
*  structures by asking the question, how do we topologically characterize these kinds of spaces?
*  So we're led from topology into algebra, and Emily's going to take us there. We're going to
*  discuss things like homotopy, groups, rings, groupoids, all these words that you're not
*  supposed to have necessarily been familiar with already. We're going to discuss them. And by the
*  end, we're getting into what is called category theory. Category theory is something where
*  even the other mathematicians go, oh no, that's too abstract for me. Category theory is sort of
*  a general theory of spaces and structures and maps between them. It provides a different way
*  of thinking about mathematics as a whole. So I'm a big believer that math, just like physics,
*  is part of the general intellectual conversation we should be having. There should be history and
*  economics and math and physics, and it would be a mistake to exclude math from this overall
*  intellectual discourse. And I think this conversation is a good example of how we can do it. Thinking
*  like a mathematician gives you new handles on the world, just like thinking like a physicist does.
*  And so I think it's going to be fun. Let's go.
*  Emily Reel, welcome to the Mindscape Podcast.
*  Thank you.
*  You know, I know that as a physicist, as a theoretical physicist, who thinks about the
*  universe and the many worlds of quantum mechanics and so forth, I'm often asked, like, what is the
*  point of this? Are you making a better cell phone or are you curing cancer? Like, why are you doing
*  this? And I have my own answers, but as a mathematician who works on topology, category,
*  things like that, you must also get this. So what is your, do you have a favorite answer to that kind
*  of question? Sure. I mean, my dad loves to ask me what the practical applications are of the math
*  I love to think about. And I think he knows that he's kind of needling me because, you know,
*  that's just, it's just not the point for all mathematicians. I mean, for some, of course it
*  is, you know, there are very important uses of mathematics to make the world a better place. But
*  I guess a way that mathematics can make the world a better place is by making it a more interesting
*  place to be a conscious being. And that's how I, or that's what inspires me to be a mathematician.
*  Good. No, I think I, I'm not gonna say that's the right answer, because like you say, different
*  people have different answers, but that's analogous to my answer. And people ask me about looking for
*  the Higgs boson. And so many of my physics friends will say like, well, it might someday inspire a
*  new technological something. I'm like, no, no, number one, no, it won't. And number two, that's
*  not why we're doing it. We're doing it because we want to find out what's going on. And if there's a
*  application someday, that'll be a benefit. The other preliminary question I wanted to ask,
*  I just had a podcast episode a couple of weeks ago about the philosophy of mathematics. And,
*  you know, there's realism versus non realism, Platonism versus, I don't know, anti Platonism.
*  I'm told that most working mathematicians are Platonists. They think of what they study as
*  in some sense, real. Do you do you know, or care or have a take on that debate?
*  I certainly don't know as much about it as some of your other guests, but I, I agree with that
*  instinct. I mean, the things that I think about, and I dream about, and I talk about with my friends
*  feel very real to me. And, you know, I don't expect that I'll kind of trip over one on my walk to
*  campus. But, you know, they feel as real to me as I mean, as anything else. I mean, I guess,
*  as I understand it, that, you know, a table that seems like a solid real thing is not really real,
*  either. So, so yes, I, yeah, I subscribe to Platonism. Well, yeah, I mean, there's certainly
*  some structure to math, right? Like, we all agree, given the axioms, where we go, and so forth. So,
*  there's something there. I actually don't have a strong opinion one way or the other. That's why
*  I'm quizzing people these days. But, though, actually, I mean, there's a, there's a philosophy
*  of mathematics that's maybe a little closer to the point of view of category theory, which we'll get
*  into later on, which goes by the name of structuralism, which says that, you know, what a mathematical
*  object really is, is determined by the role that it plays within mathematics. So, so for example,
*  you know, you could ask, what are the natural numbers, you know, 0, 1, 2, 3, 4, 5, and a role
*  that the natural numbers play within mathematics. I could, I could give it a fancy name. I could
*  say they're the kind of universal discrete dynamical system. But essentially, what that means is,
*  you know, natural numbers are something you can recursively define functions on. If you have,
*  if you're trying to define a, you know, sort of a sequence of points or a sequence of real numbers,
*  what you, strategy, you know, Fibonacci sequence, for instance, is a famous sequence, 1, 1, 2, 3,
*  5, 8, 13, 21, 34. The relative terms converge to the golden ratio. It's, there's a lot of fun
*  properties in Fibonacci. But a strategy for defining a sequence is you define the first
*  term in the sequence or maybe the first few terms. And then you give a formula or a
*  strategy for producing the next term in the sequence from the terms you have previously.
*  And the fact that recursion is possible is telling us something very deep about the role
*  that natural numbers play in mathematics. And so I guess I'm of the point of view of like,
*  that's what the natural numbers are. They are sort of the thing that you can recursively define
*  functions on. How, quite how that fits with Platonism isn't entirely clear to me, but.
*  Yeah, no, no, no, me neither. I did have a guest a while ago, James Lademan, who's a philosopher,
*  who says the same thing about physics. He is a structural realist. He thinks that what really
*  matters are the different structures, not the objects that we attribute these structures to
*  relating between. I don't. Great. It sounds like he's a category theorist.
*  It could be. Aren't we all category theorists? We're moving in that direction. So we will get
*  to there. But I think you had, as we were talking about what to discuss here, I think you had a
*  strategy that makes perfect sense of starting with topology, because topology is something
*  everyone has heard of. Right. I mean, why don't I rather than try to guess, why don't you tell us
*  what do you think the definition of topology is that we could all get our hands on? Great. So
*  topology is the study of spaces, both kind of physical geometrical spaces that we move in,
*  in the world, but also spaces that you might imagine that have some resemblance to, you could
*  be in space, three dimensions, two dimensions, one dimension, but are somehow more exotic.
*  So a topological space could be, for instance, the points on a plane is an example of a topological
*  space. Or you can imagine the points that are on the surface of a sphere, so the surface of a
*  soccer ball, surface of the earth. Or you can imagine the points that are on the surface of a
*  donut. You can imagine that you're an ant that sort of walks around a donut and all the different
*  configurations that ant could be in those describe points in a topological space. And then you can
*  start to compare what those worlds are like. Topology is a realm to do that. Can I just ask
*  very quickly, when mathematicians use the word space, obviously, it doesn't simply mean the
*  three-dimensional space in which we live. What's the difference between space and set?
*  Right. So if I wanted to define a topological space formally in mathematics, I would start with a set
*  of points. So if I wanted to describe three-dimensional Euclidean space, I would
*  start with the set of points, which are determined by three real coordinates, sort of a distance
*  along the x-axis, a distance along the y-axis, a distance along the z-axis. So that's a set of
*  points. We can think of them as the points in three-dimensional space. But then what turns a
*  set into a topological space is also a way to understand distances between points, or more
*  generally understand when points are nearby and when points are far apart. So that could be a
*  function that tells you how to compute the distance between two points. That's a metric space, which is
*  an important type of topological space, or there's a more abstract way to get at the same thing in
*  the absence of a formula for distances. Okay. And so a line is a space, a circle is a space,
*  the sphere. So for mathematicians, the sphere is just the surface of the sphere, right? It's not
*  the interior, like you said. The two-dimensional sphere is the surface of the ball. And then you
*  could have like a hundred-dimensional sphere or whatever. So there's a lot of spaces we have to
*  play with. Right. You can have Mobius bands. So that's a space that's kind of like,
*  I mean, it's kind of like a cylinder. So it's like a toilet paper tube. But imagine you cut
*  the toilet paper tube sort of long ways from end to end. So now you have just a flat
*  strip, and then you twist it and then glue it back together. So that is also a space. It's quite
*  similar to the cylinder, but it's a non-orientable space. It's confusing in a Mobius strip,
*  whether you're on the inside or the outside, there's no way to decide that. Whereas on
*  the toilet paper tube, there's the outside where the toilet paper goes around, and then there's
*  the inside, which you sort of put on the roll, on the holder. So. Do you have one of those
*  Klein bottle sculptures? I have a Klein bottle sculpture. I don't, but right. So a Klein bottle
*  is a one dimension higher version of this. And what's interesting about the Klein bottle is,
*  well, so it's a surface. It's kind of like the surface of a sphere. Let me describe how you
*  would build a Klein bottle. So you can start with a flat sheet of paper. You would glue two sides of
*  the paper together. So you're forming now a toilet paper tube. And then, so from there,
*  kind of a simpler construction that isn't the Klein bottle, is you could just sort of stretch
*  the toilet paper tube and glue the end circles together. And if you did that, you would get a
*  surface of a donut shape. So that's familiar. The torus. We can use the word torus. It's okay.
*  Okay. We can use the word torus. So if I want to get a Klein bottle, it's the same idea. I'm going
*  to glue the two ends of the toilet paper tube together, glue those two circular ends together,
*  but I want to twist the one. So if I'm gluing, if I'm walking around, when I glue them together,
*  I'm sort of zipping up the going counterclockwise around one of the circles and clockwise around
*  the other circle. But I want to reverse the orientation on one of the circles before doing
*  this. Now, you can't do this in three dimensional space. So if we were in a fourth dimension,
*  you could actually embed a Klein bottle into four dimensional space and do this construction.
*  But there are these toys that you should just, everyone should just Google and there are these
*  toy glass versions. And what's fun about it is there's some ambiguity between what space is
*  inside of a Klein bottle and what is outside. So if you have a torus, like a glass donut,
*  you could sort of fill it with jelly and the jelly is inside the torus. It's not outside.
*  Until you bite it, you're not going to get jelly everywhere. But if you have one of these Klein
*  bottles, you could try and put jelly or let's say Kool-Aid inside the Klein bottle. And if you're
*  not careful, if you sort of flip it upside down and flip it right side up again, it's going to
*  get all over your desk because there's no inside and outside. And this is the stock and trade of
*  topologists, right? So you don't care so much about the individual bumps and wiggles like
*  geometry cares about. Topology is more loosey goosey in what it cares about.
*  Exactly. Yeah, very loosey goosey.
*  And so, but the other thing to get on the table, I guess, is that there are topological spaces that
*  we care about. Well, maybe they're inspired by real physical situations, but you might think that,
*  well, physical space is three dimensional and we can have subsets of that. Therefore,
*  there's some topological spaces to think about, but not that many. But as you point out, like
*  there are complicated situations where the space of all possible configurations of something is an
*  interesting topological space. Yeah, totally. So, I mean, one of my favorite sources of examples
*  of topological spaces are something called configuration spaces. And these come up in
*  robotics. They come up in physics where they might be called state spaces. And exactly as you point
*  out, these can get very high dimension very quick, but let me mention an example that's small enough
*  that we can dream about it. So, imagine you have a factory and there's a sort of one-dimensional
*  track on the floor in the factory. So, there's a strip essentially, and maybe it's a kind of a
*  wheel or like a train track. You can move forward and backwards along that track. And we're going to
*  have two robots positioned on the track. There's a red robot and a blue robot. So, well, let's
*  actually start with one robot. So, if you had one robot on a track, then you can describe its
*  positions using just kind of a one dimension. It's like an interval. You can have the robot all the
*  way at one end or all the way at the other end or any place in between. It can move continuously. So,
*  this one-dimensional interval is describing the space of configurations of that robot.
*  So, now let's put two robots on the track, a red one and a blue one. And now there's a space that
*  describes the configurations of those two robots. I mean, you might think it's a one-dimensional
*  space because the robots are still on this one-dimensional track. But actually, you should
*  use kind of one coordinate to keep track of where the red robot is and another coordinate to keep
*  track of where the blue robot is. And so, that is describing the space that's formed by taking a
*  product of an interval with itself. In other words, it's a square, including the interior,
*  except the two robots can't be in the same spot. If these are physical robots, they can't collide
*  into each other. So, you have to remove a diagonal segment from that square. And what you're left is
*  with these two triangular components. The bottom triangle corresponds to the red robot being on the
*  right of the blue robot and the top triangle corresponds to the red robot being on the left
*  of the blue robot. And so, what's interesting about the space, what we can see already by
*  visualizing the configuration space, which is this square with a diagonal removed from it,
*  is that it's disconnected. Once you've put your robots on the track, you're not going to be able
*  to swap their orientation with respect to each other. That's right. But if you're designing the
*  factory, you might say, well, that's a little bit undesirable. I don't have as much flexibility. And
*  improvement perhaps in the design, depending on, of course, what you're trying to do with these
*  robots on this track, is you could make a circular track instead of a straight track.
*  And a circle is also a one-dimensional object. You just sort of move around it going clockwise.
*  There's kind of one direction of motion. But if you had two robots on a circular track,
*  then the way you describe their configuration space is you would take, each robot is some
*  arbitrary point in the circle. We have two circles though. So, we take the product of those two
*  circles. And this is fun to think about that actually, the product of two circles corresponds
*  to the points on the surface of a torus again. So, S1 cross S1, the product of two circles are
*  the points on the torus. Again, the robots can't be on the same point. So, what you have to do is
*  you have to imagine you have the surface of a torus. You built it by gluing together your
*  toilet paper tube. Now, you're going to make a diagonal cut that, it's a cut that goes around
*  both loops in the torus once. So, you actually did this at home last night to test it in the way my
*  toilet paper tube was made. How to see exactly there. So, it was easy to see that cut. It's
*  sort of a diagonal cut that moves once around in both directions. And if you do that, you're left
*  with a connected surface. And that corresponds to the idea that if you have two robots on a circular
*  track, they can really visit all configurations. There's no left and right anymore. You can have
*  them in any position. So, anyway, this is just sort of baby, baby examples of a really rich and
*  beautiful subject. Some of the most difficult and important decisions we make involve choosing
*  people, whether it's choosing a PhD thesis advisor or choosing a prospective spouse or choosing who
*  to hire for your company. I can't help you with the first two, but if you're looking to hire people,
*  I can recommend Indeed. Indeed is the job site that makes hiring easy. You can post your ad,
*  you can screen candidates, and interview them all on Indeed. Indeed gives you tools like Indeed
*  Instant Match, giving you quality candidates whose resumes fits your job description immediately,
*  and Indeed skills tests that on average reduces hiring time by 27%. You can choose from more than
*  130 skills tests, then add your must have requirements so that you only pay for the
*  applications that meet them. Get started right now with a free $75 sponsored job credit to upgrade
*  your job post at Indeed.com slash Mindscape. That's a $75 credit at Indeed.com slash Mindscape,
*  offer valid through June 30, terms and conditions apply. Right, because it's good because what
*  topologists care about are the features that don't change by like small deformations of the
*  space. So the fact that a space is in two disconnected components, like the original example,
*  versus just being one connected component, like the second example, that's the kind of thing that
*  gets topologists very excited. Right, so when I say circular track, it could be an oval track,
*  it could be a square track, it could be a hexagonal track from a topologist, those are all the same.
*  The famous thing I bet many people have heard that to a topologist,
*  a coffee cup is the same as a donut, right? Because they're both Taurus's.
*  Right, right. I mean, that's not my favorite example because, so topologists have different
*  notions of when things are the same that we're alluding to. And one of the notions of sameness is
*  if two spaces are what's called homeomorphic. And what homeomorphic means is that there is a
*  one-to-one correspondence between the points and the space. There are two invertible functions,
*  invertible continuous functions that map all the points on one space to the other and the other to
*  the one. And so if you have a solid Taurus now built out of clay and you have a solid coffee cup,
*  you can define one of these homeomorphisms, this one-to-one correspondence between the points in
*  the Taurus and the points in the mug that are continuous so that you're not tearing the surfaces
*  apart or adding new holes where there weren't holes before, that sort of thing. So I mean,
*  it's true that topologists consider Taurus and a coffee mug to be the same, but for a really kind
*  of obvious reason, they're just so evidently the same. But there's another notion of sameness,
*  a weaker notion of sameness that also comes up in topology, which is called homotopy equivalence.
*  And here the idea is two spaces are homotopy equivalent if you can continuously deform
*  one to another. And so let me give you some examples. So all of Euclidean space,
*  three-dimensional Euclidean space is homotopy equivalent to a single point.
*  So you could imagine, I think of this homotopy equivalence as like the reverse big bang. So
*  you imagine three-dimensional Euclidean space. So you have, let's imagine we have the origin point,
*  so the center of the universe and then all the other points in the universe. I realize the
*  universe is probably not three-dimensional, but let's just bear with me here.
*  Also it doesn't have a center, but that's okay. We're going to, you're a method.
*  And or an or does have a center, but let's pretend there's a center of the universe and the universe
*  is three-dimensional. So in the reverse big bang, what I'm going to do is I'm going to continuously
*  move all the points in the universe back in a straight line to the center of the universe,
*  to the origin. And they'll move kind of faster or slower depending on how far away they are.
*  So at time zero, every point is where it is. And then at time one, they've all crashed home into the
*  center of the universe. So that is describing a continuous deformation that reveals that
*  three-dimensional Euclidean space and the points are the same. So here's an example,
*  a sort of everyday example of a homotopy equivalence that feels more fun to me than the-
*  Let me just butt in there because so just to get it clear, the reason why this is an interesting
*  example is because the point and three-dimensional space are homotopy equivalent. One can be
*  continuously deformed to the other, but they're not homeomorphic because there's not sort of an
*  equal number of points in them. Yeah, right. There's uncountably infinitely many points
*  in three-dimensional space, but there's one point in one point space. And yeah, so this is a cooler,
*  way more destructive notion. I mean, dimensions totally don't matter anymore. All n-dimensional
*  Euclidean space is also homotopy equivalent to a point. So an example, an everyday example that
*  is kind of like that is to a topologist, a pair of pants and a thong are the same.
*  You can imagine a homotopy equivalence that sort of shrinks sort of vertically, I guess,
*  and just leaves the thong from the pair of pants.
*  And this is the, so the point is that there are different ways of expressing the idea of sameness
*  depending on your sort of level of focus on what you care about. Yeah, totally, totally. And this
*  is very pervasive in mathematics. You know, mathematicians love trying to understand the
*  sense in which things are the same, and it's often a pretty loose sense. So I had a very,
*  very brief career, in fact, as a hack topologist when I was in graduate school and I needed to
*  calculate the homotopy of various things that appear in particle physics, because we have these
*  things called topological defects, right, which are very important from the early universe.
*  None of the things I calculated turn it out to be relevant to the real world, but, you know, that's
*  that's the risk that we take when we do these things. But it gets us into, you know, so far
*  it's been fun, homotopy, you know, smoothly deforming things into each other. But now we want to be a
*  little bit more rigorous about it. We want to characterize, we want to use this notion of
*  smoothly deforming one thing into another to characterize the topology of different spaces,
*  right? I mean, is in some sense our job to sort of characterize all topological spaces?
*  Yeah, exactly. And a way to a classical problem, which is a good way to visualize this, is you can
*  ask how many different surfaces are there, you know, sort of in this sort of very flexible sense,
*  so not necessarily just. So, for instance, is we've described a few different surfaces. There's the
*  sort of surface of a sphere, there's a surface of a torus. You can have many hold, the torus was the
*  donut shape. You can imagine having many hold donuts, or like, you know, you're baking a tray
*  of donuts, but you've put them too close to each other. And so they've all kind of congealed, and
*  there's, you know, one donut with three holes in it, you know, that's another surface. And there's
*  a classification question, you know, how can we tell that these spaces are really different? I mean,
*  they seem different, perhaps, maybe I'm giving away my intuition, but they seem different,
*  you know, but how do we prove that they're different? Because we've seen that these
*  wildly different spaces are, in some sense, the same. Yeah, so how do we do that?
*  So, yeah, so the idea is, I mean, this is a hard question to answer geometrically, because
*  just because you can't imagine a continuous deformation of one space to the other doesn't
*  mean it doesn't exist. So strategy is to bring algebra into the story somehow, and give a way to
*  assign a number or some other kind of algebraic structure to a topological space. And if in a way
*  that would give the same answer if the spaces were homotopy equivalent. So the homology groups
*  are homotopy groups that there are various different constructions you can do. And it's
*  easy to prove that if the spaces have continuously deformable into each other, they'll produce the
*  same invariance. And so if you happen to get different invariance, then you know that they
*  were different. Right. So actually, go ahead. Well, I can give an example of this. Yeah,
*  so we do that. So what I'm going to try and argue for you is that the surface of a sphere,
*  so the surface of a soccer ball is a different space than the surface of a donut. So a torus
*  and a sphere are different topological spaces. And just to make sure we're imagining these spaces,
*  again, you know, imagine you're an ant walking around the surface of a sphere, that's one space,
*  the different positions the ant could be. Or you can imagine an ant walking around the surface of
*  a donut. Not the interior in either case, just the surface. Not the interior in either case,
*  right? The ant can't eat the donut or eat the sphere. The ant is sort of stuck on the surface.
*  And it can't like jump off either. Okay. So, right. So the invariant that I'm going to use to prove
*  that these are different is something called the fundamental group. And what it's counting,
*  essentially, so in each, it's for convenience, I'm going to pick a point on each of these spaces.
*  These spaces are connected, so picking a point is not a big deal. So pick whichever one you want.
*  We'll take the North Pole on the sphere and any point at all on the torus. And what the fundamental
*  group is going to calculate is the number of essentially different ways that the ant can walk
*  from this home base point, walk around on the surface and come back to the home base point.
*  So the subtlety there, as I said, the number of essentially different ways. So, I mean, there are
*  uncountably infinitely many ways an ant can walk around the surfaces. But what I'm asking are they
*  essentially different? And so let's set aside the sphere example for now. Let's start by thinking
*  about the surface of the donut. So an example of two ways that are essentially different is we can
*  imagine starting at our home base point and walking, let's say in a counterclockwise direction
*  around the loop that goes through the sort of donut hole. If you put a donut hole inside the donut,
*  you can imagine walking. It's sort of in a vertical... The short way around, basically.
*  The short way around. Great. So that's one way the ant could walk.
*  Or the ant could walk, let's say, tracing the same trajectory, but going in reverse orientation,
*  going backwards rather than forwards. So those are fundamentally different. And what I mean by
*  fundamentally different is there's no way to continuously deform the first trajectory
*  into the second trajectory while staying on the surface of the donut. If I could sort of slice
*  through where the dough bit of the donut is, I could do that. I could sort of cut through the
*  bit that's not on the surface, but that's not allowed. So walking in the surface, once the ant
*  decides it's going clockwise rather than counterclockwise, those are different choices
*  that the ant can make. In fact, they're homotopically inequivalent, right? So because
*  you cannot continuously deform one into another. Right. And what's cool is you can actually
*  enumerate all of the different choices. So another different trajectory the ant could take is it
*  could walk the long way around. So let's say staying on the top and going clockwise or going
*  counterclockwise. Or it can do some sort of combination where it loops some number of times
*  through the center circle while also traversing the long way around. And there's a way to enumerate
*  all of these essentially different trajectories. What you need are two different integers,
*  essentially. One integer that's describing the number of times you go in a clockwise or
*  counterclockwise direction around the short loop. And then another integer is describing
*  the number of ways to go counterclockwise or clockwise, depending on whether it's positive
*  or negative around the long loop. And you can prove that this pair of integers enumerates all
*  possible trajectories. Right. Right. So on the sphere, it's actually quite a lot simpler. So
*  you can imagine any path the ant might take on the surface of a sphere from the North Pole to the
*  North Pole, kind of wandering around any which way. And you could kind of shrink that trajectory
*  in a continuous way so that it gets smaller and smaller and smaller. So if it in fact goes all
*  the way to the South Pole, maybe it shrinks a little bit so it only goes to the equator. And
*  then maybe it shrinks a little more so it stays north of the Tropic of Cancer and so on and so
*  forth. And eventually all of the trajectories are deformable to just the ant sitting at the North
*  Pole and never moving at all. So there there's only one trajectory that the ant can make. And
*  that's the proof somehow that these two spaces are not the same. Which is wonderful because
*  it took us on a little journey. I actually want to dig into this because on the one hand,
*  we're not surprised that the sphere and the torus are topologically different, but it was a bit of
*  an effort there to actually show it, right? Even in that case where we had things under control.
*  And in doing that, you know, you stumble across. So you ask the question, how many different ways
*  are there to sort of do this path that returns to itself? A loop, right? A closed circle in the space.
*  And in the case of the torus, you just uncovered this pair of integers. The number of times you go
*  around the short way, the number of times you go around the long way. And integers, not to get too
*  fancy about it, now that's algebra. That's not geometry or topology or anything. Like roughly
*  speaking, mathematicians are either geometers and they like space or they're algebraists and they
*  like equations, right? But an algebraic structure appeared here somehow. Right, I think, you know,
*  this is just the tale of complexity in the modern world. Like everybody has to be everything these
*  days. So even if you really, your heart isn't with geometry, you have to use some algebra. So.
*  Well, I want to just take advantage of your being here to dig into this a little bit more. I mean,
*  we asked this question about how many ways you can draw a circle, roughly speaking,
*  in the torus. And there's a lot of ways, but then there's this hidden structure in that if you have
*  a circle going around in one direction and another circle just doing the same thing,
*  you can add them together in some sense, right? And that's the beginning of algebra. Am I too
*  dramatic there? Yeah, that's exactly right. So a more, I mean, I've described this in describing
*  the fundamental group. I said, you know, let's imagine we have a home base point where they,
*  and we're going to consider the ant walking in these little loops from the home base to the home
*  base. But it's actually maybe more natural to not have a home base point because, you know, I don't
*  know where it would be on the surface of a torus, for instance. So another way to think about this
*  sort of algebraic structure is you can imagine an ant walking from any point P on the surface to any
*  other point Q on the surface. It, you know, takes some path and then later, you know, maybe the ant
*  is tired and it takes a nap, but then later it wakes up and then it walks from the point Q to some
*  other point R. And what you're referring to is you could then compose those two paths, compose those
*  two trajectories and then get a path directly from P to R. So if you can walk from P to Q and
*  walk from Q to R, you can compose those two walks and get from P to R. And that's the beginning.
*  So this is a composition operation on the paths and the surface of a torus or on any space, paths
*  in any space. And really the sort of invariant that more exactly describes the algebra that's
*  hidden in the geometry is something called the fundamental groupoid or the fundamental infinity
*  groupoid, which is not a group, which is a type of mathematical objects we teach undergraduates,
*  but an sort of infinite dimensional analog of a group, an infinity groupoid, which is a,
*  you know, sort of frontier of research level mathematics.
*  Right. I think that if, look, if people are going to listen to this entire podcast episode,
*  I want them to come away knowing what an infinity groupoid is. I think that's going to be something
*  that they'll be able to impress their friends with at cocktail parties and so forth. So you,
*  but to go very slowly to get there, you know, you mentioned the fundamental group,
*  which is the collection of the circles we started with. So what's a group?
*  Right. So a group is, I mean, a way to, I mean, this, like, there's this,
*  there's this metaphor of the blind man and the elephant and, you know,
*  somebody's holding, somebody's touching the trunk, somebody's touching one of the legs,
*  somebody's touching the tail and have a completely different perspective of it.
*  And that's, that's how I'm thinking about groups. So it's really hard to know,
*  know how to start. But, you know, a group in this context is a set here. It's the collection of all
*  different loops that a ant could take walking through some space together with composition
*  operation. So it's performing one loop and then following it by another loop that can be
*  understood as a loop, even though you come back through the center, it's still a loop.
*  And then satisfying some, you know, sort of very natural axioms. So if you're walking along a loop,
*  you could always reverse your trajectory and walk back in the other direction. And that's an undoing
*  somehow of the process. So every element in a group has an inverse that if you compose with it,
*  it gets back to sort of where you started. And a few sort of simple axioms like that.
*  So it's kind of a, it's a stripped down version of, you know, the integers or something like that,
*  right? Where the integers, you can add them together. So the integers are an example of a
*  group, right? Right. Integers with addition is an example of a group. Absolutely. That's right.
*  Not with multiplication. Matrices with multiplication is an example of a group.
*  Matrices with addition is an example of a group. So I have to say something about the dimension
*  to make those examples work. Okay. And the physicists love group theory because symmetries
*  are a group, right? Like rotations and translations and things like that. Yeah, absolutely. So another
*  perspective on groups, if we sort of move around the elephant is a group is an axiomatization of
*  the symmetries of an object. So the different configurations that an object might be. So let me
*  explain what a symmetry is. So imagine you have a twin mattress and you know that you're supposed
*  to kind of flip your mattress occasionally, because I guess it's good for the life of the mattress.
*  And so you might wonder like how many different ways are there to flip the mattress? How many
*  different configurations could the mattress be in? And well, it's the mattress, one option is
*  whatever the mattress is when you start it. Then you could sort of rotate it head to toe. So you're
*  sort of switching the head and the toe, but the top stays the same. That's one move. You could also
*  flip it sort of side to side. So I'm keeping the head at the head and the toe at the toe,
*  but I'm switching the top and the bottom. Yep. Or you could combine those two operations. And
*  the effect of this is the head is now where the toe was and the toes were the head and the top
*  and bottom surface of it has also flipped. So a group is recording on the one hand, the four
*  different positions that the mattress could be in, but also how these different flipping operations
*  that I described compose to each other. So each of those flips is an order two element of the group,
*  meaning if you perform the same move twice, you get the mattress back to where you started.
*  If you do any two different of the flips, you'll get the third one, which is not a typical property
*  of a group, but it's special to this one, which is goes by the name, the Klein four group.
*  This group does not have a generator, meaning that there's not one operation you can do over
*  and over again that will take you all the way through the group. And this is why it's hard
*  to remember how to flip your mattress because you have to remember sort of how you flipped it last
*  month so you don't just do the same operation again and get back to where you were the month before.
*  So the integers do have a generator. You just add one and then you can get all the integers,
*  either by doing that or undoing it. Add one or negative one, you get all the way through
*  everything. So yes, the integers are cyclic group, which have a single generator, absolutely,
*  but Klein four group is not. Right. So the integers may be to people who are not group theory
*  aficionados are a nice little paradigm, but it's important that groups can be very different.
*  This is a finite group, this mattress flipping group, right? How many elements are there in the
*  mattress? Four. Four elements. Okay. Yeah. All right. And there's, so I mean, these groups are
*  super cool and, you know, really tell you something profound about geometry. So you might have heard
*  of the platonic solids, which are the three dimensional figures that you can get by gluing
*  together regular two dimensional figures. So a regular two dimensional figure is like a triangle
*  or a square or a pentagon or a hexagon where all the sides have the same length, all the angles are
*  the same and so on and so forth. And, you know, there are infinitely many of these because there's
*  a heptagon and an octagon and an onagon, you know, for any natural number N you can get a
*  plain figure with N sides. So you might wonder how many of these regular platonic solids are,
*  you know, how many different shapes you can get by gluing together, say triangles or gluing together
*  squares or gluing together pentagons or, you know, gluing together hexagons maybe. And you can prove
*  in fact that there are only finitely many. In fact, there are five of them using group theory
*  by studying the symmetries, the sort of orthogonal groups, the Smith or the special orthogonal groups
*  that describe the different configurations of these hypothetical shapes before even knowing
*  they exist. You can limit the possible configurations. But clearly that's not what Plato did.
*  I don't know, maybe some somewhere like buried in Plato's intuition. But another fun fact is
*  the five, there's something called the tetrahedron, which is built from triangles. And then there's
*  the cube, which is, that's the most familiar one built from squares. Then there's the octahedron,
*  also built from triangles, and then the dodecahedron and the icosahedron. And even though I named five
*  things, in a sense, there's kind of only three of them because there's this duality relationship
*  between the platonic solids, which you might have seen if you take a cube. So it's got four,
*  sorry, its faces are squares. There are six of them, and they are glued together along
*  12 different edges, and there are eight corners. And what I'm going to do is I'm going to build a new
*  platonic solid by replacing each of the corners by a face, each face by a corner. And what you
*  get in that, just by kind of connecting everything up, is an octahedron, so one of the other platonic
*  solids. And so there's a duality relationship between the cube and the octahedron, and also
*  between the dodecahedron and the icosahedron, and between the tetrahedron and itself. And those are
*  reflected by their symmetry groups. So because of this duality relationship, the symmetry group that
*  describes the configurations of the cube is the same isomorphic to the same shape as this symmetry
*  group of the octahedron and so on. Anyone who played Dungeons and Dragons knows about the platonic
*  solids because they have the dice, but they don't know about the duality relations. So now that's
*  good. That's something else that they have in their bag now. I'm only going to do this at great
*  risk, but I figure like, all right, while we've talked about groups, why don't we also explain
*  rings and fields to the audience, since these are the other sort of algebraic structures that
*  mathematicians love to throw around? Yeah, absolutely. So I mean, what's funny is, you know,
*  after a while you kind of forget that these terms refer to other things. So I mean, you know, when
*  I say field, I mean, I definitely think about the mathematical field before I remember. That's like
*  also the thing that's out the window. But right. So a group is describing a setting where you have,
*  you know, collection of objects and you have one composition operation to combine them together.
*  So if we have the integers, we can think about addition. If you add two integers, you get another
*  integer. But, you know, there are other binary operations on the integers that come up, you know,
*  multiplication, for instance. And a ring is a setting where you have two operations, an addition
*  operation or an addition like operation and a multiplication like operation. And they interact
*  in ways that are sort of familiar for the integers. So if I, you can understand,
*  there's a distributivity property that says if I add two integers together and then I multiply
*  by something, it's the same as multiplying first and then adding. And there are a few axioms like
*  that. So what's cool about, I mean, you might ask like, why do we bother with like, everybody knows
*  what the integers are? Why do I need this abstract concept of a ring? And that's a totally fair
*  question. But a really fun, it's kind of interesting fact is there's a very deep analogy between the
*  integers and polynomials. So a polynomial is like, this is sort of the thing that you would
*  meet in a high school algebra class. So you have a variable x, an indeterminate variable x, and then
*  you can form a polynomial by sort of adding up x's and multiplying x's and then throwing in real
*  numbers as the coefficients. So the polynomial might be like 5x minus, or 5x plus, I don't know,
*  17x squared plus pi x cubed, because we can have real numbers as coefficients, minus three. So that's
*  a polynomial in a single variable x. And polynomials also form a ring. If you have two polynomials,
*  you can add them together. You can multiply them. There's sort of rules for doing this that you
*  might have learned in a high school algebra class. And those ring, the ring of polynomials
*  with coefficients in a field, which we'll get to what a field is later on, coefficients in
*  the real numbers. And the ring of integers are very, are very, quite similar as rings. They're both,
*  they have a division algorithm. You can do sort of long division with polynomials, like with rings.
*  So, I mean, that's the sort of thing that's of interest to mathematicians, are these kind of deep
*  analogies between structures that are superficially quite different.
*  And what's the difference between a ring and a field? Because they're kind of similar.
*  Right. So a field is like a ring. It has two binary operations. But if we go back to the ring
*  of integers, there's a pretty big difference between the addition rule and the multiplication rule.
*  So if I, in that, every addition, every element has an additive inverse. So if I pick my favorite
*  integer, you know, 17, there's another integer, negative 17, that when I add them together, I get
*  zero, which is the identity for the addition operation. But that doesn't work for multiplication.
*  If I pick my favorite integer again, 17, there's no integer I can multiply. And then I get zero.
*  And 17, there's no integer I can multiply 17 by to get back to one, which is the multiplicative identity.
*  Right. So that's what distinguishes a ring, where you don't necessarily have multiplicative
*  inverses from a field. In a field, you do have an inverse to both the multiplication and the
*  addition operation. You sort of assuming you're not trying to divide by zero, that never quite works.
*  So things like the rational numbers, which throw in these multiplicative inverses, or the real numbers,
*  are fields in addition to being rings. And does the existence of the number zero get you in trouble
*  because it doesn't have an inverse? Yeah, so in a field, you have to treat zero as a kind of special
*  case. So in a field, you have to, your zero and your one can't be the same. Otherwise, the whole
*  thing kind of collapses. And zero will not have a multiplicative inverse, but every other element
*  has to. Got it. Okay. And so when we started, we started this little journey, this little side track,
*  because we were thinking about the Taurus and its topology. And we found that the space of all the
*  little loops the ant could walk on formed a group. Are there examples where we associate rings or
*  fields with topological invariance? That's a good question. I don't know that that's commonly done.
*  And I think the reason is that groups are just so rich, you know. But, you know, a single group will
*  not capture the full data of a topological space. I mean, really what you have to do is have
*  introduced lots of different groups that are measuring lots of different things. So the
*  fundamental group tells you about sort of loops in the space and whether you can,
*  if you sort of walk along a circular path in the space, can you fill that in with a disc?
*  You know, could you, I guess I don't know how to say it any better than that.
*  That's a good way to say it. Can you contract it?
*  You know, if you have sort of a wire ring, is there, could you put sort of a soap bubble on
*  it somehow so that the surface of the soap bubble lives within the space that you were
*  talking about? So that's not possible if you're walking the short way around on a Taurus,
*  because the soap bubble would have to kind of cut through the dough, and that's not on the surface.
*  But it is on the surface of a sphere. You could just kind of, you know, paint over the disc.
*  Right.
*  So that's measuring this kind of one-dimensional holes, I guess, is the
*  area that's bounded by a one-dimensional sphere. But as we mentioned, there are kind of spheres in
*  higher dimensions. So you could ask if you have a balloon inside your surface, can that be filled in
*  with sand sort of staying within the surface? And that's a two-dimensional analog of the same
*  question, and there's a question like that in all positive integer dimensions. And that family of
*  groups describes the full homotopy type of a space. A single group does not, but if you have this sort
*  of infinitely many groups, it does. One of the things that I say just very casually to people
*  who are non-mathematicians is that you might think that mathematicians spend all their time thinking
*  about mathematical objects like spheres or Taurus's or whatever, but really they're thinking about maps
*  between the different objects. So I guess it's fair to say that first thing, the fundamental group
*  is maps from circles into the space you care about. Then there's the map, the set of maps from spheres,
*  and then the set of maps from three spheres, and it clearly generalizes to infinite numbers.
*  Yeah, absolutely. But there's something special about the groups. You don't get fields or rings,
*  which have two different binary operations on them. I guess the last thing that I have in that
*  angle is, is there something special about fields and rings that have two binary operations that
*  it's worth stopping there? Can we define three binary operations on a set and make hyper rings
*  or something like that? Sure. Algebra is a very flexible subject, and to define what an algebra
*  is in full generality, you need the collection of elements that you're considering, and then you can
*  specify arbitrarily many operations with arbitrary arities, and you can specify arbitrarily many
*  rules between them. The subject of universal algebra invites you to consider examples like that.
*  Let's invite listeners in the audience who are inclined in that direction to follow, study
*  universal algebras, but we're going to go back to the topology and the groups. You made a statement
*  there. I just want to make sure that I get it clear. If I figure out the set of all ways that
*  I can map circles and spheres and three-dimensional spheres, et cetera, into a space, I have not
*  specified its topology completely, but I've specified its homotopy type topology completely,
*  which is a slightly weaker thing. Is that right? That's right. Yeah. Okay. So do we know the answer
*  to the general question of how to completely specify the topology of a space? Right. So
*  the classical approach to that, and it's kind of a topology, but let's imagine it's a theorem as
*  opposed to a topology. I mean, if you restrict to sort of well-behaved spaces, it's a theorem, and
*  if you take general spaces, it's kind of a topology. So the classical approach to this is exactly
*  what you're saying. So you describe what's called the nth homotopy group as the collection of maps
*  from the n sphere into your space. And then because it's a group, you need a composition
*  operation, which for two spheres, I can describe the composition. So if I have a map from a
*  two-dimensional sphere into a space and a map from another two-dimensional sphere into the space,
*  and these maps are based, so there's the kind of North Pole, and they send them to the same point
*  in the space. You could imagine taking another two-dimensional sphere and then collapsing the
*  equator to a single point. So if you had a balloon and you collapse the points on the equator,
*  you sort of squeeze at them carefully so it doesn't pop, and so now you have a single point.
*  Now what you look like is something that's called a bouquet of spheres. It's sort of two different
*  spheres that are glued together along the point where the equator used to be, and you could sort
*  of map from that into the space because you have two different maps into the space that
*  have a common point, and sort of the combination of that operation is how you define the composition
*  here. And so there's an analog of that in all dimensions. So this is the classical approach
*  to saying what is a space algebraically? What are some algebra stuff that tell you everything
*  that you would want to know about the homotopy type of the space? But a modern approach goes
*  back to the idea of the fundamental group but replaces it by something called the fundamental
*  infinity groupoid. And since I promised I would tell the listeners what an infinity groupoid is,
*  let me do it now. So I like this because this feels like a kind of much more natural way to
*  describe the space. And again, the fundamental groupoid, depending on your point of view,
*  either it's a theorem or it's a tautology, really does capture the full homotopy type of the space.
*  So what is it? So it's some algebraic structure where I'm going to start with the set of all
*  points in the space. So I've forgotten the topology, I've forgotten about distances and
*  stuff, I'm just remembering the set of points. Because in algebra I have sort of sets and stuff,
*  I don't have geometry, so I just remember the set of the points in the space. Then what I'm going to
*  throw in is the data of every possible path between any points in the space. This is going to be a
*  very big thing, by the way. So we recover now every possible path that an ant could take between
*  points in the space, plus the composition. And by the way, I mean, I gotta say that mathematicians
*  use the word data in a different sense than physicists use it. Oh yeah, I mean, all of our
*  sets are infinite, it's fine. No problems here. But when you say like the data of a path, you mean
*  whatever information is required to specify that path among the space of all the paths?
*  Right, so we have all the points in the space, we have all the paths in the space. Now when we were
*  thinking about paths before, when we were talking about the torus, we were talking about, you know,
*  we only want to consider paths up to being essentially the same, sort of continuously
*  deformable. We're not doing that here, we're literally remembering every single path, every
*  path is a distinct path. But we are also going to remember data of these continuous deformations.
*  So there's a notion of path between paths. If a path is a map from an interval into the space,
*  this is a continuous map from a square into the space. An interval times an interval is a square,
*  and so a map from a square into space can be understood as a path between paths, sort of where
*  one edge goes as one path, where the other edge goes as the other path, and then the sort of other
*  direction, the other dimension is giving the kind of path between paths. So we're going to remember
*  all of those as well, all of these paths between paths, so these are called homotopies. And then
*  there's no reason to stop at two dimensions, so we could take three intervals, producted together,
*  that's a cube, and remember all of those maps into the space. These are paths between paths between
*  paths, and then we could take paths between paths between paths between paths, and paths between
*  paths between paths between paths between paths, and all the way up, and that goes to infinity,
*  that's the infinity groupoid. So that data, I mean this feels like it's maybe not an improvement,
*  but somehow. Yeah, it's something. Somehow that algebraic structure,
*  both describes the full homotopy type of a space, which is a useful way to think about it, but also
*  invites you to imagine a generalization to a different world that's further removed from
*  the geometry, where you can imagine some of these paths are no longer invertible anymore,
*  these are sort of one-way paths. You might not be able to go backwards for whatever reason,
*  and this is now the world of infinite dimensional category theory, and that's really where I work.
*  Well, so which brings up a couple, there's a couple things I just got to clean up there,
*  you were on a roll, so I just wanted to let you keep going. But one thing is just to remind
*  folks, when you talked about the path between two paths, right, the cube, sorry, the square
*  that was a map into it, that path between two paths might not exist. If the two paths are not
*  homotopically equivalent, that there won't be any path between them, so there's some structure in
*  the space of what paths between paths exist. Right, by what's present and what's absent,
*  that's a beautiful way to say it. Good. And the other one was, this is a little bit off topic,
*  but when you did the explanation of the sphere and you squeezed it down at the equator to get
*  the bouquet, not only is the language very beautiful, but the visualization is very
*  compelling. And one thing that always gets asked, how do you visualize the infinity groupoid? Is
*  that something that is necessary for you to do? Do you approximate infinity by two or is there
*  some other trick? It's hard. I don't know. I mean, you sort of imagine a little piece of it at a time
*  and then, I don't know. Yeah, it's hard. Okay, that's fair, completely fair. I basically give
*  the same answer. I say you don't. You do the two-dimensional or three-dimensional examples
*  you can get, but at some point you have to trust the equations you're pushing around. And I don't
*  think we've quite elaborated the difference between a group and a groupoid.
*  Right, so the difference between a group is, so the example of a fundamental group, the elements
*  of the group are actually the loops themselves. We've kind of fixed, as prior we've given data,
*  the home base point for the ant, and then the only further data we record are the loops in the space.
*  So in a groupoid, you don't fix a base point. You allow different base points, so the different
*  points on the surface of, or in the space. And so now you have kind of two levels of data. You have
*  the collection of different points and then you also have the paths between the different points.
*  Okay. Is this, I mean, outside of the world of topology and homotopy, are there groupoids? I mean,
*  physicists use groups all the time, right? SU3 cross SU2 cross SU1 is the symmetry group of the
*  standard model of particle physics. We never use the word groupoid unless we're secretly mathematicians.
*  So just in the abstract sense, is there a difference? Yeah, sure. So your groups are all
*  automorphism groups of some object, and it's a fixed object. So you're thinking about automorphisms
*  of R3 or automorphisms of R4 or sort of R3 with a chosen orientation or something like that. So
*  your groups were all automorphism groups of a fixed object. In a groupoid, you have different
*  objects. So there's not just one object anymore. There are different objects, and it's exactly the
*  many object analog of a group. Okay, I see. That's not so bad. And automorphism is just a map from a
*  space to itself. Is that right? Yeah. Okay, good. Yeah. Yeah. Sorry. We all know what automorphisms
*  are. I'm sorry about that. No, of course. So then, okay, good. Sorry. There's a lot of clarifying
*  questions. But then let's get back to the punchline here. The infinity groupoid, the sort of
*  topological sense of all the different paths that we can map into the space and the paths between the
*  paths and paths between the paths of paths. So if we knew the infinity groupoid of a space, we would
*  know what? Everything. Everything. Well, everything if you only care about the space up to homotopy.
*  I mean, if you're willing to say that n-dimensional Euclidean space is the same as a point, there's no
*  difference whatsoever. Then yes, you know everything about the space. Now, I mean, if you care about
*  geometry or dimension or things like that, then this is not the right point of view. But that's okay.
*  But for the torus, when you said, let's calculate the fundamental group, and we noticed that it
*  looked like, so for the sphere, the fundamental group is as trivial as this one element. For the
*  torus, it's two copies of the integers. So it's basically two integers you just give me. How do I
*  even express what the infinity groupoid of a space is? Right. So let me move back to the sphere
*  because the two sphere, because it's a little easier to describe here. So if we're thinking
*  about the loops in the two sphere or the paths in the two sphere, there's kind of nothing interesting
*  to say. If you have any two points on the, sorry, the two sphere is the ordinary sphere. If you have
*  any two points on the sphere, you can connect them by a path. And there's a sense in which all paths
*  are the same. You could continuously deform any path from X to Y into any other path from X to Y.
*  But now if we think about these two dimensional paths between paths, there are fundamentally
*  different ones. And this is really surprising. So in one dimension, all paths are somehow the same.
*  On the sphere. But in two dimensions, paths can be quite different. So I want to think about paths
*  between paths. And so I should fix the two paths first. So let's start at the
*  North Pole and the South Pole. So these will be paths from the North Pole to the South Pole.
*  And one of the paths I want to take is the International Dateline. So somewhere through
*  the Pacific Ocean. And the other path I want to take is the Prime Meridian, which is, I don't
*  know, it's through England or something like that. Through Greenwich, yeah. Okay, somewhere else. So
*  there's the Greenwich one and the Pacific Ocean. So those are both paths from the North Pole to the
*  South Pole. Now a path between paths is a continuous map from a square onto the surface of the Earth
*  that sends one edge to the Prime Meridian and the other edge to the International Dateline.
*  And one of them is the one that would cover Asia, that would go east from the Prime Meridian to the
*  International Dateline. And the other one is the one that would cover the New World. So go west.
*  And those are fundamentally different in the sense that there is no three-dimensional path,
*  no path between paths between paths that continuously deforms the one to the other.
*  If you could pass through the core of the Earth, you could do that, but we have to stay on the
*  surface. It's not allowed. So in this sense, the fundamental group or the fundamental group or the
*  sort of one-dimensional thing does not describe everything that's going on on the surface of the
*  sphere. But once we allow these higher dimensional things, we do get everything. And it's your,
*  is the kind of day job that you're involved in more actually calculating the fundamental,
*  the infinity groupoid of this or that, or is it more proving theorems about properties of
*  infinity groupoids? Right. So that's a great question because those are both very active
*  areas. There are a lot of researchers working on both problems. I don't do the calculations myself.
*  They're very hard. I do kind of the theory side, but some of my colleagues work on the calculations.
*  I'm sure it makes everyone feel good that you don't really do the hard part. You're just doing
*  the simple part of proving theorems about infinity groupoids. Right. And it also, this discussion is
*  wonderful because it does, beneath the surface in the language that you use and the way you talk
*  about it, the role of the maps between the different spaces really shines through. Just
*  think of all the spaces you can invent and all the different ways you can map them in some sense.
*  And that sneaks us up into the topic of category theory, which is not really our focus here,
*  but I don't want to leave the audience completely bereft of category theory while we're here. So
*  how do we get from topology to category theory? Sure. I mean, again, there's lots of different
*  roots in, but maybe the one that's most relevant to this conversation, and this is kind of back to
*  this, back to the conversation and philosophy that we started off with is, so the fundamental
*  theorem and category theory, or somehow that's expressing the core philosophy of category theory,
*  this thing called the Yenata Lemma says that if you have any sort of mathematical object, it could
*  be a topological space or it could be a vector space or it could be a ring or it could be a field
*  or whatever, any sort of mathematical object, you can understand everything that you want to know
*  about it by considering the other objects of that same type, so other spaces or other rings or other
*  fields and the maps between them. Oh my goodness. Right. So what this is saying in the case of spaces
*  is that if you have unknown space X and you're trying to understand that space, so we don't know
*  sort of what its dimensions are, what its points are, we don't know anything about it,
*  a theorem in category theory, the Yenata Lemma says that you can completely characterize your
*  unknown space by considering the other spaces, so all these spheres and tori and other surfaces
*  and whatever in all dimensions and then the continuous maps from that into your space X.
*  Well, okay. But what's cool about that result, so we were using this idea in topology already
*  to understand spaces, but what's cool is it's completely independent of the mathematical
*  context, so the same theorem is true for rings, you can understand a ring by thinking about other
*  rings and the ring homomorphisms between them, you can understand a group by thinking about other
*  groups and the group homomorphisms between them, this works in any mathematical context whatsoever.
*  It's again a little bit related to some ideas in physics that we should always be talking about
*  relations between different things rather than intrinsic essences of things themselves, so.
*  Yeah, absolutely. And why is this called category theory? Like let's just bite the
*  bullet and tell people what a category is maybe. Sure, so I mean a category is kind of like a very
*  general template for a mathematical theory, so Barry Mazer has this metaphor, it's like something
*  with nouns and verbs, so a category is given by a collection of objects, these are the nouns,
*  and what you should think of here are like all the rings, all the possible rings, so the integers and
*  the rationals and the polynomials and matrices and blah blah blah, so all the rings. And then
*  you also have the sort of functions between them, so in the case of rings these would be functions
*  that respect the addition and multiplication laws, in the case of spaces these would be continuous
*  functions, and sort of that totality of information, the objects like the spaces and the functions, the
*  continuous functions or maps between them and their composition and so on, that's a category.
*  And what's great about this is every word you say makes perfect sense, and at the end I'm left not
*  quite knowing what the implications of these ideas are, and that's where that's the devil being the
*  details, right? You've ascended to this platonic realm of wonderful abstraction where there's just
*  things and maps between them, so how do you, what's the usefulness, what's the caching out of this,
*  what is the free market value of a good category theory? Right, so I mean one nice thing about
*  category theory is you can just say when two categories are the same in an essential sense,
*  so there's a notion of equivalence between categories, and I'll give you my favorite example,
*  so there's a category whose objects are vector spaces, which are something that are kind of
*  fundamental in sort of modern quantum physics, so a vector space is like a collection of vectors
*  with vector addition and scalar multiplication, and then the sort of transformations between vector
*  spaces are called linear transformations, so this is kind of a bread and butter category,
*  objects are vector spaces, the maps are transformations, which are some sort of
*  functions between these vector spaces. Now there's another category that's kind of a lot simpler to
*  define, so the objects in this category are just natural numbers, so there I know exactly how many
*  objects there are, each natural number is an object, there are no other objects, that's it,
*  and now I need to say sort of what an transformation is. Sorry, the natural numbers are 0, 1, 2, 3, the positive,
*  non-negative integers. Absolutely, okay, so now I need to say what a sort of transformation or what
*  an arrow is from one number, let's say 5, to another number 8, and what it is is it's going
*  to be an 8 by 5 matrix, so to make something a category I need to tell you about the objects
*  and the arrows between them, and that's what I've done, the natural numbers are the objects, the
*  matrices are the arrows, but you also need a composition law, so I need a way to take a 5
*  by 8 matrix and an 8 by 7 matrix and produce a 5 by 7 matrix, but there's a thing for that,
*  it's called matrix multiplication, it's an operation that satisfies the axioms of category,
*  so those are two very different sounding categories, on the one hand I have this like
*  very abstract, you know, very large thing of all vector spaces and all linear transformations
*  between them, and then on the other hand I have this kind of toy category with natural numbers
*  matrices, and those categories are equivalent, so in other words you can think of the natural
*  number as a stand-in for a vector space, the number 5 corresponds to five-dimensional Euclidean space.
*  I was going to guess that, I promise, yes. Yeah, and you can think of matrix as a stand-in for
*  linear transformations, so if you have vector spaces and you choose a basis then you can use
*  those bases to get a matrix of numbers that encodes the full data of the linear transformation,
*  and so in a mathematics department we often teach linear algebra in kind of two different tracks,
*  there's a sort of computational linear algebra, if you're going to be, you know, the next founder
*  of Google you need to learn how to use these matrix operations and you'll take that sort of course,
*  or there's a theoretical linear algebra that's, you know, taken maybe by more math majors, and
*  this, on the ground the subjects feel very different because one you're learning a lot
*  about matrices and reduction and operations, and then the other you're learning this theory about
*  linear independence and bases and so on and so forth, but it's the same subject because they're,
*  these are equivalent categories. Okay, that is actually a very good example of like a little
*  useful bit of insight that you get from thinking this way, so just, I know that this has sort of
*  already been said by you, but let me try to say it again to drive home this notion of a category
*  to people who don't use it as bread and butter, because when you say a vector space,
*  let's just imagine, let's optimistically imagine everyone knows what a vector space is, right,
*  they have in their mind x, y axes and little vectors, so a vector space is itself a collection
*  of things, right, the vectors, there's an infinite number of vectors in the vector space, but the
*  category is of vector spaces, so the individual elements of the category are the whole vector
*  space, a two-dimensional vector space, a three-dimensional vector space, etc., and you're
*  thinking about the maps between vector spaces and then extra maps between the set of all vector
*  spaces and the set of all integers and things like that, so it gets pretty unvisualizable pretty
*  quickly, but that's why you get paid the big bucks. Well, the visual is you're sort of zooming out,
*  you're really taking a bird's-eye view of mathematics, or you know, the objects that
*  you know group theorists would study are really just little atoms inside the category of all
*  groups, and what's fun is if you're a category theorist or a higher dimensional category theorist,
*  really the categories themselves become very small, so in my work I zoom out one other level
*  and I think about categories whose objects are categories, and so those categories are things
*  like the category of vector spaces and then some vector spaces, an actual vector space which has
*  uncountably infinitely many vectors in it as you point out, so. And so at what point do we get to
*  the infinity categories? There's an infinity group or there must be an infinity category, right?
*  Yeah, sure. I mean, yeah, you know, as every decade mathematicians invent more complicated objects to
*  study and the universes where those objects live are categories with more dimensions of morphisms
*  between them, and those are these infinity categories. I mean, just knowing that, can you
*  foresee what was going to be invented in the next decade? Like what is the obvious thing to like
*  draw more arrows between? Yeah, I mean, what I'm hoping happens in the future is that we change
*  our foundation system of mathematics, so it's kind of more suitable to these complicated up-to-home
*  atopy structures that we're thinking about today. Well, maybe this is a good place to end up, because
*  in some sense, like this all, it's kind of fun, like you and I are both in the small group of
*  people who just think it's fun thinking about this stuff, right? But it's also maybe a shift
*  of perspective on what math is, right? And in changing what we mean by equality and equivalence
*  and things like that. And so can you imagine that math is going to look very different down the road
*  when this really seeps in? Is it kind of like a shift from classical mechanics to quantum mechanics
*  in some sense? Yeah, I think so. I think we maybe see glimpses of it today, but I think
*  every living mathematician would be very surprised by 22nd century mathematics, and
*  I hope to be around to see some of it. Well, I was very interested to read this wonderful interview
*  with you in Quantum Magazine, and one of the interesting things you're doing is writing books.
*  I mean, maybe you count them as textbooks, but anyway, technical mathematical books where,
*  correct me if I'm saying this wrong, but you were just as interested in reproving known theorems
*  in better ways as improving new theorems, which is supposed to be the typical thing mathematicians
*  are paid to do. Right. And, you know, there's this Bill Thurston, who is this wonderful topologist
*  geometer, drew attention to, you know, kind of the role that mathematicians need to play in making
*  mathematics understandable to humans, you know. So, you know, because something has been proven,
*  that means it's true, which, you know, a nice thing about mathematics is the theorems that were
*  proven 2000 years ago are equally true today. But that doesn't necessarily mean that it's
*  understandable by somebody who wants to build on those ideas and use them to do something else.
*  So I think it is worthwhile to do a bit of, you know, kind of tidying up and repackaging,
*  streamlining, you know, a wonderful success in the history of mathematics is, you know,
*  these cutting edge discoveries that were, you know, kind of very controversial or inconceivable
*  to somebody 100 years ago are now stuff we teach undergraduates in their first and second year.
*  True, right. I mean, there's a lot of controversy over calculus, right? That was considered hard.
*  Right. These pinnacles of human achievement are now something that, you know,
*  thousands and hundreds of thousands of students are learning every single year. And I hope we
*  continue to progress in that way. We should check back 30 years from now. We'll have you back on the
*  podcast and we'll check to see whether or not category theory is taught to at least
*  undergraduates, at least first year students in the math classes. So that's something to
*  look forward to. Emily Reel, thanks very much for being on the Mindscape podcast.
*  Great. Thanks for having me.

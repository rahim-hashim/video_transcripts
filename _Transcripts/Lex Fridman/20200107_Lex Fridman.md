---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 3765s
Video Keywords: []
Video Views: 556967
Video Rating: None
Video Description: 
---

# Grant Sanderson 3Blue1Brown and the Beauty of Mathematics  Lex Fridman Podcast #64
**Lex Fridman:** [January 07, 2020](https://www.youtube.com/watch?v=U_lKUK2MCsg)
*  The following is a conversation with Grant Sanderson.
*  He's a math educator and creator of 3Blue1Brown,
*  a popular YouTube channel that uses programmatically animated visualizations
*  to explain concepts in linear algebra, calculus, and other fields of mathematics.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  give it five stars on Apple Podcasts, follow on Spotify, support on Patreon,
*  or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N.
*  I recently started doing ads at the end of the introduction. I'll do one or two minutes
*  after introducing the episode and never any ads in the middle that can break the flow of the
*  conversation. I hope that works for you and doesn't hurt the listening experience.
*  This show is presented by Cash App, the number one finance app in the app store.
*  I personally use Cash App to send money to friends, but you can also use it to buy,
*  sell, and deposit Bitcoin in just seconds. Cash App also has an investing feature.
*  You can buy fractions of a stock, say $1 worth, no matter what the stock price is.
*  Broker services are provided by Cash App Investing, a subsidiary of Square, and Member SIPC.
*  I'm excited to be working with Cash App to support one of my favorite organizations called FIRST,
*  best known for their FIRST Robotics and LEGO competitions. They educate and inspire hundreds
*  of thousands of students in over 110 countries and have a perfect rating at Charity Navigator,
*  which means the donated money is used to maximum effectiveness.
*  When you get Cash App from the app store at Google Play and use code LexPodcast, you'll get $10,
*  and Cash App will also donate $10 to FIRST, which again is an organization that I've personally seen
*  inspire girls and boys to dream of engineering a better world. And now here's my conversation
*  with Grant Sanderson. If there's intelligent life out there in the universe, do you think
*  their mathematics is different than ours? Jumping right in. I think it's probably very different.
*  There's an obvious sense. The notation is different, right? I think notation can guide what
*  the math itself is. I think it has everything to do with the form of their existence, right?
*  Do you think they have basic arithmetic? Sorry to interrupt.
*  Yeah. So I think they count, right? I think notions like one, two, three, the natural numbers,
*  that's extremely, well, natural. That's almost why we put that name to it. As soon as you can count,
*  you have a notion of repetition, right? Because you can count by two, two times or three times.
*  And so you have this notion of repeating the idea of counting, which brings you addition
*  and multiplication. I think the way that we extend to the real numbers, there's a little
*  bit of choice in that. So there's this funny number system called the surreal numbers
*  that it captures the idea of continuity. It's a distinct mathematical object. You could very well
*  model the universe and motion of planets with that as the back end of your math, right? And you still
*  have kind of the same interface with the front end of what physical laws you're trying to,
*  or what physical phenomena you're trying to describe with math. And I wonder if the little
*  glimpses that we have of what choices you can make along the way based on what different
*  mathematicians have brought to the table is just scratching the surface of what the different
*  possibilities are. If you have a completely different mode of thought, right? Or a mode
*  of interacting with the universe. And you think notation is a key part of the journey that we've
*  taken through math. I think that's the most salient part that you'd notice at first. I think
*  the mode of thought is going to influence things more than the notation itself. But
*  notation actually carries a lot of weight when it comes to how we think about things,
*  more so than we usually give it credit for. I would be comfortable saying.
*  Do you have a favorite or least favorite piece of notation in terms of its effectiveness?
*  Yeah, well, so least favorite, one that I've been thinking a lot about that will be a video,
*  I don't know when, but we'll see. The number E. We write the function E to the X, this general
*  exponential function with a notation E to the X that implies you should think about a particular
*  number, this constant of nature, and you repeatedly multiply it by itself. And then you say, oh,
*  what's E to the square root of two? And you're like, oh, well, we've extended the idea of
*  repeated multiplication. That's all nice. That's all nice and well. But very famously,
*  you have like E to the pi I, and you're like, well, we're extending the idea of repeated
*  multiplication into the complex numbers. Yeah, you can think about it that way. In reality,
*  I think that it's just the wrong way of notationally representing this function,
*  the exponential function, which itself could be represented a number of different ways.
*  You can think about it in terms of the problem it solves, a certain very simple differential
*  equation, which often yields way more insight than trying to twist to the idea of repeated
*  multiplication, like take its arm and put it behind its back and throw it on the desk and
*  be like, you will apply to complex numbers, right? That's not, I don't think that's pedagogically
*  helpful. And so the repeated multiplication is actually missing the main point, the power of
*  E to the S. I mean, what it addresses is things where the rate at which something changes
*  depends on its own value, but more specifically, it depends on it linearly. So for example,
*  if you have like a population that's growing and the rate at which it grows depends on how many
*  members of the population are already there, it looks like this nice exponential curve.
*  It makes sense to talk about repeated multiplication because you say how much is there
*  after one year, two years, three years, you're multiplying by something. The relationship can
*  be a little bit different sometimes where let's say you've got a ball on a string, like a game
*  of tether ball going around a rope, right? And you say its velocity is always perpendicular to its
*  position. That's another way of describing its rate of change as being related to where it is,
*  but it's a different operation. You're not scaling it. It's a rotation. It's this 90 degree rotation.
*  That's what the whole idea of complex exponentiation is trying to capture,
*  but it's obfuscated in the notation when what it's actually saying, like if you really
*  parse something like E to the pi i, what it's saying is choose an origin, always move perpendicular
*  to the vector from that origin to you, okay? Then when you walk pi times that radius, you'll be
*  halfway around. That's what it's saying. It's kind of the, you turn 90 degrees and you walk,
*  you'll be going in a circle. That's the phenomenon that it's describing, but trying to twist the idea
*  of repeatedly multiplying a constant into that. I can't even think of the number of human hours,
*  of intelligent human hours that have been wasted trying to parse that to their own liking and desire
*  among scientists or electrical engineers or students, which if the notation were a little
*  different or the way that this whole function was introduced from the get-go were framed differently,
*  I think could have been avoided, right? And you're talking about the most beautiful equation
*  in mathematics, but it's still pretty mysterious, isn't it? You're making it seem like it's a notation.
*  It's not mysterious. I think the notation makes it mysterious. I don't think it's,
*  I think the fact that it represents, it's pretty. It's not like the most beautiful thing in the world,
*  but it's quite pretty. The idea that if you take the linear operation of a 90 degree rotation
*  and then you do this general exponentiation thing to it, that what you get are all the other kinds
*  of rotation, which is basically to say if your velocity vector is perpendicular to your position
*  vector, you walk in a circle. That's pretty. It's not the most beautiful thing in the world,
*  but it's quite pretty. The beauty of it, I think, comes from perhaps the awkwardness of the notation
*  somehow still nevertheless coming together nicely because you have several disciplines coming
*  together in a single equation in a sense, historically speaking. That's true. So the
*  number E is significant. It shows up in probability all the time. It shows up in
*  calculus all the time. It is significant. You're seeing it mated with pi, this geometric constant,
*  and I, the imaginary number and such. I think what's really happening there is the way that E
*  shows up is when you have things like exponential growth and decay. It's when this relation that
*  something's rate of change has to itself is a simple scaling. A similar law also describes
*  circular motion. Because we have bad notation, we use the residue of how it shows up in the context
*  of self-reinforcing growth, like a population growing or compound interest. The constant
*  associated with that is awkwardly placed into the context of how rotation comes about because they
*  both come from pretty similar equations. And so what we see is the E and the pi juxtaposed
*  a little bit closer than they would be with a purely natural representation, I would think.
*  Here's how I would describe the relation between the two. You've got a very important function we
*  might call exp, that's like the exponential function. When you plug in one, you get this
*  nice constant called E that shows up in probability and calculus. If you try to move in the imaginary
*  direction, it's periodic and the period is tau. So those are these two constants associated with
*  the same central function, but for kind of unrelated reasons, right? Not unrelated, but
*  orthogonal reasons. One of them is what happens when you're moving in the real direction. One's
*  what happens when you move in the imaginary direction. And like, yeah, those are related.
*  They're not as related as the famous equation seems to think it is. It's sort of putting all
*  of the children in one bed and they'd kind of like to sleep in separate beds if they had the choice,
*  but you see them all there and there is a family resemblance, but it's not that close.
*  So actually, thinking of it as a function is the better idea. And that's a notational idea.
*  And yeah, and like, here's the thing. The constant E sort of stands as this numerical
*  representative of calculus, right? Calculus is the study of change. So at the very least,
*  there's a little cognitive dissonance using a constant to represent the science of change.
*  I never thought of it that way. Yeah. Right?
*  Yeah. It makes sense why the notation came about that way, because this is the first way that we
*  saw it in the context of things like population growth or compound interest. It is nicer to think
*  about as repeated multiplication. That's definitely nicer, but it's more that that's
*  the first application of what turned out to be a much more general function that maybe the
*  intelligent life your initial question asked about would have come to recognize as being much more
*  significant than the single use case, which lends itself to repeated multiplication notation.
*  But let me jump back for a second to aliens and the nature of our universe. Okay.
*  Uh, do you think math is discovered or invented? So we're talking about the different kind of
*  mathematics that could be developed by the alien species. The implied question is, is, um, yeah,
*  is math discovered or invented is, you know, is fundamentally everybody going to discover the same
*  principles of mathematics? Uh, so the way I think about it, and everyone thinks about it differently,
*  but here's my take. I think there's a cycle at play where you discover things about the universe
*  that tell you what math will be useful. And that math itself is invented in a sense,
*  but of all the possible maps that you could have invented, it's discoveries about the world that
*  tell you which ones are. So like a good example here is, um, the Pythagorean theorem. When you
*  look at this, do you think of that as a definition or do you think of that as a discovery? From the
*  historical perspective, right? It's a discovery because they were, but that's probably because
*  they were using physical object to build their intuition. And from that intuition came the
*  mathematics. So the mathematics wasn't in some abstract world detached from the physics, but
*  I think more and more math has become detached from, you know, when you even look at modern
*  physics from, from string theory to even general relativity, I mean, all math behind the 20th and
*  21st century physics kind of, uh, takes a brisk walk outside of what our mind can actually even
*  comprehend in multiple dimensions. For example, anything beyond three dimensions, maybe four
*  dimensions. No, no, no. Higher dimensions can be highly, highly applicable. I think this is a common
*  misinterpretation that if you're asking questions about like a five dimensional manifold,
*  that the only way that that's connected to the physical world is if the physical world is itself
*  a five dimensional manifold or includes them. Well, wait, wait, wait a minute. Wait a minute.
*  You're telling me you can imagine, uh, uh, a five dimensional manifold. No, no, that's not what I
*  said. I, I, I, I would make the claim that it is useful to a three dimensional physical universe
*  despite itself not being three dimensional. So it's useful meaning to even understand a three
*  dimensional world. It'd be useful to have five dimensional manifolds. Absolutely. Because of
*  state spaces. But you're saying there in some, in some deep way for us humans, it does,
*  it does always come back to that three dimensional world for the use of usefulness at the
*  dimensional world. And therefore it starts with a discovery, but then we invent the mathematics that,
*  um, helps us make sense of the discovery in a sense. Yes. I mean, just to jump off of the
*  Pythagorean theorem example, it feels like a discovery. You've got these beautiful geometric
*  proofs where you've got squares and you're modifying the areas. It feels like a discovery.
*  If you look at how we formalize the idea of 2d space as being R2, right? All pairs of real
*  numbers and how we define a metric on it and define distance, you're like, hang on a second,
*  we've defined a distance so that the Pythagorean theorem is true. So that, and suddenly it doesn't
*  feel that great. But I think what's going on is the thing that informed us what metric to put
*  on R2 to put on our abstract representation of 2d space came from physical observations.
*  And the thing is there's other metrics you could have put on it. We could have consistent math
*  with other notions of distance. It's just that those pieces of math wouldn't be applicable to
*  the physical world that we study because they're not the ones where the Pythagorean theorem holds.
*  So we have a discovery, a genuine bona fide discovery that informed the invention,
*  the invention of an abstract representation of 2d space that we call R2 and things like that.
*  And then from there, you just study R2 as an abstract thing that brings about more ideas
*  and inventions and mysteries, which themselves might yield discoveries. Those discoveries might
*  give you insight as to what else would be useful to invent. And it kind of feeds on itself that way.
*  That's how I think about it. So it's not an either or it's not that math is one of these
*  or it's one of the others at different times, it's playing a different role.
*  So then let me ask the Richard Feynman question then along that thread. What do you think is the
*  difference between physics and math? There's a giant overlap. There's a kind of intuition
*  that physicists have about the world that's perhaps outside of mathematics. It's this
*  mysterious art that they seem to possess, we humans generally possess. And then there's the
*  beautiful rigor of mathematics that allows you to, I mean, just like as we were saying,
*  invent frameworks of understanding our physical world. So what do you think is the difference
*  there and how big is it? Well, I think of math as being the study of abstractions over patterns
*  and pure patterns in logic. And then physics is obviously grounded in a desire to understand
*  the world that we live in. I think you're going to get very different answers when you talk to
*  different mathematicians because there's a wide diversity in types of mathematicians. There are
*  some who are motivated very much by pure puzzles. They might be turned on by things like combinatorics
*  and they just love the idea of building up a set of problem-solving tools applying to
*  pure patterns. There are some who are very physically motivated, who try to
*  invent new math or discover math in veins that they know will have applications to physics or
*  sometimes computer science. And that's what drives them. Like chaos theory is a good example
*  of something that's pure math. It's purely mathematical. A lot of the statements being made,
*  but it's heavily motivated by specific applications to largely physics. And then you have a type of
*  mathematician who just loves abstraction. They just love pulling into the more and more abstract
*  things, the things that feel powerful. These are the ones that initially invented like topology,
*  and then later on get really into category theory and go on about infinite categories and whatnot.
*  These are the ones that love to have a system that can describe truths about as many things
*  as possible. People from those three different veins of motivation into math are going to give
*  you very different answers about what the relation at play here is. Because someone like
*  Vladimir Arnold, who's written a lot of great books, many about like differential equations and
*  such, he would say math is a branch of physics. That's how he would think about it. And of course,
*  he was studying like differential equations related things, because that is the motivator
*  behind the study of PDEs and things like that. But you'll have others who, like especially the
*  category theorists, who aren't really thinking about physics necessarily. It's all about
*  abstraction and the power of generality. And it's more of a happy coincidence that that ends up
*  being useful for understanding the world we live in. And then you can get into like, why is that
*  the case? It's sort of surprising that that which is about pure puzzles and abstraction
*  also happens to describe the very fundamentals of quarks and everything else.
*  So why do you think the fundamentals of quarks and the nature of reality is so compressible
*  into clean, beautiful equations that are for the most part simple, relatively speaking, a lot simpler
*  than they could be. So you have, we mentioned somebody like Steven Wolfram, who thinks that
*  sort of there's incredibly simple rules underlying our reality, but it can create arbitrary
*  complexity. But there is simple equations. What I'm asking a million questions that nobody knows
*  the answer to. I have no idea. Why is it simple? It could be the case that there's like a
*  filtration at play. The only things that physicists find interesting are the ones that are simple
*  enough they could describe it mathematically. But as soon as it's a sufficiently complex system,
*  like, that's outside the realm of physics, that's biology or whatever have you. And of course,
*  that's true. Maybe there's something where it's like, of course there will always be some
*  thing that is simple when you wash away the non-important parts of whatever it is that you're
*  studying. Just from an information theory standpoint, there might be some like,
*  you get to the lowest information component of it. But I don't know, maybe I'm just having a really
*  hard time conceiving of what it would even mean for the fundamental laws to be intrinsically
*  complicated. Like some set of equations that you can't decouple from each other.
*  Well, no, it could be that sort of we take for granted that the laws of physics, for example,
*  are for the most part the same everywhere or something like that, right? As opposed to
*  the sort of an alternative could be that the rules under which the world operates is different
*  everywhere. It's like a deeply distributed system where everything is just chaos. Not in a strict
*  definition of chaos, but meaning like just it's impossible for equations to capture,
*  to explicitly model the world as cleanly as the physical does. I mean, we're almost taking it for
*  granted that we can describe, we can have an equation for gravity, for action at a distance.
*  We can have equations for some of these basic ways the planets move and just the low level,
*  the atomic scale, how the materials operate, at the high scale, how black holes operate.
*  But it seems like it could be, there's infinite other possibilities where none of it could be
*  compressible into such equations. It just seems beautiful. It's also weird, probably to the point
*  you're making, that it's very pleasant that this is true for our minds. So it might be that our
*  minds are biased to just be looking at the parts of the universe that are compressible.
*  And then we can publish papers on and have nice E equals empty squared equations.
*  Right. Well, I wonder, would such a world with uncompressible laws allow for the kind of beings
*  that can think about the kind of questions that you're asking? That's true. Right? Like an
*  anthropic principle coming into play at some weird way here. I don't know. Like, I don't know what
*  I'm talking about. Or maybe the universe is actually not so compressible, but the way our
*  brain, the way our brain evolved, we're only able to perceive the compressible parts. I mean, we are,
*  this is the sort of Chomsky argument. We are just descendants of apes. We're like really limited
*  biological systems. So it totally makes sense that we're really limited little computers,
*  calculators that are able to perceive certain kinds of things. And the actual world is much
*  more complicated. Well, but we can, we can do pretty awesome things, right? Like we can fly
*  spaceships and that we have to have some connection of reality to be able to take our potentially
*  oversimplified models of the world, but then actually twist the world to our will based on
*  it. So we have certain reality checks that like physics isn't too far afield simply based on what
*  we can do. Yeah. The fact that we can fly is pretty good. It's great. Yeah. It's like,
*  it's pretty good proof of concept that the laws we're working with are, are working well. So I
*  mentioned to the internet that I'm talking to you and so the internet gave some questions.
*  So I apologize for these, but do you think we're living in a simulation that the universe is a
*  computer or the universe is a computation running on a computer? It's conceivable. What I don't buy
*  is, you know, you'll have the argument that, well, let's say that it was the case that you
*  can have simulations, then the simulated world would itself eventually get to a point where it's
*  running simulations. And then the, the second layer down would create a third layer down and on and on
*  and on. So probabilistically, you just throw a dart at one of those layers. We're probably in one
*  of the simulated layers. I think if there's some sort of limitations on like the information
*  processing of whatever the physical world is, like it quickly becomes the case that you have a limit
*  to the layers that could exist there because like the resources necessary to simulate a universe
*  like ours clearly is a lot just in terms of the number of bits at play. And so then you can ask,
*  well, what's more plausible that there's an unbounded capacity of information processing
*  in whatever the like highest up level universe is, or that there's some bound to that capacity,
*  which then limits like the number of levels available. How do you play some kind of
*  probability distribution on like what the information capacity is? I have no idea,
*  but I don't want to meet like people almost assume a certain uniform probability over
*  all of those meta layers that could conceivably exist when it's, it's a little bit like a Pascal's
*  wager on like, you're not giving a low enough prior to the mere existence of that infinite set
*  of layers. Yeah, that's true. But it's also very difficult to contextualize the amount. So the
*  amount of information processing power required to simulate like our universe seems like amazingly
*  huge, but you can always raise two to the power of that. Yeah. Like numbers get big. And we're
*  easily humbled by basically everything around us. So it's very difficult to, uh, to kind of
*  make sense of anything actually, when you look up at the sky and look at the stars and the
*  immensity of it all to make sense of us, the smallness of us, the unlikeliness of everything
*  that's on this earth coming to be, then you could basically, anything could be all laws of
*  probability go out the window to me because, um, I guess because the amount of information under
*  which we're operating is very low. We're basically no nothing about the world around us.
*  Relatively speaking. And so, so when I think about the simulation hypothesis, I think it's just fun
*  to think about it, but it's also, I think there is a thought experiment kind of interesting to think
*  of the power of computation, whether the limits of a touring machine, sort of the limits of our
*  current computers. When you start to think about artificial intelligence, how far can we get with
*  computers? And that's kind of where the simulation hypothesis is useful to me as a thought
*  experiment is, is the universe just the computer? Is it just a computation? Is all of this just a
*  computation and sort of the same kind of tools we apply to analyzing algorithms. Can that be applied?
*  You know, if we scale further and further and further, will the arbitrary power of those systems
*  start to create some interesting aspects that we see in our universe or is something fundamentally
*  different needs to be created? Well, it's interesting that in our universe, it's not
*  arbitrarily large, the power that you can place limits on, for example, how many bits of information
*  can be stored per unit area, right? Like all of the physical laws, you've got general relativity
*  and like quantum coming together to give you a certain limit on how many bits you can store
*  within a given range before it collapses into a black hole. Like the idea that there even exists
*  such a limit is at the very least thought provoking when naively you might assume, oh, well,
*  you know, technology could always get better and better. We could get cleverer and cleverer.
*  And you could just cram as much information as you want into like a small unit of space. That
*  that makes me think it's at least plausible that whatever the highest level of existence is
*  doesn't admit too many simulations or ones that are at the scale of complexity that we're looking
*  at. Obviously, it's just as conceivable that they do and that there are many. But I guess what I'm
*  channeling is the surprise that I felt upon learning that fact that there are that information is
*  physical in this way. There's a finiteness to it. Okay, let me just even go off on that
*  from mathematics perspective and the psychology perspective. How do you mix? Are you
*  psychologically comfortable with the concept of infinity?
*  I think so. Are you okay with it? I'm pretty okay. Yeah. Are you okay? No, not really. It doesn't
*  make any sense to me. I don't know. Like how many, how many words, how many possible words do you
*  think could exist that are just like strings of letters? So that's a sort of mathematical
*  statement is beautiful and we use infinity and basically everything we do,
*  everything we do in science, math and engineering. Yes. But you said exist. The question is,
*  you said letters or words? I said words. To bring words into existence to me, you have to start
*  saying them or writing them or listing them. That's an instantiation. Okay. How many abstract
*  words exist? Well, the idea of abstract, the idea of abstract notions and ideas. I think we should
*  be clear on terminology. I mean, you think about intelligence a lot, like artificial intelligence.
*  Would you not say that what it's doing is a kind of abstraction? That like abstraction is key to
*  conceptualizing the universe. You get this raw sensory data. You need, I need something that
*  every time you move your face a little bit and they're not pixels, but like analog of pixels on
*  my retina change entirely that I can still have some coherent notion of this is Lex. I'm talking
*  to Lex. Right? What that requires is you have a disparate set of possible images hitting me
*  that are unified in a notion of Lex. Right? That's a kind of abstraction. It's a thing that could
*  apply to a lot of different images that I see and it represents it in a much more compressed way
*  and one that's like much more resilient to that. I think in the same way, if I'm talking about
*  infinity as an abstraction, I don't mean non-physical woo woo, like ineffable or
*  something. What I mean is it's something that can apply to a multiplicity of situations that share
*  a certain common attribute in the same way that the images of like your face on my retina share
*  enough common attributes that I can put the single notion to it. Like in that way, infinity is an
*  abstraction and it's very powerful and it's only through such abstractions that we can actually
*  understand like the world and logic and things. And in the case of infinity, the way I think about
*  it, the key entity is the property of always being able to add one more. Like no matter how
*  many words you can list, you just throw an A at the end of one and you have another conceivable word.
*  You don't have to think of all the words at once. It's that property. The, oh, I could always add
*  one more that gives it this nature of infinitiveness in the same way that there's certain properties of
*  your face that give it the Lex-ness, right? So like infinity should be no more worrying
*  than the, I can always add one more sentiment. That's a really elegant, much more elegant way
*  than I could put it. So thank you for doing that as yet another abstraction. And yes, indeed,
*  that's what our brain does. That's what intelligent systems do. That's what programming does. That's
*  what science does is build abstraction on top of each other. And yet there is at a certain point
*  abstractions that go into the quote woo, right? And because we're now, it's like, we built this
*  stack of, you know, the only thing that's true is the stuff that's on the ground. Everything else is
*  useful for interpreting this. And at a certain point you might start floating into ideas that are
*  surreal and difficult and take us into areas that are disconnected from reality in a way that we
*  can never get back. What if instead of calling these abstract, how different would it be in
*  your mind if we called them general and the phenomena that you're describing as over
*  generalization? When you try to generalization, have a concept or an idea that's so general
*  as to apply to nothing in particular in a useful way, does that map to what you're thinking of when
*  you think of? First of all, I'm playing a little just for the fun of it. Yeah, I know. The devil's
*  advocate. And I think our cognition, our mind is unable to visualize. So you do some incredible
*  work with visualization and video. I think infinity is very difficult to visualize for our mind. We
*  can dilute ourselves into thinking we can visualize it, but we can't. I don't, I mean, I don't, I would
*  venture to say it's very difficult. And so there's some concepts of mathematics, like maybe multiple
*  dimensions we could sort of talk about that are impossible for us to truly in into it. Like, and
*  it just feels dangerous to me to use these as part of our toolbox of abstractions.
*  On behalf of your listeners, I almost fear we're getting too philosophical. Right?
*  No, heck no. But I think to that point, for any particular idea like this, there's multiple
*  angles of attack. I think when we do visualize infinity, what we're actually doing, you know,
*  you write dot dot dot, right? One, two, three, four, dot dot dot. Right? Those are symbols on
*  the page that are insinuating a certain infinity. What you're capturing with a little bit of design
*  there is the, I can always add one more property. Right? I think I'm just as uncomfortable with you
*  are if you try to concretize it so much that you have a bag of infinitely many things that I
*  actually think of, no, not one, two, three, four, dot dot dot one, two, three, four, five, six,
*  seven, eight. I try to get them all in my head and you realize, oh, I, you know, your brain would
*  literally collapse into a black hole. All of that. And I honestly feel this with a lot of math that
*  I try to read where I, I don't think of myself as like particularly good at math. I, in some ways,
*  like I get very confused often when I am going through some of these texts. Uh, and often what
*  I'm feeling my head is like, this is just so damn abstract. I just can't wrap my head around it. I
*  just wanted to put something concrete to it that makes me understand. And I think a lot of the
*  motivation for the channel is channeling that sentiment of, yeah, a lot of the things that
*  you're trying to read out there, it's just so hard to connect to anything that you spend an hour
*  banging your head against a couple of pages and you come out not really knowing anything more
*  other than some definitions maybe and a certain sense of self-defeat. Right. One of the reasons
*  I focus so much on visualizations is that I'm a big believer in, I'm sorry, I'm just really hampering
*  out this idea of abstraction, being clear about your layers of abstraction. Yes. Right. It's always
*  tempting to start an explanation from the top to the bottom. Okay. You, you give the definition of
*  a new theorem. You're like, this is the definition of a vector space. For example, we're going to,
*  that's how we'll start our course. These are the properties of a vector space. First from these
*  properties, we will derive what we need in order to do the math of linear algebra or whatever it
*  might be. I don't think that's how understanding works at all. I think how understanding works is
*  you start at the lowest level you can get at where rather than thinking about a vector space,
*  you might think of concrete vectors that are just lists of numbers or picturing it as like an arrow
*  that you draw, which is itself like even less abstract than numbers because you're looking at
*  quantities like the distance of the X coordinate, the distance of the white coordinate. It's as
*  concrete as you could possibly get. And it has to be if you're putting it in a visual, right?
*  Like it's an actual arrow. It's an actual vector. You're not talking about like a quote unquote
*  vector that could apply to any possible thing. You have to choose one if you're illustrating it.
*  And I think this is the power of being in a medium like video, or if you're writing a textbook and
*  you force yourself to put a lot of images is with every image you're making a choice with each
*  choice, you're showing a concrete example with each concrete example, you're aiding someone's
*  path to understanding. You know, I'm sorry to interrupt you, but you just made me realize
*  that that's exactly right. So the visualizations you're creating while you're sometimes talking
*  about abstractions, the actual visualization is a explicit low level example. Yes. So there's an
*  actual like in the code, you have to say what the, what the vector is, what's the direction of the
*  arrow, what's the magnitude of the, yeah. So that's, you're going, the visualization itself
*  is actually going to the bottom of that. And I think that's very important. I also think about
*  this a lot in writing scripts where even before you get to the visuals, the first instinct is to,
*  I don't know why, I just always do. I say the abstract thing. I say the general definition,
*  the powerful thing. And then I fill it in with examples later. Always it will be more compelling
*  and easier to understand when you flip that. And instead you let someone's brain do the
*  pattern recognition. You just show them a bunch of examples. The brain is going to feel a certain
*  similarity between them. Then by the time you bring in the definition or by the time you bring
*  in the formula, it's articulating a thing that's already in the brain that was built off of looking
*  at a bunch of examples with a certain kind of similarity. And what the formula does is articulate
*  what that kind of similarity is rather than being a, a high cognitive load set of symbols
*  that needs to be populated with examples later on, assuming someone's still with you.
*  What is the most beautiful or inspiring idea you've come across in mathematics?
*  I don't know, man. Maybe it's an idea you've explored in your videos. Maybe not. What like
*  just gave you pause. It's the most beautiful idea. Small or big. So I think often the things that
*  are most beautiful are the ones that you have like a little bit of understanding of, but certainly
*  not an entire understanding. It's a little bit of that mystery that is what makes it beautiful.
*  Almost the moment of the discovery for you personally, almost just that leap of aha moment.
*  So something that really caught my eye. I remember when I was little, there were these like,
*  um, I think the series was called like wooden books or something, these tiny little books that
*  would have just a very short description of something on the left and then a picture on the
*  right. I don't know who they're meant for, but maybe it's like loosely children or something
*  like that, but it can't just be children. Cause of some of the things that I was describing
*  on the last page of one of them, somewhere tiny in there was this little formula that on the left
*  hand had a sum over all of the natural numbers. You know, it's like one over one to the S plus
*  one over two to the S plus one over three to the S on and onto an infinity. Then on the other side
*  had a product over all of the primes and it was a certain thing had to do with all the primes.
*  And like any good young math enthusiast, I'd probably been indoctrinated with how chaotic
*  and confusing the primes are, which they are. And seeing this equation where on one side you
*  have something that's as understandable as you could possibly get the counting numbers.
*  Yes. And on the other side is all the prime numbers. It was like this, whoa,
*  they're related like this. There's a, there's a simple description that includes like all the
*  primes getting wrapped together like this. This is like the oiler product for the Zeta function.
*  As I later found out the equation itself essentially encodes the fundamental theorem
*  of arithmetic that every number can be expressed as a unique set of primes to me. Still, there's,
*  I mean, I certainly don't understand this equation or this function all that well.
*  The more I learn about it, the prettier it is. The idea that you can, this is sort of what gets
*  you representations of primes, not in terms of primes themselves, but in terms of another set
*  of numbers that are like the non-trivial zeros of the Zeta function. And again, I'm very kind of in
*  over my head in a lot of ways as I like try to get to understand it, but the more I do, it's,
*  it always leaves enough mystery that it remains very beautiful to me.
*  So whenever there's a little bit of mystery just outside of your understanding that,
*  and by the way, the process of learning more about it, how does that come about? Just your
*  own thought or are you reading? Or is the process of visualization itself revealing more to you?
*  Yeah. Visuals help. I mean, in one time when I was just trying to understand like
*  analytic continuation and playing around with visualizing complex functions, this is what led
*  to a video about this function. It's titled something like visualizing the Riemann Zeta
*  function. It's one that came about because I was programming and tried to see what a certain thing
*  looked like. And then I looked at it and like, Whoa, that's elucidating. And then I decided to
*  make a video about it. But I mean, you try to get your hands on as much reading as you can.
*  In this case, I think if anyone wants to start to understand it, if they have like a
*  math background of some, like they studied some in college or something like that,
*  like the Princeton companion to math has a really good article on analytic number theory.
*  And that itself has a whole bunch of references. And you know, anything has more references and
*  it gives you this like tree to start piling through. And like, you know, you try to understand,
*  I try to understand things visually as I go. That's not always possible. But it's very helpful when
*  it does. You recognize when there's common themes, like in this case, cousins of the Fourier transform
*  that come into play and you realize, oh, it's probably pretty important to have deep intuitions
*  of the Fourier transform, even if it's not explicitly mentioned in like these texts.
*  And you try to get a sense of what the common players are. But I'll emphasize again, like,
*  I feel very in over my head when I try to understand the exact relation between like the
*  zeros of the Riemann zeta function and how they relate to the distribution of primes.
*  I definitely understand it better than I did a year ago. I definitely understand it one,
*  one hundredth as well as the experts on the matter do, I assume. But the slow path towards
*  getting there is it's fun. It's charming. And like to your question, very beautiful.
*  **Jay
*  At the same time, it doesn't feel like humans ever made an arbitrary choice in studying this
*  particular thing. So, you know, it feels like you're speaking to patterns themselves or nature
*  itself. That's a big part of it. I think things that are too arbitrary, it's just hard for those
*  to feel beautiful because this is sort of what the word contrived is meant to apply to. Right?
*  **Jay And when they're not arbitrary means it could be,
*  you can have a clean abstraction and intuition that allows you to comprehend it.
*  **Jay Well, to one of your first questions, it makes you feel like if you came across
*  another intelligent civilization, that they'd be studying the same thing.
*  **Jay Maybe with different notation.
*  **Jay Certainly. Yeah. But yeah, like that's what I think you talked to that other civilization.
*  They're probably also studying the zeros of the Riemann zeta function or like some variant thereof
*  that is like a clearly equivalent cousin or something like that. But that's probably on their
*  docket. **Jay Whenever somebody does a lot of something amazing, I'm going to ask the question
*  that you've already been asked a lot and that you'll get more and more asked in your life.
*  But what was your favorite video to create? **Jay
*  Oh, favorite to create. One of my favorites is the title is Who Cares About Topology.
*  **Jay Do you want me to pull it up or no? **Jay If you want, sure. Yeah. It is about,
*  well, it starts by describing an unsolved problem that's still unsolved in math called the inscribed
*  square problem. You draw any loop and then you ask, are there four points on that loop that make a
*  square? Totally useless, right? This is not answering any physical questions. It's mostly
*  interesting that we can't answer that question. And it seems like such a natural thing to ask.
*  Now, if you weaken it a little bit and you ask, can you always find a rectangle? You choose four
*  points on this curve. Can you find a rectangle? That's hard, but it's doable. And the path to it
*  involves things like looking at a torus, this surface with a single hole in it, like a donut,
*  or looking at a Mobius strip in ways that feel so much less contrived to when I first,
*  as a little kid, learned about these surfaces and shapes, like a Mobius strip and a torus.
*  What you learn is, oh, this Mobius strip, you take a piece of paper, put a twist, glue it together,
*  and now you have a shape with one edge and just one side. And as a student, you should think,
*  who cares? How does that help me solve any problems? I thought math was about problem solving.
*  So what I liked about the piece of math that this was describing that was in this paper by
*  a mathematician named Vaughn was that it arises very naturally. It's clear what it represents.
*  It's doing something. It's not just playing with construction paper. And the way that it solves
*  the problem is really beautiful. So kind of putting all of that down and concretizing it,
*  right? Like I was talking about how when you have to put visuals to it, it demands that what's on
*  screen is a very specific example of what you're describing. The construction here is very abstract
*  in nature. You describe this very abstract kind of surface in 3D space. So then when I was finding
*  myself, in this case, I wasn't programming, I was using Graffer that's built into OSX for the 3D
*  stuff. To draw that surface, you realize, oh man, the topology argument is very non-constructive.
*  I have to make a lot of, you have to do a lot of extra work in order to make the surface show up.
*  But then once you see it, it's quite pretty. And it's very satisfying to see a specific instance
*  of it. And you also feel like, ah, I've actually added something on top of what the original paper
*  was doing, that it shows something that's completely correct. That's a very beautiful argument,
*  but you don't see what it looks like. And I found something satisfying in seeing what it looked like
*  that could only ever have come about from the forcing function of getting some kind of image
*  on the screen to describe the thing I was talking about. So you almost weren't able to anticipate
*  what it's going to look like. I had no idea. I had no idea. And it was wonderful. It was totally,
*  it looks like a Sydney Opera House or some sort of Frank Gehry design. And it was,
*  you knew it was going to be something. And you can say various things about it, like, oh, it
*  touches the curve itself. It has a boundary that's this curve on the 2D plane. It all sits above the
*  plane. But before you actually draw it, it's very unclear what the thing will look like. And to see
*  it, it's very, it's just pleasing, right? So that was fun to make, very fun to share. I hope that it
*  has elucidated for some people out there where these constructs of topology come from,
*  that it's not arbitrary play with construction paper.
*  So let's, I think this is a good, a good sort of example to talk a little bit about your process.
*  So you have, you have a list of ideas. So that's sort of the, the curse of having,
*  having an active and brilliant mind is I'm sure you have a list that's growing faster than you can
*  utilize. Absolutely. But there's some sorting procedure depending on mood and interest and so
*  on. But okay, see pick an idea. Then you have to try to write a narrative arc that sort of,
*  how do I elucidate? How do I make this idea beautiful and clear and explain it? And then
*  there's a set of visualizations that will be attached to it. Sort of you've talked about some
*  of this before, but sort of writing the story, attaching the visualizations, can you talk through
*  interesting, painful, beautiful parts of that process? Well, the most painful is if you've
*  chosen a topic that you do want to do, but then it's hard to think of, I guess, how to structure
*  the script. This is sort of where I have been on one for like the last two or three months.
*  And I think that ultimately the right resolution is just like set it aside and instead do some
*  other things where the script comes more naturally. Because you sort of don't want to overwork a
*  narrative. The more you've thought about it, the less you can empathize with the student who doesn't
*  yet understand the thing you're trying to teach. Who is the judger in your head? Sort of the person,
*  the creature, the essence that's saying this sucks or this is good. And you mentioned kind of the
*  student you're thinking about. Who is that? What is that thing that says the perfections,
*  that says this thing sucks, you need to work on it for another two, three months.
*  I don't know. I think it's my past self. I think that's the entity that I'm most trying to empathize
*  with is like you take who I was, because that's kind of the only person I know. Like you don't
*  really know anyone other than versions of yourself. So I start with the version of myself that I know
*  who doesn't yet understand the thing. And then I just try to view it with fresh eyes,
*  a particular visual or a particular script. Is this motivating? Does this make sense?
*  Which has its downsides because sometimes I find myself speaking to motivations that only myself
*  would be interested in. I don't know. I did this project on quaternions where what I really wanted
*  was to understand what are they doing in four dimensions? Can we see what they're doing in
*  four dimensions? Right? And I had a way of thinking about it that really answered the
*  question in my head that made me very satisfied and being able to think about concretely with a
*  3D visual, what are they doing to a 4D sphere? And so I'm like, great, this is exactly what my
*  past self would have wanted. Right? And I make a thing on it. And I'm sure it's what some other
*  people wanted too. But in hindsight, I think most people who want to learn about quaternions are
*  like robotics engineers or graphics programmers who want to understand how they're used to describe
*  3D rotations. And like their use case was actually a little bit different than my past self.
*  And in that way, like I wouldn't actually recommend that video to people who are coming at it from
*  that angle of wanting to know, Hey, I'm a robotics programmer. Like how do these quaternions things
*  work to describe position in 3D space? I would say other great resources for that. If you ever
*  find yourself wanting to say like, but hang on, in what sense are they acting in four dimensions,
*  then come back. But until then, it's a little different. Yeah, it's interesting because
*  you have incredible videos on neural networks, for example. And from my perspective, because I've
*  probably, I mean, I looked at the, is sort of my field and I've also looked at the basic
*  introduction of neural networks, like a million times from different perspectives. And it made
*  me realize that there's a lot of ways to present it. So you are sort of, you did an incredible job.
*  I mean, sort of the, but you could also do it differently and also incredible. Like to create
*  a beautiful presentation of a basic concept is requires sort of a creativity requires genius and
*  so on. But you can take it from a bunch of different perspectives. And that video on neural
*  networks, maybe you realize that. And just as you're saying, you're kind of have a certain mindset,
*  a certain view. But from a, if you take a different view from a physics perspective,
*  from a neuroscience perspective, talking about neural networks or from a robotics perspective,
*  or from, let's see, from a pure learning statistics perspective. So you, you can create
*  totally different videos and you've done that with a few actually concepts where you've have taken
*  different cuts. Like at the, at the, at the Euler equation, right? You've taken different
*  views of that. I think I've made three videos on it and I definitely will make at least one more.
*  Never enough. Never enough. So you don't think it's the most beautiful equation in mathematics?
*  Like I said, as we represent it, it's one of the most hideous. It involves a lot of the most
*  hideous aspects of our notation. I talked about E, the fact that we use pi instead of tau, the fact
*  that we call imaginary numbers imaginary. And then, and actually wonder if we use the I because of
*  imaginary. I don't know if that's historically accurate, but at least a lot of people, they
*  read the I and they think imaginary. Like all three of those facts, it's like, those are things that
*  have added more confusion than they needed to. And we're wrapping them up in one equation. Like,
*  boy, that's just very hideous, right? The idea is that it does tie together when you wash away the
*  notation. Like, it's okay. It's pretty. It's nice, but it's not like mind blowing greatest thing in
*  the universe, which is maybe what I was thinking of when I said, like, once you understand something,
*  it doesn't have the same beauty. Like I feel like I understand Euler's formula and I feel like I
*  understand it enough to sort of see the version that just woke up that hasn't really gotten itself
*  dressed in the morning. That's a little bit groggy and there's bags under its eyes. It's like, it's
*  the past, the, the, the dating stage and you're not married. We're no longer dating, right? I'm
*  still dating the Zeta function and like, she's beautiful and right. And like we have fun and
*  it's that, that high dopamine part, but like maybe at some point we'll settle into the more
*  mundane nature of the relationship where I like see her for who she truly is and she'll still be
*  beautiful in her own way, but it won't have the same romantic pizzazz, right? Well, that's the
*  nice thing about mathematics. I think, uh, as long as you don't live forever, there'll always be
*  enough mystery and fun with some of the equations. Even if you do the rate at which
*  questions comes up as much faster than the rate at which answers come up. So if you could live
*  forever, would you? I think so. Yeah. So you think you don't think mortality is the thing that makes
*  life meaningful? Would your life be four times as meaningful if you died at 25? So this goes to
*  infinity. I think you and I, that's really interesting. So what I said is infinite, not,
*  not four times longer said infinite. So the, the actual existence of the finiteness,
*  the existence of the end, no matter the length is the thing that may sort of,
*  for my comprehension of psychology, it's, it's such a deeply human, it's such a fundamental part of
*  the human condition. The fact that there is that we're mortal, that the fact that things end,
*  it seems to be a crucial part of what gives them meaning. I don't think, at least for me, like,
*  it's a very small percentage of my time that mortality is salient, that I'm like aware of
*  the end of my life. What do you mean by me? I'm, I'm trolling. Is it the ego? Is it the id? Or is
*  it the superego? Is, uh, uh, so you're the reflective self, the, the vernicese area that puts all this
*  stuff into words. Yeah. A small percentage of your mind that is actually aware of the true
*  motivations that drive you. But my point is that most of my life, I'm not thinking about death,
*  but I still feel very motivated to like make things and to like interact with people,
*  like experience love or things like that. I'm very motivated and I, it's strange that that
*  motivation comes while death is not in my mind at all. And this might just be because I'm
*  young enough that it's not salient. Or it's in your subconscious or that you construct an illusion
*  that allows you to escape the fact that of your mortality by enjoying the moment,
*  sort of the existential approach to life. Could be, um, gun to my head. I don't think that's it.
*  Yeah. Another, another sort of way to say gun to the head is the deep psychological introspection
*  of what drives us. I mean, that's, um, in some ways to me, I mean, when I look at math, when I
*  look at science, is it kind of an escape from reality in a sense that it's so beautiful.
*  It's such a beautiful journey of discovery that it allows you to actually, it's, it's, it allows
*  you to achieve a kind of a mortality of, of explore ideas and sort of connect yourself to the thing
*  that is seemingly infinite, like the universe, right? That allows you to escape the, um, the
*  limited nature of our little, of our bodies, of our existence.
*  What else would give this podcast meaning? That's right. If not the fact that it will end.
*  This place closes in 40 minutes. And it's so much more meaningful for it.
*  How much more I love this room because we'll be kicked out.
*  So I understand just because you're trolling me doesn't mean I'm wrong.
*  I take your point. I take your point. Boy, that would be a good Twitter bio.
*  Just because you're trolling me doesn't mean I'm wrong. Yeah. And, and sort of difference in
*  backgrounds, I'm a bit Russian, so we're a bit melancholic and seem to maybe assign a little too
*  much value to suffering and mortality and things like that. Make, makes for a better novel, I think.
*  Oh yeah. You need, you need some sort of existential threat to, to drive a plot.
*  So when do you know when the video is done? When you're working on it?
*  That's pretty easy actually, because I mean, I'll, I'll write the script. I want there to be some
*  kind of aha moment in there. And then hopefully the script can revolve around some kind of aha
*  moment. And then from there, you know, you're putting visuals to each sentence that exists,
*  and then you narrate it, you edit it all together. So given that there's a script,
*  the end becomes quite clear. And you know, you're as, as I, as I animate it, I often change the,
*  certainly the specific words, but sometimes the structure itself. But it's a very deterministic
*  process at that point. It makes it much easier to predict when something will be done. How do you
*  know when a script is done? It's like for problem solving videos, that's quite simple. It's, it's
*  once you feel like someone who didn't understand the solution now could for things like neural
*  networks, that was a lot harder because like you said, there's so many angles at which you
*  could attack it. And there it's, it's just, at some point you feel like this, this asks a
*  meaningful question and it answers that question. Right. What is the best way to learn math for
*  people who might be at the beginning of that journey? I think that's a, it's a question that
*  a lot of folks kind of ask and think about, and it doesn't even for folks who are not really at
*  the beginning of their journey. Like there might be actually is deep in their career, some type
*  they've taken college, they're taking calculus and so on, but still want to sort of explore math.
*  What would be your advice and sort of education at all ages? Your temptation will be to spend more
*  time like watching lectures or reading. Try to force yourself to do more problems than you
*  naturally would. That's a big one. Like the, the focus time that you're spending should be on
*  solving specific problems and seek entities that have well curated lists of problems.
*  So go into like a textbook almost and the problems in the back of a text kind of thing,
*  back of a chapter. So if you can take a little look through those questions at the end of the
*  chapter before you read the chapter, a lot of them won't make sense. Some of them might,
*  and those are, those are the best ones to think about. A lot of them won't, but just, you know,
*  take a quick look and then read a little bit of the chapter and then maybe take a look again and
*  things like that. And don't consider yourself done with the chapter until you've actually
*  worked through a couple of exercises. Right. And this is so hypocritical, right? Cause I like put
*  out videos that pretty much never have associated exercises. I just view myself as a different part
*  of the ecosystem, which means I'm kind of admitting that you're not really learning,
*  or at least this is only a partial part of the learning process. If you're watching these videos,
*  I think if someone's at the very beginning, like I do think Khan Academy does a good job. They have
*  a pretty large set of questions you can work through. Just the very basics sort of just
*  picking, picking up, getting, getting comfortable with the very basic linear algebra calculus on
*  Khan Academy. Programming is actually, I think a great like learn to program and like let the way
*  that math is motivated from that angle, push you through. I know a lot of people who didn't like
*  math got into programming in some way and that's what turned them on to math. Maybe I'm biased
*  cause like I live in the Bay area, so I'm more likely to run into someone who has that phenotype,
*  but I am willing to speculate that that is a more generalizable path. So you yourself kind of in
*  creating the videos are using programming to illuminate a concept, but for yourself as well.
*  So would you recommend somebody try to make a sort of almost like try to make videos like you do?
*  So one thing I've heard before, I don't know if this is based on any actual study. This might be
*  like a total fictional anecdote of numbers, but it rings in the mind as being true. You remember
*  about 10% of what you read. You remember about 20% of what you listen to. You remember about 70%
*  of what you actively interact with in some way, and then about 90% of what you teach. This is a
*  thing I heard again, those numbers might be meaningless, but they ring true, don't they?
*  Right? I'm willing to say I learned nine times better if I'm teaching something than reading.
*  That might even be a low ball. Right? So doing something to teach or to like actively try to
*  explain things is huge for consolidating the knowledge. Outside of family and friends,
*  is there a moment you can remember that you would like to relive because it made you truly happy
*  or it was transformative in some fundamental way? A moment that was transformative. Or made you truly
*  happy? Yeah, I think there's times like music used to be a much bigger part of my life than it is now.
*  When I was a teenager, and I can think of some times in playing music. There was one,
*  my brother and a friend of mine, so this slightly violates the family and friends, but there was
*  music that made me happy. They were just accompanying. We played a gig at a ski resort
*  such that you take a gondola to the top and did a thing. Then on the gondola ride down,
*  we decided to just jam a little bit. The gondola came over a mountain and you saw
*  the city lights and we're just jamming, playing some music. I wouldn't describe that as
*  transformative. I don't know why, but that popped into my mind as a moment of, in a way that wasn't
*  associated with people I love, but more with a thing I was doing, something that was just happy
*  and it was just a great moment. I don't think I can give you anything deeper than that though.
*  Well, as a musician myself, I'd love to see, as you mentioned before, music enter back into your
*  work, back into your creative work. I'd love to see that. I'm certainly allowing it to enter back
*  into mine and it's a beautiful thing for a mathematician, for a scientist to allow music
*  to enter their work. I think only good things can happen. All right. I'll try to promise you a music
*  video by 2020. By 2020? By the end of 2020. Okay. All right. Good. I'll give myself a longer window.
*  All right. Maybe we can collaborate on a band type situation. What instruments do you play?
*  The main instrument I play is violin, but I also love to dabble around on like guitar and piano.
*  Beautiful. Me too. Guitar and piano. So in, in a mathematician's lament, Paul Lockhart writes,
*  the first thing to understand is that mathematics is an art. The difference between math and the
*  other arts, such as music and painting, is that our culture does not recognize it as such.
*  So I think I speak for millions of people, myself included, in saying thank you for revealing
*  to us the art of mathematics. So thank you for everything you do and thanks for talking today.
*  Wow. Thanks for saying that and thanks for having me on.
*  Thanks for listening to this conversation with Grant Sanderson and thank you to our
*  presenting sponsor, Cash App. Download it, use code LEXPODCAST, you'll get $10 and $10 will go
*  to first, a STEM education nonprofit that inspires hundreds of thousands of young minds to become
*  future leaders and innovators. If you enjoy this podcast, subscribe on YouTube, give it five stars
*  on Apple Podcasts, support it on Patreon, or connect with me on Twitter. And now let me leave
*  you with some words of wisdom from one of Grant's and my favorite people, Richard Feynman.
*  Nobody ever figures out what this life is all about and it doesn't matter. Explore the world.
*  Nearly everything is really interesting if you go into it deeply enough.
*  Thank you for listening and hope to see you next time.
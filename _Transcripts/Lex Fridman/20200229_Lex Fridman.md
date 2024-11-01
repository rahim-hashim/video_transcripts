---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 4368s
Video Keywords: ['john hopfield', 'physics', 'hopfield networks', 'associative memory', 'neurobiology', 'deep learning', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 118213
Video Rating: None
Video Description: John Hopfield is professor at Princeton, whose life's work weaved beautifully through biology, chemistry, neuroscience, and physics. Most crucially, he saw the messy world of biology through the piercing eyes of a physicist. He is perhaps best known for his work on associate neural networks, now known as Hopfield networks that were one of the early ideas that catalyzed the development of the modern field of deep learning.

EPISODE LINKS:
Now What? article: http://bit.ly/3843LeU
John wikipedia: https://en.wikipedia.org/wiki/John_Hopfield
Books mentioned:
- Einstein's Dreams: https://amzn.to/2PBa96X
- Mind is Flat: https://amzn.to/2I3YB84

This episode is presented by Cash App. Download it & use code "LexPodcast":
Cash App (App Store): https://apple.co/2sPrUHe
Cash App (Google Play): https://bit.ly/2MlvP5w

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
2:35 - Difference between biological and artificial neural networks
8:49 - Adaptation
13:45 - Physics view of the mind
23:03 - Hopfield networks and associative memory
35:22 - Boltzmann machines
37:29 - Learning
39:53 - Consciousness
48:45 - Attractor networks and dynamical systems
53:14 - How do we build intelligent systems?
57:11 - Deep thinking as the way to arrive at breakthroughs
59:12 - Brain-computer interfaces
1:06:10 - Mortality
1:08:12 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# John Hopfield Physics View of the Mind and Neurobiology  Lex Fridman Podcast #76
**Lex Fridman:** [February 29, 2020](https://www.youtube.com/watch?v=DKyzcbNr8WE)
*  The following is a conversation with John Hopfield, Professor Princeton, whose life's
*  work weaved beautifully through biology, chemistry, neuroscience, and physics.
*  Most crucially, he saw the messy world of biology through the piercing eyes of a physicist.
*  He's perhaps best known for his work on associative neural networks, now known as Hopfield networks,
*  that were one of the early ideas that catalyzed the development of the modern field of deep
*  learning.
*  As his 2019 Franklin Medal in Physics award states, he applied concepts of theoretical
*  physics to provide new insights on important biological questions in a variety of areas,
*  including genetics and neuroscience, with significant impact on machine learning.
*  And as John says in his 2018 article titled, Now What?, his accomplishments have often
*  come about by asking that very question, Now What?, and often responding by a major
*  change of direction.
*  This is the Artificial Intelligence Podcast.
*  If you enjoy it, subscribe on YouTube, give it five stars on Apple Podcasts, support it
*  on Patreon, or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N.
*  As usual, I'll do one or two minutes of ads now and never any ads in the middle that can
*  break the flow of the conversation.
*  I hope that works for you and doesn't hurt the listening experience.
*  This show is presented by CashApp, the number one finance app in the app store.
*  When you get it, use code LexPodcast.
*  CashApp lets you send money to friends, buy bitcoin, and invest in the stock market with
*  as little as one dollar.
*  Since CashApp does fractional share trading, let me mention that the order execution algorithm
*  that works behind the scenes to create the abstraction of fractional orders is to me
*  an algorithmic marvel.
*  Big props to the CashApp engineers for solving a hard problem that in the end provides an
*  easy interface that takes a step up the next layer of abstraction over the stock market,
*  making trading more accessible for new investors and diversification much easier.
*  Again, if you get CashApp from the app store or Google Play and use code LexPodcast, you'll
*  get ten dollars and CashApp will also donate ten dollars to the FIRST, one of my favorite
*  organizations that is helping advance robotics and STEM education for young people around
*  the world.
*  And now here's my conversation with John Hopfield.
*  What difference between biological neural networks and artificial neural networks is
*  most captivating and profound to you?
*  At the higher philosophical level, let's not get technical just yet.
*  One of the things that very much intrigues me is the fact that neurons have all kinds
*  of components, properties to them.
*  And evolutionary biology, if you have some little quirk in how a molecule works or how
*  a cell works and it can be made use of, evolution will sharpen it up and make it into a useful
*  feature rather than a glitch.
*  And so you expect in neurobiology for evolution to have captured all kinds of possibilities
*  of getting neurons, of how you get neurons to do things for you.
*  And that aspect has been completely suppressed in artificial neural networks.
*  Do the glitches become features in the biological neural network?
*  They can.
*  Look, let me take one of the things that I used to do research on.
*  If you take things which oscillate, they have rhythms which are sort of close to each other.
*  Under some circumstances these things will have a phase transition and suddenly the
*  rhythm will, everybody will fall into step.
*  There was a marvelous physical example of that in the Millennium Bridge across the Thames
*  River about, built about 2001.
*  And pedestrians walking across, pedestrians don't walk, synchronize, they don't walk in
*  lockstep.
*  But they're all walking about the same frequency.
*  And the bridge could sway at that frequency and the slight sway made pedestrians tend
*  a little bit to lock in the step.
*  And after a while the bridge was oscillating back and forth and the pedestrians were walking
*  in step to it.
*  And you could see it in the movies made out of the bridge.
*  And the engineers made a simple-minded mistake.
*  They assumed when you walk it's step, step, step and it's back and forth motion.
*  But when you walk it's also right foot left foot side to side motion.
*  The side to side motion for which the bridge was strong enough but it wasn't stiff enough.
*  And as a result you would feel the motion and you'd fall into step with it.
*  And people were very uncomfortable with it.
*  They closed the bridge for two years while they built stiffening for it.
*  Now nerves, look, nerve cells produce action potentials.
*  You have a bunch of cells which are loosely coupled together producing action potentials
*  of the same rate.
*  There'll be some circumstances under which these things can lock together.
*  Other circumstances in which they won't.
*  While they fire together you can be sure that other cells are going to notice it.
*  So you can make a computational feature out of this in an evolving brain.
*  Most artificial neural networks don't even have action potentials let alone
*  have the possibility for synchronizing them.
*  And you mentioned the evolutionary process.
*  The evolutionary process that builds on top of biological systems leverages that
*  the weird mess of it somehow.
*  So how do you make sense of that ability to leverage all the different kinds of complexities
*  in the biological brain?
*  Well, look, in the biological molecule level you'd have a piece of DNA which would encode
*  for a particular protein.
*  You could duplicate that piece of DNA and now one part of it can code for that protein
*  but the other one could itself change a little bit and thus start coding for a molecule
*  which is slightly different.
*  Now that molecule was just slightly different.
*  Had a function which helped any old chemical reaction was important to the cell.
*  You would go ahead and let that try and evolution would slowly improve that function.
*  And so you have the possibility of duplicating and then having things drift apart.
*  One of them retain the old function.
*  The other one do something new for you.
*  And there's evolutionary pressure to improve.
*  Look, there isn't in computers too but improvement has to do with closing some companies
*  and opening some others.
*  The evolutionary process looks a little different.
*  Similar time scale perhaps.
*  Much shorter in time scale.
*  Companies close, yeah, go bankrupt and are born.
*  Shorter.
*  But not much shorter.
*  Some companies last a century.
*  But yeah, you're right.
*  I mean if you think of companies as a single organism that builds and you all know,
*  yeah, that's a fascinating dual correspondence there between biological and...
*  And companies have difficulty having a new product competing with an old product.
*  And when IBM built its first PC, you probably read the book,
*  they made a little isolated internal unit to make the PC.
*  And for the first time in IBM's history, they didn't insist that you build it out of IBM
*  components.
*  But they understood that they could get into this market,
*  which is a very different thing by completely changing their culture.
*  And biology finds other markets in a more adaptive way.
*  Yeah, it's better at it.
*  It's better at that kind of integration.
*  So maybe you've already said it, but what to use the most beautiful aspect or mechanism
*  of the human mind?
*  Is it the adaptive, the ability to adapt as you've described,
*  or is there some other little quirk that you particularly like?
*  Adaptation is everything when you get down to it.
*  But the difference, there are differences between adaptation,
*  where your learning goes on only over generations, over evolutionary time,
*  where your learning goes on at the time scale of one individual who must learn from the
*  environment during that individual's lifetime.
*  And biology has both kinds of learning in it.
*  And the thing which makes neurobiology hard is that it's a mathematical system as it were
*  built on this other kind of evolutionary system.
*  What do you mean by mathematical system?
*  Where is the math and the biology?
*  Well, when you talk to a computer scientist about neural networks, it's all math.
*  And the fact that biology actually came about from evolution, and the fact that biology is about
*  a system which you can build in three dimensions.
*  If you look at computer chips, computer chips are basically two-dimensional structures,
*  maybe 2.1 dimensions, but they really have the same structure.
*  They really have difficulty doing three-dimensional wiring.
*  Biology is neocortex, it's actually also sheet-like, and it sits on top of the white matter,
*  which is about 10 times the volume of the gray matter and contains all what you might call the
*  wires.
*  But there's a huge, the effect of computer structure on what is easy and what is hard
*  is immense.
*  And biology does, it makes some things easy that are very difficult to understand how to do
*  computationally.
*  On the other hand, you can't do simple floating-point arithmetic, so it's awfully stupid.
*  And you're saying this kind of three-dimensional complicated structure makes, it's still math,
*  it's still doing math.
*  The kind of math it's doing enables you to solve problems of a very different kind.
*  That's right, that's right.
*  So you mentioned two kinds of adaptation, the evolutionary adaptation and the adaptation,
*  or learning at the scale of a single human life.
*  Which is particularly beautiful to you and interesting from a research and from just
*  a human perspective?
*  And which is more powerful?
*  I find things most interesting that I begin to see how to get into the edges of them
*  and tease them apart a little bit to see how they work.
*  And since I can't see the evolutionary process going on, I'm in awe of it.
*  But I find it just a black hole as far as trying to understand what to do.
*  And so in a certain sense, I'm in awe of it, but I couldn't be interested in working on it.
*  The human life's time scale is however thing you can tease apart and study.
*  Yeah, you can do it.
*  There's developmental neurobiology which understands how the connections
*  and how the structure evolves from a combination of what the genetics is like
*  and the fact that you're building a system in three dimensions.
*  In just days and months, those early days of a human life are really interesting.
*  They are.
*  And of course, there are times of immense cell multiplication.
*  There are also times of the greatest cell death in the brain during infancy.
*  It's turnover.
*  So what is not effective, what is not wired well enough to use the moment, throw it out.
*  It's a mysterious process.
*  Let me ask, from what field do you think the biggest breakthroughs
*  in understanding the mind will come in the next decades?
*  Is it neuroscience, computer science, neurobiology, psychology, physics, maybe math, maybe literature?
*  Well, of course, I see the world always through a lens of physics.
*  I grew up in physics and the way I pick problems is very characteristic of physics
*  and of an intellectual background which is not psychology, which is not chemistry,
*  and so on and so on.
*  Both of your parents were physicists?
*  Both of my parents were physicists.
*  And the real thing I got out of that was a feeling that the world is an understandable place.
*  And if you do enough experiments and think about what they mean and structure things
*  that you can do the mathematics of the relevant to the experiments,
*  you also be able to understand how things work.
*  But that was a few years ago.
*  Did you change your mind at all?
*  Through many decades of trying to understand the mind,
*  of studying in different kinds of ways, not even the mind, just biological systems.
*  You still have hope that physics that you can understand.
*  There's a question of what do you mean by understand?
*  Of course.
*  When I taught freshman physics, I used to say,
*  I wanted to get physics to understand the subject, to understand Newton's laws.
*  I didn't want them simply to memorize a set of examples to which they knew the equations
*  to write down to generate the answers.
*  I had this nebulous idea of understanding.
*  So that if you looked at a situation, you could say,
*  oh, I expect the ball to make that trajectory.
*  Or I expect some intuitive notion of understanding.
*  And I don't know how to express that very well.
*  I've never known how to express it well.
*  And you run smack up against it when you look at these simple neural nets,
*  feed forward neural nets, which do amazing things.
*  And yet, you know, contain nothing of the essence of what I would have felt was understanding.
*  Understanding is more than just an enormous lookup table.
*  Let's linger on that.
*  How sure you are of that?
*  What if the table gets really big?
*  So, I mean, ask another way.
*  These feed forward neural networks, do you think they'll ever understand?
*  Could answer that in two ways.
*  I think if you look at real systems,
*  feedback is an essential aspect of how these real systems compute.
*  On the other hand, if I have a mathematical system with feedback,
*  I know I can unlayer this and do it.
*  But I have an exponential expansion in the amount of stuff I have to build
*  if I can solve the problem that way.
*  So feedback is essential.
*  So we can talk even about recurrent, so recurrence.
*  But do you think all the pieces are there to achieve understanding?
*  With these simple mechanisms, like back to our original question,
*  what is the fundamental?
*  Is there a fundamental difference between artificial neural networks and biological?
*  Or is it just a bunch of surface stuff?
*  Suppose you ask a neurosurgeon, when is somebody dead?
*  Yeah.
*  They'll probably go back to saying, well, I can look at the brain rhythms
*  and tell you this is a brain which is never going to function again.
*  This one is, this other one is one that's if we treat it well, it's still recoverable.
*  And then just do that by some electrodes looking at simple electrical patterns.
*  This don't look in any detail at all at what individual neurons are doing.
*  These rhythms are utterly absent from anything which goes on at Google.
*  Yeah, but the rhythms.
*  But the rhythms what?
*  So, well, that's like comparing.
*  Okay, I'll tell you, it's like you're comparing
*  the greatest classical musician in the world to a child first learning to play.
*  The question I'm at, but they're still both playing the piano.
*  I'm asking, is there, will it ever go on at Google?
*  Do you have a hope?
*  Because you are one of the seminal figures in both launching both disciplines,
*  both sides of the river.
*  I think it's going to go on generation after generation the way it has where,
*  what you might call the AI computer science community says,
*  let's take the following.
*  This is our model of neurobiology at the moment.
*  Let's pretend it's good enough and do everything we can with it.
*  And it does interesting things.
*  And after a while, it sort of grinds into the sand.
*  And you say, ah, something else is needed for neurobiology.
*  And some other grand thing comes in and enables you to go a lot further.
*  But we'll go into the sand again.
*  And I think there could be generations of this evolution.
*  I don't know how many of them.
*  And each one is going to get you further into what a brain does.
*  And in some sense, pass the Turing test longer.
*  And for more broad aspects.
*  And how many of these are there are going to have to be before you say,
*  I've made something, I've made a human.
*  I don't know.
*  But your sense is it might be a couple.
*  My sense is it might be a couple more.
*  Yeah.
*  And going back to my brain waves as it were.
*  Yes.
*  From the AI point of view, they would say, ah, maybe these are an
*  epiphenomenon and not important at all.
*  The first car I had, a real wreck of a 1936 Dodge,
*  go above about 45 miles an hour and the wheels was shimmy.
*  Yeah.
*  Good speedometer that.
*  Now, nobody designed the car that way.
*  The car is malfunctioning to have that.
*  But in biology, if it were useful to know, when are you going more than 45 miles an hour,
*  you just capture that and you wouldn't worry about where it came from.
*  Yeah.
*  It's going to be a long time before that kind of thing, which can take place
*  in large complex networks of things is actually used in the computation.
*  Look, how many transistors are there in your laptop these days?
*  Actually, I don't know the number.
*  It's on the scale of 10 to the 10.
*  I can't remember the number either.
*  Yeah.
*  And all the transistors are somewhat similar and most physical systems
*  with that many parts, all of which are similar, have collective properties.
*  Yes.
*  Sound waves and air, earthquakes, what have you, have collective properties, weather.
*  There are no collective properties used in artificial neural networks, in AI.
*  Yeah, it's very...
*  If biology uses them, it's going to take us to more generations of things to
*  for people to actually dig in and see how they are used and what they mean.
*  See, you're very right.
*  We might have to return several times to neurobiology and try to make our transistors more messy.
*  Yeah, yeah.
*  At the same time, the simple ones will conquer big aspects.
*  Conquer big aspects.
*  I think one of the most biggest surprises to me was
*  how well learning systems as are manifesting non-biological,
*  how important they can be actually and how important and how useful they can be in AI.
*  So if we can just take a stroll to some of your work, that is incredibly surprising
*  that it works as well as it does that launched a lot of the recent work with neural networks.
*  If we go to what are now called Hopfield networks,
*  can you tell me what is associative memory in the mind for the human side?
*  Let's explore memory for a bit.
*  Okay, what you mean by associative memory is...
*  You have a memory of each of your friends.
*  Your friend has all kinds of properties from what they look like,
*  what their voice sounds like, where they went to college, where you met them,
*  go on and on, what science papers they've written.
*  What science papers they've written.
*  If I start talking about a 5'10", wired cognitive scientist who's got a very bad back,
*  it doesn't take very long for you to say, oh, he's talking about Jeff Hinton.
*  I never mentioned the name or anything very particular.
*  But somehow a few facts are associated with a particular person and it enables you to get a
*  hold of the rest of the facts, or not the rest of them, another subset of them.
*  And it's this ability to link things together, link experiences together,
*  which goes on to the general name of associative memory.
*  And a large part of intelligent behavior is actually just large associative memories
*  at work, as far as I can see.
*  What do you think is the mechanism of how it works in the mind?
*  Is it a mystery to you still?
*  Do you have inklings of how this essential thing for cognition works?
*  What I made 35 years ago was, of course, a crude physics model to show the kind,
*  to actually enable you to understand my old sense of understanding as a physicist,
*  because you could say, ah, I understand why this goes to stable states.
*  It's like things going downhill.
*  Right.
*  And that gives you the ability to understand the whole thing.
*  That gives you something with which to think in physical terms rather than only in mathematical
*  terms.
*  So you've created these associative artificial networks.
*  That's right.
*  Now, if you look at what I did, I didn't at all describe a system which gracefully learns.
*  I described a system in which you could understand how learning could link things together,
*  how very crudely it might learn.
*  One of the things which intrigues me as I reinvestigate that system now to some extent is,
*  look, I'll see you every second for the next hour or what have you.
*  Each look at you is a little bit different.
*  I don't store all those second by second images.
*  I don't store 3,000 images.
*  I somehow compact this information.
*  So I now have a view of you which I can use.
*  It doesn't slavishly remember anything in particular, but it compacts the information
*  into useful chunks which are somehow these chunks which are not just activities of neurons,
*  bigger things than that, which are the real entities which are useful to you.
*  Useful to you to describe, to compress this information coming at you.
*  And you have to compress it in such a way that if the information comes in just like this again,
*  I don't bother about there to rewrite it or efforts to rewrite it.
*  Simply do not yield anything because those things are already written.
*  And that needs to be not look this up, have you written this?
*  I've stored it somewhere already.
*  There'd be something which is much more automatic in the machine hardware.
*  Right.
*  So in the human mind, how complicated is that process?
*  Do you think?
*  So you've created, it feels weird to be sitting with John Hopfield calling him Hopfield Networks.
*  It is weird.
*  Yeah, but nevertheless, that's what everyone calls him.
*  So here we are.
*  So that's a simplification.
*  That's what a physicist would do.
*  You and Richard Feynman sat down and talked about associative memory.
*  Now, if you look at the mind where you can't quite simplify it so perfectly, do you think?
*  Let me backtrack just a little bit.
*  Biology is about dynamical systems.
*  Computers are dynamical systems.
*  You can ask if you want to model biology, if you want to model neurobiology,
*  what is the time scale?
*  There's a dynamical system in which, a fairly fast time scale in which you could say,
*  the synapses don't change much during this computation.
*  So I'll think of the synapses fixed and just do the dynamics of the activity.
*  Or you can say, the synapses are changing fast enough that I have to have the synaptic dynamics
*  working at the same time as the system dynamics in order to understand the biology.
*  If you look at the feedforward artificial neural nets, they're all done as learnings.
*  First of all, I spend some time learning, not performing, then I turn off learning and I perform.
*  Right.
*  That's not biology.
*  And so as I look more deeply at neurobiology, even at associative memory,
*  I've got to face the fact that the dynamics of the synapse change is going on all the time.
*  And I can't just get by by saying I'll do the dynamics of activity with fixed synapses.
*  So the dynamics of the synapses is actually fundamental to the whole system?
*  Yeah.
*  And there's nothing necessarily separating the time scales.
*  When time scales can be separated, it's neat from the physicists,
*  the mathematicians point of view, but it's not necessarily true in neurobiology.
*  So you're kind of dancing beautifully between showing a lot of respect to physics
*  and then also saying that physics cannot quite reach the level of the system.
*  Physics cannot quite reach the complexity of biology.
*  So where do you land or do you continuously dance between the two?
*  I continuously dance between them because my whole notion of understanding
*  is that you can describe to somebody else how something works in ways which are honest and
*  believable and still not describe all the nuts and bolts in detail.
*  Weather. I can describe weather
*  as 10 to the 32 molecules colliding in the atmosphere.
*  I can simulate weather that way if I have a big enough machine. I'll simulate it accurately.
*  It's no good for understanding.
*  I want to understand things in terms of wind patterns, hurricanes,
*  pressure differentials and so on. All things as they're collective.
*  And the physicist in me always hopes that biology will have some things which can be said about it
*  was they're both true and for which you don't need all the molecular details of the molecules
*  colliding. That's what I mean from the roots of physics by understanding.
*  So what did, again sorry, but Hopfield networks help you understand what insight
*  did give us about memory, about learning?
*  They didn't give insights about learning. They gave insights about how things having learned
*  could be expressed. How having learned, a picture of you reminds me of your name.
*  That would, but it didn't describe a reasonable way of actually doing the learning.
*  They only said if you had previously learned the connections of this kind of pattern,
*  would now be able to behave in a physical way with the day off. If I put the part of the pattern
*  in here, the other part of the pattern will complete over here. I can understand that physics,
*  if the right learning stuff had already been put in. And you could understand why then putting in
*  a picture of somebody else would generate something else over here.
*  But it did not have a reasonable description of the learning process.
*  But even, so forget learning, I mean that's just a powerful concept that
*  sort of forming representations that are useful to be robust for error correction kind of thing.
*  So this is kind of what the biology does that we're talking about.
*  This is kind of what the biology does that we're talking about.
*  And what BiPaper did was simply enable you, there are lots of ways of being robust.
*  If you think of a dynamical system, you think of a system where a path is going on in time.
*  And if you think of a computer, there's a computational path which is going on
*  in a huge dimensional space of ones and zeros. And an error correction system is a system which,
*  if you get a little bit off that trajectory, will push you back onto that trajectory again.
*  So you get to the same answer in spite of the fact that there were things,
*  the computation wasn't being ideally done all the way along the line.
*  And there are lots of models for error correction. But one of the models for error correction is
*  to say there's a valley that you're following, flowing down. And if you push a little bit off
*  the valley, just like water being pushed a little bit by a rock, it gets back and follows the course
*  of the river. And that basically the analog in the physical system, which enables you to say,
*  oh yes, error-free computation and associative memory are very much like things that I can
*  understand from the point of view of a physical system. The physical system can be, under some
*  circumstances, an accurate metaphor. It's not the only metaphor. There are error correction schemes
*  which don't have a valley, an energy behind them. But those are error correction schemes
*  which a mathematician may be able to understand, but I don't.
*  RICK So there's the physical metaphor that seems to work here.
*  JOHN That's right. That's right.
*  RICK So these kinds of networks actually led to a lot of the work that is going on now in neural
*  networks, artificial neural networks. So the follow-on work with restricted bolson machines
*  and deep belief nets followed on from these ideas of the Hopfield network. So what do you think about
*  this continued progress of that work towards now re-vigorated exploration of feedforward
*  neural networks and recurrent neural networks and convolutional neural networks and
*  kinds of networks that are helping solve image recognition, natural language processing,
*  all that kind of stuff?
*  JOHN It's always intrigued me that one of the most long-lived of the learning systems
*  is the Boltzmann machine, which is intrinsically a feedback network.
*  And with the brilliance of Hinton and Sinowski to understand how to do learning in that,
*  and it's still a useful way to understand learning and understand,
*  and the learning that you understand in that has something to do with the way that feedforward
*  systems work, but it's not always exactly simple to express that intuition. But it always amuses me
*  to see Hinton going back to the will yet again on a form of the Boltzmann machine because really
*  that which has feedback and interesting probabilities in it is a lovely encapsulation
*  of something computational.
*  LARSON Something computational?
*  JOHN Something both computational and physical. Computational, and it's very much related to
*  feedforward networks. Physical in that Boltzmann machine learning is really learning itself
*  parameters for a physics Hamiltonian or energy function.
*  LARSON What do you think about learning in this whole domain? Do you think, the aforementioned
*  guy, Jeff Hinton, all the work there with backpropagation, all the kind of
*  learning that goes on in these networks, how do you, if it comes to the network,
*  how do you, if we compare it to learning in the brain, for example, is there echoes of the same
*  kind of power that backpropagation reveals about these kinds of recurrent networks?
*  Or is it something fundamentally different going on in the brain?
*  JOHN I don't think the brain is as deep as the deepest networks go, the deepest computer science
*  networks. And I do wonder whether part of that depth of the computer science networks is
*  necessitated by the fact that the only learning that's easily done on the machine is feedforward.
*  And so there's the question of to what extent has the biology, which has some feedforward and
*  some feedback, been captured by something which has got many more neurons, much more depth than
*  neurons. You know?
*  J. So part of you wonders if the feedback is actually more essential than the number of
*  neurons or the depth, the dynamics of the feedback.
*  JOHN The dynamics of the feedback. Look, if you don't have feedback, it's a little bit like
*  building a big computer and running it through one clock cycle. And then you can't do anything,
*  do you put, you reload something coming in. How do you use the fact that there are multiple
*  clocks like, how do I use the fact that you can close your eyes, stop listening to me,
*  and think about a chessboard for two minutes without any input whatsoever?
*  J. Yeah, that memory thing, that's fundamentally a feedback kind of mechanism. You're going back
*  to something. Yes. It's hard. It's hard. It's hard to understand. It's hard to introspect,
*  let alone consciousness.
*  JOHN Oh, let alone consciousness. Yes. Yes.
*  J. Because that's tied up in there too. You can't just put that on another shelf.
*  JOHN Every once in a while I got interested in consciousness and then I go and I've done that
*  for years and ask one of my betters, as it were, their view on consciousness. It's been
*  interesting collecting them.
*  J. What is consciousness? Let's try to take a brief step into that room.
*  JOHN Well, I asked Marvin Minsky, the view on consciousness, and Marvin said,
*  consciousness is basically overrated. It may be an epiphenomenon. After all, all the things your
*  brain does, which are actually hard computations, you do non-consciously. And there's so much
*  evidence that even the simple things you do, you can make decisions, you can make committed decisions
*  about them. The neurobiologists can say, he's now committed. He's going to move the hand left
*  before you know it.
*  J. So his view that consciousness is not, that's just like little icing on the cake.
*  The real cake is in the subconscious.
*  JOHN Yeah. Subconscious. Non-conscious.
*  J. Non-conscious. That's the better word, sir.
*  JOHN It's only that Freud captured the other word.
*  J. Yeah. That's a confusing word, subconscious.
*  Nicholas Chater wrote an interesting book. I think the title of it is The Mind is Flat.
*  And flat in a neural net sense, it might be flat as something which is a very broad neural net
*  without really many layers in depth, or the deep brain would be many layers and not so broad.
*  In the same sense that if you push Minsky hard enough, he would probably have said,
*  consciousness is your effort to explain to yourself that which you have already done.
*  JOHN Yeah. It's the weaving of the narrative around the things that have already been computed for
*  you. J. That's right. And so much of what we do for our memories of events, for example,
*  if there's some traumatic event you witness, you will have a few facts about it correctly done.
*  If somebody asks you about it, you will weave a narrative which is actually much more rich in
*  detail than that based on some anchor points you have of correct things. And pulling together
*  general knowledge on the other, but you will have a narrative. And once you generate that narrative,
*  you are very likely to repeat that narrative and claim that all the things you have in it
*  are actually the correct things. There was a marvelous example of that in the
*  Watergate slash impeachment era of John Dean. John Dean, you're too young to know, had been the
*  personal lawyer of Nixon. And so John Dean was involved in the cover-up and
*  John Dean ultimately realized the only way to keep himself out of jail for a long time
*  was actually to tell some of the truths about Nixon. And John Dean was a tremendous witness.
*  He would remember these conversations in great detail and very convincing detail.
*  And long afterward, some of the tapes, the secret tapes as it were, from which these,
*  John was, Gene was recalling these conversations were published. And one found out that John Dean
*  had a good but not exceptional memory. What he had was an ability to paint vividly and in some sense
*  and in some sense accurately the tone of what was going on.
*  By the way, that's a beautiful description of consciousness.
*  Do you, like where do you stand in your today? So perhaps it changes day to day, but
*  where do you stand on the importance of consciousness in our whole big mess of cognition?
*  Is it just a little narrative maker or is it actually fundamental to intelligence?
*  That's a very hard one. When I asked Francis Crick about consciousness,
*  he launched forward a long monologue about Mendel and the peas and how Mendel knew that
*  there was something. And how biologists understood there was something in inheritance,
*  which was just very, very different. And the fact that inherited traits didn't just wash out into a
*  gray, but were this or this and propagated. That was absolutely fundamental to biology.
*  And it took generations of biologists to understand that there was genetics and it
*  took another generation or two to understand that genetics came from DNA. But very shortly after
*  Mendel, thinking biologists did realize that there was a deep problem about inheritance.
*  And Francis would have liked to have said, and that's why I'm working on consciousness.
*  But of course he didn't have any smoking gun in the sense of Mendel.
*  And that's the weakness of his position. If you read his book, what you wrote with Koch, I think.
*  Yeah, Kristoff Koch, yeah.
*  I find it unconvincing for the smoking gun reason.
*  So I'm going on collecting views without actually having taken a very strong one myself,
*  because I haven't seen the entry point. Not seeing the smoking gun,
*  and the point of view of physics, I don't see the entry point. Whereas in neurobiology,
*  once I understood the idea of a collective evolution of dynamics, which could be described
*  as a collective phenomenon, I thought, ah, there's a point where what I know about physics is so
*  different from any neurobiologist that I have something that I might be able to contribute.
*  And right now there's no way to grasp at consciousness from a physics perspective.
*  From my point of view, that's correct. And of course, people, physicists, like everybody else,
*  think very buddily about things. You ask the closely related question about free will. Do
*  you believe you have free will? Physicists will give an offhand answer and then backtrack,
*  backtrack, backtrack, where they realize that the answer they gave must fundamentally contradict
*  the laws of physics. Answering questions of free will and consciousness naturally lead to
*  contradictions from a physics perspective, because it eventually ends up with quantum mechanics,
*  and then you get into that whole mess of trying to understand how much, from a physics perspective,
*  how much is determined, already predetermined, how much is already deterministic about our universe.
*  And if you don't push quite that far, you can say, essentially all of neurobiology,
*  which is relevant, can be captured by classical equations of motion.
*  Because in my view, the mysteries of the brain are not the mysteries of quantum mechanics,
*  but the mysteries of what can happen when you have a dynamical system,
*  driven system, with 10 of the 14 parts. That complexity is something which is,
*  the physics of complex systems is at least as badly understood
*  as the physics of phase coherence in quantum mechanics.
*  Can we go there for a second? You've talked about attractor networks,
*  and just maybe you could say what are attractor networks, and more broadly,
*  what are interesting network dynamics that emerge in these or other complex systems?
*  You have to be willing to think in a huge number of dimensions, because in a huge number of
*  dimensions, the behavior of a system can be thought of as just the motion of a point over time
*  in this huge number of dimensions. And an attractor network is simply a network where there is
*  a line, and other lines converge on it in time. That's the essence of an attractor network.
*  In a highly dimensional space.
*  And the easiest way to get that is to do it in a highly dimensional space,
*  where some of the dimensions provide the dissipation, which makes, which,
*  like I have a physical system, trajectories can't contract everywhere. They have to contract in
*  some places and expand in others. There's a fundamental classical theorem of statistical
*  mechanics, which goes under the name of Liouville's theorem, which says you can't contract everywhere.
*  You have to, if you contract somewhere, you expand somewhere else.
*  And it's an interesting physical systems. You get driven systems where you have a small subsystem,
*  which is the interesting part. And the rest of the contraction and expansion, the physicists
*  would say, is entropy flow in this other part of the system. But basically, attractor networks are
*  dynamics funneling down so that you can't be any, so that if you start somewhere in the dynamical
*  system, you will soon find yourself on a pretty well-determined pathway, which goes somewhere.
*  You start somewhere else, you'll wind up on a different pathway. But you don't have just
*  all possible things. You have some defined pathways which are allowed and onto which you will converge.
*  And that's the way you make a stable computer and that's the way you make a stable behavior.
*  So in general, looking at the physics of the emergent stability in these networks,
*  what are some interesting characteristics that, what are some interesting insights from studying
*  the dynamics of such high dimensional systems? Most dynamical systems, most dynamical systems
*  driven dynamical systems, by driven they're coupled somehow to an energy source.
*  And so their dynamics keeps going because it's coupling to the energy source.
*  Most of them, it's very difficult to understand at all what the dynamical
*  behavior is going to be. You have to run it. You have to run it. There's a subset of systems
*  which has what exactly known to the mathematicians as a Lyapunov function.
*  And those systems, you can understand convergent dynamics by saying you're going downhill on
*  something or other. And that's what I found with ever knowing what the Lyapunov functions were
*  in the simple model I made in the early 80s, was an energy function so you could understand
*  how you could get this channeling on the pathways without having to follow the dynamics in
*  infinite detail. You started rolling a ball on the top of a mountain, it's going to wind up
*  at the bottom of the valley. You know that's true without actually watching the ball roll down.
*  There are certain properties of the system that when you can know that.
*  That's right. And not all systems behave that way.
*  Most don't probably.
*  Most don't, but it provides you with a metaphor for thinking about systems which are stable and
*  who to have these attractors behave even if you can't find a Lyapunov function behind them or an
*  energy function behind them. It gives you a metaphor for thought.
*  CB speaking of thought, if I had a glint in my eye with excitement and said,
*  I'm really excited about this something called deep learning and neural networks,
*  and I would like to create an intelligence system and came to you as an advisor,
*  what would you recommend? Is it a hopeless pursuit to use neural networks to achieve thought?
*  Is it what kind of mechanisms should we explore? What kind of ideas should we explore?
*  Well, you look at the simple networks, web one past networks,
*  they don't support multiple hypotheses very well.
*  As I have tried to work with very simple systems which do something which you might consider to be
*  thinking, thought has to do with the ability to do mental exploration before you make take a physical
*  action.
*  Almost like we were mentioning, playing chess, visualizing, simulating,
*  inside your head different outcomes.
*  Yeah, yeah. You could do that in a feed forward network because you've pre-calculated all kinds
*  of things. I think the way neurobiology does it, it hasn't pre-calculated everything. It actually
*  has parts of a dynamical system in which you're doing exploration.
*  There's a creative element.
*  There's a creative element and in a simple minded neural net, you have a
*  constellation of instances from which you can actually see the world.
*  Neural net, you have a constellation of instances from which you've learned.
*  If you are within that space, if a new question is a question within this space,
*  you can actually rely on that system pretty well to come up with a good suggestion for
*  what to do. If on the other hand, the query comes from outside the space,
*  you have no way of knowing how the system is going to behave. There are no limitations
*  on what could happen. The artificial neural net world is always very much, I have a
*  population of examples. The test set must be drawn from the equivalent population.
*  The test set has examples which are from a population which is completely different.
*  There's no way that you could expect to get the answer right.
*  What they call outside the distribution.
*  That's right. If you see a ball rolling across the street in dusk,
*  if that wasn't in your training set, the idea that a child may be coming close behind that
*  is not going to occur with the neural net.
*  And it is to our, there's something in the neurobiology that allows that.
*  Yeah. There's something in the way of what it means to be outside of the population of the
*  training set. The population of the training set isn't just sort of this set of examples.
*  There's more to it than that. It gets back to my question of what is it to understand something.
*  Yeah. In a small tangent, you've talked about the value of thinking of deductive reasoning
*  in science versus large data collection. So sort of thinking about the problem. I suppose it's
*  the physics side of you of going back to first principles and thinking, but what do you think
*  is the value of deductive reasoning in the scientific process? Well, there are obviously
*  scientific questions in which the root to the answer to it comes through the analysis of one
*  hell of a lot of data. Right. Cosmology, that kind of stuff. And that's never been the kind of problem
*  in which I've had any particular insight. Though I must say, if you look at
*  cosmology is one of those. But if you look at the actual things that Jim Peebles, one of this year's
*  Nobel Prize in physics, one's from the local physics department, the kinds of things he's done,
*  he's never crunched large data. Never, never, never. He's used the encapsulation of the work
*  of others in this regard. But ultimately boiled down to thinking through the problem. What are the
*  principles under which a particular phenomenon operates? Yeah. And look, physics is always
*  going to look for ways in which you can describe the system in a way which rises above the details.
*  And to the hard-died and the wool biologist, biology works because of the details. In physics,
*  to the physicists, we want an explanation which is right in spite of the details. And there will be
*  questions which we cannot answer as physicists because the answer cannot be found that way.
*  There's, I'm not sure if you're familiar with the entire field of brain-computer interfaces.
*  That's become more and more intensely researched and developed recently, especially with companies
*  like Neuralink with Elon Musk. Yeah, I know there have always been the interest both in
*  things like getting the eyes to be able to control things or getting the thought patterns
*  to be able to move what had been a connected limb which is now connected through a computer.
*  That's right. So in the case of Neuralink, they're doing a thousand plus connections where they're
*  able to do two-way activate and read spikes, neural spikes. Do you have hope for that kind
*  of computer brain interaction in the near or maybe even far future of being able to expand
*  the ability of the mind of cognition or understand the mind?
*  It's interesting watching things go. When I first became interested in neurobiology,
*  most of the practitioners thought you would be able to understand neurobiology
*  by techniques which allowed you to record only one cell at a time. One cell, yeah.
*  People like David Hubel very strongly reflected that point of view.
*  And that's been taken over by a generation, a couple of generations later by a set of people
*  who says not until we can record from 10 to the four or 10 to the five at a time,
*  will we actually be able to understand how the brain actually works. And in a general sense,
*  I think that's right. You have to look, you have to begin to be able to look for the collective
*  modes, the collective operation of things. It doesn't rely on this action potential of that cell.
*  It relies on the collective properties of this set of cells connected with this kind of patterns
*  and so on. And you're not going to succeed in seeing what those collective activities are without
*  recording many cells at once. The question is how many at once? What's the threshold?
*  And that's the... Yeah, and look, it's being pursued hard in the motor cortex. The motor cortex
*  does something which is complex and yet the problem you're trying to address is fairly simple.
*  Now neurobiology does it in ways that differ from the way an engineer would do it. An engineer would
*  put in six highly accurate stepping motors controlling a limb rather than 100,000 muscle
*  fibers, each of which has to be individually controlled.
*  And so understanding how to do things in a way which is much more forgiving and much more neural
*  I think would benefit the engineering world.
*  The engineering world, a touch. Let's put in a pressure sensor or two, rather than an array of
*  gazillion pressure sensors, none of which are accurate, all of which are perpetually
*  recalibrating themselves. So you're saying your hope is, your advice for the engineers of the future
*  is to embrace the large chaos of a messy, error-prone system like those of the biological systems.
*  That's probably the way to solve some of these. I think you'll be able to make
*  better computations slash robotics that way than by
*  trying to force things into a robotics where joint motors are powerful and stepping motors are
*  accurate. But then the physicists, the physicists in you will be lost forever in such systems
*  because there's no simple fundamentals to explore in systems that are so
*  large and messy. Well, you say that, and yet there's a lot of physics in the Navier-Stokes equations,
*  the equations of nonlinear hydrodynamics, huge amount of physics in them. All the physics of
*  atoms and molecules has been lost, but it's been replaced by this other set of equations, which is
*  just as true as the equations at the bottom. Now, those equations, they're not just equations,
*  are going to be harder to find in neurobiology. But the physicist in me says there are probably
*  some equations of that sort. They're out there. They're out there. And if physics is going to
*  contribute anything, it may contribute to trying to find out what those equations are and how to
*  capture them from the biology. Would you say that's one of the main open problems of our age,
*  is to discover those equations? Yeah. If you look at, there's molecules
*  and there's psychological behavior. And these two are somehow related. They're layers of detail,
*  they're layers of collectiveness. And to capture that in some vague way,
*  several stages on the way up to see how these things can actually be linked together.
*  So it seems in our universe, there's a lot of elegant equations that can describe the fundamental
*  way that things behave, which is a surprise. I mean, it's compressible into equations. It's
*  simple and beautiful. But it's still an open question whether that link is equally between
*  molecules and the brain is equally compressible into elegant equations. But you're both a physicist
*  and a dreamer. You have a sense that... Yeah, but I can only dream physics dreams.
*  Physics dreams. There was an interesting book called Einstein's Dreams, which alternates between
*  the chapters on his life and descriptions of the way time might have been, but isn't.
*  The linking between these being important ideas that Einstein might have had to think about the
*  essence of time as he was thinking about time. So speaking of the essence of time,
*  in your biology, you're one human, famous impactful human, but just one human with a brain
*  living the human condition. But you're ultimately mortal, just like all of us. Has studying the
*  mind as a mechanism changed the way you think about your own mortality?
*  It has really, because particularly as you get older and the body comes apart in various ways,
*  I became much more aware of the fact that what is somebody is contained in the body.
*  And it is to a certain extent true that for people who write things down, equations,
*  dreams, notes, and so on, that they're all very, very important. And so I think that's
*  the way that you're going to be able to do that. And I think that's the way that you're going to
*  be able to do that. And so I think that's the way that you're going to be able to do that.
*  Defractions, dreams, notepads, diaries, fractions of their thought does continue to live
*  after they're dead and gone, after their body is dead and gone. And there's a sea change in that
*  going on in my lifetime between when my father died, except for the things which were actually
*  written by him as it were. Very few facts about him will have ever been recorded.
*  And the number of facts which are recorded about each and every one of us
*  forever now as far as I can see in the digital world. And so the whole question
*  of what is death may be different for people a generation ago and a generation
*  further ahead. Maybe we have become immortal under some definitions. Yeah.
*  Last easy question. What is the meaning of life? Looking back you've studied the
*  mind as weird descendants of apes. What's the meaning of our existence on this?
*  Little earth. Oh that word meaning is as slippery as the word understand.
*  Interconnected somehow perhaps. Is there, it's slippery, but is there something
*  that you despite being slippery can hold long enough to express? I've been amazed
*  at how hard it is to define the things in a living system in the sense that one
*  hydrogen atom is pretty much like another. But one bacterium is not so much
*  like another bacterium even of the same nominal species. In fact the
*  whole notion of what is the species gets a little bit fuzzy. And species exist in
*  the absence of certain classes of environments. And pretty soon one winds
*  up with with a biology which the whole thing is living. But whether there's
*  actually any element of it which by itself would be said to be living, it
*  becomes a little bit vague in my mind. So in a sense the idea of meaning is
*  something that's possessed by an individual like a conscious creature.
*  And you're saying that it's all interconnected in some kind of way that
*  there might not even be an individual. We're all kind of this complicated mess
*  of biological systems at all different levels. Where the human starts and
*  when the human ends is unclear. Yeah and where the neurobiology where the
*  oh you say the neocortex is the thinking but there's a lot of the things that
*  are done on the spinal cord. And so we say where's the essence of thought? Is it
*  just gonna be neocortex? Can't be. Can't be. Yeah maybe to understand and to build
*  thought you have to build the universe along with the neocortex. It's all
*  interlinked through the spinal cord. John is a huge honor talking today. Thank
*  you so much for your time. I really appreciate it. Well thank you for the
*  challenge of talking with you and it'll be interesting to see whether you can
*  win five minutes out of this in a coherent sense to anyone. Beautiful.
*  Thanks for listening to this conversation with John Hopfield and
*  thank you to our presenting sponsor Cash App. Download it, use Code Lex podcast.
*  You'll get $10 and $10 will go to FIRST, an organization that inspires and
*  educates young minds to become science and technology innovators of tomorrow. If
*  you enjoy this podcast, subscribe on YouTube, give it five stars on Apple
*  podcast, support on Patreon, or simply connect with me on Twitter at Lex
*  Friedman. And now let me leave you with some words of wisdom from John Hopfield
*  in his article titled, Now What? Choosing problems is the primary determinant of
*  what one accomplishes in science. I have generally had a relatively short
*  attention span in science problems. Thus, I have always been on the lookout for
*  more interesting questions either as my present ones get worked out or as it get
*  classified by me as intractable given my particular talents. He then goes on to
*  say,
*  I have a great respect for them, especially for those
*  who are willing to attempt communication with someone
*  who is not an expert in the field.
*  I would only add that experts are good
*  at answering questions.
*  If you're brash enough, ask your own.
*  Don't worry too much about how you found them.
*  Thank you for listening and hope to see you next time.

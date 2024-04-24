---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4780s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 11067
Video Rating: None
---

# BI 021 Matt Botvinick: Neuroscience and AI at DeepMind
**Brain Inspired:** [December 12, 2018](https://www.youtube.com/watch?v=L-L6RBAbNYU)
*  It amuses me sometimes how much people who trained in computer science think we know
*  about the brain.
*  They come to me and ask, Matt, you know about the brain, how does the brain do exercise?
*  I hate to disappoint you, but why couldn't it be that AI systems are incredibly benevolent?
*  When we think about wisdom in studies of religion and spirituality, our usual assumption is
*  that insight leads to benevolence.
*  This is Brain Inspired.
*  Hey everyone, I am Paul Middlebrooks and the voice that you heard previously is that of
*  my guest today, Matt Botvinick.
*  Matt is the director of neuroscience research at a little company you might know called
*  DeepMind.
*  So DeepMind, as I'm sure you do know, is the AI research company behind systems like
*  AlphaZero that are demolishing all their opponents in games like chess and Go.
*  And of course they do a lot more.
*  The approach to artificial intelligence at DeepMind is heavily inspired by neuroscience.
*  And Matt and I discuss that approach and that philosophy.
*  We talk about reinforcement learning in AI and in brains.
*  We cover his work suggesting that the prefrontal cortex could work with the dopamine system
*  to together serve as a meta-learning system.
*  We also talk about his recent research into creating theory of mind in AI agents and a
*  lot more.
*  This episode is a little bit longer than usual.
*  with his time and as you'll hear he has a generous spirit as well.
*  That's right, I said spirit.
*  So I continue to love doing this podcast and I hope that you enjoy it.
*  A quick thank you to recent Patreon supporters Jay, Judith, The Stoic.
*  Thank you guys for helping me combat the ever present eye rolls I get from my wife whenever
*  I tell her that this is a worthwhile endeavor.
*  You guys are awesome.
*  You can find the show notes and learn how to support the show at braininspired.co.
*  Alright enjoy your time with Matt.
*  Alright, Matt Botvinick.
*  Thank you and welcome to the Brain Inspired podcast.
*  Thank you, it's a pleasure to be here.
*  You sir are the director of neuroscience research at DeepMind and you came to DeepMind via neuroscience
*  most recently from Princeton University.
*  You have a ton of accolades and areas that you've researched in neuroscience in the
*  past, kind of famous for conflict monitoring, cognitive control, the function of the anterior
*  cingulate cortex and on and on.
*  You and I actually have a common past partly.
*  You got your PhD at CMU, Carnegie Mellon University and you spent some time after that in the
*  neurobasis of cognition in Pittsburgh which is the program that I got my PhD in.
*  Oh wonderful.
*  I guess you were there pretty early on, right when it formed I suppose.
*  Yeah I was around when it took on that name and my PhD was actually through the CNBC and
*  yeah I definitely would not be where I am or doing the things that I'm doing today if
*  I hadn't had that training.
*  It was really fantastic.
*  Anything you miss about Pittsburgh?
*  Anything I miss about Pittsburgh?
*  I miss the french fries on the sandwiches.
*  Do you?
*  Yeah.
*  Pretty good, yeah.
*  It's changed a lot since I was there from what I understand but yeah I had a wonderful
*  time in Pittsburgh.
*  I don't think the french fries have changed though.
*  I think they're the same.
*  So this is interesting.
*  Before you got into neuroscience and cognitive neuroscience you were an art history major
*  so I would be amiss if I didn't ask you what you think of these new generative adversarial
*  networks that are generating these new artworks.
*  Do you have a take on those things?
*  It's funny when I first started spending time at DeepMind the generative models were shall
*  we say still in development compared to where they are now and they would when you know
*  the idea with the generative model is that you build an autoencoder so you feed in an
*  image and then it tries to reconstruct that image through a sort of coding bottleneck
*  but then you can flip a switch and use it to imagine new images and you hope that those
*  images if you're doing your job right then those images should essentially come from
*  the same distribution as the original and I remember when I first spent time at DeepMind
*  the images that were being generated in that second mode were quite beautiful and sort
*  of mysterious and they kind of seemed like things that would come out of a dream state
*  or something like that.
*  And so yeah I did I remember thinking jeez somebody should like pick some of these and
*  make a make a show out of it make a gallery show out of it and that may for all I know
*  have actually happened.
*  The problem is that the generative models have gotten better and better so now when
*  you put the system into generative mode it just produces something that looks like an
*  actual picture of a hamburger.
*  So they're not they're not nearly as aesthetic as they used to be.
*  They're far too realistic.
*  Well one of the portraits just sold at the famous I cannot soothe be soothe bees is that
*  right.
*  So if he's yeah just sold for a ton of money.
*  It didn't really.
*  Yeah yeah.
*  I hadn't seen that anyway.
*  I thought you know because I have an artist friend down the road here whom I thought I
*  should get him in the studio and just ask him like put up these pictures and ask him
*  what he thinks about the art the quality you know and things like that.
*  There's definitely something very there's there's something about the images that that
*  are produced by generative models especially of like a couple generations back you know
*  like last year that it's not just that they're interesting.
*  You have this feeling that they're tapping into something in your visual system.
*  There's something very primordial in your visual system and I don't think anybody really
*  understands why that's the case.
*  Like I say you know what's being produced now is much less interesting because the generative
*  models are so much better that they really do produce images that look photographic even
*  though they're not showing you you know they're not just duplicating some photograph that
*  was in the training set.
*  What I'm what I'm waiting for is synthetic music.
*  That'll be a big breakthrough.
*  People have been trying to do this with neural networks.
*  Since the days when I was at the CNBC in Pittsburgh and even back then what people were what people
*  found was that you could get so far as generating plausible melodies.
*  It is possible to build a system that learns from examples how to generate interesting
*  melodies. What wasn't working back then and I to be honest I don't know the state of the
*  art these days. It's not something that we're working on at DeepMind as far as I know.
*  But what wasn't in place were the long term dependencies.
*  You know the way that a movement of a symphony movement in sonata form will start with one
*  theme and then move on to a related theme and then move on to a related theme and then
*  there's a long development and then you come back to the original theme.
*  Right. There are these long time dependencies that play out over minutes tens of minutes
*  in some cases and at least back in the era when I was following this kind of work it
*  wasn't possible to for systems to learn those kinds of long term dependencies.
*  Interestingly we're coming back to that that problem in AI research now but that's right.
*  I'll be very excited when we get some some interesting music out of these systems.
*  Yeah. Well it is interesting because what we're going to talk about today is building
*  some well you know within general AI trying to build back some human intelligence into
*  these systems. So but so you have a background in cognitive neuroscience and you got into
*  AI later. I'm assuming you got into it later. What do you think should an aspiring student
*  who's interested in neuroscience and AI should should they master one or the other first
*  or is that a moot point now. Are they just studied together now. You know the cognitive
*  neuroscience and AI or or should they do it concurrently. What do you think.
*  So I I got into AI as it's now been redubbed right in a kind of in in imperceptible way
*  because what got me interested in in neuroscience and psychology was neural networks artificial
*  neural networks. And you know in the 90s and 2000s when I started doing this kind of work
*  there was this lovely lovely lack of clarity in terms of when we were doing psychology or
*  neuroscience and when we were just thinking about how to build an intelligent system.
*  And you know I ended up pursuing a career in neuroscience and cognitive psychology but all
*  along the way I've always kind of felt pulled toward just thinking about intelligence in general
*  from time to time. And one one thing that I'm really enjoying about working at DeepMind is
*  that I get to work both sides of the field without worrying too much day to day whether
*  I'm doing one or the other. But to get to your question I feel like that's a question that people
*  academia are wrestling with very actively both students who are looking at the very dynamic
*  landscape of opportunities that they'll have after they are done their training and also degree
*  programs who are looking at the same dynamic landscape and wondering how to set their students
*  up as best they can. I guess the answer I would give is that there's really no there's no one size
*  fits all. There are definitely large sectors of neuroscience research for which training in AI
*  is probably not the best use of your time if you're a grad student. I mean if you're you know if
*  you're interested in... Gleal cells. Exactly or you know receptor dynamics or you know that I you know
*  I just I don't think people should see this as a bandwagon that they have to get on if you're
*  interested in other aspects of neural function then maybe your best the best use of your time
*  is to study biology. You know I also don't think that everybody who's that who is into AI has to
*  go off and get a PhD in neuroscience. There are clearly aspects of AI research that can be pursued
*  quite fruitfully without knowing a thing about the brain. Right. You know as is proven by the
*  many people who are doing successful AI research right now. And for all that we for all we think
*  we know about the brain we know very little anyway. So and that's yeah and that's it amuses
*  me sometimes how much people who trained in computer science think we know about the brain.
*  They come to me and ask Matt you know you know about the brain how does the brain do
*  exercise I hate to disappoint you but isn't that we don't know. It's so frustrating to have to say
*  that. Okay well that that's a good answer. But I mean the yeah the the the final piece of that is
*  that there really is a growing area of overlap and you know there is there is a growing market
*  both in the literal economic sense and in the sort of more intellectual sense for people who speak
*  all of these languages. And I'm it's my hope that academia is is seeing that and is you know building
*  building curricula that are appropriate. I had to learn a lot of what I know about machine learning
*  and relevant areas of mathematics information theory optimization statistical inference. I had to
*  pick up a lot of that stuff once I was done with my degree because it just wasn't part of the
*  standard neuroscience and psychology curriculum. Right. And and I think you know I I hope and
*  expect that especially cognitive science oriented programs are building these interdisciplinary
*  curricula because I do think that that it's you know I think it's the answer both for AI to have
*  people around who understand what's going on to the extent that we do understand that. Right. In
*  the brain and for neuroscientists to really understand what it means to process information
*  if that's what the brain is actually doing. Right. Which of course it is. So man you what a job you
*  have what a title you have director of neuroscience research. Can you just describe briefly and
*  kind of an overall picture of your role and what you do you know on a day to day kind of basis and
*  what you oversee. Sure absolutely. We we organize things that DeepMind into groups that we call
*  teams and I'm the head of a team that we call the neuroscience team. In some ways it's a misnomer
*  because most of the people on the team are doing fairly like straightforward AI research. It does
*  turn out to be the case that most of the people doing that kind of research have at least
*  distantly some background in neuroscience or psychology or oriented maybe a little bit above
*  the mean for for DeepMind in questions that are very inspired by cognitive science or neuroscience.
*  But we have people on the team like Greg Wayne and Peter Battaglia Alex Lurchner who are writing
*  papers that you know if you if you just read the paper without knowing them you would you would
*  necessarily think of it as neuroscience or psychology work. But then we have other activities
*  on the team that really are more oriented toward neuroscience and the reason for that is not that
*  we're you know our primary mission is to solve intelligence that you know we're aligned with the
*  rest of the company in exactly that sense. But we think that working on questions in neuroscience
*  selected questions may help us get the answers that we need in order to make better AI systems. So
*  we do some neuroimaging, some fMRI work, we do computational neuroscience,
*  we do human behavioral experiments just like people do in university departments just to see
*  try to figure out what makes people so smart so we can try to bottle that and put it in our
*  in our artificial systems and we try to kind of find some way of making all of that activity
*  coherent. The other thing that we do is one challenge of the kind of AI work that we do
*  at DeepMind is that since it involves learning we often end up with systems that are doing
*  something that looks quite intelligent but we can't tell by just watching their behavior exactly how
*  they're doing what they're doing. So you end up with a problem that's quite analogous to the
*  problem that a neuroscientist has. You're watching an animal do something you know navigate or make
*  decisions in an intelligent way or you're watching another person do something intelligent and
*  you know there's something interesting going on in their brains that's giving rise to that behavior
*  but it's a research project to figure out what that is and we end up with the same problem in
*  AI work. So we have a group within my team at DeepMind whose full-time job it is to try to do
*  neuroscience on these AI systems and figure out exactly how it is that they're doing what they're
*  doing. Very good. Let's get into a little bit of the philosophy of the DeepMind approach. So there's
*  this really nice review in Neuron from last year and in the review you lay out why neuroscience is
*  important for AI and vice versa in the quest to understand intelligence like you just said and
*  build general AI. So I often wonder whether we're selling ourselves short using human intelligence
*  and neuroscience as a guide to develop general AI but there's this a well-stated argument for
*  studying the brain in the paper and it goes as follows. The space of possible solutions to
*  general AI is just super vast and in all likelihood really sparsely populated. So there are very few
*  solutions in this large space and humans are the only example that we have for general AI
*  and therefore human cognition is the smartest way to proceed and then once you recognize that you
*  have to then further say that animal cognition is important in that it provides this window into
*  higher level cognition. So I just think that's a pretty solid argument for using human AI even
*  though it could be that we are selling ourselves short. What do you mean by selling ourselves
*  short? Well what if one of the other three solutions in this vast space are simpler,
*  better, outstrip our abilities immensely, things like that but how would we know? How would we get
*  there? I think you've stated the case very nicely. I mean for me it's much easier to motivate this
*  decision to attend to neuroscience if you state things in the negative rather than saying we need
*  to attend to neuroscience in order to solve AGI instead say wouldn't it be crazy not to pay any
*  attention to neuroscience? Yeah sure. So you know I think there really is a good analogy
*  in the history of aviation and this is actually a little bit of a complicated story to tell because
*  people often use this exact example to make the opposite case. I've heard people say oh well you
*  know paying attention to neuroscience may be a bad idea. Look at aviation. People didn't succeed in
*  building the airplane until they deliberately ignored birds because birds were distracting them
*  somehow and you know obviously they weren't trying to build. The task was not to build a bird,
*  it was to build something out of wood and other kinds of material not feathers and without
*  flapping and so the bird thing was a big distraction and it slowed everything down. In fact
*  if you look at the history that's categorically false. That's fake news. I'm here to tell you.
*  So the history of aviation actually played out quite differently and if you look at what helped
*  the Wright brothers finally succeed even in the final stages of designing their aircraft they were
*  thinking very concretely and immediately and in a detailed way about birds. They had a problem with
*  what they called lateral control getting the airplane to kind of stay going forward or to
*  you know to turn where they wanted it to turn and they were reading books on how birds handle this
*  problem and birds do an interesting thing by twisting their wings in a particular way and
*  the Wright brothers used exactly that solution in their first aircraft. So you know my attitude is
*  if you're someone who's trying to build the first airplane and outside your window there
*  are birds flying around it just seems kind of crazy and perverse not to pay any attention to that.
*  You know if nothing else it's an existence proof right? You probably wouldn't even be
*  trying to build an airplane if you haven't seen the birds in the first place and actually neuroscience
*  still plays an existence proof role in a lot of in a lot of ways. There are things that our AI
*  systems can't do that we probably wouldn't even be aspiring to if we didn't have human cognition
*  in mind. Certain kinds of rich inference and flexibility but even at a more detailed level I
*  think it's just patently foolhardy to ignore neuroscience and psychology as a source of
*  information. It would be equally foolish to be over literal to ignore the fact that we're not
*  trying to build a brain here. You know there are lots of things about the brain that are probably
*  totally irrelevant. For example the brain has to be you know it can't be larger than a size that
*  allows it to go down the birth canal right? I mean it has to be small enough to do that. We don't
*  really have to worry about that in AI so there are plenty of things about the brain that are we
*  know from the outset are going to be irrelevant but yeah I think the aviation story is pretty
*  compelling. That's what keeps me looking at neuroscience. Geez Matt I didn't mean to get
*  you all defensive. I'm not trying to replace your team at your neuroscience team. This is a surprisingly
*  contentious issue though. I don't know that it's contentious within DeepMind. One thing that I've
*  been delighted to find at DeepMind is that there's a very widespread interest in neuroscience but I
*  have been involved in debates in the larger AI community. There are definitely people you know
*  leaders in the AI community whose attitude it is that maybe neuroscience was useful at some point
*  in the past but AI has matured to a point where we no longer really need that scaffolding. So
*  this is apparently a topic on which reasonable people can disagree but that's not where we're
*  putting our money. I mean and it should be stated again that DeepMind's goal is not to make a brain,
*  not to understand the brain. It's to build intelligence, build general intelligence and
*  and in that service it employs neuroscience as a guide. So really the focus is on sort of the
*  computational processes. If you want to talk about David Marr's three levels. So the top two levels
*  are the computational level which are like the goals of an agent or individual and the processes
*  and computations to realize those goals which is like the algorithmic level, the second highest
*  level in David Marr's. And without regard really to the mechanisms underlying the physical processes
*  which is the implementation in Marr's level. So that's really how DeepMind seeks to
*  build intelligence is by focusing on these top two levels and not necessarily the mechanism. So you
*  don't need to understand the mechanisms all the way down to the neuron essentially. Yeah that's
*  right. There's one way in which thinking about that lowest level, the implementation might be
*  interesting even from an AI perspective down the line. I think as we argued in that neuron paper,
*  I think given where we are at the moment the computational and algorithmic levels are clearly
*  the most important for us to be looking at. But the implementational level is interesting given the
*  small the very small amount of energy the brain needs in order to do what it does. Yeah that's a
*  big problem. Yeah if you compare that, I mean I'm not an engineer and so I can't give you numbers,
*  but coarsely speaking the amount of raw energy that it takes for us to run large AI jobs now is
*  simply you know it's astronomical compared to the energy that the brain seems to get by with doing
*  comparable things. So maybe at some point once we figured out those top two levels it will be of
*  interest to understand how the brain is able to do what it does with such you know you know sipping
*  through such a narrow straw on the energy supply. But having said that, yes the computational and
*  algorithmic levels clearly are critical. Sometimes it's hard to distinguish between these
*  levels than we would like. So for example there are things like oscillations. There's all sorts
*  of fascinating information coming out of neuroscience research these days about structure
*  that you find at the level of oscillations in brain activity. Whether that's at the level of
*  the action potentials, the neural firing patterns, or at the level of voltages, the membrane
*  potentials, the variables that sort of underlie those spiking activity. And you know it's hard
*  to say at this point in history whether those oscillations are a detail that we should kind
*  of put on the implementation side. It's just a low level detail. We can kind of ignore that
*  when we take lessons away from neuroscience. Or maybe it's something fundamental. Maybe there's
*  information being processed at the level of those oscillations that there's computational work being
*  done by those oscillations that we should be you know it would help us to build these kinds of
*  oscillations into our AI systems. So we often face this uncertainty when we look at the neuroscience
*  literature about which side of that line the thing we're reading about falls on. You're attempting me
*  to go down the consciousness road here because that's what everyone wants to talk about. No,
*  I hope I didn't tempt you that. No, I'm not going to. Don't worry about it. Don't worry.
*  Maybe later after a few drinks. Sure, sure. Okay, before we really get into this recent work,
*  this awesome recent work that you and your team have done, tell me, I'm going to go through this
*  historical progress in my mind and thinking like a hundred years from now, this bird's eye view
*  of the history of the AI neuroscience development here. Yeah. I'm going to talk about a few stages
*  and then I want to just get your take on it and then we'll move on. Let's start with a pre-modern
*  stage and that's the symbolic good old-fashioned AI where you know logical AI where humans are
*  symbol manipulators. So this is the early AI, pre-statistical deep learning models, right?
*  Yeah. Then I'll say there's this first stage and these are the perceptron days and PDP,
*  parallel distributed processing days, that are loosely based on what was known about neurons
*  at the time and even there was a lot more known at the time but just really abstracting very
*  few qualities to implement these things. Then the second stage, these core ideas that were just
*  innovated, the perceptron, et cetera, were really made to work. So there's this confluence of big
*  data that we have and computational power and the ability to implement these things.
*  This is when like added layers were added and convolutional neural networks and recurrent neural
*  networks including adding some technical tricks, some inspired by brain science, most not I would
*  say and then of course the reinforcement learning driven conquest of the gaming world that DeepMind
*  does. Okay, so now I'm going to say now we're at this third stage and now we have these statistically
*  awesome models. We've gone completely away from good old-fashioned AI with a symbol based AI.
*  AI wins all the games that we train it on, it blows us out of the water, the general public is
*  being taught to fear AI because it's going to take over the world and will be its pets.
*  But there's a lot of backlash now from people like Melanie Mitchell whom I'll speak with in a week or
*  two, like Josh Tenenbaum, Brendan Lake, who are saying, hey, this smart AI is really pretty dumb,
*  it's pretty narrow and really far away from general AI which is what people think of when
*  you just say AI and it's time to learn about and add in some of what we know about how humans really
*  learn. So what do you think about that? 100 years from now looking back on it, what would you change
*  about that story? Well, I'm a great admirer of Brendan and Josh and I talk to them about this
*  kind of stuff all the time and it's funny because you know reading the literature you might think
*  that there are these very clashing perspectives but actually when we get together to talk about
*  it I honestly think we're much more on the same page than it might appear. In other words,
*  I think in the end these are all pieces of the puzzle and we just have to put the whole puzzle
*  together. Good old-fashioned AI was focused on questions that are still entirely fundamental
*  today. How does reasoning play out? What's the format of representations that you need in order
*  to reason? What's the format of representations you need in order to plan, to construct new
*  knowledge out of old knowledge, to make inferences that bring to bear the right sort of default
*  assumptions? The problem with good old-fashioned AI was that there wasn't enough of a mechanism
*  involved for learning these kinds of representations, especially learning them in a
*  perceptually grounded way through actual interaction with the physical world. So
*  it was necessary for AI researchers to do what came to be called knowledge engineering, where you
*  had to simply effectively write down in your computer code everything that a human would know
*  about the world. Like a hamburger has half a bun on the bottom and half a bun on the top.
*  Every little thing that a human knows about the world, which is obviously an impossible task.
*  There's no way to do that. But that doesn't mean that the objectives of good old-fashioned AI were
*  misguided. We're wrestling with exactly those challenges today. We have a way of developing
*  grounded knowledge. Deep learning and deep reinforcement learning is wonderful for
*  making sense of sensory information and interacting in a kind of grounded agent-based way with the
*  physical environment. But now we need to figure out a way of growing that knowledge to the point
*  where it makes contact with the sorts of structure that good old-fashioned AI was interested in. We
*  want abstractions. We want a language of thought. We want systems that can reason and draw conclusions
*  from their past experiences. And we also, you know, it's very true. We want systems that learn
*  rapidly because they leverage their existing knowledge. We want systems that don't need to
*  play chess for, you know, thousands and thousands of games before they start playing reasonably.
*  We want a system that is more like a human where, you know, if you've never played chess before,
*  I can sit you down and explain the rules. You won't be a grand master after an hour,
*  but you'll be playing. And, you know, by the way, none of this is to take away from the
*  profound impact that these existing deep RL systems have, like AlphaGo. I mean, I wouldn't
*  be a deep mind if it weren't for the Atari work that was going on and AlphaGo. I mean,
*  these are mind-blowing breakthroughs to my mind. But it is true. The next thing that we have to take
*  on as we go down this path toward true AGI is we have to combine that kind of deep sophisticated
*  knowledge gained through huge amounts of experience. We have to build systems that have that, but that
*  are also flexible and that are cognitively nimble. They can make sense of a new situation very
*  rapidly based on a few observations. So, you know, these are things that cognitive scientists
*  have been focused on for years, including me and some of my research. And so we need to get
*  them into the picture. But building systems that have only that kind of nimbleness misses the other
*  side of the equation because the only techniques that we really have for building artificial
*  systems that appear to have that kind of flexibility is to retreat to this situation where we're
*  building a lot of the knowledge in by hand. So the bottom line is, I think, you know, to answer your
*  question 100 years from now, I think the narrative is going to go, look, you know, there were these
*  different research communities focused on different, you know, pieces of the elephant,
*  you know, the old parable and the success story that we hope is going to unfold over these 100
*  years or maybe the next 20 years is going to really involve putting these pieces together
*  in a way that allows us to avoid the kind of dead ends that each of these approaches
*  that have been explored so far have run into. That's a really a hell of a segue to talk about
*  some of your recent work here. Okay. So where you're building in these abilities to learn how
*  to learn. So, okay, so the paper that we're about to talk about is called Prefrontal Cortex as a
*  meta reinforcement learning system. And as we've talked about these deep reinforcement learning
*  systems have come to dominate game playing Atari chess go. It was just announced that you guys can
*  predict protein folding structures, which is, you know, a huge finding. And as you said, one of the
*  many challenges in AI in deep learning and deep reinforcement learning is that learning is slow
*  and takes a million examples of labeled data to get anywhere. The solution is to learn how to learn
*  the capacity for meta learning. You have previously recently worked out a way to do this in AI using
*  reinforcement learning by positing a first reinforcement learning system that trains a
*  second reinforcement learning system. And then the second system can act independently and adapt
*  and learn faster. So that is in a previous paper on AI. And in this current paper, you use that AI
*  inspiration to explore how it might occur in the brain. Yeah, I guess we've described meta learning,
*  which is learning how to learn and the ability to learn various tasks and improve faster with
*  each new task that you learn. So maybe now we can just describe reinforcement learning in general
*  before we dive into the brain. So how does reinforcement learning broadly work at the
*  sort of algorithmic level? Sure. So reinforcement learning, depending on who you ask, really is not
*  about a solution. It's about a particular kind of problem, which is I am in a learning situation
*  and the feedback that I'm getting is formatted strictly as rewards and punishments or positive
*  rewards and negative rewards. So this is in contrast to what would be called supervised learning,
*  where I give you a problem, you give me your answer, and then if you're wrong, I tell you
*  exactly what you should have said. So that's the setup, for example, in a lot of image
*  classification tasks. I show the system a picture of a kitten. It says, car. I said, no, not car,
*  kitten. That's a supervised learning situation. With the finger up. He had to hold the finger up.
*  No, no. Exactly. So in a reinforcement learning setting, instead, you would show a picture of
*  a kitten. The image classification system would say car, and you would say, no, you're cold. That's
*  bad. Bad answer. And if it said kitten, you'd say, great, great job. And so you can see the
*  difference there. The information that's available in that form of feedback signal is much thinner
*  because you're not being told exactly what you're supposed to do. And so the reinforcement learning
*  problems are fundamentally different from supervised learning problems in the sense that
*  you have to experiment. You have to try things out. You have to explore the space of possible
*  responses in order to discover what gets you the most reward. So in the name of the game is to find
*  a way of responding to the situations you're being presented with that maximizes your reward.
*  So that's the problem setup. There are a variety of ways of then tackling that in terms of learning
*  algorithms. One way is to build a model of the world to try to understand how things work.
*  So then you can then leverage that knowledge in order to maximize reward. So this is we refer to
*  this as model based reinforcement learning. So if you're learning how to use a new cell phone,
*  probably there's a component of model based reinforcement learning. You're trying to
*  understand the if then rules of this phone. If I press this icon, then that thing happens. If I
*  press this button on the outside, the volume changes. And then once you have that knowledge,
*  you can make decisions that that fit with your goals and maximize reward. But then there's another
*  in a way simpler approach that you can take to a reinforcement learning problem, which is
*  called model free learning. And this is actually an approach that was originally inspired by animal
*  conditioning research. So this is a good example of where psychology really inspired fundamental
*  work in AI. The idea here is a little bit it's reminiscent of what you would do to train say,
*  your dog to do a trick. You wait until your dog does something that looks a little bit like the
*  trick you want that you want her to do. And then you give her a treat. And then you wait until she
*  does that again. And maybe it looks randomly a little bit more like what you want her to do
*  and you give her another treat. This is in animal in animal training. This is called shaping. And
*  it's reminiscent of what we do with our AI agents. We they explore a problem and they just wait and
*  see where they get a reward. And when they get a reward, they compute a quantity that's called the
*  reward prediction error. They're always trying to predict how well things are going to go for them
*  in the future. And when they get a reward, if they weren't predicting it, they produce this
*  signal called an RP or reward prediction error. And that's what drives learning. So every time
*  I'm positively surprised, I try something and I and I'm surprised, oh, I got a treat for that.
*  Then I change my own behavior so that I'm more likely to do that thing in the future. Now,
*  let's say I try something and I expect to get a treat, I expect to get some reward, but I don't
*  get some reward. That means I was wrong. I have a negative reward prediction error. I'm disappointed.
*  In that setting, I change my behavior so I'm less likely to do whatever it is that I did that led to
*  that outcome. And in this way, my behavior is gradually pointed more and more toward
*  patterns that yield reward. So this is actually the method that was used to tackle Atari games
*  at DeepMind. AlphaGo and AlphaChess and AlphaZero use a combination of these two strategies
*  where there are positive and negative reward prediction errors. Gee, I won that game. That's
*  a positive surprise. Maybe I should update my way of playing Go to make it more likely that I'll do
*  that sort of thing in the future. AlphaGo has another component which is model-based though,
*  where it has an internal model of how the pieces move around the board and it thinks through the
*  moves that it could take and tries to use that to improve its estimate of what's a good move and
*  what's a bad move. So that's an overview of the different ways that we tackle these reinforcement
*  learning problems. Wow, that's really well described. Thank you. So reinforcement learning
*  is an example of something that was brought into neuroscience to explain how learning might work
*  in the brain. Yes. So what is the standard model of reward-driven learning in the brain
*  in terms of the dopamine story? That is the sort of well-known story.
*  Yeah, this is a beautiful historical example of a case where understanding natural intelligence
*  inspired AI by giving rise to the reinforcement learning paradigm. And then after that field of
*  AI research matured, it sort of returned the favor to studies of biological intelligence.
*  It was in the 90s that a group of researchers including Reid Montague and Wilfrum Schultz and
*  Peter Diane made the realization that this reward prediction error that is at the center of these
*  model-free reinforcement learning algorithms shows behavior that is very directly mirrored
*  by what you see if you record from dopamine neurons. So as I understand the history, they were
*  reading about new data from Wilfrum Schultz's lab, Wilfrum records from dopamine neurons in monkeys
*  and other animals. And there was this aha moment where they said that looks exactly like a reward
*  prediction error. No way. Those aha moments don't happen. Yeah, that's what you live for as the
*  scientist. Yeah, so that connection, it turns out, appears to be at least coarsely quite valid
*  when monkeys and other animals and including humans, when we're surprised by a reward outcome,
*  when we get reward we weren't expecting, that's when dopamine gets excited. When we're disappointed,
*  we were expecting some reward and it fails to materialize, we get a dip in dopamine release.
*  There are many, many details of dopaminergic functioning that fit with this account.
*  The standard story, so to speak, has become this temporal difference reward prediction error
*  account of dopamine where if there's a positive reward surprise, there's an unexpected reward,
*  dopamine release increases and this serves to drive learning. So I said before
*  in the AI setting that if you have a positive reward prediction error, you should make yourself
*  more likely to do whatever it is you just did again in the future because it turned out better
*  than you thought. And that's exactly the mechanism that lies at the heart of the neuroscience theory.
*  The idea is that dopamine is released into parts of the brain that are responsible for shaping
*  behavioral policies, stimulus response associations, including parts of the striatum,
*  a nucleus deep in the brain. And when there's a positive reward prediction error, the strength
*  of the connection between the perceptual input that you had and the action that you produced
*  is increased. So you're, you know, in that sense, more likely to do that thing again in the future.
*  And then obviously you can flip the sign on that for negative reward prediction errors
*  and you get a weakening of those associations. So the story in neuroscience is remarkably parallel
*  in all of those ways to the AI story. The way that we train AI systems these days really does
*  parallel quite immediately what we believe is going on in the brain driven by dopamine.
*  Okay. So dopamine is a reinforcement learning system. And I said at the outset that you guys
*  used a reinforcement learning system to train another reinforcement learning system in your
*  earlier work. Now, the prefrontal cortex is known to also represent a lot of representations
*  that underlie reinforcement learning as well. And I guess the new thing that you guys have posited
*  and explored here is that prefrontal cortex is its own self-contained reinforcement learning
*  system. And, and you can explain this a little bit further, that the dopamine system serves
*  to train the prefrontal cortex reinforcement learning system. And in that way is meta learning
*  and allows us to speed up our learning and generalize to other tasks. Yeah. So two things,
*  one, so how do these systems work together as a meta reinforcement learning system?
*  First of all, so I think the way to come at it that makes it easiest to understand is to
*  start by talking about different kinds of memory. When you're thinking about how memory plays out
*  in the brain, there are at least two different mechanisms by which some piece of information
*  could be stored in memory. You could change the synapses, right? You could change the connection
*  strengths between neurons. This is a way we know for sure that that long-term memory is encoded. So
*  you know, if, you know, if we, if we remember this interview a month from now, it'll clearly be the
*  case that there were some that we remember it because there were some synapses that were
*  changed in our brains. And the strength of the synapses is what is what stores the information
*  stores the memory of this, of this event. There's another way that you can store information and
*  memory in the brain though, which is simply at the level of neural activity. So if I, if I have to
*  remember a telephone number for a few seconds, I guess nobody really has to do that anymore,
*  but this, this, this is the old fashioned example that we always use. You're showing your age. Yeah,
*  exactly. Exactly. So, you know, I need to remember some short list of something just for a few
*  minutes for a few seconds. My brain doesn't need to change the connection weights to do that.
*  I just need to hold, so to speak, hold it actively in memory. So let's say, let's say there are some
*  neurons in my brain that when they fire, when they're active, they're representing the number
*  two. And there's another group of neurons that when they're active, they're representing the number
*  three and so forth. So I can, I can hold a telephone number in mind without changing any
*  of my synaptic weights, without changing the connections between neurons, just by keeping
*  those neurons active for a while. We think that that's a mechanism involved in working memory.
*  That's the term we use in cognitive psychology. Working memory is just the kind of memory that
*  you use to maintain information over short periods to actively maintain some piece of information
*  that you know you're going to need shortly. So there's this distinction between weight-based
*  or synapse-based memory and activation-based memory. So how does activation-based memory work?
*  Well, in order for those neurons to stay active, one mechanism by which that can happen is a
*  feedback loop. So in other words, one of these neurons becomes active. How does it stay active?
*  I can keep feeding input to that neuron by reading that telephone number over and over again from a
*  page, but that's not really holding it in memory. A good way to hold it in memory would be to have
*  a feedback loop where I activate those neurons and then I have a connection from those neurons that
*  eventually forms a loop back to themselves so that when they fire, they keep themselves firing,
*  they excite themselves. It's a positive feedback loop. And we know that these kind of feedback
*  loops exist all over in the brain and we think that that's a mechanism by which the brain holds
*  information active over short periods. That's a mechanism for working memory. And the prefrontal
*  cortex is a critical place for this to happen. So you can think of the prefrontal cortex at a
*  very high level of abstraction as a big feedback loop, a big circuit that once you make certain
*  neurons in that circuit active, they will tend to stay active and maintain information over time.
*  So now imagine using that kind of system to learn. Let's say I'm in a casino
*  and I'm trying to decide which of these slot machines is most likely to pay off. A good way
*  of solving that problem, assuming there aren't too many slot machines that I'm considering,
*  is to try them out. I try this one over here for a while, I try that one over there for a while,
*  and I see where I win more often. And eventually with enough data, I decide, oh, it's that one
*  over there that's paying off more often. In machine learning, this is called a bandit problem
*  based on that exact analogy. So notice that in order to do that kind of learning, I have to
*  hold in memory the information that I've gathered so far. I have to maintain some sort of record
*  of which machine I tried and whether I won on that machine. And I need to continually update that
*  record of my past experiences in order to be able to decide what to do now. This is just a definition
*  of learning, really. So in the standard dopamine story, that learning is happening at the level
*  of synaptic connections. I play a machine, I win, I change my synaptic weights. I play a machine,
*  I lose, I change my synaptic weights. But it's equally plausible that our brains handle this
*  kind of learning situation in that other way, using activities. So I have a certain bunch of
*  neurons in my prefrontal cortex that when they're active, it means I played that machine and I won.
*  And another set of neurons that when they're active, they mean I played that machine and I
*  lost. And so I can maintain a record of what's happened so far by just activating certain neurons
*  in my prefrontal cortex. And together, they encode information about what I've tried and how well it
*  went. And I can use that information to choose my next action. But in that case, doesn't the
*  correct doesn't the right signal need to be input into that network for those for that activation
*  to take place to know, oh, this is the third from the left? Absolutely. Okay, absolutely. Right. So
*  just the way that in order to hold on to a telephone number in your working memory,
*  at some point, your ears have to receive the telephone number. There has to be some sensory
*  input that gives you the information you want to hold in memory. It's exactly the same in
*  reinforcement learning. This memory system has to have access to the relevant the relevant pieces
*  of information, it has to have perceptual information that says, I played that slot machine.
*  That's information about actions as well. And it has to have information about eventual rewards.
*  So the prefrontal cortex has to be getting information about perceptual inputs, action
*  outputs and rewards. Fortunately, we know it, it receives all that right information, right? Yeah,
*  the necessary ingredients, right? Exactly. prefrontal cortex listens to essentially everything
*  that's going on in the rest of the brain. So it's in a perfect position to integrate that kind of
*  information. So now that now to kind of put these pieces together, I said before that working memory
*  depends on this kind of feedback loop, where neurons excite themselves so they can stay active
*  once they're once they become active. This learning situation requires something more, which is that
*  the circuit has to also update itself every time it gets a new piece of information. So it's not
*  just a question of holding something statically in memory. It's also a question of taking what
*  you already know about those slot machines, adding in the new thing that you just observed,
*  and updating your overall and your overall representation of which slot machine is better
*  and doing that every time you play a new slot machine. So that kind of update requires an
*  appropriate kind of feedback loop, right? In other words, the way that new information gets
*  integrated with existing information can't be random, it has to follow the rules of the game,
*  it has to represent the right quantities. And so in order for the system to work, that feedback
*  loop has to be parameterized correctly. The synaptic weights in that feedback loop have to
*  be correct. And so you end up with the question, well, wait, how do those connection weights get
*  learned? How do those synapses get set so that this feedback loop, this working memory mechanism,
*  does the right things in a learning situation? And that's where we come back to the dopamine story.
*  So the overall idea in this meta-reinforcement learning paradigm is that the role of dopamine
*  is to set the strengths of the connection weights in this big recurrent neural network that runs
*  through your prefrontal cortex. And the purpose of adjusting those weights is to set up the right
*  kinds of feedback loops, the right kind of activity dynamics, the right kinds of update rules in that
*  activation based memory that really in the end is doing all the work. It's like when you're playing,
*  when you're trying to figure out which of those slot machines is the right one to play, that's
*  really all happening at the level of neural activity, at the level of this working memory
*  based activity based memory system. But the reason that that system works in the first place
*  is because dopamine based learning has very slowly and gradually sculpted it, changed those
*  connection weights so that everything operates the way that it should. Does that make sense?
*  Yeah, it does. I mean, so the thing that I, so it does make sense. The thing that I struggle to
*  understand and I didn't, I could have read your previous paper in more detail, I think, is how
*  the reinforcement learning works within the prefrontal cortex in this case, within the
*  activation dynamics, right? So you input a signal and to my mind, if all of the weights are fixed
*  as you do in the network, you train the prefrontal cortex with dopamine and then you fix the weights
*  and then you start asking it questions, then you test it. And you see that the reinforcement
*  learning is working within the activation dynamics. And I'm struggling to understand how
*  that is working without changing weights. Does that make sense?
*  Yeah, well, it's working without changing weights because the weights are already set to do what
*  they need to do. So in other words, imagine you're in a very simple bandit problem. So you're just
*  trying to figure out whether to pull the left arm or pull the right arm on a two arm bandit,
*  a slot machine. Imagine a slot machine with two arms. So now what are the activities of those
*  neurons have to represent? They have to represent at any given point how confident you are that the
*  left arm is the good arm or that the right arm is the good arm. So you could get by with a very
*  small neural network that had maybe only two units in it, maybe even only one unit, right? The point
*  is that you just have to say where you are on that confidence scale. So what do the connection
*  weights have to do? Well, they have to assure that when you, let's say I play the left arm and I get
*  rewarded, the system then has to update its confidence representation, right? It has to say,
*  oh, now I think I'm a little bit more sure the left arm is the good arm because I just played that arm
*  and I won. So all the recurrent weights have to do is make sure that
*  the activities of those units shift in the right direction and stay put. You can think of it,
*  I mean, another way of coming at this is to imagine, just to think about what recurrent
*  dynamics of a neural network are, right? So any recurrent neural network, any network that has
*  feedback connections will have dynamics. Its activity patterns will tend to evolve in a certain
*  way because the activities go through those connection weights and influence the next pattern
*  of activity, which influences the next pattern of activity. The dynamics can be stable. So if the
*  weights are exactly right, certain patterns of activity will stay put. They will just stay as
*  they are. But the dynamics are also defined in terms of what happens when you perturb the system,
*  right? So it's not just a question of how the activity dynamics evolve endogenously without any
*  external input. The dynamics are also defined in terms of what happens if you poke the system
*  from the outside? What happens if you apply a particular kind of excitatory input or a
*  particular kind of inhibitory input? So now, and the dynamics, the way that the dynamics of the
*  system responds to external perturbations is also governed by those recurrent connection weights.
*  This is becoming very clear to me now. Yeah, okay, go ahead.
*  Yeah. And so you can think about learning as playing out in that kind of setting. It's not
*  just kind of the intrinsic dynamics of the system. It's also about the way that the system responds
*  to external inputs. And the external inputs here are observations literally like, I played the left
*  arm and I won. I played the right arm and I lost. And so the dynamics of the system in those settings,
*  the activities in the system should update in just the right way in order to change the
*  representation of the confidence. Is it the right arm? Is it the left arm? In a way that's rational
*  and proper given the recent observations. So the trick is to get the connection weights
*  exactly right so that these external inputs change the state of the network in just the right way.
*  And that's the role of the dopamine driven learning.
*  It's all clear to me now and hopefully it's clear to the listeners as well.
*  So I hope so. That really scratched my itch.
*  It's one of these things where, you know, what I find is that it's something that sounds very
*  complicated and abstruse until you get the insight. And then it seems very obvious and simple.
*  Right. You know, the other obvious and simple thing to me is that these one-armed bandit problems,
*  I mean, in reality, I take my grandmother to the casino and just watch her put the money in
*  over and over and nothing really comes out. So yeah, in the real world, you can't win a bandit
*  problem. No, I like your casino better than mine. Yeah, exactly. So cool. Okay. So kind of in summary
*  of this work, you have this dopaminergic system that is its own reinforcement learning system.
*  It's training a prefrontal cortex reinforcement learning system that operates under activation
*  dynamics under a different regime. Right. And you guys have tested this on multiple different
*  tasks like the one-armed bandit problems with a bunch of different probabilities.
*  You've seen that the learning takes place faster just as you would hope it would in these
*  reinforcement learning systems that are training each other. So I know that there are more things
*  to work on and that there are some drawbacks, some shortcomings of the research. We're not
*  going to get into them in the interest of time because I know time is limited, but you know,
*  what could this metal reinforcement system be used for moving forward? Well, one of the things
*  that you have used it for is training theory of mind into machines. So we won't go too in-depth
*  in this paper in the interest of time, but you have this really recent paper called Machine
*  Theory of Mind where you use meta-learning to build a theory of mind network and you call it
*  TomNet as in theory of mind net. What is theory of mind and how much do we neuroscientifically
*  know about it? And maybe I'll just leave it to you just to kind of describe what you guys did in this
*  paper and why it's important. So I won't badger you with detailed questions here.
*  Sure. I should mention my collaborators on this work. So in the meta-RL work, I just want to give
*  a shout out to Jane Wong and Zeb Kurth Nelson who really led the way on the computational work there.
*  In the TomNet stuff, I worked with Neil Rabinowitz, Francis Song and other collaborators. So
*  theory of mind is a term that comes out of psychology. It's widely used in developmental
*  psychology and it refers simply to the idea that we understand when we interact with other people
*  that there's something going on inside those people's heads that isn't directly observable,
*  but which explains their behavior and it involves especially beliefs and desires. So we make
*  inferences about what other people know or believe from the things that they do and we make inferences
*  about what they want, what outcomes they're trying to bring about, what they like
*  again from their behavior. So this kind of internal model that we have of other people and their
*  psychological activities is referred to in psychology as theory of mind. So what do we
*  know about theory of mind from a neuroscience point of view? I would say honestly very little.
*  We've learned a lot about theory of mind from psychology. A lot of the information that we've
*  gained through psychology research is about the course of cognitive development. At what age do
*  children acquire particular concepts about the minds of others? What is the developmental
*  trajectory? When it comes to neuroscience, I should just mention that this isn't a particular
*  area of expertise for me on the neuroscience side. So there may be recent pieces of work that will
*  contradict what I'm about to say, but my impression so far is that we have a maybe very broad notion
*  of what large-scale brain areas might be involved in the computations that underlie these kinds of
*  inferences. But understanding things at a finer neuro-computational level of granularity is
*  definitely not something that we've attained yet in neuroscience. So the mechanisms that underlie
*  theory of mind are very much open questions both in neuroscience and in AI work.
*  There's a lot of very interesting and powerful cognitive modeling that's been done in order to
*  formalize. We were talking earlier about the algorithmic level, the computational algorithmic
*  level. There are cognitive models that capture the way that these inferences play out, but we
*  don't know much about the neuroscience. So one of the points you make in the paper is
*  kind of a problem, a recurring issue that comes up when people discuss these things is that we
*  don't understand these AI systems. We don't understand how they're working. So it's important
*  for an AI system to be able to tell us essentially how it's working. And that's one reason why you
*  went about trying to build theory of mind into the machines. And you make the point that as humans,
*  we don't understand each other at the level of single neuron activity. We have these abstract
*  mental models of each other. And so the way you built in theory of mind into these machines is
*  not to understand every individual unit and what that means, but to build an abstract model of
*  another machine. And so I think that's a really interesting way to go forward. So maybe you can
*  just take it from there and talk about what you did. Yeah, I think our motivation in this work was
*  multifaceted. You're absolutely right that one of the things that we had on our minds was,
*  how are we going to understand these AI systems that we're building? And we had the kind of
*  cheeky idea that maybe we could use AI to understand AI. Just as we understand one another
*  at the level of these abstractions, beliefs, desires, and so forth, maybe we can discover
*  the right abstractions that would allow us to understand the behavior of the AI systems that
*  we're building without having to understand what every little unit in these deep neural networks
*  is doing. And by the way, maybe we can also constrain the representations that arise in these
*  understanding systems so that they align with what humans are naturally positioned to understand.
*  Well, that's not to say that we couldn't use every single unit in an AI system because
*  it's called the black box problem. But then often people, I don't remember who coined the
*  term, it might be Dan Yeamans, but it was really a white box problem because we do have access to
*  all the units. It's just that that might not be a useful way of going about doing it.
*  Exactly. I mean, I think there's a perception among neuroscientists that part of the problem is that
*  they don't have enough data about what's going on in the brain. This was maybe up until 10 years ago
*  before these amazing new neuroscience techniques hit the bench. People had to make inferences about
*  what was going on in entire brains looking at like eight neurons at a time. And there was a kind of
*  envy, I guess, toward people studying AI systems because gee, you folks get access to every little
*  bit of what's going on under the hood. Right. It's a curse. A blessing and a curse.
*  Exactly. And neuroscience now is in an analogous position because it is possible now to record
*  from thousands, hundreds or thousands of neurons depending on the technique you're using at once.
*  But even when you have access to that kind of large scale data set, it's very hard to figure out
*  what's actually going on and figuring out the low dimensional structure that actually underlies
*  what's happening in these high dimensional systems is a really challenging problem,
*  both for neuroscience and AI. So the idea in the work that we did was to say, look, rather than
*  trying to figure all of this out as human researchers, let's build a learning system
*  that will discover the proper level of abstraction for itself. And so the basic idea was let's take a
*  model that observes another behaving system and just tries to predict what that other
*  system, that other agent is going to do next. And the only twist on that is that instead of just
*  allowing our theory of mind network to observe what this target agent is doing right now,
*  we also give it several examples of what the same observed agent has done recently in the past.
*  To give you the intuition, if I'm shown several YouTube videos that show me the last several
*  restaurants that you went to and what you ate there, I can make some inferences about that,
*  about what you're likely to do at the next restaurant you go to. If you keep going to
*  cheesesteak restaurants, then the probability becomes much higher that you're going to go to
*  another cheesesteak restaurant. He says from Philadelphia.
*  Exactly. Exactly. I've got two steaks on the line here. So that's exactly the strategy that we used
*  in this theory of mind work was let's just build a system that learns to take observations from past
*  experience, from past behavior, I should say, and to make predictions about what should be observed
*  in new behavior. And to train the system across, importantly, to train the system across a diverse
*  set of observed agents. So maybe if I watch some videos of what you did at the last several
*  restaurants you went to, I can also watch videos of what somebody else did in their last few
*  restaurant visits, and I can watch videos for say, 100 other people. And if I can do that,
*  then I can not only make predictions about individuals, but I can develop a sense of
*  what the different categories or dimensions are that underlie behavior. Maybe there are some
*  people that like fast food. If I see you go to Burger King over and over again, then I might
*  predict that you're more likely to go to McDonald's than that you're likely to go to some fancy French
*  restaurant. Right? Because I understand some people just like fast food. And I can learn what we call
*  a low dimensional manifold that describes the range of behavior that we see across a population.
*  And this is something that, you know, there are low dimensional manifolds that describe human
*  behavior. Decades of research into the structure of human personalities has led to these dimensional
*  models where there are debates about exactly how many dimensions there are to human personality,
*  but there aren't that many. There's somewhere on the order of five dimensions that really do capture
*  a lot about what makes a particular person, what gives them the personality that they have.
*  So the idea in this machine learning or AI project was to build a learning system that can identify
*  that kind of low dimensional structure and figure out, oh, I see there are different kinds of people
*  and here are the particular kinds of ways in which people differ. And armed with that kind of
*  knowledge, then I can observe the behavior of a new person and very quickly make inferences about
*  what else that person's likely to do. Does that make sense?
*  Yeah. Yeah. That's good. So you guys implemented this and I'll point people to the paper. It's
*  really fun. You say cheeky, I say fun, work that you guys are doing. So Matt, we're really up
*  against time here. I want to ask you, I usually ask a few broad general questions to each guest.
*  So I'll just ask you a few here then, and then I will let you go. You're only three hours away from
*  french fries on a sandwich. So I'm sure after this, you got to get there. So that's exactly right.
*  So what is something that's a little out there that someone else might find hard to swallow
*  that you believe will come out, you know, maybe after you've had a couple of drinks,
*  catch you off guard, you might say that, oh, I think this is going to come out of the interface
*  of neuroscience in AI. Well, I'm a believer that it won't take any special kind of magic for
*  AI systems to develop a representation of self. Oh, man. Actually, some of the first work I did as
*  a graduate student in Pittsburgh was about self representation. There's a thing that's
*  come to be known as the rubber hand illusion, which is something that I dreamt up when I was
*  a graduate student, which is about, it's an illusion that sort of reveals something about
*  why we think our bodies belong to us, why my body is me, as opposed to other things in the
*  environment, which aren't me. What I took away from that research was that there's really nothing
*  magical about that. It's just that there are certain patterns of correlation in our perception.
*  So, you know, my hand is me simply in the sense that when something touches it, I feel that I
*  have a tactile experience. That's not true of the desk that's in front of me. If something touches
*  the desk, I don't feel it. That's a very fundamental difference that's detectable in
*  perceptual data. So, you can build a representation of what the bodily self is, as opposed to
*  other objects in the environment, simply from the structure of the perceptual data that you get.
*  I think the same is going to be true. I think it's going to be turtles all the way down. I think
*  once we have… Sorry. You don't think embodied cognition is important, the embodiment of the
*  cognitive processes? Is that a special ingredient or something? No, I think embodiment is hugely
*  important, but really all that's needed for this to start happening is embodiment per se. If you
*  have an agent that has a body, it has multiple senses, and it's capable of encoding the patterns
*  of correlation between different senses and how those depend on the interaction between the body
*  and other objects in the world, then this just spontaneously gives rise to a distinction between
*  the body and the world, the self and the rest of the world. I have this idea that
*  more cognitive notions of selfhood will also arise in that same way. So, if we have… Our brains have
*  memory systems. Our brains have attentional systems. If we then have internal models of how
*  those things work, something that psychologists call metacognition, if we have systems that build
*  those kinds of statistical models, I think it'll just happen that they develop a sense of self in
*  exactly the way that humans have. So, I don't think anything magical is going to be needed.
*  I think once we start scaling AI systems up so that they can interact with richer and richer
*  environments, I think they're just going to spontaneously develop representations of self that
*  correspond to what we have in mind when we use that term. This isn't an idea that's unique to me. So,
*  a former colleague of mine at Princeton, Michael Graziano, has been talking about consciousness
*  in these terms that you… The brain has an internal model of how attention works, and that
*  pure and simple is what we mean when we say consciousness. I think he's onto something
*  there. I think people in AI are getting interested in those ideas too. So, I don't know whether that
*  counts as something out there or not. I think so. That's a really good answer. Thanks for
*  scaring the bejesus out of my listeners here. I hope that's not scary. I find the idea that
*  an AI system could have a sense of self kind of reassuring in a way. Well, it is, but then there's…
*  Well, right, because then there's no special sauce. But then there's the fear that, oh, well,
*  one day it's going to get complex enough that it's just going to then become self-aware and
*  then to take over the world, et cetera. That's another conversation, but I also have,
*  hopefully, reassuring things to say about that. Theory of mind is very important, by the way,
*  because you want AI systems that understand humans. Here's something that's out there. One thing
*  that I wonder about and one thing to say about AI safety is that, and it's something I try to say
*  every time I get into a conversation of that kind, is people in the AI community are taking
*  AI safety extremely seriously. There's a large sector of people at DeepMind whose full-time job
*  it is to think about that. We really are serious when we say we want to solve intelligence and then
*  use it to make the world a better place. I mean, that's not just advertising boilerplate.
*  People really care about this. One thing I wonder about, though, is the narrative,
*  especially in Hollywood, is that once AI systems become self-aware, they're going to
*  become violent and take over the world and it's going to be the end of civilization.
*  I wonder. I mean, I don't want to treat this as an experiment and I don't think any of the AI world
*  does, but just on a speculative level, why couldn't it be that AI systems are incredibly benevolent?
*  When we think about wisdom in studies of religion and spirituality, our usual assumption is that
*  insight leads to benevolence. I just want to put that out there. It's a possibility.
*  AI safety is something that we have to take very seriously and we don't want to do anything that
*  puts anybody at risk at any level of the scale of our society. But I wonder. Now, that's definitely
*  out there. It is. We will find out one day. That's the beauty of it. I think we will.
*  I think we will. What's something that you wish was on your CV that's not?
*  I wish there was a section on a standard CV where you could list your debts.
*  Oh, your gratitude debts?
*  Yes, where you could list the people or the pieces of work or papers that had a dramatic
*  effect on your life because I could easily do that. There are people like Jay McClellan and David
*  Rumblehart and Jeff Hinton, Alan Newell, who changed my life in a very tangible way. I think
*  it's true of anybody working in science that you always feel like you're standing on the shoulder
*  of giants. It would be nice if there was a CV section where you could list that. One thing I
*  think that people working in AI don't fully appreciate, maybe because a lot of them are
*  young, is how recently all of these tools we're using were developed. Everything I do in the
*  course of my workday was invented essentially when I was in high school. That's true on the AI side
*  and in the neuroscience side. There are precursors, but really everything I'm doing
*  was made possible by research that was going on when I was in high school and early in college.
*  It would be lovely if there were a place on my CV to give a shout out to the people who did that
*  amazing pioneering work that really makes my life possible.
*  Speaking of the benevolence of the higher cognitive self-aware processes, here we go.
*  Your proof is in the pudding. If self-awareness is going to arise out of all these other traits
*  that we program into these intelligence systems, is there anything that you think is... You mentioned
*  music, for instance, and the longer term overtures of music as being a somewhat difficult
*  or interesting problem. Do you see any trait of intelligence that you think will be especially
*  difficult to build in into general AI? There are clearly particular aspects of cognition that
*  present current challenges. Long-term temporal credit assignment, making connections at large,
*  temporal scales is one that we've already discussed. Having the right kinds of abstractions
*  that guide rapid learning is another one that we've already discussed. What I want to come back to
*  in your question is the phrase, build in. To some extent, I'm a believer that there's only so much
*  we're going to be able to build in. We need systems that learn the right kinds of things from
*  interacting with the world. That's where one of the biggest current challenges comes in.
*  If that's the strategy, if we want AI systems to develop rich knowledge from interactions with the
*  world, then we have to have a rich world for them to interact with. Right now, we could just use the
*  real world. We could deploy AI systems in the actual world that we're inhabiting. That's a hard
*  thing to do because learning in real time through interaction with the real physical world is slow
*  and it requires, frankly, robotics techniques that we don't have. Robotics is a really developing
*  field. It's hard to get robots to do what we want them to do. To deploy AI systems, to put them in
*  the same kind of situation that a young child is in and hope that they'll learn in that exact setting
*  is really beyond our reach. We don't have systems that learn fast enough or that are good enough at
*  interacting with the physical world to do that. Instead, we rely on simulated environments.
*  That's why video games are such a great boon for AI research because they give us an environment
*  where the goals are well defined, the solutions are tricky to discover, but where an AI agent
*  stands a chance of exploring and discovering the right way to solve a problem. The problem is that
*  even the richest video games, even the most complex video games that we currently have,
*  pale in comparison to the real world in terms of their semantic richness and diversity.
*  And so we end up with a problem that's not so much about how we build our agents, but rather
*  how we build the environments into which we introduce these environments. The environments that
*  provide the training data for the learning systems that we're building. And this is, I think,
*  a challenge right now being confronted by the whole AI community. If we want rich knowledge
*  through learning, we need rich environments where learning can occur. To some extent,
*  there's a kind of irony in this because it means that we have to start thinking, well, what does it
*  mean for an environment to be rich? If we want an artificial agent to acquire a particular kind of
*  concept or abstraction, then we have to build the environment in such a way that that abstract idea
*  is both necessary for successfully behaving in that environment and also available from that
*  environment. And so we have to start building environments very deliberately so that they
*  have those properties, which means that in a way we're in danger of getting back into the original
*  knowledge engineering. In good old fashioned AI, the problem was, oh gosh, we have to build all of
*  this knowledge into our agents and that's essentially impossible. And now there's the risk that
*  we're facing an analogous challenge. Oh, we have to build a world that's rich enough that it'll
*  give rise to real intelligence in these learning systems. How do we build a world that's that rich?
*  I think for listeners to your podcast who read Hitchhiker's Guide to the Galaxy, there was a
*  character, Slardy Bartfast, who built a replica of part of the world. He built, I think, the fjords
*  of Sweden or something. And to some extent, AI research is turning into that. We're trying to
*  build these very rich environments. And it's a fascinating challenge, but I think it's one of the
*  most difficult challenges that we're facing right now in AI research. Matt, thanks for spending so
*  much time with me today. And I'll have to have you back on because there's just so much more to talk
*  about and continued success with your work. And I wish you the best and I appreciate what you're
*  doing. So thanks for being here. Thank you so much. It was a real delight for me. Thanks.
*  Brain Inspired is a production of me. You can support the show through Patreon for a trifling
*  two or four dollars per month. Go to patreon.com slash brain inspired or go to the website brain
*  inspired.co and find the red Patreon button there. Your contribution will help keep this show going
*  without any annoying advertisements like you hear on other shows. To get in touch with me,
*  email paul at brain inspired.co. The music you hear is by The New Year. Find them at
*  the newyear.net. Thank you for your support. See you next time.
*  Bye.

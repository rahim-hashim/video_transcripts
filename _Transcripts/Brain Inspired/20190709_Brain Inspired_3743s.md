---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3743s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 4665
Video Rating: None
---

# BI 040 Nando de Freitas: Enlightenment, Compassion, Survival
**Brain Inspired:** [July 09, 2019](https://www.youtube.com/watch?v=lAZlf98Tqg0)
*  I do believe that in the long run, we will have to fare into space.
*  This planet has a limited lifetime.
*  Basically, much of the history of AI is we believe some things are hard and they turn
*  up to be easy and things that we think are easy turn up to be hard.
*  We're really bad judges.
*  Terrible.
*  Of how we think or what is hard and what is easy.
*  This is Brain Inspired.
*  Hello everyone.
*  This is Paul Middlebrooks.
*  You just heard Nando de Freitas, a long time machine learning practitioner and one of the
*  first, if not the first person to record his lectures on machine learning and post them
*  for free on YouTube, which have been viewed and appreciated by many, many people.
*  So it's a really great service that he provided.
*  Like a previous Brain Inspired guest, Matt Botvinnik from episode 21, Nando is at DeepMind
*  and he also has an appointment at the Canadian Institute for Advanced Research, CIFAR.
*  Unlike Matt, my previous guest, Nando's background and general thought process is definitely
*  on the AI side of the neuroscience AI spectrum.
*  As most of you know, my guests have tended to be heavy on the neuroscience side, so it
*  was fun and enlightening to hear Nando's take on everything.
*  I will continue to invite guests more on the AI side of things, which has always been a
*  goal.
*  It just hasn't worked out like that yet.
*  On the show today, we talk about Nando's principled reasons for studying AI in the first place.
*  Why he thinks to understand our minds, it's worth studying both single agents and multi-agents,
*  his balanced view of being inspired by neuroscience but also influenced by engineering concerns
*  when developing AI systems, and what it looks like through his eyes to observe neuroscientists
*  in their native environments doing neuroscience experiments.
*  We touch on a couple of the topics that he researches, but we don't dive deep into any
*  one area.
*  So, I will put a host of his recent papers that are relevant to our discussion in the
*  show notes for you to find and enjoy.
*  They cover a range of topics, including meta-learning, which we talk about some in the show.
*  He works on few-shot and one-shot AI agents, which are agents that can learn things with
*  just a few or one example, respectively.
*  So, a classic problem with modern deep learning is the ungodly amount of data examples that
*  a network requires to learn.
*  So, his work addresses that problem.
*  He also works on something called neural program interpreters, which are programs that learn
*  how to represent and execute other programs.
*  So, he's all over the place if that place is the forefront of modern machine learning
*  research.
*  Like I said, I will link to all of that in the show notes at brandinspired.co.
*  slash podcast slash 40.
*  If you like the show, you can support it on Patreon.
*  I'll tell you more about that later.
*  But you can also help by simply telling a friend.
*  And thank you in advance for that.
*  I even had someone email me and tell me they plan to use the show as a sort of journal
*  club for one of their courses.
*  So that was delightfully terrifying.
*  One note before we start.
*  I had to record this episode with an unusual recording setup.
*  So apologies that my audio is less than stellar.
*  You know who is stellar?
*  This person.
*  Nando, thank you for being on the show and welcome.
*  Thank you.
*  So, you are a busy person.
*  You're a principal scientist at DeepMind and you have an appointment at the renowned Canadian
*  Institute for Advanced Research, otherwise known as CIFAR.
*  But what I really want to know is how different your life is now compared to how you envisioned
*  it when you were growing up in Africa without running water or electricity under the apartheid.
*  Actually, I was born in Africa and I did spend my early years in Africa.
*  But when I encountered having no water and electricity was in Europe.
*  Oh, is that right?
*  That's correct.
*  Oh, I heard incorrectly.
*  In Madeira Island, part of Portugal, when I lived there, there was no water for four
*  years that I was there and there was no electricity at the beginning.
*  Eventually, you know, like all houses started getting light.
*  So modernity didn't get to Europe that long ago, or at least not to all of Europe.
*  I certainly didn't dream of being at DeepMind in those days.
*  I was just a happy child content with things around.
*  I guess you definitely didn't have Atari games, but you could have been playing chess and
*  Go for all I know.
*  No, actually, what I found always the most entertaining was to be in nature and to play
*  with ants and so on and to see how things work and understand how wasps build their
*  nests and how their whole life cycle and so on.
*  That's always what fascinated me, life.
*  That's great.
*  Well, you have come a long way and you've been in the machine learning world for a long
*  time now.
*  You even have some of the, I think some of the earliest courses that you made available,
*  just your lectures on some machine learning and deep learning.
*  I'll link to those in the show notes because they're excellent.
*  Of course, they've been viewed.
*  Everyone's probably already knows about them, everyone listening to the podcast.
*  Thank you.
*  But you've talked about your reasons for working on AI and you've sort of given three
*  reasons and I just kind of want to walk through those and talk about them for a second.
*  So one is enlightenment and understanding how our brains work.
*  And I mean this in the nicest way possible.
*  Why not study brains then?
*  Well, I do mean brains, but I don't think we should be thinking of only like say the
*  brain of one creature.
*  The whole human race can be understood as one brain.
*  It's a collective brain.
*  And it's also very interesting to understand that.
*  And also because for me, the concept of mind goes beyond just what's inside your head.
*  So for example, I don't remember the phone of my girlfriend, the phone number.
*  So I have to rely on my, you know, to have an argument, of course.
*  But I do rely on mobile device.
*  And there's a particular motor command that I execute that I've memorized that retrieves
*  that information.
*  So my mind is now being externalized into the devices that surround me.
*  In fact, it's externalized in people as well.
*  I rely on people to answer.
*  I know that for some people, if I ask them a question, they will answer it.
*  So I take advantage of that.
*  In the sense, I think mind is a broader concept than just what's inside your head.
*  So are you a hardline extended cognition thinker then in the domain of Andy Clark and folks
*  like that who, you know, is this more of a concept or is it a real thing that our cognition
*  is extended into in our minds are extended into a broader scope like that?
*  Yeah, I don't know if I would put myself in the group of those amazing philosophers.
*  I don't feel I qualify to be there.
*  But I certainly from a practical perspective, for me, the division, the boundary of what
*  makes an agent is not a clear one.
*  And this transpires very clearly in the research that we do as well.
*  When we treat, when we build some neural networks for multi-agent research, but quite often
*  you can look at it from afar and you see, okay, this is just one single neural network.
*  And you can think of communication between agents as well.
*  This is just a part of the network sending information to another part of the network,
*  which is no different than a single what we do in a single network.
*  So the divisions are not clear.
*  And hence, I think it's important to study both multi-agents and single agents.
*  I think they just give us different perspectives on how to approach the problem.
*  I also think that to address some of the important problems that we face in society, like, you
*  know, economic problems, making sure that everyone has a reasonable income and so on.
*  We need to actually understand society.
*  So we need to understand groups of brains ultimately, not just a single brain.
*  Yeah.
*  So that's an important reason for doing it.
*  And in motor control, it's also useful because in terms of storage, I think that's a very
*  useful trick that I don't have to remember everyone's phone.
*  What I remember is a key.
*  And I remember a set of motor controls such that when I execute the motor control and
*  my fingers start touching the phone, I know that I will encounter information along the
*  way that will guide the next sequence of motor controls and so on.
*  And that, to me, is a much more parsimonious way of storing information than if I was storing
*  everything that's on my phone in my head.
*  So in that sense, I think I would say I am with Andy Clark and so on and the externalists
*  and all that, but in a very pragmatic way.
*  Yeah.
*  So just so many points.
*  I just wanted to go down the road there and diverge because this takes us back all the
*  ancient Greeks about language and how it's going to ruin us versus whether it's helpful
*  to write things down because it'll either ruin our memory or it'll help us encode the
*  information moving forward.
*  So all right, let's skip that for now.
*  But understanding the social aspect, lots of brains together, brings me to your second
*  reason or a second reason for why you have said that you study AI and that's compassion
*  and that's understanding and encouraging empathy.
*  And you've stated that machines are going to need compassion as we build them.
*  I don't know if you want to comment further on that.
*  Yeah, I mean, I think that's self-evident.
*  It's I don't think we understand well how to bring all the richness of emotive systems
*  that humans and other animals have into machines.
*  There have been some attempts, but I feel like often they have been, you know, very
*  simple, hard-coded rules as to what happened in this or what sadness is for a small agent
*  in an environment.
*  So I think we are very far from understanding all the rich emotional system or the rich
*  set of neurotransmitters and so on in the brain and different parts of the brain that
*  is responsible for in the brain and the nervous system in general that are responsible for
*  emotions. So from that perspective, I do think we need to do a lot more research.
*  There's two goals here. One is to do research in a motor systems to understand better what
*  we are, you know, to understand humanity better and to understand that other animals
*  better. And I think in that understanding, compassion arises in two ways.
*  It will allow us to see that, for example, oh, my God, this dog has this very rich emotional
*  system. It's capable of sadness and happiness.
*  My dog certainly is.
*  And that allows us to relate better to other animals and so on.
*  So I think that's part of that discovery process.
*  But it also that same compassion that I want to have toward my dog and I hope you have
*  towards yours, the compassion that I would like machines to have toward me.
*  So I think if we're building artificial intelligence systems and if we want to build
*  general artificial intelligence systems, to me, there's still a question as to whether we
*  want to do that or not.
*  But if we do, then I think compassion is a must.
*  They need to be able to empathize with us and be compassionate.
*  So when I was in early in my college undergraduate career, my friend and I were it was
*  late at night and we were sitting on his front steps and we were talking about the future
*  of humanity taking and the future of Earth.
*  And his take was that we are ruining the Earth as we know it.
*  You know, the rainforests are disappearing and such.
*  And we need to figure out how to fix our problems here.
*  We need to figure out how to not destroy the Earth.
*  Before we do what I thought was important, which was colonize space, get off this planet
*  because we're going to crowd it and we need to figure that out.
*  There's going to be so many problems we got to figure out as fast as possible.
*  At the time, I didn't think about it, but these two are not mutually exclusive ideas,
*  which brings me to your third reason for studying AI, which is the one that really seems
*  to get people these days is survival.
*  That we have to, A, get off the planet and B, make the planet last longer
*  because there is a limited time.
*  Yes. So so I do believe that if you think about existential crisis and AI, I do believe
*  that in the long run, we will have to fare into space.
*  You know, this planet has a limited lifetime.
*  It's a huge one.
*  So probably a lot of things could go wrong in the time that the solar system will exist.
*  But we know that there's an upper bound there.
*  And we know that if you don't develop AI systems and robots that can build sustainable
*  life systems for life and space, we will be in trouble.
*  Robots can sort of fare into space.
*  We know this because we send robots to Mars, but it's very hard to send people to Mars.
*  And so developing autonomous agents that are capable of building life preserving cities,
*  think in space, it will become important in a very distant future.
*  There is, and here I guess one has to bring in some speculation.
*  You know, if you talk to a physicist, they'll tell you about meteorites that could hit the Earth.
*  Yes.
*  They have hit us before.
*  They could hit us again.
*  Folks talk about super volcanoes and so on.
*  So there's clear threats.
*  I mean, these are very unlikely events, but we know that in 100 million years,
*  again, there's upper bounds.
*  So ultimately, for the survival of life, so that we can have any hope of perhaps meeting
*  other species in the universe, then our only chance is to develop AI.
*  Of course, I also think in the short run, data AI systems, data statistics, better machine learning
*  basically is what I'm referring to as AI here, will also enable us to understand better what I'd
*  say the weather conditions to be able to understand how to be able to monitor the planet better.
*  So we can make more intelligent decisions about the resources in our planet.
*  So I think that's about how to or give us guidance on how to manage energy or maybe help us develop
*  new ways of coming up with friendly types of energy sources that will enable us to then be
*  much more sustainable.
*  So it's clear that we are in a pickle now with where the human race is and the planet and so on.
*  And the way ahead, one of the ways ahead is by trusting technology.
*  Okay, so in general, on the podcast, I have interviewed people heavily on the neuroscience
*  side between the two facets of neuroscience and let's say AI or machine learning.
*  You are a great example of someone who is, I would say, deep on the machine learning or AI side,
*  but you also have this deep interest in understanding brains and forgive the pun saying deep, of course.
*  And you have reminded people on multiple occasions that our current AI systems were
*  dreamt up from early neuroscience experiments like from Hubel and Wiesel.
*  However, we do all know that how divorced dreams can be from reality.
*  And some of the best dreams are some of the most fantastical and least realistic.
*  So where would you put yourself on the scale between pure AI and pure neuro if they were
*  clear distinctions? And maybe you can answer independently for your sort of daily workflow
*  practice and just your mindset. So I'm definitely not a neuroscientist. I'm more of a dreamer
*  or a creator of ideas and I sort of steer people to create ideas and so on and develop,
*  you know, sort of push the boundary of what exists in the world of AI.
*  I'm very interested in getting to know some of the things we have struggled with in the past,
*  things like awareness. How does an agent know what it knows? How does an agent know what it doesn't
*  know? This kind of question that we're so far from resolving with our current systems.
*  I'm also interested in perception, which is I still think highly unsolved and motor control,
*  which is also unsolved, and you know, in a multitude of problems. For all these, I always
*  find it useful to go and read papers in neuroscience and papers in cognitive science,
*  because they inform my thinking and what things we can do. Of course, I'm also informed by
*  engineering. I know I can store in a machine all the data that a human perceives in their lifetime.
*  Right. All the pixels.
*  All the pixels and not just the pixels, the skin sensation, the temperature, the height,
*  and so on, which are signals that are just as rich as the pixels. I think there's an obsession
*  with pixels because that's kind of where tech has gone. Well, I just was referring to our impoverished
*  sensation that we don't even get all the pixels deep into our brains, right? Because we filter them
*  out so much. Correct. That's very true. And of course, we get it, as you know, in a very different
*  way than by a psychotic system and so on. And so it's important to look at the papers in
*  psychophysics and neuroscience, because they do sort of guide the design of AI systems.
*  And what we build might not be like anything that the brain does. It likely will be more efficient
*  and it will be different. But if we go back, I mean, a few years ago, I had the fortune,
*  actually, I kind of want to do a shout out here to Professor Fukushima, who gave us the new
*  Cognitron, who I think probably deserves a lot more recognition for his amazing work. So I met
*  him in Japan. I had the fortune of attending a meeting there four years ago, and I had dinner
*  with him. And he was, you know, a lovely man, probably in his 80s, I'm not sure. But he's so
*  still very upbeat. And you know, he was drinking Sapporo with me and so on. So I asked him, how did
*  he come up with the new Cognitron? He mentioned he worked in a research lab with neuroscientists,
*  and they explained to him the Hubel and Wiesel model. And then he was inspired by the findings
*  of neuroscientists that he went and he started hard coding, you know, more or less what
*  would be the, you know, the first stage or second stage of V1. And so he thought of the, you know,
*  the convolutions and the pooling. And he added the RELLO units, which have been rediscovered.
*  And, and of course, he had some sort of learning rule, which was competitive. And that's basically
*  the one of the big success stories of learning the convolutional network architecture. Of course,
*  it later was refined by Jan LeCun by with automatic differentiation. So that was an important
*  advancement as well. But I think that sort of there's a clear thread there of how neuroscience
*  inspired this. The other workhorse out there in has been LSTM. And once again, they were
*  sort of inspired by cortical circuits. And so what gets produced at the end is perhaps a model of
*  a neuron that's not quite like a cortical neuron, but it nonetheless drew inspiration from that
*  literature. And finally, there's the models of attention. Again, there's been a lot of
*  literature in cognitive science and attention and so on. And that's also has sort of somewhat
*  motivated. Having said this, I don't want to say that everything that there's out there in cognitive
*  science and so on, there's also a lot of quite often, and this is what the engineering matters
*  to me. So the inspiration matters. But at the end of today, you have to build it, you have to have
*  a way of measuring performance, and you have to make sure it works. So what I don't like is when
*  people build these proposed these huge models of how the attention works and how awareness
*  in the brain, in the brain, say, and then there's no experiments. It's just a proposal or the
*  experiment is like a really tiny thing that it's not compelling enough. You don't like thought
*  experiments. So I think those are useful. It's useful to have paper. I mean, in fact,
*  the original papers and ICM and somewhere of that nature, the experiments were in that developed
*  with the ideas that proved to be useful. But quite often we have people build systems with,
*  you know, boxes and so on and attention feeds into awareness and awareness feeds into perception,
*  mental control. And it gives a lot of detail. And that's important detail. And that annoys the
*  deep learning crowd. And with some reason, interesting, although it's, of course, we need
*  to strike a balance. I think we need both things. We need sort of inspiration, but we also need
*  execution and measurement.
*  Patreon. I'm going to be producing some content soon that I will share with you as a Patreon
*  supporter. And I look forward to getting your valuable feedback on it. So stay tuned Patreon
*  supporters. If you dear listener would like to be a part of that, you can support the show for a
*  mere couple bucks per month. Go to brain inspired.co hit the red Patreon button there.
*  So when just in your day to day sort of workflow, when you're thinking about how to make an algorithm
*  work or how to build certain modules to work together, for instance, you know, how much of
*  your time is spent thinking on the engineering side and on the statistical side versus like how
*  brains might do it? Is it constrained at all thinking about that? Or is that just something
*  you take the inspiration from what you've a few papers you've read, and then you're back into your
*  engineering world? And I'm not trying to pin you down at all. I'm just genuinely curious.
*  So I'll mention this one example, because it's very recent is one of the things that's in my
*  mind right now, one of the problems I'm trying to solve. So the inspiration here is, if I ask you,
*  and I'm going to ask you, do you know what a two four is?
*  I do because I've read your big with your thoughts.
*  So okay, so you know what a two phase. But you can explain it for the listeners. I'm an expert
*  in two firsts, of course, but I'm going to leave it to you. Will you? Oh, no. So my understanding of
*  it, I thought, okay, I'll put that in the introduction. My understanding of a two five is,
*  well, I know what it looks like, from what I've seen, if I if I'm remembering correctly. So
*  there's this sort of an arrow shape is a three dimensional shape. And I've only seen them in
*  black and white, unless I'm remembering incorrectly. I don't know the function of the two, but I only
*  know the way it appears. That's pretty much it. So Justin and Balmour, when he gives me this talk,
*  he always shows images of two firsts. So he shows the images of a bunch of things are sort of alien
*  mushrooms. And then they're pretty similar looking. Yeah. Yes. And then he says these two are two
*  firsts. And then he shows you another one. And he asks you is that a two four naught? And people
*  are very quick to identify what a two phase. But I could also ask you, do you know what a script
*  Nick is? No. Okay. So basically, what I'm doing with you right now, at the mental level is I've
*  asked you about two firsts and script next, you know, what a two phase you have some sort of idea
*  of what it is, you can give an explanation of what it is. You also know that you don't know what a
*  script Nick is. So because this exists, we've just witnessed it in this conversation, it would be
*  interesting to enable our agents to also be able to know what they know, and to know what they don't
*  know. Now, a meta question here is why? Why would we want that from agents? And I think one of the
*  reasons why we want this is because we want the agents to explain themselves, we want to be able
*  to ask questions of the agents and have them to explain to us why they chose a, why they made a
*  particular decision, especially with our agents, we watch them acting, and it's almost impossible
*  you start humanizing them until and perform or fighting them and saying, you know, this agent is
*  going to the right of the maze, because you know, she wants to grab the apple. But in effect, what
*  tends to happen is the agent is just looking at a particular pixel pattern on the roof, perhaps,
*  and it's using that to guide it. So it has no notion of what the apple is or and so on. Sometimes
*  the agents do have that knowledge. And we're able to actually measure it. So we actually, for example,
*  if the agent uses an LSTM network, we can with a linear function regress out things like the
*  orientation of the agent, the location of the agent in the maze, and so on. So there's some sort
*  of form of the information is there. And sometimes it's not there, we would like to know what
*  information is there, what is not there, even before without us having to construct a test like
*  this by regressing out. So the natural way, I think eventually is for us to be able to ask
*  questions, just very much like the dialogue we just had when I asked you what is a twofer and
*  asked you to explain yourself and you went back to just an amount of presentations and so on.
*  So I would like to do that with agents. So that's the inspiration part. And then comes the pragmatic
*  part, which is like, how do I go about constructing a task where this is useful? Or how can I do this?
*  Or even if I don't construct a task where it's useful for an agent to know what it knows,
*  to know what it doesn't know, which is quite hard actually to do. It's difficult for humans too,
*  because we're notoriously inaccurate in our own metacognitive awareness, let's say,
*  and our own metacognition. Very much so. And so, but a simple thing I can do is maybe start
*  figuring out the question answering system where I can sort of ask the agent questions or ask an
*  agent to explain itself. And that quickly leads you into making sure that whatever you do with
*  language in these networks doesn't confound with the knowledge that's in the agent. So you start
*  getting into the pragmatics of how you construct the neural networks and so on, how you train them.
*  It also then leads to the question of how do you ensure that the agents are truthful?
*  And so you invariably end up in the world of causality and counterfactual reasoning and so on
*  and tests. And so you start going in that route. So basically, so you start with a big grand vision.
*  You sort of think of something that would be nice. It would be nice to have tasks
*  for which it's clear that it's useful for agents to know what they don't know and so on. But then
*  that turns out to be quite hard. Then you might then take a step back to something that's a bit
*  more feasible. Like maybe it's just a simple question answering system that asks the agent
*  how far are you from the wall and so on. And you could try to think of how to construct a data set
*  for this and try to think of how to train an agent to do this type of work. And so this
*  is work that actually some of the folks that work with me, some of my collaborators have been doing.
*  So you sort of try to go back and try to find a way, a problem that you can attack.
*  You have to figure out a way of measuring performance. And so defining clearly what
*  your goals are, how will you know that you will succeed or not with your research.
*  And yeah, and also have some de-risking strategy. If you go to for something too ambitious,
*  you might not succeed. So sometimes it's also good to have some simpler goals or sort of
*  more achievable goals and make sure that you can achieve those goals. So de-risking is important.
*  And of course, then there's all the other things that are sort of obvious, which is you should be
*  thinking of baselines and so on. So it was really difficult actually preparing to talk to you because
*  you've done so much recently in so many facets, but sort of the overarching theme that I've seen
*  in the recent few years of the work that you've put out on an archive and other venues has been,
*  in my mind, it's been sort of expanding AI beyond its narrow ability to do a few things extremely
*  well. And I guess generalization is the word that seems to tie all of your different facets of work
*  together. And so would you say that's accurate? And then what would you say is the most critical
*  question that intrigues you right now? Is it this idea of teaching machines to learn what they do
*  and don't know? Or is it a meta-learning drive? Yeah, I think one of the questions that interests
*  me the most right now is the meta-learning question, because it's about how will agents perform
*  in different environments? How do they perform when their bodies are slightly different? Because
*  every time we wake up, our bodies are slightly different depending on how well we slept and so
*  on. But we don't even perceive that. But if you work in a robotics lab, then you become aware of
*  this very quickly, because you realize that if you collect data one week and then with deterioration
*  a few months later, you're trying to test the policy that you learned before and it fails,
*  because maybe there's dust now in the joints of the robot or hysteresis or something like that.
*  So agents are adaptive and we live in non-stationary worlds. Our worlds keep changing.
*  And so we're adapting over time to new tasks. So you can think of the
*  non-stationarity of the world as many tasks. And then of course, there's also a parallel aspect to it.
*  If you think of like, say now going to agents as populations, if you think of how we do hospitals,
*  whatever treatments we do in different hospitals should inform the treatments that say a nation
*  should follow up. If one hospital is sort of doing better or what data they're gathering,
*  the summary statistics should go to the nation. If there's a national, something like the NHS,
*  they can come up with a better update, a meta update, and then distribute it back to their
*  hospitals. And then this process keeps going on and also with time. So having things in parallel
*  and sequentially are very natural. And in fact, this is what hierarchical base was sort of developed
*  for and has worked very well at it. And for now several decades with the basis of decisions.
*  I think with meta learning now with the neural networks and automatic differentiation, we've
*  been able to do a lot of new exciting things in terms of learning loss functions automatically,
*  learning optimizers, learning networks, learning new architectures. There's a lot of fascinating
*  stuff going on. And a lot of it is about also using data to perhaps learn some inductive biases that
*  allow you to learn faster. But it's also about trying to figure out what are the inductive
*  biases that will allow you to learn something in one domain and then some say pockets of knowledge
*  and then be able to take some of these pockets of knowledge to solve a new task.
*  And machine learning traditionally has dealt with the approach that there is smoothness in the data
*  that's essentially, so the idea is that you train in your training data, you test in your
*  validation sets and so on. And then you hope that those model will transfer to will also do well in
*  the test set. So intrinsically there is an assumption of smoothness in the function spaces
*  here. But what we're now after is not just about training a classifier, but rather we want to learn
*  multiple neural networks, say, or multiple modules of knowledge. And then we want to transfer
*  some of these, reuse some of these. The useful parts.
*  Correct. So repurpose some of these pockets of knowledge. And of course this will be context
*  dependent. In a context use some knowledge will be useful, in other contexts a different type of
*  knowledge will be useful. And every time we go into a new environment there's an opportunity
*  to learn new modules which we can add to our sort of big system of modules. So here there's a clear
*  inductive bias I'm talking about which is modularity. But I think this is an important one,
*  especially if we start thinking of independent modules of knowledge, then it starts tying also
*  with the work on causality. We want to learn, say, physical laws like invariant mechanisms.
*  Mechanisms that would work across many environments and then be able to sort of repurpose
*  these mechanisms to build larger systems of thought to solve new tasks. That I think is one
*  of the most fundamental questions going on in science right now, is this question of adaptability.
*  And in particular I want it to be fast as well. So I think a key thing is that I don't want to go
*  to a new environment and then have to spend a lot of time learning. No, I want to do this quickly
*  the way humans do. And I think that's what meta learning buys us to a large extent is this idea
*  to be able to do fast inference or fast imitation. Just with a bit of data with one demonstration,
*  for example, you can do the task or with language description that's enough to do the task.
*  So it becomes easy to adapt the agent as well. So the agent is adaptive but you can also
*  just by providing a little bit of data you could adapt the agent to do something new.
*  This is exactly what you've done with your meta-mimic work, using imitation as a strategy to
*  use this one-shot learning or few-shot learning to imitate what an agent sees on YouTube, for
*  instance, or from another agent to then mimic that process. So this is exactly the work that
*  you've been doing. And I know that we're going to come up against time pretty soon here. So
*  instead of diving deep into your actual research in the papers, what I'm going to do is point to
*  a bunch of them that have this kind of common thread that you've already alluded to a lot.
*  Sorry to interrupt you, by the way, but you've alluded to a lot just in the course of your
*  thinking out loud sort of. So to get at this, first of all, you're giving a keynote address
*  at the Cognitive Computational Neuroscience Conference in Berlin in a few months. And
*  this brings together neuroscientists and AI researchers. What are a few of the topics that
*  you might talk about at CCN? I know it's really early yet and things happen so quickly, but do
*  you think it might be about this meta-learning? Oh, gosh. Yeah, I still haven't decided what I'm
*  going to talk about, but I think meta-learning would be a good topic. It is a topic that
*  is of interest to cognitive scientists and neuroscientists at large. I mean, there's
*  interest in possession now. There's an interest in learning with few data, being able to do
*  fast inference. And of course, a lot of the meta-learning was largely, again, inspired by
*  words done in psychology, with people seeing how quickly, say, monkeys will learn the meta-task
*  when they're doing specific tasks, the work of Harlow, which I don't have time to describe here.
*  That's okay. I'll refer people. I had Matt Botvinick on the show. So we talked about his
*  meta-learning work and then we talked about the Harlow experiments during that episode as well.
*  Yeah. And actually, I'm always chatting with Matt. So that's a good example of that sort of,
*  I guess, what Fukushima had in Japan back in the 60s and 70s. It's something I have nowadays
*  here at DeepMind because I get a chance to work and collaborate with Matt on some of the
*  meta-learning projects and find that to be extremely useful and enlightening.
*  Yeah. Well, how do you think that, so Matt's sort of from a psychology, neuroscience background,
*  but he's also been in the machine learning world a long time. But at a conference at something like
*  CCN, it brings together these different people from different backgrounds and expertise.
*  How can cognitive science and computational neuroscience and artificial intelligence best
*  work together, you think, now that you're in this sort of boiling cauldron at DeepMind where that's
*  kind of happening? I think we just need to keep talking to each other. We need to listen to each
*  other's presentations. And even if all what you get is 10% of the presentation, then you can always
*  get together and have lunch with people in the outer field. And you can ask questions.
*  Yeah, perhaps with support or in Berlin, I'm not sure.
*  There's always a way to engage with other people in which you actually can get to learn a lot.
*  And this pretty much has been what we've done at CIFAR for the last 20 years.
*  So CIFAR always brings neuroscientists and cognitive scientists and machine learning
*  researchers together. And then we discuss, you know, we have presentations and then most of
*  the meetings are actually useful discussions where you get to learn a lot. You know, I go for,
*  so for example, one of the people who I enjoy going out for lunch is Bruno Schauzen.
*  And I mean, it's fascinating. You learn all about, you know, like the experiments that people do with
*  trying to, you know, deal with insect brains and so on. And then the issues with, you know,
*  sometimes you just learn about, you know, like all the sort of experimental issues that they might
*  have with say the brain's not exploding when they're trying to sort of analyze the brain,
*  trying to open the brain of a fly or something. And so these are things I don't usually think
*  about. So being able to sit down with Bruno and talk about jumping spiders and learn all the many
*  amazing things that humbling things that a jumping spider can do is just fascinating.
*  And, or learn more about the understanding that neuroscientists have of a single cell in V1.
*  And also be able to get a good grasp of the difference between findings that are based on
*  a monkey sitting in a lab versus, you know, an animal that runs freely on the fields. I think
*  that that's very important. Occasionally engaging also with neuroscientists in labs and experiments
*  also useful. So I had a pleasure of doing that with some neuroscientists when I was at UBC in
*  Vancouver. And then you go there and you see what kind of measurements they're getting of
*  their neuron readings. But you also see the measurement system that they have in terms of
*  cameras and so on to be able to track say a rat. And then you realize, wow, you've invested a lot
*  on these chips to measure neurons, but you're using such a simple tracker to track this rat.
*  And you're trying to infer some something deep about the hippocampus, but you sort of
*  visual that is so poor. And maybe what's really happening here is not as right as planning which
*  buttons to press, but just how to escape this cage. So it's useful to, like, I wouldn't,
*  you know, to be able to sort of understand what neuroscientists do, it's really important to
*  actually have these meetings with them and to engage with them, you know, and vice versa, I
*  think. And chastise them for using such crazy methods to measure things.
*  Yeah, you know, it's more understanding better where the data comes from, so that we just don't
*  go on blindly satanising it. But we actually have a better understanding of the difficulties that
*  they face. Because in doing that, actually, what you learn is that, well, they're using those
*  methods, but that's because we haven't provided them with better methods. And so in a way, we're
*  the ones that are at fault for not having given them better computer vision systems
*  that they could use to track, you know, the rats, and we'll say 3D frames.
*  Wes, what do you think is the neural basis of consciousness? What is consciousness?
*  Nora, what do you think the neural basis of consciousness is? What does that even mean?
*  Bringing that back to the, you know, I asked you what is most intriguing to you, and you talked
*  about meta-learning. What do you think that we need more of to understand these things? Do you
*  think that we need better technology? Do you think we need better or more data, or better models,
*  for instance, or theories? I think we need to be able to train agents in many diverse environments.
*  So this is one thing that has been missing. We often design for a specific task, and we're very
*  good at doing that. We're very good at designing an agent to play go. We're very good at designing
*  an agent to classify images or to do speech recognition. But if we're trying to think of
*  designing agents capable of a wide range of tasks, then that turns out to be very hard.
*  So that's certainly something that we need a lot more. The other thing is there are
*  things that are not essential to, I think, what we would define as maybe intelligence or
*  understanding brain, but things like motor control, which I still think are very important,
*  nonetheless. And for me, no satisfying understanding of the nervous system is
*  accomplished until we understand motor control. And so it's not enough, but it's essential.
*  It's a sort of a requirement for me. And we are very far from that. I mean, we don't know how to
*  build a machine that is capable of tying shoelaces and at the same time being able to chop an apple
*  and be able to fold a towel and be able to do a variety of things that a three-year-old does.
*  Actually, no, I take it back. My three-year-old doesn't tie shoelaces. I think it takes about
*  six years for humans to learn to do that, if not more. So it's actually a very hard task.
*  And in that sense, what's missing there is we still don't have good robotic
*  hardware. The hardware is coming along. We still don't have good ways. Machine learning hasn't
*  really hit robotics as it should either. So I think we're so far from... And why that is interesting
*  is because if we could do machine learning with actual real robots and so on, it's very easy to
*  create many tasks in a real system, except that the tasks that will require that you run them in
*  real time. So sample complexity is something we would need to address. And this is why I think
*  mental learning also comes in. Simulation allows us to run things thousands of times faster than
*  real time. So we can do a lot more experiments. So we don't need to care about sample complexity.
*  But I think that's a bit of a trap. And it's useful for a lot of things and might allow us to
*  see, to solve some problems that we're not solving because we haven't solved sample complexity
*  and meta-learning. But it nonetheless is a trap in terms of we not being able to solve lots of
*  tasks with few data. Yeah. So when you're sitting down with a neuroscientist, a Bruno Oelshausen or
*  a Matt Botvinnik or something, what are you looking for from the neuroscience side? What
*  is something important that you think that neuroscience will or can contribute to AI?
*  And how much neuroscience is the right amount for AI? This goes back to what you were just
*  talking about with simulating and how some things are necessary but not sufficient and so on.
*  Yeah. I guess when I talk to a neuroscientist, what I'm looking for is inspiration. And in a way,
*  when I sit down with Bruno, the first question I asked him was, okay, so what's the latest?
*  What's new? Yeah. Yeah. What's new? He asked you the same thing probably, right?
*  Yeah. And you just want to find out, okay, maybe there's this new finding that's very interesting
*  and this means that we now have a good chance of finally understanding the role of top-down
*  processing and perception, something like that. What's something historical that's not mainstream,
*  an idea or a body of work that you think that neuroscience or in your case, really more machine
*  learning or AI needs to be paying more attention to? I think we're paying attention to a lot of
*  important problems right now. It's hard to pinpoint things that are sort of being underestimated.
*  One that I think, and this was true of it two years ago, but fortunately, it's been corrected,
*  is counterfactual reasoning, causal thinking. But now that has hit deep learning as well. So folks
*  are thinking about that. I think that's very important, not just because of societal reasons
*  and bias and all that, but because I think it's essential to build such systems into the agents.
*  I think that's also essential to understand independent mechanisms and so on, as Bruno
*  Schalkhoff and his team have been doing, which is what also will allow us to get agents that
*  generalize with fewer data, fewer resources, and that reuse and repurpose their knowledge.
*  So I know that you are interested in consciousness and awareness, and you've done some work on
*  showing that the internal states of recurrent neural networks are maintained over time,
*  so they have some sense of internal awareness in that regard. You've used change blindness
*  to demonstrate how bad we are at introspecting about our own minds. I don't know if you want
*  to elaborate on that, but my question is, will our poor introspection thwart our progress in AI
*  in understanding our own minds? Are we going to get in our own way?
*  Definitely, I would say. I mean, that's basically much of the history of AI,
*  is we believe some things are hard and they turn out to be easy, and things that we think are easy
*  turn out to be hard. We're really bad judges of how we think or what is hard and what is easy.
*  So I do believe strongly in that. And I'm trying to see, and you're probably right,
*  I might be contradicting myself here, because I do believe in change blindness. I mean, I think
*  that's very clear, there's data. But I also know that I know what a two-phase is, and I don't know
*  what a script neck is. I just made up that word a few minutes ago. So there are things I know,
*  and there's things I don't know. And that's sort of useful knowledge. And knowing about my body,
*  knowing about what I can do with my body, knowing about that helps me because it will help me,
*  I don't know, choose my pose, make sure that I'm looking at you when we're talking, and so on.
*  So I think that also is an important part of the puzzle. I think we do have some awareness
*  of external things to us, of our bodies, and of our thoughts, some more than others.
*  Your dog, not my dog.
*  So it's something that I think we need to study, and we need to understand, because it's also kind
*  of what allows us to explain ourselves, and just tie with explanation and causation. So I think
*  it's an important problem that we can study. And it's grounded, it's a scientific problem.
*  So I'm not interested in the sort of metaphysical awareness, or the heart problem,
*  or sort of consciousness, and so on. But I'm more sort of thinking of the
*  Contramy, or how Chalmers calls it. Is it the weak one, or the easy one?
*  But I think it is perfectly feasible to build, and I think we just haven't done it, but to sort of
*  build a machine that is aware of what it knows, and what it doesn't know, that has a model of
*  what it knows. What it knows. Yeah, this is, it gets murky, because what do we mean by aware,
*  and etc., etc. You've mentioned the attention schema theory of awareness. I'm actually reading
*  a book by Graziano right now, and so far it hasn't really touched the heart problem, but
*  you're not interested in the heart problem. And so much of this is just moving the goalposts,
*  and understanding what it is we're actually defining and talking about. So anyway.
*  Yeah, and I'm trying not to call it just a name and leave it there, because,
*  and it can be anything really. You have to define it computationally.
*  Right. Correct.
*  So we're terrible introspectors. We're also terrible at prediction, longer term prediction,
*  right? We don't have flying cars and such. Yeah. So a hundred years from now, Nando, how will people
*  write about this era in AI? It certainly was a turning point. No doubt, people will see this
*  was a turning point. Is there another AI winter coming? I don't know if there's more winters
*  coming, but this was definitely a turning point. I think in technology and everything. I think in
*  my lifetime, I've gone from there were no personal computers to everyone carries one
*  in their pocket almost throughout the entire planet. There's as many of these computers as
*  there are humans. And it was predicted by early computer manufacturers that no one would even want
*  a personal computer. Speaking of how poor we are at predicting.
*  I don't know if they were thinking of iPhones, but I still remember when the first one came out,
*  and that wasn't long ago. And how dramatically it has changed the world and how people behave as
*  well. We behave so much better now, don't we? No, no. In some ways, yes. And in some ways,
*  not. I think that's part of who we were sort of seeing ripples. And hopefully we will adjust and
*  sort of keep the good things of finding new technology and learn to put aside the things
*  that are not really useful to us in the long term. This is a challenge. Finally, Nando,
*  I know you have to go. What is something that you used to believe that you find naive now?
*  Oh, that's a good question. Oh, this one gets us get metaphysical.
*  Yeah, great.
*  I'm trying to think of something technical. What comes to mind on a technical front is during my
*  thesis, I started, you know, I was doing neural networks, and then I was estimating the hyper
*  parameters by gradient descent. So I built these sort of hierarchical systems where everything got
*  to be estimated by gradient descent. And then I abandoned that work, because I felt like it wasn't
*  like fancy enough. And I started doing a lot of work on interacting particle systems, you know,
*  sequential Monte Carlo, because it was cool, you could learn a lot about probability. And then
*  there was this esoteric thing called measure theory that I got into learning. And, you know,
*  and I started learning about super marketing girls, and I started learning about, you know,
*  measurability, and so on. And then you could build these interacting particle systems, train your
*  neural networks. And, you know, they would learn the number of neurons of the neural networks and
*  and learn how many neurons it has, it would learn the hyper parameters, it would learn
*  the entire neural network, and we'd do this online. And that to me was like, we just need to keep
*  scaling this, it's parallel. So I believed in going, essentially going, being enamored by
*  mathematics, being enamored by this idea that you could just scale it easily, by having more compute.
*  And Dan took me away from the gradient approach, which is the one that has succeeded now.
*  So far.
*  So far. I might still be wrong on this. But it's clearly the case that if you and it's interesting
*  that I bring this sort of the sort of being enamored by mathematics or the surface asymptotic
*  computation, as opposed to sort of finite resources and making trade offs. Because clearly those things
*  have been useful to me, you know, throughout the you know, I still use mathematics to derive some of
*  the meta learning algorithm. So these tools are extremely useful in my thinking and so on.
*  And likewise, thinking about sort of scale and how algorithms do asymptotically is useful.
*  You want them to be at least sublinear and so on in any resource communication or storage or
*  computation. But what I wasn't thinking about was like, what are the finite resources that we have,
*  you know, that there's some very practical limits as to what we can do. And that I should be designing
*  guided by those practical limits. And instead of trying to go with the thing that's fancy,
*  and think of the future and all that, sometimes it's good to just pick the one that you really
*  know works. Work a little on making it better. Oh, okay. Well, Nando, thank you for taking the time.
*  I know time is always short for busy and successful people. Why do you have to be
*  so successful and busy? Why can't we talk for another hour? But anyway,
*  thanks for being on the show. I really appreciate it. Thank you so much. I really enjoyed this
*  opportunity.
*  Advertisements like you hear on other shows. To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year. Find them at thenewyear.net. Thanks for your support. See you next time.
*  you

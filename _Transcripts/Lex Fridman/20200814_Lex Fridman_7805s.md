---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 7805s
Video Keywords: ['dileep george', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 114839
Video Rating: None
---

# Dileep George: Brain-Inspired AI | Lex Fridman Podcast #115
**Lex Fridman:** [August 14, 2020](https://www.youtube.com/watch?v=tg_m_LxxRwM)
*  The following is a conversation with Dalip George, a researcher at the intersection of
*  neuroscience and artificial intelligence, co-founder of Vicarious with Scott Phoenix,
*  and formerly co-founder of Numenta with Jeff Hawkins, who's been on this podcast, and Donna
*  Dubinsky. From his early work on hierarchical temporal memory to recursive cortical networks
*  to today, Dalip's always sought to engineer intelligence that is closely inspired by the
*  human brain. As a side note, I think we understand very little about the fundamental principles
*  underlying the function of the human brain, but the little we do know gives hints that may be more
*  useful for engineering intelligence than any idea in mathematics, computer science, physics, and
*  scientific fields outside of biology. And so the brain is a kind of existence proof that says
*  it's possible. Keep at it. I should also say that brain inspired AI is often over-hyped,
*  and use this fodder, just this quantum computing, for a marketing speak. But I'm not afraid of
*  exploring these sometimes over-hyped areas since where there's smoke, there's sometimes fire.
*  Quick summary of the ads. Three sponsors, Babbel, Raycon Earbuds, and Masterclass. Please consider
*  supporting this podcast by clicking the special links in the description to get the discount.
*  It really is the best way to support this podcast. If you enjoy this thing, subscribe on YouTube,
*  review the Five Stars on Apple Podcast, support on Patreon, or connect with me on Twitter at Lex
*  Friedman. As usual, I'll do a few minutes of ads now, and never any ads in the middle that can
*  break the flow of the conversation. This show is sponsored by Babbel, an app and website that gets
*  you speaking in a new language within weeks. Go to babbel.com and use code Lex to get three months
*  free. They offer 14 languages, including Spanish, French, Italian, German, and yes, Russian. Daily
*  lessons are 10 to 15 minutes, super easy, effective, designed by over 100 language experts.
*  Let me read a few lines from the Russian poem, Noch Ulitsa Fanar Abteka by Alexander Block,
*  that you'll start to understand if you sign up to Babbel.
*  Now, I say that you'll only start to understand this poem because Russian starts with the language
*  and ends with the vodka. Now, the latter part is definitely not endorsed or provided by Babbel,
*  and will probably lose me the sponsorship. But once you graduate from Babbel, you can enroll
*  my advanced course of late night Russian conversation over vodka. I have not yet developed an app for
*  that. It's in progress. So get started by visiting babbel.com and use code Lex to get three months
*  free. This show is sponsored by Raycon Earbuds. Get them at buyraycon.com slash Lex. They become
*  my main method of listening to podcasts, audiobooks, and music when I run, do push-ups
*  and pull-ups, or just living life. In fact, I often listen to brown noise with them when I'm
*  thinking deeply about something, it helps me focus. They're super comfortable, pair easily,
*  great sound, great bass, six hours of playtime. I've been putting in a lot of miles to get ready
*  for a potential ultra marathon and listening to audiobooks on World War II. The sound is rich
*  and really comes in clear. So again, get them at buyraycon.com slash Lex. This show is sponsored
*  by Masterclass. Sign up at masterclass.com slash Lex to get a discount and to support this podcast.
*  When I first heard about Masterclass, I thought it was too good to be true. I still think it's
*  too good to be true. For 180 bucks a year, you get an all-access pass to watch courses from,
*  to list some of my favorites. Chris Hatfield on space exploration, Neil deGrasse Tyson on
*  scientific thinking and communication, Will Wright, creator of SimCity and Sims on game design.
*  Every time I do this read, I really want to play a city builder game. Carlos Santana on guitar,
*  Garry Kasparov on chess, Daniel Nagrano on poker and many more. Chris Hatfield explaining how
*  rockets work and the experience of being launched into space alone is worth the money. By the way,
*  you can watch it on basically any device. Once again, sign up at masterclass.com to get a discount
*  and to support this podcast. And now here's my conversation with Dalip George. Do you think we
*  need to understand the brain in order to build it? Yes. If you want to build the brain, we
*  definitely need to understand how it works. So Blue Brain or Henry Markram's project
*  is trying to build a brain without understanding it, just trying to put details of the brain
*  from neuroscience experiments into a giant simulation by putting more and more neurons,
*  more and more details. But that is not going to work because when it doesn't perform as
*  what you expect it to do, then what do you do? You just keep adding more details. How do you debug
*  it? So unless you understand, unless you have a theory about how the system is supposed to work,
*  how the pieces are supposed to fit together, what they're going to contribute, you can't build it.
*  At the functional level, understand. So can you actually linger on and describe the Blue Brain
*  project? It's kind of a fascinating principle and idea to try to simulate the brain. We're talking
*  about the human brain, right? Right. Human brains and rat brains or cat brains have lots in common.
*  That the neocortex structure is very similar. So initially they were trying to just simulate a
*  cat brain. To understand the nature of evil. To understand the nature of evil. Or as it happens
*  in most of these simulations, you easily get one thing out, which is oscillations. Yeah, if you
*  simulate a large number of neurons, they oscillate. And you can adjust the parameters and say that,
*  oh oscillations match the rhythm that we see in the brain, et cetera. But-
*  Oh, I see. So the idea is, is the simulation at the level of individual neurons?
*  Yeah. So the Blue Brain project, the original idea as proposed was, you put very detailed
*  biophysical models of neurons and you interconnect them according to the statistics of connections
*  that we have found from real neuroscience experiments. And then turn it on and see what
*  happens. And these neural models are incredibly complicated in themselves, right? Because these
*  neurons are modeled using this idea called Hodgkin-Huxley models, which are about how
*  signals propagate in a cable. And there are active dendrites, all those phenomena, which
*  those phenomena themselves we don't understand that well. And then we put in connectivity,
*  which is part guesswork, part observed. And of course, if you do not have any theory about how
*  it is supposed to work, we just have to take whatever comes out of it as, okay,
*  this is something interesting. But in your sense, like these models of the way signal travels
*  like with axons and all the basic models, they're too crude. Oh, well, actually they are pretty
*  detailed and pretty sophisticated. And they do replicate the neural dynamics. If you take a
*  single neuron and you try to turn on the different channels, the calcium channels and
*  the different receptors and see what the effect of turning on or off those channels are in the
*  neurons spike output, people have built pretty sophisticated models of that. And they are,
*  I would say, in the regime of correct. Well, see the correctness, that's interesting,
*  because you mentioned at several levels, the correctness is measured by looking at some kind
*  of aggregate statistics. It would be more the spiking dynamics of a signal. Spiking dynamics of
*  a signal. Yeah. And yeah, these models, because they are going to the level of mechanism, right?
*  So they are basically looking at, okay, what is the effect of turning on an ion channel?
*  And you can model that using electric circuits. So it is not just a function fitting, people are
*  looking at the mechanism underlying it and putting that in terms of electric circuit
*  theory, signal propagation theory and modeling that. And so those models are sophisticated,
*  but getting a single neurons model 99% right does not still tell you how to,
*  it would be the analog of getting a transistor model right and now trying to build a microprocessor.
*  And if you did not understand how a microprocessor works, but you say, oh, I now can model one
*  transistor well, and now I will just try to interconnect the transistors according to whatever
*  I could guess from the experiments and try to simulate it, then it is very unlikely that you
*  will produce a functioning microprocessor. When you want to produce a functioning microprocessor,
*  you want to understand Boolean logic, how do the gates work, all those things, and then understand
*  how do those gates get implemented using transistors. Yeah, there is actually, I remember,
*  this reminds me, there is a paper, maybe you are familiar with it, that I remember going through
*  in a reading group that approaches a microprocessor from a perspective of a neuroscientist. I think
*  it basically, it uses all the tools that we have of neuroscience to try to understand, like as if we
*  aliens showed up to study computers and to see if those tools could be used to get any kind of sense
*  of how the microprocessor works. I think the final takeaway from at least this initial exploration is
*  that we are screwed. There is no way that the tools in neuroscience would be able to get us
*  to anything, not even Boolean logic. It is just any aspect of the architecture of the
*  function of the processes involved, the clocks, the timing, all that, you cannot figure that out
*  from the tools of neuroscience. Yes, I am very familiar with this particular paper. I think it
*  was called, Can a Neuroscientist Understand a Microprocessor? or something like that.
*  Following the methodology in that paper, even electrical engineers would not understand
*  microprocessors. I do not think it is that bad in the sense of saying, neuroscientists do find
*  valuable things by observing the brain. They do find good insights, but those insights cannot be
*  put together just as a simulation. You have to investigate what are the computational underpinnings
*  of those findings. How do all of them fit together from an information processing perspective?
*  You have to painstakingly put those things together and build hypotheses.
*  I do not want to disall of neuroscientists saying, oh, they are not finding anything.
*  That paper almost went to that level of neuroscientists will never understand.
*  That is not true. I think they do find lots of useful things, but it has to be put together in
*  a computational framework. Yes, but just the AI systems will be listening to this podcast
*  a hundred years from now and they will probably, there is some non-zero probability they will find
*  your words laughable. It is like, I remember humans thought they understood something about
*  the brain that are totally clueless. There is a sense about neuroscience that we may be in the very,
*  very early days of understanding the brain. That is one perspective. In your perspective,
*  how far are we into understanding any aspect of the brain? The dynamics of the individual neuron
*  communication to how in a collective sense, how they are able to store information, transfer
*  information, how intelligence then emerges, all that kind of stuff. Where are we on that timeline?
*  Yes. Timelines are very, very hard to predict and you can of course be wrong.
*  You can be wrong on either side. We know that when we look back, the first flight was in 1903.
*  In 1900, there was a New York Times article on flying machines that do not fly.
*  And, you know, humans might not fly for another hundred years. That was what that article stated.
*  But no, they flew three years after that. So it is very hard to...
*  And on that point, one of the Wright brothers, I think two years before, said that, like he said,
*  some number, like 50 years, he has become convinced that it is impossible.
*  Even during their experimentation? Yeah.
*  I mean, that is the entrepreneurial battle of depression, of going through just thinking
*  that this is impossible. But yeah, there is something, even the person that is in it
*  is not able to see, estimate correctly. Exactly. But I can tell from the point of,
*  objectively, what are the things that we know about the brain and how that can be used to build
*  AI models, which can then go back and inform how the brain works. So my way of understanding
*  the brain would be to basically say, look at the insights neuroscientists have found, understand that
*  from a computational angle, information processing angle, build models using that,
*  and then building that model, which functions, which is a functional model, which is doing the
*  task that we want the model to do. It is not just trying to model a phenomena in the brain. It is
*  trying to do what the brain is trying to do on the whole functional level. And building that model
*  will help you fill in the missing pieces that biology just gives you the hints. And building
*  the model fills in the rest of the pieces of the puzzle. And then you can go and connect that back
*  to biology and say, okay, now it makes sense that this part of the brain is doing this, or this layer
*  in the cortical circuit is doing this. And then continue this iteratively, because now that will
*  inform new experiments in neuroscience. And of course, building the model and verifying that in
*  the real world will also tell you more about does the model actually work? And you can refine the
*  model, find better ways of putting these neuroscience insights together. So I would say,
*  neuroscientists alone, just from experimentation, will not be able to build a model of the brain,
*  or a functional model of the brain. So there's lots of efforts, which are very impressive efforts
*  in collecting more and more connectivity data from the brain. How are the microcircuits of the
*  brain connected with each other? Those are beautiful, by the way.
*  Those are beautiful. And at the same time, those do not itself, by themselves,
*  convey the story of how does it work? And somebody has to understand, okay, why are they connected
*  like that? And what are those things doing? And we do that by building models in AI,
*  using hints from neuroscience, and repeat the cycle.
*  So what aspect of the brain are useful in this whole endeavor? Which, by the way, I should say,
*  you're both a neuroscientist and an AI person. I guess the dream is to both understand the brain
*  and to build AGI systems. So it's like an engineer's perspective of trying to understand
*  the brain. So what aspects of the brain, functionally speaking, like you said, do you find interesting?
*  Yeah, quite a lot of things. So one is, if you look at the visual cortex,
*  visual cortex is a large part of the brain. I forget the exact fraction, but it's a huge part
*  of our brain area is occupied by just vision. So visual cortex is not just a feedforward cascade
*  of neurons. There are a lot more feedback connections in the brain compared to the
*  feedforward connections. And it is surprising to the level of detail neuroscientists have
*  actually studied this. If you go into neuroscience literature and poke around and ask, have they
*  studied what will be the effect of poking a neuron in level IT in level V1? And
*  have they studied that? And you will say, yes, they have studied that.
*  Every possible combination.
*  It's not a random exploration at all. It's very hypothesis driven. Experimental neuroscientists
*  are very, very systematic in how they probe the brain because experiments are very costly to
*  conduct. They take a lot of preparation. They need a lot of control. So they are very hypothesis
*  driven in how they probe the brain. And often what I find is that when we have a question in
*  AI about, has anybody probed how lateral connections in the brain works? And when you go and read the
*  literature, yes, people have probed it and people have probed it very systematically.
*  And they have hypothesis about how those lateral connections are supposedly contributing
*  to visual processing. But of course, they haven't built very, very functional detailed models of it.
*  By the way, how do the studies, sorry to interrupt, do they stimulate like a neuron
*  in one particular area of the visual cortex and then see how the signal travels kind of thing?
*  Very, very fascinating experiments. So I can give you one example I was impressed with.
*  So before going to that, let me give you an overview of how the layers in the cortex are
*  organized. Visual cortex is organized into roughly four hierarchical levels. So V1, V2, V4, IT.
*  What happened to V3?
*  Well, yeah, there's another pathway. Okay, so I'm talking about just object recognition pathway.
*  All right, cool.
*  And then in V1 itself, there is a very detailed microcircuit in V1 itself. There is organization
*  within a level itself. The cortical sheet is organized into multiple layers and there are
*  columnar structures. And this layer-wise and columnar structure is repeated in V1, V2, V4,
*  IT, all of them. And the connections between these layers within a level, in V1 itself,
*  there are six layers roughly, and the connections between them, there is a particular structure to
*  them. And now, so one example of an experiment people did is when you present a stimulus,
*  which is, let's say, requires separating the foreground from the background of an object.
*  So it's a textured triangle on a textured background. And you can check,
*  does the surface settle first or does the contour settle first?
*  Settle?
*  Settle in the sense that when you finally form the percept of the triangle, you understand where
*  the contours of the triangle are and you also know where the inside of the triangle is, right?
*  That's when you form the final percept. Now, you can ask, what is the dynamics of forming that
*  final percept? Do the neurons first find the edges and converge on where the edges are and then they
*  find the inner surfaces or does it go the other way around?
*  The other way around. So what's the answer?
*  In this case, it turns out that it first settles on the edges, it converges on the edge hypothesis
*  first, and then the surfaces are filled in from the edges to the inside.
*  That's fascinating.
*  And the detail to which you can study this, it's amazing that you can actually not only find
*  the temporal dynamics of when this happens, and then you can also find which layer in V1,
*  which layer is encoding the edges, which layer is encoding the surfaces, and which layer is
*  encoding the feedback, which layer is encoding the feed forward, and what's the combination of
*  them that produces the final person. And these kinds of experiments stand out when you try to
*  explain illusions. One example of a favorite illusion of mine is the Kinesa triangle. I don't
*  know that you are familiar with this one. So this is an example where it's a triangle, but
*  the corners of the triangle are shown in the stimulus. So they look like kind of Pac-Man.
*  Oh, the black Pac-Man.
*  Exactly. And then your visual system hallucinates the edges. And when you look at it, you will see
*  a faint edge. And you can go inside the brain and look, do actually neurons signal the presence of
*  this edge. And if they signal, how do they do it? Because they are not receiving anything from the
*  input. The input is black for those neurons. So how do they signal it? When does the signaling
*  happen? So if a real contour is present in the input, then the neurons immediately signal,
*  oh, okay, there is an edge here. When it is an illusory edge, it is clearly not in the input.
*  It is coming from the context. So those neurons fire later. And you can say that, okay, these are
*  it's the feedback connections that is causing them to fire. And they happen later. And you can
*  find the dynamics of them. So these studies are pretty impressive and very detailed.
*  So by the way, just to step back, you said that there may be more feedback connections
*  than feed forward connections. First of all, if it's just for like a machine learning folks,
*  I mean, that's crazy that there's all these feedback connections. We often think about,
*  thanks to deep learning, you start to think about the human brain as a kind of feed forward
*  mechanism. So what the heck are these feedback connections? What's the dynamics? What are we
*  supposed to think about them? Yeah. So this fits into a very beautiful picture about how the brain
*  works. So the beautiful picture of how the brain works is that our brain is building a model of the
*  world. So our visual system is building a model of how objects behave in the world. And we are
*  constantly projecting that model back onto the world. So what we are seeing is not just a
*  feed forward thing that just gets interpreted in a feed forward part. We are constantly projecting
*  our expectations onto the world. And what the final percept is a combination of what we project
*  onto the world combined with what the actual sensory input is. Almost like trying to calculate
*  the difference and then trying to interpret the difference. Yeah. I wouldn't put it as
*  calculating the difference. It's more like what is the best explanation for the input stimulus
*  based on the model of the world I have. Got it. Got it. And that's where all the illusions come in.
*  But that's an incredibly efficient process. So the feedback mechanism, it just helps you
*  constantly hallucinate how the world should be based on your world model and then just looking
*  at if there's novelty, like trying to explain it. Yeah. Hence, that's why movement,
*  we detect movement really well. There's all these kinds of things. And this is like at all different
*  levels of the cortex you're saying. This happens at the lowest level, the highest level. Yes.
*  Yeah. In fact, feedback connections are more prevalent everywhere in the cortex. And so one
*  way to think about it, and there's a lot of evidence for this, is inference. So basically,
*  if you have a model of the world and when some evidence comes in, what you are doing is inference.
*  You are trying to now explain this evidence using your model of the world. And this inference
*  includes projecting your model onto the evidence and taking the evidence back into the model and
*  doing an iterative procedure. And this iterative procedure is what happens using the feed forward,
*  feedback propagation. And feedback affects what you see in the world and it also affects feed
*  forward propagation. And examples are everywhere. We see these kinds of things everywhere. The idea
*  that there can be multiple competing hypothesis in our model trying to explain the same evidence.
*  And then you have to make them compete. And one hypothesis will explain away the other hypothesis
*  through this competition process. Wait, what? So you have competing models of the world
*  that try to explain. What do you mean by explain away? So this is a classic example in
*  graphical models, probabilistic models. What are those? Okay.
*  I think it's useful to mention because we'll talk about them more.
*  Neural networks are one class of machine learning models. You have a distributed set of
*  nodes, which are called the neurons. Each one is doing a dot product and you can
*  approximate any function using this multilevel network of neurons. So that's a class of models
*  which are useful for function approximation. There is another class of models in machine learning
*  called probabilistic graphical models. And you can think of them as each node in that
*  model is variable, which is talking about something. It can be a variable representing
*  is an edge present in the input or not. And at the top of the network, a node can be representing
*  is there an object present in the world or not. So it is another way of encoding knowledge.
*  And then once you encode the knowledge, you can do inference in the right way. What is the best way to
*  explain some set of evidence using this model that you encoded? So when you encode the model,
*  you are encoding the relationship between these different variables. How is the edge connected to
*  the model of the object? How is the surface connected to the model of the object?
*  And then, of course, this is a very distributed complicated model. And inference is how do you
*  explain a piece of evidence when a set of stimulus comes in? If somebody tells me there is a
*  50% probability that there is an edge here in this part of the model, how does that affect my belief
*  on whether I should think that there is a square present in the image? So this is the process of
*  inference. So one example of inference is having this experience of effect between multiple causes.
*  So graphical models can be used to represent causality in the world. So let's say your alarm
*  at home can be triggered by a burglar getting into your house, or it can be triggered by an earthquake.
*  Both can be causes of the alarm going off. So now you're in your office, you heard burglar alarm
*  going off, you are heading home, thinking that there's a burglar got in. But while driving home,
*  if you hear on the radio that there was an earthquake in the vicinity, now your strength
*  of evidence for a burglar getting into their house is diminished. Because now that piece of evidence
*  is explained by the earthquake being present. So if you think about these two causes explaining
*  at lower level variable, which is alarm. Now, what we're seeing is that increasing the evidence for
*  some cause, there is evidence coming in from below for alarm being present. And initially it was flowing
*  to a burglar being present. But now, since there is side evidence for this other cause,
*  it explains away this evidence and evidence will now flow to the other cause. This is two competing
*  causal things trying to explain the same evidence. And the brain has a similar kind of mechanism
*  for doing so. That's kind of interesting. How's that all encoded in the brain? Where's the storage
*  of information? Are we talking just maybe to get it a little bit more specific? Is it in the hardware
*  of the actual connections? Is it in chemical communication? Is it electrical communication?
*  So this is a paper that we are bringing out soon. This is the cortical microcircuits paper
*  that I sent you a draft of. Of course, a lot of it is still hypothesis. One hypothesis is that
*  you can think of a cortical column as encoding a concept. Think of it as a
*  an example of a concept is an edge present or not, or is an object present or not.
*  You can think of it as a binary variable, a binary random variable, the presence of an edge or not,
*  or the presence of an object or not. So each cortical column can be thought of as representing
*  that one concept, one variable. And then the connections between these cortical columns
*  are basically encoding the relationship between these random variables.
*  And then there are connections within the cortical column. Each cortical column is implemented using
*  multiple layers of neurons with very, very, very rich structure there. There are thousands of
*  neurons in a cortical column. But that structure is similar across the different cortical columns.
*  Correct. And also these cortical columns connect to a substructure called thalamus.
*  So all cortical columns pass through this substructure. So our hypothesis is that
*  the connections between the cortical columns implement this. That's where the knowledge is
*  stored about how these different concepts connect to each other. And then the neurons inside this
*  cortical column and in thalamus in combination implement these actual computations in there for
*  inference, which includes explaining away and competing between the different hypothesis.
*  So what is amazing is that neuroscientists have actually done experiments to the tune of showing
*  these things. They might not be putting it in the overall inference framework, but they will show
*  things like if I poke this higher level neuron, it will inhibit through this complicated loop
*  through the thalamus, it will inhibit this other column. So they will do such experiments.
*  But do they use terminology of concepts, for example? Is it something where it's easy to
*  anthropomorphize and think about concepts like you start moving into logic-based reasoning systems?
*  So how would you think of concepts in that kind of way? Or is it a lot messier, a lot more gray
*  area, even more gray, even more messy than the artificial neural network kinds of abstractions?
*  It's the easiest way to think of it as a variable. It's a binary variable,
*  which is showing the presence or absence of something.
*  But I guess what I'm asking is, is that something that we're supposed to think of,
*  something that's human interpretable? It doesn't need to be. It doesn't need to
*  be human interpretable. There's no need for it to be human interpretable. But it's almost like
*  you will be able to find some interpretation of it because it is connected to the other things.
*  Yeah. And the point is it's useful somehow. It's useful as an entity in the graph,
*  in connecting to the other entities that are, let's call them concepts.
*  Okay. So by the way, are these the cortical microcircuits?
*  Correct. These are the cortical microcircuits. That's what neuroscientists use to talk about
*  the circuits within a level of the cortex. So you can think of, let's think of a neural
*  network, artificial neural network terms. People talk about the architecture of the,
*  so how many layers they build, what is the fan in, fan out, et cetera. That is the macro architecture.
*  And then within a layer of the neural network, the cortical neural network is much more structured
*  within a level. There's a lot more intricate structure there. But even within an artificial
*  neural network, you can think of feature detection plus pooling as one level. And so that is kind of
*  a microcircuit. It's much more complex in the real brain. And so within a level, whatever is
*  that circuitry within a column of the cortex and between the layers of the cortex, that's the
*  microcircuitry. I love that terminology. Machine learning people don't use the circuit terminology,
*  but they should. That's nice. So that's the cortical microcircuit. So what's interesting about,
*  what can we say? What is the paper that you're working on propose about the ideas around these
*  cortical microcircuits? So this is a fully functional model for the microcircuits of the
*  visual cortex. So the paper focuses on your idea in our discussion now is focusing on vision.
*  The visual cortex. Okay. This is a model. This is a full model. This is how vision works.
*  But this is a model of- A hypothesis.
*  Okay. So let me step back a bit. So we looked at neuroscience for insights on how to build a vision
*  model. And we synthesized all those insights into a computational model. This is called the recursive
*  cortical network model that we used for breaking captures. And we are using the same model for
*  robotic picking and tracking of objects. And that again is a vision system.
*  That's a vision system. Computer vision system.
*  That's a computer vision system.
*  Takes in images and outputs what? On one side, it outputs the class of the image
*  and also segments the image. And you can also ask it further queries. Where is the edge of the object?
*  Where is the interior of the object? So it's a model that you build to answer multiple questions.
*  So you're not trying to build a model for just classification or just segmentation,
*  etc. It's a joint model that can do multiple things. So that's the model that we built
*  using insights from neuroscience. And some of those insights are what is the role of
*  feedback connections? What is the role of lateral connections? So all those things
*  went into the model. The model actually uses feedback connections.
*  All these ideas from your science. So what the heck is a recursive cortical network? What are
*  the architecture approaches? Interesting aspects here, which is essentially a brain inspired
*  approach to computer vision. Yeah. So there are multiple layers to this question.
*  I can go from the very, very top and then zoom in. Okay. So one important thing,
*  constraint that went into the model is that you should not think of vision as something
*  in isolation. We should not think perception as something as a pre-processor for cognition.
*  Perception and cognition are interconnected. And so you should not think of one problem in
*  separation from the other problem. And so that means if you finally want to have a system that
*  understands concepts about the world and can learn a very conceptual model of the world and
*  can reason and connect to language, all of those things, you need to think all the way through
*  and make sure that your perception system is compatible with your cognition system and language
*  system and all of them. And one aspect of that is top-down controllability. What does that mean?
*  So that means, so think of, you can close your eyes and think about the details of one object.
*  I can zoom in further and further. So think of the bottle in front of me. And now you can think
*  about, okay, what the cap of that bottle looks. You can think about what's the texture on that
*  bottle of the cap. You can think about what will happen if something hits that. So you can
*  manipulate your visual knowledge in cognition-driven ways. And so this top-down controllability
*  and being able to simulate scenarios in the world. So you're not just a passive
*  player in this perception game. You can control it. You have imagination. Correct.
*  So basically, having a generative network, which is a model, and it is not just some arbitrary
*  generated network. It has to be built in a way that it is controllable top-down. It is not just
*  trying to generate a whole picture at once. It's not trying to generate photorealistic things of
*  the world. You don't have good photorealistic models of the world. Human brains do not have.
*  If I, for example, ask you the question, what is the color of the letter E in the Google logo?
*  You have no idea. Although you have seen it millions of times, or not millions of times,
*  hundreds of times. So our model is not photorealistic, but it has other properties
*  that we can manipulate it. And you can think about filling in a different color in that logo.
*  You can think about expanding the letter E. So you can imagine the consequence of
*  actions that you have never performed. So these are the kind of characteristics the
*  generative model need to have. So this is one constraint that went into our model.
*  When you read just the perception side of the paper, it is not obvious that this was a constraint
*  that went into the model. This top-down controllability of the generative model.
*  What does top-down controllability in a model look like? It's a really interesting concept,
*  fascinating concept. Is that the recursiveness that gives you that?
*  Quite a few things. What does the model factorize? What is the model representing as
*  different pieces in the puzzle? In the RCN network, it thinks of the world. The background
*  of an image is modeled separately from the foreground of the image. So the objects are
*  separate from the background. They are different entities.
*  So there's a kind of segmentation that's built in fundamentally.
*  And then even that object is composed of parts. And another one is the shape of the object
*  is differently modeled from the texture of the object.
*  Got it. So there's like these... You know who Francois Cholet is?
*  So he developed this IQ test type of thing for ARC challenge. And it's kind of cool that there's
*  these concepts, priors that he defines that you bring to the table in order to be able to reason
*  about basic shapes and things in IQ tests. So here you're making it quite explicit that
*  here are the things that you should be... These are like distinct things that you should be able to
*  model in this. Keep in mind that you can derive these from much more general principles.
*  You don't need to explicitly put it as objects versus foreground versus background,
*  the surface versus texture. No, these are these are derivable from more fundamental principles of
*  what's the property of continuity of natural signals.
*  What's the property of continuity of natural signals? By the way, that sounds very poetic.
*  But yeah, so you're saying that there's some low level properties from which emerges the idea that
*  shapes should be different than... There should be a parts of an object. There should be...
*  Exactly. Kind of like Francois talked, there's objectness. There's all these things that
*  it's kind of crazy that we humans evolved to have because it's useful for us to perceive the world.
*  Correct. And it derives mostly from the properties of natural signals.
*  And so... Natural signals. So natural signals are the kind of things we'll perceive in the
*  natural world. I don't know why that sounds so beautiful. Natural signals, yeah.
*  As opposed to a QR code, which is an artificial signal that we created,
*  humans are not very good at classifying QR codes. We are very good at saying something is a cat or
*  a dog, but not very good at classifying... Computers are very good at classifying QR codes.
*  So our visual system is tuned for natural signals. And there are fundamental assumptions
*  in the architecture that are derived from natural signals properties.
*  I wonder when you take hallucinogenic drugs, does that go into natural or is that closer to the QR
*  code? It's still natural.
*  It's still natural? Yeah, because it is still operating using our brains.
*  By the way, on that topic, I haven't been following... I think they're becoming legalized
*  I can't wait until they become legalized to a degree that vision scientists, researchers
*  could study it. Just like through medical, chemical ways, modify it. There could be ethical
*  concerns, but that's another way to study the brain is to be able to chemically modify it.
*  There's probably a very long way to figure out how to do it ethically.
*  I think there are studies on that already. I think so. It's not unethical to give it to rats.
*  Oh, that's true. There's a lot of drugged up rats out there. Okay, cool. Sorry.
*  So there's these low level things from natural signals that...
*  ...from which these properties will emerge. But it is still a very hard problem on how to encode
*  that. You mentioned the priors Franchot wanted to encode in the abstract reasoning challenge,
*  but it is not straightforward how to encode those priors. So some of those challenges,
*  the completion challenges are things that we purely use our visual system to do. It looks
*  like abstract reasoning, but it is purely an output of the vision system. For example,
*  completing the corners of that Kanisa triangle, completing the lines of that Kanisa triangle.
*  It's a purely visual system property. There is no abstract reasoning involved. It uses all these
*  priors, but it is stored in our visual system in a particular way that is amenable to inference.
*  That is one of the things that we tackled. It's basically saying, okay, these are the prior
*  knowledge which will be derived from the world. But then how is that prior knowledge represented
*  in the model such that inference, when some piece of evidence comes in, can be done very
*  efficiently and in a very distributed way. Because there are so many ways of representing knowledge,
*  which is not amenable to very quick inference, quick lookups. That's one
*  core part of what we tackled in the RCN model. How do you encode visual knowledge to
*  do very quick inference? Can you maybe comment on, so folks listening to this in general may be
*  familiar with different kinds of architectures of neural networks. What are we talking about with
*  RCN? What does the architecture look like? What are the different components? Is it close to
*  neural networks? Is it far away from neural networks? What does it look like? Yeah. You can
*  think of the delta between the model and a convolutional neural network, if people are
*  familiar with convolutional neural networks. Convolutional neural networks have this
*  feed-forward processing cascade, which is called feature detectors and pooling. That is repeated
*  in a multi-level system. If you want an intuitive idea of what is happening, feature detectors are
*  detecting interesting co-occurrences in the input. It can be a line, a corner, an eye,
*  or a piece of texture, et cetera. The pooling neurons are doing some local transformation
*  of that and making it invariant to local transformations. This is what the structure
*  of convolutional neural network is. Recursive cortical network has a similar structure when
*  you look at just the feed-forward pathway. In addition to that, it is also structured in a way
*  that it is generative so that it can run it backward and combine the forward with the backward.
*  Another aspect that it has is it has lateral connections.
*  This lateral connection, if you have an edge here and an edge here, it has connections between
*  these edges. It is not just feed-forward connections. It is something between these
*  edges, which is the nodes representing these edges, which is to enforce compatibility between them.
*  Otherwise, what will happen is that- Constraints?
*  It is a constraint. If you do just feature detection followed by pooling, then your
*  transformations in different parts of the visual field are not coordinated. When you generate from
*  the model, you will create jagged things and uncoordinated transformations. These lateral
*  connections are enforcing the transformations. Is the whole thing still differentiable?
*  No. It is not trained using a back prop.
*  That is really important. There is this feed-forward, there is feedback mechanisms,
*  there are some interesting connectivity things. It is still layered?
*  Yes, there are multiple layers.
*  Multiple layers. Very interesting. The interconnection between adjacent connections
*  across service constraints that keep the thing stable.
*  What else?
*  Then there is this idea of doing inference. A neural network does not do inference on the fly.
*  An example of why this inference is important is, one of the first applications that we showed in
*  the paper was to crack text-based captures. What are captures, by the way?
*  By the way, one of the most awesome. People do not use this term anymore. It is human computation,
*  I think. I love this term. The guy who created CAPTCHAs came up with this term. I love it.
*  What are CAPTCHAs?
*  CAPTCHAs are those strings that you fill in. If you are opening a new account in Google,
*  they show you a picture. It used to be a set of garbled letters that you have to figure out
*  what is the string of characters and type it. The reason CAPTCHAs exist is because Google or Twitter
*  do not want automatic creation of accounts. You can use a computer to create millions of accounts
*  and use that for nefarious purposes. You want to make sure that, to the extent possible,
*  the interaction that their system is having is with a human. It is called a human interaction
*  proof. A CAPTCHA is a human interaction proof. CAPTCHAs are, by design, things that are easy for
*  humans to solve, but hard for computers. Hard for robots, yeah.
*  Text-based CAPTCHAs was the one which was prevalent around 2014 because, at that time,
*  text-based CAPTCHAs were hard for computers to crack. Even now, they are actually, in the sense of,
*  an arbitrary text-based CAPTCHA will be unsolvable even now. But with the techniques that we have
*  developed, you can quickly develop a mechanism that solves the CAPTCHA. They've probably gotten
*  a lot harder too. They've been getting clever and clever at generating these text CAPTCHAs.
*  That was one of the things you've tested on, is these kinds of CAPTCHAs in 2014, 15, that kind of
*  stuff. By the way, why CAPTCHAs? Yeah. Even now, I would say CAPTCHA is a very, very good challenge
*  problem if you want to understand how human perception works and if you want to build
*  systems that work like the human brain. I wouldn't say CAPTCHA is a solved problem. We have cracked
*  the fundamental difference of CAPTCHAs, but it is not solved in the way that humans solve it.
*  So, I can give you an example. I can take a five-year-old child who has just learned characters
*  and show them any new CAPTCHA that we create. They will be able to solve it. I can show you
*  pretty much any new CAPTCHA from any new website. You'll be able to solve it without getting any
*  training examples from that particular style of CAPTCHA. You're assuming I'm human, yeah.
*  Yes, yeah. That's right. So, if you are human, otherwise I will be able to figure that out
*  using this one. This whole podcast is just a touring test, a long touring test. Anyway,
*  I'm sorry. So, yeah. So, humans can figure it out with very few examples.
*  Or no training examples. No training examples from that particular style of CAPTCHA.
*  And so, even now this is unreachable for the current deep learning system. So, basically,
*  there is no... I don't think a system exists where you can basically say,
*  train on whatever you want. And then now say, hey, I will show you a new CAPTCHA,
*  which I did not show you in the training setup. Will the system be able to solve it?
*  It still doesn't exist. So, that is the magic of human perception. And Doug Huffstater
*  put this very beautifully in one of his talks. The central problem in AI is what is the letter A.
*  If you can build a system that reliably can detect all the variations of the letter A,
*  you don't even need to go to the... The B and the C.
*  Yeah. You don't even need to go to the B and the C or the strings of characters.
*  And so, that is the spirit with which we tackle that problem.
*  What does it mean by that? I mean, is it like without training examples, try to figure out
*  the fundamental elements that make up the letter A in all of its forms?
*  In all of its forms. A can be made with two humans standing leaning against each other,
*  holding hands. And it can be made of leaves. It can be...
*  Yeah. You might have to understand everything about this world in order to understand the
*  letter A. Yeah. Exactly.
*  So, it's common sense reasoning, essentially. Yeah.
*  Right. So, to finally to really solve, finally to say that you have solved CAPTCHA,
*  you have to solve the whole problem.
*  No. Yeah. Okay. So, how does this kind of the RCN architecture help us to get a better job,
*  that kind of thing? Yeah. So, as I mentioned,
*  one of the important things was being able to do inference, being able to dynamically do inference.
*  Can you clarify what you mean? Because you said neural networks don't do inference.
*  Yeah. So, what do you mean by inference in this context then?
*  So, okay. So, in CAPTCHAs, what they do to confuse people is to make these characters
*  crowd together. Yes.
*  Okay. And when you make the characters crowd together, what happens is that you will now
*  start seeing combinations of characters as some other new character or an existing character. So,
*  you would put an R and N together, it will start looking like an M. And so locally,
*  there is very strong evidence for it being some incorrect character. But globally,
*  the only explanation that fits together is something that is different from what you find
*  locally. Yes.
*  So, this is inference. You are basically taking local evidence and putting it in the global
*  context and often coming to a conclusion locally, which is conflicting with the local information.
*  So, actually, you mean inference in the way it's used when you talk about reasoning, for example,
*  as opposed to inference with artificial neural networks, which is a single pass to the network.
*  Correct. Okay. So, you're basically doing some basic forms of reasoning, like integration of
*  how local things fit into the global picture. And things like explaining away coming into this
*  one, because you are explaining that piece of evidence as something else, because globally,
*  that's the only thing that makes sense. So, now, you can amortize this inference by,
*  in a neural network, if you want to do this, you can brute force it. You can just show it all
*  combinations of things that you want your reasoning to work over. And you can just train the help out
*  of that neural network. And it will look like it is doing inference on the fly, but it is really
*  just doing amortized inference. It is because you have shown it a lot of these combinations during
*  training time. So, what you want to do is be able to do dynamic inference rather than just being
*  able to show all those combinations in the training time. And that's something we emphasized in the
*  model. What does it mean, dynamic inference? Is that that has to do with the feedback
*  thing? Yes. What is dynamic? I'm trying to visualize what dynamic inference would be in this
*  case. What is it doing with the input? It's shown the input the first time. What's changing
*  temporally? What's the dynamics of this inference process? So, you can think of it as you have,
*  at the top of the model, the characters that you are trained on, they are the causes. You're
*  trying to explain the pixels using the characters as the causes. The characters are the things that
*  cause the pixels. Yeah. So, there's this causality thing. So, the reason you mentioned causality,
*  I guess, is because there's a temporal aspect to this whole thing. In this particular case,
*  the temporal aspect is not important. It is more like when, if I turn the character on,
*  the pixels will turn on. Yeah, it will be after this a little bit. Okay. So, that is causality
*  in the sense of a larger causality, hence inference. Okay. The dynamics is that even
*  the locally, it will look like, okay, this is an A. And locally, when I look at just that patch of
*  the image, it looks like an A. But when I look at it in the context of all the other causes,
*  A is not something that makes sense. So, that is something you have to recursively figure out.
*  So, okay. And this thing performed pretty well on the captures. Correct. And,
*  I mean, is there some kind of interesting intuition you can provide? Why it did well? Like,
*  what did it look like? Is there visualizations that could be human interpretable to us humans?
*  Yes. Yeah. So, the good thing about the model is that it is extremely, so it is not just doing a
*  classification. It is providing a full explanation for the scene. So, when it operates on a scene,
*  it is coming back and saying, look, this is the part, is the A, and these are the pixels that
*  turned on. These are the pixels in the input that makes me think that it is an A. And also,
*  these are the portions I hallucinated. It provides a complete explanation of that form.
*  And then, these are the contours. This is the interior, and this is in front of this other
*  object. So, that is the kind of explanation the inference network provides. So, that is useful
*  and interpretable. And then, the kind of errors it makes are also, I don't want to
*  read too much into it, but the kind of errors the network makes are very similar to the kinds
*  of errors humans would make in a similar situation. So, there is something about the structure that
*  feels reminiscent of the way human's visual system works. Well, I mean, how hardcoded is this to the
*  capture problem, this idea? Not really hardcoded, because the assumptions, as I mentioned, are
*  general. And those themselves can be applied in many situations, which are natural signals. So,
*  it's the foreground versus background factorization, and the factorization of the surfaces versus the
*  contours. So, these are all generally applicable assumptions. And in all vision. So, why
*  attack the capture problem, which is quite unique in the computer vision context, versus the
*  traditional benchmarks of ImageNet and all those kinds of image classification, or even segmentation
*  tasks, all that kind of stuff? What's your thinking about those kinds of benchmarks in
*  this context? I mean, those benchmarks are useful for deep learning kind of algorithms. So, the
*  settings that deep learning works in are, here is my huge training set, and here is my test set. So,
*  the training set is almost 100x, 1000x bigger than the test set in many cases. What we wanted to do
*  was invert that. The training set is way smaller than the test set. And capture is a problem that
*  is, by definition, hard for computers. And it has these good properties of strong generalizations,
*  out of training distribution generalization. If you are interested in studying that and having
*  your model have that property, then it's a good data set to tackle. So, have you attempted to,
*  which I think I believe there's quite a growing body of work on looking at MNIST and ImageNet
*  without training? So, the basic challenge is what tiny fraction of the training set can we take in
*  order to do a reasonable job of the classification task? Have you explored that angle in these
*  classic benchmarks? Yes. So, we did do MNIST. So, it's not just capture. So, there was also
*  multiple versions of MNIST, including the standard version, where we inverted the problem,
*  which is basically saying rather than train on 60,000 training data, how quickly can you get
*  to high level accuracy with very little training data? Is there some performance you remember?
*  How well did it do? How many examples did it need? Yeah. I remember that it was on the order of
*  tens of hundreds of examples to get into 95% accuracy. And it was definitely better than
*  the systems, other systems out there at that time. At that time. Yeah. Yeah. They're really pushing.
*  I think that's a really interesting space, actually. I think there's an actual name for
*  MNIST that there's different names to the different sizes of training sets. I mean,
*  people are attacking this problem. I think it's super interesting. Yeah. It's funny how the MNIST
*  will probably be with us all the way to AGI. Yes. It's a data set that just sticks by. It's a clean,
*  simple data set to study the fundamentals of learning with. Just like CAPTCHAs, it's interesting.
*  Not enough people. I don't know, maybe you can correct me, but I feel like CAPTCHAs don't show
*  up as often in papers as they probably should. That's correct. Yeah. Because usually these things
*  have a momentum. Once something gets established as a standard benchmark, there is a dynamics of
*  how graduate students operate and how the academic system works that pushes people to track that
*  benchmark. Nobody wants to think outside the box. Okay. So good performance on the CAPTCHAs.
*  What else is there interesting on the RCN side before we talk about the cortical microswitch?
*  Yeah. So the same model. The important part of the model was that it trains very quickly with
*  very little training data. It's quite robust to out of distribution perturbations. We are using that
*  very fruitfully and advocatiously in many of the robotics tasks we are solving.
*  Well, let me ask you this kind of touchy question. I have spoken with your friend,
*  colleague, Jeff Hawkins, too. I have to kind of ask, whenever you have brain inspired stuff
*  and you make big claims, big sexy claims, there's critics, I mean, machine learning subreddit,
*  don't get me started on those people. Criticism is good, but they're a bit over the top.
*  There is quite a bit of sort of skepticism and criticism. Is this work really as good as it
*  promises to be? Do you have thoughts on that kind of skepticism? Do you have comments on the kind
*  of criticism we might have received about, is this approach legit? Is this a promising approach?
*  Or at least as promising as it seems to be advertised as?
*  Yeah, I can comment on it. Our Arsene paper is published in Science, which I would argue is a
*  very high quality journal, very hard to publish in. Usually, it is indicative of the quality of the
*  work. I am very, very certain that the ideas that we brought together in that paper in terms of the
*  importance of feedback connections, recursive inference, lateral connections, coming to best
*  explanation of the scene as the problem to solve, trying to solve recognition, segmentation,
*  all jointly in a way that is compatible with higher level cognition, top down attention,
*  all those ideas that we brought together into something coherent and workable in the world and
*  solving a challenging, tackling a challenging problem. I think that will stay and that
*  contribution I stand by. Now, I can tell you a story which is funny in the context of this.
*  If you read the abstract of the paper and the argument we are putting in, look,
*  current deep learning systems take a lot of training data. They don't use these insights.
*  Here is our new model, which is not a deep neural network. It's a graphical model. It does
*  inference. This is how the paper is. Now, once the paper was accepted and everything,
*  it went to the press department in science, AAAS, science office. We didn't do any press
*  release when it was published. It went to the press department. What was the press release
*  that they wrote up? A new deep learning model. Solves captures. Solves captures. So you can see
*  what was being hyped in that thing. So there is a dynamic in the community of
*  that especially happens when there are lots of new people coming into the field and they get
*  attracted to one thing and some people are trying to think different compared to that.
*  I think skepticism is science is important and it is very much required, but it's also
*  it's not skepticism usually. It's mostly bandwagon effect that is happening rather than-
*  Well, but that's not even that. I'll tell you what they react to, which is like,
*  I'm sensitive to as well. If you look at just companies, OpenAI, DeepMind,
*  Vicarious, I mean, there's a little bit of a race to the top and hype. It's like,
*  it doesn't pay off to be humble. And the press is just irresponsible often. They just, I mean,
*  don't get me started on the state of journalism today. It seems like the people who write articles
*  about these things, they literally have not even spent an hour on the Wikipedia article about what
*  is neural networks. They haven't invested just even the language to laziness. It's like robots
*  beat humans. They write this kind of stuff that just- And then of course the researchers are
*  quite sensitive to that because it gets a lot of attention. They're like, why did this word get so
*  much attention? That's over the top and people get really sensitive. The same kind of
*  criticism with OpenAI did work with Rubik's Cube, with the robot that people criticized.
*  Same with GPT-2 and 3, they criticize. Same thing with DeepMinds with AlphaZero. I'm sensitive to it.
*  And of course, with your work, you mentioned deep learning, but there's something super sexy to the
*  public about brain inspired. I mean, that immediately grabs people's imagination. Not even
*  like neural networks, but like really brain inspired, like brain like neural networks.
*  That seems really compelling to people and to me as well, to the world as a narrative. And so
*  people hook up, hook onto that. And sometimes the skepticism engine turns on in the research
*  community and they're skeptical. But I think putting aside the ideas of the actual performance
*  and captures or performance on any data set, I mean, to me, all these data sets are useless anyway.
*  It's nice to have them, but in the grand scheme of things, they're silly toy examples. The point is,
*  is there intuition about the ideas, just like you mentioned, bringing the ideas together in a unique
*  way. Is there something there? Is there some value there? And is it going to stand the test of time?
*  And that's the hope. That's the hope. My confidence there is very high. I don't treat
*  brain inspired as a marketing term. I am looking into the details of biology and I'm puzzling over
*  those things and I am grappling with those things. And so it is not a marketing term at all.
*  You can use it as a marketing term and people often use it and you can get combined with them.
*  And when people don't understand how we are approaching the problem, it is easy to be
*  misunderstood and think of it as purely marketing. But that's not the way we are.
*  So you really, I mean, as a scientist, you believe that if we kind of just stick to really
*  understanding the brain, that's the right, like you should constantly meditate on the
*  how does the brain do this? Because that's going to be really helpful for engineering
*  intelligent systems. Yes. So I think it's one input and it is helpful, but you should know
*  when to deviate from it too. So an example is convolutional neural networks, right?
*  Yes. Convolution is not an operation brain implements. The visual cortex is not
*  convolutional. The visual cortex has local receptive fields, local connectivity. But
*  there is no translation invariance in the network weights in the visual cortex. That is a
*  computational trick, which is a very good engineering trick that we use for sharing
*  the training between the different nodes. And that trick will be with us for some time. It will go
*  away when we have robots with eyes and heads that move. And so then that trick will go away. It will
*  not be useful at that time. So the brain doesn't have translational invariance.
*  It has the focal point. It has a thing it focuses on. Correct. It has a fovea. And because of the
*  fovea, the receptive fields are not like the copying of the weights. The weights in the
*  center are very different from the weights in the periphery. Yes. I did this, actually wrote a paper
*  and just got an chance to really study peripheral vision, which is a fascinating thing. Very
*  under understood thing of what the brain does at every level. The brain does
*  with the periphery. It does some funky stuff. So it's another kind of trick than convolutional.
*  Convolution in neural networks is a trick for efficiency. It's an efficiency trick.
*  The brain does a whole other kind of thing. So you need to understand the principles
*  of processing so that you can still apply engineering tricks where you want to do. You
*  don't want to be slavishly mimicking all the things of the brain. It should be one input. I think it
*  is extremely helpful. But it should be the point of really understanding so that you know when to
*  deviate from it. Okay. That's really cool. That's work from a few years ago. You did work in
*  Umenta with Jeff Hawkins, with hierarchical temporal memory. If you could give a brief history,
*  how is your view of the way the models of the brain changed over the past few years leading up
*  to now? Is there some interesting aspects where there was an adjustment to your understanding of
*  the brain or is it all just building on top of each other? In terms of the higher level ideas,
*  especially the ones Jeff wrote about in the book, if you blur out, right?
*  On intelligence. Right. On intelligence. If you blur out the details and if you just zoom out
*  and at the higher level idea, things are, I would say, consistent with what he wrote about. But
*  many things will be consistent with that because it's a blur. Deep learning systems
*  are also multi-level, hierarchical, all of those things. But in terms of the detail,
*  a lot of things are different and those details matter a lot. So one point of difference I had
*  with Jeff was how much of biological plausibility and realism do you want in the learning algorithms?
*  So when I was there, this was almost 10 years ago now.
*  That applies when you're having fun. I don't know what Jeff thinks now, but 10 years ago,
*  the difference was that I did not want to be so constrained on saying my learning algorithms
*  need to be biologically plausible based on some filter of biological plausibility available at
*  that time. To me, that is a dangerous cut to make because we are discovering more and more things
*  about the brain all the time. New biophysical mechanisms, new channels are being discovered
*  all the time. So I don't want to upfront kill off a learning algorithm just because we don't
*  really understand the full biophysics of how the brain learns.
*  Exactly.
*  Let me ask Sergeant Traub, what's your sense, what's our best understanding of how the brain
*  learns?
*  Things like back propagation, credit assignment. So many of these algorithms, learning algorithms,
*  have things in common. Back propagation is one way of credit assignment. There is another algorithm
*  called expectation maximization, which is another weight adjustment algorithm.
*  But is your sense the brain does something like this?
*  Has to. There is no way around it in the sense of saying that you do have to adjust the connections.
*  And you're saying credit assignment, you have to reward the connections that were useful in making
*  a correct prediction and not, yeah, I guess, but yeah, it doesn't have to be
*  differentiable. Yeah, it doesn't have to be differentiable. Yeah. But you have to have a
*  model that you start with, you have data comes in, and you have to have a way of adjusting
*  the model such that it better fits the data. So that is all of learning. And some of them can be
*  using backprop to do that. Some of it can be using very local graph changes to do that.
*  Many of these learning algorithms have similar update properties locally in terms of what the
*  neurons need to do locally. I wonder if small differences in learning algorithms can have
*  huge differences in the actual effect. So the dynamics of, I mean, sort of the reverse spiking,
*  if credit assignment is like a lightning versus like a rainstorm or something, whether there's
*  like a looping local type of situation with the credit assignment, whether there is
*  regularization, like how it injects robustness into the whole thing,
*  like whether it's chemical or electrical or mechanical, all those kinds of things.
*  Yes. I feel like those differences could be essential, right? It could be. It's just that
*  it's just that you don't know enough to, on the learning side, you don't know enough to say,
*  that is definitely not the way the brain does it. Got it. So you don't want to be stuck to it.
*  Right. So you've been open-minded on that side of things.
*  Correct. On the inference side, on the recognition side, I am much more amenable to being constrained
*  because it's much easier to do experiments because it's like, okay, here's the stimulus.
*  How many steps did it get to take the answer? I can trace it back. I can understand the speed
*  of that computation, et cetera, much more readily on the inference side.
*  Got it. And then you can't do good experiments on the learning side.
*  Correct. So let's go right into the cortical microcircuits right back. So what are these ideas
*  beyond recursive cortical network that you're looking at now?
*  So we have made a pass through multiple of the steps that, as I mentioned earlier,
*  we were looking at perception from the angle of cognition. It was not just perception for
*  perception sake. How do you connect it to cognition? How do you learn concepts? And
*  how do you learn abstract reasoning, similar to some of the things Francois talked about?
*  Right. So we have taken one pass through it, basically saying, what is the basic cognitive
*  architecture that you need to have, which has a perceptual system, which has a system that
*  learns dynamics of the world, and then has something like a routine program learning system on top of
*  it to learn concepts. So we have built the version point one of that system. This was,
*  another science robotics paper. It's the title of that paper was something like cognitive programs.
*  How do you build cognitive programs? And the application there was on
*  manipulation, robotic manipulation? So think of it like this. Suppose you wanted to tell
*  a new person that you met, you don't know the language that person uses. You want to communicate
*  to that person to achieve some task. So I want to say, hey, you need to pick up all the red cups
*  from the kitchen counter and put it here. How do you communicate that? You can show pictures.
*  You can basically say, look, this is the starting state. The things are here. This is the ending
*  state. And what does the person need to understand from that? The person needs to understand
*  what conceptually happened in those pictures from the input to the output.
*  So we are looking at pre-verbal conceptual understanding. Without language,
*  how do you have a set of concepts that you can manipulate in your head? And from a
*  set of images of input and output, can you infer what is happening in those images?
*  Got it. With concepts that are pre-language. Okay. So what does it mean for concepts that are
*  pre-language? Why is language so important here? So I want to make a distinction between concepts that
*  are just learned from text. By just feeding brute force text, you can start extracting things like,
*  okay, cow is likely to be on grass. So those kinds of things you can extract purely from text.
*  But that's kind of a simple association thing rather than a concept as an abstraction of
*  something that happens in the real world in a grounded way that I can simulate it in my mind
*  and connect it back to the real world. And you think kind of the visual world,
*  concepts in the visual world are somehow lower level than just the language.
*  The lower level kind of makes it feel like, okay, that's like an unimportant, like it's more like,
*  I would say the concepts in the visual and the motor system and the concept learning system,
*  which if you cut off the language part, just what we learn by interacting with the world
*  and abstractions from that, that is a prerequisite for any real language understanding.
*  So you disagree with Chomsky because he says language is at the bottom of everything.
*  No, I disagree with Chomsky completely on a common level, from universal grammar to...
*  So that was a paper in Science B on the recursive cortical network.
*  What other interesting problems are there, open problems in brain-inspired
*  approaches that you're thinking about? I mean, everything is open, right? No problem is
*  solved, solved. I think of perception as kind of the first thing that you have to build,
*  but the last thing that you will be actually solved. Because if you do not build perception
*  system in the right way, you cannot build concept system in the right way. So you have to build a
*  perception system, however wrong that might be, you have to still build that and learn concepts
*  from there and then keep iterating. And finally, perception will get solved fully when perception,
*  cognition, language, all those things work together finally. Great, we've talked a lot
*  about perception, but then maybe on the concept side and like common sense or just general
*  reasoning side, is there some intuition you can draw from the brain about how we can do that?
*  So I have this classic example I give. So suppose I give you a few sentences and then ask you a
*  question following that sentence. This is a natural language processing problem, right? So here it goes.
*  I'm telling you, Sally pounded a nail on the ceiling. Okay, that's a sentence. Now I'm asking
*  you a question, was the nail horizontal or vertical? Vertical. Okay, how did you answer that?
*  Well, I imagined Sally, it was kind of hard to imagine what the hell she was doing, but
*  I imagined the visual of the whole situation. Exactly, exactly. So here, I post a question in
*  natural language. The answer to that question was you got the answer from actually simulating the
*  scene. Now I can go more and more detailed about, okay, was Sally standing on something while doing
*  this? Could she have been standing on a light bulb to do this? I could ask more and more
*  questions about this and I can ask, make you simulate the scene in more and more detail,
*  right? Where is all that knowledge that you're accessing stored? It is not in your language
*  system. It was not just by reading text you got that knowledge. It is stored from the everyday
*  experiences that you have had from, and by the age of five, you have pretty much all of this,
*  and it is stored in your visual system, motor system, in a way such that it can be accessed
*  through language. Got it. I mean, right. So the language almost serves as a query into the whole
*  visual cortex and it does the whole feedback thing, but is all reasoning kind of connected to the
*  perception system in some way? You can do a lot of it. You can still do a lot of it by quick
*  associations without having to go into the depth, and most of the time you will be right, right?
*  You can just do quick associations, but I can easily create tricky situations for you where
*  that quick association is wrong and you have to actually run the simulation. So figuring out how
*  these concepts connect, do you have a good idea of how to do that? That's exactly what one of the
*  problems that we are working on, and the way we are approaching that is basically saying, okay,
*  you need to... So the takeaway is that language is simulation control, and your perceptual plus
*  motor system is building a simulation of the world. So that's basically the way we are approaching
*  it, and the first thing that we built was a controllable perceptual system, and we built
*  a schema network, which was a controllable dynamic system, then we built a concept learning system
*  that puts all these things together into programs or subtractions that you can run and simulate,
*  and now we are taking the step of connecting into language. It will be very simple examples.
*  Initially, it will not be the GPT-3-like examples, but it will be grounded simulation-based language.
*  And for like the querying would be like question answering kind of thing?
*  Correct. And it will be in some simple world initially, but it will be about, okay, can the
*  system connect the language and ground it in the right way and run the right simulations
*  to come up with the answer? And the goal is to try to do things that, for example, GPT-3 couldn't do.
*  Correct. Speaking of which, if we could talk about GPT-3 a little bit, I think it's an interesting
*  thought-provoking set of ideas that OpenAI is pushing forward. I think it's good for us to talk
*  about the limits and the possibilities in neural networks. So in general, what are your thoughts
*  about this recently released very large 175 billion parameter language model?
*  So I haven't directly evaluated it yet. From what I have seen on Twitter and other people evaluating
*  it, it looks very intriguing. I am very intrigued by some of the properties it is displaying.
*  Of course, the text generation part of that was already evident in GPT-2, that it can generate
*  coherent text over long distances. But of course, the weaknesses are also pretty visible in saying
*  it is not really carrying a world state around. Sometimes you get sentences like,
*  I went up the hill to reach the valley, or some completely incompatible statements. Or when you're
*  traveling from one place to the other, it doesn't take into account the time of travel, things like
*  that. So those things, I think, will happen less in GPT-3 because it is trained on even more data.
*  And so it can do even more longer distance coherence. But it will still have the fundamental
*  limitations that it doesn't have a world model. And it can't run simulations in its head to find
*  whether something is true in the world or not. Do you think within, so taking a huge amount of
*  text from the internet and forming a compressed representation, do you think in that could emerge
*  something that's an approximation of a world model, which essentially could be used for reasoning?
*  I mean, I'm not talking about GPT-3, I'm talking about GPT-4, 5, and GPT-10.
*  Yeah, I mean, they will look more impressive than GPT-3. So if you take that to the extreme, then
*  a Markov chain of just first order, and if you go to, I'm taking it the other extreme,
*  if you read Shannon's book, he has a model of English text, which is based on first-order
*  Markov chains, second-order Markov chains, third-order Markov chains, and think that,
*  okay, third-order Markov chains look better than first-order Markov chains. So does that mean a
*  first-order Markov chain has a model of the world? Yes, it does. So yes, in that level, when you go
*  to higher-order models or more sophisticated structure in the model like the transformer
*  networks have, yes, they have a model of the text world, but that is not a model of the world. It's
*  a model of the text world and it will have interesting properties and it will be useful,
*  but just scaling it up is not going to give us AGI or natural language understanding or meaning.
*  The question is whether being forced to compress a very large amount of text
*  forces you to construct things that are very much like, because the ideas of concepts and meaning
*  is a spectrum. Sure, yeah. So in order to form that kind of compression,
*  maybe it will be forced to figure out abstractions which look awfully a lot like the kind of things
*  that we think about as concepts, as world models, as common sense. Is that possible?
*  No, I don't think it is possible because the information is not there.
*  The information is there behind the text, right? No, unless somebody has written down all the
*  details about how everything works in the world to the absurd amounts like, okay, it is easier to
*  walk forward than backward, that you have to open the door to go out of the thing,
*  doctors wear underwear. Unless all these things somebody has written down somewhere or somehow
*  the program found it to be useful for compression from some other text, the information is not there.
*  So that's an argument that text is a lot lower fidelity than the experience of our physical world.
*  Pictures worth a thousand words.
*  Well, in this case, pictures aren't really... So the richest aspect of the physical world isn't
*  even just pictures, it's the interactivity with the world. It's being able to interact.
*  It's almost like if you could interact... Well, maybe I agree with you that pictures
*  were a thousand words, but a thousand... Yeah, you could say you could capture it with the GPT-X.
*  So I wonder if there's some interactive element where a system could live in text world where it
*  could be part of the chat, be part of talking to people. It's interesting. I mean, fundamentally,
*  so you're making a statement about the limitation of text. Okay, so let's say we have a text corpus
*  that includes basically every experience we could possibly have. I mean, just a very large
*  corpus of text and also interactive components. I guess the question is whether the neural network
*  architecture, these very simple transformers, but if they had like hundreds of trillions or
*  whatever comes after a trillion parameters, whether that could store the information
*  needed, that's architectural. Do you have thoughts about the limitation on that side of
*  things with neural networks? I mean, so Transformer is still a feed-forward neural network. It has a
*  very interesting architecture, which is good for text modeling and probably some aspects of
*  video modeling, but it is still a feed-forward architecture. And you believe in the feedback
*  mechanism, the recursion. Oh, and also causality, being able to do counterfactual reasoning,
*  being able to do interventions, which is actions in the world. So all those things require different
*  kinds of models to be built. I don't think Transformers captures that family. It is very
*  good at statistical modeling of text and it will become better and better with more data,
*  bigger models, but that is only going to get so far. So I had this joke on Twitter saying that,
*  hey, this is a model that has read all of quantum mechanics and theory of relativity,
*  and we are asking it to do text completion or we are asking it to solve simple puzzles.
*  When you have AGI, that's not what you ask the system to do. We'll ask the system to do
*  experiments and come up with hypotheses and revise the hypothesis based on evidence from
*  experiments, all those things. Those are the things that we want the system to do when we have AGI,
*  not solve simple puzzles. Impressive demo, somebody generating a red button in HTML.
*  Right. Which are all useful. There is no dissing the usefulness of it.
*  So by the way, I'm playing a little bit of a devil's advocate, so calm down, Internet.
*  So I'm curious almost in which ways will a dumb but large neural network will surprise us.
*  Yeah.
*  So I completely agree with your intuition. It's just that I don't want to dogmatically
*  like 100% put all the chips there. We've been surprised so much. Even the current GPT 2 and
*  3 are so surprising. The self-play mechanisms of AlphaZero are really surprising.
*  The fact that reinforcement learning works at all to me is really surprising. The fact that
*  neural networks work at all is quite surprising. Given how nonlinear the space is, the fact that
*  it's able to find local minima that are at all reasonable, it's very surprising. So I wonder
*  sometimes whether us humans just want it for AGI not to be such a dumb thing. Because exactly
*  what you're saying is like the ideas of concepts and be able to reason with those concepts and
*  connect those concepts in hierarchical ways and then to be able to have world models.
*  Just everything we're describing in human language in this poetic way seems to make sense. That is
*  what intelligence and reasoning are like. I wonder if at the core of it, it could be much dumber.
*  Well, finally it is still connections and messages passing over them.
*  Right.
*  Right.
*  So in that way it is dumb.
*  So I guess the recursion, the feedback mechanism, that does seem to be a fundamental kind of thing.
*  Yeah. Yeah. The idea of concepts, also memory.
*  Correct. Yeah. Like having an episodic memory.
*  Yeah. That seems to be an important thing. So how do we get memory?
*  So yeah, we have another piece of work that came on recently on how do you form episodic
*  memories and form abstractions from them. And we haven't figured out all the connections of
*  that to the overall cognitive architecture. But-
*  Well, yeah. What are your ideas about how you could have episodic memory?
*  So at least it's very clear that you need to have two kinds of memory. That's very, very clear.
*  There are things that happen as statistical patterns in the world, but then there is the
*  one timeline of things that happen only once in your life. And this day is not going to happen
*  ever again. And that needs to be stored as just a stream of string. This is my experience.
*  And then the question is about how do you take that experience and connect it to the
*  statistical part of it? How do you now say that, okay, I experienced this thing. Now I want to
*  be careful about similar situations. And so you need to be able to index that similarity
*  using your other giants that is the model of the world that you have learned. Although the situation
*  came from the episode, you need to be able to index the other one. So the episodic memory
*  being implemented as an indexing over the other model that you're building.
*  So the memories remain and they're an index into the statistical thing that you formed.
*  Yeah, statistical causal structural model that you built over time. So it's basically the idea is
*  that the hippocampus is just storing or sequencing a set of pointers that happens over time. And then
*  whenever you want to reconstitute that memory and evaluate the different aspects of it,
*  whether it was good, bad, do I need to encounter the situation again, you need the cortex to
*  reinstantiate, to replay that memory. So how do you find that memory? Which direction is the
*  important direction? Both directions are again bidirectional. I guess how do you retrieve the
*  memory? So this is again hypothesis, right? So when you come to a new situation, your cortex
*  is doing inference over in the new situation. And then of course, hippocampus is connected to
*  different parts of the cortex. And you have this deja vu situation, right? Okay, I have seen this
*  thing before. And then in the hippocampus, you can have an index of, okay, this is when it happened,
*  as a timeline. And then you can use the hippocampus to drive the similar timelines to say,
*  now I am, rather than being driven by my current input stimuli, I am going back in time and
*  rewinding my experience from there. Replaying it. But putting back into the cortex. And then
*  putting it back into the cortex, of course, affects what you're going to see next in your
*  current situation. Got it. Yeah. So that's the whole thing, having a world model and then,
*  yeah, connecting to the perception. Yeah, it does seem to be that that's what's happening.
*  On the neural network side, it's interesting to think of how we actually do that.
*  Yeah. To have a knowledge base.
*  Yes. It is possible that you can put many of these structures into neural networks and we will find
*  ways of combining properties of neural networks and graphical models. So, I mean, it's already
*  started happening. Graph neural networks are kind of a merge between them. And there will be more
*  of that thing. So, but to me, the direction is pretty clear. Looking at biology and the history
*  of evolution, the history of intelligence, it is pretty clear that, okay, what we need is
*  more structure in the models and modeling of the world and supporting dynamic inference.
*  Well, let me ask you, there's a guy named Elon Musk. There's a company called Neuralink and
*  there's a general field called Brain-Computer Interfaces. Yeah. It's kind of an interface
*  between your two loves, the brain and the intelligence. So, there's very direct
*  applications of brain-computer interfaces for people with different conditions, more in the
*  short term. But there's also these sci-fi, futuristic kinds of ideas of AI systems being able to
*  communicate in a high bandwidth way with the brain, bidirectional. What are your thoughts
*  about Neuralink and BCI in general as a possibility? So, I think BCI is a cool research
*  area. And in fact, when I got interested in brains initially, so I was enrolled at Stanford,
*  and when I got interested in brains, it was through a brain-computer interface talk that
*  Krishna Shainoy gave. That's when I even started thinking about the problem. So, it is definitely
*  a fascinating research area and the applications are enormous. So, there's a science fiction
*  scenario of brains directly communicating. Let's keep that aside for the time being.
*  Even just the intermediate milestones they're pursuing, which are very reasonable as far as I
*  can see, being able to control an external limb using direct connections from the brain and
*  being able to write things into the brain. So, those are all good steps to take and they have
*  enormous applications. People losing limbs being able to control prosthetics, quadriplegics being
*  able to control something, and therapeutics. I also know about another company working in this
*  space called Paradromics. They're based on a different electrode array, but trying to attack
*  some of the same problems. Also, surgery? Correct. Surgically implanted electrodes.
*  Yeah, I think of it as a very promising field, especially when it is helping people overcome
*  some limitations. Now, at some point, of course, it will advance the level of being able to
*  communicate. How hard is that problem, do you think? Let's say we magically solve what I think is a
*  really hard problem of doing all of this safely. Being able to connect electrodes,
*  and not just thousands, but millions to the brain. I think it's very, very hard because you also
*  do not know what will happen to the brain with that. How does the brain adapt to something like
*  that? As we're learning, the brain is quite, in terms of neuroplasticity, it's pretty malleable.
*  So it's going to adjust. So the machine learning side, the computer side is going to adjust,
*  and then the brain is going to adjust. Exactly. And then what soup does this land us into?
*  The kind of hallucinations you might get from this. That might be pretty intense.
*  Just connecting to all of Wikipedia. It's interesting whether we need to be able to figure
*  out the basic protocol of the brain's communication schemes in order to get them to
*  machine and the brain to talk. Because another possibility is the brain actually just adjusts
*  to whatever the heck the computer is doing. Exactly. I find that to be a more promising way.
*  It's basically saying, okay, attach electrodes to some part of the cortex. Maybe if it is done from
*  birth, the brain will adapt. It says that part is not damaged. It was not used for anything.
*  These electrodes are attached there. And now you train that part of the brain to do this high
*  bandwidth communication between something else. And if you do it like that, then it is brain
*  adapting to, and of course your external system is designed such that it is adaptable. Just like we
*  design computers or mouse, keyboard, all of them to be interacting with humans. So of course,
*  that feedback system is designed to be human compatible. But now it is not trying to record
*  from all of the brain. And now two systems trying to adapt to each other. It's the brain adapting
*  into one way. That's fascinating. The brain is connected to the internet. Just imagine it's
*  connecting it to Twitter and just taking that stream of information.
*  But again, if we take a step back, I don't know what your intuition is. I feel like that is not
*  as hard of a problem as doing it safely. There's a huge barrier to surgery because the biological
*  system is a mush of weird stuff. So that, the surgery part of it, biology part of it,
*  the long-term repercussions part of it, I don't know what else will. We often find after a long
*  time in biology that, okay, that idea was wrong. People used to cut off the gland called the thymus
*  or something. And then they found that, oh no, that actually causes cancer.
*  And then there's a subtle millions of variables involved. But this whole process, the nice thing,
*  just like again with Elon, just like colonizing Mars seems like a ridiculously difficult idea.
*  But in the process of doing it, we might learn a lot about the biology of the brain, the neuroscience
*  side of things. It's like, if you want to learn something, do the most difficult version of it
*  and see what you learn. The intermediate steps that they are taking sounded all very reasonable
*  to me. Yeah, it's great. Well, but like everything with Elon is the timeline seems insanely fast. So
*  that's the only awful question. Well, we've been talking about cognition a little bit. So like
*  reasoning, we haven't mentioned the other C word, which is consciousness. Do you ever think about
*  that one? Is that useful at all in this whole context of what it takes to create an intelligent
*  reasoning being? Or is that completely outside of the engineering perspective of intelligence?
*  It is not outside the realm, but it doesn't on a day-to-day basis inform what we do. But it's more
*  so in many ways, the company name is connected to this idea of consciousness.
*  What's the company name? Vicarious. So Vicarious is the company name.
*  So what does Vicarious mean? At the first level, it is about modeling the world, and it is
*  internalizing the external actions. So you interact with the world and learn a lot about the world.
*  Now, after having learned a lot about the world, you can run those things in your mind without
*  actually having to act in the world. So you can run things vicariously just in your brain.
*  And similarly, you can experience another person's thoughts by having a model of how that person
*  works and putting yourself in some other person's shoes. So that is being Vicarious.
*  Now, it's the same modeling apparatus that you're using to model the external world or some other
*  person's thoughts. You can turn it to yourself. If that same modeling thing is applied to your own
*  modeling apparatus, then that is what gives rise to consciousness, I think.
*  Well, that's more like self-awareness. There's the hard problem of consciousness, which is
*  when the model feels like something, when this whole process is like you really are in it,
*  you feel like an entity in this world. Not just you know that you're an entity, but it feels like
*  something to be that entity. And thereby, we attribute this... Then it starts to be where it's
*  something that has consciousness can suffer. You start to have these kinds of things that
*  we can reason about that is much heavier. It seems like there's much greater cost of your decisions.
*  And mortality is tied up into that. The fact that these things end. First of all, I end at some point
*  and then other things end. That somehow seems to be, at least for us humans, a deep motivator.
*  That idea of motivation in general, we talk about goals in AI, but goals aren't quite the same thing
*  as our mortality. It feels like, first of all, humans don't have a goal. They just create goals
*  at different levels. They make up goals because we're terrified by the mystery of the thing that
*  gets us all. We make these goals up. We're like a goal generation machine, as opposed to a machine
*  which optimizes the trajectory towards a singular goal. It feels like that's an important part of
*  the whole mortality thing. Cognition.
*  Well, it is a part of human cognition, but there is no reason for that mortality to
*  come to the equation for an artificial system because we can copy the artificial system.
*  The problem with humans is that I can't clone you. Even if I clone you as the hardware,
*  your experience that was stored in your brain, your episodic memory, all those will not be
*  captured in the new clone. But that's not the same with an AI system.
*  But it's also possible that the thing that you mentioned with us humans is actually of
*  fundamental importance for intelligence. The fact that you can copy an AI system means that AI system
*  is not yet an AGI. If you look at existence proof, if we reason based on existence proof,
*  you could say that it doesn't feel like death is a fundamental property of an intelligence system.
*  But we don't yet give me an example of an immortal intelligent being. We don't have those.
*  It's very possible that that is a fundamental property of intelligence. It's a thing that
*  has a deadline for itself. But you can think of it like this. Suppose you
*  invent a way to freeze people for a long time. It's not dying. You can be frozen and woken up
*  thousands of years from now. It's no fear of death.
*  It's not about time. It's about the knowledge that it's temporary. That aspect of it,
*  the finiteness of it, I think creates a kind of urgency.
*  Correct. For us, for humans.
*  Yeah, for humans.
*  Yes. And that is part of our drives. And that's why I'm not too worried about
*  AI having motivations to kill all humans and those kinds of things. Why? Just wait.
*  Why do you need to do that?
*  I've never heard that before. That's a good point. Yeah, murder seems like a lot of work.
*  They'll probably hurt themselves. Let me ask you. People often kind of wonder,
*  world-class researchers such as yourself, what kind of books, technical fiction, philosophical
*  were, had an impact on you in your life and maybe ones you could possibly recommend
*  that others read. Maybe if you have three books that pop into mind.
*  Yeah. So I definitely liked Judea Pearl's book, Probabilistic Reasoning and Intelligent Systems.
*  It's a very deep technical book. But what I liked is that, so there are many places where
*  you can learn about probabilistic graphical models from. But throughout this book, Judea
*  Pearl kind of sprinkles his philosophical observations and he thinks about, connects
*  to how the brain thinks and attentions and resources, all those things. So that whole thing
*  makes it more interesting to read.
*  He emphasizes the importance of causality.
*  So that was in his later book. So the first book, Probabilistic Reasoning and Intelligent Systems,
*  mentions causality, but he hadn't really sunk his teeth into how do you actually formalize it.
*  The second book, Causality, the one in 2000, that one is really hard. So I wouldn't recommend that.
*  So that looks at the mathematical, his model of-
*  Do calculus.
*  Do calculus. Yeah, it was pretty dense mathematical.
*  Right. The book of Why is definitely more enjoyable.
*  Oh, for sure.
*  So yeah, so I would recommend Probabilistic Reasoning and Intelligent Systems. Another book I
*  liked was one from Doug Hufstadter. This was a long time ago. He had a book, I think, called,
*  it was called The Mind's Eye. It was probably Hufstadter and Daniel Dennett together.
*  And it actually was, I bought that book, it's on my shelf, I haven't read it yet, but I couldn't
*  get an electronic version of it, which is annoying because I read everything on Kindle.
*  So I had to actually purchase the physical, it's like one of the only physical books I have.
*  Yeah.
*  Anyway, a lot of people recommended it highly.
*  So yeah. And the third one I would definitely recommend reading is, this is not a technical
*  book, it is history. It's called, the name of the book I think is Bishop's Boys. It's about
*  Wright brothers and their path and how it was, there are multiple books on this topic,
*  and all of them are great. It's fascinating how flight was treated as an unsolvable problem.
*  And also, what aspects did people emphasize? People thought, oh, it is all about
*  just powerful engines, just need to have powerful lightweight engines.
*  Some people thought of it as, how far can we just throw the thing? Just throw it.
*  Like a catapult.
*  Yeah. So it's very fascinating. And even after they made the invention, people not believing it.
*  Ah, the social aspect of it.
*  The social aspect. It's very fascinating.
*  Do you draw any parallels between birds fly? So there's the natural approach to flight,
*  and then there's the engineered approach. Do you see the same kind of thing with the brain
*  and our trying to engineer intelligence?
*  Yeah. It's a good analogy to have. Of course, all analogies have their limits.
*  For sure.
*  So people in AI often use airplanes as an example of, hey, we didn't learn anything from birds.
*  But the funny thing is that, and the saying is, airplanes don't flap wings. This is what they say.
*  The funny thing and ironic thing is that you don't need to flap to fly. It's something
*  Wright brothers found by observing birds. In some of these books, they show their notebook
*  drawings. They make detailed notes about buzzards just soaring over thermals. And they basically
*  say, look, flapping is not the important. Propulsion is not the important problem to solve here.
*  We want to solve control. And once you solve control, propulsion will fall into place.
*  All of these are people, they relate this by observing birds.
*  Beautifully put. That's actually brilliant. Because people do use that analogy a lot.
*  I'm going to have to remember that one.
*  Do you have advice for people interested in artificial intelligence, like young folks today?
*  I talk to undergraduate students all the time. Interested in neuroscience,
*  interested in understanding how the brain works. Is there advice you would give them
*  about their career, maybe about their life in general?
*  Sure. I think every piece of advice should be taken with a pinch of salt, of course. Because
*  each person is different. Their motivations are different. But I can definitely say,
*  if your goal is to understand the brain from the angle of wanting to build one, then
*  being an experimental neuroscientist might not be the way to go about it.
*  A better way to pursue it might be through computer science, electrical engineering,
*  machine learning, and AI. And of course, you have to study up the neuroscience,
*  but that you can do on your own. If you are more attracted by finding something intriguing,
*  discovering something intriguing about the brain, then of course, it is better to be an experimentalist.
*  So find that motivation. What are you intrigued by? And of course, find your strengths too.
*  Some people are very good experimentalists and they enjoy doing that.
*  It's interesting to see which department, if you're picking in terms of your education path,
*  whether to go with like, at MIT, it's brain and computer, no, BCS.
*  Yeah. Brain and cognitive sciences.
*  Yeah. Or the CS side of things. And actually, the brain folks, the neuroscience folks are more and
*  more now embracing of learning TensorFlow and PyTorch. They see the power of trying to engineer
*  ideas that they get from the brain and then explore how those could be used to create
*  intelligent systems. So that might be the right department actually.
*  So this was a question in one of the Red Bull Neuroscience Institute workshops
*  that Jeff Hawkins organized almost 10 years ago. This question was put to a panel, right?
*  What should be the undergrad major you should take if you want to understand the brain?
*  And the majority opinion in that one was electrical engineering.
*  Interesting.
*  Because I mean, I'm a doubly undergrad, so I got lucky in that way. But I think it does have some
*  of the right ingredients because you learn about circuits. You learn about how you can construct
*  circuits to do functions. You learn about microprocessors. You learn information theory.
*  You learn signal processing. You learn continuous math. So in that way, it's a good step.
*  If you want to go to computer science or neuroscience, it's a good step.
*  The downside, you're more likely to be forced to use MATLAB.
*  One of the interesting things about, I mean, this is changing. The world is changing. But
*  certain departments lagged on the programming side of things, on developing good
*  habits. There's a software engineering. But I think that's more and more changing.
*  And students can take the answer with their own hands, like learn to program. I feel like everybody
*  should learn to program because it, like everyone in the sciences, because it empowers, it puts the
*  data at your fingertips. So you can organize it. You can find all kinds of things in the data.
*  And then you can also, for the appropriate sciences, build systems that, like based on that.
*  So like then engineer intelligence systems. We already talked about mortality. So we hit
*  a ridiculous point. But let me ask you the, you know,
*  one of the things about intelligence is it's goal driven. And you study the brain.
*  So the question is like, what's the goal that the brain is operating under? What's the meaning of
*  it all for us humans in your view? What's the meaning of life?
*  The meaning of life is whatever you construct out of it. It's completely open.
*  It's open. So there's nothing, like you mentioned, like you're not going to be able to
*  like you mentioned, you like constraints. So there's what's, it's wide open. Is there,
*  is there some useful aspect that you think about in terms of like the openness of it and just the
*  basic mechanisms of generating goals in studying cognition in the brain that you think about?
*  Or is it just about, cause everything we've talked about kind of the perception system
*  is to understand the environment. That's like to be able to like not die,
*  like not fall over and like be able to, you don't think we need to think about anything bigger than
*  that. Yeah, I think so because it's, it's basically being able to understand the machinery of the
*  world such that you can pursue whatever goals you want. Right. So the machinery of the world is,
*  is really ultimately what we should be striving to understand. The rest is just,
*  the rest is just whatever the heck you want to do or whatever, whatever.
*  One who is culturally popular.
*  I think that's, that's beautifully put. I don't think there's a better way to end it.
*  I'm so honored that you, you would show up here and waste your time with me. It's been an awesome
*  conversation. Thanks so much for talking today. Oh, thank you so much. This was,
*  this was so much more fun than I expected. Thank you.
*  Thanks for listening to this conversation with delete George and thank you to our sponsors,
*  Babbel, Raycon earbuds and masterclass. Please consider supporting this podcast by going to
*  babbel.com and use code Lex going to buy Raycon.com slash Lex and signing up at masterclass.com slash
*  Lex. Click the links, get the discount. It really is the best way to support this podcast.
*  If you enjoy this thing, subscribe on YouTube, review the five stars, not the podcast,
*  support on Patreon, connect with me on Twitter, Alex Friedman spelled. Yes. Without the E,
*  just F R I D M A N. And now let me leave you with some words from Marcus Aurelius.
*  You have power over your mind, not outside events. Realize this and you will find strength.
*  Thank you for listening and hope to see you next time.

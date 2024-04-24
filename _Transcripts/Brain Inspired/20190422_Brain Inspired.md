---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4545s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 3643
Video Rating: None
---

# BI 032 Rafal Bogacz: Back-Propagation in Brains
**Brain Inspired:** [April 22, 2019](https://www.youtube.com/watch?v=DYOXAMthyiw)
*  So I think this sounds like a really crazy principle, but I think that it may turn out
*  to be a correct description of how we select actions.
*  There's this big question, how these micro changes are orchestrated in the whole brain
*  and how they together result in learning in the distributed network of brain areas.
*  And I think this is the place where the theory inspired by deep learning can bring a lot
*  of insight.
*  This is Brain Inspired.
*  And so I say to you, my fellow truth seekers, ask not what backpropagation can do for neuroscience,
*  Ask what neuroscience can do for backpropagation.
*  You may have recognized that from a famous speech long ago.
*  It's possible I altered some of the words there.
*  Welcome to the show, everyone.
*  I'm Paul Middlebrooks.
*  My guest today is Rafal Bogach.
*  He is a professor at University of Oxford, where he leads a group of researchers focused
*  on understanding the information processing and the dynamics of neural activity that underlie
*  decision making and what goes wrong therein in neurological disorders.
*  Rafal has mostly worked with computational models and simulations in this regard, but
*  he's recently become interested in how backpropagation may be approximated in brains.
*  And today we talk about his recent review article on that topic in Trends in Cognitive
*  Science with his co-author James Whittington.
*  Talk during the show in broad terms about what we know about how brains learn by changing
*  the strength of connections between neurons called synaptic plasticity and how machines
*  learn these days by changing network weights between units via backpropagation and how
*  the brain might implement some version of backpropagation or some approximation of backpropagation,
*  which has proven so efficient and useful in machines.
*  We also revisit the free energy principle and predictive coding, which we've talked
*  about on the show here multiple times now.
*  But you free energy principle nuts out there might enjoy hearing about it once again.
*  Today we talk about it in terms of what a predictive coding framework would look like
*  implementing an approximation to backpropagation in the brain, which is what got Rafal interested
*  in the first place in this question.
*  That is part of the larger picture of how backprop might be approximated by brains,
*  and we cover the various proposed mechanisms they describe in the review paper, although
*  it's by no means an exhaustive survey on the topic.
*  One of those mechanisms is by encoding errors in apical dendrites, which we discuss more
*  in depth in the episode.
*  To learn even more about that, I would also refer you to episode 9 with Blake Richards,
*  where we talk about his and others' work modeling how that could work in dendrites.
*  Rafal and I also today talk about the merits of looking for different kinds of computations
*  in different brain regions.
*  Rafal waxes poetic about the free energy principle and its broader implications, and of course
*  we cover a lot more.
*  And links to the stuff that we discuss in the show notes at braininspired.co slash podcast
*  slash thirty two.
*  Anand, Wally, Henrik, Scott, when I see any of you, I will put you on a balcony and serenade
*  you.
*  Thanks for supporting the show through Patreon and or PayPal, both of which you can find
*  on braininspired.co if you find it within your means to contribute two or four dollars per
*  month to the show.
*  Thanks for listening, guys.
*  I have a lot more great guests lined up in the near future.
*  But for now, please enjoy the delightful, insightful Rafal Bogac.
*  Rafal, it is great to have you here.
*  Thanks for being with me today on the show.
*  It's a great pleasure.
*  Thank you, Paul.
*  So I will have introduced you more in the introduction here, but just very briefly,
*  you're a professor at the University of Oxford and you lead a group that models information
*  processing and decision making in our brains.
*  And I know you from your work on decision making and assessing different models for
*  how perceptual decisions get made, asking which models are the most efficient, make
*  the most sense, you know, in various conditions, are the most optimal.
*  And your work relating these models to known properties in brain circuits, like those in
*  basal ganglia and the cortex, and your work on the speed accuracy trade off, which actually
*  played a big part in one of my colleagues' research on that topic.
*  So thanks for that in general.
*  But recently, you have spent some time focusing on the free energy principle and predictive
*  coding.
*  And you wrote a really nice mathematical tutorial that's very accessible on the subject.
*  And we'll talk predictive coding a bit today.
*  But the big topic really for today's show is how the brain might implement something
*  like back propagation.
*  Now based on your body of work, my guess is that you are mostly concerned with optimization
*  and efficiency in brains and models.
*  So okay.
*  So if that is correct, so how would you characterize your approach and what drives your interests?
*  So as you mentioned, we are very much interested in the idea that the brain is performing computations
*  close to optimality.
*  So you can make an argument that there was always an evolutionary pressure for the brain
*  to perform optimal or efficient computation.
*  So the animals which had brain, which were performing computations more efficiently,
*  had larger chances for survival.
*  And the same can be applied not only to decision making, but also to learning.
*  So the models which are able to learn better have higher chances of being implemented in
*  the brain.
*  And as you mentioned, my previous interest in the interest of my group was in the models
*  of decision making.
*  So we wanted to know how the brain made decisions, but also how the brain decisions should be
*  made in a given circumstances.
*  And this is how we kind of entered the world of learning, the world of predictive coding
*  and our interest in the in the declining.
*  So like we just discussed, you've recently focused on the free energy principle and predictive
*  coding.
*  And we'll come back to this a little bit when we talk about an approach that you've taken
*  to modeling backpropagation in the brain.
*  But just to kind of start out, I kind of want your broad thoughts about the free energy
*  principle.
*  This is an exciting sort of it's gaining excitement, it seems.
*  Do you feel like this is the way forward for like a general principle of the brain?
*  You know, and maybe you can just describe the free energy principle in broad terms and
*  then and then judge it.
*  Okay, so you had a very nice show on free energy principle where you interviewed Sam
*  Gershman who already presented this very nicely.
*  So as Sam said, free energy principle is a subset of a Bayesian brain.
*  So it's a way in which brain could implement Bayesian inference.
*  And it's a particular algorithm of how it can do it.
*  And what this principle is saying is that during Bayesian inference, the brain is trying
*  to minimize a particular function called the free energy.
*  And it's difficult to maybe give the equations over the podcast.
*  But as you mentioned, there is a I'll refer people to your paper, I'll link to that tutorial
*  Excellent, excellent.
*  What's nice about free energy, it shows how the Bayesian inference can be implemented
*  in a very simple networks of neurons.
*  Because this optimization of free energy can be written as a set of differential equations,
*  which can be then mapped on simple networks of computational elements which behave like
*  neurons.
*  And one of these networks is the network of Ryan Ballard called predictive coding network.
*  And what it basically assumes was the fundamental principle of predictive coding is that each
*  area of the brain is trying to predict the inputs it receives.
*  And also that the brain has hierarchical organization.
*  And the lowest area could be considered like primary visual cortex, which tries to predict
*  the sensory inputs.
*  And then there are higher areas, which then trying to predict the input from the lower
*  areas, and then they send their expectations for the lowest areas.
*  And what's special about the predictive coding is that the network has a particular implementation,
*  and it includes two types of neurons.
*  So there are neurons which encode expectations and neurons which encode the errors, which
*  is how the observed inputs differ from the expectations.
*  And what the network is trying to do is trying to minimize these prediction errors all the
*  time.
*  So it's trying to minimize the surprise.
*  And this prediction errors are basically minimizing two ways.
*  So the nodes which encode the prediction errors send their errors to other nodes in the hope
*  that somehow this by changing the activity in the network, the errors can be reduced
*  and the surprise can be resolved.
*  If this is not possible, then errors will drive learning in the network and will drive
*  the changes in synaptic weights.
*  So that parameters of this network change such that the prediction errors are minimized.
*  That was a great primer and actually great for what we're going to talk about later with
*  your modeling work.
*  Do you think about...
*  So in models, you just said that there are value units and error units.
*  Do you feel like that that maps onto single neurons in the brain or a little populations
*  of neurons?
*  Is there a value neuron or is there a value population of neurons that's encoding this?
*  Or do you want to just leave that open?
*  So this is a very interesting question.
*  How do you actually map this relatively abstract model on the details of the neurobiology?
*  Because of course, we know about the anatomy of different parts of the brains and it's
*  very rich, very complex and also it differs from area to area.
*  So I think that there are some parts of the brain where we know that there are indeed
*  neurons encoding errors.
*  And I think that the best example of this is the basal ganglia where there are neurons.
*  So the basal ganglia is the part of the brain which is very important for making choices,
*  collecting actions and also learning about the rewards resulting from different actions.
*  So in the basal ganglia, there's this population of dopaminergic neurons which essentially
*  encode reward prediction errors.
*  So these neurons will have increased firing rate where the animal gets more reward than
*  it expects.
*  So I think that in this case, you can try to maybe indeed map the predictive conic networks
*  on this basal ganglia network.
*  This is in fact the focus of my current work.
*  In case of other areas like the cortex, it's less clear if there are separate neurons encoding
*  errors and separate neurons encoding predictions.
*  So we know that there's lots of evidence that neurons increase their activity when there
*  is surprising input coming, but it's not fully clear if there are separate populations of
*  error and prediction nodes.
*  And also there have been interesting models proposed and there's a particular model called
*  dendritic error model proposed by Joao Sacramento and Walter Sen, which suggest that the errors
*  are not encoded in the separate neurons, but in apical dendrites of pyramidal neurons.
*  So there are ways of mapping the predictive coding, which is like an abstract algorithm
*  in different ways on the kind of more detailed structures of neurobiology.
*  Well, Jesus, man, I've already taken this into the weeds here.
*  So let's back up just a little bit and then we're going to really get into it.
*  So before we talk about the different approaches to modeling back propagation in the brain,
*  let's just talk about learning in a very broad sense.
*  What do we know about how learning works in the brain?
*  I mean, is synaptic plasticity, is that the only game in town?
*  Is it the universally accepted way that brains learn at this point?
*  I think that there's a lot of evidence that the main mechanism by which the brain learns
*  are the changes in the strength of the synaptic connections between the neurons, which is
*  called the synaptic plasticity.
*  And this evidence comes from studies which show that learning results in changes in synaptic
*  weights.
*  And also if you prevent changes in synaptic weights by certain interventions, like blocking
*  certain neural modulators or channels, then you can prevent learning from happening.
*  But in big brains like our human brain, like mine, like my brain, where the memory is stored
*  in a distributed way in thousands of synapses, in hundreds of neurons, it's very difficult
*  to pin down this process precisely.
*  However, you can see this much more precisely in case of simple brains, like in case of
*  the insect brains, where you were a particular memory may be stored in just handful of synapses
*  on a few neurons.
*  So this approach is, for example, taken here by my colleague, Scott Waddle and his group,
*  who studies learning in the insect mushroom body, which is a part of the brain which learns
*  association of odors and rewards.
*  And there we know quite well how this network is organized.
*  And it's very simple.
*  So there's a lot of neurons which represent odors, but they have very sparse encoding.
*  So for each odor, just very few neurons are active.
*  And there's just handful of neurons which control approach and avoidance of the odors.
*  So this network can be studied very precisely because if we want to see how the system learns
*  that particular odor should be approached, we know that there's just a few synapses which
*  should change.
*  So basically, Scott and his group, they will train this animus that particular odor results
*  in reward.
*  And then they can see the changes in a small group of synapses.
*  And they see these plastic changes.
*  And then these plastic changes drive the behavior.
*  There's also another important thing to say that we know a lot about plasticity happening
*  between two neurons.
*  So neuroscientists very often study these kind of microplasticity rules.
*  How the changes in the synaptic weights depend on the activity of two neurons, the synaptic
*  weight connects, and maybe levels of the neuromodulators.
*  And the picture which emerges is that these changes are very diverse.
*  So different types of synapses have different rules.
*  And plasticity between different types of neurons depends on their timing of their activity
*  and levels of the modulators in a very different way.
*  So there's this big picture which emerges, which basically describes these micro rules
*  of synaptic plasticity.
*  But there's this big question, how these micro changes are orchestrated in the whole brain
*  and how they together result in learning in the distributed network of brain areas.
*  And I think this is the place where the theory inspired by deep learning can bring a lot
*  of insight.
*  Oh, that's interesting.
*  Even just Googling for theories of learning before synaptic plasticity is really, you
*  just don't see anything.
*  I guess there's some psychological theories.
*  But the only other thing that comes to mind is that the dynamics of the system, which
*  you could almost say is an emergent property of the underlying neurophysiology, that that
*  in itself could be implementing some sort of learning rules.
*  And maybe there's the downward causation of the dynamical system doing this overall learning,
*  what you were just talking about, distributed system.
*  There's the answer, right?
*  Or maybe not.
*  No, so I think that there are also other changes which happened during learning.
*  So for example, the excitability of neurons can change.
*  And this definitely happens.
*  But if you think about a neuron, neuron has just one parameter describing its excitability,
*  while it has thousands or tens of thousands parameters describing its synaptic connections.
*  There's just much more information capacity in synaptic connections, much more than in
*  other elements of the neuron.
*  OK, so we're on board that synaptic plasticity has something to do with learning in the brain.
*  OK, so then there are these deep learning networks.
*  So maybe we could just talk real briefly about and broadly about backpropagation, which is
*  the main way that neural networks these days and days of yore are trained.
*  So what is backpropagation?
*  And maybe you could just talk a little bit about how it differs from what we know about
*  brains.
*  OK, so I guess most of the listeners know about this, but I will just explain it very
*  briefly.
*  So the backpropagation describes learning in feedforward neural networks, which have
*  some input layer and output layer.
*  And the network works in a way that when you present an input, it can propagate the activity
*  and generate a particular output.
*  And what you want to achieve during training is that network produces a particular target
*  pattern for the given input pattern.
*  So this network is presented with multiple pairs of target and input patterns.
*  And during the learning, synaptic connections are modified.
*  And the key component or key concepts in the learning in the backpropagation algorithm
*  is the concept of error associated with each neuron.
*  And this error could be thought as expressing a difference between the activity the neuron
*  produced and the activity it should have produced in order for the network to generate the right
*  target pattern.
*  So this error is very easy to define for the last layer as simply the difference between
*  the target activity and the activity actually produced by the network.
*  And it turns out that these errors can also be defined for the intermixing layer as some
*  function of the errors from the next layer.
*  And this gives name to the algorithm as the backpropagation because these errors are kind
*  of computed backwards.
*  So they are backpropagated in the network.
*  And the key change which occurs during learning is that synaptic weights are modified proportionally
*  to the errors of the corresponding neurons.
*  And now probably the main reason why the backprop has been for a long time considered as biologically
*  implausible is that in the standard backpropagation algorithm, the errors are not computed by
*  the network itself, but are computed by an external computer program which simulates
*  the network.
*  So basically the computer program runs, which simulates the learning, will compute the errors
*  and modify the synaptic weights.
*  And in the brain, the synaptic plasticity only depends on activity of local neurons
*  connected via the sinus.
*  So this is probably the main difference and the main reasons for the critique of the algorithm.
*  Yeah.
*  I mean, I'll just quote Francis Crick from directly that you quote in the review that
*  you wrote, despite the apparent simplicity and elegance of the backpropagation learning
*  rule, it seems quite implausible that something like equations are computed in the cortex.
*  And that's from 1989, I believe.
*  And the main reason that you just gave is one of those reasons.
*  Why?
*  There are other reasons as well.
*  I don't know if you want to...
*  There are other reasons as well.
*  So I think that which were pointed by Francis Crick, such as differences between the biological
*  neurons and the neurons in artificial neural networks, as well as particular patterns of
*  connectivity which are expected from this backpropagation networks and the connectivity
*  in the brain.
*  And I have to also admit that I find it surprising that on the kind of sociological level of
*  sociology of science, that backpropagation algorithm has been considered implausible
*  for so long, because in fact, the first biologically plausible implementation of backpropagation
*  algorithm, which is really, really nice and has been proposed in 1996 by Randall O'Reilly,
*  who in fact lives in Colorado, as you do.
*  I hope to interview him sometimes.
*  And so basically, this is a great work.
*  And he provided a first really convincing demonstration how something like backprop
*  could be implemented with just local plasticity rules and local information.
*  And somehow this work hasn't become very well known outside people working with Randall.
*  And I guess it's partly connected with the fact that by 1996, machine learners lost interest
*  in backprop.
*  So this was the time where basically there was a rise of support vector machines and
*  maybe just people didn't consider the questions how you can do backprop so interesting.
*  Yeah, it's interesting.
*  I've heard a few people say that Randall O'Reilly has just been a few steps ahead of everyone
*  else in multiple facets.
*  So maybe he'll get his due pretty soon here.
*  That was back in the connectionism, connectionist days, right?
*  Okay, great.
*  Well, so we're about to dive in a little bit here to the different theories of backpropagation.
*  But when you, let's say when we figure out how this does work in brains, and I should
*  say too, I should ask too, is your interest in backpropagation that it itself is an efficient
*  way of training the network?
*  And so you thought, ah, there must be evolutionary pressure on the brain to do something like
*  this?
*  Was it your efficiency flag that went up or what?
*  No, so okay, so the story why we started to work on this problem was more coincidental.
*  So I've been interested for some time in this free energy networks and how they can be involved
*  in decision making.
*  And then there was a seminar in Oxford given by Jeff Hinton, who basically talked about
*  deep learning and some of his ideas how deep learning could be implemented.
*  And maybe that there was some backpropagation of information going through connections in
*  the neurons.
*  And during this talk, my colleague, Tim Barrens asked a question that, you know, there are
*  all this backward connection in the brain and there are all these neurons representing
*  else surely you could do backprop with this kind of models which describe this.
*  And then after hearing this question and have hearing this gush to the seminar together
*  with my graduate student, James Whithington, we thought that, well, we are working on this
*  free energy networks.
*  Can they actually approximate backprop?
*  And we were just got really excited.
*  And for a few weeks, we bounced with ideas and indeed convinced ourselves that they indeed
*  do something like backprop.
*  So this is kind of the way how we started to work on this.
*  That's interesting.
*  How similar do you think when we figure out how quote unquote works in the brain, how
*  similar to actual backpropagation do you think that it's going to look?
*  OK, that's a very interesting question.
*  So I think that all the models which have been proposed of our machine, most of the
*  models don't implement even physically backpropagation.
*  They just approximate it.
*  Right. So even our predictive coding model on that basically implements backprop in the
*  limit of certain parameters converging to some unusual limits.
*  So all the all the most approximate backprop and they perform learning, which is
*  fulfilling also different goals.
*  So they are not just doing supervised learning.
*  They are trying to fulfill other goals like reinforcement learning or unsupervised
*  learning. So you want to have a network which is able to perform both supervised,
*  unsupervised learning and reinforcement learning at the same time.
*  And that's that's a very interesting question to what extent this network will be
*  similar to backprop.
*  Yeah, I mean, we can we can probably talk a bit more about it later after we talk about
*  the different theories.
*  I mean, so you talked about the question that Tim asked and Tim Behrens has been on the
*  show as well. And he it makes me think, you know, the brain is such a beautiful mess.
*  There are so many different ways that you could get to backprop.
*  But like you said, under the under lots of various constraints and there's such a vast
*  array of neurons and circuitry and a vast array of constraint possibilities that you
*  could implement that it's almost let me let me phrase it this way.
*  When we figure out how something like backpropagation is approximated in the brain,
*  do you do you think that people like the neural network people are going to say,
*  ah, see, we came up with this and we knew how brains work.
*  And the neuroscientists and neuroscientist modelers just followed our lead.
*  And so you should now we should take the reins here as as AI theorists.
*  Who's going to get credit for this?
*  Raffel, who's going to get credit?
*  That's that's an interesting question.
*  So just maybe first to answer the first part of the question.
*  So I think that when we figure out how the brain works, eventually, this solution will
*  also look slightly different for different parts of the brain.
*  Yes. So the brain is not very uniform.
*  And maybe the solution for cortex, for hippocampus, for basal ganglia, for cerebellum
*  will look slightly differently.
*  So there will be just not one uniform solution.
*  Well, who will take credit?
*  I think this is a distributed effort.
*  And I think that both neuroscientists and machine learners can influence each other
*  and inspire each other.
*  The correct answer was our current United States President Trump will take credit.
*  OK, OK, moving along.
*  Theories of error back propagation in the brain is a really nice review that you wrote
*  with is it James Whittington?
*  Yes, James Whittington.
*  So let's get into this. So what are some of the guiding principles to help us evaluate
*  what a good model would even look like of back propagation in the brain?
*  So I think that there are two sets of these principles.
*  The first are connected with efficiency.
*  So we want models which actually can work, which can actually learn some benchmark
*  task, which we humans are able to learn or our visual systems are able to learn.
*  So, you know, several models have been proposed in the past, which are biologically
*  plausible and quite simple, but maybe they don't scale very well for larger problems
*  and are unable to learn even this kind of benchmark problems like classification of
*  written handwritten digits.
*  Right. So efficiency is one set.
*  But there's also a second set of constraints connected with biological plausibility.
*  So I think that at the first instance and the first approach, we want to see models
*  which are able to perform local computations.
*  So the other neurons just get information from other neurons and all the synaptic
*  weights are just modified on the basis of information provided by the neurons they
*  connect and maybe some one global signal which could be encoded by neuromodulators.
*  We want the networks which work autonomously where you don't have to have a little
*  homunculus which rewires networks in different phases in different ways.
*  And we want to have a network which have their architectures, the pattern of
*  connectivity, which are similar to those seen in the brain.
*  And I think I think that this is the kind of the first step.
*  And then, you know, once we identify these kind of candidates, I think the real fun
*  will start when we try to map these networks on the details of the biologic.
*  So, you know, long term in the next maybe five to 20 years, you would like to be able
*  to take these networks which have been proposed and map them on the actual neural
*  circuits on the actual anatomically known populations.
*  Are we going to end up with models that look that just replicate brains?
*  You know, what's the limit of where where are we going to stop and say, OK, this is
*  good enough? We can defer.
*  No, I think it's a very interesting, very interesting question.
*  And, you know, it's connected with a question.
*  And what insights from neuroscience machine learning should take on board is.
*  So, as you know, it has been proposing computational neuroscience that the models
*  can be built on different levels.
*  So there are these three levels of MAR, the computational algorithmic and
*  implementation levels.
*  And I think that you can describe the computations of the learning networks in
*  the brain in the form of the computation performance, the form of the algorithm and
*  form of the detailed implementation.
*  And for different people, different levels are interesting.
*  So if you really want to understand just the overall algorithm, maybe you don't
*  want to dive into the algorithm, into the details of the biology.
*  But I think for neuroscientists, it's really important to understand what is actually
*  the function of the different subtypes of neurons they they observe under the
*  microscopes and records from.
*  Right. Yeah, OK.
*  I'm sorry, I keep derailing us with these sort of broader, broader pictures here.
*  Fascinating questions.
*  So in the paper, you really separate two main categories of models that try to
*  tackle this modeling back propagation in the brain, temporal error models and
*  explicit error models.
*  And, of course, as you note in the paper, these aren't the only kinds of models
*  that exist, but these are just the ones that you focus on in the paper.
*  So maybe you can just walk us through in broad terms what a temporal error model
*  is and what an explicit error model is and how they differ.
*  So the temporal error models represent errors as the difference in activity in
*  time. So they would have an architecture which, in addition to feed forward
*  connections, which are present in standard artificial neural networks, also
*  have feedback connections.
*  And because the network is recurrent, they are described by a set of differential
*  equations which describe the evolution of these neuron like nodes across time.
*  And the key insight of the temporal error models is that you can essentially
*  separate the error as a difference in activities across time.
*  So the error is defined as the difference between activity which you want the
*  neuron to produce and the activity the neurons actually produce.
*  So you can basically, instead of changing the synaptic weights proportionally to
*  the error, you can modify them twice.
*  Once with the target present and once without the target.
*  So when the target is present, you modify proportionally to the activity the
*  network should have produced.
*  And when the target is not present, you modify them in a way inversely proportional
*  to the activity the network actually produced.
*  So it's like a two-step process.
*  Yes, you have a two-step process.
*  You first unlearn existing association between the input and output and then you
*  learn the new association.
*  So basically, in terms of its implementation, these models predict that you would have
*  neural synaptic weights which are modified twice during learning.
*  Once in a way which is inversely proportional to the activity, which neuroscience
*  would be called anti-hebium.
*  And then when the target is provided, they are modified in a way which is
*  proportional to the activity, which would be called Hebium.
*  And what's kind of really appealing about this temporal error models is that they
*  are very simple and they have very simple plasticity tool and very simple dynamics.
*  But they have a drawback that they require a control signal which tells the network
*  in which phase of activity it is.
*  Is it the phase without the target present or the phase with target?
*  Because in different phases, the rules of the plasticity should be different.
*  And you may also even have a problem that maybe the target never arrives.
*  It's not an intuitive way to me of thinking about it.
*  Yes. So basically, it has been proposed by Randall and others that maybe this solution
*  for this problem of this phases could be provided by oscillatory rhythms.
*  So in a certain parts of the brain, like in the hippocampus, you have this very strong
*  oscillations and maybe in one phase of the oscillation, you don't provide the target
*  pattern in another you do.
*  And then you can control the plasticity according to the phase of those oscillations.
*  But there's no there's no clear evidence that such phases exist in other parts of the
*  brain. So therefore, it's also interesting to consider the other type of models, which
*  are the explicit error models.
*  And the explicit error models would have slightly more complicated network architecture,
*  which will include some additional elements which represent the errors explicitly.
*  That's OK, because the brain is complicated.
*  Yes.
*  Maybe we could just talk about a couple of the examples of the explicit error models.
*  So I had Blake Richards on the show kind of early on.
*  So it was a long, long time podcast wise now.
*  But so we talked about his work and others work using apical dendrites to model the
*  error explicitly in a neuron.
*  And basically, the way that this work works is you have a neuron and it has these basal
*  dendrites, this big net that projects pretty locally to the neuron body.
*  And it's receiving inputs from one region of the brain and local feedback connections.
*  And then you have this long extending apical dendrite that extends up into different layers
*  of the brain and is receiving input from different regions.
*  And because of the separation of the dendrite from the neuron cell body, it can perform
*  different computations of these incoming signals and lead to different properties,
*  different plasticity changes in the way that that neuron fires.
*  I think that's the general gist of it.
*  Is there anything to add to that sort of model, the dendritic model?
*  Yes, so this is a very good description of how the network, how a single neuron works.
*  And then there's an interesting question on how you connect this kind of neurons into
*  a multilayer networks and how they communicate with each other.
*  And I think that a very nice answer to this question has been provided by a model to
*  which I refer as dendritic error model, which was developed by Joa Sacramento and Walter
*  Sen, where they proposed a particular architecture of the network.
*  So this network is organized into a layer, into layers.
*  And within each layer, the apical dendrite will calculate the error and it calculates
*  the error as the difference between the feedback from the layer above and the local prediction
*  of what this feedback should be, which is generated by a network of interneurons.
*  So there's a network of interneurons which kind of generates a prediction what the feedback
*  should be given from the layer above.
*  And this prediction is compared with the actual feedback given to the apical dendrite
*  in the apical dendrite itself.
*  And then when this prediction is high, then this activity in the apical dendrite can drive
*  plasticity in the network.
*  And this will closely approximate the propagation.
*  So what we point out in this review paper in Trans in Cognitive Science is that this
*  dendritic error network is closely related to predictive coding network.
*  So it has lots of similarities in a sense that it also has a separate representation
*  of error as explicit in this case dendrites, not the error nodes.
*  And in fact, we show that you can essentially rewrite the mathematical equation describing
*  predictive coding in a different equivalent way.
*  And this different equivalent way can be mapped on this dendritic error model.
*  So this dendritic error model could be viewed as an alternative way of implementing the
*  computation of the predictive coding networks.
*  The predictive coding network that you're talking about is one that you actually worked
*  on and the other one that you describe in the paper.
*  So you already described what predictive coding is and the free energy principle.
*  Maybe you can describe a little bit the model that you made and how predictive coding
*  without these constraints can be used to approximate backpropagation.
*  OK, so as I mentioned just a few minutes ago, predictive coding networks also have this
*  hierarchical organization.
*  And in each level of hierarchy, you have two types of neurons, neurons encoding the
*  predictions and neurons encoding the errors.
*  And they essentially communicate with each other through the neurons and coding errors.
*  And in the original work of Rayan Balard, the predictive coding networks were developed
*  for unsupervised learning.
*  So what Rayan Balard tried to do is they demonstrated that these networks can be used
*  to learn the representation of visual stimuli.
*  So you can learn, the network can learn to predict what features are present in visual
*  stimuli and build a representation of this.
*  So these models were used for unsupervised learning.
*  So what James Whittington and I realized is that although these models are actually very
*  old and they were developed in 1989, nobody has tried to use them for supervised learning.
*  And if you take these networks and instead of just constraining them on one end, on the
*  kind of bottom level of the sample, you also constrain them on the top level.
*  These networks very closely approximate backpropagation algorithm.
*  So basically, these networks have the property that when you just constrain the top level
*  and let the network predict its output, it will generate exactly the same pattern of
*  activity as artificial neural network with equivalent weights.
*  By contrast, if you constrain both ends of this network, both the one end and the other
*  end, and let the network relax, then the network will modify its connections in exactly the
*  same way as in artificial neural networks.
*  So that's the rule for the weight modification in predictive coding is that weight modification
*  is proportional to this prediction errors.
*  And when you just provide the pattern on one end of these networks, this pattern will
*  propagate and because the other end is unconstrained, all the prediction errors will converge
*  to zero. So there will be no weight modification.
*  While when you constrain both ends of this network, these prediction errors don't have
*  freedom to decay to zero.
*  So there are some errors which cannot be explained and these errors lead to weight
*  modification. So what is particularly appealing about these predictive coding networks is
*  that they work in a completely autonomous way.
*  So you don't have any control.
*  You don't have to specify in which phase they are.
*  You just provide patterns.
*  And if you just provide pattern on one end, the network will make a prediction.
*  If you provide patterns on two ends, the network will essentially learn to associate
*  them.
*  So, Rafał, are we going to have to wait until we have nanoparticles embedded in all of our
*  neurons and can record from every neuron simultaneously and somehow analyze that data to
*  really determine which of these models is the better candidate and how back propagation
*  actually works? Or how can we determine this stuff experimentally right now?
*  You know, so the models make different experimental predictions.
*  And I think that these predictions could be roughly grouped in two classes.
*  So they make predictions about the activity and how the activity of neurons depend on
*  errors in the network or surprise in the stimuli.
*  So the predictive coding models assume that there are neurons which explicitly encode
*  errors. The dendritic error models assume that the errors are encoded in dendrites and
*  neurons will produce bursts of spikes when the errors are present, while the temporal
*  error models do not actually make any explicit prediction of neurons increasing their
*  activity with error.
*  And as I mentioned before, there is evidence that at least in some brain areas, there are
*  neurons which clearly encode errors or increase the activity with errors.
*  And then the second class of predictions are connected with plasticity.
*  So different models predict different types of plasticity.
*  So, for example, this contrastive learning, this temporal model, which I described, makes
*  this prediction that the sign of plasticity should be different depending whether the
*  target pattern is present or not.
*  Or if you think that this is implemented in a neural oscillation on the face of the neural
*  oscillation. And indeed, there is some evidence suggesting that the sign of the plasticity
*  in the hippocampus depends on the face of the theta cycle.
*  Also, these different models, and I think that we go through this in detail in our
*  Trans-Cognitive Science review, that different models make different predictions on the
*  type of the spike time dependent plasticity.
*  And what we see is that different models would predict different types of spike time
*  dependent plasticity. But as I mentioned at the beginning, different types of synapses in
*  the brain actually exhibit different types of spike time dependent plasticity.
*  So there is a big variety.
*  So it's not if you just look at the existing data, it doesn't seem that, you know, there
*  is just one model which is most consistent with all data.
*  It seems that all these kind of models are consistent with some pieces of data which
*  have been proposed. So, you know, maybe one way of thinking about this is not that we
*  have to look for one model.
*  Maybe these models are not just competing theories, but maybe they are just describing
*  different motives which are combined by the brain.
*  So you can imagine that different parts of the brain will be better described by
*  different models which are kind of specialized for different operations.
*  And maybe some parts of the brain will combine different models together.
*  Yeah, you guys talk about in the paper, I mean, you basically admit, look, the brain
*  is really complicated and there's room for all of this diversity in these different
*  ways of doing it, as you were just saying.
*  So I meant to say that up at the top, but you just said it for me.
*  So thanks. So what do you think are the I mean, do you really think that it's going
*  to turn out that way, that there are going to be different ways of implementing this
*  in different brain areas and some areas that implement them together?
*  You know, what what is your outlook or opinion?
*  I mean, I know that these are very speculative things.
*  Yes. So I think that's exactly my way my thinking at the moment.
*  So, for example, the temporal models have this advantage of simplicity, but they have
*  this kind of drawback that they require this information, whether the target pattern is
*  present or not. So they may be particularly suitable to describe information processing
*  in the brain areas, which make predictions for the future where the target pattern
*  always arrives. For example, like the hippocampus is very well known to deal with
*  space. So maybe it's trying to predict where will I end up in the next time frame.
*  So this information about the next time frame always arrives.
*  Now, maybe the explicit error models are more suitable for for tasks where the target
*  presence is uncertain in time, such as, for example, learning about the rewards or
*  outcomes of different events and even different types of explicit models have different
*  tradeoffs among them. So I think that we talk a little bit about this in the paper that
*  the drawback of the predictive coding models is that they are actually slow to propagate
*  because in the predictive coding model, you have to propagate information via error neurons.
*  So you have like twice as many synapses to transmit information as you actually have
*  layers in the artificial neural networks. So these networks are slow.
*  But this is the knock on brains from computer scientists is how slow they are. But come
*  on, it's parallel so we can do it all in parallel. So it's relatively fast and efficient,
*  even so. Right.
*  Yes. Yes. But even even though you do a lot of computation in parallel, you still have
*  computation in the predictive coding network which has to go through the layers. Right.
*  From layer to layer, you have to go via this error nodes in the predictive coding
*  architecture, which basically introduces delays.
*  But on the other hand, the dendritic error networks have this drawback that they have
*  this additional network which generates local predictions of the top down input.
*  And these networks have to be pre trained.
*  So so basically you need a little bit.
*  So the predictive coding networks are slower to propagate information, but faster to
*  train while the dendritic errors networks may be faster to propagate by slower to train.
*  So basically by merging the two types of networks in the cortical circles, you can
*  essentially beat the trade off and maybe initially use the predictive coding networks to
*  learn fast and then kind of consolidate this information with time in this dendritic error
*  models to allow faster information processing.
*  But that's different than having a control signal which tells the system which learning
*  strategy to use at different times.
*  Right. Because they're kind of working in accordance with each other.
*  Yes. So of course, there's a non trivial questions how you actually integrate and how
*  you build this kind of combined models.
*  Also in the paper, we point out that, you know, it may seem a little bit daunting and
*  depressing that there is this big diversity of the brain and big diversity of the most.
*  So we review four models in the paper, which on the first side look very different.
*  You use different network architectures, different plasticity.
*  But we also point out that what's really nice that there's this one mathematical framework
*  called equilibrium propagation in which all these models can be described.
*  So all these models can be described in a framework which considers networks, which
*  during their evolution minimize an energy function.
*  And this framework prescribes how synaptic waves should be modified in this kind of
*  models. And remarkably, all these different models actually follow this framework.
*  So although they are very different, they have like a common mathematical description.
*  Yeah, it's beautiful.
*  Yes, so I should say that framework was developed by Benjamin Sellier and Joshua Benjo.
*  And I think it's really important because it can essentially give you a recipe how to
*  modify synaptic waves in any network which has dynamics, which optimizes energy.
*  And so what is meant by optimizes energy is that when you have a network which during
*  the evolution will converge to some equilibrium and it can describe this equilibrium in a
*  way in a function which is minimizing this equilibrium, this network will fall into
*  this framework.
*  And so the sorry, the equilibrium is just a minimal energy level.
*  Exactly. Equilibrium is the minimum energy level.
*  And so I think that this framework could be used to basically drive the research on the
*  mapping of this deep learning architectures on the brain.
*  So, for example, you can have a candidate model which is based on the anatomy of the
*  brain circuits. And for this candidate model, you can figure out what would be the
*  corresponding energy function and then use this framework to suggest the synaptic
*  plasticity rules. And then you can compare the synaptic plasticity rules to the rules which
*  are actually found in these cortical networks.
*  And then through this iterative process, you can essentially refine the models.
*  So it's really nice that, you know, in addition to this kind of abundance and complexity,
*  there's this nice, simple and general principle which kind of can describe the learning
*  rules in all these models.
*  Yeah, that really is nice.
*  What do you think is the one of the biggest hurdles right now to figuring this stuff out in
*  the brain? Is it just the diversity like we were just talking about, even though the
*  equilibrium principle, you know, brings it all into one form?
*  But what do you view as maybe the biggest hurdle to figuring out how back propagation
*  might happen in the brain?
*  So I think that, as I mentioned before, maybe the question should be how the propagation
*  is implemented in a particular part of the brain.
*  Maybe we should not think about this as a kind of general algorithm, which will be the
*  same in all different systems.
*  Yeah.
*  Start with systems.
*  So I personally really like the Basal Gambia, as I mentioned before, which is a relatively
*  simple brain circuit, which has performs a quite complex function, like action selection
*  and learning about the rewards.
*  And it has also a hierarchical organization.
*  It's kind of organized in several loops, which go from more abstract to most motor.
*  And this is an example of the system where we know the anatomy very well.
*  We know very well what are the key neurons, how they are connected.
*  And of course, we don't know all the details, but we have that big picture.
*  And this is the place where we can essentially already now, I think, try to do this mapping
*  of the algorithm on the structure.
*  And I think that it would take maybe slightly more to do similar mapping in more
*  evolutionary newer areas, like the neural cortex, which are more complex.
*  So, you know, the truth is that we still don't understand the neurobiology and anatomy
*  and physiology of this different structure.
*  So we know that there's this anatomy with the six layers, but we don't understand the
*  response properties of this, you know, to the extent, for example, we understand in
*  the Basal Gambia. So great progress is being made in this respect.
*  So there's great work by George Keller, for example, in Switzerland, who describes the
*  neurons responding to errors and to unexpected violation of expectations in the cortex
*  and how this responses arrives.
*  And I think that thanks to the new tools of neuroscience, like the optical imaging and
*  tools allowing manipulation of the circuits, we will get this picture very soon, which
*  will allow us to do this mapping.
*  So I'm optimistic. And I think that probably we will.
*  Well, I just submitted a grant proposing that we will crack this Basal Gambia within five
*  years. And in case any reviewers are listening, I'm sticking to this.
*  But, you know, it will probably take slightly more for the cortex.
*  Well, when you get your grant reviews, we'll see how optimistic you are then.
*  Yes.
*  But it's interesting because everyone is in love these days with the cortex and and
*  compares deep learning to different areas in cortex.
*  And no one in the AI world really talks about, you know, even on the that straddles the
*  AI and neuroscience world really pays much attention to subcortical areas, however, and
*  to older regions of the brain.
*  But it really might be some of these regions.
*  And I know that areas like the cerebellum, like the basal ganglia, like you were just
*  talking about, even like hippocampal structures, which I guess is technically cortex, but
*  older and lower, that these might really be the major players, these older regions in
*  implementing different aspects, different ways of implementing different kinds of back
*  propagation like learning in the brain.
*  So I don't know if you want to comment on that.
*  Yeah, I fully agree.
*  Of course, the cortex is fascinating because of the area which makes us special.
*  Yes, make us special. Yes.
*  So we want to understand it.
*  But there are these other areas.
*  And so I talked a lot about the basal ganglia, but cerebellum is another really, really
*  interesting area. And what's special about cerebellum is that in cerebellum, there are
*  special neurons which encode errors and which basically for each Purkinje cell, which is
*  the main neuron in cerebellum, there exists a corresponding neuron encoding errors.
*  And this neuron sends an accent just to this one Purkinje cell and to its associated
*  interneurons. So basically, it's a system where you can see this kind of like representation
*  of, separate representation of neurons making predictions and neuron generating errors,
*  which is, for example, present in these predictive coding networks.
*  Yeah. Well, that's I think one of the reasons why subcortical structures in general and
*  older structures in general might be of interest is because they're so conserved and the
*  motifs, the circuitry is much more straightforward in many cases.
*  So you can really make crisper predictions, perhaps, and see how it will actually turn
*  out.
*  Yeah, exactly. So, you know, our basal ganglias have exactly the same anatomy as the basal
*  ganglia of fish. So it hasn't changed much through evolution.
*  So if you have a part of the brain which hasn't changed for so long, it probably suggests
*  that, you know, it's doing something really useful.
*  It's kind of optimized in a very good way.
*  So for the listeners who can't see Raffel, but every time he says basal ganglia, I actually
*  see his gums. He smiles so wide that I see his gums every time.
*  So I don't know if that comes through in the audio.
*  Well, Raffel, do you think that like solving how the brain implements approximate back
*  propagation, do you think that that will actually improve our AI systems, our deep networks
*  and other AI systems?
*  So when I was an undergraduate studying computer science, my view was definitely yes.
*  And then I remember I had this great conversation with my project advisor, Professor Christophe
*  Jurek-Carrier, who told me this old story about taking inspiration in artificial intelligence
*  from nature is similar to taking inspiration when people were building airplanes.
*  So when people were building airplanes, they noticed that, you know, there are these creatures
*  which fly, birds, and they have wings.
*  And it's probably really great to add wings to airplanes.
*  And this is really great insight.
*  But then they notice also the birds flap wings and the airplanes try to flap wings.
*  And this was not such a good engineering solution.
*  You can actually can realize that actually you can build propeller, which is a much
*  simpler solution. And the only reason why birds don't have propellers is that propeller
*  has a disjoint part. So there would be no way to deliver blood to the propeller in case
*  of birds. So, you know, there is an extent to which it's useful to take inspiration from
*  nature. And maybe it's useful to take inspiration to solve general problems, but not maybe
*  to look at the details of the implementation.
*  And I think the same is with artificial intelligence.
*  I think that there are still some areas where we still need inspiration from the brain,
*  like the autonomy of artificial agents.
*  But maybe we shouldn't look at details of the implementation.
*  So I mentioned this kind of like more levels of implementation.
*  I think it's really nice to take the inspiration from the computations made by the brain and
*  the algorithms it uses.
*  But maybe the things which excite me, like the anatomy of the strata circles and the
*  rules of the synaptic plasticity are not so relevant.
*  So in your analogy, I suppose back propagation would be the propeller solution to deep
*  neural networks, whereas our brains would be the flapping wings.
*  Exactly. Was that?
*  Yes.
*  Oh, thank God I got it right.
*  Yeah, that's a really nice analogy, actually.
*  OK, so you have the solution back propagation, right?
*  And now you have all these neuroscientists and theorists like yourself.
*  And this is not a knock on you or anyone doing this work, but who are seeing, OK, this is
*  great. It works really efficiently.
*  Let's see how this happens in the brain.
*  Do you think that that's taking too seriously the implementation in artificial systems and
*  applying it to brains or maybe not seriously enough?
*  Do you think that neuroscientists and computational neuroscientists in general are taking
*  these AI developments too seriously or maybe even not seriously enough?
*  So I think that there is a big need for the theory in neuroscience.
*  So there's there's need for experimentation.
*  Theories are everywhere.
*  The experimenters are trying to keep up.
*  Sorry to interrupt.
*  Well, you could say this.
*  But, you know, if you go to the meeting of the Society of Neuroscience and you look at
*  a fraction of posters are theoretical, it's just a tiny fraction of the sea of posters.
*  And I think that neuroscience is a very young area.
*  I think it's still pre-Newtonian.
*  So we are still lacking the fundamental principle.
*  So we understand very well how single neuron works, but we do not understand very well
*  what are the general principle guiding information processing in the brain.
*  And I think that theoretical work and in particular, theoretical work inspired by deep
*  learning can really provide a guiding guidance in discovering these fundamental principles
*  of learning in the brain.
*  So you you've done a lot of decision making work and you've recently, you know, had this
*  free energy principle push.
*  When you get an idea as a model or as a theorist, how long do you chew on it before you
*  actually start working on it?
*  Do you like get out of the shower and immediately start modeling it or do you dry off first
*  and maybe think about it for a few months?
*  Yes, I think that.
*  I know it's in between there.
*  Yes, I know. I think that I really jump on the ideas.
*  I think that my wife would say that I make notes in very unusual moments sometimes and
*  just jump out and just we have to say I have to make note of this and and just struggle.
*  Yeah, I think that when you have an idea, you don't really know if this idea works or
*  not until you try it.
*  And one amazing thing about computational neuroscience is that you can try out ideas
*  very quickly, that you can see if a particular model is correct by simulating it and seeing
*  what it does within minutes or hours.
*  I know that you work with like a man in your physiology where it takes really months to
*  basically get results.
*  So this is the appeal of the theoretical work.
*  Yes, I agree.
*  And as you see, I'm retired, so I'm no longer doing that.
*  So it's drove me out, man.
*  It drove me out.
*  But, you know, in business, like in startups and tech startups as well, you know, there's
*  this mantra of failing fast and breaking things, fail forward and this bias toward
*  action. Right.
*  And on the on the theoretical side and on the experimental side and, you know, the
*  academic side, you know, I wonder where that balance really is best between carefully
*  thinking out and planning and just trying stuff.
*  And it's easier. One of my colleagues, when I was doing monkey neurophysiology, he came
*  for a stint in our lab and he also did human EEG work.
*  And I hated him.
*  I mean, he's a great guy, but I hated him because in one day he could pilot an experiment
*  and then just figure out whether it's worth pursuing anyway.
*  All right. I'm done. Done ranting here.
*  So as a theorist and you having these ideas, I mean, do you have ideas that you could
*  pass on? Like, what's one idea that you maybe don't have the resources or the focus or
*  funds, you know, even to do that you think that someone else should be doing right now?
*  Thank you for this question.
*  So, yes, so in fact, for example, in this paper, our review in Transcognitive
*  Science, we compare several models of deep learning implementation in the brain.
*  But I think there's a need for someone to thoroughly compare them in simulation.
*  So each author of each of this model simulated the model on a benchmark task, but the
*  simulation was done in a different way.
*  And, you know, we try to kind of compare the learning times and accuracy of these
*  models, but, you know, they are really not comparable.
*  So it would be really great for I think this is a need in this in this in this field to
*  compare formally this different implementation of deep learning, how well they are doing
*  in terms of their accuracy and in terms of their simulation time and training time.
*  And of course, this shouldn't be done by me or any of the other authors of this model
*  to be unbiased. So I think that it would be really great if someone, maybe of the
*  listeners, would like to take this challenge and just bring this comparison to the field.
*  That's a great idea, because it's very straightforward and doable.
*  Yes. And another thing is that so I mentioned that I'm particularly interested in the
*  moment on trying to map this deep learning algorithm on the base of Algania, because
*  this is the area which I've been working on for the last 15 years.
*  But there are also other areas of the brain which are relatively well understood.
*  And I think that the next really interesting candidate is the hippocampus, where, you
*  know, we know quite well about the organization and physiology and properties of
*  So I think it will be really interesting to see how you can map any of these
*  algorithms or maybe the combination on the hippocampal system.
*  OK, great. Man, two very worthy projects there.
*  Hippocampus is really hot right now in, you know, talking to Tim Behrens recently and,
*  you know, of course, all the place cell work.
*  So, all right. That's great.
*  So we talked about a little bit about this before, but I just want to get your opinion.
*  If you have like a specific thought where AI and or AI in general and or deep networks
*  are most lacking with respect to incorporating what we know about brains.
*  So I think that maybe the one such area is that is autonomy.
*  So, you know, when you have these deep networks, you have to train them.
*  You essentially have to provide a lot of assistance to them.
*  And, you know, we as humans know what to do by ourselves.
*  So we make our decisions as agents just to satisfy our needs.
*  We have different needs in different time.
*  So it's really interesting to take inspiration from this and try to see if you can develop
*  artificial systems, which can also make decisions to satisfy the needs.
*  And one such need is the need of knowledge.
*  So, you know, we actually learn typically to achieve our goals.
*  So so in nature, we are learning not just to, you know, increase particular level of
*  accuracy in the training set. We were learning to survive.
*  And, you know, maybe in our in our modern life, you even create contingencies where,
*  you know, learning is required to achieve certain goals.
*  So, for example, my son really wants a BMX bike, but I set him a target on some mark
*  from the school he needs to achieve in order to get his BMX bike.
*  So essentially, he has to do this secondary supervised learning and memorize all these
*  facts in order to achieve his goals.
*  So I think that it's really important how you how you build systems, which actually
*  work autonomously in the world and trying to extract information just to realize their
*  goals. But so that sounds like steps towards general AI almost.
*  I mean, does that does that relate?
*  Yeah, I think it's closely related.
*  Yes, because, you know, you know, all the all the organized are really trying to find
*  ways to solve their various problems they are faced with.
*  Good. Well, let's flip the question around.
*  And I think I know maybe one or two words that you'll use when you answer this.
*  I think you'll use maybe I'm just going to guess here and then you can intentionally
*  not use these words if you can.
*  I'm going to say the words efficiency and optimal or optimization.
*  So the question then is, is, you know, where is neuroscience most lacking with respect
*  to incorporating principles that have been learned from AI work?
*  Yes, so I think that you're absolutely right.
*  So this is yes, I can satisfy your reduce the prediction error.
*  Right. And yeah, right.
*  Right. So, yes, definitely, definitely.
*  There, you know, the minimum of the models which have been developed for the brain are
*  not as efficient as artificial neural networks.
*  So it will be definitely a really great source of inspiration, all the technology which
*  have been developed in deep learning.
*  One such example, I think, is work in deep learning, which have been done to make
*  predictions in time and use time.
*  So most of the models of biological backprop have been developed for static input
*  patterns and static. But of course, we as living organist have to make our decisions
*  on the basis of the sequences of inputs such as speech.
*  We have to classify speech and we have to generate sequences of outputs such as our
*  movements. So it's really interesting to understand how this could be done efficiently.
*  And of course, in machine learning, we have various tools like long, short term memories.
*  And there's a lot of kind of interest how things like this could be approximated in
*  neural circuits. So I think this would be a particularly interesting insight on how we
*  can achieve the efficiency seen in the deep systems.
*  I just talked to Francisco de Saoza Weber and he actually runs a startup called
*  Coracle IO where he implements natural language processing in kind of a different way
*  with these sparse distributed representations.
*  But that does it in time, can take text over time essentially.
*  And this is based off of work that Jeff Hawkins has done modeling our neocortex.
*  And he specifically incorporates time into his networks.
*  And it's different than a deep learning approach, but it's along those same lines.
*  So that's interesting.
*  Rafał, do you have a favorite general theory of brain functioning?
*  You know, is it the free energy principle that is that your favorite?
*  I will not disappoint you. Yes.
*  So, so, yes, I'm a big fan of the energy principle developed by Carl Christon.
*  And I think it's really fascinating because it provides a description of how the brain
*  implements very efficient computation, how the brain implements Bayesian inference,
*  but also describes it, how it can be done in a biologically plausible way in a network
*  of simple elements which look like neurons, which interact with each other.
*  So it's a kind of what's really beautiful about this free energy principle, that it
*  combines the efficiency of computation with biological plausibility.
*  And you don't think that there go ahead. I'm sorry.
*  And, you know, Carl has Carl Christon has proposed that, you know, it can be applied
*  to many different computational computations in the brain, not just to perceptions, but
*  also to, you know, to action selection and so on.
*  So I think, you know, he has promoted this as a general principle and I'm I also see it this way.
*  So one of the knocks on the free energy principle, from what I understand, is that you can
*  almost accomplish anything, but every different thing that you accomplish has a large number of
*  distinct constraints that you need, distinct assumptions that you need to make to accomplish
*  any one given thing. Right.
*  So there aren't the same assumptions that encompass everything to accomplish multiple tasks.
*  Does that make sense?
*  Yes. So I think that was really interesting in this principle is that depending what
*  assumptions you make about the distributions in the probabilistic model or about values
*  priors, these different assumptions can give you different networks.
*  And, you know, of course, what you have, you have different parts of the brain which try to
*  realize different function.
*  And I think it will be really interesting to see whether you can explain the differences in the
*  anatomy of different parts of the brain in the different priors or assumptions put inside
*  this free energy model.
*  They could map directly on.
*  That's yeah, that's really interesting.
*  Okay, so just a couple more questions here and I'll let you go.
*  But what is something that that is potentially crazy that that you believe that we'll learn
*  about our brains and or minds moving forward?
*  So as I mentioned, I'm a big fan of the free energy principle.
*  And one aspect of this free energy principle, which really sounds crazy, is an extension
*  called active inference.
*  So what active inference says is the following.
*  So in general, the free energy principle could be viewed as saying that the brain is trying
*  to minimize its surprise.
*  So it's minimize the difference between what you see and what you expect to see.
*  And the active inference says that the brain is using two ways to minimize the surprise.
*  So you can either change your expectations to match your stimuli if you are if you have
*  mismatch and this corresponds to perception and learning.
*  But you can also do minimize the surprise in a different way, namely by changing the
*  world to match your expectations.
*  So this would correspond to action.
*  And this may sound really crazy why you would basically minimize expectation by changing
*  the world. But what Carl proposed is that there are some expectations which should not
*  be changed by evolution, should not be.
*  So you should not be changed through learning, for example, an expectation that my food
*  reserves on certain level.
*  And if such expectations are not satisfied, then the brain finds a way to satisfy them
*  by getting food.
*  And I think this sounds like a really crazy principle, but I think that it may turn out
*  to be a correct description of how we select actions.
*  It really is in line also with people like Daniel Wohlpert's ideas that movement is the
*  basis of all of our cognition anyway.
*  So it makes a bit of sense that that active inference idea of changing the world and
*  taking action to make the predictions match your expectations fits in that realm, too.
*  So that's a really interesting approach, I think.
*  Yes, I like that idea.
*  Connected with the work of Matt Botfinick on planning as interest.
*  And so I think he also proposed that when you see that the world is available, you take
*  the reward as premise and you try to infer what actions you should take to get it.
*  And you think the law of future research is going to be based on this principle that
*  that's the principle that drives us?
*  Yes. Yes. So this is my five year grant, which I mentioned before.
*  Yeah, great. Well, lastly, thinking about the broad swath of what there is available
*  to do right now, you're kind of deep into it.
*  You're writing grants. You know, you have this Basel Ganglia project as well.
*  And but if you were just if you think back, if you were just starting off right now,
*  think back. I know you haven't made any mistakes, but all the mistakes that you've made.
*  No, no mistakes. You know, what how would you proceed?
*  Well, how would you get into this field of that straddles both neuroscience and AI?
*  What advice would you give?
*  So that's of like research direction.
*  So I mentioned that, you know, I'm interested in this kind of subculture areas, which are
*  simple and I kind of know a lot about them.
*  But I think that time becomes ripe now to try to address the hard question of the cortical
*  circuits. So I think it's, you know, thanks to this new technologies of optical imaging
*  and circuit manipulation, we will soon have enough information to really try to understand
*  this cortical circle. So I will be, you know, still staying in the Basel Ganglia, which
*  my colleague Pete McGill's calls the basements of the brain.
*  But I think that, you know, the really interesting final frontier is the cortex.
*  And I think this is the place where it would be really interesting to try to map this
*  algorithm on the six layers of the no cortex.
*  And I hope that, you know, before not too long, someone will be able to do this.
*  Well, Raffel, this has been really fun and I really appreciate your time.
*  So I'll point people to that review paper and trends in cognitive science and some of
*  the other work that we talked about.
*  Thanks again. And really good luck on the five year grant.
*  I wish you the best.
*  Thank you very much.
*  It was pleasure.
*  Brain Inspired is a production of me.
*  You can support the show through Patreon for a trifling two or four dollars per month.
*  Go to Patreon.com slash brain inspired or go to the website brain inspired dot co and
*  find the red Patreon button there.
*  Your contribution will help keep this show going without any annoying advertisements
*  like you hear on other shows.
*  To get in touch with me, email Paul at brain inspired dot co.
*  The music you hear is by the New Year.
*  Find them at the New Year dot net.
*  Thank you for your support.
*  See you next time.

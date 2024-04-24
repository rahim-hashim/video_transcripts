---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3887s
Video Keywords: []
Video Views: 5479
Video Rating: None
---

# BI 010 Adam Marblestone:  Brain Cost Functions
**Brain Inspired:** [October 15, 2018](https://www.youtube.com/watch?v=tcZaFZ2MIHE)
*  See, this is disappointing because I really thought we had the brain all figured out,
*  you know?
*  Yeah.
*  Right.
*  Yeah, exactly.
*  I mean, in a way, some of the essays that we've been writing are just me finding out
*  how little we actually know and what questions you can still ask.
*  Oh, boy.
*  Maybe I do need a shot of whiskey.
*  This is Brain Inspired.
*  Hey, this is Paul Middlebrooks.
*  Well, it's a milestone for the podcast in two ways.
*  First, it's episode 10, so we're in the double digits now, so that's good.
*  And second, I got my first Twitter troll and I had no idea how to respond.
*  I'm a dad, so I'm kind of an expert at getting things wrong.
*  And through that wisdom and other life events every single day, I'm aware how wrong I am
*  all the time.
*  But to get Twitter trolled, that means I'm doing something right.
*  This little podcast is growing and you can help that by giving it a review on iTunes
*  or telling a friend.
*  Thank you in advance for that and thanks for listening.
*  Okay, today I talk with Adam Marblestone.
*  He has a long list of accomplishments, which you'll hear when I introduce him during the
*  show.
*  We talk about his paper, Toward an Integration of Deep Learning and Neuroscience, which gives
*  a broad and thorough outline for how to go about doing just that, integrate deep learning
*  and neuroscience.
*  And of course, I ask Adam some speculative questions toward the end.
*  If you haven't listened to episode 9 with Blake Richards, I recommend you listen to
*  it before this one.
*  We reference Blake's work plenty during our chat, so it'll make more sense if you've listened
*  to that episode.
*  We definitely set a record today for the number of times saying cost function.
*  Just to be clear, I'll state up front here what a cost function is.
*  In machine learning, a cost function is a calculation of the error the network produces
*  with respect to the correct answer.
*  And the cost function is used to train the network, reducing the cost function over time
*  until it's minimized and the network is trained.
*  That is good enough for now, I hope.
*  One more bit of info before we start.
*  There may be a little bit more lingo than usual in this one, but as usual, I link to
*  a bunch of the relevant stuff in the show notes.
*  So if there's something you hear that you don't understand, check out the show notes
*  at braininspired.co.
*  slash podcast slash 10.
*  And now here's our conversation.
*  Adam Marblestone, thank you for gracing the podcast with your presence today.
*  Thank you.
*  Yeah, you label yourself a technologist and you really explored a vast landscape in that
*  arena. So get ready.
*  You're the co-founder of BioBright, a company that aims to create a smart lab to improve
*  biological experimentation.
*  You're chief strategy officer of Kernel, which seeks to build better tools to access, read
*  and write from the human brain.
*  You've helped develop the idea of using DNA to create little DNA barcodes to label every
*  single neuron in the brain so that we can make whole brain maps.
*  You've helped develop software tools to design three dimensional little origami DNA
*  nanostructures that can be used to make little DNA boxers that can, among other things,
*  deliver drugs to certain cell types.
*  And you figured out how quantum entanglement can enhance distributed computation.
*  So you want to just spend the rest of the hour listing stuff you've done and we can just
*  call it a day.
*  I'm not so sure.
*  But yeah, I've been all over the place.
*  Yeah, you have. It's really cool.
*  And I can't even get my own family to list me on their top 41 dads, their 41 year old
*  list for 2018.
*  But there you are on Technology Reviews.
*  Thirty five innovators under 35 in 2018.
*  So I have some high expectations talking with you today.
*  Thanks. Yeah, they may go down.
*  But thanks a lot.
*  So with respect to neuroscience, would you say that you have two big picture goals, one
*  being to develop the technology that we need to understand the brain and another to use
*  AI tools to to integrate theory with brain science?
*  That's beautiful. Yeah, that's I would describe it exactly that way.
*  There's a technology observation component and there's a theory component.
*  And people sometimes say, which is which is more important, more data or more theory?
*  And I think it's both.
*  So, yeah, very good.
*  OK, well, we're going to talk today about your 2016 paper in frontiers of computational
*  neuroscience called Toward an Integration of Deep Learning and Neuroscience.
*  So this is a tour de force, I would say.
*  And it's so thorough and provides a roadmap for anyone who's interested in doing this
*  type of research, giving lots of suggestions of what experiments need to be undertaken
*  and what questions need to be asked.
*  Last week, I had Blake Richards on the show.
*  We talked about his recent work, his paper towards deep learning with segregated dendrites.
*  So so in some ways today is it's a nice continuation of that discussion, or at least
*  it's closely related. That's fantastic.
*  Yeah. Yeah, it was a great conversation.
*  But you and I are going to talk, I think, a little bit more broadly and conceptually
*  about how deep learning and neuroscience can can be friends.
*  So by way of contrast, let's start with what's been done or thought about in the past
*  with regard to how the brain works, and in particular, the cortex of the brain.
*  So what's the classic canonical microcircuit hypothesis for how the cortex works?
*  Right. Well, I think there is various versions.
*  And, you know, one of them is simply the observation that there seem to be anatomical
*  similarities between different cortical regions.
*  There are usually six layers, certain specific types of cells like pyramidal cells, certain
*  specific ways they're arranged.
*  It's still somewhat, as I understand it, kind of debated whether they are organized into
*  local columnar structures in a kind of vertical direction.
*  But there certainly seems to be this this layer wise similarity in the layered structure
*  across regions and also across different kinds of animals and even similarities between
*  different species, you know, and in brain areas like there are also pyramidal cells
*  and hippocampus. And you can talk about, you know, piriform cortex or other
*  kind of early cortical areas that maybe are more related to olfaction, turtle dorsal
*  cortex. They all seem to have some anatomical relationships.
*  And then, I guess, historically, one of the questions is whether what that means is
*  that all of these different cortical areas, which we know from all sorts of reasons
*  like fMRI studies are kind of sensitive to different things or seem to be involved in
*  different kinds of computations. But what if they are all really doing the same underlying
*  computation that may be given by this layered anatomy?
*  So that, for example, if there's a hierarchy of visual areas, is it possible that at each
*  level of the hierarchy, either the same computation or a very similar computation is
*  happening just using the input data from the level below it, but essentially processing the
*  information in a similar way.
*  Sort of like the subcortical regions or even other cortical regions that are sending its
*  signals are orchestrating how that information gets input.
*  And then and then the same computation happens on it.
*  Right. It could be a modular kind of repeating the same computation.
*  So some people think that this could be some kind of filtering operation or some kind of
*  filtering plus pooling operation or filtering plus pooling plus normalization.
*  Or maybe there's some kind of pattern completion or amplification of patterns with recurrent
*  circuits. And this all kind of in a way goes back, I think, to Hubel and Wiesel sort of
*  saying they're simple and complex cells.
*  And maybe those are repeated in a hierarchical way.
*  And there may have been many vision models over time like Hmax or Neocognitron that are
*  sort of repeating these simple complex cell structures, but then repeating them again and
*  again at multiple layers.
*  So what are some reasons that to think that it might be misguided to approach the cortex as a
*  uniform computing structure?
*  Yeah, I mean, it's an interesting question.
*  I think there's still very, very little that's that's really known about it.
*  So one ambiguity, I guess we'll talk about a lot, is the difference between a uniform
*  computation and a uniform learning rule or learning algorithm.
*  So it's one thing to say that the same kind of instantaneous computations are happening, like,
*  you know, this is doing filtering and then pooling or something.
*  And then that happens at several levels of a hierarchy.
*  It's another thing to say that there's a similar learning rule going on that may lead
*  either to filtering and pooling or to some other types of computations, but that the
*  learning mechanism is similar.
*  I think that's related to what you may have been talking about with Blake Richards.
*  The other reason is that maybe from a functional computational perspective, there's lots of
*  reason to believe that there might be qualitatively very different kinds of computations
*  going on in different areas.
*  It's kind of, I guess, known or it's kind of widely thought that prefrontal areas have more
*  kind of recurrent processing.
*  It's still kind of debated whether even in the sensory areas, there's something kind of
*  analogous to working memory, this kind of maintaining information in a more recurrent way,
*  as opposed to this idea of kind of hierarchical filtering.
*  Those are all really kind of ideas.
*  But anyway, I mean, there's a variety of possible computations that might be functionally
*  needed that go well beyond even these kind of hierarchical filtering perception type
*  models, you know, one that Gary Marcus and I have talked about a lot is variable binding or
*  symbolic operations, routing operations.
*  And it's possible that all of those could be just differently utilized in different parts of the
*  cortical circuitry and that it kind of has the availability to do all of those within the layered
*  structure. But it's also possible that the circuitry might be customized.
*  So some areas are more for kind of recurrent memory buffers with some kind of gating structure on
*  them or some are more dependent on attention.
*  And then some might be more like sort of sensory filtering.
*  It's really, I think, pretty much up in the air.
*  What's going on? Because the kind of the classical idea that sensory areas are really kind of doing
*  some kind of bottom up sensory operation and then motor areas are doing, you know, generating
*  action. This is a little bit complicated by the fact that even in sensory areas, you find motor
*  related signals and reward related signals and attention and all sorts of all sorts of things.
*  So this is disappointing because I really thought we had the brain all figured out, you know?
*  Yeah, right. Yeah, exactly.
*  I mean, this in a way, some of the essays that we've been writing are just me finding out how
*  little we actually know and what questions you can still ask.
*  Well, yeah. So you ask a lot of questions here that we'll get to.
*  You discuss how even though early AI was was directly inspired by the brain over its
*  development, it started focusing more on mathematical operations and efficiency and really
*  disregarding the brain. And it's brought us to this point where we've seen such success in
*  deep learning now in very narrow fields, but a lot of success.
*  And it's interesting. You contrast the singular focus of machine learning to optimize cost
*  functions with the overwhelming variety of approaches and sub-disciplines historically in
*  and still in neuroscience research.
*  You think now in particular is it's a ripe time to converge again.
*  So what are some of the reasons that you think that machine learning is important for
*  neuroscience? Right.
*  Well, I think I think the history of kind of how it's happened is pretty complicated.
*  I don't fully, I guess, understand or appreciate.
*  I think I think the entire history of the interaction of machine learning in neuroscience.
*  And it's also the case that machine learning is much broader than these kind of optimization
*  based framework that's largely being used in deep learning.
*  But. I think one of the original motivations of people like Geoff Hinton and so on, inventing
*  very general connection as learning algorithms for neural networks in machine learning.
*  Is to try to come up with these kind of relatively general explanations of how neural
*  circuitry could learn to do complex functions that include the kind of full diversity of these
*  different types of computations, whether it be sensory people think things that people think of as
*  pattern recognition or information routing or memory dependent operations.
*  But for a while, you know, because I think the performance of these neural net architectures
*  was maybe inferior or perceived to be inferior to various other kind of special purpose
*  processing mechanisms that people were using for these different operations.
*  You do one set of things for natural language processing, another set of things for vision.
*  And even within vision, you would have a bunch of special purpose computations.
*  This kind of notion of using kind of general learning mechanisms certainly is very much in
*  the realm of what people are thinking about in computational neuroscience.
*  But the convergence specifically on a powerful general learning to do a wide range of
*  complicated functions is one aspect related to this question of can the brain optimize cost
*  functions or do something similarly powerful as the back propagation based learning that deep
*  learning is using. That's one element.
*  And then the other element is as that has been happening, the kind of architectures and learning
*  principles and cost functions have diversified in terms of what people in machine learning are
*  using. And those, I think, are starting to suggest interesting hypotheses coming from the machine
*  learning side that could maybe provide explanations for how the brain does some of what it does if
*  you're willing to, I shouldn't say accept, but if it pans out this idea that these kind of general
*  cost function optimization mechanisms are something that is important in the brain, then in that case,
*  a lot of what's happening in deep learning with this proliferation of progress that's happening now,
*  it could trigger more bidirectional interaction by suggesting specific hypotheses for
*  neuroscience and then trying to close the loop with actually finding out, you know, is that true
*  about the brain and how does, if so, can we get at some of the specifics from the brain?
*  Yeah, we're just on the verge of that sort of blossoming as a field too. So it's going to be interesting to see how it does pan out.
*  Right. And in general, this paper that we wrote about integration of deep learning neuroscience, it is,
*  you know, fortunately or unfortunately, it is sort of at this very conceptual level where, you know, in many cases,
*  where we're trying to give is kind of abstract directions of the kinds of things. Maybe we can talk about some specifics.
*  But I think what we need is something that's a much more specific, mechanistic hypotheses about how it could work,
*  that then would really lead to closing the loop and similarly, having data from the brain that can either verify those
*  hypotheses or suggest, you know, differences, qualitative differences from what things look like under those hypotheses.
*  So the vast majority of machine learning is supervised machine learning, where you take thousands or, you know,
*  millions of training examples and feed it into the machine. But humans learn well with just a few examples, sometimes only one.
*  You and plenty of others argue that the brain must use optimization techniques other than supervised machine learning.
*  So what are we talking about there and how broadly could those different optimizations work in the brain?
*  Right. Well, and this is also a huge question in machine learning itself.
*  So people often kind of bring together this idea of doing multiple layers of neurons, of doing back propagation or a gradient based
*  learning or optimization to train something and then this idea of supervised.
*  And those are really sort of
*  several separate concepts there.
*  It is true that when one is doing supervised learning in this current deep learning paradigm, the cost function one is optimizing is,
*  you know, some kind of, let's say, classification error or error rate on the supervised labels over some batches of examples.
*  But the general kind of optimization framework can be applied to many other things, including unsupervised learning.
*  So, for example, for decades, one principle of unsupervised learning has been to try to reconstruct the input.
*  So send an input through some layer of layers of neurons that have some kind of bottleneck or transformation in them
*  with the idea of an autoencoder and then trying to train it to reconstruct the original input
*  that will kind of lead to in the kind of internal layers of the autoencoder, it forming some kind of compressed representation of the input.
*  You can also imagine doing that in more of a prediction based framework. So instead of autoencoding exactly what it's seeing,
*  can it predict what it's about to see next, like the next frame of a movie? And there are various groups working on that.
*  There's also variations of the autoencoder idea that incorporates some other kind of additional objectives, like maybe you want to encode the information in a sparse representation
*  that has very, very few neurons active and that would encourage sparsity or add other kinds of objectives, like how it behaves under transformations,
*  whether it's many independent signals that it's being encoded to or disentangled. And then there are other interesting,
*  also, there have been various variations on this idea. So rather than deterministically trying to auto encode the input, you can also have it
*  kind of stochastic element where it generates a latent code and then, but you can also stochastically generate kind of arbitrary latent codes and then those codes will
*  give rise to some reasonable example from the type of data set that you're training on. So this is like the idea of a variational autoencoder
*  where not only can you auto encode any given input, but you can also kind of generate it from it separately or encode from it separately.
*  And then there are other ideas that people are using in machine learning, which are, it seems like these are pretty important. And this is something that machine learning researchers like
*  Yoshua Bengio and many others are interested in is the idea that what you do to do unsupervised learning is to try to make some sort of
*  generative model that reproduces data that is similar to what is coming in, similar to what you see in the environment.
*  And this is potentially an alternative also to the prediction based framework or reconstruction framework.
*  So, for example, instead of trying to make a perfect prediction of what you're about to see next, you can just say, is what I see next
*  a good example of the type of data that tends to happen? Should I be surprised to see what I'm seeing? And so this is the way that these
*  networks called generative adversarial networks work is that they have a generator part and a discriminator part
*  that interact. And what the discriminator is basically trained to do is to say, is this is what the generator is producing similar to the kinds of things that I see coming in from
*  actual reality. And so the discriminator is kind of learning whether to be surprised by any given input. But in that process, it's really learned a lot about the distribution of possible inputs. And so that's also
*  internal to the discriminator, then it will have to have
*  kind of representations of that that concisely summarize what the world is like.
*  And then separately in the generator, it also has concise representations that it can use to generate things that are like what it's seeing in the world. So these are all
*  things that are happening in machine learning.
*  And then kind of on the neuroscience side, there's been related concepts, you know, like if you try to encode the visual input in a sparse way,
*  then that, you know, the sparse encodings, for example, kind of reproduce certain properties of
*  early visual areas like Gabor filters and so on. But the deep learning community is really doing this in kind of complicated multi-layer
*  networks that are learning these more complicated, either generative models or models that are kind of saying,
*  am I familiar with this? Does this look like the distribution of the world or they're doing prediction or they're doing reconstruction?
*  There are many possibilities.
*  So before we, one more thing here, before we really jump in the meat of the paper, I really enjoyed that you invoke Marvin Minsky, one of the heavyweights of cognitive science and AI.
*  You compare what we're about to talk about, your proposals, to Minsky's ideas in his book, Society of Mind, his classic book, I should say, Society of Mind.
*  So can you just describe what Minsky's Society of Mind is and how it relates to what we're about to discuss?
*  Sure. Yeah. So I think the book is a little bit hard to summarize.
*  Well, yeah, but the main thrust of the, I guess, conceptually.
*  One of the thrusts was the emergence of some kind of mental function and learning from a set of interacting agents that each are not individually intelligent
*  and that they may have some individual notions of goals or even cost functions, I think, features pretty heavily in that picture.
*  But there's not necessarily a central organizer, but you kind of have mentality that's emerging from this interaction of many different simple agents.
*  And he explores all sorts of possible principles for how that could happen or what that would even potentially mean or what it wouldn't mean for that to happen.
*  And I guess the way that that relates is partly related to your last question about supervised learning and the way that people tend to use in these very applied settings right now,
*  these deep neural networks of kind of monolithically just trying to minimize error on some training set.
*  One of the points of the paper was to say that given what we know about the brain and about cognitive science and so on, our hunch about it.
*  And again, all the things in this paper are just hypotheses, really.
*  But one of the hypotheses was that you would not have a single kind of end to end cost function for the entire brain.
*  There wouldn't be a single thing that the brain is optimizing individually, like some frameworks for understanding the brain say, well, the brain is just trying to minimize prediction error, period.
*  Every part of the brain is minimizing prediction or it's minimizing some global prediction and then back propagating all the error signals that are needed to minimize that prediction error through the entire system.
*  Or you could say something like, well, the brain is trained with some kind of reward function in kind of the behaviorist paradigm.
*  Or you could say the brain is basically just trying to minimize reward prediction error in the striatum, some kind of one dimensional reward, which is in fact how a lot of deep reinforcement learning signals are trained.
*  Everything, even if there are multiple things in the environment or internally that contribute to that reward, it gets lumped into some one kind of net future returns.
*  And then you're trying to optimize the net future returns, but that's basically one number.
*  And so what we were saying is that hypothesis is that the brain wouldn't be doing a single end to end optimization.
*  It would be doing many local optimizations.
*  So perhaps a given area of the brain could have its own cost function and that cost function could even be potentially generated by some other area of the brain.
*  But you wouldn't say that it's all globally optimizing a single cost function.
*  It's more like almost a game theory or multi agent kind of framework where one would learn to optimize its own cost function, which would then potentially be leading to the production of cost functions for other agents.
*  And this is a little bit related to the Minsky kind of multi agent notion.
*  And also something that Minsky talks about, I think both in that book and in many of his other writings, which is kind of about the developmental aspect of this, where simple systems give rise to the goals and objectives and driving forces for other systems in a kind of very multi stage way.
*  Because I think Minsky was very influenced by developmental psychology and Piaget and other people studying development.
*  And so he also wouldn't say, oh, it's just doing hierarchical filtering or something.
*  He would he would say that one stage of development is deliberately meant to bootstrap the next.
*  Very good. And why don't you just before we get on the paper, why don't you go ahead and summarize Gertel Escher Bach for us as well here?
*  Oh, I don't know if I can summarize that.
*  Just kidding.
*  I don't think it's a very good job summarizing Minsky either.
*  I haven't read the Society of Mind and I can't finish Gertel Escher Bach.
*  I've tried to start it three or four times.
*  I can't do it, man.
*  I don't know. I just it's too deep, too thick.
*  Yeah. Similar kind of illustrating the complexity of things rather than reducing them to a single.
*  Indeed. Well, OK, so let's get to this paper.
*  And hopefully what we can do is talk about the paper.
*  And then if we have time, I hope we do.
*  I'd like to ask you some some general and speculative questions.
*  But OK, so you propose three main hypotheses in your paper.
*  So I'll just state all three here and we'll kind of step through them and discuss them.
*  So hypothesis one is that the brain optimizes cost functions.
*  Hypothesis two is that those cost functions are diverse across areas and change over development, like we were just talking about.
*  And hypothesis three is that specialized systems allow efficient solutions of key computational problems.
*  OK, so let's start with hypothesis one.
*  The brain optimizes cost functions.
*  Now, this might be painful for you, but just to be thorough, what is a cost function and what basis do we have to believe that the brain could optimize cost functions?
*  Right. Well, so so in machine learning, often a cost function is it is it is some function that's that's computed based on
*  the outputs of some subset of the system in the supervised learning context.
*  It's maybe some output layer of neurons that is used to compute, let's say, some kind of classification error.
*  But in general, it's just a function of the activities of of the neurons.
*  But cost function is very related to the idea of optimizing.
*  And so what you're going to try to do is either maximize or minimize this function.
*  And the function can have multiple components, it can have all sorts of regularization terms, it can depend on multiple different parts of the system or so on.
*  But it's it's some function that you're trying to basically either maximize or minimize.
*  And the way that machine learning tends to do this is by some kind of local search method where it is changing the parameters within a large network.
*  That could be synaptic weights, let's say, or could be a kind of bias terms of the individual neurons.
*  But we can think of it, let's say, as synaptic weights is trying to optimize those parameters or weights in such a way that the activity in any given situation.
*  The cost function can also depend on the input.
*  Let's say in the supervised learning context or in, let's say, a reconstruction context, you're comparing the output of the network.
*  And how well does it do at reconstructing the inputs?
*  The cost function also depends on the input.
*  Why do we think that or what basis do we have to think that they could be in the brain?
*  Right. Well, there are kind of many sort of anecdotal lines of argument that we use to justify why this hypothesis is plausible.
*  But the main thing we're trying to do is just to set this up as a hypothesis period.
*  Regardless of plausibility, we want to know what we want to say to this hypothesis and then be able to to know whether it's true.
*  But the main motivation really is that, again, a lot of recent successes in machine learning are done by optimizing cost functions.
*  A lot of what machine learning researchers are doing is using relatively similar optimization methods, basically some kind of gradient descent based optimization, which is kind of local search, efficient local search method for finding some kind of local
*  minimum often of of a cost function.
*  It's using an optimization method and what it's doing is it's tweaking the precise architecture that you use, the precise cost function that you use in order to get some useful functional outcomes.
*  But this this part of what machine learning researchers are doing is is tweaking cost functions.
*  And they're very repeatedly using this idea of let's do gradient descent on some cost function in some architecture to do all sorts of different tasks, whether it be language translation or video segmentation or all sorts of things, including recently, you know, navigation in a virtual world or all sorts of things.
*  Right. So there are two main claims here.
*  And one is that the brain can do credit assignment.
*  And last week with Blake Richards, we discussed one way that that could happen.
*  And and two, that the brain has mechanisms to implement specific cost functions based on an animal's needs.
*  So so when I talked with Blake about credit assignment, of course, in his paper he proposed it could be accomplished using segregated dendrites on pyramidal neurons.
*  I won't put you through the ringer and tell you to describe credit assignment.
*  I'll just say that it's a way to assign to a given unit in a network, give it its weight in the contribution to the outcome.
*  Right. Yeah.
*  So what are a couple other ways that the brain could possibly do it besides this segregated dendrites story?
*  Yeah, I actually personally really like the segregated dendrites story a lot.
*  I do, too.
*  And the reason for that is that essentially the credit assignment mechanism has to satisfy various criteria and using the dendritic architecture of these pyramidal neurons does seem to be something that makes it a lot easier to imagine, not just Blake's way, but multiple potential ways.
*  There's another paper from Walter Sen and Yoshua Bengio's group that is also proposing that the multi compartment dendrites are are being used for this.
*  Yeah, but Blake has been on the show, so I'm sure he's the right one.
*  You know?
*  Yeah, no, I mean, I think, you know, it's great for there to be these multiple specific mechanisms.
*  This is really something that was missing from our kind of more general hypothesis paper, because these really are getting to the level of much more testable mechanisms.
*  And there's also things that are even potentially in common between those.
*  Like, for example, you could say if you create a situation, let's say where the brain has some kind of unpredictable or you're causing the brain to make some kind of errors or be unable to predict what's going to happen next or so on, or do something that you think for a relatively wide variety of cost functions might generate some kind of error signal.
*  Or you could it could be doing some motor task and you are manipulating its ability to actually perform that motor task by having the target move away or something in some unpredictable way.
*  You can kind of in a fairly generic way, try to say, well, what is happening up in the apical dendrites?
*  Is there more activity going on up in the apical dendrites that would be indicative of some kind of error signal that might even be common between Blake's mechanism and the Bengio signal?
*  And then the 10% mechanism and others, I mean, even even back in 2001 or so, Conrad Cording was suggesting ways to do to have both the error signal and the kind of bottom up feed forward processing happening with the basal and apical compartments.
*  I think there are many other kind of components of of how the credit assignment might work.
*  There are many other frameworks for how it might work that don't necessarily depend in a literal sense on having segregated dendrites.
*  You could have it be instead of multiple compartments of a single neuron, you could have multiple neurons involved in doing some computation.
*  There are also mechanisms that are in some cases related to to what they're using in the segregated end rights work.
*  But that I think Hinton and other people were suggesting that the temporal derivative of the neuron activity could be a way of encoding the errors.
*  So you're basically kind of doing both position or kind of what the activity is and also the rate of change of of the of the activation of the neuron.
*  That could be two kind of potentially independent variables that could be used to do credit assignments.
*  People are thinking about different ways in which the backwards feedback of the error signals could actually be done, whether it's done in an organized way or whether it is using random feedback connections.
*  There's an idea called feedback alignment from Timothy Lillicrap and others that is a kind of a randomized version of back propagation that's that's basically using something like the pseudo inverse instead of the
*  transpose of the backward weights and showing that even random backwards weights can can cause this alignment.
*  There are ideas recently for having the errors essentially fed back all the way into the input layer of the network.
*  So rather than having to feed back, you have the neurons doing actually two different feed forward computations called error forward propagation from Havo Siegelman's lab.
*  So there are many different principles of it, and there are also some kind of general mathematical notions like Joshua Benjio has an idea called equilibrium propagation that sort of describes in certain fairly general classes of of either energy based
*  Neural dynamics or other kinds of neural dynamics, how you could direct changes in the weights using kind of clamping or nudging of the activity to to start to approximate back prop by moving it in kind of small steps in the right
*  direction of change and in a way that it will be accessed locally. So there also kind of these general frameworks for biologically plausible back prop.
*  Yeah, I should have said developing. Sorry, I should have said when when from the question that, you know, in in machine learning, and I said this last episode too, but the way it works in machine learning credit assignment is easily through back propagation, but it's not readily understandable how the brain could perform back propagation itself.
*  So right. Yeah, in a literal sense, maybe maybe not exact back propagation because of various requirements. So back propagation does require these these two separate separately encoded signals that are processed differently.
*  One is the feed forward. One is the feedback or error signals. They have to be combined in kind of a multiplicative way, which is not entirely obvious how it would do that.
*  But it's good that that yeah, but it's good that there are a lot of a lot of ideas and a lot of people working on on various ways that could happen in the brain.
*  So each of the individual problems with it, one of the problems is symmetric. Do the weights for the forward and back have to be exactly symmetric? Can they be random? Right. Can be approximately symmetric or become symmetric for each of those? I think there are a bunch of potential interesting solutions.
*  And then the question is, which one specifically does the brain do, if any, or is there some way around it? Does it does it really need to do something as good as back prop? And I think that's something that that Blake and our perspective in this paper and various other people think that it seems so useful to have something that would at least approximate gradient descent learning through multiple layers.
*  That it seems like a interesting hypothesis to see if it actually did that. And if not, that's that's maybe even more interesting because that's what suggests that machine learning is kind of not necessarily pursuing a red herring, but doing in a way more.
*  There's some shortcut around having to do that, whereas machine learning is now relying on it very heavily.
*  Right. So how would we figure out if the brain is optimizing cost functions?
*  Yeah, it's an extremely difficult question, and it's one that we don't really answer in the paper, except making some very preliminary kind of general suggestions.
*  Yeah.
*  One that Blake has talked about also, and other other people, you know, we talked about this a little bit in in the paper is that you can try to see from changes long relatively long term changes, but potentially small changes that you could see in small steps, you should be able to see if you know what
*  the cost function is, or you have hypothesis about the cost function for some for some area.
*  And of course, the cost function will probably only apply to some subset of the neurons, which is additional complexity.
*  Because if you imagine the neural circuitry in the cortex, let's say some of it in this view of the world is being used to actually do the optimization.
*  So it's kind of supporting infrastructure for the optimization.
*  Some of it is being used for other functions like attention or information routing that's not necessarily subject to the cost function in any given area.
*  And then there's some subset of neurons.
*  Maybe it's some of the pyramidal neurons, right, are actually encoding the information, which is subject to the cost function.
*  But if you look at the right subset of those neurons and you have a hypothesis about the cost function should be, then as learning proceeds, or if you perturb the system.
*  In some way, so that is making errors and it wants to adjust itself to make fewer errors or to get lower onto the cost function landscape.
*  Then you should see the activity move in a direction that does minimize the cost function.
*  So you should be if you can compute the cost function or even just compute differences in the cost function across different states, you should be able to say, well, that's that's how the neural activity should evolve during learning.
*  Even better if you had a way of measuring synaptic weights directly, which right now is very limited.
*  Yeah, you could also try to say, try to say what would be the direction of gradient motion for the weights matrix if you knew the cost function that it was trying to do the gradient of or you had a hypothesis about that.
*  You could try to try to look at that right now.
*  There's not super great ways of looking at synaptic weights, but with things like a kind of functional connectomics, you know, single neuron, you know, optogenetic stimulation and recording.
*  And connectomics and so on, you may be able to get to the point where where you would actually know something about synaptic weights, even over time.
*  That's that's a bit of a longer term technology direction.
*  But but even just looking at the activities, you could say, are they moving in a direction that optimizes your cost function?
*  What if you don't know what the cost function is?
*  If you don't know what your hypothesis is for the cost function, then you can try to look at more general things.
*  If you have some idea about how the error signals might manifest in the circuit, like if you think it might be coming from the apical dendrites, then you can try to say, well, even without a super specific hypothesis about the cost function, if I somehow make the animal's behavior deviate such that it has to start optimizing cost function, can you predict changes in the level of apical dendrite activity?
*  Or maybe you can go in and actually try to have specific hypotheses like Blake's hypothesis around segregated dendrites mechanism.
*  And actually that that will then predict specific connectivity and activity patterns for various components of the circuit, you know, particular patterns of bursting as it relates to inputs coming into the apical dendrites and the soma, particular patterns of spiking or bursting as it relates to what the interneurons nearby are doing.
*  And you can create much more detailed mechanistic predictions that depend on the actual mechanism that you're proposing that would do the optimization.
*  But I think it's actually a pretty big open question.
*  The field is what is the best approach for actually experimentally answering this question?
*  Does does the brain optimize cost function and does it do it in a way that is sort of similarly powerful as these multilayer credit assignment that backprop has?
*  So what would learning about these in the brain?
*  How would how would that help?
*  A.I. Well, I think there are kind of two options.
*  I mean, so one one possibility is that, you know, long term, we do not confirm this notion that some significant part of the organization of the circuitry is there in order to do something similar to gradient descent learning with backprop.
*  If this is not confirmed, then again, I think that's very interesting because it suggests a totally different direction than the one that A.I.
*  is currently following, which is to use backprop and every possible scenario where it can be used, whether it be supervised or unsupervised or reinforcement or otherwise.
*  The other possibility is that you this does start to look like a consistent picture and then you can start to ask about the specifics.
*  So one one thing in that case is that the brain would then have a very low energy consumption, largely relying on local connections mechanism for doing the backprop, which could be very interesting for things like neuromorphic chips.
*  It may also have interesting approximations of backprop that are more efficient.
*  Yeah, I'm hearing hearing a lot of a lot of people talking about the the energy consumption problem of the machine learning as it currently is.
*  Right, absolutely. Yeah. And so, you know, the brain is if it's doing it, it's doing it at the scale that is vastly larger than what we have in machine learning.
*  So it is doing it 25 watts doing on the order of 100 billion neurons.
*  So the actual mechanism, detailed mechanism it uses.
*  And then you would want to extend that picture into other things like there is backprop in the sense of what people may call spatial credit assignment or credit assignment among the layers of weights.
*  In the neurons.
*  But there's also temporal credit assignments, which is, you know, if you have some recurrent processing, how do you attribute changing the weights in light of the fact that a given weight is going to have multiple effects in several kind of recurrent iterations of the circuit.
*  And you want it to have the right effect on the outcome, not just on the thing that happens immediately next.
*  So there's this notion of backpropagation through time, which is unrolling the network to train temporal processing with recurrent networks.
*  But if the if the brain has some mechanism for doing credit assignment, that's powerful.
*  It may also have solutions for something like backpropagation through time, which is currently kind of a big limiting factor in the amount of computation that requires the length of time over which it can operate.
*  There have been various inventions like LSTM cells, which are trying to deal with the so-called vanishing gradient problem for for these recurrent networks.
*  But even even with those in place, there's some limit on is this really a good mechanism for doing temporal processing?
*  And if the brain is doing optimization at all, it may also have some solution for these temporal aspects.
*  It may have interesting solutions for integrating reinforcement signals into this.
*  And then once once you have the mechanism right once you have the OK, yes, let's let's say it's doing segregated dendrite based gradient descent of some kind and you know something, then I think you can work out work work outward from there in theory and try to say, well, you know, where are the error signals coming from?
*  How high dimensional are they?
*  What are they representing?
*  If you know where the error signals live, then you can try to look at those as representations and say, what are what are the error signals?
*  What are the cost functions?
*  And so as soon as you start to know one of these things, if you have a good hypothesis about a cost function that can help you to localize where the error signals exist in the circuit and how it's being optimized.
*  If you have a good notion of the optimization mechanism, you can try to go and find where the error signals are coming from that feed into that mechanism with connectomics or projectomics or other other ways and start to kind of fill in the gaps.
*  This broader picture of the architecture.
*  If you don't know any of these things, which is where we stand as this this conceptual paper, then you kind of you have to have a win on one of them, I think, before you can be super concrete about this.
*  But I think if you get the mechanism, that's that's potentially a really interesting way to to work out where to all the other questions.
*  I like it.
*  All right.
*  So that's hypothesis one that the brain optimizes cost functions.
*  Now, hypothesis two, again, is that there's a diversity of cost functions across brain areas and across development.
*  And you're careful to point out that cost functions aren't necessarily replacing specific purported functions of a brain region, for instance.
*  But you're introducing the concept that the goal should be considering optimizing a cost function particular to that region.
*  And even I like that you mentioned maybe evolution even figured out that it's cheaper to solve a problem by specifying a cost function rather than specifying the solution itself here.
*  In the interest of time, maybe we can just give a really broad overview of anything that you think that is important.
*  And then I actually do have one specific question related to this to this hypothesis.
*  Right. Well, I think, again, a lot of this kind of is trying to take kind of abstract from what the machine learning community is doing and say, well, could we use this as a hypothesis about the brain?
*  You know, with again, with this caveat that, you know, in practice, many of the systems that have been built in machine learning do kind of optimize one end to end function.
*  Whereas we're thinking about this more as many interacting potentially local cost functions in the brain.
*  But yeah, this point that it seems to be powerful to separate the cost function from the optimization mechanism is an interesting one.
*  Right. It's not necessarily the case that you would expect that even if there is some kind of optimization going on in the brain, that there is that separation.
*  Right. So many other types of algorithms can be viewed as some kind of optimization of some function.
*  But that function may never actually be computed by the brain.
*  And the mechanism optimizing that function may be built deeply into the circuit.
*  Because so many people have said, you know, Jeff Hawkins and many others have said, you know, what if the brain is making predictions and adjusting itself to make better and better predictions over time?
*  And they can propose things like, you know, Bayesian belief propagation or all sorts of other algorithms that have been proposed that would lead to some kind of unsupervised learning that that's based on predictions.
*  But then that would be a specialized, a specialized anatomical structure to do that, to minimize that cost function as opposed to some other cost function.
*  But what machine learning has discovered is basically this modularity where there's basically one line of code where you specify the loss function.
*  And then there is a whole other, you know, library of code that does the optimization.
*  But the optimization, you know, algorithm doesn't care about the details of the loss function.
*  They are really separate, separate functions in the circuitry.
*  And even if even if it wasn't explicitly computed in the brain, so there may not be any either single neuron or even population from which you would perfectly decode the cost function.
*  All you have to do is be able to have give the error, the gradient of that cost function somewhere.
*  But at least there will be this modularity that basically if you feed in gradients into one part of the brain, it could then kind of backprop those gradients back to other areas.
*  And in that sense, it would have the area that's propagating back where the error signals wouldn't care which cost function it's actually receiving the error signals for.
*  It would be able to do that in a generalized way.
*  And that raises all sorts of interesting possibilities, though, as one would try to go about finding cost functions in the brain.
*  I mean, would they have to be represented as a number somewhere as a single number?
*  If they are a single number and they need to be broadcast, does that mean that they're going to be broadcast as some kind of neuromodulatory signal, basically a chemical?
*  That can be kind of broadcast everywhere?
*  Or could it be would there be dedicated circuitry again for for propagating the errors?
*  This is something that is happens kind of in an interesting way in the deep reinforcement learning aspect where the cost function, the gradient is really a vector.
*  It's it's many numbers.
*  It is how each neuron and then each neuron propagating back to its its incoming weights, how they should change.
*  So it's a big vector of directions of change.
*  But the reinforcement signal, let's say, is just one number.
*  You know, how much reward am I getting or some value function?
*  How much reward am I expecting to be getting over time?
*  And you have to convert that one number into a vector.
*  And so the machine learning community has figured out how to how to frame it as the reinforcement problem as a loss function that you can then take the derivative of.
*  And once you take the derivative, that gives you this vector.
*  So there's all sorts of questions about how would it be represented in the brain?
*  Would it have to be explicitly computed if it's kind of one dimensional than how you convert that into a vector or if it's a vector, then how do you convert that into into one number or so on?
*  So it's mid mid 2018.
*  It's 2018, let's say your best guess.
*  When will the first cost function gene be discovered or optimization gene?
*  Right. Yeah. Well, you got to give me a number here, man.
*  Yeah, I don't I don't have a super good estimate.
*  I mean, you could say already that, you know, a lot of the the genes that we know to be involved in the reinforcement system, you know, D1 dopamine receptor or something is is somehow very related to cost functions.
*  I think the question is, when when will it be something other than just a reinforcement, kind of a one dimensional reinforcement signal be discovered?
*  And when will we be able to discover that that is if if it is that that is being used in this kind of deep learning sense of of, you know, vectorial errors that get propagated back?
*  Yeah, I don't have a definite answer on this.
*  I think that it could be that in the next few years, as the technology gets better for things like, you know, very dense activity mapping in circuits and relating that to to a very large scale anatomy, that we might be able to actually hone in on these kinds of mechanistic predictions like the segregated dendrites ideas and actually go in and say, you know, here I'm looking at it and the object that I'm looking at the cost function is this activities of these apical dendrites or something and be able to actually relate that to.
*  To a cost function that makes sense to be optimized for behavior and say, OK, yes, well, this is the error signal for this part of the circuit.
*  It makes sense that that is what it is, because in the end, multiple layers forward, this actually contributes to going up the correct gradient direction for the net output that you care about.
*  So I guess my prediction would be that this would happen over the coming, say, five to 10 years as the activity mapping and connectomics technologies get better to let us look at super specific mechanisms.
*  Yes, I love the definitive span there. Appreciate that.
*  OK, so let's move on.
*  So hypothesis three is that specialized systems allow efficient solutions of key computational problems.
*  So this has more to do with the hardware, right?
*  Yeah, right.
*  So there's many aspects to that, including part that's inspired by machine learning as well, whereby one of the things that we were noting is that, I guess, classically, maybe one of the objections.
*  To kind of this connectionist picture is that historically one has seen kind of relatively uniform networks.
*  I mean, the convolutional networks have various kind of weight sharing and some structure to them, but a very minimal structure.
*  Whereas, you know, there seem to be a range of specific problems.
*  Wouldn't the brain use evolutionary specializations to do specific computations?
*  But in machine learning, we do see that happening also.
*  That's one of the things that that sort of inspired this paper is things like specialized dedicated memory systems that are not just memory that's kind of in the activities of all the neurons in an unstructured way, like in an LSTM.
*  There are dedicated memory systems and things like memory networks or the neural Turing machine or now many other dedicated systems.
*  In the more from the brain side, there are many kind of characterized systems that one doesn't think of large scale systems that one doesn't think of as being just kind of encoded into the weights of an otherwise unstructured network.
*  So there's attentional systems.
*  And we know that there are things like spatial maps of attention control.
*  There seems to be some kind of information routing, maybe routing of some kind of contextual signals.
*  It's not entirely known, but there are various models of how the thalamus could potentially be a kind of a switchboard for routing information on over long distances across cortical areas, not necessarily just going through the typical hierarchy, but being able to kind of turn on and off transient connections that are distant between cortical areas and perhaps under the control of things like the basal ganglia.
*  That then send outputs of thalamus and might be able to gate on and gate off these kinds of long range connections or dedicated working memory buffers.
*  And then for many kind of computational reasons, people have argued, and it's really I don't think it's really known, it's really settled at all.
*  But some people have argued that you need dedicated operations for things like symbolic generalization, like something like variable binding that you really need to be able to copy and paste information between buffers in a way that doesn't depend on the content of what you're copying, but will work, allow you to copy any sort of symbol between areas.
*  That's something that we talk about a little bit is this idea of of how copying or binding would work.
*  Yeah, yeah, very, very good. So, I mean, other things that you include in the paper, you guys talk about evolution a lot and how these things could have come to pass evolutionarily and what it means.
*  And then you end the paper with a long list of open questions that I won't read here, but I'll point people to the paper in the show notes and and they can go and have a read for themselves.
*  So it's a great paper.
*  So I appreciate you so much.
*  Yeah, I'm really, really thrilled that you find it interesting.
*  And yeah, so let me let's spend the last few minutes here after you have a few whiskey shots to and I'll ask you some sort of rapid fire, broader speculative questions here.
*  OK, so what's one idea that you've been really wrong about in any domain?
*  Doesn't have to be neuroscience.
*  Let's see.
*  Well, I think there's an interesting story behind this this paper that we were just talking about, which is that I previously tried to write.
*  This was with Gary Marcus and Tom Dean, a previous essay about trying to similarly kind of do some kind of integrative survey of different realms of computational neuroscience,
*  trying to understand sort of the directionality of of where things were going in relationship with computer science.
*  And there we really took this perspective just a few years earlier of let's try to make a list of all the computations that the brain does.
*  We really have a table in this paper that says, you know, it's not trying to be definitive.
*  We know the answer, but it's kind of exemplary of kind of trying to fill out kind of Mars levels of algorithm implementation, computation and particularly try to highlight things that were outside of of the kind of
*  hierarchical pattern recognition domain.
*  And so we had computation in there like there's a binding computation.
*  There's a normalization computation.
*  It's a table. Yeah. Just just a few years later, you know, we sort of really changed that concept to say, well, you know, maybe there's a single common learning algorithm, or at least I did.
*  I'm not sure if Gary agrees with this, but that might give rise to many of those things in an indirect way.
*  So I think, you know, it's just. Yeah, we can we can try to feel a sense of directionality from the literature, but it really does depend on your perspective that you take on it.
*  So I'll be curious whether in a few years we'll have a totally different perspective.
*  Maybe it may be optimization is the wrong idea or something.
*  And then, of course, I've been wrong about many other many other many other things.
*  OK, fair enough. So is it safe to say that you think that the main contribution neuroscience will have on A.I.
*  Is is building toward general A.I.
*  Yeah, I think that it seems like special purpose A.I. is making a ton of progress on its own.
*  I think it is unclear where it will get stuck towards general A.I.
*  Right. It may be that there's there's enough concepts out there that people working from a computer science perspective and building systems and just thinking, you know, can can get you there.
*  I think that neuroscience is is obviously very exciting because we do have an example of a general A.I. in the brain and because there are huge mysteries kind of on both sides that seem like they're kind of related to each other.
*  You know, how does memory relate to one shot learning?
*  How does planning and imagination and memory and cost function optimization, all these ideas relate to each other?
*  These are somehow they seem to me they're very related both to general A.I.
*  And to some of the big questions in neuroscience, like what is the hippocampus doing?
*  Right. OK, good.
*  Back to Marvin Minsky for just a second.
*  So he calls consciousness a suitcase word, which is a concept I like.
*  I don't know if you're familiar with that concept.
*  Basically carrying a lot of different concepts around in a suitcase because it encompasses so many different other domains.
*  When will we know what the heck we're talking about when we say consciousness?
*  I have no idea. I have no idea.
*  I like the idea of the suitcase word, although I'm not 100 percent sure that that's that's the right thing to apply to consciousness.
*  I mean, it does seem like a very fundamental, fundamental thing.
*  I mean, I think I I understand why he says it's a suitcase word, but I can also I also sympathize with the idea that there is a very specific mystery there.
*  We don't have a particularly good handle on right now at a few different levels.
*  Maybe I can get you and Blake Richards into a fight because he yeah.
*  Yeah, this would be good. Yeah, I think Blake is less less into consciousness.
*  Yeah, he is. Yeah.
*  OK, so just two more questions and I'll let you go here.
*  So what's something that you wish was on your CV that's not?
*  Oh, boy. Maybe I do need a shot of whiskey.
*  You do. You do have a lot on your CV.
*  Yeah. Well, I mean, I think that, you know, these a lot of the things that we've been looking at are, you know, are very long term challenges.
*  So we've been working on activity mapping and connectomics technologies.
*  And right now it doesn't say that we we got the connectome.
*  You know, it says we we have some ideas and and many awesome collaborators are doing real excellent work on that and making real progress.
*  But I would I would like to say someday that we have on our CV that we actually we solve some of these real technology challenges and maybe can do a whole brain connectivity map or activity map.
*  Well, this this segues nicely to my final question for you, Adam.
*  When will all the neurons in our brains be labeled with DNA or RNA barcodes in our personal brains?
*  I'm not sure ever. I think there's great progress being made on that, you know, particularly by Tony's Adore's lab and various groups that I've been involved with.
*  Kind of an ideas and funding level have been collaborating on what is the readout technology, combining expansion microscopy and in situ sequencing and other technologies to try to read out these barcodes that Tony has.
*  And there's also a lot of ideas about other kinds of barcodes.
*  You know, can you use protein barcodes or or other kinds that might be even better?
*  I think I hope that in just a few short years, there will be really useful entire brains labeled entire, let's say, mouse brains labeled.
*  I think it's something that can be done to label them with barcodes, whether it be with one of these blood brain barrier crossing viruses or my friend Reza Kallour from the church lab recently had self generating barcodes that are encoding the cell lineage,
*  perhaps not at a perfectly single cell diversity level, but getting pretty close to that where they're using CRISPR to in situ diversify a locus in the DNA while the while the mouse is developing.
*  It's not quite yet at the point of being a connectomic barcode for every neuron in the brain.
*  But I think that between what Tony is doing and other efforts like that one, it should be just a few years.
*  And then we need to combine that with with different readout methods and trafficking methods for these barcodes and potentially a pretty large scale investment in actually doing the data collection.
*  But I think it's a really exciting way to to scale up anatomical circuit mapping, which is still a huge limiting factor for all of what we've been talking about, I think.
*  Very good. Well, Adam, thanks for your time here.
*  And when our paths cross, I will buy you a shot of whiskey.
*  Thank you so much, Paul.
*  I appreciate it.
*  Actually, I'll link to some of the talks that you have given on DNA barcodes just because listeners probably won't know what we're talking about.
*  But so appreciate the time and keep up the good work.
*  This is great. I really appreciate talking to you.
*  Thanks.
*  That was fun.
*  As usual, you can follow Adam on Twitter.
*  He is at Adam Marblestone or Google him.
*  He's all over the Internet.
*  Thanks for listening and stay tuned.
*  I've already got a lot of great guests lined up.
*  Next week, you'll hear Grace Lindsay talking about convolutional neural networks and attention.
*  And we'll probably talk about her podcast, Unsupervised Thinking, which is about AI and neuroscience and science in general.
*  So check that out as well.
*  OK, see you next time.

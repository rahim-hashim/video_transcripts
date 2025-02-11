---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3608s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 11782
Video Rating: None
---

# BI 059 Wolfgang Maass: How Do Brains Compute?
**Brain Inspired:** [January 22, 2020](https://www.youtube.com/watch?v=aY6OybgN4n8)
*  In a sense, I think the folks in machine learning, they're right in a certain way.
*  They say we possibly have not really captured what spike and neurons are doing in the brain
*  then.
*  And so therefore, by just throwing spike and neurons into the model doesn't necessarily
*  make it brain-like.
*  Sure.
*  Neuroscience had a much more optimistic perspective 20 years ago when we had fewer experimental
*  data.
*  Now that all these experiments have shown how these simple theories don't work, then
*  things have become more complicated then.
*  Santiago Ramon y Cajal, in his Advice for a Young Investigator, writes of theorists that
*  they're, quote,
*  He goes on at length and then later writes, quote,
*  Ramon y Cajal was using theorist there to refer to one prototype of someone who is creative
*  and has a lot of potential but doesn't do what it takes to accomplish anything.
*  Well, we here at Brain Inspired, that would be me, know that theory is of course an essential
*  part of scientific progress.
*  But as my guest again today, Wolfgang Maas, knows, experiments are also essential to close
*  the loop of that scientific progress.
*  So we're at this weird stage to me, it's weird, in neural network and deep learning development,
*  where we've seen a ton of success in terms of what deep nets can do and a ton of development
*  the varieties of neural networks being built.
*  And there's a lot of excitement in neuroscience because deep networks seem to account for
*  how our brains process signals better than models in the past, in general, have accounted
*  for our brains.
*  But there are people like Wolfgang who believe that there's lots more to learn about computation
*  if we consider more details and principles that underlie how brains operate.
*  Things we learn from experiments, like trial to trial variability in the spiking patterns
*  of neurons, the stochastic nature of spiking itself, and so on.
*  So in the second part of my talk with Wolfgang, we step through a few of those promising avenues
*  for incorporating experimental findings into models of spiking networks, and we sprint
*  through a few of his latest projects implementing some of these principles.
*  You should check out his work in more detail.
*  I wanted to talk at greater length about his latest work, but we just ran out of time.
*  So go check out the show notes at braininspired.co.uk, podcast slash 59 to learn more about that work.
*  I have a lot of great guests lined up, and thanks to those of you who are emailing me.
*  Well, thank you if you're emailing me with kind words of appreciation that, along with
*  monetary support on Patreon, really do let me know that I'm headed in the right direction.
*  But I also enjoy your emails with requests for various guests.
*  I have a long list of people to invite, but when I hear from you guys and you suggest
*  someone, it either puts them on my radar or on my list, if they're not already on there,
*  but usually it's someone who is already on my list, but your email serves to basically
*  bump them closer to the top of that list.
*  So if you want to hear someone on the show, do get in touch.
*  Just email paul at braininspired.co.
*  Happy theorizing and experimenting out there.
*  I'll see you next time.
*  Let's start getting into some of what you do really more.
*  So spiking neural networks, this is like your bread and butter here.
*  You've called spiking neural networks the third generation of artificial neural networks.
*  You want to just kind of walk through really high level, like what are the first two generations
*  and how do they differ from spiking nets?
*  Yeah, this is something I wrote a long time ago.
*  Remember correctly the first generation were just the threshold circuits, which I mentioned
*  now, which were at the same time a cool off pitch neurons, so the earliest models for
*  the function of neurons in the brain and also know that they're considered in computer science
*  and computational complexity theory.
*  And there's characteristic that you have neural models which give a binary output, no zero
*  or one then.
*  And then one notice know that it's very hard to train these networks at that time.
*  And so therefore they went to neurons which give an analog output number.
*  So sigmoidal neurons, so they give a smooth output, which is a nonlinear way, kind of
*  proportional to the input.
*  And this is what has driven us all the way up through current days in deep learning networks.
*  Right, branch of it.
*  Although not a funny aspect of history is since a few years, one knows also really how
*  to apply powerful learning principles to threshold circuits or spiking neurons.
*  So, you replace the spike with sort of a smooth function, right?
*  Yeah, or simply plug in for the non-existing derivative, something which goes up and goes
*  down then in a smooth manner.
*  This is mathematically awful, right?
*  But practically, it's the most powerful method for really training now at the moment also
*  networks of spike and neurons.
*  And it works really so much better than previously considered learning methods.
*  At least, no, everyone wants to really train a whole network if you don't just want to
*  kind of train a single connection between two neurons then.
*  And you can do that using backpropagation.
*  Right, no.
*  So, in principle, one can therefore use versions of backpropagation, of backpropagation through
*  time then.
*  And it's amazing how well this works then.
*  And one can watch it, we apply it to the spiking neural networks for the same task as then
*  a model for differentiable neurons, which is used in machine learning, like networks
*  of LSTM units.
*  And then simply compare the performance then.
*  And typically, the spiking version is a few percent off, which may be due to this defect
*  in the training then, or for other reasons.
*  But they're in the same ballpark then.
*  Yeah.
*  Well, okay.
*  So, brains are efficient.
*  Deep learning networks, the ones that use the gradient responses, the analog signals,
*  are extremely inefficient.
*  Is efficiency the main reason to start to figure out how to use spiking neural networks?
*  Or is there something about the computational principles from spiking and from brains that
*  deep networks won't ever be able to capture?
*  Yeah, I find it difficult to say something which says, you know, deep learning networks
*  will never capture this because previously, you know, these things turned out to be wrong.
*  But there are certain characteristic differences.
*  And I think it's not only spiking neurons, but the fact that neurons in the brain of
*  different types, you have excitatory and inhibitory neurons, even you have different classes of
*  inhibitory neurons, which well-defined parallel neural connectivity profiles and probably
*  also functions.
*  And this is something we don't have in deep learning networks.
*  And this is at least as fundamental as spiking versus non-spiking.
*  I think, for example, this fact that you have inhibitory neurons and some articles in neuroscience
*  proposed actually that one should typically think of brain networks when you have
*  peripheral cells, it's under inhibitory lock then only if there is a certain release for
*  a short time window because just the things are right at the moment for various reasons.
*  So the network allows this neuron to fire.
*  So the network is always at the ready and ready to go.
*  And it's only until it's released.
*  And once it's released by the inhibition from, so it's disinhibited, then it can enact the
*  performance.
*  Right.
*  And it's really not sparsely disinhibited.
*  And so therefore, it's sparsely active.
*  And this may contribute really to its also energy efficiency, because if you have a generic
*  artificial neural network, most of the neurons are more or less active all the time than
*  the brain.
*  Most of the neurons are not active.
*  And if a neuron is active, it says something, it has a meaning then.
*  And probably this could even be a coding principle that individual neuron in the brain has, as
*  its individual, has more of a meaning than neuron in the artificial neural network, which
*  is always a voice in a crowd then.
*  Yeah.
*  Let's get into this.
*  So you wrote a review in Current Opinions of Behavioral Sciences called Searching for
*  Principles of Brain Computation.
*  And you lay out multiple, you suggest multiple features of brain networks and neurons that
*  you think can provide clues to how they compute and learn.
*  And we've just talked about two, spiking is one of them and spiking neural networks.
*  And you just talked about the sparsity.
*  And I guess we talked about more than two.
*  Sparsity and, go ahead.
*  Actually, these two were not even mentioned among these four things which are there addressed
*  then.
*  Yeah.
*  Well, so you've mentioned more in talks as well.
*  So I just kind of wanted to walk through some and just kind of explain, get your comments
*  on them.
*  Yeah.
*  So this also, I think it goes to me, coming back to the way our think, no, theoretician
*  in this area should really do science.
*  should watch out for solid experimental data, which really are in contradiction to common
*  theoretical assumptions then.
*  How does that contrast with the way that a theoretician would normally go about?
*  I mean, are they sitting in their church and that's how they get their ideas?
*  Well, you read papers typically from your community then.
*  Now, they of course, now, unfortunately also, there are not quite a number of research labs
*  that people now look into the other field.
*  Now, I don't want to end in a too negative feature.
*  I want to see it more positive.
*  I want to encourage people in theory not to look more at experiments.
*  But I think now that, for example, people who do work on, say, predictive coding, typically
*  when I talk to people or at least the people to whom I talk, I didn't find that they're
*  really search the literature for experimental evidence for against this hypothesis.
*  And so this is somewhat, it's a gulf, of course, between experimental kind of style papers
*  and theoretical papers.
*  And it's usually not required then from republishing a theoretical paper that you really go down
*  into the experimental literature and discuss the validity of your assumptions in light
*  of this experimental data then.
*  There's a lot of data out there.
*  Yeah.
*  So you have to select it.
*  So, for example, therefore, in this review article that I mentioned, I looked at four
*  principles which really go against basic assumptions of no larger portions of theoretical models.
*  The first one was this heterogeneity of neurons then.
*  And it goes even beyond now having excited inhibitor neurons.
*  If you take a closer look, it's hard to say that you find any two neurons which respond
*  in exactly the same way to the same stimuli.
*  This is what experimental neuroscientists told me.
*  And the same actually holds for synapses then.
*  If you apply the same protocol, pairing protocol to two synapses, typically you find no different
*  outcomes there.
*  Right.
*  And one finds this distribution of data points clearly in all these STP papers.
*  But people ignore these data points and they just look at these interpolating curves which
*  have a nice exponential shape and then derive STP rules from this averaging over lots of
*  different synapses.
*  Sure.
*  But if you would then apply theory or any model where you have this diversity of synapses,
*  then probably it wouldn't produce the outcome that you would like to see out of this.
*  So therefore, I think there's simply a fundamental principle in place then that one should not
*  think that brain networks in the brain really are just architectures of a single, of a very
*  small number of building blocks then.
*  There's almost infinite diversity of emergent local models then.
*  And so therefore, from the theoretical perspective, we have to really move towards formalism,
*  which allows us to study dynamical systems which consist out of such heterogeneous adapting
*  units then.
*  One approach to this is liquid computing, which you developed almost 20 years ago now.
*  Yeah.
*  And I mean, maybe I can just ask you like what the, well, liquid computing, I guess,
*  diversity of all sorts of types of neurons in principle and all sorts of types of synapses
*  because in essence, it's this just mass of recurrently connected units that you just
*  send input in and because of all their diversity, they come up with all sorts of different sub-functions
*  that then you can output this mass of units to these readout neurons and just train the
*  readout neurons of how to interpret all these sub-functions and put them together to train
*  them to do what you want.
*  That's probably an insufficient description of liquid computing.
*  Maybe you can add a better description.
*  Yeah.
*  Yeah.
*  Liquid computing came really about out of meeting with Henry Markram, who is an experimental
*  neuroscientist, one of the most talented experimental neuroscience in recording with
*  patch claim for many neurons and simply one of the discoveries of SEDP.
*  And he deeply cares about really what is the computational organization of a cortical column.
*  And at that time, there were two kind of dominant schools of thinking.
*  One was a tractor neural network model that the whole network moves into a tractor and
*  then this produces the answer.
*  The other one was more the ice cube model more oriented towards coding in visual cortex
*  who will envisage that you have a whole column and all the neurons in this column have the
*  same role they're supposed to fire when a certain orientation shows up then.
*  And then you have the next column where all the neurons there do some other things.
*  And both of these hypotheses are not really consistent with experimental data as far as
*  I know. And so therefore, Henry said, no, everything flows then like here I click then.
*  Right. And he wanted to see how you can still do meaningful computation within this seemingly
*  uncontrollable diversity of local dynamical units then.
*  And so then liquid computing was simply one way of getting your sense and use out of such
*  a system there by just keeping in mind that there are certain readouts, which are certain
*  neurons, maybe in other areas, which have a particular task and a particular goal to
*  extract particular information.
*  And there it's good simply to multiplex lots of information.
*  You can superimpose it in such a liquid then and then still individual readout neurons
*  can tease it out.
*  And so I think it's still an interesting paradigm.
*  I think one aspect where I now think differently is that in that model, all the plasticity
*  was really postulated to take place in the readout neurons then.
*  Whereas in this recurrent circuits, we didn't need even plasticity.
*  And this is something which is probably biologically wrong then.
*  There's plasticity everywhere.
*  And so at that time, I think this was simply a convenience because we didn't have any
*  theoretical or algorithmic tools to understand learning in recurrent networks of diverse
*  elements.
*  And so now since a few years, we do have, for example, E-PROP, a method which is even
*  biologically possible and which allows you to understand learning, not only supervised
*  learning, but also reward-based learning in recurrent networks and when sees that really
*  they gain can gain a much higher level of functionality.
*  Yeah.
*  So nowadays, I think no actual circuits are somewhere in between.
*  To some extent, also the recurrent circuitry itself is already pre-configured to maybe
*  facilitate the role of common subsequent readouts.
*  But it still has a certain general purpose aspect in order to allow new readouts when
*  you want to learn a new task then and you need to extract new features from your input
*  that still is feasible because the recurrent circuitry, say in a cortical column, isn't
*  completely already dedicated to one function then.
*  Is one of the lessons there that it actually is beneficial to have maximally diverse types
*  of neurons and types of synapses to maximize the number of different computations that
*  could be performed with the same pool of neurons?
*  That's correct.
*  This is one of the few cases where I saw then really useful having diversity then and there
*  even was some theory going along with this from approximation theory, but it was not
*  really that no tight level that's a theoretical explanation.
*  But I think we do need more kind of theoretical frameworks which allow us to really approach
*  understanding of diversity of dynamical system which consists of diverse elements.
*  And I think what's somewhat against this is simply a certain kind of tradition in our
*  thinking which is probably influenced by theoretical physics there where you think of statistical
*  physics, you have certain molecules of a gas, they're all the same and you get really exciting
*  global phenomena in terms of interaction of the same units then.
*  And I think this paradigm really is in the back of heads of many neuroscientists also.
*  And I think probably biological tissue is really not suitable for these models which
*  come from physics, but it's very hard to depart from such a well-established check of thinking
*  and concepts there.
*  And you really have to set out to really make a conscious effort to move the science into
*  a somewhat different direction to really get an understanding of dynamical system, we have
*  heterogeneous adaptive components then.
*  And this is exactly I think the type of theory that we are missing at the moment to really
*  have an analytical counterpart for understanding complex experimental data.
*  Well, like you said, it's sort of easy if all the units are the same, you can mentally
*  kind of chunk them into a space in your mind and then start manipulating them in your head
*  and how they can interact.
*  But all of a sudden you throw diversity of units and diversity of synapses and it just
*  gets really messy and it's really hard to keep track of.
*  Yeah, so as I started out with the first one of this kind of no-stumbling blocks from experimental
*  science that are listed in my review article.
*  The second was that neurons don't behave the way as we expect them also from theory,
*  that they somehow look for finding a role on their own, finding a role in the network
*  to make themselves useful.
*  They tend to gang up into so-called assemblies or assembly sequences.
*  And there's rich literature which started a little bit in the Boczaki lab, but they
*  really went out into all areas of neocortex that everywhere where you look, you find that
*  neurons don't really act on their own, their collisions of them then.
*  And these are some loose collisions, but one really should not think of a neural circuit
*  really of being just a set of individual neurons which all do their own thing then.
*  They have certain group phenomena.
*  Modularity.
*  Right.
*  But it's a difficult one because these are not clear-cut groups like in the ice cube
*  models.
*  These are kind of ensembles.
*  And I think this is very nicely described by Boczaki also in his review paper in Neuron
*  I think about 2010 where he said, at each moment a neuron decides whether it wants to
*  join assembly or not then.
*  And this may actually be possibly something really fundamental to the way in how brains
*  work because we don't just do sensory processing.
*  We always have goals in mind.
*  We have no memory in our mind.
*  We have no preconceived, no hypotheses.
*  And this all colors our sensory information, our processing all the time then.
*  And I think one could possibly view this as being kind of more the system level consequence
*  of having this somewhat loose assemblies then.
*  Where one should think of a hardcore of an assembly as something which really corresponds
*  to a hardcore of a concept then.
*  And then there are these fringes then which provide no rich meaning which surely is less
*  reliable.
*  It really depends on your recent history and other goals or so.
*  And so therefore I think now, and this is something actually which is now at the center
*  of this new book by Boushaki, The Brain from Inside Out, because he postulates there an
*  exciting hypothesis that these assemblies are there already in the brain from the beginning,
*  say.
*  In the structure?
*  Yeah.
*  And this is something which has some support then.
*  You find new activity patterns even developing new tissue.
*  And then he think now the issue of new recording is really that these assemblies have to find
*  now some meaning in the outside world to which they then relate then.
*  So that first have a certain organization of kind of say potential concepts which are
*  still empty, possibly relating to motor outputs.
*  And then you relate them to meaning in the outside world, to events, to sensory information
*  then.
*  So this is like imprinting in a duck.
*  A duck comes out and it has an assembly that's just like, mom, mom, mom, mom, and it's waiting.
*  And then it sees the lamp post and thinks, oh, that's mom.
*  OK.
*  This is a perfect example then, right?
*  And I think it's quite exciting because it really requires a new way of thinking about
*  really how new recording happens, what really happens during learning then.
*  And they also know, I would recommend if anybody was interested, look for example at the work
*  of Ken Harris at UCL London or Jason McLean at University of Chicago, who have studied
*  now various aspects of this assemblies.
*  And for a theoretician, this is as far as I can see still an enigma then.
*  We tried to get hold of this organization in summer, creating a theory of computing
*  with assemblies then also not partially together with no well-known computer scientists, Christos
*  Papadimitriou at Columbia University.
*  But at the moment, I think the reality of the assemblies in the brain escape us.
*  We don't have a conceptual, no analytical framework which is flexible enough to fit
*  to the complex data then.
*  But I think it's something that we may have to grope for really a formalism then.
*  It may not really fit to any existing way of formalizing things then.
*  But now coming back to my observations, kind of facts which I took from as lessons for
*  experimental neuroscience, this is certainly something which should occupy many theoreticians
*  and modelers because this is likely to be really also very rewarding because we know
*  from recording from human brain also epileptic patients that concepts are intimately linked
*  to assemblies then basically evoking a concept is like really activating assembly.
*  And then also a few years ago, it was shown that if you form an association between concepts
*  like you see a person in front of a background for the first time, you see even how these
*  two assemblies in the brain change then.
*  So we even have now evidence how assemblies are modified in order to accommodate associations
*  between different tokens of meaning then.
*  So we have really wonderful evidence then which links this activity on the level of
*  neurons to really, really high level cognitive operations then.
*  But more work needs to be done then.
*  The theory is not there.
*  Yeah.
*  And I think for me, the exact frontier is we have now published a paper in several
*  cortex where we in principle tried to model this process of the formation of associations
*  then using STP.
*  And it works then also.
*  But also what we found, it's very hard to create a model which scales up then because
*  in the brain you have thousands of different concepts and assemblies, probably ten of
*  thousand, and they're quite selectively associated and not associated.
*  And at the moment, I'm missing really a modeling framework which allows us to create such
*  large set of assemblies which don't interfere with each other in unwanted ways, but are
*  kind of ready to be associated whenever this arises then.
*  So therefore, I think that this is really a wonderful area to work on.
*  But and I find it unfortunate that very few theoreticians are working on this problem.
*  I mean, there's so many things that you work on that so many people could join in and
*  contribute to as well.
*  I mean, it's super impressive just the scope of the directions that you're taking from
*  the theoretical perspective using these biological constraints.
*  So anyway, so I mean, there are plenty more of these biological constraints that you
*  mentioned in the paper and then beyond.
*  Maybe we should keep walking through them.
*  Yeah, I think the third one is also really exciting for theoreticians.
*  This is the fact now that neurons are not deterministic as far as we know then.
*  And this is apparently really built into the way how neurons are built.
*  The spiking mechanism around the soma and axon is quite deterministic, as many people
*  have shown. But synaptic release is probabilistic, as we know, and probably also
*  genetic spikes to some extent, to drastic there.
*  Yeah, with a probability varying between some estimates of really low to about by
*  chance.
*  And this I find intriguing, right, because if you want to build a model and we believe
*  no synaptic weights are important and synaptic connections are important because they
*  hold the learned information, you wouldn't make them so unreliable.
*  Yeah. So therefore, I think this may really inform us because the brain really wants to
*  optimize something else and really has a different architectural paradigm in mind now.
*  And then we have when we build neural networks.
*  So the stochasticity issue, I mean, you've done work on what it could be good for.
*  Right. So one of the things is probabilistic inference.
*  And we don't need to go into detail about these things.
*  But this could be how state transitions are computed by sampling.
*  And I had Matej Lingel on the show, and he's worked a lot on calculating computing
*  probabilistic inference using sampling from stochastic populations of neurons.
*  You know, so they're stochastically firing exponentials.
*  And also, that means from trial to trial, the variability in their spiking is high.
*  There's high trial to trial variability.
*  Another problem that you have seen a benefit to computation of this stochasticity
*  is the potential to solve constraint satisfaction problems in a heuristic manner.
*  I don't know if you want to just comment on that.
*  Yeah. Yeah, I think this is still an exciting area.
*  And it points to me towards an aspect of understanding stochastic activity in brain
*  circuits, which I don't understand yet, because in order to do something to solve
*  in a stochastic manner, constraint satisfaction problem, you simply know you
*  go stochastically through many possible solutions until you find a solution that
*  you find satisfactory.
*  And now this the second part is really difficult.
*  And I don't see any hints from biology how this is implemented, because you not
*  only have to generate stochastically possible solutions to a problem, you need
*  to then have a very effective and also very fast probably evaluation circuitry.
*  Which one's right.
*  Which says, this is now completely crap.
*  This could be good, but I will put it into memory and look for still something better.
*  And how long do I need to look until I say, okay, fine, I'll do that.
*  And so this is something that we are missing.
*  I think we're also missing really also information about what is the speed of the
*  sampling then, because if it's happening at the speed of say single spikes, so that
*  you have every 20 or 40 milliseconds, another sample that's extremely fast sampling.
*  And this makes, of course, even harder for any evaluation circuitry to look at the
*  quality of any current proposed solution then, right?
*  That's got to be unlikely, right?
*  Yeah.
*  So probably the brain uses some slower sampling and the best evidence that I found
*  now there is really work of Wallis from UC Berkeley, a few years ago, which was an
*  obituary frontal cortex, where monkeys had to evaluate which of different liquid
*  reports they probably would like more.
*  And he found that before they made the selection, he found that in obituary
*  frontal cortex, he had certain characteristic state switches then, and they were on a
*  slower time scale, I think more of hundreds of milliseconds.
*  So this would be a kind of, you know, a search, a stochastic search, which would
*  better fit into the speed of really cognitive processing and evaluation circuitry.
*  But then we have problems to really implement this whole slanting, slow sampling
*  of the level of neurons and synapses then.
*  So this is probably the reason is because our standard models of neurons and
*  synapses are really lacking in this intermediate time scales.
*  Now they're made to model the spiking process and post-synaptic potentials, so
*  at tens of milliseconds, but they're not good in really reflecting what neurons and
*  synapses can do on this intermediate time scale of hundreds of milliseconds and
*  going to seconds.
*  This is not in the scope of the models.
*  One knows, you know, this time scales exists, no calcium concentrations or
*  the phosphorylated Comk-2, or various, no processes in synapses, metaprotropic
*  synapses, which have no slow processes.
*  Now we know this exists, but I'm missing quantitative models, which allow us to
*  put them into models and put them together with a network function then on
*  this immediate time scale.
*  And this, I think, is really a major deficiency then.
*  And possibly there, it would be fruitful if theoreticians and
*  experimentalists would come together because I hear from many neuroscientists
*  that they know about this, but apparently they're also a little bit frustrated
*  because if they tell their colleagues from theory about this, they're not so
*  interested because this doesn't fit into the usual frameworks, right?
*  And they can't even model this.
*  And they even have trouble, for example, to find a reasonable good, no model for
*  metaprotropic synapses and all the signals which affect it then.
*  So this can be solved probably right now, if one just puts the mind to it then.
*  And I think this is something we need then.
*  Maybe let's get through a few more and then I kind of want to ask high level
*  questions about the, just these constraints and constraints in general.
*  Yeah.
*  So there was only the last constraint then in this review paper, which is this
*  novel observed fact that a neural circuitry is not really fixed then.
*  And so it's from some imaging of spines.
*  Once one were able to monitor them for hours and days, one sees now the many
*  connections that come and go then.
*  And so therefore it appears to be that it's probably the wrong mindset to think
*  that this is genetically encoded circuitry, which is just very good in
*  supporting many computation functions, many adaptive functions, but even the
*  architecture of circuitry adapts to the set of tasks at hand then.
*  And they were nice quantitative models.
*  And then one can even view this.
*  Now one can put then also stochasticity into synoptic plus system rules.
*  And then one can view also network adaptation as a sampling process, but
*  now on a slower time scale, on the time scale of connections that come and go
*  then.
*  And so one can view this as a network really searching for configuration,
*  which works well then.
*  And so this was again something kind of back to kind of, you know, favorite
*  beliefs in neuroscience.
*  Now in neuroscience, typically you have a model where these connections are
*  fixed then, right?
*  No, you don't change them.
*  And I think this is probably not the way how brain circuits act.
*  Well, you don't change them until you need to, until you need to learn something.
*  Right.
*  But yeah, but we know that there's spontaneous pruning of synapses and growth
*  of synapses and, and that they're constantly changing over time.
*  And it's, it's a miracle, use the word miracle.
*  We're talking about churches.
*  So I'll use the word miracle that there is stable computational function given
*  this dynamic process of synapses constantly changing and their stochasticity
*  and the diversity of types.
*  I mean, it's, it's just amazing that there is, you know, how can there be
*  computational stability in that regime?
*  Yeah, I think this in principle, no, my, what my take home messages from the
*  modeling and theory that we did on this few years ago is that in principle, no,
*  even local synaptic plasticity rules or stochastic rules aren't principle able
*  to maintain the system level robustness and stability and always move the system
*  towards something that works better, at least, no stochastically then.
*  But then the open question is, no, these are now particular plasticity rules,
*  which have now a certain stochastic term.
*  And I don't know how close they are to the actual no plasticity of synapses.
*  And so in the next step, we would have to go back then to synaptic plasticity
*  and analyze it, you know, say from the perspective of the theory to see to
*  what extent it fits then.
*  And I find it unfortunate, apparently synaptic plasticity research is not so
*  popular anymore in experimental neuroscience.
*  Maybe it's just not too difficult.
*  And many neuroscientists also see that everyone everybody wants to see STP and
*  they can't produce it in their data.
*  Different wrinkles, right, which don't fit series.
*  So this is, again, the missed opportunity to bring these two communities together
*  then to have open minded theoreticians who really out for understanding what are
*  actually are these plasticity rules in different specific types of neurons,
*  particular context and neuroscientists who have now new tools to really know to
*  answer some of these questions then through the experiments.
*  So what you don't understand Wolfgang is that we've got plasticity figured out.
*  I don't there needs to be no more experimentation on it.
*  You see, but I mean, that is an interesting thing.
*  So plasticity is the standard story of learning.
*  And there are different types, you know, spike timing, dependent plasticity, long
*  term potentiation, long term depression.
*  But what do you think the legacy is going to be of plasticity and our current
*  understanding of it and how it functions and what it does in brains?
*  Do you think we have it all wrong or just an extremely incomplete picture of how
*  it's working in brains and therefore how we can even really theorize about how it
*  might work?
*  I think we have some bits of no truth then, but we extrapolated too much then.
*  And I think we know besides STP, actually, there's wonderful work which was done
*  now, I think, about 15 years ago about synaptic plasticity on dendrites.
*  And there are different rules in place.
*  There doesn't need to post synaptic spike.
*  And it actually this exhibits fast plasticity.
*  And this is something which is really postulated in most models then, but it's
*  not something which STP can provide according to any of the data.
*  If you look at, for example, this really thorough experiments of Frumke in New
*  York, who had published a paper about this, about this temple aspect that
*  typically synapse needs at least 50 to 100 pairings really to move into
*  direction you want to move it.
*  And so this doesn't fit together with we learn a new fact then and it's now in
*  our brain.
*  Yeah.
*  So this doesn't fit together all together then.
*  So I think, you know, that different types of plasticity and certainly I think
*  dendrites seem to play a role there.
*  I think what, but as me is also, we know so little about consolidation.
*  We think now often, you know, if you don't reflect about it, that consolidation
*  is somewhat a very simple and boring process where, for example, you know, the
*  most recent or the most important information is kept and the other one is
*  forgotten.
*  But there's evidence and it was now pointed out by Stigald and Wocken some
*  years ago, also in a very nice review paper, I think was called the memory
*  triage that consolidation appears to be really a very intelligent process where
*  new fact is scrutinized from the perspective to what extent does it fit
*  into already known schemes?
*  Whether it contradicts it or completely fits into this.
*  So therefore it's really something where new knowledge is really compared with
*  existing knowledge.
*  And it's then the decision about this new knowledge is done in a way which
*  builds a useful data structure there.
*  Within the context of existing knowledge, is that why as we age, we become
*  resistant to considering novel perspectives?
*  I don't know.
*  Yeah.
*  I didn't encounter this yet.
*  I think it's a cultural aspect probably.
*  Oh, probably so.
*  And you're young at heart and in that culture.
*  So, yeah.
*  But this is, I think, something which is really missing.
*  And I think it's a very difficult question because it probably goes deep
*  into molecular biology, right?
*  Into epigenetics then.
*  We know something about the signal cascades then.
*  I haven't seen any quantitative rules about the timing.
*  And I think now any theory about learning in a model for brain circuits
*  without consolidation is probably something very, it's only half of a
*  model then because the brain does use no consolidation in a strong way then.
*  And I think that we are missing this.
*  I think it had been approached in recent years with some interesting papers, but
*  they looked at the problem of consolidation only from the perspective of
*  avoiding catastrophic forgetting.
*  And this is for me a little bit to isolate or possibly even contrived
*  a functional aspect then.
*  Now, as I indicated before, the evidence from cognitive science is that
*  consolidation does something much more intelligent than just avoiding that
*  your memory overflows then.
*  And I think we need to formulate precisely what we need and then again,
*  bring theoreticians who ask these questions together with experimentalists
*  who are able to bring evidence from the experimental side.
*  I mean, consolidation too is one of the beautiful functions for it.
*  It's known that all of us have the capability of near infinite memory and
*  half of the job is just getting the memory out, right?
*  Retrieving the memory, right?
*  So if it's well consolidated, it might be easily retrieved as well.
*  So I think it's a very good point.
*  As I know, I think what one says about autism, autistic people, right?
*  No, they have some of them have an infinite memory, but they have the
*  problem really of really fitting this new contact content into the context
*  of the old content.
*  Exactly this intelligent part of consolidation is apparently not
*  working so well then.
*  But as you point out, not just putting new information, new items into memory
*  does not appear to be a problem really for brains then, right?
*  They really want to create meaningful data structures in the brain, not
*  just pieces of items.
*  So you, okay, so we just stepped through a bunch of biological features that
*  you think are important to think about for how computation can work in this
*  regime and not only are they important, but you take these constraints and
*  this is a thread that is just constant throughout your work.
*  You take these constraints and you approach it thinking about how they
*  could actually benefit computation.
*  What we think of as constraints could potentially benefit computation, right?
*  And we just listed these like the, how could variability benefit it?
*  How could stochasticity, how could the plasticity, et cetera?
*  What I'm wondering is, are there constraints that are detrimental or will
*  will we always find the constraint and think, ah, how can that benefit
*  computation and will there always be a benefit to computation or can we just
*  throw some away?
*  Are there some that just aren't going to help us that are actually unhelpful?
*  Yeah, yeah, I think I'm not aware of this.
*  And, but this may also really say something about the rich reservoir of
*  theories, right?
*  You have a theory for everything then.
*  You just have to change your tools somewhat and then you have a new
*  constraint and you find a theory which fits.
*  So this is just mathematics, you know, is that so rich then it's very hard to
*  come up with a scenario where just, you know, anything shares and say, I don't
*  have any theory really to apply there.
*  Although altogether there, I say, no, there will still be a struggling then.
*  I think we're missing, you know, a theoretical approach for understanding
*  dynamical systems, which consists of heterogeneous components, which have
*  their own dynamics on different time scales.
*  So this is really something which is, you know, a big stumbling block,
*  stumbling block, and it's right in the middle of this research there.
*  Okay.
*  So Wolfgang, we were running up against time and I wanted to go through, you
*  know, three of your more recent papers.
*  Um, I, let me just list them off and then I want you to sort of choose what,
*  what road we go down for just a few minutes.
*  Um, so one of the things that you've recently done is so recurrent neural
*  networks have come on the scene.
*  They're very powerful, uh, because they have recurrent connections like the brain.
*  So they can use previous information moving forward and computing things,
*  moving forward, a memory essentially.
*  Uh, and then along came long short-term memory LSTMs, which can hold onto
*  memories for longer and are, you know, they had this read, write capability,
*  which is trained in them.
*  It's not actually programmed in them.
*  Uh, and one of the things that you've recently done is you have created a
*  spiking neural network version of LSTM using biological, uh, properties known
*  that is adaptation in neurons.
*  So that's one thing that we could, uh, talk about.
*  Um, you've, you've also done a lot of work on this learning to learn or meta
*  learning, meta reinforcement learning framework.
*  Um, and all of these are really related.
*  And then another one, which, uh, you may want to talk about, because you mentioned
*  it earlier, which is E-Prop, uh, and this is using biological constraints to
*  basically replace, uh, back propagation through time in spiking neural networks
*  and implement a biologically plausible way for spiking neural networks to learn.
*  That has been really powerful and has, um, been able to, you'd been able to
*  train neural networks, spiking networks, basically to the same capabilities, uh,
*  as their cousins, as their, um, back propagation through time cousins.
*  Let's see what, you know, oh, and the last thing was just using, we talked about
*  liquid computing earlier, uh, and you've used, uh, reservoirs.
*  It's also called reservoir computing.
*  Liquid computing is one type of reservoir computing and you've used this
*  reservoir computing regime in the meta learning framework as well, the learning
*  to learn framework as well.
*  Well, what do you, what do you want to talk about before, before we wrap up here?
*  Yeah, maybe I say something now briefly about each of them.
*  So just one or two sentences.
*  Great.
*  Great.
*  I first want to say this is actually not my work, but it's the work of our group
*  then, and we have wonderful, uh, young researchers and I think also the
*  researchers, which are both are not theoreticians, computer scientists, and
*  they know quite a bit of neuroscience.
*  Uh, and I think we need more of this junior researchers who have this
*  multiple competence and interest and truly not to make progress.
*  So the first was no for many years, no, in the context of spiky neural networks,
*  we were looking for something which has similar function at this really no
*  strange LSTM units in artificial networks.
*  And it turned out, no, if you just throw into model, basically any kind of slow
*  process, which you want to, and we just took spike rate adaptation as a kind of
*  very handy and well-documented process, which seems to take place on the right
*  time scale, namely on the time scale of seconds, if you just put into the model,
*  then in this networks do acquire a functionality, which is comes very close
*  in simulations to LSTM networks, even for speech processing or hard, no benchmark
*  task. And so for me, it's just a lesson in really, no looking at the functionality of
*  slow processes.
*  So this is, I think, just the starting point for this then.
*  But also there's another kind of lesson behind it.
*  It doesn't work if you construct networks now with adapting neurons, then this only
*  works if you have sufficiently capable network learning algorithm then.
*  And you can use spec prop through time just to make it work in the model.
*  But now more satisfactory would be to have now more biologically possible algorithm.
*  And E-Prop is one proposition that we made now in this year, which seems to have
*  these properties. I don't want to say, no, it's proven that this biologically realistic.
*  But at the moment, we don't see a concrete aspect of it.
*  We can definitely say, no, this can't happen in neural circuits.
*  So again, it's a proposition for experimentalists to falsify this then.
*  But at the moment, we are happy and also actually know people who build spiking hardware
*  happy because in contrast to backpropagating through time, E-Prop is an online learning
*  method and therefore can be implemented on the chip then.
*  And so this is happening right now in two, in one company and one university lab.
*  You know, they're implementing E-Prop on their chips.
*  And this will probably become the most powerful on-chip learning method for recurrent
*  networks.
*  Cool. Well, and I just want to interject because E-Prop combines this eligibility
*  trace, this biological property of a fading memory in synapses with also a top-down
*  learning signal, which can be equated with things like dopamine neurotransmitters in
*  brains. So it's beautiful work.
*  And I wish we had more time to go into it.
*  But so it's going to be it's going to dominate neuromorphic chips, huh?
*  Well, we've seen I don't want to be modest.
*  And but I think for recurrent networks of spiking neurons, we don't have much else
*  than I think now here.
*  Now we see we don't get quite now to the level of of what can be done with backpropagation
*  through time. But I'm very happy, for example, one of our guys, Frans Scher, showed
*  that you can even a network of spiking neurons can learn to win Atari games then.
*  So this type of benchmark task was really not used to be deep in the home turf of
*  deep learning people, people know an industry, a deep mind.
*  And now we have a spiking networks who learns this without any human supervision,
*  just from rewards, no from making points within the game then.
*  So I think it's very nice to know that we no longer have a gulf in the type of task
*  we consider in models for brain circuits and the learning and the type of task which
*  are tackled in artificial intelligence.
*  And so I think it's very nice now that we can partially start to talk about the same
*  problems and then compare solutions and see to what extent they inspire each other
*  then. And the last word on meta learning, this is simply also which I think came
*  really from machine learning then was started, I think, by Sepp Hochreiter.
*  And it also has a root in neuroscience no longer go then, which is simply the
*  observation that we're doing something wrong when we model learning typically
*  because we take off the shelf a certain network and then we expose it to a certain
*  learning problem then. And no network in the brain is ever in the situation then.
*  Right. And so this simply takes us into account that there's a priming, probably
*  very sophisticated priming, through evolution, through development, through
*  prior learning then.
*  And I think these methods allow us to at least on a functional level to go through
*  some of these processes and in this way to get a better understanding.
*  And I think what I find most exciting about this, we find in this way you can also
*  get the capability of obstruction into neural network models then, that they don't
*  always work on the level of immediate central inputs at the pixel level, as one
*  says in machine learning, but they can more work on the level of obstructions,
*  relation between objects or other kind of abstract reasoning.
*  And I think this is something which is going to happen in the next few years that
*  we see how metals of spiking neurons can do reasoning, abstract reasoning also.
*  And so this is something that I always wanted to do.
*  I wanted to see how a model for network spiking neurons starts to think.
*  And I think this becomes possible within the next few years.
*  Wow, that's a great place to end it.
*  Quickly, though, you know, so you are really engrossed in these spiking neural
*  networks. What's your take on how deep learning folks think about spiking neural
*  networks? I know the neuromorphics people love it, but do deep learning practitioners
*  care about spikes?
*  Not so much then.
*  And I think the main reason why it's also of interest from the perspective of deep
*  learning where industries that know possibly spike based implementation of deep
*  learning can be implemented more in energy efficient way than.
*  So, you know, this is still something where the answer is out.
*  There are many, I think, over 40 startup companies working on this problem, building
*  energy efficient hardware for AI.
*  And we have to see whether spiking works or not.
*  But in a sense, I think the folks in machine learning, they're right in a certain way.
*  They say we possibly have not really captured what spike neurons are doing in the
*  brain then. And so therefore, by just throwing spike neurons into the model doesn't
*  necessarily make it brain like.
*  And my reading of this is that, sure, because we're missing so many aspects of
*  biologic neurons, which are not in traditional spike neural models, like all these
*  intermediate slow processes.
*  Right. And so therefore, these are so far not so genuinely kind of more complex or
*  more resourceful models then.
*  And so therefore, I think they're right then.
*  But it could be also that it happens more in other, in more complex work on deep
*  learning then. But at the moment, no, I think they're right now of ignoring it.
*  What is something that you used to believe that you now consider naive?
*  Being a skeptic, I can't really see something then, just because I'm very
*  skeptical about things and I don't believe so many things per se then.
*  And in a sense, I think the skepticism itself now has been proven wrong then.
*  So I like it very much.
*  One of the most famous neuroscientists in Europe, Wolf Singer from Frankfurt, says
*  in his talk sometimes he thought that neuroscience had a much more optimistic
*  perspective 20 years ago when we had fewer experimental data.
*  Now that all these experiments now have shown, now the simple theories don't work,
*  then things have become more complicated then.
*  And I think this tended to be always my approach from the beginning then.
*  And so therefore, I'm not so surprised by this effect.
*  Yeah.
*  I think altogether, if you want to think about the benefit of the field, of this kind
*  of also tentative growing together of neuroscience and machine learning and AI on
*  the other side, I think what is really is needed more workshops where we ask
*  questions which are cross-cutting of the type that you have raised then.
*  And I think as soon as people from either side have an opportunity simply to become
*  familiar with this main concept and result from the other side, they love it then.
*  Right.
*  So it's really the problem is not to create enough opportunities of this type then.
*  And it's not so easy because, for example, if somebody says, computer science, I want
*  to read up on neuroscience, what should I read?
*  I don't have an answer in the same hope for the other way.
*  Right.
*  So we need somehow to create at least a temporary curriculum and really work on this,
*  identify or encourage the students to try to understand both of these fields then and
*  then create bridges for them, which make it easier for them to cross these gulfs between
*  these areas.
*  I love it, Wolfgang.
*  Thank you so much for your time.
*  I kept you very late, and I would love to keep you all day.
*  So I'm sorry that we can't, but I appreciate you being here.
*  Thanks.
*  Thank you, Paul, very much.
*  And happy new year.
*  Happy new year.
*  Brain Inspired is a production of me and you.
*  You can support the show through Patreon for a microscopic two or four dollars per month.
*  Go to braininspired.co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show and prohibit any annoying
*  advertisements like you hear on other shows.
*  To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year.
*  Find them at thenewyear.net.
*  Thanks for your support.
*  See you next time.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.
*  Hey.

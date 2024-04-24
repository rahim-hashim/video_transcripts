---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5213s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 10986
Video Rating: None
---

# BI 131 Sri Ramaswamy and Jie Mei: Neuromodulation-aware DNNs
**Brain Inspired:** [March 25, 2022](https://www.youtube.com/watch?v=cr4dLXRFwvc)
*  The goal is to try and build neuromodulation-aware deep networks that are informed by principles
*  of neuromodulation, simply because there is no one-size-fits-all for neuromodulatory function,
*  and it really depends on the brain region, the neuromodulator, and the cell type.
*  We just wanted to open this discussion that there are all these neuromodulatory effects
*  at different levels, including the fine dendrites, and the cell can really behave differently
*  under different contexts.
*  And I think that's also one point of the paper.
*  And so we really want to bring that into the scope.
*  Hey everyone, it's Paul.
*  So on the previous episode, I had Eve Martyr on the podcast.
*  And one of the things that Eve has done, among many others, during her career, is study the
*  effects of neuromodulation on neural networks, in her case on a rather small neural network
*  in crustaceans.
*  But that conversation focused more on overarching principles and less on neuromodulation itself.
*  On today's episode, I speak with Srikanth Ramaswani and Jhe Mei.
*  So Sri recently started his neural circuits laboratory at Newcastle University, and Mei
*  is a postdoc at Western University.
*  And I thought it would be a good time to have them on because they recently collaborated
*  on a review that is focused on how principles of neuromodulation might benefit deep learning
*  networks.
*  So in this episode, we dig deeper into neuromodulation itself and how it affects brain states and
*  dynamics and how these principles might improve deep learning models, both in terms of their
*  capabilities and in terms of modeling brains.
*  So in the computational neuroscience world, there's always the question of how much biological
*  detail is needed to create good models.
*  And of course, the answer depends on the question that you're asking.
*  But Sri and Mei believe that as we learn more about neuromodulators and different neuromodulator
*  systems and how they interact to affect the landscape of ongoing neural net activity,
*  it could lead to big improvements in model function without necessarily needing to just
*  keep scaling up to bigger and bigger models.
*  And they believe we're just at the beginning of understanding those neuromodulation principles.
*  And it's clear that we're at the beginning of efforts to incorporate them into deep learning
*  models.
*  I also solicited a guest question from Mack Shine, who has been on the podcast before
*  and is also interested in these topics.
*  You can find the show notes at braininspired.co.uk slash podcast slash 131, where I also link
*  to the review that I mentioned, which is called Informing Deep Neural Networks by Multiscale
*  Principles of Neuromodulatory Systems.
*  Thanks for listening.
*  Enjoy.
*  I wanted to start a little bit with your background.
*  So Sri, I know that you were a big part of the Blue Brain project, which is a very different
*  beast.
*  So, how did you and we'll talk about that project a little bit more in relation to this,
*  but how did you come to be interested in neuromodulators?
*  So as you said, when we were trying to tame this whole beast, this detail model, probably
*  that we ever built on the somatosensory cortex, well, we integrated all this hard one anatomical
*  and physiological data at the cellular and the synaptic level and integrated this really
*  into a complex microcircuit level model.
*  But when we turned on the switch, when we simulated this model, we were slightly disappointed
*  because the model wasn't doing anything terribly exciting.
*  All it was doing was to fire in highly synchronous bursts of action pretensions.
*  So that really got us wondering, I mean, what is this model doing?
*  It's almost resembling like an epileptic cortex.
*  So what do we need to do to get it right?
*  And that was when there was a bit of a eureka moment when we realized that, hey, look, we've
*  been building this model based on data obtained from brain slices, which are all typically
*  done at high levels of extracellular calcium.
*  But lo and behold, in the intact brain, the levels of extracellular calcium are actually
*  lower, about 1 millimolar, 1 to 1.2 millimolar.
*  So what we then realized was we had to drop the levels of extracellular calcium in this
*  detailed microcircuit model for it to try to do something similar to the intact brain.
*  And that's when we came about, that's when we thought about ways to really decrease the
*  level of extracellular calcium by reducing the transmitter release probability of synaptic
*  connections in the model.
*  And then the emergent dynamics of the model began to make a lot more sense.
*  It was a lot more desynchronous that kind of collaborated with what the intact brain
*  was doing.
*  But the brain has myriad ways of doing this.
*  So of course, changing calcium is probably one way that we could do with this model.
*  But another way, another huge spectrum that the brain tries to employ to change these
*  network dynamics is through neuromodulators like acetylcholine.
*  So acetylcholine, the way it acts, for example, to change the brain from sleep to wakefulness
*  is really by modulating network activity from synchrony to desynchrony.
*  So that's when we realized that there could also be other mechanisms at play to bring
*  about this change in network dynamics.
*  And that's really what got me interested in neuromodulation.
*  So Mei, how did you come to be interested in neuromodulators and neuromodulation?
*  So I have a background as a computer neuroscientist.
*  And I did a computer neuroscience project, of course, in my master's studies.
*  And I was working at the senior S near Paris.
*  I was hosted by Yves Renac and Andrew Davidson.
*  So like this thing, I started working to simulate the sensor perception in the visual thalamus.
*  And we had a really biologically detailed model, which means we use morphologies, compartments
*  of the entire neuron to make a neural network.
*  So we call that neural network because that represents the detailed characteristics of
*  neurons.
*  So that's why we call that neural network.
*  So we also had recorded cell responses from, for example, the thalamic cells, including
*  the principal cells and also reticular cells.
*  And the motivation of this project was that one of the PhD candidate at the lab, he was
*  trying to do the same using a different simulator called NEST.
*  And he was not really able to capture or replicate the properties of visual thalamus cells that
*  they have recorded and observed in the experimental study.
*  So that's why we discussed that might be an interesting chance to introduce more biologically
*  detailed modeling work.
*  And at that time I was using another simulator called a neuron simulator.
*  And we kind of played with the really fine mechanisms, including the L channel kinetics
*  and as well as neuromodulators using the mock files of the neuron simulator.
*  And we actually saw a big difference when we had these mechanisms really implemented
*  in details were partly impaired.
*  And also I was really able to replicate this visual perception phenomena we have observed
*  in reticular cells and principal relay cells biologically.
*  So that's how I got interested in the whole thing, because having these mechanisms can
*  really introduce the big difference in the neuronal properties as well as the network
*  properties and also the connectivity in between neurons.
*  And I think this is a big drive for me.
*  Because I have also seen other approaches in computational neuroscience that are there
*  using primarily point neurons and linear simulating after the same thing, we see big differences.
*  And also in deep learning is more even more abstract.
*  We have unit units as neurons that are storing for the error and for the back propagation.
*  So I think after seeing all these different approaches got even more interesting how we
*  can add this biological realism to this model to make a difference.
*  So in some sense, both of your background work has focused on more or less a bottom
*  up approach, right?
*  So you can go through all the details and run the simulation and kind of see what happens.
*  But deep learning networks is a different beast, right?
*  It's very much a fit whatever model you do build, however much biological detail there
*  is fit it to some behavior based on some behavior, which is, in essence, a top down approach.
*  And you know, I know, like one of the criticisms, at least of the blue brain project is that
*  the bottom up approach of just building all the details, turning it on, running it and
*  seeing what happens is fundamentally flawed, right?
*  But I know you both appreciate both the bottom up and top down approach.
*  So how do you guys think about bottom up versus top down?
*  And Sri, I don't know if you want to just respond to like that kind of criticism of
*  blue brain in particular, but just in the larger picture, bottom up versus top down.
*  Right.
*  I think what this convergence of bottom up versus top down biases is.
*  So traditionally, all these top down approaches have been a bit ad hoc because they've always
*  been built to reproduce a very specific phenomenon, right?
*  So these top down models are great at reproducing something specific, but they probably can't
*  reproduce something that's a lot more gender.
*  Whereas on the other hand, what a bottom up approach affords us is a framework or a reference
*  that could be used to try and understand what level of detail is required to model what
*  phenomenon.
*  And then based on what level of detail is required, I mean, you could then just shave
*  off these details and then only focus on what matters to contribute to a certain phenomenon.
*  So in some sense, I think a purely bottom up approach is really a beacon, a guide to try
*  and tell top down approaches on what details matter and what could be included in order
*  to reproduce a specific phenomenon.
*  Because otherwise, I think if these two approaches don't come together, I think it's a bit of
*  a groping in the dark because indeed top down models can tell us a lot about what's happening,
*  but they might not really be able to pinpoint what are the finer details, the cellular and
*  the synaptic details, for example, that are responsible to shape a certain phenomenon.
*  So this is where I think the convergence of bottom up and top down approaches is very crucial.
*  So mostly people will say there is actually a clear dichotomy between top down and bottom up.
*  But I mean, I've seen people really driving through this research using a hybrid approach,
*  for example, that has been used in the philosophy of computer neuroscience.
*  One of the examples I've seen is a lot of desk textbooks published in 1999, I think.
*  And I think he was trying to work on a reticular cell, a principal release cell,
*  again, like the thymic cells.
*  And the thing he was doing is that he has really detailed morphological reconstruction of this cell,
*  so up to more than two hundred compartments within a cell.
*  And he also wanted to see what's the level of detail he required to replicate the sensory
*  phenomena. And he also tried to reduce the amount of compartments in this model to,
*  I think, around 70 or three or 10 or something.
*  So I think also within the computational neuroscience community, there are a lot of
*  people that are interested in trying to find the more gross details that are required to replicate
*  without going into too much detail. Because otherwise, we may require a lot of computational
*  power to really have a model running, especially considering that the brain has a great amount of
*  neurons. And if we all incorporate this kind of level of details into that, it's going to
*  lead to endless simulations.
*  Yeah. And in the meantime, I think what's interesting about the current trends in the
*  deep learning community is that we have more and more work coming in the directions of having
*  a hybrid model in between these two approaches.
*  For example, we have, I think, from Blake Richards' lab in 2017, where they had a deep neural
*  network. But for the single units, they have tried to replicate a compartmental setting.
*  So they had an apical dendrite instead of just a single neuron. And in the meantime, we have also
*  seen work from DeepMind where they tried to capture the faring of these DNA cells or the
*  activity in itself throughout the field when the agent is navigating. So I think we have gradually
*  a more recent appreciation of this hybrid approach by really having some top-down
*  approach. And we try to add more finer details to see if that's leading to something different.
*  So thinking back to the early days of neural networks, in one sense, that was bottom up because
*  it was saying, well, the brain is made up of neurons, so let's make a network of neurons and
*  then kind of go from there. But of course, then the training to do tasks is the more top-down
*  approach. So we'll talk about neuromodulators. And you give examples in the paper of various
*  neural networks incorporating neuromodulation into the networks. And then, of course, there's a call
*  for more of that. And May, you're talking about even using dendritic computation to build that
*  into neural network models. And of course, there are even neural network models with glial cells
*  and their functional roles. So in some sense, it's... Well, I don't know if it's a small trend or...
*  In some sense, it's a trend to see if these different kind of detailed microcircuitry and
*  inductive biases, dendritic computation, neuromodulation, in some sense, there is a
*  push to start building these things into the models. But like you said, it becomes intractable
*  computationally. So my question, I suppose, is, what is the right level of abstraction? And you
*  might just echo what you just said, that we have to figure out what is needed to constrain. I mean,
*  Sri, you were talking about the original modeling the calcium in the system and then having to
*  change that. And then that's what got you onto neuromodulators in the first place. But it's almost
*  overwhelming to think about the detail to add into a neural network computationally, demandingly.
*  So how do we know what the right detail is? The so-called right level of detail or the correct
*  level of detail really depends on the kind of questions you want to answer. So Chris Elias-Smith
*  wrote this review many years ago. If I remember correctly, the title of this review is the use
*  and abuse of large scale neural network models, something along these lines. So it really boils
*  down to the kind of question you want to ask. So if, for example, I would like to know the role of
*  oblique dendrites of layer five pyramidal cells in modulating gamma oscillations in the neocortex,
*  then I better model them. Otherwise, I won't know what these dendrites are doing. So it really
*  boils down to the kind of question you want to answer. And yes, sure, adding all this detail
*  might seem daunting. But to a certain extent, it's not about this all-encompassing model
*  that's like a silver bullet. But it's more of like a framework that lets you add the kind of
*  detail you would like to. And then if at the end of the day, you realize that this detail is not
*  letting you answer the kind of questions you want to, then sure, feel free to isolate this level of
*  detail and then see what really is contributing to the kind of phenomenon you would like to explore.
*  So in that sense, I think detail is not daunting. It is necessary. But what we need to understand
*  is how to incorporate this in the most economical way possible. Because adding more detail, of course,
*  as May said, implies a lot more computational power. So there's the need to be judicious about
*  adding detail. But on the other hand, this detail is there for a certain reason. We don't know what
*  the reason is. So unless we have some room, some place, some placeholder to include this detail,
*  we'll never know what this detail is actually contributing to what we'd like to study. So
*  I'd again like to reiterate on the fact that the level of detail depends on the kind of questions
*  you'd like to answer. I feel that in part from the question itself also depends on the...
*  There are some other factors that are more realistic. For example, the budget you have,
*  the duration of the project, and also computational power you have. So sometimes we are bound to the
*  amount of machines we have and we cannot really go into any further details. And I think there is
*  also something in addition to this point is that in some cases, the brain's energy consumption is
*  actually one interesting question. So it optimizes itself in some way. So it optimizes the cost
*  function or it optimizes the neurons, the way the neurons are communicated and how the connectivity
*  is enhanced or reduced in a certain area and uses sleeps and rest cycles to restate some certain
*  states of the brain. And I think these are quite interesting as well, because there are actually
*  some active neuroscience research studying why the brain is so energy efficient. And this is
*  something we can also try to think from a perspective in a way that we can maybe potentially tackle this
*  highly computationally costly problem that we have in deep neural networks and also biologically
*  detailed neural networks. Yeah. Right, Mei, but yes, I mean, resources, that's something.
*  But on the other hand, let's assume you had infinite resources, right? So what would you then do?
*  Where would you stop to add all these details? So that's another thing. Would you go down
*  to the level of proteins or single genes? What would you do?
*  I agree with what you said. Yeah. Yeah. So the question matters.
*  Right. So, I mean, ultimately, I think to some extent, it boils down to what you'd like to answer.
*  So sure, the energy consumption part, that's indeed very important.
*  But that also boils down to what computing resources we have. I mean, whatever computing
*  architectures we have right now are quite energy greedy. So at the end of the day, perhaps to make
*  these computing architectures also more energy efficient, we would need to understand how the
*  brain is implementing this energy efficiency. And to do that, perhaps we need to build models
*  of some level of detail. Otherwise, we probably wouldn't know why the brain is so energy efficient.
*  Right. So I think it's a bit of a chicken and an egg problem in my opinion. So.
*  So I personally prefer that if I have sufficient details that make something work, I won't really
*  go into any more details unless the details are the things I wanted to study. So what I think,
*  I think Shuri is right on the point that it depends on the question I wanted to answer. If I
*  wanted to replicate a cognitive processes or phenomena. So in that case, if the details I have
*  are sufficient, maybe I'm going to just try adding more detail to try to play with that. Yeah. Like,
*  but if I wanted to study the details themselves, I definitely want to go into another level of
*  details. So it depends. Yeah. And also there's really like no right or wrong level of details
*  because we also like, we all say that all the models are wrong, but some are useful.
*  So, you know, in that way, I think the right level depends really depend on the question you
*  wanted to answer. If this is a thought experiment that we have, you know, unlimited power and
*  computational resources. So I think that's a point of, you know, the first thing you want to
*  define is a question you want to answer. And then what are the models you can potentially use to
*  answer this question? And then like, what is the main most simplistic model you can try to go from
*  and what is the level of detail we want to stop with maybe. So that's how I would frame it.
*  Yeah. So Mei, you just said the right level of detail is the level of detail that makes it work.
*  And Sri, when you were talking, you alluded to Chris Elias Smith, who's been on the podcast,
*  and his viewpoint. And one of the things that actually Chris Elias Smith focuses on is,
*  for his purposes, what makes it work is if it matches behavior, right? So he has this cognitive
*  architecture spawn. And in the paper that you guys wrote, you go through a lot of
*  literature detail in neuromodulators and how they're related to our cognitive functions and
*  what we know about how they interact and the different mappings of a particular neuromodulator
*  onto various cognitive functions. Do we know enough about, so, you know, for example, like
*  dopamine, right? So the classic reward prediction error, that's what it is, except that's also,
*  it also plays like 17 other different roles that are being discovered all the time, right?
*  And then you have on top of dopamine, you have all the other neuromodulators. So for instance,
*  Sri, I know you're interested in histamines specifically, among others. Do we know about
*  the relation between neuromodulation and cognitive functions and behaviors and how
*  the neuromodulators interact? Or is that part of the project to learn more about these things by
*  developing them into deep neural networks? Okay. I think it's a bit of both because we definitely
*  are really at the tip of the iceberg when it comes to neuromodulating function.
*  So what these neuromodulators are probably doing is analogous to a relay race, right? So
*  one neuromodulator sets the stage for another to take over. So one neuromodulator passes the baton
*  onto another neuromodulator to take over, to then capitalize on a platform that's already built,
*  to then prime the brain to do something, right? So neuromodulatory function depends on brain state.
*  And for the brain to reach a particular state, it needs to activate certain neuromodulators,
*  right? A combination or whatever. So it's really this synergistic effect that's going on throughout
*  where the brain needs to get to a certain state and you can't get there without neuromodulators.
*  And these neuromodulators are constantly priming the brain to get to a particular state.
*  Like so in this way, it's a very synergistic problem. And we're only beginning to appreciate
*  what these permutations and combinations in terms of neuromodulatory effects are. But a lot of this
*  is being studied at the global level, at the behavioral level. So while we appreciate that
*  a certain neuromodulator like dopamine, as you said, which is probably doing 17 different things
*  in addition to reinforcement or reward prediction error, there are also other neuromodulators that
*  are very likely causing the dopaminergic system to execute these functions, right? So we like studying
*  what's happening at the global level, but there's a lot, lot more that's happening at the local level
*  because there are a lot of different cell types. Like let's just take the example of the new cortex,
*  right? So I've tried to build in collaboration with the Blue Brain Project, a little crumb of
*  the somatosensory cortex that's roughly the size of a grain of sand, right? About 0.3 millimeter
*  cube of cortical tissue. So this little crumb of cortical tissue has about 55 different morphological
*  types. So combinatorially speaking, 55 different morphological types, assuming all to all connectivity
*  would lead to 55 square or 3025 possible synaptic connection types. But we know again, by virtue of
*  axo-dentity geometry, that only about 2000 or so of these 3025 combinations are biologically viable
*  because the axons of some cell types cannot reach the dendrites of others to form synapses,
*  so on and so forth, right? So over the past 50 years or so, we've been doing whole cell recordings
*  of these synaptic connections. We only have quantitative data on 20 or so of these synaptic
*  connection types. So that's less than 1%, right? Of the 2000 or so biologically viable connection
*  types. And of these 20 or so that we have data on, we probably know what a neuromodulator like
*  acetylcholine might be doing to less than 10 of these combinations. So the data on the effects
*  of neuromodulators on synaptic transmission alone is extremely sparse. We just don't know what's
*  happening at the local level. So the need of the art to try and understand neuromodulation is to
*  build these bridges between what's happening locally at the cellular and synaptic level,
*  and then try and connect this to what could be happening at the global behavioral level,
*  but we are not there. So of course, this asks the question, is there any incentive in doing
*  all these 2000 or so whole cell recordings and applying acetylcholine? There probably isn't.
*  So we need to come up with clever ways to try and understand some predictive patterns on what
*  could be happening at the cellular and synaptic level due to a single neuromodulator like acetylcholine.
*  It could be that pyramidal cells all have similar receptors expressed on their dendrites for acetylcholine.
*  So perhaps acetylcholine could be having the same kind of effects. We don't know. So unless we break
*  down this problem into something a bit more tractable, it's going to be a real challenge
*  to understand what these neuromodulators are doing across cell types, even in a small part of the brain.
*  So I think the need of the art is to really try and come up with approaches to bridge levels of
*  detail to try and understand how the local modulation, the local effect of neuromodulators
*  translates into something more global, something at the behavioral level.
*  Yeah, so I think what's interesting about the neuromodulators is that there are a lot of more
*  modern technological approaches allowing for different explorations from the
*  in vivo, in vitro, and in its local perspectives. So according to what Sri said, there are many
*  kind of interactions across the types of neuromodulators. For example, as he mentioned,
*  dopamine can only achieve its goals under the modulation of other neuromodulators such as,
*  I think, acetylcholine as well as serotonin, because there are opponents existing between
*  serotonin and dopamine. They're counting for punishment and rewards, respectively. And it
*  also has a lot of implications in cognitive disorders. And of course, another kind of a
*  principal example is cholinergic regulation of dopinergic cell activities within the basal
*  ganglia that has a lot to do with the movement initiation execution in Parkinson's disease.
*  So I mean, I think what's interesting to us is that we have seen these neuromodulatory processes
*  all different spatial temporal scales. And these are from one aspect, these are not so finely defined
*  in deep neural networks. So this is something we can try to incorporate. And there are a lot of
*  evidence on that computationally and experimentally. And of course, we computer neurosciences, we do
*  use different approaches. And of course, we can try to work with deep deep learning practitioners
*  to have a hybrid approach between biologically detailed modeling and deep neural networks.
*  The second thing is that we are not only using competition models to kind of replicate it,
*  we also wanted to use these models to have a better refined computational hypothesis on how
*  these areas might be interacting with each other. For example, if you're trying to use an in vivo
*  approach to kind of a patch clamp some cells in a certain brain area, for example, like the midbrain
*  nucleus, such as the basal ganglia striatum, for example. And these are some areas that are really
*  hard to reach using the traditional experimental approaches. So yeah, I was really fortunate when
*  I was working at Gili Silberberg's lab in 2015. And I witnessed kind of the first patch clamping
*  session in the world on cholinergic neurons in the basal ganglia. So I mean, yeah, it's really
*  nice for me. I was working with Ramon and a really experienced postdoctoral researcher at that time.
*  So I mean, for these areas, my point is that it's really hard to explore, you know, in vivo and
*  we used awake behaving animals. And these experiments are really hard to conduct,
*  because the animals are kind of performing and behaving all the time. After they receive this,
*  for example, like sensor stimulus from the viscous or stuff. And also like these areas.
*  These are patch clamped?
*  Yeah, patch clamps.
*  Awake behaving? Because I'm going to ask you a technical question in a second about that. Okay,
*  go ahead. Sorry.
*  And then like these are areas are hard to patch from. And sometimes we have more
*  two neurons per day, that's already good enough. And so definitely if we can kind of replicate
*  certain experimental conditions in computational models, that's going to help us have better
*  computational, you know, hypotheses, and that can be tested using experiments further. So I think
*  these experimental approaches and competition modeling really goes in a cycle and promote
*  here in a certain way, because we have better experimental results, we have more biologic
*  constraints in modeling. And if we have better models, we may have better hypotheses on what
*  the biologist is doing. So I think this is a quite, we are not only using this to really make better
*  models, but we also use mechanistic models to create better hypotheses. So that's what I wanted
*  to say here. Yeah.
*  Yeah. Okay. So one of the drives for this, right? So from what you guys are saying, one of the drives
*  for building in a neuromodulator at multi-scale, multiple different scales,
*  and in multiple levels of detail, building them into deep learning models is to help us understand
*  actually what's going on in the brain, right? And that's a lot of what we talk about on the podcast
*  is using deep learning AI methods to help us understand what's going on in the brain. But as
*  I was reading your review, I thought the other way to go would be like, why not
*  invent new neuromodulators for deep learning models and to see what they can do, right? Like why not,
*  instead of constraining the neuromodulators thinking, well, acetylcholine does this in the brain,
*  so let's build it in like that in a deep learning model. Why not invent a new neuromodulator that
*  you somehow fit in the model, right? If we did that, would it come out that it would behave like
*  acetylcholine and then acetylcholine and histamine would interact the same way? Would we find that
*  they interacted the same way or would there be other emergent properties that are good for
*  the way that the models function? Sorry, it's kind of an out there question.
*  Well, that's an interesting question, I think. And so, right now, I don't think there are deep
*  network models that try and incorporate mechanisms of specific neuromodulators,
*  perhaps in reinforcement learning, but they're all focused on dopamine.
*  That's what you've sort of proposed, right, in the paper?
*  Exactly. Yeah, exactly. Yeah, exactly.
*  There's a different story for neurobotics because if you consider deep learning,
*  so it's primarily people that are interested in dopamine. And if you go to a bit of neurobotics
*  research, I mean, there are research done by certain neuromodulators, for example, studies
*  done by Krishmar, and he has actually proposed different roles of individual neuromodulators
*  and tried to implement that all in one of the robot models. So I think all the different fields
*  that take different approaches, and definitely we have seen more natural interest in reinforcement
*  learning regarding dopamine. And I think one recent proposal by Uchida from Harvard is that
*  we can try to incorporate acetylcholine in parallel with dopamine because these two interact a lot.
*  So yeah, we have seen some interest in that field, but I think according to our knowledge,
*  our paper is actually kind of the first one to kind of try to push people to pay more attention
*  to other neuromodulators, even apart from the ones we mentioned in the paper. Yeah, also there's
*  histamine, there's neuropeptides as well. So yeah, I think that's quite important. And also, you
*  mentioned we may use another neuromodulator that's not really like a biological neuromodulator in the
*  brain. I think, I'm not sure about that, but I think there are some commentary facts achieved
*  by having these neuromodulators working that in your brain. So maybe the novel neuromodulator
*  proposing is actually like the effects equals what we have when the neuromodulators are working
*  in combination, right? So that's a possibility. But then it would be redundant because then if
*  you're also modeling the two neuromodulators that then have that effects when they're working
*  together, then why add a third, I suppose. Right. But then this just reminds me of an ingenious
*  study where they invented a neuromodulator and they called it backpropamine.
*  Oh yeah, yeah, yeah. Right. But somehow the role of backpropamine
*  as is pretty self-explanatory was kind of limited to backpropagation, which is interesting in itself.
*  But we know for a fact- But it was invented for backpropagation.
*  Yes, you're right. Yes. So it was invented for backpropagation. But indeed, I mean,
*  there's clear evidence that depending on the kind of neuron and the brain region,
*  and the neuromodulator. So this is like really, you know, like a 3D problem, a neuromodulator,
*  the brain region, and the cell type, that of course, the definition of backpropagation in
*  machine learning and the backpropagating action potential is a bit different. But nevertheless,
*  these neuromodulators seem to have very specific effects in actually modulating the so-called
*  backpropagating action potential in itself. So yes, I mean, there could be completely new
*  functions for neuromodulators in only modulating the so-called backpropagating action potential
*  itself. So perhaps a fictitious neuromodulator like backpropamine could actually
*  tell us something very new. So indeed, yes, there could be a new neuromodulator. We have no idea
*  about it. Yes. Okay. But to add one or two sentences to that study called backpropamine,
*  actually, they were probably spared by the heavy learning, you know, when they were trying to build
*  the connectivity in between neurons. And also, they had a kind of a retroactive version of
*  neuromodulation where you use actually like dope mini-spared mechanisms for the change of the
*  weight. So I think it's also, you know, it sounds like something totally novel, but actually it has
*  the roots in, you know, in dope as well as heavy learning. So yeah, it's not like 100% novel or
*  makeshift or made up neuromodulator. Yeah, but it's actually a novel work by combining
*  the fact that it's the connected level as well as the neuronal level. So I think that's quite
*  interesting study. But what you're proposing in the paper, and please correct me if I'm wrong,
*  is using what we do know about neuromodulators and their role in cognitive functions to build in
*  kind of to constrain the models in that way. Indeed, that's correct. So as the title of the
*  paper itself says, so the goal is to try and build neuromodulation aware deep networks
*  that are informed by principles of neuromodulation, simply because there is no one size fits all for
*  neuromodulatory function. And it really depends on the brain region, the neuromodulator, and the cell
*  type. Also, possibly the domain in a particular cell type, because there could be different
*  receptors that are expressed in dendrites and axons. So indeed, yes, this is really the proposal,
*  the grand proposal. And this is the direction that we would like to pursue.
*  Yeah, I mean, also, I think this is pretty much like a demonstration of what neuromodulators in
*  the brain are doing. And we are aware of some of the problems the deep learning community is
*  trying to solve. And these are problems that are tackled by the brain using this kind of
*  adaptive design by the neuromodulatory system. So we think we can maybe provoke some thinking
*  in these newer directions and maybe we can showcase, okay, this is how the brain does it by
*  having a neuromodulatory system. I mean, this is not a unified solution to all your problems,
*  but these are like how they're tackling specific individual problems, using all these systems
*  and processes. And we wanted to kind of attract people and make them maybe ponder a bit more
*  within this field. Yeah. All right. So here's an unfair question I want to ask both of you. So
*  it's two questions in parallel on a scale of zero to 100, zero being like nothing and 100 being
*  solved or perfect knowledge or something. So the first question is, where are we in our understanding
*  of biological neuromodulators and their interactions in the whole world and how
*  their roles, right? Zero to 100. And of course, there's a much longer history. And then the second
*  question is, where are we zero to 100 in terms of exploiting the potential of neuromodulators in deep
*  neural networks? Okay. I probably take the first part. So where are we in terms of understanding
*  neuromodulatory function, the role of biological neuromodulation on a scale of zero to 100?
*  Yeah, because you don't know what you don't know, right? I'll be very generous. I'll say three,
*  maybe. Three. Okay. Yeah, that's generous. Yeah, because the first step it takes you to know,
*  like the big step is that you know what you don't know. So we don't know what we don't know. And
*  that's one of the biggest issue here, right? So we don't know what's the boundary of this whole
*  field. And it's making us even more not so confident when we're faced by this kind of
*  questions. So would you go higher or lower than three? I initially thought it's around 10 or
*  something. But since three is set three, and he has a, you know, definitely a more say than I do
*  when it comes to experimental studies on neural modulation. So I mean, I'm going to take it down
*  to five or yeah. Okay, so then, yeah. So just to add to my choice of three. So three is simply
*  because, I mean, we've always been studying neuromodulators mostly, or rather the function
*  of neuromodulators, as though it's always a single neuromodulator that's doing something.
*  Yeah.
*  Primarily because a lot of this knowledge comes from slice physiology, where the approach has
*  always been to apply a certain agonist to the path and look at what's happening at the level
*  of cells and synapses due to a particular neuromodulatory agonist. But this is clearly
*  not how things are implemented in the intact brain, right? Like, as you said, Paul, there are
*  all these interactions, and we simply have no idea to try and quantify these interactions. Of course,
*  now we slowly beginning to have the tools where it's possible to like genetically, or rather express,
*  I don't know, ways to monitor, to simultaneously monitor the function of multiple neuromodulators
*  through genetically expressed encoders and things like that in neurons. But
*  I mean, we're still getting there, and we definitely have a long way to actually
*  try and understand how neuromodulatory interactions are actually shaping a brain function.
*  So hopefully, I'll be a lot more generous and predict that three could probably go to around
*  five or six in the next few years.
*  Yeah, okay.
*  Optimistic, yeah.
*  Well then, so the parallel question, and May I'll ask you to answer this one first, right?
*  Where are we zero to 100 in terms of the potential of exploiting neuromodulation function
*  in deep learning?
*  You mean the potential or the progress?
*  Yeah, well, progress, I suppose. And the potential is, let's say the maximum potential is 100.
*  Yeah, I mean, the progress is really, I would give it a...
*  She's going to go conservative, much more conservative now.
*  Something under five, yeah. Why is that one not exceeding 10?
*  Why is that one not exceeding 10? Something under five? Yeah, because we have...
*  So if you read, there's a couple of papers using so-called artificial neuromodulation,
*  artificial neural networks, they have defined neuromodulation in a really loose term.
*  So something that's adaptive, self-adaptive, and self-adjusting, self-refining based on feedback,
*  or something that is locally applied to a certain population of a neural network,
*  and this factor can go adjusting itself, is called neuromodulation. So it's a really
*  loose definition of neuromodulation. I don't know if this is being critical or something,
*  but it's definitely a fancy word to use by people. And of course, they have demonstrated
*  different behavior benefits and learning benefits from having more adaptive mechanism in their
*  studies. But we really have a loose definition of neuromodulation. It's not always biologic
*  plausible, and they have been applied to neural networks of relatively small scale. So for example,
*  we have reviewed a couple of studies in the paper as well. So we initially had a table dedicated to
*  that. Yeah, but we found... So most studies we have observed in this field, so I think it's up to 10
*  or something, if you add, neurobotics is going to be around 15, 20, because we have more studies
*  actually in this from the neurobotics side. So, but if we only discuss in pure DNA approach,
*  I think mostly people were using these mechanisms smaller network because they have a better see
*  through of what it's doing from the inside out. Yeah, and they were really applied to really tiny
*  networks of sometimes naturally around 100 neurons. So they were trying to observe what each neuron is
*  doing under different neuromodular factors that are kind of scaling up the connectivity in between
*  neurons, where they were trying to see if a simple network can adapt or can learn kind of a different
*  association between stimulus and response, you know, if we add a richer number of neuromodular
*  factors. So I think from the scale of a neural network we have been using to investigate
*  artificial neuromodulation is kind of a homogenous, it's always mostly a small network. And we have
*  only seen more two studies applying this kind of a thing to a larger network from the connectivity
*  level. For example, the Mikoni paper is actually the back problem thing, Shree discussed. And
*  also from the implementation level, they're like, re-implementing all different ways. For example,
*  it can be represented by a hyper network, it takes input from the deep neural networks and computes
*  the hyperparams they wanted to modify upon each sampling, or it can be like represented as a
*  novel activation function, or it can be represented as a scaling factor that are applied to the whole
*  population, or overlapping or non-overlapping subpopulations. So again, see, there's a really
*  wide, I mean, you get to the definition of neuromodulation and the people are trying to
*  inject this into a neural network in different ways. So we all have different takes on that.
*  And I hope there's a chance we can, you know, having neuroscientists and deep learning
*  practitioners work together to have something that's more detailed, that's more in between.
*  And we can test this in kind of different architectures. And I think this is something
*  interesting, Rush, I'm currently probing at Western and wanted to see more of these work
*  coming instead of having a really lucid defined and heterogeneous kind of object
*  hips and studies. But of course, having different objectives, saying that we have observed the
*  benefits at different level from different aspects. And that's also one interesting,
*  I think, particularly interesting thing of current ongoing studies in this field.
*  Very good. Shreya, you need to say your number on the scale. And then,
*  because I wanted to respond to that, but I've got to make you say your number as well. And the why.
*  I would still say, yeah, it's certainly much below 10. Let me stick to five now,
*  or maybe even lower than that. Because, yes, as May said, I think, indeed, so it's not like
*  there haven't been any attempts to include neuromodulation in deep networks. But on the
*  other hand, as I mentioned before, it really boils down to what element of neuromodulation
*  that one would like to include in these deep neural networks, because it again, really depends
*  on the brain region, the cell type, and the neuromodulator. And right now, we still,
*  at least in terms of implementing these details in deep neural networks, we're definitely not
*  there yet. Because, of course, we are, of course, very handicapped by the biological knowledge
*  itself. And it's another process to try and transform this biological knowledge into how
*  we could implement whatever into deep networks. But there are some very global analogies,
*  as May said. Kenji Doya's work from the early 2000s has always been very illuminating.
*  In setting the stage to kind of confer a specific hat to each of the so-called
*  big five, or rather, would I say big four neuromodulators, like acetylcholine,
*  non-adrenaline dopamine, and serotonin. So again, indeed, Paul, as you mentioned before,
*  I'm currently studying the role of histamine, because I think it's very underappreciated,
*  and has only been restricted to its role in regulating sleep and wakefulness. But I believe
*  there's a lot more histamine could do. Therefore, I say the big five. But we know a lot more about
*  the role of the, or rather, the roles of the big four. And we've been pretty good at assigning
*  a specific hatch to what each of these big four neuromodulators are doing. For example, acetylcholine
*  in terms of gain normalization, or dopamine in terms of reward prediction error, and more recently,
*  serotonin, and things like that. But again, we really need ways to try and identify the nuances
*  of how these neuromodulators operate, and their interactions indeed, because they don't operate
*  in isolation. They always interact. But the interaction bit is a little masked, and we need
*  to understand how they interact, and hopefully come up with ways to encapsulate and formalize
*  the ways these neuromodulators interact into deep neural networks. So currently, we don't have that,
*  because we only looked at neuromodulation as one global, all-encompassing silver bullet. But this is
*  clearly not the case. So we need ways to try and model the spatiotemporal specificities of neuromodulatory
*  action into deep networks. Yeah. So on top of that, there are also a lot of technological
*  changes seen in both fields, and we have been observing different things thanks to them. And
*  it means when we're trying to model after certain aspect or certain neuromodulator, we always update
*  our model based on these new studies, right? For example, we have no adrenaline, which is traditionally
*  thought that only having a really homogeneous distribution as well as function. But now recently,
*  thanks to Optogenetics, we have observed really contact-dependent and also projection-dependent
*  functions of this neuromodulator. So we definitely wanted to update our model based on what the
*  experiments suggest, which means we will never go there, but we will never be there, but we will
*  get better and better. Yeah. Well, Mei, I wanted to say, because you mentioned networks of like 100
*  neurons. And one of the reasons why I wanted to have you guys on was because on the previous episode,
*  I had Eve Marder on, and she's famous for working on this approximately 30-neuron system in the
*  lobster stomatogastric nervous system and crab. And one of the things that she's famous for is being
*  struck and worried that because the resilience of these networks under different sets of
*  parameters essentially, right? So you could throw in terms of neuromodulators, and she doesn't
*  specifically only focus on neuromodulators, but if you had a high concentration of noradrenaline or
*  something, you might still get a nice rhythmic behavior from the system could produce nice
*  oscillations, right? So it's an oscillatory system. And then the crab moves south 100 yards or
*  something, and then there's like a lower concentration of potassium or something in the
*  seawater. And still you get these rhythmic concentrations, which goes to show how resilient
*  even small networks can be. But also the worrying part is how to understand what those networks are
*  doing because there are so many different parameters that work and it's hard to crash the system.
*  So then thinking about scaling up to such a massive neural network level, that actually seems
*  even more daunting. Because I know you're familiar with Eve Marder's work. How do you think about
*  that smaller scale and how much we still don't know about that versus scaling it up to something
*  much larger? So one statement that Eve made many years ago at a garden research conference
*  has always stuck with me and was also a factor to motivate me to look at neuromodulated function.
*  So Eve said that the connectome is absolutely necessary but completely insufficient to understand
*  the brain. So what she probably meant there was that, yes, I mean, there's the anatomical
*  wiring diagram, the blueprint that's kind of carved in stone or not entirely. But this provides a set
*  of instructions to the network. But what neuromodulators do is to act on top of these
*  set of instructions to then confer a lot more flexibility to expand the set of instructions into
*  a set of options. And indeed, in some sense, looking at the architecture of deep neural networks,
*  I mean, their layered configuration and stuff like that. Yes, so they are structured in a way
*  to work with a set of options. But how exactly the whole around these options is something
*  we don't know. And again, coming back to your question on complexity, sure, yes, we still don't
*  know how the small network of 30 neurons or rather the output of this small network of 30 neurons
*  is going to be the same regardless of a lot of stuff that's going on deep down under. So how
*  local components are being constantly reconfigured to end up with the same kind of result.
*  And indeed, so this is also something that I've looked into as part of my own stint
*  in the Blue Brain Project. And this combinatorial explosion is indeed a problem. But of course,
*  so what we still don't know is how to relate neuromodulatory function
*  and map it to a certain brain state. Because as I mentioned before, I think it's a synergistic role
*  play in that getting to a certain brain state and demands a certain configuration of neuromodulators
*  to act. And the brain can only get to a certain state if this combination of neuromodulators
*  are activated. So I think if we could try and understand what are the specific neuromodulators
*  that could actually function to get to a certain brain state and how do they act on certain cells
*  and synaptic connections, then I think this problem could be a little more tractable.
*  And of course, to add to this, the whole new field of transcriptomics is actually a very good ally
*  in trying to help us understand how this could work. Because it could be that there are certain
*  combinations of neuromodulatory receptors that are expressed in some cell types. And looking at what
*  are these receptor combinations and linking these receptor combinations to different neuromodulators,
*  I think we could then try and predict how combinations of neuromodulators could actually
*  act on the expression of certain receptors to help us or to help the brain get to a certain
*  network state. And therefore, we wouldn't have to study all possible neuromodulators, but just
*  try and understand the expression of certain receptors, how they correlate with the expression
*  of receptor types of other neuromodulators. And if these are all expressed in high levels, then
*  it could be that these neuromodulators that are acting on these different receptors
*  are having a similar function. So I think these are some of the ways that we could try
*  and harness to really break down this problem into something that's a bit more tractable.
*  Yeah, so apart from the biological constraints, when we are working with DNNs, and I think it's
*  quite important to understand what each layer, very, very each layer is playing a role. And I
*  think the one way is also to kind of work with the deep learning community to have better
*  visualization tools and something from the inside. I think this is something the community is
*  currently working on. So explainable AI, and try to kind of break down the black bars. And for
*  example, for example, so now I'm working with biologically plausible fairing of deep neural
*  networks. And so from this fairing, we can kind of have a more direct way to observe what's going
*  on in between, you know, the neural connectivity and within each neuron. So we simply kind of
*  visualize all the fairing pattern of cells in a fully connected layer. And we try to see if
*  when we try to play with the adaptive factor or the monetary factor within, you know, these layers,
*  how it's going to affect the fairing pattern of the cells. And we have found something quite
*  interesting that, you know, the fairing is actually factor dependent. So if you play with
*  the hyperparameter a bit, we can kind of change the fairing of the cells and also some distributions
*  of cells judging by their fairing pattern. So I think this is a really interesting observation.
*  And we should really push that we have better visualization tools or computational tools to
*  kind of understand what's going on in between each layer and have this as a dynamics. And one more
*  thing is that we can also use, you know, a shallower network at the beginning. And also we can try to
*  play with different architectures and how this interacts with the new monetary systems. And I
*  think one interesting study done by the Colman and colleague is that the robustness of a neural
*  network from having a modulation or not. So actually they found that as a network is more
*  robust against different architectures and having a modulation. I think this is something quite
*  interesting. I mean, they may observe the robustness due to different factors. For example,
*  like the internal working might be different, but they output the same result. But this is something
*  I think it's a function, kind of a direction we can step into is how your modulation is affecting
*  the general output and also inner working, you know, in addition to the output of the neural
*  network as measured by accuracy or something in between, you know, like when we are trying to
*  prove this question and also in our paper proposed to add, you know, in addition to the traditional
*  global loss or something you want to have, especially, you know, feedback based learning
*  or continuous learning, you want to have something in between, you know, we want to have a more direct
*  feedback from a task or like a smaller task related, you know, learning or responses. And
*  this way we can kind of capture it from a different spatial temporal scale. So this is more related to
*  the temporal scale. Yeah, we can have a more like a frequent sampling of the learning trajectory.
*  Going back to something that Sri said about, well, so, you know, even Marder and she actually used
*  the same quote that structure is necessary, but not sufficient to explain function, right? I don't
*  remember if we actually spoke about this on the episode with her, but, you know, one of the things
*  that they found in simulating five million, I'm going to make this up five million different
*  simulations with different sets of parameters, right? That the actual space out of five million
*  that were viable was pretty low, but it as a percentage, but it was still like in the
*  hundred thousands, right? Of parameter spaces that would work. So yeah, I mean, it's constraining, but
*  still quite daunting. So guys, I'm aware that our time is pretty close here. I have a guest
*  question from Mack Shine. Okay. And so he so in the question Sri, he's talking to you, but, you know,
*  the question is for both of you. So I'm going to play it through the phone here. Okay. Hi Sri,
*  this is Mack. So we're both really interested in how different arms of the ascending arousal system
*  release neuromodulatory chemicals that change the firing rate and plasticity of areas of the brain,
*  like the cerebral cortex and the thalamus. But I would say that we take quite different approaches.
*  I've been interested in trying to understand the basic principles underlying the interactions
*  between the neuromodulatory system and the circuitry of the brain, whereas you've really
*  dove down into the details and embrace the complexity of an area like the cerebral cortex
*  and all of the different types of cells that exist there. And I wonder if you have any ideas
*  about how to join the dots here, how to extract basic principles from the brain,
*  but also really understand the exquisite detail that's present.
*  Okay. So that, you know, we've already touched on this topic throughout the conversation, but
*  there's the question. Right. So I think one way to do this is really to harness this whole approach
*  of optogenetic recordings in the intact brain. Right. So now, I mean, we really have these very
*  specific transgenic mice lines for these big five neuromodulators. There's also a technique called
*  compound breeding. I'm just getting into the nitty gritties of these experimental details.
*  But with these compound breeding techniques, I mean, I'm sure it's very complicated,
*  but in principle, assuming that it's seamlessly possible. So one could, in fact, try and
*  genetically, of course, label a certain neuromodulatory projection, like let's say
*  histamine, right? And then tag these histamine energy projections to specific neuron types,
*  let's say in the, in the cerebral cortex. So that way it would enable trying to quantify,
*  for example, what's going on in a population of layer five pyramidal cells in the neocortex
*  upon activating histamine. Right. So that way, you're somehow trying to come midway in terms of
*  a top-down approach in that you're trying to understand what's happening to a population
*  of neurons under a certain behavioral paradigm and how a certain neuromodulator is actually
*  regulating this behavioral paradigm. Right. So that way we're actually bringing these two
*  approaches, like what I'm a fan of partly, a bottom-up approach and what I know
*  about Matt's own work in that he's trying to build mean field models, population level models of
*  network activity. So I think that way we would really try and merge these two complementary
*  perspectives to try and understand what a certain neuromodulator is doing to a specific population
*  of neurons under a behavioral task. Yeah. I mean, regarding the biological details,
*  and there are many studies that are using novel approaches like optogenetics, I think one of the
*  principle, also really important finding was reported in science, comes to dopaminergic
*  modulation on cell morphology and really goes down to the final level of dendric spines.
*  And so this way, so they kind of, there's a group of Japanese researchers who study the strido of
*  medium spiny neurons and use, going to really refined time scales as well. So they found that
*  the dopaminergic regulation can kind of enlarge the spine, the dendric spine of this certain
*  neurons within a short time within 0.3 to two seconds. I think this is one prime example of
*  using novel technologies to really go into the biological detail on the smallest possible spatial
*  scale you can have. And also like a lot of projection specific studies on the goals of,
*  for example, cholinergic cells are relying on the same techniques or sometimes two photon
*  engaging as well. So two photon microscopy, a combination of this with the optogenetics,
*  which is also done by this group of Japanese researchers. We've also done like in other studies
*  are studying the projection specific functions of, for example, neurogenergic systems, such as
*  for example, Wematsu did. So they published their studies on nature communications. I think it's
*  Dr. Johnson's lab at Regan. And they were trying to unlock the function of neurogenergic
*  system in different projections for different functions. So like it's more like sensor perception
*  as well as for your conditioning. So in this way, we can really kind of more comprehensively
*  understand the diverging function of the same system within the same area across different areas
*  depending on their projections and also in kind of an intrinsic between, you know, like the
*  interactions across cells within the same microcircuits, for example, within the basal
*  ganglia, the D1, D2 cells as well as cholinergic cells that are regulating their behavior. So I
*  think it's definitely contributing to a more comprehensive understanding of what convergence,
*  divergence ongoing at the local more global scale. So we've been talking about neuromodulators
*  largely here, but may you interest you mentioned your interest in and you mentioned Blake Richard's
*  work incorporating like multi compartment models of units instead of just point units. And you guys
*  talk about that in the paper, but you don't go into as much detail as you do with the neuromodulator
*  story. But and what I was going to ask is how challenging it will be to. So my first thought
*  was that it's a lot more straightforward to incorporate dendrites, let's say, because if you
*  model them all the same anyway, then it's almost like just modeling another computation, right,
*  like another activation function almost in just at higher scale. But then you mentioned that,
*  you know, if you're going to model like the size of the dendrites changing and there,
*  I guess that's in some sense like modeling a weight change to a dendrite differently,
*  right over the course of all the dendrites. But then neuromodulation with all the interactions
*  seems to me at first pass to be a much more complicated thing to model to figure out.
*  I'm just yeah, OK, so I'm wondering if you guys agree with that,
*  you know, building in the dendrites, for example, or multi compartment models,
*  if you feel like that's a much more straightforward process than modeling in neuromodulation.
*  Well, sure, that's one way to do it. But there have been efforts to try
*  and systematically collapse the biological detail into simpler models.
*  But maybe two ways of retaining this biological complexity through some kind of activation
*  functions, right, that could represent nonlinearities in dendrites or could also
*  represent synaptic conductances on dendrites, right. And then to account for the fact that these
*  conductances, when they're activated at the synaptic location on dendrites,
*  but by the time they get to the soma are severely attenuated, for example,
*  in the perimodular cells and things like that. Right. So there are ways to do this. So I think,
*  I mean, a more efficient and a smart way to try and see how to incorporate
*  a neuromodulation into such a framework would be to write this bandwagon and see.
*  So how can we capitalize from this whole infrastructure
*  that's being developed to try and collapse biological detail into something that's
*  that's more simple, that's more tractable, and then use this framework to try and also incorporate
*  like neuromodulatory receptors? I mean, ultimately, what this means is this could just be another set
*  of activation functions, because the way these neuromodulatory receptors also work is pretty
*  nonlinear. So this could be like another set of complementary parallel activation functions
*  that could go into such a modeling framework. So this is one way to do it. And there are groups,
*  for example, like Idan Segev's group or Ivan Solitesh group that are actually trying to
*  look at ways to simplify all the complexity out there, and yet somehow retaining this flavor of
*  complexity. So what this enables us to do is to model and simulate networks that are not as
*  expensive in terms of computational infrastructure. And yet, the beauty here is that they're
*  retaining a lot of the biological complexity. Yeah, so according to me, what's interesting is also,
*  in addition to the about mentioned point Sri had, I think what's interesting is that there are already
*  like this established approaches of computer neuroscience allowing us to do that. For example,
*  they have, so how they are actually modeling neurotransmitters and neuromodulatory receptors
*  actually through the ion channel kinetics file, you know, mostly like cod neuronal,
*  no, like neurosimulator mod files. So they're kind of really like investigating the biological
*  literature and how the neuromodulatory affecting the local conductances and also acceptability of
*  a cell. And they kind of bridge this into mechanisms within the mod file. So I think we
*  can do something similar. And we, as Sri said, we can pretty much like model a cell with a changing
*  acceptability using, for example, also like alternating activation functions, right? Because
*  what takes to trigger a cell to spike at a certain time point can differ from another time point,
*  depending on the events and scenarios. So we can kind of model this kind of acceptability
*  change or production change as something that's more commonly used in deep neural
*  network sets, activation functions or hyperparameter change. So there are always like parallelism in
*  between the two, but we just wanted to open this discussion that there are really like all these
*  modulatory effects at different levels, including the fine dendrites and the cell can really behave
*  differently and they're different contacts. And I think that's also like one point of the paper.
*  And so we really want to bring that into a scope. A lot of what we know from neuromodulators in
*  particular, bringing it back to neuromodulators is through mammals, right? Mice systems. Do you
*  think that there is any reason to look across different file? Like, I don't know anything about
*  neuromodulation in the octopus or the shrimp or something, or it doesn't have to be a sea animal
*  or birds, right? I mean, do you think there's any use in studying the different capabilities
*  of different species and their set of neuromodulators and that landscape? Or do we need
*  to focus on things that we're so interested in ourselves, our mammalian selves, that human is
*  the goal. But there's a possibility, this wouldn't be inventing new ones, but incorporating
*  across species principles, right? Actually, Sri, please go ahead. Yeah, sure. So I think
*  a lot of the neural mechanisms that underlie the evolution of behavior is pretty much remarkably
*  conserved across species. Yeah, that's what I thought. But there must be differences. There
*  must be appreciable differences. Indeed. Indeed. So I mean, as species as you want, right? So
*  of course, the size of brains have of course, remarkably changed. There's also the aspect of
*  more neurons, perhaps more intricate genetic architectures that could then invariably
*  support more receptor types and things like that. So I think overall, the primordial function
*  of certain neuromodulators is pretty much conserved across species. But indeed,
*  with evolution, there are also certain nuances. For example, I don't know if the octopus brain
*  would have the same kind of receptor diversity for histamine as the mammalian brain.
*  So I don't think octopi don't sleep, do they? Well, okay. They probably don't. But I don't know.
*  I mean, they probably have some kind of a quiescent state. I don't know.
*  Yeah. Anyway, because since you mentioned histamine, so I may have triggered that.
*  Oh, okay. Wait. So again, we've traditionally studied the role of histamine in the mammalian
*  brain in relation to sleep and wakefulness. But I think a histamine in itself is a distinct
*  neuromodulatory system that's probably doing all kinds of things. I mean, there's a lot more
*  evidence now that it's involved in regulating gamma oscillations and things like that.
*  So all I'm trying to say is that, I mean, it could be that given the fact that the architecture of
*  neurons is a lot more complicated across the evolutionary tree, that there simply is room to
*  support more receptor types that could do or that could bring about assorted functions
*  upon the action of the same neuromodulator. But overall, I think this basic function is
*  probably conserved across species. But the nuances is what sets the function of neuromodulators apart
*  from invertebrates to vertebrates. And this is something that we simply don't know much about.
*  I mean, I think an interesting example is that again, we have different purposes in different
*  disciplines. For example, if we discuss the pneumatic design of robotics, it has a different
*  meaning than what we have in neuroscience, right? So they pretty much use exoskeleton or other kind
*  of simple architectures, mechanical ones to simulate what the animals are, how the animals
*  are ambulating or stuff. And I think for different subjects, for different areas, we have different
*  goals. For example, the reinforcement learning in actual scenarios, actually like the danger
*  avoidance or avoidance behavior is actually one important point of discussion, right? So we avoid
*  the danger, we kind of preserve ourselves within the wild environment. So this is their focus of
*  study. So I think it's kind of interesting to study different organisms depending on the question
*  you want to answer. For example, the lampreys, like there are a lot of studies by Stein-Grillner
*  studying the lampreys and the central pattern generator and also Eve Mutter, as you mentioned,
*  her really famous study, she used the crustacean. You know, these are simpler networks and are easier
*  to test. And also the crustaceans have different kind of neuromodulators, for example,
*  preptolen or something else, not the same as a big four as what we have in the brain. So there are a
*  lot of primitive functions are largely preserved, for example, phytoplankton flight and also, you
*  know, like as a preserving body heat and certain body temperature reflexes, these are already
*  preserved and there are like a higher diversity when it comes to higher domains, cognitive domains
*  such as social functions, exactly functions, and there is a big divergence between like individuals
*  and we can even have subtypes of cognition in people. In our paper, like there's a figure
*  representing different spatial, temporal, specificities of neuromodulatory functions
*  and processes and on the higher, you know, like temporal and then the spatial scale,
*  we have a longer extending functions, more like continuous feedback and learning and processing
*  bees. And I think this is something quite specific to mostly mammals and then human that possess
*  social function and access to really like reacting a kind of a really complex environment. I think
*  these kind of behavior demands are really different from other species and I think that's
*  also one interesting point and having all the knowledge of all those different species are
*  definitely interesting for us scientists to build different model mechanisms to address certain
*  questions because, you know, like sometimes the ambulation on a kind of, you know, like really
*  bumpy terrain by people is definitely something that's less well studied because we are not
*  advancing on that. We are not surpassing certain species on that because we don't navigate well
*  on this kind of a terrain, right? So really, it should be studied more if not just for comedy.
*  Yeah, exactly. So it really depends on the question we wanted to answer and this is also,
*  I think Shri and I earlier during the year and last year, we wanted to think of future study,
*  you know, where we focus on the evolutionary perspectives of neuromodulations, how it changes
*  from a perspective that is more primitive and, you know, like just basic life function preserving
*  to something that's more elegant and involving higher cognitive domains. We wanted to understand
*  how this is related to the evolution of the brain and increasing folding of our neocortex.
*  So maybe we'll have this study in the future. Yeah. Tiny questions then. Shri, go ahead. Sorry.
*  So I think Corey Bargman has actually been doing a lot of these seminal studies,
*  really only looking at the role of specific neuromodulators in an extremely primitive
*  organism like the C. elegans, right? 300 or so neurons. And yet remarkably, this primitive
*  organism displays a very rich repertoire of behaviors possibly due to neuromodulating function.
*  For example, right from olfaction to something else. And it seems that these neuromodulatory
*  systems are conserved across phylae, like C. elegans all the way to the mammalian brain where
*  it seems that these similar neuromodulators are involved in olfaction, for example. So that's
*  really remarkable. But the question obviously is how do these neuromodulatory systems also scale
*  as brains expand with the number of neurons and also their architectures and different brain
*  regions and their interactions? And how is this primordial function actually conserved despite
*  this whole combinatorial explosion? So I think this is really fascinating. This is really,
*  really remarkable. And as May said, we're trying to really skim the surface of how
*  this could be possible to provide some perspectives.
*  **Matt Stauffer** That is even a larger question, I suppose. But if we're at
*  three on a scale of zero to 100 in terms of what we understand about neuromodulators and three-ish
*  on a scale of zero to 100 and incorporating that and making it useful in deep learning networks,
*  there's certainly a lot more work to do. So I look forward to a lot more of that work from
*  you guys and wish you luck. Appreciate the conversation today.
*  **Sara Kauravaraman** Thank you for the questions. Yeah, it also leads to more thinking. I think
*  we'll have discussions internally and also with the wider public regarding our work and the things
*  we can do in the future. **Sushant Duttraib** Yeah, thanks a lot, Paul, for the chance to chat with
*  you and for the great podcast. Well, hopefully a lot more people would realize the urgency of the
*  problem and try and join hands with us to crack neuromodulation a lot more efficiently in the
*  coming years or maybe in the coming months. We don't know. We'll see. The more hands we have
*  on board, the better, of course. **Matt Stauffer**
*  There you go. You heard it, listeners. It's a call to arms to join the cause. So,
*  all right. Thanks, guys. Appreciate it. **Sara Kauravaraman** Thank you.
*  **Sushant Duttraib** Sure.
*  **Matt Stauffer**
*  The stare of a boundless blank page led me into the snow
*  that covers up the paths that take me where I go
*  **Sushant Duttraib**

---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 3992s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 3571
Video Rating: None
---

# BI 093 Dileep George: Inference in Brain Microcircuits
**Brain Inspired:** [December 29, 2020](https://www.youtube.com/watch?v=-_13jtIPjWI)
*  It's like solving a jigsaw puzzle. Biology gives you some set of hints and your model
*  gives you a full set of computations and then it's a question of how do you map these computations.
*  We had to put in there because that's the only way to make the model work and then when
*  we worked back from that to see where it would fit, there was no place to fit it other than
*  in the thalamus.
*  This is Brain Inspired.
*  Hey it's Paul. Once again today I have Dalip George on because last time he was on we ran
*  out of time to talk about what he's back today to talk about and that is his recent work that
*  maps his model for visual inference onto the circuitry of the cortical column in combination
*  with the thalamus to account for the function of the loops of connections between the cortex
*  and thalamus. The model I just mentioned is what we discussed in previous episodes with Dalip
*  which he calls a recursive cortical network which is a generative probabilistic graph model
*  for inferring the best explanation for visual evidence presented to the model. In this case
*  the Arsian model, the recursive cortical network model, was adapted to account for the corticothalamic
*  circuitry and the way it turned out, Dalip thinks of cortical columns as little belief machines
*  about some feature or concept about the world that you're perceiving and the belief is informed
*  by sensory input, by top-down attention, and the context of everything else that's going on at the
*  time or in the same scene. All that information goes into a vote on whether to believe the feature
*  or concept that the cortical column stands for should be present in your perception. So I'm
*  either on or I'm off. You do see an edge there or you don't, for instance. This model gives the
*  thalamus a crucial role for explaining away evidence for other interpretations as information
*  gets processed up the hierarchy of vision. So we discussed the model and its functioning in more
*  detail and we compared a little bit with Randy O'Reilly's ideas about the thalamus providing a
*  predictive learning mechanism from a few episodes ago when Randy was on. Show notes are at brandinspired.co
*  slash podcast slash 93. If you value the podcast and can afford a couple bucks a month, consider
*  supporting it on Patreon. Often I include extra bits of these regular episode conversations and
*  every once in a while I'll post a bonus episode. And I'm almost to the point now where I can start
*  using some of the funds from the Patreon support to pay for a little help with things like editing
*  and transcripts, which would help immensely. Anyway, Dalip won't be back on for a while,
*  but he's always fun to talk with, so I hope you enjoy the conversation.
*  Thanks for coming on the show again and we'll talk soon again, so I appreciate it.
*  Thanks Paul. Thanks a lot for having me and I hope I will come back again before two years.
*  Alright, so Dalip, here we are. Welcome back. Yes, great to be back. It hasn't been two years,
*  it has been just a few weeks, I think. Only a few weeks, but I know of at least two things that have
*  happened during that time. One, how was your RV trip? How was your first ever RV trip? Oh,
*  that was so much fun. The kids loved it and it was just one night of RV camping, but the whole
*  experience was fun. For me, it was first time driving a big truck, basically. And then it was
*  just good to get out for a few days. Oh yeah, especially these days. Can you imagine, so you
*  did it for one night, I did it for a year and a half, although we towed a fifth wheel, which is
*  like the big ones that you tow in a monster truck and stuff. Do you think you could handle a year
*  and a half with the kids and everyone in there? Wow, so you did a year and a half in an RV with
*  kids? Yeah, and I'm basically bald now. I would love to do that next week. Yeah, well, maybe
*  we should talk before you just sell all your stuff and move into an RV like we did. Anyway,
*  I'm glad to hear that you got out and that it was fun. The other thing that happened is that you
*  published this nice review in Frontiers that details really your overall approach, but also
*  is based on the recursive cortical networks that we've talked about a few times here already on
*  the podcast. And so obviously I'll link to that review. It's a great review, by the way,
*  and I have a few questions here related to that before we really get started.
*  So one of the things that you lay out, what you mentioned and described in the last episode,
*  this triangle strategy that you employ for building AI. Basically, you use in parallel
*  cognitive and neuroscience observations, and you match those in parallel with computational
*  algorithms and principles, and you match all of that with the third node of the triangle,
*  which are properties of the real world. And that's a little bit reminiscent of Mars levels of
*  analysis. And I had a, the reason I'm bringing this up is because I had a listener question
*  about you trying to understand how the brain works. The question is, how do you define
*  the levels of abstraction of the description of the brain, and what level are you working at
*  in particular? So I just will throw it to you. Yeah. The tricky part here is that you cannot
*  define a level of physical abstraction in the brain. You cannot think of you're operating at
*  neuron level, column level, or synapse level, or you cannot make any physical cutoff like that
*  because if you make a physical cutoff like that, and if your overall system needs a mechanism that
*  is below that level, then you will be missing that out. And that's why we don't describe it in
*  terms of a physical abstraction level, like a cortical column or anything like that in the brain.
*  And it's more you look as deep as you need to, but you ignore irrelevant things at any level,
*  any physical level of abstraction. So if something at the cortical column level is
*  irrelevant for information processing, you ignore that. So this triangulation strategy is more for
*  figuring out what is important for information processing at any physical level of implementation
*  versus what is not relevant for information processing.
*  Great. So hopefully that satisfies Jeff. Okay. Last question about this review. And again,
*  I'll point people to it. So in Vicarious, the goal is to build AGI. And one of the things that you
*  write about is why are we calling it AGI? Why not A-H-I, as in artificial human intelligence?
*  So you make that distinction between artificial human intelligence and artificial general
*  intelligence. And then you add in artificial universal intelligence. So how do you think
*  about these things? What is all that? What do you mean? Yeah. So we need a term to refer to
*  building of intelligence models after the human brain. And people have been calling it artificial
*  general intelligence for a while, but there is some confusion. And this confusion can be because of
*  books like super intelligence being written, where what is imagined is an arbitrarily powerful
*  entity, which would just instantaneously learn everything and take over the world and convert
*  everything to paper clips, et cetera, et cetera. But such things do not exist. There are fundamental
*  limits on what even a general intelligence will be able to do, how quickly it will be able to learn
*  new things, how quickly it will be able to disentangle the causal mechanisms in the world
*  so that it can make decisions and drive actions. So those fundamental limits will always put a,
*  there is a constraint on how quickly something can learn and act in the world.
*  So those are not constrained in this mythical super intelligence setting. So that's why I call it
*  some arbitrary artificial universal intelligence, which is like perpetual machines. You can imagine
*  something like that existing, but it violates the laws of physics and it cannot exist. So that's
*  the thing I put in artificial universal intelligence, something that exists only in our imagination
*  cannot be really built. So then some people, since people were mischaracterizing
*  general AGI as this AUI, some people started basically saying that, oh, it should be just called
*  human intelligence, not AGI. But the problem that is that, that also doesn't solve the problem because
*  are you going to model exactly like human intelligence? Are you going to put in
*  the working memory limitations that we have just because we have some hardware limitations?
*  So are you going to impose all the arbitrary constraints that might be there on our own
*  intelligence? Are you not going to wire a Google search directly into the prefrontal cortex?
*  If you could. So it's basically, whenever we are going to build something based on human intelligence,
*  but on a different substrate, it will be more general than human intelligence,
*  just because of the way we are building it. So you can think of, oh, I want to model human
*  intelligence exactly and try to build it, but you will end up building something that is more
*  general. So that's why I like the term artificial general intelligence. It is not some arbitrarily
*  universal intelligence, and it is not exactly time to replicate human intelligence with all
*  its limitations. So that's why I like the term AGI as something, general intelligence model after
*  the human brain. I like that too. And it's not subject to the same constraints physically,
*  or just capacity wise as well. So you kind of have a hierarchy. There's artificial human intelligence,
*  and then above that is artificial general intelligence, and the limiting
*  fictional idea, theoretical, is artificial universal intelligence. So then below the
*  human intelligence, where is that? Is that me? So is there a term for that? Computers or something?
*  I would call them specialized intelligences.
*  I enjoyed the review paper because it lays out your approach and gives examples that we've talked
*  about already on the podcast and that are in all these papers in a very easily digestible manner.
*  Glad you liked it.
*  I have just a couple things on Vicarious, and then we're going to get into the meat of this thing.
*  Doing things in general, and creating startups for instance. So it seems like 99% of startup
*  ideas begin with the wrong idea. And you were talking about how important it is to listen to
*  customers, and that's how it kind of shapes what you're building, not only the specifications
*  and the technical information, but the kind of things that you're making.
*  I'm wondering, does it even matter, how much does it matter what idea you start with,
*  given that it's going to change probably dramatically?
*  Well, it matters in terms of what is the skill set of people you are bringing in,
*  and what are your key people in the company. As long as whatever you are changing to fits within
*  the skill set of what those people can build, then I think it will be reasonably fine. It will be
*  very hard to pivot to something that is totally outside the scope of them. That will be almost
*  like starting a new company. Do you think that's why a lot of startups fail? I mean,
*  most startups fail for various reasons, but do you think that might be an underlying reason that when
*  people have to quote unquote pivot, then their team or their technical skills aren't up to par
*  for whatever the end goal is at that point? I mean, there are multiple, multiple reasons,
*  right? And it depends on the different stages of the company. So at early stage, what I've seen are
*  things falling apart, sometimes just based on disagreements between the founders, they just
*  try to work for a few months together, just didn't pan out, they want to go in different directions.
*  So at the very early stage, when it is two or three people in a garage kind of setting,
*  it can fall apart because, oh, just didn't gel to working together. So that's one reason. And often
*  it is just finding that core team that will stick it through, which is the hard part, getting a co
*  founder and or a key employee, employee number one, which becomes super important in the company,
*  that that core team clicking together can be a challenge. And so that's a lot of ideas fall
*  apart right at that stage. And then, and then it is, you know, the different gates that you have
*  to pass through, you know, seed, CDC, etc. So, and things can fall apart at the seed stage,
*  where, oh, you just the idea does not get any traction at all, where you talk to multiple people
*  and just cannot raise any, any money, and you might bootstrap it for some time. But if it's
*  not getting customer traction, or if it is an idea that actually requires capital to get that, you
*  know, customer traction, then it will fall apart at that at that stage. Then, later on, what can
*  happen is that, you know, companies can scale too quickly. Because you always want to scale because
*  there is a perceived customer demand. But if you if you scale too quickly, and then the customer
*  demand doesn't materialize in time, that's, you know, something can go wrong in later in the
*  lifecycle. Then scaling too slowly sometimes can also be bad. That sounds so fun, man.
*  Because then somebody else scales faster than you. So, yeah, so there are many, many things that can
*  go wrong. We know the costler has a nice analogy for what startup life is like, right? It's
*  basically, he's saying, it's like jumping off an airplane, and building a parachute on the way down.
*  And then the goal is to basically just not hit the ground.
*  Note to self, the leap does not suggest starting a startup.
*  No, it's fun. It's still like skydiving fun.
*  Yeah, that's right. There you go. There's the plus side of it. Yeah. Okay. Well, that's great. So
*  you've made it you've built your own parachute. You know, it seems like you're or hang glider,
*  even maybe I don't know what you you've built, but you've done a really nice job so far. So anyway,
*  continued success, of course, with vicarious. Thank you. But what we're really here to talk
*  about today is the second of two recent papers, the first of which we talked about last time.
*  So the second one is all about, well, I'll just read the title, a detailed mathematical theory of
*  thalamic and cortical microcircuits based on inference in a generative vision model.
*  And I'll just kind of introduce it here. And then you can correct me and we can and then we
*  can get into it. So the neocortex seems important for our general intelligence. However narrow that
*  generality may be, as we were, you know, sort of just discussing, you have argued that the cortex
*  is, you know, in on the one hand, you know, the important thing to understand. But on the other
*  hand, that, you know, it's it's the easier bit of brain to understand, because the rest of the brain
*  is so complex and specialized honed through eons of evolution. Okay, so cortex, just to bring everyone
*  up to speed is this big sheet made up of a repeated architectural motif, what's called the
*  cortical column, or microcircuit, which is repeated throughout the cortex fairly uniformly,
*  but with variation. But it, you know, it's the basic organization is similar across cortex. And
*  you've argued that if we knew what it was doing, as many have, that we could apply that and then
*  take us a big step forward, not only in understanding our own human intelligence, but in building
*  artificial intelligence. And there are many theories of which you have, you know, worked on
*  already. But they're based on sort of two, I would say main approaches. One approach is to think of
*  cortex as sort of a feed forward, bottom up series of hierarchical processing. So going from like
*  these simple to more complex and abstract representations. So like in vision, that would
*  be going from like lines and edges building up to all the way up to an image that you can identify,
*  an object like the face of Abraham Lincoln, someone famous, right? The other approach,
*  the one to which you subscribe, is to think of cortex more as a top down inference engine,
*  which creates generative models of possible worlds to then best explain the data that is
*  coming in to our senses. Am I on point so far here? Yes, you are exactly on point. Yes. Okay.
*  Do I have to say anything at all? No, no, just, just by the way,
*  Dileep's on a treadmill. This is great. This is the first time someone's exercised during the
*  podcast. I love it. So it's great to be standing and walking while talking. That's fun. Yeah. Oh,
*  yeah. I should get a treadmill because I do, I use a standing desk. Okay. Anyway. All right. So,
*  so I'm going to continue here. So most focus has been on the canonical cortical microcircuit asking,
*  you know, what does that column do? What does that cortical microcircuit do? But of course,
*  cortex doesn't act alone in the brain. It's highly interconnected with lots of other brain areas.
*  In these complicated loops between cortex and the other brain areas, one of which is the thalamus.
*  And the role or roles of the thalamus has been debated for many a year now. It was originally
*  thought, you know, just to be a relay from our sense organs to the rest of the cortex. And it
*  does do that. But more recently, it's been thought that it's played a role in attention and the
*  regulation of information flow between cortical areas and from our senses to those cortical areas.
*  So the circuitry and the loops between the thalamus and the cortex have led, you know,
*  some people to kind of rethink the canonical microcircuit computation, right? What is the
*  canonical microcircuit actually computing? So to move beyond just cortex and then actually
*  involve the thalamus. So I had Randy O'Reilly on recently, and he has this deep predictive learning
*  model where there's a feedforward projection to the thalamus from cortex and a feedback projection
*  to thalamus from cortex. And the idea, and this happens in the pulvinar, at least in the visual
*  system, these feedforward and feedback connections join together in the pulvinar and act like a,
*  you know, predictive learning mechanism in the style of this top-down predictive coding
*  inference approach. And so, and I only say that because, I mean, you know, this conversation
*  that we're having is basically the closest thing that we've talked about on the podcast. To that is
*  Randy's predictive learning mechanism here. Okay. So that brings us up to speed now, sort of up to
*  speed. So you had these recursive cortical networks that you've been working with for years.
*  Yeah. And you realized that they could be implemented with networks of neurons, and you
*  realized that you could map the computational properties and the flow of these RCNs onto the
*  cortical column. And thus, the bio RCN was born. Yes. And all right. So I'm going to hand it over
*  to you. So we've done this already multiple times, but just really broad overview. Let's just recap
*  what recursive cortical networks are and what you've used them for in the past.
*  Yeah. So recursive cortical networks are a hierarchical generative model for vision.
*  It builds a hierarchy from parts for line segments at the bottom, going all the way to
*  object level models at the top. And these are all encoded as a probabilistic graphical model.
*  And when a new piece of evidence comes in, like a scene of characters or scene of objects, this
*  model can pass that scene as best explanation under the model. And we used it for cracking
*  captures, defeating their fundamental defense. And also we use it regularly in our robotics tasks
*  for cluttered bin picking, detecting boxes, all those things. So it's a vision model that can be
*  used for object recognition, for foreground background segmentation, for estimating pulls,
*  for generating from the model, for occlusion reasoning. So it's a uniform generative model
*  on which the different tasks are just different queries on the model rather than having to train
*  specifically for the task. Yeah. Having to retrain the model like a deep learning network
*  that you'd need to retrain for every task. Right. I mean, there might be some generality between tasks,
*  but in general, you'd have to retrain it. Yeah. All right. Good. So like I said, you've taken those
*  RCNs and applied them to a cortical column and developed the bio RCN. And one of the nice things
*  about applying this to a cortical column is that because you already had the theory basically of
*  the RCN, it makes very specific biological predictions of what kind of connections there
*  need to be and what kind of cells need to be involved and precise inhibitory and excitatory
*  interactions. And the way that this works, so well, maybe you can elaborate on that just a little bit.
*  Okay. So one thing is that when we built RCN originally, we were looking at the brain for
*  insights. We were looking at visual cortex for insights to say what kind of structural constraints
*  need to exist in the model. And so it is not surprising that we will be able to map it back
*  because we started with insights from the brain. But the insights from neuroscience are clues.
*  For example, the idea that surfaces and edges are represented separately, but in an interacting way,
*  that is an idea that came from neuroscience and we triangulated it to some algorithmic principles
*  and properties of the world. But then how exactly it gets implemented in the graphical model,
*  that is something we develop in the context of everything else that we are building. So
*  the mathematical model that we are building is filling in a lot of the details based on
*  hints from neuroscience. And the good thing about the final model that it's built is it is
*  functionally complete. Even though it is partial functionality, it is not doing everything that
*  visual cortex is doing and not to the level of performance that the visual cortex is doing.
*  But at least it is complete. It is doing the whole thing of parsing a scene and recognizing
*  characters, all those things. So it is a complete functional model. That means it fills in a lot of
*  the details that are not available when you look initially at biology. So now we can go and map
*  back these computations to the cortical lamina and columns. And again, there information from anatomy
*  and physiology, all the experimental data act as constraints in that mapping. So you know that,
*  for example, feedforward input from the thalamus mostly lands on layer four in the cortical lamina.
*  And if that falls on layer four, then you know that if you place that computation there,
*  you know that the next set of computations, which are dependent on the projections from layer four
*  to layer two, three, there is only one place to put that. So it's like solving a jigsaw puzzle.
*  Biology gives you some set of hints and your model gives you a full set of computations.
*  And then it's a question of how do you map these computations? And you anchor them based on
*  known data from biology. Those becomes your anchoring points, the corner pieces of the puzzle.
*  And then the rest of it gets filled in based on those constraints imposed by these anchoring
*  pieces of data from biology. Good. One of the things that you do is,
*  so in the RCN, it's a probabilistic graph model. Each node in the RCN, when you break it into
*  biology, is sort of broken into groups of neurons. So each node kind of represents
*  groups of neurons that then you break down mathematically and computationally how they
*  interact and compute and then send projections to other nodes that are made of other groups of
*  neurons that do different computations. Correct.
*  So we'll bring Thalamus in here in just a bit, but let's start with the cortical micro column.
*  You fashioned the cortical micro column as a binary random variable.
*  Yeah. So what does that mean?
*  Yeah. So one pleasing thing out of this mapping is that it gives us a tool to think about
*  cortical micro column. So you can think of a cortical micro column as representing a feature
*  or a concept. So it can be a cortical micro column represents an edge or a character A
*  at a higher level. And then, so what do those different lamina in the cortical column do? They
*  are all talking about the same feature. They are all talking about this one thing, whether it's edge
*  or a character, but they are talking about different aspects of that thing. So it could be,
*  how does this edge participate in lateral connections with other edges in the same level?
*  How does this edge decompose itself into smaller edges? Or how does this edge compose itself in a
*  hierarchy with a corner in the next level in the cortical? And these different aspects,
*  the participation of that feature in different aspects, whether it is laterally, hierarchically,
*  sequentially, et cetera, all these different aspects get represented in different cortical
*  lamina. And then finally, there is this need for computing the final belief that each cortical
*  column needs to say, am I on or off as part of the overall coherent thing that the visual cortex is
*  trying to explain? When am I part of the best explanation for the scene or not? And that is the
*  belief, whether that particular column is finally on or off. And that requires integrating information
*  from bottom-up evidence, lateral evidence, top-down evidence, sequential evidence, all of them. And
*  all of them are finally combined into a signal saying, am I on or off? And so that is represented
*  in another lamina. So this mapping uses this conceptual tool to think about what a cortical
*  column is doing. Just to give a really coarse sort of cartoon of this, it could be that in one layer,
*  let's say, layer projection coming into layer four saying, I'm an edge. I have edge properties. And
*  then the projection's up to layer two, three is like, you're an edge, but you're near a surface.
*  And I'm going to vote on that. And then projection, it gets the context from lateral layers.
*  And so then you have layers one through six, sort of all voting on their specific contextual
*  votes about this one property of the edginess. And then altogether, they vote on the thing as a whole.
*  Correct. That's perfectly done. Yes.
*  Okay. Okay. So I mean, is it useful? Should we break down the different roles of the different
*  laminae? Or is that maybe too fine-grained? I don't know.
*  We could. So we could at least try. So one thing this brings up is that when you measure it the
*  right way, all the neurons in a cortical column will tend to have the same receptive field. And
*  this is, of course, observed. But also you will see that the receptive fields will change based on
*  the context. So initially, if you are measuring it based on purely bottom-up evidence and just
*  power it through, you will see that all the different laminae, neurons in all the different
*  laminae have the same classical receptive field. But then depending upon which lamina they are in,
*  and depending on what contextual computation they're doing, their classical receptive field
*  can change into something more dynamic and something that depends on extra columnar input,
*  or the inputs that are not directly bottom-up for that column, but based on lateral or top-down
*  inputs. So if you go lamina to lamina, so in the mapping, layer four is, of course,
*  feed-forward input. Layer two, three has multiple roles. One is computing the lateral connections
*  for contour continuity. And the other is pooling, just like in a complex cell, pooling information
*  for invariant representation, and then projecting to the next high level. And then layer five,
*  which is below layer four, is pretty much doing the same computations as layer two, three. But now
*  that layer also includes feedback from above. So in this mapping, as you mentioned before,
*  every node in the probabilistic graphical model needs to have multiple copies in a
*  neurobiological implementation, because you need to have messages going in different directions,
*  being represented by a different set of neurons, because neurons are not bidirectional. And that's
*  why the same computation, which happens in the feed-forward pathway, is also kind of replicated
*  in the feedback pathway, because one is using purely feed-forward information, the other is
*  using a combination of feed-forward and feedback information. So layer five is lateral connections
*  and unpooling, so that uses the combination of feed-forward and feedback information.
*  And in layer five, also a sub-lamina of layer five is involved in belief computation, which uses both
*  feed-forward, feedback, lateral, all those things together. And then layer six is computing feedback
*  messages to send to the children. So that's the rough breakdown.
*  All right, good. Yeah. Everybody memorize that? All right. It's nice. It's in the paper.
*  I mean, I'm just going to start listing interesting things as we go through here,
*  things that are interesting to me. So copies. So the clonally related excitatory neurons
*  are copies to participate in different lateral and hierarchical contexts. So when Cortex is
*  developing, these clonal neurons, they all come from the same neuron, essentially, when these
*  neurons are being created. And that's what's referred to, I believe, as these clonal neurons.
*  And so what role do these copies or clones play within the processing?
*  So this is an interesting aspect that kind of falls out of the model and the mapping it produces
*  to biology. So the model used clones in its representation for representing higher order
*  contexts. And this is also related to our work on cognitive maps, where you're using different
*  clones to represent different contexts. So that same idea is also used in RCN. And instead of
*  temporal thing, it was in the context of lateral connections. Is this line part of
*  what different curvatures are a line part of? And representing that in an efficient way uses
*  clones in that representation. So basically what it means is that if you think of these
*  lateral connections as a sequence and different curvatures are different sequences it participates
*  in, then you can think of it as a particular feature, which is an edge in this case, has
*  different clones for participating in these different curvatures. And that's a very efficient
*  way to represent this higher order lateral context. So that's one place in which these
*  clonal neurons come in. And this, if I'm going to speculate forward, this might be a general
*  property of how a cortical column represents higher order information using cloning. We're
*  basically saying you create different clones for the different higher order contexts it is
*  participating in, whether it is lateral context based on line continuation or whether it is
*  sequential context based on temporal continuation or whether it is based on surface properties.
*  So just using different clones for different contexts might be a general property. That's one
*  aspect. And there's also another aspect, which is basically saying irrespective of what a cortical
*  column represents, you need to have some basic computations to be done in that cortical column,
*  which is part of inference saying, oh, it doesn't matter whether it is representing line segment or
*  a character or a frequency bin, you still need to process feed forward information,
*  combine it with feedback information, lateral information, etc. And those set of computations
*  imply a particular connectivity. And those connectivity can be wired up front. You don't
*  need to wait for environmental signals to come in to wire them because those computations are
*  irrespective of what the column represents. So that's this idea of establishing some connections
*  a priori in a cortical column. That don't need to be learned. They don't need to go
*  undergo any learning. It's just hard wired. Yeah, exactly. And this is also related to
*  the clonal neurons. There are some recent papers which we cite in our paper showing that
*  a lot of vertical wiring in the cortical column can be established a priori and are established
*  a priori. And maybe those synapses will still retain some plasticity, but you don't need that
*  plasticity to be the one establishing those connections. Yeah, maybe a lower sensitivity
*  to change, perhaps. Correct. Right. I mean, this is in contrast to the lateral connections
*  between columns which have in the model a higher learning capacity, learning sensitivity.
*  Correct. Yeah. So the lateral connections are all learned. You can, of course, genetically project
*  them to an area where they are more likely to make connections. But the specific connections it makes
*  to other cortical columns are learned because the definitions of cortical columns themselves are
*  learned. So whether a cortical column represents an edge or not is not something that's a priori. So
*  the lateral connections will depend on what those cortical columns themselves represent. So they
*  have to be learned. So I mean, this is all about one of the things that I love about this.
*  I've been reading about prefrontal cortex. Was it passing him in Ys? I don't remember. But
*  the overarching theory of the prefrontal cortex function in their view is that it's all about
*  context and planning actions, but vastly based on the context of multiple different sources of
*  information that are coming in. And this really fits with that broadly, just these lateral
*  connections, because it just makes a lot of sense. There was a postdoc that I used to work with,
*  and he was all about context, and I used to make fun of him. He's probably much more successful
*  than I am now. But I've come around on it and thinking, wow, it really is a fundamentally
*  important thing to do to be able to move through the world, is to integrate these different sources
*  of information. And it's all about context. So maybe we can just go through a bit of the
*  processing. And then this is when we can bring the thalamus in as well. And of course, this is all
*  detailed in the paper. But essentially, there is a feedforward pass, which you already mentioned,
*  and it goes through this sequence of features, laterals, pools, this cascade. There's also a
*  feedback pass, which goes through the reverse of those features. It cascades in the reverse
*  direction. So it goes pools, laterals, features. And I don't know if you want to comment on
*  the functionality of that. Well, features are detecting co-occurrences,
*  line segments or corners. And laterals are just enforcing continuity between in the line
*  representations, so contour continuity. And pools are pooling for invariance so that the higher level
*  can be more invariant. And that's a structure that is repeated in the hierarchy. And it's just that
*  it is formulated as a generative model so that you can sample from the model and also pay top
*  down attention, control things with top down attention, etc. That's kind of the core of the
*  RCN, right? So there's this forward pass, and then going to the top, and then there's the top down
*  attention feedback pass that then hones in on the correct answer. Is that a way to put it? Yes.
*  It comes iteratively to the correct answer. Yeah, it refines the bottom up projections
*  and refines it into the top down generative fashion. So I'm just stumbling over my words here.
*  Okay, so that's kind of the core of the RCN. And now let's bring the thalamus in because there's
*  this cortical-thalamo-cortical pathway, which you describe as explaining away where the thalamus is
*  explaining away these or factors. Maybe you could describe that. Yeah, so when you have
*  multiple things modeled in your model or in the brain, so you can think of it as each thing you're
*  modeling, whether it is an edge or whether it is an object, it is specifying how it generates
*  the input. So when you think of an edge, it's basically saying, okay, if I activate this edge
*  feature, it will generate this set of pixels in the world. And if it's an A, it's basically
*  specifying if I poke this node, it will generate these pixels in the world. And now, of course,
*  many of these things are interconnected. If you poke an edge and an adjacent edge, then
*  they will overlap in the fields that they generate. Some set of pixels will be overlapping between
*  an edge and adjacent edge when you try to generate them. And then when you actually do influence in
*  the real world, you need to find which subset of these need to be on because some of the evidence
*  will be overlapping between them. And we have some examples of this happening in captures where
*  when you look locally, because of the juxtaposition between these characters, you can
*  start seeing characters in between some of these characters. For example, when you bring an R and
*  N close to each other, it can look like an M. So all the locally, the evidence for that character
*  might be very strong in the global parsing of the scene that evidence is just a hallucination and
*  needs to be explained away. And so this is the core idea called explaining area, which
*  happens in probabilistic graphical models naturally if you formulate it the right way. And when you're
*  parsing a scene, yes, you definitely need to explain every local evidence using the global
*  context. And not only that, it's not a competition that happens just at the first level. This needs
*  to happen between every level in the hierarchy. So from V1 to V2, from V2 to V4, you need to have
*  these explaining of computations because the things that are modeled in V2 also have overlap
*  in V1. And you need to explain them in a hierarchy. And these explaining of computations
*  exist in RCN because it's a computational requirement. If you want to come to global
*  consensus, you need to explain a local evidence. It's something we had to put in there because
*  that's the only way to make the model work. And then when we worked back from that to see where
*  it would fit in this cortical mapping, there was no place to fit it other than in the thalamus.
*  And not only that, it turned out to be a very, very good mapping to what the computations,
*  the thalamus is doing. And I would say based on this mapping, it kind of starting to make sense
*  why it would be implemented in the thalamus and why it is related to other projections to the
*  thalamus, et cetera. So basically, if you think about what this explaining of a computation does,
*  it's gating of feedforward information based on feedback information. That's fundamentally when
*  you look at what is happening in a subset of neurons or in a node in RCN when you pass messages
*  for explaining away, it's routing of bottom-up evidence based on top-down support. So if a node
*  has two parents pointing to it, both are causal influence on this node being on. So a pixel can
*  be on due to parent A or parent B. And now evidence comes in from bottom-up saying, oh,
*  this pixel should be on 0.9. That's the likelihood of this pixel being on. Now you have to make a
*  decision locally on how to share that piece of evidence among the parents. Should you basically
*  say, oh, 0.9 goes to parent A or 0.9 goes to parent B or is it a fraction of half of 0.9 goes
*  to parent A? And this depends on how much other support does parent A or parent B have. So if
*  somebody says parent B from elsewhere in the network, you know that parent B is the one likely
*  to be on, then you pass all the evidence to parent B and you give very little to parent A.
*  So it's based on this top-down information that you get from these parents on how much support
*  they have from elsewhere in the network, you decide to route this bottom-up information.
*  So that is the fundamental computation that is happening in this explaining away circuit.
*  And that fits very well with what Sherman and Guillory and many other people have
*  found out about the thalamic circuit. Like the feedback connections from layer six in the cortex
*  projecting back to the thalamus. So it's almost like a center-on mechanism, although it's not
*  anatomically set up the same way. How is explaining away then related to attention?
*  Because you were saying top-down and that's like an attentional kind of mechanism. Is it attention or
*  how does it relate? So attention, you can think of it as a very special case of explaining away.
*  So this explaining away is a mechanism where the parents can be kind of half on or half off. They
*  don't have to be full. They don't have to commit to being fully on or fully off. And even then,
*  this computation happens. But now suppose you set a parent to be off or a set a parent to be on,
*  then that is hard. I would call it hard explaining away. And so that is attention.
*  So basically you're saying, oh, I want the computations to happen under the assumption that
*  the letter A is on. So turning that letter on top-down will basically change the nature
*  of explaining away computations happening at the lower level. So the explaining away is happening
*  anyway, but then the attention can have an effect on top of the explaining away. Exactly.
*  One of the worst times I had coming down off of acid, I was laying in bed trying to sleep and
*  still my mind couldn't stop. I saw this cylindrical green thing made up of almost like Minecraft
*  blocks. Minecraft didn't exist back then. But it kept spinning and spinning and these blocks kept
*  coming in and adding to it and adding to it. It was driving me insane. But this, what I'm wondering
*  is, first of all, what's your worst experience on acid? No. What I'm wondering is if you didn't
*  have these explaining away mechanisms, my guess is it would be like an acid trip where everything
*  is super local and you can't sharpen anything. You can't have the global features. You can't
*  filter anything out basically and everything is present and interacting. How does that sound?
*  Well, that all sounds reasonable. This is something I have to extend the theory to.
*  Oh yeah, because psychedelics are back. You could make a therapeutic use for explaining away.
*  Exactly. Yeah. So I haven't done much on that one, especially this idea of feeding the top
*  down input back into the network. So basically, this is where there is no sensory input. Your
*  eyes are closed and the system is running on its own. So you're generating your top down input and
*  effectively feeding it back into your network. And that is obviously some amount of mixing of
*  top down and bottom up is happening all the time in the network. But where you cut off the bottom
*  up totally and feed it back in, that's something we haven't explored much in detail. But I would
*  love to because of the connections to psychedelics and also because of the connections to some other
*  things like schizophrenia where we start mixing what is real versus what is hallucinated. So that
*  would be an interesting direction in which to take this model. We haven't done anything that,
*  but that is an interesting way to look at it. That is interesting. I want to introduce you to
*  my friend. I have a friend a few states away who's growing his own mushrooms,
*  it's like a mushroom. He keeps sending me these pictures. I haven't done psychedelics in a long
*  time, but I'll hook you up with him. That's the language of the kids. But so anyway, just bringing
*  you back a moment because your story then, the story of your model here is that these feedback
*  projections from the cortex come on to thalamus and have these explaining away mechanisms.
*  Randy O'Reilly's story is that the feedback projections, same feedback projections,
*  but in this case they are comparing the generative prediction with the bottom up information.
*  Yours is as well, but in his case it's a story about learning how off the prediction is and then
*  that's how plasticity happens within these circuits. The temporal difference between
*  the prediction and the bottom up gets sent and drives the learning in cortex. I don't see
*  a problem for both of these things to be correct. I'm not sure.
*  That's right. I don't see why both can't be correct. Especially in our model, we don't talk
*  about the learning part at all. We are really talking about the inference side. Once the model
*  is learned, how does inference happen? I won't be surprised if learning involves some mechanism
*  like O'Reilly suggesting there based on error between the prediction from one layer
*  and the other, how the synapses are adapted. I won't be surprised there. They can both be
*  compatible, but I do want to make a contrasting statement between what our model is doing and
*  this generally accepted idea about predictive coding. Predictive coding is a popular word in
*  neuroscience and it's used everywhere. Every model is a predictive coding model. That's right.
*  KippaCampus is a predictive coding model. Michel Cotex is a predictive coding model.
*  Predictive coding is thrown out. Just a word that is just overused everywhere.
*  That's a bonanza. You could say it's a bonanza these days of predictive coding in the literature.
*  Yes. When you look at what actually predictive coding, if you go back to the
*  literature and look at what predictive coding entails, this is during inference. We are not
*  talking about learning. This is during inference. It needs to subtract the top-down input from the
*  bottom-up information. Then only the errors between the top-down prediction and the
*  bottom-up input are passed up. That's actual computation. If you want to
*  map that word to an actual computation, but that computation of subtracting the top-down
*  predictions from bottom-up input makes many restrictive assumptions. It's basically assuming
*  that your model is linear and your noise is Gaussian. It's only in that setting that
*  subtracting the top-down predictions from bottom-up input makes sense. I would say this might go back
*  to one of the first papers on predictive coding, which was from Raj Rajashrao. This was a nature
*  neuroscience paper. But then that idea got stuck. Basically saying, oh, this idea that you should
*  subtract top-down predictions from bottom-up input is the right way to do things that somehow got
*  stuck. That's the way. Right. But it is not. What you want to do is combine bottom-up input with
*  top-down. You want to say top-down prediction influences how bottom-up information is
*  sent up. But it is not a subtraction. Sometimes it can be an amplification of compatible regions.
*  So if top-down prediction agrees with bottom-up input, you keep those things around. You pass
*  those up. Where there is a mismatch, you can kill off the bottom-up input. It depends on
*  the particular context in which the computation is happening, whether it is based on top-down
*  attention, whether it is just software explaining away. It's a richer story than just subtract top-down
*  input from bottom-up evidence. I would call it more, rather than calling it predictive coding,
*  it's probabilistic inference. What is happening is probabilistic inference of combining bottom-up
*  and top-down information. That can look like subtraction in some settings. It can look like
*  amplification in some other settings. In reality, it will be a mix of both of those things.
*  You have the model. It's not just a model. It does things. It accounts for things. You go through
*  multiple visual phenomena that it accounts for in the paper. I'll just let you choose. Maybe
*  you can just describe one of the phenomena that it accounts for and just a little bit about how
*  it does so. One of the phenomena that we explain and replicate in our paper is the subjective
*  contour effect. Subjective contour effect is where you see parts of an object as the bottom-up
*  stimuli, but the rest of the object is filled in top-down and you actually hallucinate things that
*  do not exist in the real world. This is the famous Kinesa triangle example. It's the most salient
*  thing I can think of in this category where what you're seeing bottom-up in terms of the real
*  evidence is just these three Pac-Man-like figures, which are the corners of the triangle, but your
*  brain actually hallucinates. You interpret the image as a triangle sitting on top of three circular
*  disks. That is your interpretation of the image. Then your brain, in its vast wisdom, actually
*  hallucinates the three edges of the triangle. When you look at this, an image like that, you
*  actually perceive a faint line and that line is not there.
*  The faint line is...
*  Delineating the shape of the triangle.
*  Right. That faint line is completely created by your brain. This is something that fits very well
*  with the theory because this hallucinating something that doesn't exist is part of inference
*  because that hallucination is part of the best explanation that the brain is cooking up for the
*  scene. If you are thinking in terms of cortical columns, you can basically say what happens in
*  the cortical column in that location where there is no bottom-up evidence. That cortical column
*  is looking at a segment of the portion of the image where there is nothing. It's just blank.
*  Then it is hallucinating a line there. You can think of what happens as part of the dynamics there.
*  When bottom-up input comes in, layer four neurons will be essentially silent. Nothing to see here.
*  A blank image. Later on, when the context kicks in and the top-down and the lateral context kick in...
*  The lateral context in this case would be... Correct me if I'm wrong. You'd have a receptive field
*  for one cortical column or something in that blank spot where there is no line.
*  But then next to it, because it's a topographical map in the cortex, let's say,
*  next to it is the edge of one of those Pac-Man shapes. It's getting that context that there is
*  this edge near me even though I'm blank. That's a feed-forward pass through with the context.
*  Then it will also be compatible with the final decision arrived at the top, which is,
*  oh, it's a triangle. There will be top-down information saying that, oh, it's a triangle.
*  That means all these columns in between should be on. At first, it's like, I think it might be a
*  triangle. Oh, no. Then it goes and goes, oh, it's a triangle. Then it really clamps it down.
*  Correct. You can think of what will happen in that cortical column. Initially, you don't say,
*  oh, blank. Nothing to see here. But then as the lateral context and top-down context gets
*  incorporated, suddenly neurons in this other laminae, which are responsible for representing
*  those aspects of computation of that cortical column, will turn on. Then finally, when you
*  look at the belief of that column, it should basically say, oh, I am on.
*  Similarly, the belief neurons in the outer edges of the Pac-Man, which is the circular parts of
*  the Pac-Man, it should say they're off because that's not part of the explanation of the triangle.
*  If you're paying attention only to the triangle. If you basically are clamping the triangle at the
*  top, then the circular parts of the Pac-Man should turn off and you should be able to see that in the
*  cortical column. That's effectively what we're doing. What we are doing is virtual neurophysiology.
*  It's almost like we have a functioning monkey in the lab and we can show it stimuli and basically
*  record from different layers and show this is how information settles and this is how it arrives at
*  the final answer. You can extend this to not just the Kineser triangle explanations and
*  subjective contours explanation in our model. Mostly uses just the contour model, but you can
*  also extend it to an illusion called the neon color spreading illusion, which also it's a
*  two layered illusion. There are subjective contours in it because it is hallucinating edges.
*  Not only that, it's also hallucinating the color inside the circle and it's interesting that
*  the color hallucination respects the hallucinated edges. The color doesn't bleed out of the edges.
*  It's interesting in that way. We can replicate the dynamics of that too. Hopefully, it's also making
*  some predictions about how that illusion also comes into effect.
*  Steve Grossberg has work on this sort of color spreading and respecting the boundaries of the
*  neon thing as well. It looks like it's along the same lines explanatorily.
*  While you were talking, I was just thinking about the Necker cube and these phenomena where your
*  conscious experience of something switches on this slow time scale. Have you thought about that and
*  how that might fit into the model? Yes, we have actually. In fact, we have several examples like
*  that in the lab at Vicarious where precisely the Necker cube one, we have created that one and
*  replicated it just to not get it into the paper. There's a Necker cube one, the phase-square solution.
*  There are a handful of them like that.
*  You can make them flip by just randomly perturbing the network or you could also even see
*  because we have full access to the model, you can also see which nodes should I perturb. If you want
*  to do the minimum amount of perturbation, which nodes in the network should I perturb so that I
*  flip the explanation to the other thing. Those are fascinating illusions to play with
*  because they are all, I would say, results of doing inference on a model.
*  To the inference to the best explanation. Yes.
*  Right.
*  Dalip, this is great stuff as always. You must be very confident in the model.
*  Let's say a healthy skeptic's confidence, perhaps.
*  That's right. Yes. My philosophy is that you want to be the
*  most skeptical about your own model. Only you can be because you know what works and
*  all the nitty gritties of what works and what doesn't work. It's in the right direction,
*  I would say. There are so many things to be worked on and improved and some fundamental
*  problems to be fixed. We will be tackling all of those as we go. I would say the general direction
*  in which we are going, I am very confident about that.
*  It's the Richard Feynman quote. The first principle is that you must not fool yourself
*  and you are the easiest person to fool. It sounds like you have that attitude.
*  When are we going to see this thing published in Nature? It's on archive right now, right?
*  Yeah. We still have to do a little bit more work for clearing it up. We haven't submitted it yet.
*  You haven't? Okay.
*  No. I hope to submit it in the coming month. If you have feedback, I can use it. If any of
*  your listeners have feedback, I can use it before submitting and maybe it will help smooth the
*  process. Wonderful. There you go, listeners. Dalip has put the call out for feedback.
*  Dalip, thanks again. If we keep this current trajectory, I'm not sure if it follows a power law
*  distribution of our podcast rate, but I'm pretty sure that we should have another episode in
*  probably about two hours from now. It might be a little bit longer than that, but it's always fun
*  and I really appreciate you coming on and I wish you success going forward, of course.
*  Thanks, Paul. It is always fun to be on this one. I don't intend to come back in the next two hours.
*  Now, I think I have talked too much. I need to go and get some work done. That's what I should do.
*  Great. Happy working, my friend. Take care. Thank you.

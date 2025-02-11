---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 6704s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 3480
Video Rating: None
---

# BI 138 Matthew Larkum: The Dendrite Hypothesis
**Brain Inspired:** [June 06, 2022](https://www.youtube.com/watch?v=gv3PhpGtTbI)
*  The bane of neuroscience has been that most methods record from the cell body.
*  And so I think we're all somatocentric, I like to say, which means that we all think
*  that the spike at the cell body is somehow more meaningful than anything else that happens
*  in the neuron.
*  And I think from a computational point of view, it's the least interesting part of the
*  neuron.
*  The question is, if having just seen a movie and somebody recorded all your action potentials,
*  if they replayed all the action potentials very faithfully at every neuron in your brain,
*  would you have the experience of seeing the movie again?
*  This is Brain Inspired.
*  Welcome to Brain Inspired, I'm Paul.
*  Are dendrites conceptually useful?
*  That's the title of a recent perspective piece from Matthew Larkham, whose voice you
*  just heard.
*  Matthew runs his lab at Humboldt University of Berlin, where his group studies how dendrites
*  contribute to computations within and across layers of the neocortex.
*  Over the past few years, Matthew has published many theoretical proposals and many experimental
*  results that argue for a better appreciation of the role of dendrites in our cognition,
*  like perception, memory, consciousness.
*  All of these ideas fall out from the unique structure of pyramidal neurons in our cortex.
*  Paraminal neurons are the majority of the neurons in our cortex, and although we name
*  their cell bodies are in the cortical layers, like layer 5 pyramidal neurons or layer 2-3
*  pyramidal neurons, Matthew argues it's more useful to consider which layers their dendrites
*  occupy, because their dendritic trees stretch out in different directions to receive incoming
*  signals from different areas of the brain.
*  For example, layer 5 pyramidal neurons have a set of dendrites at their base, which receives
*  mostly feed-forward projections from earlier brain areas, and by earlier I mean closer
*  to sensory areas, so as early visual cortex projects forward, those projections land on
*  the basal dendrites of the later area.
*  Those same layer 5 pyramidal neurons have dendrites that project up into layer 1 of
*  the cortex, called apical dendrites, and those dendrites largely receive feedback projections
*  from later brain areas.
*  That's simplistic of course, because there are other lateral projections and connections
*  across layers of the cortex and so on.
*  But the story remains that these two sets of dendrites from the same neuron are receiving
*  signals from fundamentally different brain areas.
*  One of Matthew's early key findings was that these two sets of dendrites are electrically
*  separated, and depending on what's receiving signals at any given time, the neuron will
*  either be silent, if only the apical dendrites are receiving signal, or will fire at low
*  levels if only the basal dendrites are receiving signal, or fire in a bursting mode if both
*  are simultaneously receiving signal.
*  This led Matthew to realize this coincidence detection type mechanism makes for a great
*  way to associate feed-forward sensory-like information with feedback, memory, or context-like
*  information, and might therefore be a fundamental principle of how the cortex operates, a big
*  question in neuroscience.
*  So we discuss a handful of the ideas and experiments that fall out from that, like I said, related
*  to learning and memory and consciousness and more.
*  We also discuss how Matthew's work has made him appreciate how a bottom-up approach or
*  examining the implementation level, in terms of Mars' famous levels of analysis, can inform
*  what algorithms and computations might be possible, as opposed to starting with the
*  computation and figuring out how it must work in the brain.
*  We talk about how the principles derived from dendritic computation might improve deep learning.
*  You may remember many episodes ago, I had Blake Richards on, that was episode 9, and
*  Blake used Matthew's work as inspiration for his neural network models to solve back
*  propagation in the brain, for example.
*  And toward the end, we discuss a recent thought experiment Matthew and a couple of colleagues
*  offered asking whether action potentials, or more broadly brain activities, cause consciousness.
*  Oh, and there are a few guest questions from Mack Shine, a previous guest on episode 121.
*  Okay, sorry for the long intro, but I thought it would be useful to set up the background
*  a little, even though we cover it in more detail in the episode.
*  Find links to Matthew's lab and the papers we discuss in the show notes at braininspired.co.
*  And here's to the dendrite.
*  And enjoy Matthew.
*  Matthew, pleasure to have you on.
*  It's wonderful to be here.
*  I've really enjoyed the podcast.
*  It's been, for me, a revelation.
*  My PhD student put me onto it, I think around about the time you interviewed Yogi Buzaki.
*  And since then, I've just faithfully listened to it nearly every week.
*  Oh, that's so funny that-
*  For me, it's a fantastic thing.
*  Oh, well, thanks for saying that.
*  It's funny that I hear that quite often that someone's PhD student put them onto it, just
*  as you said.
*  So I guess it's working in that respect.
*  I was trying to figure out how to describe what it is that you do.
*  And one way to describe that would be that you are wreaking havoc on the notion of the
*  primacy of the neuron cell body and the action potentials produced there and championing
*  the role of dendrites.
*  That's a very simplistic way to say it, but how would you say it?
*  Oh, I'm glad you put it like that, actually, because I would like that message to come
*  across.
*  I don't know where to start in the trajectory of explaining how you could come to that opinion.
*  Well, from a historical point of view, from a methodological point of view, I think that
*  the bane of neuroscience has been that most methods record from the cell body.
*  And so if you think of like an extracellular recording, it'll pick up spikes that are near
*  the tip of the electrode.
*  And if you do it, obviously, if you do a targeted whole cell patch recording or even a juxta
*  cellular patch, or if you use other methods like calcium imaging, which is now one of
*  the main methods in neuroscience, they all are much better at picking up signals from
*  cell bodies.
*  And so I think we're all somatocentric, I like to say, which means that we all think
*  the spike at the cell body is somehow more meaningful than anything else that happens
*  in the neuron.
*  And I think from a computational point of view, it's the least interesting part of the
*  neuron.
*  And I think that, I mean, if you would do this exercise, if you would take, if you'd
*  collapse all of the branch points in a neuron, including the cell body, and you'd make them
*  all just tiny nodes, right?
*  So that there's no big sack of lipid which represents the cell body anymore, but just
*  little junctions where things meet.
*  Obviously, now your electrodes would not think the cell body is special in any way.
*  The axon is where you could say the output is, and it's also where the output is generated,
*  which happens to come out of the somatic node, but who'd know that if it was as small as
*  every other junction point in the neuron.
*  And now you would be saying this entity, the collapsed neuron, would be transforming
*  inputs that come everywhere, more or less everywhere else but the cell body, not completely,
*  but to a first approximation, and transforms it in the axon to outputs that also go all
*  over the place.
*  You'd never mentioned the cell body, and yet this is the place that is central to describing
*  a neuron and to describing the computations that neurons make.
*  So I think in the first instance, it's almost irrelevant.
*  Well, I know that I've heard you talk about how Ramonica Hall appreciated the role of,
*  well, the potential role of dendrites.
*  And in his beautiful drawings, it's interesting.
*  I don't know if in neuroscience it's still taught with the sort of cell body as the primary
*  focus, but when you look at his drawings, of course, there are all these different beautiful
*  of dendrites and axons.
*  And you've quoted him in some of his work appreciating and sort of speculating that
*  there might be a computational kind of role for those dendrites.
*  So do you know, is it still taught that, I don't know if you teach neuroscience?
*  I do, yeah.
*  Well, I know that I'm sure the way that you teach sort of diminishes the role of the cell
*  body, but I guess writ large in textbooks, it's still somaticentric, as you said.
*  That's right.
*  I start with the, when I get to the subject, I start with a slide showing about 10 different
*  pictures from textbooks.
*  And they typically, almost all of them have a sizable cell body, looks like an orange
*  or something, and it's got little, tiny little sort of hairs coming out of it, which are
*  the dendrites, but they're really de-emphasized.
*  And then if you're lucky, it's got one myelinated axon coming out and then a sort of hand structure
*  at the end, which represents what could be the processes of the axon.
*  And basically, the dendrites, you could forget them if you didn't look carefully in the textbook.
*  And yeah, I guess I complain usually in my lecture that this is my favorite subject and
*  the dendrites are missing, but there's usually a few titles and then we get on with just
*  describing the way you have to basically, the way a neuron operates.
*  At least if we're talking about basic neuroscience, if I get high level course, then I get the
*  chance then to do all my propaganda on what I think the neurons are really doing.
*  So you're just disgruntled for a few moments there and then move on.
*  We were talking before I hit record that the arc of the story of your research is quite
*  long and I'm afraid that we're not going to be able to get to a lot of the things.
*  Maybe we could start, I'd like to start before 1999, but a lot of the, when you start, often
*  I think that you send people the 1999 paper in which you're recording apical dendrites
*  and from the basal dendrites as well.
*  So maybe we could start just what the dendrite hypothesis is and then I would love to hear
*  how you came about searching for these sorts of questions, doing these experiments and
*  asking these questions.
*  You know, I think it's going to work better the other way around because the only way
*  the dendrite hypothesis makes sense in my mind is to step back and look at the cortex.
*  The way I came to look, yes, right, the way I came to look at the cortex, first of all,
*  actually in the end it's, I think more recently, at least in my lab, exploring the way the
*  cortex interacts with subcortical structures and so it's perhaps a bit rash to just say
*  cortex, but nevertheless I think it's quintessentially a hypothesis about the cortex.
*  Is that how you began thinking about it or is that where the recordings and experiments
*  came from is thinking about cortex and the multilayered structure, etc.?
*  Right, absolutely.
*  So I found myself in a laboratory, it was Bert Sackmann's laboratory in Heidelberg,
*  which I arrived at in 1997 as my first postdoc and so this is the guy who's invented Patch
*  Clamp and won the Nobel Prize for it and by that point the lab was humming with, they
*  had almost a decade at this point of fabulous findings after being able to patch dendrites
*  for the first time at the same time that they could record from this whole body.
*  So basically do the first experiments into how signals were generated in the dendrites
*  and how they propagated around the neurons.
*  So I came into sort of a second generation of researchers looking at this after the first
*  amazing revolutionary experiments had been done and back then we took slices of cortex
*  from rats and so my first confrontation with the whole thing was to look at the cortex
*  side in the dish as it were under a high powered microscope and what you see in that situation
*  is mostly pyramidal neurons and if you've done a nice preparation you see the dendrites
*  quite nicely and so what you're effectively looking at is a forest of tall trees and where
*  the cell bodies have roots going down and they all oriented the same way like a forest
*  and then there are tough dendrites at the top and I don't think you can look at that
*  structure and not ask why the hell is the cortex made of these really peculiar but specialised
*  neurons and I think it's natural to and Cajal as you mentioned also did the same thing.
*  He looked at these neurons and said, well there's got to be something special about
*  these neurons but by then we were finding out that not only were they morphologically
*  special but physiologically or bi-physically so they have a whole complement of specialised
*  channels that are distributed in specialised ways that make this a much more complex machine
*  than the sort of neurons you find to this day in either models of the cortex or models
*  or artificial neural networks and so on. So they're just obviously on their face much
*  more complex but of course you don't know a priori what this complexity serves and the
*  and what it's doing. So when I got to the lab the talk of the town was the latest recordings
*  and publications of Jackie Schiller and Greg Stewart that had shown that there was not
*  just a spike in the axon but there was a special dendritic spike. We subsequently found there
*  were more than one type but at the time there was a so-called calcium spike or sometimes
*  called a calcium plateau potential right at the top of this tree. You can think of it
*  like a big oak tree or something. Just before the branching out into the tufts there's
*  another zone, an initiation zone for an incredible spike that's more like the spike you get in
*  heart muscle and it's actually due to the same channels. It's the long lasting calcium
*  channels that sustain a plateau in this dendrite. So it's altogether more amazing and incredible
*  than the spike that we all know and love that comes out of the axon, the so-called sodium
*  spike. At the time people, in particular Sackman I think was the boss as it were, were skeptical
*  about whether or not the calcium spike would be of any use because it had a high threshold
*  and it was difficult to imagine what would actually make it fire. It wasn't completely
*  clear whether it was just an artifact or anecdotal.
*  Byproduct.
*  Yeah, byproduct. I remember I was trying to explain to my wife who as I say is a musician
*  and so it takes some time to get through these nutty details. I had to explain to her on
*  a long walk once what I was doing and what the point of this calcium spike was. The other
*  point that had been discovered just before that was that the sodium spike that everyone
*  knew went down the axon and signalled the next neuron also went back up the big trunk
*  of the tree.
*  Also a byproduct, right? That's the idea.
*  Maybe, yes, yes, right. People were speculating what the good of that was and so it all hit
*  me in an instant that it could be that the signal that's generated at the bottom of the
*  tree basically primes the top of the tree such that you can reach threshold for inputs
*  coming into effectively the leaves at the top, the dendritic tufts.
*  That idea just came to you of a sudden?
*  Yes, yes. It was a eureka moment on a Sunday as we were walking through the forest in Heidelberg.
*  By Monday afternoon I had the first result which was that indeed this is the case and
*  it's even more exciting that because what it does is halve the threshold for the big
*  plateau potential, the calcium spike in the dendrites and that in itself leads to a kind
*  of ping pong exchange between the top of the neuron and the bottom of the neuron that
*  causes it to burst fire.
*  Effectively you can arrange it such that innocuous inputs that appear to be doing nothing on
*  their own make the whole neuron explode. All of a sudden I think it was clear to me that
*  this was an associative device. The neuron was basically associating whatever came to
*  the top and the bottom of the neuron. The next question was what goes to the top and
*  the bottom of the neuron? To some extent we're still trying to work that out but I think
*  in broad strokes to a first approximation you can say that the top of the neuron receives
*  a lot of long range input that's predominantly feedback in some hierarchical sense, meaning
*  that if you've got something coming from a higher, let's say you said secondary visual
*  cortex or semi-incentory cortex going to primary cortex, it'll target the top of the cortex
*  and higher order thalamus targets the top of the cortex. Lots of superior colliculus
*  targets the top of the cortex. We've now subsequently learned that lots of memory structures target
*  the top of the cortex. If you saw that architecture in the first instance without knowing about
*  this physiological property you'd have to wonder what the hell it's doing going to the
*  top of this tree, particularly when you do the actual electrical recordings and you find
*  that it has no influence at the cell body. It's basically a flat line. If you put an
*  input at the top of the tree there's basically nothing to see at the bottom of the neuron.
*  That's because it's electrically decoupled essentially because of the long dendritic
*  tree structure.
*  That's right. This word decouple comes into the picture right in the most recent stories
*  that we've had because it turns out, and this is jumping right to the end now, that the
*  brain has a handy little switch to couple the top to the bottom of the neuron. That
*  means that it's possible. I should have completed the story and said that we think the bottom
*  is receiving predominantly feed forward, although let's just leave it in simplistic terms for
*  the moment. There's complexity in everything and exceptions to everything. To a first approximation
*  you've got a feed forward drive to the bottom and feed back to the top. If you would have
*  the neuron decoupled such that the top can't influence the bottom, then you've basically
*  taken feedback out of the system with one fell swoop. That's what the cortex has as
*  a handy switch and something that would be fantastic to try out in a model. I guess it's
*  too early at this point because that's a fairly recent discovery. In the dish, so in vitro,
*  they tend to be decoupled. When you put them in vivo in the awake state with the neuromodulation
*  and so on, they tend to be coupled. But coupled here, so the way this term coupled is going
*  to be confusing at this point of the story because it's still the case that the bottoms
*  can signal the top and cause a cooperative interaction between the two regions. That,
*  I think, is still a fundamental way of explaining what the purpose of the cortex is and what
*  it does, which may sound like a bold claim, but I'd have to deconstruct that claim to
*  try to convince anyone that that's the case. But now I'm completely convinced at this point
*  that the key to understanding the cortex is understanding this neuron and the architecture
*  of long range connectivity.
*  But so this neuron is a layer five pyramidal neuron and the cortex is made up of multiple
*  layers. Why this neuron? Because there are other layers that, of course, stretch out
*  among other layers in the column, stretch their dendrites and axons out, and of course
*  have lateral connections. So why the specific? Because I know that you're also looking at
*  layer two, three pyramidal neurons, which also have that kind of structure, but why
*  the layer five?
*  Yeah, so in the first instance I'd say it's the pyramidal neuronal type that should be
*  used with this description. They're all subtly different from each other. The main point
*  being what we call the layer five neuron is the neuron with the cell body in the soma,
*  which by the way, if my claim is right that the cell body is not relevant, then there's
*  nothing layer five about this neuron in particular.
*  No, let's pause there because you kind of reformulate. That's kind of the way that we
*  think of traditionally the cortex or the way I was taught is in layer five there are the
*  cell bodies of the pyramidal neurons, but you're kind of reformulating a perspective
*  on how to think about the cortex because all of the action taking place is essentially
*  outside of the layer. Well, a lot of it is outside of the layer in which the cell body
*  exists.
*  That's right.
*  I don't know, can you elaborate on how your perspective on the cortex differs then?
*  Sure. So I mean, I think in terms of describing what a neuron does, I think the easiest thing
*  to say is that it's transforming inputs into outputs. That's probably maybe too boring,
*  but if that's the case, then you have to look at where the inputs are and where the outputs
*  are. And maybe the last thing you want to ask is where is the transformation happening,
*  which could be everywhere. I'm claiming that the last place you want to look is the cell
*  body for this transformation. But in principle, the transformation starts where the inputs
*  arrive and involves the entire neuron in terms of because signals are going up and down,
*  back and forth and causing different kinds of signals in different places in a very,
*  very complex way, none of which has anything really to do with where the cell body happens
*  to be. And then in the end, the axon itself typically goes all over the place and you
*  can't easily predict which layer or even whether or not the output remains in the cortex. So
*  actually, there's no particular layer that this element, the neuron, is confined to.
*  If you ask yourself what is the function of this neuron, you're going to have to essentially
*  find out what are all of the interactions that can occur within the dendritic tree,
*  mostly within the dendritic tree. In principle, there's some things that could happen in the
*  axon. And then you're going to have to describe this in terms of the long range. So where
*  do the inputs to the cortex arrive and what they represent? What classes of information
*  this represents?
*  I realize we're talking about on a smaller scale than when people usually formulate hypotheses
*  about what the cortex is doing. They talk about the cortical column as if it's a unit
*  operation. And then there are different high level theories about what each column is doing
*  and then that's repeated over all of the different columns essentially and just specialized based
*  on where the column is. So is your idea about, it's less about the cortical column so much
*  or maybe you can correct me. I'm trying to think of how your ideas fit within the higher
*  theories of cortex, so to speak. Because we're talking about a very specific kind of cell
*  structure and the way that it is decoupled and or coupled depending on which kinds of
*  inputs and I'm kind of jumping the gun here I know.
*  I think it fits well into the idea of what the structure is.
*  I think it fits well into the view of the cortex's, the sort of Mountcastle view that
*  there are lots of vertically oriented columns that basically are all, dare I say feature
*  encoders or detectors. And very much with a kind of hierarchical view of that such that
*  some of these cortical columns are receiving more primary information. That means in the
*  stream of information from the outside world to the inside world they're early on. And
*  then there are other cortical columns that are higher up in that hierarchy meaning further
*  along the processing line. And then with lots of information going in the other direction.
*  And so in that scheme of things if we just stick to primary sensory cortex for a minute
*  then you would be claiming that any given, that the role of the pyramidal neurons in
*  this sense. First of all the layer five pyramidal neuron is the only neuron that spans all
*  of the layers, so collects input from all of the layers. And it's the only neuron that
*  goes completely out of the cortex with the exception of some layer six that also go to
*  the thalamus. But the layer five is an output neuron in the sense that it's projecting both
*  within the cortex long range but also outside the cortex very long range. They're the neurons
*  for instance that would go to your spinal cord and directly sign up onto motor neurons.
*  So that there's some kind of encapsulation if you like of what the column is doing. You'd
*  like to think anyway. It's hard to imagine that that's not the case. And so I presume
*  that the circuit of a column at a minimum is serving to encapsulate some feature that's
*  either in sensory space or at high levels are some more complex features. And that if you would
*  record from the layer five neuron you'll have the best idea of what the brain or cortex currently
*  thinks is a feature in cognitive space let's say. And in that world if that's a good way of
*  looking at the cortex I think there are two categorically two kinds of information at least
*  that and two really important types of information. One would be the feed-forward stream which would
*  represent the information coming from the external world and one would be the feedback stream which
*  would represent information that's been generated in the cortex itself. And it would make sense of
*  why you want to have neurons which are elongated and have a large collecting a large set of
*  dendrites collecting inputs at both ends and essentially at least two compartments to you can
*  imagine two boxes or two neurons in fact at both ends. And that one is predominantly collecting
*  one kind of information and the others predominantly connecting collecting the other kind of information.
*  And in fact since these are very difficult words to use feedback forward feed forward or top down
*  bottom up and typically this is the stumbling block for many conversations that you could just
*  take the attitude why not talk about a basal and an apical being the description of the top of
*  this neuron and basal being the bottom of the neuron. And then we could worry about what terms
*  we want to use later on for this but essentially you could say this neuron is allowing you first
*  to separate those two streams of information and then bring them together in special ways under
*  special conditions and have a way to manipulate those conditions and the way you combine them.
*  Well yeah I was going to ask because it's kind of easy to wrap your head around it when you're
*  talking about let's say early visual cortex right and where you're having most purely sensory data
*  coming in and you're looking at features of a tiger or something. I think you often use a
*  tiger in your examples and then in the so that's coming into the basal dendrites and then all these
*  and again I'm jumping the gun but these work I'm going to say feedback connections coming into the
*  apical dendrites which are you know memories of tigers and models that the brain is built etc.
*  Context is what you refer to so it's kind of easy to think about it like that but then as soon as
*  you go up another hierarchical layer that feed forward information is not sensory anymore or it's
*  less sensory but now it is it's still feed forward right but then it's with it's like the sensory
*  information that's been transformed by the context and memories and we'll talk maybe about
*  memories in a little bit so then it's like you said those are tricky terms feed forward and
*  feedback but all of the sudden you're already in a very kind of complex model as opposed to
*  like the simple sensory versus feedback story. I agree but I think that's the beauty of it I mean
*  the point would be that what is context for one region could be data for the next and vice versa
*  and this will depend on where you are in the in the processing but it could easily be that
*  the means that this is loops upon loops in some sense and that although there would be a way to
*  describe let's say a direction of flow of information in the end this is all going to be very much is
*  going to get very complicated very soon in terms of how you would describe what any given column
*  that's not at the top or the bottom is actually doing. I think the other thing that maybe is
*  occurring to you and occurs to most people is that what happens at the top because it turns out that
*  the other thing to say which I should have started with really is that the whole cortex is full of
*  these neurons that are ubiquitously everywhere and they're not in other structures they're like 70
*  80% of the cortex and you don't find them elsewhere so there's something special about
*  this neuron for sure and they're ubiquitous throughout the cortex and you find them at
*  the top of the so-called hierarchy just as much as you find them at the bottom and with
*  this simplistic way of describing it in terms of feed-forward feedback you know what's feeding
*  back to the apical tufts of neurons at the top of this hierarchy you might ask. Right oh I just
*  drew I was drawing this out and I have a big question mark right there in my diagram. Right
*  that's so in I think when we get to this point you want to that's where I think the words fail us
*  and where the where the language is really just a hindrance. What I'd rather say is that we've
*  got a that the cortical column is is as architecturally speaking at least from the point of the neurons and
*  the the six layers and so on is more or less the same in at the top of the hierarchy as it is at
*  the bottom of the hierarchy and and I presume well we know that the properties of these neurons are
*  if not identical roughly the same and and so we do know that inputs coming to the top of neurons
*  in prefrontal cortex is doing roughly the same as as inputs to the top of neurons in sensory cortex
*  so that's where I say it'd probably be better to reframe what a cortical column does with it with
*  respect to the top and the bottom of these neurons which ends up being particular layers rather than
*  rather than trying to find an English word to describe that this the information categorically
*  such that it's always the same. There's probably a good German word for it no? Probably yeah no well
*  actually when it comes to these words I think they're they use the English I'm just trying to
*  think whether there's a specialized German word for feedback and feed for me. Don't they just stick
*  words together and yes they do yeah yeah yeah we could probably definitely yeah in any case the I
*  think the fact that it's that it's the same everywhere is in a sense the guiding principle
*  for for claiming that that there's something special about this neuron about what it's actually
*  doing in the first place and then then you can ask yourself well I mean essentially what the word
*  you brought up the word context which is the best word I think one can find for as a best English
*  word I think to describe what might be coming to the top in other words if you imagine that the
*  the output of this neuron is is encoding some either low level or high level feature that a
*  feature is is everything that you're trying to encapsulate and propagate and context is everything
*  other than that that relates to it so when when if you're talking about the tiger for instance which
*  is what I always go back to then then if you're talking about the color orange you might want to
*  associate you so you're the you're the orange column let's say and or let's say you're talking
*  about the neuron that is that is giving information about whether or not orange is in your cognitive
*  space then other things that are not orange but relate to orange particularly in the case of a
*  tiger what can then be linked if you like and if you asked where are they linked I would say they're
*  linked at the top of the neuron that the top of the neuron can get other other things that tend
*  to happen when when orange is in your cognitive space if you ever think about tigers then you'll
*  have learned to associate stripes and and growls and movement and and anything else that pertains
*  to that and I would expect to be finding that kind of information affects the top of the orange
*  column in your brain and and then if we if we don't transfer that to to higher cortical areas
*  it's still the same operation you saw so especially doing some complex decision there'll be some
*  output that is relates to the decision and the type of decision you're trying to make and so on
*  and there'll be other things that often occurred during that decision that are not the decision
*  itself that would that you could call context that come to the top of that neuron is this a good time
*  do you think to talk about consciousness and the dendritic integration theory because what you know
*  we're talking about you've used the word feature right where each that's what gets passed along but
*  then when we think of our experiences coupling the features for the the input with the context
*  and then a feature is passed along and that's happening at every hierarchical level and as
*  we just said there's a big question mark about the top and how it's the wrong way to think about it
*  but one of the things that you guys found have found is that under anesthesia it's decoupled the
*  pyramidal neuron is decoupled and when we're awake in a conscious state it's coupled so however if
*  we're in a conscious state the coupling would be you know all over the the cortex right everything
*  is potentially at least coupled so then I you immediately think well how does this well maybe
*  you can explain what the dendritic integration theory is and then maybe we could discuss like
*  how to wrap our heads around where our experience arises essentially you know this is terrible it's
*  a podcast and we have to use language and language is no good right but I ought to be able to do this
*  I'm glad to start with the with the anesthesia because I think in a way we we don't it's a very
*  nascent theory of consciousness I think it's more theory of of loss of consciousness at the moment
*  and it's it's giving us some hopefully some information about consciousness and the sense
*  in which we're proposing a theory of consciousness is not so much that we think we solve consciousness
*  but we're looking at the lead the other leading theories of consciousness and saying how does this
*  mechanism that we found that clearly is at least correlated to loss of consciousness if not the
*  mechanism for the loss of consciousness how what that actually informs us and and how that relates
*  to the leading theories of consciousness so yes it's as you say the if you if you record from the
*  these the cell body of the or so close to the axon of of a layer five neuron in an awake in this case
*  mouse and you you opt to genetically depolarize or excite the the top of the neuron you see what
*  we see under many situations in vitro where the the top signals to the bottom and causes it to
*  burst fire as I've seen before and and and and this is very clear to see and then if if you
*  anesthetize the animal with with different kinds of it anesthetics you find that it flatlines that
*  the although you continue to to excite the top because we're basically imposing that opto
*  that's to say we express channeled opsin in the neurons and put lights specifically on the top
*  of the neuron then you under the anesthesia you get no effect at all in terms of self firing of
*  this neuron and well that was for me astonishing in the first instance because I mean you might
*  think well anesthetics are anyway subduing the network and so on and so maybe you should expect
*  that but but this is a biophysical claim because we're taking single neurons and we're forcing
*  depolarization at the top of the neuron and we're saying that depolarization is not doing what it did
*  just a minute ago it's not getting to the bottom of the neuron so it's a claim a biophysical claim
*  about the neurons of course we do think that that circuit elements are impinging on that neuron and
*  preventing the coupling from the top to the bottom but but what it's what in that instant what we
*  could see is that well after a few more experiments maybe I should say because what let me just
*  wish that always completely the the the we also found that if you suppress the higher order
*  thalamus that projects to that particular region that you're recording from that that has the same
*  effect on the coupling that meaning if you shine light at the top of the neuron and you record
*  from the bottom of the neuron at the same time that you're suppressing higher order thalamus
*  then it's also decoupled and then we found that so we knew from Mary Sherman's work and several
*  others that that the higher order thalamus when it does project to the cortex projects both to the
*  top and to the middle of the cortex and that there's a lot of metapotropic receptor activation
*  involved in about 50% of the work being done by the by the thelamic inputs is through metapotropic
*  receptors and so which nobody really knew how to interpret and we therefore just tried blocking
*  the metapotropic receptors in this case both glutamate and cholinergic receptors and both
*  of blocking either of those receptors had the same effect of decoupling the neuron so information
*  that you were that you're impinging or imposing on the top of the neuron cease to influence the
*  bottom of the neuron and and I suppose the the upshot is that we and I suppose I should also
*  say that these are the neurons or one of most these neurons have a large input to higher order
*  thalamus and and so there's a loop between these neurons the higher order thalamus and back again
*  in controlling the coupling of these neurons and and so if you would break that loop anywhere
*  what's what we would claim now is that it's it's actually taking away cortical cortical feedback
*  because that those things that come to the top of the neuron from other areas of the of the cortex
*  are now have no influence because they get to the top of the neuron but had no influence on the bottom
*  of the neuron from which the axon comes so basically it's a handy switch as I say in the
*  beginning for taking away all in this case ubiquitously across the whole cortex all feedback so once you
*  got to that point then you could posit that that's possibly the mechanism for anesthesia and our next
*  I hope we've got another we've got now got a five-year plan to to see if we can prove that that's
*  true but but on the other hand we're already speculating that if if that is the case then
*  then you could you could speculate that consciousness is in fact the reintegration of feedback via these
*  neurons somehow and in that engages the thalamus-cortical loop or at least I shouldn't say is but but
*  requires and and then and then you can look at the different kinds of claims about what consciousness
*  is in the major theories and I think there is basically well three main genres maybe four main
*  genres I think anil seth who you interviewed recently just had a a review paper on on the
*  different categories of consciousness but one one sort is these the sort of interconnectivity
*  type theories of consciousness like the integrated information theory by Tanoni or the global neuronal
*  workspace theory by Shenzhen and De Henne and these are theories that posit that there's there's
*  long-range interactions going on and and that interconnectivity in some sense is the be all
*  and end all of of consciousness and you get to a certain level of interaction which in Tanoni's
*  IIT theory would be described by a number with phi in in the global neuronal workspace theory would
*  be some threshold ignition point where where you get now let's say an explosion of activity around
*  the the brain in this case I think it's clear that either of those two theories would be well
*  explained if you like the mechanism would be well explained as being a decoupling of the
*  parameter neurons because this would instantly take away either it would instantly lower phi or
*  it would instantly bring you below the ignition point of the global neuronal workspace theory
*  now another class of theory is the higher order theories of consciousness and in these these are
*  if I say content driven in the sense that that is you posit that there's some higher level process
*  going on that is responsible that says exists in in cognitive space somehow that that supervenes
*  if you like on the on the rest of the low-level activity that's going on and and it would I think
*  be easy deposit that that that's exactly what's embodied in feedback that if it's going to be
*  embodied anywhere it's going to be in the in the kind of information that you generate as opposed
*  to the kind of information that you're receiving from from the rest of the world although the I
*  think the in the the interesting claim going on here is that it's neither nor it's it's the in the
*  perception or or what the cortex is actually doing is is comparing your to internally generated
*  information with the external information and it's not until those two things match in the
*  correct way that you have that you have a perception and and I guess that if it claims
*  anything dendritic information theory claims that you perceive nothing when you don't combine these
*  things and if you would decouple them you would stop perception and that would be that would be
*  like being unconscious what happened okay so when when you're unconscious they're decoupled when
*  you're conscious and you have content they're coupled what about when you're in a mindful
*  meditative state I'm not sure or or you could ask when you're dreaming or sure the and and we'd
*  like to know the answer to all of these so it's so I can only speculate at this point and and I
*  guess the the other really close question would be what happens when when you when you take some
*  kind of psychedelic drug and so on right and and another related question would be what happens in
*  in the various kinds of pathologies where where you see cognitive changes and so on I think they
*  all can be you can think that's the in a sense the beauty of looking at the the cortex through
*  these glasses that let's say through the dendritic integration theory glasses you can now say well
*  what will happen if we if we you've got basically two dials you've got the what would you say the
*  receptiveness or the activity state of the top of the neuron and the bottom of the neuron and you
*  can turn it up or down let's say so you've got you've got four degrees of freedom if you like or
*  two knobs that you can turn in both directions and you could imagine for instance that that when
*  you're in a meditative state that you're you're you're you're turning down your receptiveness to
*  the outside world and and turning up your your receptiveness to the inside world that's that
*  you're you're basically vice versa for the opposite right yeah it mindful at least mindful you know I'm
*  not an expert or anything but you you're turning off your internal world and and it's like pure
*  perception right without judgment right right yes yes yes right I guess I at this point I so I
*  don't know the answer particularly and we haven't tested the answer but but but I think that's the
*  nice way of that simplifies the question enormously what might turn out is that when for instance
*  you're doing something like meditation that it might be a particular part of you know you might
*  be switching off your frontal regions and and let's say turning down the top on your frontal
*  regions and putting up the the the bottom on on the center is or who knows but there could be that
*  kind of nuance to the question but but essentially it's still much simpler question all of a sudden
*  and and it seems tractable to me first of all it's tractable because you could describe what
*  you expect really easily and secondly it's tractable because we have the tools to explore
*  this now so with with at least in at least in rodents we can we can now basically answer the
*  question we can use various different tools to to work out what's going on in humans this of course
*  is more difficult because we can't get we can't do the same kinds of sophisticated things like
*  optogenetics and so on in in a human I still feel like this there's a path to to getting to
*  explaining this in humans I think it would start with with doing this in in mostly rodents but
*  perhaps other animals and then looking for non-invasive ways to see the clues of of what
*  in animals and then take these non-invasive approaches to in the human case and we've
*  started this in many different ways and I think it it looks promising to me at this point albeit
*  at the beginning of a long long road to to get there so Matthew this is kind of a pause or
*  orthogonal but we've just been talking about high-level concepts like consciousness and we
*  may go into talk about the ideas about memory and learning in layer one and kind of these big
*  ideas but this all started from recording that nitty-gritty recordings in the dendrites you know
*  of pyramidal neurons so so you know sort of bottom-up right and then you've extrapolated
*  it to the larger ideas so I elicited a few guest questions and I want to make sure that I play them
*  for you they're both by the same person here so I'm gonna play this question for you with that
*  background that I just said and then and then we'll move on to other high-level topics. Hi Matthew
*  this is Mac nice to see Paul getting a few more Australian accents on the podcast the way it
*  should be so one of the things that I really love and admire about your work Matthew is your ability
*  to conduct really precise technical experiments at the micro scale but then extrapolate the
*  importance of those experiments and the outcomes of those experiments to a broader functional
*  interpretation and as someone who typically starts from the other end at the systems level and tries
*  to peer down into the micro circuits I'm curious whether you have any tips or tricks for people
*  working on the macro scale that can make the results of our experiments more palatable and
*  more profound to people like yourself who are working down at the microscopic level and trying
*  to extrapolate out to the macroscopic. It's Mac Shine asking for tips and tricks. Well thanks Mac
*  yeah great question it's it's it's so ironic to get that question because I'm normally thinking
*  about the difficulty I'm having talking to people at max level which I also really admire and trying
*  to convince them that they should care about the low-level features and I guess Mac is is asking
*  the other way around how would he get somebody at the low level like me to be interested in high
*  level actually that seems to be a theme of your podcast going through I love the the interviews
*  you did with John Cracker and various people like this who I think are are starting more or less
*  where where Mac starts and they hate the low level hate it right they hate the level yes right and
*  and and and it's so I'm I'm find myself defending in the other direction in that context but if
*  you do want to get through if you're in if you were a John Cracker of this world and it wanted
*  to to to interest somebody at the low level well I mean I I listen to to his argument and and I'm
*  totally convinced that you you definitely need to imagine what the purpose of all of this is but but
*  I know that a lot of a lot of people get lost in in the world in fact I'm probably in one of those
*  fields where when we get together in in our conferences you know conferences that are
*  specifically about dendrites tend to focus on such minutiae that you if you were a observer to such
*  a conference you would wonder why anybody would be worried in this that or the other and it gets
*  down to all sorts of details that are hard to to know if they should matter at all and I think
*  it's also true that a significant fraction of the people really don't care about whether or not it
*  matters at these these higher levels I guess that I feel intrinsically if if it wouldn't matter at
*  the high levels I wouldn't care about it at the at the low level so I'm not interested in just the
*  properties of dendrites for their own sake if it doesn't matter at the high level then I don't think
*  so but what I guess I'm arguing is that and this was in an opinion piece that came out recently I'm
*  arguing that as much as it's it's important to ask the question what is the what are the consequences
*  if you like at the high level I think it's it's instructive the the low level is in fact instructive
*  of the kinds of it gives you a framework or a parameter to to guess what's going on at the high
*  level so for instance when when we look at the the the question where we recently looked at memory
*  for instance and we've for me a light came on when I saw that the memory structures tend to go to
*  layer one of the cortexes they one way or another they feed back information if bit the hippocampus
*  of the medial temporal loop lobe or the or they say the basal ganglia through higher order
*  salamic regions or the amygdala just going directly to to to layer one of the cortex that for me that
*  I I immediately said to myself well there must be a reason for that and of course with the with the
*  kind of goggles that I have on and looking at this in terms of the the cortical column and that's what
*  the parameter neurons are doing for that I'm asking more that I'm saying to myself that must
*  be influencing the top of the pyramidal neuron and why would this be true and so on out of that
*  pops the hypothesis that drove a whole you know five years of research which is maybe the top
*  layer of the cortex is is cares about memory if you like or needs to get signals that things
*  need to be remembered and if so it would imply that the thing that you want to remember is
*  context which actually the more you think about it makes perfect sense in fact when I was saying
*  this to a psychologist the psychologist said we already knew that you know that yes you you remember
*  context that's to say if I if I tell you my phone number you don't remember particularly you don't
*  want to perceive the number six any different afterwards if you have a sixth column or I don't
*  know you you want to associate it with me and and and probably a telephone number is the worst example
*  but in any case the the if you want to remember something you want to remember the the features
*  of something and how they what they relate to you're now in my tiger context because of the
*  examples that you use right so right exactly yes and and so so how would I get the high level
*  person to to interest the low-level person I would say that this has to manifest whatever your high
*  level claim is has to manifest at the low level and if you're if your low level is is if you're
*  steadfastly going to ignore any possibility for this connection then then you will you will
*  constantly be in your own bubble as it were which I think actually a lot of neuroscience is and it's
*  also I think there are a lot of exceptions and a lot of them are you tend to I think collect that
*  kind of a mindset for your podcast so I mean I can think of notable exceptions of people who
*  who really don't stay in their bubble see people like Buzhaki for instance who who doesn't want to
*  be trapped in that bubble but amongst I think being in where I come from at the level we we
*  look at the brain I'm very used to that milieu where where where it seems really important to
*  talk about you know what what subtype of what channel is in which which oblique dendrite and
*  so on which which makes the the ilk that you were just describing makes their eyes roll right but
*  let me let me read something you mentioned the review that you wrote and it's our dendrites
*  conceptually useful where you make these kinds of arguments so I'll just read a quick quote from
*  that because it has to do with what we're talking about there's every reason to suspect that better
*  descriptions of sophisticated single-cell computation will lead to better descriptions
*  at the network level blurring the distinction between Mars algorithmic and implementation
*  levels so people you mentioned John crack our he's one example right who don't care about the single
*  neuron level let alone dendrites right that's even worse and but because the argument is we
*  have to stop looking at how these neurons are connected as a like box-and-arrow kinds
*  of diagrams because they're not telling us anything about the higher level cognitive
*  functions essentially are you fighting an uphill battle in this current not amongst your low level
*  dendrite friends low-level friends but just in the neuroscience world at large do you have you have
*  you found yourself fighting an uphill battle as a sort of bottom-up experimentalist yes I think
*  the it's always very difficult to to take somebody who hasn't considered these problems and even get
*  them to pay attention let alone let alone take it seriously and I guess the claim I'm making the
*  quote that you just read is that it's not just the claim that there has to be a through line from
*  from the implementation to to the algorithm to the computation but but that the the implementation
*  is very suggestive of what types of algorithms and eventually what types of computations are
*  being carried out and and that sounds like an unreasonable claim I'm sure to the John
*  crack house of this world that that doesn't seem plausible but but I think that what we've just
*  been going over is the case in point I think there are things that we're suggesting such as
*  for instance perhaps the the top of the cortex is the place where you should look for semantic
*  memory that you can only come to by a synthesis of the of this bottom-up approach with a with an
*  eye to the top down types of questions and in the end it I think is really instructive to somebody
*  is from a sucker psychological point of view and somebody who wants to understand it's a
*  computation level in mass mass terminology right but but in in terms of getting back to looking
*  looking at high-level features of cognitive features of the way the brain operates it not
*  only I think suggests how it operates but why it operates that way it makes a lot of sense I think
*  that if you want to remember the way things are associated or the context for things then you
*  would like to separate that you'd be really useful if you could separate that as a compartment to
*  handle it separately and then in reintegrate it into the larger cognitive domain and and hey
*  presto that's what that's what the low level is telling you is happening and all of a sudden it's
*  giving you clues about how you should talk about the at the high level about what's going on and
*  and it also tells you why this is semantic information by the way this is essentially
*  semantic which is a really difficult notion you know meaning or you know how how do we describe
*  this in the end it tells you if this is the right way to look at it then semantic means nothing
*  other than then the distillation of context and and so if you can distill the context of something
*  then you know the meaning of it and and and yes that's a bold thing to claim but I'm claiming it
*  on the on the basis of the low-level description and I'm saying that that it appears that way from
*  the low-level description so let's let's let's posit it as a hypothesis at the high level well
*  so I guess a pro computation level perspective would say that's fine but you didn't start with
*  dendrites you actually had memory in mind a high-level concept right a computation in mind
*  to then make a hypothesis about what the dendrites might be doing so to me it seems silly to say we
*  need to go this way or that way because we're we're all working at all levels it's essentially
*  not well not me since I'm retired but I couldn't agree more I couldn't agree more that's exactly
*  right that that we should this should not be a fight between which which direction to think
*  of things this should be a call to arms for people at all levels to to start talking to
*  each other and to see how this all fits together and I think that's that's what I admire a lot in
*  Max Shines work because he's doing that and they're very very few people who who do that
*  and a lot of people who resisting it since I mentioned that paper and read a quote are
*  dendrites conceptually useful how's it been received have you gotten feedback positive or
*  and or negative did it do its job it's too early to say now Tony it's only a few weeks since came
*  out I've not had any any really negative feedback but maybe it's maybe it's still arriving in the
*  I do kind of feel I'm a little bit conflicted by this paper because it's a little bit polemic
*  at least for what I'm used to saying I'm using a little bit more tentative about saying but what
*  it's it's trying to say essentially that there that there may be things that we've yet to
*  understand about the way the brain operates that can only be approached if we would if we would
*  include some of the the possibilities that we could learn from dendrites and the analogy I have
*  actually which is in this paper I look at the way I contrast the revolution in neural nets with with
*  a normal digital computer and I think it's fair to say that that neural networks are conceptually
*  in advance for neuroscience no matter whether you think they're the be all and end all but
*  certainly deep neural networks are doing a lot of work at the moment in terms of our understanding
*  of how neural of how networks might work and I think this is on a conceptual level and I think
*  it's on a conceptual level in the sense that we run these these artificial neural networks
*  on digital computers which are nothing other than Turing machines so so you could because maybe I
*  should add that the often the the throwback that you get as a dendritic researcher as well you know
*  that it's not really necessary to consider these dendrites as if or neural networks because we can
*  always build a more complex neural network that includes all the properties of your dendrites and
*  and so it's not relevant is it and and we'll be able to solve everything with point neurons because
*  if we needed something that the dendrites do without a few new point neurons you know points
*  yes yes right and and I'm a I'm just saying well you could have said that about neural networks
*  in the first place you could have said look I don't need a neural network to to solve this because
*  all I need is a few more states and a longer and a longer ticker tape to have to have more numbers
*  on it see it's it's just a Turing machine after all and I can prove it because I can run it on
*  this digital computer and and you'd you'd you'd in that instant lost all of the power of having
*  collapsed what I think is the real inside of a neural network is that you can do this fantastic
*  statistical learning with basically three three facts if you if you have a learning rule and you
*  you know the the cost function of this and and and you have basically a particular architecture
*  of you know you've figured out your your connectivity that with those armed with those facts you can and
*  and a method for for communicating the deep deviation from from the goal that you want to
*  to the to all of the connections you're done and and you you can you can do you can beat the world's
*  best chess player with these three principles essentially with a few tweaks and so obviously
*  I think that's a conceptual advance and it doesn't it's no for me I it's absolutely not an argument
*  against this that you can run it on a digital computer I'm saying so so what you know that
*  it's conceptual about so the argument would be we haven't spent enough time looking at the the
*  kinds of insights you might have over and above these these these things we now know about this
*  this framework of looking at learning within your network we haven't looked at end rights
*  closely enough to know whether or not there are more principles on those levels and and the first
*  principle I would go for actually is the the separation and reintegration of two different
*  fundamental streams of categorically different streams of information and and mess around with
*  those kinds of principles but I'm not claiming that that is the be all and end all I'm just
*  that that seems useful intuitive to me at the moment and and you'd want to be really sure before
*  you just threw away what biology has spent hundreds of millions of years playing around
*  with and and and just say well that's irrelevant I think I'll stick with point neurons that seems
*  to me to be an incredibly stupid thing to do okay I like that you said stupid I recently had Elena
*  Galea on talking about astrocytes you know for example right yes thinking about things that are
*  not neurons in the brain and of course there are neuromodulators and I've had people on to
*  discuss those but it's it just seems the more I think about it the more I learn about some of
*  the lower level things that were carved through evolution the sillier it seems that the deep
*  learning world is based on these point neurons right that are essentially from the 50s 40s and
*  you know earlier is by by looking at the the brain and deciding that neurons from single
*  neuron doctrine etc were the end all that's where artificial intelligence or the modern version of
*  it the birth of deep learning etc that's where it all started and it just seems silly that it's
*  so archaic based on the technology that we had on at the time and our experimental capabilities
*  based on those technologies so I'm with you that it seems useful to at least try out what
*  evolution has suggested to us right and so so I guess I want to just reiterate the claim that
*  I'm making it's not that I imagine in the end that you're going to need a sophisticated real
*  description of dendrites and and that unless you had a really complex machine with dendrites you
*  wouldn't get the full functioning brain I'm claiming that there are insights that you can
*  get from dendrites and until you understood what they're really doing then you then you'll miss
*  these insights in the same way that if all you had was a state finite state machine and a ticker
*  tape you're probably never going to stumble across the idea of a neural network the that that you're
*  probably if you only have a neural networks with point neurons you're probably not going to stumble
*  across some of the insights that you can see with these higher concepts whatever they may be and I
*  guess to the John Crackers of this world I would say you know just that that's an example of let's
*  say going I didn't that's where I'm trying to say we may be confusing implementation with algorithmic
*  I'm not quite sure how I would describe the the point neural network in terms of where it fits on
*  the Mars level of description but but I think it's clear that it blurs that district description
*  because you can you can get from a neural network now to beating a chess player and and and all the
*  other face recognition and God knows what and we'll come around the corner next that that there are
*  insights that we're getting from that that are crossing these boundaries as my would put them
*  they're not so simple to to see the line between between what in fact in a way this is perhaps more
*  the problem that we're facing because when you sit down and you know when you want to beat the
*  world's best chess player and you want to improve your network now comes the rub actually because
*  it's it you can you could train it on on a hundred million chess games and it's going to be fantastic
*  but if you want to improve it past that you suddenly realize you don't understand how this
*  neural network in front of you is solving the problem or at least in the sense that you you
*  don't understand in the sense that you don't know how to tweak it to improve it past past giving it
*  more information and and training it more but I think that's where that's where dendrites are
*  likely to come in and be useful because clearly the what I think this is a this is a hypothesis
*  or a wild claim you feel like that the the neural networks point neural networks deep neural networks
*  are autistic savants these are machines that can collect information and synthesize that close to
*  perfectly such that you get close to the best statistical description of the of the input output
*  function that you're seeking and in that sense you can't do better and and what you're missing
*  is context what you're missing is a way to when we're talking about sort of general AI that that
*  that you're missing insights in a in a directed way that that allows you to do what what is
*  difficult for autistic savants to put some meaning to it also you might be able to count
*  how many matchsticks fell on the floor but you've no idea what you're going to do with this
*  information and and you can't you can't put it in other contexts that you haven't been trained to
*  to do and so on and what we clearly can do with with one or two presentations of the data humans
*  in particular but I think mammals in general can generalize from situations and and make
*  conclusions that are startling with comparison so the and and at the moment we are all super
*  impressed by something that is that as we would be I think if you if you if you meet a an autistic
*  savant then you're also super impressed by what they can do and I think your first impression is
*  I wish I could do that but I think I think it comes at a cost and I think the the low level
*  implementation is telling you why it comes at a cost it's because if you've got if you're let's
*  say that you could train this whole network in a feed-forward sense by just using the bottom of
*  every neuron and and now you would be putatively perfect in or at least as good as possible in
*  framing problems and but if you want to have context it comes to the other end of the neuron
*  and and is reintegrated into the neuron there's only one output from the neuron so essentially
*  the the the top-down signal is adulterating your perfect statistical calculation and you can't
*  have it both you can't be perfect in your statistical analysis of something and have
*  your context at the same time and and so you're going to have to put up with that and my claim
*  would be that from an evolutionary point of view you want to be something like the the
*  six-layer cortex and and a mammal that is imperfect because from an evolutionary point of view every
*  now and again you're going to come across life-threatening situations where you're going
*  to have to think laterally and use all your knowledge to avoid it and I think we come across
*  them actually not just every now and again but all the time particularly say you're driving a car
*  and and today somebody dropped their hat in the road or or there's some strange obstacle in front
*  of you and the and let's say the an automatically driving car would just say well that's the first
*  time I've seen that I'll add that to my database and run over the little kid or whatever it is
*  and and you say you say no this is strange I I don't not seen this before and I don't know how
*  to handle it but I can see that something's different and I know I can work out all of a
*  sudden that all of these other things pertain to the problem and and although you've not seen it
*  before you can you can deal with that I should have framed this in terms of the driver dying
*  there's you could easily frame this in terms of and and and children you're talking about children
*  dying nice sorry about that but my main point is that you would be coming across situations
*  throughout life where if you didn't have this kind of ability to think on your feet and interpret
*  and and let's suppose this pose I told you that that this autonomous vehicle was so good that in
*  ten years of driving it'll be a hundred times better than you are at driving the car but once
*  in ten years it'll drive into a truck you know you don't get into that car because this this is a
*  your day you're gonna die in the next ten years and you don't want to die in the next ten years
*  you want to survive it even if that means making hundreds of little errors that you're that that
*  are not not optimal you would prefer to be ready for the for the divergence that is hard to predict
*  and and and you can't learn statistically so that's what I'm guessing is the reason why you need
*  this kind of general intelligence in from an evolutionary point of view I had the thought and
*  you can tell me why this is a ridiculous thought but you know thinking about our mammalian cortex
*  and well our human cortex relative to other mammals it is thicker and these you know their
*  descriptions of these layer five pyramidal neurons for example have longer apical dendrites
*  they're more decoupled essentially and I was trying to think well you know under your like
*  the dendrite hypothesis why would that be and I actually thought maybe one evolutionary advantage
*  and sorry you know you talking about the savant made me think about of this is to actually prevent
*  us from well it you said it for me from like being a savant it's actually to prevent us from
*  learning too well so that we have the capacity in those situations over a mouse let's say or in
*  this case a savant I guess I'm just repeating what you said but I thought of it in in terms of
*  reducing what we're learning in given situations even though we have a much higher to allow us to
*  have a higher capacity to learn when we need to learn does that make sense yeah I really liked
*  that I hadn't actually thought of them that's really nice so I in other words the thickness
*  of the human cortex would have a tendency to be be able to be savant like in because it's more
*  decoupled is what you're saying well the thickness would would prevent savantness right it would
*  because you wouldn't just learn everything without the imperfection without the feedback
*  right the the feedback in some sense is gating your ability to become a savant is what you actually
*  you said but now I'm just you know it was yes that's right it's what but but but but but the
*  reason I extrapolated to that from what you said was that the the thing and actually the first
*  findings in vitro from human neurons is that they're less coupled than than the rodent neurons and
*  and they would seem counterintuitive at first and that's what I'm saying is like to prevent the
*  learning essentially right and and but then but then you would need some way for to reintegrate
*  that so and and and I think that I'm betting that the latest thing that we saw under anesthesia is
*  giving us the answer here that that essentially different kinds of neuromodulation affects the
*  coupling and I'm betting that if you took a human neuron with you know in a situation that's that's
*  more sophisticated than the in vitro situation where there's no neuromodulation that you've got
*  all sorts of ways to reintegrate the tuft and as you say now you could be doing learning with and
*  without it and and I suppose that that I guess where I was going with saying that also first
*  time I do rise you weren't safe now so we can we can own this idea together that that you would
*  also in principle have the advantage of being able to decouple it under certain situations so if you
*  did want to just if you just wanted the statistical part of this if you just wanted to let's say ram a
*  lot of information in and you could in principle I don't know exactly whether it happens or how you
*  would do it but in principle if you've got a mechanism to to decouple the top from the bottom
*  and you were under control of that you could for for whatever time it takes decouple it and maybe
*  that is what it means to really focus on throwing a football or something that's what Ritalin does
*  or something yeah right exactly and then then you then you could putatively work up the the
*  statistical information and then and then reintegrate the the context I guess that the way we had
*  thought that this happens is is in two stages but it's it's just a at this point we were I guess so
*  this is this is really speculative but but one way you could imagine is what the critical period
*  is during the the development of a mammal right is a period where you are decoupled by the way the
*  at least in a rodent during the the days between so when you're born up until just after weaning
*  that's a few weeks so three or four weeks you don't have a calcium spike and you don't have you don't
*  have this apical non-linearity and then it starts to kick in at around about four weeks and and then
*  up to about eight to twelve weeks it's really fully developing and then you have really large
*  plateau potentials but so you could have and that corresponds to an early phase where there's a
*  critical window where where you're learning just the the features of your environment the statistical
*  regularities right and and then you basically shut down the top of the of the neurons while you
*  learn the statistical regularities now you've got the the features in place in your cortex and you're
*  grounded in the world and all your all your columns are grounded and now you can start putting them
*  together associating to each other and I guess that I was positing that that's when the the critical
*  window ends and you stop being so good at learning statistical and that would explain for instance
*  why it's difficult to learn a new accent or instrument you know a past yes or instrument if
*  you haven't got those there's that grounding with the world up to that point that gets slowed down
*  deliberately because now you don't want to be bothered with with that but but as I say why not
*  why not have maybe you need Ritalin and and and you prevent feedback or something you could in any
*  case you could imagine that that again this is a this is a handy conceptual tool for trying to
*  understand the link between the implementation and these large-scale concepts of in this case
*  learning statistical information versus contextual information so whichever way you look at I think
*  it's I sort of might be wrong but if it's wrong at least you've got a framework for for talking
*  about it and and testing it and and for me that's that's worth something that gives you a a way to
*  treat this what otherwise seems like an intractable mess of possibilities so so I've heard you in your
*  talks and this is going back to artificial neural networks now talk about how we don't need to model
*  dendrites and you've just been talking about that as well we don't you know we don't need to model
*  all the exact details of dendrites to create a useful artificial intelligence for instance
*  that instead we can extract the correct principles that the dendrites just like we've been talking
*  about how much detail do you need to build in it are there are there lower level things that you
*  think are dendrites the lowest level that we need to consider or are there principles that we can
*  extract looking at lower level things like I don't know channels right ion channels it's or whatever
*  I don't want to plant a seed in your head but are dendrites the bottom level I don't know the answer
*  and and I mean when we when we're talking specifically about dendrites there's there's
*  levels also in dendrites right you could be talking about spine heads or or little branches
*  or or or whole arborization so that's on it and it's this is a well-known thing actually
*  I don't know if you've talked with Mike Hoyser before but but he he and Bartlett Mayall have a
*  a really good paper it's now about two decades old asking exactly this question whether or not
*  what your what level is is appropriate and it wasn't clear then I don't think it's clear now and
*  and I mean I've got my favorite intuitions but I don't think you're asking that I think
*  the larger question is how would you know and what's the principle for for deriving this and
*  you have to take a walk with your wife and it has to come to you in a flash
*  exactly no well yes actually if there's one principle to come out of that you need
*  a really naive person to to say well wait a minute and and not to stop asking you
*  to keep on coming back to something you thought was obvious and and and keep on having to explain
*  why why you think it's obvious and and actually my experience is trying to explain to somebody a
*  really a really persistent naive person why something is obvious so marry a naive person
*  is what you're saying something like that but but actually I think in the end that that's why
*  I think teaching is actually really useful to students because often they're asking you
*  naive questions and and then you find yourself actually I don't really know the answer I thought
*  I knew the answer to that but actually and and very often you realize that even the student
*  doesn't realize what they're asking it's not it's not necessary that the naive person gets the has
*  the insight that you're having in that moment for you to suddenly realize that you don't really
*  understand that and and I wouldn't claim that anything that I've said now is categorically
*  true it seems what the good thing the good news I think is that if you start with this mindset that
*  there's something to be learned from from let's say bottom up descriptions that then you can always
*  test it well you can mostly test it you've always got a at least a conceptual way to test something
*  and and that's that's worth gold dust I think in a you know in a scientific context because if
*  you're starting from the really high level ones you may or may not be able to test a high level
*  theory particularly if it's very if you are on the wrong track then it's going to be very difficult
*  to get any proof at all that that that it'd be hard to to get in there and and and actually test
*  it from but so that I think that's that's worth a lot but the the bad news is that it's it's hard
*  to stumble across the high level concepts that way and so that's why I think you were right before
*  everyone should be talking to each other and and we shouldn't be doing one or the other
*  okay Matthew speaking of naivete and relying on our assumptions and questioning our assumptions
*  let's get to the action potential and consciousness thought experiment piece do action
*  potentials cause consciousness this really challenges our assumptions about what's important and
*  um and the primacy again of action potentials and I guess somatocentric
*  thinking in in a sense would you like to explain the the thought experiment and maybe high level
*  and then I also then I have a question from Maxine and then we can discuss more just before I the
*  caveat on on on the description of this is that the um that you hate neurons you hate cell bodies
*  and actual potentials well first of all first of all the the the question as stated as you put it
*  is supposed to be provocative yes um and and so to be even more provocative I think I would say
*  um does brain activity cause consciousness and and I I guess I would be I would be hoping that
*  my interlocutor like you would be uh would be would have the spontaneous response of course
*  so that's what in a sense that thank you that that that's where the starting point should be
*  but because then we the thought experiment starts and I and I should first of all um say that this
*  was put forward in in our philosophy club in our lab by a really fabulous um uh now senior postdoc
*  Albert Gidham um who proposed this one day and and it sounded so similar to what I'd heard in
*  other kinds of contexts um that at first I thought that it wasn't new but there's
*  there's something really important about it and more recently I found that there are a few other
*  people who've who've either said similar things or the same things even um but here it is the so
*  imagine that you first of all you you take a subject who and you you give them some experience
*  so I think it's easy to do this with let's say a movie so you get them to watch five minutes of
*  movie um and while they do this you use some modern technology um where you record from every
*  neuron in the brain so future technology some future technology right um what we'd like to if
*  you go to some conferences what you'd like to believe we're closing in on right probably we're
*  still a long long away from um in any case so you record from every door so you know how every
*  neuron fired during the movie at every instant and and you can just for the sake of this thought
*  experiment record from retinal neurons and and also any any neurons in your spinal cord and so on
*  so that you know the whole deal um but but in principle we're talking about what you were
*  thinking when when you saw the movie and and the experience you had when you saw the movie um
*  okay and now you imagine that you had a device to to replay that uh that to the to the person
*  and actually although this to some people this sounds really really futuristic and that's not
*  futuristic it's futuristic is the number of neurons you can do at the same time right but
*  but getting one neuron to repeat the exact activity in the form of action potentials is not
*  even hard that all you need is a really good amplifier and and a good recording of the initial
*  conditions and you can you can do what's called dynamic clamp on the neuron and and literally
*  create the same voltage at that point where the neuron is which is unfortunately as i say
*  typically the cell body but nevertheless um you can make the cell body do exactly what it did before
*  and since that is actually a nexus point because most of the dendrites are feeding into that point
*  and that's just before the axon that's going to have a pretty uh that's going to really dictate
*  what the output along the axon is of that neuron if you can absolutely recreate and not only that
*  but uh if you do a dynamic clamp in a continuous way over over the whole period of this movie
*  it won't just dictate what that what that cell body should do uh when it when it fires an action
*  potential but every other part so every sub-threshold deviation from that as well so in
*  other words the the cumulative effect of all the inputs as seen at the cell body you can recreate
*  with this with this um so-called dynamic clamp and now okay it's futuristic but let's say you now do
*  this at every neuron in the brain the question is if having just seen a movie and somebody recorded
*  all your action potentials if they replayed all the action potentials very faithfully at every
*  neuron in your brain would you have the experience of seeing the movie again and and do you ever do
*  you well can i challenge you with that well because i've kind of vacillated so um i want to say sort
*  of because i don't it's not a to me it's there are questions right because well i've ended up on no
*  but i but i think that it's because uh i've come to think of let's say our subjective experience
*  as not being due solely to spiking activity um so i was already kind of a no on this but i i
*  definitely used to would have said yes uh okay very pro spiking okay let's just take your used to
*  persona because there's a couple more steps um so so if you would say yes of course i wait wait
*  what would you say i would say what you just said actually i'm i'm i'm agnostic and i think i would
*  jump off the train at the very first step okay and say no but um but i'm very conflicted i don't
*  know the answer so and it's it's for me this is torturous but um but the next that i think a lot
*  of people would say of course you know penfield used to stimulate the brain and you had experiences
*  so if you made the neurons fire you just had the experience that that gives you um and really
*  important to this thought experiment is that although we so we're not controlling everything
*  else that's going on including the glial cells and the and the neurotransmitter and and so on
*  and so forth but we're not we're not interfering with it either so there's no reason to not to
*  posit that when the action potential goes down the axon it won't lead to the same release of
*  transmitter and so on at the other end of course that's a stochastic thing and maybe that's important
*  and so on yeah that's homeostasis and all sorts of things yeah but but but on the other hand if
*  let's suppose homeostasis was coming in you're you're in every subsequent instant in this you're
*  also making the neurons do what they're going to do so so you're never going to know what homeostatic
*  changes actually occurred to i meant in the astrocytes and glial and all the other parts
*  of the brain right and uh yeah right right okay i i i can see that um if if you wanted you could
*  you could extrapolate this this uh thought experiment to clamping everything but that
*  this seems too unnatural for the timing so so let's let's just let's step through yeah again and then
*  because i need to play this before we you answer it already okay all right so so the next step is
*  um what would happen if you now um blocked all the uh sodium channels so you blocked all the
*  all the chats for the action potentials to propagate down axons but nevertheless you make
*  every neuron fire the way it was doing so if you got to this point i think you should be saying
*  something like well it didn't matter before whether or not the action potential influenced
*  the next neuron because my electrode is telling the next neuron what to do not not the action
*  potential from the previous neurons so in principle those connections are now the the action potentials
*  are going down the axons are irrelevant because what makes an action potential is no longer
*  the the influence from the so so then you but but nevertheless you would ask you know
*  would would that cause you to be unconscious and and then the next step would be blocking
*  neurotransmitter and so you could put in let's say drugs that blocked the receptors or we did it in a
*  sophisticated way for for um in the thought experiment with the optogenetics and so on just
*  so that you could get around some of the believable the tricky problems yeah well it's
*  not so much as believable actually it's it's it gets a little bit more fantastic that way but but
*  i think it it avoided some of the obvious um the obvious complaints somebody might have on a on a
*  philosophical level let's say um could do it more cleanly let's say than just cut out um just
*  transmission um and and then the next step in the argument is what if you take each of the neurons
*  or first of all what if you make an incision in the brain and you cut one part of the brain
*  from another but you're still clamping every neuron so essentially the information is getting
*  around the brain in the sense that you're you're imposing it just like it would have happened
*  in the original brain but they're physically not connected anymore but they weren't connected
*  anyway um with due to your blocking of neurotransmission so why should that matter
*  and then the last step is to is to take the every neuron in the in the brain to a petri dish
*  spread it around the world have different neuros researchers in their different laboratories
*  replay at their neuron what they had to do and and then some set of neurons that used to be your
*  brain does exactly what it did before and i think by most most people at this point are starting to
*  object they can't imagine that would be conscious not panpsychists though probably right right
*  and and so so if and then you ask yourself well if if you decided that at some point in this set of
*  steps you went from being conscious to unconscious you have to say where and why and uh so that's
*  where we get to and then that's very challenging i think because now you have to you have to be
*  you have to have a i think a more first of all you have to have some better reason for for explanation
*  or what let's say imagination for what what would make you conscious but also and and this is where
*  i think it's an important thought experiment is that whereas say the chinese room does something
*  like this and and various other ways of looking at what computation does and and different ways
*  to simulate what the brain does are good thought experiments very often and actually john seoul the
*  the originator of the chinese argument i think does this when challenged he says well i know
*  i'm conscious so there must be something about wetware that makes you conscious
*  and and it's it's like the last retreat i don't know why i'm conscious but i know that i am
*  conscious and i know that i'm i'm a set of neurons so it must be something special about a set of
*  neurons and and and basically this is saying that's you can't escape because it's still your neurons
*  doing this in fact in the in the sort of in the most idealistic way of stating this you're in the
*  first step when you replay all this activity you can posit that all your neurons did exactly what
*  they did before and and that there's that and and if you want to say well there's no they didn't
*  there's there's this there or this there you have to now say why that should be the seat of
*  consciousness so so i think i'm just saying that you can no longer retreat to saying well
*  there's something special about the way you framed this and and actually but i still i still retreat
*  to yes brain activity causes consciousness um right because you're being asked why does brain
*  activity cause consciousness that's the that's what i was going to say is that the frustrating
*  part of this because i feel comfortable i guess like you jumping off at the beginning but then i
*  cannot articulate why right so which is the important part what else then why would it be
*  it's an etc right okay i'm going to play this question from mac and i'm not sure
*  whether you want to answer or or what you'll think of it so uh all right here i'll play it
*  hi matthew this is mac you uh albert and jan recently had a quite thought-provoking thought
*  experiment and in the spirit of um playfully manipulating thought experiments i wonder if you
*  have thought about some of the other aspects of this sort of experiment and i was imagining a
*  situation as someone who doesn't do a lot of cellular neuroscience myself that some of the
*  patch clamping could go awry and i started wondering just how much of that patch clamping
*  could become impaired or could be inaccurate for an individual to have that same conscious experience
*  in other words how robust do you think our conscious awareness of an individual moment
*  is to individual variation in the firing or the activity patterns the calcium dynamics
*  of the cells distributed around our brain okay oh thanks mac i love that question um and i think
*  you were you i don't know if you were being triggered by that but that that was sort of what
*  you were just alluding to before i think that that the action potential that causes release is is a
*  very stochastic process and and so that's one one form of things you're not under control of
*  in this thought experiment um and but i think i like the question because it's framing something
*  in a way that i've been sort of playing around with i love to listen to dan denet and his
*  his kind of theories of of consciousness that by and large i i find myself agreeing with him in
*  a sort of matter of fact way but he also talks about free will and that's another thing that
*  i'd never linked free will and consciousness in particular before but but i start to see that
*  there's there's some link between these two topics and you know that there's this famous famously
*  there are lots of neuroscientists who think free will doesn't exist but nevertheless you're
*  conscious and and and i i one thing in particular that struck me about
*  something dan denet talks about and i think he's actually talking i forget the originator is it
*  john astin or somebody else was talking about it's it's the put example where where a putter comes
*  to the green he's with his with his colleague he puts tries to putt the ball into the hole
*  he says damn i could have got that when he misses the putt and and then there's this big
*  philosophical article about what do you mean by you could have got that and do you mean that every
*  if every particle in the unit was exactly like it was before that this you could have got it on one
*  re one reversal of time and not on the next reversal of time which is effectively the same
*  as saying can you break the causal chain of the universe and and and if you can't then maybe you're
*  not you don't have free will and and i think the same thing could apply to that's one way of framing
*  what consciousness is about that essentially that and and it comes back i think to maybe to the
*  dendrite theory because essentially what one way of framing what's going on with the architecture
*  the cortex is that in order to have any perception you don't just receive information from the outside
*  world in fact almost to a large approximation it's the other way around you you make a guess
*  about what the outside world is is telling you and you compare this to what the outside world
*  actually tells you and and and it's in that interaction that you have perception that you
*  you have a sensation let's say and given that the the neurons that are going to eventually
*  come well to represent this also project all the way down through your sensory space they also go
*  all the way in some cases all the way back to your sensory organs certainly in hearing for instance
*  you you're actually using your cortex to in some way to modify the outer hair cells and the game
*  of your ears and so on and and you're affecting the input and so on so so you could imagine that
*  that sensation that you're having of of hearing and why it's different to vision is exactly because
*  of the the question that you pose to the distal parts of your dendrites where you say
*  uh is this the case do i get what i expect in this situation and if you're expecting something
*  auditory you you actually not only have to expect an auditory type of sensation or or effect in the
*  feed-forward direction but you have to the your your expectation will become output that will
*  interfere with the whole loop of information coming from from your ears and so on so you could
*  that's a first-pass way to explain why this view of the cortex is encompasses why seeing red is
*  different to hearing hearing the middle c on the piano say and now getting back to the the
*  variability of course this has to be for you to to perceive in this framework it has to be that
*  there's some that there's some way that you could be wrong let's say that that that or that it's in
*  the deviation from what you expect that you you actually make the the important perception
*  that that the extent to which this is is or isn't what you expected is the extent to which
*  you assess what you perceive and the extent to which in the end you have the experience
*  so the experience is all in the the the noise if you like in this sense not in the noise so much as
*  in stochasticity but in the noise as in the deviation from from expectation and and so that
*  would be a way i don't feel confident enough to claim that i'm not a philosopher so i suppose i
*  should farm that one out to people who have more experience than i am but but i i say this but
*  two reasons one being the the the distort experiment and and the other this framework
*  that anyway the goggles that i have for seeing the the cortex that that's that's maybe an escape
*  route that that you can frame all conscious experience in terms of this interface which
*  might actually be at a you know sort of meta space let's say not not not in the nuts and
*  bolts of what action potentials fired and so on but but in the if if there's if this
*  higher order what should i call it if this um yeah okay i said higher order um question that
*  you're asking of of an ensemble of of columns around the brain has meaning it has meaning
*  because first of all you're grounded in the world and there's the you're asking questions of grounded
*  grounded columns and second of all because it can be that it's it doesn't have to be
*  the case and you're you're asking this question and so in a world where everything is just a repeat
*  you will never see any deviation or never have any so everything will will be your simulation
*  and and therefore it won't be an experience anymore and if it's not experienced you won't
*  be conscious of it so that that's the that's fantastic but maybe i kind of feel like a
*  philosopher will catch me out somewhere in that loop but but um it feels i guess i'm positing it
*  i get to so this is this actually is a nice way to close the loop because you're asking you know
*  why would you how do i convince the john crack i was to see from the bottom up i'm saying that
*  i'm asking a really now high level question probably one that's probably more high level
*  that he wants to to go for and but i'm nevertheless looking at the the implementation that i see
*  and asking well is it at least plausible at the implementation level given the this broader
*  perspective of why the implementation is the way it is and i at least get i at least get a loop
*  that's closable um i i agree that one needs to look at this closer but but if if i'm yeah so a
*  that's i say i came to this with some inspiration from the implementation level and b i claim that
*  if if ever i'm on the right track i've got some things to test here that that that is that is
*  also from my point of view this is an important statement to be able to make that this isn't just
*  so i might well be wrong but at least i've got the the way to check it or at least theoretical
*  ways to check it there's the conceptual ways to check it that's it let's hope that we get the
*  the appropriate devices going forward soon well matthew it's it's time for us to close our loop
*  and i still this is a long episode and i still had plenty of things to ask you but i i appreciate
*  you letting me put your goggles on for a little while and i've really enjoyed reading all your
*  works and continued success i know you have a ton of experiments left ahead of you a lot of
*  ideas to test and it's in some sense only the beginning right yes yes i guess it's never ending
*  never i mean it's such such fun that that's probably a good thing not a bad thing right so
*  we're looking forward to the next five years oh yeah you have your five-year plan
*  all right thank you matthew no thank you it's been great
*  right
*  brain inspired is a production of me and you i don't do advertisements you can support the
*  show through patreon for a trifling amount and get access to the full versions of all the episodes
*  plus bonus episodes that focus more on the cultural side but still have science
*  go to brain inspired dot co and find the red patreon button there to get in touch with me
*  email paul at brandinspired.co. The music you hear is by The New Year. Find them at
*  thenewyear.net. Thank you for your support. See you next time.

---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4525s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 4509
Video Rating: None
---

# BI 054 Kanaka Rajan: How Do We Switch Behaviors?
**Brain Inspired:** [November 27, 2019](https://www.youtube.com/watch?v=uxwfvhJUr_g)
*  So I think now we're at the sort of second revolution in neuroscience, but theories are
*  not experiencing the same revolution yet.
*  We need fundamentally new models of the brain that capture not just within region interactions,
*  ignoring everything else, but treating each region as only a small bit of the vast ensemble
*  of what it sits in.
*  This is Brain Inspired.
*  Is the brain one big recurrent neural net?
*  Yeah, sure.
*  Is it a bunch of interacting recurrent neural networks or RNNs?
*  Yeah, yeah, you bet.
*  How, when needed, do we switch from using some set of those RNNs to some other set?
*  Ah, alright, I'm stuck.
*  Actually, we're stuck, since none of us know yet.
*  But my guest today, Kanaka Rajan, is hot on the trail of this mystery.
*  Kanaka recently took a professorship at Mount Sinai where she brought her bag of very useful
*  tools that she can apply to a wide array of problems.
*  In the past, she has contributed a lot to our ability to tame and harness the often
*  slippery RNN, and she now uses those RNNs and other tools to understand how our brains
*  produce behaviors and how regions within our brains interact to produce those behaviors.
*  Recently she applied her talents to help understand how we transition from actively
*  resisting a challenging situation to passively giving up on it.
*  In this case, she used RNNs as a powerful tool complementary to calcium imaging of the
*  entire brain of zebrafish while they go from regular old fish to a state of sort of throwing
*  their hands in the air, or their fins in the air, I guess, and giving up all hope,
*  somewhat like graduate students do at least once per week.
*  Anyway, we talk about that and how Kanaka thinks that using RNNs this way can be an
*  alternative kind of connectomics to understand functional connectivity in our brains.
*  We also touch on her work to create models that can multitask, which is an ongoing challenge
*  in AI and something that we need to understand better to understand our own brains.
*  And as usual, we touch on a lot of surrounding topics like the current challenge for theory
*  needing to keep up with this deluge of brain data that's being recorded these days.
*  Plenty of useful advice and more.
*  Links to all this stuff can be found in the show notes at braininspired.co.au slash podcast
*  slash 54.
*  I am Paul No Brooks.
*  You can get in touch with me by emailing paul at braininspired.co or on Twitter I'm
*  at PGMID.
*  It makes me really happy to bring you guys these excellent guests.
*  And I hope that the podcast is setting off all sorts of ideas in your biological recurrent
*  neural networks so that, like Kanaka suggests, you can find like a little sliver of a problem
*  and start to explore your way to really interesting places.
*  Be well and be happy out there and please enjoy Kanaka Rajan.
*  Kanaka, we finally digitally meet.
*  Welcome to the show.
*  Well, thank you very much for having me.
*  I'm really excited.
*  I've, you know, even mixture of excitement and nervousness, but I'm delighted to be asked
*  and I'm excited.
*  I was just talking to an old friend on the old telephone last night and he was asking
*  me how the podcast was going.
*  I was like, oh, it's good.
*  I've got an interview tomorrow.
*  And he said, oh, where are you going?
*  What do you mean?
*  Oh, they must be coming through Durango, huh?
*  I had to explain the entire internet concept to my friend.
*  Okay, that doesn't happen that often.
*  I mean, right now I resent people that just pick up the phone and call me without texting
*  me that they're calling me.
*  I never answer the phone.
*  Why would someone answer the phone?
*  Why would someone answer the phone?
*  Yeah.
*  I don't know, but it's attached physically to my body.
*  So, you know, stands to reason.
*  Yeah, sure.
*  Anyway, that that conversation made me feel pretty advanced relative to my my friend who's
*  aging like I am.
*  Right.
*  But people like you have always made me feel very behind in everything I do.
*  So thank you for that.
*  So Kanaka.
*  We try.
*  We try.
*  That's a secret club.
*  And that's the goal.
*  I think you do have a secret club.
*  That club.
*  And you're one of it's a growing club, I guess.
*  But it's always been there.
*  That club is a group of neuroscientists with a, you know, physics and engineering background
*  and approach to things.
*  And much of what you do is theory driven.
*  And I'm insanely jealous of your kin.
*  This has allowed you to sort of choose what areas that you want to study, really.
*  So I kind of want to start off just with a couple of broad questions about about this
*  this whole thing.
*  So a lot of people on the show, when I ask them, you know, what would you do differently
*  or how would you approach things if you started now and stuff, they always often will say,
*  you know, it's computational skills are important.
*  I wish I had done more math.
*  And even people well versed in math will say this, you know.
*  And I personally have the same feeling.
*  I wish I had done more computational, had a better fundamental understanding of much
*  in computation.
*  Right.
*  Do you agree with that?
*  And I kind of want your take on, you know, if whether you're surprised how little maybe
*  you see in the neurosciences.
*  I see a fair bit.
*  But, you know, the reasons I have the sort of circuitous math, physics, heavy background
*  and my route to neuroscience has been sort of atypical.
*  Right.
*  Like that has actually helped me in terms of, you know, the physics and math training.
*  And you kind of alluded to it a little bit in your in your question, which is there's
*  this freedom.
*  Right.
*  Like I can literally pick any class of problems within the broad realm of biology and look
*  at it from this lens of the set of powerful tools that physics and math have.
*  My formal training in physics and math have provided.
*  So yeah, I think that every especially now, right, given how advanced technologies are
*  and how advanced computing technologies are, people should absolutely have a quantitative
*  background and it's never late.
*  Right.
*  That's the beauty.
*  Now it's not like you have to literally go to a class or anything.
*  Now there's all these massively online courses to pick up the stuff that we need.
*  It isn't that much.
*  It isn't 200 years of theoretical physics to make a dent in research problems.
*  It really isn't.
*  You don't have to read the Principia from Newton.
*  So yeah, that's right.
*  But do you I mean, so there is a sort of fundamental question of how much is enough to start off
*  with fundamentally right.
*  And how much can be learned as you need it to sort of in a just in time taking these
*  online courses and stuff.
*  You know, what's the right end?
*  I mean, just to throw another cog here in the wheel, then there's the you know, you've
*  always been interested in neuroscience and in biological intelligence in some way or
*  another.
*  So that has kind of guided you.
*  It's not like you just thought, oh, I'm just going to study these.
*  I'm going to study physics in case it comes in handy someday.
*  Right.
*  There needs to be some sort of interesting thing that you're striving toward.
*  Right.
*  Well, kind of.
*  Right.
*  So my interest in neuroscience wasn't piqued until after I had gotten an undergraduate
*  degree in engineering and I was, you know, halfway through a master's program in physics.
*  And so, you know, interest in neuroscience was really brought by looking at the problem
*  from the lens of my training and from, you know, how much is enough?
*  I think linear algebra is a good place to start.
*  And very, very quickly, you can ramp up to, you know, the kinds of problems that I actually
*  rigorously and analytically solve.
*  And so the thing is with with neuroscience, we know so little and there's so many unsolved
*  problems.
*  That very, very quickly, even someone with, you know, not much more than a high school
*  education in quantitative fields like math or physics can ramp up to really contributing
*  to research in a matter of months.
*  That said, everything can't be just acquired the data sciences through an online course
*  route.
*  This requires, I mean, you know, there is the discipline and the philosophy of, you
*  know, sitting down and writing equations and problem solving.
*  And the discipline for me is the clearing the deck.
*  Right. I mean, it's philosophically, you know, the brain is gnarly, the biological brain
*  finds gnarly solutions.
*  And so to be to have the discipline to say, OK, this is the small problem, a sliver of
*  the problem that I am interested in solving.
*  And these are the tools I'm going to use.
*  That requires discipline.
*  So clearing the deck, you mean getting rid of everything and setting your sights on that
*  one sliver of a problem on one sliver of a problem, which, you know, looks small from
*  the start. It's not like, you know, I can start with something like I want to understand
*  memory. That is not how the day to day works.
*  The day to day works with I want to understand the small sliver of a problem.
*  How does the brain do exactly or how does the brain solve this one small problem?
*  And then can I build an artificial like a toy model that can solve that problem, then
*  compare the strategies that my toy used with the one that biological brains could use.
*  But that discipline is what my training taught me.
*  Honestly, everything else can be picked up.
*  Yeah. OK.
*  Because when you get old like me, it's really hard.
*  You know, the math is harder and harder to pick up as you age.
*  Right. So I don't know.
*  This is a constant question that I get in emails to, you know, like wanting people
*  wanting advice on how to start and stuff.
*  So it's linear algebra.
*  I'm telling you, literally, it's like, you know, follow Gilbert Strang's video lectures,
*  which, you know, are now available and then do the homework exercises in the back.
*  Then literally pick up one of the homeworks that people post from their computational
*  neuroscience courses.
*  And you'll surprise yourself.
*  Hopefully. I hope that's true.
*  Yeah, it is 100 percent.
*  The kind of work that you do, it's right in between AI and neuroscience, really, it can
*  be right. You know, do you feel like your work applies as much to artificial intelligence
*  work as it does to neuroscience?
*  Absolutely. Absolutely.
*  One of the questions is what should, you know, brain research, neuroscience and AI be
*  doing less of?
*  It's literally the stop fighting and recognize the fact that the two fields are really
*  two sides of the same coin.
*  The goals are slightly different, right?
*  The goal of traditional AI machine learning is to build the best tool that does
*  something. The original goal, though, was to understand minds, I think.
*  That's right. So that's right.
*  So that's right. Somewhere along the way, we've gone, we've diverged a little into an
*  engineering focused, let's build the smallest thing that can do the most things model
*  versus someone like me who wants to say, OK, I'm going to take the innovative and
*  technological explosions from AI.
*  But my goal is to understand how the brain would solve that problem given only the
*  machinery that the brain has access to.
*  So that is the constraint and the lens through which I'm looking at the problem.
*  So, you know, so take, for example, multitasking, right?
*  It's a thing that we do, animals do effortlessly.
*  We do many, many things. And of the many tasks we do, they're chunked into many actions
*  that have to be threaded exactly right in the right order.
*  So from an AI perspective, right, if I were working in a traditional AI field, my thing
*  is how do I build the smallest network with the fewest components that can do the most
*  massive array of things? Right.
*  And then, you know, I want to go sell that or whatever.
*  Right. What I'm keen on is to understand, well, OK, so the brain does do this thing,
*  right, of many, many tasks.
*  I'm capable of having this parallel thread of thinking in my brain about why is he asking
*  me this versus also actually having a conversation with you.
*  So the question about neuroscience here that I'm keen on is what in the brain is
*  tracking what task I'm engaged in and when it's time to switch.
*  There has to be something in the brain that's monitoring, OK, I'm engaged in this task
*  and these are the switch points.
*  And that's something that I think is, you know, a kind of a big unanswered question
*  that, of course, can go both ways.
*  The better models of this kind of tracking ability that we have, the better we're able
*  to build AI, but also understand the brain.
*  I think that's right. It's come up a lot on the show.
*  And just in neuroscience in general, there's, you know, there's proposed two systems that
*  operate in some domain.
*  Right. And then the question is always, how does it switch between the two?
*  The two systems, the two ways of doing it.
*  Right. And so this is open in a lot of different fields.
*  So, yeah, it's an important question.
*  That's right. That's right. So what in the brain?
*  Like, where do you look for this thing?
*  Right. This thing that's a state tracker, that thing has to have, you know, a steady
*  representation while I'm having this conversation with you.
*  But when I'm done talking to you, that thing needs to switch to a different mode to say,
*  OK, ask over.
*  Now, look at it from the disease perspective.
*  Right. I mean, I'm at Sinai and, you know, I.
*  I'd sort of be an idiot to not think about that.
*  Right. But let's say I take a sip of a glass of wine and I know that action is complete.
*  I put it down and I do that until, you know, I'm done drinking my glass of wine.
*  But suppose that system that tracked when the task was over and when it was time to
*  switch failed or just refuse to track it at the right transition points.
*  I could have compulsions, addictions.
*  I could fail to complete movements because, you know, I was repeating the same sets of
*  movements because a tracker was broken.
*  So where does where in the brain do I look for such a thing?
*  What time scales do its activity patterns vary like?
*  And and so on.
*  Yeah, this is a well, first of all, I'm glad you're drinking wine while we're talking.
*  So I know you've picked up your fake wine glass, your bottle of water.
*  Yeah. Well, so you've been working with recurrent neural networks since before it was
*  cool. You know, it's really cool these days.
*  You've done a lot of work dealing with the chaos that made RNNs difficult to work with
*  and with how they can be used for things like memory and sequence processing and so on.
*  So we're about to get into some of your work in particular.
*  But why are recurrent neural networks in particular good models for brains?
*  Well, the brain is recurrent.
*  So that's sort of the simplest answer possible here.
*  The brain isn't you know, brain doesn't transmit information unidirectionally from one
*  group of active neurons to the other without any feedback loops, even in the primary sensory
*  areas, right, like the visual cortex connections go back and forth.
*  There's an incredibly rich network of feedback connections.
*  Recurrence is what drives it.
*  Now, a slightly deeper answer to this is that recurrence buys you some very cool
*  properties, mostly in terms of processing things in time.
*  And so that can only come from feedback loops.
*  And so when you brought up these chaotic networks, there used to be this thing in the
*  field, right, like chaos is bad because you make a small perturbation and, you know,
*  things can flail out into unpredictable trajectories.
*  And for a long time, networks that produced chaotic activity were considered unusable.
*  Well, they were they were unusable in that in that they were unpredictable.
*  They weren't solving the problems, right?
*  They couldn't be trained.
*  That's right. That's right.
*  And then innovative people showed up and figured out how to, you know, quote unquote,
*  harness this this sort of chaotic patterns of activity into meaningful patterns of
*  activity. And so I've contributed to that body of work and so forth.
*  But but the key is that, you know, at the there are sort of two main issues.
*  So there is a thing as less chaos and more chaos.
*  This was a thing that I learned during my work in my PhD on networks that were
*  spontaneously chaotic, but could be channeled to do useful things nonetheless.
*  So there are things that are in the regime of fully chaotic and unusable, but there
*  are also things that are less chaotic and could be used.
*  So, for example, my entire thesis was about how inputs like subtle inputs could
*  influence the pattern of spontaneous activity.
*  So you while I'm having this conversation with you, I'm not shutting off all of the
*  rich thoughts and daydreams that occur in my brain.
*  Right. So there is that aspect.
*  The second major thing is that at the point when these networks become chaotic, there's
*  a critical slowing down.
*  And this comes from actually solving these equations in an idealized setting, which may
*  or may not have much to do with the real brain's operation, but have guided our
*  intuition till today.
*  That critical slowing down is responsible for for explaining a lot of how we can do
*  things over time.
*  Is the do you mean by the critical slowing down?
*  Are those the fixed point attractors or those the attractors that it's slowing down
*  in the regime?
*  So it's related to that.
*  That is exactly related to that.
*  I just want to talk about chaos the rest of the time, but we'll come back to it, I
*  suppose. OK, cool.
*  So, I mean, obviously, yeah, RNNs, that's the other way to go.
*  Brains aren't just feed feed forward.
*  They just are. Right.
*  I mean, the question is really back to, you know, do you want to understand the
*  functioning of the brain with the constraints of the machinery that the brain has?
*  Yeah. Or do you just want to build a device that does something better than the brain
*  does, which is, you know, great.
*  Also, computers outperform us every day, every day.
*  All right. So here's my goal for the rest of today's show.
*  I'm going to hammer you with really stressful questions, and I'm going to be
*  unsatisfied with all of your answers.
*  Of over the course of the show.
*  My hope is that I will affect your serotonin and send you into a downward spiral
*  from an active, enthusiastic participant into a passive, nearly non-responsive
*  pool of depression.
*  Does that sound good?
*  Let's see how it goes.
*  OK, let's see. Let's see how much violent thrashing occurs and, you know, en route to
*  this. So I'm referring to this recent paper that you were a part of here called
*  Neuronal Dynamics, Regulating Brain and Behavioral State Transitions.
*  And this is a nice example of what's happening a lot lately is just kind of a
*  massive collaboration between a lot of different people coming together, a lot of
*  different parts coming together to answer these questions.
*  And your role in this thing, was it mostly modeling using the recurrent neural
*  networks? That's right.
*  So I was the lead theorist on this project.
*  The lead experimentalist, of course, was my long-term collaborator and friend,
*  Karl Dysarath, whose lab also provided all of these data from experiments that Aaron
*  Andelman in his lab performed.
*  And so, yeah, we're in this era where, you know, these problems have gotten very hard
*  for one person to just to lift.
*  So, yeah, we're in that in that time.
*  Plus, you can't publish anymore unless you've done the modeling and the behavior and
*  the optogenetics and, you know, bring it all together, right?
*  So, OK, so let's just to kind of set up what was done.
*  You know, what so what are active and passive coping?
*  Right. So, you know, in life, right, we're constantly evaluating amongst actions and
*  figuring out whether whether doing something is worth the effort.
*  Right. Like including this, you know, charming interview that I'm currently in.
*  So, you know, how optimistic or pessimistic I feel is influenced in large part by how
*  how these choice of actions has yielded fruit in the past.
*  And so, you know, if if you keep repeating actions and they keep failing, you become
*  hopeless. Right. In the extreme, hopelessness can, you know, cause things like depression.
*  And so hopelessness is one of the hallmarks of depression.
*  And it's defined as the deep discounting in the value of effort applied.
*  And so this is seen in many, many animal models as well as obviously in human studies.
*  And so a lot of work was done on rodents before, including, by the way, in Carl's lab
*  about animals in various laboratory settings.
*  And they were stressed and the stresses have to be persistent and inescapable.
*  And animals would initially try to avoid the stress by vigorously trying to move away.
*  Right. I mean, this is what animals do.
*  That state of trying to fight against the stress and leave the situation is active coping.
*  But if those actions are ultimately fruitless with enough persistent and inescapable stress,
*  you go into this mode where you don't thrash around anymore or movement cease completely
*  in some cases. So that in a more sort of complex setting is known as learned helplessness
*  or more generically passive coping.
*  So, you know, active to passive coping, there's like a line between the two.
*  It's a continuum. And in disease cases, you become you, you lapse into passive coping
*  earlier. And in response to medications, you may you may delay the onset of passive coping.
*  And so what they did in their experiment in this in this beautiful set of experiments was to, you
*  know, figure out a zebrafish model.
*  Larval zebrafish have, you know, many, many advantages, but they, you know, figured out this
*  way of stressing larval zebrafish until they elapsed into passive coping.
*  These are just like little mild shocks.
*  Right. That's right. Little mild shocks that are delivered.
*  And initially when the shocks arrive, the fish whip vigorously and try to escape.
*  But if the stresses keep coming, the shocks keep coming and they can't escape the
*  scenario, fish become immobile.
*  And, you know, that is passive coping.
*  But in these experiments, you could track the tail whips in real time and monitor almost
*  the entire brain with cellular resolution through this whole experiment.
*  Yeah. Which is another advantage of the zebrafish, just because they're translucent.
*  That's exactly right. And you can do really good imaging and optogenetic manipulations in
*  them. They have a powerful set of genetic tools.
*  But from a theorist perspective, right, this kind of sampling is
*  unparalleled. So, right.
*  So in mice, they have, you know, 71 million neurons and the best experiments can capture
*  you, you know, less than a hundred of the of the electrical activity of this entire
*  ensemble. But here you can record everything with cellular resolution, practically
*  everything. Well, yeah, right.
*  It's just a backup. I guess the behavioral question was, what is this transition from
*  active coping to passive coping?
*  And then sort of the neuroscience and modeling question is, how does that transition
*  happen? What's happening in the neuroscience question is, where is it happening in the
*  brain and what's happening in the brain?
*  I guess because in the past, passive coping has been associated with just a ton of
*  different neural regions based on previous studies.
*  Right. So this thing is like looking at the transition from active coping to passive
*  coping in the brain. Where does it happen?
*  How does it happen? And this is where like the modeling work comes in as well.
*  Right. That's exactly right.
*  That's exactly right. So we know by just looking.
*  So the only thing the animal is telling you is at what point it stopped thrashing.
*  Right. That's literally the only thing that you can.
*  That's the only reported variable here.
*  The rest is through measurements and through modeling, through principled theory, as
*  well as computational models to pick out signatures of the mechanisms that drive
*  this active coping and passive coping transition.
*  So from measurements alone, right, they knew that there were a few regions that are
*  involved in this.
*  They knew how these regions could behave in response to the stressor.
*  So by looking at activity directly.
*  But then how these dots are connected and what are the meaningful signatures that are
*  driving this transition?
*  What sort of connectivity changes brain wide mediate this?
*  Is there something common between the motif that, let's say, my model extracts in
*  zebrafish and the models that I build with my mice collaborators will will extract?
*  I mean, the commonalities are interesting, but the divergences are also fascinating.
*  And so, yeah, that's why I think we need these these experimentalists and theorists
*  working together. So, you know, I you know, an interesting thing is that we have a
*  interesting piece of data sparks my interest.
*  I build a model and make a prediction that they then verify, which refines my models.
*  It has to be this intimate loop.
*  Yes. Well, maybe we can just go over the neuroscience results and then I want to get
*  into the modeling because it's really cool the way that you approach this.
*  So, OK, so you have these zebrafish.
*  They were given this behavioral challenge where they were induced into a passive coping
*  state from an active coping state.
*  And I mean, the main results, I guess, are in the habinula and the raffae.
*  Do you want to do you want to just sort of just summarize what was seen in the habinula
*  and the raffae? So what they got from the measurements alone?
*  Well, they got two things from the measurements, right?
*  One was the fact that, you know, these tail whips, if you look at the, you know, the
*  number of whips the fish makes through the experiment, that in the case of the
*  challenged fish, decreased slowly until it ceased.
*  Right. So that's sort of the behavioral measurement.
*  By looking at the neural activity during this time, Aaron extracted two salient
*  signatures. One was that the habinula seemed to ramp up its activity.
*  So there was this, you know, slow and steady increase in the excitation in this one
*  region, the habinula.
*  Which had classically in people who are depressed, it has higher activity, etc.
*  That's right. So hyper activation of this of this region is known to be implicated in
*  depression. And I'm choosing my words rather carefully here because, you know, it's in
*  this, you know, brain wide ensemble.
*  Yes. The second neural signature was that the raffae nucleus, which is known to be
*  downstream of the habinula and fish, as well as in mice, that decreases its activity
*  and then sort of asymptotes throughout the experiment.
*  So those were sort of the salient findings, the experimental findings in this in this
*  article.
*  And then in you come with your recurrent neural networks.
*  That's right.
*  So what was the purpose of modeling these things?
*  So one is what caused this?
*  Right. I mean, you know, it's this it's this gross manipulation from the outside.
*  Something is coming in.
*  Right. This is shock that's given to the tank and those fish with its head fixed.
*  So what is changing brain wide?
*  Right.
*  I mean, they have activity from all of these all of these, you know, you know, ten
*  thousand neurons at a time, at minimum ten thousand to forty thousand neurons.
*  Image over, you know, an hour long, half an hour to an hour long experiment.
*  And with the tail velocities.
*  So what's causing the habanula activity to go up?
*  And, you know, at what point does the raffae decide to get engaged and what's driving
*  that? And ultimately, who's shutting the movement down, causing passive coping?
*  So to look at this massive data set and to extract motifs that are correlated with these
*  activity patterns, modeling was required to build an almost an artificial like a
*  metaphysical that captured as many of these experimental features as possible.
*  But one that I had built, so I knew what its wiring would reflect.
*  And, you know, could I test the wiring predictions on actual larval zebrafish?
*  This is this is what is, you know, under this umbrella of this often overused term, you
*  know, mechanistic understanding.
*  Well, one of the really I don't know.
*  I don't know how often this is done.
*  But one of the things that jumped out at me as being interesting is that so so they
*  recorded a ton of neurons.
*  Right. And then in your model, you could make as many units in your model as there
*  were neurons that were recorded.
*  So that's right. I can make more as well.
*  So if I'm modeling the mouse, I would be, you know, this is this is where the
*  power of building these models comes in.
*  Right. So, you know, if I'm, let's say, recording a hundred or a thousand of the
*  number of units as there are in the animal, I can still build a much larger network
*  and then subsample from it in the fish case.
*  Right. I could build a ten thousand unit network, no sweat, and then train each
*  unit to look exactly over time as the as its its its partner neuron did in the real
*  fish. Which is how you trained the models, which is how these models are trained.
*  Yes. OK, so you have you trained the models to on the population activity that was
*  recorded from the zebrafish.
*  That's right. And then, I mean, there's a nice figure in the paper where, of course,
*  the unit activity perfectly overlaps with the recorded neuronal activity.
*  Very nice. And then you could compare the activity of the models.
*  So there so there were models trained to the prebehavioral challenge before the
*  passive coping was induced in the zebrafish.
*  And then you could compare those to the models trained to the neural activity after
*  the passive coping was induced.
*  So so what did the models tell us?
*  So so the way this works is, you know, I take a recurrent network completely
*  randomly wired and to say, OK, here are these model neuron light units.
*  They're, of course, not not entirely biological.
*  They're missing many of the bells and whistles.
*  But, you know, the way it works is I take each unit and its activity, which, let's
*  say, in the spontaneous case could be chaotic or irregular.
*  And I train it by this learning rule to match the calcium imaging data directly, a
*  calcium fluorescent signal acquired from that particular neuron.
*  So in this case, every neuron in this network has a partner neuron that provides
*  its target functions and the partner neurons, of course, in the real fish.
*  So I train this network in three epochs in this paper.
*  So there's a baseline period, which is the first six minutes of the experiment.
*  Then there's, of course, the next six minutes during the early phase of the shocks.
*  And then towards the end, after the shocked fish have lapsed into this passive coping
*  or immobile state, then, of course, there's a third network.
*  So just interrupt with the so the activity that's being recorded with the calcium
*  imaging, it's an analog signal, right?
*  It's like like an activation.
*  So it's not a spiking network that you're training.
*  It's like a regular old neural network.
*  So you have an activation function.
*  It's a constant continuous signal, not spikes.
*  That's right. That's right.
*  That's exactly right.
*  I mean, these are rate based units within these networks.
*  And so, you know, it was convenient that the experimental data set was, you know,
*  calcium imaging. It was nuclear localized G camps for what it's worth.
*  So it was I mean, we knew that what was glowing was was an actually a neuron.
*  So that was that was another sort of power of the experiment that we leaned on.
*  But you are training these analog analog signals helped.
*  OK, but you know, the key is that, OK, sure, we these these networks are
*  incredibly powerful, right?
*  And the reason they're powerful is because the thing that we're changing varies at
*  the square of the number of neurons.
*  You see, so while I'm training 10,000 neurons, it's 10,000 square number of free
*  parameters. So I could do anything with them.
*  Right. I mean, they these I mean, I could train them to ballet dance and and lapse
*  into passive coping simultaneously.
*  Right. So these are very, very powerful networks.
*  So the question is, well, OK, so the thing that I derive from them, that's the key.
*  Right. Once you've trained this, of course, you can train them.
*  They work. The surprising thing is the interaction matrices that you can derive
*  from the trained network afterwards, which we don't have the foggiest idea how to do
*  with measurements alone. There is no connectome for the fish.
*  There is is not no connectome for the mouse and certainly not for humans, at least
*  for for a long time.
*  Right. And so these interactions really reflect the pairwise influences of one
*  neuron in the in the fish to another neuron in the fish.
*  That's what gives you these little arrows between region one, region two and region
*  three and up to region 21 that really drive this behavior.
*  And so you this is like sort of a modular kind of model.
*  So you had how many regions were you did you set up?
*  So they have about 15.
*  So depending on the fish, somewhere around 15 to 21 regions.
*  Oh, I see. So there are simultaneously image.
*  So, yeah, we just take a network that big and train them all.
*  I see. And then you can you can look at the interconnecting the interconnections
*  within a region and then also between regions.
*  That's exactly right. In the first in the paper that you were you were, you know,
*  you were currently discussing the paper that came out last year.
*  I think maybe, you know, it came out this year. Right.
*  So in that paper, we focused on the habanula and the raffae alone, because those
*  who had the closest link to the experimental findings in that paper.
*  So we trained the whole brain network, but we looked at it from the lens of just
*  the habanula and the raffae. What we're doing now in a subsequent manuscript is to
*  train and analyze this entire brain wide connectivity.
*  So we're deriving these directed interactions and we're also chunking this
*  experiment into finer epochs.
*  So we have these tensors that go, you know, so each it's like
*  a loaf of bread. Each slice is one of these matrices.
*  But as you go through the the loaf, it's this matrix and it captures the
*  experiential and behavioral state of the animal.
*  So it's really what I'm saying is what we have now is a chance to develop a whole
*  new kind of connectomics.
*  Are you guys writing that up right now?
*  Or we are we are currently in the process of writing that manuscript.
*  Very excited.
*  You can't talk to anyone about it. If a paper comes out, it means they did the
*  work about 600 years ago.
*  So it's right.
*  Or at least in neuroscience, not so in in AI.
*  But OK, but just a sort of idea, you know, what they refer to as a paper is
*  it's a very generous definition of paper.
*  We're getting into the politics now.
*  Sorry.
*  Well, OK, but just OK, then to get back to what you found in the model in this
*  ancient now paper.
*  So so what did what did you find in the models, you know, in terms of
*  connectivity within areas and between areas?
*  And how did that match with the neuroscience results?
*  So there were a few things we found that the biggest were OK, you know, when we
*  compared the overall distributions of the interactions within these matrices that
*  were composed of connections within the habanila, within the raffae, as well as
*  projections going from the habanila to the raffae and raffae back into the
*  habanila, we found that there was an almost 20 percent increase in
*  connectivity in the sub matrix relative to the rest of the brain between control
*  and shocked fish.
*  So that was the first result.
*  Most of these synaptic changes that were the strengthening of weights was
*  driven by the habanila, where we saw a concomitant increase in the synaptic
*  weights as well. And we also saw the surprising thing of these connections
*  strengthening in the projections between the raffae to the habanila to raffae to
*  the habanila, which is classically backwards.
*  So classically, we know that there's a raffae projection and the model is OK, bad
*  stuff happens. The habanila goes bad stuff's happening, you know, projects the
*  raffae, which dumps serotonin and say, don't worry, the cavalry's here.
*  If that helps you feel better, then great.
*  But if if that doesn't help, then something shuts the movement down.
*  Right. So we're now in the second manuscript looking for what is shutting the
*  movement down. And I'm thinking that maybe it's related to this backward
*  projection from the raffae to the habanila.
*  It may not. It doesn't have to be.
*  So the reason I call these directed interactions and not synaptic connections
*  is because I'm keeping a general it's functional connections that they're not,
*  you know, monosynaptic projections or something can be an indirect effect.
*  And so these were surprising things that were inaccessible for measurements alone.
*  Yeah, it's I mean, you know, to me, like the modeling work is such a large part of
*  it. And then when you actually read the paper, it's sort of is it the last
*  paragraph maybe before the discussion?
*  I'm not sure. But it's not like an afterthought, but it's just the amount of
*  space that it takes up in the paper isn't nearly as much as the amount of space it
*  takes in my mind. So.
*  Right. Well, hence the hence the the second manuscript that explores these in
*  much more detail. Yeah.
*  You know, there's a lot that goes into putting together this paper.
*  So really, like, you know, if you look at the first draft or something, it had like
*  87 figures and that is just impossible.
*  Many, many, many components.
*  I mean, the fact that these experiments, I mean, these experiments were heroic.
*  So in the first paper, they were center stage in the in the next paper, we're
*  going to take a different track and we're going to look at these computationally
*  focused brain wide interactions in these multi-region models.
*  So it's the same model, though, but you're just including more of more analysis on
*  the. So so it has it has a few changes.
*  We're also doing things like, you know, we're we're restricting the plasticity.
*  So we're going to say, you know, between region plasticity is a little less full
*  than within region plasticity.
*  And then I told you already about stacking many of these matrices in a logical
*  manner over time and epochs.
*  So then, you know, all of the powerful tools from math and physics with with
*  tensors comes back into play.
*  And so we're discovering kind of things brain wide.
*  All right. So you've got then you made these models and it shows the
*  interconnectivity between within the habinula and the raffae to habinula
*  connectivity. And now and I mean, I haven't read this new manuscript that has
*  six hundred figures at this point, I imagine.
*  So so where is it all going here?
*  Well, so I see this going in.
*  OK, so this is going to take a little bit of babbling to get right, if that's
*  all right. We like babbling.
*  I think it is also related to where the field is going.
*  So I think now we're at the sort of second revolution in neuroscience.
*  When I first started in in neuroscience, you know, longer ago than I care to
*  admit at this point, you know, we theorists were in some sense ahead of where
*  neurotechnologies and experimental neuroscience was.
*  Right. We were at the place where we were recording single neurons at a time.
*  Nothing wrong with that. There is nothing wrong with that.
*  Absolutely not. But I'm talking about the direction in which trends are going.
*  So then we were building these theories of, you know, n tends to infinity limits
*  and randomly connected ensembles and using insights from statistical mechanics,
*  which were incredibly powerful.
*  Right. So then that went on.
*  Now we're at the second revolution.
*  Right. So we went from the single units to, you know, recording populations of
*  neurons. Now we're recording from many, many regions with cellular resolution
*  over very fast time scales, but also over the duration of long behaviors.
*  We're also living in hypersensed environments anyway.
*  So all the way from humans to animal models, we're able to capture, you know,
*  behavior in exquisite detail.
*  So we're at that revolution with the ability, ability to do all these things,
*  ability to do all these things. That's right. But, you know, current
*  neurotechnologies and let you monitor, you know, thousands of neurons at once over
*  long periods of time, even in awake behaving mammals, sometimes simultaneously
*  in interacting mammals, which is very cool.
*  So what theories are not experiencing the same revolution yet.
*  So to make sense of data from these experiments, but also to, you know,
*  in some sense, keep up, we need fundamentally new models of the brain
*  that capture not just within region interactions, ignoring everything else,
*  but treating each region as only a small bit of the, of the vast ensemble it
*  sits in, capturing between region interactions, looking for things like
*  signal gating between regions.
*  So all the principles of inter-area communications.
*  And so we have to look at interactions brain wide and build theories of that.
*  But my pet is still to look at these from the lens of constraining to the
*  machinery that the brain has got access to.
*  Well, right. So by building networks of networks, right?
*  That's right. So that's what that is what I'm doing now.
*  I build, build these networks of networks that are constrained directly by
*  experimental data.
*  And then I either, you know, neural data or behavioral data, and in some cases
*  both, which is a hint of what is to come in the second man.
*  Oh, good.
*  But, but, you know, the key is really that I'm able to reverse engineer them and
*  bring the same sorts of tools to bear the same tools from random matrix theory and
*  the tensor analysis and, you know, all of that good stuff onto these now richer
*  ensembles.
*  Yeah, it was, I had David's a solo on my show a long time ago now.
*  And he, one of the things I remember he said is like, you know, we're recording
*  more and more neurons. And the question is, what are we going to do with them?
*  And, and I had this experience when I was a postdoc even going, I, I started my
*  postdoc was still recording single neurons in awake behaving monkeys.
*  And then over time, you know, we got bigger and bigger electrodes and record
*  more and more. And I had this conversation with Jeff Shaw, my advisor.
*  I was talking about some different tweaks we could do to the task.
*  And then we, you know, can record more.
*  And he said, yeah, but what are we going to do with all the data?
*  We have all this data that's just building and building and building.
*  Who's going to, what are we going to do with all of that old data then?
*  Where is it going to go?
*  And so this is an ongoing problem.
*  That's right. That's right.
*  I think more is not necessarily better.
*  We're with theory able to make predictions for what the minimal set is, for example.
*  So I'm not saying more is necessarily better, although that is the trendy trend.
*  I think what, what theorists can provide is some numbers to our experimental
*  colleagues and say, this is the minimal set.
*  This is where you look for the interesting behavioral drivers.
*  These are the timescales at which they vary.
*  And this is the minimal set and maybe it's conserved across species, but
*  maybe it's divergent across species.
*  But, you know, we're worth to look to insights from Eve Marder that there are
*  many ways to skin this particular fruit.
*  Yeah.
*  Well, okay.
*  So this is a good stuff.
*  So that, so this is one of your pushes in your, in your work is you have these
*  different regions and how they interact with each other and how they're
*  interacting internally.
*  And then another thing I wanted to talk about, you have this, I think it's
*  impressed now it's maybe not out yet, but it's impressed.
*  So, well, the paper is, it's a little review paper called how to study the
*  neural mechanisms of multiple tasks.
*  So then this is a different sort of pushing in your work.
*  I don't know.
*  Do you want to just kind of compare it to this inter regional?
*  Sure.
*  Sure.
*  So, you know, I mean, there's, it's not a comparison so much as a second sort
*  of interrelated direction in my lab.
*  And I think I talked about this at the very beginning as well, when we were
*  talking about this AI neuroscience drift.
*  And so I can pull from that as well, a little maybe.
*  Yeah.
*  Well, so there's, I mean, in, in AI, there's the problem of transfer learning,
*  which is like a really open challenge, a big problem still.
*  And so to get networks to perform multiple different types of tasks
*  is an ongoing challenge.
*  And there's.
*  That's right.
*  Right.
*  So, so, you know, this is a problem that is faced by, you know, essentially two
*  of the leading fields studying this kind of thing, right?
*  Like multitasking is the thing that is studied by AI machine learning approaches.
*  Like how do we build the smallest machine that can do the most variety of things
*  without forgetting the previous things it has learned.
*  So that is a, that is a big push.
*  I'm interested in a slightly different direction of that.
*  I was going to say, so, you know, I had, Matt Botvinick on the show and, you
*  know, we talked a little bit about meta learning and now every paper I see has
*  the word meta learning in the title, you know, coming out.
*  So, which is learning how to learn.
*  Right.
*  And, and, and multitasking was also, there's this, this huge explosion.
*  So, you know, how has your approach to this problem different from those?
*  Right.
*  So I, it's a, it's complimentary, I would say, right?
*  Like I'm still driven by the primary desire not to build the smallest thing
*  that can do the most things better than humans can, but I want to sort of
*  understand how the brain does it with the, with its machinery only.
*  So I want to understand this one key functionality within multitasking.
*  So, you know, the brain could solve many, many tasks by either being one
*  homogeneous bag of neurons and then train many, many outputs, one for each
*  task being performed, right?
*  In which case the prediction would be that you record from a population and
*  there would be a bunch of, you know, mixed selective neurons, for example,
*  you know, classic work from, you know, Stefano Fusi's lab also worked from
*  Insanali at all recently about these atypical, you know, tuning across
*  populations that are seen in many parts of, of the mammalian brain.
*  So that's sort of one modular, one, one module solution.
*  Then there's the other solution in which everything is specialized, right?
*  We know the brain has many regions.
*  And so each region could have a very specialized function and they're then
*  collectively, they cooperate or compete or, you know, interconnect in clever
*  ways and solve the problem.
*  So both of these are unrealistic models of the brain in multitasking, right?
*  So somewhere in between is the solution that has, you know, features of
*  flexibly learning many things, but maybe not doing everything a hundred percent
*  perfectly.
*  And so one of, again, this comes back to my training, right?
*  I want to clear the deck and, you know, laser focus on one aspect of this
*  problem that I think could, could potentially be this, the key to figuring
*  out where on this continuum the brain is.
*  And so that sliver for me is figuring out, well, when, if we're doing
*  multitasking, someone in the brain has to be monitoring, you know, what task
*  I'm currently engaged in and when it's time to switch to the next task.
*  So where's the state tracker in the brain and what time scales does its
*  activity look like?
*  What happens when the state tracker is broken and how do you correlate that
*  with, you know, timing deficits or inability to stop doing things in time
*  or festinating and those types of, you know, neuropsychiatric issues.
*  But even from a basic sciences perspective, that's the sliver problem
*  that I'm currently interested in.
*  And of course, you know, scale that up to other settings.
*  Very good.
*  So actually the, I mean, the paper that I'm alluding to here, one of the
*  coauthors is Michael Cole, with whom I was in graduate school way back.
*  Yeah.
*  So it was good to see his name on there.
*  Mike, one of the things that he was doing in graduate school and he's, you
*  know, continued to do is this sort of tasks switching work, you know, there's
*  this big automatic versus controlled processing that humans are known to, you
*  know, switch between.
*  And I've had plenty of people on the show.
*  Roshan Cools talks about, has talked about neuromodulation and its role in
*  switching between flexible and stable regimes of behavior.
*  So, so this task switching is such an important thing moving forward.
*  And we're not going to go back to phrenology where it's just super, super
*  modular, right, back in the day.
*  But like you said, it's the brain is not just a bag of neurons where every
*  neuron is mixed, is infinitely mixed selectively.
*  That's not a phrase, but I'm going to use it.
*  But then, okay.
*  NARLY, right?
*  That's another technical term I like.
*  I like NARLY.
*  Yeah.
*  I'm going to maybe start using NARLY.
*  Yeah.
*  But so what does this mean for, you know, using these network models to
*  model the brain moving forward?
*  I mean, are we just going to end up with as many RNNs connected together as
*  there are modules in the brain and then a task switcher or what?
*  What's it, what's it going to look like?
*  Personally, I would like a minimal set constrained by behavior, right?
*  Like let's find a class of behavior.
*  So that I'll tell you what the, the, the next sort of paper in the series that
*  I'm writing is about, for example, right?
*  So one of the things is, okay, can, you know, I just told you about this continuum,
*  right?
*  Is the brain a bag of neurons with many outputs, each doing a different thing?
*  And that's how we get it to, to multitasking, or is it where every module
*  is its own specialized, you know, your friend, a logical analogy.
*  And one of those modules could be the state tracker.
*  So what I'm trying to do is to find the knob that goes smoothly between these two.
*  And then the thing that makes the knob stop turning is experimental data.
*  So, you know, a person that, that has, you know, has really influenced my
*  thinking on this is Anne Churchland, who works a lot on, and also, you know,
*  work from, you know, my postdoc advisor, David Tank, for example, these are people
*  that focus very, you know, they have always the behavior of the animal in the back of
*  their minds.
*  And so they, so, so let me give you the, so the curiosity, right?
*  So one thing that I was curious about in my postdoc is, well, there are
*  sequences everywhere, right?
*  That there are these, you know, temporally ordered waves that appear in the
*  hippocampus, they're there in the striatum, they're there in the parietal cortex.
*  They're there kind of everywhere you look, A, because we can't stop sorting things.
*  But also because what if they're not doing what we think they are, right?
*  What if the role of sequences is really to track that we're seeing sequential
*  patterns in regions with vastly different anatomies and functional properties
*  relative to behavior is because really all they're marking is when the task is
*  occurring and when it's time to switch.
*  And the actual computation is either being performed by a mix of these with the
*  other ones that we're tossing in the garbage or the ones that don't look
*  sequentially modulated at all.
*  Then you go, well, why sequences at all?
*  Maybe we were seeing fixed points before because behavior was a little constrained.
*  We let behaviors become slightly more naturalistic.
*  We're seeing sequences everywhere.
*  Why stop there?
*  What if chaotic attractors are the state trackers and we see high dimensional
*  representations, higher dimensional representations and these complex manifolds.
*  Is that giving a causal role to the chaotic attractors at that point?
*  I mean, so there is this recent push with, with chaotic regimes being
*  computationally viable, right?
*  It totally could be.
*  It could be.
*  So what I'm doing in this next paper is to, you know, in an idealized setting in,
*  in models alone, training networks to do tasks of increasing complexity within a
*  certain realm, right?
*  Let's take just decision-making or just working memory.
*  One of those things.
*  Train these networks to do many things of increasing complexity and seeing if the
*  thing that is tracking, if the neurons or the, the ensemble of model units within
*  these multitasking networks that is tracking different task engagements and
*  switching at switch points are those chaotic attractors.
*  If the task is very complex, slightly simpler representations, like
*  sequences of the task is simpler.
*  And can we toggle if the task increases in complexity, do these trackers increase
*  in complexity as well?
*  See, this goes back to what people need to know when getting into these fields,
*  because now everyone's going to need to know about chaos and the dynamics and the
*  math, maybe not necessarily the math behind it, but even at a conceptual level,
*  this stuff gets pretty heavy and confusing sometimes.
*  So there's this, this is just an open question of what you need to know.
*  Cause you, my time is limited.
*  I don't know about your time and, and I'm a apparently extremely slow learner.
*  So you really have to like sort of pick and choose what you're going to study
*  because anything worthwhile, it's just going to take a damn long time to really
*  know.
*  Again, sliver.
*  This is my thing.
*  This is sort of, I mean, my philosophy almost now at this point is pick a
*  problem.
*  So, you know, here's the thing, right?
*  It used to be, Oh, I, you know, don't do any simulations.
*  I used to solve equations by the light of the moon.
*  And I'm going to one day write a theory of the brain.
*  That's bullshit.
*  We're never going to have a theory of the brain.
*  Okay.
*  Let's just start there.
*  So, you know, so we're not going to do, we're going to be building, you know,
*  we're going to be sitting atop a huge pile of models and then experimentalists and
*  us together will either whittle or aggregate from those and a meta understanding of
*  how we think the brain works.
*  That's how it's going to go.
*  And so, yeah, how much do you need to know?
*  Right.
*  So again, pick a problem, right?
*  Like pick a thing that you're curious about, about the brain, right?
*  I mean, it can't be as big as, you know, dreams or consciousness because, you
*  know, even defining those problems is hard, but pick something, right?
*  Like how do we, you know, swallow or how do I remember phone numbers?
*  And why is it that I remember social security numbers in three, two and four,
*  but phone numbers are like, you know, three, three and four.
*  So what is going on there?
*  And do animals process numbers the same way?
*  Like you walk into a room to figure out which side has, you know, more
*  tables that are free, like walk into a, you know, a cafe and say, which
*  side has got more people.
*  Do you, do you evaluate this based on counting or do you go with a feels like?
*  You know, these are questions like pick us, pick a sliver and then, and then,
*  you know, and then talk to people like me, we'll tell you, okay, read this,
*  this, and this, the minimal set.
*  But, okay.
*  So you've talked to people like you, and this is, I think this is, I'm hoping
*  that this is one of the values of this show that I make is there's a huge value,
*  I believe in circling around, right?
*  So you, you have the sliver and you think, how would I approach this?
*  And then you go, but then you learn like six other things and you come back
*  around to the same sliver and then you have a different approach.
*  And so it's never completely clear on what the correct approach is to any given problem.
*  And so to go and learn these different facets.
*  This is the thing.
*  There isn't going to be a correct approach.
*  You see, like if you, you're talking to me, so my definition of the problem is,
*  you know, quantitatively driven, right?
*  I'm, you know, this, this person that wants to write down something on the X axis,
*  but maybe somebody's intuition is more like, well, how do you know, how do you
*  extract from, you know, let's say videos of patient recordings, you know, things
*  using, let's say deep lab cut, which I'm a huge fan of signatures of when a person
*  has an affective disorder that could be the flavor of problems.
*  Sorry.
*  Deep deep lab cut is the recording system.
*  Deep lab cut is a, is a, is a, is a tool developed by McKenzie Mathis, who was at
*  Harvard and I think she's moving to Switzerland soon.
*  And it's this open source software that you can, you know, it's a, it's a marker
*  less post estimation software.
*  Right.
*  She's, she's also an absolute rock star and could deeply committed to open
*  science and dissemination of her tools and like that, but, you know, maybe the,
*  the problem sliver that you care about are looking at people's videos and
*  patient interviews and extracting features of, you know, when did they get
*  depressed?
*  I mean, what, what are their, you know, pupillary responses in response to, you
*  know, it could be, has to be something that you're curious about.
*  And then the approach, you know, then, you know, you wouldn't be talking to me.
*  Talking to someone like Helen Mayberg and saying, okay, this is, you know, a
*  problem that I care about.
*  Do you have a dataset that would be valid?
*  Then you go learn a tool from McKenzie.
*  Who teaches it to you for free?
*  Man, this is fun.
*  I wish I could do this all day.
*  Uh, I can imagine.
*  Um, well, all right.
*  So just to wrap up, I guess this, um, so I recommend this, this paper about how to
*  go about studying the neural mechanisms of multiple tasks and, uh, people can go
*  and read it on their own.
*  I, I guess in the, in the last few minutes here, if you have time, do you
*  mind if I ask you a few more sort of broad type questions here?
*  Go for it.
*  So what is, uh, one of the best investments of your time?
*  We've kind of covered a lot of this already, but, but looking back, what do
*  you think is one of the best investments you've made in your time?
*  Best investments of my time?
*  Um, you know, I would say a hundred percent diving beyond seeking, um, you
*  know, closed analytic solutions and, and writing down theorems.
*  So, you know, at some point in my career, I mean, my PhD was all about, you know,
*  doing these hard calculations on these idealized systems and, you know, they,
*  it just, you know, shaped who I am and the way I think and everything.
*  Right.
*  That said, at some point in my postdoc, I was like, well, I'm going to look at real
*  data now, and that was a hundred percent best investment of my time.
*  You know, it took a long time.
*  There's nothing more humbling than, than real data cause, you know, nothing behaves.
*  And that's when, you know, the biology is gnarly thing got
*  tattooed to the inside of my skull.
*  But then when you solve a very small problem, even within this gnarliness,
*  it has a miserable impact, you know, like the zebra fish thing.
*  And it's linked to this one very small flavor of this very multifaceted
*  and complex disorder like depression, but you know, it's incredibly
*  valuable and impactful.
*  So that was diving into real data for sure.
*  I mean, and it hasn't sent you into a passive coping state yet.
*  So that's good.
*  Okay.
*  Humbling.
*  Okay.
*  What is a, what's something that you used to believe that now you think is, is naive.
*  That we will one day have a grand unified theory of the brain.
*  You don't think we're going to have a grand unified theory.
*  I do not.
*  I think we are going to have a set of models and mathematical theories and
*  principles, and from which we have to then green some kind of meta understanding.
*  Is that reason for celebration or depression?
*  Celebration.
*  Oh, for sure.
*  Oh, for sure.
*  It's, it's, you know, it's actually giving biology the respect it deserves.
*  You know, in, in, in all of it's it's a knarl and warts.
*  Yeah.
*  Yeah.
*  Oh, a hundred percent.
*  Yeah.
*  Norlin warts.
*  What, what should a neuroscience and or artificial intelligence be doing less of?
*  I may have talked about this a little before, and that's fighting.
*  Fighting.
*  Well, you know, we are after slightly different goals, especially, you know,
*  given that, you know, one is largely driven industrially, one is largely driven
*  academically and forthright.
*  So there are a few differences in viewpoint and how we approach the problems,
*  but ultimately cooperation between these two fields and much more cross
*  pollination is required for us to make progress.
*  Cause I think, you know, if, if, you know, a traditional AI models had, you know,
*  much more regard for, you know, the constraints that biology puts the
*  biological brain, biological nervous system puts, then it would enrich their
*  models and the tools and algorithms that they build.
*  But from our perspective, you know, the explosive and rapid advances in that
*  field in terms of, you know, even coming up with learning algorithms could help
*  people like me understand the brain better by using them as tools to pick out
*  things from data.
*  Well, it can be overwhelming the speed of different proposed models in AI and for
*  neuroscience to try to keep up.
*  Do you see that as a problem?
*  It's challenging for sure.
*  It's challenging for sure.
*  Also, because there's some, there's a fundamental difference in the way that
*  we choose to disseminate our results, right?
*  A traditional neuroscience still very journal driven AI is very
*  conference proceedings driven.
*  On the other hand, conference proceedings have, you know, it's, it's a, it's
*  in an enormous volume, right?
*  They come out at an enormous volume without necessarily as much depth as I,
*  in my oldie timey fashion would like to see with notable exceptions and so forth.
*  So I think, yeah, I mean, to keep up with all of it is definitely challenging, but,
*  you know, you have colleagues whose work and opinions you trust and you talk to
*  them. And I have become much more focused in the classes of problems that I care
*  about. So it has come at the expense of learning broadly, for sure.
*  Yeah.
*  But it has gotten me deeper.
*  And I think it's, it's, yeah, it's, it's a choice I'm OK with for now.
*  Just this morning, I was, I had this moment of self-realization.
*  I was, I had spent, I don't know, I was on probably a minute 15 of merely
*  organizing my reading list, you know, like all the things I need to get to.
*  And I was like, good God, I could have just read for 15 minutes and gotten it
*  over with. So that's right.
*  Then thank God. Then I had to quit.
*  I had to come talk to you, which was the best thing I've done all day.
*  So, yeah.
*  Yeah. So, you know, honestly, between you and me, I get a lot by going to like a
*  smaller meeting, not like, you know, a spray and pray style meeting, but like,
*  you know, a meeting, let's say a Janelia or something or a GRC or, you know, a
*  smaller meeting. And then people will usually describe the results of their two
*  or three papers in that talk.
*  And then stuff a little bit falls off.
*  You also get just better human interactions, which is the thing that
*  really, I think, advances ideas, generation and then productivity.
*  100 percent. 100 percent.
*  This is why, you know, this now, the way that we're working together in
*  neuroscience and not in isolated silos, but in large groups of people, group
*  thinking, I've become a fan.
*  Yeah, because, well, I just had John Brennan on the show who's a linguist.
*  And he kind of he's one of the people who said, I wish I did more computational
*  work, more coding. So he's sort of the opposite of you.
*  But then he employs sort of offloads, I guess he says, that job to his
*  collaborators and gets to learn from it.
*  So we all benefit. It's wonderful.
*  That's right. No, it's it's it's it's I mean, I'm telling you, it's like physics
*  used to be in the 20s. Right.
*  And in computational neuroscience is there.
*  Where do you mean? What else could I be doing with my life?
*  Yeah. Well, OK, so there's not going to be a grand unified theory, the brain.
*  But what do you think is one given trait of our intelligence or cognition
*  that you think is going to be really hard to understand and model and build?
*  The hardest, I think, would be to capture things like learning and development.
*  Right. Like, how do children learn?
*  And are we going to is there something?
*  I mean, look, I don't pretend to think that human intelligence is this
*  mystical, magical peak of the intelligence pyramid that all models should aspire to.
*  I literally do not. Yeah.
*  I think that there's a lot to be gained by looking at things like octopodes
*  and swarms of ants and stuff. Right.
*  I mean, so so yes, I'm agnostic to that.
*  But I think that, you know, the way that juvenile animals learn
*  and then they acquire that learning or shape that learning process
*  throughout their lifetime,
*  that one is going to be a hard one to recapitulate in these machines
*  because there's clearly a value in that route
*  that animals take or even humans take through their development.
*  And so that one, I think, is going to be the be a hard nut to crack.
*  And development always scared me.
*  It's just because but you're used to these things because you've done sequential.
*  But just putting the element of time into anything is scary.
*  Hence recurrence. Right.
*  So what I put time at, you know, what I consider a longish time scale
*  is still, you know, hours at most. Yeah.
*  The problem becomes when the hardware is changing, too. Yeah.
*  Oh, I'm hoping to have someone on my show who deals with this stuff.
*  Sort of the evolution of your best friend.
*  Well, I'm going to she's on my list.
*  OK, she's the email will go out later today. How about that?
*  Got it. Yeah, yeah. No sweat.
*  I mean, she's a person who has work. I'm a fan of his all.
*  I don't know her personally.
*  Yeah, she's definitely if she'll agree, she'd definitely be on the show.
*  What is one of the best scientific, quote unquote, moments that you've had?
*  I feel like there's been many,
*  especially since I've come to Sinai, right?
*  I having your own shop is absolutely, you know, it's a yes.
*  It is completely incredible, freeing intellectually.
*  And so
*  well, I know it's a personal choice.
*  I mean, it's not for everyone. Sure.
*  I mean, ask anyone that's been a postdoc for seven and a half years.
*  But you know, my best, I think still is.
*  So I did my PhD at Columbia
*  with Larry Abbott and Heimson Polinsky.
*  And one of the first papers we wrote together,
*  so Larry and I wrote together was what's now called the Rajan Abbott distribution.
*  So we did the we calculated the spectrum of modes
*  that a network that is composed of excitatory and inhibitory neurons together
*  would form.
*  And so we were doing this kind of, you know, it was a tough calculation.
*  And we were sitting in the Columbia, old Columbia Theory Center,
*  which was, you know, kind of a fishbowl.
*  We were just sitting together and, you know, breaking our heads on this calculation.
*  And meanwhile, I, you know, wanted to put this into Mathematica and see, OK, look,
*  are we are we making an algebraic mistake somewhere?
*  And he was doing it, you know, pen and paper.
*  We were sitting literally side by side.
*  And then all of a sudden, the same result popped up.
*  We jumped out of our seats and yelled.
*  I mean, that to me, it was I mean, everyone just stopped and went freaks.
*  Wow. That to me and that has, you know, it was the first one like that.
*  And it's it's always been special to me.
*  I returned to that memory often.
*  I've got goosebumps myself.
*  I really do. It's kind of a cool one.
*  It kind of never happens.
*  It doesn't ever happen. That's true.
*  That's why I'm saying.
*  So that's why I'm kind of holding on to that one.
*  Finally, Kanaka, what is you have a lot of ideas.
*  You have this set of tools that you can apply to anything that you want,
*  but you have a limited amount of time.
*  Well, what is one idea that, you know, you don't have time to pursue,
*  that you that you think someone else that you wish someone else would
*  or you think someone should?
*  Right. I'm thinking, OK, so I have to.
*  And then you can pick whichever one you like.
*  There's the pet one that I like very much.
*  So, you know how so I have this interest in conservation, wildlife conservation.
*  So, you know, recently I've been sort of involved
*  with this David Sheldrick Wildlife Foundation.
*  And so they rescue elephants, orphan elephant babies that have been orphaned
*  because of, you know, human wildlife conflicts or poaching or what have you.
*  Right. So there are these infants that are hand raised for many,
*  many years by humans, and they're then released into the wild,
*  reintegrated into the wild.
*  They have certain behaviors that entirely wild elephants do not.
*  So, for example, they one of these hand reared elephants
*  were returned after 10, 15 years and they will bring their newborn baby
*  back to the handlers to show them and stuff.
*  So they're not domesticated by any means, rather wild living animals that are,
*  you know, I would like for someone to look at this thing called the expo zone.
*  So what are these elephants exposed to?
*  You know, their genetic makeup, their protein makeup, their epigenetics.
*  I mean, is there anything in there that has now changed
*  because of the way that they've been their early life has experienced?
*  Is that a term expo zone?
*  Exposome is apparently a term I learned recently.
*  Everything that they're exposed to in the environment, it could be the genome,
*  the methyl, the metabolome.
*  So that's one sort of pet thing that I wish somebody did.
*  Then there's the other one, which, again, I don't have time to do,
*  but relates to tools that I know how to use.
*  So what I want to do is to build recurrent neural network models
*  of things like social media engagement or games like Fortnite.
*  So, you know, if I could find one of those guys and have them give me,
*  you know, even anonymized, right, like user data by time engagement.
*  These are still vast time series data.
*  And I would like to use my approach of inferring directed interactions
*  to see if the interactions are, you know, organized by
*  by something sensible and, you know, by like a higher,
*  like a higher order principle or like a high order principle.
*  Like, for example, do these interesting modes come out of it? Right.
*  Like if I diagonalized one of the matrices of interactions from just
*  from fitting the time series data of individuals on social media,
*  are they organized by, you know, our bubble versus the other bubble?
*  Do these bubbles change as a function of what season or, you know?
*  Why do you want to know that so you can beat Fortnite?
*  This is a that's a terrible thing to say, because I know that that I don't.
*  Can you beat Fortnite? I don't. I don't know.
*  I don't know. It's a multiplayer thing.
*  I know. I want to know if it is if there's something interesting
*  in the way that populations, I mean, you know, you know, huge numbers,
*  people in huge numbers are drawn to it.
*  Yeah. Yeah. People that don't play games were hooked on to things like Twitter
*  and Facebook for that reason. Right.
*  So there's something about population wide engagement,
*  even without face to face or interpersonal interaction
*  that could have, you know, interesting mathematical properties.
*  I wish I had something noble to say, like, oh, you know, social media
*  and its effect on election season and the whatever.
*  I honestly not.
*  I want to see this matrix interesting properties.
*  I'll be able to use that. I just had my my wife and I.
*  Our daughter, seven year old daughter, just asked us.
*  Well, if cigarettes, what did she ask us?
*  It led us into the the cigarettes and addiction conversation.
*  And then I brought up social media and this is the new cigarettes
*  you're going to have to worry about, because when I was young,
*  we had candy cigarettes that, you know, we're given.
*  But but now everyone's going to be socially anxious all the time
*  if they don't have their phones on and stuff.
*  So so that work will be directly applicable to me
*  and being able to describe the higher order principles under
*  undergirding my daughter's addiction, future addiction to social media.
*  Well, you're saying future, which, you know, which is it
*  indicates hope and optimism.
*  So so, you know, yeah, there are some positives to write
*  to social media engagement.
*  Of course, I mean, we're able to do this, for example. Of course.
*  Yeah. Well, this isn't social media.
*  However, you can find Kanaka on social media on Twitter.
*  She's at Twitter at Rajan KDR.
*  And of course, I'll link to that in the show notes.
*  And then you can also, of course, find her at Rajan Lab dot
*  org to learn more about what she does.
*  Kanaka, I'm looking forward to these papers that we didn't talk about
*  because they're coming out.
*  Thank you for talking with me today.
*  And I wish you luck.
*  I've had I've had a delightful time.
*  And thank you so much for making the time.
*  to the red Patreon button there.
*  Your contribution will help sustain and improve the show
*  and prohibit any annoying advertisements like you hear on other shows.
*  To get in touch with me, email Paul at Braininspired.co.
*  The music you hear is by The New Year.
*  Find them at TheNewYear.net.
*  Thanks for your support. See you next time.
*  Searching the coffers
*  for empty offers
*  I don't know why
*  you trust the sky
*  You must like your lies from blue eyes

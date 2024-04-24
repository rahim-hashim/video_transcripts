---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5482s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 7666
Video Rating: None
---

# BI 116 Michael W. Cole: Empirical Neural Networks
**Brain Inspired:** [October 12, 2021](https://www.youtube.com/watch?v=LNQVg_o1XaI)
*  We have the activity patterns and the connectivity patterns.
*  And so if it works, then we would say maybe we understand more directly how the neural
*  populations are interacting because there's actual this empirical constraint of the connectivity.
*  If you don't have that, then it's an optimization problem and there's a lot of different solutions
*  that would lead to the same predictions without saying that's actually how it works in the brain.
*  Do I think that this is the real connectivity like they use in models?
*  And I said, I don't know, maybe not, but I should try it and see.
*  And then I've been surprised that these things, I'm sure there's gonna be limits to it,
*  but it does seem to be some sort of equivalence there.
*  This is Brain Inspired.
*  Hey everyone, it's Paul.
*  So often, as you know, I have on the podcast people who use deep learning models to understand
*  brain function.
*  So generally the idea is that you train a model to perform a cognitive task and then
*  compare what's happening in the model with what's happening in the brain.
*  And often, as in the case of a convolutional neural network, the models are built and designed
*  to roughly mimic different brain regions.
*  So if you're building a convolutional neural network to study the ventral visual processing
*  stream, then you will build your layers to mimic the various hierarchical layers in the
*  visual stream, like V1, V2, V4, etc.
*  And of course, there are lots of other networks like recurrent neural networks that don't
*  necessarily mimic brain areas but are still trained to perform a task.
*  And again, you can examine properties of the networks and compare them with brain properties.
*  But the underlying theme with these approaches is learning, you're training the network.
*  Not so with my guest today.
*  Michael Cole runs the Neurocognition Lab at Rutgers University.
*  So I knew Mike back in graduate school.
*  We went to graduate school together, as you'll hear.
*  And he's gone on to do great things, as you'll hear.
*  So Mike has always been interested in cognitive control and our human ability to flexibly
*  adapt and control our cognitive behavior.
*  So you'll hear some about that today.
*  But the main topic that we talk about is his recent work building network models that are
*  kind of like deep learning models, except for two important differences.
*  One of those differences is that the models are built based on empirical brain network
*  data, both structural and functional.
*  So the way it works is he puts someone in an fMRI scanner, he records their brain while
*  they're performing a task or just resting, and measures the activity flow between different
*  regions of the brain.
*  Then he builds a network model.
*  And instead of training the model, where the weights between the units get adjusted over
*  long periods of training, Mike uses the functional connectivity data to just assign weights between
*  the nodes.
*  So he builds models that can perform tasks without training them.
*  He calls these models network coding models and or empirical neural networks.
*  And that's the main thing that we talk about.
*  But of course, we talk about plenty of other things.
*  I joke in the podcast that Mike hates learning.
*  But that's not true.
*  He actually started his career.
*  His PhD was about learning, as you'll hear in the beginning.
*  So I link to the papers that we talk about in the show notes at brain inspired.co slash
*  podcast slash 116.
*  And Mike also fields questions from a few guests like Kendrick Kay, Kanaka Rajan and
*  Patrick Laurent.
*  Thanks for listening, everyone.
*  Thank you so much to Patreon supporters.
*  Enjoy.
*  Michael Cole, you and I go back a few years.
*  Welcome to the podcast.
*  Yeah, thanks for having me on.
*  So we well, I say we go back a few years.
*  It's more like I've just been admiring you from afar.
*  I guess you were one year ahead of me in graduate school at the CNBC and CMU.
*  And you've gone on to be many years ahead of me.
*  It turns out.
*  I don't know about that.
*  You're pretty I don't know, like intellectually, I feel like I've been following you from afar,
*  I guess I should say, in the form of the podcast.
*  As soon as I heard you had this podcast, I started listening.
*  I haven't heard all your episodes yet so many.
*  But I've heard a handful.
*  How dare you, sir.
*  But yeah, I don't know, like I can I can see that you've really expanded your horizons.
*  And I'm a little jealous that you have the time and and I guess space to be having these
*  really awesome conversations with such a variety of people.
*  Well, today's topic is about the jealousy that I have for you and what you're doing.
*  Okay, let's focus on that.
*  Yeah, focus.
*  Let's focus on that.
*  So back when I knew you, you were a cognitive control guy, back with Walt Schneider early on.
*  But I'd like to just pick your brain about how you see your sort of career trajectory
*  and alongside that, just how your interests have changed over time.
*  Yeah, sure.
*  So how far back should we go?
*  I actually got into cognitive control in Mark Dispizito's lab at UC Berkeley.
*  That's where I went to undergrad.
*  And I didn't know much about it when I volunteered in that lab.
*  I mean, I learned about it in class.
*  So I was a cognitive science major.
*  So that was the multidisciplinary major at UC Berkeley.
*  And actually started out with more interest in psychology and computer science.
*  And then I was forced to take these neuroscience classes that ended up shifting my interest towards there.
*  So I had this kind of computational and cognitive psychology kind of bent to my interest in neuroscience early on.
*  I volunteered in Mark Dispizito's lab, so full-time RA for a little bit, and then started working with Walt Schneider.
*  And while I was there, I got more and more into computational topics, but kind of like indirectly, I guess.
*  I've been reading papers and building little models for a long time, but not publishing much on that.
*  But it's really shaping my thinking over the years.
*  And so while I was there, so Walt, back in the 1970s, had come up with this controlled versus automatic processing dichotomy that really influenced things a lot.
*  And so you would talk a lot about the real basics of like, what is control processing, what's automatic processing?
*  And out of that, I realized there hadn't been much exploration of one of the definitions of control processing as novel task performance.
*  And so that led me into rapid, instructive task learning, which is there wasn't much or almost any work done at the time when I first started thinking about it and talking to Walt about it.
*  And so, yeah, that ended up being a dissertation.
*  That's technically, you know, almost by definition, cognitive control is just a different, it's not that conflict kind of stuff is typically talked about with cognitive control.
*  So what, because we're going to talk a little bit about RIDL, rapid, instructed task learning.
*  So what is that? And in the sort of big picture, what have you found?
*  And I know that it has stayed with you throughout your career.
*  Right. Yeah. So RIDL stands for rapid, instructed task learning.
*  And it's something that we actually do all the time in everyday life.
*  So, for instance, like playing a new game that you've never played before, like Monopoly, there's maybe some rules that someone tells you about the game.
*  And then you can rapidly integrate those all together and play this game.
*  And it may sound kind of trivial because, you know, I'm using a game example, but it's really in everyday life.
*  We do all sorts of things like cook a new recipe or use new technology.
*  So it's not just about being able to understand the words.
*  It's about being able to transfer previous knowledge into new context.
*  So you get a new smartphone. You don't have to start from scratch and kind of do this trial and error learning.
*  You can transfer knowledge that you already had and also have the instructions kind of prompt you on what kind of transfers to have different kinds of information that you've actually learned before.
*  Could be relevant in a new context. And it's really interesting to me, both from a computational perspective and also just in terms of, I guess, I guess,
*  kind of contrasting humans with machines and humans versus animals.
*  The animals can't do it, except for it turns out, I ended up adding this with a figure to my dissertation because I thought it was interesting.
*  There's one bonobo chimpanzee named Kanzi who can do it.
*  So it's possible in animals through not through sign, right?
*  English words, English words, very simple little tasks.
*  English words. Yeah, he's like a genius champ.
*  So it's possible. But yeah, there's just like one genius animal that can do it pretty much.
*  So the idea, right, is to have a massive set of different possible tasks that an organism or a machine could perform.
*  And then you instruct whatever task to perform, you instruct it.
*  And this happens just kind of interleaved, right?
*  Where you say, do this task. All right. Now, do this task.
*  Now do that task. And the idea is you have to be able to switch between them, which takes a lot of cognitive control.
*  Yeah, I mean, there is a distinction between the theoretical topic or construct or however you want to put it of riddle, which is just things that we do every day.
*  Like, I don't know, like.
*  Get directions to go to a new grocery store or something or kind of arbitrary things you could have people do, like, I don't know, sing the national anthem while jumping on one leg or some things that you've never done before that you could clearly do immediately.
*  There's this whole set of them, but there's, of course, limits to that.
*  And so the problem was, how do we translate that into an actual systematic way to research it empirically?
*  And so that's where this cognitive paradigm that I developed with Walt started from.
*  And the idea is this cognitive task that we came up with to investigate riddle systematically.
*  The idea is that we have these little tasks with three rules each.
*  And the key is that we want them to be kind of arbitrary and complex enough that we're really sure that participants haven't actually done them before.
*  So they're novel, right? There's something to be learned.
*  But we also want them to be learnable very rapidly for humans.
*  And so we have an example here would be both vertical left indexes.
*  Those would just be cues that you'd see on the screen.
*  And then what that means is if both stimuli are vertical, press your left index finger.
*  So then to stimuli will come up in this case, there are these vertical or horizontal bars.
*  You see two vertical bars in this case, in this example.
*  And so the answer would be true and you'd press your left index finger.
*  And so we can swap out these different stimuli and different rules.
*  So another example task would be neither red left index.
*  So that means if neither stimulus is red, press your left index finger.
*  And so you press and if it's not true, you press your left middle finger.
*  And then so you see like a blue vertical bar and a red horizontal bar.
*  So it's not true that neither stimulus is red.
*  So you press your your left middle finger in that case.
*  And so, you know, it's not super easy to do, but participants can do this.
*  On the first try, if you can believe it, of a chance.
*  And the key is that we're moving across, you can think of it like a state space, right?
*  You have all these different combinations of rules and it's systematically,
*  we're systematically traversing it cognitively, right?
*  In terms of information processing.
*  And we want to be looking at the brain while that's happening.
*  You can see the brain updating in a systematic way.
*  We can do all sorts of things like look at changes in activity patterns and
*  the functional connectivity patterns with task state punctual connectivity.
*  And then that's led to what we call the flexible hub theory that we're really
*  testing in some of these papers where we have these kind of control networks
*  that are really highly distributed.
*  And we found evidence that there have hubs in them that update global processing
*  systematically as you perform different tasks like this.
*  Say a few more words about flexible hub theory because I'm not sure that we're
*  gonna be talking about it a ton, but I think it's neat and important.
*  So can you just talk about that a little bit more about what it is and
*  what you found?
*  Okay, so the flexible hub theory is really building on some older theories.
*  One is called the guided activation theory by Miller and Cohen.
*  So that's back in 2001.
*  And it actually goes all the way back to some artificial neural networks.
*  In the early 90s, they're really focused on lateral prefrontal cortex and
*  how it represents contexts or task rules.
*  And so what we've done with this theory is really expand that to entire cognitive
*  control networks so much more distributed.
*  We're also emphasizing global brain connectivity or hubness.
*  Because we're really thinking about in a context of something like Riddle,
*  you need to be able to rapidly update your global information processing.
*  And so how is that gonna happen?
*  How are you gonna even coordinate that sort of update?
*  And so there's a lot of evidence from neuroimaging that these
*  common control networks are involved in that sort of thing.
*  And also from lesion studies, from neurology and neuropsychology.
*  So if you ablate these regions, you have major problems with things like Riddle and
*  fluid intelligence generally.
*  So that's one thing.
*  So we're really emphasizing the connectivity here.
*  There's also flexible connectivity.
*  So we're looking at task state function connectivity,
*  how it updates the connectivity, how the brain regions interact update.
*  And then finally, more of a computational property is called compositional coding.
*  So the idea is that you don't just totally update with new connections and
*  new activity patterns.
*  Every time you do a new task, you actually reuse activity patterns and
*  connectivity patterns that you've done before.
*  And the kind of format of the pro paradigm lends itself to this, right?
*  Cuz we're reusing different rules in different contexts,
*  making new task sets that have never been performed before.
*  And you can see that a lot of the same information patterns are being reused
*  when we actually look at the connectivity and activity patterns.
*  So altogether, yeah, that kind of builds this theoretical framework that we call
*  the flexible hub theory.
*  All right, well, take a deep breath because I'm gonna play you the first guest
*  question here.
*  Okay, this early, okay.
*  Yeah, well, because it's from the rapid instructed task learning era of your life.
*  And I think you'll recognize who it is.
*  I'll say who it is after the question.
*  Hi, Mike, Patrick here.
*  Big fan of your work ever since graduate school at the Centers for
*  Neuroscience and the Neural Basis of Cognition in Pittsburgh.
*  Wondering if you could share ideas on how riddle could be used to study
*  a couple of phenomena.
*  On the one hand, free will, which I'll narrowly define as the emergence
*  of an instruction rather than an explicit given instruction through language.
*  Perhaps synthesized by activity in another brain region or
*  even a neuromodulatory process.
*  So not quite a random goal, but rather an intended goal.
*  Do free will representations like the decision to go to a particular goal or
*  perform a particular action look like commanded instructions?
*  And on the other hand, stubbornness or steadfastness,
*  preservation of instruction or goal in the face of distracting, disruptive,
*  or even goal related inputs.
*  Do those representations look similar to the commanded representations?
*  All right, Mike, we've only got three hours to do this.
*  So that's Patrick Laurent, an old friend of both of ours,
*  who is the Director of Emerging Technology at DMGT, which is a British private holding company.
*  All right.
*  Wow, what a question.
*  This is, wow.
*  Starting with an easy one, right?
*  That's why I wanted to introduce riddle because I knew that question was coming.
*  Is this question about riddle?
*  So yeah, there are a few things I could say about that.
*  One is that we could think of our ability to flexibly switch our goals into novel
*  scenarios on a continuum with riddle.
*  So the way we've been studying it is just kind of taking the shortcut for
*  experimental convenience of giving the instructions and just having the participants
*  like do this task correctly or incorrectly and systematically explore the space.
*  But I have thought quite a bit about what if we had the participants select their own tasks or
*  explore some space of tasks.
*  And then I guess, yeah, that would open things up to more free will.
*  There is a literature on task switching.
*  So there's a relationship between all this stuff and task switching.
*  So those would be between two familiar tasks as opposed to a novel task.
*  And there's a whole literature on if you let the participant choose whether to switch to the other
*  task or not.
*  And then there's different brain responses to those two things.
*  And it's not my exact area.
*  So I can't really describe what the differences are in detail, but they tend to be from what I
*  recall and what we call cognitive control network.
*  So there's some kind of additional control processes that are involved in making that
*  decision.
*  Yeah, I'm not sure what was the second part of the question.
*  It was a very nuanced question.
*  Stubbornness, right.
*  Yeah, I mean, there's a whole literature on perseveration with
*  that's related to cognitive control.
*  So it's the inability to switch to switch the current rule that you're supposed to be
*  applying in a given task.
*  It kind of gets stuck in one state.
*  So I don't know.
*  I kind of wonder if stubbornness might be actually our default and you need cognitive control
*  and higher order cognition that kind of jump out of that unless there's some kind of stimulus
*  driven reward thing that would pop you out of the state.
*  But yeah, kind of, I guess I'm trying to read between the lines.
*  I think Patrick might be asking about self-instruction kind of.
*  And I think that is pretty compelling.
*  And maybe like an evolution when we evolve the ability to represent these kind of task
*  instructions in this really flexible way, we probably got both some ability to
*  think of novel tasks and perform them and also be instructed from others,
*  either through imitation or language.
*  With the rapid instructor task learning, I mean, like you already said, you create these
*  artificial scenarios where you have to, it was really instruction dependent.
*  And there's a lot of control having to even understand the instructions and put them together.
*  Right.
*  So free will, right?
*  Internally generated, internally motivated, whatever free will really is.
*  But that internal self-organ, wherever it comes from some sort of self-organization
*  process where it's generated internally, I don't know.
*  How much do you think that it would overlap network wise with like the riddle type of networks?
*  I guess I'm kind of thinking of there's some set of mechanisms that the language network would
*  interact with in these kind of control networks.
*  So I'm talking about prefrontal cortex, posterior parietal cortex,
*  mid-singulate part of mid-singulate cortex.
*  And what would happen in the case of instruction, external instruction would be through
*  auditory cortex, the language network, and then the cognitive control network.
*  And then maybe, I don't know where it would start, maybe orbital frontal cortex or something
*  where you're representing the reward that you might receive if you do this other thing.
*  It might drive selection of a set of task rules or strategies for getting those rewards.
*  Yeah, I mean, free will is a tricky thing, obviously.
*  But I guess my own, as a neuroscientist, I think most neuroscientists,
*  I don't want to speak for everyone, but there's this sense that I get when I speak to
*  neuroscientists about free will is that there is no free will or there's mechanisms all the way down
*  that are largely determined just by one's history and physical reality.
*  And so I don't think maybe Patrick intended us to go down.
*  Never have a hold that deep, but like...
*  Oh, I bet he did.
*  But he did, yeah. He didn't bring it up free will.
*  But yeah, I guess I would say that, yeah, it's probably going to come down to reward predictions
*  as for selecting the goal and maybe the task that you want to perform if you have free reign.
*  There's also this funny thing a lot of the free will experiments will do.
*  They'll give you two choices and then you just kind of randomly...
*  Or like Benjamin LeBette's experiment where it's this, press a button whenever you want.
*  There's some, they're called demand characteristics in the literature, but the task is to press a
*  button whenever you want. Well, if you really ask the person, do they even want to press the button?
*  If they really were free, they'd just walk out of there and do something more fun
*  than that. So what they're really doing is forcing you into this situation where you
*  need to decide if you're going to press a button.
*  And then you're sitting there and you're like, well, I kind of don't...
*  Let's say you didn't even want to press the button at all, but you're like,
*  I have this social pressure to press this button. So I guess I'll press it every once in a while.
*  And so there's some little element of free will, but it's also just like,
*  okay, I have to... I have all these constraints on my behavior actually.
*  And then there's also this sense of like, it's got to appear random, which is not
*  normal for people to be random.
*  So...
*  Right. We're not random. I hadn't heard that. There have been other criticisms of the
*  Libet experiments and we don't need to go through all that because we need to move on.
*  But I hadn't heard that one, that you are constrained to that particular response.
*  And so that in itself is a bit of a confound, I suppose, for free will.
*  So most of these solutions to free will are really reconceptualizations of the concept of free will.
*  So it's almost like moving the goalposts. But on the other hand,
*  the free will that we commonly want, right? This sovereignty over all of our actions and thoughts
*  I think everyone agrees that that doesn't exist because it...
*  Well, most people agree that doesn't exist because it requires some sort of quantum indeterminacy.
*  And then we have to somehow be in that nexus and be responsible for our own behaviors
*  or something like that, right?
*  So anyway, most of the solutions that I see, we reconceptualize it, rightly so, I think.
*  Yeah. We should move on. But I will say that I do think we have pretty much the kind of free will
*  that we actually do want. It's just that I think of it as as long as who I am, my self-representation,
*  which is in my brain, is properly controlling or influencing how I behave and what goals I pursue,
*  then that's the kind of free will that we want. It's just that who we are
*  was determined by genetics and our past, right? That's my conceptualization of it.
*  Yeah. All right. Very good. Well, let's back out. So thanks, Patrick, for the question.
*  So thanks, Patrick.
*  I'm going to go ahead and play another question because it has to do with fMRI.
*  And then this will bring us up to speed with the work that you've done that we really want to talk
*  about because a lot of your empirical work is based on fMRI measurements, right? How you construct
*  these networks that we're going to talk about.
*  So let me just play this question for you.
*  Hey, Mike. This is Kendrick K. and I have a question for you. It's sort of an open-ended
*  question. So really any remark you have along these topics would be appreciated.
*  I was thinking about your sort of research and your focus. I mean, obviously you use fMRI as
*  a measurement technique and you are thinking about computational models of cognition.
*  So I guess my question has to do with the limitations or your wish list, maybe, so to speak,
*  for neuroimaging, I guess, specifically fMRI. In terms of informing your network models of
*  computation, what do you desire out of fMRI or what do you see are the current limitations?
*  For example, is it spatial resolution? So obviously fMRI is limited, at least compared to
*  single neurons or multi-unit activity type recordings. And fMRI is trying to push the
*  limits there and trying to get higher and higher resolution, but it's from practical sense pretty
*  far away from small populations of neurons. So do you feel that's a major bottleneck to, say,
*  developing the types of network models that you do? Or alternatively, things like artifacts and
*  head motion and whether you think that's a major problem and whether you think that's a
*  problem and whether that's limiting your progress in the type of research that you do.
*  So I'd just be curious to hear your thoughts on whether you're worrying about currently
*  trying to make fMRI better, either in terms of the raw acquired data and or the analyses
*  that we can make of it, again, with the ultimate goal of trying to inform what we can learn about
*  computation in the brain.
*  So he mentioned your network coding models. I think he just called them network models.
*  And we're going to talk about those, the types of models that you build. So if you feel that
*  that was Kendrick K, by the way, if you feel like you need to explain those to answer those
*  questions, go for it. Otherwise, we can hold off and you can answer your wish list for fMRI.
*  So yeah, I have been, I'll say this in general, in my career, I have these kind of
*  oscillations of pessimism versus optimism. And so it's actually pretty useful, because when I'm in
*  one of the other states, I'm maybe overly optimistic, I'll think back to like, my pessimistic
*  views. So at various times, I've been quite pessimistic about fMRI. And then other times,
*  I'm quite optimistic. And I have to say, overall, I've learned a lot more about computation from
*  fMRI than my most pessimistic phases. And the things that frustrate me the most about fMRI,
*  at this point, I think has to do with the temporal resolution. Because these things have
*  these network models, which we can get into in a bit, I've really come to the conclusion that we
*  need to understand causal relationships between neural populations. And that's going to be the
*  key. And temporal information is very useful, right for making causal inferences. But it's not
*  the only way. It's not the only piece of information, but it's quite useful. So I actually
*  have done a bit of work with MEG, and I've started doing more EEG work, high density EEG, because of
*  course, it's the opposite problem there, we're more frustrated with the poor spatial resolution.
*  And then, yeah, my frustration has led me to work with some non-human primate data sets
*  recently for multi-unit recording, not collecting the data in my lab. But really,
*  in terms of theory and method development, a kind of thought experiment that led to a lot of this
*  stuff we're going to talk about, the network models, was from actually thinking about the perfect
*  kind of neuroimaging technique if we could record all neurons in real time, what would I do with
*  that? And so that actually keeps coming up again and again, where I'm just like, oh, well, you know,
*  I want it, I wish I had that, here's what I actually have, how do I make do and try to get
*  closer to that? Would you know what to do with that? I think so. It's one of the
*  things where you don't know for sure until you go and try it. It'd be probably too much data,
*  I'd have to do data reduction, to be honest. But what would be cool about that is you could
*  pick your data reduction based on theory or something, get ensembles and do a different
*  analysis that would get different ensembles or something like that. But yeah, I mean, I guess
*  we get into the network model approach. I mean, I thought about it pretty abstractly,
*  pretty abstractly with doing these thought experiments about like, well, what if it was
*  real, like spiking data or LFPs or something. But the idea is that we have these artificial
*  neural networks. And we want to, with this, these algorithms that can dictate how the dynamics play
*  out on a network architecture. If we had the data, we would go in and take all the detailed
*  connections between all the neurons and maybe we could simulate those dynamics on that network.
*  Now, since we don't have that sort of data, especially in humans, we are using fMRI.
*  And that's given us somewhat decent spatial resolution compared to something like EEG or MEG.
*  And not great temporal resolution, but we have a lot of tricks up our sleeves for making do.
*  And the main trick is really experimental control. So you can control the timing of stimuli and
*  responses and so forth. So we can separate different neural events from each other.
*  And then there's a lot of useful connectivity techniques. We could use structural connectivity.
*  We could use, we typically use functional connectivity and we use
*  specifically resting state functional connectivity. And the way I think about that might be a little,
*  I think it's different than a lot of people think about it. I should ask, make a little survey and
*  ask how people think about this, but I think the resting state connectivity is if you,
*  it's almost like if you could just inject noise into each neural population and see what happens
*  downstream. But it's spontaneous activity. So it's kind of like just, we're looking at the
*  effects on the statistics of the signal from just these spontaneous activities
*  flowing between different neural populations. And then that gives us a sense of what's called
*  intrinsic functional connectivity. And what we found was that it's really similar across a
*  bunch of different brain states. So resting state isn't necessarily that special. It's just that
*  you've removed some compounds that might be coming from past stimuli. And maybe it's closer to
*  something like structural connectivity with maybe the synaptic weights kind of influencing things.
*  That's one thing I like about it too, relative to structural connectivity. You might be getting
*  closer to the actual, well ultimately causal influences between them, but it's really hard
*  to make strong causal claims. All right, Mike. Well, I've already, you know, I've buried the
*  lead already, but I thought that those two guest questions were sort of, would fit better toward
*  the beginning. So, and in fact, I don't really know exactly where to start because, so what you've
*  done in the paper is to take functional connectivity data and in contrast to training up a model made
*  up of some sort of architecture and otherwise fairly random units and random connectivity,
*  instead you guys have built models and used functional connectivity data to decide the
*  architecture and also decide the weights between the nodes. So you don't train the model. There are
*  sort of two axes that we could talk about. One is the difference between your approach and the deep
*  learning Jim DiCarlo, Dan Yehman's type approach and also with recurrent neural networks where you
*  train the network on a cognitive task, like you would train an organism on a cognitive task,
*  and you optimize the network and then you compare the network to your neural recordings or
*  however you're recording data. The other way, the other axis that we could talk about, and I'll let
*  you decide what you'd like to, how you'd like to introduce network coding models, is this play
*  between encoding and decoding models, which we've talked about on the podcast about a long time ago
*  and it would be good to refresh people's memory and then use that to talk about what network
*  coding models are. So is that a fair enough summary? Yeah, yeah. So we're trying to kind of bypass
*  the whole like what's the right learning rule, how do you update the weights in these networks to
*  just say let's go look in the human brain or even animal brains would work too if you had the
*  right data and then just parameterize the network that way. And then so there are lots of different
*  things that we are using it for and thinking that it's useful for. One is just why we can go and
*  test these artificial neural network theories because instead of just doing the same thing of
*  optimizing for task performance, we can go and see whether the weights that are there from
*  functional connectivity in the brain, whether the performance or the cognitive effects of
*  interest will just emerge when you go ahead and simulate these things. And so it actually,
*  I use the word emergence which has been, I really think that's what we're doing but I know there's
*  a lot of philosophical baggage with that term. So I started using the word that just generate
*  the cognitive process of interest but it's really the same thing. I mean, emergence in a very simple
*  sense of like the property of going 60 miles an hour down a highway emerges from these mechanisms
*  in the car that we understand. It's not some sort of like a very mysterious thing but yeah.
*  I've been trying to say emergent properties just because it sounds less like strong magical
*  emergence but I don't know how to turn emergent properties into a verb.
*  Emerging properties, I guess.
*  Yeah, I'm trying to think. So there's that you can test, use these models to test these theories.
*  We can use them to make sense of the neural data. So you have a connection when you say,
*  oh, I think this connection is important or it's connecting these two regions. You can have all
*  these different ideas about what it does or is for but when you build one of these models,
*  we'll literally have these what we call activity flows over those connections.
*  And you can go and see and you can even lesion inside the model and see like, oh, what did it do
*  downstream? And the same goes for the activation. So the classic neuroimaging approach of just
*  saying like, where in the brain is this kind of a process? You do that and it's like, yeah,
*  you learn something but then, you know, what does that activity do mechanistically? It's not really
*  clear. And there's typically, you know, there's all this kind of hand wave and trying to interpret
*  it, including in my own work, right, because you're trying to make some bigger narrative here
*  that you understand what's going on. But you know, if you actually link it up with connectivity,
*  then you can say, well, oh, this, this activity here plausibly, you know, influences activity over
*  here. And then that could lead to motor responses and behavior. And so you start to maybe have
*  something like an integrated understanding of what's going on. It's not as easy as all that,
*  of course, like I said before, you know, I think it comes down to causal inferences and causal
*  inferences are super hard. But I think a lot of a lot of people have kind of given up on causality,
*  and they'll just use correlations, we've been trying to kind of move past correlations
*  for the connectivity estimates because of this. And we have made some progress towards more
*  causally valid estimation. But yeah, they're imperfect causal inferences. So we're always
*  pushing towards, you know, more valid measures and trying to make clear inferences here. But it's
*  like, I think it's a good starting point. I think we are learning a lot. And this is a matter of,
*  you know, keeping on and, and advancing the methods while we're advancing that theory and
*  kind of making a nice feedback loop there. How I mentioned the like the Jim DeCarlo work
*  using convolutional neural networks to study the ventral visual stream, right and object
*  recognition. How do you think of network coding models in relation to that? Because,
*  you know, one of the strengths of convolutional neural networks, which of course, were inspired
*  by the visual system already from way back with Fukushima and up, you know, through Yon
*  LeCun. And now, those models are the best predictive models for brain activity in those regions. And
*  they were roughly modeled, they were built to recreate roughly the hierarchical layers
*  within the ventral visual stream, both in sort of their, their magnitude, the size of each layer,
*  and of course, their, their ordering. So how does your approach differ? And how do you,
*  how do you think about what you're doing relative to that kind of approach?
*  I'd say that our approach is probably more empirically constrained because we not only
*  have the activity patterns that were constrained by quote unquote, I mean, and I mean, constraints,
*  both as like, holding us in, but also telling us what how the brain is computing things, right. So
*  constraints also in a good way that we have the activity patterns and the connectivity patterns.
*  And so if it works, you know, if it predicts well on each layer, say, if you're we haven't
*  done this, the visual model with the multiple layers, but that would be interesting. If it
*  actually did work, then we would say, well, maybe we understand more directly how the neural
*  populations are interacting because there's actual this empirical constraint of the connectivity.
*  If you don't have that, then it's an optimization problem. And there's a lot of different solutions
*  that would lead to the same predictions without saying that's actually how it works in the brain.
*  Of course, you'd have more constraints than we have. And that would be nice. And then we'd
*  be even more confident, right, that this is exactly how it works in the brain. But that the point is,
*  right, that these this key constraint of like, here's actually how the neural populations
*  interact with each other is in there. And that could allow for emergence of things, you know,
*  the generation of processes that we don't even think of. Because, you know, if it is really how
*  the brain is, is working, then, you know, you put in maybe some stimulus that the person you're
*  modeling from, I guess you could take one individual or you could take group data from
*  fMRI or whatever modality and parameterize this thing, maybe that person has never seen that
*  stimulus before and you can see what happens in the model. That would be interesting to see.
*  Would it and then you actually take that person and have them see the stimulus, would it do the same
*  thing? But yeah, I think they're both super useful approaches. But there is this added
*  something about the inferences you can make. And then there's this like, potential for,
*  yeah, something that the connectivity is doing, maybe evolution specified it, there's some kind of
*  some kind of bias in the connectivity weights that does something, a model that's optimized for the
*  particular stimuli that were presented during training, maybe they wouldn't be optimized in
*  the same way. Maybe it's from the person's development or experience that the connectivity
*  weights might have been biased in a particular way, maybe to generalize better. So yeah, there
*  are a lot of questions like that. That would be really interesting to, could even be really
*  interesting just to directly compare them. The thing is, though, because it's not optimized for
*  the task performance, it's probably going to do worse, just because there's noise in the data,
*  right? Like even if we had perfect data, then I would think it would do better just because humans
*  have a ton of training and have evolution, like setting things up for optimal performance,
*  to some extent. But yeah, there is this idea that we haven't actually explored yet, but
*  of also just starting with connectivity and then training on top of that. So that could be
*  interesting too, right? Like maybe it would speed up training to start from the connectivity and
*  maybe push the model in a certain way. One reason that we're really excited about this activity flow
*  approach and the whole ENN approach is applications to mental health and brain diseases. So we actually
*  had a paper come out recently and Science Advances that looks at schizophrenia, and we build these
*  little, we could think of as simple computational models that predict activity during a working
*  memory task. And what we found is that we can predict the abnormal activations during the
*  working memory task in schizophrenia patients. And it's also predictive of their working memory
*  performance and how they have this deficit in working memory performance. And we took it,
*  just to kind of illustrate the power of these kinds of models is we actually took it a step
*  further and made a treatment, a kind of hypothetical treatment that if we could get in and change the
*  connectivity however we wanted, what would happen? And we have this machine learning algorithm that
*  predicts from the healthy individuals and the patients what their working memory performance
*  would be. And once we implemented this hypothetical treatment and applied the activity flow algorithm
*  to generate what activations would happen in the context of this treatment, we actually predict a
*  12% increase in the working memory performance, which puts the patients just about in the normal
*  range. And so yeah, we're excited about, well, I mean, that's illustrative of the power of this
*  kind of approach for real world applications potentially. And so we're excited just about
*  the potential for that. But also we want to actually start to learn how to change
*  connectivity systematically and other research so that we can actually go and test this stuff.
*  So I'm really glad that there are people like you that are working on these things because
*  diseases are super important and they're not something that I ever cared about in my research.
*  But I know that that's sort of the point. And so it's really great that you're focusing on that.
*  Now I'm going to have to go ahead and play our last guest question. I think that this is a good
*  time. Although I was just talking about these convolutional neural networks. Obviously something
*  that you've worked on is having recurrent neural networks and setting them up in an architecture
*  so that they are talking to each other like different brain areas would talk to each other
*  and where you can go and perform multiple tasks. And we can come back to this idea of multiple
*  tasks. But you just saying that you've been thinking about training on top of the functional
*  connectivity models made me think of this next question. So final guest question here
*  from your co author, one of your co authors. Hi, thank you for asking my opinion. I'm always happy
*  to chat. First of all, Mike is great. He and I co authored a review on multitasking learning
*  in RNNs with Robert Yang a few years ago. And two, this is such a clever paper. One of the many holes
*  in the field of computational neuroscience, in my opinion, is that there aren't too many models of
*  RNNs based on human data, fMRI data in particular. Mike is one of the few people thinking deeply in
*  this space. And selfishly I hope to be working alongside him again. Scientifically, both the
*  approaches, using connectivity motifs inferred from fMRI in a generative sense in neural network
*  models like Mike does in this paper, Mike and his team, and training RNNs based on time series or
*  dynamics data directly like I do and inferring from the second type of network models, connectivity
*  motifs, I think both of those approaches are perfect complements. The two types of models
*  should also be able to work as constraints for one another. And the reason I'm asking,
*  the reason for my question is, you know, functional connectivity is often inferred using,
*  you know, network analysis or graph theoretic methods on the covariance matrix of time series
*  data, which is, you know, this, you know, N by N object for N units or N voxels. Now in types of
*  networks that I build and train to match units activity to time series directly, such a covariance
*  matrix should come along for free. You see, because every neuron or every voxel is kind of being fit.
*  But in addition, in my type of models, the recurrent weight matrix should also be dynamically stable
*  and should work and you should be able to find one even if the underlying distribution were to
*  change over time, as it does in the brain. So if you buy both of these things that I said,
*  by knowing just the initial condition, we should be able to use this recurrent weight matrix from
*  an RNN fit to dynamics in generative sense also, you know, almost as if it were hooked up to an
*  actuator. So my question to Mike would be, you know, when would this approach in his opinion work
*  or fail? And, you know, when I say work, I want that to mean to capture dynamics and maybe some
*  features of behavior. And also, how would this depend on task complexity and the number of tasks
*  being performed? Now, I haven't obviously shown any of this directly yet, or at all for human data.
*  But you know, I really would like Mike's thoughts on these and then also, you know,
*  would you please work with us on this problem? Thanks, Paul.
*  All right, Kanika Rajan. So did you get all that?
*  Yeah. I don't know if I got all of it, but it sounds awesome.
*  And an invitation for collaboration.
*  Yeah, that's I'm flattered. This is yes, I would like to work on that. I'll say that.
*  Let's see. Some problems I worry about are relevant here, worry about this type of approach.
*  And I'm so I'm focusing on the negative, but I think it's it is awesome. And so I'll say that
*  upfront. That isn't a really good way to go. I think that things that worry about so the
*  limitations of fMRI with the temporal resolution in particular. So the kind of recurrent dynamics
*  are going to be difficult to pick up when you're the neural activities being filtered through the
*  hemodynamic response function. And so it'll be like, you know, event that's 100 milliseconds
*  long will be spread out over 18 seconds. Yeah, yeah, this function and you can kind of infer
*  when it happened, but it's it's a rough approximation. Yeah, so we could use something
*  called deconvolution to help with that potentially. Luke Kern in my lab is a postdoc.
*  And my lab who is currently working on exploring those and trying to validate
*  those approaches more so that that could help. But they aren't perfect. But there are still a lot of
*  can there's still a lot of constraints that are there. So it's possible that we could use fMRI
*  data for that fitting recurrent neural networks. The other thing I worry about is model complexity
*  between, say, two neural populations. There are a bunch of different functions that could equally
*  well predict downstream. So you need to take a certain strategy for dealing with that. And
*  one of our strategies has been simplicity, kind of like Occam's razor kind of approach.
*  And then adding complexity as necessary. So, you know, we start out with correlation.
*  It's probably the simplest thing, actually, covariance without the normalization to be
*  even simpler. But, you know, you move up to correlation, you move. But then we we want to
*  deal with the confounding problem and causality. So they're confounders. So it's one region, say,
*  influencing two others, you'll make a false connection between those two others.
*  So we use multiple regression typically, to deal with that. So you fit all the time series
*  simultaneously. And then but then there are nonlinearities, which we haven't fully gone into,
*  but we're finding that there are cases where nonlinearities are really important.
*  I don't know the nitty gritty details of how the recurrent neural networks are fit. Is there some
*  way to or like with multiple regression, for instance, we use regularization to also deal
*  with some of this, it's a way of putting a bias into the model to simplify things. And basically,
*  you can you don't fit noises as much. You put a bias in there. So you're not doing as much over
*  fitting. So I wonder if there's some way to do that with however the recurrent neural networks
*  effect. But yeah, I definitely think, you know, the actual, I mean, there's evidence that actual
*  brain uses recurrent connectivity, a ton. And there's a lot of really good computational
*  things that come out of that, just from artificial neural networks, like the old element nets and
*  so forth, like for language, and I could imagine for like,
*  that kind of paradigm, so we're talking about with rapid instructor task learning.
*  I forgot to mention Todd Braver. I was in his lab for my postdoc. And actually, Todd helped me,
*  you know, we together developed rapid instructor task learning, the paradigms and the theory.
*  So I don't mention Walt Schneider, but yeah, Todd played a big role in that. And also the
*  network theories. But yeah, so that kind of task requires the sequential processes. And it's kind
*  of like, yeah, you're, you're being programmed to do this little three rule program. And that's very
*  different than I guess, what artificial neural networks are really good at, like more like pattern
*  recognition kind of thing. It's this is actually a sequence and it requires like, temporal control
*  and maintenance of information and updating information in time. And so that is really
*  compatible with things that recurrent neural networks can do. I was gonna say, by the way,
*  it's fun to watch you think about a proposed collaboration in real time, and immediately
*  know the negative like a good scientist. I kind of bookended it though, I said positive, and then
*  a bunch of negative. And then at the end, I was like, no, this is totally the way to go.
*  Sorry.
*  In fact, what happened is you started saying something negative and then
*  caught yourself and said, oh, I think it's a really good idea.
*  Which is good on you. All right. Well, thanks, Kanaka for the question.
*  Thanks for the question, Kanaka.
*  Thinking about these. So the thing that you and Kanaka and like Robert Yang are working on,
*  are these sort of inter-regional like multi-region kinds of models, right? Whereas, I mean, I think
*  you could think of a convolutional neural network as multi-regional, but if you train
*  a convolutional neural network to do perform object recognition, you're training it on one thing,
*  essentially. And of course, catastrophic forgetting is a problem in artificial networks,
*  and so is continual learning. Do you see the advent of these multi-regional kinds of networks,
*  whether they're inferred from empirical data like yours are, or trained on the current flows
*  like Kanaka's are, or the more traditional train a recurrent network on a set of cognitive tasks
*  like Robert Yang is doing? Do you think that the interplay between these regions
*  will help us explain, especially in a multi-task sort of environment,
*  will help us explain properties of empirical data that wouldn't be explained by
*  training on one task in one network?
*  Yeah. I think that's plausible. I don't know exactly why mechanistically though.
*  I'm trying to think of, well, I think actually it's the, what do they call it, the inductive
*  biases is one term that's out there for the kind of things that evolution brings to the table
*  in actual biological systems, and maybe those biases are toward generalization. And so that
*  might be the way, you know, we would discover what those are, and then we can start using those in
*  artificial neural networks too. So that's kind of, I kind of alluded to that sort of idea,
*  like if we did, you know, the Jim Carlo style network, but using empirical connectivity,
*  maybe that would generalize better for vision. I don't know, but certainly, yeah, I can imagine
*  there's all sorts of different processes for generating flexible behavior that would have been,
*  you know, supposedly selected for during evolution that would maybe shape how development happens or
*  how, yeah, just the brain is organized as a whole. And then on top of that, there'd be these,
*  there are these learning algorithms that fine tune things, but maybe the, these biases in the
*  network organization are key. That would be my guess. I don't know about whether it's important
*  to have a lot of regions or, you know, it's really about the number of units or, well,
*  one thing that, yeah, I've kind of wondered about actually is, but what's different about what we do
*  is we look at the empirical brain connectivity and it's quite sparse, at least if you're not
*  using correlation, it's quite, it's quite sparse. You look at the structural connectivity at the,
*  at the like large scale. Whereas, you know, artificial neural networks will start out with
*  these like all the connections that are randomly weighted. And I do wonder if sparsity is a big
*  role here. That's just the beginning, right? Like sparsity and then what, you know, what,
*  what is it about the particular organization that's helping shape activity flow and create these
*  computations that generalize? One of the reasons why I'm asking,
*  and I'm going to kind of keep pushing on this just a little bit, just to build up, I suppose,
*  is something like a Jim DeCarlo convolutional neural network trained to perform object recognition.
*  And that's not really what vision is, right? To solve static objects because we're in this constant
*  flow of doing quote unquote vision while we're doing seven other things and, you know,
*  paying attention to our internal homeostatic signals, et cetera, et cetera. But, and it's
*  not enough just to like show movies because yes, that's, that's movement, but it's also
*  still embedded in this sort of here is a task framework where the world is much more,
*  and I guess I could allude to the push for ecologically valid tasks, but I'll still say
*  task, but, but our interaction with the world is much more dynamic and flowing. And, you know, so
*  I'm, I'm wondering if you, if you think that, and here I'll say emergent properties, right? So if
*  you think that using these kinds of interregional approaches where you have more dynamic interactions
*  among the different regions, however they're connected, et cetera, whether, you know, we,
*  we might be able to explain inch closer to explaining more of our subjective awareness
*  or our, our internal cognitive flow, you know, of, of processing that we experience.
*  That was a mouthful. Sorry. Yeah. Yeah. That's really interesting. So,
*  yeah, so I think in order to really get the kind of dynamic interactions with the world,
*  we're really going to need to be modeling multiple brain regions at the same time, but, but not just
*  that, but how they interact with each other. And so we've really emphasized going all the way,
*  ideally from stimulus to response. We focus really on that feed forward process for now,
*  and it's really about experimental tractability there. But the key is, right, there's no one
*  brain region that's going to go all the way from stimulus to response. So we're really going to
*  need all these inter brain region interactions. And then, yeah, once we get the feed forward
*  process figured out, you know, in some probably limited context, because it's a huge challenge,
*  then I can imagine worrying more about feedback, which is going to be, you know, let's say the
*  feed forward processes, a lot of context, it's most of the problem, right? If you're just like,
*  kind of passively, I don't know, watching TV, or playing a video game or something,
*  maybe that's most of it. But other contexts, it's it's just a small part of it. In reality,
*  most contexts, feed forward and feedback are just constantly dynamically updating with action,
*  protection, perception cycle. But yeah, I mean, at a minimum, yeah, you'd want multiple brain regions
*  involved in your model. And so what we found is that if we took the activity from those things
*  I just described, you know, the sensor input, the task context or rule representations,
*  and also the the motor responses, then we were able to actually simulate that and generate a
*  task performing model from empirical brain data. The trickiest part was was in the middle, like,
*  how do you integrate the task rule representations, so they're going, there's activity flowing
*  through the resting state connections somewhere, and there's sensory information flowing through
*  the resting state connections somewhere. And we want to know where is that. And that's equivalent
*  to the hidden layer and an artificial neural network. It's just like, it's just thrown out
*  there like, Oh, clearly, there's this hidden layer. And in the literature, it's talked about
*  association cortex, which is most of cortex in humans, right. So it's like, where is that
*  exactly? Right. So this is part of the this is kind of a major issue. And actually an opportunity
*  for advancing understanding by saying, like, now, let's actually figure out what where this
*  theoretical construct, the hidden layer is, these are the connection or sorry, these are the
*  conjunction, conjunction hubs is what we call that. Yeah. Because it's hidden layer actually
*  plays a lot of different roles in a lot of different networks. So in this particular
*  situation, it's at the conjunction between the context, you know, task rule representations
*  and stimulus input. And then so what we ended up doing, so there are a lot of different strategies
*  we thought of, what we ended up doing is actually building an artificial neural network that could
*  perform the task. And then looking at what's called the representational geometry of the hidden
*  layer, and then using a representational similarity analysis to look at where which brain regions
*  have a similar representational geometry. So they, you know, the similarity of the activity patterns
*  matches what's going on in the hidden layer. So just to go over this pre print, it's ito at all
*  2021 pre print on the NN, there are basically three, let's say four steps to it. So what we
*  the big idea is that we wanted to take the actual empirical brain data for that activity patterns
*  and use empirical function connectivity to link together these different brain regions,
*  all the way from stimulus to response. And so we start with the sensory input, we decode sensory
*  areas to ensure that we actually have the information that's relevant to the task in
*  these regions. We then also decode the task context. So this is all using that pro paradigm
*  that I talked about earlier, by the way. So you have all these 64 different task rules that are
*  recombined, we decode each of those tasks, and find brain regions that actually have that information
*  in them. We then use functional connectivity to simulate the activity flow that would go into
*  what we might call the hidden layer, or what we call specifically conjunction hubs, because it's
*  the conjunction between the sensory input and task context. We then apply a nonlinearity there,
*  which turns out to be pretty important. And then after that, we do another activity flow step to
*  M1, so the output regions. And then that's our prediction of behavior, right? So we've gone all
*  the way from sensory input to motor output in a context of dependent decision making task.
*  And then we decode what motor response is happening. And it's not just a normal decoding,
*  by the way, it's trained on actual empirical, this is how people press buttons. And this is
*  what happens in primary motor cortex when they do. So we're actually decoding in the form that
*  M1 uses to represent these button presses, and then we get above chance accuracy. So that's
*  actually a full task performing brain model from empirical data.
*  RG Without training, with zero training, just using the, that's awesome.
*  And trying to think, oh, yeah, the other thing that theory predicted that made us think we're
*  really gonna have to do this, but we weren't totally sure, was whether we needed a nonlinearity
*  at the hidden layer. So there, there's a model by John Cohen, Dunbar and James McClellan,
*  in 1990. It's a Stroop model where they introduce this context layer to complement the hidden layer.
*  So that we think of that as like, you know, where the rules are represented as the context layer.
*  So they made a big deal in that paper about the nonlinearity and the hidden
*  layer is really important. It's kind of like an attention kind of mechanism where it's you're
*  selecting the representations that are going to basically filter the stimuli according to the
*  task context, so that you select the correct motor responses. And so lo and behold, we did need a
*  nonlinearity just like we thought we would. I mean, for theoretical reasons, you think so,
*  right? Because it's context dependent decision making, you need this interaction, so that it's
*  like, contingent, right? So if the stimulus, the stimulus can go to totally different motor responses,
*  the same exact stimulus, but depends on the rule. And so that there's a nonlinear interaction that
*  has to happen so you could select the correct one. So I thought that was pretty cool that that came
*  out of the work. One of the things that I like that that you are in pursuit of is so you have
*  connections, right? And it's all networks. And you can talk about the properties of those connections.
*  This is like network neuroscience, right? Where you talk about path length, and the, you know,
*  different metrics of how to characterize a static, essentially network. And then you have
*  functional connectivity between them. And what your work is doing is bringing those two things
*  together. Do you think that but it's still essentially all networks, right? Do you think
*  that this sort of network vernacular and approach, also looking at the dynamics, and like you just
*  were talking about the nonlinearities, but and looking at activity flows within networks,
*  will you think that's going to be enough to, quote unquote, explain cognition? Or do we will
*  we need to talk about multi scale, multi, multi level scale of organizational components?
*  Yeah, so one reason I went down this path of making these empirically estimated neural networks,
*  so these network coding models, which ever term you want to use, was to make that an empirical
*  question. Basically, it was a bit like, you know, do I think I really had a couple moments like this,
*  I'm like, do I think that this is the real connectivity, like, they use in models, I said,
*  I don't maybe not, but I should try it and see. And then I've been surprised, you know, that it,
*  these things, I'm sure there's going to be limits to it. But it does seem to be some sort of
*  equivalence there. And so, like I said earlier about the same, like, we probably won't be able
*  to like, model someone playing a complex piano piece using fMRI, there's going to be similar
*  limits at whatever scale we are. And I'm, but I'm hopeful, right, I think it's plausible to say,
*  like, we could make these tasks that are a little bit artificial, but still informative enough.
*  It's a forced choice between two button presses, because maybe we can decode the right versus left
*  hand really easily or something like that. But you can still get the key network computations,
*  the network mechanisms, as long as you, you know, maybe construct the task appropriately.
*  Like, if we were able to do that, I would be very happy. And then it would be like, oh, no,
*  we can't, you know, do this really subtle thing. And then, yeah, then you'll have to get into,
*  you know, very fine grained things. There's also always the question of like, like, when I say,
*  okay, there's this connectivity pattern between these two regions, and I have all these, you know,
*  voxels inside there. So it's like, pretty fine grained on in some sense. But you always could
*  say like these between these two voxels, what exactly is the physical basis of that, and you
*  go all the way down to individual synapses and explaining that right, so that there's always
*  levels here, it's just whether we are at a level where we can say we're pretty satisfied with our
*  explanation of this cognitive process. And I'm hopeful that, you know, we'll get pretty far
*  at this level. But you never know till you try.
*  Oh, see, there's more more optimism also.
*  Yeah, I guess that was overall optimistic.
*  So Mike, this is ostensibly a show about neuroscience and AI. And, you know, often what
*  gets left off the table in these conversations, and I'm going to make sure and include it in ours,
*  is the potential for like your work, for instance, and this kind of approach for actually
*  influencing and benefiting AI, because right now we're in this place where, you know,
*  we're using all these deep learning. You guys are using all these deep learning models, even though
*  you hate learning and don't use deep learning, of course. But the deep learning model approach is
*  the flow, I'll say, is much more toward neuroscience and benefiting how we're understanding
*  brains. But of course, the whole deep learning approach was began, the whole deep learning
*  approach began with the concept of neural networks, right? So the activity flow does go both ways.
*  Do you feel like these models that you're building, for instance, will have implications
*  for or benefits for AI? Yeah, it's actually on multiple fronts, I guess, if you
*  you resume out a little bit. So the one reason I was interested in the rapid
*  instructive task learning stuff was because I am actually interested in learning, but
*  I'm interested in how, you know, humans learn some things much more rapidly than artificial
*  neural networks. And so, you know, it's possible that some of the insights we get from
*  the riddle work will translate into, you know, being able to just instruct a machine verbally
*  to do some tasks like you would another person. And also just the general ability to flexibly
*  reorient to and reuse concepts and, I guess, task rules or task information. And then in terms of
*  activity flow models, like the ENNs, that's, that's a little bit more where I'm just,
*  yeah, I think I already described a little bit just like, will something emerge from these things
*  that is in biological tissue that we're able to simulate and then just be kind of surprised by its
*  ability to generalize, it's a little more of a bottom up kind of thing than the riddle work,
*  where we're, you know, we have this kind of cognitive theoretical target. And I guess,
*  because, you know, I am trying to merge the two whenever I can, that that would be the ultimate,
*  right? If it was like, we simulate riddle, and then it works. And then it's like, we dig into
*  how the models work in and we say, Oh, this, if AI models just did this one thing, you know,
*  generalize to allow generalization. Is this along the same lines as like the system one, system two,
*  the, you know, condiment system one, system two difference, and or the AI needs a prefrontal
*  cortex push from Benjio and O'Reilly and those sorts of folks? Do you see that? Yeah, it's totally
*  related to that. Yeah. So like, you know, I worked with Walt Schneider, you know, had the control
*  versus automatic processing, which maps, like, even, you know, I believe condiments,
*  said it maps one to one to the system one system two concept. So yeah, I mean, controlled processing,
*  but this particular flavor of control processing that is really about novel task behavior and
*  transferring abilities into novel situations. And that which is directly related to
*  a general human intelligence, which is another topic that I really dug into when I was working
*  with Todd Braver. So general fluid intelligence is this really fascinating concept in psychology
*  that's really about individual differences and is directly related to riddle abilities.
*  They actually correlate quite strongly. And so if we could really, you know, figure out what's going
*  on, like, why do why do humans have this? It's in that it's a factor analytic thing that you can
*  see in the statistics that each individual seems to have this general ability that generalizes
*  across a bunch of different tasks. What is that? You know, where is that in the brain? And like,
*  what's the mechanism behind that? You know, maybe once we figure that out, we can copy that over
*  for AI. And then I guess there's the term artificial general intelligence. And I'm talking
*  about natural general intelligence, right? And maybe there's some way to learn from one and take
*  it over to the other. Well, are those control processes? Are we going to be talking more,
*  like, in symbols and rather than lower level network properties? Are we going to end up,
*  you know, having having this mesh between symbolic and neural network type of architectures?
*  From what I understand, that was a really hot topic, like, in the late 1980s, early 1990s,
*  and it was going that way. And then it, yeah, that's when I read about it more, you know,
*  right, the old literature. So I don't, I haven't been following the recent stuff. But I guess,
*  my, you know, having thought about it for a long time now from that, that older literature,
*  literature, my thought was, you know, let's just figure out how the actual biological tissue does
*  the symbol like stuff. And then, then we can still just stay in this distributed architecture. And
*  you have the benefit of right, like mapping potentially one to one onto the human brain,
*  like we're trying to do with the ENNs. Right, if we start putting in these abstract symbolic
*  modules, then it'd be like, well, where exactly does it map onto you? And then it's like,
*  can we go any deeper into that? Not really, I guess you might be able to find, you know,
*  it maps onto a brain region, but not the inner workings, I bet wouldn't, you know, not very well.
*  So very good. Well, so in our final few minutes here, and thanks for hanging with me for so long.
*  What do you I know you're working on multiple fronts, we talked mostly about just one of the
*  things that you're working on. But I just want to ask you what, like last night, after you brushed
*  your teeth, you know, and flossed and put your anti aging cream on, you know, and laid down,
*  what did you think about what what kept you up longer than you should have been up?
*  You know, I thought I mentioned earlier, something about causal imprints, and I guess that keeps
*  coming, coming up for me as, you know, central to not just what I'm working on, but really,
*  neuroscience and science in general, you know, it's a really hard problem, especially in complex
*  systems, like, you know, the brain and even these AI systems. So one big idea that we've been
*  pursuing in my lab is just this idea of using causality as a kind of common ontology for
*  different areas of neuroscience. And it's really based on a general hypothesis that
*  causal interactions among neural populations, we are really thinking that those will end up
*  being the most critical features for explaining the neural basis of cognition. Of course, there's
*  a lot of other things. But if you have things, if you have neural processes described in terms of
*  causal properties, and these kind of activity flow processes that I've been talking about,
*  then that's going to maybe be the main way of describing, like an explanation for how
*  some kind of cognitive process emerges is generated. So there's tons of other details,
*  of course, but you could think of them more as modifying that process, right,
*  that sets a processes. So you have a nonlinearity at one step, that's about, you know, selecting
*  a subset of the activity flows that then change how things happen downstream. You also have
*  lots of concepts like confounders, causal colliders, that would take a while to get into.
*  But all of those things, I think together are going to be really important for getting
*  explanations for brain function and how cognition emerges from neural populations,
*  the kind of explanations that would be actually satisfied by potentially.
*  One thing I will say that I've been thinking about recently along these lines is the concept of
*  what I call causal sufficiency. So I don't know, maybe, you know, this is already out there,
*  I just haven't come across it. But the idea is, you know, even if you have a blade or lesion
*  or region, you can show that it's causally necessary, but you don't know if that brain
*  region, say, was causally sufficient to make the cognitive process. And that's where these
*  models can come in, right? Like the ENN or even an ANN or any sort of model, right, you actually
*  generate the process. And you could show especially if it's empirically constrained, you can say,
*  this is equivalent in all these ways to the actual biology, and then where it generates
*  the cognitive process of interest. So, you know, at the very least, it's causally sufficient.
*  And then, you know, you also would like to have some of these lesions and stimulation to show
*  causal necessity potentially. But you could even imagine, like, say, there's like,
*  two different pathways that can accomplish the same cognitive process. So you have a blade one,
*  and it does nothing potentially, you blade the other, it does nothing, but really, they're both
*  causally maybe sufficient for generating the cognitive process. Yeah, that's that speaks to
*  work like from, you know, like Eve Marder and the idea of multiple realizability and how, you know,
*  in the end, anyway, we're actuating our muscles, right, to perform some tasks. So it might, right,
*  you might get away with being pretty ugly internally, and still come out with the right
*  behavior. And, you know, this is what everyone's interested in, I suppose, or what we're testing,
*  the vast majority of it is behavior anyway. Right. Yeah, I did have some interesting reviews for
*  something that I was working on with the ENN where I was emphasizing behavior. And that's like,
*  kind of the, it was, I felt like it was like a holy, the holy grail, like, if I can predict
*  behavior, well, you know, that's how, you know, things are indexed. But then I had like,
*  sort of here to say, well, like, all you're doing is predicting motor behavior. You know,
*  what about cognitive processes? I'm like, oh, what, like, we, that, that's what we have been
*  doing. And it's the innovation is that we're getting all the way to behavior now. So then I
*  just, all I have to say is like, no, we've been doing that. That's, that's, that's, you have to
*  make the cognitive process to, you know, predict M1 behavior. But yeah. And they accepted?
*  Oh, I, I'm still in the process of, I haven't submitted yet. So we'll see. Yeah, we'll see.
*  Maybe we'll hear this explanation and be like, oh yeah. Oh yeah. Well, I'll push the, oh, I can't,
*  I got to air it in a few days, man. I can't push this out until it's accepted. So sorry.
*  We'll bleep that I suppose. So finally, Mike, I want to ask you career, a career type question
*  here. So I knew you back in graduate school. I know you did a lot of stuff before that.
*  You've had a lot of good advisors, you know, throughout, and I know you've worked extremely
*  hard, which I've always been impressed with. It seems like you're always on focus and on point.
*  I'm wondering if there's a time throughout your career or, you know, a specific time, or I'm sure
*  there are multiple times, but if you could tell a story about some time that when you feel like
*  luck played a integral part of some success in your career.
*  Yeah. So I guess the early interest in what later became known as network neuroscience.
*  Yeah. Like, and I guess that really started and Mark Desposito's lab. I just lucky that I ended up
*  in his lab and then continued along that line. And the reason it's lucky is because it's beyond
*  me that, you know, the rest of the field really went in that direction so that, you know, I could,
*  I didn't have to swim upstream, I guess, to like make progress on that. There was really a current
*  going and, and, and then also that I was at Washington University. So that's when I was
*  working with Todd Braver and also Steve Peterson, when the human connectome project was started there.
*  I wasn't actually involved in it, but I was right there and I had all these advantages for like
*  knowing about it and what it involved and being able to like ask questions about the data
*  early on. And, and, and that was just like this treasure trove of,
*  of, you know, questions that we could ask without having to even collect new data. We just
*  asked a bunch of questions. And, you know, the analysis took a long time and were a lot of work,
*  but it wasn't nearly as hard as, you know, designing experiments and also, you know,
*  designing experiments and collecting data. And then the large end actually made for much more
*  robust conclusions and statistics. So anyway, all that, that, that I have to say that was,
*  that was luck. Is it possible to parlay that kind of serendipity into advice for aspiring people,
*  maybe people who feel like they haven't been so lucky or they are swimming upstream? Is it even
*  possible or is it just, is the only thing to say that those are just lucky events?
*  I'll say that, you know, there are a lot of people that watch you
*  when I was there that didn't work with the human connectome project data. So I mean,
*  I guess it's like, what's that saying? Like, sees the day favors the prepared minder.
*  I know that sees the day that works too. Yeah. You know, I don't know, just
*  really look for opportunities wherever you are and, and, and kind of, you know,
*  it required me to change what I was going to do. Right. Like, or, you know, even if I didn't even
*  have a plan, you know, I made that my plan instead of something else. So it wasn't pure,
*  you know, like I'm just totally passive. There was some kind of like, yeah, seizing the opportunity.
*  And then there's also, I guess, in this particular case, some intuition. So I don't know,
*  I don't know if that's like, you can totally plan on that, but also be smart. Just like,
*  just like, think plausibly, you know, if this trends this or this little, this little idea,
*  actually, because it was before it was a trend, I guess, or early, early days of the trend,
*  if this kept going, is it even plausibly going to lead to anything? It was like,
*  okay, the brain is a network. You know, we already have known that forever. So like, yeah, studying
*  the brain as a network seems like a good idea. So, you know, that kind of general logic, I think
*  could help. But yeah, I mean, you can't really make general advice on this. I don't think it's
*  just like in this case, important factors. It's like, yeah, the only advice you can give is like,
*  you have to work super hard and, and, and develop skills in whatever you're doing, and I guess,
*  be willing to change, right? And seize the day when something like that comes along and it feels
*  right and seems right. I don't know. Yeah. Yeah. Yeah. Yeah. What is that called? Like,
*  exploration, exploitation tradeoff? Yeah, but then the boy that's a whole, that's a whole other bag
*  to open. Yeah. But yeah, you have to explore and then exploit, exploit, exploit, exploit, and then
*  explore. And I don't know the, but I don't know the perfect pattern for that either. That's
*  something, a recurring theme actually, that I don't know that there's the right,
*  I can't, that I can write out that algorithm, but. Right. All right. All right. I won't keep
*  you any longer. Thank you, Mike, for coming on. Thanks for answering those guest questions as well.
*  Oh yeah. I love the work and continued success to you. Oh, thank you. Thanks for having me on.
*  It's been great talking and the guest questions were a real highlight. It was great to hear from
*  some old friends.
*  Thank you for your support. See you next time.

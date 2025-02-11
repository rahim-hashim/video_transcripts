---
Date Generated: December 18, 2024
Transcription Model: whisper medium 20231117
Length: 5841s
Video Keywords: []
Video Views: 188
Video Rating: None
Video Description: Rajesh Rao shares his updated theory on how the cortex could implement active predictive coding

Show notes:  https://braininspired.co/podcast/201/

Patreon (full episodes and Discord community:  https://www.patreon.com/braininspired

Apple podcasts:  https://itunes.apple.com/us/podcast/brain-inspired/id1428880766?mt=2
Spotify:  https://open.spotify.com/show/2UZj8c8Ap5oc2gh2rJxLLe

The Transmitter is an online publication that aims to deliver useful information, insights and tools to build bridges across neuroscience and advance research. Visit thetransmitter.org to explore the latest neuroscience news and perspectives, written by journalists and scientists. 

Read more about our partnership: https://www.thetransmitter.org/partners/

Sign up for the “Brain Inspired” email alerts to be notified every time a new “Brain Inspired” episode is released: https://www.thetransmitter.org/newsletters/

To explore more neuroscience news and perspectives, visit thetransmitter.org.


Today I'm in conversation with Rajesh Rao, a distinguished professor of computer science and engineering at the University of Washington, where he also co-directs the Center for Neurotechnology. Back in 1999, Raj and Dana Ballard published what became quite a famous paper, which proposed how predictive coding might be implemented in brains. What is predictive coding, you may be wondering? It's roughly the idea that your brain is constantly predicting incoming sensory signals, and it generates that prediction as a top-down signal that meets the bottom-up sensory signals. Then the brain computes a difference between the prediction and the actual sensory input, and that difference is sent back up to the "top" where the brain then updates its internal model to make better future predictions. So that was 25 years ago, and it was focused on how the brain handles sensory information. But Raj just recently published an update to the predictive coding framework, one that incorporates actions and perception, suggests how it might be implemented in the cortex - specifically which cortical layers do what - something he calls "Active predictive coding." So we discuss that new proposal, we also talk about his engineering work on brain-computer interface technologies, like BrainNet, which basically connects two brains together, and like neural co-processors, which use an artificial neural network as a prosthetic that can do things like enhance memories, optimize learning, and help restore brain function after strokes, for example. Finally, we discuss Raj's interest and work on deciphering an ancient Indian text, the mysterious Indus script. 

0:00 - Intro
7:40 - Predictive coding origins
16:14 - Early appreciation of recurrence
17:08 - Prediction as a general theory of the brain
18:38 - Rao and Ballard 1999
26:32 - Prediction as a general theory of the brain
33:24 - Perception vs action
33:28 - Active predictive coding
45:04 - Evolving to augment our brains
53:03 - BrainNet
57:12 - Neural co-processors
1:11:19 - Decoding the Indus Script
1:20:18 - Transformer models relation to active predictive coding
---

# BI 201 Rajesh Rao From Predictive Coding to Brain Co-Processors
**Brain Inspired:** [December 17, 2024](https://www.youtube.com/watch?v=cmxQgQmY9js)
*  The goal of the brain, or at least one goal of the brain, is to learn a generative model
*  of the world, an internal model of the world.
*  And it's constantly making these predictions or doing essentially hypothesis testing, right?
*  So it's essentially generating hypotheses and it's trying to then match those hypotheses
*  with what's coming in through the senses.
*  And when there are deviations or mismatches, those are called prediction errors, and those
*  errors are what are used to then update the hypothesis.
*  If you want to have a very rich way of modeling the world, then what you want to do is have
*  the higher level modulate the dynamics of the lower level.
*  So you need to change the function being computed at the lower level, depending on the task.
*  And so we said, OK, why don't we use these primitive modes of interacting with the brain,
*  so EEG and TMS, and let's build a brain to brain, direct brain to brain communication
*  system with them.
*  This is Brain Inspired, powered by the transmitter.
*  Hello, I'm Paul.
*  Today, I am in conversation with Rajesh Rao.
*  Rajesh is a distinguished professor of computer science and engineering at the University
*  of Washington, where he also co-directs the Center for Neurotechnology.
*  Back in 1999, Raj and Dana Ballard
*  published what became quite a famous paper, which proposed how predictive coding
*  might be implemented in brains.
*  What is predictive coding?
*  You might be wondering. It is roughly the idea that your brain is constantly predicting,
*  or at least back then, it was roughly the idea that your brain is constantly predicting
*  incoming sensory signals, and it generates that prediction as a top-down signal that
*  meets the bottom-up sensory signals.
*  And when those two signals meet the top-down prediction with the bottom-up sensory input,
*  the brain computes a difference between the prediction and the actual sensory input.
*  And that difference, that error, is sent back up to the quote-unquote top, where the brain
*  then updates its own internal model to make better future predictions.
*  So that was 25 years ago, and it was focused on how the brain handles sensory information.
*  But Raj just recently published and proposed an update to the predictive coding framework,
*  one that incorporates perception and action, suggesting how it might be implemented in the
*  cortex. Specifically, which cortical layers do what? Something that he calls active
*  predictive coding.
*  So we discussed that new proposal. We also talked about his engineering work
*  on brain-computer interface technologies, like BrainNet, which basically connects
*  two brains together, and like neural coprocessors, which use an artificial neural network as a
*  prosthetic, essentially, that can do things like enhance memories, optimize learning,
*  and help restore brain function after strokes, for example.
*  Finally, we discussed Raj's interest and work on deciphering an ancient Indian text,
*  the mysterious Indus script.
*  All right, I link to all of the work that we discussed in the show notes at
*  braininspired.co.uk slash podcast slash 201.
*  201. I'm in the process of setting up our next live discussion for Patreon supporters, so
*  if you're a Patreon, check your Patreon messages soon, or check in on the Brain Inspired Discord.
*  Thank you for listening. Here's Rajesh.
*  Raj, by the way, this is the first long motorcycle ride I've taken
*  in since I got a motorcycle and I'm in a hotel. So I may not be on the top of my game,
*  not that there is a top of my game, but anyway.
*  You look great. And yeah, I think it should be interesting to see what kind of interesting
*  questions come out of having done that long motorcycle ride.
*  Well, I actually wanted to start with, well, maybe you won't tell me this, but you were born.
*  Oh, I mean, it's on the Internet, right? It's on my Wikipedia page. It's 1970.
*  70. OK, so when it was the 60s and you're already good at academia,
*  perhaps before you were born, I understand that you excelled in early years in your schooling.
*  Here's what I want to get to. I would like you to tell me the origins of the predictive coding
*  story. So that's what I, yeah, when it was in the 60s and you were before you were born and
*  you were thinking about predictive coding, how did you start thinking about that?
*  That's right. Yeah, it was in my previous life, right? I've been reincarnated now to bring up
*  predictive coding. No, no. So basically it was, you know, the story is essentially that I grew up in
*  India, in Hyderabad, and did my high school there. And I got a chance to come to the US as an 11th
*  grader because I got a rank in the Indian Central Science exam that they have. And as part of that
*  rank, they were able to send me with another group of people to do some research. And so basically
*  I got hooked on to research right at 11th grade, went to University of Maryland, did some research.
*  I would call that, you know, put that in codes, research and superconductivity. It was a time of
*  high temperature superconductivity at the University of Maryland. And I got a taste of research then,
*  and then, you know, took the SAT exam. Never applied to any universities. I was just waiting
*  for universities to contact me thinking if my SAT score is high enough, somebody will contact me.
*  And obviously that never happened because that's the way it works in the IIT exams in India, right?
*  You write an exam, the rank is high enough, you get to go to an IIT.
*  And they will contact you. They'll contact you.
*  They'll let you know, or at least there'll be like a ranking of the announcement and things like that
*  of who got in or didn't, right? So I was under that impression. And then luckily for me,
*  there were a couple of universities that did write to me saying, hey, look, we have scholarships for
*  international students. And one of them was in Texas, a tiny university called Angeles State
*  University. Another one was in Alaska, University of Alaska Fairbanks. And given my preference
*  for weather, you can imagine where I went. So I had some family in Texas as well. So I went to Texas
*  for my undergrad. All right. I grew up in Texas. So I was curious about that aspect of your
*  development and how you found Texas in general. But that was in the, what, early 80s?
*  Yes. No, not early 80s. I'm not that old. I'm kind of old, but I'm not that. It was like a late 80s.
*  So it was basically late 80s. And it was the time before the internet. And, you know, it was
*  interesting. It was an interesting culture shock for somebody coming from, you know, a bustling
*  place in India to like a small town in Texas with cowboys for roommates, right? You can imagine all
*  the interesting things that happened. And I could talk about that over beer sometime. Yeah. Yeah.
*  We'll do that over a beer. Okay. Well, all right. So maybe fast forward, I suppose, because I do
*  want to buy you a beer now about and talk about Texas. But. Predict a coding, right? Yeah. Like,
*  I don't understand the origins of it. Right. I mean, I understand Helmholtz. So, I mean,
*  we don't have to go that far back. So Hermann von Helmholtz with inference and predicting the best.
*  Yes. Predicting the best outcome, predicting, sorry, predicting what you will perceive. And I
*  know that origin story, but in terms of neurons, do you like, what is that origin story? Yeah,
*  I think for me and my advisor at the time, Dana Ballard, so I went to the University of Rochester
*  for my PhD and I was going to do a PhD in theoretical computer science. But then I happened to
*  meet Dana Ballard in the copy room and he said, Hey, you know, I have the summer RA. So can you
*  work with me for a summer? I said, okay, I'll give that a try. And sure enough, you know, that got me
*  hooked to at that time, computer vision. And we were looking at this problem of, you know, how do
*  you reconstruct, you know, objects that are behind occlusions, right? So the idea was, you know,
*  let's take the representation from the visual cortex. You have these Gabor filters, these
*  oriented filters. Now, if you can recognize objects using this representation based on the responses
*  of these filters, can you now also reconstruct what's behind these occlusions that the objects
*  may be behind? And then it turned out that, you know, those filters, you cannot just combine them
*  linearly with, you know, the responses of the filters and then reconstruct an image like you
*  would do for a PCA filters, right? Principle component analysis or the eigenvectors, right?
*  Because they're not just linear, which is linear. I'll just say near. Yeah. But even if you do a
*  linear combination of these Gabor filters, they are non-orthogonal to each other. So that's when
*  we got into, so the idea was, can we then do gradient descent on a reconstruction error cost
*  function, right? And so you have this idea that, okay, we can reconstruct images that are based on
*  non-orthogonal filters, right, the responses. So then it leads to this idea of optimization of
*  the responses of neurons that are trying to reconstruct an image that's been presented
*  based on these Gabor filters. And then if you flip that and say, okay, what if we can not just
*  estimate the responses, but also learn those filters? Then you get this really interesting
*  idea of, you know, at a fast time scale, you do inference, which is similar to what, you know,
*  Helmholtz was talking about, which is inference of what object you're perceiving right now.
*  And you do that using this dynamical system, which is based on gradient descent, right? So the
*  interesting thing there, which was not really appreciated at that time, and even I didn't
*  appreciate as much was the equation that you get from gradient descent. So you have this cost
*  function of, you know, minimizing the prediction error or the reconstruction error. When you do
*  the gradient descent equations, it basically falls out of the equation that you need in
*  architecture that has feedforward and feedback connections. And the feedforward connections in
*  the architecture will be carrying the prediction errors, and the feedback connections will be
*  carrying the predictions or the reconstruction of the image. For fear of losing the audience,
*  I'm just going to back up and we'll go Lego bricks. Sure, yeah. Right. So what is the idea
*  of predictive coding? The idea, do you want me to say it and then you can correct me?
*  Oh, yeah. Go ahead. Yeah, yeah. So predictive coding is basically that you have some
*  idea forward in the brain, somewhere forward in the brain, some idea of what you're expecting,
*  and you're sending that backward through the brain. And those incoming sensory signals that
*  are coming up toward forward of the world of shapes, if we're talking about vision,
*  then they get met with this prediction. And then there's a difference between what you're expecting
*  and what those signals are propagating forward. And it's the difference between the prediction
*  and the signals that gets propagated forward. How does that sound?
*  That's great. That's great. Yeah. So I guess we were good at conveying the message in those
*  papers. So I'm glad to hear that. So yeah, so basically the idea is the traditional model,
*  going back to Hubel and Wiesel was always that you have this feedforward pass. So you flash an
*  image, you get a feedforward pass all the way from V1, V2, V4 in the visual system up to IT,
*  and then you get recognition. And then you get cognition of that. It can make a decision. Maybe
*  you press a button. So that's action. But back in those days, was it always like,
*  voila, there's the cognition of it? If it just builds up to an abstract enough
*  edges to a table leg to a table. Oh, there's a table. And it magically happened?
*  That's the way it was taught, even in the AI field. The whole field of AI was partitioned into all
*  these different... There's people doing vision, there's people doing motor control robotics,
*  there's people doing higher level AI based on logic. It was very similar to how even in
*  neuroscience and cognitive science, we have these people focusing on particular modalities and so on.
*  And then for me, as somebody coming into that area of neuroscience and looking at the anatomy,
*  it seemed really surprising that people were completely ignoring the feedback connections.
*  So if you look at every cortical area, it's sending not just the feedforward connections,
*  but also receiving feedback connections from a higher order area. And then if you talk to people
*  at the time, who are really famous visual neuroscientists and ask them, okay, what about
*  those feedback connections? And they're like, no, no, no, that's maybe doing attention. They're
*  just doing something. Really? Would they really say that?
*  Yeah, yeah, sure. I mean, people thought that those were not really critical for
*  the traditional kind of perception of objects. And those were maybe brought into play when you're
*  doing something like very specific kinds of attention, maybe during sleep and things like
*  that. So a lot of people were not necessarily even acknowledging that those feedback connections
*  could be playing a very dominant role. And so predictive coding flips it on the head. It says
*  the goal of the brain, or at least one goal of the brain is to learn a generative model
*  of the world, an internal model of the world. And it's constantly making these predictions or
*  doing essentially hypothesis testing, right? So it's essentially generating hypotheses
*  and is trying to then match those hypotheses of what's coming in through the senses.
*  And when there are deviations or mismatches, those are called prediction errors. And those
*  errors are what are used to then update the hypothesis. So you're sending them back in the
*  feed forward pathways. So the feed forward pathways are actually not carrying the raw
*  signals, but they're carrying the deviations or errors, mismatches. That was very inside,
*  I think. Yeah, that was different from what the conventional thinking was at that time.
*  Well, okay. So, all right, let's stick with that insight for a second. I mean, did you,
*  was that insights an aha moment for you? I would say the idea was in the air, right? So I was at
*  that time reading papers by people like David Mumford, for example, who was also talking about
*  things like that between the talamus and the cortex and cortex to other cortical areas.
*  There were people like James Albus, who was talking about it in the context of AI. And
*  he'd already done work, obviously, in the cerebellum. That was his main contribution.
*  Neuroscience was the model, right? The Albus model of the cerebellum. But he also had really
*  interesting ideas about hierarchies in AI and in robotic controllers and things like that.
*  And then finally, if you really go back in time, there was somebody named Donald MacKay, right?
*  He's actually the father of David MacKay, who wrote that book on AI information theory. So he
*  actually proposed, he had a paper called the epistemological problem for automata back in the
*  1950s. And he proposed this kind of idea that what if you can send error signals from one module to
*  another, and then you could then build up this sort of abstract representations at multiple levels
*  of the hierarchy. So what we did was essentially take many of those ideas that had been around and
*  then say, okay, let's actually implement that mathematically. Let's see what comes out of it.
*  And then we showed that some of the things that come out of it, if you interpret neural responses
*  as prediction errors, is that you can explain some of these puzzling effects, like end stopping,
*  contextual modulation, orientation, contrast effects, things like that, that would be harder
*  to explain if you just have a feedforward model. This actually gives you a normative explanation
*  in terms of natural images and in terms of natural behaviors. But even if you look back at the
*  McCulloch-Pitts articles, they knew feedback was important. Maybe you can educate me on this a
*  little bit better, but it was almost like a nod to the fact when they were drawing their little
*  neuron diagrams, McCulloch-Pitts neurons, right? One to the other, and then there'd be a feedback
*  loop. And I think they wrote about how it would be important one day, perhaps.
*  Yes, yes. I think they call them loops, right? And they definitely add this idea that loops are
*  pretty important. I think at that time, there were a lot of people interested in characterizing,
*  essentially what we call dynamical systems now. But they were trying to characterize the properties
*  of these loopy networks, right? I think the correspondence between that kind of work, which
*  is very fundamental rigorous basic elementary work, to now trying to map that onto anatomy
*  is, I think, the leap, right? So you have to, that's what Mumford has suggested. And that's what
*  we also tried to suggest was that, okay, let's try to map some of those ideas now
*  onto the cortical anatomy, right? The idea of there's six layers in the cortical area.
*  There's feed forward connections coming into the middle layers, layer four, and then there's feedback
*  coming from the superficial deep layers. And if you look at that, you have the Vanuisen-Fellman
*  Vanuisen hierarchy, right? So can we actually- That monstrosity, that monstrosity of the diagram.
*  So the way that we looked at that Fellman-Vanuisen hierarchy was, okay, what if we interpret that as
*  a generative model that evolution came up with for essentially modeling the world, right? And once
*  you interpret it in that sense, then it says, okay, if you have this idea that you can sample
*  from that generative model and generate examples of what the animal faces, right, and its interactions
*  with the environment, then inference becomes this idea of trying to update those estimates you have,
*  those hypotheses you have about the world. So I think the key idea there was inference as a fast
*  update of the neural responses at the population level in all the different cortical areas. And at
*  a slower time scale, using the same mismatch or errors to then update the weights, right? The
*  learning part, the synaptic plasticity part, that was happening at a much slower time scale.
*  So your famous paper is the 1999, that must be your most cited paper, am I correct?
*  It is, yeah.
*  Yeah. So you had that, and in fact, I've seen you in a talk point to it with optimism for graduate
*  students saying, see, stick to your ideas, and eventually perhaps they will come to fruition.
*  Or perhaps the key word there already.
*  Well, perhaps. I mean, maybe. What do you think is the, oh gosh, I would say 5%. No, no, 3%. What do
*  you think?
*  Yeah, so I think it's hard to say, right? So I would say one of the reasons why that paper,
*  it was published at a time when I think there were still not the kind of techniques you would
*  need to really test some of these predictions. Like for example, these prediction error neurons,
*  right? So can we look at specifically layer 2 and 3, which is where you would expect these
*  prediction error neurons to be, because those are the feed forward connections to the next cortical
*  areas. Similarly, can you look at the deeper, like layer 5 neurons, and look at, okay, what kind of
*  responses? Because in the predictive coding model, the deeper layers are the ones that are storing
*  the estimates of state or in a motor kind of responses and so on. So you'd have to have the
*  techniques, which were not available at that time. But I think if you fast forward 10 years
*  from then and then start looking at in the late 2000s, you start to see more citations of that
*  paper. And then now I think there's so many people trying to look at different aspects of that theory
*  with evidence for some people against, right? So I think it's become a very, very rich area
*  of research. So I think the theory was maybe a little too early for its time at that time.
*  But I think the fact that Nature Neuroscience, which is where it was published, was willing to
*  publish it, right? As opposed to saying it's just pure speculation, right? Which they could have done,
*  I think is credit to them for having taken that particular paper.
*  Yeah, I mean, Occam's razor, it's theoretically great, right?
*  Yeah. So it had an elegance to it, which I think was, we ourselves didn't quite appreciate as much.
*  And I think Friston actually wrote a news and views on it 10 years, 10 or 20 years after it was
*  published, talking about how that one paper really influenced him as a researcher to really pick up
*  the mantle at that point. Because we had actually, I mean, I had sort of moved on to more general
*  models on the Bayesian brain hypothesis and belief propagation in Bayesian networks and things like
*  that. But then of course, Friston went on to do the free energy principle based on
*  predictive coding ideas. And then more recently, active inference. And there's a whole bunch of
*  work that's- Free energy principle, yeah. But so at the time, and I'm sorry to perseverate on this,
*  but at the time, did you know that it was going to be so influential? Or not no, but did you have
*  some confidence, some sense that this is, I know you had a sense that it was a good idea,
*  but I have good ideas every day and they're never good ideas.
*  Yeah. I think at that time I would say I was not too confident that it would actually be
*  something that would inspire people to do experiments. Because there was a news and
*  views that was written on that paper by Koch and Poggio. And it's an interesting news and views.
*  You can see them, they code Sherlock Holmes in a story and then talk about how the fact that the
*  dogs were not barking at night in the Silver Blaze was a story of Sherlock Holmes is an example of
*  predictive coding because the person was not surprising. So then the deduction is that the
*  person who stole, I guess, the horse called Silver Blaze- So that's a very positive review.
*  Yeah. So it was a positive review. But before that, I was told by the editor that the previous
*  person at the ass refused to write a news and views. So it's like, oh, there's already people
*  that are not necessarily going to like this. It goes against their way of thinking about how
*  the cortex works. But yeah, but I think, like I said, there was not as many citations. There
*  was not a huge number of people writing to me and saying, hey, that's a great picture. So I was like,
*  okay, so we wanted to get it out. It's out there. Let's see what happens. And then it took 10, 15
*  years before it really caught on. Caught on, but were there early detractors also?
*  Yeah, I think there's always been detractors. So there's been people, even now. So basically,
*  a lot of people don't buy into this notion of the feedback really influencing the responses and then
*  the prediction errors. How can that even, oh, well, specifically with the prediction errors,
*  that's a different- Yeah.
*  So feedback is obvious in the brain. But even feedback carrying predictions from a higher area,
*  right? So even that- That's not obvious.
*  ... the notion of that is still debated for particular tasks, right? I think there's really
*  clear evidence now that for sensory motor tasks, where there's the animal makes a motor movement,
*  and then there's an inference copy that allows you to make a prediction, right? I think there's
*  a lot of evidence now coming from David Schneider's lab, from your Kellar's lab and so on, showing
*  that when there's locomotion or there's a four-limb press of a lever and there's an auditory response,
*  you get a prediction in the auditory cortex. There's a suppression that looks like a prediction
*  error signal there. So definitely for the motor, I think you see that. If it's purely sensory,
*  I would say I would argue that's in some sense, a purely sensory experiment typically has a
*  fixation and then you're flashing something. It may not necessarily be the kind of naturalistic
*  behavior that would elicit predictions and prediction errors, right? But there have been
*  some reports about these error-like responses in those situations as well, right? So I think-
*  So yeah. Yeah.
*  That's where I think there was initially some resistance in terms of the fact that there
*  wasn't at that time any evidence for feedback conveying predictions and feed forward conveying
*  prediction errors, except for these contextual effects, like these extra classical receptive
*  field effects. And even that, some people were explaining with just through lateral inhibition,
*  right? Which could be one way to explain that. Yeah. So I just want to... So what is the
*  lesson here? It's not that predictive coding is universally accepted still, but now the technology
*  is better and we can have better measurements of hypotheses generated by a predictive coding
*  framework. So one lesson is keep going, grad students, it might get better. But
*  for a... So the jury's still not out, I guess, right?
*  Yeah. I would say there's evidence for some parts of the theory. And I think as a theorist,
*  I feel like our job, all the theoreticians out there, our job is to propose theories that are
*  explicit enough in terms of connecting to the anatomy, which is what we think.
*  Specific enough, yeah.
*  That they can be shot down, right? They can be falsified, right? We basically want to have
*  the ability to falsify theories. And in the process of that, if it generates some new data that then
*  really sparks a new theory, right? And then leads the field forward. I think that's the job, right?
*  And we should not be afraid to propose these theories as long as they're sensible, they match
*  the existing data, right? Which is what we were trying to do at that time was saying, okay,
*  we have these puzzling responses called end-stopping or contextual effects. We have
*  the anatomical evidence saying there's feedback connections. So let's propose this theory and
*  let's see what happens if you start doing experiments. So I would say the same thing now,
*  look at what's out there, what people have collected in terms of the data and look at
*  the computational aspects also, right? So what is the brain really trying to do?
*  Let's look at evolution and yeah.
*  That's what I was about to ask you because so do you see predictive coding or the family
*  of predicting coding approaches as some sort of general theory about what the brain is supposed
*  to do? What the brain is doing because there's the free energy principle now,
*  there's Jeff Hawkins, everything is prediction.
*  These things go back years obviously and everyone points to Helmholtz and there was someone
*  before him.
*  And there's chat GPT and Transformers which are also based on prediction, right?
*  That's right. And we love them.
*  I would say it's just part of the story, right? So prediction is important because
*  animals have to predict to survive. I mean, ultimately it goes up. It's this idea of
*  at a certain point in evolution, the brain start building models of the world to be able to predict,
*  to anticipate, right? And so I think that's an integral part of it. If you're learning a model
*  of the world, then it comes with this benefit of you can use that to generate hypotheses,
*  you can use that to generate predictions. And that I think is an integral component.
*  This idea of world models or predictive models of intelligence, either artificial or natural,
*  right? It gives you a lot of benefits. And it wouldn't be surprising if evolution came up with
*  that way of handling the uncertainties of the world and to compensate for delays as well from
*  your sensors and your muscle sensors all the way to the brain. So there's always going to be delays.
*  So if you're too late to react, you're probably going to get killed, right? Also, if you have the
*  ability to predict and have a model, then you can do planning, right? You could essentially go
*  forward in time and then you can do planning. And then that leads to abilities that allow you to
*  have much more sophisticated behaviors than if you're just a reactive organism, right? So I think
*  there are a lot of reasons, at least from a computational point of view, but probably also
*  from an evolutionary, biological point of view, to have something like an internal model and
*  prediction that comes with it. Okay. So Raoul and Ballard was in 1999. And then the sensorimotor
*  theory of the cortex, I think I have the name wrong, but I'll get it right and I'll flash it
*  up there, which you've recently presented, which you've been working on for, I think, a long time
*  now. Not so long. I would say maybe like four years, like three, four years. Oh, that's not
*  so long at all in terms of research age. Oh, okay. Well, so that's what I wondered. I'm not sure if
*  you flipped in that regard. It sounds like you've somewhat flipped, but if you have how that...
*  Did someone drag you out of perception or did you climb out yourself or...?
*  I think it was multiple things. So I think it was just this realization that if you think about
*  what is the purpose of having a brain, the context of evolution, right? So going back to
*  some of the early creatures that were trying to, for example, move to two or three places that have
*  more nutrients because you don't have enough nutrients. But hang on, let me just stop you
*  there. I'm so sorry to interrupt, but they're moving to a place with more nutrients because
*  they can already perceive whether there are nutrients there, right? So the movement...
*  You need perception as a way to minimize the error, right? So ultimately you're trying to minimize...
*  So perception came first. You need both, right? So you can do random movements, but you still have
*  some notion of perception because when you taste the nutrients or when you actually sample the
*  nutrients, then that is like perception, right? You're going to call it perception. So I think
*  it's kind of like the sensory and motor part are integrally tied, right? So the motor part allows
*  you to change your location or sample a different part of your environment. But then if you want to
*  know, was that successful or not, right? Then you do need sensation of some sort to know, okay,
*  what I did was good for me or bad for me, right? And that's what we're calling perception in a very
*  coarsest level, right? So do you think... All right. So I guess we have sensation without brains
*  or perception, sensation, perception. We can use them interchangeably, although that's dangerous,
*  but let's say light sensors, right? You mean artificial sensors? No, no. Well,
*  you could do artificial, but I meant biological, right? Pre-movement. I guess what I'm wondering
*  is that evolutionarily, why did brains develop? And that is in some sense,
*  moot point because they are integrated, like you said. But I think you have to perceive before
*  you can move. No, I don't think it's one or the other, right? So essentially, yeah, I mean,
*  you could say perceive because you're perceiving the fact that maybe you're low in nutrients
*  inside your body, right? So you're hungry. I mean, you could think of that as a kind of
*  internal perception, right? And that may drive you to then move, right? But then when you go out and
*  you actually consume some nutrients, then your internal state may change because you're not
*  perceiving it as, okay, I've consumed food and so I'm more... Yeah, but if you move without any
*  perception, then you can't decide... Exactly. So you do need perception, but at the same time,
*  if it's just a creature that doesn't move at all, but it's just perceiving, I mean,
*  that also doesn't quite make sense, right? Does a Venus flytrap move to you?
*  In the sense that it does have an action, right, of grabbing the insect and digesting. So I guess,
*  but it doesn't move in the sense of creatures moving, right? But in some sense, maybe it does
*  if you consider the movement. But again, it's not a moving organism, right? Like the one that we
*  associate with brains, right? Yeah. Right. Yeah.
*  It's an interesting... Go ahead.
*  Well, these are great questions to think about, right? In terms of...
*  Oh, no, I'm sorry. I'm telling you, man, I had a long motorcycle ride and my brain is fried and
*  so I'm sorry if I'm a little squishy myself. But...
*  Yeah. Back to this, what is it, 25 year divide between these two papers. I'm just going to
*  focus on these two. I think you've published in total probably four papers or something like that.
*  Slightly over. Yeah.
*  In total? Sorry. All right. So, but...
*  Yeah, I guess... In total?
*  All right. So, but it felt like a big reveal when you added the motor aspect to the predictive
*  coding. And we just talked at length about how you have come around to thinking that action and
*  motor behavior is important. So can you maybe just give a summary of how you incorporated it
*  and what people can expect if they read this paper?
*  Yeah. So I think the first observation that really prompted me to go on that whole journey
*  was the fact that there were all these new results coming in showing that even primary sensory areas
*  or quote unquote sensory areas like V1, S1 or A1 were being influenced by motor activity or actions.
*  There was papers from the Karen Dini Harris lab. There was papers from David Schneider's lab
*  showing that you can actually get these responses that are motor related, but they're happening in
*  the traditional sensory areas like V1 or A1. And not only that, but then the other interesting
*  observation was anatomically again. If you look at anatomy, the layer five cells, there's like 5A, 5B,
*  but the layer five cells, even in the primary sensory areas like V1, A1, S1, somatosensory cortex,
*  primary somatosensory, the layer five in all of these areas are sending axons to motor,
*  subcortical motor areas. Like the V1 sensitive superior colliculus, A1 sensitive inferior
*  colliculus. It's all completely connected. It's a ridiculous system for an engineer.
*  I mean, it's not completely connected in the sense that you don't have the superficial cells
*  sending axons to superior colliculus. We don't know that yet.
*  Well, okay. So there's always the possibility. But I think that was the other interesting anatomical
*  constraint that we were looking at. And then the funny thing there is, okay, it's not just that you're
*  going from layer four to layer two, three, and then to layer five. And then that's it. Now layer five
*  is sending information back to layer two, three. There's a loop there between the superficial deep
*  layers. What is that loop doing? And if the superficial layers are receiving sensory information
*  from layer four, and then the deeper layers are sending quote unquote outputs to motor centers,
*  then there is this loop going on between the sensory and motor within each cortical area.
*  And that was the first insight was, okay, what if we take some inspiration from reinforcement
*  learning? So we all know about the Markov decision process idea and the fact that there's-
*  We don't all know about it. Even for non-scientists, the most basic version.
*  Yeah. So the basic idea with reinforcement learning is that there's a world and there's
*  something called the state that the animal or agent is in. And then when you take an action,
*  that state changes. And basically, that's called a Markov assumption because you're saying the next
*  state only depends on my current state and current action. But that is typically called the forward
*  model or the dynamics of the world. You're saying the world is in this state or I'm in this state,
*  and then I take this action and the world changes to this next state. And that if you repeat that,
*  it becomes like a dynamics, like the physics of the world. And that is the forward model or what
*  we call the generative model of the world. But then reinforcement learning, the goal is to learn a
*  policy, which is given a state of the world, what is the best action I can take? So that is called
*  a policy. It's a function. So for any state the animal is in, it's going to say, okay, I want to
*  take this action because that action is the one that will let me achieve my current task.
*  And so if you now combine the model, which is at the top, and then the policy at the bottom,
*  so you have one that is making predictions of what the next state is going to be based on your
*  sensory inputs, and the other that is saying, given that I'm in this state, here's what the
*  action is that's most suitable. Then you can have this kind of a cycle between prediction, action,
*  prediction, action, prediction, action. And that is the general idea. And that's what we suggested
*  as a module, like a sensory motor module for any cortical area. And it's going to operate at its
*  own spatial temporal scale, depending on the kind of inputs it is getting. So every cortical area
*  has its own spatial temporal scale and modality, depending on the kinds of inputs it's getting and
*  the kinds of outputs it's controlling, or potentially controlling. And then the last thing
*  we threw in there was, okay, what about the different hierarchy and the different cortical
*  areas interacting? Why is there a feedback connection or a reciprocal connection? And so
*  it turns out that from a computational point of view, if you want to have a very rich way of
*  modeling the world, then what you want to do is have the higher level modulate the dynamics of
*  the lower level. So you need to change the function being computed at the lower level,
*  depending on the task. So if my task is to drive to the grocery store, then you basically want to
*  load up the program for getting into your car, figuring out where you're going, and then driving.
*  So you have all those quote unquote programs that are policies. These are these policies that
*  are already being learned, that are being plugged in to achieve your current goal. But if your goal
*  is now to go to your friend's house, it'll be similar programs, but the sequence may be different.
*  Or if it's a cook something, again, it's the same idea. You load up a different program. So
*  we're suggesting that that kind of schema or loading up new programs can be done through top
*  down modulation. Maybe prefrontal cortex loads up in the lower areas, these programs, and
*  corresponding dynamics of what to expect. All right. So we'll just say it's in the
*  prefrontal cortex. So how does the prefrontal cortex come to be that way? Yeah. So our hypothesis
*  is that it starts off with all areas operating in terms of their respective spatial and temporal
*  scales. But by the time you get to the prefrontal cortex, you have information that is now operating
*  at a much longer time scale. And the abstraction level has gotten to the point where it's now
*  operating at the level of abstract actions. So there could be a population of neurons that
*  are coding the current context or task, which is just saying right now, OK, I want to go to the
*  grocery store. That's like a goal that got instantiated at the highest level. But it's
*  maintained until that goal is achieved. And while it's being maintained, it is modulating
*  all the other areas that are involved in achieving that goal. And that involves even the basic lower
*  level somatosensory cortex, visual cortex, auditory cortex. They all now have that context from the
*  higher area saying, here's what my current goal is. Now let's see if we can achieve that goal.
*  And then you get your, I don't know what you would get, my grandmother would get cookies,
*  definitely at the grocery store. You get those cookies. And then how does it switch?
*  So the idea is it's a hierarchy. So as you achieve the sub-goals, so basically the idea is that
*  a complex problem, a complex task is split up into its sub-goals, subtasks. And those are in turn
*  split up into subtasks all the way until you get to the point where you're operating at the level
*  of milliseconds and controlling your muscles. And that's happening in the spinal cord loops.
*  So the spinal cord is controlling things at a very fast time scale. But then as you go up the
*  hierarchy through the different areas, including the midbrain, and then you go all the way up to
*  the cortex, you start to get longer and longer time scales. And then that's where you start to get
*  these subtasks being achieved. And then those in turn cause a flip to the higher levels.
*  And we go to the next goal. So you're going from one goal to the next goal to the next goal.
*  But how do those goals get programmed?
*  Yeah. So that's all about learning. So you have to learn. And that's what some people call that
*  curriculum learning in the AI literature. But as babies, after we were born, or even before we were
*  born in the wombs, we're starting to learn these modules of, okay, what happens if I move my hand
*  in this way, my arm in that way? But then once you're born, you're starting to grab objects,
*  you're trying to reach for objects, you're trying to grasp different kinds of things.
*  So you're building up this repertoire of action policies, and the corresponding dynamics that go
*  with the action policies. And the idea is as you go through learning, through your toddler years
*  and so on, you're building up a very rich set of primitives that can eventually be composed
*  for solving more and more complex problems. There's still a lot of unknowns, but I think
*  that's kind of the way to do it. Right. Right. I guess what I was asking was what...
*  I mean, I think we've all had the feeling like once you're done with a goal, you're like,
*  well, all right, what now? And you kind of feel lost for a moment until you realize what else you
*  have to do. But what I'm wondering is how those sequence of abstract goals, if you have an abstract
*  goal, how does it switch? Once you accomplish one, you got to do the next one, and then the next one.
*  Yeah. How does your prefrontal cortex go? But like you said, there's a lot of unknowns.
*  That's a wonderful question. I think in the model, at least, you start off with some higher level
*  goal, which I guess we give it, or we say, here's the task. And then the way it decomposes that is
*  as you go down each higher level abstract action or policy, it generates a function at the lower
*  level. And that function basically has as the output... So remember, functions are basically
*  state to action mappings. Each of those actions is now another abstract action, which is like a
*  sub goal. And then that in turn generates another function at the lower level, all the way down to
*  the spinal cord level. And that is what we're saying has to be learned. You have to learn
*  each of those sequences, those functions that capture the sequence of sub goals.
*  But we're saying it's the same module replicated at all the levels. And that's one of the
*  things that for me, in the Mountcastle's whole idea of the cortex has something similar across...
*  The algorithm may be similar across different cortical areas. As a theorist, you always have that
*  fascination with those kinds of ideas. And so the challenge here was, is there something like that
*  that we can come up with from a computational point of view? And then of course, the brain may
*  or may not implement it, but let's try to come up with something like that. And it turns out that
*  this active predictive coding idea seems like it is versatile enough to tackle many, many different
*  kinds of problems, but it remains to be seen how well does it map to something that the brain may
*  actually be doing. But do you believe it? Do you believe Mountcastle?
*  Yeah. Not exactly the cortical column is something where everything is. But I believe in this more
*  broader idea that if you take any piece of cortex, a chunk of it, and then you give it even to trained
*  neuroscientists, it may be hard to figure out which part of cortex that is. And of course,
*  there's motor M1 versus V1. But I think... But 90% of that is who they're connected to,
*  not what they're doing probably. Exactly. Yeah. And I think that's a really interesting finding
*  because you would think that language area should be programmed very differently from vision areas
*  and so on. If you train traditionally, you would think, okay, visual cortex is doing edge detection,
*  right? But then if you look at auditory cortex, there's no edges. So they can be doing edge
*  detection, right? You're doing something completely different. Motor cortex must be doing something
*  very different, right? But it's really intriguing if you think about it in terms of, okay, what if
*  they all have components of this kind of sensory and motor aspects to them. And it's just that in
*  some areas, some got more emphasized than others, but they still have the basic primitives, right?
*  Of sensory inference as well as motor control, right? And they're operating together at multiple
*  levels. You're a BCI, brain computer interface person, an engineer-minded person.
*  This is maybe a throwaway question, but given... All right. So what you just described is maybe it's
*  somewhere in the prefrontal cortex. There's this higher level, more abstract goal, and then it gets
*  implemented at lower and lower levels until it pans out in musculoskeletal system. If you were
*  evolution, where would you move next? Do we just get more and more abstract?
*  What does that mean, more and more abstract? What would be a more abstract goal than
*  honoring my great-great-great-great-grandmother's legacy by...
*  I don't want to be stereotypical, but by doing something the way that she would do it, right?
*  Right. Yeah. So basically you're saying, okay, what is the next evolutionary milestone?
*  What would be in 10,000 years? Yeah. How come we can't guess that?
*  Because we've been very bad at it. We can guess it, but we've been pretty bad in terms of...
*  We can't. We're very good at guessing and being wrong. Sure.
*  Yeah. So I would say, I think in terms of at least human evolution, we see that we're
*  essentially, biologically, we may not have added new cortical areas or new brain structures, but
*  we have been really making amazing strides in terms of adding tools and the cultural knowledge
*  and tools. Perfect segue, by the way, to BCI, but I'm sorry to interrupt you.
*  Yeah, exactly. So basically, I think if you think about it in terms of we basically augmented
*  ourselves. So humans augmented themselves additionally using tools like rocks and
*  made these little blades to cut meat and so on. And then we, of course, augmented ourselves in
*  terms of wheels to move faster because our legs can only go so fast. And then of course, we went
*  beyond that to... We were able to fly with airplanes more recently, right? And then similarly,
*  memory, right? So memory augmentation. So we could only hold so much in our memories, but then we
*  started writing. We had language, so we started writing things down and then we were able to pass
*  it from generation to generation. So that's another big tool in terms of cultural knowledge
*  accumulating over time. This is the most beautiful thing about language, I think.
*  Yes. It's an amazing thing which other animals unfortunately don't have. So I think that leads
*  to this idea of, okay, so if it's really tool use, and nowadays we all hang around with these
*  devices in our hands and in our pockets. And basically, we've augmented ourselves in terms
*  of knowledge and access to information with these kinds of devices, right? And so people in the BCI
*  world and brain computer interfaces think maybe there is a progression there. If you really
*  take that idea to the extreme, then if the brain itself biologically is limited in terms of its
*  speed, right? And in terms of its memory capacities, then would it make sense to then augment it with
*  artificial memories and artificial processing capacities and artificial communication capacities,
*  right? And that leads into the whole augmentation side of brain machine interfaces or brain computer
*  interfaces, which is an area that is not something most academics want to really go too much into
*  because there's a lot of ethical applications. So most of us tend to stay on the medical application
*  side, right? That's where the funding is, and that's where a lot of important contributions have
*  been made and need to be made. But there are companies and people in the tech world that are
*  really interested in that aspect, the augmentation aspect, right? Yeah, and uninterested in ethics.
*  So how do you navigate that? Yeah, so I co-direct the Center for Neurotechnology here. We were funded
*  by the NSF for about 10 years as part of an engineering research center. And we had a team,
*  a neuroethics team, right? We still have them. But during the grant, what we did was for all
*  the projects, we embedded a member from the neuroethics team into the engineering team itself,
*  right? So every engineering team that was developing a brain computer interface application had an
*  ethicist who was giving them active feedback about, okay, what is the end user going to think about
*  this? What are the long-term implications? And the engineer- And did your team hate the ethicist?
*  How did that work? I mean, I don't need to ask you how you feel personally about it because it
*  is a conundrum, I think, from a technological point of view. But that's like embedding a
*  philosopher into a research lab or something like- There were philosophers, actually, many of them.
*  Of course, of course there was. Well, that's all philosophy has left is ethics, right? No,
*  I'm just kidding. Just kidding. Okay. But yeah, I mean, was there resistance? I mean, you know-
*  No, I think there was- I don't want to have to deal with that kind of stuff, is what I'm saying.
*  And I admire you for doing it. No, I think it's important because as engineers, we're really
*  excited about building the next great thing and doing something very novel. But at the same time,
*  the consequences may not be anticipated by engineers as much as people that are more
*  trained to anticipate those consequences. Yeah, but the consequences are always bad, right?
*  Not always. I think there are some constructive things you could do. For example,
*  there were actually some interesting observations the ethicists made when they talked to the
*  families of patients that had, for example, deep brain stimulation. And many times a family member
*  provide insights that may not be very obvious. Like they may say, okay, the personality of my
*  partner changed right after they got the DBS. Or they may say, the actual patient may say,
*  sometimes I feel like I've lost my sense of agency, right? Because there's this device in there.
*  So then the question becomes, okay, what are the ways in which you could restore that sense? If it
*  gets to the point where the person feels like they've lost their sense of agency, then is it
*  okay to have a kill switch or some other way to at least provide them some relief? So there are ways
*  to have engineering solutions if you know about some of these things that the patients are going
*  through. And I think at least that's a good way to then find ways to address issues before they
*  become too bad to really address if they're commercialized. The technology gets commercialized
*  maybe too late at that point in time. So that's one of the hopes. But you're right that many
*  companies may not necessarily look into any of these issues, right? Because they're not-
*  And or like even academically and research wise. So we're talking about, you mentioned agency,
*  we're talking about concepts that not the philosophy has settled on anything ever, but
*  concepts that are very much in the air in terms of like, well, if I mean, my personality has changed,
*  but if I add a BCI or some sort of prosthetic to my brain, and then is it the
*  fault of the prosthetic or was that a deep-seated thing in me? Who's responsible and
*  ethically? I don't want to deal with it. Yeah. Those are great questions that we've been
*  talking about them and we've been discussing those. And I think it gets even more trickier
*  just think about it in terms of, okay, now we have DBS, which is open-loop stimulation,
*  just delivering some constant current. Let's talk about AI, right? So if you add AI into the picture
*  that adapts- Well, hang on before you do that. So this is something that you've done and are
*  continuing to do. So just to get, and I'll introduce this in the beginning, but I mean,
*  there's BrainNet, there's NeuroCo processors. I'm not sure how you would like to describe it
*  as sort of an introductory idea, but you've done two people, you've done three. I don't know how
*  many people have you gotten up to in terms of collaborating? Yeah. So I think the idea there,
*  so we were talking about brain-to-brain direct communication or BrainNet was when we had three
*  people collaborating directly using their brain signals to solve a problem that was, in that case,
*  was just a Tetris video game, right? And this is one person gets their, has their brain signals
*  communicated and stimulated and the other two get to interact. Right. So the idea here was,
*  the technology is not there yet in terms of actually doing brain-to-brain communication,
*  but the idea was if we take up this challenge of, okay, let's see what we can do with the
*  technology we have now as a way to spur people to talk about this technology so that they can
*  put safeguards now or at least start thinking about safeguards before it gets too far away.
*  Right. So we said, why don't we take technology we have now like EEG? So we all have, many people
*  have EEG equipment in their labs. So we can use the EEG to decode simple things like if you have
*  a flashing light, it's called steady state visually evolved potentials, you can decode
*  the frequency at which you're staring. Right. So if you're staring at two different flashing lights,
*  one of them will trigger oscillations in your visual cortex and we can decode your intention.
*  Or if you imagine making your movement, like move your hand, or imagine moving your hand,
*  you can decode that from the motor cortex. So what we said was, okay, we can use EEG for decoding
*  and let's use TMS, so transcranial magnetic stimulation, to deliver information directly
*  to the brain. Right. Which is just for people listening. TMS is like when there's a coil
*  outside of your brain and there's a pulse aimed at a very small part of your brain. It delivers a
*  non-invasive, non-damaging pulse in your brain and then depending on what function or
*  affects you, potentially affects how you think or your behavior. Yeah. And especially if you
*  deliver it to the back of your head, the visual cortex, then you see what is called a phosphine,
*  which should be a little spot of light or a bar or something like that. And so we basically used
*  a Morse code kind of idea. So the flash was just conveying binary a bit of information. Right.
*  And so we said, okay, why don't we use these primitive modes of interacting with the brain,
*  so EEG and TMS, and let's build a brain to brain, direct brain to brain communication system with
*  that. And this was several years ago. And we did some proof of concepts and published a few papers
*  on that, just as a way of not necessarily saying, look, we can actually commercialize this technology
*  because obviously we cannot, it's too bulky. But if you just think about companies that are now
*  developing implants, then you can imagine once they have implants on multiple people,
*  then they can start doing this. If they can stimulate the brain and record from the brain,
*  right? It's bi-directional BCI, bi-directional brain computer interface. Then you can start to
*  do these kinds of experiments and you can start to implement these kinds of systems of recording
*  from one brain, stimulating another brain, decoding and encoding the information in another brain and
*  so on. Right. And that's where we get into augmentation. Right. So now we're using
*  neurotechnology for augmenting, in this case, the communicative and processing capacity of the human
*  brain. So where are you now, right now with these? Right. So once again, I think we are not in the
*  business of really going on the commercial route. So what we're doing is a lot of theory. So what
*  we're talking about- Oh, is that what people usually ask you that? And their question is really
*  what future human are you creating? Is that their question? Yeah. I mean, some people are
*  very much interested in that, the singularity and things like that. Right. What's that going to be
*  in the future? Of course, there's some people who want to merge with AI. So that's the whole other
*  crowd, right? Who want to actually- Are you going to? Do you want to merge with AI? No, not really.
*  I don't either. Yeah. I don't understand it. But I think what we're doing is in some sense,
*  we're saying, okay, if you really are thinking about processing information from the brain and
*  making sense of it and sending information back to the brain, that's what we call a co-processor
*  for a brain. That's what we're working on is a brain co-processor, which is this idea that
*  there's a device that is essentially a tool for the brain that can both decode information from
*  the brain and encode information back into the brain. So what that means is like, so it's
*  listening to the brain and then it goes into an algorithm in it. Well, in terms of modern AI,
*  it categorizes what that brain process is signaling. That was almost that understands it
*  and then transforms it into a signal to inject into the brain. I'm sorry if these are too
*  low-level descriptions, but- Right. I think that's one way to think about it. And of course,
*  the way it would have to work would be that co-processor has to have AI in it of some form.
*  And so we suggested a neural co-processor, which was a neural network. So an artificial neural
*  network. And so what we have there is an interaction between artificial and biological
*  neural networks where both of them are adapting. So it's a co-adaptive system. And the challenge
*  there is how do they co-adapt to really achieve a goal? And from a medical point of view, if you,
*  for example, are trying to replace lost function, like somebody had stroke and you want to be able
*  to restore their movement, then this could be a device that could replace that lost function of
*  the cortical or other subcortical circuitry. And the AI has to train itself and the person now has
*  to command this AI replacement circuit to do what the person wants it to do. So then that becomes
*  an interesting AI problem. So how do you ensure that the communication between the human brain
*  and this artificial device achieves a common goal? And that's what we did with the neural co-processor
*  was we said, hey, look, if the goal is, for example, to reach for an object when the person
*  cannot reach the object, but then you can stimulate, let's say, the spinal cord and make
*  the person reach that particular object, then the error is now in the space of visual error.
*  So there's an error signal. Can you do back propagation, for example, which is a standard
*  thing people do in AI? But the problem is back propagation here, you'd have to do it through
*  your body and your brain. You have to do it through the body.
*  That's not back propagation by definition.
*  Yeah. But I mean, in terms of ideally, if you want to train your neural network,
*  that's delivering the stimulation, then you have to get that error signal somehow. And the error
*  signal, unfortunately, is now in the space of an external task. So what we suggested was, okay,
*  for all of these AIs, they need to have an internal model, this forward model of, in this case,
*  your brain dynamics. So how your brain reacts to stimulation. So it's like a forward model of
*  the action here is stimulation. And then it's going to cause your brain dynamics to move in
*  a particular way. And if you're able to predict that dynamics, then you can come up with the best
*  stimulation to give for achieving a particular goal. So it becomes, again, a control problem.
*  How imperfect can... So I mean, these are things I just... I'm a neuroscientist, but I ponder these
*  things. I mean, one of the most amazing things about the brain is how adaptive it is. And
*  sometimes I think, well, maybe that is the function of the function as if there was a function. But
*  the adaptability is almost the answer. And so what I was going to ask is,
*  how wrong can it be for the brain to still be able to deal with it? Is that a testable question?
*  How bad can you make the signal relative to how quickly the brain can learn it? That's a terrible,
*  poorly phrased question. I'm sorry. It's actually a very important question,
*  especially in the sensory stimulation area. So people that are trying to restore the sense of
*  touch, for example, from an artificial prosthetic device, stimulating the somatosensory cortex.
*  There's a big question there in terms of, should we make the stimulation be as natural as possible? So
*  we make the sense of touch. When you stimulate the somatosensory cortex,
*  you typically... Patients typically report, okay, I feel like it's pins and needles.
*  It's not quite the nice sense of touch I get when I use my own hand.
*  And then you say, well, just wait a week or two and it won't be, or something like that.
*  Some people would say, hey, you're just not used to it. It's a novel signal right now. But if you
*  keep using it, maybe you get used to it and that becomes a natural sense of touch.
*  This is like training. This is like trying to convince my children that, oh, don't worry,
*  keep practicing. It'll get easier. But it sounds pretty painful.
*  Painful is a key part there because if you are not really delivering, quote, unquote,
*  naturalistic stimuli, then it may take much, much longer for you to learn. So I think there's a
*  trade-off there in terms of if you're able to speak the language of the brain in some way,
*  basically you're delivering the pulses, electrical stimulation, optical stimulation, the way that the
*  brain can parse it more easily, then you may be able to learn much more quickly than if it's an
*  artificial set of pulses like stimuli. I think that's an interesting problem.
*  In terms of natural, then, is that just noise or is it the natural statistics of the world?
*  It's more the way that the neurons in that particular area are receiving information
*  from other neurons. For example, if you know that in the population level, there's a particular
*  set of frequencies that are operating at that scale, like beta frequency oscillations or
*  something. So then you can think of delivering the stimulation at some particular phase of that
*  oscillation or you're trying to synchronize with that oscillation. Maybe that is better than you
*  just delivering it irrespective of what's happening in that brain area. So the bottom line is you need
*  to be recording as well as stimulating. You can't just be stimulating the brain area. You need to
*  be recording to know what's happening in that brain area and then change the stimulation according
*  to what's happening at that point in time to consistently deliver intelligible stimulation.
*  But within a window because that's antithetical to the idea that the brain can handle a bunch of
*  wide range. So a brain area doesn't get to decide the signal incoming. But what you just said is that
*  you need to do it in a way that it's expecting it. It's a very predictive coding outlook, by the way.
*  Otherwise, it might not work. Yeah, it's a way to enable the brain to learn faster. Like I said,
*  it's possible that you could not pay attention, just keep delivering something and eventually
*  the brain may figure out how to interpret that stimulation pattern. But the question is how long
*  will that take? It may happen quickly or it may take very, very long or maybe it'll take forever.
*  In general, it makes sense to have some feedback about what's happening in that brain area and as
*  you're delivering the stimulation. Can we partially get to this by doing learning studies and maybe
*  just probing the historical literature and learning studies? Modern learning studies are
*  becoming more better and better. And I don't know if there is an answer to the proper way to learn
*  X yet, like the most optimal. I know that there's a lot of people who make a lot of money who say
*  that there is. But I sort of intuitively think it's got to feel really bad at first and that's how
*  you're going to eventually learn. But it also depends on the goal. But do you think that we can,
*  is this an experimentally behaviorally tractable problem that could help answer these issues?
*  Because you're speaking about the activity in the brain, but then we're eventually talking about
*  behavior. Yeah, it's an interesting question in terms of how do you study what's happening
*  as the brain is interacting now with this external device that is sending direct input into the brain.
*  Or it's just the optimal input if you're going to use these external devices.
*  And so the neural core processor idea was one way to get at it in terms of saying,
*  if you are able to adapt the neural network that's delivering the stimulation to minimize the error
*  in the external staff space, then you're leaving the brain of having to do a lot of that learning.
*  But of course, the brain is already trying to learn. So it will be changing. It's a non-stationary
*  system, which is why we call it a co-adaptive system. And that's where it becomes tricky.
*  So if it's only one side is adaptive, let's say the brain is adaptive, but then you have a fixed
*  mapping for your stimulation pattern, then all the burden is on the brain to learn that.
*  But then if you do it where both the systems are able to adapt, then the challenge is,
*  can you make it... They're both optimizing the same cost function or same optimization function.
*  And that's where the interesting engineering challenge is, to make it a co-adaptive,
*  co-evolving system. And that's where I think the future is probably going to go if you're going to
*  use AI for these brain computer interfaces. You want to do a quick segment of epiphenomenon
*  or causal? What was that again? You want to do a quick segment of, is this an epiphenomenon or
*  is it causal? Oh, okay. Like a quiz? Ready? Yeah. Yeah. Opinion. Ready? Oscillations.
*  It's... I would say it's causal. Yeah. Consciousness. Epiphenomenon.
*  Oh my God. We're done. I just heard someone say that.
*  But I'm taking the most liberal definition there.
*  Okay. Those are the only two. I heard someone I respect say
*  consciousness was epiphenomenal and then you were talking about oscillations.
*  I just want to be a little bit on that cutting edge there. So yeah, let's go with that.
*  Okay. All right. Great. That's staying in by the way. I'm not going to edit that out
*  unless you force me to. Sure.
*  Okay. Before we... So, all right. So I'm looking at the time right now. And first of all,
*  what have we missed about the neural... I'm going to point everyone to all of your work, but
*  I've been punchy in jumping around. So what have we missed in terms of the neural coprocessing
*  and or brain net and the... We haven't used the term telepathy, right? Which is sort of the coup
*  de grace, the pinnacle, what people... The spooky term, right? That these things imply. I mean,
*  is that a goal? Well, I'm going to stop interjecting. What have we missed in terms
*  of what we haven't spoken about with the neural coprocessors?
*  Yeah. So the neural coprocessor idea, there was relationships to the brain to brain communication
*  work that we had done early on, right? And that work of course got us both people that were
*  quite interested and quite intrigued by it, but also I think a lot of scientists were like,
*  oh yeah, that's just the old using TMS is like frogs legs being stimulated, right? So
*  we got people saying, why did you even do that? I think that... Oh, really? Yeah. So the main point
*  is it's not that we were claiming that, hey, this is like a grand new discovery or invention, right?
*  The idea was to say, okay, we have been talking about things like mind to mind communication or
*  telepathy for a long time in science fiction, right? And then the DCI really progressing at
*  the rate that it's progressing with companies getting interested in it. This may be a good time
*  to have that conversation, right? And I think one of the interesting things there is we may actually
*  get something like very primitive forms of brain to brain communication if these companies have
*  multiple patients with implants, right? Because it doesn't take much to send really simple kinds
*  of information from one person's brain to another as soon as you have the ability to stimulate,
*  right? Which is something I haven't seen yet. But once that starts happening, then I think it's
*  only a small step towards starting some really primitive kinds of what you may call like... I
*  mean, I'm sure the companies will claim is telepathy, right? But yeah. They'll be called tele...
*  What will they be called? Because there was the telephone beforehand. What would be a good
*  company name for that? Right, right. Yeah. So for this one, it will be like teleneuronics or something
*  like that, right? Yeah. Why can't we come up with something, Raj? I mean, this is...
*  I'll think about it. Yeah. It's going to have to be trademarked first before we can talk about it.
*  No, I'm just kidding. So... I know you have it. You have it in your back pocket and you're not
*  letting on. But yeah, I think the unfortunate consequence of some of these kinds of claims
*  by companies and even I think some of the experiments that we've done is that there's
*  a lot of people who are probably schizophrenics who think that they are implanted with these
*  kinds of devices already. And so a lot of us get emails every day, right? From people saying,
*  hey, can you help us? Do you think the government has implanted something in me or there's a chip
*  in my brain? Or the Lord did, you know? Yeah. I mean, people actually even come to campus,
*  right? So there are people who have driven miles just to come to campus to our center to say,
*  hey, the doctor says there's nothing there. Here's an X-ray. There's nothing in the X-ray.
*  But I firmly believe it's this microscopic thing that's in my brain that's controlling
*  my actions, right? So unfortunately, I think that's the price you have to pay. You start to push that
*  frontier. There's going to be people who also think that that's happening to them, even though
*  we can assure them that that's not really possible at this point in time, right? And we don't have
*  the technology to do something like that. But that is something we are faced with as well. So
*  it's part of the whole ethical issue and communication issues with this field.
*  Yeah. So you said that we can't telepathically communicate yet, and we can't stimulate each
*  other's brains, what we do all the time. You and I are doing it right now through language.
*  Yeah. And you have an interest in... I don't know where your interest in
*  the Indus script came from. And or now at some point, you learned a ton about language
*  and just how language works and some of the statistical properties that are indicative
*  of what a language is. So is this a hobby of yours? It's beyond a hobby now, but how did you
*  get involved in the Indus script and determining, trying to decipher this thing?
*  Yeah. I've always been interested in ancient history. And so it was during one of my sabbaticals,
*  I think my first sabbatical when I said, okay, now what if I indulge in that fascination with
*  ancient history, right? And especially ancient Indian history because I'm from India. And we
*  have the civilization there that's more than 4,000 years old that we know very little about,
*  partly because the script of that civilization is not yet deciphered. And this was a civilization
*  that was much bigger than the Egyptian and the Mesopotamian civilization.
*  So I took... I'm sorry to interrupt, but one of my favorite classes that I took when I was
*  an undergraduate was the origins of writing. Denise Schmalte-Bessourette taught the course,
*  and we learned all about cuneiform and how early writing might have been
*  been brought about by economic exchanges with little clay tablets where people put little marks
*  to show how many goats or cattle that need to be owed or exchanged and stuff. Where does this...
*  And I can't remember how... So what you're talking about is for... There's like 2000 BC.
*  Yeah. Before that, I think starting from probably 2800 BC is when they believed the civilization
*  started evolving to the point where it was mature enough and then it ended or the demise
*  of the civilization started to be more like 1800 BC, like 2000 to 1800 BC. But the curious thing
*  about them is that the... That was not... Yeah, it was not like a huge amount of time. And there
*  were some precursors, 3000 BC and so on, but the prime of the civilization and they were really...
*  In their prime was probably 2800 to 1800 or so, like 1500 BC. And I think the interesting thing
*  about the civilization is the fact that they were actually trading actively with the Mesopotamian
*  civilization, the Sumerians and those civilizations in the Middle East. And they've found these seals.
*  You mentioned they had these stamp seals so you can stamp information about typically trade
*  the kind of goods that they may have been stamped on. So I think the intriguing thing there is,
*  of course, we know cuneiform and the kind of history of writing did evolve from the Middle
*  East, right? And then the Egyptians, of course, followed suit with their hieroglyphics.
*  And it's believed that the Indus civilization also evolved their own set of symbols, about 500
*  to 700 symbols that are very pictographic in many cases. And unfortunately, there are no long
*  inscriptions. So most of the inscriptions they've found have been on these stamp seals,
*  which are only about five symbols long on average. Some of them kind of squished in different...
*  Yeah. So there's usually an animal imprint, which may have been like a symbol of a clan,
*  like a unicorn is the most common animal symbol. Really? Yes, a unicorn, yes. But people
*  in ancient times thought it originated in India, right? So unicorns. I didn't know that.
*  I didn't know that. Yeah. Yeah. So perhaps it was because of the Indus civilization and their seals,
*  right? But the seals always had at the very top a set of symbols, a sequence of symbols,
*  which were typically on average length five symbols long. But there have been no long
*  inscriptions on tablets. And so unfortunately, we cannot apply many of our AI techniques, right?
*  Because there's only about 6,000 of these. Right. How do you tokenize that? Yeah.
*  Right. But what we did do, we did do some kind of analysis of it, which is we looked at the
*  entropies, the block entropy of these symbol sequences in terms of which symbol follows
*  which other symbol sequence. And then we showed that the block entropies tend to match the block
*  entropies of linguistic scripts, as opposed to DNA, for example, or proteins, which are much more,
*  quote unquote, random. They're more flexible, right? So the entropies are much higher.
*  Music is slightly about language, right? So music is a little is more flexible,
*  but not as much as DNA or proteins. What's less flexible?
*  Least flexible is computer programming languages like Fortran, right? It's below.
*  You're going to say Fortran. Yeah. That was the original one that they did, right? So we followed
*  that. But I'm sure it may start to fall, especially with now different kinds of
*  programming languages. Naturalistic.
*  Naturalistic. You're probably getting closer to the entropy of natural languages, right? But
*  it's an interesting way to think about it. So what we did was said, okay, here's an
*  und deciphered script. Let's look at all the symbol sequences and see if they fall in any
*  of those ranges. And it turned out that they fall right in the middle of the range of linguistic
*  scripts, which means that perhaps there's at least one piece of evidence that they may have
*  used it to encode a language. But we still don't know what language that was. There's a huge
*  political debate in India about whether it was the Indo-Aryan language Sanskrit as a
*  derogatory civilization, or is it the South Indians have a Dravidian language family?
*  So some people think it's that language that's encoded in there.
*  Political factions are trying to claim it or something?
*  In some sense, yeah. In some sense, there's that. There's also this notion of Aryan invaders coming
*  to India. People don't like that, right? Any kind of migration to India, especially if it was these
*  Indo-European invaders coming to India. That was the original colonial interpretation of it. But
*  the genetic evidence seems to indicate there was actually migrations happening from Central Asia
*  into India. And that's possibly how these languages like Sanskrit and many of the North
*  Indian languages have similarities in grammar with the Indo-European language family,
*  compared to the South, which is more Dravidian language family, which is not related
*  to the North Indian language families. So there's some amount of friction there.
*  And even now, you'll see people claiming decipherment of the Vedas in the seals.
*  But you're an expert now, so you can judge those things, right?
*  To some extent, yeah. I've definitely delved into that for a long time now. I can look into it.
*  And unfortunately, most of the time, you can see that they're stretching it. And it's just not a
*  plausible decipherment. So I think you're just going to have to wait for more excavations and
*  maybe a Indus Rosetta stone that'll help us decipher that script.
*  But I doubt we'll find it. Do you think we'll find it?
*  No. I mean, it's a difficult task. I mean, it's possible it's already been found and it's just
*  lying in some warehouse in Iraq somewhere in a museum because they were trading with these folks.
*  So maybe there were some inscriptions that had both cuneiform and the Indus script.
*  But so far, nobody has found anything like that. They have found Indus scripts with really odd
*  sequences. So it seems like they were using the Indus script to express the language in Iraq,
*  like a foreign language maybe in... Yeah. So that's really interesting.
*  But they're only with five characters?
*  But the simple sequences are very different from what you'd find in the Indus
*  Valley, in the finds there. So they were using it in a different way, at least.
*  So I think there are some really intriguing suggestions like that.
*  So is this going to be a lifelong project for you?
*  For me, I mean, I think at this point, it's kind of... It's been from being a hobby to more of
*  really getting drawn into the literature and the history of it. And so I do spend a lot of time
*  reading about it. But yeah, but I have no funding for it. And it's more of a sabbatical project,
*  where it keeps me interested in something very different from what I typically do.
*  I sort of look at myself as somebody who's interested in the past, which is this Indus
*  script. And then the present is like, okay, let's figure the brain out. And then the future is like
*  the BCI augmentations. I like to keep looking at all of those aspects. And it keeps
*  my brain at least occupied and interested. So one obvious question to me then is,
*  I mean, not many people who use or... Sorry, not many people who engineer large language models
*  are linguists or have a sense of what language is or how it may have come about or its early
*  post origins, etc. Or even its origins. I mean, has this affected how you think about
*  large language models? And I'll preface this also by saying that whatever great AI model is working,
*  people are going to say, well, maybe the brain is like that. And then map whatever AI model is
*  currently working to brain processes. And often it works and stuff. So has this affected how
*  you think about large language models? Or how do you situate how you think about large language
*  models maybe is a better question. Yeah, I was quite intrigued. I mean, when the paper came out,
*  the attention was all you need paper. And then also the fact that prediction was a very key aspect
*  of it, right? Yeah, you must have been elated about that. Yeah. So it was basically predictive
*  coding except for the fact that they were not using the prediction errors to do inference. I
*  mean, there was no update of the internal representation. But the learning was obviously
*  driven by prediction errors, right? And the fact that there was a hierarchy there as well. So that
*  there's these soft attention layers, which is building up these dynamic representations over
*  time. And you're doing sending out the representation to every layer, like every time. I mean,
*  it's just massive, right? Exactly. But it's sort of, in some sense, beautiful probably to you.
*  Yeah, it was actually very interesting to know that there's now this artificial system that
*  just purely based on prediction, right? By predicting the next word, it was able to do so
*  much. Not even recurrent. There's no feedback. Yeah. Well, that's true. It's not a regressive
*  model. But yeah, you're right. But effectively, it was like taking into account everything in the
*  past. Well, processing the future and the future and the past were all getting processed
*  simultaneously, right? But I think the cool thing there was the fact that yeah, it was able to
*  really learn these very impressive predictive models and then generate these sequences,
*  which seemed to be quite in line with the kind of thing we were thinking about for our
*  active predictive coding model. This idea that there's a sensory processing aspect that's
*  constantly predicting the next state based on the previous state and action. But there was no action
*  here. The action was missing. Action is just output. It's just like a token, basically. The
*  previous token maybe being put in. All the tokens in the past are being used to process the current
*  token. But I think that that's also something that's missing. In my sense, the controller is
*  missing. So in the active predictive coding architecture, there's a policy network that is
*  controlling the generation of the next input. So we have the predictive network and the controller
*  network, and they're closely interacting with each other. And depending on the task, the controller
*  network is feeding in the action to the predictive network saying, okay, generate this next,
*  because I'm going to take this action. And I think we've lost that in the transformer model.
*  And I think that's where some of these RL approaches they're applying now to the
*  transformer models. It's kind of getting the controller back in the picture. So I think
*  that's where I see a relationship. And more recently, people have shown that transformer
*  networks implement a special kind of hyper networks, which is what we are using for active
*  predictive coding. So when I said that the higher areas are modulating, the lower areas in active
*  predictive coding, the higher cortical areas may be modulating the function being computed at the
*  lower areas. That is basically what is called a hyper network in the AI literature, where the
*  vector, an input at the higher level is transformed by a neural network called a hyper network to
*  another neural network, which is the function. It's basically a whole new network is being
*  generated. And it appears that transformers are doing something like that in a simple way,
*  like a linear hyper network model. So I think if that's true, then I would say there's probably a
*  closer link between what we've suggested and what transformers are doing, except we were trying to
*  model the cortical architecture in terms of hierarchy and laminar structure. Transformers
*  don't have that, and they don't have the controller aspect either.
*  Yeah. So then overall, our transformers, I'm trying to get a sense of your judgment on them.
*  I would say they're great, but they're not enough. They're great as a principle of how predictive
*  models can really capture a lot of information about the, essentially the statistics of the
*  world. The physics of the world or the dynamics of the world, they can be used to capture that,
*  but that's not enough for intelligence. So I would say, I go back to that notion that people
*  have suggested, Paul Cizek and Zaki and others, that ultimately it's all about actions and
*  movements. And so if you don't have the controller there telling you what to do, then you... Transformers
*  don't have like chat GPT and transformer, they don't have a sense of agency. And that comes...
*  How do you get that?
*  What's that?
*  How do you get that? How do you get a sense of agency?
*  Well, I think we get it from being able to act in the world and being able to actively
*  use action as a way to generate language. And we get that because we actually act upon the world
*  and we use speech, and that's actual motor actions.
*  Yeah, but squirrels have agency, and they don't have speech.
*  Yeah. So you have to have action. You don't have to have speech, but in order to have agency,
*  you need to be able to act upon the world and be able to cause consequences. You have to be able
*  to see the consequences of your action and then maybe achieve goals. So you start to see, okay,
*  if I take these actions, I achieve my goals. And then if I do these actions, I get something else.
*  And that's how you build a sense of agency. And then for a purely predictive system,
*  which is only predicting, but not really using actions as a way to guide those predictions and
*  get to a particular goal, then it becomes hard to argue it has agency. I mean, some people do,
*  but I think it's a missing piece. So you think that we could build agency?
*  Yeah. I think any system that starts to interact with the world with its own actions and generate
*  goals, those are all things that you associate with an agent. So I think you do require to
*  have that policy or controller and potentially a model of the world to go along with it.
*  I have two more questions for you and I promise I'll let you go.
*  Way earlier. I'm sorry?
*  Well, it's been fun, so I could probably go on. So yeah, go ahead.
*  Okay. I have to be up for the... I'm doing a brain initiative workshop tomorrow where I
*  am participating. So I have to like... Yeah. One, so way earlier on, we were talking
*  when we were talking about active predictive coding or predictive processing. In general,
*  you were talking about back then, back in 1999, when people... I said we were recording single
*  neurons and that's when I grew up, I recorded single neurons. And the technology wasn't quite
*  there to be able to begin testing the hypotheses that might be issued from a theoretical framework
*  like predictive coding. Since then, we now have... We're starting to get connectomes, which
*  everyone always said, like, well, man, once we have a map of all the connections, we can do
*  everything. And that is starting to come to pass. We now have super high density
*  recording techniques, neuronal recording techniques, so that we can put high density
*  electrodes in different parts of the brain and get lots and lots of neurons.
*  Between those two... Okay. And then now... And we have... Sorry. There's like five things, right?
*  Those two. And then we have AI models. We have high compute. We have lots of
*  a lot more statistical models that we can employ. That's the same as AI in terms of modeling.
*  Which of those, if any, has been... Do you think is the most important that is happening right now?
*  That's a trick question because I think if I choose one, it's probably going to alienate
*  a whole bunch of people working on the others. I would say we need all...
*  No, no, no. Okay. I'll ask it differently. I'll ask it differently. Which of those do you...
*  Like when you wake up, you're like, oh man, I could use this to do that.
*  In your current... I know they're all necessary and awesome.
*  Yes. Yeah. I think it changes. For me, the amazing part, it's a fantastic time to be a
*  theoretician in neuroscience right now because there's so much data. And this is a great time
*  to really think about these larger scale theories. When I was a grad student, there were books
*  and papers by Mumford. There was a book called Large Scale Neural Theories of the Brain by
*  Christophe Koch and Joel Davis. And these were all like at that time, there were these theories,
*  but then the data just was not there to test these theories. But now I think we're at a time
*  where we can actually start to test some of these theories. So I would say from one day to another,
*  I feel like some days when I'm thinking about a particular theory, I may go into the literature
*  on large scale neural recordings, really try to find, okay, is this supported or not? And what
*  are the things out there? But then the next day I'm actually be looking at connectomics to see,
*  okay, is the connectivity and anatomy still... Is that there to support some of these other
*  theories? And of course, AI is a wellspring of new ideas always. There's so much going on in AI that
*  it's hard to keep up. But then of course, there's some gems there that you can pick out and then
*  see if that's relevant to understanding the brain. So I think it just feels like we're at a time
*  where it's this explosion of information and really to make advances, it's almost like you
*  have to train your brain to essentially forage and find the right kinds of information to really
*  build up new theories. It's a tough task, but I think it's actually better than not having any
*  data. When I was a grad student, we didn't really have that kind of data. We had, like you said,
*  single neuron responses and so on. It was very difficult to say, okay, what's the system doing,
*  the systems level? Now I think we're getting to the point where we can actively collaborate. I think
*  your generation, the generation that's actually training right now, they're much more, I think,
*  savvy with computational models. They're much more receptive. Oh yeah. Computational models.
*  I think that's really great. That means that these ideas like predictive coding hopefully
*  can be tested more quickly and they're not going to lie dormant for 10 years before people start
*  taking an interest in them. So I feel like this is a great time for people. I encourage people in
*  many different areas. They can be computer scientists, they can be people doing AI, they
*  can be people in neuroscience, psychology. I think they should all feel comfortable with coming up
*  with theories and computational models. I think we have the training now in many areas, but this
*  is a great time to start thinking big. Think across just one area and one region. There's maybe a
*  paradox here. If you have tons and tons of tools, it may be harder to think big. It may be harder
*  to think theoretically. I'm wondering how you might think to foster someone's theoretical bent
*  or how to think theoretically given this deluge of tools. Yeah, so that's a great question again.
*  So I think it's something that for me at least it comes from thinking about it first from a
*  computational point of view saying, okay, here's a particular problem that, you know, let's see if we
*  think of solving this problem, how would you do that from a normative point of view or from an AI
*  point of view? But then I think you can then say, okay, let's look at some of the data from the
*  brain in terms of where these kinds of problems have been explored. And then that's one way to
*  do it is to start from the computational and then go more deeper and deeper into the neuroscience.
*  The other way is to go bottom up. So you could say, okay, I'm working on these areas,
*  but then I want to actually go beyond just this one area from a theoretical point of view. Even
*  though I'm just recording from this area, but let's think of it in terms of this area interacting
*  with all the other areas that are connected to it. And then the bigger picture of behavior,
*  right? And how is that going to work? Right? And so maybe look at people working in those other
*  areas as well. Right? It is a hard problem, but I think it's worth looking at it beyond just,
*  I remember like when I was a postdoc, I went to the lab of a very famous neuroscientist. And then,
*  I was asking- Sanowski? Is it?
*  Oh no, maybe I was doing a postdoc in Sanowski's lab in Salk, but I was visiting another lab
*  somewhere else. Okay. That's a different famous nerd.
*  Yes. There was another, I was doing a postdoc in Terry's lab, but then I went to a different,
*  visiting a lab, right? Many different labs were visiting at that time as a theoretician.
*  And then I was asking them, hey, the person who was working in V1. And then so I said, okay,
*  what about V2? Right? I mean, V2 and V1 are connected. Shouldn't you be considering the
*  interactions between the two? But the person said, no, no, I'm going to figure out V1 first,
*  after I understand V1. And then I'm going to understand V2. Right? But what if you cannot do
*  that? Right? What if we cannot reduce, it's not a reducibility in that sense. Right? What if V1's
*  properties are intimately connected with V2 and other structures? Right? Then it becomes
*  really hard to understand just one area. Right? So I think that's the challenge we have, right?
*  As neuroscientists is, the brain is a very complex piece of machinery that's been evolving or
*  millennia. And if you use sort of reductionism, then it becomes very hard to understand what's
*  happening across the brain. At the same time, maybe we don't have the capacity to understand
*  the whole brain, like what's happening everywhere. So then we have to find ways of picking the right
*  abstraction level to understand and hopefully connect those abstraction levels, like from the
*  behavioral level all the way down to like the molecules. Right? But one person may not be able
*  to do all of that. But hopefully as a community, we can start to understand the brain at multiple
*  levels of understanding.
*  It's hard. It's hard. And even people like you who are like super good at it,
*  you will admit it, it's a little difficult.
*  Definitely. Yeah. Especially with all the information that's now coming out and trying to.
*  But I don't think we can lose hope. So I'm optimistic that it's going to happen. I don't
*  know if it's in my lifetime, but I think we're on our way. It may be sooner than we think. So
*  I think we should be optimistic about that.
*  All right. Well, that's a great note to end it on. I meant to mention this at the top.
*  What I'm going to do when we're done here, I'm going to email you an invitation to join me again,
*  because I know it takes about a year to get you on. So
*  it took a long time to get you on. But man, I really appreciate it Raj, you coming on.
*  It was fun. Yeah, it was fun. Thanks again for having me.
*  Yeah.
*  Brain Inspired is powered by The Transmitter, an online publication that aims to deliver useful
*  information, insights, and tools to build bridges across neuroscience and advanced research.
*  Visit the transmitter.org to explore the latest neuroscience news and perspectives
*  written by journalists and scientists. If you value Brain Inspired, support it through Patreon
*  to access full length episodes, join our discord community, and even influence why invite to the
*  podcast. Go to braininspired.co to learn more. The music you're hearing is Little Wing performed
*  by Kyle Donovan. Thank you for your support. See you next time.
*  Bye.

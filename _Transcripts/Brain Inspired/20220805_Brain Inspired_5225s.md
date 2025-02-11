---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5225s
Video Keywords: []
Video Views: 1217
Video Rating: None
---

# BI 143 Rodolphe Sepulchre: Mixed Feedback Control
**Brain Inspired:** [August 05, 2022](https://www.youtube.com/watch?v=hKYGq0FY9YQ)
*  Maybe it was the first time where I got such a sense that science is historical and this
*  is something that is very close to my heart.
*  And you know, it's really a human adventure.
*  My view is that, you know, the digital age is just a moment, another moment in history
*  that very soon we're going to go back to something which is much more mixed.
*  But I think we see that happening already.
*  At the end of the day, the only thing that makes it possible for you to work in isolation
*  is to believe in what you're working on.
*  This is Brain Inspired.
*  Hello, everyone.
*  I'm Paul.
*  On today's episode, I'm joined by Rodolphe Seppelkre.
*  So Rodolphe is a control engineer and theorist at University of Cambridge.
*  And today we discuss a range of topics around his work using control theory, specifically
*  using a mix of positive and negative feedback control to model and build circuits that mimic
*  the mixed digital and analog signals in our brains.
*  So neurons, they're special because they spike, they emit action potentials, right?
*  They're digital.
*  Much of neuroscience is devoted to counting spikes, doing statistics on spikes and correlating
*  spikes with behaviors.
*  I counted spikes during most of my career.
*  Spikes inspired the McCulloch-Pitts artificial neurons, which would output a one or a zero,
*  binary, digital, which led to, well, you know, deep learning.
*  But spiking isn't all neurons do.
*  Their membranes have continuous analog voltage signals that are usually considered only in
*  relation to whether a neuron will or won't spike.
*  But that membrane voltage is sensitive to things like neuromodulators, ion concentrations,
*  and so on.
*  According to Rodolf, the mixed digital and analog signals of neurons remind him of good
*  old-fashioned control theory, and specifically a mixed feedback kind of control, mixed positive
*  and negative feedback control.
*  So he has been modeling single neurons as mixed feedback control systems and began building
*  up to small circuits of neurons that are further regulated by neuromodulation.
*  In fact, much of his work has focused on modeling a small-ish circuit of neurons in
*  lobsters and crabs called the stomatogastric ganglia, or STG.
*  So you may remember Eve Martyr from episode 130, who's been studying the STG for many
*  years and famously showed it can function within a normal range despite wide variations
*  in environmental conditions.
*  Despite individual neurons behaving quite differently, the system as a whole remains
*  steady.
*  It turns out Rodolf's mixed feedback control approach may be a great way to understand
*  how the STG does this.
*  Anyway, we talk about all that.
*  We discuss Rodolf's recent plunge into building these principles into neuromorphic chips,
*  which he sees as the future and kind of the present.
*  We discuss a little control theory history.
*  It turns out the mixed feedback control has always been there, even though since the early
*  days of cybernetics, we tended to focus on negative feedback control.
*  We talk about how, quote, if you wish to contribute original work, be prepared to face loneliness,
*  and a handful of other topics as well.
*  If you like this topic, you may want to visit or revisit episode 119 with Henry Yin and
*  his views on what cybernetics got wrong and his perspective on control theory and brains
*  and or episode 130 with Eve Martyr, whom I mentioned before.
*  If you want to dive deeper into Rodolf's work, go to the show notes at braininspired.co
*  slash podcast slash 143.
*  If you want to express support for the Brain Inspired podcast, go to braininspired.co and
*  check out Patreon or my online course all about neuro AI.
*  There's a free short video series that you can sign up for.
*  I hope you're all doing well, staying in control, sometimes getting a little out of control perhaps.
*  All right, here's Rodolf.
*  So Rodolf, are you, do you consider yourself a control engineer?
*  Do I have, if I asked you what you do, would you say you're a control engineer?
*  I would be flattered.
*  Many people think that I'm sort of a theoretician, but I think that control is really an engineering science.
*  Engineering is about building things.
*  Right, OK, so that leads directly to my next question.
*  Well, maybe first, then I would ask what a control engineer is.
*  How would you describe what a control engineer is?
*  Right, that's a good question.
*  I often joke that control is to engineering what philosophy is to humanities.
*  So many people, I mean, on the surface, you might think it's pretty useless, but at the end of the day,
*  it is the foundation of any engineering development, I would say.
*  Why would you think that, I know it's a joke, but why would you think that it's useless?
*  I know that the history of control has ups and downs within the engineering field, but it seems fairly central.
*  It depends on the place.
*  But certainly, you know, if you speak to control theories nowadays, many of them,
*  I think, have a little bit of difficulty placing themselves with respect to striving
*  fears like machine learning, optimization.
*  But I think that control is really great and very important, especially nowadays.
*  And perhaps the reason why some people might think it's useless, it's because, you know,
*  all the central concepts of control, like, for instance, feedback, are almost daily life concepts.
*  And so you wonder whether you really need a theory for that.
*  And then when you start doing the theory, it all sounds very mathematical.
*  And it looks like there is a huge gap between, you know, the control problems that you start introducing in a basic course
*  and then the mathematical theory that goes to address those questions.
*  But at the end of the day, I think it's one of the few courses in an engineering curriculum where you go the whole line,
*  the whole way from, I mean, I would say you see the value of abstraction,
*  that you see the value of abstraction, but to address very concrete questions.
*  I think that's perhaps what I like about control.
*  You mentioned machine learning. Is there no room for control theorists and machine learning at the moment?
*  Of course, of course. But there is a temptation to become a machine learner, you know,
*  and I think the challenge is to bring your expertise and as opposed to trying to, you know, to become someone different.
*  At the end of the day, I think we need all expertise and all expertise are valuable.
*  But there's always a balance between being sort of faithful to your expertise,
*  which I think is where you can make a difference if you really because this is your competitive advantage at the end of the day.
*  And of course, you want to use your expertise, but you also want to address global questions.
*  And so that's why you want to sort of reach out, which is very good as well.
*  But there is a balance to keep there.
*  And is neurophysiology reaching out for you?
*  Absolutely. Where to start?
*  Well, let me ask you this before we go on, because do I have it right that I think I read in one of your editorials
*  that it was was it James Gleek's book that drew you into control in the first place?
*  Can you just tell me that background story?
*  Probably. So do you know about this book?
*  This was a book of chaos and celestial mechanics and I mean, the whole history of science,
*  starting with Newton and then finishing with Poincaré and dynamics in the 20th century.
*  I found this absolutely fascinating.
*  Maybe it was the first time where I got such a sense that science is historical.
*  And this is something that is very close to my heart.
*  And it's really a human adventure across centuries sometimes.
*  And it's fascinating to see that at the same time, it it it progress very slowly,
*  but at the same time, it's very connected.
*  And I think that chaos was the sort of the deep learning of today.
*  It was very it was a hype in the 80s.
*  It was a very sort of novel way of linking the deterministic and the stochastic.
*  And so it raised many hopes and many expectations.
*  So, yeah, that that that was all very attractive to me.
*  I've sort of moved away from dynamical systems because I've realized over the years
*  that dynamical systems was a sort of very often an obstacle to think of questions of neuroscience.
*  And in my first steps in neuroscience, I was always told that, you know,
*  the only way for an engineer to approach neuroscience was neuro dynamics.
*  And I think that many people still nowadays in neuroscience have this view of the brain as a dynamical system.
*  And I yeah, I think that this causes a lot of difficulties, at least to me, it has been
*  the journey has really been from dynamical systems to, you know, open systems,
*  that interact with the environment.
*  And this is why I think that the brain is so much about control.
*  It's interesting that you say that maybe we should pause here for a moment and think about that more,
*  because right now, at least from my perspective, there is a resurgence of dynamical systems theory,
*  at least at the large population of neuron level, maybe not so much at the single neuron Hodgkin Huxley.
*  You know, modeling a single neuron, but thinking of the activity of populations of neurons and how to tie those two cognitive processes.
*  Dynamical systems theory seems to lend itself fairly well to think of these,
*  you know, to take high dimensional activity, reduce the dimension of that activity and see what kind of landscapes and attractors you can glean from that activity.
*  Is that the kind of dynamical systems theory approach that you're that you have come to think is not as valuable?
*  Yes, but of course, don't get me wrong.
*  I mean, I think it's of course very good that people wish to acknowledge the dynamical nature of the brain and of neural behaviors.
*  So there is no question that the activity in the brain is very dynamical.
*  And so when we want to model the brain, we need dynamical models.
*  However, there is a big and underappreciated distinction between closed and open dynamical systems.
*  So I think we are still very much influenced nowadays by Newton's description of celestial mechanics.
*  And so this is what we call a closed system.
*  There is no interaction within environments.
*  It's all planets moving like clocks.
*  And I think that this view is very difficult to transpose to the brain, because I think of the brain as really a machine that the main role of which is to interact with its environment.
*  And once you have a dynamical system that has sort of input and outputs, I think that the dynamical system has strong limitation.
*  It's very important to acknowledge the open nature of those systems.
*  And this is very much the field of control.
*  So this is more or less moving from science to engineering as well.
*  And often, when it comes to the methodology, we have to acknowledge that there is a methodology of dynamical systems is at least four centuries old.
*  So we have a lot of tools to talk about dynamical systems.
*  Control theory is much more recent.
*  And so we have much less tools to talk about open systems and interconnection of open systems.
*  So maybe we should just dive into the mixed feedback signals that you've been working on.
*  But maybe before that, even just to really zoom out, how would you describe what is the
*  grand vision or what is the goal or project that you see yourself attacking?
*  The short answer would be building a brain, which is, of course, slightly provocative.
*  But what I think is important there is building versus understanding.
*  I think I see a lot of people in neuroscience considering that the grand question is to understand the brain and to understand how the brain works.
*  I think I moved away from that question.
*  Perhaps it's too hard for me.
*  But I think that and perhaps this is my sort of engineering background that is now speaking.
*  But I find that when you want to build the machine that approaches the behavior of the brain,
*  it's sort of very concrete and it's also perhaps sort of a bottom up because it's going to be a long way before we build a brain.
*  But I think we understand what I mean when I say I want to build a brain.
*  I want to build a machine that is closer to the brain that the machines that we currently have.
*  Why?
*  Well, again, that's very historical, because if you go back to the early days of control,
*  which we call cybernetics, which I think was a great time that is, in a sense, very similar to the current time.
*  So we are talking about the late 40s, right after the Second World War.
*  And this is a time where there was a lot of enthusiasm to think about machines and animals in the same language and to try to really think of the brain as a machine in the first place.
*  And then as a second step, sort of try to imitate that machine.
*  But in fact, this moment in history was very short lived because.
*  I think it was stopped quite abruptly by Shannon's theory, which is 1948.
*  So it's really we are talking about a few years and Shannon, I think, was very disruptive in saying,
*  we need an information theory and that theory needs to be discrete.
*  And a few years later, as we had the digital computer and from that time on,
*  we have seen an increasing split between what we call analog technology and digital technology.
*  And perhaps today we are sort of the very climax of that of that split in the sense that,
*  students enter engineering thinking that analog is old and obsolete and useless and that digital is important and is cool and is the future.
*  And my view is that the digital age is just a moment, another moment in history that very soon we're going to go back to something which is much more mixed.
*  But I think we see that happening already.
*  And I'm quite fascinated by the sort of return to the mixture of the analog and the digital,
*  because I think I read it as a return to the cybernetics age, which was sort of ahead of its time.
*  But I think now we can really make another try because we have 60 years of developments in neuroscience.
*  So we understand the brain much better than in 1948.
*  And also, of course, we have 60 years of developments of digital technology and of computational technology.
*  How did you come to the did you look at a neural signal?
*  I was going to make a joke and say, well, of course, the brain is digital because it communicates in spikes.
*  Right. But then, of course, when you look at the activity of a neuron,
*  there's a voltage signal, which is a continuous analog signal, and then these somewhat discrete spikes, which are really continuous.
*  But as you say, you can count. Did you one day see a neurophysiological signal and think, oh, that's mixed feedback?
*  That's how I could solve that. How did how did you maybe you could describe the mixed feedback approach and then and then give the background.
*  OK, yeah, I mean, I think I should I should I should tell the anecdote because this is really a turning point in my in my scientific life.
*  And it happens more or less accidentally.
*  And I certainly, as you said, did not think of spikes as mixed feedback signals before that.
*  So in 2008, I I helped neurophysiologist from my university to develop a computational model of a single neuron.
*  He was studying the effect of specific calcium channels in dopamine neurons.
*  And so we shared a student for a year and we helped him developing the computational model.
*  And then at the end of that project, the students came to me and said, could I start a PhD?
*  And I told him, you know, I'm not interested in computer simulation.
*  But of course, this student was afraid of nothing.
*  His name is Guillaume Drion, and he's a mountain biker.
*  So he he's sort of crazy student who wants real challenges.
*  And and I told him, OK, the first thing that I would want you to do if you want to do a PhD is to take this computational model and to simplify it,
*  to a second order differential equation so that we can draw a face portrait.
*  And he tried to do that.
*  And we knew already quite a bit of neurodynamics by the time.
*  So we were trying to connect essentially what this computational model to the little neurodynamics that we knew.
*  And it didn't work. He tried and kept trying.
*  It didn't work. And we felt that there was something missing.
*  And and so eventually we had a visiting student who was a sort of with a math background and wanted to do neuroscience.
*  And I told him, OK, here is a five dimensional model, a model with five differential equation.
*  How do you reduce that model to two?
*  And he came back to me a week later with a face portrait, what was obviously wrong.
*  In a sense that it was different from any face portrait I had seen in neurodynamics.
*  And then we start working, the three of us on this face portrait and the rest is history.
*  But very rapidly, I understood that the role of calcium channels in this neuron was a positive feedback,
*  very much like the sodium channels of the Hodgkin-Hudgkin model.
*  And that it was just in a slower time scale and that neurons were organized with this big feedback motif
*  that you can pile up at whatever, how many scales you wish, both in times and in.
*  And it was sort of a flash that this provides a completely novel way of attacking multiscale control and control across scales.
*  And then it took many years to sort of connect that to to history to discover that, in fact,
*  mixed feedback was very well known in the cybernetics time.
*  So, in fact, the mixed feedback amplifier was the main object of study in the 30s and 40s in Bell Labs,
*  when people started using feedback to do long distance communication.
*  But I had never been told that. So I had to sort of rediscover that.
*  Is that because cybernetics is all negative feedback?
*  Right. That's the story is that cybernetics is all negative feedback.
*  Is it not the story?
*  That's what we have. That's what we have remembered from cybernetics.
*  But before, in fact, at the time, the only way to build switches was analog.
*  And how do you build a switch in analog circuits by using positive feedback?
*  In fact, historically, positive feedback was discovered before negative feedback.
*  So all the electronic circuits early in the 20th century were positive feedback circuits to build memory,
*  what we would call memories today. And negative feedback was discovered much later.
*  And it was a complete revolution by Black to understand that negative feedback had a role and not just positive feedback.
*  We have, I think, sort of forgot that early part of the history of feedback.
*  And then we have remembered the role of negative feedback.
*  And from the invention of the digital computer, you know, positive feedback became obsolete and useless
*  because we had a different way to sort of encode memory.
*  And we were only needing negative feedback in the digital age.
*  And so that's why we have this nowadays, this vision that negative feedback is analog and positive feedback is either in existence or just digital.
*  And so you have modeled neural activity at the single neural level as a mixed positive and negative feedback signal.
*  I wonder if it's worth just describing the overarching principles of that model.
*  Right. So because, of course, neither negative feedback nor positive feedback is something novel.
*  Right. And I think most people have a sort of a rough idea of what negative feedback means.
*  We think of thermostat and we think of, you know, creating a negative error to reduce the variations of the plans and to reduce sensitivity.
*  So we think of our cruise control system for the car.
*  And we can think of many examples of sort of negative feedback.
*  And then I think we especially biologists, they are very familiar with the idea that positive feedback creates, you know, binary memory or digital automata.
*  But I think that's what I discovered as fundamental in the organization of neural behavior is the fact that once you have both,
*  you can just balance positive and negative feedback and you can continuously sweep between those two.
*  And in particular, there is a sort of a boundary between the world of negative feedback and positive feedback, where you go from one behavior to the other.
*  And that boundary is what we call in mathematics a singularity.
*  And this is, in fact, the place for ultra sensitivity, for spiking and for thresholds.
*  And I think it's really a fundamental organizing principles of neural circuits.
*  The fact that neuromodulators can continuously balance these two feedbacks and so use the same device,
*  if you want to think of it in terms of a machine, to either have a memory or to have a processor and to have, in fact, a mix of both.
*  Which I think is very cool and something that as engineers we have lost in technological worlds,
*  which is nowadays divided into, on the one hand, a digital world and on the other hand, an analog world.
*  But the way that you describe it, it seems, and I don't know if this is why in engineering,
*  it maybe seems less appealing is because it seems like a very delicate balance that needs to be walked so that you don't,
*  between the positive and negative feedback control signals, is that just difficult in engineering applications?
*  Is that why it might be a little less appealing?
*  It's a very important question that you raise because I haven't spoken about the most important feature of this mechanism, which is its robustness.
*  If you have one source of positive feedback and that source is sort of, think of it as being narrow range.
*  So it provides positive feedback only in a very narrow range of amplitude and perhaps temporal scale.
*  And then it is sort of surrounded by another source, which is a source of negative feedback, which is much more broad range.
*  And now you sort of superpose the two.
*  And I don't know whether it's intuitive that it's like summing a negative function that is very narrow to a positive function that is broad.
*  The result will be the sort of convex function with a little dip, with a little bump.
*  And the little bump is created by the positive feedback.
*  This picture is extremely robust because even if you have a lot of uncertainty on both sources, as long as you have this principle of, you know,
*  the positive feedback being sort of narrow range, you will always have this spiking behavior existing.
*  You cannot control exactly where and when, but it's going to always be there.
*  And that's, I think, fundamental to design of the biologic system, because it's a design principle under uncertainty.
*  And I think that's the most important meeting point between the brain or even biology in more general and control.
*  I think of control as a design discipline under uncertainty.
*  And since you mentioned robust and sort of making the connection with biology, I suppose it might be the right time to bring up Eve Martyr's name and how you,
*  I know that you're largely inspired by her work on the stomatogastric ganglion of the lobster and crabs.
*  And maybe you can just kind of bring that in and talk about, did you already have these principles that we've been discussing in mind?
*  And then you saw her work. And then that was another aha moment.
*  How did you come to be interested and appreciate the STG and her work in that system?
*  So I've had her on the podcast and famously that system is robust and can operate under different temperature ranges and still under different regimes,
*  come out with a functioning central pattern generator oscillatory system that can still function in the crab.
*  And likewise, that same structure can give rise to different functions depending on neuromodulators that's being bade then, etc.
*  Right. So very soon after this, I think that I've been telling you about earlier, we, you know, we, we said,
*  we feel that this is very important. We should, you know, go to neuroscience meeting and talk about it.
*  So we set an abstract to the neuroscience meeting and we went there.
*  You know, the biggest conference in control is about 3000 people.
*  And then I there I am at San Diego, 30000 people.
*  Where do you start?
*  And then one at the time postdocs who then became my colleague, Tim O'Leary, came to our poster.
*  And he was he had been working in Eve's mother's labs for three or four years at the time.
*  And he told me he told us this is what we need.
*  And that was the start of discovering it matters work.
*  And very rapidly, I found that I had found my home in neuroscience that to me,
*  no relation is the control systems of the brain.
*  Yes.
*  OK, well, I'm just curious at that.
*  You know, so you're talking about SFN, which is the Society for Society for Neuroscience, the largest neuroscience conference.
*  How well what year was that approximately and how well trafficked was your poster?
*  I think it was 2012, if I'm not wrong.
*  And then we went a couple of times, maybe 2013.
*  And and and then I, you know, I visited Eve mother's lab and you know, spend a year.
*  Then then eventually Tim O'Leary took a faculty position in Cambridge.
*  So since then, we have sort of become much closer to each other.
*  And and and I think that's yeah, if mother's work is is really I find many similarities between also the position of neuromodulation
*  in the world of neuroscience and the position of control in the world of engineering.
*  You know, I think her work is nowadays recognized as sort of groundbreaking and extremely fundamentally.
*  But I also know that for many, many years, she worked pretty much in isolation, being told that she was working on something obsolete and from the past.
*  So I've read this.
*  Excuse me. I read this quote from you since you said that about Eve.
*  I don't remember the source, but you wrote, If you wish to contribute original work, be prepared to face loneliness,
*  but never stop asking and listening.
*  Yeah, that's certainly my experience in over the last 10 years.
*  And that's why I was saying that it has been a sort of a turning point in my career, because before that, you know, when I submitted the paper, I knew it was always going to be accepted.
*  I mean, it was it was more like a business work.
*  And then start in 2009, I've got papers and papers and papers rejected and has really been a very hard journey.
*  Not just I wouldn't say that much for myself because I was sort of established by then.
*  I'm thinking more about my PhD students and postdocs who were really in the wild.
*  And and and I think this is inevitable.
*  It was a long journey.
*  I think mostly, you know, when I look back at those reviews and those hard times, I don't blame anyone.
*  I don't blame anyone.
*  I think if there is anyone to blame, it was us.
*  We were using a language.
*  I mean, we are not communicating with that, essentially expressing things in our own language, but not in language that allowed communication.
*  And we wanted to reach out in communities and we didn't really speak the language of those communities.
*  And so that has been a sort of the reason why it took a long time.
*  I would say that this difficult time ended up with being invited at Telluride and discovering Neuromorphic Engineering in 2018.
*  I had never heard of Carver Meet until 2018.
*  And going to that conference was sort of a shock because I suddenly felt like all the work we had been doing for the last for the ten preceding years
*  was essentially an answer to the question raised there.
*  Wow.
*  And at the same time, it felt like going back home.
*  Suddenly, I was speaking to engineers.
*  I was speaking to people who understood my language.
*  And and since then, things have been easy.
*  No more loneliness.
*  What happened?
*  Is that the is that when you started modeling the crab stomach, stomatogastric ganglion system?
*  Or was that a couple of years later?
*  Because I know so we'll go to we'll talk more about neuromorphics and that in your interest in those.
*  And you have been for a few years, at least, modeling parts of the stomatogastric ganglion.
*  Was that was there a challenge in that conference or how did that begin?
*  No, that well, that began as soon as we as we met Eve's group and that we were sort of given with a relatively small network.
*  But we were told that this network was nevertheless very rich.
*  And so it models tells that the stomatogastric ganglion has about 30 neurons.
*  But in fact, you can sort of have a cartoon model with about five neurons.
*  And that's the size of circuits that we are ready to jump in coming out of our cellular work.
*  OK, so the STG was very instrumental to help us understanding how you move from the cellular level to the circuit level and whether there is any
*  chance to do that in a sort of a bottom up fashion.
*  I think many people think that, you know, cellular work is sort of useless if you are interested in brain functions.
*  And so there is this big split of communities.
*  And so, of course, it's very questionable whether doing work at the cellular level has any chance to have an impact at the circuit or functional level.
*  But that was our interest from the start, because my interest from the very start was to discover a principle of what I call control across scales,
*  which I think is the big, big open question nowadays.
*  See, even in neuroscience, but not only neuroscience, but certainly neuroscience.
*  If you go to the SFM meeting, you see this very layered conference where some communities study the cellular level, some communities study the animal level and then all the.
*  But the grand challenge, of course, seems to be that how you go from one level to the other and how does and whether it's hard to imagine that a community would have worked
*  for more than 70 years on the cellular level if it was totally useless.
*  But at the same time, it's still, I think, very much an open question on how the cellular level sort of governs the organization of higher level.
*  And as a control engineer, this is a very central question for me.
*  So let's talk about across scales for a moment, because it's it's fairly intuitive to think at a single neuron or thinking about the molecules, the receptors and that neurons need for homeostasis and to remain within a range to stay alive.
*  And then and then you can kind of it's still intuitive to build it up and think, well, these are now communicating with each other.
*  But then you start getting into higher, let's say, cognitive functions.
*  And then it seems harder to connect that in a control story.
*  Where is the that internal reference signal that is being controlled for?
*  Right. Does that make sense that do you think of higher cognitive functions as control also?
*  Definitely, but probably I think that way because I don't know much about what you mean by higher cognitive level.
*  No one does, though. And so I'm sort of I'm sort of very naive in having in lacking the knowledge of neuroscience.
*  And and but at the same time, I've been continuously amazed by how much, you know, we in the first year, we spend a lot of time, most of our time, I would say,
*  explaining how a single cell can sort of be modulated between a spiking state and a bursting state.
*  And of course, it was very difficult to make any point of that, because everyone was telling us, I mean, this has been studied 40 years ago.
*  What what are you what you want to do?
*  And yeah, I will not answer to too many details because it would it would get technical.
*  But then already, if you go from the single cell to an STG, so an STG is essentially an example of what neuroscientists call central pattern generators.
*  You you must generate rates and STG generates a slow rate with essentially two neurons and another faster rate with another two neurons.
*  But how you generate a rate out of a single cell has been studied for a century.
*  It's the so-called half center oscillator model.
*  You just attach two cells to each other with inhibitory coupling and you create a sort of anti-phase clock in a very natural way.
*  Now, discovering the fact that cellular bursting was the control mechanism of that very simple rhythm was already, I think, a big, big step forward for us.
*  Because it has always been a difficulty for me when I studied the literature on central pattern generators to know whether you should think of central pattern generators as autonomous clocks
*  or as circuits that interact with the environment.
*  And of course, we know that it's a mix of both.
*  But many people have a view of either inhibitory networks as being sort of very autonomous and not requiring any signal from the environment.
*  And you see other people who sort of reject that idea saying, no, no, no, no, that doesn't make sense.
*  Any cell must interact with the environment, which is true.
*  You see this balance, in fact, is very much, again, a manifestation of the balance between positive feedback and negative feedback, but already at a higher scale.
*  There is not much cognition, perhaps, going on in a CPG, but it's already a higher level than a single cell level.
*  In fact, we see nowadays that, in fact, CPGs are all over the brain in a sense that inhibitory networks play a role to generate rates in many, many areas of the brain.
*  And then if you go even higher up, you find that this transition of a single cell between spiking and bursting, for instance,
*  has been described to play an important role in sleep and in sort of disconnecting the thalamus from sensory mode and sort of creating a sort of a gate between the cortex and the sensory layers.
*  And again, you find that you see this same balance between inhibition and excitation as something that can regulate how much you want the behavior to be endogenous and sort of disconnected from the world versus you want the network, the circuits to be connected to the world.
*  And nowadays, there is still a lot of it's a very active research area in neuroscience and in neuromodulation.
*  And people talk about brain states and brain states are sort of cover all the levels all the way from the whole brain, which is whether you sleep or whether you are awake to very small circuits that can be sort of temporarily disconnected or connected.
*  Now, this is just an example, and it's one of the few areas that have studied a little bit, I would say, neuroscience.
*  But this gives me hope that this bottom up approach can go a long way.
*  And I don't know how much it can cover cognitive areas, but certainly it is enough.
*  If you ask the engineering question of using an evidence based camera to create something like attentive vision, how can you make a camera asleep or awake?
*  I think that already this is sort of a very engineering question, which, by the way, it's a very important question nowadays in engineering.
*  And I think you can directly connect that question to what I've been talking about and that have been studied in neuroscience for now 50 or 60 years.
*  So how far have you taken the taken the neuromorphic approach to the STG?
*  OK, so again, I mean, we started neuromorphic quite recently, and I have very little expertise in circuit design.
*  And. But I found in Cambridge, one or two students sort of brave enough to design analog circuits.
*  But you have to imagine that nowadays for a student, it requires a lot of courage to dig into an analog circuit design, because.
*  Why would you study analog? Anyway, we have built and students of mine have built first what I would say the first neuromodulatory neuromorphic circuit.
*  So very elementary circuits that can be controlled between sparking and bursting between on and off discrete states.
*  It's tremendously encouraging to see that it works and to see that it works in the presence of uncertainty.
*  And so. I think my next five years or even 10 years will entirely be in that area, because now we really are at the stage where we can try to.
*  Design and build circuits of growing size and the STG will be one example of them where we're going to start assembling those motifs to create circuits of higher dimension.
*  And of course, electronics is a very good area to scale up, because you can very easily build chips with several thousands of neurons of the type of neuron that we call the neuromorphic.
*  Urines of the type of neuron that we have built just on the PC board with two or three.
*  But thinking about so, as you build up and even as you're modeling, you know, even your mixed feedback signal, the way that you model a neurons membrane right to to simulate the signals coming from a neuron.
*  So, a real neuron has dozens of receptors, ion channels, et cetera, and you are, you have to abstract away from that. And like you were saying to earlier, if you can get two equations, does it.
*  Do you feel as you scale up that you're going to continue to need to abstract things out or do you have any.
*  Plans or desire to build in finer detail of those ionic currents, or is that just are we at the right level of abstraction in your opinion to, but because it functions as a mixed signal feedback, and then you can change the motifs with the neuromodulation principles.
*  Right.
*  Okay, maybe there are two aspects on the question. One aspect is.
*  If we look at the complexity of these neuromodulators and receptors and ion channels, and to what extent do we want to replicate that in a circuits and.
*  My view is that there is a huge amount of redundancy in those circuits.
*  Which makes them credibly adaptive and reconfigurable and evolutionary and so on. And of course.
*  It's going to.
*  That's perhaps the biggest challenge if we want to build machines that have the same level of sort of evolutionary capabilities.
*  Well, they're also continuously being turned over.
*  Turned over in Watson. What do you mean by that?
*  They're continuously moving on the membrane each ion channel and then that ion channel dies. A new one is synthesized. You know, so there's continuous turnover in the system as well.
*  Sure.
*  Absolutely.
*  So that has a, I think.
*  Pretty good translation in cover meets electronic elements that you use these trans conductance transistors that are voltage gated and you can really think of the voltage as a.
*  As a way to modulate their maximal conductance, which is very much like what a neuromodulator does by, you know, modulating the expression of a channel.
*  Essentially, you create more conductance or less conductance. So there is quite a good match between those two principles.
*  And so that I think we can imitate. But of course, in a much simpler way, right?
*  And of course, the way I think of how you control spiking neuron, which would be a sort of the simplest control system is that in principle, if you want to control a spike, you only need one conductance for the positive feedback and one conductance for the negative feedback.
*  So you only need two parameters and you balance the two parameters.
*  But in fact, the way a neuron does it, it use perhaps hundreds of parameters to control the positive feedback and another hundreds of parameters.
*  Why so much redundancy? Because then you can think that, you know, there are many, many different ways you can modulate, let's say, the positive or the negative conductance and.
*  And. You can sort of think of attaching of each receptor as being another sensor for the neuron.
*  And so a single neuron can sort of pay attention to a diversity of signals in the environment.
*  But at the end of the day, the control task of all these channels and receptors has a certain level of simplicity.
*  It just has to balance this positive and negative feedback, but just can do it in many, many different ways.
*  That's really something I learned from Eve Marder's work.
*  Because I would say that if you think of the STG as a control system, the task of that control system is pretty simple.
*  It just has to articulate two rates with each other.
*  But it is done with tons of neuromodulators and tons of receptors.
*  And this is what is creating the complexity.
*  So sometimes I say that I think of neural circuits as very simple control systems with very complex controller,
*  which is almost the opposite of what we do in engineering, where we use always the same type of PIT controller.
*  But then we put many, many, many of them to control a very complex system.
*  But at some point that gets wasteful, right?
*  While wasteful, we have to be careful when we use that word.
*  Because, I mean, our experience of animals is that they're not wasteful at all.
*  And so, but I think that I think of this redundancy as being accumulated over evolution.
*  And so the way I think of building machines that sort of mimic those behaviors, those machines at least initially would be much, much simpler.
*  But perhaps over time, you know, you add another function.
*  It's a little bit like software, the way software is developed nowadays.
*  You keep adding functions and at the end of the day, they look pretty wasteful.
*  Okay, well, let me I'm going to play you this question from a listener because I want to make sure I get it in before the end.
*  And it might be the right time to play it and might lead to other topics here.
*  So here's the question from Matt.
*  Hi, Professor Supplicker.
*  Since you and your colleagues work on mixed feedback control has made progress on the issues of component variability and noise fragility.
*  What do you see as the next big technical barrier standing in the way of mainstream adoption of neuromorphic methods, if any?
*  Or is it more a matter of getting the right people in industry interested?
*  Thank you.
*  That's a tough question.
*  Talking about the future, it's always difficult.
*  Yes.
*  But my experience is that technology as very often is way ahead of us.
*  And when I say us, I mean researchers.
*  So I think that the theory of neuromorphic design is lacking behind the technology of neuromorphic design by a very significant margin.
*  Nowadays, there is a huge interest from the industry for neuromorphic.
*  Intel is building neuromorphic chips and then the Evan-based camera was commercialized just a few years ago.
*  But I think it's a complete revolution in the computer vision industry and community.
*  But the theory lags behind.
*  Why?
*  Because what we have on the table, what we learn as students, is a sort of double set of tools.
*  And you pick your digital tool, your analog tools from two different backs.
*  And you do that at every level in every discipline.
*  And at least my understanding of neuromorphic is that it's precisely the mixture of the tool that is fundamental to neuromorphic.
*  And the truth is that we don't have a theory for that.
*  We don't know how to handle spikes.
*  So some people handle spikes in a statistical way.
*  Some people say that spikes are irrelevant.
*  Some people say that each single spike is hugely important.
*  But I mean, this diversity of almost opinions, I would say, is just telling us that we don't have a good theory to handle spiking information technology at the moment.
*  What role do you think the modern successes of rate-based deep learning models has played or continues to play in that divide?
*  I mean, a lot of people, even in neuroscience, look at the success of these rate-based models sometimes that are just feed forward and really abstract away a lot.
*  Going back from McCulloch-Pitts, the binary neuron, to now these rate-based approaches.
*  And they can do so much. So, right, like you just said, we don't need spikes. They're irrelevant.
*  How do you view that in terms, just personally, but also then in terms of, related to Matt's question, getting people excited about neuromorphics?
*  Well, my experience is that a lot of people are getting very excited about neuromorphics these days.
*  But it was not certainly not the case 10 years ago.
*  And so, and that was a time where I was digging into spiking. And so I asked myself that question very often.
*  I remember reading a famous paper, I think, Requiem for the Spike, and thinking that perhaps I was working on something completely irrelevant.
*  But, you know, I think it's phenomenal what has been achieved based on McCulloch-Pitts ideas.
*  You know, you use so little of what we know of the brain, and then you build 60 years of technology that is still developing.
*  And I mean, who could have predicted what has happened in digital technology in the 60s? It's just phenomenal.
*  At the same time, I think that an increasing number of people think that, you know, digital technology has very, very strong limitations.
*  And probably Carver Mead was visionary in sort of foreseeing that 30 years before the others.
*  And perhaps it's probably because he was at the very forefront of, you know, computer technology.
*  And so he I think he became because he was an expert in CMOS technology.
*  I think he perceived before others that this was hugely inefficient.
*  And sooner or later, we would be hit by this inefficiency. And that's what we see now.
*  Suddenly, you know, the carpet footprint of digital makes news and he's really becoming a huge problem.
*  And that's why there is such an interest in the industry.
*  And so I'm not worried about, you know, the potential of neuromorphic.
*  I'm more worried about the pace of developments of the theory.
*  It's very slow, partly because, you know, most of people work.
*  I mean, this is a bandwagon effect.
*  So nowadays it's far easier to get a job and just to develop another deep neural network.
*  And I don't think there is much you can do about this phenomenon.
*  It's a sociological phenomenon that will always exist.
*  But if we let's say we could siphon from a black hole some energy portal.
*  And so we had nearly infinite power consumption ability and then didn't have to worry about wasting the power.
*  Right. Would it matter?
*  Could we just scale up with what we have?
*  And of course, we could give the energy back to the black hole.
*  So it wouldn't increase global warming anymore.
*  Then would we still be building neuromorphics and worried about the power consumption?
*  Is there something else besides power efficiency that neuromorphic computing can add?
*  What's that?
*  So very good point.
*  I'm talking about energy just because it's in the news currently.
*  And that's why I'm not worried about the power consumption.
*  I'm talking about energy just because it's in the news currently.
*  And that's the argument of companies like Intel.
*  But energy efficiency has never been my interest in neuromorphic.
*  But I've very long been fascinated by the power of animal vision in selecting the right sort of information
*  with a speed and a resolution that will never be achieved by any digital camera.
*  So I think that when you study for five minutes the difference between a digital camera and an evidence-based camera,
*  you immediately realize that there is nothing more stupid than a digital camera.
*  And that's storing streams of millions of pixels for nothing most of the time.
*  And then piling up this in huge servers is, I think, a century from now.
*  We will laugh about that in the same way as we laugh about, you know,
*  the way people were using mechanical power at the end of the 19th century.
*  And so there is no question that the way we use digital technology today will sound extremely obsolete maybe already 20 years from now.
*  And not just for energy efficiency. It's much more than that.
*  Think about soft robots that need to grasp anything with a sort of sense of touch.
*  We are nowhere in designing such robots. Nowhere.
*  And I think we will never get anywhere as long as we stick to digital technology.
*  Likewise for acoustic sensing, likewise for digital visual sensing, all the sensing that we see in the animal world.
*  How long will it take for the theory to catch up?
*  I think it's speeding up.
*  You know, I see that I mean, I can at least speak for my work that if I look over the past 10 years,
*  I think the pace has been extremely slow because it has been a lot of deconstruction and a lot of reconstruction.
*  But I'm quite optimistic that the developments will be quite fast in the next 10 years.
*  And I think that many people express the same in different areas.
*  And there is a sense, I think, growing up that we are about sort of a turning point in the way we understand the brain in the sense of designing machines.
*  So we are very close to, you know, designing machines in a very novel way.
*  And I think that perhaps the Evan-based camera is the best current example of that.
*  So from your engineering perspective, I know you have your fingers dipped in a lot of different areas.
*  You have a view on neuroscience.
*  And I know earlier you said that you don't understand enough about enough neuroscience to speak about higher cognitive functions, et cetera.
*  But and I know that you're aware of the modern deep learning successes.
*  And there's this large push in neuroscience these days to use those deep learning models to help us understand and control.
*  Actually, if you look at Jim DiCarlo and Dan Yehman's labs, I know that you're you think of control as understanding to use those deep learning models as a window into how our brains function.
*  Does this look right to you? Does it look silly to you?
*  Does this do you think like neuromorphics in a hundred years, we're going to look back and think that the whole deep learning, quote unquote, revolution that is continuing to scale that's by itself.
*  Sorry, those are I'm conflating two things using deep learning to understand brains and deep learning itself continuing to scale.
*  Anyway, let's stick with the neuroscience deep learning comparison.
*  Do you think that's a useful way to model what's happening in brains or do we need to use things like, you know, the mixed feedback signal?
*  Which is it seems like an entirely different beast.
*  I'm not sure. I mean, using deep learning to advance neuroscience doesn't speak to me.
*  But using deep learning for whatever scientific question doesn't speak to me.
*  That doesn't mean that it's silly.
*  It just doesn't speak to me.
*  And I think we have to be very careful about the time scales of these hypes.
*  Deep learning started, let's say, 2012.
*  So this is just 10 years ago.
*  And I might be wrong, but I think that deep learning will be very short lived.
*  I see nothing fundamental in deep learning.
*  And I think that many researchers in machine learning would agree with that.
*  Don't take me wrong.
*  It is creating a huge advance in the industry and in the technology.
*  So it is a technological advance, perhaps a technological revolution.
*  I don't think so. But it's certainly not a revolution in science.
*  And I think that it is very tempting, especially if you don't work in machine learning.
*  But if you use machine learning, if you use deep learning, it's very tempting to think of it as a sort of a black box that is doing miracles.
*  But that won't last.
*  And in fact, we have seen that in previous sort of winters and summers of machine learning, you know, whenever you create big expectations, the deception comes next.
*  And so I think we are very close to that stage.
*  Where do you see us in neuroscience right now?
*  I know it's an unfair question.
*  You know, I know too little about neuroscience to say anything relevant about neuroscience.
*  I see neuroscience as the most important scientific field in science today.
*  And so no question that this is going to be the big science of the 21st century.
*  I think that progress has been very slow initially, and it is speeding up.
*  And what can I say beyond that?
*  As an anecdote, I could mention a book that I read last summer by Max Sorens called The Hidden Spring.
*  So this is a book about consciousness.
*  And I usually when I read articles about consciousness, I stop after two paragraphs.
*  But I read this book in and out.
*  And what I found really fascinating in that book is that I understood it all with the very little background that I have in neuroscience.
*  And I really read it as a control textbook.
*  To me, Max Sorens is describing the brain as a control system.
*  And now we are talking about, you know, perhaps the biggest or most grand problem of neuroscience.
*  And this, again, this speaks to me.
*  The fact that I think there is a convergence of.
*  And so what I especially like in that book is that I think Max Sorens at the end of the day, he's demystifying the question of consciousness.
*  And and he's using his background in neurology, his background as a psychiatrist.
*  He's making a huge number of reference to Freud.
*  And I think this is a very important time that the fact that now we start people feel, you know, a lot to go back to the roots,
*  a lot to contemplate the developments of neuroscience and go back to the early questions.
*  I think it's a very positive sign that there has been a huge developments of the field and that the field is entering an area where perhaps progress will be less disorganized and less fragmented and more cohesive.
*  I just recently had Karina Kurtow on the podcast and you probably don't know her name, but she is an ex-physicist.
*  And I was making a connection between her work and yours because she works on these models.
*  They're called linear threshold networks and they are essentially graph models where each node is an excitatory unit.
*  And then there's this background inhibition that follows kind of two rules that's just bathing the whole network.
*  And she's using that to be able to make rules.
*  They're mathematically tractable models so that she can look at the structure of the model and then predict the dynamics that are coming out of it.
*  And from building up these models, you know, into five, ten units, etc., then she can make these dynamic attractors that create sequences of numbers and etc.
*  Like she models a horse galloping in sequences and all sorts of different dynamical attractors.
*  And the goal is to be able to say what kind of dynamical structures will result in a network structure.
*  That's sort of beside the point.
*  So one question is I'm still trying to connect that with the mixed feedback signal approach.
*  And there's some fruitful project there to be had.
*  But the other reason I thought of her just now is because thinking about moving forward in neuroscience, as you say, slow progress, but it seems more concerted.
*  I mentioned that she has a physics background because the physicists seem to still be coming in droves into neuroscience.
*  But the background of neuroscience is a bunch of engineers also.
*  And I don't know if that has just been a steady march.
*  Do you think neuroscience needs more engineers, needs more physicists, needs more molecular biologists?
*  We all know that's not true.
*  What do you think? Is it lacking an engineering approach?
*  Is the engineering approach going to help advance the needle?
*  I think neuroscience needs all backgrounds and certainly needs physicists as well as it needs engineers.
*  I cannot resist telling another anecdote that it's back, I think, 2009 or very early in my journey in neuroscience.
*  I spoke to a computational neuroscientist and he told me, you know, there is only one good background if you want to do computational neuroscience, it's physics.
*  So he was sort of kicking me out of the room.
*  That's a very physicist thing to say, by the way.
*  Yeah, he had a few. He had a background in physics.
*  Of course.
*  But I've seen a lot of that, I would say.
*  And I would say that still nowadays in computational neuroscience, it's probably dominated by physicists.
*  And there is nothing wrong about it, except perhaps that it has created a vision of the brain that is very similar to, you know,
*  we spoke about the vision of James Glyke of celestial mechanics.
*  So I still sometimes amaze to see some people thinking of the brain as a sort of gigantic universe where things rotates like planets.
*  And that creates whatever it creates.
*  Perhaps engineers are useful to complement that view with a view that is much, much more close to Earth.
*  And I think that my competitive advantage as an engineer in that story, I think, is the design element.
*  So the word that you just mentioned sounds extremely interesting and, in fact, resonates with, I think, some of the things that we do indeed.
*  But my first question to that physicist would be, how would you build a circuit that does that?
*  And I think that's so this is a sudden question.
*  And it is the what we call in control the realization question.
*  You know, you build an abstract model of something and then you ask the question,
*  How do I translate this mathematical model or this simulation model into a machine, into a physical machine?
*  And I find that this realization question is not very often present in neuroscience.
*  And the result of that is a gap.
*  You see, I know that someone like Eve Marder has very little communication with computational neuroscientists.
*  And that I have perceived that gap very often between computational neuroscience and experimental neuroscience.
*  So, yes, I think that we see and I think we need more engineers in neuroscience.
*  And I think that this will happen because of neuromorphic engineering on the one hand, but also because of medical neuroscience.
*  No, inevitably, we will see a move from science to medicine.
*  And whenever we see in biology a move from science to medicine, we see the analog move from physics to engineering.
*  Because medical doctors, you know, at the end of the day, they don't really ask whether they understand the brain.
*  They just want to heal a dysfunctioning brain.
*  And in that sense, they are very close to engineers who want to build things.
*  And I think that a lot of progress in neuroscience, I'm sure, will come from brain machine interfaces,
*  will come from deep brain stimulation to cure diseases.
*  And so I'm quite optimistic about the progress of neuroscience being driven by medicine more and more rather than science only.
*  I don't want to get you in trouble, but what about philosophy? Is there a role for philosophy?
*  Well, of course, it's like asking a physicist if he thinks that physics is important.
*  I have a little bit of background in philosophy, and I think that philosophers do have a role in neuroscience.
*  In fact, a very important one.
*  Maybe not so much to develop theories of consciousness, but to bring more epistemology in neuroscience.
*  I think that there is a lot of confusion in neuroscience between the sub communities and that sort of develop their own languages and then have difficulties to speak to each other.
*  And I think that's the sign of a field that is developing.
*  But at some point, if you want to put a little bit of order and structure in that mess, I think philosophy is very useful.
*  And also another, I think, value of philosophy is to move people away from their methodologies,
*  which in neuroscience could be also experimental devices, and move them back to the questions.
*  And in particular, the sort of the core questions.
*  And so I think that philosophers have always had that role in science.
*  And it is something that is suddenly, suddenly a little bit these days that.
*  Sometimes you feel like philosophy is no longer regarded as a science and that there is this.
*  We tend to think that science is only about technology and that humanities are not really in the same playground.
*  I disagree very strongly with that view.
*  I think that science is a human adventure and that humanities have as an important role as as as technical science.
*  And certainly that's the case for the brain.
*  And, you know, we haven't been talking about all the ethical questions.
*  And yeah, I think there is a place for philosophy in many, many areas of neuroscience.
*  All right. I've kept you long enough, but I want to end on this, perhaps, unless you have other things that you would like to discuss.
*  But, you know, we've talked about sort of the history of feedback and how it began with positive and mixed and then negative feedback came to dominate with cybernetics and then cybernetics went away.
*  So there are these kind of fads and we've talked about how you think that the deep learning of these days is going to be fairly short lived.
*  And we discussed how, you know, I read that quote. I'm going to read it again.
*  The quote from you, if you wish to contribute original work, be prepared to face loneliness.
*  But the question is, how do you know you are working on the right thing?
*  Is it just that you are submitting manuscripts and they're getting rejected?
*  Or and then how long can you continue on that path? Because they're not all the right paths and they're not all the right subject areas to study to answer certain questions, right?
*  Engineering isn't applicable to certain questions.
*  So how do you know that you're doing it the right way?
*  Like, I think a lot of people struggle with this.
*  I struggled with this with this question throughout my career.
*  Definitely. I think in that same interview that you are quoting, I advise to always think of our profession as a privilege.
*  I feel very privileged, you know, to be paid to do what I'm doing, a little bit like artists who are paid for what they are doing.
*  I think it's a very luxury position.
*  But of course, this sort of role of research and academia is very much challenged nowadays.
*  Because we like to think more and more of academic people as contributing to the benefit of society and they have to do their job.
*  And so there is this sort of a business like model of academia that many people resent and especially I would say young people.
*  I've often had conversation with postdocs telling me, you know, scientists no longer what used to be.
*  I would never have the freedom that you have had. I'm forced to do one this and this and I have no choice.
*  I think there is always a balance.
*  And I think of the academic profession as a sort of something in between a profession and an art.
*  But sometimes I feel a little bit like often part of my job is the job of an artist, not my entire job.
*  So an artist is allowed to do wrong things.
*  An artist is allowed to work on things that, you know, will never be of interest to anyone.
*  And I think that academics should be allowed to work on things that will never have any impact.
*  But of course, you know, if you manage a department, you hire people, you also want to make sure that those people bring some money.
*  And so we are not just living in a purely artistic world.
*  And it is a balance that is very difficult to maintain.
*  I would also say that I was describing earlier that, you know, I think that the first part of my career has been closer to a profession.
*  And the second part of my career has been closer to an artistic life.
*  And certainly moving to Cambridge has given me a freedom that I don't know how many places still give that freedom.
*  But maybe this is something that one can develop over time.
*  And I always tell my postdocs and, you know, perhaps there is a way, there is a path to what you want to do.
*  And perhaps you have to sort of accept that you will not immediately be given the freedom of perhaps working on something totally useless.
*  But perhaps you can always try to push things in that direction.
*  And I think that in my case, it certainly has been a very slow journey.
*  And of course, I've been lucky in many ways, because you also depend on opportunities and on the so you don't control everything.
*  But I think you can always try to push the path in the direction of things in which you believe.
*  Because at the end of the day, the only thing that makes it possible for you to work in isolation is to believe in what you're working on.
*  And we have to be careful with that sort of faith.
*  It can be very dangerous.
*  So I think it's good to believe in something, but it's very important to keep interacting with others so that they can always have a chance to tell you that you are a fool.
*  Do you agree with like the postdocs you're talking about that the perhaps the on average the struggle along that path is of greater proportion than it used to be?
*  You know, it's very hard for me to compare the current situation to the situation 40 years ago.
*  I think it was hard at the time.
*  It is hard today.
*  Maybe it has always been hard.
*  Maybe what perhaps we.
*  Yeah, perhaps there is a tendency to think that.
*  Academia should be a mass thing.
*  I mean, that everyone should have the chance to become an academic and.
*  Yeah, I don't know.
*  I completely acknowledge that it is very difficult nowadays to navigate between the business demands and artistic hopes.
*  But I think that this is true of every profession.
*  At the end of the day, this is true of every life and we have to.
*  We don't have to just complain that things were easier before we have to.
*  I think there is always a path forward and and and that should be our focus.
*  Well, Rodolf, I'm happy for you that your path has become slightly clearer these days and that you've walked through the fire, so to speak.
*  And I appreciate your time with me today.
*  Thanks.
*  Thank you so much.
*  It was really a very nice opportunity to have a chance to talk about what is close to my heart.
*  Thank you.
*  I alone produce brain inspired.
*  If you value this podcast, consider supporting it through Patreon to access full versions of all the episodes and to join our discord community.
*  Or if you want to learn more about the intersection of neuroscience and AI, consider signing up for my online course, Neuro AI, the quest to explain intelligence.
*  Go to brain inspired dot co to learn more.
*  To get in touch with me, email Paul at brain inspired dot co.
*  You're hearing music by the new year.
*  Find them at the new year dot net.
*  Thank you.
*  Thank you for your support.
*  See you next time.
*  Yeah.

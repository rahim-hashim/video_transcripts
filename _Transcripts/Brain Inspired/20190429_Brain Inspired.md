---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3967s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 382
Video Rating: None
---

# BI 033 Federico Turkheimer: Weak Versus Strong Emergence
**Brain Inspired:** [April 29, 2019](https://www.youtube.com/watch?v=XTErs0p_mQs)
*  Okay, Federico, so you have a few hours on a Sunday, which ones you think you should
*  read about?
*  And I say, oh, this is a strong emergence theory, so I'm not going to spend too much
*  time on it.
*  I'm going to turn to something else.
*  You need to give space to creativity, and also you need to allow people to fail and
*  allow them to put them together and try again.
*  This is Brain Inspired.
*  Hello, exceptional brains out there.
*  This is Paul Middlebrooks.
*  Welcome to Brain Inspired.
*  Before I introduce the show today, I just want to quickly address some recent fun on
*  Twitter and a few emails that I've received encouraging me to have more women on the show.
*  If you've listened to more than a couple episodes, you'll likely have heard me lament
*  the relative lack of women I've had on the show.
*  Anyway, as I've shared on Twitter and in some email exchanges and as I've shared on the
*  show multiple times, it's not for lack of trying.
*  So no need to get into it here, but I'm happy to say that I'll have some more female guests
*  on soon, even though it personally feels weird to me to feel anyway in relation to what the
*  sex is of any guests on the show.
*  Anyway, we'll likely talk about the whole women in science issue and so on.
*  Okay, and now through no fault of his own, today I talk with another male guest.
*  Federico Turkheimer is a professor at King's College London who has studied largely human
*  imaging data like functional magnetic resonance imaging or FMRI and positron emission tomography
*  or PET or PET.
*  Discovering biomarkers for numerous neuropsychological and neurophysiological disorders and a wide
*  range of related statistical analyses.
*  But that is not why we talked today.
*  We talked because I came across his paper called Conflicting Emergences, Weak vs. Strong
*  Emergence for the Modeling of Brain Function.
*  This was in the journal Neuroscience and Biobahavioral Reviews.
*  You may remember my conversation with Paul Humphries a few episodes ago about emergence,
*  but here we discuss different facets of emergence, namely the distinction between weak and strong
*  emergence and how they relate to our ability to compute and or simulate the emergent processes
*  on their underlying processes.
*  Namely, a strongly emergent phenomenon can't be simulated by models whereas a weakly emergent
*  phenomenon can.
*  Federico considers some of the theories on brain function and consciousness with regard
*  to strong vs. weak emergence, including the free energy principle of Karl Friston and
*  his colleagues, integrated information theory of Giulio Tononi and his colleagues, and Federico's
*  own work on oscillatory mechanisms in the brain from the molecular level all the way
*  up to the neural circuit and brain regions levels.
*  So this is an interesting angle to approach these topics, and I hope that you find it
*  inspiring in your own work and thoughts.
*  We also talk about Federico's background a little bit and how it influenced his careful
*  and bottom-up approach to neuroscience and science in general, how students have such
*  a hard time understanding Bayes' rule, and we talk about plenty more, of course.
*  Find the show notes at braininspired.co.
*  slash podcast slash 33.
*  You can connect with me on Twitter, I'm at PGmid, or send me an email to paul at braininspired.co.
*  As always, thank you to recent supporters on Patreon, which you can do at braininspired.co.
*  Robert, Demetris, Mikael, if we run across one another, I promise I'll share my secret
*  award-winning chili recipe with you.
*  Alright, thanks for listening, everyone.
*  I hope you're having a wonderful bus ride, jog, or experiment.
*  And here is Federico Terkheimer.
*  Federico, take two here.
*  Thank you for joining me on the show and being here.
*  Good morning to you, Paul, and thank you for having me.
*  So I will have introduced you a little bit more at the top of the show, but briefly you
*  are a professor at King's College, London.
*  And I would say, and you can correct me if I'm wrong, but the majority of your research
*  has focused on neuroimaging analysis using things like positron emission tomography and
*  MRI to determine biomarkers for various neurological conditions.
*  Maybe, so we're going to talk about emergence a lot here today, but maybe you could just
*  describe a little bit more in depth about that kind of background, that kind of work
*  that you've done.
*  Yeah, that's correct.
*  So my core interest is developing imaging biomarkers, particularly molecule biomarkers.
*  Most of my work has been on positive emission tomography.
*  But obviously, and I focus on brain.
*  I used to, for many years, I've done also cancer and cardiac and everything else.
*  So in many ways, more than a computational or statistical, computational scientist, which
*  is my original training, I trained as an engineer, but I then became sort of a statistician at
*  a certain point.
*  I see myself as a physiologist.
*  And I think the difference is that when you are a physiologist looking at organs like
*  the heart, the lungs, the liver, you're engaged in far more traditional kind of outputs like
*  energetics, biochemistry, and so forth.
*  But since I moved into psychiatry, I worked at the Institute of Psychiatry in London.
*  I had to engage with the output of the brain, the main output, which is behavior.
*  So that's my interest at that.
*  Yeah.
*  I mean, given that statistical engineering background, and I guess you're kind of building
*  up to this in general, but I'm curious how you became interested in emergence.
*  So it's, well, it's a long story.
*  So as I said, I started from basic molecular measures and at a certain point, because I
*  lead the analysis section here, and you have to engage with the question on how you link
*  everything we measure from a neurobiological point of view with behavior.
*  And you have to.
*  And that's so I got interested in complex systems and all these modeling and mathematics.
*  But as I said, more than the statistical aspect, I'm more interested in the models.
*  I'm interested in modeling pretty much.
*  Yeah.
*  So how do you, so the real question is how do you link changes in basic and neuro,
*  molecular, neurobiological substrates to behavior, which is quite a complicated question.
*  Yeah, to say the least.
*  To say the least.
*  Yes.
*  And obviously you asked about emergence.
*  So emergence is a concept, is a word that has is used, has been used a lot in a lot
*  of the modeling work.
*  So you have to engage with that concept as well.
*  And that's why I got interested in that.
*  Also, I have a classic background.
*  My mother used to be a professor in Greek and Latin.
*  So I grew up surrounded by Greek philosophers.
*  And I was educated in the Southern European system, which values philosophy and the rest
*  more than the Anglo-Saxon, I think.
*  So that's probably my experience.
*  I see.
*  I see.
*  Well, I know that the concept of emergence goes back at least to Aristotle and probably
*  before that.
*  Correct.
*  Yes.
*  So it's a long story.
*  So given your background, now I'm just curious and you know, you don't have to answer this
*  if you don't want to, but coming into sort of the neuroscience world from the engineering
*  and statistical and physiology world, do you have a general take on the state of neuroscience
*  these days?
*  Well, it's a big question.
*  I think it would be disrespectful to have a sort of sort of broad take.
*  Sure.
*  It's such a wide field.
*  I feel like a lot of people get into it and then they're kind of surprised by how little
*  we still know.
*  That's why I ask.
*  So just to explain the attitude.
*  So I trained at NIH as a postdoc.
*  My mentor at the time was Lou Sokoloff.
*  Lou Sokoloff, as many others, he was a psychiatrist.
*  He was pretty much touched by the Second World War and all these men coming back from the
*  Pacific.
*  And the thing that these people decided to do at the time was not touch consciousness
*  or cognition or anything like that.
*  Right.
*  So I was trained into physiology, so metabolism flow.
*  So I come from that background, which is you approach cognition and higher brain function,
*  tiptoeing basically, step by step, little by little.
*  And so it takes to me quite complex subject.
*  So I approach it with respect.
*  And so that's why I wouldn't like to say to give a broad judgment.
*  Judgment.
*  Obviously, I'm also a statistician.
*  So for many, many, many years, I was the chap that was supposed to analyze data.
*  Right.
*  And yes, some of that part is frustrating.
*  I think the frustrating part is from my end, it was the lack of models.
*  So it was just, you know, lots of associations and correlations for not a lot of for model testing.
*  It's changing, I think.
*  Boy, I think the pendulum has swung because it's just models all the way down now, it seems.
*  Yes.
*  And I think also because the models were not good enough.
*  Right.
*  So it's certainly getting much better at the moment.
*  Yes.
*  So that's a really good jumping off point, I think, to start talking about your paper here in neuroscience and biobahavioral reviews
*  called Conflicting Emergences, Weak versus Strong Emergence for the Modeling of Brain Function.
*  And I guess I'll maybe just to not bury the lead, the overall argument here, and then you can add on and correct me,
*  is that some of the recent general theories of brain function or consciousness,
*  including the free energy principle of Karl Friston and integrated information theory of consciousness by Giulio Tononi,
*  suffer in that they're dependent on strongly emergent processes,
*  whereas it might be more fruitful to focus on weakly emergent processes and then scale upward to understand brain function.
*  Is that about accurate or what would you add to that?
*  Right. Yes. So these are just examples of strongly emergent theories.
*  But these are popular instances, yeah?
*  They are popular examples. But for example, after I published that paper,
*  I did receive questions about, interestingly enough, not these two particular theories, because these are not the only ones.
*  Right.
*  I engaged in conversations about Roger Pembro's quantum.
*  Oh, really?
*  Yes.
*  I didn't realize that was still part of the conversation, really.
*  Yeah, you might remember Douglas Hofstadter's book.
*  Of course.
*  So there are many theories out there.
*  And I think that the first reason why I wrote this paper, I write a lot of the papers just for me, really,
*  and asking myself the question, with what theory should I engage and spend time on?
*  I'm a bit older than you are.
*  And when you get older, you don't have a lot of time in front of you.
*  So I think you need to decide how I'm going to spend this time.
*  Some of these models take quite a bit of time to understand.
*  Yes.
*  And particularly a few, I don't want to be specific, are very badly communicated.
*  So for me, this paper was just personal.
*  It was just a test saying, okay, Federico, so you have a few hours on a Sunday.
*  Which ones you think you should read about?
*  And I said, oh, this is a strong emergence theory, so I'm not going to spend too much time on it.
*  I'm going to turn to something else.
*  Does that make any sense?
*  And then if you want, we can go into what is weak and what is strong.
*  Yeah, no, I think that's a good starting off point.
*  Because obviously we need to talk about weak and strong.
*  So just emergence in general, I've had, I've talked on the show a little bit about emergence.
*  I had Paul Humphries on the show.
*  But he and I spoke more about kind of two areas.
*  One was his taxonomy of emergence with respect to sort of our human access to understanding how emergent phenomena arise from lower level processes, right?
*  Like epistemological, ontological emergence.
*  And the other thing we talked about, which I had actually never considered before, was the difference between synchronic and diachronic emergence.
*  Synchronic meaning that the emergent property arises at the same time as its lower level processes,
*  whereas diachronic emergence is where the emergent property arises over the course of time of these lower level processes building up to the emergent process.
*  But we did not talk about strong versus weak emergence, which is what you focus on with regard to the promise of understanding our brains.
*  So what are the broad definitions of strong and weak emergence?
*  OK, so let's say that a strong emergent process can be defined as something that not only cannot be reduced to the mechanics of its components,
*  in the case of the brain to the basic neurobiology, but also cannot be computed at all.
*  In other words, in order to explain this new property of the system, you need to come up with a new principle,
*  something that you wouldn't expect to be generated by the underlying components, individual components of that system.
*  Which to me, first of all, since I think I've already explained why I'm interested in these models,
*  would be a waste of time if this were true, because I would not be able to link directly behavior to biology.
*  Yeah, that's a full stop for you, huh?
*  Yeah, and that would be immediately a stop.
*  But I was also interested by the fact that this had been debated many, many times throughout history, from Aristotle onwards, and has some weaknesses.
*  And the main weakness is that it doesn't seem to work on the metaphysical level.
*  While, again, it's not me saying this, and I didn't come up, you know, I'm not a philosopher, but I'm interested in philosophy.
*  It was your mom.
*  Exactly. So I have to be interested in philosophy.
*  But I think it's important to ask questions on why we're doing what we're doing.
*  I think that is a very decent question to ask, not every day, but I mean, occasionally.
*  But I was also aware that there is the other kind of the way you can refer to a model, an emergent model, which is weak.
*  And again, a weak model cannot be really reduced.
*  So it's component, but it can, its output can be computed through a computer simulation.
*  So these are obviously very general statements.
*  And funnily enough, these are the kind of models that I'm interested in because they really allow you to make predictions,
*  which at the end of the day is an important part of the scientific process and what we do.
*  And I also acknowledge that models linking the biological behavior is difficult.
*  I'm not underestimating the task.
*  Yeah.
*  I think it's a very worthwhile and metaphysically sound way of proceeding.
*  In that because you with a weakly emergent model, you can make predictions and simulate and actually test the predictions.
*  Is that accurate?
*  That is accurate, yes.
*  OK. Well, so we'll talk about the weakly emergent models that you describe and you've worked on actually.
*  But first, let's talk about the examples with the free energy principle and integrated information theory as examples of strong emergence.
*  And maybe you could just describe how those are examples of strong emergence and whatever sort of introductory summary remarks you need to make about those those two different systems, those two different theories, I should say.
*  OK, so first of all, these are just two examples.
*  As I said, there are many others and that is I think already a problem because when you have so many theories, grand theories of brain function, how do you know you're going to decide which one is the better one if they are so loosely linked to the underlying biology.
*  Setting that apart, it's a good question because I don't I don't live in to the the block sphere on the I'm not on any social media, but I'm told that this paper was discussed in a few blogs.
*  And one of the I think misconceptions that I think I've seen in these blogs is the fact that it was my decision to define this to models, the free energy principle and the Tononis model as strongly emerging.
*  Now, as far as Tononi model, Tononi himself, I think if I remember correctly, I think in the PNAS paper in 2013 defined his model as strongly emerging.
*  It would have to be right, because I guess the knock on integrated information theory is that and I know that there's a lot more work being done on this.
*  But I guess the idea is that with a measure of complexity, which is given the name phi, if phi is high enough, which is a measure of the complexity of the system, then all of a sudden you have an emergent conscious conscious being, I suppose you'd say consciousness.
*  I mean, that is almost the definition of strong emergence, right?
*  That's right. Again, there was not any of my doing.
*  Tononi decided to define his model as such.
*  As far as the free energy principle, again, I think there is a reference in the paper.
*  This again is not any of my making.
*  I think the philosophical literature, there are a number of philosophers that are interested in this topic.
*  Obviously, defines this free energy principle as a strong emergent.
*  And now I'm not going to I don't want to discuss a lot of the principle.
*  As you say, you had quite good discussions on this in your previous podcast.
*  Yeah, that's fine, because even even this last one that has not I haven't even aired the show yet.
*  We talk more about the free energy principle and predictive coding in general.
*  So, you know, if it's in the in this paper is written by Lestienne, basically says the free energy principle as an example of Sperry,
*  who was the one that again brought back into neuroscience as strong emerging.
*  And it's clear that FEP has been presented.
*  And it's to me, I understand it as a strong as a strongly emergent principle.
*  So we can then discuss whether this is really true and whether you can or cannot derive this principle, whether it's true or not,
*  which is also another conversation from elementary computer, the mental computation of brain units.
*  Yeah, it's literally it's literally a top down theory in that in that it uses predictive coding.
*  But also the approach is top down in that it is a general computational principle that's supposed to underlie brain mechanisms.
*  And then from that computational principle, then you start looking for examples of how it could be implemented.
*  Correct. And to be honest with you, if I may use an analogy in the British system, we are told that the analogy is the tool of the desperate lecturer.
*  So that's Hofstadter for you.
*  I think it's pretty much, you know, discussing football on the Monday.
*  So it's it's I've seen this theory applied as a postdoc explanation of a very number of large number of things.
*  But to be honest, when I understand it, and this is the other issue, I think I've been in this job long enough to be able to understand quickly
*  a number of theories. And I struggle with this again.
*  I think there is an history, particularly of these authors, of actually obfuscating the topic more than clarifying it.
*  And I know them well being in London. So to me, doesn't really is not telling me much.
*  I think I would like also to add the free energy principle is interpreted largely as a Bayesian.
*  So it becomes the theory of the Bayesian brain.
*  I've been lecturing in elementary statistics in undergraduate and graduate for I don't know how many years since before Bayes became popular again, probably.
*  Exactly. And I can tell you that if there is one thing that I know is that students brain do not work as Bayesian statistics.
*  At all. As a matter of fact, they really struggle to understand it.
*  So I am I am a bit perplexed on the fact that if our brain is so by reason, why is it so difficult to teach Bayesian inference to pretty good students?
*  You see what I'm saying? So I'm not sure.
*  Well, so OK, so I mean, you use these as examples.
*  And what you're what you're telling me is that you're not the one that decided that the free energy principle and integrated information theory are strongly emergent.
*  But but you went from other claims.
*  So maybe we can just talk about strong emergence in general and why I mean, you've touched on this a little bit already talking about metaphysics.
*  But but what is the problem with strong emergence?
*  Why should we veer away from strongly emergent models in the paper?
*  I give an example, which is from Kim.
*  And so, again, it's not something I made.
*  I made myself and I think that example is pretty clear.
*  So Kim talks about to say mental states one and two that somehow emerge from again in a very strong way.
*  So from two physical states again, again, one and two.
*  Now, Kim says that if we assume that M2 is somehow caused by M1, then we have a problem because in the same way, then the mental state and two is explained by the mental state and one week.
*  We could also say that the mental state M is caused by the physical state that underlines and one.
*  So we have two redundant explanations for the same thing.
*  In practice, if this is not clear enough, what this means is that if you don't have a computational or reduction of way of deriving a mental state from whatever is the underlying system,
*  then you are prone to have a very large number of good explanations for the same phenomenon and you will not have a way of deciding which one is better than anyone else.
*  For one and two, how are you going to make predictions particular or how in my more practical way, how on a more pragmatic way,
*  how are you going to establish a scientific program on that model, given the fact that you have no idea how and you will have no understanding how playing with the biology,
*  the neurobiology of the system, you are going to observe magically all these mental states coming up and without any real understanding of what's going on.
*  So there is a theoretical issue and then also a pragmatic issue in my mind.
*  Well, coupled oscillators pass your weekly emergent test here.
*  So how are coupled oscillators a potential modeling regime for weak emergence?
*  And I should just ask you, did you bring your metronomes today?
*  Oh, you've seen my videos. Yeah.
*  So I'm not saying that a couple of oscillators are the only ways we can think about networks and information flow across networks.
*  I think, but they work pretty well at it.
*  One and two.
*  The other thing which I think is I like is as an image is the fact that if you represent brain function with a very, very large number of oscillators that are coupled
*  and that are distributed in the same way that the brain nodes are distributed, you get signals that resemble a lot what you measure in what we call the intermediate phenotype,
*  which is the fMRI data we get from the human brain and the rest.
*  So there is a test of validity for these modes.
*  Yeah. And obviously, the fact that oscillation is basically the product of an excitation and inhibition really allows you to start from the basic tenets, the basic elementary mechanism of neural signals.
*  So you use the example of glutamate and GABA, URGIC, excitation and inhibition in the circuitry.
*  Absolutely. But then you can expand it because, for example, serotonin, dopamine, all they do really, they change the excitation-specific inhibition ratio.
*  So it's like tuning a radio. So as an engineer, to me, I think it's pretty easy to see how this stuff works.
*  Not only that, you can establish once you calculate the cost for a gamma oscillation, which is quite high, you can calculate the energetics of that particular system.
*  And the brain is very costly from an energetic point of view system as well.
*  So you begin to embed your model into a credible neurobiological milieu.
*  And in factors that are likely to influence its development and its functioning.
*  And you can have plasticity. So, you know, it can grow. I think we are just the beginning, obviously.
*  Yeah. Well, so one of the features like you were just describing is that it's scalable, right?
*  So you see it at the microcircuit level, this oscillation. And then when you look in the fMRI signals, you see it as well.
*  And you've actually hypothesized, I believe, that the default mode network that has been pretty popular now for the past 10 years
*  as a series of brain regions, collection of brain regions that is involved in the sort of internalized thought and non-task related behavior.
*  You've hypothesized that this can be viewed almost as an oscillation between the task based areas and the non-task based areas.
*  So that it's kind of an oscillation on a grander scale. Would you say that's right?
*  Yeah. So if to the oscillators you add some sort of self similarity in the way the brain functions, because most biological systems are like that.
*  So they develop in some sort of self similar scales. Then the argument, the model we have tested, we have hypothesized and tested is whatever happens to the micro level should actually be visualized at the macro level.
*  So just to be more clear, so you have oscillations in cortex, but these oscillations that you can call activations corresponds to deactivations in the lateral channels,
*  which means that if a pyrometer neuron is excited through the interneurons, it will sort of diminish, shut down the activity of the neurons that are physically located nearby.
*  Now, if you expand that model to the larger scale, and obviously that is quite important and is commanded, if you wish, by a proper excitation inhibition ratio.
*  Now, if you just scale it up to the whole brain, you would expect that to any excitation, which is, say, physically localized in a certain piece of cortex, there will be other pieces of cortex which will be down regulated.
*  And that is the default network. I think there is a paper from Rob Leach that has shown that the parts of the formal network that get down regulated are always the closest to the activation area.
*  So it's not only, but then you can make predictions. You can say, well, if, for example, in schizophrenia, you have a problem with interneurons.
*  So, and these are the GABA interneurons, the neurons that actually are suppressing, inhibiting the signal, then I should see the same phenomenon as sort of mirrored in the formal network, which is actually the case because there are problems in the synchronicity between activation and deactivation in schizophrenia.
*  But that also, in a way, explains any delusions because these brains are not as good in discriminating between external and internal process.
*  So but that was obviously had to be tested. So how do we test it? We go and use that and measure a GABA, GABA tone in in schizophrenics.
*  And we just finished the work here with a group in psychosis. And I probably they will get mad at me because I'm anticipating the paper. But there is clear evidence of GABA tone reduction in schizophrenia.
*  So, you know, you start having interesting observations at different scales and you beginning to be able to pull these things together. I hope I was not too long.
*  No, no, that's great. You know, schizophrenia is it's like the last frontier, right, of what we need to understand. So that's pretty cool to hear new results on it.
*  But so most of the work most of the work with these coupled oscillators has focused on like on spontaneous neural activity, but in a static way that is without like a system or an agent performing a task or behavior.
*  And you have developed a toy a few years ago, a toy example of how how such coupled oscillator could scale and generate behavior.
*  As you were saying, behavior is the thing that is the ultimate output of our brains. Right.
*  So do you think you can just describe how like that model how the coupled oscillators in a broad way were put together and embodied really in an A.I.
*  agent that that then would use the spontaneous neural dynamics to navigate an environment?
*  Yeah. So first of all, I think it was not me. I mean, obviously I was part of the project. The book was done by Peter Hellier.
*  So the idea was that one day we were looking at these oscillators that were so the way you embed a very, very large number of oscillators and just distribute them using the human conductive as a base.
*  And we were looking at these amazing signals that were resembling the FMRI rest in state.
*  So you would kind of you just turn it on and see what happens.
*  Exactly. Yeah. So but after what you know, sometimes spent looking at this, you're asking yourself the question, you know, so what?
*  Right. So, OK, fine. We have been able to do this, but where is this taking us?
*  And then we realized that we had just gone half the way because in order to have behavior, the brain has to interact with an environment.
*  And and so as it happens, Rob Litch is again also in the section.
*  He's another professor. He has a daughter who is and he was making a game for her.
*  And so we started having a conversation saying, why don't we just use one of these avatars?
*  And we just, you know, project instead of using the gaming, we just project these signals into his brain and we design an environment which was a room and see what happens.
*  And it's a very basic avatar as motor functions and sensory functions.
*  And so and instead of looking at a screen with all these fantastic oscillations, we started looking at an avatar navigating a room and then changing excitation inhibition and looking at fixing plasticity or moving plasticity.
*  We started seeing changes in behavior.
*  And I think in the paper, I think one of the staggering thing is that, for example, if you increase excitation, suddenly you see this avatar banging his head against the wall, which ultimately is if you have seen a an autistic kid is pretty much what you see.
*  And that is sort of suddenly made I think, you know, wow, maybe maybe that's all it is because we're talking about schizophrenia.
*  For me, it's a much bigger challenge is actually autism.
*  I think we still don't have a clear molecular structure or signature for for for this for this disorder.
*  And that actually sparked some predictions on excitation and glutamate in or GABA again, because schizophrenia and autism do have communal features on this particular disorder.
*  So that's that's that's that's where we are at the moment.
*  And this is work that Peter is is is moving forward as well.
*  Yeah, that's what I was going to ask is if if you're developing more in this same environment or building more into the system to elicit more complex behaviors.
*  So I think one of the things we have to do at the moment is a lot of time with this avatar is spent in programming very, very simple things like bipedal movement or.
*  And so we are trying to move out of from that trying trying to find something which is already pre built and just focusing on on cognition.
*  So there are some technical issues.
*  Yes. So the idea is slowly moving towards more complex behavior, particularly social behavior.
*  So you started looking at different avatars in the same environment, how they they may interact.
*  Then I once they showed me a group of avatars playing football, which I'm not sure was a serious experiment to be honest.
*  But what I find fascinating is that a lot of things that you think are complex may not be that complex.
*  I mean, that is the key to emergence that in the end, when you put together a million ends, you start seeing very complex behavior from the elementary unit.
*  So I I say as with the not as an expert, but what this made me understand is that what we think is complex may not be that complicated in the end.
*  Yeah, that underlies the entirety of complexity.
*  Exactly. Yeah.
*  Yeah. Well, I have a couple of things here.
*  One, you know, so you're going to just projecting forward and you so you have companies like DeepMind and OpenAI that are creating avatars to play in social gaming environments.
*  You know, but they're using systems that are based on deep learning and and reinforcement learning and some other bells and whistles in there.
*  And those are brain inspired. If I can use the term, you know, I've talked a lot about them a lot on the show here.
*  But it's a very different approach than your brain inspired approach, which uses these very specific cellular types.
*  I'm just wondering what how you see this kind of work and this kind of approach fitting with respect to that the deep learning deep reinforcement learning approach.
*  Well, it's different. As you say, it's very different. I'm not going to say to you that is better.
*  Yeah.
*  This is just what we are interested in. You know, it's it's fascinating to just sit and create these experiments without not really knowing what's going to happen.
*  And then seeing that happen. And that is probably the difference, I suppose. So at the moment, we just want to learn from these machines.
*  So we are learning, not the machines in many ways.
*  And also, the difference is we.
*  We have the ability of integrating molecular maps of the brain.
*  And this is obviously a very, very long game.
*  But if we start making sense of cellular energy function or the only function, for example,
*  tuning these these avatars and see and see what happens that that, you know, I hope I'm going to see this in my lifetime.
*  Yes, just. But I'm going to be the one learning and not the other.
*  Well, but in so, I mean, you know, your approach is much more closer, much more closely related to the actual physiology of the brain.
*  Whereas in deep learning, it's very loosely modeled on the way that neurons are connected and the way that plasticity works.
*  And in the system, it's updating the weights between units.
*  So it's it's it is a very different approach. And it's it's that's it's really interesting.
*  And I think that's why. And in some ways, that's to your advantage. Right.
*  Because then you're not you're not like competing against these systems, essentially.
*  Like you said, you're learning about how it can work. Yeah, correct.
*  So there is the it's a complete different objective.
*  Also, we want to continue in studying the stochastic aspect of the brain.
*  The brain is not a deterministic machine, which and a lot of the algorithms you define are deterministic in many ways, not all of them.
*  So we I'm also interested in the effect of variability and noise, which is how noise is important for brain function,
*  how the relationship between the environmental variability, environmental noise, if you wish, and brain noise, that's together.
*  I have another life in the city on trading in equities and stuff like that.
*  And and I am aware of the importance of volatility and noise in systems.
*  So so there are a lot of things that can can be done.
*  And yeah, I hope we are different than we I'm really hoping we're going to stay different.
*  Yeah, you talk about the long game and and running out of time.
*  I had Jay McClelland on the show a couple episodes ago, and he and he's one of the early pioneers in parallel distributed processing.
*  And he has this he's made this goal for himself to build mathematical reasoning in a neural network, essentially.
*  And he gave himself ten years. And part of the reason he gave himself.
*  Well, he said it would take at least ten years.
*  But part of the reason why he wanted to put a limit on it is because he wanted to do it before he was dead, essentially.
*  Yeah, exactly.
*  Well, Federico, so OK, so you use the examples of free energy principle and integrated information theory as strongly emergent.
*  Is there a chance, though, that principles like that theories like that could be, you know,
*  is there room for those types of theories to actually be discovered by simulations if you went from the bottom up approach, right?
*  By, in other words, through weekly emergent and a weekly emergent approach?
*  Yes, of course. Yes. I think that in many ways a lot of these approaches are laid out and published too early.
*  I think, for example, Tononi's work, if you look at what he's been producing recently, I think we can calculate this fee if you wish.
*  It's I think the mathematics was a bit lacking.
*  I'm part of the Complexity Centre at Imperial College.
*  And there are new developments in mathematics in trying to calculate, if you wish,
*  emergence from the nonlinear interactions of units.
*  So I think it was basically a lack of tools more than anything else.
*  And I think it might be arrogant to say that more or less all these grand theories, particularly the good ones,
*  then sooner or later will become connected in a way, if you wish, to some form of computation. Absolutely. Yes.
*  Well, they have to by definition at some point if they're going to be viable theories.
*  Yeah. Although I did have someone that corresponded with someone who said that according to Golder theorem,
*  because that is still around, we will not ever be able to do that.
*  So this particular person believed that there was no way we could ever build these bridges.
*  Well, but so you promptly ended your friendship with this person then, right?
*  No, no, no, no. I just pointed out that I should have then quit my career straight away,
*  because then that won't be the point.
*  And also, I think in the paper, we cite an example of things in the past where philosophers were involved,
*  where things were really thought to be emergent.
*  And then that was not the case.
*  You know, a bit more work, experimentation, and then you got chemistry coming out.
*  And the philosophers, there is no philosopher interested in chemistry anymore.
*  They moved on to something else.
*  So that to me is saying something.
*  I think it's just part of the way science works, you know, moving to more complicated things.
*  And there is always someone that coming out and saying, oh, you will never be able to correct this.
*  So far, we've been able to correct most of things.
*  Well, you mentioned getting some responses on blogs that you hadn't read about people saying,
*  well, you didn't include this and that theory in your examples.
*  But I'm wondering if you had any response or backlash or support from people in the free energy principle
*  or IIT community, people with those backgrounds.
*  Have you heard from anyone that is upset with you?
*  No.
*  No, which is interesting because I actually have a few in my institute that actually do that.
*  But nobody engaged.
*  I think the only engagement I've seen is basically in trying to deny that these theories are actually strongly emergent,
*  which I think is an interesting, which is fine, absolutely.
*  Because that what that says is that new energy should be devoted in making these models computation computable.
*  So I think that's fine.
*  Yeah. OK. Well, so you make the point in the paper that strong emergence has been central to most theories of consciousness,
*  including integrated information theory.
*  So how do you devote you devote one paragraph to this in the in the paper?
*  But I'm wondering how you see consciousness fitting into the picture here.
*  Can can we get to an explanation of consciousness through simulations, through a weak emergence approach?
*  Or do we need emergence at all to explain consciousness?
*  Well, again, I think I'm respectfully staying out of this question.
*  I think it's a big it's a it's a it's a very big question.
*  Yes. And I'm very respectful of how complicated and big this is.
*  Do I find this necessary? Personally, no.
*  I've seen accounts of consciousness that actually were already pretty satisfactory.
*  I did like Damasio's. Remember, he had a book called The Discard Error.
*  Pretty nice book. There was an account, a qualitative account of consciousness, which I found quite sensible.
*  But if we want to, I suppose that if there will be a rigorous definition, a model of consciousness,
*  which I hope I will say in my lifetime, there was still a lot of work to be done.
*  And I think piece by piece, you know, it's a big mountain to to to climb.
*  But the composing in gradual, I think they will get there.
*  Well, you keep talking like you're near your deathbed.
*  My grandfather just turned 95. So you're not that old, I'd already go.
*  No, but you know, you never know. I mean, it's not because of that.
*  I think it's just that I think neuroscience is it's a long game.
*  Yeah, that's that's all I want. What I really want to say.
*  Do you think I mean, you already kind of talked about this, but do you think that simulations
*  of things like coupled oscillators will, you know, will lead to a general theory of brain function
*  or general AI, general intelligence?
*  Or do you think it will be something a little bit more like these more theoretically based approaches
*  that you've denigrated with their strong, strong emergence?
*  I think that would be useful in the same way that, for example, the law of thermodynamics
*  establishes general principles that are very, very handy to have.
*  But you can derive these principles from simulations of the of the molecular state of the atomic state.
*  So it's all about linking different levels.
*  And we may not need these simulations in the end, or we may not want to run them all the time.
*  But as long as whatever meta description will will come out is compatible with the atomic state,
*  if the model is compatible with the outputs of these models, then I think then, you know,
*  we might get a step closer to the theories you were referring to.
*  I've asked this to a few guests in the past, but you just mentioned that neuroscience in general is a long game.
*  And it feels like when I went into graduate school, which was, oh, what was it, 12 years ago or something?
*  It feels again like this was the golden era of neuroscience.
*  And it feels now like this is the golden era of neuroscience.
*  Do you think that this is the golden era of neuroscience or is that later?
*  I don't know. I think I think it's definitely the golden era of psychiatry.
*  Because I spent a long time in neurology, which is easier in many ways, because there is no,
*  if you wish, attempt to general theories there.
*  It's more about how an injury can be addressed or, you know, neurodegeneration and so on.
*  What I find exciting is the fact that psychiatric disorders can now,
*  some of them have biological mechanisms underneath.
*  They may not be all true, but and that is if you think about what was going on 20 years ago, 30 years ago, that's a big step forward.
*  And we suddenly we are seeing features of biological features of disorders.
*  I'm working on the immunology of depression at the moment.
*  And, you know, it's it is quite interesting to realize that sometimes we are depressed because there is something happening in our body.
*  And also, and finally, I think we are developing biological models of how brain and body interact, which is quite quite new.
*  Well, the immunology work is really taking off right now, it seems like.
*  Exactly. Yes.
*  So in your in your reasonings that oscillations might be the way or one way to go to understand brains, scalability is important.
*  And scalability means that the brain has essentially fractal qualities, which means that, you know, you can look at it on the microscopic up to the macroscopic level.
*  And you point you pointed out that it's fractal both at the anatomical level and the functional level.
*  That is, as you go from microscopic to macroscopic, there are common characteristics.
*  It essentially looks the same.
*  Why is a fractal quality important?
*  You know, why is it important that brains are functionally and anatomically fractal?
*  I wouldn't say it's important from a pragmatic perspective, because it allows you to make easy generalizations from the micro to the macro.
*  OK, it's it's it's important because it's it's useful.
*  But I think what matters is whether it is true or not.
*  I think what matters is whether it is true or not.
*  I think what again, from a pragmatic perspective, if it weren't true, you would be in trouble, I think, because then it would be really difficult to to scale up all these dimensions easily.
*  So more than important is it's a relief that it's it's worked like that.
*  Obviously, it's it's I don't think we want to say that all of the divide in brain function can be explained by pure self-seminar scalability.
*  The cortex is very much scalable, not entirely sure about subcortical structures, but that already helps quite a bit.
*  And also, if you die is also visible in not only in the brain signals, but in behavior in the way in a lot of systems, manmade systems are done.
*  So it is using my other interest.
*  There is a factor theory of financial markets, for example, which is very popular at the moment.
*  So again, that doesn't explain everything that happens in financial systems, but quite a bit.
*  So I think it's quite a useful, useful conceptual tool.
*  Can you tell me about a time that you either failed at something or got rejected and how you dealt with it and came back?
*  You mean personally or professionally?
*  Probably professionally, but you can answer it however you'd like.
*  All the time, I think.
*  That's always the answer. That's always everybody's answer.
*  Well, see, everyone. So someone in business, like a tech startup, could answer this pretty easily because maybe it's easier to measure failure in that world than it is in the academic world.
*  Maybe that's why.
*  Rejection is.
*  But go ahead.
*  So you're right.
*  So people in business would even like to consider failure.
*  For us, failure is daily. You get rejected all the time.
*  Whether it's a grant, whether it's a paper, whether it's an idea.
*  And actually, sometimes the better idea, the more likely it is to get rejected.
*  That's right.
*  So it's not for everyone.
*  You need to be probably to be arrogant, hyper self-confident.
*  I don't know.
*  There are other things that I can think of that probably I cannot name on your podcast.
*  It takes it takes particular strength to do this job properly.
*  And that's obviously I mean, there are many ways in which you can do a job so you can probably sit comfy and just follow the stream.
*  And if you have your own ideas, if you have things that you want to do, things you believe through better ways of explaining the evidence that are not to anyone, everybody's liking, then prepare for a tough for a tough ride.
*  But that's that's that's fine.
*  Well, you've been in this world for quite some time now.
*  Can you you know, when when you have an incoming maybe not you personally, so that's not personal.
*  But can you see in others whether they have the right amount of resilience to to continue working in the field?
*  Is that something that is readily visible to you when you?
*  Yeah, so that's my job as a as a senior scientist is to but also to protect them in many ways, because I was privileged in the sense I started in the early 90s, which the scenery in Europe and in the States has changed a lot.
*  So the lot now of financial everything is is finance at the moment.
*  Everything is money driven and was not was not like this when I started.
*  The pressures are far greater as a PhD students these days, for example, are not allowed to fail while failure was a key ingredient in the in the PhD when I started, because that basically showed, you know, whether you could do it or not.
*  So it's a different world.
*  And I think there are a lot of I'm privileged to work with very, very talented young people.
*  And so sometimes they say I come to the office with a baseball bat because because my job is just to, you know, to keep the bad guys away and also to allow them to concentrate on the stuff they they they can do and not on the level of the field.
*  And so I think that's a very important thing to do and not on the next grant, the next fellowship, the next, which is quite disruptive.
*  I think you need to give space to creativity and also you need to allow people to fail and allow them to put them together and try again.
*  If they recognize talent, if you recognize talent, they have to take risks.
*  They have to fail.
*  I'm not sure that the system these days allows that anymore.
*  Well, you have, you know, with your background statistics, you know that it's just statistically likely that you know all the time, particularly if you if you are doing science, which is, you know, doing something new, something disruptive, something, you know, and we were allowed to take risks more years ago.
*  And now I'm not entirely sure that's that the system allows that.
*  If you were going to get in to neuroscience these days, and I know that's a very broad field and a broad this is a broad question, but do you looking back, do you appreciate your background in statistics and engineering or, you know, how would you approach going into the field these days?
*  I would say that a quantitative background is key now to whatever you do, not just science.
*  And unfortunately, I know that, for example, statistics is very badly taught, at least in the UK and in Europe in general.
*  But if you are asking specific into neuroscience, then it's all a matter of stretching yourself.
*  You know, yes, I was an engineer, I was interested in stats.
*  In my first postdoc job, I worked with rats.
*  So I was doing experiments as you were doing experiments.
*  And I might supervisor didn't even ask whether I wanted to do it or not.
*  He thought that I had to stretch myself and that is that is really key.
*  And I'm looking forward to do something a bit different next month.
*  So it's stretching, stretching, stretching, doing different things.
*  It's a long game. I don't think I'm a neuroscientist.
*  I'm trying to become one.
*  You mentioned many of your influences as we talked.
*  What is one book or one person that has been a major influence in how you approach your work?
*  Well, the important thing to mention is that a lot of what we do is thanks to the people we have around.
*  So I was basically picked and by I did my PhD, part of my PhD in Italy in a very small hospital.
*  And I was taken to NIH by Gus Sokolov, who was Alaska Price at the time.
*  So yeah, so that is I have to is probably he passed away a couple of years ago.
*  So it was fantastic, incredible guy.
*  And then I trained with Kathy Schmidt at NIH, where I learned how you do rigorous work in neuroscience.
*  I moved back to London and I had two amazing supervisors, Terry Jones and Bing Cunningham, and people that work in impact know them very well.
*  And then I spent 10 years in pathology, the pathology department, working side by side with the pathologists.
*  And then I was in Manchester looking at tissues.
*  Amazing experience again.
*  So and as I said, now it's me being surrounded by people that are far more intelligent than I am, far more talented than I am.
*  And it's just a pleasure just to see them coming up with ideas.
*  And so I enjoy my time here because of that.
*  One of the themes that keeps coming up is, you know, you talked about stretching yourself and, you know, it occurs to me that these days a lot of what is called for our experts in very narrow domains.
*  But from what you're saying, it would be beneficial still to maybe not be a Renaissance man, but at least to explore a variety of topics in some depth.
*  Am I reading it right?
*  Absolutely. So that's why what I'm it's not easy.
*  I mean, not everyone wants to do it.
*  You're more comfortable in your little garden.
*  And so sometimes with postdocs here, it's a matter of kicking them out and saying, no, you're now doing this different.
*  And they may become uncomfortable for a month or two.
*  But then suddenly, you know, you push them into a completely different area and suddenly they come up with incredible ideas and at the same time having good collaborators.
*  So again, the team we have here is computational scientists, but there are neuropharmacologists, clinicians, biologists.
*  You need all these to make any sense.
*  And unfortunately, as I said, I spend a lot of time in pathology and missing that enormously just looking to the microscope.
*  Oh, yeah. Yeah.
*  Well, finally, Federico, thanks for all your time here.
*  And I'll let you go kick a postdoc out in just a minute here.
*  But what is what's something that you wish was on your CV but isn't the oh, my next project.
*  That's obvious. So that was keeps me alive.
*  I mean, you know, it's another project now.
*  I spent a few weeks without one after the emergence.
*  And then this other idea came into my head.
*  And now I'm looking forward to working in it and trying to make it make sense.
*  That's wonderful. I was just listening to a different podcast today about how common it is when someone, you know, even if they're in business or whatever, they're in if they go on vacation after working for so long, so hard or they retire.
*  And then all of a sudden they have the major heart attack and perish.
*  So I think it's it's good to be excited about your next project.
*  Yeah, yeah, yeah, absolutely.
*  I'm fortunate I never switch switch off.
*  I'm told by family.
*  So which is not a talent is a problem.
*  But I guess that's that's that's where it is.
*  Well, thanks again for your time.
*  And I guess we'll switch off the podcast here.
*  But you can carry on with your project, sir.
*  Thanks, Federico.
*  Thank you very much for your time.
*  Brain inspired is a production of me and you.
*  You can support the show through Patreon for a microscopic two or four dollars per month.
*  Go to brain inspired dot co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show and prohibit any annoying advertisements like you hear on other shows to get an idea of what's going on.
*  And I'm sure you'll find a lot of great content.
*  So I hope you'll be able to find a good show.
*  And I'll see you next time.
*  If you want to get in touch with me, email Paul at brain inspired dot co.
*  The music you hear is by the New Year.
*  Find them at the New Year dot net.
*  Thanks for your support.
*  See you next time.
*  You.

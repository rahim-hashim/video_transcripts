---
Date Generated: June 10, 2024
Transcription Model: whisper medium 20231117
Length: 5399s
Video Keywords: ['brains', 'neuroscience', 'free', 'energy', 'friston', 'bayesian', 'brain']
Video Views: 32200
Video Rating: None
Video Description: Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2020/03/09/87-karl-friston-on-brains-predictions-and-free-energy/

Patreon: https://www.patreon.com/seanmcarroll

If you tell me that one of the world’s leading neuroscientists has developed a theory of how the brain works that also has implications for the origin and nature of life more broadly, and uses concepts of entropy and information in a central way — well, you know I’m going to be all over that. So it’s my great pleasure to present this conversation with Karl Friston, who has done exactly that. One of the most highly-cited neuroscientists now living, Friston has proposed that we understand the brain in terms of a free energy principle, according to which our brains are attempting to model the world in such a way as to minimize the amount of surprise we experience. It’s a bit more complicate than that, but I think we made great headway in explicating some very profound ideas in a way that should be generally understandable.

Karl Friston received his medical degree from King’s College Hospital, London. He is currently Professor at the Institute of Neurology, University College London, and Wellcome Principal Research Fellow and Scientific Director of the Wellcome Trust Centre for Neuroimaging. Among his major contributions are statistical parametric mapping, voxel-based morphometry, and dynamical causal modeling. He is a Fellow of the Royal Society, of the Academy of Medical Science, and of the Royal Society of Biology. Among his awards are the Young Investigators Award in Human Brain Mapping, the Minerva Golden Brain Award, the Weldon Memorial Prize, the Charles Branch Award, and the Glass Brain Award for human brain mapping.
---

# Mindscape 87 | Karl Friston on Brains, Predictions, and Free Energy
**Mindscape Podcast:** [March 09, 2020](https://www.youtube.com/watch?v=TcFLQvz5uEg)
*  Hello everyone and welcome to the Mindscape Podcast. I'm your host Sean
*  Carroll and in the course of doing many podcasts interesting phenomena arise
*  when I look at what the comments are and from various sources whether it's email
*  or Twitter or comments on the web page or on YouTube or Reddit. Different podcast
*  episodes have different spirits in some sense. Sometimes we're big picture, right?
*  We're sort of talking about various ideas from a very high level view and it's
*  more inspirational than challenging, right? It's like thinking about things
*  rather than getting a lecture in them. Other times we get a little deeper. We
*  kind of get our hands dirty. We get into the weeds. We try to dig into some
*  specific example of something. Either way I will get complaints that I know and
*  you know what? I love and cherish the complaints because I want constructive
*  feedback. I want to hear what people have to say but honestly going forward
*  realistically it's going to be a mix of both kinds. So today we're getting our
*  hands dirty. We're gonna get into the weeds. Don't be afraid, you know, don't
*  think that well this is gonna be a slog or anything like that. This is one of the
*  most fascinating episodes I think that I've done here on Mindscape and perhaps
*  the most useful in a sense I will explain to you in just a second. Our guest
*  is Carl Friston who's a neuroscientist at University College London and Carl
*  Friston is by many measures the most influential neuroscientist alive today.
*  The most citations, the highest H index, all these different quantitative measure
*  of scientific success. He is a practicing psychiatrist and is very interested in
*  schizophrenia and he serves patients but he has also contributed to neuroscience
*  more broadly most obviously in developing techniques for imaging the
*  brain. Ideas like statistical parametric mapping, voxel based morphometry. I really
*  have no idea what these ideas are. Sorry about that. What I'm interested in is
*  where he's moved more recently in his career into the theory of how the brain
*  works and he's been developing an idea called the free energy principle. It's
*  part of a bigger set of ideas called the Bayesian brain. The idea that what the
*  brain is trying to do is to model the world around it and therefore develop a
*  little picture of what's going to happen next using Bayesian inference.
*  Something you all are experts on because you've all read the big picture or
*  somewhere else. Bayesian inference is getting data in and using that data to
*  update your beliefs about the world. The free energy principle is Friston's idea
*  for how the brain effectively does that. It turns out that calculationally
*  updating your beliefs about the world can be very very hard. The free energy
*  principle is a way to sort of simply and quickly get to an effective view of the
*  world. The basic idea is that the brain is constantly trying to minimize
*  surprise. It's trying to develop a model for all the stimulus, all the sensory
*  input that it's going to get that is least likely to be surprised by
*  something new happening. That sounds simple but when you get into it, when
*  you look at the actual way it's supposed to work, it actually turns out
*  to be pretty darn complicated and intimidating. Famously there's a large
*  number of people in a lot of different fields, not just neuroscience but deep
*  learning, machine learning, biologists and physicists and a whole bunch of
*  people who have trouble really figuring out what this is all about. I really
*  think that in this podcast we present quite an understandable picture of what
*  it's all about. There's some jargon but we explain what the jargon is. Of course
*  Carl understands what it's all about but I think that we're able to give enough
*  examples, talk a little bit about why the brain would work this way and what it's
*  supposed to be, why in particular he's interested in it from the point of view
*  of addressing schizophrenia and other problems. To me of course I'm biased. I
*  know a lot about free energy and entropy and measures of information theory etc.
*  But I think we did a good job of uncovering what's going on here. You know
*  there's no equations in the podcast but the ideas I think are out there. This is
*  the kind of episode which it really repays listening closely to. I think you
*  can learn a lot and learn about something that is really at the absolute
*  cutting edge of modern neuroscience. I also want to mention a tiny little
*  announcement. You know that I have a Patreon account that you can find on the
*  web page, preposterousuniverse.com slash podcast. There's a link to the Patreon.
*  One of the benefits that Patreon users get is that they get a monthly ask me
*  anything episode. So Patreon users ask me questions. I try to answer as many of
*  them as I can and someone on Patreon suggested that even though it makes sense
*  that Patreon supporters get the ability to ask questions, the ability to listen
*  to the answers might be more widely shared. So I'm working out a way to do
*  that. Every month there's like a two or three hour episode that I put on Patreon
*  and right now it is only for Patreon listeners but going forward I'm going to
*  try to figure out how to make those answers available to anyone. Right now
*  the only way to do it is going to be to go to the Patreon page every month when
*  they appear but hopefully I'll figure out a way to put them into the regular
*  podcast feed. The trick is that it cost me a lot of money to put two or three
*  hours worth of gigabytes of data onto the podcast feed because my host is
*  really expensive. It gets paid for by the ads. It's not clear whether we can
*  get ads to pay for the AMA or not. Let me know, you know, especially on the
*  comments in the blog post associated with this particular episode, whether or
*  not this is a good idea at all, whether people would be interested, would it
*  make sense just to include like one hour's worth of answers, then you can go
*  to the Patreon page to get the rest, etc. etc. But I think it's a different kind of
*  thing. It's not going to replace regular Mindscape episodes but it might be a
*  different way to get some ideas out there and talk about them. And with that,
*  let's go!
*  Karl Welfristen, welcome to the Mindscape Podcast. Thank you. Glad to be here. I figured we
*  would talk about this thing called the free energy principle, which you've been
*  investigating and championing for a while now, but maybe just to get there
*  rather than just start by defining that, could you just explain what is the
*  problem that we're trying to solve? What is the question that we're trying to
*  answer by talking about free energy? From my perspective, it's trying to find a
*  first principle account of sentient behavior and just very practically that's
*  relevant because of my background, which is a psychiatrist. So very simply, as
*  Richard Feynman says, if you want to understand something, you've got to be
*  able to build it. If you want to understand psychiatric patients, you have
*  to, in some minimal way, be able to build or simulate sentient behavior that goes
*  wrong. So that's basically how I got into it. So you were actually a
*  practitioner with patients and the whole thing transitioned out of that? Yes,
*  slowly but surely, yes. I transferred my angst from patients to students.
*  I spent an early part of my life in a therapeutic community with 30
*  chronic schizophrenics, which was an eye opener for several years. I can imagine.
*  Yeah, okay. So we want to understand how the mind works, how the brain
*  works, in part to help fix it when it goes wrong. That's the ultimate agenda
*  because I got seduced away from clinical psychiatry into systems, neuroscience,
*  and brain imaging. The question became slightly less focused and more how
*  does the brain work? That became relevant when you're trying to
*  characterize or analyze neuroimaging time series from things like
*  functional magnetic resonance imaging or electroencephalography. So to make
*  sense of these data, you have to have some conceptual generative or forward
*  model of what's actually under the hood. Sure, otherwise it's just a bunch of time
*  series data. Yeah, and neuroimaging is sort of where you made your money, as it
*  were, right? That's my day for a while. And thinking about the grand theory of the brain is what
*  we're doing now. So good. So that's enough for me to dive into free energy, except
*  that you had this lovely story that I've heard about woodlice when you were young
*  and seeing them scurry around. That does set the stage very nicely. If you could
*  tell our listeners that story. Right. Well, that was my first, looking back, my
*  first sort of scientific insight. So it was a hot summer's day and I must have been
*  between five or eight years of age playing in the garden and just became
*  preoccupied by watching little woodlice scurrying around, noticing that they
*  tended to avoid sunlight, that they ended up in underneath bits of rock or wood in
*  shady places. And just looking at this, I thought that's interesting because that
*  looks like purposeful behavior. It looks as if they are purposefully in a gold
*  directed way avoiding the sunlight. But then there was another interpretation
*  that came to mind. Well, yes, but you would also see exactly the same
*  phenomenology if they just move more quickly when they were warmed up by the
*  sun. So there was a more deflationary account. I didn't use these words at the
*  age of five. The essence of the insight was, well, there's a much simpler
*  explanation for what's going on here. For this sort of very elemental form of
*  self-organization, ensemble dynamics. This is a simple explanation. Things just
*  move fast when they're hotter. And that notion, that sort of deflationary, simple,
*  almost verging on a tautology explanation for self-organizing behavior,
*  kept sort of representing itself throughout my education. So natural
*  selection, I think, is another nice example of that. If it doesn't work, you
*  move in some phenotypic space right through to physics at Cambridge and sort
*  of density dynamics and the Fokker-Planck and quantum physics. Again, if
*  it's not good, if it has a high potential, just get out of there.
*  Were you a physics undergraduate?
*  Natural sciences, yes. So half psychology and half physics, quantum physics.
*  I had no idea. So the audience don't, you know, I don't seek out people who were
*  physics undergraduates, but I find them in all sorts of fields.
*  Apparently, yes.
*  But in a deflationary way, just because you move away from people who are
*  physicists.
*  That's right, exactly. So, but I love that kind of story because it's an example of
*  what I talk about a lot in the big picture, this emergence of purportedly
*  higher, well, purportedly purposeful, teleological, goal-directed behavior out
*  of, you know, things just obeying the laws of physics one way or the other,
*  right? And so that's the kind of thing that you saw in your undergraduate
*  education and even today, I presume, in studying the brain?
*  Yes. Well, I mean, at its heart, that is the free energy principle that, you
*  know, we've been promoting.
*  It is very much this deflationary getting back to the first principles and then
*  rebuilding up on that and seeing what would this kind of behavior look like in
*  a sufficiently itinerant context.
*  How would it be fit for purpose to explain the behavior of you and me?
*  Or starting at a slightly simpler level, would it be fit for purpose in
*  explaining a thermostat or a virus or something, an ensemble of bacteria or
*  the like? So it's a question of how far can you get from first principles as a
*  principal account of sentient behavior?
*  So we get back to the human brain.
*  And of course, that is in terms of writing down the dynamics, the mechanics
*  and specifically in mathematical terms, becomes necessary if you want to write
*  down formal models of brain imaging time series.
*  So there's an interesting dialogue between the rather self-indulgent
*  theoretical neurobiology side of it.
*  Yeah, what I often refer to is the work that you do at the weekend when the
*  pressures are off and the day job, which is analyzing brain brain data.
*  Both sides inherit from each other in a very interesting way that you're
*  constantly building models of how the brain works and then testing those
*  models in relation to the empirical data you get from brain imaging, which
*  forces you, puts pressure on you to actually sort of think, well, what's the
*  simplest sort of dynamical functional computational architecture that could
*  possibly explain these data when I look at this sentient creature that usually a
*  normal subject, human subject, when exposed to these experimental
*  manipulations. And yet on the other side, the very algorithms or schemes or data
*  analytic approaches that you apply to make the inference about, you know, is
*  this the right model of the brain or is that the right model of the brain
*  themselves now become inherit from the theoretical work?
*  Because if you can solve how a brain works, that's the best sort of data
*  analysis machine you can possibly have.
*  And then that helps with analyzing the actual data.
*  Has it affected what data you collect?
*  Yes, yes.
*  I mean, that's true in both senses.
*  It's true in terms of me as a sentient creature.
*  You're an example.
*  Yeah.
*  I looking around and I'm literally collecting visual data as I circuited
*  around the room, interrogating your face, trying to anticipate who's turn it is to
*  talk, whether you've understood me.
*  So I'm selectively sampling the right kind of data to resolve uncertainty about
*  those hypotheses that are relevant to my behavior at the moment.
*  Sure.
*  And in exactly the same way as a, you know, as a neuroimaging scientist, I
*  designed those experiments to solicit the right kind of data that resolve my
*  uncertainty about my hypothesis, about the functional integration of the
*  hippocampus with the prefrontal cortex.
*  Same stuff.
*  It's exactly the same principles.
*  Good.
*  Except now I'm self-conscious that everything that I do, you're right.
*  I mean, of course you're going to be looking at my face in a different way
*  than you're looking at the desk in front of you, which you see every day, right?
*  The surprise, all the new information is much larger for something like that.
*  So, okay, good.
*  What is free energy when you think about it?
*  Because I'm a physicist and I have a definition and I think it's a little bit
*  different than yours, but there's a mathematical relationship.
*  So I want to clear up for everyone in the audience what we mean when we use these words.
*  Right.
*  So when I talk or when people, when I say I am a bit self-centered, when people in
*  things like machine learning talk about free energy, they mean variational free
*  energy.
*  So technically, if you were talking to somebody from machine learning, we're
*  talking about an evidence upper bound.
*  They switched the sign in machine learning, so often called an evidence lower bound
*  acronym ELBO, which confused me for enormous amounts of time.
*  I literally thought it was part of your body.
*  That's asking for trouble, really.
*  So it's a statistical information theoretic concept, which licenses your
*  previous discussion about hypotheses and inferring this and rich information.
*  So its scores basically are bound on the technically the self-information or the
*  log probability of some data given a model of how those data were generated.
*  So from a pure...
*  So sorry, that's the crucial thing.
*  There's a model and there's data and we would like them to match.
*  Yes, absolutely.
*  So, well, let's just rehearse that, because that's absolutely fundamental.
*  So everything that we talk about, either in terms of sort of sentient behavior and
*  the free energy principle as applied to sentient artifacts, or in terms of actually
*  analyzing data, rests upon this notion of a generative model.
*  Generating what?
*  Generating data, generating sensations, generating any observables.
*  And an even more simple expression of that is you have to have some way of
*  articulating a mechanics of causes and consequences.
*  So the generative model causes or is a description of how causes generate
*  consequences, and in this instance, the consequences are sensory observations or
*  data, observables, measurables.
*  The causes are the sort of the latent variables, features, structures, whatever
*  you want to call them, that are responsible for generating those things.
*  So central to the free energy as a scalar functional is a generative model.
*  So it's only defined in relation to a generative model.
*  So that tells you immediately the free energy, the variational free energy is a
*  functional, a function of a function, and the function that is a function of is a
*  probability distribution or a belief.
*  So this is your brain giving probabilities to the various things it might experience
*  out there in the world, and the free energy is a way of measuring, all to say,
*  relating that prediction for what you see to what you actually see, and then sort of
*  what measure is it?
*  What does it characterize really?
*  Well, exactly as you defined it, it's a measure of the surprise that you would have.
*  And I'm using surprise in a sort of, you know, well, I actually used a folklore
*  sense, a folk psychology sense, but literally the surprise or the self-information.
*  There is a technical version of it, which is in this case pretty close to the full
*  version.
*  Yes, absolutely.
*  So it's the surprise that you would associate with a bunch of data, given a
*  belief or a model about how those data were generated.
*  So technically it's also called the marginal likelihood or the logarithm, the
*  negative logarithm of the marginal likelihood.
*  And that marginal likelihood is also called model evidence.
*  And all this rhetoric becomes important because, you know, you can gracefully move
*  from one interpretational stance to another one without making any mathematical
*  moves whatsoever.
*  Right.
*  The math is, it carries over.
*  It's just exactly the same.
*  Yeah.
*  But depending upon how you grew up or how you appreciate these quantities or what
*  the rhetoric that you would interpret them, you get a very different look and feel
*  to the fundamental behavior of systems that look as if they're minimizing the
*  variational free energy.
*  So if this surprise is interpreted from the point of view of a statistician, so the
*  brain as a statistical organ, a little scientist inside your head, then if it is
*  in the game of minimizing its variation free energy, its evidence bound, that
*  makes it appear as if it is maximizing model evidence.
*  What does that mean?
*  Well, it will look as if it's gathering information in the service of seeking
*  evidence for its own existence.
*  And this translates nicely into a philosophical concept, self-evidencing.
*  So another way of looking at this purely mathematical sort of behavior is in terms
*  of self-evidencing.
*  So you have lovely little phrases like, you know, people going around gathering
*  evidence for their own existence.
*  Which is mathematically truism.
*  So that's certainly one.
*  Or you can look at it the other way around.
*  We're trying to minimize surprise.
*  So what would that look like if you were taught to think about things in terms of
*  information theory and uncertainty?
*  Well, mathematically expected surprise, expected self-information is entropy.
*  Entropy is one way of describing uncertainty.
*  So what does that mean?
*  It means that you look as if this creature or this artifact or this system is gathering
*  information in the service of resolving uncertainty.
*  Uncertainty in relation to its model of how we think the world works and in particular,
*  how it is situated within that world and sampling from that world.
*  So that brings us back to your phrase earlier on about looking around, not looking at my
*  desk because there's no rich information there.
*  I'm not going to be surprised.
*  Hopefully.
*  Just to reassure you, I haven't got my glasses on so I can't see.
*  It doesn't look very surprising to me.
*  So what is another way in information theory of articulating the notion of rich
*  information?
*  It's just minimizing uncertainty.
*  It's maximizing the relative entropy as scored by the technically the KL divergence that
*  is part of an expected free energy.
*  But put more simply, it just means that minimizing free energy or making moves that
*  will minimize free energy in the future simply means maximizing information gain or
*  optimizing some divergent measure, literally making your mind up in the sense of moving
*  a belief, moving a probability distribution from one prior belief to a posterior belief.
*  And the more information that you can have at hand, you will assimilate and the KL
*  divergence will in this instance be greater.
*  And that's a very important part.
*  And when you actually write down the imperatives for action, that becomes a very,
*  very important part.
*  And this kind of makes intuitive sense, right, that our brain would like to carry around
*  with it a model of the world such that it typically looks around and says, yes, that's
*  more or less what I would have expected.
*  Right.
*  And so the free energy is the difference between what it's sort of expecting and what
*  it's seeing.
*  So it wants to minimize that.
*  Absolutely.
*  And it's completely information theoretic, which I need to say out loud because, of
*  course, the word energy appears in it.
*  And as a physicist, we have a notion of free energy that it's a kind of energy you can
*  use to do useful work.
*  And in fact, in the thermodynamic system, when you maximize entropy, you're minimizing
*  free energy and vice versa.
*  If you have a box of gas that is in equilibrium, it has no free energy, lots of
*  entropy.
*  If it's all bundled up on one side, it's the opposite.
*  But you're looking at a context in which the brain is both minimizing a kind of
*  entropy and minimizing a kind of free energy.
*  That's a great paradox.
*  Now, I should try to unpack it.
*  Yes.
*  But we are right in the depths of the mechanics.
*  Yeah, that's OK.
*  So I apologize in advance.
*  So let's just back up.
*  And it'll pay off later.
*  We'll, you know, we'll bring you down to Earth.
*  Don't worry.
*  OK.
*  So let's just start from, you know, you've gone to university, you've learned that
*  free energy is that amount of energy that is available to do work that, you know,
*  there's not locked into the entropy.
*  So the total entropy is the expected energy minus the entropy.
*  So what that would suggest in terms.
*  So the first thing to acknowledge is that the form of the free, the variational free energy
*  is formally identical to a sort of, you know, a Gibbs or a thermodynamic equation.
*  It's the same equation.
*  The same equation.
*  The only move you make is you drop Bilton's constant from the channel entropy.
*  That's all you do.
*  We said it equals one anyway, so it doesn't make any difference even there.
*  There's no difference between us, we are.
*  Speaking the same language.
*  And on that view, what does that mean?
*  Well, that means if you now write down the energy as a potential, a potential energy,
*  and I'm thinking now from the point of view of a statistician, for example,
*  what's the potential energy that gets into the variational free energy?
*  Well, it's effectively the accuracy.
*  So it's the negative log probability of getting these data given the parameters of my generated
*  model, given all the variables, the quantities, the structure of my model of what could have
*  caused those data, my hypothesis, if you like, that is parameterized, and that's quite important.
*  So the accuracy is just basically the surprise that we were talking about before.
*  I should say the way that you described, you know, it makes sense having a model in the world
*  we can make predictions and then we can test those predictions against sensory
*  impressions.
*  It's absolutely spot on.
*  And indeed, there's a whole industry in both in terms of data compression and engineering,
*  but also more recently in neuroscience and particularly cognitive neuroscience
*  that is predicated on predictive coding, which is exactly that.
*  So prediction errors are just the mismatch between what your generated model predicted
*  and what you actually sample.
*  You take the sum of squared prediction errors, you weight them by some precision or inverse
*  variance, that is basically free energy.
*  Yeah, it's just the other under some simple assumptions about the generated model and,
*  you know, the nature of random fluctuations.
*  So predictive coding is one instance of the more general notion that we're in the game
*  of minimizing our free energy.
*  So coming back to this, you know, the physicist conception of free energy in
*  systems that have attained equilibrium.
*  What does it then mean to minimize the free energy?
*  Well, you're trying to minimize your energy, which is maximizing your accuracy, minimizing
*  the surprise, averaging out your ignorance about the parameters.
*  And then you try to maximize the entropy.
*  Now, that may seem paradoxical, which is why it's good.
*  Or why I apologize.
*  We're going to have to resolve.
*  So I've just said, if you remember, minimizing uncertainty by choosing the right moons,
*  that will get the most information, resolve the greatest uncertainty, looks as if it's
*  trying to maximize the information gain or the relative entropy.
*  But now I'm saying, well, minimizing free energy will require a maximization of entropy
*  from the physicist's point of view.
*  And that's absolutely right.
*  So the key distinction is basically what I do at this moment in time will always be to
*  maximize my accuracy or my energy in terms of minimizing this sort of prediction error,
*  whilst at the same time, maximizing my entropy, keeping my options open, because the entropy
*  that we're talking about is an attribute of a belief about the causes of my data.
*  So this is not an entropy measure of the brain by physically.
*  Right.
*  It's not the molecules in your brain that we're treating as a thermodynamic system.
*  It's a set of beliefs.
*  Absolutely.
*  So these beliefs are then driven to be as broad as possible, entirely consistent with
*  the second law of thermodynamics.
*  So there's an imperative, there's a drive to disorder, and the entropy will increase.
*  But it's the entropy of our beliefs.
*  Now, what does that mean?
*  Well, it basically means I'm trying to find a low energy explanation for my data,
*  whilst at the same time, keeping my options open.
*  So this is essentially Occam's razor.
*  It's basically not committing to a very precise posterior belief.
*  If I've seen these data, then I believe this caused it.
*  So you don't want to commit to a very precise one.
*  So you've kind of found the simplest, the most accommodating explanation for your data.
*  So that's where the paradox, if you like, in terms of whether you're trying to maximize
*  or minimize the entropy term comes in.
*  But I think more fundamentally makes the point that the entropy we're talking about at the
*  moment is a function or a scalar functional of a belief about something.
*  It's not the thing that is encoding those beliefs.
*  It's not the neuronal firing or the molecules or the atoms.
*  The twist, the sort of the slightly paradoxical aspect of this is when you move into the future
*  and when you have the beliefs about the consequences of an action, say looking over there or
*  Googling a certain entry or going to Wikipedia, before you make that action, you have beliefs
*  about how your free energy is going to change.
*  And at that point, your entropy or your relative entropy effectively switch around because the
*  outcomes now become random variables.
*  You have to take an expectation.
*  This is a bit technical, but it's a beautiful little bit of techie stuff, which basically
*  flips this imperative to minimize these entropy and relative entropy when you're applying it
*  to the system as it is now, as it is behaving.
*  When the system looks at itself, say, well, how would I have to now act in order to minimize
*  my free energy in the future?
*  I now include basically outcomes as random variables and they get into the expectation
*  operators and suddenly you're then in the service of minimizing the entropy.
*  So there's this sort of yin yang, which means that as I'm currently processing my data,
*  I'm striving to find the explanations that maximize my uncertainty because I don't want
*  to commit to a particular belief.
*  Yet at the same time, I'm going in the exactly opposite direction.
*  I'm trying to sample those data that will shrink my uncertainty.
*  And then when I find that balance, then we have this sort of active self-evidencing.
*  Let me try to put it in my words and you can tell me if I'm coming close here.
*  I mean, we want to minimize the times that we're surprised.
*  You might think, well, just predict the thing you think is most likely to be true all the time.
*  But if you put 100% probability on that, then any time that you're not exactly right,
*  you're hugely surprised and that's bad.
*  So you might say, well, let's do the other thing.
*  Let's have no beliefs about anything.
*  Let's say anything could happen.
*  But then in some cases, especially when you go through the math, you're always surprised.
*  Everything that happens is a little bit unlikely because it could have been anything else.
*  And so there's this compromise where you sort of try to home in on something you think is
*  most likely, but you do give allowance for the deviations.
*  Absolutely.
*  Beautifully put.
*  And as a sort of a physicist, what you could understand, what you've just said as is basically
*  how do we describe systems that have some itinerancy, but they still restrict themselves
*  to a limited part of their face space or their state space.
*  So it's not one point.
*  We're not little marbles or moon rocks, nor are we gases.
*  There that we are.
*  We certainly have boundaries and we have a shape and a form in the sense of those parts of the
*  state space we could occupy or where the woodlice are running around.
*  There's a structure there.
*  So that structure, if it is the case that these sorts of systems exist, things like you and me
*  or anything actually exists in a non-trivial way.
*  By non-trivial, I mean basically having an attracting set that is just one being in one
*  state deterministic.
*  Absolutely.
*  Then there has to be this balance between this itinerancy, this sort of
*  the expiration of a face space in a structured way where many regions are visited, but some regions
*  are visited more often than other regions.
*  When you start to think about, well, how would you articulate that mathematically,
*  you start to get sort of random attractors that inherit from under-diagonal systems.
*  So what you're saying is there's an attracting set out there.
*  It is not its probability distribution.
*  If I measure the probability of finding me at any point in my state space
*  over a very long period of time, it's certainly not uniform.
*  I have a shape.
*  I have a temperature.
*  Something's more likely than that.
*  Absolutely.
*  Yet I am not a fixed point.
*  I am not just in one state.
*  So what you are talking about effectively is a non-equilibrium steady state.
*  It is not the kind of equilibrium steady states that physicists knew and love and know and love
*  and were taught in the 20th century.
*  This is the new challenge of understanding non-equilibrium steady state in open systems
*  that exactly have this delicate balance between it being a point attractor and being completely
*  diffused at the end of the universe, if that's the way it's going.
*  Just parenthetically, I did have Antonio Demacio on the podcast a little while,
*  and his favorite word in the universe is homeostasis, right?
*  The idea of keeping within this tiny little range as much as we can,
*  but some flexibility there.
*  Yeah.
*  And you want to do, correct me if I'm wrong again, but you really want to say that this
*  minimization of free energy and surprizal is sort of the key to unlocking what the brain does,
*  right? It's the underlying thing for most everything.
*  Yeah, it is. Absolutely.
*  I mean, there's a joke in my group meetings that the answer to any question is model evidence.
*  Usually, it's-
*  It can do worse, yeah.
*  Certainly, when you're talking about colleagues and research fellows and,
*  you know, whenever they ask the question, well, what happens if this is like that?
*  Well, get the evidence for that hypothesis and then, you know,
*  and then you can quantify your beliefs about whether it was like that or whether it broke
*  like that or whether that difference is in play.
*  So can I come back with another parenthesis because I think it nicely
*  falls on from Antonio Demacio's focus on homeostasis.
*  Of course, the roots of much of self-organization to non-equilibrium steady state
*  inherit from the work of people like Ross Ashby, who made apparent his ideas through the homeostat.
*  So it's exactly the same or the good regulator theorem.
*  I think that this is just my personal opinion. I think that physics has a lot of work to do
*  and there's a lot of discoveries to be made along exactly these lines. You know,
*  where non-equilibrium statistical mechanics is a booming growth field that I need. I try to get
*  my colleagues excited about it, but they're used to doing their things. It's a tricky
*  kind of pre-paradigmatic area where we don't exactly know.
*  I don't know because I became a psychiatrist and left the physics behind, but certainly
*  surfing the web, that pre-paradigmatic thing, that's very exciting, isn't it?
*  Oh, yes, exactly.
*  21st century physics.
*  It's much more comfortable when you know, like in particle physics or cosmology, where I was
*  raised, you know what the questions are, you know what would qualify as an insight. Whereas in
*  complex systems, dissipative systems, Ilya Prigogine was an early pioneer here also, right?
*  Self-organization, and we just don't know what words to use. We don't know what equations to use,
*  but I think like you, I'm a fan of these sort of statistical mechanical lenses at which to
*  view these things.
*  Yes, I'm sure that's the only way really to, well, for me, it is the only way to write these
*  things down because at the end of the day, you actually have to have a model in code that
*  generates predictions to analyze the brain data. So you don't really have the, unless you're a
*  philosopher or you write books, there is no-
*  Need to be able to give it to a computer and ask it how well you're doing.
*  Let's just do sort of the reality check for this perspective here. I certainly get that if I'm
*  driving down the street, I would like to be surprised as little as possible, but isn't it
*  true that also informally, I do sometimes seek out new experiences, right? How does that fit in?
*  Well, it's exactly that sort of paradox that we were addressing technically in terms of the
*  difference between me at this point in time, this moment, minimizing my free energy via a
*  maximization of the entropy uncertainty of my explanations or beliefs about what's going on now
*  and choosing those actions that will in the future minimize my expected free energy.
*  So that basically means that when you talk about the expected free energy conditioned upon a
*  particular action move, looking over there when driving the car, you have this opposite imperative.
*  So now you become information seeking, now you become a curious creature, now you become
*  sensation seeking, but it's a particular kind of sensation seeking. It's those sensations that
*  would resolve uncertainty about what would happen if I did that. Because behind a lot of the ways
*  I've just described that is a sense of me as an agent. So once you generalize the non-equilibrium
*  physics of sentient systems to write down what might be the imperative for the way that they act
*  upon the world, that they evidence their agency and you make the assumption that, or you try to
*  prove it can be no other way, that they will act in the service of minimizing the long-term average
*  of free energy in the future, then you get this curiosity written into the information theory.
*  To resolve uncertainty means you're going to be sensation seeking. Now whether that's a sensation
*  seeking of a banal sort that you're looking at the traffic lights or the street lamps to see whether
*  it's go or stop, or whether it's going to a disco or doing bungee jumping, it's a different,
*  but it's the same imperative underneath. But this is the response to the wisecrack that if we just
*  wanted to minimize surprise, we would sit in a dark room and not do anything. But how innocent is
*  that move to go from minimizing surprise to minimizing the expectation value of all my future
*  surprises? That seems like a little bit of a different minimization. Is that fair? Which one is
*  it that we're doing? Well, in a minimal sense, you're doing both. You're sort of touching on
*  the issues that normally come to the end of conversations like that. What is the difference
*  between you and a virus? So to cut to that distinction before revisiting the fundaments
*  of minimizing expected free energy in the future, it may be the case that certain systems, certain
*  biotech systems, creatures basically, have acquired the capacity to include, install in their
*  generative models the prior belief that they are free energy minimizing creatures. And if they
*  can do that, then they will have the prior belief that the way that I will act will be to minimize
*  my free energy. That was how you might write it down as a physicist. I see where this is going.
*  Yes, good. If you were a psychologist, all you're saying is I have the capacity to plan. Yeah. So
*  that's all you're saying. What to imagine. Exactly. Yeah. So you have sort of, yeah, perfect. So
*  your generative model is now equipped with the capacity to imagine a counterfactual,
*  fictive future, to imagine the future, to roll out possible consequences of actions. And of course,
*  the consequences of those actions in terms of the observations now are random variables because
*  they haven't happened yet. And that's why you get this reversal. And suddenly you become a creature
*  that seeks out sensations, literally sensation seeking that resolve uncertainty. You become
*  curious and you go to your discos and you do your bungee jumping at a certain age.
*  So that's, I think, an important distinction between very simple
*  attracting sets. Let's go right back to the moon rock. OK, so an appropriate description of that
*  non-equilibrium steady state is, in fact, an equilibrium steady state. And that's got a
*  point attractor. It could have a quasi-periodic attractor, so the orbiting of the planets.
*  But these are very simple, non-itinerant attracting sets that would approach an
*  equilibrium steady state. Then we move up to systems right from sort of rocks through to,
*  yeah, you may even go as far as some not insects, but certainly say viruses. So things that don't
*  plan. But they live, they're very effective, occupying our universe. But they live in the
*  moment in some sense. Absolutely. In Jerry Adelman's words, there is no remembered present,
*  there is no imagination, there's no planning. They have all the mechanical finesse of a thermostat.
*  But they're very good at what they do. Homeostasis, yeah. I mean, that's a nice
*  example. So even in our own bodies, there are possibly 99% of all that actually goes on in
*  terms of physiology, which is homeostasis, is just as reflexive in the moment,
*  keeping yourself in there. Regulating yourself. So those kinds of systems are distinct, I think,
*  from systems like you and me that start to plan and have the ability to, their generative models
*  do actually span the future and by implication, the path. They implicitly have a dynamics where
*  the trajectories actually go quite a long way in, or in their generative model, go quite a long way
*  into the future. So that would be a really interesting sort of way to take forward the
*  argument or a response to your question. But your question is slightly just to return to,
*  well, is it minimizing free energy or is it minimizing the free energy conditioned upon
*  a particular aspect? It is both. The degree to which you actively minimize your uncertainty
*  depends really upon the shape of the attractor that we're talking about, the attracting set that
*  we're talking about. So with itinerant systems, it is possible to write down the density dynamics
*  and work out the probability distribution of trajectories of action into the future. So this
*  just acts as another state and you can apply fluctuation theorems or pathological formalisms
*  to work out a distribution over trajectories of action into the state, into the future,
*  my apologies. Which means that technically what you can do now is characterize a given system
*  in terms of probability distributions over courses of action, policies into the future,
*  trajectories or paths of action under a model of what would the implications of that particular
*  action have for my sensory input, for example. When you write that down, there is
*  a way of showing that that is essentially a description of systems that do minimize their
*  expected free energy in the sense of just minimizing the distance, in fact technically
*  the chaos divergence between where they think they are probabilistically and their attracting set.
*  So that's one part of expected free energy. There is another part which is all about ambiguity
*  reducing, which kicks in when there are particular constraints on the shape of this
*  probability distribution that you and I evince just by existing. That depends really upon the
*  itinerancy which you can measure in terms of mutual information or relative entropy between
*  different partitions of the states. All of this rests upon a Markovian partition into a Markov
*  blanket. It all rests upon carving the universe into internal states that are inside you that
*  constitute your internal states, the rest of the universe and then crucially blanket states that
*  separate you from the rest of the universe that enable you to be identified. A further
*  bipartition on those blanket states into active and sensory states. Once you've compartmentalizing
*  the different kinds of states that would be necessary to describe a universe in which something
*  exists, i.e. you, in a way that is separable from not you, then you can start to write down,
*  you can go beyond just the 20th century physics in terms of entropies of distributions of say an
*  idealized gas or some sort of closed system. Now you have to deal with the entropies of a partition
*  and furthermore you've got the relative entropy now. So suddenly you're in a game of,
*  which is pure physics, it's just now you've got to think about the relative entropy. You can't just
*  talk about the entropy of this ensemble or this, the entropy of this, associated with this wave
*  function or this solution. You now have to carve it up and talk about the relative entropy, which
*  is where the information theoretic and all the information richness and all the uncertainty,
*  or that's where it all starts to kick in. And of course in so doing you've actually now committed
*  yourself to a mechanics of open systems because the whole point of having the Markov blanket is
*  that it enables a two-way traffic between the inside and the outside. So now by definition
*  you're in the game of writing down these statistical mechanics of open systems that have
*  some non-equilibrium steady state in virtue of having an attracting set. So now the game becomes
*  well what different kinds of attracting set could be and if they are what would it look as if they
*  are doing in terms of these mutual informations or relative entropies or uncertainty resolving
*  pressures that you know are one way of describing the very existence of this attracting set.
*  I do want to get more into the Markov blankets but I don't want to quite let go of this transition
*  from living in the moment to living in the expected future I guess. This seems to be without me
*  planning something that appears on the podcast over and over again recently in a conversation
*  with the philosopher Janane Ismael when we were talking about free will and what that means that
*  came up and earlier with Malcolm McIver who was a mechanical engineer and neuroscientist who has a
*  theory that one of the steps on the road to consciousness was when we fish climbed up onto
*  land and could begin planning in the future because the life the the time scales are much slower
*  on lands you have the ability to plan. So I wonder is it possible in this framework to sort of
*  pinpoint a place in the evolutionary scheme where we flip over from living in the moment to being
*  more planning animals. My personal theory is that it's with cats because I have two cats my listeners
*  are well aware Ariel and Caliban and I swear that one of them Caliban just lives in the moment
*  like he his needs are being met or they're not and those are the only two states he has
*  whereas Ariel you could see that she's trying to figure something out about what would happen
*  subjunctively if she did something and like her little kitty brain is trying its best.
*  So I'm sure the cats is an exaggeration but is it as late as mammals where this becomes important
*  or do you want to attribute it much earlier than that? I don't know but I'm compelled by
*  it seems very clear. But you know everything you've said in terms of these other perspectives
*  you know particularly from philosophy makes entire sense to me. The ability to plan
*  and suddenly means you have now a space of trajectories courses of actions in the future
*  and it means that you have because you can only
*  realize one deterministic action because action is actually a physical state of the universe.
*  It's not you know the action in and of itself is not a belief you know we have beliefs about action
*  but the action is realized so that realization means that you have to commit to one of a multitude
*  so there's a selection process in play which must in some sense speak to the free will
*  or at least if it doesn't depending upon your your your commitment that it used to free will
*  what it does say is if there is a selection process in play in terms of selecting an action
*  from some probability distribution or beliefs about the way that I am currently acting then
*  it must be the case that that only applies to systems that actually have posterior beliefs about
*  the future. Yeah it cannot have capacity. So a thermostat could not I think be confused with
*  something that might express free will whereas your question now is at what point do we have
*  biological thermostats that have this beautiful homeostasis that become equipped with the capacity
*  to imagine to plan to think and as you intimated possibly even have some minimal form of of
*  consciousness or even self perhaps selfhood before consciousness and so I normally recourse to the
*  philosophical notion of a vague concept here so you know I only recently learned about this is
*  here's a whole philosophy of vagueness is true we haven't talked about on the podcast but that's
*  an interesting topic yeah so um you know for those people who don't like me who don't know
*  like I was a few months ago so at what point is a pile of sand a pile you know is it one two three
*  four five grains so I quite like that as a way of without moving getting out of the question
*  at what point would you would you put your cap threshold right and I think it's warranted or
*  licensed mathematically because even things like thermostats and viruses they say predictive
*  coding so predictive coding does not have this planning it doesn't have this sense maybe defined
*  for the audience predictive coding well predictive coding is just uh well originally devised in the
*  1950s as a way of compressing sound files so it's it's a very efficient way of
*  complying with occam's principle by make providing the most retain the most information
*  but in the simplest coding that you can which is another way of algorithmic compressibility
*  yeah that is in fact the phialis principle as well but just written in terms of algorithmic
*  complexity and minimum message methods it's exactly the same maths but different different
*  sort of event spaces so predictive coding as currently applied to things like the brain is
*  just the notion that we're minimizing our prediction error yeah so we so it doesn't talk
*  about action what it does talk about is how our brains might respond how our sort of decoders
*  might respond to some new data and they do it by sort of reorganizing and belief updating
*  or state estimation in a way that minimizes the prediction error so if you can predict
*  what is currently being presented currently exactly on the basis of what you have previously seen
*  then you must have a perfect model of what is generating that signal or that soundtrack or the
*  auditory stream and therefore you have minimized your free energy or variational free energy or
*  you've maximized your evidence evidence lower bound in terms of the pure sensory the sentient
*  aspects of it notice that we haven't which is you know the important thing we haven't talked about
*  what we're going to do or how to do that yes so this you know that prediction code doesn't
*  address active inference it doesn't oh active learning it just talks about sort of how to make
*  sense of data so that that would be a nice example of um you know the sensory part of a of a virus
*  or a thermostat it you know it's it's uh can be completely described as just minimizing the
*  discrepancy take a thermostat for example let's now put action back into the mix so you can describe
*  the thermostat as just minimizing its prediction error prediction error between what well between
*  the temperature it's sensing and it's attracting fixed point so it's one of these fixed point
*  creatures and it's got the tracking set it has its prior belief the temperature will be like this
*  and all i need to do is to minimize my prediction error minimize my free energy
*  and uh i don't know how i'm doing it but i do seem to be turning on the heater the air conditioning
*  i guess no i don't know but he's equipped with action uh that will enable it to to get to its
*  fixed point so in what sense is that planning if you remember i'm trying to argue for a vagueness
*  here so i don't have to see your question um well when when you formulate that kind of predictive
*  coding in terms of kalman filtering or bayesian filtering which would be the technical um or the
*  statisticians way of describing a predictive coding scheme you're always working with with
*  derivatives so it's you're always working um in a dynamical setting with not just the prediction
*  errors but the rate of change of particular errors with time so in a minimal sense you've got a
*  notion of the future through a linear first-order approximation next incident anyway absolutely
*  yeah okay so that's what i meant with in a trivial in a minimal sense that everything has every
*  generative model has a notion of the future just in virtue of having a notion of trajectories or
*  dynamics yeah okay uh but it's not quite the same as your second cat yeah it's not thinking well if
*  i sit here i look like this yeah you can see it's just at the level of her capacity but but you
*  mentioned action and i think this is a natural place to go there because you also want to say
*  that free energy helps us understand how we behave is that safe to say in fact so let me let me
*  sort of repeat the thing that i read and then again you'll fix it uh one way of thinking about
*  what happens when i move my hand is that my brain sort of intentionally gets it wrong about where
*  my hand is and then there seems to be a mismatch between where my hand actually is and where my
*  brain thinks it is and rather than fix my brain i move my hand to bring it to where it is is that
*  that's beautiful yeah okay i don't need to fix anything there um in fact we should celebrate
*  that because what you've just described um is um a modern day recount of idea motor theory which was
*  which was prevalent in you know the 19th century which uh helmholtz yes well well um yeah i mean
*  he did everything so i could say yes he's a high entropy thinker yeah there were other
*  um sort of german neurologists and natural scientists you know sort of focused specifically
*  about that was picked up by william james uh you know on his european tours but the i the i is
*  exactly what you just said it is to move i have to in my mind imagine the outcome of that movement
*  and then just let my reflexes realize that imagined outcome which basically was in the
*  victorian era um positive explanation for um stage hypnotism that your your arm is getting lighter
*  and lighter and lighter and lighter and of course if you believe your arm is getting lighter and
*  lighter and lighter and lighter is floating then your predictions about the proprioceptive
*  input that you would get if your hand was in fact floating can now be fulfilled at a sort of
*  pre-awareness level simply by reflexes and your hand will indeed just rise so you know it's this
*  is as much as nearly all the free energy principle actually particularly it's sort of incarnations
*  when applied to things like active inference these are very old ideas and you can actually
*  probably trace them back to the students of playto but they come through count and helmholtz
*  okay very much so yeah uh and alongside that um that sort of um perception as inference it was
*  this sort of actions inference basically actions beliefs about the way i should be oh yes now i am
*  like that and if of course you actually attend to the evidence that in fact your hand is not floating
*  then of course it won't move and which sort of um takes us into the interesting scenario
*  that you must in some sense attenuate the evidence prevent yourself from getting that exactly yeah
*  okay is this is this i guess maybe what we have that playto or helmholtz or william james did
*  not have is the ability to poke inside a brain and see what's going on there is this is this idea
*  that action is driven by a mismatch between model and a sensory input verified testable in the brain
*  yeah yeah absolutely a number of levels um but again just coming back to this sort of notion that
*  most of what emerges from this from a sort of mechanical treatment of the vng principle
*  was well known you know a century ago so what we are describing are classical reflexes so there's
*  this you know the brain sends down messages to alpha motor neurons and spinal cord there effectively
*  are a mismatch between the intended signals sensory signals from the muscles the motor plant
*  and what it's actually receiving and then those cells elaborate signals to the muscles to cause
*  them to contract until the signals match so the way that we move and in fact the way that we
*  secrete our autonomic functional works the way that our heart works in fact all of our homeostasis
*  works generalized homeostasis works is by supplying the right set points to um servos or homeostatic
*  or reflex mechanisms in the periphery what are those set points they're just predictions of the
*  way i want to be and is the role of does free energy have a role here in kind of an optimization
*  problem or an efficiency maybe mechanism like there's different ways you could imagine the
*  brain or the the nervous system bringing this match between expectation and reality but is
*  there just a sort of there are easier ways to calculate how to do that using free energy using
*  well um i mean you know the free energy formalism is if you like that your
*  grandfather's all of these particular manifestations yeah okay um i guess what you're asking is
*  if i wanted to now describe the the biology or the wiring or the time constants um what you'd
*  have to do is to write down the genitive model if you remember the free energies are functional
*  of a belief and the belief is defined in relation to a genitive model so if you can write down the
*  genitive model you can then write down the differential equations of these sort of sensory
*  and active internal states internal states you can associate with neural activity active states can
*  be either secretions or it could be physical movements of a of an arm and then you will be
*  able to simulate these kinds of phenomena what you can then do is take empirical data and then
*  change the parameters of the generative model until your simulation of an arm movement for example
*  or a neuronal responsive perceptual synthesis matches what you what you observe in terms of
*  brain signals so that you know in a sense that's another description what we already do we are
*  that's what neuro scientists do we you know we think about the functional anatomy in terms of
*  well how does the brain model its world how does it make these predictions how does it generate for
*  example in movement how does it generate these motor commands but they're not motor commands
*  they're just predictions of what i should feel if um i was actually in this position or walking or
*  talking and in fact that that that the whole industry of not only theories of interpreting
*  reflex arcs and the motor system under that kind of perspective called the equilibrium point
*  hypothesis but there's also massive debates about you know the actual implementation of that and
*  you know well that's the right way to look at things i guess i had this impression that
*  you might imagine that what the brain is trying to do is just use bayes's theorem it has some
*  beliefs it gets in more data it updates its beliefs but that is calculationally difficult
*  computationally intensive and calculating free energy is a sort of shortcut you know minimizing
*  the free energy is calculationally easier than simply conditionalizing probabilities i see it
*  sorry yes you you've you've moved us into a very important observation so so i mean we've been
*  talking about sort of beliefs about where we should be in prior beliefs and beliefs about the future
*  and of course prior beliefs implicitly rests upon a bayesian distinction between prior beliefs prior
*  to seeing any sensory states of sensory data and posterior beliefs that are the product of belief
*  updating having observed those data so that is the process of minimizing variational free energy for
*  example or is it not quite if you um if that process of belief updating and this just connect
*  it back to physics so what we are saying is that there is a gradient flow that is in place that
*  underwrites a random attractor and that attracting set defines the kind of thing that we are and
*  there's this mark-off blanket or partition in play so that gradient flow we're going to now
*  associate with belief updating on the assumption that some states encode probability distributions
*  or stand in for the parameters of beliefs and once we've made that move then we can actually
*  write down the gradient flows in terms of belief updating we just literally we're taking a random
*  dynamical system on say a l'enjevain system and um you know interpreting the dynamics as belief
*  updating and the belief updating is from prior to post-teriors so that's a gradient flow in this
*  case is a way of saying moving from where we are a little bit closer to where we want to be yes yeah
*  absolutely well i mean that's exactly what the free energy actually scores um yeah so we're covering
*  all sorts of wonderful issues here but we haven't gotten to the origin of life yet but we're going
*  to get there too um so yeah no it was different between bays and approximate base inference that's
*  where we go but but i think actually you're touching on something um which we'd we'd rehearsed
*  previously um which is another perspective on variational free energy so so just for your interest
*  once you um um abandon um equilibrium uh physics uh 20th century physics and you just live in a
*  world of non-equilibrium steady state uh which implies that there is some attracting set there
*  and you have to explain it you know its mechanics um then the um the free energy um the variational
*  free energy now starts to have the look and feel of something that is much closer to a physicist's
*  thermodynamic free energy and effectively it scores the divergence between the current stated system
*  and the probability distribution it would have on its attracting set exactly on the attracting set
*  yeah so it's basically how far away am i from my attracting set or my um my sort of non-equilibrium
*  steady state probability distribution so in that sense in now it looks very much like the amount
*  of energy available to do work so i look at me i perturb me i put me in a highly unusual frightening
*  angst inducing situation i've never been in before uh you know homeostatically or conceptually um and
*  i will work towards getting back to my comfort zone yes i mean i have you please my happy place
*  and i my right temperature and in so doing i will minimize my fear and i'll be working literally on
*  the environment uh so now the to my mind that there becomes an almost invisible distinction
*  between the variational free energy in the context of writing down the dynamics or the mechanics of
*  non-equilibrium steady states with attracting sets and thermodynamic free energy and in fact
*  you can just put a belzman constant on and they are the same thing and interesting the
*  belzman constant is uh in the purely information theoretic perspective it now becomes um just
*  equips the amplitude of random fluctuations with units and now you can start to interpret it in
*  terms of you know physical measure yeah that's right yeah physical measures anyway that was that
*  was me indulging myself because i i know you're no no yeah you like that sort of thing yeah uh
*  but back to the you know why not disbaiting inference um and what's the difference between
*  minimizing free energy and basic inference great question so the the um if basic model evidence
*  is just simply the marginal likelihood of states of being then one could trivially say just by
*  optimizing the likelihood that i am in this state which by definition is the thing that i do because
*  that's how i exist i could describe myself as performing basic inference trivially so because
*  i can i can just call the negative log of my non-equilibrium state density model evidence and
*  therefore everything i do is in the service of maximizing model evidence i'm the perfect
*  basic statistician it doesn't get you anywhere but it's a nice a nice thing to say yes so
*  where does the variational free energy comes in well the variational free energy comes in um
*  because it's um operationally defines what's called approximate bayesian inference so what's
*  the difference between um bays basic inference uh that would conform to bayes rule um and
*  approximate bayesian inference or variational base or sometimes called ensemble learning but
*  probably variational basis is the most technically correct term well the difference is that you're
*  not minimizing model evidence they're maximizing model evidence you are um maximizing a lower
*  bound on model evidence which means that um the thing that you can measure which is this
*  variational free energy or the negative in machine learning um is now always a um um in machine
*  learning it's always below the actual thing you want to you want to maximize which is your
*  model evidence if i just flip the side and bring us back to physics and the free energy principle
*  um so the negative logarithm of um uh model evidence which is essentially our self-information
*  our surprise can always be minimized as if as if you were a perfect basic statistician
*  by minimizing uh something that's always provably larger than that yeah and that's the
*  k-l divergence or bound approximation so the variation of energy is an upper evidence bound
*  and if you minimize that then you become an approximate bayesian inference why approximate
*  well because the bound is not necessarily zero it's not saturated yeah right uh and that might be
*  easier to work that way that's the only rationale for it yeah so it's just that you the evaluation
*  of the actual um evidence a partition function if you're a physicist becomes intractable
*  um because in high dimensional systems so how do you elude that intractability when you've actually
*  got real physical systems that seem to be able to do this kind of thing um well you just create a
*  tractable bound and um and who did that well richard freeman that's that's that's you know
*  that's where it came from right on on one reading of the legacy there's another russian reading
*  yes uh one reading of the legacy of of physics for things like the free energy principle
*  it's certainly machine learning uh that's you know it was feinman's pathological formulation
*  which introduced the notion of a variational bound a bound that was using variational calculus
*  was provably always greater than the thing you wanted to optimize so you just optimize the bound
*  instead and you get into some nice rhetoric about sort of bounded rationality economics
*  oh okay yeah i haven't even thought of that but i guess it makes sense it's not it's not perfectly
*  rational it's not exactly based in but it's doable it's physically realizable so that's that that's
*  the key difference none of us is laplace's demon absolutely yeah yeah but so much of this conversation
*  and i think for good reason has been in the context of agents or brains occasionally thermostats
*  but you do want to be even a little bit more ambitious right and and talk about uh sort of
*  a general organizing principle of non-equilibrium systems uh to minimize their free energy and maybe
*  this has something to do not just with the nature of cells and organisms but with their origin
*  is that safe to say is that a fair ambition to attribute to you that minimizing free energy helps
*  explain why life came into existence in the first place oh um yeah you're taking me out out of my
*  comfort did i say that so well it's probably um it could be me could be my lenses because i want
*  to do that oh maybe you should talk about that yeah yeah yeah well you know okay let's put it
*  this way you mentioned mark all blankets right um the idea of the you know in fact we have a bunch
*  of systems in the universe that have a pretty clear boundary between themselves and the rest
*  of the world right in this boundary mediates their interactions with the world the appearance
*  of cell walls is clearly one of the most important steps in the origin of life and and a literal cell
*  wall is is certainly similar in spirit if not exactly identical to the the conceptual mark of
*  blanket between the inside and the outside is that is that safe to say absolutely yeah yeah yeah i
*  don't know if that is the metaphor we always use this is a cell surface is about yeah yeah and so
*  but somehow life as we know it um you could imagine that if life were just defined as some
*  complex thing that had a big chemical reaction and it evolved it wouldn't need to have cell walls it
*  wouldn't need to be in a compartment and yet it is uh as a matter of fact and i'm wondering if
*  if somehow being compartmentalized like that uh affords a special set of powers to certain
*  chemical reactions to then go and adapt in in a crazy world yes i'm sure that's right i i'm not
*  sure um about um i i i'm wondering whether there's a slightly more deflationary way of it's very
*  likely yeah um you know in order to exist and to have measurable characteristics and
*  the sense of ergodicity you'd have to have a mark of blanket so from a sort of um so weak
*  anthropomorphic principle point of view then you know it could have been no other way well does a
*  hurricane have a mark of blanket um interesting point i've been asked this gear gaia um no it
*  doesn't that's very irritating not nor the candle flames and they're not alive so that's but oh i
*  see there is some right yes right um but they have characteristics some characteristics yes
*  but on an ergodic sense in the sense that that um that they don't last long enough um however you
*  could say an eternal flame that i i think you're right i i think that's a you know from um from my
*  um perspective that that's a really interesting outstanding challenge i'm wondering whether
*  burkoff's notions of wandering sets you know resolves that that you can actually have a
*  mark of blanket that renews itself right however that's that you know um but in some sense you know
*  one of the reasons why we don't count hurricanes or forest fires as living is that they're not
*  rich with information right they're just doing their thing and uh even the simplest cell you
*  know in your language carries a model of the world around with it right and a and a forest
*  fire does not ah good yes no that makes a lot of sense i wish i'd said that yeah and so somehow
*  i don't know how life began that some of my friends are working on it you know i do i do
*  wonder whether or not uh we are under emphasizing the important there's there's this debate in the
*  origin of life between replication first where you imagine that rna or the information carrying
*  thing came first and then it sort of wrapped a blanket around it and got energy and get go
*  got going there's another camp metabolism first that said that the uh actually extracting free
*  energy in the physicist's sense from the environment was the first thing that happened and only later
*  did it sort of get uh imprinted informationally onto rna and then put in a cell and then there's
*  the easy everyone agrees that the easy part is making a cell wall it's just like a bilipid
*  layer like that that can just happen automatically so i wonder if we're not uh you know underselling
*  the importance of that thing that without that compartment without that blanket um the very
*  notion of having a view of the outside world having a having a model even if it's very very
*  primitive uh is not really tenable if you if you don't even have a difference between self and
*  other yes what does it mean to have a view of the other that well that's the deflationary aspect
*  for me it's beautiful for me it's a quinien desert landscape i mean there's a fundamental truth to
*  that i haven't really thought about this and clearly you have so i have to be you know i'll
*  speak tentatively but it does strike me as when when we use the the free energy principle to model
*  morphogenesis and cellular organization it becomes immediately obvious you need rna and dna as a
*  generative model that's certainly the case when he's talking about sort of multicellular organization
*  that you you cannot get a free energy minimum minimum uh minimum from coupled free energy
*  minimizing markov blankets without some shared generative model that how you know that is most
*  naturally written down in terms of some genetic code so it may well be from a perspective that
*  makes perfect sense that's what dna is good at doing right storing the information so um so perhaps
*  you could argue and i um um perhaps you have already or people have already that yes first of
*  all you need a mark of blanket you know otherwise there is no existence um of the sort that we're
*  talking about um um but but if if it is the case that just uh you know the part of having a mark
*  of blanket means there is a way of writing down the dynamics or the mechanics that makes it look
*  as if there's a generative model there also has to be something in the internal states that plays
*  the role of a generative model and it seems quite natural then to you know for things that endure
*  over generations or show that sort of attracting set uh with a sense of itinerancy that come and
*  looks like reproduction um then that that that that's what we call rna or dna uh yeah so it may
*  well be that the you know the other side of the coin of having a mark of blanket namely i must
*  have an implicit generative model or it looks as if my gradient flows are on a variational
*  uh gradient and that that free energy gradient and that free energy is a function of a generative
*  model therefore there must be a biophysical encoding of that that could be a statement that
*  you need something like rna dna sorry in order to you know to go hand in hand with the mark of
*  blanket yeah well i do appreciate you indulging me there but that may be good then to sort of
*  wrap things up we can bring it back close to where we started uh with uh going back to the
*  clinic out of the research uh environment how does this perspective this point of view of free
*  energy minimization um help us understand not just the brain when it's working but the brain when it's
*  not working uh i i recall schizophrenia is something uh that you might be thinking about
*  but maybe other things as well yes i mean my personal um training and and an interest in
*  schizophrenia but i have to work with uh that sounds awful isn't it i have the pleasure of
*  working with lots of psychologists and psychiatrists who like all sorts of uh who
*  are interested in all sorts of uh neuropsychiatric conditions so um i think it's a lovely question
*  because um it allows me to make some simple points so if cant and helm holt and everybody
*  since that time are right and effectively um psychology is inference consciousness is
*  it was an unconsciousness is inference psychology is inference and psychiatry is psychopathology
*  that tells you by definition that psychiatry is all about broken inference right false inference
*  and i mean that in a very literal sense that basically inferring something is it's there when
*  it is not like a delusion or a hallucination or inferring something is not there when it is
*  like an agnosia or a denial that something exists or part of my body exists so just extending that
*  notion that nearly um that nearly every psychiatric and probably neurological syndrome can be cast as
*  an instance of false inference suddenly gives you um or puts pressure on you to now derive a calculus
*  of how the brain works that is framed in terms of beliefs and inference so just a few examples
*  always cover say delusions and hallucinations that schizophrenia that's those are sort of the
*  post-chance of your false inference um but also you could be are in can manifest in a slightly
*  more subtle way like take parkinson's disease let's come back to our idea motor picture of
*  why and how we move i infer that my mom is going to be over there or i infer that in the next
*  600 milliseconds i'm going to stand up and start walking now if i make a false inference because i
*  fail to attenuate the evidence that i am not moving i will never realize that prior belief
*  i will never form an intention to move what's i'm moving i'm fine but if i'm not moving i cannot
*  deny the sensory evidence that i'm stuck immobile of course that's a classic description of parkinson's
*  yeah and actually if you drill down on the things that um the um the belief updating at the neural
*  level it actually implicates directly you know the neurotransmitters and chemicals that are
*  uh implicated in parkinson's disease so if we just generalize this notion of false inference when
*  inference really underwrites your free will selection of what to do next in terms of
*  predictions about what's going to you know how you're going to feel yourself move and talk and
*  think and feel um including your gut feelings then you've got a um a way now of um writing down a
*  mechanics of psychiatry so in a way that all other normative schemes do not you know because it's
*  actually um articulated in terms of probability distributions because if you remember it's all
*  about functional it's all about things like entropy and beliefs and relative interfaces and
*  certainties um beliefs about something then you know you've now got a calculus which is fit for
*  purpose to understand false inference hallucinations and perceptions and the physics that gives rise to
*  those the physics that underwrites the belief updating that leads to this false inference so
*  in the past 10 years that's hit me time and time again you know why it is so useful and if not
*  essential to understand sentience in its sort of philosophical sense and the failures of sentience
*  that we have in psychiatry to understand those in on a formal footing um you know calls for something
*  like uh the free energy principle and has it led to any specific uh tactics for uh therapeutic
*  interventions well what might hope soon so um it certainly led to um and you know and i may be
*  misinterpreting this through the way that i the things that i must review so i only speak to
*  people who commit or subscribe to the free energy principle so uh i don't see alternative but but
*  certainly from what i see in terms of being asked to contribute to special issues and what i see
*  in terms of being asked to review uh for this specialist psychiatric literature there has been
*  a sort of slight paradigm shift in the past five years it also sent us something called precision
*  um we mentioned that very very briefly before when when when we were talking about the predictive
*  coding implementation of of variational approximate based inference by minimizing
*  variation free energy um so i talked about the precision weighted prediction errors so what
*  what that basically means is that um you can have a mismatch between what you predicted and what you
*  sensed does it really matter right you know if it's in the dark if i get a mismatch between you know
*  if i thought i was seeing a visual angel and what i actually get is darkness does that really matter
*  because there's no precise visual information around so i actually now have to see the darkness
*  by inferring the precision the signal to noise ratio effectively the error bars and something
*  exactly it is exactly the error bars interestingly of course that's 99 of the challenge for
*  statistical analysis it's not measuring the group it's measuring your uncertainty about it
*  so but that's that's interesting people like you have to emphasize this the importance of what
*  you've just what we've just said for psychiatry getting the error bars right is at the heart of
*  good inference if you break the capacity to get your error bars spot on you're going to get all
*  sorts of false typed one and type two errors false inferences very things are there when they're not
*  and they are they're not there when they are so that's where the precision comes in it's literally
*  the sort of the you know the more precise the type of the error bars the less precise the more
*  dispersed or uncertain you are about something or in particular the the precision of the sensory
*  evidence and for example all the precision of my beliefs how the confidence with which i hold my
*  prior beliefs that are being used to explain these data that may other may themselves
*  may or may not be precise so but you have to estimate this precision so it looks as if and
*  this is the mini paradigm shift i was talking about it looks as if in psychiatry nearly all
*  the phenomenology in the psychopathology and possibly a lot of the neurochemistry and
*  psychopharmacology can be explained by failure to encode the precision the error bars
*  and that makes a lot of sense because nearly every treatment or certainly every pharmacological
*  treatment in psychiatry targets those neurotransmitters that have a modulatory effect so they don't
*  in themselves encode shifts in the beliefs or expectations or averages they encode changes in
*  the sensitivity to sensory input for example so it looks as though those are exactly from the
*  point of view of predictive coding exactly the biophysical mechanisms that would encode your
*  beliefs about the precision so what does that tell you well it it tells you first of all
*  where you should target your therapy it's likely to be in broken standard error estimators in the
*  brain so where are they and then you know that you know once you know about the neurochemistry
*  the functional anatomy the projection systems and the domains of beliefs that are broken if you've
*  got anorexia nervosa it's beliefs about your body if you've got visual hallucinations it might be a
*  sort of a little body disease and organic psychosyndrome but the same underlying mechanisms
*  should be played just with different neurotransmitters and different possibly neurogenetic
*  processes so it does give you a mechanistic focus so you can start to move away from what is if you
*  like haunted psychiatry for centuries which is this purely nosological describing descriptive
*  approach to a slightly more mechanistic understanding which is starting to it's pre-paradox
*  i'm going to use all the time now so so that yeah so that what do you say is it currently
*  affecting treatment strategies no it is pre-paradigmatic but i guess if you came back in
*  five to ten years then i think you'd then see evidence of where that that turn led in terms of
*  possibly reinvigorating the the pharmaceutical industry i say that very practically something
*  you won't know but it worries a lot of people in my game so the pharma have basically given up on
*  psychiatry developing psychiatric drugs there's no money to be made because there's no progress
*  there's no mechanistic underpinning so about three years ago they basically all just pulled out well
*  no idea yeah so there is no active research at all i mean this is expensive research is billions
*  or millions in drugs for schizophrenia depression you know which is a great shame and you can see
*  why because they don't know what to target because there's no one said well it's got to be this
*  system or that system that system so we all agree it's important they just don't see the
*  direction forward yes yeah absolutely yeah and of course they have to just they have to keep the
*  money coming in to fund the research to make the next but maybe this will propose a direction
*  forward in some that would be the cross our fingers yeah all right i think this is a wonderful
*  lesson to end on we should all aspire to uh have our error bars brought in as close alignment
*  with reality as we possibly can carl friston thanks so much for being on the podcast thank you

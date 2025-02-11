---
Date Generated: December 14, 2024
Transcription Model: whisper medium 20231117
Length: 5831s
Video Keywords: []
Video Views: 382
Video Rating: None
Video Description: Grace Hwang and Joe Monaco discuss the future of the interaction between neuroscience and artificial intelligence.

Show notes: 
https://braininspired.co/podcast/200/

Patreon  (full episodes and Discord community: 
https://www.patreon.com/braininspired

Apple podcasts:  https://itunes.apple.com/us/podcast/brain-inspired/id1428880766?mt=2
Spotify:  https://open.spotify.com/show/2UZj8c8Ap5oc2gh2rJxLLe

The Transmitter is an online publication that aims to deliver useful information, insights and tools to build bridges across neuroscience and advance research. Visit thetransmitter.org to explore the latest neuroscience news and perspectives, written by journalists and scientists. 

Read more about our partnership: https://www.thetransmitter.org/partners/

Sign up for the “Brain Inspired” email alerts to be notified every time a new “Brain Inspired” episode is released: https://www.thetransmitter.org/newsletters/

To explore more neuroscience news and perspectives, visit thetransmitter.org.

Joe Monaco and Grace Hwang  co-organized a recent workshop I participated in, the 2024 BRAIN NeuroAI Workshop. You may have heard of the BRAIN Initiative, but in case not, BRAIN is is huge funding effort across many agencies, one of which is the National Institutes of Health, where this recent workshop was held. The BRAIN Initiative began in 2013 under the Obama administration, with the goal to support developing technologies to help understand the human brain, so we can cure brain based diseases. 
So it just became a decade old, with many successes like recent whole brain connectomes, and discovering the vast array of cell types. Now the question is how to move forward, and one area they are curious about, that perhaps has a lot of potential to support their mission, is the recent convergence of neuroscience and AI... or NeuroAI. So the workshop was designed to explore how NeuroAI might contribute moving forward, and to hear from NeuroAI folks how they envision the field moving forward. You'll hear more about that in a moment.
That's one reason I invited Grace and Joe on. Another reason is because they co-wrote a position paper a while back that is impressive as a synthesis of lots of cognitive sciences concepts, but also proposes a specific level of abstraction and scale in brain processes that may serve as a base layer for computation. The paper is called Neurodynamical Computing at the Information Boundaries, of Intelligent Systems, and you'll learn more about that in this episode.

0:00 - Intro
25:45 - NeuroAI Workshop - neuromorphics
33:31 - Neuromorphics and theory
49:19 - Reflections on the workshop
54:22 - Neurodynamical computing and information boundaries
1:01:04 - Perceptual control theory
1:08:56 - Digital twins and neural foundation models
1:14:02 - Base layer of computation
---

# BI 200 Grace Hwang and Joe Monaco The Future of Neuro-AI
**Brain Inspired:** [December 03, 2024](https://www.youtube.com/watch?v=v-wmGOC68wg)
*  Maybe this interdisciplinary process, whatever we're calling neuro AI, can help dislodge
*  some of these stale debates and arguments and help us get to a new conceptualization
*  of what's really going on in brains.
*  There are some people that think neuro AI is about using AI to understand neuroscience
*  and then there are people that think neuro AI is about using insights and principles
*  from neuroscience to improve AI.
*  They're really more interested in the convergence and the reciprocal aspects of neuro AI.
*  You can like ignite it essentially and then the connections are such that the non-linearities
*  all line up and you get self-reinforcing, self-supporting, self-sustaining activity.
*  That's the basis.
*  That's the base computational unit.
*  And I turned out to be the only student that had the right answer.
*  Is that because you used the for loop and just did it like the careful slow way?
*  This is Brain Inspired, powered by the transmitter.
*  Well, well, if you're a longtime listener, you may recognize that I added back in Chopin.
*  That is at the demand of one of my guests today, Joe Monaco.
*  Joe berated me, you could say, for removing it a long time ago from the introduction.
*  So he took it upon himself to play it, record it, and send me the recording.
*  And so it's back.
*  I hope you're happy, Joe.
*  Grace Huang, the other voice you just heard, will introduce themselves in a moment, but
*  I will introduce them now as co-organizers of a recent workshop that I participated in,
*  the 2024 Brain Neuro AI Workshop.
*  You may have heard of the Brain Initiative, but in case not, it is a huge funding effort
*  across many agencies, one of which is the National Institutes of Health, or the NIH,
*  where this recent workshop was held.
*  The Brain Initiative began in 2013 under the Obama administration with the goal to support
*  developing technologies and implementing those technologies to help understand the human
*  brain so that we can cure brain-based diseases.
*  So the Brain Initiative just became a little over a decade old now, with many successes
*  under its belt, like the recent whole brain connectomes you may have heard of and discovering
*  the vast array of cell types and many others.
*  I'm not going to list them here, but I'll point to a reference for you to learn more.
*  So now the question is how to move forward.
*  And one area they are curious about that perhaps has a lot of potential to support their mission
*  is the recent convergence of neuroscience and AI, or what has been recently coined as
*  neuro-AI, for better or worse, as we discuss.
*  So the workshop was designed to explore how neuro-AI might contribute moving forward and
*  to hear from neuro-AI folks, people doing the neuro-AI research, to hear how they envision
*  the field moving forward.
*  You'll hear more about that in a moment.
*  That's one reason I invited Grace and Joe on.
*  Another reason is because they co-wrote a position paper a while back that is, among
*  other things, it's an impressive synthesis of lots of concepts in the cognitive sciences
*  and neurosciences and history.
*  So we talk about that.
*  But it also proposes a specific level of abstraction and scale in brain processes that may serve
*  as what Joe calls a base layer for computation.
*  So the paper is called Neuro-Dynamical Computing at the Information Boundaries of Intelligent
*  Systems.
*  All right.
*  So you'll learn more about that in this episode as well.
*  Okay.
*  I don't want to yammer on here.
*  So let's get you to Grace and Joe.
*  There are lots of show notes in this one to workshop related stuff and to many of the
*  papers that Joe and Grace reference.
*  Those are at braininspired.co.
*  slash podcast slash 200.
*  Right.
*  I forgot.
*  It's the 200th episode.
*  That is awesome.
*  And amazing.
*  And what a fitting way to bring in 200.
*  Talking about a neuro AI workshop, among other things.
*  Patreon supporters, you are the best.
*  Let's have a live chat before the Christmas holidays if you're up for it.
*  So I'll be in touch about that.
*  Go to braininspired.co to learn how to support the show on Patreon and join in on fun stuff
*  like that and get full episodes all the time.
*  All right.
*  Here are Grace and Joe.
*  Yeah, we're starting.
*  We're starting.
*  Okay.
*  You guys just blew my mind.
*  So this is the beginning.
*  I didn't I've been interacting with both of you.
*  I had no idea that you were a married couple because my interactions with you, you know,
*  were very professional because I just came back from this neuro AI brain initiative workshop.
*  And then 30 seconds into us speaking to each other, Grace said, you do know that we're
*  or one of you said you do know that we're a couple, right?
*  And nope, no, I did not.
*  But I do know.
*  So first of all, hi, Joe.
*  Hi, Grace.
*  Thanks for being on the podcast.
*  Thanks for having us.
*  So in this is a little bit different than the way I normally do things.
*  But could you just like very briefly state your name and occupation or not your name,
*  but your occupation?
*  Grace, we'll start with you.
*  Grace Huang.
*  I am a program director at the NIH at the National Institutes of Neurological Disorders
*  and Stroke.
*  And I support the brain initiative full time.
*  And Joe.
*  I am Joe Monaco.
*  I am a scientific program manager and I am a contractor for the office of the brain director
*  at the NIH.
*  So we are housed under NINDS.
*  So I'm there with Grace, but I work with the brain director and I work with all of our
*  internal brain teams.
*  OK.
*  And I just worked with both of you among many other people who worked with both of you because
*  you both put in an absurd amount of work to organize this recent brain initiative neuro
*  AI workshop.
*  But now I don't know where to start because your partnership has gone back a long time.
*  Grace, I had recently learned that it was an interesting way that you guys met originally
*  and came to form an intellectual partnership.
*  So maybe we could just start there.
*  Well we met originally in 2004 at Brandeis University when we both were in taking computational
*  theoretical neuroscience class under Larry Abbott back when he was there.
*  That's kind of a famous class.
*  I feel like a lot of people matriculated through that class and have fond memories of it.
*  Indeed.
*  Joe and I started our first collaboration.
*  This was when I had just gone into computational neuroscience and was learning how to use MATLAB
*  for the very first time and had to do a homework problem.
*  And I was the only student that had a different answer than everybody else because I had not
*  figured out how to unroll my loops.
*  So I was literally writing all these loops.
*  Nothing wrong with a for loop, although it's better to not have them if possible.
*  That's right.
*  That plays into the story.
*  And because I was the only person who wrote a for loop, I had a different answer and I
*  thought I had the wrong answer.
*  Even the TA had a different answer than me.
*  So I sat in the computational annex for days trying to find the bug in my code.
*  And then at one or two in the morning before the homework was due comes in a student very
*  quickly writes his code and is about to leave with his correct answer.
*  And I asked him, can you just look at my code?
*  And he looked at it and he said, there is nothing wrong with your code.
*  And an hour later, he found a bug in his code that every other student who are super programmers
*  made.
*  And I turned out to be the only student that had the right answer.
*  Is that because you use the for loop and just did it like the careful slow way?
*  Yes.
*  Because all of the other computer nerds in the class, they know about vectorization.
*  Vectorize, vectorize, yeah.
*  And MATLAB is very slow when you write manual for loops.
*  And so everyone got the same wrong answer and they thought it was the right answer.
*  But looking through Grace's code, it's like she sequenced the order of operations absolutely
*  correctly.
*  And then I was able to figure out when you vectorize it, it actually changes the order.
*  And we were doing classical conditioning.
*  So the order in which you update the parameters of the synapses really mattered.
*  And you guys were already married at that time, right?
*  No.
*  No, no, no, no.
*  But you were just saying that...
*  That was when we met.
*  We married, we've been married for 10 years.
*  So it took us a long time to get married in 2014.
*  We had to get our PhDs first.
*  Backing up even further, Grace, I understand that the only reason you went into computational
*  neuroscience was because you developed mouse allergies.
*  Is that correct?
*  Yes.
*  I initially went to Brandeis University to study biophysics and structural biology.
*  I was building a single photon molecule microscope trying to study the translocation of HIV protein.
*  And that required that I work with protein chemicals and rotate it through a mouse lab.
*  And I had really bad allergies, whereas in hives and going...
*  I had an EpiPen.
*  And it was not a sustainable lifestyle.
*  So in my third year of graduate school, I changed labs into a computational memory lab
*  where I joined Michael Kahana back when he was at Brandeis University.
*  The interesting thing about that is I've only physically been near Joe a couple of times
*  now, but I think I developed an allergy.
*  No.
*  I don't know how to take that.
*  No.
*  Okay.
*  But so then how did you guys...
*  Because what you just co-organized was a neuro AI workshop.
*  So then how did you guys end up coming together in that state?
*  Well, so out of the two of us, I'm the one who was a neuroscientist from the beginning.
*  I was a computational neuroscientist and a theorist.
*  I did my PhD on grid cells and place cells and modeling how they might be related through
*  remapping.
*  It's very important computational transformation and hippocampal studies.
*  But I kind of brought that through to expanding outwards to think more about the complexity
*  of behavior throughout my postdoc.
*  So I joined Jim Canerum's lab at Johns Hopkins where he had a wealth of experimental data
*  of freely moving but on track rats basically navigating in a clockwise circle a number
*  of times.
*  And so you can very closely track the behavior, where's the position of the head and body,
*  and then you can track the emergence of place field activity over time.
*  And so that was kind of the basis of me getting into complex neurobehavioral analyses and
*  thinking about from an organismal perspective, what's actually going on here?
*  It's like, do we have all these just internal computational representations?
*  How does that translate into what this interesting little animal is doing on a moment to moment
*  basis?
*  And so that's kind of where I started thinking more deeply about complex temporal dynamics
*  and behavior.
*  And eventually, Grace was kind of off doing other things in other fields.
*  She's kind of a polyglot of science and technology.
*  So basically, after I graduated with my PhD, I went to the MITRE Corporation and I was
*  developing optical biosensors to detect pathogens from exhaled breath.
*  And I did some work in government at IARPA as a CIDA contractor and also at DARPA as
*  CIDA contractor.
*  And it wasn't until 2015 when I went back into quote unquote, academia.
*  I joined Johns Hopkins University Applied Physics Lab as a program manager to run their
*  applied neuroscience program.
*  Initially, I was an assistant program manager.
*  And that was the first time since 2005 that I started to pay attention to neuroscience
*  again.
*  And it was so exciting because neuroscience had just accelerated.
*  And so I started going to sites for neuroscience meetings.
*  But I wasn't following Joe's research at all.
*  And it wasn't until the 2017 Society for Neuroscience poster session that I learned about Joe's
*  discovery of phasor cells.
*  This came out of his research with actually Ketchensong and Tad Blair.
*  And I was so intrigued by phasor cells because unlike hippocampal place cells that maps phase.
*  They're mapped asymmetrically to the traversal of a place field.
*  And so very famously in hippocampus, the pyramidal neurons there, the place cells will start
*  firing at a later phase of the theta rhythm.
*  And then as the animal moves through the place field, each spike will become earlier and
*  earlier within the theta cycle across subsequent theta cycles.
*  And so if you plot the distance through the field against the theta phase of spikes, you
*  get this kind of nearly monotonic decrease in the phase.
*  So that's called phase precession.
*  And that's a very robust field.
*  It's thought to be related to sequence learning and very important things that CD3 is doing
*  in hippocampus.
*  That's the highly recurrent subregion.
*  But with Tad Blair, I had a collaboration where we were looking at the one synapse downstream
*  into the subcortex.
*  We were looking at lateral septum.
*  And so the septal bodies are very interesting.
*  People don't record from them very often.
*  But we were looking at what other phase codes might there be.
*  It's a theta rhythmic brain error.
*  And so we found, or well, I went looking for a different kind of code, one that wasn't
*  locked to a particular trajectory, but one that was locked to space.
*  So I was looking purely for spatial information in the timing code relative to theta oscillations
*  and found it.
*  And so that's kind of, I coined the name phasor cells.
*  There's a couple other models out there called phasor.
*  And this blew me away because you were able to directly map phase to place.
*  And I was working at the applied physics labs in the intelligence system center surrounded
*  by roboticists.
*  So I immediately thought, wow, if we could use this internal phase code to do self-localization
*  and mapping, wouldn't that be cool?
*  And on that very same day, there was this other paper that came out.
*  It was titled Swarmulators.
*  And these are swarmulators that can sync in swarm using an internal phase variable, which
*  came out of Kevin O'Keefe and Steven Strohgatz lab.
*  And so the two things got me thinking, wow, maybe there's a there there for using Joe's
*  discovery of phasor cells and controlling multi-agent robotics.
*  And so that was how our collaboration re-initiated back in 2017.
*  And then AI became pervasive.
*  And so we kind of now just begrudgingly call it neuro AI because people tend to know what
*  that means.
*  There are some people that think neuro AI is about using AI to understand neuroscience.
*  And then there are people that think neuro AI is about using insights and principles
*  from neuroscience to improve AI.
*  And AI could be hardware, software, or a combination of the two.
*  So we kind of left it open ended because we told people for the purpose of the neuro AI
*  workshop, we're really more interested in the convergence and the reciprocal aspects
*  of neuro AI and not in the feed forward using AI for any science approach.
*  I wouldn't say begrudgingly.
*  I would say this is where the opportunity is.
*  So in this interview, we both have to be clear about when we're speaking from the perspective
*  of the brain initiative, when we're speaking from our own scientific perspective, from
*  the perspective of the brain initiative, there's a lot of interesting opportunity here.
*  And so in my opening remarks, I showed a figure from Brad Heimany's review paper of the four
*  or five main threads of this kind of how AI has evolved from different ways of computing
*  through learning with data.
*  The question is, how does all this come together and what do more brain like forms of this
*  type of computing by learning with data?
*  What does that look like going forward?
*  And there's been a few major inspirations from neuroscience from the brain over the
*  decades since good old fashioned AI in the 50s where you had these symbolic approaches,
*  Newell and Simon coming out of cognitive science.
*  And then we're all kind of familiar with the history of the back and forth there, the AI
*  computers, connectionism rose in the 80s with the advent of neural networks and back
*  propagation for updating weights.
*  And it's only in the last 115 years did the scalability come into play with the hardware
*  that enabled the amazing advances that we've seen in the last 10, 15 years in what we now
*  call AI computing or AI technology.
*  And so the convergence right here is really ripe.
*  And I think we should not be arguing about definitions necessarily because people in
*  cognitive science and neuroscience and artificial intelligence are very good at arguing about
*  terminology and definitions.
*  We could bring in the consciousness researchers if you really want to go to…
*  Leave the philosophers out because they're the best at arguing about semantics, right?
*  Right.
*  Well, we do need people worrying about this.
*  But I think it's at this early stage in this kind of like this exciting convergent period,
*  there's a lot of decades of thought and research going into all these different threads.
*  And they've all hit kind of fairly related roadblocks, it seems.
*  Cognitive science didn't become that fully encompassing research program that started
*  in the 60s and 70s that Miller kind of anticipated.
*  Neuroscience has kind of gotten wrapped around certain ideas, attractor dynamics and population
*  geometry, and we're trying to figure out if this is the right way to go or not and
*  how to incorporate large scale data.
*  But maybe coming together, we can solve all these problems simultaneously.
*  I guess I want to defend my personal position a little bit about being…
*  Begrudgingly.
*  Begrudgingly with the word AI because this would be the second time that the word neuroAI
*  was put in a program or in a concept that I'm working on.
*  When I was at the National Science Foundation back from 2020 to 2023, I created a program,
*  a topic that was part of the Emerging Frontiers in Research and Innovation Program called
*  Brain-Inspired Dynamics for Engineering Energy Efficient Circuits and AI.
*  The original name of that program was not…did not have AI in it.
*  But because AI was so hot, my former NSF leadership said AI's got to be in the title.
*  And so that was kind of where I was coming from, Joe, is we have to use the word AI because
*  it's gotten so in vogue these days.
*  Well, I think it's useful to use the words that people are using.
*  Right.
*  And it's a new term.
*  I think it's not fully well defined and that's kind of what this workshop was about.
*  Let's bring together…
*  So Grace and I have been going to neuroAI conferences and workshops, a lot of them over the last
*  year as I know you have as well, Paul.
*  You see a lot of themes emerging and so brain is interested, well, let's explore what potential
*  roles look like.
*  Is there a piece of this where brain can help, where it fits within brain's mission to
*  go forward?
*  And so we want broad input from the community.
*  For the workshop, we wanted broad input from the community.
*  I think we got it about helping us identify what those opportunities are to be considered
*  further.
*  Yeah.
*  What I wonder is…
*  So I hear when you have a new hot term like neuroAI, it makes me think of, you know, if…
*  I'm not sure what hats you want to put on if you respond to this, but speaking scientifically
*  or from the NIH, but you know, you have to put the word mechanistic in all of your papers
*  now because that's, you know, mechanisms became the hot thing and computational neuroscience
*  is dominated by mechanisms.
*  And I've heard that the sentiment I'm about to express, expressed among grad students
*  just in the past few weeks, you know, of like everything now is neuroAI and if you want
*  funding for anything, you just call it neuroAI and therefore you don't really have to worry
*  about how what you're doing fits into neuroAI.
*  And if it's ill-defined or not defined at all, then…
*  So here's the worry is that like, all right, so then there's going to be this surge of
*  grants and everyone's going to use the hot term neuroAI and that's going to bolster
*  their chances of getting funded.
*  And I'm not sure if there's a solution to that because that's just the name of the game,
*  but I don't know if you have a response to that.
*  It's always something like that.
*  You can't control, you know, the community.
*  You can't control people.
*  Essentially, you have to communicate in a way where, you know, people say need to be
*  clear about what they're doing when they're applying for funding.
*  And we have, you know, obviously the NIH and NSF and other funding agencies have scientific
*  review processes in place to kind of discern who's maybe following hype and over claiming
*  or overusing words versus where the real advances are.
*  And that's obviously not a perfect system.
*  Right.
*  And I'll say from my experience when I was at the NSF, for the BRAID topic, we had very
*  strict solicitation specific criteria that would filter out people who are just using
*  the buzzwords to try to get in.
*  And I think having strong review sections would avoid these kinds of problems.
*  I do want to say that there is a true inflection point here in that the technologies that's
*  been enabled by the BRAID initiative is allowing us to observe circuits in animals across many
*  different spatial and temporal scale.
*  And so there is a real opportunity.
*  And I think just putting the word neuro AI on any project is going to be easy to filter
*  out.
*  Perhaps.
*  So, yeah, I mean, I think that that that little light bulb went off in my head when Grace
*  used the term begrudgingly because I can that sense that I get from these handful of people
*  who have it's sort of an eye roll like, oh, that must be neuro AI, you know, like because
*  that's just a hot term or something.
*  So I'm wondering, man, is this I already feel like the backlash of this emerging field.
*  So I originally wanted to call this workshop the brain neuro AI and theory workshop because
*  I wanted to bring neuro AI.
*  I wanted that convergence point to be focused on advances in theories, theoretical frameworks
*  and theory driven models because I think there's so much there.
*  And I think that's where a lot of the obstacles in all scientific opinion of my personal personally
*  speaking, that's where I think a lot of the obstacles have been.
*  I mean, there are a few unifying theoretical frameworks of neuroscience and you've discussed
*  them on this podcast over the years with a lot of people who have, you know, have been
*  made major contributions to those theories.
*  But I don't see, you know, I don't see that CUNY and kind of process of the field, you
*  know, testing confirmatory hypotheses, falsifying different theories and making progress.
*  And so I think maybe this interdisciplinary process, whatever we're calling neuro AI can
*  help dislodge some of these stale debates and arguments and help us get to a new conceptualization
*  of what's really going on in brains and which by the way are fundamentally embodied and
*  inherently integrated as biological systems, which is different from AI.
*  And I also think being a little loose with our definition is OK because, you know, we
*  were able to bring in the neuromorphic community.
*  Yeah, it was a huge, I mean, maybe let's talk about just the reason that the workshop existed
*  and just how you managed to how you decided how to frame it, how to organize it.
*  And because the neuromorphics was a larger part of the workshop than I had anticipated
*  it might be if one just said we're going to have a neuro AI workshop.
*  And that's all I had to go on.
*  So for me, you know, coming from the NSF to the NIH, I was shocked that there was very
*  few investment in neuromorphics at the NIH.
*  If you go into the NIH reporter, you type in the word neuromorphic, you'll probably
*  get 60 returns and under 20 million investments since the 19 late 80s, whenever NIH reporter
*  was started compiling information.
*  Is that because neuromorphic is inherently slow?
*  Is that the reason?
*  Well, it has been slow, as we heard from the last two days.
*  But I think the other part of it is just that the neuromorphic engineers and the neurotech
*  and biomedical engineers go to different meetings.
*  They don't really talk to each other.
*  And so for me, it was really important to bring to close the loop between neuromorphic
*  and neuroscience so that we can better benefit brain health and not just brain, but health
*  in general.
*  And that that was very critical for me.
*  And I actually hosted co-hosted a workshop with my colleagues at the NSF with co-funding
*  from NIBIB and NINDS in late October in Baltimore.
*  It was a workshop called the neuromorphic principles in biomedicine and health care.
*  And it was important to capture the health focus for neuromorphic and neurotech at this
*  workshop.
*  And that was why the second day was designed to be more like a tutorial.
*  The first session of the second day was intended to teach everybody what neuromorphic means,
*  both large scale digital computing style of neuromorphic, as well as the small scale mixed
*  signal analog computing and neuromorphic sensing, which we had Jacque Molland-Deverie as well
*  as Ralph Etienne Cummings, who really, I think, helped teach the audience the differences
*  between the different kinds of neuromorphic technologies and how they may or may not be
*  useful in health care.
*  And then the second session was to really bring it home and have clinicians talk about
*  the value of neuromorphic technology.
*  Yeah, just as an interjection.
*  I mean, I've done some conversing with people, like I just said, you know, reflecting about
*  the workshop.
*  And one of the things I said to another academic was I was surprised that there was, you know,
*  so much neuromorphics in the workshop.
*  And this person said, what's neuromorphic?
*  I was like, whoa.
*  And there were neuroscientists, you know.
*  It's surprisingly not very well known.
*  And that's one of the exciting opportunities and why we wanted to have good, you know,
*  healthy representation from neuromorphic approaches.
*  Wait, because we should, Joe, maybe just say what neuromorphics is because I realize there's
*  thousands of neuroscientists, I guess, who don't know what neuromorphics is.
*  Let's introduce it.
*  So this question was asked by an audience member at the workshop, you know, what is
*  the definition of neuromorphic?
*  And nobody wanted to take that on.
*  Well, I admonished folks not to get into debates about definitions.
*  Yeah, yeah.
*  But I just knew like broadly what are we talking about?
*  But I'm saying so Klappen Abohen, who is also a leader in neuromorphic computing, he's put
*  forward, it's computing that scales.
*  It's scalable computing.
*  So in order to have fundamentally scalable computing, you need to be more brain like.
*  You need to have memory on compute.
*  And so the closer you get to the brain, which is very fundamentally a memory on computing
*  system, then you break or bend some of the scaling laws that make it difficult to scale
*  up conventional CPUs, GPUs on CMOS processes.
*  But neuromorphic, I mean, I would say it kind of comes to the Feynman quote that we see
*  everywhere, right?
*  And there were two good Feynman quotes that came out of the workshop.
*  But the one that you see everywhere is, you know, paraphrasing, you know, what I cannot
*  build, I cannot understand, essentially.
*  And so the neuromorphic engineering community is folks who have been trying to build it.
*  I mean, they've been from the SNF level to the cellular level to the...
*  The original lineage, Carver-Mead lineage of neuromorphic engineers were people that
*  were trying to emulate these channels on a chip and creating spikes and characteristics
*  that are comparable to what you would measure off of a cat pyramidal cell.
*  That was the original Nisham Ahabah 1991 paper that I think first popularized neuromorphic.
*  And that's what Ralph referred to as old school neuromorphic.
*  But since then, there's been all sorts of development, which is why it's so hard to
*  define neuromorphic.
*  It's a word that, you know, it means different things to different people.
*  And it could even mean principles.
*  You want to, you know, as Kai said, you want to have your device that operates with the
*  statistics of the signals from the brain, right?
*  So some people even think of neuromorphic as principles.
*  Whether or not...
*  But it could be physical principles as well.
*  Yeah, physical and material principles as well.
*  Guiding principles.
*  Whether or not you actually use a neuromorphic hardware is...they don't...it's okay.
*  So there's people in the neuromorphic community that think of neuromorphic as hardware.
*  And there are others that think of it as design principles.
*  So it's hard to define neuromorphic.
*  But for me, it's brain-like.
*  It usually operates on spikes, but not always.
*  Most importantly, it's energy efficient.
*  Six orders of magnitude energy efficiency.
*  And it's adaptive to the user.
*  It's a system that can evolve with the user.
*  And those are the four things I think that really stood out and was discussed at the
*  panel.
*  And people went as far as saying because it's adaptive, it's less hackable because you don't
*  actually need a computer to run it.
*  The on-chip device is self-containing.
*  Well, I'd say it's important to distinguish not all neuromorphic hardware is learning
*  hardware.
*  A lot of the testbed systems that have been developed...So Intel had a program called
*  Loihi.
*  There were two generations of these Loihi chips that were basically...it's an academic
*  research partnership program.
*  You can get some of these chips to devise models for and test and run them.
*  And those were...you could have a large number of spiking neurons, essentially.
*  You integrate and fire neurons and you could just run that physically on these chips.
*  But it was very difficult to implement spike-based learning rules like STDP on those chips.
*  So there's other kinds of chips which are more amenable to implementing different types
*  of learning rules.
*  But that's something the field is still working on and trying to figure out.
*  And it's one of the big questions going forward.
*  How do you have these be adaptive in a safe way?
*  That's a really good point.
*  There are some chips that are designed for inference only and others that are designed
*  for learning.
*  So I totally see how neuromorphics...and it sounds like the whole thing was focused on
*  neuromorphics, which is not the case at all.
*  But this is just a way into talking more broadly about the workshop.
*  I totally understand why neuromorphics then would be something to put a large focus on.
*  But then the question is like, okay, so what Joe was talking about earlier about needing
*  to bring in theory and get all these people sort of under the same roof to sort of bring
*  together these otherwise kind of disparate ideas to work on the problems.
*  One could wonder, well, what is that?
*  What you guys were just describing?
*  What does that have to do with anything related to theory?
*  So did we make progress on that or is that an ongoing challenge?
*  It's an ongoing challenge.
*  I mean, so the workshop was to bring...like Grace said earlier, there hasn't been enough
*  conversation between these fields.
*  And so that was very intentional on our part to bring together these different communities
*  to start having that conversation.
*  Even within neuromorphic engineering, the folks who want to use large-scale neuromorphic
*  computing systems to basically run large models of the brain.
*  And so they need large-scale brain data to build those kinds of models, connectomes and
*  cell types and that kind of thing.
*  And so you can use that as a test evaluation system, a modeling and simulation system to
*  or falsify theories about how certain aspects of these networks work.
*  But then there's the small-scale side of it, energy-efficient analog or mixed signal devices
*  that can be distributed to the edge to do brain-like, neural-like intelligent computing
*  in a wider array of applications.
*  And that's more towards the translational end.
*  But I think it covers the full spectrum.
*  And I want to go back to the theory.
*  I don't think we talked a lot about it.
*  So Brad Iamony actually came to the NIH and gave a Wednesday afternoon lecture series
*  talk on October 23rd where he talked about how large-scale neuromorphic computing could
*  inform new theories, how you can make observations at scale that you just don't see in smaller
*  circuits.
*  It's much more difficult and particular to the types of models that you're building,
*  how to scale them up.
*  And so I think there's opportunities here to break some of those scale barriers within
*  computational neuroscience and theory-driven modeling and take it to the scale where the
*  things that we care about happening in brains can actually be studied in a principled way.
*  So okay, we've kind of been focusing on neuromorphics and then we delved into theory, but I didn't
*  say in the beginning the backdrop of this is that the Brain Initiative is 10 years old
*  now.
*  So part of the driving force, and correct me if I'm wrong with putting this workshop
*  together, was to figure out where the future roadmap should lead or what avenues are explorable
*  and should be explored moving forward.
*  Is that a fair assessment?
*  Well, we wouldn't use the word should, right?
*  Because we want to get all...
*  Right, exactly.
*  We want to get the shoulds from the community.
*  What are the different...
*  I think we have the neuromorphics, we've got the people doing metrics and benchmarks, we've
*  got the people thinking about natural intelligence capabilities.
*  How do they all come together?
*  What are the main priorities and opportunities they see?
*  And we want insight about that.
*  You got some shoulds, at least during my last session there.
*  There were some shoulds from the audience, which was fun.
*  So good.
*  So from the Brain Initiative's perspective, we want to see, okay, get all these pieces
*  together in this jumbled puzzle and then figure out which of those pieces makes sense for
*  the Brain Initiative potentially to contribute to, to lend the type of work that we do in
*  the Brain Initiative.
*  Another thing I would say as a co-organizer is we invited a lot of other funding agencies
*  to this meeting, to be part of the workshop, because a lot of these problems aren't necessarily
*  brain's problems, right?
*  It's like coming up with the next super-efficient computing system is a great idea and it's
*  great for humanity, it's great for solving the carbon footprint, but that probably lies
*  in a different agency's mission space.
*  However, the knowledge the Brain Initiative collects and continues to generate is useful
*  to that longer-term mission.
*  And I was really hoping that would be clear from the funders panel.
*  I don't know if we hit the mark there, but this is really a collaborative effort where
*  lots of agencies are interested for different reasons.
*  Yeah.
*  I want to kind of complete the circle on just what the workshop was about and how you decided
*  what kinds of topics to bring in.
*  So when I think of neuro-AI, I think of like the...
*  It's not traditional, it's new, but it's not new.
*  But it's like kind of testing, like using some artificial intelligent models, neural
*  network models, as proxies for brain prostheses and then asking whether you get something
*  brain-like representationally out of those systems, like the sort of early work with
*  convolutional neural networks and modeling the visual object recognition system on those
*  networks.
*  There's been a lot.
*  Since then, there's been a lot of recurrent network work like that.
*  And then someone like Andreas Tullius, who works on what are called foundation models,
*  was represented.
*  So that sort of side of it was also represented.
*  But maybe you guys could speak to what you wanted, what other kinds of things that you
*  wanted to bring into the workshop.
*  I think that's our personal scientific opinion and perspective at that time, which came out
*  of the symposium that Grace and I co-organized for the 2020 Brain Investigators meeting.
*  That was a great panel.
*  We had Conrad Kording and Zach Picko and Nathaniel Da, Kanaka Rajan, and I'm forgetting, Brad
*  Pfeiffer on that kind of...
*  We called it Dynamical Systems, Neuroscience and Machine Learning.
*  That's what we were bringing together, but it's a prototype for neuro-AI thinking these
*  ideas through.
*  But the perspective that Grace and I wrote coming out of that was that a lot of the problems
*  seem to be from this purely computational perspective.
*  And that's the perspective that's kind of grounded in this almost traditional brain
*  as computer metaphor that has pervaded all of these fields.
*  Pervaded, cognitive science, AI, and neuroscience.
*  Neuroscientists talk constantly about neural encoding, neural decoding representations,
*  talk about representations as these computational constructs.
*  And that once you have representation and it has to the experimenter some explainable
*  relationship with what we think is going on in the animal.
*  Like we put it in the task, so it needs to go left at this point after seeing this cube
*  and we see correlations to the right kinds of things.
*  And it's like, okay, we found the computational representation.
*  That is the explanation, we're done here.
*  So I think the we're done here part of that has been the barrier because you're not actually
*  done there because there's still behavior that needs to be in the loop.
*  There's this moment to moment dynamical coupling between brain and body, between body and environment.
*  And so that's why we wanted to expand outward and bring in ideas from embodied cognition,
*  the 4D literature.
*  And not to sign on to that, but to say, hey, there's something here about these massive
*  distributed feedback loops through the environment that are a key part of what's going on in
*  cognition and animals.
*  So that's kind of where we took this.
*  And day one was designed to be all computational intelligence, whereas day two was more the
*  embodied neuromorphic translation.
*  Even during day one, I was impressed with how many people were reflecting on the importance
*  of embodiment.
*  I mean, it came up a lot.
*  That was not planned.
*  It was a surprise.
*  I may have I may have planted.
*  Did you plant that seed?
*  Is that what?
*  Well, for instance, in the same issue in which our paper came out, there was another paper
*  called Deep Intelligence by Ali Manai, who's an electrical engineering professor at University
*  of Cincinnati.
*  And so I was aware of that work.
*  And he's done computational neuroscience for a long time now, since I started in the field
*  in hippocampus.
*  So I was aware of him.
*  But he had a very evolutionary perspective on it as well.
*  He has a very holistic perspective on biology.
*  Biological organisms are inherently integrated.
*  They're integrated through evolution phylogenetically.
*  They're integrated through development ontogenetically.
*  They're integrated through learning and aging and experience.
*  And you have to keep coming back to that because that is kind of well, at least that was his
*  perspective that he was taking in the paper and in the talk that we invited him to give
*  comparing natural intelligence with AI.
*  And there's so many important distinctions that you can make.
*  But I think that's one of the key ones.
*  And so we can't call it just occurred to me that like holistic neuroscience would be a
*  great term, except that it would be associated with holistic medicine, I think, which the
*  word holistic has some positive and negative connotations.
*  Right.
*  I think it gets into the impulse for reductionism and the kind of counter movement of looking
*  at downward causation and emergence.
*  Well, I just meant the science of holistic medicine is sometimes questionable.
*  So to be a holistic neuroscience, someone might see that and think, oh, it's woo woo
*  or something like that.
*  But on the whole, that's a pretty good phrase.
*  I think it's woo woo if you do ignore the internal computational representations.
*  You can't ignore it.
*  That's why across two days we had the focus on, yeah, so a personal opinion is calling
*  it kind of the mainstream neuro AI.
*  Let's figure out how to map these task constrained AI models to what we see in the ventral visual
*  stream.
*  And it has been, like you said, a lot coming out of that.
*  People are looking at dorsal stream.
*  People are looking at motor system and other areas.
*  Cognitive maps.
*  Cognitive maps.
*  Yeah, you name it.
*  Well, cognitive maps are maybe the clearest example of actual high level cognitive encoding
*  in the brain.
*  At least that's my personal opinion as a hippocampal researcher.
*  Yeah, well, I just mean like-
*  Hippocampal chauvinism.
*  Applying neuro AI models to account for cognitive functions, cognitive maps has been a big-
*  Absolutely.
*  No, I think it's an important, I mean, it ties into the dimensionality reduction, the
*  task based low dimensional manifolds.
*  Yeah, we're hurting hundreds of thousands or millions of neurons now.
*  There's no way to visualize that.
*  If you just throw everything into a U map, you get some interesting colored splotches
*  on your screen, but it doesn't tell you how to interpret what's happening.
*  Oh my gosh, you're speaking to what I'm, I make some really pretty naturalistic behavior
*  neural U map graphs right now and gosh, they're pretty, but they're not the solution.
*  I'm not done.
*  Right. When this ties into the whole interpretability, explainability, and mechanism
*  discussion, how do we get at what the important factors are that are driving
*  that high dimensional neural activity?
*  Oh wait, so now you're just jumping the gun and going right into, I mean, maybe that's the way
*  that we should do it is talk about some of the topics in the paper and then bounce back and
*  forth, but I don't want to also not come back at least to, well, actually let's hold off on going,
*  I know that they're all related.
*  I'm saying that you need both, right?
*  Okay, so then I'm not sure what we've missed about the workshop, but I wanted to get your
*  kind of general reflections on how it went.
*  Yeah, I mean, so from the point of view of the workshop, we were both incredibly thrilled and
*  pleased at the discussions that we had and thank you, Paul, for stepping in as I discussed it on
*  the first day and for helping with the wrap up on day two. Yeah, we've been reviewing the recordings
*  and it's, when you're in the middle of it, you don't get to really listen and experience it,
*  but it's really great conversations and discussions and questions that we had.
*  At one point in my first discussing panel thing, I got to yell at Terry Sanowski and I thought like,
*  oh, why am I saying something negative about, to Terry Sanowski about what he said? As I was
*  saying it, I was having this moment like, oh, you're not in a position to even talk about this with
*  him, but he was fun. It was fun because he's like a hero, intellectual kind of hero to many people,
*  including myself. And so you're in that situation and this is maybe very meta, so I apologize, but
*  you're talking to your heroes sometimes and you realize either they're a colleague or they're a
*  hero and it's just kind of a not surreal, but an interesting feeling.
*  Well, this is why we brought everyone together. We want the leaders of the field who have been
*  around and just driving things forward for as long as anyone can remember. Oh, sorry.
*  And his colleagues had won the Nobel Prize just a few weeks before the workshop.
*  And if you talk to people around that and you go back and read those papers from 84, 86,
*  Terry is a co-author in all of that.
*  I was wondering how he felt about that. I'm not sure if it's the right place to discuss that,
*  but I imagine a lot of people have wondered, like, does he feel like he was missing from that?
*  Well, the day the Nobel Prize was announced, the Telluride neuromorphic community overtly
*  wondered why Terry was left off. I saw a few things like that.
*  That was shared upon all of us who attended Telluride this year. So it was good to be able
*  to acknowledge Terry's contribution at the workshop through multiple talks. And I think you were fine,
*  Paul. You were. Oh, no. Yeah. But he corrected me, which he corrected me, which was which was
*  wonderful because he correctly corrected me. And then I was like, all right, I'm not going to
*  get into a back and forth with this person. I have to say, every time I felt something
*  didn't go well, I went back and listened to the recording. I was like, oh, it went way better than
*  I thought. So I think the workshop was really a great success. And I learned things that I
*  didn't expect to learn. Well, I came away thinking that it felt like a win, a great success. And so
*  I'm not sure if you guys want to elaborate more on how you or reflect more on how you felt about
*  how it went and maybe even what could have been what may have been missing that will happen next
*  time or how this how reflecting on what happened here affects how you think about moving forward.
*  I feel like the ethical, the neuro ethical conversation was a really important one
*  because neuro AI is going to bring about a lot of new challenges. And that Karen Marble
*  Finders talk was really insightful. And I think, you know, if we were to have another one of these
*  workshops in the future, you know, I felt like we didn't give her a chance to ask her a question
*  because we ran out of time. You know, so it may be a little more actually, to be honest,
*  though, I don't think you could do neuro AI ethics justice in half in a one hour session. So
*  there ought to be more conversations about ethics and as well as regulatory questions.
*  Yeah, we can't speak directly about the future. But, you know, clearly, you know, brain put on
*  this workshop is interested in the space. And we and you know, we agree, we think it was it was a
*  great success as far as our goals of hearing from now from everyone. How do you think there was a
*  scientific community that was not represented at the workshop that should have been? Well,
*  oh, geez, putting on the spot here. I mean, in some sense, so I was rereading your position paper.
*  And maybe this is a segue into that. Because, yes, there's a lot of embodiment.
*  And I'm trying to reflect now myself, because as I'm reading through this paper, the title of your
*  position piece, neuro dynamical computing at the information boundaries of intelligent systems.
*  And so I'm reading through this thing again, and it's so rich and dense and and makes the case for
*  embodiment and the importance of environment, body, brain, continuous cycle interactions.
*  And of course, and then I'm like reading, I'm like, Oh, my God, I click on every reference. And I'm
*  like, half the time, I'm like, Oh, good, that's good. I've read that. And then the other half,
*  I'm like, I got to add it to my reading list, you know, and it's like, it's but so in some sense.
*  And the irony is, my original job was to send it at the end was to synthesize the workshop.
*  And I didn't, to be honest, I didn't really know how I had an idea of how I was going to do it.
*  But I didn't have like a set plan. And it ended up being like a more of a moderated discussion,
*  which was great. And then a lot of interaction from the audience as well. But the reason why I
*  said synthesize, and I think Joe might have mentioned that term earlier, is because your
*  position piece synthesizes a ton of stuff with the goal of using so much historical perspective,
*  and what's maybe missing these days in AI to synthesize what you call a base layer of
*  computation. You're going to correct me on this. I don't have the exact quote,
*  but a base layer of neural computation. I think that's what we called it. Yeah.
*  Okay. Well, I know it's called a base layer. But yeah. And so you asked me what I thought
*  might have been missing. It might have been that sort of bringing together of the historical
*  context and why these things are important. And then an interesting thing happened that two people,
*  Blake Richards and Zach Pitko, Zach at the very end said, a great goal for us would be to record
*  the connection strength of every synapse. And that's such a reductionistic approach that is
*  in line with modern reductionist neuroscience. And it kind of flies in the face of what you guys
*  argue for in this position piece a little bit. And I thought it was odd that there was still kind of
*  this reductionist assumption underlying all these things to measure more. And here's the level that
*  we need to measure at. And modern dynamical systems theory, manifolds, looking at larger
*  populations and that lower dimensional structure is somewhat antithetical to that story. So if
*  anything, I thought maybe like that the whole even manifold and more talk about like levels
*  and going across levels, what's the right level of abstraction, why it's the right level of
*  abstraction. And that's more on the theoretical side. If anything, I thought there could have
*  been more of that, I think. Man, that was long-winded. I apologize.
*  That was more of a comment than a question. No, I totally agree. So here I have to be very careful
*  to differentiate my perspective opinion on the field. As I said, Grace and I wrote this paper
*  a couple of years ago now. And this did kind of come out of a wide range of frustrations,
*  which is why I went deep historically and I brought in ideas from philosophy of mind,
*  philosophy of computation. Let's think about what is computation? What does computation mean in the
*  brain? What does information even mean in the brain? Because one of these other things that pervades
*  all these fields, and I do give like a historical capsule at the top of the paper,
*  cognitive science, neuroscience, AI, is this kind of, they have the same conception of what
*  information is. It's Shannon information, which as we know from the 48 paper and the later one,
*  where it's about communication where you have a transmitter and a receiver and you have a shared
*  alphabet. And that may not be the right metaphor or framework for understanding information in the
*  brain, especially how brains construct semantically meaningful structures and processes and dynamics.
*  Well, Shannon was even aware of this conflation of information with meaning. And there's a very
*  short, I could put it in the show notes, he actually wrote up a very short piece saying like,
*  look, people, this might not apply to your field because everyone was applying Shannon
*  information to their fields. So he was warning against his own work being applied too broadly
*  and misconstrued. Yeah, I think I've seen that. And it kind of reminds me, but also Tony Zador in
*  the opening keynote brought up the concept of the hardware lottery. So in a sense, Shannon's
*  information theory is kind of a theory lottery. It provided everyone a readily accessible tool.
*  Yeah. For like, oh yeah, information, this is a really important concept. How do we measure it
*  and grab hold of it? It's like, okay, well, here you go. You just run these sums and averages
*  over this kind of distribution. It's a purely a statistical process now. It's purely syntactic.
*  And I think it was Shannon maybe at that piece who said, this is purely syntactic. This does not get
*  at the semantics of what this actually means. And if we think about, so this paper, Neurodynamical
*  Computing at Information Boundaries, it's because there's different types of information and they
*  are transformed across the boundary of an organism. And so you have the-
*  But now you're not using information in the Shannon sense. You're using it in a-
*  Right. So what is different about information in a biological cognitive organism? Organisms construct
*  a boundary. It's our skin, but it's also our exteroceptive senses. And we have ways of taking
*  in information. You have the whole universe of sensory input coming in, but then you also have
*  the internally generated universe of goals and drives. So organisms are in constant conversation
*  with the environment. We depend on the environment for energy. That's why foraging is such a
*  fundamental problem for animals. Animals fundamentally, what defines them is that they
*  move. And they move in order to forage and find food and energy and then safety and shelter.
*  So they can move. So they can find more food so they can move more. So they can find more.
*  Well, it turns out ecologically, there's a lot of niches that open up if you can move through the
*  environment. Otherwise you're a coral or you're a sea squirt attached to a rock somewhere or you're
*  a filter feeder. People will take umbrage to the idea that those don't move by the way. Some people
*  will, even plants. But yes, I get the point. There are sessile animals. I did not mean to offend the
*  sessile organism community, but movement is fundamental to all of this. And so it's that
*  dynamical coupling at those informational boundaries that allow the goals to basically stream
*  against the incoming sensory inputs along that kind of like hierarchy of both perception,
*  you know, ascending, the hierarchy of drives and movement and behavior control descending.
*  And so that was our perspective that you can think of. It's related to like the predictive
*  processing framework like Carl Friston's unifying theory where he sees the brain as a distributed
*  internally generated feedback model and you're canceling out prediction errors as they ascend
*  with the top-down expectancies. And then there's trade-offs that are governed by
*  his conception of free energy. But that unifying theoretical framework has had trouble gaining
*  traction about making direct predictions about what people should be doing in neuroscience.
*  What type of experiments should you design to figure out, oh, this particular function,
*  it operates this way within the predictive processing framework in a way that's
*  distinguishable from some other framework. And so I'm just trying to step back and not put a name
*  on things, but fundamentally organisms construct meaning through kind of managing basically the
*  entropy at this interface. And so that maybe that's prediction error, maybe it's something,
*  some other quantity, but you need to manage entropy. Fundamentally, that's what you're doing.
*  Thermodynamically, we're far from equilibrium. Like that's the whole game.
*  And that's the control theory aspect of it. Is that where that comes in as well? So what I was
*  going to say originally is injecting meaning back into neuroscience is not the default.
*  The default in neuroscience is this reductionist, brain is a computer, and then we can go from
*  sensation back to, and we can disregard goals and meaning and purpose. That's kind of been the
*  default position of most neuroscience for a long time, although in the paper and elsewhere,
*  it's pointed out like that early cyberneticists movement was more about control. And so I guess
*  that's why I'm asking, is that where the control theory aspect comes in?
*  So that ties into, so in this paper, which again was our perspective, we found the most,
*  I guess, simpatico framework out there to be what's called perceptual control theory.
*  And so this is an alternative branch of cybernetics essentially from the 50s and 60s that was kind of
*  brought home or initiated by Bill Powers in the 60s and 70s.
*  Yeah. So like Henry Yen, whom you cite in the paper and who's, he's been on this podcast,
*  many of the references in your paper. You influenced us too, Paul.
*  Well, just by having maybe by having people, yeah, through the podcast. Thanks. That's awesome.
*  Yeah. It's awesome to see so many references in a paper. It's like, oh, that person has been on
*  the podcast. That's the person's book. So I just mentioned Henry Yen and he was saying one of the
*  problems with early cyberneticist research and control theory in general actually is that
*  the reference signal of a machine is external to the machine. Whereas we have internal reference
*  signals that we're trying to control to match for those reference signals. And that's a fundamental
*  difference. And that's what neuroscience is missing. And so I don't even remember my question,
*  but that is what you speak to in the paper as well.
*  Right. Yeah. So Henry's written a couple book chapters with this perspective and they're kind
*  of bomb throwing chapters in a way. And I think it's helpful to have strong opinions out there,
*  right? Because it really makes you think, okay, this kind of sounds interesting. It's provocative,
*  but where does it go wrong? And so that's, or does it go wrong? So that's kind of reading that and
*  reading, I'm not a motor systems person, but I have passing familiarity with the motor control
*  paradigms. Those theories coming out of the 90s and 2000s, optimal feedback control,
*  conceptions of motor commands, the theories and models about effort to copy and corollary
*  discharge systems. And all the traditional motor control systems or frameworks were based on
*  building up more and more detailed and refined internal models, basically forward models,
*  to predict the consequences of action and movement. And then using that to evaluate
*  different commands and behaviors and then putting that in this much larger,
*  much more complicated control loop. And PCT or perceptual control theory is appealing because in
*  a way it kind of reverses it. It says, no, what only matters is that you're only making comparisons
*  at each level in this hierarchy because you're making direct perceptual comparisons.
*  And so if you have a direct perceptual goal at the highest level, then those reference points
*  come down, they're compared to the ascending perceptual input. And then that descending
*  reference to the next level gives you what you need. And then so-
*  And eventually it filters out through your muscle actuators and your movements in the world.
*  But it's not eventual because it's all simultaneous, right?
*  It's all simultaneous. Yeah.
*  Everything, it's a staged flow of control signals, right? Sensory and control signals across a
*  hierarchy. I'm individual in terms of time. Where one signal flow starts, it takes time to propagate.
*  Not that there's a central organizer that says, go and then from nothingness. Because yes,
*  the part of what you push for also is this consideration that perception and action cycles
*  are continuous flows. Right. And so that phrasing kind of ties into this conception of everything
*  as being linear. Input, output, right? So if you have a cycle, it's like, okay,
*  first you're at this step and then you're at the next step. So you're at sensation,
*  then you're at cognition, then you're at motor commands, and then you're at behavior.
*  And then that changes the pose, the orientation of the organism with respect to the environment,
*  which changes the sensory inputs. And now you're back at the beginning of the cycle.
*  And so if you have a very complex computational forward model in that control loop, then you have
*  to imagine that the delay of computation is now a delay in your control loop. And from a control
*  theory perspective, from a control engineering perspective, the more delays you have, the weaker
*  your control is. Yet one of the, I think the most dispositive or fascinating properties of animal
*  behavior is that it's really good. It's really resilient. Animals can accomplish their goals.
*  Not always, but they're very good at it. Yeah.
*  Right. But compared to the variability of the observed behavior. So the robustness of accomplishing
*  goals far outstrips the actual movement. It seems like, wait a second, how is any of this possible?
*  How is it possible for a rat to make its way through this very complicated burrow with basically
*  no light and only a small set of sparse cues, but it can navigate that burrow really well.
*  And so it comes down to, well, maybe you don't have all this complex computation going on in the loop.
*  And so this is a conversation that I've tried to have over the years with people working in motor
*  systems and they think either I have the wrong idea or Henry has the wrong idea or actually
*  all of their theories already encompass this idea. Don't worry about it. But it seems to me,
*  this is an open, for my personal scientific opinion, this is an open question of forward
*  versus inverse models, ascending like prediction error comparisons versus perceptual reference
*  point comparisons up and down the hierarchy. And that's some of the discussion that I wanted to
*  open up at the workshop. So from a brain's perspective, I'm not going to impose my views
*  on this, but I see that that's an important conversation. And I think that will open up
*  a lot of potential opportunities for driving theory forward and data is a part of it.
*  So the reduction is obviously molecularly characterized cell type atlases of whole brains,
*  very fine grained conic tomics data sets, the flywire data set that was just released,
*  which was brain supported on a number of grants. And there's more to come. We launched the Brain
*  Connects program last year and we'll start seeing data from those projects in the next few years.
*  Lots of exciting stuff to come, but that's obviously from a very reductive approach to
*  neuroscience, break things down and just so we can see everything that's there.
*  But I think that does need to be in the loop with this more holistic way of thinking.
*  And so I think that's where there was a lot of talk about digital twins, multi-scale biophysical
*  modeling, and then thinking about different ways of putting this in the loop with behavioral
*  neuroscience and different ways of understanding them.
*  That was definitely a surprise for me at the neuro AI workshop.
*  There was so many talks about digital twins.
*  Oh, even in sessions three and four, it seems like the community is really ready
*  and really want digital twinning in their respective research areas.
*  What's a digital twin and why do we want one?
*  Well, that's another definition question.
*  Well, you don't have to define it, but actually there actually is a
*  definition that the National Academies of Science, Engineering and Medicine put out.
*  I have it in front of me.
*  I'll read it to you because a digital twin is a set of virtual information constructs
*  that mimics the structure, context and behavior of a natural, engineered or social system
*  or system of systems is dynamically updated with data from its physical twin,
*  has a predictive capability and forms decision that realize value.
*  The bidirectional interaction between the virtual and the physical is central to the digital twin.
*  That is like the, that's it.
*  That's the official definition.
*  And I think people have their own definitions.
*  Yeah, I'm sorry I asked for the definition.
*  Just kidding.
*  And they were using their own definition, which is a subset of this official definition.
*  And this actually was a question that came in in the email.
*  I was surprised to hear so much digital twin talk and I think that's potentially
*  a new exciting area that could, that the Neuro AI Workshop participants can continue to engage in.
*  I think there's an important continuum there as well.
*  So we heard some of that discussion in the first session of the workshop
*  between neural foundation models on one side and digital twins on the other.
*  So these are both large scale ways of using large scale neural and behavioral data,
*  but they have different goals.
*  So neural foundation model is kind of like foundation models in AI,
*  where you want to have a base model from which you can generalize to downstream tasks and
*  application specific domains or to answer particular questions.
*  And so digital twins, parsing the definition that Grace just gave, it is really more focused on
*  using lots and lots of data to make very
*  clear predictions about a particular individual system.
*  And so it's kind of individualized or in the health context, it can be personalized.
*  And you can test hypotheses about the natural system using the digital twin.
*  Right. And the idea is it evolves with the system you're studying.
*  So if you have a digital twin of, let's say a mouse, and then the mouse is in a particular task,
*  you can be running the digital twin model in silico in parallel with the actual experiments.
*  And now you've got the title of Patrick Munoz's talk, closing the loop with virtual neuroscience.
*  So closed loop neuroscience, we've got an in silico ghost or simulation essentially of the
*  actual animal in the experiment. And then you can do very fine grained real-time predictions,
*  modulation. And the idea is that should be a very powerful approach.
*  Yeah. I mean, you can imagine all sorts of things like tracking through the lifetime
*  changes and through development and the lifetime and not necessarily in humans,
*  because that's really longitudinal, but you can do it on a faster time scale with something like.
*  Well, it actually came out during Kai Miller's presentation that he as a
*  functional neurosurgeon would like to have digital twinning in the future.
*  Sure. Yeah. But I just mean the particular idea of tracking over the lifetime.
*  But if he had that in his surgical suite, then he could test things very quickly and then decide
*  whether or not to implement some surgical technique. Exactly. Yeah.
*  That was really a conversation I wasn't expecting from session four, but it was very insightful.
*  Those are the fun things at workshops when something like that surprises you.
*  Yeah. And also, the combination of Chris Rozell and Kai Miller on the same discussion,
*  both are very clinically savvy and taking opposing views for neuromorphic was exciting session four.
*  And when Joe brought up the concept of a hardware lottery in the concepts of Shannon information
*  theory, it kind of reminded me how neurotech certainly also could suffer from the hardware
*  lottery, given how hard it is to get devices approved. And so we're often just stuck with
*  what's approved and not what's necessarily the best. I'm aware of our time and I want to make
*  sure that we talk about that. So what's one of the interesting and maybe surprising things,
*  because there's the paper does so much is that you end up arguing that for a base layer of
*  neural computation, like we talked about before. So what, and you don't have to define it,
*  but what is a base layer roughly of neural computation? And then why do we need one?
*  Why do we need to determine what the base layer is? Well, okay. Well, what I call the base,
*  this is not a term that I coined. It's just I referred to it as the base layer in this paper.
*  But that kind of came out of thinking, I was reading some philosophy, philosophy of computation,
*  what are the different types of computation? How do you do computation in physical systems
*  and dynamical systems? Is a system of ODEs differential equations and you just evolve them
*  forward with Runge-Kutta or whatever your algorithm is, can that do computation? Can
*  continuous dynamics compute? So there's a lot of really interesting questions around computation
*  and brains are a particular kind of physical, dynamical, material, chemical system.
*  So I think just, again, falling into the default concept of the neurocentric framework
*  for understanding brains, is maybe leading us astray. Obviously, throughout biology,
*  cells are super important. So neurons are super important to brains, but also neurons are not
*  the only cells in brains, as we know, there's all sorts of glia, astrocytes, oligodendrocytes,
*  microglia, which have important roles in structural plasticity.
*  Looking beyond, digital computing has gotten us into thinking about computational systems as,
*  okay, there has to be a transistor. There's some unitary element, that's the lowest level thing.
*  And so if you think about a silicon disc with chips that have been burned into it,
*  photolithographic process, all it is, is a material carving in silicon and other types of materials.
*  And so that's the base layer. The transistors in the CPUs that we use in all of our computers
*  and phones right now, that's the base layer of computation for digital computing and on
*  conventional CMOS processes. So is our brains just like that? Are cells like transistors? Is that it?
*  Right. No, cells are binary event action potential generators, right? I think
*  McCulloch and Pitts were right and nothing has changed. And so we should still consider them
*  that, right? No. So McCulloch and Pitts, that was fundamentally wrong, right? It's not a binary
*  signal. It's an event. A spike is an all or none event. And so some people say, oh, okay,
*  so it's a spike timing. It's like, we just need a highly precise, what's the timestamp on that spike
*  versus that spike? And then that'll tell us everything. Well, no, because you don't need an
*  absolute timestamp. You need to know what the role of that one spike is in this dynamical system,
*  because that spike is propagating to downstream neurons. And at some point you hit recurrent
*  connections and it feeds back. And then you go up a layer to the next higher level of cortex or
*  whatnot. Everything is causal dynamical interconnected. So you can't just say, it's a one or a zero.
*  Obviously that inspired von Neumann and it's an amazing insight because that's why we have
*  digital computing technology now, but it's not how brains work. As Walter Freeman pointed out.
*  And as we also heard from Jotar, there's all this dendritic computing that's happening at the
*  dendrites. Right. And so there's just, I think so much more richness that we are now aware of
*  that wasn't available to McCulloch and Pitt. That's true. But now, Grace, you just went down a level
*  physically from the point neuron to dendritic computing, which would make Panjota very happy.
*  But then, but you guys want to go up a level and talk about the role of oscillations in this dynamical
*  coupling. And I also found myself wondering, I don't know how engineers think about oscillation.
*  The other thing is traveling waves that we really didn't talk much about at this workshop.
*  That's true. Which I'm surprised Terry didn't bring up because he likes to talk about traveling
*  wave. Yes. And he actually sees oscillations and traveling waves to be one in the same
*  for many parts. How would they not be? I mean, an oscillation has some spatial.
*  Well, oscillations repeat. You can have a wave that travels that's not being generated by an
*  oscillating generation process. Okay. Yeah, yeah. That's fine. You can separate them in,
*  but that's like having one wave in the ocean, which isn't an odd. Once one wave leaves, the
*  other wave has to, I don't know, they are intertwined in general, but I could see you could just do a one.
*  Right. Space and time are coupled in the brain. Right. And so fast oscillation. I mean, so
*  there's a mathematical formalism called hierarchy theory, which is basically if you have oscillations
*  at a fast frequency, you can only maintain coherence over a small amount of space. If
*  you have oscillations at a slow frequency, you expand the region of space over which you can
*  maintain coherence with that clock, with that slower oscillation. And at least mammalian brains
*  have a really well preserved set of neural oscillations in different parts of the brain
*  at different times that interplay with each other in different ways at base frequencies,
*  which are at these really interesting incommensurate fractions between each other. So it's almost like
*  we need, nature needed to find half a dozen different frequency bands that didn't interfere
*  with each other or minimally interfered with each other. Because then you can have a theta
*  and you can have a gamma and you can nest seven of those gamma cycles and one theta cycle. And
*  then that becomes an interesting packet of coordination. So it's not the spike timing.
*  It doesn't matter that neuron A fired at time t zero within theta cycle, whatever, x. It's not
*  that absolute index of time that matters. It's the fact that, oh, you've got this packet of
*  activity that's carved out by this sequence of gamma oscillations or gamma cycles within this
*  theta cycle and that theta cycle is within this larger set of slower rhythms. And
*  it's hard to ignore these laws almost. So this relationship between space and time,
*  we have these conserved oscillations and they do govern the timing of spikes, the activity of
*  neurons. And so there's this feedback loop that goes up a level to a collective behavior,
*  like an oscillation. And then through apathetic effects or through just other modulations,
*  they entrain and feed back into causal mechanisms at the cellular level.
*  So then I want to ask what the base layer is, what the proposal is for the base layer. But maybe
*  even before that, I could list off the three requirements that you posit for a base layer
*  to be a useful computing layer. And by the way, this is a, I should also say that the proposal
*  is a non-reductionist mechanistic account of neural computation, which is an interesting thing
*  itself. Okay. So the requirements that you state for a base layer, and I'm reading directly from
*  the paper here, is that one, that they encompass a macro scale hierarchical control structure.
*  So over which it implements comparator error and output functions. So that's the control theory
*  aspect, part of it. Two, that to adaptively control access to internal and external information
*  flows generated by physical embodiment and situated embedding in a causal environment.
*  So that's the sort of almost ecological psychology interaction between these continuous
*  flows. And then three, support discrete neuro-dynamical states and adaptive high
*  dimensional state transitions across time scales of neural circuit feedback.
*  And then you list some specific kinds of time scales. And I suppose that links into the reason
*  why oscillations are important. These nested structures of oscillations, the spiking information
*  carried within those oscillations and how they're interacting across different time scales and
*  structures and flows. All right. Mouthful. But-
*  Wow. That's an ambitious framework.
*  It's super ambitious. It is super ambitious. This is a 30 year brain initiative. That's the
*  other thing is reading this paper, it's like, oh, this is like a whole textbook or a whole
*  four special issues in some journal condensed into one thing. I mean, yeah, it's ambitious.
*  Well, I should make clear this document has nothing to do with the brain initiative.
*  Views, perspectives, priorities, plans or any of that.
*  But you come out thinking, oh my God, where do you begin? How do you start and where's
*  the so much to do? Well, I mean, so, okay. I wrote this a
*  couple of years ago and I'm not sure I even remember the three criteria that you just listed.
*  I'm looking at the paragraph now. But this all came out of, again, kind of a frustration and just
*  wondering, well, what if the whole neurocentric paradigm is wrong? Rafa Usta had a review or
*  perspective favor from a number of years ago saying the network centric paradigm is what we-
*  Right. He went from the neuron doctrine saying that's old, didn't work. Now we're in a population
*  doctrine era he was advocating for, which is kind of where the field is right now. Okay,
*  it's all population dynamics and manifold. And so, well, and John Hoffield, just
*  got the Nobel Prize. And so, yeah, there has been movement in that direction. Fundamentally,
*  there's a lot of technological determinism here. The better our tools get, and brain initiative
*  is certainly behind a lot of that, the more neurons are going to record at better fidelity,
*  more throughput, the more you can see. And so that's, we're getting beyond single neurons
*  because we can record millions of them now. But we need to understand what's happening still. And
*  so now the focus is on low dimensional representations, right? But what's a low
*  dimensional representation? Essentially, it's an attractor. It's a small subset of a high
*  dimensional space that's been carved out. And you can say, okay, effectively, this million neurons
*  I'm looking at, the state of the system is somewhere on this like two, three, four-dimensional,
*  maybe four, but a low dimensional system. And you can basically understand it. If you can map
*  the axes, the dimensions of this low dimensional manifold onto task requirements and constraints,
*  then it's like, oh, that's explainable. I know what's happening in this neural system.
*  But then there's questions about, well, okay, the whole brain isn't a single attractor. It's
*  not one giant hot field network. Yeah. I don't know. Some people may disagree, but okay, go ahead.
*  But I'm saying, well, I think there's attractor-like dynamics everywhere, but it's complex and
*  heterogeneous, modular to a degree, and governed transiently, dynamically by lots of things at
*  different levels of organization, including things like oscillations and things like traveling waves.
*  So you have coherent organization at time, coherent organization in space. A lot of it's
*  quasi-hierarchically organized because the flexibility, people will think about
*  natural intelligence and its agility, its flexibility. Your animals are optimizing
*  multiple objectives simultaneously. How do you do that? Well, you do that by flicking on and off
*  different sub networks at different scales, adaptively in the right way. It's like,
*  I need to keep, I'm trying to do three things at once. I want to get food in an hour. I'm trying
*  to wrap up the current sentence I'm speaking. You've got these multiple goals in mind. How do
*  you do that? You need to activate different attractors in different ways in a complimentary
*  pattern to achieve the goals of the organism. So that's where the spatiotemporal organization
*  comes in, but it's governing this heterarchy maybe of attractors or quasi-attractors.
*  So that's where I went to in this paper is thinking about something. I kind of regret that
*  terminology, but I called them tokens or causal tokens. I was just trying to think of how do we
*  think of an attractor knot as this, oh my gosh, this is huge task manifold. The animal goes into
*  a maze. The manifold needs to come up and then it needs to go along the manifold.
*  Yeah. And then all the activity projects onto that manifold. You can figure it all out. And then
*  it's like, if there's a go, no go, then it's like, okay, then the selection vector rotates
*  through it and then boom, the behavior happens. And Dave Cicillo's work and going back to that
*  2013 paper, which I think is a great idea. And so something there, but the interpretation of what
*  that means, what does the selection vector versus the command vector or whatever the other space was
*  there, how do we think about communication subspaces? How do they come on and off adaptively
*  and serve as some goals? So my idea was, you know, causal tokens are kind of like these
*  little quasi attractors and they can exist at different scales and quasi attractor because
*  like, you know, you don't get stuck there. The system doesn't get stuck there. You always need
*  destabilization. If you fall into an equilibrium state and you can't get out of your debt.
*  But as we know, cognition keeps moving. It's always, always moving. So you're always finding
*  little attractors and then being bumped out of them. You know, there's a competitive process,
*  maybe, you know, it's, but it's, it's just trying to think of like, what is the base
*  unit of computation if that's what's happening? So what is the base unit of computation
*  that you're advocating for the base layer? Well, I kind of went back to
*  Heb and Carl Lashley. And I should say this was a great review and perspective put together by
*  Drew Marr and Lynn Nadel from a few years ago. It's cited in the paper where they really make the,
*  they reconceptualize what Heb was talking about. You know, Heb and his student, Carl Lashley,
*  really thought deeply for many decades about what it meant for networks of neurons to be connected
*  to each other. What are they doing? Looking at persistent activity as well, they're self-reinforcing
*  patterns of activity. So basically that's the causal base layer that I was interested in.
*  If you have a supra neuronal group, you know, a group of multiple neurons, and the thing is
*  there's like a loop of reverberant activity going through those synapses within that interconnected
*  loop at some level. And it's self-stabilizing. Like you can like ignite it essentially. And then
*  the connections are such that the non-linearity is all lined up and you get self-reinforcing,
*  self-supporting, self-sustaining activity. That's the basis. That's the base computational unit
*  that I was speculatively putting forward in this paper. And then the nice thing about that is you
*  can sprout loops off of that, right? There's always another connection. You can always
*  reconsolidate those connections in a different way. That's maybe structural plasticity is like,
*  maybe there's a side loop that's sub threshold, but then one thing happens experientially for
*  the animal. And then that connection gets twisted up a little bit. And now the non-linearity is lined
*  up in a different way and the loop expands. And so now you're at a higher scale causal token or
*  whatever I was calling it. This quasi attractor now means something because it's incorporated this
*  new correlation from the environment. And so maybe that's a control signal or control parameter that
*  was updated within the hierarchy or something like that. But it's a self-sustaining bit of activity
*  governed by all the spatial temporal structure that we were talking about with oscillations.
*  S1 It's fun to see you light up like that when you're describing it. You look excited
*  and sounded excited talking about it. S2 I think you reactivated my
*  neuro-dynamical state when I was writing the paper. Yeah.
*  S1 Yeah. So then, all right, we have just a few more minutes. Grace,
*  it looked like you might have wanted to jump in there also or no?
*  Well, I just wonder how any of this could be measured experimentally.
*  S1 Oh, good God. We don't have another two hours or were you planting? Was that a plant question?
*  S2 It's a quick question for Joe because the idea of measuring every synapse came up yesterday.
*  S1 Oh, yes. S2 Well, you could do that. That's very straightforward,
*  assuming you had the right technology, right? But yeah, that's a great question, Grace.
*  Well, you brought it up earlier, Paul, as well. And so, this does tie in directly, right? So,
*  I'm not saying my idea here that I just went through is absolutely right. I mean, it's just
*  where I went is like, this seems like the most likely useful framework for thinking about it.
*  But if this is true, then the actual particular value, the precise synaptic weight of any given
*  synapse is almost immaterial. It doesn't matter. S1 Okay. That's why you're bringing that up.
*  Because I questioned that too. I actually pushed back in that discussion. What did I say? Something
*  about if you just measuring something doesn't give you the theoretical, some blah, blah, blah.
*  I can't remember what I said. But then I got kind of pushed back for saying that. And I was like,
*  oh, I didn't realize that what I was saying was even controversial. But okay, yeah. So,
*  thanks for bringing that up again. S2 Right. Yeah. So, in the paper, we say that,
*  if this hypothesis were true, this kind of like what matters is self-sustaining little clumps of
*  neurons that can expand outward and adaptively, then this is completely antithetical to what we
*  see in AI models based on artificial neural networks, where everything we care about is,
*  when you distribute an AI model or transformer LLM, it's a binary blob full of very precise weights.
*  And then the whole game is to see how far you can quantize those weights down and still preserve
*  the functionality. And so, you can put these things on phones and home computers and all of that.
*  So, everything that matters is the weights. It's all in the weights and nothing else,
*  the biases too. But if this hypothesis is right, then that doesn't matter. And to understand the
*  brain, we don't actually need to go around and measure every synapse because they're wildly
*  fluctuating anyway. It's highly volatile, right? S1 So, people would argue,
*  against that because I've received pushback saying that exact same thing that actually they're
*  largely quite stable. And I guess we won't know until we measure every single synaptic.
*  Well, you have to de-confound the effect of, if you do have like the self-sustaining quasi-attractors,
*  then you're going to have synaptic loops which self-sustain and do maintain like
*  strong correlations over time that persist about relative synaptic weights. You would expect that.
*  But it's not the weights that matter. It's only lining up the right set of non-linearities so
*  that that group fires in the way that it does and interacts with other tokens or other quasi-attractors.
*  S1 Sounds like dynamics was what largely- S1 Dynamics was switching, right?
*  S1 In a hierarchical, hierarchical and heterarchical fashion.
*  S1 Or just heterarchical. I think it encompasses all of it.
*  S1 Guys, I have to go here in a minute. I really, again, this is one of those papers that I'm going
*  to revisit and then feel guilty that I'm not reading every reference in that stack that grows
*  ever so larger of what we're supposed to be reading all the time. But it is just so rich.
*  And I'm glad to point people to it. Well, congrats again on running a great workshop.
*  And I think a successful workshop. And I really hope that you guys get some rest. Get some rest.
*  And I know you have to sort of take in everything now and then reflect. But hopefully that's a
*  little bit more relaxing a process and then you can take a little vacation.
*  S1 Yes. And thank you so much, Paul, for coming to the various pre-coordination meetings. I mean,
*  I was so impressed at how hard everyone worked. We got multiple abstracts, multiple versions of
*  presentations. It was amazing that we had everybody share their files on the NIH box. And you could see
*  how people were changing their presentations in response to each other. And it was just thank you
*  so much to you and everyone else who really made this a great workshop.
*  S1 Oh, that's great.
*  S2 Thanks for having us.
*  S1 Yeah. Thank you.

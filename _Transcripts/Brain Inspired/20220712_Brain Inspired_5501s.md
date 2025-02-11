---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5501s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 830
Video Rating: None
---

# BI 141 Carina Curto: From Structure to Dynamics
**Brain Inspired:** [July 12, 2022](https://www.youtube.com/watch?v=Es_FvEyRe4E)
*  Physics has shown us that doing mathematical analyses on simple models is a very, very
*  fruitful game and I strongly felt and continue to believe that it's a fruitful game to play
*  in neuroscience as well.
*  The perspective is that somehow you have modules, you know, sub-networks in the brain that do
*  things, right?
*  And you want to understand how they can be embedded in the larger networks so that they
*  can still do their thing and not be kind of destroyed in terms of the activity they produce
*  by the way that they're embedded.
*  Neural networks fundamentally are high dimensional nonlinear dynamical systems.
*  And high dimensional nonlinear dynamical systems are a nightmare mathematically.
*  It's really hard.
*  This is Brain Inspired.
*  Hey everyone, it's Paul.
*  Often on this podcast we talk about how deep learning models might be used to help explain
*  our brain processes and intelligence.
*  But a continuing obstacle is that we're using one complex system to study another.
*  We don't yet have a great grasp on how artificial neural networks are doing their thing, so
*  it's an ongoing question how we'll use them to explain how wet neural networks, our brains,
*  do their thing.
*  Karina Kurto is a neuro-theoretical mathematician at Penn State University.
*  I just made that phrase up, but what I mean is that she applies her background skills
*  in mathematical physics to study theoretical neuroscience.
*  One of the mathematical tools she uses is topology, which in neuroscience is roughly
*  the study of the theoretical geometric shapes we use to say something about the possible
*  range of activity of a population of neurons.
*  So we've discussed the dynamical systems approach multiple times on the podcast, things
*  like how neural population activity can often be reduced in dimension and traced out over
*  time on some lower dimensional structure, like a manifold or a tractor.
*  And that manifold is a way to think about the shape of cognition, so to speak.
*  Topology is the study of those possible manifold-like structures and the rules by which neural activity
*  is allowed to unfold.
*  It's a pretty new tool in neuroscience, so we discuss it during this episode.
*  Another mathematical tool Karina uses are called linear threshold networks, and in her
*  case often a special case called combinatorial linear threshold networks.
*  I'm sorry that's jargony, but these are highly abstracted neural network models that
*  importantly are mathematically tractable, meaning you can use proofs and so on to conclusively
*  state how different architectures of the model lead to different dynamic features of the
*  activity that the model will produce.
*  You can look at a structure and know what dynamics will result.
*  An age-old challenge in neuroscience and now deep learning, I suppose, is trying to connect
*  function with structure.
*  So it's possible these CLTN networks are a step toward bridging that gap by connecting
*  structure and dynamics.
*  So we talk about topology, these CLTNs, which Karina always likes to stress is work that
*  she's done with Katie Morrison and wider topics like the differences between different
*  kinds of modeling approaches, the reason why people with physics backgrounds are specially
*  relevant right now in neuroscience, how we can all remember Jenny's phone number, eight,
*  six, seven, five, through, okay, I'll stop.
*  Show notes are at braininspired.co.uk slash podcast slash 141.
*  On the website you can also check out my Neuro AI online course about many of the topics
*  you hear on the podcast or decide to throw me a few bucks a month through Patreon with
*  various bells and whistles.
*  Both of those options are of immense help to me.
*  Learn more at braininspired.co.
*  Thanks to everyone who supports the podcast.
*  All right, here's Karina.
*  Karina, have you always been interested and enjoyed math?
*  Math?
*  Yes, I think so.
*  Although if you had asked me when I was younger, like in high school or even when I started
*  college, if I would become a mathematician, I would have said, absolutely not, because
*  that's what my father did.
*  And so it wasn't cool.
*  So I was going to be really different and become a physicist.
*  That was my plan originally.
*  Right.
*  Yeah, we were just talking about your background in mathematical string theory, which is what
*  you got your PhD in, you were telling me.
*  A long time ago, yes, in 2005.
*  And then you had a decision to make to, what was the decision?
*  You didn't tell me what the decision to make was.
*  Yeah, I actually made the decision before I finished my PhD.
*  So about halfway through grad school.
*  So I went to grad school, first of all, completely focused on this idea of becoming a string
*  theorist.
*  So I had been an undergraduate at Harvard in physics, but I had started taking lots
*  of pure math classes at the time.
*  The environment at Harvard was very surreal in a way, because doing pure math was really
*  considered very cool.
*  And so I got increasingly interested.
*  And also because I wanted to be a theoretical physicist, it made sense to take as much math
*  as possible.
*  And then I ended up going to grad school in math, but to do mathematical string theory
*  at Duke and was very, very much committed to it.
*  And then a few years in, I just realized my heart wasn't in it in a very serious way.
*  I loved the mathematics.
*  I still loved the fundamental ideas of string theory.
*  I do think it's a lovely theory in many ways, and someone should keep pursuing it.
*  But at that point, it was sort of like, this was in the early 2000s.
*  It felt like to make a significant advance, I felt out of reach for a variety of reasons.
*  Anyway, so the point is I became dissatisfied, disillusioned, depressed.
*  I don't know what you want to call it.
*  I had a little bit of a quarter life crisis, I guess, and just kind of didn't feel like
*  this was right for my career.
*  I still wanted to finish the PhD in string theory, which I did in mathematical string
*  theory.
*  So I finished my PhD, but I started looking for what am I going to do next?
*  So I very much took on this attitude, OK, I'm going to do this for my PhD.
*  I'm going to write a nice thesis.
*  I'm going to publish it.
*  I did all that.
*  But then I'm going to switch fields.
*  And I made the decision that I'm going to switch fields, like, probably in the middle
*  of my third year.
*  And then just kept the grit to stick it out.
*  And then just kept the grit to stick it out.
*  And I also had to figure out what I'm going to switch to.
*  So I needed a little bit of time.
*  Well, I want to ask about that too.
*  Did you get a, and I told you so, from your mathematician father as soon as, or did you
*  not confide in him that it was like the mathematics?
*  I kind of kept this all secret.
*  Yeah, I was kind of looking for something else.
*  I think in my fourth year, the beginning of my fourth year of grad school, I actually
*  sat in like on an economics course because I was like, oh, maybe economics will be interesting.
*  And that was intolerable because at the level of economics that I had, I needed to sit in
*  kind of on an intro undergrad course.
*  But the intro undergrad course like spent the entire lecture, you know, talking about
*  vector calculus or, you know, just very, you know, math that I was teaching as a grad
*  student.
*  And so it was, you know, there wasn't a good level.
*  There was no like, you know, there's like, you know, there's always field X for dummies,
*  right?
*  But there also needs to be field X for people who know a lot of math and don't want the
*  review.
*  Yeah.
*  But neuroscience is not that field.
*  No, neuroscience is not that field.
*  But I was just saying why the economics class didn't work for me.
*  Okay.
*  So that was just yeah, in some ways, maybe sitting in on a neuroscience class was much
*  more appealing because there was no math.
*  So I was bored with the math.
*  It was just like it was all biology.
*  It hurts.
*  It hurts.
*  Right.
*  Well, I mean, in the undergrad, no, I'm, I'll be there's a lot of math in neuroscience,
*  actually.
*  I mean, I don't mean to otherwise I wouldn't I wouldn't be here.
*  The intro level neuroscience courses at Duke, right?
*  So I sat in on on an intro level neuroscience course and loved it.
*  It was totally different.
*  And in a way, it was all new because I had avoided biology since ninth grade in high
*  school collecting.
*  Right.
*  Exactly.
*  But did you when you were sitting in that course, then with your heavy math and physics
*  background, did you just immediately see an opportunity to enter the field because all
*  these people, they they don't know what they're talking about.
*  No, no. I mean, it was that was not my feeling at all.
*  My feeling was like, wow, this is so cool.
*  You know, and I didn't you know, it just it was more just like entering a new land,
*  you know, and just see I was like a tourist.
*  Right. And I was like, wow, all these beautiful all this beautiful structure.
*  All you know, who doesn't want to know how the brain works?
*  It just seemed very exciting.
*  And I didn't I didn't, you know, see much math in it.
*  I mean, I think maybe the Hodgkin-Huxley equations were like mentioned in passing, you
*  know, like with the with a hurrah.
*  We did it. Hodgkin-Huxley.
*  We solved the brain. Right.
*  Exactly.
*  But no, I just because I really didn't know anything about biology.
*  I mean, I was very, very ignorant.
*  And so to me, it was like learning biology for the first time at age 25, you know, and
*  I recommend it because by the time you're 25, you really appreciate it.
*  It's like, wow, all these cool things.
*  And you've lived long enough that you know you have a brain.
*  Right. And it's kind of fun to to learn about how it works.
*  But all the things, you know, the ion channel channels, the synapses, the all the various
*  structures, you know, it was blown away.
*  Just simple things, you know, that you might everybody in neuroscience knows from when
*  they were babies.
*  Right. Like I it was all new to me.
*  I didn't see necessarily potential for myself in there, but it was just kind of fun,
*  much more fun than the economics class.
*  But then then it just happened that Duke was running like a computational or theoretical
*  neuroscience seminar series.
*  And so I went I went to some of the seminars and I distinctly remember Larry Abbott
*  coming down and giving a talk about vision.
*  But he very much brought, you know, like he does in so many of his talks, he very much
*  brings to the forefront the perspective, his perspective as a physicist.
*  It was such a lovely talk.
*  And it was like it was the first time I had ever seen anything like that.
*  It was the first time I had seen a physicist, someone who's, you know, obviously a
*  theoretical physicist by background talking about neuroscience.
*  And that combination made me see it, you know, made me see myself as being able to do
*  this. I kind of started paying more attention.
*  And then this crazy thing happened.
*  There was a kind of a young professor at Rutgers and Ken Harris.
*  He's still around. He's a very prominent neuroscientist in London now at UCL.
*  So young anymore. Not so young anymore.
*  Neither am I.
*  Yeah, none of us are young anymore.
*  But but at the time he had just I think he had had a very successful postdoc in the
*  Boczaki lab and he was starting up his own lab at Rutgers and he was recruiting.
*  He was trying to recruit postdocs and grad students.
*  And he himself had a background in math and physics and had actually started grad
*  school to do string theory.
*  Oh, OK. Yeah.
*  It's a circle. Right.
*  And so I think that's why he gave me a chance.
*  But he started spamming math departments, like literally sent email spam to math
*  departments saying, by the way, I'm starting this lab if you're you know, if you have
*  strong quantitative skills and are interested in neuroscience, you know, get in
*  touch. You know, at the time I had just gotten married.
*  Actually, my new husband at the time was also kind of having Vladimir Itzkov was also
*  having a little bit of a crisis.
*  He was doing differential geometry as a postdoc and had also kind of lost interest in
*  the problems that he was working on.
*  And and together we sort of answered the call and and wrote to Ken.
*  Anyway, he ended up hiring us both.
*  And he ended up.
*  But, you know, the summer before my fifth year of grad school, he had promised me a
*  postdoc position for after I graduated and I accepted it before I started my last
*  year. And that was wonderful.
*  It was amazing because suddenly I had this really serious opportunity to learn some
*  neuroscience and to do it in a lab that was being run by someone who, you know,
*  understood my background, right, someone who really had had kind of a similar
*  background himself.
*  Yeah. So I kind of I committed to that postdoc and then I started my fifth year and I
*  still hadn't still hadn't told anybody.
*  And I remember having this conversation with my advisor where he was like, oh, so
*  it looks like you're going to graduate this year.
*  It's time to start thinking about jobs.
*  It's like in September of 2004.
*  And I was like, oh, I already have a job.
*  So that's when it was really weird.
*  I felt I felt like I was confessing to cheating on him or something with this other
*  field. But yes, I I told him that I had already gotten the job and that I was going to
*  go to a neuroscience lab.
*  And I think he was very surprised, but ultimately very supportive.
*  Yeah. And then I was made it easy because I didn't apply for jobs.
*  I didn't have to go through that stress of going on the job market, finishing grad
*  school and so on. And so I just focused on writing up my thesis and learning as much
*  neuroscience as I could to get ready for my new postdoc.
*  And, you know, kind of came in to hit the ground running and went from there.
*  So that was that was my that was a very long version of my decision.
*  I switched. But there's a lot to chew on there.
*  But and we don't have to persevere on this very long.
*  First of all, I wonder how many people were affected by Larry Abbott specifically in
*  this kind of regard, because I don't know if you have the same observation or
*  perception, but that it just seems like the physics background world has infiltrated
*  neuroscience over the past 15, maybe 20 years.
*  I don't know. A is do you think that that's true?
*  But B, you know, the the physics mindset sort of lends itself to a lot of what at
*  least these days is studied in computational neuroscience anyway.
*  But then thinking about I don't know if we want to talk about relative to string
*  theory in particular, but just maybe physics writ large.
*  Do you see the complexity of studying something like the brain as also naturally
*  lending itself to the physics kind of background and mindset?
*  Or because string theory to me, it seems much more like, you know, reductionist
*  individual particles and equations that are that don't necessarily feedback on each
*  other, which is a very different story relative to something as, quote unquote,
*  complex, like a complex system like the brain.
*  I'm wondering if well, I guess just your thoughts on that.
*  Yeah, so so first of all, I think a lot of I mean, I absolutely think it's true that
*  physics has had an enormous physicists have had an enormous influence on
*  theoretical neuroscience.
*  And, you know, I would say maybe half of the theoretical neuroscience community is
*  people with physics backgrounds, maybe more than half.
*  It's hard to tell. Part of that is because neuroscience was not its own.
*  You know, there weren't neuroscience departments, you know, in so many
*  universities back back 20 years ago.
*  Right. Right. Everyone had to come from somewhere.
*  And so I think I mean, I think on some level, neuroscience itself is a little
*  bit like a land of immigrants.
*  You know, I think people in neuroscience come from all kinds of backgrounds,
*  whether it's physics or math or computer science or engineering, or on the other
*  end, psychology, you know, sometimes philosophy, sometimes molecular biology.
*  So I think there's a there's a huge spread of backgrounds in neuroscience period,
*  you know, not even I'm not even just thinking about the more theoretical or
*  mathy. And on the other hand, I think, you know, you might say, well, why are so
*  many physicists? There are other quantitative fields.
*  There's math and economics, right?
*  Why are there more physicists than there are mathematicians or economists?
*  And I think what's special about the physics training, it is really a
*  scientific training fundamentally.
*  I mean, physics is a science that it does deal with, you know, the real world and
*  trying to understand rules for how the world works.
*  But it's also of all the sciences, I think it's safe to say it's it's the most
*  mathematically sophisticated. And so every physics student learns a lot of math,
*  every physics student, you know, no matter what kind of physics they're doing,
*  there's there's just a huge amount of mathematics that's that's in the training.
*  And so physics students end up learning a lot of science integrated together
*  with mathematics. So it's like naturally integrated.
*  And I think that's the preparation that is so useful for something like
*  computational neuroscience. It's not, you know, so much the the physics content
*  per se or the math content per se.
*  But it's somehow the that integrated approach is like physics is just naturally
*  this field that is developed in a way that there's this integrated approach to
*  science and mathematics, where every time there's a physical phenomena you want to
*  understand, first thing you do is start trying to write down some equations.
*  And this is sort of the beautiful thing about it.
*  Right. So there's natural phenomena in the world.
*  There are equations you can write down, and this includes complex systems.
*  That idea, right, that you can take some messy,
*  you know, real world situation, maybe idealize it a little bit or a lot
*  and then write down some mathematical equations.
*  And then you're going to do some math and you're going to analyze those equations.
*  Maybe even see how the behavior depends on various parameters in the equations,
*  you know, push and explore scenarios that are not exactly like the one that you're
*  initially trying to describe, but you're looking at a family of problems.
*  That whole game, right, where you take something about the messy real world,
*  turn it into equations, play with the equations, you know, study them,
*  really understand them and then feedback into some insight
*  about what's happening with the original physical phenomena.
*  I think that's the training that a physicist gets that is extremely useful.
*  The other thing that helps is that the physics job market sucks
*  if you want to be an actual physicist.
*  That wasn't really the job market that I was a part of.
*  I was sort of more on a math track, which which is a little better, actually.
*  But that combination, I think, of very good training to go elsewhere,
*  but like a very bad market to stay in, you know, precisely physics,
*  I think has led to this proliferation.
*  It's almost like, you know, just to use these analogies, right,
*  of land of immigrants, it's almost like physics is like the Soviet Union.
*  Right. It was like very good, well-trained people, but like no jobs for them.
*  And neuroscience is like America, just welcoming,
*  you know, people from all backgrounds.
*  And anyway, I don't want to say much more.
*  No, no, this is not the moment.
*  This is not the moment to make that kind of analogy.
*  But but anyway, I think there's there's some something to that.
*  So the word beauty is often invoked by physicists and by mathematicians.
*  And in 2013, you wrote a very short piece.
*  And I'll read the title.
*  A major obstacle impeding progress in brain science is the lack of beautiful models.
*  And after our brief conversation here, I realize a someone of your background
*  who got went into, let's say economics or something like that,
*  might just replace the phrase brain science with whatever field they go into.
*  Right. So but so I mean, I guess you've kind of covered this already a little bit,
*  but maybe you can restate.
*  So that was 2013.
*  Has that changed or has your thought about that statement
*  and the very brief piece, which I recommend and I'll link to it,
*  has it evolved as you're thinking about it evolved?
*  Do you think it's changed in neuroscience?
*  And then I just want to talk about what an ugly model is and what a beautiful model is.
*  Sure. So let me just tell you the context of that piece.
*  So this was in the context of the Obama brain initiative.
*  So back in like 2012 or whatever, there was this developing.
*  It hadn't really started yet.
*  This brain initiative was put forward by the Obama administration.
*  It was being led by Terrence and Oski and and others.
*  And they had a workshop,
*  just like an early workshop where they kind of gathered people
*  from different corners of neuroscience to discuss
*  what we were going to do in this brain initiative.
*  And so at the time, I was kind of a young assistant professor and
*  but had already had a little bit of work that I'd already done
*  in computational neuroscience or theoretical neuroscience.
*  And so, you know, along with just like a handful of other mathematicians,
*  I was invited to be a part of this.
*  But it was really a big group of people.
*  It was, you know, maybe maybe over 100 people.
*  And all of the participants were asked to write a one page
*  white paper with that question.
*  Like, what do you think is the biggest obstacle?
*  Advancing progress. Right.
*  So so everyone wrote a one page paper.
*  So I decided so that so I like I just wrote that in one day.
*  I like had to submit it.
*  And I just thought, well, you know, I'm going to take a very mathy
*  perspective here. And this is this is what I think is something to pay attention to.
*  I kind of knew nobody else would highlight the same thing.
*  So so that's where it came from.
*  And when I met by beautiful models, really was
*  this idea that I was sort of describing from from physics before is
*  models that you can, you know, that are abstractions in some sense
*  or dealing with a simplified version of the of the real life situation,
*  of the real life phenomenon, but are kind of simple enough
*  that you can analyze them mathematically and get some traction out of that.
*  But rich enough that they really do capture
*  something fundamental about the phenomenon so that when you do some
*  some mathematical analysis, you actually can gain some insight
*  into the original scientific phenomenon.
*  So, you know, the examples kind of that I had in my head
*  and that I referred to in that white paper were things like the Hopfield model, which
*  for neuroscience was, you know, in in the 80s,
*  kind of led to a bunch of physicists getting involved in the field.
*  And and trying to to see if they could study recurrent networks
*  and and brain dynamics and so on, using this kind of simple model.
*  And the advantage of it is really that you can do some math.
*  Right. So it's like it's not so simple that any mathematical result is obvious.
*  So the idea is you do have some richness to the model.
*  And so if you analyze it mathematically, you might discover something new
*  that wasn't obvious.
*  It wasn't, you know, an ingredient that you put in by hand.
*  And but somehow it's a it's a property that emerges
*  from the properties that you do put in by hand.
*  And so that, you know, as a way of really trying to understand how
*  various scientific properties or scientific phenomena interact
*  and how some depend on others and and so on, I think you can.
*  It's a very it's a very fruitful game.
*  I think, you know, physics has shown us that
*  doing mathematical analyses on simple models is a very, very fruitful game.
*  And I and I strongly felt and continue to believe
*  that it's a fruitful game to play in neuroscience as well.
*  But neuroscience is developing in a little bit in a different era.
*  So unlike, you know, most of theoretical physics,
*  neuroscience is developing in an age when we have, you know, powerful computers.
*  And so there's this other pathway as well
*  that you can take with modeling, whereas that now, you know.
*  Is this the ugly pathway?
*  Well, I believe it's a little bit of a because I
*  I don't want to be. Yeah.
*  I mean, I want to be careful.
*  I want to be careful.
*  Well, ugly in the mathematical sense, not in the real world sense.
*  Right. So or, you know, something like that. Yeah.
*  But, you know, the so in computational neuroscience,
*  the first kind of models, right?
*  Well, not the first kind of models, but there's sort of like these toy
*  models that you can that are kind of simplistic. Right.
*  And I don't know that you necessarily need to even do mathematical analyses
*  and prove theorems about them.
*  But then you can simulate them and get results.
*  And then you can kind of build up and, you know, there's that whole simulation streak.
*  But but then now there's all these deep learning models.
*  So that's really what I wanted to ask you about is the is
*  are these large deep learning models,
*  transformers, large language models, convolutional neural networks,
*  even like, you know, with recurrents, are those ugly models
*  in the technical sense?
*  So I wasn't thinking about.
*  Yeah, no, I know.
*  I mean, so by the way, I mean, beautiful and ugly are obviously subjective terms.
*  And I meant to use them as subjective terms as well.
*  You know, those were words chosen because because they aren't particularly objective.
*  You know, and I didn't want to sort of overplay my opinion here.
*  But what I was thinking of when I wrote that in 2013 was not so much deep learning,
*  which is not as sensational at the time.
*  You know, it's hard to believe, but 10 years ago, it was really not as prominent.
*  And what you know, I was I was more thinking about very biophysically detailed models.
*  So there's another sort of realm of modeling.
*  And this is actually kind of was, you know, a scene like in the Blue Brain Project in Europe.
*  And it's kind of it's kind of what spurred the Obama Brain Initiative was sort of a reaction
*  to a huge investment in that kind of project.
*  That failure. Well, it hadn't failed yet.
*  Right. But I think there was an idea to have an American response, right.
*  And to do a big, you know, brain investment ourselves, but with a different flavor,
*  very different flavor. And I'm happy for that, actually, for how it played out.
*  I think it played out much better.
*  But anyway, so at the time, that was kind of the other extreme.
*  So it wasn't so much deep learning, which deep learning is also an abstraction.
*  It's also in some sense a very well, we can talk about that later.
*  But it's it's not biophysically detailed deep learning networks.
*  I was thinking more about the models where it's like you take a bunch of Hodgkin Huxley
*  neurons, except you add all these dendrites and all these different compartments.
*  So these multi compartment models for single neurons,
*  the first single neuron may already have 50 or 100 parameters.
*  And then you put many of them together
*  into this large scale network.
*  And what happens in a model like that is that in some sense,
*  you have parameters that are interpretable.
*  You can say, oh, this G sub i is the value of the conductance of this particular
*  ion channel on this particular neuron.
*  So you have all these different parameters,
*  and you have you can you can put together lots and lots of neurons
*  in a network and add different kinds of inhibitory cells.
*  And so there's there's a lot of richness that you can build in.
*  I would say it's built in with a lot of guesswork because
*  ranges of values, parameter ranges of values.
*  And and it's the kind of thing that a hundred years ago
*  nobody would have done because it would have been impossible.
*  Computationally. Right.
*  You couldn't run a simulation.
*  And that's the only thing you can do with a model like that is run a simulation.
*  Right. And so, you know, it's not a bad thing that we can run simulations.
*  I do simulations all the time.
*  I think they're very important.
*  They're a very important tool.
*  But in some sense, because we have this extraordinary ability
*  to simulate large sets of differential equations on computer,
*  we have this other choice in modeling. Right.
*  We have this other choice in how to develop computational theories
*  that wasn't available when physics was being developed.
*  You know, or in sort of like theoretical physics was really
*  cementing itself and establishing itself as a field.
*  They didn't have this.
*  I actually have have brought up the thought.
*  I've come up with this thought experiment before where I was like,
*  what would have happened if back in the beginning of the 20th century,
*  before it was even clearly established that atoms existed?
*  Right. Way back then, when people were sort of laying the foundations
*  for things like statistical mechanics, what would have happened
*  if we had had the ability to measure individual atoms
*  in a gas and track them with position and velocity over time?
*  And, you know, and have this huge database where it's like,
*  OK, here's my gas and here's like 100 million atoms.
*  And, you know, here I'm like, I'm tracking all their positions
*  and velocities over time and seeing how they interact.
*  And now let me build like this giant deep learning model
*  or, you know, detailed biophysical model, physical model,
*  not biophysical, physical model. Right. Right.
*  Like, imagine that we could have done that,
*  we could have had like gasomics, you know, and just done this
*  like large scale like gas modeling.
*  Would that have really been better than the way thermodynamics
*  and statistical mechanics developed?
*  You know, obviously it's a different problem.
*  And somehow physicists got lucky that they were able to get
*  so much mileage out of simple mathematical models.
*  But I do think that that sort of not having the that ability
*  to do the large scale computational modeling
*  allowed a very different style of modeling to develop.
*  Oh, now you're calling deep deep learning practitioners lazy.
*  I see. No, no, no, no, no, no.
*  I'm saying I'm saying no, I'm the opposite.
*  Right. Like in some sense, it's like that's that's the hard work.
*  Right. And it's like, I think physicists were forced to take shortcuts
*  and, you know, dramatically reduce dimension and idealize abstract
*  and idealize and abstract.
*  I think they were for it.
*  What I'm saying is for them, it wasn't a choice.
*  They were forced to package things in ways that then they could sort of
*  do mathematical computations with pen and paper,
*  because that was the tool that they had.
*  They didn't have, you know, supercomputers that could run huge simulations.
*  And so I think that, yeah, there wasn't really a choice there.
*  Now we have a choice.
*  And so and I in, you know, as with most science,
*  I think when there are choices of different ways to do things,
*  you know, I'm happy for for all the choices to be, you know,
*  like there's a community, right, so different people can make different choices
*  and we can explore problems in different ways.
*  I mean, you know, I'm not against those choices.
*  You know, I just but I but I think that there's a danger of going too far
*  in the direction of like the large scale computational modeling and then forgetting
*  that there's also a lot of mileage that potentially could be had
*  by simpler models that can be analyzed mathematically.
*  And that's what the sort of the beautiful models
*  concept that I kind of wanted to promote at the time.
*  And still, you know, I still think that that's it's just a different pathway
*  of trying to do theory.
*  And and I think that it can coexist alongside the other ones.
*  And, you know, I just don't want that one to be forgotten.
*  And that's the one that that I, you know, that I feel like I can do well.
*  And, you know, and many people with with physics and math backgrounds can do.
*  And I just I I I was hoping, you know, with the brain initiative,
*  that the brain initiative would carve a space for that.
*  That was kind of my hope.
*  And and I think it has actually.
*  So and I think that I think there are there are a lot of people who who are
*  continuing. I mean, a lot of people with physics training, especially
*  because that's what they're trained to do, who are continuing to do that.
*  And in addition to the large scale modeling is, I think the sometimes
*  the same person is doing both. Right. So and that's that's interdisciplinary.
*  Yeah, it's interdisciplinary. Exactly.
*  My my so my summary of what we just talked about is
*  you got the beautiful model community, which you're a part of the ugly model
*  community and the lazy coming up model community.
*  That's that's my take home.
*  Is that no, I know.
*  Yeah, I don't want to be on record
*  calling anyone the ugly model community or the lazy.
*  And then there's the Russians and the United.
*  Yeah, we don't have to know.
*  I'm really getting myself in trouble here.
*  No, no, I think there are different approaches.
*  Yes. Deep learning is another approach that has emerged after
*  that has emerged as being very prominent in neuroscience.
*  I think after I wrote that.
*  Yeah, that's kind of going in a different direction, because on the one hand,
*  they are also very abstract models.
*  Deep learning networks are very simple.
*  It's really just like composition of simple functions
*  is what a deep network is doing.
*  But it has a lot of parameters.
*  So it's kind of the simple model in terms of the framework,
*  but really complex in terms of parameters.
*  And so, yeah, I don't know.
*  I don't know if it's beautiful or ugly.
*  Yeah, we can we can drop that.
*  I just wanted to give you a little bit about it.
*  So we'll kind of come back to that.
*  Maybe when we talk about the combinatorial linear threshold models,
*  which is part of what you're working on before we get there, though,
*  another line of, you know, mathematical analysis that applies
*  or is beginning to apply more to neuroscience is topology.
*  And but the way that I have been talking about, you know,
*  like your math and physics background, right?
*  It's not as if math and physics freezes.
*  And we figured all math out and we figured all the physics out.
*  And now we can just start applying them because they're both developing also.
*  And I know that topology is a developing mathematical field
*  as we speak still, right?
*  But you have argued that it it's useful as an application
*  to neuroscience as well.
*  So what is topology?
*  And it might be useful to just relate it to the dynamical systems theory,
*  you know, compare, contrast, essentially, since that's another like very popular
*  theoretical approach to the geometry of thought and neural activity, et cetera.
*  Yeah. So, I mean, topology is basically
*  geometry without distances.
*  So where you're really thinking more about relationships
*  and and and what properties of an object are preserved as you can deform it without,
*  you know, just to go back into the cliches without tearing holes into it
*  and so on. And but, you know, so, yes, as a field,
*  topology is still developing.
*  I mean, there's a topology community in mathematics.
*  But I would say that the the so there's sort of developing in two different ways.
*  So there's a traditional topology community.
*  There's like low dimensional topology that people do.
*  If you if you heard about the plunker a conjecture being proven,
*  I think 15 years ago now, that was a topology result.
*  So there's definitely, you know, a lot of, you know, a lot of open questions.
*  There's a lot of active work in topology in math.
*  So that's sort of pure topology.
*  But there's also an applied topology community that has emerged recently.
*  So applied topology is kind of a spin off branch of topology
*  that deals with applications.
*  But but in particular, it's really kind of computational topology in a sense.
*  So it deals with finding ways to
*  compute topological properties of data sets,
*  point cloud data, for instance,
*  but also can be applied to neuroscience data. And so
*  strictly speaking, the the topological ideas
*  that are in applied topology or in this sort of newer computational topology
*  area are like 100 years old.
*  You know, the basic questions like you want to you want to look at features
*  of geometric objects that are kind of independent of precise distances.
*  So if you imagine a torus, probably know what a torus is.
*  It's like a bagel, but hollow.
*  And so you have, you know, you can you can loop string around
*  two different holes that can't be pulled shut.
*  So algebraic topology is
*  a field that.
*  Try that has techniques to compute these properties, right?
*  So you can assign to various geometric spaces,
*  properties such as these sort of numbers of holes in different dimensions.
*  It's like a sphere, right?
*  It has like a two dimensional hole that it bounds,
*  which is different from kind of a disc with a puncture inside,
*  which would have kind of a one dimensional hole that it bounds.
*  And so there are these topological invariants that have been defined,
*  I guess, at 100 years ago to quantify these sort of qualitative features
*  in a way, sort of looking at qualitative features of geometric objects,
*  but quantifying them so you can count the number of holes or you can count,
*  you know, what are called Betty numbers and so on.
*  But when it comes so so, you know, these are old ideas.
*  They've been they've been used in string theory, by the way.
*  So string theorists definitely
*  the Calabi outspaces, which I studied as a PhD student,
*  are definitely studied topologically as well.
*  So, you know, topology has been used in other areas of physics already.
*  That's so it's, you know, in some sense, applied topology isn't new,
*  but computational topology, I would say, is relatively new.
*  And so the big breakthrough that was made,
*  you know, starting around 20, 25 years ago
*  is when this field kind of started and it's really taken off
*  in the last 10 or 15 years,
*  was to develop, you know,
*  with solid mathematical foundations, algorithms
*  that would compute these topological properties for
*  geometric objects that were defined via data.
*  Right. So if you have a bunch of points now, like you no longer have
*  kind of this clean mathematical description, say of the Taurus,
*  but you've sampled a bunch of points and maybe they're in this high
*  dimensional space and you want to know, oh, does that
*  data set have the form of a Taurus?
*  How would you figure that out?
*  I mean, on some level, it is just a bunch of points.
*  So literally speaking, the topology of the data set is pretty trivial.
*  It's just a bunch of points.
*  But if you think that, oh, these points are sampled from some underlying manifold
*  and that manifold has a shape to it and has topological features,
*  can you in some way use
*  that data set to estimate or to get a handle on
*  what those topological features are?
*  And the answer is yes, you can.
*  And you can do it by using kind of really
*  basic techniques in algebraic topology, but automating it,
*  you know, with the automating these computations.
*  Yes. Right. And so that was the big breakthrough is to sort of the old ideas.
*  But with a new perspective, applying them to data sets,
*  discrete data sets, right, and then developing algorithms to automate them
*  and proving theorems that tell us that the approximations that we make
*  in these algorithms are actually reasonable and will give us the right answer.
*  So there are different ways in which we have to kind of cheat
*  when we implement these algorithms.
*  And one of the important things that needed mathematical justification
*  was that in some, you know, in some limit, you really are approximating
*  the right answer.
*  And so those foundations were
*  were laid down, you know, still being worked on in various variations.
*  But the basic ones were laid down by a bunch of topologists
*  who started working on this.
*  So people who really were coming from that pure topology community
*  and decided to start working on applied topology.
*  I think they had DARPA support early on.
*  There were some early applications to robotics that excited
*  various government agencies.
*  And, you know, and then and now I think it's it's completely
*  taken off and is infiltrated in many different communities, including neuroscience.
*  How so in neuroscience?
*  What is it? How does topology apply to brain data, et cetera?
*  So, I mean, I think in neuroscience, it is still
*  much more at the beginning.
*  But on one level.
*  So I actually I wrote an I wrote an article about this maybe back in 2017,
*  which is what can topology tell us about the neural code?
*  So high level. I mean, on some OK.
*  So on some level, and this is one of one of the things I articulated
*  in that article, you know, neuroscience produces lots of data.
*  Right. So just in the sense that topological data analysis is another lens
*  for analyzing data, for trying to do dimensional reduction,
*  for looking at features of data sets and so on.
*  You know, there's kind of an obvious hope that it might be applicable
*  just by the nature of having large scale data.
*  But there are, I think, even more compelling reasons to look for topology,
*  which is that I think that there are there's some evidence, right,
*  that there are areas of the brain that are really encoding topological features
*  of stimuli as opposed to being so focused on the on the metric properties.
*  And so one of the places where,
*  you know, sort of the early places where we found that there was a really
*  natural application of ideas from topology
*  was looking at something like hippocampal place cells and place fields.
*  So I'm just thinking about really the classic setup where you have,
*  you know, a rat roaming around some open field environment,
*  recording place cells in CA1 or CA3 of the hippocampus.
*  And, you know, you have these individual neurons that appear to be acting
*  as sensors for localized regions of the environment.
*  So you can think of the place fields are like these oval like regions,
*  hot spots where when the animal crosses through one of those regions,
*  the neuron associated to that region starts firing a lot.
*  But these regions are overlapping.
*  So you have, you know, many neurons, right.
*  And every neuron has its own place field.
*  And you can think of, you know, people think of the of the place
*  fields as covering the entire environment that the animal is in.
*  And thus we have a cognitive map to navigate an environment like a cognitive map.
*  Right. But interestingly, right, the cognitive map,
*  if you think about the activity, the neural activity,
*  itself, it doesn't necessarily encode the map itself.
*  Right. So you have this.
*  How do I say this?
*  The place field is something the experimenter,
*  the experimentalist computes.
*  So you do it by correlating positions to the firing of this neuron.
*  And so if you know all the positions that the animal went through
*  and you know who fired at every position, you can construct the place fields.
*  But within the brain itself,
*  sort of like the only information really is the spiking of the neurons.
*  And the place maps, the cognitive map is not a topographic map.
*  You know, the same cells can either overlap or not in different environments.
*  It's not like retinotopy in the visual cortex.
*  It's very different.
*  And so in some sense, if you think about what information is really available
*  to the brain, it's not the position information necessarily,
*  because there's no sensor for position.
*  But somehow it's the information about when place fields overlap.
*  So if two cells fire at the same time or in a small time window,
*  you can infer that their place fields overlap
*  because there must be some position that's activating both neurons.
*  And so if you look at the co-firing, if you look at the neural code
*  that emerges from the animal roaming around this environment,
*  it gives you information about which place fields overlap,
*  but not where they are.
*  So you don't know if I'm just looking at the spike trains,
*  if I'm just looking at the spiking, I can say, all right,
*  the place field from neuron one overlaps with the place field
*  with the place fields from neurons five, seven and 15.
*  Also, five and 15 overlap.
*  And there's a three way overlap between one, five and 15.
*  I mean, you can say things like that, but you don't necessarily know
*  where the place fields are located.
*  And so one of the questions back in like 2007
*  that Vladimir and I asked, actually, is that we were we were at the time
*  we were sort of talking and collaborating with the Bujaki lab
*  and so thinking a lot about place cells and so on.
*  One of the questions we asked is like, well, what what can you learn
*  about the environment? What can you learn about the stimulus space?
*  Just from that, just from that information, just from knowing
*  which place fields overlap without knowing where the place
*  fields actually are.
*  And it turns out that you can know you can learn quite a bit
*  about the topology of the environment.
*  You can learn if there are holes in the in the environment,
*  like if the rat is roaming on a on a table that has a hole cut out of it
*  or maybe a tree in the middle of some place that it can't it can't traverse.
*  And you can do that using methods from algebraic topology,
*  because, in fact, algebraic topology
*  allows you to infer
*  topological properties of a space from what's called an open cover.
*  So an open cover would be like a bunch of open sets that cover a space.
*  And now you can imagine, you know, going back to my Taurus or or
*  or a sphere or some other
*  some other topological space, if you take a bunch of open sets
*  that cover it and that cover is good in some sense
*  that I'm not going to in the technical sense that I'm not going to describe.
*  But if you have a bunch of sets like that,
*  what you can think of like place fields, right, covering your topological space
*  and you know how they overlap.
*  So you can you can encode the information of how they overlap
*  in a combinatorial structure called the nerve of the cover.
*  They actually called it the nerve of the cover
*  100 years ago. No connection to neuroscience.
*  But you can encode that in this combinatorial object
*  called the nerve of the cover, which is a simplicial complex, which is
*  it's a generalization of graphs.
*  So graphs have edges between pairs of objects.
*  This is like a graph.
*  But instead of just having edges between pairs,
*  you can also have like a triangle between a triple
*  or a tetrahedron between a quadruple and so on.
*  And that's keeping track of the overlap.
*  So if I have place fields, you know, one, five and 15,
*  and they not only pairwise overlap, but there's also a triple overlap.
*  Then instead of having a graph where I just connect one five, five,
*  15 and 15 and one, I also fill in this triangle to denote that there's
*  a triple overlap as well.
*  And so that overlap information, you know, in topology land
*  gives us this nerve of the cover, the simplicial complex that encodes
*  all of that intersection data.
*  And and and there's a theorem called the nerve lemma
*  or the nerve theorem, depending on which version.
*  And that mathematical result tells you that you can compute these topological
*  features like homology groups, which count these holes
*  that we were talking about earlier.
*  You can compute them from the nerve, from that combinatorial object
*  of the cover, and it will tell you what the what those same
*  topological features are of the underlying space that's covered by those open sets.
*  So this is exactly like the place field setup.
*  Right. So the place fields are like the open sets.
*  The animals environment is like the underlying topological space.
*  And what this theorem, you know, hundred year old theorem from algebraic topology
*  is telling us is that just from that combinatorial data of who intersects
*  with who, even without knowing who the place fields are, right,
*  who the open sets are, just knowing how they overlap.
*  You can compute topological features of that underlying space that was covered.
*  So this is like really kind of a magical.
*  Sorry, sorry. No, I was going to say which map on to in
*  the case that we're talking about the example, which map on to the environment,
*  essentially with holes and borders and so on.
*  Exactly. Which map on to the environment. Exactly.
*  And so and so in the neuroscience context, you know, what this translates to is
*  the neural code intrinsically encodes topological properties of the environment
*  in the case of say hippocampal place cells.
*  And so that I think is a really lovely insight. Right.
*  And so that that neural codes,
*  when you look at the structure of the entire code, it's not just about,
*  you know, which pattern of which pattern of firing corresponds to which stimulus.
*  But somehow the collection of all the firing patterns,
*  the collection of all the code words has structure in it.
*  And that structure of the code reflects structure of the stimulus
*  space that's being encoded.
*  Well, we can't record all neurons, right.
*  In, let's say, hippocampus, CA1 or something. Right.
*  So you're only subsampling.
*  So does that affect the ability of a topological analysis to
*  complete the cognitive map?
*  Yeah, absolutely. So so when we so, you know,
*  Vladimir and I wrote a paper on this back in 2008, where we we simulated
*  we simulated place cells from place fields, you know, using
*  using sort of properties of place fields that were taken from from real data.
*  But, you know, making many of them right so that we completely cover the space
*  as a proof of principle that this would actually work.
*  And so that, you know, again, because of limitations of data, right, we
*  we had to kind of make synthetic data
*  that matched in terms of properties with real data, but was nevertheless,
*  you know, complete. Right.
*  So you can completely cover the space.
*  However, I should say a lot of advances have been made by now.
*  And so I think the most recent result really looking at these topological
*  properties in neuroscience is coming from the Moser lab.
*  So they have this nature paper that was published just last year.
*  I forget the name toroidal structure or something of in grid cells.
*  So they actually were able to record
*  lots and lots of cells enough to to really cover the space.
*  But in their case, they're doing grid cells and grid cells are interesting
*  because there you have this repeating grid like structures.
*  So the grid cells are kind of like place cells in that they are responding to,
*  you know, positions in space, except that a single neuron
*  will have many hotspots that it responds to and they form a hexagonal grid.
*  And so different neurons will have different hexagonal grids
*  that they're associated to that are kind of shifted from each other.
*  In scale and orientation. Yeah.
*  Yes, in scale and orientation.
*  And and so and they really can be grouped into these modules
*  because if you have a different scale to your grid,
*  you want to sort of group all those neurons together that have different phases
*  and different orientations, but are sort of on the same grid size.
*  And so they were able to record so many neurons that they could capture
*  enough grid cells to cover the space
*  with various modules, if that makes any sense.
*  And and there, because of the struck, because of the sort of hexagonal structure
*  of the grid cells of the grid cell map,
*  it was predicted from topology considerations that that those neurons
*  should trace out a torus.
*  That paper is really a tour de force in terms of recording enough neurons
*  that they can actually see the they can actually see that torus.
*  They can see the topological structure of the torus in the neural activity.
*  And again, it just it just points to topology being fundamental to neural coding.
*  And I think that we're going to see that in in more and more areas, more and more systems.
*  And I think that's the sort of an exciting reason to use topology
*  neuroscience that goes beyond just, oh, it's data.
*  Let's analyze it with topology, because because we can.
*  You know, I think there's something more fundamental than that
*  when it comes to neural coding in particular, that oftentimes
*  what's being encoded really is topological in nature.
*  So the structure of like a topological structure.
*  Well, what I want to ask is sort of really high level, how
*  how topology relates to the dynamical systems theory, because a lot of
*  there's a lot of neuroscience talking about manifolds reducing dimension.
*  And there are trajectories along these low dimensional manifolds.
*  And that's how we can sort of describe in a way
*  some cognitive function as having some manifold shape.
*  And so anyway, it sounds like topology and
*  dynamical systems theory are highly overlapping, but how do they differ?
*  What what's different between the two?
*  Yeah, so that is a good point.
*  I mean, even in the even in the math community,
*  there is a long tradition of dynamical systems and topology overlapping, I should say.
*  And so that that is not just a phenomenon in neuroscience.
*  That is something that goes way back.
*  And that is because dynamical systems,
*  when you look at the configuration spaces for them,
*  when you look at sort of the set of all the states that the system can have
*  or the attractors of the system and so on,
*  those can be often described by manifolds that have certain topology.
*  And so understanding topology has always been fundamental
*  to understanding dynamical systems.
*  Yeah. And and I think in neuroscience,
*  it's a it's a similar connection.
*  So and this is another way that that topology can potentially play
*  a big role in neuroscience is an understanding
*  those lower dimensional manifolds.
*  So when people talk about sort of dynamic attractors
*  or they talk about manifolds of activity,
*  in some sense, they're really thinking about attractors. Right.
*  So they're thinking of a dynamical.
*  The network is kind of this giant dynamical system.
*  But the activity, the population vectors or what have you,
*  whatever you're tracking of the activity, are getting sucked into a lower
*  dimensional space and not sampling the full
*  repertoire of possible states that you might think you have.
*  And those lower dimensional structures, sometimes it might be appropriate
*  to call them attractors of the network.
*  And but even if not, you know, you you you would want to
*  describe them topologically.
*  You would want to know, OK, is that like a periodic structure?
*  Is is it a torus?
*  Is it a is it a loop that comes back to itself?
*  There are all kinds of, you know, questions that you could ask about
*  the shape of that, and that would sort of get to the heart
*  of what the network is doing.
*  So somehow you have this complicated dynamical system,
*  which is your neural network.
*  But the emergent activity of that network would sort of get like trapped
*  or sucked into this lower dimensional manifold that itself,
*  if you try to describe it, would have some topological properties.
*  And so that topology of that manifold is somehow a property
*  of the network and of the way that the network functions.
*  OK, all right, we got to
*  I really want to cover the linear network, so
*  I'm just going to skip ahead a little bit to those.
*  So beautiful models, combinatorial linear threshold networks.
*  This is what I originally wanted to talk to you about also.
*  And then, of course, I did a deep dive and then all the other questions
*  come out. But these are interesting in that I think that they apply
*  to your beautiful model
*  camp because they are even more abstracted.
*  Maybe I'll just try to describe them and then you can correct me.
*  And then we can talk about what they do and stuff.
*  So, first of all, one of the goals is to
*  be able to look at the structure of a network
*  and then predict the dynamics that if you ran that network,
*  predict the dynamics that it would give rise to different attractors, etc.
*  That's I know that that's that's one of the goals.
*  So, I mean, that's an interesting thing because there's this
*  structure function problem in neuroscience, right?
*  With Eve Martyrs work, for example, if you look at structure,
*  lots of different structures give rise to can give rise to the same function,
*  depending on your parameters that you're using.
*  So, you know, you can call it multiple realizability.
*  But it's also daunting to.
*  The thought is that we may never be able to look at a structure and know function.
*  But if we if we can look at a structure and know some dynamical properties,
*  that might lend something to say about the function.
*  Anyway, I'm rambling. But what you've essentially done
*  and maybe we can talk about like the simplest, you know, smallest ones.
*  And we don't need to go through examples.
*  But you, you know, you've gone down to like even two nodes, three nodes, four nodes
*  and abstracted away into this graphical network
*  where the nodes can can be connected and and the nodes are all excite
*  like excitatory neurons.
*  And when one node points to the other, it's going to excite that neuron.
*  Meanwhile, in the background, you have this invisible,
*  writ large inhibitory activity that is affecting the whole network,
*  but with kind of different rules for how it affects
*  different nodes, depending on which nodes are pointing to which other nodes
*  and connected in certain ways.
*  And that sounds, you know, very complicated, but it's actually a stripped down
*  and very simple way, which makes it tractable mathematically. Correct.
*  Yeah, that's a great description, actually.
*  Yes. Oh, good. OK.
*  So and I know this is kind of related.
*  This goes back to the idea of Hopfield networks, because these are,
*  you know, recurrent networks because there's loops and loops and loops,
*  depending on how big you build it up.
*  And Hopfield networks are kind of a special case of this because they all
*  they have like symmetric connections between all the units and et cetera.
*  So with that kind of background description in mind,
*  what have we learned about, you know, how structure, you know,
*  how far can we get looking at a structure?
*  So you've done this from, you know, two nodes together up to
*  I don't even know how big you have gotten so far,
*  but where you've been able to prove that if you set a node up this way
*  or if you can look at all the connections, if there are different sinks
*  and sources and the way that the way the different nodes are connected
*  without even fooling with weight connection parameters,
*  you've been able to prove what kind of dynamics can emerge from that structure.
*  Yeah, we've been able I mean, not completely,
*  but we've been able to say a lot.
*  So and it's been exciting.
*  So the yeah.
*  So the basic results that we have are kind of,
*  I think you mentioned graph rules.
*  So what are these?
*  These are these are direct relationships between graph structure
*  and fixed point structure.
*  So I should say the way we have access to the dynamics of these networks
*  is primarily through the fixed point structure,
*  familiar to anyone who studied hot field networks or has studied,
*  any kind of networks in neuroscience is the idea of stable fixed points.
*  So when your activity goes to, you know, a single firing rate vector
*  that kind of persists, persistent activity is often modeled by a stable fixed point.
*  And in the hot field model,
*  the memory patterns are all modeled by stable fixed points of the dynamics.
*  So these are really a single point in your state space.
*  So I have a pattern of firing and I'm just stuck there.
*  And but there are many of those patterns that I can get stuck in.
*  So if you imagine kind of this landscape and there are these minima of your landscape
*  and what the computation of the network is to take an initial condition,
*  evolve the network dynamics until you fall into one of these minima.
*  And that's your recovered pattern.
*  And so that initial condition could be a partial pattern of, you know,
*  maybe an image that has missing pixels and has like a partial pattern.
*  And then the network would evolve it to do pattern completion,
*  to fill out the rest of the of the pixel values.
*  So if I had a degraded picture of a mouse face or something, I would easily.
*  Right. Because of my that pattern completion completion,
*  my hot field network inside my brain would settle down to the mouse pattern.
*  And I would be able to say, oh, mouse. Exactly. Yeah.
*  So that corrupted pattern would put you in a in an initial condition
*  that is in what's called the basin of attraction of the complete pattern,
*  which is stored already in the network.
*  And if you don't have that pattern stored already in the network, you won't complete it.
*  So you can only kind of complete patterns that have been previously stored in the network.
*  And so you imagine the entire state space, right?
*  All the possible firing rate vectors
*  gets partitioned into these basins of attraction,
*  which is like the region where if I start there,
*  I'm going to get sucked into a particular attractor.
*  And the attractors here are all just stable fixed points.
*  And they correspond to sort of a single pattern that's been stored or a code word.
*  You might say the neural code of the network is like all those stored patterns.
*  And so the hot field model was really
*  about that setup, right.
*  And so the questions that were asked were, how do I store patterns in the network?
*  What kind of learning rule?
*  Once I have all these stored patterns, am I going to get extra spurious patterns
*  that I didn't mean to store? Right.
*  Because sometimes it's like it's not clear that I can just arbitrarily choose
*  pattern A, B and C without accidentally creating a new pattern
*  that I didn't want to create.
*  And if I create too many patterns, then my basins of attraction
*  get too small and too finicky.
*  And so then I can't really complete, you know, I might start with that
*  corrupted mouse picture, but because I have so many different patterns store,
*  maybe I will accidentally go into the wrong attractor.
*  And so those are their issues of capacity.
*  How many patterns can you reliably store without, you know, and still
*  recover them with reasonable initial conditions and so on.
*  And so that's this whole game of how memory works. Right.
*  So this is kind of a framework for thinking about memory
*  as consisting of these stored patterns
*  that are really encoded in the synaptic weights of the network.
*  And in the case of the hot field model, they really are all kind of stable
*  fixed points. And the model itself, in order to guarantee that,
*  has symmetric weights.
*  So that just means that between any two neurons,
*  the connection from neuron I to neuron J is identical to the connection
*  from J to I. So that is, you know, not true in the real brain.
*  Despite the processing.
*  Well, yeah, no, not true. Right. Not true.
*  Brains messier. But your model, but your model models are
*  super abstracted and not messy either. Right.
*  Sorry to interrupt, but.
*  Yeah. So so it's not true.
*  The brain is messier.
*  But like this particular messiness can be done,
*  you know, by simply not having symmetric weights anymore.
*  But the and so in the combinatorial threshold
*  in your network models, we don't require symmetry. Right.
*  So we don't require the connections to be symmetric.
*  And that just means we allow that sort of W matrix of connection
*  strengths to have a different IJ value from its J.I value.
*  That opens up the dynamics into a whole richer world of possibilities.
*  So it turns out when you when you impose the symmetry,
*  there are some other conditions that I'm sort of going to gloss over.
*  But roughly speaking, when you impose the symmetry on these weight matrices,
*  you can get multiple stable fixed points, which is a feature of nonlinear dynamics.
*  So you get nonlinear phenomena, the multi stability,
*  but you can't get dynamic attractors.
*  So you're still stuck with only having stable fixed points as your possible attractors.
*  Why do we want to get dynamic attractors, though?
*  Because the memories is a great question. Right.
*  Why do we want to add it?
*  So, you know, all you care about is taking corrupted images and pattern
*  completing. You don't care about dynamic attractors. Right.
*  And if that's all if that's all your brain wants to do is look at a fragmented
*  picture and say, oh, that's a dog, you know, that's a cat.
*  Then you don't really need dynamic attractors.
*  But I would argue that, well, first of all, when we look at brain activity,
*  it does not appear to go into fixed points.
*  It's always oscillating. It's always constantly changing.
*  And and one of the things that I think the neural recordings show us,
*  which is why the sort of manifold manifold methods and so on are so popular
*  these days, is that often what happens to the neurons in a network in response to a
*  stimulus is they don't go to a stable fixed point, but they do get sucked into
*  some lower dimensional manifold or what I might call an attractor that is
*  dynamic. So you might have a stimulus comes in.
*  You have some big transient response potentially from the network.
*  I used to work in auditory cortex when I was a postdoc.
*  So it's like we would see, you know, we'd have a sound played.
*  We were recording from primary auditory cortex and rats.
*  We'd see some big transient response, lots of neurons firing.
*  And then the activity would like settle down and there would be some subset of
*  neurons that would continue to fire a lot, but not in a stable fixed point kind of
*  way. There would still be some kind of oscillation, some sort of dynamic activity,
*  but in this lower dimensional space.
*  So it would be kind of sucked into like a, you know, like an attractor that is
*  dynamic. The other thing I should say is that, you know, beyond seeing this in
*  experiments, it's clear that we have we're able to store memories that are dynamic.
*  So we can remember sequences. We can remember the alphabet.
*  We can remember songs.
*  8675309.
*  I put that in one of my talks.
*  Yeah, because you give an example of a network that can encode if you assign a
*  number to each of the nodes, nodes of the network.
*  Yeah.
*  It spits out this limit cycle, which encodes at the peak of every neurons firing, every
*  units firing is it spells out the phone number anyway, which is a famous song.
*  I don't remember who, but so there are these like dynamic sequences and limit cycles
*  and all these different types of attractors, right?
*  That you can get out of these networks.
*  Right. Exactly.
*  So it's like when I'm remembering a phone number, you know, it seems perfectly
*  reasonable to model that as a limit cycle.
*  Like I remembering a sequence and we don't do this anymore, right?
*  Because we have cell phones and we just have a, but I, you know, we used to like
*  look up phone numbers in the phone book and then have to like remember it until we
*  got to the pay phone, you know, to dial it.
*  And I would play it in a loop, right?
*  I would think of the number in a loop.
*  And so there's something very dynamic about the way many memories are encoded.
*  I mean, I should also say there's also this whole area of central pattern generator
*  circuits, which I'm very interested in, which has traditionally been modeled with
*  limit cycles in the sort of mathematical and theoretical neuroscience community.
*  I mean, some of Eve Martyr's work with theorists, right, has been very specifically
*  about modeling central pattern generator circuits.
*  And yeah, and there you see limit cycles all the time.
*  You just, you see periodic sequences of neural activity that repeat.
*  Like if you imagine a animal locomotion, right?
*  You have a horse walking or trotting or something.
*  And there's a periodic, a repeating sequence of signals activity.
*  Left hoof, right hoof, back hoof, forward hoof.
*  Right, exactly.
*  You've also demonstrated that's something else.
*  But so then you have these examples that you use in your talks and papers of these
*  kind of different kinds of attractors.
*  But and I'm sorry if I'm skipping ahead too much, I'm just aware of our time.
*  But I'm just wondering in some sense, these are still small kind of toy models.
*  And the background inhibition that I talked about, there are just two rules, right, of
*  this inhibition that affects all of the units the same way.
*  A, I'm wondering, you know, can we really apply this to real messy brain data, right?
*  And look at, you know, record neurons and say something about the dynamical structure
*  and prove it mathematically, right, in some structure of the brain.
*  And then B, like just how far up do you feel like you can scale these models in an
*  attractable way?
*  Because I know that you have like sub modules and there are rules for modules being,
*  motifs being embedded within larger motifs.
*  And you can still look at that structure and talk about some of the chaotic and well,
*  talk about some of the types of attractors that come out.
*  So is this something that just will scale easily?
*  So it's true that the examples I show in my talks, which are the sort of like the ones
*  we've studied the most, you know, kind of show off the techniques.
*  Which are super cool, by the way.
*  All right.
*  And they tend to be, they tend to be small because we're sort of designing them to.
*  So one of the questions that we like to ask is how do you encode multiple dynamic
*  attractors at once, right?
*  So if you go back to the Hopfield model, right, one of the challenges was like, OK,
*  how do I store multiple memory patterns as fixed points, you know, and keep them all,
*  right, so that you can still recover them and you don't have too much interference.
*  And if you ask that question about dynamic attractors, right, it's trickier because now
*  you're no longer talking about it, you know, isolated stable fixed points.
*  Now you have these larger, you know, these dynamic attractors that have, you know, it's
*  a subset of the state space.
*  It's a big loop of activity and you have many of them.
*  And they may share the same neurons between them.
*  And you want to know, like, how is it possible to store those in a larger network in sort
*  of a modular fashion that preserves the dynamic attractor, even as you're adding other stuff
*  to the network?
*  And what we have found are rules that allow us to kind of predict when, you know, one of
*  these sort of smaller networks that produces a dynamic attractor, when that dynamic attractor
*  will persist when embedded in a larger network.
*  And sometimes we can predict that will happen and sometimes it's happening even though we
*  don't have a good handle on why.
*  But there's something about the inhibitory structure that really helps to be able to,
*  like, encode these structures.
*  And so I would say that in order to scale things up, we really do sort of depend on
*  this strong, locally strong inhibition in order to sort of keep the attractors clean.
*  I don't know if that makes any sense, but somehow the inhibition is what allows the
*  attractors to really lock in and stay there even as you make the network larger.
*  And so we've done these experiments, for instance, where we kind of want a big thing
*  that we do is we try to classify motifs that support attractors.
*  Right.
*  So one of the questions you might ask, like, okay, I have this large network.
*  What are the substructures that are really supporting these dynamic attractors that you
*  might see?
*  So going back to kind of the experimental data that I was telling you about where you
*  might have some large transdentive activity and then it settles into some subset of neurons
*  that are really firing but in some kind of pattern that's dynamic.
*  So you might ask, okay, well, there's a sub network for those neurons alone.
*  And somehow that sub network is supporting this lower dimensional attractor.
*  And but it's embedded in the larger network.
*  Right.
*  So why how does that happen?
*  How can you take a dynamic attractor that is really supporting on a small network and
*  still have it persist when you've embedded it in the larger network?
*  And that is that is one that, you know, that is definitely something that we think a lot
*  about and have made some progress on.
*  So mathematically, one of the things we can prove theorems about is when kind of the
*  unstable fixed point that's associated to the dynamic attractor, when that one will
*  persist.
*  And that gives us clues as to when the attractor will persist.
*  And so via the fixed point structure and via the way the fixed point structure changes
*  or is preserved when a sub network is embedded in a larger network, we get sort of strong
*  clues as to whether those attractors survive.
*  And so that's the sense in which we think about scaling it up.
*  So we the perspective is that somehow you have modules, you know, sub networks in the
*  brain that do things.
*  Right.
*  And you want to you want to understand how they can be embedded in the larger networks.
*  So let's say they can still do their thing and not be kind of destroyed in terms of the
*  activity they produce by the way that they're embedded.
*  So that those are sort of the questions that we have.
*  Sorry to rub it.
*  Is this something that would like potentially solve the binding problem?
*  As you think, like looking at a horse or like if you're in front of a horse, right, you
*  see the horse, you smell the horse, you can hear the horse and all.
*  And it's like a cohesive experience.
*  Right.
*  Are these sub modules that are in some topological toroidal shape that's somehow and that's
*  the binding?
*  Yeah.
*  I mean, I've thought a little bit about the binding problem because I, you know, I don't
*  I don't want to get too far ahead of myself, but on one of the cool things that we've
*  found and that we can predict via the fixed point structure is these attractors that we
*  call them fusion attractors.
*  So it's almost like it's like, oh, I have an attractor, you know, some dynamic pattern
*  supported on some or a fixed point, you know, supported on one sub network.
*  And I have another sub network that has another kind of attractor.
*  And if they are embedded.
*  So previously I was saying, okay, there are ways we can embed those sub networks to preserve
*  the attractor in the larger attractor, right, in the larger network.
*  Sorry, I meant the larger network.
*  And so that's one question, right?
*  How do you embed so that it's so that these individual attractors are preserved in the
*  larger network?
*  But there are other ways to embed them where you lose the individual attractors, but you
*  gain an attractor that really looks like a fusion between the two.
*  So it's like they're both going at the same time.
*  And that is really striking because now somehow I've been able to take these different pieces
*  and connect them up in such a way that I still see the individual attractors going.
*  So maybe I have a three cycle going for some subset of neurons and, you know, a fixed point
*  or some other dynamical attractor going for another subset of neurons.
*  And now I've embedded them together and I've connected them in such a way that in the larger
*  network, what I will see is them turning on together into a single higher dimensional
*  attractor that encodes kind of both attractors at once.
*  And that feels like a binding kind of thing.
*  And or the emergence of consciousness or something.
*  Yeah.
*  Yeah, no.
*  Not sure about consciousness.
*  And I don't think I don't think CTLNs are sentient.
*  Oh, come on.
*  Why is that getting so much traction?
*  Yeah.
*  So I know that I've already taken you over, but maybe the last thing that we can end on is
*  just how you know, how plausible is it given how messy the brain is?
*  And, you know, we haven't even mentioned that for just to bring it back to like a deep learning
*  network where the whole thing is about the weights changing and learning.
*  Right.
*  These networks are so abstracted that you fix the weights, you fix like the parameters,
*  and there's very few parameters, which is what makes them tractable in the first place.
*  But then applying that to real wet brains, is there going to be a clean mapping there?
*  Yeah. So I should say, so the CTLNs, I do think of them as having fixed weights for a graph.
*  But there are these parameters for the weights, right, that we are allowed to change.
*  And so one of the goals is to the graph rules, for instance, which tell us how to relate fixed
*  points to the structure of the graph. Those are parameter independent. So I can change the
*  weights within some, what we call a legal range. I can alter the weights and preserve the basic
*  structure of the fixed points. So that's, you know, so we do sort of, we are trying and we
*  often do prove results that are largely independent of those weights. That said,
*  you know, even with a two parameter family is still a very small number of parameters for,
*  you know, a network of neurons. And so we also study more general threshold in your networks.
*  And one of the things that we have found is you often have the same attractor that can appear
*  in different networks. And this is not so surprising, given what I've just told you,
*  that we think about how do you embed a particular sub network so that the dynamic
*  attractor is preserved, right? But so once you understand the rules for that, then what that
*  tells you is that there are weights that you can change in the larger network that keep the
*  attractor intact. And so that really addresses kind of the learning. So there's a robustness.
*  Yeah, there's a robustness. And there's this concept that, you know, once I embed a dynamic
*  attractor, you know, with say some subset of neurons, five neurons, 10 neurons, right in a
*  larger network that maybe has hundreds or thousands of neurons, there are now edges that I
*  want to freeze, right? There are weights that I don't really want to change because I want to
*  preserve my attractor. But there are other edges, there are other weights that are going to be free,
*  and I can freely move them and still keep this attractor. And I have these I have this sort of
*  simulations where I show moving through that weight space. And it's really striking because
*  you see this, you know, different dynamical systems, you know, solutions to different dynamics,
*  and they're just right on top of each other. It's really like the same attractor, but I'm changing
*  edge weights, and changing the network, but I'm really preserving this attractor in this piece of
*  it. And so, so that I think the the way that we are, what we want to understand is, you know,
*  who's allowed to be plastic, right? What weights are allowed to change in order to preserve an
*  attractor? And what weights, if we change them, we may actually lose the attractor or distort it.
*  And understanding that is really kind of the key to sort of developing learning rules that would
*  allow you to store multiple attractors in a network, you know, without distorting them.
*  Because now it's no longer an issue, like in the Hotfield model, the question is, how many memory
*  patterns can I store and not lose, lose the previous ones. But here, it's not just about
*  losing the attractor, you can corrupt it. Because now it's not a point anymore.
*  Yeah.
*  Right. It's a whole dynamic attractor, and you can really distort it. And so, how do you preserve
*  the full dynamic attractor in this larger network? And so we are studying in the broader TLN space,
*  so not confined to the combinatorial threshold linear networks, which are our subfamily,
*  but in the broader family of threshold linear networks, where in principle, all the weights
*  are allowed to change freely. We are trying to understand which weights matter and which
*  weights don't matter for particular attractors and thereby figure out where the plasticity is.
*  And so the vision is that somehow the networks in the brain, once you encode certain attractors,
*  you might want to kind of stabilize certain synapses, but others are left free and can be
*  freely changed to store a different attractor, some other song, some other pattern of activity,
*  and still guarantee that you preserve the first one. So that's how you and I can learn the same
*  song and not corrupt everything else we know.
*  But I can learn Jim's phone number too, and Mary's.
*  Right. And I don't have to know those and somehow...
*  You don't need to know those.
*  Right.
*  Yeah. But I need to make a song out of them to remember them, of course, as we learned with
*  what was her name in that song?
*  Jenny?
*  Jenny. I believe it was Jenny's phone number.
*  Yeah. There you go.
*  Yeah.
*  Okay. Okay, Karina, I'm glad this is all so easy for you and I appreciate you talking with me.
*  I promise this is the last question. How much more math are we going to need to learn to,
*  well, quote unquote, understand the brain? Do we have the right math tools or do we need to...
*  How many more different math tools will we need to apply, invent, and or apply?
*  That's a loaded question. I think we're still very limited in our math tools, honestly.
*  And I'll just quickly say why. Neural networks, fundamentally, are high dimensional, nonlinear,
*  dynamical systems. And high dimensional, nonlinear, dynamical systems are a nightmare.
*  Mathematically. It's really hard. And if you see what people do when they analyze networks,
*  it's striking. And to this day, 2022, people will simulate large nonlinear networks that do all
*  kinds of crazy things. And then when they come down to analyze them mathematically, they linearize.
*  It's like linearize around a fixed point, which by the way requires that you have a fixed point to
*  linearize around and a single one that somehow is representative of the activity of the whole
*  network, which when you think about that real networks probably have multiple fixed points,
*  multiple attractors, you can't just pick one point in the space to linearize around.
*  So I think there's a fundamental gap between the tools we have to analyze large dynamical systems,
*  which tend to be just linear tools, and the beast, which is high dimensional, nonlinear dynamics.
*  And that's a gap that exists in the math world, too. It's not that mathematicians secretly have
*  books where they figured out all of this stuff. It's just a real gap. And I think with threshold
*  linear networks, I am trying in my own way to fill that gap in some very simplified,
*  the simplest nonlinearity you can have, but fully high dimensional systems of differential equations
*  with a very simple nonlinearity and trying to actually develop mathematical theory that would
*  allow us to predict. So when it comes to linear systems, it can give you a giant matrix.
*  If you have a linear system of differential equations, we teach our undergrads how to solve
*  these. And you can predict long term behavior. You can predict, if you have a Markov chain,
*  you can predict the long term behavior, the long term dynamics, you can answer that question
*  mathematically. You put nonlinearity in there, and now you're screwed. Yeah. But if the nonlinearity
*  is simple enough, like threshold linear, you're not screwed, not completely. And that's what the
*  threshold linear network is trying to do. It's trying to generalize the theory of linear systems
*  of differential equations to a mildly nonlinear, mildly but still dramatic enough that you get
*  dynamic attractors and all these things that you don't see in linear systems. Linear systems,
*  you have one fixed point, it's either stable or it's unstable, and that's the end of the story.
*  But once you put in that threshold for the nonlinearity, now you get the whole repertoire.
*  You get chaos, you get limit cycles, you get multi-stability, you get all of that stuff.
*  But you still somehow can piggyback on the tools of linear differential equations in patches,
*  right? With combinatorics, with care, right? You can kind of bootstrap from there and
*  get access to the nonlinear phenomena. So that's what I'm trying to do. And the reason I'm trying
*  to do it is because I do think it's a real mathematical gap, and there are many. Yeah,
*  I think neuroscience is really a field that is experimentally super advanced, I would say,
*  I would say, compared to 19th century physics. But mathematically, I think there are a lot of
*  challenges, and that's part of why our theory and our modeling is still somewhat limited,
*  because we're still relying on linear methods all the time. And that's really limiting our data
*  analysis and our dynamical systems modeling and just our theory in general. And so, yeah,
*  so unfortunately, well, unfortunately for some people, fortunately for mathematicians like me,
*  I think there's a lot to do. One person's challenge is another's opportunity.
*  So thank you for my opportunity to speak with you, and thanks for coming on. Thank you.
*  Brain Inspired is a production of me and you. I don't do advertisements. You can support the
*  show through Patreon for a trifling amount and get access to the full versions of all the episodes,
*  plus bonus episodes that focus more on the cultural side but still have science.
*  Go to braininspired.co and find the red Patreon button there. To get in touch with me,
*  email paul at braininspired.co. The music you hear is by The New Year. Find them at the newyear.net.
*  Thank you for your support. See you next time.

---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 2894s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 371
Video Rating: None
---

# BI 047 David Poeppel: Wrong in Interesting Ways
**Brain Inspired:** [September 15, 2019](https://www.youtube.com/watch?v=UqMQ3Hg8FSU)
*  When we first wrote this and tried to publish it, people basically said to us, you guys
*  are just, you guys are nut jobs, you don't know what you're talking about, you're young
*  and you don't know the field and you're just very naive and it's kind of sad, hashtag
*  sad.
*  It's a system that's just absolutely shocking and I think in 20 years or maybe 50 people
*  are going to say, wow, you guys lost generations of wonderful, creative, exciting scholars
*  but putting them into this ridiculous system of what counts as success and what counts
*  as what the meritocracy is about and how you publish and how you assign beans.
*  This is Brain Inspired.
*  Hey everyone, this is Paul Middlebrooks here again with David Popple for the second part
*  of our conversation about speech processing, language, understanding, the neural basis
*  of all of that and some of the recent progress in AI on that front plus plenty more including
*  David's thoughts on how we are failing to provide graduate students with the right environment
*  to become great scientists.
*  If you missed the first part, you should listen to it first, episode 46 because this picks
*  up where that left off.
*  We were basically in mid-conversation.
*  Thank you for listening and if you like the show, consider a tiny two or four dollar per
*  month contribution through Patreon.
*  You can go to BrainInspired.co to find the red Patreon button there to click.
*  I am a solo act, no big podcast production company, no massive university or company
*  backing me.
*  It's just me, my guests and you guys.
*  So thank you in advance and thanks to all my supporters on Patreon out there.
*  It is astounding and super encouraging.
*  You could also reach out to me with questions and or suggestions on Twitter.
*  I'm at pgmid, P-G-M-I-D or email paul at BrainInspired.co.
*  Okay here is the loving curmudgeon who wants us all to do the best science that we can,
*  David Popple.
*  Since we're talking about oscillations and time, it might be a good time to transition
*  and talk a little bit about AI and deep learning because dynamics are important in our cognition
*  as we were just talking about, but it's not, you know, dynamics aren't so much important
*  in deep learning nets, right?
*  So there's been a ton of progress in natural language processing, doing things like translating
*  between languages, speech recognition, summarizing texts, you know, and so on.
*  Are you familiar with the transformer model for NLP that Google created at all?
*  Yeah, it's all the rage and certainly in Europe.
*  Oh yeah, I bet.
*  I was just at a meeting in Holland where people were just going nuts about their transformers.
*  Oh yeah, yeah.
*  Well, yeah, so there's that track.
*  There's also, I'm sure you're familiar with this recent work out of Josh McDermott's lab
*  creating these deep networks to, so I had Dan Yeamans on the show and some other people
*  who have talked about, you know, have worked on these deep learning networks that have
*  replicated some of the findings in the visual stream, right, in the ventral visual stream,
*  object recognition stream in particular.
*  Yeah, there's a certain kind of fervor of argumentation in that line of work coming
*  from John DiCarlo's lab.
*  Yeah, fervor is a good word.
*  And Dan Yeamans did the work there and of course Josh was formerly here and worked on
*  stuff together too.
*  That's right.
*  Really gone on board with that and sort of translated some of that to the auditory case,
*  which is interesting and looks like a potentially promising way.
*  Yeah, that's, yeah, so I mean, there's this, I think it's nature neuroscience.
*  The network that I'm talking about where they, similar to the visual ventral stream,
*  they sort of replicated behavioral findings and some auditory tasks.
*  Yes.
*  And you see the same kinds of representations at some levels in the network as you see in
*  neurons, for example, in brains.
*  And actually they found that the best network that they trained, so they did like a speech
*  task and the best quote unquote network was actually two separate networks.
*  With different ones, yeah.
*  Yeah, with different.
*  Well, it's consistent with Josh with other work from that lab and other labs and that
*  actually Sam Norman-Hagner, former student there, has done on really the, in some sense,
*  refinding a more modular organization of speech and music.
*  So that's interesting.
*  And the network results are quite recapitulate that, what the imaging results had shown.
*  And actually what lesion results show too is that there's considerable segregation of
*  function when you compare speech and music.
*  It's not that surprising.
*  They're not the same animal.
*  But it's cool to show it.
*  And I think it's quite interesting that the architectures these guys were pursuing, which
*  in this very cool work are, yeah, it's not the same animal.
*  What I'm concerned about that is different things are different.
*  So that's...
*  You heard it here, folks.
*  Well, so one of the things that deep learning nets sort of implicitly assume is that the
*  neuron is the right level of analysis.
*  Right.
*  The right orientation of the...
*  Yeah.
*  They don't train on oscillations, for instance.
*  Yes, that's right.
*  So I'm just kind of curious in general on your take.
*  How has deep learning, do you think, contributed to or affected our understanding of auditory
*  and speech processing?
*  I mean, so it's just beginning to, right?
*  So let's take the...
*  Actually, I think it was Josh who...
*  There was an interesting workshop probably organized by Josh at MIT about two years ago.
*  So a bunch of us and a bunch of the deep learning people were sitting together for a couple
*  of days trying to get our head around sort of what are the different performance things.
*  And of course, the performance of the ASR system is kind of awesome now, right?
*  Assuming there's no noise, it's the same speaker, you don't have an accent, you don't have a
*  cold, you know...
*  You have to enter your accent.
*  Yeah.
*  So the performance is amazing, although not as amazing as any two-year-old.
*  So the...
*  Yeah.
*  Just to be...
*  But one of the interesting things was one of the things that could be, for instance,
*  an interface, it may or may not be necessary, right?
*  Remember that for those guys, of course, for the people working on the engineering problem,
*  performance is the ultimate, you know, performance on benchmark tests is what they're about.
*  And it's not of interest what a cognitive system does, that's not their business.
*  But it's interesting, nevertheless, to sort of exchange ideas.
*  And one of the things that we do particularly well is what we were talking about a bit earlier,
*  which is the segmentation issue.
*  Like, we're really good in a language that we speak to just chunk stuff up.
*  And we use physical cues like, for instance, the amplitude envelope, because it's an obvious
*  one.
*  And then we use other cues, for instance, you know, that we have knowledge of vocabulary,
*  we have all kinds of top-down information.
*  So we're really good at unitizing the problem as the signal comes in, which makes the decoding
*  problem easier.
*  So one of the discussions we had, which I thought was quite interesting, is what would
*  happen if you enrich, you know, a really, you know, an ASR system built on a deep learning
*  architecture with rhythmic activity of some form that capitalizes on that?
*  And I don't think the results are in yet, but there were some discussions about how
*  to do that, when to do that.
*  Would that actually tweak your performance in a bit?
*  Because that's something that you get sort of for free from the human auditory system,
*  from even the afferent system.
*  Well, it's free, but it's also a constraint, right?
*  I mean, it's a great constraint, and it could actually boost performance.
*  So let's say reduce the search space for these learning systems, because you say, look, you
*  know, here's a chunk, go find me that.
*  And so there's interesting potential interaction between that.
*  To what extent these architectures, you know, what's your favorite transformer, DNN, CNN,
*  LSTM, for your system is?
*  I mean, it's not yet clear from the cogneuro point of view.
*  I think it's a little early days.
*  I mean, I think Josh is one of the first people to really work on it very effectively in an
*  interesting way.
*  It's beginning to sort of penetrate the field, but it's not so obvious what the questions
*  are, other than being descriptive, right?
*  So I think that's a good point to say, well, the network that recapitulates what we knew
*  about the network is good.
*  It's a really good first result.
*  It's a little bit like the early work on the Ventral Visual Stream, that, you know, your
*  144-layer CNN can be probed, and you find something that's a little bit like, you know,
*  before, that's cool.
*  The question is, where does that go?
*  Is that just a re-description of the system, or, you know, is it really capturing something
*  deep?
*  I mean, I think that some of the work extending what is a reasonable, you know, how can you
*  drive cells into some weird perceptual space by saying, you know, I've recreated the optimal
*  stimulus by, well, by reverse engineering, what is the best thing for my receptive field?
*  Can I make a super stimulus, right?
*  Can I make a stimulus that drives a cell even more than a naturalistic stimulus, right?
*  That was a recent paper by the DeCarlo lab, which sounds pretty cool and weird.
*  And the images were weird, yeah.
*  The images are like, yes, kind of tripping thing, right?
*  Yeah, that makes sense.
*  So one could imagine doing something like that for the auditory case.
*  So let's say we reverse, we look at that and we say, hey, it turns out that, you know,
*  tonotopy, which is, by the way, one of my least favorite concepts, boring as all hell,
*  probably not useful.
*  You heard also that here first.
*  Okay.
*  But not like any friends, but tonotopy is not as useful as retinotopy.
*  How do you keep friends, sir?
*  I don't have friends.
*  I'm just trying to be nice to my family.
*  That's hard enough.
*  That's already a lot of work.
*  So it's conceivable that we end up with interesting stimulus parameters that are more powerful
*  drivers of, let's say, cortical cells than we have.
*  Right now, how many times are you going to listen to a talk with, yeah, we played 400
*  hertz, 1,000 hertz, and 3,000 hertz, and they were different?
*  Mm-hmm.
*  Mm-hmm.
*  Okay.
*  Right.
*  Differences are different.
*  That's right.
*  The question is, does it do anything for you?
*  Is it relevant?
*  Is that spatial arrangement even relevant at the sound pressure levels that we use when
*  we speak or hear?
*  I mean, there's a lot of open questions about this stuff.
*  It's a very coarse thing.
*  So we could use this to inform a little bit about what kinds of things the auditory cortex
*  is sensitive to, which would be really useful because our understanding, unlike the visual
*  case, our understanding of the human auditory cortex is not awesome.
*  It's not so we've imported, so there's partly because it's just painstaking work that hasn't
*  been done or is done by very few labs.
*  It's Yeoman's work, unbelievably important just to do the anatomy and the histology and
*  the staining on human cortical tissue.
*  There's very, very few data sets because it's a pain in the neck, right?
*  And so there's a big lab in Germany that does a lot of anatomy led by Katrin Amunds, does
*  very important work on this.
*  It's a little bit shameful how little we know about, you know, here we are very casually
*  talking about the old Felemen and Van Essen diagram, you know, and everything connects
*  to everything.
*  But if you ask for something like that for human auditory cortex, well, we look to the
*  macaque.
*  Well, there's some beautiful stuff by Royce and John Kass and colleagues that have done
*  some stuff.
*  But that's not the human auditory cortex.
*  And they're quite different, actually.
*  Like we speak and do other interesting stuff that, you know, and so there the animal model
*  stuff becomes really tenuous.
*  I mean, we really need a parochial model in the sense that, you know, parochial to us,
*  like to the human brain.
*  And that's a really important intermediate step.
*  And whoever does that and really is going to do a huge, huge service.
*  I mean, there's endless studies going on still defining, you know, primary auditory
*  cortex, core auditory cortex.
*  And like, yeah, it's never ending.
*  Yeah.
*  Let's just, you know, someone has to do their hard, difficult work of doing what was done,
*  you know, for 100 years and in the animal preps, which is doing, you know, the careful
*  histology, the staining, the lining up, the segregation.
*  Are there boundaries?
*  Are there not?
*  I know it's difficult.
*  I think the techniques are getting better.
*  You know, the hypnotized analysis getting better.
*  But we simply are still struggling with these basic questions about structure.
*  I mean, this really contrasts with the hype that deep learning has brought recently.
*  And are you optimistic?
*  Are you pessimistic in?
*  I'm very optimistic about it as an engineering thing.
*  And I'm very pessimistic about artificial general intelligence.
*  Well, about about its use in helping us understand cognition.
*  Yeah, there I'm I guess.
*  Because I'm a grumpy middle aged guy.
*  You know, there's a sort of age thing.
*  You know, you're my age.
*  You don't know anything.
*  If you're between my age and 30, you really have lived a life of MATLAB.
*  And if you're under 30, you're just a creature of Python.
*  Right.
*  That's how life is structured from my perspective.
*  I guess I'm seduced by the excitement of the results.
*  I think it's interesting.
*  And the fact that engineering solutions that are sort of brute force mechanisms,
*  this is what I was saying earlier, like, you know, is science become regression?
*  And so brute force, big data mechanisms are it's impressive to me that they work
*  across a range of tasks.
*  It's not obvious to me that that's the way we want to go in terms of
*  understanding cognition, perception, human brain organization.
*  And the sense that obviously we don't we don't work on billions of training
*  examples and learn discriminant.
*  We have a slightly different architecture.
*  And the but more importantly, you know, that can probably be solved and you can
*  do kind of wickedly cool unsupervised learning.
*  But what you and even unsparse examples and stuff like that.
*  So there's what I'm more interested in is that the kinds of problems that we
*  solve, you know, we can do in a way that's not so much about the data,
*  but the problems that we solve are the problems of common sense.
*  And they seem much less tractable than the problems of data.
*  So the problems of common sense are, you know, well, the kind of stuff that people
*  in robotics face.
*  Right.
*  So, you know, I can walk upstairs and get my keys and I can walk.
*  That's not a trivial problem as it turns out.
*  But it is actually a trivial problem.
*  Or you can tell me, you know, can you just quickly go back to your place and
*  pick up, you know, that book?
*  I mean, I can do that.
*  And, you know, I'm sort of moved by the fact that those systems are extremely
*  good.
*  And I think always have been.
*  I mean, they're just better now.
*  Right.
*  But they're good at the kind of stuff that requires pattern matching and
*  handling large amounts of data.
*  But they're less good at things that we actually do, which is having a
*  conversation, navigating my way home, watching, although, you know, can do a
*  Roomba, but that's hardly navigation.
*  I wish I had one.
*  It's cool.
*  So the kind of and common sense conception.
*  Right.
*  So things that aren't, you know, so chess or, you know, go is one thing.
*  But sort of conversationally appropriate chit chat over lunch is another.
*  Let's see.
*  There's a there are a lot of people working on this and they actually do use
*  Bayesian concepts.
*  A lot of base prediction.
*  That's right.
*  But are you optimistic about that?
*  I mean, you know, so what do you want to the questions what you want to
*  understand?
*  Do you want to understand the system that generates it or do you want to
*  understand how we work?
*  I guess I'm on the latter camp.
*  I'm in this not to press by the engineering solution, but I'm I'm in a
*  department of neuroscience and psychology because I'm interested in how
*  like our stuff is organized.
*  Yeah.
*  I mean, Richard Feynman famously had on his chalkboard when he died, it's
*  something to the effect of I do not understand what I cannot build.
*  Cannot build.
*  But building something doesn't mean that you do understand it.
*  I mean, yes, thank you.
*  So Feynman is wrong as rarely but occasionally.
*  Yeah.
*  So so so here we have deep nets where you are building, let's say, cognitive
*  function in some sense.
*  Look, I mean, forget the cognitive function.
*  So here's so here's a concrete case where I think the deep stuff could be
*  really useless.
*  We could learn from the stuff that the vision community has implemented
*  pretty successfully.
*  And maybe we could use that to solve one of the problems that, you know, like I
*  said earlier, why is it that we have such poor understanding of anatomy?
*  You know, as a tool.
*  Yeah.
*  So use it as a tool to learn some basic properties of the structure of that
*  thing that that's just been resistant.
*  Right.
*  So it makes some predictions.
*  So for that kind of exercise, feeding in a lot of data and doing some
*  classification and clustering super useful.
*  You can say, actually, I predict that, you know, you need to look for, you
*  know, nine things.
*  I mean, whatever turns out, it would give us a sort of heuristic device to
*  take a bunch of data and kind of somehow structure the search problem for us to
*  say, actually, this would be a reasonable subdivision.
*  And it might not have anything to do with, let's say, the macaque subdivision,
*  the bird subdivision, the, you know, whatever is going to be next, whatever
*  nonhuman primate is, you know, next on our list subdivision.
*  We just don't know.
*  We have to be.
*  This is why we want to be parochial.
*  You know, the human auditory system might have properties that are a little bit
*  different because of the incredibly rich interaction with the motor system and
*  the thinking system.
*  Right.
*  So a kind of multi stream model that I've worked on for many years as a kind of
*  fundamental principle of the speech and language systems, which we have any.
*  We're not even going to get have time to talk about the dual stream.
*  That's, you know, it's like your major, major contribution that people have
*  cited early cited often.
*  It's now that's sort of like the well, I'll tell you a brief story about that.
*  Just for fun.
*  The issue is that so I could imagine a very beautiful contribution to that
*  because, you know, what, you know, we all build on, we read the anatomy and
*  physiology from the monkey literature and say, OK, so let's assume that that's a
*  good model.
*  There's maybe tonal topic areas and this is their arrangement and there's core
*  areas and the belt area surrounding the core areas and so on.
*  But look, the human auditory system and it's, you know, in my runs have to do
*  slightly different things.
*  Namely, they have to create the infrastructure to link seamlessly to the motor
*  system, the speech motor system and seamlessly to the recognition and memory
*  systems that are very different in kind.
*  And so these are extremely different kinds of demands.
*  And so it stands to reason that the intermediate layers of analysis are quite
*  different.
*  So take a one.
*  Right.
*  So there's no reason to believe the primary auditory cortex is structurally or
*  functionally that similar to the primary visual cortex.
*  In fact, it's much more likely that the inferior colliculus is similar to V1.
*  So that's the kind of representational, you know, fine grain orthogonalization and
*  granulation of the problem.
*  A1 or, you know, that might be multiple areas because there's multiple targets
*  going to A1 might already be doing something quite different and kind in terms of
*  the, let's say, transformations it does on the inputs.
*  And so we have to look for different things.
*  And I could imagine a really amazing contribution of the deep net kind of
*  approach could be to make data driven suggestions or kind of heuristic, the
*  derived hypothesis about what to even look for.
*  Yeah, I like that.
*  You're really big and cool.
*  And if any graduates have ever listened to this, go run, do it.
*  Yeah.
*  You'll be rich and well, you'll be famous.
*  Maybe not famous.
*  You'll be a really great scientific contribution for a big chunk of the field.
*  It's like a good project.
*  Take a break.
*  A few deep breaths.
*  Today's quote of the show.
*  Within a generation, the problem of creating artificial intelligence will
*  substantially be solved.
*  That would be Marvin Minsky, 1967.
*  So you're but you're pessimistic about artificial general intelligence.
*  You were starting to say I'm pretty pessimistic about that.
*  There I hold it with my you know, with the fact that we just don't understand how
*  the mind works at all.
*  And so yeah, pattern matching and serves so simple.
*  I mean, also, you know, Bayesian predicted pseudo common sense, a mind not makes.
*  We don't even know the right questions to ask.
*  I think it's a problem.
*  Yeah, I think it's a I think that's just too.
*  I mean, I think it's a really it's obviously, you know, a big goal and it's kind
*  of a fun goal.
*  That's fun.
*  It's fictiony.
*  And I can get into what people want to do that.
*  But I just don't think it's it's just not right.
*  Just just work on something that we can actually get some traction on.
*  What I don't even know what it what it would look like.
*  How would we know if we built something that was generally intelligent?
*  I don't even know what that means.
*  I don't know what it means.
*  I don't know what intelligence means.
*  I don't know if it's a look.
*  I mean, like I said, I have problems understanding how you recognize a single word.
*  So, I mean, since I'm stuck with that, right, right, right.
*  You know, there's a seemingly banal problem.
*  I'm really hosed when it comes to artificial general intelligence and the and the problem.
*  So there are solutions.
*  So one of the properties of general intelligence, as far as I'm concerned, is the issue of
*  compositionality.
*  And there are some solutions for that.
*  But the problem of compositionality is just one.
*  And it doesn't just mean that you can, let's say, look up, concatenate and form a new
*  representation that has that because that takes on the interpretation of its parts
*  but in a joint sense, but also then that becomes an inferential step for the next.
*  I mean, it's very thought is a difficult thing.
*  Very, very difficult thing.
*  We started the thought.
*  Yes.
*  I maintain that thought is not a gimme.
*  Thought is actually a hard problem.
*  So let me I want to tell you that just because, you know, as a sociological point, should
*  there ever be a younger listener to this?
*  The thing about the dual stream, I think, is a sort of funny thing.
*  So this is a this is an idea that my friend and colleague Greg Hickok and I have worked
*  on since since actually around my dissertation.
*  Since the late 90s, we wrote our first paper on this in 2000 and another one in 2004 and
*  another one a little later.
*  And it's become it's become quite influential.
*  It's the standard.
*  It's the standard model now.
*  It's not.
*  It's not.
*  So here's the funny thing about this.
*  When we first wrote this stuff, basically.
*  So we know.
*  So the moral of the story is we never had any good years.
*  When we first wrote this and tried to publish it, people basically said to us, you know,
*  you guys are just you guys are nut jobs.
*  You don't know what you're talking about.
*  You're young and you don't know the field and you're just, you know, just very naive.
*  And it's kind of sad.
*  Hashtag sad.
*  They I mean, we had some pretty nasty commentary and we were we were youngish or whatever,
*  you know, and we're not so amused and didn't have a thick skin.
*  Right.
*  We're like, thanks a lot.
*  So but then eventually people like it.
*  Maybe it's not that dumb because look, it was a straight lift from vision.
*  Right. We just said, well, if this is a fundamental organization of cortical systems and this
*  is actually a useful computational subdivision, what would it look like for a language system?
*  So we thought, let's just kind of reason through it from the point of view of, you know,
*  lesion data, imaging data, physiology.
*  What would such a system look like?
*  And we thought, OK, it's not such a terrible idea.
*  Jesus.
*  It's just so first we got absolutely reamed.
*  We still have some of those old reviews.
*  Oh, good.
*  Yeah. Greg was reading these.
*  They were not fun.
*  And then so now we go to conferences and now we're like the old guys were like, well, that's
*  obviously the old school stuff.
*  I'm like, thanks.
*  When were the years when you were just saying we had a very quick you shade.
*  We had like, you know, hatred, brief acceptance and hatred.
*  So now basically it's become the sort of, you know, the model that you put up at the
*  beginning of your talk and say, well, here's the old standard model.
*  Now let me take some shots at what it's.
*  I mean, that's good.
*  It's kind of, you know, it's how progress should be.
*  But we were always like, you know, we wanted just one year or two of like, you know, happy
*  times.
*  Yeah.
*  How does that feel as that doesn't normally happen?
*  There is usually, oh, a decade, you know, where people get to win awards and things
*  for their awards.
*  I mean, you're like, not just like the old fart.
*  I mean, it's fine.
*  We're happy that it's, you know, it's been a very useful heuristic model and it's made
*  some, you know, it's made some progress and there's some support for it.
*  And there's some subparts that work well and others that don't.
*  Yeah.
*  So, I mean, we're still pretty attached.
*  I mean, I think it's probably wrong in an interesting way.
*  Oh, so yeah.
*  Yeah.
*  It's under specified to be sure.
*  I mean, there's no such thing as, you know, to, I mean, as in the vision case, we now
*  know, you know, there's way more organization to it.
*  But as the first cut of sort of subdividing again, it was very Marion inspired.
*  Like, how do you subdivide the computational problems if there are different processing
*  streams?
*  And we thought, well, if the visual case is sort of what, how or what versus where kind
*  of stream the way it was originally proposed by Jerry Schneider, I believe, for the
*  Anst.
*  Oh, wow.
*  And from the Caliculus, actually, multiple visual streams.
*  And then later on by Ungerleiter and Mishkin for Macaque Visual Cortex.
*  But it was really an older paper by Jerry Schneider that initially did the multiple
*  streams in vision.
*  Interesting.
*  And I think it's a 1967 science paper.
*  You know, that was the initial impetus for really thinking about this kind of segregation.
*  And then I think, you know, the more obviously the Mishkin and Ungerleiter things unbelievably
*  influential.
*  And we simply took that notion because it seemed to make a very sensible subdivision,
*  not just for vision, but possibly for perception in the language case, namely the interface
*  to production systems and the interface to meaning or, you know, representational structural
*  systems.
*  And then we just tried to rehearse the argument of what would follow from it, what would be
*  the parts.
*  And of course, you know, that was now 10 years ago or more.
*  More.
*  The kind of standard version.
*  We're now working on the next version, unsurprisingly.
*  And it's actually held up pretty well for now in terms of its empirical basis.
*  And there's not the general idea of this.
*  And that's probably just because cortexes are organized that way.
*  And we just happen to import the right metaphor from the vision case because it was, you know,
*  and it's probably just a very useful match between implementation and computation in
*  the sense that somehow evolution has figured out, look, these very broad problems are best
*  solved by specializing yourselves to do this or that.
*  Like maybe this bunch of cells is really good at coordinate transformation and some kind
*  of basis function of this or that.
*  And that seems like a really old idea in terms of evolutionary mechanisms.
*  And so the fact that it would be recycled is in retrospect not that surprising.
*  I have this, I don't know, I've been, you know, everything seems dual and there's no
*  reason why it needs to be just dual.
*  At some point, a process has to split in two, but then it can keep splitting.
*  That's true.
*  And it probably does.
*  But I mean, let's say in the visual case for a while, there was also, there was the
*  trull thing, right?
*  There was a third stream in the visual case.
*  But maybe there is sub-splitting.
*  I mean, I think that the two thing is just a really broad subdivision.
*  And I think you're absolutely right.
*  So for instance, in our case, the dorsal stream stuff, I've worked a bunch on that in the
*  last couple of years, actually, with some of my friends here.
*  And we have a lot of stuff to say about subroutines that are supported by that.
*  So you're quite right.
*  It's not that it's a monolithic kind of, you know, chunk of wires.
*  I mean, there's subparts responsible for different things, but arguably, well, they
*  share at the very least the same or at least partially the same origin and maybe some
*  overlapping things in terms of the targets.
*  But it may be that, for instance, you know, just anatomically, there's no dorsal
*  stream.
*  There's like three or four.
*  Yeah, right.
*  And they have different origins, right?
*  It's different if you're, you know, if you originated in the middle temporal
*  gyrus or more, you know, a little bit more posterior than that, you know, that means
*  your input is quite different into whatever, I don't know, you know, whatever gets sort
*  of read out at the other stage.
*  Is it more dorsal premotor cortex?
*  Is it more into, you know, conventional Broca's area, whatever that is, and so on and so forth.
*  So there's no sense that there's no monolithic thing at all.
*  It's just totally fractionated.
*  See that that's the problem.
*  The brain is complex.
*  Let's just quit and study deep learning.
*  This is probably I mean, maybe that is an I mean, the complexity is disheartening because
*  every time you look closer with a new machine, you find there's like 20 more things to look
*  at.
*  Don't look closer.
*  Don't look any closer.
*  Exactly.
*  Yeah.
*  Every time you look closer, it's like, oh, it was pretty good when we just had dendrites.
*  Now we have spines.
*  Yeah.
*  And then the locus of activity becomes the smaller thing always.
*  Right.
*  So if you're a vision person, you now work on the spines of the B1 neuron.
*  That's right.
*  We're going to get down to atoms.
*  You'll see.
*  So yeah, this is so I can hear John Krakauer just seething right now.
*  Nonsense.
*  You don't need the vaguest idea.
*  You don't need to know what neurons are doing.
*  So that was my poor impersonation.
*  So this has been a long time and I, you know, we didn't even get into your music research.
*  I want to talk about your what you used to call.
*  Let me I want to pull it up because you call it the maps and mapping problem, which kind
*  of touched on a little bit.
*  And you used to call it the granularity.
*  Oh, what the granularity mismatch problem and the ontological incommensurability problem.
*  Those are those are that's some serious shit.
*  That is some serious shit.
*  That's I mean, I can give you a quick.
*  So things that I care about in terms of so this this issue of this issue with these pretentious
*  words, right.
*  So let me unpack them a little bit.
*  So some years ago, my friend Dave Enbeck and I wrote a couple of papers about this because
*  we were thinking quite seriously about again, you know, from a slightly more inspired perspective
*  about how do you link what we've learned in psychology and particular linguistics as a
*  cognitive science versus the neuroscience language.
*  And there there's two issues we have.
*  You know, we tried to grapple with one which we called the granularity mismatch problem
*  is exactly that just the grain size of problem that people in linguistics work on versus
*  the people that neuroscience of language work on is hugely mismatched, hence granularity
*  mismatch.
*  Right.
*  So people in the neuroscience of language do experiments on like, can I find words or
*  can I you know, is there a difference between phonology, syntax and semantics or something
*  like that, which is relatively coarse grained.
*  People who work, you know, who work on linguistics know something about the details.
*  Languages across languages work on extremely subtle issues across languages that are that
*  are extremely fine grained in their nature.
*  And so the question is, and that's to us, that was more of a practical problem.
*  That is, if neuroscientists and linguists work more productively together, and then
*  this is a this can be solved.
*  That is, linguistics gives you extremely useful hypotheses, actually.
*  And then you hold their feet to the fire and say, and that doesn't mean that the doesn't
*  mean it has to be reduced.
*  There's no sense of reduction.
*  That's just has to mean, you know, we have good evidence for this kind of stuff and we
*  have good evidence for that.
*  How can we operationalize the question so we get meaningful measurements in the middle?
*  That's a kind of practical issue.
*  The more problematic issue is what we were talking about earlier, too, which is what
*  we call the ontological incommensurability problem.
*  And that is a more that's our kind of philosophically deeper problem, which is just a fancy way
*  of saying mind body problem.
*  Right. That is the ontological commitments you make in psychology, computer science,
*  cognition or whatever, are very different to the ones that you make in neuroscience,
*  which is stuff.
*  It's the stuff of neuroscience is stuff like neurons, you know, dendrites, receptors,
*  oscillations, spikes.
*  There's a there's a parts list.
*  The parts list of the cognitive sciences are especially in terms of language is very different
*  units, let's say morphine or, you know, syntactic relay.
*  I mean, it has different primitives and different primitive operations.
*  Yeah.
*  The question is, are those so different in kind that there is no linking hypothesis that
*  we can even think of?
*  So they're ontologically incommensurable.
*  And if that's true, then we're toast.
*  Now, I don't believe that to be true, because I believe that the brain is the part of the
*  body that does the language part and not the knee or the liver.
*  But we're stuck on that because we have equally good reason to believe that linguistics has
*  given us very good primitives, you know, whether from cognitive science, computer science,
*  language.
*  And we have reason to believe that neuroscience has given us good primitives.
*  So the linking hypothesis problem is non-trivial to say the least.
*  And so that's an exercise for the future.
*  But the maps and the mapping problem is just a version of that.
*  So for me, what we work on in our day to day work as neurobiology languages, the map is
*  making maps because we're all seduced by maps.
*  We want to have a V1 is here, V2 is here, MT is over there, and you know, primary atherocortices
*  is there.
*  And we have often basically adopted localization as explanation and localization is not explanation.
*  Is that still a problem?
*  You think it was a problem?
*  It's getting better.
*  I mean, you know, there's plenty of talks where you see a bunch of localizations.
*  It feels good to see a blob light up.
*  Yeah.
*  And it feels that sort of intermediate level of understanding.
*  But what needs to be said is this is just the beginning of the research, just like the
*  correlation.
*  This now tells me this is where I got to look into the real experiments now.
*  So the maps problem is something to do, you know, can we do better characterization?
*  What we were talking about earlier about getting a really good anatomic description of the
*  human auditory cortex.
*  That's a maps problem that requires good technique, good research thinking about how to do it.
*  What's the right level of characterization?
*  You know, maybe it's some kind of weird laminar thing.
*  And who knows?
*  That's kind of doing good systematic kind of nuts and bolts anatomy.
*  Really useful, really important.
*  But that's making maps.
*  It's a practical problem, solvable.
*  The mapping problem is the same as I just talked about, which is how do you map a level
*  of representation onto another level of representation?
*  And so that's making mappings from, let's say, the cognitive sciences to the neurosciences.
*  That's or as it was 100 years ago or more, how do you map from chemistry to physics?
*  And as we know, famously, it wasn't a case of reduction.
*  It was a case of that physics had to change its conceptual fundamental commitments to
*  accommodate the facts of chemistry.
*  So it was the fact that the unification or change in the other direction.
*  So not reduction, but actually anti-reduction.
*  And maybe to have really unified neurobiology of language, we actually need conceptual change.
*  We need to figure out whether the primitives of neuroscience and the primitives of linguistics
*  are even right at all.
*  Some poor graduate student of mine has to deal with that.
*  It's tricky business for real, but it's an exciting problem.
*  It's a deep problem.
*  It's a variety of the mind-body problem.
*  It's one of the most exciting things in intellectual history.
*  I want to know.
*  I want to understand.
*  What do you think?
*  So I ask this sometimes at I don't go to cocktail parties anymore, but I've social gatherings
*  or something.
*  Beer parties.
*  Yeah, beer parties right before my keg stand.
*  I ask the.
*  So we.
*  OK, so let's say slavery, right?
*  That's bad.
*  Slavery is bad.
*  If we sort of take the bird's eye view and we think, OK, we've got that solved, but it's
*  kind of embarrassing that we ever did it.
*  Right.
*  And you know, let's say women's rights, you know, things like that.
*  What are we doing right now?
*  And this can be in the world of science and figuring out brains or just in general, you
*  know, whatever you're thinking.
*  What are we doing right now that our descendants are going to look back on and think, Jesus,
*  what?
*  Why?
*  How do they even think that was OK?
*  And, you know, it can be about understanding ourselves, too.
*  Yeah.
*  I mean, so there let me say something about I mean, so I have a long list of things, sciencey
*  things here, but let me actually deviate a bit from your script.
*  I think that people should be now and later will say we're doing a shitty job on is how
*  we treat younger people and trainees, how we publish stuff that is going to be looked
*  on as absolutely appalling.
*  The way we discourage the way the system is organized to discourage people from wanting
*  to do something that's hard and not well paid and ultimately very important.
*  The way we have set up reward systems through grants and publications that do nothing but,
*  you know, reward the wrong instincts.
*  I mean, it's a very it's a system that's just absolutely shocking.
*  And I think in 20 years or maybe 50 people are going to say, well, you guys lost generations
*  of wonderful, creative, exciting scholars, but by putting them into this app, you know,
*  ridiculous system of what counts as success and what counts as what the meritocracy is
*  about and how you publish and how you assign beans.
*  You see, you're preaching to the choir.
*  This is like my calling.
*  This is why I left.
*  Part of the reason why I left.
*  Get out of the game.
*  Yeah, you got to get I mean, I think that's one of our biggest problems.
*  That's not for our science, not just for neuroscience or cognitive science.
*  That's, I think, really across a bunch of sciences.
*  And I say that as someone I care a lot about my trainees here and at the Max Planck Institute,
*  my two job gigs, I try to do my best to support them and to help them find jobs and to not be an unwavering advisor.
*  But all good intentions pave the way to hell.
*  I mean, we do our best and we say, look, you know, you should just follow your hunch.
*  You're doing an exciting experiment.
*  I'm really, you know, really cool.
*  The results you're sharing with us at the end of the day, we say, look, you know, really better publish that in this kind of journal if you want to jump.
*  Yeah. Yeah.
*  I mean, come on.
*  Really, that's our that's like the way we set this up.
*  You know, it's not about ideas and, you know, looking forwards and thinking thinking forwards.
*  It's about totally accommodating to some kind of weird, you know, set up by my generation and the generation in front of me, you know, imperialism of how to do science.
*  Well, there has to be there has to be some system, right.
*  But I mean, so a lot of people hide in academia because you don't actually need to do anything often.
*  If you don't know what else to do in your life, you can stay in school, essentially.
*  Right. So there's and and high.
*  To some extent, that's not uniformly true.
*  You have to there's some luck required to actually get that job for the long term.
*  It's true that there's too many people who are but it's not I mean, you can't just say, hey, I'm here, you know, sign me up.
*  But the efficiency of science is you see a lot of wasted efforts.
*  Yeah, a lot of wasted effort.
*  And just I mean, to me, the most discouraging is the well, the extent to which we're discouraged.
*  I mean, we're discouraging smart people, you know, and maybe a good example.
*  And people who were committed and excited and, you know, good at the work and lab and good thinkers because the system is set up to, you know, to beat you down and not to make it a joyous experience.
*  Right. So that's, you know, I don't know what to and I have, you know, in sort of a sense of self irony, where's my little sticker?
*  Here's a friend of mine gave me that, you know, there's a there's a famous play by David Namet called Glenn Gary, Glenn Ross.
*  There's a there's a good movie adaptation of this with Alec Baldwin giving this monologue about, you know, how crappy all these realtors are.
*  And he gives us amazing monologue.
*  And it starts with the line that you get your crumpled up paper.
*  So Jack Lemon is standing getting himself a coffee.
*  And Alec Baldwin says, put the coffee down.
*  Coffee is for closers.
*  I have the coffee that are lying around everywhere.
*  That's a coaster, huh?
*  For your coffee.
*  Coffee is for closers.
*  Coaster is everywhere.
*  And partly, you know, and it's sort of ironic, but not right.
*  I mean, it's funny and ironic.
*  But the fact of the matter is that is the thing.
*  If you can't close and be an integrate yourself into a system that we've set up, the chances of success now are minuscule.
*  And that's it is what it is.
*  But are we going to stand for that?
*  You know, how are we going to know how am I supposed to?
*  And I I want to do right by my peeps.
*  You know, I love the people in my lab.
*  Fabulous.
*  My lab is wonderful researchers and I learn a ton and they're fun to discuss with and the ideas are cool.
*  But I can't find I can't guarantee everyone a successful future of scientists.
*  It's just not possible.
*  No matter how much I support them and want them to succeed.
*  It's just you need luck.
*  You need familial support.
*  You need champions who who in the field who reach out to other people and say Paul's work is the best.
*  If you don't, it's a huge mistake not to get Paul.
*  You need that.
*  You need way more family support or partner support than people are aware of.
*  Or or you reject the system and forge your own path like Paul is doing.
*  I think extremely I think that is that's actually an absolutely reasonable and it's not just courageous.
*  Those are reasonable and actually can yield can lead to actually quite happy existence going down a different.
*  See, I hope so.
*  It's hard as hell right now.
*  But I know.
*  But you're you're doing cool stuff by basically talking about science and educating other people about it.
*  And that will you know, you're sort of paying it forward.
*  That will come.
*  That will be rewarded.
*  And some it'll it'll happen for you.
*  But it's like presumably takes a while.
*  But I think it's the right I think it's absolutely the right thing to do.
*  So I think, you know, it's the it's a high risk, high reward scenario for you.
*  I think it's there.
*  I'm optimistic because nothing is more important than kind of educating people about science stuff and letting them meet scientists because people think we're these weird people.
*  We're just you know, I also go home and I have three kids.
*  And you know, and I whine about, you know, laundry in school and, you know, how shitty people are.
*  Whatever.
*  We're all those whiners.
*  Yeah, yeah, sure.
*  It's all tough.
*  It's always tough.
*  Yeah.
*  I think I get to know people is I'm in half the battle of doing this kind of thing that you're doing.
*  It's just introducing people say these are just people they're doing.
*  They're working on this side or the other thing.
*  Hopefully you get a glimpse of the work.
*  The work of the person.
*  And just it's not that it's sort of a demystification exercise, which I think is extremely useful.
*  I do too.
*  Yeah.
*  So, David, thanks for spending so much time with me.
*  I appreciate what you do and the way that you approach your science.
*  It's slow.
*  It's curmudgeonly.
*  It's curmudgeonly.
*  But it's wonderful.
*  And, you know, hopefully in the future we can have you back on and talk a little bit more deeper, more deeply about some of the things you're actually doing here.
*  That would be great.
*  It'd be fun to do it again alone or with somebody else.
*  It's fun to talk about work.
*  You and John on at the same time.
*  So that would be fun.
*  Follow David on Twitter.
*  He is at David Popple.
*  And of course, you can look at the show notes for that as well.
*  Last thing, David, I know that you have a side passion here.
*  What and you just brought up Glenn Gary, Glenn Ross.
*  What is your dream directorial debut, directorial debut?
*  My dream directorial debut?
*  Yes, I wanted to be a director instead of a scientist.
*  That was actually my dream career.
*  And it's not too late.
*  I suppose what I would really like is something like what I'd like to direct is something like Heiner Mueller's quartet, you know, an adaptation of the famous liaison dangereuse, right?
*  The book by the novel by a show that they like called Liaison Dangereuse, famously remade as a movie with Michelle Pfeiffer, but adapted by the East German playwright, Heiner Mueller or high level of called quartet.
*  Funny, savage, linguistically brilliant, exciting and with a lot of room for directorial shaping.
*  But, you know, now I'm a director of an institute.
*  That's good, too.
*  Yeah, that's pretty good.
*  But for all you higher up executives involved in plays that are listening to this show, go ahead.
*  I'm up for directing and I'm happy to do it and it wouldn't suck.
*  Yeah.
*  All right, David, thanks.
*  Thanks for your time and we'll talk to you soon.
*  Absolutely. Thanks, Paul. Good to talk to you.
*  Brain inspired is a production of me and you.
*  You can support the show through Patreon for a microscopic two or four dollars per month.
*  Go to brain inspired dot co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show and prohibit any annoying advertisements like you hear on other shows.
*  To get in touch with me, email Paul at brain inspired dot co.
*  The music you hear is by the New Year.
*  Find them at the New Year dot net.
*  Thanks for your support. See you next time.
*  You.

---
Date Generated: November 12, 2024
Transcription Model: whisper medium 20231117
Length: 5704s
Video Keywords: []
Video Views: 232
Video Rating: None
Video Description: Tony Zador discusses why he's excited about how neuroscience can help "catalyze" the next generation of artificial intelligence.

Show notes: 
https://braininspired.co/podcast/198/

Patreon  (full episodes and Discord community: 
https://www.patreon.com/braininspired

Apple podcasts:  https://itunes.apple.com/us/podcast/brain-inspired/id1428880766?mt=2
Spotify:  https://open.spotify.com/show/2UZj8c8Ap5oc2gh2rJxLLe

The Transmitter is an online publication that aims to deliver useful information, insights and tools to build bridges across neuroscience and advance research. Visit thetransmitter.org to explore the latest neuroscience news and perspectives, written by journalists and scientists. 

Read more about our partnership.

Sign up for the “Brain Inspired” email alerts to be notified every time a new “Brain Inspired” episode is released: https://www.thetransmitter.org/newsletters/

To explore more neuroscience news and perspectives, visit thetransmitter.org.

Check out Tony's essays in the Transmitter:

NeuroAI: A field born from the symbiosis between neuroscience, AI: https://www.thetransmitter.org/neuroai/neuroai-a-field-born-from-the-symbiosis-between-neuroscience-ai/

What the brain can teach artificial neural networks: https://www.thetransmitter.org/neuroai/what-the-brain-can-teach-artificial-neural-networks/

Tony Zador runs the Zador lab at Cold Spring Harbor Laboratory. You've heard him on Brain Inspired a few times in the past, most recently in a panel discussion I moderated at this past COSYNE conference - a conference Tony co-founded 20 years ago. As you'll hear, Tony's current and past interests and research endeavors are of a wide variety, but today we focus mostly on his thoughts on NeuroAI. 
So, we're in a huge AI hype cycle right now, for good reason, and there's a lot of talk in the neuroscience world about whether neuroscience has anything of value to provide AI engineers - and how much value, if any, neuroscience has provided in the past. 
Tony is team neuroscience. You'll hear him discuss why in this episode, especially when it comes to ways in which development and evolution might inspire better data efficiency, looking to animals in general to understand how they coordinate numerous objective functions to achieve their intelligent behaviors - something Tony calls alignment - and using spikes in AI models to increase energy efficiency. 
If you like written essays, by chance Tony has written two essays, on the past and the future of NeuroAI, which are available on the Transmitter website and I think nicely complement our discussion on this episode. I'll link to those essays in the show notes, where I also link to a couple of the papers we discuss, and Tony's previous BI episodes. 

0:00 - Intro
3:28 - "Neuro-AI"
12:48 - Visual cognition history
18:24 - Information theory in neuroscience
20:47 - Necessary steps for progress
24:34 - Neuro-AI models and cognition
35:47 - Animals for inspiring AI
41:48 - What we want AI to do
46:01 - Development and AI
59:03 - Robots
1:25:10 - Catalyzing the next generation of AI
---

# BI 198 Tony Zador Neuroscience Principles to Improve AI
**Brain Inspired:** [November 11, 2024](https://www.youtube.com/watch?v=9C0qkxu0UyE)
*  In fact, I'll go as far as to say, as far as I can tell, Transformers are almost a counter
*  example to the successes of neuro AI in that they bear, as far as I can tell, very little
*  resemblance to anything that I expect to find in the brain.
*  I'm particularly interested in three sort of large questions about, you know, where
*  you can hope to gain insights from biology, from neuroscience and port them over to artificial
*  systems.
*  And alignment is sort of, in some sense, the most fundamental.
*  You know, this is crazy, a crazy amount of flexibility.
*  And so how does that happen?
*  I mean, we don't know the details, but the answer is, I think, that there is a developmental
*  process, you might even call it a developmental curriculum.
*  This is Brain Inspired, powered by the transmitter.
*  Hello, I'm Paul.
*  I do neuroscience things at Carnegie Mellon University.
*  Tony Zador runs the Zador lab at Cold Spring Harbor Laboratory.
*  You've heard him on Brain Inspired a few times in the past.
*  Most recently in a panel discussion that I moderated at this past COSIGN conference,
*  a conference that Tony co-founded 20 years ago.
*  As you'll hear, Tony's current and past interests and research endeavors are of a wide variety.
*  But today we focus mostly on his thoughts on neuro AI, roughly the interplay between
*  neuroscience and artificial intelligence.
*  So we are in a huge AI hype cycle right now, and for good reason.
*  And there's a lot of talk in the neuroscience world about whether neuroscience has anything
*  of value to provide to AI, and how much value, if any, neuroscience has provided in the past.
*  Tony is team neuroscience in this regard.
*  You'll hear him discuss why in this episode, especially when it comes to using biological
*  processes like development and evolution to improve data efficiency in AI models.
*  Also looking to animals in general to understand how they coordinate their numerous objective
*  functions to achieve their intelligent behaviors, something Tony calls alignment, and using
*  spikes in AI models to increase energy efficiency.
*  If you like written essays, by chance Tony has written two essays on the past and the
*  future of neuro AI, respectively.
*  And those are available on the transmitter website, and I think they nicely complement
*  our discussion on this episode.
*  I will link to those essays in the show notes, where I also link to a couple of the papers
*  that we discuss, and Tony's previous brand inspired episodes.
*  Thank you to my Patreon supporters.
*  I think we need to have a discussion in the near future, maybe some sort of live discussion.
*  I'll be on Discord soon to probe your interest in what topics we might talk about when we
*  meet next.
*  If you want to support brand inspired through Patreon, just go to brandinspired.co and you
*  will find a link to the Patreon there.
*  All right, here is Anthony, Tony, Zador.
*  Hey, first, I just upfront, I just want to thank you for hooking me up essentially with
*  the good folks at the transmitter.
*  I'm so glad that worked out.
*  Yeah, I mean, just such a not random occurrence, but you and I were passing at cosine in the
*  hall and just chatted for a minute.
*  And the next thing you know, I'm speaking with Emily at the transmitter.
*  It's just all really worked out.
*  So I'm really grateful.
*  So thank you.
*  I'm glad that worked out.
*  I think I thought it would be a good match.
*  So you have Nicys coming up.
*  I'm not going to be able to be there, but I will see you maybe a month later in Bethesda
*  at the brain neuro AI workshop.
*  Oh, nice.
*  Which you're just you're all over the place.
*  You're organizing all sorts of neuro AI stuff.
*  That's right. I think I think this is the time for are we officially interviewing now?
*  Yeah, sure.
*  We didn't we didn't have a transition.
*  Yeah. Yeah, I hope this is Tony.
*  Tony, thank you for being on.
*  Welcome. I appreciate you being on.
*  Sorry about that.
*  Yeah, yeah, yeah.
*  I'm I'm pretty excited about neuro AI these days, both, you know, the work that I'm doing
*  myself and sort of the broader field and seeing what other people are doing, getting people
*  with these shared interests together in a variety of settings.
*  So the Nicys meeting, the NIH meeting, which brings together not only a bunch of researchers,
*  but also, as they say, stakeholders, various branches of government funding agencies,
*  NIH, NSF, a couple of others.
*  And then there's.
*  There's also one coming up at NURPS.
*  So, yeah, you know, that's only in the next two months.
*  Right. I know it's all over the place that you may be the most excited person about neuro AI
*  that I know.
*  Actually, I was just on a boat in Norway at a neuro AI workshop, and at the very end, I
*  had I was tasked with.
*  I thought I thought they couldn't hold on without inviting me.
*  What? I was surprised.
*  I was surprised to say the least.
*  I was assuming that I am.
*  I am hurt. Yeah, no, I'm hurt.
*  There was a yeah, there was a no Tony rule for sure.
*  But but I sort of pulled the participants.
*  There was about 30 people like whether they liked the term neuro AI.
*  And a few of them were very.
*  Advocated for it somewhat passionately, which I was surprised by.
*  Of course, some people don't like it, but how is it sitting with you?
*  I mean, you love the term, right?
*  You know, honestly, I wasn't a big fan at the beginning.
*  Um, it was actually.
*  Like five years ago or so that I started that actually somebody I was working with here
*  at Cold Spring Harbor, who is trying to help me put together a program here at Cold
*  Spring Harbor on neuro AI, sort of we tossed around various ideas.
*  And I think she can take Kat Donaldson, who's no longer here at Cold Spring Harbor.
*  But I think she can actually take credit in at least from my point of view of really
*  getting me to land on that as the term, because I had to write a couple of proposals.
*  And I was using these like three or four word phrases, the intersection of neuroscience
*  and AI, and she's like, that is just so clumsy.
*  That is just so awkward.
*  So I actually did a Google Scholar search a couple of weeks ago to figure out when the
*  earliest occurrence was.
*  And there's been a tremendous uptick.
*  There's essentially no occurrences of the term going until sort of the mid to late 2010s.
*  There are a handful, but it's often used to mean something different, actually, something
*  closer to what we would call, you know, what these days is called something like, you
*  know, brain machine interface or brain computer interface.
*  To the extent that it was being used, you know, 20, 30 years ago, apparently, that's
*  that's how people were using it.
*  I mean, part of my hesitation in adopting it, I agree it is the least clunky, clumsy
*  way to say it. Right.
*  And it's kind of clear what it means, I think.
*  But part of my issue is, you know, even in the early days of AI was a John McCarthy who
*  turned who turned at artificial intelligence.
*  I think that's right. It was that meeting.
*  That he organized. I'm not sure who actually coined it.
*  There was like a 50 1956 Dartmouth meeting on what is now called AI.
*  But maybe it was him who disliked it.
*  There were some people who disliked the term.
*  And I appreciate that going back.
*  So there's kind of been not controversy, but there's some been some debate on whether
*  it's artificial intelligence itself is a good term to use.
*  And I'm sort of on board with that criticism.
*  Yeah. I mean, when I was a kid, when I was in graduate school, AI was the the the
*  boogeyman. AI referred exclusively to symbolic AI.
*  Right. And by contrast, the thing I was interested in was artificial neural networks,
*  computational neuroscience and machine learning.
*  And very few people in my circles would have described what they were doing as AI.
*  What they would say is that what they were doing was the opposite of AI.
*  And so it's it actually took me a while to start even being willing to say that what
*  I'm interested in is AI.
*  What would they would they call it connectionism?
*  What would the term?
*  Well, yeah, it's funny.
*  So the term connectionism was more specifically for a particular subset of of people who did
*  who did neural networks, the people who came sort of more from the you know, it's the PDP
*  books, the people who came from mostly from psychology and who wanted a connectionist
*  of human cognition.
*  Right. They wanted to.
*  So and again, we could we could sort of talk about all the substreams and the various
*  approaches. But, you know, the the the you know, part of the research program there was
*  to jump to skip rule based approaches, for example, in understanding verb conjugations.
*  And to use a so-called connectionist approach.
*  And there was a lot of debate and sort of the cognitive science literature about which
*  of those is right.
*  So you've seen that historically developed in and you've made your own transition into
*  accepting the term.
*  Yeah, less right.
*  But but so why why are you particularly excited these days?
*  I mean, I know it hasn't it wasn't last week that you were talking about the term
*  but hasn't it wasn't last week that you became excited.
*  But because this has been a while now.
*  Yeah, so, I mean, my own trajectory was that when I was starting graduate school and I
*  was in graduate school, sort of late 80s, early 90s, I was excited really about what
*  at that point was one field, which was computational neuroscience slash artificial
*  neural networks.
*  They were two sides of the same coin.
*  And there the idea was that you would build models of how neural circuits compute.
*  And then you would extract your understanding of what you thought or your beliefs, you
*  would abstract your beliefs about how you thought neural circuits computed and apply
*  them to build better machines.
*  And so there was no really especially in the late 80s, early 90s, when I started getting
*  involved with this, there was no clear distinction between those those two.
*  Right. And so what I was excited about was both sides of it, because there was a long
*  tradition in neuroscience of using quantitative models.
*  And that was certainly part of computational neuroscience.
*  But typically, those models were not constrained by the recognition that neural
*  circuits not only have dynamics and have behavior, but they have to actually perform
*  a function. They have to enable the organism in which the circuit is embedded to solve
*  a problem. And I think it was really that constraint that was was really crystallized
*  in but by sort of the early neural network.
*  Combination or meeting with with computational neuroscience.
*  So, you know, sort of very naively, I would say that, you know, if you asked a lot of
*  people who worked on vision and this is this is now before my time.
*  And so I'm actually I was just recently trying to talk to people who were around, you know,
*  back then to see if my sort of inference about the history is true.
*  But my belief is that, you know, a lot of the early vision scientists, you know, the
*  people who were inspired by Hubel and Weasel didn't really see that there was a hard
*  problem underlying vision. Right.
*  They thought that the in the same way that, for example, the you know, the early
*  people who started working with computers thought that, OK, chess was going to be hard,
*  but getting getting a computer to control an arm to pick up a chess piece was going
*  to be easy. And that turned out, obviously, even by the early 60s to be false.
*  But I think that vision scientists took a while to to recognize that the the circuits
*  they were studying were doing something really hard.
*  And so, you know, the research program that I see based on published work following from
*  Hubel and Weasel, you know, through the 60s, 70s and 80s was let us identify the
*  representations in different brain areas of visual scenes.
*  And that will be an explanation for vision.
*  Oh, right. Like, are you talking like the like neocognitron kind of days or?
*  Well, no. So that so that is an exception, right?
*  Because that is somebody who's actually saying, OK, let's take what we believe is
*  happening and put it together and see if we can build an artificial vision system.
*  I'm talking on the physiologist side, right?
*  Yeah. But that sort of has kind of stayed with us, right?
*  I mean, that's it's not like that has really left altogether.
*  I don't. I mean, I think that there I think you would be hard pressed to find, you
*  know, a visual physiologist who does not recognize that vision is a hard
*  computational problem. They might say, look, what I can contribute to it is a
*  characterization of neuronal receptive fields.
*  And I'm going to I'm going to characterize those receptive fields and because that's
*  what I can do.
*  And I'm going to tell a story about the role that these receptive fields might play
*  in visual processing.
*  But, you know, I think it would be very naive for a modern visual neuroscientist
*  to think that that by itself was the answer.
*  Right. Because. Right.
*  Like when I was in graduate school, one might have imagined that, well, you know,
*  it's pretty straightforward. You build a system with these receptive fields and
*  you've got a working vision system.
*  And the reason we haven't been able to do that so far is we just haven't bothered
*  we haven't had enough engineers.
*  We didn't have enough computer power.
*  Right. And you know that, you know, 30, 40 years ago, that might have been a
*  viable argument. But now we know that, like, if you try really, really, really
*  hard and devote lots of computer power and lots of engineers, you get something
*  now that works pretty well.
*  But for a long time, you didn't.
*  It remains a hard problem.
*  Well, and in those early days, it was all Gabor filters also.
*  And as directions in the in the receptive fields.
*  And it's like, can you build up to vision from Gabor filters?
*  Yeah, exactly. Right.
*  Like, basically, you would you would break the problem into, you know, 12 or 24 or 50
*  subproblems, solve those into individually.
*  Right. Like shape from shading and, you know, optimal.
*  I can't tell you how many papers I read at various times about, you know, different
*  variations of optimal edge detection.
*  Right. So part of the reason you're excited is because because of that history of.
*  Thinking that it was an easier problem than it turns out to be.
*  Well, it got me excited.
*  So when I was in graduate school, I thought I could do both things.
*  I thought that I could simultaneously
*  learn about neuroscience and develop better,
*  you know, take what I learned and apply it to building better systems.
*  By the time I got to doing a postdoc,
*  I decided that you kind of have to pick one at that point.
*  The the interest within the neural.
*  Well, in first of all, interest in neural networks was beginning to wane a little bit.
*  But more relevant to me,
*  I felt like that.
*  There were real opportunities to learn more about neuroscience,
*  and I felt like I should just take this approach that I had
*  and do the right neuroscience experiments.
*  And so I retooled as a pure experimentalist or as an experimentalist
*  driven by theoretical and computational questions.
*  And for, you know, my postdoc, I worked on synaptic physiology.
*  Now, you know, I still was interested in quantitative approaches. I
*  there was an excitement at that time about
*  using information theoretic techniques pioneered by Bill Bialik.
*  And so I was pretty excited by those.
*  How do you think about those?
*  What do you think about information these days?
*  Well, I think I still it is the core of how I approach problems.
*  I think the exercise of measuring information,
*  which is what a lot of us, including me, were doing at that time.
*  It is it is.
*  Useful for thinking clearly
*  about how collections of neurons represent
*  information, at least their capacity to their capacity to do so.
*  Yeah. Yeah. There are lots of limitations to it.
*  But I think it the actual numbers that you get out turn out to be boring
*  and sterile. And I guess that's that's sort of the complaint
*  that people have is that what's for me compelling is, you know,
*  the framework, the way of thinking about the world, the recognition that,
*  you know, among other things, if you're going to process information,
*  that information has to be propagated and transformed.
*  And yeah, right.
*  So you have the bits and then what the hell do you do with them?
*  Is the that's right. That's right.
*  So it's sort of part of the problem.
*  I mean, it addresses part of the problem that that we have in the nervous system.
*  I guess, you know.
*  One thing that changed for me
*  and I think for a lot of the field was that back then, a lot of us were focused
*  more on sensory processing.
*  And so information theory is covers a lot of how you
*  take information in from the outside world and you represent it.
*  How do you characterize those representations?
*  What it left out
*  was something that I didn't come to until really
*  I started my own lab, which was the recognition that, you know, animals behave.
*  This is not a shocker.
*  But back back then, many of us were studying
*  anesthetized animals. Yeah.
*  And so the behavior that you get out of an anesthetized animal
*  is usually somewhat less interesting.
*  And if it's can I just pause there for a second?
*  Because there are so many instances and I can't think of one,
*  an episodic memory of one where people point to historical
*  experimental work like anesthetized animals. Right.
*  And then they say, talk about how it was a necessary step
*  to get to where we are these days. Right.
*  Using different animal models, using them in controlled experiments
*  versus natural, et cetera.
*  Do you I mean, do you think that that's true in this case
*  with the anesthetized animals?
*  I mean, I think people going back to ancient
*  history, ancient philosophers have asked whether, you know,
*  any particular path through history is an inevitable path. Right.
*  Like, so was it inevitable?
*  I mean, I'm not sure it was inevitable, but to this day, right.
*  There are experiments that are I mean,
*  let's even go more extreme for my postdoc.
*  I studied brain slices. Yeah. Yeah. Right.
*  We certainly can learn a lot of things in brain slices that
*  would have been hard to learn in the intact preparation,
*  especially back then.
*  You know, a crazy thing is that when a neuroscientist
*  refers to an in vivo prep,
*  we refer to one in which the brain is still inside the skull.
*  If a biochemist refers to an in vivo prep,
*  they are talking about one in which all the proteins are still inside
*  the cell membrane. Right.
*  I mean, so, you know, different preparations for different questions.
*  I think what.
*  You know, so I'll never I'll never ding a preparation.
*  I'll never ding. I'll never I'll never, you know, find fault with a line of research.
*  I think what gets problematic is when the community
*  forgets that this is a model,
*  this is a limited model of something. Right.
*  And, you know, when the community becomes sufficiently large,
*  it begins to talk only to itself.
*  And then.
*  Those questions sort of take on a life of their own
*  that is independent of sort of how they were originally formulated
*  as part of sort of an overall research program for a field of,
*  you know, I would characterize it as understanding
*  how brains work to control behavior. Right.
*  Or how how I mean,
*  there are lots of different ways of characterizing it,
*  but I don't think that most people when they started their careers
*  were would have have honed in on the representation of a static visual image
*  in the anesthetized brain of a cat as sort of the central question
*  that they wanted to set out to answer.
*  Like that is a super useful question.
*  That is a super useful question to answer.
*  And it's great to have a model system where lots of people agree on the preparation.
*  You can really make progress.
*  But ultimately, that I don't think was the fundamental question
*  that drove all these people to work on that preparation.
*  It was sort of a model of a larger question.
*  Things like how do you represent the world outside of you?
*  And then probably people were asking, you know, the original people who
*  wanted to know how do those visual representations get used by the animal
*  or what is thought? Right.
*  Things like that.
*  But do you think that the modern deep learning approach,
*  neuro-AI approach runs any risk of falling into that same error
*  of sort of mistaking the map for the territory?
*  Because that's a leading question.
*  Do you have anything in mind there?
*  What do you mean?
*  Like specific criticisms?
*  Because people think, right, that, for example, a transformer is doing cognition
*  or something.
*  And that's a very simplistic way of saying it.
*  But we're still, it's still a model.
*  And it's not the thing.
*  It's not the ultimate question.
*  It's still a model.
*  But it's a lot closer, perhaps.
*  I don't know.
*  What do you think?
*  Well, transformers in particular, right?
*  I don't, yeah, transformers, I don't think of as, in fact,
*  I'll go as far as to say, as far as I can tell,
*  transformers are almost a counterexample to the successes of neuro-AI
*  in that they bear, as far as I can tell, very little resemblance to anything
*  that I expect to find in the brain.
*  And their success basically derives from the fact
*  that they are extremely well-matched to our current generation of GPU hardware.
*  Right?
*  Yeah.
*  And that's great, right?
*  I am blown away by ChatGPT.
*  That is on fire.
*  It feels it's necessary to state that, that everyone's blown away.
*  But yeah.
*  Well, I mean, well, I am more blown away than that.
*  Well, I'm especially blown away, I'll say, because right up until the week
*  that I played with it, I was doubling down on my belief
*  that you would never have a large language model that was any good
*  at all without grounding.
*  In fact, I was having arguments with people who worked at DeepMind
*  and Google who were already playing with these.
*  I was like, no, no, it won't work.
*  And they were like, no, no, it does work.
*  I was like, nah, nah, nah, nah, nah, nah.
*  And they were like, no, no, you're wrong.
*  And yeah, I was wrong.
*  Yeah, so what do you think the role of ground?
*  I'm sorry I'm jumping around, but what do you think the role of grounding is now?
*  Do you think it has an importance?
*  Yeah, so we can jump to that.
*  I mean, what I think is that ChatGPT taught us something
*  that I don't think we would have learned any other way.
*  And that was not obvious to me, which is that in some sense,
*  language is a closed system in the same way
*  that arithmetic is closed under the integers.
*  So basically, it's very hard to break ChatGPT by asking it questions.
*  It gives reasonable answers and has reasonable things to say about almost
*  saying, and I know there are countless examples.
*  And honestly, the fact that it can't do arithmetic,
*  it literally can't do arithmetic, I don't see as a condemnation at all.
*  I think that's a ridiculous claim.
*  I can only do arithmetic for large numbers if I follow the algorithm.
*  And that's how to add numbers.
*  And that's not what we're asked.
*  That's not what ChatGP does.
*  So yeah, I think that what we've learned there
*  is that it can give a reasonable answer to almost any question that's
*  formulated as a string of words.
*  And that is super interesting and to my mind, surprising.
*  Early on, 3.5 you could still break by asking it,
*  which I thought was significant, by asking it something like,
*  what is the problem with making shoelaces out of uncooked spaghetti?
*  Oh, that's a good one.
*  Yeah.
*  Because that required some knowledge of the physical world.
*  And I thought that's what you wouldn't have.
*  That's the grounding.
*  That's your grounding.
*  That was an instance of grounding.
*  And I was pretty smug.
*  I was like, ha, ha, ha.
*  But no, GPT-4 can give you a long exposition
*  on the problem of using uncooked spaghetti for shoelaces.
*  So I cannot find anything like that anymore that breaks it.
*  There are a couple of like the goat, the goat, the cabbage,
*  and the man crossing a river that is said to break it.
*  Do you know?
*  No.
*  Oh, OK.
*  You know the classic logic puzzle that you have a goat, a cabbage,
*  and a wolf, and you want to get them across a river,
*  and you have to figure out the right sequence to do this.
*  Oh, OK.
*  And it will give you that.
*  What's that?
*  Nothing.
*  Yeah, that's vaguely familiar to me.
*  Yeah, yeah.
*  OK.
*  Yeah, and it will give you the right answer.
*  But then if you give it a variant of that,
*  it will not pay attention.
*  And it will answer reflexively.
*  And various people like Gary Marcus
*  will hold that up triumphantly and say, that's an exception.
*  I think a lot of lazy people who aren't thinking clearly
*  would also make the same mistake.
*  Or I can't operate on him.
*  He's my son.
*  But how is that possible?
*  You know that one.
*  No.
*  You don't know these paradoxes, right?
*  Yeah, yeah.
*  Well, I don't.
*  Yeah, I'm not part of the cottage industry of Gary Marcus.
*  Yeah, no, this is the right way.
*  It's a two minute digression, not worth it.
*  Anyway, the point is that I don't find those breakages
*  interesting.
*  So if you ask, what is the limitation?
*  It's the things that can't be done.
*  And there are hallucinations, which are interesting.
*  And that may or may not turn out to be a solvable problem.
*  It seems like people are making a lot of progress
*  on solving it.
*  But the point is, and this I think is important,
*  is that language is only a tiny bit of what we do.
*  And I think for me, that's really the key point,
*  is that we do an awful lot of things.
*  In fact, we are the product of 500 million years
*  of evolution.
*  And language, although I'm very impressed with it,
*  and I think it's key to our success, probably
*  emerged, depending on whether you think Neanderthal had
*  language, somewhere in the last couple hundred thousand,
*  maybe million years at most.
*  So we've had 499 million years of evolution.
*  And language is just this extra on top of that.
*  And all that other stuff is the stuff
*  that remains incredibly hard for artificial systems.
*  We have vision systems that work on static images.
*  They're really impressive.
*  You can take a picture.
*  One fun thing is someone sends you a picture of themselves
*  standing with some background in some random city.
*  You can upload that picture, and it'll say,
*  oh, that's Sofia Bulgaria.
*  Well, who would have known?
*  But yeah, go ahead.
*  Well, yeah, but I shouldn't have said transformers,
*  because like you said, that's sort of an example
*  of the opposite, right?
*  But I was thinking more in terms of the convolutional neural
*  networks with recurrence, and that neural AI push in terms
*  of understanding our brains.
*  Right.
*  I think convolutional neural networks are the example
*  that those of us who advocate for neural AI
*  hold up every single time to the point
*  where anyone who doesn't finds them that example annoying.
*  But it is sort of, and I'll say actually,
*  there's an even more fundamental example,
*  which is the idea of neural networks in the first place.
*  The idea that you're going to compute
*  with a whole bunch of elements that
*  are connected with variable parameters.
*  Right?
*  It's not obvious that we would have gotten there
*  had we not sort of been inspired by sort of squinting
*  and making an abstract model of the brain.
*  So if the question is what the question that usually comes up,
*  and maybe this is what you're getting to,
*  is well, what are we going to do in the future?
*  So here's the argument that people usually have,
*  which is, OK, sure, brains early on inspired
*  artificial neural networks in the same way
*  that birds inspired planes.
*  But we do not design planes based on careful study
*  of birds.
*  Right?
*  And that's the argument.
*  So one argument, one counter argument
*  that Jan Nikun likes to bring up is that apparently,
*  aerospace engineers do actually study birds
*  and get cool ideas from them.
*  I'm agnostic to that.
*  I'll defer to him, someone who apparently
*  has read up on aerospace engineering.
*  For me, the more fundamental counter to that
*  is simply that we are not, we are building systems,
*  in this analogy, that we want to be as bird-like as possible.
*  Right?
*  We define success as building the most bird-like bird we can.
*  Right?
*  So it's true that a 747 can do amazing things
*  that a bird can't do.
*  It can fly whatever, 10,000 miles.
*  It can carry lots of tons of cargo.
*  It can go 500 miles an hour.
*  But it cannot, and in the same way,
*  computers can do all sorts of things people can't do.
*  Right?
*  They can multiply big numbers.
*  They can serve up queries for Google, whatever.
*  But that's not what we're asking.
*  That's not what we would like artificial systems to do better.
*  We would like artificial systems to do better
*  at what birds do, which is to swoop from the sky
*  and pick up a fish.
*  Right?
*  And so if we wanted to build a bird-like bird that
*  could fly through the forest fairly quietly,
*  without using too much energy, and swoop out of the sky,
*  and grab a fish out of the water,
*  then we would probably do well to look very carefully
*  at how birds do all these things.
*  And in the same way, if our goal is really
*  artificial intelligence, which is the ability
*  to do anything a person could do,
*  I mean, that is sort of the most generic explanation,
*  we should probably figure out how people do what they do.
*  And I would argue that the path to understanding how people do
*  what they do is to look at how animals do what they do.
*  Because people have very little, I
*  would say, that's novel over what our ancestors did.
*  That's the language.
*  That you refer to as alignment.
*  So I asked you offline what you're excited about.
*  And one of the things that you listed
*  was alignment that you wrote to me,
*  that our current models for how to formulate objective
*  functions for reinforcement learning and stuff
*  are very limited.
*  And you think that we should look to the animals for that.
*  I think that's exactly right.
*  So I think there are, yeah, I'm particularly
*  interested in three large questions about where
*  you can hope to gain insights from biology,
*  from neuroscience, and port them over to artificial systems.
*  And alignment is sort of, in some sense,
*  the most fundamental, right?
*  So we currently build, are very good at building systems
*  that are pretty good at building systems that maximize
*  a well-defined objective function.
*  Right.
*  And if we say, well, we want multiple objective functions,
*  the answer is usually, OK, we'll just add a couple of terms
*  to the original objective function, right?
*  Lambda 1, objective 1 is lambda 1 plus objective 2 times
*  lambda 2 and so on.
*  Yeah, that has not turned, like choosing those lambdas,
*  that's a very impoverished way of representing objectives.
*  And I think in most cases, that particular expansion
*  hasn't worked particularly well.
*  It's brittle and it hasn't been effective.
*  So by contrast, animals are necessarily
*  expert through evolution at balancing multiple objectives.
*  They're called 4Fs, beating, fleeing, fighting, and romance.
*  Yeah, so we have to balance all of those.
*  When we're hungry, that might take precedence.
*  But at some point, no matter how hungry we are,
*  if we're about to get eaten by a predator,
*  we should probably put our hunger on hold and flee, right?
*  And romance sometimes takes a back seat to all of those,
*  only when the other three are dealt with.
*  And this is sort of the top level objectives,
*  but those are broken down into sub-objectives
*  and sub-sub-objectives.
*  And humans and other social animals
*  have social objectives that are as compelling and profound
*  as hunger, right?
*  Yeah.
*  There's a sort of biological architecture
*  that allows evolution to sort of introduce
*  new objectives that interact appropriately
*  with the existing ones.
*  And I don't think we know how that works in biology.
*  And I don't think we understand how
*  to do that in artificial systems.
*  Yeah, if you ask some of the cognitive architectures,
*  we're a big thing for a long time.
*  And they still are.
*  But one of the issues, or one of the things
*  that those people learned in trying to build those systems,
*  is that the coordination between the modules
*  is like a harder problem than the actual objective functions
*  in the modules.
*  Exactly.
*  Exactly.
*  I think that's exactly right.
*  And yet, I think that this is a case.
*  So I make the argument that neuroAI is really
*  this virtuous circle, this virtuous cycle,
*  between taking insights from neuroscience,
*  applying them to AI, using AI as a model of neuroscience,
*  in the same way that I don't think we understand,
*  vision scientists understood just how hard vision was
*  until they sort of took their fuzzy ideas
*  and tried to build a system on them.
*  I don't think even the people who
*  work on various motivations understand how hard it is,
*  as you say, to coordinate them.
*  And we won't really understand how hard it
*  is to generate behavior from an agent that
*  has a whole bunch of objectives until we start
*  trying to build such agents.
*  OK.
*  And that will define the problem better even
*  for the experimentalists.
*  We're still, at the experimental level,
*  still trying to define what are the signals for reward.
*  And obviously, important groundwork.
*  But it doesn't necessarily get us to the really hard problem,
*  or what may turn out to be the really hard problem of
*  coordinating a bunch of these things simultaneously.
*  This goes back to the question of what
*  you want your artificial intelligence system to do.
*  And I don't know, replicating us,
*  maybe that's not the best use of building these things.
*  Why would we want a system to have
*  all the hard-won evolutionary coordination dynamics
*  among our whatever 16, 17 objective functions?
*  Why would want them to have to battle that out,
*  have to implement all that?
*  I mean, I want a robot that washes my dishes.
*  Yeah.
*  Yeah.
*  Right?
*  But I want that robot also not to step on me.
*  I want it to be aware if my house catches on fire
*  and do something appropriate about that.
*  What about the romance part?
*  Do you want that too?
*  I do not want romance, but I will tell you
*  that what drives technology traditionally has been romance.
*  If you look at the history of various technologies,
*  it turns out that the rise of VHS
*  was apparently driven by, let's say, romantic movies.
*  Oh, yeah.
*  Is that true?
*  I didn't know that.
*  That is.
*  It is.
*  It is apparently.
*  Yeah.
*  Movies featuring private romance were
*  one of the main drivers of VHS.
*  Certainly one of the main drivers of the early internet.
*  I believe it's still one of the main sources of traffic
*  for the internet.
*  I think so.
*  Yeah.
*  So I have no doubt that romantically inclined robots
*  will be a huge market.
*  Not my own personal dream, but like.
*  Right.
*  Yeah.
*  Wash the dishes and have a little romance.
*  That's right.
*  But yeah, so I think in practice,
*  the particular objectives that we
*  want that robot to be guided by will undoubtedly
*  turn out to be very different from our objectives.
*  But what's important is not the content of those objectives,
*  but the computational framework for creating them off
*  appropriately.
*  Like our objectives in our objective function survival
*  features pretty heavily for most humans.
*  But even that, that can be relaxed.
*  An individual ant does not really care that much
*  about its own survival.
*  An individual ant, in large part,
*  I guess because it's a clone of all the other ants
*  in its colony, is very willing to sacrifice itself
*  for the good of the colony.
*  Right.
*  Yeah.
*  It's all other things being equal, I'd rather not die.
*  But it's not mostly focused on not dying.
*  But there's still something at stake.
*  Sure.
*  Yeah.
*  And same thing with a robot.
*  Like you don't want your robot randomly
*  walking into a lava pit.
*  But you do want your robot not to value,
*  I guess, Asimov's three laws of robotics.
*  Survival, I believe, was, yeah, don't harm another.
*  Do what other people tell you unless it violates the first.
*  And try to survive unless it violates the other two.
*  I think that's roughly what they were.
*  But maybe we need something richer than that.
*  And certainly, we don't necessarily
*  want it given how we envision programming or instructing
*  our agents these days.
*  It's unlikely that we'll lay it out in words.
*  Although maybe with LLMs.
*  I mean, I had you on a really early episode.
*  And we talked about your paper that
*  argues that most of what's useful
*  is actually innate due to evolution over time.
*  And more recently, so you're still on that idea.
*  But also, you've incorporated development
*  as something that would be interesting to study
*  in terms of how is this related?
*  Your interest in development, is it
*  related to this coordination of the objective functions?
*  Absolutely.
*  Yeah.
*  So that's right.
*  The original idea that the original bandwagon upon which
*  I hopped was the-
*  You built the bandwagon, right?
*  You helped build it.
*  Well, it turns out other people were on this bandwagon.
*  But yeah, I've been-
*  You gave it a fresh set of wheels.
*  Well, I think, yeah, maybe I put some flags on it.
*  I don't know.
*  Anyway, yeah.
*  So I'm excited by the idea that much of all behavior,
*  all animal behavior, and humans are animals,
*  derives from deep, innate drives.
*  And this is true at every level, that we just
*  don't have time to learn everything from scratch.
*  In fact, I would go as far as to say that learning
*  can be seen as on a continuum with and really
*  an extension of simply development.
*  So if you buy the idea that most of what we have,
*  most of our neural circuits, most of our,
*  therefore, our behavior is determined
*  by our genome, which specifies a neural circuit,
*  then that sort of- it took me a while
*  to come around to the idea that that really requires
*  that you pay some attention to the relationship
*  between the genome and the final brain you get.
*  And the process by which biology takes a genome
*  and produces a brain is called development.
*  I thought for a while that I could sort of ignore
*  the biology of that, but it turns out that it's number one.
*  Well, mostly I wanted to ignore it,
*  because I didn't know much about development,
*  and I'm still woefully ignorant.
*  Me too.
*  Yeah.
*  Yeah.
*  But it turns out to be pretty interesting.
*  And there are principles that you can sort of abstract from it,
*  and that maybe can help guide your sort of how
*  we approach these problems.
*  And so sort of one of the core principles, for example,
*  is the idea that the process by which you derive
*  a brain from a single cell involves
*  sort of the recursive application of a relatively
*  simple set of rules.
*  And then when necessary, those rules
*  are modified across developmental time.
*  So people like Robin Heisinger, who would say,
*  and he's very focused on development,
*  and you make this point that there's not enough coding
*  capacity in our DNA to specify the entire structure of,
*  for example, our human brains.
*  And he would make the point, and I
*  don't know how you think about this,
*  that what the DNA is doing is actually
*  encoding those recursive rules.
*  And you have to have that.
*  That development is necessary.
*  You can't just go from DNA to the connect.
*  100%.
*  100%.
*  So in fact, Robin was just here for a meeting at Coldstream
*  Harbor last week.
*  And we had a wonderful meeting of minds.
*  And I'd never met him in person.
*  I'd read his stuff.
*  But we were 100% aligned on that.
*  And I would say I'm now hopping on his bandwagon.
*  The recognition.
*  The development bandwagon.
*  Yeah.
*  The recognition, exactly as you said, that just to back up.
*  So the idea that I was pursuing was
*  that the genome is a compressed representation
*  of our wiring diagram.
*  The bottleneck.
*  The bottleneck.
*  And it represents a genomic bottleneck.
*  And in fact, just this week, a paper,
*  our very first attempt to formulate that rigorously,
*  that paper was finally published.
*  It was out on bioarchive for, I don't know,
*  the last four years.
*  But it was finally published in PNAS.
*  Worked with Alex Kulikov, who's a fellow professor here
*  at Coldstream Harbor.
*  And in that vision, in that version of it,
*  we formulated the problem of compressing a weight matrix
*  by using another smaller neural network.
*  So we're compressing the weight matrix of a neural network
*  by using another smaller neural network
*  to predict the weights of the network.
*  So it's not quite an autoencoder.
*  Basically, you have a weight matrix.
*  And the weight matrix is n by n.
*  So you have n squared elements.
*  And then you have a smaller neural network
*  whose input is a pair of n squared elements.
*  And then you have a smaller neural network
*  of elements, two indices of the larger weight matrix.
*  And its output is a prediction of that weight.
*  And that worked.
*  I mean, we got great results.
*  We were able to compress big matrices from MNIST and CFAR
*  and ImageNet into a factor of 100, factor of 1,000.
*  And the compressed weight matrix basically
*  could perform almost at the same level as the uncompressed one,
*  the one after learning, just out of the box.
*  And so on top of that, we showed that these compressed
*  representations led to better transfer learning,
*  suggesting that when you compress a weight matrix,
*  you're throwing away the junk.
*  And you're keeping the stuff that's important.
*  Generalizable, more generalized.
*  Yeah, exactly.
*  Exactly.
*  So we saw compression as a regularizer.
*  And so that worked.
*  And then more recently with Blake Richards,
*  we had another version of this inspired by some,
*  which is now on BioArchive and under review.
*  It'll be another six years before it's published.
*  Yeah.
*  Where we use cell types and stochastic connectivity
*  among cell types.
*  And that also works.
*  And it has somewhat different properties.
*  So in a sense, you've solved that bottleneck problem.
*  Well, so I would say that both of those
*  were fun and great learning experiences.
*  But the stuff that I'm working on right now
*  with a postdoc named Stan Christian,
*  it's really driven by some ideas he
*  had for how you can formulate that developmental process
*  recursively.
*  How you can grow a network using very simple rules.
*  And this network grows and can be
*  guided to produce a final result that solves tasks.
*  That, to my mind, has captured some of the key elements
*  of development.
*  And these recursive rules.
*  What's that?
*  Would that process also then be more efficient?
*  Well, that's what we're interested in finding out.
*  So what I think is that it represents a prior
*  on the possible circuit.
*  Any set of rules you have for compression
*  represents a prior over the circuits
*  that you can generate.
*  You might not be able to articulate that prior,
*  but if you have a small thing making a big thing,
*  then it's only going to be able to make
*  a subset of the big things just by information
*  theoretic arguments.
*  And the subset of things that it can produce,
*  and which ones it learns most quickly,
*  that represents a constraint on the set of networks
*  and a prior over those.
*  OK, yeah.
*  You said the word I was thinking, constraint.
*  And I've come to think of constraints as that coordination
*  problem.
*  Constraints are everywhere.
*  In some sense, they're more important than the process
*  is the constraint.
*  Exactly.
*  So people will argue that the success
*  of artificial neural networks is really
*  that they represent, well, a prior, a smooth prior
*  over data.
*  Like there's a lot of work on that.
*  But it's the same sort of idea.
*  And you can't know ahead of time what
*  the right set of constraints is, what the right set of priors
*  is.
*  This is sort of an experimental question.
*  The proof is in the pudding.
*  But in this case, the fact that the prior
*  at a very high level from 30,000 feet
*  kind of looks like the prior that
*  guides the formation of actual neural circuits, right?
*  The idea that every neural circuit ever in existence
*  in biology arose from a single cell, right?
*  And then the set of rules that took you from one cell
*  to many cells has to fit in the genome.
*  That maybe is one of the key constraints.
*  So anyway, that's something I'm pretty excited about now.
*  We'll see how that plays out.
*  But I feel like that's sort of the right way to go.
*  And there's also a very natural sort
*  of interpretation of that or evolution.
*  Because what evolution does is it produces a circuit.
*  So evolution, so you start with a circuit.
*  And then the circuit is good at doing some things.
*  The organism, well, the organism in whose brain that circuit is
*  good at performing some behaviors and perhaps not
*  others, then you select for animals
*  that are maybe somewhat good at performing some other behavior.
*  And then they will develop possibly, right?
*  In the next generation, if the rules of development
*  are such that the animals circuits sort of get even
*  better at that behavior, then you select for those, right?
*  And then you sort of add on to the existing circuit.
*  You add on new abilities, new circuits.
*  But you have to make sure that every generation you
*  can produce an organism that has a brain that can do
*  all the things you want it to do.
*  Why do you need development in there, though?
*  Well, in biology, you need development
*  because you start every generation with a single cell.
*  So you have to give a plan for how you go from one cell
*  to a body and a brain connected to the body.
*  I personally focus, I'm at this point,
*  more interested in the rules for generating the brain.
*  But honestly, if we're ever going to understand robotics,
*  we might want to think about the fact
*  that bodies also are built that way.
*  Yeah.
*  But the AI field, earlier you alluded to your reluctance
*  to take on development.
*  And I have felt it scares me, essentially,
*  because it seems so hard.
*  But then I imagine the AI field would
*  want nothing to do with development
*  or think that it's something that biological organisms have
*  to go through because they're coming from one cell.
*  But that might not contribute to AI, for example.
*  Sure.
*  Let me tell you about a case that I've been thinking of.
*  We haven't made any progress on it.
*  So I'm giving away my research ideas.
*  But that's OK.
*  I think I'd be thrilled if other people pursued them as well.
*  I've been thinking a lot about robots recently.
*  There's a problem that we don't really
*  have terribly good robots.
*  They're not very good at interacting with the world.
*  For a while, I think there's a community of people
*  who are excited about these physics simulators.
*  I've been playing around with them like Mujoko.
*  But I think a lot.
*  So in these physics simulators, you
*  can specify agents that have arms and legs.
*  And they're connected by something like muscles.
*  And you can apply forces on them.
*  And then you can learn policies to control them
*  in these artificial environments.
*  And I think they're thought to be pretty realistic simulators.
*  They try to make them as realistic as they can.
*  And it turns out to be remarkably hard to build,
*  even in these reduced physics simulators,
*  agents that can walk around.
*  It was a real teaching point to me
*  that how hard it is to make a simple agent walk around
*  in a physics simulator.
*  And so we fooled around with that a little bit.
*  And many other people have done serious work in these.
*  But I think that my understanding
*  is that relatively few serious roboticists spend
*  a lot of time in simulation.
*  Because the problem of taking the simulated agent
*  and bringing it into the real world is basically unsolved.
*  It doesn't work.
*  It's the so-called sim-to-real problem.
*  And so here's my thinking on that.
*  There is a kind of similar, if you like,
*  sim-to-real problem that confronts us in that we have
*  a genome that specifies a body and a neural circuit.
*  And the specification of the body
*  need not be terribly closely coupled
*  to the specification of the neural circuit.
*  So you are born with a brain that
*  had better be able to fairly quickly learn
*  to control whatever body you are born with.
*  Well, there's an exception to this.
*  I was just talking with Karen Adolf.
*  She studies human motor development
*  and has spent years studying children.
*  And the rate at which they fall and run into stuff
*  is just super high, starts super high.
*  Because they're exploring this space.
*  So they don't necessarily have to come out with.
*  So a horse, you use the example, can walk in a minute or two
*  of being born.
*  But humans were awful.
*  Yeah, it's a great question.
*  Humans are always the exception.
*  And I think once we understand animals,
*  it will be interesting to understand
*  why humans are the exception to a lot of what I'm saying.
*  Why is it that it takes us many years to learn how to walk?
*  I think it's pretty clear that it's not
*  because we couldn't have learned to walk more quickly.
*  In fact, I'll go as far as to say as a, well,
*  my kids are older now.
*  But I remember when my kids were younger.
*  And I would have preferred them to take even longer
*  to learn to walk.
*  Because if they don't have the common sense
*  not to do stupid things, right?
*  There's this long, I don't know how,
*  I think you have kids how old are they now?
*  Nine and 11.
*  And I'm just, there's a breakthrough
*  where I'm trying to make my son ambidextrous,
*  which is impossible.
*  So we've been doing a lot of throwing with left handed
*  and stuff, it's hard.
*  Yeah.
*  But you remember that period where there are toddlers,
*  where they now have the ability to locomote,
*  but not the good sense not to locomote to the wrong place.
*  They have the ability to pick something up and put it
*  in their mouths, but not the good sense
*  not to put the wrong thing in their mouth.
*  I think this long delay before we can even learn to stand
*  is just a reflection perhaps of the fact
*  that the ones who learned to stand too early
*  made bad decisions.
*  Anyway, going back to animals, I would go and point out
*  that you can meet a Chihuahua and a Great Dane.
*  Might be a little awkward, but it can happen.
*  And basically their DNA is compatible.
*  The same circuit, basically.
*  What that tells you is that the instructions that
*  build a Chihuahua brain are essentially
*  indistinguishable from the instructions that
*  build a Great Dane brain.
*  And that's two orders of magnitude.
*  When you run Mujoco, if you build a typical agent
*  in a Mujoco physics simulator, at least in our hands,
*  if you train the agent to control its body
*  and then you change the body by 10%, 20%, it breaks.
*  And we're not talking 10%, 20%.
*  We're talking a Chihuahua is a couple pounds.
*  A Great Dane is 200 pounds.
*  So this is a crazy amount of flexibility.
*  And so how does that happen?
*  I mean, we don't know the details,
*  but the answer is, I think, that there
*  is a developmental process.
*  You might even call it a developmental curriculum.
*  And at each step, you solve some problems
*  of the overall problem that somehow enable
*  this entire brain-body combination
*  to learn to walk and run within a few months,
*  even a few weeks.
*  I'm picking Great Danes, but I think even those dogs,
*  and I think even those probably, the evolutionary pressure
*  wasn't as high to get things moving immediately.
*  You could probably use a pony and I
*  don't know what large horse.
*  I don't know the names of a large horse.
*  Anhyzer bush horses, whatever those are.
*  Yeah, exactly.
*  So that's probably only one order of magnitude difference
*  in size, but I think the same argument holds.
*  And those guys can walk within a day or two.
*  Yeah, this reminds me of, so you use the word curriculum.
*  So curriculum learning, and you can correct me,
*  is the idea, is that idea that you just mentioned of,
*  instead of learning to, let's use tennis,
*  a tennis serve as the common example, right?
*  You don't just go and just do the serve.
*  You learn how to stand.
*  You learn how to bend your knees.
*  And then you put all these, then you do those separately,
*  and that's curriculum learning.
*  And then you can put them together.
*  Someone at the, was just, Alexander Mathis
*  was just talking about this and how it actually
*  helps to teach an artificial system how
*  to do something like that.
*  So I guess that's what you're asking.
*  That's right.
*  There has been a fair amount of work
*  in ML and machine learning on curriculum learning.
*  Usually people push back and say that the failure there
*  is that it's too hard to choose a good curriculum.
*  Yeah, right.
*  And I guess I would say that probably for many problem
*  domains, that's kind of right.
*  Like if your goal is to learn image recognition,
*  to build a system that does image recognition,
*  and your goal is to train it faster,
*  I guess it's not clear what role curriculum would play there.
*  You might take a guess as to what are good building blocks.
*  But by the time you've tried a whole bunch of curricula,
*  you may as well just have used your data
*  and trained end to end once.
*  So I think that's kind of how it got a bad name
*  because it's been applied to solving a different problem
*  from the one that I outlined here.
*  Because where the curriculum is potentially useful,
*  at least one place where I see it is potentially really useful,
*  is if you have essentially the same problem
*  that you need to solve over and over again
*  with slightly different constraints,
*  a slightly different formulation, a slightly
*  different brain, a slightly different body,
*  now we're in a domain where that curriculum could really
*  pay off.
*  Because I think, yeah, go ahead.
*  So you're thinking in terms, I'm thinking
*  in terms of like Karen Adolf studies and stuff,
*  just because she's been on my mind.
*  You're thinking in terms of taking inspiration from how,
*  let's say, an example like as a baby crawls,
*  the way it can even hold its head is different.
*  So it looks at different things at different times.
*  And then as soon as it can sit up and move around better,
*  then it's outlook on the world, the way it actually
*  takes in the world changes.
*  And it's scanning a different set of things.
*  But again, it's the same sort of problem
*  of getting visual information in.
*  And then by the time they're walking,
*  is that what you're talking about,
*  using that from development as inspiration?
*  Because they're solving slightly different.
*  That's right.
*  So that's right.
*  They're solving different problems.
*  And the solution to one problem provides a foundation
*  for the solution to the next problem.
*  And the particular, so this is where evolution comes in,
*  is that evolution in some sense provides guidance
*  as to the sequence of problems that were solved.
*  So I don't know if you've yet had Max Bennett on as a guest.
*  Yeah, yeah.
*  He's a good book that he wrote.
*  Yeah, yeah, yeah.
*  He lays out a particular collection
*  of five brief history of intelligence.
*  I recommend it to all of you.
*  He's one of the speakers at NISUS.
*  He's one of the speakers at NISUS.
*  Yeah, beautiful book.
*  Just frustratingly good in that I
*  was thinking of writing a book, and now I
*  don't know what I'd write.
*  He wrote a better book than the one I was,
*  much better book than the one I was envisioning writing.
*  But in any case, he lays out five big problems that, yeah,
*  there you go.
*  That's it.
*  At this point, I've recommended his book so widely,
*  I feel like I deserve a fraction of the royalties
*  that he's getting.
*  No, it's a very well-written book.
*  Yeah, OK.
*  Yeah, it's beautiful.
*  The five breakthroughs.
*  The five breakthroughs, right?
*  So I don't know if it's exactly right,
*  but it has the flavor of a really nice framework
*  to think about the problem.
*  And the idea is that you can't get to the second breakthrough
*  until you've had the first one.
*  And then there's this old adage, which
*  has some truth in it.
*  We could even talk about why it's not quite true,
*  but ontogeny recapitulates phylogeny.
*  In other words, development replays the evolutionary history
*  up to a point.
*  And so the natural interpretation
*  is that, well, you have an agent,
*  you have an animal that can perform a bunch of things,
*  and those things are so important.
*  It can do them at birth, and then it learns other things
*  that turn out to be useful.
*  And those animals that are particularly
*  good at learning those other things quickly get selected for.
*  And the fastest way to learn something quickly
*  is to not have to learn it at all,
*  but just stuff it into your genome,
*  or stuff it into your genome as much as is possible.
*  And that's what led me to say earlier
*  that it's extremely hard to distinguish
*  between development and learning.
*  Basically, the faster you are at learning something,
*  the better your priors for learning it are,
*  the less information you need from the world to learn it.
*  And that all happens by stuffing it into your genome.
*  Are you familiar with Justin Wood, his work?
*  I'm not.
*  You should check him out.
*  So he used to be a staunch nativist.
*  And now he is a staunch empiricist.
*  And it's because of his work.
*  He does controlled rearing of chicks.
*  So when they're hatched, they go straight
*  into this automated box where they
*  have complete control over what they see,
*  and what they can do, and stuff.
*  And some of his research findings have the...
*  Everything he's finding is leading
*  him to think that everything is learned and nothing is innate.
*  And so you guys should have a conversation, perhaps.
*  Yeah, I mean, yeah, I don't think
*  I ever want to have an arm wrestle with the nature
*  nurture crowd.
*  The answer is it's both, right?
*  Of course.
*  Do you famously, I had a friend who used to always ask me,
*  do you walk to school or carry your lunch?
*  Right.
*  That's good.
*  I mean, yeah.
*  But that said, he's wrong.
*  I have no idea.
*  No idea.
*  Google, some of his stuff.
*  So after we're done, I'll take a look at it.
*  Sure.
*  Yep.
*  I don't know.
*  I interrupted us.
*  You were talking about packing information into the genome.
*  Yeah.
*  Yeah, I would say that part of it, going back to AI, right?
*  So one problem this curriculum issue
*  could solve, or address, or provide a way forward on
*  is it could...
*  You could imagine in simulation figuring out
*  what the right developmental curriculum is.
*  And then, right?
*  And what success would look like is
*  you pick a series of 10 things or 20 things
*  that an agent would have to learn and subproblems.
*  And the hope would be, right?
*  The expectation would be that if there
*  exists such a curriculum, learning those 10 things,
*  the sum of the time it takes to learn those 10 things
*  is shorter than the amount of time
*  it takes to learn the thing that you're ultimately
*  trying to learn, for the sake of argument, walking.
*  And that then, if those 10 things are relatively
*  straightforward, you could maybe follow
*  that same developmental curriculum in an actual agent
*  with the idea that, yeah, it's still
*  going to have to learn the body, all the differences
*  between the body it would have thought
*  it had from the simulator and the one it actually
*  got in the real world.
*  But maybe those differences, if you break that into pieces,
*  are smaller than trying to learn the whole thing end to end.
*  But you wouldn't want to create a robot that develops?
*  I might want to create a robot that maybe is born into its body
*  but then learns how to control the nuances of its body.
*  Because really what I want is to be able to build many robots
*  and not have to spend a year each time
*  I build a new robot body.
*  Yeah.
*  Right.
*  Right.
*  So you're not 100% on board with all facets of development,
*  then?
*  No, no, no.
*  Look, I mean, that's always the rule from at least,
*  that's always my idea when looking to neuroscience
*  for guidance, for inspiration.
*  Right?
*  Like, I don't want to make, I don't even
*  know what it would mean to make a perfect,
*  to incorporate all the details from biology, right,
*  into an artificial system.
*  The only thing that has all the details of biology
*  is biology, right?
*  Yeah.
*  So I spent a fair amount of my graduate work
*  studying single channels, and I think they're fascinating.
*  I like open, I like studying channel kinetics.
*  I think these are fun problems.
*  I don't think they're at all relevant, as far as I can tell,
*  to anything I'd ever want to put in an artificial system.
*  Right?
*  Like, how you make an action potential
*  is a cool problem that stands on its own,
*  and as far as I can tell, I mean,
*  maybe someone else will come around and explain
*  why it is relevant, but I will certainly not
*  want to build an artificial system that
*  has sodium and potassium channels.
*  At least it's not obvious to me why I would.
*  Yeah.
*  Yeah.
*  Right?
*  That's even best below my line as well.
*  Yeah.
*  And so sure, I'm open to the idea that neuromodulation
*  is important, right?
*  Obviously, it's super important for how animals work.
*  I don't personally yet know how to,
*  and this just reflects my ignorance.
*  I'm not saying that other people don't know how to do this well,
*  but I don't know how to sort of abstract
*  the principles of neuromodulation in a way that
*  makes them useful for an artificial system.
*  So I'm not just going to put it.
*  We don't know the principles of how they're
*  useful in biological systems, right?
*  So I think we're still pretty far away from having,
*  from feeling like we have that even close to being tackled.
*  Exactly.
*  Exactly.
*  The tremendous success of convolutional neural networks,
*  which were inspired by Hubel and Weasel, right?
*  Like that is a great example that not all aspects
*  of receptive fields were stuffed into a neural network.
*  It is the idea like that.
*  You can now, in retrospect, 2020 hindsight,
*  we can boil it down and just say, look,
*  it's the idea of translational invariance, which maybe could
*  have come from some other angle, right?
*  Like maybe you didn't need to study receptive fields,
*  but that's how the idea was hatched.
*  So that's my attitude toward how these things.
*  I'll just go and make one other comment, though,
*  about the appeal of a curriculum as opposed
*  to end-to-end learning and the idea
*  that a curriculum that is rooted in the actual evolutionary path
*  that humans follow to get where we are,
*  why that would be useful.
*  And I think a lot about the example of self-driving cars,
*  right?
*  Self-driving cars don't work that well.
*  I'm surprised.
*  I just recently read an article, apparently even Waymo,
*  which is pretty widely deployed.
*  There's basically literally a roomful of people
*  who are helping the Waymo cars out when they get into trouble.
*  They need grounding, right?
*  Is that what they need, grounding?
*  I don't know.
*  But no, no, Waymo, apparently there's a control center.
*  Like online?
*  And a bunch of people's, yes.
*  So there are people sitting in a room.
*  This was a New York Times article a couple of weeks ago.
*  There are people sitting in a room somewhere.
*  And I think it said every three to four minutes,
*  they are called upon to help out one of their cars,
*  which is having trouble.
*  I said online.
*  What I meant is real time.
*  So they're doing this in real time.
*  Real time.
*  Waymo is driving around.
*  And then, oh no, there's a yellow cone.
*  What do I do?
*  Poo, poo, poo.
*  And then there's a guy sitting there saying, OK,
*  steer to your left.
*  Go, OK.
*  And then I think he has a little mouse or something.
*  And I white knuckled it on a self-driving Tesla before.
*  And it's an exciting experience.
*  So why doesn't it work?
*  The hope has been that just increase the amount of data
*  by another order of magnitude and another order of magnitude.
*  And you'll start fixing all these problems
*  on the long tail.
*  And I guess my argument is twofold.
*  One is that, again, the reason driving is pretty easy for us
*  is that we already understand everything we need to know
*  about how to parse visual scenes.
*  We didn't have to learn how to parse visual scenes
*  by sitting behind the wheel of a car.
*  We didn't have to.
*  Yeah?
*  Yeah, well, there's also the frame problem,
*  which is still a problem.
*  And that we have solved the frame problem
*  to know what's relevant when we're driving.
*  Sure.
*  Well, we have solved, more generally,
*  we have solved the problem of being able to,
*  in a novel situation, figure out what's relevant and what
*  isn't, right?
*  And then we learned the details.
*  I'm teaching my 14-year-old how to drive.
*  And it's-
*  Talk about white knuckling.
*  It's very good.
*  Yeah, OK.
*  But yeah, so it's definitely a learning experience.
*  But we've gone out a half dozen times,
*  and there's been dramatic improvement, right?
*  So he has to fill in some of the blanks.
*  But I guess the other problem, in some sense,
*  I would say that this is even a more fundamental problem.
*  So even if we get to the point where self-driving cars,
*  on average, make fewer mistakes than people, which
*  we may get to, we're going to be very disappointed
*  if the mistakes they make aren't kind of similar to the mistakes
*  we make, right?
*  So if a self-driving car, on average,
*  has a much better track record than a human,
*  but it occasionally just runs down
*  a kid in the middle of the street who any-
*  you're going to review the video,
*  and you're like, what the heck happened there?
*  Anyone should have seen that.
*  That is going to limit our enthusiasm about adopting
*  these self-driving cars.
*  And I think this is a general principle that-
*  so what is going on there, right?
*  If the objective function is don't run things over,
*  you're going to get a system out of many systems that runs
*  things over as little as possible, right?
*  In order to ensure that it not only does a good job,
*  but it fails in the same way we do, right?
*  We need a system that is as isomorphic to the way
*  we do something as possible, right?
*  It can't just not make mistakes.
*  It has to- or it can't just make as few mistakes as possible.
*  When it makes mistakes, they have to be human-like errors.
*  And that- yeah, go ahead.
*  The problem with that, though, is that we're not great drivers.
*  I mean, you and I are above average, right?
*  Everyone's above average, right?
*  I mean, I'm not sure what- we can mostly agree on what
*  are reasonable mistakes to have made, right?
*  Yeah, yeah.
*  And I think that's sort of the key point here, right?
*  The fact that we do make mistakes,
*  those are mistakes of lapses of attention, et cetera.
*  And I expect that those are mistakes
*  that the artificial agents won't make, right?
*  They hopefully won't get distracted.
*  They hopefully won't be talking on their cell phones.
*  They won't be driving drunk.
*  Romancing and driving.
*  They will not be romancing and driving.
*  That is-
*  That's what we can do while they're driving, right?
*  That's right.
*  That's right.
*  Before-
*  Just to that point, right?
*  When we have robots that drive and romance,
*  they will know that they shouldn't mix the romance
*  and the driving if we can get their objective functions right,
*  if we have a complex multi-objective function,
*  right?
*  They will know-
*  Yeah.
*  You're on board with thinking that that
*  is a harder problem than implementing
*  an objective function itself.
*  Yeah.
*  Yeah, yeah.
*  Tony, what have we missed here?
*  We've gone through kind of like those three main things
*  for the reasons that you're excited about,
*  maybe the most excited about neuro AI.
*  Yeah.
*  Did that paper, the one that maybe was it a year ago now,
*  the Catalyzing the Next Generation
*  of Artificial Intelligence from Neuroscience Principles,
*  something like that.
*  Oh, wow.
*  You know the titles of my papers.
*  Something.
*  Yeah, that's close.
*  Did that get much pushback?
*  No, no.
*  I don't think anyone bothers.
*  So my take on it is that-
*  So when I started, like I said, there
*  was widespread agreement among the leading AI researchers.
*  Jeff Hinton, Jan LeCun, Joshua Benjio, people like that.
*  They were excited about neuroscience.
*  They wanted to learn about neuroscience.
*  Right.
*  They were very clear that these things were important.
*  I think what has happened is there
*  have been several generations of engineers, AI scientists,
*  who never actually had direct contact with neuroscience.
*  Maybe in an introductory lecture,
*  they heard that in prehistoric days,
*  AI, machine learning, had something
*  to do with neuroscience, but it was prehistoric for them.
*  And so if you go to NeurIPS today,
*  my guess is that fewer than 1% of the people there
*  have any interest in this potential for Neuro
*  to have any impact on AI.
*  And I think that's fine.
*  If my goal is to deploy a commercial LLM for a recommender
*  system or whatever, something that digest law documents,
*  there's absolutely no reason that any of these people
*  could be learning about neuroscience.
*  I think even the next level of optimizing algorithms,
*  which takes a lot of work and a lot of theory,
*  it's not clear to me why those people should
*  care about neuroscience.
*  I think the bet that I'm placing,
*  and I think some very small fraction of the overall community
*  is willing to place, is that just continuing
*  on our current trajectories without some really
*  new ideas may asymptote before we get to where we want
*  or where they want.
*  But I was just talking with Kim Stakenfeld,
*  and one of the things I brought up
*  is didn't DeepMind, in a sense, fail
*  because their original mission was to use neuroscience
*  principles.
*  And now they've outgrown that with scale, et cetera,
*  so that mostly they've moved on from trying
*  to find inspiration in that sense.
*  I mean, have they failed or have they abandoned their mission?
*  I use the word failed because it's a hotter take.
*  Yeah.
*  Well, I think there's no world in which you'd say DeepMind has
*  failed.
*  No, no, no.
*  I know.
*  I was just being provocative.
*  But even there, yeah, no, my understanding,
*  and she and others know this better than I do,
*  is that they're under some pressure
*  to deliver the order term.
*  And I think there are people there who are disappointed
*  that they now actually, they're being asked to,
*  and this is happening also at Google Brain and elsewhere,
*  people are being asked to actually get away
*  from the basic research that they were doing
*  and help build a better.
*  And look, from a corporate strategy point of view,
*  when your profits are only $40 billion and a year,
*  you could see how you might get nervous.
*  Yeah, yeah.
*  Yeah, so yeah, I think these are strategic decisions.
*  I think basically there's a gold rush going on with LLMs.
*  Each of these companies is trying
*  to figure out how to capitalize, how to cash in on that.
*  I don't blame them.
*  Sure.
*  If they miss the boat on that, they're cooked.
*  You don't want to fail on that.
*  But I don't think that that necessarily
*  has much to say about the medium five to 10 year time
*  horizon of potential impact of the intersection
*  of neuroscience and AI.
*  Well, I see that paper getting cited a lot.
*  I've not looked at citation counts.
*  You probably know that.
*  No, I don't look at them either.
*  Oh, OK.
*  It seems to be a pretty popular.
*  Yeah, no.
*  I think for a small group of people,
*  it helps galvanize their interest.
*  It helps focus their interest.
*  And I don't think anyone cares enough to say,
*  no, this is a waste of time.
*  The people who do think it's a waste of time, and like I say,
*  I think that's a large fraction of the community,
*  they just ignore it.
*  Sure, yeah.
*  And the only reason that people would push back, I guess,
*  now that I think of the sociology of it,
*  is if we were fighting for limited resources.
*  By doing this, we were getting a larger slice of the pie.
*  And that pie is so enormous that this is barely even a crumb.
*  So right now, it's not in anyone's interest
*  to argue against this research program.
*  Yeah.
*  All right, well, thank you for taking me
*  on that meandering walk through your recent work.
*  Keep up the good work.
*  I'm glad that you're delving into development
*  and that I'm not, because it's still scary.
*  Can I just say one final word?
*  Yeah, yeah.
*  Well, two words.
*  One is delving is a word that's overused by chat GPT.
*  And I'm surprised to hear.
*  Oh, you didn't know that?
*  No.
*  It is the most overused word by chat GPT.
*  It is the, like I'm now suspicious that you
*  are being powered by chat GPT.
*  Oh, and so should I remove it from my vocabulary?
*  Or do people say it too much?
*  Certainly from your written vocabulary,
*  because that is the marker of chat GPT.
*  Anyway.
*  All right, I will delve.
*  Yeah, but what I was going to say about development,
*  and this was the one point I wanted to make,
*  I realized that the reason that I was turned off to development
*  is that over most of my professional career,
*  development has been a pretty uninteresting list
*  of molecules.
*  And so I just thought of it as some
*  of the least interesting, like important,
*  like that list of molecules is super important.
*  But I can't, unless you're in the field,
*  you don't want to, at least I don't want to just memorize
*  a list of molecules or learn any new ones.
*  But there's a previous generation going back even
*  to Turing, who worked on development,
*  von Neumann and Turing both worked on development.
*  The question of how you build a system
*  from a single building block, how that thing can
*  make copies of itself and self-organize
*  into a global structure, I think is a really interesting problem
*  and not utterly unrelated to the kinds of problems
*  that neuroscientists and AI people think about.
*  Yeah.
*  And that has been the realization
*  that I've had as I went back to generations of literature
*  before I started watching or not watching
*  talks about development.
*  I didn't know or I had forgotten that about von Neumann.
*  But for Turing, that's like his lesser known
*  but still really cool work on those cascade instability work.
*  Yeah.
*  Anyway.
*  OK.
*  All right.
*  So thanks again, Tony.
*  Have a great conference, by the way.
*  I'm sorry I'm not going to be in time.
*  Yeah, I'm sorry you can't make it.
*  But I'll see you in a month or so.
*  See you in a month.
*  Thank you for your support.
*  See you next time.

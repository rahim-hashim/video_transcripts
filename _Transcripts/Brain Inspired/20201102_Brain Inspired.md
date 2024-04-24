---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5950s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 13746
Video Rating: None
---

# BI 088 Randy O'Reilly: Simulating the Human Brain
**Brain Inspired:** [November 02, 2020](https://www.youtube.com/watch?v=dMI4-xvuhNw)
*  People really have this ability for flexible cognition.
*  We can solve open-ended kinds of problems in a way that current models can't.
*  We've got this lever model. There's this weird circuitry in the thalamus.
*  What is it doing? How do we think about that? How are we going to incorporate that into our model?
*  And then it kind of all started to fall into place with this idea that it might be doing the actual predictive learning.
*  I think we're going to have AI that's conscious.
*  Everybody's going to be happy to say, yeah, that thing seems pretty conscious.
*  And again, I think that would be a situation in which we had essentially done a pretty good job recreating the human brain.
*  How far along are we to building a functional and biologically mechanistic model of a brain?
*  Some of us are farther along than others. Randy O'Reilly is farther than me, probably farther than you.
*  Randy recently moved his computational cognitive neuroscience lab to UC Davis,
*  but he's been working on his cognitive architecture Libra since he was a graduate student many years ago.
*  There are a small handful of cognitive architectures out there, big theory-based models that attempt to recreate large swaths of our cognition
*  using various levels of inspiration from neuroscience and psychology.
*  Most neurocomputational models focus on some singular mechanism, like how spike timing could drive plasticity,
*  or they focus on some psychological function, like how we maintain some information in working memory.
*  But cognitive architectures attempt to use overarching principles to assimilate lots of brain mechanisms and psychological functions into a unified whole.
*  And Libra, Randy's long-term attempt to simulate a human brain, is one such impressive architecture.
*  So we talk about Libra and how it started, some of the principles and ideas that drive it, and what he's currently adding to it.
*  One thing he's adding is a thalamus, for instance, because Randy's done some recent work that shows that the thalamus may be important for predictive learning, among other things,
*  which is learning by comparing our predictions about what's coming next with what eventually does come next.
*  Randy calls this deep predictive learning and relates it to bottom-up and top-down connections from cortex to thalamus and back.
*  So pretty important.
*  So we talk about that in a ton more, plus a question from previous guest Anna Shapiro, who ruined the surprise.
*  But I forgive her, barely.
*  You can run Libra if you'd like.
*  So I linked to Randy's lab in the show notes where you can find instructions on how to play with Libra and the free textbook that Randy and his partners wrote to go with Libra.
*  All of that's in the show notes at brandinspired.co.uk, slash podcast, slash 88.
*  If you value this podcast, the best thing you can do is to support it on Patreon.
*  It's super cheap and you get all of the full episodes plus bonus episodes, other bells and whistles like requesting guests for the show and submitting questions for the guests and so on.
*  Go to brandinspired.co and click the Patreon button there.
*  Thank you guys for your support and for listening.
*  I consider this podcast a celebration of ideas, and I'm glad to share that celebration with you.
*  Here's Randy.
*  So I have a memory of being at Phipps Conservatory 10 years ago in graduate school in Pittsburgh, Pennsylvania.
*  I was walking through this exhibit of blown glass.
*  There are these blown glass artworks shaped like plants and trees and it was all very pretty and delicate.
*  And I was thinking of you, Randy O'Reilly, during this time walking through Phipps.
*  Because I had I think I even applied to Boulder, to University of Colorado Boulder for grad school.
*  I'm sure I just got quickly rejected because of my previous academic performance.
*  But and I was thinking back how how my life might have been different had I been in your lab.
*  And now I have this memory of having the memory that at that point walking through Phipps of before I was in grad school.
*  Can Libra can you just code that up in Libra and tell me what's happening in my brain?
*  That's awesome.
*  Okay, I just searched and yeah, I see a email from you at UNC.
*  No, no.
*  From 2005.
*  Oh, this is embarrassing.
*  Working with Ben Philpott.
*  An excellent man.
*  Please don't read it.
*  I will definitely edit it out if you read it.
*  That's interesting.
*  Yeah, small world.
*  So, yeah, so the ability for cues to trigger memories is something we've really looked at in in our model of the hippocampus.
*  And so this idea that you know you can have this integrated representation of different you know situations and the whole idea of episodic memory of combining these you know sensory cues.
*  I'm trying to kind of lost track of what I was going to say though.
*  Well, we're going to get into Libra.
*  I just I just want to know if you could code that up real quick and tell me what's happening.
*  So anyway, thanks for coming on the show and talking to me and thanks a lot for pulling up that email.
*  Geez.
*  Yeah.
*  I'll have to ask you to forward that to me if I want to self-flagellate.
*  I remember though back in those days being in awe of things that I was learning.
*  You know, kind of early in graduate school.
*  How often are you in awe these days just at the state of how far you've come?
*  What you know, the ability of the brain and mind.
*  Do you ever take the time, you know, in the shower or wherever to and just kind of have that sense of awe anymore?
*  That is a really interesting question because, you know, our brains are wired to discount everything.
*  And so I often try to tell myself that I should, you know, think get some kind of bigger picture perspective on things.
*  And certainly, you know, I'm in awe when I read all the work that's going on in AI.
*  And so I think it's easier, you know, to kind of confront new things quickly.
*  And so when you see some some new finding or some new result or, you know, some amazing kind of new AI thing that happened,
*  you can you can kind of get that instantaneous kind of derivative, right?
*  That delta that says, oh, wow, that's different.
*  But for your own work, you just like, you know, it's so slow, it's so painstaking.
*  It's you discount it entirely.
*  And it's almost impossible to have that perspective.
*  So it's always, you know, I think it's I lecture about this, you know, that it's kind of this double edged sword of like, you know,
*  it's what drives us onward, but it kind of deprives us of our, you know, ability to kind of get pleasure out of things
*  because and it goes right back to the dopamine system, you know, this whole idea that that everything is relative to this expectation.
*  It's an error signal. It's not the raw value.
*  And so no matter what you do, how much you accomplish, you know, whatever you think, you know, you you discount that.
*  That's your that's your expectation.
*  And then everything is kind of relative to that.
*  And it's hard to get those kind of occasionally right when I come up with a new idea, you know,
*  which actually is often in the shower. Right.
*  You get that kind of, you know, miniature burst of like, aha, here's something new.
*  But a lot of times it's such a slow process that it's it's hard to get that kind of appreciation of like, you know, it's it.
*  I do have a declarative sense that, you know, if I ever I get kind of a bad review or which happens very frequently
*  or other kinds of disappointments, I have these kind of mantras of like, I am so lucky to be doing this.
*  I get to do what I want to do.
*  You know, it's such an amazing opportunity.
*  You have to repeat it to yourself, though, sort of.
*  Yes, exactly. Yeah.
*  And, you know, people people interview for the lab or, you know, I talk to people and I get that you kind of get it vicariously.
*  So like people, you know, when they first hear about what I'm doing, I have conversations, you know, with random people or just,
*  you know, when people come to interview in the lab and they're like, wow, that's so cool.
*  You get to work on that stuff.
*  And then I sort of like, you know, I think, oh, yeah, that is really cool.
*  Your mouth moves and you say, yes, that is cool.
*  And what you mentioned having having that feeling when you get a new idea.
*  And I yeah, that's a really good example, because I was reading Alison Gopnik the other day and just happened to come across her
*  analogy of explanation or grasping an explanation to the feeling of orgasm.
*  And I and wow, I know. Yeah.
*  So this is a popular thing that she does. Yeah.
*  Speaking of showers. No, I don't.
*  But that maybe we're like wired to for our, you know, learning and motivation systems.
*  And that's one of the things that, you know, when we grasp something, it sort of co-ops the the org org orgasm system.
*  And maybe the new idea is the same sort of thing. Absolutely.
*  No, I mean, I think, you know, everything we do at some level has to be driven by our low level kind of dopamine motivational pathways.
*  Right. And so so we have to have something that that gives us pleasure for, you know, achieving insight and learning because we obviously are motivated to do that.
*  And so, yeah, so I think it is.
*  And, you know, if you think about capturing that in a computational model, this is this is and I have thought about that.
*  And it's really interesting kind of like, like if you have a food and it actually, you know, when you think about it pretty deeply, there's similar kinds of issues like, you know, we know you get a dopamine reward if you get some positive, like, you know, food taste or something like that.
*  But there is this kind of question of like, when does the dopamine come, especially like if it's a meal, right?
*  The meal is a protracted thing. And so like, when does it count?
*  When do you actually sort of get the dopamine?
*  And if you look at the recordings of these dopamine neurons, it's like a little tiny bit of juice.
*  And it's like last a millisecond or something.
*  And so, you know, you just get this kind of instantaneous burst.
*  But like for something that's more protracted or more complex, when does the dopamine come?
*  When do you get that satisfaction, that feeling of satisfaction?
*  And then if you take that same question and apply it to like, you know, when do you understand something?
*  And when do you know that you understand something?
*  How do you know that you've actually understood it?
*  These kind of metacognitive things that then also connect to the dopamine system.
*  We think about that motivational stuff as being kind of hardwired because it's kind of, you know, what drives the system.
*  And if you could actually just kind of think thoughts and drive dopamine without actually doing anything meaningful,
*  that would really short circuit the system and be like doing drugs, right?
*  So you would just be like, you know, here I am sitting on my couch and I just told my dopamine system to fire a bunch.
*  And, you know, it's like having an orgasm on the couch.
*  You know, it's like, wow, this is great, you know, but you can't do that.
*  Right. And so what is it?
*  You know, how does our brain actually connect these kind of like more abstract, high level metacognitive things about like, what is it that we how do we know that we've done something
*  or understood something and then, you know, that our low level dopamine system can actually reward us for that?
*  And I think it actually does go back even for like meals and other kind of more basic low level type of things.
*  This kind of question of when do you know you've done something?
*  My dopamine hit at the meal table comes after the European style, seemingly hour and a half that we all that the family spins around the table waiting for the children to finish eating.
*  And that and the I just realized also the the understanding the grasping and that being a rewarding thing.
*  My experience is really a series of realizing what I don't understand.
*  So I'm not sure how that fits into the picture as well.
*  Right. Well, I mean, in some ways, understanding what you don't understand is, you know, more or, you know, equal if not more important.
*  Right. Yeah. And I think that that famous quote, it's not even wrong, you know, from whatever, whoever that physics guy was.
*  Yeah. Polly, I think Wolfgang Polly or something. I think I think it was him.
*  And so like knowing precisely what you know and what you don't know is a prerequisite to sort of getting those answers.
*  Right. And it's kind of like, you know, negative results in an experiment or, you know, finding something that doesn't fit with your theory or something.
*  You know, people think of that as like a negative thing, but it's actually, you know, the most positive thing because, you know, everything just kind of consistent and kind of, you know, you don't learn anything in that case.
*  So, yeah, I do think one of the big things, you know, going probably a little bit off topic here.
*  One of the big things that we're really thinking about in my lab right now is this kind of idea of like the thing that makes us able to solve new problems is having that that ability to recognize what we don't know.
*  And and to sort of to have again, I like even like this kind of conscious metacognitive, however you want to describe it, kind of knowledge of like, OK, I know A, B and C, but I don't know these other key points.
*  And then you know, kind of like what you need to do. Right. And that knowing what you need to do, knowing the answers you need to figure out, you know, allows you to then deploy like cognitive resources and everything to solving those problems.
*  In any given situation, it's going to be different stuff that you don't know, different stuff that you know.
*  And so that flexibility that we have to sort of solve new problems may be kind of tied up with this kind of ability to be aware of what we know and don't know.
*  A lot of these current A.I. models are really struggling with this question of like, you know, people really have this ability for flexible cognition.
*  We can solve open ended kinds of problems. We can do this kind of out of domain application of our knowledge in a way that current models can.
*  And so one idea is that this ability to kind of have a metacognitive understanding of what we know and what we don't know is an essential part of that, that instead of just having like fixed pathways where information flows through neural networks.
*  And, you know, you represent pieces of information that you know in certain ways.
*  And it's kind of, you know, these again, these kind of fixed pathways that you do have this kind of introspective cognitive access, this metacognitive access to what you know and what you don't know.
*  And then you can kind of say, OK, look, I can focus my now next steps of processing on this stuff, these questions that I've now recognized that I just don't know the answer to.
*  And the other kind of piece of it is knowing the relationship. So, you know, you know, if I could just figure out what some particular mechanism is that connects phenomenon A and phenomenon C, you know, and I could find that missing link B, then I could answer this question that I want to answer.
*  Kind of being able to represent the relationship among the knowledge that you have and where the missing pieces fit into that overall schema relationships seems like, you know, a really key element that we have that that A.I. models don't have.
*  And that's kind of like, you know, how does that actually take place in neural networks? That's our big challenge.
*  That is a big challenge. Is that your existential experience of things that you don't know? I mean, my personal experience often is sort of just fumbling along and then come up.
*  I seem to come across something that fills a gap, right? I don't like lay out the what I do know and what I don't know in front of me and then can pick and choose what to study next.
*  Sometimes it's that explicit, but most of the time it seems more I'm unaware of it. I'm not metacognitively blind perhaps to it, but that might just be me.
*  OK, unfortunately.
*  So I do think that that is something, you know, a lot of times when I start something, you know, in a new area or something, it's very, like you say, kind of just fumbling along and you're just trying stuff.
*  And I always have this mantra of like, start simple, start with success, you know, just just do something.
*  And it's very much like this kind of, you know, agile software development process or whatever.
*  Instead of trying to plan everything out and figure out that, you know, some kind of big logical structure, just like, you know, get started and see what you can do quickly.
*  That's just kind of my personality to very impatient and sort of lazy or whatever.
*  Well, yeah, but it works.
*  Well, yeah, so I do think that it is it fits in with our kind of motivational systems that we want, you know, incremental progress.
*  We want those little bits of success and dopamine or whatever.
*  Yeah, so I do think it is useful in general, despite whoever whatever your personality is.
*  But in those early stages, yeah, you don't even know enough to know what you don't know and don't know.
*  Yeah, but I do think, you know, and then you kind of accumulate and then when you do get to that point where you can say, here's what I know here, so I don't know, then maybe you're kind of pretty far along towards actually then being able to solve the problem.
*  Because it's it is you're right that it is like not the early stage, but the later stage.
*  You mentioned the thing that your lab is working on now, but your lab is working on lots of things and millions of things.
*  Yeah, one of the one of the big questions we're working on.
*  So when we started off, you mentioned, you know, being in awe of, you know, seeing like whatever the latest AI thing is that's coming out when you see that when you read something like that, do you immediately think?
*  I know I gotta I gotta build that into into Libra.
*  How can I do that? Like I need to do that. Yeah. Is that is that is that your thought process? Yeah, that's no good.
*  Well, a lot of times, yeah, a lot of times it's kind of, you know, how do I think about that? You know, and what does this tell me? Right.
*  You know, a lot of times I will try to dig in and see, you know, if I can figure out, you know, what what kind of lesson about, you know, because I think my focus very much is on the kind of scientific question, not the engineering question.
*  So I want to figure out, like, how does the human brain work? And and so I see AI kind of stuff is like potentially informative for, you know, what's what what is unexpectedly powerful?
*  What principles, you know, really work, you know, that we might not have thought about? And then how do we understand how those might function in the brain?
*  So I'm always thinking about it from that perspective. And, you know, like, for example, like generative adversarial networks, GANs, incredibly powerful, incredibly creative.
*  I think they tell us a lot about why, like social interaction is so important, because, you know, it's this open ended kind of interactive, you know, I'm talking to my friends, they're talking to me.
*  Both of us are kind of in a kind of, you know, competitive, cooperative kind of arrangement where we're, you know, we're trying to impress each other, we're trying to outdo each other.
*  And there's that kind of open ended kind of interaction that allows us to sort of train each other. Right. So our social interactions have that same kind of GAN like property.
*  But does that also operate in the brain? Is there a part of my brain that's like, you know, talking to another part of my brain? And we do have this notion of like an actor critic.
*  That's a well established idea that's kind of like what you see in these adversarial networks. But, you know, it is a really I think it's to me, it's a question I don't have an answer to, but it's kind of still a question of like, you know, what, what is it?
*  They're incredibly powerful. I can see like how social interaction can lead to those kinds of open ended kind of, you know, generative type of learning.
*  And I wonder in the brain to what extent there is a thing like that, that kind of maps on to the GAN. I don't know yet.
*  Yeah, those are inspirational findings in AI. Yeah, yeah.
*  This is a good time for me to play. So I have a question for you from a previous guest. So this is this is the other side of the coin. But this is on a Shapiro. She was on episode 43. Okay. Hi, Randy. This is on a Shapiro. And here's a question for you.
*  What do you think are the most important aspects of the brain that are missing from current state of the art machine learning models? So if you think about the problems that machine learning researchers are currently struggling most with, which of those problems do you think will be solved next if we take these elements of the brain into account?
*  Maybe a question for later in the conversation, but it seems topical. So yeah, absolutely. So thanks, Anna.
*  Awkward, isn't it? I had to say in full disclosure that we were just meeting on Monday and and she's she mentioned that she was going to do that. Oh, I'm gonna have to. Oh, that is. You didn't plant the question, did you? Did you? Did you tell her to ask that?
*  I would never do that. I don't buy it.
*  I go to great lengths. This is always doing us a surprise. It's ridiculous. Yeah, she just, you know, she couldn't resist anyway. So anyway, I hope I didn't get her in trouble. But so back to the question, though, I do think, you know, this, this, the thing we were talking about with the consciousness and the
*  metacognitive access to your knowledge, to me, that is something that I can see being supported by the bidirectional connectivity in the brain. And so, you know, there's these various theories of consciousness that are actually have this kind of common element of kind of bidirectional recurrent connectivity, global
*  workspace, integrated information, all these different kinds of ideas that are all reflecting that same kind of core element of, you know, this kind of plenary aspect of consciousness that that you have this sort of sense of everything being interconnected and talking to each other.
*  And that is that same kind of thing about like metacognitive access that you kind of have knowledge and that you kind of can take that knowledge and reflect that everywhere else in the brain and kind of operate on the knowledge, right?
*  And this gets really back to ultimately to a lot of things that you see in these kind of more symbolic models, being able to operate on knowledge kind of as as a thing that is really hard to understand in the brain.
*  But I do think these bidirectional connections are a key element, and they're really missing in in most of the AI models. And I have a particular bone to pick about this, which is a lot of the papers and everything talk about recurrent networks.
*  And they're talking about these LSTMs, the long short term memory machines. Yeah. And those in the way that they've actually implemented them are not the same kind of recurrent networks that exist in the brain.
*  The brains recurrent networks are these kind of massive bidirectional attractor dynamics. And these are the kinds of things that were very popular. We talked about a lot in the 80s and 90s in the early neural network work that aren't what happens in an LSTM.
*  LSTM has a single independent neuron that has like a self connection of exactly one. And it's basically just like a kind of memory gate that can latch on to information and hold on to it.
*  But it doesn't have any of this kind of attractor dynamic and this kind of sense that you know, you would have like a state of consciousness in your brain, where all the different neurons would be kind of talking to each other.
*  LSTM models don't support any of that kind of kind of recurrent dynamics of that sort. And we think, you know, we know from a lot of stuff like in perception, and, you know, lots of other cases, language understanding, everything that like top down influences on perception and language understanding and just everything are that kind of top down bidirectional recurrent connectivity.
*  And I think that existing models essentially don't capture any of that. So it's like a huge, a huge, you know, blind spot in the field. And the reason they don't capture it is because it's really, really complicated.
*  It gets into these kinds of neural dynamics that unfold over time and they get chaotic and they, you know, it just adds a lot of complexity to the models.
*  And so this kind of existing paradigm, though, is really wedded to these very deterministic feed forward kinds of activation dynamics. And again, even when they have recurrence, it's not true recurrence of this form.
*  And so, so I think bottom line, current AI is missing dynamics, these kind of interactive bidirectional dynamics.
*  Okay, well, at least current popular AI.
*  I mean, I have, the brain is so massively recurrent. And, and so, like you said, there's these top down projections and that, you know, we'll hopefully get into that with your deep predictive learning framework.
*  Yes. But couple that with, you know, local lateral projections that then feedback, but then you have to combine them in different amounts and different links, different synaptic traversing different numbers of synapses.
*  And good God, it's messy. And I don't have a good picture in my head. I don't feel comfortable knowing. I don't feel comfortable just saying, okay, there's top down and then there's lateral and they have different functions.
*  Like I can't wrap my head around what might encompass all that. Do you, do you have a principled way to think about that? I mean, I know you do.
*  Yeah, so I think about the lateral specifically is really important for inducing topology. If you and you know, everything's anytime you have bidirectional connectivity, there's a certain common element, which is this kind of, you know, mutual, mutual determination, right?
*  That you have that really strong interdependence between the neurons. But, you know, if you want to make a distinction, the lateral stuff is really important for enforcing kind of, you know, the organization topographically of, you know, different representations of similar items are in similar parts in the brain.
*  And that's probably really important for, you know, just basic connectivity patterns. We know that connectivity in the brain tends to follow these kind of, you know, neighborhood topographic kinds of wiring patterns. And when you have something as big as the actual brain, you really have strong wiring constraints.
*  And so, you know, the AI models have these really, you know, massive convolutional type of kernels and have a similar kinds of biases because of those kind of convolutional kernel-like organization to organize things in these topographic ways.
*  And so, you know, I think of that recurrent connectivity as sort of, yeah, again, just sort of organizing this stuff to fit with the wiring diagrams that are the wiring constraints that we have to have in the brain.
*  But the bidirectional, the between layer bidirectional stuff is where you get the more interesting kind of really top down kind of, you know, it's like, I have a concept of what I should be seeing or hearing.
*  And it really changes, like, literally what I see or hear, you know. It's like you really get that kind of modal completion, like the Kinesa Triangle, like pops out, you know. It's not like it's just kind of like, oh, I thought I saw a triangle. It's like, I see a triangle, you know.
*  Right. Okay. Well, I won't bother you with the recurrence anymore because I mean, I know that there are those two main stories, but well, we'll move on.
*  So I want to talk about Libra. Before we get there, I know that learning is, you consider, one of the most important aspects of cognition. And I think it's really hard to argue with that.
*  I had Tony Zader on my podcast and he makes the argument that the vast majority of learning that we do happened throughout evolution and were born with.
*  And that if you compare that amount of quote unquote learning, which is just evolution, he doesn't call it learning, it's evolution.
*  I mean, you can kind of soup it up and call it learning. But that amount of learning is much larger than the teeny amount that we learn to get us by during our lifetimes.
*  What do you land on this?
*  I disagree because I think we have a huge amount of subcortical, kind of evolutionarily wired, kind of, you know, again, like all the motivational stuff.
*  There's a huge amount of stuff that we are kind of born with and, you know, that is evolutionarily determined.
*  But if you look at development, you get this really interesting kind of transitions where, you know, as soon as the cortical side slowly starts to kick in, you get these amazing regressions where we, you know, babies look like they're really good at recognizing faces and all of a sudden they just fall apart.
*  And that's because, you know, the cortex is relearning everything from the ground up, I think.
*  And I think, you know, that's the kind of the core principle of like what drives my research.
*  And I think it's the core assumption that, you know, I know I had this conversation with Jeff Hinton and, you know, various people who do, you know, backprop AI type models, you know, they motivate this thing by saying, you know, look, the cortex is essentially a blank slate more or less.
*  You know, there's this you want to you want to qualify that statement.
*  But, you know, that the secret to human intelligence, you know, so the story goes, is finding the learning rule because it seems like we do learn the vast majority of what we know.
*  And, you know, there's so many examples like, you know, it's impossible for evolution to have enabled us to do reading and writing because, you know, that's such a short period of evolutionary time.
*  That's a huge part of what we do.
*  And just, you know, the general, you know, we don't know for sure, but it seems like our language and our culture and all the things that we, you know, that kind of make us smart are fairly recent, you know, in evolutionary times.
*  And most likely not something that, you know, is just like coded up evolutionarily.
*  So, you know, I think if you put all these pieces together and you just look at, like, you know, how does the cortex organize?
*  How does it develop?
*  It seems like it's mostly learned.
*  I mean, I think that there could be the case made for, you know, mice, for instance, that don't need a lot of rearing.
*  Yeah.
*  Humans are OK. So when we talk about wonderful cognition, we're always talking about humans.
*  Right.
*  But, you know, so Tony gives a lot of examples of, like, burrowing field mice, you know, and how they're different and all that.
*  But humans also take a long time to develop and they come out, we come out completely helpless, basic, more or less.
*  Yeah. So we might be kind of a special case.
*  And so the learning.
*  Exactly.
*  The ratio might be higher for us than other lowly, lowly animals.
*  Absolutely. Absolutely.
*  Exactly.
*  And that's always, you know, I think it's a fascinating question.
*  Like, to me, like, again, I think it's easier to understand how we could come up with, you know, just from a technology perspective, a learning rule, an amazing learning rule that, like, now enables us to learn, then to understand kind of like, given all that time of evolution, you know, how can we capture that?
*  Like now, you know, evolution is a very, very computationally expensive process.
*  And so if it if we have to, if we have to fall back on that, it's going to be like, you know, it's too much work.
*  So it's just not practical.
*  All right. Let's talk about Libra.
*  Shall we?
*  Yeah, sure.
*  So this is like your, your baby.
*  I mean, one of your, your, your digital baby.
*  Yeah.
*  What's Libra?
*  So it's basically, you know, this project that I started back in grad school.
*  And at that time, I didn't know it was in grad school that you started it.
*  Yeah. And at that time, there was really this kind of sense that, you know, there's first of all, a lot of excitement about neural networks back then.
*  And there are these different kinds of neural networks and some of them were like Hebbian kind of self organizing networks and other ones were error driven backdrop networks.
*  OK. And and so my feeling was, well, both of those things are really important kind of learning principles.
*  Why can't we just put them together in a coherent framework so that we can kind of take advantage of both of those really important things?
*  So, yeah, so the original idea was just to put, you know, self organizing associative learning, which is another term for it that happened to fit with this this acronym.
*  So Libra literally stands for learning in error driven and associative biologically realistic algorithms.
*  And so the project was to sort of just say, well, you know, we can we can do associative learning and we can do error driven learning and we can and we can put it together in a way that's biologically kind of plausible, biologically based.
*  And so those are kind of my main themes that have driven my research throughout is like, you know, I want to know how the brain works.
*  So it's biologically realistic and I want to know how these learning principles operate.
*  And so error driven and associative and then the whole kind of Libra word is supposed to be like this balance, this process of balancing and coming up with something that that's kind of, you know, kind of integrating and balancing different forces and not being kind of like extreme in only error driven learning or extreme and only one way or another.
*  And furthermore, as a metaphor, kind of also balanced at the level of analysis.
*  So a lot of people think you have to do like fully biologically based models like, you know, really, really detailed computational neuroscience type models.
*  Other people, you know, like back prop nets.
*  Fine. We can be very abstract.
*  And I'm trying to find that kind of middle balance again point in between.
*  It's that sort of, you know, what does a really kind of reasonable job of capturing the biology, but also allows us to address these large scale computational questions.
*  So that that kind of balance point in the middle.
*  I mean, it seems like Libra is full of compromises and allowing the constraints and compromises to drive.
*  But yeah, because it's I mean, the other thing is, well, there are 400 things to get to with Libra because it's become a monster.
*  Right. But you kind of have it's it's a model of the brain at this point.
*  I mean, did it? Yeah. Did you start off wanting to to simulate a human brain when you're in?
*  Oh, yeah. Well, that's always been my goal. Basically, you know, if you know, it's like I want to figure out how it works.
*  And to me, the technique to figure out how it works is to, you know, put it in computer code.
*  And so, you know, one definition of Libra is whatever my current understanding of how the brain works is, you know, pretty much that's that's what it is.
*  But, you know, I think one thing that I've really taken to heart from, you know, Alan Newell really articulated this principle early on that, you know, you want to have some kind of cumulative process in your in your development of computational models that you don't want to be just like making random models of a bunch of different things.
*  Because then, you know, you're kind of answering all these separate questions, but you're not really tackling kind of something more coherent that really builds a single explanation that can account for a really wide range of different data.
*  And, you know, the basic principle of, you know, have have the simplest theory, but no simpler that accounts for the widest amount of data is kind of the right criterion for thinking about what you want for a theory.
*  And, you know, a lot of times you for any particular phenomenon, you can always come up with a particular model that does a reasonable job of explaining it.
*  But if that doesn't also explain all this other stuff, then it's like, okay, well, how many theories do we need, you know, so that cumulative approach has always been there.
*  And so we do have a strong bias, you know, in my lab to sort of say, well, if it's something we can explain with existing principles, let's do that instead of just like cooking up a brand new model just to explain this one thing.
*  I mean, how often do you when you're going to tackle a new cognitive function, let's say, and you want to use the principles that have now you've whittled a little bit over the years and have fit with 14 other cognitive functions and that you're going to add a new one.
*  How often does it screw up the whole thing and you have to either bring in a new thing or completely reinvent the, you know, the learning function or, you know, whatever function that you that you're dealing with.
*  Yeah. And mostly a lot of the earlier work that we did was kind of basically saying, okay, look, we've got this this vocabulary of mechanisms.
*  And now let's go look at different parts of the brain. Right. And so you say like the hippocampus, the prefrontal cortex, etc.
*  And there the idea is like, okay, well, within this common vocabulary, we have different parameters.
*  And we can say the hippocampus is an area that, for example, has a really high level of inhibition.
*  And so the representations are very sparse. There's certain patterns of connectivity.
*  And when we put those things into this kind of common framework, it behaves differently in a way that fits with like this ability to do episodic memory.
*  And so that's a kind of nice explanation that says, okay, well, different parts of the brain have different parameters.
*  And so it doesn't really change the overall framework because we're kind of taking the same principles but applying it in a new brain area.
*  But more recently, we have been doing kind of more of this, like, you know, flipping over the apple cart or something where we're adding these principles of like, how does the thalamus interact with the cortex?
*  And this is something that was very much missing in our previous models.
*  And now we have to say, OK, well, all this stuff that we were thinking about in one way was kind of only part of the picture.
*  There's this kind of thalamic component to everything.
*  And so now we're kind of revisiting a bunch of stuff to to change how we think about what's happening there.
*  Well, the main brain areas, I guess it's interesting because you talk about having main brain areas.
*  But then, you know, then you're adding thalamus.
*  That was going to be one of my questions because this predictive learning, the thalamus is pretty damn important for within that circuitry.
*  I was like, well, he's going to be adding thalamus to Libra then soon.
*  Yeah. Maybe next. You know.
*  So, yeah. I mean, is that but it's kind of started off with like three or four main brain areas and then you keep like plugging a new one in.
*  So what are the main ones?
*  And then and then we can go from there.
*  Prefrontal cortex.
*  So, yeah. So so in terms of, you know, so that and just to clarify, there there's a sense of like these kind of more micro scale principles.
*  So like the idea of like, what do neurons do and what do small smaller scale networks of neurons do kind of in general?
*  And then you have this kind of architecture level question of like, what are the different parts of the brain and how are they specialized?
*  Right. And so that's like the macro scale organization.
*  And so at the macro scale, you know, I think there's pretty solid agreement that like the frontal cortex is doing something different than like the posterior cortex.
*  And so that's a big dividing point.
*  And then, you know, the hippocampus clearly is specialized relative to those other cortical areas.
*  So the tripartite kind of organization into posterior cortex, hippocampus and frontal cortex is very, very widely adopted and very clearly supported.
*  And that's the you'd say that's the core of that's the core.
*  You know, if you want to do if you want to understand cognitive level phenomenon, you pretty much need those three players.
*  And then, you know, when you talk about frontal cortex, what we found is that you really start to need to involve the basal ganglia.
*  Right. So now and this is this is the nature of how it goes.
*  Right. So you kind of like, right, you go down these rabbit holes and you're like, OK, well, if we want to understand how the frontal cortex works, you know, what is that basal ganglia thing doing in densely interconnected?
*  You know, you can't really understand just the frontal cortex.
*  You have to understand that system. And so in the same way, you know, I think the thalamus, instead of thinking of it as like a module in the overall system, it's more like part of the posterior cortical and frontal cortical.
*  It's basically part of all cortical networks.
*  And so it's more like adding to the micro scale rather than adding to the macro scale.
*  And so that's a key point. Like, you know, do you put thalamus as a macro scale player like the hippocampus or is it a is it a micro scale kind of ingredient that's that's common across all these different areas?
*  And that's more how we think about it.
*  Let's go ahead and talk about the circuitry and just the idea because then and then we can bring it back to Libra and how it fit in fits in because there's a you know, the classical thing is the cortical, the canonical cortical computation in the cortical column.
*  And this is not that well, it's sort of that right.
*  It's sort of that. And so and so, you know, once you start looking at the anatomy, it's actually remarkably clear.
*  And that's great for, you know, computational modeling that there's a there's a real story to build on there, which is that there's layer six, the deep layers of the cortex has multiple kind of sub layers.
*  And so layer six is kind of the deepest of the deep and it has these cells called CT cortical thalamic cells that project down to the thalamus.
*  And and so, you know, once you start talking about the thalamus, you also then have to talk about the different lamina of the cortex.
*  And so in the way we think about it, the previous models that we had been developing were all about the superficial layers of the cortex.
*  So layers two and three, which everybody, I think, pretty much agrees are kind of the main information kind of representation processing kind of areas of cortex.
*  They're densely, bidirectionally interconnected and they have these pyramidal cells that, you know, interconnect all the different areas of the cortex.
*  And so they're the kind of main players in the cortex. And then you have these deep layers which have in general more restricted patterns of connectivity.
*  And again, that we said the cortical column, you know, you have a general topology where you have input coming in layer four, it goes up to the superficial layers and two, three,
*  and then it comes down to the deep layers, right, as kind of an output pathway.
*  And then, you know, what's interesting about the thalamus is that deep layer connection through the cortical thalamic cells then goes back up.
*  It's a loop and it feeds back up into layer four and it kind of completes that whole circuit.
*  So really you have a kind of column level organization that involves all of those kind of cortical lamina and the thalamus in a loop.
*  And that's why we think of it as kind of like, you know, a kind of micro scale thing.
*  It's like a canonical architecture that exists across the entire cortex.
*  Does it get called canonical yet? Because that's the word I was thinking as well.
*  Oh, yeah, I think there's a paper from, geez, Shepard maybe? Sherman? I can't remember.
*  Sherman and Guillory have the main thalamic paper, but somebody else called it a canonical cortical circuit.
*  Canonical thalamic corticals. Yeah, something like that.
*  Yeah. So then you have to say, OK, well, what, you know, it's like this is always the challenge.
*  OK, you've got all these different parts. What are they doing? Right.
*  And that's really, I think, the key place where a computational approach can sort of give some insight.
*  It's like if you look at it from electrical recordings, you know, the neuroscience says, well, neurons kind of have similar tuning curves in the superficial and the deep layers, even in the thalamus.
*  So if you just kind of look at what are the neurons like firing at, they're very similar.
*  And so it's like, OK, what is it? You know, and if you actually look at the Sherman and Guillory account,
*  they kind of have a fairly vague story about like modulation, right?
*  So that the thalamus, you know, has this kind of top down modulation of what's happening in the cortex.
*  And that makes sense in terms of like attention. And so a lot of people think that one of the main functions of the thalamus is attention.
*  Just to just to back way up, the old story of thalamus is it's just a a pass through for right.
*  Right. For the relay feed forward relay feed forward relay to just to spread it around the brain.
*  But that's changed in recent years. And yeah, so there's this attention story.
*  Right. So there's a there's the attention story.
*  And there's certainly a lot of evidence consistent with that, that that you see these kinds of signals and deficits if you have damage to the thalamus, that you you have certain kinds of intentional impairments.
*  But, you know, even then it's like, OK, well, we needed all this extra circuitry just for attention.
*  Maybe, maybe not. And so that's where we started staring at the circuit and coming up with this kind of predictive learning story.
*  And so I guess we can get into that.
*  Let's just let's talk about it. Yeah. I mean, it's it's it's it's a beautiful story.
*  So, yeah, and it's it's a, you know, without visuals, it's a really hard story maybe to talk about.
*  But, you know, but but the gist of it is that would you like to do the gist of it or would you like me to do the gist of it?
*  Well, I'd be curious to hear your gist. I'll give my gist of it.
*  Yeah. I mean, there's a lot of gisting, but the gist of it is that like a lower layer lower area in like, say, early visual cortex projects to the thalamus.
*  And a higher area projects back to the thalamus.
*  And they do so at sort of different. Well, I see I'm going to watch this from the beginning, like the importance, the relative importance of what to say.
*  But they do so in in such a timing that the projections from the early layers are these like really focal bursting projections.
*  Whereas the feedback projections from the higher area that come onto the same within the same circuitry in the thalamus are more of these lower firing, but tonic tonic.
*  More tonically active. Yeah. Yeah.
*  And so what happens is the way the way this all works is that the higher area, let's say V2 or later visual cortex, sends thalamus a prediction.
*  And then the early area, the sensory incoming information sends what the real sensory information is, which you guys call the outcome and a very bursty way just after that prediction.
*  And this all happens over and over and over at a cycle of 10 Hertz. So every cycle is 100 milliseconds.
*  That's the sort of my gist of it. You can fill in the rest of the gist.
*  Yeah, exactly. Exactly. That's great. That's awesome.
*  So so that's exactly it. That you that you're essentially constantly making predictions and you're constantly getting kind of the right answer, the bottom up sensory answer.
*  And that you have a circuit that basically allows you to kind of represent the prediction and then represent the right answer.
*  And then the temporal difference between those two over the thalamus is kind of the error signal that then kind of propagates back up into the cortex and trains up the cortex to be a better predictor.
*  The next the next prediction. Exactly.
*  And and you know, there is a large body of work over the many years thinking about how the brain might do predictive learning.
*  And so the normal kind of default model for that, so to speak, the conventional model for that involves cells in the cortex that are kind of explicitly computing some kind of difference between a prediction and the outcome.
*  And these models typically are based on Bayesian kinds of math.
*  And and it's nice because the Bayesian framework basically has a way of representing kind of a top down expectation of an internal model.
*  This is what you would expect to see. And then you get kind of the bottom of data and then you can kind of compare, you know, did the bottom of data fit with your top down model or not.
*  And so the Bayesian framework is a very natural framework mathematically to think about this kind of predictive learning idea.
*  And so, you know, most recently, Carl Friston, for example, has written a lot of papers, you know, embracing this kind of Bayesian idea.
*  But again, it goes back pretty far.
*  Rowan Ballard are one of the most early, widely cited papers on this topic.
*  And so we're basically offering a different way that the biology may support a similar kind of computational objective.
*  And so instead of thinking about there being these explicit error coding neurons, you have this temporal difference operating over the thalamus that that kind of codes the error.
*  And an advantage of that is that nobody really has found solid biological evidence for these error coding neurons that that kind of standard approach, so to speak, predicts.
*  And so, you know, it's a very I think it's a really compelling overall computational idea that we learn by predicting because, you know, it really answers this question of like learning requires data.
*  We know that, you know, it's a big data problem.
*  You need constant sources of data to learn on.
*  And, you know, the amount of quote unquote labeled data that we as as humans plausibly receive is minimal.
*  And so we need a bunch of unlabeled data to learn on.
*  And how do you learn on unlabeled data?
*  Mainly, you have to turn it into some kind of kind of predictive regenerative problem where basically your job is to encode and predict what's going to happen next.
*  And if you can do that, you can then say, well, I've now learned kind of an internal model of the world such that I can actually predict what's going to happen next.
*  And if I do that, it obviously has, you know, survival advantages. I know what's going to happen. I can anticipate what's going to happen.
*  I can behave in a way to avoid negative potential future outcomes and seek out positive ones and all those kinds of things.
*  And so I think it makes sense from a big computational picture that we want to be doing something like predictive learning.
*  And so this this model basically kind of just very serendipitously.
*  We just happen to be looking at this circuitry thinking about, you know, we've got this lever model.
*  There's this weird circuitry in the thalamus. What is it doing?
*  How do we think about that? How are we going to incorporate that into our model?
*  And then it kind of all started to fall into place with this idea that it might be doing the actual predictive learning.
*  But hang on, because you could be looking at anything, any data and say we have this Libra model we could do.
*  So, I mean, there must have been some more intriguing reason to be looking at the circuitry of the thalamus.
*  Well, I mean, it's so important.
*  And, you know, it's like anything like, again, this idea that you kind of do research incrementally, you start with problems you can solve and you move on.
*  You know, we felt like, OK, we kind of understand, you know, sort of, you know, a lot of cognitive phenomena with this Libra model.
*  But, you know, we're really missing this key part of the brain.
*  And so it's kind of, you know, we got to that point where we're like, OK, we need to we've done enough with what we have.
*  We need to really start to think about what's missing.
*  What do we need to include?
*  And the attention stuff really was an important motivator, because I think, you know, attention also is a really important shaper of learning.
*  And a lot of the problems also that we see in AI models, one of the big stories in the last few years is including more and more of these kinds of attentional mechanisms.
*  To allow kind of like the same network to do many different things.
*  And so like multitask learning and learning without interfering interfering with what you learned before, these kinds of things all really seem to depend on being able to sort of dynamically take the same network and kind of reconfigure it in different ways, depending on what kind of task you're trying to solve.
*  And that's basically attention. Right.
*  And so so we originally started looking at it from an attention perspective and then only kind of serendipitously started to see, wait, this could actually do this kind of predictive learning.
*  So we really didn't sort of come into it saying, oh, we need a system to do predictive learning at all.
*  It was just kind of looking at those driver pathway connections and saying, those are weird.
*  I mean, that was really the crux of it is like, why is it that there's like this kind of one to one almost pathway where like the bottom up kind of cortical areas are just like, you know, driving these these Islamic representations.
*  It just seemed like that's a very striking and puzzling kind of aspect of the circuitry.
*  And if we could figure out how that would make sense, then maybe we would sort of see what the whole circuit is doing.
*  That's the whole Isaac Asimov. The interesting science happens when you say, huh, that's weird.
*  Yeah, exactly. Exactly.
*  So you're talking about attention being a big story in AI. Back propagation has been a big story in neuroscience.
*  And you, you know, you're like maybe the earliest cited example, your 1996 work on biologically plausible back propagation in the brain.
*  And but then recently, maybe in the last, I don't know, five, six years, we've talked a lot about how back propagation might happen in brains on the podcast here.
*  Yep.
*  And so how does this I know you tested it against back propagation in the paper.
*  And this paper is a monster and it's a real delight. It's a chore and a delight to go through.
*  Yeah, but but it's just super chock full of information.
*  And so you tested it against back propagation and how does it relate to back propagation?
*  And I want to know how you think about, you know, your early 96 work compared to like these days that it's the hot ticket to find back propagation in the brain.
*  Yeah, absolutely. So one thing about that, first of all, is that I yeah, that was one of my early things.
*  I actually did that in grad school. And and I'm really gratified that the current work that people have been doing has actually, you know, recognized that original work.
*  And so people are kind of saying, OK, yeah, this is this is one way to do it.
*  And kind of, you know, not all has been forgotten in the in the, you know, new, new is new.
*  You know, everybody loves the new stuff and kind of forgets about the old stuff.
*  Oh, I think it's a very celebrated paper.
*  So, yeah. So anyway, that's that's been very gratifying.
*  And so the core idea there, you know, just to summarize it, is that you have instead of back propagating kind of like mathematically by going in the reverse direction down axons and stuff like that.
*  So really kind of undoing or reverse propagating through the same kind of biological circuits.
*  You just add a separate direction of connectivity.
*  Again, these kind of recurrent connections that we know exist in the brain, the bidirectional connections that exist in the brain.
*  And so the top down flow of activity from higher layers to lower layers conveys error signals.
*  And interestingly, the way that that works in most naturally in our framework is as this temporal difference.
*  And this temporal difference actually goes all the way back to Jeff Hinton's original Boltzmann machine.
*  That's where I, you know, encountered the idea first.
*  And I don't know where he encountered it, but probably probably Steve Grossberg.
*  It'll hazard a guess.
*  Probably Grossberg.
*  Certainly Grossberg has a phase like top down, bottom up dynamic.
*  So that's absolutely true.
*  So you have to give credit where credit's due there.
*  So anyway, the idea that there is this kind of, you know, phasic difference that you can learn on is the core of that.
*  And I just showed basically that if you just have these top down connections and you literally take kind of the difference in activity when the right answer is kind of present at the output layer,
*  of this network versus kind of the answer that the network itself came up with, you know, its quote unquote prediction or its own, you know, guess, then that difference over time is the back propagation gradient.
*  So these bidirectional networks essentially directly compute backprop and approximation to backprop.
*  But it's not a backprop.
*  And so in fact, what's cool about this predictive learning thing is that it actually plugs into exactly that same temporal difference dynamic.
*  And this is something we realized that we weren't very successful in the paper in kind of conveying that essentially, you know, the one way to think about it is we're just kind of plugging in the pole of the same dynamic.
*  The thalamus as a kind of output layer to generate error signals.
*  But otherwise, it's just exactly the same principles of learning that we had talked about previously in terms of these back propagation gradients in the cortex.
*  I mean, do you have when you have thalamic lesions in the pulvinar?
*  I'm really unadapted to that.
*  Are there learning deficits of the?
*  Yeah. And the early interesting thing about that is that they would have to be very early for most cases.
*  Early cortex. What do you mean?
*  Early in development.
*  Oh, because you already learned that.
*  Because you're already learned up.
*  Yeah.
*  Exactly.
*  So it's just exactly the same principles of learning that we had talked about previously in terms of these back propagation gradients in the cortex.
*  So you're already learned up.
*  Because you're already learned up.
*  Yeah.
*  Exactly.
*  And so most of the cases that we know about are kind of cases, you know, and acquired, so to speak, you know, strokes and stuff.
*  And so there you see mostly attentional deficits because, yeah, the cortex is all wired up, you know.
*  So but a major prediction would be that if you did do like a neuroscience level, you know, test in some animal with enough of a developmental window that you could kind of get it early and you would actually see learning impairment.
*  So I'm very excited if somebody wants to test that.
*  And you guys talk about that. I'm sorry. I have a million questions.
*  You guys talk about this in terms of V1 to thalamus and V2 back to thalamus, right?
*  So kind of early visual cortex, but it's a principle that could just apply across cortex.
*  Absolutely. Totally. So it is, again, it's like this microcircuit kind of idea.
*  It's something that would be present everywhere. And it is present everywhere.
*  You know, we know that these patterns of connectivity are present everywhere.
*  And you think it's the same canonical function everywhere?
*  Yep.
*  So one of the neat things is just the timing of all of all of this, because you bring you can bring oscillations in and say it happens all within a hundred milliseconds over and over and over.
*  And it made me think and I don't know if you guys talk about this, whether if someone has a slightly faster alpha, if Bill has a slightly faster alpha than Jenny, what does that mean about their ability to learn?
*  And I don't want to poor Jenny or poor Bill. Who's who gets the short end of the stick?
*  Exactly. So it's really interesting. So we actually looked at some of this.
*  There's a data set that we had of people doing saccades in visual scenes.
*  And we had electrophysiology recordings in posterior cortex.
*  And you could really see strong individual differences in the timing, the phase relationships of these alpha signals.
*  And you could see, you know, there's it's the variability is not massive.
*  So people do have pretty amazingly consistent hundred millisecond, 10 hertz kind of alpha overall.
*  But, you know, the precise kind of, you know, there were definitely individual differences in in the duration and also in the kind of phase alignment.
*  And it was striking to me, you know, even though there was a lot of consistency, there clearly were a lot of individual differences, too.
*  And so I really want to go back and see just exactly your question.
*  Like, what is the effect of that? And, you know, there's this idea that that was very popular and very controversial from Paula to law and Mike Merzenich.
*  And the idea that developmental dyslexia and generalized language disorder, I forget what the right term is.
*  There's a there's a generalized language disorder term that I can't remember what it's called.
*  But that those were due to timing due to these kinds of differences in fine grained brain timing.
*  And it's controversial because, you know, they started a company and there was kind of commercial conflict, you know, of interest type of issues in in how they presented their research and maybe some difficulty in replicating some of their their results.
*  There was lawsuits. So but I do think that there's some core element to that, that like, you know, just having these these rhythms, if these rhythms are really driving our fundamental kind of learning processes, then it does seem like, you know, little changes in that rhythm could really have some kind of effect.
*  I mean, there's a there's a limiting factor as well, probably with how fast synapses can actually change.
*  So if you can't you can't go to write, you know, a thousand hertz or something, you can't speed it up too much. Right.
*  Exactly. But at the same time, if you wait too long, your synapse might be not might not be tagged or something, you know, to exactly actually change.
*  I mean, you're talking about the, you know, this dyslexia theory.
*  And one of the things that you harken back to in the paper is a 1991 Mumford theory about thalamus being a blackboard.
*  Yeah. And yeah, yeah.
*  I hear all the time these days that what what I hear neuroscience needs a lot of things, but I hear neuroscience needs more theory, less data.
*  We have enough data now. We need more theory.
*  And I just and then I keep like reading papers like this and and reading about some theory that was 30 years ago, 40 years ago.
*  Yeah. And yeah, that's now coming back and relevant again.
*  And I'm just wondering, you know, are the theories there but buried in the literature or and just weren't paid attention to at the time?
*  Or do we really need theory? Like what what do we need?
*  You know? Yeah. Well, I think what we need is is basically that kind of collaboration between theorists and and empirical research to really take the theory and make it testable in a way that that somebody can actually do.
*  And, you know, with the advances that we have now with optogenetics, it's really amazing what people can do.
*  People can test theories in a way that just wasn't possible before.
*  Like for this theory, you know, you need to be able to disrupt, you know, a particular pathway or, you know, disrupt a particular channel in these in these circuits that gives rise to the timing dynamics, you know, various very, very precise kinds of manipulations.
*  Whereas before it's like, let's cut it out and see what happens, you know.
*  So being able to manipulate the system at a fine grain level like that is essential for for testing these theories.
*  The other thing I'll say is that a lot of these early theories like Francis Crick, for example, has a very famous paper on attention and the thalamus that was based on anesthetized data, data from anesthetized animals.
*  And what I've seen in the last few years is a huge overturning of a lot of prior literature that was all done with these anesthetized animals.
*  And the behavior of neurons is extremely different in the kind of awake state versus the anesthetized state.
*  Shockingly, yeah.
*  Shockingly. Big surprise, right? At some level.
*  But people never really appreciated that.
*  And so, you know, a lot of these kind of especially like the bursting dynamics are really absent.
*  The downstate, upstate dynamics are really absent in the waking state.
*  And so a lot of the theories that people had built up kind of were based on the wrong data in some sense, because they only really apply to these kind of phenomena that don't really happen, you know, in the relevant state when we're actually awake and thinking.
*  So you do have to kind of, you know, it's always everything's always a process of kind of, you know, figuring out what the right data is and not getting too attached to data that might be the wrong data.
*  And, you know, so a lot of theories like Crick's theories, you know, especially about these attentional things, I think, are basically have been invalidated because of these results.
*  And so, you know, yeah.
*  I mean, another loud cry, or at least in my neighborhood of hooligans, you know, that I don't know how loud it is amongst, you know, the rest of the field is that I mean, speaking of the right data is that well, you know, that behavior is much more important to than we previously realized.
*  Ecologically valid behavior and that behavior can tell us some people go so far as to say that behavior can tell us more about the brain than the brain can tell us about the brain.
*  And that's that gets thorny.
*  But so Libra itself, and we can always come back.
*  We can just jump around, which is fine.
*  Libra itself is I mean, it's not a robot.
*  It's a it's a it's a cognitive functioning neural network based cognitive architecture, but it's not embodied.
*  Right. I know you have plans to embody it.
*  So I'd like to ask you because I'm going to have Chris Elias Smith on the show in a few weeks here.
*  And he hates you, by the way. No, I'm just kidding.
*  But he we're going to talk about spawn his cognitive systems architecture.
*  And I wanted you to kind of compare Libra and spawn as a preview.
*  Oh, yeah, for sure.
*  And, you know, I think the a lot of the there's a lot of commonality and therefore, you know, a lot of opportunity to draw kind of key contrasts.
*  And, you know, spawn, I think, you know, does have that advantage of being something where you have a lot of control over what the system does.
*  And a lot of what they've done with their architecture is is kind of configure really building on work that Tony plate did in the 90s, these holographic reduced representations to solve the binding problem, to do kind of, you know, fairly complex, elaborate forms of cognitive information processing.
*  And and so I think they're able to get a lot of functionality out of the system because essentially they have a lot of control over what's happening.
*  And whereas in Libra, we're more at the mercy of like, what can we train the system to do and what kind of dynamics are going to emerge as we try to train these systems?
*  And so we have a lot less control. And so I think we can't, you know, they have like models of doing like Raven's progressive matrices and lots of complicated kinds of tasks.
*  On the other hand, those models also provide then kind of perhaps less insight into how the brain really does it, because it's kind of reflecting more of an information processing kind of prior assumption about how it could work.
*  And and one question I would ask about these models is how much have you learned in making that model relative to what you kind of came in with it? Like, how much did the model teach you in making the model?
*  Because I feel like once you have a framework where you can basically get the model to do what you want it to do, that's nice.
*  But it also means that the model has less opportunity to teach you something that you didn't otherwise, you know, kind of know about the brain itself or about the functioning of the brain, about how the how that cognition actually might work in the brain.
*  You know, I don't feel like the model of Raven's progressive matrices, for example, that they have gave me a lot of insight into how like the brain might actually solve that problem.
*  Likewise, with other models that we've seen in AI, where they are now also taking on these Raven's progressive matrices tasks, which are kind of the one of the classic tests of general intelligence.
*  And that's why they're very attractive to model with these kind of AI models.
*  But the whole thing about it is that it's a test of your on the fly ability to solve these kind of novel problems.
*  And yet they're training these models or hand configuring these models kind of in a special purpose way to solve that task.
*  And once you do that, it sort of negates the entire point of the of the task, which is that it's supposed to be a transfer task, a novel task that you've never done before.
*  And so it's like, yeah, I can get a system to solve that task. That's not the problem.
*  The problem is, how do I get a system that's never done something like that before to figure out how to solve the task on the fly on its own?
*  You know, and that's the real problem.
*  And again, I think that's where, you know, having kind of introspective access to, OK, well, gee, how am I going to solve this task?
*  Well, I know there's these patterns, you know, just that whole process we would introspectively go through in thinking about how you would tackle a new task.
*  That kind of flexibility, I think, is what is what's missing.
*  Good. That's good. I'm going to play your clip there.
*  When I talk to Chris, you'll be the you'll have the question.
*  Yeah. And don't tell him the other the other the other question to ask.
*  Yes. Yeah. Don't tell him. I won't tell him.
*  The other question to ask Chris is, you know, do they clearly explain that the spiking is added on after like you program the model using dynamic equations, continuous dynamic partial differential equations?
*  And then they kind of add on the spiking afterwards.
*  And when I learned that, you know, I was kind of like because he, you know, in his talks, he makes a big deal about how it's a spiking network.
*  Right. But it's kind of first a not spiking network and then it becomes a spiking network kind of after the fact.
*  And so to me, that sort of was like, OK, well, how much is really different between the spiking network and the original kind of, you know, differential equation version of the model?
*  So anyway, you could ask him that. All right. Shots fired. I like it.
*  One of the one of the things about Libra that you've built in is you can flip switches and turn on biological realistic details and turn them off depending on how fast you want it to run and what what you're concerned with.
*  Yeah. I mean, what has that taught you? What I want to know is like what building Libra and the overall large perspective, what has it taught you?
*  I mean, you're you're wondering what it's taught Chris. What is taught Chris?
*  Yeah. And that's where I think, again, another major question that we're wrestling with in the lab right now is about spikes.
*  Ah, OK. And I think one of the big limitations that we've learned is in scaling up these models that you get an interesting kind of kind of a heat death.
*  People talk about like, you know, as the universe ages, there'll just be this increase in entropy and nothing, nothing interesting will happen.
*  And the same kind of thing happens due to the law of large numbers as you scale up these networks that they really thrive on kind of randomness to select subsets of neurons to encode, you know, some piece of information, one face versus another face.
*  And as you scale them up and you have this law of large numbers, basically, statistically, if you have ten thousand different synaptic inputs, the standard deviation of like how much input you got from one pattern versus another pattern shrinks to the point where basically every neuron is sort of getting some pretty similar overall level of input.
*  And it's very hard to sort of choose like which neurons to represent one face or another face.
*  And that's that that scaling problem intuitively seems like seems like something that adding noise right in the form of all the noise we associate with spiking would solve that there's a sampling process taking place that, you know, the neurons in some sense, the synaptic weights are representing some kind of probability distribution.
*  But that the active process of, you know, activating the neurons and information flow in the brain is kind of like a statistical sampling process, sampling from some larger distribution that's encoded in the synaptic weights.
*  This goes back to constraint satisfaction and Boltzmann machines again, really.
*  So, yes, exactly.
*  So the Boltzmann model is exactly that.
*  It's a it's it's a sampling process and all the Bayesian models with the particle filters are also the set sampling processes, Gibbs sampling, et cetera.
*  And so so somehow we're totally missing that in the Libra model.
*  It's great for working on small scale models because they're very deterministic and easy to work with and things like that.
*  And again, we have these switches, like you say, and we could turn on spiking.
*  But every time we turn on spiking, it doesn't quite work.
*  And so it sort of works, but it's like it doesn't learn as reliably.
*  And so I feel like we're missing a critical element there in bridging down to the level of spiking and that once we have it, we may then have, you know, a better ability to scale up the models.
*  And this is another case where the work in in A.I. has also really kind of shined a light on a computational principle that we think also relates to this, which is in the form of these things called variational autoencoders.
*  And there's been a lot of interest in these.
*  And they they are, again, a Boltzmann like kind of sampling process that operates in a neural network.
*  And they when you do that, they actually generate much more kind of systematic, generalizable kinds of representations.
*  So there's some hints there that really figuring out exactly how spiking works and capturing that again, you know, in a way that integrates with our learning mechanisms, which is the key thing.
*  Then we could really kind of take take things to the next level.
*  So that's the that's the goal.
*  Is it important to you to get to spiking or would you be satisfied without with a solution that didn't involve spiking?
*  Yeah, and it's kind of like the thalamus.
*  Like, you know, I wouldn't want to just add the thalamus just so I could have a box on my model that says thalamus.
*  I want to figure out like what computational function that those spikes are actually doing so that, you know, when I put it in, I know like, OK, we're having spikes not just because they're there, but rather because they're doing this exact kind of computational function.
*  And so that's where I think some of these insights about, you know, the sampling process and the scaling give us a clue as to what the importance of the spikes are.
*  And then we can kind of connect to connect it with the computational story and the biological story and build those bridges.
*  I mean, what has what has playing with the biological realistic switches on and off?
*  What has that taught you about, you know, functionalism and multiple multiple realizability and what actually is important in AI and in simulating a brain?
*  Right.
*  Any major takeaways?
*  Yeah, I mean, the extreme version of it is that it's not really about the ability to simulate a brain.
*  And the extreme version of that is like, you know, we have this collaboration with the folks doing act our models.
*  Yeah, that's that's another cognitive systems architecture.
*  There you have a very high level kind of description of what's happening.
*  And I feel like, you know, also going back to your question about behavior, that's a framework that almost exclusively, you know, is it's constrained by modeling actual behavior.
*  Right.
*  And they also came up with this constraint about timing that, for example, the basal ganglia has to essentially update every 50 milliseconds.
*  And it turns out that 50 milliseconds is the beta rhythm and the basal ganglia oscillates at the beta rhythm.
*  Gate gate gate gate gate gate gate gate kind of thing.
*  Exactly. Yes.
*  So the opportunity for gating in the in the basal ganglia essentially opens up at this 50 millisecond time frame.
*  And so, you know, that's like a coincidence that's too, too perfect to ignore, I feel like.
*  And and so I do think that, yeah, you can learn a lot from behavior and you can learn a lot from these large scale models.
*  And just saying, like, you know, from from if you if you have something that's like a basal ganglia, which they do in the kind of production firing and you have these maintained kind of goal states and you have declarative memory, you know, how do those macroscopic kind of architecture level elements kind of work together to do cognition?
*  That's something that's really hard to address at a more biological level, right?
*  Because the models that you're working with are so, you know, they would have to be so large scale and so complex and so so hard to understand that having that that kind of much more compressed, simplified framework allows you to kind of get to the essence of the information processing and the division of labor among those systems.
*  So I think it's essential.
*  I mean, I think I'm a big advocate of multi-level modeling, you know, just like there is no one right model, even though we try to hit a middle ground with our models.
*  Like you're saying we have switches that allow us to kind of go up and down a bit.
*  And sometimes when you go to act or actually code it up act are in our simulator.
*  Okay, because I wanted to be able to first of all understand it and you know, coding is how you understand things, at least for me.
*  And then I also wanted to be able to kind of go back and forth with these act our models, understanding the overall information flow kind of dynamics and then try to relating those and maybe even kind of swapping parts of it out with like a Libra model where the rest of it is an act our model that kind of idea.
*  So is building the models from I mean, it's kind of from the ground up because you know, at bottom they are connectionist neural networks, right?
*  And has simulating at that level?
*  Has that changed the way that you think about any mental functions?
*  Or is it always the here's working memory and and we know we have working memory quote unquote, and we're going to put it in.
*  And here's and then and then we put the network in or is it have you ever had the experience of running the model and maybe you added a new function or something and then I don't want to say emergent but there's some new property that makes you think differently about some mental mechanism, some mental function.
*  Does that make sense?
*  Absolutely. Yeah, I think the biggest case where that happens and this happened to me multiple times is with these kind of binding problems, which come up a lot in when you start to think about kind of again these larger sources of thinking.
*  Again, these larger scale architecture level models.
*  You know, you think about this part of the brain represents X and this other part of the brain represents why and and if you just kind of have that large scale compartmental kind of understanding.
*  You always have this problem of like, well, how do you coordinate? How do you bind those those representations across these areas?
*  And I think that's where when you run like an actual learning model that you know uses distributed representations. A lot of times it just kind of solves those problems kind of along the way.
*  And it's a virtue of the kind of high dimensional nature of distributed representations. It can kind of have both systematic and kind of idiosyncratic elements represented in these very hard to imagine high dimensional spaces.
*  And that's where again our limitations of imagination. Like if we just think in terms of these really simple symbolic like, you know, separated elements, these binding problems seem like a really huge problem.
*  But when you actually like think it's very hard to think in terms of these high dimensional spaces, those binding problems in a lot of ways can kind of go away.
*  It's kind of makes it a robust system almost.
*  And so I do think there's that's a good example where, you know, running the model kind of avoids problems that you thought you were going to have and that you would have had and that you do have if you just kind of have these large scale schematic models.
*  And I think there's, you know, there's an example of this in there's a recent paper that was kind of a manifesto by some computational folks saying here's what's wrong about neuroscience.
*  I forget. I think maybe Richards is the first author.
*  Oh, there's the Blake Richards back propagation of the brain. There's the John Krakauer, We Need Behavior. Okay.
*  I think it's the Blake Richards one. I'm pretty sure that's it.
*  There's a lot of here's what's wrong with neuroscience these days.
*  Yeah, yeah, yeah, exactly.
*  So, but I think the thing about that Richard's paper is, you know, it's like neuroscientists are asking these very local questions about individual neurons.
*  Right. And the computation is distributed, first of all, okay, and also kind of governed by these learning processes.
*  And so if you think about like, what is the system learning to do? And how is the information being transformed across these distributed high dimensional representations?
*  You get a very different picture and you ask very different questions than if you're just like saying this individual neuron has to code the task relevant information in its own single individual neural firing.
*  And I'm going to try to understand how the brain works. You know, neuron by neuron.
*  I totally agree that you can't understand how the brain works. Neuron by neuron. You know, you really have to understand these distributed.
*  Yeah, well, I mean, neuroscience, it's like Hubel and Weasel. Right. I mean, yeah, but that's the techniques that were available.
*  I feel I think I feel defensive because I was a neuroscientist, but I hear these arguments and I think who actually thinks. Yeah. Like who thinks that?
*  So just to be clear that the paper is a deep learning framework for neuroscience. So this is like using the deep learning ideas.
*  Yeah. But as to who thinks it, it's maybe not that people actually think it, but it was kind of also again this thing about the techniques. Right.
*  Yeah. So if you can only record from a few neurons, that's all you can do. Right.
*  And if the story isn't really amenable to being told with a few neurons, then it's kind of like a mismatch between the techniques and the kind of explanations.
*  And you definitely see now in the field of neuroscience, many papers that are looking at population level information and coding and telling, I think, a much clearer story at the population level than at the individual neuron level.
*  So I do think it is something that people, it's a technique limitation. And then, you know, the field is kind of now that there's the ability to record from all those neurons.
*  Now you're seeing, you know, the same kind of representational similarity analysis kind of techniques and all these similar kinds of techniques are now being used across models and neuroscience.
*  Yeah, that's a good thing. I went from grad school recording one electrode, putting one down at a time.
*  Then even in my postdoc, we started with a tetrodes. That's four. And like every every two months, we'd have to like switch out our systems because there'd be a new electrode with even more and more.
*  And yeah, so frustrating, really, to get anything done in neurophysiology. You must have. Have you ever made any mistakes with Libra? What's the biggest? What's the biggest setback that you've had?
*  Oh, gosh. Well, one just, you know, massive mistake. We had the activation function, you know, the core thing like about how does the neuron fire, you know, was totally wrong.
*  So, you know, my understanding, again, from like grad school neurophysiology classes is, you know, you take the excitatory current and the inhibitory current and they integrate and they produce a membrane potential.
*  Right. And then when that membrane potential gets over threshold, then they're on fires. Sure. And so that's that's how it works. And so I said, well, if I'm going to make again a rate code model, because I didn't want to deal with spikes all the time.
*  So I make a rate code model. I based my rate code on the membrane potential. Okay. And it turns out mathematically, unbeknownst to me that basing a rate code model on the membrane potential is actually the wrong thing to do.
*  It's not monotonic with respect to the actual kind of rate of firing. It turns out this is one way that I know in one version of spiking neural networks. This is one way that back propagation has been implemented by using the gradient of the membrane potential.
*  So I don't know how that relates, but interesting. Yeah.
*  So it doesn't. Yeah. Yeah. So we had we basically had a non monotonic activation function for many years that was broken in a lot of ways and later discovered basically that, you know, there is this more linear relationship with the excitatory conductance relative to a threshold that incorporates the inhibition.
*  And that that produces a activation curve that fits kind of what spikes actually do. So that was like a big bug. You know, it's like, you know, just just just a mistake right straight out.
*  How long does it take someone to go to the website, which I'll point to and get up and simulating with Libra? How long would that take?
*  Well, so one thing is we have a whole new framework now. So we had previously a whole kind of C++ based more like a kind of like a word processor kind of like a system where you would kind of create the model in a GUI interactively.
*  We've now switched over to more of the typical kind of every simulation is a separate program using a library. And you can now do that in Python, calling our library.
*  The library itself is written in Go, which is this fun language that I really love that was invented by Google. Yeah. So basically, you know, you can download stuff immediately and run it.
*  And, you know, if you're if you're using Python, you can you can we have a textbook set of simulations that go with our textbook that that you know has all the executables and you can just download it and run it directly.
*  So we teach this class, you know, to undergrad psychology majors and everything. And and so that has the kind of nice GUI still where people can kind of access the models in a more point and click way when they run them,
*  even though they're still kind of coding them as a program, you know, under the hood. And and that's always been a big priority for me in terms of, you know, balancing the research with the teaching, having something that that gives people an easy way to access the models.
*  And I'm also a very kind of visual person. So I like to see my models running. Right. So one of my goals is to actually use this kind of visualization stuff for like the pie torch kind of backdrop models as well, so that I can actually see how those models kind of work at a more visual level.
*  And I'm always kind of amazed how much you know the field in a is just kind of running these models almost like black boxes and they never look at them and they don't know what they're doing. And I feel like, how do you how do you know what your model is doing if you can't see it?
*  But some of them are so complicated. I'm not sure if it's going to work.
*  It's just be rough. Yeah. But but so long if I'm comfortable with Python, let's say how long would it take me to feel like I've done something in Libra?
*  Yeah, I mean, it's a you know, this is it's a it's a gradation. Right. So you can you can pull up a model, modify it, you know, very easily. You can kind of see where where everything's taking place, you know, to actually kind of like master it and be like, able to say I want to take a new cognitive phenomena and, you know, apply a hippocampus and a cortex to it. You know, that's going to be several months to a year or something. So yeah, yeah, I could do it in a day. I can get a simulation running in a day. Yeah.
*  For sure. Yeah, it's very quick. Yeah. Is it is it silly to ask you about AI consciousness? I know that you associate consciousness with human you. Yeah. Are only humans conscious or is it just such a specific flavor of subjective awareness that you restrict it to human?
*  Yeah, that's the thing is I think it's because we only have one reference point, which is our own subjective experience, we have no real way ever to understand what the subjective experience of another brain is like. And so it becomes very difficult to ask the question and to answer the question, because we'll never be inside another brain. And so you can never know.
*  You can never know. And so you can speculate and you can do these kinds of correlations of like what properties of brain seem to be important for what kinds of overt behaviors. But fundamentally, this kind of Chalmers hard problem, this this duality, this divide between, you know, what we can characterize objectively versus what we can actually seductively experience that barrier prevents us from really saying, you know, this other thing is conscious of what we can actually do.
*  So I think we're going to have AI that's conscious. Oh, okay. Everybody's going to be like happy to say, Yeah, that thing seems pretty conscious. It's expressing subjective experiences in a way that you know, we can relate to. And again, I think that would be a situation in which we had essentially done a pretty good job recreating the human brain.
*  Yeah, so you're not that much of a functionalist that you could do it with a water clock set up the right way. Right. Okay, exactly. You could have other things that have other kinds of subjective experiences that are rich and complicated. And but if we can't subjectively relate to it, then we won't really know what to make of it, you know, and, and, you know, maybe they'll be like, this whole different way of having consciousness, but that thing will be able to
*  explain and translate its experiences into terminology that we can understand. And then maybe we would sort of vaguely understand kind of what's going on in that other thing. But we wouldn't be able to have that quality of like, like, Oh, yeah, you know, this thing is feeling sad in a way that I feel sad, you know, that kind of direct ability to understand what that means.
*  Well, I know you're gonna be sad if I don't let you go in a minute, because you need to you're not Libra or AI and you have to put food in your body and play with your children with your kids with Legos. But let me ask my last question is, and thank you very much for your time. If you were going to go back and begin again, like right now, how would you how would you proceed? That's another huge question for 30 seconds or whatever, but
*  Absolutely. Yeah, it's really interesting. You know, I think there's so much available right now in terms of, you know, all these, you know, training courses and people can learn a lot of core principles of AI and statistics and just all this amazing stuff, programming languages. So I feel like we have all those resources that we have in the world.
*  We have all these resources available. And, you know, for me, back then, it took a long time to sort of, you know, learn all that stuff. So I feel like there's a great opportunity to sort of, you know, quickly, efficiently learn all the kind of basics, but fundamentally, you know, finding a lab where people are asking the same kinds of questions that you know, you resonate with. And for me, you know, it's still the same questions. Like, you know, how do we understand how the brain works?
*  And, and so it would, I wouldn't go, you know, I wouldn't, I wouldn't necessarily go back to Jay McCollum's lab now, because, you know, that that was then, this is now. So but I would seek out those kind of same kinds of experiences, you know, I feel like grad school was amazing. I really like academia, I like the freedom, I like the ability to kind of, you know, explore the questions I want to explore. So even though, you know, the competition level in academia is much harder now, I would probably at least give that a try.
*  See how it goes. But you wouldn't do neurophys lab, you go computational think I think I would stay computational. It's hard. I feel like we're going to get all the answers from neurophysiology someday. Some. Yeah, some days a long time, maybe. And, and I feel like if you want to get the low hanging fruit, you can still attack a lot of questions computationally quicker. And you may not you don't have that you don't have the certainty you don't know if you've really answered the question, but you do have.
*  At least the ability to kind of address the questions computationally more quickly in a way that suits my inpatient personality. Yeah, it's still a slog, but it is faster than everything's faster than neurophysiology. By the way, Jay says hello. He didn't he didn't submit a question for you in time. I thought that would be fun. But your old advisor. Yeah.
*  And he's interested in your motivation work, which we didn't get to. But yes, yeah, I need to connect with Jay again. I haven't, I haven't been in touch. It's really been tough moving here to Davis with all this, you know, all the moving the whole lab and everything and getting Reese rebooted here. But yeah, well, continued success. And thank you for your time. And I appreciate it. This is really fun.
*  Brain inspired is a production of me and you. I don't do advertisements. You can support the show through Patreon for a trifling amount and get access to the full versions of all the episodes. Plus bonus episodes that focus more on the cultural side but still have science. Go to brain inspired.co and find the red Patreon button there. To get in touch with me, email Paul.
*  The music you hear is by the new year. Find them at the new year dot net. Thank you for your support. See you next time.

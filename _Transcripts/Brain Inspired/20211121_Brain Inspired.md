---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 6003s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 12058
Video Rating: None
---

# BI 120 James Fitzgerald, Andrew Saxe, Weinan Sun: Optimizing Memories
**Brain Inspired:** [November 21, 2021](https://www.youtube.com/watch?v=V-ku3AMgCiU)
*  I guess the jumping off point is this long-running debate about where memories are stored in
*  the brain.
*  And it's a profound question, it's something that people have struggled with for many decades
*  at this point.
*  This really gives me the insight on why a lot of episodic memories are being kept in
*  the HEP campus and required the HEP campus.
*  A lot of it is because the world is so complex.
*  I definitely think that we wouldn't have gotten to where we currently are in AI without past
*  generations of theoretical neuroscience research.
*  And I also definitely think that projects like this, where we try to boil it down to
*  the essentials and really analyze everything very rigorously and really try to figure out
*  to what extent this relates to the biological brain, will provide useful seeds for future
*  AI research.
*  This is Brain Inspired.
*  Hey everyone, it's Paul.
*  Today, I have three fine folks on the podcast.
*  James Fitzgerald, Andrew Sachs, and Waynon Soon.
*  James and Waynon are both at the Janelia Research Campus at the Howard Hughes Medical Institute.
*  James is a group leader and Waynon is a research scientist in Nelson Sprueston's lab.
*  And Andrew is a joint group leader at University College London.
*  Andrew's been on the podcast before when we discussed his work on deep learning theory
*  on episode 52.
*  And you'll learn more about what James and Waynon do in a moment.
*  The reason I'm speaking with them today is their recent theoretical neuroscience preprint
*  with the title, Organizing Memories for Generalization in Complementary Learning Systems.
*  So we've discussed complementary learning systems a few times on the podcast before.
*  The general idea is that we have a fast learning system in the hippocampus that rapidly encodes
*  specific memories.
*  And we have a slower learning system in our neocortex where over time and through mechanisms
*  like replay from the hippocampus, memories get consolidated.
*  So in their new paper they build on complementary learning systems and suggest that these two
*  learning and memory systems might work better together in a way that optimizes generalization,
*  which is a good thing if you want to function well in our topsy-turvy world.
*  And one of the big takeaways is that how much consolidation should happen from hippocampus
*  to cortex depends on how predictable the experiences are that your brain is trying
*  to remember.
*  So in unpredictable environments you want to cut off the consolidation pretty early.
*  In predictable environments you want to let consolidation run for longer.
*  And that's of course a very simplified explanation which gets elaborated during the podcast.
*  So they built a model to explore that hypothesis.
*  And we discuss many topics around their model and related phenomena.
*  I linked the paper and the show notes at braininspired.co.
*  There's also a guest question from Mike, a Patreon supporter, who actually pointed me
*  to the work that we're discussing.
*  So thanks Mike for the question and pointing me to it.
*  And thank you to all my Patreon supporters.
*  By the way, during my little post-recording check-in with James, Andrew, and Waynon asking
*  if everything went okay, James mentioned that it felt a lot like a conversation they would have
*  in their regular weekly lab meetings.
*  So if you're wondering what their lab meetings might be like, here you go.
*  Andrew, James, Waynon, thanks for being on the show here.
*  So what we're going to do to start off is I'm going to ask you guys to each introduce yourselves.
*  Andrew, let's start with you because you were on the podcast before.
*  We were talking about deep learning theory.
*  And ever since you're on, of course, you've been emailing me, can I please come back on?
*  Can I please come back on?
*  And finally, we have you back on here.
*  So Andrew, who are you?
*  Yeah. So I'm a joint group leader at the Gatsby Unit in Sainsbury Welcome Center at UCL.
*  And I'm interested in deep learning theory and ways that can inform theories of psychology and neuroscience.
*  James, would you like to go next?
*  Sure. Yeah, my name is James Fitzgerald.
*  I'm a group leader at the General Research Campus, which is part of the Howard Hughes Medical Institute.
*  So I'm a theoretical neuroscientist.
*  I'm actually very broadly interested in a lot of different things.
*  So in addition to the learning and memory stuff we'll talk about today, I also work on small animals like zebrafish and food flies.
*  And I'm very collaborative.
*  So I like to work with diverse people coming from all sorts of different perspectives.
*  I think that's one of the most fun parts of doing science.
*  I'm going to ask about the collaboration in just a minute here.
*  Waynon, hi.
*  Hi, Paul. It's great to finally meet you.
*  Yeah, you too.
*  My name is Waynon.
*  I'm currently a senior postdoc in Nelson Spruce's lab at Genelia.
*  So I joined Genelia four years ago after doing ion channel biophysics and synaptic transmission studies for seven years.
*  After joining Genelia, I just wanted to sort of step up and get a bigger picture, kind of more of framework thinking on neuroscience.
*  So I decided to, okay, let me do theory and experiments together.
*  So it has been a pleasure to collaborate with Andrew and James on this project.
*  Yeah. So this project is pretty much all theory, right?
*  So the title of the paper that we're going to talk about is Organizing Memories for Generalization in Complementary Learning Systems.
*  Before we talk about the theory, I kind of want to ask, well, how did this collaboration come about?
*  Anyone can jump in and answer because and tied into that is the idea of Genelia.
*  And I'm curious, you know, it seems like Genelia specifically is highly collaborative.
*  So I don't know if that's a factor in this as well.
*  Yeah, for sure.
*  I mean, I think, you know, as you just heard, so Waynon's actually in Nelson Spruce's lab at Genelia.
*  So none of us are actually in the same lab anyway.
*  So Genelia labs are very small to kind of try to encourage collaboration.
*  So the idea being that, you know, no one lab has enough people or all the expertise you would want to kind of achieve the project's goals.
*  Is that built in though as a as a principle when forming a lab?
*  It is. Yeah, it is. Yeah.
*  So that's why they've kept the lab small is to kind of, you know, really encourage people to interact with each other and collaborate.
*  So Waynon and I kind of arrived at Genelia at almost the same time.
*  And, you know, at the time, my lab was completely empty.
*  So Waynon was really kind of my first main postdoc collaborator at Genelia, even though he didn't have any position in my lab.
*  So I don't know, Waynon, do you want to kind of reflect a little bit on the early days?
*  Oh, yeah, that was interesting story.
*  So in 2017, I joined and that's exactly when James just joined.
*  I was just in a sort of experimental crisis mode, like I've been doing so many experiments and and I was trying to decide what to do here in Genelia.
*  I know I joined Nelson's lab just to study some more single neuron computations, but that's when DeepMind released their AlphaGo.
*  And it was having a big splash in the world.
*  And I was a longtime Go player and that just really shocked me how human like the moves are.
*  And I just started to think, OK, so where can I get frameworks to inform like all the data I collected?
*  I think I need to collaborate with theorists and I need to combine neuroscience with AI.
*  So and then James and I started to talk and I was generally interested in complementary learning systems.
*  So the seminal work by Jay McClellan.
*  And then we started to talk and then James was interested.
*  OK, so why don't we just start with modeling CA1 because his recent findings show that CA1 spines are very transient.
*  So it turns over every two weeks.
*  In hippocampus. I'll just interject in hippocampus. Yeah.
*  Yeah, so that quick spine dynamics, James suggests that it might be a form of regularization like weight decay in machine learning.
*  So that's what got us started. So I was modeling that.
*  And I don't want to get this too long, but later on, James just I remember that really vividly.
*  He drew on the board that, OK, do you know what happens if you have noise in the data?
*  If you train on the training data and the generalization error is that your performance on new data will start to decrease and that will start to rise up.
*  And I remember being an experimentist, I was shocked by that fact.
*  I said, why is that? OK, you need regularizations in order for training to not overfit.
*  And I think that's just interject a little bit.
*  I think that's actually a great segue in also to how Andrew got involved in all this stuff, which is that Andrew and I go back a long, long way.
*  So we were grad students together. We knew each other way back then.
*  And then we were actually postdocs also together in the same program.
*  And so we've known each other for a very long time, but we hadn't been collaborating.
*  And while Andrew was in his postdoc, he was working with Madhu, another author on this paper, very precisely analyzing the amount of learning in a batch system that would be optimal for generalization.
*  And so it was very much in my mind the importance of thinking about regularization in part by interactions with Andrew in a non collaborative way.
*  But then once Wayne and I started to think about the benefits that this types of regularization might provide for learning systems, we decided to be really fun to see if Andrew would also be interested because we knew that he had overlapping interests too.
*  And that's when we kind of kind of bought Andrew into everything.
*  And we had Andrew come to Janelia. We planned to visit our project.
*  And then, you know, we wrote it up and we've been working together for the last couple of years on this.
*  So, yeah, in the early days, what Wayne and I were modeling, you know, we were thinking about kind of the role of, you know, transient memories in the hippocampus and what that might do to kind of aid system wide function in a complementary learning systems type way.
*  But we didn't actually have any kind of explicit cortical model in those early days.
*  And it was only once Andrew started to get involved that we kind of really started to build an integrated model of the whole system based on the insights that he's had by kind of thinking about learning in deep linear networks.
*  Andrew, you're not at Janelia.
*  So I don't know if you're being pulled in a thousand different directions by lots of people that want to collaborate with you.
*  So, yeah, how do you how do you where's your threshold?
*  How did you get sucked into collaboration with these guys?
*  Yeah, well, it's just thinking I'm glad you two remember how this started.
*  It's sort of ironic in that we're studying episodic memory, but I really don't remember quite how it all came together.
*  But but yeah, I mean, I guess the memories that are recurring are yeah, thinking about deep learning theory.
*  I have this structure that I'm hoping will be replicable across many experimental domains.
*  The idea is first come up with some basic insights into how deep networks work, just treat them on their own terms.
*  At that point, it looks basically like what a computer scientist or physicist would be doing.
*  And then if you can get some durable insights into those systems, hopefully that offers interesting hypotheses for certain experimental domains.
*  And in this case, we initially did work on generalization error.
*  And then it seemed like this could potentially shed light on hippocampal consolidation.
*  We actually had a cosine poster on this to just to do a night that didn't go nearly as far as this paper.
*  But it was some of the early seeds of it.
*  And then I think James and I probably just get Harvard.
*  James, we just actually couldn't reconstruct actually how I even looked at old emails to figure out how this got started.
*  But I do remember when you visited us at Janelia.
*  And at that point, presumably, we already knew we were planning to collaborate.
*  Or maybe we just had you come for a talk, actually.
*  Maybe we're just going to come and give a talk.
*  But in any case, I remember us taking a walk along Seldon Island.
*  So Janelia is right on the Potomac.
*  And one of the odd but wonderful things about us is we have a private island in the Potomac that does a footbridge.
*  And it's just well worth this.
*  There's nothing there except for like a field.
*  And so Andrew and I were walking.
*  And Wayne and I had already been working on this stuff.
*  And of course, Andrew had been doing his stuff with Madhu.
*  And we were just discussing, like, well, you know, everybody talks about complementary learning systems.
*  And it's kind of implicit in a lot of what people say that they think that the point of having the cortex is for generalization.
*  But do people actually realize the danger of overfitting in these systems?
*  And we were kind of debating this back and forth a lot, because on the one hand, you're like, well, it seems like they kind of should if they think about it from the viewpoint of machine learning.
*  But at the same time, it didn't actually seem like anybody had been thinking through the consequences of that about kind of,
*  well, then you really need to regulate the amount of transfer.
*  You can't have it that you just kind of fully transfer memories from the hippocampus to the neocortex.
*  And then I think that these conversations also in terms of Wayne on, I can remember that same visit, him getting very excited by the generalization angle.
*  You know, before that visit, we were thinking about many different things about the benefits of kind of transient hippocampal traces.
*  So also in terms of things like memory capacity in the hippocampus and stuff like that.
*  But I think after that visit, we all kind of consolidated around this fundamental importance of, you know, if you build the system for generalization, there's going to be some new requirements that, you know, people have not been thinking through from the perspective of neural networks.
*  I think one of the most fulfilling aspects of this collaboration is that at this point, the ideas are so jointly woven that it's like it really was one of those wonderful times where you're just everyone's riffing off of each other and it somehow comes out to be this thing that's greater than some of the parts.
*  Well, that's interesting. I didn't know the connection, James, between you and Andrew, because I didn't do my homework about reading your CVs, I suppose.
*  But I but I believe it was Wayne on actually who first recommended Andrew to come on the podcast way back when.
*  So I know that there's a connection there as well.
*  Yeah.
*  It's great to you, you know.
*  Well, let's talk about the big idea in the paper and then we can kind of unpack it from there because you've already hinted at some of the some of what it's about.
*  So I don't know who would like to start and give like a really high level overview.
*  And then we can talk about complementary learning systems and just go on down the list there.
*  Sure.
*  Sure. Well, maybe I can.
*  So I guess the jumping off point is this long running debate about where memories are stored in the brain.
*  And it's it's a profound question is, you know, something that people have struggled with for many decades at this point.
*  And the data from neuropsychology is riveting.
*  So, for example, a patient HM, for instance, lost his hippocampus and other structures and just can't form new memories.
*  But even more striking, if you look into the memories before he had this resection operation, a lot of those memories are damaged as well.
*  So the damage went back into the past, basically.
*  And what that suggests is that there's some process by which memories might initially be stored in hippocampus, but ultimately transfer out or reduplicate themselves in other parts of the brain.
*  But this just raises all kinds of questions.
*  Why would you have a system set up like this? Why do you need multiple memory systems to start with?
*  Why couldn't you have these memories stored in all places across the brain?
*  And there's a raging debate about this topic.
*  And so when we were looking at this, we were trying to find ideas that might have been overlooked.
*  And looking at machine learning, you can see that there's this very interesting phenomenon that if you're training from a fixed set of data,
*  and you're going through it again and again, then the idiosyncrasies of that data can cause you to learn spurious relationships.
*  And so too much learning from the same fixed batch of data can be counterproductive.
*  And so we thought maybe this was relevant to systems consolidation.
*  If you think of that batch of data as the experiences you stored in your hippocampus,
*  what it's saying is that there's only so much replay you should do to sort of try to encode those memories into neocortex,
*  because if you did too much, you would not be learning the general rule that's in that data set.
*  And so that, we think, can start to make sense of a lot of these empirical puzzles that have been out there.
*  Yeah, so maybe to kind of just elaborate on that a little bit.
*  So one of the big empirical puzzles is that because of patients like HM,
*  there's been what's called the standard theory of systems consolidation,
*  which says that in the beginning, everything is encoded into the hippocampus,
*  but then over time, everything is consolidated into the cortex and becomes hippocampus independent.
*  And there's a lot of data to support that from both humans and from animals.
*  But over time, there's also been a growing body of literature that conflicts with that
*  and suggests that in both humans and in animals, certain types of memories do permanently require the hippocampus.
*  And so there's been kind of a conceptual shift in the field where people start to think about consolidation,
*  not just as something that happens over time, but that has something to do with the content of memory.
*  And there's all sorts of conceptual ideas about what that content might be
*  and why it is that certain things do require the hippocampus permanently.
*  But again, from this perspective of generalization and neural networks,
*  we thought we might be able to make this very concrete about kind of when you can and when you can't
*  take something that was initially encoded into hippocampus and gradually make it hippocampal independent.
*  So you've taken complementary learning systems, which we've already talked about a bit.
*  And essentially, the theory is generalization optimized complementary learning systems
*  is the name of the I guess is it the theory or the model setup or is that interchangeable?
*  I think there's sort of actually two levels that you can view this this work on.
*  The first is a formalism that could let you model many other kinds of consolidation theories.
*  So we have this particular mathematical framework.
*  You can instantiate the standard theory. You can instantiate generalization optimized
*  complementary learning systems. There may be others.
*  And so at that level, it sort of lets you understand the consequences of different choices
*  about how these memory systems interact.
*  But then the one that looks good to us just looking at the data, yes, is generalization optimized complementary learning systems.
*  So what is the take home of what's new about generalization optimized CLS versus and you may be repeating yourself.
*  So I apologize.
*  So maybe the way I'd characterize the original CLS idea is that there are benefits from a rapid learning system and a slow learning system.
*  And a lot of those benefits that were highlighted in the context of the original complementary learning systems idea was that having a fast learning system
*  that can record and memorize examples could allow the slow learning system to interleave those examples during learning and prevent what they called catastrophic interference.
*  And so you'd be able to use the fast system to record the memory as it comes, but then slowly train up a slow learning system based on those experiences.
*  And the idea would then be that in this slow learning system, you get some sort of representation that is kind of generalized over the various training examples that you've seen.
*  So in some sense, I think generalization has always been an important part of thinking about the complementary learning systems framework.
*  But what is new in how we set things up is that we have an explicit generative model for the environment that allows us to consider the possibility that there are unpredictable elements in that environment or noise.
*  If you set it up in kind of an abstract way.
*  And because of this, what we show that had not been kind of considered in earlier complementary learning systems models is that in the presence of noise, it's not always ideal actually for the slow learning system to learn forever.
*  At some point, you actually have to stop learning to avoid overfitting to this noise, which again, from the viewpoint of machine learning makes a lot of sense.
*  But in the setting of conventional complementary learning systems problems, you're learning from these data that don't actually have any noise.
*  It's just kind of these very reproducible, very reliable cognitive relationships.
*  And as a consequence, there's no tension between what we call generalization and what we call memorization, like the ability of the system to recall those examples versus kind of deal with cognitively or semantically similar examples going forward.
*  But once you add noise, you break that and it starts to become actually that you have to make a choice.
*  That, you know, what is it that you want the slow learning system to do?
*  Do you want it to be able to faithfully reproduce the past, which is what we would call the standard model of systems consolidation?
*  Or do you want it to actually do as well as it possibly could in anticipating new experiences from the environment that can occur in the future?
*  And that's what we mean by generalization.
*  So I had Uri Hassan on a while back and he had written this paper, I believe, called Direct Fit to Nature.
*  But the idea was that our cortex essentially have so many neurons and synapses, aka so many parameters that it's constantly trying to overfit, trying to basically you can't overfit.
*  It's so big that it can memorize everything.
*  And of course, this has been shown in deep learning networks as well.
*  Is the right way to think about the cortex then?
*  So, James, what you were just describing was sort of a larger picture normative framework for what you would want as a generalization organism, generalization geared organism.
*  And one of the things I thought in reading the paper was, well, is it right to think of cortex then as trying its damnedest to fit everything perfectly?
*  And there are regulatory systems that are preventing it from this direct fit that Uri talks about.
*  And so at the organism or brain level, I suppose, we should think about that system as separate, well, as kind of a control mechanism for this otherwise running rampantly memorizing things, cortex.
*  Sorry, that was a mouthful.
*  Yeah, no, I think that, I mean, you can do better by, for instance, stopping training early, even in a large deep network.
*  And so if this is something that the brain takes advantage of, then it would be generalizing better.
*  So there are circumstances like Uri is saying where if you have a giant network, you're not really going to overfit dramatically.
*  So it's not maybe a huge benefit if you stop early, but it's still there.
*  And in some regions, the effect of early stopping is incredibly important.
*  So if the amount of experience is roughly matched to the number of degrees of freedom in your model, then that's the point where you could get a lot of benefit from replaying that data if it's noise free.
*  You could just perfectly determine what the whole mapping should be.
*  But if it's noisy, it's also the point where you can do as badly as possible.
*  And so regulations are very important.
*  And maybe just to highlight with an example, so because these things can sound abstract, but patient HM, for instance, Suzanne Corkin, the MIT professor who did a lot of work with him, was asking him if he had any memories of his mother and specific memories of his mother.
*  And his response was, well, she's just my mother.
*  And, you know, I think the point there is that this is someone who had their entire cortex intact.
*  Right. And they he could not come up with a specific memory of even his parents.
*  Right. This drove his father as well. But he knew all kinds of more reliable facts.
*  He knew that his father, for instance, was from the South and things like this.
*  And so there's this interesting tension here where the quality of the memory, the type of memory that you can put in your cortex seems to be very different.
*  And we think this theory explains some of that because there's certain components of a memory or a certain scenario that you can transfer.
*  Like the fact that mom is mom is always true and very reliable.
*  But then there's other features of memory which can be very idiosyncratic, like what you did one specific Christmas.
*  So he knew that Christmas trees were things that happened at Christmas time.
*  Right. But he didn't have a specific memory of one specific Christmas and what they did.
*  And that's the sort of that's what we're proposing is explaining the character of this transformation as being aimed at generalization and flowing from these properties of deep networks.
*  Maybe we should get into the model, the models, the three models used in just the whole setup.
*  I was going to say experimental setup, the whole modeling setup.
*  So, Wenon, do you want to describe how like the different kinds of models used that are supposedly to represent different brain areas, although you use a different vernacular in the paper because you talk about how these could map on to other brain areas or it's amenable to other brain areas because well, so you use student, teacher and notebook in the paper.
*  But do you want to talk about how the what the models are and how they map on?
*  Oh, yeah. So we thought about how to formalize this learning problem of systems consolidation.
*  So typically think about a brain that can learn things from environment.
*  And what is the environment? It's just that sort of can be viewed as a data generator.
*  And you produce some kind of input output mappings, maybe very complex functions.
*  And we want to replicate that by a very simple generative model.
*  In this case, it's a shallow linear neural network.
*  So it just transforms input vector into a single scalar in most of our simulations.
*  And this transformation.
*  Generate produce data pairs like X and Y input output pairs to feed to another similar architecture student network.
*  So it's another shallow linear network that can be trained on the training data generated by the teacher and learn to represent the mapping of the teacher.
*  And the student learning is aided through a memory module similar to like the current AIs external memory idea is modeling the HEP campus.
*  So it's a hot field network that's bi-directionally connected all to all to the student.
*  So the job is really capture the ongoing experiences by one shot encoding through high-being learning.
*  So the HEP campus has been proposed to be learning really fast.
*  And then after capturing that, it has the ability to undergo pattern completion offline.
*  So you can just randomly search for a previous memory and reactivate the student through the feedback with.
*  So this essentially is modeling episodic recall.
*  So you could offline replay what the students was seeing when the teacher give the student the example.
*  So as if you have the teacher like it's a notebook.
*  So you're just reviewing what the teacher said essentially through doing this offline reactivation, the student can learn much more efficiently as we later show in the paper.
*  So that's roughly the three neural networks.
*  So you have the environment, which is the teacher.
*  You have the cortex, which is the student.
*  And you have the HEP campus, which is the notebook.
*  Just to kind of emphasize one of the things is that one important difference between the teacher and the student is that the teacher has noise.
*  And because the teacher has noise, what that means is that the mapping provided by the teacher may or may not actually be fully learnable by the student.
*  And controlling the magnitude of that noise then is a critical parameter that determines the optimal amount of consolidation in this framework.
*  Just realize one more thing that you asked what's new comparing to the original CLS framework.
*  So we have an explicit notebook in this model that's directly connected to the student.
*  I think some of the early CLS works just kind of replay training examples, not by storing them in a neural network, but just replaying the representations.
*  And this has generated some really interesting insights we can talk about later.
*  Having a distributed binary Huffing network reactivating the student can have some very interesting interference robust properties to train the student.
*  Great. Andrew, I was going to ask, so you guys are using linear, although these are shallow linear networks.
*  And we talked all about your deep linear networks last time you were on.
*  Why the linear networks in this case? Is it just to have principled theoretical accountability?
*  Yeah, I mean, I hope one day we'll have nonlinear ones, but all of the qualitative features that we wanted to demonstrate came out with shallow linear networks.
*  So we're just learning linear regression. Right.
*  And so my impulse, and I think it's shared by James and Wayne on to some extent, at least, is to go as simple as you possibly can and still get at the essentials.
*  And what you get for that in return is greater tractability.
*  So another feature of this framework is that most of our results are sort of mathematical demonstrations.
*  And so you feel like you can really at least I feel it's easier to get one's head around it.
*  And another thing that this very simple setting enabled is we can make clearer normative claims.
*  So we can optimize everything about these settings.
*  How well could you possibly do if you just had a notebook or if you just had a student?
*  And then we can show that, yes, indeed, you really do do better when you have both interacting.
*  I was just going to say, just to add to that, I think another thing that's really powerful about setting it up in this very simple way and being able to analyze it so comprehensively is that, you know, as we kind of alluded to earlier, I think one of the big challenges in memory research is to figure out, well, what is the key quantity that determines whether it's going to be
*  hippocampus dependent or not. And within this kind of modeling architecture, we can really solve that problem from the viewpoint of what would optimize generalization.
*  And then, you know, going forward, you know, Wayne on an experimenter.
*  So we can actually design experiments very much around directly that parameter and just test the theory very rigorously about whether or not this actually does provide empirically meaningful predictions more than just theoretical insights.
*  And I think that that gets harder and harder, the more complicated the model becomes to really kind of boil down.
*  What is the critical parameter and to design an experiment that embodies that critical parameter?
*  Oh, no, when on you're going to be stuck in experimental crisis still.
*  I thought you were trying to get out of that.
*  Now I think that's perfect combination with the theory and then do the experiment.
*  Okay.
*  All right. So who wants to talk about how how the model works to to generalize the right amount of generalization.
*  Yeah. So the setting that we're looking at is sort of like imagine you're doing a psychology experiment for an hour and you see a bunch of experiences over the course of that hour.
*  And then you go home and over maybe many days you have whatever you store during that hour and you can perhaps, you know, different the notebook could replay that information out into student to learn from it.
*  And then after some period of time, we bring you back into the lab and we test your memory.
*  So it's this sort of upfront get a batch of data.
*  How do you make the best use of that scenario over analyzing.
*  And so generalization for us just means when you come back to the lab.
*  How well will you do on new problem instances drawn from the distribution of problem instances that you're seeing on that first case first time.
*  So it could be you're learning to distinguish dogs and cats or something like this.
*  And then we show you new images of dogs and cats.
*  How well do you do on that?
*  And the key feature of the framework is that justice in deep learning theory means building directly off of deep learning theory and double descent phenomena.
*  There is an optimal amount of training time that you can train from a fixed batch of data because otherwise you start picking up on these aspects that are just noise.
*  And so as the predictability of the rule that you're trying to learn increases, you can train for longer and longer and you can characterize exactly how long.
*  But that that's the basic idea.
*  As you get more predictable, you can train for longer.
*  If you can train for longer, you can also memorize the exact examples you've seen more.
*  And so your your memory error is decreasing.
*  And that means that more of the memory with specific memory would transfer into your cortex and not just be the notebook.
*  Maybe one of the thing to throw in here before I let someone else jump in is that you can compare this.
*  So there's different ways you could generalize.
*  You could try to use the student network, but you could also try to use the notebook.
*  You could just say, let this hotfield network complete the pattern that whatever pattern you give it and make its prediction.
*  And one important result here is that in high dimensions, that strategy fails completely, actually.
*  So basically, if you think of high dimensional vectors, the geometry is very different.
*  Any new input is almost surely orthogonal to all of the inputs in your that you've all of the experience that you've had previously.
*  And because of that, it doesn't let you generalize.
*  So it's interesting. You need this notebook to store these examples so that you can replay them to the student.
*  But ultimately, it's the student that's going to be able to generalize well and not know.
*  Maybe this is a good time to have a listener question.
*  So predictability is a key aspect of the performance of the generalization performance.
*  So with different levels of predictability, the generalization needs to cut off at certain different points.
*  Well, you know what? I'll just play the question.
*  So this is from Michael Tilldahl.
*  And then we can back up and talk about the bigger issue after the question if needed.
*  In the discussion section, it's suggested that replay could be the mechanism that regulates generalization to the neocortex, which seems very probable.
*  But the thing I'm still missing is, do you have any ideas around how predictability of an experience is determined, as that seems to be a key parameter in the theory?
*  OK, so I know that's a little ahead of the game here, but I thought I didn't want to miss the opportunity to play the question before one of you started answering the question on your own.
*  Yeah, no, that really is such a good question.
*  And that, you know, we don't we don't address that in this paper.
*  What we say is, imagine you had an oracle, which could tell you exactly how predictable this experience was.
*  What should you do to be optimal?
*  But we don't explain how you could estimate that.
*  It's not we do think there are ways you could potentially estimate it, but it's not part of this theory at present.
*  We just are saying suppose you were able to understand the predictability.
*  What would that then mean for systems consolidation?
*  I was going to reiterate the problem, which is that predictability needs to be estimated by some system to regulate the generalization process.
*  Yeah, just to give a journal club yesterday.
*  And this question is such an important one.
*  Yeah, people always ask.
*  Okay, so that's great.
*  But wait, how do you actually estimate SNR in the experience?
*  So, operarily, if you get a new batch of data for the first time, and if you're learning from no previous knowledge, there's no way for you to know whether this batch of data is predictable or not.
*  So you kind of have to learn that through trying to error.
*  But the trial and error can be divided into like a long term evolutionary scale or like a big in a lifetime.
*  So maybe some animals already has built in predictability estimators from birth.
*  Maybe there's something like humans, like certain facial features or certain animals that if you see that it just the brain will treat it as a high SNR data no matter what.
*  Or during a lifetime, I think probably like that the main way we learn how to estimate predictability through lifelong meta learning.
*  So when you are a child, you experience a lot of things and you make predictions all the time and then gradually you learn what source of information is good to consolidate.
*  I always give this example that okay, so people typically know the reliability of the source of information.
*  So, for example, I give you an article from New York Times and then I give you an article from the onions.
*  You get a really visceral feeling like which one to trust more and to understand more.
*  Another example is like my daughter.
*  I see like she has no idea what's almost no idea what's predictable or what's not.
*  And just one time I was holding her and cooking and she just wanted to touch the hot stove.
*  I said, OK, that's not a good idea to do that.
*  You're going to get burned.
*  And she said, can I touch the edge just a little bit?
*  And she just said, OK, if you don't listen to me, you can go ahead and try it.
*  And she touched an ouch.
*  And then she turned my head back to me and look.
*  I think the look in her eyes is that, OK, I really need to listen to this dude in the future.
*  This dude is that I think that's when I think that's what meta learning is occurring in her brain that is assigning different sources for like different predictability.
*  Like we all trust our authorities, like teachers in our lives, parents and friends you trust.
*  Like even like another key aspect is that a lot of people think more frequent things should be consolidated because it's more reliable.
*  But our theory is really decoupling predictability from frequency.
*  So nowadays, you know, there are frequent misinformation online.
*  And it's not the quantity that can overwhelm your brain and determine what gets transferred.
*  It's really like, like, for example, like something your trusted friend told you, like even for once can can really make a long lasting impact.
*  But some news outlets give you the same story again and again.
*  And you will not transfer. So I think that's a key thing that we learn these predictability through experiences through meta learning.
*  But those experiences need to be essentially stored right in some system to be able to be used again.
*  And so is that is that just a different kind of memory? Is that more of a implicit procedural memory or outside of the hippocampal neocortex complementary go complementary learning system framework?
*  Or do we know or does it matter? Yeah, that's a great question.
*  I mean, so in our model, the notebook does kind of create a record of the whole memory.
*  And so using the hippocampus or the notebook in the mathematical framework, you can reactivate those cortical patterns that correspond to that full memory.
*  But that is, I think, part of what we mean by complementary learning systems.
*  You already had the ability to do that in the notebook.
*  So then maybe you don't need to kind of create a new cortical system to do the same thing.
*  And the idea would be, well, what can't the notebook do and what the notebook can't do is generalize well to new examples.
*  And to kind of go back to one of Waynon's points earlier, I don't mean to say that, you know, the neocortex can't actually aid in memory itself.
*  And in fact, there are some examples within our framework where the cortical module is actually able to even memorize better than the notebook.
*  But we think that the really fundamental thing that's missing from that just sort of faithful reproduction of the past, which the notebook can do, is the ability to generalize well.
*  But then the amount of consolidation that would optimize for that generalization is what depends on degree of predictability.
*  And as we've been describing, you know, it is a very important unknown within our modeling framework how precisely this gets done.
*  But we think that you first have to recognize that it needs to be done before you have to think about how it is done.
*  And so the earliest experiments I think that we could design and test, you know, we can just configure them so that the predictability is set according to us and then see kind of to what extent the brain in fact does regulate the consolidation process based on that predictability.
*  And then get more into the both algorithmic and mechanistic details of how that degree of predictability is determined and then once determined how that leads to regulation of the consolidation process itself.
*  There is some quite compelling experiments that show that it could be that individuals do misestimate the predictability sometimes.
*  Or maybe it's not even fair to say misestimate, but they just estimate it differently.
*  So there's individual differences. Maybe, Wei-Nan, do you want to explain that? The generalizers and discriminator experiments?
*  So I think a key thing about predictability is that it's, in a way, it's not the universal predictability objectively.
*  It's really like the inferred predictability. I'm not sure if you guys agree, but just the thought of this is really like how the agent or how the animal thinks what the predictability is.
*  And that depends on a lot of things. So there's an interesting set of rodent experiments in fear conditioning.
*  There's like really like individual differences on like the policy of animals doing the same task, whether they generalize or not.
*  So like there are certain certain animals, if you shock them in a cage, for example, and two weeks later, bring them back and they will show high freezing.
*  So there's a fear memory. But then if you take the same set of animals into a different but similar cage to test their fear generalization,
*  only like around half of those animals will freeze, will start to generalize to different cages.
*  But the other half will just maintain their discrimination in these two cages and not freeze. And they know this is a different cage.
*  And surprisingly, that the generalizers who froze in both cages, the memory is not dependent on the hep campus.
*  So there's this evidence that, you know, the generalizers do treat the original context as a high SNR context.
*  And that promoted generalization and systems consolidation. So that the memory actually is becoming cortical dependent.
*  But the other group that is still maintaining the discrimination,
*  leasing the hep campus actually impaired the original memory.
*  So I think that means that those animals is treating the environment as a probably like a low SNR task and that will not transfer.
*  So it still maintains the hep campus dependence. And we have different like in figure five of our paper, like we have a diagram showing that.
*  OK, so even within a single experience, the single animals, maybe there are different cognitive processes can change the SNR of the data.
*  So, for example, if you have a whole scene, the animals can actually use their covert or overt attention to only focus on part of the scene that might has different predictive value to the outcome.
*  So maybe the animal can just pay attention to the general features in the experimental room, like the smell may be similar and the experimenter may be wearing the same lab coat.
*  And that's highly predictable.
*  The other one, like if you just focus on the things that different patterns on the wall, that's highly idiosyncratic.
*  So that would be low SNR. So I think attention is a very key thing, both in determining the signal to noise ratio, also for regulation in consolidation.
*  I just want to add one last thing about the implementation of this regulation.
*  Like we said in the discussion that replay might be a natural way to do this, just regulate the amount replay to modulate consolidation.
*  But it has been shown that replay actually functions in a variety of different ways to promote, for example, enhancing attractors in the recurrent network, for example, or keeping the head campus in register with the neural cortex.
*  And so replay, so it could be not beneficial to stop replay altogether just to prevent overfitting.
*  It might be the brain might be using that you replay, you still replay all the memories and then you have a predictability module.
*  For example, like the PFC, it can control offline which part of the cortex gets activated and enable learning in an offline attention manner.
*  Like we have the amazing ability, like for example, you close your eyes, you can navigate within your memory, like focus on certain aspect of things.
*  And maybe the brain could tap into that mechanism to mask certain memory components during offline replay for consolidation.
*  One of the things that you said, so I kind of like two questions and one here.
*  One is, you know, there are certain situations where I don't care about predictability because I have to climb up the mountain before I fall or whatever.
*  You know, what's the classic escape the lion or something like that.
*  Right. And in that case, I guess you would predict that predictability, your predictability regulatory system just gets overrided perhaps because you're not needing to really consider the impact of the system.
*  You don't need to consider how predictable the data is or maybe it just automatically happens.
*  And I mean, because you're going to remember that event probably unless you die.
*  That's another really, really good question.
*  So I think throughout framework, many people ask us, what about emotional salient memories?
*  That's really surprising, really normal.
*  How is that related to the idea of predictability?
*  I think it's important to keep these two concepts orthogonal to each other.
*  For example, emotional memories could either be highly idiosyncratic or it could be predictable.
*  I think what the emotional salient is doing is maybe I'm not sure how much data support there is.
*  It could bias the memory retention of certain memories.
*  So, for example, you've climbed the mountain and you made a mistake and that was really dangerous or something like surprising happened.
*  That's pretty random.
*  That surprising factor may be enhancing the memory retention in your happy campus.
*  And then you can actually remember that memory for a long time.
*  You can tell the story maybe 20 years later.
*  OK, back 20 years ago, I had this terrible event.
*  But then which components gets transferred to the new cortex is determined by the predictability of the different memory components on top of that.
*  So I think that's almost a first future process of which memories.
*  Like we forget almost all of our episodic memories in a few days and only a few gets encoded.
*  Maybe that's more like hidden in our happy campus and to be weakened.
*  But who knows? But it just seems that we forget most of the things and certain things that we remember, we do remember, is modulated by some kind of other neuromodulatory process.
*  And our theory builds on top of that is the memories that gets retained for long term storage, which components actually routes to the new cortex and which components should stay in the happy campus.
*  That's kind of determined by the secondary factor is the predictability.
*  I think your question also brings up another interesting and subtle point about predictability.
*  And we introduced the teacher as an environment in terms of this is some sort of generator of experiences.
*  But that's actually pretty abstract because what the brain only knows is the brain's activity.
*  And so really what the teacher is, is a generator of brain activity based upon, for example, sensory and motor experiences in the world.
*  So if you kind of think about the teacher, not exclusively as an environment, but just as a generator of neural activity, then of course your cognition itself can also contribute to part of what the teacher is, because the teacher is just whatever it is that leads to patterns of activity that the student is trying to learn to produce without, for example, the involvement of the happy campus or other modules.
*  And so if you think about the teacher in this way, it could be that, for example, some of these highly emotionally salient or very memorable events in some sense are very predictable just because you think about them a lot.
*  And because you think about them a lot, you actually do recurrently get these patterns of neural activity that you may actually want the student or the neocortex to be able to start to be able to reproduce on its own.
*  And we think that this may have to do with why, you know, in human patients, for example, they are sometimes able to reproduce highly detailed aspects of their past life that seem to be highly unpredictable.
*  But we think that the reason for this is because basically they are so reproducible based on the experiences of that person or based, for example, on the thinking patterns of that person that they start to be able to be consolidated because they start to be predictable in this more general sense of not just what happens in the environment, but what happens in your mind.
*  So is it too simple to map on the teacher to the perceptual systems, perceptual cortex, for example?
*  I think it could be. I mean, I definitely do agree that, you know, we think about the teacher in the most simple setting as just the perceptual systems.
*  And that is kind of the examples that we provide in the current paper.
*  And that is the setting that is designing our kind of initial round of experimental design.
*  But I do think that when it comes time to really understanding how these abstract neural network models will get mapped onto real human cognition and neuroscience, that that is too simple, I believe that you do need to consider more broadly what it is that's leading to patterns of neural activity across the entire cortex.
*  Then you would have the problem that the sensory cortex should be getting trained also as a generalization optimizer.
*  Absolutely. Absolutely. And in fact, that's a very important part of how we think about it is that, you know, from the viewpoint of the abstract neural networks, we have very well defined inputs and outputs.
*  But when we actually think about what that means in terms of the brain, we're just thinking about the neural cortex as if it's some kind of an autoencoder where, you know, activity is generated by your sensory motor experiences in the world, your cognitive processes.
*  And what you're trying to do is build a cortical system that is able to reliably reproduce those patterns going forward into the future without needing sensory inputs, without needing involvement of other parts of the brain.
*  And in this point of view, then, you know, it's not as though just that, you know, as you said, like some low level sensory area is not only the input of this framework, it's also the output.
*  And many of these relationships have to get learned simultaneously. And for each one of these relationships, there could be a highly different degree of predictability.
*  And as we emphasize in the paper, based upon that high then variability in the degree of predictability, there should also therefore be a high variability in terms of the amount of consolidation in terms of different types of synapses within the cortical network.
*  So, so when I mean you you you posited evolutionary architectural constraints versus meta learning earlier when talking about the regular how to regulate the system.
*  So you think that there's a room for both, I suppose?
*  Yes.
*  I think I don't want to really get into.
*  Yeah, no, it's okay. I just I just wanted to make it clear.
*  So, so Nate, wait, so nature and nurture are factors.
*  So one of the things that's, you know, fairly attractive about complementary learning systems is is the idea of, you know, when you have complementary systems that the whole is greater than the sum of its parts.
*  And actually, Steve Grossberg calls this complementary, a complementary computing paradigm.
*  And, you know, he thinks of multiple processes in the brain acting like this, and that when you have these two things working in parallel, both neither of which can do well on its own.
*  But when they are paired together, actually give rise to a what he calls a new degree of freedom, an extra degree of freedom.
*  How would you describe that in terms of the whole being greater than the sum of its parts with this go CLS architecture?
*  Yeah, so I think this the sum is greater than its parts in at least several interesting ways within our current go CLS framework.
*  So one, as Andrew mentioned earlier, we're able to determine what would be the optimal learning rate you could have for generalization if all you had was the students.
*  You just don't have any hippocampus or notebook you can use to recall the past.
*  And because we could kind of treat that problem optimally, we could show very rigorously, in fact, that when you put the two systems together, that in fact, you do get a cortical network that generalizes more efficiently from the data than you could from online learning.
*  And so there's a really fundamental advantage where if you're going to have some finite amount of data, you can just make better use of it period.
*  If you have the ability to record it somewhere and we call it subsequently to guide learning.
*  So that's one way. Another way that kind of also came up a little bit earlier is that actually, even when it comes to memory, there is a benefit, at least if you have a small notebook or a small hippocampal system,
*  because what we were able to show there is that in that setting, you actually get some errors when the hippocampus or the notebook is trying to recall those memories.
*  But what's really amazing is that the nature of those errors is that it's interference with other memories.
*  And so if what you're actually trying to do is train the student to memorize, then in fact, you can actually do better training from those noisy reactivations than actually those noisy reactivations themselves.
*  And so what ends up happening is that quite counterintuitively, the training error or the memory performance of the student can actually outperform what you could get in a notebook alone.
*  So yet again, for both of these cognitive functions, for both the memory and the generalization, the system works better when you put the two parts together.
*  And one, just to elaborate one small piece of that is it also clarifies the regime where you get the benefit.
*  So there are regimes where online, sort of just having the student and the replay strategy will look very similar.
*  And that's if you have tons of data, if you have tons of data, it doesn't matter. You get to the same point for both of them.
*  Also, if your data are very noisy, then in the limited data regime, it's still the gap can be fairly small.
*  So I think it delineates the regime where this dual system memory, it sorts of worlds basically where it's the most useful and it happens to be when you have sort of a fairly moderate amount of data and that data is quite reliable.
*  Then you see a big advantage from replaying a lot. And arguably, that's a setting that a lot of real world experience falls into.
*  Yeah, and just to follow up on that, what's incredible about that as well is that that same regime is where the risk of overfitting is highest in the model.
*  And so what's really interesting, if you just kind of step back from the details of the model and think about what it might mean, we basically say that, well, if you're in a regime where actually having these two learning systems is complementary,
*  you're also in the same regime where if you don't regulate, you're going to overfit.
*  And we think that this is a really important conceptual point because then we do know that the biology has built multiple memory systems in the brain.
*  And one of the lessons we can walk away with our artificial neural network is that perhaps the fact that it's built it suggests that it's good for something.
*  And at least within our framework, it's very rigorously true that when it's good for something, you absolutely need to regulate.
*  You can't just kind of transfer everything to the cortex.
*  Yeah, so this is going back to James point on like we have a notebook replaying examples.
*  And because a notebook has limited capacity, it shows some interference.
*  So the replayed example is not exactly the training examples.
*  There's some error. And this error, just surprisingly, as James mentioned, that it does not hurt training the student.
*  And in fact that, so I think this is a great story that is just so counterintuitive that I was running the simulations and James and Andrew are here in Agilene.
*  And I showed them the curves for the first time.
*  So the notebook reactivation error is like there's a little bit error due to interference.
*  And I use this type of reactivated data to train the student.
*  And it turns out the student training error can drop below that reactivated error.
*  And that's, we were like, you are using the notebook reactivity examples as labels.
*  And you can't possibly do better than that reactivation.
*  And later on, it just that led to a lot of mathematical analysis.
*  And it turns out that I think to me, this is so powerful.
*  And they questioned me, OK, wait a minute, that's you should check your code if there's any bugs.
*  And then I did something crazy.
*  So I said, OK, no matter what I do, I'll get the lower error from the student.
*  So what if I just generate random activities in the notebook?
*  And to my surprise, that still trains the student perfectly with some change in the learning rate.
*  So I think this is something deep that about like maybe if listeners are building future generation models of memories,
*  I think the reactivation has a certain property that can enhance generalization mainly by.
*  So let me give you an example.
*  So in machine learning, after all this, I discovered a connection that they use some certain data argumentation methods called mixed up.
*  That you just like, for example, you train ImageNet or MNIST, and you just linearly combine different training classes together
*  and also combine the output probabilities together, like adding them together.
*  And they only use the mixed examples to train the network.
*  The images themselves are mixed like one image would be a mixture of two separate images.
*  Yes. So you just randomly sample like two to four images and stack one and two together.
*  And then the output probability will be like you have 10 outputs and it will be 0.5, 0.5.
*  I see. Yeah.
*  And you only use this. Just get rid of the original pictures.
*  You only use the composite images to train the network and it trains equally well and sometimes is even better.
*  And this has became a very powerful data argumentation in even modern transformers that just performs much better.
*  And it is also really interesting being used in data encryption.
*  There is the Princeton study showing that the hospitals have records to train some kind of AI model for prediction.
*  And because of the data privacy issues, they just randomly merged the patient's data together and merged the output together.
*  And it still trains the model equally well, but masking the original data.
*  So I think this interesting connection is I mean, the brain is capacity limited.
*  And if you want to store some previous experiences to train up your new cortex,
*  and you've such a flexible ability to change your input data and still train the new cortex well,
*  I think the brain might be tapping into this mechanism and have sort of weird ways of generating examples instead of just replaying,
*  train examples one by one exactly that might be random merges of memories that has been supported by experimental data in the hippocampal field that certain memories are just prone to errors.
*  So for example, you imagine a house like you left your house yesterday, and there could be related things being put wrongly put in the scene.
*  Like you will remember, OK, there's a car parked right in front of me, but it was not.
*  So there's this leaking interference between memories could also be helpful in training the new cortex because a car is a car sort of independent of which scene it's at.
*  So that this kind of interference might not be as bad at training the new cortex.
*  And that probably reflects some certain compositionality nature of the world.
*  Like you can have different things merged together and still give out good training data.
*  This is a trivial question, or maybe this is a trivial question.
*  But how do humans perform on the mixed ImageNet data set?
*  I think I can't tell them apart.
*  Well, so then does that run counter to the story you just told then?
*  Because presumably unless that's just an inherent difference with deep learning networks, which we're going to talk about here in a second anyway.
*  Yeah, so that perceptual example might be different.
*  But if you really put different objects together and humans have the amazing ability, like if I put like a cup, apple, a weird like a car in the same scene versus seeing them apart,
*  I think human will have an easy time to pick up, OK, how many objects are in the scene and give each labels.
*  Oh, I thought that the pictures were blended like where you take the RGB values and can.
*  Oh, they are. So they're not compositional pictures.
*  They are. They're literally blended where we wouldn't really be able to perform well. Is that true?
*  Yeah, I guess so. Yeah, this I need to think about this more.
*  But maybe there's something there.
*  So predictability is a key or the key. Is the world really predictable or is it super noisy?
*  Are we ever in? I'm trying to think if I've ever been in a situation where it was completely unpredictable, maybe early on when I was dating.
*  But so how does predict are there situations where something is just truly unpredictable?
*  And if so, how does the network handle that?
*  Yeah, it's a great question because so far we've basically been talking about predictability as noise.
*  So, you know, real randomness coin flips.
*  But it doesn't. In fact, all the same phenomena occur in completely deterministic settings.
*  It's just what the equivalent is that the teacher is more complex than the student.
*  So there's something that the student can't possibly represent about the teacher.
*  And I think that is definitely a reasonable assumption about the world.
*  Right. This very, very hard to imagine that we would be able to predict everything about a physical situation.
*  And so essentially that unmodelable component, which in learning theory would be called the approximation error, it looks like noise from the perspective of the student.
*  And that judgment is completely relative to the students.
*  What can the student actually do? And then if the teachers were complex, then that will have the exact same effect.
*  You can see the same overtraining, all of the same behavior in learning curves.
*  And another version is maybe you have a completely deterministic world.
*  Maybe it's completely predictable, even. It's just that you don't observe the full input.
*  So imagine that the teacher has 100 input nodes, whereas the student only has 50.
*  Now the remainder looks like unpredictable information from the perspective of the student again.
*  And now we'll have all of the same properties as if it was really just a noisy environment.
*  So there are several forms of unpredictability that behave similarly and would require the same regulation and transfer between brain areas.
*  Yeah. So just want to add to that, like maybe I was just trying to really think about this intuitively.
*  These are silly examples.
*  So for example, the noisy teacher, you can imagine someone going to the casino in Vegas and then play the role late and then pick number 27 and bet a lot of money on it.
*  And he lost. He lost like $10,000. And then the unregulated consolidation will be that you treat number 27 as the bad number forever.
*  Like you just learned that I should never pick number 27, despite it's kind of random.
*  And that could be detrimental to your future. For example, if you are dating a girl whose birthday is on August 27th and you say, oh, no, no, no, I'm not going to date this girl.
*  So that's going to be bad for generalization. And the second example is about the complex teacher.
*  Like this is really gives me the insight on why a lot of episodic memories are being kept in the HEP campus and require the HEP campus.
*  Just a lot of it is because the world is so complex. Just imagine you're on the street.
*  There are different things happening and a lot of them are independent processes, has its own cause and effect.
*  And to cross predict such complex interactions between so many things, it's generally impossible for a human brain to do.
*  And like an intuitive example is that a lot of times in movies you see like a tragic like a tragedy, like a part of the scene is lowest of the low.
*  Like the person got cancer and then hit by a truck and there's something else happened.
*  The actor just start to cry like, why? Why me? I think at those times it might not be beneficial to really consolidate such complex events.
*  It's better to remember those things. But if you overgeneralize from those complexities, it's going to hurt generalization.
*  And the last thing about partial predictability, partial observability is, I mean, a lot of like most of the time our perceptual access to certain events are really limited.
*  Like people always say like the traditional wisdom is that you should really put things into context and don't just judge things by the first glance.
*  Like someone is behaving in a certain way and you get offended. And maybe that person is having a really, really bad day.
*  And you can't just base on that partial observation that this guy is just a grumpy person and he's not friendly.
*  Maybe just keep that as episodic memory and maybe you can build up more accurate representation of this person by long term interactions.
*  So I think about those three unpredictability this way.
*  Can I throw one more concept into the mix?
*  This seems to me related somehow to concepts like Herbert Simon's, Satisfycing and Bounded Rationality and Kahneman and Tversky's heuristics, the use of heuristics and good enough scenarios.
*  Have you guys thought about how your work and the results and implications of your work overlaps with those sorts of concepts?
*  So yeah, bounded rationality. That's interesting because we kind of are assuming we have this oracle assumption, you know, the predictability.
*  We're optimizing all parameters of the setting, but we've constrained the system to be this particular neural network with inherent limitations in that.
*  So yeah, I mean, I wonder if that is a version of, I guess, this like bounded architectural rationality.
*  You know, there's something baked into the architecture that you just it only is going to take you so far.
*  And in terms of heuristics, I mean, yeah, I guess you could maybe view it similarly that you may be forced into a simpler solution to what is actually a complex problem just because of the resources that the student actually has available to it.
*  But I don't know how many really interesting connections.
*  James, it looked like you were going to add something.
*  No, I think that was a good answer. I wasn't going to add anything more than that.
*  I was just going to kind of bring up the same points that this notion of unpredictability as it relates to approximation error is kind of giving the idea that the cortical network may only be able to do so well.
*  And that could have to do with the architecture of the network. It could have to do, for example, with what it's able to learn, the learning mechanisms involved in that network.
*  And so it is a notion of bounded rationality, I think, for sure.
*  But then how closely that would relate to the more famous notion of bounded rationality, I think, is a very interesting and deeper question that I think is harder to kind of answer at the moment.
*  Yeah, because one of the great things about heuristics, although they fail in many ways, but they're also beneficial in many scenarios.
*  And that's kind of why I was wondering, because you have to have this predictability estimator and it needs to be beneficial for the organism.
*  And then I was thinking, you know, heuristics for all their failures are also very beneficial in certain scenarios.
*  Yeah, I mean, I think you could view whatever it is that the student learns in our framework as a heuristic, because it is going to be an incomplete and inaccurate to some degree representation of what the teacher actually is.
*  But as you said, this heuristic is very useful. And in our setting, it's very useful in a very precise mathematical sense, and it nevertheless optimizes generalization, given the bounded rationality possible for that system.
*  And so it kind of brings these two things together that, you know, if you have some sort of bounded rationality or some sort of limitations in terms of what the system can do, then, you know, obviously you can't do better than that.
*  But then the heuristic may be the best possible thing.
*  So you guys put this in terms, you're careful not to just map on the networks to the brain areas, to hippocampus and cortex and the environment or perceptual cortex, for instance.
*  How should I think about this? Should I think about this as theoretical neuroscience? Should I think about it as artificial intelligence work?
*  And then what does it imply? Because there are, you know, like what we alluded to earlier, there are networks already with external memory. There are meta learning networks.
*  So what could deep learning and or AI in general take from from these networks?
*  Yeah, so there, yeah, like you mentioned, there are a lot of memory augmented neural network neural networks out there and also memory based RL agents that can use like it's typically is coupling some kind of cortical module like LSTM to an external memory.
*  So typically the memory is fairly simple. So a lot of times it's just a pending each new experience as like additional row.
*  So it's kind of pending into a big matrix. And a lot of times there's a keys and values like you use the keys to search and retrieve softmax averaged output as your episodic memory.
*  And that has been very successful in certain problems like the neural Turing machine or differential neural computer work from deep mind can solve a vastly different problems than the traditional neural networks.
*  Like Greg Wayne's Merlin framework also can solve the water maze like typical LSTM cannot perform. But I think there are inspirations we can take from the mammalian hippocampal architecture.
*  I think instead of like first thing is that still like the experience replay in RL agents and the usage of online like memory external memory modules.
*  Those two are different things like a different modules to doing the memory storage and doing the online inference.
*  In the mammalian brain we think we use the hippocampus to predict the future.
*  But we also have evidence that the hippocampus is replaying and serving as experience replay buffer to train up the new cortex.
*  So maybe there's a vantage of merging the two modules together. So that's one direction.
*  And the second direction is that how exactly should be the memory representations in external memories.
*  Like instead of just appending different roles can we use like more sparse distributed representation and a biologically realistic retrieving rule for memory retrieval.
*  So that's actually a very interesting work.
*  I think last year there's a group showing that Hopfield network like a modern continuous Hopfield network is equivalent to the transformer self-attention mechanism.
*  So there's some deep connections here maybe like memory and attention are really like different aspects of the same thing.
*  So I think using some kind of hippocampus inspired architecture maybe there's some certain research directions can be uncovered.
*  I don't know exactly what yet.
*  And also I think the last thing about the memory module is we use the Hopfield network and that's fairly traditional.
*  And the current AI external memory modules they use like a form of like more advanced versions of those generative models like variational auto encoders or organs.
*  So these things I think like one insight might inspire AI is that you know we know the anatomical connections between the hippocampus and between like the rest of the cortical areas and also the PFC.
*  And typically people doing variational auto encoder work assumes there is an input going into a series of hierarchies and arriving to the hippocampus.
*  And the hippocampus sort of try to encode a latent representation that can reconstruct the input to reduce the reconstruction error.
*  But maybe there is a way to improve this by I just realized that you know there is architecture called VEGAN.
*  It's VAE GAN. So it's VAE and GAN connected together.
*  So the idea is that instead of reconstructing the original input you send your reconstruction to for example the PFC.
*  And the PFC serves as a critique or the discriminator in the GAN and tell and feedback the signal that is this realistic or not.
*  And this is a plausible assumption to make because like a lot of patients with schizophrenia if they have lesions in the PFC they cannot tell the difference between imagination and real world.
*  So it might be true that the reconstruction from the hippocampus is sent to multiple modules to compute different cost functions.
*  For example can be both reconstruction or it can be reconstructing another discriminator's function to best reproduce that sensory string.
*  So I think some architectures like this like a multi-head generator model as external memory will be very interesting.
*  Where different parts of cortex serve as different modules for different well like you said cost functions is in the vernacular of AI but purposes I suppose in the vernacular of organisms.
*  Yes. Yeah.
*  Yeah. I mean I also think there is maybe not as exciting lessons to be learned from this work for AI.
*  Like if you build a continual learning system that does store its own examples and manage its own learning then it's going to have to regulate the amount of replay it does.
*  That's a very simple point but I do think that's probably something that will start emerging.
*  And it's an interesting broader question of how do you decide when to learn and how to learn.
*  Ultimately agents we decide oh this was a learning episode I'm going to store that presumably how do you manage those decisions.
*  Because in the original complementary learning systems more replay is better always.
*  Right. And that's one of the take homes here is that you have to regulate that and knowing when to regulate it is a pretty important factor.
*  Yeah. Yeah. Also with that point I think more than more than RL algorithms.
*  It's kind of having like a lot of problems of generating generalizing to new tasks like train on one game and test on the unseen levels of the other game.
*  There are a lot of effort improving this but I think those agents will be benefited by having a different module that specifically estimate the predictability of the captured experience.
*  Instead of like replaying or train on all perceptual data you only train based on the score of that predictor.
*  Like so you can actually filter through your experiences only generate generalize the useful components.
*  So maybe that will help our as well.
*  So one of the recurring themes these days is that AI is moving super fast and neuroscience especially experimental neuroscience because experimental science in general is very slow.
*  But even I think theoretical neuroscience is kind of lagging behind the progress of the engineering in AI.
*  Right. And so what this is is theoretical neuroscience at least partly.
*  Right. We talked about how it's kind of a mixed bag of things.
*  But do you see this kind of work theoretical neuroscience more broadly as being able to.
*  So backing up what what the implication of that rate of progress means is that right now and for the past 10 years or so AI has been informing neuroscience a lot more.
*  And the direction of the other arrow from neuroscience to AI is slow or lagging or lacking.
*  Do you guys see theoretical neuroscience as a way to bring more influence from neuroscience into AI.
*  Yeah I mean I'm used to hear what everybody else has to say but for me I definitely do because I think that you know it may be slow but I think that theoretical neuroscience and kind of really rigorously working out how individual models work and how they relate to the biological brain.
*  I think that that provides kind of fundamentally new and fundamentally more robust conclusions than you can get from just kind of numerical experimentation on very large AI systems.
*  And so I definitely think that you know we wouldn't have gotten to where we currently are in AI without past generations of theoretical neuroscience research.
*  And I also definitely think that you know projects like this where we try to kind of boil it down to the essentials and really analyze everything very rigorously and really try to figure out to what extent this relates to the biological brain will provide useful seeds for future AI research.
*  What do you guys think? Do you guys agree with that?
*  Yeah I mean I think James and I see very similarly on this. The time scale may be long but ultimately I think theoretical neuroscience and psychology just have an enormous role to play in driving AI.
*  But you have to be willing for that impact to happen many years down the line. But just imagine, I mean for instance deep learning right.
*  But the whole thing, the fact that we're using neural networks, those all came from contributions that were worked out in dialogue with neuroscientists.
*  And if what theoretical neuroscientists were doing right now today, 50 years from now, had a similar impact, wouldn't that be amazing and something that everyone would want to work towards.
*  And that's how I really do think that's possible. We don't know what those, it's more inchoate, it's more uncertain. We don't know what these principles will be that will guide us towards even better systems.
*  But having the insights from the brain guiding the inquiry and showing us some of the problems that maybe we didn't even realize were problems is really valuable.
*  But my perception is that the in large part, the majority of folks working in the AI world, what they would say is, well sure theoretical neuroscience may eventually provide us with something.
*  But by that time our systems are going to be so advanced that it won't matter, right. Because we've already basically accomplished that.
*  And I mean, I think that that personally, my personal opinion, it's just an opinion, is silly. Do you think that that's right, that the AI world thinks that? And is it comforting to know that the mass majority is wrong? Or how do you think about that?
*  I do think it's right to say that that's a widespread opinion. I've had AI people tell me, why do you even do mathematical theory? Because eventually I'm going to make a theory prover that's going to do the mathematical theory and explain it back to us.
*  So, you know, just focus on getting the AI system to work. We won't know until, the proof will be in the pudding. My own opinion is that we're going to make, it's going to turn out that today's AI systems, as fantastic as they are, will hit roadblocks.
*  And part of getting them unstuck from those roadblocks will be looking again to the brain, just as happened with deep learning.
*  Again, I mean, I think this history often gets kind of run rough shot over, but the paper on backpropagation, the first author is David Rumelhart, who is a psychologist.
*  The first paper on the perceptron, that's Frank Rosenblatt. He's a psychologist.
*  The contributions, and I remember as an incoming graduate student, the paper that inspired me towards deep learning was from, and I'm sure it's different for different people, there were AI people working on it.
*  But for me, it was Tomas Apagio's work and Maximilian Reisenhuber. And they are neuroscientists, the theoretical neuroscientists.
*  And the reason why they were interested in these convolutional network architectures, even though the rest of the field, hard to remember, but rest of the field was not.
*  They're doing SIFT features, totally different. The reason why they were interested is because they kept looking at the brain and saying, like, this is what we see in the brain, somehow it has to work.
*  So I think that that promise is still there for the future. And if you think about some of the topics like theory of mind, some of these ideas that have come from cognitive science again, ultimately causal reasoning, all of these things have been pointed to by cognitive scientists.
*  And now we're seeing that, yeah, they really are important and require their own methods to address.
*  Yeah, so I guess I think it will continue to be important going forward.
*  I just want to add on that. I totally agree with both James and Andrew. I think neuroscience still has a lot to offer to AI.
*  And especially exciting new direction like Yoshua Banjo has proposed this idea of we should learn from human cognition or animal cognition on the systems to level cognition.
*  So that's comparing to the directly perceptual classification tasks that Apple is Apple is like you have long term deliberate planning and reasoning that you have to think about things.
*  And those abilities are not well captured yet in the current models. And one of the solutions I think Yoshua Banjo was proposing is there's some kind of attentional so-called sparse call to graphs that is a good word model.
*  And you form this causal nose through learning, like whether by semi supervised learning or by other methods.
*  And you form this causal nose and you can actually reasonably within that work model.
*  And the key thing, I think just one of the key things is there's a recent debate about whether to learn things from end to end or just have innate structures.
*  All the other side, like whether to use deep learning or to use good old fashioned AI like mainly on symbolic processing.
*  I think there is a trend now is is actually beneficial to learn the symbol like or abstract representations of entities in the world.
*  It has been an old topic in psychology, but more recently, especially by work by Randall O'Reilly and by Jonathan Cohen's work from Princeton.
*  They show that if you couple a LSTM controller to an external memory and only manipulate the memories indirectly from the keys of the memories.
*  And through learning through many manipulations, you can form this symbol like representations in the keys.
*  So I think that's a kind of a key insight offering like how the brain might be generating those abstract representations.
*  And it could be in like a hippocampal like structure that the cortex and the sensory encoding actually are bound together through fast plasticity.
*  And the cortex can learn to manipulate those memories and eventually symbols are generated by this manipulation.
*  So this is kind of going from sensory generalization to the next level, the out of sample distribution.
*  And it's like a higher systematic level generalization idea that the hippocampus might also offer insights into this process.
*  So I think this systems to level cognition is really like what is needed for a more more powerful or even like more human like agents in the future.
*  OK, guys, this has been a lot of fun. I want to wrap up.
*  Let's do one round of what kept you up last night.
*  What were you thinking about? That's just at the edge of your knowledge.
*  And I know that this is really more of a question for the beginning of a conversation, but something may be unrelated.
*  Since I know you all have different lives outside of this topic that we've been talking about.
*  Wayne, on can you tell me what what's been troubling you lately that you can't quite figure out just beyond your reach?
*  Yeah, a lot of things, to be frank.
*  Yes. So I think reflecting back to the other collaboration, I think there are really two things that really troubled with is so mainly it's just due to the general sense of being in the
*  adequate for so many years.
*  So so being an experimentalist interacting with both Andrew and James and this first few years, I I found this interdisciplinary work just to be extremely challenging.
*  And, you know, I was stepping outside of the synaptic transmission world, single cell computations to cognitive science.
*  Like, I've never heard of dressed to grade amnesia curves before this, to be frank, and I was surprised to find, OK, there are so many diversity.
*  I thought this are all like really figured out.
*  And I was just diving into this research literature and and also on the other side, I dive into the mathematics and modern machine learning is really trying to learn multiple things.
*  That has been extremely difficult, but also rewarding.
*  So still that poses a challenge to me.
*  I think if you try to learn multiple things at the same time, I mean, I'm just barely feeling that I can barely keep up with the minimal amount of knowledge that happening in this both fields.
*  So I still don't know how to deal with that.
*  Maybe more collaborations, but, you know, our human just have certain amount of hours during the day.
*  So how do you read so many papers?
*  That's what's keeping up.
*  Yeah, yeah.
*  Well, you can't read so many papers.
*  So there's isn't there a perfect interleaving of time spent on various things going back and forth?
*  And have you figured that out?
*  Because I don't know it.
*  That's going to be the next normative model.
*  OK, learning strategies.
*  Yeah.
*  So I think the second thing just real quickly is really like this process like with Andrew and James.
*  I mean, I think I talked to me about, you know, really the benefit of really talking to people in different fields.
*  And that's kind of obvious now.
*  But but in the beginning was not easy.
*  Like I felt being an experiment with James and Andrew had to explain things very carefully from very basic level knowledge to build me up.
*  I think I really appreciate that.
*  But also, like through interactions, we found like including my current advisor, Nelson, who are also experiment lists like the communication between theory and experiment are extremely like could be challenging at times because we spoke different languages.
*  Like, for example, like even James and Andrew, like the idea of generalization in machine learning is well appreciated.
*  And that has entirely different meaning in the experimenter's mind.
*  So I think that communication is hard.
*  And also, like I talk about experimental details, that huge complexity in experimental neuroscience.
*  I think that sometimes we just assume people know this knowledge and know this complexity.
*  That's not true either.
*  Right. So I think the natural tendency is really like, OK, I just gave up.
*  We theorists work together because we talk well to each other and experiment with this work together because, you know, it's really effective communication.
*  But I think what's what I learned is it's really important to be patient and to really try to understand each other.
*  So I think that still is challenging science.
*  Communication is super important, important for multidisciplinary research.
*  Is there a role of predictability in this complementary collaborative learning whole organism system system?
*  Sorry, I just I couldn't help the analogy to to go CLS here.
*  But yeah, no, I was joking about the predictability.
*  All right. Well, that's great.
*  Andrew, do you want to chime in?
*  Anything bothering you last night that you couldn't that you you're frustrated, you just can't figure out, et cetera?
*  Well, one very this is very specific deep learning theory.
*  But I actually think it's quite important.
*  When you look at the brain, you see lots of modules.
*  You see this complex interconnectivity of sort of mesoscale modules.
*  And we all think that those modules are kind of specialized for function and kind of not.
*  And it's distributed representations, but also not.
*  And somehow this all is important for generalization and systematic reasoning and cognitive flexibility.
*  And I want to understand why.
*  And it's still very much bothers me that we don't have a theory.
*  But maybe to build on one of Wayne on points to another thing, which keeps me up at night is whether this theory that we proposed will in fact be tested by an experiment.
*  Well, I thought you guys had begun sort of the early stages of thinking about how to actually I was wondering if you had already begun.
*  But I know that you're thinking about how to test it.
*  Yeah. And and if anyone could do it, it would be Wayne on and Nelson's lab is perfect for it.
*  I have, however, been in the beginning stages of many experiments that have not finally panned out.
*  So, you know, it's just I think like when I was saying it's hard to cross these communities.
*  And one of the things that I would love to see is how we can create this feedback loop and virtuous cycle and actually get it functioning on all cylinders to sort of, you know, make the theories concrete enough that they can be falsified and make those experiments actually happen using all the amazing methods.
*  All right. So, James, I'm sorry we ran out of time and can't include you.
*  No, I'm just kidding. James, do you have something that sure.
*  I think it's actually super interesting that, you know, both Wayne on and Andrew highlighted the difficulty of how hard it is actually to kind of really get these feedback loops going very robustly.
*  And I agree with that. And that really does, you know, often keep me up last night.
*  I mean, I guess in reality, last night, there was a big election in Virginia.
*  So maybe that wasn't what was keeping me up last night.
*  But on many nights, I may have been what keeps me up.
*  But I think it may be also related to that.
*  I think, you know, and also maybe going back to a theme of earlier about, you know, the value of kind of abstract models.
*  Like, I think that actually when I am often kept up at night by science, it's often because it's a real concrete math problem that actually keeps me up at night most often.
*  Because I feel like when you get it to that level, you can think about everything so crisply and you can really get the sense of, you know, I'm really about to solve this problem.
*  Like, if I just think about this a little bit longer, I'm going to have that solution.
*  And so actually, there is another one there. And maybe I'll give a little plug.
*  Completely unrelated to this work, I'm collaborating with Tiothe Bir Biswas, I said, you know, we're trying to analyze the links between structure and function in neural networks using geometry.
*  And we've had a lot of really interesting conversations over the last week where I've learned a lot mathematically about, like, how to think about this problem.
*  And that's what keeps me up at night in a positive way.
*  Maybe the negative way is worrying, like, are we communicating clearly enough that we're going to be able to kind of break down these barriers?
*  But, you know, maybe also just highlight that sometimes you stay up because you can't bear to go to sleep and the solution to the math problem is so close.
*  Is the desire for the solution to the math problem due to your background in physics? Or is it just?
*  You know, I think I would actually flip it. I think actually my background in physics is probably due to my desire to solve math problems.
*  And I think that this is why it gets so hard, I think, to cross these boundaries, because I think that, you know, fundamentally, probably why different scientific communities, like why their individuals went into science could actually differ.
*  I mean, for me, it probably really is that the beauty of, like, solving a math problem.
*  But, you know, for many other scientists who have a lot of valuable expertise to lend me, that's not why they went into science.
*  And they went into science for completely different reasons.
*  And so then how do we kind of, you know, not only communicate to each other to help them understand what we understand, but also listen, well, what we're motivated by and go to Andrew's point about like, okay, well, why don't many theories get tested?
*  And I think that a lot of times it happens because the motivations of the theorists and the motivations of the experiment was actually not the same.
*  And so, you know, the theorists may be like, oh, I don't understand why you don't want to test this.
*  But then the experiment was like, I don't know why you keep on talking to me about this boring theory. That's all this other stuff going on.
*  I just found this crazy thing. Like, look at what actually came out of my experiments.
*  And I think that, like, you know, getting those motivations aligned, I think, is another huge part of what will eventually be needed, I think, to kind of close these disciplinary divides.
*  That's a challenge. All right, James. Well, I'm going to let you go do some beautiful math.
*  Guys, thanks for talking to me for so long. It's really cool work. And I appreciate your time here today.
*  Thanks for having us. This was a lot of fun.
*  Thank you, Paul.
*  Brain Inspired is a production of me and you. I don't do advertisements.
*  You can support the show through Patreon for a trifling amount and get access to the full versions of all the episodes, plus bonus episodes that focus more on the cultural side but still have science.
*  Go to braininspired.co and find the red Patreon button there.
*  To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year. Find them at thenewyear.net.
*  Thank you for your support. See you next time.
*  The New Year.

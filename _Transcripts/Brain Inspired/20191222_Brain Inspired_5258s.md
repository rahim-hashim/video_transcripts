---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 5258s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 10717
Video Rating: None
---

# BI 056 Tom Griffiths: The Limits of Cognition
**Brain Inspired:** [December 22, 2019](https://www.youtube.com/watch?v=fgO5CZYwL_U)
*  A key part of the flavor of intelligence that we associate with human beings is that we
*  have to take on complex problems with finite resources.
*  So if you decided that you wanted to have a system that had more human-like intelligence,
*  then using paradigms that force you to solve problems with more constrained resources is
*  the way to get there.
*  This is Brain Inspired.
*  Hey everyone, I'm Paul Middlebrooks.
*  It's an open question these days just how many different fundamental algorithms the
*  brain employs to accomplish its computational goals and how many different neural mechanisms
*  could implement those algorithms.
*  Just as important, or maybe more important, are principles that frame and constrain how
*  those algorithms and mechanisms might occur.
*  One of those frameworks is the resource rationality framework that my guest today, Tom Griffiths,
*  has developed through classical bounded rationality and bounded optimality concepts that you'll
*  hear about.
*  Tom runs his Computational Cognitive Science Lab at Stanford and he uses this resource
*  rationality framework to better understand our cognition and to begin to make connections
*  between Mars' famous levels of understanding, the computational level, the algorithmic level,
*  and the implementation levels that you've heard on the show before.
*  While it's clear that biological intelligence is bound by energy and efficiency constraints,
*  at least I certainly am, it is less clear where those bounds might be for machine intelligence.
*  So it's a question whether our resource limits might actually be a key to what we consider
*  our general intelligence and whether without those constraints machines could manifest
*  that same degree of generality or something entirely different.
*  That is the main topic of this episode, but it's only one of Tom's many pursuits in cognitive
*  science.
*  We also talk about the prospect of artificial general intelligence, whether it makes sense,
*  how we would get there.
*  We talk about Tom's work on developing cognitive prosthetics to help us overcome our cognitive
*  limitations like procrastination, even though I know none of you guys procrastinate, right?
*  Right?
*  And we get into a lot more, of course.
*  One thing we did not get into that I want to mention, Tom talked about how we have more
*  behavioral data now than ever to explore cognition, but we didn't talk about his collaborative
*  project Data on the Mind, where you can access a bunch of data to ask your own questions.
*  So you can learn more about that by going to dataonthemind.org and find out all you
*  need to know there.
*  Find out more about Tom and things that we discuss in the show notes at braininspired.co
*  slash podcast slash 56, where I also linked to his book with Brian Christians called Algorithms
*  to Live By, which is a few years old now, but I highly recommend for a gentle but fulfilling
*  survey of some algorithms in computer science that are relevant to our everyday lives.
*  Thank you guys for your support on Patreon.
*  I'll be sending you stuff soon to increase your cognitive resources and advance you closer
*  to your optimum.
*  To support the show for next to nothing, visit braininspired.co.
*  It's super helpful and thanks again to all my Patreon supporters out there.
*  Okay, talk to you soon and enjoy Tom Griffiths.
*  Tom, hello or as I'm told that the way you greet people, on guard.
*  That means hello in fencing, right?
*  We normally salute in fact before you would get into on guard.
*  My daughter just asked me what salute means and I gave her the military salute, but I
*  guess salute, how do you do it in fencing?
*  Well, I mean, there's a long tradition of different kinds of salutes for different kinds
*  of styles of fencing.
*  The basic thing you do in modern fencing is just bring your blade to your face and then
*  tip it to your opponent.
*  Oh, well, I forgot my blade today, but hello and thanks for being on the show.
*  Yeah, thank you.
*  It's great to be here.
*  So I know that about you because I recently enjoyed your book, Algorithms to Live By,
*  which probably seems now to you to have been written a decade ago or so.
*  But it's about more or less how algorithms that are used in computer science can be helpful
*  in our own everyday decisions and activities.
*  Do I understand?
*  Are you writing a sequel right now?
*  We're working on something which is an audio project, which is a follow up to it.
*  So what we're doing is taking that same algorithmic lens and then broadening a little bit and
*  thinking about the insights that gives us more at the level of organizations and how
*  people kind of work together to do things.
*  Oh, man, you're going to be getting a bunch of consulting calls.
*  So I've heard this book, Algorithms to Live By, called A Gateway Drug to Computer Science,
*  which is a good description.
*  But it also sort of anticipated or joined this recent wave of approaching neuroscience
*  and how our brains work at the computational and algorithmic levels.
*  And I actually see it also as a great introduction to thinking about cognition at this algorithmic
*  level.
*  So I was thinking about this recent explosion in approaching cognition at the algorithmic
*  level and this constant sort of siren call that I hear for more and better theory.
*  That's what we're missing.
*  That's what we need.
*  Right.
*  It makes me think about the early days of neuroscience when people were just starting
*  to record single neuron activity in animals while they were either doing tasks or sensing
*  some visual stimuli, for instance.
*  So our subjective experience is what we're really after, right, is one of the big questions.
*  And the early single neuron studies didn't really address that because the early studies
*  had to do with reflexes in our spinal cord and just moving light bars in front of frogs'
*  eyes and cats' eyes and things.
*  And then only later did we sort of bring that more internally and start relating it to our
*  ongoing behavior and our perception or experience of those events.
*  And I mean, it just kind of dawned on me.
*  Maybe about an hour ago and I was thinking, is that where this algorithmic approach is
*  right now where it doesn't have a lot to say about our subjective experience?
*  But it could be like the very early tools for how our brains, how our minds are doing
*  these things without our subjective experience of them.
*  Does that make any sense?
*  So maybe here's one way of engaging with this, which is to say, if we take this computational
*  perspective, what I do in my research is I ask, what are the computational problems
*  that human beings have to solve?
*  And then what are good solutions to those problems?
*  And then we use those good solutions as a means of then getting insight into human behavior.
*  So we can say, this is the right way of solving this problem.
*  Maybe if this lines up with what people are doing, that tells us something about why people
*  are doing the thing that they're doing.
*  In that analysis, what might be missing is something which is more like what's the subjective
*  stuff that's going on inside people's heads, that's leading to the behavior that we're
*  analyzing in those terms.
*  And I think that's reasonable.
*  I think there's not a lot of room for what a philosopher would call qualia.
*  Oh, man, you said it.
*  You said qualia.
*  So all right.
*  In that computational perspective.
*  And that's actually something that philosophers have talked about as a critique of what are
*  called functionalist views of the mind, that that kind of explanation is something that's
*  missing.
*  So yeah, I agree with that.
*  It's not something that I worry about too much in the course of my research.
*  It's something that I think is a key part of human experience that we might need to
*  look further in order to be able to understand.
*  Yeah, I mean, obviously, it wasn't a criticism of this approach.
*  It's just I'm just kind of wondering if, you know, if that was analogous to those early
*  sort of hardcore single cell studies.
*  So well, I mean, one thing that I've been thinking about is, you know, to what extent
*  something like consciousness can have a computational explanation.
*  Yeah.
*  And there are there are arguments where, you know, you can you can give an argument for
*  why you need something like consciousness, but they're kind of they're architecturally
*  constrained sort of arguments.
*  So like arguments that are based on the idea that you maybe your brain has a bunch of modules
*  that are solving problems and those modules operate unconsciously and then that information
*  needs to be aggregated together somewhere.
*  Right.
*  And consciousness is the place that does this.
*  So this is this is Bernard Barr's global workspace theory and sort of outlines of you like that.
*  Yeah.
*  And so I think what's missing from that kind of argument from a computational perspective
*  is the a priori justification for why it is that that would be the way that the brain would
*  work.
*  Like, why is it that that's necessary in order to produce an agent that does all of the things
*  that human beings do?
*  And those are the kinds of questions that I get preoccupied by when I think about these
*  topics.
*  Well, OK, in the spirit of your chapter in the book on Bayes rule, you I think you start
*  off the chapter by talking about the Copernican principle.
*  And this is essentially Bayes rule with an uninformed prior, which states that if you're
*  trying to guess how long something will continue, if you don't know anything about if you have
*  no good prior, then the best estimate is that it will to guess that it will continue for
*  as long as it has lasted already.
*  So with that in mind, what do you what is your estimate for how long will continue to
*  be unsatisfied with our understanding of of subjective experience?
*  Is the Copernican principle at play here?
*  Yeah, so so that that analysis assumes that so that the uninformed prior there says that
*  you don't even know whether it's reasonable to measure the duration of something in seconds,
*  minutes, years, centuries, millennia, so on.
*  It's kind of like agnostic as to what any of those scales might be.
*  So that may not be a reasonable prior to start with when you're thinking about things that
*  are operating at a human scale.
*  But certainly applying that, yeah, we've got we've got a while ahead of us.
*  OK, you're going with a while.
*  I like that. And thanks for playing, because I'd say 90 percent of the people that when I
*  you even brought up the word qualia, which is way beyond what most people are comfortable
*  talking about on the show. So that's great. So anyway, it's a great book.
*  I'm looking forward to the audio project.
*  Are you doing an audio project because you don't want to do another book tour circuit?
*  No, it was really we.
*  So this is with my my co-author, Brian Christian.
*  We were just excited about having the chance to explore some of these ideas in a different medium.
*  So the the audio book version of our book was actually extremely successful.
*  I think it was perhaps more successful in the print version.
*  And that made it clear that people enjoy listening to these kinds of ideas.
*  So we had the opportunity to think about doing something that would be not necessarily audio only,
*  but perhaps audio first.
*  And so we've been enjoying the process of doing that.
*  So we've actually been traveling around and interviewing people.
*  And it's a much more intimate experience because when you do audio, as you know,
*  one of the things you care about is getting high quality recordings.
*  And that means getting people in studios and going to the houses and so on.
*  And so when we did the book, we were sort of calling people up on the telephone and talking to them
*  and getting their versions of their stories.
*  But I think the process of just like interacting with people in all of these different settings
*  has added this physical component to the project that's been really interesting.
*  That also adds a lot more editing, I imagine.
*  Yeah, so we work with a producer who's doing that.
*  And it'll be released through Audible next year.
*  Oh, great. All right. That's the target anyway.
*  This is another...
*  No, I think we're going to hit that one.
*  Good luck on it. Yeah.
*  So the previous book, Algorithms to Live By and this new project,
*  align with what I assume this new project align very well with one of the main focuses of your work,
*  essentially how to choose the right algorithm given how limited we are cognitively.
*  And you've, you know, over the years developed what's called the resource rationality framework,
*  which we'll work up to here.
*  So I'll start with a quote by Herb Simon from 1957.
*  He said, the capacity of the human mind for formulating and solving complex problems is very small
*  compared with the size of the problems whose solution is required for objectively rational behavior in the real world.
*  In other words, if there's a complex problem, perfect solutions require more than our brains are up for.
*  And he developed this concept of bounded rationality,
*  which was later developed into a concept called bounded optimality,
*  which is where this resource rational analysis framework comes from.
*  What got you interested in bounded optimality in the first place?
*  Was it an interest all along or did it develop over time?
*  So my trajectory here was roughly.
*  So I started working on what we call rational models of cognition or probabilistic models or Bayesian models in grad school.
*  So Josh Tenenbaum and I really took that idea.
*  And, you know, my experience of that in grad school in the early part of my career was really taking that perspective
*  and then applying it to kind of one problem after another.
*  Right. And this is this perspective that says, let's think about the abstract computational problems human beings have to solve
*  and then find ideal solutions to those.
*  And that's normally done in a way where we don't care about how complex it is to solve that problem.
*  So, for example, you know, if you want to describe human learning,
*  you can describe human learning as a process of Bayesian inference,
*  ignoring the fact that Bayesian inference is something which is in itself extremely computationally costly.
*  So that gives you a way of then saying, you know, answering questions about cognition in this kind of why way,
*  which is, you know, why is it that people do that?
*  They do that perhaps because that's a good way of, you know, that's what the ideal solution to this problem looks like.
*  But that perspective is also something that I think a lot of traditional cognitive psychologists found unsatisfying
*  because cognitive psychology is not about behavior necessarily as much as it's about identifying the cognitive processes that underlie that behavior.
*  Right. And so those computational level explanations are things that are a why story that don't give us a how story.
*  Right. And so I thought a lot about how do you bridge that gap?
*  And it's it's a gap between what David Ma would have called different levels of analysis.
*  So the computational level is this abstract. What's the problem that's being solved?
*  What's the ideal solution? And then you have the algorithmic level, which is how is that solution implemented in an algorithm?
*  That's kind of the level of cognitive psychology, cognitive process.
*  And then the implementation level, which is how is that algorithm implemented in some physical thing?
*  And that's like neuroscience. And so bridging those levels, the computation and computational and the algorithmic level,
*  I felt like was something that would be important for two reasons.
*  One is to be able to connect the kinds of theories that we were developing to the traditional kinds of explanations in cognitive psychology.
*  And the other was that it gives us the opportunity to address some of the ways in which people systematically deviate from those ideal, rational, computational level solutions.
*  And that's something that's particularly salient in areas like decision making.
*  But we've known for a long time that people don't do the thing that the sort of classic rational theory says that they're supposed to do.
*  But it's also something that's going to show up across different areas of psychology as we get enough data that allows us to then differentiate what signal and what's noise in the behavior that people are producing
*  and then be able to separate what people are doing from the predictions of those rational models make.
*  One of the ways that people deviate, one of the labels given to the way that people deviate from perfectly rational behavior is heuristics.
*  And one of the things that's fallen out is that you make the case that heuristics actually are optimal behavior given our some of our limited resources.
*  So heuristics, good or bad?
*  Yeah, I think heuristics. So heuristics can be good or bad, depending on whether it's a good heuristic or not.
*  So where we started out in terms of trying to bridge this gap was by looking at the things that computer scientists and statisticians do for solving these problems where you do care about computational cost and then using those as psychological theories.
*  And so, for example, to make Bayesian inference easier, instead of calculating your posterior distribution over all of your hypotheses, which is what Bayes' Rule tells you how to do, you sample a few hypotheses from that distribution.
*  And so doing that random Monte Carlo sampling process is something that saves you a lot of computation because now you only have to think about a subset of your hypotheses.
*  And so when you start thinking in those terms, you can show that some of the kinds of heuristics that have been identified by psychologists are things that are actually reasonable sorts of strategies that we can make sense of in terms of those kind of Monte Carlo models.
*  And that then got us asking the question of, well, how can you tell what's a good way of approximately solving a problem?
*  If you're going to follow a heuristic, then let's have a way of saying what's a good heuristic.
*  And so this notion of bounded optimality tells us exactly that.
*  It says, what a rational agent should do is not necessarily just choose the very best action as what classical theories of rationality say.
*  You focus on choosing the action that has the highest expected utility.
*  The bounded optimal agent executes the sequence of computations that get them to the point where they're if they take an action based on the beliefs that result from those computations, the result of that action is good relative to the computational cost of the computations that they executed in order to get there.
*  Right. And so that gives you a criterion for evaluating a heuristic.
*  Right now, a heuristic, you think about it as a sequence of computations that you're going to follow to try and solve this problem.
*  And bounded optimality says a good heuristic is going to be one that finds the right balance between error and computational cost, right?
*  Between the utility that you derive from following that heuristic and the computational cost that was involved in executing it.
*  And so that's a way of taking an intuitive notion, a heuristic, something that had kind of been suggested in the psychological literature before and turning it into something which is much more precise, which is now we can say a heuristic is going to be a sequence of computations and a good one.
*  It's going to be something which optimizes this this trade off.
*  So bounded rationality sort of started with without a prescription of how to go about doing this, but just more laying out the problem, the framework right from Herb Simon and then bounded optimality really systematizes how to how to how to optimize, I suppose, how you're going about solving these problems under limited resources.
*  Yeah, that's exactly right.
*  So I would think about bounded optimality as a theory of rational behavior for finite agents.
*  And that's the way that so people like Stuart Russell and Eric Horvitz, who are AI researchers, develop this framework because they were encountering the problem of thinking about, well, if I'm building an AI system, I have to decide how much computation I'm going to put into solving a problem.
*  Right.
*  And that wasn't something that was addressed by this kind of classical notion of rationality.
*  And so they needed to work out what was the right way of making these trade offs in order to think about what's the right way of building their AI systems.
*  And, you know, the theory of rational behavior for an AI system with limited compute is actually a much better theory of rational behavior for a human being who has limited compute.
*  Right. Yeah, it's interesting because at least at first pass, one might or I might think of, you know, computers, well, they have essentially infinite resources.
*  And so they should always go for the maximally rational answer.
*  Right. But but in fact, they're subject to the same time and resource constraints. Well, not the same, but a similar set of time and resource constraints that we are.
*  Yeah, so that's I think that's true of, you know, sort of like fielded computer systems that have to make these trade offs because those systems are engaged in solving the problem of, you know, I have to do this so I can do the next thing and do this so that I can do the next thing.
*  Interestingly enough, that paradigm does not characterize a lot of what's going on in AI research at the moment.
*  So a lot of the recent breakthroughs in AI have been a consequence of essentially, you know, there's a lot of smart innovations that are going on in terms of designing these systems and thinking about how to structure them appropriately and how to, you know, coming up with better algorithms for training them.
*  But another big part of what's been happening is that people are throwing increasingly large amounts of compute and increasingly large amounts of data at the systems in order to get to the point where they're then able to do things which are, you know, which are more impressive than the things that they were able to do in the past.
*  And so there's a sense in which, you know, if you extrapolate from current trends in AI, we're going to see AI systems, at least in these kind of showcase examples being things that are using increasing amounts of compute.
*  Whereas human beings are intrinsically characterized by a limited amount of compute, what we're able to carry around in our heads.
*  And so you can extrapolate that there's going to be a sort of divergence there where I think about it as one of the things that's characteristic of human intelligence is the fact that we have to solve problems with the finite amount of compute that we have.
*  Whereas AI systems aren't necessarily subject to those constraints.
*  And so that might be a way in which we might expect the intelligence of these AI systems to diverge from human intelligence.
*  So this makes me want to talk about artificial general intelligence.
*  Maybe we'll get there in a minute.
*  But so do you see constraints as a sort of a tool in that respect?
*  But, you know, so as a generative tool to for cognitive processes to settle on because they're limited by these constraints, right?
*  It's almost like scaffolding for the building up of cognitive processes.
*  Does that make sense?
*  Yeah, well, I would say, you know, the key part of the flavor of intelligence that we associate with human beings is that we have to take on complex problems with finite resources.
*  And so that means that humans have to develop a capacity for what we call meta reasoning, which is deciding how to decide.
*  Right. Or, you know, deciding how it is that you're going to deploy the computational resources you have in order to solve a problem.
*  And that doesn't have to be explicit.
*  What it basically means is that, you know, a lot of what human brains do is when you encounter a new problem, figuring out how to break that problem down and think about how to solve it in terms of the pieces that you have from the way that you've solved problems in the past.
*  And so we're looking for the kind of generalizable structure across problems.
*  And our brains are good at reorganizing things in ways that allow us to exploit that structure in order to be able to effectively, maybe not optimally, but effectively solve a wide range of problems with a finite amount of resources.
*  Is there one meta level or are there multiple metas?
*  So in our work, we focused on one meta level.
*  And there's a good reason for that, which is basically as you go, as you get more meta, there are decreasing returns.
*  So we find going one level meta makes a big difference for the what's called the object level, which is where you're actually making decisions.
*  Then as you get more meta than that, it doesn't make as much of a difference.
*  Diminishing returns.
*  Yeah, so there's one exception to the, you know, staying at one level of meta in the research that we've done, which is we've looked at, you can think about it as architecture design as a meta meta level problem.
*  Right. So the yes. So the problem, the first object level problem is I'm going to make a decision.
*  The meta level problem is which system should I use to make this decision?
*  And then the meta meta level problem is what kinds of systems should agents have access to in order to do a good job of making decisions?
*  Right. And in the work that we did on that, this was with the Falk leader and Smith and Milley and Falck has played a big role in developing this resource rationality and bounded optimality research program.
*  He's now at the Max Planck Institute in Tupingen.
*  So what we did was show that for a bunch of different problems, you want something like a two system architecture, like a fast and a slow system.
*  It's always two. It's always two for some reason.
*  Well, that was that was the question that we were interested in.
*  So as a, you know, as a somewhat cynical psychologist, I had had for a long time said, you know, well, the reason why you see lots of two systems theories in psychology is that two is the simplest thing after one.
*  So is that okay? Well, you know, we've ruled out the one system thing.
*  What what could it be to, you know, but what we showed in this analysis is that there's a sense in which two is kind of a sweet spot where there's a big difference between two and one.
*  They're not such a big difference between two and three or two and four and so on.
*  And the reason why there's a big difference between two and one is that it's exactly that it enables you to have that meta level.
*  Right. So if you've just got one system, you're solving problems the same way all the time.
*  Yeah. If you've got two systems, then you can be adaptive.
*  And so you're using different strategies for different problems.
*  And that's something which results in potentially a pretty big increase in performance.
*  And then having three systems, you know, helps you a little bit.
*  But if you assume that there are some increasing cost for more systems, then, you know, two ish turns out to be a pretty pretty sweet spot in terms of enabling decision making agents to do a good job of solving different problems.
*  And the thing that determines exactly how many systems you want in our analysis is the ratio of the variance of the utilities across problems to the to the to the time costs across problems.
*  And so what that means is if you're going to have agents that need to decide whether to pull a toddler out from in front of a speeding truck and figure out whether you should declare a nuclear war,
*  right, that's a pretty big range of like utility and time costs such that it can make sense to have different kinds of systems for solving those problems.
*  And so the bigger that range gets, then the more pressure you get to have systems that are able to cover more things that lie in that range.
*  All right. So we've already gotten kind of in the weeds.
*  So let's just back up a little bit here. And so one of the one of the assumptions that the resource rational analysis makes is that we do indeed make rational use of our even though our cognitive resources are limited, we make rational use of those limited resources.
*  Do we do you feel confident?
*  So, so to me, it doesn't necessarily matter that much in an important sense. So resource rationality is a framework, right? So resource rationality just means using this idea of bounded optimality as a tool for making sense of human behavior.
*  Right. And that's not a claim about human behavior. It's a methodology for studying human behavior.
*  It's not a theory. It's a framework. It's a methodology.
*  Yeah, yeah. So we're so we're not saying people always rationally allocate their resources. And that's how we solve problems.
*  What we're saying is, if we want to understand human cognition, one of the critical things that's involved in human cognition is this problem of how do we allocate our computational resources.
*  And as a consequence of that, if people are doing a pretty good job of that, we're going to be able to get leverage on understanding human cognition by working out what the resource rational strategies look like, and then using those as a as a lens or a, you know, a comparison, a way of then parsing out the aspects of human behavior that we want to understand.
*  So, yeah, it's not an empirical claim. It's a methodological proposal. And in order for that methodology to be useful, right, I think I think one thing that people get concerned about is, you know, is this falsifiable or not?
*  And it's not really relevant whether it's falsifiable, because it's not a theory. It's not a theoretical claim. It's what matters to thinking about this is whether it's a useful way of looking at the mind. And then that's something we're going to determine empirically by seeing, does this help us understand what people are doing across a bunch of different contexts.
*  And I think the to me, one of the really important ways in which it's useful is that it's generalizable. So as much as is wrong with that classical theory of rationality, it has one really nice feature, which is that if you have a new situation, and you know what the utilities are that people assigned to different outcomes, then it makes a prediction about what people will do in that situation maximize expected utility prediction happens to be wrong, but it makes a prediction about what people will do in that situation maximize expected utility prediction happens to be wrong, but it makes a prediction about what people will do in that situation maximize expected utility prediction happens to be wrong, but it makes a prediction about what people will do in that situation maximize expected utility prediction happens to be wrong, but it makes a prediction about what people will do in that situation maximize expected utility prediction happens to be wrong, but it makes a prediction about what people will do in that situation maximize expected utility prediction happens to be wrong, but it makes a prediction about what people will do in that situation maximize expected utility prediction happens to
*  an important pattern, which is that it makes a prediction. And it does that for all of these different circumstances you can put people in. And that's quite different from, I think, a lot of psychological theories which say, oh, people could do this or they could do that or they can do this or they can do that. And we sort of identify these context specific heuristics or strategies that people follow in particular situations but don't necessarily have an overarching theory that helps us to say exactly what people were doing in a particular context. And so resource rationality gives us a way of making
*  about what people are going to do across a wide range of contexts. And that
*  matters if you're an engineer trying to figure out how to build systems that are
*  going to interact with human beings where you need to be able to sort of
*  have a way of interpreting the behavior that the human beings are producing in
*  terms of things like their beliefs and their desires and their knowledge and
*  their utilities and so on. As an engineer you need to model the individual.
*  As an individual you need to model the world. One of the things that this
*  approach does and I mean there's so many different things to talk about but one
*  of the things that it does is it attempts to bridge Mars levels which you
*  articulated earlier that from the come mostly I'd say from the computational
*  level to the algorithmic level right so there's a lot I've been a lot of
*  discussion on okay we have these three different levels of explanation and
*  understanding but it's a problem going from one to the other and that's one of
*  the strong suits of the resource rational approach. So how does this
*  approach bridge from the computational level to the algorithmic level let's
*  say? So it does that because our starting point is a computational level problem
*  right so our starting point is saying here's the thing that people need to be
*  able to do like as an example make a judgment of a quantity right so you know
*  I'm gonna ask you what would you guess a particular value is we can say you know
*  based on some knowledge that you have and some you know some pieces of
*  information that are available to you I want you to to estimate this particular
*  quantity right so that's our computational level problem we can work
*  out a computational level solution to that which is based on the information
*  that you have compute a posterior distribution over the value of that
*  quantity you know use Bayes rule plus the data that you have some prior
*  distribution you had put those together and you get a posterior distribution
*  great and then the algorithmic level part is now we say well how could you
*  implement that so maybe you can implement that by having some kind of
*  sampling algorithm that's gonna give you a way of drawing samples from that
*  posterior distribution so you don't have to compute the whole thing but it'll get
*  you to something that on average is gonna look like the right value and then
*  the the bounded optimal part says okay now you've given me an algorithm now
*  let's find the right trade-off between that algorithm between the the the error
*  that that algorithm is gonna make and the amount of time that you're gonna
*  spend you know computing the amount of computation you're putting into it and if
*  you know what the cost of thinking is right the opportunity cost of what you
*  could be doing other than solving this problem and you know what the payoff is
*  for getting a better estimate then you can put those together and you can make
*  a you can identify the point where you should stop thinking and just you know
*  act on the estimate that you currently have and so go ahead yeah so so as a
*  consequence of that we can make a prediction about at the algorithmic
*  level this is the the sequence of computations we expect people to engage
*  in when they're solving this particular version of the problem and you make the
*  point and by the way you have a really nice behavioral brain science paper
*  coming out of I don't know if you have the rebuttals to it yet or what but yeah
*  I think we're done with that process I don't know what's out yet okay well I
*  read the paper without the rebuttals anyway where you go through all of this
*  so it's it's a really great resource for me you have a couple great papers where
*  you really walk through these things but what I was gonna say is another premise
*  that evolution is taking care of this this is not something that you are
*  suggesting that humans do in every given situation but this is something that
*  through the constraints of our cognitive resources evolution has brought us to
*  this point is that right yeah so the way that I think about it so you asked
*  before like how meta do you need to get like how many levels of meta I think you
*  know one reason why I'm not concerned about an infinite regress there so I
*  said one one thing is you have these diminishing returns right the other
*  thing is that I think about each level of meta as operating on a different
*  time scale right so you're making a decision that's something that operates
*  on the time scale of let's say seconds right the meta level above that is how
*  are you developing strategies for making decisions in general and that's
*  something which could be at the scale of hours or years or whatever it is
*  right are you going to the Big Bang with this are you going to the entire
*  universe and if you go to the meta level above that that's kind of like what
*  architecture do you have what are the the you know the the computations that
*  are available to you for solving those problems and that's something which is
*  that like an organismal lifespan sort of time scale right that you know you're
*  talking about and so so as you're working up you know any of those things
*  that you can imagine being things that are adapted as a consequence of learning
*  or evolution or cognition right but those processes operate on different
*  time scales as well so if we think about individual decisions those decisions
*  they could be the consequence of some you know evolved reflex but you lose
*  some adaptivity there so going all the way to just sort of figuring it out on
*  the fly is the way that you get most adaptive and maybe that makes sense for
*  a lot of those you know second time scale level things when you start talking
*  about your meta level strategies you could figure those out on the fly where
*  you're like oh for this problem it has this structure so it's not worth
*  thinking more right so cognition can be involved in coming up with those meta
*  level strategies you do some explicit meta reasoning to do that but there are
*  also things because of the time scale that you're operating on that you can
*  imagine learning as habits over time right you kind of learn good strategies
*  for solving problems and as you acquire expertise in a domain you're gradually
*  getting better at those things or you could imagine that those are things
*  which are a consequence of again an evolutionary time scale you lose some
*  adaptivity but you know the you can imagine to the extent that you need to
*  be adaptive that's going to determine whether that makes sense to think about
*  in those evolutionary terms and then at that meta meta level then you're talking
*  about stuff that's you know mostly evolutionary right unless you're
*  unless you're doing things like for example I think about things like
*  mnemonics as a meta meta level thing that you can do as a learning intervention
*  right so for example I you know I taught myself a set of peg words that I can use
*  for memorizing things and so if I'm in a situation we're like okay now I need to
*  you know 14 things I'm not gonna try and do that I know that it's gonna fail to
*  use like just regular sort of short-term memory which is extremely fast to use
*  but yeah pretty limited and so I'll switch to using the peg words which is a
*  little more laborious but it can give me a bigger capacity right and so that's a
*  case where you're giving yourself that extra bit of cognitive architecture by
*  you know training this this extra capacity that you can then use for
*  solving other problems yeah but in that case by leaning on a different algorithm
*  essentially by co-opting it one could say yeah it's giving you giving yourself
*  access to a different algorithm yeah okay so that's computational to
*  algorithmic level but this strategy does it apply also go from going from the
*  algorithmic level to the implementation level down at the neuronal mechanism
*  level I think I think you can use a similar kind of strategy right this
*  strategy has a name which is called optimization and so you can ask so the
*  equivalent question going from algorithm algorithmic to optimization is what
*  would be the best way of realizing this algorithm in say a neural architecture
*  given these pieces of neural architecture that's a kind of question I
*  have no idea how to answer I'm not a neuroscientist well we don't either
*  neuroscientists don't either but yeah but I think the neuroscientist can ask
*  that question right so if you say look here are the pieces from which I can
*  build a neural circuit what's the best neural circuit to build to execute this
*  algorithm yeah that's a well-defined kind of problem and I think you can see in
*  practice in machine learning people engaging a little bit in that exercise
*  where they do things like you know these sort of complex searches over neural
*  network architectures and so on so what they're doing there is saying I'm gonna
*  fix an algorithm that algorithm is going to be you know learning by gradient
*  descent and I'm gonna optimize over the neural architecture here in a way that's
*  gonna try and find a good inductive bias for solving the problem that I want to
*  be able to solve and then the sort of the story about the implementation right
*  at that point of you know of this learning circuit is something where you
*  can say yeah doing that hyper parameter search or architecture search that is
*  implicitly an optimization that's kind of saying let's sort of fix the algorithm
*  that we think we're trying to trying to learn how to execute well we're gonna do
*  this via gradient descent and now we're gonna optimize over you know neural
*  architectures or whatever it is have you gotten feedback much from from
*  neuroscientists like what about this approach you know has it connected I
*  don't think so the lesson that I think about here for neuroscientists is more
*  about what I think of as I give talks where I call it silver bullet syndrome
*  which is so when we were working on Bayesian models of cognition you know
*  there were a lot of neuroscientists who were interested in that and you know
*  there are whole books about like the Bayesian brain and so on right and a lot
*  of the way that neuroscience engaged with that was saying something like okay
*  at the computational level you have Bayes so now let's go and figure out how
*  the brain does base out of the brain does base yeah and that means like find
*  the one neural circuit that does Bayesian inference or the strategy the
*  right way of coding and so on and there's like lots of papers that fall into
*  this genre of this is the thing that allows you to do Bayesian inference so
*  you know proposing the one silver bullet that's gonna be the way that the brain
*  does base yeah and so from my perspective I would say the big problem there is
*  that you missed a level of analysis which is this algorithmic level right and
*  so if we look at how computer scientists and statisticians do Bayesian inference
*  it's not that there's one thing that is done in order to efficiently do Bayesian
*  inference there's not one sort of you know you like it's not like you can
*  build one device that's gonna solve all of your Bayesian inference problems
*  different problems have different structures and and it's more efficient to
*  use different algorithms for solving those problems and so we see a kind of
*  what I would call a mechanistic plurality right that when we ask what are the best
*  algorithms at that algorithmic level we're gonna see lots of different kinds
*  of algorithms being used and I would expect the same kind of mechanistic
*  plurality at the level of implementation right that if you've got important
*  sampling a markup chain Monte Carlo and variational inference and all of these
*  different strategies for approximating Bayes at the algorithmic level those are
*  going to be instantiated in different kinds of circuits and we might expect to
*  see the same kind of plurality and in the ways that the brain does base and
*  that would be that step would be an optimization in optimizing selecting
*  amongst the the multiple mechanisms possible yeah or just saying you know
*  like based on the computational structure of the particular problem that
*  a particular part of the brain has to solve yep we're gonna expect to see
*  different kinds of algorithmic level solutions to those problems and we're
*  gonna expect to see different architectures that are better at
*  implementing those kinds of algorithms and do you see that it could be multiple
*  for instance at the algorithmic level multiple algorithms simultaneously
*  working or does it need to select amongst one because then you run into an
*  efficiency issue as well yeah I mean I think you could believe that again it
*  comes down to this sort of point about adaptivity right like to what extent are
*  you always solving the same problem or are you encountering different kinds of
*  problems right and so you can expect that there are some things where it's
*  essentially the same problem all the time right it's just sort of variance on
*  that and then you'd expect to see one way of solving that and in other cases
*  yeah you're gonna be trying to do different things at different times that
*  are gonna require different solutions and so you might expect to see some
*  multiplicity like the silver bullet syndrome it's so it's like I have that
*  and shiny object syndrome like every every time I do an interview like you
*  know I dive in and like ah that's it's the new object and it's the solution to
*  everything you know yeah so it's I don't know there's there's probably some value
*  into putting your blinders on and only focusing on your one problem right yeah
*  I mean I think the way that we make progress is by taking individual problems
*  and really nailing them in a way where you can begin to understand some of the
*  complexity of those problems so having said that what I do is look at lots of
*  different problems and try and figure out what the things are that are the
*  generalizations across them yeah so those are those are two different
*  strategies right but a lot of what my lab has been doing lately is actually
*  thinking about like using the fact that it's so much easier to get more
*  behavioral data now to collect really large data sets and dig into those
*  really large data sets and the thing that we consistently find there is that
*  human behavior is complicated and we didn't have enough data before to really
*  make reliable models of complex behavior and so we focused on you know as we
*  should from a sort of statistical bias variance trade-off perspective we focused
*  on simple models because we had small amounts of data and as we get lots more
*  data we can start building more complex models and we discover it's never just
*  one thing that's going on it's that's that there's a lot of stuff that's going
*  on and we need to develop modeling frameworks that allow us to deal with
*  that that amount of complexity and so that's that's a kind of at this point
*  still a promissory note but one of the things that excites me about bounded
*  optimality and resource rationality is that it's a kind of framework where we
*  can keep pushing on it and start you know as we as we learn more about the
*  computational architecture and the kinds of computations people are able to
*  execute you can you can start deriving more complex models and one reason why
*  that's important is that as we were talking about humans are limited right
*  yeah so if we're dealing with really complex phenomena and we want to be able
*  to figure out what are good theories of those phenomena and we want to be able
*  to do that from first principles having an automated way of going from here are
*  my assumptions about the computational problem here are the pieces that I think
*  the mind can put together for solving that problem how should we put those
*  pieces together in order to solve that problem there's a point where that
*  outstrips the complexity of the minds of individual scientists and so having a
*  framework that allows us to automatically derive predictions from
*  that way of framing the problem is something that I think is going to
*  become more and more important yeah you just touched on a lot of subjects that
*  we could go down well you talked about machine learning a few minutes ago and
*  you know ways of approaching this through machine learning so so how does
*  the resource rationality rational analysis approach how does it connect
*  the AI world and biological intelligence so I mean the first connection is that
*  this is an idea that began in the AI world that we're now using to explain
*  biological intelligence right so trying to understand human cognition in terms
*  of this sort of framework for thinking about how to use finite computational
*  resources I think the the second thing it does I I think that there's an
*  important way in which it dissociates the human and artificial intelligence
*  which is that if human minds are characterized by having finite
*  computational resources and artificial intelligences are not then we wouldn't
*  necessarily expect that an artificial intelligence would develop that same
*  capacity for meta reasoning and the kind of flexibility that I've been talking
*  about because it's not a prerequisite for them to be able to do whatever it is
*  that you're asking them to do right so there's a an important sense in which
*  this characteristic that we see and we think of as as being an intrinsic part
*  of intelligence which is being able to sort of flexibly adapt to the different
*  problems that you face and deploy the resources that you have to solve them
*  could ultimately be a characteristic of particularly human intelligence because
*  of the computational constraints that human minds operate under you've
*  suggested that putting an artificial intelligence exposing them to these same
*  constraints we might expect them to develop more human like intelligence
*  yeah so that's so that would be the question right so if you decided that
*  you wanted to have a system that had more human like intelligence then using
*  paradigms that force you to solve problems with more constrained resources
*  is the way to get there right so if we look at human intelligence and the kinds
*  of computational problems that human beings have to solve those computational
*  problems are characterized by the fact that human beings have finite compute
*  because we're limited to what we can carry around you know inside our heads
*  and finite time because we're limited by our human lifespans and energy finite
*  energy yeah yeah which is the same thing but yeah that's right so so those those
*  two things define the scale of human intelligence right the scale at which
*  the scale of the kinds of problems that human beings are able to solve and so if
*  we think about that okay you're subject to those intrinsic constraints and now
*  we ask the question how do you design an organism that makes the very best use of
*  the resources that they have given that those resources are limited then you
*  know my hypothesis is that's where you end up with something that looks like
*  human intelligence right the human intelligence is an adaptive response to
*  having finite compute and finite time and so these things that we see that are
*  differences between things that human beings can do and things that current AI
*  systems can do things like being able to efficiently restructure problems in ways
*  that allows us to reuse past computations in order to solve these things right or be able to exploit
*  information that we've learned from previous experience in order to make it
*  easier for us to learn in a new setting these processes that we call meta
*  reasoning and meta learning those we think of as being intrinsic to
*  intelligence but I'd say those are things that are intrinsic to human
*  intelligence and are a consequence of the constraints under which you know
*  human beings have operated and so if you want to make AI systems that have those
*  human-like capacities then yeah taking setting up this constrained problem is
*  actually a way of thinking about doing that but you don't necessarily have to
*  do that right like it might be there are just different kinds of intelligence
*  and that's part of what we're figuring out as we get into this yeah this idea
*  of this the space of possible minds and space of possible intelligences so so the
*  idea of artificial or rather the idea of general intelligence is often expressed
*  in terms of humans because this is the only example of quote-unquote general
*  intelligence that we have but you know the more I learned that the less the
*  concept of general intelligence itself makes sense and then the desirability so
*  artificial general intelligence is often stated as the goal to build intelligence
*  like human intelligence which that makes less and less sense to me seems less and
*  less desirable the more we we learned what do you think does a GI make sense
*  and is it desirable yeah so I think it comes down to exactly what your goals
*  are in building intelligent systems right and I think you can make an argument
*  that building systems that are intelligent like humans is different
*  from building the most intelligent systems we can build right although
*  ultimately I think you would expect yes there are going to be computational and
*  data limits that are gonna affect AI systems and being able to do a better job
*  of accommodating those is potentially going to make those AI systems function
*  better but I mean the examples that I think about here are things like goals
*  right so if you look at the if you look at the literature on AI starting with
*  you know Simon and Newell through to you know attempts to build systems that can
*  do a good job of solving Atari games like Montezuma's revenge which involved
*  these kind of long planning horizons there's a lot of emphasis on you know
*  finding goals and subgoals and sort of you know that exploiting that part of
*  tasks and that's something that human beings certainly do humans are really
*  good at figuring out how to break down problems into a structure where they're
*  then able to work out you know how to deploy their intelligence of these
*  different levels of abstraction but it's also something which is intrinsically a
*  consequence of human limits you don't need goals if you have infinite compute
*  right like if you could just plan all the way to the end of a problem you don't
*  need subgoals you have the one yeah that's right you don't you don't need to
*  have like you know intermediate subgoals yeah so so you're you can just say okay
*  I'm just gonna solve that problem yeah yeah and so so to the extent that we
*  need those things it's it's it's a consequence of dealing with the
*  limitations under which we operate but that's sort of assuming a static
*  environment right because environments change and are dynamic so then you yeah
*  sort of necessitates changing your goal you might you might change your goal but
*  you still don't necessarily need subgoals right so like the point is like
*  if you're planning horizon is of a length which is equivalent to the
*  structure of the problem that you're solving then you don't need to be able
*  to reduce the problem to something where you have subgoals in order to solve it
*  right and so so I think about things like AlphaGo as an example of this where
*  I think it was a good demonstration of what happens when you start building
*  systems that have superhuman planning horizons where it would make moves and
*  people be like we have no idea why I did that you know and and it wasn't playing
*  in a way where they were recognizable subgoals from a sort of human
*  perspective right because all that it was focused on was you know getting a
*  half-point advantage 25 moves into the future right and that's what you can do
*  if you have you know enough compute and an effective representation of the
*  problem. Well so is AGI desirable do we do we you know how do we what do we want
*  our artificial intelligence to look like do we want human-like companions or do
*  we want a ton of super specialized high compute I mean and this actually can
*  lead into your work on cognitive prosthetics? I don't know what we want so
*  I don't I don't know what we want I think that's a question that I think
*  we're all trying to find answers to but my real focus is on understanding human
*  cognition and so for understanding human cognition then these problems like
*  meta reasoning and meta learning are exactly the things that we need to focus
*  on and in terms of making sense of how it is that people solve these problems
*  of you know finite resources and doing the best we can with what we've got so
*  the other side of that though is we can ask the question if a lot of human
*  behavior and in particular a lot of maybe undesirable aspects of human
*  behavior are a consequence of those finite resources then as we develop
*  other kinds of computational resources how do we best deploy those computational
*  resources to help humans out? Don't we build an app and or a cognitive
*  prosthetic? Yeah so with Falk Leader we've been working on this line of
*  research which is about how to most effectively use computation to help
*  human beings make decisions and so we call these cognitive prostheses sort of
*  by analogy to you know the other sort of more physical kinds of prosthesis that
*  we're used to thinking about just as that physical prosthesis might help you
*  to overcome a limitation then a cognitive prosthesis helps you to
*  overcome a cognitive limitation and so the the basic idea here is if the
*  limitation is that we have you know finite compute then let's think about
*  how we can introduce more compute but one thing we can do is we can stick a
*  chip in your head that might be something that might work at some point
*  people are certainly trying that but another strategy is instead of putting
*  the compute inside the agent we put the compute inside the environment and so
*  you can think about that as you know instead of modifying what the agent is
*  doing we're going to modify the environment such that when the agent
*  does what the best that they can do with the resources that they have they're
*  nonetheless going to end up doing something which is smarter as a
*  consequence of the environment in which they're making that decision. So how do
*  you change the environment? So the way you do that is by changing either the
*  information that you're providing to people or the way in which people are
*  rewarded for the actions that they take. So an example of this is to say that
*  people have a limited planning horizon right so that means that in a situation
*  where there's some outcome which is a desirable outcome there might be you
*  know ten actions in the future if you're only able to plan four actions into the
*  future you're never going to realize that long-term outcome right and so we
*  know the structure of the problem we know what the optimal solution is but
*  being able to get to that optimal solution requires you having this you
*  know ten step planning horizon and the humans are only capable of doing four
*  steps. You can think about probably lots of problems that have structure like
*  that I think the most provocative ones are things like climate change right
*  where you know you have this very big long-term cost but you also have a lot
*  of very salient short-term costs right and so the question is like how do you
*  trade off these short-term costs against the long-term costs or another perhaps
*  more immediate example is procrastination right which has a classic
*  structure where there's something you need to do in order to get to the point
*  you know when you do that thing you're going to get a big reward but in order
*  to get to the point where you've done it you need to do a bunch of smaller things
*  each of which is slightly aversive to get you there right and so there's a
*  kind of motivational problem around that of like getting through all of the
*  aversive stuff to get to the point where you get the big reward at the end.
*  Slightly aversive. And so the way that we engage with that is by saying well let's
*  formalize those problems you can think about them as sequential decision
*  problems so we can we can express them using a mathematical framework called
*  Markov decision processes which means basically a process where at each point
*  you're choosing an action to take and you're getting a reward for that action
*  and then that action is moving you forward you know so you're sort of going
*  through a sequence of states of the world as a consequence of those actions
*  and so then we can ask what's the right way of structuring the reward function
*  for an agent such that that agent is able to solve that problem even if they
*  have a limited capacity of plan into the future and so it turns out that this
*  question again has been studied in the artificial intelligence literature so the
*  problem that people have in the AI literature is they want to train
*  reinforcement learning agents so you want to train a robot to play soccer
*  right yep how do you train the robot to play soccer well playing soccer has
*  exactly the structure there's you know some sequence of things you have to do
*  and then if you do exactly the right things you score a goal and you get some
*  reward right but that reward can be potentially a very far you know distance
*  in the future and so people realize okay what we can do this is actually now
*  bouncing back to psychology if you look at the animal training literature then
*  there's this idea of shaping and so a shaping reward is a reward that you give
*  to the agent as it gets sort of closer and closer and closer to the desired
*  behavior so you start out with like you know the first step towards that
*  behavior and you reward that and then you you know stop rewarding that and
*  start rewarding the second step towards the behavior once they're reliably doing
*  the first one and so on and so people in reinforcement learning were like okay
*  we'll just use shaping rewards what we're gonna do then is you know give
*  little rewards to the agents as they're doing things that maybe are getting them
*  closer to scoring that goal yeah but when they started doing that they
*  discovered that there were all sorts of problems with it if you rewarded the
*  things that intuitively kind of seemed to make sense like rewarding the soccer
*  playing agent every time it touched the soccer ball then it would evolve a
*  strategy where it basically like would just stand next to the soccer ball and
*  like
*  and so you have to think really hard about how to structure reward functions
*  and if you look at things like gamification in apps or you know where
*  you sort of you're being given points or rewards by a company for doing things
*  those are exactly introducing a modified reward function in the same kind of way
*  but there's not really a science of it and so what we did is try and figure out
*  you know what's the the right science of doing that by looking at how this
*  problem has been solved in reinforcement learning in AI and basically there's a
*  result that says the optimal form so the setup is you're gonna take your original
*  reward function and then you're going to add to it a second reward function and
*  that second reward function is the thing that you have control over you have to
*  start off with a goal though right you need you have some you have some goal
*  that gives you your original reward function that's like you get you get a
*  payoff you know when you complete the project you're procrastinating or when
*  you score a goal right and then we're gonna add another reward function on top
*  of that so it's kind of like one reward function is reality and then the other
*  reward function is like the game layer that we impose over reality to get you
*  over your own cognitive biases yeah that's right and so the so the there's a
*  result in in the AI literature where which shows that the optimal form for
*  that that what's called a pseudo reward is you you can derive what form that
*  that has and basically what you do is you take the the original description of
*  the problem you're solving this markup decision process you solve it using a
*  computer so that what you're doing is for every state in that system you're
*  working out how valuable is it to be in that state so as you're getting closer
*  to the goal it's more valuable because you're getting closer to the chance to
*  score right yep and then you make the that additive pseudo reward reflect the
*  value of that state so that when you're moving from state to state the additional
*  reward you get is based on the difference between the values of the
*  two states so as you move from one state to another from a lower value state to a
*  higher value state you get a positive reward you move from a high value state
*  to a lower value state then you you know lose some reward and so then the agent
*  is motivated to follow a trajectory where they're gonna now be moving from
*  you know towards states of higher value and so we can then take that analysis
*  and then think about it back in our sort of cognitive prosthesis setting it says
*  take the problem you want to tell you solve someone tells you what their
*  long-term goals are you formulate what the reward structure of that problem is
*  and then we pass that off to the computer the computer solves that problem
*  and works out okay what's the value of each of these states assuming that
*  you're following the optimal policy the optimal strategy for getting towards your
*  goal and then we take those values and we feed those back as pseudo rewards to
*  people like you get stars or points or maybe even we take the big payoff you're
*  gonna get and we spread it back so you get incremental dollars as you get
*  closer to what's your goal you missed the brain surgery step where the chip is
*  implanted you don't need a chip right because this is just about the
*  environment right so so it's just saying okay you know as you as you get each
*  step so you could do this for yourself right so if you're procrastinating yep
*  you can say okay if I turn in this writing assignment I'm gonna get like a
*  right but I have to spend you know ten painful hours to get there and so what
*  you do is you take that big reward at the end and you divide it up and you
*  spread it back through time so that after the first hour you get you know
*  like five dollars and then after the next hour you get seven dollars and after
*  the next hour you get nine dollars and so you have not not only you have a
*  reward for each action you're taking but you also have like sort of increasing
*  rewards over time in a way that's gonna keep you motivated to do it just just
*  like in a real game right so if you think about like how you get hooked on
*  addictive games part of it is that the rewards that you're getting are not only
*  it's not you're just getting a constant rate of reward is that you're getting an
*  increasing rate of reward and that turns out to be the optimal structure for
*  something where you have like a big payoff at the end and then you call this
*  optimal gamification yep is there and so okay I'm trying to imagine a scenario
*  you know like I have my goal right of whatever make writing the next great
*  American novel or something and so then I would sort of somehow submit that to a
*  computer and then I would submit myself to its reward structure in the
*  environment and then I'd have to agree to kind of like go along that reward
*  structure right that I mean you know you can just like jump to so many
*  conclusions here because it sounds well it sounds harmless right but is there
*  value so one of the trade-offs I suppose in doing that is you are
*  potentially reducing your exposure to randomness which could contribute to the
*  creative process right so I mean you're potentially reducing any sort of
*  creativity that might arise right you told me your reward structure was you
*  want to get it done another cognitive limitation is we don't maybe understand
*  our own goals as well as we would like to right so yeah you know so I'm just
*  wondering if there's value in exercising some randomness you know in the
*  algorithms to live by book as well you guys have a chapter on randomness as an
*  algorithm for creativity so I'm wondering how that relates you know yes
*  so far I can't help you with self-insight so we assume that you have
*  you have pretty good self-insight and you're able to say what your goals are
*  and then we can help you achieve those goals as a consequence of doing that you
*  might discover that you had different goals it's a pretty common experience
*  right right actually what I want to write is just one paragraph not not
*  American novel yeah but a really good version of that yeah yeah so the yeah I
*  mean I think I think you can think about how you could modify that I think the
*  main thing that I think isn't nice about this from a cognitive perspective is
*  that it gives you guidance but it also gives you agency so it's kind of setting
*  things up in such a way that you accurately know what the cost of not
*  doing that thing is and so I think that's a big problem if you want to do a
*  big project right it's really hard to do the things which are important but not
*  urgent right like though that's the category of things that in everybody's
*  life kind of hangs over them yeah and this is a way of being able to say that
*  which is you know okay like you can now say here was this unit of time that
*  you're going to spend on that thing which is important but not urgent by not
*  spending that unit of time on that then you're giving up this future reward
*  right like this this amount of that future reward and so it allows you to
*  quantify that in a way that means that you can make more intelligent decisions
*  about maybe what your goals actually are and trade off the short-term and
*  long-term consequences of those they may even prevent people helpfully prevent
*  people from starting to go down a road that they may actually not want to go
*  down right yeah yeah do not go into grad school or you know things like that yeah
*  if you if you're able to it might help you to accurately work out if you if you
*  can accurately work out what you think the payoff of that would be then you can
*  discover that in fact even the first step in that direction is not worth more
*  than the the the other rewards that you can get from yeah all of the other
*  things that you could be doing yeah if I had only known that so right now you
*  guys have done experiments using you develop like an app for this optimal
*  gamification what's next so the experiments we did so far we're looking
*  at doing things like helping people not procrastinate and so we ran some online
*  experiments which which showed that you can get people to complete writing
*  assignments at a higher rate these were also just devious experiments where we
*  asked people you know over an extended period complete these writing
*  assignments and then on the interface where you had to do the writing
*  assignment it also had like a header which showed you like the top headlines
*  on reddit and things like that so it was like built in built-in procrastination
*  attractor so the things we're currently working on and Falck is really taking
*  the lead on this is extending this to to-do lists right so in exactly the way
*  that we were talking about being able to help people to figure out you know how
*  to trade off short-term and long-term goals that they might have expressed and
*  in the form of a to-do list you're gonna be a rich man there's like a billion
*  dollar you know industry in self-help these very things so you'll get to
*  retire early perhaps so Tom we have one of the things I want to talk about but
*  I'm just going to gloss over and I'll point people to it in the show notes is
*  this work that you've done comparing deep neural networks with psychological
*  representations and so there's been this big recent push in the literature just
*  at the at the neuroscience level comparing deep neural network
*  representations to biological neural network representations and and what
*  you've done is started to compare these things to psychological representations
*  so because of time we won't really get into it but it's really interesting work
*  and of course you're doing what you ever think about slowing down your
*  publication rate well I have to think about how to reconcile my short-term and
*  long-term goals no I mean I think the all of that reflects the fact that I
*  have pretty broad interests and have the opportunity to pursue those in parallel
*  and so in parallel with all of the things that we've been talking about as
*  I as I mentioned earlier one one of the things that I'm really preoccupied by is
*  thinking about how to do psychology differently now that we have access to
*  way more data on human behavior oh yeah and you know that data takes different
*  forms I think every technology company at this point has more data on human
*  behavior than the entire history of academic psychology but also you know we
*  can generate new data pretty efficiently using methods like crowdsourcing which
*  is essentially a mechanism for turning dollars into data and that was the thing
*  that didn't exist before and I think we're just starting to see the
*  ramifications of that for the field like at this point mostly people are still
*  taking things they would have run in the lab and then running them faster on
*  mechanical Turk or something like that but I think there's a qualitative
*  transformation that is yet to happen in terms of just realizing no because we
*  can get so much data there are different kinds of studies we can run different
*  kinds of questions we can ask and just different things that we can be doing as
*  cognitive scientists for understanding how human minds work and so I have a
*  whole research enterprise which is based around that where we do things like we've
*  built software for running what we call society scale behavioral simulations
*  where we have people interacting online groups of you know up to a hundred
*  people solving problems looking at how information changes as it's transmitted
*  between people looking at social dynamics those are things that we're
*  able to do as a consequence of that scale we have research which is about
*  just collecting really large-scale experimental data sets where we're using
*  this perspective to allow us to run kinds of designs that we wouldn't run
*  before where we just randomly explore the space of stimuli and that gives us a
*  much richer picture of what's going on in human behavior but we're also engaged
*  in an enterprise of thinking about okay because we had limited amounts of data
*  when we were trying to answer questions in the lab we had to use these very
*  simple kinds of artificial stimuli right like if you wanted to study
*  something like categorization you use a circle with a line through it and you
*  change the size of the circle and the angle of the line yeah and those are the
*  two dimensions of your stimulus and you could get control over it and get enough
*  data that you could resolve things at that scale but if you can get orders of
*  magnitude more data then maybe we can actually take on the challenge of
*  working with more naturalistic kinds of stimuli and so I work on deep neural
*  networks is motivated partly by that so the big problem that you run into is how
*  are you going to represent naturalistic stimuli in a way that you can use things
*  like computational models of cognition to make sense of people's behavior and
*  so in a lot of domains the best models we have of those complex stimuli are
*  things like different kinds of deep neural networks and so step one was
*  let's see if we can actually build good models of human similarity judgments for
*  images by taking representations from those deep networks and so that's the
*  paper that you described looks at that and the answer is they do a surprisingly
*  good job yeah it turns out that there are things that are systematically
*  missing from them but there are things that it makes sense and we can think
*  about ways of mitigating that and then there are ways that we can adjust those
*  representations to bring them into closer alignment with human
*  representations and then step two which is something that we're just wrapping up
*  we have a paper that's on archive but isn't published yet where we show that we
*  can use those representations to predict human categorization judgments so we
*  collected a data set which is the entire test set of CIFAR-10 so it's 10,000
*  natural images classified into 10 categories and then we fit standard
*  psychological models of categorization like prototype and exemplar models to
*  those data we collected 50 human judgments for every one of those 10,000
*  images so we have this as I said large-scale data set and we fit
*  categorization models to those data and that gives us models that you know do a
*  good job of predicting human categorizations of natural images and
*  engage with some of the theoretical debates that have been held in psychology
*  about you know which which kind of models are the best models for making
*  sense of human categorization.
*  Yeah you do have a broad interest of it when you visit your website you're running well
*  you I guess you've been out of rainbow colors but you color coordinate your
*  your research topics but and then there's like I don't know six hundred
*  colors to go through on the on the website but it's nice you can click on
*  one and then see oh these are all the decision-making papers etc.
*  Yeah so part of that is my advising philosophy so my goal is for every one of my students to
*  look completely different from one another.
*  Oh wow why is that a strategy why is that a?
*  It's it's it's because like I think you see a lot of labs where every person who
*  comes out of that lab looks exactly like the PI.
*  Well see I was thinking about that with you and Josh Tenenbaum because you've
*  really taken your own route here so yeah it's impressive so.
*  Yeah it's and that's that's I mean I think Josh did a you know as we work
*  together I had lots of opportunities to explore the directions that I was
*  excited about and take things and you know I think a lot of our joint work
*  reflects the flavor of both of our interests and then those have diverged
*  in some places and continued to be together or reconverged to different
*  points but no I mean my goal is I want every graduate student to be able to do
*  things that nobody else can do and and have their own unique research identity.
*  That also fosters sort of collaboration in the future as well I would imagine.
*  Yeah yeah and so I do a lot of work with my students about kind of figuring out
*  what those trajectories look like but as a consequence I have as many different
*  research directions as I have students and that works okay for me because
*  there's a thing that unifies all of those which is this kind of theoretical
*  framework that we've been talking about of you know a particular way of looking
*  at computational problems that human minds have to solve and using that toolbox
*  to make sense of all of these different kinds of things that human beings do and
*  so for most of my students there's going to be a particular area that they're
*  interested in using that toolbox to make sense of and then that translates into
*  you know all of these different kinds of projects that we engage in.
*  What's the wait list like on getting into your lab?
*  At the moment I'm not taking students this year.
*  So we have just a few minutes left here I kind of want to open it up broadly if
*  that's okay. A lot of guests I've had on the show and a lot of people have
*  expressed this idea that there is will not be a grand unified theory of the
*  brain and what we've been talking about is a framework and approach the resource
*  rational framework but so could there be a grand unified framework?
*  I don't think that's gonna work right for the reason that...
*  Do you also do you agree that there won't be a grand unified theory of the brain?
*  So I think that we're gonna be able to identify principles that are productive
*  principles for thinking about human intelligence right so I don't think it's
*  gonna be the case that there's gonna be you know a set of axioms from which you
*  can derive every aspect of how it is that brains work but I think that what
*  we're gonna be able to do and are in the process of doing is more generally like
*  lay out some of the axes along which varieties of intelligence differ and
*  then be able to situate human intelligence along those axes and
*  understand you know what the characteristics are that are the
*  characteristics of human intelligence in a way that translates into insight into
*  how the cognitive processes and the neural processes are involved in
*  supporting that so I think that's a realistic kind of goal so I don't think
*  there's gonna be one way that we get there so when I talk about Mars levels
*  of analysis I really talk about it you know when I when I teach it I talk about
*  it as a choice right it's like these are all different kinds of questions that we
*  can ask about our minds and brains work and as a scientist we're engaged in a
*  gamble where the stakes are our time and payoffs our discovery and we're all
*  making choices about where we're gonna put our chips right like and so you know
*  some people are making the gamble that studying neurons and building up from
*  neurons is gonna be the way that we're gonna make the most progress some people
*  are making the gamble that operating at that level of algorithms and and sort of
*  trying to understand cognitive processes is the right way to make progress you
*  know between these levels of analysis some people that computational levels
*  where we're gonna get our most biggest insights right and I think ultimately all
*  of those levels of analysis have something to contribute and developing
*  ways that we can pursue those enterprises more synergistically is
*  something that's gonna help us to make progress on solving all of those
*  different problems and so so I think that's the why I see a lot of value in
*  bridging levels of analysis because it's a way that we can say okay here's this
*  idea that's been proposed over here here's this idea that's been proposed
*  over here now let's ask are these incompatible with one another are they
*  special cases of one another are they a way to think about implementing this
*  thing with that thing the more connections like that you can make the
*  more insights at one of those levels of analysis translate back to another level
*  right and so we start to populate that whole picture much more efficiently it's
*  sort of in the same vein so you have this I mean this is not Mars levels but
*  you have you know like the neuroscience approach cognitive science approach and
*  artificial intelligence approach to intelligence but one of the problems is
*  is potential problems is that all these different fields are working on different
*  problems different tasks different you know they have different different
*  approaches so like AI they're so they're they're solving Atari games for instance
*  you know and other things and and that's not what neurophysiology experiments
*  seek to understand for instance right so you know are the scope of neuroscience
*  problems just too damn boring for AI people to approach to try to solve or you
*  know is there a way for us to come together and try to solve similar
*  problems so that we can bridge the biological and artificial intelligence
*  worlds yeah I mean I think to some extent that happens I was on a neuroscience
*  students committee and suggested that they run some Atari
*  well yeah yeah what in there in their monkeys this was in humans but it was a
*  is a large-scale like developmental like multifactor sort of you know data set
*  and I said hey just just throw this in you know we might not be able to make
*  sense of it now but it's probably gonna be useful yeah yeah okay so I mean I
*  think there are ways of doing that I mean to me the the big thing that I think
*  about is like data right like a lot of what's gonna get us there is being able
*  to collect data on scales that allow us to have theories that are of appropriate
*  complexity that they allow us to make those connections so doing these studies
*  where we've just been collecting very large amounts of data has helped to
*  convince me of that where often we'd go into those studies being like is it this
*  theory or is it this theory let's run a study and we'll definitively figure it
*  out and then the answer is it's neither of those it's way more complicated yeah
*  and people hadn't had the kind of data that they need in order to get that
*  insight before right and so I think in order to be able to do things like work
*  with stimuli that are of equivalent levels of complexity across all of those
*  domains then being able to increase our bandwidth is something that's going to
*  be important to be able to make sense of what's going on with those stimuli we
*  haven't talked about data on the mind so I will introduce it in the introduction
*  and and point to it there finally Tom what is something that you used to
*  believe that you think is naive now hmm well I don't know if it's naive but I
*  mean I think I've had a personal evolution just along this axis of
*  rational models to bounded optimality I don't know what goes beyond that I'm on
*  that trajectory which is you know really thinking that this notion of
*  constraint plays just as an important role in understanding human cognition is
*  the notion of optimization that's a great answer I've really enjoyed you know
*  reading a bunch of your work and and thinking in in the bounded optimality way
*  is it's really broadened my horizon so I I appreciate it and thanks for being
*  with me on the show thank you very much
*  brain inspired is a production of me and you you can support the show through
*  patreon for a microscopic two or four dollars per month go to brain inspired
*  co and find the red patreon button there your contribution will help sustain and
*  improve the show and prohibit any annoying advertisements like you hear
*  on other shows to get in touch with me email Paul at brain inspired co the
*  music you hear is by the new year find them at the new year dotnet thanks for
*  your support see you next time
*  oh
*  you trust the sky
*  light your lives
*  you

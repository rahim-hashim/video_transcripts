---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4740s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 30623
Video Rating: None
---

# BI 123 Irina Rish: Continual Learning
**Brain Inspired:** [January 02, 2022](https://www.youtube.com/watch?v=jlmqxoZTX5Y)
*  We are not the first one asking the question about what intelligence is.
*  People think they're the first one to ask the question or to build something or to attempt
*  something and it's not the first time to put it mildly.
*  It's always a trade-off.
*  Capacity versus complexity.
*  When you want to find the minimum cost, the minimum capacity agent that's capable to
*  conquer the complexity of whatever future tasks that agent will be exposed to.
*  But if the agent hits the wall, the agent will have to have the ability to expand itself
*  and continue learning.
*  What I've learned from two years trying to do the new AI project IBM, that it was, first
*  of all, much less well defined than AI for Neura.
*  Here you like search for a black cat in the black room and you're not sure if the cat
*  is there.
*  That's Neura for AI.
*  This is Brain Inspired.
*  Hey everyone, it's Paul.
*  Happy holidays.
*  I hope you're well.
*  Today, I speak with Irina Risch, who is currently at the University of Montreal and also a faculty
*  member at Miele Quebec AI Institute.
*  I wanted to have Irina on for multiple reasons, one of which is her interesting history having
*  been kind of on both sides of the AI and neuroscience coin.
*  She's also worked at IBM, as you'll hear, working on healthcare and also neuroscience
*  inspired AI.
*  We have a pretty wide ranging conversation about much of her previous and current work.
*  We talk about her work on alternatives to the back propagation algorithm and we talk
*  about her ongoing work on continual learning, which is kind of a big topic in AI these days.
*  As you probably know, deep learning models suffer from what's called catastrophic forgetting,
*  where when you train the model to do one thing really well and then you train it to do another
*  thing, it forgets the first thing.
*  Humans don't suffer from this problem and it's an important problem to tackle moving
*  forward in deep learning.
*  We discuss many of the methods being used to try to solve continual learning and some
*  of the inspirations from neuroscience along those lines.
*  We also talk a little bit about scaling laws, which is roughly the relationship between
*  how big and complex a model is and how well it performs over a range of tasks.
*  We also talk about definitions and Irina's definition of artificial general intelligence
*  and how she views the relationship between AGI and continual learning.
*  We talk about a lot more.
*  You can learn more about Irina in the show notes at braininspired.co.au slash podcast
*  slash 123.
*  You can also learn about how to support the show on Patreon and possibly join the Discord
*  community of Patreon supporters who are awesome.
*  Thank you guys and thank you for listening.
*  Enjoy.
*  You're actually kind of a perfect fit for this podcast because on the one hand, you
*  have a background in a lot of computer science and I guess your early work was in applied
*  mathematics.
*  You kind of come from that side, but I know that you're interested in using, among other
*  things, among the many things that you're interested in, in using some principles and
*  ideas in neuroscience to help build better AI.
*  So could you just talk a little bit about your background and how you came to be interested
*  in being inspired by brain facts and etc.
*  Yeah, that's a very interesting question indeed.
*  Sometimes I ask myself and I try to dig into the past.
*  The question is how far in the past I want to go.
*  Indeed a couple of years ago, I joined Miele and the University of Montreal, but before
*  that I was at IBM research and I was there for quite a long time initially in the department
*  of computational biology where I did indeed focus on neuroscience, neuroimaging and applying
*  statistical methods, machine learning, AI to analysis of brain data.
*  So that's mainly where I kind of really got, I guess, deeper into neuroscience, psychology,
*  psychiatry type of topics.
*  And I'm still collaborating with a group.
*  It's my kind of long-term collaborators in computational psychiatry and neuroimaging,
*  Geshe-Machechi and his friends.
*  So that was really exciting and that's, I guess, where I actively was pursuing this
*  idea of the intersection between AI and neuro.
*  But I think the interest in that intersection started long time before I even joined IBM.
*  And I usually, I realized that I could track it back to my, I think, elementary or even
*  middle school years.
*  I used to go to mass Olympics in Russia.
*  I don't know if it's too long of an answer.
*  Well let me ask you this.
*  So when I was in college there wasn't even a neuroscience program degree and I don't
*  know that I would have been, you know, I started in aerospace engineering and then moved on
*  to molecular biology and I don't know if neuroscience was available as a program, whether I would
*  have actually chosen it.
*  But so I was going to ask if that's what was limiting, if you had that kind of kernel of
*  interest, why then go into applied mathematics?
*  That was your first degree, right?
*  Right.
*  Yeah.
*  I mean, I probably should explain and did what I wanted to mention.
*  The reason was from practical perspective, I was going to mass Olympics and I was quickly
*  realizing that you don't have that much control over your brain and like you want to solve
*  a problem and you're kind of hitting the wall.
*  So what's going on?
*  And sometimes it works, sometimes it doesn't.
*  You want to understand like why and how to make it work better.
*  And then you see people around you, some of them struggling, unable to solve anything.
*  Some of them are able to solve like more than you do.
*  And again, you wonder what the difference, what does it take?
*  Then you start reading books like Poia, How to Solve It, How to Learn How to Solve Problems
*  and this and that.
*  It really came from very practical goal.
*  Like I need to figure out how to solve all those problems quickly because I want to win
*  the Olympics.
*  So what do I do?
*  My brain doesn't seem to be cooperating.
*  So what should I do?
*  Like how do I make it work?
*  So you start digging into how to make brain work and then you run into books accidentally
*  which say, well, whether machines could sing.
*  It was a Russian translation, I guess, of the famous Turing's work.
*  That gets me into thinking about AI when I'm like 14 or something.
*  That's why I go to computer science.
*  The closest to computer science at that point, kind of in Russia, was like applied math,
*  essentially applied math slash computer science, but formally applied math.
*  And that's kind of that's how it goes from there.
*  So like my focus on computer science and AI actually came from the really very practical
*  goal.
*  I understand how this brain works, so I make it work better.
*  That's pretty much it.
*  Then you realize there is psychology, psychiatry, neuroscience, and many other things that study
*  brain like whatever goes.
*  Okay.
*  So at IBM then you were part of a team, I think you said you're in computational biology
*  division.
*  And so you were a part of a team that was sympathetic to using principles from biology
*  to help make machines better, right?
*  Okay, the focus of the department was not on machines.
*  The focus was on health care.
*  So the focus was on how to make humans healthier.
*  That was computational biology, neuroscience, and neuroimaging kind of groups focus.
*  So it's not the focus of that group was not really on AI.
*  And I was kind of back and forth between focus on AI and computer science and machine learning
*  to biology and back.
*  Originally, I started in machine learning group for distributed systems, changed names
*  a few times, then I moved to this computational biology center.
*  And then in the past few years before moving to Miele, I moved again from computational
*  biology department to AI department of IBM.
*  So as I said, I was kind of iterating between the two multiple times.
*  And the focus in those past couple of years before moving to Miele was indeed to bring
*  kind of neuroscience inspirations and ideas to improve AI.
*  So that was my latest focus on IBM was indeed on what you're asking about.
*  And that was new AI kind of project between IBM and MIT that was going on.
*  That kind of remained part of my focus when I joined Miele and was part of the direction
*  for that seven year program that I'm leading the Canada Excellence Research Chair.
*  The new AI component is one of the kind of axis along which things are supposed to be
*  developing.
*  We'll see.
*  Okay, so this is what I wanted to get to because I'm curious about your experience about your
*  colleagues and their sort of opinions about using neuroscience or neuro inspired tools
*  to build better AI because that's very much the industry side of it.
*  And you have a lot of like passionate opinions about whether we should be looking to the
*  brain to build better AI or whether you know, we should just continue to scale with what
*  we have.
*  Right?
*  Right.
*  I know both sides really well.
*  We just ran our scaling laws workshop last week in Trimland.
*  Yes.
*  So what did your IBM colleagues, if you feel free enough to talk about it, what was kind
*  of like their reception of your focus on using neuroscience?
*  Again, the colleagues in AI department or colleagues in the biodefartment.
*  Well, I think actually this whole neuro for AI and AI for neuro, all these ideas actually
*  grew out my multiple interactions and discussions with my friends at computational psychiatry
*  and neuroscience department and primarily Gizher Macieci.
*  And I think what really also helped to shape my views was the interactions which involved
*  not just discussing technical aspects of AI or technical aspects of brain imaging or even
*  neuroscience, but there was lots of philosophy in those discussions because like a legege
*  had first degree in philosophy and the second in physics and then went to neuroscience.
*  And I think that really made him like stay, stay kind of apart and ahead of many colleagues.
*  So I'm really like really, really grateful for those discussions because they helped
*  me to shape my views as well.
*  So what I'm trying to say that while the healthcare department, the comb biodefartment was focused
*  on healthcare applications, the idea of using neuroscience and biology inspirations for
*  improving AI was very exciting for at least several people there.
*  And it's still exciting.
*  And we would like to kind of do more along those lines.
*  When I moved to AI department at IBM, again, it was kind of a mix of opinions because just
*  like in the field in general.
*  And I agree with that view.
*  It may not necessarily be the case that the only path to intelligent artificial intelligence
*  systems is mimicking the brain.
*  Moreover, like even my colleagues, neuroscientists never said that we have to mimic the brain.
*  The tricky question is like, what is the minimum part of those inspirations that might be necessary
*  to transfer?
*  And that's just like Jan Likhan always gives us example about airplanes not flying their
*  wings.
*  Right.
*  So you don't have to copy the biology exactly.
*  And yet you want to come up with some common laws that govern the flight, right?
*  Some aerodynamics of intelligence in our case.
*  And that's a tricky part.
*  And that's, I think, where everyone agrees.
*  So nature found the solution.
*  There are some properties of that solution that might be specific to evolution and nature.
*  And perhaps we can abstract from them.
*  But there are some parts.
*  The question is, which ones that are probably invariant or necessary for any intelligence?
*  Finding those invariant properties is a good open question.
*  And I think that's subconsciously everybody doing AI is trying to do that.
*  But I definitely am not in the camp of first you need to completely understand how brain
*  works and only then you can create artificial intelligence.
*  I don't think so.
*  Just like with airplanes and engineers there, they don't have to be like biologists understanding
*  birds perfectly, right?
*  You need to understand enough.
*  But the good question is, what is enough?
*  Well, it's interesting because we're going to talk about a few of the neural inspirations
*  that you have focused on.
*  In some sense, I don't mean this is not an insult at all, but it's almost like we are
*  sometimes cherry picking and just trying kind of one thing at a time.
*  We think this might be important, think that might be important.
*  What we could do, which you say is not the right path.
*  And I agree, is we could instead of cherry picking these facts that we're going to discuss
*  in a little bit, you really could go more all in and try to, you know, there are people
*  trying to quote unquote build a brain, right?
*  And they're still having to abstract out a lot of things.
*  But that push would be to build in more that we know about the brain rather than less,
*  it seems.
*  But I want to ask you before we move on about philosophy.
*  I happened to see a panel that you were on.
*  I don't remember the source.
*  It may have been the main conference.
*  Yeah, yeah, yeah.
*  Oh, we had an interesting discussion about philosophy there.
*  Well, it didn't go that that far.
*  But you got into a back and forth a little bit with Surya Ganguly, who finds philosophy
*  useless and you made the push that in fact it is useful.
*  So I just wanted to say you're useless.
*  You can learn from anything.
*  But let's not go there.
*  Okay, okay.
*  So you don't want to make a case for philosophy.
*  I can make a case for philosophy.
*  Let's hear it.
*  I think what happened there, maybe it was as usual, by the way, it's not specific to
*  that panel.
*  People mainly disagree because of differences in their definitions of interpretations of
*  terminology.
*  And unfortunately, that's a universal problem in the field.
*  Like many concepts are not well defined and in general.
*  That's the main reason people argue because when people actually nail down details of
*  what they're arguing for or against, surprisingly, in many cases, they all agree.
*  So I think the problem was what people understood as philosophy.
*  When I say the word philosophy and it means something to me, it probably meant different
*  things to different people.
*  So they were really arguing not with my point, but they were arguing with their own understanding
*  of the world.
*  That's why because I don't think Surya or anyone else will disagree in general that
*  If you have different disciplines, whether it's philosophy or neuroscience or psychology
*  or psychiatry or any type of discipline that studied mind and its function, how it works
*  and what are the mechanisms at different levels in different ways.
*  And philosophy is one of them.
*  And even more, not just philosophy, I mean, you can think about Buddhism and I brought
*  this example.
*  To me, it's empirical science of how mind works, which has several thousand years of
*  knowledge accumulated in very different terminology and so on.
*  But that's a data, that's knowledge accumulated by people from observations.
*  So there is some truth to it.
*  And the question is like, how to dig that truth out since we're coming from different
*  terminology again, how do you translate philosophy and Buddhism to machine learning slang in
*  a sense so people will understand it.
*  Not everything there might be relevant, but we are not the first one asking the question
*  about what intelligence is.
*  What usually amazes me, again, I don't mean it as insult, but and plus it's very natural,
*  it always happens, but people think there's a first one to ask the question or to build
*  something or attempt something.
*  And it's not the first time to put it mildly.
*  There are many bright minds that for many years were facing similar type of questions
*  just in different circumstance.
*  So I think it might be useful to learn more about what they found.
*  It does seem to be a recurring theme that there'll be a hot new trend.
*  And then it turns out 100 years ago, someone already had written basically the answer,
*  and laid out the groundwork for it.
*  That then we go back and something that we resolved had already essentially been solved.
*  It is, I mean, it's nothing specific to our field or our time.
*  It's always been like that.
*  It's probably always going to be like that.
*  But that's just why I mentioned philosophy.
*  And also, I mean, I know, I know, I essentially meant the same thing that Surya was saying
*  himself, that we are trying to kind of discover the common laws behind intelligence, whether
*  biological or artificial, and kind of pushing it forward, common laws behind how mind works
*  or how it could work, and how you can kind of affect it in different ways so it works differently.
*  And I think any source of knowledge about like people asking similar type of questions
*  and finding whatever answers, any information like that, you can learn from all this data.
*  All I actually was suggesting that, yeah, let's try to learn from all data,
*  quote unquote data being different disciplines.
*  But okay, so there's a problem here, right, where throughout the years, all the different
*  disciplines have continued to progress, and it is essentially impossible to be an expert in all disciplines.
*  So how, you know, what's the right...
*  That's why we need AGI.
*  It will be an expert in all of them.
*  And they can tell us which disciplines we need to learn, but we won't need to learn any disciplines.
*  It will extract the knowledge for us and convey it to us in an understandable manner.
*  I'm just quoting Ted Chiang's short sci-fi story from Nature.
*  But it's only half-joking.
*  Yeah, yeah.
*  Well, so you are interested in...
*  That's a goal, to build AGI.
*  And we're going to talk about lifelong learning in a little bit.
*  I want to ask you about backpropagation first.
*  But would you say that's one of your goals?
*  Yes and no.
*  AGI is not the final goal itself.
*  It's an instrumental goal.
*  The final goal, as I was always putting, AI as augmented rather than artificial intelligence.
*  To me, just the goal of building AGI never felt truly motivating.
*  Why do I care about machines?
*  Well, do you know what AGI even is?
*  I don't really know what AGI is because that's another thing where people have different definitions and viewpoints.
*  Yes.
*  It's one of those terms in machine learning, which is not well defined.
*  And I know that creates lots of confusion.
*  And we recently had two debates in the Miele on the topic of AGI.
*  There are different definitions and different people, again, mean different things.
*  One practical definition could be just stick to the words.
*  It says artificial, general intelligence.
*  So general means capable of solving multiple, really multiple problems.
*  To me, that means general broad versatile, which relates to continual learning or meta-learning or transfer learning, but kind of pushed to extremes.
*  So like truly versatile AI that can do well, at least pretty much anything we can do, not a narrow opposite of narrow broad general.
*  So that can be just a relatively clear definition, at least to me, of what AGI could stand for.
*  There are many other definitions and we probably could write a list of different ones.
*  But I think you're absolutely right.
*  It's not the term.
*  It's not a mathematical term.
*  Yeah.
*  Do definitions matter?
*  Definitions matter.
*  I mean, yes and no again.
*  So you can have different definitions.
*  What matters is for people before they start kind of working together on something or discussing something to agree on definitions.
*  Because again, the main reason for debates, sometimes unending debates, is at the core that people did not agree on definitions.
*  And what comes to my mind whenever I listen to machine learning people debating something or pretty much anyone debating anything,
*  the picture of that elephant and seven blind men touching different parts of the elephant and saying, no, elephant is this.
*  No, you're wrong.
*  Elephant is that.
*  No, it's you're wrong.
*  And they're all right.
*  And nobody is wrong.
*  But they didn't agree on definitions and they don't see the full picture.
*  That's all.
*  I've come to think that the purpose of debates is to talk past one another and not progress at all.
*  Well, that's not the purpose to me.
*  It's a sad reality.
*  Yeah, you can do that.
*  You will probably have some fun, maybe for some limited amount of time.
*  And then pretty much you just wasted the time and everybody moved on.
*  So what was the point?
*  I don't know.
*  We're agreement.
*  We're not debating that.
*  Yes, if you try to learn something or converge to something or make some progress, then probably not.
*  OK, so you and I agree.
*  That's good.
*  We don't need to debate that issue then.
*  OK.
*  So you've done work.
*  One of the ways that you have thought to use neuroscience is on the question of backpropagation.
*  And maybe before, because you've done work on what's called auxiliary variables, like a backpropagation alternative.
*  So I'd like you to describe that and where that came from.
*  But before doing that, because we've talked about backpropagation multiple times now on the podcast.
*  I had Blake Richards on way back when he uses the morphology of neurons and the electrically decoupled
*  uncoupled apical dendrites and blah, blah, blah, burst firing, etc.
*  As an alternative.
*  And now, you know, there's this huge family now of alternatives to backpropagation.
*  Yes.
*  I'm curious about your overall view on that progress, that literature.
*  Yes.
*  Yeah, that's a very good question.
*  And actually, in fact, we are working right now with a group of people at Miele and outside of Miele on extending
*  difference target propagation.
*  So basically, that line of work is still going on, although it was a bit of a backburner for a while.
*  OK.
*  And there are, as usual, at least two motivations here, whether you come from neuroscience and you try to come up with a good model of how essentially learning happens in the brain.
*  Basically, how the credit assignment for mistakes happens in the brain and whether backpropagation is a good model for that, or you can come up with a better model.
*  So this is one motivation.
*  And many people who kind of are less concerned with competitive performance of alternatives to backpropagation and more concerned with really understanding how it works in the brain, they focus on that.
*  And I also totally agree with that view.
*  As I said, I mean, there is no contradiction.
*  Once you clearly state what your objective is, you cannot say that they are wrong or you are right or vice versa, because they just optimizing different objective function.
*  They want to answer the question, how we best model what happens in the brain.
*  Their objective is not to beat you on MNIST and CIFAR.
*  As long as we all agree on what objective is, it's not wrong.
*  It's an interesting line of research, and that's kind of initially what motivated also work on beyond backprop, kind of just trying to understand things better.
*  And Blake is definitely doing lots of things in this direction and other people.
*  But on the other hand, there is another objective.
*  Like if you come from the point of view of AI person who says, OK, I understand, I want my analogies with brain if and only if it helps me build more effective, more efficient algorithm.
*  So when you come from that objective, you can start wondering purely computationally what are limitations of backpropagation and what could you do differently or better and how to solve those kind of shortcomings.
*  And usually people were always claiming that, yeah, there is problem of vanishing gradients, exploding gradients.
*  Yeah, there is a problem that basically backpropagation is inherently sequential because you have to compute this chain of gradients and you have to do it sequentially.
*  But again, one hand in brain processing is purely parallel.
*  Second, in computers, if we were able to do it in parallel, it probably would have been more efficient and better, would scale better as well.
*  So you want this parallelism, you want to avoid possible gradient issues.
*  So what do you do?
*  And that's where many optimization techniques came, starting from this.
*  Essentially, Yanli Khan's own thesis mentioned alternative to backpropagation that later was called target propagation.
*  And all it meant is another view of the problem.
*  So basically, instead of just optimizing the objective of the neural net with respect to the weights of the neural net being unknown variables you're trying to find,
*  you introduce auxiliary variables that are different names.
*  It all comes from the just trivial kind of equality constraint there that those activations or hidden units,
*  they are equal to what?
*  To that linear function of previous layer transformed by some nonlinearity.
*  And you can play with that. You can introduce extra auxiliary variables, just the linear ones and another one, another set, nonlinear transformation of those, so on and so forth.
*  You can write it purely as a constrained optimization problem.
*  You can modify constrained optimization into just like this Lagrange and whatever.
*  So Yan mentioned that in the thesis and kind of was looking into that later.
*  So it's not something that was not kind of considered before.
*  It's just people didn't really try to push directly optimization algorithms that would take into account those auxiliary variables explicitly.
*  And to me, the work from 2014 was the AI stats paper.
*  I'm forgetting the name right now.
*  I mean, that basically motivated us to start looking into auxiliary variable approaches.
*  And then there was a whole wave of this optimization approaches.
*  Anyway, so they all tried to do the same thing.
*  They tried to introduce activations or linear pre-activations as explicit variables to optimize for that would reformulate your objective function for neural net learning in terms of two sets of variables.
*  One being your usual waves and the second being those activations.
*  And that had some pluses and minuses as everything.
*  The pluses would be that once you fix activations, it completely decouples the problem into local layerwise subproblems.
*  So you can solve for those waves completely in parallel.
*  Basically, the chain of gradients is broken and it's good.
*  So you don't have, by definition, any vanishing gradients or exploding gradients because there is no chain.
*  And second thing, you can do things in parallel.
*  So those two things are good.
*  There is also some similarity and more kind of biological plausibility because you take into account now activations in this neural net explicitly as variables.
*  And essentially interpretation of that is also view them as a noisy activations, which they are unlike classical neural nets where they always deterministic variables, deterministic functions.
*  In real neurons, they're noisy.
*  Real neurons are not fully deterministic functions.
*  Right. I thought they were relu's.
*  Right. Yeah.
*  So nonlinearity is a separate thing, but even just the fact that in artificial neural net, they're totally deterministic, that's also quite a kind of simplification.
*  So there are other kind of, I mean, there are other flavors of this auxiliary variables and kind of target propagation methods in our kind of approach,
*  which is essentially in line of the auxiliary variable optimizations where you can write the joint objective in terms of activations and weights.
*  The thing here is we still use the same weights for kind of forward propagation or basically computing output given input as well as for the optimization or in a sense like backward pass.
*  There are other flavors like target propagation by Jan Lekhan and difference target propagation by Josho and his students and all flavors of methods on top of that.
*  They use two sets of weights, the forward weights and backward weights, which may be even more biologically plausible than those auxiliary methods that I mentioned.
*  And then there is lots of kind of flavors and variations on that.
*  And actually, it's nice to see this subfield expanding recently.
*  And there were some papers at New Reaps last year and so on, so forth.
*  So it's all interesting. It has its pluses and those things such as parallelization.
*  And by definition, lack of vanishing gradients and exploding gradients, no matter how deep the network is or how long is a sequence in a recurrent network or STM or something.
*  Those are good. But you move into different optimization space.
*  And empirically, whenever you try these methods on standard benchmarks and standard architectures, they are not always performing as well as a classical back propagation.
*  And that was one of the issues with the whole field of alternatives to backprop, how to make them competitive.
*  There are multiple successes, but they're not like completely kind of putting backprop out of the picture.
*  Plus, we didn't aim to do so. We had some successes on fully connected architectures.
*  We had successes on CIFAR and MNIST. We had some successes even on RNNs and even on simple coordinates.
*  But what we learned, I mean, that was good because it was the first time when you actually do see those improvements in the paper at New Reaps by Sergei Bartunov.
*  Yeah, and Jeff Hinton and others, they also kind of were trying different alternatives like target prop and variances of that.
*  And unfortunately, they couldn't show that it would beat or be comparable with standard backprop on, say, ImageNet.
*  So there were this kind of many unsuccessful attempts.
*  There were some limited successes. And the question is still open whether such alternatives can become true state of art.
*  And the hunch is, I think you shouldn't beat your head against the wall trying to use alternative optimizations like that on architectures like ConvNets and so on,
*  which were so well optimized to work with standard backprop. You need different architectures.
*  And maybe the fact that we really tried hard to beat backprop on classical ResNets and it didn't really work.
*  Maybe that's a problem. ResNets go well with backprop.
*  Something else will go well with auxiliary variables and target prop.
*  It's a hypothesis, but I think it's kind of something to try.
*  Anyway, I think if you make those methods work, you will get benefits of much better parallelization and scalability.
*  You will not have these nagging issues of potentially exploiting or vanishing gradients, but you will have other problems.
*  You will possibly have convergence problems and alternating minimization type of algorithms and so on and so forth.
*  I mean, there is no free lunch.
*  Since you mentioned architectures, I want to pause and ask you if you think looking to the brain for architectural inspiration makes any sense at all or, you know,
*  because it's a whole system with lots of different architectures interacting.
*  And if you're thinking like different optimization methods might work better or worse with different architectures, if that is another avenue where we should look.
*  I think it would be useful to explore it again.
*  There is this
*  heated debate within the field, inductive biases versus scaling the most generic architectures, say transformers, or even scaling multilayer perceptron.
*  Ultimately, it's a universal function approximator.
*  If you scale it enough, it probably will do anything right.
*  It's probably just not going to scale very efficiently, to put it mildly.
*  So, yeah, that's why maybe transformers are better.
*  But the question.
*  OK, here is the thing.
*  Inductive biases or priors versus scaling very generic type of networks.
*  I might be wrong, my personal opinion, but I think just like historically, whenever you have not enough data,
*  say brain imaging, sometimes it's small data sets or in medical applications, so on and so forth.
*  When you don't have enough data, then using priors or inductive biases from the domain is extremely helpful.
*  They take the role of regularization constraints.
*  And if those regularization constraints or priors or inductive biases are right, they help tremendously.
*  And you can perform really well despite having small amounts of data.
*  And that's where you could kind of use specific architectures and so on.
*  And basically, that's why, say, convolutional networks were so successful for such a long time.
*  But then you start scaling, right?
*  And the amounts of data, if you have those amounts of data, they go way beyond what you had before.
*  Your model size goes way beyond what you had before.
*  You scale the number of parameters while maintaining some kind of structure of the network, like you scale weights and depths and something.
*  There are many kind of important caveats here about how to do it so scaling model will actually capture the amount of information while you scale data.
*  So, I mean, there are smarter ways to do that and less smart ways.
*  But say you do it right.
*  Now, it looks like those priors, inductive biases become less and less important.
*  And we do have empirical evidence, say, visual transformers at scale in terms of data start outperforming conv nets.
*  And by the way, that's why I think looking at scaling laws is so important.
*  You have two competing architectures.
*  You see how they scale and you see that in lower data regime,
*  conv nets are so much better in higher data regime, it's vice versa.
*  And that approach, that kind of empirical evaluation of different methods, architectures or whatever you compare by looking at the whole curve rather than point,
*  that one architecture, another architecture, one data set and other data set, it's not that informative, all those kind of tables.
*  The plots, scaling laws plots are giving you much fuller picture and give you a better idea.
*  Say, if you can't scale, what type of method you should invest into.
*  And apparently, if you can't scale, visual transformers would be better than conv nets.
*  But still question remains, what if there are inductive biases such as maybe those brain architectures and so on that can improve your scaling exponent?
*  Essentially, what it means when we talk about scaling exponent is that empirically,
*  it's found that the performance of models expressed as basically the cross entropy laws on the test data and or loss or classification accuracy on downstream models.
*  They usually seem to improve according to power law.
*  You've seen probably those papers by Jared Kaplan and his colleagues from OpenAI and now, I guess, Entropic and so on and so forth.
*  And all those papers show you power laws, which are straight lines in log-log plot.
*  And the exponent of power log responds to the slope of that line in log-log plot.
*  And the whole billion dollar question in the scaling laws field is what kind of things improve that slope?
*  So you get better improvement in performance for smaller amount of scaling, therefore cheap.
*  And scaling, by the way, involves here not just scaling the data and scaling model size, but also scaling amount of compute,
*  because you may just even keep the model fixed and data fixed, but let your algorithm compute more.
*  And sometimes you see very interesting behavior like grokking paper from workshop at a clear last spring where they just ran the method for a long time, just forgot to kind of kill it.
*  And then there was a sudden phase transition from almost zero to almost one accuracy.
*  They just managed to find some point in the search space.
*  Yeah, well, it was not intentional, apparently, but it happened to be that for that type of benchmark and architectures they used,
*  it was a case that somewhere in the search space, there was a place with extremely good solution surrounded by not so good solutions.
*  And if you find that place, you can jump there and that's your phase transition from zero to one.
*  Anyway, we're kind of trying to explore those phase transitions recently with my colleagues at Miele as well.
*  So back to your question, the question inductive biases versus scaling.
*  As usual, I would say maybe inductive biases plus scaling, because certain inductive biases maybe can improve the exponent.
*  And at least you want to explore that they might be useful.
*  I wouldn't kind of throw the water, I wouldn't throw the baby together with the water, as I say, just saying, OK, let's just scale multilayer perceptron.
*  Yes, of course you can do that.
*  It will be just extremely inefficient.
*  Don't you want more advantageous scaling laws?
*  And maybe inductive biases can help you with that.
*  It doesn't have to begin the two camps fighting each other, although I understand it's more fun to fight than collaborate, probably.
*  It's human nature.
*  It's more fun to do both, right?
*  Just like scaling and inductive biases, the answer is always both.
*  Yeah, it doesn't have to be either or, it could be both.
*  The question is what inductive biases help to improve scaling?
*  And that's a good question.
*  It might be, it depends, like Jared Kaplan was presenting at our workshop a couple of times.
*  We had two workshops so far, one in October, one just now last week.
*  And again, he mentioned that in his experience, again, for that, setting that problem for GPT-3, improvements due to architecture did not seem to be as significant as just kind of scaling.
*  And that's totally fine.
*  It doesn't completely kind of exclude the situation when inductive biases may be for some other problems, would be much more important.
*  How do you explore the full space of architectures, though?
*  You have some limited amount of exploration.
*  Right.
*  Right.
*  That's a good question.
*  I mean, just like with everything neuroscience-inspired, it's such a huge space on its own.
*  And to be completely honest, you cannot just go and ask neuroscientists what, in your opinion, is the most important
*  Right, motif.
*  inductive bias that AI people should use.
*  It doesn't work this way, at least not in my experience, because they say, we don't know.
*  Don't know.
*  Like you tell us what you need.
*  And then maybe we can think and suggest what kind of inductive bias can best help you with what you need.
*  So what I've learned from two years trying to do the Neural AI project at IBM, that it was, first of all, much less well defined than AI for neural, where you take methods to analyze the data.
*  That's we know how to do.
*  Here you like search for a black cat in the black room and you're not sure if the cat is there.
*  That's neural for AI.
*  But I think what helped interaction with those neuroscientists, let's say, look, I need, OK, you're asking what I need for AI.
*  I'd like my system to be able to continually learn.
*  I mean, well, it has to be learning how to do new tasks and work on new data sets.
*  And it should keep doing this because I might have my robot walking in the wild and it has to adapt.
*  Or I might have my personal assistant chatbot and it has to adapt to my changing mental states or it has to adapt to other people.
*  So it will have to keep looking into different data environments, tasks and doing them well.
*  At the same time, I don't want it to completely forget what it learned before because it may have to return to it and may not have to remember.
*  I don't really push for absolute lack of so-called catastrophic forgetting.
*  Fast remembering is fine.
*  So just like basically a few short learning of new things and few short remembering of old things would be just fine.
*  After all, I don't remember myself, the courses I took in the whatever years of my undergrad, but I could remember them, hopefully.
*  So you want that. How does brain do it?
*  And that may be more specific questions.
*  So you say, OK, how does continual learning happen?
*  What are the tricks?
*  And then people are actually using those inspirations.
*  I mean, this whole bunch of continual learning methods were inspired by some phenomena in neuroscience.
*  For example, kind of freezing or slowing down the change of certain weights in the network.
*  If those weights are particularly important for some previous tasks, it was kind of more formalized in work like EWC.
*  Elastic weight consolidation.
*  Or synaptic intelligence also.
*  There are many of those regularization based approaches, essentially in continual learning.
*  And it's kind of one flavor of, well, very abstracted inspirations, I would say.
*  But from this phenomenon that does happen in the brain.
*  Or replay methods.
*  Again, so this classical example of having hippocampus that essentially forms very quickly,
*  kind of memories, but then they're consolidated, say, during sleep and you kind of have this longer term knowledge and prefrontal cortex.
*  So having this complementary learning systems approach.
*  Yeah. Yeah.
*  So that is another example.
*  Again, it's very much simplified and abstracted.
*  It has its roots in neuroscience, but then it kind of gives rise to machine learning algorithms like rehearsal,
*  pseudo-rehearsal, replay, generative replay, so on and so forth.
*  But the idea of, yeah.
*  There is also the third kind of direction that people take usually in continual learning.
*  More like architectural based approaches.
*  When you essentially expand your network model, expand your architecture, depending on the needs of your learner.
*  And that also has its roots in you can connect it to things like adult neurogenesis,
*  that even adult brains apparently do grow new neurons when needed.
*  And they do so in specific places like hippocampus, well, the digeras of hippocampus.
*  It's still happening there.
*  It doesn't stop at the beginning of adulthood.
*  And yes, there was dogma 30 years ago or more that adult brains do not grow new neurons.
*  Well, apparently they do in mammals.
*  In rats, they do it in the hippocampus and olfactory bulb.
*  As you kind of mentioned, olfactory bulb is very important for rats and other mammals because they do use smell quite a bit.
*  And humans, apparently, olfactory bulb doesn't matter as much anymore as in rats.
*  But we still have some neurogenesis happening in hippocampus.
*  And what was interesting, and we kind of did some work on top of that, had a paper about neurogenetic kind of model,
*  although a very simple version of that.
*  But the idea was all the empirical evidence about neurogenesis in the literature suggests that there is more neurogenesis happening
*  when the animal or a human is exposed to radically changing environment, like different tasks or different environments and continual learning.
*  So then it is associated with more neurogenesis.
*  If the environment is not very complex and it's not changing, you kind of don't really seem to need to expand capacity of your model.
*  Like you have some new neurons being born, but they die at a higher rate.
*  So it's like use it or lose it.
*  If you don't need extra capacity, you won't have extra capacity.
*  If you keep challenging yourself and you keep kind of pushing yourself to extremes and totally new situations,
*  then new neurons will be incorporated and your hippocampus will expand somewhat.
*  I mean, to some degree, of course, that's everything.
*  So it's an interesting observation and it's associated with possible ideas of expanding architectures in continual learning
*  to accommodate for new information that cannot be possibly represented well using existing model.
*  So that's...
*  So let me just recap what you've said there, because you covered a lot of ground.
*  So you kind of just transitioned.
*  I was going to ask you about continual lifelong learning and you just transitioned into it.
*  So and you talked about the three neuroscience principles that have been implemented.
*  And the whole point of lifelong learning that there's this huge problem in deep learning called catastrophic forgetting,
*  where once the network is trained on one task, if you train it to learn a new task, it forgets completely forgets the old task.
*  And so there's been this explosion in lifelong learning methods.
*  One of which is continual learning.
*  Is that under the umbrella of lifelong learning?
*  Because there's transfer learning, meta learning, continual learning, and now there's meta continual, continual meta and on and on.
*  Right.
*  OK. Yes. OK.
*  So it's again question of terminology.
*  Like we again kind of stepping on the same rake of machine learning terminology again.
*  I gave the tutorial at ICML last summer.
*  One way actually to me and I guess to many people lifelong learning and continual learning as synonyms.
*  OK. And they all just mean that you would like your model to learn in online scenario,
*  where online means you get your samples as a stream instead of I mean, you can get them as sequence of data sets or a sequence of batches or a sequence of just samples.
*  But the point is you have that sequence of data, you keep learning and you do not have an option of keeping the whole history of data sets.
*  Or you might even have that option, but you may not want to constantly retrain because it's not so efficient.
*  So continual and lifelong learning in this approach are synonyms.
*  Meta continual, continual meta and so on and so forth are still within the umbrella of continual learning,
*  but kind of different formulations of how you might go about training your system to do that continual learning.
*  Again, as I said, I'm sure people have different definitions.
*  So in my mind, it's a particular definition of continual learning, which just means online, non-stationary learning.
*  By non-stationary, I mean any change to the environment or input data, whether it's a change of data distribution, it's a change of task or both.
*  So as to transfer, transfer learning, again, I have the slides in the tutorial as well as in the class slides for the continual learning class.
*  They're all online on my web page.
*  I gave it for two years in a row.
*  It was winter semester class 2020 and 2021.
*  But I'm not giving it this year because I will be teaching neural scaling laws.
*  Oh, yes, there you go.
*  That's your new thing.
*  OK, well, continual learning is related to that.
*  It's not like we completely jump to something unrelated.
*  It is related, but with more focus on the scaling models, data and compute and continual learning being a problem that you're also trying to solve.
*  That's why. But back to your question about transfer, meta and the made adaptation and so on.
*  First of all, I have it in my slides.
*  Second, well, the slides are based on the very, very nice tutorial by the launch from 2020.
*  Anyway, so the picture defines each of those problems and shows how they are different and how they're similar.
*  Transfer usually assumes that you have two problems and by learning on one, you're trying to kind of trying to be able to use that knowledge to do better on the second problem.
*  As it is not necessarily any notion of remembering or being equally interested in doing both problems, it's like more unidirectional.
*  Again, question of terminology.
*  To me, transfer is a property of your model and algorithm.
*  And continual learning is a setting in which you would like transfer to happen, which means while learning, I always would like to improve or at least not make it worse.
*  My performance of the past, which means backward positive transfer or at least backward non-negative transfer.
*  At the same time, I'd like to hopefully learn better and faster in the future because I already learned so much.
*  So ideally, I would like to have some positive transfer to future.
*  And that view of not equating continual learning with catastrophic forgetting issue, but rather more general view of continual learning as a problem of maximizing transfer in both past and the future.
*  That kind of also came out of our joint paper on MetaExperienceReplay from 2019 with Matt Rimmer.
*  And I very much kind of support that view, more general view of continual learning.
*  And especially when it comes in the context of not just supervised or unsupervised, but continual reinforcement learning as an ultimate continual learning setting.
*  Yeah, so that's kind of where these different aspects may align and come together to build kind of the same thing.
*  I don't know. One big picture of what we're trying to achieve.
*  Agent that can adapt and still be able to return back to what's learned, maybe by retraining slightly with a few shorts like the flexible avoiding or forgetting and adaptation that is fast.
*  And the aspects such as transfer playing the key role.
*  The meta learning is essentially very similar to continual learning, but it does not assume that your different data sets came in a sequence.
*  They available to you at the same time.
*  And you try to learn from them common model that will be very easily adaptable to any new environment or data set, presumably from the same distribution of data sets.
*  So that's essentially meta learning.
*  And by the way, out of distribution, generalization is another related subfield, which is to me essentially zero short meta learning.
*  It's out of distribution setting is give me multiple data sets or environments, and I will try to learn a model that basically distills some common,
*  invariant, robust features or in general, common, invariant, robust predictor so that next time you give me data set for testing that is different from my training,
*  it's out of distribution and yet shares that invariant relationships, which are essentially closely related to causal relationships.
*  If you give me that, I will do well on that.
*  So it's extreme case of meta learning because meta learning will tell you I want to do well on that out of distribution data set.
*  Just give me a few samples to adopt.
*  So they all all this terminology, in a sense, comes together and has many shared aspects.
*  It's just, as I said, unfortunate Babylon tower situation and machine learning that makes it difficult.
*  The set of ideas is much less dimensional than the ambient dimension in terms of our terminology.
*  So they need machine learning compression.
*  It's long overdue.
*  Well, it's also the yeah, it's also the variety and problem statements.
*  But I want to ask you about that in a second, because so so just backtracking once more.
*  So you talked about three inspirations from neuroscience to help with continual learning.
*  One was the variability in plasticity.
*  So if you say you want to remember a certain task, there's evidence that those those synapses form stronger connections and are less likely to change.
*  Right. And so you lower the plasticity moving forward so that you can maintain good skills on a certain task.
*  Right. You also talked about the complementary learning systems approach using these two different learning and memory mechanisms.
*  One is fast and very specific.
*  And then that's associated with the hippocampus.
*  And then there's this general, slow and generalizable learning happening.
*  And that's associated with the neocortex.
*  And of course, you use replay, which has been used and I think originally with DQN to solve the Atari games.
*  And that's the reason I used much, much before.
*  Well, of course, even that's OK.
*  No, thank you for correcting me.
*  I knew I right when I said originally, I was like, oh, that's not good.
*  I'm just kidding. I'm just kidding.
*  But OK. And then the third was essentially inspired from neurogenesis, which is the idea that especially in the hippocampus of an adult,
*  you can continue to form new neurons and that this might help us in forming new memories.
*  So what I wanted to ask you about is the issue of the facts in neuroscience continuing to change because it's an empirical science.
*  Right. So I thought that recently there was backlash against this idea of neurogenesis in adults.
*  It's like one year milk is good for you.
*  The next year, it's really terrible for you based on new evidence.
*  So there are these I didn't know that the evidence was still pointing toward neurogenesis as a concrete fact.
*  Right. Because we're always finding out new things.
*  So the story is always being revised in neuroscience.
*  And I'm wondering if that affects your own approach, because if we hang our hat on neurogenesis and it turns out we actually don't create new neurons or something,
*  then how do we move forward from there?
*  Well, the good thing about computational, I don't know, machine learning kind of side of that,
*  even if it happens and in nature there was no neurogenesis to start with, we don't care.
*  We have algorithms that work better.
*  Yeah, you can always go back to that. Now you have your AI hat back on.
*  Exactly. That's why I never have only one hat.
*  I have multiple.
*  And I actually don't even think it's effective to have a single hat ever.
*  Although I understand it's kind of people tend to have one hat because we are so,
*  I don't know, we're so kind of tied to the notion of our identities, including the identity in terms of scientific views.
*  It's so common. It's so dear to our heart.
*  But in reality, the notion of identity in general is much more vague than we might think.
*  But I don't want to go into philosophy here because it will take a long time and we don't have the time.
*  It's a separate conversation.
*  Anyway.
*  OK, so then coming back to all of these different problem statements and how you were saying,
*  you know, are different definitions, but really they're all kind of converging onto like a lower dimensional problem space.
*  Given the various approaches to training and testing and meta-learning, you know, all the things that you just covered,
*  do we actually understand how humans learn well enough?
*  The developmental literature, the psychology, like do humans do all of these different problem statements or would it?
*  Is there a so I know that there's a little bit of work at least on, you know,
*  the humans actually showing a little bit of catastrophic forgetting in certain circumstances.
*  But do we actually understand human behavior enough and how humans learn, not at the neural level,
*  but at the behavioral level to map that onto these different continual learning, meta-learning, transfer learning?
*  Do humans do all of that? Do humans do some of it?
*  You know, does that make sense?
*  Yeah, it definitely makes sense. Well, first of all, I mean, there are many people who kind of focusing on this type of studies and developmental neuroscience.
*  So I really would love to read more about that.
*  As you just mentioned earlier, no human being, unfortunately, can be on top of all the literature and all the fields related to mind.
*  So there is lots of interesting recent work as well.
*  And I have some colleagues at UDM working on that.
*  And for example, Guillaume Dumas in the psychiatry department and Elif Muller in the neuroscience department.
*  There is a lot there. But in terms of not looking at neuro, just looking at the behavior and asking the question
*  whether human do transfer learning or continual learning particular settings.
*  I think yes, because in a sense, the notions of particular settings in continual learning, they came out of researchers thinking about like,
*  what do we do in real life in different situations?
*  Say we have robotics, what are kind of scenarios there?
*  The robot moves from one room to another room.
*  Environment changes.
*  All these settings and specifically of them, oh, now it's not just room didn't change, but I gave robot different tasks.
*  They all came out of our anecdotal observations of our own behavior of like just common sense reasoning in our heads about what people do.
*  So in a sense, yeah, I mean, whatever you have right now in continual learning fields, for example, of transfer,
*  it came out of our knowledge about human behavior.
*  Because in a sense, where else would it come from?
*  Well, yeah.
*  Yeah. So in this sense, yeah, but more on that, like more specifically, like studies about how it's being done and like what effects that what kind of makes it better or worse.
*  For that, we would need to talk to our colleagues in psychology and your science and read more about that.
*  And I'm pretty sure, as I said, I mean, I'm not claiming I'm completely on top of any literature that you don't wear infinite hats.
*  Well, that would be that would be the ultimate goal.
*  But for that, first, I need to create a G.I.
*  Then you connect with a G.I.
*  And then you have your augmented brain, which can finally stay on top of all that literature.
*  That's my true motivation.
*  All right. All right. OK, so I have one more question about about continual learning.
*  And then we'll begin to wrap up here.
*  Someone in the brain inspired discord community asked whether the learning trajectories of artificial networks impact
*  have an impact in continual learning, right?
*  How much it retains and how much it forgets over successive tasks and training?
*  Have you do you have you studied the learning trajectories at all?
*  Because that's something that's being looked into in deep learning theory these days as something that matters.
*  Yeah, the learning trajectory.
*  OK, the question is also it depends on several things.
*  It depends on, say, the sequence of tasks like curriculum learning, which which can matter a lot indeed.
*  Actually, it matters not just for continual learning, it matters for, say, adversarial robustness.
*  Even it matters for various aspects of the end model, like how what sequence of data was given to it and how it arrived there.
*  But of course, it also depends on, say, particular optimization algorithm that basically different trajectory leads you to different state in the weight space,
*  leads you to different model or think about a different, yeah, different brain, artificial brain.
*  And of course, they will differ in terms of their properties, in terms of forgetting and so on.
*  So I guess when we were looking into again, I'm thinking about this MERE paper with Mudd and others.
*  Obviously, the trajectory matters.
*  The question is, how do you how do you know what the local kind of constraints or local kind of intuitions you should use to push trajectory into the desired kind of direction?
*  Because like all we can do is just to use kind of some local information, just like as gradient is.
*  And I guess, well, things that change trajectories, I mean, as I said, data can change trajectory, all kind of regularizations can change trajectory.
*  Basically, regularizations are precisely things, among other things, that change trajectories a lot.
*  You have objective, standard objective of your neural net, and you're trying to optimize for that.
*  And then you add things.
*  One example, say you say, I really would like to make sure that I have that positive transfer or at least non-negative.
*  Let me add as a constraint the product of gradients on new and old samples.
*  And I want the things to be aligned.
*  I do not want my new gradient to point in the direction opposite of the gradient on previous samples,
*  because that would mean I will be decreasing performance on the past task I will be forgetting.
*  So I'll try to add at least locally regularizer, again, like in my paper with smart, for example,
*  just one example that will push my weight kind of trajectory in that direction and so on and so forth.
*  So basically, any regularizer you put there with some desirable features, but without, of course,
*  any guarantee because it's all local, it will change the trajectory.
*  So in a sense, the whole field of continual learning playing with at least the regularization based field,
*  it's all about changing trajectories and then changing the final solution.
*  So there isn't a good theory about how to do that really yet, right?
*  Again, I don't want to claim, I mean, there is various work.
*  There was a paper on them, like trying to theoretically understand continual learning algorithms,
*  but for specific type of them, there is this, what was the name, orthogonal gradient descent and that work.
*  OK, there is various work, but to me, continual learning is still the field that is lagging behind quite a lot in terms of theoretical understanding.
*  I was going to ask what your outlook is for continual learning.
*  If we solve continual slash lifelong learning, is that the same as solving AGI?
*  And, you know, are you optimistic about what, you know, what's what?
*  What is the normal number that people say 20 years and that's when we'll have solved everything?
*  It's always 20 years or so, right?
*  Oh, some say less than that.
*  What's your number?
*  Ten or less.
*  Ten years for lifelong learning?
*  Yeah.
*  OK.
*  And AGI.
*  That equates to AGI or when we solve lifelong, is that solving AGI?
*  OK, so again, difference in terminology.
*  I apologize to people who might like really strongly disagree with me.
*  And I know some people who will.
*  I'm not going to say.
*  Let's drop some names.
*  I know. No, no, no, no, no.
*  We're not going to do that.
*  But those people know.
*  Well, there is also this kind of view, which is still an open question.
*  The view about what does it take to solve continual learning, whether it equates to AGI and so forth.
*  So if we assume that AGI for all practical purposes is general artificial intelligence,
*  by general, it's versatile, broad.
*  It can kind of learn to solve pretty much any task that is, as people often put it, economically valuable.
*  So say AGI is kind of a model that can solve all economically available tasks, say, as good as or better than human.
*  Something rough like that.
*  The question is, if you kind of put that agent in the wild, it will have to do continual learning, right?
*  So it needs to be kind of solved.
*  The question is whether you approach solving it by trying to train that agent in continual learning manner or as scaling crowd will tell us,
*  or at least part of the scaling crowd.
*  I'm not overgeneralizing that maybe it's enough just to really pre-train a humongous foundation models on multi-modal data,
*  not just language, not just video, not just the images like video, or perhaps even all kinds of time series data.
*  But once you pre-train it, it essentially solved continual learning.
*  I had this question during the workshop discussed and it's ongoing debate.
*  What I would say is that for any fixed set of possible tasks that you will give continual learner,
*  like, for example, recent submission to a clear on scaling and continual learning for a fixed set of tasks.
*  Yes, sure.
*  Scaling model, scaling amount and diversity and complexity or information content of pre-training data will at some point conquer the complexity of the fixed set of tasks.
*  And yes, you will solve catastrophic forgetting.
*  You can capture information of all those things and you can do all of them well.
*  But if that stream of tasks and continual learning continues growing, right, infinitely,
*  will your pre-trained model hit the wall at some point or not?
*  And that's a good question.
*  And I think it's interplay between the model capacity.
*  I always keep saying that also in my tutorial on continuing capacity of the pre-trained model
*  that you learned and the complexity of unseen part of the universe that your agent will have to adapt.
*  And I would say that what you really need to look into would be relative scaling of how your model capacity that depends on size,
*  architecture and information content of the data you trained on, which depends on the amount or number of samples,
*  but other things too, how that capacity scales with respect to complexity of downstream tasks.
*  So to me, relative scaling laws would be the most interesting thing to dive into.
*  And I think it makes sense.
*  It's always a trade off capacity versus complexity, just like great distortion theory and information theory and so on.
*  And you want to find the minimum cost, the minimum capacity agent that's capable to kind of work well,
*  conquer the complexity of whatever future tasks that agent will be exposed to.
*  But if the agent hits the wall, the agent will have to have the ability to expand itself and continue learning.
*  So to me, continue learning is the ultimate test for anything that is called AGI.
*  That sounds like incorporating principles of evolution into...
*  Yes.
*  So any pre-trained model may hit the wall and I believe it will have to keep evolving.
*  And if it won't be able to evolve itself, too bad.
*  OK, Irina, this has been fun.
*  I have one more question for you, and that is considering your own trajectory,
*  if you could go back and start over again, would you change anything?
*  Would you change the order in which you learned things or order of your jobs?
*  How would you start again?
*  Oh, that's a very interesting question.
*  I'm not sure I have an immediate answer to that.
*  But in one of those realities, I might have been taking a totally different trajectory from the one I'm on right now.
*  I probably would have been skiing somewhere in Colorado, working as a ski instructor.
*  Oh, I do all of that except work as a ski instructor.
*  You should try what I do.
*  I would be full-time ski instructor.
*  OK, I just went two days ago.
*  Look, Tremblant is pretty good, too.
*  So it doesn't matter. Some good mountain.
*  And just, I know.
*  Why don't you come visit me and we'll go ski and we'll see if we can change your trajectory.
*  And you're welcome to visit Tremblant.
*  It's pretty nice.
*  All right, very good.
*  Well, I really appreciate the time.
*  So thanks for talking with me.
*  Thank you so much for inviting me. It was fun.
*  The music you hear is by The New Year.
*  Find them at thenewyear.net.
*  Thank you for your support.
*  See you next time.

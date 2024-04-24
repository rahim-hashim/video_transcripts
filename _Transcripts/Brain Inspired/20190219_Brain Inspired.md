---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4450s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 14113
Video Rating: None
---

# BI 028 Sam Gershman: Free Energy Principle & Human Machines
**Brain Inspired:** [February 19, 2019](https://www.youtube.com/watch?v=U5RVQGdHI0k)
*  you could build agents that adhere to those principles and many agents in that set would be what we consider smart and many of them would be stupid.
*  Isn't that what we have already?
*  Yeah, right, exactly. So I really like what Sherlock Holmes said that to understand nature, your mind must be as broad as nature.
*  That's how I feel. Like really the study of intelligence is that.
*  This is Brain Inspired.
*  Hey everyone, welcome to episode 28 of Brain Inspired. I am Paul Middlebrooks.
*  I had been thinking of a way to talk about the free energy principle on the show and I was going to have a guest on a few weeks ago, but we had to reschedule that for a later time.
*  But I stumbled on a recent paper by the person you just heard, Sam Gershman, who is a professor at Harvard University and runs the Computational Cognitive Neuroscience Lab there,
*  where they study learning, memory, decision making, you know, cognition.
*  He's recently written about the free energy principle and how it relates to other bigger picture theories of how our brains function,
*  in particular the Bayesian Brain Hypothesis and the concept of predictive coding in general.
*  So we talk about just that during the first part of the show.
*  Sam also co-authored a paper a couple years ago now called Building Machines That Learn and Think Like Humans.
*  That paper breaks down some of the important ingredients that current deep learning networks are missing if we want to get to human-like intelligence.
*  So we talk about those concepts and how far along we've come since then.
*  So those are the two major themes during this show.
*  And of course we discuss much more like the limits of our own cognition and how that affects our ability to understand complicated processes in the world, including our own intelligence.
*  And hang on until the end too, because Sam gives some career advice that I love for those of you early in your career or even deep in your career,
*  but trying to figure out your next course of action, your next direction.
*  Every new show I do, I realize I have more and more questions to ask of the guests to try to bring it all together and keep some sort of running thread from the previous guests.
*  So I try to do that here, but of course I can never get to all the questions.
*  You can find out more about Sam and links to the stuff that we discuss in the show notes at braininspired.co.slash podcast slash 28.
*  And you can also find how to support this ad free labor of love of a podcast by finding and clicking on the red Patreon button at braininspired.co.
*  Fair y'all see May, Ion and Justin did just that this past week. Thank you guys. That is beautiful.
*  All right. Thank you for listening. I hope that your projects are coming along smoothly and you're immersed in and loving whatever it is that you're pursuing.
*  Enjoy the show.
*  All right, Sam Gershman, welcome and thanks for being on the show.
*  Thank you. So Sam, you are a you run the computational cognitive neuroscience lab at Harvard and you do lots of things.
*  For instance, you study how we learn. You study the different systems that we use to learn and how they interact, how our perceptions get transformed into these internal states in our brains and how those states can be used to guide our actions.
*  You study processes like exploration versus exploitation and plenty more.
*  Today we are here to talk about two subjects in particular.
*  One, the free energy principle, which is a hot topic these days in brain function and neuroscience.
*  In your recent paper, what does the free energy principle tell us about the brain?
*  And two, we're going to talk a little bit about the concepts introduced in your paper from, I guess, two years ago now called Building Machines that Learn and Think Like Humans.
*  You ready?
*  The free energy principle. What does the free energy principle tell us about the brain?
*  So in this paper, you compare predictions of the free energy principle with the Bayesian brain hypothesis and how those two systems might fall out and compare to each other in this realm of what's called predictive coding.
*  Now, I'll just begin by reading the opening paragraph of a 2009 review by Carl Friston, who has been the developer of the free energy principle, just to get us kind of rolling on this topic here.
*  So he writes, The free energy principle is a simple postulate with complicated implications.
*  It says that any adaptive change in the brain will minimize free energy.
*  This minimization could be over evolutionary time or milliseconds.
*  In fact, the principle applies to any biological system that resists a tendency to disorder, from single cell organisms to social networks.
*  I could go on, but that's his opening paragraph to introduce the concept of the free energy principle.
*  Now, I'll let you maybe comment on this. So, Sam, what is the free energy principle?
*  Yes, I should preface this by saying that I'm not either an advocate or an antagonist of the free energy principle.
*  I've just noticed over the years that through many conversations with colleagues that there's widespread confusion about what exactly the free energy principle is and what it predicts.
*  And so that was the motivation for me to enter into this fray.
*  And I should say that the free energy principle is closely connected to ideas that I've proposed and have been deeply interested in.
*  So I think the real question here is what is really special about the free energy principle relative to other ideas that have been out there for a while.
*  And I can elaborate on that. So in essence, the free energy principle is the idea that the brain minimizes surprise.
*  Mathematically, it's a little bit more complicated than that, but that really gives you the gist of it.
*  Now, the term free energy is a little bit unintuitive for a lot of people because it actually comes from physics.
*  The idea was that you can decompose a complicated inference problem into an equality that expresses the relationship between what physicists call the partition function
*  and what they call the variational free energy. And it turns out that the object that the physicists were studying is closely related to problems in machine learning and statistics
*  where probabilistic inference problems are intractable and they can be made more tractable by turning them into an optimization problem under constraints.
*  So what does that mean? And this actually is perhaps usefully introduced by first talking about the Bayesian brain hypothesis and then talking about where the free energy principle enters into that.
*  So the Bayesian brain hypothesis states that the brain is confronted with ambiguous sensory evidence, and it tries to interpret that sensory evidence by making inferences about the hidden causes of the brain.
*  So we have two different processes that produce the sensory data. So for example, on our retina we get a two dimensional projection of a three dimensional world,
*  which means that the two dimensional information is fundamentally ambiguous. There's no unambiguous mapping from the 2D into the 3D.
*  Nonetheless, we're able to perceive three dimensional structure and the way we do that is we combine the noisy or ambiguous sensory information with prior beliefs about the nature of the world.
*  So for example, that objects have surfaces that are smooth and continuous, right? We can exploit those prior beliefs to make inferences about the hidden structure of the world.
*  And the Bayesian brain hypothesis is really that the brain is using Bayes' rule to convert its prior beliefs into its posterior beliefs.
*  The posterior beliefs are the beliefs about hidden variables in the world, given the sensory data or other kinds of information that the brain has received.
*  Now, that sounds very simple, and if you just write down Bayes' rule, it's actually mathematically extremely simple, and it's a direct consequence of the axioms of probability theory.
*  The problem is that if the space of latent variables, the hypothesis space, is really large, then implementing Bayes' rule computationally is totally intractable.
*  And part of the algorithmic challenge is to develop approximations of Bayes' rule that can give approximately correct answers.
*  And that's where computer scientists and statisticians drew inspiration from solutions that were developed in physics.
*  In fact, a lot of algorithmic ideas in computer science, particularly in the domain of probabilistic reasoning, come from physics originally.
*  And so the idea was that we can convert Bayesian inference into an optimization problem.
*  And the way we do that is we say that there's some family of possible probability distributions, and I'm going to try to pick one distribution in that family that gets as close as possible to the true posterior distribution.
*  Right. A good first guess.
*  Yeah. Well, no, it's not necessarily a first guess. It's that I'm going to actually try to search through this space of distributions to find the one that gets closest.
*  Now, the problem there is that if you just state it in that way, it's just as intractable as the original problem, because you can't compute the similarity between distributions unless you actually know both distributions.
*  And the whole name of the game is that we're trying to approximate the posterior distribution.
*  So the way that the key algorithmic trick that variational inference introduces is to put some constraints on the family.
*  So, for example, if you have a collection of hypotheses about the world, like a bunch of different dimensions of the hypothesis space.
*  So, for example, you're looking at you're getting some two dimensional data and you're trying to infer both the size and the weight of some object that you're looking at.
*  Now, in general, size and weight may be correlated, but you could make the approximation that I'm only going to consider approximations in which those two things are uncorrelated with each other.
*  So that's sometimes called a factorization of the posterior and it's related to what physicists call the mean field approximation.
*  So it turns out that if you do that, then you can simplify the inference problem and it no longer becomes intractable.
*  Now, what does this all have to do with the free energy principle?
*  So the free energy principle is a form of variational inference.
*  When we say that we're converting an inference problem into an optimization problem, the thing that we're optimizing is the free energy.
*  And so there's really no difference between variational inference and the free energy principle in general.
*  And in fact, there's no difference between those things and the Bayesian Brain Hypothesis in general,
*  unless you put some constraints on the family of distributions, this variational family, as they call it.
*  So once you start putting constraints, then the solution to this optimization problem is no longer identical to the true posterior.
*  OK, so that was a really nice introduction, I think, to the topic here.
*  But you threw around a bunch of technical terms.
*  And so your paper is all about how putting different constraints on the free energy principle, how it then matches up with the Bayesian Brain Hypothesis and so on.
*  I mean, is this why the free energy principle is notoriously difficult to understand?
*  Because it's a little slippery in that it's not, well, to say it's not overly constrained may be an understatement,
*  because it can go so many different ways. It seems so plastic with the way that it can account for different processes.
*  I mean, is that why it's so difficult to understand?
*  Well, I think there's a few different factors here.
*  So one is that you're right that there are a lot of degrees of freedom depending on how you implement the free energy principle.
*  So in this context, as I was saying, a critical question is how do you parametrize the distribution, the family of distributions that you're going to consider?
*  And then also, how do you search through that space and actually solve the optimization problem?
*  Efficiently.
*  Yeah. So it turns out that those different choices have important implications about things like predictive coding, which we can talk about.
*  But I mean, another issue here is that the papers on free energy principle are notoriously dense and long and hard to read.
*  Yeah.
*  And so I think that even quite technically literate people have trouble with that.
*  And so I was trying to clarify some of those issues.
*  Yeah. So, I mean, as you were talking about the Bayesian Brain Hypothesis, I immediately jumped six analogies or something and just thought about the tabula rasa of, you know, potential tabula rasa of a baby being born, let's say.
*  Right. And they come out and obviously they don't have an infinite number of distributions ready at hand to then be able to parse them down and constrain the actual problem of sensing mom's nipple, you know, whatever.
*  So and this actually gets to what we may speak about later in terms of what deep learning needs and the other paper.
*  But it's an interesting argument against a tabula rasa, because if you come out as a tabula rasa, you do have an overwhelming number of possibilities and you're just stuck with too many options.
*  Right.
*  In other words, your prior is infinite. So how do you even come up with a posterior?
*  Right.
*  Because how do you choose a prior at that point?
*  So it's a really it's a really intriguing and comforting hypothesis that makes a lot of sense, let's say, common sense to me, the way to approach how we learn and act.
*  Yeah, I mean, I would just try to clarify that the free energy principle is somewhat different from how we choose a prior.
*  It's certainly true that learning about the world is impossible without a prior.
*  There are theorems stating basically that if you're totally unconstrained in what you can learn, then basically you'll never be able to generalize effectively.
*  But that's a little bit different from the free energy principle, which in my view is really about algorithmic approximations of problems to get in front.
*  So even after you pin down your priors, there's still the question of how do you actually compute with them?
*  How do you make inferences? And that's where all the action is in free energy.
*  That's that's really what differentiates free energy approaches from just the Bayesian brain hypothesis writ large.
*  It's really a subset of possible algorithmic solutions to Bayesian inference.
*  Do you want to talk a bit about predictive coding?
*  I'm not sure that. Sure.
*  I mean, I don't think it's not going to be easy to convey the technical arguments on a podcast.
*  None of these things are easy, really, on a podcast.
*  But I would just make the point that let's start by summarizing what predictive coding is all about.
*  So predictive coding has been perhaps the most influential legacy of the free energy principle for neuroscience.
*  And the idea there is that that there are ascending and descending or feedforward and feedback pathways in the brain.
*  Most of the time we're talking about cortex.
*  Right. And the feedforward pathways are conveying prediction errors, so discrepancies between observations and expectations at each level of the hierarchy.
*  And then the feedback pathways are conveying those expectations.
*  Let's just contrast this with sort of a classic view of the feedforward projections, right?
*  Classically, you could think of, well, not classically, I suppose.
*  I don't know what classic is anymore, but the feedforward projection sort of building up a hierarchy of representation becoming more and more abstract.
*  Would you say that's accurate?
*  Yeah, yeah. That's one way to think about that.
*  Predictive coding doesn't necessarily exclude the possibility of some increasing level of abstraction,
*  but it does make the strong claim, which there is some experimental evidence for, that the representation at a particular level of the hierarchy is suppressed.
*  The feedforward pathway is suppressed if that representation is anticipated.
*  So, for example, there were studies about a decade and a half ago using functional MRI showing that when you present a collection of line segments,
*  activity in primary visual cortex, V1, is suppressed when those line segments can be understood or interpreted as a shape, as a coherent three-dimensional shape.
*  And concomitantly, activity in the lateral occipital complex, which is known to be shape-sensitive, increases.
*  So there's a decrease in activity in V1 and an increase of activity in LOC.
*  And that was interpreted as arising from this predictive coding framework where because the shape representation could predict the underlying line segments,
*  then the line segment representations become suppressed because now they're predictable.
*  Gotcha.
*  Now, what does this have to do with the free energy principle?
*  Well, it turns out that you can derive this kind of architecture from the free energy principle.
*  But the catch is that you have to make a whole bunch of assumptions that have to do with the variational family.
*  So what space of distributions are you going to constrain the inference problem to?
*  You have to make assumptions about ways in which you're going to approximate the free energy itself
*  because it turns out that under those chosen specifications, you can no longer actually analytically compute the free energy.
*  So anyway, the point is that there's a bunch of ingredients that have to work well together in order to produce predictive coding.
*  It's not a generic consequence of the free energy principle as is sometimes conveyed.
*  So these are the things that you actually explore deeper in the paper.
*  Yeah.
*  And of course, the paper's online and I think it's archived, right?
*  Yeah.
*  So I'll link to it and pretty soon it'll be in science, I'm sure.
*  So, Sam, what do you think?
*  Like the Bayesian brain hypothesis and the free energy principle can both be seen as these over-
*  these encompassing theories of brain function in general, right?
*  And how we aim to understand our minds and intelligence in general.
*  Do you think that we'll ever have like a single account of our brains and our minds?
*  Well, I think that the Bayesian brain hypothesis and free energy principle, they are good candidates for some general principles,
*  but they're not really sufficient by themselves, right?
*  They're too general in some sense. They're too powerful.
*  In order to act- basically, you could build agents that adhere to those principles
*  and many agents in that set would be what we consider smart and many of them would be stupid.
*  Wait, isn't that what we have already?
*  Yeah, right. Exactly.
*  But my point is that if you want to pin things down sufficiently that you could say,
*  all right, this kind of architecture, these kinds of constraints, these principles are only going to produce smart things
*  or tend to primarily produce smart things, then you need to make more assumptions than just that the brain is Bayesian or minimize the surprise.
*  I mean, thinking about that, do you think it's a better approach?
*  Of course, both approaches together is probably the best path, but a better approach to go-
*  to start overly constrained or to start without enough constraints, to start with something like the free energy principle
*  and then start whittling away with constraints. You know what I mean? What approach is a favorable approach?
*  Well-
*  There's a balance, I know.
*  Yeah. I mean, it's important to make a distinction between the engineering goals of building artificial intelligence
*  and the scientific goals of trying to parse what makes humans or animals intelligent.
*  Obviously, those things will converge in some ways, but the scientific strategy is different in the sense that
*  we want to design controlled experiments where we can isolate a particular hypothesis and test it.
*  That's different from engineering approaches, which typically aim to construct something that does something useful,
*  and whether or not some particular component of it has been isolated is not that important,
*  particularly in the era of building very large deep neural network architectures that don't have a lot of interpretability,
*  but can still accomplish certain kinds of tasks. The research strategy is different.
*  Well, speaking of building things, maybe we could transition here and talk about deep learning and the state of AI
*  and what it has, what it needs, what it's missing. So this is your paper, Building Machines that Learn and Think Like People.
*  This is in Behavioral and Brain Sciences, and this is a thorough paper because it's in Behavioral and Brain Sciences,
*  and made even more thorough by the format. So just, I mean, people know this, but there's a target article which you guys wrote,
*  and then there's a bunch of reviews, and then you get to rebut the reviews, and this is all in a single document,
*  and it costs about a three and a half if you really want to print the whole thing out. So I've always liked that format,
*  but I've not written one like that, and it's a lot of work just to get reviews. One of my papers is under review right now,
*  and just with three to four peer reviewers, it's a lot of work just to rebut that and send it back, but it seems like a lot more work for you guys.
*  I mean, what was that experience like?
*  It's all kind of a blur to me now.
*  Yeah, I know. That's the other thing is if it was written last year, you probably did the work 12 years ago.
*  Yeah, yeah. No, it was a lot of work, but it was fun to write. It was great writing that paper with those co-authors,
*  because these were ideas that we had talked about for a long time, and it finally forced us to really coalesce them.
*  Yeah. Okay. So I had Melanie Mitchell on the show a few weeks ago, and she's a complexity expert, and she's been in the field of AI for a long time,
*  and she had written this op-ed in the New York Times.
*  Yeah, I read that.
*  Yeah, okay. So here's just a quote from her approach to this.
*  Today's AI systems sorely lack the essence of human intelligence, understanding the situations we experience, being able to grasp their meaning.
*  The mathematician and philosopher Giancarlo Rota famously asked, I wonder whether or when AI will ever crash the barrier of meaning.
*  So there's this phrase, the barrier of meaning. And this paper that you co-authored takes that sort of broad statement and breaks it down into cognitive components that could help bridge that gap.
*  So it's really an initial roadmap of sorts and has seemingly served as such, which must be pretty rewarding for you to have seen.
*  So maybe we can frame this this way.
*  Maybe we can just start off talking about how machines think and learn currently, and then maybe bring in how humans think and learn what we know about that, and then talk about them together.
*  So the premise of the paper is like, look, yeah, we've done great work with AI and deep learning has done amazing things, but it's still not human-like.
*  And if we want to make it human-like, we need to build in these other components, these higher level components, either build them into the deep nets or however you're going to perform the AI, build these core ingredients in.
*  Do you want to just talk for a moment about the current state of how machines think?
*  Yeah, well, it's quite hard to make a really general characterization of how machines think because there's a hundred papers posted on archive every day on machine learning.
*  It's a rapidly moving target. And our paper was really focused on kind of general patterns.
*  So it's not the case that our critique skates every machine learning paper that was ever written.
*  But these are debates that have been going on for a long time.
*  And we discussed this history a little bit in our paper, I mean, since the 70s and 80s.
*  By the way, it's a beautiful paper. I really enjoyed it. I bet you've heard from a lot of people the same as well.
*  Thank you.
*  Yeah, so people have been going back and forth about the necessary ingredients for intelligence for a long time.
*  And I sympathize with computer scientists in some ways because there's this feeling of moving goalposts.
*  Like there's a time when people said, you know, when a computer can win at chess, that's when we know it's really intelligent.
*  If it wins a go, then it's really intelligent. And it's a sort of moving goalpost.
*  And, you know, I'm sure some people wonder, like, when are you going to be satisfied?
*  And I'm not really a big believer in having a kind of single test of that sort, because I just think that human intelligence is too multifaceted to really be boiled down in that way.
*  But that being said, I do think that it's important for us to think about what we've learned from the study of cognitive science and what that tells us about the nature of human intelligence and the limitations of current AI approaches.
*  So with that preface in mind, I can kind of make some broad stroke characterizations.
*  The basic thrust of modern machine learning approaches, particularly deep learning approaches, has been to construct systems that are extremely expressive in the sense that they can learn lots and lots of different things.
*  So we could think about this as a kind of function approximation problem.
*  Like, you get you have a function that maps images to object categories, and that's one way to think about an object recognition system.
*  Or you have a translation system that's mapping text in one language to text in another language.
*  So these are all potentially really complicated functions.
*  And the general approach has been to build very complicated neural network architectures.
*  Now, I should say they're not conceptually complicated.
*  You can basically draw a picture of them, and it's pretty straightforward.
*  You have a bunch of neurons that are connected to each other in layers.
*  But they're complicated in the sense that they're very expressive.
*  They have lots of degrees of freedom, possibly millions of parameters that then get optimized by a learning algorithm.
*  So you could take the same network, same naive network or whatever, and train it on a bunch of different types of domains.
*  So you could use this thing to train it on recognizing objects.
*  You could use this same network to train it on language or something within the realm.
*  There's a lot of possibilities to train it.
*  Yeah. So just to maybe put this in perspective, before the heyday of deep learning,
*  the most successful approaches used collections of hand-engineered features.
*  So people would put a lot of thought into defining various kinds of image or natural language features depending on the domain.
*  And then they would assume a fairly simple supervised learning algorithm that operated on those features.
*  So, for example, you might assume that you take this collection of features, you map them through a linear function,
*  you map them through a linear classifier, and then you basically train the weights of that linear classifier.
*  So that's a very low-complexity solution in the sense that the space of possible functions that can be learned is relatively small.
*  So you can only learn linear functions of this feature set.
*  Contrast that with a deep neural network where all the different parameters and all the layers are being optimized to solve this classification problem.
*  That's what's commonly called end-to-end training.
*  And now you have millions of parameters and the function space is enormous because now you don't necessarily, you're not necessarily restricted anymore to linear functions.
*  You could learn linear functions, but you could learn all sorts of nonlinear functions.
*  So you might think, okay, well, that's great. Now we can learn more functions, right?
*  But the catch is that the more complex your function class is, the more data you need to effectively learn it
*  in the sense that if you only have a small amount of data, then you could learn to model those data very well.
*  If you have a very large function class, you can fit the training data really well.
*  But the problem is that there may be noise in that training data or the training data might not be representative sufficiently of all the test cases you might encounter.
*  And so your classifier is going to fail to generalize.
*  And there's a whole literature that rigorously analyzes this from a statistical learning perspective.
*  It's called the study of sample complexity.
*  How much data do you need to effectively learn, to effectively generalize?
*  And in general, more complex models need more data.
*  And that's why actually, in some sense, the deep learning revolution has been just as much about big data revolution in the sense that we've constructed bigger and bigger data sets to feed the insatiable sample complexity needs of these learning algorithms.
*  Plus the computational power to do so.
*  Yes, absolutely. Yeah. And that was the other thing. So yeah, big computation is a big contributor.
*  In some sense, the deep learning architectures we're using today are pretty similar to the ones that we had in the 90s, but they work better because we have a lot more data and a lot more computing power.
*  That being said, it is still somewhat of a mystery to learning theorists why these things work because, you know, at first blush, the learning theories would say that you would need even more data than we have to effectively generalize.
*  But learning theorists are trying to crack open that nut and that it's probably not worth getting into that right now.
*  But the point here is that the approach today is about building really flexible function approximators.
*  Now, that doesn't sound so sexy from the perspective of artificial intelligence to boil them down to nonlinear function approximation.
*  But that's really what it's all about.
*  Now, as I was saying, the architecture of these networks is really flexible, but it also means that that that very flexibility allows the system to learn things that we might think of as not being the right answer.
*  So it's going to pick up all sorts of patterns, but it might fail to learn the same kinds of things that humans learn and they might not learn those things in the same way.
*  So let me try to elaborate on what I mean by that.
*  So I was talking about complexity in terms of the number of parameters and the size of the function class.
*  But another way to restrict the effective complexity of a machine learning system is to have an inductive bias.
*  So it says that the inductive bias says that, all right, I could in theory learn any function in this function class, but I have a preference a priori for certain functions over others.
*  So I think that some functions might be more plausible than others.
*  And I can formulate that in the language of probability theory.
*  And that shapes the sample complexity arguments, because now, even if I have a really large function class, if I have very strong inductive biases, that can kind of compensate for the need to experience a lot of data.
*  The inductive biases basically say that some things are going to be easier to learn with less data and other things are going to be harder to learn and will require more data.
*  And how does that compare to having a stronger priors?
*  Those are priors, right? So inductive biases are priors.
*  I mean, you can construct, depending on what your kind of formal framework is, you can talk about inductive biases in a non-Basian way.
*  But I often think it's helpful to think about prior distributions as a particular way of representing inductive biases.
*  I see. Okay.
*  So now, let me try to loop this back to human cognition.
*  We think that humans can learn from small amounts of data precisely because they have very strong inductive biases.
*  And they also have inductive biases that are relatively abstract, which allows them to generalize their knowledge very widely.
*  So let me just talk about some of those inductive biases.
*  Actually, before I talk about inductive biases, let me just try to make vivid why you need an inductive bias.
*  There's a great book by Eric Baum called What is Thought?
*  And he has the following example. So imagine I'm training a chair classifier.
*  So I'm giving it images and it's telling me chair or not chair.
*  All right. So I give it some finite number of these training images and it learns to perfectly classify, to perfectly discriminate chairs from non-chairs.
*  All right. Now I'm going to give it a new chair. And I want it to generalize to that.
*  Now, let's imagine that it had no inductive bias.
*  The implication of having no inductive bias is that, in fact, this classifier, which could perfectly discriminate between chairs and non-chairs in the training set,
*  has no basis of generalizing to this new image.
*  In fact, it would have no basis of knowing whether this new image is a chair or a non-chair.
*  And the reason is because in a continuous function space, there are an infinite number of functions that separate the chairs from the non-chairs.
*  And that means that there's an infinite number of functions that would perfectly separate chairs from non-chairs and classify this new image as a chair.
*  And then there's also an infinite number of functions that perfectly separate chairs from non-chairs and classify this new image as a non-chair.
*  And what it means to have no inductive bias is that you have no preference about which of those functions is the correct function.
*  So generalization depends crucially on having some inductive bias.
*  Now, neural networks do have inductive biases. The architecture of the network, the parameterization and so on, those are all forms of inductive biases.
*  But they're just relatively weak inductive biases.
*  Now, we think that humans have strong inductive biases. They have strong inductive biases about things like causality, about objects, about relations between objects,
*  about compositionality of knowledge, so that the idea that you can build complex representations out of simpler ones.
*  And we have strong inductive biases in different domains that take the forms of something like an intuitive theory,
*  like an intuitive theory of psychology that lets us make inferences about other people's minds or an intuitive theory of physics that allows us to make inferences about physical interactions in the world.
*  Anyway, I'll stop there and let you.
*  Well, no, that's okay because you're sort of rattling off the ingredients that are proposed in this paper.
*  So and you just got there naturally, which is a beautiful thing.
*  Yeah, so I was going to ask about how humans learn, right?
*  And in comparison, which is where you've really just brought us to anyway.
*  But before we even get into just a few, maybe of the examples of these things that you just listed,
*  it's an interesting conundrum whether we understand how humans learn well enough to then.
*  So the whole goal is to build systems that learn and think like humans.
*  But do we learn? Do we know how humans learn and think well enough to even begin doing that?
*  And so these are things, you know, like when you say terms like intuitive physics, of course.
*  Well, let's just maybe we can put that question on hold unless you want to answer it.
*  And then we can kind of step through a few of the ingredients.
*  Well, no, I mean, I don't think that we know enough about human cognition that we can just implement human intelligence in a computational system.
*  It's more just that we have some general hints and also some specific computational models about how humans think.
*  And those are in interesting ways different from a lot of the prevailing deep learning architectures.
*  Now, I will say that even at the time that we were writing that Behavioral and Brain Sciences article, people were already starting to realize this.
*  So, for example, in the domain of intuitive physics, there was a lot of interest in building machine learning systems that that solved intuitive physics problems.
*  And if you build them in a kind of naive sort of off the shelf way, they didn't work very well.
*  And they only started to work really well when people started building in constraints.
*  And I would argue that those a lot of the constraints that worked well were precisely the constraints that we think people have.
*  So, for example, DeepMind and other groups have developed models in which there are primitives that correspond to objects and their functional interactions between the objects.
*  So it's a relational model that's object oriented.
*  And then you use deep learning to learn the parameters of those functional interactions.
*  And that works much better for modeling intuitive physics.
*  So I would argue that that's kind of harnessing the strengths of deep learning, which are really about flexible function approximation with the kinds of inductive biases that we think humans have.
*  OK, so let's just step through these. So there are five core ingredients. Is that the latest count?
*  I mean, this is the sort of the count in the paper.
*  Yeah, so one of them is this intuitive physics that you're just talking about.
*  And this is the idea of so this falls under the rubric of when we're really young, we're kind of born with and have really early on this developmental software.
*  Right. So that's sort of ingrained or an inductive bias.
*  Right. So intuitive physics is the idea that we understand that when one cue ball hits, when one pool ball hits the other billiard ball, we understand that there's a collision there.
*  These two things are solid and one affects the other. Yeah. Well, it's a lot more than that, probably.
*  But well, that's one aspect of it. Yeah, that's one aspect of it.
*  So, you know, the things are solid, not a liquid and and so on and so on.
*  So so this is one thing that is sort of missing in deep learning networks that you were just describing.
*  And there's been there's work being done on all of this.
*  Like I said, it's it's this is a nice roadmap that people have seemingly been following, actually.
*  So another one of those that falls under the rubric of developmental software is the intuitive psychology like you were just that you mentioned.
*  Do you want to just describe what that is briefly? Yeah.
*  So maybe just first for those people who are not familiar with the notion of intuitive theory, the reason that they're called intuitive theories is to contrast them with scientific theories.
*  And the argument is that intuitive theories and scientific theories share a lot of the same structural characteristics.
*  But obviously, they differ in content in the sense that, you know, intuitive psychology doesn't have access to, you know, functional MRI and response time studies and so on.
*  Right. But but we still can build a theory like representation of another person's mind.
*  For example, we can reason about another person's beliefs and desires and combine our beliefs, our knowledge of those beliefs and desires to, for example, make predictions about what that person is going to do.
*  Another example would be, you know, when kids are shown, kids can discriminate between whether an acting agent is is helping another agent or hindering the other agent.
*  And so, yeah, there are these psychological aspects of other agents that can easily be inferred with this sort of developmental startup software.
*  Yeah. OK. And then the rest of the other three ingredients kind of fall under what you describe as model building elements.
*  And one of them is this comp and you've listed all these already.
*  You've mentioned these in passing. So one is copies and compositionality.
*  And this is basically where you can build new things from simpler parts.
*  And so deep networks.
*  And let's just run through these real quick and then we can kind of talk about them more broadly, maybe.
*  So deep networks are not great at this.
*  Another is learning to learn or meta learning.
*  And so there's actually a lot to talk about with this, probably.
*  And and causality is the last the fifth ingredient and building causality.
*  And I talked about this last episode a little bit with Conrad Kurding and you want to modernist go his wife because they just wrote a paper on how to infer causality and quasi experiments.
*  So it's a little different. OK.
*  So like I said, this is a roadmap and it's like the paper was written and then learned meta learning work immediately came out of DeepMind.
*  And then I don't know if you recently I didn't get a chance to read the paper, but there's this recent paper out of DeepMind as well that is using the meta reinforcement, their meta reinforcement learning framework to build in causality to.
*  Yes, it's written by my student.
*  Oh, is that right?
*  Yes, well, I should have some internship at DeepMind.
*  OK, very good. Yes.
*  It's funny because in the paper and one of the rebuttals from the people at DeepMind, they're like, maybe we are on a converging path here.
*  And so I suppose you are.
*  We're definitely there's definitely points of convergence, not not completely.
*  But I mean, I I talk to those people on a regular basis, so it's not we're not like, you know, in conflict or anything.
*  Oh, of course not.
*  We're all going for the same goal anyway.
*  So so I don't know if you want to if any of those that you want to really elaborate on as something that, you know, I'm kind of curious your take on how the paper has continued to be received over time and how people, you know, if you've seen a lot of progress in all of these domains or what's really still lacking, et cetera.
*  Yeah, I think I think that there's been a ton of progress.
*  I think that as I was saying before, many people have begun to acknowledge that you need to build in some constraints to get these systems to work appropriately.
*  Now, we're certainly not there yet in a lot of practical areas of application.
*  You know, for example, we we still, I think, can't get systems to make reasonable captions for images.
*  They just the fact of matters, they just don't really understand what's going on in the image.
*  The barrier of meaning, but they make reasonable captions, you know, five out of seven times maybe now.
*  Is that a good?
*  I don't know.
*  I mean, not my experience.
*  Okay.
*  Yeah.
*  Anyway, but the point is just that these systems can sometimes fool us into thinking that they know more than they really do.
*  And yeah, so so I'm encouraged by things like the paper you mentioned, meta learning for causal inference.
*  I think that those kinds of approaches are definitely on the right track.
*  I don't know to what extent the particular basically the thing that I.
*  Wonder about is to what extent building exploring in the space of kind of different neural network contraptions and putting in different kinds of widgets and so on is going to get us to intelligence.
*  Sometimes it feels a little bit like building a ladder to the moon.
*  Doing more of the same that didn't get us there initially.
*  And yeah, well, it's just it's just certainly there's no doubt that there's been a huge amount of progress, but it also I get the sense reading these papers that are not necessarily the same.
*  That we're kind of swirling around a local optimum, and every once in a while we kind of pop out of that and go a little bit farther.
*  But the developments don't seem of the sort that are really getting a significantly closer to human intelligence.
*  So it's just.
*  To give one example.
*  Think about.
*  Alpha Go Alpha Go is.
*  An amazing accomplishment.
*  I love everyone has to always preface it with how amazing it is and then yeah yeah yeah yeah well it's an amazing accomplishment there's no doubt about that.
*  But just think about what happens at the end of a of a go game.
*  You know, you just shut it down because of the go can only play go and that's in some sense true of almost all the models that we have now and even.
*  Even within the space of let's say video games so we have algorithms that can play video games, but you can make.
*  Changes to those games that would be completely trivial to a human player and yet would be catastrophic to these algorithms.
*  Yeah, so we're really far away.
*  I think in the sense of capturing that human like flexibility and I and I think it's because we haven't fully embraced the principles of causality and compositionality and intuitive theories and so on.
*  I think I think I guess my general impression is that we have this really useful tool that we can build these gadgets out of neural networks that do things and you if you can feed it enough data they can.
*  You know classify images or recognize speech, but it's tempting to kind of over apply those things as a substitute but really thinking hard about the structure of a problem.
*  But it'd be fair to say that that it's a sort of a change in quantity when you're adding these sorts of widgets etc to the deep learning networks and not quality.
*  Yeah, yeah, I think that most of the advances that we see on a day to day basis are about like you know getting a few more decimal points score on some benchmark data set but you're not really you I think the real contribution of cognitive science is to get people out of the thinking in terms of.
*  Get people move people away from thinking in terms of these benchmarks and and or rather thinking about thinking more broadly about what the benchmarks really are.
*  What is it that you want the system to do it's not just about playing go or playing video games or recognizing objects there's some set of competences there that transcend those individual tasks and if you only kind of play to win those tasks then you're going to be missing something.
*  So we need to figure out where the hell we actually want the goalposts and pour concrete and then make them stick there.
*  Yeah, yeah, yeah.
*  So I asked this to a lot of my guests so I'll ask you as well is emulating the human mind is that you know is is emulating human thought and learning is that the only way to get there you think to to general AI to something that we would satisfy that would satisfy our notion of what generally is.
*  Well can I tell you what you're going to say before you say it yeah go for it you're going to say well it's the only example that we have it's the best example it's the most complicated you know the brain's most complicated thing in the universe.
*  Okay now go ahead and repeat what I said and I'll be sad.
*  No, no I wasn't going to say that actually.
*  I think it depends on what you mean by general intelligence because it could potentially be a tautology if we think that what we mean by general intelligence is whatever we think humans do then that's only going to be satisfied when we build machines that think like humans.
*  But we might not right maybe we'll eventually come to some way of thinking about intelligence that's really different from our own it's just it's very hard to get to that point because inevitably we project our own notions of intelligence onto our machines.
*  Of course.
*  But I mean one way to approach this potentially is from you know the computational level so we can always talk about David Maher and computational highest in level and where where would you start like the free energy principle for instance I think starts with existence itself right as the.
*  You know the fact that we exist and if you start at that level well then what's the for living things and what's the algorithm maybe that's is that evolution and you know I don't know is there is there a way to come at it from a really high computational level where then the algorithms could differ or you know for instance and then the implementation level below that could differ as well to get to that same whatever the actual computational level is of living in existence this is getting a little too deep.
*  I'm sure for the for the podcast but.
*  Well we I think that's absolutely right I mean there's some sense in which look at the very highest level it's to like do well at life right to survive and reproduce the imperatives of natural selection and so on.
*  But that as a as we were talking about before it's not very constraining on theories of intelligence at least in its most general form.
*  Yeah.
*  So.
*  We need to make more specific assumptions but but just to make this a little bit more concrete so even if I said all right and intelligent system has to reason according to Bayes rule then there's there going to be algorithmic constraints to grapple with the interactability of that in any large domain.
*  It's perfectly conceivable that a machine we could design machine learning algorithms that excel whatever algorithms humans are using because there's no reason to think that evolution is necessarily selected the best possible algorithm to solve these problems.
*  There is no best best is just what is existing at the time I suppose right.
*  Right well I mean yes so I'm saying within whatever particular niche you're looking at you could ask like what is the best way to solve this problem and humans might not have achieved that.
*  So for example, people might engage in some kind of tree search to solve planning problems, or they might engage in some kind of like variational optimization to solve inference problems, but the particular way in which they do that might not actually be the optimal way.
*  And we could we could design machine learning algorithms that do better than humans.
*  Now they're still trying to they're designed to achieve the same goals that humans want to achieve and the overarching architecture of that system is similar, but it's doing it differently right so that's that's a concrete way in which it wouldn't even make sense at that point to demand that the machines adhere slavishly to make no sense.
*  What humans are doing right yeah yeah so I mean I the reason you know I told you what you're going to say I mean that was a joke obviously but so many people have said that you know they can't imagine another way and my intuition is that wow you know if you ask a hundred experts and they all say no way we have to do it this way it must be the other way you know.
*  I can't imagine another way but I can imagine right there being another way in the same way that I was very struck by I think this has very deep implications for how we think about ourselves and our own thought processes so I attended a dinner once and I talked to this geologist who was working on earthquake prediction.
*  And he made the very vociferous point that he felt that the classical education in geology had ruined generations of geologists because the classical models simply could not accurately predict earthquakes like tectonic plate shift models or this is what he said I'm not a domain and he didn't really go into the details of why that was that you could have sound geophysical principles that were not actually useful at making predictions.
*  And he argued that this whole thing was blown wide open when people started to use deep learning to predict earthquakes and he felt that whatever it is that we thought we knew about geology you know even if it was right maybe there are more correct theories of geology that are expressed in some inscrutable language that the deep learning system can discover and eludes us.
*  And I have a hard time swallowing that but at the same time you have to acknowledge the possibility that it's our hubris as humans that convinces us that the nature of the universe has to be expressible in the language that we have at our disposal right now in the scientific language in current use.
*  I mean this is something that historians of science have known for a long time that our theories are strongly latched to our description languages and even our basic observations can't be described in a theory independent way when our theories change our observations change we actually see things differently and so that's reason for humility in terms of privileging our notions of intelligence.
*  Right right well in that same vein I had John Krakauer on the show a few weeks ago and we were talking about different levels of explanation and you know we talked about reductionism and the proper level of understanding phenomena and there are lots of like higher cognitive functions that it may not make sense to try to understand on the level of neurons and neural circuits right.
*  But instead on the level of some behavioral function and so on and the like the core ingredients that you guys mentioned in your paper confer like these advantages right they make humans so awesome in various ways and I'm wondering you know could there be disadvantages to.
*  And there have to be right that that's the yin and yang of the trade off.
*  Yeah so that's what I was thinking too is like you know let's say it is possible you know we can map some of these differences in the way that we can understand the nature of the universe.
*  These higher level cognitive functions to the level of neural circuits you know are we humans but you know because we need to reduce complexity using things like compositionality and intuitive physics are we incapable of conceiving.
*  How that mapping could occur whereas like a deep learning network or some sort of a system without these human like skills quote unquote or limits might by brute force figure it out in a way that we could eventually be satisfied with that kind of explanation you know does that does that make sense.
*  Yeah so I wouldn't say that people are incapable of doing this since historically we've been very capable of constructing various kinds of cognitive prosthesis that allow us to understand things that seemed mystifying before.
*  That being said it's certainly a logical possibility that neural networks could discover these theories maybe more easily than us because they have different inductive biases than us.
*  I certainly think it's within the realm of possibility to think about neural network scientists that are as different from us as we are from you know dogs and cats.
*  That being said I think my experience in studying these systems is that in some sense there's always less than meets the eye that we have this strong inclination to kind of anthropomorphize these systems and attribute to them psychological competences that they lack.
*  And when you start to really test these rigorously they fall short.
*  I mean this is very clear in the domain for example of natural language where most natural language processing systems simply don't recover the same kind of semantic understanding of the world that humans have.
*  It's not that hard to demonstrate this.
*  So I just think that while it's a logical possibility I think we need to be doing more than just training neural networks on ImageNet for like you know data set.
*  Even data sets on reasoning from natural language I think are too impoverished.
*  It's really a privilege to be able to be at the point where we can say that and you know that there have been these advances right that are amazing and now we can say it's not enough.
*  That's great. I think that's a great place to be in.
*  So I can imagine like lots of different scenarios for this path toward fuzzily what we could call general AI.
*  And reading your paper brought just one to me this one scenario and as soon as you write this in a science fiction book it means it's going to be completely wrong.
*  But so you know I can imagine and you know the way I sort of envision it is what we're building toward is an AI system that comes off the shelf or out of the box.
*  And it's ready to solve new problems and learn new things efficiently and have some of these built in ingredients right that are proposed in the paper.
*  I can also imagine a scenario though where we have this sort of an in between phase where we have to build these machines that then we set out into the world like with little embodied cognitive architectures.
*  And then we have to wait for them to gather enough different kinds of data and experience that we can't build into them.
*  You know do you think that's a possibility that we'll go through this phase where we're you know taking these these bots these robots and stuff and then letting them be for a while and then we can use them for instance.
*  Then then their general domain general enough that we can actually use them.
*  Or you know can you imagine that kind of scenario.
*  It's a ridiculous question.
*  Yeah I mean I don't see why not although of course there's all sorts of ethical and practical issues sure are setting loose robots in the world.
*  It depends what kind of constraints we put on them and what kind of challenges you know do they have to enter the workforce and work for their.
*  Definitely definitely for me anyway.
*  Yeah.
*  So I came up through neurophysiology in my graduate work and my postdoctoral work and this podcast I made has the tagline where neuroscience and AI converge.
*  But I always have thought of and and I'm only starting to not think of it this way.
*  I've always thought of cognitive science as a part of neuroscience that neuroscience sort of subsumes psychology even you know.
*  It seems to depend on whose definition you like of these things.
*  But so this paper was written in a real from a real cognitive science historical perspective and modern day sense of cognitive science.
*  Do you think that we're in a cognitive science resurgence sort of over over neuroscience.
*  So there is a lot of hype in neuroscience right.
*  We're going to figure all this out and now cognitive is cognitive science coming back now and saying whoa whoa.
*  You know this is the way to go.
*  Are we in this resurgence to understand how how to understand the brain and how to program machines that think like brains.
*  It depends who you ask.
*  I mean there's certainly still people who argue very strenuously that neuroscience is really important for building intelligent machines.
*  I just I don't think either for cognitive science or for neuroscience psychology or neuroscience.
*  They're both in some sense very dependent on our computational notions.
*  We need ideas from machine learning and other disciplines technical formal ideas to interpret both psychological and neural data.
*  I don't think it's the case that we've gotten a lot of mileage out of just looking at those data and from that extracting algorithms that we can plug into machine learning systems.
*  I just don't think that's how it really works.
*  People have different arguments about this of course.
*  Yeah so let's kind of transition.
*  I just have a few general kind of broad questions for you and then we'll then I'll let you go.
*  OK we'll see how you perform on this one.
*  So in the spirit of human compositional skills and our ability to produce infinite things from a finite set of things.
*  Can you say utter a grammatically correct English sentence right now that you think nobody has ever said or written.
*  Sure. Yeah.
*  I don't think that.
*  I mean you could do any variant of Chomsky's classic sentence colorless green ideas sleep furiously.
*  You could have them sleep quiet sleep effervescently effervescently colorfully.
*  The adverbs it's the adverbs that allow you to do this.
*  Yeah. Yeah I think it's pretty straightforward to do that.
*  OK.
*  I could you know I could say the sentence I don't believe that Chomsky said that colorless green ideas sleep furiously.
*  I bet that's been said but we'll see.
*  I'll let someone can Google it.
*  OK so often when we're stuck and need to figure out the solution to some sort of problem we need to step away from the problem.
*  Right. You can't just like you're at your desk you're trying to figure the thing out.
*  But it's only later when you step away that the solution comes to you.
*  And often like immersing ourselves in a like long form complicated novel for instance can lead to more creative ideas than like reading a summary of that novel.
*  Right.
*  Presumably because we need to sort of steep in that mind frame for longer.
*  Let the things bubble in our minds.
*  Do you think that there's something about time scales in this.
*  I thought you might be going to this when you're talking about your your dinner with the with the geologist.
*  Is there something about time scales and dynamics and processing time that is important for how we think and learn and how maybe machines might need to think and learn.
*  So thinking of the idea is.
*  Can like the the the geological formations right there moving and they're they're a dynamical system.
*  Could we if you stepped back on a really slow time scale would those look intelligent.
*  Could we make the case that those looked intelligent.
*  Right. Or is there something special about the millisecond processing times of our brain that gives rise to intelligence and that we need to consider when building machines.
*  I don't think so.
*  I mean.
*  It's not entirely clear whether you mean that the.
*  The time scales refer here to the time scales of computational processing versus the time scales of events unfolding in our world.
*  I could clearly we can reason about events that happen on vastly different time scales even though the time scale of our neural processing is fixed.
*  I didn't say I asked they're going to be good questions or well constrained.
*  Yeah I mean I think that there's something important about.
*  Time scale but I'm not sure what it is.
*  I mean it is an intriguing question why thinking over long periods of time would help you.
*  What is one idea that you seemingly you have time to do all your ideas but what's one idea that you either don't have the resources or time to tackle that you wish someone else might pursue.
*  Yeah well a lot of my questions about the brain really need to be answered in animal models.
*  And although I do human experiments in my lab I don't do animal experiments and so.
*  Typically I try to farm out those animal experiments to other labs that do that kind of research and that's been no no pun intended.
*  That's been very fruitful for me to answer questions for example about the nature of dopamine processing.
*  So there's lots of questions like that I mean often the kinds of experiments that we do we we often try to design them in such a way that both humans and animals could do those tasks.
*  And then eventually eventually try to port them over to animals and there's some you know process of convincing animal experimentalists to take on that challenge.
*  Well they're busy you know things going on.
*  Well it's not just they're busy I think they're also they're conservative understandably because it takes a long time as you know to train animals.
*  That's what I mean they're busy yeah they're steeped in their two year other other experiment.
*  If you could bet on a single discipline or sub discipline that will that will break open our understanding of the human mind.
*  What would it be you could say cognitive science physics astrology etc.
*  Well I feel like the longer that I do this stuff it just seems that the more everything kind of converges that we already talked about how.
*  Physicists came up with this idea of free energy that then got picked up by computer scientists to develop efficient inference algorithms that then got picked up by neuroscientists to think about the brain.
*  Yeah I mean these are all these things are intertwined they're they're deep.
*  With formal and metaphorical relationships between all these concepts and so I really like what Sherlock Holmes said that to understand nature your mind must be as broad as nature.
*  That's how I feel like really the study of intelligence is that in a nutshell you need the intelligence is drawing upon all of these different disciplines and ways of thinking.
*  So in that vein keeping one's mind as broad as possible do you have a advice that you would give to you know say a graduate student or an undergraduate student.
*  Interested in these topics and just wanting to start out in the arena like what how to how to move forward.
*  Yeah I think it's hard for students to follow the path of greater resistance because they look around and they see what's happening in the world.
*  What's successful what's not successful and it's natural for people to gravitate towards the things that they perceive as being more successful.
*  But the paradox is that to be really successful to really make a difference to change the way people are thinking to change the course of scientific discovery.
*  You have to swim against the current you have to pursue ideas that are not popular that people might not agree with that might not really make sense at first.
*  You have to befriend the crackpots and read poetry and you know take a little bit of a break from the past and then you know start to think about what's going on in the world.
*  And so we have to be really attentive to the unappreciated importance of uselessness.
*  Oh that's a good quote. I'm tempted in there but I'll I'll I have one more question for you here.
*  So yeah well AI is a very important part of the science of science.
*  sauce.
*  feel like I can really give a good
*  that
*  I
*  So in my view, consciousness is a little overrated.
*  Bam!
*  All right.
*  Well, I know what I'm thinking.
*  I'm feeling grateful and thinking I'm glad to have you on the show.
*  So Sam, where should people go to learn more about you?
*  Well, they can look up my lab webpage and if they're interested in reading my papers,
*  that's where they all are.
*  Very good.
*  That'll also be linked to in the show notes.
*  So thanks for your time, Sam, and continued good luck to you.
*  Yeah, thanks so much, Paul.
*  Take care.
*  Thanks for watching.
*  I'll see you next time.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.
*  Bye.

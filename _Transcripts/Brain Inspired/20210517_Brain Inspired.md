---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 3704s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 6600
Video Rating: None
---

# BI 105 Sanjeev Arora: Off the Convex Path
**Brain Inspired:** [May 17, 2021](https://www.youtube.com/watch?v=CGiouXjdpmE)
*  When we used to look at it, you know, 30 years ago when I was in grad school, we would look
*  at these very difficult computations that were needed for deep learning and we would
*  say, this can never happen, you know, this can never work.
*  Now it's clear that the model is fine and it's just we had a very exaggerated view of
*  complexity.
*  I'm actually delighted and amazed how much progress we've made in six or seven years.
*  This is a shock and awe result to make you completely realize that all the old ways that
*  you've thought about, you know, that this is optimization and so on, is just not correct.
*  Neuroscience is potentially even more open.
*  Why not go to neuroscience then?
*  Too hopeless?
*  Yeah, it seems much more difficult, right?
*  So with deep nets, it's clear that they work for many settings and so you can run experiments
*  and see what works and doesn't work and so on.
*  With neuroscience, they're doing a lot more shooting arrows in the dark and it feels like
*  from the outside.
*  So it seems much more challenging.
*  This is Brain Inspired.
*  Hello, it's Paul.
*  Usually guests on this podcast lean toward the neuro side of neuro AI.
*  Their expertise is on the neuro side.
*  But today we have someone who doesn't really have a neuroscience background, but a heavy
*  math and computational complexity and computer science background.
*  Sanjeev Arora is a professor of computer science at Princeton.
*  In fact, he's won numerous prestigious awards for his work in computational complexity and
*  computer science and he co-authored the textbook Computational Complexity, a Modern Approach.
*  But in the last handful of years, he's turned much of his attention to machine learning
*  and deep learning theory, partly at least because deep learning poses a challenge for
*  mathematics.
*  Basically, that challenge is to understand why deep learning works in a theoretical and
*  a mathematical sense.
*  So deep networks are really over parameterized, which means that there are way more parameters
*  in the model to fit than there is data to train the model.
*  So the traditional story in machine learning would suggest that deep nets shouldn't work
*  as well as they do, but they do work.
*  So it's a question, why does gradient descent work?
*  Why do deep nets generalize as well as they do, when they'd be expected to overfit?
*  One of Sanjeev's takeaways from studying deep learning theory is that optimization, that
*  language, the way that we normally think about how deep networks learn, isn't the right way
*  to think about how deep nets learn.
*  So just to elaborate on that, we think of deep nets as learning solutions by minimizing
*  some objective function, minimizing error, and doing it as efficiently as it can.
*  Instead, Sanjeev thinks that we need to focus on other factors to explain how training works
*  in deep nets.
*  And similar to Omri Barak, who's been on the show, and Andrew Sachs, who was on the podcast,
*  Sanjeev thinks that we need to pay more attention to the training algorithm itself and the learning
*  trajectories, the process of learning that occurs as a consequence of the training algorithm.
*  That those determine the solutions, not the objective function itself.
*  Okay, that's a little heavy, but I wanted to introduce that overall idea a little because
*  the discussion that we have goes kind of fast, I think.
*  But with that little bit of background there, we talk about two lines of his theoretical
*  work that support this claim by doing surprising counterintuitive things, essentially.
*  Something people often do in deep learning theory is test what happens when you push
*  things to their limits and even beyond their limits.
*  One example of that is to see what happens when you make the layers in deep nets really,
*  really big.
*  When you do that, when you push them toward infinity, you get a situation where the space
*  of possible solutions goes toward infinity as well.
*  So we talk about that situation where, surprisingly, gradient descent, the common training algorithm
*  used in deep learning, still finds a solution among those near infinite possibilities.
*  In the other example we discuss, Sanjeev and his group play with the learning rate of the
*  training algorithm, which controls how big of a step to take while learning within each
*  training iteration.
*  And they show that doing something a little crazy with the learning rate, increasing it
*  over the course of training, which is the opposite of what is traditionally advised,
*  that that still works also taking larger and larger steps instead of smaller and smaller
*  steps.
*  So we discuss all that.
*  I get some of his thoughts later in the podcast on neuroscience and the prospects of understanding
*  how brains work.
*  A little spoiler, he's not as fanatic about the recent hoopla around using deep learning
*  networks to understand brains.
*  We begin the conversation talking about his previous life as a computational complexity
*  theorist.
*  We do really just scratch the surface of many topics actually.
*  So I link to a couple papers and talks in the show notes for you to learn more, which
*  I encourage.
*  That's at braininspired.co.
*  slash podcast slash one oh five.
*  If you value this podcast and you want to support it and hear the full versions of all
*  the episodes, you can do that for next to nothing through Patreon.
*  Go to braininspired.co and click the red Patreon button there.
*  OK, here's the conversation with Sanjeev.
*  I feel like I was sent here to help you along in your eventual transition to neuroscience.
*  So we'll see how far along I get in that.
*  So you have this blog called Off Convex and you wrote about four years ago, you wrote
*  on that blog, quote, deep learning holds many mysteries for theory.
*  So first of all, why the name off convex?
*  And do you think that sentence still holds now that it's four years old?
*  Yeah, so the name off convex comes from off the convex path.
*  And six, five, six, seven years ago, when I got into this field, machine learning theory
*  was primarily focused on convex models, convex learning models, and then the optimization
*  and all the analysis is much easier.
*  And so I wanted to get off that path.
*  What is the what is a convex model?
*  And we'll get into this a little bit more deeply, but just the overarching idea.
*  What's a convex versus a non convex model?
*  OK, so a convex model is where if you look at the parameter vectors or think of the model
*  as a parameter vector, the vector parameters, if you take two different models and take
*  the average, the average model does at least as well as average performance of the two
*  models.
*  And so that makes the math of optimization much easier.
*  Yeah, OK.
*  I mean, the first thing that I the major thing that I want to ask you is how your work on
*  computational complexity, which is kind of your background and where you cut your teeth
*  on all this stuff, how your work in that and theoretical computer science has influenced
*  how you approach and think about deep learning.
*  So you became an expert in computational complexity.
*  You've shifted your focus over, I don't know, the past decade or so to algorithms.
*  So can you explain the shift in your interest?
*  Actually, algorithms, I was doing way before that, too.
*  In the past decade, I've switched to machine learning and especially deep learning.
*  That would be the shift I would say.
*  So computational complexity is concerned with showing that problems are hard.
*  And maybe in the popular expositions, it's not always clear to the reader that when we
*  mean hard, we mean hard in the worst case, like for worst case instances.
*  So to give an analogy, like if we are thinking about learning problems or classifying images,
*  which is something we do very easily and deep nets now as well, you would phrase it as a
*  computational problem for complexity theory using worst case instances.
*  So those are not any images that you've seen.
*  They are like some very crazy classification problem, some jumble of pixels, essentially
*  cryptographic or something like that.
*  So it would not correspond to anything that we consider computer vision.
*  So that was computational complexity.
*  And it has amazing insights and helps things like cryptography and so on.
*  But it wasn't clear to me that it was so relevant to machine learning because problem instances
*  in machine learning have a lot of structure.
*  And so when I got my feet wet in this field, I quickly realized we did some work in the
*  topic models and so on where it was clear that there was a lot of structure in the problems
*  that you could leverage and come up with provably correct algorithms.
*  And so that was an aha moment for me that there was something different going on in
*  machine learning than what I'd been used to.
*  And it seemed like a very intriguing question to understand machine learning.
*  I mean, was it difficult to pull yourself away from the depths of computational complexity?
*  I'm sure you're still working on those problems as well.
*  No, actually, I don't work so much on computational complexity for the last seven, eight years.
*  Do you think about it still, though?
*  Because I mean, do you think about things through that lens in general?
*  Yeah, you can never get away from who you are.
*  So you are the sum of all your experiences, just like a machine learning model.
*  So yeah, so certainly it does inform how you look at things.
*  Well, I wanted to ask you and we'll talk more about brains and neuroscience later.
*  But I just wanted to ask you right off the bat how you view the current state, if you have a view,
*  how you view the current state of neuroscience and just how you view brains and their function in general, given your background.
*  So it's been a fascinating process to discover that as well, you know, what's going on.
*  I guess the interesting things that I've learned about the brain have to do with more a higher level than about things that are at a higher level than neurons.
*  Because, yeah, you know, for ever since I've been in science, right, one hears about neural nets and the neural inspiration.
*  And that part is not as developed as what I was surprised to learn, you know,
*  that we really don't understand neurons and their precise functioning and so on.
*  The real neurons, you mean?
*  The real neurons, yes.
*  And but there's this entire world of, you know, fMRI and all kinds of other imaging, which is fascinating, which is a higher level,
*  which has been which I really didn't know about 10 years ago so much.
*  What do you think about fMRI?
*  Because I'm a neuroscientist and I look at an fMRI picture and I think, eh, that's where it happened.
*  That's where something that's where oxygen is increased.
*  It's like the limits of I don't know how much it really tells me or what it explains.
*  It explains almost nothing.
*  So correct. But then you contrast it with, you know, the very elementary questions about neurons and what they're doing, which are still open.
*  Yeah. And for very good reasons, right?
*  How do you actually see them in action and so on?
*  Right. One of the reasons I was asking is because I think with the deep learning boom and I guess hints of this were on the horizon beforehand even.
*  I don't really know, but algorithms are the popular kid on kids on the block here these days in neuroscience.
*  And so you're right in the popular vein of how to understand deep learning and how to understand brains, I think.
*  So you think algorithms are are where it's at, huh?
*  Yeah. So I guess what I would say is that the the model is a model, right?
*  Which, you know, is it has a few rules and it's not so complicated, right?
*  So those are kind of like the elements, right?
*  Or atoms, maybe. And then you put it together and something emerges.
*  And what emerges is really a result of the training algorithm.
*  You mean as in by model, you mean individual neuron units or do you mean the.
*  No, the collection, the collection of millions or billions or more.
*  I see. Of those units. And it all gets trained.
*  And at this point, it's very clear that the training algorithm plays a big role,
*  maybe even the biggest role in determining what happens.
*  So, yeah, OK. That's what a lot of your work has been on.
*  And I hope to hope we get to dive a little deeper in that.
*  Looking at kind of the bigger picture still.
*  What do you find? What do you see as difficult about deep nets, you know,
*  with respect to the traditional optimization problems that you faced in computational complexity work that you've done?
*  Yes, in computational complexity, even the simplest problems are difficult, you know,
*  like optimizing a cubic polynomial is difficult, you know, and be hard.
*  So. So with worst case complexity, you really don't get very far.
*  So when when we used to look at it, you know, 20, 30 years ago, when I was in grad school,
*  we would look at these very difficult, nonconvex computations that were needed for deep learning.
*  And we would say this can never happen. You know, this can never work.
*  There must be something wrong with the model. But now it's clear that the model is fine.
*  And it's just we had a very exaggerated view of complexity that, you know,
*  that these models can be trained with very simple algorithms.
*  Is it because you were looking for exact solutions? I mean, that's sort of the goal, right?
*  No, the issue is what I mentioned earlier about worst case complexity.
*  So when I say that, you know, optimizing a cubic polynomial is difficult, it's on some very artificial data set.
*  So, I mean, you said that a central goal of complexity theory is trying to prove that some algorithm is the most efficient
*  to compute some task and that a better algorithm doesn't exist.
*  So how do you how do we think about that in deep learning?
*  Is it provable or have you just come to accept that, you know, given an objective function,
*  given an algorithm and given an architecture that we that we can get there?
*  OK, so again, in computational complexity, those nice, exact understanding that you hear about
*  is very much of a worst case type, namely that for this computational task,
*  there is this algorithm which achieves a certain performance.
*  And then there is some set of instances, some family of instances where doing any better is NP hard or whatever, NP complete.
*  OK, so it just shows that, you know, there exists a set of very adversarially chosen instances for which it's impossible to do any better.
*  But it could be that you go out in the real world and pick up instances and all of those,
*  you could do much better than this theoretically best algorithm.
*  Yeah, so we know of such cases.
*  So that's why that's where I came from, that I was very interested in this phenomenon that real world complexities is quite different from what complexity theory gave us.
*  And so do you do you see deep learning as capturing that real world complexity and as sort of middle middle ground?
*  So if if if zero is best case scenario, right, and NP is worst case scenario, where is deep learning in that scale?
*  Well, it's somewhat still of an open question, but clearly the experimental success cannot be denied.
*  Right. So it's clearly for many learning tasks, it does work just on a broad scale.
*  Also, how has your view of deep learning changed over your career?
*  So you sort of got you did some machine learning work and then your interest gradually, if I'm correct, transition to deep learning.
*  Did you see it as a what, you know, as a super difficult problem theoretically to tackle at first and now you're making headway.
*  And and and so, you know, you see it as promising now or, you know, how has that changed?
*  How has your thoughts changed about deep learning?
*  I got into deep learning and thinking about deep learning actually before the Hinton paper,
*  because I met Jan LeCun.
*  I invited him to some workshop and we started chatting and it just made sense, you know, that that this is an interesting model and we should look at it.
*  And then the Hinton work happened and of course, the entire world was on it.
*  So, yeah, so I was very open to deep learning.
*  Even back then, you know, it made sense.
*  Or maybe Jan is just very persuasive about what back then was.
*  But in terms of, you know, how my views have evolved, it seemed like a forbiddingly difficult problem mathematically to to understand it.
*  And I'm actually delighted and amazed how much progress we've made in six or seven years, including here at Princeton, you know, amazing students and postdocs.
*  So it's you set the smartest people as young people in the world to work on it and amazing things happen.
*  One of the things I watched part of the the Alchemy is deep learning alchemy, that series that you hosted for the Institute for Advanced Studies.
*  And I hadn't realized that. So, first of all, there's this kind of well known, at least in neuroscience, big reproducibility crisis and reliability crisis of results.
*  I didn't realize that that was also there's at least a mini crisis or something in a I.
*  I mean, is that true? First of all, how do you see it?
*  And then I'm wondering if there are similar reproducibility crises, you know, just going back to the theoretical computer science side of things.
*  It seems like there would be less because it's more grounded in math and hardcore theory.
*  There would be less reproducibility issues in theoretical computer science.
*  I mean, theoretical computer science, usually the.
*  The proof that something works was mathematical, you know, so there was no claim that it would be the best algorithm in practice, you know,
*  and often for many problems, the best algorithm in practice would be something completely different, maybe something more like deep learning heuristic.
*  Anyway, but in terms of reproducibility crisis, one should be clear that.
*  It's not often the same type as in science, you know, like all social science.
*  Other people are able to reproduce the results on the same data set.
*  The reproducibility crisis is, you know, what the takeaway is.
*  Does that mean that that particular method that you introduce, you know, which on this benchmark gave five percent improvement?
*  Is that robust in other two other tasks?
*  So that's the crisis. So it's a little bit different.
*  You know, it's not the same issue like in the social science experiments.
*  Arguably, it was just bad application of mathematics.
*  And here it's just over optimistic takeaway from one experiment.
*  Well, I thought so in neuroscience, part of the problem is that you can't my lab can't reproduce your results.
*  You tell me what you did and I try my best and I can't reproduce.
*  And that from what I saw, that's also a problem on the same data set.
*  Well, generally not data sets. I mean, that's changing as open science becomes more open.
*  But I mean, there was one talk, Joel, I think, and we don't need to get into details, but you know, yeah.
*  She was showing, you know, you go on GitHub and there are one hundred thousand, you know, open algorithms that you can use.
*  And using the same algorithms, same hyperparameters, same everything that she could.
*  And she was getting different results, if I'm understanding that correctly, that there's some like the reporting maybe isn't as clean and as forthcoming as it could be.
*  Or maybe I'm missing something. I don't know. Am I missing something?
*  Yeah, there's probably I mean, there's probably a range of issues, you know, ranging from just.
*  Incompetent research to, you know, there's sort of a sliding scale of probably the issues, you know, such a vast field that she says hundred thousand or whatever codes.
*  But yeah, so and then she was talking about about reinforcement learning, which does have this issue that it's in some sense testing and training on the same set.
*  Right, right. So a maze task or something. Yeah, you test and train on the maze task.
*  Yeah, so that's sort of a special case. So where this I mean, where it starts getting to be kind of like the reproducibility crisis and social science and science.
*  But so in the in the non-reinforcement learning world, then the reproducibility issue is really just the conclusions aspect.
*  Like what can I use from this to build my own and and make progress?
*  Yeah. So, yeah, so we don't really have a science for.
*  For knowing, you know. Broad applicability, I mean, that's not part of the paradigm, right?
*  You just have a data set and you do well on it.
*  But how representative is that data set of whatever you want to do out in the real world?
*  OK, so that kind of gets into generalizability.
*  It's actually meta generalization, I would say.
*  Meta generalization. Yeah, that's right. Yeah, not the not the classic generalizability.
*  Yes. OK, so my second kind of main topic or question for us is just what you're discovering in deep learning theory.
*  You talk often about the the mysteries of deep learning, one of them being gradient descent, essentially that it works and that it can lead to a almost near zero error.
*  And the other is that deep learning networks don't overfit because classically, theoretically, they were thought or the assumption, I suppose, would be when you have something that is highly overparameterized, that it would overfit the data.
*  And there's this that's a classic assumption, I suppose.
*  So where do you think we are broadly in respect to those two mysteries?
*  And then we'll get into some of your work in particular.
*  Yeah, so it's clear that the training algorithm has a lot to do with it and also the data, right?
*  There's some structure in the data. So you put the two of them together and somehow things work.
*  And that's what we're trying to understand, that generalization happens and zero training error is achieved.
*  But I guess the mathematical difficulty in understanding that seemed fairly large, and at least there's been reasonable progress in the last five years or so of understanding,
*  albeit for simpler models, this trajectory of optimization and how it determines the properties of the final model and also why it promotes better generalization.
*  So you can see that going on with rigorous proofs in models that are somewhere between a full blown deep net, the kind that you would deploy and the classical models like kernels.
*  So there's some range of in between models where we've seen clearly what's going on.
*  And then in the real life models, just in the last couple of years, there's been a few papers from our group with grad student John Lee being a very key author in those,
*  which actually tries to understand this evolution of the model during optimization, you know, the trajectory mathematically for real life nets.
*  And there's some theorems and some mathematical understanding of what's going on.
*  How did you that's part of the take home lesson is that trajectories are more important than we used to think that they are.
*  We used to think that everything the only important thing was the objective function landscape.
*  Right. And to minimize, to find some minima in the objective landscape.
*  But what you have found and I've had I've had Andrew Sachs on the on the show.
*  I also had only Barack, who has been who considers the dynamical processes and the learning trajectories kind of as a prior on ongoing training.
*  And so there's a lot of interest in focusing on the learning dynamics and the trajectories.
*  Now, how did you come on to that?
*  Well, I guess it was clear from the experiments that, you know, something's happening during training.
*  So so that part was clear.
*  The question was how to understand it.
*  And what we and I guess some other people also in the field quickly lash onto is that you need this.
*  The only vocabulary we have for understanding that is evolution of these systems and, you know, basically in the gradient.
*  So this was studied in many settings and classical mathematics.
*  And so we sort of adopted some of that terminology and some of the works there.
*  I mean, that field isn't really developed enough, as far as I can tell, to help us directly with machine with deep learning.
*  Which field?
*  Like this, there's a there's a set of mathematical fields which are concerned with evolution of a high dimensional system or multidimensional system.
*  Under some kind of a differential equation like dynamical systems theory, for example.
*  But there are other fields like that, too. So like stochastic systems.
*  I mean, that's more directly relevant because in deep learning, you are doing stochastic gradient descent and that stochastic component as well as far as we can tell is important.
*  So, yeah. So so we've drawn inspiration from from those fields to analyze simple systems.
*  Do we have the right vocabulary or do we need to invent new vocabulary to understand these things?
*  I think the vocabulary is there. We need to invent new mathematics to to figure out what's going on.
*  So new concepts, essentially.
*  Yeah. Even new definitions.
*  Right. I mean, yeah, this has happened for hundreds of years in science that you are trying to understand new phenomena and you come up with new concepts, entropy or whatever.
*  And those are sort of very germane to the phenomenon.
*  You talked about understanding.
*  Do you think that there is more explanatory power in in understanding the trajectories to help us understand deep nets relative to analyzing objective function landscapes, for instance?
*  Oh, yeah, the landscape viewpoint is it can be very misleading because because think about deep learning, you start from random initialization.
*  And then you just follow the trajectory of gradient descent.
*  So it's a very you're sampling this landscape in a very special way.
*  Because thinking about so it turns out that most objective function landscapes have lots and lots of local minima that and so what you're saying is that you start you start randomly and you're bound to end up in one of those local minima among many.
*  And you're kind of stuck with if you start on on a bank, stochastic gradient descent is going to take you down to that local minima.
*  Yeah, but what I'm saying is that if you just OK, so the landscape view often just treats the landscape as a black box, like the objective as a black box, it's some function with some.
*  Differentiability properties and norm of the gradient, things like that, right?
*  Lipschitz constants. And that's a very.
*  Uninformative view of what's going on.
*  Whereas the.
*  If you're going to analyze trajectories, you.
*  You're going to do something more than that.
*  And that's actually more directly relevant to what's happening in deep learning.
*  Let's talk about two of the things that you've done to help open that black box.
*  One of the things I mentioned Andrew Sachs and one of the things that he and his collaborators have done, they've taken linear deep learning networks and made them.
*  Narrow, but essentially infinitely deep and you've gone the other route. You've made them fairly shallow, although I know that the results generalized to deeper networks as well, but made them infinitely wide so without getting super technical, I suppose.
*  You know what did you do to you know and and what did we learn from it using infinitely wide nets.
*  Sorry, so that's two separate things. So I presume that with Andrew's work, you're referring to something I like a lot. He started this thinking about linear nets and super wide nets are actually not linear.
*  Those are, you know, take your standard deep nets, you know, learn that or VGG and you let the width go to infinity.
*  Often normal deep net and so that's different model. Yeah, so those are indeed the two models that people have analyzed very well linear models and very wide nets.
*  And the reason very wide nets are still kind of linear is that the analysis shows that when you follow the trajectory of training with an ultra wide net, it ends up being this neural tangent kernel.
*  And so that's which is kind of a related to the old kernel literature. So like in the limit of an infinitely wide net. It's a fairly simple solution that it generalizes to
*  Well, the optimization has a very simple solution and then generalization is a whole other ballgame, you know, to understand generalization of that kernel.
*  Yeah, I shouldn't have said generalization because I know that that's a huge term. But yeah. So what is that? What would we have? What would you have expected when you I guess you did expect this because you did the math beforehand before you did the empirical testing of the infinitely wide nets, right?
*  Right.
*  Well, okay. So the reason we came up we meaning the field came up with this notion of an infinitely wide net is that it was clear that with deep learning in practice, you can use very wide nets like
*  the wide resnet and, you know, make the width really a lot and still and they do even better. Okay, so doesn't hurt optimization doesn't hurt generalization. So
*  it was clear that there's something going on during training, which makes overparameterization or over provisioning
*  not so bad or even beneficial. So, so I was encouraging my students and postdocs to look at that. I'm sure this was happening in other groups to that.
*  Let's look at
*  the one the model I was suggesting was student teacher net that the data is generated by a teacher net, which could be fairly small. And then you're using a student net, which is much more over provisions
*  compared to the teacher to learn to classify as well as the teacher using the teachers data. So that was a model that several people were interested in. And then from there, it went to infinitely wide.
*  Is it counterintuitive that that the optimal solution resembled a the kernel that you were talking about? I mean, is there is there is it surprising? What would we have expected without doing the math? What would we have expected if we made our layers infinitely wide?
*  Well, without the algorithm without the training algorithm, infinitely wide nets really don't make sense because it can fit in everything. Right. So they were defined exactly because you know, empirically was noticed that you could very over provision the neural net, the learning net, a lot and it doesn't seem to hurt performance. So it was clear that or it felt like
*  there should be some interesting structure there. And you always hope when you go to the infinite limit that it becomes easier to prove things as has happened in math a lot.
*  You talk about the thermodynamics as a inspiration for that as well.
*  For example, yeah. But there are many other examples we're going to the infinite limit gives you some new insight. So so that was the natural reason to look at it.
*  Yeah, I guess the reason it's not clear within infinite net is because you're training it. So it's not it could go either way, you know, it could it could devolve to the infinite behavior, which can fit anything and sort of meaningless. But because you're training with a particular algorithm, it could be an interesting model. And that's what it turned out to be.
*  Does that mean so training on an infinite net does and I know that we don't want to talk about objective function landscapes. But does that entail infinite minima mathematically?
*  Right. So the net is not infinite. It's just going to infinity. So you're looking at the limiting process as you make it bigger and bigger. And in the the landscape has all kinds of things going on, which are not interesting because it's just going on this way.
*  Or one class of trajectories and those turn out to be well behaved. So it's just a stark illustration of what we think is a broader phenomenon that should be studied for deep nets.
*  So another thing that you did that seems counterintuitive is is you took the learning rates and grew them exponentially. So classic deep learning you start with a fairly high learning rate to bounce around and get out of local learning.
*  Let's say from the objective function landscape perspective. And then you gradually lower that learning rate or you can give it as cooling so that you settle in and instead of bouncing around a minima, then you actually settle in and reach the minimum through the learning process.
*  But but you guys have shown that you did the opposite. You grew the learning rate exponentially as you trained the models and still settled on the same learning rate.
*  Yeah, that was that was a huge surprise. And that's this work with a grassroot and generally, I mean, he's the main author in that series of papers. And yeah, the idea there was that when we were firstly trying to understand batch normal normalization, which is a very important technique in deep nets.
*  That you basically are putting in some kind of normalization at each layer. The details are not important for this conversation. So that and that behaves that makes the net better behaved. And that was actually key to to the many of the deep learning successes.
*  That's norm.
*  That's norm was yeah, to making large scale deep learning work, including resonance, which go very deep. And so so it's clearly an important phenomenon. And what this is, it's a very important phenomenon. And so it's a very important phenomenon.
*  go very deep. And so so it's clearly an important phenomenon. And what this work showed, you know, and we do trajectory analysis over several papers, is that once you have batch norms, you cannot really think of the training in the traditional way that people think about
*  optimization. You know, like what you just said, you know, local minima and, you know, jumping out of the wrong way. It's the wrong way to think about it.
*  All right, I'll change my vocabulary.
*  Yeah, so yeah, I'm, I don't know a good vocabulary either for this bizarre new world. But yeah, one of the things that we were discovering various things, and you try to come up with one phenomenon that catches people's attention and makes them stop and, and that, and so
*  that exponential learning rate was one that you can that learning rates really per se have no meaning. Once you have batch norm, that learning rates, you can mathematically show really is no different from scale of initialization, which you know, people don't think is such a big deal.
*  You know, when you initialize randomly the deep net, you use a certain scale, and it's just related to the scale of initialization. And so there's nothing more than that. You know, whereas people think that you tune this learning rate and things happen later on, which are magical, they don't think that it's just like the initialization, which they don't think of as such a big deal.
*  And so you can even have the learning rates, increasing exponentially and optimization works, probably.
*  Is this an example of the whatever, you know, I don't know if crisis is the right word, but just one of the fallacies in the machine learning and AI world, deep learning world, that, you know, we, we, everyone should just start with a high learning rate and decrease.
*  So the conclusion was not merited. Is this an example of that?
*  What ironically, in the follow up paper with John and other students, we actually show that you can actually train with very low learning rate all along.
*  Yeah, so it just, it just violates all standard ways of explaining what's going on in deep learning. So that's all. That was the point, you know, I was at a workshop right before the pandemic started with Jan Likhan, Yoshua Benjo and others. And I briefly presented this work. And Yoshua said, so what's the takeaway of this?
*  Right.
*  Like, what should I learn? So I said, this is a shock and awe result to make you completely realize that all the old ways that you've thought about, you know, this, that this is optimization and so on. Is this not correct? That's, that's the main takeaway.
*  Well, that's not very prescriptive.
*  I mean, should we get rid of batch norm? Is that one?
*  No, no, not at all. No, it's just showing that, you know, so it's going back to the themes we've been discussing that, you know, that the old way of thinking about deep net training, you know, was using this optimization view and the landscape and the first order minimum, second order minimum. And that just doesn't fit what's going on in deep learning.
*  You know, just accepting that is a big step forward, right? Because if you're thinking in a way that really is not a good fit, then you cannot discover the truth.
*  You have to admit your addiction to start to treat it, I suppose.
*  Something like that. Yes.
*  So do you so when you're in a talk and someone starts talking like I was talking about objective landscapes, do you take a quick catnap or do you actively do you throw a tomato or do you boo them? What happens?
*  Well, no, I wouldn't boo them. But yeah, I lose interest.
*  Okay, because they're not hitting the right because you know that it's off of what will what will be useful theoretically to move forward in deep learning. Is that the case?
*  What useful as you say, you know, like useful is when you change, you know what everybody's doing, right. But in terms of it's clear that that's a very that vocabulary, the classical vocabulary is not a good fit to what's actually happening under the covers in deep learning.
*  Now, what we do with that realization, you know, whether huge new inventions come out of it is it still remains to be seen. But certainly we should remove the cobwebs from our mind as my some college teacher of mine used to say every 15 minutes, let's remove the cobwebs from our mind.
*  So keep the beginners mindset.
*  Yeah, yeah.
*  How did how did Jan and Joshua when you, you know, when Joshua said, you know, what's the takeaway? And you told him this? What was what was their reaction? Were they accepting?
*  Yeah, yeah. I mean, they're very curious that all the classical ways of I mean, you know, they had a certain intuition about what's going on, that those intuitions are certainly very incomplete.
*  Do you like so from this vantage point, do you feel like this is just going to keep happening? You know, like, I guess the overall question is, where are we in the theory of deep learning? Like, how far along are we? How many more of these assumptions are going to end up just we're going to have to throw them out and accept a different way of viewing things?
*  So I think the often call theory of deep learning's goal is to open the black box. And there are several black boxes. So one is this whole what happens during optimization. And we're beginning to open that at least in simplistic models. And and with this like the exponential learning rate and so on, in actual, you know, models that people use.
*  But the other black box that we have not touched is the data, because the loss function depends on, of course, the architecture and so on. But it also depends on the data. Right. And that's what makes that mathematical function a black box, because we don't know what the data properties are. So that's the black box that has not been opened.
*  So this takes us a little bit toward, I mean, you saying that the data is another black box, essentially, this is like thinking in brains, this is like thinking of the environment, and the, the role that the environment plays in shaping the learning trajectories that our brains undergo.
*  So maybe we're getting fairly close to, you know, toward the end here. And maybe we should switch a little bit to, to speculative thoughts that you have about neuroscience. Just to start off, do you have opinions on, you know, how much biological plausibility I'm doing air quotes here, should be incorporated moving forward when you're thinking you're not thinking in terms of how brains do things, right? You're thinking in mathematical terms of how to move forward.
*  Yeah, so I would argue that the trend is in the other direction, right? Like, the neuroscientists have latched on to the deep learning paradigms, and trying to use them, you know, anything that gets invented meta learning, you know, suddenly the neuroscientists are using it. So I guess the reason for that is this paucity of data, right? That we just don't have enough data about what's going on in here. So we're trying to, people are trying to,
*  see what goes on artificial nets.
*  But we can't latch on to everything as neuroscientists. So for instance, we would be hesitant to latch on to the exponentially growing learning rates. And with regard to infinitely wide nets, what, like how to think about that in terms of brains? Are we just massively over parameterized toward the limit of infinity then?
*  Or, you know,
*  Yeah, no, I wouldn't have I wouldn't suggest there's a takeaway of all these things to the brain. Yeah. So I mean, batch norm is almost certainly not biologically possible. So yeah, so these are, I mean, in general, it's almost certainly going to be the case that what our intelligence will emerge out of computers will be very different from from human intelligence and in many ways. So
*  it would have to be right. The more I think the more I learn, the more I think about it. I mean, even the concept of artificial general intelligence doesn't mean anything to me, especially human, human level AI. I don't know, it seems like an empty concept to me. Do you agree?
*  Empty in what way?
*  Well, the AI that we will end up building, we're not going to replicate human intelligence, right? So it's going to have more resources in some domains, be more specialized, be more general in other domains, etc. And it would be silly to the only reason to build human level AI that I can see is to help understand human intelligence, not to not to build great AI because we're so limited. So you agree?
*  Yeah, I agree. Yeah, I mean, it I mean, that's the that's quite clear that computers have the advantage that you can string together millions of computers, right? And they can share their experiences. And it's just a very different kind of learning. I mean, I can't learn from your experiences because you're the bandwidth of communication solo.
*  Maybe AI will help that though AI bring computer interfaces, right? That's happening.
*  Maybe Yeah. That's very far in the future.
*  I think so as well. There's a recent push that I would like to ask her opinion. Well, opinion about I don't know if it's pushed. There's a recent opinion that neuroscience would do well to focus, you know, in terms of understanding brains, we all understand brain function and minds. Well, given the success of deep learning, that we might do well to focus to understand brains, we might do well to focus on objective functions.
*  On the architectures and the learning algorithms and that somehow grasping those will provide some explanatory purchase on how brains are working. Does this seem like a fruitful approach to you?
*  No,
*  why not?
*  So firstly, it's, it's not obvious to me at all that brains are optimizing an objective. I mean, let me say is the world optimizing an objective? Like, you know, our
*  evolution is right.
*  Well, interesting you say that because you know, there are thinkers about evolution who think that evolution is also completely hooked on the wrong terminology. Like maybe you should talk to Christos Papadimitriou sometime.
*  Oh, good. Okay.
*  Yeah. So I mean, what's going on in evolution and in life is there are all these creatures and they have these needs and they interact based on those needs. But is that clear that this interaction amounts to gradient descent or whatever, wants some global objective? That's not, that's not clear.
*  Yeah, I shouldn't have brought up evolution. It's not I agree.
*  Right? No, but that but then brains also like that, right? There's neurons. And it's not clear how they decide to link up or what even drives up. It is some kind of a system of entities interacting. It's not clear. Maybe there's some is selfishness among neurons. I don't know.
*  Right, right, right. So in general, it seems, it seems very naive. And I don't know, 19th century, 20th century, to think that interactions have some complicated enough system of many entities of 100 billion entities is gradient descent on some objective, right? That doesn't feel right to me.
*  So you think that's over simplistic that, that maybe neuroscience is just taking these the success of deep learning too much to heart and thinking, well, the brain must be doing deep learning.
*  Well, let me clarify that a little bit. So for instance, from the linear nets, something that we discussed earlier. So there's two levels of gradient descent, right? So there's, you know, that individual neurons are doing some, some process, right? And then there's the purpose of the overall entity, right? What is it trying to do?
*  And even in linear nets, you see that, you know, the gradient descent on some objective, but what the end to end net is doing, right? When you stack up all the layers and look at them to unfortunately, that's something very different.
*  So, you know, that is what we're seeing. We're seeing the behavior. And then the gradient descent is done on some other objective, which is not the behavior. And somehow magically, it leads to the behavior.
*  And in fact, you can show that that end to end behavior that it's exhibiting cannot be expressed, you know, it cannot be expressed as a gradient of anything that you can prove for linear nets.
*  But so you're admitting of the potential existence of objective functions of learning algorithms, but just that maybe we are unable to tie them to the end to end.
*  Functionality.
*  To behavioral output.
*  To behavior, yes.
*  So, so in that case, then understanding the objective function or functions or and or learning algorithms and or architecture would be sort of barking at the wrong tree because the behavior is sort of an emergent property that is, I don't know if orthogonal is the right word, but not tied directly to those functions.
*  Yeah, I think it's too early to know, right?
*  You can't generalize, you can't carry over conclusions from linear nets to brain.
*  But it does show, you know, something that's clearly mathematically very possible.
*  And given that it happens even for linear nets, I would say it's probably the way things happen all the time that, you know, you have systems of interaction, interacting units.
*  And their overall behavior is some complicated thing which you cannot understand in a very easy way from the atomic interactions.
*  Right.
*  That's just the takeaway from science, right?
*  Like how, as we run into complex things, that's probably happening.
*  So you interact with neuroscientists pretty frequently, especially at these, you know, at these workshops and conferences that.
*  I also at Princeton a little bit, yeah.
*  And at Princeton, yeah, like, all right.
*  So, so is there never a temptation?
*  I'm curious about your own curiosity, right?
*  Because you, you know, what drew you into the algorithms and into deep learning is this, it's kind of an open field, right?
*  Well, neuroscience is potentially even more open.
*  Why not go to neuroscience then?
*  Too, too hopeless?
*  Yeah, it seems much more difficult, right?
*  So, so with deep nets, it's clear that they work for many settings.
*  And so you can run experiments and see what works and doesn't work and so on.
*  With neuroscience, the capacity of experiments is very limited.
*  So you are sort of doing a lot more shooting arrows in the dark and it feels like from the outside.
*  So it seems much more challenging, maybe in 20, 30 years.
*  So you have like a comfort level with a field being somewhat, constrained is the wrong word.
*  You have hope to pursue.
*  So I'm asking what advice you're going to give now.
*  So to pursue a given topic, you need to feel like there can be progress made on it.
*  And that's a question, I suppose.
*  You know, like, I'm wondering, like, what is your right level of unknown?
*  So that, you know, maybe there's a little bit of candle lit in the dark.
*  So you're not shooting arrows and complete pitch blackness.
*  What's the right amount of luminance that you need to go shoot arrows?
*  Yeah, so it's clear that, you know, okay, so firstly, my mind works in mathematical ways.
*  I like to understand things mathematically.
*  And as we discussed earlier in the interview, it was quite clear that if you want to understand
*  machine learning and especially deep learning currently,
*  you have to get out of that comfort zone.
*  You cannot mathematically understand everything.
*  So then it becomes a little bit more like physics, that there is some level of mathematical
*  understanding and some experimental.
*  And then sometimes you just say, okay, systems are just too complicated, right?
*  As far as I can tell, that's what my physics friends tell me.
*  We still don't understand superconductivity very well, you know, things like that.
*  So some phenomena are just too complicated.
*  So maybe that's where deep learning is, maybe more like physics.
*  We need math and we need experiments.
*  And that seems like a reasonable, just from my philosophical bend of mind,
*  seems like a reasonable state of affairs, you know, that you can make progress.
*  With neuroscience, it seems more challenging to me.
*  Just that's just my philosophical, my makeup of my mind.
*  How many more years will you be working on deep learning theory before you feel
*  you've satisfied your own curiosity?
*  Ramesh Prasad
*  That's always hard to predict.
*  Yeah. It's already come a long ways compared to what I would have imagined six, seven years ago.
*  So you've outperformed your expectation.
*  Ramesh Prasad
*  Well, I and the field, I mean, I'm not taking credit for everything that's happened, right?
*  But yeah, there's, you know, very smart people got into it, young people.
*  And amazing things have happened.
*  So you stay in a field until it's so long as it's exciting.
*  And it is very exciting.
*  If you speaking of young people, if you were going to give advice to someone entering the field,
*  I mean, would you, it sounds like you would shake them and, and demand that they pay attention to
*  learning trajectories, that that's the way, that's the way in.
*  And that's how we're going to make progress and abandon objective function landscape.
*  Landscape thoughts is that would that be your advice?
*  How would you, how, what would be your advice to someone entering
*  into the deep learning theory field specifically?
*  Ramesh Prasad
*  Yeah, I think the trajectory thing is fairly at this point, pretty well established in the
*  last two, three years. I think the young people are very aware of it in terms of what I'm telling
*  my students to look at. I'm interested in the data. What I said, you know, that's the black box.
*  That's the next black box. And actually, I got into machine learning looking at data,
*  like topic models and other kinds of probabilistic models that we saw using method of moments.
*  That's how I got into it. And I've always been interested in structure of data, like
*  structure of language of images. Yeah, I would like to understand that better.
*  Adam Backer Does this go back to the,
*  you're thinking about NP worst case scenarios, complex computational complexity wise, was,
*  was data part of that thought process as well?
*  Ramesh Prasad Right. So it's clear that real life
*  data is not worst case, right? It has a lot of structure. And that's what makes learning
*  possible. So yes, it's connected to that. But yeah, it's the black box in learning, right?
*  The data is considered a black box. It's just a data distribution. And clearly,
*  the properties of the models that we learn depend on the data. So that's the next frontier.
*  That's what so in the next five years, I would hope that theory makes some progress in coming up
*  with realistic data models. So they don't have to be 100% or even 75% accurate, right? So language,
*  people have tried to model for decades at this point, right? And it's very complex. And you
*  won't have a simple probabilistic model that describes all features of language, but we can
*  try to have a little bit more informative models than we have currently.
*  Mike
*  Two, two quick questions here before I let you go. I know that you've got to go. One,
*  do you think that the that minds are inherently cryptographically unbreakable? This is harkening
*  back to your complexity computational complexity days.
*  Ramesh Prasad Oh, you mean understanding the mind?
*  Mike Or decoding like the you know, the contents of mind. Yeah. And or understanding.
*  Ramesh Prasad Hmm. Yeah,
*  I'm not sure if that's currently formalizable. Like, what does that mean? So if like if you had
*  like a core dump of whatever neuron is doing at this moment, whether to understand
*  Mike Yeah, what if we what if we could record all neurons
*  at millisecond time scale, so all spikes of all neurons?
*  Ramesh Prasad Yeah, see, the thing is that, you know,
*  then you're working with whatever 100 million 100 billion data points or something, right, or more.
*  Ramesh Prasad You don't need NP completeness for it to be
*  basically unsolvable, right? Even if it takes, let's see, quadratic or cubic time.
*  That's already intractable, right? With 100 billion data. Yeah. So that's something to always
*  keep in mind. So it's not clear that NP completeness is even needed here for it to be
*  intractable for all practical purposes.
*  Mike So, and G, does P equal NP?
*  Ramesh Prasad It probably is different. Yeah.
*  That's what most people would say.
*  Mike Probably does not equal NP.
*  Ramesh Prasad Yeah.
*  Mike Yeah. Yeah. That's a so does your work on approximation and so was it your thesis work
*  where you prove that for NP problems, if you can find an approximation, it basically means
*  that you can find an exact solution. So there's no advantage of approximating a solution relative
*  to finding an exact solution. Is that work that drives you to believe that NP and P are different?
*  Ramesh Prasad Well, right. So that work would
*  become fairly meaningless if P were equal to NP because then you would just be able to solve
*  problems exactly and approximation goes away, right? The whole reason for approximation is that
*  we cannot in practice do exact computation.
*  Mike Well, thank you so much. I know you have to go. Sanjeev, continued success. And I hope to see
*  you still at least thinking and talking about brains on occasion.
*  Sanjeev K. Totally. Yeah. Okay, thank you very much. It was a pleasure.
*  Go to brandinspired.co and find the red Patreon button there. To get in touch with me,
*  email paul at brandinspired.co. The music you hear is by The New Year. Find them at the newyear.net.
*  Thank you for your support. See you next time.

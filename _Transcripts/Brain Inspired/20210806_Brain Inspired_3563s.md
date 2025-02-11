---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 3563s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 6529
Video Rating: None
---

# BI NMA 04: Deep Learning Basics Panel
**Brain Inspired:** [August 06, 2021](https://www.youtube.com/watch?v=Cz2NAQvCc5k)
*  All of deep learning is optimizing something.
*  And what engineers do if they're smart is think about what am I really trying to optimize?
*  What's the loss function?
*  What goes in goes out.
*  Obviously, now that I know a lot about machine intelligence, I know it is very different
*  from human intelligence, maybe inspired, but still it is not the same.
*  So it may take time for the science of deep learning to catch up to the engineering of
*  deep learning.
*  It could be like decades, right?
*  This is Brain Inspired.
*  Hey everyone, it's Paul.
*  This is the fourth installment of the Neuromatch Academy panels and the first of the three
*  deep learning modules.
*  So with me today is Amita Kapoor from the University of Delhi, Lyle Unger from University
*  of Pennsylvania, and Surya Ganguly from Stanford University.
*  The topics this week were the basics of deep learning, linear deep learning, and PyTorch,
*  which I mistakenly call TensorFlow, a forgivable offense, I hope, multilayer perceptrons, optimization
*  and regularization.
*  And we mostly focus on optimization and regularization in the bulk of our conversation.
*  We talk about the relation between optimization and regularization, how necessary regularization
*  is and will be, whether optimization is the right way to think about learning in deep
*  nets, given the role of learning trajectories.
*  We also talk about paying for sterility, magic, and lots more.
*  And it all goes by way too fast.
*  So I link to the information for Amita, Lyle, and Surya in the show notes at braininspired.co
*  slash podcast slash nma-4.
*  Thanks for listening and I hope you enjoy the discussion.
*  Amita, Lyle, Surya, thanks for being with me here.
*  I thought what we could do is just go around, you guys could give a brief introduction of
*  who you are and what you do.
*  But then I thought it'd be fun if, to get to know each other, if you guys started with
*  telling a story about an early question you had early in your research career before you
*  guys became the experts that you are now, and then a question that is interesting you
*  now, now that you are the expert that you are and why you're interested in that.
*  So Amita, should we start with you?
*  Yes, definitely.
*  So when I started with my career, very initial stages, and I was studying and I was teaching
*  at the same time, my questions were more related to intelligence.
*  So like, you know, what is intelligence?
*  How do we say one person is more intelligent than other?
*  Shouldn't everyone be equally intelligent?
*  And I would say at that time, I used to believe everyone is equally intelligent, but perhaps
*  there are different dimensions where they express their intelligence.
*  So someone experts in art, someone in maths and so on.
*  And I guess that was one of the reasons why I was also interested in artificial intelligence,
*  to understand intelligence better, even maybe natural intelligence.
*  Obviously, now that I know a lot about machine intelligence, I know it is very different
*  from human intelligence, maybe inspired, but still it is not the same.
*  It's very different.
*  And now the questions are basically how to go towards, you know, achieving an intelligence
*  which can be similar, more towards, you know, going towards AGI, more towards understanding
*  the natural intelligence by means of artificial intelligence.
*  These are the queries which I have.
*  You started off interested in neural networks and perceptrons and also reading Isaac Asimov
*  and you were like a Trekkie, right?
*  Is that the...
*  Yes, yes, definitely.
*  Almost from the childhood, Star Trek is my favorite serial even now.
*  I will see it for hours and hours, repeat all the episodes.
*  So yes, definitely.
*  I'm sorry, I'm just going to jump in with questions because that's what this is about
*  anyway, but you mentioned AGI.
*  So you think AGI is a thing?
*  Right now not, but I do believe sometime, somewhere we should be able to get it.
*  With the present technology, definitely not.
*  What do you mean by AGI though?
*  What is it?
*  What I would say is AGI is some sort of an intelligence which is more general in the
*  nature.
*  It can apply its intelligence not to just one domain or few domains, but to multiple
*  domains.
*  And for each domain, it should not require 20 years of learning as we do.
*  So that is what I would call as AGI.
*  So I do hope we do reach it and hopefully in our lifetimes that would be great.
*  So let's see.
*  Should we apply Asimov's, the three laws of robotics?
*  Oh yes, they should be there.
*  How we still have to think about them.
*  There are ways and there are things that one has to decide how to go about it.
*  But I guess that some form of three laws of robotics, not exactly the same, but some form
*  of three laws of robotics is needed.
*  Especially when we talk about ethical AI, we have to have bias, discriminations.
*  These things should not go.
*  Misuse of AI is always a possibility so that we should try and do something about it so
*  that it doesn't happen.
*  Very good.
*  Lyle, you played with early perceptrons too, if I'm not mistaken.
*  So I have my whole career modeled the world, complex nonlinear phenomena.
*  I started actually as a chemical engineer and I realized that we wrote down these incredibly
*  complicated chemical reaction equations, some of which pieces were true like mass is conserved.
*  And some of which were just made up.
*  And it turns out you can throw neural nets inside of partial differential equations.
*  Oddly enough, 30 years later, this has now become popular again to do physics constrained
*  to neural nets.
*  And in some sense, I spent my whole career, I've modeled genomics, I've modeled economics,
*  people, I do psychology mostly now.
*  And I think for me, the thing that keeps fascinating is what can we build in?
*  Some things are easy invariants, translational, rotational, some things conservation of mass,
*  conservation of energy.
*  Some things are harder things to build in.
*  How do you build in linguistic structure?
*  I do natural language processing.
*  What are the universals across English or across all languages you could build in?
*  So I think for me, the fascination has always been we're not able to write down complete
*  models.
*  widely studied language like English, the largest grammar is six volumes long.
*  It's terribly incomplete.
*  It's just missing lots of stuff, lots of stuff that Google Translate knows with transformers
*  and modern deep learning.
*  So I think the question is always what do you build in?
*  What do you learn?
*  How do you structure it?
*  And I think that's been the case and it's still the case for deep learning.
*  Being a chemical engineer in your background, what do you think of applied physicists?
*  They're smart.
*  I wasn't an applied physicist.
*  I mean, there's lots of people that are well trained in doing things.
*  I think, why do you ask?
*  I might start a little beef between you and Syria.
*  I wasn't sure.
*  The interesting thing is I know lots of ex-physicists.
*  I worked with a psychology PhD student who was an undergrad degree in physics.
*  I see a lot of people trained in physics with really good training and they're feeling
*  that physics is not going anywhere interestingly fast enough and they've shifted into biology
*  or computer science where there seems to be more action for smart mathematical people
*  to go.
*  So that's sort of my take on applied physics is it's awesome training, but it's a little
*  scary to me how many ex-physicists I know.
*  Surya, before you start, sorry Amita, did you want to jump in?
*  No, I was just...
*  I didn't know if you had some.
*  No, no, no, no, thanks.
*  Continue please.
*  Yeah.
*  Okay.
*  So Surya, it is an interesting thing.
*  I think I often complain on the podcast or note, let's say note instead of complain,
*  mostly because the complaint part is just jealousy that there's a lot of physicists
*  coming into neuroscience, right?
*  But that's because there really aren't neuroscientists.
*  There's neuroscience now, which is now made up of people from all different sciences.
*  What do you think about Lyle's contention that physics is dead?
*  I'm paraphrasing.
*  Physics is dead.
*  Let's do something more complicated, more complex like biology and neuroscience.
*  Does that ring true to you?
*  Yeah, I think yes and no.
*  So first of all, Lyle, I'm glad you like applied physics because I happen to be one.
*  I figured that out sort of halfway through there.
*  By the way, physics is dead.
*  Long live physics.
*  Yeah.
*  But I mean, you know, I went through that path actually.
*  I did my PhD not even in applied physics.
*  I did my PhD in string theory.
*  And you know, I had a lot of fun doing that.
*  If I had to do it over again, I would still do a PhD in string theory.
*  It was fun, but eventually I wanted to connect to nature, like really understand how nature
*  works.
*  And I think it was hard.
*  It was very hard to do that with string theory.
*  And so I switched fields and I took my first course in neuroscience at the end of my PhD.
*  It was taught by excellent professors at Berkeley like Bruno Olshausen, Frederick Tutusen, Yang
*  Tan.
*  And I just fell in love with it.
*  And I realized I could use my physics skills to analyze complex systems in biology.
*  And yeah, I think a lot of physicists do go through that.
*  Like I think physics is fantastic training.
*  And then they want to try other things afterwards.
*  And for me, I think it's more power to them.
*  I don't think physics is dead.
*  I think there's very interesting stuff going on in condensed matter physics, quantum entanglement,
*  like so forth.
*  There's actually a merger between neuroscience and physics now too, because there are things
*  called neural quantum states where they try to approximate many body quantum wave functions
*  using neural network parameterizations.
*  And they're doing really, really well.
*  So I think like I actually have fun working in neuroscience physics and machine learning.
*  And I guess that's typically what applied physicists do.
*  They kind of work broadly in many fields using their training, just like applied mathematics.
*  I would like to add here, even my PhD was in photonics.
*  So it's kind of physics based.
*  And I would say it's not dead in that sense, because even during my PhD, I was thinking
*  about implementing optical neural networks and how to go about that.
*  But yes, pure physics requires a lot of experimentation and a lot of infrastructure, which may not
*  be possible for many of us, unless we have big grants, big universities.
*  Yes, I have collaborators like related to that, like with Benjamin Lev, a colleague
*  of mine in applied physics.
*  The only reason we started working together on this particular project is because we're
*  both colleagues in the same department.
*  But he can build neural networks out of atoms and photons.
*  So the atomic spins are like the neurons and they exchange photons.
*  Those are like the synapses.
*  And we show the whole quantum neural network is exactly that.
*  Exactly.
*  Yes.
*  So a particular cavity quantum electrodynamics system could implement a hotfield model.
*  And its particular intrinsic quantum dynamics is better than that of the hotfield model
*  in terms of maximizing memory storage capabilities.
*  So I think it's just fun to be open minded to these collaborations.
*  I can't run an experimental physics lab because I don't have the expertise.
*  And that's a lot of grant money to raise.
*  But it's good to have friends who can.
*  And fostering those collaborations is, I think, a lot of fun.
*  So this is super cool.
*  So as a more applied guy trying to model the world, when am I going to get a hold of some
*  of these quantum computers, quantum neural nets that actually outperform my old fashioned
*  GPUs and TPUs I'm using now?
*  Well, this is something Amita, you and Surya have in common, that you think that the future
*  of deep learning is sort of dependent on quantum computing.
*  Is that right?
*  I think quantum computing will help, definitely.
*  It's like the work that I have already done in quantum computers with the IBM machines.
*  I feel, yes, quantum computing has a lot of scope.
*  But yes, it is limited.
*  Again, as Lyle said, hardware is not available to everyone.
*  Even the cloud computers, they are like quantum computers.
*  They are hard to get by.
*  You have to have credits and all that stuff.
*  But it will come, hopefully, to most.
*  Lyle, is that something that you are just chomping at the bit for?
*  I mean, how much do you think that it would...
*  Is that something you are actively waiting for, is quantum computing to help your deep
*  learning algorithms?
*  Completely not.
*  I have spent my whole career trying to avoid hardware.
*  I'm interested in how do people think, how do genes work.
*  But every decade, I have to learn to run my stuff on a new hardware system.
*  I've used Cybers and Cray's.
*  I now use GPUs.
*  Because hey, they are way cheaper and way faster.
*  And so, sure, well, I like quantum computing.
*  No, it's going to be annoying.
*  I'm going to have to redo my algorithms and recode things for a different computing hardware
*  structure.
*  And will I do it?
*  Of course I will.
*  If I can do something that allows me to be 100 times faster, I can do better modeling.
*  But in some sense, for me, this is all just an unfortunate consequence of progress.
*  And I do think that when my contributions are much more how can you build in knowledge
*  of the world, which also gives you your 100-fold or 1000-fold faster improvement.
*  So far, it's 50.
*  Well, no.
*  So far, the hardware guys are winning.
*  I mean, convolutional neural nets were a huge leap.
*  One might almost say quantum leap.
*  But let's be honest, the real benefits in the last 30 years has just been way faster
*  conventional silicon-based old-fashioned computing with different vector architectures.
*  But I'm happy when these guys give me the computers, I'm going to use them.
*  What am I going to say?
*  No, I don't want to be faster.
*  I don't want quantum computing.
*  But this is the lifelong learning problem in deep learning.
*  Sorry, Surya, go ahead.
*  I just want to say I'm not all in the quantum thing for sure.
*  I think it's important to note that human intelligence doesn't in any essential way
*  Right.
*  Despite Penrose's assertions and so forth.
*  Right?
*  I mean, we operate at a lower temperature, we don't have quantum current dynamics and
*  so forth.
*  We're basically classical computers.
*  And if you think about order of magnitude discrepancies between the capabilities of
*  humans and machines, energy expenditure is one of those.
*  Our brain spends 20 watts, supercomputers operate at the megawatt power consumption
*  range, and they can't do what humans can do.
*  So if you think about why that is, it may actually be that digital computing itself
*  is the fundamental mistake that we made.
*  Right?
*  We rely on computations with the intermediate steps of computation, i.e. bit flips and transistors
*  are extremely fast and extremely reliable.
*  But we play a huge energetic cost for that because the laws of thermodynamics demand
*  that every fast reliable bit flip costs a lot of joules of energy.
*  Right?
*  Energy instead is slow, it's noisy, it's very, very parallel.
*  Every intermediate step of the computation looks a bit chaotic and noisy, but the final
*  answer is just good enough.
*  And so by avoiding fast, reliable intermediate steps, I think that's where we got the energy
*  efficiency in biology.
*  And we've already gone down the wrong route in digital technology if our goal is energy
*  efficient AI.
*  So I think analog computing, if we can harness that and power that and create error corrective
*  analog computing, that might be the better way to go to get energy efficient AI than
*  quantum computing.
*  But Lyle still has to learn it.
*  Well, the trick is we really don't know how to code it.
*  So I do think that not just Lyle has to learn it, but a lot of people that it's not obvious
*  that the same algorithms and coding things that work well in the current infrastructure,
*  which we've optimized over 50 years, are going to work as well.
*  So I think it's going to raise a bunch of interesting issues.
*  So I understand at the macro level.
*  So I worked at Google, which is getting close to having as much GPU power as it has human
*  power in terms of compute power.
*  If you look at the overall memory capacity of its computers versus its people, they've
*  at the macro level, of course, machines fail all the time.
*  If you look at the early machines, my university, Penn, had something called ENIAC.
*  When one of the little components failed, the vacuum tube, the whole thing went down.
*  Google and anybody, Baidu, whoever you like, always machines fail.
*  At the macro level, we've learned to route around and deal with this constant failure.
*  At the micro level, of course, they're still using very conventional digital computers,
*  and they don't allow failures.
*  I do think it's maybe going to trickle down as Surya wants, and we will get more and more
*  fault tolerant because it's been forced already at the high level.
*  Amit, so TensorFlow, I believe, is one of the topics of the week at Neuromatch.
*  Lyle was just talking about how he doesn't look forward to learning new hardware systems,
*  but this is applicable to software as well.
*  I remember one of my grudges, a real point of friction for me, was I would finally get
*  used to coding in a certain language, and then something else would come in and I would
*  have to...
*  Updates, yeah.
*  Updates, yeah.
*  TensorFlow, right now, I suppose, is the language du jour.
*  Amit, you write textbooks and all sorts of things about TensorFlow.
*  Is TensorFlow here to stay?
*  Or when is the next thing going to come through?
*  People used to talk about...
*  There was a graduate student who said that Matlab would re-consume Python.
*  Is everyone who's learning TensorFlow, is that going to be with them for their life,
*  or eventually we're going to have to learn analog computing with a different scripting
*  language, et cetera?
*  Here, I would say any deep learning framework is going to live as long as there are contributors
*  working on it, as long as there are people improving it.
*  Right now, TensorFlow is very actively maintained, very actively updated, and all the new models
*  are very actively added into it.
*  That makes our work easier as a deep learning scientist.
*  So TensorFlow is here, but if they stop doing it, there will be someone else.
*  There was a time when we had Cafe.
*  Everyone was using Cafe.
*  It simply depends on how many people are updating it, regularly maintaining it, and contributing
*  to it.
*  That's a major factor.
*  PyTorch at the moment is at least as widely used.
*  I think it's actually gradually more widely used than TensorFlow.
*  At some level, those differences are so small that once you learn the concepts, whether
*  you're doing PyTorch or TensorFlow, who cares?
*  All good languages, they're both incorporating.
*  Each one makes an advance.
*  The other one puts it in.
*  True.
*  Both have their features, yes.
*  It's PyTorch.
*  I'm sorry.
*  I said the wrong thing.
*  They're learning PyTorch, not TensorFlow.
*  Yeah.
*  So, so PyTorch.
*  It means learning PyTorch.
*  TensorFlow is really more last year than this year?
*  No, I would not.
*  I would disagree.
*  I would disagree.
*  Okay.
*  It's all about Jacks now, right?
*  At some level.
*  I'd say PyTorch is more good for research and implementation.
*  TensorFlow is very convenient in the terms of production, like especially the ecosystem
*  that they have developed now, like TensorFlow probability, TensorFlow data sets, TensorFlow
*  hub.
*  That whole ecosystem is very supportive for doing things very quickly.
*  So that's one advantage of TensorFlow.
*  Otherwise, both are equal.
*  Although PyTorch is rapidly putting a whole set of basic machine learning functions and
*  they're copying lots of that functionality.
*  So again, I think on the short term, the five year timeframe, TensorFlow and PyTorch are
*  both actively evolving and looking really similar.
*  Longer term, sure.
*  Something will take over with different architectures.
*  I mean, we're mostly not writing Fortran or COBOL or even C or even C++.
*  Right?
*  So fine, they evolve, but the concepts haven't changed that much.
*  I still miss Turbo Pascal.
*  That's what I forgot.
*  Oh my God.
*  Fortran.
*  I learned Fortran.
*  I'm old enough to have learned Fortran.
*  I wrote my thesis in Fortran, but I got to say Python is so much nicer.
*  It is.
*  There's been improvements in design and languages.
*  They're just better designed now than they were 20 years ago.
*  Nothing like a bumbling podcast host to throw around buzzwords incorrectly.
*  TensorFlow, PyTorch, all the same.
*  Throwing people off.
*  All right.
*  Well, so other topics that the students were learning about or I think that we should focus
*  mostly on probably are regularization and optimization and not necessarily in that order.
*  So, Lyle, actually, one of the things that you suggested that we talk about is the relationship
*  between optimization and regularization.
*  So I want to ask you what that relationship is.
*  The thing that I'm currently fascinated by is the fact that the way that people build neural nets
*  is they make them too big, too complicated, and then they optimize them by some version of gradient descent.
*  And the optimization process of doing the gradient descent, magically, which is to say there's lots of cool math,
*  magic, same thing, magic math, I can't tell the difference, magically converges to good optima.
*  And then you only partially converge, which regularizes and it converges to a nice flat minima if you do it well,
*  which regularizes.
*  So the optimization scheme we're using is, in fact, regularizing.
*  If somebody said, hey, I can use a quantum computer, I can find the true global optimum of your neural net.
*  I can solve the NP-hard problem quickly.
*  First, I'd be skeptical.
*  But then I would say, God, that's terrible.
*  The worst thing you could ever do is find the global optimum.
*  The thing you've overfit the data beyond all possible things there.
*  Turn off the quantum computer and go back and do gradient descent because it gives me nice optima.
*  Magic.
*  Do you guys agree with that?
*  Yeah, I think this is one of the biggest things that we've learned from a statistics perspective in deep learning is
*  classical statistics says if you have many, many more parameters than data points, you're going to be in big trouble because you'll overfit to the data
*  and you won't be able to generalize to new health data.
*  Right.
*  But if you analyze like now, mathematicians have worked out like why this is not having happening in certain overparameterized systems.
*  We also have a paper on this topic where we showed that if you train even simple linear deep networks and also nonlinear deep networks on on some data set,
*  they learn the most important structure in the data first and then learn less important structure in the data later.
*  And learning the most important structure helps you generalize.
*  So, for example, if you stop early a little bit and don't go down the rabbit hole of the deepest minimum, you will learn the most important structure and you'll generalize well.
*  And, you know, people have been working on multiple areas like the other thing is beneficial regularization.
*  Right. You have that proverbial picture where if you imagine your head a whole bunch of points that all come from approximately a straight line plus noise
*  and you fit a higher order polynomial to those points that goes through every single point,
*  it'll it'll oscillate wildly around the points of intermediate positions and you'll overfit.
*  It turns out if you have a very, very high degree polynomial, but you start from zero weights and you do gradient descent to do the fitting,
*  the polynomial will get wigglier and wigglier until it goes through all the points and the wiggles won't grow beyond that.
*  So the overfitting is beneficial. If you do gradient descent starting from small weights in the high degree polynomial,
*  you'll get beneficial overfitting in the sense that you'll interpolate the data.
*  You'll go through every training point, get zero training error.
*  But in between the training points, you won't wiggle as much as you think you would.
*  So that in a nutshell is the basic idea. If you do gradient descent from small weights, you won't learn that wiggly of a function and you'll generalize in between data points.
*  I think that's the simplest way to explain the intuition.
*  I love it.
*  Yes, it is magic. And I would say like whether it is optimization and regularization,
*  starting with the simple models is always better rather than going to the complex networks directly.
*  You mean certainly when I teach applied sense, always fit a linear model first, see how well it does.
*  Yes, it's for the students.
*  For the students to distinguish a process, you should always get a simple linear model and see how well it does.
*  Often it's incredibly hard to beat the baseline of a decently regularized linear or logistic regression.
*  Absolutely. What Anita says. And oddly enough, if you're doing a neural net,
*  then usually the simple neural nets are not as good as the complex ones with sorry, as magic gradient descent applied.
*  By the way, the last time last episode of a Neuromatch panel like this,
*  I threw out the word magic and got excoriated by the panelists because, you know, real magic is not real.
*  But I know what you guys mean. So I'm not going to I'm not going to push back at all.
*  Paul, did you carefully say that magic is the same as mathematics? You missed the equivalence class.
*  I called mathematics sterile, in fact, so that was fun.
*  But it is. Mathematics is sterile.
*  No, mathematics is the most beautiful subject.
*  Hey, I'm sterile and I paid for it.
*  I doubt you're truly sterile with a little bit of biology.
*  If you don't have lots of bacteria growing in you, you're probably a zombie.
*  My association that meets your magic, Paul.
*  Sterile and magic. Yeah, a little oversharing for everybody.
*  But so so so so you start with small weights, you do the gradient descent.
*  Do we even need to regularize or because the the initial idea of regularization or the initial need for it was to not overfit.
*  But what you're saying is with with a big enough model, essentially with enough parameters,
*  you'll and if you start with low initial weights, you're not going to overfit.
*  So in that case, do we even need to regularize?
*  Yeah. So, you know, sometimes no, actually.
*  Right. Like what this what this theory tells you is if you don't regularize at all, you still won't wildly overfit.
*  You can in principle do better with some regularization.
*  And we actually have another paper on a theory of high dimensional regression where we show that if you don't regularize, you don't do that bad.
*  But if you regularize optimally, you do better. Right.
*  In practice, data sets won't always obey all the theoretical conditions you impose on your model data to prove your theorems.
*  So in practice, you always got to cross validate into hyper parameters, including regularization parameters.
*  And you just pick in practice the level of regularization that helps you best perform on your test set and then eventually validate
*  or best perform in your validation set and then eventually test on a test.
*  So I think it's always a good idea to regularize.
*  But I think what the theory tells us is why you don't do that bad if you don't regularize.
*  And this is really like a conceptual insight that has taken the field of statistics by storm.
*  Right. They're they're card carrying statistical theorists theorizing about this now.
*  And they're kind of wringing their hands saying, why are the statistics textbooks written in such a way that suggests that this is impossible?
*  So the statistics textbook has to be rewritten. Right.
*  Oftentimes, people say in deep learning, it's just, oh, we just got like Newton and an algorithm that goes back to the type of Newton, the chain rule, i.e.
*  backprop. And we marry it with GPUs.
*  And so there's no new conceptual advances in deep learning.
*  I think to defer, there are lots of conceptual advances coming out of the field, which I think are really exciting.
*  I completely agree with three and I'm still struck by the contrast between the really cool math, which is just giving really nice insights.
*  And the fact that when I talk to people in industry, they spend all their GPU time doing optimization of trying to fine tune the hyper parameters and choose the geometry and choose architecture.
*  There's just an enormous empiricism, which drives almost all the application work in spite of the fact that the theory work is is gorgeous and making really nice progress.
*  Yeah, I don't think so. Yeah. What theory hasn't given us yet.
*  It's not powerful enough to give us yet is the rational theory guided design of hyper parameter choices in realistic data settings that matter to industry.
*  We don't have that yet. But if you go back to like the old ages when we had steam engines, right, we had like steam engines before we understood the laws of thermodynamics.
*  And so we had to work really hard to sort out the laws of thermodynamics.
*  And then we got the Carnot cycle, the most energy efficient steam engine and so forth.
*  And then eventually a deeper understanding of the science led to better engineering.
*  But more often than not, engineering leads the science.
*  The science catches up. But then once the science catches up, we can work in synergy and get a rational theory of design.
*  Right. But, you know, it remains to be seen whether steam engines are much simpler than networks that solve alpha goers.
*  And it took a good 100 years before the thermodynamics theory was actually useful.
*  I mean, now it's useful, right? It's something we teach all undergraduates in chemical engineering.
*  I've taught thermodynamics. It's actually a very applied subject right now in spite of being based on this, you know, again, very elegant math.
*  Exactly. So it may take time for the science of deep learning to catch up to the engineering of deep learning.
*  It could be like decades. Right.
*  One of the things that I found surprising when I tried pulling my predecessor to this course, I took a standard rules like how fast should the learning rate be?
*  Should you, Anil, slow down with the square root of iterations, for example, which seems like the right theory.
*  And it turns out that there's lots of nice theoretical papers.
*  And then you try and actually make up a homework assignment. And then it's very frustrating because the darn simple, clean homework assignment actually contradicts the very elegant theory that says, of course, pick your favorite scaling.
*  Is it linear in iterations? Is it square root of iterations? Whatever it is, whatever it is, it's easy to it's embarrassingly easy to find counter examples and almost harder to find ones that actually support the theory for fairly simple.
*  Yeah. Just to state that more precisely than I mean, you can't counteract a correct theorem because it's correct.
*  Of course. What I would say is like, what is it about the structure of the real world problem that you're solving that violates the assumptions of the theorem?
*  Right. And that's where I think like theorists have to make assumptions to make progress.
*  And then the question is, like, how relevant are your assumptions? Right. And then, you know, that's the cycle between theory and experiment.
*  Right. When you find a situation where the theory doesn't apply because the data has a different assumption, can we generalize the theory?
*  I think that's incredibly exciting interplay. And so, you know, I spent time at Facebook also, and I talked to a lot of people, industry practitioners there at Facebook AI research.
*  And I love hearing all the weird puzzles that they see because it's just fun to and then you try to think, well, why is that happening?
*  And then you try to come up with a simple situation where you can explain why that's happening.
*  But then you have to iterate. You have to talk to them and say, hey, this is why I think that's happening.
*  And then they try to poke holes. And so it's a lot like neuroscience, to be honest, like the same way I talked to experimental neuroscientists when I try to understand how a biological system is working.
*  I feel like I talk the same way to engineers when I try to figure out how artificial systems work.
*  Because computer science and biology broadly are the two sciences that deal with complexity in a way that you actually have some chance of understanding it.
*  I mean, history also does, but they're not going to be a science. You can't run the same experiments you can in history that you can in neuroscience or computer science.
*  You can't do causal perturbations of history.
*  Unless we're all within a simulation and we're one of them.
*  OK, OK. Right. Yeah.
*  So I had there's lots of different ways we could go right now.
*  I'll go this way. So I had Sanjeev Arora on my podcast a while back and he says we need to discard the notion of or stop talking about optimization.
*  It's the wrong framework and focus more on the learning trajectories because the trajectory and I know Surya you've done work on this as well with the with the linear networks.
*  And I've had other people on who have as well that we should stop thinking about.
*  Great like landscapes, error landscapes, optimization landscapes, because that will lead us astray because it all depends on the trajectory that the learning algorithm takes you.
*  I was going to say along that landscape, but then that's bringing us back into thinking about the landscape, which is a good point of how hard just let go of it.
*  Right. Right. Right.
*  This either or thing is really hard way to pose it as opposed to I mean in some sense Sanjeev and Surya are saying the same thing.
*  The trajectories matter to try and say, well, throw out the landscape.
*  What is the trajectory in if it's not in a landscape? Hello.
*  So plus I think we're in a simple interpretation of that is like, yeah, there is the landscape and it's there.
*  But the trajectories may not explore the landscape in an unbiased manner and many parts of the landscape may be completely irrelevant and unreachable.
*  So what really matters at the end of the day is the properties of the trajectories and what parts of the landscape they explore.
*  And that I think is a fairly uncontroversial statement because because what the trajectories explore is what you see in practice.
*  Right. So so then we have to think about it.
*  So what is the
*  analog in physics between equilibrium physics and non-equilibrium physics?
*  Right. In equilibrium physics, you assume that the system settles into some Boltzmann distribution over the set of all possible states with a probability of the state is e to the minus energy in the landscape.
*  In non-equilibrium, you could be more cadetically constrained.
*  Right. You may not settle into equilibrium.
*  You may be constrained by your initialization and so forth.
*  So I think multiple fields of discipline have have come into this sort of landscape is equilibrium and trajectory is non-equilibrium and in many situations, the non-equilibrium that matters.
*  I completely agree with Sanjeev and I actually don't think anyone could disagree.
*  Throw that out there.
*  It's all true.
*  It's all true.
*  In the economics back in the 1920s, John Maynard Keynes famously attacked equilibrium economics by saying in the long run, we're all dead.
*  When you achieve equilibrium, it's all over.
*  That's not fine.
*  There's an attractor point.
*  Yeah, we know what the attractor is.
*  And the equilibrium is a boring one.
*  Yeah, in my biophysics class, I like to say that in biology, equilibrium is also death.
*  Right.
*  We're fundamentally non-equilibrium.
*  We're always consuming energy and we're violating the second law of thermodynamics, at least if you don't account for the fact that you're consuming energy.
*  Right.
*  So, yeah.
*  So that said, I want to go back to the students and say, on the other hand, even though the full landscape is irrelevant, to think of things as optimization is the right way.
*  I'm the engineer, I think, the token real engineer here.
*  The right way to think about things is what's your loss function?
*  What are you trying to find?
*  What are you trying to minimize or maximize?
*  And so in some sense, forgetting the landscape question, all of deep learning is optimizing something.
*  And what engineers do if they're smart is think about what am I really trying to optimize?
*  What's the loss function?
*  What goes in goes out?
*  And the trajectory is some way to get to that loss function you're minimizing.
*  So I still think thinking in terms of optimization as a problem specification, which is very different from this question of will we explore the whole landscape?
*  Of course not.
*  But the problem of this is the function I would like to make small is a very important engineering thing.
*  And I think there's been a huge progress in the last 20 years from ad hoc optimization schemes.
*  Many things like support vector machines started by talking about weird large margin and eventually said, oh, look at just a loss function we're minimizing.
*  However you get there.
*  And so I think it is progress to think about it.
*  I can tie this in a very concrete way back to the generalization problem, right?
*  So let's talk about like the landscape over the set of say, degree 50 polynomials that set up by trying to minimize the squared error to fitting 10 points that are near a line.
*  Okay.
*  There's a huge space of degree 50 polynomials that exactly go through all the 10 points.
*  If I pick a random polynomial from that huge space of zero error configurations in the landscape, I'll get an extremely wiggly polynomial.
*  But if I start from a polynomial with zero, all 50 coefficients zero and I do gradient descent, I'll end up with a polynomial that's not that wiggly.
*  So I'll end up at a very special point, a very special restricted non wiggly point in that landscape.
*  Whereas the entire landscape is dominated mostly by wiggly points or wiggly polynomials.
*  So basically, because the trajectories are limited, we don't get overfitting.
*  And to tie that back formally to an optimization, you're optimizing not just fitting, but fitting plus minimal wiggliness, which is what we call regularization.
*  But we're not putting, we're not putting that in as an explicit term in the cost function.
*  But we are putting that in as an engineering criteria.
*  We're saying what we want is something that fits the points and is minimally wiggly.
*  So it's not an explicit regularization.
*  It's implicit.
*  But note that what you've done, again, I'm talking not to you because you know this, I'm talking to the students.
*  Yeah.
*  That what you've done cleverly is saying what I really care about is something that fits the data well and minimizes the wiggles.
*  And that is something that you as a mathematically gifted person will say, and you can actually measure how wiggly they are and quantify how good a job you do in terms of minimizing the wiggliness.
*  And that's precisely something which is called regularization or shrinkage or smoothing or any of these things are all doing the same thing.
*  They're minimizing wiggliness.
*  So you're not putting it as a penalized something.
*  You're doing it through search.
*  But note that I want the students to know, again, you know this.
*  I want them to note that what Surya is doing is really thinking very clearly what his true loss function is, which is not just fitting the data because there's an infinite number of ways to do that.
*  It's that plus some wiggliness penalty.
*  And that's really what you're optimizing by your search.
*  Amita, I want us to hear from you as well.
*  What do you think about all this?
*  I would agree with basically Surya and LiveBoard, although they have voicing points.
*  I think the trajectory is important because trajectory decides, especially like since I'm working more in the area of reinforcement learning, if I am starting up with an agent and if I do not have the right trajectory, I can end up with an agent that doesn't know anything.
*  And yet at the same time, the landscape is important because unless I define my reward function properly, I'm not going to reach any goal.
*  So I cannot say one is more important than the other.
*  For me, both are important.
*  So reinforcement learning is all about, one of the things it's all about is that when you take action in the world, it changes the world.
*  So I have a naive question.
*  It's good to be naive because you can ask questions like this.
*  So thinking about the learning trajectories and landscapes, does reinforcement learning or a different setting imply that a learning trajectory could actually change the landscape?
*  So usually you think of there is a static landscape and then you're optimizing to minima.
*  But could the trajectory, and I thought of this as well, Surya, when you were talking, starting with the space of possible sets of 50 polynomials that you could start with, that sort of thing, or reinforcement learning.
*  And Amita, I'm asking you, can the learning trajectory create a dynamic landscape essentially?
*  It's an interesting idea and I think it can.
*  I think it can.
*  We just need to, you know, like for example, when we talk about auto RL, we are kind of doing that only where we are having a dynamical landscape.
*  And that is a dynamical reward function which is going to be updated as the model is learning as the agent is evolving and seeing the world.
*  So it is an interesting idea and I think definitely it is possible.
*  I would say that.
*  You can phrase it either way. So imagine searching over the space of different neural net architectures.
*  Yes. You can either say that each time you change the architecture, you add in more hidden nodes, of course you change the landscape, or you can go meta and say oh it's just searching a bigger space, the landscape includes all the architectural choices.
*  I think reinforcement learning makes this feel a little bit deeper.
*  And it's still very much the same thing that you say, am I changing the world, or is my model of the world so big that includes everything in terms of the search base.
*  They're probably both useful I think mostly we tend to think of, at least I tend to think of things in terms of, here's a huge search space, including all architectures and all agent structures and everything I could ever build.
*  It's just a really really really really really big search space. And now we need to find the right trajectory in it. But I guess you could instead say okay I want to picture a whole bunch of smaller search spaces, and then tweak the hyper parameters to find a nice world that has nice trajectories
*  and people do that sometimes. Sometimes there's a whole lot going back for decades, continuation theory says start with an easy problem you know how to solve, and have some hyper parameter you gradually tweak that makes it into a really really hard problem.
*  So you manipulate the world from a simple approximation to the world continuously to a complex one in order to be able to find the solution to complex one. So that's a classic optimization trick that explicitly says I will change the world from the one I know how to solve smoothly to one I don't know how to solve.
*  That's not used very much in deep learning.
*  Yeah, I think RL theory is incredibly fascinating and people are making interesting progress on RL theory in simple settings and RL theory has its own kind of version of convergence proofs to the best value.
*  You know oftentimes in RL you want to find the optimal value function or optimal policy, and you have various algorithms that you can show in the space of policies or contraction mappings like you know your policy updates and iterations and so forth and you know Bellman updates and so forth and you can show that in the space of policies you're contracting and then you're these updates are contracting so you converge to a particular policy and then you can show that there's no policy that's better. So I think that's super cool, but they rely on like a complete model of the environment like all this and these proofs break down.
*  When you don't have complete knowledge of the environment, when you have to approximate it, when you have an yeah and so I think there's a lot of interesting work for theory to be done there.
*  Yeah, I think it's much harder than the theory that's being done when you have an optimization problem with fixed out of the fixed architecture and you're trying to understand trajectories and gradient design is much harder because of temporal dependencies and so forth.
*  But there's really, yeah it's super exciting like you know for students like you know I don't follow this field except from afar but you know the people like Shab Kakade, Eldad Hazan, my colleague Teng Umad, Stanford like they've done really cool theory papers on this stuff.
*  And there's many more than I'm leaving out for sure.
*  Alright, I have two more topics for us and then we can finish up because the hour is flying by. One, regularization. So dropout was helpful for the deep learning revolution in 2012 with Alex Net and dropout was at least inspired by stochasticity in the brain and so neurons don't fire reliably.
*  So the idea, at least partial idea, was that sometimes if a neuron doesn't fire it's like a unit when it's not active. So the idea of dropout is you turn off usually half the units on the forward pass and also on the backward pass when they're being updated through back propagation.
*  So two questions, you know thinking about the relationship between optimization and regularization. Does the brain have a built-in regularization mechanism? Because there are other, you know another way to regularize in deep nets is to just inject a certain amount of energy into the brain.
*  So the idea, at least partial idea, was that sometimes if a neuron doesn't fire regularly, it's like a unit when it's not active. So the idea, at least partial idea, was that sometimes if a neuron doesn't fire regularly, it's like a unit when it's not active.
*  Which is the same thing, you know the same idea as firing neurons. Basically I would be amiss if we didn't try to talk a little bit about the way that brains do deep learning and I'm wondering where regularization fits in that story.
*  That's a good question. I mean short answers we don't know.
*  That's always the problem, that's always the answer.
*  That's true.
*  We can still speculate, we can still speculate. I can give you my intuition. I mean yeah so synapses are unreliable. I think drop connect is a little bit better of a model than drop out where you randomly drop synapses. So yeah synapses have regular probabilities of failure.
*  And they're relatively high, like 20%, 30% chances of failure of transmission. So I think drop connect is a good model for what the brain is doing. And if it plays a regularization role in artificial networks, there's no reason to believe it doesn't play a regularization role in the brain.
*  How the brain does backprop or whether it does backprop?
*  Well we're not getting into that.
*  We're not getting into that.
*  That's not.
*  It's more on the field.
*  But you know they're doing interesting work but I think there's a lot of interesting questions there.
*  But yeah how does the brain regularize?
*  The noise has to be doing some sort of regularization but I've never seen any clean analysis of how that works.
*  Yeah.
*  So I'm collaborating with Mark Schnitzer at Stanford who has amazing microscopes that record thousands of neurons across 10 brain regions, and we're observing like neurons coming in and out of visual representations over time.
*  So these long time fluctuations in the nature of representations in the brain. So how the heck, how the heck can you decode visual stimuli if your brain's representations are changing over days?
*  Well what we found is that the short time fluctuations like over you know seconds, during the presentation of a single stimulus, their correlational structure is closely related to the long time fluctuations over days.
*  So if you learn decoders that take into account and opting to deal with the short time fluctuations, they'll be robust to long time fluctuations.
*  So i.e. their decoding capacity would be stable over days if they have high performance in a single day.
*  So this connection between two disparate timescales of seconds and days, it implicitly solves the problem of maintaining the robustness of perception in the face of high variability of your representations across days.
*  So we were, yeah you could do mathematical analysis to show that what I said is you can formalize that in social that's true. So I think even though there's a lot of variability in the brain, what we really have to do is measure many neurons at once, and look for dimensions and firing
*  space that are actually stable. And they exist despite single neuron variability. So I think we should be careful to overinterpret how we think the brain works from looking at individual neurons and their behavior.
*  Any other thoughts on this? So Lyle you had started off by saying that regularization is kind of built in if you optimize slowly through stochastic gradient descent.
*  And so I don't need to harp on this point, but I keep coming back to the idea how important is explicit regularization when it could be done implicitly in the way that you, through the learning algorithm and the way that you train your model.
*  I don't really expect the brain to have a little L2 and L1 penalty built into the loss function. Right. It's got to be sort of implicit in there.
*  And I, it's clear that we do do generalization in brains and that it has a distributed representation.
*  And I still don't know in detail, I mean, sure, there's noise, there's these sort of things that we talked about, but exactly how that causes a robust distributed stable representation.
*  Well, there's so many different ways to do it. But it certainly is regularization. Yeah. Or at least it's just.
*  Our models are growing and growing and growing and it could be that if we are vastly, vastly over parameterized, then we don't need explicit regularization.
*  And you guys know about this stuff. I don't. This is why I get to talk naively about it.
*  By the way, there might be an L1 penalty that on synapses, it could be really, it's like a synapse that's stronger, it turned out to be bigger in size.
*  And the brain is super packed as an incredible like if you think real estate and SF is expensive, it's expensive.
*  You know, it's super packed. So a bigger synapse takes up more space.
*  And so there could be like growth limitations that implicitly implement an L1 regularization on the size of the synapse and therefore the strength.
*  So I think that part's easy. It's like, how do you do credit assignment across multiple layers?
*  Like when I teach this to my students, I say the following unsolved problem is unsolved.
*  Like if you state it dramatically, let's say you're a tennis player, right? You're learning to play tennis.
*  You hit the ball wrong. You see that the ball went in the wrong direction.
*  You get your visual feedback and visual coordinates like, you know, a second later, hundreds of milliseconds later, you have to correct some synapses in your motor system.
*  You have like trillions of synapses in your brain. Which one screwed up? How does the brain figure that out?
*  Like we have no clue how that works.
*  Like not even the foggiest theoretical idea of what could solve that problem.
*  Backpropagation is the only game in town in machine learning.
*  But it's not obvious that that's what the game is that the brain plays.
*  Right. So anyways, unless the biological computer can do the gradients very fastly, then we can think of.
*  But it clearly has other methods of different spatial things. You look at the dopamine coverage.
*  You know, there's clearly lots of other mechanisms in the brain that we don't have anything to do in our artificial.
*  Another way I phrase it for my students is like, so there's biologically plausible mechanisms of sensitivity that we measure like Hebbian learning, dopamine-based learning, and I don't know.
*  But if you think about the set of rules for which learning rules for which you can make money off of and the set of learning rules that are biologically plausible, at least under current consensus,
*  the intersection of those two is empty.
*  Right. Which I mean to say is no biologically plausible learning rule works.
*  Right. So that's another big open question.
*  You're going to rile up some people. I said we weren't going to talk about backprop.
*  So I'm going to squeeze us back out of there.
*  So Amito, we started talking about Asimov's laws and something, a different kind of law is in physics, you know, natural laws.
*  And the whole goal is defined in deep learning theory or what are the laws?
*  What are the laws of optimization, regularization, et cetera?
*  But is that newer physics seems to be less attached to laws.
*  And as we all know, biology and deep learning nets with their massive amounts of parameters is, you know, they're messy and complex.
*  Do we need laws?
*  Is that a desirable thing or do we need other principles to account for how to understand deep learning networks?
*  Well, I would say this is again my presumption and this is what I think about it.
*  So I feel we cannot make there are certain cases, certain scenarios, certain applications where we can have explicit laws.
*  But some laws are inherent natural part of, you know, such a multiple, such a vast chaotic system.
*  Because if you talk about neural networks itself, there is a lot, for example, again, going back to reinforcement learning, if I go, randomness plays a very important role in learning there.
*  So, you know, that chaos again, I guess, has some sort of a natural convergence, which by itself have some form of laws.
*  Definitely it needs to be explored.
*  And I haven't done any work on that area to give you any specific answer about it.
*  But that is what I think.
*  Maybe Lila or Surya can add to it if they have some experience about it.
*  But yeah, that is what I would say.
*  I think there are lots of heuristics that are useful for guidance and a number of them come from theory.
*  And as Surya has repeatedly pointed out, as I would say, never trust the mathematician, read the fine print.
*  But if all the preconditions are true, then the theory gives you clear guidance.
*  In the real world, that law, the mathematical rule, becomes a heuristic because you violated the assumptions.
*  And I think part of what we're building up in deep learning is a set of heuristics.
*  Drops out with dropping out half of them seems to work pretty well.
*  It's not something that's super worth fine tuning.
*  That's a nice way to put it.
*  So we've got a bunch of heuristics, all of which in some limiting case have some very strong math.
*  But we don't live in that limiting case.
*  I've never seen an infinite data set.
*  I've never seen infinite compute power.
*  These are all things that my mathematician friends seem to like, but I can't seem to get a hold of them.
*  Where is that infinitely large computer?
*  I just didn't like that.
*  Even a little Turing machine would be fine.
*  I don't want a big one.
*  But I think the heuristics really are nice.
*  And the beauty of having things from math is they often give us starting points for heuristics.
*  Sorry, anything to add before?
*  I'd like to end on an optimistic note.
*  I believe that eventually, like 50 years from now, we'll have kind of a unified theory of how intelligent behavior emerges from distributed nonlinear systems that will apply to biology and artificial intelligence alike.
*  Now, there's an oft quoted trope that's saying that we shouldn't look to biology to develop AI, which is like airplanes versus birds.
*  It would be folly to have an airplane that flaps its wings like a bird.
*  But if you look at the laws of aerodynamics, there's two problems that need to be solved in flight.
*  There's lift and there's thrust.
*  Airplanes and birds solve those two problems in completely different ways.
*  Flapping wings versus jet engines.
*  But the problem of lift is solved in exactly the same way.
*  An aerodynamic wing shape that creates high pressure on the bottom, low pressure on the top.
*  So just like that, and woe unto any flying object that violates the laws of aerodynamics.
*  So in the same way, just as aerodynamics governs both the dynamics of birds and planes, I think there will be laws to govern distributed emergence of intelligence.
*  And they'll apply to both machines and humans.
*  And they might solve it in different ways.
*  Some of the problems are different ways, some of the problems are the same way.
*  And I hope that before I die, we'll see the glimpses of the beginnings of such a unified theory.
*  That's it Neuromatch students. Get on it before Surya dies.
*  Amita, Lyle, Surya, thanks. I know Amita, your alarm went off, which means it's time for us to go.
*  So thanks guys for joining me. Sorry it went by so fast.
*  Thank you. It was nice.
*  Yeah, yeah, fine. Thanks.
*  Brain Inspired is a production of me and you.
*  I don't do advertisements.
*  You can support the show through Patreon for a trifling amount and get access to the full versions of all the episodes,
*  plus bonus episodes that focus more on the cultural side but still have science.
*  Go to braininspired.co and find the red Patreon button there.
*  To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year. Find them at thenewyear.net.
*  Thank you for your support. See you next time.
*  Thanks for watching.

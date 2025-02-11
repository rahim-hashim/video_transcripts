---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5234s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 13420
Video Rating: None
---

# BI NMA 01: Machine Learning Panel
**Brain Inspired:** [July 12, 2021](https://www.youtube.com/watch?v=7MddIo1hj9s)
*  At a very high level, we could say that the organism has evolved to process, I'm going
*  to use big terms here and I'll explain what they mean, but a manifold of sensory signals
*  that are out there in the world.
*  If you think of a deep neural network or all these dimensionality reduction methods that
*  we talk about, they're really about learning different manifold of sensory representations.
*  Once you accept that you need to do model work for your behavioural work, there is no
*  way back.
*  It is like a dimension reduction for the data.
*  So once you have a model, you form an idea, you form a narrative about what's going on,
*  then you can remember it for a long time.
*  If you want to find a new island, it's impossible not to get lost first in the ocean.
*  So if someone really wants to kind of work on some really novel ideas, right, it's at
*  the kind of a frontline, then you really need to get lost before getting there.
*  Oh my God, are you crazy?
*  This is career suicide.
*  Don't do that.
*  The main point is if you believe in something, do it.
*  Don't listen to the trends.
*  Things get in and out of fashion all the time in every single piece of science.
*  This is Brain Inspired.
*  Hey, it's Paul.
*  This is the first in a series of special little episodes I'm doing in collaboration with
*  NeuroMatch Academy, the online summer school for computational neuroscience.
*  So each of these episodes is a panel discussion surrounding experiences with topics of the
*  past week at NMA.
*  This is the machine learning module covering model fitting, general linear models, dimensionality
*  reduction and deep learning.
*  Here to share their experiences and thoughts and feelings about these topics are four people
*  you'll learn more about in a second.
*  So we have Athena Akrami at University College London in England, Dimbaba at Harvard University
*  in the USA, Gunnar Blom at Queen's University in Canada, and Kunlin Wei at Peking University
*  in China.
*  And I will just say that in addition to talking about their scientific experiences regarding
*  these machine learning topics, there's a lot of wisdom and encouragement shared as well,
*  as you heard in the intro there, especially in the second half.
*  You can find the NeuroMatch Academy website at academy.neuromatch.io.
*  But I also linked to all the information for each of the guests today in the show notes
*  at brandinspired.co.
*  slash podcast slash NMA-1.
*  And with that, I guess we're going to just start by going around and I will just ask
*  you guys to introduce yourselves and just to be a little different than usual, let's
*  go in reverse alphabetical order here.
*  So Kunlin Wei, Kunlin, can you introduce yourself and talk a little bit about how what you do
*  interacts with how you use some one of the modeling types that has been talked about
*  over the course of the recent tutorials?
*  Yeah, I understand the first week is about model fitting and also GLM models.
*  I think that pretty much related to my own research as I'm a motor control guy.
*  I'm doing study how perception actions.
*  I actually my bachelor degree was studying biomechanics of human movement.
*  Then I went on to study motor control, did my PhD in Penn State.
*  Then I did a postdoc with Conrad Kurding.
*  And somewhere during my PhD years, I also did a master degree in electrical engineering
*  and then I learned something.
*  Is it hazy now?
*  You can't quite remember.
*  You said somewhere in there you did a master's degree.
*  Because it's a dual degree, right?
*  And it just take credit and doing a scientific project.
*  I kind of scattered along my PhD years.
*  Then I went to Chicago and did a postdoc with Conrad Kurding.
*  At that time, also working in We Have a Patient Institute of Chicago.
*  So I have some kind of medical experience.
*  Then I came back to China and work in the department of psychology.
*  So now I do a little bit more related to cognition.
*  But my own research is more about perception action, especially motor learning.
*  And so you're kind of focused more on the GLM side.
*  Maybe we can speak to that a little bit later in the show then, huh?
*  Yeah, definitely.
*  And you see, my research tool is more about behavior.
*  So behavior studies.
*  Then we need those modeling tools to make that.
*  You're all about sensorimotor adaptation.
*  Is that right?
*  Actually, not really.
*  Now I'm doing some interesting stuff.
*  I study, for example, astronauts, et cetera.
*  Oh, man.
*  All right.
*  Well, we're going to have to talk about that, of course.
*  Okay, thanks.
*  Thanks, Kunlin.
*  So Gunnar, I think you're next on the reverse alphabetical order here.
*  Yeah, that is very unusual.
*  Yeah, I know.
*  It's very indecent.
*  We have a very biased sort of like name ranking here.
*  So hi, everyone.
*  My name is Gunnar Blom.
*  Since Kunlin started with like a bachelor's degree, my original degree is in physics.
*  And then like many people in computational neuroscience, I think.
*  And at some point, I sort of got a little bored about thinking about solid-state matters
*  and like inert stuff.
*  And I thought, hey, wait a minute.
*  There's like living beings and like there's physicists that work in that area.
*  That sounds really fascinating.
*  And then I saw a talk in my physics department about some physicists, and I unfortunately
*  can't even remember the person's name, applying chaos theory to understand epilepsy.
*  And that just blew my mind.
*  And from that point on, I was set on neuroscience, and I got very lucky and was very fortunate
*  to be still in that field.
*  And so now my main research is very similar actually to Kunlin's research, sensorimotor
*  control in general.
*  So I use the sensorimotor control, so essentially how our senses guide our actions, as a paradigm
*  to try to get insight into how the brain works.
*  And so I'm now a professor at Queen's University in Canada.
*  Do you think, I'm just going to jump in.
*  Do you think that anyone just calls themselves a straight-up neuroscientist?
*  Everyone says I'm a something-neuroscientist.
*  There's no such thing as just a pure neuroscientist, perhaps.
*  I don't know.
*  I would totally agree.
*  And this is one of the nice, fascinating, and just amazing parts of the neuroscience
*  field in a certain way, is it's so multidisciplinary, right?
*  And I really enjoy working with people that are in neuroscience, but whose background
*  is really from anything, right?
*  From chemistry to medicine to engineering, physics, math, computer science, you name it.
*  Molecular biology?
*  Anything, of course.
*  I just noticed you didn't name it.
*  Some of us have molecular biology backgrounds, Gunnar.
*  Come on.
*  I can't possibly enumerate all disciplines.
*  There's even people from economics working in here, right?
*  Yeah.
*  Yeah.
*  Dumbah, what slash neuroscientist would you classify yourself as?
*  That's a difficult one.
*  I would just say computational.
*  So I have a background in electrical engineering and mathematics by training.
*  I came into neuroscience about 15 or so years ago, and someone mentioned GLMs earlier.
*  So I did my PhD with Emery Brown, who together with a group of other people is one of the
*  persons in neuroscience that brought GLMs to our analysis toolkit.
*  So I lead two different kinds of lives, and I'm not sure if people in those different
*  kinds of lives know that I even lead these lives.
*  So one that I've been very excited about recently, I got bored when I started my faculty
*  job and I couldn't understand deep learning.
*  So I started getting interested in the mathematics of deep learning.
*  So that's one kind of life that I lead.
*  Now it turns out that it's related to my other life in neuroscience, and we can talk about
*  this later in the podcast.
*  So I work with experimentalists to develop encoding models as it relates to this module,
*  so GLM type models, but a very specific kind of GLM model in the following sense.
*  So if you think of a GLM, the vanilla one, you typically have to pick the covariates
*  that you want to use to develop your models.
*  Now if you think of deep learning, what deep learning does that's really nice for you is
*  that it automatically extracts features that you can then use for a task.
*  So a lot of my research has been about how do you develop neural networks in a principled
*  fashion, so from very basic principles, so mathematics of deep learning, but how do you
*  utilize them then for dimensionality reduction and to solve automatic encoding learning problems
*  in neuroscience?
*  And we can go through some of the details of this later in the podcast.
*  But yeah, thank you for having me and I'm looking forward to hearing from everybody
*  else.
*  But would you consider yourself almost more interested in the tools used to analyze data,
*  more so than sort of the questions about what the brain is doing and how to understand the
*  functions of the brain, et cetera?
*  I would say 60% the former and 40% the latter in the sense that, so I mean, the typical
*  motivation for deep learning in computer science is hierarchical processing, right?
*  So one of the things I'm fascinated about is how does the brain process information
*  in a hierarchical fashion?
*  So if I present to you a cat versus a dog, you can tell them apart.
*  If I present to you two different breeds of cats, presumably you're using information
*  at different scales to be able to tell them apart.
*  How does the brain actually do this and how can we utilize deep learning or develop deep
*  learning models from first principles that can help us answer these questions?
*  Yeah.
*  All right.
*  We are at the end of the alphabet at A. Athena, thanks for being here.
*  You want to jump in and tell us about yourself and how what you do relates to one of these
*  modeling topics.
*  Yes, sure.
*  Thanks, Paul.
*  Okay.
*  Following the tradition of starting from undergrad, my undergrad was in bio-medical engineering
*  and control engineering double major.
*  And I quickly became kind of disillusioned after that training in engineering, just like
*  in terms of what I really would like to do is science, not engineering, meaning that
*  I'm looking for just kind of answers and hows and whys and not necessarily kind of finding
*  solutions for daily life problems.
*  But during my undergrad, I did some work developing a BCI system, brain computer interface system,
*  and I did a lot of linear and nonlinear classification of EEG signals to predict movement imagery,
*  basically movement from the from mental imaginations.
*  After that, I started my PhD in computational neuroscience and theoretical neuroscience,
*  actually developing some dynamical system attractor network ideas to understand interaction
*  between short-term memory, long-term memory, and they're used in kind of ambiguous perception
*  when we deal with some sort of a noisy, ambiguous inputs, how we use our long-term attractors
*  in order to kind of deduce these ambiguous patterns.
*  And then after when I started my postdoc, I was thinking I'm going to continue being
*  a theorist or computational neuroscientist, but after six months, I just like, that was
*  the postdoc was in an experimental lab with Matthew Diamond, and I just like decided I
*  want to start doing my own experiments and just like collect my own data and think about
*  my own projects and ideas.
*  So I started to become also an experimental neuroscientist.
*  And then I continued that working with rats, working memory, decision making, various type
*  of things with rodents.
*  And then now I have my own lab in Science Very Welcome Center in UCL in London, and
*  we use human, rats, mice, and computational models.
*  And we would like to try to understand how basically these different species would kind
*  of infer regularities and meaningful patterns in the environment in an unsupervised way,
*  in an implicit way, right?
*  We know that like, evolutionary speaking, different brains are equipped with kind of
*  a certain machinery to just like learn a structured input around us, right?
*  Whether that can be just like, you know, a human baby that starts to learn language,
*  which is a very structured and complex auditory input, or it can be also other things in the
*  daily life of our rodents.
*  And then right now, we use different types of computational tools in the lab to, from
*  descriptive models like GLM, in order to just like make sense of the very complex behavioral
*  data that we have from our animals, because they are performing pretty complex cognitive
*  tasks, rats on mice, very similar to our human subjects.
*  So just like to describe the behavior, we use various type of descriptive models, GLM
*  fitting, we use neural network models to create kind of hypothesis in order to then test them
*  in experiments.
*  And we use also various types of kind of normative models, right?
*  Bayesian framework and other type of normative models to try to again explain behavior.
*  It's interesting. So I come from an experimental background.
*  I had Nathaniel Daw on the podcast a long time ago, and I think offline he was I don't
*  remember if it was during the podcast, but he was telling me that, you know, he and a
*  few other theoretical neuroscientists were considering whether they needed to start labs
*  because they're like heavy on the modeler.
*  So I came to modeling if I could if I could say I've you know, I've done modeling.
*  So I don't know. I'm not a modeler.
*  I've done modeling, but I came to it through experimental neuroscientists.
*  So I'm wondering, like, what what regrets do you have, Athena, for or was it the right
*  move to to open that experimental side of things or?
*  No, I'm very happy about that.
*  I'm very happy and I'm actually very happy that I'm I'm running an experimental lab from
*  theoretical background.
*  I think that's that's yeah, it was a yeah, it was a very right move for me because now I
*  kind of can understand both camps, right?
*  I can talk their language.
*  I can talk to the computationalist, the theorist, and also at the same time, kind of very
*  just like thinking about experiments on a daily basis.
*  And and and I know the complexities of data collection and working with animals and
*  limitations and all of that.
*  So I think I don't regret that decision.
*  Well, who do you find more optimistic theorists or experimentalists?
*  In terms of understanding the brain one day?
*  This is a question for everybody.
*  It's not. Yeah.
*  Yeah. Yeah. Which side of your personality?
*  Because nothing in experiments works out at all.
*  Like the models say it should or the theory says it should.
*  So, yeah, yeah, yeah, that's true.
*  So in that sense, maybe theories are more optimistic.
*  But on the other hand, I mean, I think soon also a lot of theorists can can become
*  disillusioned that like maybe it's more complicated than what they think that they
*  can put in their models and in their theories.
*  So then in those days, maybe experimentalists, at least they they have the joy of seeing
*  the data, working with the real data that always surprises us.
*  So you see, like what I learned in the past 10 years that I started to be to do
*  experiment myself, like it's just like it goes in directions that you you haven't
*  predicted before.
*  Like the results always like looking when you open the brain, look into the brain and
*  also combine that with the behavior.
*  It's just like takes you into really new, unsure the territories that you hadn't
*  thought of. So that's very exciting.
*  Yes, I think it's it's it's really important that, as Athena said, that theorists
*  understand data.
*  And one of the best ways to really understand data is is to manipulate data,
*  collect data, do your own experiments.
*  And I'm not I don't want to say that that everyone should be doing this.
*  It's really a personality thing, I think, like in the same way as some
*  electrophysiologists stick with one particular technique.
*  Don't look at behavior.
*  Don't look at patients.
*  They just they're in their thing.
*  And some are just like all across the board, right?
*  They take their model from like the mouse to the non-human primate to the human, to
*  the clinic, et cetera, et cetera.
*  And I think we really need to bring this a little back to to to the to the teaching
*  of the first week of NeuroMatch Academy.
*  We really need this diversity of approaches, this diversity of points of views in the
*  field. We need the people that can really dive in into this one particular little
*  topic and be the world expert in this.
*  And then we need the people that have like a broader view that can open up and
*  translate across different disciplines, across different settings, different
*  approaches, et cetera, et cetera.
*  In fact, I agree with you.
*  In fact, I have a different development trajectory.
*  Originally, I was trained like, I would say, more doing descriptive studies.
*  So, you know, for behavior study, you can do just to expand the fund, have different
*  kind of findings, especially if you find some interesting patterns, you just raise a
*  hand, submit a paper, that's it.
*  But it's afterwards, and especially in Conrad's lab, then we started looking at the
*  things with with a theoretical lens and the study of beauty models.
*  Then the the approach become very different because we are getting used to just looking
*  to all kinds of findings.
*  The different labs have different findings.
*  We see there is any some common threat in the data.
*  Then whether we can model it with a simple, realistic model from a minimal model can
*  explain a way of studies, a way of behavior findings, then we are happy.
*  Then starting from there, I was trained to doing modeling for behavior data, especially
*  motor learning and motor control data.
*  Then once you have a model, then you can make new predictions.
*  And of course, sometimes it would get very frustrated because when you're doing this
*  new experiment, the findings will match your model predictions.
*  You want to come back and think about whether you need to modify the model, extend the
*  model. This happens all the time.
*  But for me, it's like once you accept that you need to do modeling for your behavior
*  work, there is no way back.
*  Afterwards, whenever you do any descriptive studies, you're still thinking from the
*  modeling mindset.
*  You think about whether I can derive from the existing model, making new predictions
*  instead of just go blindly in doing some behavior studies.
*  So that's my developmental path from those all these years work.
*  You think through the models now.
*  Has that become sort of the method of approaching any problem is thinking through the
*  model first?
*  It's like this. It's like in my own area, I have, say, several competing models
*  available. And sometimes because in in model control, model learning, especially model
*  adaptation, you have some very good behavior data, very clean ones.
*  But people don't just don't agree on theories behind it.
*  So sometimes those theories, if they don't put down into mathematical terms, it's just
*  talking for me. It's just talking.
*  Unless they're put into equations, then we can distinguish them.
*  So when I look at it, those kind of diverse findings, especially the coming from very
*  different behavior paradigms, I mean, thinking whether there is any some some common
*  theories behind it. That means is there a common model to explain it all?
*  Then if you accept this mindset, you're just looking at your studies or looking at your
*  areas very differently.
*  Dimba, what do you think about has this all convinced you that you need to open an
*  experimental laboratory here?
*  Oh, it's something that I've been thinking about for a while now.
*  Yeah, yeah, yeah.
*  Because, I mean, my own feeling, and I'm not sure if this is what your motivation had
*  been, Athena, sometimes as a theorist, there's a myriad questions that I would like to
*  answer for which the data or the experiments have not been performed in the way that
*  would allow you to answer those theoretical questions.
*  So there's a certain amount of control that comes from having a theory to test and
*  actually having experiment associated with that, that, hey, frankly, sometimes you need
*  to convince an experimentalist to do that, and you might have competing interest and
*  so on and so forth.
*  But related to this and another comment that Athena made is the following.
*  So one of the things what I found fascinating about what you've been saying, Athena, and
*  I guess you've been thinking about this from an experimentalist perspective, but I've
*  been thinking about this from a theory perspective.
*  So one of the things that's been fascinating me is this idea that let's just think of any
*  organism at a very high level.
*  We could say that the organism has evolved to process.
*  I'm going to use big terms here and I'll explain what they means, but a manifold of
*  sensory signals that are out there in the world.
*  Right. And depending on the organism, that manifold of sensory signals that they care
*  about might be different.
*  Right. So why is this interesting from a theory perspective?
*  Because if you think of a deep neural network or all these dimensionality reduction methods
*  that we talk about, they're really about learning different manifold, potentially
*  nonlinear of sensory representations.
*  And I think what's fascinating is that now, let's say I want to I have a hypothesis that
*  says that, OK, the brain, let's say the let's say the early layers of visual processing
*  may have evolved to process different categories of inputs.
*  Let's say dog versus cat.
*  Right now, I don't know the experiment off the top of my head right now, but I imagine
*  that if this is my mathematical hypothesis and I can write this down mathematically,
*  there ought to be some experiment that could help me test this.
*  And I think that's kind of what fascinates me in being able to actually run my own
*  experiments.
*  Join us, Denver.
*  Then he doesn't have control.
*  But what can you speak to that?
*  So there's the issue of the speed of being able to do things because modeling is faster.
*  I'll say faster than experiments.
*  And so it has the potential to really slow you down.
*  I don't know. So you guys can all think about this.
*  Oh, Gunnar is shaking his head.
*  So just, yeah, I'll drop in here really quickly.
*  So I feel that I think when we say modeling, it means a lot of different things to a lot
*  of different people.
*  It took me three years to finish writing a theory or modeling paper.
*  And I know that monkey experiments, for example, take a lot of time.
*  Right. So I think I think I think it's a misconception that modeling is faster.
*  I vehemently disagree, but I'm not the one to talk about it, I suppose.
*  No, but even even even if maybe it's true for some sort of modeling, it can be faster.
*  The thing is that once we start to kind of put them in a kind of synergistic relationship with
*  the experiments, right, then it really doesn't matter how long each component will take,
*  because really you may start from a modeling part of the project, then you have some kind of
*  predictions. You start to kind of do experiments and they are going to feed back into your model
*  in order to change them, to modify them.
*  And it's I mean, that's that's super important to really kind of do to treat modeling at
*  something kind of auxiliary, completely independent of the rest of the work.
*  They really need to be integrated into the whole workflow of the of the projects in the lab.
*  Right. And then then it's it's it's OK, even if some part of the project may take longer than the
*  other, the overall project matters.
*  My last modeling project, I think, took me about 20 years, including starting it as a PhD
*  student, like being lost and absolutely having no answer to describe the data, thinking about it
*  continuously, having ideas that failed along the way.
*  And then at some point there was a click and that's when we actually managed.
*  And then the click led to a series of papers because the theory that we wanted to build this
*  model on didn't really exist yet.
*  And we needed different other components that were too complicated to make them part of the
*  final model. So we published them on the way.
*  So modeling is really like sort of like for me, it's more like a like Kundan said, like more of a
*  mindset. Right. It's a it's a tool.
*  It's a way of thinking. And it's not necessarily that you go and start here and go like, I want to
*  do a modeling project right now.
*  This is like the confines of my modeling project that can happen, but very often is more sort of
*  like a, you know, I want to understand the brain.
*  Well, OK, that's you're not going to solve that tomorrow.
*  Right. This is going to be like your whole career potentially and more, of course.
*  Right. So modeling is the same way.
*  I think that's an extremely important point.
*  Yeah, go ahead.
*  Sorry, I just wanted to kind of make a point following Gunnar's comment that for the students
*  that are basically learning these tools and techniques this week, they really need to know
*  that like mastering the technique is something.
*  But it's actually that's the that's the trivial part of working on any project, which is like you
*  have the data in front of you and then you just like apply a technique.
*  You don't need to analyze it right.
*  I mean, you want to kind of fit a GLM to your data.
*  That's the easy part.
*  The difficult part is to think about which model suits your data and the caveats, the
*  assumptions that you put in the data and why it fails.
*  Is it a really suitable type of model for your data or really there are some sort of a kind of
*  caveats that you better deal with them right now.
*  Otherwise, it's going to really kind of produce very kind of misleading results.
*  Right. So that this this this layer around applying these tools is extremely important.
*  The students should have in mind that like they really need to start thinking about the
*  putting these tools in the scientific context and just like why they are they are they are
*  learning these tools and what is the right application and which assumptions come with each
*  of these these these methods and whether the assumptions fit the conditions of their data
*  set or not.
*  You know, Gunnar's story 20 years for one model just fit my recent experience.
*  I published a modeling paper in back in 2009.
*  Then some people criticize it because there is some prediction that doesn't match the data
*  or my at least my experimental data did not go all the way to the model predicted.
*  Then only recently.
*  And in fact, just last week, I look at another behavior data, another experimental data set
*  published by other people.
*  I think I had an idea because of that.
*  Their data because my old paradigm cannot test my model in the in the unplanned territory.
*  But the new paradigm can actually fit my model.
*  Now I'm thinking about doing new experiment to to say argue against my those previous
*  criticisms on my model.
*  So it has been 11 years.
*  OK, 11 years.
*  So my bottom line is I think the model is it is like a dimension reduction for the data.
*  So once you have a model, you form an idea, you form a narrative about what's going on.
*  Then you can remember it for a long time.
*  So even though I didn't touch the topic for so long, if there's something something related
*  pop up in the data, I immediately see it because I have this kind of a narrative, have this kind
*  of modeling idea in my idea in my mind.
*  So that's my take on the modeling.
*  It by itself is a data dimension reduction for our scientific data.
*  Timbo, sorry, you started to speak earlier.
*  Did you want to throw something in there?
*  I'll make this point quickly, but I think Athena made it somehow.
*  So I think we might be using terminology this vague here.
*  So sometimes mathematical.
*  So there's a difference between method development and data analysis.
*  So sometimes the mathematical tools you need to analyze a certain kind of data do not exist.
*  In those cases, you need to come up with them.
*  And the process of doing so may not necessarily be a trivial one.
*  And in fact, in some sense, it's an experimental process.
*  There are experiments that are going on inside here.
*  They're not actually playing with animals and so on and so forth.
*  Right. But there's something to the method development process that's very similar to
*  experiments. Yes.
*  Biological experiments.
*  That's a great point, actually.
*  Like even in terms of you think of what are models, right?
*  Some people say there's model based data analysis.
*  What is that? Is that a data analysis technique or is that is that a model?
*  Right. So I can build, like, let's say an optimal feedback control model or something like that.
*  Right. And I can say, hey, look, I could compare that to the human behavior and looks very similar.
*  So humans must be close to optimal.
*  Or I can say, hey, look, I fit it to the human behavior and the parameter Delta, whatever, is different across different participants.
*  So now I get very different things out of the same mathematical formulation.
*  Right. In one case, I tried to explain why the movement looks the way it is with sort of like a, you know, and what we call a normative model.
*  So a model that sort of like evolves or falls out from first principles.
*  On the other hand, I use the exact same math essentially to do something more along the lines of dimensionality reduction, right?
*  Reduce the actual movements into a single parameter that I then want to interpret in some particular way.
*  And so the same formalism can can be a data analysis tool or can be like a conceptual model to understand sort of like the foundations of why we do things the way we do or what the brain works, the way it works.
*  So I'm always a little unsure about this classification, right, between tools and models.
*  To me, models are tools in a certain way.
*  But then I'd like to hear from you what you think about that.
*  No, that's that's so the quick point that I wanted to make was that so at the end of the day, in those two use cases, you just describe, don't you think that at the end of the day, there's even when one is not aware of it, when they're using the model to analyze data?
*  Somewhere, there's an there are underlying assumptions about how the data you're analyzing or generated that make it such that you can utilize this tool to model the data.
*  Does that make sense?
*  So totally.
*  Yeah, I said this because because of a lot of the work that we do in the mathematics of deep learning.
*  So I think of deep learning right now as a bunch of Legos, data, weight, nonlinearity, and so on and so forth.
*  But a lot of the work I've been doing, a lot of people have been doing is to try to reverse engineer them.
*  It turns out that in certain settings, you can reverse engineer all of the processing that happens in a deep network from a normative perspective.
*  So does that mean that the deep network has made normative assumptions?
*  I think yes and no, even implicitly, it may have.
*  That's that's but I think we need a lot of time to and a board to discuss some of this.
*  But boards not good for an audio podcast, of course, so we'll have to do it another time.
*  I'm wondering if it'd be a good idea for the students sake if we could maybe go through some concrete examples of how a particular model has either made you change your intuitions about a particular phenomena, made you understand something differently
*  and or just given you a really hard time, you know, just how like some model that you've used that has been talked about in Neuromatch Academy.
*  One of those types of models, your experience with it and how it relates to how it moved your science forward, how it set you back, how it made you cry or jump for joy, etc.
*  I can start with an example of use of GLM in my in my work.
*  So during my postdoc with Carlos Bordia at Princeton, we were having these animals rats that they were doing a working memory task.
*  It was an auditory working memory task. They were hearing the first sound and there was a delay period, the second sound.
*  And the animals need to compare it like the amplitude of the second sound with the memory of the first one and then judge whether it's like louder or not and make a decision.
*  Right. So it's a kind of a delayed comparison of two auditory sounds.
*  And when I was I mean the whole when when I started this project and I wanted to develop it to do this task for rodents, I was really after understanding the neural mechanism underlying working memory maintenance in rodent brain.
*  That was my naive scientific ambition at that point.
*  And this look, can I just jump in?
*  This was kind of the earlier days of this move toward studying quote unquote higher level cognitive functions in rodents, because classically it's been done in in nonhuman primates.
*  So so just wanted to frame it a little bit.
*  Yeah, this task didn't exist in rodents.
*  Like really, 10 years ago, people didn't think that rodents can do this task.
*  It was a very classical task in primates.
*  There is a famous research group, Run For Romo, who developed this task in primates.
*  And so then I had this task in rodents and I wanted to just like figure out what's happening in the rodent brain.
*  And the starting point was just let's kind of inactivate some brain areas, see whether they are involved in that task at all.
*  OK, so I was doing then some inactivation experiments using optogenetics that like you put in a virus that it's going to express some options in some neurons, meaning that after that, if you shine light over that piece of cortex that is in
*  infected with this with this virus and options, then you can shut down.
*  Right. You can just inactivate neurons.
*  And then I collected data and to my surprise, it seemed that like the performance of these animals are getting better.
*  Right. In some of the some of the task parameters that I was testing at that at that initial phase of the experiment, which was extremely confusing because you would usually imagine that like when you inactivate a part of the brain, either you don't see any effect,
*  which means that like that that part of the brain is not really involved in that behavior, or it's just like it's you get some sort of impairment.
*  But just like to see that like performance is getting better was extremely confusing for, of course, I spent weeks to check my code.
*  Maybe I'm just like calculating, computing performance wrong.
*  And then actually then what was happening is just like behavior is much more complicated than what we thought.
*  We were just thinking that the animal what they are doing in this task, they kind of engage in this sequential task.
*  Right. There are the task structures that they receive that first sound delay, second sound, they make a choice.
*  And then the next trial starts and the next trial starts is going to present new sounds, which we as experimenter just give them independence.
*  Right. Of the previous trials.
*  But then what is actually happening is that the animal engages in this sequential task and is going to show various types of biases due to the to the history of previous actions, previous rewards that use previous sensory experience.
*  So then I started to actually then work with a relatively simple logistic regression model, a linear regression model that would just like quantify for me the contribution of different variables in in in in rats performance.
*  So I was then not only including the sounds in the current trial, but also what were the sounds that animal received in one trial before to trial before maybe average over some time window.
*  And then what was the what was the reward is that was was there whether the animal was rewarded or not rewarded.
*  Right. So you just like put some sort of a predictors in your in the GLM.
*  And you want to see that like whether they have any influence on the behavior or not.
*  And that's kind of a simple GLM exercise really taught me that human animals very similar to our human subjects, they have this very interesting sensory biases, sensory history biases, as well as reward history biases due to this kind of a sequential nature of the of the task.
*  And to be honest, then learning that about the behavior helped me to actually then understand the inactivation results helped me understand to also the electrophysiology results that we found in that part of the brain that they were all related to this sensory history.
*  So and link to some sort of, you know, we when we kind of engage in an environment, we receive inputs, we build priors, we use this kind of the priors in our future decision making tasks.
*  And it really opened up a new era into my research. Now from just like focusing on the working memory maintenance, I am now focusing on formation of priors and the use of the priors in the in the context of working memory or any other decision making task.
*  And this is this is all because you implemented a model.
*  Yes, but I have to say that it's also important, like when you implement the model, it's only as good as your assumptions, right, that what you put in the model, right, it really depends, like, so when we and that model was a descriptive model, right, but
*  I want included some predictors that given the literature, known literature about other human cognitive behavior, literature, or in animals, I was aware of some sort of a kind of a stereo biases, right.
*  So then you put things that you think are relevant for this specific behavior, and then you measure them in your model, right, when the your model is a tool to then actually like in a kind of a rigorous way quantify the contribution of these different
*  requestors into the behavior. So it's a really combination of your assumptions that should be an informed assumption, educated assumption, given what we know already into this kind of a new model in order to to explain the new behavior.
*  In that instance, it's not like you set up a model and it taught you new potential avenues. It really is like the model, what you learn from the model is bound by the, the way you set the model up the questions that you ask it. And that in that sense, it's it's definitely a very specific tool.
*  Yes.
*  So thank you, Athena. That was awesome. Because that really brought everything together. Do you think anyone else can can top that?
*  Yeah, I
*  Kunlin says he can top it.
*  Okay, I can give the other side of a coin is how model, how model make me make just make my life miserable in a period of time. At that time, we are we are studying motor learning, right, then in terms of in Bayesian theory is very simple. If you have a, say, large
*  prior uncertainty, then you should learn less.
*  That is, this sounds very simple is because of the prior effect perception at that time. A lot of people, there are a lot of examples. But in terms of a motor system, how a prior especially a prior about your own body,
*  about your own body state, if you have a large uncertainty in the prior, then you should learn less. But we have this idea, right? This is kind of theory driven. But as an experimentalist, I need to find a way to modify my prior in my motor systems prior and modify is uncertainty.
*  Then I remember I did the less work. I tried a different kind of experimental techniques. In the end, I did it. But it took me like a year. At the end of time, I check my code. I tried to seven versions of it.
*  Checking the code is always step number one after kicking the computer, right? Like you have to check your code.
*  Yeah, yeah. So
*  then
*  my solution in the end is very simple. I ask people to sit in the dark for one or two minutes before I turn on a computer screen and ask them to do some auto learning task to quantify the learning speed.
*  This kind of manipulation, in fact, can speed up the learning speed. You see what I mean? If you're sitting in the dark for a long, long time, you have a larger uncertainty about your own body state. Then you learn faster. This is kind of unintuitive. Because at that time, in theory, this makes perfect sense. But at that time, I couldn't get to this point. I couldn't get to this kind of experimental technique because it's not very easy to learn.
*  But I'm glad I tried seven versions of manipulation. Finally, rather less. But this is what one lesson for me is sometimes theory could be right. But when you're trying to come up with an experimental technique to test it, sometimes it's hard. So that's my story about this.
*  Great. Yeah. I'm going to force Dimba or Gunnar to use a concrete example of how modeling has changed your intuition or understanding of something or some instance like that.
*  Yeah, I'll keep it very short. So I started my faculty two years ago. I was a student at the University of Michigan. I was a student at the University of Michigan. I was a student at the University of Michigan. I was a student at the University of Michigan.
*  Yeah, I'll keep it very short. So I started my faculty job in 2015. And a year later, I did something that I don't advise doing is I kind of did a
*  almost a 90 degree. So this was around the time where deep learning started getting really hot and I could not for the life of me actually understand why it was working reading papers.
*  So this is a story about method development. So I started because of some background that I have in certain areas of mathematics, I just started thinking about from scratch.
*  How could I justify to myself that the operations that a deep network is doing kind of makes sense? Weight, value, and so on and so forth.
*  And it took me about a year, year and a half of reading and so one connection that I've made or that we've made is between sparse coding and actually deep learning.
*  Turns out that you can derive certain deep learning architectures from first principles using a sparse coding model, which a lot of people will be familiar in
*  neuroscience. But so the process of starting from a very simple equation, if you look at sparse coding models,
*  there is a very simple set of equations, the process of starting from that, and then convincing myself that yes, actually, this actually makes sense for why
*  a deep neural network does what it does. It took about probably a year, year and a half to at least convince myself of that.
*  Going back to what I mentioned earlier about method development, right? You start in the dark and you have some very rough ideas based on experience.
*  And by reading papers and based on things that you believe you understand or not, you slowly come up with some understanding in this particular case of a normative model that gives rise to deep learning architectures.
*  Do you recall how you got to that point, which is at the beginning of that year and a half or whatever, to think about sparse models? Was there a breakthrough or is it just after reading a hundred papers that somehow it seeped into your collection of ideas?
*  So I wish I could tell you really, but it began just by reading papers and being confused and having this idea of oneself as, hey, I should not be confused. Yes, you should be. That's actually a good thing when you're confused.
*  And then stepping back, and honestly, it was almost serendipitous because I turned out to have a background in sparse coding that I did not think was related to this.
*  And just essentially by relaxing to the process, I just had a flash and then this ballooned into more understanding.
*  I wish I could tell you that this was it, but it was basically working with the process and being patient with myself. I think that was super important.
*  That's what I wanted to jump on because just even in day-to-day, my list of tasks day-to-day, you kind of avoid the thing that makes you feel uncomfortable.
*  And that is like the most important thing to move forward in and to work in.
*  And I think that a lot of people, at least for me, because I didn't have a modeling background, that is the thing of most resistance that you need to push through.
*  Actually, Dimba, I know that you have read Stephen Pressfield's War of Art, and he talks about this concept of resistance and working through the resistance.
*  And I know that you happen to be a fan of that concept. And it's really hard to do, but that's like the most.
*  And I'm only saying this because probably people who are going through Neuromatch Academy are feeling this resistance because it's very confusing because it's a lot of work very quickly.
*  And that's the most valuable thing is when you have no idea what's going on, but you don't even realize it.
*  But at a subconscious level, these things are probably seeping in that will come back later and you'll realize sparse coding is useful for your modeling, pushing forward.
*  Can I add to that? Because I think this is actually super important. And thank you, Dimba, for bringing that up.
*  The fact of entertaining a certain level of uncertainty and doubt as a researcher opens our minds up to learning.
*  And that really relates in a certain way deeply also to what Kunlin said about motor control learning.
*  The more uncertainty you have, the more you can learn. If you think that you're super certain about your knowledge, you will not let any new information in.
*  And so I think in this particular as we advance in our careers becomes more and more sort of like an active or semi-active process where we actively have to sort of like entertain the curiosity, the open mindedness to new ideas and things like that.
*  And if we don't do that, we just will not ever be able to learn. So I really find that very inspiring. Thank you, Dimba.
*  Yes, I second that.
*  Gunnar, do you want to add a story or shall we move on?
*  I can add a very quick story, but from a very different point of view, because I want to make a point with that.
*  And so this is also like a neural network story and from my own research.
*  So when I was a postdoc, I essentially wanted to understand reference frame transformations in the brain.
*  Right. And so I built like these complicated geometry models and kind of things.
*  And then I wanted to know, well, but real neurons don't do geometry, right?
*  They somehow have to process or compute that with parallel processing.
*  And I want to understand how to do that.
*  And so I thought, like, well, obviously, neural networks is the best thing to do.
*  Right. And I was sort of like around 2004, 2005 in the middle of the AI winter.
*  Right. And, you know, as a scientist, I go to my colleagues or the advisors, I would say.
*  And everyone told me, oh, my God, are you crazy?
*  This is career suicide. Don't do that.
*  We're in the middle of an AI winter. We know this will never work, etc, etc.
*  But my postdoc supervisor actually believed in that.
*  And he thought it was a good idea and said, no, I think you should do that.
*  And so I did. And it ended up being like one of my most cited papers now.
*  But also the main point is that if you believe in something, do it.
*  Don't listen to the trends. Don't listen to the fashion.
*  Things get in and out of fashion all the time in every single piece of science,
*  whether that's single cell recordings, whether that's certain paradigms,
*  whether that's certain approaches, they come in and out.
*  Right. And what at some point, like support vector machines were the thing to do.
*  Right. Now no one looks at them anymore. Everything is like, you know, deep networks.
*  These things just come and go. Take the tools for what they are.
*  Know what they can do and just go with your intuition.
*  Yeah. Related to that, like, don't go after what is fashion, what is trendy.
*  I think if you start from our, what is our question, right?
*  Just like, and then understanding our question, if you understand that deeply,
*  then we will find the methods. And sometimes methods can be a very simple,
*  simple statistics can really give us a lot.
*  It doesn't need really fancy machine learning methods to throw out a very,
*  you know, kind of a simple question. So I think if you really could just try to answer the questions
*  rather than apply certain methods and just like, you know, go fancy and go, go, go after
*  what is, what is the, what is the, what is the most hot and fanciest method of the time,
*  then I think we will be less kind of confused and more focused on answering the scientific questions.
*  And this is really all that we wanted to teach you in the first two days.
*  Appreciate the diversities of the models, what they can do for you.
*  And then essentially make the right choice based on the scientific question
*  in which approach, which toolkit is the best way to potentially answer your question.
*  I have a question related to questions. So I agree that it is, it's most important to focus
*  on the question and to frame things from that. But in a practical day to day, like during your workday,
*  work days, how much time do you spend thinking about the question, thinking about the phenomenon
*  you want to understand or the theoretical entity or what have you versus mucking with the model,
*  thinking about how to make the model different and how to make the model work and which version of
*  the model you should use. Like in other words, how much time do you spend thinking about the
*  technical side of the modeling, which is kind of away from the larger issue that you want to,
*  that you originally wanted to focus on. I asked because this was like, I did experiments and
*  modeling at the same time. In both of those, you find yourself in the technical details mired often
*  and you can really lose focus of the bigger picture. Why am I asking these questions even?
*  Like, what was I originally interested in? So I'm wondering about your experience with that on a
*  daily basis. Maybe I can just quickly say that I don't have a definite answer because I think
*  that depends a lot on what you're actually doing and that the technical implementation side
*  can take arbitrary amounts of time. But what I want to say is that if you don't have a specific
*  goal and a specific question in mind, then you will take way, way, way more time and potentially
*  never finish because you would never know when you're done. I guess I agree with Gunnar as it
*  really depends on what kind of research area you are in and what kind of research question you're
*  asking. For example, for motor adaptation and more into one area I'm focused on,
*  you have very clean data and the data can be easily modeled. Then you can spend more time
*  thinking about modeling, especially when multiple labs producing diverse results with different
*  paradigms. You're thinking about maybe a universal model to explain all kinds of phenomenon.
*  But for some other areas, for my other research interests, there is no way you can model it.
*  For example, I have some work on motor control in autism children. Because I'm doing motor control
*  studies, there is only vague theories about why people, autistic children, have different
*  developmental trajectories. One theory could be the social deficit or so-called communication
*  deficit comes from early deviations in terms of perception action. Well, in this particular area,
*  there are not many clean data to model. Then I need to do a lot of descriptive work. As I
*  mentioned earlier, I think my work is more focused on descriptive work. It's the same thing for,
*  as I mentioned before, when I was studying working with astronauts, or you call it
*  tachyonauts, the Chinese call it tachyonauts. Then there was a lot of mysteries there in terms of
*  perception action in space. But there was no way we see a clear pattern. Instead, you need to collect
*  a lot of data before you can come up with a theory. For example, you probably know we're doing those
*  multiple sensory integrations. Those Bayesian models are dominant. But even in a simplistic form,
*  their challenge in space could be space sickness. The mechanisms of space sickness,
*  you think it's simple, it could be a vestibular disturbance, but it's not as simple as
*  you can use Bayesian models to explain it. It's really complicated. In this kind of area, you need
*  to do a lot of experimental work or just collect data to figure out what's going on.
*  Just to go back to the original question, it really depends on the topic you're focusing on.
*  If the area has clean data, has those well-recognized experimental paradigms,
*  so everybody can agree on the data set from different labs, then you can go on with your
*  modeling. If the area is more immature in a scientific sense, in a modern sense,
*  then you just need to collect more data and do more descriptive studies.
*  Good. Damba, how about you?
*  I'll take it a bit more philosophical. To me, at least in my own experience,
*  I think about it as an iterative process. There's a big question that you would like to answer.
*  And I think, at least when I see this in my students, the most important part
*  that they're missing or that they forget, and I know they can graduate when they get over this,
*  is first they get attached to the big question, which is a big mistake, in my opinion. And two,
*  they fail to take action that might lead them to smaller questions that can give them more and more
*  clues. So in my own experience, it's that failure to take action that actually leads to the inertia,
*  to the resistance that you were talking about earlier. Because at the end of the day,
*  I don't think it's actually about answering the question itself. It's about how you ask even better,
*  better questions. And the question itself might actually change. So there's an iterative process
*  that has to involve some form of action, in my opinion.
*  Damba, how do you get your students to get to that point? What do you do?
*  Yeah, teachers.
*  Oh, how do I get them to get to that point?
*  Or to just overcome that hurdle?
*  I think in the, I don't think I do it. I do it so that they don't notice it in the following sense.
*  So I think this is where the advisor becomes super important in the beginning that, so typically,
*  the way I set things up is that their first few projects, I guide. So by them coming to me and
*  being like, this didn't work, blah, blah, blah. And we have a big question. And I make suggestions
*  that lead to action that they then see work. I think then they trust the process.
*  But you let them get lost first?
*  I do. I do. Definitely. It's useful. It's very useful.
*  Can you unpack why you think it's useful?
*  Sorry.
*  Say again? Can I unpack why I think it's useful to get lost?
*  I mean, it might be part of my own bias because I find that, so if I can get to an answer tomorrow,
*  or maybe this is me being torturing myself. If I have question A to answer today and I can get to
*  an answer tomorrow, that's not exciting to me. Because I think along the way, I'm missing all
*  these other things that may not have come to my mind just by getting into directions that may not
*  necessarily lead to something else. There is a saying, Demba, I don't know whether it's Chinese
*  or other nations, that if you want to find a new island, it's impossible not to get lost first in
*  the ocean. So if someone really wants to work on some really novel ideas, it's at the front line,
*  then you really need to get lost before getting there. And I think I totally agree with you. And
*  my philosophy really is very much similar to what you described in terms of this iterative
*  process. And we really need to let students get lost, because eventually those students want to
*  become independent researchers. And then if they really want to work on novel ideas, they need to
*  be trained to really get lost a lot of the times and then come out of that swimming world and come
*  out of that getting lost in the ocean and find a new island. I have a controversial question.
*  Do you think in some sense that we fail to teach them this? So for example, when I read papers,
*  I'm actually, I would love to see a journal that where you have to talk about what didn't work.
*  So you publish your paper, you had great results, but I want to read and I want to hear about what
*  actually didn't work. Because I find that that's what I learned the most from. So do you think that
*  in some sense, we're failing our students or the younger generation by not, I'm not talking about,
*  okay, let's talk about our failures, et cetera, but just by going through the process of things
*  that did not work and how you actually do research? I think that's extremely important. Yeah. I mean,
*  we usually, because when it gets to the communication of our scientific outcomes,
*  we really just talk about the successes. And all this kind of a process is lost internal to the
*  lab. And people then just tend to forget about it and just talk about, okay, we found this new island,
*  we found this new island, we found this new island. But how about, yeah, as you said,
*  the underlying hidden process. It's extremely important to talk about that. I totally agree.
*  Right now, over the past six, eight months, one of my students, she was feeling extremely lost.
*  I've been always supportive of her attempts, try to design new experiments and just try different
*  variations. But I really knew that it will eventually pay off. But that process of getting
*  lost, it was very frustrating for her. And as a supervisor, it was also kind of painful for me
*  to watch it, just like this student feels lost and feels... But it's a very subtle thing. It's a very
*  tricky situation because you also don't want the students get to a point of complete despair and
*  getting completely give up on the idea of pushing more on that specific research project. So I think,
*  as you said, it's important to just in that process, give them maybe some sort of a shorter
*  term, practical, feasible goalpost to just give them motivation. It's rewarding for them on this
*  process that they get lost, but then there is a kind of a concrete result that they can achieve
*  and then we'll give them hope and then they can continue. So it's a very subtle process, I think,
*  but extremely important. I actually agree. Just one question, because our podcast will be heard
*  by a lot of students. I'm just asking a question on their behalf. They may ask, because we are all
*  faculty members, and do we have the so-called survivor bias? We're talking about all kinds of
*  frustrations, especially long-term frustration. We know when we juggle in between model and data,
*  sometimes you get very frustrated because it takes a long time. But for students, think about it.
*  Some of them may experience difficulties of, say, failed experiments, failed modeling for,
*  for say over a year. How we can still encourage them saying, come on, this is still normal
*  in terms of research. Otherwise, they will just accuse us that you guys have a survivor bias.
*  Does everyone agree that you do have survival bias? That is just a fact of life.
*  So then you have to bake into the equation there, Kuhnlin.
*  A, there is survival bias and that's going to happen and B, you still should keep going.
*  Can you explain to me what survival bias means?
*  Because we are all survivors. We, we, we say we went through, maybe we went through a lot of
*  tortures in, in, in our PhD years, in our post-doc years. We have a lot of difficulty, but we went
*  through it and we somehow are working as a, as a faculty. So in students' eyes, we are survivors.
*  We are, we are the winners. So think about it in their shoes is sometimes like that,
*  they face great difficulties. Sometimes they will get very, very frustrated.
*  That you guys somehow, despite the luck of the draw at about 40 different points along the way,
*  the right mentors, your model working out, an editor at a journal accepting it in a high tier
*  journal for whatever reason, those sorts of things, in addition to your hard work and your,
*  your own intelligence and persistence, that all those, all despite all of the, the positives and
*  negatives that has, that have happened, you're the ones that have survived because someone has to.
*  I see. I mean, I, I actually don't think about it a hundred percent this way, but I can see how
*  somebody else from the outside might, might perceive it as such. So I don't agree with the
*  concept, but I can see how it might be perceived as such. But the answer that I have to this,
*  I don't think it stops this thing, the frustration we've discussed, the, I think the relationship
*  with it evolves over time as you gain more experience, so on and so forth. But in my
*  opinion, it never stops. I don't, I don't think there's a point where you've arrived.
*  I mean, at least this is my perspective. You don't arrive and that's, and to me,
*  that's actually exciting. When I've arrived, that's when I got to change career. That's,
*  that's, that's how I think about it. But it is for a student. I think it can be very,
*  it's a tricky situation, right? And in particular, if you think about a professor running a lab and
*  essentially running their own research agenda, right? I don't know, maybe I want to put like
*  three students on a problem that is really, really hard. And I know two of the three will fail,
*  but you know, this is what my grant proposal says I'm going to do. So I'm going to do that.
*  Right. And, and of course, personally, I would never do this because I think it's just super
*  wrong. But it's also in terms of the sort of incentive structure, the way that we value
*  research right now, research output is only in terms of positive findings. So in my example,
*  the two students that would have failed, essentially, they would have failed because they
*  have nothing positive to show for, but I'm sure they would have lots of experience that would be
*  very valuable to communicate, but we just don't value it in the, in the field. Right. And I think
*  this is more of a sort of like cultural problem that we have among many others in science that we
*  we've become sort of this like stronger and stronger merit of Christ, Christy and where,
*  where, you know, only, only if you're doing really well, and you get really lucky, you'll survive.
*  And if you are, you know, if you don't agree with that system of sort of like, you know,
*  publish or perish, which pretty much is the system right now, then you will fall,
*  fall through the cracks. And personally, I have very strong opinions about that. And we're trying
*  with Neuromatch Academy to push against this, but it's a hard, it's a hard fight.
*  So thinking about feeling lost and learning all these modeling techniques,
*  you know, I'm kind of curious how you, how long it takes to feel comfortable with these things.
*  And then once you, you know, really have them, you know, do you feel like you can
*  now apply them to whatever questions you have? Like, do you feel a level of comfort with all
*  of these different modeling skills that, you know, is it essentially is it worth feeling so lost for
*  so long? Like, when do you feel a certain level of comfort where you feel like, okay, now I can
*  use these tools and apply them to various questions?
*  I can kind of jump in briefly. I think it is, it is worth it, because all this like getting lost,
*  the process of really trying to understand something, trying to figure out something,
*  trying to kind of get to the right question, understanding how to ask the right question,
*  and how to apply the right method. It's going to train us as some sort of a scientist that we can
*  kind of apply our skill, not only in our direct field of research, right, but in the kind of a
*  broader sense of event. Like, I have a personal anecdote here that over the past year, due to
*  some incidental involvement with coronavirus, I developed long COVID, and I got involved in
*  some researches, patient-led research, particularly understanding long COVID,
*  their different characterization of long COVID, which symptoms are involved, which symptoms can
*  be predictive of developing long COVID during the first kind of acute phase and things like that.
*  And I'm doing a lot of kind of a data analysis and modeling in that field, which is a very
*  different field of research from my neuroscience systems, neuroscience lab that I'm running,
*  but the skills that I'm using there are basically the same things. I'm using, I'm applying GLM,
*  I'm developing predictive models that they are all, I was using those models to analyze
*  behavior of my rats in the lab, or understanding some neural activity, or understanding some
*  perturbations of the rodent brain, but now I'm using those skills in a completely different
*  field. And I think it was a eye-opening experience for me that now that I have acquired these
*  quantitative skills, it doesn't matter what is the exact maybe question, I can really apply them
*  in fields out of my direct expertise. How much experience using the model
*  to understand the phenomenon in your neuroscience experimental work,
*  how much does that play into using the model to understand some other phenomenon like COVID, right?
*  I think that's pretty important. If you really kind of know the math, the assumption, the kind
*  of statistical properties of each of these models, if you understand them deeply, then it's easier to
*  just kind of change the data sets, and also understanding the data set, because all these
*  data sets, all the variables that we are dealing with, they might have different types of
*  interactions and correlations. And if you're not aware of the possible type of correlations
*  in our data set, then again, we can create wrong models basically. So it's both like understanding
*  the assumptions of the model and understanding the different type of data that you are dealing with.
*  If you know them, then maybe there is, for some cases, it doesn't really matter the data is the
*  spiking data, is behavior, or is like symptoms of a particular disease maybe. I don't know if I
*  answered your question.
*  So I do have one final question if we want to go around. What trait do you wish you had more of
*  as a modeler? Kunlin, you wear your failures in modeling on your sleeve here. Do you have an
*  answer to this question? What trait do you wish you had more of as a modeler?
*  Well, I do wish I had more mathematical background before I learned all kinds of modeling skills.
*  Because as I said, I was trained in biomechanics, which is not very computational in that sense.
*  Then it's after learning, doing models, and then I found out if I have more
*  mathematical intuitions, I can see through those behavior data better.
*  How do you get the mathematical intuitions? I think this is an eternal struggle because
*  go back to however many years ago that you wish you were studying mathematics. How do you convince
*  yourself that it's going to be important one day to study this thing that feels like it's in a
*  vacuum right now to get the background in case you have a question that one day you may be able
*  to answer using a better mathematical background? Well, I guess when I was in school, I don't have
*  the mindset that linear algebra and all kinds of optimization skills, all kinds of stuff,
*  learning the class can be used in my own research. At that time when I was still
*  undergraduate or in my master's years, it was only after when I was dealing with those
*  scientific questions, I found out if I have more mathematical backgrounds, I can see through them.
*  Because when I'm working with other modelers, when I see the same data set, when I see the same pattern,
*  they immediately notice there should be a model better for this kind of data set. But I don't have
*  that kind of intuition at that time. So it's only through case by cases, different kind of
*  research experiences, I kind of accumulate those mathematical intuitions for my own research.
*  In fact, when we talk about the struggle between the modern data, this is my words for students,
*  for studying in my own areas, for studying model control and model learning,
*  if you're just doing those behavior studies without a clear modeling mindset, you won't get
*  a high impact publications or high impact studies out of it. Nowadays you can do behavior studies,
*  but you need to have some kind of a mathematical modeling that can reveal the cognitive
*  mechanics behind it. That can get you some high impact work done. So this is not just,
*  I mean, for all the participants for the summer school, it's not just some classes you can take,
*  you just simply take as my, I can see myself in when I was a student, it's some tools you
*  have to master. Otherwise you will regret just as I did. Okay.
*  The fear based approach. I like that. So we'll open it up. So you can either say, how about this,
*  either a trait that you wish you had more of as a modeler or the alternative question,
*  which Kunlin actually answered is, if you were back at the beginning of your training,
*  you'd either study more of something and or less of something else. Damba, what do you think?
*  Yeah. So it's actually, it's an interesting question because I sometimes wish the opposite
*  of which Kunle wishes. I wish that I knew less math and that I could trust my intuition about data
*  more. Right. Because sometimes it goes back to something you mentioned earlier, right? Which is
*  sometimes it's easy to lose the forest for the trees, right? So it's easy to be stuck in the
*  mathematical details of what you're trying to accomplish and forget about the big picture.
*  So I wish I trusted that intuition more. And at a high level, there's a lot of talks about this
*  recently in the past couple of years. It's part of a tension right now that's happening
*  because of deep learning. Because you have the computer scientists on the one side that say that,
*  you know what, it works. And it outperforms 50 years of algorithms that we've developed that
*  are normative and mathematically based. So why do people like me bother them with trying to make
*  this thing, trying to come up with a mathematical theory for it? And I actually don't have a good
*  answer other than it's exciting to me to explain it. Yeah. Okay. So this is very confusing to people,
*  Gunnar and Athena, do you guys have clarification on this? Can you help them be less confused?
*  Yeah. I think this, I don't know, I totally understand DEMBA. And I think again, it's one
*  of those kind of maybe good confusions, right? It's always good to just have the rigor eye of
*  a mathematician. It's like, I want to really get to the bottom of formalized things and understand
*  the logical flow of different parts of the framework. But also if you can just get away,
*  because we have developed some sort of maybe a philosophical eye to just abstract out
*  some finding, even if they are not completely kind of based into a very clean and analytical
*  formalism, that's okay. Maybe we should just go back and forth between these two
*  type of scientists. I would totally agree with that. I think this falls to me into the category
*  of diversity as a strength. We need the different approaches, we need different ways of thinking,
*  there's no one that's better than another one in my mind to complimentary, we need them all.
*  Perhaps this is where I think we've been talking about a lot of this in a vacuum.
*  This is where a good supervisor or a good network helps, right? Because I think what I have of my
*  student is experience. I can help you while you're learning X say that, you know what,
*  this detail that you've been spending three days on, it doesn't matter right now.
*  Let's come back to it later. So I think this is where having a good
*  network around oneself can help. And a good supervisor, for example.
*  And their NeuroMatch Academy, TM.
*  Well, you know, it's actually, it's not a joke. Like the reason why we teach NeuroMatch Academy
*  through the Socratic approach is exactly because we want the students to ask questions themselves.
*  We don't just spoon feed, want to spoon feed them the answers, right? And so the TAs are not
*  supposed to be specialists of every day, quite the opposite. But they're supposed to be guides
*  in the learning experience. That's what they're there for. And I think this perfectly summarizes
*  what Timber said. It's like what the TAs have, because they're typically a little more senior
*  than the students, and what we have for our students is added experience. And my students
*  are way more specialist than I am in their particular fields of research. They know the
*  literature, they know, like, I don't, but if I can learn from them every day, then I feel happy.
*  Anyone else closing thoughts?
*  I can say what trait I wish I had.
*  Please, yeah.
*  I mean, I wish I had more kind of a classical training in physics, not to become a physicist,
*  just like to be right where I am right now, but like coming from a physics background.
*  That's not a trait, though. That's a skill. So we'll put that in skills,
*  which is totally fine. That's how Kuhnlin answered because, yeah.
*  I think it's more than a skill because I think training – okay, so the reason that I actually
*  didn't study physics was more maybe a kind of a childish reason that like I kind of as an Iranian
*  girl in Iran, I wanted to rebel against my family who were – I had a physicist dad and a physicist
*  brother and I didn't want to do what they wanted me to do. And I just like, okay, I go and I
*  just study biomedical engineering. But then later on during my PhD, I kind of regretted that. And I
*  started to kind of learn physics, particularly statistical mechanics, but more than really skills.
*  I'm talking about the way physicists look at questions that like they really would like to
*  get to some sort of abstract understanding of the phenomena. And a lot of the times it becomes very
*  annoying, actually, particularly for experimentalists, the way that physicists kind of forget about
*  details and just like, you know, kind of minimize the details and just like look for the general
*  principle. But I think that view, it's really a particular eye by which they look at the questions
*  and look at the phenomenology in the world, just like try to think to put the complex
*  phenomenology in a very kind of a simple theoretical framework. And I think that's more of a really kind
*  of a day to day way of looking at things and asking questions. And it just like, I tried to learn that,
*  but I think a classical training in that would have been different.
*  Do you worry that you'd have a reductionist bias?
*  If so, though?
*  That's why I said that I want to get to where to really be where I am, which means that it really
*  just like running an experimental lab that would just kind of remind me every day that like this
*  reductionist approach maybe really is not working. So you have to really top it up with something else.
*  But a lot of the cases that reduction approach is a good starting point.
*  It's a good thing to just like provide some sort of a framework that can be very well wrong.
*  But at least I mean, starting from some sort of a kind of a
*  theory, it's a good thing. And then we can disprove theories all the time.
*  But Paul, for all these things we mentioned, it's never late. It's not late.
*  Okay, Kunlin, is it too late to learn the math?
*  It's not late.
*  Why not late? No.
*  So why are you doing it?
*  It's just a test to learn it. It just accumulates all those.
*  I mean, sometimes you can learn math by project driven. You have a pretty good project and you
*  know you need those kind of mathematical tools for tackling those problems, then you can learn it.
*  It's just like learning a programming language.
*  Yeah. Well, that's so, Dimba, I think, you know, what popped in my mind is it's never too late
*  because it never ends until you die. Like you keep circling around to the same things and
*  learning more, but then having to relearn and it never ends. So it's not like you
*  learn modeling and then you're done, right? You learn modeling and then you learn modeling.
*  And then you learn modeling. And it just keeps building and building, right?
*  And the theory, I mean, people do real work in developing theories, right? All these things
*  evolve. It's not like you have learned linear systems, you're done forever. No, there's a
*  whole bunch of other things that come on top of that. Like, you know, Bayesian statistics
*  and neuroscience, one of those examples of a more recent translation of techniques or
*  introduction of techniques or tool sets into the neuroscience research field, right?
*  Reinforcement learning is probably another one of those. And you can just,
*  optimal control theory, right? That's also like very recent. And so it gets developed. Like now
*  we're at robust and adaptive control, et cetera, et cetera. And it's not going to stop there. So
*  as a computation, you're a scientist, you're not sort of like learn the tools and then you're done
*  and you can go do your research. It's a continuous learning exercise of the tools in the same way as
*  we're continuously learning, like any scientist has to continuously learn and catch up with the
*  progress of their field. It's the same thing. So NMA will look very different in 10 years,
*  if it's still running by then. All right, guys, I'm going to let you continue along your own days
*  and go learn some more modeling or whatever you're doing for the day. But thanks for the
*  discussion. And I hope it was useful for the Neuromatch students. So I appreciate it, guys.
*  Thanks, Paul. Thank you, Paul. Thank you. Thanks, Paul. Thank you. Thank you, everyone.
*  Brain Inspired is a production of me and you. I don't do advertisements. You can support the
*  show through Patreon for a trifling amount and get access to the full versions of all the episodes,
*  plus bonus episodes that focus more on the cultural side, but still have science.
*  Go to braininspired.co and find the red Patreon button there.
*  To get in touch with me, email paul at braininspired.co. The music you hear is by The
*  New Year. Find them at thenewyear.net. Thank you for your support. See you next time.
*  The covers of the past that take me where I go.

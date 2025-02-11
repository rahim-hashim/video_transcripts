---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5328s
Video Keywords: []
Video Views: 1168
Video Rating: None
---

# BI 148 Gaute Einevoll: Brain Simulations
**Brain Inspired:** [September 25, 2022](https://www.youtube.com/watch?v=ld9B_tqupwE)
*  I think it's a combination of these detailed models and these simple models that really
*  gives sort of like a...
*  Because the detailed models are needed to maybe make contact with experiments, but they
*  are not alone, not sufficient alone to give you that insight.
*  It's not like you can sort of just look at these traces and say, oh, there's a Higgs
*  boson.
*  You have to simulate the whole experiment.
*  You have to do the measurement physics.
*  And so it's like a separate thing.
*  And this measurement physics has been sort of, I think, underdeveloped in computational
*  neuroscience.
*  I think actually when it comes to simulations like our kinds of studies, a quantitative
*  difference would make a qualitative difference in terms of what we could explore.
*  That's the hope anyway, right?
*  Yeah, that's the hope.
*  This is Brain Inspired.
*  Hello, everyone.
*  I'm Paul.
*  So on the last episode, I had Noah Hutton on to talk about his documentary film In
*  Silico, which chronicles Henry Markram's quest to simulate a human brain under the
*  project names The Blue Brain Project and The Human Brain Project.
*  By coincidence, as you'll hear, today I have Gauta Einvall on the podcast.
*  Gauta is a professor at the University of Oslo and Norwegian University of Life Sciences.
*  And he happens to have been part of The Human Brain Project since its inception in 2013.
*  Gauta focuses on what he calls measurement physics in biologically realistic simulations
*  of neural networks.
*  His goal in the simulations is to faithfully predict or recreate the various types of signals
*  that neuroscientists measure in real brains, signals like spikes and local field potentials,
*  EEG and MEG.
*  As you probably know, one of the grand achievements in neuroscience is the famous work by Hodgkin
*  and Huxley in the 1950s, working out the dynamics equations that govern the activity of single
*  neurons, which has led to tons of productive neuroscience.
*  As Gauta points out, we still haven't had the same success simulating networks of neurons.
*  And his hope is that by doing so, we can use the simulation models as tools to better understand
*  networks of neurons across multiple scales and levels of biological detail.
*  And to test hypotheses then about these networks.
*  So we discuss all of that and more.
*  And you can learn more about Gauta and his work in the show notes at brandinspired.co
*  slash podcast slash 148, where you can also learn how to support this here podcast to
*  get all the full episodes and to join our discord community or to take my online course
*  Neuro AI, the quest to explain intelligence, which is all about the intersection of neuroscience
*  and current AI.
*  OK, without further ado, here's Gauta.
*  So Gauta, the the genesis for our conversation today was an email that you sent in response
*  to a conversation I had with Karina Kurtow about the difference between beautiful and
*  quote unquote ugly models.
*  And I feel bad for her because she this is like a two page thing that she wrote a while
*  ago in response to what neuroscience needs.
*  She was asked to write this and she kind of backtracked also on the ugly part because
*  and you know, and you in your email called them messy, which, you know, was a messy kinds
*  of models. So yeah, that's yeah.
*  I mean, for first, as you say, it was a quite friendly email.
*  It is very friendly.
*  So this is sort of and I sort of understand what is meant by and especially these beautiful
*  models because I think she had this this nice example of the Hopfield network, which
*  is clearly a beautiful model.
*  It's quite easy to write down.
*  It has some beautiful mathematical properties and it tells you something about
*  about the I mean, you get some intuition about it.
*  I actually asked I was at one of my first meetings.
*  I attended the neuroscience there was and was in was just after I switched to neuroscience
*  from from Convince Matter Physics.
*  So John Hopfield was there.
*  This was in Sweden. So I asked him about the role, what role his model would have.
*  And he said it might be a metaphor for how the brain works or how memory works.
*  And that was very nice.
*  That's what that's, of course, what it could be.
*  So I think you all agree that this was a very useful model and it's certainly beautiful
*  also. And then then you have this other extreme where you have this this because a complex,
*  complicated models or messy models.
*  So I guess the most value neutral thing is to say complicated models.
*  But I'm not aware of some ugly is sort of ugly.
*  It has a yeah, it's a negative connotation.
*  Yeah, but I mean, it's sort of I think we all agree that it is in some sense ugly compared
*  to the beautiful models because they have so many more parameters are much, much more
*  difficult to understand.
*  I mean, in physics, some people sort of call this kind of model as like what's called
*  number crunching.
*  And they do it like doing this kind of modeling just for number crunching.
*  And they sort of look down at some theoretical chemists for sometimes doing this kind of
*  what they call number crunching.
*  So so so but I think it's obviously these these these ugly models have, I think, have
*  an important role to play.
*  I hope you think that together with it.
*  Hmm.
*  I would hope that you think that given given your work.
*  Yeah, exactly.
*  And it's not because I think they are have some special interests that they particularly
*  whatever less find them less ugly than other people do.
*  But it's just that I think this is an important type of model we need in order to make make
*  progress.
*  Yeah. So so the other thing that was kind of fortunate, and we're going to talk about
*  some of your complicated models and the approach.
*  And the other thing that was fortunate is that I just this last episode, I interviewed
*  Noah Hutton, who made this movie, this documentary in Silico about the Human Brain Project,
*  by which you receive some at least some of your funding.
*  And you've been involved with the Human Brain Project since its inception.
*  So you got to see the film also.
*  And we don't need to talk about it for long.
*  But I'm just curious about your reactions to the film, which you were not in, by the
*  way.
*  No, no.
*  So so that's right.
*  I've been in the Human Brain Project, still in the Human Brain Project since its start in 2013.
*  And I think it was an interesting movie.
*  And certainly Mark Graham himself is a very interesting character.
*  Yeah.
*  So so I think it was and I also heard your podcast, your live podcast, or a podcast with
*  audience. That was very nice discussion.
*  And yeah, so that was very nice.
*  And and I think Noah came came across as a very reasonable person.
*  So so so I guess my my only criticism is that is of the movie is that it's all it didn't
*  take the grass-pad opportunity to clear up the difference between the Blue Brain Project
*  and the Human Brain Project.
*  Right.
*  That is.
*  Yeah.
*  Yeah.
*  So he mentioned it a little bit in the movie, but he sort of says that sort of that because
*  these are very different projects.
*  And these some of these more grandiose claims of of of Mark Graham has to do with the Blue
*  Brain Project. If you look at the goal of the Blue Brain Project started, I guess, around
*  2005 and had Mark Graham had this TED talk in 2009.
*  And then this then Human Brain Project started in 2013.
*  And this was not the continuation of the Blue Brain Project.
*  It was they had a different goal.
*  It was about really about making the infrastructure or making sort of making it possible to
*  simulate large scale networks on the computers and make this available for the community.
*  And that was one of the goals.
*  There was other goals of the project.
*  So and but but this has sort of often people have criticized the Human Brain Project and
*  held it to the goals of the Blue Brain Project.
*  And that has been sort of and that I think that that that that in Silico didn't really
*  take the opportunity to to take advantage of the possibility to actually clear that up.
*  Because I think much of the criticism and this petition that was signed against the
*  Human Brain Project was based on people who mix it up with the Blue Brain Project.
*  So and this was all there was.
*  So what now I'm a little bit because this is a sore point for us human brain projectors
*  that it was also a critique in the I think Atlantic paper, an article there.
*  At Young, I think we also did exactly at Young who did this mixed it up in the same in the
*  same way. So and the Human Brain Project is still running.
*  I mean, that is also was said in the movie.
*  But the goal is quite different.
*  The goal is actually to now one of the goals that I'm very busy working on is to
*  contribute to make this sort of like this like this computer with this infrastructure
*  for doing large scale simulations so that people can actually be able to do these kind
*  of simulations without having access to a supercomputer by themselves or and also.
*  So it's a sense democratizing simulation science is that if you have a laptop computer
*  somewhere, you should be able to sort of go in and run this large scale models and do
*  research on them on using these sort of like supercomputers at different places in
*  Italy, Spain, Germany and France and so on.
*  So that is really the goal.
*  And that's this this kind of tools are now collected under this umbrella E-brains,
*  which then we hope the planet that this will certainly continue beyond 2023.
*  So I really hope that this will both be successful in the sense that it's in the sense
*  that it's going to be easy to use and also to go to get user to this.
*  The people who want to do this kind of large scale simulations that that they were able
*  to find is useful and use it.
*  I think it's going to be so it's more about the tools than the than the model.
*  So so the human brain project ends in 2023.
*  But but you think that the funding will stay strong to continue these types of large scale
*  simulation projects?
*  I don't really know. I mean, we actually we are applying now for a much, much smaller
*  project to just maintain, maintain and sort of like develop and make it like it smooth
*  this like the use of these tools that's been developed as part of the human brain project.
*  So we're literally writing a proposal now to the EU to to and hopefully that will.
*  But that would just be a small fraction of them.
*  Oh, yeah. Oh, like the funding for the human brain project.
*  Do you think that what effect, if at all, do you think that that documentary could have
*  on the future funding of of your flavor of science?
*  Yeah, I don't know.
*  I think it would have been really helpful if this myth, this misunderstanding had been
*  sort of cleared up. I think that has been because this obviously this thing of this
*  whole reaction to the human brain project has certainly hurt neuroscience, I think.
*  Because I mean, I think this is I think that's.
*  Yeah. Do you think some of the reaction simply stems from jealousy?
*  Perhaps envy?
*  I don't know. I think it's also that somehow this this strong, strong claims that that
*  maybe have marker made sort of rub people the wrong way.
*  And I sort of also I also didn't sort of I believe I agreed partially with like with
*  his vision, not not completely.
*  But it wasn't really that I mean, I just I mean, it's in some sense, it was a lot of
*  money, right. But it was all spread on like hundreds of labs.
*  So we had I think I had two, three people working in the group because of this.
*  So it was sort of was like an R01.
*  So it was whatever.
*  I mean, like a rather modest.
*  So but obviously, I think it is this you see this, I think the neuroscience community,
*  you see all this money and it's it's a big sum.
*  And it goes to a sort of another type of of neuroscience.
*  And then maybe don't sort of even though it was an IT project.
*  So so I don't know what it was.
*  Obviously, there's always some worries, I think, everybody, especially neuroscience,
*  where there's so many approaches to neuroscience these days.
*  So I think, of course, the approach I do is very promising.
*  So I should get the sufficient funding and I everyone I guess everyone in neuroscience
*  is doing is feeling like this.
*  So I guess there's always this also also this worry about getting getting funded for
*  your own approach.
*  Yeah. But last question about this and then we can move on to more fruitful topics.
*  Have you personally received pushback from the community, like any part of the
*  community, or do you feel supported within the neuroscience community?
*  Or what's the general feeling you have?
*  No, I certainly hasn't been a particular pushback.
*  I also been a little bit on the never been in the leadership of the Human Brain Project.
*  Yeah, I think so.
*  So I've been a little bit on the on the periphery.
*  I worry, however, maybe that this that I mean, some of these some of these more
*  grandiose claims, maybe that was people got the impression from from from maybe from
*  like presentation of the Blue Brain Project is that if you sort of just make a very
*  complicated model and put a bunch of like detailed neuron models in the network and
*  simulate on the supercomputer, then voila, you sort of this spirit comes out of the
*  bottle. If that is like this very naive thing that I don't think anybody believed, at
*  least sort of not not anybody I know, not anybody I know.
*  I mean, this this kind of you have such a model, it's sort of like a starting point for
*  doing research. It's not the end of it.
*  And it's so there's all these unknown parameters, which is also pointed out by by
*  like some some of the people who are interviewed in Silico, which I think is a very,
*  very good point that you don't know the parameters.
*  But this the way to find the parameters is to build sort of what I call a skeleton model
*  and then sort of use that to sort of try to compare with data and so on.
*  But it's not. So anyway, so I think sometimes when you present this and maybe apply
*  for money, people have this sort of conception of that.
*  We have this naive vision that if you just put to make a very messy model and it looks
*  sort of realistic, that is somehow it's going to act realistically.
*  And I think that's always that's not common.
*  That's how it works. Yeah.
*  OK. Well, so you detail.
*  Well, in this review paper, the scientific case for brain simulations, which was a
*  2019 review paper, I believe you talk about this approach and why it's supported and
*  also like you alluded to before, that it's going to take a lot of different labs, a lot
*  of different people working on it spread out and that we have the capabilities of
*  doing that these days with supercomputers that you can send your data off to and it
*  runs on a supercomputer in some other country or something.
*  So maybe maybe you can just kind of give an overview of what your approach is and
*  then why. So it's so it's it's cool that you think it's important to for these
*  models to be able to predict not only spiking activity, but local field potentials,
*  EEG signals, fMRI.
*  And these all come with their own challenges, of course.
*  But maybe you can kind of broadly overview what you're doing.
*  I think that the overall approach, I think, is very similar to like the approach of
*  Hodgkin and Huxley. And when they when they model the I mean, a neuron or actually a
*  piece of the neuron, the axon.
*  So they just looked at it as a physical system, right?
*  They made a model for the axon and then they they use all kinds of clever experiments
*  to sort of to to design this model and determine parameters and run it on computer
*  eventually. Right. So they didn't have a computer, right?
*  So they got wrenching hand calculations.
*  Now, that was extremely impressive in so many and along so many different axes.
*  Yeah. So so so now after that, we now have a pretty good way, well, pretty good idea
*  about how to model single neurons.
*  Right. We have at least we have this cable, you have this what you call multi, you can
*  do this reconstructed morphology with then writes and so on.
*  So we can make sort of like the structure.
*  We know the then writes and we can make mathematical models.
*  We have the mathematical framework.
*  What is hard, though, is to find the parameters.
*  What sort of ion channel densities should you put in the soul mice at IH?
*  Is it more along than like apical then write and basically all is this these choices.
*  Right. So so then you have to to sort of to to do as many measurements as you can, in
*  some sense. Often this patch patch electrodes.
*  And now people also started to use extracellular recordings.
*  If you have this neurons on like this microelectrodes, they raise and so on.
*  And then you have all this experimental data and then you sort of fit the model parameters
*  to sort of to make this neuron model that you make predict as accurately as possible.
*  These like the behavior of this.
*  Well, the model make the model behave as similar as what you see in experiments.
*  And there's many types of experiments and so on.
*  And already there you have this this problem that this problem that is not a unique solution.
*  It's not it's not like it's a one set of parameters that sort of that sort of this gives
*  the uniquely best fit.
*  And I think already there was this one one model that we use lot was in the so we call
*  it the model because the first author was Ithai Hey, it was like 2011.
*  He was in a group of you know, Segev.
*  So there they had like this this beautifully multi compartment detail neural model.
*  But they and they had one sort of like one sort of examples parameter set they use
*  throughout the paper, a couple of them.
*  But they also gave up five and other parameter sets, which did equally well.
*  So that already sort of like this thing that about model solution degeneracy, which is
*  another thing to discuss.
*  But we are essentially trying to do the same thing for a network.
*  Because if you look at network studies, especially the cortex, there are no examples
*  that I know of, of like a piece of cortex for a particular biological system that has
*  been like made so that you can sort of essentially that this network model can mimic a
*  bunch of different experiments.
*  And we are now working with collaborators at Allen Institute, Antony Arkhipov and
*  Kristoff Koch on sort of to as you know, they had done a lot of well, the Allen Institute
*  has focused a lot on the mouse visual cortex of the last decade, mapped out all kinds of
*  met out all kinds of things and also then made this like first version of a network
*  model.
*  So then so then but then of course, how do you constrain this?
*  How do you constrain this?
*  How do you how do you determine the parameters of this model?
*  And that's that's a huge challenge.
*  But again, you have to use use the old experiments, not only spikes, but but also
*  other experiments.
*  So that's in fitting this, this complex models is ugly models to experiments.
*  You need to take advantage of all experiments available.
*  And so that is sort of where you but that was the same thing with if you look at Hodgkin
*  and Huxley, they did all kinds of different manipulations with patch clapping, no space
*  clapping. And so they did all kinds of manipulation to get a rich sort of set of
*  experiments. And so which they use.
*  So I say it's very much the same same spirit as Hodgkin and Huxley.
*  Yeah, well, maybe we should talk about the degeneracy.
*  So I had Eve Martyr and she's become this famous figure in neuroscience showing that
*  there are a thousand different ways to skin a cat in the stomatogastric ganglion of
*  lobsters and crabs.
*  So how you know, and I know that you see the and rightly so see the degeneracy as a
*  feature and not a bug of the system.
*  But how much do you worry that it's going that it has that it will have an impact on
*  the I guess, the relevance of the brain simulations that you perform?
*  Now, this is this is this is a major worry, of course.
*  So then you have to do this, this thing that you sort of say you fit your model to one
*  type, one type of data.
*  For example, when it comes to when it comes to like this this mouse visual cortex model
*  that has been developed at Allen Institute, they have they have all these beautiful
*  experiments where they show these different kinds of like images and movies and spots
*  and whatever visual stimuli to the mouse.
*  And so you can sort of sometimes fit the model to to data for one type of experiments
*  and then test it on others and so on.
*  But I think also it's an important thing to what what does this degeneracy mean?
*  Because I think I mean, obviously, this wonderful podcast, by the way, I'm I'm a big
*  fan. I think you're doing a good service to the to the field.
*  By the way, I should say I should we should plug your podcast since and science, right?
*  So it's largely in.
*  Go ahead. Yeah.
*  In Norway.
*  So that's true. So I have this is this Norwich.
*  Essentially, it's it's a podcast where most of the episodes are in Norwegian.
*  But there are some of them are made in English.
*  I think it's four or five or something.
*  And with with some neuroscientists and that's called it's it's a found on the sense of
*  science. So that's you got Terry Sanofsky to laugh a lot more than I did.
*  So nice job. He was he was generous with the laughter is great.
*  Yeah. So that's true.
*  So there is no is there and and and and the cook is there.
*  And I was at Sean Carroll.
*  He's not a neuroscientist, but he's I think he's a wonderful podcaster.
*  So I really like I sort of am only a patron subscriber to podcast is yours and his.
*  So that's man. My heart.
*  You my heart is a flutter.
*  Exactly. No, that's true.
*  And I actually tell my students sort of to listen to this podcast because it's I mean,
*  following up while even in reading papers with your own field is quite sort of like,
*  as you know, quite challenging.
*  But you sort of having listened to like one hour to our podcast where you interview
*  someone like from like in like in especially this a I think which is a little bit like
*  adjacent to what I do, but not certainly not interested in it.
*  We're going to come back to that.
*  Yeah. Yeah. So this is sort of so this is it's been very useful for me just to stay
*  oriented in the field.
*  But what I was saying is that if you look at this this deep, deep network, say the
*  ones that can be the normal deep sort of convolutional networks that can be used for
*  like image recognition, if you sort of train, say, if it took like two identical
*  identical networks or like to start off with and then you train that but maybe with a
*  different initial conditions or maybe with a different order of images or something.
*  Yeah. Then you will end up with two networks which are probably behaving the same way
*  and performing the same way and both are sort of hopefully then successful.
*  But if you go into the detailed parameters and you look at the synaptic connections or
*  the connections, right, they will be different.
*  Yeah. So in some sense, it's it's this tells that it's not the detailed connections
*  that matter. It's some kind of more like some kind of more kind of average thing in
*  the connection, whatever some other measure of the connection that matters.
*  And so that's also not a unique solution.
*  So I think this thing of looking for a unique solution is something we're so used to
*  because that's typically how we made our models.
*  We want to make them sort of low dimensional, I guess, what to call so that you have few
*  parameters and a few parameters.
*  And then you sort of try to find this sort of set the parameters so that it sometimes
*  gives the most like suitable behavior.
*  But but that's just like that's a special case.
*  And even if you looked at like the Hodgkin and Huxley, if they instead of fitting
*  ion channel densities, if the star is sort of to fit in a position of individual ion
*  channels, then you would end up with the same kind of degeneracy of solution.
*  So this degeneracy is just that's it just has to do with how the resolution we use
*  when we model.
*  Well, and of course, you know, your brain and my brain, we both can speak English and
*  your English is probably better than mine because, you know, multilingual and you're
*  just right. But, you know, of course, our brains are not parameterized the exact same
*  way, nor is the structure the exact same way, et cetera.
*  But, you know, you mentioned in convolutional neural networks.
*  So the hope is that you can extract some principle out of, you know, how it's doing
*  what it's doing. And in the case of convolutional neural networks, those principles are,
*  well, you need multiple layers, you need the convolutions and and to form abstractions.
*  So I don't know if you want to say so, I guess I just wanted to throw that out there
*  to you. And, you know, how do you think about extracting, I guess, abstract principles
*  from these detailed model simulations?
*  Yeah. In the face of degeneracy.
*  Yeah. So that's that's obviously I think the first case of the first step is trying to
*  find this very complicated model. And how do you how do you and what we're after, we
*  often call this like trying to find what's called a multipurpose model, a model that
*  can explain many things at the same time, because that typically if you look at some
*  of these earlier works on the modeling the visual system, there are like this firing
*  rate models, which I think are sort of showing some things like whatever it's like this
*  constant invariance and like responses to visual stimuli with the contrast invariance.
*  I mean, so there are certainly things but they typically can only explain one thing
*  at the time, but they're still useful to explain that thing. And if you try it on someone
*  and something else, whatever orientation, selectivity or direction selectivity, it
*  doesn't work. Right. And that's, it's not surprising, right, because it's, it's, you
*  need a probably a complex model. If you want to have this multipurpose model, that say
*  if you had like a model of the mouse visual cortex, that should be able to reproduce
*  I mean, within some accuracy responses to different visual stimuli, and also maybe
*  different brain states like the mouse is like active or resting. And, and so that would
*  be sort of like a multi purpose, multipurpose model. And that that sort of is. Yeah. And
*  so then, then of course, then there's also a question what you do with what kind of
*  model are you after? Are you going to actually the data from the Allen Institute, they
*  have not only a beautiful model, they also have this beautiful electrophysiological and
*  opto optophysiological data. So they have data from 50 mice. And when we look at them,
*  even in the visual system, if you look at the like the spike patterns, and also like
*  the local feed potential is other things, they are quite different from mouse to mouse.
*  And so they can probably also vary of, I mean, it's this all kind of variability. So
*  you have to think about, do I want to make a make a model for an average mouse or some
*  kind of individual mouse? So what are you really? So there's all these other kinds of
*  issues. But say if you have this, this sort of like multipurpose detailed model that is
*  able to predict, predict all these, all these different experimental observation for the
*  particular mouse, that would certainly not be the end of the project. Some people say
*  that's just as complicated as a real mouse always. And that's true. But then you have
*  this perfect, I guess, what's called a white box, a white mouse. Well, that's probably
*  not there. But anyway, a network. Yeah, whatever. So they call about the black box and the
*  white box, right? So this would be analogous to a white box, white box mouse, where you
*  can actually do all kinds of experiments, right? So you can sort of then start looking for
*  principles. And so then that will be a very nice starting point, I think, for making more
*  model simplified models at different sort of coarse grain levels. I mentioned in this, I
*  think we mentioned this paper in Neuron, about the scientific case for brain simulations
*  that you can sort of maybe then in addition to having this biophysically detailed model,
*  and well, that biophysically detailed network model, you can also have maybe network models
*  of point neurons, like integrating fire type neurons, and also then maybe on terms of like
*  firing rates or population firing rates. And you would like these to be sort of linked together
*  in a systematic way so that you can under some approximations, be able to sort of derive the
*  model at the more coarse grain level from the lower level, right? So it's the starting point
*  and so it's not the end point.
*  So and then be able to extract some principles from comparing the different granularity models.
*  And that would of course be, yeah, go ahead. I'm thinking, yeah, sorry. So no, I because I'm in
*  I'm in this all this if you think of all the models that have come about, good suggestions for
*  like principles for how the brain works, you have like the, well, predictive coding and 1000
*  brains theory and like this inside out perspective of Bushaki, it's all interesting,
*  right? And, and but it's some of them have been around for a long time. And it's just difficult,
*  difficult to find out which of those if any is correct, right? So all so all maybe, exactly.
*  Maybe there's a dead degeneracy there.
*  Yeah, exactly. But then at least if you could then someone who believes in one of these sort of
*  tried to make actually a model based on these, because we know quite a bit about the about sort
*  of how to make. Well, I mean, we know quite a bit about the structure of the mouse or the visual
*  cortex, right in terms of the neurons and that they are connected. We don't know the how strong
*  these connections are. And so we certainly don't know all the parameters that we have. Obviously,
*  we don't know this plasticity rules either. But nevertheless, there are some constraints, right?
*  So, so if there's one of these ideas that easily can sort of be accommodated with this structure,
*  that adds to the credence of that ID. And if there's another ID, which is much more difficult to,
*  to sort of to fit with this, what we know about the structure and these type of models,
*  and they're sort of like less, less credence. So that would be certainly a way to sort of do,
*  yeah, to also get hopefully closer to these principles.
*  Well, so but you view these models not as hypotheses, but as tools, right? I don't know
*  if you want to just comment about that. Because I think some of the criticism is based on that
*  notion, like, well, what are they actually, what will these models be testing? You know,
*  like, what's the question? Right? But that's but the whole point, I suppose, not to put words in
*  your mouth, is that the question, their question agnostic tools.
*  Mm hmm. Yeah, exactly. So that's how I think about it. Say if you have this, this, this,
*  you're out there, that's my I like to hike in the mountains, like many Norwegians do.
*  And say if I get an idea, oh, I believe this M channel is very important in to get the hippocampal
*  circuit to function. And I do get that out hiking. And then I get back to my little cabin and then
*  sort of do something with the M thing and get the M channel and then simulate it down on some
*  supercomputer in whatever Lugano or whatever, right? So that you can test that out what a
*  consequence of that. So that's how it's a tool for testing hypothesis. It's not a hypothesis in
*  itself. And I think, I mean, my background before I came into neuroscience was in solid state
*  physics, where I worked with like materials. And there we have, we know how to in some sense,
*  we have the fundamental principle for solving materials, we just have to put all these atoms
*  into sort of like the grid or like the whatever, like the structure that we know is there,
*  and the lattice structure. And then we have to solve the Schrodinger equation, this quantum
*  mechanical equation for the electrons. And that's a very complicated equation to solve. But
*  nevertheless, we know that if you're able to solve it, then then sort of that sort of gives you the,
*  it's a close approximation of the truth. So that's, but that's the same thing that, well,
*  that's very useful. But it's not the end of the story. You don't really understand,
*  you need additional simpler theories to understand particular at the moment, particular
*  phenomena, like for example, superconductivity, some materials can conduct electricity without
*  any resistance or, and that some, some materials are semiconductors, others are metals, and so on.
*  So you need also these other like what a coarse grain theories and, but I think it's a combination
*  of these detailed models. And the simple models that really gives sort of like a, because the
*  detail models are maybe are needed to maybe make sure to make contact with experiments. And, but
*  they are not alone, not sufficient alone to give you that, that that insight. Okay, well, maybe just
*  coming back to the models that you work with. So one of the goals, and I guess the main goal is for
*  the model to predict all these various types of signals, like I was mentioning earlier, and
*  I guess you started off with wanting to predict local field potentials, because, well, I guess to
*  give it away, you found that a model that predicts the spiking activity of a network doesn't
*  necessarily predict the local field potentials of the network. So talk about that and why it's
*  important, you think, to, you know, come up with these equations, like you were saying, in solid
*  state physics, to make predictions about the neural measurement signals that we measure.
*  I think so. I mean, if you look at the, at the, at the systems neuroscience, right, all the insights
*  we have from studying systems has been from measuring spikes, the exocellular signatures of
*  action potentials. I generally threw my local field potentials away. Yeah, exactly. And I think there
*  was also like, I guess, historically, there were two reasons. I mean, you couldn't store them all,
*  so because you didn't have cheap hard drives and stuff, maybe that's not the problem,
*  problem now. But obviously, there was like, in some sense, we were a little bit blistered in
*  neuroscience, that the spikes are so easy to interpret, right? You know that they are from
*  action potentials of neurons in the neighborhood. And so that's why this is typically,
*  typically, what you measure and analyze, right? But you know, yeah, you've made the point also,
*  though, we're still not confident that we understand the quote unquote code of spikes,
*  whether it matters, the timing between them, the firing rate, the overall firing rate, etc. So we're
*  not that comfortable, even with spikes. But I guess we do believe that if I knew all the spikes
*  in the brain of an animal, then we have all we need to understand, in principle,
*  the information flow, or if you're just very clever and figure things out. So that I think
*  is also true. And if you sort of look just for the history of spikes, right, with its receptive
*  fields, that was sort of like the Jubilee Weasel and obviously told us a lot about neural
*  representations. And now we have with these manifolds, whatever these neural manifolds,
*  which is also obviously a nice way to look at this, which also tells us, tells us things.
*  But but from the point of view of falsifying models, say if you have, if you measure spikes
*  and LFPs, local field potentials, just to make sure that I mean, the local field potentials,
*  yeah, in the cortex is measured from the same electrode. It's just a low frequency part. So
*  maybe the part below a few hundred hertz, and then and then the spikes are actually extracted from
*  the high frequency part above a few hundred hertz. So it's the same same electrode. It's just that
*  this it's like a different aspect of the signal. And the local field potential, just to carry on
*  with what you're doing, which I should do more often to describe what we're actually talking
*  about. The local field potential has traditionally been thought to measure the synaptic input to the
*  neurons and a broader scope than of course, a spike, which is the output of a neuron.
*  Exactly. And I think that is still true in many situations. That's true. We're actually writing
*  a book now on the electrical electrical signals of the brain, which hopefully come out the next
*  year on Cambridge. So we go through the like the what I call the measurement physics, the link
*  between what the neurons or our group goes through the what the link between the neurons are doing,
*  and what you would measure in terms of spikes and local field potential and EEG and ECog and also
*  MEG and so on. So but but it's it's the thing. So the thing is that with them,
*  the thing is that if you the local field potential, well, even with the best electrodes,
*  that you have, say the neuropixel probe that that's like they're using at the Allen Institute,
*  and while it's used all over the world now, you can only measure to say like, I think if you have
*  one of these neuropixel probes, that's a multi shank multi electrode that has like many, many
*  contacts. And but even that you can sort of impale quite deep into the court and cover lots of mouse
*  visual cortex and mouse brain altogether, you can only measure about 70 80 neurons spikes from 70
*  80 neurons at a time from each each of these shanks. You say only if you want to back back in
*  the day when you can only measure one, it's it's much, you know, much more enticing.
*  That's true. So it's a so it's only so it's only compared. If you if you want to use this,
*  this data to constrain a network model. So then it's then it's so then, then yeah, so that's sort
*  of the key thing that if you want to constrain a network model, say if you have this model with
*  many, well, 1000s or 10s of 1000s or 100s of 1000s of well, a few 10s of 1000 100,000 neurons
*  mimicking a piece of visual cortex, it's certainly the spiking data are important, but they are quite
*  erratic and stochastic. So it's it's a lot of variations of that model that will be compatible
*  with like, well, the experiments that you have on spikes. And that's where you come in with
*  if you can, if the same model can predict not only spikes, but also other things that the local
*  field potential, then it's more you put more constraints on. So that is sort of the why,
*  like one of the reasons I'm very interested in local field potential, and also E cog in EG,
*  that they'll be able to predict all these different measures from the same physical model.
*  So it's sort of, yeah, so that is all that there's.
*  Does that have a touch point with thinking in terms of one mouse versus average mouse that LFP
*  signals essentially would also get us closer to the average mouse?
*  Yes, I think that's that's certainly also true. Yes. And I think also if you just look at the
*  a single mouse, one trial versus another trial for the same mouse. Yeah, so everything is just more
*  or less right. Because it's what what is you said that the LFP is sort of reflects the synaptic
*  inputs to neurons. And these synaptic inputs, of course, comes from pre synaptic spikes.
*  So in some sense, the local field potential is sort of like some kind of average weighted average
*  of spikes, just a different kind of weighted average. So in some sense, it in captures,
*  capture a lot of the spiking going in going on in the network in an indirect way. So it's,
*  it's sort of like some sense there. So that's an and there's a thing if you want to compute the
*  local field potential, say, the computer, what does the contribution to the local field potential
*  from a neuron that gets a synaptic input, say at the apical dendrite, what does it look like,
*  if you want to model that you cannot use a point neuron model, because a point neuron
*  model doesn't have doesn't generate an extra cellular potential. And it turns out that this
*  contribution to the local field potential that depends on the morphology and where the synapses
*  are and, and then you need to use these biophysical detail models. And actually, if you want to do this
*  measurement physics properly, that's not only for the electric measures, like spike, LFP, EG, Ecol,
*  or the magnetic measures, particularly MEG, but also for the optical measure, like the response
*  to voltage sensitive die imaging and so on. That very much depends on then you need this
*  biophysically detailed models. So to make this proper measurement physics link, then you need
*  this biophysically detailed models, even if you but there are even if you sort of maybe can get
*  away with simpler models to get an idea about like how the information flows in the network.
*  If you want to sort of translate into the things you measure, you need to go, go via this, this sort
*  of like biophysically detailed models. And so that's something that we have worked quite a bit
*  on doing this kind of making this practical tricks for making that possible. So that you can sort of
*  compute EEG contributions from a network model, even of point neurons or even firing rate,
*  firing rate models. So it's sort of this more mundane thing of doing the measurement physics.
*  Sometimes compared it to the discovery of the Higgs boson in CERN Switzerland,
*  because there you had, if you look at the people at CERN, they had maybe like 20, 30 people,
*  I don't know, who worked on why there should be a Higgs boson in the first place. That has to do
*  with the standard theory of particle physics. But then it's like, okay, so but then most of
*  the people work on how can I, how can you measure this Higgs boson, right? It's not like you can
*  sort of just look at these traces and say, oh, there's a Higgs boson. You have to simulate the
*  whole experiment. You have to do the measurement physics. And that's so it's just like a separate
*  thing. And that's sort of this measurement physics has been sort of, I think, underdeveloped in,
*  in, in competition neuroscience, most people have worked on sort of this information processing and
*  seeing how spikes generate new spikes and so on, which I understand, because this is sort of the
*  most interesting thing. But if you don't do this measurement physics correctly, then it's then you're
*  going to make incorrect, incorrect sort of like comparisons with experiments. So there's many
*  examples of people who haven't sort of, I mean, papers who are sort of not very valuable when
*  they're compared with experiments, because they've forgotten this sort of basic, or they haven't done
*  the measurement physics thing. So that's one of the reasons we, well, one of the reasons we, well,
*  do this, this, this sort of like model the potentials, there's also this other thing that,
*  I mean, people obviously measure local field potential and ECOG and EEG. And what do they
*  do with them? Well, typically, they do statistical analysis of some sort, right? And then try to
*  interpret this sort of this data in terms of some kind of underlying neural activity.
*  And how do you, how do you test this data analysis methods? I think it's always a good,
*  like a sane approach, if you can make some good benchmarking data, where you know the ground
*  truth. And if you have sort of a, have sort of like a test circuit, we'd say like a piece of mouse
*  visual cortex, even if it's not, I mean, fine tuned to correspond to one particular mouse,
*  in that sense, not very realistic, it's still probably good enough to test a method for,
*  for example, what's called current source density analysis, which doesn't, which would work for
*  also unrealistic models or unrealistic bias, it doesn't depend on. So I think depend on sort of
*  being biologically accurate. So I think that's a very important, and we have used that actually to
*  test sort of different, we have also developed some new methods for current source density analysis
*  back in the past, and they were tested on, on bench model based benchmarking data. And I think
*  that's, and this is also important for developing automatic spike sorters. I guess you were sort of
*  ignored. Yeah, I don't want to talk about it. Yeah.
*  Exactly. So this is sort of, I mean, we are in, I'm in Oslo at this, called the center for
*  integrated, well simpler center for integrated neuroplasticity. So we have modelers and
*  experimentalists sitting side by side. So we also look at these, these people, well, doing spike
*  sorting, right? And all the issues related to that. And it's like, so that's extremely, yeah. So, so
*  having automated validated spike sorting methods, I can trust that be very useful, I do the field,
*  right? So, and I think there with a, then you need ground truth data. And you could get it two ways.
*  If you have dual recordings, say like measure things, measure spikes and maybe optical responses
*  to two photocalcime imaging or something. But, but that's sort of quite hard to get by and, and, and
*  to at least get a lot of these kinds of data, but with model based data, I think the, the modeling
*  of these exercise signals are quite, quite well established. So I, I sort of, so, so I think it's,
*  it's the modeling formalism you can, you can trust. Yeah. The spike sorting thing, I'll just
*  make one further comment on that. That has become more important with these high density,
*  multi-electrode recording techniques, because back in the old day, when I started, you could,
*  with a single electrode, you could, everything drifts while you're recording. So you could kind
*  of chase that neural signal and be confident that you're still recording the same neuron.
*  But you really, you can't, you can't do that with these multi-electrode systems. And, you know,
*  there's questions about, you, you, you impale the cortex, right? Or, or put it down into the brain.
*  And then this is talking a little shop, but, and then you wait and, you know, you go, go get a coffee,
*  because you know that it's going to drift over time. And so you want it to be as stable as
*  possible, but it's never completely stable. So there are different, you know, ideas about how
*  long to wait and so on. So anyway, you were working with, with monkeys, right? Monkeys. Yeah. Yeah.
*  But they're, they're head fixed and, you know, so they weren't freely behaving in that sense,
*  but still there's, there's drift. Yeah. So anyway, just to say about this, the usefulness for,
*  for modeling signals, I think you're, you had a nice podcast with your old postdoc advisor,
*  Jeffrey Shaw. Oh yeah. Yeah. He was, he was my advisor when I was, yeah, I did a postdoc with
*  him. So he referred to this, this work with our, uh, Jorge Riera and others down in East
*  Florida. They work on that. Yeah. Yeah. So I was, uh, so I know this, so they are doing some very
*  nice work using actually some of our tools. I was wondering about that. Yeah. So exactly. So this is,
*  Jorge is a great guy and I, well, Jeffrey also, I'm quite sure I just haven't met him in person.
*  But, um, but Jorge was, well, he's been visiting a few times. So this is, it's not so this, I mean,
*  computational neuroscience community is, is sort of not so big compared to the neuroscience community.
*  Right. And within the computational neuroscience community, there's like this, the people who model
*  signals are the minority of the minority. Fractions. Like Jorge Riera is one of them, right? But
*  more and more people are, I think, well, that's what they always say when you sort of want to
*  promote your, your approach or tell about your approach. But I think more and more people are,
*  sort of, if you want to go beyond this sort of, I would say like anecdotal understanding of networks,
*  I think there's been some very beautiful, uh, model studies of, of learning about how, uh,
*  principles for how, for how networks may operate, how they get the dynamics. Maybe particularly this
*  one example is this balanced excitation inhibition ID, which was beautifully demonstrated,
*  like, 20, 25 years ago in a more generic network, like simple neurons. And then,
*  and we'll learn a lot from those. But if you want to make sort of not what are like these generic
*  studies, go beyond that and make models for particular, particular systems, particulars,
*  like pieces of cortex or, or particular systems, then you have to sort of look into,
*  well, then you have to sort of do this, this measurement physics more properly.
*  Even though there's, I think, obviously you mentioned Eve Marder and the work of, uh, well,
*  her work, obviously, or the work in her group on, on this, this, those, what is stomatogastric
*  ganglion. Yeah. It's certainly very beautiful. Yeah. Yeah. It's, uh, has been, it's very important.
*  And as obviously illustrated the many of the same issues that we have to, have to address in,
*  in, in computation, in, in when you're dealing cortex, I would say though that one, I think life,
*  if we get stronger computers, say like, if you get this, like the e-brains, there's like the
*  infrastructure following the human brain project so that you can sort of run
*  decently large network models and run them for a long time. Then we can start also exploring,
*  uh, like plasticity rules because, uh, actually coming out from Eve Marder's lab,
*  there are these sort of beautiful work on, on, on homeostasis. Why does sort of a, uh,
*  why does a layer five neuron in the cortex know that it's a layer five neuron? What, what happens?
*  And, and it turns out of course, and it was like also beautiful work. I remember why
*  one of our posters, Tim, Tim O'Leary, I think he's now at Cambridge where it is showed how sort of
*  you can sort of, instead of fitting channel densities for in, in neural models, you can sort
*  of essentially just let them tune themselves using this essentially like plasticity rules
*  based on the intercellular calcium concentration. And then suddenly you have changed the parameter
*  fitting from channel densities to, to essentially fitting these, these learning rules, these plasticity
*  rules. So it might get much simpler. And it's the same thing with, uh, there was also this
*  beautiful work from the group of Wolfram Gassner. And that was like 10 years ago where they showed
*  how you could get to this balanced state without having to fine tune and, and to, to get these
*  right parameters. You could have this particular synaptic plasticity rule. I think it was an
*  inhibitory synaptic plasticity, which let the network tune itself. So I think it's, it's like
*  that's closer to what the real brain does. I'm quite sure. And it will make life easier
*  if you just are able to run the models longer so that we can use this, use this.
*  So, so you make these, uh, you know, complicated high parameter models and I know you make them
*  at different levels of abstraction as well. And then you can compare between them,
*  but how long are we talking? Uh, do you run your simulations? So it's not long enough for
*  sort of a plasticity allowance. No. So, uh, so typically they are run for a few,
*  few seconds of biological time. Uh, even though we haven't really pushed that. And so far
*  we haven't looked, I think we can sort of add short term plasticity. Uh, like that is something
*  we could add to the model and that could maybe give, yeah. And, and well add, add something to it.
*  But these sort of more, this homostatic plasticity and synaptic like long-term,
*  like a long-term synaptic plasticity, it's not something that we can, we can do. And, and they
*  are obviously, I think hopefully that will make our life easier when the, in the future we can
*  actually explore these things in the, in, in models and let, I think you got to make the
*  parameter fitting problem. But you could potentially do that right now. So a lot of what you do is,
*  model multi-compartment neurons where, where you're breaking down the neural, neural structure into
*  like lots and lots of different sections, but you also test a dual compartment, right? Where you have
*  an apical area and a basal soma area and, and, um, two compartments we call it. Yeah. Yeah. You could
*  potentially already, I mean, but they're not as computationally costly to run, right? So you could
*  potentially go down that avenue right now with those, right? Exactly. So, so actually when it
*  comes to these, um, this, this Allen mouse visual cortex model, they have like two versions, one
*  with a biophysically detailed models in multi-compartment and one with point neurons.
*  And, uh, we are actually using, using both. And actually when it comes to, we have a lot of,
*  well, master students working on this model here and they very typically use this simpler point
*  neuron version simply because then you can run it on like normal computers and you can sort of
*  get feedback. And I think it's true when it comes to synaptic plasticity and it's like effect of,
*  of spiking, uh, then, uh, and sort of how self-tuning of these connection parameters,
*  then I think sort of actually exploring point neuron networks first is probably a right avenue.
*  And people are, are doing that. I don't really, I don't have a full, I don't follow that feel as
*  closely as I should, but certainly that's, uh, that's important work there. And I, I think
*  that's true. So you just have to be practical about it. And, and, uh, but at the end of the day,
*  you would like this different approximation schemes to be internally connected so that you
*  don't just invent something that on the coarse grain level, that could never happen for a real
*  neuron. Right? So it has to be some kind of a consistency, but even the multi-compartment
*  neurons, that's a decision to make, uh, how many compartments, you know, because you're still,
*  it's not biophysically equivalent to a real neuron. So, you know, how does that decision get made?
*  For instance, I think they're typically the standard way is that you, you, you choose the,
*  you divide it up into these small sections, which are compartments. And the key thing is that the,
*  the membrane potential within each compartment should be the same meaning. So there shouldn't
*  be a potential difference within the, within the compartment, uh, which is sort of a larger than
*  some kind of a fraction of it. So that, that's how we set it. So the, some say that compartment
*  should be equally potential as we say, but then how do you decide how to go ahead? Sorry.
*  No, so how, so what was the question? How, how do we decide the size of the compartment or?
*  Yeah. How many, how many, how do you decide how many compartments? I mean, I know sometimes you
*  just kind of plug in like with the Allen Institute model, you use other people's models also,
*  and sometimes alter them, uh, you know, changing parameters, but.
*  I think, I think, I think in neuron, what they often do, what neuron is this simulation tool
*  that is used, uh, still sort of like, I guess the most used simulation tool where you can import
*  this reconstructed morphologies of neurons into the model. And then it sort of compartmentalizes
*  it itself. And then you have this, uh, what's called the, you have this measure called the
*  electronic length. How, how fast does the potential, if you have this little piece of a cable,
*  then you have this what's called the electronic length, which tells you how fast does the potential
*  decay from one end of the cable to the other. And that depends on the, on the, on the diameter and
*  circumference, like this thing and their resistivity and so on. And if you say that,
*  well, it shouldn't decay more than maximally say 1%. And that also depends on frequency.
*  So you have some criteria like this that you can use to sort of say, but, but again,
*  what you typically do, uh, well, what you could do if you're worried about this, you can sort of
*  change it and make a more stringent criterion and see if the results you're interested in change.
*  Right. Right. So that's like, uh, so, so that's sort of like, uh, so there are like these approaches
*  to at least do the, to like have some sanity tests in the model on the modeling itself.
*  All right. So in terms of, you know, what you've been able to accomplish, uh, you've been at this
*  for quite some time. And I mentioned earlier that, and I think this is correct that you started with,
*  um, trying to essentially predict LFPs and spiking, but LFPs was a local field potentials was
*  the problem. Uh, and I know that you, you are continuing to, um, you know, move into EEG
*  signals, which has not been as much of a problem as the LFP was originally, if I understand
*  correctly, uh, and other types of signals. So, you know, what, um, you know, what, what lessons
*  have we learned or have you learned so far about the importance of being able to predict these
*  signals? Yeah. So I would say what we have done, I mean, we have worked on these signals for like,
*  I guess, 15 years or something. And most of them was sort of the just sort of,
*  to look like what are called generic studies. Say if you have a population of, of, of
*  pyramidal neurons that receives a synaptic input, what really determines how strong the local field
*  potential measured inside this population would be. I mean, and morphology is important, but what
*  is also found is that it really did distribution of synaptic inputs. I mean, it's like, you say
*  homogeneously distributed, you get a very small LFP, even though the spiking resulting from this
*  might be very high, but it's just that you, you need this like asymmetry or unbalance in the input
*  sort of to, uh, and then another thing we found out is that, or we explore systematically. I think
*  people have sort of known this before, but I think we have done it sort of taking it to a quantitative
*  level and the effects of correlations, how correlated the synaptic inputs are. So that
*  really determines a lot. So say if you have a, so we had one, one paper that came out, I guess,
*  10 years ago or something where we looked at how local the local field potential is. So if you,
*  if you put down an electrode, you know that, well, if you measure a spike or spikes, you know that
*  they typically come from within a hundred micrometers from the tip of the electrode.
*  But what about the local seed potential? And then experiments have sort of had very different
*  estimates on that all the way from like a few hundred micrometers to centimeters. And what we
*  found by exploring it in a model is that these could be that this, this, what we call the spatial
*  reach very much depends on how correlated the inputs that are correlated to them,
*  correlated the, like the, the different, well, the signals that to the neurons that sets up this LFP.
*  So it's a little bit like if you have a microphone hanging over a football stadium,
*  right? And then it's, if there's like, it is like small talk and nothing is happening, just boring,
*  then it's, you don't hear it very well. But if somebody scores a touchdown, right,
*  you get this sort of some sense correlated chair and then you can hear it from outside the stadium.
*  So it's a, it's a little bit the same, the same kind of idea. If you have like this
*  correlated neurons that singing in, in synchrony, then you get a strong LFP.
*  So anyway, so these are the kinds of studies that we have investigated then. And also, for example,
*  if you measure an LFP, could it, is it necessarily due to neurons around you, around the electrode?
*  Or could it be this very loud neighboring population? And you have explored this
*  quantitatively and learned, I think, a lot about these, how these, how these sort of like,
*  what really determines that, that competition. And then they looked at sort of other aspect,
*  effect of active conductance, IH, for example, that you can, can they, how, how will they affect
*  things? So we have done studies like that. And now also, as I said, focus on EEG. Because,
*  I mean, the traditional way to analyze, one traditional way of analyzing EEG signals is to,
*  to try to do sort of like, identify estimate sources where there's like dipole sources.
*  And that's like an ill-posed problem and very hard, but you can put the constraints. So there's a lot
*  of work that has gone into this. But, and what we have done is sort of to add to this is that we
*  now can actually compute the current, if you have a particular neuron population that gets a synaptic
*  input at a certain place, we can compute the current dipole moments. So we can actually
*  make that connection between the current dipole moment and what's actually going on into the,
*  in the circuit. So that sort of is, is sort of what we have worked a lot on this,
*  what's called the forward modeling of electrical, electrical signals. So I would say
*  most of the work we have done has been on sort of finding these principles. What makes large
*  LFP? When is it large? When is it small? And, and also we have worked on making tests,
*  like ways to make test data for spike sorting algorithms, sort of like different kinds of
*  application of forward modeling, testing data analysis methods and so on. But now we are trying
*  to, to, I would say like the last couple of years in collaboration with the Allen Institute,
*  we're trying to use this to, to constrain and work towards this multi-purpose
*  version of this mouse visual cortex model. That is something we have actually a couple of workshops
*  that we have organized together with the Allen Institute, Anton Akipov. So if people are interested,
*  they can look it up on the net and find some, I mean, they are, they are out on YouTube,
*  this, this thing. So, so it's this, this goal of trying to, trying to make this multi-purpose model.
*  And one important thing is that, well, there's a lot of parameters, right? Obviously in this,
*  and you can think in these models and you say, well, with five parameters, you can fit an elephant
*  and right to the six, you can make it blink or whatever. But that is for statistical models,
*  right? When you just fit it to a mathematical function, fitting a curve to mathematical function.
*  But, but, but if you have this mechanistic models, like the physics type and the type of
*  network models and finding combination of connectivity or connection parameters and,
*  and so on, that sort of makes the LFP look right is very hard. It's not like it's easy at all. So
*  it's not like it's like many models that at least at the present stage, the hard, the, the
*  challenge is to find one model that actually is quite close to experiments. It's not that we have
*  if probably if you found one such model, we can sort of expand and find where it sort of is
*  find this parameter set, but at the, it's not like it's many models. It's very easy to find a model
*  that fits the experimental data because it's a mechanistic model. It's not a statistical model.
*  Well, so you've tested models with like a handful of neurons and you know, you're scaling up. How
*  much of a problem is that aspect of it of trying to find the right parameters for let's say an LFP
*  signal or something like that as you scale up and then and then what's your outlook on
*  scaling these simulations up? Yeah, in terms of one thing that the LFP is,
*  it's also it's a coarse grained signal, right? So I think if you, so it's not like moving
*  one neuron around a little bit or changing a little, it sort of takes the, it's sort of
*  the roar of the crowd in some sense. So, and we haven't, so we have actually now,
*  I mean, what we have done in the last paper that is just, well, coming out in, it's out on
*  Bioarchive coming out in Plus, it's out on actually it's out in Plus Computational Biology
*  where I looked at the trick for being able to, if you have even a firing rate model,
*  when you model say populations and say in a cortex and then like, I don't know,
*  laminarily organized set of populations and being able to convert that into
*  LFPs using a sort of like some tricks, we'll call the kernel trick, so that we're able to actually
*  to compute these signals without, because if you want to do brute force, it's actually,
*  it's actually quite additional. Well, I mean, it's really, it's an additional load. So if you want
*  to combine it with, with say firing rate models of like, you know, like the neural field models,
*  neural mass models, then you need to do some kind of trick to compute say the EEG contributions.
*  And when you want to make a neural field model for the whole brain predict EEG signals, then you need
*  some kind of trick. And that is something we have worked on. So the limitation, one important thing
*  is that finding a mouse visual cortex model, tuning the parameters so that it becomes
*  multipurpose is very hard. So that's going to keep us busy. It's not like an either or thing either.
*  I mean, you're going to get closer more and more sort of more and more multipurpose and we don't
*  really know how fast the progress will be and so on. But that's the hard thing. If you have a model
*  to compute the, this LFP and EEG and so on, that's very easy. The measurement physics is much easier
*  than the, sometimes the network physics. So it's a limitation is actually being able to make,
*  well, both make larger and network models covering maybe cortical areas and actually whole
*  cortices and making it make it have good sensible parameters so that actually it's,
*  it can actually predict sort of similar, predict some of the things that, of the experiments.
*  That's sort of the hard thing. But take going from that model to the EEG signals over the other
*  signals is not so hard. And the first of going, say going towards the human brain, it's, I mean,
*  obviously there's not only the problem of knowing enough about the neurons and particularly the
*  connections, but it's also then a matter of scaling up and being able to run large enough
*  network models that they sort of make sense and that their network behavior sort of like resembles
*  what you see in experiments. Of course, also in humans, you have much less data because you only
*  have, you don't have, it's essentially just EEG and MEG, which are non-invasive.
*  But I think that maybe it's a little bit like, if you sort of look at the, I mean,
*  like deep networks, again, convolution networks, the neuron dynamics, that is typically assumed.
*  You have this linear threshold, these ReLU networks. So the neurons are sort of fixed and
*  you tune the synaptic weights. And I think with this, say with the mouse visual cortex,
*  where they're mapped out using this patch electrode, this automated way to find quite good
*  neural models, I think the weakest link now is finding the synaptic connections.
*  I think we're better off making some kind of automated procedure for getting at least decent
*  neural models. So I think in our project, we often start with taking the neural models for granted,
*  at least as a starting point. And then we had to deal with the synaptic connection weights.
*  Okay. So I just want to understand and reiterate that, and I may be repeating what you've said
*  earlier, but you know, with something like predicting an LFP signal or figuring out how,
*  how widespread, from how widespread you're recording in an LFP, the goal is not necessarily
*  to understand the meaning of the LFP, but just to be able to get the models right so that when
*  you are testing these against experimental data, you know you have a well constrained and built
*  model, right? So it's not specific to interpretation of the signals you're recording.
*  It is specific to the model as a tool. That's true. Yeah. So it's, yeah, it's a way,
*  exactly. That's true. So it's a way to predict, given that you have your model,
*  if you believe in your model, if that's your hypothesis, then what are the consequences
*  in terms of what the LFP should look like? And because I don't think there's this question of
*  whether local field potential has sort of actually feeds back to and modulates dynamics. It could be,
*  I don't know, it's not quite clear how whether that is important in practice, but I look at LFP
*  sort of like, I actually talked about the Terry Sanofsky, which I made laugh, he called LFP the
*  exhaust fumes of the brain. Sometimes that's true. It's sort of, so it's more about what can
*  you learn from the exhaust fumes if that's the only thing you measure. So it's, I think that's
*  true. So if it's like a proxy for the spikes. So, yeah. So just to stick on LFPs for a moment,
*  neural oscillations kind of waxes and wanes as a focus of neuroscience. Like you mentioned,
*  Buzsaki, he's studied oscillations a lot. Is that something that is of interest to you to
*  recapitulate oscillatory dynamics also? For me, it's one of the features that a successful model
*  should sort of, say if you have a model for the hippocampal formation and so on, and where
*  obviously oscillations are prominent, then a successful biophysical based model of that should
*  reproduce the oscillations. So for me, it's another, it's sort of like where there's oscillations or
*  something else that's, yeah. So that doesn't really change in terms of the modeling. Even though
*  it's what we've shown, I mean, but it's important to, we, for example, found that we have like this,
*  for some of these hippocampal neurons, you have these resonances, I think, that you can sort of
*  get the largest, you get, how is it? I mean, you get the typical, sort of that largest LFP is at
*  some, I think it's theta frequency or something like eight hertz or something like that. Yeah.
*  But anyway, so we saw that we get actually, in principle, that could be an artifact of how the,
*  in some sense, how the IH is distributed. It's just like the, it's an IH messes up the, or changes the
*  LFP. So it just illustrates that you have to be, when you see an oscillation, it doesn't necessarily,
*  in an LFP, it doesn't mean that the firing rate necessarily is oscillating at the theta. Certainly
*  not, you don't get the weighting right, at least. So you have to sort of do, you have to do the
*  measurement physics, right? So that's why it's really important, I think, to have this modeling
*  framework sort of as like a way to test your hypothesis. When you have an idea that, well,
*  well, just whether it's like a firing rate thing versus like another thing that sort of sets up
*  the oscillation. Because it's, I mean, we have worked on this cable accuation and neuron models
*  and networks for a long time. We have really spent a lot of time on this in our group. And we are
*  still surprised by the predictions from the cable. And sometimes you have these intuitions that,
*  oh, then there should be a bump here. And then you do a simulation and then, no, it isn't. And then
*  they go back and figure out why it isn't there, maybe. But it's difficult to have intuition about
*  how the signal should be. It's all this what are called folk physics. It's sort of where people
*  sort of, they saw like these rules of thumb, which are sometimes, which should be tested. And they
*  sort of like, it's a little bit like spread from father to son or around the campfire in the science
*  community. So you have to test these things. For example, the thing that if you sort of measure
*  strong local field potential in layer four, in cortex, it doesn't mean that the neuron that
*  generates that layer LFP has a so my layer four, they don't have this locality that you have for
*  spikes. So these are stills, you see sometimes meet this still. So it's just that it's some of
*  these things have to be corrected. So I think it just make and make the field more quantitative
*  and precise and help us when we sort of do this kind of measurement physics exercises to get sort
*  of to at least not fail on that because it's so many other things which are inherently difficult.
*  You mentioned the recent kind of explosion in focusing on low dimensional manifolds and
*  the dynamics of populations of neurons. I mean, are there simulations that you do not long enough
*  to connect with that? Or how do you how do you see? How do you see that in general? And then do you
*  think about that in terms of your own models and simulations? Yeah, no, I think it's I mean,
*  if you think of say, if you want to make this mouse visual cortex model, right, so you have this
*  model with some hundred thousands of neurons. And say if you measure in animals that you then you
*  can measure these while you measure receptive fields and selectivity and so on. And they can
*  also measure these neural manifolds and experimental data. And then that's one thing that your model
*  can be compared with. It's another sort of things that you compare that based on spikes. So it's
*  another sort of like one another thing that I go and go that another kind of insight data that
*  you can use to constrain your model. So that's so I think that's all all these different measures
*  that you can get from that you can use to go to which you think are important is something you
*  can use it to test your model. So then you will have sort of like this benchmarking test suit,
*  right? If you sort of have this this non-monetization predictors, how does it well
*  does it do on this or how similar is it to whatever the present experimental data.
*  And then and then you have a little bit like they have for this what's called a brain score. Is that
*  what they have in the DeCarlo lab? Yeah, brain score. Yeah. So that is if you get some sense,
*  I mean a similar thing if you have a test suit not with a single brain score with some kind of
*  multi-objective thing and see how high dimensional high dimensional test scores. You got to reduce
*  the dimension of those also. Exactly. But it just to be so because I think that's why I think
*  what I like about this overall project for one thing obviously I think it's I mean it's it will
*  be cool to really understand a piece of cortex at the level that you understand the neuron, right?
*  That would be a very important thing and has so many. But I also think so many applications
*  and ramifications. But I also think it's because it's really a project or a program
*  where you can make progress because we can measure success because we compare with different kinds of
*  experimental data and you can compare how well you're doing. And at the moment we are far away
*  from that's certainly room for improvement in our models. I mean this is like I would say early
*  days and we only worked on this for two years and I hope that more people get interested in this.
*  I think this experimental data set that they have in electrophysiology and
*  optical physiology that they have freely available at the Allen Institute for these mice which are
*  like 50, 60 mice and they're the same age and everything is almost as reproducible as it can
*  be because it's almost like this industry style lab. It's a fantastic opportunity for this kind
*  of neuroscience which hasn't been there before. I hope there are some young eager brains in
*  whatever listening to this, US or Indonesia or Australia or North Finland or Norway or whatever.
*  All this data is available for everyone with a laptop and if you also get these
*  possibilities to do these large scale simulations from all these places, it's an enormous
*  opportunity for neuroscience. One thing I have to say because it's the reason I mean Hodgkin and
*  Huxley did essentially this made this neural model by themselves and ideally I would also like to do
*  the same thing for a cortex by myself or in our group. The reason we have this large scale
*  initiative like the Human Brain Project and others is really that it's collecting all this data and
*  also just building this infrastructure for simulating things. It's not the job for a single
*  group and also just making this what's called skeleton models, the candidate models just putting
*  up with some kind of plausible starting point. It's like many years. It's a kind of approach.
*  When you do this approach, the Hodgkin-Huxley style approach to say a network in a visual cortex,
*  you need the large community, many people. It's not like this collaboration has a value in itself,
*  that can be fun also but that's not really it. That's something you also make the case for in
*  that 2019 neuron perspective as well. I'll point people to that also. Gautu, I want to switch gears
*  and ask you one more question before we move on to some extra time for the Patreon supporters.
*  That's just kind of your broad thoughts about, so a lot of what we talk about on this podcast is
*  the connection between deep learning and AI and neuroscience and cognition and brains.
*  I'm wondering how you view your simulation-based approach with respect to a deep learning
*  approach to understanding brains and minds and cognition.
*  Yeah, obviously, concretely, the goal of my approach is really to mimic a piece of the brain.
*  It's not really at the moment. Hopefully, then expand it to go beyond just the visual cortex
*  to a whole brain. It has a very different goal. On the other hand, it's
*  now, if you want to sort of tune these parameters, I think everything is allowed in law,
*  war and optimization. If you get some clues from AI in sort of how starting point for making these
*  networks say, so that they get some extra hints so that the parameter space you have to search is
*  smaller. I think it's an especially have all this great brain power and of course,
*  resources going into AI. We have a bio-AI group also at our university, which I collaborate with
*  some people there also because it's fun. But also because I think we need sort of,
*  I don't know, I think you talked a little bit earlier on an early podcast about we should be
*  more charitable towards each other. And I think that's the very important thing. I think we should
*  be charitable is a good thing in general. But also in neuroscience, I mean, in this sort of,
*  in this like the goal of the task of trying to understand the brain, we don't have too many
*  success stories, I would say. It's not like clear. So I think if people should be very sort of open
*  to all the people's approaches and as less unless people are doing something which are clearly
*  unethical or like factually wrong. But who am I to tell? I mean, I pursue this like biophysically
*  detailed thing trying to model as a physical system, partly because I think it's promising,
*  but also I think because it's something I know how to do. Because that's sort of what I've been
*  trained, right? I'm trained as a physicist. If I figured out that what I really should do was monkey
*  experiments, that would be the most promising, that would be helpless, right? I could never do
*  that. I'm sure you can teach an old dog new tricks, but there's a limit.
*  Yeah, there are limits. So I don't know. And then you have like maybe on the other extreme,
*  you have like this or other opposite of this Elias Smith with this other what's called, right?
*  Spawn.
*  Yeah, Spawn, exactly. And we should just sort of root on each other and take compare notes and see
*  how we're doing. So we should be very, and I think AI also with the people working there trying to
*  make connections to the brain, excellent. We should just like what, for example, DiCarlo is doing and
*  comparing there. That's exciting. So I think we should be spend less time criticizing each
*  other's approaches and just try. Yeah.
*  So the AI models, right, are still built on, essentially built on neuroscience ideas from
*  very, very early on, you know, like point neuron kind of ideas, right, and are highly, highly
*  abstracted. So in that sense, are at the opposite of end of the spectrum of something like you're
*  doing, creating these simulations. And do you hope and or think that the simulation based approach
*  might actually end up teaching AI something or importing some principles into AI to help improve
*  artificial intelligence? Because it should in principle flow both, both ways, right?
*  I agree. Yeah, it could be. I mean, one thing that is, if you see this very successful,
*  deep learning applications, they are what are called like, single purpose, they're like category
*  image classification, right? And there's struggling with this transfer. There is not multi-purpose
*  in the sense that it can provide for many very different tasks. While the mouse visual cortex is
*  used as input for dealing with many different tasks. So maybe it's something with the neurons
*  and maybe they like, especially the temporal dynamics of real neurons, which are sort of not
*  captured. Well, deep networks is not captured at all. But even with these artificial networks,
*  that is crucial for to get to these multi-purpose things. So I think we should certainly,
*  we should certainly, well, as we start making, hopefully make more progress along these biological
*  networks and we get towards this multi-purpose models. And I certainly think that it should be,
*  well, that could be that that is something for the AI people to look at also.
*  So Gauta, thank you for the thoughtful email, which generated this conversation. I'll pass
*  this on to Carina also, I'm sure she'll get a kick out of me having had you on the podcast.
*  And thanks for being with me today and sharing some of your work and much luck moving forward.
*  Yeah. And well, thanks a lot for being invited. I really appreciate it.
*  I alone produce Brain Inspired. If you value this podcast, consider supporting it through Patreon
*  to access full versions of all the episodes and to join our Discord community. Or if you want
*  to learn more about the intersection of neuroscience and AI, consider signing up for my online course,
*  Neuro AI, the quest to explain intelligence. Go to BrainInspired.co to learn more. To get in touch
*  with me, email paul at BrainInspired.co. You're hearing music by the new year. Find them at
*  thenewyear.net. Thank you, thank you for your support. See you next time.

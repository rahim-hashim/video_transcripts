---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5599s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 11995
Video Rating: None
---

# BI 122 Kohitij Kar: Visual Intelligence
**Brain Inspired:** [December 12, 2021](https://www.youtube.com/watch?v=lzfijbO8qZ8)
*  I kind of wake up every day to sort of think that maybe my research is going to help someone's
*  life and I think this is kind of like, oh wow, what a great person you are.
*  But like I really, I mean, I think I'm going to tell you like a small story.
*  Maybe this is, please you can cut it out if it's not relevant.
*  Let's go to 5000 BC trying to explain it.
*  I'm trying time traveling back then trying to explain the motion adaptation model to
*  them.
*  And they're like, go away, like, you know, what are you talking about?
*  This is not, I don't understand anything.
*  So these models are not real models of the brain.
*  Like I don't know.
*  How is the network failing?
*  How do we know it is failing?
*  And like what could be the additions that you can make to the models that improves it?
*  I think to actually have a good quantitative, tangible grasp on those questions, I think
*  you need a platform like Brainscore to actually be there.
*  This is the model that tells you that what is going to be the predicted neural response
*  for any given image.
*  I think that's where we are in terms of that we think of this as a stronger test of the
*  model because there are many models then they've come up with different images then you can
*  test those as well.
*  This is Brain Inspired.
*  Hello, good people.
*  I'm Paul, Attemptor of good personhood, Master of None.
*  Today I bring you Kohitij Kaur, who also goes by Ko, Master of Core Visual Object Recognition.
*  So Ko has been a postdoc for the past few years in Jim DiCarlo's lab.
*  And if you remember, I had Jim DiCarlo on back on episode 75 talking about the approach
*  that his lab takes to figure out our ventral visual processing stream and how we recognize
*  objects.
*  And much of the work that Jim and I actually talked about was done in part by Ko.
*  Now Ko is an assistant professor at York University where he'll be starting his lab this summer.
*  His lab is called the Visual Intelligence and Technological Advances Lab.
*  And he's part of a group of people who were hired into a fancy new visual neurophysiology
*  center at York that is going to be led by none other than my previous postdoc advisor,
*  Jeff Schall.
*  So Ko and I kind of continue the conversation about using convolutional neural networks
*  to study the ventral visual processing stream.
*  And on this episode, we talk about that background a little bit and also Ko's ideas for where
*  it's going.
*  So as you may know, what started out as a feedforward convolutional neural network has
*  since been extended and expanded.
*  And Ko continues to extend and expand both the models to account for object recognition
*  and experimental work that will be used in conjunction with the models to help us understand
*  visual object recognition.
*  And that includes adding other brain areas and therefore models to more wholly encompass
*  an explanation of our visual intelligence.
*  So I get Ko's thoughts on what's happening, what will happen, and how to think about
*  visual intelligence and a lot more topics.
*  I linked to his lab and he is hiring as he says at the end.
*  So if you're interested in this kind of research, you should check it out.
*  I linked to it in the show notes at braininspired.co slash podcast slash 122.
*  Thank you as always to my Patreon supporters.
*  If you decide you want to support the podcast for just a few bucks a month, you can check
*  that out on the website at braininspired.co as well.
*  All right.
*  Enjoy.
*  Koji teach car.
*  Ko, are you an electrical engineer?
*  Are you a neuroscientist?
*  What the heck are you?
*  Yeah, I think I'm an electronics engineer, according to my undergraduate education and
*  training.
*  And then sort of I moved slowly gradually into like biomedical engineering, one step
*  towards neuroscience maybe, and then finally did a PhD in neuroscience.
*  What was it that got you interested in neuroscience?
*  I think like a lot of us, I think those were discussions about consciousness and things
*  like that, that I kind of cringe upon a little bit now.
*  But those were the introduction to neuroscience.
*  And I think I particularly got influenced by a lot of these very nice storytellers.
*  So I was doing my master's at New Jersey Institute of Technology, but I was sort of cross registering
*  for courses at Rutgers where Yuri Buzhaki was a professor back then.
*  And just like listening to him and the way he talks about the brain, I think those kind
*  of those were sort of the initial hooks to like, I really want to be in this field and
*  be with these people and like talk about the brain with them.
*  Things like that, like sort of at a very artificial sort of superficial level mostly.
*  And I remember going to one talk from V.S. Ramachandran at Princeton.
*  And it was like those kind of things were like, wow, like this is such an interesting
*  system and I want to work on it.
*  And I think that were the initial things that kind of like drew me towards studying the
*  brain.
*  The storytellers.
*  The storytellers pretty much.
*  And I think now I'm kind of like thinking there could be something beyond storytelling.
*  And like, but I mean, the storytellers are perfectly fine scientists and they also do
*  a lot of stuff that I kind of do now.
*  So like there's nothing against storytelling.
*  I think that component that I sometimes kind of feel like, oh, what is the use of that?
*  I think it's really useful because like to tell a story about your science in a way that
*  sort of attracts young minds, I think is very useful.
*  But now, so, so consciousness and storytelling drew you in, but now you've discarded both
*  of them as frivolous.
*  I don't think I've discarded them as frivolous.
*  I just have I think my time is spent better doing other things than that.
*  I don't think those are like bad problems to work on or like useless things.
*  I think that's actually very useful.
*  But I kind of realized that that's not my sort of, you know, foretell.
*  Like that's not my expertise is not doing that.
*  What percentage of people do you think who, you know, are drawn in are drawn in because
*  of like the big questions like that?
*  And then, you know, I said discard or, you know, whatever I said, but then go on to realize,
*  you know, start asking very specific questions and kind of leave those larger things by the
*  wayside.
*  It's a really high percentage, isn't it?
*  I think so.
*  I think it's a very high percentage.
*  But I think also it probably is useful to kind of keep reminding ourselves what the
*  big questions are.
*  And like, so I think that's simultaneously very important.
*  It's just that the sorry.
*  No, no, that's fine.
*  I was just going to say that I think part of the reason and I don't really know the
*  whole reason, but I think part of the reason is that those big questions get you in and
*  then you realize that there are a lot of big questions that are super interesting that
*  aren't those questions.
*  I don't know.
*  Does that seem on point?
*  I think that's right.
*  And I think that's kind of like very similar to how I feel right now.
*  And I think I mean, I know that it's sort of like said multiple times that it's all
*  about like asking the right questions and like the questions are very important.
*  But what at least from my perspective, I think I've realized that like the answers and what
*  do I consider a satisfactory answers to those questions often determine like how you approach
*  your science and things like that.
*  So to me, like it's just not about the questions.
*  Also like what kind of answers am I satisfied with and why am I seeking that answer?
*  I think those are the real drivers of what I actually do in the lab.
*  Yeah.
*  Of course, I would like to like, you know, simulate, I don't know, consciousness in
*  an artificial system.
*  But I think that that is going to be a very difficult kind of objective to, you know,
*  go for it in a lab and get funding for it.
*  I'm really happy that some people are trying to do that who are more privileged than probably
*  I am.
*  But congratulations on the new job.
*  I guess it's not so new now.
*  But where are you where are you sitting right now?
*  You're not at York yet, are you?
*  No, no.
*  I'm still at in Cambridge, Massachusetts at MIT at McGovern Institute.
*  When are you?
*  So when are you headed to York?
*  Yeah, I'm starting in July 2022.
*  Nice.
*  Well, congratulations.
*  Yeah.
*  Thank you.
*  Thank you.
*  Yeah, I'm very excited and was a very interesting hire because all of this happened during the
*  pandemic.
*  Yeah.
*  I'm still supposed to go and see the department to some degree.
*  Oh, wow.
*  Yeah.
*  I'm really virtual remote, but I'm very happy so far with what I have all the discussions
*  that I've had with colleagues there and I'm very excited to start working.
*  You'll be you'll be near my my postdoc advisor, Jeff Shaw up there.
*  So yes, he's great.
*  Yeah, yeah, I'm very much looking forward forward to working.
*  Tell him that I you know, I've asked him a couple times.
*  He's been pretty busy because he just moved to York as well.
*  Tell him that I'm still waiting for him to come on the podcast.
*  So okay.
*  So so you you your your most recent work was a postdoc in Jim DeCarlo's lab and Jim's
*  been on the show and you guys are.
*  Yep.
*  One of the reasons why I asked you about your engineering background is because you guys
*  are quote unquote reverse engineering the visual system.
*  Right.
*  I guess it all started off with convolutional neural networks and the feed forward story
*  of convolutional neural networks.
*  I don't know how you got into deep learning, but I do know that you were discouraged at
*  one point from from studying deep learning or using it.
*  Can you tell that story?
*  Sure.
*  Yeah.
*  So, I mean, it's an old story.
*  It's like probably like now already 10, 11 years old.
*  This was 2008 when I started my master's in biomedical engineering.
*  I think I kind of realized talking to a lot of people back then is that even saying the
*  word or saying something like, oh, I'm working with a computational model and I'm in a neuroscience
*  program, it's sort of like you look down upon as a fake neuroscientist.
*  You're not one of the real people that is doing the real neuroscience.
*  Experiments because you're not doing experiments?
*  Because I was at that time I was not doing experiments and I was mostly trying to like
*  look at things like, for example, like, you know, I was doing like working on autoencoders
*  or neural network models trained with back propagation, basically looking at how internals
*  of these networks might match some neurophysiological data that I had or some behavioral data, aka
*  the things that everybody, including me, is all excited about these days.
*  But like, but that was before the quote unquote deep learning revolution in 2012, right?
*  So it was, I think it was still popular back then among certain groups, I guess.
*  But I just did not, I mean, I could not predict that if I had worked on that, maybe there
*  could have been some nice papers or nice studies that I could have done.
*  But as I was saying that like, I kind of got a bit discouraged because like I just started
*  realizing that, oh, this is not the real neuroscience because I'm not sitting there with a slice
*  of a mice brain patch clamping and like looking at neuronal voltages going up and down on
*  a stupid monitor or something.
*  Like I kind of felt like, you know, that's the real deal.
*  And I remember I prepared a poster for a conference and I was going to present this poster which
*  is work done with like these artificial neural networks.
*  And I think I was so, you know, I was afraid that I would be ridiculed at that conference
*  that in the morning of that day I can just got out of there.
*  Like I'm not going to present this, forget about it.
*  I'm going to go back and I'm going to do real neuroscience and look what I'm doing right now.
*  So I have a, unfortunately it's really ridiculous, but it's kind of pathetic.
*  But there's a paper that I wrote back there with all these ideas of like a back prop,
*  like reinforcement learning, autoencoder, student teacher network.
*  And it's really badly written and don't look at it.
*  But like I kind of use that as a joke with my friends, like only if I had pursued this,
*  you know, like all this work from Dan and Jim, like, oh, I was way before that.
*  Did you tell Jim that?
*  It was ridiculous and pathetic.
*  No, I don't think he would take that.
*  That paper is a joke.
*  Yeah.
*  Well, yeah.
*  Well, you were talking, so real neuroscience, that's interesting because what you described
*  with the mouse brain slices and patch clamping is exactly how I cut my teeth in neuroscience
*  because I was a real neuroscientist.
*  Right.
*  Do you think the definition of what a real neuroscientist is has changed now so that
*  people, you know, doing what you do is, do you feel?
*  Like a valid neuroscientist now?
*  Yeah, well, I kind of validated myself by doing monkey physiology and like perturbation.
*  So whenever I'm doing that, whenever I'm leading that life, I feel like as a real neuroscientist.
*  I mean, I still think that like, actually, it helps to look at the brain and the biological
*  data to get the right perspective about the system.
*  So I definitely value that.
*  But I think with time, the importance of computational techniques and analysis techniques are so
*  important now.
*  I think as we were discussing, like there's an answer that we are seeking and that answer
*  to me is going to be in the form of those models.
*  And so like, if you're not talking that language, it sort of becomes difficult to communicate.
*  It will become difficult to communicate any neuroscientific finding in the future.
*  So I think in that regard, that might become the real, you know, talk of neuroscientist
*  in a few years if it hasn't become that already.
*  You're looking for an answer.
*  What's the question?
*  That's a very good question.
*  So I think exactly.
*  So the question that I think a lot of people are interested in is that how do we solve
*  certain tasks?
*  Like at least that's the way how I look at formulating questions.
*  Like I'm interested in neuroscience because I'm interested in a behavior.
*  And why I'm interested in that behavior, particularly maybe because if that behavior goes missing,
*  I'll be in deep trouble.
*  So like that's kind of my sort of way of getting into this space of like, okay, there's
*  a behavior, then what does it mean to do a behavior and how do we actually scientifically
*  study it?
*  So we measure this behavior, we operationalize that behavior with some tasks and we measure
*  that and then the understanding or the question is that like, how does the brain solve that
*  problem or give rise to that behavior?
*  And then we start by building models of that behavior and depending on what type of answers
*  we're looking for, are we looking at how different neurons come together and produce that behavior
*  or how different brain areas are participating in that behavior, we try to like, you know,
*  build specific units or parts of that model and look at them carefully.
*  So at least that's how I formulate the questions.
*  The bigger question is like, okay, there's a big behavior and how are we actually solving
*  it in our brain?
*  Well, so you can correct me if I'm wrong here, but the story as I see it from Jim's lab and
*  from the convolutional neural network work is that, you know, you're trying to solve
*  object, core object recognition and, you know, it started off with a feed forward neural
*  network, you know, that was built through many years and then, you know, the deep learning
*  world came on the scene and you guys realized that these networks accounted well for predicted
*  the brain activity well and kind of went on from there.
*  But things have developed.
*  The reason why I asked what the question was is because, you know, it's interesting.
*  It's almost like an isolated system, right?
*  So you have this convolutional neural network and it is modeled, the layers are modeled
*  after the ventral visual processing, hierarchical layers in the brain.
*  And you know, the goal is to understand vision, right?
*  And I don't know what that means.
*  Do you feel like you guys have a where are we in understanding vision?
*  Yeah, I think there's a lot of questions in that in the center because like, let me maybe
*  like explain a little bit about what I think of what understanding means, maybe like.
*  So I think one definition of understanding that I have in my head is that it is basically
*  coming up with a falsifiable model of something like if I understand something and you can
*  tell me that it's a wrong understanding and if I can basically have a model that is falsifiable,
*  which like I can make predictions and you can tell me that, oh, you're wrong.
*  So for example, and there could be different levels of this understanding.
*  So I understand how my coffee machine works because I can predict which button to press
*  and the coffee is going to come out.
*  It's like a concrete prediction.
*  You can test me like, oh, you can tell me like, go turn on the coffee machine and go
*  press the wrong button.
*  You're like, you don't have any understanding of how this machine works.
*  But if I press the right button and the coffee starts coming out, but then if the machine
*  breaks down, there's a different level of understanding.
*  I might need to fix it.
*  So like then I then you might ask me like which part of the machine to fix and how does
*  it work?
*  And there's a more detailed level of understanding required.
*  So in the same way, I feel like understanding vision would require multiple levels.
*  And I think one of it is like the behavioral level, like I predict a behavior.
*  So that's where we start.
*  But all of this sort of relies on models like concrete computational models.
*  At least that's what my current sort of understanding, like my current sort of opinion of like what
*  understanding for me might mean is that like you have concrete computational models that
*  make explicit predictions about, you know, how a system is going to work or perform and
*  then you get to test it.
*  And that's sort of the understanding and that that's moving.
*  Now the problem, I think usually is that if we define understanding this way, then we
*  have to also sort of have common, I don't know, goals of like what are we trying to
*  understand?
*  Like what is that behavior?
*  And my current view of the field is that we actually don't have common goals like that.
*  We are kind of like all doing our own things.
*  And so I think it's kind of important to maybe like have certain specific goals as like this
*  is what we are trying to predict.
*  These are the behavior of the system.
*  These are the neural data or something that we're trying to predict and then come together,
*  like come up with what are the best models that can do that.
*  And some of it is we are currently trying to do it with this website and platform called
*  Brainscore and trying to have an integrative approach to like all kinds of data and all
*  kinds of model and things like that.
*  So how's Brainscore going?
*  Are a lot of people using it?
*  Yeah, I think the user base of Brainscore is definitely increasing.
*  And I think we are having a conference now.
*  Well, we still submitted it at COSAI and we are potentially going to have a competition.
*  It's like I think it's going to feel a little bit more like an ImageNet competition or something
*  like that.
*  But my personal opinion is that maybe someone can look at Brainscore and say it's too early
*  for someone to like start making these models and or scoring them and being so concrete
*  about it.
*  But I think it has to be done.
*  That's kind of my goal.
*  If you ask me where vision, like understanding of vision is, to me, like pointing to some
*  kind of platform like Brainscore is a concrete answer that I can give.
*  That's my way of modifying it.
*  Yeah, so it's a benchmark.
*  But on the other hand, benchmarks have gotten some flak because like you were talking about,
*  we don't know whether that's the right benchmark, right?
*  Whether it's the right question.
*  So it is concrete, but I guess we're progressing and asking better questions.
*  Would you agree with that?
*  Yeah, absolutely.
*  And I think there is no like three or four benchmarks that will define our understanding.
*  So I think the goal is to have more and more benchmarks and hopefully we will see that
*  because it's the same brain that is giving rise to all that data.
*  So if you're actually modeling that particular brain, then we should be converging to like
*  a very small space of models eventually.
*  At least that's the dream.
*  So of course, like there could be multiple different benchmarks and different ways people
*  are probing the system.
*  But I think the value add of Brainscore is that if we can get all those experimentalist
*  and modelers on board, then they can provide those data or provide those sort of benchmarks
*  as also targets for current systems.
*  Instead of saying that like, oh, you know, your network is never going to predict that.
*  Like, okay, that's okay.
*  That's fine.
*  Networks are falsified under all possible benchmarks.
*  So it's not a big sentence to say.
*  But it's just like, how is the network failing?
*  How do we know it is failing?
*  And like, what could be the additions that you can make to the models that improves it?
*  I think to actually have a good quantitative, tangible grasp on those questions, I think
*  you need a platform like Brainscore to actually be there.
*  I want to ask you about falsification because you've talked about how that's one of the
*  useful parts of the modeling push is that they are falsifiable.
*  But then, you know, you have models like the feedforward convolutional neural network that
*  predict what is it like 50% of the neural variance somewhere around there?
*  Right.
*  Yeah.
*  How does one falsify a model?
*  Yes, I don't think I mean, in the sense of falsification, those models are all falsified
*  anyways.
*  But then the question is, how do you build the next best model?
*  When I think of that, I feel like given some numbers like that, it then makes me kind of
*  figure out if I build a better model, it should at least be better than the current numbers
*  that are coming out of the feedforward neural networks or something like that.
*  So I think, of course, the question that you dismiss the entire space of models or family
*  of models as like completely useless or do you say like, that's a good start, let's build
*  upon that and start adding elements to that to build the next best model.
*  I think I'm mostly motivated by this idea that yeah, like we have a good grasp and thanks
*  to machine learning and AI for that, for actually building these real models and not like toy
*  models.
*  And so now that we have these models, let's capitalize on this momentum and get going
*  and build the next probably build the next best models.
*  Although I'm talking about models in this way, but my personal life is mostly spent
*  doing experiments trying to put holes on that on those modeling frameworks or models.
*  So I'm actually very happy that those are all falsified because I feel like that's my
*  job to falsify them.
*  But the other part of my job that I feel like is important is that it's not only just to
*  falsify them, but also get some data that is in the same scale and in the same sort
*  of spirit that would help build the next better, the best model or something.
*  So it's just not good to shit on them.
*  It's just also provide some material for them to work on, chew on and become a little bit better.
*  So what in your so you're doing a lot of experimentation.
*  What's faster modeling or experiments?
*  Experiments faster.
*  Yeah.
*  I mean, I think building a better model is way more difficult than doing an experiment.
*  This is I think I'll debate anybody about that because I think for me, like, you know,
*  so again, depends on which field you are.
*  If you are building this model for AI purposes or like so there, of course, modeling is way
*  more faster than any behavioral experiment or any neural experiment.
*  If we are trying to build a model of the brain, it's a so it's like we're discussing about
*  this engineering thing is that, okay, I have a problem of like how is the brain working,
*  but the solutions cannot be anything.
*  It's like constrained by this biological system.
*  So there's like a specific solution that we're trying to look at.
*  And I think aligning the models with that is a very I mean, I can build a model that
*  might solve action perception or action prediction better than the current system, but that
*  might not align with the brain.
*  I think when I said like the modeling of is slower, I think it's that bit which is like
*  having models that are more aligned with brain because you know, like 2012 Alex Net came
*  up and then now we don't even talk about Alex Net in terms of like computer vision.
*  I think no serious computer vision scientists would say like Alex Net is my model that I
*  start with, but it came to neuroscience and it's still here.
*  We are still using Alex Net.
*  So I think things come to neuroscience and they stay for a longer time because it's just
*  very difficult to falsify or like discriminate among these models even.
*  And I think there are maybe in your I mean, for us there's some of them are like there's
*  some deeper questions in here as well maybe because like when we say we have a model of
*  primate vision, like what do we actually mean?
*  Do we have a model of a specific human or like a specific monkey or are we modeling
*  the shared variance across humans or monkey or you know, are we developing a model of
*  the you know, all the possibilities like a superset of vision?
*  Like so how well should a model of object recognition even predict behavior of one subject
*  or some neuron that I'm recording for in a monkey brain?
*  I think we need to think carefully about those questions because like, yeah, sure, like the
*  model might predict, you know, one neuron in a monkey's brain at 50% explained variance,
*  but then how well does any other neuron in any other human brain predict that other another
*  human's IT neurons or something like so.
*  I think quantifying and sort of setting up the ceilings based on what we actually are
*  modeling are we modeling individual human beings or individual monkeys or you know,
*  the shared monkey population.
*  I think those questions are sort of important and then maybe we are done with like predicting
*  core object recognition feed forward responses because you know, one monkey predicts another
*  monkey at 50% and there's no way you can improve beyond that.
*  So it's to me, I think because of these kind of and of course, as I'm saying it, I'm realizing
*  that like this is basically like it's empirically challenged in some sense.
*  So it's actually the experiments that have to provide these answers and we are sort of
*  like limited by technology and how well we can probe the system.
*  So that's why I think slower.
*  Yeah, okay.
*  Well, you said ceilings.
*  So the way you've talked about it, it makes me it's a fuzzy ceiling, I suppose.
*  They're fuzzy ceilings in that respect.
*  Sure.
*  Yeah.
*  All right.
*  So you're I'm slowly coming around to the fact that modeling takes a long time.
*  I did I didn't do any deep learning modeling.
*  I did like a kind of a psychological model.
*  It was very simple, right?
*  And it took a long time.
*  But experiments I had to go in every day and it just was, you know, years to publish a
*  single paper.
*  I see where you're coming from.
*  And I totally I mean, that's has been sort of my experience as well.
*  I mean, it takes a long time to train a monkey to implant the arrays and get the data and
*  maybe the array doesn't get implanted well, then you have to like implant again.
*  Like there are multiple problems that can come up.
*  But I just feel like at the end of the day, you have some data and if you have designed
*  your experiments properly, that's like, especially neuroscience, which I think is still in the
*  dark ages, like it's sort of like novel data.
*  It's like just it's anything you do, you can you can basically it's like novel data
*  and a target for like a model to sort of predict.
*  And I think in that way, it's faster because I can build a model like one minute, you just
*  put some two convolution layers together and call it a model.
*  But is that really useful or is that really taking the field forward?
*  I mean, I mean, maybe I answered it too fast about like experiments are slower.
*  Yeah, you need to think about that more.
*  I might have to think about it, but I think but I think I'm trying to sort of like tell
*  you a little bit of why I think modeling is actually going to be slower, especially like
*  modeling the brain.
*  There's physical time, but then there's also heartache time.
*  So maybe those are two orthogonal things, right?
*  So like the other question would be like, where do you experience more heartache and
*  obstacles?
*  And do you think modeling would be the answer to that?
*  Again, depending on your experience.
*  So like if I'm like running a monkey, like after I have like, you know, brought a monkey
*  to the lab and done an experiment, I have zero energy to do and think about anything
*  else in the day.
*  So it's like I'm done for the day.
*  And I think that way, yes, it's a lot more I mean, at least because that's the experience
*  I have and I cannot tell how bad it is for like a modeling person to know how bad it's
*  like to come up with, you know, like a giant model.
*  My code, my code.
*  Yeah, most is like the libraries are not loading.
*  The version is not correct.
*  So those are the problems that I usually face.
*  But yeah, but at the end of the day, what was the model's training?
*  And I don't know.
*  I mean, at the end of the day, I feel a modeler is going to be more disappointed because the
*  models don't really predict much more than the previous model.
*  That's what the neuroscience experiments, if it's designed properly to begin with, I
*  think it's always going to give more insight.
*  All right.
*  Just a biased opinion.
*  Yeah, we're all we're all biased, as we know.
*  All right, so again, correct me if I'm wrong.
*  But the way that I see it, there's this core object recognition story that at the core
*  of it is a feedforward convolutional neural network.
*  And, you know, you guys in Jim's lab have done a lot to explain neural data.
*  So that's kind of like the basis the way that I see it.
*  And then from there, you've done a lot of other work.
*  Like you've started adding bells and whistles like recurrence and you've controlled you've
*  synthesized images to predict which neuron is going to be driven by a particular image.
*  So you're making the models more complicated.
*  And I've heard you argue that these that what we need is more complicated models.
*  Whereas, you know, from a from a philosophy of science classic perspective, what we like
*  are simple models.
*  Right.
*  And because part of the problem with these deep learning models is that we don't exactly
*  know how they're doing what they're doing.
*  And to use a complicated model to explain a complicated organ like the brain, there's
*  pushback on how much that actually buys us in terms of understanding.
*  But you argue that, no, we actually need them more complicated.
*  Why is that?
*  Yeah, I think depends on how you define complication, because I think the reason why I might say
*  that we need more complicated models because the models are not really predicting what
*  we set out to predict.
*  So I think making them simpler.
*  I mean, I don't know.
*  I mean, I don't think that's going to be the answer because the brain is complicated.
*  So anything that is a simulation of the brain will look complicated in some sense.
*  In the other sense, it will not look complicated because if you have correspondences and alignments
*  with the brain, you can point to a part of the model and say, oh, that's before and you
*  can say like that's before in the brain.
*  So in that way, it might be become less complicated over the course of just a definition of like
*  what complication and like what is interpretability and what is understanding.
*  I think those and because there is no objective definition of those things.
*  And I think these kind of conversations usually, you know, lead nowhere.
*  I mean, I'm trying to think of this thing like, for example, when I was in my graduate
*  studies and during my PhD, we had models of motion after effect.
*  And if I spoke to anyone like at VSS or SFN or Cosine about these models, everybody would
*  say like, oh, this is completely understandable, interpretable, simple models that we have
*  intuitions about, which is like, OK, you show coherent, so you show a random motion pattern
*  and you have these motion detectors, they're all firing and they're all firing equally.
*  There is no like basically if you after that, if you show a stimulus that is moving upward,
*  the upward neurons will do something and it's going to be like some response, which is going
*  to be higher compared to the rest of the group.
*  If you are only showing upward motion for a long time, those are the neurons that are
*  going to fire and get fatigued.
*  And then when you show like a random pattern, you will see like everything else is firing
*  higher and the upward motion detectors are kind of firing a slightly lower.
*  So overall you will have, you know, bias towards saying, OK, it's going, maybe the motion is
*  going downward, something like that.
*  And this can be modeled and people have modeled this and I think those models compared to
*  artificial neural networks now, like they might be considered simpler, more intuitive,
*  understandable models, less complicated.
*  Now I'm thinking like, let's go to 5000 BC.
*  People are talking Tamil or Sanskrit or I don't know Greek or some other language, trying
*  to explain, I'm trying time traveling back then, trying to explain the motion adaptation
*  model to them.
*  They'll be like, go away, like, you know, what are you talking about?
*  I don't understand anything.
*  So these models are not real models of the brain.
*  Like I don't know.
*  And I think I feel like the same thing is happening now, which is like artificial neural
*  network.
*  But remember like the motion model that I just mentioned was predicting this adaptation
*  phenomenon, this behavior.
*  So that was kind of the goal of this modeling.
*  It had some relevance with how people have looked at the brain and neurons.
*  But if I tell this in 5000 BC, people will be like, I don't know, this is not mapping
*  into our worldview.
*  And I think the same thing might happen right now with convolutional neural networks and
*  some terminologies and things like that.
*  It's like, OK, this is too complicated.
*  This math, I don't, I cannot like fit into my low dimensional kind of behavioral space
*  how this high dimensional areas are functioning or responding.
*  So I don't take that complaint seriously because I think with more familiarity with these
*  terms and models, that that complaint is just going to go away.
*  As the models become more and more powerful in predicting different behaviors and we will
*  see, for example, use of having these models in sort of like real world applications.
*  And I think that kind of fear of, oh, this is a too complicated of a system is just going
*  to go away.
*  And for those for whom like this won't go away, they'll just probably have to live with
*  it.
*  Yeah.
*  OK.
*  But maybe the more interesting, I think one of the reasons why I feel people like simpler
*  models is it allows them to like maybe think through like if the model gets stuck, what
*  to do to improve it.
*  And I think that to me is like a real value of having a simpler, more interpretable model.
*  And there it's a question of efficiency.
*  If you can have a complicated model, kind of self correct yourself or self improve itself,
*  which is kind of a future goal, maybe that might just be a more efficient way of dealing
*  with this problem than than kind of like humans kind of coming up with their own intuitions
*  of like what is a better model and things like that.
*  And I think we were discussing about this engineering background.
*  To me, that might be something I'm more prone to accepting because of my engineering background
*  I just feel like there's a question, there's a solution, and these are just tools to get
*  to the solution.
*  Doesn't matter if I intuitively kind of understand it or not, as long as it's aligned with the
*  brain data and things like that, it's fine.
*  So one of the I actually got even more excited to talk to you because after we had set up
*  this episode, someone in my course asked because I talk in my course, I talk a lot about I
*  use Jim's work and your work to talk about convolutional neural networks and how you
*  know how it relates to the ventral visual stream.
*  And then someone in the course asked, what about the dorsal stream?
*  Because I talk about the two visual streams.
*  And this goes back to the question of like what it means to understand vision.
*  And I know that one of the things that you're doing, so the question was like, why aren't
*  there models for the dorsal stream as well?
*  Why is it all ventral stream?
*  And I know that you are starting to incorporate and you have some background with the dorsal
*  stream as well.
*  And maybe we should talk about what the dorsal stream is just to bring everyone up to speed.
*  But what are you still are you just starting to incorporate other brain areas now?
*  What is your yeah.
*  Well the first thing is that maybe if that student is interesting in doing a PhD or a
*  postdoc, send them my way because that's that's the kind of question I was also asking about
*  like what is it also stream doing?
*  Because I had spent like five, six years studying the dorsal stream, which is slightly.
*  Above the ventral stream in sort of anatomical location in the brain.
*  Let's say what the dorsal stream is like what it classically is.
*  Do you want to say it?
*  I'm happy to as well.
*  You can say so.
*  Yeah.
*  So classically there are two ventral two visual streams.
*  It hits V1 and then it kind of branches off into a ventral stream, which is what the massive
*  amounts of neuro AI and core object recognition is about where it gets processed over hierarchical
*  areas up through V2 before IT until we suddenly have neurons that respond to whole objects.
*  But the dorsal stream is classically the where or how stream, which is much more related
*  to the motion and spatial aspects and our actions.
*  So it's activity related to and that's where I spent my career is basically from more or
*  less in the dorsal stream.
*  Yeah.
*  So I don't know.
*  Did I explain that OK?
*  Yeah.
*  Yeah.
*  Absolutely.
*  I'm usually now like I think I'm usually very careful about assigning some behavioral
*  function to areas.
*  I mean mostly start talking about anatomical locations.
*  Who knows?
*  Like you might find that the stream is just a big part of core object recognition.
*  Right.
*  Well, yeah.
*  I mean, so the thing that has been, I guess, always known but not paid so much attention
*  to is that there's a lot of crosstalk between the dorsal and the ventral stream.
*  But we've kind of studied them in isolation, right, as two individual separate things.
*  Yeah.
*  I mean, I think that's sort of I see that as an opportunity to sort of like really take
*  this sort of studies forward and trying to incorporate looking at dorsal stream as well.
*  One point I wanted to make is that I think there are folks who are beginning to build
*  models of the dorsal stream in the same way as the ventral stream modeling has gone.
*  I think I recently saw a paper from Chris Peck's group.
*  Sorry if I'm forgetting other authors.
*  I think Blake Richard was part of it.
*  Patrick was part of it.
*  I think it's a bio archive at least.
*  There's work done from Brian Tripp's group trying to model these systems.
*  Of course, dorsal stream has a lot of modeling, prior modeling work that is not kind of similar
*  to the convolution neural network stuff.
*  But I think people are beginning to build them and there are different objectives that
*  they're proposing as normative framework for how the dorsal stream gets trained up.
*  I think those are nice hypotheses and we'll see whether the data actually supports those
*  models or stuff like that.
*  For me, trying to get into this area, those are really nice work because that gives me
*  some baseline ideas or baseline models to start testing and probing.
*  When I start designing my experiments, I think those models will really help me to make a
*  good experimental design.
*  Are you building?
*  I actually don't know what kind of model because it wouldn't be just the same.
*  You wouldn't just use a convolutional neural network to model the dorsal stream, right?
*  Are you building models yourself also or are you going to incorporate?
*  I have not personally built any models right now.
*  I've just been testing some of the models.
*  I started testing some of the models that were mostly used for action perception or
*  action recognition models.
*  They have these temporal filters.
*  They're still convolutional.
*  It's just more dimensions to the convolution.
*  It's like a time dimension.
*  I think those are good starting points because they're easy to build maybe because they can
*  use the same kind of training procedure.
*  I think we have to at some point become a little bit, be okay with being a little bit,
*  go lower in terms of prediction because we need to move from static domain to a dynamic
*  domain.
*  I think my usual experience has been that whenever you make this jump, all these models
*  start to not perform as well, not predict the neural responses as well.
*  I think to me that might be one of the reasons why maybe some people are building these models
*  and they're not really coming out because they don't really predict anything.
*  Maybe backing up a little bit, my main interest in this dorsal-venture interaction question
*  kind of started when I was mostly recording, showing static images to the monkeys and recording
*  their responses in IT.
*  These are objects that are either like natural photographs or some kind of synthesized images.
*  I started thinking about my previous work in dorsal stream and it was about motion and
*  there were dots moving and gratings moving.
*  But if I think about the real world, I never see dots moving or gratings moving in the
*  real world.
*  There's objects are moving.
*  If I have to have any real world relevance of my current research, I just felt like it's
*  a dynamic world.
*  I'm moving my eyes and I'm moving myself and the objects are moving.
*  If I think of these questions or think of these behaviors, dorsal stream kind of pops
*  up in any literature search that I do.
*  Self-motion, motion of objects or motion of like, not objects, but like maybe motion of
*  like something in my visual field.
*  But then I was wondering, IT has this nice representation of what the object is and if
*  the object starts to move, does all of it fall apart?
*  What happens?
*  Just out of curiosity, I just started recording from these neurons and when the objects were
*  actually moving and then I started kind of, this work has not been published, but it's
*  like the sort of preliminary result is that, well, IT kind of can predict where the object
*  is headed, where it is moving.
*  We know from previous studies from Jim's lab that from looking at IT representations,
*  you can tell where an object is.
*  This was from Ha Hong and Dan 2016.
*  Where the object is located, you can tell in a static image.
*  So there's one trivial solution where, okay, like if you can tell where the object is located
*  at different time bins, you can maybe combine that information to tell where the object
*  is headed or where the object is going.
*  What I started finding is that like, it's not only that, it's like you can just take
*  a snapshot of like maybe after you have started this movie, two-hundred milliseconds or three-hundred
*  seconds later, you can just look a small time bin and you can tell where the object has
*  been going.
*  So it's like there's a predictive signal of where the objects are headed.
*  So that sort of like, then I started thinking like maybe this is coming from the dorsal
*  stream or is it, you know, like, but again, these are again, like ways of thinking that
*  I've kind of discarded in the last few years.
*  So I feel like the way to think about this is like, can a vanilla ventral stream model
*  explain this neural responses already?
*  Then not to invoke dorsal stream at all.
*  Maybe they will fail and then the dorsal stream models are actually necessary to, you know,
*  account for this neural responses and also the behaviors that I can test based on this
*  kind of stimuli.
*  So that has sort of been my approach and the dorsal and the quick update on the ventral
*  stream results is that these models, they're not really predictive of these kind of responses
*  at all to some degree.
*  That gives me hope.
*  It's always good to have hope when you're starting your career, although not that you're
*  starting your career, but your new start.
*  Yeah, exactly.
*  But you said you've discarded thinking about it in that way from like different brain areas.
*  Is that because you've discarded thinking about different assigning roles to individual
*  brain areas or?
*  Yeah, sure.
*  Absolutely.
*  I mean, that's that whole way of thinking is like, I think it's primitive.
*  It's not going to lead to like the brain is doing what it is to like make us go through
*  the day and like all areas are coming together in some form or the other.
*  So I think it's I will never I don't want to come up with the answer that like dorsal
*  is doing blah, blah, like I think it's just part of a system that is trying to solve a
*  behavior and the answer is going to be here is a model that has elements in it that are
*  corresponding to neurons in the dorsal stream and together they, you know, solve a behavior.
*  Now you can ask the question if I really want to satisfy someone like what is the dorsal
*  stream doing?
*  You can start doing perturbation experiments in the model or in the brain and say like
*  what happens to the behavior if I take out, you know, part of the dorsal stream or part
*  of this and that.
*  And but then I'm mostly worried like what is the answer?
*  Like my answer is going to be like, oh, it takes a 10% hit for video A versus video C.
*  Like I feel like those are the kind of answers that are really going to come out.
*  But people are going to, I mean, I might spin this off as like, oh, but this is about,
*  you know, function X or like it's about something about predictive coding.
*  I can give the answer in that form, but I think at the end of the day is just going
*  to be a big lookup table of like you perturb this part of the dorsal stream, you get X
*  hit on this particular behavior, this particular video.
*  So that's why I feel like my answers need to be in the, you know, in the modeling kind
*  of framework.
*  Yeah.
*  Words.
*  We're limited by our language.
*  It turns out this very special thing that we have language also is very limiting in
*  some respects, I suppose.
*  Yeah.
*  But I think if the models can relate back to the language, I think then some of the,
*  you know, problem or the tension might be relieved a little bit because I think now
*  there so for example, I mean, this is maybe slightly off topic from the dorsal ventral
*  discussion, but like if you look at a model of ventral stream, like you can look at brain
*  score and like say, okay, ResNet 101 or something has some numbers associated, like some scores.
*  I can see why people have a problem with that model and why people say this is not interpretable
*  because like there are parts of the model that are just don't know what it is, like
*  how does it map to the brain?
*  Like I can call it some part as IT or some part, there's thousand different things in
*  between that I have no clue of what they are.
*  And like maybe the model is not performing because of those, you know, computations that
*  are happening in those layers.
*  How do I relate this back to the brain or something?
*  So I feel like that is a real problem and I think it is in our interest to start coming
*  up with commitments to different parts of the model and then falsifying them based on
*  those commitments.
*  If so, like an interpretable model should to me should be like, if I write up, so what
*  is the interpretable thing in neuroscience?
*  Like a paper, like the abstract of the paper is completely should be at least interpretable
*  to anybody.
*  So if a model has components to it that can talk to each part of that abstract, like you
*  know, you have a task, you have a neuron, you say something and if you can basically
*  map your abstract to parts of the of the model and if the model can map onto the parts of
*  the abstract clearly, that I think just gives the model interpretability.
*  I think that level of crosstalk and language I think should exist and I think that language
*  I'm trying to sort of develop myself to even when I'm thinking about modeling and experiments.
*  Well I mean after all that about how we shouldn't assign roles to individual brain areas, you
*  are doing some inactivation experiments, right?
*  So what's going on there?
*  Why are you inactivating individual brain areas?
*  Yeah, so I think that basically try to maybe, so there are a couple of studies that I think
*  I've done recently, one has been already published which is like inactivating ventral
*  atl PFC and looking at core object recognition behavior and also looking at representations
*  in IT when the monkey was doing that task.
*  And the goal was to basically expand or test whether these feedback loops that are existing
*  between these areas, are they actually playing a role in that specific behavior that we are
*  studying because the current models are incomplete and they're not predicting enough so it kind
*  of makes sense that maybe there are other areas and there are other connections that
*  are important.
*  So that is not to say like PFC does X, right?
*  It does everything apparently.
*  Yeah, I'm sure it does a lot of things.
*  It's just like for me to actually ground this problem it was more like what kind of role
*  or what kind of signals do I, at least from the inactivation it was like what kind of
*  signals go missing in IT when I inactivate them, inactivate PFC and what kind of sort
*  of deficits do I see in behavior and then the data again as I was saying is not like
*  oh, you cannot identify objects in an occluded scene or something.
*  It's not an answer like that.
*  It's mostly like here is a big data set.
*  It's not satisfactory to many people.
*  Here is a giant data set.
*  It's clearly like you see there's an average effect PFC, no PFC.
*  Okay, I've shown you this.
*  There's a prediction that is coming out of a model that is like this model is a feed
*  forward model.
*  It might not be doing XYZ and those are the images where these effects are also much more
*  concentrated on so there's a story there.
*  Okay, it's clearly part of a system that is not the feed forward system that is maybe
*  going beyond the current feed forward system but at the end of the day, I think the next
*  step is to build a model that has a unit or module that is called VLPFC and perturbing
*  that should produce the same kind of deficits.
*  This is where I think it's a very hard thing to do.
*  It's actually easier thing for me to like perturbed PFC and get this data and say like
*  okay, this area is involved but then build this model, I think that's going to be really
*  difficult and there are limitations to perturbation data for example.
*  I think this might be relevant to the conversation about perturbation experiments because I think
*  even after this perturbation experiment, I think actually recording in that specific
*  area with the same kind of task and same kind of stimuli might be more constraining for
*  the next generation of models and that is exactly what I'm doing currently but at the
*  same time, I was thinking like what kind of perturbation experiments might be like, you
*  know, may have more benefit for the kind of models that we have right now and that kind
*  of led me to developing, mostly we say developing a lot but it's like basically testing this
*  sort of chemogenetic strategies where you inject a virus in a brain area and in my case,
*  I also implanted a UTA array on top of it so we injected DREDS in V4 that was supposed
*  to be like, you know, silencing or down regulating the activity in V4 and then we implanted UTA.
*  Sorry, can you say what DREDS are because we haven't even, I don't think we've even,
*  I think we've mentioned them on the podcast before but what are DREDS and then I also
*  want to ask you, so you injected and then you, in a separate surgery then you implanted?
*  No, it was done on the same exact surgery.
*  Okay, sorry to interrupt you.
*  No, no problem.
*  So, the basic, I think, idea is that you inject a virus that ends up sort of manifesting as
*  a receptor in a neuron that you can activate or deactivate with various means.
*  It's the same idea with optogenetics, the same idea with chemogenetics.
*  In the optogenetics to sort of activate or, you know, that particular receptor, you need
*  to shine light on that neuron, on that area.
*  For chemogenetics, you need to basically inject a drug into the system.
*  And so, there are some pros and cons of these two different, multiple different things.
*  So, for example, you're kind of like limited in terms of where you might want to inject
*  for opto because, you know, light delivery is tricky because you have to be mainly maybe,
*  you know, restricted to the surface of the brain.
*  Deeper structures might be very difficult to target at scale.
*  Maybe you can target like one or two neurons.
*  In chemogenetics, you can basically inject the virus anywhere you want in the brain and
*  it kind of gets activated through the sort of like injection that you do in the bloodstream.
*  So it basically activates or tries to activate all these receptors that has been, you know,
*  produced.
*  But then there's like temporal limitations.
*  So opto can like go very fast, quick on off.
*  But the dreads are more like musimol in some sense.
*  It's on, the effect is on for some time and they're usually weaker.
*  In my calculation, no, no, no, weaker.
*  That would not be so good.
*  I think it's mostly, so from my estimates, I think it's mostly on for like maybe a couple
*  of hours and so on.
*  So it's like very similar, at least the main time is like musimol.
*  So and what I've been doing is like we have these arrays that you can actually test, you
*  know, you can show the same images over and over again after you have injected the activated
*  drug and you can sort of see how quickly or what is the kind of time course of neurons
*  responding lower or higher.
*  And then you can have behavior on top of it.
*  The monkey is also behaving on different blocks.
*  So you can kind of see like, you know, there are some deficits that are coming up and then
*  the deficits sort of like go away at the end of the day or something.
*  So I think I'm at least thinking of like, how do I take this and like make it useful
*  for models?
*  Like, okay, I can say like a V4 is involved in, you know, object recognition.
*  That's like, I don't know.
*  Not too many people will be interested to listen to this anymore.
*  But if you give me like, okay, brain score has like 1000 models that all have like 0.5
*  correlation for V4 activity.
*  But now I give you some V4 inactivation data and then 900 of them fall off and they cannot
*  really predict the kind of, you know, pattern of deficits that V4 has.
*  That might be an important tool or maybe an important problem.
*  But as you see like here, you need to have a model that has like a brain tissue mapping
*  of V4 and, you know, where are you injecting the virus in the model versus in the actual
*  brain?
*  So, I mean, there are parts of this problem that are still more complicated.
*  But I think this, the chemogenetic strategy, at least for areas like V4, you know where
*  you're injecting.
*  And these are mostly retinotopic areas.
*  So there is some level of, you know, correspondence in the models.
*  And then you have a neural data on that.
*  So you can actually just say like, you know, like, I don't care about like your assumptions
*  just like fit to the neural data.
*  You have V4 neural data with and without activation.
*  You have, you know, your model with and without activation just fit to all the data that you
*  have got and then predict what happens to IT or predict what happens to behavior in
*  the model.
*  And that's how you validate the model.
*  I think that is a very, I think that's a stronger form of using sort of this perturbation experiments
*  Because I think it's not uncommon to see, you know, experiments where someone says,
*  you know, this area I perturbed did nothing happen.
*  And someone said like, no, no, no, you didn't do this, blah, blah, blah.
*  So I think if the answer is yes and no, I think it will just stay there.
*  It has to be sort of falsification of like competing models.
*  And then maybe some data will be more useful than the others.
*  The other, I think, upshot of having something like this is that imagine you have monkeys
*  that are doing these tasks in their home cages.
*  Like we have a lot of monkeys that are trained up and they do these tasks all day in their
*  home cages whenever they want because they have a tablet, they can do these tasks.
*  You can pair this up with that system and you just need one person to just go and inject
*  like something in a monkey.
*  And then basically you have days where you can like, you know, run this with some part
*  of their brain, quote unquote deactivated.
*  And you can multiplex even with the viruses.
*  You can like, you know, target inhibitory neurons, excitatory neurons.
*  You can have different viruses inject in different parts of the brain that have their own corresponding
*  activated drugs.
*  I think there's a lot of kind of interesting data sets that can come out of this approach
*  which should bear on the modeling question.
*  How much of your future, what I want to know is like the vision that you have for your
*  own lab and how much of it is going to be this kind of work and how much of it is going
*  to be modeling and so on?
*  I think a lot of this is going to be this kind of work and like just pushing the boundaries
*  of experimental neuroscience.
*  I think the modeling is like, it's like that's going to be the backbone of the lab.
*  Like the computational part is like no answers can be provided from the lab if there is no
*  model attached to it.
*  So I will be collaborating with others.
*  I'll have people, you know, working with people in the lab who will be building probably
*  these models as well and testing them out.
*  But I think that I don't think I will be happy at the end of my career if like I did
*  not improve like a model or something of the system even after doing all these different
*  experiments.
*  So it's going to be a mix of that.
*  I mean, maybe, I don't know, I should probably mention this.
*  Like I'm not, honestly, I'm not really interested in building the best model for core object
*  recognition or dynamic visual perception or visual cognition.
*  Just for the sake of building that model and understanding how the brain works.
*  I mean, I don't quite motivate myself that way.
*  I think it's kind of, I mean, kind of interesting because like I think for training purposes,
*  these were the most concrete fields and most concrete labs that I thought, okay, this is
*  where I should get trained.
*  But I think I kind of wake up every day to sort of think that maybe my research is going
*  to help someone's life.
*  And I think this is kind of like, oh, wow, what a great person you are.
*  Like, I really, I mean, I think I'm going to like a small story.
*  Maybe this is, please, you can cut it out if it's not relevant.
*  I was, I was, so I have been working in visual neuroscience and people know that I work in
*  visual neuroscience back home in India.
*  And what do you mean people know like the like India knows your family, my family, my
*  family, sorry, people, 1 billion people know now, like five people, 1 billion people know
*  that.
*  More than what I do.
*  So there you go.
*  Yeah.
*  So among those five people, maybe like 10 Indian families tend to be so among those
*  50 people, then there are some of them that I don't, I think they have some idea of like
*  what I might be doing, which is completely wrong.
*  And I think I had this encounter with someone and unfortunately their kid had had got diagnosed
*  to be in the autism spectrum.
*  And so I was meeting them and they asked me like, oh, so what are you working on these
*  days?
*  And I'm like, okay, I'm working on visual cognition.
*  I'm saying stuff like how do we reason and things like that.
*  And this person turns to their kid and tells them that, you know, your elder brother will
*  one day like, you know, is working towards the solutions.
*  The kid is like very young, can't understand anything of what they're saying, but they're
*  basically telling them that like, he is going to come up with the solution that will cure
*  you.
*  And it just felt like I just was feeling like I'm, I was thinking like, I'm failing to do
*  that.
*  I'm failing.
*  I cannot find any connection to like, you know, what this translates to.
*  And that really, I mean, that was kind of a pivotal, like, like a point where I started
*  to think like, I need to find real connections with what I'm doing and how that really impacts
*  or translates, not just this, you know, like the first paragraph of a grant saying like,
*  you know, I'm working dyslexia, like this is relevant to like, blah, blah, really trying
*  to schizophrenia.
*  So like, so really trying to find them.
*  Then I started actually, I mean, that's going to be at least some part of my, my, my future
*  research is like trying to find out how, you know, having these models that are these concrete
*  models with brain maps, how are they beneficial to diagnosis and potentially treatment strategies
*  in some of these neurological disorders?
*  And I've started working a little bit towards these goals.
*  And I'm very excited about this because I think there are real benefits.
*  And I think you were mentioning about this, like, neural control studies.
*  I think those are the kind of studies that are really sort of giving me hope that like,
*  there is a way to like contribute to this, to this part.
*  That's like a, that's kind of a magical thing.
*  So that wasn't your motivator for a long part of your career, but from a place of guilt.
*  It's, but, but it's developed into a great, guilt is a great motivator, but it's developed
*  into like a real motivation for you.
*  But I never had that.
*  I don't care about helping people.
*  And so I always felt bad writing schizophrenia in a grant, for example, right?
*  Yeah, I mean, yeah, I mean, it's a little bit philosophical.
*  Like I don't even know.
*  I care about helping people in some way.
*  Maybe I'm basically thinking I'm trying to help people, but I'm just trying to help myself.
*  Maybe thinking like, well, what if I have Alzheimer's or something in my old age?
*  But like, yeah, but I think currently at least I do feel like that gives me some level of
*  satisfaction to think that there is potentially some link of my research that might be getting
*  help to some book for someone.
*  Yeah, I think I mean, it is interesting to think how through our work, through your work,
*  through people's work, your interests change.
*  And as you develop and as you ask different questions and answer different questions,
*  it's just kind of a magical thing.
*  So that's thanks for telling that story.
*  Yeah, I think that that definitely like impacted me a lot.
*  But I'm also like, I think these are related issues.
*  Like I think like you were asking about understanding and progress and like things like understanding
*  vision and visual cognition.
*  I think the moment we start to like measure our understanding like in the brain score
*  way or something like then I think these answers to like the clinical translation becomes more
*  concrete maybe like, so I think they're very related.
*  It's just for me, it took me a little bit to like figure out and maybe I'm still working
*  on it like to figure out where exactly are the most relevant parts of it.
*  And I think my interaction with a lot of folks who are doing autism research like really
*  helps.
*  For example, I've been in touch with Ralph Errols at Caltech and we are sort of collaborating
*  on a project.
*  I think those discussions and like reading the papers like really, I think they have
*  a lot to contribute to what I do and I think our way of thinking about the system has a
*  lot to contribute to that research.
*  Interesting.
*  So you mentioned the image synthesis work a little bit.
*  Can we talk briefly about that?
*  Because maybe you can just describe what the work is.
*  I talked with Jim about this when he was on the podcast, but we can kind of recap because
*  it was kind of splashy, right?
*  I kind of want to hear your thoughts on how you currently think about that work as well.
*  Yeah, so this work was done in collaboration with Pooja Basivan, who's at McGill now.
*  So me, Pooja and Jim, we did the study together.
*  So the basic idea was that we were recording in V4 and we have models of V4 neuron and
*  the question was that can you from the model come up with stimuli using the model?
*  Can you come up with stimuli that puts the neuron in specific desired states?
*  And one of the states that we considered was like, let's make it fire the most we can.
*  So the model will tell me...
*  So this is the control aspect of understanding.
*  Yeah, exactly.
*  So that is like, you know, prediction and control, and this is the control part.
*  So the models could predict, but maybe they couldn't control because maybe the images
*  that were synthesized...
*  I mean, there's a part where there's a separate technique, which is the how are you synthesizing
*  the images and maybe there are ways in which that doesn't need to be attached to the model.
*  That specific model that you're using to predict, they can be two separate things.
*  But again, for us, it was like, you know, we were using the same model to come up with
*  the images as well.
*  So we came up with the images, we're trying to control the neuron and we were targeting
*  like, okay, V4, let's make this neuron fire as high as possible.
*  That was one of the goals.
*  The other goal was, let's take a bunch of V4 neurons that kind of share the same receptive
*  field properties and try to set one of them to very high and the others to be very low.
*  This is like a population level control.
*  So these were the two goals that at least we thought, let's start here.
*  And then we were asking like, okay, this question seems like, you know, you have heard of this
*  before because like, oh, what does V4 neurons do?
*  Like they respond to curvatures.
*  What does V1 neurons do?
*  Like Gabor's an orientation and V2 is like texture and like IT's faces.
*  Like now you come up with the stimuli and you look at them and like, I don't know what
*  to call them.
*  Like maybe they're something.
*  But then for us, we kind of ignored that problem.
*  We just said like, okay, let's just take these new images and like see whether the model's
*  prediction is right.
*  Because then that at least we should show that like using these models, you can control
*  the neurons to some degree.
*  That was basically the study.
*  We had some success and we were comparing our success rates with like taking a random
*  sample of new images or using the previous sort of thoughts on what are the stimuli space
*  that excites these neurons like curvatures from.
*  I want to hammer this home because the images that drove the neurons were, and you mentioned
*  this, but I just want to reiterate that they were terribly unnatural, right?
*  That's something that you would see.
*  Well, I mean, there are elements that you would see in nature, right?
*  But the majority of them, weren't they just something that you wouldn't make sense of?
*  I don't know what even called them.
*  There's some pixel conglomerations.
*  So there were two studies that came out on the same day.
*  And I think the other images are even more scary.
*  So this work from Carlos Ponzi and Marsha Winston, Gabriel Kreiman, Will Schaub.
*  So they were trying to control IT or they're trying to like, you know, come up with the
*  images for IT.
*  Those images look even more scary.
*  Because they have some kind of natural relevance.
*  They look like out of a horror movie or something.
*  But like the V4 images were more like texturing kind of images.
*  And we are also restricting ourselves to like, you know, black and white images and things
*  like that.
*  So I think that was part of the, it was constrained in certain ways that led to those images.
*  But as you were saying that, yeah, it did get a lot of attention.
*  But I think some folks have gotten excited about the wrong thing from the paper.
*  And the resulting images that drove V4, I think cannot be the protagonist of the story.
*  Because I think that kind of became the story because like we like to say like faces excite
*  IT neurons or XYZ excites XYZ areas.
*  And I think in that formulation, then it became about the images as sort of our new understanding
*  of the system.
*  Whereas that was not about the images.
*  It was about look how, what you can do with this model because this is the model that
*  tells you that what is going to be the predicted neural response for any given image.
*  So I think that's where we are in terms of like, we think of this as a stronger test
*  of the model.
*  Because there are many models then that can come up with different images, then you can
*  test those as well.
*  And I think there's work, very, very interesting work from Nico Krieger-Skott's lab about controversial
*  stimuli.
*  Those are the right kind of approaches, at least to me, like you pit these neural networks
*  against each other and then synthesize stimuli and then test them.
*  It's a different kind of control experiment.
*  But at the end, it's basically about model separation and finding the best model.
*  It's not about looking at those images and making stories about them.
*  The other side of the story though is that this should not make someone feel like, oh,
*  you know, solve, core object recognition, this is the model.
*  Clearly they have, yeah.
*  So yeah, I mean, that's the other thing I feel like, you know, there's ways of presenting
*  data that can prove our point.
*  It's a proof of concept study to me still.
*  It's like, you know, look like if you take this approach versus the other approach, this
*  approach, like our approach is better or something like that's kind of the way to present the
*  study.
*  But that doesn't mean that our approach is like the best approach or like we are done.
*  Do you have people suggesting that we're done?
*  I don't think we have people who would explicitly suggest that we are done, but they might use
*  this as an example of like, look how great the CNNs are.
*  And I think it depends on whom you're talking to, because I can also use the same example
*  to kind of like talk to somebody who's just basically saying, oh, CNNs have adversarial
*  images and this is like a completely wrong domain of like models.
*  I can then use this example to say, look, you can do some useful stuff.
*  But if I'm coming up with things like, you know, you need recurrence and you need other
*  areas to incorporate, someone might go like, but you can control reasonably well, like
*  why do you need to like incorporate all of it?
*  So if you really look into the models, you know, look at the generalization of the models,
*  it's not that good.
*  It's like, again, not that is a very arbitrary word.
*  But you feel like in some sense, you're your own worst critic, right?
*  Because you see all of the nuts and bolts and you see what's missing and what needs
*  to happen.
*  And so do you feel like people are too complimentary or too impressed with the current work?
*  Because I should be.
*  I think they should be.
*  But I think they shouldn't also like everything else.
*  I mean, I actually think this is our responsibility to sort of also expose where the...
*  If you read the two papers together, like the Neural Control paper and the Recurrence
*  paper, they're basically one paper sort of highlighting how you can use them.
*  The other paper is sort of highlighting like here are the images that humans and monkeys
*  are good and the models are failing.
*  So these are the ways to improve it.
*  So I think if you take all of these studies together, then you might get a more balanced
*  perspective.
*  I think my goal, at least, I mean, sometimes for a lot of reasons, I mean, you know better
*  that like you need to sell the studies in a certain way.
*  But I think in these kind of discussions or like in papers, in the discussion sections,
*  like we should always be highlighting sort of the confounds or the potential, you know,
*  places to improve these models.
*  I mean, even for core object recognition, these models fail in very trivial ways that
*  are maybe some people who are just reading this paper might feel like, oh, that's probably
*  already solved.
*  Yeah, maybe they don't exist.
*  Maybe this is a thing that I've created in my head.
*  More guilt, more.
*  Yeah, I know that one of the things that you're interested in is visual reasoning.
*  Right. And you're I don't know if you want to explain why you're interested in it and
*  what it is. But one of the ongoing criticism.
*  So so nonhuman primates is kind of like the gold standard.
*  Right. And neurophysiology.
*  And you need an N of two.
*  You need two monkeys to publish classically.
*  But and recently there have been a lot of people working more and more in rodents and
*  mice. And of course, there's always been the disconnect between mouse brain and human brain.
*  And one of the reasons why people like to study nonhuman primates is because it's like
*  the closest thing that we can study that resembles human brains.
*  Do you see limits to studying nonhuman primates to get at our intelligence?
*  So the reason why I asked you about the visual reasoning is because you're starting to ask.
*  So object recognition is a fairly simple thing.
*  Right. I know it's not simple, but it's a you know, we recognize objects.
*  But now you're starting to ask more cognitive, higher cognitive, quote unquote questions.
*  And I'm wondering if you see limits to using nonhuman primates for that.
*  Yeah, I think the answer will be sort of I mean, my answer to that question would be
*  maybe based on the kind of data that I will be collecting in some sense.
*  So the way I see this problem is that like, you know, ultimately, at least for myself, I'm
*  not suggesting that everybody has this approach, but I'm pretty human centric in my
*  worldview. And I think my goal is to find out how humans solve particular problems.
*  So they are basically like the main model that I'm interested in.
*  So I think we start from human behavior on different tasks.
*  And ideally, we'll have a model which is like currently maybe some form of a convolutional
*  network which has many areas other than ventral stream like dorsal stream, PFC.
*  And they will be kind of like predicting parts of the behavior of the humans and maybe at
*  full capacity or something. And I think at least one angle of approaching the monkey
*  research would be like, can I get some neural data that might be constraining for those
*  models, might improve those models?
*  And usually, I mean, the way people go about it is that they collect some neural data,
*  come up with an inference that is more can be like summarized as like a very smaller kind
*  of principle, like have recurrence or like a smaller model.
*  And then they incorporate that idea into the bigger model and ask, like, did I improve
*  my model, my bigger model?
*  I can do that. I mean, I'm probably going to do a bit of that, basically, like saying, look like
*  it looks like these other areas in the monkey brain is associated with this particular behavior.
*  And maybe that is going to improve my development of the models.
*  The other thing could be like you just directly feed the data that you're collecting into the model
*  building itself. So you're getting a lot of monkey data.
*  Then it's a matter of like questions of like how much data is enough data?
*  And I think we are getting more and more data.
*  So I think this is the right time to like start putting them in the models.
*  So right now, I'm involved in a project where all the data that I've collected is getting kind of
*  filtered into the training part of the model.
*  And the models are being regularized with that data, essentially.
*  So like, and those models are becoming better predictors of core object recognition.
*  So that is one way of bringing in the monkey neural data and the monkey behavior, maybe, to this problem.
*  The other way I think about this is that maybe, you know, humans and monkeys share a very, maybe
*  it's proven in many ways that we share a very similar visual system.
*  So if even if I just get responses of the visual neurons in IT or other areas during showing some of
*  these movies or some of these like, you know, videos on which the task is based off, I can be providing
*  constraining data for the model of like, you know, you need to be in this representational space and then
*  solve a problem. So like, it's a two part kind of approach where the neural data is basically constraining
*  the representational space of the model.
*  And then on top of that, you add a decoding layer that is like reading those representation and you can have
*  multiple ways of decoding the task.
*  And then you ask like, which one, you know, or you can then compare it to human behavior.
*  And I think this could sound novel or surprising, but like, this is exactly the thing that Jim's lab, like
*  our lab has been doing for core object recognition for quite a while where we were recording in monkey brain,
*  but then comparing the decoding models output to human behavior.
*  I have now started working, like because I was also getting the behavioral data from monkeys, I have started now
*  working, looking at trial by trial and like image by image behavioral correspondences with monkey neurons and,
*  you know, human, sorry, monkey behavior.
*  But it was basically monkey neuron human behavior.
*  We had a paper with Rishi Rajalingam looking at monkey neural responses to like words and non words and their
*  correspondence to human behavior on those sort of orthographic processing task.
*  So I think there's a way to like do this kind of separate it from a behavioral task.
*  I think maybe if you're asking that, do we, does the monkey need to do the behavior for them to be relevant to this
*  task? I think the same applies to rodents and other species.
*  It's just to me that the correspond ultimately, again, as I was saying continuously throughout this discussion is that at
*  the end, there is a model and whatever you do, you need to kind of show that that adds to improvement of the model on
*  something.
*  And now I from my just what we're talking about, I can say like, maybe my goal is like not to improve like prediction on
*  human behavior to ceiling.
*  But maybe it's like, if I'm doing maybe predicting behavior of neurotypical subjects versus, you know, people with
*  autism, do I have some traction on that problem?
*  Maybe like I can do, you know, like inhibitory, excited imbalances, I can create them more easily with hemogenetic
*  perturbation in a monkey and then test what those representational spaces are.
*  And those could be like kind of constraining ideas for when you're building models of people with autism.
*  So I think there are many, many ways in which and I'm saying all of these ideas and with the risk of sounding like a
*  scatterbrain person, like has to.
*  But I think at the end of the day, I think these are the things that excite me.
*  So I think I won't be able to solve it all by myself.
*  I am hoping that a lot of people who are kind of maybe similar minded, we all come together and kind of try and tackle
*  this.
*  So co neuro AI.
*  So, you know, a lot of your at least most recent career has been using deep learning models to shed light on brains.
*  And so this is the arrow from AI to neuroscience.
*  Do you see and part of what you're doing also is using brain architecture and neuroscience, some details to improve the
*  models bit by bit like you were discussing.
*  Do you see neuroscience helping AI or does does AI not need neuroscience?
*  Can I just scale up and go to AGI or what?
*  That's a interesting question.
*  And also, I think I'm probably not the my answer might not be that satisfactory just because of my lack of knowledge in a
*  lot of these domains.
*  But I think I think of this problem in different ways.
*  So like, if I think of this as like, OK, I'm going to build a calculator and should I constrain myself with the brain data?
*  No, it's going to be like a terrible calculator for scientific computing or something.
*  So like, if that's the goal of an intelligence system is like to compute, you know, calculate things fast and like then I
*  think constraining it with neuroscientific ideas and data is like a bad idea.
*  Now, if maybe we can make a distinction of like behavioral data and actual neural data.
*  So if I want to prioritize in my head, like which data might be more informative to building models in for AI, I think
*  behavioral data will come first before neural data.
*  Some of the examples might be like moral machines kind of data that is part of the MIT Media Lab.
*  I think if we are trying to constrain a system to work like humans, then human behavioral data, I think will be key to
*  constrain this.
*  I mean, that's kind of been the success of deep learning, right?
*  Is because the old way in neuroscience was to build a model out of kind of intuition and then compare it to data.
*  And the new deep learning approach is to build a model and train it to optimize it for a task like an animal or organism would
*  perform.
*  And so it's all about behavior.
*  And lo and behold, the model predicts neural data well also.
*  Right.
*  Yeah, yeah, definitely.
*  But I mean, I was maybe making a slight distinction between like overall performance in a behavior versus like following the
*  pattern of human behavior and the error pattern.
*  So like, imagine trained models are trying to get the labels correct, which is a behavior.
*  But like, humans might not always get those labels correct.
*  And like they might have different patterns.
*  So I think I was mostly thinking like this error pattern of like, what kind of decision do we make given some kind of confusing
*  stimuli or things like that?
*  Those kind of data might be more relevant to models if they want to sort of operate in a human regime, because I'm thinking of
*  like a system that might be like, you know, helping somebody go through life who are unable to do things in their life.
*  That machine or robot has to interact with the person.
*  And then it's I think might be important for that system to be constrained with human behavior to some degree.
*  For those purposes, I think behavioral data is very valuable.
*  At least that's how I think about it.
*  For example, also AI in health care might be something that is might be very constrained.
*  And there, I think maybe the neural data might have some bearing on that.
*  I mean, it still has to be shown, I think.
*  I mean, but I feel like there might be some.
*  I mean, as I was saying that this idea of like, you know, how does the brain differ in a neurotypical subject versus atypical subject?
*  That kind like it just depends on the scale of the data and how we are getting it.
*  And that's the relationship of the brain representation to behavior.
*  I think those kind of data might help us to build better models of the atypical systems and then use solutions that might be catered to the atypical system.
*  I mean, now I'm kind of being very abstract with me.
*  I mean, I can come up with like a dream sort of example where if you know exactly how like a system is learning, for example, a new task,
*  and you can do that for both atypical and neurotypical populations, you might be able to use the atypical model to kind of come up with a learning sequence that produces neurotypical behavior, even though it's atypical system.
*  So I think that kind of that is definitely within, I think, the the genre of like AI health care kind of like approaches.
*  So I think that way, neuro to AI links probably are more clear to me.
*  I think generative models might have a boost if they're regularized with neural system data.
*  That is another maybe angle.
*  But yeah, but but it's it's so I would just not.
*  What I'm mostly worried is that it's not like it doesn't obvious that if you have some brain inspiration or like neural data is going to improve AI models.
*  That's that's what I'm kind of pushing back against.
*  It's like maybe you can get behavioral data and that's enough and you don't need to poke around.
*  But isn't it interesting that these deep learning neural networks are based on 70, 80 year old neuroscience, like fundamentally the idea of a neural network back with even the logical units?
*  I mean, so and you're adding more biological constraints to your models.
*  So it's an interesting.
*  That's true. I mean, I'm thinking of that.
*  Like, so the first part, I agree that that's like, you know, that that's where all of these ideas might have come up.
*  And that's a good reason to keep looking at neuroscience for inspiration for building better models.
*  But if I look at the last 10 years, I really don't see a concrete example of like you read paper in Nature Neuroscience, General Neuroscience and took that idea and implemented in a model that drop out by.
*  At the end, they're like engineering hacks.
*  Like, I mean, both groups like to use it as PR, which is, I think, the reason why.
*  So it's great for that purpose.
*  But I think in reality, at the end, you can have an idea.
*  I mean, I mean, that's fine to me.
*  Like, even if you have an idea of a drop out and then you figure out how to really like tweak it to make it part of a model that does something, that's great.
*  And I think in that way, it's really good to have neuroscience as a inspirational kind of umbrella on top of everything.
*  Good for my career.
*  And I'll be able to talk to them.
*  But I think I definitely think there is purpose of I mean, yeah, there will be use of neuroscience for AI.
*  But we need to be careful to not oversell it, maybe.
*  Maybe we should. I don't know.
*  But I think the other way around for me makes more to me, it's more valuable, especially because I think, you know, you're trying to measure data in the brain that is noisy.
*  This is like sample limited and then build theories and models around that, like what to expect, like how to think about high dimensional spaces, blah, blah.
*  So like to me, like once you have a model that is doing a very, you know, high level behavior and very accurately, that complex system gives us the opportunity to like really figure out how to even analyze a complex system.
*  So to me, that's a huge bonus from these networks, because neuroscientists, I think, have been trying to do both things at the same time, like build the complex system and then figure out how to analyze the complex system.
*  And here are networks that are already built up and you can formulate like different theories.
*  And I think to me, that's like a huge advantage of having these networks.
*  And they really become like the starting points and the maybe base hypothesis for a lot of these neuroscientific experiments.
*  So that's kind of like, and this is how I have been mostly getting excited about the crosstalk between the two fields.
*  We talked about how there's this kind of archaic fallacy, I suppose, for, you know, naming a brain region, giving it a role, right?
*  And the modularity of the brain, prefrontal cortex does X, that sort of thing.
*  And we've talked about, well, I guess I mentioned about how language actually limits us in some sense.
*  Do you feel like we understand what intelligence is?
*  Do we have the right notion of what intelligence even is to start trying to, you know, to continue trying to build, quote unquote, AI?
*  I don't know which scientist we're thinking of.
*  Like, I think for me, I probably don't have a complete understanding of what intelligence is,
*  but I have a fair enough understanding of what kind of intelligent behavior I would like to build models for.
*  And so that's where I'm just kind of the engineering, engineering me maybe like talking because I know what problem I have defined.
*  I won't know the solution.
*  So like this kind of tasks that are slightly above, you know, recognizing an object and like trying to figure out like what different agents are doing in an environment or like trying to predict what might happen next.
*  Like these kind of behaviors, I think, are fairly intelligent behaviors.
*  And my goal is to build models and try to figure out how the brain is actually trying to solve that problem.
*  So in that way, I'm fairly happy about the definitions of intelligence.
*  But then again, we'll get into trouble.
*  Like I'll get in trouble saying what is intelligence?
*  Maybe like the typical like IT, you know, scores or IQ, IQ scores.
*  I think they're heavily debated.
*  And so I just feel like what I want to say is that we can keep debating about what is the right score, what is the right way of quantifying intelligence.
*  But we have to do it in some way if we want to have any measurable progress.
*  So I have defined it in some way and I will keep, you know, improving that definition and, you know, expanding on that definition.
*  But but I think intelligent behaviors are to me not that controversial.
*  Anything that I can do that my three year old son cannot do almost seems like a definition of like a little bit more intelligent, but he might be learning faster than me.
*  So at this stage, like the kind of definitions like that, maybe that exists.
*  But like, yeah, you have a three year old.
*  I do have a three year old.
*  Is that the only child?
*  Yeah, yeah, he's our only child.
*  Oh, man, that's that's kind of a hard patch going through and starting a new job and all that.
*  So I feel sorry for you.
*  I mean, it's a wonderful thing, obviously.
*  But, you know, it's challenging early on.
*  So yeah, yeah, it's yeah.
*  Yeah, yeah, yeah.
*  Yep.
*  Corey, are you go ahead.
*  I must say, like, it's I'm happier on average, like, like after taking into consideration everything around the child, I think overall I'm happier that we have a son.
*  That's the most I will say about this.
*  OK, it's like a P like P equal to point zero four.
*  Yeah, right.
*  I used to draw this a pie chart where that I would show people like, you know, do you like having kids?
*  And it's like 51 percent.
*  Yes. Right. Forty nine.
*  No. Yeah. All right.
*  Maybe I'll cut this because I sound like a real jerk.
*  Are you are you hiring in the lab?
*  Are you looking for students?
*  What's what's the situation?
*  Yeah, I'm definitely looking for postdocs and grad students to work together in my lab.
*  So I think if folks are interested, I mean, the grad students are they're basically going to be recruited through York's graduate program.
*  Yeah. And the postdoctoral candidates, I think I'm like just going to talk to them individually and then see where the sort of, you know, alignments lie.
*  And yeah, definitely.
*  So if folks are interested in whatever we spoke about and maybe they read some of the papers and think the interesting direction that they might want to pursue, I'm definitely interested in talking.
*  He's the future of neuro AI folks.
*  It's a this has been a lot of fun, Co.
*  Congratulations again on the job.
*  And gosh, I'm just excited for you.
*  It sounds like you have a lot to pursue and things are looking up.
*  Not not that they're ever looking down, but congrats.
*  Yeah. Thanks, Paul.
*  I mean, I mean, there has been a lot of promises made.
*  I feel like I'm kind of like making a lot of promise and I hope I'm able to deliver.
*  I feel like as long as I can quantify what those promises are, I can tell you in maybe a year where I have been how much I have, you know,
*  Oh, we'll check in in a year.
*  We'll check in.
*  We should check in. But yeah, but I'm excited.
*  I think I think this is worth doing.
*  So so I feel like I'm all excited to get on with it.
*  That's been great, Co. Thank you.
*  Yeah. Thank you so much.
*  Brain Inspired is a production of me and you.
*  I don't do advertisements.
*  You can support the show through Patreon for a trifling amount and get access to the full versions of all the episodes,
*  plus bonus episodes that focus more on the cultural side, but still have science.
*  Go to braininspired.co and find the red Patreon button there.
*  To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year.
*  Find them at thenewyear.net.
*  Thank you for your support.
*  See you next time.
*  The cover of a boundless blank page
*  Led me into the snow
*  The covers of the past
*  Would they take me where I'd go?
*  You

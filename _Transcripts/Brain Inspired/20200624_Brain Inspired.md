---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4564s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 3828
Video Rating: None
---

# BI 075 Jim DiCarlo: Reverse Engineering Vision
**Brain Inspired:** [June 24, 2020](https://www.youtube.com/watch?v=H7LzjJ2J7qw)
*  Science is about finding models that explain a lot but have the minimal needs in them to
*  explain the maximal amount of stuff, right?
*  But that's an art.
*  It's not really a science yet.
*  I mean, I don't think it ever is.
*  You're just guessing at the next model.
*  I don't have dreams of there's some great, simple differential equation that the whole
*  brain is going to follow and that's the answer, like Maxwell's equations.
*  I've heard some physicists tell me that's what our answers of the brain should look
*  like and I find that almost, you know, that's almost, you know, I can't imagine how that
*  could ever, someone could think that's how you should think about a system like the brain.
*  It might be, if it was true, we'd love to know it, but if we all sort of said we get
*  into neuroscience because that's our hope, then I think a lot of us are going to be disappointed.
*  My bet would be against that.
*  This is Brain Inspired.
*  Hello, everyone.
*  It's Paul.
*  Today, I'm happy to bring the voice and thoughts of Jim DiCarlo to you.
*  Among other things, Jim is the head of the Department of Brain and Cognitive Sciences
*  at MIT.
*  We've spent a good amount of time on this podcast talking about the work coming out
*  of his lab, which is right at the interface of AI and neuroscience.
*  His goal is to reverse engineer visual intelligence, and the focus has been modeling the ventral
*  visual stream, that hierarchical cascade of brain areas that's thought to underlie our
*  ability to recognize objects.
*  And he does this using deep learning models, although as you'll hear, he's careful to
*  distinguish his models from what's commonly thought of as deep learning.
*  For example, he doesn't think that his models prove that backpropagation happens in brains.
*  Backpropagation is just one solution for optimizing synaptic weights, and brains could
*  use a different solution.
*  If you've been listening since I started the podcast, you'll remember that I had
*  Dan Yeamans on way back then.
*  Dan was a postdoc in Jim's lab, and Jim gives basically all the credit to his lab
*  members for producing great work.
*  More recently, Nicole Rust was on the podcast, and she was also a postdoc in Jim's lab.
*  So it was good to finally have Jim on the podcast.
*  We discussed some of his recent work, adding recurrence to his previously feedforward models
*  of the ventral visual stream.
*  We also talked about his work using the models to create images that, when viewed by a subject,
*  can control the neural activity of specific neurons and populations of neurons.
*  So a way to stimulate neurons just by showing someone an image.
*  We also discussed his notion of what understanding is and how it differs from other notions of
*  understanding.
*  And there's plenty more beyond those topics.
*  I of course link to the papers that contain the research that we discuss.
*  You can find those at the show notes at braininspired.co slash podcast slash seventy five.
*  If you value this podcast and you want to support it and hear the full versions of all
*  the episodes and occasional separate bonus episodes, you can do that for next to nothing
*  through Patreon.
*  Go to braininspired.co and click the red Patreon button there.
*  All right.
*  Thanks for listening and enjoy the mind of Jim DiCarlo.
*  Jim, we've talked about you a lot.
*  Talked about your lab a lot, at least on the show.
*  So it's good to have you on.
*  Thanks for being here.
*  Thank you for having me, Paul.
*  So I'm going to get right into it in the interest of time.
*  You frame your work as reverse engineering visual intelligence.
*  What does that mean?
*  And maybe you can say a little bit about what that means without focusing specifically on
*  what your lab does in particular.
*  Yeah.
*  When I say that phrase, what it means to me is what we're seeking something that's going
*  to be a description of brain function at engineering level terms, which means that we should be
*  able to build something similar to it in terms of both internal and external function.
*  And I often think from a science point of view, it means forward engineering under the
*  constraints of the data of natural science.
*  And so that's how it actually operationalizes.
*  It's just do good engineering, but with guidance from the data, because the data aren't going
*  to tell you what to actually forward engineer.
*  They're just going to give you guardrails on doing that.
*  And I refer to that overall approach as reverse engineering.
*  So the reverse part is the actual biological data.
*  That's exactly right.
*  Otherwise, it's forward engineering could just be on its own.
*  But now we have some guardrails.
*  And so then we give it a new term.
*  Maybe it could be called forward engineering with natural science guardrails.
*  That doesn't sound as punchy as.
*  Yeah, exactly.
*  Right.
*  OK, great.
*  So your lab has really embraced deep learning as models of brain processing, specifically
*  core object recognition in the ventral visual stream.
*  And one of the main goals of your lab is to solve core object recognition.
*  So I'm going to do a quick and dirty summary of the past decade or so of your work that
*  will hopefully bring us up to the last couple of years in your lab.
*  And then you can correct my story as much as you'd like.
*  And then we'll go from there with the current projects and state of things going on.
*  Before I do that, though, I use this phrase core object recognition.
*  So for clarity, would you mind just describing what core object recognition is?
*  Well, that was a way of just describing how we've operationalized the problem to study
*  so far, which is vision in the central field, the central 10 degrees, which is about two
*  hands at arm's length, what you see in your center of gaze.
*  And for just the duration of time, which is about the time of a natural viewing duration,
*  which is just 200 milliseconds of a second, sort of a blink of an eye, almost literally.
*  And that's just to reduce the spatial challenge of the problem and the temporal challenge
*  of the problem.
*  And so and then I decided to call it core recognition.
*  So we had some word to refer to, but it's really just an operationalizing the problem
*  so that it's not all a vision, which is too hard to do all at once.
*  Too hard to swap.
*  Too hard to swallow visual intelligence whole.
*  Right. So, yeah.
*  Yes. And core core sounds a little more interesting than step one point, which is another way
*  to do it. Core sounds important.
*  Yeah. Right. Yeah.
*  That's a bit of branding, I guess I'd say.
*  I think you're pretty good at branding.
*  Yeah. Yeah. OK.
*  So, OK. You worked a long time with models that map onto the ventral visual stream, that
*  ventral visual hierarchy in brains.
*  And you've been doing this a long time in non-human primates that have been performing
*  what you call this core object recognition task, where you show these flash, these pretty
*  quick objects and the non-human primate or monkey has to identify the objects, essentially.
*  And while you've done this, while the monkey's performing this task, you've been recording
*  neurons and that the number of neurons that you've recorded has grown and grown and grown
*  the number of neurons that you simultaneously have recorded until these days.
*  I think you're putting like three Utah probes in and recording over a thousand units at
*  a time, essentially on average.
*  Right. And these models that you had been working with were deep in the sense that they
*  had multiple layers, but they weren't deep in the sense of deep learning as it's known
*  today. And we'll get into that.
*  But often the parameters of the models would be hand engineered using known constraints
*  from the physiological recordings.
*  This was painstaking work that made improvements.
*  They may have been somewhat marginal improvements, but there was this steady march of improvement
*  until there was a breakthrough in 2012 around that time when you started asking the network
*  like the monkey to actually perform the task.
*  And you ended up with a set of models and one model in particular called HMO model really
*  blew away the previous model's performance to account for the neural activity.
*  But you still weren't treating these models using back propagation, which is what all
*  deep learning models have used these days.
*  You found, if I'm not mistaken, you found the parameters by this sort of massive search
*  process over the space of possible parameters.
*  But still, the model was performing the task, but you would search the parameters over this
*  massive space of search parameters.
*  And so you had this really great performing model and that was very satisfying.
*  And then AlexNet came along, which is a convolutional neural network model.
*  I guess that was 2012 too.
*  Yes, it was definitely 2012.
*  And that was like a breakthrough in on the AI side in the computer vision world.
*  And you guys eventually tested your text, tested AlexNet with your neurophysiological
*  data and found that that even performed better than the HMO model.
*  And since then, you've been using convolutional neural networks and tweaking them to model
*  both human and non-human ventral stream processing with great success.
*  That was quick and dirty.
*  So I apologize, but that takes us to just a couple of years ago, I believe.
*  And I'll ask about this past sort of era a little bit more later.
*  But what did I miss that you would say that's important?
*  Well, I think you summarized some of the things that we're most well known for in this
*  space. Of course, there was sort of a couple of decades of work before that on more basic
*  neuroscience that I could tell you about that those stories as well.
*  But you hit some of the recent highlights, say, between, you know, we've always been
*  building models, but, you know, they really, you know, it was really getting serious in
*  the lab in the late 2000s and starting to run models on GPUs and first doing that.
*  Those were the fun days of just trying to start to do the things which are now commonplace.
*  But then, yeah, the breakthroughs happened in the early 2000s, 2010s or so, 2012, 13, 14.
*  And exactly the way you described.
*  And there's important things we need to talk about there, like deep learning versus deep
*  models, why HMO versus other models.
*  And I think we could love to get into those distinction with you, because I think they're
*  interesting and important.
*  And in some ways, it's our work has been sometimes miscast in those terms.
*  I think we should kind of discuss that.
*  Let's do it now. If that if it seems like a natural time to do it.
*  Yeah. So I see.
*  Probably you said, you know, you guys are known for deep learning and sometimes just to be
*  frank, it's a podcast.
*  I actually don't I don't easily say, oh, forget it.
*  That's not what we do. But because there's a big wave of deep learning and it's, of course,
*  nice to be associated with deep learning.
*  But just to be clear, you said I would say we're more associated with just high performing
*  deep models. So deep learning is just a way to update the parameters of architecture
*  to do well. It's a technique.
*  Right. And that and the part that's interesting to us is not so much the learning part,
*  which we view as not really biological.
*  Sure. People who like deep learning point to our work and say, oh, this is evidence that
*  deep learning is running in the brain. And I often correct them and say, no, no, this is
*  just evidence that a process of performing high performance in these kind of architectures
*  for these kind of tasks is what's running in the brain, whether evolution got there in a
*  different way or postnatal development or evolution is not.
*  It's not a statement about back prop.
*  It's about performance optimization is in both cases.
*  So I view it as a convergent evolution, not necessarily a copy of that, not the exact
*  process that's running in the brain.
*  And I think that's an open, important question, if that makes sense.
*  Well, how important how important do you think it is to distinguish between specifically
*  back propagation?
*  I mean, there is this real push right now to sort of force back prop on the brain and
*  figure out how it has to happen.
*  How must it happen? And even if you're even if it's not happening in your models, it must
*  happen. So we have to figure it out.
*  I mean, is back propagation sort of the key feature that that stands out in your mind
*  that separates modern deep learning from what you associate your work with, perhaps?
*  So, again, I would say our work, I would like it.
*  I do not like our work being associated as this is this is back prop.
*  This is evidence of back prop.
*  Yeah, we're just I would associate our work as we have tried to help guide the field
*  towards these are the current best models of visual processing in the brain and how
*  you get to those models.
*  Back prop is one way to get to them.
*  But there are other ways to get to them.
*  And those may be the ways that the brain gets to them.
*  But we we converge, so to speak, on that they're good approximations of what's
*  actually going on in the neural hardware.
*  So the distinction is more of the one on the building of the system, not the execution
*  or the inference running of the system where where I yes, I agree, these models are
*  the leading model.
*  So, you know, depending if I'm talking to machine learning folks, I needed to remind
*  them of this distinction.
*  If I'm talking to neuroscientists, I first have to convince them that these kind of
*  models at all are the best models because they would prefer different styles of
*  models. So so those two communities kind of have different, you know, we're sort of
*  I'm always trying to be a moderate in most of these things, like how you know, there's
*  different issues depending where you come from on how you think of these things with
*  respect to the brain.
*  But it's how you I don't even the folks that pursue back prop as a model of the brain,
*  they say, oh, there must be something like this running.
*  That's just because they think it's a very efficient learning algorithm, which is true.
*  But it doesn't mean that the brain, you know, is optimal in all senses.
*  And so it's it doesn't have to be the case.
*  And they're even relaxing now and talking about ideas of producing things that are
*  back prop like without actually being strictly back prop.
*  Right. And, you know, if you think about it that way, all of science is is back is then
*  back prop. It's like you're optimizing against something.
*  It's all optimization. Right.
*  And evolution is back prop under those kind of.
*  So sort of, you know, unless we're going to stick to details and you're going to take
*  this derivative and compute this exact error gradient here, then I think it becomes very
*  loose to say it's just optimization and everything technically is optimization.
*  Well, I mean, these are semantic issues as well, because let's say that there's a, you
*  know, a something that is somewhat similar to back propagation like you were just
*  describing. But that doesn't, you know, take the asymmetric reverse gradients on the
*  weights to to improve the model.
*  The deep learning crowd and we don't need to get into, you know, the politics of it all.
*  But they'll perhaps want to argue, ah, see, it is deep learning.
*  The brain does deep learning.
*  But, you know, so is back propagation as it's done in modern deep learning?
*  Does that is deep learning defined by that kind of back propagation or does it encompass
*  any kind of back propagation?
*  And, you know, eventually we're going to just start talking about optimization in
*  general. Right.
*  Exactly. So I think we're saying the same thing.
*  I mean, I think if you know the way to succeed in careers like science, if you can
*  capture a field which is non falsifiable, then yes, you will never be wrong.
*  But, you know, I push my own students on this.
*  It's like we're not saying we have, you know, if you just say you have the brain is
*  by some product of optimization, it's like we don't need to do any more work.
*  We can just declare evolution and it's true and and go home.
*  But we want to know exactly which model is running, exactly how does it get to be
*  there. And now you have to make stronger commitments.
*  If you're a scientist to say, my hypothesis is there's an error gradient computed.
*  This is where it's computed. This is how it's computed.
*  And those are those are more testable versions of deep learning.
*  But if you say, yes, probably it's all deep learning, then it's all evolution, too.
*  Right. So I think there's slippage on those semantics right now going on.
*  And that's maybe some politics, as you say, but also, you know, the science part
*  would be let's carve these things up into alternative views and then see which one
*  is true. And I think the question for the brain is still unclear.
*  That's I guess that's why we don't know which is running yet, whether it's the
*  strict form or the less strict form.
*  But probably some form of optimization is running.
*  Of course, that's the solution.
*  Yeah, exactly. Yeah.
*  For most of us, anyway. Right.
*  Going back to you mentioned, you know, HMO specifically, and I think you wanted to
*  highlight some differences.
*  I don't know if it was just back propagation, but maybe some differences between HMO
*  because there was, you know, the current convolutional neural networks were being
*  developed sort of in parallel in a separate world, maybe with a little bit of
*  crosstalk. But did you want to highlight some other differences?
*  Well, yeah, so HMO was a convolutional network, but its optimization was not on
*  the weight parameters.
*  It was just on the architectural parameters.
*  So it was sort of a early precursor of architectural search strategies.
*  And so all the weights were essentially random.
*  Right. So, you know, that's why it didn't perform quite as well as a back prop
*  optimized network. But it already got us sort of a long way into explaining the
*  brain data that we had.
*  And that's why I kind of am careful to point out all seems to be about so far,
*  it's about performance of the network, not how you get to the performance like
*  that. And HMO was one way to get high performance.
*  And it wasn't quite as high performing as a back prop.
*  We found a slightly higher performing one, and it also matched the brain better.
*  So to us, the main signal is the one of the performance of the task, not the
*  method by which you get to that performance.
*  At some point, at some point, our data will hopefully reveal that those those
*  differences can be fleshed out with the data.
*  But right now, I can't we don't know that.
*  It's I mean, it's interesting.
*  You've made the point previously that, you know, since the really good performing
*  model like AlexNet and that little era that performed well and accounted also
*  pretty well for behavior for the neurophysiological data.
*  You know, since then, of course, the AI world has been making deeper and deeper,
*  bigger convolutional neural network, bigger models, and those don't account at
*  all. The account for brain activity has really gone by the wayside in those, you
*  know, latest models, whereas you guys are continuing to focus on accounting for the
*  neurophysiological data and the performance.
*  And it's not that they've gotten worse.
*  They just haven't gotten much better than AlexNet.
*  They've gotten a little bit better.
*  And they've gotten better on some of the behavioral measures.
*  But this gets into the details of all the various measures.
*  When we say it's better, it's many measures, the internals, in many ways you
*  can look at it. So they've gotten better on some things and not so much on other
*  things. But but you're right, it's sort of tapped out a little bit.
*  The performance is now driving to computer vision and it's not necessarily leading
*  to further gains on the matching to the brain.
*  Which you wouldn't expect because the goal is not to match brain.
*  The goal is to perform a task, perform the computer vision task.
*  The goal of the people building those models is to do it.
*  The goal of our lab is to build models that are going to better match the brain.
*  So you're right. I'd ideally like to do both.
*  But yes, the goals may diverge a bit the last five years or so.
*  Yeah. So how do you think that brings us up to speed here?
*  I mean, you want to talk about some current things going on in your lab?
*  Sure. I'd love to tell you about things going on now.
*  Yeah. Speaking of the goal of, you know, matching brain data, one of the things,
*  one of the recent trends in your lab is adding recurrence to these networks that
*  you've been building. So, you know, up to this point, up to a couple of years ago,
*  all of the networks were still feed forward, which, you know, makes sense that
*  have, you know, on a feed forward sweep through the visual system, it can core
*  object recognition, as we know, can happen very fast, you know, 200 milliseconds or
*  so. And it takes time for a feed forward sweep to happen through the
*  ventral visual stream.
*  But you guys have been adding recurrence to your network.
*  So why add recurrence, which is a softball question, I suppose.
*  And what, you know, what does recurrence do in your hands?
*  Well, I think, you know, the why I think recurrence is there's many ways to answer
*  that. Some people would say you should just have recurrence because the brain has
*  recurrence. And I'd say, well, that's, of course, an argument, but the brain also
*  has, you know, ion channels and glial cells and all kinds of other things that
*  are not yet in the model. So we want to be, want to choose the things that are
*  most likely to, to produce gains on the functional measures, as we call them, the
*  behavior of the spike. So, so this is recurrence is an architectural change
*  that is, of course, present in the brain, but as you point out, not present in most
*  of those initial models and likely to lead to functional changes in the
*  response of the network. One example is just simple one of like the neurons in the
*  brain have time dynamics, they don't just show an image and they step up to a new
*  value, they have some dynamics to them. So you need some form of recurrence or
*  time dependence to make that interesting, or to even compare to the brain. So again,
*  that's another argument that the functional data is something that can't be
*  explained without a more complicated model. But, but I think those are reasons
*  that I think are sort of more obvious. I think the more the more interesting thing
*  to us is that we were noticing that the networks were getting deeper and deeper,
*  they're getting more and more feed forward. And of course, you can take any,
*  you can take a recurrent network and unroll it into a very deep feed forward
*  network and adding a bunch of skip connections, you just redraw the, you
*  know, what's a neuron up, you know, the neurons don't have one to one mapping
*  with the brain anymore. But you could imagine taking the brain's recurrent
*  network and redrawing it as another sort of feed forward with a bunch of skip
*  connections network. So the point is, at an algorithmic level, these are almost
*  like they're equivalent, right? So what's, but when you're doing neuroscience,
*  you're actually at the hardware level, you're those aren't equivalent, you
*  have defined mappings of, you know, in the feed forward version, something
*  that's one neuron is actually like, well, now multiple neurons in that unrolled
*  system, right? Cut multiple copies. Yeah.
*  is now rolled out into space, right? So you have like multiple copies of that
*  sort of neuron or very points of that neuron in time, right? So, so this is
*  showing that you might end up if you don't follow the, if you don't put
*  recurrence, you might start diverging again, if you want to model the actual
*  brain, you could still get good algorithmic performance with those deep
*  networks, but you won't get good matches to the brain if the brain is in a more
*  recurring mode. And this leads us to the question of why you might start asking,
*  why do we want to even match the brain? This comes down to two different goals.
*  If we just want performance, maybe it's, you know, deep four networks are fine.
*  But if you want to match the brain, then you need to, you can't just keep going
*  down that road forever. And again, we noticed that the networks were getting
*  longer and longer, deeper and deeper. And we noticed that, you know, the later
*  time points of the neural responses, and we had a paper on this a few years ago,
*  the later responses that it the dynamic, the later responses tended to match the
*  deeper layers of those networks, which was kind of a signal that, yeah, this
*  looks like an unrolled version of what we're seeing in the brain again. So, so
*  these are all the those are sort of some sort of, I guess I'd say, data driven,
*  but also, I guess, goal driven to figure out the brain questions of why we went
*  to the current models.
*  Is that so, like you said, there's a host of biological, you know,
*  we more realistic details that you could add in.
*  I mean, recurrence is some in some sense, the most obvious to do.
*  I mean, you know, you wouldn't want to just add metabolism into the units,
*  for instance. I mean, that's also just a more difficult project.
*  So recurrence is also more tractable, is it not, to add in more tractable than,
*  say, ion channels or?
*  Sure. Yeah. Make them all.
*  That's going to actually. Yeah.
*  Right. Well, I think you're that's your thing.
*  And the way I think about it, too, is you start with the things that seem like
*  what's going to it's like it's engineering, you know, approximation.
*  So, you know, the first thing we did was build a feedforward model.
*  We wouldn't start with a feedback model.
*  How could that make sense? I can't process an image.
*  So you start with a dumb model first.
*  You push it till it doesn't work.
*  And then you add the next thing that's going to add you think is going to add
*  value. And I don't know if recurrence is the next best thing.
*  It seemed like, as you said, the most obvious next thing.
*  And then there's various forms of recurrence within area, cross area.
*  And then that becomes more subtle interesting.
*  And and and then we'd say, well, at some point, maybe we've got to add spikes.
*  And, you know, there's there's many things that are missing.
*  But, you know, what order and sort of which orders do we have intuition
*  to choose to add them in there?
*  I think I've just admit that's just art and guessing.
*  Nobody really knows the answer.
*  They have their own preferences, their own beliefs.
*  And we have our own guesses, too.
*  And it's really a matter of kind of what's doable at the moment in time
*  and what data you're going to have to help guide you is the other thing
*  you have to think about as you as you try to improve the models.
*  We improve when I say improve.
*  I mean, to make them more brain like more brain like that.
*  That's something we should return to.
*  It's like there's different senses of improve that are
*  our fields between ML, AI and neuroscience are not always doing the same same thing.
*  For the purposes of our conversation, let's just always assume that that's
*  what we mean by improve is more brain like.
*  But let me so now I just want to interrupt because I want to make sure
*  I ask you this question.
*  I mean, you mentioned adding spikes and eventually or something.
*  I mean, really, do we really need to add spikes?
*  Is that something that's going to make a difference?
*  Is there something special about action potentials?
*  Look, I think that's pretty low on my list at the moment.
*  But again, I'm going to say that's a guess.
*  And my guess is going to have a lot to do with energy,
*  energetics and I'll just take that, too.
*  It could also the noise properties of spikes may end up, you know,
*  making the system more naturally robust in some ways.
*  So there there are other reasons to think that spikes are important,
*  but it is a fine line, as you said, like, well, we could model it down
*  to the exact copy.
*  And that feels, you know, science is about finding models that explain a lot,
*  but have the minimal needs in them to explain the maximal amount of stuff.
*  Right. So so but that's an art.
*  It's not really a science yet.
*  I mean, I don't think it ever is.
*  You're just guessing at the next model.
*  Well, you made a good guess with the recurrence.
*  And I mean, maybe one of the things that you found,
*  you're just talking about how the the forward feed forward networks
*  are getting deeper and deeper.
*  And what you have found, I can just summarize quickly, is that
*  there are images that take longer to identify
*  objects, images of objects that take longer to identify.
*  And when you add recurrence to the network,
*  what you find is that that later processing around the time that it takes to
*  to identify these objects with the recurrence actually matches the brain data
*  better. And that that's sort of the main finding right from the recurrent addition.
*  That's right. But then as details of how the recurrence is implemented
*  and how much the brain, you know, there's still lots of ways to implement that,
*  as I said earlier.
*  And the data only, you know, they're only explaining some fraction of the data.
*  So there's still sort of, you know, residual variance in the data,
*  as we call it, that's not captured, which means basically we don't have
*  the right model yet.
*  We have models that are better, again, in the brain matching sense,
*  but they're not not perfect.
*  And I want to point out something you said about core recognition.
*  Remember, we said this is 200 milliseconds.
*  And oh, it's you know, this motivated it's in a glimpse.
*  But what's interesting now is even in that 200 milliseconds,
*  everything you just said about some images take longer.
*  That's all still happening within that within 200 seconds.
*  So we're talking about recurrence that is not the kind where you kind of
*  kind of overtly think, oh, I now see something that I think about it,
*  I move my eyes or my head, long timescale, seconds timescale.
*  This is all sort of subconscious, sort of sub sub mill sub second
*  recurrence structure that that we're talking about here.
*  So even in core recognition, which we thought was a simpler problem,
*  there's complexities around time that sort of make it even still
*  a very rich problem in that regard.
*  You don't have to go to more than even 200 milliseconds
*  to even engage on these interesting questions.
*  So that suggests a local recurrence or at least a few synapse
*  sort of recurrent mechanism happening.
*  But I mean, we can just jump to the next thing I was going to ask you about,
*  because you so you actually did, you know, get
*  step away from the models, you inactivated the prefrontal cortex,
*  part of the prefrontal cortex and found that that is actually
*  very important for object recognition.
*  So I.T. and prefrontal cortex connected, but maybe that
*  in a more of a top down feedback sort of recurrence than a local
*  lateral sort of recurrence.
*  I don't know. Maybe you can just address because I just said,
*  oh, that makes it would suggest that it should have local recurrence
*  to process it so quickly. But maybe I'm wrong.
*  I would say the answer is probably all of the above.
*  It probably has some what we think there's some local.
*  If you think a lot of recordings are in the I.T. cortex
*  and we haven't talked much for the for the listeners is V1, V2, V4 I.T.
*  So I.T. is sort of the highest visual area.
*  And then I.T. connects up to prefrontal cortex, as you mentioned.
*  So if we record at the level of I.T., the temporal dynamics
*  that we see in I.T. are probably due to local recurrence within I.T.
*  They're probably due to top down recurrence from prefrontal
*  in the recent paper we had, as you mentioned, top down recurrence
*  from other areas that we haven't talked about peri-rhinocortex,
*  peri-hippocampal cortex, amygdala.
*  Those are other areas that would be affected.
*  And also there's time for recurrence of I.T.
*  to V4 to V2, back up to V4 to I.T.
*  sort of sort of cross area recurrence within the ventral stream itself.
*  And our best guess is probably all of the above.
*  It's not some simple thing, right?
*  So we've so far we've attacked prefrontal because it was easier
*  to make an experiment there than to get at some of those other things.
*  But we're interested in all let's call all three of those types of recurrence
*  and their relative roles and shaping up those I.T.
*  representations to be even better than the ones you get out of V4 and models alone.
*  Well, there's I.T. representations for core object recognition,
*  but then with the connections with all the other areas.
*  But then you start getting a definer
*  behavioral output, you know, amygdala, maybe put some
*  some masking on, be afraid of this object or, you know, something like that.
*  And then, you know, hippocampal memory, you know, some sort of abstract notion
*  of the object and prefrontal cortex controlling task selection, et cetera.
*  We don't have to go through all of them, sorry.
*  But then are we still talking about core object recognition?
*  Or are we talking about something more cognitive at that point
*  that we're going to have to tease out?
*  Yeah, that's back to the object recognition 1.0 that we said in the beginning.
*  It's like core recognition was just an operationalization of way to get started.
*  But it's not, you know, the only way that operation is that you tend to move
*  your eyes every couple hundred milliseconds.
*  So that causes sort of a hard could say that's a hard stop on the system has moved.
*  You know, there's overt feedback.
*  Usually when you're viewing the world, your eyes are actually moving.
*  Other parts of your brain are redirecting your eyes, which you could call a form of recurrence.
*  It's a, you know, it's a feedback on your whole your sensor system.
*  It's just executed by moving the sensor array rather than neural processing.
*  But, you know, but I guess what I'm trying to say is everything
*  that we call visual intelligence or cognition is it becomes a gray area between, well,
*  do I have cognition in 200 milliseconds?
*  Yes or no? I think yes, partly.
*  I mean, depending what that word means.
*  What does it mean?
*  And right for me, it's like if you say I can recognize your face
*  or something else about it within 200 milliseconds, if that counts as,
*  you know, if that counts as cognition, then you certainly have cognition in that time.
*  Do you have all of cognition?
*  Well, of course not. So it's it's, you know, it's it's not a yes or no question.
*  These are all shades of grays and the models get bigger and bigger
*  and more time extended and more time extended.
*  And this is back to, you know, one point two point oh, and we just keep extending that way.
*  And we capture more and more of visual intelligence is the hope of bigger spatial regions,
*  longer time extensions, models that now are bigger and have more recurrent areas that
*  I mean, that's how it's going to have to unfold.
*  It's not it's not a, you know, here's cognition.
*  You know, perception stops and cognition begins.
*  It's not going to be that clean.
*  That might be textbooks, but that's not how the brain looks.
*  Yeah. I mean, just to linger on this idea of, you know,
*  so this idea of adding more biological detail and incrementally improving the models.
*  I mean, is it just going to be like that from here on out or, you know,
*  I guess the question is, will it disappoint you or excite you if
*  if eventually we do have to get down to the real nitty gritty and add so many biological details?
*  Is that going to be disappointing?
*  Should it should there be some better explanation that we can
*  where we don't have to add in the biological details to really understand the system?
*  Yeah, I think I think that's really it's a good starting question.
*  It leads to a very long discussion of what does it mean to understand the system?
*  And I think we'll get to that.
*  That would be something something to discuss.
*  And you're asking, would it disappoint me?
*  And I think these are related questions.
*  Depends on what the goals are.
*  And I I wouldn't I don't I don't see it as a disappoint.
*  I don't think it would be disappointing if models get more complicated.
*  And in fact, I think they're going to have to get more complicated.
*  How much detail they have to get to explain which phenomena is unclear.
*  But that's OK, such as life with complex systems.
*  I I wouldn't disappoint me.
*  I don't have dreams of there's some, you know, great, you know, simple,
*  differential equation that the whole brain is going to follow.
*  And that's the answer. Like Maxwell's equations.
*  I've heard some physicists tell me that's what our answers of the brain should look like.
*  And I find that almost, you know, I can't imagine how that could ever
*  someone could think that's how you should think about a system like the brain.
*  It might be if it was true, we'd love to know it.
*  But if we all sort of said we get a neuroscience because that's our hope,
*  then I think a lot of us are going to be disappointed.
*  My bet would be against that.
*  But I know we can make progress with models that are more more complicated,
*  not just because we want them to become them, because they need to be more complicated,
*  because the brain is complicated.
*  I remember going to an SFN keynote address many years ago.
*  And it was I cannot remember who it was.
*  He was Scottish, but he was essentially saying we should give up
*  and let the physicists come in and do the job.
*  So you're saying not so much, huh?
*  I would say let the engineers come in and do the job, but not the physicists.
*  And I think some of that is happening in vision.
*  And they're doing the job on computer vision in this sense.
*  When they're working with those models, they're doing a big part of our job.
*  Of course, they're building hypotheses.
*  And that was part of what we showed is that some of the hypotheses that they built
*  are actually not bad models of what's going on inside the brain.
*  Yeah. OK, so let's move on here.
*  So an important part of an important property of IT neurons
*  is that they respond to particular objects, even when those objects
*  are presented in slightly different ways and, you know, different aspects,
*  different shades of color, different situations.
*  And, you know, speaking of so back propagation,
*  you know, was originally thought from, you know, back in the days of HEB
*  that the brain is doing all unsupervised learning, essentially.
*  So the HEBian neurons that fire together,
*  wire together is an unsupervised learning principle.
*  And you guys thought that there could be a role for unsupervised
*  learning mechanisms in IT, whereas everything else
*  up to this point had been supervised learning, I believe.
*  I mean, you know, since a certain point.
*  So maybe you could describe that work real quickly before.
*  Then I do want to talk about understanding and some of that work.
*  Right. You're actually describing the part I mentioned.
*  There was about a decade of work before the things in the deep networks
*  that you referred to.
*  And a big part of what I did in 2000 was we worked on kind of
*  can we see evidence of unsupervised learning in the visual system?
*  Because one of my favorite ideas is still one of my favorite ideas
*  is a system wires itself up with a combination of architecture
*  and some clever unsupervised learning strategies. Right.
*  So a lot of people still believe that idea, even in ML.
*  That's kind of one of the holy grail questions is to not have a fully
*  supervised system, have a more unsupervised system.
*  And Jan Mikun and others have sort of made that point very eloquently.
*  And I think so that that was a problem that drove me as well.
*  And the work you described was work where we said, well, one way
*  you could learn about objects and their stability, you know, to say,
*  as have neurons that say, respond to a face, even if it's shifted left or right
*  or, you know, a dog, if it's to the left or the right.
*  So that's called translation variance or it's distance from you.
*  So it's big or small is that you tend to see those kind of sequences
*  naturally during time.
*  If you during, you know, you just think about, you know, as you move your eyes
*  around the world, objects are translating on your retina.
*  And if your brain makes an assumption that, well, look, things that are nearby
*  in time are probably derived likely from the same things that objects don't
*  jump in and out of existence, that you could come up with a heuristic,
*  which is why don't you do some associative type learning related sort of
*  the HEB ideas you mentioned?
*  Others, again, these are not our original ideas.
*  I'm sort of summarizing them that you would you could build neurons
*  that would naturally build up in variances if they just leverage things
*  like time stability.
*  And this is there have been models of that.
*  Terry Sonofsky's group and Larry Whisk and others have worked on them.
*  They're under the framework of slowness models.
*  There's more recent versions of this in the ML community.
*  But that was the idea we pursued it.
*  We just recorded it neurons and said, if this is true, we should be able to mess
*  around with the visual statistics over time and cause the neurons
*  to change the response properties.
*  So it neurons that tend to like a dog over different positions.
*  If we keep playing it where the dog becomes a sailboat, when the object
*  translates over the eyes, either by eye movements or passive movement,
*  that that should cause the neuron to start to think a dog on a sailboat
*  of these two different positions are essentially the same thing.
*  Respond similarly to them.
*  That's the basic idea.
*  And we had a series of papers that showed that, yes, when you give the brain
*  those kind of statistical exposures and starts to bend the IT responses,
*  you know, slowly but significantly in that exact direction,
*  as if it's starting to absorb those statistics.
*  If you keep hammering the system with those kind of statistics,
*  even adult brains will start to reshape the IT response
*  as if that kind of learning rule using time unsupervised.
*  No instruction is actually running.
*  And that was actually quite exciting, because I didn't think
*  that was going to work at all.
*  But, you know, we had a nice couple of papers out of it and it worked.
*  And then I said, you know, and then you say, well, that work still stands there
*  waiting for a model to just absorb that.
*  And that's what we're excited about now, as these unsupervised models come.
*  Maybe we can start to connect them to those older results,
*  which were non-model based.
*  They were just sort of intuition phenomenology measured in IT.
*  And then the loose way I describe without a model to start to predict them,
*  you know, quantitatively.
*  Yeah, I think that's sort of an open frontier for the next five to ten years.
*  That's going to be exciting, I think.
*  So I hope those two lines of work will come together, a deep network
*  that learns in an unsupervised way and explains not just the response data
*  that you referred to of lots of neurons firing response to images,
*  but also the changes as you manipulate the statistics of the environment
*  that that we and others have measured along the visual system.
*  Sort of a model that can capture both of those kinds of phenomena
*  would be a model that starts to be more in the direction of it
*  learns more like the brain is learning because there's no supervision,
*  a very little supervision there.
*  I mean, eventually, you know, all these pieces are just going to have to come
*  together and it's going to be a massive system, right?
*  That's the way it's going to look.
*  It depends. Yeah, it'll be massive.
*  Well, I don't know what you mean.
*  You say massive.
*  We like a model that explains everything rather than one model
*  that explains one part of another.
*  And that's a little bit back to the you know, do you want simple models
*  or Maxwell's equations or do we want a big model that can explain everything?
*  And I agree with you.
*  You'd like something that was a little bit bigger that can explain more things
*  than we currently have.
*  OK, so finally, you're
*  now you're driving neurons wild at will
*  by having, you know, these your models create images, essentially,
*  that look extremely unnatural.
*  But and you know, you show but you show this extremely unnatural image
*  to a subject and you can control not just a single neuron.
*  You can make a single neuron
*  fire higher, more feverishly than it has to any other thing you've shown it.
*  And you can also tweak whole populations of neurons.
*  So I know you're excited about this because it affords powerful opportunities.
*  So maybe you can describe that a little bit further.
*  And then I want to ask you about understanding.
*  Yeah, that's great. You set this up well, Paul, because you described
*  exactly the the results that we've had recently.
*  There's a sort of fun story about this.
*  It's like, you know, I was trained to just say, we're going to build models
*  of the system. That's what our understanding is going to look like.
*  Engineered models of the system.
*  And, you know, so we were kind of doing that a little bit with our heads down
*  for a while, like let's build model,
*  like explain the responses better and better.
*  And then we started to succeed, as you mentioned.
*  And then, you know, it sort of struck us like, wait a minute.
*  What, why are we doing this again? Why are we building these models?
*  What's the they're complicated?
*  And, you know, what's our answer to why they're complicated?
*  We're explaining the data so we should be happy.
*  And then, you know, at some point, I realized the reason you build the model
*  is, of course, so that you can use it to do stuff.
*  It's not just to have a model.
*  You want to be able to predict stuff, but then you want to the next
*  move beyond prediction is to is control. Right.
*  So this is and your control knobs are afforded by the axes of the model.
*  So in this case, the models take images.
*  So they start with pixels
*  and they're predicting neural responses all on the ventral stream.
*  So their setup is you can control pixels.
*  You can move the pixels around to control the neural responses. Right.
*  So this is kind of a just a general statement of science.
*  The models that you build are basically ways to link
*  various things that you might be able to control or measure,
*  in this case, control, because we can control light on your eyes
*  to something else, a dependent variable, in this case, neural responses,
*  either single neurons, as you mentioned, drive a neuron wild
*  or a bunch of neurons set the population one neuron on and all the neurons
*  other off or every other neuron. Right.
*  So so this is really just a test of if you really have a good model,
*  you should be able to drive neurons wild or turn them off in these different ways.
*  So we said, let's let's go ahead and give it a shot.
*  And at least an area before this mid-level visual area,
*  it worked really well, much better than any.
*  You know, we were able to show against standard measures of, hey,
*  we we already had neuroscientists running around trying to do controls.
*  They would dream up stimuli and say, we think these are this.
*  And they would use them.
*  And so that was our reference.
*  If you use those stimuli, could we beat those?
*  And now so now we're able to drive the neurons higher
*  or more accurately in terms of populations than those in that previous work.
*  And we showed that in the paper.
*  But the control is also not perfect because the model is not perfect. Right.
*  So the the model that sort of attest to the model,
*  but also it's an application tool because, hey, one of the goals of brain
*  science is to do things like apply images and maybe be able to tune your brain
*  into a way that's helpful to improve, say, your health or even your mood.
*  And it leads to those kind of uses of models, right?
*  Not just models for model sake and so-called understanding,
*  but models for actual use in some way.
*  For use. Yeah, I imagine that.
*  So you envision, you know, down the line, like you said, they're not perfect right now.
*  But you envision this and using this in a therapeutic fashion, potentially.
*  That's how I think about it. Right.
*  We've grown up so long with brain science is like the way you're going to fix
*  a brain disorder is, oh, you've got to give a drug.
*  Of course, you give a drug. That's how we treat everything.
*  But there's many brain disorders that we don't.
*  There's one big one that we don't fix without drugs.
*  And it's my colleague, Josh Tenenbaum, here at MIT.
*  And for reminding me of this, it's like, you know, a lot of vision problems.
*  I don't give you a drug.
*  I just put these kind of funny lenses in front of your eyes.
*  And, oh, suddenly you're improved in your behavior. Right.
*  Well, that's just optics on the front of the eyes.
*  But that's an example of a, you know, something about understanding
*  the eyeball that, you know, then turns into a device on the front
*  without actually having to go inside the head. Right. Right.
*  So so there may be ways and there's other areas.
*  Others people are thinking about this in digital medicine more broadly.
*  The more you understand these, you may be able to inject energy
*  properly into the system without getting so inside the head,
*  whether molecule or a beam of light or whatever you want to stick in someone's skull.
*  You might be able to make progress without doing that.
*  And so that that excites me from a vision side, because that
*  that would offer new opportunities that just usually aren't thought of that way.
*  I mean, even, you know, so obviously you take a drug and it just bathes
*  your entire brain in it, you know, it doesn't really target specific
*  a neuron, for instance, you know.
*  But even like Parkinsonian patients, patients who are getting deep brain
*  stimulation, that's still that stimulation is just massive.
*  And it's just driving like the whole population.
*  And so, yeah, the more subtle these sorts of
*  abilities to perturb in a very specific way is the more subtle
*  and specific that gets that that is exciting.
*  So all right, let's talk about understanding.
*  So so in in the deep learning world, there's this growing divide
*  between prediction, you know, these models that predict
*  are super accurate with predicting things.
*  And I'm going to use air quotes with understanding now,
*  because you often use quotes when you talk about understanding.
*  And if that's happening in deep learning, then, you know, it's scary to think
*  how far that divide could go in in brains and neuroscience.
*  So there are a few different ways of talking about understanding.
*  And some say, you know, to understand these more recent deep learning models,
*  we can't really understand again.
*  Just assume I'm using quotes around understanding.
*  We can't really understand them at the unit level or population level.
*  The internal working.
*  So what we should do is try to understand them at the level
*  of the things that we control, like the algorithms, the architectures,
*  you know, the objective functions.
*  And that is kind of provides a first pass rudimentary understanding of these models.
*  And then in the philosophy of science, there's really been an explosion recently
*  in people writing books.
*  You know, there's been a handful the past few years
*  trying to figure out what understanding is.
*  And those are all driven by the conception of understanding as something that,
*  you know, discovers some simpler principle than the thing that you're
*  trying to understand, discovering some simpler principle,
*  not Maxwell's equations, for instance, but some simpler principle
*  that can account for the host of more complex things going on
*  that you're trying to understand.
*  But you have this you've kind of pushed this new operationalized
*  definition of understanding.
*  And what it means in the modeling world.
*  So what do you is that of understanding?
*  And what is the because I know you use it in quotes.
*  What's the blowback that you're getting from using it like this?
*  Yeah, this is a fun discussion.
*  We have it all the time in the lab.
*  So I often say, you know, scientists, I was true.
*  We all use this for humans.
*  We use the word understanding, and it's kind of a cover word for not saying
*  what your goal is.
*  It's another way to put it like if you soon as someone tells you
*  they want to understand, so they say, well, what do you mean by that?
*  And they might first they might say, well, I haven't thought about it.
*  And then eventually they might, you know, you're going to get them
*  down to something like you think they're going to be a form of prediction
*  or control, like it all if they're it's going to boil down to prediction
*  or control. And that's where I guess the main thing I would say,
*  they usually wouldn't phrase it that way.
*  But that's that's what they would seek.
*  And they would want to seek that under some simplicity,
*  you know, constraint, as you mentioned.
*  It's like you'd ideally want a lot of prediction with the simplest model.
*  Now, simplicity is hard to define, but that's the that's sort of
*  a good model is one that's as simple as possible and predicts a lot.
*  And not simpler and not so well, because you take it simpler.
*  It'll predict less, right?
*  You make it less simple to predict more.
*  So there's just a trade off between those two things.
*  And that's we could all choose where we want to be on that trade.
*  And sometimes I think scientists want to be on the simplicity end
*  and engineers want to be on the other end.
*  And I'd like to think the middle is where you really want to be.
*  I mean, you know, if you want to fix brain disorders, I'm sure, you know,
*  people that would that are suffering from that would rather you
*  went by a model that was a very accurate model of what's going on
*  when they had a brain disorder, regardless of how complicated it was
*  and not have to say, well, no, but I needed the beautiful model
*  because it just made me aesthetically proud or pleasing as a piece of art.
*  That's not going to help the person with the brain disorder.
*  Sure. Right. They don't care if it's complicated or not.
*  That's a sort of scientific aesthetic
*  that that is grounded in the idea that it will tend to generalize.
*  Right. That's a sort of an Occam's razor.
*  Like if you make it simpler, it will tend to generalize in some way.
*  And so I'm going a little bit off your question, but I think that's sort of
*  that's how we were all trained that because physics found that, well,
*  you made these beautiful models and they tended to generalize in other ways.
*  And there may be aspects of that for brain science.
*  Imagine what does generalization mean to, you know, you know, another species
*  on another planet we haven't yet encountered.
*  Yes, that might be true.
*  But maybe there are things that will generalize notions of intelligence
*  and so forth. But right now we have an operational problem of like
*  we've got this thing that lives between our ears and the homo sapiens
*  that we're trying to build good models of.
*  And it's sort of an earlier stage problem that just requires.
*  You know, principles is a little too lofty, is I guess another way that I
*  that I would go.
*  So so I I think again, I'm I'm
*  the notion of understanding is a tricky one.
*  But to me, it's all about building models that support prediction and control.
*  And it's trade off between simplicity and prediction and control.
*  But in this phrasing, you know, it comes down to then,
*  even when I say that you should push to me and say, well, Jim,
*  what are you trying to predict?
*  What are you trying to control?
*  You know, that becomes the again, you know, because I'm being vague about that.
*  Right. I said earlier, oh, I can control light on your eyeballs,
*  but maybe I can control your genes.
*  You know, if I'm a molecular biologist, I have good control over genetic tools.
*  So those are my control knobs.
*  So and what do they want to predict?
*  Well, maybe I want to predict your behavior.
*  I want to explain your behavior because, you know, we're we're the organisms
*  that are paying the bills as taxpayers.
*  So we're the ones that we want to help.
*  But maybe I want to predict the responses of neurons.
*  Well, again, the taxpayers don't care about the neurons.
*  They care about if they actually, you know, are they are they feeling better?
*  Right. So those are those are, again, the operational definitions.
*  But but to me, but you have to you choose those.
*  And then that different scientists will choose different forms of those.
*  And then everybody's science could be boiled down to a choice of
*  what are you controlling and what are you trying to predict?
*  I mean, what do you? Yeah.
*  So you what you see is sort of a two pronged
*  possible set of definitions of understanding.
*  One is very specific to if you understand something, you can predict it.
*  And the other is if you understand something, you can control it.
*  Is that so you don't like the idea of understanding as being
*  I don't know, you know, to say ontologically is heavy,
*  but as being something separate from prediction.
*  And of course, separate from control, because, you know, that's that's the
*  sort of monkey, you know, elephant in the room.
*  But so and in between prediction and understanding is explanation,
*  which kind of goes back and forth as well.
*  So but but the way you conceive of understanding, then
*  is this if you understand something, you can either predict it or control it.
*  Do you get blowback for that?
*  I do. Right. And so and I would say, first of all, prediction
*  and controller to me are two sides of the same coin.
*  You could do it. You know, if you can predict well,
*  the difference is whether you actually have control knobs, right?
*  So, you know, sure.
*  You know, astrophysicists might have a hard time controlling certain things
*  that they're measuring out in the universe, but but they can still predict them.
*  So I wouldn't call that not a science.
*  But where we on this planet, we have a lot of control knobs
*  we might be able to use for the brain.
*  So we have both prediction and control, but they tend to go together.
*  If you can do good prediction, you generally should be able to do good control.
*  But that's not so let's couple those together.
*  And I think the thing that you raised was like, well,
*  what about explanation or something more vague that you called understanding?
*  And you said something a minute ago that I lost the thread.
*  But maybe you could say it again, Paul, because I think I was
*  you tweaked my interest there.
*  A separate line of the way to understand something.
*  Well, in the philosophy of science.
*  Oh, I probably said ontological.
*  So in the philosophy of science, it's almost agreed upon, I would say,
*  that there is again, I kind of cringe to say ontological,
*  but there is a difference fundamentally between what prediction is.
*  And prediction is just quantifying the output.
*  Right. And you can say it's accurate or inaccurate, you know, very quantified
*  and understanding. And a lot of work, at least in the philosophy of science
*  these days, is aimed at getting a better grasp on what we actually even mean
*  when we say understanding.
*  Right. Because there's these notions from historical science
*  and philosophy about explanation itself.
*  And now it's sort of blooming into more of an understanding,
*  which is brings it down more to the our cognitive capacity
*  to conceive of something and think about how that,
*  let's say a model be able to in our heads sort of simulate.
*  If I did this to the model, this is what would happen to the output.
*  Something like that is more akin to the philosophy of science
*  sense of understanding as I understand it these days.
*  So what's your response? Right.
*  So now I sort of. Yeah.
*  So I think if you that version of this understanding and this boiled down version,
*  imagine whatever that is, let's suppose you had it,
*  and it was declared ontologically beautiful or whatever version you want to use.
*  And it didn't predict anything.
*  Would you call that understanding?
*  I don't think you could. Right.
*  So if you you could have something that you thought was beautiful
*  and easily digestible by humans and all the things that you were describing.
*  Yet it failed all prediction tests.
*  Like, I think that's a nonstarter. Right.
*  You would say that can't count as understanding. Right.
*  So now we're now we're on the path. Right.
*  So now we're going to say, well, how much can I predict?
*  So, OK, then you're going to it's just the curve at one axis.
*  You're predicting everything perfectly well,
*  and you have a very more complicated, harder to intuit model.
*  The other end, you're going to have a lower dimensional,
*  simpler to explain human model that may predict nothing at all.
*  And what you want is to be in the middle of those,
*  which is the most intuitive model you could have that explains the most things.
*  And I mean, the other thing we're circling around here is the notion of,
*  you know, why is the goal to explain it to other humans?
*  Is that really is that I want to know?
*  Well, but I think that's sort of the thing we should ask ourselves.
*  I mean, I always pull out my iPhone.
*  It's like you understand your iPhone, you know, you feel like you do,
*  but you don't really.
*  And actually, no human on the planet actually does, I think,
*  because it takes teams of teams of humans.
*  And that's sort of how I think models of the brain are going to look is together.
*  We think as a species, we understand it.
*  Individuals understand it well enough to use it.
*  Some individuals understand it well enough to improve parts of it.
*  But no human individual understands the whole thing.
*  And this is a device we built.
*  It's not probably as complicated as the brain.
*  And so so the form of our understanding is going to be a little more like that.
*  And what's wrong with that?
*  We can cure brain disorders with if we had an iPhone version of the brain.
*  We would just we just have to get used to the idea that the complexity is managed
*  by many people together, not by each of us feeling satisfied on our own.
*  I think that's the maybe tension that we're sort of describing here.
*  And many people got into science because they thought they themselves
*  are going to have to get intuition.
*  And I don't know if we have to.
*  Maybe that's the part that feels as hard for me to sell this vision,
*  because I like it, too.
*  I'm a human being. I like it to feel intuitive, too.
*  But I don't know.
*  If you think about your iPhone, there's many parts of it.
*  They're not. You say, I don't care.
*  Somebody knows those details. Well, OK.
*  The brain, somebody has to know those details, too.
*  And it is we don't have to have intuition for every component of everything.
*  We just you know, the way to judge it is whether the darn thing works
*  when you pull it out of your pocket or whether it actually controls and predicts.
*  Is that in the language that I'm using for the brain or helps you cure brain disorders?
*  I'm going to give one more concrete example of this, because I just had Masri to Chirimutah on,
*  who has written about this and she actually has written about your work,
*  which she admires, but her conception of understanding.
*  So, you know, she compares not your models, but specifically
*  because it gets a little complicated because your models map onto the,
*  you know, brain areas and are trying to account for brain areas.
*  But let's say, you know, neural network models writ large these days
*  versus earlier canonical models of things like simple V1 cells
*  or normalization as a canonical computation.
*  So her argument would be is and I can speak for her, I believe that
*  the canonical models, even though they don't predict as well.
*  So they predict pretty well in certain circumstances,
*  but then in natural circumstances, they don't.
*  So they, you know, their prediction is not perfect.
*  But because of the way that they are conceived in this canonical sort of computation,
*  they actually provide greater understanding.
*  And this is just a different definition of understanding, maybe in that conception.
*  They provide greater understanding while predicting worse than,
*  let's say, a neural network model that predicts beautifully
*  because it can perform the task and it can.
*  But we but it doesn't provide understanding in, you know,
*  it doesn't spit out the mathematical function that it's using to predict those things.
*  That mathematical function is really embodied and buried in,
*  you know, distributed units.
*  And so it doesn't provide the same level of understanding.
*  So that's the concrete example.
*  But I think that's orthogonal to your control prediction sense of understanding.
*  Yeah, I don't. Again, control prediction, let's just call that one direction.
*  That's just better prediction for now.
*  So keep those together as one.
*  And I don't think it's entirely orthogonal. Right.
*  So, again, I think you're just if I was drawing with my fingers around one axis
*  is simplicity or what the human thinks is beautiful.
*  And that might include close form math equations if you want, depending on your
*  there's an aesthetic there of what what we mean by beautiful or understandable.
*  And the other axis is prediction slash control.
*  And there's you can imagine a curve of points.
*  Right. And you'd say I wanted your you've got this really complicated,
*  ugly thing that predicts everything.
*  It's almost like the data itself. Right.
*  And the other extreme I mentioned is that you got this beautiful
*  statement to the world like a poem, but it predicts nothing.
*  Right. And of course, you want to be up in the corner where you're doing both.
*  And I think we all we all want to be there.
*  But imagine that there's a world, imagine the world, the function doesn't look like that.
*  It looks like, you know, a kind of exponential fall.
*  Now you've got a hard choice.
*  Do you want to actually be in the beauty world?
*  And it's like, we're nice. It's good for museums and talking to other humans
*  and making them feel like they have understanding and having nice math equations.
*  Or do you want to be in the world of actually predicting and controlling?
*  And I hope you won't have to choose.
*  But I think that's why there's so much pushback.
*  Because people are maybe afraid that we're getting forced into that world.
*  And that's not the world that they hoped for.
*  And imagine the smart Einstein might come around to our field and say, actually,
*  if we rethink what we need with simplicity, the curve will suddenly open up
*  and it'll become a not an exponential but more of a square again.
*  And then we'll get up into the corner and just have to think about it in a different way.
*  And everybody will be happy.
*  We need that. We need the tensor geometry with our sense of the axes.
*  Right. So I get it. I think that could happen.
*  And I'm not opposed to that.
*  We're just busy trying to build models that are at least doing well on the prediction and control
*  in a fair sense, not just capturing the data, but real prediction and control,
*  knowing that that minimally will be fuel for those that like to try to make
*  let's call them simplify them and make them more beautiful and find the underlying principles
*  if they exist.
*  So I view our work as sort of a step towards that larger goal,
*  which would means that we could make progress along the way in things like brain disorders
*  and other things that we mentioned earlier, even if we haven't yet fully made them
*  simple and beautiful and give material for people to chew on
*  with the hopes that they may eventually find simpler ways of describing those models.
*  Right. So these are not at odds.
*  It's really a question of which thing is the field ready for first?
*  Like, should it keep thinking about beauty and principles or should it work on models
*  that are capturing the data?
*  And I guess the thing I would advocate for is right now we need to have models that predict
*  stuff at all and do that first.
*  Not, you know, not that's not let the enemy, you know.
*  Well, you know what I'm trying to say?
*  Perfect be the enemy of the good.
*  We don't need to jump.
*  We don't need to jump right to the perfect model that's beautiful in every way and
*  predicts everything. Let's just try to get some prediction models going and then we can
*  simplify them later.
*  That's a choice that's spoken like a successful engineer modeling the visual
*  stream.
*  Well, yes, that's right. So I'm I'm a I'm in a science department, but I'm actually an
*  engineer at heart. Right.
*  So I hope that's right.
*  So maybe I'm not I sometimes tell my students maybe I'm not really a scientist in this
*  sense. And that makes me a little sad because of science is only going to be if you're
*  beauty, then OK, then we'll see the whole field of neuroscience to engineering is, you
*  know, if that's what I fear the next decade will become.
*  And I don't think a scientist should see the field of neuroscience to engineers, even
*  though I'm an engineer. I'm also a scientist that I think scientists should just be
*  willing to embrace more complicated models and have their not be so afraid.
*  I mean, that this is doesn't mean that we're giving up on those ideas.
*  It just means this is the next step.
*  Not it's not a dead end.
*  But I do resonate with that. You know, again, you point out our work is a little hard to
*  categorize because some people use deep networks as just, oh, it's just a big hammer and
*  you just predict stuff. And it's just a black box of a bunch of stuff.
*  And then then I'm with you. And I'm with anybody would say, that's not understanding
*  because then then it's just a big complicated system as just a prediction tool.
*  And when I say prediction, maybe this is very important to point to get across.
*  The deep neural network of the brain has many levels and our measurements, every level
*  of that model better have a mapping within the brain, which can be tested.
*  There's no black boxes allowed in our framing of these models.
*  And I think maybe that's where we have agreement with, you know, that's where I think
*  the begin. This is back to the field is often used networks to do things like prediction
*  and control without worrying that they're, you know, mapping all the components to this
*  system like the brain. And that's where I think our work is not.
*  Some people get that from our work, but we're sort of cast into the lot of we're all doing
*  deep network. So we must be doing that crazy thing where we build a big black box and then
*  just do prediction. And that's not actually what's going on.
*  We view those as neural mechanistic approximations of what might be going on in different
*  parts of the brain. And our job is to check how true they are and then improve them.
*  But the models are still complicated. They're big networks.
*  Oh, the brain is a network. How can that not be true?
*  So I hope that makes some sense that there's a middle ground between these.
*  There is an extreme that I don't want to be put in either camp.
*  I'm not in the simple models, you know, physicists camp.
*  I'm also not in the let's just build deep networks and hammer on every data set and
*  put a big black box and go home. Right.
*  There's a there's a middle ground, which is the interesting space.
*  I think that's really exciting for our field, not just for vision, but, you know, from
*  Ramon y Cajal, we said, oh, it's a neural network.
*  So our job is to figure out if we're going to be neuroscientists, it's a big neural
*  network. So our job is to search through which neural network is actually running in the
*  head and find the right one and model that.
*  That that was what we were trained to do.
*  Otherwise, we shouldn't call it neuroscience.
*  We can call it cognitive science.
*  We could remove the neuron. We could.
*  And I'm not saying that in a joking way.
*  Neuroscientists need models with neurons and then they're connected, a.k.a.
*  they work with neural networks.
*  So what is to this?
*  What is to dislike about working with big, complicated neural networks?
*  That's the whole brain. I mean, it's it's.
*  The base hypothesis in the field.
*  And I don't know how a neuroscientist can sort of say, well, these I don't like deep
*  neural. What do you mean?
*  You don't like the brain, then?
*  This is the base hypothesis.
*  The trouble is they're mapping the word, you know, artificial neural network into today's
*  current feed forward only simple rectification functions.
*  And of course, that's not right.
*  It's an approximation.
*  But they can't dismiss the whole class because that is obviously right.
*  They take it. They learned it on day one of neuroscience that it's right.
*  So I think it's there, you know, navigating those two worlds of, you know, those views
*  on an artificial neural network that we our field has to kind of come come to grips with.
*  That's good. I'm glad I scratched that itch for you.
*  So so optimistically, optimistically, eventually the full story about, let's say, the
*  ventral visual stream will be told.
*  Where are we in that story?
*  Yeah, well, I think I'd like to say we're, you know, in terms of there's two parts to this
*  question. So, you know, where are we in explaining the ventral visual stream or even just for
*  core recognition, which is only, again, one part of visual intelligence.
*  Yep. You sort of said earlier, we have pretty decent let's just there's two main parts of
*  what I think about what is what is the adult inference engine doing?
*  What is the description of the adult ventral stream as it is?
*  And say you or I and that, you know, we might be a quarter of the way there, maybe halfway
*  there. We have some models that can approximate that pretty well.
*  There's a lot of important opening questions.
*  You mentioned recurrence and others.
*  But, you know, we're making good progress on that.
*  And that's where a lot of our work has been.
*  And there's still a ton to do there.
*  But there's another question, which is how does the darn thing wire itself up?
*  Right. How does it go from a birth state or evolution, which, you know, also connects to the
*  machine learning community when they think about learning the system is partly, you know,
*  there's learning, which is kind of neuroscientists called development or evolution or some
*  combination thereof.
*  That that part we've got much less progress on.
*  That's sort of the whole. There's a huge open space of questions.
*  And that's back to our earlier discussion of the learning part is not mapped on to the to the
*  actual system very well.
*  The deep learning part may or may not be right in various ways.
*  So I think there were sort of less far along.
*  But on the inference side, we're sort of, you know, you know, we're, you know, again, we're going to
*  look back and say these models were we're good, but far from perfect.
*  But they're, you know, maybe I can generously say we're, you know, a quarter to a halfway
*  there where you'd like to be on that problem.
*  So do you see is the rest of your academic path career?
*  Do you just see it mapped out already because you have these five or six different full on
*  streams of beautiful potential work to do?
*  I mean, you're busy.
*  Yeah, we're not going to we're not going to get to all of those things.
*  I mean, we talked about some of the things we are most excited about, like moving, pushing some of
*  these control experiments deeper into the brain and obviously always improving models.
*  Thinking about some questions for human health or maybe even some learning, learning related
*  questions for education.
*  Those are things that are starting to excite me now.
*  But I'm also, you know, I, you know, I'm 52.
*  So maybe I'm like halfway through my career.
*  I'm starting to think about, you know, what's that going to look like at the end?
*  But, you know, what excites me now is all the people coming through my lab and, you know, they
*  come away saying, well, I've got, you know, they come away with it.
*  Yeah, I think a different way of a different way of thinking.
*  And they come back and tell me this like, wow, I, you know, I, I didn't see an
*  until I kind of spent time in your lab.
*  And instead we, we sometimes a lab joke, we're doing indoctrination.
*  Like maybe it's a bit of a religion, but they sort of, they sort of start to come around
*  and some of the views that we've been discussing about here and they see that as, oh, this
*  is actually a way to make progress.
*  And then they go and I'm seeing them do it in other parts of vision or beyond vision.
*  And, you know, what will make me happy is when they'll come, you know, 50 years, if I'm
*  still alive, I'll get to hear their stories of how they took those ideas and extended
*  beyond core recognition, beyond vision and, and, and took them to, to the bigger problems,
*  because we're going to need teams of people working on this.
*  And one lab is just going to kind of try to do the bit we can.
*  But I think that's what's going to excite me is the way I can influence others to try
*  to do that.
*  You've certainly spawned a lot of successful teams.
*  Have you always had this way of thinking or has your way of thinking about these things
*  changed since early in your career?
*  Yeah, I mean, the way I think about these things, I got a ton of credit is to my
*  graduate advisor, a professor named Ken Johnson.
*  He passed away about a decade ago.
*  He he Ken was an engineer by training and he, you know, he was the one who got me on
*  these problems like there's this you have to transform the data.
*  You have to go through a series of representations and look, the visual system does
*  this in this magical place up to the ventral stream called IT and it then enables object
*  recognition. Those are the things he would while we were busy working on the somatosensory
*  system. Right. So that was what I was in his lab as a graduate student.
*  And I said, well, Ken, well, that's great.
*  Let's go do that. So then I figured out how to kind of get John Mansell to let me do a
*  postdoc in his lab and give me some vision credentials.
*  And John is a super incredibly supportive mentor.
*  And and then between those two, I take kind of Ken's vision and then John's teaching of
*  how to actually do some vision science.
*  And that's where that comes from for me is the combination of them.
*  So a lot of what I'm doing is just taking forward visions that I got from the two of
*  them. In that sense, I owe a debt to them.
*  This is not something I dreamed up one day of.
*  This is the right way to do it.
*  And maybe I've added our other ways of other tweaks here or there that we've come up with.
*  And I credit those to my students and postdocs.
*  I've been lucky enough to join my lab.
*  So I'm more of a steward of what's going on than I would not call myself a mastermind
*  genius. I'm a community organizer to kind of get some stuff done together.
*  Do the students that come in, do they do they want to do engineering or do they want to
*  do neuroscience? Do they want to inactivate prefrontal cortex or do they want to build
*  models or happen?
*  You know, what's what's exciting is they all want to do both now.
*  Right. And that's what's really exciting.
*  It's like they don't want to do it.
*  It's just engineering that feels a little dry.
*  You know, the brain is a very motivating thing.
*  Like, how do billions of neurons and trains of connections make each of us who we are?
*  And, you know, all the things that we can do to help humans is like this is the this
*  is the thing that you know, that's exciting.
*  That's what neuroscientists have.
*  But they also see, look, I can't just make measurements and inactivate brain areas.
*  We've been doing that for decades.
*  And you can walk around SFN with 30,000 posters and not clear it's converging into kind
*  of a model of the system.
*  Right. So they're sort of drawn to this sort of interface between models and data.
*  And I I've sort of been trying to nurture that in my lab where everybody does a little
*  bit of both sides and they work together, often the best projects.
*  And you mentioned the control projects like two postdocs, one coming from a more ML
*  background, the other coming from neuroscience.
*  And they each learn from each other and they get something done together that neither of
*  them would get done on their own.
*  And that I think that's kind of that's what it's heading to me.
*  And I think exciting to a lot of students.
*  They want to touch both sides of that of that that bridge.
*  Yeah, the actual brain wetware.
*  But the models and the ML and the AI that go into that side as well.
*  And that has practical advantages, too.
*  You could get a job at Google or Apple or if you like, or you could run a lab.
*  You know, and so, you know, that these are but that's the that's the exciting time for
*  students coming into the field at that intersection, I think.
*  You record a ton of neurons at once, and that's just going to grow.
*  That number is going to grow and grow.
*  But do we need it to grow? Are we recording enough simultaneous neurons or do we need to
*  be recording all of them?
*  What's the right amount of neurons to record?
*  Yeah, I don't think there is an answer to that.
*  I mean, it's my first of course, more is always better.
*  But but but do you do you get more explanatory power if you double the neurons that you're
*  recording right now?
*  Would it actually benefit the, you know, the match from the models to the brain?
*  Not the ways that we've been matching so far, we're rematching sort of how we can
*  predict individual neurons and then we talk about averages over a many neurons.
*  But I think the interesting form of that question to me becomes if we have two models
*  that we can't tell apart, like you seem to match the data, how many neurons and what
*  type would you need to distinguish among those two?
*  Right.
*  And notice when I phrase it that way, that sounds like science, right?
*  You've got two alternative hypotheses.
*  The hypotheses drive the experiment and then the experiment is powered enough to separate
*  the two alternatives.
*  But that's our field is only just starting to do those things.
*  Most of the history of neuroscience is led by people's intuitions of, well, I should,
*  you know, inactivate this or record here and then I'll make sense of it later.
*  It's not very model experiment driven for the most part, right?
*  It's more kind of intuition driven.
*  Exploratory.
*  Yeah.
*  Exploratory.
*  And that's not bad.
*  You need to do that at the beginning.
*  And beginning is the last century, right?
*  And that work should continue.
*  I don't need to say that that work shouldn't go, but it's sort of exciting that now the
*  models are going to start to tell us what experiments to do.
*  And like they're going to guide even to answer your question.
*  The first thing I would do is kind of ask folks in my lab and say, let's run the simulation
*  on if we had this many neurons, what would we be able to do?
*  But I'd have to have a question.
*  Is it separate two models?
*  Is it to control something?
*  We otherwise it's sort of very hard to answer.
*  You know, it's sort of like asking how many humans do you need for a vaccine study?
*  Well, it depends on a lot of what is the safety or, you know, there's lots of things
*  that go into that question.
*  So you started off recording single neurons, right?
*  We did, because that's how we were trained.
*  Yeah.
*  Did you, did you think, did you think that you'd be recording thousands of neurons at
*  a time back then?
*  Again, we're not thousands or more hundreds of thousand at the moment.
*  But well, it's multi-unit.
*  So who, you know?
*  Yeah.
*  Okay.
*  So we could say, but then they're mixed together.
*  So that's, you know, against the, the, you know, with the training was you should get
*  really good clean single units.
*  Does that matter that we're that it's multi-unit?
*  It, as far as we can tell, it doesn't again, add much more constraint power to the, to
*  the model separation.
*  But, but again, we keep asking it.
*  We don't, we're not going to give up on that.
*  We try to find clean single units and multi-unit.
*  We ask, we'd re-ask the questions that you're asking for almost every experiment.
*  If we had more clean single units, what do we think if we had more units, does that
*  tell us anything different?
*  So you're asking why should we keep recording single units or, you know, I think this to
*  me becomes a, it's, it becomes a, a model driven question.
*  What, what is the goal of the, which models are you trying to separate and what's the
*  best data to do that?
*  If you, you know, given the choices you have, you may be able to get thousands of multi-units
*  versus a hundred clean single units.
*  Okay.
*  Those are apples and oranges.
*  So only if you have a goal in mind, can you then say, which is better?
*  So more is better, but that's sort of an undergraduate answer, right?
*  That's the undergraduate criticism to this.
*  How could this paper be better?
*  Well, they could have collected more neurons.
*  Well, that's always true, right?
*  It's, it's harder to answer it in the concrete, but you need, you need some alternative
*  hypotheses to then, to, to answer that question.
*  I know it's after hours in your world.
*  So I had just had one more question for you and that is what are brains for?
*  What are brains for?
*  Yeah, I think, um, first of all, I would, my answer to that question is brains are not
*  quote for anything, right?
*  They use the word for it's sort of a subtle thing in the language implies, implies
*  that it's designed, right?
*  So the four implies designed everything we know about evolution says none of this was
*  designed, it's not for anything, but brains, I would say brains are a very interesting
*  part of a machine that was selected for its ability to survive and reproduce.
*  So that's really just a statement of evolution recapitulates evolution, which is
*  totally fine because it all comes back to evolution.
*  But, uh, yeah, right.
*  Right.
*  But that's, but that's also why we couldn't give the answer of, well, uh, you know, it's,
*  it's just evolution with what's go home.
*  This is optimized and you know, we can, we can make a textbook.
*  How does the brain work?
*  Well, it's for survival and reproduction.
*  We should all go home.
*  Right.
*  Let's go home.
*  We're good.
*  Let's get on other problems to be solved.
*  Yeah.
*  Well, Jim, thank you for your generous time.
*  I'm going to let you go home.
*  Uh, I really appreciate you spending time with me.
*  Oh, it's been fun, Paul.
*  Thanks.
*  Thanks for chatting with me.
*  Brain inspired is a production of me and you.
*  I don't do advertisements.
*  You can support the show through Patreon for a trifling amount and get access to the full
*  versions of all the episodes.
*  Plus bonus episodes that focus more on the cultural side, but still have science.
*  Go to braininspired.co and find the red Patreon button there.
*  To get in touch with me, email paul at braininspired.co.
*  The music you hear is by the new year.
*  Find them at the new year.net.
*  Thank you for your support.
*  See you next time.

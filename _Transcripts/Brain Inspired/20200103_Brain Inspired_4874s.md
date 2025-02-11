---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4874s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 6594
Video Rating: None
---

# BI 057 Nicole Rust: Visual Memory and Novelty
**Brain Inspired:** [January 03, 2020](https://www.youtube.com/watch?v=FARtT-bG7Uc)
*  While identifying the objects that are in view is a really important problem that has
*  contributed tremendously to our understanding of processing in the Ventral Stream, I think
*  that it has happened at the expense of appreciating that that's not just what your form processing
*  pathway is for.
*  You might want to take even a step further back and ask yourself, well, what do we do
*  with that amazing ability to remember images?
*  And there, I think machine learning has some really interesting things to say that build
*  on some observations that I think are classic observations.
*  Hey everyone, I'm Paul Middlebrooks.
*  Welcome to Brain Inspired.
*  One of the great success stories connecting neuroscience and AI is how well some deep
*  neural networks match brain activity.
*  In particular, convolutional neural networks can be arranged in layers and made to mimic
*  the cascade of brain regions associated with processing visual images from low-level features
*  like edges and contrast up to entire objects like hot dogs and elephants.
*  But identifying objects isn't particularly useful in itself.
*  It's useful in context.
*  What can we do with an object?
*  Can we eat it?
*  And so on.
*  One particularly useful thing to do is to remember what we've seen.
*  And we're extremely good at remembering what we see.
*  So good that if we're exposed to 10,000 images for just a second or so each, we can later
*  pick out those seen images among ones we haven't seen before.
*  My guest today, Nicole Rust, studies visual memory.
*  And we talk all about her work showing that the same populations of neurons in our visual
*  cortex that can represent objects and images can also represent how memorable and how novel
*  those objects and images are.
*  More than that, those convolutional neural networks that represent objects similar to
*  the way visual cortex represents objects, they also appear to represent memorability
*  similar to how visual cortex does, even when the deep networks aren't even trained to
*  predict memorability.
*  This train of work has led Nicole to also start thinking about how a system could use
*  to drive its curiosity and exploration to learn most efficiently.
*  And she sees a way forward to combine what we know about how brains do this with how
*  AI has done this using reinforcement learning to better understand how we use visual memory
*  and novelty to help us learn.
*  You can find out more about Nicole by following her on Twitter at visual memory lab.
*  And I link to that and her website and things that we discuss in the show notes at braininspired.co
*  slash podcast slash 57.
*  If you follow the podcast, you know I'm building an online course to explore the entire neuroscience
*  and AI landscape.
*  I just posted a little introduction video that I made that explains more what to expect
*  from the course.
*  If you're interested, you can learn more at braininspired.co slash course, which reminds
*  me if you're a Patreon supporter, like recent supporters, Charlie, Travis, and Chomsky Balls.
*  Chomsky Balls.
*  Did you enter your name as Chomsky Balls just so I'd say Chomsky Balls on the podcast?
*  Anyway, thanks Patreon supporters.
*  If you are a Patreon supporter, you will have that video in your email box.
*  So check your emails.
*  Happy New Year, everyone.
*  If you're like me, the new year means essentially nothing.
*  But either way, a great way to start the new year or any day really is learning from Nicole
*  Rust.
*  So I'm walking into my front door of my childhood home and there's this giant squid hanging
*  in my way, drying and wilting in the harsh heat of the sun.
*  I get through and I turn right and in the corner of the entryway, I see my third cousin,
*  the one with all the herpes breakouts, performing a lewd act on a hamburger.
*  Right next to her is the fish tank that's filled with jello and this crying roly poly.
*  And this is how I remember my wife's phone number.
*  Nicole, welcome and thanks for being here.
*  How do you remember your social security number?
*  Thanks so much for having me, Paul.
*  Yes, that was a great example of the method of loci, right?
*  The highly visual imagery with which they can help us remember hard things.
*  Yeah, wonderful example.
*  Yeah.
*  Well, so that method also called the memory palace, I guess, technique uses visual imagery,
*  which is easy to remember to help people remember things that are harder to remember like sequences
*  of numbers.
*  So a real story, my actual cousin, when she was young, I asked her what her first memory
*  was and she told me she remembered being born.
*  And the way she described it was, you know, there's this light and then there's this pink
*  stuff all around and she goes toward the light and then she's born and she sees all this
*  stuff.
*  And what's striking about that besides that, I think she watched the movie Look Who's Talking
*  and took her memory from that, which is, dates me, I guess.
*  Yes, I'm with you.
*  Yeah.
*  What's striking is the all of her memory has to do with what she saw.
*  It's not the smell or the sounds and things.
*  Do you have an earliest memory?
*  Oh, goodness.
*  I do have an earliest memory of kind of running away from home when I was two years old.
*  And I do.
*  I can remember.
*  I think I just got lost.
*  Yeah.
*  Visually, I do remember the color of the truck and what the woman looked like, who picked
*  me up and brought me home.
*  And my mother was hysterical, but I remember it was a brown truck.
*  Yeah.
*  So I have this very salient visual imagery of wandering away.
*  It's visual.
*  But man, too, that is impressive.
*  I think my memory is really poor.
*  I don't have memories from that young.
*  I don't know that many people do.
*  Yeah.
*  No, it's a wonderful unsolved mystery about what happens because children can remember
*  things when they're children.
*  Right.
*  And then those memories seem to get overwritten.
*  Yeah.
*  It's a fascinating question that we still don't understand.
*  I guess your synapse is never pruned as you were growing.
*  But that would explain a lot.
*  Yeah.
*  All right.
*  Well, let's talk about visual memory here.
*  You have recently applied what you've learned about how brains recognize objects to how
*  those same neurons in brains could basically be used to remember the objects.
*  So I'll just ask you to start off.
*  What is visual recognition memory and what about it interests you?
*  Yeah.
*  So what is recognition memory?
*  I mean, the thing that interests me, starting with that question, is I'm really compelled
*  by the remarkable ability to remember the images that we've seen.
*  So a classic example, we can take you or any of your listeners and we can have them flip
*  through a big stack of photographs.
*  So for example, you know, thousands and thousands of images and we can ask them to look at each
*  one of those images.
*  It would take them hours or maybe several days to look at all those images.
*  And then we can test their memory.
*  And what we find is that subjects are remarkable at remembering images.
*  So for example, if you took photographs from the stack and you paired them with photographs
*  that they haven't seen and you gave them a memory test, just ask them, which one did
*  you see?
*  Subjects will perform on average over 90% correct on that task.
*  So memory is this remarkable form of learning that happens on single trials.
*  It happens with vast capacity.
*  And so that's really what motivates me to study this.
*  It's just a remarkable ability to remember images, coupled with the fact that we have
*  very little idea how our brains manage to support that type of memory.
*  So that's what we're trying to figure out.
*  So the task that you just described is kind of the same.
*  That task is used in studies of this kind of visual recognition memory.
*  One could potentially perform that, look through all those, you know, let's say 10,000 if we
*  go back to the 1970s study, you know, you look through 10,000, which is just a monstrous
*  thing to have people do in the first place.
*  But it was done and it's been scaled back these days, but still a lot of time and effort
*  is required to perform these studies.
*  I know.
*  Yes.
*  But I can imagine someone performing this task where, you know, you're shown two pictures,
*  one of which you have seen, one which you have not seen.
*  And I wouldn't need to necessarily exactly remember the picture to guess that that's
*  the one that I've seen.
*  I just would have I could have some sense of familiarity with it.
*  I know that there's this difference between familiarity and recollection memory in recognition
*  memory.
*  So what is that difference?
*  I mean, you know, and do we know what underlies it?
*  Yeah, yeah.
*  So there are two questions that we might want to talk about.
*  So yeah, so what is familiarity?
*  So I like to describe that experience that I think we've all had.
*  So you're walking down the street and you see someone and you say, oh, I know that person.
*  And sometimes you can have that experience absent any details, any ability to recall
*  who they are or how you know them.
*  You just can have that.
*  You just have that sense of remembering that percept that they're familiar.
*  So that's familiarity, the sense of remembering absent details.
*  And then sometimes what happens is a few moments later, you get this wave of details that come
*  back to you.
*  So who they are, how you know them, where you met them, that's recollection.
*  So that's the difference between familiarity and recollection.
*  Are they both grouped under episodic memory or declarative memory?
*  Yes.
*  I mean, yeah, yeah.
*  So the field has decades of very hot debate about whether or not familiarity and recollection
*  are two memory systems or one, whether they're supported by two different brain structures
*  or the same brain structure is familiarity, a weak form of recollection.
*  I think that there's some pretty strong evidence at this point to suggest that our ability
*  to remember the images that we've seen is supported by stuff that's going on in high
*  level visual parts of our brain in addition to a specialized structure called perirhinal
*  cortex.
*  And that's a distinct memory system from what's happening in, say, the hippocampus that's
*  supporting recollection.
*  Right.
*  Well, let's get into this memory in the brain and with objects.
*  So the rate code is an idea, it's an old idea of how neurons encode information.
*  It's old, like I said.
*  So it's essentially the idea that neurons spiking rate increases as you stimulate it
*  more with increasing stimulation.
*  And this goes back to Edgar Adrian, the first single neuron recordings, right?
*  And he was hanging weights from frog leg muscles that had been prepared.
*  And the more weight he hung, the higher the firing rate of the neurons were essentially.
*  And we've been using that as the rate code to understand how processes get encoded in
*  neurons ever since.
*  But the new thing, I say new, it's now sort of decades old, I guess, is population codes.
*  That things can be represented as distinct patterns of neuron firing rates within the
*  population, right?
*  So you studied object identity quite a bit now.
*  So how is object identity thought to be represented in IT populations of neurons?
*  And for a temporal cortex, I should say.
*  Yeah, yeah.
*  So object identity is exactly one of those representations we think of as being a pattern
*  of spikes coding scheme.
*  So as we know, the way information gets into our brains, visual information is through
*  And so that's going to activate a wave of activity across our brain.
*  So signals are going to propagate through these hierarchically arranged brain areas.
*  So V1, V2, V4.
*  And then eventually signals reach this brain area called infratemporal cortex, or IT.
*  And we think of IT as the highest stage of processing in the form processing pathway,
*  meaning that after signals leave IT, they are combined with other sensory modalities.
*  And so they go into association cortex.
*  But within IT, we have a lot of reason to think that that brain area is supporting our
*  ability to identify the objects that are out there in the world, and specifically to solve
*  what is known as the invariance problem.
*  So the fact that you can identify the same face or the same object as the same thing
*  despite different views you might see it in.
*  So it might be from different positions or background contexts or different sizes as
*  it moves closer to you on your retina.
*  And within IT, different objects will evoke different patterns of spikes across the population
*  for precisely the reason you said.
*  Some neurons are more selective for particular objects than others.
*  So some neurons might be more responsive to say a pencil and others to an apple.
*  And so that's going to evoke a different pattern of spikes depending on the objects that are
*  out there in view.
*  And the way we like to think about that is in a representational space, which is very
*  geometric so it makes it very intuitive, where we can think about each axis in that
*  space as the activity of a particular neuron.
*  So if we're working in IT cortex, we have say a 16 million dimensional space we're working
*  in and the patterns of spikes that are evoked across the IT population will correspond to
*  a vector in that high dimensional space.
*  And what we know about IT is when you look at different images that have the same content,
*  like the same objects in them, what you get are clusters of these response vectors in
*  similar locations at this high dimensional space.
*  So you can think about them, for example, as the population vector angle, those are
*  all going to be clustered together.
*  And so that's how we think object identity is reflected.
*  So looking at a hot dog from up above, looking at it down on the table versus picking it
*  up and looking at it on end before I take a delicious bite of it or something.
*  You got it.
*  Yeah.
*  Okay.
*  So very good.
*  So you have this vector angle in a, what'd you say, 16 million dimensional space?
*  Yeah.
*  Of course.
*  Easy to visualize.
*  Easy.
*  Very intuitive.
*  But then I brought up the old rate code idea because you found a different independent
*  mechanism could underlie memorability in this same population of IT neurons.
*  And I know it's not exactly the rate code that we're talking about, but it is the magnitude.
*  You know, how?
*  I'll ask you just how.
*  Yeah, how?
*  So yeah, so memorability refers to the fact that we systematically find some images easy
*  to remember and others we find easier to forget.
*  And so you can ask the question, well, what differs in the representation, in the visual
*  representation of those easily memorable versus easily forgettable images?
*  And so let's go back to our example of you have a bunch of different images of the same
*  object.
*  Let's say it's an elephant.
*  Okay.
*  And so it's an elephant and lots of different pictures, but some of those pictures are going
*  to be super memorable pictures of that elephant and others are going to be less memorable.
*  And so yeah, we went after this question and we found that the answer is remarkably simple
*  and elegant and that is it's the overall magnitude of the response.
*  So the identity is encoded in the pattern of spikes across the population or the angular
*  and the angle in this high dimensional space.
*  Whereas the memorability is encoded in the numbers of spikes coming out of IT or the
*  magnitude of this population response vector.
*  So one of the things that-
*  So two complementary coding themes.
*  Which is- So you wouldn't just at first, Blush, think, well, this is going to be the same
*  population of neurons that would encode both of these things.
*  What made you think, we'll just look in the same area as object identity and see what
*  we can pull out of it for memorability?
*  Yeah, yeah.
*  I mean, for us, we're really driven by the behavior at first, right?
*  So there's a behavior we're trying to explain and so we go to the neural correlate that
*  can account for that behavior.
*  And so the historical trajectory there was that this fascinating field of image memorability,
*  there's really beautiful work done there in human behavior and then in human fMRI.
*  And it was really the work of Wilma Bainbridge working with Odulliva that pinpointed high
*  level visual cortex in humans as being the locus for image memorability.
*  And so then the question was just, well, then how?
*  So that's where we went in and looked for how.
*  Yeah.
*  Well, so one of the first things, and I'm kind of going off of two recently published
*  papers in eLife here.
*  And by the way, Travis Meyer, who is on both these papers, used to have an office just
*  a few doors down from me in the Carnegie Mellon Institute.
*  Really?
*  You would tell me such a thing.
*  That's fantastic.
*  You should ask him if he remembers me because he was a postdoc in Carl Olson's lab.
*  And maybe he'll remember I beat Carl Olson in a ping pong match one Christmas and that
*  was a big deal.
*  But I don't know.
*  Yeah, yeah.
*  You've probably heard some Carl Olson stories.
*  Yes, I know Carl.
*  He's fantastic.
*  Oh, yeah.
*  You probably know Carl.
*  Yeah.
*  He's one of the godfathers of IT cortex.
*  Indeed.
*  Anyway, so one of the first things that you guys showed is that memorability could be related
*  to what's a phenomenon known as repetition.
*  Suppression in IT.
*  So how does memorability relate to repetition suppression?
*  Yeah, yeah.
*  No, that's a great question.
*  So what we've talked about so far is what differs in the visual representation of a
*  more memorable versus a less memorable image.
*  So how is when you see something for the first time, what happens in terms of its visual
*  representation?
*  But you can think about the question then, well, what happens next?
*  So how is that more robust visual representation?
*  How is that transformed into a more robust memory?
*  And so in order to answer that question, it's useful to first pinpoint that signal that
*  drives your sense of remembering.
*  So again, you're walking down the street, you see someone, you say, I know, I know that
*  person.
*  Where is the signal in your brain that's driving that perceptive familiarity?
*  And so we've been hunting around the brain trying to pinpoint that signal.
*  So we don't definitively know, but our working hypothesis now, which is supported by a considerable
*  amount of evidence at this point, is that it is this what the signal you referred to,
*  repetition suppression in high level visual brain areas like IT cortex and perirhinal
*  cortex.
*  And so what repetition suppression is, is it's a phenomenon we know exists.
*  So it's an adaptation like phenomenon where you get a really high fire rate response to
*  a novel image and then you get a decrement in the response the next time you see it.
*  So when it's familiar and the characteristics of this signal are remarkably well aligned
*  with everything we know about visual memory behavior.
*  So for example, repetition suppression is extremely selective for images, even after
*  you've seen many of them, hundreds or thousands of images.
*  It's still very specific to the images you've seen.
*  It lasts a very long time, even after you've seen an image only once.
*  And it seems to disappear at the same rate at which we forget the images that we've seen.
*  So they seem to be well aligned in many respects.
*  So the idea is you see the elephant or something and your IT population of neurons fires and
*  says, ah, elephant.
*  And then the next time you see the elephant, they say, oh, elephant, a little quieter.
*  And that's the repetition suppression.
*  Yes.
*  Yeah.
*  That's what it looks like.
*  And it is the case.
*  So going back to the question, well, how does this more vigorous response to the first time
*  you see something that's highly memorable, how's that transformed into a more robust
*  memory?
*  It is the case that that more vigorous response produces a larger magnitude decrement or more
*  repetition suppression than a less memorable image.
*  So these are all consistent.
*  Yeah.
*  So this was kind of the first study that you guys published about this that we're talking
*  about here.
*  And this has to do with seeing the image the second time, right?
*  And measuring how much suppression there is and correlating that with how memorable it
*  is.
*  Yes.
*  But then this idea of the magnitude of firing being on first viewing of an image being related
*  to how memorable it is is sort of this this what you guys explored in the second more
*  recent publication here.
*  Exactly.
*  Exactly.
*  So how is memorability then related to because I guess previous studies have not paid any
*  attention to the actual rate, the actual magnitude of firing rates to decode things like object
*  identity, right?
*  Yeah.
*  Yeah.
*  So I was I was really surprised.
*  It is the case that we the field at large didn't really appreciate that there was a
*  magnitude coding scheme associated within the class of natural images.
*  But if you're just trying to decode object identity, it doesn't really matter.
*  And if that doesn't really matter.
*  Right.
*  Yeah.
*  But you guys find that magnitude does indeed matter and it matters for memorability, right?
*  Yes, exactly.
*  So yeah.
*  So you could flip all of this on its head and you could say what we've determined is
*  that there's a previously unappreciated coding scheme that exists in IT, where some images
*  evoke higher population response magnitudes than others and that this magnitude coding
*  scheme does have consequences for cognitive processing downstream.
*  For example, it influences how well you're going to remember an image.
*  Yeah.
*  And presumably it influences other things as well, not just memory, but other downstream
*  processes.
*  Right.
*  Well, that's kind of my next question.
*  So I mean, you can picture this, you know, this vector, right, in a let's say a 3D Cartesian
*  coordinate system and it's got some angle where all the where its population response
*  points and then it's pretty natural to then be able to imagine that arrow growing and
*  shrinking and the direction of the arrow can encode what object it is and the growing and
*  shrinking can encode how well you might remember it.
*  But that's what I was going to ask is what else is hiding in IT responses?
*  Is there room for other information in there?
*  What else is hiding in IT responses?
*  It's a great question.
*  Not to cut off your thinking, but one of the reasons why I ask and this is a terrible,
*  terrible tangent because I have very, very informed notions in my head.
*  Is IT all about object identity?
*  Or I guess the bigger question is, is the ventral stream, is brain processing really
*  about identifying the objects?
*  Or is it, you know, could it be about something else on a much more fundamental level?
*  Is that a ridiculous question?
*  It is not a ridiculous question.
*  And I think that while identifying the objects that are in view is a really important problem
*  that has contributed like tremendously to our understanding of processing in the ventral
*  stream, I think that it has happened at the expense of appreciating that that's not just
*  what your form processing pathway is for, is to identify objects invariant to all of
*  the details that the details matter to.
*  And certainly the details matter for memory.
*  So one of the classic behavioral signatures is we don't just remember the objects we've
*  seen, but we remember a lot of detail about the configurations and contexts that we saw
*  those objects in and probably for good reason.
*  Right.
*  Yeah.
*  So that's not the ventral stream is not just doing invariant object processing.
*  It's doing a lot of other stuff as well.
*  Yeah.
*  Obviously the world is not, I mean, except for magazines and well, I guess these days
*  pictures on computer screens, but the world is not made up of static images, obviously.
*  Yeah.
*  But a lot of what is studied in the ventral stream and in IT is object categorization
*  recognition of static images.
*  And that's a lot of what is studied using convolutional neural networks, using these
*  deep learning networks as well.
*  And well, so you guys actually used and you're part of the story of convolutional neural
*  networks becoming this huge tool in neuroscience.
*  You guys tested this hypothesis that, you know, these signals that you see in IT relate
*  to memorability by testing it in these convolutional neural networks.
*  And it's pretty interesting.
*  Do you want to just describe how you tested it and what you found?
*  Yeah.
*  Yeah.
*  So the question we were asking is having identified population response magnitude as a strong
*  correlate of memorability.
*  We were interested in tracing that back to its origin.
*  So you can ask the question, does this emerge from a system that's been wired up to see
*  or does it require that you constrain the system to also remember what it's seeing?
*  So is it due to the optimizations required for visual processing or for memory?
*  And so we started by just probing deep neural networks that have been trained to categorize
*  objects.
*  So as you and I'm sure many of your listeners are probably aware of this really great literature
*  by, say, Dan Yemens and Jim DiCarlo and Nico Cringascorte.
*  I've had Dan and Nico on the show.
*  Yeah, that's fantastic.
*  That's fantastic.
*  Yeah.
*  So in that work, what they have done is they've trained deep nets, so convolutional neural
*  networks and variants of that, to categorize objects.
*  So just to take images and put tags on those images.
*  And they train those computer models to perform object recognition.
*  And then they compare different layers of those deep neural networks to representations
*  in the brain.
*  And they find some really nontrivial alignments between what's happening in the deep nets
*  and what's happening in brains.
*  Yeah, the story is that convolutional neural nets provide the by far best account of the
*  neural responses in brains.
*  And I would agree with that completely.
*  Yes, for sure.
*  So we asked the same question.
*  Well, now let's just take those same deep nets that have been trained just to do object
*  categorization.
*  And I want to emphasize these networks cannot remember anything.
*  They'll respond exactly the same way to the first time they see an image and the second
*  time and the millionth time.
*  These are once the training has been fixed, these are static processing machines.
*  They also haven't been optimized to predict memorability in any way.
*  But those same networks naturally not only predicted the images that would be most memorable,
*  but they did it via the same coding scheme that we found in the brain.
*  So if you looked at higher layers of these networks, places that are analogous to infer
*  a temporal cortex, we found that those layers responded more vigorously with higher magnitude
*  responses to some images over others.
*  And those images that they responded the most vigorously to are the ones that we find most
*  memorable remarkably.
*  It is remarkable.
*  Yeah.
*  Yeah, it's remarkable.
*  And I think it really, it's not just remarkable, it's insightful as well, because it tells
*  us a lot about what this memorability phenomenon is and what it isn't.
*  So for example, you might speculate that the reason that certain images are more memorable
*  is because they grab your attention.
*  Or you might say the reason that it's more memorable is because it produced some sort
*  error, I think, insofar as if you wire up a system to categorize objects and it recapitulates
*  this phenomenon, you might argue that whatever a system that's wired up to process objects
*  does, we might call that sensory processing and that these other phenomenon might be just
*  kind of explained away, demystified in that sense and that attention and predictive coding,
*  you might argue belong to other realms of explanation, not just this one, for example.
*  Right.
*  So I think this is an example of CNN making an important contribution of demystifying
*  how the complexity of the brain works.
*  And so I think that that's what's been satisfying to me.
*  Well, it's, I mean, it is, it's satisfying.
*  I mean, so, you know, CNNs, by and large, these days are still like feed forward only
*  and cognitive functions you were just talking about, like, you know, well, or reward prediction
*  errors, attention.
*  A lot of those things are thought of to be can be top down processes, right?
*  Yes.
*  Recurrent neural networks cause all sorts of math trouble and interesting dynamics and
*  very interesting possibilities.
*  But I mean, so what do you think?
*  Is recurrent activity in networks that overhyped or is it just useful for other things like
*  top down processing or or does it mean that vision and in this case, memory or memorability
*  is just less interesting or more fundamental or what?
*  What does it mean?
*  Yeah, no, these are all great questions.
*  I mean, you know, one of the things that I find really striking about the signals that
*  we've just been talking about, so we've talked about three different types of representations
*  so far, object identity, memorability and memory.
*  Those three signals are actually staggered in time in IT cortex.
*  So strictly, a CNN can't account for that aspect of what the brain is actually doing.
*  So what we see is if you present an image, you get a delay between the time that that
*  image is presented and the time that the signals arrive in IT cortex is about 80 milliseconds.
*  And it's only about 40 milliseconds later that you get information about memorability.
*  So in that first feed forward wave, you don't have any information about the images that
*  are going to be the most versus the least memorable.
*  That arrives about 40 milliseconds later.
*  I did not.
*  And at that point, you don't have any information about whether you've seen something before,
*  yes or no.
*  That arrives yet 40 milliseconds later still.
*  So these things are in fact staggered in time.
*  So the brain is certainly reflecting these signals, but reflecting them in a very dynamic
*  way and to really explain or recapitulate what the brain is doing, we're going to have
*  to account for that recurrent processing as well.
*  But at first pass, you still see that the magnitude of the responses in your current
*  and your convolutional neural network do reflect the memorability in these later IT like stages,
*  right?
*  And yes.
*  And like you said, I mean, it's remarkable that these were trained just to categorize
*  objects, not to remember the objects.
*  It would be trivial to train a convent to unmemorability, right?
*  You were just, you know, did have I seen it or not?
*  That would be a trivial matter.
*  And I imagine the artificial unit responses you'd see would be quite different.
*  Well, so that's there is a neural network that's remarkably good at predicting what
*  images will be most memorable.
*  It comes out of Oud Olav's group at MIT, it's called MemNet.
*  And what they did is they started with a version of AlexNet that had been trained not only
*  on objects, but also scenes.
*  And they found that was already a really good predictor of image memorability.
*  But then they topped up this training to be even better.
*  And then that does perform at the noise ceiling of like human memorability scores.
*  So yeah, so you're right on both counts, right?
*  You get almost there with a deep net and then you can get a little bit better by doing something
*  else.
*  So you'll learn Nicole.
*  I'm right on all accounts.
*  You know, it's my podcast.
*  I get to know.
*  I wish that were the case.
*  But so.
*  Surveyed a lot of the videos.
*  Yeah.
*  They're becoming really the standard way, almost to test neural hypotheses, since like
*  we mentioned, they match neural data better than any other model that's been tested essentially.
*  And like I said, you're part of this story of the rise of, you know, CNN through like
*  Jim DiCarlo's lab and others as a tool in neuroscience to understand perception, sensation.
*  You know, what are your thoughts on sort of the state of CNNs as I don't know, are they
*  a gold standard yet?
*  Are they considered a gold standard?
*  Well, I mean, I think there's a strong argument to be made that their existence doesn't amount
*  to understanding.
*  Yes.
*  Insofar as, you know, it's it's amazing now that we have computer models that recapitulate
*  how the brain works to some extent, to some extent, that it's, you know, they're doing
*  a pretty good job at this point.
*  But having a new thing that you don't understand, you would also argue is not much more useful
*  than having the first thing that you don't understand, aside from the fact that presumably
*  it should facilitate our ability to figure out how the CNNs work.
*  And I would argue there's a lot of work to be done there.
*  That this is a tractable problem that we should attack.
*  And yeah, that's the next the next phase of research that's going to help us understand
*  how the visual system works.
*  And we do not understand that.
*  And having a CNN does not amount to understanding.
*  We need to figure out how the CNNs work now.
*  Yeah, I'm going to I'm going to have Nico on again pretty soon.
*  We'll go down that road a little bit.
*  But your take then, are we anywhere near the limits of the usefulness of using these deep
*  learning networks like CNNs to understand how brains work or at least perception?
*  I mean, I think there's just really exciting work also to be done, you know, in broad strokes
*  on using those as a front end to understand, you know, the even deeper parts of the brain,
*  you know, executive function, memory, how do memory and perception interact with one another?
*  Right. So we want to take the CNNs and build on those to understand even, you know, more
*  awesome processing beyond basic sensory perception.
*  Throw some throw some other even more complicated neural networks that we won't understand on
*  top of each other and see what we get.
*  What's your general experience about how neuroscientists?
*  I know you run in a crowd that's probably very pro deep networks to understand brains and
*  things like that. But I don't know what's your experience about how neuroscientists feel
*  about things like convolutional neural networks as models of visual perception?
*  Are people skeptical?
*  Yeah, I mean, I think that there's there's skepticism on different levels.
*  I think, yeah, there are the hardcore, you know, deep netters that I wouldn't call myself
*  a part of who really argue that the deep the existence of the deep nets themselves and
*  the fact that we can picture what the brain is doing amounts to understanding, right,
*  that you have now the architecture, you have the optimization principles, you have the
*  learning algorithm, that that is understanding.
*  I think there's that crowd and that's a rare breed, but they definitely exist.
*  And then there there's the little bit more middle of the road.
*  And I would include myself in that camp who thinks like, wow, they're an awesome tool,
*  but they're just another tool in the toolbox.
*  Right. You know, are they that much more useful than my electrodes or my behavior?
*  No. I mean, it's just, you know, it's one of these tools that all together can help us
*  solve this problem.
*  I think it's pretty rare these days to encounter someone who is a complete skeptic and
*  sees that they have no role whatsoever.
*  But I think there are there are there are also good arguments that they could be vastly
*  improved by making them more biologically realistic, for example.
*  Right. Yeah.
*  And so I think Eero Simoncelli at NYU has some really beautiful examples of that.
*  You know, you can recapitulate in a very deep net.
*  You can recapitulate the same thing it's doing by a few shallow layers if you just
*  include things like divisive normalization or gain control.
*  So we might argue that that's like a more efficient shallow net is better or equal to
*  a very deep net.
*  You know, yeah. Since we're talking about convolutional neural networks.
*  So there's the sort of ongoing tension between A.I.
*  and neuroscience. I don't really want to call it a tension, but there's just different
*  rates of progress, let's say, in the A.I.
*  world. Right. Where in archive you have 10,000 papers every day coming out with a
*  different tweak of a network and different implementation and does different things.
*  And then from the A.I.
*  side, they'd probably expect, OK, now you and neuroscience now test this.
*  And it's just slower in neuroscience.
*  Is this a problem or is it an opportunity?
*  You know, how do you view these different sort of rates of A.I.
*  and neuroscience progress?
*  I mean, you're not tempted like you.
*  You don't like read an archive paper and think, oh, I've got to implement this tweak
*  into my network to test it against my data.
*  Things like that. Right.
*  Yeah, I mean, I think building systems, engineering is fundamentally different than,
*  you know, neuroscience.
*  I think that, yeah, doing experiments and collecting that whole arc from behavioral
*  to neural data and doing sophisticated analysis on it right now.
*  Yeah, we're we're in a state in which it just takes a long time.
*  I mean, we will spend as we will spend more time analyzing our data than we'll spend
*  collecting it. Right. The bottleneck is not really even in the experiments.
*  It's in the trying to wrap our heads and understand what's going on once we get the
*  data on the hard drive.
*  Yeah. But experiments take a long time.
*  So that's even sadder.
*  Yeah. No, I mean, I mean, we're dealing with difficult problems.
*  I mean, it's wonderful.
*  You know, the new the new things that are happening in neuroscience to speed all this
*  up. But really, they're not speeding it up.
*  What they're doing is they're allowing us access to the data we always wanted to have.
*  Right. Like, right.
*  We're getting massive data sets now, which is really exciting and is allowing us to do
*  all sorts of things with it.
*  Yeah. So it feels a little bit apples and oranges to me.
*  I mean, I understand why engineering is moving at the rate it's doing.
*  And I think they shouldn't slow down.
*  They should, you know, keep keep doing that.
*  And but we can't keep up with that because there's just no way.
*  But there is. And sorry, this is kind of a large tangent and we'll move on in a second.
*  So there is the engineering push, and that's to solve problems and make the world a better
*  place. But there is still a core push in a I, at least from its origins.
*  And I would argue still today, a core part of a I is understanding minds, is understanding
*  intelligence in general.
*  And they're not they.
*  AI engineers, people who work solely with neural networks and categorizing things, doing
*  speech recognition, they're not bound by the same questions of is that actually how
*  it works in brains or can we make it work and then create this shiny new toy that then
*  could be used as a model to understand how we think?
*  Did I ask a question? I didn't even ask a question.
*  So, well, I'm curious.
*  So I think that's where the crux of the disparity in rates of progress comes in.
*  I don't know, I think I'm just jealous of the AI world that they can just make models and run
*  free. You know, yeah, yeah, yeah, yeah.
*  The robots. Yeah, it's going to work or it's not going to work.
*  The algorithm works or it doesn't work. Right.
*  And if it does something interesting, then that's great.
*  Right. Yeah, I agree.
*  There's something I think we're both having a hard time verbalizing in terms of just the
*  difference in science versus engineering, the difference in building something versus
*  trying to discover something.
*  Yeah. Yeah. I don't have good words for that either.
*  Right. Yeah.
*  Maybe I'm trying to verbalize without denigrating anyone.
*  So there you go. Exactly.
*  Yeah. OK. So different.
*  Different. Yeah. More is different.
*  So the idea of visual memory and image memorability and how it's reflected in brains
*  leads into your recent ideas about how visual novelty could be used as a mechanism in
*  brains and in machine learning, specifically reinforcement learning for intrinsic
*  reward, which you detail in this current opinion of neurobiology, neurobiology piece,
*  which is titled Visual Novelty, Curiosity and Intrinsic Reward in Machine Learning and
*  the Brain. Nicole, why do machines and or animals need to encode novelty?
*  Yes. So this is an example of myself and my group getting a lot of inspiration from
*  what's been happening in AI and machine learning.
*  And so asking ourselves, just taking a step back and asking ourselves, we initially
*  started the investigation of visual memory just motivated by the fact that we're amazing
*  at remembering the images that we've seen and that in and of itself, it was just a
*  behavior we want to explain.
*  But you might want to take even a step further back and ask yourself, well, what do we
*  do with that amazing ability to remember images?
*  Like, what's it for? What do we use it for?
*  And there, I think machine learning has some really interesting things to say that build
*  on some observations that I think are classic observations.
*  And that is if you have a really effective memory system that can report to you what
*  you've seen before, the flip side of that is you also have a really good novelty indicator
*  that tells you what you have not seen and that novelty or the preference for looking
*  at or being attracted to novelty, you might call that curiosity, is a really effective
*  way to drive efficient exploration for learning.
*  So imagine, for example, you're a baby, you're trying to learn about the world instead of
*  just looking randomly about your world and encountering half the time things you've seen
*  before and the other half of the time, things that are new to you.
*  You might want to preferentially explore the things that you have not seen.
*  It's a more efficient way to learn.
*  And that is, in fact, exactly what babies do.
*  So babies will preferentially view things that are new to them.
*  It's a behavior that we see ubiquitously across all animals and it's been documented for
*  over 100 different species, including turtles and dolphins and sheep and monkeys and
*  everything else. So in machine learning, the way that this has been formalized is by
*  building on classic reinforcement learning.
*  So the way classic reinforcement learning works is it's completely reward driven.
*  So the value. So when trying to decide between two different options, things to explore,
*  the value of those different options is computed based on the amount of reward that's
*  anticipated to be associated with each of them.
*  And so you're going to choose the more valuable option, the one that gives you more
*  reward. Now, this type of classic reinforcement learning has been hugely effective and
*  very insightful in figuring out how biological creatures and machines might and can
*  learn. But it's also known to be ineffective in certain situations.
*  For example, when almost everything is new and you don't know anything about the world
*  or when rewards are very sparse.
*  So it's really hard to drive and drive a system to learn that way.
*  What's been going on in reinforcement learning is extensions of classic reinforcement
*  learning to incorporate novelty considerations.
*  So now computing value, not just based on how much reward a particular option is
*  anticipated to give you, but a combination of reward and the intrinsically valuable
*  experience of novelty or curiosity.
*  And so by combining those two things and different weighted contributions, you can drive
*  an agent to learn, for example, an artificial agent to learn how to play an Atari video
*  game. And under a bunch of different scenarios, it's a more effective way to drive
*  the exploration required for learning.
*  Or to get a human to not drop out of grad school, but continue forward.
*  And yes, when rewards are sparse and everything is new.
*  Exactly. Exactly.
*  Curiosity. Yeah, must be intrinsically motivated.
*  Yeah. So so it's pretty straightforward, like you said, how to encourage exploration or
*  curiosity. I mean, you have this reward function that an algorithm can do.
*  Maximizes in reinforcement learning and and you just add novelty as an extra reward term in
*  the equation. Balanced by some bells and whistles that you mentioned.
*  Yeah. But to do that, the agent actually needs to know if something is novel or whether
*  it's been in this particular state before.
*  And at first blush, it seems easy to do right.
*  Seems easy for like an agent, especially an artificial agent to keep track of states just by
*  counting. So, you know, for example, you know, if if it's been at the annual SFN conference
*  before, the agent would would know, ah, this is neither novel nor good.
*  I should do something else.
*  It would think right. But it's it's my dig at SFN.
*  But it's not it's not so simple.
*  So you know, it's not simple.
*  Right. Well, keeping track of things is not simply.
*  SFN is not simple either.
*  You point out there are hurdles to overcome for the agent to really know if, you know, if it's
*  revisiting the same state or if it's in a novel state.
*  So what are those hurdles and how can reinforcement learning algorithms overcome them?
*  Yes. So the hurdles have strong analogies to the sorts of things have been tackled for
*  solving the problems of visual object recognition.
*  And they are the host of invariance problems.
*  So, for example, in order for an artificial agent who receives pixels on a video screen as input
*  to convert that into some estimate of whether or not a particular state or location in a video
*  game has been visited before, they have to solve the problem, which is often referred to as view
*  invariance. So they have to appreciate that different pixel patterns can correspond to the same
*  state or the same location in the game.
*  Another type of invariance that's incorporated into these machine learning algorithms is what we
*  might call state invariance.
*  And so this is an appreciation that there might be kinds of states that might have similar
*  characteristics and that so from you might imagine that all hallways that are green lead to
*  dead ends. And so if you see another green hallway, it's not worth exploring, but a red hallway
*  might be even if you haven't been down that particular green hallway before.
*  So that's state invariance.
*  And so, yes, so the way that these systems deal with this issue is they train up typically deep
*  neural networks to solve these two types of invariance problems and then order to compute the
*  novelty of a particular state or option that's before them.
*  I guess these are called pseudo counts is a name given.
*  Yeah, so the first generation really was a count based approach, which really counted the number of
*  times a state or a type of state had been visited.
*  And so the new generation performs pseudo count type operations.
*  And the difference and the advantage of pseudo counts over counts are that pseudo counts are
*  probabilistic estimates of the probability that that is a novel option before you based on
*  everything you've experienced up to this point.
*  And that allows for and facilitates generalization to new things that are similar to the
*  things you've experienced. Right.
*  So it's not a binary have I seen this?
*  Yes or no. But rather, it's a continuous estimate of novelty.
*  And so OK, so we start off the show by talking about how memorability could be encoded in
*  brains. And that includes novelty, essentially, because the more novel something is, the more
*  you're going to remember it.
*  And now we're talking about novelty and in these mechanisms in machines and using pseudo
*  counts. Is there a way to compare these two things?
*  I mean, so it's your contention that we can bring these two ideas together and learn
*  something and move forward.
*  How's that? Yeah, I mean, so yeah, so we're very inspired by again, going back to like the
*  foundational question. We're amazing at remembering the images that we've seen.
*  We're amazing at detecting things that are novel.
*  What do we use that for?
*  Perhaps we're using that for the learning required to guide exploration.
*  Can that give us any insight into how novelty and familiarity are encoded in IT cortex?
*  Like, why do they have the properties that they do?
*  And what we do see is a lot of inspiration and things that make us rethink how IT cortex
*  is operating. So, for example, we also see like these pseudo count like approaches, we see
*  somewhat unsurprisingly, continuous estimates of novelty as opposed to discrete ones in the
*  brain. Right. So IT cortex signals not only whether something is novel or familiar, but for
*  example, recency.
*  So how recently you've seen something before.
*  So if you've just seen it, you get this really strong familiarity signal.
*  And if you it's been a long time, then that signal weakens.
*  We also have representations in IT cortex of individual neurons aren't themselves
*  invariant detectors of object identity, but it's really the population as a whole by
*  which you get this object identity based representation.
*  And we see in IT cortex also that the novelty signal is not an invariant novelty signal
*  for object identity, but rather there's a lot of information that's rich about the
*  particular images that you've seen.
*  So if you saw an object in a particular configuration or context, IT cortex also signals
*  that. And that's the thing that we can begin to link to some of the machine learning type
*  approaches where you can imagine if an agent's playing a video game, it's not really
*  effective to have a novel object detector.
*  Right. That's not really going to help you learn how to play an Atari video game.
*  Right. Because it's not that apples are associated with states.
*  So it's more scene based.
*  It's more more of a holistic account of, you know, have you been at this state before?
*  But it's also and it's important to say that in IT cortex, we also see generalization
*  across, for example, views.
*  So you do see to some extent that different views of the same object, you will get some
*  generalization of this novelty signal, but you'll still have information about whether you
*  saw that exact pixel pattern before.
*  Right. So IT cortex seems to be doing lots of different things in complicated ways.
*  And this works helps us understand or conceptualize what it might be doing.
*  Yeah. This I mean, this goes back to my thought about, you know, my question of whether
*  object recognition is is what IT is doing, right?
*  Because it's always doing it in the service of something.
*  And whether I whether object recognition could actually just fall out of whatever it's
*  doing in the service of whatever it's doing.
*  This actually reminds me of Tonya Conkle's work to whom I had on the show and the
*  looking at the visual stream orthogonally.
*  And basically, you know, she showed that objects can be are grouped in the brain based
*  on whether they're small or large or animate.
*  And and this kind of maps onto this work.
*  It's fantastic. Yes.
*  Her work is absolutely fantastic.
*  Yeah, it's fun. But it's all based on, you know, then essentially what the thing that
*  you're categorizing is actually useful for.
*  Right. Yes. Navigation or eating or whatever running from or handling in your hand.
*  And and that way of looking at it is, well, it's an orthogonal way essentially of
*  looking at it where the object categorization recognition then almost kind of falls out
*  of the purpose of the thing that the process that you're I mean, I'm just using all
*  sorts of words here that don't mean anything.
*  But but so, yeah, I'm wondering how you know how you view then the role of I.T.
*  with within that realm of, you know, if it is, is it is the core thing that is doing
*  object recognition or is it helping animals behave and object recognition falls out of
*  that? Does that make sense?
*  Yeah, yeah. I mean, we could we could frame the question a couple of different ways.
*  We could ask what are the optimization principles by which, you know, evolution tried to
*  wire up the visual system?
*  One one piece of work that I find really interesting and insightful is the recent
*  work of Dan Yam and Scroop at Stanford has been taking on the problem of how is the
*  visual system actually wired up?
*  So as compelling as all of the deep stuff is, we also know that it's highly
*  nonbiologically realistic insofar as it requires millions and millions of labeled examples.
*  Right. So here's a picture of a ball you label with ball.
*  Here's a picture of pencil. It's labeled pencil.
*  And we know that there's no way that a baby is going to experience that many labeled
*  examples in a lifetime.
*  The parents are going to give them a few.
*  Yeah, exactly. But they're not going to give them millions.
*  And so there's been an idea floating around for a while that the visual system might be
*  wired up via some form of unsupervised learning.
*  But nobody's really figured out how to get that to work robustly.
*  And that's where Dan Yam and his group have made some really important progress by
*  optimizing a deep net to wire itself up via unsupervised learning through a process that
*  they call local aggregation.
*  And we don't have to get into the weeds of the details, but basically it's a clustering
*  algorithm. And what I find really compelling about it is not only one does it work,
*  so this network performs really well at classic state of the art computer benchmarks,
*  it also wires up a system that bears as much resemblance to the visual system as any
*  other network wired up via backprop does.
*  But this algorithm also relies on having something like a familiarity memory bank.
*  So it does store memories of what it's seen so far in the process of forming these
*  aggregates in these clusters.
*  So to flip all of this on its head and to answer your question in a very indirect way,
*  one might postulate that what the visual system is actually doing in the process of
*  visual development is implementing some sort of form of local aggregation that
*  incorporates memories of the things that it's seen.
*  And what emerges from that are the properties of the visual system that include clustering
*  for objects of different identities, but also relies on memories.
*  And naturally, what emerges is memorability.
*  So it starts to tie all these things together in compelling ways that I think we're just
*  beginning to scratch the surface of understanding.
*  But I think you're on to something that all of this is really related to one another.
*  And it's not about labeled examples and optimizing for object recognition.
*  There's something else going on there that's really important.
*  Even if that something else is more fundamental or core, it's still really impressive that
*  you can train a deep net on object categorization and then have things like
*  memorability fall out of that, which is pretty interesting.
*  Yeah, I agree. I agree.
*  Yeah. And a huge contribution that we can do that now.
*  Right. That's an amazing development since I got into this field 15 years ago, you know,
*  into object recognition specifically.
*  Right. It's just it's a wonderful, wonderful development.
*  Yeah, we can all agree on that.
*  When you were describing that work that Dan is pursuing, you used the term familiarity
*  again. And, you know, it's hard for me to wrap my head around the idea that AI agents
*  are also limited by the same, essentially the same resources that our brains are limited
*  by, although the limit is much higher.
*  Right. And so it's hard for me to wrap my head around the.
*  The idea that an AI agent would need familiarity over just perfect recollection.
*  Like, why would why would an AI agent not recall perfectly?
*  Why wouldn't you build that into an AI agent?
*  Yeah, I don't have a good answer for that.
*  I don't know. Certainly, you know, you you you emphasize that it must be the case that
*  having this low bit familiarity tag, if what you're trying to extract is novelty, having
*  that low bit information is a very efficient way to store novelty.
*  It's going to be a very fast way to recover novelty.
*  And it's going to be a really good way to do it if you have efficiency constraints or
*  you're limited in your resources, whether or not AI is going to need it or not.
*  I think, you know, yeah, the question is, I don't know.
*  I don't know whether that's going to be true or not.
*  Yeah, I just had Tom Griffiths on the show and, you know, he uses this resource rationality
*  framework to investigate these sorts of things.
*  And one of his ideas is that if you build a system with limited resources, like we are
*  limited, the efficiency with which we work and the, you know, the limits that we have,
*  you might actually then get some sort of generality that we have.
*  And it's really unknown, like what you would get if you just lifted the top off of all
*  of the resources, like what would fall out of it.
*  And so so our limits could actually constrain the constraints of imposed by our limits
*  could actually, you know, lead us to this generality.
*  But anyway, so all this is tied together.
*  Beautiful stuff. Well, so, so, you know, this is kind of a review and in the current
*  opinion in your biology, are you are you guys pushing forward with it?
*  What's going on? Yeah, so, yeah, so we're trying to we're trying to think about, like,
*  what's the right experiment to do?
*  Right. So minimally, we would love to have a behavioral paradigm where we can actually
*  trade off, for example, the intrinsically valuable experience of novelty with external
*  rewards. Right.
*  And so in order to trade those things to things off.
*  So how do you quantify that behaviorally, how valuable novelty is?
*  And then we're interested in where novelty and reward are integrated in the brain.
*  And there's a good reason to think that's probably the same place housing
*  representations of novelty peri-renal cortex.
*  So it's vastly underappreciated that peri-renal cortex receives this giant dopaminergic
*  input that those of us who work in peri-renal cortex kind of whisper about, but nobody
*  really understands very well.
*  And so I think it's a very likely the case that the same place that is storing
*  representations of the things that we've seen is also integrating that information
*  with external rewards in order to compute a holistic estimate of the value of a
*  stimulus. So that's my pet hypothesis right now.
*  And so that's a hypothesis that we're starting to figure out and ask ourselves, how
*  could we test that?
*  That's great. Do you guys whisper about it because you don't want other people to
*  jump in and compete or do you whisper about it because it's unknown?
*  It's more just like, oh, it's so giant.
*  What's it doing? What do you think it's doing?
*  Right. You know, I think it's more of a whisper along those lines.
*  It's trying to get ideas from one another.
*  Have you ever observed anything?
*  You know, what have you seen?
*  Yeah. How could we go about this?
*  It's more of that.
*  That's cool. You don't often think of, I mean, so there are hot areas in the brain,
*  right? They become, you know, like right now, like grid cells in hippocampus.
*  That's you win a Nobel Prize and then everything, everybody just follows suit and
*  studies those. And that's the key to the brain.
*  You know, so but but the uncharted territory is running out in the brain.
*  Right. So it's cool to that there are still there are still plenty of areas that
*  it's it's really uncharacterized, unknown.
*  That is true. There are still plenty of areas in the medial temporal lobe, perirhinal
*  cortex, parahippocampal cortex.
*  I agree. Enterontal cortex and the hippocampus are starting to be less sparsely
*  populated.
*  Yeah, there are still places.
*  Yeah.
*  So this is great, Nicole.
*  I I wish you luck moving forward here.
*  And do you mind if I open it up to sort of more more general questions?
*  Yeah, that's great. Yeah. Happy to.
*  Do you have like some sort of neuroscience, something that's known in neuroscience
*  that you think would benefit A.I.
*  that is not currently being appreciated in the A.I.
*  world or it's being appreciated, but maybe used the wrong way or something like
*  that?
*  The one the one example that comes to mind is an example about future predictive
*  coding.
*  So so there's a lot of really great work in A.I.
*  going on right now in terms of predictive coding and namely in the realm of, for
*  example, LSTM.
*  So what what we know about predictive coding is that in order to predict what
*  will happen next, which is a fundamentally important problem, you have to have some
*  understanding of the statistical structure of the world, right?
*  What things follow, what other things, what's correlated with what?
*  And you also have to have a memory of what's happened recently that you can then
*  extrapolate on into the future.
*  And so I think that in A.I., those memories of recent history have typically had
*  analogues to what's going on in terms of persistent recurrent circuitry in the brain.
*  So that's an activated working memory.
*  One of the things that I've been very compelled by is the work about future predictive
*  coding in the retina, which uses a fundamentally different type of circuit in order to
*  store memories of recent history that then can be extrapolated.
*  And the types of computations in terms of future predictions that happen in the retina
*  are really important, for example, to when you're trying to catch a ball, your brain has to do
*  something called leg compensation.
*  So if you just do the delay between the visual world and the latency of the activation of
*  your retina, if you put your arm out at where you see the ball at any where your retina is
*  activated at any one point in time, you're going to miss it by meters if a ball is moving, say,
*  at 100 kilometers an hour.
*  So your brain has to fix this.
*  And we think that the retina does some work to fix this.
*  And one of the ways it does future visual prediction is by simple feedforward adaptation,
*  as opposed to a so that's how it stores memories of what's happened recently.
*  And stacks of that very simple feedforward computation have proven to be really valuable
*  for predicting future events, at least under some circumstances.
*  I've never seen this type of thing employed in AI.
*  Maybe I'm wrong.
*  But usually, future predictive computation in AI, it's much more complicated than that.
*  It involves something like an LSTM or a more complicated piece of machinery than that.
*  Yeah. So an example, simple computations, really powerful output.
*  You're all about this adaptation, habituation, repetition, suppression.
*  I mean, this could be how we encode time as well, for instance.
*  Yeah, yeah.
*  That's interesting.
*  Really simple mechanisms.
*  Like I said, you've had this, you know, career in visual neuroscience, but things change.
*  You know, I remember how naive I was going in to graduate school and even just as a technician before that.
*  Is there something that you can think of that you've changed your mind about through your career?
*  I think the biggest changes of mind, I mean, aside from, you know,
*  just being completely exposed to new questions that didn't even exist.
*  The biggest changes, the most fundamental changes across my career have been just the appreciation
*  for how rewarding and how challenging being a good mentor is.
*  Oh, yeah.
*  Yeah. So I did not appreciate that when I was a mentee.
*  You probably appreciated how poorly it could be performed at some times.
*  I had such great experiences with my mentors.
*  I look back and I just feel so fortunate.
*  And you didn't know how good you had it, huh?
*  And I now can appreciate what a challenge it is, but also how rewarding it is to invest in it.
*  And, you know, if you can take good people and help facilitate the bringing the best out of them.
*  But it's a huge responsibility.
*  You know, when you have a mentee, there's a big responsibility on your shoulders, right,
*  to minimally don't screw them up.
*  Ideally, bring out the best in them, right?
*  And that means it's a lot of it's challenging.
*  And so far, there is no one right mentoring style.
*  Every mentee is a unique individual who has a unique set of needs.
*  Right. And so, yeah, yeah, it's something I did not appreciate.
*  It's depth and breadth.
*  When I was when I was younger, who was one example of a mentee that you really screwed up?
*  No, I'm just kidding.
*  So I made the joke earlier about needing we were talking about the scant external rewards
*  that you get when you're in graduate school as a faculty member.
*  Since since I opted out and never got there, right, people have to keep their eyes on the prize
*  and become a faculty member and tenure and all that stuff.
*  Are the external rewards more frequent as a faculty member with with the mentoring?
*  And or or is it even less frequent?
*  Um.
*  And there's a bias here because to get to where you are, you have to be highly
*  intrinsically motivated anyway and not give a damn so much about external rewards.
*  Yeah, no, I mean, there's.
*  I'm trying to very succinctly answer your questions because it's really it's a very big space.
*  So on one hand, insofar as science is about.
*  Big gains and, you know, but we set a high bar, so many rejection.
*  Yeah, yeah, the grand of the vision.
*  You're going to experience more gains, but more rejections as well.
*  Right. And so there's some asymmetry there.
*  So you better be able to take it.
*  Yeah, so you're just it's just more of that stuff.
*  So on one hand, because you get to be involved in so many different projects, right,
*  it's hopeful that at least something's working at any one time.
*  Right. So you're not going to suffer that same hit as you suffer when you're a graduate
*  student or a postdoc. And, you know, if you have one thing going on and it's going well,
*  or it's not going, you know, and so so you have to be really resilient to the downs, to
*  see your way up to the ups.
*  When you're a faculty member, you know, there is some benefit to hopefully something's working
*  at any one time. If not, everything is working.
*  You got something you can point to at the same time.
*  There's a lot of some things that aren't working.
*  There are a lot of rejections and things. Right.
*  You know, so you do have to keep your eye on the it's all going to be good in the end.
*  Yeah. In some sense, I think one of the most valuable things that I took away from
*  graduate school and graduate school is not the only, you know, venue because there's
*  postdoc and multiple postdocs, et cetera.
*  It's just not celebrating being able to celebrate failure, but really being able to take it
*  and move forward. And I think it's such a valuable skill to learn if you can call it a skill.
*  For sure. Yeah. That resilience, that ability to celebrate the successes of, for example,
*  civilian paper. That's one of my favorite times to celebrate.
*  Like if we can get to the stage that we think, you know, that we've completed the project,
*  let's celebrate that moment. Right.
*  After that, it's a little bit out of our hands.
*  There's a lot of noise in the system.
*  It's going to be a tough road, but let's celebrate that moment.
*  And then let's have each other's backs on all the moments going forward.
*  And then there's, of course, the big celebration at the end.
*  Right. When the world gets to see it.
*  Yeah. In my case, that that in celebration, when it drags on for two and a half, three
*  years, though, it's hard to.
*  It is hard. A lot of people I've had on the show have said that math is the most important
*  skill to learn for someone wanting to get into neuroscience and AI.
*  Do you agree with that? And if so, I mean, linear algebra is the one that everyone says
*  points to, to being the most important.
*  But, you know, what do you see as the most important skill, whether it's math or not?
*  Yeah. I mean, I would rephrase it a little bit and I wouldn't say math.
*  I would say quantitative training.
*  OK. Which comes, I think there's an arm that's mathematical, but there's another arm
*  that's more engineering based.
*  And then there's another arm that's scientific based.
*  At least it has applications then.
*  It has applications.
*  I think that somebody can be exquisitely trained in math and incapable of dealing with
*  the complexities and the messiness of brain and engineering.
*  There's a beauty and an elegance to math.
*  It's so clean. There's a closed form solution in the limit of infinite data when you have a
*  spherical cow, that sort of thing, right?
*  That I don't think that it's not that alone.
*  It's it's. The most important thing is a quantitative foundation that allows you to have
*  the self-confidence to acquire the new skills you're going to need going forward and even
*  develop those new skills when you realize they don't exist.
*  Develop new quantitative tools, new ways of data analysis, new engineering things.
*  Right. It's really the self-reliance and the self-confidence that you can do that.
*  And just that basis that allows you to do that.
*  But again, these three arms math, engineering, programming, big data, data analysis, it's
*  all of these things, I think, together that that are the important things to kind of
*  cross-train in.
*  It's interesting to me that no one has just blanket said coding, because that's a it's
*  such an important skill nowadays.
*  When I the coding became important while I was in graduate school, I feel like for
*  across the neurosciences.
*  And now it's important.
*  Yeah, I mean, so I am highly involved in undergraduate education.
*  And we talk about the difference between computer science and data science.
*  Right. Those are actually two different things.
*  Like you can code, but still not know what to be able to, you know, when you have a big
*  data set, not know what to do with it.
*  Right. So so there's a distinction between those two things, for sure.
*  Well, if you were just starting out in undergrad and you're or you were in undergrad and
*  thinking about your next steps or something, what and you took away all of the knowledge
*  that you have now? Well, it doesn't matter if you take it away.
*  And what would you go into?
*  One of the most exciting developments I've seen is an increased appreciation in the stem
*  fields of making early STEM education kind of universally interesting.
*  So I experienced that when I started.
*  So I started in chemical engineering and I experienced that early.
*  What I saw as kind of an obsession.
*  It was with, I think, combustion rates of different materials that might be used for
*  fuel. And I bailed and I went into microbiology and biochemistry because they seem to be
*  studying interesting problems.
*  Oh, that's why I got out of mechanical engineering, sort of because they had like a materials
*  push. I was like, this is what are you doing?
*  Yeah, exactly right. And so I think STEM has really started to rethink education in an
*  important way. And if I look back on my education, it was interesting, but it was very fact
*  based. And I think it wasn't enough problem oriented.
*  So if I had to do it again, I think I would stick with engineering.
*  But I would hope that I would be in an era that now appreciates that engineering should
*  be interesting beyond just combustion rates or material properties.
*  It's more broadly interesting to the students who are who are interested in those fields.
*  Yeah.
*  This is sort of seeing the forest for the trees, too.
*  And it's almost impossible to know when you when you aren't even when you've never seen
*  a forest. Right.
*  Like what. And all of a sudden, they're throwing trees at you.
*  Yeah. I don't know.
*  That's a terrible metaphor.
*  But I hear you, though.
*  Yeah. Yeah.
*  In the same vein, there's this there's a right balance and I don't know what it is.
*  This is why I'm asking you, what is the right balance between having a singular focus going
*  and going way down the road in a very narrow topic and becoming a super expert in that
*  very narrow topic versus keeping a lot of focus on the very narrow topic.
*  So this is keeping a broad picture and studying neighboring fields that don't necessarily
*  have exactly to do with what you're studying.
*  Yeah. I don't think there's a universal answer for this.
*  I mean, I think that science benefits by having such a diversity diversity of personalities
*  when it comes to this question.
*  Right. You know, in science, we need those pioneers who are going to take on problems
*  that nobody's even thought of before.
*  And they're just going to like plow ahead.
*  And then we need others who are going to come and really dig in and spend their entire career
*  like flushing out the answers to a problem.
*  You can imagine that first generation, you know, they need lots of breadth.
*  They need to be really open and have like lots of knowledge.
*  It's kind of, you know, very global.
*  Whereas that person is really going to dig in.
*  And those those people are really important, too.
*  But maybe they don't need such incredible breadth.
*  I think we also have the have these really great individuals who have a particular tool
*  and then they apply their tool to lots of different problems.
*  Again, they need the breadth to be able to acquire the expertise to use their tool and apply it.
*  But but they are experts at one thing.
*  So, yeah, I don't think there's one right answer to any of this.
*  And I'm just so happy that there isn't a prescription because I think science would suffer
*  if we didn't have a diversity of different types.
*  Yeah, yeah, we just we wouldn't we wouldn't progress at the same rate.
*  You know, when I think back to when I remember reading Patricia Churchland's
*  neurophilosophy book in a laundromat when I was in college, this is when I was in mechanical engineering.
*  And and you have this vision, OK, like I'm going to go and I'm going to study this.
*  I'm going to become an expert neuroscientist.
*  Now I have a PhD in neuroscience.
*  And I don't know, I I still feel naive in many ways.
*  But do you feel like an expert?
*  You are obviously an expert.
*  Do you feel like an expert?
*  I feel like an expert.
*  Yeah, I remember I had a similar experience like that.
*  I remember telling my father at some point, I think it was in high school.
*  I want to get a PhD, so I know everything about something.
*  Everything. Yeah.
*  And my dad just looked up from his paper and said, no, you won't.
*  And he started reading his paper again.
*  No, you won't what? Get the PhD or you won't know everything about anything.
*  Right. You know, like he had the wisdom to know that like that.
*  That's what he meant.
*  Do I feel like I know everything about something?
*  Absolutely not.
*  But that's what really inspires me and drives me is this.
*  If I spend too much time on any one problem, I tend to get a little bit bored.
*  So the fact that I can use my expertise to dream up, you know, new things I want to work on
*  allows me to become to stay really engaged and excited in this field.
*  So I'm happy that I don't know everything about anything,
*  because that would be a very boring place to be.
*  My favorite part is the the creation, the naivete.
*  Fortunately for me, I'm a very naive person in many ways.
*  So I can always maintain that level of interest in everything,
*  because I just somehow stay naive.
*  It's something to do with my brain. I'm not sure.
*  I like that. Yes, it is.
*  It is the childlike curiosity, right?
*  That drives efficient exploration for learning.
*  There you go.
*  Well, I appreciate your time.
*  I can feel the gratitude that you have looking back and wanting to impart this on your mentees and stuff,
*  which I so much appreciate and much luck moving forward, Nicole.
*  My last question here, because I received an email from you and we're in different time zones.
*  But I think that it was well, it was really early in the morning.
*  My question is, what time do you wake up?
*  And I'm wondering if I beat you in this regard.
*  Yes, so I do have a toddler in the house who likes to wake up early.
*  And so, yeah, typically that is around.
*  Yeah, it's around five, five thirty.
*  OK, we get up in the morning.
*  I did beat you. You know what happens?
*  Is this is this your only child? First child?
*  No, no, no. It's the second.
*  Oh, second. OK.
*  Well, so I have to and the youngest one is this is fascinating for listeners.
*  Right. The youngest one is is almost five now.
*  But I get up at four thirty because that's the only time no one needs anything from me.
*  Yes. As soon as they wake up, it's all done.
*  And then, of course, the headspace.
*  Yeah. Yeah. Yeah.
*  Then past six p.m., I'm mush anyway.
*  So for sure. For sure.
*  Well, thank you, Paul. This has been a tremendous amount of fun.
*  And I'm a huge fan of the podcast.
*  And thank you for doing it.
*  I mean, authentically, like, like, I really enjoy listening.
*  I enjoy the people that you've sampled.
*  It's been just a ton of fun talking to you.
*  It's been really enjoyable. So thank you.
*  Thanks, Nicole.
*  Go to BrainInspired.co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show
*  and prohibit any annoying advertisements like you hear on other shows.
*  To get in touch with me, email Paul at BrainInspired.co.
*  The music you hear is by The New Year.
*  Find them at thenewyear.net.
*  Thanks for your support. See you next time.
*  I don't know.
*  Searching the coffers.
*  For empty offers.
*  I don't know why.
*  You trust the sky.
*  You must like your lies from blue eyes.
*  You

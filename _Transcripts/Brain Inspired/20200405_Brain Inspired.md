---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 6015s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 293
Video Rating: None
---

# BI 065 Thomas Serre: How Recurrence Helps Vision
**Brain Inspired:** [April 05, 2020](https://www.youtube.com/watch?v=Seq9baIbces)
*  That to me was kind of, I don't know if I would call that a wake-up call, but certainly
*  a major surprise.
*  Back then I was educated with the belief that supervised learning and back propagation through
*  neural network was a no-go for biology.
*  Your feedforward visual system has potentially anywhere from two to three orders of magnitude
*  less layers of processing than the state of the art in deep learning.
*  You know, this is just the beginning and this is opening up doors that I haven't seen open
*  until now.
*  This is Brain Inspired.
*  Hey everyone, I'm Paul Middlebrooks.
*  Today I'm bringing you someone straight from the cauldron of visual neuroscience and AI.
*  Thomas Serre runs his computational neuroscience lab at Brown University.
*  These days Thomas is working with deep learning type networks to model various aspects of
*  visual processing.
*  One of his main thrusts is to figure out exactly what all the brain's recurrent processing
*  is good for.
*  We know that feedforward models like convolutional neural networks are good at object recognition.
*  And some of Thomas' work has shown that there's an initial feedforward sweep of visual processing
*  in our brains that can do the same thing.
*  But we also know there are lots of cognitive functions beyond object recognition and there
*  are lots of loops in the brain, giving rise to recurrent connections both locally in a
*  given brain area and across brain areas with feedback type projections.
*  So we talked about some of his current work showing what recurrence can do for us, for
*  our brains, and what it can do for deep learning networks.
*  And we cover some of his other current projects as well.
*  We also talk about Thomas' history a bit and the history of modeling visual processing.
*  So Thomas worked on the well-known H-max model of visual processing in Thomas' lab and he
*  spent much time and effort building in biological constraints into the model.
*  And I think you'll enjoy his stories about deep learning sort of coming onto the scene
*  and before that his interactions with some of the people who were working on early convolutional
*  neural network models.
*  It's an interesting tract in history in these subjects that hopefully someone is documenting
*  out there.
*  Thanks this week to Walshjek, Frederick, Yolande, Kasia, and Lana for your support on Patreon.
*  You'll be hearing from me soon.
*  Find the show notes at braininspired.co.uk slash podcast slash 65.
*  A link to some of Thomas' recent work and also some excellent reviews that he's recently
*  written about the things that we discuss.
*  All right.
*  I have to go teach my youngest son how to read now.
*  It's a very different sort of challenge.
*  Hope you're doing well out there and I hope that you enjoy my conversation with Thomas.
*  Thomas, thanks for joining me here.
*  I know that you guys are on lockdown at Brown, so thanks for it.
*  And things are probably kind of chaotic right now, aren't they?
*  Well, we're getting ready for transitioning to online courses.
*  And so, yeah, it's a little bit of chaos, but it's manageable.
*  Well, thanks for taking the time.
*  So all right.
*  You've worked on computer vision for a long time and hierarchical models of vision in
*  brains.
*  Like, for instance, you worked on H-max, the H-max model, which is one of the most recent
*  precursors sort of to deep networks.
*  And you used H-max for a variety of things, for instance, rapidly categorizing visual
*  objects.
*  And maybe, so I'm going to ask you a question and maybe as a point of reference, you can
*  kind of describe what H-max is for people who haven't studied it in depth.
*  Because my question is, you know, what's your overall take on this recent burst of deep
*  learning?
*  Yeah.
*  Yeah, so H-max is essentially the product of many years of research in the Poggio lab,
*  which is where I did my PhD at MIT.
*  You know, Tommy Poggio is one of these kind of, I guess we can call him the grandfather
*  of one of the grandfathers of computational neuroscience.
*  Does he like to be called that?
*  I don't know.
*  I'll ask him.
*  Yeah, I'll have him on sometime, hopefully.
*  I'll ask him to.
*  That'd be great.
*  And you know, he did a lot of work, similar work on statistical learning theory in the
*  90s.
*  You know, kind of the, back then the work was focusing on what by today's standard we
*  would call shallow architecture, shallow neural networks, things like three-point vector machines,
*  radial basis functions, but really all the theory that kind of laid down the groundwork
*  for the field of machine learning, modern machine learning.
*  And what is interesting, I think, about the work that Tommy has done is that Tommy slowly
*  transitioned from kind of a focus on a three-point vector machine and those shallow architectures
*  towards moving in a direction that essentially turned those architectures into more hierarchical
*  kind of feed-forward network models.
*  And this is the work that he did with Max Rosenüber in the late 90s.
*  So I would say, you know, and so really I joined the group, started my PhD in 2001,
*  and I joined Tommy's group because I was very, very excited about the work that was going
*  on back then.
*  So H-Max was this kind of exciting but also highly simplistic kind of model of the ventral
*  stream of the visual cortex.
*  To me what was exciting about H-Max was that it showed the potential of trying to build
*  computational models that would be able to explain the response properties of neurons
*  in specific areas of the visual system.
*  But back then I was an engineering student back in France and I remember looking at this
*  work and thinking, you know, there's a lot of engineering and kind of hand crafting in
*  that, you know, it's not clear, you know, the selectivity of neurons in intermediate
*  areas was essentially built by hand so that neurons would respond to very simple combinations
*  of orientations.
*  And, you know, the recognition was tested on the same kinds of stimuli that were used
*  on for the monkey electrophysiology, you know, things like paper clips and, you know, kind
*  of simple black and white stimuli.
*  But as I remember as an engineer and a student interested in computer vision, I was convinced
*  by the neuroscience, but I was not really convinced by the application and, you know,
*  the demonstration that potentially this neural network could solve complex visual recognition
*  tasks.
*  And so part of the reason why, you know, I applied to MIT and wanted to work with Tommy
*  Poggio was really to try to bring in my expertise and background in computer vision to try to
*  take this model to the next step and really try to see how far we could go towards getting
*  this, you know, kind of somewhat toyish computational neuroscience model of vision into a model
*  that could solve complex visual recognition tasks.
*  And back then, I was interested in face recognition and so and detection.
*  And so some of the first problems we tried to tackle was what was, you know, how to extend
*  this this model of neuroscience, what's missing in this model of neuroscience to try to get
*  it to work on more complex problems.
*  Something that I forgot to mention is that, yeah, when I started, I took the HMAX, tried
*  to perform sort of face detection task and the network was a chance.
*  Right. So that's kind of disappointing.
*  But, you know, this was the focus of my PhD and working closely with Max Fusenuber and
*  Tommy Poggio, we kind of took the model, extended the model towards a one and more realistic
*  model of biological vision by adding additional constraints derived from neurobiology and
*  the anatomy of the visual system.
*  So we ended up with a network that had more units that was a little bit deeper than the
*  original model, et cetera, more constrained by biophysical data.
*  But you came in with a less biological background.
*  I came, you know, apply for the PhD in neuroscience at MIT with zero neuroscience background.
*  But you're saying so just in retrospect, you saw it and you thought, well, the biology
*  is fine, but I need to bring a better engineering perspective to it.
*  But that's correct.
*  So how did you judge the biology of it without a?
*  Well, I guess I to be fair, I don't think I was in a position to really judge it.
*  Publishing, you know, nature neuroscience and, you know, the fact I mean, the fact that
*  the model was really able to reproduce some of the, you know, what it appeared to be back
*  then, you know, the key properties of neurons in the inferotermal cortex.
*  I mean, I was I was willing to take that at face value and, you know, seeing the potential
*  of, you know, mechanistically accounting for neural responses.
*  But yeah, trying, trying to make this this architectural work on more complex kind of
*  stimuli. And then again, when I joined, you know, the model appeared not to work very
*  well for more realistic stimuli like faces.
*  And so, yeah, the idea was, you know, how to extend those networks.
*  We thought, you know, we went into the direction of adding more biological constraints.
*  But I think the main the main ingredient that we introduced was learning.
*  And so kind of what is interesting.
*  And I think you were asking me about the similarities and differences between something
*  like the HMAX model, which was a hierarchy model very closely related to a
*  convolutional neural network.
*  But back then, I was educated with the belief that supervised learning and back
*  propagation through neural network was a no go for biology that there was.
*  It is. It's still that's still a no go as it is implemented in supervised learning
*  current systems.
*  Correct. That's correct.
*  But I think people are more willing to to consider the possibility that they are good
*  enough approximation of backprop.
*  And, you know, there is a flurry of papers that have come out in the in the past, you
*  know, for five years suggesting, you know, to with varying degrees of success, that
*  there are plausible approximations of backprop.
*  Back then, there was sort of kind of very strong tension between the field of
*  biological vision and computer vision.
*  An easy way to to separate these two fields was by the line was drawn at supervised
*  versus unsupervised learning.
*  And so I literally spent a big chunk of my PhD thesis trying to come up with ways to
*  introduce learning.
*  The original HMAX didn't have any learning at all.
*  The features were really kind of hard coded.
*  But I focused on unsupervised learning mechanisms, versions of ABN learning and other
*  forms of unsupervised learning towards trying to learn kind of intermediate level
*  visual representations, which did help.
*  And so I think that was the difference between getting a network that would, you know, I
*  think it was easy starting with this paper clips, you know, this wiry objects, back and
*  wide objects to come up with a way to engineer neural selectivity for, you know, bars
*  and corners and combinations of orientations.
*  But I think, you know, clearly it was hard to come up with features that would just work
*  for faces. Right.
*  And the secret there was that as soon as we introduced learning and even a very simple
*  form of learning, but that would allow the network to figure out, you know, good enough
*  features to represent faces, then suddenly it started to work and it worked very well.
*  And kind of what is interesting is that I remember very vividly, I think this must have
*  been CVPR 2005.
*  So CVPR is one of the major computer vision conference.
*  I think we had posters with one of young look, look, a graduate student.
*  And we are literally next to one another where we realized that, you know, we were
*  dealing with almost the same models, the same architectures.
*  They were we would not they were calling those convolutional neural networks.
*  We were calling those feed for the article models.
*  They were using backprop.
*  We were using unsupervised type of learning mechanisms, meaning they would try to learn
*  features that are discriminative between object classes.
*  We were learning features that are frequent, right, that are occurring with high
*  probability in some sense in whatever image database we were using.
*  What I find interesting is that back then, I think if I remember correctly, and maybe,
*  you know, Jan will scream at me for saying that, but I think back then we were getting
*  slightly better results than they were.
*  And part of the part of the reason is that, you know, the data sets were so much smaller
*  that, you know, we were dealing with data sets that, you know, on the order of a few
*  hundred classes of objects.
*  So you could really like engineer to the features in a small data set.
*  Engineer also, you know, supervised learning just wouldn't work.
*  That backprop, which is over, they would overfit massively to this training data sets
*  with a hundred. And so, you know, in a sense, you know, unsupervised learning would do
*  slightly better, not by a lot, but slightly better because, you know, less overfeeding.
*  Yeah, very general.
*  Yeah. And and so anyway.
*  So that's funny. So there's two posters right next to each other.
*  This is burned in your memory now because it's kind of a classic case of, you know,
*  these two separate parallel fields moving along together.
*  And did you I mean, you couldn't peer into the future at that point.
*  But did you feel like there was going to be definitive overlap or that it would still
*  be separate? I mean, the overlap.
*  Well, the overlap did happen to some extent.
*  So what is interesting that if you look at the nitty gritty details, I think the original
*  kind of convolutional neural network would would again, without getting into too much
*  of the weeds, one of the key operation in those neural networks is the what we call
*  the pooling operation. That's the operation that allows networks to learn invariant
*  representations or invariant position.
*  And by then they would use something more akin to an average operations when the H
*  Max is called H Max as in the article Max.
*  The key kind of idea behind H Max was that perhaps the right
*  operation for building in invariance is a Max, not an average operation.
*  And now CNN's do Maxing.
*  And exactly. And this is as a result that, you know, I think, you know, the
*  Yen started to play with the Max operation and that they found that it helps.
*  That's funny. The other the other interesting thing was that, you know, again, to account
*  for kind of divisive normalization and things like that, that that are principles that
*  have been long studied and understood in neuroscience.
*  All our convolution included some kind of normalization operation, which, again, was
*  not present in the original CNN.
*  And I believe that there is a kind of systematic study from Yen's group done, you
*  know, maybe the year after or a couple of years later, where they systematically look
*  at those various ways of pooling and normalize, etc.
*  And they also confirm there that the normalization actually end up helping quite a
*  bit. The modern version of that is the so-called patch normalization, which is one
*  of the kind of key ingredients of the of the success of deep neural networks.
*  I mean, I know Yen's not shy about talking about the influences of neuroscience, you
*  know, back to the Hubel and Weasel days and the neocognitron and all of these
*  influences. And then at some point, there's just so much interaction and overlap.
*  It's just hard to parse out like where when you were influenced, did it come to you
*  in a dream or did you talk to someone at a poster or, you know, how these things come
*  about? So it's a pretty interesting and muddled history, probably.
*  That's correct. Yeah, I mean, it's yeah.
*  I mean, yeah, I mean, that's that's an interesting idea.
*  But I mean, what is interesting is that really, it seems, you know, what I understand
*  from Yen's comments is that, you know, the Yen was influenced by Fukushima's
*  neocognitron, which was the kind of first real translation of Hubel and Weasel's
*  work from the 60s, early 60s, mid 60s into neural architecture.
*  I think the neocognitron motivated the H-max.
*  Then, you know, the work that Yen and others were doing in the 90s and early 2000
*  was somewhat removed and disconnected from the work done by, you know, we
*  discussed the H-max and Tony Pudger's work.
*  But, you know, there's a zoo of similar models.
*  You know, Edmund Rawls did a lot of work in the years 2000.
*  There was Dave Barrett, which did a lot of work, a lot of work done, you know, in
*  more kind of neuroscience, computational neuroscience groups.
*  And, you know, there was really literally no overlap and no discussions between the
*  two fields. And then I think, you know, probably Yen and people like Jeff, I
*  remember I wouldn't be able to come up with the exact date, but I remember, you
*  know, Jeff Hinton inviting me to give a talk at one of the CIFAR meetings
*  somewhere around this time.
*  And I think this is the first time that as a grad student, I realized that, oh, my
*  God, there's so much overlap.
*  It's kind of crazy to, you know, to, you know, not having more fruitful kind of
*  conversations.
*  And interesting. Those conversations are being had a lot these days, I suppose.
*  I mean, that's what this podcast is all about that, essentially.
*  So, you know, and of course, you know, yeah, I think things have changed so much
*  since then that, you know, the blur between computer vision and biological
*  vision is almost non-existent.
*  Right. And just to make a small point, you know, it's it's kind of
*  I guess both sad to one extent, but also fascinating to realize that, you know,
*  after having spent so many years of my PhD thesis trying to engineer a model
*  that would as closely as possible approximate, you know, the neural
*  responses found along the ventral stream of the visual cortex, constraining, you
*  know, neurons in the H max so that, you know, the neurons would exhibit similar,
*  you know, tuning properties like peak spatial frequency, receptive field sizes,
*  and, you know, you name it going through decades of electrophysiology work.
*  Important stuff.
*  Right. And then realizing that, you know, and this is the work that Jim DiCarlo
*  has done since realizing that just taking kind of a state of the art deep
*  neural network that has literally no constraints in terms of receptive field
*  sizes or tuning properties from biology and seeing how so much better this
*  neural network feed to experimental data compared to, you know, perhaps simpler
*  older models that were, you know, more grounded in your physiology.
*  That to me was kind of, I don't know if I would call that a wake up call, but
*  certainly a major surprise.
*  So the pessimistic view would be.
*  So when you look at one of those graphs that compares these modern
*  convolutional neural net performance on like object recognition to the older
*  classical models, H max is it's always like the second best second, third best.
*  You know, it's right up there and H max performed much better than earlier
*  different models and a lot of its contemporaries.
*  But so you could either look at that and think, oh, man, we performed so poorly.
*  Or you could look at that and think, man, we were almost there.
*  So which is it?
*  Which do you feel both?
*  You know, a little bit of both.
*  I mean, I think, you know, yeah, a little bit of both.
*  I mean, now we understand better what has been a key kind of engine of the of the,
*  you know, gaining performance.
*  And so, you know, it's clear that backprop makes, you know, we're having this
*  discussion over supervised and supervised.
*  And I was telling you that back in the CVPR 2005, we were using, you know,
*  learning of the convolutional layers, visual representations would be unsupervised.
*  People like Jan's group, you know, and his group would focus on backprop.
*  Back then, the data sets were small for reading being both properly
*  sentations, so they would overfeed unsupervised method, we tend to outperform
*  them. But of course, you know, once the data sets became large enough,
*  internet scale with data sets like ImageNet, then, you know, the gap
*  started, you know, there was not even any kind of possible comparisons between
*  the unsupervised and supervised methods.
*  So, so, you know, to your point, yeah, I mean, if you look at, you know,
*  yeah, I would say it's it's both half full and half empty glasses.
*  At the same time, you learned a lot about vision during the during that time.
*  Right. I mean, well, I'll ask you about that later, because I want to know about,
*  you know, your your advice to people who are getting into the field.
*  So I'll ask you that in a little bit.
*  I mean, one of the one thing that these that HMAX and deep
*  learning, current deep learning nets have in common is that the vast majority
*  of these models are working on object recognition.
*  And it's it's as if we've just kind of made this assumption and accepted that
*  object recognition is what our visual systems do.
*  It's the most important thing.
*  It's weird to me, because whether it's a computer or a human,
*  it's like we show them this picture of something.
*  It's a static image and they can look at it, you know, if it's a computer,
*  you feed it in in vector form.
*  But it's just this image that's static.
*  And that's not how our that's not how we work.
*  That's not how we turn our heads.
*  We move forward and backward and the visual scenes always changing everything.
*  And I'm wondering if we've focused too much on object
*  recognition as, quote unquote, the,
*  you know, computation that vision does.
*  What do you think?
*  Yeah, I completely agree.
*  I mean, you know, the my interpretation of why there is so much focus on object
*  recognition, I think it is to reason.
*  One is that it fits very nicely within the predominant
*  framework in machine learning, which is the supervised learning framework.
*  And we're talking about work in the 90s earlier.
*  You know, this is really the stuff that was formalized and understood relatively
*  early on. So the idea of, you know,
*  organizing samples into categories, classes, you know, natural object categories,
*  become a very, very natural kind of test bed for those kinds of theories.
*  So on the one hand, I would say this is the stuff that we understood
*  and were able to formalize very early on.
*  You know, so that drove a lot of the early work.
*  In addition, I think the value of such
*  automated categorization systems for big companies like Facebook, Google,
*  et cetera, helping you make sense of the deluge of
*  images and videos we have to deal with on the Internet,
*  you know, certainly help
*  kind of add focus to this kind of task and really try to to to solve them in full.
*  Now, so I would say, you know, this has been probably mostly a
*  an opportunistic take that scientists have followed.
*  To your to your point, the relevance for biology, I think you're absolutely right.
*  We do not spend our days categorizing objects.
*  But it's interesting. I was I happen to be watching this interview
*  or listening to this interview with with Torsten Weisel of Hubel and Weisel.
*  And he was recounting their early times,
*  recording these edge detectors and things like that.
*  And he was saying, you know, the dream is to understand how we perceive objects.
*  And so it was even embedded in their early days of recording.
*  Like that is what we want to understand is how brains perceive objects.
*  And so that notion has been also in biology, I suppose, from the beginning,
*  if we consider Hubel and Weisel the beginning, which many of us do.
*  Yeah, which is interesting. You're right.
*  Yeah, I mean, you're right. Yes, that's that's
*  and certainly, you know, I would say to your point, I think this is a very poor proxy
*  for, you know, what the goal of a biological agent is. Right.
*  So our goal cannot be just recognizing objects.
*  We need to find food. We need to navigate a scene.
*  We need to manipulate stuff. We need to make, you know, all of these tasks,
*  I think, go way beyond what object recognition is.
*  In addition, you know, almost any way you want to you want to count,
*  there is no way we can get to the level of supervision,
*  you know, in terms of getting associations between individual images,
*  retinal images or digital images and class labels.
*  And so clearly, the way we learn is not through this, you know,
*  kind of presentation of random images in random order.
*  And so, yeah, our our the level of supervision
*  we're getting is by interaction with the environment.
*  And so these interactions are a much better way to formalize
*  and think about the the the goal of our visual system.
*  So in a sense, figuring out how to manipulate an object
*  is probably a much better proxy for the job that our visual system
*  has to go through every day, as opposed to necessarily recognizing it. Yeah.
*  How do we come about and recognize the object
*  and come about to organize the the set of our visual world in two categories
*  is an important and interesting question,
*  but maybe not the most important one for for biological agents.
*  Well, you've mentioned also the not to go back to HMAX and that distinction.
*  But one of the things that modern deep learning networks do
*  is not care so much about the biological constraints, but they perform a task.
*  And and that's the surprising thing is like all you have to do
*  is ask it to perform the task, not all you have to do.
*  But by performing the task, all of a sudden,
*  the representations are similar to brains in many respects.
*  That's a very simplified way of saying it.
*  So so in that notion, the actual action of performing the task
*  becomes important, primary almost. You're right.
*  And so I think what we've learned from that is that, you know,
*  purely unsupervised learning is probably not sufficient to account,
*  at least in the in the ways that this has been formalized up to up to now
*  as in being sufficient to account as well as supervised training methods have.
*  That said, you know, it could also be that we haven't quite figure out
*  the right learning approach.
*  And so, you know, I'm particularly excited about, you know,
*  some of the most recent developments in deep learning in the area
*  of generative adversarial networks and more broadly, the generation,
*  the the the notion of generative neural networks
*  that are really just trained to synthesize images
*  as opposed to categorizing them.
*  And so I'm not aware of any kind of analysis so far
*  that would have compared the ability of these networks
*  that are not trained and optimized for object recognition,
*  but rather have been trained to learn a generative model
*  of natural images, natural statistics.
*  And I wouldn't be surprised if we find very soon
*  that this neural network even outperform
*  the neural network that have been trained, supervised for, say, image categorization.
*  Yeah, it's coming, isn't it?
*  I'm sure it's just a question of time. Yeah.
*  So, I mean, I have sort of gone back and forth on deep learning, my,
*  you know, opinion on it, right.
*  So sometimes I think that it's a fundamental advancement.
*  I mean, this is the cry of the masses right now that it's going to change
*  the way that we understand brains and intelligence. Right.
*  Other times, I think that it's sort of like the latest in a long line of,
*  you know, fads that kind of coats neuroscience and puts a nice sheen on it.
*  And we learn things from it, but it's fairly incremental
*  is maybe the way that we'll look back on it in the future,
*  at least in its current instantiation.
*  So but it's unclear to me what impact it's it's already had.
*  Right. In neuroscience, has it has it fundamentally changed
*  how we think about brain processing or is it has it been incremental so far?
*  You think?
*  That's a tough question.
*  I think it has already changed the landscape in neuroscience. Right.
*  So, you know, I think one thing that it has done already is that
*  I think many of the tasks that we used to think as neuroscientists
*  as really, really hard turns out to maybe not be so hard.
*  Yeah. You know, if you look at the success of deep neural network
*  for image categorization, I see there are claims that already for the
*  on image net categorization of one thousand natural object categories.
*  There are claims that, you know, the state of the art is already outperforming humans.
*  Right. Face recognition.
*  There was a paper published a couple of years ago
*  by Jonathan Phillips, who has been working for the government,
*  you know, for decades now, assessing progress in facial recognition.
*  The claim of this paper is that, you know, they made a systematic comparison
*  between the accuracy of deep networks versus not just naive facial recognizers
*  like you and I, but the very best facial recognizers we have
*  were these facial forensic experts.
*  I didn't even know that these people existed, first of all. Right. Right. Right.
*  But, you know, they are on par.
*  If anything, the deep neural network is actually a fraction of a percent
*  of accuracy higher than those guys. OK.
*  That, to me, is mesmerizing.
*  And, you know, if you had asked me the question, you know, back in 2005,
*  we're talking about the CVPR 2005,
*  just a little while ago, I would have never expected to see that
*  that kind of improvements.
*  I don't want to say within my lifetime, but certainly within 10 years.
*  So that, to me, is fascinating.
*  I think this is potentially changing.
*  I just my view of what is easy and hard in vision.
*  So that's what I thought would be really, really hard, like natural image
*  categorization, because these are natural images and they are hard
*  to parameterize or facial recognition.
*  Turn out to maybe be easier task than I thought.
*  And yet what's also fascinating is that there are so many other tasks
*  that do not seem quite as hard and that turn out to be much harder
*  than we expected for this deep neural networks. Yeah.
*  So, you know, a few examples, but if you look at adversarial images,
*  for instance, that, you know, are pretty well known, but just briefly,
*  the idea is that it's possible through optimization methods
*  to come up with a very specific pattern of targeted noise
*  that could be superimposed on images so that a neural network
*  would be tricked or what we call full. Right.
*  So the idea is that I can take an image that a particular neural network
*  is very confident and recognizing as say as a cat.
*  Researchers have shown that it's possible to engineer a very,
*  very small amount of a pattern of noise that gets imposed on the image
*  that will fool the network in classifying this cat image in, you know,
*  any arbitrary class of object.
*  And what's interesting is not so much that you can do it,
*  because mathematically this could be shown.
*  But what is interesting is that how little amount of noise is needed
*  to get this neural network that achieves superhuman accuracy
*  on normal images, how this network can so easily get fooled
*  by a tiny amount of noise.
*  Whereas when a human will look at the noise with human design, even
*  and the human barely sees the noise.
*  I can't generally.
*  So that to me is fascinating.
*  Reconciling, you know, the ability of this neural network
*  to exhibit superhuman level of accuracy on the one hand, and then, you know,
*  fail miserably in, you know, in with a tiny amount of noise.
*  Yeah. Similarly, you know, I think there is a growing consensus that
*  it turns out that maybe there is not so much evidence that deep neural network
*  generalize much beyond the training data that was used to train them.
*  So if you had asked me 10 years ago, something like ImageNet,
*  one point five million images sampled from the Internet,
*  you know, that should be a gold standard.
*  Like if this is random images collected on the Internet,
*  that should really tap into the core problem of object recognition.
*  Well, it turns out people are realizing that ImageNet is highly biased,
*  that a lot of the images are taken by human photographers.
*  And so, you know, typically we tend to center objects.
*  We tend to take objects under certain canonical viewpoints
*  and their backgrounds that are consistent, you know, with the class of objects.
*  And we and we love cats.
*  We love cats.
*  You get a lot of cats in your house on your sofa, as opposed to,
*  you know, the middle of the street.
*  And so there turns out to be all these kind of easy tricks
*  that neural network could in principle leverage that a human subjects
*  might not actually be able to leverage because we don't have the ability
*  to see it through millions and millions of images.
*  But but computers have this ability.
*  And so it is possible, although I have to be cautious, of course,
*  about how strong of a claim I'm making, but it is possible
*  that those neural networks leverage a lot of tricks
*  that are present in those data sets.
*  I think that two examples that are speaking to this
*  very recent work done by Boris Katz at MIT
*  has been to try to reengineer a novel image nets.
*  And so what they did is that they ask people on the Internet
*  to take pictures of objects from certain categories,
*  categories that are overlapping with categories of image net.
*  But they essentially ask people to take pictures of those objects.
*  They could ask you to go into your kitchen and take pictures of forks.
*  Right. They would ask you to take pictures of forks
*  under very constrained kind of viewpoints.
*  So you'd be asked to take a top view, a side view,
*  and then to take pictures of those at different maybe distances,
*  maybe under background that are consistent or inconsistent.
*  So they have complete control over the the range of transformations
*  that are being applied to those objects. Right.
*  So forcing, you know, truly the need for a truly invariant representation,
*  invariance to position scale.
*  But you're still in the kitchen.
*  Are they saying hold up the fork with the road in the background or something?
*  They do both.
*  Or they would ask you maybe to take the fork on your sofa, for instance, out of contact.
*  Yeah. So these are still conditions that are trivial for human subjects.
*  Right. You'll still recognize the fork, etc.
*  What they've shown is that if you take different networks
*  that were trained on image net, they there's a massive drop in accuracy
*  when you test them on this novel data set called object net.
*  OK. And so what is even more interesting is that they've also shown
*  that it's not just a kind of what we would call a low level transfer problem,
*  because even if you I'll get a little jargony and I apologize for that.
*  If you try to fine tune the neural network,
*  so you try to retrain them a little bit on this new data set
*  to make sure that, you know, they adjust to the maybe the different illumination,
*  the different level of pixel intensities, etc.
*  They do not improve. OK.
*  And so the conclusion is that, you know, this neural network potentially
*  haven't learned to solve, you know, what most people would qualify
*  to be the core object recognition problem, where you would have to recognize
*  objects under any viewpoint and background, etc.
*  that they are really kind of overtrained and perhaps overfitting to image net,
*  which contains only a very small subset of all the transformations
*  and image degradations that can be applied to natural object categories.
*  So that's another example, I think, suggesting that, you know,
*  perhaps we're not quite as far as we think we are in terms of achieving
*  human level object recognition.
*  I think this is exemplified if you look at the trouble that people are having
*  with self-driving cars, right.
*  So essentially, right now we have many startups,
*  many companies driving, you know,
*  having cars driving millions of miles per year
*  with a human behind the wheels, right.
*  The human, you know, the car driving itself, except, you know, when the car,
*  you know, either makes a mistake or seems to be confused
*  when the human has to take over the wheel.
*  What is interesting is that we find that in general, those cars can go on
*  and on and on and on for, you know, up to I was told even on the order
*  of 100000 miles with that human
*  interaction.
*  The idea is that, you know, those companies are potentially, you know,
*  this once in a while that the humans is taking control over.
*  This could be a failure of potentially the recognition system of the car,
*  that a pedestrian was not detected or that, you know, a flying plastic bag
*  was wrongly detected as a pedestrian.
*  And it's pretty clear that those companies are essentially trying to harvest,
*  you know, kind of those edge cases of vision, right.
*  The pedestrians in this wheel illumination, the
*  weather condition that was not used during training, et cetera.
*  But what we're also seeing is that this is taking a long time.
*  You know, it's it's not just millions of miles, but there are always those
*  edge cases, right.
*  So you can drive as much as you want.
*  There will always be cases in vision that you've never experienced, right.
*  Never seen a particular son in this particular position,
*  particular weather pattern and particular pedestrians wearing this particular shirt.
*  And so what we're seeing is, in a sense, I think the limit of this
*  the current deep neural network approach where, you know, the level of generalization
*  goes just, you know, maybe beyond the training data.
*  And we're still missing this level of abstraction that, you know, is so
*  representative of human vision where, yeah, I mean, at some point, you don't need to
*  continue seeing any more pedestrians crossing the road.
*  You know, we just get it.
*  And that, I think, is the key ingredient that is missing.
*  I mean, this I recently had already has on on the podcast, and
*  he's had this transition in his approach to thinking about
*  neural networks and how brains compute things.
*  And he has come to the conclusion that, OK, we have these neural networks
*  and we you know, they can they overfit things if we let them, right.
*  Just like you're talking about.
*  And if you know, if you have like a really small data set, you have
*  you're way over parameterized and you have these big networks
*  and it'll totally overfit it.
*  And he's come to the conclusion that this is how brains work, too.
*  But because when you give
*  a network, all of these that's over parameterized, let's say all these forks,
*  you know, in different vantage points, that that is still so you probably
*  wouldn't have a fork in by the moon at that point.
*  Right. And so that could be like an outside kind of example still,
*  because you're not going to you're not going to give it every single example possible.
*  And so that the network and our brains will still won't generalize necessarily
*  will fit statistically to the minutia as much as possible.
*  Every single different condition.
*  You've talked about these networks, you know, that you can show like
*  you just memorize all the data instead of generalizing. Right.
*  And because we're exposed to so much data, our brains
*  and by the way, our brains are massively over parameterized
*  is one of his points as well, way over more over parameterized
*  and than any current deep network. Right.
*  And that that's what our brains are doing, but that that is good enough
*  because they're so powerful to essentially almost everything is within our training set.
*  So then we're going to when we're going to be tested on it,
*  it's basically within that what's called the interpolation zone.
*  And that our brains are bad at generalization or extrapolation.
*  An example that's outside being, you know, the training set, essentially.
*  I don't know. So so this notion had kind of, you know, got me on board
*  essentially that, OK, you know, we're not so general and special.
*  We're actually overfitting everything.
*  He calls it direct fit.
*  And that, you know, also his argument is that this is the way evolution works
*  over massively longer time scales, that, you know, evolution works
*  by directly fitting our biological fitness or whatever to the environment.
*  And and that that's not all brains do necessarily.
*  But that's he, you know, he puts it between like 70 and 90 percent of what brains do.
*  And I don't know. What do you think of this notion?
*  I mean, I do think, you know, I mean, I agree with many of the things that I've heard.
*  I do think that there is a qualitatively different level of abstraction
*  that's possible in this, again, as current iteration of
*  deep neural network and biological homologues.
*  You know, one example, you know,
*  learning something as simple as the notion of sameness from training examples.
*  So I can show you, you know, pairs of shapes or multiple shapes.
*  I give you a maybe a handful of images.
*  And I told you I don't tell you the rule, but I tell you those are
*  positive examples.
*  And all these positive examples would contain pairs of shapes
*  that are always identical, maybe up to a transformation to be determined.
*  And then the negative set shows pairs of different shapes or colors.
*  I think, you know, depending on the task, you can imagine
*  cases where human subjects could learn that from maybe two, three, four
*  training examples. Right.
*  We and others have shown that in the same condition it takes, you know, orders.
*  I mean, I'm talking about tens of thousands of training examples
*  for neural network to learn those tasks.
*  And that even when they seem to learn the task, they do not seem to
*  necessarily demonstrate an abstract understanding of the rule,
*  which would be figuring out whether two things are the same or different,
*  because they never generalize much beyond the shapes that are used for training.
*  Are these feed forward networks?
*  Convolutional neural network. We've also tested, you know,
*  kind of what a few years ago was considered the state of the art
*  in visual reasoning, the so-called relational network.
*  And what's fascinating is that, you know, people have done the experiment
*  on newborn ducklings. You can wiggle.
*  You can take a pair of, you know, a very simple geometric shapes,
*  you know, cubes and balls and of colors.
*  You take a pair of this, you wiggle them in front of a newborn duckling.
*  You perform what is called imprinting, right, which normally appears at birth
*  when the duckling imprints on their mothers.
*  A single training example.
*  And yet those authors have been able to show that the duckling
*  do seem to generalize beyond the appearance of the shapes used during training.
*  So they can generalize to different colors, different shapes
*  from a single training examples.
*  They seem to get this notion of same or different.
*  And that is at the level where, you know, I would challenge anyone to
*  provide a neural network today that can do that, can learn the notion of sameness
*  from a single training example.
*  And I think this is the level of abstraction we're talking about, you know,
*  seeing a pair of of of of blue cubes.
*  And from that understanding that the rule is same or different.
*  And being able to generalize to other colors and shapes, etc.
*  Yeah. On the whole, we have a lot more to get to, I suppose.
*  So on the whole, you don't think deep learning is overhyped then?
*  I know. Well, I think there's a little bit of both.
*  I think the success we're seeing is tremendous.
*  Let me restate, actually, with respect to neuroscience.
*  You don't think deep learning is over overhyped with respect
*  to its potential in neuroscience.
*  I think it has already demonstrated the benefit for neuroscience.
*  You know, we went through this example where, you know, I think it has allowed us
*  to rethink what's easy and hard in vision.
*  We just went through examples of, you know, image categorization,
*  face recognition that turns out to be easier than we thought.
*  And yet simple task like figuring out whether things are same or different
*  or very big visual task, very simple shapes, colors,
*  parameters that would seem trivial for computer vision algorithm
*  turn out to be much harder than we would have imagined for a neural network.
*  And so I think it's kind of what deep neural network has already done is allowing us
*  to rethink a little bit the framework of visual tasks,
*  the space of visual tasks.
*  There's a ton of work, obviously, on using deep networks in vision.
*  I mean, I think we went really to the work of Jim DiCarlo
*  feeding deep networks to neural recordings done along the ventral stream
*  of the visual cortex in area V1, V4, IT.
*  There's amazing work done by Surya and Goody and colleagues at Stanford,
*  where they've been feeding those convolutional neural network to regional data.
*  And then if you look at the quality, the goodness of the fit,
*  I mean, we're really talking about goodness of fit that is, you know,
*  significant, very significantly better.
*  So massive improvement in our ability to capture something about the response
*  of neurons along visual areas.
*  That, I think, is very significant, right?
*  That's showing us that there is much more explainable variance
*  that can be captured from neural recordings,
*  from the response of neurons that is observed.
*  I think the part where maybe it's overlapped is that I think there is a lot of work
*  that is, by lack of a better and more
*  politically correct way to say it is mindless in, you know, I think just,
*  you know, feeding arbitrary neural network to arbitrary neural data
*  is not going to get us very far.
*  But I think we're at the point where, you know, the field is understanding that,
*  you know, we have neural network that can capture a lot of information
*  and the variance observed in neural data.
*  The next step will be to try to open up the black box and figure out,
*  you know, what it is in those neural networks that enables them
*  to go beyond some of the older models that we went through.
*  And so I think if we do this,
*  you know, there's the opportunity for deep neural networks to do
*  what computational neuroscience hasn't been able to do until now,
*  which is really to set the ground for,
*  you know, making predictions, testable predictions for neuroscience that can,
*  you know, that can be tested.
*  And so I think we the next phase for this line of work will be to have
*  essentially closed loop experiments where based on the initial recordings we have
*  and feeding of data permissible with the current architectures,
*  people will be able to make specific predictions about how specific,
*  maybe class of interneurons or very specific type of neurons
*  would contribute to very specific kinds of computations
*  that can then be inter inter integrated with kind of modern neuroscience tools,
*  such as, you know, various kinds of imaging, various kinds of optogenetic techniques.
*  And so I do not think this is overhyped.
*  I think there is potentially room for improving the kind of work that's being done.
*  But I'm certainly one of the more optimistic in thinking that,
*  you know, this is just the beginning and this is opening up doors
*  that I haven't seen open until now.
*  You're doing a lot of the work on implementing biological constraints
*  still, things like excitation and inhibition.
*  And I hope that we get to a lot of your work actually here.
*  But, you know, one thought is, well, do we need neuroscience at all?
*  Do we need to study brains or can we just bypass brains?
*  Keep throwing, keep building new networks
*  and throwing more computational power at them and asking them to perform tasks.
*  And we could get to whatever artificial general intelligence
*  or eventually build quote unquote intelligence.
*  And I don't know that we're ever going to come to a satisfying notion
*  of what intelligence is.
*  So that is a question in itself.
*  But, you know, do you think that we need brains?
*  Do we need this? Do we need neuroscientists?
*  Well, I think, you know, I think it depends on your goal.
*  My goal is to understand the brain.
*  So I see deep learning as a tool towards achieving this goal.
*  So there is no question that, you know,
*  by testing the possibilities and limitations of current computer vision,
*  deep neural networks, you know, that gives us a lot of information
*  about what can and cannot be done with, you know, with a finite set of
*  what I would call neural computations. Right.
*  So that's certainly gives me a lot of information, useful information for brains,
*  which in turn allow us to ask the question, what it is,
*  what are the additional computations that brains are able to implement
*  that are not currently present in modern deep neural networks
*  that potentially could help a deep neural network.
*  And so I think this interplay between computer vision,
*  assessing the limitations, strengths and limitations of computer vision
*  allows us in turn to understand, you know, what makes brains so special.
*  And so in that sense, I think, you know, given some of the limitations
*  of deep neural network that, you know, we've alluded to in the short term,
*  there is certainly given that those are tasks that are, you know,
*  much easier for biology.
*  There's certainly a lot of room for neuroscience to contribute
*  to deep learning. And, you know, if we have time, I hope we can go through some
*  more specific examples.
*  Now, to your point, you know, that's not to say that
*  the ultimate solution to, you know,
*  achieving true general intelligence will require biology.
*  You know, after all this, our brains and computers are
*  very different kinds of strengths and weaknesses,
*  very different kinds of power requirements, et cetera.
*  And, you know, I wouldn't bet my career on the fact that, you know, down the line,
*  the solutions of the optimal solution to general intelligence
*  has much to do with neuroscience.
*  Let's play a fun game real quick.
*  So I just thought of this little thought experiment.
*  So we have a number line from zero to 100 and zero is the McCulloch-Pitts
*  artificial neuron and 100 is,
*  I don't know, true intelligence, human like intelligence, something like that.
*  Where on the scale is current deep learning?
*  Oh, that's on the current scale.
*  It's probably at about I would say a scale of 20, you know, 20, would be my guess.
*  Twenty. All right.
*  This is I'm going to keep asking people this and we'll we'll get a great.
*  That's a great question.
*  You can get statistics.
*  Yeah, I need data, right?
*  It'll be a small data set.
*  So I'll overfit. But oh, well, you know.
*  And that's funny, because I think yours is kind of pessimistic.
*  Twenty is somewhat pessimistic, but we'll see.
*  So, you know, sorry.
*  So maybe let me restate that.
*  I guess my answer was if if I go from the McCulloch-Pitts
*  model of a neuron all the way to a model that would capture every possible
*  biophysical phenomena of a neuron, we're on a scale of 20.
*  Now, if I maybe I misunderstood your question,
*  yeah, let's reforgerate the question, which has which had more to do with
*  how far you need to get towards biological realism to achieve,
*  you know, general intelligence.
*  You know, it's not clear to me that you need to pass 50 anyway, right?
*  That, you know, and, you know, I think this is very much the point
*  that Yann LeCun has been making for, you know, many years now that, you know,
*  it could well be that, you know, coarsely approximating
*  the main two kinds of functional cells found in the visual cortex,
*  you know, simple and complex cells, which, you know, are well approximated
*  by convolutions and kind of putting operations.
*  Maybe that's all you need.
*  You know, with a proper, you know, learning algorithm,
*  that's all you need to get past
*  human visual intelligence.
*  And so, you know, so I don't know if then I'm fully answering your question.
*  No, well, it wasn't a well-formed question, see,
*  because what I kind of wanted to go is from McCulloch-Pitts,
*  you know, to the birth of this AI neuroscience collaboration, right?
*  But, you know, to whatever we would consider satisfying
*  the general intelligence, right?
*  And where we are in that march, not necessarily like how much
*  biology we need to implement, you know, how specific the models need to get,
*  how biologically real, just like where deep learning,
*  because there's so much hype about deep learning right now.
*  And everyone thinks, oh, we just need to put two of these networks together
*  and we're going to have an intelligent system, you know.
*  And but my feeling is we're way far from that.
*  And I wonder how far.
*  And so that's what, you know, where in the current state of deep
*  learning on that number line are we, you know?
*  Yeah, I mean, again, I'm not trying to avoid the question,
*  but the difficulty in answering this is that it depends
*  what the actual final metric will be.
*  So one example is that if you look at self-driving cars,
*  I mean, I think if you look at it by, you know, the level of human
*  intervention that's actually happening, you know, you could claim that
*  we're 99.9% there, right?
*  I think those those self-driving vehicles have a false alarm every,
*  you know, hundreds of thousands of miles, right?
*  Now, the problem is that if your goal is to have, you know,
*  no mistake, then, you know, I don't think the current paradigm of,
*  you know, looking for mistakes of the system to reinject those mistakes
*  in the training data set is going to get us to that level.
*  And so on the one hand, you could say we're 99.9% there.
*  But if your goal is to achieve 99.99999% accuracy,
*  then I think we're not even halfway there
*  because what we're going to need is much more than more of the same.
*  Yeah. Well, it needs to be a logarithmic scale, too, I realize.
*  And and, you know, it's tempting to say, OK, well, touring test.
*  That's the end. But that's not a good test to me.
*  So, yeah. OK, we'll have to all of reform the question.
*  Thanks for sharpening my questions here over the long haul.
*  Well, Toma, you have you've made models of cortical columns in vision.
*  And, you know, they have pretty specific computations
*  about how classical receptive fields and extra receptive fields
*  interact with excitatory and inhibitory connections.
*  And it's quite it's quite complex and it works really well,
*  as you can tell us more about.
*  But there's this notion of the canonical microcircuit in the cortex,
*  which is sort of repeated across cortex and cortex
*  writ whole writ large is just this repeated computation over and over and over.
*  The same basic computation happens over and over.
*  So what do you think?
*  First of all, do you think that that's true?
*  And if so, what do you think that the cortical column computes?
*  What's that general computation?
*  Yeah, so I think, you know, there's there's little to dispute that claim.
*  Right. So I think the evidence is there and there is, you know,
*  plenty of evidence for for cortical columns,
*  but cortical columns potentially being the the building block of computation.
*  And so, you know, chances are the basic computational unit
*  in biological neural network not being the neuron,
*  but maybe something more akin to the cortical column.
*  So I think that, you know, it's easy to believe again.
*  I think that there are there's pressure from
*  in biology for things to be more easily,
*  you know, to to to to to be sharpened by, you know, to be set by genetic.
*  And so I think a lot of that
*  repetition and the fact that we find these motifs, et cetera,
*  is probably a byproduct of the need for, you know,
*  much of the wiring to be genetically encoded.
*  Right. Because we need to to have certain minimal functions at birth.
*  Imprinting so imprinting would be one of them if you are duckling.
*  You know, there's evidence now that babies learn face recognition in the womb.
*  Right. So there is already a lot happening.
*  And so I think, you know, genetic is probably one of the, you know,
*  so that potentially, you know, the existence of these motifs
*  or is probably a byproduct of a lot of genetic.
*  Now, what I think is, you know, your question to do with
*  actually, do you mind reformulating your question?
*  Yeah, well, I mean, there's a lot of been a lot of suggestions of what the
*  what the cortical column computes.
*  Right. It's computing a prediction.
*  LSTM have been used as a model, you know, to try to model
*  the cortical microcircuit and its computation.
*  Maybe it has some sort of gating function, right, like an LSTM that it's all built in.
*  It's just a repeating motif of LSTM, the cortex.
*  And and you have this, you know, beautiful model of the
*  that captures a lot of the receptive field dynamics and a lot of visual illusions.
*  And, you know, I'll point to that work in the show notes.
*  And if that if it would help, you can describe that
*  that modeling, because what you're essentially doing is modeling the canonical microcircuit.
*  Yeah, so that's a good point.
*  So the you know, if you look at
*  what a modern convolutional neural network does, a feed for neural network,
*  much of the wiring is happening from a particular layer of processing on the
*  higher level of processing.
*  Right. So there is no.
*  So in a way, the only way for neurons to communicate is through bottom up processes
*  or what we call feed forward processes.
*  Now, in contrast, if you look at the visual cortex, there's actually extensive cortical feedback.
*  So this feedback takes two forms.
*  One is what people commonly refer to as lateral horizontal connections.
*  So those essentially link neurons and cortical columns within a layer of processing.
*  And as a maybe point of clarification, especially in early visual areas,
*  columns correspond to typically a group of neurons spanning potentially a range of selectivity.
*  So in the primary visual cortex, you'll find at least a hyper column will contain
*  all neurons due to all possible orientations and maybe a range of spatial frequencies, et cetera.
*  But one commonality between all these neurons within the these cortical hypercolumns
*  is that their receptive fields overlap.
*  Is that their receptive fields overlap.
*  Right. So they're all responsive for the same part of the visual field.
*  Yeah.
*  OK. So if you add horizontal connections or an ability for neurons to communicate
*  laterally, that means that essentially you allow neurons that have receptive fields
*  centered at different locations to communicate between themselves.
*  So essentially, you allow the information not just to flow upward,
*  but also laterally across region of the visual field,
*  which is you're saying one fundamental type of recurrence.
*  The other type being the top down.
*  The other type being the top down, going from a higher level layer of processing
*  onto a lower level of processing.
*  So some of the early work we had done, and I think this is the work that you were alluding to,
*  was really trying to figure out a way to go beyond this very simple model of neural responses
*  as found in current convolutional neural network.
*  As I mentioned earlier, this neurons can only propagate information from the bottom to the top.
*  And so essentially, when you go into different layers of the hierarchy,
*  you'll find that neurons have what we refer to as a receptive field,
*  which is a part of the visual field that can trigger elicitor response from them.
*  What is interesting in neurobiology is that you find that neurons don't just have a classical receptive field,
*  but they also have a zone, an area, sitting right outside of their classical receptive field
*  that can modulate their response.
*  So by construction, by definition, the extract classical receptive field,
*  if you stimulate that part alone, will not elicit any response from the neuron.
*  But if you stimulate the classical receptive field, then what you put in the extract classical receptive field
*  can have a tremendous impact on the neural response.
*  Those kind of effects are completely inconsistent and hard to reconcile with modern convolutional neural network.
*  So we wanted to understand that and build a model of biology
*  that would allow us to explain those type of phenomena.
*  And so we started with a very simple model of horizontal connections.
*  We looked at the anatomical and neurophysiological data available to try to figure out how we need to link neuron
*  both within a cortical hypercolumn, but also across cortical hypercolumns,
*  so that we could explain the neurophysiology of this so-called extract classical receptive field phenomenon.
*  We were able to do this, and that was our starting point.
*  The next step was to show that we could leverage this model of neurobiology
*  and test how far we could go in explaining so-called visual contextual illusions.
*  So there are many of those, and they are hard to explain without visuals.
*  But one example would be color perception.
*  So your perception of color, what we refer to as the reflectance properties of a surface, are highly context dependent.
*  So I can show you a little gray patch, a colored gray patch.
*  And so if I force you to see this through an aperture and there is no context,
*  you'll be very good at recovering the exact shade of gray that's being used.
*  If I start embedding this gray patch into a context of different color,
*  your perception of this gray patch will be altered completely.
*  And this is, of course, very well known.
*  You know that painters know these facts very well.
*  And they will never choose a particular color in isolation,
*  but they will always choose this color next to other colors.
*  And so those are called color contrast effects.
*  If I embed a gray patch on a red background, the gray patch will look greenish.
*  Conversely, if I show you this gray patch on a green background, the patch will look reddish.
*  And there are many such phenomena spanning many visual modalities.
*  For instance, I can show you bars at different orientations.
*  Your perception of the orientation of a center bar can be drastically affected by what I put in the surround and the orientation of the surround.
*  Same with motion. I can show you moving stuff.
*  And if I embed this moving stuff into a background of things that's moving in different directions,
*  depending on the kinds of movement of the background, you're going to see things moving in one way or another.
*  So our perception in a way is, to a large extent, context dependent.
*  Your perception of your particular perception can be drastically affected by what is presented in the context of a particular stimulus.
*  So we wanted to test the ability of this very simple model to account for those.
*  And we found that, you know, to our surprise, we were able to account in relatively good detail for many of those contextual illusions.
*  And we produced very known psychophysics results.
*  Now, you know, the skeptic would say, well, you know, I'm a computer vision scientist.
*  Why should I bother? Essentially, you're telling me you've been able to design a circuit,
*  you know, derived from neurophysiology that is essentially able to get fooled by the context, right?
*  Because that's what we do.
*  Illusions are deviation of our percept from the physical reality of those of the stimuli.
*  But we suspected that a lot of these visual illusions are kind of just edge cases that aren't really bug of our visual system.
*  The edge case in the sense that they are very artificial, they are very different from the kinds of visual stimuli that we have to deal with on a day by day basis.
*  And so we thought that, you know, a system that exhibit the sensitivity to contextual illusions would demonstrate many other benefits in maybe more realistic and of natural recognition.
*  And so we wanted to demonstrate the benefit of this kind of highly recurrent neural network,
*  where once again, the flow of information is not just bottom up,
*  but that neurons with receptive field spanning different region of space are able to communicate horizontally to solve, you know, jointly certain kinds of tasks.
*  And so the first task we came up with is a task that was motivated by earlier work in cognitive psychology.
*  And we call that the Pathfinder. So the Pathfinder is very simple.
*  I give you images. I don't tell you the rule. You have to learn that from examples.
*  The positive examples include both positive and negative examples include markers, two markers.
*  The positive examples, you'd find that there is essentially a path, a contour that goes from point A to point B.
*  Like footsteps in sand or something, right? Like different...
*  Imagine in sand. In practice, you know, we use very simple tasks, simple stimuli such as, you know, black and white pixels and things of that sort.
*  But yeah, imagine following footsteps in the snow, right? Where you would have multiple footsteps.
*  And I tell you, you know, you are at point A. Is there a way following either a footstep that would take you to point B?
*  Yeah, okay.
*  And the negative examples would, you know, the two markers would fall on different paths or contours.
*  We thought that the way for a feedforward neural network to solve this task,
*  we thought that the feedforward neural network would have to reach or build receptive fields that at least encompass both markers and the entire path linking the two markers.
*  Right. And in order to figure out the task.
*  And so the way modern neural network grow their receptive fields is through depths.
*  Okay. And so the prediction was that if we parameterize the stimuli so that we test neural network with increasingly long contours or path,
*  the prediction was that the minimal neural network, the depths of the minimal neural network that would be able to solve that task should grow.
*  Should grow. Yeah. As the path grows, it should grow.
*  As the path as the as the length of the path grows.
*  And so we verify that and confirm that even for a very simple task, black and white images,
*  even million of training examples available again for a task that we take human subjects,
*  you know, potentially just one positive and one negative example feedforward neural network can solve that.
*  But, you know, in the extreme case, we had to reach hundreds of layers of depths to solve this,
*  what is otherwise a very trivial task and hundreds of thousands of training examples.
*  In comparison, we show that if you take one of our basic circuits,
*  highly recurrent, you know, circuit that leverage recurrent connections across locations,
*  across vertical columns, then we find that the single layer can solve the task invariant to the number, the length of the path.
*  So it can solve that with a single layer with orders of magnitude less free parameters.
*  We're talking about overparameterization of modern deep network just a few minutes ago.
*  Yeah. Three orders of magnitude less free parameters and a fraction of the number of training examples needed.
*  Okay. So this is one example.
*  This kind of what I would refer to as incremental grouping task task where you have to literally follow a path from point A to point B are very natural for this kind of recurrent neural network.
*  Feed for neural network are what we call universal approximators.
*  So in the limit of enough units and enough training examples, they can learn any arbitrary task,
*  but they will do it in what I would call the brute force way.
*  It was going to take them a lot of training example and a lot of neurons to do what is otherwise trivial for a single layer of processing with a proper kind of recurrent feedback.
*  So, I mean, modern convolutional neural networks have grown and grown.
*  I don't know what the latest number of layers on average being used is 200, 300.
*  Well, it depends on how you count.
*  But yes, so because now some of these neural network are actually what we call ensembles of neural network with 100.
*  You could say this is equivalent to thousands of layers of processing.
*  And so what you found with this and what you claim in general is that recurrence is a way of replacing that depth with fewer parameters.
*  Absolutely. So what is interesting is that, you know, there is there is a task that has been extensively studied,
*  which is called the rapid image categorization.
*  The idea is to flash images very briefly in front of human subjects, force their response to be as fast as they can.
*  And the assumption is that when you constrain the visual system to operate at its temporal limits,
*  what you're doing is forcing the visual system to operate in what we refer to as a single feed-forward sweep of activity.
*  So although there is massive feedback in your visual system,
*  the assumption is that when you force when you're pressed for time to detect a tiger, you know,
*  and move away from a from a predator, your visual system can do that in an almost automatic reflex like way through a single feed-forward sweep of activity with limited contribution of the feedback.
*  The motivation for feed-forward neural network was originally to try to account for these kinds of rapid visual processing.
*  And this was we were talking about H Max.
*  That was one of the goal to ground one of those network in electrophysiology and to demonstrate or to at least assess the consistency or inconsistency of responses from such a network with those of human subjects.
*  Now, what is interesting is that the H Max had, you know, the order of maybe I think there was eight layers of processing, depending on how you count in human subjects.
*  People would say probably anywhere from the human subjects at anywhere between six and 12 layers of processing during this feed-forward sweep of activity or rapid categorization task.
*  So arguably, your feed-forward visual system has potentially anywhere from two to three orders of magnitude less layers of processing than the state of the art in deep learning.
*  What is interesting is that the H Max was consistent with human subjects during, you know, because people do make mistake if you force them to respond fast.
*  The H Max was able to be to show that it was consistent with human decisions.
*  In other words, it was making similar pattern of errors with the rapid categorization.
*  It was a rapid categorization.
*  So the point that I'm going to I'm about to make is that today, you know, those very deep neural networks outperform human subjects, not just in rapid categorization task,
*  but even when in unconstrained visual recognition task, I can show you pictures of, you know, different kinds of boats and insects.
*  Those deep neural networks will be doing much better than you, even if I don't give you any limitation in time.
*  And not just because you don't know the name, but because really, you know, you're almost at the limit of what you're, you know, the level of detail that your visual system is able to to categorize.
*  And so, you know, to some extent, we've engineered feedforward neural network that has orders of magnitude deeper than our own visual system.
*  They outperform what our visual system can achieve in a feedforward sweep of activity.
*  And so in a sense, they've gone beyond, you know, they have diverged from essentially the way our visual system actually works.
*  As you pointed out, my main argument and that of many others is that the way by which we can increase our depth of processing as human subjects when we're allowed more time.
*  Right. So if I give you a five-minute millisecond to perform a task, you'll make some mistake.
*  If I give you an extra 200 milliseconds, you'll start doing less mistakes.
*  So the argument is that the more time you have, the more you see and the better you get.
*  The way this is done is not through static processing depth in your visual system, but by allowing feedback to essentially kick in and potentially refine some initial decision that would have been possible through an initial kind of feedforward sweep of activity.
*  So do you think and I want to talk a bit more about the recurrence aspect of this, but so if we built a convolutional neural network that was 10,000 layers deep, would it be, you know, is there something?
*  That it would be missing in terms of what recurrence would buy us, you know, so you just talked about the the ability of these lateral horizontal sort of recurrent feedback projections.
*  And you're just talking about recurrence as a way to be able to, you know, be able to spend a little more time processing an image, for instance.
*  So what are some other things that recurrence might be able to buy besides just computational efficiency?
*  Because you don't want to build the biggest convolutional neural network if you can build a smaller recurrent neural network.
*  So that's that's fine. But let's take efficiency off the table.
*  But biological skill wise, right?
*  What can recurrence buy us?
*  Right. So, you know, just to get this out of the way, as we said, you know, feedforward neural network are universal approximators.
*  So if you give them enough units and enough training samples, in theory, there is no task that they that that recurrent neural networks can solve that they cannot solve.
*  That's right. So we could make a near infinite one layered hidden one hidden layer network and it could do, you know, in theory as well as a very deep network and vice versa.
*  Right. So that's, you know, right.
*  Now there's a number of things, you know, so the interesting question becomes, yeah, what can I learn with a as small as possible number of samples?
*  And so what you find there is that potentially if you try to, you know, if you try to leverage recurrence, you can increase processing depth through time without necessarily increasing the number of free parameters.
*  So what I mean by that is that, you know, and there's a lot of debate and a lot of work being done today in this field to try to formalize this a bit better.
*  The kind of textbook machine learning kind of golden rule of machine learning is that if you want to generalize well, you need to force some constraint on the number of parameters in your network or the degrees of freedom of your parameters.
*  And so to a first approximation, you know, you want to be in regimes where you have more samples and free parameters with deep neural networks.
*  The other way around, imagine that as 1.5 million training examples.
*  That seems like a lot, but the state of the art has hundreds of millions of free parameters.
*  And yet, you know, they seem to be working to some extent.
*  So that's kind of a puzzle.
*  But suddenly, in general, controlling the capacity or the number of free parameters or the degrees of freedom of a learner is never a bad thing.
*  What a recurrent neural network allows you to do is to some extent recycle the same computation over and over again.
*  And so essentially increase the processing depth through time while controlling because those recurrent connections are fixed.
*  They do not contribute to increasing the number of free parameters or degrees of freedom.
*  So in a way, a deep neural recurrent neural network might be able to do as well as a much, much, much deeper neural network with many more degrees of freedom, many more free parameters.
*  And so that means that it has an advantage that it may be able to learn much faster from far fewer training examples.
*  And so, in fact, you know, one of our paper that's going to come out at the next ICLEAR conference is showing precisely that that if we leverage those recurrent circuits in the in the context of image segmentation and control detection as a side note, the state of the art are still very deep fit for a neural network.
*  And they do achieve human level of accuracy at deciding whether there is a contour or an edge at that particular image location.
*  So there is not much room for improvement.
*  But the problem is that to get to that level, you have to go through a lot of hoops.
*  You have to do some pre-training on ImageNet.
*  You have to continue the fine tuning on Pascal.
*  And then you have to continue, you know, fine tune on the actual data set.
*  So there's so much training that goes on.
*  But yet, you know, works.
*  I have to confess that, you know, this is human level of accuracy.
*  So this is quite impressive.
*  What we've shown is that if we just leverage the recurrent neural circuits that we've just been discussing, we can also achieve human level of accuracy when we use all the bells and whistles and all the engineering that comes along with training those networks.
*  But once we start kind of reducing the number of training examples available to the system to learn, then we start seeing a very kind of drastic improvement in the generalization ability of the recurrent neural network.
*  We find that, for instance, we can do the same, achieve the same level of accuracy as a very deep state of the art fit for a neural network.
*  So we can achieve the same accuracy as the system using 100% of the training set with only one-tenth of the training sets.
*  So, you know, it's a very substantial improvement in the efficiency or how many training examples those neural network need in order to learn any particular task.
*  Now, you know, to be honest, this is control detection.
*  And there are many reasons to suspect that control detection is kind of an optimal task to leverage this kind of horizontal or feedback connections.
*  I think the jury is still out as to which, if any at all, other visual recognition tasks will similarly benefit from the inclusion of feedback mechanisms.
*  So right now I have students working on the prime of color constancy, recovering the color of the what we call the reflectance property of a particular surface in a way which is invariant to the color of the light source.
*  Again, we suspect that the feedback will help us tremendously there.
*  But I think, you know, the jury is still out and this is still very much an ongoing project.
*  The work you're describing with the pathfinding work, I think that's what you call it.
*  Is that a visual reasoning task? Does that fall under the?
*  Well, we call it visual reasoning because I think, you know, this is certainly the kind of task that you might not be able to solve in this kind of rapid image categorization mode.
*  So presumably this is the kind of task that require additional computation.
*  We call it visual reasoning, but I think, you know, we can.
*  Yeah, the reason why I ask is because you do work on things like that.
*  And I'm wondering what other domains recurrence might be important for in our cognitive abilities.
*  Right. You've mentioned, I think, attention and search task, things like that.
*  And I don't know if you want to wax poetic about those.
*  What other abilities might be good?
*  Well, so for instance, you know, we were earlier and we were talking about the tackling and the same different task.
*  So there is there is evidence that human subjects solve this task with the involvement of attention and working memory mechanisms.
*  Both of those functions require feedback.
*  And so, you know, that could be an additional kind of role for feedback that might be needed to solve, you know, what I would refer to as visual reasoning task beyond just, you know, simply image categorization.
*  Another possible role of the feedback, which is something that we had found already many years ago with the H Max is that before a neural network tend to have a hard time dealing with clutter.
*  So they can they can do very, very well when there is a single kind of well isolated object.
*  But the more you embed this object in clutter, the harder it gets.
*  Don't don't take it into my children's room, in other words.
*  I see. Yes.
*  And so we have been speculating that to deal with clutter of visual system leverages attentional mechanisms.
*  So essentially an ability to somewhat zoom in onto a region of interest and then essentially focus processing on that region of interest.
*  Essentially, you know, we're suppressing, you know, forcing the visual information to be only from that part of the visual field to be routed to higher visual areas.
*  So she explicitly suppressing clutter.
*  A few years ago, we had a collaboration between the Podula and the decimal lab at MIT when I was opposed out there that has shown precisely that.
*  And if you do monkey electrophysiology in the infer temporal cortex and you try to decode the identity of an object shown to them to a monkey from a small population of, you know, say, a hundred neurons, if there is a single object, you can do that perfectly from a small population of neurons.
*  If you start putting multiple objects in the receptive field of neurons, then the accuracy drop.
*  Right. So essentially the neuron is sensitive to clutter just the same way as the H Max was.
*  But then if you train the monkey to attend to one particular object location, say a location corresponding to one of the objects presented in the receptive field, then suddenly the same neural decoder that was trained on the presence of a single object in the in the receptive field, then start working again.
*  And then you can start decoding what's going on at the cued location.
*  And so what that suggests is that this is essentially what attention does.
*  Attention as a way to somewhat suppress the clutter and and and force receptive fields and processing more generally to be focusing on an object of interest.
*  To be clear, those kinds of attentional mechanisms are known to rely on feedback mechanisms.
*  That that account of attention can conforms with how we how we understand human attention mechanisms in action anyway.
*  So that's great.
*  So, so, I mean, we, you know, we could go on and on about feedback and recurrence has become really popular in the world as well.
*  And obviously brains are massively recurrent.
*  So this is a very extremely important thing to build into our models if we want to really understand how brains are processing information.
*  Another obvious thing that brains do is is create spikes, action potentials.
*  And I know you've done work on sort of getting around that essentially.
*  So you've you've modeled spiking like features by using complex numbers.
*  And we don't we don't need to go into that work.
*  I mean, people can can look it up and I'll point to it.
*  But basically you've avoided modeling spikes by going around it by using these complex numbers.
*  And like I just said, recurrence has enjoyed this rise in deep learning.
*  And its recurrence has always been there since the very beginning.
*  But it's sort of become more popular recently.
*  Do you think spiking is going to enjoy a rise at any point or are we going to use complex numbers always to avoid it at all costs?
*  Yes, that's a tricky question.
*  I have to be honest, because I have a lot of friends working on spikes and spiking neural networks.
*  You call you call them friends.
*  My my view is that so I think spikes potentially serve a I mean, a clear role in biology.
*  There is a an efficiency, right?
*  A kind of role. I know that, you know, there is, for instance, exciting work happening right now in hardware with what we call event driven cameras.
*  So those are cameras that are not, you know, measuring the response of every pixel location, you know, for every frame,
*  but rather only detect the change that's happening.
*  Right. So those are cameras that can, you know, with very, very small bandwidth transmit a lot of information, very, very high resolution information by being only sensitive to change.
*  I would say that, you know, spiking neural network would make a lot of sense in this context because, you know, these are the, you know, the notion of timing becomes much more explicit when you relate timing to change and things of that sort.
*  So I kind of like this line of work. And I think, you know, from a hardware perspective, there's a lot of very good argument that's being made for building chips of spiking neural networks because they have very low power consumption.
*  And it's true that our modern GPUs and our disaster in terms of, you know, the amount of power consumption.
*  So I'm all in favor of this line of work. And I think spikes makes a lot of sense in the context of minimizing energy use.
*  What I'm a little bit more skeptical about is the idea that, you know, if you have spikes in one of our modern neural networks, the magic will happen.
*  And suddenly they're going to start solving all kinds of problems that, you know, the current neural network won't solve.
*  And the reason I'm skeptical is that there is literally nothing in our modern formulation of neural network that would warrant that statement in the sense that there's nothing for this neural network to explicitly use spikes or the timing of spikes.
*  And so I think that that's where my skepticism is. I do not think this is necessary about, you know, whether we need spikes or not, because again, I think spiking neural network,
*  BA for the most part, very similarly to rate based non-spiking neural network.
*  I think what we should be asking ourselves is what it is that we need to add in modern neural networks so that they are able to maybe encode information that potentially cannot be encoded in a simple rate kind of base model.
*  So, you know, of course, I'm relating to a lot of old work and old ideas related to oscillations, synchrony, the notion of essentially multiplexing information in neural networks and the possibility of binding, say, visual representations to objects through the notion of synchrony, for instance.
*  And so, you know, you're related to the work that we've been doing. This is very much my philosophy.
*  The focus should be much more about how to extend neural networks so that are able to maybe leverage aspect of spike timing, whether you do it with spike or without spike, to me is irrelevant.
*  And in fact, you know, there's a lot of progress done right now in getting learning to work in spiking network.
*  But because of very strong non-linearity and non-differentiability of this neural network, learning is typically a pain in the neck.
*  And so to me, there is very little benefit in giving yourself the extra trouble of dealing with spikes, as opposed to coming up with formalisms such as, you know, complex value neurons and things of that sort that might enable you to build mathematical abstractions of what those neural networks are.
*  And so that's what this spiking network can do without having to deal with the nitty gritty details and the pain that comes along with dealing with spikes.
*  Yeah. And I know that you're all in on oscillations, too, and the importance.
*  And it's a fairly straightforward spikes are fairly straightforward to integrate with the oscillation world, right, in a network.
*  But your bet is building a biological constraint in a model, something like a spike, isn't by itself likely to lead to some insight that will later improve models.
*  I mean, there's this balance, right, because some biological constraints do lead to insights that improve deep neural networks like convolution, convolutional neural networks and all the H max H max works right.
*  But there are pain in the ass spikes, but you can't do back propagation, for instance.
*  And so, you know, you have to draw the line somewhere of what is important and what's not.
*  And so for you, spikes in themselves, maybe what computationally what they could give rise to, we could build in another way.
*  And that would be just fine. Just fine and much easier. That's easier. Yeah.
*  Well, that's always good. Yeah.
*  So what do you think is one of the, you know, one or two of the missing biological constraints that you think would help break open a new frontier in deep networks is oscillations and synchrony one of them?
*  Maybe, you know, again, we have very, very preliminary work. There are old ideas that have been around. I think, you know, the jury is still out.
*  I think we need to do much more work. I think we need to come up with, you know, kind of clear, better demonstration of their benefits.
*  You know, we've been talking about a few examples. We've talked about attention.
*  I mean, it's exciting, you know, which is one of the hallmark of kind of biological vision, working memory, attention.
*  And, you know, interestingly for me, I think there is this trend in image categorization even where, you know, attention network has now taken over.
*  And so, you know, people in computer vision are starting to realize the need for attentional mechanisms.
*  And in fact, you know, beyond image categorization, if you look at the field of visual question answering, again, all of the state of the art architecture incorporates some attentional mechanisms.
*  The same way I was very excited by, you know, the neural train machine, you know, the people have started to show the benefit of having neural network that can read and write into memory,
*  allowing them to solve tasks that would be otherwise, if not impossible, very, very hard for, you know, kind of standard convolutional neural network.
*  And yet, you know, I would say those attention network and, you know, memory network neural training machines are quite different in their implementation or even algorithms with, you know, what we know and understand about attention and working memory and memory more generally in biological vision.
*  And so I think, you know, there's still a lot of work that should be done looking at the interplay between, you know, this additional functions and with the potential for neuroscience to continue to inspire kind of computer vision.
*  We've talked about spike timing. You know, there's also a lot of minutiae that goes on, you know, the model of neurons, at least as implemented in kind of modern neural network is, you know, we're talking about the scale from zero to 100.
*  Where zero is the Machinac NP and 100 is like the perfect model with millions of compartments and all that stuff capturing every detail of neural processing.
*  I told you, I think we are at the scale of 20 being fairly optimistic.
*  You know, that said, it's not clear how much, you know, so we know that there's much more happening.
*  We know that computations happens happen at ten rights.
*  There are all these kinds of non linearity that are far from being, you know, even remotely captured by our simple models of neural function.
*  And yet we don't know, you know, what those biophysical mechanisms by individual neurons.
*  And so, you know, I think the jury's entirely out.
*  I think more people need to get on board.
*  More people need to try to ask and test the functional role of what does be of this place of this biophysical mechanisms.
*  Some of them will probably be epiphenomena of, you know, biological minutiae.
*  But it's very likely that many of them will would allow presumably neural network to go far beyond the capabilities of our kind of current state of the art artificial intelligence systems.
*  Do prospective students when they come and want to join your lab, are they just interested in deep learning?
*  And is that if so, is that a problem?
*  I hope not. So it's true that, you know, most of my graduate students and postdoc come like myself from a more mathematical and computer science kind of background.
*  But I think what what unite all of us is a shared vision that, you know, one, we care about biology and we want to understand biology better.
*  And two, that in the process, we might still have something to contribute to the current field of computer vision and I.
*  So I do hope that, yes, they care about deep learning, but they do care about genuinely care about leveraging knowledge about neuroscience towards improving deep learning.
*  I've heard you lament the lack of knowledge these days from people coming into the field of just basic computer vision kind of functions from the old days.
*  And where would you if you were interested, there's so much to learn if you were interested in positioning yourself to join a lab like yours, for instance, where the hell would you start?
*  You know, do you have a clear path of how to train yourself up?
*  You know, where would you begin?
*  Yes, so we take a blend of neuroscience, computer science, math and psychology courses.
*  Just cycle between them or?
*  Yeah, I mean, with a focus potentially on, you know, the interplay between taking enough courses in algebra and, you know, machine learning and deep learning.
*  But also a fair amount of course, percept, cognitive psychology, cognitive neuroscience.
*  And, you know, as a side note, that's I think part of the reason why, you know, being French and, you know, I live and work in the US and not in Europe.
*  What fascinates me about the American educational system, especially liberal college such as Brown, is that you have the flexibility of, you know, really doing, you know, just enough math, computer science, psychology and computer vision during your undergrad.
*  That is specifically tailored to your own interest.
*  And so I've seen, you know, amazing undergraduate students coming out of, you know, liberal art institution like Brown with, you know, just I mean, I so wish I mean, I'm literally jealous, you know, to get to that point.
*  It took me, you know, two years of class preparatory in France where we did math and physics, you know, kind of mindlessly followed by three years of graduate engineering school where, you know, I did more math and signal processing and computer science.
*  Again, without necessarily understanding, you know, what for.
*  It's only in my third year that I, you know, I specialize in computer vision, image processing, discovered artificial neural network, got really interested in the biological side of neural network, and then fell in love with neuroscience and really wanted to contribute to that field.
*  So, you know, six years before I get my first, you know, class in the course in neuroscience when, you know, I have students at Brown who are able to take in their first year an introduction to computational neuroscience where, you know, it's pretty unwavering.
*  It's pretty, you know, but they are able to learn just enough to get hooked on the topic and then then being motivated to take the right amount of linear algebra that they need the right amount of functional analysis, the right amount of neuroscience psychology so that they are, you know, really becoming experts in this field.
*  I think it's really underrated to always, if possible, have in mind the what for. Why am I studying this particular topic because it's going to make everything so much easier and faster.
*  Absolutely. Yeah.
*  Is there anything that you wish you could have done differently besides having, you know, that sort of tangible thing to grasp onto the whole time in your career because you've had a really, from the outside, it looks like a really nice path you went and you studied in a very famous person's lab and you've done great work and you've gone on and started your own lab.
*  Anything you wish you'd done differently?
*  You know, I always feel already privileged and, you know, I think I was, you know, I had a fair amount of luck my whole life.
*  You know, I was, you know, one of the big luck in my life was to get an internship in the Podium Lab at MIT.
*  This is this was my entry point at MIT. This is how I discovered research has done in the US.
*  I was never exposed to research up to that point.
*  And so I came into a lab where, you know, there was a fair amount of mathematician, people, you know, doing formal statistical theory.
*  There was people doing good engineering, developing, you know, designing computer vision systems or face detection and recognition.
*  And then all the way to people collaborating very closely with monkey electrophysiology groups.
*  And so when I arrived in the Podium Lab, you know, this was a complete eye opener where, you know, I'd never been exposed to this kind of interdisciplinary research.
*  You know, I know that Tommy gets potentially hundreds of emails per week.
*  I don't think there was anything massively special about my own email.
*  You know, a lot of it was luck, the chance to being able to land in his lab and then, you know, work hard, prove myself to be admitted as a PhD student, et cetera.
*  So I would say, you know, I had a fair amount of luck to your point.
*  You know, would I do things differently? It's really hard.
*  On the one hand, I kind of hated my undergrad again, doing things for the, you know, doing math, physics, computer science, without knowing why.
*  And I just had to suck it up.
*  And, you know, at the same time, again, it's hard to imagine my life being as happy and seemingly perfect as it is.
*  It's hard for me to argue that I should have done differently.
*  But I am generally jealous for what I see our students were able to combine both.
*  Right. So not maybe do as much rigorous studying in math and computer science, but get enough of it that they can also enjoy taking more neuroscience and kind of vision classes and strike this balance between fundamental knowledge that you need to acquire to reach a certain level of, you know, in science and research, but also doing research along the way and enjoying what they are doing in the process.
*  To me, it's invaluable.
*  Last question. And if you don't have an answer, that's okay.
*  But I'm just thinking sort of, you know, the idea of skating to where the puck is going to be, not where it is.
*  You're mired. I mean, you obviously have like a vision long term, but you're also working on your very, you're very in deep working on your projects.
*  And you know, that's going to take a long time and you're making progress.
*  But then if you if you had to think like, what would I be working on if I just wrote a grant from nothing? And what would what would be the thing to be working on 15 years from now?
*  You know, I think that X is going to be important 15 years from now and I want to work up. It might not be hot right now, but I want to work up to my knowledge base to be studying that thing in 15 years. What is that thing?
*  I wish I had an answer, but to be honest, I don't. I mean, I can't see the future.
*  As I said back as a graduate, you know, if you ask me back in the year 2005 that, you know, what the field would look like in 2015, I would have been so far off.
*  I would have never predicted what we're seeing. The field is changing so quickly that, you know, I, you know, I would like to believe that neuroscience will be, you know, continuing, you know, in 15 years to still be a
*  and cognitive science will still be kind of sources of inspiration. So continuing to try to reverse engineer brain mechanisms will continue to provide some. But, you know, it's it's yeah, I don't have a good answer.
*  Yeah, none of us do. Toma, thank you so much. So you're on Twitter. You're on Twitter at TSAIR. So you guys can find them there. And of course, at your lab website, I'll link to and I really appreciate the time and good luck moving all your your teaching online.
*  Thank you so much. This was fun. Thank you, Paul.
*  To get in touch with me, email Paul at braininspired.co. The music you hear is by The New Year. Find them at thenewyear.net. Thanks for your support. See you next time.
*  I don't know why. You trust the sky. You must like your lies from blue eyes.

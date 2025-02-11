---
Date Generated: April 19, 2024
Transcription Model: whisper medium 20231117
Length: 5925s
Video Keywords: []
Video Views: 714
Video Rating: None
---

# BI 165 Jeffrey Bowers: Psychology Gets No Respect
**Brain Inspired:** [April 12, 2023](https://www.youtube.com/watch?v=Nen4ifJpZUs)
*  You know, I've been doing a lot of work. My lab is working with neural networks. I'm a
*  fan of neural networks in a lot of ways. I do disagree about how people are testing some
*  of these neural networks and the claims that they're making about these neural networks
*  at the moment. And I was just struck by there was almost no reference to psychology. That's
*  where the mind comes in. It's like, how can one make a claim that this is the best model
*  of human vision and ignore 100 years of research in human vision carried out by psychologists?
*  Psychology just gets no respect. I mean, we need more, you know, people need to pay attention
*  because psychology has the beautiful data and relevant data for so many things.
*  This is Psychology Inspired. Just kidding. This is Brand Inspired. I'm Paul. But this
*  is a Psychology Inspired episode because my guest today is Jeffrey Bowers, a psychologist
*  and professor at the University of Bristol. As you know, many of my previous guests are
*  in the business of comparing brain activity to the activity of units in artificial neural
*  network models when humans or animals and the models are performing the same tasks.
*  And a big story that has emerged over the past decade or so is that there's a remarkable
*  similarity between the activities and representations in brains and in models. This was originally
*  found in object categorization tasks where the goal is to name the object shown in a
*  given image where researchers have compared the activity in the models that are good at
*  doing object categorization to the activity in the parts of our brains good at doing object
*  categorization. It's been found in various other tasks using various other models and
*  analyses, many of which we've discussed on previous episodes. And more recently, a similar
*  story has emerged regarding a similarity between language-related activity in our brains and
*  the activity in large language models. Namely, the ability of our brains to predict an upcoming
*  word can be correlated with the model's ability to predict an upcoming word. So a
*  common claim is that these deep learning type models are the best models of how our brains
*  and cognition works. However, this is where Jeff Bowers comes in and raises the psychology
*  flag so to speak. His message is that these predictive approaches to comparing artificial
*  and biological cognition aren't enough, and that approach can mask important differences
*  between artificial and biological networks. And what we need to do instead is start performing
*  more hypothesis-driven tests, like those performed in psychology, for example, to ask whether
*  the models are indeed solving tasks like our brains and minds do. So Jeff and his group,
*  among others, have been doing just that and are discovering differences in models and
*  minds that may be important if we want to use models to understand minds. So we discuss
*  some of his work and thoughts in this regard, and a lot more, of course. Show notes for
*  this episode are at braininspired.co.slash podcast slash 165. On the website, braininspired.co,
*  get more brain inspired stuff by supporting it on Patreon, or you can sign up to get a
*  short video series that I made about some of the open questions and challenges in understanding
*  our brains, our minds, and artificial intelligence. All right. Thank you for being here and thank
*  you for your support. Here's Jeff. Why do you hate brains and artificial neural networks
*  so much?
*  Yeah, a lot of people think that about me, and it's really not true. I've been doing
*  a lot of work. My lab is working with neural networks. I'm a fan of neural networks in
*  a lot of ways. I do disagree about how people are testing some of these neural networks
*  and the claims that they're making about these neural networks at the moment. And I do think
*  ultimately, I think what I would like to do is improve neural networks to make them
*  better models of the visual system. I've focused quite a lot on vision, but I'm also interested
*  in other domains, language, and so forth. So yeah, the goal isn't to somehow reject
*  them. The goal is to improve them. The goal is to have a better assessment of how similar
*  they are to the human visual system or the other memory systems or language systems,
*  because you really can't improve a system until you have a better understanding of how
*  good the correspondence is. So I would also say, I do think in the case of vision, these
*  so-called image-computable models, these models that actually take photographic images and
*  classify them accurately in impressive ways, and it is certainly no doubt an amazing engineering
*  feat. So there's no question about the engineering feat about this. But I also think they're
*  not the only game in town. They're not the only way to gain insights. And so I'm a fan
*  of deep neural networks as a promising approach. I think it needs to be approached differently,
*  but I'm certainly in my own research using them. But I also think models in psychology,
*  maybe models in neuroscience, they're not image-computable, but they may nevertheless
*  be insightful about how the brain works. And at the end of the day, a model really, I think,
*  is designed to increase our understanding of the human brain. And that's the ultimate criteria
*  you need to judge a model by. Well, you just mentioned the human brain, and I want to come
*  back to that. When did you get interested in helping improve these models? With the advent
*  of Alex Nat or something, 2012. Because I know you have a long history of arguing for symbolic
*  cognition over parallel distributed processing, and then just to bring it back to the human brain,
*  then. I thought your interest was more in the human mind than the human brain.
*  Yeah. I mean, obviously, I think the brain, when it works, it produces mind. But you're right.
*  I think, so I got my PhD way back in the early 1990s, not that long after the
*  PDP stuff was going on. I found it very exciting. And it's true, I was quite interested,
*  and I continue to be interested. At the time, I was somewhat critical of, or at least the big
*  debate back then was distributed versus localist coding in psychology. And I was at least open to
*  the idea that localist coding, so-called grandmother cells, might be a useful way to think about how
*  knowledge is coded in the brain, or at least not rule it out. So way back when, I was interested
*  in that debate. And then, yeah, I guess for a while, I continued to be interested all along.
*  But with AlexNet and all this excitement, I think what really generated my interest late,
*  and by late in the last seven, eight years now, is all these strong claims being made about how
*  these are the best models of human vision, or fundamentally improving our insights into how the
*  visual system works, or the brain works. And I was just struck by there was almost no reference
*  to psychology. That's where the mind comes in. It's like, how can one make a claim that this is the
*  best model of human vision and ignore 100 years of research in human vision carried out by
*  psychologists? And it just hit me as you go to the reference section of some of these papers,
*  and there's virtually no, or very few, if any, articles published from a psychology journal.
*  So I think that's been the theme of my thinking, because I've dabbled in various different areas.
*  And I think one thing I've always tried to argue in different contexts is psychology has a lot to
*  say. So I think sometimes people jump on neuroscience or artificial intelligence, and they ignore
*  psychology. And I'm fundamentally a psychologist. And when I see these claims being made with not
*  enough reference to psychology, that just kind of irks me a bit, I suppose. So that got my attention.
*  And so that got me back and get it. Like you said, I was way back in the 90s interested in some of
*  these questions, and I kind of got invested in researching. Things got updated. There's lots
*  to learn. And I was just in a way struck. An interesting feature about how things have changed,
*  I think, is back in the 90s or in the late 80s with the PDP, McClellan and Ramelhart and Hinton
*  back then, they were using neural networks, and they were really much more informed, I think,
*  by psychology. So they really were. A lot of them were psychologists.
*  Psychologists. And so they really focused on trying to account for psychological phenomenon.
*  And then, was it 2012? Is it AlexNet or something about that time? And subsequently after that,
*  a lot of excitement. But that crowd, first, the actual remarkable engineering successes was
*  computer science. And then people who got more interested, kind of starting to relate this to
*  them, to the brain and mind, more the brain, because they more focused on trying to predict
*  neural activations in the brain. And so again, their claims again about links between humans
*  again, but there was less contributions from psychology. And I think that was the big,
*  empty space that I decided to walk into.
*  So, I mean, that's often pointed to by modern people who use, let's say,
*  convolutional neural networks, people like Jim DeCarlo, Dan Yamans and that ilk, is that
*  these models, which were not built to, so which were engineering feats and were not built to model
*  specifically the visual system, even though convolutional neural networks were born out of
*  the Fukushima Neocognitron and what we knew about the way that the human visual system is supposedly
*  set up. But the astounding thing was that, lo and behold, when you actually do compare these models
*  to brains, it does predict through linear regression, predict neural activity. And
*  even more recent, if we're sticking to vision, more recent work, even you can find a cell and
*  figure out what image, however bastardly non-ecologically valid that image is, what image
*  will drive that unit the most in a living brain. And so that is sort of the astounding thing,
*  is that these quote unquote, best models of vision, and you can riff on this if you'd like,
*  best models of our human vision were not born out of neuroscience or psychology, but were
*  born out of engineering would be the claim. Right. Well, that's a claim, I suppose.
*  That's a claim. Yeah, that's the claim. Yeah, so
*  one of the findings, I think the main kind of finding that is used as empirical evidence that
*  these models are like the human brain is their ability to predict brain activations. And it
*  looks impressive at first, but what we know of basic fact about statistics is that
*  correlation is not causal, and you can have confounds that can predict quite well.
*  So you can predict off things that have no mechanistic similarity, just the mere fact
*  that something is predicting something else is, I suppose it's unnecessary, but certainly not
*  sufficient condition to conclude that there's a similarity there. And what you normally do
*  when you're concerned that confounds might be driving a prediction is you run an experiment.
*  You kind of vary independent variables, try to rule out certain possible bases of the prediction
*  and say, okay, if I vary something, how does that impact in the prediction? And in psychology is
*  full of the basic experimental method where you manipulate things, you understand something about
*  how something works by running an experiment. And those to me are the kinds of findings
*  that would be much more, they're more theoretically informative. You learn something,
*  if you run a, if you manipulate something and you find what affects something and what doesn't,
*  that gives you some conceptual insight of what's driving how is the system operating.
*  So yeah, so I just think good predictions by themselves are not secure in knowing how similar
*  the system is. And you could have, it could just simply be a confound. In fact, I mean,
*  primatation that just seems like very likely, you know, it is a confound in the sense that
*  what we know is, so, you know, I know you're familiar with brain score and they've ranked
*  hundreds of models on trying to get the highest brain score. But if you look at the models in the
*  top of the leaderboard, it doesn't matter if you look at any of these models, but even at the models
*  in the top of the leaderboard, they classify objects in a fundamentally, the most fundamentally
*  different way than humans could be, which is they rely on texture and they largely ignore shape.
*  So there's just immediately a bit of a paradox there. It's like, how can you have a model doing
*  good predictions about human object recognition and miss the, like, step number one? I mean,
*  I just don't think you could have a more basic criterion of developing a good theory of human
*  vision, at least at object recognition, is that your theory should be caring about shape and shape
*  representations. I mean, there's a lot more to say about what kind of shape representations you want,
*  but let's just start with step number one. It should encode shape. Now, the fact that a model
*  that does rely on shape gets a high brain score should raise serious alarm bells. And there is a
*  straightforward way that that could happen, which is there could be a confound that's driving the
*  good prediction. So for instance, you know, the shape of an object will correlate with its texture.
*  I mean, so, you know, airplanes have a certain shape and they'll have a certain kind of texture
*  and cats will have a certain shape and a certain kind of texture. Now you can predict,
*  potentially, a shape representation in a human brain on the basis of a texture representation
*  in a model. And so you could make a good prediction, but it's due to a confound. And then in fact,
*  people like Robert Garros did this lovely experiment, they ran a controlled experiment.
*  They ran these studies where they, you know, they said, well, let's run an experiment. Let's attach
*  the texture of an elephant on the shape of a cat and see how the model classifies that object.
*  Because the higher the brain score you get, you'd never know the answer is a texture or shape. Well,
*  you couldn't know you can't, you'll never know. You can get 100% prediction and you wouldn't know
*  on what basis is the good prediction being made. The way you find out is the way you've all people
*  have always done experiments, you've manipulated something. And so Robert Garros and colleagues
*  did that experiment and they found lo and behold, these models recognize things based on their
*  texture. So, you know, on the, you know, there's, there just seems like, well, hold on, there's
*  something seriously problematic with brain score as a measure when you get a high score
*  and you've failed on such a basic criterion. Now I know it's interesting. I still don't think it's
*  a, we can talk more about this, but I don't think it addresses the problem deeply. But nevertheless,
*  it's interesting that there are these new models, some transformer model with, I don't know,
*  20 billion parameters trained on, I don't know how many 30 billion images or something like this.
*  And that model does start to pick up on shape rather than texture. So, and so people point that
*  out, oh, scale is all you need. I mean, more, so more, you know, more training and then in fact,
*  the model picks up on shape. And I guess my response, two responses to that is, it still
*  doesn't point, it's still the case that the models on brain score, the top scoring models on brain
*  score recognize things based on texture. So that weighs this question on the predictivity measure
*  by itself. I mean, and, but then, you know, and then when people find that, oh, I can get a model
*  to recognize a cat that has the skin of an elephant as a cat, like a human does,
*  that's great. But that's still a pretty low bar in terms of our understanding of how human vision
*  and shape represent it. We know a lot from psychology, from lots of research over time,
*  about the nature of the shape representations that are employed by humans when they recognize
*  objects and recce, you know, so that's fine. It's great that you've recognizing based more on
*  shape and not based on texture. But to claim that that then a model of human shape representation
*  is a big jump, you know, again, you've, you've now passed step one, but there's lots we could,
*  there's lots of stuff we could do if you paid attention to the psychological research. And
*  there's, but that's, again, that's gets me back to my, you know, the thing as a psychologist,
*  I'm really trying to, you know, get people to pay more attention to psychology. And there's a lot
*  of interesting research out there. And I think people would find out that these models are
*  failing and more are more dissimilar than they think. And, but the great thing is, you know,
*  once you find a failure, I mean, the garros is a lovely example, as soon as you ran an experiment,
*  you found that there is a failure that is relying on texture, not shape, it immediately generates a
*  hypothesis of the kinds of things you need to do. At least now, you know, okay, our model has a
*  particular type of problem is a problem that is not working on shape. And then people like garros,
*  their first intuition was, was to train the model differently with the kind of data sets in which
*  shape was more diagnostic than texture. That was there. They changed the model, they changed the
*  training space, which is fine. I mean, the training, the particular training they did
*  was not particularly psychologically plausible. What they did is they said, okay, let's take the
*  shape of a cat and attach the texture of an elephant to that can, you know, there's a hundred
*  different kinds of call it cats. And each time, so now that, you know, the shape and not the texture
*  is diagnostic. So that's obviously not human like, but other people have done more realistic
*  training environments and found that, okay, you can start getting in the, but you can start getting
*  in the direction of getting a shape bias with better training. It may be different architectures
*  will do a better job as well. But the thing is when you ran an experiment, you knew what to try
*  to fix. But if you just did brain score and you got, oh, I got a brain score of 0.5 and then the
*  next model gets a model of 0.56. I mean, what have you learned? I mean, what do you know?
*  Have you learned, oh, that means it has more of a shape bias? No, you don't know that. You have no
*  idea what the increased predictivity advantage is due to. So that's what's good about it. I mean,
*  an experiment not only starts removing confounds, which is important, but it also gives you
*  a conceptual understanding of what the nature of the failure might be or the nature, hopefully,
*  of the success sometimes. I mean, it gives you a better understanding. And that's just like
*  running experiments. Why? It's fine to run big regressions on big data, just observational
*  data sets, but it's better to run an experiment if you can. And this is a domain where you can run
*  experiments. So why not?
*  I just, as you were talking about the shape versus texture, it made me wonder, and you would know
*  this better than I, sorry, this is an aside, but are there disorders of human cognition where
*  that is reversed? And you could find maybe a model for some disorder in these great vision models.
*  I mean, there's certainly various forms of agnosias. I don't,
*  and so you definitely can have, I mean, normally I think of agnosias as disorders of shape
*  perception. There's various different ways in which shape perception breaks down. Off hand,
*  and I used to know this literature, but I haven't followed in a while. I don't remember
*  a form of agnosia which people make judgments based on texture. It's certainly the case that
*  people, if you have post-agnosia, you might be recognizing things on local features,
*  which actually is a little bit like a neural network might do sometimes as well. And so you
*  might recognize somebody because they have a big nose or some particularly distinctive feature,
*  and you're not recognizing faces in the normal way. But whether it's texture or some local feature,
*  but it's possible, but it just hits me as an odd,
*  maybe, okay, you train a model to classify objects accurately and you get a good theory of
*  disordered human vision. Maybe, maybe, but you have to then run experiments to test your theory.
*  Okay, it's just really like a form of, I mean, there's going to be a vast large interesting
*  neuropsychological literature that would probably then something that you should run
*  experiments to determine whether that's true or not. I mean, so running experiments, a current
*  controversy maybe or a current criticism of the way that, for example, neuroscience has been done
*  the past 50, 100 years is that the experiments are too controlled and that the animals and humans
*  that we're experimenting with, because they're not ecologically valid situations, that we're
*  going to get results that are tailored to the experiment or the experimenter and not how it's
*  actually working in the brain and or mind. And in these really highly controlled, low
*  number of stimuli kind of experiments, that's kind of what you could be getting. But then
*  these giant data sets that the deep neural networks are trained on should in theory
*  dissolve that. They're not ecologically valid. And actually, I'm going to ask you about
*  what vision is for in a second because object recognition and categorization,
*  is that what vision is for? But inherently, these models that are trained on so many different
*  types of images and categories, you would think in principle would, if they are constrained,
*  like human vision is constrained, would have a shape over texture kind of bias in that one example.
*  I mean, there's lots more examples that you list in your recent paper as well.
*  So is the question should I agree that there are, I mean, there's no doubt dangers on both sides. I
*  mean, you could run experiments with artificial stimuli that you're missing the big picture,
*  I suppose. But so many of these studies, I mean, what is like a line drawing of an object? I mean,
*  what's so striking is we can recognize an object by its line drawing. In fact, there's a kind of a,
*  I can't remember the name of the, but a study done in the 50s, I think it was, I can't remember the
*  author of him. But he did this bizarre developmental study, but not bizarre, but kind of, I think about
*  the ethically questionable today. But today, he raised his child with the kind of ensuring that he
*  never saw a line drawing. So until two or three years old, the child, they did their best not to
*  let the child see a line drawing. And then eventually, so they had, I suppose, turn off
*  the TV when cartoons were on or whatnot. But eventually, it became too difficult to continue
*  this thing. But the child was old enough, I don't know, three or something, or two or something like
*  this. So the big moment happened is, okay, take a look at this and tell me what you see. And they
*  showed line drawings and it was trivial. I mean, it wasn't even, you know, there was no, you certainly
*  don't have to train a child to see line drawing. So there's an artifact, it's artificial in some sense.
*  I mean, until cavemen drew on walls, you know, there weren't line drawings, but it was,
*  it's not an artificial stimulus. But I think it's very informative about how human vision works.
*  I mean, illusions are such striking things to me. I mean, I just seemed like, yeah, they're
*  artificial. I mean, sometimes, you know, there are real illusions that occur in the world and
*  natural context. But it just seems odd to me to think that those aren't important constraints on
*  how the human visual system operates. And to call them artificial would be, well, yeah, I mean,
*  that's, you know, we kind of, that's what an experiment is. You kind of find particular
*  circumstances and it works when something happens. And that just seems important to me. I mean,
*  but the thing is, in deep neural networks, and this is sort of what I'm doing with them,
*  I have a team of people. So in fact, the people on my team are doing all the modeling, I can't
*  model myself. So they're doing all the actual hard work. And you can, the point is, you can run
*  experiments on deep neural networks. So that's what you should do. That's, you know, that's sort of
*  the main, I mean, you know, one of the main messages, you know, another message is, there
*  are other approaches to modeling as well that we should dismiss out of hand. But what I'm doing in
*  our lab is running experiments on deep neural networks. So there's no reason why if you're
*  absolutely committed to having an image computable model, and I think this commitment is,
*  you know, it's a nice thing to have an image computable model, but I just don't think that's
*  entry point to doing good research, you know, but anyways, you know, all right, so you want to work
*  with image computable models, you want to ignore any model that's not, okay, that's, you know,
*  you're free to do that. But what you really shouldn't do is not run experiments with your
*  model, you should run experiments and find out whether these, you know, artificial stimuli are
*  producing results that resemble human results. So if they don't, you might have, I mean, I'm sure
*  there are some phenomena that are potentially not interesting. I mean, you know, I mean, it's not
*  that you have to count, you know, I mean, I think some phenomena are no doubt more interesting than
*  others. But you know, like, recognizing things based on shape is not one of the things you can
*  ignore safely. But yeah, one of my favorite examples that you give in fooling artificial
*  networks or showing that they don't categorize the way that humans do is the single pixel
*  example. Can you just describe that? And then we'll come back to and then I'll have some
*  follow up questions. Sure. Yeah, so this is an experiment run by Gerov Malochov, where what we
*  did is just added a confound in a stimulus set. So we use this very simple data set called CIFAR-10,
*  which is just 10 categories each with, I think, 60,000 images. So it's a compared to what's
*  normally used image net, much smaller, easier model data set to work with. And we simply
*  added a pixel like, you know, we had different conditions. But one of our conditions was a
*  single pixel where you'd say, okay, every time you see a plane, put a pixel of a certain hue in
*  this location or in this small region of space. And every time you saw a horse, you put it over
*  here. And every time you see a bus, you put a certain pixel over there. So now there's two
*  kind of diagnostic cues for the classification that a model in principle could pick up on.
*  They could pick up on the overall, well, shape or texture, in fact, texture,
*  probably overall texture, really. But anyways, some, you know, something that you think, you know,
*  the whole image itself is used. Or alternatively, you could do it, you know, sometimes called a
*  shortcut, you could just exploit this single diagnostic pixel. And that's what the model does.
*  The model will decide, you know, what's a lot easier because the model does, you know, the model
*  just wants to classify it. There's no reason it should do it like a human. And so when given that
*  those data sets with this kind of confound that we just artificially inserted, the model chooses
*  that shortcut. And so what happens is that if you then attest, give a picture of a plane,
*  but put the pixel where a bird was, the model will, you know, from a human person, you know,
*  it looks exactly like I came over and I said a plane. Horse. Yeah. Whatever it was. Oh, yeah.
*  But the model will come jump is an idea. You'll say, oh, I think that's a bird because it's just
*  all it knows is the pixel doesn't learn it. It's just focused on the pixel. So and because.
*  Sorry, I was going to say, because the pixel in that case is the most predictive thing of that
*  category. Yeah, that is the most predictive, or at least it's the easiest thing to pick up.
*  They're both in principle, the human could, you know, pick up on either. And it could get
*  essentially in C part. Both are, you know, at some level equally predictive. But but the prediction
*  on the level of the image is a more complicated, challenging set of invariance is it has to pick up
*  on it just picks up on the simpler feature that it can pick up on. Whereas a human being doesn't
*  even notice there's a pixel there. So and data sets are just full of confounds. And some sometimes,
*  you know, it's nice in our experiment, we, you know, we know what the confound is, because we
*  inserted it. But in in naturalistic data sets, God knows how many confounds there are. And, you know,
*  some of them you won't see. But you know, some of them are things like what texture is correlated
*  with shape, that will certainly be one. And that's no doubt, I think why models, to our surprise, I
*  mean, I don't think the expectation was prior to Gero's that the model, you know, was relying on
*  texture, not shape. I mean, but turns out it did, because that's just an easier feature to pick up on.
*  In something like cancer diagnosis, right, where where a deep learning network is being used as a
*  tool to look for anomalies or something, you know, what detect pixels, you know, like little that's
*  like little clusters of pixels, right, that might not be detectable by the human eye. In that regard,
*  you would want a superhuman, for lack of better term, a machine that can attend to all pixels,
*  equally well and doesn't run out of energy and can make decisions based on taking in entire, you know,
*  entire images and statistically go over all the pixels and see if there is any anomaly.
*  On the other hand, you know, that's not how humans work, even though we can get pretty good at that
*  kind of stuff. And then there's the question of whether we want these things to work like humans,
*  or to work differently than humans, or better than or just differently, or whether it even matters.
*  Why would it matter for one of these networks to function the way that a human mind or brain does?
*  Yeah, if you're an engineer, I mean, it doesn't I mean, you know, my, you know, my, my critique
*  doesn't apply. I mean, well, I do think if you take the example of, you know, these, these models that
*  are trying to detect cancer and things or make diagnosis, I mean, it turns out that these models
*  often pick up on confounds that you don't want them to pick up on, because it turned out that
*  there's just, you know, is a particular logo on the hospital, you know, corner or there might be,
*  if people are lying down versus standing up, there might be some weird kind of configuration
*  that you weren't aware of, but actually, the model picks up on that. So confounds are a problem
*  in that engineering, pure engineering context as well. But as, but if you put away, you know,
*  if you put aside the fact that, you know, that's, you know, if the confound is going to allow you to
*  on a test set, diagnose correctly, you know, you don't actually care in a way, I mean, if it's,
*  if it's picking up cancer cells or some extra correlated thing that's associated with cancer
*  cells, and you thought, you know, you thought it's picking up cancer, in fact, it's picking up,
*  you know, a byproduct of cancer, who cares, as long as you're correctly identifying
*  some x-ray that's starting to needs to be picked up. And then it's fine. I mean, you know, I don't,
*  you know, models can outperform players in chess and go and, you know, and that's, you know, I have
*  no nothing but kudos to any engineer that built this stuff. Fantastic. I mean, it's impressive.
*  Who would have thought? But also from an engineering perspective, there are people who
*  are interested in building, you know, general and generally intelligent agents, right? Someone who
*  could detect cancer perfectly paint your house perfectly. I don't know, tell you what cartoon
*  you should watch next perfectly, whatever that means. Yeah. And, and which is a different task
*  than understanding the brain and mind. And I understand that you are more interested in
*  understanding the brain and mind than, you know, building these sort of general, I know that you
*  are interested in general, generally intelligent agents, but I mean, how much of the mind and brain
*  do we need to emulate if we want to build general, generally intelligent agents? And if you know what
*  a generally intelligent agent is, you should let me know. Yeah. Well, I mean, I think, you know,
*  one of the messages that we're doing in our research is that there's often, you know,
*  multiple ways to get an outcome. There's, there's shortcuts. So, you know, you can,
*  you can classify images based in ways that, you know, you didn't think, you know, wasn't the way
*  you imagined. There's probably multiple ways to achieve some goal. And yeah, if you can get a car,
*  they can drive you home safely at night based on training and on trillions of miles of, you know,
*  simulated driving and then, you know, and things like that, you know, I'd be happy to have a,
*  you know, if once it works, I'm all, I'm all for it. And it's, and, but the idea that that's how
*  human learn to drive would be, you know, absurd because it's been trained on a trillion miles of,
*  of data. But so yeah, you know, if you can, if you could train a model on all, you know,
*  relevant human skills and you just have a whole collection of, you train it with an exorbitant
*  amount of data and the driving context and an exorbitant amount of training and language
*  context and an exorbitant amount of training on image data sets and, you know, you know,
*  motor, you know, I don't know, robots that are somehow eventually trained in, you know, ways,
*  you know, you can capture all the forms of intelligence that would be useful for us.
*  If then I'm all, I'm all for it. It's just, but I know, but like you say, I'm a psychologist. So,
*  you know, to me, the question is, to what extent is success on these tasks,
*  a demonstration that it works like the brain, but yeah, I don't have any magic definition of what
*  general intelligence, general artificial intelligence should be, but I guess a model
*  that just was very useful in helping us in our daily life and doing all the things we want to do.
*  I suppose that would be, you know, a practical way, but don't confuse that or just at least
*  certainly don't assume that that's a human based solution. But you think it's worth continuing with,
*  I'm just going to put everything under the deep learning umbrella and then to understand our
*  brains and minds better. And if that's correct, what, you know, what is the solution? You know,
*  the term inductive biases is thrown around a lot. We need to put more,
*  constrain these systems in a way that we're constrained more that we have to move about
*  the world. You know, are we going to have to essentially emulate all things that humans and
*  animals do to build and test these systems correctly? Or since there are multiple ways
*  to skin a cat, are we going to find 14 different unique solutions until, you know, once you're
*  satisfied to satisfy, to eventually satisfy you rather? So you're asking me now back to
*  emulate the brain as opposed to just solve an engineering test.
*  Well, yes. I mean, whether, yeah, I mean, how much are we going to have to emulate the brain
*  to understand the brain and mind? Yeah, it's a good question. I'm skeptical that
*  we're going to be able to, you know, use, I mean, you know, the one approach that
*  people are adopting is that scale, you know, scale is all you need, more training,
*  you know, basically use the architectures. Okay, maybe go from convolutional models to transformers
*  but, you know, somewhere we got something as architecturally we're kind of close,
*  but the training environment or the objective function or, you know, some, you know, some extra,
*  and that may be, and, you know, proof is in the pudding, we're running experiments and find out
*  how far you get. I mean, but I mean, there are just such striking differences between what these
*  models look like and what brains look like and the assumption that, so, you know, all these models
*  have, you know, have units that are effectively all the same as each other, other than the connection
*  ways they have to other units. So, I mean, we're, you know, and they're not spiking, you know, so we
*  have more, you know, if you look at a brain, there's, you know, hundreds of different types of neurons
*  that have incredibly different, you know, diverse morphology and they vary in ways that would, you
*  know, potentially be important computationally. They have different, you know, time constants as
*  how long they integrate information. They have different, they conduct information at different
*  speeds and they have spikes in which the timing of spikes is really quite essential into whether
*  information is communicated and, you know, there's endless other kind of differences and sort of the
*  assumption is that we can ignore all that. We can kind of assume they'll be functionally equivalent
*  if we just train a model in which the only adaptive area of change is a synapse between units in which
*  everything works in fixed time steps and there is no other form of variation. Now, that may be true,
*  but it's, but, you know, A, it would be if you want a model of the biology of, I mean, it,
*  you know, maybe as a psychologist, I don't, I tend to imagine that these varying forms of variation
*  matter and they may give you some capacities that you wouldn't otherwise have or even if they don't
*  give you additional capacities, they make you, they make you manifest your capacities in a certain way
*  that are interesting from a psychological point of view. So just to ignore all that is,
*  is, it's a big gamble. And, you know, and again, test your models, see if it works. But, you know,
*  I wouldn't be surprised if you're missing something important by ignoring all these forms of variation.
*  And, and, you know, I guess the assumption is that people often talk about, well, you know,
*  when we train a model endlessly, you know, with, you know, more and more, you know, we're going to
*  eventually get there. It's like some, as if the learning of the model, some combination, some of
*  the learning is sort of like the in life learning, you know, the learning that happens in a lifetime.
*  And a lot of this other training is sort of emulating the evolution in the first place,
*  you know, somehow you just can get everything, you know, it's always, you know, I don't know which
*  part of my outcome was a product of what, you know, what, what we'd call evolution and what we call
*  learning. But at the end of the day, the answer I obtained is like, you know, I'm going to be able
*  to answer. I obtained is a lot like the brain. And the thing is, you know, evolution is not
*  constrained by changing just the weights between neurons. I mean, evolution produces
*  whole varieties of, you know, again, a wide range of morphological forms of neurons, all of which,
*  you know, may change, you know, the architectures change, the properties, the neurons change,
*  and all of that is outside the scope of these models that just change their weights. So whether
*  you're in the possible space of a solution that's going to be a biologically, you know,
*  interesting, biologically, a close correspondence to humans is a big, it's certainly a failure at
*  the single cell at the neuroscience level, they're trying to understand, you know, if you say what,
*  why, you know, why do we have this morphological diversity of neurons? Well, you're not going to
*  get an answer from a model that has every neuron is the same. Whether, whether you'll have a
*  psychologically equivalent model that okay, we could just ignore those forms of variance, and
*  we'll get a functionally equivalent thing. Okay, well, that that's in the realm of possibility,
*  but it's not it's not a, I don't think we should say it's a safe bet, you know, and
*  but one way you're never going to find out is doing more brain score. I mean, you're going to
*  have to run experiments to see whether these models function in the way that a human visual
*  system functions or language system functions. But it just seems to me, a very unsafe premise
*  to assume that just changing weights, the only relevant form of learning and computation in the
*  brain isn't synaptic changes and ignoring other forms of variation in the brain. I'm just repeating
*  myself. It seems unsafe. Yeah. Yeah. So in some sense, okay, so I'm sure you're aware of the idea
*  of multiple realizability. And people like Eve Martyrs work who show that given like a the same
*  set of a small number of neurons, you can still there are lots of different ways that you can
*  come up with a behaviorally relevant behavior outcome to produce the behavior behavioral
*  behaviorally relevant outcome. I'm repeating myself. And in some sense, though, like, so then
*  you have this like problem space in Eve Martyrs work. It's like the stomatogastric ganglion,
*  right? So the problem space is how to digest food and stuff and contract the muscles in a certain
*  way. And that constrains in some sense constrains the possible solutions, although there are lots
*  of different solutions to do that. And so one of the again, I'm at a loss maybe to ask you a
*  question about this, or maybe just ask you to comment on it. One of the impressive things,
*  maybe about neural network models is that even though they are so divergent from our biologically
*  realistic, because they're biological brains, that maybe if the problem space is the same kind
*  of problem space, they'll converge on a solution within the space of possible solutions that are
*  still valid, right? But then that goes back to the question of like, well, are we just giving them
*  the wrong training data? Or are we asking them to solve the wrong problems? So this is where I was
*  going to ask you what our vision is for? Is our vision for object detection?
*  Yeah, yeah. Well, almost certainly. That's not the, you know,
*  I mean, we can classify objects, we can label objects, but you know, our visual system obviously
*  evolved from, you know, vision has been around a long time. I don't know how far back vision goes.
*  And we, you know, evolution kind of descent with modifications, we've adapted our visual system is
*  based on much more species long, long, long gone. And yeah, I don't think they were labeling
*  the images in their world. So the visual system is, is no doubt. And, you know, and so our history,
*  you know, evolutionarily, in time scale, it wasn't all about that. And then in our own lives,
*  it's not all about that. I mean, obviously, we're, you know, we manipulate objects, we walk around
*  the world. I mean, what one of the ways that people talk about things is that, you know,
*  what we're doing is trying to infer a distal representation of the world. So we have this
*  2d image projected on our retina, and we're trying to infer a three dimensional representation of the
*  world. And it's an ill posed problem. I mean, we have, you know, going from 2d to 3d means that
*  you're in principle, there's a lot, you know, the infinite principle, different worlds out there,
*  they can project the same 2d image on our, on our eyes, we need to kind of have some assumptions
*  about the likely causes of this image on our retina. And that's where these kind of various
*  priors come in. But we're trying, the argument is, we're trying to build a 3d representation,
*  because that, you know, a distal representation of that world, because once you have a distal
*  representation, ideally, you can do lots of things with that, you can reason about the objects, you
*  can, you know, you can, you can grab them from different points, you know, different perspectives,
*  you can kind of, you can do lots of things. Whereas, you know, what, what, I mean, not all,
*  I mean, models, there are more and more people are developing self supervised models. And so not all
*  the all the models are only classifying images now. But yeah, most, you know, the models and
*  brain score for the most part, are they don't, they don't compose a three dimensional representation
*  at all. They don't, they're taking a 2d surface representation of texture and labeling it. There's
*  no, there's no attempt to infer the distal representations of the objects in the world
*  from those images. It's just a 2d mapping onto a label. And that's clearly not what our visual
*  system is doing. Again, what do you make of that fact that you get a high brain score in a model
*  that's not composing 3d representations, it's not organizing the scene by gestalt principles or
*  performing constancies or all these features that we know about human vision
*  are just not part of the task of or they're certainly not,
*  they're not necessary for a model that's trained in a supervised way to classify 2d representations
*  in a labeling task. And the hope and, and it's, I think it's definitely worth pursuing is that if
*  you get much more sophisticated training, you know, a much more realistic,
*  you know, a more realistic data set to train and you're not classifying static images,
*  but you're predicting, you know, predicting images and you're developing embodied representation in
*  the world and you're kind of developing a robot that's kind of learning and grabbing things.
*  And then, you know, almost certainly, I don't doubt that a lot, you know, some of the things that we
*  see in human visual properties are going to manifest themselves in a much, you know, once
*  you have a much more realistic training and a better objective function, I don't, I would be
*  surprised at all if more and more of these properties of human vision start manifesting
*  themselves in a deep neural network. But I also would be surprised if some things are just outside
*  the scope of current models are just not going to ever find themselves in the human space because
*  they're just working with neural networks that, you know, for one thing, don't spike, they don't
*  have morphological diversity in their units. And they're not the product, they didn't start from
*  the evolutionary starting point that human visual system worked from, which at times had very
*  different functions in the first place. I mean, there's lots of things that, you know, our bodies,
*  you never would have, you never would have ended, you know, if you started from scratch and you tried
*  to evolve something, you probably wouldn't come up with a solution that humans have done, but
*  the reason humans ended up with a solution that was sort of adaptive, having a weird evolutionary
*  history and you started, you know, once you get to this place, the best solution is here, but you
*  never would have started there. And I don't expect, I mean, even like the silly thing that our
*  photoreceptors are in the back of our retina, right? We have all this light that's, you know,
*  it's going through three layers or more of other neurons in the retina. And we have a big blind spot
*  because, you know, the ganglion cells are leaving from a part of there and your veins blocking the
*  light and all these different things. I mean, if you, you know, an engineer would decide on
*  adaptive grounds for that. I mean, it turns out that there's lots of other constraints that you have.
*  Yeah. So humans have it hard, animals and humans have it hard. I'm not sure. I think the octopus,
*  there's some weird animal that doesn't have them. The photoreceptors are at the front of the retina.
*  So there's like one, I think it might be an octopus. I don't know if octopus have eyes,
*  maybe I got really wrong there. But there's some animal that doesn't do it. But I think for some
*  reason, most animals have the photoreceptors at the back of the retina, which just from a surprise,
*  you know. And then, so then the individual system is, you know, is confronted with problems
*  that it wouldn't other. And so there are these interesting ways in which we have filling in
*  processes and there's a whole, you know, there are ideas, you know, people have developed like
*  people like Steven Grossberg and others have developed interesting architectures that are
*  trying in part trying to rectify the, you know, terrible signal that's being projected to the
*  photoreceptors. But that's just sort of like, so, you know, so there are actually important,
*  you know, cognitive visual low level visual processes that may be only manifest only required
*  because the nature of the input. But you know, these models, you know, they don't have those
*  problems. In fact, they have just equal tend to have equal acuity across the entire space and
*  they don't have any. So, so whether if you train the model more and more stuff, but you didn't work
*  on getting more realistic retina, you may begin with a very, you know, missing important parts of
*  filling in phenomena and then, you know, things that, you know, might not,
*  it's not even a problem to solve.
*  Well, maybe octopi can't fill in. That's something to test. You know, thinking about our evolutionary
*  needs and projection. I mean, do you think that homeostatic needs and life processes
*  a sense of autonomy and, you know, the fact that our bodies regenerate and have to maintain itself?
*  I mean, how important do you think that is to our quote unquote higher cognition?
*  That's a good question. Yeah, I mean, I think
*  I may not be answering your question, but things like, you know, you know, I sort of get this,
*  you know, embodied cognition. I think, you know, that's just a robot where a robot is not,
*  doesn't have to be autonomous. We can just give it a battery. You know, it doesn't have to,
*  it doesn't have to maintain itself for instance. Yeah. Well, yeah, I, I'm not 100% sure I know
*  what you mean, but I do think that, you know, all of the, they'll have, you know, achieving
*  homeostasis is certainly to be important for the, you know, hypothalm, or the, you know,
*  hypothalm. The lower, the lower brain. The lower bits for sure. The higher bits, I expect so too.
*  I expect everything is going to be at some level,
*  constrained, you know, whether that's the place to
*  constrain, you know, a series of human vision. I, you know, just, you know, that may not be the
*  place to start. I mean, I think, but. Do you think that we, let's say just humans, right, are
*  implementing algorithms, straight up algorithms and objective functions, or is it messier than that?
*  Or, you know, is that, is that just like the, an algorithmic solution to something, a necessary
*  means to attain that thing, whatever the algorithm that's needed at the time? Or do you think that
*  we have just by hook or by crook come to develop a bag of tricks? I think someone like Gary Marcus
*  might say to, you know, to serve as objective functions and algorithms.
*  Everything, I mean, I mean, the neural network is, you know, so by algorithm, you mean like symbolic,
*  some kind of list kind of like. No, just a set, a set of concrete predefined steps to determine
*  a solution to a problem. I think the brain clearly can do that. I do, you know, I mean,
*  I do think the brain does have a bag of tricks. So I think there are, you know, lots of hacky
*  solutions and, you know, satisfying in many different ways. So I don't doubt that at all, but
*  you know, we can have an algorithm for, you know, addition and multiplication. And, you know,
*  so we can kind of very strategically, I mean, I might relate to the system one, system two, condiment
*  kind of thing. So we certainly can implement kind of rational. What portion do you think?
*  Yeah, I don't know. Of our cognition. I mean, I do,
*  I do think we need some, one of the things that certain types of models of vision or language have
*  are, you know, these compositional representations where you have the kind of explicit encoding of
*  relations and elements that can bind in various ways to these things. And again, it's Gary Marcus
*  or people like, you know, Jay Fodor and vision people like John Hummel and Biederman with the
*  Gion theory, with structural description theories, where you have an explicit coding of parts and
*  the relationships between parts. I do think that's very likely an important component of human
*  vision. I mean, I do think that, you know, coding relate. So one of the things I was mentioning
*  before that it's not enough in theory of vision just to say, oh, I can, I recognize this thing
*  that has a shape of a cat and the texture of an elephant, or that must be a cat. So that's,
*  okay, that's good, because humans do the same thing. But there's a lot more about shape
*  representation. So one thing about shape representations is that we recognize objects
*  based on their parts and the relationships between the parts. And we have an explicit
*  representation. At least that's what we'd argue in some of our research and other people long before
*  I would say. And I think that might be really hard for a lot of these models. I mean, even people like,
*  you know, so people like Biederman and John Hummel developed, or as Hummel and Biederman in 1992,
*  have this great psych review paper where they kind of implemented the Gion theory of object
*  recognition into neural network 30 years ago, no, more than 30 years ago. And it has a mechanism
*  by which you do dynamic binding of relations and explicit representations of relations and explicit
*  representations of parts and associate these things. But even recently, people like Jeff Hinson
*  are developing things like capsule networks. And this is kind of, I don't really, it has this thing
*  called GLOM. It's I think a conceptual idea, but he's trying to understand the hierarchical
*  relationships between parts and explicit representations. So, you know, and these are
*  not image-computable models. I mean, so he's developing these non-image-computable models
*  that, you know, would do terribly on brain score. I presume we get a score of zero probably or
*  something. But he's developing these models to say, you need to develop models that code for
*  relations. And he doesn't do it in the way that Hummel did. Hummel had like synchrony of activation
*  units. And Hinson has some routine mechanism of, which I couldn't tell you much about it really,
*  but it's an attempt to develop coding of explicit forms of relations and part relationships between
*  these things. And in both cases, sacrifice at the moment image-computability. Ultimately,
*  you're going to need an ultimately the human visual system works as a retina. And so, you know,
*  I agree. Ultimately, you want a model that image-computable, but whether that's the place
*  to start or whether you should kind of work with a toy model in order to figure out how can you code
*  for parts relations. And everyone from, you know, John Hummel to Jeff Hinton have adopted the
*  approach of playing with toy models to work and try to understand these relations, which eventually
*  you would try to implement in a full-scale model with image-computable. So, I don't know
*  that relate to algorithms or not. I mean, I think it relates to the idea of having an explicit
*  encoding of parts and relations and a mechanism by which that's achieved.
*  But it's not like an algorithm of, you know, long division.
*  Yeah. Yeah. Part of what one of the examples that you were just alluding to, or at least one of them
*  was, and I don't remember that, I know you've done work on this also, but basically neural networks
*  will judge if something is same or different based on like some trivial pixel displacement,
*  whereas humans won't be able to tell that difference, but humans will be able to tell
*  if the relations between two, for example, lines are different.
*  That's the kind of research that I'm talking about. So, we have this stuff where we kind of,
*  so this is stuff by John Hummel and I think a PhD student here, Stankovitch, back in the 90s,
*  showed that humans are highly sensitive to this kind of categorical relationship between object
*  parts and in these simple line drawing kind of things, like those kind of simple, people might
*  notice, Tarn Pinker had some kind of simple stimuli and they kind of slightly based off those
*  things. And yeah, in our research showed these models, current models, completely blind to these
*  kind of, you know, so they don't care about those things. We even tried to train the model on to,
*  okay, you know, okay, we'll train it on these relationships and, you know, we left out one
*  relationship, but we trained it on lots of other relationships. So, the categorical relationship
*  between parts matters here and here and here and here and here and then we have a left out one,
*  left out one, we say, okay, how, you know, and the model ignores it there. So, there, it's just
*  over and over, it's not learning the relationship, it's learning some particular local feature,
*  but it's not understanding the concept of a relation that then applies. And that's where
*  people like, you know, John Hummel says, you're never going to understand these, you need an
*  explicit representation of a relation that can take on any kind of, you know, kind of, you know,
*  object part and it's not a conjunction, it's not a single unit or some distributed representation
*  of a circle on top of a square, it's a circle representation, a square representation,
*  a relationship between those two and that same relation would be involved in representing a
*  cube on top of a cone. I mean, you know, you maintain, that's kind of the stuff that people
*  like Fodor and Polishin argue for, compositional representations where the parts, the complex
*  thing is composed of parts and the parts maintain their identity, you can combine them in new ways,
*  but you don't kind of just forget, you know, you actually have a concept of loves, you know,
*  that, you know, John loves Mary, Mary loves John, it's the same love, you know, it's not like these
*  are just different things. Hopefully it's the same thing, who knows? Maybe. That could be argued.
*  Anyway, so, you know, it's possible some of these massive models will kind of pick up these things
*  in a way that, you know, are compositional, but, you know, our experience, I've worked with in our
*  lab, we've used models where we learn what are called disentangled representations, we take these
*  variational autoencoders, you take an image and you reproduce an image as some variant of the input
*  and you can kind of train in a certain way with certain kind of loss functions that leads the
*  model to learn what are called disentangled representations, so it's kind of this unit
*  in the hidden layer is coding for the exposition of the object in the scene and this is the Y unit,
*  this is, you know, the level of activation of unit number three codes for its shape and so on.
*  You learn these kind of, sort of grandmother-like representations, they're not exactly grandmother
*  cells, but they're kind of interpretable locals, but those models don't support
*  combinatorial generalization, so even once you learn those things, you say, oh great,
*  that will be, that's the answer to now I should be able to kind of recognize,
*  I've seen circles on the right-hand side, I've seen, you know, but, and I've seen squares,
*  but I've never seen this on the right-hand side, but I've never seen a blue square on the right-hand
*  side, you know, that combination, you know, having learned those disentangled representations,
*  you still fail when you combine these features in a novel way, so there's something, there's,
*  I think, a real challenge about how you solve these kind of combinatorial
*  compositional representations, it's a challenge and, you know, maybe these models will do it,
*  but maybe you need something, again, qualitatively different than what these models that we're
*  working with at the moment.
*  Well, I want to ask you about language in a moment because you've done some fun tricks with
*  languages, the large language models, but before we leave the vision aspect, taking us back to
*  comparing brains and, well, two different brains or two different models or a brain versus a model,
*  something that you write about a bunch is representational similarity analysis,
*  and this is a way to basically see the correlation between how a model and its given units are
*  representing pairs of objects, for example, versus how a brain or different model or something
*  would be, and you don't like representational similarity analysis because you can get a high
*  score saying that the representations are very correlated between, let's say, a brain and a
*  model, and still you have these psychological disparities with the psychological experiments.
*  If I didn't explain that correctly or if I don't have that correct, you should correct me before
*  I ask you a question here.
*  That's right.
*  Okay. Okay. So, and we've talked about those a little bit on the podcast, but we don't need
*  to go into detail on them. Another thing that people are looking at is the sort of low dimensional
*  dynamical structure between artificial networks and brains, especially in recurrent neural networks
*  and finding that there's a similarity between the low dimensional structure on, let's say,
*  manifolds and that the trajectory of neural activity through time is similar, often,
*  between a model performing a task and a monkey's neurons or something performing the same task.
*  I don't know how much into this kind of work you are or if you have opinions on it. I was
*  just curious if you did.
*  Yeah. In terms of the temporal dynamics and showing, I don't know too much about the temporal
*  domain about how, but almost certainly it's going to be another case of,
*  it's a kind of correlation. You're taking some kind of representation in the case of some kind
*  of representational geometry in the case of RSC. I guess some temporal dynamics in the case of
*  what you're talking about, which I don't know much about, and correlating with each other.
*  But there is an interesting paper that came out. I can't say too much about it, but it has to do
*  with temporal domains where they show that you can kind of predict, I hope I get this right,
*  you can predict ups and downs of Bitcoin based on neural activations in a monkey or in a rat,
*  so there's some kind of ability to predict well above, and they collect for statistical
*  chance and things based on relating brain activation of a rat in Bitcoin.
*  And this is probably, I don't want to listen to the details of it, but the reason I'm thinking
*  of it now is that it has to do with time dependency. So it's kind of like you can get these
*  spurious correlations and it hinges on time dependent things. So it may not apply-
*  Stochastic things probably.
*  Well, as long as you have some kind of-
*  Alpha rhythm or something in there.
*  Yeah, the state you're in now is auto correlated with what it was before, and you can kind of get
*  these various auto correlations between systems, and it depends on that it relates to the temporal
*  aspect of both Bitcoin moving up and down and neural firing of a rat moving in a maze,
*  and you can just get spurious correlations between these things. So I don't know,
*  but I just think it's very easy to get correlations that are very misleading.
*  It hadn't been Bitcoin, but if you'd run something that looked like a model,
*  you might go, oh, look at that correlation. If you only realize it doesn't mean very much
*  when it becomes an absurd correlation that you're measuring, but if it had been, this is my model
*  of something, then it might seem quite impressive. So I don't know. I don't know, but I do think that
*  these correlations that are found in RSA, correlations that are found in linear productivity
*  that you found in brain score are dangerous because they could be the product of confounds
*  or some other factors as well. There's another thing where just simply the number of independent
*  light factors, there's some paper that came out just having more sort of orthogonal-like
*  representations in architecture affords better predictivity, independent of whether the
*  representations are aligned. So there might be yet another kind of way in which you can get these
*  correlations that look impressive, but they're not necessarily informative of similar mechanism.
*  **Matt Stauffer** This all reminds me of the dead salmon in an fMRI machine experiment in neuroscience.
*  People put a dead salmon in an fMRI machine and recorded a bold signal, which is supposed
*  to suggest that there's brain activity. I think they have the dead salmon performing a task or
*  something. I don't remember the specifics. **Rick Paglia** I think it's a social psychology mind read.
*  **Matt Stauffer** Okay. Yeah. **Rick Paglia** Yeah, but I think that's a danger. You get these things
*  and you can get things that look impressive, but then you can do a kind of a reductive absurdum
*  kind of condition and you find that actually, well, the methods we're using doesn't mean it's
*  wrong. It just means it means you need to run an experiment to find out whether this correlation is
*  really producing the similarities that you think that they do. **Matt Stauffer** All right. So we've
*  focused on vision so far and I am aware of our time here, but you've done some fun things with
*  large language models in this same kind of vein. I know you haven't worked with them as much.
*  First of all, well, I'll ask you the question and then you can kind of
*  generally tell me what your thoughts are on large language models in general and especially
*  again, as models, the same kind of work that predicts visual model activity and compares it
*  to neural activity, this same kind of linear regression readout has been performed on
*  data sets like fMRI and EEG in terms of predicting an upcoming word, which is how these large language
*  models largely function these days. So maybe what do you think in general of these large language
*  models? And then I want to ask about how they can learn nonsense languages just fine.
*  **Roy Seidler** Yeah, well, I mean, like everyone else, I'm blown away by chat GPT. It's like an
*  amazing thing. If you asked me a year ago, you can have something that actually is so useful and
*  interesting. I mean, I'm not going to lie. I'm not going to lie. I'm not going to lie. I'm not going
*  to lie. I'm not going to lie. I'm not going to lie. I'm not going to lie. I'm not going to lie.
*  So I didn't see it coming. So again, amazing. I mean, I know some people are criticizing
*  and you can find cases where, you know, many, maybe many cases where it does silly things,
*  but overall it's bloody impressive. So I don't want to suggest it's not impressive, but yeah.
*  But the next step is, is it a good model of human language? And so that's a totally different
*  category, fish. And the, yeah, for one thing, it just hits me as
*  implausible in the sense it just seems unlikely that the language acquisition is
*  a product of predicting the next word. So the idea that children are-
*  **Jay Stoltenberg** So it's like solely a product of predicting the next word or the prediction
*  surely has to be a part of it. **Matt Stauffer**
*  Well, I think you're, you know, I would have thought what you're predicting is, you know,
*  you're trying to communicate ideas and, you know, you're hoping using words to achieve an end.
*  You want the cookie or you want, you know, you want someone to agree with you that that's a doggie
*  or something like this. So you're just going to have reference to the world. And then, and I don't
*  know too much about the syntactic capacities of one and a half year olds, two years olds, but
*  you know, I don't, you know, but I, but I don't, I really don't think that the child is as their
*  learning language, their primary objective is to predict the next word in a sentence. It hits me
*  as implausible. So in a way, it's sort of another example in my mind, I mean, with, you know,
*  but before we talk about any data, just kind of this striking example of how remarkable similar
*  something can be because it is, it just generates, you know, flawlessly lovely text,
*  syntactically coherent now, now meaningful in terms of useful things. I don't mean it means.
*  **Matt Stauffer** Okay. Okay. All right. I was going to.
*  **Matt Stauffer** Yeah. I don't want to go there, but I would say that I can, you know, I can read
*  this and go, that's a, that's a, it's a two one in my essay, you know, a student can get a, you know,
*  a B. So, you know, so it's a pretty impressive text that they could write, you know, so, but they can
*  get that from a system that had a completely wrong objective function, you know, or largely,
*  I mean, it's a, you know, it's one where you first were predicting the next word and then you have
*  this weird reinforcement kind of human in the loop reinforcement component, which is again,
*  you know, obviously not part of the mechanism by which children learn to kind of generate
*  coherent text. So, just as an example of how very different, you know, learning objectives
*  can produce behaviors that are eerily similar to human performance doesn't mean that the same
*  thing in a way, you know, or, you know, example I gave, you know, a couple of times on Twitter.
*  Twitter, I like that. Yeah.
*  The, you know, if you have a model like Dali that kind of generates images, you wouldn't say,
*  oh my God, that's the best theory of human drawing or painting. I mean, it's an amazing painting,
*  you can sell the painting and win a competition, a painting contest, but it's not, you know,
*  you know, it doesn't seem like a plausible account that it's the best theory of human painting.
*  And, you know, you can generate models of coherently meaningful text to a human being anyways,
*  and doesn't mean it did it like in a way like a human did it. So, I think it's a nice example of
*  how different something can be in its objective function and nevertheless emulate behavior,
*  you know, in an impressive way. Yeah, when it comes to the, okay, but then you can say,
*  okay, well, that's fine, you know, but Jeff, look at, you know, I can predict brain data,
*  you know, again, so it's again, it's again, it's a predictivity thing again, but so, you know,
*  there's a paper that came out, PNAS last year, I think, and they were claiming you can account
*  for 100% of explainable variants. That's shrimp-fed-all, I believe. Yeah.
*  That's right. That's the paper. And so they have a paper where they're making, you know,
*  it sounds very impressive. The first thing you find out if you go, you know, is that by 100%
*  explainable variants, explainable variants isn't that much because, you know, the amount of variants
*  you can predict one brain, the human brain from another brain is quite small. So, you know,
*  it doesn't account for 100% of variants, it's 100% explainable variants, and the explainable
*  variants is very small. So, I think 10% is like that. So, you know, so it predicts 100% of 10%.
*  But then, if you look carefully at the paper, you find out that it can predict,
*  in some cases, just as well, the brain activations and non-language areas. So,
*  it's like, okay, you can predict 100% of 10% both in language areas and non-language areas.
*  So now I think, you know, what's going on here? And that just, again, highlights, well, maybe these
*  predictions are not reflecting the mechanist similarities that you think. There can be other
*  ways in which you can get similarities that don't reflect mechanistic similarities. It seems to me
*  a problem that non-brain areas are, you can predict those just as well as brain language areas. I mean,
*  what does that mean? It means that this predictivity stuff is not doing what you think it's doing.
*  Or that language is distributed more highly.
*  And I think, yeah, that may, I think they have some, you know, they give some explanation about
*  semantics. Yeah, you could do that. And it's possible. But, you know, but all of a sudden,
*  the story is not quite so straightforward. And there's some questions that one should raise.
*  Yeah, so there's a bunch of these studies that there's another paper, but even smaller,
*  the amount of variance accounted for is, I don't know, 0.007%. It's significant, but it's so small.
*  So, you know, I don't know, I'm not very persuaded anymore that, I mean, the correlations are much
*  more powerful in the domain of vision. And I'm not very persuaded by them. So, you know, so that
*  you go to language domain, they're much, much smaller. And I'm not impressed by them either.
*  Yeah, but it's a different data set, right? Because in vision, a lot of the data sets are
*  from non-human primates where you're recording actual neurons. I'm not trying to argue with you,
*  but, you know, I'm just thinking there's probably a lot more variation in the fMRI
*  bolt signal in the EEG. Yeah. Well, it's definitely the case. I mean, because you get much less,
*  you know, what they call a noise ceiling, the amount one human brain can produce another,
*  it's much slower in language studies. So, yeah, so it's not, you know, it's not the fault of the
*  model that the noise ceiling in humans is so low. It's just the data is much more noisy, but that
*  that does, nevertheless, to some extent, weakens the evidence that one's presenting when one says
*  that, I don't know, kind of 100% of explainable variants. And then you find out, well, the noise
*  ceiling is awfully low. So, that is relevant. So, these large language models can learn English,
*  they can learn Dutch, they can learn French, and I don't know, all, you know, all the different
*  languages, learn them very well. They can also learn impossible languages, which is what you've
*  taught them to do. And, you know, you use the term meaning, and then I thought you're going to go
*  toward, you know, I thought you're going to start criticizing, you know, whether these large language
*  models understand the meaning of what they're producing, right? And to me, you know, when I
*  was reading your work on teaching these things, nonsense, impossible languages, that speaks
*  against the idea that large language models can understand the meaning of what they're generating.
*  But maybe you can clarify what you guys did. And then I don't know if you have comments on that
*  related to what that means about meaning in large language models. Yes, this is work with Jeff
*  Mitchell. So, he, and yeah, so we just train, you know, so, so this was a couple years back now. So,
*  this is pre-Chat GBT, and these are models of just was purely predicting the next word, there was no
*  other humans that leap and so it wasn't generating, it was generating syntactically coherent sentences,
*  it wasn't generating useful, you know, you know, it would just generate a ramble on and talk nonsense.
*  So, it didn't mean the meaning wasn't there because it was just talking rubbish after a while.
*  But the meaning for us. Yeah, it was the meaning, even the meaning for us was missing. Although,
*  at the sentence level, it might be meaningful to us. But at the paragraph narrative level,
*  it would start rambling off. And that's what the genius of chat GBT was against to reign these
*  models in to kind of be more meaningful for us. But anyways, the models could learn syntactically
*  impressive sentences, and they could do various, you know, subject, you know, verb agreement,
*  and number agreement between various grammatical markers. So, you know, so it could do things
*  quite impressively. So, in other words, syntactically correct sentences. And, you know,
*  the thing that people have been saying recently as well, especially with chat GBT is aha,
*  Chomsky is wrong. I mean, look, and we've demonstrated that you can learn syntax.
*  And these models have no universal grammar. They just been into some generic architecture,
*  there's nothing language is the same. I mean, in our case, it wasn't, I don't
*  nowadays, it's transformer, but it's not built, you know, that transformer can be
*  used in visual domains. I mean, it's a modify things, but it's nothing really about language.
*  And nevertheless, you can get these syntactically coherent sentences. And
*  so therefore Chomsky is wrong. But I think that's just a misunderstanding. Like Chomsky's story was,
*  I mean, and I'm no expert on the details of Chomsky for sure. But yeah, Jeff Mitchell might
*  know a lot more than me. But anyways, but the basic idea is that the critical thing about human
*  language is we have an ability to learn a language with relatively little data. A child is learning
*  to generate syntactically competent, you know, grammatically accurate sentences with relatively
*  little input with the claim that's kind of the poverty of the environment. And so,
*  but that comes at a cost according Chomsky. So you can learn quickly, but you have to kind of
*  abide by the rules of universal grammar. So we have inductive biases that allow us to learn certain
*  types of languages, and we can learn them relatively quickly. And so that's so we're constrained in the
*  languages we can learn in a normal way quickly, you know, in a natural way. But the benefit is
*  we can learn quickly. Whereas large language model have exactly the opposite properties,
*  which hit me as supporting Chomsky. So these models need a lot of data,
*  much more data than a human would require. And, but they can learn anything equally well,
*  there are no inductive biases. That's the reason they can learn anything,
*  there's nothing constraining them all to learn certain types of things. But so the benefit,
*  I suppose, if you want to call it benefit, it can learn anything. But the cost is it takes a lot of
*  training. But that hits me as not falsification of Chomsky that supports the idea that there's
*  something you know, doesn't support Chomsky's particular theory and Chomsky's theories have
*  changed a lot over time, but doesn't support any particular theory. But it does seem to me support
*  an idea that there are important, you know, inductive biases that a human being needs
*  in order to learn language quickly. So that's the, you know, that's the main story, I think.
*  And it's, you know, I've heard recently people, you know, again, informal conversations on social
*  networks and Twitter and stuff saying, ah, humans actually do have a massive amount of
*  exposure to language, a child does expose. But I don't think it's appropriate to say,
*  you know, words that they overhear as a child. I mean, if you just passively, just the words
*  around you are not contributing very much, I don't think to language learning. You have to actually,
*  there are studies by, I think this is right. So I, you know, I'm saying something that I'm
*  only 90% sure about this. I think it's Patricia Cool did some interesting studies. It may have
*  not been about syntax, it might have been about phonology, but aspects of language where if a
*  child is just kind of watching passively, you know, being exposed to a language, a foreign language
*  on a radio or television, they don't learn. So just passive exposure. So when someone says, oh,
*  a child learning, you know, exposed to 50 million words a week or something like that, just because
*  that's how many words are spoken around them. And that's maybe less than, you know, chat GPT,
*  but nevertheless, you know, it's not crazy. It's like, well, I don't think those are the relevant
*  kinds of exposure. To what extent are children actually engaged in language and keep children,
*  parents speaking to the child? And that's the more relevant number of episodes, not just,
*  you know, the sea of words around them that there might largely be ignoring. I mean, because,
*  so I do think, I do think there is a challenge for these models require a lot of training. Every
*  exposure is part of the learning environment of these models. The child's learning, it's not going
*  to be anything remotely as large as what's required to train chat GPT. So I do think,
*  you know, I think the large language models provide some evidence in support of the general
*  hypothesis that humans have inductive biases to learn certain types of constructions.
*  And they can do it relatively with little data compared to what a model can. I mean,
*  and there's a parallel kind of case that we've studied in vision where we've said,
*  at least it wasn't, I think it was Sammy Benjo and his lab, a few years, 2019 or something like this.
*  And we kind of followed up on some of this work subsequently, but they found,
*  you can train a model to learn, you take ImageNet and just convert all those million images in
*  ImageNet. So there's like a thousand categories, each with a thousand exemplars. And if you just
*  kind of make them all random pixels, like a TV static, so there's just absolute randomness.
*  There's no structure. There's no structure amongst the 1000 cat and members of category one.
*  There's similarly no structure of the members of category two. You can logically rotate. So it's
*  just a million random bits that are arbitrarily assigned patterns assigned to a thousand categories.
*  And you train a model and it can learn it. And it doesn't take that much longer than actual images.
*  I mean, it's sort of like, but that's not like humans. And in the same way, it doesn't seem to
*  have inductive biases in our language models like that. It can learn impossible stuff. No human
*  being is going to learn. Now, you can, to some extent in the human case, in language, you could
*  deliberately slowly kind of learn something about it, but it'd be like a problem solving exercise.
*  I don't think there's any reason to imagine it's the kind of language that would ever be learnable.
*  In some cases, they're just clearly not learnable. We had cases where the dependencies are beyond
*  short-term memory capacity. So these models, so a human couldn't do it because they couldn't,
*  you have to repeat a word at 27 times like that on the 28th trial, something happens. It's like,
*  well, you can't do that because it's beyond our human capacity. But the models
*  are exploiting that human, superhuman capacity to perform as well as they do.
*  When you're science-minded or have a science background like me, and you're talking about all
*  these different, the poverty of the stimulus and not subjecting how children aren't subjected to
*  words. I just automatically think about experimenting on my son and if we just
*  stopped speaking to him completely or started reversing nouns and verbs.
*  Speak backwards. Speak backwards.
*  Yeah. Speak backwards. Oh, that'd be rough.
*  If you could. I think that's the point. It'd be very hard to do that, but give it a go.
*  Do you know the phenomenon when, I'm sure you've seen this, when you can take every word in a
*  sentence and sort of flip a couple letters and you still read the sentence fluently,
*  right? And you don't even notice differences often. And even when there are harsh differences,
*  you know, even if you notice a difference, you can still read the sentence fluently.
*  Maybe this is just another experiment for you to perform to test psychologically these models,
*  how they perform with that kind of, with the anagram. I'm not sure what they're called,
*  but every word is kind of an anagram, right? Yeah.
*  We've done actually a little bit like some work like that actually, but they did surprisingly well
*  actually. Is that because there's so many typos on the internet or is there?
*  It's a good question. In our case, no, I don't think we trained it on typos. So the model,
*  so these letter transpositions, I mean, it's not quite true that if you read a word,
*  you transpose things, you don't notice it. I mean, some words are different.
*  Form and from. I mean, you can read those words. So clearly many words. And turns out there are
*  other, some language like Hebrew. There's some interesting studies in Hebrew where lots of words,
*  I think it's not only Hebrew, but some studies have been done in Hebrew where in Hebrew,
*  when you swap two letters, you produce another word. In English, you swap two letters,
*  you end up with just a nonsense thing. But in Hebrew, for just the nature of how
*  it is. And so human, so they're very saliently different. So if you transpose letters in Hebrew,
*  the visual systems learn to be very attuned to the orders of letters. Where in English,
*  because it doesn't matter as much, people are a little bit less sensitive to those transpositions.
*  So the training environment will impact the extent to which you're sensitive to transpositions.
*  And yeah, we found a study, we have a paper that's I think coming out now, but it was showing
*  my surprise, the model did a surprisingly good job at accounting for the similarity between
*  meta transpose, you know, a word that you transpose something and then you compare it
*  to a word without the transposition. And you ask how similar those internal representations.
*  And they're more similar than I would have thought. And the pattern of results kind of
*  capture the experimental conditions that people have done. So sometimes these models do, you know,
*  I still think I could make the model fail if I tried harder. But I was, you know, I suppose,
*  please, I don't know. I try to enjoy finding faults in these models. But you know, credit to
*  a credit to you, the model did a good job. I was gonna say, to your surprise, you mean to
*  your chagrin because you hate these models, right? I don't. Yeah, I know. I know. I don't want to
*  give people that impression, actually. Psychology just gets no respect. I mean, we need more,
*  you know, people need to pay attention because psychology has the relative beautiful data
*  and relevant data for so many things that somehow people think it's more impressive to look at
*  neuroscience than the relevant behavioral data. So I mean, the very simple version of this is that,
*  you know, people would kind of, I don't know, do an MRI scan, you do some instruction on
*  intervention to try to improve someone's reading skills. And you show you do, you know, you kind
*  of say, this is a state of it. Johnny has trouble reading. Here's the state of his brain as measured
*  by FMRI before intervention. And then you do some intervention. And then you look and then you see
*  the brain has changed. The bold signals different post-test. And you think, oh, the intervention
*  worked. Just like, well, no, I mean, we don't know. I mean, the question is, does Johnny read
*  better? I mean, behaviorally, that's what matters. And if they did, if the reading did change,
*  we know that the brain changed. I mean, you know, where the brain changed is interesting
*  if you're a neuroscientist, but it's just not that relevant to, is it Johnny? I can't remember who
*  I'm talking about. Johnny. So it's irrelevant to Johnny, it's irrelevant to Johnny's mother. I mean,
*  the point is Johnny can now read and it's the behavioral, you need a careful behavioral measure
*  of the performance of Johnny when reading. We need a good behavioral intervention to kind of,
*  you know, hopefully design a study that has some, you know, logic, given what we know about
*  learning and memory. And, you know, so you kind of use psychological insights to design the
*  intervention. You use psychological methods to evaluate the outcome of the intervention to find
*  out where the performance is better. And neuroscience doesn't have any role in any of those stages,
*  I don't think. Neuroscience is just not a useful tool for the teacher or, you know, but it's
*  certainly interesting intellectually. I like to know where Johnny's brain changed after instruction.
*  I'm not criticizing neuroscience, I'm criticizing the idea that it's useful for education and we
*  should invest. And grant funding is a zero-sum game and the neuroscience studies are expensive,
*  you know. Actually, so are psychological studies where you do, you know,
*  randomized control studies are also super expensive. They're both expensive. So, you know,
*  you know, better spend your money if you're interested in education on psychology,
*  not neuroscience. That would be my, that's the sort of the short. But again, the theme is
*  pay more attention to psychology. I was going to, I was thinking about naming this episode,
*  Deep Problems with Deep Learning, based on the title of your recent, you know, your archive paper,
*  Deep Problems with Neural Network Models of Human Vision. But now I think maybe I shouldn't
*  name it, Psychology Gets No Respect. What do you think? What's a good name for the episode?
*  I like that. I like that one. Why not? Go for that.
*  Okay, I'll go for that. But it's going to be attributed to you, Jeff. Thank you so much for
*  spending the time with me. We could talk for a lot longer, but it's late in your world and
*  I have to go as well. So, I really appreciate it. I had fun.
*  Yeah, you too. I really enjoyed the conversation a lot.
*  I alone produce Brain Inspired. If you value this podcast, consider supporting it through Patreon
*  to access full versions of all the episodes and to join our Discord community. Or if you want to
*  learn more about the intersection of neuroscience and AI, consider signing up for my online course,
*  Neuro AI, The Quest to Explain Intelligence. Go to braininspired.co to learn more. To get in touch
*  with me, email paul at braininspired.co. You're hearing music by the new year.
*  Find them at thenewyear.net. Thank you, thank you for your support. See you next time.
*  Bye.

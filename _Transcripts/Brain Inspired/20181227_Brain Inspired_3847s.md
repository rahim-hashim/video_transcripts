---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3847s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 2711
Video Rating: None
---

# BI 023 Marcel van Gerven: Mind Decoding with GANs
**Brain Inspired:** [December 27, 2018](https://www.youtube.com/watch?v=PPM-ErrIUsQ)
*  That's something which has been kind of missing in cognitive neuroscience at least, because
*  we have been doing a lot of studies which focus on one of the aspects of the human mind.
*  But to have this integrative picture or understanding of how mind comes about, I think the only
*  way you can start doing this is by building it.
*  Is it a case that consciousness is like the most compact solution to the problem which
*  organisms need to solve?
*  This is Brain Inspired.
*  Greetings, good people.
*  This is Paul Middlebrooks.
*  Hope you've enjoyed seeing your family and friends over these holidays.
*  I apologize for the background noise that may be occurring during this little introduction.
*  I'm at my brother-in-law's house with about 400 children, 300 dogs that you may hear.
*  Somewhere around there, anyway.
*  My microphone right now is sitting on one of the children's beds in their room.
*  So anyway, I hope it's not too bad and distracting.
*  Today I add to your holiday treats and bring you Marcel van Kerven, or as we say in America,
*  Marcel van Gerven.
*  I suppose we pronounce it.
*  He is the head of the AI department at the Donders Institute for Brain, Cognition, and
*  Behavior.
*  That's at Radboud University in the Netherlands where he runs his artificial cognitive systems
*  research group.
*  So he's surrounded by folks interested in understanding the brain and using that understanding
*  to build AI and vice versa.
*  So the beautiful productive cycle that we love here at Brain Inspired.
*  Marcel and I talk about his life as head of the AI department at Donders and the challenge
*  of keeping people in the research world instead of them going and taking high-paying jobs
*  at companies that want in on the latest deep learning and data science boom.
*  And the type of people that do stay in academia and forge ahead in the quest to understand
*  things and solve problems.
*  One of the things that Marcel's lab does is develop algorithms to reconstruct the images
*  that someone viewed while in an fMRI scanner.
*  There are various ways to accomplish this, but most recently they've used a technique
*  you've probably heard of called Generative Adversarial Networks or GANs.
*  If you haven't heard of them, they were developed really recently in 2014 by Ian Goodfellow
*  and Joshua Bengio and their colleagues.
*  And GANs are a sexy topic in the news these days because they're being used to create
*  realistic looking pieces of art, including portraits and so on.
*  Marcel describes how they work and we discuss the recent paper from his lab reconstructing
*  natural images that people were viewing while in the fMRI scanner.
*  So they develop encoding models which predict fMRI responses in the people that are looking
*  at the images and decoding models which reconstruct those images from the fMRI activations.
*  We talk about why this is even a desirable thing to do, where it's headed from here,
*  some of the shortcomings of GANs in general.
*  Marcel has his hands on a lot of projects, as you might guess.
*  We also talk about his work to help restore vision to the blind by directly stimulating
*  visual cortex.
*  And of course we talk about where AI and neuroscience are headed while they continue to hold hands.
*  Marcel and I are Skyping from across the world.
*  He's in the Netherlands, I'm in the United States, so there are a few instances where
*  he cuts out just a bit, but I tried to patch them up as best I could.
*  But I know you'll enjoy Marcel as much as I did.
*  Special thanks to David and Fareed this week for helping me make this podcast by supporting
*  it on Patreon.
*  I make this thing all by my lonesome, so it takes a ton of time and effort, etc. etc.
*  And you can support it by contributing just $2 per month.
*  You can go to BrainInspired.co and click on the red Patreon button there, should you choose
*  to do so.
*  Show notes for this episode are at BrainInspired.co slash podcast slash 23.
*  Okay, here's Marcel.
*  Marcel van Gerven, welcome and thanks for sharing your time and knowledge with me here today.
*  Thank you.
*  It's my pleasure to be here.
*  So you're Dutch.
*  Can we talk about the Netherlands just for a moment?
*  Sure, why not?
*  What do you want to know?
*  It's not what I want to know, it's what I want to tell you.
*  I'm Dutch as well.
*  No, you're kidding.
*  I have Dutch in my genes anyway, in my background.
*  When I was in fourth grade, I actually had to give a presentation on, believe it or not,
*  I was in a gifted program in elementary school when this was about nine years old.
*  I'm not sure fourth grade means anything to you.
*  The most popular girl in the school and by my accounts, the prettiest also, she had a
*  crush on me and she even wrote me a note and had one of those, do you like me circle yes
*  or no?
*  Is that a thing in the Netherlands?
*  Well, we do have multiple choice exams.
*  Anyway, I circled yes and then I never gave it back to her because I was too nervous.
*  But anyway, she ended up learning me some wooden clogs for my presentation in my little
*  course on my family background.
*  So there's a little bit of Dutch in me, so this should be a great conversation, I would
*  imagine.
*  Okay, yeah.
*  So I guess we Dutch people, we don't all work on wooden clogs anymore, but I have seen them
*  in the past, yes.
*  Do you ever see any these days?
*  You don't, do you?
*  In the tourist shops.
*  Oh, sure.
*  But not in the fields, not people.
*  No, no, no.
*  And well, probably if you go to some very remote areas of the Netherlands, then maybe,
*  but it's not very conventional.
*  But see, my Dutch friends tell me there aren't remote regions, there aren't forests and natural
*  areas in the Netherlands anymore.
*  Well, so I remember this one quote where there was like this foreign visitor and he landed
*  in Schiphol in Amsterdam and he basically drove all the way through the country and
*  at some point at the other side of the country, he mentioned, well, when are we going to leave
*  Amsterdam?
*  Oh my gosh.
*  Yeah, I mean, it's quite a densely populated area, but there's still some nature reserves
*  and forests.
*  I see.
*  Well, my friend's gentleman I worked with, who is now back in the Netherlands, we went
*  camping together and he marveled at all the natural space in the United States still.
*  When you're here, when you're in the States, you think, oh no, it's all becoming urban.
*  And then I guess if I visited the Netherlands, I'd feel better about it.
*  I guess so.
*  It's one of the most densely populated areas, I think, in the world.
*  Is that right?
*  I didn't know.
*  Okay.
*  Well, thank you for that.
*  So Marcel, you are head of the AI department at the Donders Institute for Brain Cognition
*  and Behavior.
*  And this is at Radboud University.
*  I don't know if I pronounced that correctly.
*  Perfect.
*  Oh, great.
*  So congratulations, I think.
*  Yeah, yeah, yeah.
*  It's an exciting time to be here and to help develop the field of AI at our university.
*  I think it's also quite exciting that we are based in an institute for neuroscience.
*  And I think that creates a very interesting and vibrant atmosphere at the interface between
*  both AI and neuroscience.
*  Well, I want to talk more about the AI department there.
*  Just to sort of introduce you a little bit more, you actually got your undergraduate
*  degree at Radboud and you've worked at the Max Planck Institute and you also got your
*  PhD at Radboud University.
*  Is that correct?
*  Yeah, that's true.
*  I studied here, then I've been here and there at the Max Planck Institute.
*  I've been at UCL for a bit of time.
*  And then I went back, did my PhD here and in Amsterdam at the Dutch Cancer Institute.
*  And basically I was developing machine learning techniques to predict treatment outcome in
*  cancer patients.
*  And then I actually got a postdoc at the Donlis Institute focusing on brain-computer interfacing
*  and from there on I became staff.
*  And at this point, I'm basically head of the department where I once started to study myself.
*  That's an interesting journey.
*  It really is interesting.
*  But you also went to industry at some point and worked on some educational games using
*  and worked on like AI software, right?
*  Yeah, true.
*  So I've been in industry for like one and a half years and then I realized, well, the
*  academia is basically my place.
*  So yeah, I spent some time there and then went back into academia.
*  I see.
*  Okay.
*  So you also run the Artificial Cognitive Systems Research Group there.
*  And so the goal is to use what we know about human intelligence in our brains and cognition
*  to develop AI.
*  So you guys study human cognition and artificial intelligence and the human-machine interaction
*  and interface like you were just mentioning.
*  And there's even keep a blog.
*  I guess there's a variety of writers in the blog, but it's mindcodeec.ai.
*  Yeah, we call it MindCodec.ai.
*  And it's basically members of my research group who are writing bits and pieces on things
*  related to either neuroscience or AI and preferably both.
*  Preferably both.
*  So you're perfect for the show.
*  So it's perfect.
*  So let's talk a few minutes more about just the AI department and sort of your role in
*  it.
*  So is the department itself a year old or have you just been appointed as the head for
*  a year?
*  I've been appointed as the head for a year, but the department has been around, I think,
*  for, well, maybe even 20 years.
*  Is that right?
*  So it has been there for a long time and it basically grew out of cognitive science.
*  So our AI department is based in the Faculty of Social Sciences.
*  And this is because it has its roots in cognitive psychology and cognitive science.
*  Right.
*  Okay.
*  So what's the intention of, you know, and the current overall picture of the AI department
*  there?
*  Yeah.
*  So AI is, of course, a hugely broad field.
*  And given our cognitive roots, we are really focusing on cognitive AI.
*  So really thinking about ways in which psychology or neuroscience can inform AI or thinking
*  about ways in which AI can help neuroscientists and psychologists understand the human mind
*  better.
*  Yeah.
*  So that's the main focus of the department.
*  Some people in the department are also focusing more on the societal impact and the ethical
*  implications of developing AI techniques.
*  And our focus is mainly human centered.
*  So we place the human central.
*  Yeah.
*  We focus on different aspects.
*  And the field, it seems like, I guess, this is my little bubble because I do this little
*  podcast, but it seems like this field in academia, in universities, is really exploding.
*  The interface between AI and neuroscience and neuroscientists working with AI researchers
*  and vice versa.
*  Is that a false impression that I have?
*  Are you guys growing?
*  Do you see the field growing in the world, etc.?
*  Yeah.
*  So it depends a bit on where you come from.
*  So if you look at the field of AI, of course, it can also be rooted completely in engineering.
*  And one argument there could be, well, we completely don't care about the brain.
*  We just want to build artificial systems.
*  And who cares that it's either that it's mimicking the brain or not.
*  So in a way, that's true.
*  If you want to build these artificial systems, yes, then why care?
*  But I still think on the one hand, I think that we can take a lot of inspiration from
*  human brain function.
*  And of course, historically speaking, AI has its roots there.
*  You mean on the on the neurotechnology side, we could still take inspiration from brains?
*  Well, I would say on the algorithmic or functional side of things.
*  So yes, we can build very advanced AI systems, but they are nowhere near the flexibility
*  or the adaptive nature of our of our own brains.
*  So I do think that by investigating the human brain, we can also start building more advanced
*  artificial systems.
*  At the same time, my interest is also fundamentally in understanding the human mind.
*  And I think AI is one of the ways to to get there and to at least mimic the human minds
*  or the human brain in artificial systems and trying to gain some some knowledge from this.
*  I wonder if if the AI approach is it's exciting.
*  But I wonder if one of the reasons why it's exciting is because people like me, even in
*  my postdoctoral research, kind of ran up against this not wall, but where things are kind of
*  slowing down and think, OK, now, where can I go from here?
*  Not that there weren't plenty of projects to do, but to understand the mind.
*  Right. Because I'm doing electrophysiology and along comes AI and it's sort of this new,
*  unknown, potentially limitless type of thing.
*  So I wonder if we're all fooling ourselves and it's just super hyped up right now.
*  You know?
*  Yeah, I know what you mean.
*  So I don't think we are fooling ourselves.
*  I also think it's it's quite hyped up at the moment.
*  So I think there are large promises in media, et cetera.
*  I'm quite convinced, actually, that AI and definitely the reappearance of neural networks
*  are really going to offer us new insights into human brain function.
*  And I think in a way that's also well, as also working in cognitive neuroscience,
*  I think this is one of the ways we want to start doing things.
*  So I think we have been collecting a large mass of knowledge and data about the human brain.
*  But there are no, well, no ways to get a complete understanding of how to how to build a mind.
*  Right. And I think AI is giving us this model based approach of building a model,
*  training it on certain tasks, letting it lose in the environment and actually starting to test
*  how this corresponds to our own ideas about how the human brain fulfills certain tasks.
*  So I think that's something which has been kind of missing in cognitive neuroscience,
*  because we have been doing a lot of studies which focus on one of the aspects of the human mind.
*  But to have this integrative picture or understanding of how
*  mind comes about, I think the only way you can start doing this is by building it.
*  OK, well, so logistically, let's let's say for a second, not just logistically,
*  but so you've been the head of the department for a year now of the AI department.
*  Have you what kind of challenges have you faced? Has it been all super easy?
*  So that's a good question. So I think one of the challenges and it's kind of a luxurious position
*  to be in, but we had a very rapid increase of students. And I think all AI departments are
*  facing the same challenge. So that's nice. We are growing. There's a lot of interest at the same
*  time. How do you manage these large numbers of students? And what we decided to do is to
*  put a cap on the number of students, because I think it's also important to be able to offer
*  good student support and supervision, which means that you need enough staff members to
*  manage those students. Luckily, our university, the faculty, the department, they are all realizing
*  that we need to invest a lot in AI. And so we now have the means to attract many additional staff
*  members. So we basically are aiming for controlled growth. I think things are looking very nice.
*  We are offering new positions. And I think it's a really exciting time to actually be
*  head of an AI department, at least definitely more exciting than 20 years ago.
*  Oh, so your challenge is that you're growing. That's a good problem to have.
*  By the way, was that a job offer to be Marcel?
*  Well, we still have some vacancies left.
*  Okay. Well, so you're having this influx of students, right? So then they go through the
*  program and you yourself, you went to industry for a year and a half, and then you came back
*  into academia. What I imagine is people are getting these skills and then moving into
*  industry and making hundreds of thousands of dollars per year in American US currency anyway.
*  So is that an issue of just, so the students are going to come in, are they then just going
*  to disperse and leave, leaving a hole behind them? Yeah, that's an issue we see across the board. So
*  not only for students, but also staff members. There are so many opportunities now. And well,
*  from a financial point of view, being a full professor in AI is not the best career move,
*  I would say, because there are so many other opportunities.
*  You've got to really want it.
*  Yeah. But at the same time, I think the students we do attract and the staff we do keep,
*  at least in my department, are also people who are fundamentally interested in understanding this
*  this utmost complex object, namely the brain and how does it fulfill these tasks. This inherent
*  motivation is really what's driving us. And I think that makes it a very exciting place to be in.
*  Yes, I see this outflux of people, but I also see that there's still enough people who really,
*  well, are not aiming for the more applied side of AI, but are aiming for more theoretical,
*  fundamental understanding. And you can do this in companies as well, but you can definitely also
*  do this in academia. I think that game is changing too, that a lot of companies are hiring
*  university departments or working with university departments and vice versa. So that might be
*  opening up a little bit. I'm not sure, really. Yeah, I think so. And also what I see in our
*  institute is we have also surrounding us many great cognitive scientists, cognitive neuroscientists,
*  systems neuroscientists, lots of facilities to brain imaging, either invasively or non-invasively.
*  And I think having those resources, that's quite a unique position to be in from an AI department
*  point of view. Yeah. Okay. So we're going to transition here in just a minute and talk about
*  some of the work that you've done recently. But before we do that, I have a question.
*  Just for people listening out there to get a head start for them, what's an area or a focus
*  of research that you don't have time for or maybe don't have resources for in your own lab
*  that you hope someone else will work on? Well, I can give two answers to this. So I can stay
*  a bit close to my own research. And well, what I'm noticing in my own lab is that we are
*  focusing more and more on the more theoretical side of things. So really new algorithm developments,
*  theoretical understanding of natural intelligence, which means that there's less time for the applied
*  side of things. And I think there are so many exciting applications nowadays, either in healthcare
*  or in neurotechnology, neuroprosthetics, brain machine interfacing. We are definitely doing
*  research there. But I think we need to connect there to the more clinically oriented people
*  in order to really make a difference. And, well, I would definitely hope to be able to hook up to
*  those people. More broadly, we are focusing on human centered intelligence. I also think
*  we have to focus on something like, I don't know, AI for the environment or AI for sustainability.
*  I think there's a big challenge there. And, well, I don't have the time to focus on these questions,
*  but I think they are very, very important. And I sincerely hope that other people are picking this
*  up. Ah, good. Okay, so finally, before we move on here, what is it like describing what you do
*  when you're talking to family and friends who aren't familiar, you know, who aren't experts
*  on this topic? Because I find it's never a great experience in my experience. How do you do it?
*  And is it pleasant? So, well, I recently gave my inaugural speech. And there, well, the speech is,
*  of course, geared towards a more layman audience. And, well, this may be an interesting quote. So,
*  I wrote the speech because you basically write a small booklet accompanying the speech.
*  And, well, at least in the Netherlands. And the first time I gave the speech to my girlfriend,
*  and just to have a chat. And at the end of reading the speech, she was like,
*  I have no clue what you're talking about. It's awful, right? It's so awful.
*  That was quite a terrible experience. But at the same time, the second time around, I think this
*  speech came out really nicely. And, well, everything was quite understandable. Also,
*  in the inaugural speech, people picked up on the ideas, which was really nice. At the same time,
*  you can never really talk about what you're working on. So, yes, I can talk about trying
*  to understand how the brain works, trying to build truly intelligent machines. But at the same time,
*  concretely, we are working on things like Wasserstein Variational Gradient Descent.
*  Exactly. Well, so you never can really talk about the stuff you're working on.
*  But that's fine. Okay. Well, we're going to... So it's hard to know, even doing the podcast,
*  the balance between how to technically, how much to dive in and how much to keep it on the surface.
*  But let's dive in a little bit to some of your recent work. And one of the things I want to
*  focus on... So I haven't had anyone on the podcast with whom we've spoken about using functional MRI
*  based neuroscience research. And so I wanted to talk about this. You've done this recent
*  work with fMRI and artificial intelligence, such that you're able to read people's deepest
*  dark secrets and thoughts and desires. That's what you do with fMRI and AI, right, Marcel?
*  Well, I know you know that that's not exactly what we are doing. So, yes, we are trying to... Well,
*  we're developing new decoding algorithms or reconstruction algorithms. And we're basically
*  applying this now to read out visual perception. So that's something we have been focusing on
*  quite a bit. Yeah. So you've been doing this for a little while now. And this technique's not new,
*  but the idea is to put someone in a scanner and then use some equations to reconstruct what they
*  might've been seeing in the scanner, be that handwritten digits or, in your case, you've done
*  studies with reconstructing faces. And this most recent one, I'll just read the title now,
*  it's Generative Adversarial Networks for Reconstructing Natural Images from Brain Activity.
*  And in this one, you're getting more and more complicated, these images that you're reading
*  out from brains and then using some algorithms to reconstruct the image. And even that's not new. So
*  I guess fMRI to reconstruct images started around 2011. Does that sound right?
*  Uh, using fMRI? Yes, I think a little bit earlier, but around that time.
*  But using deep learning techniques is pretty new. And you have been doing that, incorporating it
*  with other techniques for a few years now. So just on a really high general level, why do we
*  even want to reconstruct the images that people are seeing? Yeah, that's a good question because,
*  of course, you could say, well, why should I use the brain to reconstruct this? I can just look at
*  the original images which have been shown to the subject. So this might seem like a futile exercise.
*  So I think there are two reasons. So these reconstruction approaches are basically
*  decoding techniques on steroids. And if you look at decoding, that's basically an established
*  approach in computational neuroscience, also trying to figure out what certain neurons are
*  responsive for. Right? And people have been developing techniques like reverse correlation
*  in order to do so. This is in the same family of algorithms. However, we are trying to
*  boost the sensitivity of these algorithms. So I think there are two reasons why we would want to
*  do so. So if we can develop these reconstruction techniques well, then we will also be able to gain
*  insights into what is encoded where in the brain. So we can start to probe different brain regions,
*  different areas of the brain, maybe individual neurons or neuronal populations,
*  and ask via reconstruction, basically visualize what are the properties those populations are
*  sensitive to. So for visual perception, that's one thing. Of course, the holy grail is to take
*  this one step further and to move towards more internal processes like imagery, working memory,
*  internal speech decoding. So I think this will really offer a unique insight into these processes
*  that are not otherwise, how do you say, we cannot access these otherwise. So I think it will give us
*  insights. At the same time, it also provides the basis for brain machine interfaces that allow us
*  to restore communication and control. So I think there's a scientific reason to want to develop and
*  improve these techniques. And there's also an applied reason. Okay, so do you want to just kind
*  of take us through, we'll talk about what a generative adversarial network is in a few moments,
*  but do you want to just take us walk us through like the setup and the way that the, you know,
*  where the humans go and the computational flow, what goes in, what goes out just to give the big
*  picture and make sure everyone's up to speed? Yeah, yes, I can do so. So the idea is that we
*  start with a large set of stimuli, and in our case, naturalistic stimuli, let's say photographs of
*  human faces, for instance. And basically, what we do is we place people in the MRI scanner,
*  we measure fMRI bolt responses while people are experiencing these stimuli. And then we are
*  developing computational models that either tell us how a stimulus is encoded in the brain. So we
*  go from the stimulus towards predicting the observed brain responses. So that's an encoding
*  model. Or we are developing a decoding model, which takes the brain responses and basically
*  reconstruct the original stimuli. And there's a nice correspondence between these encoding
*  and decoding models, because you can basically show by using Bayes rule, that the coding models
*  can actually be seen as an inversion of these encoding models, given a right image prior. So
*  there's a nice correspondence between these and building these models. That's kind of what we are
*  up to. So the idea is we take a large stimulus set, a large set of observed associated brain
*  responses, we estimate model parameters, let's say parameters of a decoding model. And later,
*  we apply to another set of observed brain responses where we don't know which stimulus
*  has been shown. And then we see what the reconstruction is. Okay, so I thought of this
*  earlier. So an audio podcast is probably not the best way to talk about these things,
*  because we can't show the images. But I'll link to the paper. And there's a pre-print available
*  that I'll link to in the show notes, of course. So how has image reconstruction sort of developed
*  over time? Like I said, it's not completely new, but the deep learning edition is new. And you've
*  used other techniques in the past. So what has been your trajectory with what you've used in the past
*  up to sort of what you're using these days? Yeah, I already mentioned more basic reverse
*  correlation techniques. So there are simpler techniques we can use. And we also have been
*  working on them ourselves. And these techniques have nice properties because they are analytically
*  tractable. So for instance, in the past, we have been using models that assume linearity of
*  responses, Gaussianity of the world around us, in order to basically obtain reconstructions
*  in close form. So if you have a certain encoding model, you can invoke Bayes rule,
*  you can obtain these reconstructions in close form. And it's really nice and it works pretty well for
*  basic images. So the usage of Gaussian things to smooth out spike density functions, for instance,
*  for all sorts of processes. Did you ever get flack for that? Even though it works really well,
*  right? But the world's not Gaussian. A lot of the world's not Gaussian. I mean, did you ever get
*  pushback on that? Well, not completely. I mean, so I was really trained in machine learning. And
*  of course, the simplest approach you could take is to just assume that everything is Gaussian,
*  and then everything becomes analytically tractable. And there are the aim of to see,
*  okay, if we make those assumptions, what do we get? And what we do see is that we can get
*  very nice reconstructions of simple stimuli, like presented letters, which we have shown in the past.
*  Right. But we also acknowledge ourselves that the world is not Gaussian, of course.
*  And that's also why these models tend to fail if we move towards more complex stimulus settings,
*  like naturalistic images or photographs, etc. So we definitely need these more complicated,
*  nonlinear models in order to obtain better reconstructions. The downside is that we
*  don't have analytical solutions anymore. So we need to come up with other strategies to achieve
*  this, these reconstructions. I see. And so you did? Yeah, well, at least we try. And we did. I mean,
*  it's still hard to obtain crisp reconstructions for these more complicated stimuli. But I think
*  definitely if you look at the face reconstruction work we have been doing in the past,
*  we do see that those reconstructions start to look eerily similar to the presented stimuli.
*  So fast forward to today, and now you're using these generative adversarial networks
*  and reconstructing both faces. But now, but this most recent paper that we're talking about,
*  you're reconstructing these grayscale natural images. Now, when I talked with Matt Botvinick
*  a couple weeks ago, he described GANs. I asked him what he thought of the recent artwork produced
*  by GANs, because I found out he was an art history major. I thought he might have a take on it. But
*  and his take was he doesn't like how realistic they're getting because it's less interesting.
*  But let's dive a little bit deeper into how GANs actually work so that people just have that broad
*  understanding. So can you just describe that for me? Yeah, so these generative adversarial
*  networks consist of neural networks. So basically, we have two neural networks that are
*  in interaction with each other. So we have a generator network, and this generator network
*  uses a deep neural network, starting with a random vector. So we just take a random sample,
*  just some random vector. And the goal of this generator network is to transform this random
*  vector into an image. And this image could, for example, be a human face. Then we take a
*  discriminator network. This is also a deep neural network. And the goal of this discriminator
*  network is to determine if a stimulus it sees is either a real stimulus or stimulus generated by
*  the generator network. So what happens is that these two networks are basically playing a zero
*  sum game against each other, where the generator tries to fool the discriminator. And the discriminator
*  tries to identify which image was generated by the generator. So the discriminator is also
*  getting real images to vote on, right? Exactly. It either gets a real image or it gets a generated
*  image. And if we then combine these two models, then we can actually define a loss function for
*  both models, which allows us to train the models using standard gradient descent back propagation
*  techniques. And if we basically let those models compete against each other, what we see, technically,
*  is that these generated images become closer and closer to the image statistics of the real images.
*  So what we do in order to make these scans suitable for reconstruction, for decoding,
*  is we condition these random vectors on brain responses. So the goal of the model, which links
*  the brain to these random vectors, is to predict the state of the random vector based on the observed
*  brain response. So we predict the vector, we generate an image, and the goal is to make that
*  image as close as possible to the image which has been shown to the subject in the MRI scanner.
*  Powerful. Yes. Yeah, it's powerful stuff. So what happened? What were the results here?
*  If we look at the phase decoding work, there we can really see that high level characteristics
*  are reconstructed really well. So things like gender, ethnicity, age, whether somebody is
*  smiling or not. So these things can be reconstructed. And then of course, those reconstructions are
*  still not perfect. But even within those subgroups, we can show that the reconstructions are better
*  than what can be expected by chance. If we then look at the natural images, we can still show
*  that these images are, the reconstructions are better than can be expected by chance. But I think
*  the results are a bit less convincing in the sense that it's harder to identify the similarities
*  between the reconstructions and the images which have been shown. And this also makes sense because
*  we are basically assuming that these GANs should be able to capture anything, so anything in the
*  environment. And these are, this is really a hard problem, capturing the image statistics of
*  arbitrary naturalistic images. So the nice thing of phases is that they are restricted in a way,
*  but also at the same time, still variable enough to be interesting. And I think focusing on
*  naturalistic images, that's the next step. We can do stuff there, but we still need to
*  advance our algorithmic approaches. And we also need to, of course, advance our
*  neurotechnological approaches. So we are still looking at regional blood flow, and we're trying
*  to reconstruct these really complicated images. So there, we also need some improvements, I would say.
*  It's nice. In the paper, you provide a bunch of examples of images, the natural stimuli,
*  which pass the human test, where the human recognizes that this image was the natural
*  image presented before. And you also give examples of failures, right, where the decoded or the
*  reconstructed image does not look very much like the natural image at all. So there's a lot of
*  progress, and like you said, a lot more work to do, I suppose, which is good for you.
*  Yeah, it keeps us off the streets.
*  It keeps you out of industry.
*  Exactly.
*  So these GANs, what you do is you use neuroscience to inform AI and vice versa. But are there
*  anything like generative adversarial networks in the brain? Or should we look in the brain
*  for something like this? I don't know. In a way, something akin to GANs could underlie predictive
*  processing in the brain. So I'm not saying that the brain consists of GANs. That's definitely not
*  what I'm saying. All the way down, yeah. All the way down. But from a high level, in predictive
*  processing, we are trying to predict our sensory inputs, which can then be compared with actual
*  sensations, which can be used as a training signal. And this prediction can be seen as the
*  generator part of a GAN. And the comparison with actual sensations can be seen as a discriminator
*  part. So there's a nice analogy there. But I would see it as an analogy and nothing more than that.
*  So where do these GANs fall short? What's something that they're currently not doing very well?
*  So of course, these GANs, they have been around only for a couple of years now. So it's still a
*  relatively new area, but we know that they are suffering from certain problems. Things like
*  convergence issues. So sometimes if we train those models, they tend not to converge. Or
*  mode collapse. That's a very famous problem in GANs where the generator basically collapses,
*  which means that it only produces a low variety in the reconstructions.
*  Is that because it settles in a local minimum? And so it can fool the discriminator really well,
*  so there's a low error being given to it. And so it just keeps reproducing those types of images?
*  Exactly. Yeah. But there are multiple other problems. So we can suffer from diminished
*  gradients such that the discriminator can get really successful at predicting whether it's
*  looking at the generated or the real images, which means that the gradients start to vanish
*  and nothing is learned. So there are various theoretical reasons why these GANs don't
*  converge well or perform well. So there's a bit of black magic involved in getting them to work.
*  But at the same time, I think we are making great progress, better reconstructions, and we're also
*  working on ways to fix things like mode collapse. So I think the field is just making rapid steps
*  there and we can piggyback on those. There's really so much to do. So I mean,
*  on 60 Minutes, which is a popular sort of layman's news program here, they always show FMRI scans
*  and they're always talking about the future of brain technology. And if they had you on,
*  they would say, they would introduce you just like I did by saying, the man who's going to
*  read our deepest and darkest secrets, read our brain activity and know exactly what we're thinking.
*  So where are we with that grand ridiculous vision? What you're doing right now, how far away is it?
*  Where does it fit in that vision, you know, or relative to the the unreality that is that vision
*  right now? So I think we can definitely do certain things, right? So we can read out those
*  representations that are currently actively maintained in ongoing neuronal dynamics.
*  So we can observe brain activity using FMRI, for instance, and we can start to decode certain
*  properties of things we perceive or either imagine, definitely for high level things.
*  So we can classify what somebody is thinking of or looking at. But it's also kind of obvious in
*  a way. I mean, we know that if we're looking at faces that FFA starts to respond and well,
*  if we can read out FFA activity, well, then we can decode something like that. So yeah,
*  I think there we can take many, many steps. And I think we can reach the point that we could
*  reconstruct the ongoing flow of thoughts, or at least our visualizations, maybe inner speech,
*  things like that. But that doesn't say that we are able to read out things like beliefs, desires,
*  and intentions, right? So these are basically encoded in whole brain synaptic traces that are
*  not directly accessible by current techniques. So I definitely don't think we are touching upon
*  those things. So I think in terms of privacy issues, we are still doing well.
*  You're safe. Yeah. Well, my next question, I suppose, would be, do you think that the future
*  of this technology resides in FMRI, using FMRI? Or will we be using something like little
*  nanoparticles to attach to all of our brain cells and read out the activity, etc.? I mean,
*  because it is, because FMRI has really great spatial resolution and really terrible temporal
*  resolution, as people know. So is the future in FMRI here? Is it still going to be leading the way
*  in 20 years, let's say, in this regard? So we have not only been working on FMRIs,
*  so we've also been using MEG, ECoC data, etc. And I definitely do think that we, in this area of
*  research, will move more towards invasive techniques. So think of high density electrode
*  grids, maybe calcium imaging, optogenetics type of work. So I do think that the future will be more
*  in those domains, if we think about the applications of these techniques. And I think
*  there are also rapid progress is being made. And we can tap into that.
*  Great. So thanks for going over this recent work with me, Herman. Now, I watched a talk you gave
*  at VSS about four years ago. And your last slide, you had some future pointing questions, and your
*  answers were on the slide. So can we just go through those and I can get your take on how
*  far we've come? And I'm curious what my thoughts were at that time. Let me tell you what your
*  thoughts were. I don't know what they are right now, because I'm not reconstructing anything.
*  So the first question, you had two big questions. One was, what's the most critical open question
*  about visual representation? The most critical question that you offered was, what are the most
*  important nonlinear transformations encoded by different neuronal populations up to the level
*  of objects and categories? Looks like we've come a long way in that regard, or you have.
*  Yeah, I think so. I think, well, multiple groups have. And I think many of the people you have
*  already talked to in the podcast, right? So I think we have come a long way. What I do see is
*  that also the focus is shifting a little bit, especially for the people focusing more on the
*  AI side of things. So the question in the end is also, why do these object representations emerge?
*  So the brain is definitely not directly optimized to represent objects. It's optimized for something
*  else. And of course, other people have also argued that the brain might be optimizing different kinds
*  of cost functions. And we need to figure out how the brain under certain evolutionary constraints
*  organizes itself. And I do think that if we apply the right constraints and we identify the right
*  objective functions, many of the properties we see in our own brains also emerge in models,
*  artificial models that are subjected to the same kinds of tasks. So I do think that, well,
*  the field is moving more in that area. Right? So we're going beyond objects.
*  Yeah, it's crazy to think that we're talking about objective functions in the brain,
*  but that's where we are. So it's great from my background, from my limited scope.
*  Well, I mean, interestingly, of course, in the field of machine learning and AI,
*  this has been something we, this is kind of the lingua franca we have had for decades, I guess. And
*  what for me is really interesting to see is that the fields of neuroscience and AI who
*  grew up together, drifted apart, but are now coming together again. And I think that's very exciting.
*  Yeah, that's why I'm doing the podcast. So it's exciting to me as well.
*  Yeah. And I must say, it's a great podcast. The whole department is listening to the podcast.
*  Oh, get out of town.
*  On a regular basis.
*  Oh, thanks, man. Thank you very much. Thanks. I'm trying. I'm trying to make it better and
*  better, you know, so I appreciate that. So your second main question on the slide was,
*  what is the most important thing we need more of? And you listed three things. One was realistic
*  encoding models whose feature spaces are obtained using unsupervised deep learning.
*  I'll let you comment on that.
*  Okay. So I think what we what we definitely do need is this notion of synthetic brains,
*  right? So trying to mimic in silico what the brain is doing. And I think there,
*  yes, we can talk and think about unsupervised techniques. But I think what we should start
*  thinking about is, how do we build these realistic models? Are neural networks good enough to do so?
*  So on the one hand, we could say, well, all we need is a recurrent neural network, because these
*  are just ways to model any dynamical system, the brain is dynamical system. So voila, we are done.
*  On the other hand, you could say, well, no, we need to start focusing on spiking models,
*  because the brains had a brain is basically communicating via spikes. Then people could
*  respond, well, spikes are only relevant to facilitate long range communication. And that's
*  that. So I think addressing these questions is going to become really important. And in my group,
*  we are focusing mainly on rate based models. So standards recurrent neural networks. I mean,
*  there are many functional properties of the human brain, which have been studied in various guises.
*  And I think by building these in silico models, we can start to gain an understanding of why
*  the brain functions the way it does. Good. So the other two that things that we need more of on
*  your slide were neural data recorded at the columnar level and sharing of models and data.
*  And that last one I know you guys are really good at because you put all of your code is available
*  and a bunch of data sets is available through the artcogsis.co or .com website. So check off
*  number three, I suppose, at least from your lab. But I was invited to give a talk. I recorded
*  spiking neurons, right? And didn't model the data. And I was invited to give a talk. And it was a
*  heavily modeling department centric group of people. And we were having lunch and they said,
*  why don't you guys like to give your data to modelers? And I felt kind of icky explaining it,
*  but this data was really hard won and I might model it one day. And of course, I never did.
*  And I might still. I still have the data. But that wasn't a very good satisfying explanation
*  to them. But I think that the sharing of models and data is really coming along and becoming
*  more and more the rule rather than the exception. I'm not sure what you think.
*  Yeah, I think so. And of course, I also hear you. I mean, we have recently collected
*  quite a large data set. So we basically collected 40 hours of fMRI data in one of our master
*  students. So he spent quite some time in the scanner. Yeah. Well, these data, they take some
*  time to obtain. And of course, you also want to run your own analysis first. But I think, yeah,
*  it's good practice to at some point, make this available to the community. I also think it's
*  important because I think it's important to be able to have people work on the stuff they do best.
*  So yes, we collect our own data, but we're also developing algorithms and models. And I'd rather
*  be focusing on the algorithmic part and collaborating with the people who really, really know how to
*  collect at the highest quality possible data we can obtain in order to get the best of both worlds.
*  But we have to learn cross-disciplinary skills these days, too. So there's a balance in there
*  somewhere, I suppose. Yeah, somewhere. You definitely need to be able to talk to each other.
*  That's definitely important. But I do think that the field is also becoming so specialized. So think
*  about the more theoretical work. It's quite hard to be excellent both on the theoretical side and
*  the algorithmic work and to be excellent on the data collection and neurophysiology side. So I
*  think it's also important to form teams there and collaborate. Well, Marcel, we were going to,
*  I wanted to talk about some of your other recent work with recurrent neural networks
*  that you've been doing and seeing. The title of the paper is Emergent Mechanisms of Evidence
*  Integration in Recurrent Neural Networks. And so this is where you guys model a decision-making
*  task and use recurrent neural networks. So you're all over the place. You're doing lots of different
*  kinds of work. So we're going to have to save that for next time when I demand,
*  actually when I visit the Netherlands, my home country. Yeah. If you're here, please drop by.
*  Oh, sure. I'll buy you a beer and we'll talk more. That's great. So another thing that you're
*  working on is on the neurotechnology side, you have a project going on to restore vision to the blind.
*  Now, there are multiple approaches historically and these days to restoring some sense of vision
*  to people who suffer from various types of blindness. One of the earliest ones was a little
*  tongue stimulator, right? Where there is some sort of camera and it processed the visual stimuli and
*  then it would stimulate your tongue tactically. And then people learned to use that tactile
*  stimulation as a proxy for visual cognition. There are things like prosthetic retinas,
*  replacing the eye lens with a tiny telescope. There's little microchips you can implant under
*  your retina and even gene therapies are coming along now. You guys are doing something different.
*  You want to just give us an overview of the approach you're taking and the progress being made?
*  Yeah, sure. Yeah. So we are working together in a consortium of other mainly Dutch researchers.
*  And the aim is to basically restore visual perception or visual sensation in the blind.
*  And the way we approach this is basically using cortical implants. So the idea is that we
*  directly stimulate early visual cortex, V1. And if you stimulate a certain location of visual cortex,
*  we can basically generate a phosphine, so a light flash in your visual field.
*  So the grids we are using at the moment, they are quite high density. So we have a thousand
*  contact points. And by stimulating each of these contacts individually, we can generate a phosphine.
*  So if we can do this in a very targeted manner, we can start to generate patterns,
*  which means particular visual sensations. So the idea is not so much to restore the
*  clarity of vision, but to present the subject with a pattern of phosphines that they can then
*  translate into knowing that there's a couch in front of them, for instance, or something like that.
*  Exactly. And I think the challenge is to optimize the phosphine patterns in such a way that the
*  experience of a couch is basically instantiated.
*  Gosh, there's all sorts of plasticity issues here too, that things are going to be dynamic
*  and changing over time. So is it really early on in the work?
*  This is work together with my colleagues at the Nettles Institute for Neuroscience. And there,
*  in primate work, we can definitely show that we can generate those phosphines in a controlled manner.
*  And this is still very early days, but I'm quite hopeful that in a couple of years we can
*  establish some breakthroughs there. And I think it's one of the most exciting projects I at least
*  ever worked on. So it's highly exciting from the neuroscience point of view, from the algorithm
*  point of view, and also from the societal impact point of view.
*  Yeah. My very first guess was Stephen Potter. And he said one of the reasons he
*  loves what he does is because it's our job to solve problems. And I just felt guilty all of a
*  sudden when he said that, because what I wanted to do was understand things. And what he wanted to do
*  was help people. And I didn't care about helping people. But I think anytime you can, and I think
*  he's right. I think that that should be the major reason why people work on these things. And so
*  I'm learning to be a little bit less selfish as time goes on, hopefully, because I think it's great.
*  Ideally, you get the best of both worlds, right? So I think it's highly satisfying to be able to
*  work on such a project. But it's also extremely satisfying to, I don't know, write down a very
*  elegant equation or to figure out that your algorithm converges. There's also some theoretical
*  satisfaction there. And I think achieving this balance is nice.
*  I think I'm just on that. I'm kind of far on that side of the spectrum, unfortunately.
*  Also fine.
*  Yeah. Okay, good. Thanks. Thank you for that reassurance. Okay, Marcel, we've come to the
*  time in the program where we both take shots of what are you drinking over there?
*  At the moment?
*  Is vodka there?
*  Or in general?
*  In general. Let's say at the moment.
*  Vodka is more a Russian thing.
*  Well, I know it's Russian, but what's the drink de jour in the Netherlands?
*  It's typically beer. And then typically Belgian beer, because they are better at making beers
*  than the Dutch.
*  Okay. Well, let's have some imported Belgian, some strong imported Belgian beer, or at least
*  pretend to do so. And I have some broader, more speculative questions perhaps for you.
*  It seems like the more people I talk to, the general consensus is that we're really,
*  really far from general AI. And that it's not time to be scared yet that AI is going to take
*  over the world and we're going to be its pets and things like that. But then there's a lot of people
*  in industry, and there's a lot of people in working on the ethics of the implications of all
*  this progress that we're making. So I'm just curious what your outlook is
*  regarding the timeframe of achieving or not achieving general AI, general human level AI.
*  So first of all, I don't think we have to be that afraid of achieving AGI. I think we should be more
*  afraid of the ways the non-AGI type of artificial intelligence is now ingrained within society.
*  And what are the implications of this? I think that's a more urgent problem at the moment.
*  Of course, it's important to speculate about this and to think about the consequences of building
*  machines that are able to surpass ourselves. But well, maybe call me naive, but I think it's only
*  very exciting. So I think it's very exciting that we're at least able to think about ways to
*  build systems that might be able to mimic properties of the human mind.
*  I think we're completely not there yet. And I think we still have a long way to go. But thinking
*  about ways of building models that are forced to understand their environments by placing them in
*  the right conditions and forced to build very expressive world models and forced to predict
*  the consequences of their actions. I think that's really interesting. I think these are
*  kind of the building blocks of building AGI. And in the end, it will buy us intelligent algorithms
*  that allow us to solve current societal problems in a more optimal manner. So I'm not that afraid
*  of like these doom scenarios where terminate the type of robots will take over the world.
*  But at the same time, I do think that currently AI is so ingrained in society that we should be
*  scared about this because we didn't think hard enough about the potential consequences of
*  using these systems. Okay, but how far are we from achieving this goal? I think still very,
*  very far. And I think we are optimistic. But we also don't know if we're still missing ingredients,
*  right? I mean, of course, you will at some point drop the magic word consciousness,
*  and then I will start to shiver and scream and it's coming. Oh, it's coming. It's coming.
*  Maybe if we have time. Okay, that's what everyone want. Anytime I ask like people do,
*  do you want what do you want me to ask someone about their like consciousness? Yeah, so
*  well, let's let me let me ask you this. So speaking of like the ethical implications of things,
*  are you familiar with the trolley problem? Yeah, sure. Okay, so let's say you're standing up on a
*  hill. And you're standing next to a neuroscientist. And you see the train coming down below and you
*  see an AI researcher down there, you can stop the train by throwing the neuroscience researcher in
*  front of the AI researcher on the tracks. He or she is kind of a big heavy set person. So it's
*  going to take a little strength. So what do you do you throw the neuroscientist off and save the AI
*  researcher? Or do you let the AI researcher die? It depends a bit on who the neuroscientist and the
*  AI researchers are. They're clones of each other. They're complete clones, but they are
*  neuroscientists or AI researchers. Can I spend like 10 seconds to think about this?
*  Well, in other words, I'll because 10 seconds would be not enough for me. So but what? So here's an
*  easier question. Which will you think do you think will have more influence on the other AI
*  on neuroscience or neuroscience on AI? I think in the short run, AI will have a big influence on
*  neuroscience. Maybe not only in terms of being able to model these these generating these
*  artificial cognitive systems that behave like like brains, but also more in the context of
*  developing new techniques to perform neural data science or to neural data analysis, right? So
*  I think coming from a machine learning point of view, if I look at the techniques that are
*  currently used in neuroscience, I think there's still such a big gap between what we are able to
*  do and what we are currently doing that I think that will make a big impact. And I think that's
*  really important because what we see in neuroscience, of course, is that we are generating
*  generating these larger and larger whole brain, single neural real time data sets. And we know
*  less and less well what to do with these data sets. So I think their AI will play a very big
*  role. And I think there are definitely people at the interface between neuroscience and AI,
*  with machine learning backgrounds, who are really pushing the field forward. And I think that will
*  be a major short term impact. So in terms of neuroscience feeding into AI, people are also
*  arguing, well, what did neuroscience really actually buy AI, right? So, yes, some some ideas
*  or some some concepts. Wait, it gave birth to AI. It gave birth to AI. But as an AI researcher,
*  you could also say, okay, yes, it gave these nice ideas like convolutional deep neural networks,
*  like the neocognitron, right, which comes from from neuroscience, which gave birth to deep neural
*  networks, which are now kind of all the grace in in AI. But in the end, AI is also applied
*  mathematics. So when we truly understand what we are doing, we might not need neuroscience.
*  I don't agree with this, because I think there are still there's so much knowledge in the field
*  of cognitive psychology and neurophysiology, which will be able to feed into AI, definitely at the
*  functional level. So trying to understand how intelligent beings operate, because we are the
*  existence proofs there. And hopefully, at some point, at the more algorithmic level, right, so
*  maybe thinking about the ways backpropagation can be implemented in the brain. That's now a whole
*  topic. Yeah, neurophysiology might lead us into clues on how this could be achieved. And I think
*  that will be a massive impact in in AI. And that maybe takes a little bit more time. Yeah, okay,
*  I like that answer. What is something that you envision in the future that may seem a little bit
*  out there to a lay person or even to an educated person, maybe something that's that they might
*  find hard to believe that that you believe will occur? I think we will be able to mimic
*  the human brain to such an extent that we are able to build artificial systems that really behave
*  very naturally in many, many ways. So I think we should be thinking much harder about, okay,
*  what are the functional subsystems of which our brain is composed? And how can we build this into
*  our artificial system? So I think the strong convergence between neuroscience, cognitive
*  psychology and AI will allow us to build systems that behave like biological organisms. The question
*  is, what do we need in terms of ingredients? And I can imagine that we're currently modeling things
*  a bit at the wrong level. So I think we are looking at it from a functional point of view.
*  And I think we can get a long way there. We're also of course, ignoring certain details, which
*  probably play a role like dendritic computation and synaptic processes and maybe intracellular
*  processes that are subserving cognition. So I think at some point, we can mimic all of this
*  in artificial systems and create very naturally behaving AI systems that look like they might be
*  biological organisms. That look like they might be.
*  Yeah, well, so that's the next question. You can begin to shiver now. So will those organisms,
*  right? Or those systems, will they be conscious? And or you could answer the alternative question,
*  do you think that work in AI and or neuroscience will help us understand
*  consciousness, what it is, how to build it, and so on?
*  So it's kind of like a more fingers crossed experiment, right? So if we build those systems
*  and we subject them to the same constraints, is it a case that consciousness is like the most
*  compact solution to the problem which organisms need to solve? If that's the case, then we can
*  enforce it. However, it's really fingers crossed, right? Because we either build very smart zombies
*  or we build conscious systems. And the question is whether consciousness naturally emerges.
*  Yeah, empirical question.
*  I like the way that you phrased that. Okay, so Marcel, thanks for your time. I have one
*  last question for you here. So luck plays a role in everybody's lives and careers,
*  and you've been very successful. Can you think back to a particular time that luck played a role,
*  large or small, in some of the success that you've had?
*  So I think I can give like a social answer to this. So I think luck is also related to
*  being surrounded by the right people at the right time. So I think much of the work I've
*  been doing is done with a team of people. And I think if you resonate well with those people,
*  you can really achieve really great things you cannot achieve on your own. And that's what I see
*  in my department now that it's like a vibrant community of people who all aim to understand
*  natural intelligence. And I think I'm quite lucky to be able to have those people around me. So
*  for me, that's the luck. That's great answer. I have been lucky to talk to you today and the
*  listeners have all been lucky that they've tuned in. Tell Katja I say hello and thank you.
*  I will do.
*  And I really appreciate the time. So thanks.
*  My pleasure.
*  Brain inspired is a production of me. You can support the show through Patreon for a trifling
*  two or $4 per month. Go to patreon.com slash brain inspired, or go to the website brain inspired
*  dot co and find the red Patreon button there. Your contribution will help keep this show going
*  without any annoying advertisements like you hear on other shows. To get in touch with me,
*  email Paul at brain inspired.co. The music you hear is by the New Year. Find them at the New
*  Year.net. Thank you for your support. See you next time.

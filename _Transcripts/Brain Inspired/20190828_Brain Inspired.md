---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4613s
Video Keywords: ['Science & Medicine', 'Technology', 'Education']
Video Views: 156
Video Rating: None
---

# BI 045 Raia Hadsell: Robotics and Deep RL
**Brain Inspired:** [August 28, 2019](https://www.youtube.com/watch?v=j9qZeX9NUw8)
*  I think that the intelligence of humans and other creatures on this planet is very much
*  motivated and driven by how the bodies of those creatures interact with the world.
*  So learning embodied intelligence is a much different thing, which makes it more challenging,
*  but also potentially more powerful.
*  We get excited when we stack two or three blocks on top of each other, but that's a
*  long ways away from, for instance, building a Lego house from directions.
*  This is Brain Inspired.
*  When are robots going to be a thing?
*  I mean, besides your dishwasher or your Roomba?
*  What's it going to look like when we make intelligent robots?
*  Why do I have only questions and no answers?
*  Welcome everyone.
*  I am Paul Middlebrooks, and today I seek some answers from Raya Hadzal.
*  Raya has been working in computer science for a while now.
*  She did her PhD working on machine learning with Jan LeCun and has worked in robotics
*  at CMU and at SRI International.
*  She was one of the earliest members of DeepMind since way back in 2014, so she has seen the
*  rise of DeepMind's stature.
*  Raya has lots of talents, but one of her specialties these days is robotics and figuring out how
*  to use deep reinforcement learning to do for robotics what deep learning has done for things
*  like speech recognition, image classification, and machine translation.
*  We talk about how far along we are to developing intelligent robots, that is AI, that is embodied,
*  what's different and what's challenging about robotics relative to non-embodied AI, and
*  how deep reinforcement learning approaches can help meet those challenges, including
*  her work using Google Street View data to make an AI agent that can navigate the streets
*  of your favorite city, perhaps.
*  It's the first time that anyone's talked about a defecating duck on the show, so you're welcome
*  for that.
*  I will link to some of the papers that we discuss and her website where she has those
*  and links to some of her talks where she goes into more detail on all this exciting work.
*  Those are at braininspired.co.
*  slash podcast slash 45.
*  You can follow Raya on Twitter.
*  Her Twitter handle is at Raya Hadsell.
*  I keep a list of all of the Brain Inspired guests on my Twitter feed.
*  I am at PGmid, P-G-M-I-D.
*  Alright, thank you for listening to the show.
*  If you have questions, feedback, and or suggestions, send them my way to paul at braininspired.co.
*  Here is the decidedly human and naturally intelligent Raya Hadsell.
*  Raya Hadsell, thanks and welcome to the show.
*  Thank you.
*  Nice to be here.
*  You have been at DeepMind for what, five years now?
*  Yes, five years.
*  Is that right?
*  So I'd like to talk about DeepMind for just a second.
*  So you've been there long enough to sort of experience the rise of what I consider kind
*  of the celebrity status of DeepMind.
*  Do you see it in the same way?
*  And if so, what's your experience been of the sort of rise of that celebrity status?
*  Yeah, I mean, I guess I don't think about it as celebrity status, but certainly just
*  the eyes of the world and the media and other labs are really on us more and more.
*  And it has been a change.
*  Sometimes the extra scrutiny that we get can make it hard to work.
*  If you have to always be thinking, oh, if the media picks this up, how are they going
*  to construe this?
*  What picture are they going to put in here?
*  Am I going to see the Terminator robots coming to a door in my research?
*  Of course, it opens doors as well.
*  So I can't complain because I know that being from DeepMind, having been here since close
*  to the beginning means that that has opened doors to me being able to present my research
*  in different forums and have a lot of people read my work and be interested in it.
*  Yeah, I just realized right after I asked you that question, I guess I'm the media too.
*  Damn it.
*  But that's the way it is, I suppose.
*  And that's probably one reason I'm talking with you right now.
*  So you've worked on a host of things, including deep reinforcement learning, some of the current
*  challenges in deep learning, like transfer learning and continuous learning.
*  You've worked on navigation using these tools.
*  And we will don't worry, listeners will unpack these things as we go along.
*  When we talk about them, I can't really chat with my mom about the neuroscience research
*  that I did.
*  I couldn't chat about it then.
*  I can't chat about it now.
*  And I can't really chat with her about this show and what we talk about.
*  You know, she's nice.
*  She's a smart lady and she's nice and asks me, how's it going and things like that.
*  I know your mom was a ceramicist.
*  And then around in her 60s or so, she decided to just start making iPhone apps.
*  Can you guys just sit around and chat about this stuff or what?
*  Yeah, my mother is one of the best examples of, you know, how we all get a long life and
*  there's lots of amazing things that you can do with that.
*  So yeah, she was a potter, a ceramicist for three or four decades.
*  And then when I was doing my masters, she stole, borrowed my computer graphics textbook
*  in one of my courses.
*  And she taught herself how to program and she started making shareware for the PC.
*  And then that was in the early not.
*  So when the iPhone came out, then she started porting her games that she had written to
*  the iPhone.
*  My dad joined in to help write plumbing and infrastructure.
*  And the two of them are pretty neat.
*  I still think that it's hard to explain what you do when you're working on something like
*  AI.
*  There's all sorts of information that comes in on the nightly news and in the newspaper.
*  Oh, God, it's awful.
*  Yeah.
*  So it's a lot of work.
*  And but somehow that doesn't really convey what actually AI is and where we're at and
*  has we have we solved it or not.
*  But it's great to be able to talk with them.
*  And I love the fact that my mother, who is a grandmother, seventy five years old, and
*  she's a better programmer than I am.
*  Just an amazing, an amazing person.
*  Yeah, that's that's really a great story.
*  So my dad started off wanting to be a marine biologist in his youth.
*  So did you.
*  I understand.
*  True.
*  Is this going to continue?
*  Are we the last generation that starts off wanting to be marine biologists?
*  It seems like everyone that's that's what everyone's dream job when they're younger.
*  But now are the kids going to start wanting to be roboticists and things?
*  Gosh, I don't know.
*  I don't know.
*  I think that we are.
*  You know, it's it's our heritage as biological, evolved beings to be interested in, amazed
*  by, you know, inspired by nature around us.
*  I think that that's in some ways pretty hardwired into us.
*  So I think that people will continue to want to understand oceans and animals and plants
*  and such, because that that's where we come from as well.
*  But, yeah, I hope that more more kids are interested in becoming roboticists and computer
*  scientists.
*  Well, it always changes.
*  You start off wanting to be the marine biologist, but then it changes to roboticists.
*  So I'm wondering if the starting off is going to change, you know, as we're surrounded
*  more and more by the technology and things.
*  So that becomes part of our DNA that, you know, if we're raised by screens and devices,
*  then that's what that's what we're curious about at a formative age.
*  Right. You may be right.
*  Who knows? The phrase nature deficit disorder was just brought upon me by a friend the other
*  day. Have you ever have you heard this disorder?
*  No, I haven't.
*  I started looking it up. He said there's neuroscience involved, but no, not really.
*  But he's an outdoorsman.
*  And the idea is that we need nature.
*  And when we're deprived of nature, we develop this disorder.
*  So anyway, I'll let the listeners run with that and look that up.
*  We won't get into it.
*  So your technical expertise and background is in computer science and in robotics.
*  But I've heard you say that you're learning some neuroscience these days, maybe a lot.
*  I don't know why.
*  Well, I mean, when I joined DeepMind, one of the reasons that I did so was because DeepMind
*  was formed on the notion that we need to understand deep learning, as in these powerful
*  artificial neural networks.
*  We need reinforcement learning as a way of understanding how to learn from experience
*  and that we need neuroscience.
*  And so these were the three groups that started DeepMind.
*  And that's why I joined. I really thought that that was a pretty magical combination of
*  disciplines to understand intelligence.
*  And so the thing that I knew least about was neuroscience.
*  And so one of my projects that I worked on here was in navigation.
*  And so understanding how animals navigate place cells, grid cells, these sort of structures
*  in the brain, these different types of neurons was really inspiring to me because obviously
*  humans and animals don't navigate by drawing out maps and making an explicit representation of the
*  world. They have an internal representation of the world.
*  And so I really wanted to learn how to navigate in this end to end way where the representation of
*  the world would be internally in the state of the agent, the state of the network, the internal
*  memory, however you want to put it.
*  And so getting that inspiration from neuroscience was really important.
*  And in fact, in that research, we were able, I think, to give back something to validate some of
*  the neuroscience work that had been done on grid cells and place cells because of what we found.
*  So I think that there's a really wonderful virtuous cycle there that goes back and forth between
*  computer science, specifically AI and neuroscience.
*  And we're just beginning to just getting started with giving back to neuroscience instead of just
*  take, take, take.
*  And I'm excited about that.
*  So I wouldn't say that I've got given myself a proper education in any way in neuroscience, but at
*  least I can work through a journal article and not get lost.
*  Hey, that's more than I can do.
*  It's funny.
*  You know, I tend to interview mostly neuroscientists and when I ask them about the give and take
*  between neuroscience and AI moving forward, the neuroscientists tend to say, well, I think that AI
*  has a lot to give to neuroscience.
*  And the few people more on the AI side tend to see it, have seen it the opposite way that they've
*  either been inspired by neuroscience or that in the moving forward, neuroscience will give a lot
*  to AI.
*  That's not a hard and strict rule, but it's just an interesting pattern that's emerged talking to
*  people. So I wonder why.
*  Has the...so is the...you talked about when it began, when DeepMind was starting, those are the sort
*  of areas. Neuroscience was one of the areas that they felt like they needed to understand to solve
*  intelligence. Is that still a very ingrained part of the culture or is it moving away from that or
*  is it becoming more ingrained?
*  Do you know what the pattern is there?
*  No, we've expanded.
*  There's more, more breadth in terms of...we didn't have a robotics group when I started.
*  Now we do.
*  Yeah.
*  Other sorts of areas that have...where we've grown into, but neuroscience is definitely a very
*  fundamental part of what we study.
*  I think, you know, for me, a downside of how large DeepMind has grown is the fact that because of
*  that, the groups have pulled a little bit further apart.
*  So I don't work as closely with any of our neuroscientists anymore.
*  But it's still quite important.
*  There's still a lot of research being done by the neuroscience team that's quite important, led by
*  Matt Botvinick.
*  Yes. He's been on the podcast as well.
*  So, yeah, I realized...actually, I got a notice from one of the administrative people at DeepMind.
*  Hey, you're talking to a lot of DeepMind people here.
*  Just wanted to loop in.
*  So I was like, oh, yeah, I guess I am.
*  I was watching a talk by David Silver, and he was going over the Deep QN networks that were developed
*  that sort of famously played all these Atari games really well.
*  And someone asked him whether using these networks, we can learn interesting representations.
*  What can we get out?
*  What can we learn from the networks?
*  And basically, you know, it's a neuroscience related question.
*  And he said, you know, well, what we want to do is what neuroscientists would do, the equivalent of
*  FMRI on these networks.
*  And that was like a full stop for me because I thought you would, as a neuroscientist, my immediate
*  reaction was you would never do FMRI on a network like that.
*  And it just sort of hit me like there's still a lot of work between, you know, like, how naive must I
*  be about the AI side if just as a neuroscientist, I see, you know, a statement like that and I see how
*  inaccurate it is.
*  Right. From the neuroscience point of view.
*  And I think, gosh, I'm so naive about AI and like, how can we get closer to each other and, you know,
*  and talk more?
*  And I guess as organizations grow, that becomes harder and harder, I suppose, like you're saying.
*  It does. And yet there's lots of new opportunities to to discuss these things.
*  I mean, I'm excited about a new meeting that I'm going to be co-founding with Richard Blake, Blake
*  Richard, sorry, and and Tony Zador.
*  That will be a Cold Spring Harbor this spring.
*  And so that will be specifically that's NASIS, Neuroscience for AI Systems.
*  Oh, cool.
*  Is there a website for that yet?
*  Yeah, it's under Cold Spring Harbor.
*  I don't think that we've publicized it a lot yet, but we're going to have some great speakers, at
*  least a couple of them with touring awards to their name.
*  And that's really trying to get back to that close interaction that was, you know, that that's what
*  the Snowbird Workshop used to be about.
*  That's what NeurIPS used to be about.
*  And as these things grow or disappear in the case of Snowbird, then it's harder to get back to those
*  fundamental conversations between the different disciplines.
*  So, yeah, that's great.
*  I've had both Tony and Blake on the show as well.
*  I guess I'm doing something right.
*  Getting the right guests.
*  So before we kind of get into things, I'm curious, what can you do or say to me right now to
*  convince me that you are not in fact a robot?
*  Well, I think that maintaining a cohesive conversation for the last 15 minutes, that should be
*  good enough.
*  Yeah, sure. I'll press you on that.
*  I was going to ask for a Kathleen Turner impression since you alluded.
*  First of all, by the way, we were going to speak earlier a couple of weeks, maybe a week or two
*  earlier, but you had laryngitis and you alluded to Kathleen Turner as if I would know who
*  Kathleen Turner was.
*  And I feel slightly offended, I guess, by that, because a lot of our listeners have no idea who
*  Kathleen Turner is.
*  I'm sure that they don't, but it's still my favorite reference for, you know, the best you can
*  say when you've got laryngitis as well.
*  Maybe I'm a little bit more like Kathleen Turner.
*  I don't know. Yes, Romancing the Stone had a big impression on me.
*  I guess so. Yeah, I guess so.
*  Romancing the Stone.
*  Man. All right.
*  And, you know, my last question before we really get into it.
*  So you've worked on a lot of robots and your graduate work was on robots navigating
*  forests, I believe, if I'm correct.
*  Do you have a favorite robot from like books or films that, you know, is either well known or
*  maybe not so well known?
*  I mean, my favorite fake robot is definitely the defecating duck automaton.
*  Oh, Sherrington's?
*  Is that? Yeah. Yeah, I think so.
*  No, no, that wasn't Sherrington.
*  No, that couldn't sound I don't know.
*  It was a Dutch guy or something, right?
*  Yeah, exactly.
*  Had this lovely duck that you could feed grain to.
*  It would quack. I'm not sure if it moved around.
*  But and then if you waited a few minutes, it would defecate for you.
*  But it was exposed as being a fake because it was actually not digesting.
*  Right. So I love the fact that, you know, here's this amazing automaton that's been
*  developed that would be very hard to develop even today, something like this.
*  But somebody built this beautiful thing as complex as a clock.
*  And then people were upset that it wasn't actually digesting the food.
*  That's right.
*  But robots that are maybe a little bit less that are more upfront, more modern.
*  I have to say I'm absolutely fascinated by all of the biomimetic robots.
*  You know, that's that's the thing that I always click on online is when somebody has a new
*  snake robot or a bat robot or we recently had a demonstration of an of a squid, a soft
*  robot that was propelling itself around in water like a squid.
*  And these are just wonderful because they get at the heart, I think, of why we want to
*  develop robots and that's to, you know, solve the type of problems that nature has solved
*  through evolution, but be able to control this and use it to solve the problems that
*  we're interested in. So copying nature is fundamental, I think, to robotics.
*  Well, of course, you chose a squid, given your marine biologist's early giving toward
*  marine biology there.
*  What's also fascinating to me and hopefully I'll have someone on the show one day to talk
*  about this is like swarm intelligence with robots, you know, with robots that are acting
*  in mass in groups and stuff.
*  I think that's pretty fascinating stuff as well.
*  So we have recently seen the explosion.
*  It's it is recent, even though it doesn't feel recent, the explosion of deep learning.
*  But we don't we don't have robots assisting us in the kitchen to make dinner, for instance.
*  They could tell us the best ingredients to make dinner, but they're not assisting us
*  making dinner. We don't have robot tennis trainers yet, right?
*  They're great at recommending the best tennis trainer for us, for instance.
*  Where do you see robotics fitting in into the grand scheme of our little march here
*  toward developing A.I. that we would consider that would be satisfyingly general to us?
*  I think that we are just at the beginning of developing intelligence that is embodied
*  in an actual physical system, a robot that takes actions in the world.
*  And we're we're really are just at the beginning of this, where I'd say that computer
*  vision was, you know, 10 or 15 years ago when that field started to be transformed by deep learning.
*  And so when I talk to large groups of roboticists, for instance,
*  it grows big conference in robotics, I gave a keynote there last year, the year before.
*  And I told them that, you know, I thought that this was a a change, a transformation
*  into the field that's going to come because of deep learning and interactive learning systems and algorithms like reinforcement learning.
*  And there was a lot of a lot of people agreeing with me, but also a lot of a lot of doubt and skepticism.
*  And I think that that's because robotics is a much different domain than the other domains that we've seen transformed by deep learning,
*  for instance, vision, speech, understanding, speech recognition, text, machine translation, these other fields.
*  I think that solving robotics and understanding how to how to have an intelligence that is embodied in a physical system is very important.
*  I think that the intelligence of humans and other creatures on this planet is very much motivated and driven by how how the bodies of those creatures interact with the world.
*  So learning embodied intelligence is a much different thing, which makes it more challenging, but also potentially more powerful.
*  That's interesting because embodied cognition is is growing in the neurosciences.
*  And but it's a relatively new kind of hot topic.
*  So it's interesting. You know, the appreciation of embodiment has not always been there in neuroscience as well.
*  And I think that that's growing as in appreciation.
*  So so it's interesting to when you bring in robotics, you get this whole new set of problems to deal with that then you find are important to understanding how like how to move around in the world and interact with the world and in a robotics way.
*  So I think that's a really interesting thing.
*  So you experienced the the 2012 ImageNet success in visual deep learning with convolutional neural networks.
*  What parallels do you see today between the robotics moving, developing and the advent of the deep learning success?
*  Yeah, I mean, they look very similar in a lot of ways.
*  I was certainly part of that, you know, transformation of the computer vision field because the.
*  You know, in computer vision was dominated by these pipelines, this modular pipelines with these different models that were trained to extract features, to recognize features, to produce a classification,
*  maybe to fit to a model, you know, a deformable part model, for instance, of objects that were going to be recognized in an image.
*  And there's sort of this this modular pipeline of different algorithms that would go towards solving the problem of recognizing stuff from pixels.
*  And to have end to end learning be something that could improve upon that state of the art through something that's very simple and yet scalable was really a remarkable change in the field.
*  And as an arguably just that change has brought on so much of the A.I. revolution that we're now that we're now in a similar thing happened in machine translation, going from one language to another language.
*  You've got text in, you've got text out.
*  And in the middle there, the state of the art was this series of different modular algorithms that would extract features and put together, put together different parts and do alignment, etc.
*  Huge amount of work and expertise went into the system.
*  And similarly with speech recognition to go from recognizing phonemes and recognizing words and alignment to a language model, these different components.
*  And all of these fields were, you know, the state of the art was exceeded by a deep learning system that was trained end to end from whatever that input is, text or pixels to the desired output of other text in another language or characters or labels.
*  And when you look at robotics, well, the canonical methods right now that are used start with the perception of the robot from coming from the camera or from other types of sensors or the proprioception of the motors, joint positions, torques, etc.
*  So you have sort of these raw sensory inputs that are coming in.
*  And then you've got algorithms which extract entities from that perception, which build that into an explicit model of the world, like a map.
*  Then there is planning that's done on top of that.
*  Then there is something, then there is control, which takes the result of that planning and outputs actual torques to the motors or some sort of a control actions to the robot itself to move it.
*  And when you look at it this way, this is a pipeline of different modules that's going from raw sensory inputs to the desired output.
*  And it seems obvious that this could be improved if we could learn this end to end using a deep neural network, similarly to the other fields.
*  But this is a little different.
*  Robots are a little different.
*  So, a little different.
*  So, but all of those systems, those deep learning systems that you described are sort of closed systems.
*  I don't think I'm using that term right.
*  But in any case, you feed in some sensory data, like an image in a visual net, and then it spits out a category or something that's a tree or in the simplest cases.
*  But robots are different from all of these other sort of closed system applications because a robot moves and it changes the world.
*  Is that like the major difference?
*  Is that because as a robot uses its actuators and effectors, then it changes the sensory information coming in?
*  I don't know if you want to expand.
*  There are three big differences or three most important differences, which makes robots different from those other fields.
*  First of all, it's inherently sequential.
*  And yes, you change the world instead of your data coming from a data set.
*  You make your own data through your actions in the world.
*  You being the robot.
*  So you're building the robot has to build its own data set as it moves through the world or as it acts in the world.
*  And this makes the problem inherently sequential, which means that it now has the problem of things like catastrophic forgetting and instability that we get with with neural networks.
*  So that's one big area of difference.
*  The second big area is the fact that you've got hardware, that you're not just accumulating data on a server somewhere or on big machines and able to train on lots of data altogether.
*  Instead, you've got sort of this massively distributed processing that's going on.
*  If I've got many robots or if I've just got one robot, it has to that processing, that learning process has to happen there on the hardware.
*  So how do you get to that state of big data where I'm learning on lots and lots of data?
*  Because that's where we really see deep learning outperforming other systems is only in the space of big data, large networks and a lot of information.
*  It's really hard to get to that point with robots.
*  Even if you put a lot of them together, now you've got other problems.
*  You still have the problem of each of these different processors being separate entities in the world, essentially.
*  Which is very different than with the big data regimes of the other fields.
*  The other problem is also hardware.
*  So the other problem with hardware is that it's not robust enough.
*  So even if we did have a way of putting together lots of different data, lots of different experience and learning from that, just what we tried to do, then the hardware itself isn't necessarily robust enough to be able to survive.
*  This type of learning process, if you think about real world robots, which is why so many researchers use simulations.
*  But that has its own pitfalls.
*  But the third main area which makes robotics harder to solve as a deep learning problem is that we don't really know what we want.
*  Or when we do know what we want, it's awfully hard to learn that.
*  So we use rewards if we're using reinforcement learning.
*  But rewards for robots are very hard to come up with.
*  The right type of reward and very failable in different ways in terms of learning from those rewards.
*  You can have the problem where it's too sparse and you can't learn anything at all.
*  You can have the problem of reward hacking where your robot learns to solve the problem, but in entirely the wrong way.
*  Then there's things like, well, we can just use human demonstrations and copy those demonstrations.
*  This is also hard. It's hard to generalize from that.
*  And it's hard to scale that to enough data.
*  So I think that the that general category of we don't know how to say what we want when we do machine translation, we know what we want.
*  We want to go from French to English and we know what those should be.
*  When we label images, we know what we want there.
*  We want those images or we want those labels from those images.
*  But when we're training robots, we don't have very good general scalable ways to define what we want.
*  It's not as simple as a good defecation for its own reward.
*  It's Valkonsen.
*  I'm not sure if I'm pronouncing that correctly.
*  Did the pooping duck.
*  Yeah.
*  Are you tired of your dreams just slipping through your fingers like so many grains of sand?
*  Try the newest smart dream catchers and for a limited time upgrade yours to the new deep dream catchers.
*  Now with three extra hidden layers.
*  Just go to braininspired.co and press the red Patreon button there or just support the show if you like it.
*  Thank you, David, Nicholas, Mike and Yinan for your support of this podcast on Patreon.
*  Before we move on, let's talk about deep reinforcement learning.
*  So we have deep learning, which we've talked a lot about on the show, which is, you know, these multi layered networks that you feed in, feed some data into.
*  And it either categorizes a picture that you fed into it, for instance, is maybe one of the most well known version.
*  And then on the other hand, you have reinforcement learning, which, like you were just describing, you have basically an actor in the world take some action and that changes the world.
*  And you get a reward based on that action that feeds back into the agent's policy and how it behaves in the world.
*  That's a really, really rough description of enforcement learning.
*  So what is deep reinforcement learning?
*  Well, if you ask an RL person, then they will tell you that it's simply a function approximation and that that's the sum total of it.
*  It's simply a nice, complex, nonlinear function approximator that you use to fit the value function or the policy for your reinforcement learning algorithm.
*  Whereas if you ask a deep learning person what deep reinforcement learning is, then they will say, well, it's a neural network that's just like any other, except for that you're using an RL objective function, you're using an RL loss function.
*  So, you know, you can definitely look at it through two different lenses here.
*  But that aside, it really is both of those things.
*  We're taking a objective, a loss function that we're deriving from maximizing returns in an environment, as you said, and we're simply training a different type of function with those with those gradients.
*  I think that there are some things that are quite interesting that don't get caught by either a study of deep learning or a study of reinforcement learning that really do exist only in this cross section of approaches that we call deep reinforcement learning.
*  Because there's a lot of things that do not quite generalize from either of those domains, and you really need to look at them separately in the context of what happens in learning as you train this potentially very complex, very large neural network using these different loss functions.
*  I mean, I've been thinking about, I mean, there are these sort of three grand categories of learning supervised learning, unsupervised learning and reinforcement learning.
*  And, you know, we're terrible at predicting the future as humans.
*  But it's hard to imagine.
*  So these are really, really broad categories of learning, and it's hard to imagine that a new form of learning might be discovered or invented that won't be encompassed by these three types of really broad categories.
*  I mean, can you imagine another form of learning that we will come to appreciate as being a fundamental type of learning that that we will incorporate into intelligence systems or that we do as humans, right?
*  Because these types of learning can be applied to what we do as well.
*  There's truth in that, but also those categories of unsupervised learning, supervised learning and reinforcement learning are fairly artificial and come out of academic divisions that, you know, maybe aren't necessary.
*  I think that most people would agree that we're not going to get to something that we would call intelligence with only one of these methods.
*  Right.
*  It simply doesn't make sense.
*  I think that all of them will need to be parts of a learning system because we need ways of attaching value and ways of learning over extended time periods.
*  And that's something that reinforcement learning gives.
*  We need ways of learning from all of the data that we come across, and that's unsupervised learning.
*  And we need ways of having teachers be able to give specific answers, to be able to give ground truth answers and to assign categories and assign names to the things in our world.
*  And that would be supervised learning.
*  But I think that ideally this all comes together in one system.
*  If you ask Rich Sutton, I don't know if he's been on your podcast.
*  Finally, finally someone who hasn't been on.
*  Neither has Malkonson.
*  But Rich Sutton is a wonderful, wonderful person to have a conversation with.
*  OK.
*  But Rich Sutton, I think, might say that all of these are about prediction and that really there isn't any when we learn, there's no such thing as an external reward.
*  There's no such thing as that type of reward that we put in into a game, for instance, to train our ancients on.
*  Nor is there necessarily any such thing as a supervised label.
*  Instead, we just take in lots of information and we keep on trying to predict and we're trying to get things right all the time.
*  And that happens every time we touch our fingers together and predict that we're going to get that tactile response from each of our fingers.
*  At the same time that we see our fingertips come closer, that happens when we walk down a flight of stairs.
*  That also happens when we expect to get a confirmation about the name of an object or when we use language.
*  So to some extent, we can put all of the we can put these different categories of learning that I think are academic distinctions and put them all under the blanket of simply prediction.
*  Yeah, I mean, that's a very popular notion, too, in neuroscience these days.
*  That's what we do. That's what we are built to do. That's what our brands are built to do.
*  Oh, I was just going to mention forgetting as a learning mechanism.
*  I wonder if forgetting can be thought of as a fundamental way to learn because it's important to forget things that don't work out, I suppose.
*  But, you know.
*  Well, a lot of my research since joining at DeepMind has been on continual learning.
*  And so that is the study of for neural networks, at least that's a study of neural networks that can both transfer to new tasks and that also can not catastrophically forget previously learned tasks.
*  Yeah, I'm going to I'm going to ask you about that in just a second, actually.
*  We'll go a little bit deeper into that.
*  You talked about how a lot of people in robotics do a lot of work in simulation.
*  And so then there's, you know, simulating robotics, but then there's the actual doing the tasks in physical robots.
*  Well, what is the right balance developmentally when you're developing robotic algorithms and things?
*  What is the right balance between simulation and physical robots?
*  Presumably, you want to do as much as you can in a simulated environment, right, and get as far as you can get before you oil up the joints and stuff.
*  Well, what is simulation good for?
*  Simulation is good for prototyping, and it's good for understanding the complexity of an algorithm.
*  It's good for making sure that your code runs without bugs, things like this.
*  I'm not sure that it's good for coming up with solutions for what will work on a robot.
*  So it can be an accelerator of research.
*  It also can be a bit of a.
*  So Rodney Brooks, famous roboticist, and what he said is that simulations are doomed to succeed.
*  There you go. OK, so what does that mean?
*  It means that if you're defining the problem, then you can always make it work.
*  Yeah, same problem with like benchmarks in these types of things.
*  Yeah, exactly.
*  So if you're engineering your own problem domain, and then you're going to be doomed to succeed, meaning you will succeed, but you're not going to have necessarily learned anything from it or really solved the problem.
*  And I think that that's very true, especially, I dare say, in robotics, where a lot of the unsolved problems, the unsolved domains of interest are things that we can't even simulate very well.
*  So things like contacts.
*  When you look at a physics simulator, contacts are the thing that are hardest to model.
*  What do you mean contacts? Just to be really clear.
*  Just the contacts between, for instance, if you're trying to train an agent to control a robot to do a manipulation task, to pick up objects, then being able to model using a physics simulator, the contacts between the robot hand gripper and the actual object, is it slipping or is the friction enough?
*  And just these different things is very hard to do.
*  What's another thing that's hard to do in a physics simulator?
*  Soft, deformable objects.
*  Very hard to model well.
*  Yeah.
*  So, and somehow, I don't know whether or not this is by chance, but I suspect not, then these are exactly the areas that we also don't have, that the state of the art in robotics doesn't solve the problem.
*  These types of areas where there's a lot of contact, where there's uncertainty, where there's deformable objects or articulated objects, these are all areas where the current state of the art in robotics falls short and yet we can't simulate them.
*  So relying on simulators to do our research means that I feel like we are shying away from exactly what we need to be solving.
*  So the area where robots have really, really excelled in the last few decades has been in factories, right?
*  Where you have an entire, you know, mini BMW plant here in Cambridge that has a massive number of robots that completely assemble new minis and roll them off of the assembly line, fully put together and a human just gets in and drives them away.
*  It's remarkable.
*  But these environments are completely modeled in simulation.
*  They're very well known.
*  They have a high certainty and a very, you know, just a very high certainty about where everything is.
*  That the tires are always made of the same material.
*  They're never wet.
*  They're always at the same temperature.
*  So the contacts in that example are always going to be the same and you don't have to do a lot of modeling for variation there, I suppose.
*  Right.
*  So for us to rely too much on simulators means that we're going to be trying to solve the problems that we already know how to solve by very good methods.
*  There's no reason to reinvent those solutions.
*  So I think that we do need to focus on robotics, not fall into that local minima of finding solutions only in simulations, but really work on real robots in situations where there's a high degree of variation, where there's uncertainty, where there's dynamics.
*  Where there's deformable objects, all of these things.
*  I wonder if there's an analogy to be made when you are, for instance, trying to learn an instrument, a musical instrument.
*  I mean, you have to actually play the thing.
*  But then once there's a back and forth between simulating you're playing in your mind, playing the videotape and practicing in your head and then actually getting it in your hands, getting those contacts, you know, and playing it.
*  They're both very valuable, it seems, because the simulation actually does help you improve, it seems.
*  In the studies of learning anyway.
*  So, Raya, when you give talks, or at least the ones that I've seen, you do this nice thing where you list out some of the challenges for robotics and talk about the massive amounts of work that you've done to address those challenges.
*  And maybe for the sake of time today, we could focus on maybe two of those, hopefully, maybe more if there's more time.
*  But I would like to ask you about one in particular.
*  And then after that, maybe we can you can talk about one that a different one that you're excited about right now.
*  Does that sound good?
*  Sure.
*  So the one I would like to ask about is one that you have stated as being perhaps the most important to solve lifelong learning.
*  And you've already alluded to it talking earlier.
*  This is the idea of learning multiple tasks without forgetting each one as you learn them.
*  And I'm cheating here because there are actually multiple sub challenges within this one larger challenge.
*  But so the challenge, I suppose, as you put it, is can reinforcement learning, can deep reinforcement learning learn multiple tasks?
*  Do you want to just talk about what the challenges are here?
*  And and then maybe we can talk about catastrophic forgetting and some of the other.
*  Sure. Yeah, I think that lifelong learning or continual learning, as I tend to call it, is actually a bit of a laundry list.
*  The setting is that we learn tasks, we want an agent or a network to learn a set of tasks in sequence.
*  But then the desiderata of of things that we're looking for is pretty long.
*  So we want to not forget tasks that we learned before.
*  And so we want to avoid catastrophic forgetting.
*  We want to be able to do better on new tasks if they're related to tasks that we've already learned.
*  So that's forward transfer.
*  We may be looking for backwards transfer, which means that when I learn something,
*  when I learn a new task and then I go back to an old task, I actually immediately do better on it because I'm transferring backwards something important that I learned on a new task.
*  Another aspect is that we want to see things like skill composition.
*  So if I learn different skills from three different tasks and then I'm tested on a fourth task,
*  I'd like to be able to actually put these different things together and learn, you know,
*  and be able to immediately have this new skill that came from compositing what I've learned before.
*  There's also things like forgetting.
*  So you don't want to have catastrophic forgetting, but you also don't want to necessarily enforce that you're going to remember everything forever.
*  So you may want to be able to gracefully forget.
*  And you don't want this to scale.
*  You want this to be a process that where you're not just going to keep on adding on new neural networks, for instance,
*  and solving this by a giant ensemble of networks, but solve this in a scalable way.
*  So it's there's a lot of different criteria that we have for solving continual learning.
*  But it is a very powerful area for deep reinforcement learning in general and for robotics in particular.
*  Some of the work that I've done has been on avoiding catastrophic forgetting through elastic weight consolidation
*  as one approach that we that we had that was directly inspired by neuroscience, actually,
*  where we would understand which specific parts of the network, which neurons or which synapses to allow to be more plastic or less plastic
*  based on their importance for the task that we had just learned.
*  And that would allow parts of the neural network to adapt to learn new tasks and parts to stay more fixed so that we could continue to perform well on previous tasks.
*  So it's called elastic weight consolidation.
*  So the weights are elastic and then that they can change.
*  But some of them can be consolidated and change less if they need to be used in other tasks.
*  Is that correct?
*  OK, correct.
*  So it means that you can continue to reuse parts of your network that were important for one task.
*  You can reuse those for a new task that you learn.
*  So there is feature sharing and you could have forward transfer from this.
*  But you're not going to damage those.
*  You're not going to be able to change those weights.
*  So so this is I think has been quite exciting for people in the field.
*  Doesn't solve all of the problems.
*  But it does.
*  It makes made a dent, at least, in the problem.
*  And this was one of the first papers to show continual learning for deep reinforcement learning problems in that domain.
*  Another approach that we published just last year is called progress and compress.
*  And the idea here is that you're going to have a two phase learning process.
*  When you want to learn a new task, you're going to essentially concatenate a new neural network on that's going to be used just to learn that new task.
*  And it's going to be able to take advantage of all of the features that you've learned previously.
*  But you have the second neural network that's there to learn new things.
*  And this means that you can quickly learn on a new task, have forward transfer by taking advantage of what's in your base network.
*  And then that's the progress phase.
*  And I also call that the wake phase.
*  That's what you learn when you're active in the world.
*  And then the compressed phase or you could call it the sleep phase is when you want to consolidate that new task that you've learned back into your base network.
*  So this would be the process of doing knowledge distillation from the network that you've just learned back into your base network.
*  And this allows you to have a very scalable process where you can think about it as every day I wake up, I learn a new task.
*  I can take advantage of transfer for what I've learned before, but I learn this new task.
*  And then when I go to sleep, I consolidate that back into what I've learned before.
*  So in a very rough sense, again, inspired by neuroscience, but really taking this idea of active learning and then consolidation to turn this into a scalable process.
*  But these are built so the progress and compress networks are built on earlier work that you did with these progressive neural networks.
*  And so the idea is you train up a neural network on a task.
*  And then when you introduce a new task, you actually introduce a new network.
*  And so every new task that you introduce, you add on a network to the network group, I suppose.
*  You know, think about it as a column, you add a column to the network and the previous columns are all frozen.
*  So you can't overwrite those.
*  You just are able to take advantage of them.
*  And you have these lateral connections between every layer of the new column that you're adding and all of the columns of the perceiving preceding ones so that you can take take advantage of features that have been learned previously.
*  And it's interesting. You find that the more columns that you add on, the more tasks, the less and less work it takes to learn essentially the new task and to train up the new column of the network.
*  Correct.
*  This is decidedly not how brains are structured or function.
*  So I just thought that was an interesting thing.
*  But then but then you're adding on the compression progress and compress.
*  Yes, the compression part, which is inspired by how the brain works.
*  So it's an it's an interesting dynamic, a give and take.
*  And of course, I'm going to point to all of this work that we're talking about here for listeners that are just barely hanging on, you know, to these ideas.
*  Yeah. So so so so that's great.
*  So there's a lot of work being done in this continual learning push here.
*  And I mean, it is also just in deep reinforcement learning.
*  It's not just in robotics, but the robotics aspect has some special problems, as always associated with it, I suppose.
*  Right. I mean, even the simplest of the experiments that we did for some of these continual learning papers involved.
*  Millions and millions of examples, millions and millions of steps by the agent in the environment, whether that was Atari or something else.
*  And that's just not feasible on a robot.
*  So we did start looking at these approaches and continual learning as being a way that we could do a sim to real transfer.
*  So that's basically starting in simulation.
*  And you might train up for two or three tasks in simulation using this approach.
*  For instance, progress and compress.
*  And then you'd learn a new task that's now in the real world.
*  So just like in the games where with each new game that you learn, each new task that you learn, you need less and less data.
*  You can learn it more and more quickly than ideally when you learn some tasks in simulation and then you go to the real world equivalent.
*  You could learn that quickly and much more efficiently than starting from scratch on the real robot.
*  It's still tough to get to.
*  I don't think that we have the right algorithms to really get us to the complexity of tasks that we want.
*  I mean, we get excited when we stack two or three blocks on top of each other.
*  But that's a long ways away from, for instance, building a Lego house from the directions.
*  Yeah, but it's a long way from zero to that as well.
*  It is indeed. Yeah.
*  One of the areas that I'm excited about in robotics is looking at intrinsic motivation.
*  So instead of using rewards that are coming from smart PhD students coming up with how to reward an agent for picking up a block and stacking it on top of another block,
*  we instead start with an extended learning process where you use things like curiosity to motivate the robot to explore objects,
*  explore a tabletop with the idea that eventually you're going to learn how the robot can use its hand,
*  how the robot can touch the objects in its environment and interact with those.
*  And that if you learn through that process first, like a child would, that when you see an example of blocks stacked one on top of the other,
*  you already have the motor skills and the sort of the understanding in order to be able to do that quickly.
*  So I think that this is more of that merging of unsupervised learning plus some supervision or some learning from imitation that we talked about earlier.
*  If you could replace any part of your body with a machine, what would it be?
*  My face and my head.
*  Why?
*  Well, I just didn't.
*  I want to see if my face falls off.
*  So there are like three other challenges.
*  I'll just list them off.
*  And I wonder if you might want to say a few words about some of your work with one of them.
*  One is can reinforcement learning learn efficiently?
*  So this is a problem is that we have to feed it tons and tons of data.
*  And the progressive networks, the progressive neural networks and progressive compress address this a little bit because you have to learn through less and less data each time, I suppose.
*  The other is learning from real data, using real data to train networks up.
*  And this is the difference between sort of simulation and also and putting robots into the real world.
*  And you've used Google Street View.
*  You've done some work using Google Street View to train robots to do navigation tasks.
*  And then there's the problem, the challenge of continuous control, which is learning the continuous value of actions, for instance, muscle control and such.
*  I mean, are any of these hot in your mind right now?
*  Are any of them that you're excited about?
*  Or you can even we can go beyond that.
*  And you can just tell me about some of the recent work that you're working on that you're excited about.
*  Oh, well, all of all of those things are still are important to me and relevant.
*  I think that maybe we can touch on the work with Street View, because I really found that to be a important work to do to go from algorithms that we had been developing and training in simulated mazes
*  and going from that to a much more realistic environment where you actually could see the real world in terms of the photographic representation.
*  And this introduced a lot of complexity in terms of our experiments.
*  So we were training agents to using deep reinforcement learning to be able to get through mazes.
*  And we had these simulated 3D mazes that the agent would see from this first person perspective.
*  And go through the mazes and try to find the goal, this target object.
*  And then every episode was different.
*  And we could train agents to solve this problem, but only using massive amounts of data.
*  And I was really uncertain as to whether or not these were the results were meaningful for that reason.
*  And I wasn't sure whether or not that the algorithms could train if they were in a more real environment.
*  For example, one of the things that you did to get that agent to work really well was add depth into the training, right?
*  To learn the depth of the visual scene that the agent was seeing.
*  And it was just interesting that the depth improved, the agent learning depth improved the performance as much as it did.
*  It wasn't maybe something that you would have expected.
*  Right.
*  And that's really bringing in saying that, well, we need to learn from not just the sparse reward,
*  but also from auxiliary tasks or auxiliary loss functions.
*  And these improve and stabilize the learning process a lot.
*  And this is going back to the idea of predict everything all the time.
*  So if you predict, if you're in these 3D environments, then predicting depth makes a lot of sense.
*  So we started to look at Street View as being a source of real world imagery and real world complexity in terms of the layout of streets in a city.
*  So if you look at how the streets are laid out in London and New York and Paris, it can be really interesting, very different, very complex.
*  Pittsburgh. Pittsburgh has hills. That makes it fun. Is that where you live?
*  Yeah.
*  So we took Google Street View and we turned it into this interactive environment where the agent would get to take a step from through the different panoramas in Street View
*  and try to find different goals, trying to find different positions in the city.
*  And there's a lot of visual noise along the way in terms of having buses cross past or different types of noise in the scene,
*  pedestrians and lights and trees and all these different things.
*  But really what we found was that the agent was able to interpret the visual world in that complexity,
*  be able to correctly anticipate where there was a four way turn or a stop sign coming up,
*  these different sorts of geometries of street and be able to interpret that,
*  pick a direction and be able to learn the city and go towards the goal.
*  So that project was very complex because in part because we were using real world data.
*  So it did not have the ease of using a simulator that we had built ourselves because we had to deal with privacy.
*  We had to deal with making this data set public, having all of the data checked to make sure that it didn't contain any faces or license plates, things like this.
*  Things that Google doesn't care about.
*  No, I'll have to edit that out.
*  You're a Google company. We can't talk about privacy.
*  Things that Google does care about.
*  That's exactly why I had to do even though the Google algorithms automatically blur faces in the data.
*  We had to take every single image, 100,000 images and run it past an actual human using mechanical Turk to make sure that that was correct.
*  Because if Google's automatic face detection algorithms are failing, 0.1 percent of the time,
*  we need to find those images and make sure that those faces are blue.
*  We still need humans.
*  So we still need we still need humans.
*  But doing this had the virtue of being able to produce data that now other people could use.
*  So the data set is called Street Learn and the environment is public as well.
*  And being able to validate our research and show that we could train an agent that could navigate as well as a human across all of Manhattan, across all of London, across all of Paris.
*  And the way this works is you would just drop it, drop this agent randomly in the city and it would have a courier task, right?
*  Where it would have to deliver something somewhere.
*  So you wouldn't start it from the same spot each time.
*  It would just appear in a location and would have to figure out how to deliver flowers.
*  It gets a reward if it gets close enough to the goal within 100 meters of the goal.
*  Then it gets given a reward and gets given a new destination that has to go to.
*  And it's got a long episode, I think, 10,000 steps, and it tries to get through as many of these random stops as it can.
*  And this is very hard to learn from scratch by the agent.
*  But we started with a curriculum where first it's only delivering things nearby and then it gradually expands until it's learned the entire city sort of internally to the representation.
*  So there's no external map here.
*  There's no external representation.
*  It's all intrinsic to the to the LSTM and the confino of the network.
*  Good stuff.
*  I'm reading or I just finished reading The Age of Surveillance Capitalism, which talks a lot about Street View and collecting this data and stuff and how it happened and the legalities and things like that, the policies and things.
*  So it's interesting that we're now using this data, at least for good, right?
*  Or for if you consider training, training of robots, good.
*  Thinking about what this might look like, just projecting for a robot, robots running around cities.
*  Couriers. This is not the way it's going to happen.
*  You know, we're not training for actual robot couriers to run around cities and deliver things unless we are.
*  Why are we so bad at predicting what the future looks like?
*  It's an interesting question.
*  I realize at times how bad we are.
*  And there are people with a specific job of that they are futurists and they try to think about these things.
*  Yeah, that's a job.
*  They take that as their job description because it really is a difficult thing to try to think forward, you know, five, ten, fifty years into the future and think about what could possibly be there.
*  And, you know, I'm a deep mind.
*  I'm at the forefront of innovation in AI.
*  And it's hard for me.
*  I have to really think about it to think where are where will we be in 20 years?
*  Where will we be in 50 years?
*  Where will we be in two years?
*  Right.
*  I do think that sometimes we tend to think locally and think, well, what do we need a robot for?
*  I don't need a robot in my house.
*  I don't need another device.
*  But that's not really what it's for.
*  That's not a problem that needs to be fixed.
*  The problems that need to be fixed are where we have factories where humans and even children are still putting together, connecting wire A to wire B, because that's something that a robot can't do now.
*  Yeah.
*  So there's still a lot of problems or hazardous environments where we really don't want to put people.
*  And if we had more capable robots than the robots could do those jobs and save lives.
*  So it's important to keep in mind where the real problems are of our world, not think too locally about just our our own lives, but think about what are the problems that need solving that we don't know how to solve right now?
*  Where would help people?
*  Where would help?
*  Where would innovation help societies, help towns, help help cultures?
*  What do you when you close your eyes and envision yourself, whatever, 10 years from now, what do you envision yourself working on?
*  And this can be a hopeful answer or an optimistic answer as well.
*  Ceramics, pottery, that's what it's going to be.
*  That's that. That's my usual take is that, you know, my mother, my mother started doing computer science when she was 60.
*  So in about 15 years, I can look forward to that myself or maybe building robots to protect my garden from the rabbits and woodchucks.
*  Well, that's military application right there.
*  Or you could build a robot to make pottery.
*  How about that?
*  No, that would take the fun out of it.
*  Well, speaking of the future, there's a lot of talk about ethics these days in A.I.
*  And there are a lot of doomsday singularity projections about when A.I.s get too smart for their britches.
*  And I part of my research for this show is sort of look, you know, studying the early days of A.I. and neuroscience.
*  And I feel like when the like good old fashioned A.I. days, right, early when the when artificial intelligence, the term was coined.
*  There was a lot more talk, I feel like, about optimistic futures, right?
*  Robot companions, the Jetsons cartoon, that sort of thing.
*  But there wasn't nearly as much talk about the doomsday types of scenarios.
*  And I'm wondering, but given our current state.
*  So, yes, we've made a lot of advances, right?
*  There's been the deep learning revolution, I guess you could say.
*  And there are a lot of advances and you're working hard to push the robotics front ahead with deep reinforcement learning.
*  But why are we it seems like we're still way far away from even being near where that could be a feasible problem to face.
*  And you're just talking about, you know, keeping an eye on what the right problems are to focus on.
*  So why are we why are we worried now?
*  By we, I mean, a few people that have a lot of money that that have influence on social media and stuff.
*  But is it fundamentally different now that we need to start worrying about it?
*  No, I don't. I don't think that it is.
*  I think that the media, sorry to implicate you as well, but I think that the media really loves to think about these extremes.
*  I really don't see any danger of a super intelligent robot wreaking havoc on our world.
*  I really think that that is science fiction.
*  And there are much more important things that if we want to worry and we want to take action on, I think that we should worry about deep fakes.
*  I think that we should worry about autonomous weapons and the sort of the the use of the AI techniques that we have now in the wrong hands in terms of doing automatic targeting and these sorts of things.
*  I think that we need to worry about social bias and exacerbating social bias through automatic decision algorithms.
*  So I think that there's a lot of things that we can worry about now.
*  And it's more important that we worry about those and and an act to find fixes there than we worry about doomsday scenarios,
*  existential risk scenarios that I just don't think are supported at all by where research is going.
*  I also think that and those risks are real.
*  Sorry, the risks of things like autonomous weapons and societal bias and privacy issues, these sorts of things are real.
*  So why continue to work on AI?
*  And the answer is that there are a lot of problems that we want to find answers for that are incredibly important.
*  Understanding how to solve climate change is extremely important.
*  If AI can be developed that can find a solution to that, because AI knows how to process lots of data and find solutions that are not known to to human scientists,
*  then that would be an incredible benefit to our world.
*  If we can use AI approaches to improve the power efficiency of all of our systems,
*  then that would be a benefit as well, coming out the climate problem from a different side.
*  And if we can use AI approaches to better understand humans and how they work from the point of view of medicine,
*  from the point of view of neuroscience, then that's also a benefit.
*  There's still an awful lot of ways, a lot of diseases out there that have no cures.
*  And we have a lot of data.
*  This also seems like a problem that deep learning approaches are well suited for.
*  So I think that there's a lot of hope and there's a lot of excitement in some of these different areas.
*  And I do hope that the concern about doomsday type of scenarios doesn't overshadow that.
*  Me too.
*  How do we get people to work on these worthwhile problems instead of working at social media companies that are making billions of dollars?
*  Well, I think that talking about the problems is important.
*  I think that supporting them in various ways.
*  I think that the government support these.
*  I think that, you know, not because I'm a Google employee,
*  but I will just say that I think that Google does a really wonderful job at having a lot of fostering,
*  a lot of startups, a lot of development to look at different types of problems of climate change, of all sorts of things.
*  I think that that's really valuable to have that freedom.
*  I don't know.
*  Yeah, it's an ongoing problem.
*  So I know that we're just out of time here and I will point to.
*  So I unsmoothly transitioned from talking about your research to these sort of broader questions.
*  So I apologize for that.
*  But I'll point to also some talks that you've given that which lay these things out really nicely.
*  And I have one more question before I let you go.
*  What is something that you used to believe that you believe is naive now?
*  Well, I suppose I used to think that all of the interesting problems could be solved with a big data set and,
*  you know, a feedforward convolutional neural network.
*  And now I have now I think that all of the interesting problems involve time and involve extended decision making problems
*  that you don't see in a single image or in the elements of a single data set.
*  So I think just zooming out from the smaller problems that I used to be very focused on towards larger,
*  larger problems of intelligence and algorithms.
*  Very good. Well, you know, these days, Hollywood is only makes remakes of previous movies.
*  There's nothing original coming out. So but if they're going to make a remake of Romancing the Stone,
*  they better do it soon because everybody ages and dies.
*  Or unless they end up using robots, maybe there'll be a robotic Kathleen Turner in the remake of Romancing the Stone.
*  We should hope so. Raya, thank you.
*  Thank you so much for taking so much time with me today.
*  Thank you, Paul.
*  Brain Inspired is a production of me and you.
*  You can support the show through Patreon for a microscopic two or four dollars per month.
*  Go to BrainInspired.co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show and prohibit any annoying advertisements like you hear on other shows.
*  To get in touch with me, email Paul at BrainInspired.co.
*  The music you hear is by The New Year. Find them at TheNewYear.net.
*  Thanks for your support. See you next time.
*  Mayday, mayday
*  We've left all hating
*  Searching the coffers
*  For empty offers
*  I don't know why
*  You trust the sky
*  You must like your lies from blue eyes

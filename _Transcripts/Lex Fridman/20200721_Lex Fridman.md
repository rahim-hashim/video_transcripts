---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 6096s
Video Keywords: ['jitendra malik', 'deep learning', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 59453
Video Rating: None
Video Description: Jitendra Malik is a professor at Berkeley and one of the seminal figures in the field of computer vision, the kind before the deep learning revolution, and the kind after. He has been cited over 180,000 times and has mentored many world-class researchers in computer science.

Support this podcast by supporting our sponsors:
- BetterHelp: http://betterhelp.com/lex
- ExpressVPN at https://www.expressvpn.com/lexpod

EPISODE LINKS:
Jitendra's website: https://people.eecs.berkeley.edu/~malik/
Jitendra's wiki: https://en.wikipedia.org/wiki/Jitendra_Malik

PODCAST INFO:
Podcast website:
https://lexfridman.com/podcast
Apple Podcasts:
https://apple.co/2lwqZIr
Spotify:
https://spoti.fi/2nEwCF8
RSS:
https://lexfridman.com/feed/podcast/
Full episodes playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

OUTLINE:
0:00 - Introduction
3:17 - Computer vision is hard
10:05 - Tesla Autopilot
21:20 - Human brain vs computers
23:14 - The general problem of computer vision
29:09 - Images vs video in computer vision
37:47 - Benchmarks in computer vision
40:06 - Active learning
45:34 - From pixels to semantics
52:47 - Semantic segmentation
57:05 - The three R's of computer vision
1:02:52 - End-to-end learning in computer vision
1:04:24 - 6 lessons we can learn from children
1:08:36 - Vision and language
1:12:30 - Turing test
1:16:17 - Open problems in computer vision
1:24:49 - AGI
1:35:47 - Pick the right problem

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Jitendra Malik Computer Vision  Lex Fridman Podcast #110
**Lex Fridman:** [July 21, 2020](https://www.youtube.com/watch?v=LRYkH-fAVGE)
*  The following is a conversation with Jitendra Malik, a professor at Berkeley and one of the
*  seminal figures in the field of computer vision, the kind before the deep learning revolution
*  and the kind after. He has been cited over 180,000 times and has mentored many world-class
*  researchers in computer science. Quick summary of the ads. Two sponsors,
*  one new one, which is BetterHelp and an old goodie, ExpressVPN. Please consider supporting
*  this podcast by going to betterhelp.com slash Lex and signing up at expressvpn.com slash LexPod.
*  Click the links, buy the stuff. It really is the best way to support this podcast and the journey
*  I'm on. If you enjoy this thing, subscribe on YouTube, review it with five stars on Apple
*  Podcasts, support it on Patreon or connect with me on Twitter at Lex Friedman. However,
*  the heck you spell that. As usual, I'll do a few minutes of ads now and never any ads in the middle
*  that can break the flow of the conversation. This show is sponsored by BetterHelp, spelled H-E-L-P
*  help. Check it out at betterhelp.com slash Lex. They figure out what you need and match
*  you with a licensed professional therapist in under 48 hours. It's not a crisis line,
*  it's not self-help, it's professional counseling done securely online. I'm a bit from the David
*  Goggins line of creatures, as you may know, and so have some demons to contend with, usually on
*  long runs or all nights working, forever impossibly full of self-doubt. It may be because I'm Russian,
*  but I think suffering is essential for creation. But I also think you can suffer beautifully in a
*  way that doesn't destroy you. For most people, I think a good therapist can help in this,
*  so it's at least worth a try. Check out their reviews. They're good. It's easy, private,
*  affordable, available worldwide. You can communicate by text, any time and schedule weekly audio and
*  video sessions. I highly recommend that you check them out at betterhelp.com slash Lex.
*  This show is also sponsored by ExpressVPN. Get it at expressvpn.com slash Lex pod to support this
*  podcast and to get an extra three months free on a one-year package. I've been using ExpressVPN
*  for many years. I love it. I think ExpressVPN is the best VPN out there. They told me to say
*  but it happens to be true. It doesn't log your data. It's crazy fast and is easy to use.
*  Literally just one big sexy power on button. Again, for obvious reasons, it's really important that
*  they don't log your data. It works on Linux and everywhere else too, but really why use anything
*  else? Shout out to my favorite flavor of Linux, Ubuntu Mate 2004. Once again, get it at expressvpn.com
*  slash Lex pod to support this podcast and to get an extra three months free on a one-year package.
*  Now here's my conversation with Jitendra Malik. In 1966, Seymour Papert at MIT wrote up a proposal
*  called the Summer Vision Project to be given, as far as we know, to 10 students to work on and
*  solve that summer. That proposal outlined many of the computer vision tasks we still work on today.
*  What do you think we underestimate and perhaps we did underestimate and perhaps still underestimate
*  how hard computer vision is? Because most of what we do in vision, we do unconsciously or
*  subconsciously. In human vision. In human vision. That gives us this, that effortlessness gives us
*  the sense that, oh, this must be very easy to implement on a computer. Now,
*  this is why the early researchers in AI got it so wrong. However, if you
*  go into neuroscience or psychology of human vision, then the complexity becomes very clear.
*  The fact is that a very large part of the cerebral cortex is devoted to visual processing.
*  I mean, and this is true in other primates as well. So once we looked at it from a
*  neuroscience or psychology perspective, it becomes quite clear that the problem is very challenging
*  and it will take some time. You said the higher level parts are the harder parts?
*  I think vision appears to be easy because most of what visual processing is subconscious or
*  unconscious. So we underestimate the difficulty. Whereas when you are
*  proving a mathematical theorem or playing chess, the difficulty is much more evident
*  because it is your conscious brain which is processing various aspects of the problem
*  solving behavior. Whereas in vision, all this is happening, but it's not in your
*  awareness. It's operating below that. But it still seems strange. Yes, that's true,
*  but it seems strange that as computer vision researchers, for example,
*  the community broadly is time and time again makes the mistake of thinking the problem is
*  easier than it is. Or maybe it's not a mistake. We'll talk a little bit about autonomous driving,
*  for example, how hard of a vision task that is. Is it just human nature or is there something
*  fundamental to the vision problem that we underestimate? We're still not able to be
*  cognizant of how hard the problem is. Yeah, I think in the early days it could have been
*  excused because in the early days all aspects of AI were regarded as too easy. But I think today
*  it is much less excusable. And I think why people fall for this is because of what I call the fallacy
*  of the successful first step. There are many problems in vision where getting 50% of the
*  solution you can get in one minute. Getting to 90% can take you a day. Getting to 99% may take you
*  five years and 99.99% may be not in your lifetime. I wonder if that's the unique division. It seems
*  that language people are not so confident about, so natural language processing people are a little
*  bit more cautious about our ability to solve that problem. I think for language people intuit
*  that we have to be able to do natural language understanding. For vision, it seems that we're not
*  cognizant or we don't think about how much understanding is required. It's probably still
*  an open problem. But in your sense, how much understanding is required to solve vision?
*  Put another way, how much something called common sense reasoning is required to really be able to
*  interpret even static scenes? Yeah. So vision operates at all levels and there are parts which
*  can be solved with what we could call maybe peripheral processing. So in the human vision
*  literature, there used to be these terms sensation, perception, and cognition,
*  which roughly speaking referred to the front end of processing, middle stages of processing,
*  and higher level of processing. I think they made a big deal out of this and they wanted to
*  study only perception and then dismiss certain problems as being cognitive. But really,
*  I think these are artificial divides. The problem is continuous at all levels and there are challenges
*  at all levels. The techniques that we have today, they work better at the lower and mid-levels of
*  the problem. I think the higher levels of the problem, quote, the cognitive levels of the
*  problem are there and in many real applications, we have to confront them. Now, how much
*  that is necessary will depend on the application. For some problems, it doesn't matter. For some
*  problems, it matters a lot. So I am, for example, a pessimist on fully autonomous driving in the near
*  future. And the reason is because I think there will be that 0.01% of the cases where quite
*  sophisticated cognitive reasoning is called for. However, there are tasks where you can,
*  first of all, they are much more, they are robust. So in the sense that error rates,
*  error is not so much of a problem. For example, let's say you're doing image search. You're trying
*  to get images based on some description, some visual description. We are very tolerant of errors
*  there, right? I mean, when Google Image Search gives you some images back and a few of them are
*  wrong, it's okay. It doesn't hurt anybody. There's not a matter of life and death. But
*  making mistakes when you are driving at 60 miles per hour and you could potentially kill somebody
*  is much more important. So just for the fun of it, since you mentioned, let's go there briefly
*  about autonomous vehicles. So one of the companies in the space, Tesla, is with Andhra Pratapati
*  and Elon Musk are working on a system called Autopilot, which is primarily a vision-based
*  system with eight cameras and basically a single neural network, a multitask neural network.
*  They call it HydroNet, multiple heads. So it does multiple tasks, but is forming the same
*  representation at the core. Do you think driving can be converted in this way to purely a vision
*  problem and then solved with learning? Or even more specifically in the current approach, what
*  do you think about what Tesla Autopilot team is doing? So the way I think about it is that
*  there are certainly subsets of the visual-based driving problem, which are quite solvable.
*  So for example, driving in freeway conditions is quite a solvable problem. I think there were
*  demonstrations of that going back to the 1980s by someone called Ernst Tickman in Munich.
*  In the 90s, there were approaches from Carnegie Mellon. There were approaches from our team at
*  Berkeley. In the 2000s, there were approaches from Stanford and so on. So autonomous driving
*  in certain settings is very doable. The challenge is to have an autopilot work under all kinds of
*  driving conditions. At that point, it's not just a question of vision or perception, but really
*  of control and dealing with all the edge cases. So where do you think most of the difficult cases,
*  to me, even the highway driving is an open problem because it applies the same 50-90-95-99 rule
*  or the fallacy of the first step, I forget how you put it, we fall victim to. I think even highway
*  driving has a lot of elements because to solve autonomous driving, you have to completely
*  relinquish the help of a human being. You're always in control. So you're really going to
*  feel the edge cases. So I think even highway driving is really difficult. But in terms of
*  the general driving task, do you think vision is the fundamental problem or is it also your action,
*  the interaction with the environment, the ability to... And then the middle ground,
*  I don't know if you put that under vision, which is trying to predict the behavior of others,
*  which is a little bit in the world of understanding the scene, but it's also trying to form a model
*  of the actors in the scene and predict their behavior.
*  Yeah, I include that in vision because to me, perception blends into cognition and building
*  predictive models of other agents in the world, which could be other agents, could be people,
*  other agents, could be other cars. That is part of the task of perception because perception always
*  has to not tell us what is now, but what will happen because what's now is boring. It's done.
*  It's over with. We care about the future because we act in the future.
*  And we care about the past in as much as it informs what's going to happen in the future.
*  So I think we have to build predictive models of behaviors of people and those can get quite
*  complicated. I've seen examples of this in... Actually, I own a Tesla and it has various
*  safety features built in. And what I see are these examples where, let's say there is some
*  skateboarder. I don't want to be too critical because obviously these systems are always being
*  improved and any specific criticism I have, maybe the system six months from now will not have that
*  particular failure mode. So it had the wrong response and it's because it couldn't predict
*  what this skateboarder was going to do. Because it really required that higher level cognitive
*  understanding of what skateboarders typically do as opposed to a normal pedestrian. So what might
*  have been the correct behavior for a pedestrian, a typical behavior for a pedestrian was not the
*  typical behavior for a skateboarder. So therefore, to do a good job there,
*  you need to have enough data where you have pedestrians, you also have skateboarders,
*  you've seen enough skateboarders to see what kinds of patterns of behavior they have.
*  So it is in principle with enough data that problem could be solved. But I think our
*  current systems, computer vision systems, they need far, far more data than humans do
*  for learning those same capabilities. So say that there is going to be a system that solves
*  autonomous driving. Do you think it will look similar to what we have today but have a lot
*  more data, perhaps more compute, but the fundamental architecture is involved? Like, well, in the case
*  of Tesla autopilot is neural networks. Do you think it will look similar in that regard and
*  we'll just have more data? That's a scientific hypothesis as to which way is it going to go.
*  I will tell you what I would bet on. So, and this is my general philosophical position on how these
*  learning systems have been. What we have found currently very effective in computer vision
*  in the deep learning paradigm is sort of tabular ASA learning and tabular ASA learning in a
*  supervised way with lots and lots of... What's tabular ASA? Tabular ASA in the sense that blank
*  slate. We just have the system which is given a series of experiences in this setting and then
*  it learns there. Now, if let's think about human driving, it is not tabular ASA learning. So at the
*  age of 16 in high school, a teenager goes into driver ed class. And now at that point they learn
*  but at the age of 16, they're already visual geniuses because from zero to 16,
*  they have built a certain repertoire of vision. In fact, most of it has probably been achieved by
*  age two. In this period of age up to age two, they know that the world is three-dimensional.
*  They know how objects look like from different perspectives. They know about occlusion. They
*  know about common dynamics of humans and other bodies. They have some notion of intuitive physics.
*  So they have built that up from their observations and interactions
*  in early childhood and of course, reinforced through their growing up to age 16. So then
*  at age 16, when they go into driver ed, what are they learning? They're not learning afresh
*  the visual world. They have a mastery of the visual world. What they are learning is control.
*  They're learning how to be smooth about control, about steering and brakes and so forth.
*  They're learning a sense of typical traffic situations. Now, that education process
*  can be quite short because they are coming in as visual geniuses. And of course, in their future,
*  they're going to encounter situations which are very novel. So during my driver ed class,
*  I may not have had to deal with a skateboarder. I may not have had to deal with a truck
*  driving in front of me where the back opens up and some junk gets dropped from the truck
*  and I have to deal with it. But I can deal with this as a driver even though I did not
*  encounter this in my driver ed class. And the reason I can deal with it is because I have all
*  this general visual knowledge and expertise. And do you think the learning mechanisms we have today
*  can do that kind of long term accumulation of knowledge? Or do we have to do some kind of,
*  you know, the work that led up to expert systems with knowledge representation,
*  you know, the broader field of what of artificial intelligence worked on this kind of accumulation
*  of knowledge. Do you think neural networks can do the same? I think I don't see any in principle
*  problem with neural networks doing it. But I think the learning techniques would need to evolve
*  significantly. So the current learning techniques that we have are supervised learning. You're given
*  lots of examples, X, Y, Y pairs and you learn the functional mapping between them. I think that
*  human learning is far richer than that. It includes many different components. So I think
*  it includes many different components. There is a child explores the world and sees, for example,
*  a child takes an object and manipulates it in his or her hand and therefore gets to see the object
*  from different points of view. And the child has commanded the movement. So that's a kind of
*  learning data, but the learning data has been arranged by the child. And this is a very rich
*  kind of data. The child can do various experiments with the world. So there are many aspects of
*  sort of human learning and these have been studied in child development by psychologists.
*  And what they tell us is that supervised learning is a very small part of it.
*  There are many different aspects of learning. And what we would need to do is to develop models of
*  all of these and then train our systems with that kind of protocol.
*  So new methods of learning, some of which might imitate the human brain. But you also,
*  in your talks, have mentioned sort of the compute side of things,
*  in terms of the difference in the human brain or referencing Hans Moravec.
*  Do you think there's something interesting, valuable to consider about the difference
*  in the computational power of the human brain versus the computers of today in terms of
*  instructions per second? Yes. So if we go back, so this is a point I've been making for 20 years now.
*  And I think once upon a time, the way I used to argue this was that we just didn't have the
*  computing power of the human brain. Our computers were not quite there. And I mean, there is a
*  well-known trade-off, which we know that neurons are slow compared to transistors,
*  but we have a lot of them and they have a very high connectivity. Whereas in silicon,
*  you have much faster devices, transistors switch on the order of nanoseconds,
*  but the connectivity is usually smaller. At this point in time, I mean, we are now talking about
*  2020, we do have, if you consider the latest GPUs and so on, amazing computing power. And if we
*  look back at Hans Moravec's type of calculations, which he did in the 1990s, we may be there today
*  in terms of computing power comparable to the brain, but it's not of the same style.
*  It's of a very different style. So I mean, for example, the style of computing that we have in
*  our GPUs is far, far more power hungry than the style of computing that is there in the human
*  brain or other biological entities. Yeah. And that the efficiency part is we're going to have
*  to solve that in order to build actual real world systems of large scale. Let me ask sort of the
*  high level question, the step, taking a step back, how would you articulate the general problem of
*  computer vision? Does such a thing exist? So if you look at the computer vision conferences and
*  the work that's been going on, it's often separated into different little segments,
*  breaking the problem of vision apart into whether segmentation, 3D reconstruction,
*  object detection, I don't know, image captioning, whatever, there's benchmarks for each. But if you
*  were to sort of philosophically say, what is the big problem of computer vision? Does such a thing
*  exist? Yes, but it's not in isolation. So for all intelligence tasks, I always go back to sort of
*  biology or humans. And if you think about vision or perception in that setting, we realize that
*  perception is always to guide action. Perception for a biological system does not give any benefits
*  unless it is coupled with action. So we can go back and think about the first multicellular animals
*  which arose in the Cambrian era, 500 million years ago. And these animals could move and they could
*  see in some way. And the two activities helped each other. Because how does movement help? Movement
*  helps that because you can get food in different places. But you need to know where to go. And
*  that's really about perception or seeing. I mean, vision is perhaps the single most perception sense,
*  but all the others are equally are also important. So perception and action kind of go together.
*  So earlier it was in these very simple feedback loops, which were about finding food or avoiding
*  becoming food if there's a predator running, trying to eat you up and so forth. So we must
*  at the fundamental level connect perception to action. Then as we evolved, perception became
*  more and more sophisticated because it served many more purposes. And so today we have what seems like
*  a fairly general purpose capability, which can look at the external world and build a model of
*  the external world inside the head. We do have that capability. That model is not perfect.
*  And psychologists have great fun in pointing out the ways in which the model in your head is not
*  a perfect model of the external world. They create various illusions to show the ways in which it is
*  imperfect. But it's amazing how far it has come from a very simple perception action loop that
*  exists in an animal 500 million years ago. Once we have these very sophisticated visual systems,
*  we can then impose a structure on them. It's we as scientists who are imposing that structure
*  where we have chosen to characterize this part of the system as this quote module of
*  object detection or quote this module of 3D reconstruction. What's going on is really all
*  of these processes are running simultaneously and they are running simultaneously because
*  originally their purpose was in fact to help guide action. So as a guiding general statement
*  of a problem, do you think we can say that the general problem of computer vision,
*  you said in humans it was tied to action. Do you think we should also say that ultimately the
*  goal, the problem of computer vision is to sense the world in a way that helps you
*  act in the world? Yes, I think that's the most fundamental. That's the most fundamental purpose.
*  We have by now hyper evolved. So we have this visual system which can be used for other things.
*  For example, judging the aesthetic value of a painting. And this is not guiding action.
*  Maybe it's guiding action in terms of how much money you will put in your auction bid, but that's
*  a bit stretched. But the basics are in fact in terms of action. But we have evolved really this
*  hyper, we have hyper evolved our visual system. Actually, just to sorry to interrupt, but perhaps
*  it is fundamentally about action. You kind of jokingly said about spending, but perhaps
*  the capitalistic drive that drives a lot of the development in this world
*  is about the exchange of money. The fundamental action is money. If you watch Netflix,
*  if you enjoy watching movies, you're using your perception system to interpret the movie.
*  Ultimately, your enjoyment of that movie means you'll subscribe to Netflix. So the action is
*  this extra layer that we've developed in modern society perhaps is fundamentally
*  tied to the action of spending money. Well, certainly with respect to
*  interactions with firms. So in this homo economicus role, when you're interacting with firms,
*  it does become that. What else is there?
*  Now is a rhetorical question. Okay. So to linger on the division between the static and the dynamic,
*  so much of the work in computer vision, so many of the breakthroughs that you've been a part of
*  have been in the static world and looking at static images. And then you've also worked on
*  starting, but it's a much smaller degree. The community is looking at dynamic and video at
*  dynamics. And then there is robotic vision, which is dynamic, but also where you're actually have a
*  robot in the physical world interacting based on that vision. Which problem is harder?
*  The trivial first answer is, well, of course one image is harder. But if you look at a deeper
*  question there, are we, what's the term, cutting ourselves at the knees or like making the problem
*  harder by focusing on images? That's a fair question. I think sometimes we can simplify
*  our problems so much that we essentially lose part of the juice that could enable us to solve the
*  problem. And one could reasonably argue that to some extent this happens when we go from video to
*  single images. Now, historically you have to consider the limits imposed by the
*  computation capabilities we had. So if we, many of the choices made in the computer vision community
*  through the 70s, 80s, 90s can be understood as choices which were forced upon us by the
*  fact that we just didn't have access to compute, enough compute. Not enough memory, not enough
*  hard drives. Exactly. Not enough compute, not enough storage. So think of these choices. So one of
*  the choices is focusing on single images rather than video. Okay. Clear question, storage and compute.
*  We had to focus on, we used to detect edges and throw away the image. So you have an image,
*  which I say 256 by 256 pixels, and instead of keeping around the grayscale value,
*  what we did was we detected edges, find the places where the brightness changes a lot,
*  so now that's, and now, and then throw away the rest. So this was a major compression device.
*  And the hope was that this makes it, that you can still work with it. And the logic was
*  humans can interpret a line drawing. And yes, and this will save us a competition.
*  So many of the choices were dictated by that. I think today we are no longer detecting edges,
*  we process images with coordinates because we don't need to, we don't have those compute
*  restrictions anymore. Now video is still understudied because video compute is still
*  quite challenging if you are a university researcher. I think video computing is not
*  so challenging if you are at Google or Facebook or Amazon. Still super challenging. I just spoke
*  with the VP of engineering, Google, head of the YouTube search and discovery, and they still
*  struggle doing stuff on video. It's very difficult except using techniques that are essentially the
*  techniques you use in the 90s, some very basic computer vision techniques. No, that's when you
*  want to do things at scale. So if you want to operate at the scale of all the content of
*  YouTube, it's very challenging and there are similar issues in Facebook. But as a researcher,
*  you have more opportunities. You can train large, and that works with relatively large
*  video data sets. Yes. So I think that this is part of the reason why we have so emphasized
*  static images. I think that this is changing and over the next few years, I see a lot more progress
*  happening in video. So I have this generic statement that to me, video recognition feels
*  like 10 years behind object recognition. And you can quantify that because you can take some of the
*  challenging video data sets and their performance on action classification is like say 30%,
*  which is kind of what we used to have around 2009 in object detection. It's like about 10 years
*  behind. And whether it'll take 10 years to catch up is a different question. Hopefully, it will take
*  less than that. Let me ask a similar question I've already asked, but once again, so for dynamic
*  scenes, do you think some kind of injection of knowledge bases and reasoning is required
*  to help improve action recognition? If we solve the general action recognition problem,
*  what do you think the solution would look like? That's another way to put it. Yeah. So I completely
*  agree that knowledge is called for and that knowledge can be quite sophisticated. So the way
*  I would say it is that perception blends into cognition. And cognition brings in issues of
*  memory and this notion of a schema from psychology, which is, let me use the classic example, which is
*  you go to a restaurant, right? Now there are things that happen in a certain order. You walk in,
*  somebody takes you to a table, waiter comes, gives you a menu, takes the order, food arrives,
*  eventually bill arrives, et cetera, et cetera. This is a classic example of AI from the 1970s.
*  It was called, there was the term frames and scripts and schemas. These are all quite similar
*  ideas. Okay. And in the 70s, the way the AI of the time dealt with it was by hand coding this.
*  So they hand coded in this notion of a script and the various stages and the actors and so on and so
*  forth. And use that to interpret, for example, language. I mean, if there's a description of a
*  story involving some people eating at a restaurant, there are all these inferences you can make
*  because you know what happens typically at a restaurant. So I think this kind of knowledge
*  is absolutely essential. So I think that when we are going to do long form video understanding,
*  we are going to need to do this. I think the kinds of technology that we have right now with
*  3D convolutions over a couple of seconds of clip or video, it's very much tailored to us
*  short term video understanding, not that long term understanding. Long term understanding requires
*  this notion of schemas that I talked about, perhaps some notions of goals, intentionality,
*  functionality, and so on and so forth. Now, how will we bring that in? So we could either
*  revert back to the 70s and say, okay, I'm going to hand code in a script, or we might try to learn
*  it. So I tend to believe that we have to find learning ways of doing this, because I think
*  learning ways land up being more robust. And there must be a learning version of the story because
*  children acquire a lot of this knowledge by observation. So at no moment in a child's life
*  it's possible, but I think it's not so typical that somebody that a mother coaches a child through
*  all the stages of what happens in a restaurant. They just go as a family, they go to the restaurant,
*  they eat, come back, and the child goes through 10 such experiences, and the child has
*  got a schema of what happens when you go to a restaurant. So we somehow need to provide
*  that capability to our systems. You mentioned the following line from the end of the Alan Turing
*  paper, Computing Machinery and Intelligence, that many people, like you said, many people know and
*  very few have read, where he proposes the Turing test. This is how you know because it's towards
*  the end of the paper. Instead of trying to produce a program to simulate the adult mind,
*  why not rather try to produce one which simulates the child's? So that's a really interesting point.
*  If I think about the benchmarks we have before us, the tests of our computer vision systems,
*  they're often trying to get to the adult. What kind of benchmarks should we have? What kind of
*  tests for computer vision do you think we should have that mimic the child's in computer vision?
*  Yeah. I think we should have those and we don't have those today. I think part of the challenge
*  is that we should really be collecting data of the type that a child experiences.
*  That gets into issues of privacy and so on and so forth. But there are attempts in this direction
*  to try to collect the kind of data that a child encounters growing up. What's the child's linguistic
*  environment? What's the child's visual environment? If we could collect that kind of data
*  and then develop learning schemes based on that data, that would be one way to do it.
*  I think that's a very promising direction myself. There might be people who would argue that we
*  could just short circuit this in some way. Sometimes we have imitated, we have had success
*  by not imitating nature in detail. The usual example is airplanes. We don't build flapping wings.
*  So yes, that's one of the points of debate. In my mind, I would bet on this learning
*  like a child approach. So one of the fundamental aspects of learning like a child is the
*  interactivity. So the child gets to play with the data set it's learning from. Yes. It gets to select.
*  You can call that active learning. In the machine learning world, you can call it a lot of terms.
*  What are your thoughts about this whole space of being able to play with the data set or select
*  what you're learning? Yeah. So I think that I believe in that. And I think that we could
*  achieve it in two ways. And I think we should use both. So one is actually real robotics.
*  So real physical embodiments of agents who are interacting with the world and they have a physical
*  body with dynamics and mass and moment of inertia and friction and all the rest. And you learn your
*  body. The robot learns its body by doing a series of actions. The second is that simulation
*  environments. So I think simulation environments are getting much, much better. In my life,
*  in Facebook AI research, our group has worked on something called Habitat, which is a simulation
*  environment, which is a visually photorealistic environment of places like houses or interiors of
*  various urban spaces and so forth. And as you move, you get a picture, which is a pretty accurate
*  picture. So now you can imagine that subsequent generations of these simulators will be accurate,
*  not just visually, but with respect to forces and masses and haptic interactions and so on.
*  And then we have that environment to play with. Let me state one reason why I think this active,
*  being able to act in the world is important. I think that this is one way to break the
*  correlation versus causation barrier. So this is something which is of a great deal of interest
*  these days. People like Judea Pearl have talked a lot about that we are neglecting causality, and he
*  describes the entire set of successes of deep learning as just curve fitting. But I don't quite
*  agree. He's a troublemaker. Causality is important, but causality is not like a single silver bullet.
*  It's not like one single principle. There are many different aspects here.
*  And one of the ways in which, one of our most reliable ways of establishing causal links,
*  and this is the way, for example, the medical community does this, is randomized control trials.
*  So you pick some situation, and now in some situation you perform an action, and for certain
*  others you don't. So you have a controlled experiment. Well, the child is in fact performing
*  controlled experiments all the time. Small scale.
*  And in a small scale. But that is a way that the child gets to build and refine its causal models
*  of the world. And my colleague, Alison Gopnik, together with a couple of co-authors, has this
*  book called The Scientist in the Crib, referring to his children. So the part that I like about
*  that is the scientist wants to build causal models, and the scientist does control experiments.
*  And I think the child is doing that. So to enable that, we will need to have these
*  active experiments. And I think this could be done, some in the real world and some in simulation.
*  So you have hope for simulation. I have hope for simulation.
*  That's an exciting possibility if we can get to not just photorealistic, but
*  what's that called? Life realistic simulation. So you don't see any fundamental
*  blocks to why we can't eventually simulate the principles of what it means to exist in the world.
*  I don't see any fundamental problems. Look, the computer graphics community has come along
*  way. So in the early days, going back to the 80s and 90s, they were focusing on visual realism.
*  And then they could do the easy stuff, but they couldn't do stuff like hair or fur and so on.
*  Okay, well, they managed to do that. Then they couldn't do physical actions. Like there's a
*  bowl of glass and it falls down and it shatters. But then they could start to do pretty realistic
*  models of that and so on and so forth. So the graphics people have shown that they can do
*  this forward direction, not just for optical interactions, but also for physical interactions.
*  So I think, of course, some of that is very compute intensive, but I think by and by,
*  we will find ways of making our models ever more realistic.
*  You break vision apart into in one of your presentations, early vision, static scene
*  understanding, dynamics and understanding, and raise a few interesting questions. I thought I
*  could just throw some at you to see if you want to talk about them. So early vision, so it's,
*  what is it that you said? Sensation, perception and cognition. So is this a sensation?
*  Yes.
*  Okay. What can we learn from image statistics that we don't already know? So at the lowest level,
*  what can we make from just the statistics, the basics, the variations in the rock pixels,
*  the textures and so on? Yeah, so what we seem to have learned is
*  that there's a lot of redundancy in these images, and as a result, we are able to do a lot of
*  compression. And this compression is very important in biological settings, right? So you might have
*  10 to the eight photoreceptors and only 10 to the six fibers in the optic nerve. So you have to do
*  this compression by a factor of 100 is to one. And so there are analogs of that which are happening
*  in our artificial neural network. At the early layers. So you think there's a lot of compression
*  that can be done in the beginning, just the statistics. How much?
*  Well, the way to think about it is just how successful is image compression.
*  That's been done with older technologies, but it can be done with several companies which are trying
*  to use these more advanced neural network type techniques for compression, both for static images
*  as well as for video. One of my former students has a company which is trying to do
*  stuff like this. And I think that they are showing quite interesting results. And I think that that's
*  all the success of that's really about image statistics and video statistics. But that's still
*  not doing compression of the kind when I see a picture of a cat. All I have to say is it's a cat.
*  That's another semantic kind of compression. Yeah. So this is at the lower level, right? So
*  as I said, yeah, that's focusing on low level statistics. So to linger on that for a little bit,
*  you mentioned how far can bottom-up image segmentation go? And in general,
*  you mentioned that the central question for scene understanding is the interplay of bottom-up and
*  top-down information. Maybe this is a good time to elaborate on that, maybe define what is
*  bottom-up or top-down in the context of computer vision.
*  Right. So today what we have are very interesting systems because they were completely bottom-up.
*  What does bottom-up mean, sorry? So bottom-up means, in this case,
*  means a feed-forward neural network. So starting from the raw pixels?
*  They start from the raw pixels and they end up with something like cat or not a cat.
*  So our systems are running totally feed-forward. They're trained in a very top-down way.
*  So they're trained by saying, okay, this is a cat, this is a cat, this is a dog, this is a zebra,
*  etc. And I'm not happy with either of these choices fully. We have gone into, because we have
*  completely separated these processes. So I would like the process,
*  so what do we know compared to biology? So in biology, what we know is that the processes
*  at test time, at runtime, those processes are not purely feed-forward, but they involve feedback.
*  So and they involve much shallower neural networks. So the kinds of neural networks
*  we are using in computer vision, say a ResNet 50 has 50 layers. Well, in the brain,
*  in the visual cortex going from the retina to IT, maybe we have like seven. Right. So they're far
*  shallower, but we have the possibility of feedback. So there are backward connections.
*  And this might enable us to deal with the more ambiguous stimuli, for example. So the biological
*  solution seems to involve feedback. The solution in artificial vision seems to be just feed-forward,
*  but with a much deeper network. And the two are functionally equivalent, because if you have a
*  feedback network, which just has like three rounds of feedback, you can just unroll it and make it
*  three times the depth and create it in a totally feed-forward way. So this is something which,
*  I mean, we have written some papers on this theme, but I really feel that this should, this theme
*  should be pursued further. Some kind of recurrence mechanisms. Yeah. Okay. The other, so that's,
*  so I want to have a little bit more top-down in the, at test time. Okay. Then at training time,
*  we make use of a lot of top-down knowledge right now. So basically to learn to segment an object,
*  we have to have all these examples of this is the boundary of a cat, and this is the boundary of a
*  chair, and this is the boundary of a horse, and so on. And this is too much top-down knowledge.
*  How do humans do this? We manage to, we manage with far less supervision, and we do it in a
*  sort of bottom-up way, because for example, we're looking at a video stream and the horse moves,
*  and that enables me to say that all these pixels are together. Yeah. So the gastro-psychologist
*  used to call this the principle of common fate. So there was a bottom-up process by which we were
*  able to segment out these objects, and we have totally focused on this top-down training signal.
*  So in my view, we have currently solved it in machine vision, this top-down bottom-up interaction,
*  but I don't find the solution fully satisfactory, and I would rather have a bit of both in,
*  at both stages. For all computer vision problems, not just segmentation.
*  And the question that you can ask is, so for me, I'm inspired a lot by human vision,
*  and I care about that. You could be just a hard-boiled engineer, not give a damn.
*  So to you, I would then argue that you would need far less training data if you could make my
*  research agenda fruitful. Okay. So then maybe taking a step into segmentation, static scene
*  understanding, what is the interaction between segmentation and recognition? You mentioned
*  the movement of objects. So for people who don't know computer vision, segmentation is this weird
*  activity that computer vision folks have all agreed is very important, of drawing outlines around
*  objects versus a bounding box, and then classifying that object. What's the value
*  of segmentation? What is it as a problem in computer vision? How is it fundamentally different
*  from detection, recognition, and the other problems? Yeah. So I think, so segmentation
*  enables us to say that some set of pixels are an object without necessarily even being able to
*  name that object or knowing properties of that object. Oh, so you mean segmentation purely as
*  the act of separating an object- From its background.
*  A blob of, that's united in some way from its background.
*  Yeah. So, entitification, if you will, making an entity out of it.
*  Entitification, beautifully. So I think that we have that capability,
*  and that enables us to, as we are growing up, to acquire names of objects with very little
*  supervision. So suppose the child, let's posit that the child has this ability to separate out
*  objects in the world. Then when the mother says, pick up your bottle, or the cat's behaving funny
*  today. The word cat suggests some object, and then the child sort of does the mapping.
*  The mother doesn't have to teach specific object labels by pointing to them.
*  Weak supervision works in the context that you have the ability to create objects.
*  So I think that, to me, that's a very fundamental capability. There are applications where this is
*  very important. For example, medical diagnosis. So in medical diagnosis, you have some brain scan.
*  I mean, this is some work that we did in my group where you have CT scans of people with
*  traumatic brain injury. And what the radiologist needs to do is to precisely delineate various
*  places where there might be bleeds, for example. And there are clear needs like that. So there's
*  certainly very practical applications of computer vision where segmentation is necessary.
*  But philosophically, segmentation enables the task of recognition
*  to proceed with much weaker supervision than we require today.
*  And you think of segmentation as this kind of task that takes on a visual scene and breaks it apart
*  into interesting entities that might be useful for whatever the task is.
*  Yeah. And it is not semantics-free. So I think it blends into, it involves perception and cognition.
*  I think the mistake that we used to make in the early days of computer vision was to treat it as
*  a purely bottom-up perceptual task. It is not just that. Because we do revise our notion of
*  segmentation with more experience. Because, for example, there are objects which are non-rigid,
*  like animals or humans. And I think understanding that all the pixels of a human are one entity is
*  actually quite a challenge. Because the parts of the human, they can move independently.
*  The human wears clothes, so they might be differently colored. So it's all sort of a challenge.
*  You mentioned the three Rs of computer vision are recognition, reconstruction, and reorganization.
*  Can you describe these three Rs and how they interact?
*  Yeah. So recognition is the easiest one, because that's what I think people generally think of as
*  computer vision achieving these days, which is labels. So is this a cat? Is this a dog? Is this
*  a chihuahua? I mean, it could be very fine-grained, like a specific breed of a dog,
*  or a specific species of bird, or it could be very abstract, like animal.
*  But given a part of an image or a whole image, say, put a label on that.
*  Yeah. So that's recognition. Reconstruction is essentially,
*  you can think of it as inverse graphics. I mean, that's one way to think about it.
*  So graphics is you have some internal computer representation, and you have a computer
*  representation of some objects arranged in a scene. And what you do is you produce a picture.
*  You produce the pixels corresponding to a rendering of that scene.
*  So let's do the inverse of this. We are given an image, and we say,
*  oh, this image arises from some objects in a scene looked at with a camera from this viewpoint.
*  And we might have more information about the objects, like their shape, maybe their textures,
*  maybe color, et cetera, et cetera. So that's the reconstruction.
*  In a way, you are in your head creating a model of the external world.
*  Okay. Reorganization is to do with essentially finding these entities.
*  So it's organization. The word organization implies structure.
*  So in psychology, we use the term perceptual organization.
*  An image is not just internally represented as just a collection of pixels, but we
*  make these entities. We create these entities, objects, whatever you want to call them.
*  And the relationship between the entities as well, or is it purely about the entities?
*  It could be about the relationships, but mainly we focus on the fact that there are entities.
*  I'm trying to pinpoint what the organization means.
*  So organization is that instead of like a uniform grid, we have this structure of objects.
*  So segmentation is a small part of that.
*  So segmentation gets us going towards that.
*  Yeah. And you kind of have this triangle where they all interact together.
*  Yes.
*  So how do you see that interaction in sort of reorganization? Is yes,
*  defining the entities in the world, the recognition is labeling those entities,
*  and then reconstruction is what, filling in the gaps?
*  Well, to, for example, see, impute some 3D objects corresponding to each of these entities.
*  That would be part of it.
*  So adding more information that's not there in the raw data.
*  Correct. I mean, I started pushing this kind of a view in around 2010 or something like that,
*  because at that time in computer vision, the distinction that people were just working on
*  many different problems, but they treated each of them as a separate isolated problem,
*  with each with its own data set, and then you try to solve that and get good numbers on it.
*  So I didn't like that approach because I wanted to see the connection between these.
*  And if people divided up vision into various modules, the way they would do it is as low-level,
*  mid-level, and high-level vision, corresponding roughly to the psychologist's notion of sensation,
*  perception, and cognition. And that didn't map to tasks that people cared about.
*  So therefore, I tried to promote this particular framework as a way of considering the problems
*  that people in computer vision were actually working on and trying to be more explicit about
*  the fact that they actually are connected to each other. And I was at that time just doing this on
*  the basis of information flow. Now it turns out in the last five years or so, in the post the deep
*  learning revolution, that this architecture has turned out to be very conducive to that.
*  Because basically in these neural networks, we are trying to build multiple representations.
*  There can be multiple output heads sharing common representations.
*  So in a certain sense, today, given the reality of what solutions people have to these,
*  I do not need to preach this anymore. It is just there. It's part of the solution space.
*  So speaking of neural networks, how much of this problem of computer vision, of reorganization,
*  recognition, can be reconstruction, how much of it can be learned end to end, do you think?
*  Sort of set it and forget it. Just plug and play, have a giant data set, multiple perhaps,
*  multimodal, and then just learn the entirety of it.
*  Well, so I think that currently what that end to end learning means nowadays is end to end supervised
*  learning. And that I would argue is too narrow a view of the problem. I would
*  like this child development view, this lifelong learning view, one where there are certain
*  capabilities that are built up and then there are certain capabilities which are built up
*  on top of that. So that's what I believe in. So I think end to end learning in the supervised setting,
*  for a very precise task to me, is sort of a limited view of the learning process.
*  Got it. So if we think about beyond purely supervised, look back to children. You mentioned
*  six lessons that we can learn from children of be multimodal, be incremental, be multi-modal,
*  be incremental, be physical, explore, be social, use language. Can you speak to these perhaps,
*  picking one that you find most fundamental to our time today?
*  Yeah. So I mean, I should say to give due credit, this is from a paper by Smith and Gasser.
*  And it reflects essentially, I would say, common wisdom among
*  child development people. It's just that this is not common wisdom among people in computer vision
*  and AI and machine learning. So I view my role as trying to bridge the two worlds.
*  So let's take an example of a multimodal. I like that. So multimodal, a canonical example is
*  a child interacting with an object. So then the child holds a ball and plays with it.
*  So at that point, it's getting a touch signal. So the touch signal is getting
*  the notion of 3D shape, but it is sparse. And then the child is also seeing a visual signal.
*  So imagine these are two in totally different spaces. So one is the space of receptors on the
*  skin of the fingers and the thumb and the palm. And then these neuronal fibers are getting activated
*  somewhere. These lead to some activation in somatosensory cortex. I mean, a similar thing
*  will happen if we have a robot hand. And then we have the pixels corresponding to the visual view,
*  but we know that they correspond to the same object. So that's a very, very strong cross
*  calibration signal. And it is self-supervisory, which is beautiful. There's nobody assigning a
*  label. The mother doesn't have to come and assign a label. The child doesn't even have to know that
*  this object is called a ball. But the child is learning something about the three-dimensional world
*  from this signal. I think tactile and visual, there is some work on. There is a lot of work
*  currently on audio and visual. And audio-visual, so there is some event that happens in the world,
*  and that event has a visual signature and it has an auditory signature. So there is this glass bowl
*  on the table and it falls and breaks and I hear the smashing sound and I see the pieces of glass.
*  Okay, I've built that connection between the two.
*  This has become a hot topic in computer vision in the last couple of years. There are problems like
*  separating out multiple speakers, which was a classic problem in audition. They call this
*  the problem of source separation or the cocktail party effect and so on. But just try to do it
*  visually. It becomes so much easier and so much more useful. There's so much more signal
*  with multimodal and you can use that for some kind of weak supervision as well.
*  Yes, because they are occurring at the same time in time. So you have time, which links the two.
*  So at a certain moment, T1, you've got a certain signal in the auditory domain and a certain
*  signal in the visual domain. But they must be causally related. Yeah, that's an exciting area.
*  Not well studied yet. Yeah, I mean, we have a little bit of work at this, but so much more needs
*  to be done. So this is a good example. Be physical, that's to do with like the one thing we talked
*  about earlier, that there's an embodied world. To mention language, use language. So Noam Chomsky
*  believes that language may be at the core of cognition, at the core of everything in the human
*  mind. What is the connection between language and vision to you? What's more fundamental? Are they
*  neighbors? Is one the parent and the child, the chicken and the egg? Oh, it's very clear. It is
*  vision, which is the parent, which is the fundamental ability. Okay. So it comes before
*  you think vision is more fundamental than language. Correct. And you can think of it either in
*  phylogeny or in ontogeny. So phylogeny means if you look at evolutionary time, right, so we have
*  vision that developed 500 million years ago. Okay. Then something like when we get to maybe
*  like 5 million years ago, you have the first bipedal primate. So when we started to walk,
*  then the hands became free. And so then manipulation, the ability to manipulate objects
*  and build tools and so on and so forth. So you said 500,000 years ago? No, sorry. The first
*  multicellular animals, which you can say had some intelligence arose 500 million years ago.
*  Okay. And now let's fast forward to say the last 7 million years, which is the development of the
*  hominid line, right? Where from the other primates, we have the branch which leads on to modern humans.
*  Now there are many of these hominids, but the ones which, you know, people talk about Lucy,
*  because that's like a skeleton from 3 million years ago and we know that Lucy walked. Okay. So
*  at this stage, you have that the hand is free for manipulating objects. And then the ability
*  to manipulate objects, build tools and the brain size grew in this era. So, okay, so now you have
*  manipulation. Now we don't know exactly when language arose. But after that. But after that.
*  Because no apes have, I mean, so, I mean Chomsky is correct in that, that it is a uniquely human
*  capability and we primates, other primates don't have that. But so it developed somewhere in this
*  era, but it developed, I would, I mean, argue that it probably developed after we had this stage of
*  humans. I mean, the human species already able to manipulate and hands free, much bigger brain size.
*  And for that, there's a lot of vision has already had, had to have developed.
*  Yeah. So the sensation and the perception may be some of the cognition.
*  Yeah. So we, we, so those, so, so that, so the world, so there, so, so these ancestors of us,
*  you know, three, four million years ago, they had, they had spatial intelligence. So they knew that
*  the world consists of objects. They knew that the objects were in certain relationships to each
*  other. They had observed causal interactions among objects. They could move in space. So they had
*  space and time and all of that. So language builds on that substrate. So language has a lot of,
*  I mean, I mean, the, none of all human languages have constructs which depend on a notion of space
*  and time. Where did that notion of space and time come from? It had to come from perception
*  and action in the world we live in. Yeah. Well, you've referred to the spatial intelligence.
*  Yeah. Yeah. So to linger a little bit, we'll mention Turing and his mention of,
*  we should learn from children. Nevertheless, language is the fundamental piece of the test
*  of intelligence that Turing proposed. What do you think is a good test of intelligence? Are you,
*  what would impress the heck out of you? Is it fundamentally natural language or is there
*  something in vision? I think I wouldn't, I don't think we should have create a single test of
*  intelligence. So just like I don't believe in IQ as a single number, I think generally there can
*  be many capabilities which are correlated perhaps. So I think that there will be,
*  there will be accomplishments which are visual accomplishments, accomplishments which are
*  accomplishments in manipulation or robotics and then accomplishments in language. I do believe
*  that language will be the hardest nut to crack. Really? Yeah. So what's harder to pass the spirit
*  of the Turing test? Like whatever formulation will make it natural language, convincingly a
*  natural language, like somebody you would want to have a beer with, hang out and have a chat with
*  or the general natural scene understanding. You think language is the top of the problem?
*  I think, I'm not a fan of the, I think, I think Turing test that Turing as he proposed the test
*  in 1950 was trying to solve a certain problem. Yeah, imitation. Yeah. And I think it made a lot
*  of sense then. Where we are today, 70 years later, I think, I think we should not worry about that.
*  I mean, I think the Turing test is no longer the right way to channel research in AI because that
*  it takes us down this path of this chat bot which can fool us for five minutes or whatever.
*  Okay. I think I would rather have a list of 10 different tasks. I mean, I think there are tasks
*  which, they're tasks in the manipulation domain, tasks in navigation, tasks in visual scene
*  understanding, tasks in under reading a story and answering questions based on that. I mean,
*  so my favorite language understanding task would be reading a novel and being able to answer
*  arbitrary questions from it. Okay. Right. I think that to me, and this is not an exhausted list by
*  any means, so I would, I think that that's what we need to be going to and each of these, on each of
*  these axes there's a fair amount of work to be done. So on the visual understanding side, in this
*  Intelligence Olympics that we've set up, what's a good test for one of many of visual scene
*  understanding? Do you think such benchmarks exist? Sorry to interrupt. No, there aren't any. I think,
*  I think essentially to me, a really good aid to the blind. So suppose there was a blind person
*  and I needed to assist the blind person. So ultimately, like we said, vision that aids
*  in the action in the survival in this world. Yeah. Maybe in a simulated world.
*  Maybe easier to measure performance in a simulated world. What we are ultimately
*  after is performance in the real world. So David Hilbert in 1900 proposed 23 open problems in
*  mathematics, some of which are still unsolved. Most important, famous of which is probably the
*  Riemann hypothesis. You've thought about and presented about the Hilbert problems of computer
*  vision. So let me ask what do you today, I don't know when the last year you presented that,
*  2015, but versions of it, you're kind of the face and the spokesperson for computer vision.
*  It's your job to state what the open problems are for the field.
*  So what today are the Hilbert problems of computer vision, do you think?
*  Let me pick one which I regard as clearly unsolved, which is what I would call long
*  form video understanding. So we have a video clip and we want to understand
*  the behavior in there in terms of agents, their goals, intentionality,
*  and make predictions about what might happen. So that kind of understanding which goes away from
*  atomic visual action. So in the short range, the question is, are you sitting, are you standing,
*  are you catching a ball? That we can do now. Even if we can't do it fully accurately, if we can do
*  it at 50%, maybe next year we'll do it at 65% and so forth. But I think the long range video
*  understanding, I don't think we can do today. And that means so long-
*  And it blends into cognition. That's the reason why it's challenging.
*  And so you have to track, you have to understand the entities, you have to understand the entities,
*  you have to track them, and you have to have some kind of model of their behavior.
*  Correct. And their behavior might be, these are agents, so they are not just passive objects,
*  but they're agents, so therefore they would exhibit goal-directed behavior.
*  Okay, so this is one area. Then I will talk about understanding the world in 3D. Now this may seem
*  paradoxical because in a way we have been able to do 3D understanding even like 30 years ago,
*  right? But I don't think we currently have the richness of 3D understanding in our computer
*  vision system that we would like. Because, so let me elaborate on that a bit. So currently,
*  we have two kinds of techniques which are not fully unified. So they are the kinds of techniques
*  from multi-view geometry, that you have multiple pictures of a scene and you do a
*  reconstruction using stereoscopic vision or structure for motion. But these techniques
*  do not, they totally fail if you just have a single view, because they are relying on this
*  Okay, then we have some techniques that we have developed in the computer vision community which
*  try to guess 3D from single views. And these techniques are based on supervised learning
*  and they are based on having at training time 3D models of objects available. And this is
*  completely unnatural supervision, right? So, we have a single view, and we have a single view
*  of natural supervision, right? That's not, CAD models are not injected into your brain.
*  Okay, so what would I like? What I would like would be a kind of
*  learning as you move around the world notion of 3D. So we have our
*  a succession of visual experiences. And from those, we, so in as part of that, I might see a chair
*  from different viewpoints, or a table from viewpoint, different viewpoints and so on.
*  Now as part that enables me to build some internal representation. And then next time, I just see a
*  single photograph. And it may not even be of that chair, it's of some other chair.
*  And I have a guess of what its 3D shape is like. So you're almost learning the CAD model, kind of?
*  Yeah, implicitly. I mean, implicitly. I mean, the CAD model need not be in the same form as
*  used by computer graphics programs. Hidden in the representation. It's hidden in the representation,
*  the ability to predict new views. And what I would see if I went to such and such position.
*  By the way, on a small tangent on that, are you okay or comfortable with neural networks that
*  do achieve visual understanding, that do, for example, achieve this kind of 3D understanding,
*  and you don't know how they, you don't know the rep, you're not able to interest, but you're not
*  able to visualize or understand or interact with the representation. So the fact that they're not,
*  or may not be explainable. Yeah, I think that's fine. To me, that is, so let me put some caveats
*  on that. So it depends on the setting. So first of all, I think the, humans are not explainable.
*  So that's a really good point. So we, one human to another human is not fully explainable.
*  I think there are settings where explainability matters. And these might be, for example,
*  questions on medical diagnosis. So I'm in a setting where maybe the doctor, maybe a computer
*  program has made a certain diagnosis. And then depending on the diagnosis, perhaps I should have
*  treatment A or treatment B. Right? So now is the computer program's diagnosis based on data,
*  which was data collected off for American males who are in their 30s and 40s, and maybe not so
*  relevant to me, maybe it is relevant, you know, et cetera, et cetera. And I mean, in medical
*  diagnosis, we have major issues to do with the reference class. So we may have acquired
*  statistics from one group of people and applying it to a different group of people who may not
*  share all the same characteristics. The data might have, there might be error bars in the prediction.
*  So that prediction should really be taken with a huge grain of salt. And, but this has an impact
*  on what treatments should be picked. Right? So there are settings where I want to know more than
*  just this is the answer. But what I acknowledge is that, so in that sense, explainability and
*  interpretability may matter. It's about giving error bounds and a better sense of the quality
*  of the decision. Where I'm willing to sacrifice interpretability is that I believe that there
*  can be systems which can be highly performant, but which are internally black boxes.
*  And that seems to be where it's headed. Some of the best performing systems are essentially black
*  boxes. Yeah. Fundamentally by their construction. But you and I are black boxes to each other.
*  Yeah. So the nice thing about the black boxes we are is so we ourselves are black boxes,
*  but we're also the, those of us who are charming are able to convince others, like explain the black,
*  what's going on inside the black box with narratives, the stories. So in some sense,
*  neural networks don't have to actually explain what's going on inside. They just have to come
*  up with stories, real or fake, that convince you that they know what's going on.
*  And I'm sure we can do that. We can create those stories. Neural networks can create those stories.
*  Yeah. And the transformer will be involved. Do you think we will ever
*  build a system of human level or superhuman level intelligence? We've kind of defined what it takes
*  to try to approach that. But do you think that's within our reach? The thing that we thought we
*  could do, what Turing thought actually we could do by year 2000, right? What do you think we'll
*  ever be able to do? Yeah. So I think there are two answers here. One answer is in principle,
*  can we do this at some time? And my answer is yes. The second answer is a pragmatic one. Do you think
*  we will be able to do it in the next 20 years or whatever? And to that man says no.
*  So of course that's a wild guess. I think that Donald Rumsfeld is not a favorite person of mine,
*  but one of his lines is very good, which is about known knowns, known unknowns, and unknown unknowns.
*  So in the business we are in, there are known unknowns and we have unknown unknowns.
*  So I think with respect to a lot of what's the case in vision and robotics, I feel like
*  we have known unknowns. So I have a sense of where we need to go and what the problems that need to
*  be solved are. I feel with respect to natural language, understanding, and high level cognition,
*  it's not just known unknowns, but also unknown unknowns. So it is very difficult to put any kind
*  of a time frame to that. Do you think some of the unknown unknowns might be positive in that they'll
*  surprise us and make the job much easier? So fundamental breakthroughs? I think that is
*  possible because certainly I have been very positively surprised by how effective these
*  deep learning systems have been because I certainly would not have believed that in 2010.
*  I think what we knew from the mathematical theory was that convex optimization works.
*  When there's a single global optima, then these gradient descent techniques would work.
*  Now these are nonlinear systems with non-convex systems. Huge number of variables, so over
*  parameterized. Over parameterized. And the people who used to play with them a lot,
*  the ones who are totally immersed in the lore and the black magic, they knew that they worked
*  well even though they were. Really? I thought everybody would-
*  No, the claim that I hear from my friends like Yan LeCun and so forth is-
*  Oh, now, yeah. That they feel that they were comfortable with them.
*  Well, he says that now. But the community as a whole
*  was certainly not. And I think to me that was the surprise that they actually worked robustly
*  for a wide range of problems, from a wide range of initializations and so on.
*  And so that was certainly more rapid progress than we expected. But then there are certainly
*  lots of times, in fact, most of the history of AI is when we have made less progress at a slower
*  rate than we expected. So we just keep going. I think what I regard as really unwarranted are
*  these fears of AGI in 10 years and 20 years and that kind of stuff. Because that's based on
*  completely unrealistic models of how rapidly we will make progress in this field.
*  So I agree with you, but I've also gotten the chance to interact with very smart people who
*  really worry about the existential threats of AI. And I, as an open-minded person, am sort of
*  taking it in. Do you think if AI systems, in some way the unknown unknowns, not super intelligent AI,
*  but in ways we don't quite understand the nature of super intelligence, will have a detrimental
*  effect on society? Do you think this is something we should be worried about or we need to first
*  allow the unknown unknowns to become known unknowns? I think we need to be worried about AI today.
*  I think that it is not just a worry we need to have when we get that AGI. I think that AI is
*  being used in many systems today. And there might be settings, for example, when it causes biases or
*  decisions which could be harmful. I mean, a decision which could be unfair to some people,
*  or it could be a self-driving car which kills a pedestrian. So AI systems are being deployed
*  today, right? And they're being deployed in many different settings, maybe in medical diagnosis,
*  maybe in a self-driving car, maybe in selecting applicants for an interview.
*  So I would argue that when these systems make mistakes, there are consequences. And we are,
*  in a certain sense, responsible for those consequences. So I would argue that this is
*  a continuous effort. And this is something that, in a way, is not so surprising. It's about all
*  engineering and scientific progress, which great power comes great responsibility.
*  So as these systems are deployed, we have to worry about them. And it's a continuous problem.
*  I don't think of it as something which will suddenly happen on some day in 2079,
*  for which I need to design some clever trick. I'm saying that these problems exist today.
*  And we need to be continuously on the lookout for worrying about safety, biases, risks. I mean,
*  self-driving car kills a pedestrian. And they have. I mean, this Uber incident in Arizona,
*  it has happened. This is not about AGI. In fact, it's about a very dumb intelligence,
*  which is still killing people. Well, the worry people have with AGI
*  is the scale. But I think you're 100% right. The thing that worries me about AI today,
*  and it's happening in a huge scale, is recommender system, recommendation systems.
*  So if you look at Twitter or Facebook or YouTube, they're controlling the ideas that we have access
*  to, the news and so on. And that's a fundamental machine learning algorithm behind each of these
*  recommendations. And they, I mean, my life would not be the same without these sources of
*  information. I'm a totally new human being. And the ideas that I know are very much because of
*  the internet, because of the algorithms that recommend those ideas. And so as they get smarter
*  and smarter, I mean, that is the AGI. The algorithm that's recommending the next YouTube video you
*  should watch has control of millions of billions of people. That algorithm is already super
*  intelligent and has complete control of the population. Not a complete, but very strong
*  control. For now, we can turn off YouTube. We can just go have a normal life outside of that. But
*  the more and more that gets into our life, it's that algorithm, we start depending on it in the
*  different companies that are working on the algorithm. So I think it's, you're right. It's
*  already there. And YouTube in particular is using computer vision, doing their hardest to try to
*  understand the content of videos so they could be able to connect videos with the people who
*  would benefit from those videos the most. And so that development could go in a bunch of different
*  directions, some of which might be harmful. So yeah, you're right. The threats of AI are here
*  already. We should be thinking about them. On a philosophical notion, if you could,
*  personal perhaps, if you could relive a moment in your life outside of family,
*  because it made you truly happy or was a profound moment that impacted the direction of your life,
*  what moment would you go to?
*  I don't think of single moments, but I look over the long haul. I feel that I've been very lucky
*  because I feel that I think that in scientific research, a lot of it is about being at the right
*  place at the right time. And you can work on problems at a time when they're just too
*  premature. You know, you butt your head against them and nothing happens because the prerequisites
*  for success are not there. And then there are times when you are in a field which is all pretty
*  mature and you can only solve curlicues upon curlicues.
*  I've been lucky to have been in this field, which for 34 years, well, actually 34 years
*  as a professor at Berkeley, so longer than that, which when I started in it was just like some
*  little crazy, absolutely useless field. Couldn't really do anything to a time when it's really,
*  really solving a lot of practical problems, has offered a lot of tools for scientific research,
*  because computer vision is impactful for images in biology or astronomy and so on and so forth.
*  And we have made great scientific progress, which has had real practical impact in the world.
*  And I feel lucky that I got in at a time when the field was
*  very young and at a time when it is now mature, but not fully mature. It's mature, but not done.
*  I mean, it's really still in a productive phase. Yeah, I think people 500 years from now would laugh
*  at you calling this field mature. Yeah, that is very possible.
*  Yeah. But you're also, lest I forget to mention, you've also mentored some of the biggest
*  names of computer vision, computer science and AI today.
*  There's so many questions I could ask, but it really is, what is it, how did you do it?
*  What does it take to be a good mentor? What does it take to be a good guide?
*  Yeah, I think what I feel, I've been lucky to have had very, very smart and hardworking
*  and creative students. I think some part of the credit just belongs to being at Berkeley.
*  Those of us who are at top universities are blessed because we have very, very smart
*  and capable students coming knocking on our door. So I have to be humble enough to acknowledge that.
*  But what have I added? I think I have added something. What I have added is, I think
*  what I've always tried to teach them is a sense of picking the right problems. So
*  I think that in science, in the short run, success is always based on technical competence.
*  You're quick with math or you are whatever. There's certain technical capabilities which
*  make for short range progress. Long range progress is really determined by asking the
*  right questions and focusing on the right problems. And I feel that what I've been able to
*  bring to the table in terms of advising these students is some sense of taste of what are good
*  problems. What are problems that are worth attacking now as opposed to waiting 10 years?
*  What's a good problem? If you could summarize, is that possible to even summarize? What's
*  your sense of a good problem? I think I have a sense of what is a good problem, which is
*  there is a British scientist, in fact, he won a Nobel Prize, Peter Medever, who has a book on this.
*  And basically, he calls it the research is the art of the soluble. So we need to sort of find
*  problems which are not yet solved, but which are approachable. And he sort of refers to this
*  sense that there is this problem which isn't quite solved yet, but it has a soft underbelly.
*  There is some place where you can, you know, spear the beast. And having that intuition that
*  this problem is ripe is a good thing because otherwise you can just beat your head and not
*  make progress. So I think that is important. So if I have that and if I can convey that to students,
*  it's not just that they do great research while they're working with me, but that they continue
*  to do great research. So in a sense, I'm proud of my students and their achievements and their
*  great research even 20 years after they have ceased being my student. So it's in part helping
*  them develop that sense that a problem is not yet solved, but it's solvable. Correct. The other thing
*  which I have, which I think I bring to the table is a certain intellectual breadth. I
*  spend a fair amount of time studying psychology, neuroscience, relevant areas of applied math,
*  and so forth. So I can probably help them see some connections to disparate things which
*  they might not have otherwise. So the smart students coming into Berkeley can be
*  very deep in the sense, they can think very deeply, meaning very hard down one particular path.
*  But where I could help them is the shallow breadth, but they would have the narrow depth.
*  But that's of some value. Well, it was beautifully refreshing just to hear you
*  naturally jump to psychology back to computer science and this conversation back and forth.
*  That's a rare quality and I think it's certainly for students empowering
*  to think about problems in a new way. So for that and for many other reasons,
*  I really enjoyed this conversation. Thank you so much. It was a huge honor. Thanks for talking to
*  me. It's been my pleasure. Thanks for listening to this conversation with Jitendra Malik and thank
*  you to our sponsors, BetterHelp and ExpressVPN. Please consider supporting this podcast by going
*  to betterhelp.com slash Lex and signing up at expressvpn.com slash Lex pod. Click the links,
*  buy the stuff. It's how they know I sent you and it really is the best way to support this podcast
*  and the journey I'm on. If you enjoy this thing, subscribe on YouTube, review it with five stars
*  on Apple podcast, support it on Patreon or connect with me on Twitter at Lex Friedman. Don't ask me
*  how to spell that. I don't remember it myself. And now let me leave you with some words from
*  Prince Mishkin and the Idiot by Dostoevsky. Beauty will save the world. Thank you for listening
*  and hope to see you next time.
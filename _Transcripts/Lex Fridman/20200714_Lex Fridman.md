---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 5850s
Video Keywords: ['sergey levine', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 99957
Video Rating: None
Video Description: Sergey Levine is a professor at Berkeley and a world-class researcher in deep learning, reinforcement learning, robotics, and computer vision, including the development of algorithms for end-to-end training of neural network policies that combine perception and control, scalable algorithms for inverse reinforcement learning, and deep RL algorithms.

Support this podcast by signing up with these sponsors:
- ExpressVPN at https://www.expressvpn.com/lexpod
- Cash App - use code "LexPodcast" and download:
- Cash App (App Store): https://apple.co/2sPrUHe
- Cash App (Google Play): https://bit.ly/2MlvP5w

EPISODE LINKS:
Sergey's Twitter: https://twitter.com/svlevine
Sergey's Website: http://rail.eecs.berkeley.edu/
Sergey's Papers: https://scholar.google.com/citations?user=8R35rCwAAAAJ

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
3:05 - State-of-the-art robots vs humans
16:13 - Robotics may help us understand intelligence
22:49 - End-to-end learning in robotics
27:01 - Canonical problem in robotics
31:44 - Commonsense reasoning in robotics
34:41 - Can we solve robotics through learning?
44:55 - What is reinforcement learning?
1:06:36 - Tesla Autopilot
1:08:15 - Simulation in reinforcement learning
1:13:46 - Can we learn gravity from data?
1:16:03 - Self-play
1:17:39 - Reward functions
1:27:01 - Bitter lesson by Rich Sutton
1:32:13 - Advice for students interesting in AI
1:33:55 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Sergey Levine Robotics and Machine Learning  Lex Fridman Podcast #108
**Lex Fridman:** [July 14, 2020](https://www.youtube.com/watch?v=kxi-_TT_-Nc)
*  The following is a conversation with Sergey Levine, a professor at Berkeley and a world-class
*  researcher in deep learning, reinforcement learning, robotics, and computer vision,
*  including the development of algorithms for end-to-end training of neural network policies
*  that combine perception and control, scalable algorithms for inverse reinforcement learning,
*  and, in general, deep RL algorithms. Quick summary of the ads. Two sponsors,
*  CashApp and ExpressVPN. Please consider supporting the podcast by downloading CashApp
*  and using code LexPodcast and signing up at expressvpn.com slash LexPod. Click the links,
*  buy the stuff. It's the best way to support this podcast and, in general, the journey I'm on.
*  If you enjoy this thing, subscribe on YouTube, review it with five stars on Apple Podcast,
*  follow on Spotify, support it on Patreon, or connect with me on Twitter at Lex Friedman.
*  As usual, I'll do a few minutes of ads now and never any ads in the middle that can break the
*  flow of the conversation. This show is presented by CashApp, the number one finance app in the
*  app store. When you get it, use code LexPodcast. CashApp lets you send money to friends,
*  buy bitcoin, and invest in the stock market with as little as one dollar. Since CashApp does
*  fractional share trading, let me mention that the order execution algorithm that works behind the
*  scenes to create the abstraction of the fractional orders is an algorithmic marvel. So big props to
*  the CashApp engineers for taking a step up to the next level of abstraction over the stock market,
*  making trading more accessible for new investors and diversification much easier. So again,
*  if you get CashApp from the app store, Google Play, and use the code LexPodcast, you get ten
*  dollars, and CashApp will also donate ten dollars to FIRST, an organization that is helping to
*  advance robotics and STEM education for young people around the world. This show is also sponsored
*  by ExpressVPN. Get it at expressvpm.com slash LexPod to support this podcast and to get an
*  extra three months free on a one-year package. I've been using ExpressVPN for many years.
*  I love it. I think ExpressVPN is the best VPN out there. They told me to say it, but it happens to
*  be true in my humble opinion. It doesn't lock your data. It's crazy fast and it's easy to use,
*  literally just one big power on button. Again, it's probably obvious to you, but I should say it
*  again. It's really important that they don't log your data. It works on Linux and every other
*  operating system, but Linux, of course, is the best operating system. Shout out to my favorite
*  flavor, Ubuntu Mate 2004. Once again, get it at expressvpm.com slash LexPod to support this
*  podcast and to get an extra three months free on a one-year package. And now here's my conversation
*  with Sergey Levine. What's the difference between a state-of-the-art human such as you and I? Well,
*  I don't know if we qualify as state-of-the-art humans, but a state-of-the-art human and a
*  state-of-the-art robot. That's a very interesting question. Robot capability is, it's kind of a,
*  I think it's a very tricky thing to understand because there are some things that are difficult
*  that we wouldn't think are difficult and some things that are easy that we wouldn't think are
*  easy. And there's also a really big gap between capabilities of robots in terms of hardware and
*  their physical capability and capabilities of robots in terms of what they can do autonomously.
*  There is a little video that I think robotics researchers really like to show, especially
*  robotics learning researchers like myself from 2004 from Stanford, which demonstrates a prototype
*  robot called the PR1. And the PR1 was a robot that was designed as a home assistance robot. And
*  there's this beautiful video showing the PR1 tidying up a living room, putting away toys,
*  and at the end bringing a beer to the person sitting on the couch, which looks really amazing.
*  And then the punchline is that this robot is entirely controlled by a person. So you can,
*  so in some ways the gap between a state-of-the-art human and state-of-the-art robot, if the robot has
*  a human brain, is actually not that large. Now, obviously like human bodies are sophisticated and
*  very robust and resilient in many ways, but on the whole, if we're willing to like spend a bit of
*  money and do a bit of engineering, we can kind of close the hardware gap almost. But the intelligence
*  gap, that one is very wide. And when you say hardware, you're referring to the physical sort
*  of the actuators, the actual body of the robot as opposed to the hardware on which the cognition,
*  the hardware of the nervous system. Yes, exactly. I'm referring to the body rather than the mind.
*  So that means that the kind of the work is cut out for us. Like while we can still make the body
*  better, we kind of know that the big bottleneck right now is really the mind. And how big is that
*  gap? How big is the difference in your sense of ability to learn, ability to reason, ability to
*  perceive the world between humans and our best robots? The gap is very large and the gap
*  becomes larger the more unexpected events can happen in the world. So essentially the spectrum
*  along which you can measure the size of that gap is the spectrum of how open the world is.
*  If you control everything in the world very tightly, if you put the robot in like a factory
*  and you tell it where everything is and you rigidly program its motion, then it can do things,
*  one might even say in a superhuman way. It can move faster, it's stronger, it can lift up a car
*  and things like that. But as soon as anything starts to vary in the environment, now it'll trip
*  up. And if many, many things vary like they would like in your kitchen, for example, then things are
*  pretty much like wide open. Now again, we're going to stick a bit on the philosophical questions,
*  but how much on the human side of the cognitive abilities in your sense is nature versus nurture?
*  So how much of it is a product of evolution and how much of it is something we'll learn from sort
*  of scratch from the day we're born? I'm going to read into your question as asking about the
*  implications of this for AI. Of course, exactly.
*  I'm not a biologist, I can't really speak authoritatively about that.
*  So until we go on it, if it's all about learning, then there's more hope for AI.
*  Yeah. So the way that I look at this is that, well, first, of course, biology is very messy.
*  And if you ask the question, how does a person do something or how does a person's mind do something,
*  you can come up with a bunch of hypotheses and oftentimes you can find support for many different
*  often conflicting hypotheses. One way that we can approach the question of what the implications of
*  this for AI are is we can think about what's sufficient. So maybe a person is from birth very,
*  very good at some things like, for example, recognizing faces. There's a very strong
*  evolutionary pressure to do that. If you can recognize your mother's face, then you're more
*  likely to survive and therefore people are good at this. But we can also ask, what's the minimum
*  sufficient thing? And one of the ways that we can study the minimal sufficient thing is we could,
*  for example, see what people do in unusual situations if we present them with things
*  that evolution couldn't have prepared them for. Our daily lives actually do this to us all the
*  time. We didn't evolve to deal with automobiles and space flight and whatever. So there are all
*  these situations that we can find ourselves in and we do very well there. I can give you a
*  joystick to control a robotic arm, which you've never used before. And you might be pretty bad
*  for the first couple of seconds, but if I tell you your life depends on using this robotic arm to
*  open this door, you'll probably manage it. Even though you've never seen this device before,
*  you've never used the joystick control, you'll kind of muddle through it. And that's not your
*  evolved natural ability, that's your flexibility, your adaptability. And that's exactly why our
*  current robotic systems really kind of fall flat. But I wonder how much general, almost what we
*  think of as common sense, pre-trained models underneath all of that. So that ability to adapt
*  to a joystick requires you to have a kind of, you know, I'm human, so it's hard for me to
*  introspect all the knowledge I have about the world. But it seems like there might be an iceberg
*  underneath of the amount of knowledge we actually bring to the table. That's kind of the open
*  question. What's your sense on that? I think there's absolutely an iceberg of knowledge
*  that we bring to the table, but I think it's very likely that iceberg of knowledge is actually built
*  up over our lifetimes. Because we have a lot of prior experience to draw on, and it kind of makes
*  sense that the right way for us to optimize our efficiency, our evolutionary fitness and so on,
*  is to utilize all that experience to build up the best iceberg we can get.
*  While that sounds an awful lot like what machine learning actually does, I think that for modern
*  machine learning, it's actually a really big challenge to take this unstructured massive
*  experience and distill out something that looks like a common sense understanding of the world.
*  And perhaps part of that is not because something about machine learning itself is broken or hard,
*  but because we've been a little too rigid in subscribing to a very supervised, very rigid
*  notion of learning. Kind of the input-output, Xs go to Y sort of model. And maybe what we really
*  need to do is to view the world more as like a massive experience that is not necessarily
*  providing any rigid supervision, but sort of providing many, many instances of things that
*  could be. And then you take that and you distill it into some sort of common sense understanding.
*  I see. Well, you're painting an optimistic, beautiful picture, especially from the robotics
*  perspective, because that means we just need to invest and build better learning algorithms,
*  figure out how we can get access to more and more data for those learning algorithms to extract
*  signal from, and then accumulate that iceberg of knowledge. It's a beautiful picture. It's a
*  hopeful one. I think it's potentially a little bit more than just that. And this is where we
*  perhaps reach the limits of our current understanding. But one thing that I think that
*  the research community hasn't really resolved in a satisfactory way is how much it matters where
*  that experience comes from. Do you just download everything on the internet and cram it into
*  essentially the 21st century analog of the giant language model and see what happens?
*  Or does it actually matter whether your machine physically experiences the world in the sense that
*  it actually attempts things, observes the outcome of its actions, and augments its experience that
*  way? That it chooses which parts of the world it gets to interact with and observe and learn from.
*  Right. It may be that the world is so complex that simply obtaining a large mass of IID samples of
*  the world is a very difficult way to go. But if you are actually interacting with the world and
*  essentially performing this hard negative mining by attempting what you think might work, observing
*  the sometimes happy and sometimes sad outcomes of that, and augmenting your understanding using
*  that experience, and you're just doing this continually for many years, maybe that data
*  in some sense is actually much more favorable to obtaining a common sense understanding.
*  One reason we might think that this is true is that what we associate with common sense or lack
*  of common sense is often characterized by the ability to reason about counterfactual questions.
*  Here I'm this bottle of water sitting on the table. Everything is fine. If I were to knock it over,
*  which I'm not going to do, but if I were to do that, what would happen?
*  And I know that nothing good would happen from that. But if I have a bad understanding of the
*  world, I might think that that's a good way for me to gain more utility. If I actually go about
*  my daily life doing the things that my current understanding of the world suggests will give
*  me high utility, in some ways I'll get exactly the right supervision to tell me not to do those bad
*  things and to keep doing the good things. So there's a spectrum between IID, random walk
*  through the space of data, and then there's what we humans do. I don't even know if we do it optimal,
*  but there might be beyond. So this open question that you raised, where do you think
*  intelligent systems that would be able to deal with this world fall? Can we do pretty well by
*  reading all of Wikipedia, randomly sampling it like language models do? Or do we have to be
*  exceptionally selective and intelligent about which aspects of the world we interact with?
*  So I think this is first an open scientific problem, and I don't have a clear answer,
*  but I can speculate a little bit. And what I would speculate is that you don't need to be
*  super, super careful. I think it's less about being careful to avoid the useless stuff and
*  more about making sure that you hit on the really important stuff. So perhaps it's okay if you
*  spend part of your day just guided by your curiosity, visiting interesting regions of
*  your state space, but it's important for you to every once in a while make sure that you really
*  try out the solutions that your current model of the world suggests might be effective and
*  observe whether those solutions are working as you expect or not. And perhaps some of that is
*  really essential to have a perpetual improvement loop. This perpetual improvement loop is really
*  the key that's going to potentially distinguish the best current methods from the best methods
*  of tomorrow in a sense. How important do you think is exploration or total out of the box
*  thinking exploration in this space as you jump to totally different domains? So you kind of
*  mentioned there's an optimization problem. You kind of explore the specifics of a particular
*  strategy, whatever the thing you're trying to solve. How important is it to explore totally
*  outside of the strategies that have been working for you so far? What's your intuition there?
*  Yeah, I think it's a very problem dependent kind of question. And I think that that's actually,
*  in some ways that question gets at one of the big differences between the classic formulation of
*  a reinforcement learning problem and some of the more open-ended reformulations of that problem
*  that have been explored in recent years. So classically, reinforcement learning is framed
*  as a problem of maximizing utility like any kind of rational AI agent. And then anything you do is
*  in service to maximizing that utility. But a very interesting kind of way to look at,
*  I'm not necessarily saying this is the best way to look at it, but an interesting alternative way
*  to look at these problems as something where you first get to explore the world however you please
*  and then afterwards you will be tasked with doing something. And that might suggest a somewhat
*  different solution. So if you don't know what you're going to be tasked with doing and you
*  just want to prepare yourself optimally for whatever your uncertain future holds, maybe then you will
*  choose to attain some sort of coverage, build up sort of an arsenal of cognitive tools, if you will,
*  such that later on when someone tells you, now your job is to fetch the coffee for me,
*  you'll be well prepared to undertake that task. And you see that as the modern formulation
*  of the reinforcement learning problem, as the more multi-task, the general intelligence kind
*  of formulation. I think that's one possible vision of where things might be headed. I don't think
*  that's by any means the mainstream or standard way of doing things. And it's not like if I had to.
*  But I like it. It's a beautiful vision. So maybe actually take a step back. What is the goal of
*  robotics? What's the general problem of robotics we're trying to solve? You actually kind of painted
*  two pictures here, one of sort of the narrow, one of the general. What in your view is the big
*  problem of robotics? Again, ridiculously philosophical high level questions.
*  I think that maybe there are two ways I can answer this question. One is there's a very pragmatic
*  problem, which is like, what would make robots, what would sort of maximize the usefulness of
*  robots? And there the answer might be something like a system where, a system that can perform
*  whatever task a human user sets for it, within the physical constraints, of course, if you tell it
*  to teleport to another planet, it probably can't do that. But if you ask it to do something that's
*  within its physical capability, then potentially with a little bit of additional training or a
*  bit of additional trial and error, it ought to be able to figure it out in much the same way as
*  a human teleoperator ought to figure out how to drive the robot to do that. That's kind of the
*  very pragmatic view of what it would take to kind of solve the robotics problem, if you will.
*  But I think that there is a second answer. And that answer is a lot closer to why I want to
*  work on robotics, which is that I think it's less about what it would take to do a really good job
*  in the world of robotics, but more the other way around, what robotics can bring to the table
*  to help us understand artificial intelligence. So your dream fundamentally is to understand
*  intelligence. Yes. I think that's the dream for many people who actually work in this space.
*  I think that there's something very pragmatic and very useful about studying robotics. But I do
*  think that a lot of people that go into this field, actually, the things that they draw
*  inspiration from are the potential for robots to help us learn about intelligence and about ourselves.
*  That's fascinating that robotics is basically the space by which you can get closer to
*  understanding the fundamentals of artificial intelligence. So what is it about robotics
*  that's different from some of the other approaches? So if we look at some of the
*  early breakthroughs in deep learning or in the computer vision space and the natural language
*  processing, there's really nice clean benchmarks that a lot of people competed on and thereby came
*  up with a lot of brilliant ideas. What's the fundamental difference to you between computer
*  vision, purely defined and image net and kind of the bigger robotics problem? So there are a couple
*  of things. One is that with robotics, you kind of have to take away many of the crutches. So
*  you have to deal with both the particular problems of perception, control and so on,
*  but you also have to deal with the integration of those things. Classically, we've always thought
*  of the integration as kind of a separate problem. So a classic kind of modular engineering approach
*  is that we solve the individual subproblems, then wire them together, and then the whole thing works.
*  One of the things that we've been seeing over the last couple of decades is that, well, maybe
*  studying the thing as a whole might lead to just very different solutions than if we were to study
*  the parts and wire them together. So the integrative nature of robotics research helps us see, you know,
*  the different perspectives on the problem. Another part of the answer is that with robotics,
*  it casts a certain paradox into very clever relief. So this is sometimes referred to as a
*  Moravix paradox, the idea that in artificial intelligence, things that are very hard for people
*  can be very easy for machines and vice versa. Things that are very easy for people can be very
*  hard for machines. So, you know, integral and differential calculus is pretty difficult to learn
*  for people, but if you program a computer, do it, it can derive derivatives and integrals for you
*  all day long without any trouble. Whereas some things like, you know, drinking from a cup of water,
*  they're easy for a person to do, very hard for a robot to deal with. And sometimes when we see such
*  blatant discrepancies, they give us a really strong hint that we're missing something important. So if
*  we really try to zero in on those discrepancies, we might find that little bit that we're missing.
*  And it's not that we need to make machines better or worse at math and better at drinking water,
*  but just that by studying those discrepancies, we might find some new insight.
*  So that could be, that could be in any space. It doesn't have to be robotics, but you're saying,
*  I mean, it's kind of interesting that robotics seems to have a lot of those discrepancies. So the
*  the Hans Marvac paradox is probably referring to the space of the physical interaction. Like you said,
*  object manipulation, walking, all the kind of stuff we do in the physical world.
*  How do you make sense if you were to try to disentangle
*  the Marvac paradox? Like, why is there such a gap in our intuition about it?
*  Why do you think manipulating objects is so hard from everything you've learned
*  from applying reinforcement learning in this space?
*  Yeah, I think that one reason is maybe that for many of the other problems that we've studied in
*  AI and computer science and so on, the notion of input, output and supervision is much, much cleaner.
*  Computer vision, for example, deals with very complex inputs, but it's comparatively a bit
*  easier, at least up to some level of abstraction, to cast it as a very tightly supervised problem.
*  It's comparatively much, much harder to cast robotic manipulation as a very tightly
*  supervised problem. You can do it, it just doesn't seem to work all that well. So you could say that,
*  well, maybe we get a label data set where we know exactly which motor commands to send and then we
*  train on that, but for various reasons, that's not actually such a great solution.
*  It also doesn't seem to be even remotely similar to how people and animals learn to do things
*  because we're not told by our parents, here's how you fire your muscles in order to walk.
*  We do get some guidance, but the really low-level detailed stuff we figure out mostly on our own.
*  And that's what you mean by tightly coupled, that every single little sub-action gets a supervised
*  signal of whether it's a good one or not.
*  Right. So while in computer vision, you could imagine up to a level of abstraction that maybe
*  somebody told you this is a car and this is a cat and this is a dog. In motor control,
*  it's very clear that that was not the case.
*  If we look at the sub-spaces of robotics, that again, as you said, robotics integrates all of
*  them together and we get to see how this beautiful mess interplays. So there's nevertheless still
*  perception. So it's the computer vision problem, broadly speaking, understanding the environment.
*  Then there's also, maybe you can correct me on this kind of categorization of the space,
*  then there's prediction in trying to anticipate what things are going to do into the future in
*  order for you to be able to act in that world. And then there's also this game theoretic aspect of
*  how your actions will change the behavior of others. In this kind of space, what,
*  and this is bigger than reinforcement learning, this is just broadly looking at the problem of
*  robotics. What's the hardest problem here? Or is there, or is what you said
*  true that when you start to look at all of them together, that's a whole other thing. Like you
*  can't even say which one individually is harder because all of them together,
*  you should only be looking at them all together. I think when you look at them all together,
*  some things actually become easier. And I think that's actually pretty important. So we had,
*  back in 2014, we had some work, basically our first work on end-to-end reinforcement learning
*  for robotic manipulation skills from vision, which at the time was something that seemed a little
*  inflammatory and controversial in the robotics world. But other than the inflammatory and
*  controversial part of it, the point that we were actually trying to make in that work is that for
*  the particular case of combining perception and control, you could actually do better if you treat
*  them together than if you try to separate them. And the way that we tried to demonstrate this is
*  we picked a fairly simple motor control task where a robot had to insert a little red trapezoid into
*  a trapezoidal hole. And we had our separated solution, which involved first detecting the
*  hole using a post detector and then actuating the arm to put it in. And then our end-to-end
*  solution, which just mapped pixels to torques. And one of the things we observed is that if you
*  use the end-to-end solution, essentially the pressure on the perception part of the model
*  is actually lower. It doesn't have to figure out exactly where the thing is in 3D space.
*  It just needs to figure out where it is, distributing the errors in such a way that
*  the horizontal difference matters more than the vertical difference because vertically it just
*  pushes it down all the way until it can't go any further. And their perceptual errors are a lot
*  less harmful. Whereas perpendicular to the direction of motion, perceptual errors are
*  much more harmful. So the point is that if you combine these two things, you can trade off errors
*  between the components optimally to best accomplish the task. And the components can actually be
*  weaker while still leading to better overall performance. It has a profound idea. I mean,
*  in the space of pegs and things like that, it's quite simple. It almost is tempting to overlook.
*  But that seems to be, at least intuitively, an idea that should generalize to basically all
*  aspects of perception and control. Of course. That one strengthens the other.
*  Yeah. And people who have studied perceptual heuristics in humans and animals find things
*  like that all the time. So one very well-known example of this is something called the gaze
*  heuristic, which is a little trick that you can use to intercept a flying object. So if you want
*  to catch a ball, for instance, you could try to localize it in 3D space, estimate its velocity,
*  estimate the effect of wind resistance, solve a complex system of differential equations in your
*  head. Or you can maintain a running speed so that the object stays in the same position as in your
*  field of view. So if it dips a little bit, you speed up. If it rises a little bit, you slow down.
*  And if you follow the simple rule, you'll actually arrive at exactly the place where the object lands
*  and you'll catch it. And humans use it when they play baseball. Human pilots use it when they fly
*  airplanes to figure out if they're about to collide with somebody. Frogs use this to catch
*  insects and so on and so on. So this is something that actually happens in nature. And I'm sure this
*  is just one instance of it that we were able to identify just because all the scientists were
*  able to identify because it's so prevalent, but there are probably many others. Do you have a,
*  just so we can zoom in as we talk about robotics, do you have a canonical problem, sort of a simple,
*  clean, beautiful representative problem in robotics that you think about when you're
*  thinking about some of these problems? We talked about robotic manipulation. To me, that seems
*  intuitively, at least the robotics community has converged towards that as a space. That's the
*  canonical problem. If you agree, then maybe do you zoom in in some particular aspect of that problem
*  that you just like? If we solve that problem perfectly, it'll unlock a major step
*  towards human level intelligence. I don't think I have a really great answer to that. And I think
*  partly the reason I don't have a great answer kind of has to do with the, it has to do with the fact
*  that the difficulty is really in the flexibility and adaptability rather than in doing a particular
*  thing really, really well. So it's hard to just say like, oh, if you can, I don't know, shuffle
*  a deck of cards as fast as like a Vegas casino dealer, then you'll be very proficient. It's really
*  the ability to quickly figure out how to do some arbitrary new thing well enough to move on to the
*  next arbitrary thing. But the source of newness and uncertainty, have you found problems in which
*  it's easy to generate new newnessnessnesses? Yeah. New types of newness. Yeah. So a few years ago,
*  so if you had asked me this question around like 2016 maybe, I would have probably said that robotic
*  grasping is a really great example of that because it's a task with great real world utility.
*  You will get a lot of money if you can do it well. When is robotic grasping? Picking up any object.
*  With a robotic hand. Exactly. So you will get a lot of money if you do it well because
*  lots of people want to run warehouses with robots and it's highly non-trivial because
*  very different objects will require very different grasping strategies.
*  But actually since then, people have gotten really good at building systems to solve this problem
*  to the point where I'm not actually sure how much more progress we can
*  make with that as like the main guiding thing. But it's kind of interesting to see the kind of
*  methods that have actually worked well in that space because robotic grasping classically
*  used to be regarded very much as kind of almost like a geometry problem. So people who have
*  studied the history of computer vision will find this very familiar that it's kind of in the same
*  way that in the early days of computer vision people thought of it very much as like an inverse
*  graphics thing. In robotic grasping, people thought of it as an inverse physics problem.
*  Essentially you look at what's in front of you, figure out the shapes, then use your best estimate
*  of the laws of physics to figure out where to put your fingers and you pick up the thing.
*  And it turns out that what works really well for robotic grasping, instantiated in many different
*  recent works, including our own but also ones from many other labs, is to use learning methods with
*  some combination of either exhaustive simulation or like actual real world trial and error.
*  And it turns out that those things actually work really well and then you don't have to worry about
*  solving geometry problems or physics problems. So what are, just by the way in the grasping,
*  what are the difficulties that have been worked on? So one is like the materials of things,
*  maybe occlusions on the perception side. Why is it such a difficult, why is picking stuff up
*  such a difficult problem? Yeah, it's a difficult problem because the number of things that you
*  might have to deal with or the variety of things that you have to deal with is extremely large.
*  And oftentimes things that work for one class of objects won't work for other classes of objects.
*  So if you get really good at picking up boxes and now you have to pick up plastic bags,
*  you just need to employ a very different strategy. And there are many properties of
*  objects that are more than just their geometry. It has to do with the bits that are easier to
*  pick up, the bits that are harder to pick up, the bits that are more flexible, the bits that will
*  cause the thing to pivot and bend and drop out of your hand versus the bits that result in a nice
*  secure grasp. Things that are flexible, things that if you pick them up the wrong way, they'll
*  fall upside down and the contents will spill out. So there's all these little details that come up,
*  but the task is still kind of can be characterized as one task. Like there's a very clear notion of
*  you did it or you didn't do it. So in terms of spilling things, there creeps in this notion that
*  starts to sound and feel like common sense reasoning. Do you think solving the general
*  problem of robotics requires common sense reasoning, requires general intelligence,
*  this kind of human level capability of, like you said, be robust and deal with uncertainty,
*  but also be able to sort of reason and assimilate different pieces of knowledge that you have.
*  Yeah. What are your thoughts on the needs of common sense reasoning in the space of
*  the general robotics problem? So I'm going to slightly dodge that question and say that I think
*  maybe actually it's the other way around is that studying robotics can help us understand how to
*  put common sense into our AI systems. One way to think about common sense is that, and why our
*  current systems might lack common sense, is that common sense is an emergent property of actually
*  having to interact with a particular world, a particular universe and get things done in
*  that universe. So you might think that, for instance, like an image captioning system,
*  maybe it looks at pictures of the world and it types out English sentences. So it kind of
*  deals with our world. And then you can easily construct situations where image captioning
*  systems do things that defy common sense, like give it a picture of a person wearing a fur coat
*  and we'll say it's a teddy bear. But I think what's really happening in those settings is that
*  the system doesn't actually live in our world. It lives in its own world that consists of pixels
*  and English sentences and doesn't actually consist of having to put on a fur coat in the winter so
*  you don't get cold. So perhaps the reason for the disconnect is that the systems that we have now
*  simply inhabit a different universe. And if we build AI systems that are forced to deal with
*  all of the messiness and complexity of our universe, maybe they will have to acquire common sense
*  to essentially maximize their utility. Whereas the systems we're building now don't have to do that.
*  They can take some shortcuts. That's fascinating. You've a couple times already sort of reframed the
*  role of robotics in this whole thing. And for some reason, I don't know if my way of thinking is
*  common, but I thought like we need to understand and solve intelligence in order to solve robotics.
*  And you're kind of framing it as no, robotics is one of the best ways to just study artificial
*  intelligence and build sort of like robotics is like the right space in which you get to explore
*  some of the fundamental learning mechanisms, fundamental sort of multimodal multitask
*  aggregation of knowledge mechanisms that are required for general intelligence. That's really
*  interesting way to think about it. But let me ask about learning. Can the general sort of robotics,
*  the epitome of the robotics problem be solved purely through learning, perhaps end to end learning,
*  sort of learning from scratch, as opposed to injecting human expertise and rules and heuristics
*  and so on? I think that in terms of the spirit of the question, I would say yes. I mean, I think that
*  though in some ways, it's maybe like an overly sharp dichotomy. Like, you know, I think that in
*  some ways when we build algorithms, we, you know, at some point a person does something like a
*  person turned on the computer, a person, you know, implemented TensorFlow. But yeah, I think that in
*  terms of the point that you're getting at, I do think the answer is yes. I think that we can solve
*  many problems that have previously required meticulous manual engineering through automated
*  optimization techniques. And actually, one thing I will say on this topic is I don't think this is
*  actually a very radical or very new idea. I think people have been thinking about automated
*  optimization techniques as a way to do control for a very, very long time. And in some ways,
*  what's changed is really more the name. So, you know, today we would say that, oh, my robot does
*  machine learning, it does reinforcement learning. Maybe in the 1960s, you'd say, oh, my robot is
*  doing optimal control. And maybe the difference between typing out a system of differential
*  equations and doing feedback linearization versus training in neural net, maybe it's not such a
*  large difference. It's just, you know, pushing the optimization deeper and deeper into the thing.
*  Well, it's interesting you think that way, but with especially with deep learning,
*  that the accumulation of sort of experiences in data form to form deep representations
*  starts to feel like knowledge is supposed to optimal control. So this feels like there's
*  an accumulation of knowledge through the learning process. Yes. Yeah. So I think that is a good
*  point that one big difference between learning-based systems and classic optimal control systems is
*  that learning-based systems in principle should get better and better the more they do something.
*  Right. And I do think that that's actually a very, very powerful difference.
*  So if we look back at the world of expert systems, the symbolic AI and so on, of using logic to
*  accumulate expertise, human expertise, human encoded expertise, do you think that will have
*  a role at some points? Deep learning, machine learning, reinforcement learning has shown
*  incredible results and breakthroughs and just inspired thousands, maybe millions of researchers.
*  But there's this less popular now, but it used to be popular idea of symbolic AI. Do you think
*  that will have a role? I think in some ways, the kind of the descendants of symbolic AI actually
*  already have a role. So this is the highly biased history from my perspective. You say that, well,
*  initially we thought that rational decision-making involves logical manipulation. So you have
*  model of the world expressed in terms of logic. You have some query, like what action do I take
*  in order for X to be true, and then you manipulate your logical symbolic representation to get an
*  answer. What that turned into somewhere in the 1990s is, well, instead of building kind of
*  predicates and statements that have true or false values, we'll build probabilistic systems where
*  things have probabilities associated with them, probabilities of being true and false,
*  and that turned into Bayes Nets. That provided a boost to what were really still essentially
*  logical inference systems, just probabilistic logical inference systems. Then people said,
*  well, let's actually learn the individual probabilities inside these models. Then people
*  said, well, let's not even specify the nodes in the models, let's just put a big neural net in
*  there. But in many ways, I see these as actually descendants from the same idea. It's essentially
*  instantiating rational decision-making by means of some inference process and learning by means
*  of an optimization process. In a sense, I would say yes, that it has a place, and in many ways,
*  that place is already holds that place. It's already in there. Yeah, it's just by different.
*  It looks slightly different than it was before. Yeah, but there are some things that we can think
*  about that make this a little bit more obvious. If I train a big neural net model to predict what
*  will happen in response to my robot's actions, and then I run probabilistic inference, meaning
*  I invert that model to figure out the actions that lead to some plausible outcome. To me,
*  that seems like a kind of logic. You have a model of the world that just happens to be expressed
*  by a neural net, and you are doing some inference procedure, some sort of manipulation on that model
*  to figure out the answer to a query that you have. It's the interpretability, it's the explainability,
*  though, that seems to be lacking more so because the nice thing about expert systems is you can
*  follow the reasoning of the system. To us, mere humans is somehow compelling. It's just,
*  I don't know what to make of this fact that there's a human desire for intelligence systems to be able
*  to convey in a poetic way to us why it made the decisions it did, like tell a convincing story.
*  Perhaps that's a silly human thing. We shouldn't expect that of intelligence systems. We should
*  be super happy that there is intelligence systems out there. If I were to psychoanalyze the
*  researchers at the time, I would say expert systems connected to that part, that desire of AI
*  researchers for systems to be explainable. Maybe on that topic, do you have a hope that
*  inference systems, learning-based systems, will be as explainable as the dream was with expert systems,
*  for example? I think it's a very complicated question because I think that in some ways,
*  the question of explainability is very closely tied to the question of performance. Why do you
*  want your system to explain itself? Well, so that when it screws up, you can figure out why it did
*  it. In some ways, that's a much bigger problem, actually. Your system might screw up and then it
*  might screw up in how it explains itself, or you might have some bug somewhere so that it's not
*  actually doing what it was supposed to do. Maybe a good way to view that problem is really as a
*  bigger problem of verification and validation, of which explainability is one component.
*  I see. I just see it differently. I see explainability. You put it beautifully. I think
*  you actually summarized the field of explainability. To me, there's another aspect of explainability,
*  which is storytelling, that has nothing to do with errors or with … It uses errors as elements
*  of its story as opposed to a fundamental need to be explainable when errors occur. It's just that
*  for other intelligence systems to be in our world, we seem to want to tell each other stories.
*  And that's true in the political world. That's true in the academic world.
*  Neural networks are less capable of doing that, or perhaps they're equally capable of storytelling.
*  Storytelling, maybe it doesn't matter what the fundamentals of the system are. You just need to
*  be a good storyteller. Maybe one specific story I can tell you about in that space is actually
*  about some work that was done by my former collaborator, who's now a professor at MIT named
*  Jacob Andreas. Jacob actually works in natural language processing, but he had this idea to do
*  a little bit of work in reinforcement learning on how natural language can basically structure
*  the internals of policies trained with RL. One of the things he did is he set up a model
*  that attempts to perform some task that's defined by a reward function,
*  but the model reads in a natural language instruction. This is a pretty common thing
*  to do in instruction following. You tell it, go to the red house, and then it's supposed to go
*  to the red house. But then one of the things that Jacob did is he treated that sentence not as a
*  command from a person, but as a representation of the internal state of the mind of this policy,
*  essentially, so that when it was faced with a new task, what it would do is it would basically try
*  to think of possible language descriptions, attempt to do them, and see if they led to the
*  right outcome. So it would kind of think out loud, like, you know, I'm faced with this new task,
*  what am I going to do? Let me go to the red house. Oh, that didn't work. Let me go to the blue room
*  or something. Let me go to the green plant. And once it got some reward, it would say, oh, go to
*  the green plant. That's what's working. I'm going to go to the green plant. And then you could look
*  at the string that it came up with, and that was a description of how it thought it should solve the
*  problem. So you could basically incorporate language as internal state, and you can start
*  getting some handle on these kinds of things. And then what I was kind of trying to get to is that
*  also, if you add to the reward function, the convincingness of that story. So I have another
*  reward signal of like, people who review that story, how much they like it. So that, you know,
*  initially, that could be a hyperparameter, sort of hard coded heuristic type of thing. But it's an
*  interesting notion of the convincingness of the story becoming part of the reward function,
*  the objective function of the explainability. It's in the world of sort of Twitter and fake news,
*  that might be a scary notion that the nature of truth may not be as important as the convincingness
*  of the how convincing you are in telling the story around the facts. Well, let me ask
*  the basic question. You're one of the world class researchers in reinforcement learning,
*  deep reinforcement learning, certainly in the robotics space. What is reinforcement learning?
*  I think that what reinforcement learning refers to today is really just the
*  kind of the modern incarnation of learning based control. So classically, reinforcement learning
*  has a much more narrow definition, which is that it's, you know, literally learning from
*  reinforcement, like the thing does something, and then it gets a reward or punishment. But really,
*  I think the way the term is used today is it's used to refer more broadly to learning based control.
*  So some kind of system that's supposed to be controlling something and it uses data to get
*  better. And what does control mean? So this action is the fundamental element. It means making
*  rational decisions and rational decisions are decisions that maximize a measure of utility.
*  And sequentially, so you made decisions time and time and time again. Now, like, it's easier to see
*  that kind of idea in the space of maybe games and the space of robotics. Do you see it bigger
*  than that? Is it applicable? Like, where are the limits of the applicability of reinforcement
*  learning? Yeah. So rational decision making is essentially the encapsulation of the AI problem
*  viewed through a particular lens. So any problem that we would want a machine to do, an intelligent
*  machine can likely be represented as a decision making problem. Classifying images is a decision
*  making problem, although not a sequential one typically. You know, controlling a chemical
*  plant is a decision making problem. Deciding what videos to recommend on YouTube is a decision
*  making problem. And one of the really appealing things about reinforcement learning is if it does
*  encapsulate the range of all these decision making problems, perhaps working on reinforcement
*  learning is, you know, one of the ways to reach a very broad swath of AI problems.
*  But what is the fundamental difference between reinforcement learning and maybe supervised machine
*  learning? So reinforcement learning can be viewed as a generalization of supervised machine learning.
*  You can certainly cast supervised learning as a reinforcement learning problem. You can just say
*  your loss function is the negative of your reward, but you have stronger assumptions. You have the
*  assumption that someone actually told you what the correct answer was, that your data was IID,
*  and so on. So you could view reinforcement learning as essentially relaxing some of those
*  assumptions. Now that's not always a very productive way to look at it, because if you actually have a
*  supervised learning problem, you'll probably solve it much more effectively by using supervised
*  learning methods, because it's easier. But you can view reinforcement learning as a generalization.
*  No, for sure. But they're fundamentally different. That's a mathematical statement. That's
*  absolutely correct. But it seems that reinforcement learning, the kind of tools we'll bring to the
*  table today, of today, so maybe down the line, everything will be a reinforcement learning
*  problem. Just like you said, image classification should be mapped to a reinforcement learning
*  problem. But today, the tools and ideas, the way we think about them are different.
*  Sort of supervised learning has been used very effectively to solve basic narrow AI problems.
*  Reinforcement learning kind of represents the dream of AI. It's very much so in the research
*  space now, in sort of captivating the imagination of people of what we can do with intelligent
*  systems. But it hasn't yet had as wide of an impact as the supervised learning approaches.
*  So that sort of, my question comes in a more practical sense. Like, what do you see is the
*  gap between the more general reinforcement learning and the very specific, yes,
*  it's sequential decision making with one step in the sequence of the supervised learning?
*  From a practical standpoint, I think that one thing that is potentially a little tough now,
*  and this is, I think, something that we'll see, this is a gap that we might see closing over the
*  next couple of years, is the ability of reinforcement learning algorithms to effectively utilize
*  large amounts of prior data. So one of the reasons why it's a bit difficult today
*  to use reinforcement learning for all the things that we might want to use it for
*  is that in most of the settings where we want to do rational decision making,
*  it's a little bit tough to just deploy some policy that does crazy stuff and learns purely
*  through trial and error. It's much easier to collect a lot of data, a lot of logs of some
*  other policy that you've got. And then maybe, if you can get a good policy out of that,
*  then you deploy it and let it kind of fine tune a little bit. But algorithmically,
*  it's quite difficult to do that. So I think that once we figure out how to
*  get reinforcement learning to bootstrap effectively from large data sets, then we'll see
*  very, very rapid growth in applications of these technologies. So this is what's referred to as
*  off-policy reinforcement learning or offline RL or batch RL. And I think we're seeing a lot of
*  research right now that's bringing us closer and closer to that.
*  Can you maybe paint the picture of the different methods? She said off-policy,
*  what's value-based reinforcement learning? What's policy-based? What's model-based? What's
*  off-policy, on-policy? What are the different categories of reinforcement learning?
*  So one way we can think about reinforcement learning is that it's in some very fundamental
*  way, it's about learning models that can answer kind of what if questions. So what would happen
*  if I take this action that I hadn't taken before? And you do that, of course, from experience,
*  from data. And oftentimes you do it in a loop. So you build a model that answers these what if
*  questions, use it to figure out the best action you can take, and then go and try taking that
*  and see if the outcome agrees with what you predicted. So the different kinds of techniques
*  basically refer to different ways of doing it. So model-based methods answer a question of
*  what state you would get, basically what would happen to the world if you were to take a certain
*  action, value-based methods, they answer the question of what value you would get, meaning
*  what utility you would get. But in a sense, they're not really all that different because
*  they're both really just answering these what if questions. Now, unfortunately for us, with current
*  machine learning methods, answering what if questions can be really hard because they are
*  really questions about things that didn't happen. If you wanted to answer what if questions about
*  things that did happen, you wouldn't need a learned model, you would just repeat the thing that worked
*  before. And that's really a big part of why RL is a little bit tough. So if you have a purely on
*  policy kind of online process, then you ask these what if questions, you make some mistakes, then
*  you go and try doing those mistaken things, and then you observe kind of the counter examples
*  that will teach you not to do those things again. If you have a bunch of off-policy data and you just
*  want to synthesize the best policy you can out of that data, then you really have to deal with the
*  challenges of making these counterfactual. First of all, what's a policy? A policy is a model or
*  some kind of function that maps from observations of the world to actions. So in reinforcement
*  learning, we often refer to the current configuration of the world as the state. So we say the state kind
*  of encompasses everything you need to fully define where the world is at at the moment.
*  Depending on how we formulate the problem, we might say you either get to see the state
*  or you get to see an observation, which is some snapshot, some piece of the state.
*  Policy just includes everything in it in order to be able to act in this world.
*  What does off-policy mean?
*  The terms on-policy and off-policy refer to how you get your data. If you get your data from somebody
*  else who was doing some other stuff, maybe you get your data from some manually programmed system
*  that was just running in the world before. That's referred to as off-policy data. But if you got the
*  data by actually acting in the world based on what your current policy thinks is good, we call that
*  on-policy data. Obviously, on-policy data is more useful to you because if your current policy makes
*  some bad decisions, you will actually see that those decisions are bad. Off-policy data, however,
*  might be much easier to obtain because maybe that's all the log data that you have from before.
*  We talked about offline, talked about autonomous vehicles so you can envision off-policy approaches
*  in robotic spaces where there's already a ton of robots out there, but they don't get the luxury
*  of being able to explore based on a reinforcement learning framework. How do we make, again, open
*  question, but how do we make off-policy methods work? Yeah. This is something that has been
*  a big open problem for a while. In the last few years, people have made a little bit of
*  progress on that. I can tell you about it. It's not by any means solved yet, but I can tell you
*  some of the things that, for example, we've done to try to address some of the challenges.
*  It turns out that one really big challenge with off-policy reinforcement learning is that
*  you can't really trust your models to give accurate predictions for any possible action.
*  If in my data set, I never saw somebody steering the car off the road onto the sidewalk,
*  my value function or my model is probably not going to predict the right thing if I ask what
*  would happen if I were to steer the car off the road onto the sidewalk. One of the important things
*  you have to do to get off-policy RL to work is you have to be able to figure out whether a given
*  action will result in a trustworthy prediction or not. You can use distribution estimation methods,
*  density estimation methods to try to figure that out. You could figure out that, well, this action,
*  my model is telling me that it's great, but it looks totally different from any action I've
*  taken before, so my model is probably not correct. You can incorporate regularization terms into your
*  learning objective that will essentially tell you not to ask those questions that your model is
*  unable to answer. What would lead to breakthroughs in this space, do you think? What's needed? Is
*  this a data set question? Do we need to collect big benchmark data sets that allow us to explore the
*  space? Is it new kinds of methodologies? What's your sense? Or maybe coming together in a space
*  of robotics and defining the right problem to be working on? I think for off-policy reinforcement
*  learning in particular, it's very much an algorithms question right now. This is something that
*  I think is great because an algorithms question is that that just takes some very smart people
*  to get together and think about it really hard, whereas if it was a data problem or a hardware
*  problem, that would take some serious engineering. That's why I'm pretty excited about that problem
*  because I think that we're in a position where we can make some real progress on it just by coming
*  up with the right algorithms. In terms of which algorithms they could be, the problems at their
*  core are very related to problems in things like causal inference. Because what you're really
*  dealing with is situations where you have a model, a statistical model, that's trying to make
*  predictions about things that I hadn't seen before. If it's a model that's generalizing properly,
*  that'll make good predictions. If it's a model that picks up on spurious correlations that will
*  not generalize properly, and then you have an arsenal of tools you can use. You could, for example,
*  figure out what are the regions where it's trustworthy, or on the other hand, you could
*  try to make it generalize better somehow, or some combination of the two. Is there room for mixing
*  where most of it, like 90, 95% is off policy, you already have the data set, and then you get to
*  send the robot out to do a little exploration? What's that role of mixing them together?
*  Yeah, absolutely. I think that this is something that you actually described very well at the
*  beginning of our discussion when you talked about the iceberg. This is the iceberg. The 99% of your
*  prior experience, that's your iceberg. You'd use that for off-policy reinforcement learning.
*  And then, of course, if you've never opened that particular kind of door with that particular lock
*  before, then you have to go out and fiddle with it a little bit, and that's that additional 1%
*  to help you figure out a new task. And I think that's actually a pretty good recipe going forward.
*  Is this, to you, the most exciting space of reinforcement learning now? And maybe taking a
*  step back, not just now, but what's, to you, is the most beautiful idea? I apologize for the
*  romanticized question, but the beautiful idea or concept in reinforcement learning?
*  In general, I actually think that one of the things that is a very beautiful idea in reinforcement
*  learning is just the idea that you can obtain a near-optimal controller, a near-optimal policy,
*  without actually having a complete model of the world. It's something that feels perhaps kind of
*  obvious if you just hear the term reinforcement learning or you think about trial and error
*  learning, but from a controls perspective, it's a very weird thing because classically,
*  we think about engineered systems and controlling engineered systems as the problem of writing down
*  some equations and then figuring out, given these equations, basically solve for x, figure out the
*  thing that maximizes its performance. And the theory of reinforcement learning actually gives us
*  a mathematically principled framework to reason about optimizing some quantity when you don't
*  actually know the equations that govern that system. And to me, that actually seems
*  very elegant, not something that becomes immediately obvious, at least in the mathematical sense.
*  Does it make sense to you that it works at all?
*  Well, I think it makes sense when you take some time to think about it, but it is a little surprising.
*  Well, then taking a step into the more deeper representations, which is also very surprising,
*  of the richness of the state space, the space of environments that this kind of approach can operate.
*  And can you maybe say, what is deep reinforcement learning?
*  Well, deep reinforcement learning simply refers to taking reinforcement learning
*  algorithms and combining them with high capacity neural net representations,
*  which is, it might at first seem like a pretty arbitrary thing, just take these two components
*  and stick them together. But the reason that it's something that has become so important
*  in recent years is that reinforcement learning, it kind of faces an exacerbated version of a
*  problem that has faced many other machine learning techniques. So if we go back to the early 2000s
*  or the late 90s, we'll see a lot of research on machine learning methods that have some very
*  appealing mathematical properties, like they reduced the convex optimization problems, for instance.
*  But they require very special inputs. They require a representation of the input that is clean in
*  some way, like for example, clean in the sense that the classes in your multi-class classification
*  problems separate linearly. So they have some kind of good representation, we call this feature
*  representation. And for a long time, people were very worried about features in the world
*  of supervised learning, because somebody had to actually build those features. So you couldn't
*  just take an image and plug it into your logistic regression or your SVM or something. Someone had
*  to take that image and process it using some handwritten code. And then neural nets came along
*  and they could actually learn the features. And suddenly, we could apply learning directly to the
*  raw inputs, which was great for images, but it was even more great for all the other fields where
*  people hadn't come up with good features yet. And one of those fields was actually reinforcement
*  learning, because in reinforcement learning, the notion of features, if you don't use neural nets
*  and you have to design your own features, is very, very opaque. It's very hard to imagine,
*  let's say I'm playing chess or Go, what is a feature with which I can represent the value
*  function for Go or even the optimal policy for Go linearly? I don't even know how to start thinking
*  about it. And people tried all sorts of things. They would write down, an expert chess player
*  looks for whether the knight is in the middle of the board or not. So that's a feature, is knight
*  in middle of board. And they would write these long lists of arbitrary made up stuff. And that was
*  really getting us nowhere. And chess is a little more accessible than the robotics problem.
*  Absolutely. There's at least experts in the different features for chess. But still,
*  the neural network there, to me, you put it eloquently and almost made it seem like a
*  natural step to add neural networks. But the fact that neural networks are able to discover
*  features in the control problem, it's very interesting. It's hopeful. I'm not sure what
*  to think about it, but it feels hopeful that the control problem has features to be learned.
*  Like, I guess my question is, is it surprising to you how far the deep side of deep reinforcement
*  learning is able to, like what the space of problems has been able to tackle from, especially
*  in games with the Alpha Star and Alpha Zero and just the representation power there and in the
*  robotics space? And what is your sense of the limits of this representation power and the control
*  context? I think that in regard to the limits bit here,
*  I think that one thing that makes it a little hard to fully answer this question is because
*  in settings where we would like to push these things to the limit, we encounter other bottlenecks.
*  So the reason that I can't get my robot to learn how to do the dishes in the kitchen,
*  it's not because this neural net is not big enough. It's because when you try to actually do
*  trial and error learning, reinforcement learning directly in the real world where you have the
*  potential to gather these large, highly varied and complex data sets, you start running into other
*  problems. Like one problem you run into very quickly, it'll first sound like a very pragmatic
*  problem, but it actually turns out to be a pretty deep scientific problem. Take the robot, put it
*  in your kitchen, have it try to learn to do the dishes with trial and error. It'll break all your
*  dishes. And then we'll have no more dishes to clean. Now you might think this is a very practical
*  issue, but there's something to this, which is that if you have a person trying to do this,
*  a person will have some degree of common sense. They'll break one dish, they'll be a little more
*  careful with the next one. And if they break all of them, they're going to go and get more or
*  something like that. So there's all sorts of scaffolding that comes very naturally to us for
*  our learning process. Like if I have to learn something through trial and error, I have a
*  common sense to know that I have to try multiple times. If I screw something up, I ask for help,
*  or I reset things or something like that. And all of that is kind of outside of the classic
*  reinforcement learning problem formulation. There are other things that can also be categorized as
*  kind of scaffolding, but are very important. Like for example, where do you get your reward function?
*  If I want to learn how to pour a cup of water, well, how do I know if I've done it correctly?
*  Now that probably requires an entire computer vision system to be built just to determine that.
*  And that seems a little bit inelegant. So there are all sorts of things like this that start to
*  come up when we think through what we really need to get reinforcement learning to happen at scale
*  in the real world. And I think that many of these things actually suggest a little bit of a shortcoming
*  in the problem formulation and a few deeper questions that we have to resolve. That's really
*  interesting. I talked to like David Silver, bought AlphaZero, and it seems like there's no, again,
*  we haven't hit the limit at all in the context when there is no broken dishes. So in the case of Go,
*  it's really about just scaling compute. So again, like the bottleneck is the amount of money you're
*  willing to invest in compute and then maybe the different scaffolding around how difficult it is
*  to scale compute maybe. But there, there's no limit. And it's interesting. Now we move to the real
*  world and there's the broken dishes, there's all the, and the reward function like you mentioned.
*  That's really nice. So what, how do we push forward there? Do you think there's this kind of a sample
*  efficiency question that people bring up of, you know, not having to break a hundred thousand dishes?
*  Is this an algorithm question? Is this a data selection like question? What do you think? How
*  do we not break too many dishes? Yeah. Well, one way we can think about that is that
*  maybe we need to be better at reusing our data, building that iceberg. So perhaps,
*  perhaps it's too much to hope that you can have a machine that in isolation, in the vacuum,
*  without anything else can just master complex tasks in like in minutes the way that people do.
*  But perhaps it also doesn't have to, perhaps what it really needs to do is have an existence,
*  a lifetime where it does many things and the previous things that it has done, prepare it
*  to do new things more efficiently. And, you know, the study of these kinds of questions typically
*  falls under categories like multitask learning or meta learning. But they all fundamentally deal
*  with the same general theme, which is use experience for doing other things to learn to
*  do new things efficiently and quickly. So what do you think about if you just look at the one
*  particular case study of a Tesla autopilot that has quickly approaching towards a million vehicles
*  on the road where some percentage of the time, 30, 40% of the time is driving using the computer
*  vision, multitask, HydroNet, right? And then the other percent, that's what they call it, HydroNet.
*  The other percent is human controlled. From the human side, how can we use that data? What's your
*  sense? So like, what's the signal? Do you have ideas in this autonomous ecosystem when people
*  can lose their lives? You know, it's a safety critical environment. So how do we use that data?
*  So I think that actually the kind of problems that come up when we want
*  systems that are reliable and that can kind of understand the limits of their capabilities,
*  they're actually very similar to the kind of problems that come up when we're doing
*  off-policy reinforcement learning. So as I mentioned before, in off-policy reinforcement
*  learning, the big problem is you need to know when you can trust the predictions of your model
*  because if you're trying to evaluate some pattern of behavior for which your model doesn't give you
*  an accurate prediction, then you shouldn't use that to modify your policy. And it's actually
*  very similar to the problem that we're faced when we actually then deploy that thing and we want to
*  decide whether we trust it in the moment or not. So perhaps we just need to do a better job of
*  figuring out that part. And that's a very deep research question, of course, but it's also a
*  question that a lot of people are working on. So I'm pretty optimistic that we can make some
*  progress on that over the next few years. What's the role of simulation in reinforcement
*  learning, deep reinforcement learning, reinforcement learning? Like how essential is it? It's been
*  essential for the breakthroughs so far, for some interesting breakthroughs. Do you think it's a
*  crutch that we rely on? I mean, again, it connects to our off-policy discussion, but do you think we
*  can ever get rid of simulation? Or do you think simulation will actually take over? We'll create
*  more and more realistic simulations that will allow us to solve actual real-world problems,
*  like transfer the models we learn in simulation to real-world problems. Yeah. I think that simulation
*  is a very pragmatic tool that we can use to get a lot of useful stuff to work right now.
*  But I think that in the long run, we will need to build machines that can learn from real data,
*  because that's the only way that we'll get them to improve perpetually. Because if we
*  can't have our machines learn from real data, if they have to rely on simulated data,
*  eventually the simulator becomes the bottleneck. In fact, this is a general thing. If your machine
*  has any bottleneck that is built by humans and that doesn't improve from data,
*  it will eventually be the thing that holds it back. And if you're entirely reliant on your
*  simulator, that'll be the bottleneck. If you're entirely reliant on a manually designed controller,
*  that's going to be the bottleneck. So simulation is very useful. It's very pragmatic,
*  but it's not a substitute for being able to utilize real experience. And this is, by the way,
*  this is something that I think is quite relevant now, especially in the context of some of the
*  things we've discussed, because some of these kind of scaffolding issues that I mentioned,
*  things like the broken dishes and the unknown reward function, these are not problems that you
*  would ever stumble on when working in a purely simulated kind of environment. But they become
*  very apparent when we try to actually run these things in the real world.
*  To throw a brief wrench into our discussion, let me ask, do you think we're living in a simulation?
*  Oh, I have no idea.
*  Do you think that's a useful thing to even think about, about the fundamental physics nature of
*  reality? Or another perspective, the reason I think the simulation hypothesis is interesting
*  is to think about how difficult is it to create sort of a virtual reality game type situation
*  that will be sufficiently convincing to us humans, or sufficiently enjoyable that we wouldn't want to
*  leave? That's actually a practical engineering challenge. And I personally really enjoy virtual
*  reality, but it's quite far away. But I kind of think about what would it take for me to want
*  to spend more time in virtual reality versus the real world? And that's a nice clean question,
*  because at that point, we've reached, if I want to live in a virtual reality, that means we're just
*  a few years away where majority of the population lives in a virtual reality. And that's how we
*  create the simulation, right? You don't need to actually simulate the quantum gravity and just
*  every aspect of the universe. And that's an interesting question for reinforcement learning
*  too, is if we want to make sufficiently realistic simulations that may, it blend the difference
*  between sort of the real world and the simulation, thereby just some of the things we've been talking
*  about, kind of the problems go away if we can create actually interesting, rich simulations.
*  It's an interesting question. And it actually, I think your question casts your previous question
*  in a very interesting light. Because in some ways, asking whether we can, well, the more
*  kind of practical version of this, like, you know, can we build simulators that are good enough
*  to train essentially AI systems that will work in the world? And it's kind of interesting to
*  think about this, about what this implies. If true, it kind of implies that it's easier to create the
*  universe than it is to create a brain. And that seems like, put this way, it seems kind of weird.
*  The aspect of the simulation most interesting to me is the simulation of other humans. That seems to be
*  a complexity that makes the robotics problem harder. Now, I don't know if every robotics person
*  agrees with that notion. Just as a quick aside, what are your thoughts about when the human enters
*  the picture of the robotics problem? How does that change the reinforcement learning problem,
*  the learning problem in general? Yeah, I think that's a, it's a kind of a complex question. And
*  I guess my hope for a while had been that if we build these robotic learning systems that
*  are multitask, that utilize lots of prior data, and that learn from their own experience,
*  the bit where they have to interact with people will be perhaps handled in much the same way as
*  all the other bits. So if they have prior experience in interacting with people, and they can learn from
*  their own experience of interacting with people for this new task, maybe that'll be enough.
*  Now, of course, if it's not enough, there are many other things we can do. And there's quite a bit of
*  research in that area. But I think it's worth a shot to see whether the multi-agent interaction,
*  the ability to understand that other beings in the world have their own goals and intentions
*  and thoughts and so on, whether that kind of understanding can emerge automatically from
*  simply learning to do things with and maximize utility. That information arises from the data.
*  You've said something about gravity, sort of, that you don't need to explicitly inject anything
*  into the system, they can be learned from the data. And gravity is an example of something that could
*  be learned from data, sort of like the physics of the world. Like, what, what are the limits of what
*  we can learn from data? Do you really, do you think we can, so a very simple, clean way to ask
*  that is, do you really think we can learn gravity from just data? The idea, the laws of gravity?
*  So, so something that I think is a common kind of pitfall when thinking about prior knowledge and
*  learning is to assume that just because we know something, then that it's better to tell the
*  machine about that rather than have it figure it out on its own. In many cases, things that are
*  important that affect many of the events that the machine will experience are actually pretty easy
*  to learn. Like, you know, if things, if every time you drop something, it falls down, like,
*  yeah, you might not get the, you know, you might get kind of the Newton's version, not Einstein's
*  version, but it'll be pretty good. And it will probably be sufficient for you to act rationally
*  in the world because you see the phenomenon all the time. So things that are readily apparent from
*  the data, we might not need to specify those by hand. It might actually be easier to let the
*  machine figure them out. It just feels like that there might be a space of many local,
*  local minima in terms of theories of this world that we would discover and get stuck on.
*  Yeah, of course. That Newtonian mechanics is not necessarily easy to come by.
*  Yeah. And well, in fact, in some fields of science, for example, human civilizations
*  that sell full of these local optima. So for example, if you think about how people try to
*  figure out biology and medicine, you know, for the longest time, the kind of rules, the kind of
*  principles that serve us very well in our day-to-day lives actually serve us very poorly
*  in understanding medicine and biology. We had kind of very superstitious and weird ideas about how the
*  body worked until the advent of the modern scientific method. So that does seem to be,
*  you know, a failing of this approach, but it's also a failing of human intelligence, arguably.
*  Maybe a small aside, but some, you know, the idea of self-play is fascinating and reinforcement
*  learning. Sort of these competitive, creating a competitive context in which agents can
*  play against each other in sort of at the same skill level and thereby increasing each other's
*  skill level. It seems to be this kind of self-improving mechanism is exceptionally
*  powerful in the context where it could be applied. First of all, is that beautiful to you that this
*  mechanism work as well as it does? And also can we generalize to other contexts like in the robotic
*  space or anything that's applicable to the real world? I think that it's a very interesting idea.
*  And I, but I suspect that the bottleneck to actually generalizing it to the robotic setting
*  is actually going to be the same as, as the bottleneck for everything else. That we need
*  to be able to build machines that can get better and better through natural interaction with the
*  world. And once we can do that, then they can go out and play with, they can play with each other,
*  they can play with people, they can play with the natural environment. But before we get there,
*  we've got all these other problems we've got, we have to get out of the way.
*  So there's no shortcut around that. You have to interact with the natural environment that.
*  Well, because in a, in a self-play setting, you still need a mediating mechanism. So the,
*  the reason that, you know, self-play works for a board game is because the rules of that board game
*  mediate the interaction between the agents. So the kind of intelligent behavior that will emerge
*  depends very heavily on the nature of that mediating mechanism.
*  So on the side of reward functions, that's coming up with good reward functions seems to be the thing
*  that we associate with general intelligence. Like human beings seem to value the idea of developing
*  our own reward functions of, you know, at arriving at meaning and so on. And yet for reinforcement
*  learning, we often kind of specify that's the given. What's your sense of how we develop
*  reward, you know, good reward functions? Yeah, I think that's a very complicated and very
*  deep question. And you're completely right that classically in reinforcement learning,
*  this question has kind of been treated as an on issue that you sort of treat the reward as
*  this external thing that comes from some other bit of your biology and you kind of don't worry
*  about it. And I do think that that's actually, you know, a little bit of a mistake that we should
*  worry about it. And we can approach it in a few different ways. We can approach it, for instance,
*  by thinking of rewards as a communication medium. We can say, well, how does a person
*  communicate to a robot what its objective is? You can approach it also as sort of more of an
*  intrinsic motivation medium. You could say, can we write down kind of a general objective that leads
*  to good capability? Like, for example, can you write down some objectives such that even in the
*  absence of any other task, if you maximize that objective, you'll sort of learn useful things.
*  This is something that has sometimes been called unsupervised reinforcement learning,
*  which I think is a really fascinating area of research, especially today. We've done a bit of
*  work on that recently. One of the things we've studied is whether we can have some notion of
*  unsupervised reinforcement learning by means of information theoretic quantities, like, for instance,
*  minimizing a Bayesian measure of surprise. This is an idea that was pioneered actually in the
*  computational neuroscience community by folks like Carl Friston. And we've done some work recently
*  that shows that you can actually learn pretty interesting skills by essentially behaving in a
*  way that allows you to make accurate predictions about the world. It seems a little circular,
*  like do the things that will lead to you getting the right answer for prediction. But by doing this,
*  you can sort of discover stable niches in the world. You can discover that if you're playing
*  Tetris, then correctly clearing the rows will let you play Tetris for longer and keep the board nice
*  and clean, which sort of satisfies some desire for order in the world. And as a result, get some
*  degree of leverage over your domain. So we're exploring that pretty actively. Is there a role
*  for a human notion of curiosity in itself being the reward sort of discovering new things about
*  the world? So one of the things that I'm pretty interested in is actually whether discovering new
*  things can actually be an emergent property of some other objective that quantifies capability.
*  So new things for the sake of new things maybe might not by itself be the right answer, but
*  perhaps we can figure out an objective for which discovering new things is actually the natural
*  consequence. That's something we're working on right now, but I don't have a clear answer for
*  you there yet that's still a work in progress. You mean just that it's a curious observation to see
*  sort of creative patterns of curiosity on the way to optimize for a particular
*  for on the way to optimize for a particular measure of capability.
*  Is there ways to understand or anticipate unexpected unintended consequences of
*  particular reward functions sort of anticipate the kind of strategies that might be developed
*  and try to avoid highly detrimental strategies? Yeah. So classically this is something that has
*  been pretty hard in reinforcement learning because it's difficult for a designer to have
*  good intuition about what a learning algorithm will come up with when they give it some objective.
*  There are ways to mitigate that. One way to mitigate it is to actually define an objective
*  that says like don't do weird stuff. You can actually quantify it. You can say just like don't
*  enter situations that have low probability under the distribution of states you've seen before.
*  It turns out that that's actually one very good way to do off-policy reinforcement learning actually.
*  So we can do some things like that. If we slowly venture in speaking about reward functions into
*  greater and greater levels of intelligence there's I mean Stuart Russell thinks about this the alignment
*  of AI systems with us humans. So how do we ensure that AGI systems align with us humans? It's a
*  it's kind of a reward function question of specifying the behavior of AI systems such that
*  their success aligns with the broader intended success interest of human beings.
*  Do you have thoughts on this? Do you have kind of concerns of where reinforcement learning fits
*  into this or are you really focused on the current moment of us being quite far away and
*  trying to solve the robotics problem? I don't have a great answer to this but
*  you know and I do think that this is a problem that's important to figure out.
*  For my part I'm actually a bit more concerned about the other side of this equation that
*  you know maybe rather than unintended consequences for objectives that are specified too well I'm
*  actually more worried right now about unintended consequences for objectives that are not optimized
*  well enough which might become a very pressing problem when we for instance try to use these
*  techniques for safety critical systems like cars and aircraft and so on. I think at some point we'll
*  face the issue of objectives being optimized too well but right now I think we're more likely
*  to face the issue of them not being optimized well enough. But you don't think unintended
*  consequences can arise even when you're far from optimality sort of like on the path to it?
*  Oh no I think unintended consequences can absolutely arise. It's just I think right now
*  the bottleneck for improving reliability safety and things like that is more with systems that
*  like need to work better that need to optimize their objective better.
*  Do you have thoughts concerns about existential threats of human level intelligence that if we
*  put on our hat of looking in 10, 20, 100, 500 years from now do you have concerns about
*  existential threats of AI systems? I think there are absolutely existential threats
*  for AI systems just like there are for any powerful technology. But I think that these
*  kinds of problems can take many forms and some of those forms will come down to people with
*  nefarious intent. Some of them will come down to AI systems that have some fatal flaws and some of
*  them will of course come down to AI systems that are too capable in some way. But among this set of
*  potential concerns I would actually be much more concerned about the first two right now
*  and principally the one with nefarious humans because you know just through all of human
*  history actually it's the nefarious humans that have been the problem not the nefarious machines
*  than I am about the others. And I think that right now the best that I can do to make sure
*  things go well is to you know build the best technology I can and also hopefully promote
*  responsible use of that technology. Do you think RL systems has something to teach us humans?
*  You said nefarious humans getting us in trouble. I mean machine learning systems have in some ways
*  have revealed to us the ethical flaws in our data. In that same kind of way can reinforcement
*  learning teach us about ourselves? Has it taught something? What have you learned about yourself
*  from trying to build robots and reinforcement learning systems?
*  I'm not sure what I've learned about myself but maybe part of the answer to your question
*  might become a little bit more apparent once we see more widespread deployment of reinforcement
*  learning for decision-making support in you know in domains like you know health care, education,
*  social media etc. And I think we will see some interesting stuff emerge there. We will see for
*  instance what kind of behaviors these systems come up with in situations where there is interaction
*  with humans and where they have you know possibility of influencing human behavior.
*  I think we're not quite there yet but you know maybe in the next few years we'll see some
*  interesting stuff come out in that area. I hope outside the research space because the the exciting
*  space where this could be observed is sort of large companies that deal with large data and I hope
*  there's some transparency. One of the things that's unclear when I look at social networks
*  and just online is why an algorithm did something or whether you know even an algorithm was involved
*  and that'd be interesting as a from a research perspective just to observe the results of
*  algorithms to open up that data or to at least be sufficiently transparent about the behavior of
*  these AI systems in the real world. What's your sense? I don't know if you looked at the
*  block post beta lesson by Rich Sutton where it looks at sort of the big lesson of researching AI
*  and in reinforcement learning is that simple methods, general methods that leverage computation
*  seem to work well. So basically don't try to do any kind of fancy algorithms just wait for
*  computation and get fast. Do you share this kind of intuition? I think the high level idea makes a
*  lot of sense. I'm not sure that my takeaway would be that we don't need to work on algorithms. I
*  think that my takeaway would be that we should work on general algorithms and actually I think
*  that this idea of needing to better automate the acquisition of experience in the real world
*  actually follows pretty naturally from Rich Sutton's conclusion. So if the claim is that
*  automated general methods plus data leads to good results then it makes sense that we should build
*  general methods and we should build the kind of methods that we can deploy and get them to go out
*  there and like collect their experience autonomously. I think that one place where I think that the
*  current state of things falls a little bit short of that is actually that the going out there and
*  collecting the data autonomously which is easy to do in a simulated board game but very hard to
*  do in the real world. Yeah it keeps coming back to this one problem right? So your mind is focused
*  there now in this real world. It just seems scary the step of collecting the data and it seems
*  unclear to me how we can do it effectively. Well you know seven billion people in the world each
*  of them had to do that at some point in their lives. And we should leverage that experience
*  that they've all done. We should be able to try to collect that kind of data. Okay big questions
*  maybe stepping back through your life. What book or books technical or fiction or philosophical
*  had a big impact on the way you saw the world and the way you thought about in the world,
*  your life in general? And maybe what books if it's different would you recommend people
*  consider reading on their own intellectual journey? It could be within reinforcement learning
*  but it could be very much bigger. I don't know if this is like a scientifically like particularly
*  meaningful answer but like the honest answer is that I actually found a lot of the work by
*  Isaac Asimov to be very inspiring when I was younger. I don't know if that has anything to
*  do with AI necessarily. You don't think it had a ripple effect in your life? Maybe it did.
*  But yeah I think that a vision of a future where well first of all artificial
*  I might say artificial intelligence system, artificial robotic systems have you know kind
*  of a big place a big role in society and where we try to imagine the sort of the limiting case
*  of technological advancement and how that might play out in our future history. But yeah I think
*  that that was in some way influential. I don't really know how but I would recommend it. I mean
*  if nothing else you'd be well entertained. When did you first yourself like fall in love with
*  idea of artificial intelligence get captivated by this field? So my honest answer here is actually
*  that I only really started to think about it as something that I might want to do actually
*  in graduate school pretty late. And a big part of that was that until you know somewhere around 2009,
*  2010 it just wasn't really high on my priority list because I didn't think that it was something
*  where we're going to see very substantial advances in my lifetime. And you know maybe
*  in terms of my career the time when I really decided I wanted to work on this was when I
*  actually took a seminar course that was taught by Professor Andrew Ng. And you know at that point
*  I of course had some kind of like a decent understanding of the technical things involved.
*  But one of the things that really resonated with me was when he said in the opening lecture something
*  to the effect of like well he used to have graduate students come to him and talk about
*  how they want to work on AI and he would kind of chuckle and give them some math problem to deal
*  with. But now he's actually thinking that this is an area where we might see like substantial
*  advances in our lifetime. And that kind of got me thinking because you know in some abstract sense
*  yeah like you can kind of imagine that but in a very real sense when someone who had been working
*  on that kind of stuff their whole career suddenly says that yeah like that that had some effect on me.
*  Yeah this might be a special moment in the history of the field that this is where we might see some
*  some interesting breakthroughs. So in the space of advice somebody who's interested in getting
*  started in machine learning or reinforcement learning what advice would you give to maybe
*  an undergraduate student or maybe even younger how what are the first steps to take and further on
*  what are the steps steps to take on that journey? So something that I think is important to do is to
*  is to not be afraid to like spend time imagining the kind of outcome that you might like to see.
*  So you know one outcome might be a successful career, a large paycheck or something, or state
*  of the art results on some benchmark but hopefully that's not the thing that's like the main driving
*  force for somebody. But I think that if someone who's a student considering a career in AI like
*  takes a little while sits down and thinks like what do I really want to see? What I want to see
*  a machine do? What do I want to see a robot do? What do I want to do and what I want to see a
*  natural language system? Just like imagine you know imagine it almost like a commercial for a
*  future product or something or like something that you'd like to see in the world and then actually
*  sit down and think about the steps that are necessary to get there and hopefully that thing
*  is not a better number on image net classification. It's like it's probably like an actual thing that
*  we can't do today that would be really awesome whether it's a robot butler or a you know a really
*  awesome healthcare decision making support system whatever it is that you find inspiring. And I think
*  that thinking about that and then backtracking from there and imagining the steps needed to get there
*  will actually lead to much better research. It'll lead to rethinking the assumptions. It'll lead to
*  working on the bottlenecks that other people aren't working on. And then naturally to turn to
*  you we've talked about reward functions and you've just given advice on looking forward how you'd like
*  to see what kind of change you would like to make in the world. What do you think ridiculous big
*  question what do you think is the meaning of life? What is the meaning of your life? What gives you
*  fulfillment, purpose, happiness and meaning? That's a very big question.
*  What's the reward function under which you are operating? Yeah I think one thing that does give
*  if not meaning at least satisfaction is some degree of confidence that I'm working on a problem
*  that really matters. I feel like it's less important to me to like actually solve a problem
*  but it's quite nice to take things to spend my time on that I believe really matter.
*  And you know I try pretty hard to look for that. I don't know if it's easy to answer this but
*  if you're successful what does that look like? What's the big dream? Now of course success is
*  built on top of success and you keep going forever but what is the dream? Yeah so one very concrete
*  thing or maybe as concrete as it's going to get here is to see machines that actually get better
*  and better the you know the longer they exist in the world and that kind of seems like on the
*  surface one might even think that that's something that we have today but I think we really don't. I
*  think that there is an unending complexity in the universe and to date all of the machines that
*  we've been able to build don't sort of improve up to the limit of that complexity. They hit a wall
*  somewhere maybe they hit a wall because they're in a simulator that has that is only a very limited
*  very pale imitation of the real world or they hit a wall because they rely on a labeled data set
*  but they never hit the wall of like running out of stuff to see. So you know I'd like to build a
*  machine that can go as far as possible. Runs up against the ceiling of the complexity of the
*  universe. Yes. Well I don't think there's a better way to end it Sergei. Thank you so much. It's a
*  huge honor. I can't wait to see the amazing work that you have to publish and in education space
*  in terms of reinforcement learning. Thank you for inspiring the world. Thank you for the great
*  research you do. Thank you. Thanks for listening to this conversation with Sergei Levine and thank
*  you to our sponsors Cash App and ExpressVPN. Please consider supporting this podcast by downloading
*  Cash App and using code LexPodcast and signing up at expressvpn.com slash LexPod. Click all the links,
*  buy all the stuff. It's the best way to support this podcast and the journey I'm on. If you enjoy
*  this thing subscribe on YouTube or view it with five stars on Apple Podcast, support on Patreon
*  or connect with me on Twitter at Lex Friedman spelled somehow if you can figure out how without
*  using the letter E just F R I D M A N. And now let me leave you with some words from Salvador Dali.
*  Intelligence without ambition is a bird without wings. Thank you for listening and hope to see you
*  next time.
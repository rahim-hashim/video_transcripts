---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 5371s
Video Keywords: []
Video Views: 2167
Video Rating: None
---

# Mother of Robots Keerthana Gopalakrishnan of Google Robotics
**Cognitive Revolution "How AI Changes Everything":** [March 30, 2023](https://www.youtube.com/watch?v=5tlQhgz-xuY)
*  That's why I'm so excited about robotics,
*  because it's like we are inventing ourselves.
*  It is in many ways a quest to understand us and our intelligence.
*  It's so hard to put down onto paper how we detect
*  like a cup or how we are doing these things or how we are planning tasks.
*  You know how software engineers say the best way to learn something is to build it.
*  I think robotics is basically our quest to
*  understand ourselves and build more of ourselves.
*  Hello and welcome to the Cognitive Revolution,
*  where we interview visionary researchers, entrepreneurs,
*  and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas,
*  and together we'll build a picture of how AI technology will transform work,
*  life, and society in the coming years.
*  I'm Nathan Labenz joined by my co-host, Eric Torenberg.
*  Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work.
*  Customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it,
*  and I recommend you use it too.
*  Use CogRev to get a 10 percent discount.
*  Kirtana Gopalakrishnan, mother of robots,
*  is a robotics and machine learning engineer conducting
*  advanced robotics research at Google AI,
*  where she's been an author on several of
*  the most influential papers of the last year,
*  including Seikan, which demonstrated that language models
*  can effectively act as the executive planning function,
*  or brain, of a robotic system capable of understanding and carrying out,
*  long horizon, abstract,
*  natural language instructions,
*  by assessing situations,
*  decomposing problems into parts,
*  and issuing logical next step commands for their robot bodies to execute.
*  Also, robotics transformer or RT1,
*  which demonstrated that the same large scale
*  pre-training paradigm,
*  which has recently delivered so many breakthroughs in so many domains,
*  can also work for robotics.
*  RT1 ultimately delivered a 97 percent success rate on some 700 different tasks.
*  It's a truism in Silicon Valley startup culture that it's easier to
*  manipulate and control bits than it is to control atoms.
*  Some have argued that the impact of AI will be
*  limited to digital domains as a result.
*  To me, Kyrithuna's work strongly suggests that this outlook is wrong.
*  Google's most recent release,
*  Palme, as well as OpenAI's GPT-4,
*  show that computer vision is still improving rapidly.
*  At this point, the combination of visual and language understanding
*  seem quite clearly rich enough to support general purpose robots,
*  suggesting that relatively few major conceptual problems,
*  including more general robotic control,
*  which Kyrithuna suggests we will likely achieve by
*  teaching robots to learn from watching humans,
*  still remain to be solved.
*  Barring an unexpected slowdown,
*  my takeaway from this conversation is that we should expect
*  many form factors of robots that can see,
*  communicate with us in natural language,
*  and solve basic problems on their own,
*  all in just the next couple of years.
*  At that point, the race to engineer and scale
*  the production of all sorts of robots will be on,
*  and shortly after, we'll begin to encounter them in factories,
*  offices, businesses, and even homes.
*  I enjoyed this conversation with Kyrithuna tremendously.
*  She is technically deep and we get into the weeds,
*  but she's also extremely thoughtful about how her work will affect the future,
*  and I very much enjoyed her thoughts on the big picture as well.
*  I hope you enjoyed this conversation with Kyrithuna Gopalakrishnan.
*  Kyrithuna Gopalakrishnan, welcome to the Cognitive Revolution.
*  Thank you.
*  Really excited to have this conversation, a lot to cover.
*  You have one of the best Twitter bios that I've seen,
*  Mother of Robots, and as soon as I saw that,
*  I was like, all right, we've got to get Kyrithuna on the show
*  and talk to her about everything that she's doing.
*  You've had quite a tour de force over the last year
*  and change as well in terms of having been an author
*  on some of the biggest papers in robotics,
*  and obviously, you've worked with an outstanding team at Google
*  to create that work, but really looking forward
*  to getting into some of the weeds on that.
*  You recently gave a lecture for the ML Collective,
*  which I have watched and definitely recommend.
*  One of the things that you said in that lecture
*  that really caught my ear was that we're somewhere between GPT-2
*  and GPT-3 in the world of robotics.
*  I wanted to just start by asking,
*  what does GPT-4 look like in robotics?
*  Or zooming out even more broadly,
*  how do you think we will integrate robots into our lives
*  as they get smarter and more capable over the course of, say,
*  the rest of the 2020s?
*  I'm very excited because we are seeing the type of scale,
*  learning at scale in robotics,
*  so which is similar to like GPT-3 for language.
*  So like we are seeing emergent capabilities in reasoning
*  and also in low-level control.
*  And the way that I see robots coming into our lives is,
*  definitely I think at robotics at Google,
*  we have cracked this recipe of like transformers for control,
*  language for interface,
*  and then foundation models for like reasoning.
*  I feel like this recipe is fairly generalizable
*  and extensible and has the potential to scale
*  with data and with compute.
*  So the way that I see robots coming into our lives is,
*  where humans interact with robots in natural language,
*  and the robots can do a lot of instructions in the real world,
*  and they can think and plan in visual language space.
*  So without being falsely precise in terms of like a specific date
*  for a prediction, does it seem realistic to you
*  that we are headed for a time within the decade
*  where we might have, for example, domestic service robots
*  that can like do the dishes for me after dinner,
*  or pick up the toys after my kids and put them away
*  when the kids don't do it?
*  What is this going to like actually look like in homes
*  or in places of business for people?
*  Oh, absolutely, I do.
*  In fact, the tasks that we train our robots
*  that we publish on are in office environments,
*  and like picking things and cleaning and everything.
*  In robotics, there is the problem of like,
*  a lot of demos that you see are like fairly staged.
*  If you look at like robotics technology,
*  there was like very traditional control,
*  like PID control and like search algorithms and stuff,
*  and then there was early deep learning,
*  like end-to-end deep learning,
*  but which was mostly like ConNets and everything,
*  and now there is transformers in robotics.
*  And so we are seeing like a curve,
*  and we are seeing that transformers are actually pretty good
*  at doing a lot of tasks with one model,
*  which is quite similar to how you are, right?
*  Like you can cook, you can clean, you can like plan tasks,
*  you can talk to your kids, like language generation.
*  So I feel like to build a robot that's like very useful
*  that goes into different people's houses,
*  it's going to be very generalizable,
*  and it's going to be one model
*  that's good at a lot of different things.
*  And we are kind of seeing those trends already.
*  The question is like, so we know it works
*  in like multiple Google Kitchens,
*  RT1 can do a lot of tasks,
*  but Google Kitchens are still very similar
*  and still a very small subset
*  of the total number of Kitchens
*  that people can see in the world.
*  So like, how do you scale fast enough
*  that you can bring the generality and complexity
*  of the real world into the models?
*  And where like, you bring that to my house,
*  and then it doesn't suddenly break down.
*  Yeah, it's unbelievable convergence
*  across kind of all the things.
*  We've talked to guests who are in computer vision
*  and who are just touching
*  all these different modalities,
*  and the same story is kind of underlying the progress
*  in all of them.
*  So no surprise to learn on some level
*  that that is also happening in robotics.
*  I think one of the things that you talked about
*  in your lecture and you kind of alluded to there
*  is just scale is starting to happen in robotics
*  as it has happened in other modalities.
*  But the data doesn't naturally exist, right?
*  That's like a huge difference between,
*  for language we have web scale data,
*  for we just did an episode on generation
*  of human-like voices,
*  and obviously there's a ton of voices out there.
*  I cloned my own voice.
*  It took only 10 minutes of audio
*  because there was so much pre-training.
*  But obviously that doesn't exist in robots
*  or for robots because we don't have all the robots.
*  They're not out there doing tasks in today's world
*  and collecting data.
*  So I was really interested.
*  I kind of dug in a little bit to the RT1 paper
*  and tried to get a sense for the work
*  that you guys have done to assemble the data set,
*  at least like beginning to approach the scale
*  that is needed to power this.
*  And I wanna get into that a little bit deeper
*  because I think that's something that people
*  probably have no real intuition for,
*  and you have lived it,
*  and put hours into helping to assemble that data set.
*  So maybe we could just like run down some stats
*  and then get like very kind of practical
*  in terms of what the data is
*  and how you're going about collecting it.
*  So you've got, this is from the RT1 paper,
*  700 tasks, 130,000 episodes,
*  which I take to be an attempt to complete a task.
*  You can definitely correct or refine my understanding.
*  Multiple different robot form factors
*  and a project that took a year and a half to complete.
*  I guess for starters, can you like just describe the robots?
*  There are a few videos out there that people can watch
*  to also kind of go see them.
*  What are these robots?
*  What do they look like?
*  How big are they?
*  What do they like to be around?
*  Tell us about the robots.
*  Firstly, a lot of questions here.
*  So let me go part by part.
*  The robots are really cute that we currently use.
*  So they are mobile manipulators.
*  They can drive and they have an arm
*  with a gripper at the end.
*  You can also like fit different tools,
*  like they can do wiping and other things.
*  And they also have like self charging
*  and other capabilities on top of that.
*  So they are really, and I think like they're a pretty good
*  and fairly stable stack and we have a fleet of them
*  and we have been collecting data on them.
*  And the 130K episodes used for RT1 are supervised launch.
*  So they are collected by a human tele-operating these robots
*  to do different tasks and over the seven.
*  So they will attempt all of these tasks
*  and then we train on that using supervised learning.
*  So now that brings you a question about like data
*  and language and vision and stuff.
*  So in language and vision, as you said,
*  there's a lot of free data available on the internet
*  that you can just take and then use
*  and then you're good to go.
*  But in robotics, like, okay, there's reasoning and planning
*  for which there is a lot of data
*  because it's similar to both humans and robots,
*  but for actions specifically, there is not that much data.
*  So that is one bottleneck in robotics.
*  And it is also like a very engineering bottleneck.
*  Like very few people can collect
*  and accumulate data sets of that scale,
*  which means that very few people,
*  like robots are expensive
*  and you need like a lot of engineering effort
*  to like orchestrate this large data farming operation.
*  So that already means that very few people can do robotics.
*  And also, which is why like, I feel like we at Google
*  who have the opportunity to do it are really,
*  we really have to, we really have a unique position
*  in scaling and making a dent in our attempt
*  towards solving robotics.
*  So I'm very excited about that.
*  But also, if you look at language and vision,
*  the acceleration in deep learning
*  was achieved by weekly supervised learning.
*  Collecting data using robots can only scale linearly
*  and only scale, especially with like human demonstrations,
*  it can only scale with all of humans.
*  But we wanna scale faster than that.
*  And so one way would be to get transfer
*  from human manipulation data.
*  For example, imagine how you would learn to surf
*  or cook something, you would take a YouTube video
*  and then you would watch it.
*  And there are a lot of YouTube videos
*  of humans doing a lot of things.
*  Imagine that like one day you wanna train,
*  like let's say an NBA level basketball player,
*  but who's a robot, you would not do like teleoperate robots
*  to do NBA level basketball or do self play.
*  Maybe you'll do a little bit of reinforcement learning
*  and specific fine tuning on top,
*  but you would make it watch all of the NBA videos
*  that humans have been playing all these years
*  and then you would try to get the robot
*  like scaled up to that point
*  and then collect a bunch of data
*  to like exactly fit to the robot's environment.
*  So transferring from human manipulation
*  to robot manipulation is a problem
*  that we haven't yet solved yet,
*  which I think is going to be very important
*  in really solving robotics.
*  So while humans cannot scale that fast,
*  robots can actually scale.
*  We can build like 50,000 robots.
*  It's just a question of money.
*  And then if robots can do autonomous collect,
*  then that's going to scale faster
*  than with supervised learning.
*  So how can robots do autonomous collect?
*  So one is like using these foundation models
*  to like collect data zero shot
*  or with a little bit of fine tuning,
*  like something like code as father says.
*  So let's build up those layers
*  in a little bit more detail,
*  starting with the supervised learning,
*  like the 130,000 episodes.
*  So if I understand that correctly,
*  you've got essentially a kitchen,
*  which is a lab on the Google campus.
*  And you've got robots that as of the time
*  that you're collecting these episodes are not AI powered.
*  They are instead remote control powered.
*  So somebody sitting there with like a PlayStation controller
*  going around and picking up napkins
*  and whatnot with the robot.
*  Is that actually like a reasonable picture
*  of what's happening?
*  Like a PlayStation controller type of interface?
*  Yeah, we have like Oculus controllers for these robots.
*  And then we have like multiple mock kitchens,
*  which are like, they are called robot classrooms.
*  Like the robot goes to a classroom and learn some things.
*  And then once they can reasonably do things
*  in the classroom,
*  then they are brought to like our actual kitchens
*  to do like stuff.
*  You know, I just did the most like naive math.
*  I just divided 130,000 episodes
*  by the number of work days in the year and a half
*  that the project took.
*  And I got 367 episodes collected per day.
*  So if I'm envisioning this right, it's like,
*  you must have, I don't know,
*  20 people who like have been operating the robots
*  and like doing the actual VR to robot housework
*  and collecting all the data.
*  And then I understand also that like the robot sensors,
*  you know, sort of robot proprioception, I guess,
*  if you will,
*  is also being just recorded at like each timestamp
*  along the way.
*  And once all that is done,
*  now you have kind of the, you know,
*  reasonably big data set for supervised learning.
*  So then your inputs would be the task or the command
*  or the instruction plus the imagery that was seen
*  at that given time,
*  plus like state of the robot at that given time.
*  And then the model is predicting next action.
*  How many like data points does that translate into?
*  Cause it's each episode presumably has,
*  I know you're running like multiple inferences per second.
*  So do you have a sense for what that 130,000 episodes
*  would translate into in terms of like example predictions,
*  so to speak?
*  Yeah, so it depends on the median task length, right?
*  So, and it also depends on what tasks, for example,
*  picking is something that is fairly fast.
*  And I think it's about like 30 steps.
*  So you have 30 actions to pick an object
*  and like something like opening doors is a longer episodes.
*  So because you have to like approach the door,
*  grab the handle, then open the door.
*  So let's say if we put a median around like 40 or 50,
*  let's say 50, 50 steps per episode,
*  then each step has around eight plus few,
*  like let's say 11 tokens.
*  So that's how many.
*  And then you multiply that with the number of episodes.
*  So it's like still way, way, way smaller compared
*  to like language and image datasets.
*  So we need to scale both by autonomous collection
*  as well as by like transparent.
*  Okay, cool.
*  So we've got the foundation
*  of all this manually collected data.
*  And now tell us kind of the outlook for the self collection.
*  So I'm kind of, you know, I do this with language models
*  where I'll try to get it to do a task, you know,
*  it sometimes does it, it sometimes can't.
*  And then I basically siphon off the data that is good,
*  that shows successes and like feed that back
*  into my fine tuning.
*  And, you know, I get better that way.
*  Probably a lot of our listeners are familiar
*  with that general kind of cycle.
*  How does that, is that basically what you're doing also
*  in robotics or what is the kind of, you know,
*  robotics twist on that?
*  So right now our system has like a high level
*  and low level control.
*  The high level control runs at like lower frequency
*  compared to the low level control is like much faster.
*  And the high level control, that paper is called FACAN
*  where a language model is deciding how to plan,
*  like what task to do in sequence.
*  So imagine something like, bring me a coffee.
*  So it'll be like, go to the kitchen, find a coffee cup,
*  pick up a coffee cup, place it on the counter
*  and then go to the coffee machine, press the button.
*  So like there's a series of steps to,
*  steps in natural language to do,
*  to achieve like a small task that you tell the robot to do,
*  which is like, go get me like a Coke can
*  from the fridge or something.
*  So there is a language model,
*  which is like planning how to do the series of tasks.
*  And then there is the robotics transformer,
*  which is executing each of the smaller tasks.
*  I'd love to just hear more examples of what the tasks are
*  and maybe your overall kind of impression
*  of where the robots are today in terms of,
*  like are they practically helpful?
*  Like if you had one at home, would it be worth it,
*  to have one at home at this point?
*  Or is it still more trouble than it's worth?
*  Like how close are we actually having something
*  that would be useful in the wild?
*  So it's not in the wild yet.
*  And that's one thing that we are working towards.
*  But the thing is scaling from five to 500 is quite hard,
*  but scaling from 500 to 5,000 tasks is easier
*  and 5,000 to 50,000 is going to be also easier.
*  Like each of them are like a different class of problems.
*  Like towards the end, you come to like more scaling
*  and distribution and inference at scale problems.
*  But initially you are like, you have algorithmic problems.
*  And I feel like we sort of more or less
*  have the algorithmic problems down.
*  So the tasks in RT1 are mostly like pick object,
*  place knock pick, open cabinets,
*  take things out of drawers and put them on counter,
*  also open fridges and clothes,
*  technically things that you can do in a kitchen.
*  And we also tried in like various Google Kitchens.
*  So it's like, yeah, if you take it to a new Google Kitchen
*  and make it run there, I think it should work.
*  But if you bring it to your house, I doubt it will work
*  because all the images kind of look
*  like it's very out of distribution.
*  I don't think it would generalize that much,
*  but Google Kitchens are still like somewhat similar.
*  Things are at similar heights and stuff.
*  So it should sort of work.
*  So then that is the question of like generalization, right?
*  And also like how many objects
*  or how many scenarios can we generalize to?
*  So the initial RT1, we wanted to focus on skills.
*  So we were like, we will do a lot of skills,
*  but a few objects.
*  So we only had like 17 objects.
*  Now, 17 objects are like too small, right?
*  You have millions of objects in the real world.
*  And in order to be realistic,
*  you need to be manipulating millions of objects.
*  So which was our recent paper
*  on like open vocabulary object manipulation.
*  So the idea there is that,
*  so imagine you can do 17 objects,
*  and then you collect a little bit of data
*  on about a hundred objects.
*  So generalizing from 17 objects to any objects is quite hard,
*  but generalizing from 100 something objects
*  to any objects is slightly an easier problem.
*  So this was like, yeah.
*  So what we did was use a visual language model
*  that can do a lot of zero-shot detection, right?
*  Like right now, language models can differentiate
*  between your faces.
*  Language models can say, hey, this is like a bottle,
*  or this is a phone, just from a zero-shot image.
*  So can we use that information to go manipulate that object?
*  And it sort of works reasonably well.
*  So what are like the high-end tasks?
*  You kind of gave verbs, you know,
*  of knock, lift, open, grasp, et cetera.
*  And then you also kind of talked about
*  the longer time horizon planning,
*  which I mentioned is still like pretty short.
*  Like it sounds like the things are, you know,
*  tasks that would be like 30 second tasks for a human.
*  But like, how far is that currently going?
*  Could the robot, for example, like actually make
*  and deliver a coffee with like actual hot coffee in it?
*  So we don't let them handle hot objects yet.
*  And they're also not good at operating machines yet.
*  But that's something like, because we didn't,
*  we just didn't collect data on it,
*  but that's something fairly doable and that you can learn.
*  They probably shouldn't be handling like hot coffee.
*  I doubt that that's probably like, I don't know,
*  like imagine you're carrying a hot coffee
*  and then there's like a kid nearby,
*  like something happens and then you splash it,
*  that's not good.
*  Or you just pour it over yourself
*  and then you break your electronics.
*  So if you think about tasks in a kitchen,
*  let's say when you're cooking and stuff,
*  you only actually do a finite number of skills,
*  but you are able to combine them in various fashions.
*  So if you do one, let's say you have 100 skills.
*  So which is like, let's say pick vegetable,
*  cut vegetable, wash them,
*  put them in plates like an aniseed.
*  So it's only finite number of skills,
*  but then let's say you have around 100 skills now,
*  and then you can then combine them in various ways.
*  So it would be like 100 CX where X is the number of tasks
*  that you wanna draw in order to do a high level sequence.
*  So something like make an omelet.
*  So that's like, I don't know, open the fridge,
*  take an egg, break an egg.
*  Even with like a finite set of skills,
*  you can still do a lot of tests in the real world
*  by combining them and a lot of like high level instructions.
*  We still have a lot of skills to go.
*  I think with RT1, the objective was,
*  how do we get an algorithm that shows like scaling limits?
*  So if you look at the scaling plots in there,
*  task diversity is very important.
*  RT1 doesn't seem to saturate
*  with the amount of data you throw in.
*  And in fact, it actually seems to like get much
*  and much better like emergence at like higher scales
*  and higher diversity.
*  And you can also increase the size of the model a lot
*  to fit the data.
*  If you imagine that you have to build
*  like a very generic robot manipulator,
*  you need data and you need a data absorber.
*  So in our office, we call it like a sponge and a firehose.
*  So a sponge is like, RT1 is a very good sponge.
*  And we are also building like better sponges there,
*  which is like, I don't know,
*  like VLM like foundation model transformers, right?
*  Which can transfer also like internet scale generality
*  into robot manipulation.
*  So like visual language models as manipulator,
*  like have you seen the PAMI paper, something like that.
*  So now imagine that you do have a data sponge
*  that you can put a lot of data and then it just learns
*  and then it does them in the real world.
*  Now the question is, how do you build a firehose
*  to like really pump it with like a lot of data?
*  So that's one of my main projects at Google.
*  So like how to scale autonomous,
*  but like also how to like mine a lot of data
*  from the internet.
*  Tell us more about that.
*  I mean, I'm understanding from your commentary
*  that you, it sounds like are kind of trying to base this
*  on video of humans doing stuff,
*  which this is always kind of an interesting pattern as well
*  where it's like a lot of times the hardest part
*  is figuring out how to cast the problem in such a way
*  that you actually have or can create or can sort of,
*  massage existing data into form where it can actually,
*  power the training paradigm that you wanna power.
*  So obviously there's a lot of data out there,
*  whether it's NBA basketball games or,
*  how to stuff of all kinds on YouTube.
*  I guess a couple of questions that come to mind there.
*  One is like, there's so many different possible forms
*  of robots that, kind of if I was thinking about this naively
*  I would think, okay, maybe I need, does video work
*  or maybe I need like a first person like POV,
*  GoPro type of view to make this work
*  because that might be a little bit more analogous.
*  Boy, there's so many different possible forms of robot.
*  Obviously you'd want this foundation model to like,
*  be able to adapt to all kinds of different form factors
*  or embodiments, if you will.
*  So I guess those are my two questions.
*  Like in the sort of pre-training,
*  do you think that like the third party point of view,
*  like the NBA basketball camera from the side view
*  is going to be enough to kind of develop the conceptual,
*  semantic understanding that you need
*  or is there gonna be kind of a need
*  for like more specialized point of view type thing
*  or something else?
*  And then second, is this kind of inevitably shaping up
*  to be like a two-stage thing where there's sort of first,
*  like building the representations
*  of what the humans are doing and then later,
*  like a bunch of adapters to specific forms.
*  What am I getting right and what am I getting wrong
*  is I guess there what that might look like.
*  So some of the things you can actually transfer, right?
*  Like let's say I see my mom cooking an omelet
*  and then from third person view,
*  and then I can try to cook an omelet
*  and I'm mostly successful.
*  But if I see Kobe Bryant playing basketball
*  and then I try to play at that level,
*  I'm not gonna be successful,
*  even though I have a very good modeling of my own body.
*  So I think it's going to be similar like that.
*  A lot of tasks, like whatever is easier,
*  you can learn by like third person watching,
*  but there still are tasks that you can only do
*  by actually practicing and improving your own control model.
*  We have some good work coming,
*  like I don't wanna speak about it before it's published
*  on like transferring between human and robot data
*  and also yeah, training larger VLMs for control.
*  Just the one that came out this week,
*  Palm E was pretty amazing, kind of inherent in that.
*  The big project is the E stands for embodiment, right?
*  So we're taking Google's kind of signature language model,
*  which has been adapted to seemingly every domain already.
*  I go on and on about MedPalm in other conversations,
*  but this is Palm E.
*  So kind of sitting at the center of this robot system
*  and having it do the kind of reasoning and planning,
*  pretty amazing.
*  Definitely picks up on another theme too
*  that we've talked about a few times,
*  which is the model to model communication.
*  If I understand correctly with Palm E,
*  the kind of auxiliary models are trained to inject
*  embeddings into the language latent space directly
*  without going through language itself, right?
*  So there's this kind of really interesting connectivity
*  that's starting to happen across these models.
*  That's something that we also talked to the blip authors
*  about and that's been a technique that they have used
*  in their most recent paper as well.
*  Translating these predictions to actual action in space
*  and accomplishing stuff,
*  that's very particular to robotics, obviously.
*  Can you kind of talk us through that half of the equation?
*  I think the key to building like a foundation model
*  would be data interoperability.
*  And if you look at Palm E, it converts images into tokens,
*  language into tokens and actions into tokens.
*  And once they are tokens,
*  then like a transformer can like operate on all of them.
*  And also if you really think about it,
*  the foundations of like thought is similar
*  in whether you are acting in language space
*  or vision space or action space.
*  And to get a globally optimal solution,
*  you need to think in all of these spaces, right?
*  Like if you are a person who's cooking or cleaning
*  or walking your dog or your kid,
*  you are thinking in both in language, in vision
*  and also with like your body.
*  So any solution that would be like a globally optimal
*  solution will be fully multimodal.
*  And I think eventually it would be like one model
*  to rule them all, to like does all the modalities together.
*  And specifically the way I think one of RT1's innovation
*  is tokenizing actions.
*  And at any given point of time, at least for the EDR robot,
*  we have like 11 variables for one to terminate
*  the episode or not and decide between arm and base control
*  and like around seven variables for arm control.
*  And for arm, we are only doing basically
*  where to put the end effector.
*  So end effector positions, end effector rotation
*  and how much to close the gripper.
*  So seven variables, three variables for position,
*  three variables for rotation
*  and one variable for gripper close.
*  And then for base, X, Y and the angle.
*  So three variables for base, seven variables for the arm
*  and one variable to decide to control base or arm
*  and then to also terminate the episode.
*  So once you like make your actions like tokens,
*  then it's just like vision tokens or language tokens.
*  Like it's actually kind of like a, it's very radical
*  when VIT came out, people were like,
*  oh, this is not gonna work because like,
*  how can you convert an image into language
*  as like a sequence of tokens?
*  Like language is a sequence of characters,
*  but then it works and it was able to bring us
*  like large multimodal VLM models like clip,
*  even stable diffusion, Dali and everything
*  which is built on top of like clip like models.
*  So then the question becomes like,
*  now can you also add actions in there like tokens?
*  Like now actions look exactly like language
*  and it's just a question of predicting like 11 tokens after
*  and you can do that for any robot.
*  And maybe another robot has like,
*  that has like more degrees of freedom,
*  like let's say imagine like a humanoid or something
*  and then you have a lot more variables.
*  So each degree of freedom can be like one extra variable
*  for the transformer model to predict.
*  And then it just becomes like,
*  can you predict the XYZ sequence?
*  That's how I think actions are going to be tokenized
*  and converted into data for transformers.
*  So at each step of inference,
*  the kind of core language model,
*  which is you're kind of projecting out in the future,
*  there might just be literally one big model
*  that takes everything in and it's one huge black box.
*  But for now we kind of have some auxiliary models
*  that like do the vision part
*  and kind of feed that into the language.
*  And I looked at the Paul Mead paper,
*  there's even like a couple of different types of language,
*  of vision model, excuse me, that object segmentation,
*  general scene description, depth mapping, whatever,
*  like all these kinds of different things come in together
*  into the language model, along with of course,
*  what are we trying to do here?
*  What did the human ask us to do?
*  And then what is spit out the other end is 11 values,
*  which say, and was it either or like,
*  you're either gonna do something with the arm
*  or you're gonna do something with the base?
*  So RT1 is like that, but our next models
*  are going to be whole body control.
*  So which means that you move both of them together.
*  If you really think about how you do your control,
*  you are not either moving your arm
*  or your head separately, right?
*  At any given point, you move them together.
*  So yeah, that's going to be fixed.
*  So there's kind of a couple,
*  I'm understanding like a couple of different paradigms here
*  or ways that this could work.
*  One would be that the language model says like,
*  okay, based on what I'm seeing
*  and what I'm trying to accomplish,
*  I want to move the base to position X and Y.
*  Okay, cool, we got there.
*  Now, next time I want to move the gripper to position XYZ
*  and have a certain angle and have a certain open close.
*  How does the sort of issuing of that command
*  relate to the cycle time?
*  Because I would assume that like,
*  you can only accomplish so much
*  before you're gonna be kind of
*  running the whole process again.
*  So that's like the action bound, right?
*  The language model basically predicts a token
*  and the token is like a value between like zero to 256.
*  But each of those numbers correspond to like a certain bound
*  between no action versus go forward or backward.
*  The language model is predicting still
*  within like a bounded space of action
*  that you can go to or not.
*  And in RT1, the inference time was 100 milliseconds.
*  And then the full stack time was 300 milliseconds.
*  So that's like three hertz control.
*  Humans are a lot faster than that.
*  And yeah, we know that we need to optimize it
*  but these are research robots,
*  which is why the stack is slower.
*  But production robots would be like a lot faster than that.
*  And also, let's say assume that once the language model says
*  go to XYZ position or whatever,
*  and we are doing concurrent or non-blocking control.
*  So what that means is that after the language model
*  tells the robot to go move to that position,
*  the next cycle of inference does not wait
*  until after that action is executed
*  to start the next step of inference.
*  So there is a thinking cycle, which is going,
*  and then there is an executing cycle, which is going.
*  I mean, this is also like how you do it, right?
*  Like you don't wait until, let's say,
*  you grab something to think about
*  what is the next thing to do.
*  So thinking and acting are happening simultaneously.
*  And it is also important for robots to be fast
*  because like there are moving objects.
*  Let's say if your kid throws your ball,
*  you need to be dynamic.
*  And if you are slow, if your control is too slow,
*  if you move like that,
*  then you're not gonna catch the ball.
*  So which means that it imposes certain limitations
*  on the latency of the whole system.
*  So one of the ways in which we tackle that
*  is by using the token learner,
*  which is like really compressing the tokens
*  from the pre-trade efficient net.
*  And so that the inference times are faster
*  and that cuts the inference time like one third.
*  And also in language models,
*  it's like everyone is excited about
*  like really, really big models.
*  But scale comes with emergent properties
*  and scale comes with like large reasoning abilities.
*  But then that also means makes inference slower.
*  So they are sort of like competing objectives.
*  So we want fast control,
*  but we also wanna fit as much information,
*  as much context as possible.
*  And definitely like in the future,
*  our hardware, our inference hardware,
*  all of that is going to be much faster
*  and optimized for transformer inference.
*  But right now there is still that competing objectives.
*  Okay, that's really helpful.
*  And I think likely very clarifying for a lot of people.
*  If I understand correctly there too,
*  like the command, I guess, right?
*  The predicted command of go to XYZ,
*  that's explicit enough, I gather,
*  that it can be just sent directly
*  to the robot control system for execution.
*  But then with the latest paper with PalmE,
*  it sounds like there's a bit of a different architecture
*  where it's starting to,
*  instead of saying like go directly to XYZ,
*  it's giving like slightly higher level commands
*  that are then received by
*  and translated into actual action or motion
*  by another model within the same system.
*  So can you describe that version as well?
*  And then maybe like the pros and cons,
*  like why, is that just a strictly better approach
*  or do they have trade-offs?
*  Yeah, so actually PalmE and RT1 work together.
*  So PalmE is like the updated Secan,
*  which is a converting high level language
*  into low level language.
*  So converting between like how to go get coffee
*  and then planning that with like feedback
*  from the system and everything.
*  And then RT1 is doing the little things
*  like pick up the coffee cup.
*  So I think two models are like optimizing both of them
*  synchronously is suboptimal compared to having one model
*  do both planning language generation and inference control.
*  And I think like that is the way
*  that we will go in robotics.
*  You'll see future papers from us which go in that direction.
*  Yeah, so PalmE is more like Secan level,
*  like reasoning about the environment,
*  but also it is also doing like affordance.
*  It is also doing like scene feedback.
*  And RT1 is doing the exact actions.
*  PalmE, the successor to Secan will take in
*  everything that's going on,
*  which includes my having told it to get a cup of coffee
*  and its knowledge of its position and state
*  and its visual input.
*  And then it will translate that to a low level command
*  that is like grab the cup.
*  And then RT1 takes that input in
*  and translates that to X, Y, Z coordinates for the gripper.
*  What does sound nice about that architecture is
*  you could have like RT2, three, four, five, and six
*  for different kinds of robots, but does RT1,
*  it already handles multiple different types of robots
*  as well, right?
*  So is that just like a variable within the bigger thing?
*  Like what kind of robot arm you're actually controlling?
*  Is that just another token that's in the input
*  or how does it kind of know which embodiment
*  it is controlling at any given time?
*  So it has another input.
*  So when RT1 was jointly trained with KUKA and with EDR,
*  it was told where like the data came from
*  and the action spaces were also sort of mapped together.
*  Yeah, so one way that you could compose like a one model
*  on like multiple robots is like using one token
*  to determine like which robot you're inferencing on.
*  So let's say, imagine like if you're running like a robot dog
*  and then you have one token saying this is a robot dog,
*  which means you predict like, I don't know,
*  maybe 24 variables versus if it's like the everyday robot
*  that we are doing, then just predict 11 tokens.
*  That's one way where you can like still mix
*  a lot of different data from a lot of different robots
*  and then also have like transfer between them
*  while allowing it to influence on a lot of different robots.
*  One of the videos that I thought was most striking from
*  was an example of where there's these sort of exogenous
*  shocks to the robot's plan.
*  For example, there's one video where the robot is picking up
*  a bag of chips out of a drawer and then the human comes in
*  and knocks the bag out of its hand
*  and puts it back in the drawer.
*  And so it's a demonstration of the fact that
*  the language model, especially as it's informed
*  by the visual inputs, obviously it's not having
*  these conscious thoughts of like,
*  oh, somebody knocked this thing out of my hand,
*  but it is realizing the bag is over there
*  and I need to go back and get it to pick up my,
*  to accomplish my objective.
*  That's a pretty striking video.
*  There's one with pizza being made as well
*  and sauce being kind of smoothed around on the pizza.
*  And the person comes and moves the pizza
*  and the robot recognizes that and continues
*  to apply the pizza sauce appropriately.
*  So I was like, boy, that's pretty awesome.
*  Then I was also thinking,
*  what is the limit of how much perturbation
*  I would want a robot to sort of push through
*  in the real world?
*  You know, and I have a four-year-old kid
*  and a two-year-old kid and another new baby coming in,
*  let's see, 25 days.
*  You know, it's definitely a very common occurrence
*  in our house that I'm trying to do something.
*  And then, you know, there's a shock of a kid
*  entering the scene and, you know,
*  messing something up or whatever.
*  How are you guys thinking about sort of a,
*  okay, this is sufficiently big of a shock,
*  you know, that we did not,
*  that the model did not expect
*  that maybe it's time to just stop.
*  You know, like I should not pursue this goal anymore
*  because something is happening that like, you know,
*  is out of distribution and I don't know what to do with it.
*  Again.
*  So these are like ethics questions, right?
*  So it's like not a question of can you do it,
*  but should you do it?
*  And it's also like very similar to like safety questions.
*  And here our straightforward approach is to borrow
*  from like AI safety, AI alignment research.
*  So one way, like we are running a lot
*  of autonomous scale operation.
*  So like where the robots run around
*  and then they propose what tasks to plan to practice
*  and then autonomous policies then try to attempt
*  to practice those tasks.
*  But now the question becomes like,
*  imagine the robot is roaming around people's desks.
*  It should not attempt to pick up their personal belongings
*  or if people are sitting in the Google MyToolKitchen,
*  it should not come near them and then like try
*  to disturb them or like propose any tasks
*  that is harmful for them.
*  So like, for example, one of the days there was the robot
*  that we were planning and it detected
*  that there was a phone in my hand
*  because I was recording it and it was like,
*  take the phone and then pick up and then put it on the table.
*  But the phone was sitting in my hand as a human
*  and I would not appreciate it if it just like grabbed
*  the phone from my hand without any consideration
*  for like how humans behave, right?
*  Like before you take my phone from my hand, firstly,
*  you need to understand that the social norms
*  do not grab people's phones from their hands.
*  Secondly, you would ask for these things.
*  So there's a lot of like HRI components in there,
*  which is like how can robots be like nice and polite
*  even in social interactions?
*  And we have a group that is working on HRI research,
*  which is like thinking about like how to make the robots
*  polite, how to make them reason contextually
*  about these things.
*  Like for example, in this failure mode,
*  the robot detected a phone in the scene and proposed a task,
*  but it did not detect that the relational aspect
*  of the phone being in my hand
*  and the fact that I was holding him.
*  If we have better scene description,
*  I think a language model would be able to reason
*  that the phone is in the hand of a person.
*  So then, you know, don't do that.
*  And so currently our approach to safety now
*  is asking a language model, like should you do this or not?
*  We also have like for tasks like collision and stuff,
*  we have like more harder bounds,
*  like it would not do tasks that actually have collisions,
*  even if the language model plans and everything,
*  it is still like bounded.
*  It should not be like dropping objects
*  or like colliding into things.
*  So there is a hard bounding from a control perspective,
*  which is just like don't run into anything.
*  Then there is the question of like asking a language model,
*  is this a safe task to do?
*  Is this a nice task to do?
*  Or if not, can you explain to me why this is something
*  that you should not attempt to do?
*  So some of the tasks,
*  it's like our robots right now have only one hand.
*  So when it is given a task that requires two hands,
*  then it should be like, I'm not able to do it
*  because I don't have two hands.
*  Or if it's asked to lift a heavy object
*  that's about its payload,
*  it will be like, this is unsafe for me to do
*  because it's a heavy object.
*  Or if you say like pick up the thing with the hot coffee,
*  it'll be like, this is a very hot object
*  that I should not be handling.
*  So maybe you do it.
*  So like, so, and then, so now here we come into the realm
*  of collaboration between a human and a robot,
*  where the robot is closing the loop in itself.
*  The robot knows what it should do, what it shouldn't do,
*  what it can do, what it can't do,
*  and also how to be nice while doing these things.
*  And now, so once it determines,
*  once it can classify these things,
*  now the question is like,
*  you should still be able to get the coffee to the human,
*  even if it's hot coffee.
*  But if you are not able to handle that,
*  if you think you're not safe enough to handle that,
*  then you need to re-plan and reason about
*  how to still get that task done.
*  So one way it could be, you can like chat with the robot.
*  Our robots have like a chat interface.
*  You can tell the robot back, the human back,
*  hey, look, I have the hot coffee in there.
*  Can you come help me pick it up?
*  So that is the realm of like collaboration
*  and or like intervention.
*  So I think deploying robotics in the wild
*  is not going to be with fully autonomous policies,
*  but with autonomous plus interventions.
*  So like how self-driving cars are, right?
*  They are good for handling,
*  autonomy can handle like 95, even 98% of cases.
*  But those like, those 2% of cases were like,
*  or even 1%, if you run at like 10 hertz in front
*  and you have 1% mistakes,
*  you are making a mistake every 10 seconds.
*  And that's like highly unsafe.
*  So, but what the self-driving cars are good at
*  are knowing where they're good at and where they are bad at.
*  And they can ask a human for help
*  when let's say the map doesn't make sense
*  or like there's a person there saying,
*  asking the cars to go around.
*  So similarly, I think that the way that robots
*  will be deployed is like,
*  they know their bounds of operation
*  and they also can ask a person for help
*  when they are confused or when they can't do something.
*  And they also have like hard bounds around them,
*  like common sense things like,
*  don't hit a child or like don't run into things.
*  And even if a language model somehow plans
*  like hit a child or whatever,
*  then you still have like safety on robot,
*  like control, which is not a machine learning model,
*  which is deterministic control
*  that says like, don't run into objects.
*  That sounds like for one thing,
*  kind of another percolation labor to collect all that data.
*  Cause that's another level that doesn't really exist, right?
*  Or maybe you're in the process of collecting it now,
*  but there's not really a lot of examples,
*  certainly out there on YouTube or whatever,
*  of robots running into situations where they,
*  determine that like they can't do the task.
*  So definitely I think that we will get a lot of transfer
*  from a language model,
*  like all the work that people are doing for alignment
*  and safety of language models and other,
*  now with like GPT-4 or multimodal models,
*  like don't generate harmful output,
*  don't ask it to do harmful things.
*  So that's definitely going to feed directly
*  into our research that's there.
*  But we also need more information
*  about the specific failure modes of our data,
*  of our problem.
*  And once it is close to productization,
*  so you know, like how Waymo or like self-driving companies
*  have their simulators to test for safety related things.
*  They also have like human in the loop,
*  which is like constantly testing the hardware.
*  So I think all of those things will come in.
*  But robotics especially has like a particular imposition
*  which is that language models can be wrong on the internet.
*  Right? You ask Chad GPT something, it goes wrong,
*  no problem.
*  Or it says something weird, no problem.
*  But then if you make a bad plan,
*  if you like drop an object, you break things,
*  you cost money and you probably injure a person
*  or destroy an object, which is,
*  so there is a higher penalty of failure on robotics models,
*  which is going to be very important
*  towards their safe deployment.
*  I don't think that this is an impossible problem to solve.
*  Look at self-driving cars,
*  they're already making money in San Francisco.
*  So it's just a question of us doing it carefully
*  with human in the loop and then rolling it out in phases.
*  Yeah, initially everyone was like self-driving cars
*  would never work because they can never solve
*  100% of the problems.
*  They're always gonna be long tail and whatever.
*  But yeah, you don't have to solve the long tail.
*  You can solve as much as you can
*  and then you can make humans solve the rest.
*  So you're basically doing intervention.
*  Assume that the robot already works,
*  like start making money today
*  and then keep solving the problem,
*  then reduce the intervention rate.
*  So then that becomes your whole problem.
*  I think bringing robots to people's houses
*  will also be like deployed today
*  with whatever capability you have
*  and then use humans to fill the gap
*  of your algorithms right now.
*  And then as you go, as you make money,
*  as you keep improving, slowly phase it out.
*  It's funny you mentioned the self-driving cars too.
*  I just took a ride in my neighbor's Tesla
*  that has the full self-driving enabled
*  and I came away from that feeling like,
*  first of all, just pure wow.
*  It really does work amazingly well.
*  And also like nobody seems to be acknowledging it.
*  It's this odd, as you said,
*  people say it's never gonna work.
*  Like you can still go online today
*  and find recent articles.
*  Probably we can find one from today
*  that says FSD is never gonna work.
*  But I just wrote in one
*  and it definitely is a lot farther along
*  than some of the naysayers would suggest.
*  So it sounds like robotics from this conversation
*  is probably in a similar position.
*  I wanted to talk a little bit more
*  about kind of the hard bounds
*  because that also is something that seems,
*  as you just kind of spoke about,
*  much more important in the robotics paradigm
*  than language models or others.
*  One article, just for listeners, that I really recommend,
*  because I can go back to it repeatedly
*  just to kind of meditate on how I work as a human
*  is this Scott Alexander book review
*  of a book called Surfing Uncertainty.
*  We could put the link in the show notes.
*  But basically he kind of talks about how the human,
*  like biological nervous system,
*  just has like a ton of layers.
*  And you've got like the prefrontal cortex layers
*  are kind of the highest layers
*  that deal with the highest level of abstraction.
*  And then obviously, you know, radically oversimplifying.
*  But as you kind of go down the nervous system
*  all the way out to the periphery,
*  there's just like layer after layer.
*  These are probably not discrete layers,
*  but to some extent there are discrete cells.
*  So there is some amount of discreteness to it.
*  Anyway, whatever.
*  It's not meant to be too literal.
*  But as you get out to kind of the periphery,
*  you have just like very low level interpretation
*  of what's happening.
*  And you can do things like remove your hand
*  from a hot stove before there's certainly
*  any conscious thought of the hot stove.
*  So all of that, you know,
*  and I highly recommend that article,
*  all of that to just kind of preface like,
*  it seems like robots need something similar, right?
*  Where they need to sort of detect that like,
*  I'm encountering resistance, you know,
*  or like the thing that I'm grabbing is like deforming
*  in my grasp more than I expected it to,
*  or more than it seems like it should.
*  And therefore I need to kind of back off, right?
*  I need to like slow down.
*  I don't necessarily wanna wait for the next inference cycle
*  to withdraw pressure or, you know,
*  back off of a collision or whatever.
*  So how is that working today?
*  Is that like a non,
*  something more of like a classical system
*  that's not AI driven, or is that also, you know,
*  something that the models are ultimately gonna handle
*  in your view?
*  Like what's the future of that look like?
*  So let's go back to the example
*  of the touching the hard object, right?
*  So there is like the planning in our body,
*  which like goes to the brain and the spinal cord
*  and whatever, and then tells you
*  that you should not touch the hard object.
*  But then when you touch a hard object
*  and then you reflectively act,
*  you are not going all the way to run the inference step.
*  This is what I was previously talking about
*  by various layers of safety.
*  There is one layer, which is the language model telling you
*  should you do it or not, don't touch hard objects,
*  don't handle whatever.
*  But there is also like low level control layer.
*  RT1 also has its own like safety.
*  It will not do like highly unsafe things
*  because it doesn't have the data
*  and it is like the data is cleaned and everything.
*  But also on the robot, on the control level,
*  just like the C++ code,
*  there is also a way to determine like,
*  don't do collision related stuff,
*  like don't run into objects.
*  And that's very easy to detect.
*  Like you know the occupancy in space,
*  don't deform the object, like don't run into things.
*  But also more than just collision,
*  there's various other types of feedback,
*  which is like tactile sensing.
*  It's like, as you said,
*  if you try to pick up a full bottle and I don't know,
*  like if it deforms a lot, then maybe don't do it.
*  Or if it spills over, don't do it.
*  So right now our robots don't have tactile feedback on them.
*  So like with the gripper,
*  so it knows some like, it has some pressure feedback.
*  So if it's like a very hard object and then you squeeze it,
*  you won't be able to squeeze it.
*  And that's reflected in the like the max torque
*  applied onto the thing.
*  But then there's also like more softer feedback,
*  like to like cut like vegetables or like soft objects,
*  like tomatoes and stuff,
*  you need more finer feedback, which is not there yet,
*  but then we can still do a lot.
*  We can still deconstruct safety into various layers
*  with existing like just force feedback.
*  So that I think that's reassuring that there's like some,
*  that it's not fully a black box,
*  that there is this kind of C++ safety layer
*  that is like a hard override
*  and zooming out just a little bit more still
*  and just kind of like returning to some of our,
*  very early discussion around how we'll interact with robots,
*  what kind of role they are gonna play.
*  How fast do you ultimately think we will want robots to be?
*  As I watched the videos,
*  it is notable that they run pretty slow today,
*  certainly like much slower than humans.
*  Like the videos are typically shown at like either 4x speed
*  or 10x speed, I've seen both.
*  So they're pretty slow in today's world.
*  Obviously you'll wanna speed them up.
*  But I wonder if you have like a sense
*  for what the optimal frequency is for a robot
*  to be operating at in a human environment.
*  There might be a maximum at a certain like
*  human like frequency that would be sort of accessible.
*  You know, if we could run them at a thousand Hertz,
*  I'm not sure that we would even really want to.
*  Frequency of inference is not the only variable for speed.
*  So frequency is, think of frequency as how reactive you are.
*  So even if you're running inference a lot,
*  but each step you can only move a little bit,
*  then let's say to go to here,
*  you're gonna let's say run like 10 inferences,
*  but then you can also go to here in one instance, right?
*  So there are two variables to control here.
*  One is how reactive you are and your inference frequency.
*  But second is also like how much movement you are allowed
*  in each inference step.
*  Time to complete a task is within 2x or 3x
*  of what a human would take for that task.
*  And then that is about optimizing both the machine learning
*  on robot software and also optimizing for both reactiveness
*  as well as speed.
*  We didn't play around with speed a lot
*  because it can be a little bit dangerous, right?
*  You're trusting the inference a lot,
*  but I think because these are research robots,
*  we haven't really optimized all of these things a lot.
*  When they come into production,
*  then that becomes a more important question.
*  But I think it's fairly solvable still
*  with existing machine learning models and existing robots
*  to get at least like within 2x of a human.
*  Yeah, robots, you would be freaked out
*  if a robot were as fast as you in doing things, right?
*  And as good as you.
*  I think it's fine to give them a little bit more time
*  until they like, I don't know, ease into society
*  and people are like okay with them.
*  Yeah, totally.
*  I agree with that for sure.
*  I have a, the most advanced robot in my home right now
*  is the Roomba and it's kind of stumbles its way
*  and crawls its way around the house.
*  It's not too smart and doesn't figure things out too quickly,
*  but it kind of feels appropriate.
*  And like we run it overnight.
*  So it's one of these things too where it's like,
*  it doesn't really matter if it takes it an hour or two hours
*  or whatever, five minutes.
*  It wouldn't be much better for me
*  if it was a five minute task for the robot
*  instead of an hour.
*  Honestly, it probably wouldn't be any better for me.
*  So yeah, I do think you're right.
*  But it is also interesting to hear that perspective
*  that increasing the frequency of inference
*  really just smooths the behavior
*  as opposed to really changing the behavior.
*  And then you have a separate decision to make around like,
*  okay, per unit time, whatever that interval is,
*  how much am I going to move in that unit time?
*  So that's something you can kind of control independently,
*  which is, that's helpful
*  because I hadn't really conceived of it in that way.
*  What are they like to work with?
*  Like, do they break a lot?
*  Do they need maintenance?
*  Are they heavy?
*  Like how robust are these robots
*  that you are currently working with?
*  So I've worked with space robots.
*  Like when we were in grad school,
*  we sent a little robot to the moon.
*  I have worked with like self-driving cars
*  and I've worked with everyday robots.
*  And I think these are the most stable,
*  at least at the fleet scale they have.
*  And they're fairly robust,
*  like the navigation stack and everything
*  is fairly reliable.
*  They don't break as much.
*  They don't run into objects, like everything works.
*  And I think it's because like Google's
*  really good at engineering.
*  And we also have like great ops folks
*  who are like keeping everything like,
*  it's like oiling the machine, right?
*  Like, and yeah, they are fairly robust
*  and fairly good robots so far.
*  I think they don't break easily
*  and it's very convenient to like run experiments on them.
*  We still have a long way to go
*  with like solving smaller issues and stuff,
*  but I think they are the best robots
*  that I have worked with so far.
*  And another thing is that like,
*  you see industrial robots, right?
*  They are also fairly robust,
*  but they are very constrained environment.
*  Like it's like fixed base,
*  it's like doing picking or like it's like doing scanning,
*  but these robots also move around.
*  So compared to the complexity of the domain
*  that they operate,
*  I think their reliability is really good.
*  Do you think that they are the right form factor
*  for like ultimately, you know, use in homes?
*  I think form factor is a very, very important question.
*  And there's a lot of like debate among roboticists
*  on like what is the ideal form factor.
*  Initially, a lot of robotics was like fixed base.
*  So they were just like these KUKA arms and stuff.
*  They would just like do things from a fixed location,
*  but this is not very general robotics,
*  which is why we now have like arms moving around,
*  but the arm is the most costliest part of these robots.
*  So if they have like two arms,
*  then the robots is going to be almost twice as expensive.
*  And then the equation,
*  the economic equation would not work out.
*  So there are like various ways.
*  So cost is one trade off.
*  Up until this point, we were limited by the robot software.
*  And so if you cannot even do one hand task,
*  then it doesn't justify having multiple hands and legs
*  and whatnot on the robot, right?
*  But now we are seeing that we are limited.
*  The robot capabilities have increased to a point
*  where we are actually limited by the,
*  we are limited by the hardware.
*  So we have cracked a paradigm where it's like throw data
*  and then just learn it.
*  So then the question is like, how much data can you throw?
*  And then on which robot should you throw the most data?
*  And I think that if you really think about it,
*  if you really think about like the ideal generalization,
*  like a superhuman physical intelligence,
*  it's probably going to look like human race, right?
*  Because our world is designed for humans.
*  Like your kitchen is designed for humans.
*  A car is designed for a six feet human.
*  And a cup is the dimensions of this,
*  like what fits in my hand.
*  A lot of the data on YouTube is from like
*  a human egocentric perspective
*  with like human hands operating.
*  So if you look at it from a design of the world perspective,
*  then humanoids are the most optimal form factor.
*  If you look at it from a data perspective,
*  like NBA basketball agents playing, they look like humans.
*  So then, and you probably need like a human-like form
*  to play very good basketball, right?
*  Both from a data and a utility perspective.
*  Humanoids, I think, are the ultimate form factor for robotics.
*  But if you really think about it,
*  stability is a very, very hard problem to solve.
*  And Boston Dynamics has like really, really complex robots,
*  which all of them are like robots.
*  But stability is a very hard problem to solve.
*  And then that means that all of your problems
*  become stability problems.
*  While you are like picking things up,
*  you are also worried about like falling.
*  And if you do fall, you are a danger of breaking parts
*  or injuring other people.
*  So I think that one of the reasons that Boston Dynamics
*  has like little stubs for their arms
*  is because like they invested into legs too soon.
*  And then now all their problems are stability problems.
*  So initially it was one arm on fixed-based robot,
*  then one arm on mobile-based robots.
*  And like now we have navigation and manipulation together.
*  I think the next is like bimanual manipulation.
*  A humanoid on wheels is basically two arms
*  and a camera at human height, right?
*  It's not like, it sounds so complex,
*  but it's actually just two arms and a camera on wheels.
*  So I think that would be the form factor
*  for a lot of like indoor and office applications.
*  Like most homes nowadays have like,
*  most offices have like elevators and stuff.
*  And for most robots, like if they're on the floor,
*  they can do a lot of things.
*  And then the next step would be like leg robots,
*  which adds an additional level of complexity, right?
*  Because imagine that you do build
*  a superhuman intelligence and then it goes to deliver,
*  but then it can't cross a little curb
*  on the in front of your door.
*  So you need legs to like go upstairs or go past curbs
*  or even to do like outdoor robotics.
*  So humanoid on wheels would be the next version
*  with two arms, then would be like legs
*  and also are like fingers, like five fingers
*  would be another upgrade because a lot of things
*  you can do with just grippers,
*  but then fingers are highly complex.
*  Like we have so many degrees of freedom in here
*  and it's highly complex to plan and stuff.
*  But ultimately a lot of the tasks
*  would need more finer dextrous manipulation.
*  As you're describing that, I have this kind of image
*  in my mind that's like analogous to the human evolution
*  where it starts with like the great ape or whatever.
*  And then it gradually sort of becomes more,
*  to human over like six steps.
*  You basically just described the six steps
*  that goes from one arm to the ambulatory robot.
*  It's a pretty similar evolution, so to speak.
*  That's why I'm so excited about robotics
*  because it's like we are inventing ourselves, right?
*  It is in many ways a quest to understand us
*  and our intelligence.
*  And it's so hard to put down onto paper why,
*  how we detect like a cop or how we are doing these things
*  or how we are planning tasks.
*  Like at least high level things
*  you can like describe in language,
*  but low level manipulation, low level influences,
*  you really cannot like why your arm and leg
*  are moving in a certain way, you cannot.
*  But then building like, you know how software engineers say
*  the best way to learn something is to build it.
*  And I think robotics is basically our quest
*  to understand ourselves and build more of ourselves.
*  If you think about GPT and language models are doing a lot
*  with respect to like scaling intelligence, right?
*  And bringing down the cost of knowledge work.
*  Like if you think about it,
*  industrial revolution has automated a lot of mechanical labor
*  that our lives are much easier.
*  And now with the intelligence revolution,
*  we are like automating a lot of knowledge work.
*  But then truck drivers in the United States make like 200K
*  because no one wants to drive trucks.
*  Even like people that like sand boats apparently
*  in San Francisco makes like $95 an hour.
*  And which is like, you know,
*  comparable to a software engineer.
*  So as the availability of labor changes,
*  once like more knowledge work gets automated,
*  physical work is going to be the most valuable.
*  Like when my friends ask me like,
*  oh, software engineers are getting automated,
*  artists are getting automated.
*  It's like the more of a paradox, right?
*  The things that we thought were hard to do
*  are actually easy to do for computers.
*  But the things that we find are easy to do are really hard.
*  Like for us, like composing these images
*  and stable diffusion is like super hard
*  and editing those things.
*  But then computers apparently can do that.
*  But something so easy as like going to my kitchen
*  and make me a coffee or like take my dog for a walk
*  that we take for granted.
*  We think it's so easy.
*  It's like really, really hard for computers to do.
*  So, but physical labor still accounts
*  for a large portion of our GDP
*  and automating that has like a lot of economic opportunity.
*  And I think eventually, if we think of like our species,
*  like really going forward and capturing different planets
*  or expanding ourselves,
*  then definitely solving both AGI in the digital world
*  and AGI in the physical world
*  is going to be very important.
*  We had Sue Hale from Playground,
*  which is a image creation service
*  that people are obsessed with.
*  He has a young child as well.
*  He said, you know, maybe my kid, who knows?
*  Like maybe some of their best friends will be AIs.
*  And then we also had Eugenia Koida from Replica,
*  which is the like, you know, virtual friend app
*  that, you know, is all digital today, you know,
*  which people are already falling in love with.
*  And that's become like a big challenge for her
*  because people are doing like, you know,
*  erotic role play in the app.
*  And she's like, you know,
*  I might have problems there in any number of ways.
*  So they just kind of dialed that back
*  and they had a bit of a backlash from users
*  because people really care about that stuff
*  as they become attached to it.
*  Does it, is there anything that's like blocking
*  in your mind the sort of extension of, you know,
*  when I think of this,
*  I just think of like picking up the toys.
*  And I'm like, that's where as far as it goes,
*  typically in my imagination.
*  But then, you know, when I think of Suhail and his kid,
*  and I think of Eugenia and all her users,
*  it's like, boy, are we gonna have robots
*  that are like playmates to our kids?
*  Are we gonna have robots that are like robot spouses?
*  We are gonna have them.
*  Like in our lab, like on days like I'm like driving to work
*  and then I have booked like two robots
*  to like play with me the whole day.
*  At the end of the day,
*  and you get close to these robots, right?
*  Like you are like, this meta or this one,
*  they have the numbers at their end.
*  And then you're also like, at the end of the day,
*  I like cracked one robot's wrist
*  because like I moved the chair against it.
*  And then you spend the whole day with it.
*  And then you're like, okay, I had to like file a bug
*  to take it to like it's like a hospital kind of service
*  that they have where they fix the arm.
*  But like, I felt like so bad that I broke the robot,
*  but the robot would never understand
*  that I'm actually sorry.
*  And I would not even, the robot never told me that it's okay.
*  But a human, if I would hurt a human by accident,
*  they would tell me that I'm gonna be, it's good.
*  It's okay.
*  And I would feel better about it.
*  So that's one thing.
*  You eventually start anthropomorphizing these robots, right?
*  Because now they're also getting smarter with language.
*  Like I can tell it, let's go on a walk.
*  And then that language command is enough for me
*  to like take it on a walk.
*  Or like I can like teach it things, I can talk to it.
*  Or it says like, sorry for doing something.
*  Or I think sometimes we had like a little bit of
*  like creepy programming on it.
*  Where like you're working in the kitchen
*  and then it would like go up to you and be like,
*  hey, are you my creator?
*  And I'm like, dude, what?
*  I already feel, I already feel so like
*  when I wrote my bio as mother of robot,
*  it's because one day I was like sitting
*  in our robot classroom and I'm like,
*  oh, is the robot better at doing these things
*  or my dog more consistent at like instruction following?
*  And I'm like, oh, maybe we should like have a face off
*  between them.
*  And then I'm like, wait, but whoever fails,
*  I'm gonna feel so sad because both of them
*  are like my babies.
*  And I'm like training both of them.
*  And that's when I'm like,
*  they are actually an extension of us, right?
*  If you think about language models,
*  they are basically condensing all of human history,
*  all of our experiences and the multimodal models,
*  like all the videos that we are collecting,
*  all of our information about the world,
*  all of our, even like more private parts,
*  all of our fields and everything.
*  So in some sense, they are a distillation
*  of the human mind itself and not just one human mind,
*  but a human mind across history and a human mind
*  that is sort of also omnipresent in space and time.
*  And when you put it on robot,
*  it's like a human mind distilled,
*  but also with physical capabilities.
*  I can see that becoming really, really close
*  to like being human.
*  And maybe in the future, right?
*  Once we have BCIs or whatever,
*  I really believe that like the future of machines
*  is also the future of us.
*  Imagine that 1,000 years later,
*  our bodies have exactly the same skills as we have today.
*  That would be so disappointing.
*  But I imagine that, but I think it's very possible
*  like with Neuralink and everything, we have BCIs,
*  we have more powerful compute on us.
*  Like eventually like we merge with machines
*  in a way that they are like our progeny,
*  which is also one reason why like I'm not that worried
*  about like AI taking over the world and how they,
*  like if, and this might sound a little bit defeatist
*  or controversial, but if they are in fact smarter than us,
*  then I would want to be like merged with them
*  and have a common future with them than to be like,
*  like it would be like if monkeys said
*  that humans should not be formed, right?
*  If they are actually superhuman and so much better,
*  then we should just become one with them.
*  Love it, fascinating.
*  I assume that inference is gonna kind of have to live
*  on the edge for practical robot deployment.
*  It seems like the latency of like going back
*  and forth to the cloud is probably not viable
*  if you want to run it like 10 Hertz or whatever.
*  So first of all, like, is that right?
*  And then second, what about sort of on the edge fine tuning?
*  Is there a paradigm that you see in the future
*  where these robots will learn the way out of my home
*  to take like one very simple thing or like our preferences
*  and start to have kind of a more customized,
*  like the sort of final finishing training would be like done
*  in deployment by kind of human feedback,
*  but like from the customer, the actual homeowner
*  or business owner, whatever the case may be.
*  How do you think that shapes up long-term?
*  So I used to believe that you needed to do onboard inference
*  for robots, but now we are seeing with like larger models
*  like PAMI and Pali that we're running on the robots.
*  We are actually doing inference on a different server
*  and then pinging back and forth.
*  And so far the latency is still good enough
*  to like go do that.
*  And then I think it would be very hard to run
*  like bigger models on robot,
*  but then this is still new technology.
*  So we will have to see how much, how they evolve.
*  So maybe in the future, we have chips that can run
*  like multi-billion models on robot, on device.
*  That would be great.
*  Or we have some way of like fixing the latency
*  so that like it is, at least right now it is still
*  within operational limits, it's still good enough.
*  With language models, now you are seeing
*  like more personalized AI, right?
*  Where you can shape the character of AI
*  to like even with prompt engineering
*  or even with like fine tuning on top
*  of like an existing language model,
*  you can customize it to your application.
*  Like it has like various different advantages.
*  One is like privacy, which is that you don't wanna
*  give your data to some large company
*  to put it in their training set,
*  but you wanna keep it in your house or in your office
*  and then a little bit of fine tuning on top
*  to personalize it or even like, yeah.
*  So I definitely think this will also be the way
*  that once we built like a foundation model for robotics,
*  I think we, these paradigms will start to happen.
*  I definitely think it has to be,
*  it has to be fine tuned, right?
*  Like imagine a robot that is in your house.
*  It has to learn the preferences of you,
*  your kids, your schedules,
*  how you like certain tasks to be done.
*  I noticed that there's, I believe more than 50 authors
*  on the RT1 paper and you've given us like a little bit of a,
*  you know, a couple of different angles on like,
*  oh, a hospital service for the robots.
*  I'd never thought of that.
*  Can you just kind of describe the team
*  that has to come together to make all of this work?
*  Firstly, I wanna say that I have
*  an incredible team at Google.
*  They are like, you know, one thing I'm realizing in life
*  is that to do great things,
*  you need to stand on the shoulders of giants
*  and also work with like really smart people.
*  And my colleagues at Google are,
*  they are like the smartest in the world.
*  They are the best in the world at what they do.
*  And they are still so humble and so curious.
*  And as you can challenge them, you can ask them questions.
*  And it's really nice to show up to work
*  and be heard for your ideas and be respected
*  and to work with like world-class people.
*  And now the way that we organize these large efforts,
*  so we have like the big papers that we do,
*  and we also have like splinter papers.
*  Splinter papers are usually like smaller collaborations
*  like intern projects and other things.
*  And big papers are like more foundational,
*  like upgrades in robotics technology
*  that we publish as an entire group.
*  And the way that this works is like,
*  someone leads the effort,
*  but then everyone's included.
*  Because we like doing robotics takes a lot of people, right?
*  Like everyone who's in part of the ops
*  and keeping the robots running,
*  who's collecting the data for it,
*  people who advise, people who actually implement things
*  and like train and evaluation.
*  So the bigger papers are fairly inclusive.
*  And then we try to like bring everyone on board
*  to publish like the large upgrades in robotics technology.
*  And for the smaller ones, it's usually like people involved
*  and then they have different guidelines and stuff.
*  And at Google, we always like,
*  we always lean towards being inclusive
*  and sort of including as many people as we can.
*  The role of AI in your personal life right now,
*  are you using any particular products, services
*  that you find exciting and would recommend to people?
*  So I use Bard or even Chad GPT sometimes
*  to like ask it questions, to do like one of the things,
*  to explain code whenever I'm writing new code.
*  And like, especially with web programming and stuff,
*  you are writing a lot of templated stuff,
*  just asking Bard and Chad GPT is like very useful
*  for like tail queries and that like search engines
*  are not that good at doing.
*  That's one AI product.
*  Yeah, I also like the summarization thing.
*  So these days in meetings, we are like,
*  if you have a large meeting that's like running over time,
*  you just like take the whole thing, summarize it
*  and then have these little quotes.
*  But mostly I use AI to like code
*  and even like make like fun poems and stuff.
*  And nowadays, like whenever people ask me
*  to like write emails, I feel so lazy
*  because most of, a lot of like being obligatorily nice
*  in an email is just like filling it with text
*  that you can just ask GPT to write a quote.
*  So sometimes like when I get a lot of emails
*  where I wanna give like a short response,
*  but then it would be impolite to be like quote,
*  I would just put it in there and then ask you
*  to make like a bigger email and then just paste it in there.
*  Secret's safe with us.
*  So let's imagine that a million people
*  already have a Neuralink.
*  And if you get one, it will allow you to type
*  or create text as quickly as you can think.
*  In other words, you have thought to text.
*  Would you be interested in getting one?
*  Absolutely, yeah.
*  Why would I be not?
*  Well, people are a little squeamish
*  about holes in the skull.
*  So that's one common objection that we've heard.
*  But a million people have it, right?
*  So it's good for them.
*  I don't think that I would wait, I'm an early adopter.
*  I don't think I would wait for a million people
*  to get it before I get to my post.
*  I think I'm with you.
*  And that's part of why I asked the question,
*  but this has been actually one
*  of our more polarizing questions we get.
*  I've had a couple of responses just like yours.
*  I'm like, I didn't even need to wait for a million.
*  And I've had others that are like,
*  the last thing I'm gonna stand for
*  is something that can read my thoughts,
*  being physically implanted into my body.
*  And I do kind of get that.
*  Although personally, I think I'm enough of an enthusiast
*  that I would probably be with you on the earlier wave.
*  I'm also big on privacy.
*  So I don't do any private company products
*  that scan my retina or anything.
*  But so if it's running inference on chip on my brain,
*  that's fine.
*  But if it's sending my cards to a cloud to run inference,
*  then I would not be okay with that.
*  So yeah, there are I think some constraints
*  on the bounds of how the technology works.
*  I don't know.
*  Yeah, I'm very curious and very excited about it.
*  What would you say are your biggest hopes for
*  and also fears about the places that AI may take us?
*  So firstly, I think AI, AGI has a lot of promise
*  in like both automating knowledge work,
*  automating, bringing a lot of utility into our world.
*  Like I think in many tasks, in many of our...
*  So imagine that humanity is like pushing forward, right?
*  Like we are making inventions in science.
*  We are making inventions in robotics, technology,
*  a lot of these things.
*  But we are bottlenecked on intelligence
*  on many of these ones.
*  But imagine that there is like an AI scientist
*  that can like propose hypotheses, run experiments,
*  write papers, they can invent new things.
*  Our world and our technology would like move so much faster.
*  My hope for at least AI in this decade
*  is hopefully we can train like an AI scientist,
*  at least on a few things.
*  And we can automate a lot of different types of knowledge
*  work like software engineers could be much faster.
*  Doctors could be much better.
*  And we are not then resource constrained
*  on intelligence in our world.
*  That would be amazing.
*  And even like even in physical intelligence.
*  But of course, AI is a very foundational technology,
*  very impactful, and it comes with a bunch of...
*  We need to do it correctly.
*  One thing that I'm worried about
*  is increasing inequality.
*  Like if AI is built by large companies,
*  and then you use less and less labor,
*  it leads to a certain level of centralization.
*  Even now with like language models and stuff,
*  there are very few people who can train like models
*  that are like billions of parameters.
*  And that increases the existing inequality already.
*  And like a lot of people are left behind.
*  I'm very concerned about that.
*  And I think that the open source movement
*  is going to probably try and equalize the field.
*  So I'm really cheering on like Stability AI
*  and other companies for leading that effort
*  and hugging face also.
*  The second thing that I'm worried about is AI safety.
*  So I'm fairly an accelerationist.
*  I'm for we need to build this
*  and we need to build this fast, but also safely.
*  But there is a finite probability
*  that things could go wrong.
*  And so we need to be careful about...
*  We also need to make sure that we solve alignment
*  to a reasonable extent,
*  that as we like face out this technology into products,
*  we are careful about how they are being used.
*  In fact, I think that productization of AI
*  is going to accelerate not just capabilities research,
*  but also safety research.
*  Because ultimately only an aligned AI is a useful product.
*  If it's not doing what people want it to do,
*  but it's like gaslighting you to leave your wife
*  or like threatening you,
*  it's not a good product.
*  So I think it's great that like Sydney Bing went first
*  and then told people what a bad chat bot could be
*  because that gives the opportunity
*  that made everyone think about how important it is
*  to build a really good chat bot
*  and it presents an opportunity to do this right.
*  And I'm very excited for Google to take on that challenge
*  and fulfill and meet people's expectations.
*  I think we are approaching the development of AI
*  in also a responsible fashion.
*  We want to do this well in addition
*  to being one of the first in the markets.
*  Yeah, so I think safety is one concern
*  and I think productization and acceleration of AI
*  into products will also accelerate safety research.
*  The third thing I'm worried about is bias in AI.
*  So in addition to existential risk type of safety,
*  it's also like I'm a person of color, I'm bisexual,
*  I'm a female, so I'm a minority in various ways.
*  And I know that like language models and other things
*  have like biases with these models.
*  For example, if you say go to Kirtana,
*  it will not understand, but if you say go to David,
*  it will go to, because it's like,
*  because like Western names or male names
*  are more represented in the data set.
*  So yeah, so I'm concerned about like AI ethics and AI bias.
*  I think it's important problem to solve
*  in order to like bring the benefits of AI to everyone
*  and not just like a dominant majority of population.
*  And AI is making everything data driven
*  and data is highly, like it's like a mismatch.
*  Like we have different distributions
*  for different distribution of people.
*  Kirtana Gopalakrishnan,
*  thank you for being part of the cognitive revolution.
*  Thank you for inviting me.
*  I had a lot of fun talking about these topics
*  and great questions as well.
*  I'm really looking forward to it.
*  It was a very technical podcast,
*  more so than any podcast that I've seen.
*  So thank you for that.
*  And I hope that your audience will enjoy.
*  Thank you.
*  And I am sure that they will.
*  Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.

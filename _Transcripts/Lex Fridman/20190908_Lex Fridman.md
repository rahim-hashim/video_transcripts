---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 3407s
Video Keywords: []
Video Views: 42795
Video Rating: None
Video Description: 
---

# Vijay Kumar Flying Robots  Lex Fridman Podcast #37
**Lex Fridman:** [September 08, 2019](https://www.youtube.com/watch?v=HYsLTNXMl1Q)
*  The following is a conversation with Vijay Kumar.
*  He's one of the top roboticists in the world,
*  a professor at the University of Pennsylvania,
*  a Dean of Penn Engineering,
*  former Director of GraspLab,
*  or the General Robotics Automation Sensing
*  and Perception Laboratory at Penn,
*  that was established back in 1979.
*  That's 40 years ago.
*  Vijay is perhaps best known
*  for his work in multi-robot systems,
*  robot swarms,
*  and micro aerial vehicles,
*  robots that elegantly cooperate in flight
*  under all the uncertainty and challenges
*  that the real world conditions present.
*  This is the Artificial Doses podcast.
*  If you enjoy it, subscribe on YouTube,
*  give it five stars on iTunes,
*  support it on Patreon,
*  or simply connect with me on Twitter
*  at Lex Friedman, spelled F-R-I-D-M-A-N.
*  And now, here's my conversation with Vijay Kumar.
*  What is the first robot you've ever built
*  or were a part of building?
*  Way back when I was in graduate school,
*  I was part of a fairly big project
*  that involved building a very large hexapod.
*  It's weighed close to 7,000 pounds,
*  and it was powered by hydraulic actuation
*  or was actuated by hydraulics
*  with 18 hydraulic motors,
*  each controlled by an Intel 8085 processor
*  and an 8086 coprocessor.
*  And so imagine this huge monster
*  that had 18 joints,
*  each controlled by an independent computer,
*  and there was a 19th computer
*  that actually did the coordination
*  between these 18 joints.
*  So I was part of this project,
*  and my thesis work was,
*  how do you coordinate the 18 legs,
*  and in particular, the pressures
*  in the hydraulic cylinders
*  to get efficient locomotion?
*  It sounds like a giant mess.
*  How difficult is it to make all the motors communicate?
*  Presumably, you have to send signals
*  hundreds of times a second, or at least.
*  This was not my work,
*  but the folks who worked on this
*  wrote what I believe to be the first
*  multiprocessor operating system.
*  This was in the 80s.
*  And you had to make sure that, obviously,
*  messages got across from one joint to another.
*  You have to remember the clock speeds
*  on those computers were about half a megahertz.
*  Right.
*  The 80s.
*  So not to romanticize the notion,
*  but how did it make you feel
*  to make, to see that robot move?
*  It was amazing.
*  In hindsight, it looks like, well,
*  we built this thing which really
*  should have been much smaller,
*  and of course, today's robots are much smaller.
*  You look at Boston Dynamics or Ghost Robotics
*  has been off from Penn.
*  But back then, you were stuck
*  with the substrate you had, the compute you had,
*  so things were unnecessarily big.
*  But at the same time,
*  and this is just human psychology,
*  somehow bigger means grander.
*  People never had the same appreciation
*  for nanotechnology or nanodevices
*  as they do for the Space Shuttle or the Boeing 747.
*  Yeah, you've actually done quite a good job
*  at illustrating that small is beautiful
*  in terms of robotics.
*  So what is, on that topic, is the most beautiful
*  or elegant robot in motion that you've ever seen?
*  Not to pick favorites or whatever,
*  but something that just inspires you that you remember.
*  Well, I think the thing that I'm most proud of
*  that my students have done is really think about
*  small UAVs that can maneuver in constrained spaces,
*  and in particular, their ability to coordinate
*  with each other and form three-dimensional patterns.
*  So once you can do that,
*  you can essentially create 3D objects in the sky,
*  and you can deform these objects on the fly.
*  So in some sense, your toolbox of what you can create
*  has suddenly got enhanced.
*  And before that, we did the two-dimensional version of this.
*  So we had ground robots forming patterns and so on.
*  So that was not as impressive.
*  That was not as beautiful.
*  But if you do it in 3D, suspended in midair,
*  and you've got to go back to 2011 when we did this.
*  Now it's actually pretty standard
*  to do these things eight years later.
*  But back then, it was a big accomplishment.
*  So the distributed cooperation
*  is where beauty emerges in your eyes.
*  Well, I think beauty to an engineer is very different
*  from beauty to someone who's looking at robots
*  from the outside, if you will.
*  But what I meant there, so before we said that grand
*  is associated with size.
*  And another way of thinking about this
*  is just the physical shape.
*  And the idea that you can get physical shapes in midair
*  and have them deform, that's beautiful.
*  But the individual components,
*  the agility is beautiful too, right?
*  That is true too.
*  So then how quickly can you actually manipulate
*  these three-dimensional shapes
*  and the individual components?
*  Yes, you're right.
*  By the way, said UAV, unmanned aerial vehicle.
*  What's a good term for drones, UAVs, quadcopters?
*  Is there a term that's being standardized?
*  I don't know if there is.
*  Everybody wants to use the word drones.
*  And I've often said this, drones to me is a pejorative word.
*  It signifies something that's dumb,
*  that's pre-programmed, that does one little thing.
*  And robots are anything but drones.
*  So I actually don't like that word,
*  but that's what everybody uses.
*  You could call it unpiloted.
*  Unpiloted.
*  But even unpiloted could be radio controlled,
*  could be remotely controlled in many different ways.
*  And I think the right word is thinking about it
*  as an aerial robot.
*  You also say agile, autonomous, aerial robot, right?
*  Yeah, so agility is an attribute,
*  but they don't have to be.
*  So what biological system,
*  because you've also drawn a lot of inspiration with those.
*  I've seen bees and ants that you've talked about.
*  What living creatures have you found to be most inspiring
*  as an engineer, instructive in your work in robotics?
*  To me, so ants are really quite incredible creatures, right?
*  So you, I mean, the individuals arguably are very simple
*  in how they're built,
*  and yet they're incredibly resilient as a population.
*  And as individuals, they're incredibly robust.
*  So, you know, if you take an ant,
*  it's six legs, you remove one leg,
*  it still works just fine.
*  And it moves along,
*  and I don't know that even realizes it's lost a leg.
*  So that's the robustness at the individual ant level.
*  But then you look about this instinct
*  for self-preservation of the colonies,
*  and they adapt in so many amazing ways.
*  You know, transcending gaps,
*  by just chaining themselves together when you have a flood,
*  being able to recruit other teammates
*  to carry big morsels of food,
*  and then going out in different directions looking for food,
*  and then being able to demonstrate consensus,
*  even though they don't communicate directly with each other
*  the way we communicate with each other,
*  in some sense, they also know how to do democracy,
*  probably better than what we do.
*  Yeah, somehow even democracy is emergent.
*  It seems like all of the phenomena that we see
*  is all emergent.
*  It seems like there's no centralized communicator.
*  There is, so I think a lot is made about that word, emergent,
*  and it means lots of things to different people,
*  but you're absolutely right.
*  I think as an engineer,
*  you think about what element, elemental behaviors,
*  what primitives you could synthesize
*  so that the whole looks incredibly powerful,
*  incredibly synergistic,
*  the whole definitely being greater than the sum of the parts,
*  and ants are living proof of that.
*  So when you see these beautiful swarms
*  where there's biological systems of robots,
*  do you sometimes think of them
*  as a single individual living intelligent organism?
*  So it's the same as thinking of our human civilization
*  as one organism, or do you still, as an engineer,
*  think about the individual components
*  and all the engineering
*  that went into the individual components?
*  Well, that's very interesting.
*  So again, philosophically as engineers,
*  what we wanna do is to go beyond the individual components,
*  the individual units, and think about it as a unit,
*  as a cohesive unit,
*  without worrying about the individual components.
*  If you start obsessing about the individual building blocks,
*  and what they do,
*  you inevitably will find it hard to scale up.
*  Just mathematically, just think about individual things
*  you wanna model, and if you want to have 10 of those,
*  then you essentially are taking Cartesian products
*  of 10 things, and that makes it really complicated.
*  Then to do any kind of synthesis or design
*  in that high-dimensional space is really hard.
*  So the right way to do this is to think about
*  the individuals in a clever way so that at the higher level,
*  when you look at lots and lots of them,
*  abstractly, you can think of them
*  in some low-dimensional space.
*  So what does that involve?
*  For the individual, do you have to try to make
*  the way they see the world as local as possible?
*  And the other thing, do you just have to make them robust
*  to collisions, like you said, with the ants?
*  If something fails, the whole swarm doesn't fail?
*  Right, I think as engineers, we do this.
*  I mean, you think about we build planes,
*  or we build iPhones, and we know that by
*  taking individual components, well-engineered components
*  with well-specified interfaces that behave
*  in a predictable way, you can build complex systems.
*  So that's ingrained, I would claim,
*  in most engineers' thinking,
*  and it's true for computer scientists as well.
*  I think what's different here is that you want
*  the individuals to be robust in some sense,
*  as we do in these other settings,
*  but you also want some degree of resiliency
*  for the population, and so you really want them
*  to be able to reestablish communication
*  with their neighbors.
*  You want them to rethink their strategy for group behavior.
*  You want them to reorganize, and that's where,
*  I think, a lot of the challenges lie.
*  So just at a high level, what does it take
*  for a bunch of, what should we call them,
*  flying robots to create a formation?
*  Just for people who are not familiar
*  with robotics in general, how much information is needed?
*  How do you even make it happen
*  without a centralized controller?
*  So, I mean, there are a couple of different ways
*  of looking at this.
*  If you are a purist, you think of it as a,
*  as a way of recreating what nature does.
*  So nature forms groups for several reasons,
*  but mostly it's because of this instinct
*  that organisms have of preserving their colonies,
*  their population, which means what?
*  You need shelter, you need food, you need to procreate,
*  and that's basically it.
*  So the kinds of interactions you see are all organic,
*  they're all local, and the only information that they share,
*  and mostly it's indirectly, is to, again,
*  preserve the herd or the flock or the swarm,
*  and either by looking for new sources of food
*  or looking for new shelters, right?
*  As engineers, when we build swarms,
*  we have a mission, and when you think of a mission,
*  and it involves mobility, most often it's described
*  in some kind of a global coordinate system.
*  As a human, as an operator, as a commander,
*  or as a collaborator, I have my coordinate system,
*  and I want the robots to be consistent with that.
*  So I might think of it slightly differently.
*  I might want the robots to recognize that coordinate system,
*  which means not only do they have to think locally
*  in terms of who their immediate neighbors are,
*  but they have to be cognizant
*  of what the global environment looks like.
*  So if I say, surround this building
*  and protect this from intruders,
*  well, they're immediately in a building-centered
*  coordinate system, and I have to tell them
*  where the building is.
*  And they're globally collaborating
*  on the map of that building.
*  They're maintaining some kind of global,
*  not just in the frame of the building,
*  but there's information that's ultimately being built up
*  explicitly as opposed to kind of implicitly,
*  like nature might.
*  Correct, correct.
*  So in some sense, nature is very, very sophisticated,
*  but the tasks that nature solves or needs to solve
*  are very different from the kind of engineered tasks,
*  artificial tasks that we are forced to address.
*  And again, there's nothing preventing us
*  from solving these other problems,
*  but ultimately it's about impact.
*  You want these swarms to do something useful.
*  And so you're kind of driven into this very unnatural,
*  if you will, unnatural meaning not like how nature does,
*  setting.
*  And it's probably a little bit more expensive
*  to do it the way nature does,
*  because nature is less sensitive
*  to the loss of the individual.
*  And cost-wise in robotics,
*  I think you're more sensitive to losing individuals.
*  I think that's true,
*  although if you look at the price to performance ratio
*  of robotic components, it's coming down dramatically.
*  Oh, interesting.
*  It continues to come down.
*  So I think we're asymptotically approaching the point
*  where we would get, yeah,
*  the cost of individuals would really become insignificant.
*  So let's step back at a high-level view,
*  the impossible question of what kind of, as an overview,
*  what kind of autonomous flying vehicles are there
*  in general?
*  I think the ones that receive a lot of notoriety
*  are obviously the military vehicles.
*  Military vehicles are controlled by a base station,
*  but have a lot of human supervision,
*  but have limited autonomy,
*  which is the ability to go from point A to point B,
*  and even the more sophisticated vehicles
*  can do autonomous takeoff and landing.
*  And those usually have wings and they're heavy.
*  Usually they're wings,
*  but there's nothing preventing us from doing this
*  for helicopters as well.
*  I mean, there are many military organizations
*  that have autonomous helicopters in the same vein.
*  And by the way, you look at autopilots and airplanes,
*  and it's actually very similar.
*  In fact, one interesting question we can ask is,
*  if you look at all the air safety violations,
*  all the crashes that occurred,
*  would they have happened if the plane
*  were truly autonomous?
*  And I think you'll find that in many of the cases,
*  because of pilot error, we make silly decisions.
*  And so in some sense, even in air traffic,
*  commercial air traffic, there's a lot of applications,
*  although we only see autonomy being enabled
*  at very high altitudes when the plane is an autopilot.
*  There's still a role for the human,
*  and that kind of autonomy is, you're kind of implying,
*  I don't know what the right word is,
*  but it's a little dumber than it could be.
*  Right, so in the lab, of course,
*  we can afford to be a lot more aggressive.
*  And the question we try to ask is,
*  can we make robots that will be able to make decisions
*  without any kind of external infrastructure?
*  So what does that mean?
*  So the most common piece of infrastructure
*  that airplanes use today is GPS.
*  GPS is also the most brittle form of information.
*  If you're driven in a city, try to use GPS navigation.
*  You know, in tall buildings, you immediately lose GPS.
*  And so that's not a very sophisticated way
*  of building autonomy.
*  I think the second piece of infrastructure
*  they rely on is communications.
*  Again, it's very easy to jam communications.
*  In fact, if you use Wi-Fi,
*  you know that Wi-Fi signals drop out, cell signals drop out.
*  So to rely on something like that is not good.
*  The third form of infrastructure we use,
*  and I hate to call it infrastructure,
*  but it is that in the sense of robots, it's people.
*  So you could rely on somebody to pilot you.
*  And so the question you wanna ask is,
*  if there are no pilots,
*  if there's no communications in any base station,
*  if there's no knowledge of position,
*  and if there's no a priori map,
*  a priori knowledge of what the environment looks like,
*  a priori model of what might happen in the future,
*  can robots navigate?
*  So that is true autonomy.
*  So that's true autonomy.
*  And we're talking about, you mentioned,
*  like military application of drones.
*  Okay, so what else is there?
*  You talk about agile, autonomous flying robots, aerial robots.
*  So that's a different kind of,
*  it's not winged, it's not big, at least it's small.
*  So I use the word agility mostly,
*  or at least we're motivated to do agile robots,
*  mostly because robots can operate
*  and should be operating in constrained environments.
*  And if you want to operate the way a global hawk operates,
*  I mean, the kinds of conditions in which you operate
*  are very, very restrictive.
*  If you wanna go inside a building, for example,
*  for search and rescue, or to locate an active shooter,
*  or you wanna navigate under the canopy in an orchard
*  to look at health of plants,
*  or to look for, to count fruits,
*  to measure the tree trunks.
*  These are things we do, by the way.
*  Yeah, some cool agriculture stuff you've shown in the past.
*  It's really awesome.
*  Right, so in those kinds of settings,
*  you do need that agility.
*  Agility does not necessarily mean
*  you break records for the 100 meters dash.
*  What it really means is you see the unexpected
*  and you're able to maneuver in a safe way,
*  and in a way that gets you the most information
*  about the thing you're trying to do.
*  By the way, you may be the only person
*  who in a TED Talk has used a math equation,
*  which is amazing.
*  People should go see one of your TED Talks.
*  Actually, it's very interesting
*  because the TED curator, Chris Anderson,
*  told me you can't show math.
*  I thought about it, but that's who I am.
*  That's our work.
*  I felt compelled to give the audience a taste
*  for at least some math.
*  On that point, simply, what does it take
*  to make a thing with four motors fly, a quadcopter,
*  one of these little flying robots?
*  How hard is it to make it fly?
*  How do you coordinate the four motors?
*  How do you convert those motors into actual movement?
*  This is an interesting question.
*  We've been trying to do this since 2000.
*  It is a commentary on the sensors
*  that were available back then,
*  the computers that were available back then.
*  A number of things happened between 2000 and 2007.
*  One is the advances in computing.
*  We all know about Moore's Law,
*  but I think 2007 was a tipping point,
*  the year of the iPhone, the year of the cloud.
*  Lots of things happened in 2007.
*  But going back even further,
*  inertial measurement units as a sensor really matured.
*  Again, lots of reasons for that.
*  Certainly, there's a lot of federal funding,
*  particularly DARPA and the US,
*  but they didn't anticipate this boom in IMUs.
*  But if you look subsequently,
*  what happened is that every car manufacturer
*  had to put an airbag in,
*  which meant you had to have an accelerometer on board.
*  And so that drove down the price to performance ratio.
*  Wow, I should know this.
*  That's very interesting.
*  That's very interesting, the connection there.
*  And that's why research is very,
*  it's very hard to predict the outcomes.
*  And again, the federal government
*  spent a ton of money on things
*  that they thought were useful for resonators,
*  but it ended up enabling these small UAVs,
*  which is great,
*  because I could have never raised that much money
*  and told, sold this project,
*  hey, we want to build these small UAVs.
*  Can you actually fund the development of low-cost IMUs?
*  So why do you need an IMU on a UAV?
*  So I'll come back to that.
*  But so in 2007, 2008, we were able to build these.
*  And then the question you're asking was a good one.
*  How do you coordinate the motors to develop this?
*  But over the last 10 years, everything is commoditized.
*  A high school kid today can pick up a Raspberry Pi kit
*  and build this.
*  All the low-level functionality is all automated.
*  But basically at some level,
*  you have to drive the motors at the right RPMs,
*  the right velocity,
*  in order to generate the right amount of thrust
*  in order to position it and orient it
*  in a way that you need to in order to fly.
*  The feedback that you get is from onboard sensors
*  and the IMU is an important part of it.
*  The IMU tells you what the acceleration is,
*  as well as what the angular velocity is.
*  And those are important pieces of information.
*  In addition to that, you need some kind of local position
*  or velocity information.
*  For example, when we walk,
*  we implicitly have this information
*  because we kind of know what our stride length is.
*  We also are looking at images fly past our retina,
*  if you will, and so we can estimate velocity.
*  We also have accelerometers in our head,
*  and we're able to integrate all these pieces of information
*  to determine where we are as we walk.
*  And so robots have to do something very similar.
*  You need an IMU, you need some kind of a camera
*  or other sensor that's measuring velocity.
*  And then you need some kind of a global reference frame
*  if you really want to think about doing something
*  in a world coordinate system.
*  And so how do you estimate your position
*  with respect to that global reference frame?
*  That's important as well.
*  So coordinating the RPMs of the four motors
*  is what allows you to first of all fly and hover,
*  and then you can change the orientation
*  and the velocity and so on.
*  Exactly, exactly.
*  So it's a bunch of degrees of freedom
*  that you're complaining about.
*  There's six degrees of freedom,
*  but you only have four inputs, the four motors.
*  And it turns out to be a remarkably versatile configuration.
*  You think at first, well, I only have four motors,
*  how do I go sideways?
*  But it's not too hard to say,
*  well, if I tilt myself, I can go sideways.
*  And then you have four motors pointing up,
*  how do I rotate in place about a vertical axis?
*  Well, you rotate them at different speeds
*  and that generates reaction moments
*  and that allows you to turn.
*  So it's actually a pretty,
*  it's an optimal configuration from an engineer standpoint.
*  It's very simple, very cleverly done and very versatile.
*  So if you could step back to a time,
*  so I've always known flying robots as,
*  to me it was natural that a quadcopter should fly.
*  But when you first started working with it,
*  how surprised are you that you can make,
*  do so much with the four motors?
*  How surprising is that you can make this thing fly,
*  first of all, that you can make it hover,
*  then you can add control to it.
*  Firstly, this is not,
*  the four motor configuration is not ours.
*  It has at least a hundred year history.
*  And various people try to get quadrotors to fly
*  without much success.
*  As I said, we've been working on this since 2000.
*  Our first designs were, well, this is way too complicated.
*  Why not we try to get an omnidirectional flying robot?
*  So our early designs, we had eight rotors
*  and so these eight rotors were arranged uniformly
*  on a sphere, if you will.
*  So you can imagine a symmetric configuration.
*  And so you should be able to fly anywhere.
*  But the real challenge we had is the strength
*  to weight ratio is not enough.
*  And of course we didn't have the sensors and so on.
*  So everybody knew, or at least the people
*  who worked with Rotocraft knew four rotors would get it done.
*  So that was not our idea.
*  But it took a while before we could actually do
*  the onboard sensing and the computation that was needed
*  for the kinds of agile maneuvering that we wanted to do
*  in our little aerial robots.
*  And that only happened between 2007 and 2009 in our lab.
*  Yeah, and you have to send the signal
*  many hundred times a second.
*  So the compute there, everything has to come down in price.
*  And what are the steps of getting from point A to point B?
*  So we just talked about like local control.
*  But if all the kind of cool dancing in the air
*  that I've seen you show, how do you make it happen?
*  Make a trajectory, first of all, okay,
*  figure out a trajectory, so plan a trajectory.
*  And then how do you make that trajectory happen?
*  Yeah, I think planning is a very fundamental problem
*  in robotics, I think, 10 years ago,
*  it was an esoteric thing, but today with self-driving cars,
*  everybody can understand this basic idea
*  that a car sees a whole bunch of things,
*  and it has to keep a lane or maybe make a right turn
*  or switch lanes, it has to plan a trajectory.
*  It has to be safe, it has to be efficient.
*  So everybody's familiar with that.
*  That's kind of the first step that you have to think about
*  when you say autonomy.
*  And so for us, it's about finding smooth motions,
*  motions that are safe.
*  So we think about these two things,
*  one is optimality, one is safety.
*  Clearly, you cannot compromise safety.
*  So you're looking for safe, optimal motions.
*  The other thing you have to think about is,
*  can you actually compute a reasonable trajectory
*  in a small amount of time?
*  Because you have a time budget.
*  So the optimal becomes suboptimal,
*  but in our lab, we focus on synthesizing smooth trajectory
*  that satisfy all the constraints, in other words,
*  don't violate any safety constraints,
*  and is as efficient as possible.
*  And when I say efficient, it could mean,
*  I wanna get from point A to point B as quickly as possible,
*  or I wanna get to it as gracefully as possible,
*  or I wanna consume as little energy as possible.
*  But always staying within the safety constraints.
*  But yes, always finding a safe trajectory.
*  So there's a lot of excitement and progress
*  in the field of machine learning,
*  and reinforcement learning and the neural network variant
*  of that with deep reinforcement learning.
*  Do you see a role of machine learning in,
*  so a lot of the success of flying robots
*  did not rely on machine learning,
*  except for maybe a little bit of the perception
*  of the computer vision side.
*  On the control side and the planning,
*  do you see there's a role in the future
*  for machine learning?
*  So let me disagree a little bit with you.
*  I think we never perhaps called out in my work,
*  called out learning, but even this very simple idea
*  of being able to fly through a constrained space.
*  The first time you try it, you'll invariably,
*  you might get it wrong if the task is challenging.
*  And the reason is to get it perfectly right,
*  you have to model everything in the environment.
*  And flying is notoriously hard to model.
*  There are aerodynamic effects that we constantly discover.
*  Even just before I was talking to you,
*  I was talking to a student about how blades flap
*  when they fly.
*  Wow.
*  And that ends up changing how a rotorcraft
*  is accelerated in the angular direction.
*  Does he use like micro flaps or something?
*  It's not micro flaps.
*  So we assume that each blade is rigid,
*  but actually it flaps a little bit.
*  Oh.
*  It bends.
*  Interesting, yeah.
*  And so the models rely on the fact,
*  on an assumption that they're actually rigid,
*  but that's not true.
*  If you're flying really quickly,
*  these effects become significant.
*  If you're flying close to the ground,
*  you get pushed off by the ground, right?
*  Something which every pilot knows when he tries to land
*  or she tries to land, this is called a ground effect.
*  Something very few pilots think about is what happens
*  when you go close to a ceiling,
*  where you get sucked into a ceiling.
*  There are very few aircrafts that fly close
*  to any kind of ceiling.
*  Likewise, when you go close to a wall,
*  there are these wall effects.
*  And if you've gone on a train and you pass another train
*  that's traveling in the opposite direction,
*  you feel the buffeting.
*  And so these kinds of micro climates
*  affect our UAVs significantly.
*  So if you want- And they're impossible to model,
*  essentially.
*  I wouldn't say they're impossible to model,
*  but the level of sophistication you would need in the model
*  and the software would be tremendous.
*  Plus to get everything right would be awfully tedious.
*  So the way we do this is over time,
*  we figure out how to adapt to these conditions.
*  So early on, we use the form of learning
*  that we call iterative learning.
*  So this idea, if you want to perform a task,
*  there are a few things that you need to change
*  and iterate over, few parameters
*  that over time you can figure out.
*  So I could call it policy gradient reinforcement learning,
*  but actually it was just iterative learning.
*  Iterative learning.
*  And so this was their way back.
*  I think what's interesting is,
*  if you look at autonomous vehicles today,
*  learning could occur in two pieces.
*  One is perception, understanding the world.
*  Second is action, taking actions.
*  Everything that I've seen that is successful
*  is on the perception side of things.
*  So in computer vision, we've made amazing strides
*  in the last 10 years.
*  So recognizing objects, actually detecting objects,
*  classifying them and tagging them in some sense,
*  annotating them.
*  This is all done through machine learning.
*  On the action side, on the other hand,
*  I don't know of any examples where there are fielded systems
*  where we actually learn the right behavior.
*  Outside of single demonstration is successful.
*  In the laboratory, this is the holy grail.
*  Can you do end-to-end learning?
*  Can you go from pixels to motor currents?
*  This is really, really hard.
*  And I think if you go forward,
*  the right way to think about these things
*  is data-driven approaches, learning-based approaches,
*  in concert with model-based approaches,
*  which is the traditional way of doing things.
*  So I think there's a piece,
*  there's a role for each of these methodologies.
*  So what do you think, just jumping out on topics,
*  since you mentioned autonomous vehicles,
*  what do you think are the limits on the perception side?
*  So I've talked to Elon Musk,
*  and there on the perception side,
*  they're using primarily computer vision
*  to perceive the environment.
*  Because you work with the real world a lot,
*  and the physical world,
*  what are the limits of computer vision?
*  Do you think we can solve autonomous vehicles
*  on the perception side,
*  focusing on vision alone and machine learning?
*  So we also have a spin-off company, Exxon Technologies,
*  that works underground in mines.
*  So you go into mines, they're dark, they're dirty.
*  You fly in a dirty area,
*  there's stuff you kick up by the propellers,
*  the downwash kicks up dust.
*  I challenge you to get a computer vision algorithm
*  to work there.
*  So we use lidars in that setting.
*  Indoors, and even outdoors when we fly through fields,
*  I think there's a lot of potential
*  for just solving the problem using computer vision alone.
*  But I think the bigger question is,
*  can you actually solve,
*  or can you actually identify all the corner cases
*  using a single-sensing modality and using learning alone?
*  So what's your intuition there?
*  So look, if you have a corner case
*  and your algorithm doesn't work,
*  your instinct is to go get data about the corner case
*  and patch it up, learn how to deal with that corner case.
*  But at some point, this is going to saturate,
*  this approach is not viable.
*  So today, computer vision algorithms
*  can detect 90% of the objects,
*  or can detect objects 90% of the time,
*  classify them 90% of the time.
*  Cats on the internet, I probably can do 95%, I don't know.
*  But to get from 90% to 99%, you need a lot more data.
*  And then I tell you, well, that's not enough
*  because I have a safety-critical application,
*  I wanna go from 99% to 99.9%, well, it's even more data.
*  So I think if you look at wanting accuracy on the X axis
*  and look at the amount of data on the Y axis,
*  I believe that curve is an exponential curve.
*  Wow, okay, it's even hard if it's linear.
*  It's hard if it's linear, totally,
*  but I think it's exponential.
*  And the other thing you have to think about
*  is that this process is a very, very power-hungry process
*  to run data forms or servers.
*  Power, you mean literally power?
*  Literally power, literally power.
*  So in 2014, five years ago,
*  and I don't have more recent data,
*  2% of US electricity consumption was from data farms.
*  So we think about this as an information science
*  and information processing problem.
*  Actually, it is an energy processing problem.
*  And so unless we figure out better ways of doing this,
*  I don't think this is viable.
*  So talking about data,
*  so talking about driving,
*  which is a safety-critical application,
*  and in some aspect, the flight is safety-critical,
*  maybe philosophical question, maybe an engineering one.
*  What problem do you think is harder to solve?
*  Autonomous driving or autonomous flight?
*  That's a really interesting question.
*  I think autonomous flight has several advantages
*  that autonomous driving doesn't have.
*  So look, if I want to go from point A to point B,
*  I have a very, very safe trajectory.
*  Go vertically up to a maximum altitude,
*  fly horizontally to just about the destination
*  and then come down vertically.
*  This is pre-programmed.
*  The equivalent of that is very hard to find
*  in the self-driving car world
*  because you're on the ground,
*  you're in a two-dimensional surface,
*  and the trajectories on the two-dimensional surface
*  are more likely to encounter obstacles.
*  I mean this in an intuitive sense,
*  but mathematically true.
*  Mathematically as well, that's true.
*  There's other option on the 2G space of platooning,
*  or because there's so many obstacles,
*  you can connect to those obstacles and all these kinds of-
*  Sure, but those exist in the three-dimensional space as well.
*  So they do.
*  So the question also implies how difficult are obstacles
*  in the three-dimensional space in flight?
*  So that's the downside.
*  I think in three-dimensional space,
*  you're modeling three-dimensional world,
*  not just because you want to avoid it,
*  but you want to reason about it
*  and you want to work in that three-dimensional environment,
*  and that's significantly harder.
*  So that's one disadvantage.
*  I think the second disadvantage is of course,
*  anytime you fly, you have to put up with the peculiarities
*  of aerodynamics in their complicated environments.
*  How do you negotiate that?
*  That's always a problem.
*  Do you see a time in the future where there is,
*  you mentioned there's agriculture applications,
*  there's a lot of applications of flying robots,
*  but do you see a time in the future
*  where there's tens of thousands,
*  or maybe hundreds of thousands of delivery drones
*  that fill the sky, a delivery flying robots?
*  I think there's a lot of potential
*  for the last mile delivery.
*  And so in crowded cities,
*  I don't know if you go to a place like Hong Kong,
*  just crossing the river can take half an hour,
*  and while a drone can just do it in five minutes at most.
*  I think you look at delivery of supplies to remote villages.
*  I work with a nonprofit called Weave Robotics.
*  So they work in the Peruvian Amazon,
*  where the only highways are rivers.
*  And to get from point A to point B may take five hours,
*  while with a drone, you can get there in 30 minutes.
*  So just delivering drugs,
*  retrieving samples for testing vaccines,
*  I think there's huge potential here.
*  So I think the challenges are not technological,
*  the challenge is economical.
*  The one thing I'll tell you that nobody thinks about
*  is the fact that we've not made huge strides
*  in battery technology.
*  Yes, it's true, batteries are becoming less expensive
*  because we have these mega factories that are coming up,
*  but they're all based on lithium-based technologies.
*  And if you look at the energy density and the power density,
*  those are two fundamentally limiting numbers.
*  So power density is important because for a UAV
*  to take off vertically into the air, which most drones do,
*  they don't have a runway,
*  you consume roughly 200 watts per kilo at the small size.
*  That's a lot.
*  In contrast, the human brain consumes less than 80 watts,
*  the whole of the human brain.
*  So just imagine just lifting yourself into the air
*  is like two or three light bulbs,
*  which makes no sense to me.
*  Yeah, so you're going to have to at scale
*  solve the energy problem then,
*  charging the batteries, storing the energy and so on.
*  And then the storage is the second problem,
*  but storage limits the range.
*  But you have to remember that you have to burn
*  a lot of it per given time.
*  So the burning is another problem.
*  Which is a power question.
*  Yes, and do you think just your intuition,
*  there are breakthroughs in batteries on the horizon?
*  How hard is that problem?
*  Look, there are a lot of companies
*  that are promising flying cars,
*  that are autonomous and that are clean.
*  I think they're over promising.
*  The autonomy piece is doable.
*  The clean piece, I don't think so.
*  There's another company that I work with called Jatatra.
*  They make small jet engines.
*  And they can get up to 50 miles an hour very easily
*  and lift 50 kilos.
*  But they're jet engines.
*  They're efficient.
*  They're a little louder than electric vehicles,
*  but they can build flying cars.
*  So your sense is that there's a lot of pieces
*  that have come together.
*  So on this crazy question,
*  if you look at companies like Kitty Hawk,
*  working on electric, so the clean,
*  talking to Sebastian Thrun,
*  it's a crazy dream, you know?
*  But you work with flight a lot.
*  You've mentioned before that manned flights
*  or carrying a human body is very difficult to do.
*  So how crazy is flying cars?
*  Do you think there'll be a day when we have
*  vertical takeoff and landing vehicles
*  that are sufficiently affordable
*  that we're going to see a huge amount of them
*  and they would look like something like we dream of
*  when we think about flying cars?
*  Yeah, like the Jetsons.
*  The Jetsons, yeah.
*  So look, there are a lot of smart people working on this
*  and you never say something is not possible
*  when you have people like Sebastian Thrun working on it.
*  So I totally think it's viable.
*  I question, again, the electric piece.
*  The electric piece, yeah.
*  And again, for short distances, you can do it.
*  And there's no reason to suggest
*  that these are all just have to be rotorcrafts.
*  You take off vertically,
*  but then you morph into a forward flight.
*  I think there are a lot of interesting designs.
*  The question to me is, are these economically viable?
*  And if you agree to do this with fossil fuels,
*  it instantly immediately becomes viable.
*  Okay, that's the real challenge.
*  Do you think it's possible for robots and humans
*  to collaborate successfully on tasks?
*  So a lot of robotics folks that I talk to and work with,
*  I mean, humans just add a giant mess to the picture.
*  So it's best to remove them from consideration
*  when solving specific tasks.
*  It's very difficult to model.
*  There's just a source of uncertainty.
*  In your work with these agile flying robots,
*  do you think there's a role for collaboration with humans
*  or is it best to model tasks in a way
*  that doesn't have a human in the picture?
*  I don't think we should ever think about robots
*  without human in the picture.
*  Ultimately, robots are there
*  because we want them to solve problems for humans.
*  But there's no general solution to this problem.
*  I think if you look at human interaction
*  and how humans interact with robots,
*  we think of these in sort of three different ways.
*  One is the human commanding the robot.
*  The second is the human collaborating with the robot.
*  So for example, we work on how a robot
*  can actually pick up things with a human and carry things.
*  That's like true collaboration.
*  And third, we think about humans as bystanders,
*  self-driving cars, what's the human's role
*  and how do self-driving cars
*  acknowledge the presence of humans.
*  So I think all of these things are different scenarios.
*  It depends on what kind of humans work on a task.
*  And I think it's very difficult to say
*  that there's a general theory that we all have for this.
*  But at the same time, it's also silly to say
*  that we should think about robots independent of humans.
*  So to me, human robot interaction
*  is almost a mandatory aspect of everything we do.
*  Yes, but to which degree?
*  So your thoughts,
*  if we jump to autonomous vehicles, for example,
*  there's a big debate between what's called level two
*  and level four.
*  So semi-autonomous and autonomous vehicles.
*  And sort of the Tesla approach currently at least
*  has a lot of collaboration between human and machine.
*  So the human is supposed to actively supervise
*  the operation of the robot.
*  Part of the safety definition of how safe a robot is
*  in that case is how effective is the human in monitoring it.
*  Do you think that's ultimately not a good approach
*  in sort of having a human in the picture,
*  not as a bystander or part of the infrastructure,
*  but really as part of what's required
*  to make the system safe?
*  This is harder than it sounds.
*  I think, you know, if you,
*  if you, I mean, I'm sure you've driven before
*  in highways and so on.
*  It's really very hard to have,
*  to relinquish control to a machine.
*  And then take over when needed.
*  So I think Tesla's approach is interesting
*  because it allows you to periodically establish
*  some kind of contact with the car.
*  Toyota on the other hand is thinking about shared autonomy
*  as a collaborative autonomy as a paradigm.
*  If I may argue, these are very, very simple ways
*  of human robot collaboration.
*  Because the task is pretty boring.
*  You sit in a vehicle, you go from point A to point B.
*  I think the more interesting thing to me is,
*  for example, search and rescue.
*  I've got a human first responder, robot first responders.
*  I gotta do something.
*  It's important.
*  I have to do it in two minutes.
*  The building is burning.
*  There's been an explosion.
*  It's collapsed.
*  How do I do it?
*  I think to me, those are the interesting things
*  where it's very, very unstructured.
*  And what's the role of the human,
*  what's the role of the robot?
*  Clearly there's lots of interesting challenges
*  and as a field, I think we're gonna make a lot of progress
*  in this area.
*  It's an exciting form of collaboration.
*  You're right.
*  In autonomous driving, the main enemy is just boredom
*  of the human as opposed to in rescue operations.
*  It's literally life and death
*  and the collaboration enables the effective completion
*  of the mission.
*  So it's exciting.
*  In some sense, we're also doing this.
*  You think about the human driving a car
*  and almost invariably the human's trying to estimate
*  the state of the car.
*  They estimate the state of the environment and so on.
*  But what if the car were to estimate the state of the human?
*  So for example, I'm sure you have a smartphone
*  and the smartphone tries to figure out what you're doing
*  and send you reminders
*  and oftentimes telling you to drive to a certain place,
*  although you have no intention of going there
*  because it thinks that that's where you should be
*  because of some Gmail calendar entry
*  or something like that.
*  And it's trying to constantly figure out who you are,
*  what you're doing.
*  If a car were to do that,
*  maybe that would make the driver safer
*  because the car is trying to figure out
*  is the driver paying attention,
*  looking at his or her eyes,
*  looking at circadian movements.
*  So I think the potential is there,
*  but from the reverse side,
*  it's not robot modeling, but it's human modeling.
*  It's more in the human, right?
*  And I think the robots can do a very good job
*  of modeling humans if you really think about the framework
*  that you have a human sitting in a cockpit,
*  surrounded by sensors, all staring at him,
*  in addition to be staring outside,
*  but also staring at him.
*  I think there's a real synergy there.
*  Yeah, I love that problem
*  because it's the new 21st century form of psychology,
*  actually, AI-enabled psychology.
*  A lot of people have sci-fi-inspired fears
*  of walking robots like those from Boston Dynamics.
*  If you just look at shows on Netflix and so on,
*  or flying robots like those you work with,
*  how would you, how do you think about those fears?
*  How would you alleviate those fears?
*  Do you have inklings, echoes of those same concerns?
*  Anytime we develop a technology
*  meaning to have positive impact in the world,
*  there's always the worry that
*  somebody could subvert those technologies
*  and use it in an adversarial setting,
*  and robotics is no exception, right?
*  So I think it's very easy to weaponize robots.
*  I think we talk about swarms.
*  One thing I worry a lot about is,
*  so for us to get swarms to work
*  and do something reliably is really hard,
*  but suppose I have this challenge
*  of trying to destroy something,
*  and I have a swarm of robots,
*  where only one out of the swarm
*  needs to get to its destination.
*  So that suddenly becomes a lot more doable.
*  And so I worry about this general idea
*  of using autonomy with lots and lots of agents.
*  I mean, having said that,
*  look, a lot of this technology is not very mature.
*  My favorite saying is that
*  if somebody had to develop this technology,
*  wouldn't you rather the good guys do it
*  so the good guys have a good understanding
*  of the technology so they can figure out
*  how this technology is being used in a bad way,
*  or could be used in a bad way,
*  and try to defend against it?
*  So we think a lot about that.
*  So we have a, we're doing research
*  on how to defend against swarms, for example.
*  That's interesting.
*  There's in fact a report by the National Academies
*  on counter UAS technologies.
*  This is a real threat,
*  but we're also thinking about how to defend against this,
*  and knowing how swarms work,
*  knowing how autonomy works is, I think, very important.
*  So it's not just politicians.
*  You think engineers have a role in this discussion?
*  Absolutely.
*  I think the days where politicians can be agnostic
*  to technology are gone.
*  I think every politician needs to be literate in technology.
*  And I often say technology is the new liberal art.
*  Understanding how technology will change your life,
*  I think is important,
*  and every human being needs to understand that.
*  And maybe we can elect some engineers to office as well,
*  on the other side.
*  What are the biggest open problems in robotics in your view?
*  You said we're in the early days in some sense.
*  What are the problems we would like to solve in robotics?
*  I think there are lots of problems, right?
*  But I would phrase it in the following way.
*  If you look at the robots we're building,
*  they're still very much tailored towards doing specific tasks
*  and specific settings.
*  I think the question of how do you get them to operate
*  in much broader settings where things can change
*  in unstructured environments is up in the air.
*  So think of a self-driving cars.
*  Today, we can build a self-driving car in a parking lot.
*  We can do level five autonomy in a parking lot.
*  But can you do level five autonomy
*  in the streets of Napoli in Italy or Mumbai in India?
*  No.
*  So in some sense, when we think about robotics,
*  we have to think about where they're functioning,
*  what kind of environment, what kind of a task.
*  We have no understanding
*  of how to put both those things together.
*  So we're in the very early days
*  of applying it to the physical world.
*  And I was just in Naples actually.
*  And there's levels of difficulty and complexity
*  depending on which area you're applying it to.
*  I think so.
*  And we don't have a systematic way of understanding that.
*  Everybody says just because a computer can now beat a human
*  at any board game, we suddenly know
*  something about intelligence.
*  That's not true.
*  A computer board game is very, very structured.
*  It is the equivalent of working in a Henry Ford factory
*  where parts come, you assemble, move on.
*  It's a very, very, very structured setting.
*  That's the easiest thing.
*  And we know how to do that.
*  So you've done a lot of incredible work
*  at the UPenn University of Pennsylvania Grass Club.
*  You're now Dean of Engineering at UPenn.
*  What advice do you have for a new bright-eyed undergrad
*  interested in robotics or AI or engineering?
*  Well, I think there's really three things.
*  One is you have to get used to the idea
*  that the world will not be the same in five years
*  or four years whenever you graduate, right?
*  Which is really hard to do.
*  So this thing about predicting the future,
*  every one of us needs to be trying
*  to predict the future always.
*  Not because you'll be any good at it,
*  but by thinking about it, I think you sharpen your senses
*  and you become smarter.
*  So that's number one.
*  Number two, and it's a corollary of the first piece,
*  which is you really don't know what's gonna be important.
*  So this idea that I'm gonna specialize in something
*  which will allow me to go in a particular direction,
*  it may be interesting,
*  but it's important also to have this breadth
*  so you have this jumping off point.
*  I think the third thing,
*  and this is where I think Penn excels,
*  I mean, we teach engineering,
*  but it's always in the context of the liberal arts.
*  It's always in the context of society.
*  As engineers, we cannot afford to lose sight of that.
*  So I think that's important.
*  But I think one thing that people underestimate
*  when they do robotics is the importance
*  of mathematical foundations,
*  the importance of representations.
*  Not everything can just be solved
*  by looking for ROS packages on the internet
*  or to find a deep neural network that works.
*  I think the representation question is key,
*  even to machine learning,
*  where if you ever hope to achieve or get to explainable AI,
*  somehow there need to be representations
*  that you can understand.
*  So if you wanna do robotics,
*  you should also do mathematics,
*  and you said liberal arts, a little literature.
*  If you wanna build a robot,
*  you should be reading Dostoyevsky.
*  I agree with that.
*  Very good.
*  So Vijay, thank you so much for talking today.
*  It was an honor.
*  Thank you.
*  It was just a very exciting conversation.
*  Thank you.
*  Thank you.
---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 5179s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 5710
Video Rating: None
Video Description: Patreon for full episodes and Discord community: 
https://www.patreon.com/braininspired

Free Video Series: Open Questions in AI and Neuroscience:
https://braininspired.co/open/

Show notes: https://braininspired.co/podcast/134/

Music by: The New Year: http://www.thenewyear.net/

Apple podcasts: https://itunes.apple.com/us/podcast/brain-inspired/id1428880766?mt=2
Spotify: https://open.spotify.com/show/2UZj8c8Ap5oc2gh2rJxLLe

Srini is Emeritus Professor at Queensland Brain Institute in Australia. In this episode, he shares his wide range of behavioral experiments elucidating the principles of flight and navigation in insects. We discuss how bees use optic flow signals to determine their speed, distance, proximity to objects, and to gracefully land. These abilities are largely governed via control systems, balancing incoming perceptual signals with internal reference signals. We also talk about a few of the aerial robotics projects his research has inspired, many of the other cognitive skills bees can learn, the possibility of their feeling pain , and the nature of their possible subjective conscious experience.

0:00 - Intro
3:34 - Background
8:20 - Bee experiments
14:30 - Bee flight and navigation
28:05 - Landing
33:06 - Umwelt and perception
37:26 - Bee-inspired aerial robotics
49:10 - Motion camouflage
51:52 - Cognition in bees
1:03:10 - Small vs. big brains
1:06:42 - Pain in bees
1:12:50 - Subjective experience
1:15:25 - Deep learning
1:23:00 - Path forward
---

# BI 134 Mandyam Srinivasan Bee Flight and Cognition
**Brain Inspired:** [April 27, 2022](https://www.youtube.com/watch?v=mdUMLtP6ESA)
*  I would say that no organism perceives the whole world in its total reality as it is,
*  I would say.
*  Each animal experiences the world through the window of its own visual and perceptual
*  capacities and its limitations.
*  You don't need to be necessarily slavishly biomimetic.
*  Our idea was to basically test to see whether the principles we extract from honeybee vision,
*  flight and navigation guidance, for example, can you use optic flow information to do all
*  the things that insects do.
*  You know, for a long time bees and other insects were really considered to be rather simple
*  reflexive automatons.
*  Pattern recognition in bees has gone a lot beyond this over the last few decades, so
*  they're able to learn abstract properties of patterns.
*  This is Brain Inspired.
*  Hello good people, I'm Paul.
*  So it's often stated that the human brain is the most complex object in the universe.
*  That's probably not true, but we do know it is complex, and our efforts to understand
*  how our brains work and or to build human-like intelligence is constantly running up against
*  that complexity.
*  Of course, we study the brains of other organisms as models or a proxy of our own brains, hoping
*  we can extract general principles often from brains much smaller than our own.
*  For example, the bee has a brain with about 1 million neurons.
*  That's a big number, but it's also tiny compared to our 86 billion neurons.
*  That organisms like bees with relatively few neurons keep surprising us with impressive
*  feats of intelligent behavior.
*  Today my guest is Manjam Srinivasan, or Srini, who's an emeritus professor at the Queensland
*  Brain Institute in Australia.
*  So you know about the bee waggle dance, I'm sure, where a bee will fly to a location and
*  forage in that location and then fly back to the hive and do a little dance to communicate
*  to the rest of the hive where the good food is.
*  Srinivasan has for a long time studied the abilities of bees and other insects and birds.
*  In this episode, he shares much of what he has discovered, specifically about bees and
*  how they navigate and how they use perception to control their flight speed and path and
*  their graceful landings, for example.
*  We also discuss a few of Srini's robotics projects where he applied principles of bee
*  flight to create fully automated aerial robots that can take off and fly and maneuver and
*  land quite well.
*  And beyond flight, we also discuss some of the higher cognitive abilities bees can be
*  trained to perform, the possibility of their having subjective experience and their capacity
*  to feel pain.
*  In the show notes, I'll link to a nice review that summarizes a lot of what we talk about
*  in this episode.
*  Show notes are at braininspired.co.
*  slash podcast slash 134.
*  Thank you to my Patreon supporters.
*  Here's a little something extra for you today, which I hope captures my gratitude for your
*  support and bonus points if you can reference this little ditty.
*  Thank you for being a friend.
*  Travel down a road and back again.
*  Thank you guys.
*  Okay, enjoy Srini.
*  When I got into neuroscience, like many people, I was interested in the quote unquote big
*  questions like consciousness and I ended up studying monkeys in a laboratory setting.
*  Why, why insects?
*  And I don't mean that as an insult.
*  What drew you into studying bees and insects and birds?
*  Okay, thank you, Paul.
*  Thank you for having me.
*  First of all, it's a great, great, great delight and a great honor to be with you on
*  the show.
*  Yeah, thank you.
*  So just a little bit about my background.
*  I was I was born and raised in India.
*  I did my bachelor's degree in electrical engineering and my master's degree in control systems
*  in Bangalore.
*  And towards the end of my master's degree, I think I underwent a kind of a premature
*  midlife crisis.
*  I wanted to pursue something other than just a straight standard career as an electrical
*  engineer.
*  So one of my professors suggested that I could try to maybe apply my knowledge in EE, electrical
*  engineering and control systems to modeling the function of a biological system.
*  So we decided to model a system that controls the movement of the human eye when it tracks
*  a moving target, modeling it as a server mechanism, you know, feedback control server mechanism.
*  Smooth pursuit, the smooth pursuit.
*  Smooth pursuit and saccadic movements.
*  Yes, that's right.
*  Yeah.
*  And this turned out to be a very engaging sort of project and it was a lot of fun.
*  And so when I went to Yale to pursue a PhD in engineering, I was again keen to do research
*  that was sort of at the interface between engineering and biology.
*  And the only person I could find there at that time who had similar interests was a
*  professor by the name of Gary Bernard and who was studying and modeling the optics of
*  insect eyes.
*  This sounded quite interesting and I jumped right into it.
*  In those days, you didn't worry about future career prospects.
*  You just followed your heart, you know, and let things happen and it was wonderful.
*  Maybe things are not the same these days, unfortunately.
*  How is it different these days?
*  Oh, my students, for example, are constantly worried about, you know, whether this project
*  is going to get them a job, going to allow them to continue in academia, you know, sort
*  of that sort of thing.
*  What's in it for me?
*  They're not so interested in what the intrinsic questions that are being asked and how interesting
*  they are.
*  That seems to be secondary.
*  So you went kind of naturally went from control systems and engineering into studying what
*  has, you know, classically been studied from kind of an engineering perspective because
*  the psychotic eye movement system and the smooth pursuit eye movement system are both
*  very well understood circuits.
*  So that was probably a...
*  Yeah.
*  And then that was probably a smooth transition to the optic studies in insects.
*  Exactly, exactly.
*  It seemed an interesting thing with the PhD was that Gary himself was really more into
*  the optics and the photoreceptor aspects of it, whereas I was more interested in sort
*  of higher level processing that drives the behavior.
*  So it let me be fairly independent as a PhD student.
*  And you know, so it was nice.
*  We had almost like two separate sort of things going on in the same lab, which is really
*  good fun.
*  So it taught me to be a little more independent, you know, fairly early in my career, which
*  is really good.
*  That's a nice balance.
*  Do you recommend that kind of balance if, you know, thinking about people have struggled
*  to find the right advisor and what's the perfect match?
*  And so are you suggesting that it might be nice to have...
*  Yeah, ideally, if there's funding to allow a student to do whatever they want to do for
*  their PhD, and if the supervisor, in this case myself, feels competent enough to, you
*  know, supervise that particular project, then that would probably be the best solution.
*  Unfortunately, there's so many different constraints because students come quite often, you're
*  hiring them through a grant, which forces you to do a particular kind of project and
*  you have to sort of keep them on that straight and narrow project to make sure that the project
*  succeeds.
*  Right.
*  And there are all these constraints which are really...
*  It's sad, but it wasn't there in the old days.
*  It was so different.
*  You went to register to do a PhD with a professor, you had your fellowship or scholarship and
*  off you went.
*  There were no constraints.
*  All you had to do is to do good work and produce a lot of good publications and that
*  was it.
*  Well, those problems are behind you, right?
*  Because you're three years retired now.
*  Thankfully, yes, thankfully.
*  Nowadays, my engagement is all fun and no responsibility.
*  So I'm sort of a backseat operator in a couple of grants, research grants, but I'm not getting
*  any money.
*  I'm deliberately not asking for any money.
*  I just want all fun and no responsibility.
*  Oh, that's great.
*  So I'm kind of an armchair advisor, yeah.
*  Very nice.
*  Well, you've done a lot of work over the years on bee in particular navigation and you've
*  worked on birds as well and we may talk about birds, but mostly we'll probably talk about
*  bees and their navigation abilities and flight abilities and their cognition.
*  So give us a sample.
*  What has your work...
*  I mean, this is a...
*  I know it's an impossibly large question because you've done so much work, but what has your
*  work revealed about bee navigation and flight?
*  Yeah, sure.
*  I could start by telling you a little bit about how I got into bees in the first place
*  because at Yale, I was really working with houseflies, looking at the movement detection
*  system of the housefly and seeing how it guided course stabilization and how it also enabled
*  the flight to pick up small moving targets like other flies and chase them for the purpose
*  of mating or territorial defense.
*  So that was the project for my PhD at Yale.
*  But then I moved on to do a postdoc at the University of Zurich in Switzerland where
*  I also had to learn German and lecture in German.
*  Oh my gosh.
*  But anyway, that was quite a challenge, yes.
*  Are you still fluent?
*  Poor students.
*  Well, not anymore, but even when I was fluent, it was stressful for me.
*  It was also even more stressful for the students because the poor student had to kind of try
*  and understand what I was trying to tell them.
*  But Zurich was such an amazing place.
*  It was the department of professor Rudi Gavreina who introduced me to the world of bees.
*  And it was there that I realized that the bee is an amazing learning machine.
*  And what I found, not only can they learn amazing things very quickly, but what's really
*  appealing is that you can study their behavior by tapping into their natural lifestyle.
*  So you can sort of entice the bee to come into your lab, draw it in with a nice sort
*  of sugar water, move the sugar water feeder step by step into your lab.
*  And they're coming in of their own free will.
*  I mean, there's no coercion here.
*  They're free to go somewhere else if they find better food.
*  But we have a very strong sugar solution that they find quite tempting and they come.
*  And the thing is you're catching them, you're sort of observing them in their sort of natural
*  style of behavior.
*  And so you're not really being forced, not like a caged rat or mouse that you're trying
*  to train, right?
*  It's really a freely moving, behaving animal.
*  And also, once you have them coming into your lab and visiting your apparatus, which you've
*  designed to try and answer the question that you've set up, I mean, they fly back and forth
*  and you can film them in a way that actually addresses the question that you want to answer.
*  If you're studying another creature, for example, like a fly or a dragonfly, you have to have
*  your camera strained on the creature all the time and then wait until you find the right
*  moment when that behavior occurs, right?
*  Whereas here, you don't have to do that.
*  You have them directly coming to you and they're doing exactly what you want them to do in
*  the right location.
*  So you've got full sort of observability, I would say, a very efficient way of kind
*  of observing and recording what they're doing in the lab.
*  So that was really very nice about bees.
*  And of course, no bees are hurt or harmed in the whole process.
*  Once you finish the experiments, they're free to go back and continue the normal foraging
*  lifestyle.
*  How long does a bee live?
*  I forget.
*  They live about four weeks at most.
*  But typically, our experiments run for three or four days.
*  And for three or four days, you've got the answers you want.
*  Either you've got them or you don't have them.
*  But in three or four days, you let them go.
*  It must take what takes probably what, two days to entice them in with the sugar water
*  and get them comfortable coming in?
*  No, no, no, no.
*  Well, it depends.
*  No.
*  Well, in Zurich, we had the way it works is that you have a, we were working in one of
*  the upper levels of the building and there's a balcony outdoors.
*  So over there, you have a sugar water feeder there permanently all the time.
*  So bees already know that location.
*  There's a few beehives sort of on campus, but they don't necessarily have to come from
*  any of these beehives either.
*  They can come from anyone's home.
*  Someone could have a beehive at their home.
*  They could come.
*  And what you do is, the way you start an experiment is the sugar feeder solution outdoors in the
*  balcony is not very strong.
*  It's moderate.
*  So it keeps the bees interested.
*  So one bee comes along and then sort of tastes it and says, go back and does it.
*  If it likes it, it goes back and does a dance and tells all the other bees, hey guys, there's
*  something interesting.
*  Come and check it out.
*  So more and more bees come in and you have a steady stream of bees coming in and visiting
*  that feeder.
*  Now, if you want to start, when you want to start an experiment, you take this feeder
*  and then move it in step by step into the lab, through the doorway, into the lab.
*  forwards by about a foot every five minutes.
*  So in fact, people have found that bees can actually predict if you're steadily moving
*  a feeder, they actually predict the speed of movement of the feeder and look ahead when
*  they come next time on the next visit.
*  So they go, they predict the next location.
*  And you said that the sugar water was weak at first.
*  Are you strengthening it as you move it?
*  Yeah, we're strengthening it.
*  Sorry, thanks for pointing that out.
*  Yes, we're strengthening it.
*  And it gets more bees excited, of course, and there's more and more bees coming in
*  and you're ready to start the experiment.
*  But you don't want 100 bees visiting your apparatus.
*  So what you do is at that moment, when you've got the right number of bees coming in, you
*  mark them individually with colored dots.
*  And then at the same time, you place another feeder outside the door.
*  And that's a weaker sugar solution.
*  That acts like a sort of a decoy because the new recruits that have been recruited by
*  these very enthusiastic bees that are going back home and dancing, they come and look
*  at the most obvious spot, which is the feeder outside.
*  And they have a taste of that sugar water solution.
*  It's not as good as it's cracked up to be.
*  It was a false alarm.
*  And so they get disappointed and don't come back again.
*  So that way you can control the number of bees that are coming in and make sure it's
*  only the bees that you marked individually that keep coming again and again faithfully
*  and all the other bees, the sort of recruits come outside and get disappointed and they
*  don't enter the lab.
*  So they don't disturb the experiment.
*  A lot of what you have done with bees are behavioral experiments looking at how they
*  navigate, right?
*  So as they're coming in, I mean, you can describe this much better than me, but as they're coming
*  in, you're then having them fly through like different tubes and different, you're putting
*  different optical shapes and patterns that shows how their flight varies.
*  And through this, you've found out a bunch of stuff.
*  I don't know, how would you summarize some of what you've learned about how they do it?
*  Well, I mean, it all started with a fairly random chance observation.
*  We found that when bees were entering our lab, some of them would take a shortcut and
*  fly through a hole in the wall rather than fly through the open door.
*  And we noticed that when they flew through this hole, they were flying fairly precisely
*  down the middle of the hole.
*  And we wondered about that because how can they actually fly so precisely down the middle
*  when in fact they cannot measure distances the way we do because the stereo vision is
*  sort of compromised because the two eyes are actually very close together.
*  And if my eyes are fairly far apart, they're about eight centimeters apart, I think.
*  So if I look at my finger with one eye and then with the other eye, the image of the
*  finger is displayed between the two eyes, right?
*  And so your human stereo system is working out the triangulation.
*  It's measuring that disparity or displacement and working out how far away your finger is.
*  So that's how 2D mesmeristereo works, right?
*  But if you now take these two eyes and move them progressively closer and closer together
*  until you come to the point where the two eyes are actually a couple of millimeters
*  apart, that shift or disparity becomes very small and it's very hard to measure.
*  So insects really cannot rely on stereo unless some object is very close, in which case you
*  start to get a bigger shift, angular shift, I should say.
*  So insects really have sort of evolved or come to rely on a completely different way
*  to see the world in 3D and that's to actually move in the world actively and look at how
*  rapidly images move in their eyes as they move past them.
*  And if something is nearby, it moves very rapidly if you move in a straight line.
*  And that tells you that this rapidity of eye movement tells you, well, image movement
*  motion tells you that this object is very close.
*  Whereas something is very distant like a hill or clouds in the sky, those don't move very
*  much at all if you're moving in a straight line.
*  And that tells you that those objects are actually very far away.
*  So insects have somehow evolved to translate image motion into three-dimensional object
*  distance.
*  And we're doing that too, unconsciously.
*  When we move with one eye closed, we are in fact taking advantage of eye movements and
*  head movements and eye movements to gain some information about the three-dimensional percept
*  of the world.
*  But all this has come about starting from, you know, this is what I was saying, to go
*  back to what I was saying, the bees flew down the middle and we're saying, given the fact
*  that these bees don't have stereo, how could they possibly be gauging the distance and
*  balancing them on the two sides, right?
*  So one thing we wondered was, are they really sort of flying through the passage in such
*  a way that the two rims seem to move past their eyes, past the two eyes at the same
*  speed?
*  That's one way of balancing your sort of position in the middle of the hole, right?
*  That was your first guess?
*  That was the first guess, yeah.
*  Wow, okay.
*  All right.
*  How often does that happen?
*  So that was a very lucky guess.
*  I mean, it could have been wrong.
*  So we put bees in this tunnel and then we had, in the old days, we had conveyables to
*  move the walls, you know, with that shrub patterns and we moved them.
*  Of course, you had a perspective sheet in the middle to make sure there were no wind
*  currents that could influence their flight.
*  So the bees would be flying down this tunnel to the end to get a food reward and then they'd
*  fly back and we filmed their flight trajectory from above to see how they flew when they
*  flew down the tunnel.
*  And when they flew down, when both walls were stationary, they flew fairly precisely down
*  the middle.
*  Well, give or take one or two centimeters, but they're bees, they're only human, they
*  make mistakes too, but fairly precisely down the middle.
*  However, when we took one of these walls and moved it in the same direction as the incoming
*  bee, then the bees flew a lot closer to the moving wall.
*  And we think this is because when the bee and the wall are moving the same direction,
*  the image velocity as seen by that eye is much lower, right?
*  So the bee thinks that wall is much further away.
*  So she moves closer to that wall to make up for it.
*  To get to the center, to where she thinks the center is.
*  Exactly, she thinks she's entering, yeah.
*  And exactly the opposite thing happens when you move this wall in the opposite direction
*  to the bees' incoming flight direction.
*  Because then you've got a large image motion on this side, so the bee thinks, hey, there's
*  something dangerously close to this wall, to the surface, I'm very close to the surface,
*  I better move away from the surface to compensate.
*  So this simple experiment really taught us that bees really are flying through these
*  narrow passages safely by balancing the optic flow, as they say, in the two eyes.
*  And you can also make predictions about where should they position themselves if you move
*  one of these walls at a certain speed, for example.
*  You can do the little mathematical calculation and work out where they should be, and it
*  seems to fit really quite nicely.
*  So that seems to be the way they're actually flying down in the middle.
*  But once we had the tunnel going, there were lots of other experiments we could sort of,
*  things we could test.
*  For example, control of flight speed, how do they control their speed?
*  We noticed that if it's a constant width tunnel, they fly at a fairly constant speed right
*  through the tunnel.
*  Initially, what we did was, when they're flying through this tunnel, the walls were stationary.
*  Now what we did, they flew at a certain speed.
*  Now we moved both walls forward at a certain speed, and the bees increased their speed
*  by the same amount as the wall speed.
*  And when you move both walls backward, the bees slowed down by the same amount as the
*  wall speed.
*  So what they're trying to do is to keep constant the angle of velocity of the image that the
*  two eyes are experiencing as they fly through this environment.
*  And this is one way of controlling or regulating your flight speed.
*  When they're flying in an open field though, for instance, when everything is essentially
*  at infinity or something, are they going back?
*  Exactly, exactly.
*  Bingo, you hit the right question.
*  So the next question is the tapered tunnel.
*  So if you fly them through a tapered tunnel, initially the walls are fairly far apart,
*  and the bees are flying at a certain speed.
*  So by the way, that first experiment with the static tunnel or the walls moving in the
*  same direction backwards or forwards told us that they're trying to hold an angle of
*  velocity of about 300 degrees per second constant as they're flying through this tunnel.
*  Now if you go to this tapered tunnel, which is wide to begin with and then narrows down,
*  you find initially when they come in, they fly at a certain speed, fairly high.
*  And as they progressively move into the tunnel and the tunnel narrows down, they fly slower
*  and slower.
*  So what seems to be happening is they're trying to keep this image velocity constant throughout
*  the passage, but initially they're keeping it constant at 300 degrees per second, let's
*  say.
*  And then as they go in closer, the walls are much further, the walls are much closer, so
*  it increases the angle of velocity of the image, right?
*  But the bees think they're speeding up, so they're slowing down to compensate for that.
*  And so they keep slowing down further and further until they reach the narrowest part
*  of the tunnel, which is the neck.
*  And then when they're asked to flare out again, they speed up again.
*  And even through this tapered tunnel, they're maintaining a constant image velocity of 300
*  degrees per second.
*  This is a very nice way to ensure that when you're flying in a wide open environment,
*  you fly fairly fast.
*  And when you enter a dense cluttered environment, you automatically slow down.
*  And the nice thing is you don't need to do the standard thing that computer vision people
*  and machine vision people will be doing to measure distances to various obstacles and
*  saying, hey, what should my speed be?
*  You just measure the global average image velocity so that when you're flying in an
*  open meadow, you fly fairly fast.
*  When you enter a forest or something, you automatically slow down to an appropriate
*  speed.
*  So they must have an internal reference signal that they're trying to match, essentially,
*  that 300 degrees per second.
*  And so that's kind of like in control theory terms, that would be the reference signal,
*  but that would be an internal innate, I suppose, innate signal.
*  I don't know if you meant it this way, but you said they think that they're slowing
*  down or they think that they're speeding up, depending on how you manipulate their
*  environment.
*  But then as they actually are slowing down or speeding up, they also must have an internal
*  reference signal for the output of their wing expenditure.
*  Sure, sure, sure.
*  I'll use that term just to make the explanation more.
*  They could have trusted you, exactly.
*  Wingbeats, of course, is one thing.
*  There's also the airspeed.
*  You could be flying against headwind or tailwind.
*  So they have many insects have these hairs on the thorax and the abdomen and the antennae
*  as well, which act as wind sensors, so air flow sensors.
*  So they're measuring their airspeed as they fly through the environment.
*  And these also are not really well studied.
*  We don't know exactly how the weather study affects their flight behavior, but they're
*  certainly there.
*  Those sensors are there.
*  So you solved B flight, optic control flight there.
*  Well, there was one part of it.
*  The next step, can I describe the next step?
*  Oh, yeah, please.
*  I want to ask you about landing in a second too.
*  Landing is well, before we go into landing, this was more about flying through the environment,
*  going to a food source.
*  How do bees work out how far they are flown?
*  Because bee that's gone to a particular food source has to come back and signal through
*  its dance how far it's flown and gives the information in polar coordinates, right?
*  The distance as well as the direction to go.
*  So the direction of the dance, the Weigel dance, is a measure of the indication of direction
*  in which to go.
*  And the duration of the Weigel dance has information about how far away the food source is.
*  The longer the duration of the Weigel, the further away the food source is.
*  So there's a roughly linear relationship between the two.
*  Now how do they work out how far they've gone?
*  Now we're not the first ones to have done this.
*  Carl von Frisch, the Nobel laureate who did all the wonderful work on bees, every aspect
*  of bees, looked at this too.
*  He did something really quite clever.
*  What he did was he had bees flying from a hive to a feeder, and he sort of 500 meters
*  away, let's say, quite some distance away.
*  And when they came back, he looked at their dance and filmed it.
*  They were indicating, you know, they had calibrated it for 500 meters.
*  And then he put these tiny lead weights on the bees and made them fly the same distance.
*  And when they came back, they were now reporting a much larger distance.
*  So von Frisch decided that this was probably, they're using a measure of energy consumed
*  to signal the flight distance, right?
*  That seems like the most obvious thing when you're carrying a weight.
*  We think that may not be the case.
*  So what we did was the following.
*  We trained bees to fly down this tunnel again, a very short tunnel.
*  In this case, it was about, I think, about eight meters, a fairly short, narrow tunnel
*  to a feeder, and then come back.
*  And even though they flew only this very short distance of eight meters, they were signaling
*  something like 300 meters in their dances.
*  They were being comprehensively, they were comprehensively overestimating the distance.
*  And we wondered why is this going on?
*  And one of the possibilities was that they could be measuring not this flight energy
*  consumed, but actually measuring how far the image of the world, how much the image of
*  the world had moved past their eyes as they fly from their hive to the food source.
*  So they're measuring it visually.
*  Now, the thing is, because the walls of the tunnel are very narrow, even a small amount
*  of forward motion causes a huge amount of image motion, right?
*  So the things have gone a long way.
*  So it's a bit like, you know, if I were to fly from, let's say, Brisbane to Sydney and
*  look down at the ground, the ground is so far away, it wouldn't appear to be moving
*  at all.
*  So I wouldn't think I've gone a long way.
*  Whereas if I were to drive from Brisbane to Sydney, everything is very close to me.
*  There's a lot of image motion and I think I've gone a long way.
*  So we think that the odometry, the bees' odometry is working visually.
*  And the way to test this, of course, is to remove that image cue, that image motion cue,
*  and see what happens.
*  So if you, normally the tunnel would have a textured pattern, a randomly textured pattern
*  or vertical black and white stripes.
*  But if you change that and make the stripes horizontal, then when the bees are flying
*  down the tunnel, the same tunnel, they don't experience any optic flow because they're
*  flying parallel to the stripes.
*  And then when they come back home, they dance again, but signal almost zero distance, right?
*  So they really are.
*  So it looks like the odometer is really visually driven.
*  What we think went wrong with, well, not wrong, it was the wrong interpretation maybe, with
*  Karl von Fischer's experiment was that when you load these bees, they probably tend to
*  fly closer to the ground.
*  That increases the optic flow produced by the ground.
*  And so their odometer is telling them they've gone much further distance.
*  That's a nice segue into the landing.
*  I want to come back also to, I mean, there's a lot of questions I have, but I don't know
*  if this is the right time then, because their landing is controlled, I suppose, by a very
*  similar optical flow kind of system, correct?
*  Yeah, yeah, that's the thing.
*  So the same system that keeps the flight speed constant or tries to keep the image velocity
*  constant at about 300 degrees per second when they're cruising, that same thing is put to
*  a different use when they're landing because we thought, okay, the way we did this was
*  to simply train bees to come and land on a drop of sugar water placed on a horizontal
*  textured surface.
*  It could even be a wooden table with some grains so that you could get some texture
*  that they can see.
*  And if we fill them in three dimensions as they came into land and analyze the flight
*  trajectory data, and we found that it's a very simple thing.
*  When they're flying high, they're flying fairly fast, and they fly low, they're flying
*  slow.
*  And in fact, the speed of flight, the speed of approach, I should say, to the target is
*  very strictly proportional to the height above the surface.
*  And what that is telling us is that they're actually, as they're coming in, they're keeping
*  the image velocity of the ground constant in their eyes as they're coming into land,
*  right?
*  If you were sitting in a plane, for example, and looking out the window, the ground beneath
*  you as a pilot is coming into land, as you get closer and closer to the ground, you find
*  the image of the ground appears to move faster and faster, right?
*  But that's because the pilot is not slowing down.
*  The bee doesn't do that.
*  The pilot comes in at a constant velocity.
*  The bee slows down appropriately at every time to keep this image velocity constant.
*  And this automatically ensures that when it's coming back very close to the ground, it's
*  flying with almost zero velocity so it doesn't burn its feet when it makes contact with the
*  ground.
*  So it's a very nice low impact landing strategy.
*  And the beauty about this is you don't need to know at any time how far away you are from
*  the surface.
*  You don't need to know how rapidly you're approaching it.
*  All you need to do is to measure the image velocity initially and keep that constant.
*  Adjust your speed to keep that constant as you're coming in to land.
*  And bingo, you've done it, right?
*  There's a beautiful biological autopilot to make a nice smooth landing.
*  Yeah, it's an elegant and very simple way.
*  Yeah, that's right.
*  So that was on the horizontal surface.
*  But what we then did was to look at landings on a vertical surface like this where the
*  bee has to come and dock, for example, a flower or something.
*  When you do a grazing landing on a horizontal surface, the image velocity, the image motion
*  is mainly from front to back in your eye as you look down below in your ventral field
*  of view.
*  Whereas if you dock a flower to approach a vertical plane, for example, a flower in a
*  vertical plane, what you see is an expanding images like watching a Star Wars movie or
*  something like that.
*  Different pattern of optic flow.
*  So we also wanted to know whether you know what do we do to use a different strategy
*  for landing on horizontal surfaces as opposed to vertical surfaces because the pattern of
*  optic flow is different.
*  So we tried to do this by having bees come in and land on a vertical pattern.
*  But the pattern in this case had a spiral on it.
*  And I'll tell you the reason for the spiral.
*  But first of all, we found that as the bee came in and approached the thing, it again
*  did the same behavior.
*  So when it was far away from the spiral, it was approaching fairly fast.
*  As it came closer and closer to the thing, it slowed down progressively.
*  And again, a nice linear relationship between approach velocity and distance to the actual
*  landing target.
*  So we thought again, okay, it must be something to do with image motion.
*  But now the nice thing about the spiral, because bees are experiencing a kind of an expanding
*  pattern, right?
*  As they approach the target.
*  That's what happens when you approach a target frontally.
*  You see something expanding.
*  Now the nice thing about the spiral is you can artificially manipulate the rate of expansion
*  by spinning the spiral in a way as to make it either expand or contract.
*  When you rotate the spiral to make it appear to expand, you're increasing the apparent
*  rate of expansion that the bees experience as they approach the target.
*  We find that the bees then hit the brakes and approach the target more slowly in order
*  to maintain the original rate of expansion.
*  On the other hand, when the spiral is rotated to create an apparent contraction, the bees
*  approach the target more rapidly.
*  The simple experiment tells us that the landing bees are approaching the spiral in such a
*  way as to hold the apparent rate of expansion of its image constant.
*  So that simple experiment tells us that they're doing the same thing.
*  It doesn't matter whether you're approaching a horizontal surface or an oblique surface
*  or a perpendicular surface.
*  All you have to do is to look at that total optic flow that surface is generating around
*  the target that you're going towards and keep that flow constant.
*  No matter what it is, just keep that hold that constant as you're coming into land
*  and you've done your job.
*  So it's a very simple, simple, elegant way of thinking, which we wouldn't have even
*  thought about until we started to look at these bees by doing a very simple experiment
*  and measuring their flight as they landed.
*  Well, you know a lot more about engineered flying systems.
*  So I wanted to ask you about robotics in a second, but just as an aside, one of the
*  things you were talking about how when you change their perception of how fast they're
*  flying or how slow they're flying, et cetera, they will come and report through their waggle
*  dance incorrect distances, incorrect distances and directions.
*  However, as you point out in some of your talks, it doesn't matter because if the other
*  bees take that same route, they're going to have that same error.
*  So it's a fine dance.
*  Exactly.
*  So yeah, yeah.
*  So if a bee flies through an open environment, if I'm the meters, it'll come back and signal
*  some distance.
*  But if it flies the same through a different environment and flies the same distance, for
*  example, through a forest, it'll come back and signal a much bigger distance.
*  But as it turns out, all the bees that follow the dancing bee will take the same route as
*  the bee took the original scouts bee took.
*  So they'll change the same environment.
*  So it doesn't matter if you're a ruler, you're measuring yardstick or something is not perfectly
*  calibrated because as long as all bees use the same yardstick, it doesn't matter.
*  Everything cancels out.
*  Right?
*  So that's the thing, I think.
*  So it's really tied to the perceptual capabilities and skills of, in this case, bees.
*  What I was going to ask you is, there's a lot of talk these days about ecologically
*  valid studies and umwelts, you know, like the different organisms relations, like their
*  specific environment and what they're evolutionarily honed for.
*  So does this, in your eyes, does this tell you that what we are perceiving as organisms
*  isn't necessarily veridical, as in the real world, but it's just based on our perceptions?
*  And if you and I share the same perception systems, we're going to make the same errors,
*  they're not errors to us because we're following our own subjective, evolutionarily honed abilities.
*  Yeah, exactly.
*  Exactly.
*  You know, I would say that, you know, no organism perceives the whole world in its total reality
*  as it is, I would say.
*  You know, I don't think there's a totally true or complete representation of the world
*  in any creature, you know, including humans.
*  What?
*  Or for that matter, even in the machine.
*  Because each animal experiences the world through the window of its own visual and perceptual
*  capacities, right?
*  And its limitations.
*  For example, insects have poorer spatial acuity than humans.
*  So their vision is not as sharp as us.
*  So there's about their visual resolution is only a factor 60, a factor 60 poorer than
*  humans.
*  But they have much higher temporal acuity.
*  They can see the flicker in the fluorescent lamp, for example, which is flickering.
*  Well, in your country, it's 60.
*  60, yeah, I think so.
*  60.
*  So 120 flashes per second.
*  And they can see that clearly, whereas we cannot.
*  So our eyes are sluggish, but sharp, especially.
*  And theirs are sort of not that sharp in terms of spatial resolution, but they're very,
*  very rapid responding.
*  And so they need that because they're flying through dense environments and things are
*  very close to them.
*  So they want to see lots of objects without blur when things are moving rapidly past their
*  eyes.
*  And insects can see in the ultraviolet, which we cannot.
*  Right.
*  They can see patterns in flowers, ultraviolet marker patterns in flowers, which bees use
*  to lead them to the nectar.
*  We cannot see that.
*  We can perceive polarized light in the sky, which we cannot.
*  So the visual world is entirely different from ours.
*  So what is really real, which is hard to decide, is the eagles have higher visual acuity than
*  us.
*  They can see much better resolution than us.
*  So yeah, so every person has their own world, I think.
*  Even across humans, I don't know if we can say that all humans perceive and recognize
*  objects in the same way.
*  I mean, both you and I could agree.
*  Look at a car and say, OK, this is a particular model of Ford.
*  But whether your brain responds in the same way as mine does, I don't think we know yet.
*  Right.
*  And even if it doesn't, it doesn't matter.
*  As long as we both agree.
*  I mean, you have a certain pattern of activation in your neurons that says it's a model Ford.
*  And mine says, OK, it has a certain pattern of activation, but I've learned that that
*  is a model Ford.
*  So we both agree it's a model Ford.
*  But the representation might be quite different, right?
*  We can't be sure.
*  And you're red and my red.
*  Who knows if they're the same, right?
*  Exactly.
*  Exactly.
*  Well, let's do you want to shift and talk a little bit about the robotics that you've
*  been developing also?
*  I know you have a few projects that have been directly based on these optic flow studies
*  in insect navigation.
*  Yeah, it's interesting.
*  I mean, the way we got into robotics also was quite sort of accidental because we were
*  really looking at doing basic bee research.
*  And then at one stage, somebody from DARPA, who happened to be at a conference where I
*  was talking, approached me later and said, hey, would you like to get some money to work
*  on developing biologically inspired studies for flying machines?
*  And it sounded like a good idea.
*  We didn't go looking for it, but we sort of got enticed into it.
*  I was imagining that you had that in your kind of back pocket the whole time coming
*  from that engineering background.
*  No, it's strange.
*  Yeah, it's strange as an engineer.
*  It's so stupid that I didn't even think about it.
*  Even the thing about navigating safely down a corridor by balancing the optic flow, the
*  first people to actually pick up that idea and use it to navigate robots were not people
*  from our lab.
*  It was people in labs in Italy and in France and so on.
*  So they were using it and they said, hey, my God, why didn't we do that?
*  But we weren't really, we were really looking for, we're just having fun with these insects.
*  It's enjoyable work, isn't it?
*  Yeah, that's right.
*  Nowadays, of course, I think the way research goes is that you tend to be more applications
*  oriented.
*  You have to be that way because your application and the grant application depends very much
*  on how you can tout how relevant this research is going to be.
*  That again, is something that was not there in the old days, which is something I again
*  miss very much.
*  You have to either cure disease or build a good robot or something like that.
*  Exactly, exactly, exactly.
*  Bingo, you've got it.
*  Oh, I know.
*  Yeah.
*  So, okay.
*  Do something useful, yes.
*  So is the DARPA money that got this off the ground, so to speak, pun intended there?
*  Exactly, exactly, exactly.
*  So we're very thankful to DARPA for that.
*  Of course, in a way, working for military funding organizations, we're also involved
*  in that with the US Air Force and Office of Naval Research and so on later on.
*  But there's good in that.
*  You always worry about whether what you do could be used incorrectly and things like
*  that.
*  But it turned out it was actually very good.
*  DARPA especially was really very keen on promoting basic research.
*  They wanted us to publish our work in good journals.
*  They were not trying to keep it classified or anything like that.
*  So I really appreciated that.
*  Well, one of the things that you have worked on, and I don't know how many of these different
*  robotic systems you want to talk about, but one of them is like a bi-winged plane, like
*  a standard model plane.
*  But then you install kind of a fly navigation system using the principles.
*  That's right, that's right.
*  But before, I'd like you to describe that.
*  So there's this kind of tired trope of how much biological detail do we need to build
*  into, for example, AI, right, into artificially intelligent systems.
*  And often the example people use is, well, we didn't, you don't want to build wings
*  to build flight.
*  You want to use the principle of airlift and aerodynamics, right?
*  However, not all flight is the same.
*  So sure, if you just want lift and propulsion, that's all you need.
*  But if you want fancy kinds of flight forward and backward, and if you want to navigate
*  in certain ways, then you do need something closer to wings.
*  So there's this ever present, at least in the AI world, right, that a lot of what we
*  talk about is how much biological detail do you really need to build in?
*  Yeah.
*  So how did you decide what to build in and which systems?
*  So yeah, yeah, our sort of way of thinking about this, it's a very good question there,
*  Paul.
*  Yeah.
*  And the way we consider it is to say, okay, it depends on the task you need to accomplish.
*  I mean, you don't need to be necessarily slavishly biomimetic in the sense that you copy everything
*  that you see in the insect, for example.
*  You don't need to build an insect compound AI with thousands of facets.
*  You don't need to have flapping wings.
*  Our idea was to basically test to see whether the principles we extract from honeybee vision,
*  flight and navigation guidance, for example, do they really, can you use optic flow information
*  to do all the things that insects do?
*  So what we do is we put together a vision system to emulate the almost panoramic vision
*  of an insect compound AI, two eyes actually.
*  So we did this by placing two wide-angle cameras back to back.
*  So that gave you an almost nearer, facing this way, one this side, one the other side.
*  So it gave you nearly panoramic vision, except for a small kind of blind zone in the back.
*  So that was the thing that we're using.
*  And we're using standard computer vision techniques to measure the image motion, the optic flow.
*  We were not trying to, you do it exactly how the insect does it, because we still don't
*  know by the way exactly how the insect measures true optic flow.
*  So we didn't want to wait for that to happen.
*  So we said, okay, this time we put on an engineering hat and measure optic flow using the traditional
*  well-known techniques.
*  And we're using this to control the flight speed to regulate the height above the ground.
*  So this is a fixed wing aircraft, as you said, with the nose cone, the propeller in the nose
*  cone was removed and mounted on the top of the wings to make room for the vision system,
*  which is in the front.
*  Okay.
*  So you get a nice clear view of the front.
*  So the optic flow is used to control the flight speed, to regulate the height above the ground,
*  to compute the distance traveled using odometry like bees do.
*  How big is this thing?
*  It's about, I think the span was about a meter and a half.
*  Oh, okay.
*  Pretty big, pretty good size.
*  Yeah.
*  Fairly big.
*  Yeah.
*  So we weren't trying to miniaturize at that stage.
*  We were just trying to basically see, you know, proof of principle kind of thing to
*  see if these ideas actually work.
*  And it seems to work quite well.
*  So the other thing we put in, which we hadn't done in our own research, but others had done,
*  is to use the horizon profile, panoramic horizon profile, to control the attitude, measure,
*  monitor and control the attitude of the aircraft.
*  So you see, for example, if you're flying and then the horizon appears to move up in
*  your left eye and down in your right eye, it means you've rolled or banked to the left.
*  Yeah.
*  And vice versa.
*  Whereas if the horizon appears to move up in the front, it means you're pitching down
*  and if it moves down, you're pitching up.
*  Right?
*  So you can use the horizon profile all around you to monitor and stabilize your attitude,
*  assuming that you're not flying in a canyon or something where the horizon is not flat,
*  the world is not flat, and you've got things sticking up on one side or the other when
*  you could get misled.
*  But if you're flying high enough above the ground, the horizon is usually very reliable.
*  And the nice thing about it is it's got a reference which does not drift with time,
*  unlike many of these inertial sensors, which actually errors accumulate with time because
*  they're integrating angular motions and the noise tends to cause all kinds of drift problems
*  and things like that.
*  So we found that this could really be used to stabilize the orientation of the aircraft
*  and basically its roll and pitch.
*  And so also you can use the horizon profile to do various aerobatic maneuvers.
*  So for example, all you need to do is to say, okay, I want the shape of the horizon profile
*  to vary from this shape to that shape to that shape as a function of time.
*  And you can do beautiful things like loops and rolls and implement turns and all kinds
*  of things just by using the horizon profile.
*  We don't know if intakes do it that way.
*  They do, well, lots of aerobatic maneuvers too.
*  And sometimes they do it without even the absence of a horizon, so they must be using
*  other sensors as well.
*  But we found that at least with the horizon, we could do all these things, not just go
*  from A to B and do a smooth flight, but also do these interesting aerobatics.
*  And the nice thing was these flights are completely autonomous, take off, cruise, control turns
*  and landing back in the airstrip.
*  And they're done without using any external information such as GPS or radar.
*  So you're being entirely self-sufficient and self-reliant just the way an insect or a bird
*  would be, right?
*  And so it's a nice backup system for when there's a drop-off of GPS or radio information
*  and things like that.
*  Well, I was going to ask, how does this compare?
*  I don't even know how autopilot works.
*  So like current autopilot systems, right?
*  They're using radar?
*  Yeah, to the best of my knowledge, they're relying entirely on GPS.
*  The pilot basically takes the plane off and then they basically sit back and relax and
*  the plane is guided by GPS all the way through until it comes to land.
*  And again, even the landing, I know some pilots friends who tell me, even the landing,
*  there's a landing beacon, there's a radar, you know, it sort of helps you come down the
*  thing as long as you stay within the beam, the plane automatically stays within the beam
*  of I think that's being projected up from the ground, right?
*  So it follows that beam down and it is so precise.
*  Unless something goes wrong, I've been told it's so precise that when it lands on the
*  runway, it lands directly in the middle of the runway so that there's a little cat size
*  in the middle of the runway.
*  They're hitting against the nose wheel and they're going bump, bump, bump.
*  So the only pilot intervention is to actually steer the aircraft slightly away from the
*  middle to get rid of this bumping noise.
*  So they're so precise, but they all rely on external information, you see.
*  So if something goes wrong, this is where I think something like what we're doing could
*  be helpful because you can then at least for some period of time, you can be self-sufficient.
*  Long range navigation becomes a problem because you know, all the materials and all the things
*  will start to build up and you can't really rely on that forever.
*  But at least for a short term, you can manage without any of these things that you normally
*  very crucially rely on.
*  So, okay, so that was the fixed wing aircraft, but you also worked on like smaller miniature,
*  smaller flight systems as well, right?
*  So quadroided drones and things like that, yeah.
*  So that was mainly to see if the same thing would work and when you had things like, you
*  know, vertical takeoff and landing systems and doing things like it was easier to do
*  this on a smaller scale because we were flying and you didn't have to go to an airstrip every
*  time to run these tests.
*  We could do it right on campus.
*  And we were also doing things like developing algorithms for detecting other moving objects
*  in the environment, which is actually quite an interesting challenge because, you know,
*  we are so good at even when we're moving, we can detect small objects on a moving environment,
*  right?
*  Like another car or a bicycle or something like that.
*  And you cannot just do it by measuring motion because if you're stationary, the world is,
*  the image of the world is stationary and if something moves within it, you can pick it
*  up.
*  But you're moving, the image of the whole world is moving in your eye and within that,
*  to pick something that's moving and decide whether it's really moving or just part of
*  the world moving past you is quite a challenge even for computer vision scientists and animals
*  and humans are also so good at it.
*  So we were developing algorithms that would sort of allow sort of detection of moving
*  a movement of self moving objects, the detection of movement of self moving objects.
*  Well, that's right.
*  You teach people how to creep up on other people without being noticed.
*  That's the other thing is motion camouflage as well.
*  That's the other thing.
*  That's the other thing that we didn't probably didn't get into.
*  Insects will camouflage their own motion when there's a lot of stealth there.
*  We did a bit of study and modeling of that too.
*  I could talk a little bit about that if you would like.
*  Yeah, I don't know if that's the work with the dragonflies that...
*  Yeah, yeah, yeah.
*  Can you just describe that because that's really neat stuff.
*  That's something we put into aircraft as well.
*  So just to see if we can get it to work.
*  Yeah.
*  So the idea is very simple.
*  So a couple of ways in which you can do it is one is to move in such a way that you're
*  maintaining a constant angle of bearing with respect to the...
*  See if there's a shadow and a shadowy, right?
*  So you're the shadow.
*  So you move in such a way that the line joining you with the shadowy always says that the
*  constant orientation.
*  If that's the case, then it looks like you're an object at infinity because you're not moving
*  in the eye of the shadower and so no danger is perceived.
*  The other way you could do it is to actually pivot about a fixed point behind you as you're
*  sort of tracking the shadower.
*  That way the shadower thinks it's just a stationary object over there, right?
*  So it can't be possibly coming towards me.
*  So as long as you don't get too close and you reveal any expansion cues in your image,
*  you can shatter them.
*  That way it turns out that hoverflies do that, dragonflies do that.
*  Yeah, so there's a lot of that sort of thing going on.
*  Yeah, motion camouflage as we call it.
*  So they've learned through evolution this natural mathematical relationship between
*  which camouflages their motion relative.
*  And that's how they intersect and consume other flying objects essentially, right?
*  Exactly.
*  Exactly.
*  Yeah.
*  I'm just picturing humans trying to do that.
*  Seems like a lot of effort to camouflage.
*  I've experienced it myself, not in terms of someone shadowing me, but if you're moving
*  along and driving somewhere like this and there's another road coming in from the side
*  and the car is moving along the road, maintain that constant angular bearing, you tend not
*  to notice it until it's quite close.
*  Oh, that's interesting.
*  People have also done psychophysical experiments with human beings after we published that
*  paper and then they found the same thing, that humans can also be fooled by the same thing.
*  Is that right?
*  It seems like a fun thing to try, but I'm not sure that that would be time well spent.
*  It's still a very interesting thing for the military as we all know.
*  Oh, that's true.
*  Yeah.
*  See, this is where the nefarious purposes come in.
*  So we should move on.
*  So far we've talked all about the navigational abilities and flight abilities of insects,
*  but you've also studied quote unquote higher level cognition in bees.
*  Maybe you can give us some examples.
*  Well, I can just list some off.
*  For example, that bees have working memory up to like five seconds.
*  They can do delayed match to sample tasks, which is like a standard kind of task.
*  They can count up to at least, I think, what is it, four?
*  There's like one, two, three, four, and then everything above four is another category
*  or something like that.
*  Right?
*  I want to ask you though, like what your...
*  So maybe before you give another example or your favorite example, how far we've come
*  in terms of learning about what bees and insects are capable of cognitively, but also your
*  own, how your mind has, I don't want to say changed, but developed in terms of
*  thinking about these capabilities.
*  And have you come to respect bees more over the years through like learning their abilities
*  and or what, how has your own outlook on bees changed over the years, I suppose?
*  Yeah, sure.
*  Very good questions for Paul.
*  So let's start quickly by summarizing what we found in terms of the bees perceptual capacities.
*  And then we could talk about the broader aspects.
*  That's okay.
*  Yeah, sure.
*  So, you know, for a long time, bees and other insects were really considered to be rather
*  simple reflexive automatons that would learn just very simple associations.
*  For example, the blue dish carries a food reward, the yellow dish, no food.
*  So you can train bees to choose the blue over the yellow very quickly.
*  By the way, bees will learn these things in four or five rewards is all it takes.
*  Five minutes.
*  Wow.
*  Well, they don't have long.
*  They have to learn fast.
*  I would say five minutes, maybe half an hour.
*  They have to go back home and come back again.
*  So, you know, five rewards and half an hour and they've learned the color.
*  But it seems like pattern recognition in bees has gone a lot beyond this over the last few
*  decades.
*  So they're not just learning, for example, with learning shapes of flowers or something
*  or objects.
*  They're not really learning them in a photographic way, you know, a little eidetic way, as they
*  say, you know, pixel for pixel, memorizing the content of the image, you know, pixel
*  by pixel.
*  They're able to learn abstract properties of patterns and categorize them in more general
*  ways as well.
*  So, for example, they can learn the concept of orientation, the concept of orientation
*  in a rather general way.
*  So you can train them to distinguish between, let's say, horizontal and vertical random
*  gratings.
*  And when I say random, I mean from time to time, every visit, the grating has a different
*  pattern of black and white stripes.
*  It's not the same regular stripe.
*  So they learn to do that.
*  And then you can try and test them on other patterns, other oriented patterns, for example,
*  sinusoidal gratings or even single stripes, you know, which possess the same orientation
*  combination.
*  One is vertical, the other is horizontal.
*  So if they were rewarded on the horizontal random grating, they will pick the horizontal
*  stripe or the horizontal sinusoidal grating or the horizontal row of dots as opposed to
*  the vertical.
*  But they can generalize this concept of orientation and learn it in a fairly general way and apply
*  it to other objects they haven't even seen before, right?
*  That's something.
*  There's also one of our studies showed that bees also possess things that you would call
*  top-down processing.
*  So for example, you've probably seen this famous picture of a Dalmatian against a spotted
*  black and white background.
*  And it's camouflaged, right, because you cannot pick out the silhouette very easily.
*  But what happens is that if you're once you're given a cue and shown a solid black sort of
*  outline of the dog, then you never look at the same picture in the same way, right?
*  I mean, because once you've seen that prior information in your head pops out and sort
*  of goes down and picks out the signal from the noise because it knows what it's looking
*  for.
*  So, and it turns out that bees can also be trained to break camouflage in this way.
*  So, the way we went was that we did was to show them camouflaged patterns.
*  So one, for example, could be a textured ring presented against a textured background, a
*  randomly textured background.
*  The both the ring and the background are textured, randomly textured.
*  And the other case, on the other side of this Y maze, you have a disc, a randomly textured
*  disc presented against a randomly textured background.
*  There's some distance between the foreground target and the background wall.
*  So I'll tell you why.
*  But initially, when you try to make them distinguish between these two things, they can't learn
*  it.
*  They can't learn it at all because both patterns appear camouflaged.
*  But then if you train them on un-camouflaged versions of the same objects, one is a solid
*  black ring and the other is a solid black disc presented against a textured background,
*  they can see these discs very easily.
*  And they will learn, for example, that the ring is the one to go for to get the food.
*  Then you present these bees with the camouflaged objects.
*  And then immediately, once these bees have been pre-trained, they will pick the camouflaged
*  object right away, the camouflaged ring, without even needing to be further trained on it.
*  So they've learned the trick of breaking the camouflage and they're now using it.
*  And not only that, you can now train them on totally novel camouflaged objects.
*  And again, they will learn to do that without needing to be pre-trained because they've
*  learned how to break the camouflage.
*  And the way to break the camouflage is to actually, when you're coming towards the
*  object, you move a little from side to side.
*  And then because the object is slightly closer to you than the background, you get this motion
*  parallax between the object and the background.
*  And that makes the object pop out and reveal itself.
*  And so they've learned to use this math motion camouflage to take advantage of or exploit
*  it.
*  So you can train a bee to look at the world in new ways, which you haven't done before,
*  right?
*  Normally, they probably wouldn't need to do it.
*  Well, right.
*  That's one of my questions was, so that speaks to maybe to the capacity of what they're capable
*  of, but maybe they wouldn't necessarily ever use that in their own ecological.
*  Yeah, that's a funny thing.
*  You see, lots of these things.
*  That's what amazes me so much because even though it's not part of their natural requirement
*  or the natural history, they can learn these things.
*  They're a bit like a lab rat in the sense that you can make lab rats do things that
*  you normally...
*  Yeah, you're trying to test specific...
*  They're like that.
*  And that's what's really cool about them.
*  And this is done by a very small brain with a smaller number of neurons.
*  And yeah.
*  But still, I mean, one aspect is just that it's impressive that brains have such high
*  capacity, neural systems have such high capacity.
*  But is it just a matter of pattern matching or is there some symbolic cognition going
*  on there?
*  I think it's symbolic because all of these things, for example, the simple task of orientation,
*  for example, it's not just simply a photographic pattern matching, right?
*  Because it really wouldn't work if it was that.
*  It'd have to be some generalization.
*  Isn't it?
*  Again, when you train them to fly through mazes, for example, they can learn to...
*  A simple way to guide them through a maze is to make them follow a symbol that's tacked
*  on each one of the chambers through the maze and just learn to follow the symbol.
*  But you can do it in a slightly more abstract way by using the symbol as a guidepost.
*  You can say, okay, if this wall is yellow in color, it means you've got to turn left.
*  If it is blue in color, you've got to turn right.
*  So they're using these things in a...
*  Not as guideposts, but actually...
*  Well, it's sort of a guidepost, but much more abstract.
*  It's a symbolic kind of guidepost, right?
*  It's at least toward abstract symbolism.
*  Yeah.
*  I don't know how much we actually use symbols either.
*  So there's that question as well.
*  Yeah.
*  Yeah.
*  I'm not saying bees are superhuman.
*  Please don't get me wrong.
*  But it's amazing what they can do.
*  Okay.
*  That was just a reality check there.
*  I was just testing you.
*  But you have come to appreciate bee cognition a lot more and respect the bee as an organism
*  probably through your studies.
*  Yeah, for sure.
*  For sure.
*  I mean, when you grow up as a kid, all you're trained to do is to avoid bees because they'll
*  sting you, right?
*  I mean, but really, it's amazing.
*  A bee doesn't really sound aggressive in any way.
*  The only time it stings you is when it perceives a threat because it dies when it stings you,
*  right?
*  It bleeds to death.
*  So it's not in its interest to sting you anyway.
*  My daughter wanted me to ask you about bees stinging, but I'm going to refrain.
*  Oh, yeah.
*  Especially when they're foraging, they're in a beautifully peaceful state of mind.
*  All they want to do is to come there, get their food and go away.
*  In fact, when they're feeding at your feeder, you can even reach over and stroke their backs
*  with your finger and they won't even notice.
*  They're just blissfully drinking their sugar water.
*  It's only when they perceive a threat to the hive or something that they get aggressive
*  and come and defend the hive.
*  And that's the only time when they sting.
*  But what I've learned from you is if I accidentally threaten a hive and I anger a few bees, what
*  I should do is take my fingers and move them really fast so that they kind of go further
*  away, right?
*  That's funny.
*  That's one thing.
*  But they've also said that they get attracted by movement.
*  That's for sure.
*  We also looked at experiments.
*  We haven't published them, but they do get attracted to moving objects.
*  So one of the lessons that beekeepers tell you is to not move, to freeze.
*  When you perceive a bee about to attack you, you can actually hear the wing beat increases
*  in frequency.
*  So you can hear the raised pitch that's coming to get at you.
*  But it's instinctively very difficult to freeze at that time.
*  You really want to get the hell out of there.
*  And so it's a very hard thing to do to just wait there and hope it'll go away.
*  But if it does get into your hair or something, they say the best way to get rid of that problem
*  is not to really rub your hair like this and try to get it out because that gets them even
*  more nervous and they will definitely sting your scalp.
*  The best way to deal with that situation is basically whack your head and kill the poor
*  bee.
*  But that's the best way to do it because it's going to die anyway.
*  Even if it stings you, it's going to die.
*  Right.
*  Right.
*  Okay.
*  Well, I'll pass that on to my daughter.
*  Thank you.
*  Oh, the other thing you should pass on to your daughter is that she can do all these
*  experiments in her own backyard.
*  She doesn't even need to have a beehive.
*  Right.
*  That's cool.
*  She can just place sugar water feeder in the backyard and I can show you some feeder water
*  designs if you want to set them up.
*  And she can do all that.
*  Somebody, a neighbor could have a beehive and she could just mark some of these bees
*  and send some information how to mark them carefully and so on.
*  And she can have a lot of fun training them to learn colors and this and that totally
*  in the backyard.
*  Oh, that's awesome.
*  At no expense.
*  You gave me a month's worth of science lessons.
*  I'm in charge of the homeschooling, the science part.
*  I do dad science, quote unquote.
*  So this will be a really fun project.
*  This is great.
*  That'll be great.
*  Okay.
*  Do you think it's silly for neuroscientists to be studying higher level, higher level,
*  like bigger brain animals like monkeys, et cetera, when there's still so much to learn
*  from such small, you could say more tractable systems?
*  I think it should go in parallel.
*  I think it should go in parallel.
*  I mean, the sad thing now is that I think some of these smaller creatures, because of
*  funding constraints and so on, they're being pushed to one side and it's hard to find
*  funding, research funding for looking at these smaller creatures.
*  And sometimes you may discover things, as I say, some of the neural bases for some of
*  these cognitive things, because the bee brain is so small and it's just about a milligram
*  and it has only about a million neurons.
*  And you compare that to a human brain that has over a kilogram, I think, in weight and
*  what, 100 billion neurons, including the glial cells.
*  That's a lot of neurons.
*  Right around there.
*  And there's no neocortex in a bee either, right?
*  Yeah, for sure.
*  Yeah, so the thing is, if you happen to hit upon something when you're recording for
*  some of these neurons, it may give us insights about what's happening across a number of
*  species, right, without being distracted by all of the other things that higher creatures
*  have.
*  That's the thing, you see.
*  You have the bare bones kind of stripped down version of several cognitive sort of capacities
*  that are there in these simpler creatures, which you might be able to unearth if you're
*  lucky in some of these simpler creatures, I fear.
*  We started off this conversation, you talked about how bees are these great learning machines,
*  but a lot of their behaviors are innate, right?
*  They're essentially pre-wired to perform a lot of these behaviors.
*  And humans, of course, come in, we have a lot of innate structure and abilities, but
*  we are highly dependent on learning, you know, with the long gestation period and long childhoods
*  and all that.
*  Do you think that some of the innate abilities that are still, you know, some higher cognitive
*  abilities like numerosity and some of the symbolic capacities that bees have, do you
*  think any of that actually gets masked or, well, I guess I'll just say masked in brains
*  that learn and then, I don't remember the word you just said, but kind of things get
*  kind of messy or covered up or something like that in these...
*  Yeah, kind of obscured by other complicated things that are happening.
*  Yeah, I suppose.
*  Yeah, I mean, I'm not saying bees can do everything.
*  I mean, they can do certain things like count up to four and I saw a lot of work in Adrian
*  Dyer's lab more recently, which has shown that bees can even add and subtract in simple
*  ways.
*  And they've even developed a concept of zero.
*  You can train them to develop a concept of zero, nothing else, you know?
*  Yeah.
*  So all these things are there.
*  I'm not saying that they will drive humans by any means, but as you're right, the evolution
*  has pre-programmed a lot of the neural structure in them.
*  And so, for example, you can train a bee to learn colors in, I said, half an hour, right,
*  with very few training samples, five.
*  Whereas, I think, if I'm correct me if I'm wrong, but monkeys take a longer time to learn
*  simple tasks like this.
*  Oh my God, I don't want to talk about that.
*  Yes, it takes forever.
*  Yeah, because the explanation I've heard is that monkeys are saying, wait, this cannot
*  be that simple.
*  Right.
*  There's got to be something more complicated.
*  And so they're trying to figure out the really complicated solution or the reason for why
*  they're telling you why the experiment is trying to make them do this silly thing.
*  Yeah, you're raising my blood pressure right now, my memories here.
*  So, yeah.
*  Sreeni, I mentioned my daughter.
*  I haven't talked about my son yet.
*  My son, I recently had to have a conversation with him because I found out we have in Durango,
*  I live in Colorado in the United States.
*  And where we live, there's this infestation.
*  Everyone has them in their houses.
*  They're called elm bugs and they're kind of harmless, but they're just a nuisance.
*  And I found out one day my son was plucking the legs off of the elm bugs while they're
*  alive.
*  And so we had to have a conversation about how that's not cool, not an okay thing to
*  do to other organisms because they might feel pain and they might be suffering and how that
*  would be a problem.
*  What are your thoughts about pain, the perception of pain in insects and other like, quote
*  unquote, lower animals?
*  Yeah, yeah.
*  So it's a very interesting question that you bring up, Paul.
*  And it's a controversial question, a difficult one to, you know, do bees experience pain,
*  for example, or any other insects or invertebrates?
*  You know, if a dog yelps when it gets stung by a wasp or something, we are sure it's
*  felt pain, right?
*  Sure, right.
*  But if an insect flinches when you prod it with a pin, we conclude that this reaction
*  is simply a reflex because, hey, invertebrates cannot possibly feel pain, can they?
*  You know, for some reason, we seem to link an animal's ability to sense pain to its
*  perceived intelligence.
*  You know, and I always wonder why do we make this default assumption?
*  Why should the two be linked?
*  I mean, it seems to me that the experience of discomfort caused by a noxious stimulus
*  does not require any particular level of consciousness, I feel.
*  It doesn't require consciousness.
*  So wait, so sorry.
*  Exactly, exactly.
*  It doesn't require any high level, something unpleasant.
*  I mean, you could again say it's a reflex, right?
*  You could say, okay, people train flies to avoid the heat to heat chambers and go move
*  into cooler chambers, you know, so they're avoiding the heat.
*  And you could say, okay, that's simply a reflex.
*  But even if it's a reflex, it could be, there's nothing to say the creature does not feel
*  discomfort, right?
*  But doesn't that imply some subjective experience?
*  Discomfort is a subjective conscious.
*  It depends on how you define this comfort, right?
*  I mean, yeah, I have the feeling if I know that someone's going to inflict pain on me
*  and I can predict it, I can see that's a conscious, tends to be a conscious experience.
*  But you know, if something happens, I get stung by something without knowing what it
*  is, I still feel the pain, right?
*  And that's where I think, you know, we should be a little more careful.
*  I think our default assumption should be that all creatures feel pain and they're unless
*  proven otherwise.
*  It's my feeling, you know?
*  Yeah, well, I know.
*  I think that I don't know.
*  I don't know why when we're young, like my son, like it's not a you really have no no
*  empathy for other organisms, essentially.
*  And now I feel bad cutting a branch off of a tree or something.
*  Yeah, it tends to everything.
*  You're right. I mean, it could be plants are also sentient creatures, they say.
*  And where do you stop?
*  Right. I mean, that's always the problem.
*  I agree completely.
*  And by the way, with with fish, for example, for a long time, you know, there were no
*  guidelines for working with, you know, fish and other cold blooded vertebrates.
*  And totally, I think maybe a decade ago that there was a paper in Nature.
*  And typically it was a very if you think about it, it was a fairly simple,
*  almost simple, so simple minded.
*  I'm surprised that I think published in Nature.
*  But anyway, so they took a they took a bee and then made its sting a sting a fish in
*  the tail. And then the fish just twitched its tail.
*  And they finally oh, my God, this feels pain.
*  And it was published. And then, you know, from then on, it changed.
*  It's just a matter of when the world is ready to accept that thing, I think, because of
*  course, the the fishermen and the anglers were very upset by that.
*  Yes, of course, because they always like to believe that there's no pain.
*  But once once, you know, the world is ready to accept it, I think it gets accepted much
*  more quickly. In fact, what we were trying to do to try and see whether bees feel pain
*  or not was something I thought was far more sophisticated.
*  And it was wasn't our own idea. It was borrowed from someone in England who did
*  some work to investigate pain in chickens.
*  And what they did was they jabbed, wounded one of the legs of the chicken, a bunch of
*  chickens, and then the other control group was unwounded.
*  And then they gave both these groups of chickens a choice between two feeders.
*  One was a normal, the normal food, and the other one was the same food pellets laced
*  with some painkiller like ibuprofen.
*  You know, and then it turned out it was only the wounded chicks.
*  Only they showed a preference for the food that had the painkiller.
*  All right. And it wasn't like the painkiller tasted good and they preferred it that way
*  because the unwounded things did not show a preference.
*  They were going randomly to both of them 50-50.
*  So this is more than just a simple reflexive reaction to a jab or something.
*  It's really something that says, hey, look, I find that this thing makes me feel more
*  comfortable. It relieves my discomfort, right, when I eat this and I'm going to eat this.
*  So it's a much more subtle way of investigating it.
*  And this is what we tried to do with bees.
*  But unfortunately, the results were there.
*  Slight difference. We used a painkiller which is morphine.
*  We didn't know what to use.
*  That's one thing. We tried to use several things.
*  But the wounded bees showed a slight preference of the morphine, but it wasn't
*  statistically significant enough as to make a claim about it.
*  So we published a paper saying we really don't know.
*  There's no statistical differences.
*  But here it is. And that's all we can say for the moment.
*  It's possible that we either had the wrong anesthetic.
*  We really don't know what works well for bees.
*  We still don't know. We had to try several things.
*  So it's still an open question, I feel.
*  You know, yeah, what can I say?
*  Just more work is needed.
*  I think just a few more work is needed.
*  I don't think it's there. It's just the beginning of a long story, I feel.
*  That wasn't a nature paper.
*  You have to have a bee sting of fish to have a nature paper.
*  If you think about it, that was so simple, Mario.
*  I know. That's great. It's great.
*  But yeah, like when you were talking about fish, I mean, I remember I grew up,
*  you know, being taught, oh, you know, I would go out fishing with my grandparents.
*  Well, fish don't feel pain.
*  And my grandfather would clean them alive, you know,
*  would just fillet them alive.
*  And that's fine. They don't feel pain.
*  But on the other hand, and we just mentioned, you know, the chickens and bees
*  and different examples.
*  On the other hand, there is, like you said, it's a tricky question
*  because the experience that they are experiencing, the subjective experience,
*  there are likely different gradients of consciousness and.
*  Uncomfortableness.
*  And what is your conception of bee consciousness?
*  If you if you had to guess, is there a rich consciousness there
*  or is there a little flicker of consciousness or what?
*  I don't think it's as rich as humans, but, you know, let me give you
*  just one example of some lovely work that a chap by the name of James Nee did.
*  And he found that have you heard of headbutting bees,
*  headbutting other bees while they're dancing?
*  So what he found was that it's very interesting.
*  So he found this is about, wow, this is almost about 10 years ago.
*  He found this that it would be noticed that another bee is dancing
*  to signal a particular food source that this particular bee has been to
*  and encountered some danger, for example, in the form of a lurking spider
*  that kind of attacked it and wounded it.
*  Then this bee, observing bee, will headbutt this dancing bee
*  and stop it from advertising that particular food source.
*  And only a bee that advertising that particular food source
*  will be headbutted and prevented from dancing.
*  I mean, to say all of this is just a pure instinctive reflex
*  seems really a bit difficult to believe, right?
*  And also the probability of headbutting increases with the severity of the injury
*  that this bee has experienced after coming back.
*  So if it thinks it's really dangerous, it's more likely to do the headbutt.
*  So he did some controlled, you know, lovely study,
*  where he controlled the sort of pinches of the legs of these bees
*  and released them back home and then looked to see how they behaved
*  in terms of the headbutting.
*  And there was a nice relationship between the two,
*  the severity of the injury and the tendency to headbutt.
*  I mean, if all this can happen, it's hard to believe all this is just a simple
*  pre-programmed reflex, and it's just that particular food source.
*  If it's signaling that particular distance and direction
*  that signals that particular food source, says, hey, it has the same order as well.
*  It says, hey, don't do that because you're putting the whole colony in danger.
*  Yeah.
*  Often, I have guests who are using deep learning networks
*  as models of brain activity and brain function.
*  And I know we haven't talked about deep learning at all.
*  And you don't use deep learning in your navigation systems, right?
*  Have you dabbled in that?
*  No, no, no, no, no, not yet anyway.
*  No, no, no.
*  Any interest?
*  Do deep nets feel pain?
*  And are they conscious?
*  Just kidding.
*  But, you know.
*  If they replicate, that's the thing, isn't it?
*  It's a philosophical question, isn't it?
*  If they replicate all the behavior that, you know,
*  a living creature would exhibit if it was subject to some noxious stimulus,
*  then I suppose you could say they feel pain.
*  I mean, that's the thing, you see, how can you, yeah.
*  I don't know, it's hard to decide one way or the other, isn't it?
*  It really is.
*  Yeah.
*  But I'm not an expert in deep learning,
*  but I can't help wondering whether, you know,
*  learning in bees and other simple creatures involves,
*  at least in some processes that might be simpler and faster.
*  It's true that, as you said, a lot of what a bee has learned or can learn
*  is partly due to evolution, which is sort of fine-tuned
*  and honed these neural circuits.
*  That's kind of a deep learning process.
*  It's gone through, you know, several thousands of years of evolution.
*  But still, you know, as we said, a bee can learn things very quickly,
*  what it needs to learn, and even some things that it doesn't need to learn,
*  novel things, very quickly.
*  It doesn't need millions of training samples, right?
*  I mean, unlike most, you know, deep convolutional networks,
*  all those are learned with two or three rewards,
*  colors in half an hour, patterns in half a day, navigational routes,
*  you know, one or two flights, and the bees learn the route,
*  you know, for its entire life, and they can learn new routes very quickly.
*  All this is happening very rapidly.
*  Bees, people have shown that bees can recognize human faces.
*  Adrian Dyer's work, one of my colleagues,
*  showed that bees can be trained to distinguish between paintings by Monet
*  and paintings by Picasso.
*  Again, probably not part of their ecological needs.
*  Yeah, that's the thing, you see, it's all novel things.
*  And some of the largest guys shown that bees can be trained to play golf.
*  This is manipulating a ball into a hole,
*  and if they get the ball into the hole, they get a reward.
*  All these things are happening, and they're learning it very quickly, you see?
*  I mean, but deep learning is, that's one of the obvious,
*  one of the first things people talk about of its shortcomings
*  is that it just takes so long to learn, and humans as well
*  have one-shot and few-shot learning.
*  But also a lot of what you talked about just in the optic flow,
*  like, is it basically a simple control system, right?
*  Which is like more of a cybernetics engineering standard kind of control system,
*  but those aren't necessarily learned, I suppose.
*  They're probably sort of hardwired, I would say, yeah.
*  Some of the basic control systems, flight control mechanisms and so on,
*  are probably hardwired.
*  Even the bee dance, from what I understand,
*  it's only, the basic ingredients are there.
*  Basically, like the gate is programmed into human infant,
*  it's probably part of the pre-programming thing, just walking, you know, the gate.
*  But it's fine-tuned after birth.
*  But the fine-tuning happens very quickly, I think.
*  Don't get me wrong, I'm totally in awe of the performance of machine learning algorithms.
*  And they're very important, right?
*  Everyone has to say this first when they're about to criticize it
*  or say something slightly...
*  Believe me, it's very impressive, but...
*  So, okay, now go ahead.
*  Yeah, standard.
*  Well, the thing is, yeah, the one thing I find a bit unsatisfying
*  about the learning we've seen, of course, deep learning,
*  is that while they work beautifully at the task that they're supposed to accomplish,
*  we do not, it seems to me, and again, I'm ignorant,
*  I really don't know the subject, so maybe I shouldn't be talking about this,
*  you know, with any authority,
*  but we don't seem to have a good idea of why they work so well.
*  Right.
*  For example, what is the nature of the computation that's being performed?
*  What are the kinds of information that are being extracted
*  by the neurons in the various layers?
*  We're still largely in the dark.
*  It's like a black box, you know?
*  You feed in millions of examples through a network and you turn a crank,
*  and out comes a beautiful result,
*  but the network is still largely a black box.
*  And I find this a little unsatisfying as a scientist
*  because I feel the goal is... the full goal is not achieved.
*  And I remember that in the late 80s, when neural networks first became popular,
*  their study was considered to be by many to be a non-science.
*  What did you think of them?
*  Do you remember what you thought of them back then
*  and compared to what you think of them now?
*  I always had this impression about, you know,
*  not being totally satisfying.
*  I've always had that.
*  I think I've come to appreciate it more as a utility, as a tool, you know?
*  I think, you know, self-driving cars and all this sort of thing, it's fantastic.
*  So it's great for engineering applications.
*  It's just great.
*  We still don't know how it works.
*  And that's the problem.
*  So in the old days, already in the old days,
*  I remember stories where people were saying,
*  you know, if you're a young faculty member
*  applying to work on neural networks,
*  they would say, don't do it because of the danger,
*  the possibility that you won't get tenure
*  because you don't consider it to be a science.
*  Right.
*  I don't know if you've come across that.
*  But so it's kind of a sledgehammer approach
*  where you blindly turn this crank without really understanding what it's doing.
*  That's what I find is missing.
*  Maybe it'll come.
*  Or maybe I don't know.
*  Maybe it's already been understood and I don't know.
*  No, no.
*  I mean, there is a lot of deep learning theory.
*  But there is a lot in neuroscience, a lot of comparing the activities in some way,
*  whether you're looking at whole population activities
*  or sometimes even individual unit activity with networks in the brain
*  and finding matches between those.
*  I mean, the jury is still out on the explanatory power of that
*  and like how much that really buys us in terms of understanding.
*  But they're not black boxes in that sense.
*  Yeah, if you do find units in the artificial neural network
*  that look very much like shoulder responses,
*  they're very similar to what the cortical neurons are doing,
*  that's great.
*  That's fantastic.
*  That at least gives us an explanation of why this circuit is designed that way
*  and what it's doing, more importantly.
*  Right.
*  You said you called yourself kind of an armchair advisor at this point.
*  But do you see within the work that you have done over the years,
*  do you see when people are carrying on that work and advancing it,
*  are people excited about using the deep learning approach
*  or is it really more of a control system?
*  It is getting very excited.
*  I mean, some of the students I'm trying to help and advise now
*  are really getting onto it.
*  It seems to be the flavor of the month, right?
*  Everyone wants to use it and they want it.
*  And I'm not going to try and stop them.
*  I'm just going to say, hey, OK, in the end, it all makes sense to you.
*  Can you please open the black box and see what it's doing?
*  To me, it's not satisfactory.
*  It's just to say, OK, I've got this network that replicates
*  the trajectory of a bee that flies through a course of obstacles.
*  I would like to know a little more about how it's doing it
*  and why it's doing it.
*  Serena, your best guess, how long is that flavor of the month going to last?
*  Oh, you never know.
*  You never know.
*  It's kind of had a revival, isn't it?
*  It was there in the 80s for a while, 80s, early 90s, and then it disappeared.
*  And it came back again with a punch, probably because the increases
*  in computing capacity.
*  So now you can put in 1,000 layers and a quarter million neurons
*  in each layer and click the switch and off it goes.
*  But also, I don't know what the next step is.
*  If that goes out of fashion, what is the next step?
*  I don't know.
*  Is it back to basics?
*  Yeah, yeah.
*  Well, yeah, it's ever forward.
*  So I'll end on this question.
*  How long until we have a fully, whatever this means,
*  a fully satisfying account of the cognition from neurons to behavior,
*  from the nervous system to behavior?
*  Well, probably when we are able to, I would say,
*  record from each of the individual relevant neurons.
*  And I mean, some people are getting to it.
*  The genelia farms, as you probably know,
*  the Howard Hughes Institute, the genelia farms,
*  they've sort of got the kind of a blueprint for the,
*  the goal is to get the blueprint for the entire nervous system
*  of the fruit fly, for example.
*  Fruit fly.
*  I don't know if they're planning to record from each one of those.
*  The one thing about genetics, molecular genetics,
*  is that it allows you to dissect the system
*  and delete certain parts of the system
*  and get an idea of which circuits do what.
*  But how they do it again, I think, requires electrophysiology really,
*  to find out how each neuron responds,
*  to find out what computation is doing.
*  And that's what I think molecular biology doesn't help sometimes, I feel.
*  And there's a lot of interest and funding for molecular biology,
*  which is great, which is nice as a tool.
*  But I find the electrophysiology should also be,
*  really be funded more, more enthusiastically, I feel.
*  The behavior in electrophysiology, I think,
*  I really ultimately want to tell you what the insect really is doing.
*  For example, electrophysiology might tell you
*  that a neuron responds to something interesting,
*  but if the animal does not use it,
*  Right.
*  behaviorally, then again, that's that ultimate test of behavior, isn't it?
*  Yeah.
*  Srini, this has been a lot of fun for me.
*  I really appreciate the conversation.
*  And you've enlightened my world about bee cognition.
*  So I appreciate all the work in bees that you've done.
*  Thanks for being here.
*  Thank you so much, Paul.
*  It was really nice to talk with you.
*  Thank you again.
*  Brain Inspired is a production of me and you.
*  I don't do advertisements.
*  You can support the show through Patreon for a trifling amount
*  and get access to the full versions of all the episodes,
*  plus bonus episodes that focus more on the cultural side,
*  but still have science.
*  Go to braininspired.co and find the red Patreon button there.
*  To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year.
*  Find them at thenewyear.net.
*  Thank you for your support.
*  See you next time.

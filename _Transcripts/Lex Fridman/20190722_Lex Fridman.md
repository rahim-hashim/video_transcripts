---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 2688s
Video Keywords: []
Video Views: 33042
Video Rating: None
---

# Chris Urmson: Self-Driving Cars at Aurora, Google, CMU, and DARPA | Lex Fridman Podcast #28
**Lex Fridman:** [July 22, 2019](https://www.youtube.com/watch?v=Tj6NOfdfa4o)
*  The following is a conversation with Chris Urmson. He was the CTO of the Google self-driving car team,
*  a key engineer and leader behind the Carnegie Mellon University autonomous vehicle entries in
*  the DARPA Grand Challenges and the winner of the DARPA Urban Challenge. Today he's the CEO of Aurora
*  Innovation, an autonomous vehicle software company. He started with Sterling Anderson,
*  who was the former director of Tesla Autopilot, and Drew Bagnell, Uber's former autonomy and
*  perception lead. Chris is one of the top roboticists and autonomous vehicle experts in the world,
*  and a long-time voice of reason in a space that is shrouded in both mystery and hype.
*  He both acknowledges the incredible challenges involved in solving the problem of autonomous
*  driving and is working hard to solve it. This is the Artificial Intelligence Podcast. If you
*  enjoy it, subscribe on YouTube, give it five stars on iTunes, support it on Patreon,
*  or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N.
*  And now here's my conversation with Chris Urmson.
*  You were part of both the DARPA Grand Challenge and the DARPA Urban Challenge teams at CMU with
*  Red Whitaker. What technical or philosophical things have you learned from these races?
*  I think the high order bit was that it could be done. I think that was the thing that was
*  incredible about the first, the grand challenges that I remember, I was a grad student at Carnegie
*  Mellon, and there we, there's kind of this dichotomy of it seemed really hard, so that would be cool
*  and interesting. But at the time we were the only robotics institute around. And so,
*  if we went into it and fell on our faces, that would be embarrassing. So I think just having
*  the will to go do it, to try to do this thing that at the time was marked as darn near impossible,
*  and then after a couple of tries, be able to actually make it happen. I think that was
*  really exciting. But at which point did you believe it was possible? Did you, from the very beginning,
*  did you personally, because you're one of the lead engineer, you actually had to do a lot of the
*  work. Yeah, I was the technical director there, and did a lot of the work along with a bunch of
*  other really good people. Did I believe it could be done? Yeah, of course. Right? Like, why would
*  you go do something you thought was impossible, completely impossible? We thought it was going to
*  be hard. We didn't know how we're going to be able to do it. We didn't know if we'd be able to do it
*  the first time. It turns out we couldn't. That, yeah, I guess you have to. I think there's a
*  certain benefit to naiveté, right? That if you don't know how hard something really is, you try
*  different things, and it gives you an opportunity that others who are wiser maybe don't have.
*  What were the biggest pain points? Mechanical, sensors, hardware, software, algorithms for
*  mapping, localization, just general perception and control. Hardware, software, first of all.
*  I think that's the joy of this field, is that it's all hard, and that you have to be good at
*  each part of it. So for the first, for the urban challenges, if I look back at it from today,
*  it should be easy today. It was a static world. There weren't other actors moving through it,
*  is what that means. It was out in the desert, so you get really good GPS.
*  So that went, and we could map it roughly. And so in retrospect now, it's within the realm of
*  things we could do back then. Just actually getting the vehicle and there's a bunch of
*  engineering work to get the vehicle so that we could control it and drive it.
*  That's still a pain today, but it was even more so back then. And then the uncertainty of exactly
*  what they wanted us to do was part of the challenge as well.
*  Right. You didn't actually know the track, you knew approximately, but you didn't actually know
*  the route that's going to be taken. That's right. We didn't know the route.
*  We didn't even really, the way the rules had been described, you had to guess. So if you think back
*  to that challenge, the idea was that the government would give us, DARPA would give us a set of way
*  points and the width that you had to stay within between the line that went between each of those
*  way points. And so the most devious thing they could have done is set a kilometer wide corridor
*  across a field of scrub brush and rocks and said, go figure it out. Fortunately, it really,
*  it turned into basically driving along a set of trails, which is much more relevant to
*  the application they were looking for. But no, it was a hell of a thing back in the day.
*  So the legend, Red, was leading that effort in terms of just broadly speaking. So you're a leader
*  now. What have you learned from Red about leadership? I think there's a couple of things.
*  One is, go and try those really hard things. That's where there is an incredible opportunity.
*  I think the other big one though is to see people for who they can be, not who they are.
*  It's one of the things that I actually, one of the deepest lessons I learned from Red was that he would
*  look at undergraduates or graduate students and empower them to be leaders, to have responsibility,
*  to do great things that I think another person might look at them and think, oh, well, that's
*  just an undergraduate student. What could they know? And so I think that trust, but verify,
*  have confidence in what people can become, I think is a really powerful thing.
*  So through that, let's just fast forward through the history. Can you maybe talk through the
*  technical evolution of autonomous vehicle systems from the first two grand challenges to the urban
*  challenge to today? Are there major shifts in your mind or is it the same kind of technology just
*  made more robust? I think there's been some big steps. So for the grand challenge, the real
*  technology that unlocked that was HD mapping. Prior to that, a lot of the off-road robotics work
*  had been done without any real prior model of what the vehicle was going to encounter.
*  And so that innovation, the fact that we could get decimeter resolution
*  models was really a big deal. And that allowed us to kind of bound the complexity of the driving
*  problem the vehicle had and allowed it to operate at speed because we could assume things
*  about the environment that it was going to encounter. So that was the big step there.
*  So that was the big step there. For the urban challenge,
*  one of the big technological innovations there was the multi-beam LIDAR and being able to generate
*  high resolution, mid to long range 3D models of the world and use that for understanding the
*  world around the vehicle. And that was really kind of a game-changing technology.
*  In parallel with that, we saw a bunch of other technologies that had been kind of
*  converging after their day in the sun. So Bayesian estimation had been, SLAM had been a big field
*  in robotics. You would go to a conference a couple of years before that and
*  you know, every paper would effectively have SLAM somewhere in it. And so seeing that,
*  that Bayesian estimation techniques play out on a very visible stage, I thought that was
*  that was pretty exciting to see. And mostly SLAM was done based on LIDAR at that time.
*  Well, yeah. And in fact, we weren't really doing SLAM per se in real time because we had a model
*  ahead of time. We had a roadmap, but we were doing localization and we were using the LIDAR
*  or the cameras, depending on who exactly was doing it, to localize to a model of the world.
*  And I thought that was a big step from kind of naively trusting GPS science before that.
*  And again, lots of work had been going on in this field. Certainly this was not
*  doing anything particularly innovative in SLAM or in localization, but it was seeing that technology
*  necessary in a real application on a big stage, I thought was very cool.
*  So for the urban challenge, there was already maps constructed offline?
*  Yes.
*  In general. Okay. And did people do that individually? Did individual teams do it individually?
*  So they had their own different approaches there or did everybody kind of
*  share that information at least intuitively?
*  So DARPA gave all the teams a model of the world, a map. And then one of the things that we had to
*  figure out back then was, and it's still one of these things that trips people up today,
*  is actually the coordinate system. So you get a latitude longitude and to so many decent places,
*  you don't really care about kind of the ellipsoid of the earth that's being used.
*  But when you want to get to 10 centimeter or centimeter resolution, you care whether the
*  coordinate system is NADS 83 or WGS 84 or these are different ways to describe both the kind of
*  non-sphericalness of the earth, but also kind of the actually in, I think, I can't remember which
*  one, the tectonic shifts that are happening and how to transform the global datum as a function
*  of that. So getting a map and then actually matching it to reality to centimeter resolution,
*  that was kind of interesting and fun back then.
*  So how much work was the perception doing there? So how much were you relying on
*  localization based on maps without using perception to register to the maps? And I guess the question
*  is how advanced was perception at that point? Yeah, it's certainly behind where we are today.
*  We're more than a decade since the urban challenge, but the core of it was there
*  that we were tracking vehicles. We had to do that at 100 plus meter range because we had to merge
*  with other traffic. We were using Bayesian estimates for state of these vehicles.
*  We had to deal with a bunch of the problems that you think of today of predicting where that
*  vehicle is going to be a few seconds into the future. We had to deal with the fact that
*  there were multiple hypotheses for that because a vehicle at an intersection might be going right
*  or it might be going straight or it might be making a left turn. And we had to deal with
*  the challenge of the fact that our behavior was going to impact the behavior of that other
*  operator. And we had to deal with the challenge of the fact that our behavior was going to impact
*  the behavior of that other operator. We did a lot of that in relatively naive ways, but it kind of
*  worked. Still had to have some kind of solution. And so where does that 10 years later, where does
*  that take us today from that artificial city construction to real cities to the urban environment?
*  Yeah, I think the biggest thing is that the actors are truly unpredictable.
*  That most of the time, the drivers on the road, the other road users are out there
*  behaving well, but every once in a while they're not.
*  The variety of other vehicles is, you have all of them.
*  In terms of behavior, in terms of perception, or both.
*  Both. Back then, we didn't have to deal with cyclists. We didn't have to deal with pedestrians.
*  Didn't have to deal with traffic lights. The scale over which that you have to operate is now
*  is much larger than the air base that we were thinking about back then.
*  So what, easy question, what do you think is the hardest part about driving?
*  Easy question.
*  No, I'm joking. I'm sure nothing really jumps out at you as one thing, but in the jump from the urban
*  challenge to the real world, is there something that's a particular,
*  you foresee as very serious, difficult challenge?
*  I think the most fundamental difference is that we're doing it for real.
*  That in that environment, it was both a limited complexity environment because certain actors
*  weren't there because the roads were maintained. There were barriers keeping people separate from
*  robots at the time. It only had to work for 60 miles, which looking at it from 2006,
*  it had to work for 60 miles. Looking at it from now, we want things that will go and drive for
*  half a million miles. It's just a different game.
*  How important, you said LIDAR came into the game early on and it's really the primary
*  driver of autonomous vehicles today as a sensor. So how important is the role of
*  LIDAR in the sensor suite in the near term? I think it's essential. I also believe the
*  cameras are essential and I believe the radar is essential. I think that you really need to
*  use the composition of data from these different sensors if you want the thing to
*  really be robust. The question I want to ask, let's see if we can untangle it, is what are
*  your thoughts on the Elon Musk provocative statement that LIDAR is a crutch, that is a kind
*  of, I guess, growing pains and that much of the perception task can be done with cameras.
*  So I think it is undeniable that people walk around without lasers in their foreheads
*  and they can get into vehicles and drive them. And so there's an existence proof that you can
*  drive using passive vision. No doubt, can't argue with that. In terms of sensors.
*  In terms of sensors, right? There's an example that we all go do it, many of us, every day.
*  Okay. In terms of LIDAR being a crutch, sure. But in the same way that the combustion engine
*  was a crutch on the path to an electric vehicle, in the same way that any technology ultimately
*  gets replaced by some superior technology in the future. And really, the way that I look at this
*  is that the way we get around on the ground, the way that we use transportation is broken.
*  And that we have this, I think the number I saw this morning, 37,000 Americans killed
*  last year on our roads. And that's just not acceptable. And so any technology that we can
*  bring to bear that accelerates this self-driving technology coming to market and saving lives
*  is technology we should be using. And it feels just arbitrary to say, well, I'm not okay with
*  using lasers because that's whatever, but I am okay with using an eight megapixel camera
*  or a 16 megapixel camera. These are just bits of technology and we should be taking the best
*  technology from the tool bin that allows us to go and solve a problem.
*  The question I often talk to, well, obviously you do as well to the sort of automotive companies.
*  And if there's one word that comes up more often than anything, it's cost and trying to drive cost
*  down. So while it's true that it's a tragic number, the 37,000, the question is what, and I'm not the
*  one asking this question because I hate this question, but we want to find the cheapest
*  sensor suite that creates a safe vehicle. So in that uncomfortable trade-off, do you foresee
*  lidar coming down in cost in the future or do you see a day where level four autonomy is possible
*  without lidar? I see both of those, but it's really a matter of time. And I think really,
*  maybe I would talk to the question you asked about the cheapest sensor. I don't think that's
*  actually what you want. What you want is a sensor suite that is economically viable.
*  And then after that, everything is about margin and driving cost out of the system. What you also
*  want is a sensor suite that works. And so it's great to tell a story about how it'd be better
*  to have a self-driving system with a $50 sensor instead of a $500 sensor. But if the $500 sensor
*  makes it work and the $50 sensor doesn't work, who cares? So long as you can actually have an
*  economic opportunity, there's an economic opportunity there. And the economic opportunity is important
*  because that's how you actually have a sustainable business and that's how you can actually see this
*  come to scale and be out in the world. And so when I look at lidar, I see a technology that has no
*  underlying fundamental expense to it. It's going to be more expensive than an imager because
*  CMOS processes or FAP processes are dramatically more scalable than mechanical processes,
*  but we still should be able to drive cost down substantially on that side. And then I also do
*  think that with the right business model, you can absorb more, certainly more cost on the below
*  materials. Yeah, if the sensor suite works, extra value is provided, thereby you don't need to drive
*  cost down to zero. It's a basic economics. You've talked about your intuition that level two
*  autonomy is problematic because of the human factor of vigilance, decadent complacency,
*  overtrust and so on, just us being human. We over trust the system, we start doing even more so
*  partaking in the secondary activities like smartphones and so on. Have your views evolved
*  on this point in either direction? Can you speak to it? So, and I want to be really careful because
*  sometimes this gets twisted in a way that I certainly didn't intend. So, active safety
*  systems are a really important technology that we should be pursuing and integrating into vehicles.
*  And there's an opportunity in the near term to reduce accidents, reduce fatalities, and that's,
*  and we should be pushing on that. Level two systems are systems where
*  the vehicle is controlling two axes. So, braking and thrall slash steering.
*  And I think there are variants of level two systems that are supporting the driver
*  that absolutely we should encourage to be out there. Where I think there's a real challenge is in
*  the human factors part around this and the misconception from the public around the
*  capability set that that enables and the trust that they should have in it. And that is where
*  I am actually incrementally more concerned around level three systems and how exactly
*  a level two system is marketed and delivered and how much effort people have put into those human
*  factors. So, I still believe several things around this. One is people will over trust
*  the technology. We've seen over the last few weeks a spate of people sleeping in their Tesla.
*  I watched an episode last night of Trevor Noah talking about this and him, this is a smart guy
*  who has a lot of resources at his disposal describing a Tesla as a self-driving car.
*  And that why shouldn't people be sleeping in their Tesla? It's like, well, because it's not
*  a self-driving car and it is not intended to be. And these people will almost certainly die at some
*  point or hurt other people. And so, we need to really be thoughtful about how that technology
*  is described and brought to market. I also think that because of the economic challenges
*  we were just talking about, that that technology path will all these level two driver assistance
*  systems, that technology path will diverge from the technology path that we need to be on to
*  actually deliver truly self-driving vehicles, ones where you can get in and sleep and have the
*  equivalent or better safety than a human driver behind the wheel. Because again, the economics
*  are very different in those two worlds. And so, that leads to divergent technology.
*  LW So you just don't see the economics of gradually increasing from level two and
*  doing so quickly enough to where it doesn't cause safety critical safety concerns. You believe that
*  it needs to diverge at this point into different basically different routes.
*  CB And really that comes back to what are those L2 and L1 systems doing? And they are driver
*  assistance functions where the people that are marketing that responsibly are being very clear
*  and putting human factors in place such that the driver is actually responsible for the vehicle
*  and that the technology is there to support the driver. And the safety cases that are
*  built around those are dependent on that driver attention and attentiveness. And at that point,
*  you can kind of give up to some degree for economic reasons, you can give up on say false
*  negatives. And the way to think about this is for a foreclosure mitigation braking system,
*  if half the times the driver missed a vehicle in front of it, it hit the brakes and brought the
*  vehicle to a stop, that would be an incredible, incredible advance in safety on our roads. That
*  would be equivalent to seat belts. But it would mean that if that vehicle wasn't being monitored,
*  it would hit one out of two cars. And so, economically, that's a perfectly good
*  solution for a driver assistance system. What you should do at that point, if you can get it
*  to work 50% of the time, is drive the cost out of that so you can get it on as many vehicles as
*  possible. But driving the cost out of it doesn't drive up performance on the false negative case.
*  And so, you'll continue to not have a technology that could really be available for a self-driven
*  vehicle. So, clearly, the communication, and this probably applies to all four vehicles as well,
*  the marketing and the communication of what the technology is actually capable of, how hard it is,
*  how easy it is, all that kind of stuff is highly problematic. So, say everybody in the world was
*  perfectly communicated and were made to be completely aware of every single technology
*  out there, what it's able to do. What's your intuition? And now we're maybe getting into
*  philosophical ground. Is it possible to have a level two vehicle where we don't over-trust it?
*  I don't think so. If people truly understood the risks and internalized it, then sure, you could do
*  that safely. But that's a world that doesn't exist. If the facts are put in front of them,
*  they're going to then combine that with their experience. And let's say they're using an L2
*  system and they go up and down the 101 every day, and they do that for a month. And it just worked
*  every day for a month. That's pretty compelling. At that point, even if you know the statistics,
*  you're like, well, I don't know, maybe there's something a little funny about those. Maybe
*  they're driving in difficult places. I've seen it with my own eyes, it works. And the problem
*  is that that sample size that they have, so it's 30 miles up and down, so 60 miles times
*  30 days, so 60, 180, 1,800 miles. That's a drop in the bucket compared to the 85 million miles
*  between fatalities. And so they don't really have a true estimate based on their personal experience
*  of the real risks. But they're going to trust it anyway, because it's hard not to. It worked for a
*  month. What's going to change? So even if you start a perfect understanding of the system,
*  your own experience will make it drift. I mean, that's a big concern over a year, over two years,
*  even. It doesn't have to be months. And I think that as this technology moves from
*  what I would say is kind of the more technology savvy ownership group to the mass market,
*  you may be able to have some of those folks who are really familiar with technology,
*  they may be able to internalize it better. And your immunization against this false risk
*  assessment might last longer. But as folks who aren't as savvy about that read the material,
*  and they compare that to their personal experience, I think there it's going to
*  move more quickly. So your work, the program that you created at Google and now at Aurora,
*  is focused more on the second path of creating full autonomy. So it's such a fascinating,
*  I think it's one of the most interesting AI problems of the century. I just talked to a
*  lot of people, just regular people, I don't know, my mom, about autonomous vehicles. And
*  you begin to grapple with ideas of giving your life control over to a machine. It's
*  philosophically interesting, it's practically interesting. So let's talk about safety. How
*  do you think we demonstrate, you've spoken about metrics in the past, how do you think we
*  demonstrate to the world that an autonomous vehicle, an Aurora system is safe?
*  This is one where it's difficult because there isn't a sound bite answer. That we have to show
*  a combination of work that was done diligently and thoughtfully. And this is where something like a
*  functional safety process is part of that is like, here's the way we did the work.
*  That means that we were very thorough. So if you believe that what we said about this is the way
*  we did it, then you can have some confidence that we were thorough in the engineering work we put
*  into the system. And then on top of that, to demonstrate that we weren't just thorough,
*  we were actually good at what we did, there'll be a collection of evidence in terms of demonstrating
*  that the capabilities worked the way we thought they did. Statistically and to whatever degree,
*  we can demonstrate that both in some combination of simulations, some combination of unit testing
*  and decomposition testing, and then some part of it will be on road data. And I think the way we'll
*  ultimately convey this to the public is there'll be clearly some conversation with the public about
*  it, but we'll invoke the trusted nodes and that we'll spend more time being able to go into more
*  depth with folks like NHTSA and other federal and state regulatory bodies and given that they are
*  operating in the public interest and they're trusted, that if we can show enough work to them
*  that they're convinced, then I think we're in a pretty good place. That means you work with people
*  that are essentially experts at safety to try to discuss and show. Do you think, the answer is
*  probably no, but just in case, do you think there exists a metric? So currently people have been
*  using number of disengagements and it quickly turns into a marketing scheme to sort of you
*  alter the experiments you run to adjust. I think you've spoken that you don't like...
*  Don't love it. No, in fact, I was on the record telling DMV that I thought this was not a great
*  metric. Do you think it's possible to create a metric, a number that could demonstrate safety
*  outside of fatalities? So I do and I think that it won't be just one number. So as we are
*  internally grappling with this and at some point we'll be able to talk more publicly about it,
*  is how do we think about human performance in different tasks, say detecting traffic lights
*  or safely making a left turn across traffic? And what do we think the failure rates are for
*  those different capabilities for people? And then demonstrating to ourselves and then ultimately
*  folks in regulatory role and then ultimately the public that we have confidence that our system
*  will work better than that. And so these individual metrics will kind of tell a compelling story
*  ultimately. I do think at the end of the day, what we care about in terms of safety is
*  life saved and injuries reduced. And then ultimately, kind of casualty dollars
*  that people aren't having to pay to get their car fixed. And I do think that you can, in aviation,
*  they look at a kind of an event pyramid where a crash is at the top of that and that's the worst
*  event obviously. And then there's injuries and near miss events and whatnot and violation of
*  operating procedures. And you kind of build a statistical model of the relevance of the
*  low severity things, the high severity things. I think that's something we'll be able to look at as
*  well because an event per 85 million miles is statistically a difficult thing even at the scale
*  of the US to kind of compare directly. And that event, the fatality that's connected to
*  an autonomous vehicle is significantly, at least currently magnified in the world.
*  The amount of attention you get. So that speaks to public perception. I think the most popular
*  topic about autonomous vehicles in the public is the trolley problem formulation, right? Which has,
*  let's not get into that too much, but is misguided in many ways. But it speaks to the fact that
*  people are grappling with this idea of giving control over to a machine. So how do you win
*  the hearts and minds of the people that autonomy is something that could be a part of their lives?
*  I think you let them experience it. I think it's right. I think people should be skeptical.
*  I think people should ask questions. I think they should doubt because this is something new and
*  different. They haven't touched it yet and I think it's perfectly reasonable. And
*  at the same time, it's clear there's an opportunity to make the road safer. It's
*  clear that we can improve access to mobility. It's clear that we can reduce the cost of mobility.
*  And that once people try that and understand that it's safe and are able to use in their daily
*  lives, I think it's one of these things that will just be obvious. And I've seen this practically
*  in demonstrations that I've given where I've had people come in and they're very skeptical.
*  And they get in a vehicle. My favorite one is taking somebody out on the freeway
*  and we're on the 101 driving at 65 miles an hour. And after 10 minutes, they kind of turn and ask,
*  is that all it does? And it's a self-driving car. I'm not sure exactly what you thought it would do.
*  But it's a self-driving car. It's a self-driving car. It's a self-driving car.
*  It would do, right? But it becomes mundane, which is exactly what you want a technology like this
*  to be. When I turn the light switch on in here, I don't think about the complexity of those
*  electrons being pushed down a wire from wherever it was and being generated. It's like I just get
*  annoyed if it doesn't work. And what I value is the fact that I can do other things in this space.
*  See my colleagues. I can read stuff on a paper. I can not be afraid of the dark.
*  And I think that's what we want this technology to be like. It's in the background and people get
*  to have those life experiences and do so safely. So putting this technology in the hands of people
*  speaks to scale of deployment. So what do you think? The dreaded question about the future,
*  because nobody can predict the future, but just maybe speak poetically about when do you think
*  we'll see a large scale deployment of autonomous vehicles, 10,000, those kinds of numbers.
*  We'll see that within 10 years. I'm pretty confident.
*  What's an impressive scale? What moment? So you've done the DARPA challenge where there's one vehicle,
*  at which moment does it become, wow, this is serious scale.
*  So I think the moment it gets serious is when we really do have a driverless vehicle operating
*  on public roads and that we can do that kind of continuously.
*  Without a safety driver.
*  Without a safety driver in the vehicle. I think at that moment, we've kind of crossed the zero to one
*  threshold. And then it is about how do we continue to scale that? How do we
*  build the right business models? How do we build the right customer experience around it so that
*  it is actually a useful product out in the world? And I think that is really, at that point, it moves
*  from what is this kind of mixed science engineering project into engineering and commercialization and
*  really starting to deliver on the value that we all see here and actually making that real in the world.
*  What do you think that deployment looks like? Where do we first see the inkling of
*  no safety driver, one or two cars here and there? Is it on the highway? Is it in specific routes in
*  the urban environment? I think it's going to be urban, suburban type environments.
*  Yeah, with Aurora, when we thought about how to tackle this,
*  it was kind of en vogue to think about trucking as opposed to urban driving. And again, the human
*  intuition around this is that freeways are easier to drive on because everybody is kind of going in
*  the same direction and the lanes are a little wider, et cetera. And I think that that intuition
*  is pretty good, except we don't really care about most of the time. We care about all of the time.
*  And when you're driving on a freeway with a truck, say, at 70 miles an hour,
*  and you've got 70,000 pound load with you, that's just an incredible amount of kinetic energy.
*  And so when that goes wrong, it goes really wrong. And those challenges that you see occur more
*  rarely, so you don't get to learn as quickly. And they're incrementally more difficult than
*  urban driving, but they're not easier than urban driving. And so I think this happens in moderate
*  speed urban environments because if two vehicles crash at 25 miles per hour, it's not good,
*  but probably everybody walks away. And those events where there's the possibility for that
*  occurring happen frequently. So we get to learn more rapidly. We get to do that with lower risk
*  for everyone. And then we can deliver value to people that they need to get from one place to
*  another. And then once we've got that solved, then the freeway driving part of this just falls out,
*  but we're able to learn more safely, more quickly in the urban environment.
*  So 10 years and then scale 20, 30 years. I mean, who knows if a sufficiently compelling
*  experience is created, it could be faster and slower. Do you think there could be breakthroughs
*  and what kind of breakthroughs might there be that completely change that timeline? Again,
*  not only am I asking to predict the future, I'm asking you to predict breakthroughs that
*  haven't happened yet. So what's the, I think another way to ask that was, would be if I could
*  wave a magic wand, what part of the system would I make work today to accelerate it as quick as
*  possible, quickly as possible? Don't say infrastructure, please don't say infrastructure.
*  No, it's definitely not infrastructure. It's really that perception forecasting capability.
*  So if tomorrow you could give me a perfect model of what's happened, what is happening,
*  and what will happen for the next five seconds around a vehicle on the roadway,
*  that would accelerate things pretty dramatically. Are you, in terms of staying up at night,
*  are you mostly bothered by cars, pedestrians, or cyclists?
*  So I worry most about the vulnerable road users about the combination of cyclists and cars,
*  right? Or cyclists and pedestrians because they're not in armor. The cars, they're bigger,
*  they've got protection for the people, and so the ultimate risk is lower there.
*  Whereas a pedestrian or a cyclist, they're out on the road and they don't have any protection.
*  And so we need to pay extra attention to that.
*  Do you think about a very difficult technical challenge of the fact that pedestrians,
*  if you try to protect pedestrians by being careful and slow, they'll take advantage of that.
*  So the game theoretic dance, does that worry you from a technical perspective how we solve that?
*  Because as humans, the way we solve that is kind of nudge our way through the pedestrians,
*  which doesn't feel from a technical perspective as an appropriate algorithm.
*  But do you think about how we solve that problem?
*  Yeah, I think there's two different concepts there. So one is, am I worried that because these
*  vehicles are self-driving, people will kind of step on the road and take advantage of them? And
*  I've heard this and I don't really believe it because if I'm driving down the road and somebody
*  steps in front of me, I'm going to stop. Even if I'm annoyed, I'm not going to just drive through
*  a person stood on the road. And so I think today people can take advantage of this and you do see
*  some people do it. I guess there's an incremental risk because maybe they have lower confidence
*  that I'm going to see them than they might have for an automated vehicle. And so maybe that shifts
*  it a little bit, but I think people don't want to get hit by cars. And so I think that I'm not that
*  worried about people walking onto the one-on-one and creating chaos more than they would today.
*  Regarding kind of the nudging through a big stream of pedestrians leaving a concert or something,
*  I think that is further down the technology pipeline. I think that you're right, that's tricky.
*  I don't think it's necessarily, I think the algorithm people use for this is pretty simple.
*  It's kind of just move forward slowly and if somebody's really close, then stop.
*  And I think that that probably can be replicated pretty easily. And particularly given that you
*  don't do this at 30 miles an hour, you do it at one, that even in those situations the risk is
*  relatively minimal. But it's not something we're thinking about in any serious way.
*  And probably that's less an algorithm problem and more creating a human experience. So the
*  HCI people that create a visual display that you're pleasantly as a pedestrian nudged out of the way.
*  That's an experience problem, not an algorithm problem.
*  Who's the main competitor to Aurora today and how do you out-compete them in the long run?
*  So we really focus a lot on what we're doing here. I think that,
*  I've said this a few times, that this is a huge difficult problem and it's great that a bunch of
*  companies are tackling it because I think it's so important for society that somebody gets there.
*  So we don't spend a whole lot of time thinking tactically about who's out there
*  and how do we beat that person individually. What are we trying to do to go faster ultimately?
*  Well, part of it is the leisure team we have has got pretty tremendous experience.
*  And so we kind of understand the landscape and understand where the cul-de-sacs are to some
*  degree and we try and avoid those. I think there's a part of it, just this great team we've built.
*  People, this is a technology and a company that people believe in the mission of and so it allows
*  us to attract just awesome people to go work. We've got a culture I think that people appreciate
*  that allows them to focus, allows them to really spend time solving problems.
*  I think that keeps them energized. And then we've invested heavily in the infrastructure
*  and architectures that we think will ultimately accelerate us. So because of the folks we're able
*  to bring in early on, because of the great investors we have, we don't spend all of our
*  time doing demos and kind of leaping from one demo to the next. We've been given the freedom to
*  invest in infrastructure to do machine learning, infrastructure to pull data from our on-road
*  testing, infrastructure to use that to accelerate engineering. And I think that early investment
*  and continuing investment in those kind of tools will ultimately allow us to accelerate and do
*  something pretty incredible. Chris, beautifully put. It's a good place to end. Thank you so much
*  for talking today. Thank you very much. Really enjoyed it.
*  Thank you.

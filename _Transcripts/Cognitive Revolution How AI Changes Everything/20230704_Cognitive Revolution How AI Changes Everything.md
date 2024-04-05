---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 6007s
Video Keywords: []
Video Views: 692
Video Rating: None
---

# The Autonomy Revolution with Hayk Martiros of Skydio
**Cognitive Revolution "How AI Changes Everything":** [July 04, 2023](https://www.youtube.com/watch?v=aaLIxW3OMXo)
*  To have something like this that's an autonomous drone doing missions be used at scale for
*  this sort of large critical infrastructure inspection, it has to be about as reliable
*  as somebody installing a printer, copier, or buying a pickup truck or a washing machine.
*  It just has to do the job.
*  The drone can know where it is without GPS.
*  The drone can navigate and manage a bunch of complex planning objectives at a low level
*  to manage aerodynamics and camera motion and drone motion and high level tasks of different
*  kinds.
*  For a bunch of reasons, basically I'm against weaponized autonomous systems.
*  We will not weaponize our drones.
*  And for a bunch of reasons, like we're just, we're focused on the camera and the reconnaissance
*  as the core focus of our products there.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers, entrepreneurs,
*  and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today July 4th is Independence Day in the United States.
*  So while it wasn't exactly planned this way, it is I think somehow fitting that we share
*  this interview with Haik Martiros, Vice President of Autonomy at Skydio, the United States'
*  largest commercial drone maker.
*  There is a lot to say about drones.
*  This industry sits at the intersection of so many critical topics.
*  Automation and the future of work, the relationship between the technology industry and the government,
*  the war in Ukraine, the trend toward autonomous lethality, which to be clear Skydio has committed
*  not to produce.
*  The U.S.-China rivalry across all sectors, the prospect for far safer infrastructure
*  and life overall, but also the possibility and the threat of mass surveillance.
*  I attempted to cover just about all of this with Haik and found him to be a sophisticated
*  thinker across the board.
*  For starters, because it was a relative blind spot for me coming in and I suspect it is
*  also for many of you listening, I really dug in deep on the autonomy systems that Skydio
*  has developed over the last decade with traditional software.
*  Long story short, they have built an impressive vertically integrated stack that translates
*  the combination of 360-degree video inputs and also user instructions to specific detailed
*  flight paths, 3D spatial models and other visual reconnaissance, largely running everything
*  So that the drone, as they say, is easy to fly and hard to crash.
*  This approach, of course, also has opened up a 10 times bigger market for Skydio than
*  existed before because it no longer requires a skilled pilot to operate.
*  I was really fascinated by all of this, but we did eventually get around to what Haik
*  and team are working on now, which is the addition of a higher level, more semantic
*  AI layer that can now be placed on top of all the more optimized, explicit technology
*  that they've already built and deployed.
*  This layer promises to eliminate the need for operators pretty much entirely in many
*  contexts as customers will be able to give verbal and other high level direction to remote
*  systems.
*  They've actually recently introduced a dock that you can install really anywhere, say
*  on an oil rig or the middle of a dam somewhere in some remote place and still carry out detailed
*  inspections and other operations remotely.
*  This combination of existing hard technology and the new natural language or other high
*  level user experience strikes me as an extremely powerful one that we're likely to see play
*  out across lots of spaces.
*  And in fact, this is a big reason that I expect today's existing winners to be the ones that
*  benefit most from the AI technology wave.
*  No surprise then that Skydio, which has every branch of the US military as customers, just
*  raised another $230 million to expand its factories.
*  At the end of this conversation, we talked about how Skydio drones, which are just a
*  couple of pounds and really not capable of carrying more than a small additional weight
*  in which, again, Skydio has pledged not to weaponize, are nevertheless being used in
*  military contexts, including in the Russia-Ukraine war.
*  We also touched on the less followed conflict currently affecting Haik's home country of
*  Armenia and neighboring Azerbaijan as well.
*  It is a sad reality, especially considering the urgency of global problems such as avoiding
*  an AI arms race, that there's still so much conflict in the world.
*  But in the context of the Russia-Ukraine war and ongoing US-China decoupling, it is hard
*  to deny that the United States and the West more broadly need champion companies to lead
*  critical industries.
*  To my eye, Skydio looks to be extremely well positioned to play that role in the vertical
*  of autonomous inspection and reconnaissance drones.
*  All this brings me to a couple thoughts about the United States in the context of the cognitive
*  revolution.
*  It's commonly said that the United States' greatest advantage is its ability to attract
*  talented immigrants from around the world and to reinvent itself on an ongoing basis.
*  And boy has that been evident across our guests to date.
*  I've always just followed my interest in specific research and projects and products to identify
*  guests to invite for the show, and I've never really worried about the resulting demographic
*  mix.
*  But looking back, it is incredible how many of our guests grew up somewhere else around
*  the world and are now living and working in the United States, particularly the entrepreneurs
*  and the researchers.
*  Amjad of Replit from Jordan, Eugenia of Replica from Russia, Anton from Chroma from really
*  all over the world, Flo from Lindy is from France, Mahmoud Felfel from PlayHT from Egypt,
*  Arvind Srinivas from Perplexity, Kirfana from Google Robotics, Shreyar Rajpal of Guardrails,
*  and Vivek Natarajan of Google Medpalm, all originally from India.
*  Andreas Stuhlmuller of AUT and Elicit from Germany, Ronen Elden and Yuanjue Li of Microsoft
*  Research from Israel and China respectively.
*  Last week's guests, Zhiming Liu from MIT and Lily Yu from MetaAI, both from China.
*  And finally today, Haik from Armenia.
*  That's nearly half of our episodes, all living and working in the United States today.
*  Personally, I hope that the United States can maintain its open posture and welcoming
*  culture and extend this advantage going forward, both because I just like to see people have
*  the opportunity to chase their American dreams and because I think the world really does
*  need a deeply connected, multicultural, intellectual hub.
*  And right now, the United States is the best candidate that we've got.
*  At the same time, I also feel like we should broaden the reach of the show by connecting
*  with more guests working in AI outside of the United States.
*  So if you have any suggestions for entrepreneurs or researchers working on AI internationally
*  that you believe would make great guests for the cognitive revolution, please do let us know.
*  You can email us at tcr at turpentine.co or send me a direct message on Twitter where
*  I am at Levenz.
*  Without any further ado, I hope you enjoy this July 4th conversation with Haik Martiros,
*  VP of Autonomy at Skydio.
*  Haik Martiros, welcome to the cognitive revolution.
*  Thanks, Nathan.
*  Yeah, I've been checking out some of the other episodes and I'm a fan.
*  Thank you very much.
*  That's kind.
*  Well, I've also been checking out a lot of the work that you've been doing over the past
*  better part of a decade and really excited to have this conversation and dive into everything
*  that goes into making an autonomous drone like the ones that you are building at Skydio.
*  So maybe just for a little bit of background, tell us a little bit about yourself.
*  And you're clearly a multi-talented individual.
*  It's sort of an odd facet of the AI moment right now that you've had this project in
*  process for a decade and built a multi-billion dollar unicorn business.
*  And I would bet that most of our listeners, if they know anything you've done, would know
*  your Refusion project from not too long ago where you created a variation of stable diffusion
*  that would create spectrograms that could then be turned into music.
*  So that's not going to be our focus today, but that was cool.
*  And it's also kind of a window, I think, into who you are as somebody who clearly has their
*  hands in a lot of different areas of technology.
*  Yeah, cheers.
*  I'll try not to pivot to talking about that for the whole hour.
*  So about my background, I mean, I think it's kind of an odd one.
*  I was born in Armenia just after the collapse of the Soviet Union.
*  And then when I was seven years old, my family moved to Alaska, kind of a middle of nowhere
*  in Fairbanks, Alaska.
*  I was with my dad and got a chance to study earthquakes there.
*  He's a seismologist.
*  And then I grew up there for about 10 or 11 years, moved to New Jersey, ended up going
*  to Princeton for my undergraduate and kind of started out very much as a mechanical engineer
*  there.
*  I considered being kind of a music major or architecture, but quickly got into just working
*  on software.
*  I took, I kind of became the robot software guy and was really interested in that and
*  came out to Stanford for the Masters after that.
*  And as I was leaving that, just thinking about what I wanted to do, kind of definitely in
*  robotics and I was, you know, the like most Stanford students' thoughts, I was some kind
*  of embodiment of Elon Musk and Steve Jobs.
*  I was thinking about, you know, should I start a company?
*  What should I join?
*  And at that time, Google X had acquired basically every interesting robotics startup around
*  2015.
*  And I was kind of looking around, trying to get into that, think about what to do.
*  And I managed to meet Adam, the CEO of Skydio.
*  And I got I didn't know anything about Skydio.
*  I thought it was already a big company.
*  I found him on AngelList and he started asking me some math questions on Skype and I was
*  pretty into it.
*  So then I went to meet them at their office.
*  But the office turned out to just be a house in Atherton and where the three of them were
*  working out of, the three founders.
*  And it was pretty incredible.
*  Like they had started the Google Wing project, the Google X, with their advisor from MIT.
*  And then they left after about a year because they were just tired of feeling like it was
*  a side project of a company that was focused on online ads and search and wanted to be
*  a core thing.
*  Like if you're building robots, it has to be a core thing.
*  It's really hard.
*  And so I was pretty inspired by that and excited to take a risk.
*  And I've been there for just over eight years now, basically my whole career outside of
*  school.
*  And so you guys have built a lot coming out of that house in the last eight years.
*  I don't know to what degree people will be familiar with Skydio and the product.
*  So I thought, you know, for starters, we could just kind of take a quick rundown of like
*  what it is. I, you know, after marching my way through all of the marketing materials
*  and demo videos on the website and all that stuff, kind of came away with the takeaway
*  that it's like the most advanced eyes in the sky that are out there today in the sense
*  that it's super easy to fly.
*  Anyone can fly is one of your big value props.
*  And then it's really just like all eyes.
*  You know, it's a light, seemingly pretty agile device that has six 4K cameras on it.
*  So, again, really emphasizing like the collection of visual data, seemingly a lot of on-board
*  processing to make use of all that.
*  And then, you know, pretty I think there's really interesting tradeoffs that I'm interested
*  to hear more about around like how big to make it and the power that you can bring and
*  how the power itself, you know, weighs you down.
*  So if I if I read the latest spec, right, it's a half hour, essentially flight time
*  and a six kilometer radius that just goes and looks at stuff.
*  So tell me what would you, you know, how would you complicate my kind of takeaway or
*  synthesis? That was my GPT 3.5 level summary of the website.
*  Come on, at least 3.7.
*  It's pretty good. Yeah, I think I think that was good.
*  I mean, essentially, Skydio is a drone company and an AI company and we're kind of both
*  horizontal and vertical.
*  So the way we started out was really around just the the autonomy software part.
*  We were like, OK, we can make autonomy software so that robots can be intelligent and
*  trustworthy and navigate the world.
*  We realized pretty soon after that, that to really make an autonomous agent that works
*  well to have a shot at that, you have to kind of control the whole stack of from the
*  mechanical design, the aerospace and the vibrations to the cameras, the drivers and the
*  chips involved and the software that runs it all.
*  And so then we became a hardware company.
*  And for the first several years of the company, we are a consumer hardware company, which
*  is a notoriously difficult and bad idea for a startup.
*  There aren't that many examples of successes there.
*  But we we essentially were focused on a drone that is intelligent enough to avoid
*  obstacles, not crash, navigate without GPS and capture cinematic kind of Hollywood
*  style footage of somebody that's skiing or mountain biking or doing some kind of action
*  sports. And that is something that a lot of people have thought about.
*  There's ideas, but the execution or realization of that is really difficult.
*  So that was kind of the journey.
*  And we have a lot of tens of thousands of customers that use that and are excited by
*  that. But now Skydio is a much broader company.
*  We're the biggest US drone maker.
*  And our focus is really around everything that is possible with autonomy to unlock more
*  intelligent drone behavior so that people that aren't trained experts can use the drone
*  so that people who don't know anything about flying robots can essentially just use the
*  data captured by the robots and all the workflows around that.
*  And so part of that path is the design of the hardware and aerospace components and
*  software and everything. And part of that is just like working into these product use
*  cases and really thinking and and in that nature.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it and I recommend you use it to use
*  Cogrev to get a 10 percent discount.
*  So at this point, Skydio has a ton of business around inspection and mapping and
*  situational awareness for fire and police and defense and all types of kind of physical
*  infrastructure inspection.
*  So we do a lot and there's a lot of surface area.
*  So in some ways, it's kind of the horizontal play of this robot that captures.
*  Image data that can go anywhere and then in some ways, it's more like an end to end,
*  like solving real problems, making things a lot safer and cheaper than alternatives in
*  an industry use cases.
*  You know, I think that's that's where we're at right now.
*  And we're still I think Skydio is very much kind of a generational company where we
*  should be tens of billions of dollar company in maturity and still just a tiny fraction of
*  the use cases and the maturity of where we need to be.
*  And there's there's just a lot to to build.
*  And that's both kind of an opportunity and the core kind of challenge of the company, I
*  would say. It definitely seems like a market that's going to continue to grow for the
*  foreseeable future and probably pretty quickly, given all the kind of trends that are
*  converging to make this better, faster, easier, cheaper.
*  You know, it seems like, yeah, the sky's the limit.
*  No pun intended.
*  So as the business has evolved, you kind of mentioned the the main use cases, I would
*  guess that like the sort of commercial industrial inspection would be the biggest segment
*  because it just seems like there's an practically infinite amount of that out there.
*  And if I'm somebody that has a lot of cell phone towers to inspect or like oil rigs or
*  whatever, I'm like, you know what sounds a lot nicer than having somebody climb this
*  pole is like using this drone, right?
*  So that seems like if you can get the product to work well enough that it would be a
*  relatively easy sale and like a huge market.
*  Is that the is that the kind of core driver of the business today?
*  Yeah, I would say I would say that's the biggest part of the vision if I had to pick a
*  single part for sure, just that the world is just covered in infrastructure that makes
*  society run from electrical equipment to roads and highways and bridges and dams to
*  all sorts of buildings and indoor industrial facilities.
*  And just like every Fortune 500 company has a huge amount of these assets, every country
*  has a huge amount of these assets.
*  So I think practically infinite is a pretty good analogy for that.
*  Like I was just traveling through Armenia where I was born last week and noting just
*  how every corner of the country is still just covered in transmission towers just like
*  everywhere else on Earth.
*  So I think, yeah, absolutely, the small drones can do it way faster, way cheaper and way
*  safer. And that's a that's a huge part of the opportunity.
*  But also, these are some of the kind of most critical, important and slow moving kind of
*  industries. And so to to handle really getting into a market like that, like inspection of
*  utility equipment, it takes years and years to really get to the point where you're taking
*  you know, here's one of the here's probably what the cutest drone that we have is.
*  There's a couple of different ones that have different kind of hardware specs.
*  But to to have something like this, that's an autonomous drone doing missions be used at
*  scale for this sort of large critical infrastructure inspection.
*  It has to be about as reliable as somebody installing a printer, copier or buying a pickup
*  truck or a washing machine. Like it just has to do the job and be reliable.
*  And the entire set of things of being a trained drone pilot with a yellow vest and a hard
*  hat that's flying the thing has to go away.
*  And the entire craziness of this thing is navigating by itself and doing all this stuff.
*  Like we have to get past that and cross the chasm to the point where it's it is like the
*  standard tool. And that's something that takes a tremendous amount of engineering and product
*  and sales effort. And so I think that's kind of the path we're on.
*  And there's a whole other kind of half of the focus, which is around situational awareness
*  and security. And those use cases are there's a lot of overlap, but there's also a good
*  amount of differences on all fronts.
*  So that's great context. Let's talk about how you did it, because it does seem like you've
*  you have crossed that chasm and to a very significant degree, like these things are
*  deployed in the field doing the job.
*  Recent news item about the company was I believe it was a two hundred and thirty million
*  dollar raise to expand the factory.
*  And I'm sure there'll be some other uses of proceeds as well.
*  But it's always good when the factory becomes the bottleneck in a company.
*  So maybe just let's dive into the approach that you guys have taken to AI.
*  It's interesting. You've been doing this kind of in a very parallel world, I would say,
*  compared to like the LLM track that is currently getting the most attention.
*  But probably a lot of the same principles can apply for one that I always like to use is
*  like, what are the inputs and what are the outputs of this system?
*  You held up the drone a second ago and I was kind of thinking like, OK, if there's an
*  AI system that I could draw a box around here, it's probably starting off with the six
*  raw video streams that are coming in from the cameras.
*  And it's then ultimately outputting.
*  My best guess was for the kind of speeds for the blade at any given time.
*  And I realized I don't know if there's maybe more variables that it needs to predict or
*  control or if those are if the four rotors are kind of the only thing.
*  But just for starters, yeah, to help us understand kind of what the inputs are and
*  broadly speaking, how those are transformed into the outputs.
*  Yeah, for sure. So I think you said it pretty well.
*  So on on this particular drone, there's there's six of these navigation cameras.
*  Each of them has a 200 degree field of view.
*  So you kind of get the three that see the entire upper hemisphere altogether.
*  And then there's three on the bottom that see the bottom hemisphere altogether.
*  So the drone is kind of built.
*  Our first drone had 13 cameras, but it's the same concept is just to see in every
*  direction with multiple cameras at once.
*  And that's the core and primary input.
*  And the you know, there's other sensors like a GPU accelerometer, gyroscope,
*  things, things like that, that have important use cases.
*  The vast majority of information is from the cameras.
*  And, you know, when Skydio began, it was definitely, you know, it was pre deep
*  learning as something that was like really worked well in computer vision and
*  possible to run on the edge, especially.
*  And so there's a whole different story from from where we are today.
*  But there's also other sensor possibilities, like the most common one is LIDAR.
*  And you see this debate, you know, Ray John and the self-driving community.
*  But specifically for these small lightweight drones, the size and the cost
*  and the power usage is completely critical.
*  And cameras being on the train of cell phones with the scale in billions,
*  investment in tens or hundreds of billions are getting so small and so cheap
*  and so high quality that like that's really the path that we followed with our
*  drones and compute stack in general.
*  So that's the primary input and the output.
*  Yeah.
*  In this case, being a quadcopter has four rotor blades.
*  The most low level input we deal with is really at the level of the kind of
*  voltages that are commanded to the actually wound up kind of magnets along
*  the radius of each of the motors.
*  Right.
*  And that kind of thing happens at something like 30 kilohertz.
*  And so it's very, very low level when you get all the way down.
*  We do control that whole stack.
*  And that's one of the interesting questions.
*  It's like, it's a long way to traverse from very high level decisions that
*  happen at low on a few times a second or something to, to the most low level
*  thing that happens at many orders of magnitude faster.
*  And so that, yeah, that's kind of the, the overall system and the way that's
*  broken into, you know, approaches and components is, is important.
*  It's something that we've tried to be very, very thoughtful about.
*  Yeah.
*  So tell me maybe more about that.
*  I mean, the 30 kilohertz, does that mean you're actually making
*  updates to the voltage 30,000 times a second?
*  Yeah.
*  So the most, the most inner loop there is basically the current controller for the
*  motors and that's something like, you know, it's on a chip that has something
*  like 200 instructions to spare every one of those loops.
*  And so that's something that's very far from a large language
*  model or something like that.
*  Yep.
*  Again, as much as, as much as the entire stack can be like thought about and
*  designed together, the more chance you have of making a robust autonomous robot.
*  Yeah, it's interesting.
*  The end to end concept always comes up in AI in a lot of different contexts.
*  And this is kind of coming up in a bit of a different way because you're not
*  training an end to end system, but you are controlling all the components
*  and kind of designing them to work well together.
*  Could you maybe kind of just outline like how many layers of, I guess,
*  abstraction and kind of communication there are between, you know, those raw
*  inputs of the cameras plus the other sensors, you know, and then all the
*  way down to that lowest level.
*  And I'd also be really interested to know where, if anywhere, there are
*  true kind of black box models, you know, where something is, you know, kind of
*  the product of gradient descent in such a way where, you know, you haven't
*  specifically controlled, you know, all of the, you know, the translation from
*  the input to the output of that layer.
*  Using a metaphor from kind of like classical control theory, I would say
*  that every time you have an order of magnitude change in the rate at which
*  you need to do things, it often makes sense to kind of have a different system.
*  And the theory there says that like, let's say you're operating something at 10
*  Hertz, you're making a decision 10 times a second, but there's an inner loop
*  that's making a decision at a hundred times a second, then you probably don't
*  need the outer loop to care about the inner loop as much, the dynamics can be
*  kind of abstracted away.
*  So at that level, kind of, if you think about something at the lowest level
*  happening at tens of thousands of times per second, then the highest level is
*  maybe, you know, once a second, then you have something like four layers in the
*  loop there.
*  And I think that's a pretty close match to what a one sentence idea of the, you
*  know, how the Skydio system is built would look like.
*  And so in terms of the, there's a lot of advantages to kind of end to end
*  reasoning, because you get to just kind of jointly take the information, you get
*  to learn from it, from data, you don't have to figure out how to program these
*  things with complex multimodal inputs.
*  And there's obviously just tremendous advantages to that.
*  It is hard to cross those gaps of different orders of magnitude of frequencies
*  with that.
*  And I don't think it makes a ton of sense to do that on the drone.
*  There's something like 10 over 10 different deep networks that are running
*  for different purposes.
*  Probably one of the most interesting ones that's the core of among the things we've
*  put the most work into is the obstacle avoidance system.
*  So we were the first company to ship a deep learning based obstacle avoidance
*  system, and we published a paper on this in 2017 and shipped it on the Skydio 2
*  for the first time.
*  And that just had tremendous wins over the systems before that were more kind of
*  classically algorithms that we wrote.
*  And the capability there is to, you know, for things that are in camera images,
*  what's hard is that you don't see a lot of the easy stuff is easy.
*  You master that quickly.
*  But then the difficult cases, the signal is not there in the pixels as much.
*  And I'll give you an example, like, let's say you're in a facility that has a
*  white ceiling that's really textureless.
*  And you have a camera that's looking upward and it's basically all white.
*  You might also have a day that's just kind of a foggy day where the sky is all
*  that same color and you really need the context of all the surrounding cameras
*  and imagery to know that that is the sky and you can fly there versus that's a
*  ceiling and you're going to crash into it.
*  And so the same thing could be said for different types of sun glare, really
*  difficult thin branches with a backlit sun, all sorts of, you know, challenging
*  cases. And so deep learning is incredible at adapting to those use cases.
*  And I think where you draw the boundaries often also depends on what your inputs
*  are, not just how fast you're running it, but which cameras, which resolutions,
*  what type of pre-processing is important.
*  And I think more and more so at the high level of the stuff that can run at lower
*  frame rates and is reasoning, there's a huge opportunity for end to end reasoning,
*  particularly just what you might call embodied AI where the drone, you know, you
*  have models that understand camera imagery, understand some kind of high level
*  task, whether that came through an example or whether it came through an instruction
*  that's written with language and translate that into kind of the high level motion
*  of the drone.
*  Our core bet and layers that we build is basically like we, you know, we build
*  this hardware that has the cameras, it has the chips, it has the drivers and core
*  kind of embedded software to have a reliable platform that works, that flies,
*  that things don't go wrong.
*  And we have the sort of health monitoring management and state machines layers
*  that just kind of do the right thing.
*  And then we have the algorithms that make it so the drone doesn't crash.
*  The drone can know where it is without GPS.
*  The drone can navigate and manage a bunch of complex planning objectives at a low
*  level to manage aerodynamics and camera motion and drone motion and high level
*  tasks of different kinds.
*  So all of that on top is kind of the core autonomy navigation layer that can have
*  basically APIs to it.
*  And on top of that, building a system that is able to basically exhibit embodied AI
*  where you're able to understand, you know, image data coming in, video data, as
*  well as a high level instruction, like, you know, natural language or examples
*  demonstrated by a person and translate that to the high level commands of the
*  robot on top of that API is, is I think the hugely valuable robotics opportunity.
*  Doing that at the same time as controlling the voltages of the motors
*  doesn't make any sense.
*  Doing that at the same time as avoiding obstacles possibly makes sense, but not
*  necessarily.
*  And so I think that's a huge opportunity and we're going to see a huge amount of
*  this sort of embodied AI in the robotics world this year, as it kind of distills
*  down from what's really come from the computer vision and LP communities.
*  Yeah.
*  It makes a ton of sense.
*  So I'm kind of just working my way back up, up the layers as well.
*  So you've got the lowest level stuff of the 30,000 Hertz controllers of voltage
*  that ultimately translates into, you know, how fast should the blade spin and how,
*  you know, how much force is it going to generate?
*  Up a level from that, you've got kind of low level control systems that.
*  I guess I don't know exactly how high you jump there.
*  Like it seems like it's probably two levels up to go to something like hover,
*  you know, to just sort of maintain, you know, state.
*  I'm guessing there would be kind of another layer of abstraction between the
*  lowest level and something like, you know, just hold steady.
*  Is that true?
*  Well, what is it?
*  What is kind of in between there?
*  Yeah, for sure.
*  So the, the dynamics kind of flow up from, you know, the, the, to the currents of the
*  motors and then to the sort of desired rotation, kind of angular rates of the,
*  of the motors, which then flow up to kind of the desired angular rates and
*  acceleration of the drone body itself, as it relates from the models of the motors
*  to the body, which then roll up to the desired kind of orientation of the drone,
*  which then roll up to the desired position and velocity of the drone.
*  Because of course the quad rotor moves because all the rotors are mostly in
*  plane has to tilt to the side to then move sideways.
*  It can't just move sideways in, in a, in an effective way.
*  And so that then rolls up to, you know, the trajectory of a position of the drone.
*  So there's a, there's a few layers there.
*  And we do reason about a lot of those layers together.
*  But there's a, basically we have a quite a mature system now that we've, we've
*  built using this, this symbolic computation layer that, that we've, we've
*  developed and rely on a lot here.
*  But at the end of the day, it's an optimization, it's a nonlinear
*  optimization, and it's, it's not of the sort of gradient descent.
*  It's more of a second order optimization that's being solved.
*  That's, that's using basically a quadratic approximation of a lot of
*  different objectives and the dynamics of the drone to reason together.
*  And at this layer, we do something like 500 iterations per second.
*  And this is thinking about how to balance the rotor aerodynamics with the motion,
*  the orientation of the drone with things like not crashing the obstacles and the
*  high level desired commands of the user.
*  And those are things that really do make sense to reason together, because as
*  soon as you decouple them, you're going to have issues because the aerodynamics,
*  you might be having a big gust of wind at the same time as you're trying to fly
*  downhill that, and then rotating to avoid a thin power line and all those things
*  that are going to clash with each other, because you'll hit the power limits of
*  your propeller, which then prevent you from tilting, which then leads you to
*  crash into the wire.
*  And so that's the kind of system that, yeah, is in, is in that realm of like
*  tens to hundreds of times a second and is, is covering a lot of ground in the
*  core navigation of the drone.
*  So it sounds like there's essentially kind of a, almost like a, you know,
*  Russian doll kind of nested layers of basically the same setup that people have
*  been, you know, for listeners to the show, probably are most familiar with like the
*  LLM based agent, where you kind of have a loop and, you know, every time you go
*  through that loop, you get to kind of observe your state and maybe issue a
*  command, kind of the react, you know, paradigm for setting up an LLM agent.
*  That obviously works at this like very high, you know, level natural language,
*  but it's kind of that all the way down, right?
*  Is what I'm taking away from this.
*  There's a sensor that detects acceleration, for example, and it kind of
*  knows what it wants to be detecting.
*  And when it's deviating from that, it knows how to send a command down to a
*  lower level to adjust so as to hopefully, you know, bring it into detecting what it,
*  you know, should be detecting.
*  And that happens, you know, however many times and at the lower level, it
*  just spins even faster.
*  Yeah.
*  I think, I think there's definitely, there's a few levels of loops.
*  Each of those loops covers a lot of things and maybe has a few kind of tricky things
*  about it.
*  And one of the things is typically the states you care about are not directly
*  observed.
*  So there's kind of a coupled estimation problem where you're trying to figure out
*  the variables you really care about.
*  For example, what is the angular acceleration of the body of my drone or what is the
*  position of my drone or what is the location of the motor right now?
*  Like those are not things you directly measure with a sensor, but you're estimating
*  from other sensors.
*  And at the same time, you're giving commands.
*  And so that sort of joint estimation is a common part of it.
*  And then the second part of it is that you, you have to reason about a lot of the
*  uncertainties in play, because when you're trying to estimate unobserved quantities,
*  you have to carefully consider what your numerical kind of information or
*  covariances are between your variables and handle those, those layers.
*  And so this may be a good time to introduce your open source library,
*  SimForce, because I think this, if I understand correctly is like, this is the
*  framework that you have developed over a number of years to try to make this more
*  manageable, right?
*  The low level number crunching of this sounds extremely tough, especially when
*  you build in all those uncertainties and, you know, kind of having to deal with
*  distributions of possibilities, et cetera, et cetera.
*  SimForce allows you to, again, it kind of bridges a divide, right?
*  On the one hand, you have the human who is trying to figure out how to program the
*  device to deal with this sort of stuff and wants to do it in a more conceptual way, a
*  more maybe, you know, say semantic way.
*  But then that ultimately is going to translate to a lot of like low level
*  number crunching and that you have kind of no choice, but to really optimize in
*  order to get it to work on the device.
*  So this library sort of bridges that gap by presenting to the developer a relatively
*  high, comparatively high level interface to deal with, and then handles that
*  translation down to the super low level.
*  And if I understand correctly, no black boxes really in that system, right?
*  Like that's all something that's been truly like designed, architected, developed,
*  you know, as a kind of traditional software project, albeit one that ultimately kind
*  of adds up to AI.
*  Yeah, I think you're right on the dot.
*  So that SimForce is something that lives at the layer below what I would consider sort
*  of the embodied AI, you know, kind of layer where you're making these high level
*  decisions. It's more about the effective execution and numerical, you know, inner
*  loops here.
*  So SimForce is something that kind of arose out of problems that we've been dealing
*  with for many years and is definitely my kind of baby and passion project of
*  building this approach.
*  And so at the core, it's a library for symbolic computation, code generation and
*  nonlinear optimization.
*  So the principle is how it works is you as an engineer, as a roboticist, design
*  some kind of symbolic expression.
*  So you're writing.
*  It's kind of like writing a mathematical equation or models of things.
*  So we might say, here's how we think the map model of the propellers or aerodynamics
*  of the drone work, or it might be here's how my robot arm moves given commands.
*  And you build expressions for those in kind of a mathematical language.
*  You're not actually having numbers.
*  It's more like you're writing equations.
*  And then you can symbolically manipulate those.
*  Like you can do operations like simplification or taking derivatives or
*  factoring.
*  And you can do all this without worrying about the speed that this runs at.
*  And you can do it from a place of like analysis and understanding.
*  And then from that, basically something you write in Python, which is pretty
*  analogous to how you might write a PyTorch model specification for a deep network.
*  You're writing it in terms of the layers and operations and stuff.
*  But it's really meant for not sort of massively data parallel on every pixel of
*  an image, but more for doing numerical computations that are more with scalars.
*  And so once you have that symbolic expression, we can generate kind of
*  extremely fast runtime code that could be, for example, our core motion planner
*  ends up being a hundred thousand instructions with no branches in a single function.
*  And that's something that is a huge speed win for our drones and allows us to run
*  very sophisticated algorithms on the edge in a manner of tens of microseconds for a
*  complicated loop like that.
*  And so all of the high level ability to, as an engineer, develop, iterate quickly,
*  understand what you're writing, and then at the same time generate production ready
*  code that's automatically translated and tested.
*  And so in that way, the code that's output by the code generation is sort of a black
*  box in that you're not going to look at those hundred thousand lines and figure out
*  what's going on.
*  But if you trust the system, then you can understand the symbolic expression that
*  went into that.
*  And then we have a layer of optimization that you plug in those generated expressions
*  into kind of a sophisticated optimization library that is built to run very fast on
*  board the robots.
*  And that supports essentially a lot of the tasks we do from the sort of motion planning
*  and control side to the computer vision estimation, kind of like think like SLAM and
*  3D reconstruction tasks where you're trying to solve for a bunch of variables.
*  So, yeah, that's really interesting.
*  And the sort of emergence of a black box, even in the absence of gradient descent, is
*  definitely an interesting detail.
*  I'm a big fan of trying to get super concrete.
*  So if I sit down as an engineer to use this system, what is the sort of thing that I
*  might initially be writing an expression for?
*  And I understand that an expression is basically like it sounds like to do this, you
*  need to have kind of mastery of like several STEM fields at least like a college level.
*  Like I need to be really good at like classical mechanics.
*  I need to be good with like maybe linear algebra, differential equations.
*  I need to be, you know, obviously a competent programmer.
*  And then I can then I can sit down and say something like what I want to write.
*  I want to I want to develop a new is this a skill?
*  This is a lower level than a skill, though, still right.
*  You have the skills that are like follow me around.
*  And these would all be kind of thing.
*  Things we're talking about here are things that become available to the skill.
*  Yeah, the skills are kind of using the APIs of the core navigation system and the core
*  navigation system is getting the APIs translating to kind of weights of different
*  objectives. And those objectives are going into this lower level system that's optimizing
*  them all. Yeah.
*  You know, what's a starting ticket or like a definition where you're like, all right,
*  this is a new kind of below the level of the skill, but this is the sort of new
*  optimization problem that we want to solve.
*  All I'll give an example, a simple one.
*  So let's say that you want to control a little race car.
*  At the end of the day, you have kind of a gas pedal, a brake and a steering wheel.
*  So those are inputs that you get.
*  And then there's something that happens in the world.
*  The tires of the car are going to react to what you did.
*  And there's a relationship with the road surface.
*  So if you're going to build a model of that, you're somebody you kind of start with
*  the simulation of dynamics.
*  So how do the inputs translate to outputs?
*  And you basically need to build up a model of, OK, well, when the tires turn, it
*  moves on the ground and you might assume no slippage.
*  So the radius of the tires is part of the function of that.
*  And you make some assumptions and you say that as the tires spin, you're moving at
*  some speed. And if the tires are turned, it changes your direction in some way.
*  And you have to kind of write equations for those bits.
*  And you say when you hit the accelerator, here's how that relates to the actual
*  speed of the tires with some time constants.
*  And when you turn the steering wheel 10 degrees, here's what the tires do.
*  They might only turn five degrees or they might turn 20 degrees or it might be a
*  nonlinear function.
*  And so as a roboticist, you kind of design those equations to model what you have.
*  And so to actually make this sort of system work, like let's say you then want to
*  make a self-driving race car.
*  You have to do a lot more on top of that.
*  You have to solve some kind of problem on top that's doing stuff with those inputs.
*  And often you need the derivatives of those equations to control their dynamics like a
*  differential equation. And to effectively do this and run it on a robot efficiently,
*  you hit it right on the head. You have to both understand the theory of these
*  equations and you have to understand how to write really fast code and you have to
*  understand how to implement, you know, in C++ or a low level language, the
*  derivatives of these things.
*  And it's a lot of different skill sets.
*  And so by decoupling a few pieces of it, if you can just write the equations in
*  like a mathematical analytical sense without thinking about how do I take the
*  derivatives of it without thinking about how do I make it fast and then make that
*  part automatic, then it opens the door to any grad student that is, you know,
*  focused on the theory, but not the time to really make it productionized and free of
*  bugs. And there's just so much of the path of robots that is that just figuring out
*  where you screwed up.
*  And it's hard to maintain like a low level implementation of something that's supposed
*  to be fast and see the big picture of like, oh, man, I wanted the equation to be this
*  way and it would be better.
*  And so that's kind of the the relationship that that I see.
*  And of course, there's the question of, well, do you need to write those
*  theoretical equations or can you just learn them?
*  And I think the you know, my perspective on that is it kind of depends a lot.
*  Obviously, it's it's it's nuanced.
*  But I would say if you're sure that something is true, like, for example, gravity
*  is a pretty simple example.
*  F equals M.A. Yeah, you don't want to learn gravity.
*  And you if there's a way to incorporate that, whether it's in the structure of a deep
*  network or the output of a deep network, it's used in a way that knows about the
*  physics. You probably don't want to rely on learning that because you're just going
*  to create more room for error.
*  And that same thing is true in a bunch of ways of the dynamics of these tires and the
*  steering wheel. So if you know something exactly, it's probably best to use it.
*  If you know something almost exactly, let's say as your tire wears out, the radius
*  changes a little bit. Therefore, your mapping of the speed of the tires to the speed
*  of the car is not well known.
*  So those are cases where a more complex example would just be like the aerodynamics of
*  the drone. What happens when there's a gust of wind and the propeller spinning at a
*  certain rate and you have the physics of those interactions?
*  Or even if you're taking a picture with your phone camera, like what's the exact
*  model of properties of the lenses?
*  Those things change with temperature.
*  You might assume you know things, but you don't exactly.
*  In those cases, it's probably often best to have that be an initial guess for a
*  learning based system, like something that says, I strongly believe this is the answer,
*  but here's the rough error bounds and you're going to figure out that answer.
*  And so the more you can kind of build in that kind of stuff and then the more the
*  dynamics are very complicated, like pixels to some decision, there's just no possible
*  way to model that parametrically.
*  You just have to you have to learn it.
*  And so I think our journey has been one of just figuring out when to use just like
*  learning and when to incorporate geometric primitives into a deep network such that
*  the job it has is simpler and more fundamentally sound when to give initial
*  guesses in the right ways, when to post process the outputs and combine with a more
*  classical kind of optimization system like with SIMFORCE and where to draw those
*  boundaries.
*  So at the end of the day, there's a lot of value that also comes from the
*  intermediate outputs.
*  Like we don't just create a 3D map of the environment so that we can avoid the
*  obstacles.
*  We create a 3D map of the environment so that we can then scan it so we can show
*  it to the user so we can build a 3D model that gets used for inspection so that we
*  can click on a point on the phone and know exactly how far away it is to then
*  let the operator make a decision.
*  So there's just a lot of trade-offs that come between those and supporting why
*  sort of end-to-end reasoning and design by like a dedicated team that controls the
*  whole stack is really important.
*  You mentioned like eight or nine different networks that are running in this kind of
*  concert with the human designed, the human architected systems and just kind of ran
*  down like a bunch of the different functions that they play and they're all
*  kind of in this, you know, it's almost like they're grafted together with the kind of
*  traditional software.
*  Do I understand correctly then that like identifying things like tree branches is
*  something where video comes in, there's like a neural network component that
*  essentially identifies where things are and then those things, you know,
*  potentially reported as like relative coordinates to the drone itself or whatever,
*  get fed into the highly optimized code that came out of SimForce as like a
*  constraint.
*  You know, that had been sort of all that optimized code had in turn been prepared
*  upstream by somebody that's like, okay, now I'm going to sit down and think about
*  how we want to deal with, you know, a certain class of like objects that are, you
*  know, a certain distance away from us or whatever.
*  I don't know how, you know, we could divide those up in a million ways, but
*  somebody at one point said, okay, when there's a twig that's like above us and it,
*  you know, appears to be small or whatever, we're going to handle it in this way.
*  And now that's kind of translating to all this low level code that's receiving
*  those inputs out of a neural net.
*  But then on the other hand of that, you also have like, well, the outputs of the
*  code itself may be just a guess.
*  And then there's like another neural net to kind of correct.
*  That's a good example.
*  So I think the, the minimum viable piece, the part that is just incomprehensibly,
*  you know, harder, more difficult to do without deep learning is the part that
*  says these pixels of this image are a very difficult to see thin branch.
*  Like that is just, that is the state of the art.
*  And you can take that and you can kind of figure out the rest then of like, let's
*  say you want to build a 3d understanding of that.
*  You need to know exactly where your camera image was taken.
*  You need to know exactly the properties of your lenses to understand how a 2d
*  pixel coordinate maps to a, a ray in 3d.
*  And then to what is the depth we're using by figuring out across multiple frames
*  and motion of the drone or across further kind of a geometric reasoning.
*  So the, the, the interactions between those systems can be designed in multiple ways.
*  And you can go more and then, so you can have a deep network that is not only
*  reasoning about a single image, but it's reasoning about a video of images, or
*  you can have a deep network that's directly thinking about 3d and
*  outputting a 3d representation.
*  Or you can have two separate ones, kind of one that's focused on the pixels and
*  one that's focused on then constructing kind of 3d understanding from, from those
*  representations and there's, there's like real trade-offs between these approaches
*  in terms of how much data you need.
*  That's kind of all synchronized together, how difficult and much of an effort it is
*  to train, how robust you get the output and you know, what the edge cases are.
*  And there's just really valid arguments for a bunch of different approaches, I
*  would say, but the more, and I'll say the more high level you get, the more it's
*  really beneficial to, to joint reasoning and, and, and, and using neural networks.
*  I think that that's kind of really clear to me.
*  You know, the broad trend, right?
*  Would seem to be more designed systems are kind of broadly giving way to like
*  more black box, more end to end systems.
*  Are you starting to see that in your own work?
*  Are you seeing like, or you mentioned, uh, Elon, you know, and one of his
*  favorite mantras that I always think about is the best part is no part.
*  So are you starting to see the opportunity to eliminate components and,
*  you know, kind of merge components into bigger, you know, but potentially less
*  scruitable pieces, or is that not really something that is happening for you yet?
*  In some ways, I think this played out in a more direct way for us when, when deep
*  learning was first emerging and we kind of saw opportunities to get rid of a
*  bunch of, you know, complicated code with, with the inference of a deep network.
*  That for sure, you know, several years ago now happened for us and, and was
*  successful in a, in a bunch of ways.
*  Um, the desire to go all the way end to end, I think has become, I mean, it's
*  increasingly becoming more viable.
*  Um, but when you're talking about things like, you know, these higher frequency
*  things, the dynamics of the robot, there's kind of real trade-offs to that.
*  And so I think there's a difference between kind of what is our biggest
*  focus at Skydio and building right now.
*  And what is, what would be the case if we were to build it all over again and
*  focus on, I think if we were to build it all over again, or put all of our focus
*  on core navigation, it probably would be, you know, more end to end in, in several
*  ways, all of this was talking about kind of the navigational components of the
*  drone, and certainly there's more opportunities to get more end to end.
*  But I want to focus, I want to pivot the focus of what is actually important to
*  be end to end for Skydio right now, because it's, it's very much higher level
*  and more important than I think the, the core navigation blocks of our autonomy
*  system, and it's more about the entire use case of the robot.
*  Like that's what we want to be end to end.
*  That's the ultimate vision of the company.
*  So we want our drone to not be a robot that somebody is flying with a
*  joystick and doesn't crash, no matter how good the doesn't crash in motion is.
*  We want it to be a robot that's an AI partner that's accomplishing tasks
*  completely by itself or really helping somebody that is saving a lot of time
*  and, and reducing danger and things like that.
*  And so when you pick any one of these use cases, like for example, inspecting
*  a bridge, the question is really, how do we get the drone to be a trusted domain
*  expert, how do we make it so the drone understands what bridge inspection is?
*  What different types of bridges are, what type of damage is important?
*  Are we looking at cracks or rust or loose bolts or some other, you know,
*  derelict thing about this, this bridge and how does it accomplish tasks?
*  How does it communicate?
*  And that's, we call this thing the arc of autonomy.
*  So as we go higher level, we want to go from a person who can fly, flies the
*  drone, but it's, but it's easier and safer to the drone is basically doing something
*  for its entire flight without help.
*  So 3d scanning is a good example.
*  Like we set up, you fly and you set up the boundaries of a 3d volume.
*  Then the drone goes and explores the space and builds a real time kind of mesh,
*  which you can see in AR and then you pick some high level parameters.
*  Like I want to scan this from a distance of three meters, which corresponds to
*  every pixel is 1.2 millimeters in size, which tells you how much resolution
*  your 3d model will have.
*  The drone says, this is going to take me 40 minutes, two batteries, 2000 photos go.
*  And then you're just watching this thing and you're sitting there and you're really,
*  you know, think about how difficult that would be to capture thousands of photos
*  and make sure you got every spot correctly with the right overlap to build a 3d
*  model, you have to be a drone expert and the photogrammetry expert, but now you're
*  kind of watching this thing and it's just way more accessible so that a company can
*  do this with closer to any of their employees rather than a trained expert
*  pilot.
*  Then we go a level further, which is really the core thing we're in the middle
*  of now, which is the dock.
*  And the whole idea there is drone is, you know, in a box that has internet and
*  power and could be anywhere in the world.
*  So it could be that your energy utility has 10,000 substations and there's
*  docs installed at every one of them.
*  Sometimes there's people there, sometimes not, but you either give an example flight
*  or you give some kind of procedural command.
*  Yeah.
*  So it already has a map of the site.
*  And what that means is you can schedule a mission to run every hour or every day.
*  And the drone will fly, do its thing and basically capture photos.
*  Those photos get uploaded to the cloud.
*  And suddenly you have basically a system that you install that's much closer to
*  the washing machine or the printer, copier combo than it is what it is to fly a
*  drone.
*  And then it's just delivering data at an enterprise level.
*  Then we have a cloud that has three models.
*  It has semantic understanding.
*  You can schedule new missions.
*  You can plan things out, but at the end of the day, the core production
*  workflows, you're pulling off image data via APIs and sort of like AI insights on
*  that data and integrating with some other system.
*  And those integrations are vast and depend on which of the kind of tens of
*  industries we're operating in.
*  So that whole play of having the dock be this platform that's kind of horizontal,
*  but also building up end to end kind of use cases from the drone flying and being
*  intelligent about what's in the scene to delivering the integration to where the
*  data ends up being stored and used for construction or mining or insurance or
*  whatever.
*  Like that's the end to end that really matters to us.
*  And that's really what we're building for across the stack.
*  And so I'd say the focus is much less on the kind of core algorithms for obstacle
*  avoidance and estimation and so on.
*  We've worked really hard on those.
*  We're the best at that, but that's not where the primary focus is.
*  Yeah, it makes total sense.
*  I think this is why, you know, this concept of like what industries will be disrupted
*  by this.
*  I kind of keep coming back to the strong incumbents are in phenomenal position.
*  Take advantage of the latest developments in AI because, you know, anybody else who
*  wants to come in and challenge you is going to have to redo all that stuff that
*  you've already done.
*  And meanwhile, you know, you should be able to take advantage of the new things,
*  you know, before they can catch up with all that.
*  That seems to be the pattern in just a ton of places.
*  Do you guys publish your pricing?
*  Like, is it known what a like what a dock and a drone would cost me to, you know, if
*  I just wanted to buy and install the level of the drones?
*  I mean, this this drone here, the Skydio 2 is kind of the most affordable thing we
*  have. And in the case where it's kind of for consumers, it's in the realm of like one
*  to two thousand dollars depending on what you get.
*  But as you move up to the enterprise drones and the docks, it is closer to, you know,
*  thousands to tens of thousands of whatever your your package is.
*  And the more the more end to end it is, the more it becomes about solving a problem in
*  the ROI on that problem for that use case.
*  And the sort of pricing is based on the value of that and ultimately kind of software
*  driven where, you know, if something happens to the drone, like.
*  Whatever, that's not a big deal if you get a new drone.
*  So the model changes the more you go towards this dock and end to end and even
*  projecting further forward.
*  It's like you can imagine docks are just installed around a location, for example, on
*  a cell tower, but that same dock can go inspect the house for insurance or it can go
*  respond to a fire when there's, you know, you're crossing getting there way much faster
*  than the fire truck is going to get there and you have eyes on sea.
*  And so you could even imagine sort of the docks as a service that's more like a piece
*  of infrastructure that can be used for multiple clients and has an API.
*  I think that's quite a bit further out for a bunch of practical reasons.
*  But yeah, so it really scales with the model of like, is it a piece of hardware that you
*  fly or is it a really end to end solution?
*  You have the room to do the value pricing because the savings is somewhere between
*  like dramatic and near total.
*  Right.
*  I mean, I'm just thinking like, if I run the Hoover dam, just to take a silly example,
*  and I've got like all this damn, you know, surface that I want to go inspect and look
*  for, you know, cracks in my dam.
*  Obviously being a little silly about the scenario here, but the, you know, there's a
*  lot of surface out there to cover.
*  And if you're telling me that it costs me basically 10 ish thousand dollars to buy one
*  of these things and have it installed and have it go, you know, fly 20 missions a day,
*  then, you know, I compare that to like, what would that cost me in terms of skilled human
*  operators?
*  And it's like, it's going to be somewhere between probably one and five percent and maybe
*  even sub one percent of what it would cost to have a team out there, you know, especially
*  if you're doing it the old school way with like ropes, you know, and in today's world,
*  that's pretty expensive.
*  So it's interesting that there's so much savings that then you can kind of think about
*  pricing in a lot of different ways and still be like a dramatic savings to the customer.
*  I'll give you two visceral examples.
*  I mean, one would be, let's say you're inspecting a bridge and a common way to do that is to
*  use a snuper truck where basically you stop a lane of traffic, you pull a guy over in
*  this like multi-legged arm in a bucket and it goes around the bottom of the bridge and
*  even putting aside the, you know, basically like the safety concerns of operating this
*  truck and what happens when you have an incident, how damaging that is to a large kind of
*  infrastructure player like a Department of Transportation.
*  Just straight up think about the cost of closing down a lane of traffic on an important
*  bridge. And you think you ask, like, what is the price of that per minute?
*  It's astronomical.
*  And a second example is just the cost of using helicopters for something like either a
*  situational awareness use case or they're frequently used for something like transmission,
*  tower inspection.
*  And the cost of a helicopter, both from a safety and training and also from a fuel
*  perspective, is very, very vastly different from a small electric drone.
*  So if I imagine a, you know, not too long time in the future when you've got kind of a
*  broad mesh of coverage and this becomes kind of an Uber style service where I could say
*  on the fire department, I'm going to a scene, I need eyes, you know, and even do it from
*  an app, perhaps. Right.
*  If I'm imagining like, what is the cost of this kind of go to in the limit?
*  I think like, OK, maybe it's a ten thousand dollar setup and, you know, maybe that maybe
*  that lasts a couple of few years, whatever.
*  And, you know, even just taking daylight hours, there's something like five thousand
*  daylight hours in a year.
*  So, you know, it seems like we kind of get down to like a buck a mission.
*  Is that kind of what you would expect this to ultimately be like?
*  Like if I could call my, you know, and at that point, then you then you have like a ton
*  of, you know, consumer, then you're back to being a consumer company, perhaps, because
*  you could be like, I want to get a little aerial footage of my kids soccer game.
*  You know, if it's a buck for me to bring the drone over to total soccer and, you know,
*  just film me and my kids goofing around at their little peewee soccer practice, that's
*  a buck well spent.
*  I mean, does it actually get that cheap?
*  You think? Hey, I can't wait for the day where we get there.
*  And I mean, it seems inevitable at some point, but it is there's a tremendous like just a
*  long path of both technical and product and kind of societal stuff to get to that point.
*  But, yeah, I mean, I don't see why it has to be in maturity.
*  It's different than renting a scooter to accomplish some task or logging into some
*  online service and doing something.
*  So I think if, you know, if we build what we're trying to build, then I think there will be.
*  A whole bunch of industry use case specific kind of apps built on top and companies that do
*  things with these drones and docks and missions to be a more end to end piece.
*  And we're only going to be able to build like the most important couple, right?
*  We have to focus, but we want to build that ecosystem where you can do all these different
*  use cases. And so so, yeah, totally.
*  I mean, if there's a if there's an area that has coverage with docs and you request the
*  mission and it accomplishes some task for you, again, I think that that should you know,
*  that task should be priced accordingly to the kind of value that it's providing.
*  And if you want a sweet selfie with your family, like, yeah, I don't think that should be it
*  should be expensive at all.
*  So is this also the moment as you think about these kind of higher level, more embodied
*  systems, more user friendly?
*  I wonder if this is the moment where you start to deviate from that kind of vertical
*  integration play, because I'm seeing all these things right.
*  And I kind of brand myself an AI scout these days.
*  So I try to, you know, it's impossible to keep up with everything that's going on.
*  But I try and you certainly see some things where I'm like, hmm, maybe you guys want to
*  want to present a sort of.
*  Reasonably high level API, but do you also want to be like responsible for the language
*  model, you know, that that kind of plays the role between cause it sounds like you're
*  going more toward platform and maybe not also like for data that's coming out, right.
*  If you're going to get in those 2000 images, I understand that you're basically to date
*  have like owned the software as well for turning that into a 3D model, but certainly
*  we're seeing like a flourishing of nerf type technologies where I imagine customers
*  increasingly may say.
*  I want to process this in any number of ways that are not necessarily exclusively through
*  your software.
*  So how are you thinking about kind of vertical integration versus platform?
*  And are those things actually ready for the quality that you need yet or are they still
*  kind of not quite there?
*  Yeah, I mean, this is a debate we have every single week and just continually kind of
*  discuss and evolve, but essentially both is the answer, partly because we have trouble
*  saying no to things and partly because it really makes a lot of sense.
*  So I think the dynamics in play, like you gave the example of language models.
*  I mean, as a natural glue of connecting together different systems and APIs, they're
*  immensely valuable.
*  And that's something that we will absolutely use ourselves and also allow others to use
*  by having the right APIs.
*  Same with kind of 3D reconstruction, visual processing, like computer vision is our core
*  competency. Like we have one of the strongest kind of vision and robotics teams around, and
*  therefore it's a very natural fit for us to do 3D reconstruction.
*  We also have more information.
*  We have the surround cameras.
*  We have a lot of priors on our data.
*  We're very good at building better models with our data.
*  But that's not to say we shouldn't let people use many, many other options that are
*  optimized for various use cases.
*  So we want to do the things that we're either really uniquely positioned for or can
*  accomplish through vertical integration.
*  At the same time, because these drones are still like we have a lot of users in a lot of
*  different industries, but especially with this kind of idea of a dock market like that,
*  that market we think should be much, much bigger than the market of manually flown drones.
*  And there is literally no scaled dock deployment on the planet today.
*  We're at a fraction of a percent of what this industry and emerging economy is going to
*  look like. It just does not exist.
*  And for that, to cross the chasm into truly widespread use, that idea of the 10,000
*  substations or whatever, that takes a really long time.
*  And for that, that is kind of just the big picture.
*  Like we have to build some killer apps that demonstrate that and get it all the way there.
*  It's for something like this, it's just really difficult to rely on an ecosystem play to
*  get there. And so I think we have to go both vertical and horizontal.
*  And in maturity, the horizontal becomes more and more important.
*  But to get there and get to that level of like actually creating the industry, I think
*  we have to go vertical for some of the most important areas.
*  Yeah, that very much echoes like the sort of platform plus killer app that you know,
*  even Sam Altman has been talking about lately with, you know, why do they build CHET GPT?
*  It's like we want to have at least one hook into people's daily lives.
*  So we're kind of the first and best customer for the underlying API layer.
*  And it sounds like a pretty similar notion there.
*  You want to provide at least some kind of core, high level services and feel like that's
*  necessary to get to the kind of the scale and value that would really support a third
*  party ecosystem. Yeah, yeah.
*  Just the robots, the robots, the flight, the aerospace.
*  It's also complex to get to the point where really traditional industries are using this
*  thing reliably at scale. We kind of have to bend reality to make that happen.
*  And I think it's really hard to do that without intense vertical integration to start as
*  it gets more mature, then it's it's way more viable.
*  Anything else on just kind of the pure technical side that you want to cover that we
*  haven't? I think robotics is an incredible use case that's getting distilled from where
*  vision and language models will kind of evolve and create value.
*  I think the of the options of those drones are really incredible.
*  Like you've got, you know, manipulator arms, you've got cars, you've got maybe larger
*  aircrafts, you've got drones, you've got robot dogs.
*  And the great thing about drones in that space is that they can fly very close to things
*  and indoors, they can fly very far away.
*  They capture image data and are just very rich to accomplish tasks with.
*  And I guess the downside is they don't interact with the environment.
*  So the manipulation piece is more missing, although I think there's good opportunities
*  for that if we were to focus on it.
*  But the other nice thing about the drones, like if it crashes in our testing, it's not
*  nobody's going to die. And it's not nearly as big of a deal as if you're working on a
*  self-driving car. The iteration speed is real and there's real customers.
*  You're not waiting to get to some level of usability to be able to sell it at all.
*  They're already useful in a bunch of different industries.
*  So that combination of having this fleet of robots that is state of the art and we can
*  develop on, but also is being used already in a bunch of different industries is a really
*  great spot for us to be in.
*  And I think that's a really great canvas to then apply the latest generation of foundational
*  models and development in AI to accomplish higher level tasks.
*  And so I think I'm just super excited about that.
*  And it's going to trickle down to all parts of robotics.
*  But I think our little drones are a wonderful spot of that.
*  Is this kind of more embodied layer?
*  How does that relate to all the work that you've done to keep things on device?
*  Obviously, we talk about that from a couple of different angles, but I don't envision you
*  running like a language model on the drone.
*  But maybe I'm you know, maybe my imagination is too limited there.
*  Every core function of the drone runs on device.
*  And the reason it does is because you could be out at some location that's remote and
*  has no Internet connection at all.
*  No, no cell service, no Internet.
*  If you have Internet, it might be intermittent or it might be very low bandwidth.
*  And you just can't rely on that for something like obstacle avoidance.
*  Right. No way.
*  And so the drone has to do everything on board.
*  And we just put years and years of work into making things fast and optimized for that
*  purpose. So as it transitions to more of kind of a doc based world, you think, OK, well,
*  now it's Internet connected, right?
*  It has maybe it has 5G on the drone or maybe it's talking to the doc directly or talking
*  to infrastructure kind of Internet that's set up at a facility.
*  But still, you know, you go to most warehouses and you ask about the quality of the
*  Wi-Fi and the coverage that you're not going to hear good things.
*  And so it depends again on what layer you're relying on it for.
*  At the end of the day, it's really best if the drone can do its whole mission without
*  needing to rely on a link directly.
*  So there's tradeoffs there.
*  And I think there's there's viable approaches for the high level stuff to basically be
*  running on the cloud.
*  And certainly if you have good coverage and embodied AI and issuing high level commands,
*  like it might work.
*  But at the same time, as we have new generations of drones, improve compute, more
*  accelerators and chips, like absolutely no question, we can be able to run language
*  models and foundation models and distilled versions of them on the drone.
*  I think a simple example, like I think the rate at which these models are being
*  accelerated, both the language ones and stuff like stable diffusion, like they are
*  they are running on phones.
*  They're running on local phones at some some rates and they're going to get faster
*  quicker. So the biggest models, the most parameters, the state of the art are never
*  going to be at that point.
*  But the rate at which they get distilled down and they faster, especially if you
*  narrow the use cases, is is enormous.
*  It's much, much, much faster than Moore's law or anything like that.
*  And so I think we basically see a ton of viability in running important, larger,
*  more common sense, general purpose models, both on the edge and in the cloud.
*  Presumably the the weight of the chips is not a big deal relative to the total
*  weight. But the power consumption might be especially as you layer on more and more
*  different models and more parameters and so on.
*  I've heard that from some self-driving companies that the power consumption of
*  the self-driving system can actually be like material even compared to like the
*  actual moving of the car to the mileage of the car.
*  Yeah, that it'll take down the mileage.
*  You know, for example, if you have a I don't know about Tesla specifically, I'm not
*  like citing any particular manufacturer, but a friend who works in the industry
*  said kind of a dirty secret of the whole thing is that it'll take like 25 percent
*  off of your range because it's a super power hungry system.
*  Do you know, like off the top of your head, what when you send out a 30 minute
*  flight, how much of the energy is going to the compute as opposed to, you know,
*  actually spinning the the blades?
*  Yeah, I mean, first, the self-driving car and you gave sounds.
*  Utterly insane to me, given how many thousands of pounds of car you're moving.
*  That seems pretty nuts.
*  It's hard for me to conceive that.
*  But yeah, for us, I'm going to take the other side of that.
*  Basically, like if you're if you're flying for us, the compute package of everything
*  is probably in the realm of maybe.
*  10 percent or so, but the impact from the weight is actually much more.
*  And that that is just the truth about these small drones is that when you're
*  designing the drone, the efficiency and basically battery life of the drone
*  really depends on the size of the propellers.
*  So the bigger the propellers, the more efficient it can be.
*  And then essentially the weight of the thing.
*  So the most efficient way you can make a drone of a certain size is to make the
*  propellers as big as you can and then have as much weight be the battery and as
*  dense of a battery as possible.
*  So it really nonlinearly scales with any other things you need to carry, which
*  ultimately are the cameras, the chips, whatever sensors you've put in.
*  But the biggest pieces are the payload cameras.
*  So this is the sort of like main at three axis gimbal and the boards and
*  chips you have on board and those things when you need to carry that payload,
*  basically scale up the size of the propulsion you need and take just just
*  influence the design of the entire drone in a really outsized way.
*  And so the weight of carrying these chips and by the way, the weight of a cooling
*  system to dissipate any thermals you need to dissipate also have an outsized impact.
*  And so certainly relative to cars or who's going to notice a couple of extra
*  pounds, we're talking about adding five grams has an impact on, you know, the
*  performance of a drone like this.
*  So in that sense, like the size of the computer in some ways is more
*  important than the power usage.
*  Gotcha.
*  So there's kind of three drivers there of putting the compute or three
*  consequences of putting the compute on the device.
*  There's the extra weight of the thing itself, the extra weight of the cooling
*  system, and then the extra energy that both of those are going to use, which is
*  going to in turn make a bigger battery and all of those are getting worse.
*  You know, that's a compounding problem, obviously.
*  So, but it's interesting that you're basically saying the, the weight of the
*  chips is a bigger deal, especially when I guess the weight of the cooling in
*  particular is a bigger deal than the, than the extra energy that it needs,
*  which in turn makes a bigger battery.
*  I'm kind of surprised, but obviously, you know, your stuff.
*  That's, that's fascinating.
*  I'm going to have to go back and talk to my friend in the self-driving car
*  game and see what, where all that energy is going, dig a little deeper on that one as well.
*  I mean, just consider that our drone has to keep this thing in the air.
*  You know, a car is rolling along the ground and it already is thousands of pounds.
*  The drone is like orders of magnitude different than that.
*  The self-driving car thing, I think is strikes me as a very like weird kind of
*  disconnect between what I have personally experienced just riding in a FSD Tesla
*  not long ago and the sort of broader narrative, which is like, it's many years away.
*  It didn't feel like it was many years away to me when I got in one, my
*  neighbor happens to own one and just, you know, he put into the navigation system.
*  Here's where we want to go.
*  And we just rode and the car drove the whole way city streets, get on the highway,
*  get off the highway, did everything but park ugly.
*  What's your view on that?
*  Do you think that we are actually a lot closer than people think?
*  Or what's your, what would you kind of expect for like consumer autonomous
*  systems, like, you know, the, obviously the crown jewel goal is the self-driving car.
*  Yeah.
*  Yeah.
*  So I'm, I'm pretty close to this because my best friend and actually several
*  friends work at Tesla autopilot.
*  And then I'm also close friends with another self-driving founder of a
*  company called wave in the UK that is really focused on end to end approaches
*  to self-driving.
*  So in both those cases, I mean, I think the, it comes down to just like a lot of
*  stuff is handled well, and you may go on drives that feel incredible and you just
*  see incredible things happening, but the end of the day, you know, autopilot is
*  in a mode where you're, you know, the humans expected to take over, right?
*  It's beta it's technically, you know, things.
*  So if you had a car and you want to truly just chill and sleep in the back while
*  it's doing its thing, what is the one out of every drives of it crashing?
*  Would you be okay with if it was one out of every thousand drives, would you,
*  would you accept that?
*  Um, or if it was when on a day where the weather is really nasty and it's a
*  combination of, you know, hail and fog or something, or you go somewhere new or
*  there's some horrible construction with the wrong sign put up or something.
*  And so just the, the distribution of this stuff is so far down the tail end of edge
*  cases where the easy case is just like, that's been solved a long time ago.
*  Um, and so, you know, there's different, there's different approaches to this
*  from gathering data, massive scale to like, relying on foundational deep
*  networks that can generalize and reason like a human would and adapt to, to
*  approaching this problem.
*  But I think in some ways we just see fatigue because people have been talking
*  about self-driving being, uh, people, including Elon talking about how it's
*  so is a year or two away and now it's been a decade.
*  Um, and I think we're getting, we're getting closer and we're making progress.
*  Um, but it's, and it will happen and we are getting, yeah, but it's just, it's
*  one of these things that's just the horrible dynamics from a product side of,
*  of, for it to actually ship as a thing, not as a beta that you're ready to take
*  over, but as something where you're actually trusting your, your baby to be
*  asleep with you in the back.
*  It's just like such a different bar that you need to get to.
*  And frankly, that bar is much higher than the actual accident rate of a human
*  because every human is like, thinks that they're a better driver than the average.
*  And every human would rather that they made a mistake and crashed than an AI
*  that's driving, made that mistake and crashed.
*  Um, and I think it's just untenable until you can prove that you're not just
*  better than a human, but orders of magnitude better.
*  We may already be better than a human in many cases.
*  I think that's, I mean, that's really interesting.
*  Do you, and I imagine you have a version of this that you deal with at Skydio too,
*  where it's like, you know, people have been doing these tasks in all sorts of
*  ways, right?
*  Whether it's literally climbing the cell tower with a rope versus, you know,
*  driving a, you know, an earlier generation drone manually or, you know,
*  whatever in between, do you have a kind of hurdle that you guys try to, you know,
*  try to hit or convince, you know, demonstrate to people that you've hit?
*  What do you think that hurdle should be?
*  Like to me, honestly, you asked the question, like, certainly if it was one
*  order of magnitude safer than human driving, I'm on board with that.
*  Like it's, you know, I can't credibly think I'm more than an order of magnitude.
*  I doubt I'm an order of magnitude better than average.
*  That seems like a pretty bold position for me to take.
*  Maybe, you know, if I'm really good and really, and I think I am like, you know,
*  more careful than some of the YAHUs I see around, you know, around me, but still
*  order of magnitude is a lot.
*  Do you think that is like just still societally not enough?
*  Or what do you guys see from your customers, you know, in terms of what
*  their elevated standard is for systems versus humans?
*  Yeah.
*  I mean, for the car case, I think order of magnitude is about right in my mind as
*  well from, from the drone side of things.
*  I think it's pretty different.
*  Like you're not like people's lives aren't at stake in the same way.
*  In some ways you're like, obviously taking the safety of people first when you,
*  when you replace some, some dangerous activity with the drone.
*  But we see these dynamics, I'd say more playing out like somebody who's inspecting
*  a structure in some other way, even with a drone today, like they're manually
*  flying a drone, um, with a trained pilot, like may that they'll have incredible
*  sort of procedures and safety precautions.
*  They have a standard operating procedure that has these, these steps and you don't
*  fly near things and you zoom in and you take photos from these angles and here's
*  what you do and here's your pre-flight checklist and all of those things.
*  So sometimes we'll come in with a drone and we just say, look, our drone will just
*  zip around the scene all willy nilly.
*  It'll build a 3d map.
*  It'll go up to two feet away from these objects and it'll take close up pictures.
*  Um, and that's awesome and mind blowing, but it's, that's so far from being a place
*  where this, this operator is like, and this massive company that's built these
*  procedures is going to be able to adopt that.
*  And so there's a, there's a huge gap there of how do you, how do you get the benefits
*  and efficiency and so on, but also meet the sort of like safety and operating
*  procedures and just ultimately enact change in a really important, critical,
*  slow moving, slow moving for a reason organization.
*  Um, so I think things like that are, are super common.
*  And I think that kind of relates to the human robot interaction element of all
*  this, where anytime you have emotion of the drone, that's not understandable, not
*  predictable, um, it creates uncertainty.
*  It creates worry.
*  It's like, why is this happening?
*  I don't understand it.
*  How do I control it?
*  Um, and so there's a lot of like design of making the drone more predictable
*  and controllable than there's the communication of having UI, having
*  designs, having explanations to know what's happening and take action.
*  So all those things together are a key part of our experience.
*  Very interesting.
*  That also gets to kind of a, another huge trend, which is just, you know, what is
*  going to be the future of jobs and work and all of the, what happens to all the
*  drone operators, I guess, in this case, it seems pretty clear to me that like,
*  you know, even if you scan a ton more stuff than is currently scanned, that
*  this should ultimately require less human labor hours.
*  And in some sense, that's like the whole point, right?
*  It's, it's safety.
*  It's there's a variety of different value drivers, but ultimately the cost savings
*  probably is the one that's going to, you know, keep you expanding your
*  factories time and again, what do you guys, you know, is that part of the
*  discussion that you have?
*  Is there a, is there an internal discourse at the company about this kind of, you
*  know, societal impact that obviously you guys are a small part of, but I find that
*  broadly this debate is kind of characterized by denial.
*  It seems hard for me to imagine that it's characterized by denial at Skydio, but I
*  wonder, you know, what that leaves you with.
*  The dynamics are pretty different from what I would say is kind of going to
*  happen with large language models and near kind of AGI adjacent kind of
*  software where a lot of white collar work across many industries at the same time
*  will be kind of like competitively driven down in money-making potential.
*  I think that's like a very tough societal problem.
*  I think in the space of what we operate in, it tends to be more dangerous jobs
*  and on kind of, yeah, not fun ones.
*  It's, it's very hot.
*  It's very cold.
*  It's very remote.
*  It's very laborious.
*  It's dangerous.
*  And so I think that kind of work combined with this idea that the, especially
*  this dock market is a fraction of a percent of where it can be, I think
*  leads to a place where people that are doing these jobs now, for example, you
*  know, climbing the towers or, or in helicopters, like it's kind of better
*  for everybody if that's not happening.
*  And I think in most cases, the people that have the expertise in these areas
*  can become the people that have the management of a larger number of drones
*  that are doing the work and the domain understanding of how to design those
*  missions, how to operationalize them, how to run this program.
*  As if they had a team of the people that are now the blue collar workers
*  and they become the kind of manager.
*  And so I definitely think there will be an impact in a bunch of ways.
*  And like all areas, like people need to adapt.
*  If they don't adapt, they're going to be in trouble.
*  I think in our case is way more credibility to say, like, these are, these
*  are trickier jobs and the people involved have the right skills to bring the
*  change of operationalizing all of this, to turn it into a place where we do have
*  way safer, way more frequent inspections.
*  And we solve these problems.
*  I mean, just think about something like warehouse workers, like there is such
*  a shortage of them right now.
*  It's, it's, it's a gigantic problem and not even just in the U S yeah.
*  So, so I think, I think it's definitely something we think about.
*  It's definitely something where people need to adapt.
*  It's something that we're trying to be thoughtful about.
*  I think there's a lot of reason to be in some ways more optimistic there than
*  the job of kind of a middle, you know, tier software developer or something like that.
*  Yeah.
*  It's coming for a lot of different things all at the same time.
*  And I probably am with you on the idea that like, I would even broaden it out
*  on some level to like for jobs that people don't want to do unless they're paid to do.
*  Then if we could get us, you know, an AI to do those jobs, like that's great.
*  You know, that does obviously leave us with kind of a big societal restructuring
*  question of how do those people still get to eat if they aren't doing the jobs that
*  they are only doing now because it allows them to eat.
*  So there's like a, a new, you know, arrangement perhaps that needs to be developed.
*  Universal basic income.
*  Yeah.
*  I mean, are you, it sounds like you're ready to endorse that.
*  I'm ready.
*  Yeah.
*  Yang gang, but I don't think we as a society are nearly in a place to execute on that,
*  at least in the, in the U S like the world is barely hanging on from not just having
*  it all be entirely authoritarian dictators.
*  So there is an amazing society from the gains and productivity we're going to have if we
*  play our cards right.
*  But we're pretty far from being in a position to play our cards right.
*  I'm afraid about that big time.
*  Yeah.
*  It's I've started saying it's the smartest of times.
*  It's the stupidest of times.
*  It seems like somehow they're, you know, they're coexisting in a really weird way.
*  But I'm broadly with you.
*  I think the UBI vision makes a lot of sense and it would, it would smooth the transition
*  that seems like it is coming at us in a, you know, at a, at a pace that is not necessarily
*  shaping up to make things super smooth.
*  So anything we could do to kind of ease, you know, transition for all sorts of people
*  seems like a great idea to me.
*  If it happens, you know, it's always happened to different industries over and over and
*  over in history and society adapts.
*  If it happens in all of them at the same time, that's much more dangerous, the quicker it
*  happens.
*  And I think that's, that's part of the risk.
*  The possibility of that leading to, you know, just an incredible amount of wealth
*  inequality is, is very high.
*  It's not managed carefully, but the potential for enormous style wins are there too.
*  Well, here's hoping we can go from here to there.
*  You mentioned also authoritarian dictators, which is the natural bridge to my last topic
*  that I wanted to ask you about, which is the use of drones in the military and specifically,
*  it's been widely reported as a key dynamic in what's going on in Ukraine.
*  I guess for starters, like you guys do sell drones to defense from what I've seen, they're
*  purely kind of eyes in the sky situational awareness products.
*  Are you able to and are you selling them like directly to the Ukrainian forces or what is
*  that kind of supply chain look like between the company and the customer in that case?
*  Yeah, I can caveat that I'm, you know, I'm an engineer, but I do have a decent amount
*  of visibility. So, yes, Skydio, absolutely.
*  We sell to both kind of like local police and fire and things like that, and also all
*  branches of US government and international governments as well.
*  So we definitely have I don't know that if we work, you know, how directly it is with
*  Ukraine versus kind of partners that act as players there.
*  But but absolutely, Skydio is a company like we have.
*  We have a lot of expertise.
*  We have a lot of veterans and Navy SEALs and experienced people in that area and a lot
*  of understanding of the product needs.
*  So from a product perspective, we are focused on camera drones and sensors like we have
*  a set of published kind of principles.
*  And one of them is that we will not weaponize our drones.
*  And for a bunch of reasons like we're just we're focused on the camera and the reconnaissance
*  as the core focus of our products there.
*  And so we have definitely sent people to Ukraine from Skydio to to train and provide
*  effective use of these things.
*  And there's a bunch of different things happening, like there's absolutely people strapping
*  things to cheap drones and using them in warfare.
*  Then there's larger devices of different classes.
*  And we are like a slice of that for reconnaissance.
*  And we have, I guess, certain advantages in kind of being well, the largest incumbent
*  drone company is a Chinese company called DJI.
*  And that's kind of they're amazing at making hardware and low cost and something.
*  And so we're the largest US drone maker, the largest world drone maker.
*  So there's some geopolitical dynamics there that go on with the company and also in Ukraine.
*  The other thing is just our drones with the autonomy tend to operate better without
*  GPS. And so that's kind of a key thing where you can just assume GPS doesn't work in
*  Ukraine, whether it's jammed or faked or whatever.
*  It's just not really great to rely on.
*  And so that's the sort of ecosystem in which things happen.
*  And I think people are realizing that, again, small drones are so much cheaper than human
*  lives or larger traditional defense equipment that's orders of magnitude more expensive
*  that it plays a role.
*  The weight of the device, just from the couple of times you held it up, it looks like it's
*  like two pounds at most.
*  Yeah, this one's just around two pounds.
*  Our current gen kind of enterprise drones a little bit more, but not a ton more.
*  Obviously, as you mentioned, a ton of different drones from a ton of different places in
*  the field. But does that have the power to attach something that you could then carry
*  and deliver somewhere? It seems like it wouldn't be able to carry much at all before it
*  would just be too weighed down to.
*  You know, to carry out the mission.
*  Yeah, a tiny bit, but definitely our drones are not optimized for that, especially these
*  ones. And even you have to if you have the autonomy system enabled and the cameras see
*  something they don't expect. So there's yeah.
*  So I think you can make it work, but it's just like you're better off buying a toy
*  drone if you're trying to carry something.
*  At some point we may focus on delivery and maybe that has a wing drone and there's some
*  amazing companies working on that, like ZipLine is a great American drone company focused
*  on that. But that's not our focus right now.
*  There's so much surface area with just cameras that we're going to we're going to roll with
*  that for quite a while.
*  So what have you learned from watching this conflict unfold from the particular angle
*  of being somebody who makes drones?
*  I don't know how qualified I feel for that.
*  I mean, I think war sucks is the one that kind of becomes real.
*  And I think a lot of people just didn't expect something like that to happen in the modern
*  era. Like it felt like Europe could not break out into war like it seemed inconceivable
*  to most most people.
*  Yeah, I think mostly just how real it is and the fact that we've had a bunch of people
*  from Skydio go to Ukraine to the Polish border and work on training and it just makes it
*  all more real.
*  So I haven't done that.
*  I'm not like that's not where my focus is.
*  But yeah, it's wild.
*  Is it feeding back into the product development cycle at all?
*  Like I read one report that there's like 10,000 drones that Ukraine is losing on a
*  monthly basis. And I see probably the again wide variety of makers and sources of those.
*  But electronic warfare was kind of cited as like the way that they're being knocked out of
*  the sky. I really don't know a lot about that.
*  But I imagine that must be something that you're kind of thinking, jeez, next generation,
*  you know, especially in defense, like what kind of defenses, if any, could we try to try
*  to build on anything that you could share about the future there?
*  I mean, I think the most the most common thing there is basically like jamming or spoofing of
*  GPS, since most drones is traveling long distances, you're issuing, you're relying on
*  GPS satellites. And that's just like kind of a no go.
*  So there's definitely a ton of product feedback and features that come back in around like,
*  you know, what is what is just getting in that mindset?
*  Like the average robotics engineer is not in that mindset of what is a useful product
*  feature in that scenario.
*  So definitely being able to do missions with less reliance on external signals is like
*  the number one thing.
*  But there's a bunch of different product features and that gets into the nuances and details of
*  everything. But we as like a dual use kind of commercial enterprise government company,
*  we just get from all the different industries, we get a lot of different product requests and
*  features. And, you know, it's hard, but we're trying to balance like those pipelines and
*  how do we have a unified product vision that covers as much as we can and makes, you know,
*  that's the biggest execution risk of the company is like having a lot of good use cases
*  that we do, but no like amazing ones.
*  And I think it's it's the challenge of, yeah, the horizontal and vertical balance and
*  having the right features that we build in the right order that in some ways you want to spread
*  the pain out. So you're developing all the different use cases.
*  But in some ways you really want to prioritize and say we're going to make this amazing and win at
*  this and then move on.
*  And so I think certainly from a Ukraine type scenario, it's a use case that's really
*  important and something that we want to like understand the product and do the best that we
*  can while also realizing that we're not a defense contractor.
*  And that's not that's not that can't be the primary focus of what we're doing either.
*  Obviously, there's been conflict in your own home part of the world, too, between Armenia and
*  neighboring Azerbaijan. And you were just there as well.
*  So, you know, I don't know if there's any intersection between your visit and kind of drones and
*  all of the I'm sure they're being used in that theater as well.
*  Right. Absolutely. Yeah.
*  I was at the Azeri border and you could see like flags of both types lined along both sides.
*  And even there was a drone strike the day after we were in that area.
*  And so there's a lot of kind of Turkish drones going to Azerbaijan being used in this in this
*  conflict. And there's a lot of ways to look at it.
*  I mean, it's a it's a really sad thing.
*  I mean, obviously, the conflict in Armenia for us, but also the use of.
*  Of drones in those ways, and I think for a bunch of reasons, basically, I'm I'm against
*  especially weaponized autonomous systems, and that's really, really common across robotics
*  researchers and AI people.
*  And I'm squarely in that line.
*  And it's hard to not get wrapped up in kind of an arms race of like, well, this this entity is
*  doing it. We have to do it, too.
*  And there's a lot of arguments for that.
*  But it's yeah, it's just a really tough thing to navigate.
*  But like any sort of powerful new technology, it gets used in a lot of really good ways and
*  it gets used in some some really bad ways.
*  And it's a tough thing to navigate.
*  Yeah, I think that's one of the biggest themes of this show.
*  So that's a great sobering, but very real note, I think, for us to end on.
*  Hike Barteros, Skydio, thank you very much for being part of the cognitive revolution.
*  That's been a blast, Nathan. Thanks a lot.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it and I recommend you use it to use Cogrev
*  to get a 10% discount.

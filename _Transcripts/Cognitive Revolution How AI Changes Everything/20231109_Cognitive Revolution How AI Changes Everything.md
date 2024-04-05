---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 5799s
Video Keywords: ['self driving car']
Video Views: 968
Video Rating: None
---

# OpenAI Invests in the Self-Driving Race with John Hayes, Founder of Ghost Autonomy
**Cognitive Revolution "How AI Changes Everything":** [November 09, 2023](https://www.youtube.com/watch?v=2I3snMT_Qrg)
*  What we're putting together is the car should tell you like why it's doing what it's doing
*  in plain language.
*  If you've rented a car that has like a bunch of features on it, it will like beep at you
*  and show you some symbol you've never seen and you don't know why it's beeping at you.
*  And it has this very, very narrow communication path.
*  And so I think the next evolution is like, yeah, you should just chat with your car and
*  tell it what you want.
*  Let's turn on absolutely everything.
*  You tend to get sensible answers and you can ask it to explain the answers and explains
*  the answers in terms of visual elements of the scene.
*  You're going to make a system that out of the box is dramatically more reliable.
*  But hallucination is actually the best part of these models because the hallucination
*  is where all the common sense applies.
*  And so when you're asking to incorporate not just all the knowledge of the scene, but all
*  sorts of the entire depth of knowledge that could be applied, you tend to get more answers
*  that are closer to reality than what an engineer having to express their thoughts in a programming
*  language would be able to express.
*  I think the amount of creativity that's going to unlock, we don't even know the limits.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture
*  of how AI technology will transform work, life and society in the coming years.
*  I'm Nathan LeBenz, joined by my co-host, Eric Thornburg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today, my guest is John Hayes, founder and CEO of Ghost Autonomy.
*  If you thought that the OpenAI news was exhausted after Monday's Dev Day, today's episode shows
*  that you were wrong.
*  Just two days later, OpenAI and Ghost Autonomy are announcing a new partnership, including
*  investment from OpenAI's Startup Fund, to bring large multimodal models to the grand
*  challenge of self-driving cars.
*  Since its founding six years ago, Ghost Autonomy has raised more than $200 million to pursue
*  a standalone software-primary strategy, building an integrated driving system on commodity
*  hardware and working toward long-term strategic partnerships with carmakers.
*  Now, today, as we all know, self-driving cars are on the road but are not quite ready for
*  prime time at scale, for a mix of reasons, both technological and sociological.
*  On the technology side, one of the major challenges has been figuring out how to handle all the
*  unusual edge cases that humans navigate with common sense.
*  And that's where Ghost's new partnership with OpenAI comes in.
*  On top of the many low-level, high-frequency, but fundamentally very narrow components
*  that they've already built, the plan now is to use a large multimodal model, complete
*  with general world knowledge and common sense reasoning ability, to make the high-level
*  decisions and tell those lower-level systems what to do.
*  In this conversation, John shares an overview of the autonomy space, including the different
*  kinds of technology stacks that companies have developed and the strengths and weaknesses
*  of each.
*  The details of their new plan to combine super-specialists and highly generalist systems
*  into a single human-level AI driver.
*  And his perspective on some of the non-technical challenges that companies in this space still
*  have to overcome.
*  As noted in my recent conversation with Flo from Lindy, I am very much an accelerationist
*  when it comes to self-driving cars.
*  And I would love not only to see this technology work, but to see society embrace it for the
*  life and time-saving value that it promises for all of us.
*  As always, if you're finding value in the show, we'd appreciate it if you'd share it
*  with a friend.
*  And of course, we welcome your feedback.
*  Our email is tcr at turpentine.co and I am easy to find on just about every social network.
*  For now, I hope you enjoy this window into the historical challenges and the new opportunities
*  in self-driving with John Hayes of Ghost Autonomy.
*  John Hayes, founder and CEO of Ghost Autonomy, welcome to the Cognitive Revolution.
*  I'm happy to be here.
*  Let's get into it.
*  Yeah, excited to talk to you today.
*  So big news coming out of your company.
*  And we will get into this in plenty of depth.
*  You are announcing today a partnership and an investment from OpenAI to bring multimodal
*  models to the self-driving space.
*  Maybe give us a quick high level on that.
*  And then I want to kind of take it back to the beginning of how you got into this and
*  started the company and the journey that you've been on.
*  And then we'll kind of circle back to how the addition of this new technology is going
*  to change the game.
*  This is the culmination we've been chasing OpenAI since March when they originally announced
*  GPT-4 with the multimodal.
*  And it wasn't quite ready at the time.
*  But what we saw was a real change and almost a reset in how autonomy for vehicles.
*  And I think most of robotics would be built.
*  And we can go back to the beginning about how it used to be built.
*  I think it's going to be very different in the future.
*  But this is just another area where AI is basically destroying whole areas of computer
*  science.
*  And so I think we're seeing stuff out of Tesla that's sort of acknowledging this reality.
*  But I think we're the first company to put multimodal LLM directly on the driving path.
*  And that's very exciting.
*  And I think everyone's going to be doing that sometime soon.
*  Cool.
*  Well, yeah.
*  So let's go back and kind of do a reprise of the history.
*  Just I guess, first of all, briefly on yourself, I understand you're a serial entrepreneur
*  and kind of a technology polymath who has done a few different things.
*  Company before this was called Pure Storage.
*  And that was a 10-year journey.
*  And then you moved from that into the self-driving.
*  So I'd love to...
*  Is there a connection there other than just kind of, hey, I want to go do another 10-year
*  super hard thing that led you from one to the other?
*  There isn't that much of a connection, but there is a connection that we'll go into.
*  But before Pure Storage, I first moved to California to work for a virtual world company.
*  That was like the first big startup I joined.
*  I was at Yahoo for a couple of years.
*  We were doing talent search and then went into Pure Storage.
*  And a lot of that was just sort of connections.
*  I was very, very interested in the underlying technology.
*  There is a thread that connects Pure Storage, which is a data storage company, a home
*  to self-driving.
*  And the insight that we had at the beginning of Pure Storage was we were looking at Flash.
*  And this was, you know, turned back the clock to 2009.
*  And Flash was taking over the consumer space.
*  So you had the MacBook Air was just released.
*  The most expensive computers had Flash in them.
*  And also the $100 laptops had Flash in them.
*  And then all the mobile devices had Flash in them.
*  And what was obvious was that Flash was just going to completely take over the entire
*  consumer space.
*  And our bet was that it would also take over the enterprise space.
*  And so we spent a lot of time taking that product out of the consumer space and putting
*  it into the data center.
*  And it took a lot of smart software and a lot of engineering to make that work.
*  But ultimately, we were proposing a product into the market that was about the same cost
*  as the storage system you're buying, but it's 10 times faster and is much more reliable
*  and much more energy efficient.
*  And all the benefits you get from just incorporating new technology.
*  I wanted to apply some of that same formula to get into autonomy.
*  And so I live in Mountain View, California.
*  So I've been surrounded by autonomous vehicles for almost a decade.
*  And there are two things that were sort of notable.
*  One is that there was a lot of utopian thinking.
*  So this is back in 2017 that people would just stop owning cars.
*  And if you look at how people actually drive or how they actually use cars, that didn't
*  seem very likely.
*  People don't use taxis very often.
*  It's like about 1% of trips are taxis and you throw in all of public transit, you get
*  another 1%.
*  And so you have this very, very concentrated use of taxi, mainly in large cities.
*  And then you look at the total use.
*  It's like, well, if you have a child under the age of eight, it's like you have a car
*  seat, you have stuff in your car.
*  It's an extension of people's homes.
*  But then the other thing was they were building very, very expensive products.
*  Like they were taking in the sensors and LiDAR, very expensive computers.
*  And so it seemed like those companies were missing 98% of the market for trips and that
*  there wasn't going to be a way for them to easily scale down.
*  And so again, we bet on two big technology trends that seem almost undeniable.
*  I'll talk about some of the objections.
*  One of them was that we bet that mobile technology, mobile cameras, mobile CPUs, would
*  just keep getting better because you have massive investment in those, like the sensors.
*  If you look at the new release of a phone, the only thing people care about is how are
*  the pictures better?
*  That's it.
*  They don't even show the front of the phone.
*  They don't show the apps.
*  Like people take that for granted.
*  They care about that one sensor.
*  And then the other thing was that AI was going to clobber all of the technology that had
*  been developed to date.
*  And so if you look at the people who started basically every autonomy company, look at
*  the people who started Waymo, Cruise, Neuro, and companies that have left us, they were
*  actually derivative of the DARPA Urban Challenge from 2004 to about 2008.
*  And the approach that was taken in the DARPA Urban Challenge, the assumption was, well,
*  we're going to have a map.
*  We're going to map out a city.
*  We're going to tell you exactly where everything is.
*  You're going to use LIDAR to look for mobile objects, like car-sized mobile objects.
*  You're going to use cameras mainly to tell what signal states are.
*  Because in 2008, you just didn't have good image recognition.
*  And now you just have a simple problem where you just have to solve whether you can keep
*  going or not.
*  And that's been the foundation of robotics.
*  It's this idea that you have to solve what track you're going on.
*  Well, 10 years into it, it's clearly not that easy.
*  And when we started in 2017, we thought that they're not going to do without a big technology
*  reset.
*  The prevailing opinion was that the sort of robotics approach, as they sort of incorporated
*  small amounts of AI into specific things, specific recognition, specific maneuvers,
*  specific predictions, that they were just going to grind and they were going to get it done.
*  It was going to happen any day now.
*  At the same time, there are a lot of criticisms of AI, which are similar to the criticisms today.
*  One is like, it's opaque.
*  It is not necessarily reliable.
*  Today, we worry about that LLMs have hallucinations.
*  It's like, yes, everything does.
*  My assumption at the time is very, very large bodies of software are also opaque.
*  No one really knows how they work.
*  All we do is we test them and we see whether they work or not.
*  And models are basically the same.
*  And so what I assumed is that AI was just getting better and better.
*  It was just knocking down all sorts of problems, like from game playing to voice recognition,
*  to image recognition, that had been subjects, intense subjects of study in the past.
*  Computer science for decades, like 40 or 50 years.
*  And it was being replaced with, you know, make a model to do it.
*  And so our assumption was you could put these pieces together.
*  One is you would take all of your off-the-shelf sensors coming back to consumer
*  because they would just get better and better.
*  You would connect them to AI because you would get all the information you need out of the scene.
*  And that sort of model of building a product would be ultimately far superior
*  to any human written algorithm for planning on where you're going to drive.
*  Yeah, that's fascinating.
*  There's a lot there, obviously, to continue to unpack.
*  Just kind of setting the level because this is actually the first full self-driving,
*  not full self-driving, but full first episode we've done dedicated to the self-driving problem.
*  We've just done one episode in the past on autonomy more generally.
*  And that was with a guy from Skydio.
*  And as you're talking, definitely one thing that really overlaps with their project is
*  they've been in business a little longer.
*  They had developed a very deep technology stack that operates at multiple different
*  orders of magnitude in terms of cycle time.
*  And this really kind of crazy mechanism for converting high-level instructions down to
*  the super lowest level control systems within their drones.
*  And it's all fully explicit.
*  But as you said, that doesn't mean it's transparent.
*  It's not a learned system.
*  It's an engineered system.
*  But still, at the end of the day, nobody can really read the code that it generates
*  because there's just too many layers and it becomes kind of opaque in its own way.
*  So I think that's kind of a fascinating phenomenon that kind of keeps popping up
*  in some of these deep tech problems.
*  I understand that there's kind of a big division and you're kind of alluding to it with the
*  LIDAR type systems, expensive specialized equipment versus the kind of consumer
*  quality hardware commodity essentially cameras that are kind of at the heart of some of the
*  systems like the ones you're building.
*  Could you kind of give us a little bit more of a zoomed out just like taxonomy
*  who's out there?
*  I think people know names in the game of your Cruzes and your Waymos,
*  but I don't think people have a sense for the fundamentally different approaches
*  that are kind of on the road today and how that's kind of leading into the future.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Real quick, what's the easiest choice you can make?
*  Taking the window instead of the middle seat, outsourcing business tasks that you absolutely hate.
*  What about selling with Shopify?
*  Shopify is the global commerce platform that helps you sell at every stage of your business.
*  Shopify powers 10% of all e-commerce in the US and Shopify is the global force behind Allbirds,
*  Rothy's and Brooklyn and millions of other entrepreneurs of every size across 175 countries.
*  Whether you're selling security systems or marketing memory modules,
*  Shopify helps you sell everywhere from their all-in-one e-commerce platform to their in-person
*  POS system. Wherever and whatever you're selling, Shopify's got you covered.
*  I've used it in the past at the companies I've founded and when we launch merch here at Turpentine,
*  Shopify will be our go-to.
*  Shopify helps turn browsers into buyers with the internet's best converting checkout,
*  up to 36% better compared to other leading commerce platforms.
*  And Shopify helps you sell more with less effort thanks to Shopify Magic, your AI-powered all-star.
*  With Shopify Magic, whip up captivating content that converts from blog posts to product
*  descriptions. Generate instant FAQ answers. Pick the perfect email send time. Plus,
*  Shopify Magic is free for every Shopify seller. Businesses that grow, grow with Shopify.
*  Sign up for a $1 per month trial period at Shopify.com slash Cognitive.
*  Go to Shopify.com slash Cognitive now to grow your business no matter what stage you're in.
*  Shopify.com slash Cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki
*  so much that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Okay, so let's start with the classic autonomy stack. And this is very derivative of the
*  Jarpert-Wyrm Challenge, but of course it has become a thousand X in many dimensions and
*  elaborated. And so you start with your base is you start with a map. And the purpose of the map
*  is to tell you the rules of the road and kind of tell you the rules that other people are expected
*  to follow. And so when you identify another vehicle in the environment or another person
*  in the environment, you can use their position, place it on the map and take a guess as to where
*  it's going to go. And so you divide that then into two steps. One is your localization. Where
*  am I on the map? And you can use GPS, but the people who are really serious about it need really
*  real precision. Use the lidar to position themselves on the map. So what they've done
*  is they've gone and done a 3D scan of every single city or every single area they're going to drive
*  so they can measure the distances to surrounding buildings and trees and other artifacts to figure
*  out where they are to a high degree of precision. And that's ultimately once they can identify that
*  on the map, they can use the relative position of other actors in the scene and put them on the
*  map as well. And that would be in combination, the perception layer. Where am I? I take all the
*  facts of my map. Maybe I do some additional perception to double check that my map still
*  roughly corresponds to the environment. I look for other actors, like other mobile things that
*  maybe there may not be there. You have to then distinguish from like a parked car or a moving
*  car or part of a person or not part of a person. The second step of that perception is called
*  prediction, where you say, okay, I'm running my system, maybe at about 10 hertz. That's a pretty
*  normal condition. I'm going to take, you know, maybe up to a second, I have a pipeline where
*  I'm accumulating facts about how the world is evolving. So what I want to do, knowing that I'm
*  in a vehicle, I can't stop instantaneously. This is one of the things that really divides
*  robotics from other applications is I have momentum. So I have to make decisions now that
*  I can't reverse at a later time. So the first step in doing that is to predict where all of the
*  other actors are going to go. And I use their position, and I use past profiles. And often,
*  this was one of the first applications of machine learning in these stacks was, hey, I need to build
*  a model where when I see a car, I have a pretty good guess as to where it's going to go. And some
*  of that, the initial conditions for that are also encoded in the map. So if I've driven around,
*  I survey the same city a bunch of times to try and see how do people actually behave in that,
*  in that, in that zone. The next phase I go through is planning, where it's like, okay,
*  I have all these facts that have been expressed about how I want to move through world, like,
*  what is my goal? How is everyone else going to move? And now what I want to do is plot out a
*  path in world spaces to where I'm going to drive. And this has been, you know, huge subject of
*  research, because you can easily come to conclusions. And you see this still in the world,
*  where your conclusion is just to not move. Because when you think about what everyone could do,
*  it's like, yes, people could just suddenly change direction and drive into you. And then if you think
*  about, you know, probably what they will do, then if you start with simple assumptions, like people
*  just go the velocity they're going, you often will not find openings that you could otherwise
*  drive through. And so this sort of planning has a really complex interaction with prediction,
*  where you have to rerun all of your prediction to say, well, if I move in the scene in a certain way,
*  I expect a reaction in order to move the flow of traffic. And then once you run that, that's often
*  the subject of more AI, lots of dynamic programming, lots of search algorithms,
*  where I'm trying to plot all the possibilities and measure all the probabilities of what's going to
*  happen. And then controls are probably the most straightforward after that point, where I've
*  already laid out where I'm going to go. And now I just have to tell the vehicle where to go.
*  And when you're at relatively slow speed, that's actually a pretty easy problem. You don't have a
*  lot of dynamics to work with. And so the companies that implement like this is like Waymo is the,
*  originally Google self driving car is sort of the granddaddy. It's like they started their project
*  in like, I think it was 2011, they might have run an experiment, they're doing it, they started
*  scaling it up in 2013. I think, you know, cruises solidified themselves as a solid number two,
*  where they started in 2015, with basically the same stack, there are smaller companies that
*  have really, you know, come and gone where it was easy to get a demo up, but often they died there.
*  And then there's the trucking company. So it can be companies like Kodiak, the largest,
*  the most prominent one is Aurora. And the trucking problem is even more complex. One,
*  you have to drive on freeways, they tend to focus on being very, very good at prediction. So very,
*  very good at perception, often seeing hundreds of meters down the road, very good at prediction,
*  because the assumption is, is that the truck is a very, very high momentum device. You know, you
*  really do want to guess how the world's going to evolve over a number of seconds, and very good at
*  traffic dynamics. So in the whole other world, you have a company like Wave. So Wave, they probably
*  started about the same time we did. And they've always focused on throwing out that stack and
*  trying to build some sort of end to end system. And so instead of breaking it down into stages,
*  where you often have completely different teams working on those different stages,
*  and negotiating the interfaces and, and trying to set up performance standards at each point,
*  what they've been focusing on is, let's just make a supermodel, and just do it end to end. So we take,
*  you know, all of our sensors in, we throw it into the supermodel, and then we get a vector of where
*  I'm going to drive out. Tesla has been an interesting case, because you've seen them actually go through
*  multiple of these serially. And so when they started out with FSD, like their FSD beta,
*  they first tried to build a pretty naive solution without prediction. And then you can see them
*  changing this through their AI days, then they moved into actually building more of a classic
*  prediction model and more of a solver, and incorporating more models into that solving process.
*  And then they haven't done an AI down it, but in the, in the biography, and in some of Elon Musk's
*  leaks, you can see they've done another reboot, where they're moving more and more towards an end
*  to end model. There's there's sort of been these two evolutionary approaches. So one is,
*  they their robotics based companies are kind of slowly incorporating AI. If you go back and you
*  look at their presentations on how they use AI, a lot of it is concentrated in their simulation
*  and test environments where they're trying to create profiles and get very, very good at
*  predicting how other cars are going to react, and then rendering that environment back to the car.
*  And I think that they're slowly moving towards this idea that that should be the same system
*  that runs in the car. And then you have the the companies that are more radical, which is we want
*  to run everything in the car. And we don't want to contemplate these stages that were defined
*  decades ago, when you had very limited access to AI. So I'm kind of mentally mapping this into
*  sort of a 2d, like a two by two kind of grid where on the one hand, you have the access of
*  the hardware. And the seemingly the evolution is from super high although I guess there's still
*  an active competition, right? Because you see a cruise running around today, or at least until
*  recently did, I'm going to ask you a little bit about that too. But you see the things spinning
*  on the top of it. And that's like a very expensive and specialized piece of equipment. Other,
*  entrance into this space have like super advanced GPS, I understand, and super advanced, like
*  accelerometer type stuff. And then on the kind of cheaper, more scalable end is,
*  we're just going to use a bunch of cell phone cameras and let software do the hard part.
*  And then on the other axis, I guess, is like, on the one end, and this one is maybe more like
*  clearly a direction in time. But going back to the DARPA thing, I assume at that point, you had like,
*  very little AI, certainly nothing like what we would consider to be like the deep learning AI
*  we're familiar with today. But in that scenario, you just have to break this problem down into a
*  bazillion little pieces and have specialized software modules that deal with each one.
*  And obviously, it becomes a real challenge to manage that code base and to figure out
*  what to do in any number of situations. And you open yourself up to like a zillion edge cases.
*  And then you can start to kind of chip away at bits of that with AI over time and kind of replace
*  modules or kind of create stitched together modules with kind of an AI layer on top.
*  But then there's also this kind of big idea that, well, hey, what if we kind of through
*  most or all of that away and really embrace the bitter lesson and hope that it's sweet in this
*  case and that that could kind of deliver the sort of end to end thing and smooth over a lot of those
*  edge cases. How do I do there? Or how would you complicate that? I would simplify by saying,
*  ultimately, the question that people want to answer is how do I know it works well enough that I can
*  deploy this in public? And so I think I would take your two by two and say, there's two philosophies.
*  One is if all my parts work, does the system work? And often this is rooted in the automotive
*  practice of making safety cases where you say, hey, if there's a series of facts that I know is true,
*  therefore my product is safe. And then there's the measurement is the other axis where it says,
*  I don't know exactly how every part works. All I care is I'm not going to try and rationalize
*  why I believe it works. I'm just going to go to in the world and measure whether it works.
*  And these two to implement that correctly, you often have to end up in the more scalable domain.
*  And so that sort of drives what axes you can do. Because if you're a company like Aurora,
*  you can't drive a million trucks and just measure it. What you have the trucks you have.
*  And so you have to spend a lot of time trying to rationalize does this work or not,
*  based on whether the individual components work. And then if you're Tesla, which is like
*  the exact opposite end where they're driving around a million cars, their philosophy is,
*  we'll just measure like we'll put stuff out there. We'll get our trusted drivers, but we'll get
*  1000s of them. I think I don't know what the scale their program is. I think it's 1000s,
*  maybe low 10s of 1000s. But then we're just going to watch what actually happens
*  and get a statistical measure about how well it works and actually use that to identify where
*  the real problems are. This might be a good time to just run through the kind of levels of
*  autonomy as well and give folks kind of a sense of how in the industry people think about these
*  gradations. And then you can maybe kind of map on to those levels, like these different paradigms
*  as you go to. There's really a divide in the industry. So they're in theory five levels.
*  In practice, there's two sets of levels. And so level zero doesn't exist, or that's like a car
*  that was built in like the 40s. Level one is basically every car that was built before 2000.
*  In the consumer space, we're very much in this level two domain. And what I've considered the
*  difference between level two and other cars is that the car measures the environment, usually
*  through radars. Radars got big in the 2000s and now through cameras, which got big a decade later.
*  And the car can have a reaction to the environment that is independent of what the driver is doing.
*  So lots of features like adaptive cruise control was sort of the original level two feature.
*  Automatic emergency braking is a level two feature, all the way up to various forms of auto
*  steering is level two feature. And sometimes the industry calls this level two plus or plus plus
*  or plus plus plus to try and break that down. So the divide happens at level three and level four
*  and level five. So let's knock off level five, because it may never exist. So that's like some
*  fully autonomous car that somehow knows what you want and can handle any scenario. We're very much
*  talking about the level three and level four. Now there's a huge community that says level three
*  doesn't make any sense because you have a human monitoring it. And the car has to have a good
*  enough sense as to whether it can operate correctly, that it can tell a human observer
*  whether they should or should not pay attention at a given time. And so the first company to bring
*  out a level three product or market something as a level three product is Mercedes. There's actually
*  debate about whether it's a level three product or level two with a lot of pluses. BMW has announced
*  level three product. Acura in Japan has announced level three product. And the main difference in
*  consumer experience is that instead of being nagged to always watch the road or touch the
*  steering wheel to prove you're paying attention, the car can say, I've got it. And your your eyes
*  and your hands can do whatever they're going to do. Like you could read a book until it
*  things that your attempts to get your attention, at which point it turns back into a level two
*  vehicle. So Mercedes is application of this is a traffic jams. So it only works under 40 miles an
*  hour. You have to have all the lanes around you filled has to be mapped, you have to have compatible
*  weather when all of those conditions are true. The car will go into level three mode, and it will
*  creep along. And I think that the product that BMW has announced is quite similar. So level four,
*  the only companies that have claimed to be level four. So the main difference there is what's called
*  an MRC, a minimal risk condition. And so a level four car can doesn't have to handle every single
*  scenario. But when it when something is not being handled correctly, it has to resort to a minimal
*  risk condition, meaning that most of the time, it just means it stops like it stops in place.
*  That's the simplest minimal risk condition. In urban environments, that is mostly acceptable,
*  except when you stop somewhere that is disruptive to other people around you, which we've seen
*  in the news. But that's actually pretty good because it avoids certain types of liability
*  on a freeway because you can't just stop in place on a freeway, it would have to involve some form of
*  pulling over to the shoulder. And so for a car to go from level three to level four, what that means
*  is if there's a person in the car or otherwise responsible for the car, and the car may demand
*  attention of that person, but if that person never responds, this car will still go into its
*  minimal risk condition. And so that's the technical definition. Now colloquially, people often think
*  of level four as robotaxis, meaning that they're automated enough that there's never a driver,
*  I can get into the car. And the way that the regulators are going like NHTSA, for example,
*  is they're just trying to explain that divide is something assistive, meaning that you always have
*  to pay attention, there's no condition under which you're not driving the car. Or is it automated,
*  meaning there are conditions under which you don't have to look out the window if you don't want to,
*  you don't have to touch the steering wheel if you don't want to. And so everything marketed today
*  is assistive. The government and other agencies and companies are exploring how would you know
*  whether an automated system was good enough to market and call an automated system.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing. And of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8 and Databricks Mosaic, take a free test drive of OCI at oracle.com.
*  That's oracle.com slash cognitive, oracle.com slash cognitive.
*  If you're a startup founder or executive running a growing business, you know that as you scale,
*  your systems break down and the cracks start to show. If this resonates with you, there are three
*  numbers you need to know. 36,000, 25 and one. 36,000. That's the number of businesses which
*  have upgraded to NetSuite by Oracle. NetSuite is the number one cloud financial system,
*  streamlined accounting, financial management, inventory, HR and more. 25. NetSuite turns 25
*  this year. That's 25 years of helping businesses do more with less, close their books in days,
*  not weeks and drive down costs. One, because your business is one of a kind, so you get a
*  customized solution for all your KPIs in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts and improve margins. Everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist designed to give you consistently
*  excellent performance, absolutely free at NetSuite.com slash cognitive. That's NetSuite.com
*  slash cognitive to get your own KPI checklist. NetSuite.com slash cognitive.
*  I'm going to tell a little bit more about what the robo taxis are really like today. I think,
*  you know, very few people still obviously have like taken a ride in one recently. And unfortunately,
*  I'm living in Detroit. We don't have any robot taxis on the road here, even though we are the
*  auto capital historically. I was kind of surprised to learn in prepping for this just like how limited
*  the scope of operation still is for a robot taxi. The robot taxis are developing a new product. So
*  it makes sense to limit the scope until you know whether it works. And so what you saw in terms of
*  scope is they're not great at weather. There's a reason Waymo deployed to Arizona, because the
*  weather is like it's extremely dry. It's also really hot, meaning that there aren't many
*  pedestrians out. And so they're taking measures to to really limit their exposure. And early on,
*  cruise was only operating at night. I think Waymo also started out operating at night,
*  just to have like less traffic activity and less people working around. Every person I've talked
*  to that's been a robot taxi said it's actually pretty good. And like to the point where, you know,
*  kind of like an Uber probably even better than an Uber, you stop paying attention to it. Like you
*  watch it for a little bit, and it's kind of neat, and it shows you what it's seeing. But you quickly
*  relax and you're like, this thing isn't going to screw up too badly. And so it goes along. And so
*  in the domain that they're running them, and in the domain where they're where the public is taking
*  rides and in San Francisco, now Waymo is the only operator, they're geography limited, like it can't
*  be too steep. I think they're avoiding some of the most crowded areas or some of the most crowded
*  times of day. But the general impression that is that it works really well in those situations.
*  I think the other development that's been happening is people have been paying a lot
*  more attention to China. So China has a very vibrant both robot taxi and autonomous driving
*  consumer driving market. And so there, it's like people are also pretty comfortable with how those
*  products work. And they're, they're kind of in a hybrid state where a lot of it is robot taxi,
*  almost all the companies there started with the same architecture, they're moving into more consumer,
*  incorporating more cameras, smaller computers and such. But there, the impression is, is that the
*  automated driving is actually better than the average Chinese driver. So people feel pretty
*  comfortable about using it. And I think that that's both positive, but it's also perceived
*  as the biggest risk, which is that people quickly get complacent. And so if you had something that
*  worked 99% of the time, it's going to work 99% of the time. And if you're sitting there watching
*  it, you quickly stop watching it. And then all of a sudden, it'll do something weird, it'll get into
*  an edge case and do something weird, and you weren't expecting it. And so that's both, you know,
*  there's considered to be an uncanny valley in the robot taxi world, where as it gets closer and
*  closer to good enough or ready to ship, people will get more and more complacent, and you'll
*  actually see the rate of incidence increase. And that may be a little bit of what happened to cruise.
*  So I've not been in the robot taxis, as I said, but I have had an opportunity to take a pretty long
*  trip in a Tesla recently, a neighbor was kind enough to lend me theirs. And I took my grandmother
*  on a was an eight hour round trip for me to take her back from a visit to our place back to where
*  she lives. And, you know, it doesn't let you get too complacent. The nag system in the Tesla is like,
*  honestly, super aggressive. But I definitely could see that happening already in a Tesla too,
*  like I was very impressed overall by how well it worked. It seemed like to me to kind of
*  trust it, you know, I was I had to watch it closely. And I was also just watching it closely,
*  because I'm super fascinated by everything that's going on in AI. So I was kind of really trying to
*  sense like, how good is this thing? But I was super impressed. I mean, we had one incident in my
*  rides, you know, to your point about weather, where it was a summer day, and all of a sudden,
*  one of these kind of Midwest, you know, flash, intense thunderstorms came up and dumped on us
*  for a minute. And in that moment, it basically said, Hey, it's on you for the time being. So I
*  had to take over at that time. And there were a couple of other things where it did something a
*  little bit weird. But I certainly never felt unsafe. And I definitely would rather have it
*  driving me, you know, even if I were going to, you know, get into that uncanny valley and really
*  trust it as opposed to like many people I've been in the passenger seat with. It did feel,
*  you know, pretty solid. So I want to come back a little bit to the sort of policy and societal
*  stuff a little bit later. But I appreciate you kind of taking all this time to set the stage and
*  give us the taxonomy and the different approaches. Where is this ghost autonomy in this whole
*  landscape? You know, obviously, we've talked about your consumer cameras being one big part of the
*  bet. But I'd love to learn more about the architecture as it's developed. And as you see it
*  evolving, you can address that in any number of ways. One I always find really instructive is
*  just mapping inputs to outputs. You know, I think kind of for any AI system, like, what does it take
*  in? What does it take out? You know, maybe there's some intermediate, interpretable stages in between
*  as well. But I'd love to kind of, you know, from potentially multiple angles, but definitely
*  including that one, kind of understand the stack that you guys have built.
*  Yes, we're building on consumer cameras, but also more importantly, consumer chips. And we want to
*  make sure that there is no magic hardware in there. Because our assumption is like, you start from
*  cameras, and you start from chips. And what's nice is those just get better every year. And so
*  then it comes down to like, how are you going to solve some of the interesting problems of autonomy?
*  And so if you look at the consumer space, there's a lot of image recognition, does something look
*  like a car? Can you guess the distance? And one of the really, really powerful things about LIDAR
*  is that you get an actual measurement of distance. And so to solve that problem, we ended up building
*  a stereo system. And stereo systems have traditionally been built with custom chips. First,
*  there's actually quite a few companies out there that do that. And also they have a lot of difficult
*  calibration problems. So if you think about you have two cameras, your pixels are literally a
*  micron in size. If the system distorts by a micron, you're going to get it won't line up
*  anymore. And so what we spent time doing is we wanted real this measurements of distance, we
*  wanted to get sort of the very nice universal behavior that you get out of LIDAR. But we wanted
*  to build that on cameras. And that was one of our first AI problems to solve, which is how do you
*  just take two cameras, they're connected to a computer and develop real measurements of distance.
*  And so a lot of that was filling in what gaps does the lack of LIDAR leave behind. And so we
*  believe that provides a lot of the same safety that you get out of LIDAR system without having
*  to put reading hardware on there. And actually, it's a lot better because we can run that 30 frames
*  a second as opposed to 10. And it's much, much higher resolution. Like a LIDAR, a very expensive
*  LIDAR is like 64 lasers, that's 64 vertical lines. And we have a 12 megapixel camera. So we have
*  1000 vertical lines, like it's not even comparable. But the other thing is that we wanted to build
*  something that was very adaptive to the environment. And so what that meant is we wanted to jettison
*  a lot of the complex planning that goes on and a lot of the prediction. And so if you're driving
*  on a freeway, often you're trying to predict because you're slow at decision making. And so
*  we basically just ramped up the speed, we made it run about 10 times faster than most stacks.
*  And a lot of that was focusing on software that would make decisions very, very quickly
*  from pretty small amounts of information on where to go. And if you're wrong, you're only wrong by
*  about 30 milliseconds, which is traveling a meter down the freeway. But that became a core
*  assumption is let's make this fit into a consumer chip by getting rid of a lot of the compute. And
*  a lot of the compute is that complex prediction and planning framework. And so what we did is we
*  incorporated a much simpler planning framework where you can only see so many cars, there's only
*  so many lanes, you're on the freeway. And so as long as you can make decisions extremely rapidly,
*  you should not have to predict very far in the future. And if you're predicting a short time
*  into the future, because you can't read the minds of the other drivers, there's a limited number of
*  things they can do because they're in vehicles that have momentum. And so they can't change
*  their acceleration that much over very short periods of time, like hundreds of milliseconds.
*  That was sort of the core software philosophy of like, how do you get started to make something work
*  in a consumer platform without providing the same level of safety without having to implement a lot
*  of the complexity? Like, what I've been looking for, for the entire life of the company is you see,
*  you see a company like Waymo, it's like they have thousands of engineers, we have about 60.
*  How do you build something with a different philosophy that gets rid of your need for having
*  1000 engineers? And speed is like a huge part of that. The next thing is we build total symmetry
*  into the system. So everything is recorded is on the same hardware platform. And so the goal there
*  was again to fit into the consumer form factor, we didn't want to have survey like specialized
*  survey vehicles that slow down your mapping of the environment. So instead, everything is recorded
*  in the system in compressed video uploaded all the time. Obviously, in a real deployed system,
*  most video is highly interesting. So we would not upload it, we'd be more selective about what we
*  upload. But we had we force ourselves into a single stack, a single software stack that can provide
*  all the inputs for learning, and all of the execution and do that simultaneously,
*  so that we could shorten the time between going on a drive, discovering a problem, and actually
*  fixing it and then trying again. And in the end, we do multiple software releases a day in order
*  to test different combinations and different algorithms. You know, the story of the company
*  has just been making that better and better, so that you have a really, really good highway
*  experience. The other thing that we've incorporated from full self driving is that we don't ask a lot
*  of questions about how you want the car to drive. And so what you see in most cars out there today
*  is they actually literally ask you what speed you want to go and how far you want to follow.
*  And so what we do is we determine that from the environment. So we're looking at all the cars,
*  we're getting their profile on stereo camera, we're getting a profile on radar to estimate
*  all their velocities. And so we look at the total traffic pattern to actually just choose a speed
*  and choose a following distance so that you never have to adjust it. We spend time looking at
*  competitive consumer products and even Tesla, you do if you go through different types of traffic,
*  like you go from stop and go to like thick traffic to thin traffic, often you do make a lot of
*  adjustments. And so we're building the same sort of anticipation and the same sort of
*  self reconfiguration that you would have in a fully autonomous vehicle. And that sort of stuff
*  is actually pretty easy, but it takes work. But it's not very compute intensive. And it dramatically
*  improves the experience. Like it makes the car feel like it's floating in traffic as opposed to
*  something where you've done some settings and it's going to slavishly execute them.
*  I'm always kind of interested in how AI ends up being kind of alien intelligence to us.
*  And often like ends up doing things very differently. So I think it's really interesting
*  right off the bat to just look at this notion of like, okay, can we make the problem really small
*  by making the performance really good and then being able to increase the frequency?
*  That in and of itself, I think is a really fascinating approach because it's like,
*  you're kind of leaning into a superhuman aspect of computers, which is just obviously that they
*  run super fast. And if I understand correctly, then kind of saying like, well, knowing that
*  we're going to be back at this again, 30 milliseconds from now, we don't have to do
*  super high level stuff nearly as much because we're going to get another update really quick.
*  So if things start to go weird, then we can kind of react to it more quickly than versus like
*  having to anticipate it. Am I understanding that right? I think that that's true. I think the other
*  thing is when you talk about inputs and outputs, part of the reason that AI is alien is because
*  it's going through a filter of what do you think you need to train it on? And so, and this is where
*  a lot of edge cases come in is that people are not very good at guessing what are salient inputs to
*  any model. And so for any model that gets developed, it's like our stereo model was
*  pretty simple because the output is just a disparity between two cameras. And so you have
*  a lot of physical parameters for how the cameras could be moved relative to each other, how they
*  could distort relative to each other for things like what is the, where are the lanes? It's like,
*  where are people driving? There's a lot of factors in the environment that are just very hard to
*  guess. And so, you know, part of the reason to be fast is because guessing all the things that could
*  occur in the environment over a very short period of time is much easier than guessing what could
*  occur over a longer period of time. And so to some extent, we've adopted a bit of a barbell strategy.
*  It's like, well, for the models that we put in the car, we want to have a development loop
*  that allows us to quickly sort of guess and have a reasonable number of things that don't require
*  a, you know, much more than a single person's intuition for how you should formulate your
*  training sets. And then the other side of it is going all the way to LLMs that have incorporated
*  all human knowledge and, you know, almost all human texts and all human images so that you
*  don't have to guess what is salient in a scene. Like simple example, we found that you can be
*  pretty good at guessing where lanes are, but performance is degraded by the presence of trees.
*  It's like, okay, why is that? Like, and some of it was like the shadows and it depended on the
*  time of day and it depended on certain, you know, aspects of glare. But the model in some sense was
*  fairly dumb because it assumed a type of illumination on the road that can be disturbed
*  by things that are off the road. And so you're just constantly editing how you train the model
*  to incorporate all of this common sense for how does a real road actually appear? How does it
*  appear when it's in the middle of construction or how does it appear when there's been just a mess?
*  Like we found roads where they're literally white paint spills and it's like, okay, that's just
*  something that occurs. And how can you take all of the information in the scene and feed into a
*  model? And I think that that's kind of goes unsaid as a challenge of making any point model is it's
*  very hard to take the input and output and extract a subset that is different from the totality of
*  common sense that you could have around that input. You mentioned radar. So is radar also cheap?
*  I wouldn't have intuited that like that there would be, you know, kind of consumer affordable
*  radar systems, but maybe there are. Well, radar is put on like 30% of cars that are built. So it is
*  it is cheap. It's been deployed on cars for many decades and it's completely solid state. And so
*  as far as like something that is sort of a known thing that can be put on a car and it can be made
*  cheaper. And so it's outside of our usual profile where something that is built exclusively for the
*  auto industry probably won't be cheap in terms of its price, but it is still a well-known thing and
*  non-controversial to put a radar. It's already standard. So, so be it. Is there a kind of
*  intermediate, you know, just kind of piecing together how this this whole system works?
*  Like in the Tesla, there's the sort of, you know, eight cameras around, right? And then they
*  synthesize all that into a 3D rendering of the scene. And then I'm looking as I'm riding
*  along in it, I'm looking at that 3D rendering and then they're kind of layering the planning
*  on to the 3D scene. And I can kind of see all that as well. Do you also have a like a human
*  interpretable visualization layer or some sort of intermediate layer where I can like inspect how
*  it's understanding the world around it? Yes. So, so the models that run in the car in some ways
*  are pretty conventional. In other words, they tell you literally where the other car is in the scene
*  in the world coordinates, what is the configuration of the road and world coordinates. And so we do
*  take that information and we render it. And we do have a forward plan of where is the car going to
*  go? The car mostly kind of follows the lane. So it's it's the same lane, unless you're making a
*  lane change, at which point we draw the plan out for where the car is going to go. Because ultimately,
*  the output is a physical acceleration that has to be applied to the car. And we have to know what
*  that goal is. So we do project that a couple of seconds into the future, knowing that it's subject
*  to change if the facts in the world change. And we think that that's essential for anyone to trust
*  what the system is doing, is to have a rendering of the world that sort of exposes the a bit of
*  the thought process of the system that matches what people see when they put up when they look
*  out the window. That's another interesting part about moving more of the reasoning into LLMs,
*  because they think in terms of text. And so you can get more of a human readable reasoning.
*  And so there's a demonstration from from wave. But what they did was they trained a language model
*  to directly interpret their machine learn models for driving. And so think of it as, you know,
*  if the machine learn models are building a token space, you create that mapping into a language
*  model, so that you could ask the questions and answers about kind of what activations in the
*  model and can you describe those activations in terms of English. And I think that that's
*  becoming an increasingly important tool, because you can take a tool like TensorBoard, and an expert
*  can look at what activations are causing what decisions. But this is a pretty interesting new
*  tool that's enabled by open source, where you can train a language model to directly interpret the
*  activations with as long as you can create a body of text or a body of responses that you can train
*  that you can fine tune from. Yeah, it's amazing how many interpretability breakthroughs are kind
*  of happening right now. And also, I'm constantly fascinated by how bridgeable different latent
*  spaces are one to the other. And so yeah, I guess this is probably a good time to, you know, kind
*  of get back to the big news. So like what, you know, obviously, there's a lot of hard parts to
*  this. But what is the kind of frontier that has proven extremely difficult, such that you were
*  like, Okay, I want to go use, you know, this more generalist kind of allegedly world model having
*  system to help get over some of these humps. And how do you see that playing out now that
*  you have this partnership underway with open AI? We've been looking a long time at how to do urban
*  driving. And the problem is, is that everyone who's tried to do urban driving, they basically
*  spent a decade banging their head against the wall. And maybe another decade, it'll work. But
*  the main thing we saw is that they're incrementally incorporating a lot of common sense into their
*  system. And that's just called edge cases. So the industry talks about edge cases, when the system
*  behaves incorrectly, based on information that was in the scene, but wasn't correctly incorporated
*  into the drive planning. And so that's, that's a wicked problem. It's like the right now the
*  only development path to solve that is to just do a lot of driving and continue to make your planning
*  algorithm more and more complex, like you can add signals and add more recognizers. So when we saw
*  the original GBT-4 release, the first thought was, hey, we could really use this for labeling,
*  like for our planning to come up with different reasons that scenes happen to be different
*  without creating special purpose recognize. So when I mentioned that, hey, trees kind of matter,
*  well, that's a question that can easily answer. Is there a tree in the scene? Is there a bridge
*  in the scene? And we don't have to train a model to recognize that or build, say, a complex cross
*  reference with someone else's database. But then what became more interesting as we experimented
*  with it realized it has a lot of common sense about driving. And so GBT-4 and GBT-B, if you start just
*  asking questions in text about describing scenarios and saying, what should I do? And you started
*  getting pretty sensible answers. And there's been, you know, a couple good papers of people making
*  these textual virtual worlds where they describe how traffic is behaving in text. And then they get
*  answers about how the car should behave. And so they do these sorts of agent-like simulations
*  to make that work. But what was really interesting is, you know, that alone doesn't solve the problem
*  of what are the salient features in the scene that could lead to a decision. And so we then
*  started experimenting with the open source multimodal models. And we want to answer a simple
*  question, which is, first, am I on a freeway? And it's like, you think it's an easy question,
*  but it's not as straightforward as you think to answer from a map. Because GPS has a lot of
*  unreliability. It especially has unreliability around on-ramps and off-ramps. So knowing precisely
*  that you're on a freeway versus not on a freeway versus something else is something that would be
*  really good to know precisely, especially from the visual field. And there's other facts that you
*  could ask. And starting with, you know, I believe we started with lava and T5, you know, it would
*  get it right about 60% of the time. But with fine tuning, that actually went to about 98% of the time.
*  And that fine tuning set was probably a few hundred examples of showing a different street
*  scenes and then defining a bit more about what we meant by freeways. And so putting this together,
*  we came to the conclusion that there was a totally viable path instead of training a bunch of special
*  purpose recognizers that you would just go to GPTV and ask what the car should do. And that opens up
*  a very interesting world because you express your navigation goals, maybe use a rag or something to
*  find relevant traffic laws. But then you literally just show it the images of what's around you.
*  You augment those images with things that you can measure directly from your sensors,
*  like perhaps you put boxes around cars, you tell it what lanes you're referring to. And even we
*  found complex environments like construction scenes, there's a flagman, there's like,
*  when you ask it how you should respond to that scene, you get a pretty sensible answer.
*  And so what this does is it divides up the autonomous driving problem.
*  Instead of being a monolithic system that every hundred milliseconds has to examine the entire
*  world, build predictions for the entire world, and then issue a command to the car, you divide
*  up into two systems where you say, Hey, there's a high speed system in the car that's running at
*  30 hertz. It does all the safety things that prevents collisions, it kind of knows what
*  path it's following in terms of lanes. And then you have a much slower system that has been trained
*  on the entire universe, has a lot of common sense built into it, and can instruct the car what to do
*  kind of at a maneuver level. And so in this way, the car becomes an API that is instructed in terms
*  of its maneuvers from an LLM that is examining the same sensory data. And to me, this represents a
*  huge reboot of how autonomous systems are built. To solve the analogy of that problem,
*  if I want to add a signal, like I see that there's something important to see, I'm driving around,
*  I notice I have edge cases, I discover that there's some particular sign or some particular
*  artifact in the environment that should have been incorporated in my decision, I would then have to
*  go to build a training set, you know, learn when I see that learn when it's relevant in terms of
*  its scene position. And then I have to edit my planning algorithm to sometimes incorporate
*  that data and sometimes not incorporate that data. And aside from being slow, it's kind of like,
*  you're just going to do that forever. And so the inversion is to say, let's try it on absolutely
*  everything, you tend to get sensible answers. And you can ask him to explain the answers and
*  explains the answers in terms of, you know, visual elements of the scene. And you're going to make a
*  system that out of the box is dramatically more reliable. It's amazing how well these visual
*  things work. I just took my kids to Salem, Massachusetts the other day and tried it in
*  chat GPT and took a picture of this like, parking sign that had been like taped to a lamppost.
*  And it said, you know, special temporary October parking, you know, Salem PD or whatever, there's
*  like two, you know, stripes of tape through it and a couple different, you know, the sign was itself
*  was like up there a couple times. And I asked it to infer the context just from that image.
*  And it was like, well, you know, first, it just reads the sign. And then it's like, Salem is known
*  as the home of the Salem witch trials. And it's a big, you know, tourist destination in October. So
*  in all likelihood, this refers to the fact that there's like elevated traffic here in October.
*  And so these like temporary parking rules apply just for this time of the year and,
*  you know, blah, blah, blah, blah. And it really is kind of striking to see how
*  much value, you know, the whole kind of world model and historical, you know, in this case,
*  like historical context can add to, you know, just a snapshot, right? I mean, it's, this is like well
*  above, you know, sort of a, what a caption, you know, might be able to do or an image segmentation
*  type of thing. It is pretty incredible. And that's what people call hallucination.
*  But hallucination is actually the best part of these models because the hallucination is where
*  all the common sense applies. And so when you're asking to incorporate not just all the knowledge
*  of the scene, but all sorts of, you know, the entire depth of knowledge that could be applied,
*  you tend to get more answers that are closer to reality than what an engineer sort of sitting
*  there having to express their thoughts in a programming language would be able to express.
*  So how does this then come to you kind of mentioned the two parts, right? Of how this
*  comes together into a new architecture. It's funny. I mean, I'm not a big analogy guy. I
*  typically resist analogies to the way humans work for AI systems. Because again, I think it's more
*  alien than human-like in many cases. I often say human level, but not human-like when I describe
*  GPT-4. But it is striking that there's kind of a system one, system two, you know, thinking
*  fast and slow kind of dynamic emerging here. How does the map fit into that? Is the map like
*  just another input into the GPT-4V? Is that how you imagine that working? And then, you know,
*  I'm sure there's a lot of logistical issues too around like, I would imagine you're not getting
*  the weights. So I imagine, you know, that you're still making API calls, which creates like,
*  you know, latency and availability concerns. So, you know, this brings a lot to the table in terms
*  of advanced understanding, but I'm sure it also brings some challenges. What's that whole picture
*  look like right now? So it's interesting to ask about the map because we still do incorporate maps.
*  And we do it in two ways. One is you license map data that's interesting and can tell you facts.
*  And when you think about constructing a prompt, you should include that information in the prompt
*  because why not? It's free context. You can also think of the map as just an extended memory. It's
*  like when you're driving around, if we're in analogies, it's like you don't go frame to frame.
*  You have a memory of what this road connects to and how you should behave on it. I think
*  the map is a good storage for that. The other thing is that we use the map as a key to store
*  media data. So if a road has been driven, we have images of that road from the car that drove it.
*  We have the inferences that were made from those images. And so for pictures in the environment,
*  one, it would be nice not to call GBTV because you pay for every single call for facts that are not
*  changed. And so you can extend your memory and rebuild your memory as you drive down the road.
*  And then the other thing is not every picture is perfect. Maybe this time there's a windshield
*  wiper in the middle of the picture. You're probably better off using a previously stored
*  picture than whatever you're sending. You will get some answers, but try and get the best answers
*  that you can. And so I think that maps are part of an extended memory system of what are all the
*  fixtures in the world and how do they connect? And when we're doing navigation, there's lots of
*  APIs that do navigation. So we just want to convert the turn-by-turn instructions into specific
*  maneuvers that are relevant to this scene. But then I guess the other part of the memory is
*  if you're driving along the road, you see a sign or you see a fact, and then you have to retain
*  that for a period of time, just like a person would retain that for a period of time. Because
*  often a big use of maps in autonomous vehicles is predicting the future, like predicting how the road
*  is going to evolve by just reading forward. Well, the way we do it is we have a sign that tells us
*  how the road is going to evolve in the future. And so to take advantage of that, we want to go
*  from the picture, the observations we make in that picture, we then want to retain that for a period
*  of time. We ideally retaining it just as text that is opaque to the program, but of course,
*  interpretable by the language model. And then you're returning that back into your prompts over and
*  over again. So in that sense, it's more like an agent model where you're updating a memory, like
*  you have a long-term memory that's your map, and then you have a short-term memory that is observations
*  that will expire as I travel along the road. And then logistical issues, it's like, well, the number
*  one issue is that GPTV is slow. You know, you make a call, it can take 10 seconds, it can take 30
*  seconds. But I'm extremely optimistic that those types of problems are solvable. So one is, yeah,
*  we should put it on our own computers. We have an application that demands a real-time response. And
*  so we have to come up with a mechanism to manage the compute capacity to make that work. But then
*  the other is, I'm expecting that as well as getting better, the models will just get much faster over
*  time. I mean, we saw GBT-35 got 10x faster. What we see in the GBTV, in the alpha edition, it's like,
*  I'm betting they were just trying to make it work. And there's certainly in the open source community,
*  a ton of research on different ways that you can make models faster. And I'm expecting OpenAIA has
*  not yet incorporated all of that. So I expect the models get faster, sort of 10x year over year,
*  proportionately cheaper to call. We would love to just call the model more and more and more,
*  and just ask more and more questions. And it'll just get more efficient to run. So when we think
*  about designing a product, you're on an auto company timeline, they want to make five years
*  plans. What's the world going to be like in five years? I don't know. You don't know. Like, five
*  years ago, you would not have guessed the world of today. But what we do know is that the models
*  will get dramatic, like, Moore's law will keep going on. But there'll be one axis of improvement,
*  the software will improve, the model design will improve. And so everything will end up like 100
*  to 1000 times faster and cheaper over that time period. And so that's what you want to aim for is,
*  let's assume we want to maximally call the largest model we can to solve problems as a default.
*  And then when we're forced to from an architecture point of view, to solve something,
*  if that's the model, for example, we're not going to embed this in a car, like we would embed much
*  simpler models, or there are certain questions that we need answered very, very quickly. Or there are
*  certain questions that we think are extraordinarily simple to answer. If you're driving along on a
*  country road and there's nothing around you, I'd rather have a model tell me there's nothing around,
*  rather than go to call it the most expensive model in the world to answer an obvious question.
*  And so there's a lot of optimization to make that work. But I think that problem gets easier over
*  time. And the goal is always to make sure that you're enabling calling a really expensive model
*  when you need to. Just to develop my intuition for the architecture a little bit more. So I sit down
*  in the ghost autonomy powered. And your business strategy here is to partner in, as you just
*  mentioned briefly, to partner into the car makers and become the kind of... I imagine it's like,
*  you need an answer to Tesla FSD, whether it's GM, Ford, whatever. We propose will be that answer
*  for you. So now I sit down in one of these cars in the future when this is all
*  kind of developed. And I basically say, okay, I want to go to this address. Obviously, we've
*  already got mapping applications that can kind of plan out the high level route in terms of a line
*  on a map at a great remove. And then the kind of second by second, or it ultimately has to be kind
*  of sub second decision making, right? Of like, what should I do now? The vision there is to
*  take advantage of all these trends and also develop your own optimizations so that you can
*  basically say, here's my high level goal. Here's where I'm at on the map. Here's what I see out the
*  window in front of me. What should I do now? And then the language model, I guess maybe has both a
*  reasoning and a maybe executable output. This is how I would do this if I was doing an
*  agent today. I would have a chain of thought and it would say,
*  well, I see that it's open road in front of you, or I see that there is a car in front of you and
*  to the right. So therefore, I think what we need to do is slow down and then get over behind it or
*  whatever. And then maybe also that gets expressed as code, like tap the brake and then in one second,
*  move over to the right or whatever. And then all that stuff gets fed down. You mentioned car as API
*  below, right? So that's kind of where I'm getting that from. And then on the car is where that stuff
*  gets executed and is also subject to any number of safety overrides, right? Where it's like, hey,
*  you told me to go right, but I'm sensing something right. So therefore, I don't do that.
*  And instead, I've sent some alarm back up that's like, can't execute the command because here's why.
*  How am I do it? I'm kind of mapping out that loop.
*  That is the main loop. But I also think it's continuous. And so you can think about the
*  user's intention at multiple levels. So one, the product as it works today is,
*  if you're driving the car, meaning you're sort of giving an input, it's a 100% conventional car.
*  Like a car just does what you tell you, doesn't fight you. If you let go, it kind of has a default
*  plan, which is keep following the road. And so we can think about it's like the car is just
*  autonomous. If you're not participating in it, now we can look in interior cameras. I think there's
*  a lot of clues for determining what does the person intend in this moment. And you can say
*  how autonomous should the car be? Then you can think about, okay, what if I just give the car
*  an instruction? I just say, take the next left. That's now, I can just inject a turn by turn.
*  And then there's the sort of point to point, which is, okay, you go to a mapping API, you
*  get your set of turn by turn directions, and that's fed down to the next level.
*  And so I think you can do all of these things. And I think that the chance are you would proceed
*  through those stages, because you just sort of get going. And, and then when you think about it's
*  like, I have to look up an address, like there's data entry, I want the car to be driving itself
*  already during that phase. And then I just want to edit what its intentions are. But yes, then the
*  cars and API and you can be expansive about how you think about the car as the API. There's no
*  reason that anything that is digitally accessible can't be also controlled by an agent using the
*  total information from inside and outside the car. So do I basically just sit down and kind of chat
*  with this like much like I can kind of chat with my chat GPT app, it's ultimately like a conversational
*  interface even what we're putting together is the car should tell you like why it's doing what it's
*  doing in plain language. I think that one of the ways that cars have gotten worse is that they've
*  become more opaque in terms of options and in terms of indications. And if you've rented a car
*  that has like a bunch of features on it, it will like beep at you and show you some symbol you've
*  never seen and you don't know why it's beeping at you. And it has this very, very narrow communication
*  path that doesn't actually incorporate information doesn't incorporate what you're doing. And I think
*  that the first simplification, which is let's put screens in cars, like that was a start in that it
*  started getting rid of lots and lots of sort of secondary miscellaneous buttons. But it's still
*  unsatisfying because there's still like deep menus and the car just seems like harder to use because
*  you don't have everything clearly labeled. The discover ability has gone way down. And so I think
*  the next evolution is like, yeah, you should just chat with your car and tell it what you want.
*  And that opens up the that experience to be one a lot more contextual. It doesn't have to be dumb,
*  like the car knows where you are, like it has the full context of your scene. And so you can just
*  refer to things in your scene or just it knows if you're in a gas station or it knows if you're in
*  a charging port, it knows if you're on an unpaved road, it knows like, and you can make the experience
*  just so much smarter by eliminating both all the buttons and eliminating all the menus.
*  Yeah, this is my I think this is going to happen for software across the board, you know, and even
*  just something like Gmail, you know, you get into the settings page and it's like, good God,
*  good luck, you know, and Salesforce, you know, and like the Adobe Creative Suite and just all
*  of these things have just gotten so bloated as they've kind of built out every feature that
*  a power user could possibly want. And at the end of that, it's like, you know, very inaccessible
*  to anybody who's not, you know, already been using the tool for years. I see this kind of as a wave
*  that's coming to sort of all of our software interactions and, you know, cars, we don't
*  always think of it as software, but increasingly, you know, that's a huge part of what they are
*  as well. It is going to be quite an evolution over the next few years, I think.
*  Well, I think and you talk about something like Gmail, it's like the first thing I thought of
*  was, well, the difference with a car is like the car has lots of external sensors, so it has lots
*  of context that it can use to do what you're doing. The thing I wonder is this also applies
*  to basically every AR application. It's like, where am I right now? Like basic questions about
*  where am I? What have you observed me doing as essential context for the total interface
*  so that I don't have to be exceedingly explicit about what I'm asking for.
*  In this context of this partnership and your overall strategy, is OpenAI the only game in
*  town here or, you know, should we expect to see like a Google and an Anthropic or a Microsoft,
*  come out with their own things and maybe start developing? We kind of see this in general,
*  right? Of this kind of big tech, you know, foundation model partnering into different
*  verticals. How do you think that shapes up over the next couple of years?
*  So today, OpenAI is the only game in town. If the criteria is an advanced multimodal model
*  that you have an API for that you can call today, yes, it is the only game in town.
*  And, you know, Google has made a lot of promises about Gemini, but then they don't ship it or they
*  delay shipping it. Anthropic, I don't know what their multimodal plans are. I think everyone
*  has to go down that path. Maybe there's probably a lot of business available to be exploited in
*  terms of documents because corporations exchange documents. I think that the enterprise market
*  will be extremely happy to absorb lots and lots more text processing in terms of
*  enhancing or automating white collar work. But I think the consumer space
*  very much depends on multimodal models, because the experiences people want is you have,
*  essentially you have a phone and maybe you have glasses in the future, but what they want is not
*  documents. You can only enter so much text on a mobile keyboard. And so the way those interfaces
*  go is you have to have less and less text and more and more context and more and more video and more
*  and more media in order to make the next generation of consumer apps. And so I see what we're doing as
*  an extension of that or a subset of anything related to robotics that has to understand the
*  environment, anything related to AR. And I think that multimodal is ultimately the future. And I'm
*  surprised I haven't seen more from Google or more from the others. I think they're very much going
*  after the enterprise market, which has been very, very good to OpenAO and other companies. And
*  there's a lot of interesting work. But I think the consumer market wants multimodal.
*  Love to hear a little bit about how you see the self-driving technology wave in relation to society.
*  I'm... Listeners of my podcast will know that I'm very naturally both a big AI enthusiast and
*  love building applications with it, love using CHPT. I don't really code anymore. I ask GPT-4
*  to code for me. At the same time, I definitely have what I would call a healthy respect,
*  fear of just what might be coming over the next few years, because it does seem like we're into
*  some pretty uncharted territory. But when it comes to self-driving, I clearly come down with the
*  accelerationists who are like, man, this is already a dangerous activity. And it seems like
*  we have some pretty good systems already starting to take shape. If you believe the statistics from
*  a cruise or from a Tesla, and I'd be interested to hear if you think these are for any reason
*  not credible, but it seems like the data suggests that they're already on par or better in terms of
*  safety, at least in the domains where they operate. And yet, we're so sluggish about it.
*  And we have these seemingly lack of enthusiasm among many possible consumers and a lot of
*  heavy-handed overreaction type stuff from regulators. What's your take on why we're not
*  more excited about this? It just seems kind of crazy to me, to be honest.
*  So what we see with consumers is that most consumers have not experienced any form of
*  self-driving. And so when they're asked their opinion, they're doing it kind of in a vacuum.
*  It's like, yeah, I heard this thing in the media. It's like I've heard about it for a while. And
*  it's not very personal to them. When they've experienced self-driving, they actually become
*  pretty bullish on it. As we talked about earlier, it does work. And it works well enough. And in
*  urban environments where you're driving pretty slow, the consequences, the ability to stop,
*  really mitigates a lot of practical issues. I think regulators are a very unusual space because
*  regulators aren't magic. When you really get down to the nuts and bolts of like,
*  well, what regulation should we actually write? No one actually knows because you don't have an
*  existence proof. And so in the automotive space, traditionally, regulations are only written.
*  And usually they're performance-based regulations. They don't tell you how to build it, but they
*  tell you what is sort of the minimum ratcheting standard years or even a decade after a product
*  is released. So any car today that has, say, auto steering, there is no governing regulation for that.
*  And I think that that's the right way to go because I don't think anyone's really nailed it.
*  There's no formula that says that one of them is sort of a lot better than the others. And five
*  years ago, I would have said Tesla is dramatically better than everyone else, but sort of traditional
*  autopilot, I think they're pretty similar. It's like you get in a 2020s car from almost any
*  manufacturer and you can debate the style at which it performs, but the performance is kind of in line.
*  This is also what motivated us to go to consumers is because the adoption of autonomous technology
*  would not be driven through robotaxis just because so few people experience taxis
*  that there would never be sort of a groundswell that people really want it because there would
*  just be this thing over there. There's no personal upside to them. Maybe there's some downside because
*  there's some bad news. And so that's kind of how they form their opinion. So our belief is that
*  you have to create great experiences for people that lots of people can feel personal about.
*  Now, when you talked about Tesla isn't there yet. And when you talked about your experience driving
*  with Tesla autopilot, what we see is that people bifurcate in how they react to the limitations of
*  autopilot. You have one population that gets really, really good at predicting when it's
*  going to work and when it's not going to work. Like they go down to the, I know it doesn't do
*  well on this exact turn or I know it doesn't do well in this exact weather, this exact bridge or
*  this, you know, this sort of traffic condition. And they get good at kind of almost unconsciously,
*  like activating and deactivating as they go on a trip. And it's still, you know, very good product
*  because it's active like 90 plus percent of the time, and they learn to manage it. The other
*  population just gets scared and never uses it ever again. And so they haven't worked out yet
*  how to onboard people in a way that teaches them limitations. I think that to make it good,
*  there's a there's always a part of the consumer population. It's like it's the classic technology
*  adoption curve, where the product really has to be perfect before the majority of people will adopt
*  it. And so, and I think that's reflected in sort of the truth of where consumer products are,
*  in that they don't work 100% of the time, they're not perfect. And, and I think that people react
*  to that more than anything else. So how do you think companies should, in the meantime, kind of
*  deal with this? I mean, we're talking, you know, just a number of days after this, you know,
*  there are, I guess it was maybe more like a month since the original incident where there was a,
*  an incident with a cruise that basically got into an accident, originally not its fault,
*  as I understand the situation, but then it kind of made a pretty big mistake and like dragged a
*  woman under the car for 20 feet or something, and she was hurt. And so that's obviously a really bad
*  incident. But I was kind of surprised that like then, you know, they ended up voluntarily shutting
*  down the fleet in other places. I mean, the California regulator, which seems a little heavy
*  handed to me, required them to shut down, but then they voluntarily shut down the rest of their
*  fleet nationwide. And I was kind of like, you know, where is our inner Travis here? Like, do we have
*  no willingness to like fight for our life's work in this space? Like, why is nobody kind of standing
*  up and saying, Hey, we are already safer. And, you know, yes, it's a terrible incident. We'll like
*  do everything we can to make it better. But, you know, we're not going to shut down because of this.
*  Are you guys crazy? Like, we're already safer. This is a dangerous activity. We're making it safer.
*  Am I wrong headed for thinking that like somebody kind of needs to stand up for the technology?
*  They definitely need to stand up for the technology. I think that, you know, Cruz's situation
*  was very much a government relations screw up at every level. And I think they're trying to figure
*  out how they screwed up so badly, which should have been the kind of incident that they could,
*  you know, explain in public that they could explain to the regulators. It was an unusual
*  thing. Like this isn't going to happen like every day. They completely screwed up their media and
*  their government relations. And so GM, their, you know, their parent corporation and by far
*  biggest funder is probably pretty upset about that. So I don't know what's going to happen
*  with Cruz. I think that that's a problem that they can solve. And they'll come up with some way
*  where one they fix the communication problem, and then they'll have to come up with some
*  engineering problem they fix. And so if you look at what happened was the cards like it was in
*  collision, you know, maybe not their fault, you know, women was tossed, and then it executed an
*  MRC. And so instead of just staying where it was after something unusual happened, it decided that
*  I'm going to pull over to get out of flow of traffic. Now, Cruz has had a lot of negative
*  press in the past about stopping in place and like blocking emergency vehicles or like stopping in
*  place in like really opportune time in opportune places. And so I think what's indicated is like
*  these sort of end states are extraordinarily difficult problems to solve. When you have to
*  try and program a solution when you'd have to try and predict everything that's going to happen
*  ahead of time. And so I think they have to come up with some solution that has a lot more common
*  sense about how they actually like what is an MRC in a given complex scenario. I don't know if that's
*  solvable with a conventional program. But to get those like they have to fight for it. It's like,
*  it's that or shut down. Like I think they really do have a binary choice of we're going to try and,
*  you know, reactivate as many jurisdictions as possible, we're going to, you know, go on our
*  campaign. Or like, you're going to have to just shut it down, which both are hard decisions for
*  them to make. Yeah, well, shutting it down doesn't seem like, you know, it seems almost impossible to
*  imagine from my perspective. Anyway, we've got the AI safety summit happening over in the UK.
*  And we've got a lot of discussion of like, you know, can we trust China at all? Or, you know,
*  is it going to be total AI arms race vis-a-vis China? You mentioned earlier that there's been
*  a lot of progress in autonomy in China. I wonder if there's anything we could do to sort of create
*  some friendly rivalry between, you know, the US or the West and China when it comes to some of these
*  mundane but very big quality of life improvements like the introduction of
*  self-driving cars. It feels to me like if we had some mojo, we'd be like, what can we do to really
*  make this thing work? We're not going to let China get to self-driving cars and enjoy that incredible
*  luxury before we do. You know, we're going to go trim the trees that are blocking the road. And
*  we're going to like, you know, make sure there aren't any of these like white paint spills that
*  are kind of confusing. And we're going to like, I don't know, put QR codes on all the road signs
*  so we can like, you know, more easily locate where we are and just, you know, there's so many things
*  that we could do right now. We're kind of like, we're not going to change the environment at all.
*  We're not going to make anything easier. I'm just going to make this and we're going to insist that
*  you'd be at least 10 times safer than a human driver and, you know, come back when you've worked
*  it all out. And I guess I wonder, like, you know, did you think about that at all? Any sort of like,
*  is there any way for us to kind of create a narrative of, you know, let's go win this?
*  And is there any other things that you would think of that we could do as a society to kind of try to
*  actually make this something that, you know, where there's kind of a natural momentum toward it,
*  as opposed to just being like, well, hey, you know, we don't care. We're not ready to listen to you
*  until you've solved it all. The Chinese situation is interesting because they have like specific
*  social forces that are pushing them down this path. So one is they're adding 20 million new
*  first generation drivers onto the roads every year. So like, let's imagine we were adding like
*  20 million effectively teenagers onto the road and, you know, in a number of years,
*  they'll get better, but that's actually happening. And so they're very, very concerned about
*  our road desk going to spike in a way that causes, you know, unrest or slows down development.
*  Because, you know, if they're bulldozing, whatever they're going to bulldoze to build that,
*  they're also much further down the path of electric cars. You know, there's only two companies that
*  are producing millions of electric cars. Tesla is one of them. BYD is the other one, which is a
*  Chinese company. No one else counts. Like you can add up all the rest. It doesn't count for anything.
*  So what I'm seeing in the US is a sort of halting rivalry on the area of EVs. So when you talk to
*  auto companies, they are absolutely consumed with EVs. And like, how are we going to build it? Like,
*  where's like all the way down to where the minerals coming from? You know, I have to retool all my
*  factories, retrain all my workers, I have to retrain my designers. I have all these mechanical
*  engineers that maybe I don't need anymore. How am I going to get this into like out of sedans into
*  like my best selling trucks and my best selling like SUVs? They're absolutely consumed. Whenever
*  you go to any automotive conference, it is like 1% AV and like 99% EV. It'll come. It's just that
*  the industry doesn't care about that yet. Because what they think is like they're going to get killed
*  on the straight up EV front without first considering other transformations they should
*  be incorporating. Regulators in the US are responsive to consumers. And so I think you
*  have to go and you have to make a case to consumers first to say this is why you want this technology.
*  And then it can become an issue that that percolates up through through Congress and
*  through the agencies as something that's worth prioritizing. A lot of that is like what could
*  you have? Right now, people don't see what's going on in China. So it's just not in their mind right
*  now. I think we're a few years away from having that technology race. Yeah, I must imagine you
*  might need to just kind of go town to town across America offering free first rides to
*  build the enthusiasm. Let's look again, the sort of VC subsidization of the early part of the
*  adoption curve to then create that demand. Yeah, I was really hoping like Waymo would do that.
*  I want them to go and more people go to Waymo or go on a cruise and just experience it and then kind
*  of ask it's like, can I have this for me? They've been, you know, slow with their expansion for,
*  you know, a bunch of reasons. But I'm really happy that the robotaxi companies to the extent that
*  there's not a Travis there who's pushing them, they still are like expanding their domain,
*  expanding their customer base, you know, giving people free rides, you know, working the press.
*  And I think all of that is important to build that like an actual consumer groundswell and say,
*  we really need this. Yeah, well, sign me up anytime you need somebody to help write a congressman or
*  whatever, you know, zooming out even beyond the autonomy realm. What's your outlook on the,
*  you know, the AI revolution from kind of the widest angle lens?
*  I think AI is basically retooling everything we know about computer science. Like we basically
*  need a whole new generation. And our bottleneck for putting AI absolutely everywhere is just there
*  aren't enough people who actually understand it. And the other thing that makes me really excited
*  about the generative AI is all of a sudden you've opened it up to like a much, much wider audience
*  where people can directly touch an AI system and get a response out of it without having to
*  write a bunch of Python. I think the amount of creativity that's going to unlock, we don't even
*  know the limits. And right now to get good results, you still have to be pretty good. Like you have
*  to be the kind of person who's willing to write a lot of different prompts and like really think
*  hard about that. As the models get better, they'll become less and less important. And furthermore,
*  it's like there should be multiple models where, you know, eventually Google will ship Gemini,
*  it will happen, you will get like new versions of code. Like, it's going to happen. As that occurs,
*  these models will actually converge in their functionality. Just like we CPUs have converged
*  with their functionality over a long period of time. And I think that once that happens,
*  you basically have this new computer where generative AI kind of mediates all the APIs
*  and all the people. And it kind of doesn't matter because the totality of human knowledge
*  and the super intelligence around that becomes itself a commodity that everyone can have access
*  to that there's an enormous amount of competition on. And so that's a pretty exciting future because
*  a lot of our deployment of computers has been limited to the number of people who can program
*  a computer in a meaningful way. And we saw like the last decade, there's this idea, hey, we're
*  going to do no code. Well, now we have real no code. So let's actually see what happens because
*  there's a real ability to say what you want in ordinary language and have a computer do something
*  that was previously unaccessible. Cool. Well, this has been a ton of fun. John Hayes,
*  founder and CEO of Ghost Autonomy. I can't wait to ride in one myself. For now, thank you for being
*  part of the cognitive revolution. It is both energizing and enlightening to hear why people
*  listen and learn what they value about the show. So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media platform of your choice.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.

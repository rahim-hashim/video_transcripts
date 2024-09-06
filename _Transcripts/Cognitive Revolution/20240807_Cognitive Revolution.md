---
Date Generated: September 06, 2024
Transcription Model: whisper medium 20231117
Length: 6608s
Video Keywords: []
Video Views: 2077
Video Rating: None
Video Description: Nathan explores the cutting-edge world of autonomous vehicles with industry expert Timothy B. Lee. In this episode of The Cognitive Revolution, we delve into the current state of self-driving technology, comparing industry leaders like Waymo and Tesla. Join us for an in-depth discussion on technical challenges, safety statistics, regulatory landscapes, and the potential future of transportation.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj


RECOMMENDED PODCAST: Second Opinion
A new podcast for health-tech insiders from Christina Farr of the Second Opinion newsletter. Join Christina Farr, Luba Greenwood, and Ash Zenooz every week as they challenge industry experts with tough questions about the best bets in health-tech.
Apple Podcasts: https://podcasts.apple.com/us/podcast/id1759267211
Spotify: https://open.spotify.com/show/0A8NwQE976s32zdBbZw6bv


SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:00:22) About the Episode
(00:03:01) Introduction and Guest Welcome
(00:03:48) SAE Levels of Self-Driving
(00:04:56) Driver Assistance vs. Fully Driverless
(00:07:02) Tesla and Waymo Experiences
(00:09:41) Liability and Driver Monitoring
(00:11:19) Waymo's Robo-Taxi Experience
(00:14:00) Tesla vs. Waymo Strategies
(00:15:15) Challenges in Self-Driving Technology
(00:17:38) Edge Cases and Safety Concerns (Part 1)
(00:18:09) Sponsors: Oracle | Brave
(00:20:13) Edge Cases and Safety Concerns (Part 2)
(00:23:53) Data Acquisition and Learning Strategies
(00:26:43) Technology Stack and Planning
(00:31:03) Sponsors: Omneky | Squad
(00:32:50) Neural Networks and Perception
(00:39:30) Hardware and Sensor Approaches
(00:45:46) Camera vs. LiDAR Debate
(00:48:20) Data Quality and Business Models
(00:52:24) Transparency and Regulation
(00:56:52) Role of Maps in Self-Driving
(00:59:49) Local vs. Remote Processing
(01:01:44) Cruise's Challenges and Future
(01:04:58) Global Self-Driving Landscape
(01:07:36) Other Notable Players
(01:10:56) Safety Statistics and Adoption
(01:20:31) Regulatory Environment
(01:23:32) Waymo's Safety Data
(01:25:39) Cultural and Technological Barriers
(01:30:09) Potential Policy Changes
(01:33:41) Market and Ownership Models
(01:36:37) Future of Self-Driving Services
(01:39:26) Unexpected Scenarios and Partnerships
(01:42:17) Comparisons to Language Models
(01:44:55) Future of AGI and AI Applications
(01:47:59) Regional Adoption Predictions
(01:49:47) Outro

---
SOCIAL LINKS:
Website : https://www.cognitiverevolution.ai
Twitter (Podcast) : https://x.com/cogrev_podcast
Twitter (Nathan) : https://x.com/labenz
LinkedIn : https://www.linkedin.com/in/nathanlabenz/
Youtube : https://www.youtube.com/@CognitiveRevolutionPodcast
Apple : https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify : https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Self-Driving Cars Timothy B. Lee Answers All the Questions You Were Too Afraid to Ask
**Cognitive Revolution:** [August 07, 2024](https://www.youtube.com/watch?v=doIcymZuw9Q)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today I'm excited to share my conversation with Timothy B. Lee,
*  noted autonomous vehicle industry analyst and author of the Understanding AI newsletter,
*  online at UnderstandingAI.org. Tim has been covering the self-driving car industry since 2016,
*  and his in-depth analysis of the various technology stacks, business models, and regulatory
*  issues that have shaped the space make him the perfect person to answer all of my many
*  questions on this topic. Over the next two hours, we characterize the current state of the art in
*  autonomous vehicles, starting with our personal experiences with both Waymo and Tesla. We unpack
*  the contrasting approaches of these industry leaders, including their different hardware
*  stacks, data acquisition methodologies, and deployment strategies. We examine the tactical
*  hurdles that are still facing self-driving cars, from handling edge cases like emergency scenes
*  to expanding beyond well-mapped areas. We interrogate company-published safety statistics
*  and explain why it remains difficult to definitively prove that autonomous vehicles
*  are indeed safer than human drivers, though it does seem like Waymo is getting close.
*  And finally, we explore the regulatory environment, starting with the very notable
*  fact that government oversight has not been nearly as restrictive as many might have feared.
*  Along the way, Tim also explains why some previous predictions have proven overly
*  optimistic and shares his current expectations on timelines for widespread adoption. We even
*  explore the potential for new vehicle form factors once human drivers are no longer necessary.
*  Throughout, Tim provides a very balanced view. He's clearly very excited about the fact that
*  today's leaders are finally getting to the point where their products really work. Today,
*  Tesla allows human drivers to take their hands off the steering wheel, and Waymo is beginning
*  to scale truly driverless cars. And yet, at the same time, Tim is realistic about the fact
*  that it probably will still take a few years before self-driving is very broadly available.
*  For my part, driving is the most dangerous thing that I personally regularly do, and many people
*  spend a lot of time doing it, so I really can't wait for AI driving systems to become the new
*  normal. As always, if you're finding value in the show, we'd appreciate it if you'd take a moment
*  to share it with friends or leave a review on Apple Podcasts or Spotify. You can also DM me
*  on your favorite social network, and we continue to invite your resumes if you're an aspiring AI
*  engineer or AI advisor via our website, cognitiverevolution.ai. Now, I hope you enjoy
*  this conversation about all things self-driving with Timothy B. Lee, author of UnderstandingAI.org.
*  Timothy B. Lee, author of the Understanding AI newsletter at UnderstandingAI.org. Welcome
*  to the Cognitive Revolution. Thanks for having me on. I've been listening to the podcast pretty
*  much since the beginning, so I'm excited to be part of it. Thank you. That's flattering,
*  and I'm excited about this as well. I've been a follower of your analysis of the self-driving
*  car industry, both through your public analysis and through many one-on-one questions you've been
*  gracious enough to answer. What I'm excited to do today is just try to lay out for listeners
*  beginning to end, like, where are we in this self-driving car journey? Ultimately, when do I
*  get my car that I can sleep in on the way to my grandmother's house? There's obviously a lot to
*  cover between here and there, so all angles is the goal, and you're the man for the job.
*  Do you want to start off with just a simple overview of the levels? I think people will be
*  familiar with, at least I've heard this before, but it's probably a good way to introduce, and I
*  think you have a little bit of a contrarian take on it too, so you can give people your sense of
*  what really matters in terms of the levels of capabilities in self-driving. Sure. There's the
*  standard SAE levels, levels one through five, and level one is just a regular car with maybe
*  regular cruise control. Level two is driver assistance. Level four is a full self-driving
*  car like Waymo, but in a limited kind of area, and then you have level three is somewhere between
*  those where it's like some kind of shared responsibility between the car and the driver,
*  and level five is supposedly like a car that can go anywhere. I don't find these levels to be super
*  helpful because, especially that level three, where you've never been totally clear. I guess
*  the idea is a car where you use it in the driver's seat, but the car mostly drivers itself, but then
*  if it gets a problem, it hands over control to you, and that just seems like a kind of user experience
*  nightmare and a safety nightmare because if the car suddenly has a problem and you haven't been
*  paying attention, it's hard to be sure. Are you going to have the context to make the safe decision?
*  What if you're turned around or you're putting your kid in a car seat or something? I think a much
*  simpler way to think about it is there's two kinds of vehicles. There is driver assistance, which is
*  any of the Tesla or any other automaker has lane keeping, driver assist kind of things, and that's
*  the system where the driver is still responsible. The car might help, the car might do a lot of work,
*  but you are still supposed to have your hands on the wheel, eyes on the road. And then there is
*  four fully driverless vehicles where you're not in the steering wheel, the car is legally
*  responsible, and so far at least that always comes with a geofence where there's some places
*  where it'll go and some places it won't go. I don't think that level five is really a useful concept
*  where there's no geofence because there's always going to be a service area. There's always going
*  to be countries or types of roads or types of off-roading that the vehicle doesn't do. I think
*  about a little bit of cell phone service, right? To first approximation, you could use your cell
*  phone anywhere, right? But that's not really true. There's areas that don't have cell phone towers
*  and nobody says, oh, that's not like a real cell phone because it doesn't go in rural Alaska or
*  something. So I think self-driving cars are similar for the foreseeable future. Vehicles that are
*  driverless are going to have a service area. And the question looks to be like, what is that service
*  area rather than can this go anywhere, just some places? It might be interesting as we get deeper
*  into the technology stack and the different approaches that different companies have taken
*  in to try to understand better to what degree that limitation will be a matter of connectivity
*  in the same way that it is with a cell phone or having a map or not having a map versus
*  if it's a self-contained system that's all on board in the car. Is it something where the car
*  is just saying, sorry, this looks too crazy for me to go any further?
*  I don't think it's about connectivity. It's partly about the map, but it's also about things like
*  regulatory questions. In the future, I assume you'll need a license to operate a taxi service
*  in certain areas. And also if there's no driver and the car gets stuck and there's nobody in it,
*  somebody's going to have to come service it. And so I think if you think about it as a service,
*  as opposed to just a car, any company that offers a service has a certain set of areas where they
*  offer the service and areas where they don't. And the car is only going to operate where the company
*  has service. Now there might be a future where the company literally has a footprint everywhere. And
*  so it can pretty much offer service everywhere, but I think that's quite far away.
*  Let's maybe talk for a second about the two canonical companies that most people have
*  experienced. I think still most listeners probably have not experienced either of these
*  technologies. I think you and I are both in the lucky few and I have to credit you for
*  giving me a connection at Waymo that got me off the wait list and allowed me to actually
*  get into the Waymo a couple of times last time I was in San Francisco. So thank you for that.
*  The two are Tesla and Waymo and we can get into other companies as well. But Tesla,
*  it sounds like you put into the level two category. Last time I used it, you can add onto this with
*  your own reflections on the experience was for me about a year ago. It was last summer. I took an
*  eight hour round trip to actually take my grandmother home. It was both my and her first FSD experience
*  together. And I would say it was very strict about enforcing that you are paying attention.
*  If I understand correctly, it has a camera on you from the rear view mirror that's monitoring to
*  make sure you're alert and engaged. And you also had to have hand on the wheel with a little bit
*  of torque, which was something it took getting used to for me in and of itself. Otherwise,
*  it would say you're not paying attention and execute like a pull over and shut down of the
*  self driving experience. So that was like pretty short leash on the human in the seat.
*  I didn't find the experience to be overall very good. I came away extremely impressed.
*  I probably let it go a little too fast on the highway. Honestly, my neighbor who lent me the
*  car had a default setting of 20% over the speed limit, which I just naively followed. And then I
*  got back. He's, Oh no, I turned that thing up and down all the time. It just depends on where we're
*  going. So I was going 84 in a 70 at night in the rain on the way home, which as I look back,
*  I was like, maybe that wasn't so smart, but I was definitely paying close attention.
*  And overall it did really well. Certainly at those high speeds, I thought it was like amazingly good
*  when it was the only kind of areas where I found that it messed up a bit was in ambiguous situations
*  where there's a stop sign that could be interpreted as facing one of two ways. And I've
*  personally been a little bit confused by some of those situations too. That was one where it was
*  probably the most like risky thing that it got wrong was stopping on the off ramp of a highway
*  where it definitely should not have. But overall, I thought that was really good. I think you've used
*  it more recently than I have. The hands are now free. What else is kind of new in that experience?
*  And is it still two at that? Would you still put that? I know you're not a lover of the levels.
*  This is why I emphasize liability. I think the fundamental question is if a car crashes,
*  you get to sue the company or whoever you hit sue you because ultimately there's a technological
*  design decision of like how strict is it going to be about enforcing the requirement to do it.
*  But even if the car is very advanced in the Tesla system, they're still going to blame you. If you
*  crash the car, they're going to say you should have been paying attention. And so that's the
*  distinction I would draw there. So I was, my experience was back in March, I spent about 45
*  minutes behind the wheel in San Francisco. And so I was not testing the strictness of the driver
*  monitoring because San Francisco is a pretty hair raising place to drive. I was happy to do it in
*  San Francisco both because it gives it a good challenge for the vehicle and also because that's
*  also where I'd taken some way more tests. So it's a little bit of an apples to apples comparison.
*  So I did not try taking my hands off the wheel or taking my eyes off the road because I was
*  like wanting to make sure I didn't crash the vehicle I was borrowing. So I don't know about
*  the driver monitoring, but my experience I had, like I said, I did it for about 45 minutes. There
*  were two times when I took over during that 45 minute period. There was one time I was making
*  a turn onto a road that had a bike lane with some plastic separators and it was about to hit one of
*  those plastic bollards or whatever you call it. And the other time it got in the wrong lane and
*  then was trying to cut over into a lane that was like full and so their cars behind me honking
*  because that was like, so that wasn't like technically a safety issue, but it was definitely
*  a mistake and something that I was annoying people on the roads. Yeah. So that was my most recent
*  experience with it. And it was this, do you know what version that was? We're now on 12.5.
*  Okay. So that was after the big streamlining to neural networks, but before the very latest.
*  Exactly. Okay. On the Waymo side, I think what people most envision when they dream about a
*  self-driving car future, and it is amazing that it's here today. It is in a limited geographical
*  area. Like I wanted to take it to the Oakland airport as I was leaving town. Can't do that,
*  can't cross the bridge, can't get out of the San Francisco city limits, but it was within the city,
*  really an amazing experience. I mean, you use the app, the app is basically an Uber-like app. I have
*  some questions about what this may mean for the future of Uber as well. Some of the car, pretty
*  quick response time. They seem to have liquidity in that San Francisco surface area. It pulls up,
*  it pulls over. I think it shows your name on the top of the thing, which is cool. Honestly,
*  probably the hardest part of that experience was figuring out, at least as a first-timer,
*  that I needed to unlock the door in the app before I could get into the car.
*  Maybe a little UX refinement still to be done there. But then once you're in the car, it's wow,
*  this thing, there's nobody in the driver's seat. There's just a sign there that says,
*  don't mess with the controls. And you ride along and it takes you where you want to go. And I think
*  if there was anything that was most striking about it, it was how quickly I adjusted to it
*  and started to become bored. I'm somebody who's very enthused about this technology. I was like,
*  this is a privilege to be in here. But then we'd stop at a red light. I'd start to look at my phone
*  and next thing we're going again, I'm still looking at my phone and I'm like, wait a second,
*  get your eyes off the phone. Actually pay attention to what's happening. It was just amazingly
*  comfortable, normal. And in my, not super high experience, but probably an hour over a couple
*  trips, about as close to flawless as I could say. I would say it was a more comfortable ride
*  than an average Uber. Maybe not quite at the level of skill of the very most skilled drivers who
*  might've made that extra light or whatever. But also that's not exactly what they're trying to
*  get. They're not emphasizing making the light. So I was super impressed. I know you're super
*  impressed with Waymo too. What would you add to that? Yeah, I've done about three hours of driving
*  over a couple trips to San Francisco this year and similar experience. So I, over those nine rides,
*  I never saw make it even like a minor mistake. Definitely nothing, no safety issues, but also
*  just the ride was very smooth and never got confused or gotten the wrong lane or anything like that.
*  And yeah, like you, it was first couple of rides, I was paying close attention. I think I took a
*  video of the first one, but by the fifth or sixth ride, I was like reading a book or looking at my
*  phone. It's just, it's just, when they're that consistently good, it's just not interesting.
*  Like nothing, nothing interesting is happening. So yeah, I'm like very impressed overall with the,
*  the quality of the driving. So we've got these kind of two apparent leaders and they have quite
*  different strategies in a number of ways with the highest level. It's like Tesla is a car that you
*  own. It is available quote unquote everywhere. You can refine that, but it's nationwide anyway.
*  And you still have to be engaged. And there are some mistakes that we've each seen that we've had
*  to catch. Although I would never say I felt like radically unsafe. Like I definitely did have to
*  do stuff on the Waymo side. It's a robo taxi. It is very narrow footprint, but it seems to be
*  more polished, at least within its kind of designated service area. So Tesla has to close
*  the gap on whatever that last, probably even less than a 10th of a percent now. And Waymo has to
*  expand its footprint to cover everybody if they really want to bring in the dream of the self
*  driving future. What makes this hard? Is it the same thing for people who obviously have a sense
*  that, wow, there's a big world. There's a lot of random things can happen. Is it the same kind of
*  hard for each of them still? Or is it a sort of different fundamental challenge that they each
*  have to solve to really get over that hump at this point? Maybe this shows my bias, but I think of
*  it being a sort of different stages. So I think some like history is just weird. So I've been
*  covering this industry since 2016, 2017. And back then, Waymo was just this Google Self Drive
*  card project. And they've had to file annual reports about their disengagement with the
*  California regulators. And in 2017, the February 2017, they reported that during 2016, their
*  vehicles, their safety drivers had to take over once every 5,000 miles. Now, there's probably some
*  cherry picking, they would go back and look at them and say, this would really cause the safety
*  instance. So you can question that. But way back then, they were, I think, in a similar position
*  to where Tesla is now, where the cars pretty much always work. There was occasional kind of weird
*  edge cases. And they really felt like they were ready to do the driverless thing. And they put in
*  orders for 60,000 vehicles in 2018 from Chrysler and from Jaguar. And they thought, I think they
*  like sincerely thought that they were on the verge of having this nationwide taxi service.
*  And then it turned out to be much harder than they thought. And the service they launched in 2018,
*  ended up having safety drivers another two years before they went driverless. And there was very
*  small scale in 2020, 2021. And it was only a year or two ago that they really started to ramp up in
*  scale. And it's not totally clear to me why, but I think it's, on some levels, just about the edge
*  cases. Some of them are really hard. And the one that I've been thinking about the most recently,
*  and I think you've seen a lot of news reporting on in San Francisco last year, is emergency scenes,
*  either a car crash or a fire scene, where the stuff that happens there is just very different
*  from the typical situation. So in a normal situation, there are lanes, the car has to stay
*  in the lane. There's rules about you turn here, you don't turn here, you stop at this light,
*  and so forth. When you get to a car crash, a police officer will come and they'll start
*  drafting traffic in a totally different way. And every car out there behaves differently. And so
*  you have to reason about for this car to go here, I have to stop or I have to back up or this police
*  officer wants, it's just a totally different problem. And that might only happen once every
*  10,000, 100,000 miles. And if you have a safety driver, it's not a big deal because the safety
*  driver can take over if the car gets confused. But if you have a driverless vehicle, the driverless
*  vehicle has to handle that somehow. And I think there's just enough of those situations that if
*  you have a driverless vehicle that only does 99.9% of the time, it's still getting stuck all the time,
*  or maybe it's running into people sometimes. And that's just not good enough. And so the last five
*  years has been Waymo going from 99.9% to what they're now, which is a little hard to tell exactly
*  what the kind of number is now. But now they handle enough of those edge cases that it seems
*  to be a kind of viable service or close to it. And I think Tesla's just at the start of that
*  state, that process. My guess is that if a Tesla comes up to a seat of a car crash, it'll either
*  get stuck or it'll signal the driver to take over. I never tried it myself, but I would assume it's
*  not ready to do that the way Waymo does pretty well. Hey, we'll continue our interview in a
*  moment after a word from our sponsors. AI might be the most important new computer technology ever.
*  It's storming every industry and literally billions of dollars are being invested. So buckle
*  up. The problem is that AI needs a lot of speed and processing power. So how do you compete without
*  costs spiraling out of control? It's time to upgrade to the next generation of the cloud,
*  Oracle Cloud Infrastructure, or OCI. OCI is a single platform for your infrastructure, database,
*  application development, and AI needs. OCI has four to eight times the bandwidth of other clouds,
*  offers one consistent price instead of variable regional pricing. And of course, nobody does data
*  better than Oracle. So now you can train your AI models at twice the speed and less than half the
*  cost of other clouds. If you want to do more and spend less like Uber, 8x8, and Databricks Mosaic,
*  take a free test drive of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive,
*  oracle.com slash cognitive. This episode of the cognitive revolution is sponsored by the Brave
*  search API. You may know of Brave as an alternative to Chrome. But did you know that Brave has its own
*  independent search engine powered by its own 20 billion page index of the web? The Brave search
*  API gives developers reliable and affordable access to programmable web search, auto suggest,
*  spell check, and more. With flexible plans for all types of use cases from rag search to automated
*  business intelligence. On top of that, it's up to three times cheaper than Bing, all without
*  compromising on quality, speed, or reliability. Over 700 businesses, including Coheer, Chegg,
*  and Kagi rely on the Brave search API. And a recent survey showed that 94% of customers would
*  recommend it to their peers. To start building apps with the power of the web, sign up at brave.com
*  slash API and get up to 5000 free monthly calls. I don't have any direct info on what a Tesla does
*  in that situation either. I did ask my neighbor who drives his a lot or has it drive him a lot.
*  And he said, yeah, it doesn't really take sort of unconventional moves to handle strange situations.
*  One I specifically asked about was like, if somebody is coming up on you and appears like
*  they might be about to rear end you, would the car move forward to give the car that's coming in hot
*  more space? And he was like, I don't think so. It's probably not going to be that creative in
*  a situation like that. So I guess there's, is this one thing or is it two things? The,
*  in my instinct as somebody who loves to test AI products in all different formats around the hand
*  signals thing would be like, I sort of bet that like the latest Gemini model that we're talking
*  on the first full day when Gemini tops the LM Sys leaderboard with their latest August 1st release.
*  And so it can handle multimodal, you can put video into it. My guess is that it would like
*  out of the box, be like pretty able to interpret a scene like that and say, what does the officer
*  appear to be signaling in the situation? Obviously you have to be like more reliable than probably
*  Gemini is going to be, but is it just ultimately just the volume of these unfamiliar? I guess my
*  gut is saying that still feels like common enough that it doesn't seem like the kind of thing that
*  should be that far. You know, if it can do all these things that it can already do, like
*  why wouldn't it be able to learn the hand signals or are the hand signals really that,
*  you know, never seen before that you couldn't expect similar
*  propellants there? I think there's a couple things. The main thing is just as different
*  from what the main training data is. So the fact that Tesla can do, can stay on your lane in the
*  highway, just doesn't tell you much about whether it's going to do those other things. It's pretty
*  rare. So it's rare enough that you're going to need a lot of miles before you have a training
*  data. If you're going to do a kind of learned approach, you're going to need a lot of training.
*  You could take a car on a test track and have somebody pretend to be a police officer, but it's
*  hard to think to do it realistically. A real crash scene has dozens and dozens of cars in kind of
*  random configurations. It would be expensive and hard to do that in kind of a fake situation.
*  But then I also think the kind of reasoning is pretty different. When you're on a regular
*  road, there's a rule you can learn that says you always stay on this lane. Whereas in a crash
*  situation, you really have to reason counterfactually. You have to anticipate what are the other drivers
*  going to do to a much greater extent. This vehicle is trying to get out of this lane,
*  and so I better not get in the rain because then we'll have a... So I'm definitely not saying it's
*  impossible for AI systems to do it. I think it seems like Waymo is getting there, and I'm sure
*  Tesla will get there eventually. Oh, and one of the things I think that with Tesla's current approach,
*  I think that most Tesla owner's instincts will be to switch off FSD as they're approaching it,
*  which means you're not necessarily going to get good training data. Ideally, what Tesla would like
*  is for the human driver to allow the FSD to try it until the point where it actually makes a mistake
*  and then take over because then you have data and this is how it works in a real situation.
*  But if the human driver is worried about annoying the cop or whatever and just turns it off before
*  it gets there, then you don't have as much... You don't have good training data. So yeah,
*  I'm not saying it's impossible. It's just... Empirically, from looking at what's happened with
*  Waymo, it seems like a much harder problem than the other way. I don't think the people at Waymo
*  cruise are idiots. I think they knew this was a problem. I'm sure they made some effort to
*  prepare for it, but it turns out to be just empirically watching how it's gone for them.
*  It seems to be a very difficult thing to deal with. Yeah, that's a good transition to
*  one dimension. And I want to go dimension by dimension here of how these companies have
*  approached this problem with their strategies have been, the strengths and weaknesses of those.
*  This is a good entry point to data acquisition and I guess overall learning strategy.
*  The Tesla bull case, as I understand it, is they've got by far the biggest deployed base.
*  And I understand that they collect data on human driving. So when you say if the person is
*  a little bit nervous or whatever and just takes over, would that mean that Tesla wouldn't get that
*  data? Because my naive understanding would just be like, if they can continue to record what the
*  human does, then isn't that sort of in a sense like labeled data or not gold standard, but there's
*  some sort of ground truth there of how the human navigated that situation. So am I misunderstanding?
*  Do they not collect as much as I thought they did? So I don't think we know exactly how they do it.
*  I don't necessarily think that. I think it's quite possible they are able to collect the data as the
*  human being is driving. I think it's just less useful. You can try to go back in simulation and
*  simulate what our vehicle have done in this case. But because it's an interactive kind of thing,
*  it's not often obvious in the moment. The question is not did our car hit the other car.
*  It's would this car's decision have led to a situation three seconds later where everybody's
*  jammed up because the car went the wrong way and got in somebody else's way, stuff like that.
*  That data is, I think that training data is definitely useful, but it's not, I think, as
*  useful as if you had a professional safety driver who was a little more aggressive about letting the
*  vehicle do its thing until it got into a mistake. But yeah, absolutely. So Tesla does have the ability
*  to gather large amounts of data from its vehicles, from its fleet. And as I understand it, it has some
*  pretty sophisticated tools where it can say, okay, we're trying to train on cars with bicycle
*  strut to the back and they can send some kind of query out where it says we're looking for this kind
*  of image and then the car will run some sort of local search through its kind of database and send
*  back candidate images. And so they have a very good ability. I do think this is one of the advantages
*  Tesla have. They have a good ability to both collect a lot of data and also focus a little
*  bit on here's the kind of data that we're looking for. I think that is plausibly one of the advantages
*  they have over other companies that are trying to do this. They would get data from all cars or all
*  cars that haven't opted out. You don't need to be an FSD customer to be like relaying back camera data.
*  Yeah, I don't look at this closely, but yeah, I don't think it's limited FSD. I think anybody,
*  probably like when your car is close to a Wi-Fi at point, the Tesla can suck down
*  images or telemetry from recent trips you take. Yeah, I would assume the Elon terms of service are
*  pretty friendly in terms of sharing data back with the company.
*  Okay, so there's like a, would seem to be a big data advantage, but I guess to the degree,
*  or the degree to which that advantage matters probably depends a lot on like other aspects
*  of the technology stack. So when I'm hearing your analysis of would the car have done something
*  which three seconds later would create a challenge, that opens up a number of questions for me. I
*  guess the first one is what is the cycle time at which these things are running and making
*  adjustments? Because if it is multi-second, then it's yeah, you're doing a significant amount of
*  modeling and predicting what other people are going to do in response. It seems to get complicated.
*  I could also imagine a stack where the sort of next move, the next token time, if you will,
*  I'm used to language models, right? So these things are measured in tokens per second.
*  And now we're often getting into hundreds of tokens a second. If you could run an inference
*  cycle at that same frequency, then it would seem like you could maybe be a little less
*  worried about the butterfly effect of if I did something slightly different, what would happen
*  downstream and more just focus on imitation learning of can I learn to do exactly what the
*  human is doing on like a hundredth of a second or a tenth of a second sort of basis. So I guess
*  first question is you can maybe just zoom out if you want and take this from the beginning.
*  But the frequency is what I'm stuck on at the moment.
*  I think so let me like walk through the standard architecture. So there's I think it has three
*  layers. So there's perception layer, which is the layer that takes the sensor data and builds a
*  world model. It says here's all the objects that I can see with my sensors, their locations,
*  their velocities, the types of objects they are. So that's the first layer. Then there's a
*  prediction layer, which has given all this data I have, what is the world going to look like one,
*  two, three seconds ahead. And that's important, obviously, because if there's a car coming from
*  the opposite way at an intersection, and it's not currently in front of you, but it's a certain
*  velocity and it's going to be in front of you, you need to be like playing that out. And if there is
*  planning, we're given this set of current states and future states, what's the path that gets me
*  where I want to go without causing any collisions, etc. And so I think that just a very naive, like
*  short term imitation learning approach, I think is not really going to work because what the human
*  is doing is the human has a prediction kind of engine in their head, right, you're thinking about
*  in three seconds, this car is going to be in this location. And so if I'm also in their location,
*  there'll be a crash. And so in the same way that like language models, when you train a large
*  language model, it builds, it learns higher level concepts that then allow it to predict the next
*  token in a way that's maybe not explicitly planning what the future tokens are, but it's able to do
*  higher level reasoning. If you had a model that was able to learn the implicit model that humans
*  have, I think that could work in theory. But I think what and actually, I think that it's evolving
*  that direction. So five to 10 years ago, it really was true that like the Waymo and Crew stacks were
*  a bunch of pretty hand coded rules where if you're in this kind of situation, do this, that kind of
*  thing. And over time, I think they have replaced more and more of that with neural networks that
*  learn. But I think it's still probably a single digit number of there's probably one or a few
*  perception networks, there's probably a one or a few planning networks that they published papers
*  about a few of these. So yeah, so I think the trend has been towards more learn neural network,
*  deep learning kind of things. But it's not they're not yet to the point where there's just one big
*  neural network that just has like sensor data and like pedal and steering wheel positions out.
*  And I'm not sure that they're going to get there or that it would make sense to get there because
*  because you do want to have you want a much higher level of reliability than you see with
*  the work language model. And there's a lot I think there's a lot you can do you at least want to have
*  visibility into the vehicles implicit knowledge model the world so you can verify yes, it's
*  seeing the things that really are there. And yes, it's making reasonable predictions. Like you can I
*  think some of the training you can do, you can train the perception and planning and predictions,
*  like layers separately because you have ground truth there you say I actually know where this
*  car was. And so I can see was my prediction to where the car go accurate. So yeah, I think that's
*  the direction it's headed is going to be a small number of networks, but not one Tesla has talked
*  about having an internet and network. And I don't think they've been super transparent about exactly
*  what that looks like. I'm a little skeptical that it's literally just one end network that takes
*  sensitive data in and outputs like a driving direction. But I'm not sure exactly. Hey,
*  we'll continue our interview in a moment after a word from our sponsors.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki
*  so much that I invested in it. And I recommend you use it to use cog rev to get a 10% discount.
*  Hey, all Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex-fang
*  senior software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale from
*  sourcing to interviewing to on the ground operations and management. That's why I teamed up with Sean
*  Lanahan, who's been building engineering teams in Vietnam at a very high level for over five years
*  to help you access global engineering without the headache. Squad Sean's new company takes care of
*  sourcing, legal compliance and local HR for global talent so you don't have to. With teams across
*  Asia and South America, we can cover you no matter which time zone you operate in. Their engineers
*  follow your process and use your tools. They work with React, Next.js or your favorite front end
*  frameworks. And on the backend, they're experts at Node, Python, Java, and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on Upwork that's doing two
*  hours of work per week, but billing you for 40. But you'll get premium quality at a fraction of
*  the typical cost. Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squad.com and mention Turpentine
*  to skip the wait list.
*  I think there is at least a, they display for you in both of these examples, they display for you on
*  the dash, a world model. So you can see that there is something else happening besides just straight
*  to actuation on the controls. Those are both striking. That's like an incredible thing to
*  watch unto itself. Honestly, if you have never sat in one of these cars, even if you just forgot
*  about the fact that it can drive itself for a second and you just looked at how well it is
*  understanding the scene around you and labeling those things and knowing what's a person and
*  what's a vehicle and that in of itself is just like pretty impressive. We just did an episode not
*  long ago with two authors, Nora and Ben of a paper called guaranteed safe AI, which is a proposal for
*  a framework that seems like it's almost perfect for self-driving. It kind of has four components,
*  but three are added onto the main AI. So their idea is maybe you have a black box AI, maybe you train
*  this thing to be 100% end to end. We want to be able to audit this. We want to be able to have a
*  much better sense of what's going on. Then we can get by just brute force poking at it with situational
*  testing. So how do we do that? The three components that they add on are a world model. So it seems
*  pretty clear that these cars have some version of that. Then they advocate for an explicit safety
*  specification. I don't know if the makers have anything like this today, but they're envisioning
*  things. They're like acceleration should never exceed whatever, or we should never get closer
*  to another object than whatever. And to make that clear, one of the benefits that they see on this
*  is that it enables a societal conversation about what the safety standards should be.
*  And then the third piece is a verifier, which is the thing that takes the output of
*  the core black box AI and simulates what will happen if we do that according to the world model.
*  And does that still fall within the safety standards? It seems like that's what's going on
*  here. Does that sound like the architecture that these companies already have? Yeah, at a high level,
*  that's what they're trying to do. I assume that Waymo has internally, either explicitly or
*  implicitly, rules like that. Don't exceed this acceleration. Don't get any closer than x to a
*  car. One of the things I think is difficult, so Mobileye has a standard called the Responsible
*  Sensitive Safety standard that tries to do this to say, here's our formal specification of how we
*  think a self-driving car should behave. And I think that's a perfectly nice idea. I think that
*  one of the things that makes it really difficult is that you're not just trying to optimize your
*  safety. You're also trying to optimize for getting where you're going and not irritating people. So
*  one way you can make a vehicle safe is having to be very conservative. And anytime it's not
*  sure what's happening, it slows down and stops. And at least if you're not in a freeway, that's
*  always safe in the sense that nobody's going to die from that. But if you have a vehicle that's
*  super over cautious, it's going to cause traffic jams and piss people off. And also if you have a
*  fire engine coming, then you could indirectly cause safety problems. And so I think part of what
*  makes this problem challenging is you want to never get into a crash, but also behave like a
*  normal driver. And when it is safe to go, you want to go. And I think that is much that tradeoff.
*  I think it would be much harder to capture in a simple, some kind of standard. It's just there's
*  lots and lots of different iterations. And ultimately, I think you just need a ton of
*  examples, ton of training data, and that's something you need to learn. And yeah, I'm all for
*  more transparency, but I think it's a hard problem to formalize it. Yeah, I think the way that they
*  would respond to that, and I can't speak authoritatively on this framework, but I think
*  the idea there would be that the core AI that you've trained, that this sort of guaranteed safe
*  framework sits around, can still be responsible for the sort of human driver experience and the
*  not annoying people and all the fine points. And it's okay if those remain opaque in terms of exactly
*  how they're working. It could be a little bit more permissive than, and in fact, you would almost by
*  definition, you need it to be a little bit more permissive than what the system actually does.
*  But you could hopefully get it down to a finite number of, and hopefully reasonably understandable
*  number of rules of the thou shalt nots of this problem, which obeying all the thou shalt nots
*  is not sufficient to have a great user experience, but it would hopefully at least be sufficient to
*  say we can make some quantitative guarantees around like very bad things not happening.
*  Yeah, my guess is that Waymo would pass that for Lee. The other issue is that sometimes you
*  have planning mistakes, sometimes you have perception mistakes where you think that the child is a
*  garbage can or something, and I don't think there's any way you can formally prove that
*  a car won't misunderstand its model. Yeah, I think you could probably apply a model like that to the
*  prediction and planning parts, or at least the planning part, and say given a particular world
*  state, we can prove that it won't make a mistake relative to the specification, but that's only
*  going to capture a slice of the possible errors it could make. But yeah, I would be happy to see
*  companies do something like that as part of the safety case they make to the public.
*  So going back to the frequency thing and the sort of planning, this maybe is just not
*  disclosed, but I guess my experience in, I would say both of these cars, but the Waymo one is most
*  fresh in my mind, was that it did feel like the response time was human-like. It felt like it was
*  responding as fast as I would respond. I actually don't know what my own response time is. Maybe
*  you have a stat on that would be the human point of comparison, but do we know how far
*  these things are planning and predicting out? How far does their
*  world model extrapolation go? And do we have any sense for how often they are updating their outputs
*  to gas brake steering? I don't think they've disclosed anything like that, and I bet it's
*  complicated. I remember maybe a year ago you had a drone maker on where they talked about there being
*  different levels of abstraction, where there's a high-level navigational thing that maybe updates
*  every second or something, and then there's a real-time make sure the drone stays stable
*  thing that's operating at a millisecond level. My guess is it would be a similar thing where
*  there's some systems, the system that figures out what's our overall direction, that's probably
*  pretty slow, but then somebody runs into the car that loop that's slam on the brakes. Maybe it's
*  very fast. I don't think they publish any specific data on which things happen at which frequencies.
*  Yeah. Deep in the catalog there, I appreciate that. That was July 4th, the last year,
*  Hike Martiros from Skydio. I learned a lot from that episode just in terms of how these different
*  frequency and different level of abstraction control loops interact with each other. I think
*  they had at least four, maybe five. The very lowest level one was I think tens of thousands of
*  hertz, and that was just at the level of the voltage being applied to the motor could change
*  that fast. Then yeah, the outer layer was language model instructions of planning,
*  how am I going to go survey this bridge or this building or what have you, and connecting all
*  those things where each level interfaces with the one above and below it was a huge part of what
*  they had invested. They're really just adding on the last layer now. Interestingly for them,
*  think the... This may be quite different from what I'm gathering from the self drivers, but
*  pretty much all of the lower level stuff was either explicit code, like they'd done a lot in
*  explicit code, or very small neural networks. That was all there. With this new generation of AI,
*  they were able to layer on one more layer at the top where the user could give high level
*  instructions. A lot of that stuff below was older technology and had been built out
*  largely in explicit fashion over a long time. Interestingly, a great callback.
*  We don't know ultimately how fast they can respond. I guess I can only say it felt like
*  I wasn't noticing anything faster or I wasn't feeling any lag relative to what I would have
*  done. It's a pretty qualitative statement. Let's do a deeper unpacking of some of these
*  technology stack decisions that folks have made. We've covered the two form factors that you can
*  get the car and you can buy it, or you can go on an app with Waymo. One other one that is
*  maybe worth considering, or maybe you think it's a red herring, is the aftermarket kit,
*  like the retrofit style, whether that's comma perhaps or some other thing. Do you see that
*  being a meaningful form factor that we should also be thinking about?
*  I think Comma is a very interesting company. They have a very active open source community
*  and they've managed to build and add support for a ton of cars. If you have a reasonably new car,
*  there's a good chance you can apply Comma to it. In Commas, they sell a device that's just like a
*  little smartphone, I think, basically with a camera on it. Every car has a port that gives you
*  access to the car's onboard network and you plug it in and it gives you Tesla autopilot style,
*  level two self-driving. I don't expect that to be a big market because for one thing,
*  it's been a regulatory gray zone. Comma, I think the fact that the user downloads the software
*  separately and installs it themselves, I think may give them a little bit of, they've had some
*  friction with NITSA, the federal regulator, about this in the past. So partly for regulatory reasons,
*  but also just because I don't think most people want to screw around with open source software.
*  So I could imagine if I think the bold case for Comma is maybe at some point,
*  it will license this technology to car makers to build Comma on. But I think there's lots of
*  good reasons to have that be vertically integrated, ultimately have your car manufacturer pick a good
*  system and put it on there for you. Yeah, it definitely takes the notion of AI hobbyist
*  to the next level when you're strapping it onto your Chrysler minivan that's how many years old.
*  The other thing is I think the car maker can integrate the sensors much better. So it's
*  impressive that Comma can do what it does with basically one smartphone camera mounted on your
*  windshield. But in the long run, you're going to have, I think Tesla has eight or 12 or something
*  cameras in there. I think in the long run, that's what you're going to want. And you might as well
*  have software that's integrated with that specific sensor suite as opposed to having some aftermarket
*  thing that's not going to work as well with the specific characteristics of your vehicle.
*  Yeah, it's amazing that they can do much of anything with just one point of view. Does Comma
*  also suppose or require that the car itself has additional cameras? It's really just using the
*  camera. There might be a rear sensor, but yeah, it's like much fewer sensors than like a Tesla
*  has. And yeah, I think it's just based on the camera that's in the little device you put on
*  your windshield. So it's pretty impressive. Yeah, cool. Okay, then let's talk hardware
*  maybe for the other leading strategies. Tesla is famous for an all-camera approach. I don't know
*  if they're still strictly on that. One look at the Waymo and you can tell that this is doing
*  something a little bit differently. So break down for us how people are sensing the world.
*  Yeah, so the three major sensors people talk about are camera, lidar, and radar. Tesla used
*  to have radar and I believe about a year or two ago, Tesla took away the radar. So they're like
*  really committed to this camera only approach. Whereas Waymo has all three. Waymo has a lidar
*  sensor on the top that's a big long range. And then it has, I forget the exact number, but maybe
*  four or six ladars around the edges of the vehicle that are short, shorter range, wider angle.
*  And I think that's partly for if a pet or a kid were right by the vehicle, like it wants to know
*  that. And then it has a bunch of cameras and I think, I don't know how many radars, but several
*  radars. So they have 20 or 30 sensors on the vehicle. Whereas Tesla, I think, again, I think
*  it's eight or 12, something like that. Cameras and older vehicles had one radar. And these sensor
*  modalities, I think, have different strengths and weaknesses. Like one thing radar does that's good
*  is it can tell velocity is in addition, they can like directly measure velocity in addition to
*  kind of position, which can be useful on a freeway. There are some ladars that do that,
*  but most of the ladars people are using do not have that kind of velocity sensing ability.
*  Lidar has the advantage that it is high enough resolution that it can get a pretty good 3D
*  structure for things. And they can directly sense the lidar bounces later, laser off the object and
*  the measures the time to return, which means it can do an exact distance measurement. Whereas
*  camera, of course, just gives you an image and then you have to do post-processing to figure out
*  what's the 3D structure of this 2D structure thing you're doing. And so Lidar gives you a 3D point
*  cloud that is different. And anytime you're trying to understand the world, it's useful to have
*  diverse types of data sets because they tell you different things and they're going to have
*  different failure modes. So yeah, that's why Limo does it that way. So I think I've seen
*  online analysis that I think you may disagree with that basically says the camera approaches
*  the winner, like cameras are cheap, they're commodities. The lidar is like more expensive,
*  takes more maintenance. But my sense is you don't think that's actually as big of a deal as commonly
*  argued. It's definitely true that ladars cost money and take work to install and maintain.
*  If it were the case that you could get very high quality with cameras, that would definitely be
*  preferable. I guess I think it's just important to think about it for in engineering terms. The
*  goal here is to make something very safe. And nobody has managed to make something we'll see,
*  at least we don't have clear evidence yet that anybody has managed to make something that's like
*  very clearly safe. And so if you're a company deciding there's a kind of safety versus cost
*  trade off, and you can pick different points along that, and Waymo has chosen to go with a higher
*  cost higher safety realm, there are some people who claim it's somehow like a disadvantage to
*  have lidar because the camera only for some reason like cameras let you use deep learning
*  more or something like that. And I think that's just a misunderstanding of the technology. There's
*  no reason you can't have a neural network that uses lidar as well as cameras. The big thing that I
*  think the big advantage lidar has, as I was saying before, is it can do direct distance measurements.
*  So you can create a neural network that has takes multiple images and do parallax effect,
*  compare kind of angles of things between different images and do a pretty good estimate of how far
*  things away are. And so you can generate a point cloud that kind of looks like a lidar poke cloud.
*  But the difficulty with that is that if that algorithm misunderstands what it's seeing,
*  it thinks something is an object that isn't or misses the existence of the object, then it will
*  get a wrong value for that. And the problem with that is that that is, I think, can be correlated
*  with other failure modes of vision. And so in the average case, it's going to work almost as well.
*  But what you really care about is these edge cases where something weird happens, where there's an
*  object your stack hasn't seen before. And lidar will always tell you there is something so many
*  meters ahead that's a size. And if I were the CEO of a self-driving company, I'd be really nervous
*  about doing the camera thing because it might work 99% of the time and then the 1% when it fails,
*  then my company gets a $10 million lawsuit. I think when my approach works, it makes more sense.
*  But it is an empirical question. If Tesla continues to improve it rapidly, maybe in two or three years,
*  like it'll be shown that you can do it with cameras. I'm not super dogmatic about this,
*  but they aren't there yet. And so I don't think that they've had a better case yet.
*  Mad Fientist So yeah, it seems like this may tie to a couple other
*  aspects of the overall strategy that these companies are taking. Would it be fair to say
*  that the lidar strategy is a balancing force just that might serve to even out the data
*  scale advantage that Tesla has? I guess what I'm thinking there is like,
*  Tesla's got a lot more cars on the road. It's collecting presumably a lot more episodes or
*  whatever. But if those inputs are fundamentally noisier, then maybe you just need a lot more to
*  ultimately learn what you need to learn. Whereas if you have much more precise measurements of
*  exactly what the structure of something is or exactly how far away it is or exactly how fast
*  it's moving, which sounds like the Waymo is getting all of those all the time, then maybe
*  if that's just a lot more accurate, then you have a less... Obviously, everybody still needs a lot
*  of data. I could see that if it's that much more precise, I could see that, hey, maybe you could
*  get away with an order of magnitude or maybe even two orders of magnitude less data. Does that seem
*  like a reasonable way to think about those trade-offs? Ben Leary
*  I think that's probably true that Waymo has less data, but it's probably higher quality,
*  both because they have letter and they also, because they have professional safety drivers
*  annotating why they disengaged. They gave a clearer signal for the data reinforcement
*  learning kind of thing where you have a clearer signal about this was a mistake at the car versus
*  this was the time when the driver just needed the bathroom break, that kind of thing. So yeah,
*  I would say in general, Waymo has less data, but I would expect it to be higher quality.
*  The main thing that's going on is just that Tesla's business model does not allow them to put
*  a 10,000-hour lighter in every car. And so they have to do the thing they're doing,
*  and then they're doing their best to make that work from a technology perspective. And maybe it
*  will work or maybe it won't. But Waymo's strategy is they're vertically integrated and they have a
*  fairly high margin business like tax. I guess we'll talk about that economics later, but
*  if they can get it working, it's potentially pretty profitable. And so they can just afford to buy.
*  They've only got a few hundred cars on the road so far. So it's not that expensive to put pretty
*  expensive lidar on every vehicle. And the bet is that over time it'll get cheaper. And so then it
*  won't be a big deal once they're at scale. Kyle Smedley
*  Yeah. So why, going back to the Tesla can't do it. If I understand that,
*  what you just said correctly, the case there is like at scale, a $10,000 lidar maybe becomes a
*  $1,000 lidar. Maybe that could work for Tesla. They're already not the cheapest cars on the road.
*  Oh yeah. No, absolutely. But like in 2016, when Tesla started selling what they characterized as
*  full self-driving ready thing, back then the lidar costs, I don't know, $50,000 or something. Then
*  also they put the cameras on every vehicle, but only 10 or 20 or 30 or something percent of people
*  sign up for it. And so that business model, it just would have been way too expensive to do it
*  back then. At some point, yeah. Kyle Smedley
*  Yeah. I can't sell that over the year. Kyle Smedley
*  Yeah. Once lidar scales up and gets cheap, and if it's a $1,000 sensor, then yeah,
*  maybe they will start putting it. Now Elon's pretty dug in, so I don't think he would want
*  to admit that he was wrong. But yeah, at some point lidar will get pretty cheap. And I expect,
*  we're starting to see, I don't think this has happened yet, but we're starting to see OEMs
*  planning to put lidar, other car OEMs planning to put lidar on their vehicles. I think you'll start
*  seeing lidar be a standard kind of component, like radars in a lot of cars. And eventually I
*  would expect Tesla to add it. But yeah, so far I don't think it's gotten cheap enough that
*  it would make sense. There's also different levels and kind of quality of lidar. So the
*  big spinning lidar that's on the top of it, well, that's still thousands of dollars. There are,
*  I think, some other ones that are hundreds of dollars that have less field of view, less range,
*  et cetera. And so those, I think, probably could put in a vehicle, but probably are not
*  powerful enough to add the kind of value that the big lidar and the Weymouth adds.
*  Mad Fientist Are they hard to maintain? I've also heard that this is an issue where the Weymouths
*  are going into the shop regularly for lidar maintenance, even if it's all good otherwise.
*  How big of an issue do you think that is? Elon That I don't know. Weymouth makes their
*  own lidar. And so it's pretty secretive. In the broader market, there's different models. There's
*  some that are more solid state than others. So yeah, I don't know the details, but I think it's
*  like anything else. It's probably somewhat hard to maintain now, but as I improve the technology,
*  it shouldn't be an issue at scale. Mad Fientist It's interesting how secretive this stuff is.
*  It feels like this would be the sort of business where it's hard to copy, even if you give some
*  details of how you're doing it. So given that and given the critical role of trust in a system like
*  this, am I off base for thinking that maybe they should be a little bit more transparent about what
*  is actually happening? Elon As a reporter, I would love that. I think they've been reasonably
*  transparent by the standards of technology companies. Google's not telling people what's
*  happening in their data centers. They have published a number of technical papers, machine
*  learning papers about the various algorithms that users want a couple of years ago where they're
*  using transformers to predict the behavior of vehicles on the road, stuff like that.
*  Then they do have a safety report they put out. They put several safety reports with crash data
*  and stuff like that. So I think they've published a lot of the information that you want to evaluate
*  safety. I think they've done an okay citizen on that. I would certainly like them to be more
*  transparent about a number of areas, but I don't think they've been notably secretive.
*  And Tesla has a similar story. They've had a couple of AI days or self-driving days where
*  they've provided a lot of detail. They've given talks about how various things work. So I think
*  we have a high level understanding, but the technical details are both some proprietary,
*  but also I think they're changing pretty fast. If you look at something that somebody said two or
*  three years ago, it might just not be the same as what's happening now.
*  Yeah, that's for sure. You can't go back and read the GPT-3 paper and expect to be
*  making good inferences about what's going on with the latest models. So I would assume there's been
*  quite a lot of change. It seems like the big thing has been the overall story in almost all of AI is
*  toward more and more stuff being trained into the neural nets. This is classic Elon, best part is
*  no part. Relative to early versions, I would guess there's probably been an order of magnitude
*  reduction in just how many components there are in the overall software. Is that your sense too?
*  Do we know what are the explicit things that remain? I guess you could think of that as
*  safety spec or some sort of governance perhaps, but it could be more than that.
*  Two, it's probably the kind of thing they haven't really shared. For example, how explicit do we
*  think that planning still is? I recall the one language model for lane changes or intersection
*  where lanes can get weird. Tesla showed a module where they had essentially used a language model
*  structure to figure out how does three lanes become two as you pass through an intersection and what
*  not. Previously, presumably that would have been done with a bunch of rules. I guess I'm just
*  wondering, do we know what pockets of these hard-coded rules remain today? I definitely think the
*  trend has been towards more learned systems, less hard-coded rules. Waymo's approach has been to
*  publish academic papers sporadically and not be super specific about the overall architecture.
*  I don't remember off the top of my head how recently they published something about their
*  planning stack, but they'll say here's a network we're using that does some aspect of it. But I
*  don't know if they've ever published an overall paper that says here's their overall architecture
*  and all the networks they're using and how they fit together. I think when they have something
*  that's interesting and I guess not so sensitive that they don't mind really feeling it, that's
*  when they will publish a paper. Tesla's a little different in that they are more presentation
*  oriented. There's been, like I said, two or three or four presentations where Elon and a few of his
*  top AI people will give an hour-long talk showing demos of various things they're doing and explain
*  a little bit how the technology works. But again, I don't think they've ever given a whole
*  architectural overview of all the networks or all the software modules that make up the system.
*  Tesla once famously open-sourced all their patents. Do you know what their status is on that
*  today? Are they just not patenting this stuff or are they no longer open-sourcing all patents?
*  I've not looked into that. I think that it's normal for companies to patent a bunch of stuff
*  and then mostly not sue each other over it. So that would be my guess, but no, I have not
*  looked into detail if they're still taking that open approach.
*  Yeah, interesting. I mean, these things can sometimes have very weird feedback effects where
*  I remember my dad used to say that the thing about a patent is you have to tell everybody
*  how you did it. So even if you're protecting that, you're also giving a lot of hints and
*  people can learn a lot from what you've done even if they can't.
*  Oh, you can patent stuff you're not doing. If you've got a lot of patents,
*  you can patent a lot of programs that didn't work out.
*  Yeah, interesting. What are the roles of maps in these systems? Does that
*  differ across companies? How exact do the maps have to be? How often do they have to be?
*  So this is something that I think Tesla people talk about a lot and I think is the difference
*  is probably a little smaller than people say. So classically, Waymo had a very detailed map of
*  what's called an HD map that shows at a very fine-grained level, 3D map of all the fire hydrants
*  and trees and whatever in an area whereas Tesla did not. And there's been a lot of kind of back
*  and forth about this where the claim is that Tesla is better because it can do this without it, but
*  it's not clear it actually is doing it better. But I think that so a couple things to say about this.
*  One of the I think criticisms of Waymo's approach is it's very expensive to collect the map data.
*  And I think that is going to prove overblown because you can automate it. So the first time
*  you enter a city, obviously you have to have a car driver on and collect the data. But then once
*  you have a fleet driving around, you can just use the data that you're collecting. In fact,
*  I know they did that. Actually, I visited Waymo's back in March and they showed me like hard drive
*  in the trunk that's collecting this data and they upload to the mothership every night. And so then
*  the data collection becomes trivial because you're just the cars are driving on the roads anyway and
*  you can just upload the data as it goes by. And then I think you'll be able to the other step is
*  the cleaning and labeling of the data and like integrating into the map. I expect that to get
*  more automated over time. And I don't think this is going to be a big kind of impediment or a big
*  cost factor for Waymo in the long run. And Tesla actually has that they had a tweet a couple years
*  ago where they forgot how they described it, but they like talked about how they could use
*  their map data to build a map. Now, they weren't saying they were using that for driving, but
*  they are also doing the same thing where they did an obvious thing where as their cars drive
*  around, they collect data and then they build that into a 3D model of the world that they could use
*  for simulation and for various kinds of testing and stuff. And so I think you'll see some convergence
*  here where the other thing is like Tesla just obviously uses a map for if you give it an address,
*  it needs to know which roads to take. And so it's following a map to edits. I think you can see if
*  you look at the visualization, it has some idea like where the lanes are, even in places that are
*  individual cameras, it's less detailed, but it still has a map that it's relying on. I think
*  it's something where the approaches will converge over time. This kind of goes back to the how far
*  off road can you go or whatever? Does that mean the cars have to be online to navigate like they
*  can't download the whole map of the whole United States? So do you have a sense for how they are
*  loading maps as they move around? I don't know exactly how that works, but at least right now,
*  like when I was in operating the whole United States, I think they could download the whole map.
*  Yeah. Yeah, they could go. I'm sure they have a big hard drive on there. I think they could probably
*  download all of San Francisco. My guess would be in the long run, they'll be a different car.
*  You'll have a hundred mile radius around your current location or something. And every night
*  you'll download for that. So yeah, I don't think it requires them to be online. I don't know all
*  the details of how they do those updates and stuff, but no, I think they have a local copy of the map.
*  So everything is happening locally. This is another thing I wanted to make sure I had a good read on.
*  There's been some talk, we did an episode with the now defunct ghost, which was experimenting a little
*  bit with online uses of vision language models. They had an investment from open AI and they were
*  looking at, can we use these vision language models for longer time horizon planning? The
*  reading of the road signs and figuring out which lane I should be in or where the drive-through
*  is at this restaurant or whatever, these sort of scenes that are just higher level analysis required.
*  Are any of the live players doing anything like that to your knowledge where they actually do
*  make a sort of remote call for any part of their operation? Yeah, I'm not sure exactly. They
*  definitely do have a network connection and you can do things like call customer service. I'm pretty
*  sure all the safety critical stuff is done locally. But one of the things we haven't talked about yet
*  is the kind of remote monitoring approach because the Waymo cars are quite good, but they're not
*  perfect. Sometimes they do get confused. Waymo has said they never have people remotely actually
*  driving the vehicles. There's nobody with a steering wheel and pedals. But what the vehicle
*  will do is they will ask questions or ask for confirmation. They'll say, I'm planning to do X.
*  Is that safe? And the person will respond. I think if a vehicle lost connectivity, it's possible
*  after a certain amount of time, it would slow down and come to a stop because it wants to be able to
*  ask for help. I'm not totally sure how that works. I think there were some incidents with
*  crews where that happened, where they had connectivity problems. You ended up with the
*  cars with their flashers on getting in the way. And it wasn't that there was anything locally. It
*  was just that the network was down and it was stopped out of an abundance of caution. So there
*  is definitely some interaction with the outside world, but I think they tried pretty hard to have
*  it be in a safe state where if you lose the network connectivity, it's not dangerous. It's just at worst
*  they have to slow down and come in as the driver. You mentioned crews there. Are they ever coming
*  back? It seems as far as I can tell, not at the time that they had their very unfortunate incident,
*  which I think is also directly related to this remote help. My sense at that time was that they
*  were on the same level as Waymo where they were both operating and driverless and had some ability
*  to get help. I wonder if you think that was a misperception and they were actually way behind.
*  It's crazy to me that they had one safety incident and shut everything down. It seems like it couldn't
*  have been that much of an entirely like a house of cards. They were going to have a lot of safe
*  trips too. So what's up with crews? A few things to say about that. So they were pursuing a similar
*  business model to Waymo and were growing at a similar pace. I would say industry insiders all
*  through 2023 were a little nervous about crews relative to Waymo. They seemed to have more
*  incidents. They weren't like wildly worse than Waymo, but I think it seemed pretty clear to me
*  their technology was behind, which I think makes sense because they're a few years younger.
*  I think they were under a lot of financial pressure because GM has deep pockets, but not
*  as deep as Google's. A lot of Ford had recently shut down Argo, which was their version of cruise
*  year or two earlier than this. I think Kyle Lothar, CEO, felt a lot of pressure to show
*  that this could be a commercially viable thing. So he was pushing pretty hard to commercialize
*  and turned out to be turned out to push it a little too hard. I would not say it was just
*  one safety incident. The incident that led to their shutdown was a case where a human driving
*  car hit a woman. Her body then bounced in front of the cruise car and the cruise car did not stop
*  in time, and so her body ended up under the cruise car. And then the cruise car, after coming to a
*  stop, pulled over and dragged her several more feet under the vehicle. And then when this became
*  a news story and regulators asked about it, the claim of the regulators is that they showed the
*  portion of the vehicle where the cruise hits the car, but did not show the part with the dragging.
*  Now they deny that. They say, you guys are paying attention, blah, blah, blah. But I'm inclined to
*  believe that. So there was a previous incident where Cruz was accused of blocking an ambulance,
*  where a car got stuck and the ambulance wasn't able to move. And I talked to them. They showed me a
*  video of the incident from their kind of internal God's Eye View model. And they said, okay, we'll
*  show you this video, but you cannot take a screen capture of it. And I said, can you send me
*  a diagram? So I can show you. Absolutely not. So they were like, I think they were like in
*  defense attorney node, as opposed to like transparency, make sure the public understands
*  what's happening mode. And I think that attitude really irritated, I think understandably irritated
*  the regulators. And so I think it was less that it was less that they had one mistake and more that
*  there was a pattern of not being as transparent and clear with the public or with officials or
*  journalists as they could be. And so they shut down their service. They are trying to come back,
*  I believe they have vehicles with safety drivers operating in Houston, Dallas and Phoenix right
*  now. Okay. And so I heard that. Yeah, they are planning to come back. But that puts them
*  three or four years behind. We started doing driverless in 2020. And so they're now several
*  years behind limo. And so I think they're probably plausibly still the number two company, but they're
*  pretty far behind at this point. Is there any way for us to get trajectory? When you say something
*  is like a couple years behind, you've said that about both Tesla relative to Waymo and also
*  cruise relative to Waymo. It seems like I could make a case. I wonder if you would find it
*  compelling that like, maybe they're not really years behind cruise. Like they have a PR issue.
*  They need to put some safety drivers in. But does that really mean they're like years behind? And
*  for Tesla, maybe I would just make it go back to that data case. They can collect 100x more data
*  or maybe even 1000x more data. They've got millions of cars on the road compared to,
*  I don't know how many way most there are, but it's right. That's definitely possible. Yeah,
*  I'm not saying they're going to. I'm just saying 2020 was when Waymo had the honest to goodness
*  driverless service on the road. And it's taken them three years, four years since then to scale
*  that up to still a pretty small scale. I'm sure it's possible to do it faster. But I guess I see
*  that as one of the clear milestones is the point where you take the safety driver out of the car
*  is a point where you show a level of confidence in your technology. And right now, Waymo is the
*  only company in the Western world that had that level of confidence in its technology. And yeah,
*  maybe Tesla will be able to scale it much more quickly once they reach that point. But they
*  haven't reached that point. And Waymo reached that point four years ago. Let's run through a couple
*  other live players. I always like to do the live player rundown. I'm very interested in what's
*  going on in China always. And if we could inspire anything in this conversation, I would love to see
*  us race China for self driving cars as opposed to for weaponized AI or whatever. So what's going on
*  there? Do they have a company that we should be inspired to not be left behind by? So China has
*  several I think, Biden is one of them. I honestly have not read much about those because it's just
*  so hard both with the language barrier and the fact that I can't go to China and the fact that
*  they don't have a free press. And so there's been some rumors that they like suppress stories of
*  crashes. Probably China I think is the number two country on this stuff after the US and they have
*  pretty substantial self driving car deployments. But it's not clear to me how much of those are
*  driverless or what the safety case safety records. Yeah, I can't tell you more than that. And I don't
*  know of anybody who's doing really good in the West who's doing like really good reporting on
*  this because I think it's hard to tell what the apples to apples comparisons are.
*  At just a notional level though, do I understand correctly that it is possible to get like a
*  Waymo like experience in China where you summon a car and get into it? There's nobody else in it?
*  I think there is. Yes. And I think they may be a larger scale in some places than the US. So yes,
*  I think they are. They're in the same ballpark as Western companies. A little rundown just of other
*  notable players in the space. Did Amazon hand in the game so on and so forth? Yeah. So there's two
*  other companies that are in the robot taxi game at the kind of with the kind of business model
*  and scale that women crews are one is Zoeks, which is was a startup that Amazon acquired a
*  couple years ago. The other is motional, which was created a long history, but it was like an
*  active subsidiary. And then they brought in Hyundai as a investor. And then I think after
*  got itself bought out anyway, so now I think it's a Hyundai subsidiary. And they are both
*  at the stage of kind of testing the technology, but have not started doing driverless or commercial.
*  And I'm like interested in what they're doing, but I've not written about them much because at
*  this point, I guess like I start taking companies seriously when they start having driverless,
*  because I think that's now the cutting edge. And so I think they're a little behind, but certainly
*  Zoeks just with Amazon behind them, like they're going to have resources as long as Amazon wants
*  to have them. And so I could see them being the fast follower of what most of success like people
*  are going to want alternatives. And so that's who they might look to. There's a startup called WAVE,
*  W-A-Y-V-E in the UK that raised, I think, a billion dollars a few months ago. And they have
*  an interesting approach and they're doing the kind of end to end approach we've talked about. I believe
*  they actually have a foundation model type thing that has in addition to driving data also has
*  some like text and images and stuff. And you can talk to your self-driving car. Apparently demos,
*  people have been impressed by demos, but they're again, early enough that it's hard to evaluate.
*  I haven't been to the UK and to try it out, but that's, there's certainly somebody worth watching
*  and their business model is they, I think are hoping to license to OEMs as an alternative to
*  test life. If you've got, if you're afforded Toyota and stuff or somebody and you say, we don't,
*  we don't have our own homegrown version of autopilot, maybe that WAVE will be able to
*  supply them with a competitive version. And then two other companies that I would mention,
*  there's a startup called Aurora that I still used to have the same business model that WAVE is
*  talking about now where they licensed OEMs, but a couple of years ago, they pivoted to trucking.
*  And there's a couple of other companies that are doing trucking that I think Aurora is probably
*  the most important. And so Aurora says they're preparing to do long haul, like 18 wheeler trucking
*  routes, I think between maybe Houston to Dallas in Texas. And they say they're going to do it by
*  the end of the year. That's another case where I think I would be nervous if I were the CEO of a
*  trucking company because the failure mode, there's a lot of math. Yeah. And so that's not where I
*  would like to stay, but I hope they, they managed to make it work. And then the final one is a
*  company called Neuro, which was started by a couple of guys who left the Google self-driving
*  car product like seven or eight years ago, and they are making street legal robots. So there's
*  sidewalk robot companies that are very small and slow, but these are smaller than a compact car,
*  washing machine size vehicles. They go 20 or 30 miles an hour and I think could go faster
*  that don't have a driver or anything. It's just a delivery robot and it's used for delivering pizza
*  or groceries, things like that. And they've been on the verge of commercialization for several
*  years. It seems like they've done a bunch of pilot projects. And again, it's not totally,
*  they're one of the ones I'm most confused about because it seems like that should be an easier
*  problem. So you don't have to worry about safety as much, at least for people inside the vehicle,
*  since there's nobody in the vehicle. I've heard that one of the issues they have is finding for
*  regulatory reasons, there's limits to how fast they can go because they're in a category that's
*  not designed for like freeway speeds. And so finding a neighborhood that has a right mix of
*  a grocery store and then some residential streets and you don't have to go through any
*  like high speeds. I've been told that's one of the issues they're having, but that's another
*  company that's working on self-driving, but not building a taxi service. Yeah. I think that's a
*  great little glimpse of the future. It's just that the form factor of the car could get a little of
*  the vehicle could no longer a car at that point could start to look really different if you
*  don't have to have a driver sitting there and in the normal posture. You could imagine people
*  sleeping in cars or whatever, but then also you can just imagine small things that just don't
*  take people at all. I think that's possible. Cambrian explosion of very different looking
*  things on the road is like a cool future to imagine. Yeah. 100%. So let's talk about these
*  safety statistics. Like where are we on this? It sounds like we probably only are far enough along
*  on a couple of companies to even have a sense, but my kind of qualitative sense has been that
*  the companies seem to be reporting that their products and here I mean in Waymo seem to be
*  reporting that their products are safer than human drivers, seemingly substantially. And then
*  my mental model of this has always been like, I'm not sure I should take that fully at face value.
*  So I'll discount it, but even if I discount it, I seem to, I feel like I get back to basically
*  like similarly safe to human drivers. If I just sort of discount whatever percent. And then
*  if I ask myself, okay, well, if they're already similarly safe to human drivers, like why don't
*  we adopt them more? I assume that it's just a quirk of society that we are going to insist
*  the AI powered technologies are not just on par, but are actually like a lot safer, maybe like
*  order of magnitude safer than human before we would actually all agree that this is something we
*  should go forward with. How would you complicate that story? Is that a good summary? Maybe you can
*  get more specific in terms of the metrics or how we should be thinking about these. Obviously
*  metrics are always complicated when you dig into them. So a lot, there's some things I disagree
*  with. So let's start with, let's just set the baseline for what human beings do. So the most
*  important thing as statistic, I think is that there is a human driven car is getting a fatal accident
*  about once every a hundred million miles driven and Waymo has driven about 20 million miles. And
*  so they are not yet at the point that they've had zero fatal crashes, but that is not yet at the
*  point where you can say anything about, are they safer? Because you would expect a fraction of one
*  death for the number of miles they've driven driverlessly. The other two, I think statistics
*  that are helpful. One is crashes with injuries, which are in the ballpark of a couple million
*  miles per crash like that. And police reportable injuries or crashes, which are serious crashes,
*  but not necessarily crashes that have once involved property damage, but not necessarily
*  injuries. And like I said, Waymo has zero deaths. So they have a perfect record, but there's not
*  enough data to really say much on injuries. Waymo had a report last December where over
*  7 million miles, they had two or three injuries. So that's every an injury every 2.4 million miles.
*  I think that works out too. And they did some statistical analysis of human drivers on comparable
*  roads in the same metro areas, same kind of roads. And they worked out to run once every 350,000
*  miles. And so they're like maybe five times safer on a per injury of her injury crashes.
*  And then police reported crashes, it's two and a half times safer. It's half a million
*  miles per crash for the Waymo's and 200,000 for the for human drivers again, in very broad terms.
*  And I think that's good. I think that's pretty impressive. And but I think it's I think that's
*  decent evidence that they're safer. But because we haven't gotten to the fatal ones, and that's
*  really what you really care about. Like you'd hope that they're all correlated, you'd hope that the
*  fact that they're safer on the lower severity crashes means they're also safer on the higher
*  severity ones. But higher severity ones are so rare that you can't say that for sure, because
*  there might be some kind of random bug that happens every 50 million miles, they get somebody
*  killed that just isn't correlated with the lower. So I think, I think that to some extent, the jury
*  is still out. My guess is they're safer, probably by a significant margin, but we're going to need
*  two or three 400 mile million miles of on road driving before I think you can really say there's
*  a statistically significant. One of the things that I've been pretty impressed with the transparency
*  of Waymo's, I mentioned the 7 million mile study, they also did a study when they got into 4 million
*  miles, where they partnered with Swiss Re, which is a insurance re insurance company, they provide
*  insurance to other insurance companies. And so because of that, they have a database of every
*  insurance report ever filed in the auto industry in the United States, going back some number of
*  years. And so they're able to do, they're able to look in their database and say for the specific
*  geographical areas where women was operating, they will list of like all the crashes, and they're
*  able to do apples apples comparisons. And they had a similar thing two or three times safer than
*  a human driver based on injury crashes and kind of police reportable crashes.
*  That's compelling coming out of Swiss Re who presumably has to ultimately price the insurance
*  for this, right? Strong incentives to be right in their business. Yeah, and strong incentive,
*  I think, not to put their name on it unless they think that the evidence is credible. If I think
*  that was a smart thing for Waymo to do is obviously a company puts out data saying we're very safe,
*  you're going to wonder if they could put the data and so they can find third parties who are willing
*  to look at the data themselves, maybe supply some of the data themselves and then put their name out.
*  That's compelling. Tesla is a hard I do not think Tesla has been as transparent about this.
*  They have a safety website where they say that drivers with autopilot crashed once ever 7.5
*  million miles, which is significantly better than human drivers. The problem with that is we don't
*  know the distribution of those miles, both plus one thing, one of the big things that actually
*  we should talk about a little bit more in general is there's a big difference between freeways and
*  city streets. Freeways are easier in most ways, like crashes are much less common on freeways,
*  but freeways are also where most of the worst crashes happen, right? The fatal crashes are much
*  if you get in a crash and the freeways must like more likely to be a fatal crash.
*  And so the fact that Tesla is much safer, has a lower rate of crashes might just be that people
*  are turning autopilot on and the kind of the safest environments and turning it off in like
*  more difficult environments. And Tesla has not done the kind of thing when what it's done where
*  they've given the data to independent experts or brought in third parties to allow people to try
*  to control for that kind of thing. The other source of data we have about Tesla is disengagement.
*  And so there's a crowd source site that where people like upload videos or records of their
*  drives. And right now that's showing that the latest version of FSD has a disengagement about
*  once every 300 miles, which it's hard to think about that because on the one hand, that's pretty
*  good. That's a lot of miles. If you drove a car for a hundred miles and it didn't make a mistake,
*  that would you'd be pretty impressed. But as I said before, Waymo nine, eight years ago was saying
*  that they were going 5,000 miles between disengagement. So the human drives are actually
*  quite good. And so making a mistake every 300 miles is like not, I think still not close to human
*  level performance. And I think this is actually, this is a pretty common thing is I frequently
*  see people say, wow, I took a test drive and it was so amazing. And how many miles? Like 20 miles,
*  like that just 20 miles a day. If it does a perfect drive for 20 miles, that tells you nothing about
*  how good it is. You need to drive it for thousands of miles to know if it's human level. Because
*  the average human driver 99% of the time, if you do a 20 mile drive, but that is not going to be
*  have any mistakes. I think Tesla is definitely making progress. And the other thing is that's
*  crowdsource. So again, there could be big self-selection issues where maybe people are
*  more likely to turn out a pilot or FSD on roads they know work well and or on any easier roads.
*  I think it's hard to put like too much stock into that number. It's wild to me that there's not
*  more there. It's just such a strange, it's also like maybe an argument for a lot of the
*  complaints that we hear about everything is overregulated and you can't do anything. And
*  it's all, we're all just handcuffed by the government. Maybe that's the lie. And this
*  sort of puts the lie to that. Like they're with this, with that, even a good safety report and
*  we're all just tolerating it. Yeah. So I was, yeah, I should answer the second half of your
*  previous question. Yeah. So one thing that has happened recently is the federal regulator on this
*  stuff has started requiring companies to report more crashes. And so we now have better data,
*  I think across the whole country. We used to have only in California. California had good data
*  because the state regulator required it, but now the whole country does. We don't have actually is
*  like the denominator. We don't know how many miles Teslas or anybody else is driving. And so you can
*  probably look and see how many Tesla crashes there have been, but you don't know how many of those,
*  how many total miles Teslas are driven or how many FSD was turned on or where they were driven.
*  And so I would, yeah, I would absolutely like to have more, more regulation, but I do think,
*  so you were saying like, it seems like society is like resisting this. I really do not think
*  there's much in the way of policy barriers here. California regulators recently gave Waymo approval
*  to operate all the way down the San Francisco peninsula, down into Silicon Valley. That was
*  several months ago and they just haven't started doing it. And I think the reason is that they,
*  and this is something you should talk about, is they don't do freeways yet. And I don't think
*  there's any regulatory reason. I think it's just that Waymo is not confident they can do freeway
*  safely. And I think it's a combination of kind of caution and safety, like they're doing the
*  things they think can do safely, but they don't quite think they have it a hundred percent.
*  But the other thing is that just because they have a vertically integrated business model
*  where they're owning the cars, they're building depots to charge and clean and repair them,
*  et cetera, it just takes a lot of time to just do the work. And so they were in only in Phoenix
*  two years ago, then they did San Francisco last year, 18 months ago. And now they're doing
*  Los Angeles and Austin. And they've grown like three to five X in the last year.
*  And if they continue growing at that rate, then in five to 10 years, they'll be nationwide.
*  But I think they just, you look back at Uber and Lyft, it took them a few years to go from just in
*  San Francisco to nationwide. And so I think Waymo is growing close to as fast as you would expect
*  for a company that kind of thought they had a successful product. And it's just going to take,
*  because of the business model they have, it's going to take them a while. Now, obviously,
*  if Tesla could just push out a software update and say, okay, everybody's driverless, they can do
*  that very quickly. But I don't think they're ready for that, technically. I'm not actually sure if
*  there'd be a legal restriction on doing that. I don't think there would be. I think it's,
*  at least I don't think that's the main issue. Yeah, that's fascinating because we do hear that
*  so much from Silicon Valley in general, right? This sort of narrative is so often repeated at
*  this point, right? Where everything's, we can't do anything with atoms, right? It's a, we all
*  move to bits because we can't do anything with atoms. Now here we have a very regulatable
*  suable, by times upwards of a trillion dollar company that is just doing it and nobody's really
*  telling them no. And again, even without what I would consider to be just like the sort of safety
*  transparency that I would expect from pure market discipline, honestly, it was like a consumer
*  reports basis. I would expect to see a little bit better numbers than it sounds like.
*  If you'd asked me 10 years ago, my expectation would be okay, they'll build the technology and
*  then there'll be some kind of regulatory process. I didn't know as much about the regulatory state
*  at that point. I think there's a couple of things going on. One is that like just the auto industry
*  has traditionally, but worked on self-certification. So NHTSA publishes a big thing called the federal
*  vehicle motor safety standards. It just says, here's all the things your cars have to do.
*  And when a car maker makes a new car, they're supposed to go through the list, test to make
*  sure it meets all that, and then file a report with NHTSA saying we meet all these requirements.
*  And so what Waymo does is they buy a vehicle that's already certified and then add some sensors and
*  compute in the trunk. But because it's already certified, they just meet the requirements by
*  default. And then the second half of regulation is states. So the federal government regulates
*  vehicle design. States regulate drivers, which until recently was human drivers, and driver's
*  licenses and traffic laws and stuff like that. And so there is some variation in the strictness of
*  different states. And so California is one of the strictest. They do have reporting requirements.
*  They do require a license to do various kinds of testing. But it hasn't been that hard to get the
*  licenses. And like I said, they're the strictest. So like Texas is much more wide open. It's pretty
*  much anybody can do anything. And actually, you do see like Cruises not going to Texas,
*  because I think they found California to be a little too restrictive. But they're not launching
*  a huge network. I think they're mostly still worried about we'll get sued if we get in a crash
*  rather than regulators come down on us. And in the Cruises case, did the regulator even
*  tell my understanding was that they voluntarily stopped their operations without being
*  forced to do so? Is that right? I think the California regulator did ask them to stop.
*  There was a crash in August involving a fire truck that I think the cruise was not a fault.
*  But there was some question about whether it could have handled it better. And they were asked to
*  reduce their fleet by half in August as they and then there was an October crash. California,
*  I think, asked them to stop. But then they voluntarily suspended their other operations
*  where they had I think Austin and Phoenix, and they voluntarily suspended that. So it's a mix.
*  There is some pressure from regulators, but it's definitely not like Cruises like anxious to get
*  going and the regulators won't let them. Yeah. So going back to the original, like the gold
*  standard of safety data right now comes from Waymo. And is it fair to say that you apply a
*  discount to that? Do you take it at face value? Would you say their reported number is like your
*  point estimate for how safe they actually are? So it's funny, like the tricky thing actually is
*  that like a crash is a pretty clear cut thing. And they have a lot of sensors and a lot of like
*  personnel. And so I think it would be pretty hard for them to fudge their like crash data.
*  The hard thing is actually knowing how often humans crash. Because if you look at the data,
*  they'll have things like we side-sliped a shopping cart, or we got in a pothole and got a flat tire,
*  or things like that. Or I think there was an incident where like a skateboard ran into a cruise
*  car that was stopped. Or actually, there's a bunch of ones where they're like parked in another car
*  bag. So all those things are in the Waymo and cruise safety report. So we know every time that
*  a Waymo or cruise car collided with another vehicle or another person. What we don't know is how often
*  that happens to people because if a person side-slips a shopping cart, they're not going to stop and file
*  a police report. They're just going to move on. And so part of the trick actually has been like
*  collecting the data. So one thing cruise did a while back is they had this service called Maven.
*  It was like a rideshare service or a zip car style car rental service. And they had some of those
*  vehicles outfitted with sensors so they could collect. They would rent vehicles to Uber drivers
*  and then use sensors to collect data. And so they had a database of all the crashes that happened for
*  Uber drivers. Anyway, so yeah, I'm pretty high confidence in the quality of their data,
*  on their crash data. And I think their safe director is not that much better than the national record.
*  But because a lot of their stuff in San Francisco, they try to get like San Francisco specific data,
*  which is I think it's much more likely to have crashes in San Francisco because it's like high,
*  low speed, dense urban situation. And yeah, I'm pretty, I think that that it's very likely true
*  that there are two or three times less likely to have police reportable injury crashes than human
*  drivers. And I think based on that, it seems pretty likely that they are less likely to have fatal
*  crashes, but we can't say much about that because we don't have enough data yet. So the highways
*  thing remains like one big barrier to like super broad adoption and I guess maybe just even
*  manufacturing bottlenecks and whatever. But yeah, if that is all true and seems very reasonable to
*  at least have a not super wide confidence interval around that, given everything you just said, then
*  why isn't there more like enthusiasm for this? If Kennedy were president, he'd be like giving a big
*  speech about how we've achieved this modern technical marvel and like life is going to change.
*  And I don't know if you have a stat on this, but like people spend a lot of time driving,
*  the pure hours that you could get back in some sense to read a book or whatever, if we could
*  really bring this thing online. We just talked about it, it doesn't feel like it's the regulators,
*  it feels like it's the culture. Like what's going on with the culture?
*  As a person who's written about this beat and wanted people to be excited about this,
*  this is something I've wondered about for a long time. I think the expansion, I don't think,
*  the sole expansion is not about lack of demand. I think it's about the stuff we talked about.
*  Basically, the technology doesn't quite work and it just, it takes a lot of work to expand it.
*  I think that's the main thing. I think the fact that it's geographically limited does
*  make it hard for people to think about clearly. Everybody's assumption, including my assumption,
*  when they first hear about self-driving cars, oh, it's a car you'll buy and you'll push a button
*  and it'll drive itself wherever you want to go. And for various reasons, that's not how it works.
*  I don't think it's how it's going to work. But then people put it in the bucket of, oh,
*  that's like a research prototype or a thing that's not ready for prime time. So that's one of them.
*  But I also think that the freeway thing is really important. So I think we should talk about this a
*  little bit. So Waymo's safety strategy is basically if you're not sure what to stop.
*  And on city streets, that works very well. And then they try to get that rate of stopping
*  low enough that it's not annoying other drivers. And that's worked very well for them. That doesn't
*  really work on the freeways, right? Because if you're going 70 miles an hour and there's a lot of
*  other cars on the road, if you slam on the... Number one, it takes longer to stop. So you're
*  not going to be able to stop before you get to whatever the problem is. And then somebody
*  might rear end you and it causes a traffic jam and stuff. And so that's why it's taken them longer
*  to get to freeways because they still need to get to what's called a minimum risk condition.
*  But that means getting to a shoulder or getting to an exit. And so that might mean you have to
*  drive for a half mile or something. And so that's just a harder problem. And so they're working on
*  that. They started testing on freeways in the Phoenix area earlier this year. And I hope that
*  means that in a few months, they'll be able to start... But not commercially. I hope that
*  means in a few months, they'll be able to start doing commercial freeways, but they haven't yet.
*  And this is actually another reason they haven't expanded is that it's not a very
*  compelling product if you don't do freeways. When I was in San Francisco, something I would do is
*  anytime I would book a Waymo ride, I would also pull up my Lyft app and pull up the same ride
*  and look at the time and the cost. It was also a little more expensive and it was always five
*  or 10 minutes slower. And... Waymo is more expensive? Waymo is a little more expensive. Yep.
*  And Waymo is also slower. If it was along a route where the Lyft would have taken a freeway,
*  it would be a lot slower. Even if there wasn't a freeway, it would still be a little slower.
*  And I think that's just because it's a cautious driver. It'll follow the speed limit and not run
*  around the lights and stuff like that. But it can be a huge difference. So there's a video a few
*  months ago where somebody did a test drive of Waymo versus Tesla in the Phoenix area. They took
*  the longest route you can do in the Waymo service area. And it was like a 2X difference. It was like
*  20 minutes and 40 minutes because the Tesla got on the freeway and went all the way in the freeway.
*  And the Waymo was going on service streets the whole way. And so it's just not a very compelling
*  product. I think they have plenty of demand because it's a novelty and people... And I think
*  safety benefits and some people like not having the driver, but there's this offsetting factor of
*  it's just not as fast as a human-driven car. I think that'll go away once they figure out freeways.
*  But right now, they want to be ready for expansion and they want to be collecting data. And so they
*  are expanding. But I think the really fast expansion will happen after they figure out
*  freeways and some of the other things. So this actually has the chance to be a profitable service.
*  I don't think it's not going to be profitable until they figure freeways out.
*  Yeah, it seems like that... It's funny. These sort of mirror image approaches of each other. It seems
*  like that can't be too far off. Coming back to the culture or the politics of it, what would
*  a warp speed look like for this? If I was to make a late push for the Democratic nomination,
*  would I show up at the open convention and say, hey, here's my platform. Here's what we're going
*  to do to actually bring self-driving cars online up. We can suspend disbelief and assume people
*  actually want that. Is there something that we could do as a more society-wide level to say,
*  let's enable this technology. Let's not make it learn or deal with every quirk that we have.
*  Maybe we could clean up our system a little bit and make it a little bit more friendly. What would
*  that look like, if anything? I don't think there's a ton that you do. Certainly, you could cram some
*  state and local regulations. I don't think those are a huge factor. But for example, in California,
*  there's been a big fight over individual localities want the ability to license and approve these
*  things. The state has preempted them, but I don't know if that fight will continue. You certainly
*  have federal regulation that says you have to allow it in every location and maybe move regulation
*  to the federal level so it's a little easier. I don't think it's a big factor though. I've heard
*  you mention on previous podcasts that maybe we should change the built environment. I don't
*  actually think that is very important because the hard thing is not figuring out where the lanes are,
*  where the stop signs are. These vehicles are all very good at that. The hard thing is, like I said,
*  the edge cases, the crash sites. There was a funny case where crews drove into wet cement.
*  I really liked another callback. You had Martin Casado on the talk about like Faddale distribution.
*  It's really that. There's lots of just weird situations in the world and you have to be ready
*  for all of them. And having self-driving only lanes or putting sensors on the roads or anything
*  like that wouldn't hurt. But I think I don't have any confidence in the government's ability to do
*  that quickly. And I don't think it would add very much value because the kind of common cases are
*  not the problem. If the road's empty or traffic's flowing smoothly, it's pretty much perfect. It's
*  when weird stuff happens. And I don't think there's anything you can do to the infrastructure to make
*  weird stuff not happen or make it easier to deal with. Actually, one other thing that I do think,
*  so another set of things that have been happening in San Francisco that would be good to replicate
*  is the interaction with law enforcement and first responders is very important. So one thing that
*  Waymo recently added is the ability to, for the like the San Francisco 911
*  or the fire department to like geo-fence an area. So this is a fire zone. So keep vehicles away from
*  it. And then Waymo cars will automatically route around that. And they've also been struggling with
*  the interface. So if a car gets stuck, one thing that's nice is the firefighter can just jump in
*  the driver's side and drive the vehicle. So having those kinds of standards of here is how
*  government can signal cars where to go. And here's how they can take control if it gets stuck. And
*  that kind of thing is the most useful thing at their federal level is both do some of the
*  federal level and also develop standards for state and local governments. So I would say that's the
*  big thing, but I don't think this is the main issue. I think the main issue is just like
*  technology and then figuring out the business aspects of it. So bummer. I was hoping there
*  would be some platform for me to run on. But it's coming. It's not like nothing's happening.
*  Right? Like Waymo, as I said, I think they were doing about 10,000 trips a year, a week and a
*  year ago, and now it's like 50,000. So another five X growth a year for two, three years, and it's
*  going to be a significant thing. Like I would like to get a little bit faster, but it's not,
*  yeah, it's not the thing like it's stuck. It's just that the US is a big country. So it takes a
*  while to get to everybody. I do something of that stop sign. And there's also a true stop sign.
*  That's behind a branch of a tree on my way to the highway, which my friend who lent me the Tesla
*  specifically called out and was like, because you live here, that there's a stop sign every quarter
*  in our neighborhood, but it misses that one every time. And so you're going to have to watch out
*  for that. I do feel like there is something there, especially if we're getting into like really long
*  tail things, just make sure the signs are all visible. But this is why you need a map. This is
*  why it's helpful to have a map is like, Waymo has the map and I assume that stop sign is correct
*  there. The thing to do there would not be to put, to do anything to stop signs. It would be like
*  publish an accurate database that says here's all the maps with their GPS coordinates and
*  there for whatever. So that could be a good thing is if the government provided data to companies
*  that said here's all the traffic rules and places you're supposed to stop and stuff that could work.
*  So yeah, I'm not opposed to that. I think it would definitely be like in general, just be nice to
*  stop signs were not covered up, but that's like a 2% faster kind of thing. That's not the main thing,
*  holding things back. Yeah, gotcha. Okay. In terms of the market and how things develop,
*  going back to really where we started, there's these competing visions of a car that you buy
*  and own like a standard car today that drives itself. Obviously that's what Tesla's pushing
*  toward. And then we've got the robotaxi service. To what degree do you think those remain like
*  separate things? Obviously we've heard from Tesla that they have plans for robotaxi.
*  I don't know what would limit to the car companies want to sell cars. I think they might be scared
*  by the idea that, geez, if utilization of cars goes up 10X, what does that do? Demand for cars.
*  I would imagine if a Toyota or a Ford wanted to do a deal with Waymo, there would at least be some
*  strong reason for them to think, can we make this something that people can have parked in their
*  driveways most of the time instead of actually on the road all the time? Yeah. Yeah. Do you see
*  like a convert? Is there a possibility of crossover or do you see convergence or are these kind of?
*  So I used to be one of these people who thought that self-driving is going to mean that nobody's
*  going to own a car. And I've chilled out on that a little bit because I think people really like to
*  own cars. You've got car seats or you like to have your golf clubs in the trunk or you just like
*  the security of knowing your car is in your driveway and it'll be ready whenever you need it.
*  So I do not think car ownership is going away. Although I think it will probably get as taxis
*  get cheaper, which I think self-driving will make it like the equilibrium will be such that there's
*  fewer own cars and more taxi rides. But the way I envision this market working is I think that you
*  are going to need support infrastructure maps, but also other kinds of things anywhere that a
*  level four self-driving car operates. And so I think what you're going to see happen is Waymo
*  will expand nationwide. You'll have a taxi in every area. And then once Waymo's service area is
*  50, 67% of the country, then Waymo can go to an OAM and say, how about if you add a Waymo service
*  where it's a hundred bucks a month and then your vehicle has built in like the Waymo service where
*  you can subscribe to that and then you push a button and it'll drive itself. And I think that
*  will probably take 10 years to get to the point where Waymo is able to offer that. And maybe
*  somebody like Wave will get there independently. Going the other way, I'm pretty skeptical of.
*  Tesla claims they're doing a robotaxi. I think you need that infrastructure. Tesla's are going
*  to get stuck sometimes. And if there's nobody in the car, because Elon has this vision that you'll
*  buy your Waymo and then go on vacation. And while you're on vacation, your car will be driving around
*  earning money for you. But what if your car gets a flat tire? Like you're not going to come home for
*  your vacation and fix a flat tire. Like presumably Tesla is going to have to send somebody. And it's
*  not like it's impossible for Tesla to build that infrastructure, but that's like not the business
*  they're in. And they certainly, I don't think have started like building that infrastructure.
*  And so I think it'll take a few years at least for Tesla to be ready to offer a Waymo taxi service.
*  And yeah, I'm not sure they have the corporate culture or the infrastructure or anything to do
*  that. And we'll see. I guess I don't, I'm not that optimistic about the robotaxi part of that. I think
*  that they're more likely to stick with the service they have now. And maybe at some point they'll be
*  ready for driverless, but I think it's probably a few years away still. Who do you think does have
*  that culture? Cause I wouldn't think of Google as being like the obvious company to really want to
*  handle all the flat tires. Uber puts that in their drivers laps, right? Yeah. No, I think it's probably
*  going to be, I think that's a big open question. Definitely. I do think one of the other reasons
*  that Waymo may be growing relatively slowly is that Google has always operated in high margin
*  businesses where massive scale software. And so they just pay top dollar for the best talent and
*  don't worry too much about like individual productivity. They're not like scrappy the way
*  Amazon is. And so I could see, totally see a scenario where they, their technology works
*  perfectly. They're not making any like mistakes, but it's just everything costs like 50% more than
*  it would if Uber were doing it. Or you actually see this to some extent with Uber and Lyft as well,
*  where Lyft takes like half of every fare. And it's because they have this building of 5,000 software
*  engineers. That's actually like a large fraction of Lyft's revenue. So I do think that companies
*  are going to have to figure out how to be a little leaner for it to run in this kind of more
*  cost conscious market. And I can imagine a number of ways, maybe Waymo have some kind of franchising
*  thing. So a while ago, they had to deal with Avis to help them manage some of their vehicles in
*  Phoenix. I think this was the 2018 time period when they thought they were going to scale rapidly. So
*  I could see them either licensing their software to other people or having some kind of franchise
*  model or some kind of, I don't know, there's lots of different ways you can imagine, but I'm sure
*  that there won't be like the nationwide Waymo network. I doubt it will be like all like Waymo
*  employees doing everything. I'm sure they will have some kind of partnerships with other country
*  companies. Uber is a good example. I do also think getting the two sided market of rideshare
*  to work and build it up is very expensive. Uber and Lyft spent a decade spending billions of dollars
*  to do that. And so one approach would be just you make Uber the partner, right? And I don't know if
*  Uber owns the vehicles or maybe the third company that owns them. But as the ride hail app, like
*  maybe in the future, like actually most of the Waymo vehicles are dispatched through Uber and
*  Lyft. I think that could be fine. So yeah, in terms of the market structure, I think it's very
*  much an open question. And I don't think Waymo, because it's not actually a profitable business
*  yet, I don't think Waymo is like thinking super hard about this. The easiest thing for them to do
*  is just to run their own ride-hailing service. And maybe that'll work. But once they get to,
*  okay, like this is actually like a viable service, which I think is probably a year or two away,
*  then they'll start thinking about how do we scale up really fast. And that probably will mean
*  finding partners or thinking about other business models.
*  Yeah, Amazon definitely comes to mind there is somebody that already manages like a million
*  vehicles and has a pretty good reliability rate for making sure the package ends up on my porch
*  and dealing with it when it doesn't. So yeah, in some ways that's really in their wheelhouse.
*  Yeah, I can see a world where a year from now, Zucs starts doing driverless, and then they scale
*  it much faster than Google. And so they end up being as big as Google, as big as Waymo five or
*  10 years from now. Yeah, that's one reason I wouldn't count them out is they have a lot of
*  those expertise that Google doesn't have. Are there any other surprising scenarios that you
*  think are underestimated? Like one that I just came up with in preparing for this was Tesla
*  currently charges $15,000 for the feature. An argument could be made that they should just
*  give it away to scale even faster and try to dominate and then figure it out later. They
*  can always charge again later. I don't know if you think that is at all realistic. And then I also
*  wonder about just like weird partnerships, alliances. This is something I've been really
*  struck by in the context of AI in general is just how we've got OpenAI partnered with Microsoft and
*  Apple at the same time. Like what? I never thought I'd see a single core technology provider could
*  play both sides of that divide. So yeah, is there any... And also at the same time, their core
*  product is free, right? You can go to Chad GPT and use GPT-4.0 for free. And yet they've managed to
*  do these strategic partnerships. Is there a move there that Tesla could make something free and
*  partner with Ford or whatever? I don't think that the cost of FSD is their main bottleneck.
*  The $15,000 is just a way like when Tesla was a kind of desperate situation, three to five years
*  came from a cash perspective. This is a way to raise cash. And they are shifting to a monthly
*  model. Like you can get $100 a month at FSD. And I think that probably makes more sense in the long
*  term. I think that's right. Yeah. Per month. I think that probably makes more sense. It's going
*  to be a service, not just like a piece of software you buy one time. So I think that does make sense
*  to have a recurring kind of revenue model in terms of like other ways the market could unfold.
*  So to some extent, I think that the kind of crazy wild west bunch of money flowing in period
*  that in self-driving was that like 2016 to 2018 period. And I think there's been like,
*  I think it's like probably five years behind the kind of generative AI. And I think that
*  there was some of that kind of stuff happening back then, but then a lot of those projects just
*  went out of business. And I don't expect to see a lot of that the way we do now. Obviously once
*  if Waymo becomes very successful or Tesla or somebody, then a new generation of startups
*  might come in. But right now it's just, I think in a consolidation mode where the companies that are
*  left are just hanging on trying to survive. So the non Waymo ones, it's just can they get to market
*  at all? And so nobody's going to want to put new money into them until they show some success.
*  And the question is, yeah, can they survive or do they go out of business?
*  Kyle Sivers There's sort of an analogy there to the large language model market, I would say,
*  which is this has happened in compressed time, but just over the last couple of years, you've
*  seen this obviously emergence of like very notable leaders with compelling technology,
*  a bunch of people who have raised like very significant money to try to get into the game.
*  And it seems we're already hitting a period where that second tier is being thinned out. It's almost
*  like the history of self-driving has like rerun for a large language models in 10% of the time,
*  or maybe 20% of the time. Kyle Sivers
*  Yeah, the current large language model market feels a lot like that early self-driving market
*  to me. There's a lot of, I have trouble working out the kind of math of the second, third, fourth
*  tier LM companies, like how they're going to make a profit. Like I'm sure one or two of them, but
*  there were a lot of self-driving companies that were just like, we're doing self-driving and
*  they were like the sixth or seventh best self-driving company and they didn't make it.
*  And so I would not be surprised. And I also see a similarity in that this kind of long tail problem
*  where people like all of them can do 90% of X and how hard can it be to the last 10%? And what you
*  learn is self-driving is that last 10% or last 1% really hard. And I expect to see some of that. I
*  don't think we'll see the same degree of crash because clearly there are some things customer
*  service automation and various kinds of documents. So I think there clearly is our useless problems.
*  I don't think they're going to go away. But yeah, the crazy evaluations I think are going to be hard
*  to justify. And I definitely expect some consolidation or some of the kind of second
*  tier companies to go out of business in the next year or two. Yeah. I think there's a musical chairs
*  game that's already underway and the music is, doesn't seem like it can play that much longer
*  for a lot of these second tier language model companies, which is not something I take any
*  pleasure in coming to that conclusion, but it does seem hard to argue otherwise at this point.
*  Yeah. I'd be interested to hear a little more. I know you have a map from,
*  that goes a little, I think a little deeper, even than what you just said on what your expectation
*  is for like future of AGI and whatever. I would put a little pin in that I think it is a lot easier
*  to control the environment for language models. And that is a skill set that if we do in fact,
*  see this stall out that some are predicting, which I don't predict to be clear as I think,
*  yeah, we're just stuck at GPT four plus a bit. Then what I would expect to happen over a long
*  time is this kind of FSD sort of slog, except instead of grinding out for all of the additional
*  nines that you need for a functional FSD product. I think what we would see in the language model
*  side is like a lot of systematically sanding down rough edges of different business processes
*  so that you can reliably feed the language model something that it can handle. And in that way,
*  you can probably automate still a ton of work across the economy. It's just that everybody's
*  in this moment now where we're not used to the technology and there's the expectation that it's
*  going to get a lot better and a lot easier. So do I really want to put in all this elbow grease now
*  to scaffold this thing up and make sure that I have it dialed in when I can maybe just wait for GPT
*  five and maybe it'll solve all my problems. But it sounds like you don't think that GPT five is
*  going to solve or even six is going to solve all our problems based on your decade following self
*  driving. Yeah, I don't have a super strong prior about this. And I do think the one obvious
*  difference between LLMs and cars is LLMs don't kill anybody. And so really hard thing about
*  self driving is it has to be close to perfect or you don't have a product at all. Whereas with LLMs,
*  there are, as you say, there are some, either some narrow domains where you can get it perfect
*  even now or domains where there's a human being checking the output. And so it's fine if it makes
*  mistakes sometimes. And so I definitely expect there's enough business processes and kind of
*  small scale stuff that there'll be a profitable business for somebody. But the hopes of the really
*  big stuff where we're going to have AI doctors or AI lawyers or programmers, things like that,
*  like, I guess one of the similarities I see is that the, I think people may be underestimating
*  how much the hard stuff is different from the easy stuff. People see, okay, Tesla can drive on the
*  freeway. And so we're like almost how much harder can it be to do cities or to do crash sites or
*  things like that. And similarly, like the routine doctor's visit, I think you can do pretty much
*  with kind of a checklist. But then part of what's valuable as a doctor is they'll recognize, oh,
*  this is a really weird situation. And there was a information from a checkup you did two years ago
*  that is relevant to this. And that long context, like abstract reasoning kind of thing. It seems
*  to me like LLMs are pretty bad at that still. And I'm not going to say that GPT-5 definitely won't
*  do that. But just scaling up the transformer does not seem to me like it's necessarily going to do
*  that. I think there's going to be some need to be some like some kind of deeper improvement to
*  how these things work. And I think that might take a few years. And I'm very interested in
*  your Mamba piece or your Mamba episode back in December got me interested in that. I'm working
*  on a piece about Mamba. I can see that being one piece of that. And that seems to be several years
*  from being at large scale. But anyway, yeah, I have a lot of uncertainty about this. But I guess,
*  I've just learned to be skeptical about confident claims that, oh, this, if we just scale this up or
*  keep doing this, it's going to everything's going to work. Sometimes that's true, but but often it's
*  not. Yeah, I think if there's one thing I've learned, it's and I recall Professor Mike Levin
*  saying this about a very different subject. But he was like, if there's one thing I could say is
*  that we should not be confident, because we've been repeatedly surprised. And it seems like we're
*  we'd be I don't there's no rational basis to expect that the surprises will stop on could go
*  in either direction. And I think we've been we've had a period where the surprises are most of all
*  the upside is all these other language ones work better than we expected in a similar way.
*  Like in 2014, 2015, 2016, self driving cars kept pretty quickly we went from like nothing to like
*  having things that were like pretty close. And but then you can enter a period where the surprises
*  are the other direction is now we've updated our expectations, we were optimistic. And then
*  actually, that was right. You're on the kind of other side of the s curve. So I don't know,
*  we'll hit that. But I'm just like based on my experience, I'm expecting it for periods like
*  that to happen. Yeah, honestly, I think it would probably be in some ways for the best. There was
*  a little bit of a just longer window of time for people to absorb what technology already exists
*  before just getting washed over by yet another wave of it. Maybe last thought, and I'll give
*  you a chance to if there's anything we didn't cover that you can you want to touch on, we can add but
*  I'm in Detroit, obviously famous auto town, you're in DC famous rulemaking town. Which one of us do
*  think gets robot taxi service first? Oh, me no question. You think you want to go there
*  to impress regulators? No way more has started testing here. I think that so several things.
*  One is that cities are easier. We have very few freeways here. I think probably Detroit has more
*  freeways. Got a lot of freeways. Yeah, two they are testing here. The third one is snow, which I
*  don't think is going to be a big obstacle. But I think if you look at the places we must come to
*  so far, it's like California, Arizona, Texas. So I think those go from the south to the north.
*  And so yeah, I expect all the southern cities to have it before any of the northern cities. And I
*  think DC is probably southern for that purpose, because we only have three or four days of snow.
*  Breaking my heart. I don't know if this is something I'm quite ready to move for, but an advocate for
*  being willing to change the environment. This is maybe something I should at least consider on
*  some level. If you can come up with a policy agenda to get rid of all the snow in Detroit,
*  I think that would be pretty popular. But yeah, no doubt. Other than massive global warming.
*  It may imply other downsides. Cool. Well, this has been a great run through of an industry that I'm
*  super interested in. And I think we're both hoping is really going to start to work sooner rather
*  than later. Anything that we can touch on that you want to make sure we mention?
*  No, I think we covered it. I really appreciate the thoroughness of these episodes. I really
*  I rely on you for situational awareness of a lot of things that happen in the industry. So
*  it's been fun to be at the other end of that process.
*  Cool. Thank you. I appreciate that. And it's a lot to live up to, but I will do my best.
*  For now, Timothy Beeley, author of the Understanding AI newsletter, which you can find at
*  understandingai.org. Thank you for being part of the cognitive revolution.
*  Thanks, Nathan.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the
*  show. So please don't hesitate to reach out via email at tcr at turpentine.co,
*  or you can DM me on the social media platform of your choice.

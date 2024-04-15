---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 1965s
Video Keywords: []
Video Views: 2096080
Video Rating: None
---

# Elon Musk: Tesla Autopilot | Lex Fridman Podcast #18
**Lex Fridman:** [April 12, 2019](https://www.youtube.com/watch?v=dEv99vxKjVI)
*  The following is a conversation with Elon Musk. He's the CEO of Tesla, SpaceX, Neuralink,
*  and a co-founder of several other companies. This conversation is part of the Artificial
*  Intelligence podcast. The series includes leading researchers in academia and industry,
*  including CEOs and CTOs of automotive, robotics, AI, and technology companies.
*  This conversation happened after the release of the paper from our group at MIT
*  on driver functional vigilance during use of Tesla's autopilot. The Tesla team reached out to me
*  offering a podcast conversation with Mr. Musk. I accepted, with full control of questions I could
*  ask and the choice of what is released publicly. I ended up editing out nothing of substance.
*  I've never spoken with Elon before this conversation, publicly or privately. Neither
*  he nor his companies have any influence on my opinion nor on the rigor and integrity of the
*  scientific method that I practice in my position at MIT. Tesla has never financially supported my
*  research and I've never owned a Tesla vehicle. I've never owned Tesla stock. This podcast is
*  not a scientific paper. It is a conversation. I respect Elon as I do all other leaders and
*  engineers I've spoken with. We agree on some things and disagree on others. My goal is always with
*  these conversations is to understand the way the guests sees the world. One particular point of
*  disagreement in this conversation was the extent to which camera-based driver monitoring will
*  improve outcomes and for how long it will remain relevant for AI assisted driving. As someone who
*  works on and is fascinated by human-centered artificial intelligence, I believe that if
*  implemented and integrated effectively, camera-based driver monitoring is likely to be of benefit in
*  both the short-term and the long-term. In contrast, Elon and Tesla's focus is on the improvement of
*  autopilot such that its statistical safety benefits override any concern of human behavior
*  and psychology. Elon and I may not agree on everything, but I deeply respect the engineering
*  and innovation behind the efforts that he leads. My goal here is to catalyze a rigorous, nuanced,
*  and objective discussion in industry and academia on AI assisted driving. One that ultimately makes
*  for a safer and better world. And now here's my conversation with Elon Musk.
*  What was the vision, the dream of autopilot when in the beginning, the big picture system level,
*  when it was first conceived and started being installed in 2014, the hardware and the cars?
*  What was the vision, the dream? I wouldn't characterize the vision or dream, simply that
*  there are obviously two massive revolutions in the automobile industry. One is the transition to
*  electrification and then the other is autonomy. And it became obvious to me that in the future,
*  any car that did not have autonomy would be about as useful as a horse.
*  Which is not to say that there's no use, it's just rare and somewhat idiosyncratic if somebody has
*  a horse at this point. It's just obvious that cars will drive themselves completely. It's just a
*  question of time. And if we did not participate in the autonomy revolution, then our cars would
*  not be useful to people relative to cars that are autonomous. I mean, an autonomous car
*  is arguably worth five to 10 times more than a car which is not autonomous.
*  In the long term.
*  Depends what you mean by long term, but let's say at least for the next five years, perhaps 10 years.
*  So there are a lot of very interesting design choices with autopilot early on.
*  First is showing on the instrument cluster or in the Model 3 on the center stack display
*  what the combined sensor suite sees. What was the thinking behind that choice? Was there a debate?
*  What was the process?
*  The whole point of the display is to provide a health check on the vehicle's perception of
*  reality. So the vehicle's taking information from a bunch of sensors, primarily cameras,
*  but also radar and ultrasonics, GPS and so forth. And then that information is then rendered into
*  vector space and that, you know, with a bunch of objects with properties like lane lines and
*  traffic lights and other cars. And then in vector space that is re-rendered onto a display. So you
*  can confirm whether the car knows what's going on or not by looking at the window.
*  Right. I think that's an extremely powerful thing for people to get an understanding,
*  so to become one with the system and understanding what the system is capable of.
*  Now, have you considered showing more? So if we look at the computer vision,
*  you know, like road segmentation, lane detection, vehicle detection, object detection,
*  underlying the system, there is at the edges some uncertainty. Have you considered revealing
*  the parts, the uncertainty in the system, the sort of-
*  Probabilities associated with, say, image recognition or something like that?
*  Yeah. So right now it shows like the vehicles in the vicinity, a very clean, crisp image,
*  and people do confirm that there's a car in front of me and the system sees there's a car in front
*  of me. But to help people build an intuition of what computer vision is by showing some of the
*  uncertainty. Well, I think it's, in my car I always look at the sort of the debug view,
*  and there's two debug views. One is augmented vision, where, which I'm sure you've seen,
*  where it's basically we draw boxes and labels around objects that are recognized.
*  And then there's what we call the visualizer, which is basically a vector space representation
*  summing up the input from all sensors. That does not show up any pictures, but it shows
*  all of the, it basically shows the car's view of the world in vector space.
*  But I think this is very difficult for people to, normal people to understand. They would not know
*  what they're looking at. So it's almost an HMI challenge to the current things that are being
*  displayed is optimized for the general public understanding of what the system is capable of.
*  It's like if you have no idea what, how computer vision works or anything, you can still look at
*  the screen and see if the car knows what's going on. And then if you're a development engineer,
*  or if you're, if you have the development build like I do, then you can see all the debug
*  information. But those would just be like total gibberish to most people.
*  Right. What's your view on how to best distribute effort? So there's three, I would say,
*  technical aspects of autopilot that are really important. So it's the underlying algorithms,
*  like the neural network architecture, there's the data. So that the strain on, and then there's
*  the hardware development and maybe others. But so look, algorithm data, hardware, you only have so
*  much money, only have so much time. What do you think is the most important thing to, to allocate
*  resources to? Or do you see it as pretty evenly distributed between those three? We automatically
*  get fast amounts of data because all of our cars have
*  eight external facing cameras and radar and usually 12 ultrasonic sensors, GPS, obviously,
*  and IMU. And so we basically have a fleet that has, we've got about 400,000 cars on the road
*  that have that level of data. I think you keep quite close track of it, actually.
*  Yes. Yeah. So we're, we're approaching half a million cars on the road that have the full sensor
*  suite. So this is, I'm not sure how many other cars on the road have this sensor suite, but I
*  would be surprised if it's more than 5,000, which means that we have 99% of all the data.
*  So there's this huge inflow of data. Absolutely. Massive inflow of data.
*  And then we, it's taken us about three years, but now we've finally developed our full self-driving
*  computer, which can process an order of magnitude as much as the Nvidia system that we currently
*  have in the cars. And it's really just to use it, you unplug the Nvidia computer and plug
*  the Tesla computer in and that's it. And it's, it's, in fact, we're not even, we're still
*  exploring the boundaries of its capabilities. We're able to run the cameras at full frame rate,
*  full resolution, not even crop the images. And it's still got headroom even on one of the systems.
*  The hard, full self-driving computer is really two computers, two systems on a chip that are
*  fully redundant. So you could put a build through basically any part of that system and it still
*  works. The redundancy, are they perfect copies of each other? Or also it's purely for redundancy
*  as opposed to an argue machine kind of architecture where they're both making decisions. This is purely
*  for redundancy. I think it's more like it's, if you have a twin engine aircraft, commercial aircraft,
*  the system will operate best if both systems are operating, but it's capable of operating safely on
*  one. So, but as is right now, we can just run, we haven't even hit the edge of performance. So
*  there's no need to actually distribute functionality across both SOCs. We can actually
*  just run a full duplicate on each one. You haven't really explored or hit the limit of this.
*  Not yet, hit the limit, no. So the magic of deep learning is that it gets better with data. You
*  said there's a huge inflow of data, but the thing about driving, the really valuable data
*  to learn from is the edge cases. So how do you, I mean, I've heard you talk somewhere about
*  autopilot disengagement being an important moment of time to use. Is there other edge cases or
*  perhaps can you speak to those edge cases? What aspects of them might be valuable? Or if you have
*  other ideas how to discover more and more and more edge cases in driving? Well, there's a lot
*  of things that are learned. There are certainly edge cases where I say somebody's on autopilot
*  and they take over. And then, okay, that's a trigger that goes to our system that says, okay,
*  did they take over for convenience or do they take over because the autopilot wasn't working
*  properly? There's also, like, let's say we're trying to figure out what is the optimal
*  spline for traversing an intersection. Then the ones where there are no interventions
*  are the right ones. So you then say, okay, when it looks like this, do the following.
*  And then you get the optimal spline for a complex, now getting a complex intersection.
*  So that's for, this is kind of the common case. You're trying to capture a huge amount of samples
*  of a particular intersection, how when things went right. And then there's the edge case where,
*  as you said, not for convenience, but something didn't go exactly right. Somebody took over,
*  somebody asserted manual control from autopilot. And really, like, the way to look at this is view
*  all input as error. If the user had to do input, there's something, all input is error. That's a
*  powerful line to think of it that way, because it may very well be error. But if you want to exit
*  the highway, or if you want to, it's a navigation decision that autopilot is not currently designed
*  to do, then the driver takes over. How do you know the difference?
*  That's going to change with navigating autopilot, which we've just released,
*  and without stalking from. So the navigation, like lane change based, like asserting control
*  in order to change, do a lane change or exit a freeway or doing a highway interchange,
*  the vast majority of that will go away with the release that just went out.
*  Yeah, so that, I don't think people quite understand how big of a step that is.
*  Yeah, they don't. If you drive the car, then you do.
*  So you still have to keep your hands on the steering wheel currently when it does the automatic
*  lane change. What are, so there's these big leaps through the development of autopilot,
*  through its history, and what stands out to you as the big leaps? I would say this one,
*  navigating autopilot without having to confirm is a huge leap.
*  It is a huge leap. It also automatically overtakes slow cars. So it's both navigation and
*  seeking the fastest lane. So it'll overtake the slow cars and exit the freeway and take highway
*  interchange and then we have traffic light recognition, which is introduced initially
*  as a warning. I mean, on the development version that I'm driving, the car fully stops and goes at
*  traffic lights. So those are the steps, right? You just mentioned something sort of inkling of
*  step towards full autonomy. What would you say are the biggest technological roadblocks to full
*  self driving? Actually, I don't think, I think we just, the full self driving computer that we just,
*  the Tesla, what we call the FSD computer that's now in production.
*  So if you order any Model S or X or any Model 3 that has the full self driving
*  package, you'll get the FSD computer. That's important to have enough base computation.
*  Then refining the neural net and the control software,
*  but all of that can just be provided as an over there update. The thing that's really profound,
*  and what I'll be emphasizing at the sort of what that investor day that we're having focused on
*  autonomy is that the car is currently being produced with the hardware currently being produced
*  is capable of full self driving. But capable is an interesting word because
*  the hardware is. And as we refine the software, the capabilities will increase dramatically,
*  and then the reliability will increase dramatically, and then it will receive regulatory approval.
*  So essentially, buying a car today is an investment in the future. You're essentially buying
*  you're essentially buying a car. I think the most profound thing is that if you buy a Tesla today,
*  I believe you are buying an appreciating asset, not a depreciating asset.
*  So that's a really important statement there because if hardware is capable enough,
*  that's the hard thing to upgrade. Yes. Usually. Exactly. So then the rest is a software problem.
*  Yes. Software has no marginal cost really.
*  Right. But what's your intuition on the software side? How hard are the remaining steps
*  to get it to where, you know, the experience, not just the safety, but the full experience
*  is something that people would enjoy. I think people enjoy it very much on the highways.
*  It's a total game changer for quality of life for using, you know, Tesla autopilot on the highways.
*  So it's really just extending that functionality to city streets,
*  adding in the traffic light recognition, navigating complex intersections, and then being able to
*  navigate complicated parking lots so the car can exit a parking space and come and find you even
*  if it's in a complete maze of a parking lot. And then it can just drop you off and find a parking
*  spot by itself. Yeah. In terms of enjoyability and something that people would actually find a
*  lot of use from, the parking lot is a really, you know, it's rich of annoyance when you have
*  to do it manually. So there's a lot of benefit to be gained from automation there. So let me
*  start injecting the human into this discussion a little bit. So let's talk about full autonomy.
*  If you look at the current level four vehicles being test on road, like Waymo and so on,
*  they're only technically autonomous. They're really level two systems
*  with just a different design philosophy because there's always a safety driver in almost all
*  cases and they're monitoring the system. Right. Do you see Tesla's full self-driving as still
*  for a time to come requiring supervision of the human being? So it's capabilities are powerful
*  enough to drive but nevertheless requires the human to still be supervising just like a safety
*  driver is in other fully autonomous vehicles. I think it will require detecting hands on wheel
*  for at least six months or something like that from here.
*  Really it's a question of like, from a regulatory standpoint,
*  how much safer than a person does autopilot need to be for it to be okay to not monitor the car?
*  You know, and this is a debate that one can have it and then if you need, you know, a large sample,
*  large amount of data so you can prove with high confidence, statistically speaking, that the car is
*  dramatically safer than a person and that adding in the person monitoring does not materially affect
*  the safety. So it might need to be like two or three hundred percent safer than a person.
*  And how do you prove that? Incidence per mile. Incidence per mile. So crashes and
*  fatalities. Yeah, fatalities would be a factor but there are just not enough fatalities to be
*  statistically significant at scale but there are enough crashes, you know, there are far more
*  crashes than there are fatalities. So you can assess where's the probability of a crash,
*  then there's another step which probability of injury and probability of permanent injury,
*  the probability of death and all of those need to be much better than a person by at least
*  perhaps two hundred percent. And you think there's the ability to have a healthy discourse
*  with the regulatory bodies on this topic? I mean there's no question that regulators pay
*  just disproportionate amount of attention to that which generates press, this is just an objective
*  fact, and Tesla generates a lot of press. So that, you know, in the United States, this
*  I think almost 40,000 automotive deaths per year. But if there are four in Tesla, they'll probably
*  receive a thousand times more press than anyone else. So the psychology of that is actually
*  fascinating. I don't think we'll have enough time to talk about that but I have to talk to you about
*  the human side of things. So myself and our team at MIT recently released a paper on functional
*  vigilance of drivers while using autopilot. This is work we've been doing since autopilot was first
*  released publicly over three years ago, collecting video of driver faces and driver body. So I saw
*  that you tweeted a quote from the abstract so I can at least guess that you've glanced at it.
*  Yeah, I read it. Can I talk you through what we found? Sure. Okay. So it appears that
*  in the data that we've collected that drivers are maintaining functional vigilance such that
*  we're looking at 18,000 disengagement from autopilot, 18,900, and annotating were they
*  able to take over control in a timely manner. So they were there present looking at the road
*  to take over control. Okay. So this goes against what many would predict from the body of literature
*  on vigilance with automation. Now the question is, do you think these results hold across the
*  broader population? So ours is just a small subset. Do you think one of the criticism is
*  that there's a small minority of drivers that may be highly responsible where their vigilance
*  decrement would increase with autopilot use? I think this is all really going to be swept.
*  I mean, the system's improving so much, so fast that this is going to be a mood point very soon
*  where vigilance is like if something's many times safer than a person, then adding a person does
*  the effect on safety is limited. And in fact, it could be negative.
*  That's really interesting. So the fact that a human may, some percent of the population
*  may exhibit a vigilance decrement will not affect the overall statistics numbers of safety?
*  No. In fact, I think it will become very, very quickly, maybe even towards the end of this year,
*  but I'd say I'd be shocked if it's not next year, at the latest, that
*  having a human intervene will decrease safety. I can imagine if you're in an elevator. It used
*  to be that there were elevator operators and you couldn't go in an elevator by yourself and work
*  the lever to move between floors. And now nobody wants an elevator operator because the automated
*  elevator that stops the floors is much safer than the elevator operator.
*  And in fact, it would be quite dangerous to have someone with a lever that can
*  move the elevator between floors. So that's a really powerful statement and really interesting
*  one. But I also have to ask from a user experience and from a safety perspective,
*  one of the passions for me algorithmically is camera-based detection of just sensing the human,
*  but detecting what the driver is looking at, cognitive load, body pose. On the computer vision
*  side, that's a fascinating problem. And there's many in industry who believe you have to have
*  camera-based driver monitoring. Do you think there could be benefit gained from driver monitoring?
*  If you have a system that's at or below human level reliability, then driver monitoring makes
*  sense. But if your system is dramatically better, more reliable than a human, then driver monitoring
*  does not help much. And like I said, you wouldn't want someone in the elevator. If you're in an
*  elevator, do you really want someone with a big lever, some random person operating an elevator
*  between floors? I wouldn't trust that. I'd rather have the buttons. Okay, you're optimistic about
*  the pace of improvement of the system from what you've seen with the full self-driving car computer.
*  The rate of improvement is exponential. So one of the other very interesting design choices early on
*  that connects to this is the operational design domain of autopilot. So where autopilot is able
*  to be turned on. So contrast, another vehicle system that we're studying is the Cadillac
*  SuperCrew system. That's in terms of ODD, very constrained to particular kinds of highways,
*  well mapped, tested, but it's much narrower than the ODD of Tesla vehicles.
*  It's like ADD.
*  That's good. That's a good line. What was the design decision in that different philosophy of
*  thinking where there's pros and cons. What we see with a wide ODD is Tesla's drivers are able to
*  explore more the limitations of the system, at least early on, and they understand together with
*  the instrument cluster display, they start to understand what are the capabilities. So that's
*  a benefit. The con is you're letting drivers use it basically anywhere. Anywhere that could detect
*  lanes with confidence. Was there a philosophy, design decisions that were challenging that were
*  being made there? Or from the very beginning, was that done on purpose with intent? Well, I think
*  frankly, it's pretty crazy letting people drive a two-ton death machine manually. That's crazy.
*  In the future, people will be like, I can't believe anyone was just allowed to drive one of these
*  two-ton death machines and they just drive wherever they wanted. Just like elevators,
*  you just move the elevator with the lever wherever you want. It can stop at halfway
*  between floors if you want. It's pretty crazy. So it's going to seem like a mad thing in the future
*  that people were driving cars. So I have a bunch of questions about the human psychology, about
*  behavior and so on that would become that. That mood, totally. Because you have faith in the AI
*  system. Not faith, but both on the hardware side and the deep learning approach of learning from
*  data will make it just far safer than humans. Yeah, exactly. Recently, there are a few hackers
*  who tricked autopilot to act in unexpected ways with adversarial examples.
*  We all know that neural network systems are very sensitive to minor disturbances to these adversarial
*  examples on input. Do you think it's possible to defend against something like this for the
*  industry? Sure. Can you elaborate on the confidence behind that answer?
*  Well, the neural net is just like a bunch of matrix math. You have to be like a very sophisticated
*  somebody who really understands neural nets and basically reverse engineer how the matrix is being
*  built and then create a little thing that just exactly causes the matrix math to be slightly off.
*  But it's very easy to then block that by having basically anti-negative recognition. It's like
*  if the system sees something that looks like a matrix hack excluded. It's such an easy thing to do.
*  So learn both on the valid data and the invalid data. So basically learn on the adversarial examples
*  to be able to exclude them. Yeah, you basically want to both know what is a car and what is
*  definitely not a car. You train for this is a car and this is definitely not a car. Those are two
*  different things. People have no idea neural nets really. They probably think neural nets involves
*  like fishing net or something. So as you know, taking a step beyond just Tesla and autopilot,
*  current deep learning approaches still seem in some ways to be far from general intelligence
*  systems. Do you think the current approaches will take us to general intelligence or do
*  totally new ideas need to be invented? I think we're missing a few key ideas for
*  general intelligence, artificial general intelligence.
*  But it's going to be upon us very quickly and then we'll need to figure out what shall we do
*  if we even have that choice. But it's amazing how people can't differentiate between say
*  the narrow AI that allows a car to figure out what a lane line is and
*  navigate streets versus general intelligence. These are just very different things.
*  Like your toaster and your computer are both machines but one is much more sophisticated
*  than another. You're confident with Tesla you can create the world's best toaster?
*  The world's best toaster, yes. The world's best self-driving,
*  I'm, yes. To me right now this seems game set match. I don't want to be complacent or
*  overconfident but that's what it appears. That is just literally how it appears right now.
*  I could be wrong but it appears to be the case that Tesla is vastly ahead of everyone.
*  Do you think we will ever create an AI system that we can love and loves us back in a deep
*  meaningful way like in the movie Her? I think AI will be capable of convincing you
*  to fall in love with it very well. And that's different than us humans?
*  You know we start getting into a metaphysical question of like do emotions and thoughts exist
*  in a different realm than the physical and maybe they do, maybe they don't, I don't know.
*  But from a physics standpoint I tend to think of things, you know like physics was my main
*  sort of training and from a physics standpoint essentially if it loves you in a way that you
*  can't tell whether it's real or not, it is real. It's a physics view of love. Yeah.
*  If you cannot prove that it does not, if there's no truth to it,
*  if there's no test that you can apply that would make it,
*  make it allow you to tell the difference, then there is no difference. Right. And it's similar to
*  seeing our world of simulation. There may not be a test to tell the difference between
*  what the real world and the simulation and therefore from a physics perspective
*  it might as well be the same thing. Yes. There may be ways to test whether it's a simulation.
*  There might be. I'm not saying there aren't. But you can certainly imagine that a simulation
*  could correct that once an entity in the simulation found a way to detect the simulation,
*  it could either restart, you know, pause the simulation, start a new simulation or do one
*  of many other things that then corrects for that error. So when maybe you or somebody else creates
*  an AGI system and you get to ask her one question, what would that question be?
*  What's outside the simulation?
*  Elon, thank you so much for talking today. It was a pleasure. All right. Thank you.

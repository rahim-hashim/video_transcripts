---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 4970s
Video Keywords: ['sertac karaman', 'mit', 'robotics', 'control theory', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 42824
Video Rating: None
Video Description: Sertac Karaman is a professor at MIT, co-founder of the autonomous vehicle company Optimus Ride, and is one of top roboticists in the world, including robots that drive and robots that fly.

Support this podcast by signing up with these sponsors:
- Cash App - use code "LexPodcast" and download:
- Cash App (App Store): https://apple.co/2sPrUHe
- Cash App (Google Play): https://bit.ly/2MlvP5w

EPISODE LINKS:
Sertac's Website: http://sertac.scripts.mit.edu/web/
Sertac's Twitter: https://twitter.com/sertackaraman
Optimus Ride: https://www.optimusride.com/

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
1:44 - Autonomous flying vs autonomous driving
6:37 - Flying cars
10:27 - Role of simulation in robotics
17:35 - Game theory and robotics
24:30 - Autonomous vehicle company strategies
29:46 - Optimus Ride
47:08 - Waymo, Tesla, Optimus Ride timelines
53:22 - Achieving the impossible
53:50 - Iterative learning
58:39 - Is Lidar is a crutch?
1:03:21 - Fast autonomous flight
1:18:06 - Most beautiful idea in robotics

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Sertac Karaman Robots That Fly and Robots That Drive  Lex Fridman Podcast #97
**Lex Fridman:** [May 19, 2020](https://www.youtube.com/watch?v=M1-v-dXIzho)
*  The following is a conversation with Sertesh Karaman, a professor at MIT,
*  co-founder of the autonomous vehicle company Optimus Ride, and is one of the top roboticists
*  in the world, including robots that drive and robots that fly. To me, personally, he has been
*  a mentor, a colleague, and a friend. He's one of the smartest and most generous people I know,
*  so it was a pleasure and honor to finally sit down with him for this recorded conversation.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  review it with 5 stars on Apple Podcasts, support it on Patreon, or simply connect with me on
*  Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. As usual, I'll do a few minutes of ads now and
*  never any ads in the middle that can break the flow of the conversation. I hope that works for
*  you and doesn't hurt the listening experience. This show is presented by Cash App, the number
*  one finance app in the App Store. When you get it, use the code LEXPODCAST. Cash App lets you
*  send money to friends, buy bitcoin, and invest in the stock market with as little as $1. Since Cash
*  App allows you to send and receive money digitally, let me mention a surprising fact about physical
*  money. It costs 2.4 cents to produce a single penny. In fact, I think it costs $85 million annually
*  to produce them. That's a crazy little fact about physical money. So again, if you get Cash App from
*  the App Store or Google Play and use the code LEXPODCAST, you get $10, and Cash App will also
*  donate $10 to Thirst, an organization that is helping to advance robotics and STEM education
*  for young people around the world. And now, here's my conversation with Surtash Karaman.
*  Since you have worked extensively on both, what is the more difficult task? Autonomous flying or
*  autonomous driving? That's a good question. I think that autonomous flying, just kind of doing it for
*  consumer drones and so on, the kinds of applications that we're looking at right now, is probably
*  easier. And so I think that that's maybe one of the reasons why it took off, like literally, a little
*  earlier than the autonomous cars. But I think if you look ahead, I would think that the real benefits
*  of autonomous flying, unleashing them in transportation logistics and so on, I think it's
*  a lot harder than autonomous driving. So I think my guess is that we've seen a few machines fly here
*  and there, but we really haven't yet seen any kind of machine, like at massive scale, large scale
*  being deployed and flown and so on. And I think that's going to be after we resolve some of the
*  large scale deployments of autonomous driving. So what's the hard part? What's your intuition
*  behind why at scale, when consumer facing drones are tough? So I think in general, at scale is tough.
*  Like for example, when you think about it, we have actually deployed a lot of robots in the,
*  let's say the past 50 years. We use academics or we business entrepreneur? I think we use humanity.
*  Humanity? A lot of people working on it. So we humans deployed a lot of robots. And I think
*  that when you think about it, robots, they're autonomous. They work. They work on their own,
*  but they are either like an isolated environments or they are in sort of, they may be at scale,
*  but they're really confined to a certain environment that they don't interact so much with humans.
*  And so they work in, I don't know, factory floors, warehouses, they work on Mars.
*  They are fully autonomous over there. But I think that the real challenge of our time
*  is to take these vehicles and put them into places where humans are present. So now I know
*  that there's a lot of like human robot interaction type of things that need to be done. And so that's
*  one thing, but even just from the fundamental algorithms and systems and the business cases,
*  or maybe the business models, even like architecture planning, societal issues,
*  there's a whole bunch of pack of things that are related to us putting robotic vehicles into human
*  present environments. And these humans, they will not potentially be even trained to interact with
*  them. They may not even be using the services that are provided by these vehicles. They may
*  not even know that they're autonomous. They're just doing their thing, living in environments
*  that are designed for humans, not for robots. And that I think is one of the biggest challenges,
*  I think, of our time to put vehicles there. And to go back to your question, I think doing that
*  at scale, meaning you go out in a city and you have like thousands or tens of thousands of
*  autonomous vehicles that are going around, it is so dense to the point where if you see one of them,
*  you look around, you see another one. It is that dense. And that density, we've never done anything
*  like that before. And I would bet that that kind of density will first happen with autonomous cars
*  because I think we can ban the environment a little bit. We can, especially kind of making them safe
*  is a lot easier when they're on the ground. When they're in the air, it's a little bit more
*  complicated. But I don't see that there's going to be a big separation. I think that there will come
*  a time that we're going to quickly see these things unfold. Do you think there will be a time
*  where there's tens of thousands of delivery drones that fill the sky?
*  I think it's possible to be honest. Delivery drones is one thing, but you can imagine
*  for transportation, like an important use case is, we're in Boston, you want to go from Boston to
*  New York and you want to do it from the top of this building to the top of another building in
*  Manhattan and you're going to do it in one and a half hours. And that's a big opportunity, I think.
*  Personal transport, so like you and me be a friend.
*  Almost like an Uber. So like four people, six people, eight people. In our work in autonomous
*  vehicles, I see that. So there's kind of like a bit of a need for one person transport, but also
*  like a few people. So you and I could take that trip together. We could have lunch.
*  I think kind of sounds crazy. Maybe even sounds a bit cheesy, but I think that those kinds of things
*  are some of the real opportunities. And I think it's not like the typical airplane and the airport
*  would disappear very quickly, but I would think that many people would feel like they would spend
*  an extra hundred dollars on doing that and cutting that four hour travel down to one and a half hours.
*  So how feasible are flying cars? It's been the dream. That's like when people imagine the future
*  for 50 plus years, they think flying cars. It's like all technologies, it's cheesy to think about
*  now because it seems so far away, but overnight it can change. But just technically speaking,
*  in your view, how feasible is it to make that happen?
*  I'll get to that question. But just one thing is that I think sometimes we think about
*  what's going to happen in the next 50 years. It's just really hard to guess, right? Next 50 years,
*  I don't know. What's going to happen in transportation in the next 50 years? We
*  could get flying saucers. I could bet on that. I think there's a 50-50 chance that you can build
*  machines that can ionize the air around them and push it down with magnets and they would fly like
*  a flying saucer. That is possible. And it might happen in the next 50 years. So it's a bit hard
*  to guess when you think about 50 years before. But I would think that there's this kind of
*  notion where there's a certain type of airspace that we call the agile airspace.
*  And there's a good amount of opportunities in that airspace. So that would be the space that
*  is a little bit higher than the place where you can throw a stone because that's a tough
*  thing when you think about it. It takes a kid on a stone to take an aircraft down and then what
*  happens. But imagine the airspace that's high enough so that you cannot throw the stone.
*  But it is low enough that you're not interacting with the very large aircraft that are flying
*  several thousand feet above. And that airspace is underutilized or it's actually kind of not
*  utilized at all. So there's recreational people kind of fly every now and then, but it's very few.
*  If you look up in the sky, you may not see any of them at any given time. Every now and then,
*  you'll see one airplane utilizing that space and you'll be surprised. And the moment you're
*  outside of an airport a little bit, it just kind of flies off and then it goes out. And I think
*  utilizing that airspace, the technical challenges there is building in autonomy and ensuring that
*  that kind of autonomy is safe. Ultimately, I think it is going to be building in complex software or
*  complicated so that it's maybe a few orders of magnitude more complicated than what we have on
*  aircraft today. And at the same time, just like we ensure on aircraft, ensuring that it's safe.
*  And so building that kind of complicated hardware and software becomes a challenge,
*  especially when you build that hardware, I mean, you build that software with data.
*  And so, of course, there's some rule-based software in there that kind of do a certain set of things,
*  but then there's a lot of training there. So you think machine learning will be key
*  to these kinds of delivering safe vehicles in the future, especially flight?
*  Not maybe the safe part, but I think the intelligent part. I mean, there are certain things that we do
*  it with machine learning and it's just there's like right now no other way. And I don't know how
*  how else they could be done. And there's always this conundrum. I mean, we could maybe gather
*  billions of programmers, humans who program perception algorithms that detect things in
*  the sky and whatever, or we maybe even have robots like learning a simulation environment and transfer.
*  And they might be learning a lot better in a simulation environment than a billion humans
*  put their brains together and try to program. Humans, pretty limited.
*  So what's the role of simulations with drones? You've done quite a bit of work there.
*  How promising, just the very thing you said just now, how promising is the possibility of
*  training and developing a safe flying robot in simulation and deploying it and having that work
*  pretty well in the real world? I think that a lot of people when they hear simulation,
*  they will focus on training immediately. But I think one thing that you said, which was
*  interesting, it's developing. I think simulation environments are actually could be key and great
*  for development. And that's not new. Like for example, there's people in the automotive industry
*  have been using dynamic simulation for like decades now. And it's pretty standard that you
*  would build and you would simulate. If you want to build an embedded controller, you plug that
*  embedded computer into another computer, that other computer would simulate dynamic and so on.
*  And I think fast forward these things, you can create pretty crazy simulation environments.
*  Like for instance, one of the things that has happened recently and that we can do now is that
*  we can simulate cameras a lot better than we used to simulate them. We were able to simulate them
*  before. And that's, I think we just hit the elbow on that kind of improvement. I would imagine that
*  with improvements in hardware, especially, and with improvements in machine learning,
*  I think that we would get to a point where we can simulate cameras very, very well.
*  Simulate cameras means simulate how a real camera would see the real world. Therefore, you can
*  explore the limitations of that. You can train perception algorithms on that in simulation,
*  all that kind of stuff. Exactly. So it has been easier to simulate what we would call
*  introspective sensors, like internal sensors. So for example, inertial sensing has been easy
*  to simulate. It has also been easy to simulate dynamics, like physics that are governed by
*  ordinary differential equations. I mean, like how a car goes around, maybe how it rolls on the road,
*  how it interacts with the road, or even an aircraft flying around, like the dynamic physics
*  of that. What has been really hard has been to simulate extroceptive sensors, sensors that kind
*  of like look out from the vehicle. And that's a new thing that's coming. Laser range finders
*  are a little bit easier. Cameras, radars are a little bit tougher. I think once we nail that down,
*  the next challenge, I think, in simulation will be to simulate human behavior.
*  That's also extremely hard. Even when you imagine how a human-driven car would act around,
*  even that is hard. But imagine trying to simulate a model of a human just doing a bunch of gestures
*  and so on, and it's actually simulated. It's not captured like with motion capture,
*  but it is simulated. In fact, today, I get involved a lot with this very high-end rendering projects.
*  And I have this test that I pass it to my friends or my mom. I send two photos, two pictures, and I
*  say, which one is rendered, which one is real? And it's pretty hard to distinguish, except I realize
*  except when we put humans in there. It's possible that our brains are trained in a way that we
*  recognize humans extremely well, but we don't so much recognize the built environments,
*  because built environments sort of came after per se we evolved into sort of being humans,
*  but humans were always there. Same thing happens, for example, you look at like monkeys,
*  and you can't distinguish one from another, but they sort of do. And it's very possible that they
*  look at humans. It's kind of pretty hard to distinguish one from another, but we do.
*  And so our eyes are pretty well trained to look at humans and understand if something is off,
*  we will get it. We may not be able to pinpoint it. So in my typical friend test or mom test,
*  what would happen is that we'd put like a human walking in a thing, and they say,
*  this is not right. Something is off in this video. I don't know what, but I can tell you
*  it's the human. I can take the human and I can show you like inside of a building or like an
*  apartment, and it will look like if we had time to render it, it will look great. And this should be
*  no surprise. A lot of movies that people are watching, it's all computer generated. Nowadays,
*  even you watch a drama movie and like there's nothing going on action-wise, but it turns out
*  it's kind of like cheaper, I guess, to render the background. And so they would.
*  LW But how do we get there? How do we get a human that would pass the mom slash friend test,
*  a simulation of a human walking? Do you think that's something we can creep up to by just
*  doing kind of a comparison learning where you have humans annotate what's more realistic and not
*  just by watching? Like what's the path? Because it seems totally mysterious how we simulate human
*  behavior. LW It's hard because a lot of the other things that I mentioned to you, including
*  simulating cameras, right? The thing there is that we know the physics, we know how it works
*  in the real world, and we can write some rules and we can do that. Like for example,
*  simulating cameras, there's this thing called ray tracing. I mean, you literally just kind of
*  imagine it's very similar to it's not exactly the same, but it's very similar to tracing
*  photon by photon. They're going around bouncing on things and coming to your eye. But human
*  behavior, developing a dynamic, like a model of that, that is mathematical so that you can
*  put it into a processor that would go through that, that's going to be hard. And so what else
*  do you got? You can collect data, right? And you can try to match the data. Or another thing that
*  you can do is that you can show the front test. You can say this or that and this or that, and
*  that will be labeling. Anything that requires human labeling, ultimately we're limited by the
*  number of humans that we have available at our disposal and the things that they can do. They
*  have to do a lot of other things than also labeling this data. So that modeling human behavior part
*  is, I think, we're going to realize it's very tough. And I think that also affects
*  our development of autonomous vehicles. I see that in self-driving as well. So you're building
*  self-driving. At the first time, right after urban challenge, I think, everybody focused on
*  localization, mapping and localization. Slam algorithms came in, Google was just doing that.
*  And so building these HD maps, basically that's about knowing where you are. And then five years
*  later in 2012, 2013 came the kind of code and code AI revolution and that started telling us
*  where everybody else is. But we're still missing what everybody else is going to do next. And so
*  you want to know where you are. You want to know what everybody else is. Hopefully you know what
*  you're going to do next. And then you want to predict what other people are going to do. And
*  that last bit has been a real challenge. What do you think is the role your own,
*  the ego vehicle, the robot, the you, the robotic you in controlling and having some control of how
*  the future unrolls of what's going to happen in the future? That seems to be a little bit ignored
*  in trying to predict the future is how you yourself can affect that future by being
*  either aggressive or less aggressive or signaling in some kind of way. So this kind of game theoretic
*  dance seems to be ignored for the moment. It's totally ignored. I mean, it's quite interesting
*  actually, like how we interact with things versus we interact with humans. Like so if you see a
*  vehicle that's completely empty and it's trying to do something, all of a sudden it becomes a
*  thing. So you interact with this table. And so you can throw your backpack or you can kick it,
*  put your feet on it and things like that. But when it's a human, there's all kinds of ways of
*  interacting with a human. So if you and I are face to face, we're very civil, we talk, we understand
*  each other for the most part. We'll see, you just never know what's going to happen. But the thing
*  is that, for example, you and I might interact through YouTube comments and the conversation
*  may go at a totally different angle. And so I think people kind of abusing these autonomous vehicles
*  is a real issue in some sense. And so when you're an ego vehicle, you're trying to coordinate your
*  way, make your way. It's actually kind of harder than being a human. You not only need to be as
*  smart as kind of humans are, but you also, you're a thing. So they're going to abuse you a little
*  bit. So you need to make sure that you can get around and do something. So I, in general,
*  believe in that sort of game theoretic aspects. I've actually personally have done quite a few
*  papers, both on that kind of game theory and also like this kind of understanding people's social
*  value orientation, for example. Some people are aggressive, some people not so much. And
*  a robot could understand that by just looking at how people drive. And as they kind of come
*  and approach, you can actually understand if someone is going to be aggressive or not as a robot,
*  and you can make certain decisions. Well, in terms of predicting what they're going to do,
*  the hard question is you as a robot, should you be aggressive or not when faced with an aggressive
*  robot? Right now, it seems like aggressive is a very dangerous thing to do because
*  it's costly from a societal perspective, how you're perceived. People are not very accepting
*  of aggressive robots in modern society. I think that's accurate. So it really is. And so I'm not
*  entirely sure how to go about, but I know for a fact that how these robots interact with other
*  people in there is going to be, and that interaction is always going to be there. I mean, you could be
*  interacting with other vehicles or other just people kind of like walking around. And like I
*  said, the moment there's like nobody in the seat, it's like an empty thing just rolling off the
*  street. It becomes like no different than like any other thing that's not human. And so people,
*  and maybe abuse is the wrong word, but people maybe rightfully even, they feel like this is a
*  human present environment designed for humans to be, and they kind of they want to own it.
*  And then the robots, they would need to understand it and they would need to respond in a certain
*  way. And I think that this actually opens up like quite a few interesting societal questions for us
*  as we deploy, like we talk, robots at large scale. So what would happen when we try to deploy robots
*  at large scale, I think, is that we can design systems in a way that they're very efficient
*  or we can design them that they're very sustainable. But ultimately the sustainability,
*  efficiency trade-offs, like they're going to be right in there and we're going to have to make
*  some choices. Like we're not going to be able to just kind of put it aside. So for example,
*  we can be very aggressive and we can reduce transportation delays, increase capacity of
*  transportation, or we can be a lot nicer and allow other people to kind of quote,
*  unquote, own the environment and live in a nice place and then efficiency will drop.
*  So when you think about it, I think sustainability gets attached to energy consumption or environmental
*  impact immediately and those are there, but like livability is another sustainability impact. So
*  you create an environment that people want to live in. And if robots are going around being aggressive,
*  you don't want to live in that environment, maybe. However, you should note that if you're
*  not being aggressive, then you're probably taking up some delays in transportation and this and that.
*  So you're always balancing that. And I think this choice has always been there in transportation,
*  but I think the more autonomy comes in, the more explicit the choice becomes.
*  Yeah. And when it becomes explicit, then we can start to optimize it and then we'll get to ask
*  the very difficult societal questions of what do we value more, efficiency or sustainability?
*  It's kind of interesting.
*  That will happen. I think we're going to have to like, I think that the interesting thing about
*  like the whole autonomous vehicles question, I think is also kind of, I think a lot of times,
*  you know, we have focused on technology development like hundreds of years and,
*  you know, the products somehow followed and then, you know, we got to make these choices and things
*  like that. But this is a good time that, you know, we even think about, you know, autonomous taxi type
*  of deployments and the systems that would evolve from there. And you realize the business models
*  are different. The impact on architecture is different. Urban planning, you get into like
*  regulations. And then you get into like these issues that you didn't think about before,
*  but like sustainability and ethics is like right in the middle of it. I mean, even testing autonomous
*  vehicles, like think about it. You're testing autonomous vehicles in human present environments.
*  I mean, the risk may be very small, but still, you know, it's strictly greater than zero risk
*  that you're putting people into. And so then you have that innovation, you know, risk trade-off
*  that you're in that somewhere. And we understand that pretty well now is that if we don't test,
*  at least the development will be slower. I mean, it doesn't mean that we're not going to be able
*  to develop. I think it's going to be pretty hard actually. Maybe we can. We don't, I don't know.
*  But the thing is that those kinds of trade-offs we already are making. And as these systems become
*  more ubiquitous, I think those trade-offs will just really hit. So you are one of the founders
*  of Optimus Ride and Thomas Vigo Company. We'll talk about it. But let me on that point ask maybe
*  good examples, keeping Optimus Ride out of this question, sort of exemplars of different strategies
*  on the spectrum of innovation and safety or caution. So like Waymo, Google self-driving car, Waymo
*  represents maybe a more cautious approach. And then you have Tesla on the other side,
*  headed by Elon Musk that represents a more, however, which adjective you want to use,
*  aggressive, innovative, I don't know. But what do you think about the difference in these two
*  strategies in your view? What's more likely, what's needed and is more likely to succeed
*  in the short term and in the long term? Definitely some sort of a balance is kind of
*  the right way to go. But I do think that the thing that is the most important is actually
*  like an informed public. So I don't mind. I personally, if I were in some place,
*  I wouldn't mind so much taking a certain amount of risk. Some other people might.
*  And so I think the key is for people to be informed. And so that they can, ideally,
*  they can make a choice. In some cases, that kind of choice, making that unanimously is,
*  of course, very hard. But I don't think it's actually that hard to inform people.
*  So I think in one case, like, for example, even the Tesla approach, I don't know, it's hard to
*  judge how informed it is, but it is somewhat informed. I mean, things kind of come out. I
*  think people know what they're taking and things like that and so on. But I think the underlying
*  I do think that these two companies are a little bit kind of representing like,
*  of course, one of them seems a bit safer, the other one, or whatever the objective for that is,
*  and the other one seems more aggressive or whatever the objective for that is. But I think
*  when you turn the tables, there are actually two other orthogonal dimensions that these two are
*  focusing on. On the one hand, for Waymo, I can see that they're, I mean, I think they a little bit
*  see it as research as well. So they kind of they don't, I'm not sure if they're like really
*  interested in like an immediate product. You know, they talk about it. Sometimes there's some pressure
*  to talk about it. So they kind of go for it. But I think, I think that they're thinking,
*  maybe in the back of their minds, maybe they don't put it this way. But I think they realize
*  that we're building like a new engine. It's kind of like call it the AI engine or whatever that is.
*  And autonomous vehicles is a very interesting embodiment of that engine that allows you to
*  understand where the ego vehicle is, the ego thing is, where everything else is, what everything else
*  is going to do, and how do you react? How do you actually interact with humans the right way? How
*  do you build these systems? And I think they want to know that they want to understand that. And so
*  they keep going and doing that. And so on the other dimension, Tesla is doing something interesting.
*  I mean, I think that they have a good product, people use it. I think that, you know, like it's
*  not for me, but I can totally see people, people like it. And people, I think they have a good
*  product outside of automation. But I was just referring to the automation itself. I mean,
*  you know, like it kind of drives itself. You still have to be kind of, you still have to pay
*  attention to it, right? But you know, people seem to use it. So it works for something. And so people,
*  I think people are willing to pay for it. People are willing to buy it. I think it's one of the
*  other reasons why people buy a Tesla car. Maybe one of those reasons is Elon Musk is the CEO. And
*  you know, he seems like a visionary person. That's what people think. He seems like a visionary
*  person. And so that adds like 5K to the value of the car. And then maybe another 5K is the autopilot.
*  And you know, it's useful. I mean, it's useful in the sense that like people are using it. And so
*  I can see Tesla, sure, of course, they want to be visionary. They want to kind of put out a certain
*  approach and they may actually get there. But I think that there's also a primary benefit of doing
*  all these updates and rolling it out because, you know, people pay for it. And it's basic, you know,
*  demand, supply, market, and people like it. They're happy to pay another 5K, 10K for that
*  novelty or whatever that is. And they use it. It's not like they get it and they try it a couple
*  times. It's a novelty, but they use it a lot of the time. And so I think that's what Tesla is
*  doing. It's actually pretty different. They are on pretty orthogonal dimensions of what kind of
*  things that they're building. They are using the same AI engine. So it's very possible that, you
*  know, they're both going to be sort of one day kind of using a similar, almost like an internal
*  combustion engine. It's a very bad metaphor, but similar internal combustion engine. And maybe one
*  of them is building like a car. The other one is building a truck or something. So ultimately,
*  the use case is very different. So you, like I said, are one of the founders of Optimus, right?
*  Let's take a step back. It's one of the success stories in the autonomous vehicle space. It's a
*  great autonomous vehicle company. Let's go from the very beginning. What does it take to start an
*  autonomous vehicle company? How do you go from idea to deploying vehicles like you are in a few,
*  a bunch of places, including New York? I would say that I think that, you know,
*  what happened to us is it was the following. I think we've realized a lot of kind of talk
*  in the autonomous vehicle industry back in like 2014 even, when we wanted to kind of get started.
*  And I don't know, like I kind of, I would hear things like fully autonomous vehicles two years
*  from now, three years from now. I kind of never bought it. You know, I was a part of MIT's urban
*  challenge entry. It kind of like it has an interesting history. So I did in college and
*  in high school sort of a lot of mathematically oriented work. And I think I kind of, you know,
*  at some point it kind of hit me. I wanted to build something. And so I came to MIT's mechanical
*  engineering program. And I now realize, I think my advisor hired me because I could do like really
*  good math. But I told him that, no, no, no, I want to work on that urban challenge car. You know,
*  I want to build the autonomous car. And I think that was kind of like a process where we really
*  learned, I mean, what the challenges are and what kind of limitations are we up against, you know,
*  like having the limitations of computers or understanding human behavior. There's so many
*  of these things. And I think it just kind of didn't. And so we said, hey, you know, like,
*  why don't we take a more like a market-based approach? So we focus on a certain kind of market
*  and we build a system for that. What we're building is not so much of like an autonomous
*  vehicle only, I would say. So we build full autonomy into the vehicles. But, you know,
*  the way we kind of see it is that we think that the approach should actually involve humans
*  operating them, not just not sitting in the vehicle. And I think today, what we have is today
*  we have one person operate one vehicle, no matter what that vehicle. It could be a forklift,
*  it could be a truck, it could be a car, whatever that is. And we want to go from that to 10 people
*  operate 50 vehicles. How do we do that? You're referring to a world of maybe perhaps
*  teleoperation. So can you just say what it means for 10? It might be confusing for people listening.
*  What does it mean for 10 people to control 50 vehicles? That's a good point. So I think it's,
*  I very deliberately didn't call it teleoperation because what people think then is that people
*  think away from the vehicle sits a person, sees like maybe puts on goggles or something, VR,
*  and drives the car. So that's not at all what we mean. But we mean the kind of intelligence whereby
*  humans are in control, except in certain places the vehicles can execute on their own.
*  And so imagine like a room where people can see what the other vehicles are doing and everything.
*  And there will be some people who are more like air traffic controllers, call them like
*  AV controllers. And so these AV controllers would actually see kind of like a whole map.
*  And they would understand why vehicles are really confident and where they kind of need a little
*  bit more help. And the help shouldn't be for safety. Help should be for efficiency.
*  Vehicles should be safe no matter what. If you had zero people, they could be very safe,
*  but they'd be going five miles an hour. And so if you want them to go around 25 miles an hour,
*  then you need people to come in. And for example, the vehicle come to an intersection
*  and the vehicle can say, I can wait, I can inch forward a little bit, show my intent,
*  or I can turn left. And right now it's clear I can turn, I know that, but before you give me the
*  go, I won't. And so that's one example. This doesn't mean necessarily we're doing that,
*  actually. I think if you go down that much detail that every intersection you're kind of
*  expecting a person to press a button, then I don't think you'll get the efficiency benefits
*  you want. You need to be able to kind of go around and be able to do these things. But I think you
*  need people to be able to set high level behavior to vehicles. That's the other thing with autonomous
*  vehicles. I think a lot of people kind of think about it as follows. I mean, this happens with
*  technology a lot. You think, all right, so I know about cars and I heard robots. So I think how this
*  is going to work out is that I'm going to buy a car, press a button, and it's going to drive itself.
*  And when is that going to happen? And people kind of tend to think about it that way. But when you
*  think about what really happens is that something comes in in a way that you didn't even expect.
*  If asked, you might have said, I don't think I need that, or I don't think it should be that,
*  and so on. And then that becomes the next big thing, code in code. And so I think that this kind of
*  different ways of humans operating vehicles could be really powerful. I think that sooner than later,
*  we might open our eyes up to a world in which you go around walking a mall and there's a bunch of
*  security robots that are exactly operated in this way. You go into a factory or a warehouse,
*  there's a whole bunch of robots that are operating exactly in this way. You go to the Brooklyn
*  Navy Yard, you see a whole bunch of autonomous vehicles, Optimus Ride, and they're operated maybe
*  in this way. But I think people kind of don't see that. I sincerely think that there's a possibility
*  that we may almost see like a whole mushrooming of this technology in all kinds of places that we
*  didn't expect before. And that may be the real surprise. And then one day when your car actually
*  drives itself, it may not be all that much of a surprise at all, because you see it all the time.
*  You interact with them, you take the Optimus Ride, hopefully that's your choice. And then
*  you hear a bunch of things, you go around, you interact with them. I don't know, like you have
*  a little delivery vehicle that goes around the sidewalks and delivers you things, and then you
*  take it, it says thank you. And then you get used to that, and one day your car actually drives
*  itself, and the regulation goes by, and you can hit the button to sleep. And it wouldn't be a
*  surprise at all. I think that may be the real reality. So there's going to be a bunch of
*  applications that pop up around autonomous vehicles, some of which, maybe many of which,
*  we don't expect at all. So if we look at Optimus Ride, what do you think, you know, the viral
*  application, the one that really works for people in mobility, what do you think Optimus Ride will
*  connect with in the near future first? I think that the first places that I like to target,
*  honestly, is like these places where transportation is required within an environment. Like people
*  typically call it geofenced, so you can imagine like roughly two mile by two mile, could be bigger,
*  could be smaller type of an environment. And there's a lot of these kinds of environments
*  that are typically transportation deprived. The Brooklyn Navy Yard that we're in today,
*  we're in a few different places, but that was the one that was last publicized.
*  That's a good example. So there's not a lot of transportation there, and you wouldn't expect,
*  like, I don't know, I think maybe operating an Uber there ends up being sort of a little too
*  expensive. Or when you compare it with operating Uber Elsevier, that becomes the priority, and these
*  places become totally transportation deprived. And then what happens is that people drive into
*  these places and to go from point A to point B inside this place, within that day, they use their
*  cars. And so we end up building more parking for them to, for example, take their cars and go to
*  the lunch place. And I think that one of the things that can be done is that you can put in
*  efficient, safe, sustainable transportation systems into these types of places first.
*  And I think that you could deliver mobility in an affordable way, affordable, accessible,
*  sustainable way. But I think what also enables is that this kind of effort, money, area, land that
*  we spend on parking, you could reclaim some of that. And that is on the order of, like, even for
*  a small environment, like two mile by two mile, it doesn't have to be smack in the middle of New
*  York. I mean, anywhere else, you're talking tens of millions of dollars. If you're smack in the
*  middle of New York, you're looking at billions of dollars of savings just by doing that. And that's
*  the economic part of it. And there's a societal part, right? I mean, just look around. I mean,
*  the places that we live are like built for cars. It didn't look like this just like a hundred years
*  ago. Like today, no one walks in the middle of the street. It's for cars. No one tells you that
*  growing up, but you grow into that reality. And so sometimes they close the road. It happens here.
*  Like they celebrate and they close the road. Still people don't walk in the middle of the road,
*  like just walk in the middle and people don't. But I think it has so much impact, the car in the space
*  that we have. And I think we talked about sustainability, livability. I mean, ultimately,
*  these kinds of places that parking spots at the very least could change into something more useful
*  or maybe just like park areas, recreational. And so I think that's the first thing that
*  we're targeting. And I think that we're getting like a really good response, both from an economic,
*  societal point of view, especially places that are a little bit forward looking.
*  And like, for example, Brooklyn Navy Yard, they have tenants. There's a distinct article like New
*  Lab. It's kind of like an innovation center. There's a bunch of startups there. And so,
*  you get those kinds of people and they're really interested in making that environment
*  more livable. And these kinds of solutions that Optimus Ride provides almost kind of comes in
*  and becomes that. And many of these places that are transportation deprived, they actually rent
*  shuttles. And so you can ask anybody, the shuttle experience is like terrible. People hate shuttles.
*  And I can tell you why. It's because the driver is very expensive in a shuttle business. So
*  what makes sense is to attach 20, 30 seats to a driver. And a lot of people have this misconception.
*  They think that shuttles should be big. Sometimes we get that at Optimus Ride. We tell them,
*  we're going to give you like four seaters, six seaters. And we get asked, how about like 20
*  seaters? You don't need 20 seaters. You want to split up those seats so that they can travel
*  faster and the transportation delays would go down. That's what you want. If you make it big,
*  not only you will get delays in transportation, but you won't have an agile vehicle. It will take
*  a long time to speed up, slow down and so on. You need to climb up to the thing. So it's kind of
*  like really hard to interact with. And scheduling too, perhaps when you have more smaller vehicles,
*  it becomes closer to Uber where you can actually get a personal, I mean, just the logistics of
*  getting the vehicle to you becomes easier when you have a giant shuttle. There's fewer of them
*  and it probably goes on a route, a specific route that it's supposed to hit.
*  Yeah. And when you go on a specific route and all seats travel together versus, you know,
*  you have a whole bunch of them, you can imagine the route you can still have, but you can imagine
*  you split up the seats and instead of them traveling like, I don't know, a mile apart,
*  they could be like, you know, half a mile apart if you split them into two. That basically would
*  mean that your delays when you go out, you won't wait for them for a long time. And that's one of
*  the main reasons or you don't have to climb up. The other thing is that I think if you split them
*  up in a nice way and if you can actually know where people are going to be somehow, you don't
*  even need the app. A lot of people ask us the app. We say, why don't you just walk into the vehicle?
*  How about you just walk into the vehicle, it recognizes who you are and it gives you a bunch
*  of options of places that you go and you just kind of go there. I mean, people kind of also
*  internalize the apps. Everybody needs an app. It's like you don't need an app. You just walk into the
*  thing. You just walk up. But I think one of the things that, you know, we really try to do is to
*  take that shuttle experience that no one likes and tilt it into something that everybody loves.
*  And so I think that's another important thing. I would like to say that carefully, just like
*  teleoperation, we don't do shuttles. You know, we're really kind of thinking of this as a system
*  or a network that we're designing. But ultimately we go to places that would normally rent the shuttle
*  service that people wouldn't like as much and we want to tilt it into something that people love.
*  So you mentioned this earlier, but how many Optimus ride vehicles do you think would be needed
*  for any person in Boston or New York? If they step outside, there will be,
*  this is like a mathematical question, there will be two Optimus ride vehicles within line of sight.
*  Is that the right number? To at least one?
*  Like for example, that's the density. So meaning that if you see one vehicle,
*  you look around, you see another one too. Imagine like, you know, Tesla would tell you they collect
*  a lot of data. Do you see that with Tesla? Like you just walk around and you look around,
*  you see Tesla? Probably not. Very specific areas of California, maybe.
*  Maybe. You're right. Like there's a couple zip codes that, you know,
*  but I think that's kind of important because, you know, like maybe the couple zip codes,
*  the one thing that we kind of depend on, and I'll get to your question in a second,
*  but now like we're taking a lot of tangents today. Hell yes.
*  And so I think that this is actually important. People call this data density or data velocity.
*  So it's very good to collect data in a way that, you know, you see the same place so many times.
*  Like you can drive 10,000 miles around the country or you drive 10,000 miles in a confined
*  environment. You'll see the same intersection hundreds of times. And when it comes to predicting
*  what people are going to do in that specific intersection, you become really good at it.
*  Versus if you draw on like 10,000 miles around the country, you've seen that only once.
*  And so trying to predict what people do becomes hard.
*  And I think that, you know, you said what is needed, it's tens of thousands of vehicles.
*  You know, you really need to be like a specific fraction of vehicle. Like for example, in good
*  times in Singapore, you can go and you can just grab a cab and they are like, you know, 10%,
*  20% of traffic, those taxis. Ultimately, that's where you need to get to so that, you know,
*  you get to a certain place where you really, the benefits really kick off in like orders of magnitude
*  type of a point. But once you get there, you actually get the benefits. And you can certainly
*  carry people. I think that's one of the things people really don't like to wait for themselves.
*  But for example, they can wait a lot more for the goods if they order something like they're,
*  you're sitting at home and you want to wait half an hour. That sounds great. People will say it's
*  great. You want to, you're going to take a cab, you're waiting half an hour. Like that's crazy.
*  You don't want to wait that much. But I think, you know, you can, I think really get to a point
*  where the system at peak times really focuses on kind of transporting humans around. And then
*  it's really, it's a good fraction of traffic to the point where, you know, you go, you look around
*  and there's something there and you just kind of basically get in there and it's already waiting
*  for you or something like that. And then you take it. If you do it at that scale, like today, for
*  instance, Uber, if you talk to a driver, right? I mean, Uber takes a certain cut. It's a small cut
*  or drivers would argue that it's a large cut, but you know, it's, it's, it's when you look at the
*  grand scheme of things, most of that money that you pay Uber kind of goes to the driver. And if
*  you talk to the driver, the driver will claim that most of it is their time. You know, they, it's not
*  spent on gas. They think it's not spent on the car per se as much. It's like their time. And if
*  you didn't have a, have a person driving, or if you're in a scenario where, you know, like
*  0.1 person is driving the car, a fraction of a person is kind of operating the car because,
*  you know, you're one operate several. If you're in that situation, you realize that the internal
*  combustion engine type of cars are very inefficient. You know, we build them to go on highways. They
*  pass crash tests. They're like really heavy. They really don't need to be like 25 times the weight
*  of its passengers or, or, you know, like area wise and so on. And, but if you get through those
*  inefficiencies and if you really build like urban cars and things like that, I think the economics
*  really starts to check out like to the point where, I mean, I don't know, you may be able to get into
*  a car and it may be less than a dollar to go from A to B. As long as you don't change your destination,
*  you just pay 99 cents and go there. If you share it, if you take another stop somewhere,
*  it becomes a lot better. You know, these kinds of things, at least for models, at least for
*  mathematics and theory, they start to really check out. So I think it's really exciting what
*  OptimusRide is doing in terms of it feels the most reachable. Like it'll actually be here and have
*  an impact. Yeah, that is the idea. And if we contrast that again, we'll go back to our old friends,
*  Waymo and Tesla. So Waymo seems to have sort of technically similar approaches as OptimusRide,
*  but a different, they're not as interested as having an impact today. They have a longer term
*  sort of investment. It's almost more of a research project still, meaning they're trying to solve,
*  as far as I understand, maybe you can differentiate, but they seem to want to do
*  more unrestricted movement, meaning move from A to B where A to B is all over the place versus
*  OptimusRide is really nicely geofenced and really sort of established mobility in a particular
*  environment before you expand it. And then Tesla is like the complete opposite, which is
*  you know, the entirety of the world actually is going to be automated. Highway driving,
*  urban driving, every kind of driving, you know, you kind of creep up to it by incrementally
*  improving the capabilities of the autopilot system. So when you contrast all of these,
*  and on top of that, let me throw a question that nobody likes, but is a timeline. When do you think
*  each of these approaches, loosely speaking, nobody can predict the future, will see mass deployment?
*  So Elon Musk predicts the craziest approach is at the, I've heard figures like at the end of this
*  year, right? So that's probably wildly inaccurate, but how wildly inaccurate is it? I mean, first
*  thing to lay out, like everybody else, it's really hard to guess. I mean, I don't know where Tesla
*  can look at or Elon Musk can look at and say, hey, you know, it's the end of this year. I mean,
*  I don't know what you can look at. Even the data that you would, I mean, if you look at the data,
*  even kind of trying to extrapolate the end state without knowing what exactly is going to go,
*  especially for like a machine learning approach. I mean, it's just kind of very hard to predict.
*  But I do think the following does happen. I think a lot of people,
*  you know, what they do is that there's something that I called a couple of times time dilation
*  in technology prediction happens. Let me try to describe a little bit. There's a lot of things
*  that are so far ahead. People think they're close and there's a lot of things that are actually
*  close. People think it's far ahead. People try to kind of look at a whole landscape of technology
*  development. Admittedly, it's chaos. Anything can happen in any order at any time. And there's a
*  whole bunch of things in there. People take it, clamp it, and put it into the next three years.
*  And so then what happens is that there's some things that maybe can happen by the end of the
*  year or next year and so on. And they push that into like a few years ahead because it's just hard
*  to explain. And there are things that are like, we're looking at 20 years more maybe, you know,
*  hopefully in my lifetime type of things. Because we don't know. I mean, we don't know how hard it
*  is even. Like that's a problem. We don't know if some of these problems are actually AI complete.
*  We have no idea what's going on. And we take all of that and then we clump it and then we say
*  three years from now. And then some of us are more optimistic. So they're shooting at the end
*  of the year. And some of us are more realistic. They say like five years. But we all, I think,
*  it's just hard to know. And I think trying to predict products ahead, two, three years,
*  it's hard to know in the following sense. We typically say, okay, this is a technology company.
*  But sometimes really you're trying to build something where the technology does that. There's
*  a technology gap. And Tesla had that with electric vehicles. When they first started,
*  they would look at a chart, much like a Moore's law type of chart. And they would just kind of
*  extrapolate that out and they'd say, we want to be here. What's the technology to get that? We
*  don't know. It goes like this. So it's probably just going to keep going. With AI that goes into
*  the cars, we don't even have that. I mean, what can you quantify? Like what kind of chart are you
*  looking at? But so I think when there's that technology gap, it's just kind of really hard
*  to predict. So now I realize I talked like five minutes and I avoid your question. I didn't tell
*  you anything about that. It was very skillfully done. And I think you've actually argued that
*  it's not a use. Any answer you provide now is not that useful. It's going to be very hard.
*  There's one thing that I really believe in. And this is not my idea and it's been discussed
*  several times, but something like a startup or kind of an innovative company, including definitely
*  Waymo, Tesla, maybe even some of the other big companies that are kind of trying things.
*  This kind of iterated learning is very important. The fact that we're over there and we're trying
*  things and so on, I think that's important. We try to understand. And I think that the code in code
*  Silicon Valley has done that with business models pretty well. And now I think we're trying to get
*  to do it where there's a literal technology gap. I mean, before, I think these companies are building
*  great technology to, for example, enable internet search to do it so quickly. And that kind of
*  wasn't there so much, but at least it was a kind of a technology that you could predict to some degree
*  and so on. And now we're just kind of trying to build things that it's kind of hard to quantify.
*  What kind of a metric are we looking at? So psychologically as a leader of graduate students
*  and at Optimus Ride, a bunch of brilliant engineers, just curiosity, psychologically,
*  do you think it's good to think that whatever technology gap we're talking about can be closed
*  by the end of the year? Or do you, you know, because we don't know. So the way, do you want to say
*  that everything is going to improve exponentially to yourself and to others around you as a leader?
*  Or do you want to be more sort of maybe not cynical, but I don't want to use realistic
*  because it's hard to predict, but yeah, maybe more cynical pessimistic about the
*  ability to close that gap. Yeah, I think that going back, I think that iterated learning is key.
*  That you're out there, you're running experiments to learn. And that doesn't mean sort of like,
*  like you're Optimus Ride, you're kind of doing something, but like in an environment. But like
*  what Tesla is doing, I think is also kind of like this kind of notion. And people can go around and
*  say like, this year, next year, the other year and so on. But I think that the nice thing about it
*  is that they're out there, they're pushing this technology in. I think what they should do more
*  of, I think that kind of informed people about what kind of technology that they're providing,
*  you know, the good and the bad. And then, you know, not just sort of, you know, it works very well,
*  but I think, you know, I'm not saying they're not doing bad and informing. I think they're kind of
*  trying, they, you know, they put up certain things or at the very least YouTube videos comes out on
*  how the summon function works every now and then. And, you know, people get informed. And so that
*  cycle continues, but, you know, I admire it. I think they kind of go out there and they do great
*  things. They do their own kind of experiment. I think we do our own. And I think we're closing
*  some similar technology gaps, but some also, some are orthogonal as well. You know, I think like we
*  talked about, you know, people being remote, like it's something, or in the kind of environments
*  that we're in, or think about a Tesla car, maybe you can enable it one day, like there's, you know,
*  low traffic, like you're kind of the stop on go motion, you just hit the button and you can
*  really, or maybe there's another, you know, lane that you can pass into, you go in that. I think
*  they can enable these kinds of, I believe it. And so I think that that part, that is really important
*  and that is really key. And beyond that, I think, you know, when is it exactly going to happen? And
*  so on. I mean, it's, like I said, it's very hard to predict. And I would imagine that it would be
*  good to do some sort of like a one or two year plan when it's a little bit more predictable,
*  that, you know, the technology gaps, you close and the kind of sort of product that would end
*  soon. So I know that from Optimus Ride or, you know, other companies that I get involved in, I
*  mean, at some point you find yourself in a situation where you're trying to build a product
*  and people are investing in that, you know, building effort. And those investors that they
*  do want to know as they compare the investments they want to make, they do want to know what
*  happens in the next one or two years. And I think that's good to communicate that. But I think beyond
*  that it becomes a vision that we want to get to someday and saying five years, 10 years, I don't
*  think it means anything. But iterated learning is key. You do and learn. I think that is key.
*  You know, I got to sort of throw back right at you criticism in terms of, you know, like Tesla or
*  somebody communicating, you know, how someone works and so on. I got the chance to visit Optimus Ride
*  and you guys are doing some awesome stuff and yet the internet doesn't know about it. So you should
*  also communicate more showing off, you know, showing off some of the awesome stuff, the stuff
*  that works and stuff that doesn't work. I mean, it's just the stuff I saw with the tracking of
*  different objects and pedestrians and so on, incredible stuff going on there. Maybe it's just
*  the nerd in me, but I think the world would love to see that kind of stuff. Yeah, that's well taken.
*  I think, you know, I should say that it's not like, you know, we weren't able to, I think we made a
*  decision at some point. That decision did involve me quite a bit on kind of sort of doing this in
*  kind of code and code stealth mode for a bit. But I think that, you know, we'll open it up quite a
*  lot more. And I think that we are also at Optimus Ride kind of hitting a new era. You know, we're
*  big now, we're doing a lot of interesting things. And I think, you know, some of the deployments
*  that we kind of announced were some of the first bits of information that we kind of put out into
*  the world. We'll also put out our technology. A lot of the things that we've been developing
*  is really amazing. And then, you know, we're going to start putting that out. We're especially
*  interested in sort of like being able to work with the best people. And I think it's good to
*  not just kind of show them when they come to our office for an interview, but just put it out there
*  in terms of like, you know, get people excited about what we're doing.
*  So on the autonomous vehicle space, let me ask one last question. So Elon Musk famously said that
*  LIDAR is a crutch. So I've talked to a bunch of people about it. Gotta ask you. You use that crutch
*  quite a bit in the DARPA days. So, you know, and his idea in general, sort of, you know, more
*  provocative and fun, I think, than a technical discussion. But the idea is that camera-based,
*  primarily camera-based systems is going to be what defines the future of autonomous vehicles.
*  So what do you think of this idea? LIDAR is a crutch versus primarily camera-based systems?
*  First things first, I think, you know, I'm a big believer in just camera-based autonomous vehicle
*  systems. Like, I think that, you know, you can put in a lot of autonomy and you can do great
*  things. And it's very possible that at the time scales, like we said, we can't predict
*  20 years from now, like you may be able to do things that we're doing today only with LIDAR,
*  and then you may be able to do them just with cameras. And I think that, you know, you can just,
*  I think that I will put my name on it too. Like, you know, there will be a time when you can only
*  use cameras and you'll be fine. At that time, though, it's very possible that, you know, you
*  find the LIDAR system as another robustifier, or it's so affordable that it's stupid not to,
*  you know, just kind of put it there. And I think we may be looking at a future like that.
*  Do you think we're over relying on LIDAR right now? Because we understand the better,
*  it's more reliable in many ways, in terms of a safety perspective.
*  It's easier to build with. That's the other thing. I think, to be very frank with you, I mean,
*  you know, we've seen a lot of sort of autonomous vehicles companies come and go. And the approach
*  has been, you know, you slap a LIDAR on a car, and it's kind of easy to build with when you have a
*  LIDAR, you know, you just kind of code it up and you hit the button and you do a demo. So I think
*  there's, admittedly, there's a lot of people, they focus on the LIDAR because it's easier to build
*  with. That doesn't mean that, you know, without the camera, it's just cameras, you can, you cannot
*  do what they're doing, but it's just kind of a lot harder. And so you need to have certain kind of
*  expertise to exploit that. What we believe in, and you know, you've maybe seen some of it, is that
*  we believe in computer vision. We certainly work on computer vision and Optimus Ride by a lot,
*  and we've been doing that from day one. And we also believe in sensor fusion. So, you know,
*  we have a relatively minimal use of LIDARs, but we do use them. And I think, you know, in the future,
*  I really believe that the following sequence of events may happen. First things first, number one,
*  there may be a future in which, you know, there's like cars with LIDARs and everything and the
*  cameras, but, you know, in this 50 year ahead future, they can just drive with cameras as well,
*  especially in some isolated environments and cameras, they go and they do the thing.
*  In the same future, it's very possible that, you know, the LIDARs are so cheap and frankly,
*  make the software maybe a little less compute intensive, at the very least, or maybe less
*  complicated so that they can be certified or, or ensure their safety and things like that, that
*  it's kind of stupid not to put the LIDAR. Like, imagine this, you either pay money for the LIDAR
*  or you pay money for the compute. And if you don't put the LIDAR, it's a more expensive system,
*  because you have to put in a lot of compute. Like, this is another possibility.
*  I do think that a lot of the sort of initial deployments of South Korea,
*  the sort of initial deployments of South driving vehicles, I think they will enroll LIDARs.
*  And especially either low range or short, either short range or low resolution LIDARs are actually
*  not that hard to build in solid state. They're still scanning, but like MEMS type of scanning
*  LIDARs and things like that, they're like, they're actually not that hard. I think they will
*  maybe kind of playing with the spectrum and the phase arrays that are a little bit harder, but,
*  but I think like, putting MEMS mirror in there that kind of scans the environment, it's not hard.
*  The only thing is that, you know, you just like with a lot of the things that we do nowadays in
*  developing technology, you hit fundamental limits of the universe. The speed of light becomes a
*  problem in when you're trying to scan the environment. So you don't get either good
*  resolution or you don't get range. But, but you know, it's still, it's something that you can
*  put in that affordably.
*  So let me jump back to drones. You've, you have a role in the Lockheed Martin Alpha Pilot
*  Innovation Challenge, where teams compete in drone racing. It's super cool, super intense,
*  interesting application of AI. So can you tell me about the very basics of the challenge and
*  where you fit in, where your thoughts are on this problem? And it's sort of echoes of the early DARPA
*  challenge in the, through the desert that we're seeing now, now with drone racing.
*  Yeah. I mean, one interesting thing about it is that, you know, people, the drone racing
*  exists as an e-sport. And so it's much like you're playing a game, but there's a real drone going in
*  an environment. A human being is controlling it with goggles on. So there's no, it is a robot,
*  but there's no AI. There's no AI. Yeah. Human being is controlling it. And so that's already there.
*  And I've been interested in this problem for quite a while, actually, from a roboticist point of view.
*  And that's what's happening in Alpha Pilot. Which problem? Of aggressive flight? Of aggressive flight,
*  fully autonomous, aggressive flight. The problem that I'm interested in, you asked about Alpha
*  Pilot, and I'll get there in a second, but the problem that I'm interested in, I'd love to build
*  autonomous vehicles like drones that can go far faster than any human possibly can. I think we
*  should recognize that we as humans have limitations in how fast we can process information.
*  And those are some biological limitations. Like we think about this AI this way too. I mean,
*  this has been discussed a lot, and this is not sort of my idea per se, but a lot of people kind
*  of think about human level AI. And they think that AI is not human level. One day it'll be human level
*  and humans and AIs, they kind of interact. Versus I think that the situation really is that humans
*  are at a certain place and AI keeps improving and at some point it just crosses off and then
*  it gets smarter and smarter and smarter. And so drone racing, the same issue. Humans play this game
*  and you have to react in milliseconds. And there's really, you see something with your eyes
*  and then that information just flows through your brain into your hands so that you can command it.
*  And there's some also delays on getting information back and forth. But suppose those
*  delays that don't exist. Just a delay between your eye and your fingers is a delay that a robot
*  doesn't have to have. So we end up building in my research group systems that see things at
*  a kilohertz. Like a human eye would barely hit a hundred hertz. So imagine things that see
*  stuff in slow motion, like 10x slow motion. It will be very useful. We talked a lot about
*  autonomous cars so we don't get to see it, but a hundred lives are lost every day just in the
*  United States on traffic accidents. And many of them are known cases. You're coming through
*  like a ramp, going into a highway, you hit somebody and you're off. Or you kind of get confused,
*  you try to swerve into the next lane, you go off the road and you crash, whatever.
*  And I think if you had enough computer in a car and a very fast camera right at the time of an
*  accident, you could use all compute you have. Like you could shut down the infotainment system
*  and use that kind of computing resources instead of rendering. You use it for the kind of artificial
*  intelligence that goes in there, the autonomy. And you can either take control of the car and
*  bring it to a full stop, but even if you can't do that, you can deliver what the human is trying to
*  do. Human is trying to change the lane, but goes off the road, not being able to do that with motor
*  skills and the eyes and you can get in there. And there's so many other things that you can enable
*  with what I would call high throughput computing. Data is coming in extremely fast and in real time
*  you have to process it. And the current CPUs, however fast you clock it, are typically not
*  enough. You need to build those computers from the ground up so that they can ingest all that data
*  that I'm really interested in. Just on that point, just really quick, is the currently,
*  what's the bottom? Like you mentioned the delays in humans, is it the hardware? So you work a lot
*  with Nvidia hardware. Is it the hardware or is it the software? I think it's both. I think it's both.
*  In fact, they need to be co-developed, I think in the future. I mean, that's a little bit what Nvidia
*  does. They almost build the hardware and then they build the neural networks and then they build
*  the hardware back and the neural networks back and it goes back and forth, but it's that co-design.
*  And I think that we tried to build a fast drone that could use a camera image to track what's
*  moving in order to find where it is in the world. This typical visual inertial state estimation
*  problems that we would solve. And we just kind of realized that we're at the limit sometimes of
*  doing simple tasks. We're at the limit of the camera frame rate. Because if you really want
*  to track things, you want the camera image to be 90% kind of like, or somewhat the same from one
*  frame to the next. And why are we at the limit of the camera frame rate? It's because camera
*  captures data. It puts it into some serial connection. It could be USB or there's something
*  called camera serial interface that we use a lot. It puts into some serial connection
*  and copper wires can only transmit so much data. And you hit the Shannon limit on copper wires
*  and you hit yet another kind of universal limit that you can transfer the data. So you have to be
*  much more intelligent on how you capture those pixels. You can take compute and put it right
*  next to the pixels. How hard is it to do? How hard is it to get past the bottleneck of the copper wire?
*  Yeah, you need to do a lot of parallel processing, as you can imagine. The same
*  thing happens in the GPUs. The data is transferred in parallel somehow. It gets into some parallel
*  processing. I think that now we're really kind of diverted off into so many different dimensions.
*  But great. So it's aggressive flight. How do we make drones see many more frames a second
*  in order to enable aggressive flight? That's a super interesting problem.
*  That's an interesting problem. But think about it. You have CPUs. You clock them at several
*  gigahertz. We don't clock them faster, largely because we run into some heating issues and
*  things like that. But another thing is that three gigahertz clock light travels kind of like on the
*  order of a few inches or an inch. That's the size of a chip. And so you pass a clock cycle. And as
*  the clock signal is going around in the chip, you pass another one. And so trying to coordinate
*  that, the design of the complexity of the chip becomes so hard. I mean, we have hit the fundamental
*  limits of the universe in so many things that we're designing. I don't know if people realize
*  that. It's great. But we can't make transistors smaller because quantum effects, the electrons
*  start to tunnel around. We can't clock it faster. One of the reasons why is because information
*  doesn't travel faster in the universe. And we're limited by that. Same thing with the laser scanner.
*  But so then it becomes clear that the way you organize the chip into a CPU or even a GPU,
*  you now need to look at how to redesign that if you're going to stick with silicon.
*  You could go do other things too. I mean, there's that too. But you really almost need to take those
*  transistors, put them in a different way so that the information travels on those transistors
*  in a different way, in a much more way that is specific to the high-speed cameras coming in.
*  And so that's one of the things that we talk about quite a bit.
*  So drone racing kind of really makes that...
*  Embodies that.
*  It embodies that. And that's why it's really exciting.
*  It's exciting for people, students like it. It embodies all those problems. But going back,
*  we're building, quote, unquote, another engine. And that engine, I hope one day, will be just
*  how impactful seat belts were in driving. I hope so. Or it could enable next-generation autonomous
*  air taxis and things like that. I mean, it sounds crazy, but one day we may need to perch-land these
*  things. If you really want to go from Boston to New York in more than a half hours, you may want
*  to fix being aircraft. Most of these companies that are doing, quote, unquote, flying cars,
*  they're focusing on that. But then how do you land it on top of a building? You may need to pull off
*  fast maneuvers for a robot, like perch-landing. Just going to go and perch into a building.
*  If you want to do that, you need these kinds of systems. And so drone racing,
*  it's being able to go way faster than any human can comprehend.
*  Take an aircraft. Forget the quadcopter. You take your fixed wing. While you're at it,
*  you might as well put some rocket engines in the back and just light it. You go through the gate,
*  and a human looks at it and just said, what just happened? And they would say, it's impossible for
*  me to do that. And that's closing the same technology gap that would one day steer cars out of accidents.
*  But then let's get back to the practical, which is just getting the thing to work in a race
*  environment, which is another kind of exciting thing, which the DARPA challenge to the desert
*  did. Theoretically, we had autonomous vehicles, but making them successfully finish a race,
*  first of all, which nobody finished the first year, and then the second year just to get to finish
*  and go at a reasonable time is really difficult engineering, practically speaking, challenge.
*  So let me ask about the Alpha Pilot challenge. It's, I guess, a big prize potentially associated
*  with it. But let me ask, reminiscent of the DARPA days predictions, you think anybody will finish?
*  Well, not soon. I think that depends on how you set up the race course. And so if the race course is
*  a slow course, I think people will kind of do it. But can you set up some course, like literally
*  some course, you get to design it as the algorithm developer, can you set up some course so that you
*  can beat the best human? When is that going to happen? Like that's not very easy, even just
*  setting up some course. If you let the human that you're competing with set up the course,
*  it becomes a lot harder. So how many in the space of all possible courses
*  would humans win and would machines win? Great question. Let's get to that. I want to answer
*  your other question, which is like the DARPA challenge days, right? What was really hard?
*  I think we understood what we wanted to build, but still building things, that experimentation,
*  that iterated learning, that takes up a lot of time actually. And so in my group, for example,
*  in order for us to be able to develop fast, we build like VR environments. We'll take an aircraft,
*  we'll put it in a motion capture room, big, huge motion capture room, and we'll fly it in real time
*  and we'll render other images and beam it back to the drone. That sounds kind of notionally simple,
*  but it's actually hard because now you're trying to fit all that data through the air into the drone.
*  And so you need to do a few crazy things to make that happen. But once you do that,
*  then at least you can try things. If you crash into something, you didn't actually crash. So it's like
*  the whole drone is in VR. We can do augmented reality and so on. And so I think at some point,
*  testing becomes very important. One of the nice things about AlphaPilot is that
*  they built the drone and they built a lot of drones and it's okay to crash. In fact, I think maybe
*  the viewers may kind of like to see things that's...
*  That potentially could be the most exciting part.
*  It could be the exciting part. And I think as an engineer, it's a very different situation to be in.
*  Like in academia, a lot of my colleagues who are actually in this race and they're really
*  great researchers, but I've seen them trying to do similar things whereby they built this one drone
*  and somebody with like a face mask and a gloves are going right behind the drone, trying to hold
*  it if it falls down. Imagine you don't have to do that. I think that's one of the nice things about
*  AlphaPilot challenge where we have these drones and we're going to design the courses in a way that
*  we'll keep pushing people up until the crashes start to happen. And we'll hopefully sort of
*  I don't think you want to tell people crashing is okay. Like we want to be careful here,
*  but because we don't want people to crash a lot, but certainly we want them to push it so that
*  everybody crashes once or twice and they're really pushing it to their limits.
*  That's where iterated learning comes in. Every crash is a lesson.
*  It's a lesson, exactly.
*  So in terms of the space of possible courses, how do you think about it?
*  In the war of human versus machines, where do machines win?
*  We look at that quite a bit. I mean, I think that you will see quickly that
*  like you can design a course and in certain courses like in the middle somewhere,
*  if you kind of run through the course once, the machine gets beaten pretty much consistently by
*  slightly. But if you go through the course like 10 times, humans get beaten very slightly but
*  consistently. So humans at some point, you get confused, you get tired and things like that
*  versus this machine is just executing the same line of code tirelessly, just going back to the
*  beginning and doing the same thing exactly. I think that kind of thing happens. And I realize
*  sort of as humans, there's the classical things that everybody has realized. If you put in some
*  sort of strategic thinking, that's a little bit harder for machines that I think sort of comprehend.
*  Precision is easy to do, so that's what they excel in. And also,
*  repeatability is easy to do, that's what they excel in. You can build machines that excel in
*  strategy as well and beat humans that way too, but that's a lot harder to build.
*  I have a million more questions, but in the interest of time, last question.
*  What is the most beautiful idea you've come across in robotics? Whether a simple equation,
*  experiment, a demo, simulation, piece of software, what just gives you pause?
*  That's an interesting question. I have done a lot of work myself in decision making, so I've been
*  interested in that area. In robotics, somehow the field has split into, there's people who
*  would work on perception, how robots perceive the environment, then how do you actually make
*  decisions, and there's people also, how do you interact with robots. There's a whole bunch of
*  different fields. I have admittedly worked a lot on the more control and decision making than the
*  others. And I think that the one equation that has always baffled me is Bellman's equation.
*  And so it's this person who have realized way back, more than half a century ago,
*  on how do you actually sit down and if you have several variables that you're jointly trying to
*  determine, how do you determine that? And there's one beautiful equation that, like today, people
*  do reinforcement and we still use it. And it's baffling to me because it both kind of tells you
*  the simplicity, because it's a single equation that anyone can write down. You can teach it in
*  the first course on decision making. At the same time, it tells you computationally how hard the
*  problem is. I feel like a lot of the things that I've done at MIT for research has been kind of just
*  this fight against computational efficiency. Things like how can we get it faster to the point
*  where we now got to like, let's just redesign this chip. Maybe that's the way. But I think
*  it talks about how computationally hard certain problems can be by nowadays what people call
*  curse of dimensionality. And so as the number of variables kind of grow, the number of decisions
*  you can make grows rapidly. Like if you have a hundred variables, each one of them take 10 values,
*  all possible assignments is more than the number of atoms in the universe. It's just crazy.
*  And that kind of thinking is just embodied in that one equation that I really like.
*  And the beautiful balance between it being theoretically optimal and somehow, practically
*  speaking, given the curse of dimensionality, nevertheless in practice works. Despite all those
*  challenges, which is quite incredible. Which is quite incredible. So I would say that it's kind
*  of like quite baffling actually. In a lot of fields that we think about how little we know.
*  And so I think here too, we know that in the worst case, things are pretty hard,
*  but in practice generally things work. So it's just kind of baffling and decision-making how
*  little we know. Just like how little we know about the beginning of time, how little we know about
*  our own future. If you actually go into from Balmain's equation all the way down,
*  there's also how little we know about mathematics. We don't even know if the axioms are
*  consistent. It's just crazy. I think a good lesson there, just like you said,
*  we tend to focus on the worst case or the boundaries of everything we're studying.
*  And then the average case seems to somehow work out. If you think about life in general,
*  we mess it up a bunch. We freak out about a bunch of the traumatic stuff, but in the end it seems
*  to work out okay. Yeah, it seems like a good metaphor. Sir, Tasha, thank you so much for
*  being a friend, a colleague, a mentor. I really appreciate it. It's an honor to talk to you.
*  Likewise. Thank you, Lex. Thanks for listening to this conversation with Sir Tash Karaman. And
*  thank you to our presenting sponsor, Cash App. Please consider supporting the podcast by downloading
*  Cash App and using code Lex Podcast. If you enjoy this podcast, subscribe on YouTube, review it with
*  five stars on Apple Podcasts, support it on Patreon, or simply connect with me on Twitter
*  at Lex Friedman. And now let me leave you with some words from Hal 9000 from the movie 2001,
*  A Space Odyssey. I'm putting myself to the fullest possible use, which is all I think
*  that any conscious entity can ever hope to do. Thank you for listening and hope to see you next time.
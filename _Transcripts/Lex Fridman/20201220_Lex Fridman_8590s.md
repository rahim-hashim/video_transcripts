---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 8590s
Video Keywords: ['dmitri dolgov', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 99410
Video Rating: None
Video Description: Dmitri Dolgov is the CTO of Waymo, an autonomous vehicle company. Please support this podcast by checking out our sponsors:
- Tryolabs: https://tryolabs.com/lex
- Blinkist: https://blinkist.com/lex and use code LEX to get 25% off premium
- BetterHelp: https://betterhelp.com/lex to get 10% off
- Cash App: https://cash.app/ and use code LexPodcast to get $10

EPISODE LINKS:
Waymo's Twitter: https://twitter.com/waymo
Waymo's Website: https://waymo.com

PODCAST INFO:
Podcast website: https://lexfridman.com/podcast
Apple Podcasts: https://apple.co/2lwqZIr
Spotify: https://spoti.fi/2nEwCF8
RSS: https://lexfridman.com/feed/podcast/
Full episodes playlist: https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist: https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

OUTLINE:
0:00 - Introduction
2:16 - Computer games
7:23 - Childhood
9:55 - Robotics
10:44 - Moscow Institute of Physics and Technology
12:56 - DARPA Urban Challenge
23:16 - Waymo origin story
38:58 - Waymo self-driving hardware
47:31 - Connected cars
53:23 - Waymo fully driverless service in Phoenix
57:45 - Getting feedback from riders
1:05:58 - Creating a product that people love
1:11:49 - Do self-driving cars need to break the rules like humans do?
1:18:33 - Waymo Trucks
1:24:11 - Future of Waymo
1:37:23 - Role of lidar in autonomous driving
1:50:23 - Machine learning is essential for autonomous driving
1:54:25 - Pedestrians
2:01:02 - Trolley problem
2:05:30 - Book recommendations
2:16:56 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Dmitri Dolgov Waymo and the Future of Self-Driving Cars  Lex Fridman Podcast #147
**Lex Fridman:** [December 20, 2020](https://www.youtube.com/watch?v=P6prRXkI5HM)
*  The following is a conversation with Dimitri Dolgov, the CTO of Waymo, which is an autonomous
*  driving company that started as Google's self-driving car project in 2009 and became Waymo in 2016.
*  Dimitri was there all along. Waymo is currently leading in the fully autonomous vehicle space
*  in that they actually have an at-scale deployment of publicly accessible autonomous vehicles
*  driving passengers around with no safety driver, with nobody in the driver's seat.
*  This, to me, is an incredible accomplishment of engineering on one of the most difficult
*  and exciting artificial intelligence challenges of the 21st century.
*  Quick mention of each sponsor followed by some thoughts related to the episode.
*  Thank you to Trial Labs, a company that helps businesses apply machine learning to solve real
*  world problems. Blinkist, an app I use for reading through summaries of books.
*  BetterHelp, online therapy with a licensed professional.
*  And Cash App, the app I use to send money to friends. Please check out the sponsors in the
*  description to get a discount at the support of this podcast. As a side note, let me say that
*  autonomous and semi-autonomous driving was the focus of my work at MIT and is a problem space
*  that I find fascinating and full of open questions from both a robotics and a human
*  psychology perspective. There's quite a bit that I could say here about my experiences in academia
*  on this topic that revealed to me, let's say, the less admirable sides of human beings.
*  But I choose to focus on the positive, on solutions, on brilliant engineers like Dmitri
*  and the team at Waymo who work tirelessly to innovate and to build amazing technology
*  that will define our future. Because of Dmitri and others like him, I'm excited for this future.
*  And who knows, perhaps I too will help contribute something of value to it.
*  If you enjoy this thing, subscribe on YouTube, review it with five stars on Apple Podcasts,
*  follow on Spotify, support on Patreon, or connect with me on Twitter at Lex Friedman.
*  And now, here's my conversation with Dmitri Dolgov.
*  When did you first fall in love with robotics or even computer science more in general?
*  Computer science first. At a fairly young age, robotics happened much later. I think my first
*  interesting introduction to computers was in the late 80s when we got our first computer. I think
*  it was an IBM, I think IBM AT. Remember those things that had like a turbo button in the front?
*  Turbo button.
*  The radio would press it and make the thing go faster.
*  Did that already have floppy disks?
*  Yeah, yeah, yeah. The 5.4 inch ones.
*  I think there was a bigger inch. So it went something, then five inches, then three inches.
*  Yeah, I think that was the five. Maybe before that was the giant plates, then it didn't get that.
*  But it was definitely not the three inch ones. Anyway, so we got that computer. I spent the first
*  few months just playing video games, as you would expect. I got bored of that. So I started messing
*  around and trying to figure out how to make the thing do other stuff. I got into exploring
*  programming and a couple of years later, it got to a point where I actually wrote a game,
*  a little game. A Japanese game developer actually offered to buy it from me for a few hundred bucks,
*  but for a kid in Russia, it's a big deal. I did not take the deal.
*  Wow, integrity.
*  Yeah.
*  Stability.
*  Yes, that was not the most acute financial move that I made in my life. Looking back at it now,
*  I instead put it, well, I had a reason. I put it online. It was, what did you call it back in the
*  days? It was a freeware thing. It was not open source, but you could upload the binaries,
*  you would put the game online. And the idea was that people like it and then they contribute and
*  they send you a little donations. So I did my quick math of like, of course, thousands and millions
*  of people are going to play my game, send me a couple of bucks a piece. I should definitely do
*  that. As I said, not the best way.
*  You're already playing business models at that young age. Remember what language it was?
*  What program it was?
*  Pascal.
*  Which what?
*  Pascal.
*  Pascal. And they had a graphical component. So it's not text-based.
*  Yeah. Yeah. It was like, I think they were 320 by 200, whatever it was. I think that kind of the
*  earlier VGA resolution, right? And I actually think the reason why this company wanted to buy
*  it is not like the fancy graphics or the implementation. It was maybe the idea of the
*  actual game.
*  The idea of the game.
*  Okay. Well, one of the things I, it's so funny, I used to play this game called golden acts
*  and the simplicity of the graphics and something about the simplicity of the music, like
*  it still haunts me. I don't know if that's a childhood thing. I don't know if that's the
*  same thing for call of duty these days for young kids, but I still think that the
*  simple, when the games are simple, that simple purity makes for, like allows your imagination
*  to take over and thereby creating a more magical experience. Like now with better and better
*  graphics, it feels like your imagination doesn't get to create worlds, which is kind of
*  interesting. It could be just an old man on a porch, like waving at kids these days that
*  have no respect, but I still think that graphics almost get in the way of the experience.
*  I don't know.
*  Flip it bird.
*  Yeah. I don't know if the imagination gets closed. I don't. Yeah. But that that's more
*  about games that up like that's more like Tetris world where they optimally masterfully
*  like create a fun short-term dopamine experience versus I'm more referring to like
*  role-playing games where there's like a story. You can live in it for months or years.
*  Like there's an elder scroll series, which is probably my favorite set of games.
*  That was a magical experience and that the graphics are terrible.
*  The characters were all randomly generated, but they're, I don't know.
*  That's it pulls you in. There's a story. It's like an interactive version of an elder scrolls
*  Tolkien world and you get to live in it. I don't know. I miss it. It's one of the things that
*  suck about being an adult is there's no, you have to live in the real world as opposed to
*  the elder scrolls world. You know, whatever brings you joy, right?
*  Minecraft, right? Minecraft is a great example. You create like it's not the fancy graphics,
*  but it's the creation of your own worlds. Yeah, that one is crazy. You know, one of the pitches
*  for being a parent that people tell me is that you can like use the excuse of parenting to,
*  to go back into the video game world and like, like that's like, you know, father son, father,
*  father, daughter time, but really you just get to play video games with your kids. So anyway,
*  at that time, did you have any ridiculous ambitious dreams of where as a creator you might go?
*  As an engineer, did you, what did you think of yourself as, as an engineer,
*  as a tinker or did you want to be like an astronaut or something like that?
*  You know, I'm tempted to make something up about, you know, robots, uh, engineering or,
*  you know, mysteries of the universe, but that's not the actual memory that pops into my mind.
*  When you, when you ask me about childhood dreams, so I'll actually share the real thing.
*  Uh, when I was maybe four or five years old, I, you know, as we all do, I thought about,
*  you know, what I wanted to do when I grow up and I had this dream of being a traffic control cop.
*  You know, they don't have those today's I think, but you know, back in the eighties and, you know,
*  in Russia, uh, you probably are familiar with that. Like they had these, uh, you know,
*  police officers that would stand in the middle of intersection all day and they would have their
*  like stripe back and white batons that they would use to control the flow of traffic.
*  And, you know, for whatever reasons, I was strangely infatuated with this whole process.
*  And like that, that was my dream. Uh, that's what I wanted to do when I grew up. And, you know,
*  my parents, uh, both physics profs, by the way, I think were, you know, a little concerned, uh,
*  with that level of ambition coming from their child. Uh, you know, that age,
*  well, that it's an interesting, I don't know if you can relate, but I very much loved that idea.
*  I have a OCD nature that I think lends itself very close to the engineering mindset,
*  which is you want to kind of optimize, you know, solve a problem by creating an automated
*  solution, like a, like a set of rules, that set of rules that you follow and then thereby make
*  it ultra efficient. I don't know if that's, it was of that nature. I certainly have that.
*  There's like fact, like SimCity and factory building games, all those kinds of things
*  kind of speak to that engineering mindset. Or did you just like the uniform?
*  I think it was more of the letter. I think, you know, the, you know, the, the stripe baton
*  that made cars go in the right directions. But I guess, you know, it is, I did end up, uh, I guess,
*  you know, working on the transportation industry one way or another.
*  No uniform, no.
*  But that's right. Maybe it was my, you know, deep inner infatuation with the,
*  you know, traffic control batons that led to this career.
*  Okay. What, uh, when did you, when was the leap from programming to robotics?
*  That happened later. That was after grad school. Uh, after, and actually they were
*  self-driving cars was I think my first real hands-on introduction to robotics.
*  But I never really had that much hands-on experience in school and training. I worked
*  on applied math and physics. Then in college, I did more abstract computer science. Uh, and
*  it was after grad school that I really got involved in robotics, which was actually self-driving cars.
*  And, you know, that was a big, big flip.
*  What, uh, what grad school?
*  So I went to grad school in Michigan, and then I did a postdoc at Stanford,
*  which is that was the postdoc where I got to play with self-driving cars.
*  Yeah. So we'll return there. Let's go back to, uh, to Moscow. So I, you know, for episode 100,
*  I talked to my dad and also I grew up with my dad, I guess.
*  So I had to put up with them for many years and, uh, he, he went to the Fistia or MIPT.
*  It's weird to say in English because I've heard all of this in Russian,
*  Moscow Institute of Physics and Technology. And to me, that was like,
*  I met some super interesting as a child, I met some super interesting characters.
*  It felt to me like the greatest university in the world, the most elite university in the world.
*  And just the people that I met that came out of there were like,
*  uh, not only brilliant, but also special humans. It seems like that place really tested the soul,
*  both like in terms of technically and like spiritually. So that could be just the
*  romanticization of that place. I'm not sure, but so maybe you can speak to it, but did,
*  is it correct to say that you spent some time at Fistia?
*  Yeah, that's right. Six years. Uh, I got my bachelor's and master's and physics and math there.
*  And it was actually interesting because my, my dad, and actually both my parents, uh, went there.
*  And I think all the stories that I heard, uh, like just like you, uh, like, uh, growing up
*  about the place and, you know, how interesting and special and magical it was. I think that was
*  a significant, maybe the main reason, uh, I wanted to go there, uh, for college. Uh, enough so that I
*  actually went back to Russia from the U S I graduated high school in the U S. Um, and
*  You went back there.
*  I went back there. Yeah. That exactly the reaction. Most of my peers in college had,
*  but, you know, perhaps a little bit stronger that like, you know, point me out as this crazy kid.
*  Were your parents supportive of that?
*  Yeah. Yeah. I can, as your previous question, they, uh, they supported me and, you know,
*  letting me pursue my passions and the things that I was interested in.
*  That's a bold move. Wow. What was it like there?
*  It was interesting, you know, definitely fairly hardcore on the fundamentals of,
*  you know, math and physics and, uh, you know, lots of good memories from, you know, from those times.
*  So, okay. So Stanford, how'd you get into autonomous vehicles?
*  I had the great fortune, uh, and great honor to join Stanford's DARPA urban challenge team in 2006.
*  There, this was a third in the sequence of the DARPA challenges. There's two grand challenges
*  prior to that. And then in 2007, they held the DARPA urban challenge. So, you know,
*  I was doing my postdoc. I had, I joined the team and, uh, worked on motion planning, uh, for,
*  you know, that, that competition.
*  So, okay. So for people who might not know, I know from, from a certain,
*  autonomous vehicles is a funny world in a certain circle of people, everybody knows everything.
*  And then a certain circle, uh, nobody knows anything in terms of general public. So it's
*  interesting. It's, it's a good question of what to talk about, but I do think that the urban challenge
*  is worth revisiting. It's a fun little challenge. One that, first of the like sparked so much,
*  so many incredible minds to focus on one of the hardest problems of our time in artificial
*  intelligence. So that's, that's a success from a perspective of a single little challenge.
*  But can you talk about like, what did the challenge involve? So were there pedestrians,
*  were there other cars? What was the goal? Uh, who was on the team? How long did it take?
*  Any fun, fun sort of specs?
*  Sure, sure, sure. So the way that the challenge was constructed, and just a little bit of
*  background, as I mentioned, this was the third, uh, competition in that series. The first two
*  were the grand challenge, called the grand challenge. The goal there was to just drive
*  in a completely static environment. I had to drive in a desert, uh, that was very successful.
*  So then DARPA followed with what they called the urban challenge, where the goal was to have,
*  you know, build vehicles that could operate in more dynamic environments and share them with other
*  vehicles. There were no pedestrians there, but what DARPA did is they took over an abandoned
*  Air Force base, uh, and it was kind of like a little fake city that they built out there.
*  And they had a bunch of, uh, robots, uh, you know, cars that were autonomous, uh, in there,
*  all at the same time, uh, mixed in with other vehicles driven by professional drivers. And each
*  car, uh, had a mission, right? So there's a crude map that they received, uh, in the beginning,
*  and they had a mission, you know, go here and then there and over here. Um, and they kind of
*  all were sharing this environment at the same time they had to interact with each other. They
*  had to interact with the human drivers. So it's this very first, very rudimentary, um, version
*  of, uh, a self-driving car that, you know, could operate, uh, and on, uh, in an environment,
*  you know, shared with other dynamic actors that, as you said, you know, really, in many ways,
*  you know, kickstarted this whole industry. Okay. So who was on the team and how'd you do? I forget.
*  It came in second. Uh, perhaps that was my contribution to the team. I think the Stanford
*  team came in first in the DARPA challenge, uh, but then I joined the team and, you know,
*  you were the one with the bug in the code. I mean, do you have sort of memories of some
*  particularly challenging things or, you know, one of the cool things it's not, you know,
*  this isn't a product. This isn't the thing that, uh, you know, it, there's, you have a little bit
*  more freedom to experiment so you can take risks and there's, uh, so you can make mistakes. Uh,
*  so is there interesting mistakes? Is there interesting challenges that stand out to you?
*  Or something like taught you, uh, a good technical lesson or a good philosophical lesson
*  from that time? Yeah, uh, you know, definitely, definitely very memorable time, not really
*  challenged, but like one of the most vivid memories that I have from the time. And I think
*  that was actually one of the days that really got me hooked, uh, on this whole field was
*  the first time I got to run my software on the car. And I was working on a part of our planning
*  algorithm, uh, that had to navigate in parking lots. So it was something that, you know, called
*  free space motion planning. So the very first version of that, uh, was, you know, we tried on
*  the car. I was on Stanford's campus, uh, in the middle of the night and you had this little,
*  you know, course constructed with cones, uh, in the middle of a parking lot. So we're there
*  in like 3 a.m. You know, by the time we got the code to, you know, uh, uh, you know, compile and
*  turn over, uh, and you know, it drove, I could actually did something quite reasonable. And,
*  yeah, it was of course very buggy at the time and had all kinds of problems, but it was pretty
*  darn magical. I remember going back and, you know, you know, later at night and trying to fall asleep
*  and just being unable to fall asleep for the rest of the night, uh, just my mind was blown.
*  I was just like, and that, that, that's what I've been doing ever since for more than a decade. Uh,
*  in terms of challenges and, uh, you know, interesting memories, like on the day of the
*  competition, uh, it was pretty nerve-racking. Uh, I remember standing there with Mike Montemariello,
*  who was, uh, the software lead and wrote most of the code. I got that one little part of the
*  planner, Mike, you know, incredibly that, you know, pretty much the rest of it, uh, with, with,
*  you know, a bunch of other incredible people. But I remember standing on the day of the competition,
*  uh, you know, watching the car, you know, with Mike and, you know, cars are completely empty,
*  right? They're all there lined up in the beginning of the race. And then, you know,
*  DARPA sends them, you know, uh, on their mission one by one, so then leave. And like, you just,
*  they had these sirens, they all had their different silence, silence, right? Each siren had its own
*  personality, if you will. So, you know, off they go and you don't see them. You just kind of,
*  and then every once in a while, they, you know, come a little bit closer to where, uh, the audiences
*  and you can kind of hear, you know, the sound of your car and, you know, it seems to be moving
*  along. So that, you know, gives you hope. And then, you know, it goes away and you can't hear it for
*  too long. You start getting anxious, right? So it's a little bit like, you know, sending your
*  kids to college and like, you know, kind of you invested in them. You hope you, you, you, you,
*  you build it properly, but like it's still anxiety inducing. Uh, so that was an incredibly, uh, fun
*  a few days in terms of, you know, bugs. As you mentioned, you know, one that was my bug that
*  caused us the loss of the first place, uh, is still a debate that, you know, occasionally have with
*  people on the CMU team. CMU came first. I should mention, uh, that- CMU haven't heard of them,
*  but yeah, it's something, you know, it's a small school. It's, it's, it's, yeah,
*  it's a really glitch that, you know, they haven't succeeded something robotics related.
*  Very scenic though. So most people go there for the scenery. Um, yeah, it's a beautiful campus.
*  I apologize.
*  Unlike Stanford.
*  So for people, yeah, that's true. Unlike Stanford, for people who don't know, CMU is one of the great
*  robotics and sort of artificial intelligence universities in the world. CMU Carnegie Mellon
*  University. Okay. Sorry. Go ahead. Good, good PSA. So in the part that I contributed to,
*  which was navigating parking lots and the way, you know, that part of the mission work is,
*  you, in a parking lot, you would get from DARPA an outline of the map. You basically get this,
*  you know, giant polygon that defined the perimeter of the parking lot. Uh, and there would be an
*  entrance and maybe multiple entrances or exits to it. And then you would get a goal, uh, within
*  that open space, uh, X, Y, you know, heading where the car had to park. It had no information about
*  the optical obstacles that the car might encounter there. So it had to navigate, uh, kind of completely
*  free space from the entrance to the parking lot into that parking space. And then, uh, once
*  you're parked there, it had to, uh, exit the parking lot while of course,
*  in counting and reasoning about all the obstacles that it encounters in real time. So, uh,
*  our interpretation, or at least my interpretation of the rules was that you had to reverse out of
*  the parking spot. And that's what our cars did, even if there's no obstacle in front,
*  that's not what CMU's car did. And it just kind of drove right through. So there's still a debate.
*  And of course, you know, as you stop and then reverse out and go out the different way that
*  costs you some time. Right. So there's still a debate whether, you know, it was my poor
*  implementation that cost us extra time or whether it was, you know, CMU, uh, violating
*  an important rule of the competition. And, you know, I have my own, uh, opinion here in terms of
*  other bugs. And like, uh, I have to apologize to Mike Montemariella, uh, for sharing this on air,
*  but it is actually one of the more memorable ones. Uh, and it's something that's kind of become a
*  bit of a metaphor and a label in the industry since then, I think, at least in some circles,
*  it's called the victory circle or victory lap. Um, and, uh, our cars did that. So in one of the
*  missions in the urban challenge, in one of the courses, uh, there was this big oval right by the
*  start and finish of the race. So the ARPA had a lot of the missions would finish kind of in that
*  same location. Uh, and it was pretty cool because you could see the cars come by, you know, kind of
*  finish that part leg of the trip, that leg of the mission, and then go on and finish the rest of it.
*  Uh, and other vehicles would come hit their way point, uh, and exit the oval and off they would go.
*  Our car in the hand, which hit the checkpoint, and then it would do an extra lap around the oval and
*  only then, you know, leave and go on its merry way. So over the course of the full day, it accumulated
*  some extra time. And the problem was that we had a bug where it wouldn't, you know, start reasoning
*  about the next way point and plan a route to get to that next point until it hit a previous one.
*  And in that particular case, by the time you hit the, that, that one, it was too late for us
*  to consider the next one and kind of make a lane change. So at every time we would do like an extra
*  lap. So that's the Stanford victory lap. Oh, that's, there's, I feel like there's something
*  philosophically profound in there somehow, but, uh, I mean, ultimately everybody is a winner in that
*  kind of competition. And it led to sort of famously to the creation of, um, Google self-driving car
*  project and now Waymo. So can we, uh, give an overview of how was way more born? How's the
*  Google self-driving car project born? Was the, what is the mission? What is the hope? What is it is the
*  engineering kind of, uh, set of milestones that it seeks to accomplish? There's a lot of questions
*  in there. Yeah. Uh, but you're right. It kind of the DARPA urban challenge and the DARPA,
*  previous DARPA grand challenges, uh, kind of led I think to a very large degree to that next step.
*  And then, you know, Larry and Sergey, um, Larry Page and Sergey Bren, uh, uh, Google founders
*  scores, you know, I saw that competition and believed in the technology. So, you know, the Google
*  self-driving car project was born, you know, at that time and we started in 2009, it was a pretty
*  small group of us, about a dozen people, uh, who came together, uh, to, to work on, on this project
*  at Google at that time, we saw an incredible early result in the DARPA urban challenge. I think we're
*  all incredibly excited about where we got to and we believed in the future of the technology, but we
*  still had a very, you know, rudimentary understanding of the problem space. So the first goal of this
*  project in 2009 was to really better understand what we're up against. Uh, and, you know, with that
*  goal in mind, when we started the project, we created a few milestones for ourselves, uh, that
*  maximize learnings. Well, the two milestones were, you know, uh, one was to drive a hundred thousand
*  miles in autonomous mode, which was at that time, you know, orders of magnitude that, you know,
*  more than anybody has ever done. And the second milestone was to drive 10 routes. Uh, each one was
*  a hundred miles long. Uh, and they were specifically chosen to become extra spicy, you know, extra
*  complicated and sample the full complexity of the, uh, that, that, uh, domain. Um, uh, and you had to
*  drive each one from beginning to end with no intervention, no human intervention. So you would
*  get to the beginning of the course, uh, you would press the button that would engage in autonomy,
*  and you had to go for a hundred miles, you know, beginning to end, uh, with no interventions. Um,
*  and it sampled again, the full complexity of driving conditions. Some, uh, were on freeways.
*  We had one route that went all through all the freeways and all the bridges in the Bay area.
*  You know, we had, uh, some that went around Lake Tahoe and kind of mountainous, uh, roads. We had
*  some that drove through dense urban, um, environments like in downtown Palo Alto and
*  through San Francisco. So it was incredibly, uh, interesting, uh, to work on. And it, uh,
*  it took us just under two years, uh, about a year and a half, a little bit more to finish both of
*  these milestones. And in that process, uh, you know, it was an incredible amount of fun, probably
*  the most fun I had in my professional career. And you're just learning so much. You are, you know,
*  the goal here is to learn a prototype. You're not yet starting to build a production system, right?
*  So you just, you were, you know, this is when you're kind of, you know, working 24 seven and
*  you're hacking things together. And you also don't know how hard this is. I mean, it's the point
*  like, so, I mean, that's an ambitious, if I put myself in that mindset, even still,
*  that's a really ambitious set of goals. Like just those two, just picking, picking 10 different
*  difficult, spicy challenges and then having zero interventions. So like not saying gradually,
*  we're going to like, you know, over a period of 10 years, we're going to have a bunch of roots
*  and gradually reduce the number of interventions. You know, that literally says like by,
*  as soon as possible, we want to have zero and on hard roads. So like to me, if I was facing that,
*  it's unclear that whether that takes two years or whether that takes 20 years.
*  I mean, it took us under two. I guess that that speaks to a really big difference between doing
*  something once and having a prototype where you're going after, you know, learning about the
*  problem versus how you go about engineering a product that, you know, where you look at,
*  you know, do you do properly do evaluation, you look at metrics, you know, drive down and
*  you're confident that you can do that at high. And I guess that's the, you know, why it took
*  a dozen people, you know, 16 months or a little bit more than that back in 2009 and 2010 with the
*  technology of, you know, the more than a decade ago, that amount of time to achieve that milestone
*  of 10 routes, a hundred miles each and no interventions. And, you know, it took us a
*  little bit longer to get to a full driverless product that customers use. That's another really
*  important moment. Is there some memories of technical lessons or just one, like what did
*  you learn about the problem of driving from that experience? I mean, we can, we can now talk about
*  like what you learned from modern day Waymo, but I feel like you may have learned some profound things
*  in those early days, even more so because it feels like what Waymo is now is to trying to,
*  you know, how to do scale, how to make sure you create a product, how to make sure it's like
*  safety and all those things, which is all fascinating challenges, but like you were facing
*  the more fundamental philosophical problem of driving in those early days. Like what the hell
*  is driving as an autonomous or maybe I'm again romanticizing it, but is it, is there, is there
*  some valuable lessons you picked up over there at those two years? A ton. The most important one is
*  probably that we believe that it's doable and we've gotten far enough into the problem that,
*  you know, we had a, I think only a glimpse of the true complexity of the domain. You know,
*  it's a little bit like, you know, climbing a mountain where you kind of, you know, see the
*  next peak and you think that's kind of the summit, but then you get to that and you kind of see that
*  that this is just the start of the journey. But we've tried, we've sampled enough of the problem
*  space and we've made enough rapid success, even, you know, with technology of 2009, 2010,
*  that it gave us confidence to then pursue this as a real product. So, okay. So the next step,
*  you mentioned the milestones that you had in those two years. What are the next milestones
*  that then led to the creation of Waymo and beyond? It was a really interesting journey. And, you know,
*  Waymo came a little bit later. Then, you know, we completed those milestones in 2010. That was the
*  pivot when we decided to focus on actually building a product, you know, using this technology.
*  The initial couple of years after that, we were focused on a freeway, you know, what you would
*  call a driver assist, maybe, you know, an L3 driver assist program. Then around 2013, we've learned
*  enough about the space and have thought more deeply about, you know, the product that we
*  wanted to build that we pivoted. We pivoted towards this vision of building a driver and
*  deploying it fully driverless vehicles without a person. And that's the path that we've been
*  on since then. And it was exactly the right decision for us. So there was a moment where
*  you're also considered like, what is the right trajectory here? What is the right role of
*  automation in the task of driving? There was still, it wasn't from the early days,
*  obviously, you want to go fully autonomous. From the early days, it was not. I think it was in
*  around 2013, maybe, that we've, that became very clear. And we made that pivot and it also became
*  very clear. And that it's, the way you go building a driver assist system is fundamentally different
*  from how you go building a fully driverless vehicle. So, you know, we've pivoted towards
*  the ladder. And that's what we've been working on ever since. And so that was around 2013. Then
*  there's a sequence of really meaningful for us really important defining milestones since then.
*  In 2015, we had our first, actually the world's first fully driverless ride on public roads. It
*  was in a custom built vehicle that we had. You must have seen those. We called them the Firefly,
*  that funny looking marshmallow looking thing. And we put a passenger, his name was Steve Mann,
*  great friend of our project from the early days. The man happens to be blind. So we put him in that
*  vehicle. The car had no steering wheel, no pedals. It was an uncontrolled environment.
*  No lead or chase cars, no police escorts. And we did that trip a few times in Austin, Texas. So
*  that was a really big milestone. But that was in Austin. Yeah. Cool. Okay. And we only, but at that
*  time, we're only, it took a tremendous amount of engineering. It took a tremendous amount of
*  validation to get to that point. But we only did it a few times. We only did that. It was a fixed
*  route. It was not kind of a controlled environment, but it was a fixed route. And we only did it a few
*  times. Then in 2016, end of 2016, beginning of 2017 is when we founded Waymo, the company.
*  That's when we kind of, that was the next phase of the project where I wanted, we believed in kind
*  of the commercial vision of this technology. And it made sense to create an independent entity
*  within that alphabet umbrella to pursue this product at scale. Beyond that in 2017, later in
*  2017, it was another really huge step for us, really big milestone where we started, I think
*  it was October of 2017, where when we started regular driverless operations on public roads,
*  that first day of operations, we drove in one day, and that first day, a hundred miles in
*  driverless fashion. And then we've, the most important thing about that milestone was not that
*  hundred miles in one day, but that it was the start of kind of regular ongoing driverless operations.
*  And when you say driverless, it means no driver.
*  That's exactly right. So on that first day, we actually had a mix and up in some, we didn't want
*  to like, you know, be on YouTube and Twitter that same day. So in many of the rides, we had somebody
*  in the driver's seat, but they could not disengage. Like the car, not disengaged. But actually on that
*  first day, some of the miles were driven and just completely empty driver's seat. This is the key
*  distinction that I think people don't realize is, you know, that oftentimes when you talk about
*  autonomous vehicles, there's often a driver in the seat that's ready to take over what's called a
*  safety driver. And then Waymo is really one of the only companies at least that I'm aware of,
*  or at least as like boldly and carefully and all that is actually has cases. And now we'll talk
*  about more and more where there's literally no driver. So that's another interesting case of
*  where the driver is not supposed to disengage. That's like a nice middle ground. They're still
*  there, but they're not supposed to disengage. But really there's the case when there's no,
*  okay, there's something magical about there being nobody in the driver's seat.
*  Like, just like to me, you mentioned the first time you wrote some code for free space
*  navigation of the parking lot. That was like a magical moment to me, just sort of an, as an
*  observer of robots. The first magical moment is seeing an autonomous vehicle turn, like make a
*  left turn, like apply sufficient torque to the steering wheel to where it, like, there's a lot
*  of rotation. And for some reason, and there's nobody in the driver's seat for some reason that,
*  that communicates that here's a being with power that makes a decision. There's something about
*  like the steering wheel, because we perhaps romanticize the notion of the steering wheel.
*  It's so essential to the, our conception, our 20th century conception of a car and it turning
*  the steering wheel with nobody in driver's seat that to me, I think maybe to others,
*  it's really powerful. Like this thing is in control. And then there's this leap of trust that you give
*  I'm going to put my life in the hands of this thing that's in control. So in that sense,
*  when there's no, but no driver in the driver's seat, that's a magical moment for robots. So I,
*  I got the chance to last year to take a ride in a, in a Waymo vehicle. And that, that was the
*  magical moment. There's like nobody in the driver's seat. It's, it's like the little details. You would
*  think it doesn't matter whether there's a driver or not, but like if there's no driver and the
*  steering wheel is turning on its own, I don't know. That's magical. It's absolutely magical.
*  I, I taken many of these rides and like completely empty car, no human in the car pulls up. You know,
*  you call it on your cell phone, it pulls up, you get in, it takes you on its way. There's nobody
*  in the car, but you, right? That's something called, you know, fully driverless,
*  you know, our rider only mode of operation. Yeah, it, it is magical. It is transformative.
*  This is what we hear from our riders. It really changes your experience. And not like that,
*  that really is what unlocks the real potential of this technology. But, you know, coming back to
*  our journey, you know, that was 2017 when we started, you know, truly driverless operations.
*  Then in 2018, we've launched our public commercial service that we called Waymo One in Phoenix.
*  In 2019, we started offering truly driverless rider only rides to our early rider population
*  of users. And then, you know, 2020 has also been a pretty interesting year. One of the first ones,
*  less about technology, but more about the maturing and the growth of Waymo as a company.
*  We raised our first round of external financing this year, you know, we were part of Alphabet.
*  So obviously we have access to significant resources, but as kind of on the journey of
*  Waymo maturing as a company, it made sense for us to, you know, partially go externally
*  in this round. So, you know, we raised about $3.2 billion with from, you know, that round.
*  We've also, you know, started putting our fifth generation of our driver, our hardware,
*  that is on the new vehicle, but it's also a qualitatively different set of self-driving
*  hardware that is now on the JLR pace. So that was a very important step for us.
*  Hardware, specs, fifth generation. I think it'd be fun to maybe,
*  I apologize if I'm interrupting, but maybe talk about maybe the generations with a focus on what
*  we're talking about in the fifth generation in terms of hardware specs, like what's on this car.
*  Sure. So we separated out the actual car that we are driving from the self-driving hardware we
*  put on it. Right now we have, so this is, as I mentioned, the fifth generation, we've gone
*  through, we started building our own hardware, you know, many, many years ago, and
*  that Firefly vehicle also had the hardware suite that was mostly, you know, design engineered and
*  built in-house. Lighters are one of the more important components that we design and build
*  from the ground up. So on the fifth generation of our drivers, of our self-driving hardware that
*  we're switching to right now, we have, as with previous generations in terms of sensing, we have
*  lighters, cameras, and radars. And we have a pretty beefy computer that processes all that
*  information and makes decisions in real time on board the car. So in all of the, and it's really
*  qualitative jump forward in terms of the capabilities and the various parameters and
*  the specs of the hardware compared to what we had before and compared to what you can kind of get
*  off the shelf in the market today. Meaning from fifth to fourth or from fifth to first?
*  Definitely from first to fifth, but also from the fourth. That was the world's dumbest question.
*  Definitely from fourth to fifth, as well as the last step is a big step forward.
*  So everything's in-house, so like lighters built in-house and cameras are built in-house?
*  We work with partners and there's some components that we get from our manufacturing and
*  supply chain partners. What exactly is in-house is a bit different. We do a lot of custom
*  design on all of our sensing models. There's lighters, radars, cameras. Exactly, there's
*  lighters are almost exclusively in-house and some of the technologies that we have,
*  some of the fundamental technologies there are completely unique to Waymo. That is also largely
*  true about radars and cameras. It's a little bit more of a mix in terms of what we do ourselves
*  versus what we get from partners. Is there something super sexy about the computer that
*  you can mention that's not top secret? Like for people who enjoy computers? There's a lot of
*  machine learning involved, but there's a lot of just basic compute. You have to probably do a lot
*  of signal processing on all the different sensors. You have to integrate everything. It has to be in
*  real time. There's probably some kind of redundancy type of situation. Is there something interesting
*  you can say about the computer for the people who love hardware? It does have all of the
*  characteristics, all the properties that you just mentioned. Redundancy, very beefy compute
*  for general processing as well as inference and ML models. It is some of the more sensitive stuff
*  that I don't want to get into for IP reasons, but we've shared a little bit in terms of the specs
*  of the sensors that we have on the car. We actually shared some videos of what our
*  lighter see in the world. We have 29 cameras. We have five lighters. We have six radars
*  on these vehicles. You can get a feel for the amount of data that they're producing. That all
*  has to be processed in real time to do perception, to do complex reasoning. It gives you some idea of
*  how beefy those computers are, but I don't want to get into specifics of exactly how we build them.
*  LW Okay. Well, let me try some more questions that you can get into the specifics of. GPU-wise,
*  is that something you can get into? I know that Google works with GPUs and so on. For machine
*  learning folks, it's kind of interesting. Or is there no ... How do I ask it? I've been talking
*  to people in the government about UFOs and they don't answer any questions. This is how I feel
*  right now, asking about GPUs. But is there something interesting that you could reveal
*  or leave it up to our imagination, some of the compute? Is there any fun trickery? I talked to
*  Chris Latner for a second time and he was a key person about GPUs. There's a lot of fun stuff going
*  on in Google in terms of hardware that optimizes for machine learning. Is there something you can
*  reveal in terms of how much ... You mentioned customization. How much customization there is
*  for hardware for machine learning purposes? LW I'm going to be like that government person
*  about UFOs. I guess I will say that it's really ... Compute is really important. We have very
*  data-hungry and compute-hungry ML models all over our stack. This is where both being part of
*  Alphabet as well as designing our own sensors and the entire hardware suite together, where on one
*  hand you get access to really rich raw sensor data that you can pipe from your sensors
*  into your compute platform and build a whole pipe from sensor raw sensor data to the big compute as
*  we then have the massive compute to process all that data. This is where we're finding that having
*  a lot of control of that hardware part of the stack is really advantageous. One of the fascinating
*  magical places to me, again, might not be able to speak to the details, but it is the other compute
*  which is like ... We're just talking about a single car, but the driving experience is a source of a
*  lot of fascinating data and you have a huge amount of data coming in on the car. The infrastructure
*  of storing some of that data to then train or to analyze or so on, that's a fascinating
*  piece of it that I understand a single car, I don't understand how you pull it all together
*  in a nice way. Is that something that you could speak to in terms of the challenges of
*  seeing the network of cars and then bringing the data back and analyzing things like edge
*  cases of driving, be able to learn on them to improve the system to see where things went wrong
*  or where things went right and analyze all that kind of stuff. Is there something interesting there
*  from an engineering perspective? There's an incredible amount of really interesting work
*  that's happening there, both in the real time operation of the fleet of cars and the information
*  that they exchange with each other in real time to make better decisions, as well as the off-board
*  component where you have to deal with massive amounts of data for training your ML models,
*  evaluating the ML models, for simulating the entire system and for evaluating your entire system.
*  This is where being part of Alphabet has once again been tremendously advantageous. We consume
*  an incredible amount of compute for ML infrastructure. We build a lot of custom
*  frameworks to get good at data mining, finding the interesting edge cases for training and for
*  evaluation of the system for both training and evaluating some components and subparts of the
*  system in various ML models, as well as evaluating the entire system and simulation. Okay, that first
*  piece that you mentioned that cars communicating to each other essentially, I mean through perhaps
*  through a centralized point, but that's fascinating too. How much does that help you? If you imagine
*  right now the number of Waymo vehicles is whatever, X. I don't know if you can talk to
*  what that number is, but it's not in the hundreds of millions yet. Imagine if the whole world is
*  Waymo vehicles. That changes potentially the power of connectivity. The more cars you have,
*  I guess actually if you look at Phoenix, because there's enough vehicles, there's enough,
*  when there's some level of density, you can start to probably do some really interesting stuff with
*  the fact that cars can negotiate, can communicate with each other and thereby make decisions. Is
*  there something interesting there that you can talk to about how does that help with the driving
*  problem as compared to just a single car solving the driving problem by itself? Yeah, it's a spectrum.
*  First, I'd say that it helps and it helps in various ways, but it's not required. Right now,
*  the way we build our system, each car can operate independently. They can operate with no connectivity.
*  I think it is important that you have a fully autonomous, fully capable
*  computerized driver that each car has. Then they do share information and they share information
*  in real time and it really helps. The way we do this today is whenever one car encounters something
*  interesting in the world, whether it might be an accident or a new construction zone, that information
*  immediately gets uploaded over the air and is propagated to the rest of the fleet. That's how
*  we think about maps as priors in terms of the knowledge of our fleet of drivers that is
*  distributed across the fleet and it's updated in real time. That's one use case. You can imagine as
*  the density of these vehicles go up that they can exchange more information in terms of what
*  they're planning to do and start influencing how they interact with each other as well as
*  potentially sharing some observations to help with if you have enough density of these vehicles where
*  one car might be seeing something that another is relevant to another car that is very dynamic.
*  It's not part of you're updating your static prior of the map of the world, but it's more
*  of a dynamic information that could be relevant to the decisions that another car is making in
*  real time. You can see them exchanging that information and you can build on that. Again,
*  I see that as an advantage, but it's not a requirement. What about the human in the loop?
*  When I got a chance to drive or ride in a Waymo, there's customer service.
*  There is somebody that's able to dynamically tune in and help you out.
*  What role does the human play in that picture? That's fascinating. The idea of teleoperation
*  being able to remotely control a vehicle. Here what we're talking about is frictionless,
*  so here what we're talking about is like a human being able to in a frictionless way help you out.
*  I don't know if they're able to actually control the vehicle. Is that something you could talk to?
*  Yes. To be clear, we don't do teleoperation. I believe in teleoperation for a reason. That's
*  not what we have in our cars. We do, as you mentioned, have a version of customer support.
*  We call it life health. In fact, we find it that it's very important for our rider experience,
*  especially if it's your first trip. You've never been in a fully driverless,
*  rider only Waymo vehicle. You get in, there's nobody there. You can imagine having all kinds of
*  questions in your head, like how this thing works. We've put a lot of thought into guiding
*  our riders, our customers through that experience, especially for the first time.
*  They get some information on the phone. If the fully driverless vehicle is used to service their
*  trip, when you get into the car, we have an in-car screen and audio that kind of guides them and
*  explains what to expect. They also have a button that they can push that will connect them to a
*  real life human being that they can talk to about this whole process. That's one aspect of it.
*  I should mention that there is another function that humans provide to our cars, but it's not
*  teleoperation. You can think of it a little bit more like fleet assistance, kind of like traffic
*  control that you have, where our cars, again, they're responsible on their own for making
*  all of the driving decisions that don't require connectivity. Anything that is safety or latency
*  critical is done purely autonomously by our onboard system. But there are situations where,
*  you know, if connectivity is available and a car encounters a particularly challenging situation,
*  you can imagine like a super hairy scene of an accident, the cars will recognize that it's an
*  off-nominal situation. They will do their best to come up with the right interpretation, the best
*  course of action in that scenario. But if connectivity is available, they can ask for
*  confirmation from a human assistant to kind of confirm those actions and perhaps provide a little
*  bit of kind of contextual information and guidance. So October 8th was when you're talking about the
*  was Waymo launched the public version of its fully driverless, that's the right term, I think,
*  service in Phoenix. Is that October 8th? That's right. It was the introduction of
*  fully driverless, rider-only vehicles into our public Waymo One service.
*  Okay. So that's amazing. So it's like anybody can get into Waymo in Phoenix?
*  That's right. So we previously had early people in our early rider program taking fully driverless
*  rides in Phoenix. And just a little while ago, we opened on October 8th, we opened that mode of
*  operation to the public. So I can download the app and go on a ride. There is a lot more demand right
*  now for that service than we have capacity. So we're kind of managing that, but that's exactly
*  the way you described it. Yeah, well, that's interesting. So there's more demand than you can
*  handle. What has been the reception so far? Okay, so this is a product, right? That's a whole other
*  discussion of how compelling of a product it is. Great. But it's also one of the most kind of
*  transformational technologies of the 21st century. So it's also a tourist attraction. It's fun to be
*  a part of it. So it'd be interesting to see like, what do people say? What have been the feedback
*  so far? Still early days, but so far, the feedback has been incredible, incredibly positive.
*  We asked them for feedback during the ride, we asked them for feedback after the ride as part
*  of their trip. We asked them some questions, we asked them to rate the performance of our driver.
*  Most by far, most of our drivers give us five stars in our app, which is absolutely great to see.
*  And yeah, that's and they're also giving us feedback on things we can improve. And that's
*  one of the main reasons we're doing this is Phoenix and over the last couple of years,
*  and every day today, we are just learning a tremendous amount of new stuff from our users.
*  There's no substitute for actually doing the real thing, actually having a fully driverless
*  product out there in the field with users that are actually paying us money to get from point A
*  to point B. So this is a legitimate, like there's a paid service. That's right.
*  And the idea is you use the app to go from point A to point B. And then what are the A's,
*  what's the freedom of the starting and ending places? It's an area of geography where that
*  service is enabled. It's a decent size of geography of territory. It's actually larger than
*  size of San Francisco. And within that, you have full freedom of selecting where you want to go.
*  Of course, there's some and on your app, you get a map, you tell the car where you want to be picked
*  up and where you want the car to pull over and pick you up. And then you tell it where you want
*  to be dropped off. And of course, there are some exclusions, right? You want to be where
*  in terms of where the car is allowed to pull over, right? So that you can't do. But besides that,
*  it's amazing. It's not like a fixed, just would be very, I guess, I don't know, maybe that's what's
*  the question behind your question, but it's not a preset set of destinations. So within the geographic
*  constraints within that area, anywhere else, it can be picked up and dropped off anywhere.
*  That's right. And people use them on all kinds of trips. And we have an incredible spectrum of
*  riders. I think the youngest actually have car scenes with them. And we have people taking their
*  kids on rides. I think the youngest riders we had on cars are one or two years old. And the full
*  spectrum of use cases, people can take them to schools, to go grocery shopping, to restaurants,
*  to bars, run errands, go shopping, et cetera, et cetera. You can go to your office, right?
*  The full spectrum of use cases. And people use them in their daily lives to get around.
*  And we see all kinds of really interesting use cases. And that's providing us incredibly
*  valuable experience that we then use to improve our product. So as somebody who's done a few long
*  rants with Joe Rogan and others about the toxicity of the internet and the comments
*  and the negativity in the comments, I'm fascinated by feedback. I believe that most people are good
*  and kind and intelligent and can provide even in disagreement, really fascinating ideas. So
*  on a product side, it's fascinating to me. How do you get the richest possible user feedback
*  to improve? What are the channels that you use to measure? Because you're no longer...
*  That's one of the magical things about autonomous vehicles. It's not... It's frictionless
*  interaction with the human. So you don't get to... It's just giving a ride. So how do you get
*  feedback from people in order to improve? Oh, yeah. Great question. Various mechanisms.
*  So as part of the normal flow, we ask people for feedback. As the car is driving around,
*  we have on the phone and in the car, and we have a touchscreen in the car, you can actually click
*  some buttons and provide real-time feedback on how the car is doing and how the car is handling
*  a particular situation, both positive and negative. So that's one channel. We have, as we
*  discussed, customer support or life help where if a customer has a question or he has some sort of
*  concern, they can talk to a person in real time. So that is another mechanism that gives us feedback.
*  At the end of a trip, we also ask them how things went. They give us comments and a star rating.
*  You know, we also ask them to explain what went well and what could be improved. And
*  our writers are providing very rich feedback there. A large fraction is very passionate,
*  very excited about this technology, so we get really good feedback. We also run UXR studies,
*  specific that go more in-depth, and we run both lateral and longitudinal studies,
*  where we have deeper engagement with our customers. We have our user experience research team
*  tracking over time. That's things about longitudinal. That's cool.
*  That's exactly right. And that's another really valuable feedback, source of feedback.
*  And we're just covering a tremendous amount. People go grocery shopping and they want to
*  20 bags of groceries in our cars. That's one workflow that you maybe don't think about
*  getting just right when you're building the driverless product. I have people who
*  bike as part of their trip. So they bike somewhere, then they get in our cars,
*  they take a part of their bike, they load it into our vehicle, then they go and that's
*  how they, where we want to pull over and how that get in and get out process works. It provides
*  us very useful feedback in terms of what makes a good pick up and drop off location. We get
*  really valuable feedback. And in fact, we had to do some really interesting work with high definition
*  maps and thinking about walking directions. If you imagine you're in a store, in some giant space,
*  and then you want to be picked up somewhere. If you just drop a pin at a current location,
*  which is maybe in the middle of a shopping mall, what's the best location for the car to come pick
*  you up? And you can have simple heuristics where you just kind of take your clean in distance
*  and find the nearest spot where the car can pull over that's closest to you. But oftentimes,
*  that's not the most convenient one. I have many anecdotes where that heuristic breaks in horrible
*  ways. One example that I often mention is somebody wanted to be dropped off in Phoenix.
*  We picked a location that was close, the closest to where the pin was dropped on the map in terms
*  of latitude and longitude. But it happened to be on the other side of a parking lot that had this
*  row of cacti. And the poor person had to walk all around the parking lot to get to where they
*  wanted to be in 110 degree heat. So that was the problem. So then we took all of that feedback from
*  our users and incorporate it into our system and improve it. Yeah, I feel like that requires
*  AGI to solve the problem of like, which is a very common case when you're in a big space of some kind,
*  like apartment building, it doesn't matter, it's some large space. And then you call the
*  Waymo from there, right? And whatever, it doesn't matter, ride share vehicle. And where is the pin
*  supposed to drop? I think that requires AGI. Okay, the alternative, which I think the Google
*  search engine is taught, is like, there's something really valuable about the perhaps slightly dumb
*  answer, but a really powerful one, which is like, what was done in the past by others? Like, what
*  was the choice made by others? That seems to be like in terms of Google search, when you have like
*  billions of searches, you could see which, like when they recommend what you might possibly mean,
*  they suggest based on not some machine learning thing, which they also do, but like on what was
*  successful for others in the past and finding a thing that they were happy with. Is that integrated
*  at all, Waymo, like what pickups worked for others? It is. I think you're exactly right. So there's
*  real, it's an interesting problem. Naive solutions have interesting failure modes. So there's
*  definitely lots of things that can be done to improve and both learning from what works,
*  but doesn't work in actual hail from getting richer data and getting more information about
*  the environment and richer maps. But you're absolutely right that there's something,
*  I think there's some properties of solutions that in terms of the effect that they have on users,
*  so much, much, much better than others, right? And predictability and understandability is important.
*  So you can have maybe something that is not quite as optimal, but is very natural and predictable
*  to the user and kind of works the same way all the time. And that matters, that matters a lot
*  for the user experience. But to get to the basics, the pretty fundamental property is that the car
*  actually arrives where you told it to ride. Like you can always change it, see it on the map,
*  and you can move it around if you don't like it. But like that property that the car actually shows
*  up on pin is critical, which, you know, where compared to some of the human driven analogs,
*  I think, you know, you can have more predictability. It's actually the fact, if I have my idea of a
*  little bit of a detour here, I think the fact that it's, you know, your phone and the car,
*  it's two computers talking to each other, can lead to some really interesting things we can do
*  in terms of the user interfaces, you know, both in terms of function, like the car actually shows up
*  exactly where you told it you want it to be. But also some really interesting things on the user
*  interface, like as the car is driving, as you call it, and it's on the way to come pick you up.
*  And of course, you get the position of the car and the route on the map. But and they actually
*  follow that route, of course. But it can also share some really interesting information about
*  what it's doing. So as you know, our cars, as they are coming to pick you up, if it's come,
*  if a car is coming up to a stop sign, it will actually show you that like it's there sitting,
*  because it's at a stop sign or a traffic light, which only that is got sitting on a red light.
*  So you know, the little things, right. But it's I find those little touch touches, really interesting,
*  really magical. And it's just, you know, little things like that, that you can do to kind of
*  delight your users. You know, this makes me think of there's some products that I just love. Like,
*  there's a there's a company called rev rev.com, where I like for this podcast, for example,
*  I can drag and drop a video. And then they do all the captioning. It's humans doing the captioning,
*  but they connect you, they automate automate everything of connecting you to the humans.
*  And they do the captioning and transcription. It's all effortless. And it like I remember when I
*  first started using them, it was like, life's good, like, because it was so painful to figure
*  that out earlier. The same thing with something called isotope RX, this company I use for cleaning
*  up audio, like the sound cleanup they do, it's like drag and drop, and it just cleans everything up
*  very nicely. Another experience like that I had with Amazon one click purchase, first time,
*  I mean, other places do that now, but just the effortlessness of purchasing, making it frictionless.
*  It kind of communicates to me, like, I'm a fan of design, I'm a fan of products,
*  that you can just create a really pleasant experience that the simplicity of it, the
*  elegance just makes you fall in love with it. So on the do you think about this kind of stuff? I mean,
*  that's exactly what we've been talking about. It's like the little details that somehow make
*  you fall in love with the product. Is that we went from like urban challenge days,
*  where love was not part of the conversation, probably. And to this point where there's a
*  where there's human beings, and you want them to fall in love with the experience.
*  Is that something you're trying to optimize for? Try to think about like, how do you create
*  experience that people love? Absolutely. I think that's the vision is removing any
*  friction or complexity from getting our users, our writers to where they want to go.
*  Making that as simple as possible. And then, you know, beyond that, just transportation,
*  making, you know, things and goods get to their destination as seamlessly as possible. I talked
*  about, you know, a drag and drop experience where I kind of express your intent and then,
*  you know, it just magically happens. And for our writers, that's what we're trying to get to is
*  you download an app, and you click and car shows up. It's the same car. It's very predictable. It's
*  a safe and high quality experience. And then it gets you in a very reliable, very convenient,
*  and frictionless way to where you want to be. And along the journey, I think we also want to
*  do little things to delight our users. Like the ride sharing companies, because they don't
*  control the experience, I think, they can't make people fall in love necessarily with the experience.
*  Or maybe they haven't put in the effort. But I think if I would just speak to the ride sharing
*  experience I currently have, it's just very convenient. But there's a lot of room for like
*  falling in love with it. Like we can speak to sort of car companies. Car companies do this well. You
*  can fall in love with a car, right? And be like a loyal car person, like whatever. Like I like badass
*  hot rods. I guess 69 Corvette. And at this point, you know, you can't really... Cars are so... Owning
*  a car is so 20th century man. But is there something about the Waymo experience where you
*  hope that people will fall in love with it? Because is that part of it? Or is it just about
*  making a convenient ride? Not ride sharing, I don't know what the right term is, but just a
*  convenient A to B autonomous transport? Or like do you want them to fall in love with Waymo?
*  Maybe elaborate a little bit. I mean, almost like from a business perspective, I'm curious.
*  How... Do you want to be in the background invisible? Or do you want to be
*  like a source of joy that's very much in the foreground?
*  I want to provide the best, most enjoyable transportation solution. And
*  that means building it, building our product and building our service in a way that people do.
*  Use in a very seamless, frictionless way in their day-to-day lives. And I think that does mean,
*  in some way, falling in love in that product, right? It just kind of becomes part of your
*  routine. It comes down, in my mind, to safety, predictability, and safety.
*  Safety, predictability of the experience, and privacy, I think, aspects of it, right?
*  You get the same car, you get very predictable behavior, and that is important, I think,
*  if you're going to use it in your daily life. Privacy, and when you're in a car, you can do
*  other things. You're spending a bunch, just another space where you're spending a significant part of
*  your life. So not having to share it with other people who you don't want to share it with,
*  I think, is a very nice property. Maybe you want to take a phone call or do something else in the
*  vehicle. And safety on the quality of the driving, as well as the physical safety of not having to
*  share that ride is important to a lot of people. What about the idea that when there's somebody,
*  like a human driving, and they do a rolling stop on a stop sign, sometimes you get a new
*  burlift or whatever, like human driver, and they can be a little bit aggressive as drivers.
*  It feels like not all aggression is bad. Now, that may be a wrong, again, 20th century conception
*  of driving. Maybe it's possible to create a driving experience. If you're in the back
*  busy doing something, maybe aggression is not a good thing. It's a very different kind of
*  experience, perhaps. But it feels like in order to navigate this world, you need to,
*  how do I phrase this? You need to bend the rules a little bit, or at least test the rules.
*  I don't know what language politicians use to discuss this, but whatever language they use,
*  you flirt with the rules. I don't know. But you have a bit of an aggressive way of driving that
*  asserts your presence in this world, thereby making other vehicles and people respect your
*  presence, and thereby allowing you to navigate through intersections in a timely fashion.
*  I don't know if any of that made sense, but how does that fit into the experience of driving
*  autonomously? Is that- It's a lot of sense. You're hitting on a very important point of
*  a number of behavioral components and parameters that make your driving feel
*  assertive and natural, comfortable, predictable. Our cars will follow rules. They will do the
*  safest thing possible in all situations. Let me be clear on that. But if you think of really,
*  really good drivers, just think about professional lemon drivers, they will follow the rules.
*  They're very, very smooth, and yet they're very efficient, but they're assertive. They're
*  comfortable for the people in the vehicle. They're predictable for the other people outside
*  the vehicle that they share the environment with. That's the kind of driver that we want to build.
*  Maybe there's a sport analogy there. You can do in very many sports, the true professionals
*  are very efficient in their movements. They don't do hectic flailing. They're smooth,
*  and precise, and they get the best results. That's the kind of driver that we want to build.
*  In terms of aggressiveness, yeah, you can roll through the stop signs. You can do crazy lane
*  changes. It typically doesn't get you to your destination faster. Typically not the safest or
*  most predictable, most comfortable thing to do. But there is a way to do both. That's what we're
*  doing. We're trying to build a driver that is safe, comfortable, smooth, and predictable.
*  Yeah, that's a really interesting distinction. I think in the early days of autonomous vehicles,
*  the vehicles felt cautious as opposed to efficient.
*  But when I rode in the Waymo, it was quite assertive. It moved pretty quickly.
*  Then one of the surprising feelings was that it actually went fast, and it didn't feel
*  awkwardly cautious. I've also programmed autonomous vehicles and everything I've ever
*  built felt either overly aggressive, especially when it was my code, or awkwardly cautious is
*  the way I would put it. Waymo's vehicle felt like assertive, and I think efficient is the right
*  terminology here. I also like the professional limo driver, because we often think an Uber
*  driver or a bus driver or a taxi... The funny thing is people think taxi drivers are professionals.
*  They... I mean, that's like saying I'm a professional walker just because I've been
*  walking all my life. I think there's an art to it, right? If you take it seriously as an art form,
*  then there's a certain way that mastery looks like. It's interesting to think about what
*  does mastery look like in driving. Perhaps what we associate with aggressiveness is unnecessary
*  it's not part of the experience of driving. It's like unnecessary fluff, that efficiency...
*  You can create a good driving experience within the rules.
*  You're the first person to tell me this, so it's kind of interesting. I need to think about this,
*  but that's exactly what it felt like with Waymo. I kind of had this intuition, maybe it's the
*  Russian thing, I don't know, that you have to break the rules in life to get anywhere.
*  But maybe, maybe it's possible that that's not the case
*  in driving. I have to think about that. But it certainly felt that way on the streets of Phoenix
*  when I was there in Waymo, that that was a very pleasant experience and it wasn't frustrating in
*  that like, come on, move already kind of feeling. That wasn't there.
*  Yeah, I mean, that's what we're going after. I don't think you have to pick one. I think
*  truly good driving gives you both efficiency, assertiveness, but also comfort and predictability
*  and safety. That's what fundamental improvements in the core capabilities truly unlock. You can
*  kind of think of it as a precision and recall trade-off. You have certain capabilities of your
*  model and then it's very easy when you have some curve of precision and recall, you can move things
*  around and can choose your operating point and your trading of precision versus recall, false
*  positives versus false negatives. But then, and you can tune things on that curve and be kind of
*  more cautious or more aggressive, but then aggressive is bad or cautious is bad. But true
*  capabilities come from actually moving the whole curve up and then you are on a very different
*  plane of those trade-offs. And that's what we're trying to do here is to move the whole curve up.
*  Before I forget, let's talk about trucks a little bit. So I also got a chance to check out some of
*  the Waymo trucks. I'm not sure if we want to go too much into that space, but it's a fascinating
*  one. So maybe we can mention at least briefly, Waymo is also now doing autonomous trucking
*  and how different philosophically and technically is that whole space of problems?
*  It's one of our two big products and commercial applications of our driver, right? Right-hailing
*  and deliveries. We have Waymo One and Waymo Via, moving people and moving goods. Trucking is an
*  example of moving goods. We've been working on trucking since 2017. It is a very interesting
*  space. And your question of how different is it? It has this really nice property that the first
*  order challenges, like the science, the hard engineering, whether it's hardware or onboard
*  software or off-board software, all of the systems that you build for training your ML models, for
*  evaluating your entire system. Those fundamentals carry over. The true challenges of driving,
*  perception, semantic understanding, prediction, decision-making, planning, evaluation,
*  the simulator, ML infrastructure, those carry over. The data and the application and the domains
*  might be different, but the most difficult problems, all of that carries over between the
*  domains. That's very nice. That's how we approach it. We're kind of building, investing in the core,
*  the technical core. And then there's specialization of that core technology to different product lines,
*  to different commercial applications. Just to tease it apart a little bit, on trucks,
*  starting with the hardware, the configuration of the sensors is different. They're different
*  physically, geometrically, different vehicles. For example, we have two of our main laser on the
*  trucks on both sides so that we don't have the blind spots. Whereas on the JLR I-PACE, we have
*  one of it sitting at the very top, but the actual sensors are almost the same or largely the same.
*  All of the investment that over the years we've put into building our custom lighters, custom radars,
*  pulling the whole system together, that carries over very nicely. Then on the perception side,
*  the fundamental challenges of seeing, understanding the world, whether it's object
*  detection, classification, tracking, semantic understanding, all that carries over. Yes,
*  there's some specialization when you're driving on freeways, range becomes more important,
*  the domain is a little bit different, but again, the fundamentals carry over very, very nicely.
*  Same, I guess you get into prediction or decision making. The fundamentals of what it takes to
*  predict what other people are going to do, to find the long tail, to improve your system in
*  that long tail of behavior prediction and response, that carries over, and so on and so on.
*  That's pretty exciting. By the way, does Waymovie include using the smaller vehicles for
*  transportation of goods? That's an interesting distinction. I would say there's three interesting
*  modes of operation. One is moving humans, one is moving goods, and one is moving nothing,
*  zero occupancy, meaning you're going to the destination, you're an empty vehicle.
*  The third is the less way, that's the entirety of it, it's the less exciting from the commercial
*  perspective. Well, in terms of if you think about what's inside a vehicle as it's moving, because
*  it does, some significant fraction of the vehicle's movement has to be empty.
*  It's fascinating, maybe just on that small point, is there different
*  control and policies that are applied for a zero occupancy vehicle, so a vehicle with nothing in it,
*  or is it just move as if there is a person inside, with some subtle differences?
*  As a first order approximation, there are no differences. If you think about safety and
*  comfort and quality of driving, only part of it has to do with the people or the goods inside of
*  the vehicle. You want to drive smoothly, as we discussed, not purely for the benefit of
*  whatever you have inside the car, it's also for the benefit of the people outside,
*  fitting naturally and predictably into that whole environment. Yes, there are some second order
*  things you can do, you can change your route and optimize maybe your fleet, things at the fleet
*  scale, and you would take into account whether some of your cars are actually serving a useful
*  trip, whether with people or with goods, whereas other cars are driving completely empty to that
*  next valuable trip that they're going to provide, but those are mostly second order effects.
*  Okay, cool. Phoenix is an incredible place and what you've announced in Phoenix is amazing,
*  but that's just one city. How do you take over the world?
*  I mean, I'm asking for a friend, one step at a time.
*  Cartoon Pinky in the Brain. Yeah. Okay. But gradually is a true answer. So I think
*  the heart of your question is... Can you ask a better question than I asked?
*  You're asking a great question. Answer that one. I'm just going to
*  phrase it in the terms that I want to answer. That's very perfect. This is exactly right.
*  Brilliant. Please. Where are we today and what happens next and what does it take to go beyond
*  Phoenix and what does it take to get this technology to more places and more people
*  around the world? So our next big area of focus is exactly that, larger scale commercialization
*  and scaling up. If I think about the main... Phoenix gives us that platform and gives us that
*  foundation upon which we can build. There are few really challenging aspects of this whole problem
*  that you have to pull together in order to build the technology, in order to deploy it into the
*  field, to go from a driverless car to a fleet of cars that are providing a service and then all
*  the way to commercialization. This is what we have in Phoenix. We've taken the technology from
*  a proof point to an actual deployment and have taken our driver from one car to a fleet that
*  can provide a service. Beyond that, if I think about what it will take to scale up and deploy
*  in more places with more customers, I tend to think about three main dimensions, three main axes
*  of scale. One is the core technology, the hardware and software, core capabilities of our driver.
*  The second dimension is evaluation and deployment. The third one is the product, commercial,
*  and operational excellence. So you can talk a bit about where we are along each one of those three
*  dimensions, about where we are today and what will happen next. On the core technology,
*  the hardware and software together comprise of driver. We obviously have that foundation
*  that is providing fully driverless trips to our customers as we speak, in fact.
*  We've learned a tremendous amount from that. Now what we're doing is we are incorporating all those
*  lessons into some pretty fundamental improvements in our core technology, both on the hardware side
*  and on the software side, to build a more general, more robust solution that then will enable us to
*  massively scale beyond Phoenix. On the hardware side, all of those lessons are now incorporated
*  into this fifth generation hardware platform that is being deployed right now.
*  That's the platform. The fourth generation, the thing that we have right now driving in Phoenix,
*  is good enough to operate fully driverless, night and day, at various speeds and various conditions.
*  But the fifth generation is the platform upon which we want to go to massive scale.
*  We've really made qualitative improvements in terms of the capability of the system,
*  the simplicity of the architecture, the reliability of the redundancy.
*  It is designed to be manufacturable at very large scale and provides the right unit economics.
*  That's the next big step for us on the hardware side.
*  That's already there for scale, the version five.
*  That's right.
*  Is that coincidence or should we look into a conspiracy theory that's the same version
*  as the Pixel phone? Is that what the hardware is?
*  I can neither confirm nor deny.
*  It looks. All right, cool. Sorry. That's that axis. What else?
*  Similarly, hardware is a very discreet jump, but similar to how we're making that change from the
*  fourth generation hardware to the fifth, we're making similar improvements on the software side
*  to make it more robust and more general and allow us to quickly scale beyond Phoenix.
*  That's the first dimension of core technology. The second dimension is evaluation and deployment.
*  How do you measure your system? How do you evaluate it? How do you build a release and
*  deployment process where with confidence, you can regularly release new versions of your driver
*  into a fleet? How do you get good at it so that it is not a huge tax on your researchers and
*  engineers? How do you build all these processes, the frameworks, the simulation, the evaluation,
*  the data science, the validation so that people can focus on improving the system and the releases
*  just go out the door and get deployed across the fleet? We've gotten really good at that in Phoenix.
*  That's been a tremendously difficult problem, but that's what we have in Phoenix right now that
*  gives us that foundation. Now we're working on incorporating all the lessons that we've learned
*  to make it more efficient to go to new places and scale up and just stamp things out.
*  That's that second dimension of evaluation and deployment. The third dimension is product,
*  commercial, and operational excellence. Again, Phoenix there is providing an incredibly valuable
*  platform. That's why we're doing things end-to-end in Phoenix. We're learning, as we discussed a
*  little earlier today, a tremendous amount of really valuable lessons from our users getting
*  really incredible feedback. We'll continue to iterate on that and incorporate all those
*  lessons into making our product even better and more convenient for our users.
*  So you're converting this whole process in Phoenix into something that could be copied
*  and pasted elsewhere. Perhaps you didn't think of it that way when you were doing the experimentation
*  in Phoenix. So how long did... Basically, you can correct me, but it's still early days,
*  but you've taken the full journey in Phoenix, as you were saying, of what it takes to automate.
*  It's not the entirety of Phoenix, but I imagine it can encompass the entirety of Phoenix. That's some
*  some near-term date, but that's not even perhaps important, as long as it's a large enough geographic
*  area. So how copy-pastable is that process currently? And how do... When you copy and paste
*  in Google Docs, I think, or in Word, you can apply source formatting or apply destination formatting.
*  So when you copy and paste the Phoenix into, say, Boston, how do you apply the destination
*  formatting? How much of the core of the entire process of bringing an actual public
*  transportation, autonomous transportation service to a city is there in Phoenix that you understand
*  enough to copy and paste into Boston or wherever? So we're not quite there yet. We're not at a point
*  where we're kind of massively copy and pasting all over the place. But Phoenix, what we did in Phoenix,
*  we very intentionally have chosen Phoenix as our first full deployment area, exactly for that reason,
*  to kind of tease the problem apart, look at each dimension, focus on the fundamentals of complexity
*  and de-risking those dimensions, and then bringing the entire thing together to get all the way,
*  force ourselves to learn all those hard lessons on this technology, hardware and software,
*  on the evaluation deployment, on operating a service, operating a business, using actually
*  serving our customers, all the way so that we're fully informed about the most difficult,
*  most important challenges to get us to that next step of massive copy and pasting, as you said.
*  That's what we're doing right now. We're incorporating all those things that we learned
*  into that next system that then will allow us to kind of copy and paste all over the place and to
*  massively scale to more users and more locations. I mean, we just talked a little bit about what
*  does that mean along those different dimensions. So on the hardware side, for example, again,
*  it's that switch from the fourth to the fifth generation. And the fifth generation is designed
*  to kind of have that property. Can you say what other cities you're thinking about? Like I'm
*  thinking about, sorry, we're in San Francisco now. I thought I want to move to San Francisco,
*  but I'm thinking about moving to Austin. I don't know why people are not being very nice about
*  San Francisco currently. Maybe it's a small, maybe it's in vogue right now, but Austin seems,
*  I visited there and it was, I was in a Walmart. It's funny, these moments like turn your life.
*  There's this very nice woman with kind eyes just like stopped and said,
*  he looks so handsome in that tie honey to me. This has never happened to me in my life,
*  but just the sweetness of this woman is something I've never experienced, certainly in the streets
*  of Boston, but even in San Francisco where people wouldn't, that's just not how they speak or think.
*  I don't know. There's a warmth to, to Austin that love. And since Waymo does have a little bit of a
*  history there, is that a possibility? Is this your version of asking the question of like,
*  you know, Demetri, I know you can't share your commercial and deployment roadmap,
*  but I'm thinking about moving to San Francisco of Austin, like, you know, blink twice if you think
*  I should move to. That's true. That's true. You got me. We've been testing in all over the place.
*  I think we've been testing in more than 25 cities. We drive in San Francisco, we drive in,
*  you know, Michigan for snow. We are doing significant amount of testing in the Bay Area,
*  including San Francisco. But just not like, because we're talking about the very different
*  thing, which is like a full on large geographic area, public service. You can't share. Okay.
*  What about Moscow? Is that, when is that happening? Take on Yandex. I'm not paying
*  attention to those folks. They're doing, you know, there's a lot of fun. I mean, maybe as a way of a
*  question, you didn't speak to sort of like policy or like, is there tricky things with government
*  and so on? Like, is there other friction that you've encountered except sort of technological
*  friction of solving this very difficult problem? Is there other stuff that you have to overcome
*  when deploying a public service in a city? That's interesting. It's very important.
*  So we put significant effort in creating those partnerships and, you know, those relationships
*  with governments at all levels, you know, local governments, municipalities, you know, state level,
*  federal level. We've been engaged in very deep conversations from the earliest days of our
*  projects. Whenever, at all of these levels, you know, whenever we go to test or, you know, operate
*  in a new area, you know, we always lead with a conversation with the local officials. And,
*  but the result of that, that investment is that, no, it's not challenges we have to overcome,
*  but it is a very important that we continue to have this conversation.
*  Oh, yeah. I love politicians too. Okay. So Mr. Elon Musk said that
*  LIDAR is a crutch. What are your thoughts?
*  I wouldn't characterize it exactly that way. I know, I think LIDAR is very important. It is
*  a key sensor that, you know, we use just like other modalities, right? As we discussed,
*  our cars use cameras, LIDARs and radars. They are all very important. They are
*  at the kind of the physical level. They are very different. They have very different,
*  you know, physical characteristics. Cameras are passive, LIDARs and radars are active,
*  use different wavelengths. So that means they complement each other very nicely. And they
*  together combined, they can be used to build a much safer and much more capable system. So,
*  to me, it's more of a question, you know, why the heck would you handicap yourself and not use one
*  or more of those sensing modalities when they undoubtedly just make your system more capable
*  and safer? Now, what might make sense for one product or one business might not make sense for
*  another one. So if you're talking about driver assist technologies, you make certain design
*  decisions and you make certain trade-offs and make different ones if you are building a driver
*  deploy and fully driverless vehicles. And, you know, and lighter specifically, when this question
*  comes up, I typically the criticisms that I hear or, you know, the counterpoints that cost
*  and aesthetics. And I don't find either of those honestly very compelling. So on the cost side,
*  there's nothing fundamentally prohibitive about the cost of LIDARs. You know, radars used to be
*  very expensive before people started, you know, before people made certain advances in technology
*  and started to manufacture them at massive scale and deploy them in vehicles, right?
*  Similar with LIDARs. And this is where the LIDARs that we have on our cars, especially the fifth
*  generation, you know, we've been able to make some pretty qualitative discontinuous jumps in terms of
*  the fundamental technology that allow us to manufacture those things at very significant
*  scale and at a fraction of the cost of both our previous generation as well as a fraction of the
*  cost of what might be available on the market, you know, off the shelf right now. And, you know,
*  that improvement will continue. So I think, you know, cost is not a real issue. Second one is,
*  you know, aesthetics. You know, I don't think that's, you know, a real issue either.
*  UDES and I, the beholder. You can make LIDAR sexy again.
*  I think you're exactly right. I think it is sexy. Like honestly, I think form,
*  all of function. Well, okay. You know, I was actually, somebody brought this up to me.
*  I mean, all forms of LIDAR, even like the ones that are like big, you can make look, I mean,
*  you can make look beautiful. There's no sense in which you can't integrate it into design.
*  Like there's all kinds of awesome designs. I don't think small and humble is beautiful. It could be
*  like, you know, brutalism or like it could be like harsh corners. I mean, like I said,
*  like hot rods. Like I don't like, I don't necessarily like, like, oh man, I'm going
*  to start so much controversy with this. I don't like Porsches. Okay. The Porsche 911, like everyone
*  says, oh, it's the most beautiful. No, it's like a baby car. It doesn't make any sense,
*  but everyone, it's UDES and I, the beholder. You're already looking at me like, what's this
*  kid talking about? You're talking about your digging your own hole, the form and function
*  and my take on the beauty of the hardware that we put on our vehicles. You know, I will not comment
*  on the Porsche, you know, Porsche monologue. Okay. All right. So, but aesthetics, fine. But there's
*  an underlying like philosophical question behind the kind of LIDAR question is like, how much of
*  the problem can be solved with computer vision, with machine learning? So I think without sort of
*  disagreements and so on, it's nice to put it on the spectrum because Waymo is doing a lot of machine
*  learning as well. It's interesting to think how much of driving, if we look at five years, 10 years,
*  50 years down the road, what can be learned in almost more and more and more end to end way.
*  If we look at what Tesla is doing with as a machine learning problem, they're doing a multitask
*  learning thing where it's just, they break up driving into a bunch of learning tasks and they
*  have one single neural network and they're just collecting huge amounts of data that's training
*  that I've recently hung out with George Hots. I don't know if you know George.
*  I love him so much. He's just an entertaining human being. We were off mic talking about Hunter S.
*  Thompson. He's the Hunter S. Thompson of autonomous driving. Okay. So he, I didn't realize this with
*  Comma AI, but they're like really trying to do end to end. They're the machine, like looking at
*  the machine learning problem, they're really not doing multitask learning, but it's computing the
*  drivable area as a machine learning task and hoping that like down the line, this level two
*  system, this driver assistance will eventually lead to allowing you to have a fully autonomous
*  vehicle. Okay. There's an underlying deep philosophical question there, technical question
*  of how much of driving can be learned. So LiDAR is an effective tool today for actually deploying a
*  successful service in Phoenix, right? That's safe, that's reliable, et cetera, et cetera.
*  But the question, and I'm not saying you can't do machine learning on LiDAR, but the question is that
*  like how much of driving can be learned eventually? Can we do fully autonomous that's learned?
*  Yeah. Learning is all over the place and plays a key role in every part of our system.
*  As you said, I would decouple the sensing modalities from the ML and the software parts of it.
*  LiDAR, radar, cameras, it's all machine learning, all of the object detection classification,
*  of course, that's what these modern deep nets and countenance are very good at. You feed them raw
*  data, massive amounts of raw data, and that's actually what our custom built LiDARs and radars
*  are really good at. And radars, they don't just give you point estimates of objects in space,
*  they give you raw, like physical observations. And then you take all of that raw information,
*  whether it's colors of the pixels, whether it's LiDARs returns and some auxiliary information,
*  it's not just distance, right? And angle and distance, it's much richer information that you
*  get from those returns plus really rich information from the radars. You fuse it all together and you
*  feed it into those massive ML models that then lead to the best results in terms of object
*  deduction classification, state estimation. So there's a side to interrupt, but there is a
*  fusion. I mean, that's something that people didn't do for a very long time, which is like at the
*  sensor fusion level, I guess, like early on fusing the information together, whether so that the
*  sensory information that the vehicle receives from the different modalities or even from different
*  cameras is combined before it is fed into the machine learning models.
*  Yeah. So I think this is one of the trends. You're seeing more of that. You mentioned end-to-end.
*  There's different interpretations of end-to-end. There is kind of the purest interpretation. I'm
*  going to have one model that goes from raw sensor data to steering torque and gas breaks. That's
*  too much. I don't think that's the right way to do it. There's more smaller versions of end-to-end
*  where you're kind of doing more end-to-end learning or core training or depropagation of
*  signals back and forth across the different stages of your system. There's really good ways.
*  It gets into some fairly complex design choices where on one hand you want modularity and
*  decomposability of your system, but on the other hand, you don't want to create interfaces that
*  are too narrow or too brittle, too engineered where you're giving up on the generality of the
*  solution or you're unable to properly propagate signal, reach signal forward and losses and
*  back so you can optimize the whole system jointly. I would decouple and I guess what you're seeing
*  in terms of the fusion of the sensing data from different modalities as well as fusion
*  in the temporal level going more from frame by frame where you would have one net that would
*  do frame by frame detection in camera and then something that does frame by frame in
*  lighter and then radar and then you fuse it in a weaker engineered way later. The field over the
*  last decade has been evolving in more kind of joint fusion, more end-to-end models that are
*  solving some of these tasks jointly and there's tremendous power in that and that's the
*  progression that our stack has been on as well. Now, I would decouple the sensing and how that
*  information is fused from the role of ML and the entire stack. There's trade-offs in modularity and
*  how do you inject inductive bias into your system? There's tremendous power in being able to do that.
*  There's no part of our system that does not heavily leverage data-driven development or
*  state-of-the-art ML but there's mapping, there's a simulator, there's perception,
*  object level, perception, whether it's semantic understanding, prediction, decision making, so on.
*  Of course, object detection and classification like finding pedestrians and cars and cyclists
*  and cones and signs and vegetation and being very good at estimating detection, classification,
*  and state estimation, there's just stable stakes. That's step zero of this whole stack. You can be
*  incredibly good at that whether you use cameras or light as a radar but that's just stable stakes.
*  Beyond that, you get into the really interesting challenges of semantic understanding,
*  the perception level, you get into scene level reasoning, you get into very deep problems that
*  have to do with prediction and joint prediction and interaction, so-called interaction between
*  all of the actors in the environment, pedestrians, cyclists, other cars, and you get into decision
*  making. How do you build a lot of systems? We leverage ML very heavily in all of these components.
*  I do believe that the best results you achieve by using a hybrid approach and having different
*  types of ML, having different models with different degrees of inductive bias that you can have,
*  and combining model-free approaches with some model-based approaches and some
*  rule-based, physics-based systems. One example I can give you is traffic lights.
*  There's a problem of the detection of traffic light state and obviously that's a great problem
*  for computer vision. Confidants, that's their bread and butter. That's how you build that.
*  But then the interpretation of a traffic light, you're going to need to learn that.
*  You don't need to build some complex ML model that infers with some precision and recall
*  that red means stop. It's a very clear engineered signal with very clear semantics.
*  You want to induce that bias, like how you induce that bias and whether it's a constraint or a cost
*  function in your stack, but it is important to be able to inject that clear semantic signal
*  into your stack. That's what we do. That's when you apply it to yourself,
*  when you are making decisions whether you want to stop for a red light or not.
*  But if you think about how other people treat traffic lights, we're back to the ML version of
*  that. You know they're supposed to stop for a red light, but that doesn't mean they will.
*  Then you're back in the very heavy ML domain where you're picking up on very subtle keys
*  about what they have to do with the behavior of objects, pedestrians, cyclists, cars, and the
*  whole entire configuration of the scene that allow you to make accurate predictions on whether
*  they will in fact stop or run a red light. So it sounds like already for Waymo, machine learning
*  is a huge part of the stack. So it's a huge part of like, not just, so obviously the first level
*  zero or whatever you said, which is like just object detection and things that you know,
*  know that machine learning can do, but also starting to do prediction behavior and so on
*  to model the what other or the other parties in the scene entities in the scene are going to do.
*  So machine learning is more and more playing a role in that as well.
*  Of course. Absolutely. I mean I think we've been going back to the earliest days like DARPA,
*  even the DARPA Grand Challenge. Our team was leveraging machine learning. I was like pre-Imagenet
*  and it was a very different type of ML. But and I think actually it was before my time, but the
*  Stanford team on during the Grand Challenge had a very interesting machine learned system that would
*  use LiDAR and camera when driving in the desert. And we had built the model where it would kind
*  of extend the range of free space reasoning. We'd get a clear signal from LiDAR and then it had a
*  model that said, hey, like this stuff on camera kind of sort of looks like this stuff in LiDAR.
*  And I know this stuff that I've seen in LiDAR, I'm very confident it's free space. So let me extend
*  that free space zone into the camera range that would allow the vehicle to drive faster.
*  And then we've been building on top of that and kind of staying and pushing the state of the art
*  in ML in all kinds of different ML over the years. And in fact, from the earliest days, I think 2010
*  is probably the year where Google, maybe 2011 probably, got pretty heavily involved in machine
*  learning, kind of deep nuts. And at that time it was probably the only company that was very heavily
*  investing in kind of state of the art ML and self-driving cars. And they go hand in hand.
*  And we've been on that journey ever since. We're doing pushing a lot of these areas in terms of
*  research at Waymo and we collaborate very heavily with the researchers in alphabet. And like all
*  kinds of ML, supervised ML, unsupervised ML. We've published some interesting research papers in the
*  space, especially recently. It's just super active learning as well. Yeah, super, super active.
*  Of course, there is kind of the more mature stuff like, you know, convnets for object detection.
*  But there's some really interesting, really active work that's happening in kind of more,
*  in bigger models and models that have more structure to them, not just large
*  bitmaps and reasonable temporal sequences. And some of the interesting breakthroughs that you've
*  seen in language models, right? Transformers, GPT-3 inference. There's some really interesting
*  applications of some of the core breakthroughs to those problems of behavior prediction as well as
*  decision making and planning. You can think about it, kind of the behavior, how, you know,
*  the path, the trajectories, how people drive. They share a lot of the fundamental structure
*  of this problem. There's sequential nature. There's a lot of structure in this representation. There
*  is a strong locality, kind of like in sentences, words that follow each other. They're strongly
*  connected, but there are also kind of larger contexts that doesn't have that locality. And
*  you also see that in driving, right? What's happening in the scene as a whole has very strong
*  implications on the next step in that sequence where whether you're predicting what other people
*  are going to do, whether you're making your own decisions, or whether in the simulator,
*  you're building generative models of humans walking, cyclists riding, and other cars driving.
*  Yeah, that's all really fascinating. It's fascinating to think that
*  transformer models and all the breakthroughs in language and NLP that might be applicable to
*  driving at the higher level, at the behavior level. That's kind of fascinating.
*  Let me ask about pesky little creatures called pedestrians and cyclists.
*  Humans are a problem. If we can get rid of them, I would. But unfortunately, they're also a source
*  of joy and love and beauty, so let's keep them around. They're also our customers.
*  From your perspective, yes, yes, for sure. They're a source of money. Very good.
*  I don't even know where I was going. Oh, yes, pedestrians and cyclists.
*  They're a fascinating injection into the system of uncertainty,
*  of a game theoretic dance of what to do. Also, they have perceptions of their own,
*  and they can tweet about your product, so you don't want to run them over
*  from that perspective. I'm joking a lot, but I think in seriousness, pedestrians are a complicated
*  computer vision problem, a complicated behavioral problem. Is there something interesting you could
*  say about what you've learned from a machine learning perspective, from also an autonomous
*  vehicle and a product perspective about just interacting with the humans in this world?
*  Yeah. Just to state on record, we care deeply about the safety of pedestrians,
*  even the ones that don't have Twitter accounts. Thank you. All right, cool. Not me. But yes,
*  I'm glad somebody does. But in all seriousness, safety of vulnerable road users, pedestrians or
*  cyclists is one of our highest priorities. We do a tremendous amount of testing and validation
*  and put a very significant emphasis on the capabilities of our systems that have to do
*  with safety around those unprotected, vulnerable road users. Cars, as we discussed earlier in
*  Phoenix, we have completely empty cars, completely driverless cars driving in this very large area,
*  and some people use them to go to school, so they'll drive through school zones.
*  Kids are the very special class of those vulnerable road users. You want to be super,
*  super safe and super, super cautious around those. We take it very, very, very seriously.
*  What does it take to be good at it? An incredible amount of performance across your whole stack.
*  Starts with hardware. Again, you want to use all sun signal modalities available to you. Imagine
*  driving on a residential road at night and making a turn and you don't have headlights covering some
*  part of the space and a kid might run out. Lighters are amazing at that. They see just as well in
*  complete darkness as they do during the day. Again, it gives you that extra margin in terms
*  of capability and performance and safety and quality. In fact, we oftentimes, in these kinds
*  of situations, we have our system detect something, in some cases even earlier than our trade operators
*  in the car might do, especially in conditions like very dark nights. Starts with sensing. Then
*  perception has to be incredibly good. You have to be very, very good at detecting pedestrians
*  in all kinds of situations, in all kinds of environments, including people in weird poses,
*  people running around and being partially occluded. That's step number one. Then you have to have
*  in very high accuracy and very low latency in terms of your reactions to what these actors might
*  do. We've put a tremendous amount of engineering and tremendous amount of validation in to make
*  sure our system performs properly. Oftentimes, it does require a very strong reaction to do the
*  safe thing. We actually see a lot of cases like that. That's the long tail of really rare,
*  really crazy events that contribute to the safety around pedestrians. One example that comes to mind
*  that actually happened in Phoenix where we were driving along and I think it was a 45-mile-per-hour
*  road, so pretty high-speed traffic. There was a sidewalk next to it and there was a cyclist
*  on the sidewalk. We were in the right lane, right next to the side. It was a multi-lane road.
*  As we got close to the cyclist on the sidewalk, it was a woman. She tripped and fell. She fell
*  right into the path of our vehicle. This was actually with a test driver. Our test drivers
*  did exactly the right thing. They reacted and came to stop. It requires both very strong steering and
*  strong application of the brake. Then we simulated what our system would have done in that situation
*  and it did exactly the same thing. That speaks to all of those components of really good
*  state estimation and tracking. Imagine a person on a bike and they're falling over and they're
*  doing that right in front of you. Things are changing. The appearance of that whole thing
*  is changing. A person goes one way, they're falling on the road. They're being flat on the
*  ground in front of you. The bike goes flying the other direction. The two objects that used to be
*  one are splitting apart and the car has to detect all of that. Milliseconds matter. It's not good
*  enough to just brake. You have to steer and brake and there's traffic around you. It all has to
*  come together. It was really great to see in this case and other cases like that that we're actually
*  seeing in the wild that our system is performing exactly the way that we would have liked and is
*  able to avoid collisions like this. It's such an exciting space for robotics. In that split second
*  to make decisions of life and death, I don't know. The stakes are high in a sense, but it's also
*  beautiful that for somebody who loves artificial intelligence, the possibility that an AI system
*  might be able to save a human life, that's kind of exciting as a problem to wake up. It's terrifying
*  probably for an engineer to wake up and to think about, but it's also exciting because it's in your
*  hands. Let me try to ask a question that's often brought up about autonomous vehicles.
*  And it might be fun to see if you have anything interesting to say, which is about the trolley
*  problem. The trolley problem is an interesting philosophical construct that highlights,
*  and there's many others like it, of the difficult ethical decisions that we humans
*  have before us in this complicated world. Specifically, it's the choice between
*  if you were forced to choose to kill a group X of people versus a group Y of people, like
*  one person, if you did nothing, you would kill one person, but if you would kill five people,
*  and if you decide to swerve out of the way, you would only kill one person.
*  Do you do nothing or you choose to do something? You can construct all kinds of sort of
*  ethical experiments of this kind that I think at least on a positive note, inspire you to think
*  about like introspect what are the physics of our morality. And there's usually not good
*  answers there. I think people love it because it's just an exciting thing to think about.
*  I think people who build autonomous vehicles usually roll their eyes because this is not,
*  this one as constructed, this like literally never comes up in reality. You never have to
*  choose between killing one or like one of two groups of people. But I wonder if you can speak
*  to is there something interesting to you as an engineer of autonomous vehicles that's within the
*  trolley problem or maybe more generally, are there difficult ethical decisions that you find
*  that an algorithm must make? On the specific version of the trolley problem, which one would
*  you do if you're driving? The question itself is a profound question because we humans ourselves
*  cannot answer and that's the very point. I will kill both.
*  I think you're exactly right in that humans are not particularly good. I think the kind of phrase
*  is like what would a computer do? But humans are not very good. And I actually oftentimes think that
*  freezing and kind of not doing anything because like you've taken a few extra milliseconds to
*  just process and then you end up like doing the worst of the possible outcomes. So I do think that
*  as you've pointed out, it can be a bit of a distraction and it can be a bit of a kind of
*  red herring. I think it's an interesting discussion in the realm of philosophy,
*  but in terms of how that affects the actual engineering and deployment of self-driving
*  vehicles, it's not how you go about building a system. We've talked about how you engineer a
*  system, how you go about evaluating the different components and the safety of the entire thing,
*  how do you kind of inject the various model-based safety-based arguments. And yes,
*  you reason at parts of the system, you reason about the probability of a collision, the severity
*  of that collision, and that is incorporated and you have to properly reason about the uncertainty
*  that flows through the system. So those factors definitely play a role in how the cars then behave,
*  but they tend to be more of the emergent behavior. And what you see, you're absolutely right,
*  that these clear theoretical problems that they, you don't occur that in the system. And really,
*  kind of being back to our previous discussion, which one do you choose? Well, oftentimes,
*  you made a mistake earlier. You shouldn't be in that situation in the first place. And in reality,
*  the system comes up. If you build a very good, safe and capable driver, you have enough clues
*  in the environment that you drive defensively so you don't put yourself in that situation.
*  Right? And again, if you go back to that analogy of precision and recall, like, okay, you can make a
*  very hard trade-off, but neither answer is really good. But what instead you focus on is kind of
*  moving the whole curve up and then you focus on building the right capability and the right
*  defensive driving so that you don't put yourself in a situation like this.
*  I don't know if you have a good answer for this, but people love it when I ask this question
*  about books. Are there books in your life that you've enjoyed? Philosophical, fiction, technical,
*  that had a big impact on you as an engineer or as a human being? Everything from science fiction to
*  a favorite textbook. Is there three books that stand out that you can think of?
*  Oh, three books. So, I would, you know, that impacted me, I would say,
*  and this one is, you probably know it well, but not generally well known. I think in the US,
*  or kind of internationally, The Master and Margarita. It's one of actually my favorite books.
*  It's a novel by Russian author Mikhail Bulgakov, and it's a great book. It's one of those books
*  that you can reread your entire life and it's very accessible. You can read it as a kid.
*  The plot is interesting. It's the devil visiting the Soviet Union. But you read it, reread it
*  at different stages of your life and you enjoy it for very different reasons. It's a great book.
*  Very different reasons. And you keep finding deeper and deeper meaning. It definitely had an
*  imprint on me, mostly from the cultural stylistic aspect. It makes you think one of those books
*  is good and makes you think, but also has this really silly, quirky, dark sense of humor.
*  It captures the Russian soul more than perhaps many other books. On that slight note,
*  just out of curiosity, one of the saddest things is I've read that book in English.
*  Did you by chance read it in English or in Russian?
*  In Russian, only in Russian. Actually, that is a question I had
*  posed to myself every once in a while. I wonder how well it translates, if it translates at all.
*  There's the language aspect of it and then there's the cultural aspect.
*  Actually, I'm not sure if either of those would work well in English.
*  Now, I forget their names, but when the COVID lifts a little bit, I'm traveling to Paris
*  for several reasons. One is just I've never been to Paris, I want to go to Paris. But there's the
*  most famous translators of Dostoevsky, Tolstoy, of most of Russian literature live there. There's
*  a couple. They're famous, a man and a woman. I'm going to have a series of conversations with them.
*  In preparation for that, I'm starting to read Dostoevsky in Russian. I'm really embarrassed
*  to say that everything I've read in Russian literature of serious depth has been in English,
*  even though I can also read, obviously, in Russian. But for some reason, it seemed
*  in the optimization of life, it seemed the improper decision to read in Russian.
*  I don't need to opt, I need to think in English, not in Russian. But now I'm changing my mind on
*  that. And so the question of how well I translate is a really fundamental one, even with Dostoevsky.
*  So from what I understand, Dostoevsky translates easier. Others don't as much. Obviously,
*  the poetry doesn't translate as well. I'm also the music big fan of Vladimir Vysotsky. He doesn't
*  obviously translate well. People have tried. But Mastermind, I don't know. I don't know about that
*  one. I just know it in English. It's fun as hell in English. But it's a curious question,
*  and I want to study it rigorously from both the machine learning aspect and also because I want
*  to do a couple of interviews in Russia that I'm still unsure of how to properly conduct an interview
*  across a language barrier. It's a fascinating question that ultimately communicates to an
*  American audience. There's a few Russian people that I think are truly special human beings.
*  I sometimes encounter this with some incredible scientists, and maybe you encounter this
*  as well at some point in your life, that it feels like because of the language barrier,
*  their ideas are lost to history. It's a sad thing. I think about Chinese scientists or even authors
*  like that we don't in English speaking world don't get to appreciate some like the depth of
*  the culture because it's lost in translation. I feel like I would love to show that to the world.
*  I'm just some idiot, but because I have this like at least some semblance of skill in speaking
*  Russian, I feel like and I know how to record stuff on a video camera. I feel like I want to
*  catch like Grigori Perlman, who's a mathematician. I'm not sure if you're familiar with him.
*  I want to talk to him like he's a fascinating mind and to bring him to a wider audience
*  in English speaking will be fascinating, but that requires to be rigorous about this question
*  of how well Bogakov translates. I mean, I know it's a silly concept, but it's a fundamental one
*  because how do you translate? And that's the thing that Google Translate is also facing
*  as a more machine learning problem, but I wonder as a more bigger problem for AI,
*  how do we capture the magic that's there in the language?
*  I think that's a really interesting, really challenging problem. If you do read it,
*  Master and Margarita in Russian, I'd be curious to get your opinion. And I think part of it is
*  language, but part of it is just centuries of culture that the cultures are different. So it's
*  hard to connect that. Okay, so that was my first one. The second one, I would probably
*  pick the science fiction by the Strogowski Brothers. It's up there with Isaac Asimov and
*  Ray Bradbury and company. The Strogowski Brothers appealed more to me. I think it made more of an
*  impression on me growing up. I apologize if I'm showing my complete ignorance. I'm so weak on
*  sci-fi. What are they, right? Oh, Roadside Picnic, Hard to Be a God,
*  Beetle in an Ant Hill, Monday starts on Saturday. It's not just science fiction. It's also has very
*  interesting interpersonal and societal questions. And some of the language is just completely
*  hilarious. That's the one. Oh, interesting. Monday starts on Saturday. So I need to read. Okay. Oh,
*  boy. You put that in the category of science fiction? That one is, I mean, this was more of a
*  silly, you know, humorous work. I mean, there is kind of... But it's profound too, right? Science
*  fiction is about this research institute. It has deep parallels to serious research, but the setting,
*  of course, is that they're working on magic. And that's their style, right? And other books are
*  very different, right? Hard to Be a God is about this higher society being injected into this
*  primitive world and how they operate there. Some of the very deep ethical questions there.
*  Right? And they've got this full spectrum. Some are more about kind of more adventure style. But
*  I enjoy all of their books. There's probably a couple. Actually, one, I think that they consider
*  their most important work. I think it's The Snail on a Hill. I'm not exactly sure how it translates.
*  I tried reading a couple of times. I still don't get it. But everything else I fully enjoyed.
*  And for one of my birthdays as a kid, I got their entire collection occupied a giant shelf in my
*  room. And then over the holidays, my parents couldn't drag me out of the room. And I read
*  the whole thing cover to cover. And I really enjoyed it. And that's one more. For the third
*  one, maybe a little bit darker, but it comes to mind is Orwell's 1984. And I asked what made an
*  impression on me and the books that people should read. That one, I think, falls in the category of
*  both. Definitely, it's one of those books that you read and you just kind of put it down and
*  you stare in space for a while. That kind of work. I think there's lessons there. People
*  should not ignore. And nowadays, with everything that's happening in the world, I can't help it,
*  but I have my mind jump to some parallels with what Orwell described. And this whole
*  concept of double think and ignoring logic and holding completely contradictory opinions in your
*  mind and not have that not bother you and sticking to the party line at all costs. There's something
*  there. If anything, 2020 has taught me, and I'm a huge fan of Animal Farm, which is a kind of
*  friendly, as a friend of 1984 by Orwell. It's kind of another thought experiment of how our society
*  may go in directions that we wouldn't like it to go. But if anything, that's been
*  kind of heartbreaking to an optimist about 2020 is that society is kind of fragile.
*  This is a special little experiment we have going on. And it's not unbreakable. We should be
*  careful to preserve whatever special thing we have going on. I think 1984 and these books,
*  Brave New World, they're helpful in thinking stuff can go wrong in non-obvious ways. And it's up to
*  us to preserve it. It's a responsibility. It's been weighing heavy on me because for some reason
*  like more than my mom follows me on Twitter. And I feel like I have now somehow a responsibility
*  to this world. And it dawned on me that me and millions of others are like the little ants
*  that maintain this little colony. So we have a responsibility not to be, I don't know what
*  the right analogy is, but put a flame thrower to the place. We want to not do that. And there's
*  interesting complicated ways of doing that as 1984 shows. It could be through bureaucracy,
*  it could be through incompetence, it could be through misinformation, it could be through
*  division and toxicity. I'm a huge believer in that love will be somehow the solution. So
*  love and robots. Love and robots, yeah. I think you're exactly right. Unfortunately,
*  I think it's less of a flame thrower type of an answer. I think it's more of a, in many cases,
*  can be more of a slow boil. And that's the danger. Let me ask, it's a fun thing to make
*  a world-class roboticist, engineer and leader uncomfortable with a ridiculous question about
*  life. What is the meaning of life, Dimitri, from a robotics and a human perspective?
*  You only have a couple of minutes or one minute to answer. So
*  that makes it more difficult or easier. Actually, yeah. You know, they're very tempted to
*  quote one of the stories by Isaac Asimov actually, actually titled appropriately,
*  titled The Last Question, a short story where the plot is that humans build this supercomputer,
*  this AI intelligence, and once it gets powerful enough, they pose this question to it. How can
*  the entropy in the universe be reduced? So the computer replies, as of yet, insufficient
*  information to give a meaningful answer. And then thousands of years go by and they keep posing the
*  same question and the computer gets more and more powerful and keeps giving the same answer. As of
*  yet, insufficient information to give a meaningful answer or something along those lines. And then
*  happening and fast forward millions of years into the future and billions of years and at some point
*  it's just the only entity in the universe. It's like absorbed all humanity and all knowledge in
*  the universe and keeps posing the same question to itself. And finally, it gets to the point where
*  it is able to answer that question. But of course, at that point, the heat death of the universe has
*  occurred and that's the only entity and there's nobody else to provide that answer to. So the
*  only thing it can do is to answer it by demonstration. So it recreates the big bang and resets the clock.
*  I can try to give a different version of the answer. Maybe not on the behalf of all humanity.
*  I think that might be a little presumptuous for me to speak about the meaning of life on the behalf
*  of all humans, but at least personally. It changes. I think if you think about what gives you and
*  your life meaning and purpose and what drives you, it seems to change over time.
*  The lifespan of your existence. When you just enter this world, it's all about new experiences.
*  You get new smells, new sounds, new emotions. That's what's driving you. You're experiencing
*  new amazing things. That's magical. That's pretty awesome. That gives you meaning.
*  Then you get a little bit older, you start more intentionally learning about things.
*  I guess actually before you start intentionally learning, probably fun. Fun is a thing that gives
*  you meaning and purpose and the thing you optimize for. Fun is good. Then you start learning. I guess
*  this joy of comprehension and discovery is another thing that gives you meaning and purpose
*  and drives you. Then you learn enough stuff and you want to give some of it back. So impact and
*  contributions back to technology or society, people, local or more globally becomes a new thing that
*  drives a lot of your behavior and something that gives you purpose and that you derive
*  positive feedback from. Then you go and so on and so forth. You go through various stages of life.
*  If you have kids, that definitely changes your perspective on things. I have three
*  that definitely flips some bits in your head in terms of what you care about and what you
*  optimize for and what matters, what doesn't matter. It seems to me that it's all of those
*  things. As you go through life, you want these to be additive. New experiences, fun, learning,
*  impact. You want to be accumulating. I don't want to stop having fun or experiencing new things.
*  I think it's important that it becomes additive as opposed to a replacement or subtraction.
*  Those few are probably as far as I got, but ask me in a few years, I might have one or two more
*  to add to the list. Before you know it, time is up just like it is for this conversation,
*  but hopefully it was a fun ride. It was a huge honor to meet you. As you know, I've been a fan
*  of yours and a fan of Google self-driving car and Waymo for a long time. I can't wait. It's
*  one of the most exciting. If we look back in the 21st century, I truly believe it will be one of
*  the most exciting things we descendants of apes have created on this earth. I'm a huge fan and I
*  can't wait to see what you do next. Thanks so much for talking to me. Thanks for having me. It's
*  also a huge fan. It doesn't work, honestly, and I really enjoyed it. Thank you.
*  Thanks for listening to this conversation, Dmitry Dolgov. Thank you to our sponsors,
*  Trial Labs, a company that helps businesses apply machine learning to solve real world problems,
*  Blinkist, an app I use for reading through summaries of books, BetterHelp, online therapy
*  with a licensed professional, and Cash App. The app I use to send money to friends. Please check
*  out these sponsors in the description to get a discount and to support this podcast. If you
*  enjoy this thing, subscribe on YouTube, review it with Five Stars and Apple Podcasts, follow on
*  Spotify, support on Patreon, or connect with me on Twitter at Lex Friedman. And now let me leave
*  you with some words from Isaac Asimov. Science can amuse and fascinate us all, but it is engineering
*  that changes the world. Thank you for listening and hope to see you next time.

---
Date Generated: April 08, 2024
Transcription Model: whisper medium 20231117
Length: 6227s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'elon musk', 'joe rogan', 'lex ai', 'lex fridman', 'lex friedman', 'lex jre', 'lex mit', 'lex pod', 'lex podcast', 'marc raibert']
Video Views: 407452
Video Rating: None
---

# Marc Raibert: Boston Dynamics and the Future of Robotics | Lex Fridman Podcast #412
**Lex Fridman:** [February 16, 2024](https://www.youtube.com/watch?v=5VnbBCm_ZyQ)
*  So Big Dog became LS3, which is the big load carrying one.
*  Just a quick pause. It can carry 400 pounds.
*  It was designed to carry 400, but we had it carrying about a thousand pounds.
*  Of course you did. Just to make sure.
*  We had one carrying the other one. We had two of them. So we had one carrying the other one.
*  So one of the things that stands out about the robots
*  Boston Dynamics have created is how beautiful the movement is, how natural the walking is and
*  running is, even flipping is, throwing is. So maybe you can talk about what's involved in
*  making it look natural.
*  Well, I think having good hardware is part of the story and people who think you don't need
*  to innovate hardware anymore are wrong.
*  The following is a conversation with Mark Ryberg, a legendary roboticist, founder,
*  and long time CEO of Boston Dynamics and recently the executive director of the newly created
*  Boston Dynamics AI Institute that focuses on research and the cutting edge on creating
*  future generations of robots that are far better than anything that exists today.
*  He has been leading the creation of incredible legged robots for over 40 years at CMU, at MIT,
*  the legendary MIT leg lab, and then of course Boston Dynamics with amazing robots like Big Dog,
*  Atlas, Spot, and Handle. This was a big honor and pleasure for me.
*  This is the Lex Friedman podcast. To support it, please check out our sponsors in the description.
*  And now, dear friends, here's Mark Ryberg.
*  When did you first fall in love with robotics?
*  Well, I was always a builder from a young age. I was lucky. My father was a frustrated
*  engineer. And by that I mean he wanted to be an aerospace engineer, but his mom from the old
*  country thought that that would be like a grease monkey. And so she said no. So he became an
*  accountant. But the result of that was our basement was always full of tools and equipment and
*  electronics. And from a young age, I would watch him assembling an ICO kit or something like that.
*  I still have a couple of his old ICO kits. But it was really during graduate school when
*  I followed a professor back from class. It was Bertolt Horn at MIT. And I was taking
*  an interim class. It's IAP, independent activities period. And I followed him back to his lab.
*  And on the table was a VIKARM robot arm taken apart in probably a thousand pieces.
*  And when I saw that from that day on, I was a roboticist.
*  Do you remember the year?
*  1974.
*  1974. So there's just this arm and pieces. And you saw the pieces and you saw in your vision
*  the arm when it's put back together and the possibilities that holds.
*  Somehow it spurred my imagination. I was in the brain and cognitive sciences department
*  as a graduate student doing neurophysiology. I'd been an electrical engineer as an undergrad
*  at Northeastern. And the neurophysiology wasn't really working for me. It wasn't conceptual
*  enough. I couldn't see really how by looking at single neurons, you were going to get to a
*  place where you could understand control systems or thought or anything like that.
*  And the AI lab was always an appealing, this was before CSAIL, right? This was in the 70s. So
*  the AI lab was always an appealing idea. And so when I went back to the AI lab with following him
*  and I saw the arm, I just thought, this is it.
*  That's so interesting. The tension between the BCS, brain and cognitive science approach
*  to understanding intelligence and the robotics approach to understanding intelligence.
*  Well, BCS is now morphed a bit, right? They have the Center for Brains, Minds, and Machines, which
*  is trying to bridge that gap. And even when I was there, David Marr was in the AI lab. David Marr
*  had models of the brain that were appealing both to biologists, but also to computer people. So
*  he was a visitor in the AI lab at the time, and I guess he became full-time there. So that was the
*  first time a bridge was made between those two groups. Then the bridge kind of went away,
*  and then there was another time in the 80s. And then recently, the last five or so years,
*  there's been a stronger connection. You said you were always kind of a builder.
*  What stands out to you in memory of a thing you built? Maybe a trivial thing that just kind of
*  inspired you in the possibilities that this direction of work might hold.
*  I mean, we were just doing gadgets when we were kids. I had a friend, we were taking, you know,
*  I don't know if everybody remembers, but fluorescent lights had this little aluminum cylinder.
*  I can't even remember what it's called now, that you needed a starter, I think it was.
*  And we would take those apart, fill them with match heads, put a tail on it, and make it into
*  little rockets. So it wasn't always about function. It was... Well, rocket was pretty
*  much... I guess that is pretty functional. But yeah, I guess that is a question. How much was
*  it about function versus just creating something cool? I think it's still a balance between those
*  two. There was a time though when I was, I guess I was probably already a professor or maybe late
*  in graduate school, when I thought that function was everything and that mobility, dexterity,
*  perception, and intelligence, those are sort of the key functionalities for robotics.
*  That's what mattered and nothing else mattered. And I even had kind of this platonic ideal
*  that a robot, if you just looked at a robot and it wasn't doing anything, it would look like a pile
*  of junk, which a lot of my robots looked like in those days. But then when it started moving,
*  you'd get the idea that it had some kind of life or some kind of interest in its movement.
*  And I think we purposely even designed the machines, not worrying about the aesthetics
*  of the structure itself. But then it turns out that the aesthetics of the thing itself
*  add and combine with the lifelike things that the robots can do. But the heart of it is
*  making them do things that are interesting. One of the things that underlies a lot of your work is
*  that the robots you create, the systems you have created for over 40 years now,
*  they're not cautious. So a lot of robots that people know about move about this world very
*  cautiously, carefully, very afraid of the world. A lot of the robots you built, especially in the
*  early days, were very aggressive, under-extuated. They're hopping, they're wild, moving quickly.
*  Is there a philosophy underlying that? Well, let me tell you about how I got started on legs
*  at all. When I was still a graduate student, I went to a conference. It was a biological-legged
*  locomotion conference, and I think it was in Philadelphia. So it was all biomechanics people,
*  researchers who would look at muscle and maybe neurons and things like that. They weren't so much
*  computational people, but they were more biomechanics. And maybe there were a thousand
*  people there. And I went to a talk, one of the talks. All the talks were about
*  the body of either animals or people and respiration, things like that. But one talk
*  was by a robotics guy, and he showed a six-legged robot that walked very slowly. It always had at
*  least three feet on the ground, so it worked like a table or a chair with tripod stability,
*  and it moved really slowly. I just looked at that and said, wow, that's wrong. That's not anything
*  like how people and animals work. Because we bounce and fly, we have to predict what's going
*  to happen in order to keep our balance when we're taking a running step or something like that.
*  We use the springiness in our legs, our muscles and our tendons and things like that as part of
*  the story where the energy circulates. We don't just throw it away every time. I'm not sure I
*  understood all that when I first thought, but I definitely got inspired to say, let's try the
*  opposite. I didn't have a clue as to how to make a hopping robot work, not balance in 3D.
*  In fact, when I started, it was all just about the energy of bouncing. I was going to have a springy
*  thing in the leg and some actuator so that you could get an energy regime going of bouncing.
*  The idea that balance was an important part of it didn't come until a little later. Then I made the
*  one like the PogoStik robots. Now, I think that we need to do that in manipulation.
*  If you look at robot manipulation, we, a community, has been working on it for 50 years.
*  We're nowhere near human levels of manipulation. It's come along, but I think it's all too safe.
*  I think trying to break out of that safety thing of static grasping, if you look at a lot of work
*  that goes on, it's about the geometry of the part. Then you figure out how to move your hand so that
*  you can position it with respect to that. Then you grasp it carefully and then you move it.
*  Well, that's not anything like how people and animals work. We juggle in our hands.
*  We hold multiple objects and can sort them. To be fair, being more aggressive is going to mean
*  things aren't going to work very well for a while. It's a longer term approach to the problem.
*  That's just theory now. Maybe that won't pay off, but that's how I'm trying to think about it,
*  trying to encourage our group to go at it. Well, yeah. We'll talk about what it means to,
*  what is the actual thing we're trying to optimize for a robot. Sometimes, especially with human-robot
*  interaction, maybe flaws is a good thing. Perfection is not necessarily the right thing
*  to be chasing. Just like you said, maybe being good at fumbling an object, being good at fumbling
*  might be the right thing to optimize versus perfect modeling of the object and perfect
*  movement of the arm to grasp that object. Maybe perfection is not supposed to exist in the real
*  world. I don't know if you know my friend, Matt Mason, who is the director of the Robotics
*  Institute at Carnegie Mellon. We go back to graduate school together. He analyzed
*  a movie of Julia Childs doing a cooking thing. I think he said something like there were 40
*  different ways that she handled the thing, and none of them was grasping. She would nudge, roll,
*  flatten with her knife, things like that, and none of them was grasping.
*  Okay. Let's go back to the early days. First of all, you've created and led the Leg Lab,
*  the legendary Leg Lab at MIT. What was that first hopping robot?
*  First of all, the Leg Lab actually started at Carnegie Mellon. I was a professor there
*  starting in 1980 to about 1986. That's where the first hopping machines were built.
*  I guess we got the first one working in about 1982, something like that. That was a simplified
*  one. Then we got a three-dimensional one in 1983. The quadruped that we built at the Leg Lab,
*  the first version, was built in about 1984 or 1985 and really only got going about 86 or so.
*  Took years of development to get it to... Let's just pause here. For people who don't know,
*  I'm talking to Mark Graeber, founder of Boston Dynamics. Before that, you were a professor
*  developing some of the most incredible robots for 15 years. Before that, of course,
*  a grad student and all that. You've been doing this for a really long time. You skipped over this,
*  but go to the first hopping robot. There's videos of some of this. These are incredible robots.
*  You talked about the very first step was to get a thing hopping up and down. Then you realized,
*  well, balancing is a thing you should care about, and it's actually a solvable problem.
*  Can you just go through how to create that robot? What was involved in creating that robot?
*  Well, I'm going to start on the, not the technical side, but the, I guess we could call it the
*  motivational side or the funding side. Before Carnegie Mellon, I was actually at JPL,
*  at the Jet Propulsion Lab for three years. While I was there, I connected up with Ivan Sutherland,
*  who is sometimes regarded as the father of computer graphics because of work he did both at MIT
*  and then University of Utah and Evans and Sutherland. Anyway, I got to know him. At one
*  point, he said he encouraged me to do some kind of project at Caltech, even though I was at JPL.
*  Those are kind of related institutions. I thought about it, and I made up a list of three possible
*  projects. I purposely made the top one and the bottom one really boring sounding. In the middle,
*  I put PogoStik Robot. When he looked at it, Ivan is a brilliant guy, brilliant engineer,
*  and a real cultivator of people. He looked at it and knew right away what the thing that was
*  worth doing. He had an endowed chair, so he had about $3,000 that he gave me to build the first
*  model, which I went to the shop and with my own hands made a first model, which didn't work
*  and was just a beginning shot at it. Ivan and I took that to Washington. In those days,
*  you could just walk into DARPA and walk down the hallway and see who's there. Ivan, who had been
*  there in his previous life. We walked around and we looked in the offices. Of course, I didn't know
*  anything. I was basically a kid, but Ivan moved his way around. We found Craig Fields in his office.
*  Craig later became the director of DARPA, but in those days, he was a program manager.
*  We went in. I had a little Samsonite suitcase. We opened and it had just the skeleton of this
*  one-legged hopping robot. We showed it to him. You could almost see the drool going down his chin.
*  It was exciting.
*  It was of excitement. He sent me $250,000. He said, okay,
*  I want to fund this. I was between institutions. I was just about to leave JPL and I hadn't decided
*  yet where I was going next. Then when I landed at CMU, he sent $250,000, which in 1980 was a lot of
*  research money.
*  LWK Did you see the possibility of where this is going? Why this is an important problem?
*  Ivan No.
*  LWK The balance, it has to do with legged locomotion. It has to do with all these problems
*  that the human body solves when we're walking, for example. All the fundamentals are there.
*  Ivan Yeah. I think that was the motivation to try and get more at the fundamentals of how animals
*  work. The idea that it would result in machines that were anything like practical,
*  like we're making now, that wasn't anywhere in my head. As an academic, I was mostly just trying
*  to do the next thing, make some progress, impress my colleagues if I could.
*  LWK And have fun.
*  Ivan And have fun.
*  LWK Pogo stick robot.
*  Ivan Pogo stick robot.
*  LWK What was on the technical side? What are some of the challenges of
*  getting to the point where we saw in the video the Pogo stick robot that's actually successfully
*  hopping and then eventually doing flips and all this kind of stuff?
*  Ivan Well, in the very early days, I needed some better engineering than I could do myself.
*  I hired Ben Brown. We each had our way of contributing to the design, and we came up
*  with a thing that could start to work. I had some stupid ideas about how the actuation system should
*  work. We sorted that out. It wasn't that hard to make it balanced once you get the physical machine
*  to be working well enough and have enough control over the degrees of freedom.
*  We started out by having it floating on an inclined air table. That only gave us like
*  six foot of travel. Once it started working, we switched to a thing that could run around the room
*  on another device. It's hard to explain these without you seeing them, but you probably know
*  what I'm talking about, a planarizer. Then the next big step was to make it work in 3D,
*  which that was really the scary part. With these simple things, people had inverted
*  pendulums at the time for years, and they could control them by driving a cart back and forth.
*  But could you make it work in three dimensions while it's bouncing and all that? It turned out
*  not to be that hard to do, at least at the level of performance we achieved at the time.
*  You mentioned inverted pendulum, but can you explain how a hopping stick in 3D
*  can balance itself? What does the actuation look like?
*  The simple story is that there's three things going on. There's something making it bounce.
*  We had a system that was estimating how high the robot was off the ground.
*  There's energy that can be in three places in a pogo stick. One is in the spring,
*  one is in the altitude, and the other is in the velocity. When at the top of the hop,
*  it's all in the height. You could just measure how high you're going and thereby have an idea
*  of a lot about the cycle, and you could decide whether to put more energy in or less.
*  That's one element. Then there's a part that you decide where to put the foot. If you think when
*  you're landing on the ground with respect to the center of mass, if you think of a pole vaulter,
*  the key thing the pole vaulter has to do is get its body to the right place when the pole gets stuck.
*  If they're too far forward, they get thrown backwards. If they're too far back, they go
*  over. What they need to do is get it so that they go mostly up to get over the thing. High jumpers
*  is the same kind of thing. There's a calculation about where to put the foot, and we did something
*  relatively simple. Then there's a third part to keep the body at an attitude that's upright.
*  Because if it gets too far, you could hop and just keep rotating around. But if it gets too far,
*  then you run out of motion of the joints at the hips. You have to do that. We did that by
*  applying a torque between the legs and the body every time the foot's on the ground. You only can
*  do it while the foot's on the ground. In the air, the physics don't work out.
*  How far does it have to tilt before it's too late to be able to balance itself?
*  Or is it impossible to balance itself, correct itself?
*  Well, you're asking an interesting question because in those days, we didn't actually optimize
*  things. They probably could have gone much further than we did and then had higher performance.
*  We just got a sketch of a solution and worked on that. Then in years since, some people working
*  for us, some people working for others, people came up with all kinds of equations or algorithms
*  for how to do a better job, be able to go faster. One of my students worked on getting things to
*  go faster. Another one worked on climbing over obstacles. Because when you're running,
*  it's one on the open ground. It's one thing. If you're running up a stair, you have to adjust
*  where you are. Otherwise, things don't work out right. You land your foot on the edge of the step.
*  There's other degrees of freedom to control if you're getting to more realistic, practical
*  situations. I think it's really interesting to ask about the early days because believing in yourself,
*  believing that there's something interesting here. Then you mentioned finding somebody else,
*  Ben Brown. What's that like finding other people with whom you can
*  build this crazy idea and actually make it work?
*  Probably the smartest thing I ever did is to find the other people. When I look at it now,
*  I look at Boston Dynamics and all the really excellent engineering there, people who really
*  make stuff work. I'm only the dreamer. When you talk about pogo stick robot or legged
*  robots, whether it's quadrupeds or humanoid robots, did people doubt that this is possible?
*  Did you experience a lot of people around you? I don't know if they doubted whether it was
*  possible, but I think they thought it was a waste of time. Oh, it's not even an interesting problem.
*  I think for a lot of people, people who were... I think it's been both though. Some people,
*  I felt like they were saying, oh, why are you wasting your time on this stupid problem?
*  Then I've been at many things where people have told me it's been an inspiration to go out and
*  attack these harder things. I think it has turned out, I think legged locomotion has turned out to
*  be a useful thing. Did you ever have doubt about bringing Atlas to life, for example, or
*  with Big Dog, just every step of the way, did you have doubt like, this is too hard of a problem?
*  At first, I wasn't an enthusiast for the humanoids because, again, it goes back to saying, what's
*  the functionality? The form wasn't as important as the functionality. Also, there's an aspect to
*  humanoid robots that's all about the cosmetics where there isn't really other functionality.
*  That is off-putting for me as a roboticist. I think the functionality really matters.
*  Probably that's why I avoided humanoid robots to start with. I'll tell you,
*  after we started working on them, you could see that the connection and the impact with
*  other people, whether they're lay people or even other technical people, there's a special thing
*  that goes on. Even though most of the humanoid robots aren't that much like a person.
*  We anthropomorphize and we see the humanity. Also, with Spot, you can see,
*  not the humanity, but whatever we find compelling about social interactions there in Spot as well.
*  I'll tell you, I go around giving talks and take Spot to a lot of them. It's amazing. The media
*  likes to say that they're terrifying and that people are afraid. YouTube commenters like to say
*  that it's frightening. When you take a Spot out there, maybe it's self-selecting, but you get a
*  crowd of people who want to take pictures, want to pose for selfies, want to operate the robot,
*  want to pet it, want to put clothes on it. It's amazing. Yeah, I love Spot. If we move around
*  history a little bit, you said, I think in the early days of Boston Dynamics, that you quietly
*  worked on making a running version of iBum, Sony's robot dog. It's just an interesting
*  little tidbit of history for me. What stands out to your memory from that task? For people who don't
*  know that little dog robot moves slowly, how did that become Big Dog? What was involved there? What
*  was the dance between how do we make this cute little dog versus a thing that can actually care
*  a lot of payload and move fast and stuff like that? What the connection was is that at that point,
*  Boston Dynamics was mostly a physics-based simulation company. When I left MIT to start
*  Boston Dynamics, there was a few years of overlap, but the concept wasn't to start a robot company.
*  The concept was to use this dynamic simulation tool that we developed to do robotics for other
*  things. Working with Sony, we got back into robotics by doing the iBo runner. We made some
*  tools for programming Curio, which was a small humanoid this big that could do some dancing and
*  other kinds of fun stuff. I don't think it ever reached the market, even though they did show it.
*  When I look back, I say that we got us back where we belonged.
*  You rediscovered the soul of the company.
*  That's right.
*  From there, it was always about robots.
*  You started Boston Dynamics in 1992. What are some fond memories from the early days?
*  One of the robots that we built wasn't actually a robot. It was a surgical simulator,
*  but it had force feedback. It had all the techniques of robotics. You looked down into this
*  mirror, it actually was. It looked like you were looking down onto the body you were working on.
*  Your hands were underneath the mirror, so they were where you were looking. You had tools in
*  your hands that were connected up to these force feedback devices made by another MIT spinout,
*  Sensible Technologies. They made the force feedback device. We attached the tools and we
*  wrote all the software and did all the graphics. We had 3D computer graphics. It was in the old
*  days when you had a silicon graphics computer that was about this big. It was the heater in
*  the office, basically. We were doing surgical operations, anastomosis, which was stitching
*  tubes together, tubes like blood vessels or other things in their body. You could feel and you could
*  see the tissues move. It was really exciting. The idea was to make a trainer to teach surgeons
*  how to do stuff. We built a scoring system because we interviewed surgeons that told us
*  what you're supposed to do and what you're not supposed to do. You're not supposed to
*  tear the tissue. You're not supposed to touch it in any place except for where you're trying to
*  engage. There were a bunch of rules. We built this thing and took it to a trade show,
*  a surgical trade show. The surgeons were practically lined up. We kept a score and we
*  posted their scores like on a video game. Those guys are so competitive that they really loved
*  doing it. They would come around and they'd see someone's score was higher there, so they would
*  come back. We figured out shortly after that we thought surgeons were going to pay us to get
*  trained on these things. The surgeons thought we should pay them so they could teach us about
*  the thing. There was no money from the surgeons. We looked at it and thought, well, maybe we could
*  sell it to hospitals that would train their surgeons. Then we said, well, at the time we
*  were probably a 12-person company or maybe 15 people, I don't remember. There was no way we
*  could go after a marketing activity. The company was all bootstrapped in those years. We never had
*  investors until Google bought us, which was after 20 years. We didn't have any resources to go after
*  hospitals. At one day, Rob and I were looking at that and we said we'd built another simulator
*  for knee arthroscopy. We said, this isn't going to work. We killed it and we moved on. That was
*  really a milestone in the company because we understood who we were and what would work and
*  even though technically it was really a fascinating thing. What was that meeting like?
*  Were you just sitting at a table? You know what? Probably. We're going to pivot completely. We're
*  going to let go of this thing we put so much hard work into and then go back to the thing.
*  It just always felt right unless we did it. Just look at each other and say, let's build robots.
*  What was the first robot you built under the flag of Boston Dynamics? Big Dog?
*  Well, there was the IBO runner, but it wasn't even a whole robot. It was just legs that we took off
*  the legs on IBOs and attached the legs we'd made. We got that working and showed it to the Sony people.
*  We worked pretty closely with Sony in those years. One of the interesting things is that
*  it was before the internet and Zoom and anything like that. We had six ISDN lines installed and we
*  would have a telecon every week that worked at very low frame rate, something like 10 hertz.
*  English across the boundary with Japan was a challenge trying to understand what each of us
*  was saying and have meetings every week for several years doing that. It was a pleasure
*  working with them. They were really supporters. They seemed to like us and what we were doing.
*  That was the real transition from us being a simulation company into being a robotics
*  company again. It was a quadruped? The legs were four legs or two legs?
*  Yeah, four legs. Yeah.
*  What did you learn from that experience of building basically a fast moving quadruped?
*  Mostly we learned that something that small doesn't look very exciting when it's running.
*  It's like it's scampering. You had to watch a slow-mo for it to look like it was interesting.
*  Watch it fast. One of my things was to show stuff in video from the very early days of the hopping
*  machines. I was always focused on how is this going to look through the viewfinder? Running
*  IBO didn't look so cool through the viewfinder. What came next in terms of what was a big next
*  milestone in terms of a robot you built? You got to say that Big Dog sort of put us
*  on the map and got our heads really pulled together. We scaled up the company.
*  Big Dog was the result of Alan Rudolph at DARPA starting a biodynamics program. He put out a
*  request for proposals. I think there were 42 proposals written and three got funded.
*  One was Big Dog. One was a climbing robot, Rise. That put things in motion. We hired
*  Martin Buehler. He was a professor in Montreal at McGill. He was incredibly important for getting
*  Big Dog out of the lab and into the mud, which was a key step to really be willing to go out there
*  and build it, break it, fix it, which is one of our mottos at the company.
*  Testing in the real world. For people who don't know Big Dog, maybe you can correct me,
*  it's a big quadruped, four-legged robot. It looks big, could probably carry a lot of weight.
*  Not the most weight that Boston Dynamics have built, but a lot.
*  No. Well, it's the first thing that worked. Let's see, if we go back to the leg lab,
*  we'd built a quadruped that could do many of the things that Big Dog did, but it had a hydraulic
*  pump sitting in the room with hoses connected to the robot. It had a VAX computer in the next room.
*  It needed its own room because it was this giant thing with air conditioning, and it had this very
*  complicated bus connected to the robot. The robot itself just had the actuators, it had gyroscopes
*  for sensing and some other sensors, but all the power and computing was off board.
*  Big Dog had all that stuff integrated on the platform. It had a gasoline engine for power,
*  which was a very complicated thing to undertake. It had to convert the rotation of the engine into
*  hydraulic power, which is how we actuated it. There was a lot of learning just on building the
*  physical robot and the system integration for that. Then there was the controls of it.
*  For Big Dog, you brought it all together onto one platform.
*  You could take it out in the woods.
*  Yeah, and you did.
*  We did. We spent a lot of time down at the Marine Corps base in Quantico where there was a trail
*  called the Guadalcanal Trail. Our milestone that DARPA had specified was that we could go
*  on this one particular trail that involved a lot of challenge. We spent a lot of time, our team
*  spent a lot of time down there. Those were fun days.
*  Hiking with a robot. What did you learn about what it takes to balance a robot like that on a trail?
*  On a hiking trail in the woods? Basically, forget the woods, just the real world.
*  That's the big leap into testing in the real world.
*  Yeah. As challenging as the woods were, working inside of a home or in an office is really harder.
*  Because when you're in the woods, you can actually take any path up the hill. All you have to do is
*  avoid the obstacles. There's no such thing as damaging the woods, at least to first order.
*  Whereas if you're in a house, you can't leave scuff marks, you can't bang into the walls.
*  The robots aren't very comfortable bumping into the walls, especially in the early days.
*  I think those were actually bigger challenges once we faced them. It was mostly getting the systems
*  to work well enough together, the hardware systems to work, and the controls.
*  In those days, we did have a human operator who did all the visual perception going up the
*  Guadalcanal Trail. There was an operator who was right there, who was very skilled.
*  Even though the robot was balancing itself and placing its own feet,
*  if the operator didn't do the right thing, it wouldn't go.
*  Years later, we went back with one of the electric precursor to spot. We had advanced the controls
*  and everything so much that an amateur, complete amateur, could operate the robot the first time,
*  up and down and up and down, whereas it had taken us years to get there in the previous robot.
*  If you fast forward, Big Dog eventually became spot.
*  Big Dog became LS3, which is the big load carrying one.
*  Just a quick pause, it can carry 400 pounds.
*  It was designed to carry 400, but we had it carrying about 1,000 pounds.
*  Of course you did, just to make sure.
*  We had one carrying the other one, we had two of them. We had one carrying the other one.
*  There's a little clip of that. We should put that out somewhere. That's from 20 years ago.
*  It can go for very long distances. It can travel 20 miles.
*  Gasoline.
*  That eventually just, okay, sorry. LS3, then how did that lead to spot?
*  So Big Dog and LS3 had engine power and hydraulic actuation. Then we made a robot that was
*  electric power. There's a battery driving a motor, driving a pump, but still hydraulic actuation.
*  Larry asked us, could you make something that weighed 60 pounds that would
*  not be so intimidating if you had it in a house where there were people?
*  That was the inspiration behind the spot, pretty much as it exists today. We did a prototype the
*  same size that was the first all-electric, non-hydraulic robot.
*  What was the conversation with Larry Page like about? Here's a guy that is very product focused
*  and can see a vision for what the future holds. That's just interesting aside. What was the
*  brainstorm about the future robotics with him? It was almost as simple as what I just said.
*  We were having a meeting. He said, yeah, geez, do you think you could make a smaller one that
*  wouldn't be so intimidating like a Big Dog if it was in your house? I said, yeah, we could do that.
*  We started and did. Is there a lot of technical challenges to go from
*  hydraulic to electric? I had been in love with hydraulics and still
*  love hydraulics. It's a great technology. It's too bad that somehow the world out there looks at it
*  like it's old-fashioned or that it's icky. It's true that it is very hard to keep it from having
*  some amount of dripping from time to time. If you look at the performance, how strong you can get
*  in a lightweight package. Of course, we did a huge amount of innovation. Most of hydraulic
*  control, that is the valve that controls the flow of oil, had been designed in the 50s for
*  airplanes. It had been made robust enough, safe enough that you could count on it so that humans
*  could fly in airplanes. Very little innovation had happened. That might not be fair to the people
*  who make the valves. I'm sure that they did innovate, but the basic design had stayed the
*  same. There was so much more you could do. Our engineers designed valves, the ones that are in
*  Atlas, for instance, that had new kinds of circuits. They did some of the computing that could get you
*  much more efficient use. They were much smaller and lighter so that the whole robot could be
*  smaller and lighter. We made a hydraulic power supply that had a bunch of components integrated
*  in this tiny package. It's about this big, the size of a football. It weighs five kilograms and
*  it produces five kilowatts of power. Of course, it has to have a battery operating, but it's got a
*  motor, a pump, filters, heat exchanger to keep it cool, some valves, all in this tiny little package.
*  Hydraulics could still have a ways to go. One of the things that stands out about the robots
*  Boston Dynamics have created is how beautiful the movement is, how natural the walking is and
*  running is, even flipping is, throwing is. Maybe you can talk about what's involved in
*  making it look natural. Well, I think having good hardware is part of the story and people who think
*  you don't need to innovate hardware anymore are wrong, in my opinion. I think one of the things,
*  certainly in the early years for me, taking a dynamic approach where you think about what's
*  the evolution of the motion of the thing going to be in the future and having a prediction of that
*  that's used at the time that you're giving signals to it, as opposed to it all being servoing, which
*  is servoing is sort of backward looking. It says, okay, where am I now? I'm going to try and adjust
*  for that, but you really need to think about what's coming. How far ahead do you have to look in time?
*  It's interesting. I think that the number is only a couple of seconds for a spot. There's a
*  limited horizon type approach where you're recalculating, assuming what's going to happen
*  in the next second or second and a half. Then you keep iterating. The next, even though a tenth of
*  a second later, you'll say, okay, let's do that again and see what's happening. You're looking at
*  what the obstacles are, where the feet are going to be placed. You have to coordinate a lot of
*  things if you have obstacles and you're balancing at the same time. It's that limited horizon type
*  calculation that's doing a lot of that. If you're doing something like a somersault,
*  you're looking out a lot further. If you want to stick the landing, you have to get the right.
*  You have to, at the time of launch, have momentum and rotation, all those things coordinated so that
*  a landing is within reach. How hard is it to stick a landing? It's very much under-actuated.
*  Once you're in the air, you don't have as much control about anything. How hard is it to get
*  that to work? First of all, did flips with a hopping robot. If you look at the first time
*  we ever made a robot do a somersault, it was in a planar robot. It had a boom.
*  So it was restricted to the surface of a sphere, we call that planar. It could move fore and aft,
*  it could go up and down, and it could rotate. The calculation of what you need to do to stick
*  a landing isn't all that complicated. You have to get time to make the rotation. How high you jump
*  gives you time. You look at how quickly you can rotate. If you get those two right, then when you
*  land, you have the feet in the right place. You have to get rid of all that rotational and linear
*  momentum. That's not too hard to figure out. Back in about 1985 or 1986, I can't remember,
*  we had a simple robot doing somersaults. To do it in 3D, really the calculation is the same. You
*  just have to be balancing in the other degrees of freedom. If you're just doing a somersault,
*  it's just a planar thing. Roy Murabu was my graduate student and we were at MIT,
*  which is when we made a two-legged robot do a 3D somersault for the first time.
*  There, in order to get enough rotation rate, you needed to do tucking also.
*  Withdraw the legs in order to accelerate it. He did some really fascinating work on how you
*  stabilize more complicated maneuvers. Remember, he was a champion gymnast before he'd come to me.
*  So he had the physical abilities and he was an engineer so he could translate some of that into
*  the math and the algorithms that you need to do that. He knew how humans do it. He just had to
*  get robots to do the same. Unfortunately, though, humans don't really know how they do it.
*  We're coached. We have ways of learning, but do we really understand in a physics way
*  what we're doing? Probably most gymnasts and athletes don't know.
*  It's in some way, by building robots, you are in part understanding how humans do it, like walking.
*  Most of us walk without considering how we walk, really, and how we make it so natural and efficient,
*  all those kinds of things. Atlas still doesn't walk like a person
*  and it still doesn't walk quite as gracefully as a person, even though it's been getting closer and
*  closer. The running might be close to a human, but the walking is still a challenge.
*  That's interesting, right? That running is closer to a human. It just shows that the more aggressive
*  and the more you leap into the unknown, the more natural it is. Walking is falling always, right?
*  And something weird about the knee, that you can do this folding and unfolding and get it to work
*  out just right. There's compliances. Compliance means springiness in the design that are important
*  to how it all works. Well, we used to have a motto at the Boston Dynamics in the early days,
*  which was, you have to run before you can walk. That's a good motto. You also had Wildcat,
*  which was along the way towards Spot, which is a quadruped that went 19 miles an hour on flat
*  terrain. Is that the fastest you've ever built? Oh yeah. It might be the fastest quadruped in the
*  world. I don't know. For a quadruped, probably. Of course, it was probably the loudest too.
*  So we had this little racing go-kart engine on it and we would get people from three buildings away
*  sending us complaining about how loud it was. So at the leg lab, I believe most of the robots
*  didn't have knees. How do you figure out what is the right number of actuators? What are the joints
*  to have? What do you need to have? We humans have knees and all kinds of interesting stuff on the
*  feet. The toe is an important part, I guess, for humans. Or maybe it's not. I injured my toe
*  recently and it made running very unpleasant. So that seems to be kind of important. So how do
*  you figure out for efficiency, for function, for aesthetics, how many joints to have,
*  how many actuators to have? Well, it's always a balance between wanting to get where you really
*  want to get and what's practical to do based on your resources or what you know and all that.
*  So I mean, the whole idea of the Poga stick was to do a simplification. Obviously, it didn't look
*  like a human. I think a technical scientist could appreciate that we were capturing some
*  of the things that are important in human locomotion without it looking like it, without
*  having a knee and ankle. I'll tell you the first sketch that Ben Brown made when we were talking
*  about building this thing was a very complicated thing with zillions of springs, lots of joints.
*  It looked much more like a kangaroo or an ostrich or something like that, things we were paying a
*  lot of attention to at the time. So my job was to say, okay, well, let's do something simpler to
*  get started and maybe we'll get there at some point. I just love the idea that you two were
*  studying kangaroos and ostriches. Oh yeah. We filmed and digitized
*  data from horses. I did a dissection of an ostrich at one point, which has absolutely
*  remarkable legs. Dumb question. Do ostriches have a lot of musculature on the legs or no?
*  Most of it's up in the feathers, but there's a huge amount going on in the feathers, including
*  a knee joint, the knee joint's way up there. The thing that's halfway down the leg
*  that looks like a backwards knee is actually the ankle. The thing on the ground, which looks like
*  the foot is actually the toes, it's an extended toe. But the basic morphology is the same in
*  all these animals. What do you think is the most beautiful movement of an animal? What animal
*  you think is the coolest? Land animal. Because fish is pretty cool. Like the way fish moves
*  the water, but like leggy locomotion. The slow-mo's of cheetahs running are incredible.
*  There's so much back motion and grace. Of course, they're moving very fast.
*  The animals running away from the cheetah are pretty exciting. The pronghorn, which they do this,
*  all four legs at once jump, called the prong, to kind of confuse the, especially if there's a group
*  of them to confuse whoever's chasing them. So they do like a misdirection type of thing?
*  Yep, they do a misdirection thing. The front-on views of the cheetahs running fast, where the tail
*  is whipping around to help in the turns, to help stabilize in the turns, that's pretty exciting.
*  Because they spend a lot of time in the air, I guess, as they're running that fast.
*  But they also turn very fast. Is that a tail thing or do you have to have contact with ground?
*  Everything in the body is probably helping turn, because they're chasing something that's trying
*  to get away that's also zigzagging around. But I would be remiss if I didn't say humans are
*  pretty good too. You watch gymnasts, especially these days, they're doing just incredible stuff.
*  Well, especially Olympic-level gymnasts. See, but there could be cheetahs that are Olympic-level.
*  We might be watching the average cheetah versus there could be a really special cheetah that can
*  do like... When do the knees first come into play in you building legged robots?
*  In Big Dog. Big Dog came first and then Little Dog was later.
*  And there's a big compromise there. Human knees have multiple muscles and you could argue that
*  there's... I mean, it's a technical thing about negative work. When you're contracting a joint,
*  but you're pushing out, that's negative work. And if you don't have a place to store that,
*  it can be very expensive to do negative work. And in Big Dog, there was no place to store
*  negative work in the knees. But Big Dog also had pogo stick springs down below. So part of the
*  action was to comply in a bouncing motion. Later on in spot, we took that out. As we got further
*  and further away from the leg lab, we had more energy-driven controls.
*  Is there something to be said about knees that go forward versus backward?
*  Sure. There's this idea called passive dynamics, which says that although you can use computers
*  and actuators to make a motion, a mechanical system can make a motion just by itself if it
*  gets stimulated the right way. So, Tad McGeer, I think in the mid-'80s, maybe it was in the late
*  80s, started to work on that. And he made this legged system that could walk down an inclined
*  plane where the legs folded and unfolded and swung forward, do the whole walking motion,
*  where there was no computer. There were some adjustments to the mechanics so that there were
*  dampers and springs in some places that helped the mechanical action happen. It was essentially a
*  mechanical computer. And the interesting idea there is that it's not all about the brain
*  dictating to the body what the body should do. The body is a participant in the motion.
*  So, a great design for a robot has a mechanical component where
*  the movement is efficient even without a brain.
*  Yes.
*  How do you design that?
*  I think that these days, most robots aren't doing that. Most robots are basically using the computer
*  to govern the motion. Now, the brain though is taking into account what the mechanical thing
*  can do and how it's going to behave. Otherwise, it would have to really forcefully move everything
*  around all the time, which probably some solutions do. But I think you end up with a more efficient
*  and more graceful thing if you're taking into account what the machine wants to do.
*  So, this might be a good place to mention that you're now leading up the Boston Dynamics AI
*  Institute, newly formed, which is focused more on designing the robots of the future.
*  I think one of the things, maybe you can tell me the big vision for what's going on. One of the
*  things is this idea that hardware still matters with organic design and so on. Maybe before that,
*  can you zoom out and tell me what the vision is for the AI Institute?
*  I like to talk about intelligence having two parts, an athletic part and a cognitive part.
*  And I think Boston Dynamics, in my view, has sort of set the standard for what athletic
*  intelligence can be. And it has to do with all the things we've been talking about, the
*  mechanical design, the real-time control, the energetics and that kind of stuff.
*  But obviously, people have another kind of intelligence and animals have another kind
*  of intelligence. We can make a plan. Our meeting started at 9.30. I looked up on Google Maps how
*  long it took to walk over here. It was 20 minutes. So, I decided, okay, I'd leave my house at 9,
*  which is what I did. Simple intelligence, but we use that kind of stuff all the time.
*  It's sort of what we think of as going on in our heads. And I think that's in short supply
*  for robots. Most robots are pretty dumb. And as a result, it takes a lot of skilled people to
*  program them to do everything they do. And it takes a long time. And if robots are going to
*  satisfy our dreams, they need to be smarter. So, the AI Institute is designed to combine
*  that physicality of the athletic side with the cognitive side. So, for instance,
*  we're trying to make robots that can watch a human do a task, understand what it's seeing,
*  and then do the task itself. So, sort of OJT for robot, on-the-job training for robots
*  as a paradigm. Now, that's pretty hard. And it's sort of science fiction. But our idea is to work
*  on a longer timeframe and work on solving those kinds of problems. And I have a whole list of
*  things that are kind of like in that vein. Maybe we can just take many of the things
*  you mentioned, just take it as a tangent. First of all, athletic intelligence is a super cool term.
*  And that really is intelligence. We humans kind of take it for granted that we're so good at
*  walking and moving about the world. And using our hands, you know, the mechanics of interacting with
*  these parts, these two things. You've never touched those things before, right?
*  Well, I've touched ones like this. Look at all the things I can do, right? I can juggle them.
*  Rotate it this way. I can rotate it without looking. I could fetch these things out of my pocket and
*  figure out which one was which and all that kind of stuff. And I don't think we have much of a clue
*  how all that works yet. Right. And that's, I really like putting that under the banner of athletic
*  intelligence. What are the big open problems in athletic intelligence? So, Boston Dynamics
*  with Spot, with Atlas just have shown time and time again, like push the limits of what we think
*  is possible with robots. But where do we stand actually, if we kind of zoom out? What are the
*  big open problems on the athletic intelligence side? I mean, one question you could ask, it isn't
*  my question, but are they commercially viable? Will they increase productivity? And I think
*  we're getting very close to that. I don't think we're quite there still. Most of the robotics
*  companies, it's a struggle. It's really the lack of the cognitive side that probably is the biggest
*  barrier at the moment, even for the physically successful robots. But your question is, I mean,
*  you can always do a thing that's more efficient, lighter, more reliable. I'd say reliability.
*  I know that Spot, they've been working very hard on getting the tail of the reliability curve
*  up and they've made huge progress. So, the robots, there's 1,500 of them out there now,
*  many of them being used in practical applications day in and day out where they have to work
*  reliably. And it's very exciting that they've done that. But it takes a huge effort to get that
*  kind of reliability in the robot. There's cost too. You'd like to get the cost down. Spots are
*  still pretty expensive and I don't think that they have to be, but it takes a different kind
*  of activity to do that. Now that, I think that Boston Dynamics is owned primarily by Hyundai
*  now. And I think that the skills of Hyundai in making cars can be brought to bear in making
*  robots that are less expensive and more reliable and those kinds of things. So on the cognitive side
*  for the Eye Institute, what's the trade-off between moonshot projects for you and maybe
*  incremental progress? That's a good question. I think we're using the paradigm called stepping
*  stones to moonshots. I don't believe, that was in my original proposal for the Institute,
*  stepping stones to moonshots. I think if you go more than a year without seeing a tangible
*  status report of where you are, which is the stepping stone, and it could be a simplification,
*  right? You don't necessarily have to solve all the problems of your target goal, even though
*  your target goal is going to take several years. Those stepping stone results give you feedback,
*  give motivation because usually there's some success in there. And so that's the mantra
*  we've been working on. And that's pretty much how I'd say Boston Dynamics has worked,
*  where you make progress and show it as you go. Show it to yourself, if not to the world.
*  What does success look like? What are some of the milestones you're chasing?
*  Well, with Watch, Understand, Do, the project I mentioned before, we've broken that down into
*  getting some progress with what does meaningfully watching something mean,
*  breaking down an observation of a person doing something into the components, segmenting. You
*  watch me do something, I'm going to pick up this thing and put it down here and stack this on it.
*  Well, it's not obvious if you just look at the raw data, what the sequence of acts are. It's
*  really a creative, intelligent act for you to break that down into the pieces and understand
*  them in a way so you could say, okay, what skill do I need to accomplish each of those things?
*  So we're working on the front end of that kind of a problem where we observe and translate the – if
*  it may be video, it may be live – into a description of what we think is going on
*  and then try and map that into skills to accomplish that. We've been developing skills as well.
*  So we have multiple stabs at the pieces of doing that.
*  And this is usually video of humans manipulating objects with their hands kind of thing?
*  Mm-hmm. We're starting out with bicycle repair, some simple bicycle repair.
*  Oh, no. That seems complicated. That seems really complicated.
*  It is. But there's some parts of it that aren't, like putting the seat in. You have a tube that
*  goes inside of another tube and there's a latch. That should be within range.
*  Is it possible to observe, to watch a video like this without having an
*  explicit model of what a bicycle looks like? I think it is. And I think that's the kind
*  of thing that people don't recognize. Let me translate it to navigation. I think the
*  basic paradigm for navigating a space is to get some kind of sensor that tells you where
*  the obstacle is and what's open, build a map, and then go through the space.
*  But if we were doing on-the-job training where I was giving you a task, I wouldn't have to say
*  anything about the room. We came in here. All we did is adjust the chair, but we didn't say
*  anything about the room and we could navigate it. So I think there's opportunities to build that
*  navigation skill into robots. We're hoping to be able to do that.
*  So operate successfully under a lot of uncertainty.
*  Yeah. And lack of specification.
*  Lack of specification.
*  I mean, that's what intelligence is, right? It's kind of dealing with
*  understanding a situation even though it wasn't explained.
*  How big of a role does machine learning play in all of this? Is this more and more learning-based?
*  You know, since chat GBT, which is a year ago, basically, there's a huge interest in that and
*  a huge optimism about it. And I think that there's a lot of things that machine learn,
*  that kind of machine learning. Now, of course, there's lots of different kinds of machine
*  learning. I think there's a lot of interest and optimism about it. I think the facts on the ground
*  are that doing physical things with physical robots is a little bit different than language.
*  And the tokens sort of don't exist. Pixel values aren't like words. But I think that
*  there's a lot that can be done there. We have several people working on machine learning
*  approaches. I don't know if you know, but we opened an office in Zurich recently. And Marco
*  Hutter, who's one of the real leaders in reinforcement learning for robots, is the
*  director of that office. He's still half-time at ETH, the university there, where he has an
*  unbelievably fantastic lab. And then he's half-time leading, will be leading off efforts in the Zurich
*  office. So we have a healthy learning component. But there's part of me that still says, if you
*  look out in the world at what the most impressive performances are, they're still pretty much,
*  I hate to use the word traditional, but that's what everybody's calling it, traditional controls,
*  like model predictive control. The Atlas performances that you've seen are mostly
*  model predictive control. They've started to do some learning stuff that's really incredible.
*  I don't know if it's all been shown yet, but you'll see it over time. And then Marco has done some
*  great stuff and others. So especially for the athletic intelligence piece, the traditional
*  approach seems to be the one that still performs the best. I think we're going to find a mating of
*  the two and we'll have the best of both worlds. And we're working on that at the Institute too.
*  If I can talk to you about teams, you've built an incredible team at Boston Dynamics before at MIT
*  and CMU, at Boston Dynamics, and now at the AI Institute. And you said that there's four
*  components to a great team, technical fearlessness, diligence, intrepidness, and fun,
*  technical fun. Can you explain each? Technical fearlessness, what do you mean by that?
*  Sure. Technical fearlessness means being willing to take on a problem that you don't know how to
*  solve and study it, figure out an entry point, maybe a simplified version or a simplified solution
*  or something, learn from the stepping stone and go back and eventually make a solution that
*  meets your goals. And I think that's really important.
*  The fearlessness comes into play because some of it has never been done before.
*  Yeah. And you don't know how to do it. And there's the easier stuff to do in life.
*  So, I mean, I don't know, watch, understand, do. It's a mountain of a challenge.
*  So that's the really big challenge you're tackling now. Can we watch humans at scale
*  and have robots by watching humans become effective actors in the world?
*  Yeah. I mean, we have others like that. We have one called Inspect, Diagnose, Fix.
*  Like, you know, you call up the Maytag repairman. Okay, he's the one who you don't have to call.
*  But you call up the dishwasher repair person and they come to your house and they look at your
*  machine. It's already been actually figured out that something doesn't work, but they have to kind
*  of examine it and figure out what's wrong and then fix it. And I think robots should be able to do
*  that. Boston Dynamics already has spot robots collecting data on machines, things like thermal
*  data, reading the gauges, listening to them, getting sounds. And that data are used to
*  determine whether they're healthy or not. But the interpretation isn't done by the robots yet. And
*  certainly the diagnosing and the fixing isn't done yet, but I think it could be. And that's
*  bringing the AI and combining it with the physical skills to do it.
*  Yeah. And you're referring to the fixing in the physical world. I can't wait until you can
*  fix the psychological problems of humans and show up and just talk, do therapy.
*  That's a different thing.
*  Yeah, it's different. Well, that's all part of the same thing. Again, humanity. Maybe.
*  You mean convincing you it's okay that the dishwasher's broken just through the marketing
*  approach?
*  Yeah, exactly. It's all, yeah, don't sweat the small stuff. Yeah, as opposed to fixing the
*  dishwasher, it'll convince you that it's okay that the dishwasher's broken. It's a different approach.
*  Diligence. Why is diligence important?
*  Well, if you want a real robot solution, it can't be a very narrow solution that's going to break
*  at the first variation in what the robot does or the environment if it wasn't exactly as you
*  expected it. So how do you get there? I think having an approach that leaves you unsatisfied
*  until you've embraced the bigger problem is the diligence I'm talking about.
*  And again, I'll point out Boss Dynamics. I think they've done it. Some of the videos that we had
*  showing the engineer making it hard for the robot to do its task. Spot opening a door and then the
*  guy gets there and pushes on the door so it doesn't open the way it's supposed to, pulling on the
*  rope that's attached to the robot so its navigation has been screwed up. We have one where the robot's
*  climbing stairs and the engineer is tugging on a rope that's pulling it back down the stairs.
*  That's totally different than just the robot seeing the stairs, making a model, putting its
*  feet carefully on each step. But that's what probably robotics needs to succeed and having
*  that broader idea that you want to come up with a robust solution is what I meant by diligence.
*  So really testing it in all conditions, perturbing the system in all kinds of ways.
*  And as a result, creating some epic videos. The legendary.
*  The fun part, the hockey stick.
*  And then yes, tugging on Spot as it's trying to open the door.
*  I mean, it's great testing, but it's also, I don't know, it's just somehow extremely compelling
*  demonstration of robotics in video form.
*  I learned something very early on with the first three dimensional hopping machine. If you just
*  show a video of it hopping, it's a so what. If you show it falling over a couple of times and you can
*  see how easily and fast it falls over, then you appreciate what the robot's doing when it's doing
*  its thing. So I think the reaction you just gave to the robot getting kind of interfered with or
*  tested while it's going through the door, it's showing you the scope of the solution.
*  The limits of the system, the challenges involved in failure. If it's shown both failure and success
*  makes you appreciate the success. Yeah.
*  And then just the way the videos are done in Balls Anonymics are incredible because they're
*  not, there's no flash. There's no extra like production. It's just raw testing of the robot.
*  Well, you know, I was the final edit for most of the videos up until
*  about three years ago or four years ago. And my theory of the video is no explanation.
*  If they can't see it, then it's not the right thing. And if you do something worth showing,
*  then let them see it. Don't interfere with a bunch of titles that slow you down
*  or a bunch of distraction. Just do something worth showing and then show it.
*  That's brilliant.
*  It's hard though for people to buy into that.
*  Yeah. I mean, people always want to add more stuff, but the simplicity of just
*  do something worth showing and show it. That's brilliant. And don't add extra stuff.
*  People have criticized, especially the big dog videos where there's a human
*  driving the robot. And I understand the criticism now. At the time, we wanted to just show, look,
*  this thing's using its legs to get up the hill. So we focused on showing that, which was, we thought
*  the story, the fact that there was a human. So they were thinking about autonomy, whereas we were
*  thinking about the mobility. And so we've adjusted to a lot of things that we see that people care
*  about trying to be honest. We've always tried to be honest.
*  But also just show cool stuff in its raw form, the limits of the system,
*  the see the system be perturbed and be robust and resilient and all that kind of stuff.
*  And dancing with some music. Intrepidness and fun. So intrepid.
*  I mean, it might be the most important ingredient. And that is, robotics is hard.
*  It's not going to work right away. So don't be discouraged is all it really means.
*  So usually when I talk about these things, I show videos and I show a long string of outtakes.
*  And you have to have courage to be intrepid when you work so hard, you built your machine,
*  and then you're trying and it just doesn't do what you thought it would do, what you want it to do.
*  And you have to stick to it and keep trying. How long, I mean, we don't often see that,
*  the story behind Spot and Atlas, how long, how many failures was there along the way to get
*  a working Atlas, a working Spot in the early days, even working Big Dog?
*  There's a video of Atlas climbing three big steps. And it's very dynamic and it's really
*  exciting, a real accomplishment. It took 109 tries and we have video of every one of them.
*  We shoot everything. Again, this is at Boston Dynamics. So it took 109 tries. But once it did
*  it, it had a high percentage of success. So it's not like we're cheating by just showing the best
*  one, but we do show the evolved performance, not everything along the way. But everything along
*  the way is informative and it shows sort of, there's stupid things that go wrong, like the
*  robot just, when you say go and it collapses right there on the start, that doesn't have to
*  do with the steps or the perception didn't work right. So you miss the target when you jump or
*  something breaks and there's oil flying everywhere. But that's fun.
*  Yeah. So the hardware failures and then maybe some soft-
*  Lots of control of evolution during that time. I think it took six weeks to get those 109 trials,
*  because there was programming going on. It was actually robot learning, but there were human in
*  the loop helping with the learning. So all data driven. Okay. And you always are learning from
*  that failure. So- Right.
*  And how do you protect Atlas from not getting damaged from 109 attempts?
*  It's remarkable. One of the accomplishments of Atlas is that the engineers have made a machine
*  that's robust enough that it can take that kind of testing where it's falling and stuff, and it
*  doesn't break every time. It still breaks. And part of the paradigm is to have people to repair
*  stuff. You got to figure that in if you're going to do this kind of work. I sometimes criticize
*  the people who have their gold plated thing and they keep it on the shelf and they're afraid to
*  kind of use it. I don't think you can make progress if you're working that way. You need to be ready
*  to have it break and go in there and fix it. It's part of the thing. Plan your budget so you have
*  spare parts and a crew and all that stuff. Yeah. If it falls 109 times, it's okay. Wow.
*  Wow. So intrepid, truly. And that applies to Spot, that applies to all the other-
*  Applies to everything. I think it applies to everything anybody tries to do that's worth
*  doing. Yeah. And especially with systems in the real world, right? Yeah. And so fun.
*  Fun. Technical fun, I usually say. Have technical fun. I think that life as an engineer
*  is really satisfying. I think to some degree it can be like craft's work where you get to do
*  things with your own hands or your own design or whatever your media is. And it's very satisfying
*  to be able to just do the work, unlike a lot of people who have to do something that they don't
*  like doing. I think engineers typically get to do something that they like and there's a lot of
*  satisfaction from that. Then there's, in many cases, you can have impact on the world somehow
*  because you've done something that other people admire, which is different from the
*  craft fun of building a thing. So that's the second way that being an engineer is good.
*  I think the third thing is that if you're lucky to be working in a team where you're
*  getting the benefit of other people's skills that are helping you do your thing,
*  none of us has all the skills needed to do most of these projects. And if you have a team where
*  you're working well with the others, that can be very satisfying. And then if you're an engineer,
*  you also usually get paid. And so you kind of get paid four times in my view of the world.
*  So what could be better than that? Get paid to have fun. What do you love about engineering?
*  When you say engineering, what does that mean to you exactly? What is this kind of
*  big thing that we call engineering? I think it's both being a scientist or getting to use science
*  at the same time as being kind of an artist or a creator. Because scientists only get to
*  study what's out there and engineers get to make stuff that didn't exist before.
*  And so it's really, I think, a higher calling, even though I think most
*  the public out there think science is top and engineering is somehow secondary,
*  but I think it's the other way around. And at the cutting edge, I think when we talk about robotics,
*  there is a possibility to do art in that you do the first of its kind thing. So then there's the
*  production at scale, which is a so beautiful thing. But when you do the first new robot or
*  the first new thing, that's the possibility to create something totally new. That is art.
*  Bringing metal to life or a machine to life is kind of fun. And it was fun doing the dancing
*  videos where it got a huge public response. And we're going to do more. We're going to do
*  something. We're doing something at the Institute and we'll do more.
*  Well, that metal to life moment, I mean, to me, that's still magical. When inanimate objects
*  comes to life, that's still like to me, to this day is still an incredible moment. The human
*  intelligence can create systems that instill life or whatever that is into inanimate objects.
*  It's truly magical, especially when it's at the scale that humans can perceive and appreciate
*  directly. But I think sort of with it going back to the pieces of that,
*  you design a linkage that turns out to be half the weight and just as strong. That's very
*  satisfying. And there are people who do that and it's a creative act.
*  What to you is the most beautiful about robotics? Sorry for the big romantic question.
*  I think having the robots move in a way that's evocative of life is pretty exciting.
*  The elegance of movement.
*  Or if it's a high performance act where it's doing it faster, bigger than other robots. Usually,
*  we're not doing it bigger, faster than people, but we're getting there in a few narrow dimensions.
*  Faster, bigger, smoother, more elegant, more graceful.
*  I'd like to do dancing that starts. We're nowhere near the dancing capabilities of a human. We've
*  been having a ballerina in who's a well-known ballerina and she's been programming the robot.
*  We've been working on the tools that can make it so that she can use her way of talking,
*  way of doing a choreography or something like that more accessible
*  to get the robot to do things. And starting to produce some interesting stuff.
*  Well, we should mention that there is a choreography tool.
*  There is.
*  I guess I saw versions of it, which is pretty cool. You can at slices of time control different
*  parts at the high level, the movement of the robot.
*  We hope to take that forward and make it more tuned to how the dance world wants to talk,
*  wants to communicate, and get better performances. I mean, we've done a lot,
*  but there's still a lot possible. I'd like to have performances where the robots are dancing
*  with people. Right now, almost everything that we've done on dancing is to a fixed time base.
*  Once you press go, the robot does its thing and plays out its thing. It's not listening,
*  it's not watching, but I think it should do those things.
*  I think I would love to see a professional ballerina alone in a room with a robot,
*  slowly teaching the robot. Just actually the process of a clueless robot trying to figure out
*  a small little piece of a dance. Because right now, Atlas and Spot have done perfect dancing
*  to a beat and so on, to a degree. But the learning process of interacting with a human would be
*  incredible to watch. One of the cool things going on,
*  you know that there's a class at Brown University called Choreo Robotics.
*  Sidney Skybetter is a dancer, choreographer, and he teamed up with Stephanie Tellex,
*  who's a computer science professor. They taught this class, and I think they have some graduate
*  students helping teach it, where they have two spots. People come in, I think it's 50-50 of
*  computer science people and dance people. They program performances that are very interesting.
*  I show some of them sometimes when I give a talk.
*  And making that process of a human teaching the robot more efficient, more intuitive,
*  maybe language part movement. That'd be fascinating. That'd be really fascinating.
*  One of the things I've kind of realized is humans communicate with movement a lot. It's not just
*  language. There's body language. There's so many intricate little things.
*  Totally.
*  And like that, to watch a human and spot communicate back and forth with movement,
*  I mean, there's just so many wonderful possibilities there.
*  But it's also a challenge. We get asked to have our robots perform with famous dancers.
*  They have 200 degrees of freedom or something, right? Every little ripple and thing, and they
*  have all this head and neck and shoulders and stuff. And the robots mostly don't have all that
*  stuff. And it's a daunting challenge to not look stupid, physically stupid next to them.
*  We've pretty much avoided that kind of performance, but we'll get to it.
*  I think even with the limited degrees of freedom, we could still have some sass and
*  flavor and so on. You can figure out your own thing, even if you can't.
*  And we can reverse things. If you watch a human do robot animation, which is a dance style,
*  where you jerk around and you pop and pop and lock and all that stuff, I think the robots could
*  show up to the humans by doing unstable oscillations and things that are faster than
*  a person could. So that's on my plan, but we haven't quite gotten there yet.
*  You mentioned about building teams and robotics teams and so on. How do you find great engineers?
*  How do you hire great engineers? I think you even need to have an environment where
*  interesting engineers... Well, it's a chicken and egg. If you have an environment where interesting
*  engineering is going on, then engineers want to work there. And I think it took a long time to
*  develop that at Boston Dynamics. In fact, when we started, although I had the experience of building
*  things in the leg lab, both at CMU and at MIT, we weren't that sophisticated of an engineering
*  thing compared to what Boston Dynamics is now. But it was our ambition to do that.
*  And Sarcos was another robot company. So I always thought of us as being this much
*  on the computing side and this much on the hardware side. And they were like this.
*  Mm-hmm. And then over the years, I think we achieved the same or better levels of engineering.
*  Meanwhile, Sarcos got acquired and then they went through all kinds of changes. And
*  I don't know exactly what their current status is. So it took many years, is part of the answer.
*  I think you got to find people who love it. In the early days, we paid a little less,
*  so we only got people who were doing it because they really loved it. We also hired people who
*  might not have professional degrees, people who were building bicycles and building kayaks. We
*  have some people who come from that kind of the maker world. And that's really important
*  for the kind of work we do to have that be part of the mix.
*  Whatever that is, whatever the magic ingredient that makes a great builder, maker,
*  that's the big part of it. People who repaired the cars or
*  motorcycles or whatever in their garages when they were kids.
*  There's a kind of like the robotics students, grad students, and just roboticists that I know
*  and hang out with, there's a kind of endless energy. They're just happy. I compare it,
*  another group of people that are like that are people that skydive professionally.
*  There's just like excitement and general energy that I think probably has to do with the fact
*  that they're just constantly, first of all, fail a lot. And then the joy of building a thing that
*  you eventually works. Yeah, talking about being happy. There used to be a time when I was doing
*  the machine shop work myself back in those JPL and Caltech days, when if I came home smelling like
*  the machine shop, because it's an oily place, my wife would say, oh, you had a good day today.
*  You could tell that's where I've been. You've actually built something. You've
*  done something in the physical world. And probably the videos help, right? The videos
*  help show off what robotics is. At Boston Dynamics, it put us on the map.
*  I remember interviewing some sales guy and he was from a company and he said, well, no one's ever
*  heard of my company, but we have products, really good products. You guys, everybody knows who you
*  are, but you don't have any products at all, which was true. And we thank YouTube for that.
*  YouTube came, we caught the YouTube wave and it had a huge impact on our company.
*  It's a big impact on not just in your company, but on robotics in general, helping people
*  understand, inspire what is possible with robots. They inspire imagination, fear,
*  everything. The full spectrum of human emotion was aroused, which is great for the entirety of
*  humanity and also is probably inspiring for young people that want to get into AI and robotics.
*  Let me ask you about some competitors. You've been a complimentary of Elon and Tesla's work on
*  Optimus robot. What do you think of their efforts there with the humanoid robot?
*  I really admire Elon as a technologist. I think that what he did with Tesla, it was just totally
*  mind boggling that he could go from this totally niche area that less than 1% of anybody seemed
*  to be interested in making it so that essentially every car company in the world
*  is trying to do what he's done. You've got to give it to him. Then look at SpaceX.
*  He's basically replaced NASA. That might be a little exaggeration, but not by much.
*  You've got to admire the guy and I wouldn't count him out for anything. I don't think Optimus today
*  is where Atlas is, for instance. I don't know, it's a little hard to compare them to the other
*  companies. I visited Figure. I think they're doing well and they have a good team.
*  I've visited Eptronic and I think they have a good team and they're doing well.
*  But Elon has a lot of resources. He has a lot of ambition. I'd like to take some credit for his
*  ambition. I think if I read between the lines, it's hard not to think that him seeing what Atlas
*  is doing is a little bit of an inspiration. I hope so. Do you think Atlas and Optimus will
*  hang out at some point? I would love to host that. Now that I'm not at Boston Dynamics, I'm not
*  officially connected. I am on the board, but I'm not officially connected. I would love to host a
*  robot meetup. Does the AI Institute work with Spots and Atlas is it focused on Spots mostly
*  right now as a platform? We have a bunch of different robots. We bought everything we could
*  buy. We have Spots. I think we have a good size fleet of them. I don't know how many it is,
*  but a good size fleet. We have a couple of Animal robots. Animal is a company founded by Marco
*  Hunter, even though he's not that involved anymore. But we have a couple of those.
*  We have a bunch of arms like Frank's and US Robotics. Even though we have ambitions to build
*  stuff and we are starting to build stuff, day one getting off the ground, we just bought stuff.
*  I love this robot playground you've built. You can come over and take a look if you want.
*  That's great. It's like all these kinds of robots, legged, arms.
*  It doesn't feel that much like – well, there's some areas that feel like a playground,
*  but it's not like they're all frolicking together.
*  Hey, again, maybe you'll arrange a robot meetup. But in general, what's your view on competition
*  in this space, especially humanoid and legged robots? Are you excited by the competition or
*  the friendly competition? I don't think about competition that much.
*  I'm not a commercial guy. I think for many years at Boston Dynamics, we didn't think about
*  competition. We were just kind of doing our thing. It wasn't like there were products out there that
*  we were competing with. Maybe there was some competition for DARPA funding, which we got very
*  good at getting. But even there, in a couple of cases where we might have competed, we ended up
*  just being the robot provider. That is for the Little Dog program. We just made the robots. We
*  didn't participate as developers except for developing the robot. In the DARPA robotics
*  challenge, we didn't compete. We provided the robots. In the AI world now, now that we're
*  working on cognitive stuff, it feels much more like a competition. The entry requirements in
*  terms of computing hardware and the skills of the team and hiring talent, it's a much tougher
*  place. I think much more about competition now on the cognitive side. On the physical side,
*  it doesn't feel like it's that much about competition yet. Obviously, with 10 humanoid
*  companies out there, 10 or 12, there's probably others that I don't know about.
*  They're definitely in competition, will be in competition.
*  LW How much room is there for a quadruped and especially a humanoid robot to become cheaper?
*  Cutting costs and how low can you go? How much of it is just mass production? Questions of
*  Hyundai, how to produce versus engineering innovation, how to simplify?
*  DF I think there's a huge way to go. I don't think we've seen the bottom of it or the bottom
*  in terms of lower prices. I think you should be totally optimistic that at Asimtoad, things
*  don't have to be anything like as expensive as they are now. Back to competition, I wanted to say
*  one thing. I think in the quadruped space, having other people selling quadrupeds is a great thing
*  for Boston Dynamics because I believe the question in the user's minds is which quadruped do I want?
*  It's not, oh, do I want a quadruped? Can a quadruped do my job? It's much more like that,
*  which is a great place for it to be. Then you're just doing the things you normally do to make
*  your product better and compete and selling and all that stuff. That'll be the way it is with
*  humanoids at some point. LW Well, there's a lot of humanoids and you're just not even
*  it's like iPhone versus Android and people just buying both and it's just
*  you're not really- You're creating the category or the category is happening.
*  Right now, the use cases, that's the key thing. Having realistic use cases that are money-making
*  in robotics is a big challenge. There's the warehouse use case. That's probably the only
*  thing that makes anybody any money in robotics at this point. LW There's got to be a moment.
*  LW There's old fashioned robots. I mean, there's fixed arms doing manufacturing. I don't want to
*  say that they're not making money. LW Industrial robotics, yes, but there's got to be a moment
*  when social robotics starts making real money, meaning like a spa type robot in the home and
*  there's tens of millions of them in the home and they're like, I don't know how many dogs
*  there are in the United States as pets. LW Many.
*  LW Many. It feels like there's something we love about having an intelligent companion with us
*  that remembers us, that's excited to see us, all that kind of stuff.
*  LW But it's also true that the company's making those things. There've been a lot of failures
*  in recent times, right? There's that one year when I think three of them went under.
*  So it's not that easy to do that, right? Getting performance, safety,
*  and cost all to be where they need to be at the same time, that's hard.
*  LW But also some of it is, like you said, you can have a product, but people might not be aware of
*  it. Also part of it is the videos or however you connect with the public, the culture, and create
*  the category. Make people realize this is the thing you want. There's a lot of negative
*  perceptions you can have. Do you really want a system with a camera in your home walking around
*  right? If it's presented correctly and if there's like the right kind of boundaries around it that
*  you understand how it works and so on, that a lot of people would want to. And if they don't,
*  they might be suspicious of it. So that's important. Like we all use smartphones and that
*  has a camera that's looking at us. LW Yeah, it has two or three or four.
*  LW And it's listening. Very few people are
*  suspicious about it. They kind of take it for granted and so on. I think robots would be the
*  same kind of way. LW I agree.
*  LW So as you work on the cognitive aspect of these robots, do you think we'll ever
*  get to human level or superhuman level intelligence? There's been a lot of conversations
*  about this recently given the rapid development in large language models.
*  LW I think that intelligence is a lot of different things. And I think some things,
*  computers are already smarter than people and some things, they're not even close.
*  And I think you'd need a menu of detailed categories to come up with that. But I also
*  think that the conversation that seems to be happening about AGI puzzles me. I ask you a
*  question. Do you think there's anybody smarter than you in the world?
*  LW Absolutely, yes.
*  LW Do you find that threatening?
*  LW No.
*  LW So I don't understand even if computers were smarter than people, why we should assume that
*  that's a threat. Especially since they could easily be smarter but still available to us or
*  under our control, which is basically how computers generally are.
*  I think the fears that they would be 10x, 100x smarter and operating under different morals and
*  ethical codes than humans naturally do. And so almost become misaligned in unintended ways and
*  therefore harm humans in ways we just can't predict. And even if we program them to do a thing,
*  as on the way of doing that thing, they would cause a lot of harm. And when they're 100x,
*  1000x, 10,000x smarter than us, we won't be able to stop it or we won't be able to even see the
*  harm as it's happening until it's too late, that kind of stuff. So you can construct all kinds of
*  possible trajectories of how the world ends because of super-intelligent systems.
*  LW It's a little bit like that line in the Oppenheimer movie
*  where they contemplate whether the first time they set off a reaction, all matter on earth is
*  going to go up. I don't remember what the verb they used was for the chain reaction.
*  Yeah, I guess it's possible. I personally don't think it's worth worrying about that.
*  I think that it's balancing opportunities and risk. I think if you take any technology,
*  there's opportunity and risk. And it's easy to point at the car. They pollute and about 1.25
*  million people get killed every year around the world because of them. Despite that, I think
*  they're a boon to humankind, very useful. Many of us love them. And those technical problems
*  can be solved. I think they are becoming safer. I think they're becoming less polluting, at least
*  some of them are. And every technology you can name has a story like that, in my opinion.
*  LW What's the story behind the Hawaiian shirt? Is it a fashion statement, philosophical statement?
*  Is it just a statement of rebellion?
*  AC Engineering statement? LW It was born of me being a contrarian.
*  AC Yes. It's a symbol. LW Someone told me once that I was wearing one when I only had one or two.
*  They said, oh, those things are so old fashioned, you can't wear that mark. And I stopped wearing
*  them for about a week. And then I said, I'm not going to let them tell me what to do. And so,
*  every day since, pretty much. That was 20 years ago, 15 years ago, probably.
*  LW That says something about your personality. That's great.
*  AC It took me a while to realize I was a contrarian. But it can be a useful tool.
*  LW Have you had people tell you on the robotic side that, I don't think you could do this,
*  the kind of negative motivation? AC I'd rather talk about, there's a guy,
*  when we were doing a lot of DARPA work, there was a Marine, Ed Tovar, who's still around.
*  What he would always say is when someone would say, oh, you can't do that, he'd say, why not?
*  And it's a great question. I ask all the time when I'm thinking, oh,
*  we're not going to do that. And I say, why not? And I give him credit for opening my eyes to
*  resisting that. LW I love it. So, yeah, the Hawaiian shirt is almost like a symbol of why not.
*  Okay. What advice would you give to young folks that are trying to figure out what they want to
*  do with their life, how to have a life they can be proud of, how they can have a career they can be
*  proud of? AC When I was teaching at MIT, for a while, I had undergraduate advisees where people
*  would have to meet with me once a semester or something. And they frequently would ask what
*  they should do. And I think the advice I used to give was something like, well, if you had no
*  constraints on you, no resource constraints, no opportunity constraints, and no skill constraints,
*  could you imagine doing? And I said, well, start there and see how close you can get.
*  What's realistic for how close you can get? The other version of that is try and figure out what
*  you want to do and do that. Because I don't think a lot of people think that they're in a channel,
*  right? And there's only limited opportunities, but it's usually wider than they think.
*  LW Yeah, the opportunities really are limitless. But at the same time, you want to
*  pick a thing, right? And it's the diligence. And really, really pursue it, right? Really pursue it.
*  AC Yeah. LW Because sometimes, like, the really special stuff happens after years of pursuit.
*  AC Yeah. Oh, absolutely. It can take a while. LW I mean, you've been doing this for 40 plus years.
*  AC Some people think I'm in a rut, right? Why don't I do? And in fact, some of the inspiration for the
*  AI Institute is to say, okay, I've been working locomotion for however many years it was. Let's
*  do something else. And it's a really fascinating and interesting challenge. LW And you're hoping
*  to show it off also in the same way as we've done with Boston Dynamics. AC Just about to start
*  showing some stuff off, yeah. I hope we have a YouTube channel. I mean, one of the challenges
*  is it's one thing to show athletic skills on YouTube. Showing cognitive function is a lot
*  harder. And I haven't quite figured out yet how that's going to work. LW There might be a way.
*  AC There's a way. LW There's a way. AC Why not? LW I also do think
*  sucking at a task is also compelling. Like the incremental improvement, a robot being like really
*  terrible at a task and then slowly becoming better. Even in athletic intelligence, honestly,
*  learning to walk and falling and slowly figuring that out. I think there's something extremely
*  compelling about that. We like flaws, especially with the cognitive task. It's okay to be clumsy.
*  It's okay to be confused and a little silly and all that kind of stuff. It feels like in that space
*  is where we can- LW There's charm. AC There's charm. There's charm and there's something
*  inspiring about a robot sucking and then becoming less terrible slowly at a task. LW I think you're
*  right. AC That kind of reveals something about ourselves. Ultimately, that's what's one of the
*  coolest things about robots is it's kind of a mirror about what makes humans special. Just by
*  watching how hard it is to make a robot do the things that humans do, you realize how special we
*  are. What do you think is the meaning of this whole thing? Why are we here? Mark,
*  you ever ask about the big questions as you try to create these humanoid, human-like intelligence
*  systems? LW I don't know. I think you have to have fun while you're here. That's about all I know.
*  AC It would be a waste not to, right? LW The ride is pretty short, so might as well have fun.
*  Mark, I'm a huge fan of yours. It's a huge honor that you would talk with me. This is really amazing
*  and your work for many decades has been amazing. I can't wait to see what you do at the AI Institute.
*  I'm going to be waiting impatiently for the videos and the demos and the next robot meetup
*  for maybe Atlas and Optimus to hang out. LW I would love to do that. That would be fun.
*  AC Thank you so much for talking to me. LW Thank you. It was fun talking to you.
*  AC Thank you for listening and hope to see you next time.

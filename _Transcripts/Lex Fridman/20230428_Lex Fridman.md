---
Date Generated: April 09, 2024
Transcription Model: whisper medium 20231117
Length: 8878s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai', 'robert playter']
Video Views: 1047384
Video Rating: None
---

# Robert Playter: Boston Dynamics CEO on Humanoid and Legged Robotics | Lex Fridman Podcast #374
**Lex Fridman:** [April 28, 2023](https://www.youtube.com/watch?v=cLVdsZ3I5os)
*  And so our goal was a natural looking gate. It was really, it was surprisingly hard to get that to
*  work. And we, but we did build an early machine. We called it Petman prototype. It was the prototype
*  before the Petman robot. And it had a really nice looking gate where, you know, it would stick the
*  leg out. It would do heel strike first before it rolled onto the toe. So you didn't land with a
*  flat foot. You extended your leg a little bit. But even then it was hard to get the robot to walk
*  where when you're walking that it fully extended its leg. And getting that all to work well
*  took such a long time. In fact, I probably didn't really see the nice natural walking that I expected
*  out of our humanoids until maybe last year. And the team was developing on our newer generation
*  of Atlas, you know, some new techniques for developing a walking control algorithm. And
*  they got that natural looking motion as sort of a byproduct of a, of a, just a different process.
*  They were applying to developing the control. So that probably took 15 years, 10 to 15 years to
*  sort of get that from, from, you know, the Petman prototype was probably in 2008 and what was it?
*  2022 last year that I think I saw a good walking on Atlas.
*  The following is a conversation with Robert Plater, CEO of Boston Dynamics,
*  a legendary robotics company that over 30 years has created some of the most elegant, dexterous,
*  and simply amazing robots ever built, including the humanoid robot Atlas and the robot dog Spot.
*  One or both of whom you've probably seen on the internet either dancing, doing backflips,
*  opening doors, or throwing around heavy objects. Robert has led both the development of Boston
*  Dynamics humanoid robots and their physics-based simulation software. He has been with the company
*  from the very beginning, including its roots at MIT, where he received his PhD in aeronautical
*  engineering. This was in 1994 at the legendary MIT leg lab. He wrote his PhD thesis on robot
*  gymnastics as part of which he programmed a bipedal robot to do the world's first 3D robotic
*  somersault. Robert is a great engineer, roboticist, and leader and Boston Dynamics to me as a roboticist
*  is a truly inspiring company. This conversation was a big honor and pleasure, and I hope to do
*  a lot of great work with these robots in the years to come. This is the Lex Friedman podcast.
*  To support it, please check out our sponsors in the description. And now, dear friends,
*  here's Robert Plater. When did you first fall in love with robotics?
*  Let's start with love and robots. Well, love is relevant because I think the
*  fascination, the deep fascination is really about movement. And I was visiting MIT looking for a
*  place to get a PhD, and I wanted to do some laboratory work. And one of my professors in
*  the aerodepartment said, go see this guy, Mark Rabert, down in the basement of the AI lab.
*  And so I walked down there and saw him. He showed me his robots, and he showed me this robot doing
*  a somersault. And I just immediately went, whoa, you know, robots can do that. And because of my
*  own interest in gymnastics, there was like this immediate connection. And I was interested in,
*  I was in an aero-astro degree because flight and movement was all so fascinating to me.
*  And then it turned out that robotics had this big challenge. How do you balance? How do you build a
*  legged robot that can really get around? And that just, that was a fascination. And it still exists
*  today. You're still working on perfecting motion in robots. What about the elegance and the beauty
*  of the movement itself? Is there something maybe grounded in your appreciation of movement from
*  your gymnastics days? Did you, was there something you just fundamentally appreciate about the
*  elegance and beauty of movement? You know, we had this concept in gymnastics of letting your body
*  do what it wanted to do. When you get really good at gymnastics, part of what you're doing is putting
*  your body into a position where the physics and the body's inertia and momentum will kind of push
*  you in the right direction in a very natural and organic way. And the thing that Mark was doing,
*  in the basement of that laboratory, was trying to figure out how to build machines to take advantage
*  of those ideas. How do you build something so that the physics of the machine just kind of inherently
*  wants to do what it wants to do? And he was building these springy pogo stick type. His first cut at
*  legged locomotion was a pogo stick where it's bouncing and there's a spring mass system that's
*  oscillating, has its own sort of natural frequency there. And sort of figuring out how to augment
*  those natural physics with also intent, how do you then control that but not overpower it?
*  It's that coordination that I think creates real potential. We could call it beauty. You know,
*  you could call it, I don't know, synergy. People have different words for it. But I think that
*  that was inherent from the beginning. That was clear to me that that's part of what Mark was
*  trying to do. He asked me to do that in my research work. So, you know, that's where it got
*  going. So part of the thing that I think I'm calling elegance and beauty in this case,
*  which was there, even with the pogo stick, is maybe the efficiency. So letting the body do
*  what it wants to do, trying to discover the efficient movement. It's definitely more efficient.
*  It also becomes easier to control in its own way because the physics are solving some of the
*  problem itself. It's not like you have to do all this calculation and overpower the physics. The
*  physics naturally inherently want to do the right thing. There can even be, you know, feedback
*  mechanisms, stabilizing mechanisms that occur simply by virtue of the physics of the body. And
*  it's not all in the computer or not even all in your mind as a person. And there's something
*  interesting in that melding. You were with Mark for many, many, many years, but you were there in
*  this kind of legendary space of leg lab at MIT in the basement. All great things happen in the
*  basement. Is there some memories from that time that you have? Because it's such cutting edge
*  work in robotics and artificial intelligence. The memories, the distinctive lessons I would say,
*  I learned in that time period and that I think Mark was a great teacher of,
*  was it's okay to pursue your interests, your curiosity, do something because you love it.
*  You'll do it a lot better if you love it. That is a lasting lesson that I think we apply at the
*  company still and really is a core value. So the interesting thing is I got to,
*  with people like Russ Dedrick and others, like the students that work at those robotics labs
*  are like some of the happiest people I've ever met. I don't know what that is. I meet a lot of
*  PhD students. A lot of them are kind of broken by the wear and tear of the process. But roboticists
*  are, while they work extremely hard and work long hours, there's a happiness there. The only other
*  group of people I've met like that are people that skydive a lot. For some reason there's a deep
*  fulfilling happiness, maybe from a long period of struggle to get a thing to work and it works and
*  there's a magic to it. I don't know exactly because it's so fundamentally hands-on and you're
*  bringing a thing to life. I don't know what it is, but they're happy.
*  We see our attrition at the company is really low. People come and they love the pursuit.
*  And I think part of that is that there's perhaps an actual connection to it. It's a little bit
*  easier to connect when you have a robot that's moving around in the world. And part of your goal
*  is to make it move around in the world. You can identify with that. And this is one of the unique
*  things about the kinds of robots we're building is this physical interaction lets you perhaps
*  identify with it. So I think that is a source of happiness. I don't think it's unique to robotics.
*  I think anybody also who is just pursuing something they love, it's easier to work hard at it and be
*  good at it. And not everybody gets to find that. I do feel lucky in that way. And I think we're
*  lucky as an organization that we've been able to build a business around this and that keeps
*  people engaged. So if it's all right, let's linger on Mark for a little bit longer. Mark Kraybert.
*  He's a legendary engineer and roboticist. What have you learned about life about robotics from
*  Mark through all the many years you worked with him? I think the most important lesson,
*  which was have the courage of your convictions and do what you think is interesting.
*  Be willing to try to find big, big problems to go after. And at the time, like at locomotion,
*  especially in a dynamic machine, nobody had solved it. And that felt like a multi-decade
*  problem to go after. And so have the courage to go after that because you're interested.
*  Don't worry if it's going to make money. That's been a theme. So that's really probably the most
*  important lesson I think that I got from Mark. How crazy is the effort of doing
*  legged robotics at that time especially? Mark got some stuff to work starting from the simple ideas.
*  So maybe the other, another important idea that has really become a value of the company is try
*  to simplify a thing to the core essence. And while Mark was showing videos of animals running across
*  the savanna or climbing mountains, what he started with was a pogo stick because he was trying to
*  reduce the problem to something that was manageable and getting the pogo stick to balance. Had in it
*  the fundamental problems that if we solve those, you could eventually extrapolate
*  to something that galloped like a horse. And so look for those simplifying principles.
*  How tough is the job of simplifying a robot? So I'd say in the early days, the thing that made
*  Boston, the researchers at Boston Dynamics special is that we worked on figuring out what that
*  that central principle was and then building software or machines around that principle.
*  And that was not easy in the early days. And it took real expertise in understanding the dynamics
*  of motion and feedback control principles. How to build and with the computers at the time,
*  how to build a feedback control algorithm that was simple enough that it could run in real time
*  at 1000 hertz and actually get that machine to work. And that was not something everybody was
*  doing at that time. Now the world's changing now. I think the approaches to controlling robots are
*  going to change. And they're going to become more broadly available. But at the time, there weren't
*  many groups who could really sort of work at that principled level with both the software and
*  make the hardware work. And I'll say one other thing about you were sort of
*  talking about what are the special things. The other thing was it's good to break stuff.
*  Use the robots, break them, repair them, fix and repeat, test, fix and repeat. And that's
*  also a core principle that has become part of the company. And it lets you be fearless in your work.
*  Too often if you are working with a very expensive robot, maybe one that you bought from somebody
*  else or that you don't know how to fix, then you treat it with kit gloves and you can't actually
*  make progress. You have to be able to break something. And so I think that's been a principle as
*  well. So just to linger on that psychologically, how do you deal with that? Because I remember I had
*  built a RC car with that some, it had some custom stuff like compute on it, all that kind of stuff,
*  cameras. And because I didn't sleep much, the code I wrote had an issue where it didn't stop the car
*  and the car got confused and at full speed at like 20, 25 miles an hour slammed into a wall.
*  And I just remember sitting there alone in a deep sadness, sort of full of regret, I think, almost
*  anger, but also like sadness because you think about, well, these robots, especially for autonomous
*  vehicles, like you should be taking safety very seriously even in these kinds of things. But just
*  no good feelings. It made me more afraid probably to do this kind of experiments in the future.
*  Perhaps the right way to have seen that is positively.
*  It depends if you could have built that car or just gotten another one, right? That would have
*  been the approach. I remember when I got to grad school, I got some training about operating a lathe
*  and a mill up in the machine shop and I could start to make my own parts. And I remember
*  breaking some piece of equipment in the lab and then realizing, because maybe this was a unique
*  part and I couldn't go buy it. And I realized, oh, I can just go make it. That was an enabling
*  feeling. Then you're not afraid. It might take time. It might take more work than you thought
*  it was going to be required to get this thing done, but you can just go make it.
*  And that's freeing in a way that nothing else is.
*  You mentioned the feedback control, the dynamics. Sorry for the romantic question, but
*  in the early days and even now, is the dynamics probably more appropriate for the early days?
*  Is it more art or science?
*  There's a lot of science around it and trying to develop scientific principles that let you
*  extrapolate from one-legged machine to another. Develop a core set of principles like a spring
*  mass bouncing system and then figure out how to apply that from a one-legged machine to a two or a
*  four-legged machine. Those principles are really important and we're definitely a core science
*  Those principles are really important and we're definitely a core part of our work.
*  There's also, when we started to pursue humanoid robots, there was so much complexity in that
*  machine that one of the benefits of the humanoid form is you have some intuition about how it
*  should look while it's moving. And that's a little bit of an art, I think. Or maybe
*  it's just tapping into a knowledge that you have deep in your body and then trying to express that
*  in the machine. But that's an intuition that's a little bit more on the art side. Maybe it predates
*  your knowledge. Before you have the knowledge of how to control it, you try to work through the art
*  channel. And humanoids make that available to you. If it had been a different shape, maybe you
*  wouldn't have had the same intuition about it. Yeah, so your knowledge about moving through the
*  world is not made explicit to you. So that's why it's art. Yeah, it might be hard to actually
*  articulate exactly. There's something about, and being a competitive athlete, there's something about
*  seeing a movement. A coach, one of the greatest strengths a coach has is being able to see
*  some little change in what the athlete is doing and then being able to articulate that to the
*  athlete. And then maybe even trying to say, and you should try to feel this.
*  So there's something just in seeing. And again, sometimes it's hard to articulate what it is you're
*  seeing. But there's just perceiving the motion at a rate that is, again, sometimes hard to put into
*  words. Yeah, I wonder how it is possible to achieve sort of truly elegant movement. You have a movie
*  Ex Machina, I'm not sure if you've seen it. But the main actress in that who plays the AI robot,
*  I think is a ballerina. I mean, just the natural elegance and the, I don't know, eloquence of
*  movement. It looks efficient and easy and just, it looks right. It looks beautiful. It looks right is
*  sort of the key. And then you look at especially early robots. I mean, they're so cautious in the
*  way they move that it's not the caution that looks wrong. It's something about the movement
*  that looks wrong that feels like it's very inefficient, unnecessarily so. And it's hard to
*  put that into words exactly. We think that part of the reason why people are attracted to the
*  machines we build is because the inherent dynamics of movement are closer to right.
*  Because we try to use, you know, walking gates, or we build a machine around this gate,
*  where you're trying to work with the dynamics of the machine instead of to stop them.
*  Some of the early walking machines, you know, you're essentially, you're really trying hard
*  to not let them fall over. And so you're always stopping the tipping motion, you know.
*  And sort of the insight of dynamic stability in a lighted machine is to go with it, you know,
*  let the tipping happen, you know, let yourself fall, but then catch yourself with that next foot.
*  And there's something about getting those physics to be expressed in the machine
*  that people interpret as lifelike, or elegant, or just natural looking. And so I think if you
*  get the physics right, it also ends up being more efficient, likely. There's a benefit that
*  it probably ends up being more stable in the long run. You know, it could walk stably over a wider
*  range of conditions. And it's more beautiful and attractive at the same time.
*  So how hard is it to get the humanoid robot Atlas to do some of the things it's recently been doing?
*  Let's forget the flips and all of that. Let's just look at the running. Maybe you can correct me,
*  but there's something about running, I mean, that's not careful at all, that's you're falling forward.
*  You're jumping forward and are falling. So how hard is it to get that right?
*  Our first humanoid, we needed to deliver natural looking walking. You know, we took a contract
*  from the army, they wanted a robot that could walk naturally, they wanted to put a suit on the robot
*  and be able to test it in a gas environment. And so they wanted the motion to be natural.
*  And so our goal was a natural looking gate. It was really, it was surprisingly hard to get that to
*  work. But we did build an early machine. We called it Petman prototype. It was the prototype
*  before the Petman robot. And it had a really nice looking gate where, you know, it would stick the
*  leg out, it would do heel strike first before it rolled onto the toe. So you didn't land with a
*  flat foot, you extended your leg a little bit. But even then it was hard to get the robot to walk
*  when you're walking that it fully extended its leg and essentially landed on an extended leg.
*  And if you watch closely how you walk, you probably land on an extended leg,
*  but then you immediately flex your knee as you start to make that contact.
*  And getting that all to work well took such a long time. In fact, I probably didn't really see
*  the nice natural walking that I expected out of our humanoids until maybe last year. And the team
*  was developing on our newer generation of Atlas, you know, some new techniques
*  for developing a walking control algorithm. And they got that natural looking motion
*  as sort of a byproduct of a just a different process they were applying to developing the control.
*  So that probably took 15 years, 10 to 15 years to sort of get that from, you know,
*  the Petman prototype was probably in 2008. And what was it? 2022. Last year that I think I saw
*  a good walking on Atlas. If you could just like linger on it, what are some challenges of getting
*  good walking? So is it is this is this partially like a hardware like actuator problem? Is it the
*  control? Is it the artistic element of just observing the whole system operating in different
*  conditions together? I mean, is there some kind of interesting
*  quirks or challenges you can speak to like the heel strike?
*  Yeah. So one of the things that makes the like this straight leg a challenge is you're sort of
*  up against a singularity, a mathematical singularity, where, you know, when your leg is fully extended,
*  it can't go further the other direction, right? There's only you can only move in one direction.
*  And that makes all of the calculations around how to produce
*  torques at that joint or positions makes it more complicated. And so having all of the mathematics
*  so it can deal with these singular configurations is one of many challenges that we face. And I'd
*  say in the in those earlier days, again, we were working with these really simplified models.
*  So we're trying to boil all the physics of the complex human body into a simpler subsystem that
*  we can more easily describe in mathematics. And sometimes those simpler subsystems don't have
*  all of that complexity of the straight leg built into them. And so what's happened more recently
*  is we're able to apply techniques that let us take the full physics of the robot into account
*  and deal with some of those strange situations like this, like the straight leg.
*  So is there a fundamental challenge here that it's maybe you can correct me,
*  but is it under actuated? Are you falling? Under actuated is the right word, right? You can't
*  push the robot in any direction you want to. Right. And so that is one of the
*  hard problems of like locomotion. And you have to do that for natural movement.
*  It's not necessarily required for natural movement. It's just required.
*  You know, we don't have a gravity force that you can hook yourself onto to apply an external
*  force in the direction you want at all times. Right. The only external forces are being mediated
*  through your feet and how they get mediated depend on how you place your feet. And you know,
*  God's hand can't reach down and push in any direction you want.
*  You know, so is there, is there some extra challenge to the fact that Alice is such a big
*  robot? There is the humanoid form is attractive in many ways, but it's also a challenge in many ways.
*  You have this big upper body that has a lot of mass and inertia
*  and throwing that inertia around increases the complexity of maintaining balance.
*  And as soon as you pick up something heavy in your arms, you've made that problem even harder.
*  And so in the early work in the leg lab and in the early days at the company,
*  we were pursuing these quadruped robots, which had a kind of built in simplification. You had
*  this big rigid body and then really light legs. So when you swing the legs, the leg motion didn't
*  impact the body motion very much. All the mass and inertia was in the body.
*  But when you have the humanoid, that doesn't work. You have big, heavy legs,
*  you swing the legs, it affects everything else. And so dealing with all of that interaction
*  does make the humanoid a much more complicated platform.
*  And I also saw that at least recently you've been doing more explicit modeling of the stuff you pick
*  up. Which is very, really interesting. So you have to model the shape, the weight distribution.
*  I don't know. You have to include that as part of the modeling, as part of the planning.
*  So for people who don't know, Atlas, at least in a recent video, throws a heavy bag,
*  throws a bunch of stuff. So what's involved in picking up a heavy thing,
*  and when that thing is a bunch of different non-standard things, I think it also picked
*  up like a barbell. And to be able to throw it in some cases, what are some interesting challenges there?
*  So we were definitely trying to show that the robot and the techniques we're applying to Atlas
*  let us deal with heavy things in the world. Because if the robot's going to be useful,
*  it's actually got to move stuff around. And that needs to be significant stuff. That's an
*  appreciable portion of the body weight of the robot. And we also think this differentiates us
*  from the other humanoid robot activities that you're seeing out there. Mostly they're not picking
*  stuff up yet. And not heavy stuff anyway. But just like you or me, you need to anticipate that
*  moment. You're reaching out to pick something up, and as soon as you pick it up, your center of mass
*  is going to shift. And if you're going to turn in a circle, you have to take that inertia into
*  count. And if you're going to throw a thing, all of that has to be included in the model of what
*  you're trying to do. So the robot needs to have some idea or expectation of what that weight is,
*  and then sort of predict. Think a couple of seconds ahead. How do I manage now my body plus
*  this big heavy thing together? And still maintain balance. And so that's a big change for us. And I
*  think the tools we've built are really allowing that to happen quickly now. Some of those motions
*  that you saw in that most recent video, we were able to create in a matter of days. It used to be
*  that it took six months to do anything new on the robot. And now we're starting to develop the tools
*  that let us do that in a matter of days. And so we think that's really exciting. That means that
*  the ability to create new behaviors for the robot is going to be a quicker process.
*  So being able to explicitly model new things that it might need to pick up, new types of things.
*  And to some degree, you don't want to have to pay too much attention to each specific thing.
*  There's sort of a generalization here. Obviously, when you grab a thing, you have to conform your
*  hand, your end effector, to the surface of that shape. But once it's in your hands,
*  it's probably just the mass and inertia that matter. And the shape may not be as important.
*  And so in some ways, you want to pay attention to that detailed shape. In others, you want to
*  generalize it and say, well, all I really care about is the center of mass of this thing,
*  especially if I'm going to throw it up on that scaffolding. And it's easier if the body is rigid.
*  What if there's some... Doesn't it throw like a sandbag type thing? That tool bag had loose stuff
*  in it. So it managed that. There are harder things that we haven't done yet. We could have
*  had a big jointed thing or a bunch of loose wire or rope. What about carrying another robot? How
*  about that? Yeah, we haven't done that yet. I guess we did a little skit around Christmas where we
*  had two spots holding up another spot that was trying to put a bow on a tree. So I guess we're
*  doing that in a small way. Okay, that's pretty good. Let me ask the all important question.
*  Do you know how much Atlas can curl? For us humans, that's really one of the most fundamental
*  questions you can ask another human being. Curl? Bench? It probably can't curl as much as we can
*  yet. But a metric that I think is interesting is another way of looking at that strength
*  is the box jump. So how high of a box can you jump onto? Atlas, I don't know the exact height. It was
*  probably a meter high or something like that. It was a pretty tall jump that Atlas was able to manage
*  when we last tried to do this. I have video of my chief technical officer doing the same jump. He
*  really struggled. Oh, the human. The human getting all the way on top of this box. But then Atlas
*  was able to do it. We're now thinking about the next generation of Atlas. And we're probably going
*  to be in the realm of a person can't do it with the next generation. The robots, the actuators
*  are going to get stronger. Where it really is the case that at least some of these joints, some of
*  these motions will be stronger. And to understand how high it can jump, you probably had to do quite
*  a bit of testing. Oh, yeah. And there's lots of videos of it trying and failing. And that's
*  all. We don't always release those videos, but they're a lot of fun to look at.
*  So we'll talk a little bit about that. But if you can talk to the jumping,
*  because you talked about the walking, it took a long time, many, many years to get the walking
*  to be natural. But there's also really natural looking, robust, resilient jumping. How hard is
*  it to do the jumping? Well, again, this stuff has really evolved rapidly in the last few years.
*  The first time we did a somersault, there was a lot of manual iteration. What is the trajectory?
*  How hard do you throw it? In fact, in these early days, I actually would, when I'd see
*  early experiments that the team was doing, I might make suggestions about how to change the
*  technique. Again, kind of borrowing from my own intuition about how backflips work.
*  But frankly, they don't need that anymore. So in the early days, you had to iterate
*  kind of in almost a manual way, trying to change these trajectories of the arms or the legs
*  to try to get a successful backflip to happen. But more recently, we're running these model
*  predictive control techniques where we're able to, the robot essentially can think in advance
*  for the next second or two about how its motion is going to transpire. And you can solve for
*  optimal trajectories to get from A to B. So this is happening in a much more natural way.
*  And we're really seeing an acceleration happen in the development of these behaviors, again,
*  partly due to these optimization techniques, sometimes learning techniques. So it's hard in
*  that there's a lot of mathematics behind it, but we're figuring that out. So you can do model
*  predictive control for, I mean, I don't even understand what that looks like when the entire
*  robot is in the air, flying and doing a backflip. But that's the cool part, right? So the physics,
*  we can calculate physics pretty well using Newton's laws about how it's going to evolve over time.
*  The sick trick, which was a front somersault with a half twist is a good example, right?
*  You saw the robot on various versions of that trick, I've seen it land in different configurations
*  and it still manages to stabilize itself. And so what this model predictive control means is,
*  again, in real time, the robot is projecting ahead a second into the future and sort of
*  exploring options. And if I move my arm a little bit more this way, how is that going to affect
*  the outcome? And so it can do these calculations, many of them, and basically solve for, given where
*  I am now, maybe I took off a little bit screwy from how I had planned, I can adjust. So you're
*  adjusting in the air? Just on the fly. So the model predictive control lets you adjust on the fly.
*  And of course, I think this is what people adapt as well. When we do it, even a gymnastics trick,
*  we try to set it up so it's close to the same every time. But we figured out how to do some
*  adjustment on the fly. And now we're starting to figure out that the robots can do this adjustment
*  on the fly as well, using these techniques. In the air. It just feels, from a robotics perspective,
*  just surreal. Well, that's sort of the idea you talked about under actuated, right? So when
*  you're in the air, there's some things you can't change, right? You can't change the momentum
*  while it's in the air, because you can't apply an external force or torque. And so the momentum
*  isn't going to change. So how do you work within the constraint of that fixed momentum to still
*  get from A to B where you want to be? That's really underactuated. You're in the air. I mean,
*  you become a drone for a brief moment in time. No, you're not even a drone because you can't
*  hover. You're going to impact soon. Be ready. Are you considered like a hover type thing?
*  It's too much weight. I mean, it's just incredible. And just even to have the guts to try backflip
*  with such a large body. That's wild. But like, how we definitely broke a few robots trying.
*  But that's where the build it, break it, fix it, you know, strategy comes in and got to be willing
*  to break. And what ends up happening is you end up by breaking the robot repeatedly, you find the
*  weak points, and then you end up redesigning it so it doesn't break so easily next time.
*  Through the breaking process, you learn a lot, like a lot of lessons and you keep improving,
*  not just how to make the backflip work, but everything. And how to build a machine better.
*  Yeah. Yeah. I mean, is there something about just the guts that
*  come up with an idea of saying, you know what, let's try to make it to a backflip?
*  Well, I think the courage to do a backflip in the first place and to not worry too much about the
*  ridicule of somebody saying, why the heck are you doing backflips with robots? Because a lot of
*  people have asked that, you know, why, why are you doing this? Why go to the moon in this decade
*  and do the other things JFK? Not because it's easy, because it's hard. Yeah, exactly.
*  Don't ask questions. Okay, so the jumping, I mean, it's just, there's a lot of incredible stuff. If
*  we can just rewind a little bit to the DARPA robotics challenge in 2015, I think, which was
*  for people who are familiar with the DARPA challenges, it was first with autonomous
*  vehicles and there's a lot of interesting challenges around that. And the DARPA robotics
*  challenges when humanoid robots were tasked to do all kinds of, you know, manipulation, walking,
*  driving, driving a car, all these kinds of challenges with, if I remember correctly,
*  sort of some slight capability to communicate with humans, but the communication was very poor.
*  So it basically has to be almost entirely autonomous. It could have periods where the
*  communication was entirely interrupted and the robot had to be able to proceed. Yeah. But you
*  could provide some high level guidance to the robot, basically load low bandwidth communications.
*  Yeah. I watched that challenge with kind of tears in my eyes eating popcorn.
*  But I wasn't personally losing, you know, hundreds of thousands, millions of dollars
*  and many years of incredible hard work by some of the most brilliant roboticists in the world.
*  So that was why the tragic, that's why the tears came. So anyway, what have you,
*  just looking back to that time, what have you learned from that experience?
*  Maybe if you could describe what it was, sort of the set up for people who haven't seen it.
*  Well, so there was a contest where a bunch of different robots were asked to do a series of
*  tasks. Some of those that you mentioned, drive a vehicle, get out, open a door, go identify a valve,
*  shut a valve, use a tool to maybe cut a hole in a surface and then crawl over some stairs and maybe
*  some rough terrain. So it was, the idea was have a general purpose robot that could do lots of
*  different things. Had to be mobility and manipulation on board perception. And there was a contest,
*  which DARPA likes at the time was running sort of follow on to the grand challenge, which was,
*  let's try to push vehicle autonomy along, right? They encourage people to build autonomous cars.
*  So they're trying to basically push an industry forward. And we were asked, our role in this was
*  to build a humanoid at the time it was our sort of first generation Atlas robot. And we built
*  maybe 10 of them. I don't remember the exact number. And DARPA distributed those to various
*  teams that sort of won a contest, showed that they could program these robots and then use them to
*  compete against each other. And then other robots were introduced as well. Some teams built their
*  own robots. Carnegie Mellon, for example, built their own robot. And all these robots competed
*  to see who could sort of get through this maze of the fastest. And again, I think the purpose was
*  to kind of push the whole industry forward. We provided the robot and some baseline software,
*  but we didn't actually compete as a participant where we were trying to drive the robot through
*  this maze. We were just trying to support the other teams. It was humbling because it was really
*  a hard task. And honestly, the tears were because mostly the robots didn't do it. They fell down
*  repeatedly. It was hard to get through this contest. Some did, and they were rewarded and won.
*  But it was humbling because of just how hard. These tasks weren't all that hard. A person could
*  have done it very easily. But it was really hard to get the robots to do it.
*  You know, the general nature of it, the variety of it, the variety. And also that I don't know
*  if the tasks were sort of the task in themselves, help us understand what is difficult, what is not.
*  I don't know if that was obvious before the contest was designed. So you kind of try to figure that
*  out. And I think Atlas is really a general robot platform. And it's perhaps not best suited for
*  the specific tasks of that contest. For example, probably the hardest task is not the driving of
*  the car, but getting in and out of the car. And Atlas probably, if you were to design a robot that
*  can get into the car easily and get out easily, you probably would not make Atlas that particular
*  car. Yeah, the robot was a little bit big to get in and out of that car. Right. It doesn't fit.
*  This is the curse of a general purpose robot, that they're not perfect at any one thing,
*  but they might be able to do a wide variety of things. And that is the goal at the end of the
*  day. You know, I think we all want to build general purpose robots that can be used for lots of
*  different activities, but it's hard. And the wisdom in building successful robots up until this point
*  have been go build a robot for a specific task and it'll do it very well. And as long as you
*  control that environment, it'll operate perfectly. But robots need to be able to deal with uncertainty.
*  If they're going to be useful to us in the future, they need to be able to deal with unexpected
*  situations. And that's sort of the goal of a general purpose or multi-purpose robot.
*  And that's just darn hard. And so some of the others, these curious little failures,
*  I remember one of the, a robot, the first time you start to try to push on the world with a robot,
*  you forget that the world pushes back and will push you over if you're not ready for it. And the
*  robot reached to grab the door handle. I think it missed the grasp of the door handle, was expecting
*  that its hand was on the door handle. And so when it tried to turn the knob, it just threw itself
*  over. It didn't realize, oh, I had missed the door handle. I didn't have, I didn't, I was expecting
*  a force back from the door. It wasn't there. And then I lost my balance. So these little simple
*  things that you and I would take totally for granted and deal with the robots don't know how
*  to deal with yet. And so you have to start to deal with all of those circumstances.
*  Well, I think a lot of us experienced this in, even when sober, but drunk too,
*  sort of you pick up a thing and expect it to be, what is it, heavy. And it turns out to be light.
*  Oh yeah. And then, so the same, and I'm sure if your depth perception for whatever reason is
*  screwed up, if you're, if you're drunk or some other reason, and then you think you're putting
*  your hand on the table and you miss it. I mean, it's the same kind of situation,
*  but there's a- Which is why you need to be able to predict forward just a little bit.
*  And so that's where this model predictive control stuff comes in. Predict forward what you think's
*  going to happen. And then if, and if that does happen, you're in good shape. If something else
*  happens, you better start predicting again. So re, like re regenerate a plan. Yeah. When you
*  don't, I mean that, that also requires a very fast feedback loop of updating
*  what your prediction, how it matches to the actual real world.
*  Yeah. Those things have to run pretty quickly. What's the challenge of running things pretty
*  quickly? A thousand Hertz of acting and sensing quickly. You know, there's a few different layers
*  of that. You want at the lowest level, you like to run things typically at around a thousand Hertz,
*  which means that, you know, at each joint of the robot, you're measuring position or force,
*  and then trying to control your actuator, whether it's a hydraulic or electric motor,
*  trying to control the force coming out of that actuator. And you want to do that really fast,
*  something like a thousand Hertz. And that means you can't have too much calculation going on at
*  that joint. But that's pretty manageable these days and it's fairly common.
*  And then there's another layer that you're probably calculating, you know, maybe at a
*  hundred Hertz, maybe 10 times slower, which is now starting to look at the overall body motion
*  and thinking about the larger physics of the robot. And then there's yet another loop that's
*  probably happening a little bit slower, which is where you start to bring, you know, your perception
*  and your vision and things like that. And so you need to run all of these loops sort of simultaneously.
*  You do have to manage your computer time so that you can squeeze in all the calculations you need
*  in real time in a very consistent way. And the amount of calculation we can do
*  is increasing as computers get better, which means we can start to do more sophisticated
*  calculations. I can have a more complex model doing my forward prediction and that might allow
*  me to do even better predictions as I get better and better. And it used to be, again, we had,
*  you know, 10 years ago, we had to have pretty simple models that we were running, you know,
*  at those fast rates because the computers weren't as capable about calculating forward with a
*  sophisticated model. But as computation gets better, we can do more of that.
*  What about the actual pipeline of software engineering? How easy it is to keep updating
*  Atlas, like do continuous development on it. So how many computers are on there? Is there a nice
*  pipeline? It's an important part of building a team around it, which means, you know,
*  you need to also have software tools, simulation tools, you know, so we have always made strong
*  use of physics-based simulation tools to do some of this calculation, basically test it in simulation
*  before you put it on the robot. But you also want the same code that you're running in simulation to
*  be the same code you're running on the hardware. And so even getting to the point where it was the
*  same code going from one to the other, we probably didn't really get that working until, you know,
*  a few years, several years ago. But that was a, you know, that was a bit of a milestone. And so
*  you want to work, certainly work these pipelines so that you can make it as easy as possible and
*  have a bunch of people working in parallel, especially when you know, we only have, you know,
*  four of the Atlas robots, the modern Atlas robots at the company. And, you know, we probably have,
*  you know, 40 developers, they're all trying to gain access to it. And so you need to share
*  resources and use some of these, some of the software pipeline. Well, that's a really exciting
*  step to be able to run the exact same code and simulation as on the actual robot. How hard is it
*  to do realistic simulation, physics-based simulation of Atlas such that, I mean, the dream is like,
*  if it works in simulation, it works perfectly in reality. How hard is it to sort of keep working
*  on closing that gap? The root of some of our physics-based simulation tools really started
*  at MIT. And we built some good physics-based modeling tools there. The early days of the
*  company, we were trying to develop those tools as a commercial product. So we continued to develop
*  them. It wasn't a particularly successful commercial product, but we ended up with some nice
*  physics-based simulation tools so that when we started doing legged robotics again, we had a
*  really nice tool to work with. And the things we paid attention to were things that weren't
*  necessarily handled very well in the commercial tools you could buy off the shelf, like interaction
*  with the world, like foot-ground contact. So trying to model those contact events well in a way that
*  captured the important parts of the interaction was a really important element to get right.
*  And to also do in a way that was computationally feasible and could run fast. Because if your
*  simulation runs too slow, then your developers are sitting around waiting for stuff to run and
*  compile. So it's always about efficient, fast operation as well. So that's been a big part of
*  I think developing those tools in parallel to the development of the platform and trying to scale
*  them has really been essential, I'd say, to us being able to assemble a team of people that could
*  do this. Yeah, how to simulate contact periods, so foot-ground contact but sort of for manipulation.
*  Because don't you want to model all kinds of surfaces? Yeah. So it will be even more
*  complex with manipulation because there's a lot more going on, you know, and you need to capture,
*  I don't know, things slipping and moving in your hand. It's a level of complexity that I think
*  goes above foot-ground contact when you really start doing dexterous manipulation. So there's
*  challenges ahead still. So how far are we away from me being able to walk with Atlas in the sand
*  along the beach and us both drinking a beer? Maybe Atlas could spill his beer because he's
*  got nowhere to put it. Atlas could walk on the sand. So can it? Yeah. I mean, you know,
*  have we really had him out on the beach? You know, we take them outside often, you know, rocks,
*  hills, that sort of thing, even just around our lab in Waltham. We probably haven't been on the
*  sand. But I don't doubt that we could deal with it. We might have to spend a little bit of time
*  to sort of make that work. But we did take, we had to take Big Dog to Thailand years ago.
*  And we did this great video of the robot walking in the sand, walking into the ocean
*  up to, I don't know, its belly or something like that, and then turning around and walking out,
*  all walk playing some cool beach music. Great show. But then, you know, we didn't really clean
*  the robot off and the salt water was really hard on it. So we put it in a box, shipped it back.
*  By the time it came back, we had some problems with it. It's a salt water. It's not like
*  sand getting into the components or something like this. But I'm sure if this is a big priority,
*  you can make it waterproof. That just wasn't our goal at the time. Well, it's a personal goal.
*  Walk along the beach. But it's a human problem too. You get sand everywhere. It's just a jam
*  mess. So soft surfaces are okay. So, I mean, can we just linger on the robotics challenge? There's a
*  pile of like rubble there to walk over. How difficult is that task?
*  In the early days of developing Big Dog, the loose rock was the epitome of the hard walking
*  surface because you step down and then the rock and you had these little point feet on the robot
*  and the rock can roll. And you have to deal with that last minute change in your foot placement.
*  Yeah. So you step on a thing and that thing responds to you stepping on it.
*  Yeah. And it moves where your point of support is. And so it's really that became kind of the
*  essence of the test. And so that was the beginning of us starting to build rock piles in our
*  parking lots. And we would actually build boxes full of rocks and bring them into the lab.
*  And then we would have the robots walking across these boxes of rocks because that became
*  the essential test. So you mentioned Big Dog. Can we maybe take a stroll through the history
*  of Boss of Dynamics? So what and who is Big Dog? By the way, is who do you try not to anthropomorphize
*  the robots? Do you try to remember that they're... This is like the division I have because for me,
*  it's impossible. For me, there's a magic to the being that is a robot. It is not human, but it is
*  the same magic that a living being has when it moves about the world is there in the robot. So
*  I don't know what question I'm asking, but should I say what or who, I guess?
*  Who is Big Dog? What is Big Dog? Well, I'll say to address the medic question,
*  we don't try to draw hard lines around it being an it or a him or her. It's okay, right? People,
*  I think part of the magic of these kinds of machines is by nature of their organic movement,
*  of their dynamics, we tend to want to identify with them. We tend to look at them and attribute
*  feeling to that because we've only seen things that move like this that were alive.
*  And so this is an opportunity. It means that you could have feelings for a machine and people
*  have feelings for their cars. They get attracted to them, attached to them. So that's inherently
*  could be a good thing as long as we manage what that interaction is. So we don't put strong
*  boundaries around this and ultimately think it's a benefit, but it's also can be a bit of a curse
*  because I think people look at these machines and they attribute a level of intelligence that
*  the machines don't have. Why? Because again, they've seen things move like this that were
*  living beings, which are intelligent. And so they want to attribute intelligence to the robots
*  that isn't appropriate yet, even though they move like an intelligent being.
*  But you try to acknowledge that the anthropomorphization is there and try to,
*  first of all, acknowledge it's there. And have a little fun with it. Our most recent video,
*  it's just kind of fun to look at the robot. We started off the video with Atlas
*  kind of looking around for where the bag of tools was because the guy up on the scaffolding says,
*  send me some tools. Atlas has to kind of look around and see where they are.
*  And there's a little personality there that is fun. It's entertaining. It makes our jobs
*  interesting. And I think in the long run can enhance interaction between humans and robots
*  in a way that isn't available to machines that don't move that way.
*  This is something to me personally is very interesting. I've been, I happen to have a lot
*  of legged robots. I hope to have a lot of spots in my possession. I'm interested in celebrating
*  robotics and celebrating companies. And I also don't want to companies that do incredible stuff
*  like Boston Dynamics. And there's, you know, I'm a little crazy and you say you don't want to,
*  you want to align, you want to help the company because I ultimately want a company like Boston
*  Dynamics to succeed. And part of that we'll talk about, you know, success kind of requires making
*  money. And so the kind of stuff I'm particularly interested in may not be the thing that makes
*  money in the short term. I can make an argument that will in the long term, but the kind of stuff
*  I've been playing with is a robust way of having the quadrupeds, the robot dogs, communicate in
*  motion with their body movement. The same kind of stuff you do with a dog, but not, not hard
*  coded, but in a robust way and be able to communicate excitement or fear, boredom, all
*  this kinds of stuff. And I think as a base layer of function of behavior to add on top of a robot,
*  I think that's a really powerful way to make the robot more usable for humans for whatever
*  application. I think it's going to be really important. And it's a thing we're beginning to
*  pay attention to. We really want to start a differentiator for the company has always been,
*  we really want the robot to work. We want it to be useful. Making it work at first meant
*  the legged locomotion really works. It can really get around and it doesn't fall down.
*  But beyond that, now it needs to be a useful tool. And our customers are, for example, factory
*  owners, people who are running a process manufacturing facility and the robot needs
*  to be able to get through this complex facility in a reliable way, you know, taking measurements.
*  We need for people who are operating those robots to understand what the robots are doing.
*  If the robot gets into needs help or, or, you know, is in trouble or something, it needs to be able
*  to communicate and a physical indication of some sort so that a person looks at the robot and goes,
*  Oh, I know what that's that robot's doing. The robot's going to go take measurements
*  of my vacuum pump with its thermal camera. You know, you want to be able to indicate that.
*  And we're even just the robots about to turn, you know, in front of you and maybe indicate
*  that it's going to turn. And so you sort of see and can anticipate its motion. So these,
*  this kind of communication is going to become more and more important. It wasn't sort of our
*  starting point, you know, but now that the robots are really out in the world and, you know, we have
*  about a thousand of them out with, with customers right now, this layer of physical indication,
*  I think is going to become more and more important. We'll talk about where it goes because there's a
*  lot of interesting possibilities, but if you can return back to the origins of Boston Dynamics with
*  so there's a more research, the R and D side before we talk about how to build robots at scale.
*  So big dog. So who's big dog? So the company started in 1992 and in probably,
*  2003, I believe is when we took a contract from DART. So basically 10 years, 11 years.
*  We weren't doing robotics. We did a little bit of robotics with Sony. They had a IBO,
*  they had their IBO robot. We were developing some software for that. That kind of got us a
*  little bit involved with robotics again. Then there's this opportunity to do a DARPA contract
*  where they wanted to build a robot dog. And we won a contract to build that. And so that was the
*  genesis of big dog. And it was a quadruped. It was the first time we built a robot that had
*  everything on board that you could actually take the robot out into the wild and operate it. So
*  it had an onboard power plant, it had onboard computers, it had hydraulic actuators that needed
*  to be cooled. So we had cooling systems built in. Everything integrated into the robot.
*  And that was a pretty rough start, right? It was 10 years that we were not a robotics company. We
*  were a simulation company. And then we had to build a robot in about a year. So that was a little bit
*  of a rough transition. Can you just comment on the roughness of that transition? Because
*  big dog, I mean, this is this big quadruped, four legs robot. We built a few different versions of
*  them. But the first one, the very earliest ones, you know, didn't work very well. And we would take
*  them out. And it was hard to get, you know, a go-kart engine driving a hydraulic pump.
*  And, you know, having that all work while trying to get, you know, the robot to stabilize itself.
*  And so what was the power plant? What was the engine? It seemed like my vague recollection.
*  I don't know, it felt very loud and aggressive and kind of thrown together.
*  It's kind of
*  it absolutely was right. We weren't trying to design the best robot hardware at the time.
*  And we wanted to buy an off the shelf engine. And so many of the early versions of big dog had
*  literally go-kart engines or something like that. You see, it's like a gas powered two stroke engine.
*  And the reason why it was two stroke is two stroke engines are lighter weight.
*  That they're also and we didn't generally didn't put mufflers on them because we're trying to
*  save the weight. We didn't care about the noise. And some of these things were horribly loud.
*  But we're trying to manage weight because managing weight in a legged robot is always
*  important because it has to carry everything. That said, that thing was big. Well, I've seen
*  the videos. Yeah, I mean, the early versions, you know, stood about, I don't know, belly high,
*  chest high. You know, they probably weighed maybe a couple of hundred pounds. But, you know,
*  over the course of probably five years, we were able to get that robot
*  to really manage a remarkable level of rough terrain. So we started out with just walking
*  on the flat and then we started walking on rocks and then inclines and then mud and slippery mud.
*  And, you know, by the end of that program, we were convinced that legged locomotion in a robot
*  could actually work because going into it, we didn't know that. We had built quadrupeds at MIT,
*  but they were they used a giant hydraulic pump in the lab. They use a giant computer that was in
*  the lab. They're always tethered to the lab. This was the first time something that was sort
*  of self-contained, you know, walked around in the world and balanced. But the purpose was to prove
*  to ourselves that the legged locomotion could really work. And so Big Dog really cut that open
*  for us. And it was the beginning of what became a whole series of robots. So once we showed to DARPA
*  that you could make a legged robot that could work, there was a period at DARPA where robotics
*  got really hot and there was lots of different programs. And, you know, we were able to build
*  other robots. We built other quadrupeds to hand like LS3 designed to carry heavy loads. We built
*  Cheetah, which was designed to explore what are the limits to how fast you can run.
*  We began to build sort of a portfolio of machines and software that led us
*  build not just one robot, but a whole family of robots.
*  To push the limits in all kinds of directions.
*  Yeah, and to discover those principles. You know, you asked earlier about the art and science of
*  the legged locomotion. We were able to develop principles of legged locomotion so that we knew
*  how to build a small legged robot or a big one. So leg length, you know, was now a parameter that
*  we could play with. Payload was a parameter we could play with. So we built the LS3, which was
*  an 800 pound robot designed to carry a 400 pound payload. And we learned the design rules, basically
*  developed the design rules. How do you scale different robot systems to, you know, their
*  terrain, to their walking speed, to their payload?
*  So when was SpotBorn?
*  Around 2012 or so. So again, almost 10 years into sort of a run with DARPA where we built
*  a bunch of different quadrupeds, we had a sort of a different thread where we started building
*  humanoids. We saw that probably an end was coming where the government was going to kind of back
*  off from a lot of robotics investment. And in order to maintain progress, we just deduced that,
*  well, we probably need to sell ourselves to somebody who wants to continue to invest in this
*  this area. And that was Google. And so at Google, we would meet regularly with Larry Page. And Larry
*  just started asking us, you know, what's your product going to be? And, you know, the logical
*  thing, the thing that we had the most history with, that we wanted to continue developing
*  was a quadruped. But we knew it needed to be smaller, we knew it couldn't have a gas engine,
*  we thought it probably couldn't be hydraulically actuated. So that began the process of exploring
*  if we could migrate to a smaller electrically actuated robot. And that was really the genesis
*  of Spot. So not a gas engine and the actuators are
*  electric. Yes. So can you maybe comment on what it's like? I Google would working with Larry Page,
*  having those meetings and thinking of what will the robot look like? That could be built at scale
*  what like starting to think about a product. Larry always liked the toothbrush test, he wanted
*  products that you used every day. What they really wanted was, you know, a consumer level product,
*  something that would work in your house. We didn't think that was the right next thing to do.
*  Because to be a consumer level product cost is going to be very important. Probably needed to
*  cost a few thousand dollars. And we were, we were building these machines that cost
*  hundreds of thousands of dollars, maybe a million dollars to build. Of course, we were only building
*  two, but we didn't see how to get all the way to this consumer level product in a short amount of
*  time. And he suggested that we make the robots really inexpensive. And part of our philosophy
*  has always been build the best hardware you can make, make the machine operate well, so that
*  you're trying to solve, you know, discover the hard problem that you don't know about.
*  Don't make it harder by building a crappy machine, basically. Build the best machine you can.
*  There's plenty of hard problems to solve that are going to have to do with, you know, underactuated
*  systems and balance. And so we wanted to build these high quality machines still. And we thought
*  that was important for us to continue learning about really what was the important parts of that
*  make robots work. And so there was a little bit of a philosophical difference there.
*  And so ultimately, that's why we're building robots for the industrial sector now. Because the
*  industry can afford a more expensive machine because, you know, their productivity depends on
*  keeping their factory going. And so if Spot costs, you know, a hundred thousand dollars or more,
*  that's not such a big expense to them. Whereas at the consumer level, no one's going to buy a robot
*  like that. And I think we might eventually get to a consumer level product that will be that cheap.
*  But I think the path to getting there needs to go through these really nice machines,
*  so we can then learn how to simplify. So what can you say to the almost engineering challenge
*  of bringing down cost of a robot? So that presumably when you try to build the robot at scale,
*  that also comes into play when you're trying to make money on a robot, even in the industrial setting.
*  But how interesting, how challenging of a thing is that? In particular, probably new to an R&D
*  company. Yeah, I'm glad you brought that last part up. The transition from an R&D company to a
*  commercial company, that's the thing you worry about, you know, because you've got these engineers
*  who love hard problems, who want to figure out how to make robots work. And you don't know if you have
*  engineers that want to work on the quality and reliability and costs that is ultimately required.
*  And indeed, you know, we have brought on a lot of new people who are inspired by those problems.
*  But the big takeaway lesson for me is we have good people, we have engineers who want to solve
*  problems. And the quality and cost and manufacturability is just another kind of problem.
*  And because they're so invested in what we're doing, they're interested in and will go work on
*  those problems as well. And so I think we're managing that transition very well. In fact,
*  I'm really pleased that, I mean, it's a huge undertaking, by the way, right? So even having
*  a robot company, I mean, to get reliability to where it needs to be, we have to have fleets of
*  robots that we're just operating 24 seven in our offices to go find those rare failures and
*  eliminate them. It's just a totally different kind of activity than the research activity where you
*  get it to work, you know, the one robot you have to work in a repeatable way, you know, at the at
*  the end of the day, it's just very different. But I think we're making remarkable progress against
*  it. So one of the cool things I got a chance to visit Boston Dynamics and I mean,
*  one of the things that's really cool is to see a large number of robots moving about.
*  Because I think one of the things you notice in the research environment is the MIT, for example,
*  I don't think anyone ever has a working robot for prolonged periods.
*  So like most robots are just sitting there in a sad state of despair waiting to be born,
*  brought to life for a brief moment of time. But just to have I just remember there's like a
*  there's a spot robot just had like a cowboy hat on and was just walking randomly for whatever
*  reason, I don't even know. But there's a kind of sense of sentience to it, because it doesn't seem
*  like anybody was supervising. It was just doing its thing. I'm gonna stop way short of the sentience.
*  It is the case that if you come to our office, you know, today and walk around the hallways,
*  you're going to see a dozen robots just kind of walking around. Yes, all the time. And that's
*  really a reliability test for us. So we have these robots programmed to do autonomous missions,
*  get up off their charging dock, walk around the building, collect data at a few different places
*  and go sit back down. And we want that to be a very reliable process, because that's what
*  somebody who's running a brewery, a factory, that's what they need the robot to do. And so we have to
*  we have to dog food our own robot, we have to test it in that way. And so on a weekly basis,
*  we have robots that are accruing something like 1500 or maybe 2000 kilometers of walking.
*  And, you know, over 1000 hours of operation every week. And that's something that almost I don't
*  think anybody else in the world can do because, hey, you have to have a fleet of robots to just
*  accrue that much information. You have to be willing to dedicate it to that test. And so that's,
*  but that's essential. That's how you get the reliability. That's how you get it. What about
*  some of the cost cutting from the from the manufacturer side? What have you learned from
*  the manufacturer side of the transition from R&D? And we're still we're still learning a lot there.
*  We're learning how to cast parts and sell instead of mill it all out of, you know, billet aluminum.
*  We're learning how to get plastic molded parts for and we're learning about how to control that
*  process so that you can build the same robot twice in a row. There's a lot to learn there. And we're
*  only part way through that process. We've we've set up a manufacturing facility in Wolfham. It's
*  about a mile from our headquarters and we're doing final assembly and test of both spots and
*  stretches, you know, at that factory. And and it's hard because to be honest, we're still iterating
*  on the design of the robot as we find failures from these reliability tests. We need to go
*  engineer changes and those changes need to now be propagated to the manufacturing line. And that's
*  a hard process, especially when you want to move as fast as we do. And that's been challenging.
*  And it makes it you know, the folks who are working supply chain, who are trying to get the
*  cheapest parts for us, kind of requires that you buy a lot of them to make them cheap. And then we
*  go change the design from underneath them. They're like, what are you doing? And so, you know,
*  getting everybody on the same page here that it yet we still need to move fast, but we also need to
*  try to figure out how to reduce costs. That's one of the challenges of this migration we're
*  going through. And over the past few years, challenges to the supply chain. I mean,
*  imagine you've been a part of a bunch of stressful meetings. Yeah, things got more expensive and
*  harder to get. And yeah, so it's it's all been a challenge. Is there still room for simplification?
*  Oh, yeah, much more. And you know, these are really just the first generation of these machines.
*  We're already thinking about what the next generation of spots going to look like.
*  Spot was built as a platform. So you could put almost any sensor on it. And we provided data
*  communications, mechanical connections, power connections. And but for example, in the
*  applications that we're excited about where you're, you're monitoring these factories
*  for their health, there's probably a simpler machine that we could build that's really focused
*  on that use case. And that's the difference between the general purpose machine or the
*  platform versus the purpose built machine. And so even though even in the factory,
*  we'd still like the robot to do lots of different tasks. If we really knew on day one that we're
*  going to be operating in a factory with these three sensors in it, we would have it all integrated
*  in a package that would be easier, more, less expensive and more reliable. So we're contemplating
*  building a next generation of that machine. So we should mention that so spot for people who
*  somehow are not familiar. So there's a yellow robotic dog and has been featured in many dance
*  videos. It also has gained an arm. So what can you say about the arm that spot has bought the
*  challenges of this design and the manufacturer? We think the future of mobile robots is mobile
*  manipulation. That's where, you know, in the past 10 years, he was getting mobility to work,
*  getting the leg of locomotion to work. If you ask what's the hard problem in the next 10 years,
*  it's getting a mobile robot to do useful manipulation for you. And so we wanted spot
*  to have an arm to experiment with those problems. And the arm is almost as complex as the robot
*  itself, you know, and it's a it's an attachable payload. It has, you know, several motors and
*  actuators and sensors, it has a camera in the end of its hand. So you know, you can sort of
*  see something, the robot will control the motion of its hand to go pick it up autonomously. So
*  in the same way the robot walks and balances, managing its own foot placement to stay balanced,
*  we want manipulation to be mostly autonomous where the robot you indicate, okay, go grab that bottle
*  and then the robot will just go do it using the camera in its hand and then sort of closing
*  in on that, the grasp. But it's a whole nother complex robot on top of a complex legged robot.
*  And so, and of course, we made it the hand look a little like a head, you know, because again,
*  we want it to be sort of identifiable. In the last year, a lot of our sales have been people
*  who already have a robot now buying an arm to add to that robot. Oh, interesting. And so the arm is
*  for sale. Oh, yeah. It's an option. What's the interface like to work with the arm? Like,
*  is it pretty, so are they designed primarily, I guess, just ask that question in general about
*  robots from Boston Dynamics. Is it designed to be easily and efficiently operated remotely by a
*  human being? Or is there also the capability to push towards autonomy? We want both.
*  In the next version of the software that we release, which will be version 3.3,
*  we're going to offer the ability of, if you have an autonomous mission for the robot,
*  we're going to include the option that it can go through a door, which means it's going to have to
*  have an arm and it's going to have to use that arm to open the door. And so that'll be an autonomous
*  manipulation task that just, you can program easily with the robot, strictly through, you know,
*  we have a tablet interface. And so on the tablet, you know, you sort of see the view that Spot sees.
*  You say, there's the door handle. You know, the hinges are on the left and it opens in.
*  The rest is up to you. Take care of it. Oh, so it just takes care of everything.
*  Yeah. So we want in for a task like opening doors, you can automate most of that. And we've
*  automated a few other tasks. We had a customer who had a high-powered breaker switch, essentially.
*  It's an electric utility, Ontario Power Generation. And they have to, when they're going to disconnect,
*  you know, their power supply, right? That could be a gas generator, it could be a nuclear power plant,
*  you know, from the grid, you have to disconnect this breaker switch. Well, as you can imagine,
*  there's, you know, hundreds or thousands of amps and volts involved in this breaker switch.
*  And it's a dangerous event because occasionally you'll get what's called an arc flash. As you
*  just do this disconnect, the power, the sparks jump across and people die doing this. And so Ontario
*  Power Generation used our spot and the arm through the interface to operate this disconnect in an
*  interactive way. And they showed it to us. And we were so excited about it and said, you know,
*  I bet we can automate that task. And so we got some examples of that breaker switch.
*  And I believe in the next generation of software, now we're going to deliver back to Ontario Power
*  Generation, they're going to be able to just point the robot at that breaker. They'll be out,
*  they'll indicate that's the switch. There's sort of two actions you have to do. You have to flip
*  up this little cover, press a button, then get a ratchet, stick it into a socket, and literally
*  unscrew this giant breaker switch. So there's a bunch of different tasks. And we basically
*  automated them so that the human says, okay, there's the switch, go do that part. That right
*  there is the socket where you're going to put your tool and you're going to open it up. And so you
*  can remotely sort of indicate this on the tablet. And then the robot just does everything in between.
*  And it does everything, all the coordinated movement of all the different actuators that
*  include the body and arm. Yeah, it maintains its balance. It walks itself into position so it's
*  within reach and the arm is in a position where it can do the whole task. So it manages the whole
*  body. So how does one become a big enough customer to request features? Because I personally want
*  a robot that gets me a beer. I mean, that has to be like one of the most requests, I suppose,
*  in the industrial setting that's a non alcoholic beverage of picking up objects and bringing the
*  objects to you. We love working with customers who have challenging problems like this. And this one
*  in particular, because we felt like what they were doing, A, it was a safety feature. B, we saw that
*  the robot could do it because they teleoperated it the first time. Probably took them an hour to do
*  it the first time. But the robot was clearly capable. And we thought, oh, this is a great
*  problem for us to work on to figure out how to automate a manipulation task. And so we took it
*  on not because we were going to make a bunch of money from it in selling the robot back to them,
*  but because it motivated us to go solve what we saw as the next logical step. But many of our
*  customers, in fact, we try to our bigger customers, typically ones who are going to run a utility or a
*  factory or something like that. We take that kind of direction from them. And if they're especially
*  if they're going to buy 10 or 20 or 30 robots, and they say, I really needed to do this. Well,
*  that's exactly the right kind of problem that we want to be working on. And so note the self by
*  10 spots and aggressively push for beer manipulation. I think it's fair to say it's notoriously
*  difficult to make a lot of money as a robotics company. How can you make money as a robotics
*  company? Can you speak to that? It seems that a lot of robotics companies fail. It's difficult
*  to build robots is difficult to build robots at a low enough cost where customers even the industrial
*  setting want to purchase them. And it's difficult to build robots that are useful, sufficiently
*  useful. So what can you speak to? And Boston Dynamics has been successful for many years
*  of finding a way to make money. Well, in the early days, of course, you know, the money we made was
*  from doing contract R&D work. And we made money. But you know, we weren't growing and we weren't
*  selling a product. And then we went through several owners who, you know, had a vision of
*  not only developing advanced technology, but eventually developing products. And so both,
*  you know, Google and SoftBank and now Hyundai, you know, had that vision. And we're willing to,
*  you know, provide that investment. Now, our discipline is that we need to go find applications
*  that are broad enough that you could imagine selling thousands of robots, because it doesn't
*  work if you don't sell thousands or tens of thousands of robots. If you only sell hundreds,
*  you will commercially fail. And that's where most of the small robot companies have died.
*  And that's a challenge because, you know, A, you need to field the robots, they need to start to
*  become reliable. And as we've said, that takes time and investment to get there.
*  And so it really does take visionary investment to get there. But we believe that we are going
*  to make money in this industrial monitoring space, because, you know, if a chip fab, if the line goes
*  down because a vacuum pump failed someplace, that can be a very expensive process. It can be a
*  million dollars a day in lost production. Maybe you have to throw away some of the product along
*  the way. And so the robot, if you can prevent that by inspecting the factory every single day,
*  maybe every hour if you have to, there's a real return on investment there. But there needs to be
*  a critical mass of this task. And we're focusing on a few that we believe are ubiquitous in the
*  industrial production environment. And that's using a thermal camera to keep things in place.
*  To keep things from overheating, using an acoustic imager to find compressed air leaks,
*  using visual cameras to read gauges, measuring vibration. These are standard things that you do
*  to prevent unintended shutdown of a factory. And this takes place in a beer factory, we're
*  working with AB InBev, it takes place in chip fabs, you know, we're working with global foundries,
*  it takes place in electric utilities and nuclear power plants. And so the same robot can be applied
*  in all of these industries. And as I said, we have about, actually, it's 1,100 spots out now
*  to really get profitability. We need to be at 1,000 a year, maybe 1,500 a year for that sort of
*  part of the business. So it still needs to grow. But we're on a good path. So I think that's
*  totally achievable. So the application should require crossing that thousand robot barrier.
*  It really should. Yeah. I want to mention our second robot, Stretch. Yeah. Tell me about
*  Stretch. What's Stretch? Who's Stretch? Stretch started differently than Spot. You know, Spot,
*  we built because we had decades of experience building quadrupeds. We just, we had it in our
*  blood, we had to build a quadruped product. But we had to go figure out what the application was.
*  And we actually discovered this factory patrol application, basically preventative maintenance,
*  by seeing what our customers did with it. Stretch is very different. We started knowing that there
*  was warehouses all over the world. There's shipping containers moving all around the world,
*  full of boxes that are mostly being moved by hand. By some estimates, we think there's a trillion
*  boxes, cardboard boxes shipped around the world each year, and a lot of it's done manually.
*  It became clear early on that there was an opportunity for a mobile robot in here to move
*  boxes around. And the commercial experience has been very different between Stretch and with Spot.
*  As soon as we started talking to people, potential customers, about what Stretch was going to be
*  used for, they immediately started saying, oh, I'll buy, I'll buy that robot. You know, in fact,
*  I'm going to put in an order for 20 right now. We just started shipping the robot in January,
*  after several years of development. This year. This year. So our first deliveries of Stretch
*  to customers were DHL and Maersk in January. We're delivering the GAP right now. And we have about
*  seven or eight other customers, all who've already agreed in advance to buy between 10 and 20 robots.
*  And so we've already got commitments for a couple hundred of these robots.
*  This one's going to go, right? It's so obvious that there's a need. And we're not just going to
*  unload trucks, we're going to do any box moving task in the warehouse. And so it too will be a
*  multi-purpose robot. And we'll eventually have it doing palletizing or depalletizing or loading
*  trucks or unloading trucks. There's definitely thousands of robots. There's probably tens of
*  thousands of robots of this in the future. So it's going to be profitable.
*  Can you describe what Stretch looks like?
*  It looks like a big, strong robot arm on a mobile base. The base is about the size of a pallet.
*  And we wanted it to be the size of a pallet because that's what lives in warehouses,
*  right? Pallets of goods sitting everywhere. So it needed to be able to fit in that space.
*  It's not a legged robot.
*  It's not a legged robot. So it was our first, it was actually a bit of a commitment from us,
*  a challenge for us to build a non-balancing robot.
*  To do the much easier problem.
*  Well, because it wasn't going to have this balance problem. And in fact, the very first
*  version of the logistics robot we built was a balancing robot. And that's called Handle.
*  That thing was epic.
*  Oh, it's a beautiful machine.
*  It's an incredible machine. So it was, I mean, it looks epic. It looks like out of,
*  I mean, out of the sci-fi movie of some sort. I mean, just, can you actually just linger on
*  that, like the design of that thing? Because that's another leap into something you probably
*  haven't done. It's a different kind of balancing.
*  Yeah. So let me, I love talking about the history of how Handle came about
*  because it connects all of our robots, actually. So I'm going to start with Atlas.
*  When we had Atlas getting fairly far along, we wanted to understand, I was telling you earlier,
*  the challenge of the human form is that you have this mass up high and balancing that
*  inertia, that mass up high is its own unique challenge. And so we started trying to get Atlas
*  to balance standing on one foot, like on a balance beam using its arms like this.
*  And you know, you can do this. I'm sure I can do this, right? Like if you're walking a tightrope,
*  how do you do that balance? So that's sort of, you know, controlling the inertia, controlling
*  the momentum of the robot. We were starting to figure that out on Atlas. And so our first
*  concept of Handle, which was a robot that was going to be on two wheels, so it had to balance,
*  but it was going to have a big long arm so it could reach a box at the top of a truck.
*  And it was going to, it needed yet another counterbalance, a big tail, to help it balance
*  while it was using its arm. So the reason why this robot sort of looks epic,
*  some people said it looked like an ostrich or maybe an ostrich moving around, was the wheels,
*  the leg, it has legs so it can extend its legs. So it's wheels on legs. We always wanted to build
*  wheels on legs. It had a tail and had this arm and they're all moving simultaneously and in
*  coordination to maintain balance because we had figured out the mathematics of doing this momentum
*  control, how to maintain that balance. And so part of the reason why we built this two-legged robot
*  was we had figured this thing out. We wanted to see it in this kind of machine. And we thought
*  maybe this kind of machine would be good in a warehouse. And so we built it. And it's a
*  beautiful machine. It moves in a graceful way like nothing else we've built, but it wasn't the right
*  machine for a logistics application. We decided it was too slow and couldn't pick boxes fast enough
*  basically. And it was doing beautifully with elegance. It just wasn't efficient enough.
*  So we let it go. But I think we'll come back to that machine eventually. The fact that it's
*  possible, the fact that you showed that you could do so many things at the same time in coordination
*  and so beautifully, there's something there. That was a demonstration of what is possible.
*  Basically, we made a hard decision. And this was really kind of a hard-nosed business decision.
*  It indicated us not doing it just for the beauty of the mathematics or the curiosity, but no,
*  we actually need to build a business that can make money in the long run. And so we ended up building
*  Stretch, which has a big heavy base with a giant battery in the base of it that allows it to run
*  for two shifts, 16 hours worth of operation. And that big battery helps it stay balanced. So it can
*  move a 50-pound box around with its arm and not tip over. It's omnidirectional. It can move in any
*  direction. It has a nice suspension built into it so it can deal with gaps or things on the floor
*  and roll over it. But it's not a balancing robot. It's a mobile robot arm that can work
*  to carry or pick or place a box up to 50 pounds anywhere in the warehouse.
*  Take a box from point A to point B anywhere.
*  Yeah. Palatize, depalatize. We're starting with unloading trucks because there are so many trucks
*  and containers that where goods are shipped. And it's a brutal job. In the summer, it can be 120
*  degrees inside that container. People don't want to do that job. And it's backbreaking labor.
*  Again, these can be up to 50-pound boxes. And so we feel like this is a productivity enhancer.
*  And for the people who used to do that job unloading trucks, they're actually operating
*  the robot now. And so by building robots that are easy to control and it doesn't take an advanced
*  degree to manage, you can become a robot operator. And so as we've introduced these robots to both
*  DHL and Mariskin Gap, the warehouse workers who were doing that manual labor are now the robot
*  operators. And so we see this as ultimately a benefit to them as well. Can you say how much
*  stretch costs? Not yet. But I will say that when we engage with our customers, they'll be able to
*  see a return on investment in typically two years. Okay. So that's something you're constantly
*  thinking about. And I suppose you have to do the same kind of thinking with Spot. So it seems like
*  with stretch, the application is directly obvious. Yeah, it's a slam dunk. Yeah. And so you have a
*  little more flexibility. Well, I think we know the target. We know what we're going after. And with
*  Spot, it took us a while to figure out what we were going after. Well, let me return to that question
*  about maybe the conversation you were having a while ago with Larry Page, maybe looking to the
*  longer future of social robotics, of using Spot to connect with human beings, perhaps in the home.
*  Do you see a future there? If we were to sort of hypothesize or dream about a future where
*  Spot-like robots are in the home as pets, as social robots? We definitely think about it. And
*  we would like to get there. We think the pathway to getting there is likely through these industrial
*  applications and then mass manufacturing. Let's figure out how to build the robots,
*  how to make the software so that they can really do a broad set of skills. That's going to take
*  real investment to get there. Performance first, right? The principle of the company has always
*  been really make the robots do useful stuff. And so, the social robot companies that tried to start
*  someplace else by just making acute interaction, mostly they haven't survived. And so, we think
*  the utility really needs to come first. And that means you have to solve some of these hard problems.
*  And so, to get there, we're going to go through the design and software development in industrial,
*  and then that's eventually going to let you reach a scale that could then be addressed to a
*  commercial consumer level market. And so, yeah, maybe we'll be able to build a smaller
*  Spot with an arm that could really go get your beer for you. But there's things we need to figure
*  out still. How to safely, really safely, if you're going to be interacting with children,
*  you better be safe. And right now, we count on a little bit of standoff distance between the robot
*  and people so that you don't pinch a finger in the robot. So, you've got a lot of things you need to
*  go solve before you jump to that consumer level product. Well, there's a kind of trade-off in
*  safety because it feels like in the home, you can fall. You don't have to be as good at,
*  you're allowed to fail in different ways, in more ways, as long as it's safe for the humans. So,
*  it just feels like an easier problem to solve because it feels like in the factory, you're not
*  allowed to fail. That may be true. But I also think the variety of things a consumer level robot
*  would be expected to do will also be quite broad. They're going to want to get the beer and know the
*  difference between the beer and a Coca-Cola or my snack. They're all going to want you to clean up
*  the dishes from the table without breaking them. Those are pretty complex tasks. And so, there's
*  still work to be done there. So, to push back on that, here's my application. I think they'll be
*  very interesting. I think the application of being a pet, a friend. So, no tasks,
*  just be cute. Because not cute, not cute. A dog is more than just cute. A dog is a friend,
*  is a companion. There's something about just having interacted with them. And maybe because
*  I'm hanging out alone with the robot dogs a little too much. But there's a connection there. And it
*  feels like that connection should not be disregarded. No, it should not be disregarded.
*  Robots that can somehow communicate through their physical gestures are you're going to be
*  more attached to in the long run. Do you remember Ibo? The Sony Ibo? They sold over 100,000 of those,
*  maybe 150,000. It probably wasn't considered a successful product for them. They suspended
*  that eventually. And then they brought it back. Sony brought it back. And people definitely
*  treated this as a pet, as a companion. And I think that will come around again.
*  Will you get away without having any other utility? Maybe in a world where we can really talk to our
*  simple little pet because chat GPT or some other generative AI has made it possible for you to
*  really talk in what seems like a meaningful way. Maybe that'll open the social robot up again.
*  That's probably not a path we're going to go down. Because again, we're so focused on performance
*  and utility. We can add those other things also. But we really want to start from that foundation
*  of utility, I think. Yeah. But I also want to predict that you're wrong on that. Which is that
*  the very path you're taking, which is creating a great robot platform, will very easily take a leap
*  to adding a chat GPT-like capability, maybe GPT-5. And there's just so many open source
*  alternatives that you could just plop that on top of spot. And because you have this robust platform
*  and you're figuring out how to mass manufacture it and how to drive the cost down and how to make it
*  reliable, all those kinds of things, it'll be a natural transition to where just adding chat GPT.
*  I do think that being able to verbally converse or even converse through gestures, part of these
*  learning models is that you can now look at video and imagery and associate intent with that. Those
*  will all help in the communication between robots and people, for sure. And that's going to happen,
*  obviously, more quickly than any of us were expecting. I mean, what else do you want from life?
*  Friend, get your beer and then just talk shit about the state of the world.
*  I mean, where there's a deep loneliness within all of us. And I think a beer and a good chat solves
*  so much of it or takes us a long way to solving a lot of it.
*  It'll be interesting to see when a generative AI can give you that warm feeling that you connected
*  and that, oh yeah, you remember me, you're my friend, we have a history. That history matters,
*  right? Memory of joint...
*  Memory of, yeah.
*  Having witnessed... That's what friendship, that's what connection, that's what love is
*  in many cases. Some of the deepest friendships you have is having gone through a difficult time
*  together and having a shared memory of an amazing time or a difficult time. And that memory creating
*  this foundation based on which you can then experience the world together. The silly, the
*  mundane stuff of day to day is somehow built on a foundation of having gone through some shit in
*  the past. And the current systems are not personalized in that way, but I think that's
*  a technical problem, not some kind of fundamental limitation. So combine that with an embodied robot
*  like Spot, which already has magic in its movement. I think it's a very interesting possibility of
*  where that takes us. But of course you have to build that on top of a company that's making money
*  with real application, with real customers, and with robots that are safe and work and reliable
*  and in manufactured scale. And I think we're in a unique position in that because of our investors,
*  primarily Hyundai, but also SoftBank still owns 20% of us. They're not totally fixated on
*  driving us to profitability as soon as possible. That's not the goal. The goal really is a longer
*  term vision of creating, what does mobility mean in the future? How is this mobile robot technology
*  going to influence us? And can we shape that? And they want both. And so we as a company are
*  trying to strike that balance between let's build a business that makes money. I've been describing
*  that to my own team as self-destination. If I want to drive my own ship, we need to have a business
*  that's profitable in the end, otherwise somebody else is going to drive the ship for us. So that's
*  really important. But we're going to retain the aspiration that we're going to build the next
*  generation of technology at the same time. And the real trick will be if we could do both.
*  Speaking of ships, let me ask you about a competitor and somebody who's become a friend.
*  Elon Musk and Tesla have announced in the early days of building a humanoid robot.
*  How does that change the landscape of your work? So there's from the outside perspective,
*  it seems like, well, as a fan of robotics, it just seems exciting.
*  Right. Very exciting. Right? When Elon speaks, people listen. And so it suddenly brought a
*  bright light onto the work that we'd been doing for over a decade. And I think that's only going
*  to help. And in fact, what we've seen is that in addition to Tesla, we're seeing a proliferation
*  of robotic companies arise now. Including humanoid?
*  Yes. Oh, wow. Yeah. And interestingly, many of them, as they're raising money, for example,
*  will claim whether or not they have a former Boston Dynamics employee on their staff as a criteria.
*  Yeah, that's true. I would do that as a company. Yeah, for sure. And it shows you're legit.
*  Yeah. So it has brung a tremendous validation to what we're doing and excitement.
*  Competitive juices are flowing, the whole thing. So it's all good.
*  Elon has also kind of stated that maybe he implied that the problem is solvable in near term,
*  which is a low-cost humanoid robot that's able to do, that's a relatively general use case robot.
*  So I think Elon is known for setting these kinds of incredibly ambitious goals,
*  maybe missing deadlines, but actually pushing not just the particular team he leads, but the entire
*  world to accomplishing those. Do you see Boston Dynamics in the near future being pushed in that
*  kind of way? Like this excitement of competition kind of pushing Atlas maybe to do more cool stuff,
*  trying to drive the cost of Atlas down perhaps? Or I mean, I guess I want to ask if there's
*  some kind of exciting energy in Boston Dynamics due to this little bit of competition.
*  Oh yeah, definitely. When we released our most recent video of Atlas, I think you'd seen it,
*  the scaffolding and throwing the box of tools around and then doing the flip at the end.
*  We were trying to show the world that not only can we do this parkour mobility thing,
*  but we can pick up and move heavy things. Because if you're going to work in a manufacturing
*  environment, that's what you got to be able to do. And for the reasons I explained to you earlier,
*  it's not trivial to do so. Changing the center of mass by picking up a 50 pound block for a robot
*  that weighs 150 pounds, that's a lot to accommodate. So we're trying to show that we can do that.
*  And so it's totally been energizing. We see the next phase of Atlas being more dexterous hands
*  that can manipulate and grab more things that we're going to start by moving big things around
*  that are heavy and that affect balance. And why is that? Well, really tiny dexterous things
*  probably are going to be hard for a while yet. Maybe you could go build a special purpose
*  robot arm for stuffing chips into electronics boards. But we don't really want to do really
*  fine work like that. I think more coursework where you're using two hands to pick up and
*  balance an unwieldy thing, maybe in a manufacturing environment, maybe in a construction environment,
*  those are the things that we think robots are going to be able to do with the level of dexterity
*  that they're going to have in the next few years. And that's where we're headed.
*  Elon has seen the same thing. He's talking about using the robots in a manufacturing environment.
*  We think there's something very interesting there about having this two armed robot. Because when
*  you have two arms, you can transfer a thing from one hand to the other. You can turn it around.
*  You can reorient it in a way that you can't do it if you just have one hand on it. And so there's a
*  lot that extra arm brings to the table. So I think in terms of mission, you mentioned
*  Boston Dynamics really wants to see what's the limits of what's possible. And so the cost comes
*  second. Or it's a component. But first figure out what are the limitations. I think with Elon,
*  he's really driving the cost down. Is there some inspiration, some lessons you see there
*  of the challenge of driving the cost down, especially with Atlas, with the humanoid robot?
*  Well, I think the thing that he's certainly been learning by building car factories is what that
*  looks like. And by scaling, you can get efficiencies that drive cost down very well. And
*  the smart thing that they have in their favor is they know how to manufacture, they know how to
*  build electric motors, they know how to build computers and vision systems. So there's a lot
*  of overlap between modern automotive companies and robots. But hey, we have a modern robotic,
*  I mean, automotive company behind us as well. So bring it on. Who's doing pretty well, right? The
*  electric vehicles from Hyundai are doing pretty well. I love it. So how much, so we've talked
*  about some of the low level control, some of the incredible stuff that's going on, and basic
*  perception. But how much do you see in currently and in the future of Boston Dynamics, sort of
*  more high level machine learning applications? Do you see customers adding on those capabilities?
*  Or do you see Boston Dynamics doing that in-house? Some kinds of things we really believe are probably
*  going to be more broadly available, maybe even commoditized. Using a machine learning,
*  like a vision algorithm, so a robot can recognize something in the environment,
*  that ought to be something you can just download. Like I'm going to a new environment, I have a new
*  kind of door handle or piece of equipment I want to inspect, you ought to be able to just download
*  that. And I think people, besides Boston Dynamics, will provide that. And we've actually built an API
*  that lets people add these vision algorithms to Spot. And we're currently working with some
*  partners who are providing that. Levitas is an example of a small provider who's
*  giving us software for reading gauges. And actually another partner in Europe,
*  Reply, is doing the same thing. So we see that, we see it ultimately an ecosystem of providers
*  doing stuff like that. And I think ultimately you might even be able to do the same thing with
*  behaviors. So this technology will also be brought to bear on controlling the robot,
*  the motions of the robot. And we're using reinforcement learning to develop algorithms
*  for both locomotion and manipulation. And ultimately this is going to mean you can add
*  new behaviors to a robot quickly. And that could potentially be done outside of Boston Dynamics.
*  Right now that's all internal to us. I think you need to understand at a deep level the robot
*  control to do that. But eventually that could be outside. But it's certainly a place where these
*  approaches are going to be brought to bear in robotics. So reinforcement learning is part
*  of the process. So you do use reinforcement learning.
*  So there's increasing levels of learning with these robots?
*  Yes. And that's for both for locomotion, for manipulation, and for perception.
*  Yes. Well, what do you think in general about all the exciting advancements of
*  transformer neural networks most beautifully illustrated through the large language models like GPT-4?
*  Like everybody else, we're all, I'm surprised at how much, how far they've come.
*  I'm a little bit nervous about the, there's anxiety around them, obviously, for I think good reasons.
*  Disinformation is a curse that's an unintended consequence of social media that could be
*  exacerbated with these tools. So if you use them to deploy disinformation, it could be a real risk.
*  But I also think that the risks associated with these kinds of models don't have a whole lot to do
*  with the way we're going to use them in our robots. If I'm using a robot, I'm building a robot to do
*  a manual task of some sort. I can judge very easily. Is it doing the task I asked it to? Is it doing
*  it correctly? There's sort of a built-in mechanism for judging. Is that, is that a risk?
*  Mechanism for judging. Is it doing the right thing? Did it successfully do the task?
*  Physical reality is a good verifier.
*  It's a good verifier. That's exactly it. And whereas if you're asking for, yeah, I don't know,
*  you're trying to ask a theoretical question in chat GPT, it could be true or it may not be true.
*  And it's hard to have that verifier. What is that truth that you're comparing against? Whereas in
*  physical reality, you know the truth. And this is an important difference. And so I'm not,
*  I think there is reason to be a little bit concerned about, you know, how these tools,
*  large language models could be used. But I'm not very worried about how they're going to be used.
*  Well, how learning algorithms in general are going to be used on robotics. It's really a
*  different application that has different ways of verifying what's going on.
*  Well, the nice thing about language models is that I ultimately see,
*  I'm really excited about the possibility of having conversations with Spot.
*  There's no, I would say negative consequences to that, but just increasing the bandwidth and the
*  variety of ways you can communicate with this particular robot. So you can communicate visually,
*  you can communicate through some interface and to be able to communicate verbally again with the
*  beer and so on. I think that's really exciting to make that much, much easier. We have this partner,
*  Levitas, that's adding the vision algorithms for daydreaming for us. They just, just this week,
*  I saw a demo where they hooked up, you know, a language tool to Spot and they're talking to
*  Spot to give a commands. Can you tell me about the Boston Dynamics AI Institute? What is it in,
*  what is its mission? So it's a separate organization, the Boston Dynamics Artificial
*  Intelligence Institute. It's led by Mark Rayburn, the founder of Boston Dynamics and the former CEO
*  and my old advisor at MIT. Mark has always loved the research, the pure research without the
*  confinement or demands of commercialization. And he wanted to continue to, you know, pursue that
*  unadulterated research. And so suggested to Hyundai that he set up this institute and they
*  agree that it's worth additional investment to kind of continue push, pushing this forefront.
*  And we expect to be working together where, you know, Boston Dynamics is again,
*  both commercialize and do research, but the sort of time horizon of the research we're going to do
*  is, you know, in the next, let's say five years, you know, what can we do in the next five years?
*  Let's work on those problems. And I think the goal of the AI Institute is to work even further out.
*  Certainly, you know, the analogy of of legged locomotion again, when we started that, that
*  was a multi-decade problem. And so I think Mark wants to have the freedom to pursue really hard
*  over the horizon problems. And that's, that'll be the goal of the Institute.
*  So we mentioned some of the dangers of some of the concerns about large language models.
*  That said, you know, there's been a long running fear of these embodied robots.
*  Why do you think people are afraid of legged robots?
*  Yeah, I wanted to show you this. This. So this, this is in the Wall Street Journal.
*  And this is all about chat GPT, right? But look at the picture. Yeah, it's a humanoid robot.
*  That's saying I will say that looks scary. And it says I'm going to replace you.
*  And so the humanoid robot is sort of is the embodiment of this chat GPT tool that there's
*  reason to be a little bit nervous about how it gets deployed. So I'm nervous about that connection.
*  It's unfortunate that they chose to use a robot as that embodiment.
*  For as you and I just said, there's big differences in this. But people are afraid because we've been
*  taught to be afraid for over 100 years. So you know, the word robot was developed by a playwright
*  named Carol Chapak in 1921 to check playwright for Rossum's universal robots. And in that first
*  depiction of a robot, the robots took over the end of the story. And you know, people love to be
*  afraid. And so we've been entertained by these stories for 100 years. But I and I think that's
*  as much why people are afraid as anything else is we've been sort of taught that this is the
*  logical progression through fiction. I think it's fiction. I think what people more and more will
*  realize, just like you said, that the threat, like say you have a super intelligent AI embodied
*  in a robot, that's much less threatening because it's visible, it's verifiable. It's right there in
*  physical reality. And we humans know how to deal with physical reality. I think it's much scarier
*  when you have arbitrary scaling of intelligent AI systems in the digital space, that they could
*  pretend to be human. So robot spot is not going to be pretend it could pretend it's human all at
*  once. It could tell you, you could put your LGBT on top of it, but you're going to know it's not
*  human because you have a contact with physical reality. And you're going to know whether or not
*  it's doing what you asked it to do. Yeah, like it's not going to like if it like, I mean, I'm
*  sure you can start just like a dog lies to you. Like I didn't, I wasn't part of tearing up that
*  couch. So spot can try to lie that like, you know, it wasn't me that spilled that thing, but
*  you're going to kind of figure it out eventually. It's, but if it happens multiple times, you know,
*  but I think that humanity has figured out how to make machines safe. And there's, you know,
*  regulatory environments and certification protocols that we've developed in order to figure
*  out how to make machines safe. We don't know we and don't have that experience with software
*  that can be propagated worldwide in an instant. And so I think we needed to develop those protocols
*  and those tools. And so that's work to be done. But I don't think the fear of that in that work
*  should necessarily impede our ability to now get robots out. Because again, I think,
*  I think we can judge when a robot's being safe. So, and again, just like in that image,
*  there's a fear that robots will take our jobs. I just, I took a ride. I was in San Francisco,
*  to ride in a Waymo vehicles and autonomous vehicle. And I've done it several times.
*  They're doing incredible work over there. But people flicked it off. Oh, really? The car.
*  So that's a long story of what the psychology of that is. It could be maybe big tech or what I
*  don't know exactly what they're flicking off. But there is an element of like these robots are taking
*  our jobs or irreversibly transforming society such that it will have economic impact and
*  the little guy will be would lose a lot would lose their well being. Is there something to be said
*  about the fear that robots will take our jobs? You know, at every significant technological
*  transformation, there's been fear of, you know, an automation anxiety, yes, that it's going to have
*  a broader impact than, than we expected. And there, there will be, you know, jobs will change.
*  Um, sometime in the future, we're going to look back at people who manually unloaded these boxes
*  from trailers. And we're going to say, why did we ever do that manually? But there's a lot of people
*  who are doing that job today, that it could be impacted. Um, but I think the reality is, as I
*  said before, we're going to build the technologies that those very same people can operate it. And so
*  I think there's a pathway to upskilling and operating just like, look, we used to farm with
*  hand tools and now we farm with machines and nobody has really regretted that transformation.
*  And I think the same can be said for a lot of manual labor that we're doing today.
*  And on top of that, you know, look, we're, we're entering a new world where demographics are going
*  to have strong impact on economic growth. And the, you know, the advanced, the first world
*  is losing population quickly. Um, in Europe, they're worried about hiring enough people
*  just to keep the logistics supply chain going. And, you know, part of this is the response to
*  COVID and everybody's sort of thinking back what they really want to do with their life. But
*  these jobs are getting harder and harder to fill. And I just, I'm hearing that over and over again.
*  So I think frankly, this is the right technology at the right time, um, where we're going to need
*  some of this work to be done and we're going to want tools to enhance that productivity.
*  And the scary impact, I think, again, uh, GPT comes to the rescue in terms of being much more
*  terrifying. Uh, the scary, scary impact of basically, so I, I'm a, I guess a software
*  person. So I program a lot and the fact that people like me can be easily replaced, uh, by GPT,
*  that's going to have, uh, well, and a lot, you know, anyone who deals with techs and writing
*  a draft proposal might be easily done with a chat GPT now, consultants, journalists,
*  yeah. Um, everybody is sweating. But on the other hand, you also want it to be right and they don't
*  know how to make it right yet. It, it, but it might make a good starting point for you to iterate.
*  Boy, do I have to talk to you about modern journalism. That's another conversation
*  altogether. But yes, uh, more right than the average, uh, um, this, the, the mean journalists.
*  Yes. Um, you spearheaded the NT weaponization letter, uh, Boston dynamics has, can you describe
*  what that letter states and the general topic of the use of robots in war?
*  We authored a letter and then got several leading robotics companies around the world, including,
*  you know, unitry and China and, um, agility, uh, here in the United States and, um,
*  animal and in Europe and, you know, some others to, uh, co-sign a letter that said we won't put
*  weapons on our robots. And part of the motivation there is, you know, as these robots start to become
*  commercially available, you can see videos online of people who've gotten a robot and strapped a gun
*  on it and shown that they can, you know, operate the gun remotely while driving the robot around.
*  And so having a robot that has this level of mobility, um, and that can easily be configured
*  in a way that could harm somebody from a remote operator is justifiably a scary thing. And so we
*  felt like it was important to draw a bright line there and say, we're not going to allow this
*  for, um, you know, reasons that we think ultimately it's better for the whole industry.
*  If it, if it grows in a way where, uh, robots are ultimately going to help us all and
*  make our lives more fulfilled and productive, but by goodness, you're going to have to trust the
*  technology to let it in. And if, and if you think the robot's going to harm you, that's going to,
*  that's going to hurt and impede the growth of that industry. So we thought it was important to,
*  to draw a bright line and, uh, and then publicize that. And then our plan is to,
*  you know, begin to engage with, uh, lawmakers and regulators. Let's figure out what the rules are
*  going to be around the use of this technology, um, and use our position as leaders in this
*  industry and technology, um, to help force that issue. Uh, and so we are in fact, I have a,
*  I have a policy, you know, director at my company whose job it is to engage with the public, to
*  engage, engage with interested parties and including regulators to sort of begin these
*  discussions. Yeah, it's a really important topic and it's an important topic for people that
*  worry about the impact of robots on our society with autonomous weapons systems.
*  So I'm glad you're sort of leading the way in this. Uh, you are the CEO of Boston Dynamics.
*  What's it take to be a CEO of a robotics company? So you started as a humble engineer,
*  uh, PhD, um, just looking at your journey, what does it take to go from being, from building the
*  thing to leading a company? What are some of the big challenges for you? Uh, courage, I would,
*  I would put front and center for multiple reasons. Um, I talked earlier about the courage to tackle
*  hard problems. So I think there's courage required, not just of me, but of, of all of the
*  people who work at Boston Dynamics. Um, I also think we have a lot of really smart people. We
*  have people who are way smarter than I am. And I think it takes a kind of courage to be willing
*  to lead them and to trust that you have something to offer to somebody who probably is maybe a
*  better engineer than I am. Um, adaptability, you know, part of it, it's been a great career for me.
*  I never would have guessed I'd stayed in one place for 30 years. Um, and the job has always changed.
*  Um, I didn't, I didn't really aspire to be CEO from the very beginning, but it was the natural
*  progression of things. There was always a, there always needed to be some level of management that
*  was needed. And so, you know, when I saw something that needed to be done, that wasn't being done,
*  I just stepped in to go do it. And oftentimes, because we were full of such, uh, strong engineers,
*  oftentimes that was in the management direction or it was in the business development direction or,
*  uh, or organizational hiring. Geez, I was not, I was the main person hiring at Boston Dynamics for
*  probably 20 years. So I was the head of HR basically. So I, you know, just willingness to sort of tackle
*  any piece of the business that, that needs it and then, and be willing to shift. Is there something
*  you could say to what it takes to hire a great team? What, uh, what's a good interview process?
*  How do you know, uh, the guy or galler are going to make a great member of, uh, of a engineering
*  team that's doing some of the hardest work in the world? You know, we developed an interview
*  process that, uh, I was quite fond of. It's a little bit of a hard interview process because
*  the best interviews, you ask somebody about what they're interested in and what they're good at.
*  And if, if they can describe to you something that they worked on and you saw they really did the work,
*  they solved the problems and you saw their passion for it. Um, and you could ask, but,
*  but that, what makes that hard is you have to ask a probing question about it. You have to be
*  smart enough about what they're telling you they're expert at to ask a good question. And so it takes
*  a pretty talented team to do that. Um, but if you can do that, that's how you tap into, ah, this
*  person cares about their work. They really did the work. They're excited about it. That's the kind
*  of person I want at my company. You know, at Google, they taught us about their interview process
*  and it was a little bit different. Um, you know, we, we evolved the process at Boston Dynamics where
*  it didn't matter if you were an engineer or you were an, uh, administrative assistant or a financial
*  person or a technician, you gave us a presentation. You came in and you gave us a presentation. You
*  had to stand up and talk in front of us. And I just thought that was great to tap into those
*  things. I just described you at Google. They taught us and I think I understand why you're
*  right. They're hiring tens of thousands of people. They need a more standardized process. So they
*  would sort of err on the other side where they would ask you a standard question. I'm going to
*  ask you a programming question and I'm just going to ask you to write code in front of me.
*  That's a terrifying, you know, application process. It does let you compare candidates
*  really well, but it doesn't necessarily let you tap in to who they are, right? Because you're asking
*  them to answer your question instead of you asking them about what they're interested in.
*  But frankly, that process is hard to scale. And even at Boston Dynamics,
*  we're not doing that with everybody anymore. We're, but we are still doing that with, you know,
*  the technical people. But we've, because we too now need to sort of increase our rate of hiring,
*  not everybody's giving a presentation anymore. But you're still ultimately trying to find that
*  basic seed of passion. Yeah. For the world. You know, did they really do it? Did they find
*  something interesting or curious, you know? And do they care about it? I think somebody admires
*  Jim Keller and he likes details. So one of the ways you could, if you get a person to talk about
*  what they're interested in, how many details, like how much of the whiteboard can you fill out?
*  Yeah. Well, I think you figure out, did they really do the work if they know some of the details?
*  Yes. And if they have to wash over the details, well, then they didn't do it.
*  Especially with engineering, the work is in the details. Yeah. I have to go there briefly
*  just to get your kind of thoughts in the long-term future of robotics.
*  There's been discussions on the GPT side, on the large language model side,
*  of whether there's consciousness inside these language models. And I think there's fear,
*  but I think there's also excitement or at least a wide world of opportunity and possibility
*  in embodied robots having something like, let's start with emotion, love towards other human beings
*  and perhaps the display, real or fake, of consciousness. Is this something you think
*  about in terms of long-term future? Because as we've talked about, people do anthropomorphize
*  these robots. It's difficult not to project some level of, I use the word sentience, some level of
*  sovereignty, identity, all the things we think as human. That's what anthropomorphization is,
*  we project humanness onto mobile, especially legged robots. Is that something almost from
*  a science fiction perspective you think about or do you try to avoid ever,
*  try to avoid the topic of consciousness altogether?
*  I'm certainly not an expert in it and I don't spend a lot of time thinking about this, right?
*  And I do think it's fairly remote for the machines that we're dealing with.
*  And our robots, you're right, the people anthropomorphize, they read into the robot's
*  intelligence and emotion that isn't there because they see physical gestures that are similar to
*  things they might even see in people or animals. I don't know much about how these large language
*  models really work. I believe it's a kind of statistical averaging of the most common responses
*  to a series of words, right? It's sort of a very elaborate word completion.
*  And I'm dubious that that has anything to do with consciousness.
*  And I even wonder if that model of sort of simulating consciousness by stringing words
*  together that are statistically associated with one another, whether or not that kind of knowledge,
*  if you want to call that knowledge, would be the kind of knowledge that allowed a sentient being to
*  grow or evolve. It feels to me like there's something about truth or emotions that's just
*  a very different kind of knowledge that is absolute. The interesting thing about truth
*  is it's absolute. And it doesn't matter how frequently it's represented in the World Wide Web.
*  If you know it to be true, it may only be there once, but by God, it's true.
*  And I think emotions are a little bit like that too. You know something,
*  and I just think that's a different kind of knowledge than the way these large language
*  models derive sort of simulated intelligence. It does seem that things that are true
*  very well might be statistically well represented on the internet because the internet is made up
*  of humans. So I tend to suspect that large language models are going to be able to simulate
*  consciousness very effectively. And I actually believe that current GPT-4, when fine-tuned
*  correctly, would be able to do just that. And that's going to be a lot of very complicated
*  ethical questions that have to be dealt with. They have nothing to do with robotics. They have
*  and everything to do with... There needs to be some process of labeling, I think, what is true.
*  Because there is also disinformation available on the web, and these models are going to consider
*  that kind of information as well. And again, you can't average something that's true and
*  something that's untrue and get something that's moderately true. It's either right or it's wrong.
*  And so how is that process... And this is obviously something that the purveyors of these,
*  Bard and Chatt GPT, I'm sure this is what they're working on.
*  Well, if you interact on some controversial topics with these models, they're actually
*  refreshingly nuanced. They present... Because you realize there's no one truth. What caused
*  the war in Ukraine? Any geopolitical conflict? You can ask any kind of question, especially the
*  ones that are politically tense, divisive and so on. GPT is very good at presenting. It presents
*  the different hypotheses. It presents calmly the amount of evidence for each one. It's very...
*  It's really refreshing. It makes you realize that truth is nuanced and it does that well.
*  And I think with consciousness, it would very accurately say, well, it sure as hell feels like
*  I'm one of you humans, but where's my body? I don't understand. You're going to be confused.
*  The cool thing about GPT is it seems to be easily confused in the way we are. You wake up in a new
*  room and you ask, where am I? It seems to be able to do that extremely well. It'll tell you one thing,
*  like a fact about when a war started. And when you correct it, say, well, this isn't... That's
*  not consistent. It'll be confused. It'd be, yeah, you're right. It'll have that same element,
*  childlike element with humility of trying to figure out its way in the world. And I think
*  that's a really tricky area to figure out with us humans of what we want
*  to allow AI systems to say to us. Because then if there's elements of sentience that are being
*  on display, you can then start to manipulate human emotion, all that kind of stuff. But I think
*  that's something that's a really serious and aggressive discussion that needs to be had
*  on the software side. I think, again, embodiment, robotics are actually saving us from the
*  arbitrary scaling of software systems versus creating more problems. But that said, I really
*  believe in that connection between human and robot. There's magic there. And I think there's
*  also, I think, a lot of money to be made there. And Boston Dynamics is leading the world in
*  the most elegant movement done by robots. So I can't wait to...
*  Thank you.
*  ...what maybe other people that built on top of
*  Boston Dynamics robots or Boston Dynamics by itself. So you had one wild career, one place,
*  and one set of problems, but incredibly successful. Can you give advice to young folks today
*  in high school, maybe in college, looking out to this future where so much robotics and AI seems to
*  be defining the trajectory of human civilization? Can you give them advice on how to have a career
*  they can be proud of or how to have a life they can be proud of?
*  Well, I would say, follow your heart and your interest. Again, this was an organizing principle,
*  I think, behind the leg lab at MIT that turned into a value at Boston Dynamics, which was
*  follow your curiosity, love what you're doing, you'll have a lot more fun, and you'll be a lot
*  better at it as a result. I think it's hard to plan. Don't get too hung up on planning
*  too far ahead. Find things that you like doing and then see where it takes you.
*  You can always change direction. You will find things that,
*  that wasn't a good move. I'm going to back up and go do something else.
*  So when people are trying to plan a career, I always feel like,
*  there's a few happy mistakes that happen along the way and just live with that.
*  Make choices then. So avail yourselves to these interesting opportunities,
*  like when I happen to run into Mark down in the lab, the basement of the AI lab,
*  but be willing to make a decision and then pivot if you see something exciting to go at.
*  If you're out and about enough, you'll find things like that that get you excited.
*  So there was a feeling when you first met Mark and saw the robots, that there's something
*  interesting. Oh boy, I got to go do this. There is no doubt. What do you think in a hundred years,
*  what do you think Boston Dynamics is doing? What do you think is the role, even bigger,
*  what do you think is the role of robots in society? Do you think we'll be seeing
*  billions of robots everywhere? Do you think about that long-term vision?
*  Well, I do think that, I think the robots will be ubiquitous and they will be out amongst us.
*  And they'll be certainly doing some of the hard labor that we do today.
*  I don't think people don't want to work. People want to work. People need to work,
*  to I think feel productive. We don't want to offload all of the work to the robots,
*  because I'm not sure if people would know what to do with themselves. And I think just
*  self-satisfaction and feeling productive is such an ingrained part of being human
*  that we need to keep doing this work. So we're definitely going to have to work in a complementary
*  fashion. And I hope that the robots and the computers don't end up being able to do all
*  the creative work, right? Because that's the part that's, you know, that's the rewarding.
*  The creative part of solving a problem is the thing that gives you that serotonin rush that
*  you never forget, you know, or that adrenaline rush that you never forget. And so, you know,
*  people need to be able to do that creative work and just feel productive. And sometimes that
*  you can feel productive over fairly simple work. It's just well done, you know, and you can see
*  the result of. So I, you know, there was a, I don't know, there was a cartoon, was it Wall-E?
*  Where they had this big ship and all the people were just overweight, lying on their bench chairs,
*  kind of sliding around on the deck of the movie because they didn't do anything anymore. Well,
*  we definitely don't want to be there. You know, we need to work in some complementary fashion
*  where we keep all of our faculties and our physical health and we're doing some labor, right?
*  But in a complementary fashion somehow. And I think a lot of that has to do with the
*  interaction, the collaboration with robots and with AI systems. I'm hoping there's a lot of
*  interesting possibilities there. I think that could be really cool, right? If you can work in a
*  interaction and really be helpful. Robots, you know, you can ask a robot to do a job you wouldn't
*  ask a person to do, and that would be a real asset. You wouldn't feel guilty about it. You know,
*  you'd say, just do it. It's a machine. I, and I don't have to have qualms about that. You know,
*  the ones that are machines. I also hope to see a future. And it is hope. I do have optimism about
*  the future where some of the robots are pets, have an emotional connection to us humans.
*  And because one of the problems that humans have to solve is this kind of a general loneliness.
*  The more love you have in your life, the more friends you have in your life.
*  I think that makes a more enriching life helps you grow. And I don't fundamentally see why some of
*  those friends can't be robots. There's an interesting long running study. Maybe it's in Harvard. They just
*  nice report article written about it recently. They've been studying this group of a few thousand
*  people now for 70 or 80 years. And the conclusion is that companionship and friendship are the
*  things that make for a better and happier life. And so I agree with you. And I think that could
*  happen with a machine that is probably, you know, simulating intelligence. I'm not convinced there
*  will ever be true intelligence in these machines, sentience, but they could simulate it and they
*  could collect your history and they could, you know, I guess it remains to be seen whether they
*  can establish that real deep. You know, when you sit with a friend and they remember something about
*  you and bring that up and you feel that connection, it remains to be seen if a machine is going to be
*  able to do that for you. Well, I have to say it's inklings of that already started happening for me,
*  some of my best friends that robots and I have you to thank for leading the way in the
*  accessibility and the ease of use of such robots and the elegance of their movement.
*  Robert, you're an incredible person. Boston Dynamics is an incredible company. I've just been a fan for
*  many, many years for everything you stand for, for everything you do in the world. If you're
*  interested in great engineering robotics, go join them, build cool stuff. I'll forever celebrate the
*  work you're doing. And it's just a big honor that you sit with me today and talk. It means a lot. So
*  thank you so much. Keep doing great work. Thank you, Lex. I'm honored to be here and I appreciate it.
*  It was fun. Thanks for listening to this conversation with Robert Plater. To support this podcast,
*  please check out our sponsors in the description. And now let me leave you with some words from
*  Alan Turing in 1950, defining what is now termed the Turing test.
*  A computer would deserve to be called intelligent if it could deceive a human into believing that it
*  was human. Thank you for listening and hope to see you next time.

---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 10126s
Video Keywords: ['russ tedrake', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 133923
Video Rating: None
Video Description: Russ Tedrake is a roboticist and professor at MIT and vice president of robotics research at TRI. He works on control of robots in interesting, complicated, underactuated, stochastic, difficult to model situations.

Support this podcast by supporting our sponsors. Click links, get discount:
- Magic Spoon: https://magicspoon.com/lex link & using code LEX at checkout
- BetterHelp: https://betterhelp.com/lex
- ExpressVPN at https://www.expressvpn.com/lexpod

EPISODE LINKS:
Russ's Website: http://groups.csail.mit.edu/locomotion/russt.html
Russ's YouTube: https://www.youtube.com/watch?v=_1CtAHVea8I
TRI: https://www.tri.global/team/dr-russ-tedrake
Underactuated Robotics: http://underactuated.mit.edu
Drake: https://drake.mit.edu

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
4:29 - Passive dynamic walking
9:40 - Animal movement
13:34 - Control vs Dynamics
15:49 - Bipedal walking
20:56 - Running barefoot
33:01 - Think rigorously with machine learning
44:05 - DARPA Robotics Challenge
1:07:14 - When will a robot become UFC champion
1:18:32 - Black Mirror Robot Dog
1:34:01 - Robot control
1:47:00 - Simulating robots
2:00:33 - Home robotics
2:03:40 - Soft robotics
2:07:25 - Underactuated robotics
2:20:42 - Touch
2:28:55 - Book recommendations
2:40:08 - Advice to young people
2:44:20 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Russ Tedrake Underactuated Robotics, Control, Dynamics and Touch  Lex Fridman Podcast #114
**Lex Fridman:** [August 09, 2020](https://www.youtube.com/watch?v=A22Ej6kb2wo)
*  The following is a conversation with Russ Tedrick,
*  a roboticist and professor at MIT
*  and vice president of robotics research
*  at Toyota Research Institute, or TRI.
*  He works on control of robots in interesting, complicated,
*  underactuated, stochastic, difficult to model situations.
*  He's a great teacher and a great person,
*  one of my favorites at MIT.
*  We'll get into a lot of topics in this conversation
*  from his time leading MIT's DOBRA Robotics Challenge team
*  to the awesome fact that he often runs close
*  to a marathon a day to and from work barefoot.
*  For a world-class roboticist interested
*  in elegant, efficient control
*  of underactuated dynamical systems like the human body,
*  this fact makes Russ one
*  of the most fascinating people I know.
*  Quick summary of the ads.
*  Three sponsors, Magic Spoon Cereal, BetterHelp,
*  and ExpressVPN.
*  Please consider supporting this podcast
*  by going to magicspoon.com slash Lex
*  and using code Lex at checkout,
*  going to betterhelp.com slash Lex,
*  and signing up at expressvpn.com slash Lexpod.
*  Click the links in the description, buy the stuff,
*  get the discount, it really is the best way
*  to support this podcast.
*  If you enjoy this thing, subscribe on YouTube,
*  review it with five stars on Apple Podcasts,
*  support it on Patreon,
*  or connect with me on Twitter at Lex Friedman.
*  As usual, I'll do a few minutes of ads now
*  and never any ads in the middle
*  that can break the flow of the conversation.
*  This episode is supported by Magic Spoon,
*  low carb keto-friendly cereal.
*  I've been on a mix of keto or carnivore diet
*  for a very long time now.
*  That means eating very little carbs.
*  I used to love cereal.
*  Obviously, most have crazy amounts of sugar,
*  which is terrible for you, so I quit years ago.
*  But Magic Spoon is a totally new thing.
*  Zero sugar, 11 grams of protein,
*  and only three net grams of carbs.
*  It tastes delicious.
*  It has a bunch of flavors, they're all good,
*  but if you know what's good for you,
*  you'll go with cocoa, my favorite flavor,
*  and the flavor of champions.
*  Click the magicspoon.com slash Lex link in the description,
*  use code Lex at checkout to get the discount,
*  and to let them know I sent you.
*  So buy all of their cereal.
*  It's delicious and good for you.
*  You won't regret it.
*  This show is also sponsored by BetterHelp,
*  spelled H-E-L-P help.
*  Check it out at betterhelp.com slash Lex.
*  They figure out what you need
*  and match you with a licensed professional therapist
*  in under 48 hours.
*  It's not a crisis line, it's not self-help,
*  it is professional counseling done securely online.
*  As you may know, I'm a bit from the David Goggins
*  line of creatures and still have some demons
*  to contend with, usually on long runs
*  or all-nighters full of self-doubt.
*  I think suffering is essential for creation,
*  but you can suffer beautifully
*  in a way that doesn't destroy you.
*  For most people, I think a good therapist can help in this,
*  so it's at least worth a try.
*  Check out the reviews, they're all good.
*  It's easy, private, affordable, available worldwide.
*  You can communicate by text anytime
*  and schedule weekly audio and video sessions.
*  Check it out at betterhelp.com slash Lex.
*  This show is also sponsored by ExpressVPN.
*  Get it at expressvpn.com slash LexPod
*  to get a discount and to support this podcast.
*  Have you ever watched The Office?
*  If you have, you probably know it's based on a UK series
*  also called The Office.
*  Not to stir up trouble, but I personally think
*  the British version is actually more brilliant
*  than the American one, but both are amazing.
*  Anyway, there are actually nine other countries
*  with their own version of The Office.
*  You can get access to them with no geo restriction
*  when you use ExpressVPN.
*  It lets you control where you want sites
*  to think you're located.
*  You can choose from nearly 100 different countries,
*  giving you access to content
*  that isn't available in your region.
*  So again, get it on any device at expressvpn.com slash LexPod
*  to get an extra three months free
*  and to support this podcast.
*  And now here's my conversation with Russ Tedrick.
*  What is the most beautiful motion of a animal or robot
*  that you've ever seen?
*  I think the most beautiful motion of a robot
*  has to be the passive dynamic walkers.
*  I think there's just something fundamentally beautiful.
*  The ones in particular that Steve Collins built
*  with Andy Ruina at Cornell, a 3D walking machine.
*  So it was not confined to a boom or a plane
*  that you put it on top of a small ramp,
*  give it a little push.
*  It's powered only by gravity.
*  No controllers, no batteries whatsoever.
*  It just falls down the ramp.
*  And at the time it looked more natural, more graceful,
*  more human-like than any robot we'd seen to date,
*  powered only by gravity.
*  How does it work?
*  Well, okay, the simplest model, it's kind of like a slinky.
*  It's like an elaborate slinky.
*  One of the simplest models we used to think about it
*  is actually a rimless wheel.
*  So imagine taking a bicycle wheel, but take the rim off.
*  So it's now just got a bunch of spokes.
*  If you give that a push,
*  it still wants to roll down the ramp.
*  But every time its foot, its spoke comes around
*  and hits the ground, it loses a little energy.
*  Every time it takes a step forward,
*  it gains a little energy.
*  Those things can come into perfect balance
*  and actually they want to.
*  It's a stable phenomenon.
*  If it's going too slow, it'll speed up.
*  If it's going too fast, it'll slow down.
*  And it comes into a stable periodic motion.
*  Now you can take that rimless wheel,
*  which doesn't look very much like a human walking,
*  take all the extra spokes away, put a hinge in the middle.
*  Now it's two legs.
*  That's called our compass gate walker.
*  That can still, you give it a little push,
*  starts falling down a ramp.
*  Looks a little bit more like walking.
*  At least it's a biped.
*  But what Steve and Andy and Ted McGeer
*  started the whole exercise, but what Steve and Andy did
*  was they took it to this beautiful conclusion
*  where they built something that had knees, arms, a torso.
*  The arms swung naturally, give it a little push
*  and that looked like a stroll through the park.
*  How do you design something like that?
*  I mean, is that art or science?
*  It's on the boundary.
*  I think there's a science to getting close to the solution.
*  I think there's certainly art in the way that they,
*  they made a beautiful robot.
*  But then the finesse, because this was where
*  they were working with a system that wasn't perfectly
*  modeled, wasn't perfectly controlled,
*  there's all these little tricks that you have to tune
*  the suction cups at the knees, for instance,
*  so that they stick, but then they release
*  at just the right time.
*  Or there's all these little tricks of the trade,
*  which really are art, but it was a point.
*  I mean, it made the point.
*  We were, at that time, the walking robot,
*  the best walking robot in the world was Honda's Asimo.
*  Absolutely marvel of modern engineering.
*  Is this 90s?
*  This was in 97 when they first released,
*  it sort of announced P2 and then it went through,
*  it was Asimo by then in 2004.
*  And it looks like this very cautious walking,
*  like you're walking on hot coals or something like that.
*  I think it gets a bad rap.
*  Asimo is a beautiful machine.
*  It does walk with its knees bent.
*  Our Atlas walking had its knees bent.
*  But actually Asimo was pretty fantastic.
*  But it wasn't energy efficient.
*  Neither was Atlas when we worked on Atlas.
*  None of our robots that have been that complicated
*  have been very energy efficient.
*  But there's a thing that happens when you do control,
*  when you try to control a system of that complexity.
*  You try to use your motors to basically counteract gravity.
*  Take whatever the world's doing to you and push back,
*  erase the dynamics of the world
*  and impose the dynamics you want
*  because you can make them simple and analyzable,
*  mathematically simple.
*  And this was a very sort of beautiful example
*  that you don't have to do that.
*  You can just let go.
*  Let physics do most of the work, right?
*  And you just have to give it a little bit of energy.
*  This one only walked down a ramp.
*  It would never walk on the flat.
*  To walk on the flat,
*  you have to give a little energy at some point.
*  But maybe instead of trying to take the forces
*  imparted to you by the world and replacing them,
*  what we should be doing
*  is letting the world push us around
*  and we go with the flow.
*  Very Zen, very Zen robot.
*  Yeah, but okay, so that sounds very Zen,
*  but I can also imagine how many failed versions
*  they had to go through.
*  I would say it's probably,
*  would you say it's in the thousands
*  that they've had to have the system fall down
*  before they figured out how to get it?
*  I don't know if it's thousands, but it's a lot.
*  It takes some patience, there's no question.
*  So in that sense, control might help a little bit.
*  Oh, I think everybody, even at the time,
*  said that the answer is to do with that with control.
*  But it was just pointing out
*  that maybe the way we're doing control right now
*  isn't the way we should.
*  Got it, so what about on the animal side?
*  The ones that figured out how to move efficiently.
*  Is there anything you find inspiring or beautiful
*  in the movement of any-
*  I do have a favorite example.
*  Okay.
*  So it sort of goes with the passive walking idea.
*  So is there, how energy efficient are animals?
*  Okay, there's a great series of experiments
*  by George Lauder at Harvard and Mike Tranifilo at MIT.
*  They were studying fish swimming in a water tunnel.
*  And one of these, the type of fish they were studying
*  were these rainbow trout.
*  Because there was a phenomenon well understood
*  that rainbow trout,
*  when they're swimming upstream at mating season,
*  they kind of hang out behind the rocks.
*  And it looks like, I mean,
*  that's tiring work swimming upstream.
*  They're hanging out behind the rocks.
*  Maybe there's something energetically interesting there.
*  So they tried to recreate that.
*  They put in this water tunnel, a rock basically,
*  a cylinder that had the same sort of vortex street,
*  the eddies coming off the back of the rock
*  that you would see in a stream.
*  And they put a real fish behind this
*  and watched how it swims.
*  And the amazing thing is that if you watch from above
*  what the fish swims when it's not behind a rock,
*  it has a particular gate.
*  You can identify the fish the same way you look at a human
*  looking at walking down the street,
*  you sort of have a sense of how a human walks.
*  The fish has a characteristic gate.
*  You put that fish behind the rock, its gate changes.
*  And what they saw was that it was actually resonating
*  and kind of surfing between the vortices.
*  Yeah.
*  Now, here was the experiment that really was the clincher.
*  Because there was still, it wasn't clear
*  how much of that was mechanics of the fish,
*  how much of that is control, the brain.
*  So the clincher experiment,
*  and maybe one of my favorites to date,
*  although there are many good experiments.
*  They took, this was now a dead fish.
*  They took a dead fish.
*  They put a string that tied the mouse of the fish
*  to the rock so it couldn't go back and get caught
*  in the grates.
*  And then they asked what would that dead fish do
*  when it was hanging up behind the rock.
*  And so what you'd expect is it sort of flopped around
*  like a dead fish in the vortex wake
*  until something sort of amazing happens.
*  And this video is worth putting in.
*  Yeah.
*  Right?
*  What happens?
*  The dead fish basically starts swimming upstream, right?
*  It's completely dead, no brain, no motors, no control,
*  but it's somehow the mechanics of the fish
*  resonate with the vortex street
*  and it starts swimming upstream.
*  It's one of the best examples ever.
*  Who do you give credit for that too?
*  Is that just evolution constantly just figuring out
*  by killing a lot of generations of animals
*  like the most efficient motion?
*  Is that, or maybe the physics of our world completely,
*  like, is like evolution applied not only to animals
*  but just the entirety of it somehow drives to efficiency?
*  Like nature likes efficiency?
*  I don't know if that question even makes any sense.
*  I understand the question.
*  That's the reason, I mean, do they co-evolve?
*  Yeah, somehow co, yeah, like,
*  I don't know if an environment can evolve, but.
*  I mean, there are experiments that people do,
*  careful experiments that show that animals can adapt
*  to unusual situations and recover efficiency.
*  So there seems like at least in one direction,
*  I think there is reason to believe
*  that the animal's motor system
*  and probably its mechanics adapt
*  in order to be more efficient,
*  but efficiency isn't the only goal, of course.
*  Sometimes it's too easy to think about only efficiency,
*  but we have to do a lot of other things first,
*  not get eaten, and then all other things being equal,
*  try to save energy.
*  By the way, let's draw a distinction
*  between control and mechanics.
*  Like how would you define each?
*  Yep, I mean, I think part of the point is that
*  we shouldn't draw a line as clearly as we tend to,
*  but on a robot, we have motors
*  and we have the links of the robot, let's say.
*  If the motors are turned off,
*  the robot has some passive dynamics, okay?
*  Gravity does the work.
*  You can put springs, I would call that mechanics, right?
*  If we have springs and dampers,
*  which our muscles are springs and dampers and tendons,
*  but then you have something that's doing active work,
*  putting energy in your motors on the robot.
*  The controller's job is to send commands to the motor
*  that add new energy into the system, right?
*  So the mechanics and control interplay,
*  somewhere the divide is around, you know,
*  did you decide to send some commands to your motor
*  or did you just leave the motors off
*  and let them do their work?
*  Would you say is most of nature
*  on the dynamic side or the control side?
*  So like, if you look at biological systems,
*  or if, you know, we're living in a pandemic now,
*  like, do you think a virus is a,
*  do you think is a dynamic system
*  or is there a lot of control, intelligence?
*  I think it's both,
*  but I think we maybe have underestimated
*  how important the dynamics are, right?
*  I mean, even our bodies, the mechanics of our bodies,
*  certainly with exercise, they evolve,
*  but so I actually, I lost a finger in early 2000s
*  and it's my fifth metacarpal.
*  And it turns out you use that a lot
*  in ways you don't expect when you're opening jars,
*  even when I'm just walking around,
*  if I bump it on something,
*  there's a bone there that was used to taking contact.
*  My fourth metacarpal wasn't used to taking contact,
*  it used to hurt, still does a little bit,
*  but actually my bone has remodeled, right?
*  Over a couple of years, the geometry,
*  the mechanics of that bone changed
*  to address the new circumstances.
*  So the idea that somehow it's only our brain
*  that's adapting or evolving is not right.
*  Maybe sticking on evolution for a bit,
*  because it's tended to create some interesting things.
*  By pedo walking, do you,
*  why the heck did evolution give us,
*  I think we're, are we the only mammals that walk on two feet?
*  No, I mean, there's a bunch of animals that do it a bit.
*  A bit.
*  I think we are the most successful bipeds.
*  I think I read somewhere that the reason
*  the evolution made us walk on two feet
*  is because there's an advantage
*  to being able to carry food back to the tribe
*  or something like that.
*  So like you can carry,
*  it's kind of this communal cooperative thing,
*  so like to carry stuff back to a place of shelter
*  and so on to share with others.
*  Do you understand at all the value of walking on two feet
*  from both a robotics and a human perspective?
*  Yeah, there are some great books written about
*  evolution of, walking evolution of the human body.
*  I think it's easy though to make
*  bad evolutionary arguments.
*  Sure.
*  Most of them are probably bad, but what else can we do?
*  I mean, I think a lot of what dominated our evolution
*  probably was not the things that worked well
*  sort of in the steady state,
*  when things are good.
*  But for instance, people talk about what we should eat now
*  because our ancestors were meat eaters or whatever.
*  Oh yeah, I love that.
*  Yeah.
*  But probably the reason that one pre-homo sapien species
*  versus another survived was not because of
*  whether they ate well when there was lots of food,
*  but when the Ice Age came,
*  probably one of them happened to be in the wrong place,
*  one of them happened to forage a food that was okay
*  even when the glaciers came or something like that.
*  There's a million variables that contributed
*  and we can't, and are actually the amount of information
*  we're working with in telling these stories,
*  these evolutionary stories is very little.
*  So yeah, just like you said, it seems like,
*  if you study history, it seems like history turns on
*  these little events that otherwise would seem meaningless,
*  but in the grand, like when you, in retrospect,
*  were turning points.
*  Absolutely.
*  And that's probably how,
*  like somebody got hit in the head with a rock
*  because somebody slept with the wrong person
*  back in the cave days and somebody get angry
*  and that turned warring tribes
*  combined with the environment, all those millions of things
*  and the meat eating, which I get a lot of criticism
*  because I don't know what your dietary processes are like,
*  but these days I've been eating only meat,
*  which is, there's a large community of people who say,
*  yeah, probably make evolutionary arguments
*  and say, you're doing a great job.
*  There's probably an even larger community of people,
*  including my mom who says it's deeply unhealthy,
*  it's wrong, but I just feel good doing it.
*  But you're right, these evolutionary arguments
*  can be flawed, but is there anything interesting
*  to pull out for,
*  there's a great book, by the way,
*  well, a series of books by Nicholas Taylor
*  about fooled by randomness and black swan,
*  highly recommend them, but yeah, they make the point nicely
*  that probably it was a few random events that,
*  that, yes, maybe it was someone getting hit by a rock,
*  as you say.
*  That said, do you think,
*  I don't know how to ask this question
*  or how to talk about this,
*  but there's something elegant and beautiful
*  about moving on two feet,
*  obviously biased because I'm human,
*  but from a robotics perspective too,
*  you work with robots on two feet.
*  Is it all useful to build robots that are on two feet
*  as opposed to four?
*  Is there something useful about it?
*  I mean, the reason I spent a long time
*  working on bipedal walking was because it was hard
*  and it challenged control theory
*  in ways that I thought were important.
*  I wouldn't have ever tried to convince you
*  that you should start a company around bipeds
*  or something like this.
*  There are people that make pretty compelling arguments.
*  I think the most compelling one is that the world
*  is built for the human form.
*  And if you want a robot to work in the world we have today,
*  then having a human form is a pretty good way to go.
*  And there are places that a biped can go
*  that would be hard for other form factors to go,
*  even natural places.
*  But at some point in the long run,
*  we'll be building our environments for our robots probably.
*  And so maybe that argument falls aside.
*  So you famously run barefoot.
*  Do you still run barefoot?
*  I still run barefoot.
*  That's so awesome.
*  Much to my wife's chagrin.
*  Do you wanna make an evolutionary argument
*  for why running barefoot is advantageous?
*  What have you learned about human and robot movement
*  in general from running barefoot?
*  Human or robot and or?
*  Well, you know, it happened the other way, right?
*  So I was studying walking robots
*  and there's a great conference
*  called the Dynamic Walking Conference
*  where it brings together both the biomechanics community
*  and the walking robots community.
*  And so I had been going to this for years
*  and hearing talks by people who study barefoot running
*  and other mechanics of running.
*  So I did eventually read Born to Run.
*  Most people read Born to Run in the first day, right?
*  The other thing I had going for me
*  is actually that I wasn't a runner before
*  and I learned to run after I had learned
*  about barefoot running,
*  or I mean started running longer distances.
*  So I didn't have to unlearn.
*  And I'm definitely, I'm a big fan of it for me,
*  but I tend to not try to convince other people.
*  There's people who run beautifully with shoes on
*  and that's good.
*  But here's why it makes sense for me.
*  It's all about the long-term game, right?
*  So I think it's just too easy to run 10 miles,
*  feel pretty good, and then you get home at night
*  and you realize my knees hurt, I did something wrong, right?
*  If you take your shoes off,
*  then if you hit hard with your foot at all,
*  then it hurts.
*  You don't like run 10 miles
*  and then realize you've done some damage.
*  You have immediate feedback
*  telling you that you've done something
*  that's maybe suboptimal, and you change your gait.
*  I mean, it's even subconscious.
*  If I right now, having run many miles barefoot,
*  if I put a shoe on, my gait changes
*  in a way that I think is not as good.
*  So it makes me land softer.
*  And I think my goals for running are to do it
*  for as long as I can into old age,
*  not to win any races.
*  And so for me, this is a way to protect myself.
*  Yeah, I think, first of all,
*  I've tried running barefoot many years ago,
*  probably the other way, just reading Born to Run.
*  But just to understand, because I felt like
*  I couldn't put in the miles that I wanted to.
*  And it feels like running for me,
*  and I think for a lot of people,
*  was one of those activities that we do often,
*  and we never really try to learn to do correctly.
*  Like, it's funny, there's so many activities
*  we do every day, like brushing our teeth.
*  I think a lot of us, at least me,
*  probably have never deeply studied
*  how to properly brush my teeth,
*  or wash as now with the pandemic,
*  or how to properly wash our hands.
*  We do it every day, but we haven't really studied,
*  like, am I doing this correctly?
*  But running felt like one of those things
*  that was absurd not to study how to do correctly,
*  because it's the source of so much pain and suffering.
*  Like, I hate running, but I do it,
*  I do it because I hate it, but I feel good afterwards.
*  But I think it feels like you need to learn
*  how to do it properly, so that's where
*  barefoot running came in, and then I quickly realized
*  that my gait was completely wrong.
*  I was taking huge steps, and landing hard on the heel,
*  all those elements.
*  And so yeah, from that I actually learned
*  to take really small steps.
*  Look, I already forgot the number,
*  but I feel like it was 180 a minute, or something like that.
*  And I remember I actually just took songs
*  that are 180 beats per minute,
*  and then tried to run at that beat,
*  just to teach myself.
*  It took a long time, and I feel like after a while
*  you learn to run, you adjust it properly,
*  without going all the way to barefoot.
*  But I feel like barefoot is the legit way to do it.
*  I mean, I think a lot of people
*  would be really curious about it.
*  If they're interested in trying,
*  how would you recommend they start, or try, or explore?
*  Slowly.
*  That's the biggest thing people do,
*  is they are excellent runners,
*  and they're used to running long distances,
*  or running fast, and they take their shoes off,
*  and they hurt themselves instantly trying to do
*  something that they were used to doing.
*  I think I lucked out in the sense that I couldn't run
*  very far when I first started trying.
*  And I run with minimal shoes, too.
*  I mean, I will bring along a pair of actually,
*  like, Aqua socks, or something like this,
*  I can just slip on, or running sandals,
*  I've tried all of them.
*  What's the difference between a minimal shoe
*  and nothing at all?
*  What's, like, feeling-wise, what does it feel like?
*  There is a, I mean, I noticed my gait changing, right?
*  So, I mean, your foot has as many muscles and sensors
*  as your hand does, right?
*  Sensors, ooh, okay.
*  And we do amazing things with our hands.
*  And we stick our foot in a big, solid shoe, right?
*  So there's, I think, you know, when you're barefoot,
*  you're just giving yourself more appropriate suction.
*  And that's why you're more aware of some of the gait flaws
*  and stuff like this.
*  Now, you have less protection, too.
*  So.
*  Rocks and stuff.
*  I mean, yeah, so I think people who are afraid
*  of barefoot running, they're worried about getting cuts
*  or stepping on rocks.
*  First of all, even if that was a concern,
*  I think those are all, like, very short-term, you know,
*  if I get a scratch or something, it'll heal in a week.
*  If I blow out my knees, I'm done running forever.
*  So I will trade the short-term for the long-term, anytime.
*  But even then, you know, and this, again,
*  to my wife's chagrin, your feet get tough, right?
*  The cows, okay.
*  Yeah, I can run over almost anything now.
*  I mean, what, can you talk about, is there,
*  like, is there tips or tricks that you have,
*  suggestions about, like, if I wanted to try it?
*  You know, there is a good book, actually.
*  There's probably more good books since I read them.
*  But Ken Bob, Barefoot Ken Bob Saxton.
*  He's an interesting guy.
*  But I think his book captures the right way
*  to describe running, Barefoot running to somebody,
*  better than any other I've seen.
*  So you run pretty good distances in your bike,
*  and is there, you know, if we talk about bucket list items,
*  is there something crazy on your bucket list, athletically,
*  that you hope to do one day?
*  I mean, my commute is already a little crazy.
*  What are we talking about here?
*  What distance are we talking about?
*  Well, I live about 12 miles from MIT,
*  but you can find lots of different ways to get there.
*  So, I mean, I've run there for many years, I've biked there.
*  A lot of ways?
*  Yeah, but normally I would try to run in
*  and then bike home, bike in, run home.
*  But you have run there and back before Barefoot?
*  Yeah, or with minimal shoes or whatever that.
*  12 times two?
*  Yeah. Okay.
*  It became kind of a game of how can I get to work?
*  I've roller bladed, I've done all kinds of weird stuff.
*  But my favorite one these days
*  is I've been taking the Charles River to work.
*  So I can put in the rowboat not so far from my house,
*  but the Charles River takes a long way to get to MIT.
*  So I can spend a long time getting there.
*  And it's, you know, it's not about, I don't know,
*  it's just about, I've had people ask me,
*  how can you justify taking that time?
*  But for me, it's just a magical time to think,
*  to compress, decompress.
*  You know, especially I'll wake up,
*  do a lot of work in the morning,
*  and then I kind of have to just let that settle
*  before I'm ready for all my meetings.
*  And then on the way home,
*  it's a great time to sort of let that settle.
*  You lead a large group of people.
*  I mean, is there days where you're like,
*  oh shit, I gotta get to work in an hour?
*  I mean, is there a tension there?
*  And like, if we look at the grand scheme of things,
*  just like you said, long-term,
*  that meeting probably doesn't matter.
*  Like you can always say,
*  I'll just, I'll run and let the meeting happen
*  how it happens.
*  Like what, how do you, that zen,
*  how do you, what do you do with that tension
*  between the real world saying urgently,
*  you need to be there, this is important,
*  everything is melting down,
*  how we're gonna fix this robot,
*  there's this critical meeting,
*  and then there's this zen beauty of just running,
*  the simplicity of it, you along with nature.
*  What do you do with that?
*  I would say I'm not a fast runner particularly.
*  Probably my fastest splits ever
*  was when I had to get to daycare on time
*  because they were gonna charge me, you know,
*  some dollar per minute that I was late.
*  I've run some fast splits to daycare.
*  But those times are past now.
*  I think work, you can find a work-life balance in that way.
*  I think you just have to.
*  I think I am better at work
*  because I take time to think on the way in.
*  So I plan my day around it,
*  and I rarely feel that those are really at odds.
*  So what, the bucket list item,
*  if we're talking 12 times two,
*  or approaching a marathon,
*  what, have you run an ultra marathon before?
*  Do you do races?
*  Is there, what's?
*  To win.
*  Not to.
*  I'm not gonna like take a dinghy across the Atlantic
*  or something if that's what you want.
*  But if someone does and wants to write a book,
*  I would totally read it
*  because I'm a sucker for that kind of thing.
*  No, I do have some fun things that I will try.
*  You know, I like to, when I travel,
*  I almost always bike to Logan Airport
*  and fold up a little folding bike
*  and then take it with me and bike to wherever I'm going.
*  And it's taken me,
*  or I'll take a stand up paddle board these days
*  on the airplane and then I'll try to paddle around
*  wherever I'm going or whatever.
*  And I've done some crazy things.
*  But.
*  But not for the, you know, I now talk,
*  I don't know if you know who David Goggins is by any chance.
*  Not well, but yeah.
*  But I talk to him now every day.
*  So he's the person who made me do this stupid challenge.
*  So he's insane and he does things for the purpose
*  in the best kind of way.
*  He does things like for the explicit purpose of suffering.
*  Like he picks the thing that,
*  like whatever he thinks he can do, he does more.
*  So is that, do you have that thing in you or are you?
*  I think it's become the opposite.
*  It's a.
*  So you're like that dynamical system
*  that the walker, the efficient.
*  Yeah, it's a leave no pain, right?
*  You should end feeling better than you started.
*  Okay.
*  But it's mostly, I think, and COVID has tested this
*  because I've lost my commute.
*  I think I'm perfectly happy walking around town
*  with my wife and kids if they could get them to go.
*  And it's more about just getting outside
*  and getting away from the keyboard for some time
*  just to let things compress.
*  Let's go into robotics a little bit.
*  What do you use the most beautiful idea in robotics?
*  Whether we're talking about control
*  or whether we're talking about optimization
*  and the math side of things
*  or the engineering side of things
*  or the philosophical side of things.
*  I think I've been lucky to experience something
*  that not so many roboticists have experienced,
*  which is to hang out with
*  some really amazing control theorists.
*  And the clarity of thought
*  that some of the more mathematical control theory
*  can bring to even very complex, messy looking problems
*  is really, it really had a big impact on me.
*  And I had a day even just a couple of weeks ago
*  where I had spent the day on a Zoom robotics conference,
*  having great conversations with lots of people.
*  Felt really good about the ideas that were flowing
*  and the like.
*  And then I had a late afternoon meeting
*  with one of my favorite control theorists.
*  And we went from these abstract discussions
*  about maybes and what-ifs and what a great idea
*  to these super precise statements
*  about systems that aren't that much more simple
*  or abstract than the ones I care about deeply.
*  And the contrast of that is,
*  I don't know, it really gets me.
*  I think people underestimate
*  maybe the power of clear thinking.
*  And so for instance, deep learning is amazing.
*  I use it heavily in our work.
*  I think it's changed the world unquestionable.
*  It makes it easy to get things to work
*  without thinking as critically about it.
*  So I think one of the challenges as an educator
*  is to think about how do we make sure people get a taste
*  of the more rigorous thinking that I think goes along
*  with some different approaches.
*  Yeah, so that's really interesting.
*  So understanding like the fundamentals,
*  the first principles of the problem
*  or in this case, it's mechanics,
*  like how a thing moves, how a thing behaves,
*  like all the forces involved,
*  like really getting a deep understanding of that.
*  I mean, from physics, the first principle thing
*  come from physics and here it's literally physics.
*  Yeah, and this applies, and deep learning,
*  this applies to not just, I mean,
*  it applies so cleanly in robotics,
*  but it also applies to just in any data set.
*  I find this true.
*  I mean, driving as well.
*  There's a lot of folks that work on autonomous vehicles
*  that don't study driving, like deeply.
*  I might be coming a little bit from the psychology side,
*  but I remember I spent a ridiculous number of hours
*  at lunch at this like lawn chair
*  and I would sit somewhere in MIT's campus,
*  there's a few interesting intersections,
*  and we'd just watch people cross.
*  So we were studying pedestrian behavior,
*  and I felt like as we record a lot of video,
*  and then there's the computer vision extracts,
*  their movement, how they move their head and so on,
*  but like every time, I felt like I didn't understand enough.
*  I just, I felt like I wasn't understanding
*  what, how are people signaling to each other?
*  What are they thinking?
*  How cognizant are they of their fear of death?
*  Like what's the game, what's the underlying game theory here?
*  What are the incentives?
*  And then I finally found a live stream of an intersection
*  that's like high def that I just, I would watch
*  so I wouldn't have to sit out there,
*  but that's interesting.
*  So like I feel-
*  That's tough.
*  That's a tough example because I mean the learning-
*  Humans are involved.
*  Not just because human, but I think,
*  the learning mantra is the basically the statistics
*  of the data will tell me things I need to know, right?
*  And for the example you gave of all the nuances of,
*  eye contact or hand gestures or whatever that are happening
*  for these subtle interactions
*  between pedestrians and traffic, right?
*  Maybe the data will tell that story.
*  I maybe even, one level more meta than what you're saying.
*  For a particular problem, I think it might be the case
*  that data should tell us the story.
*  But I think there's a rigorous thinking
*  that is just an essential skill for a mathematician
*  or an engineer that I just don't wanna lose it.
*  There are certainly super rigorous control,
*  or sorry, machine learning people.
*  I just think deep learning makes it so easy
*  to do some things that,
*  to do some things that our next generation
*  are not immediately rewarded for going through
*  some of the more rigorous approaches.
*  And then I wonder where that takes us.
*  Well, I'm actually optimistic about it.
*  I just want to do my part to try to steer
*  that rigorous thinking.
*  So there's like two questions I wanna ask.
*  Do you have sort of a good example of rigorous thinking
*  where it's easy to get lazy and not do the rigorous thinking?
*  And the other question I have is like,
*  do you have advice of how to practice rigorous thinking
*  in all the computer science disciplines that we've mentioned?
*  Yeah, I mean, there are times where problems
*  that can be solved with well-known, mature methods
*  could also be solved with a deep learning approach.
*  And there's an argument that you must use learning
*  even for the parts we already think we know,
*  because if the human has touched it,
*  then you've biased the system
*  and you've suddenly put a bottleneck in there
*  that is your own mental model.
*  But something like inverting a matrix.
*  I think we know how to do that pretty well,
*  even if it's a pretty big matrix.
*  And we understand that pretty well.
*  And you could train a deep network to do it,
*  but you shouldn't probably.
*  So in that sense, rigorous thinking is understanding
*  the scope and the limitations of the methods that we have,
*  like how to use the tools of mathematics properly.
*  Yeah, I think taking a class on analysis
*  is all I'm sort of arguing is to take a chance to stop
*  and force yourself to think rigorously
*  about even the rational numbers or something.
*  It doesn't have to be the end all problem,
*  but that exercise of clear thinking,
*  I think goes a long way.
*  And I just wanna make sure we keep preaching it.
*  We don't lose it.
*  But do you think when you're doing rigorous thinking
*  or maybe trying to write down equations
*  or sort of explicitly formally describe a system,
*  do you think we naturally simplify things too much?
*  Is that a danger you run into?
*  Like in order to be able to understand something
*  about the system mathematically,
*  we make it too much of a toy example.
*  But I think that's the good stuff, right?
*  That's how you understand the fundamentals?
*  I think so.
*  I think maybe even that's a key to intelligence or something.
*  But I mean, okay, what if Newton and Galileo
*  had deep learning?
*  And they had done a bunch of experiments
*  and they told the world,
*  here's your weights of your neural network.
*  We've solved the problem.
*  Where would we be today?
*  I don't think we'd be as far as we are.
*  There's something to be said about having
*  the simplest explanation for a phenomenon.
*  So I don't doubt that we can train neural networks
*  to predict even physical F equals MA type equations.
*  But I maybe, I want another Newton to come along
*  because I think there's more to do
*  in terms of coming up with the simple models
*  for more complicated tasks.
*  Yeah, let's not offend AI systems from 50 years
*  from now that are listening to this
*  that are probably better at,
*  might be better coming up with
*  F equals MA equations themselves.
*  Sorry, I actually think learning is probably a route
*  to achieving this.
*  But the representation matters, right?
*  And I think having a function that takes my inputs
*  to outputs that is arbitrarily complex
*  may not be the end goal.
*  I think there's still the most simple
*  or parsimonious explanation for the data.
*  Simple doesn't mean low dimensional.
*  That's one thing I think that we've,
*  a lesson that we've learned.
*  So a standard way to do model reduction
*  or system identification and controls
*  is to, the typical formulation is that you try to find
*  the minimal state dimension realization of a system
*  that hits some error bounds or something like that.
*  And that's maybe not, I think we're learning that
*  that was, that state dimension is not the right metric.
*  Of complexity.
*  Of complexity, but for me, I think a lot about contact,
*  the mechanics of contact.
*  A robot hand is picking up an object or something.
*  And when I write down the equations of motion for that,
*  they look incredibly complex.
*  Not because, actually not so much because of the dynamics
*  of the hand when it's moving, but it's just the interactions
*  and when they turn on and off, right?
*  So having a high dimensional, you know,
*  but simple description of what's happening out here is fine.
*  But if when I actually start touching,
*  if I write down a different dynamical system
*  for every polygon on my robot hand
*  and every polygon on the object,
*  whether it's in contact or not
*  with all the combinatorics that explodes there,
*  then that's too complex.
*  So I need to somehow summarize that
*  with a more intuitive physics way of thinking.
*  And yeah, I'm very optimistic
*  that machine learning will get us there.
*  First of all, I mean, I'll probably do it
*  in the introduction, but you're one
*  of the great robotics people at MIT.
*  You're a professor at MIT.
*  You've teach him a lot of amazing courses.
*  You run a large group and you have a important history
*  for MIT, I think, as being a part
*  of the DARPA Robotics Challenge.
*  Can you maybe first say,
*  what is the DARPA Robotics Challenge?
*  And then tell your story around it, your journey with it.
*  Yeah, sure.
*  So the DARPA Robotics Challenge,
*  it came on the tails of the DARPA Grand Challenge
*  and DARPA Urban Challenge, which were the challenges
*  that brought us, put a spotlight on self-driving cars.
*  Gil Pratt was at DARPA and pitched a new challenge
*  that involved disaster response.
*  It didn't explicitly require humanoids,
*  although humanoids came into the picture.
*  This happened shortly after the Fukushima disaster in Japan.
*  And our challenge was motivated roughly by that,
*  because that was a case where if we had had robots
*  that were ready to be sent in, there's a chance
*  that we could have averted disaster.
*  And certainly after the, in the disaster response,
*  there were times where we would have loved
*  to have sent robots in.
*  So in practice, what we ended up with was a grand challenge,
*  a DARPA Robotics Challenge, where Boston Dynamics
*  was to make humanoid robots.
*  People like me and the amazing team at MIT
*  were competing first in a simulation challenge
*  to try to be one of the ones that wins the right
*  to work on one of the Boston Dynamics humanoids
*  in order to compete in the final challenge,
*  which was a physical challenge.
*  And at that point it was already,
*  so it was decided as humanoid robots.
*  So there were two tracks.
*  You could enter as a hardware team
*  where you brought your own robot,
*  or you could enter through the Virtual Robotics Challenge
*  as a software team that would try to win the right
*  to use one of the Boston Dynamics robots.
*  Called Atlas. Atlas.
*  Humanoid robots. Yeah.
*  It was a 400 pound marble,
*  but a pretty big, scary looking robot.
*  Expensive too. Expensive.
*  At the time, yeah.
*  Okay, so I mean, how did you feel
*  the prospect of this kind of challenge?
*  I mean, it seems, autonomous vehicles,
*  yeah, I guess that sounds hard,
*  but not really from a robotics perspective.
*  It's like, didn't they do it in the 80s?
*  Is the kind of feeling I would have
*  like when you first look at the problem,
*  it's on wheels, but like, humanoid robots,
*  that sounds really hard.
*  So what, like, what are your,
*  the psychologically speaking,
*  what were you feeling, excited, scared?
*  Why the heck did you get yourself involved
*  in this kind of messy challenge?
*  We didn't really know for sure
*  what we were signing up for.
*  In the sense that you could have had something
*  that as it was described in the call for participation,
*  that could have put a huge emphasis
*  on the dynamics of walking and not falling down
*  and walking over rough terrain,
*  or the same description,
*  because the robot had to go into this disaster area
*  and turn valves and pick up a drill,
*  it cut the hole through a wall,
*  it had to do some interesting things.
*  The challenge could have really highlighted perception
*  and autonomous planning,
*  or it ended up that locomoting over a complex terrain
*  played a pretty big role in the competition.
*  So.
*  And the degree of autonomy wasn't clear.
*  The degree of autonomy was always a central
*  part of the discussion.
*  So what wasn't clear was how we would be able,
*  how far we'd be able to get with it.
*  So the idea was always that you want semi-autonomy,
*  that you want the robot to have enough compute
*  that you can have a degraded network link to a human.
*  And so the same way we had degraded networks
*  at many natural disasters, you'd send your robot in,
*  you'd be able to get a few bits back and forth,
*  but you don't get to have enough financially
*  to fully operate the robot, every joint of the robot.
*  So, and then the question was,
*  and the gamesmanship of the organizers
*  was to figure out what we're capable of,
*  push us as far as we could,
*  so that it would differentiate the teams
*  that put more autonomy on the robot
*  and had a few clicks and just said, go there, do this,
*  go there, do this, versus someone who's picking
*  every footstep or something like that.
*  So what were some memories, painful, triumphant
*  from the experience?
*  Like what was that journey?
*  Maybe if you can dig in a little deeper,
*  maybe even on the technical side and the team side,
*  that whole process of, from the early idea stages
*  to actually competing.
*  I mean, this was a defining experience for me.
*  It came at the right time for me in my career.
*  I had gotten tenure before I was due a sabbatical,
*  and most people do something relaxing
*  and restorative for a sabbatical.
*  So you got tenure before this.
*  Yeah, yeah, yeah.
*  It was a good time for me.
*  We had a bunch of algorithms that we were very happy with.
*  We wanted to see how far we could push them,
*  and this was a chance to really test our mettle,
*  to do more proper software engineering.
*  The team, we all just worked our butts off.
*  We're in that lab almost all the time.
*  Okay, so there were some, of course, high highs
*  and low lows throughout that.
*  Anytime you're not sleeping and devoting your life
*  to a 400 pound humanoid.
*  I remember actually one funny moment
*  where we're all super tired,
*  and so Atlas had to walk across cinder blocks.
*  That was one of the obstacles.
*  And I remember Atlas was powered down,
*  hanging limp on its harness,
*  and the humans were there,
*  picking up and laying the brick down
*  so that the robot could walk over it.
*  And I thought, what is wrong with this?
*  We've got a robot just watching us do all the manual labor
*  so that it can take its little stroll across the terrain.
*  But, I mean, even the virtual robotics challenge
*  was super nerve wracking and dramatic.
*  I remember, so we were using Gazebo as a simulator
*  on the cloud, and there was all these interesting challenges.
*  I think the investment that OSR,
*  FC, whatever they were called at that time,
*  Brian Gerke's team at Open Source Robotics,
*  they were pushing on the capabilities of Gazebo
*  in order to scale it to the complexity of these challenges.
*  So up to the virtual competition.
*  So the virtual competition was,
*  you will sign on at a certain time,
*  and we'll have a network connection
*  to another machine on the cloud
*  that is running the simulator of your robot.
*  And your controller will run on this controller,
*  this computer, and the physics will run on the other,
*  and you have to connect.
*  Now, the physics, they wanted it to run at real-time rates
*  because there was an element of human interaction,
*  and humans, if you do want to tele-op,
*  it works way better if it's at frame rate.
*  Oh, cool.
*  But it was very hard to simulate these complex scenes
*  at real-time rate.
*  So right up to days before the competition,
*  the simulator wasn't quite at real-time rate.
*  And that was great for me because my controller
*  was solving a pretty big optimization problem,
*  and it wasn't quite at real-time rate.
*  So I was fine, I was keeping up with the simulator,
*  we were both running at about 0.7.
*  And I remember getting this email,
*  and by the way, the perception folks on our team
*  hated that they knew that if my controller was too slow,
*  the robot was gonna fall down,
*  and no matter how good their perception system was,
*  if I can't make my controller fast enough.
*  Anyways, we get this email like three days
*  before the virtual competition.
*  It's for all the marbles,
*  we're gonna either get a humanoid robot or we're not.
*  And we get an email saying, good news,
*  we made the robot, the simulator faster.
*  It's now at one point.
*  I was just like, oh man, what are we gonna do here?
*  So that came in late at night for me.
*  A few days ahead.
*  A few days ahead.
*  I went over, it happened at Frank Pimentor,
*  who's a very, very sharp, he was a student at the time
*  working on optimization.
*  He was still in lab.
*  Frank, we need to make the quadratic programming
*  solver faster.
*  Not like a little faster, it's actually, you know.
*  And we wrote a new solver for that QP together that night.
*  It was terrifying.
*  So there's a really hard optimization problem
*  that you're constantly solving.
*  You didn't make the optimization problem simpler?
*  You wrote a new solver?
*  So, I mean, your observation is almost spot on.
*  What we did was what everybody, I mean,
*  people know how to do this, but we had not yet done
*  this idea of warm starting.
*  So we are solving a big optimization problem
*  at every time step.
*  But if you're running fast enough,
*  the optimization problem you're solving
*  on the last time step is pretty similar
*  to the optimization you're gonna solve with the next.
*  We, of course, had told our commercial solver
*  to use warm starting.
*  But even the interface to that commercial solver
*  was causing us these delays.
*  So what we did was we basically wrote,
*  we called it fast QP at the time.
*  We wrote a very lightweight, very fast layer
*  which would basically check if nearby solutions
*  to the quadratic program, which were very easily checked,
*  could stabilize the robot.
*  And if they couldn't, we would fall back to the solver.
*  You couldn't really test this well, right?
*  Or, I mean, so we always knew that if we fell back
*  to the point where if for some reason things slowed down
*  and we fell back to the original solver,
*  the robot would actually literally fall down.
*  So it was a harrowing sort of edge we're sort of on.
*  But I mean, actually, like the 400 pound humanoid
*  could come crashing to the ground
*  if your solver's not fast enough.
*  But we had lots of good experiences.
*  So can I ask you a weird question I get
*  about idea of hard work?
*  So actually people, like students of yours
*  that I've interacted with and just,
*  and robotics people in general,
*  but they have moments, at moments have worked
*  harder than most people I know in terms of,
*  if you look at different disciplines
*  of how hard people work.
*  But they're also like the happiest.
*  Just like, I don't know.
*  It's the same thing with running.
*  People that push themselves to the limit,
*  they also seem to be the most full of life somehow.
*  And I get often criticized,
*  you're not getting enough sleep,
*  what are you doing to your body, blah, blah, blah,
*  this kind of stuff.
*  And I usually just kind of respond,
*  I'm doing what I love, I'm passionate about it, I love it.
*  I feel like it's invigorating.
*  I actually think, I don't think the lack of sleep
*  is what hurts you.
*  I think what hurts you is stress and lack of doing things
*  that you're passionate about.
*  But in this world, I mean, can you comment about
*  why the heck robotics people are
*  willing to push themselves to that degree?
*  Is there value in that?
*  And why are they so happy?
*  I think you got it right.
*  I mean, I think the causality is not that we work hard,
*  and I think other disciplines work very hard too,
*  but I don't think it's that we work hard
*  and therefore we are happy.
*  I think we found something that we're truly passionate about.
*  It makes us very happy.
*  And then we get a little involved with it
*  and spend a lot of time on it.
*  What a luxury to have something
*  that you wanna spend all your time on, right?
*  We could talk about this for many hours,
*  but maybe if we could pick,
*  is there something on the technical side,
*  on the approach that you took that's interesting,
*  that turned out to be a terrible failure or a success
*  that you carry into your work today
*  about all the different ideas that were involved
*  in making, whether in the simulation or in the real world,
*  making the semi-autonomous system work?
*  I mean, it really did teach me something fundamental
*  about what it's gonna take to get robustness
*  out of a system of this complexity.
*  I would say the DARPA challenge
*  really was foundational in my thinking.
*  I think the autonomous driving community thinks about this.
*  I think lots of people thinking about safety critical systems
*  that might have machine learning in the loop
*  are thinking about these questions.
*  For me, the DARPA challenge was the moment
*  where I realized we've spent every waking minute
*  running this robot.
*  And again, for the physical competition,
*  days before the competition,
*  we saw the robot fall down in a way
*  it had never fallen down before.
*  I thought, how could we have found that?
*  We only have one robot.
*  It's running almost all the time.
*  We just didn't have enough hours in the day
*  to test that robot.
*  Something has to change, right?
*  And then I think that, I mean,
*  I would say that the team that won from KAIST
*  was the team that had two robots
*  and was able to do not only incredible engineering,
*  just absolutely top-rate engineering,
*  but also they were able to test at a rate and discipline
*  that we didn't keep up with.
*  What does testing look like?
*  What are we talking about here?
*  Like what's a loop of tests?
*  Like from start to finish, what is a loop of testing?
*  Yeah, I mean, I think there's a whole philosophy to testing.
*  There's the unit tests, and you can do that on a hardware.
*  You can do that in a small piece of code.
*  You write one function, you should write a test
*  that checks that function's input and outputs.
*  You should also write an integration test
*  at the other extreme of running the whole system together,
*  where they try to turn on all of the different functions
*  that you think are correct.
*  It's much harder to write the specifications
*  for a system-level test,
*  especially if that system is as complicated
*  as a humanoid robot.
*  But the philosophy is sort of the same.
*  On the real robot, it's no different,
*  but on a real robot,
*  it's impossible to run the same experiment twice.
*  So if you see a failure,
*  you hope you caught something in the logs
*  that tell you what happened,
*  but you'd probably never be able to run
*  exactly that experiment again.
*  And right now, I think our philosophy is just
*  basically Monte Carlo estimation,
*  is just run as many experiments as we can,
*  maybe try to set up the environment
*  to make the things we are worried about happen
*  as often as possible.
*  But really, we're relying on somewhat random search
*  in order to test.
*  Maybe that's all we'll ever be able to.
*  But I think, you know,
*  because there's an argument that the things
*  that'll get you are the things that are really nuanced
*  in the world, and it'd be very hard to,
*  for instance, put back in a simulation.
*  Yeah, I guess the edge cases.
*  What was the hardest thing?
*  Like, so you said walking over rough terrain,
*  like just taking footsteps.
*  I mean, people, it's so dramatic and painful
*  in a certain kind of way to watch these videos
*  from the DRC of robots falling.
*  Yep.
*  It's just so heartbreaking.
*  I don't know.
*  Maybe it's because, for me at least,
*  anthropomorphize the robot.
*  Of course, it's also funny for some reason.
*  Like, humans falling is funny for, I don't,
*  it's some dark reason.
*  I'm not sure why it is so,
*  but it's also like tragic and painful.
*  And so speaking of which, I mean,
*  what made the robots fall and fail in your view?
*  So I can tell you exactly what happened on our,
*  I contributed one of those,
*  our team contributed one of those spectacular falls.
*  Every one of those falls has a complicated story.
*  I mean, at one time,
*  the power effectively went out on the robot
*  because it had been sitting at the door
*  waiting for a green light to be able to proceed
*  and its batteries, you know,
*  and therefore it just fell backwards
*  and smashed its head against the ground
*  and it was hilarious,
*  but it wasn't because of bad software, right?
*  But for ours, so the hardest part of the challenge,
*  the hardest task in my view,
*  was getting out of the Polaris.
*  It was actually relatively easy to drive the Polaris.
*  Can you tell the story so I can interrupt?
*  The story of the car.
*  People should watch this video.
*  I mean, the thing you've come up with is just brilliant,
*  but anyway, sorry, what's...
*  Yeah, we kind of joke,
*  we call it the big robot little car problem
*  because somehow the race organizers decided
*  to give us a 400 pound humeroid
*  and that they also provided the vehicle,
*  which is a little Polaris.
*  And the robot didn't really fit in the car,
*  so you couldn't drive the car with your feet
*  under the steering column.
*  We actually had to straddle the main column
*  of the, and have basically one foot in the passenger seat,
*  one foot in the driver's seat,
*  and then drive with our left hand.
*  But the hard part was we had to then park the car,
*  get out of the car.
*  It didn't have a door, that was okay,
*  but it's just getting up from crouch, from sitting,
*  when you're in this very constrained environment.
*  First of all, I remember after watching those videos,
*  I was much more cognizant of how hard it is for me
*  to get in and out of the car, and out of the car especially.
*  It's actually a really difficult control problem.
*  Yeah.
*  And I'm very cognizant of it when I'm injured
*  for whatever reason.
*  Oh, that's really hard.
*  Yeah.
*  So how did you approach this problem?
*  So we had, you think of NASA's operations,
*  and they have these checklists,
*  pre-launched checklists and the like.
*  We weren't far off from that.
*  We had this big checklist,
*  and on the first day of the competition,
*  we were running down our checklist.
*  And one of the things we had to do,
*  we had to turn off the controller,
*  the piece of software that was running,
*  that would drive the left foot of the robot
*  in order to accelerate on the gas.
*  And then we turned on our balancing controller.
*  And the nerves, jitters of the first day of the competition,
*  someone forgot to check that box
*  and turn that controller off.
*  So we used a lot of motion planning
*  to figure out a sort of configuration of the robot
*  that we could get up and over.
*  We relied heavily on our balancing controller.
*  And basically, when the robot was in one of its most
*  precarious sort of configurations,
*  trying to sneak its big leg out of the side,
*  the other controller that thought it was still driving
*  told its left foot to go like this.
*  And that wasn't good.
*  But it turned disastrous for us
*  because what happened was a little bit of push here.
*  Actually, we have videos of us running into the robot
*  with a 10-foot pole, and it kind of will recover.
*  But this is a case where there's no space to recover.
*  So a lot of our secondary balancing mechanisms
*  about like take a step to recover,
*  they were all disabled because we were in the car
*  and there was no place to step.
*  So we were relying on our just lowest level reflexes.
*  And even then, I think just hitting the foot on the floor,
*  we probably could have recovered from it.
*  But the thing that was bad that happened
*  is when we did that and we jostled a little bit,
*  the tailbone of our robot was only a little off the seat,
*  it hit the seat.
*  And the other foot came off the ground just a little bit.
*  And nothing in our plans had ever told us what to do
*  if your butt's on the seat and your feet are in the air.
*  Feet in the air.
*  And then the thing is once you get off the script,
*  things can go very wrong because even our state estimation,
*  our system that was trying to collect all the data
*  from the sensors and understand
*  what's happening with the robot,
*  it didn't know about this situation.
*  So it was predicting things that were just wrong.
*  And then we did a violent shake and fell off
*  in our face first out of the robot.
*  But like into the destination.
*  That's true, we fell in, we got our point for egress.
*  But so is there any hope for, that's interesting,
*  is there any hope for Atlas to be able to do something
*  when it's just on its butt and feet in the air?
*  Absolutely.
*  So you can, what do you?
*  No, so that is one of the big challenges.
*  And I think it's still true.
*  Boston Dynamics and Andy Mao and there's this incredible
*  work on legged robots happening around the world.
*  Most of them still are very good at the case
*  where you're making contact with the world at your feet.
*  And they have typically point feet relatively.
*  They're balls on their feet, for instance.
*  If those robots get in a situation where the elbow
*  hits the wall or something like this,
*  that's a pretty different situation.
*  Now they have layers of mechanisms that will make,
*  I think the more mature solutions have ways in which
*  the controller won't do stupid things.
*  But a human, for instance, is able to leverage
*  incidental contact in order to accomplish a goal.
*  In fact, if you push me, I might actually put my hand out
*  and make a brand new contact.
*  The feet of the robot are doing this on quadrupeds,
*  but we mostly in robotics are afraid of contact
*  on the rest of our body, which is crazy.
*  There's this whole field of motion planning,
*  collision-free motion planning.
*  And we write very complex algorithms so that the robot
*  can dance around and make sure it doesn't touch the world.
*  So people are just afraid of contact
*  because contact is seen as a difficult.
*  It's still a difficult control problem and sensing problem.
*  Now you're a serious person.
*  I'm a little bit of an idiot,
*  and I'm going to ask you some dumb questions.
*  So I do martial arts, so like jiu-jitsu,
*  I wrestled my whole life.
*  So let me ask the question,
*  whenever people learn that I do any kind of AI,
*  or like I mentioned robots and things like that,
*  they say, when are we gonna have robots
*  that can win in a wrestling match
*  or in a fight against a human?
*  So we just mentioned sitting on your butt.
*  If you're in the air, that's a common position.
*  Jiu-jitsu, when you're on the ground,
*  you're a down opponent.
*  Like how difficult do you think is the problem?
*  And when will we have a robot that can defeat a human
*  in a wrestling match?
*  And we're talking about a lot.
*  Like, I don't know if you're familiar with wrestling,
*  but essentially,
*  it's basically the art of contact.
*  It's like, it's because you're picking contact points,
*  and then using like leverage, like to off balance,
*  to trick people, like you make them feel
*  like you're doing one thing,
*  and then they change their balance,
*  and then you switch what you're doing,
*  and then results in a throw or whatever.
*  It's basically the art of multiple contacts.
*  Awesome, it's a nice description of it.
*  So there's also an opponent in there, right?
*  So if-
*  Very dynamic.
*  Right, if you are wrestling a human
*  and are in a game theoretic situation with a human,
*  that's still hard.
*  But just to speak to the quickly reasoning about contact
*  part of it, for instance.
*  Yeah, maybe even throwing the game theory out of it,
*  almost like a non-dynamic opponent.
*  Right, there's reasons to be optimistic,
*  but I think our best understanding of those problems
*  are still pretty hard.
*  I have been increasingly focused on manipulation,
*  partly where that's a case where the contact
*  has to be much more rich.
*  And there are some really impressive examples
*  of deep learning policies, controllers,
*  that can appear to do good things through contact.
*  We've even got new examples of deep learning models
*  of predicting what's gonna happen to objects
*  as they go through contact.
*  But I think the challenge you just offered there
*  still eludes us, right?
*  The ability to make a decision
*  based on those models quickly.
*  I have to think though it's hard for humans too,
*  when you get that complicated.
*  I think probably you had maybe a slow motion version
*  of where you learned the basic skills,
*  and you've probably gotten better at it,
*  and there's much more subtlety.
*  But it might still be hard to actually,
*  really on the fly, take a model of your humanoid
*  and figure out how to plan the optimal sequence
*  that might be a problem we never solve.
*  Well, I mean, one of the most amazing things to me
*  about the, we can talk about martial arts,
*  we could also talk about dancing,
*  doesn't really matter, too human.
*  I think it's the most interesting study of contact.
*  It's not even the dynamic element of it.
*  It's the, like when you get good at it,
*  it's so effortless.
*  Like I can just, I'm very cognizant
*  of the entirety of the learning process
*  being essentially like learning how to move my body
*  in a way that I could throw very large weights
*  around effortlessly.
*  And I can feel the learning.
*  Like I'm a huge believer in drilling of techniques,
*  and you can just like feel your,
*  you're not feeling, you're feeling, sorry,
*  you're learning it intellectually a little bit,
*  but a lot of it is the body learning it somehow,
*  like instinctually.
*  And whatever that learning is,
*  that's really, I'm not even sure if that's equivalent
*  to like a deep learning, learning a controller.
*  I think it's something more,
*  it feels like there's a lot of distributed learning
*  going on.
*  Yeah, I think there's hierarchy and composition,
*  Yeah.
*  probably in the systems
*  that we don't capture very well yet.
*  You have layers of control systems.
*  You have reflexes at the bottom layer,
*  and you have a system that's capable of planning a vacation
*  to some distant country, which is probably,
*  you probably don't have a controller,
*  a policy for every possible destination you'll ever pick.
*  But there's something magical in the in-between,
*  and how do you go from these low-level feedback loops
*  to something that feels like a pretty complex set of outcomes?
*  You know, my guess is, I think there's evidence
*  that you can plan at some of these levels, right?
*  So Josh Tenenbaum just showed it,
*  I just talked the other day,
*  he's got a game he likes to talk about,
*  I think he calls it the pick three game or something,
*  where he puts a bunch of clutter down in front of a person,
*  and he says, okay, pick three objects,
*  and it might be a telephone or a shoe or a Kleenex box
*  or whatever.
*  And apparently you pick three items, and then you pick,
*  he says, okay, pick the first one up with your right hand,
*  the second one up with your left hand.
*  Now using those objects, those now as tools,
*  pick up the third object.
*  Right, so that's down at the level of physics and mechanics
*  and contact mechanics that I think we do learning,
*  or we do have policies for, we do control for,
*  almost feedback, but somehow we're able to still,
*  I mean, I've never picked up a telephone with a shoe
*  and a water bottle before, and somehow,
*  and it takes me a little longer to do that the first time,
*  but most of the time we can sort of figure that out.
*  So, yeah, I think the amazing thing is this ability
*  to be flexible with our models,
*  plan when we need to, use our well-oiled controllers
*  when we don't, when we're in familiar territory.
*  Having models, I think the other thing you just said
*  was something about, I think your awareness
*  of what's happening is even changing
*  as you improve your expertise, right?
*  So maybe you have a very approximate model
*  of the mechanics to begin with, and as you gain expertise,
*  you get a more refined version of that model.
*  You're aware of muscles or balance components
*  that you just weren't even aware of before.
*  So how do you scaffold that?
*  Yeah, plus the fear of injury,
*  the ambition of goals of excelling,
*  and fear of mortality.
*  Let's see, what else is in there as motivations?
*  Overinflated ego in the beginning,
*  and then a crash of confidence in the middle.
*  All of those seem to be essential for the learning process.
*  And if all that's good,
*  then you're probably optimizing energy efficiency.
*  Yeah, right, so we have to get that right.
*  So there was this idea that you would have robots
*  play soccer better than human players by 2050.
*  That was the goal.
*  Basically, was the goal to beat world champion team?
*  To become a World Cup, be like a World Cup level team.
*  So are we gonna see that first, or a robot,
*  if you're familiar, there's an organization called UFC
*  for mixed martial arts.
*  Are we gonna see a World Cup championship soccer team
*  that have robots, or a UFC champion mixed martial artist
*  that's a robot?
*  I mean, it's very hard to say one thing is harder,
*  some problem is harder than the other.
*  What probably matters is who started the organization.
*  I think RoboCup has a pretty serious following,
*  there is a history now of people playing that game,
*  learning about that game, building robots to play that game,
*  building increasingly more human robots,
*  it's got momentum.
*  And so if you want to have mixed martial arts compete,
*  you better start your organization now, right?
*  I think almost independent of which problem
*  is technically harder,
*  because they're both hard and they're both different.
*  That's a good point.
*  I mean, those videos are just hilarious,
*  especially the humanoid robots trying to play soccer.
*  I mean, they're kind of terrible right now.
*  I mean, I guess there is RoboSumo wrestling,
*  there's like the Robo One competitions,
*  where they do have these robots that go on a table
*  and basically fight, so maybe I'm wrong.
*  First of all, do you have a year in mind for RoboCup,
*  just from a robotics perspective?
*  It seems like a super exciting possibility that,
*  like in the physical space, this is what's interesting.
*  I think the world is captivated.
*  I think it's really exciting.
*  It inspires just a huge number of people
*  when a machine beats a human at a game
*  that humans are really damn good at.
*  So you're talking about chess and Go,
*  but that's in the world of digital.
*  I don't think machines have beat humans
*  at a game in the physical space yet,
*  but that would be just...
*  You have to make the rules very carefully, right?
*  I mean, if Atlas kicked me in the shins, I'm down,
*  and game over, so it's very subtle on what's fair.
*  I think the fighting one is a weird one,
*  because you're talking about a machine
*  that's much stronger than you.
*  But yeah, in terms of soccer, basketball,
*  all those kinds of things.
*  Even soccer, right?
*  I mean, as soon as there's contact or whatever,
*  and there are some things that the robot will do better.
*  I think if you really set yourself up to try to see
*  could robots win the game of soccer
*  as the rules were written,
*  the right thing for the robot to do
*  is to play very differently than a human would play.
*  You're not gonna get the perfect soccer player robot.
*  You're gonna get something that exploits the rules,
*  exploits its super actuators,
*  its super low bandwidth feedback loops or whatever,
*  and it's gonna play the game differently
*  than you want it to play.
*  I bet there's ways, I bet there's loopholes, right?
*  We saw that in the DARPA challenge,
*  it's very hard to write a set of rules
*  that someone can't find a way to exploit.
*  Let me ask another ridiculous question.
*  I think this might be the last ridiculous question,
*  but I doubt it.
*  I aspire to ask as many ridiculous questions
*  of a brilliant MIT professor.
*  Okay, I don't know if you've seen the black mirror.
*  It's funny, I never watched the episode.
*  I know when it happened though,
*  because I gave a talk to some MIT faculty one day
*  on an unassuming Monday or whatever,
*  I was telling them about the state of robotics,
*  and I showed some video from Boston Dynamics
*  of the quadruped spot at the time.
*  It was the early version of spot.
*  And there was a look of horror that went across the room.
*  And I said, I've shown videos like this a lot of times,
*  what happened?
*  And it turns out that this video had,
*  this black mirror episode had changed
*  the way people watched the videos I was putting out.
*  The way they see these kinds of robots.
*  So I talked to so many people who are just terrified
*  because of that episode probably of these kinds of robots.
*  I almost wanna say that you almost enjoy being terrified.
*  I don't even know what it is about human psychology.
*  They imagine doomsday, the destruction of the universe
*  or our society and enjoy being afraid.
*  I don't wanna simplify it,
*  but it feels like they talk about it so often.
*  It almost, there does seem to be an addictive quality to it.
*  I talked to a guy, a guy named Joe Rogan,
*  who's kind of the flag bearer
*  for being terrified of these robots.
*  Do you have two questions?
*  One, do you have an understanding
*  of why people are afraid of robots?
*  And the second question is, in black mirror,
*  just to tell you the episode,
*  I don't even remember it that much anymore,
*  but these robots, I think they can shoot
*  like a pellet or something.
*  They basically have, it's basically a spot with a gun.
*  And how far are we away from having robots
*  that go rogue like that?
*  Basically spot that goes rogue for some reason
*  and somehow finds a gun.
*  Right, so I mean, I'm not a psychologist.
*  I think, I don't know exactly why people react
*  the way they do.
*  I think we have to be careful about the way robots
*  influence our society and the like.
*  I think that's something, that's a responsibility
*  that roboticists need to embrace.
*  I don't think robots are gonna come after me
*  with a kitchen knife or a pellet gun right away.
*  And I mean, they were programmed in such a way,
*  but I used to joke with Atlas that all I had to do
*  was run for five minutes and its battery would run out.
*  But actually they've got a very big battery
*  in there by the end.
*  So it was over an hour.
*  I think the fear is a bit cultural though.
*  Because I mean, you notice that,
*  like I think in my age in the US,
*  we grew up watching Terminator.
*  If I had grown up at the same time in Japan,
*  I probably would have been watching Astro Boy.
*  And there's a very different reaction to robots
*  in different countries.
*  So I don't know if it's a human innate fear
*  of metal marvels or if it's something that we've done
*  to ourselves with our sci-fi.
*  Yeah, the stories we tell ourselves through movies,
*  through just through popular media.
*  But if I were to tell, if you were my therapist
*  and I said, I'm really terrified
*  that we're going to have these robots very soon,
*  that will hurt us,
*  like how do you approach making me feel better?
*  Like why shouldn't people be afraid?
*  I think there's a video that went viral recently.
*  Everything was spot in Boston,
*  it just goes viral in general.
*  But usually it's like really cool stuff.
*  Like they're doing flips and stuff or like sad stuff.
*  Atlas being hit with a broomstick or something like that.
*  But there's a video where I think one of the new productions
*  bought robots, which are awesome.
*  It was like patrolling somewhere in some country.
*  And people immediately were saying
*  this is the dystopian future, the surveillance state.
*  For some reason, you can just have a camera,
*  something about spot being able to walk on four feet
*  with really terrified people.
*  So what do you say to those people?
*  I think there is a legitimate fear there
*  because so much of our future is uncertain.
*  But at the same time, technically speaking,
*  it seems like we're not there yet.
*  So what do you say?
*  I mean, I think technology is complicated.
*  It can be used in many ways.
*  I think there are purely software attacks
*  that somebody could use to do great damage.
*  Maybe they have already.
*  I think wheeled robots could be used in bad ways too.
*  Drones. Drones, right?
*  I don't think that, let's see.
*  I don't want to be building technology
*  just because I'm compelled to build technology
*  and I don't think about it.
*  But I would consider myself a technological optimist,
*  I guess, in the sense that I think we should continue
*  to create and evolve and our world will change.
*  And if we will introduce new challenges,
*  we'll screw something up maybe,
*  but I think also we'll invent ourselves
*  out of those challenges and life will go on.
*  So it's interesting because you didn't mention
*  this is technically too hard.
*  I don't think robots are,
*  I think people attribute a robot that looks like an animal
*  as maybe having a level of self-awareness
*  or consciousness or something that they don't have yet.
*  So it's not, I think our ability to anthropomorphize
*  those robots is probably,
*  we're assuming that they have a level of intelligence
*  that they don't yet have
*  and that might be part of the fear.
*  So in that sense, it's too hard.
*  But there are many scary things in the world.
*  So I think we're right to ask those questions.
*  We're right to think about the implications of our work.
*  Right, in the short term as we're working on it for sure,
*  is there something long-term that scares you
*  about our future with AI and robots?
*  A lot of folks from Elon Musk to Sam Harris,
*  a lot of folks talk about the existential threats
*  about artificial intelligence.
*  Oftentimes robots kind of inspire that the most
*  because of the anthropomorphism.
*  Do you have any fears?
*  It's an important question.
*  I actually, I think I like Rod Brooks' answer,
*  maybe the best on this.
*  I think, and it's not the only answer he's given
*  over the years, but maybe one of my favorites is
*  he says it's not gonna be,
*  he's got a book, Flesh and Machines, I believe.
*  It's not gonna be the robots versus the people.
*  We're all gonna be robot people.
*  Because we already have smartphones,
*  some of us have serious technology
*  implanted in our bodies already,
*  whether we have a hearing aid or a pacemaker
*  or anything like this.
*  People with amputations might have prosthetics.
*  That's a trend I think that is likely to continue.
*  I mean, this is now wild speculation.
*  But I mean, when do we get to cognitive implants
*  and the like?
*  Yeah, with neural link, brain computer interfaces.
*  That's interesting.
*  So there's a dance between humans and robots
*  that's going to be,
*  it's going to be impossible to be scared
*  of the other out there, the robot,
*  because the robot will be part of us, essentially.
*  It'd be so intricately part of our society.
*  Yeah, and it might not even be implanted part of us,
*  but just it's so much a part of our society.
*  So in that sense, the smartphone is already the robot
*  we should be afraid of, yeah.
*  I mean, yeah, and all the usual fears arise
*  of the misinformation, the manipulation,
*  all those kinds of things that,
*  the problems are all the same.
*  They're human problems, essentially, it feels like.
*  Yeah, I mean, I think the way we interact
*  with each other online is changing the value
*  we put on personal interaction.
*  And that's a crazy big change that's going to happen
*  and rip through our, has already been ripping
*  through our society, right?
*  That has implications that are massive.
*  I don't know if they should be scared of it
*  or go with the flow, but I don't see some battle lines
*  between humans and robots being the first thing
*  to worry about.
*  I mean, I do want to just, as a kind of comment,
*  maybe you can comment about your just feelings
*  about Boston Dynamics in general,
*  but I love science, I love engineering,
*  I think there's so many beautiful ideas in it.
*  And when I look at Boston Dynamics
*  or legged robots in general, I think they inspire people,
*  curiosity and feelings in general, excitement
*  about engineering more than almost anything else
*  in popular culture.
*  And I think that's such an exciting responsibility
*  and possibility for robotics.
*  And Boston Dynamics is riding that wave pretty damn well.
*  They found it, they've discovered that hunger
*  and curiosity in the people and they're doing magic with it.
*  I don't care if, I mean, I guess their company
*  they have to make money, right?
*  But they're already doing incredible work
*  and inspiring the world about technology.
*  I mean, do you have thoughts about Boston Dynamics
*  and maybe others, your own work in robotics
*  and inspiring the world in that way?
*  I completely agree.
*  I think Boston Dynamics is absolutely awesome.
*  I think I show my kids those videos
*  and the best thing that happens is sometimes
*  they've already seen them.
*  Right, I think, I just think it's a pinnacle of success
*  in robotics that is just one of the best things
*  that's happened.
*  Absolutely completely agree.
*  One of the heartbreaking things to me
*  is how many robotics companies fail.
*  How hard it is to make money with a robotics company.
*  Like, I robot like went through hell
*  just to arrive at a Roomba to figure out one product.
*  And then there's so many home robotics companies
*  like Jibo and Anki, Anki, the cutest toy
*  that's a great robot I thought went down.
*  I'm forgetting a bunch of them,
*  but a bunch of robotics companies fail.
*  Rod's company, Rethink Robotics.
*  Like, do you have anything hopeful to say
*  about the possibility of making money with robots?
*  Oh, I think you can't just look at the failures.
*  I mean, Boston Dynamics is a success.
*  There's lots of companies that are still
*  doing amazingly good.
*  There's lots of companies that are still
*  doing amazingly good work in robotics.
*  I mean, this is the capitalist ecology or something, right?
*  I think you have many companies, you have many startups
*  and they push each other forward and many of them fail
*  and some of them get through.
*  And that's sort of the natural.
*  Way of things.
*  Way of those things.
*  I don't know that is robotics really that much worse?
*  I feel the pain that you feel too.
*  Every time I read one of these,
*  I sometimes it's friends and I definitely wish
*  it went better or went differently.
*  But I think it's healthy and good to have
*  bursts of ideas, bursts of activities.
*  Ideas, if they are really aggressive,
*  they should fail sometimes.
*  Certainly that's the research mantra, right?
*  If you're succeeding at every problem you attempt,
*  then you're not choosing aggressively enough.
*  Is it exciting to you, the new spot?
*  Oh, it's so good.
*  When are you getting them as a pet?
*  Yeah, I mean, I have to dig up 75K right now.
*  I mean, it's so cool that there's a price tag,
*  you can go and then actually buy it.
*  I have a Skydio R1, love it.
*  No, I would absolutely be a customer.
*  I wonder what your kids would think about.
*  I actually, Zach from Boston Dynamics would let my kid
*  drive in one of their demos one time
*  and that was just so good, so good.
*  I'll forever be grateful for that.
*  And there's something magical about the anthropomorphization
*  of that arm, it adds another level of human connection.
*  I'm not sure we understand from a control aspect
*  the value of anthropomorphization.
*  I think that's an understudied
*  and under understood engineering problem.
*  There's been a psychologist have been studying it.
*  I think it's part like manipulating our mind
*  to believe things is a valuable engineering.
*  Like this is another degree of freedom
*  that can be controlled.
*  I like that, yeah, I think that's right.
*  I think, you know, there's something that humans seem to do
*  or maybe my dangerous introspection is,
*  I think we are able to make very simple models
*  that assume a lot about the world very quickly.
*  And then it takes us a lot more time like you're wrestling.
*  You know, you probably thought you knew
*  what you're doing with wrestling
*  and you were fairly functional as a complete wrestler.
*  And then you slowly got more expertise.
*  So maybe it's natural that our first level of defense
*  against seeing a new robot is to think of it
*  in our existing models of how humans and animals behave.
*  And it's just, as you spend more time with it,
*  then you'll develop more sophisticated models
*  that will appreciate the differences.
*  Exactly.
*  Can you say what does it take to control a robot?
*  Like what is the control problem of a robot?
*  And in general, what is a robot in your view?
*  Like how do you think of this system?
*  What is a robot?
*  What is a robot?
*  I told you ridiculous questions.
*  No, no, it's good.
*  I mean, there's standard definitions
*  of combining computation with some ability
*  to do mechanical work.
*  I think that gets us pretty close.
*  But I think robotics has this problem
*  that once things really work,
*  we don't call them robots anymore.
*  Like my dishwasher at home is pretty sophisticated,
*  beautiful mechanisms.
*  There's actually a pretty good computer,
*  a couple of chips in there doing amazing things.
*  We don't think of that as a robot anymore,
*  which isn't fair,
*  because then roughly it means that robotics
*  always has to solve the next problem
*  and doesn't get to celebrate its past successes.
*  I mean, even factory room floor robots
*  are super successful.
*  They're amazing.
*  But that's not the ones,
*  I mean, people think of them as robots,
*  but they don't, if you ask what are the successes of robotics,
*  somehow it doesn't come to your mind immediately.
*  So the definition of robot is a system
*  with some level of automation that fails frequently.
*  Something like, it's the computation plus mechanical work
*  and unsolved problem.
*  Solved problem, yeah.
*  So from a perspective of control and mechanics, dynamics,
*  what is a robot?
*  So there are many different types of robots.
*  The control that you need for a Jibo robot,
*  some robot that's sitting on your countertop
*  and interacting with you, but not touching you, for instance,
*  is very different than what you need for an autonomous car
*  or an autonomous drone.
*  It's very different than what you need for a robot
*  that's gonna walk or pick things up with its hands, right?
*  My passion has always been for the places
*  where you're interacting more,
*  you're doing more dynamic interactions with the world.
*  So walking, now manipulation.
*  And the control problems there are beautiful.
*  I think contact is one thing that differentiates them
*  from many of the control problems we've solved classically.
*  Right, the modern control grew up stabilizing fighter jets
*  that were passively unstable,
*  and there's like amazing success stories
*  from control all over the place.
*  Power grid, I mean, there's all kinds of,
*  it's everywhere that we don't even realize,
*  just like AI is now.
*  So you mentioned contact, like what's contact?
*  So an airplane is an extremely complex system
*  or a spacecraft landing or whatever,
*  but at least it has the luxury of things change
*  relatively continuously.
*  That's an oversimplification.
*  But if I make a small change in the command
*  I send to my actuator,
*  then the path that the robot will take
*  tends to change only by a small amount.
*  And there's a feedback mechanism here.
*  That's what we're talking about.
*  And there's a feedback mechanism.
*  And thinking about this as locally,
*  like a linear system, for instance,
*  I can use more linear algebra tools
*  to study systems like that,
*  generalizations of linear algebra to these smooth systems.
*  What is contact?
*  Robot has something very discontinuous that happens
*  when it makes or breaks,
*  when it starts touching the world.
*  And even the way it touches or the order of contacts
*  can change the outcome in potentially unpredictable ways.
*  Not unpredictable, but complex ways.
*  I do think there's a little bit of,
*  a lot of people will say that contact is hard in robotics,
*  even to simulate.
*  And I think there's a little bit of a,
*  there's truth to that,
*  but maybe a misunderstanding around that.
*  So what is limiting is that when we think about our robots
*  and we write our simulators,
*  we often make an assumption that objects are rigid.
*  And when it comes down,
*  that their mass moves all,
*  stays in a constant position relative to each other itself.
*  And that leads to some paradoxes
*  when you go to try to talk about
*  rigid body mechanics and contact.
*  And so for instance,
*  if I have a three legged stool with just,
*  imagine it comes to a point at the leg.
*  So it's only touching the world at a point.
*  If I draw my physics,
*  my high school physics diagram of this system,
*  then there's a couple of things that I'm given
*  by elementary physics.
*  I know if the system,
*  if the table is at rest,
*  if it's not moving,
*  zero velocities,
*  that means that the normal force,
*  all the forces are in balance.
*  So the force of gravity is being countered
*  by the forces that the ground is pushing on my table legs.
*  I also know since it's not rotating,
*  that the moments have to balance.
*  And since it can,
*  it's a three dimensional table,
*  it could fall in any direction.
*  It actually tells me uniquely
*  what those three normal forces have to be.
*  If I have four legs on my table,
*  four legged table,
*  and they were perfectly machined
*  to be exactly the right same height
*  and they're set down and the table's not moving,
*  then the basic conservation laws don't tell me,
*  there are many solutions for the forces
*  that the ground could be putting on my legs
*  that would still result in the table not moving.
*  Now the reason that seems fine
*  I could just pick one,
*  but it gets funny now because if you think about friction,
*  what we think about with friction is we,
*  our standard model says the amount of force
*  that the table will push back
*  if I were to now try to push my table sideways,
*  I guess I have a table here,
*  is proportional to the normal force.
*  So if I'm barely touching and I push, I'll slide,
*  but if I'm pushing more and I push, I'll slide less.
*  It's called Coulomb friction, is our standard model.
*  Now if you don't know what the normal force is
*  on the four legs and you push the table,
*  then you don't know what the friction forces are gonna be.
*  And so you can't actually tell,
*  the laws just aren't explicit yet
*  about which way the table's gonna go.
*  It could veer off to the left,
*  it could veer off to the right, it could go straight.
*  So the rigid body assumption of contact
*  leaves us with some paradoxes which are annoying
*  for writing simulators and for writing controllers.
*  We still do that sometimes because soft contact
*  is potentially harder numerically or whatever,
*  and the best simulators do both
*  or do some combination of the two.
*  But anyways, because of these kind of paradoxes,
*  there's all kinds of paradoxes in contact,
*  mostly due to these rigid body assumptions.
*  It becomes very hard to write the same kind of control laws
*  that we've been able to be successful with
*  for fighter jets.
*  We haven't been as successful
*  writing those controllers for manipulation.
*  And so you don't know what's going to happen
*  at the point of contact, at the moment of contact.
*  There are situations absolutely where you,
*  where our laws don't tell us.
*  So the standard approach, that's okay.
*  I mean, instead of having a differential equation,
*  you end up with a very simple model
*  equation, you end up with a differential inclusion,
*  it's called.
*  It's a set valued equation.
*  It says that I'm in this configuration,
*  I have these forces applied on me.
*  And there's a set of things that could happen, right?
*  And you can-
*  And those aren't continuous, I mean, what,
*  so when you're saying like non-smooth,
*  they're not only not smooth, but this is discontinuous?
*  The non-smooth comes in when I make or break
*  a new contact first, or when I transition
*  from stick to slip.
*  So you typically have static friction,
*  and then you'll start sliding,
*  and that'll be a discontinuous change in velocity,
*  for instance, especially if you come to rest or-
*  That's so fascinating.
*  Okay, so what do you do?
*  Sorry, I interrupted you.
*  That's fine.
*  What's the hope under so much uncertainty
*  about what's going to happen?
*  What are you supposed to do?
*  I mean, control has an answer for this.
*  Robust control is one approach,
*  but roughly, you can write controllers
*  which try to still perform the right task
*  despite all the things that could possibly happen.
*  The world might want the table to go this way and this way,
*  but if I write a controller that pushes a little bit more
*  and pushes a little bit, I can certainly make the table
*  go in the direction I want.
*  It just puts a little bit more of a burden
*  on the control system, right?
*  And this discontinuities do change the control system
*  because the way we write it down right now,
*  every different control configuration,
*  including sticking or sliding or parts of my body
*  that are in contact or not, looks like a different system.
*  And I think of them, I reason about them separately
*  or differently and the combinatorics of that blow up, right?
*  So I just don't have enough time to compute
*  all the possible contact configurations of my humanoid.
*  Interestingly, I mean, I'm a humanoid.
*  I have lots of degrees of freedom, lots of joints.
*  I've only been around for a handful of years.
*  It's getting up there, but I haven't had time in my life
*  to visit all of the states in my system,
*  certainly all the contact configurations.
*  So if step one is to consider
*  every possible contact configuration that I'll ever be in,
*  that's probably not a problem I need to solve, right?
*  Just as a small tangent, what's a contact configuration?
*  Just so we can enumerate, what are we talking about?
*  How many are there?
*  The simplest example maybe would be,
*  imagine a robot with a flat foot.
*  And we think about the phases of gait
*  where the heel strikes and then the front toe strikes,
*  and then you can heel up, toe off.
*  Those are each different contact configurations.
*  I only had two different contacts,
*  but I ended up with four different contact configurations.
*  Now, of course, my robot might actually have bumps on it
*  or other things, so it could be much more subtle than that.
*  But it's just even with one sort of box
*  interacting with the ground already in the plane
*  has that many, right?
*  If I was just even a 3D foot,
*  then probably my left toe might touch
*  just before my right toe and things get subtle.
*  Now, if I'm a dexterous hand
*  and I go to talk about just grabbing a water bottle,
*  if I have to enumerate every possible order
*  that my hand came into contact with the bottle,
*  then I'm dead in the water.
*  Any approach that we were able to get away with that
*  in walking, because we mostly touched the ground
*  at a small number of points, for instance,
*  and we haven't been able to get dexterous hands that way.
*  So you've mentioned that people think
*  that contact is really hard,
*  and that that's the reason that robotic manipulation
*  is problem is really hard.
*  Is there any flaws in that thinking?
*  So I think simulating contact is one aspect.
*  I know people often say that we don't,
*  that one of the reasons that we have a limit in robotics
*  is because we do not simulate contact accurately
*  in our simulators.
*  And I think that is,
*  the extent to which that's true
*  is partly because our simulators,
*  we haven't got mature enough simulators.
*  There are some things that are still hard, difficult,
*  that we should change.
*  But we actually, we know what the governing equations are.
*  They have some foibles, like this indeterminacy,
*  but we should be able to simulate them accurately.
*  We have incredible open source community in robotics,
*  but it actually just takes a professional engineering team
*  a lot of work to write a very good simulator like that.
*  Now, where does, I believe you've written, Drake?
*  There's a team of people.
*  I certainly spent a lot of hours on it myself.
*  Well, what is Drake, and what does it take
*  to create a simulation environment
*  for the kind of difficult control problems
*  we're talking about?
*  Right, so Drake is the simulator that I've been working on.
*  There are other good simulators out there.
*  I don't like to think of Drake as just a simulator,
*  because we write our controllers in Drake.
*  We write our perception systems a little bit in Drake,
*  but we write all of our low-level control
*  and even planning and optimization.
*  So it has optimization capabilities.
*  Absolutely, yeah.
*  I mean, Drake is three things, roughly.
*  It's an optimization library, which is, sits on,
*  it provides a layer of abstraction in C++ and Python
*  for commercial solvers.
*  You can write linear programs, quadratic programs,
*  you know, semi-definite programs, sums of squares programs,
*  the ones we've used, mixed integer programs,
*  and it will do the work to curate those
*  and send them to whatever the right solver is, for instance.
*  It provides a level of abstraction.
*  The second thing is a system modeling language,
*  a bit like LabView or Simulink,
*  where you can make block diagrams out of complex systems,
*  or it's like ROS in that sense,
*  where you might have lots of ROS nodes
*  that are each doing some part of your system,
*  but to contrast it with ROS,
*  we try to write, if you write a Drake system,
*  then you have to, it asks you to describe
*  a little bit more about the system.
*  If you have any state, for instance, in the system,
*  any variables that are gonna persist,
*  you have to declare them.
*  Parameters can be declared and the like,
*  but the advantage of doing that is that you can,
*  if you like, run things all on one process,
*  but you can also do control design against it.
*  You can do, I mean, simple things like
*  rewinding and playing back your simulations, for instance.
*  These things, you get some rewards
*  for spending a little bit more upfront cost
*  in describing each system.
*  And I was inspired to do that
*  because I think the complexity of Atlas, for instance,
*  is just so great.
*  And I think, although, I mean, ROS has been incredible,
*  absolute huge fan of what it's done
*  for the robotics community,
*  but the ability to rapidly put different pieces together
*  and have a functioning thing is very good.
*  But I do think that it's hard to think clearly
*  about a bag of disparate parts,
*  Mr. Potato Head kind of software stack.
*  And if you can ask a little bit more
*  out of each of those parts,
*  then you can understand the way they work better.
*  You can try to verify them and the like,
*  or you can do learning against them.
*  And then one of those systems, the last thing,
*  I said the first two things that Drake is,
*  but the last thing is that there is a set
*  of multi-body equations, rigid body equations
*  that is trying to provide a system that simulates physics.
*  And we also have renderers and other things,
*  but I think the physics component of Drake is special
*  in the sense that we have done excessive amount
*  of engineering to make sure
*  that we've written the equations correctly.
*  Every possible tumbling satellite or spinning top
*  or anything that we could possibly write as a test is tested.
*  We are making some, I think, fundamental improvements
*  on the way you simulate contact.
*  What does it take to simulate contact?
*  I mean, it just seems,
*  I mean, there's something just beautiful
*  the way you were explaining contact
*  and you were tapping your fingers on the table
*  while you're doing it.
*  Just-
*  Easily, right?
*  Easily, just not even,
*  it was helping you think, I guess.
*  You have this awesome demo of loading
*  or unloading a dishwasher,
*  just picking up a plate,
*  grasping it for the first time.
*  That just seems so difficult.
*  How do you simulate any of that?
*  So it was really interesting that what happened was that
*  we started getting more professional
*  about our software development
*  during the DARPA Robotics Challenge.
*  I learned the value of software engineering
*  and how to bridle complexity.
*  I guess that's what I want to somehow fight against
*  and bring some of the clear thinking of controls
*  into these complex systems we're building for robots.
*  Shortly after the DARPA Robotics Challenge,
*  Toyota opened a research institute,
*  TRI, Toyota Research Institute.
*  They put one of their, there's three locations.
*  One of them's just down the street from MIT.
*  I helped ramp that up
*  right at the end of my sabbatical, I guess.
*  So TRI has given me,
*  the TRI Robotics effort
*  has made this investment in simulation in Drake.
*  Michael Sherman leads a team there
*  of just absolutely top-notch dynamics experts
*  that are trying to write those simulators
*  that can pick up the dishes.
*  And there's also a team working on manipulation there
*  that is taking problems like loading the dishwasher
*  and we're using that to study these really hard corner cases
*  kind of problems in manipulation.
*  So for me, this, you know, simulating the dishes,
*  we could actually write a controller
*  if we just cared about picking up dishes in the sink once,
*  we could write a controller
*  without any simulation whatsoever
*  and we could call it done.
*  But we wanna understand like,
*  what is the path you take to actually get to
*  a robot that could perform that for any dish
*  in anybody's kitchen with enough confidence
*  that it could be a commercial product, right?
*  And it has deep learning perception in the loop.
*  It has complex dynamics in the loop.
*  It has controller, it has a planner.
*  And how do you take all of that complexity
*  and put it through this engineering discipline
*  and verification and validation process
*  to actually get enough confidence to deploy?
*  I mean, the DARPA challenge made me realize
*  that that's not something you throw over the fence
*  and hope that somebody will harden it for you,
*  that there are really fundamental challenges
*  in closing that last gap.
*  They're doing the validation and the testing.
*  I think it might even change the way we have to think about
*  the way we write systems.
*  What happens if you have the robot running lots of tests
*  and it screws up, it breaks a dish, right?
*  How do you capture that?
*  I said, you can't run the same simulation
*  or the same experiment twice on a real robot.
*  Do we have to be able to bring that one-off failure
*  back into simulation in order to change our controllers,
*  study it, make sure it won't happen again?
*  Is it enough to just try to add that to our distribution
*  and understand that on average,
*  we're gonna cover that situation again?
*  There's really subtle questions at the corner cases
*  that I think we don't yet have satisfying answers for.
*  How do you find the corner cases?
*  That's one kind of...
*  Do you think it's possible to create a systematized way
*  of discovering corner cases efficiently
*  in whatever the problem is?
*  Yes, I think we have to get better at that.
*  Control theory has for decades talked about
*  active experiment design.
*  So people call it curiosity these days.
*  It's roughly this idea of trying to exploration
*  or exploitation, but the active experiment design
*  is even more specific.
*  You could try to understand the uncertainty in your system
*  design the experiment that will provide
*  the maximum information to reduce that uncertainty.
*  If there's a parameter you wanna learn about,
*  what is the optimal trajectory I could execute
*  to learn about that parameter, for instance.
*  Scaling that up to something that has a deep network
*  in the loop and a planning in the loop is tough.
*  We've done some work with Matt O'Kelly and Amansi.
*  We've worked on some falsification algorithms
*  that are trying to do rare event simulation
*  that try to just hammer on your simulator.
*  And if your simulator is good enough,
*  you can spend a lot of time,
*  or you can write good algorithms that try to spend
*  most of their time in the corner cases.
*  So you basically imagine you're building an autonomous car
*  and you wanna put it in, I don't know,
*  downtown New Delhi all the time, right,
*  an accelerated testing.
*  If you can write sampling strategies,
*  which figure out where your controller's performing badly
*  in simulation and start generating lots of examples
*  around that, it's just the space of possible places
*  where things can go wrong is very big.
*  So it's hard to write those algorithms.
*  Yeah, rare event simulation is just a really
*  compelling notion, if it's possible.
*  We joked and we call it the black swan generator.
*  It's a black swan.
*  Because you don't just want the rare events,
*  you want the ones that are highly impactful.
*  I mean, that's the most, those are the most
*  sort of profound questions we ask of our world,
*  like what's the worst that can happen?
*  But what we're really asking isn't some kind of
*  computer science worst case analysis.
*  We're asking what are the millions of ways
*  this can go wrong?
*  And that's like our curiosity.
*  We humans, I think, are pretty bad at,
*  we just like run into it.
*  And I think there's a distributed sense
*  because there's now like 7.5 billion of us,
*  and so there's a lot of them,
*  and then a lot of them write blog posts
*  about the stupid thing they've done,
*  so we learn in a distributed way.
*  There's some.
*  I think that's gonna be important for robots too.
*  I mean, that's another massive theme
*  at Toyota Research for robotics,
*  is this fleet learning concept.
*  The idea that I, as a human,
*  I don't have enough time to visit all of my states.
*  It's very hard for one robot to experience all the things.
*  But that's not actually the problem we have to solve.
*  We're gonna have fleets of robots
*  that can have very similar appendages.
*  And at some point, maybe collectively,
*  they have enough data that their computational processes
*  should be set up differently than ours, right?
*  It's this vision of just,
*  I mean, all these dishwasher unloading robots.
*  I mean, that robot dropping a plate,
*  and a human looking at the robot, probably pissed off.
*  Yeah.
*  But that's a special moment to record.
*  I think one thing in terms of fleet learning,
*  and I've seen that because I've talked to a lot of folks
*  just like Tesla users or Tesla drivers.
*  They're another company
*  that's using this kind of fleet learning idea.
*  One hopeful thing I have about humans
*  is they really enjoy when a system improves, learns.
*  So they enjoy fleet learning.
*  And the reason it's hopeful for me
*  is they're willing to put up with something
*  that's kind of dumb right now.
*  And they're like, if it's improving,
*  they almost enjoy being part of the, like teaching it.
*  Almost like if you have kids,
*  you're teaching them something.
*  Right.
*  I think that's a beautiful thing
*  because that gives me hope
*  that we can put dumb robots out there.
*  I mean, the problem on the Tesla side with cars,
*  cars can kill you.
*  That makes the problem so much harder.
*  Dishwasher unloading is a little safe.
*  That's why home robotics is really exciting.
*  And just to clarify, I mean, for people who might not know,
*  I mean, TRI, Toyota Research Institute,
*  so they're, I mean, they're pretty well known
*  for like autonomous vehicle research,
*  but they're also interested in home robotics.
*  Yep.
*  There's a big group working on,
*  multiple groups working on home robotics.
*  It's a major part of the portfolio.
*  There's also a couple other projects
*  and advanced materials discovery,
*  using AI and machine learning to discover new materials
*  for car batteries and the like, for instance.
*  Yeah.
*  And that's been actually incredibly successful team.
*  There's new projects starting up too.
*  So-
*  Do you see a future of where like robots are in our home
*  and like robots that have like actuators
*  that look like arms in our home
*  or like, you know, more like humanoid type robots,
*  or is this, are we gonna do the same thing
*  that you just mentioned that, you know,
*  the dishwasher's no longer a robot.
*  We're going to just not even see them as robots.
*  But I mean, what's your vision of the home of the future?
*  10, 20 years from now, 50 years, if you get crazy.
*  Yeah, I think we already have Roombas cruising around.
*  We have, you know, Alexa's or Google homes
*  on our kitchen counter.
*  It's only a matter of time till they spring arms
*  and start doing something useful like that.
*  So I do think it's coming.
*  I think lots of people have lots of motivations
*  for doing it.
*  It's been super interesting actually learning
*  about Toyota's vision for it,
*  which is about helping people age in place.
*  Because I think that's not necessarily the first entry,
*  the most lucrative entry point,
*  but it's the problem maybe that we really need to solve
*  no matter what.
*  And so I think there's a real opportunity.
*  It's a delicate problem.
*  How do you work with people, help people,
*  keep them active, engaged, you know,
*  but improve their quality of life
*  and help them age in place, for instance?
*  It's interesting because older folks are also,
*  I mean, there's a contrast there because
*  they're not always the folks
*  who are the most comfortable with technology, for example.
*  So there's a division that's interesting there
*  that you can do so much good with a robot
*  for older folks,
*  but there's a gap to fill of understanding.
*  I mean, it's actually kind of beautiful.
*  Robot is learning about the human
*  and the human is kind of learning about this new robot thing.
*  And it's also with, at least with,
*  like when I talk to my parents about robots,
*  there's a little bit of a blank slate there too.
*  Like you can, I mean, they don't know anything about robotics.
*  So it's completely like wide open.
*  They don't have, they haven't,
*  my parents haven't seen Black Mirror.
*  So like they, it's a blank slate.
*  Here's a cool thing, like what can you do for me?
*  Yeah.
*  So it's an exciting space.
*  I think it's a really important space.
*  I do feel like, you know, a few years ago,
*  drones were successful enough in academia.
*  They kind of broke out and started an industry
*  and autonomous cars have been happening.
*  It does feel like manipulation in logistics, of course,
*  first, but in the home shortly after,
*  it seems like one of the next big things
*  that's gonna really pop.
*  So I don't think we talked about it,
*  but what's soft robotics?
*  So we talked about like rigid bodies.
*  Like if we can just linger on this whole touch thing.
*  Yeah, so what's soft robotics?
*  I told you that I really dislike the fact
*  that robots are afraid of touching the world
*  all over their body.
*  So there's a couple of reasons for that.
*  If you look carefully at all the places
*  that robots actually do touch the world,
*  they're almost always soft.
*  They have some sort of pad on their fingers
*  or a rubber sole on their foot.
*  But if you look up and down the arm,
*  we're just pure aluminum or something.
*  So that makes it hard actually.
*  In fact, hitting the table with your rigid arm
*  or nearly rigid arm has some of the problems
*  that we talked about in terms of simulation.
*  I think it fundamentally changes the mechanics of contact
*  when you're soft.
*  You turn point contacts into patch contacts,
*  which can have torsional friction.
*  You can have distributed load.
*  If I wanna pick up an egg,
*  right, if I pick it up with two points,
*  then in order to put enough force
*  to sustain the weight of the egg,
*  I might have to put a lot of force to break the egg.
*  If I envelop it with contact all around,
*  then I can distribute my force across the shell of the egg
*  and have a better chance of not breaking it.
*  So soft robotics is for me a lot about changing
*  the mechanics of contact.
*  Does it make the problem a lot harder?
*  Um, quite the opposite.
*  It changes the computational problem.
*  I think because of the, I think our world
*  and our mathematics has biased us towards rigid,
*  but it really should make things better in some ways, right?
*  It's a, I think the future is unwritten there.
*  But the other thing is-
*  Ultimately, sorry to interrupt,
*  but you think ultimately it will make things simpler
*  if we embrace the softness of the world.
*  It makes things smoother, right?
*  So the result of small actions is less discontinuous,
*  but it also means potentially less, you know,
*  instantaneously bad, for instance.
*  I won't necessarily contact something
*  and send it flying off.
*  The other aspect of it that just happens to dovetail
*  really well is that soft robotics tends to be a place
*  where we can embed a lot of sensors too.
*  So if you change your hardware and make it more soft,
*  then you can potentially have a tactile sensor,
*  which is measuring the deformation.
*  So there's a team at TRI that's working on soft hands,
*  and you get so much more information.
*  If you, you can put a camera behind the skin roughly
*  and get fantastic tactile information,
*  which is, it's super important.
*  Like in manipulation,
*  one of the things that really is frustrating
*  is if you work super hard on your head-mounted,
*  on your perception system for your head-mounted cameras,
*  and then you've identified an object,
*  you reach down to touch it,
*  and the first, the last thing that happens,
*  right before the most important time,
*  you stick your hand and you're occluding
*  your head-mounted sensors, right?
*  So in all the part that really matters,
*  all of your off-board sensors are occluded.
*  And really, if you don't have tactile information,
*  then you're blind in an important way.
*  So it happens that soft robotics and tactile sensing
*  tend to go hand in hand.
*  I think we've kind of talked about it,
*  but you taught a course on under-actuated robotics.
*  I believe that was the name of it, actually.
*  That's right.
*  Can you talk about it in that context?
*  What is under-actuated robotics?
*  Right, so under-actuated robotics is my graduate course.
*  It's online mostly now,
*  in the sense that the lectures are-
*  Several versions of it, I think.
*  Right, the YouTube-
*  It's really great, I recommend it highly.
*  Look on YouTube for the 2020 versions until March,
*  and then you have to go back to 2019, thanks to COVID.
*  No, I've poured my heart into that class.
*  And lecture one is basically explaining
*  what the word under-actuated means.
*  So people are very kind to show up,
*  and then maybe have to learn what the title of the course
*  means over the course of the first lecture.
*  That first lecture's really good.
*  You should watch it.
*  Thanks.
*  It's a strange name, but I thought it captured
*  the essence of what control was good at doing
*  and what control was bad at doing.
*  So what do I mean by under-actuated?
*  So a mechanical system has many degrees of freedom,
*  for instance.
*  I think of a joint as a degree of freedom,
*  and it has some number of actuators, motors.
*  So if you have a robot that's bolted to the table
*  that has five degrees of freedom and five motors,
*  then you have a fully-actuated robot.
*  If you take away one of those motors,
*  then you have an under-actuated robot.
*  Now why on earth, I have a good friend who likes to tease me,
*  he said, Russ, if you had more research funding,
*  would you work on fully-actuated robots?
*  Yeah.
*  The answer's no.
*  The world gives us under-actuated robots,
*  whether we like it or not.
*  I'm a human.
*  I'm an under-actuated robot,
*  even though I have more muscles
*  than my big degrees of freedom,
*  because I have, in some places,
*  multiple muscles attached to the same joint.
*  But still, there's a really important degree of freedom
*  that I have, which is the location
*  of my center of mass in space, for instance.
*  I can jump into the air,
*  and there's no motor that connects my center of mass
*  to the ground, in that case.
*  So I have to think about the implications
*  of not having control over everything.
*  The passive dynamic walkers are the extreme view of that,
*  where you've taken away all the motors,
*  and you have to let physics do the work.
*  But it shows up in all of the walking robots,
*  where you have to use some of the actuators
*  to push and pull even the degrees of freedom
*  that you don't have an actuator on.
*  That's referring to walking, if you're falling forward.
*  Is there a way to walk that's fully-actuated?
*  So it's a subtle point.
*  When you're in contact, and you have your feet on the ground,
*  there are still limits to what you can do.
*  Unless I have suction cups on my feet,
*  I cannot accelerate my center of mass towards the ground
*  faster than gravity,
*  because I can't get a force pushing me down.
*  But I can still do most of the things that I want to.
*  So you can get away with basically thinking
*  of the system as fully-actuated,
*  unless you suddenly need it to accelerate down super-fast.
*  But as soon as I take a step,
*  I get into more nuanced territory,
*  and to get to really dynamic robots,
*  or airplanes, or other things,
*  I think you have to embrace the under-actuated dynamics.
*  Manipulation, people think, is manipulation under-actuated?
*  Even if my arm is fully-actuated, I have a motor,
*  if my goal is to control the position
*  and orientation of this cup,
*  then I don't have an actuator for that directly.
*  So I have to use my actuators over here
*  to control this thing.
*  Now it gets even worse.
*  What if I have to button my shirt?
*  What are the degrees of freedom of my shirt?
*  I suddenly, that's a hard question to think about.
*  It kind of makes me queasy
*  as thinking about my state-space control ideas.
*  But actually those are the problems
*  that make me so excited about manipulation right now,
*  is that it breaks some of the,
*  it breaks a lot of the foundational control stuff
*  that I've been thinking about.
*  Is there, what are some interesting insights
*  you could say about trying to solve
*  an under-actuated control in an under-actuated system?
*  So I think the philosophy there
*  is let physics do more of the work.
*  The technical approach has been optimization.
*  So you typically formulate your decision-making for control
*  as an optimization problem,
*  and you use the language of optimal control,
*  and sometimes often numerical optimal control,
*  in order to make those decisions
*  and balance these complicated equations
*  and in order to control.
*  You don't have to use optimal control
*  to do under-actuated systems,
*  but that has been the technical approach
*  that has borne the most fruit in our,
*  at least in our line of work.
*  And there's some, so in under-actuated systems,
*  when you say let physics do some of the work,
*  so there's a kind of feedback loop
*  that observes the state that the physics brought you to.
*  So like you've, there's a perception there.
*  There's a feedback somehow.
*  Do you ever loop in like complicated perception systems
*  into this whole picture?
*  Right, right around the time of the DARPA challenge,
*  we had a complicated perception system
*  in the DARPA challenge.
*  We also started to embrace perception
*  for our flying vehicles at the time.
*  We had a really good project
*  on trying to make airplanes fly
*  at high speeds through forests.
*  Sirtash Karaman was on that project,
*  and it was a really fun team to work on.
*  He's carried it farther, much farther forward since then.
*  And that's using cameras for perception?
*  So that was using cameras.
*  That was, at the time, we felt like LIDAR was too heavy
*  and too power heavy to be carried on a light UAV,
*  and we were using cameras.
*  And that was a big part of it,
*  was just how do you do even stereo matching
*  at a fast enough rate with a small camera,
*  a small onboard compute.
*  Since then, we have now,
*  so the deep learning revolution unquestionably changed
*  what we can do with perception for robotics and control.
*  So in manipulation, we can address,
*  we can use perception in, I think, a much deeper way.
*  And we get into not only,
*  I think the first use of it, naturally,
*  would be to ask your deep learning system
*  to look at the cameras and produce the state,
*  which is like the pose of my thing, for instance.
*  But I think we've quickly found out
*  that that's not always the right thing to do.
*  Why is that?
*  Because what's the state of my shirt?
*  Imagine I've-
*  Is it very noisy, you mean?
*  If the first step of me trying to button my shirt
*  is estimate the full state of my shirt,
*  including what's happening in the back here,
*  whatever, whatever,
*  that's just not the right specification.
*  There are aspects of the state
*  that are very important to the task.
*  There are many that are unobservable
*  and not important to the task.
*  So you really need,
*  it begs new questions about state representation.
*  Another example that we've been playing with in lab
*  has been just the idea of chopping onions, okay?
*  Or carrots, turns out to be better.
*  So onions stink up the lab.
*  And they're hard to see in a camera.
*  But-
*  The details matter, yeah.
*  Details matter, you know?
*  So-
*  Chopping carrot.
*  If I'm moving around a particular object, right,
*  then I think about, oh,
*  it's got a position or an orientation in space,
*  that's the description I want.
*  Now, when I'm chopping an onion, okay,
*  the first chop comes down,
*  I have now 100 pieces of onion.
*  Does my control system really need to understand
*  the position and orientation
*  and even the shape of the 100 pieces of onion
*  in order to make a decision?
*  Probably not, you know?
*  And if I keep going, I'm just getting,
*  more and more is my state space getting bigger as I cut?
*  It's not right.
*  So-
*  What do you do?
*  I think there's a richer idea of state.
*  It's not the state that is given to us
*  by Lagrangian mechanics.
*  There is a proper Lagrangian state of the system,
*  but the relevant state for this is some latent state,
*  is what we call it in machine learning.
*  But, you know, there's some different state representation.
*  Some compressed representation, some-
*  And that's what I worry about saying compressed,
*  because it doesn't,
*  I don't mind that it's low dimensional or not,
*  but it has to be something that's easier to think about.
*  By us humans.
*  Or my algorithms.
*  Or the algorithms being like control, optimal control.
*  So for instance, if the contact mechanics
*  of all of those onion pieces
*  and all the permutations of possible touches
*  between those onion pieces, you know,
*  you can give me a high dimensional state representation.
*  I'm okay if it's linear.
*  But if I have to think about all the possible
*  shattering combinatorics of that,
*  then my robot's gonna sit there thinking
*  and the soup's gonna get cold or something.
*  So since you taught the course,
*  it kinda entered my mind, the idea of underactuated,
*  as really compelling to see the world in this kind of way.
*  Do you ever, you know, if you talk about onions
*  or you talk about the world with people in it in general,
*  do you see the world as basically an underactuated system?
*  Do you like often look at the world in this way?
*  Or is this overreach?
*  Underactuated is a way of life, man.
*  Exactly, I guess that's what I'm asking.
*  I do think it's everywhere.
*  I think in some places,
*  we already have natural tools to deal with it.
*  You know, it rears its head.
*  I mean, in linear systems, it's not a problem.
*  We just, like an underactuated linear system
*  is really not sufficiently distinct
*  from a fully actuated linear system.
*  It's a subtle point about when that becomes a bottleneck
*  in what we know how to do with control.
*  It happens to be a bottleneck,
*  although we've gotten incredibly good solutions now,
*  but for a long time, I felt that that was the key bottleneck
*  in legged robots.
*  And roughly now, the underactuated course is, you know,
*  me trying to tell people everything I can
*  about how to make Atlas do a backflip, right?
*  I have a second course now that I teach
*  in the other semesters, which is on manipulation.
*  And that's where we get into now more of the,
*  that's a newer class.
*  I'm hoping to put it online this fall completely.
*  And that's gonna have much more aspects
*  about these perception problems
*  and the state representation questions,
*  and then how do you do control?
*  And the thing that's a little bit sad
*  is that for me at least,
*  there's a lot of manipulation tasks
*  that people wanna do and should wanna do.
*  They could start a company with it and be very successful
*  that don't actually require you to think that much
*  about dynamics at all even,
*  but certainly underactuated dynamics.
*  Once I have, if I reach out and grab something,
*  if I can sort of assume it's rigidly attached to my hand,
*  then I can do a lot of interesting meaningful things
*  with it without really ever thinking about the dynamics
*  of that object.
*  So we've built systems that kind of reduce the need
*  for that, enveloping grasps and the like.
*  But I think the really good problems in manipulation.
*  So manipulation, by the way,
*  is more than just pick and place.
*  That's like a lot of people think of that, just grasping.
*  I don't mean that, I mean buttoning my shirt.
*  I mean tying shoelaces.
*  How do you program a robot to tie shoelaces?
*  And not just one shoe, but every shoe, right?
*  That's a really good problem.
*  It's tempting to write down
*  the infinite dimensional state of the laces.
*  That's probably not needed to write a good controller.
*  I know we could hand design a controller that would do it,
*  but I don't want that.
*  I wanna understand the principles
*  that would allow me to solve another problem
*  that's kind of like that.
*  But I think if we can stay pure in our approach,
*  then the challenge of tying anybody's shoes
*  is a great challenge.
*  That's a great challenge.
*  I mean, and the soft touch comes into play there.
*  That's really interesting.
*  Let me ask another ridiculous question on this topic.
*  How important is touch?
*  We haven't talked much about humans,
*  but I have this argument with my dad
*  where I think you can fall in love with a robot
*  based on language alone.
*  And he believes that touch is essential.
*  Touch and smell, he says.
*  In terms of robots connecting with humans,
*  we can go philosophical
*  in terms of a deep, meaningful connection, like love,
*  but even just collaborating in an interesting way,
*  how important is touch from an engineering perspective
*  and a philosophical one?
*  I think it's super important.
*  Even just in a practical sense,
*  if we forget about the emotional part of it,
*  but for robots to interact safely
*  while they're doing meaningful mechanical work
*  in the close contact with or vicinity
*  of people that need help,
*  I think we have to have them,
*  we have to build them differently.
*  They have to be afraid, not afraid of touching the world.
*  So I think Baymax is just awesome.
*  That's just like the movie of Big Hero 6
*  and the concept of Baymax, that's just awesome.
*  I think we should, and we have some folks at Toyota
*  that are trying to, Toyota Research that are trying
*  to build Baymax roughly.
*  And I think it's just a fantastically good project.
*  I think it will change the way people physically interact.
*  The same way, I mean, you gave a couple examples earlier,
*  but if the robot that was walking around my home
*  looked more like a teddy bear
*  and a little less like the Terminator,
*  that could change completely the way people perceive it
*  and interact with it.
*  And maybe they'll even wanna teach it, like you said, right?
*  You could not quite gamify it,
*  but somehow instead of people judging it
*  and looking at it as if it's not doing as well as a human,
*  they're gonna try to help out the cute teddy bear, right?
*  Who knows?
*  But I think we're building robots wrong
*  and being more soft and more contact is important, right?
*  Yeah, like all the magical moments
*  I can remember with robots.
*  Well, first of all, just visiting your lab and seeing Atlas,
*  but also Spotmini.
*  When I first saw Spotmini in person
*  and hung out with him, her, it,
*  I don't have trouble engendering robots.
*  I feel robotics people really say, oh, is it it?
*  I kinda like the idea that it's a her or him.
*  There's a magical moment, but there's no touching.
*  I guess the question I have, have you ever been,
*  have you had a human robot experience
*  where a robot touched you?
*  And it was like, wait, was there a moment
*  that you've forgotten that a robot is a robot?
*  And the anthropomorphization stepped in
*  and for a second you forgot that it's not human?
*  I mean, I think when you're in on the details,
*  then we of course anthropomorphized our work with Atlas,
*  but in verbal communication and the like,
*  I think we were pretty aware of it as a machine
*  that needed to be respected.
*  I actually, I worry more about the smaller robots
*  that could still move quickly if programmed wrong.
*  And we have to be careful actually about safety
*  and the like right now.
*  And that, if we build our robots correctly,
*  I think then a lot of those concerns could go away.
*  And we're seeing that trend.
*  We're seeing the lower cost, lighter weight arms now
*  that could be fundamentally safe.
*  I mean, I do think touch is so fundamental.
*  Ted Adelson is great.
*  He's a perceptual scientist at MIT.
*  And he studied vision most of his life.
*  And he said, when I had kids,
*  I expected to be fascinated by their perceptual development.
*  But what really, what he noticed was felt more impressive,
*  more dominant was the way that they would touch everything
*  and lick everything and pick things up,
*  stick it on their tongue and whatever.
*  And he said, watching his daughter
*  convinced him that actually he needed to study tactile,
*  sensing more.
*  So there's something very important.
*  I think it's a little bit also of the passive
*  versus active part of the world.
*  You can passively perceive the world,
*  but it's fundamentally different
*  if you can do an experiment.
*  And if you can change the world
*  and you can learn a lot more than a passive observer.
*  So you can in dialogue, that was your initial example,
*  you could have an active experiment exchange.
*  But I think if you're just a camera watching YouTube,
*  I think that's a very different problem
*  than if you're a robot that can apply force and touch.
*  I think it's important.
*  Yeah, I think it's just an exciting area of research.
*  I think you're probably right
*  that this hasn't been under researched.
*  To me as a person who's captivated by the idea
*  of human robot interaction,
*  it feels like such a rich opportunity to explore touch.
*  Not even from a safety perspective,
*  but like you said, the emotional too.
*  I mean, safety comes first,
*  but the next step is like a real human connection.
*  Even in the industrial setting,
*  it just feels like it's nice for the robot.
*  I don't know, you might disagree with this,
*  but because I think it's important
*  to see robots as tools often, but I don't know.
*  I think they're just always going to be more effective
*  once you humanize them.
*  It's convenient now to think of them as tools
*  because we wanna focus on the safety,
*  but I think ultimately to create a good experience
*  for the worker, for the person,
*  there has to be a human element.
*  I don't know, for me, it feels like an industrial robotic arm
*  would be better if it has a human element.
*  I think like Rethink Robotics had that idea
*  with the Baxter and having eyes and so on.
*  I don't know, I'm a big believer in that.
*  It's not my area, but I am also a big believer.
*  Do you have an emotional connection to Atlas?
*  Like, do you miss him?
*  I mean, yes.
*  I don't know if I'd more so than if I had
*  a different science project that I'd worked on super hard.
*  But yeah, I mean, the robot,
*  we basically had to do heart surgery on the robot
*  in the final competition because we melted the core.
*  There was something about watching that robot hanging there.
*  We know we had to compete with it in an hour
*  and it was getting its guts ripped out.
*  Those are all historic moments.
*  I think if we look back like 100 years from now,
*  yeah, I think those are important moments in robotics.
*  I mean, these are the early days.
*  You look at the early days
*  of a lot of scientific disciplines.
*  They look ridiculous, they're full of failure.
*  But it feels like robotics will be important
*  in the coming 100 years.
*  And these are the early days.
*  So I think a lot of people are,
*  look at a brilliant person such as yourself
*  and are curious about the intellectual journey they've took.
*  Is there maybe three books, technical, fiction,
*  philosophical that had a big impact on your life
*  that you would recommend perhaps others reading?
*  Yeah, so I actually didn't read that much as a kid,
*  but I read fairly voraciously now.
*  There are some recent books that if you're interested
*  in this kind of topic,
*  like AI Superpowers by Kai-Fu Lee is just a fantastic read.
*  You must read that.
*  Yuval Harari, I think that can open your mind.
*  Sapiens.
*  Sapiens.
*  Sapiens is the first one, Homo Deus is the second, yeah.
*  We mentioned The Black Swan by Taleb.
*  I think that's a good sort of mind opener.
*  I actually, so there's maybe
*  more controversial recommendation I could give.
*  Great, we love lectures.
*  In some sense, it's so classical it might surprise you.
*  But I actually recently read Mortimer Adler's
*  How to Read a Book.
*  Not so long, it was a while ago.
*  But some people hate that book.
*  I loved it.
*  I think we're in this time right now where,
*  boy, we're just inundated with research papers
*  that you could read on archive with limited peer review
*  and just this wealth of information.
*  I don't know, I think the passion of what you can get
*  out of a book, a really good book or a really good paper,
*  if you find it, the attitude, the realization
*  that you're only gonna find a few
*  that really are worth all your time.
*  But then once you find them, you should just dig in
*  and understand it very deeply and it's worth marking it up
*  and having the hard copy, writing in the side notes,
*  side margins.
*  I think that was really, I read it at the right time
*  where I was just feeling just overwhelmed
*  with really low quality stuff, I guess.
*  And similarly, I'm just giving more than three now.
*  I'm sorry if I've exceeded my quota.
*  But on that topic just real quick is,
*  so basically finding a few companions
*  to keep for the rest of your life
*  in terms of papers and books and so on.
*  And those are the ones, like not doing,
*  what is it, FOMO, fear missing out,
*  constantly trying to update yourself,
*  but really deeply making a life journey
*  of studying a particular paper, essentially, set of papers.
*  Yeah, I think when you really find something,
*  which a book that resonates with you
*  might not be the same book that resonates with me,
*  but when you really find one that resonates with you,
*  I think the dialogue that happens,
*  and I loved that Adler was saying,
*  I think Socrates and Plato say,
*  the written word is never gonna capture
*  the beauty of dialogue, right?
*  But Adler says, no, no.
*  A really good book is a dialogue between you and the author,
*  and it crosses time and space.
*  I don't know, I think it's a very romantic,
*  there's a bunch of specific advice
*  which you can just gloss over,
*  but the romantic view of how to read
*  and really appreciate it is so good.
*  And similarly, teaching.
*  I thought a lot about teaching.
*  And so Isaac Asimov, great science fiction writer,
*  has also actually spent a lot of his career
*  writing nonfiction, right?
*  His memoir is fantastic.
*  He was passionate about explaining things, right?
*  He wrote all kinds of books
*  on all kinds of topics in science.
*  He was known as the great explainer.
*  And I do really resonate with his style
*  and just his way of talking about,
*  you know, by communicating and explaining to something
*  is really the way that you learn something.
*  I think I think about problems very differently
*  because of the way I've been given the opportunity
*  to teach them at MIT.
*  We have questions asked, you know,
*  the fear of the lecture, the experience of the lecture
*  and the questions I get and the interactions
*  just forces me to be rock solid on these ideas
*  in a way that I didn't have that.
*  I don't know, I would be in a different intellectual space.
*  Also video, does that scare you
*  that your lectures are online
*  and people like me in sweatpants can sit,
*  sipping coffee and watch, watch you give lectures?
*  I think it's great.
*  I do think that something's changed right now,
*  which is, you know, right now we're giving lectures
*  over Zoom, I mean, giving seminars over Zoom
*  and everything.
*  I'm trying to figure out, I think it's a new medium.
*  Do you think it's as possibilities?
*  I'm trying to figure out how to exploit it.
*  Yeah, I've been quite cynical
*  about the human to human connection over that medium,
*  but I think that's because it hasn't been explored fully
*  and teaching is a different thing.
*  Every lecture is a, I'm sorry, every seminar even,
*  I think every talk I give,
*  I, you know, it's an opportunity to give that differently.
*  I can deliver content directly into your browser.
*  You have a WebGL engine right there.
*  I could, I can throw 3D content into your browser
*  while you're listening to me, right?
*  Yeah.
*  And I can assume that you have a, you know,
*  at least a powerful enough laptop or something to watch Zoom
*  while I'm doing that, while I'm giving a lecture.
*  That's a new communication tool
*  that I didn't have last year, right?
*  And I think robotics can potentially benefit a lot
*  from teaching that way.
*  We'll see.
*  It's gonna be an experiment this fall.
*  It's interesting.
*  I'm thinking a lot about it.
*  Yeah, and also like the length of lectures
*  or the length of like, there's something,
*  so like, I guarantee you, you know,
*  it's like 80% of people who started listening
*  to our conversation are still listening to now,
*  which is crazy to me.
*  But so there's a patience and interest in long form content,
*  but at the same time, there's a magic to forcing yourself
*  to condense an idea to the shortest possible.
*  Shortest possible like clip.
*  It can be part of a longer thing,
*  but like just like really beautifully condensed an idea.
*  There's a lot of opportunity there
*  that's easier to do in remote with, I don't know,
*  with editing too.
*  Editing is an interesting thing.
*  Like what, you know, when most professors don't get,
*  when they give a lecture,
*  you don't get to go back and edit out parts.
*  Like crisp it up a little bit.
*  That's also, it can do magic.
*  Like if you remove like five to 10 minutes
*  from an hour lecture, it can actually,
*  it can make something special of a lecture.
*  I've seen that in myself.
*  And in others too,
*  cause I edit other people's lectures to extract clips.
*  It's like there's certain tangents that lose,
*  they're not interesting.
*  They're mumbling, they're just not,
*  they're not clarifying, they're not helpful at all.
*  And once you remove them, it's just, I don't know.
*  Editing can be magic.
*  It takes a lot of time.
*  Yeah, it takes, it depends like what is teaching.
*  You have to ask.
*  Yeah.
*  Yeah.
*  Cause I find the editing process is also beneficial
*  as for teaching, but also for your own learning.
*  I don't know if, have you watched yourself?
*  Yeah, sure.
*  Have you watched those videos?
*  I mean, not all of them.
*  It could be painful.
*  Yeah.
*  And to see like how to improve.
*  So do you find that, I know you segment your podcast.
*  Do you think that helps people
*  with the attention span aspect of it?
*  Or is it-
*  Segment like sections like-
*  Yeah, we're talking about this topic, whatever.
*  No, no, that just helps me.
*  It's actually bad.
*  So, and you've been incredible.
*  So I'm learning, like I'm afraid of conversation.
*  This is even today, I'm terrified of talking to you.
*  I mean, it's something I'm trying to remove for myself.
*  A guy, I mean, I've learned from a lot of people,
*  but really it's been a few people
*  who's been inspirational to me in terms of conversation.
*  Whatever people think of him,
*  Joe Rogan has been inspirational to me
*  because comedians have been too.
*  Being able to just have fun and enjoy themselves
*  and lose themselves in conversation.
*  That requires you to be a great storyteller,
*  to be able to pull a lot of different pieces
*  of information together,
*  but mostly just to enjoy yourself in conversations.
*  And I'm trying to learn that.
*  These notes are, you see me looking down,
*  that's like a safety blanket
*  that I'm trying to let go of more and more.
*  Cool.
*  So that's, people love just regular conversation.
*  That's what they, the structure is like, whatever.
*  I would say, I would say maybe like 10 to,
*  so there's a bunch of,
*  there's probably a couple thousand PhD students
*  listening to this right now, right?
*  And they might know what we're talking about,
*  but there is somebody, I guarantee you right now,
*  in Russia, some kid who's just like,
*  who's just smoked some weed, is sitting back,
*  and just enjoying the hell out of this conversation.
*  Not really understanding,
*  he kind of watched some Boston Dynamics videos,
*  he's just enjoying it.
*  And I salute you, sir.
*  No, but just like there's so much variety of people
*  that just have curiosity about engineering,
*  about sciences, about mathematics.
*  And also like I should,
*  I mean, enjoying it is one thing,
*  but I also often notice it inspires people to,
*  there's a lot of people who are like
*  in their undergraduate studies trying to figure out what,
*  trying to figure out what to pursue.
*  And these conversations can really spark
*  the direction of their life.
*  And in terms of robotics, I hope it does,
*  because I'm excited about the possibilities
*  of what robotics brings.
*  On that topic,
*  do you have advice?
*  Like what advice would you give
*  to a young person about life?
*  A young person about life,
*  or a young person about life and robotics?
*  It could be in robotics, it could be in life in general.
*  It could be career, it could be relationship advice,
*  it could be running advice, just like,
*  that's one of the things I see,
*  like we talked to like 20 year olds,
*  they're like, how do I do this thing?
*  What do I do?
*  If they come up to you, what would you tell them?
*  I think it's an interesting time to be a kid these days.
*  Everything points to this being sort of
*  a winner take all economy and the like.
*  I think the people that will really excel,
*  in my opinion, are gonna be the ones
*  that can think deeply about problems.
*  You have to be able to ask questions agilely
*  and use the internet for everything it's good for
*  and stuff like this.
*  And I think a lot of people will develop those skills.
*  I think the leaders,
*  thought leaders, robotics leaders, whatever,
*  are gonna be the ones that can do more
*  and they can think very deeply and critically.
*  And that's a harder thing to learn.
*  I think one path to learning that is through mathematics,
*  through engineering.
*  I would encourage people to start math early.
*  I mean, I didn't really start.
*  I mean, I was always in the better math classes
*  that I could take, but I wasn't pursuing
*  super advanced mathematics or anything like that
*  until I got to MIT.
*  I think MIT lit me up and really started
*  the life that I'm living now.
*  But yeah, I really want kids to dig deep,
*  really understand things, building things too.
*  I mean, pull things apart, put them back together.
*  Like that's just such a good way to really understand things
*  and expect it to be a long journey, right?
*  Because you don't have to know everything.
*  You're never gonna know everything.
*  So think deeply and stick with it.
*  Enjoy the ride, but just make sure you're not,
*  yeah, just make sure you're stopping
*  to think about why things work.
*  It's true, it's easy to lose yourself
*  in the distractions of the world.
*  We're overwhelmed with content right now,
*  but you have to stop and pick some of it
*  and really understand it.
*  Yeah, on the book point, I've read Animal Farm
*  by George Orwell, A Ridiculous Number of Times.
*  So for me, like that book, I don't know
*  if it's a good book in general,
*  but for me, it connects deeply somehow.
*  It somehow connects, so I was born in the Soviet Union,
*  so it connects to me to the entirety of the history
*  of the Soviet Union and to World War II
*  and to the love and hatred and suffering that went on there
*  and the corrupting nature of power and greed
*  and just somehow, that book has taught me more about life
*  than anything else, even though it's just a silly,
*  childlike book about pigs.
*  I don't know why, it just connects and inspires.
*  There's a few technical books too on algorithms
*  that you return to often.
*  I'm with you.
*  Yeah, and I've been losing that because of the internet.
*  I've been going on archive and blog posts and GitHub
*  and the new thing of you lose your ability
*  to really master an idea.
*  Exactly right.
*  What's a fond memory from childhood?
*  When baby Ross Tedrick.
*  Well, I guess I just said that
*  at least my current life began when I got to MIT
*  if I have to go farther than that.
*  Yeah, what was, was there a life before MIT?
*  Oh, absolutely, but let me actually tell you
*  what happened when I first got to MIT
*  because that I think might be relevant here,
*  but I had taken a computer engineering degree at Michigan.
*  I enjoyed it immensely, learned a bunch of stuff.
*  I liked computers, I liked programming,
*  but when I did get to MIT and started working
*  with Sebastian Sung, theoretical physicist,
*  computational neuroscientist,
*  the culture here was just different.
*  It demanded more of me, certainly mathematically
*  and in the critical thinking.
*  And I remember the day that I borrowed one of the books
*  from my advisor's office and walked down
*  to the Charles River and was like,
*  I'm getting my butt kicked.
*  And I think that's gonna happen to everybody
*  who's doing this kind of stuff, right?
*  I think I expected you to ask me the meaning of life.
*  I think that the, somehow I think that's gotta be part of it.
*  Doing hard things?
*  Yeah.
*  Did you consider quitting at any point?
*  Did you consider this isn't for me?
*  No, never that.
*  I mean, I was working hard, but I was loving it.
*  I think there's this magical thing where you,
*  I'm lucky to surround myself with people that basically,
*  almost every day I'll see something,
*  I'll be told something or something that I realized,
*  wow, I don't understand that.
*  And if I could just understand that,
*  there's something else to learn
*  that if I could just learn that thing,
*  I would connect another piece of the puzzle.
*  And I think that is just such an important aspect
*  and being willing to understand what you can and can't do
*  and loving the journey of going
*  and learning those other things.
*  I think that's the best part.
*  I don't think there's a better way to end it.
*  Russ, you've been an inspiration to me
*  since I showed up at MIT.
*  Your work has been an inspiration to the world.
*  This conversation was amazing.
*  I can't wait to see what you do next
*  with robotics, home robots.
*  I hope to see your work in my home one day.
*  So thanks so much for talking today.
*  It's been awesome.
*  Cheers.
*  Thanks for listening to this conversation
*  with Russ Tedrick and thank you to our sponsors,
*  Magic Spoon Cereal, BetterHelp and ExpressVPN.
*  Please consider supporting this podcast
*  by going to magicspoon.com slash Lex
*  and using code Lex at checkout,
*  going to betterhelp.com slash Lex
*  and signing up at expressvpn.com slash Lex pod.
*  Click the links, buy the stuff, get the discount.
*  It really is the best way to support this podcast.
*  If you enjoy this thing, subscribe on YouTube,
*  review it with five stars on Apple Podcasts,
*  support it on Patreon or connect with me
*  on Twitter at Lex Friedman, spelled somehow
*  without the E, just F-R-I-D-M-A-N.
*  And now let me leave you with some words
*  from Neil deGrasse Tyson talking about robots in space
*  and the emphasis we humans put
*  on human-based space exploration.
*  Robots are important.
*  If I had to paint this hat, I would say just send robots.
*  I'll stay down here and get the data.
*  But nobody's ever given a parade for a robot.
*  Nobody's ever named a high school after a robot.
*  So when I don my public educator hat,
*  I have to recognize the elements of exploration
*  that excite people.
*  It's not only the discoveries and the beautiful photos
*  that come down from the heavens.
*  It's the vicarious participation in discovery itself.
*  Thank you for listening and hope to see you next time.
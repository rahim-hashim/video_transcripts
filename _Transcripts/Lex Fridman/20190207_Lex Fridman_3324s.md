---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 3324s
Video Keywords: []
Video Views: 38915
Video Rating: None
---

# Kyle Vogt: Cruise Automation | Lex Fridman Podcast #14
**Lex Fridman:** [February 07, 2019](https://www.youtube.com/watch?v=YUYagvESisE)
*  The following is a conversation with Kyle Vogt. He's the president and the CTO of Cruise Automation,
*  leading an effort to solve one of the biggest robotics challenges of our time, vehicle automation.
*  He's a co-founder of two successful companies, Twitch and Cruise, that have each sold for a
*  billion dollars. And he's a great example of the innovative spirit that flourishes in Silicon Valley
*  and now is facing an interesting and exciting challenge of matching that spirit with the
*  mass production and the safety-centered culture of a major automaker like General Motors.
*  This conversation is part of the MIT Artificial General Intelligence series
*  and the Artificial Intelligence podcast. If you enjoy it, please subscribe on YouTube,
*  iTunes, or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D. And now,
*  here's my conversation with Kyle Vogt. You grew up in Kansas, right?
*  Yeah, and I just saw that picture you had hidden over there, so I'm a little bit worried about that now.
*  Yeah, so in high school in Kansas City, you joined Shawnee Mission North High School Robotics Team.
*  Yeah.
*  Now, that wasn't your high school.
*  That's right. That was the only high school in the area that had a teacher who was willing
*  to sponsor our first robotics team.
*  I was going to troll you a little bit.
*  Jog you a little bit.
*  Yep.
*  With that kid.
*  I was trying to look super cool and intense.
*  You did.
*  Because this was BattleBots. This is serious business. So we're standing there with a welded
*  steel frame and looking tough.
*  So go back there. What is that jury to robotics?
*  Well, I think I've been trying to figure this out for a while, but I've always liked building
*  things with Legos. And when I was really, really young, I wanted the Legos that had motors and
*  other things. And then Lego Mindstorms came out. And for the first time, you could program
*  Lego contraptions. And I think things just sort of snowballed from that.
*  But I remember seeing the BattleBots TV show on Comedy Central and thinking,
*  that is the coolest thing in the world. I want to be a part of that.
*  And not knowing a whole lot about how to build these 200 pound fighting robots.
*  So I sort of obsessively pored over the internet forums where all the creators for BattleBots
*  would sort of hang out and talk about, document their build progress and everything.
*  And I think I read, I must have read like tens of thousands of forum posts from basically
*  everything that was out there on what these people were doing.
*  And eventually sort of triangulated how to put some of these things together.
*  And ended up doing BattleBots, which was like 13 or 14, which was pretty awesome.
*  I'm not sure if the show's still running. So BattleBots is,
*  so there's not an artificial intelligence component. It's remotely controlled.
*  And it's almost like a mechanical engineering challenge of building things that can be broken.
*  They're radio controlled. And I think that they allowed some limited form of autonomy.
*  But in a two minute match, and the way these things ran, you're really doing
*  yourself a disservice by trying to automate it versus just do the practical thing,
*  which is drive it yourself. And there's an entertainment aspect,
*  just going on YouTube, there's like some of them wield an axe. Some of them,
*  I mean, there's that fun. So what drew you to that aspect? Was it the mechanical engineering?
*  Was it the dream to create Frankenstein and sentient being? Or was it just like the Lego,
*  you like tinkering with stuff?
*  I mean, that was just building something. I think the idea of this radio controlled machine
*  that can do various things, if it has like a weapon or something was pretty interesting.
*  I agree, it doesn't have the same appeal as autonomous robots, which I sort of gravitated
*  towards later on. But it was definitely an engineering challenge. Because everything you
*  did in that competition was pushing components to their limits. So we would buy these $40 DC
*  motors that came out of a winch, like on the front of a pickup truck or something. And we'd
*  power the car with those and we'd run them at like double or triple their rated voltage.
*  They immediately start overheating. But for that two minute match, you can get
*  a significant increase in the power output of those motors before they burn out.
*  And so you're doing the same thing for your battery packs, all the materials in the system.
*  And I think there was something intrinsically interesting about just seeing where things break.
*  And did you offline see where they break? Did you take it to the testing point? Like,
*  how did you know two minutes? Or was there a reckless, let's just go with it and see?
*  We weren't very good at BattleBots. We lost all of our matches the first round.
*  The one I built first, both of them were these wedge shaped robots, because the wedge,
*  even though it's sort of boring to look at, is extremely effective. You drive towards another
*  robot and the front edge of it gets under them and then they sort of flip over, kind of like a
*  door stopper. And the first one had a pneumatic polished stainless steel spike on the front that
*  would shoot out about eight inches. The purpose of which is what?
*  Pretty ineffective actually, but it looks cool.
*  Was it to help with the lift?
*  No, it was just to try to poke holes in the other robot. And then the second time I did it,
*  which is the following, I think maybe 18 months later, we had a titanium axe with a hardened
*  steel tip on it that was powered by a hydraulic cylinder, which we were activating with liquid CO2,
*  which had its own set of problems.
*  So great. So that's kind of on the hardware side. I mean, at a certain point, there must have been
*  born a fascination on the software side. So what was the first piece of code you've written?
*  Go back there, see what language was it? What was that? Was it Emacs? Vim? Was it a more
*  respectable modern ID? Do you remember any of this?
*  Yeah. Well, I remember, I think maybe when I was in third or fourth grade, the school I was at,
*  elementary school had a bunch of Apple II computers, and we'd play games on those. And
*  I remember every once in a while, something would crash or wouldn't start up correctly,
*  and it would dump you out to what I later learned was like sort of a command prompt.
*  And my teacher would come over and type, actually remember this to this day for some reason,
*  like PR number six, or PR pound six, which is peripheral six, which is the disk drive,
*  which would fire up the disk and load the program. And I just remember thinking, wow,
*  she's like a hacker, like teach me these codes, error codes, is what I called them at the time.
*  But she had no interest in that. So it wasn't until I think about fifth grade that I had a school
*  where you could actually go on these Apple IIs and learn to program. And so it was all in basic,
*  where every line numbers are all number, every line is numbered, and you have to leave enough
*  space between the numbers so that if you want to tweak your code, you go back and if the first line
*  was 10 and the second line is 20, now you have to go back and insert 15. And if you need to add code
*  in front of that, 11 or 12, and you hope you don't run out of line numbers and have to redo the whole
*  thing. And there's go to statements? Yeah, go to and it's very basic, maybe hence the name, but
*  a lot of fun. And that was like, that was, you know, that's when, you know, when you first program,
*  you see the magic of it. It's like, it just, just like this world opens up with, you know,
*  endless possibilities for the things you could build or, or accomplish with that computer.
*  So you got the bug then. So even starting with basic and then what C plus plus throughout,
*  well, what did you, was there a computer program and computer science classes in high school?
*  Not, not where I went. So it was self-taught, but I did a lot of programming. The thing that,
*  you know, sort of pushed me in the path of eventually working on self-driving cars is
*  actually one of these really long trips driving from my house in Kansas to, I think Las Vegas,
*  where we did the Battlebots competition. And I had just gotten my, I think my learner's permit or
*  early driver's permit. And so I was driving this, you know, 10 hour stretch across Western Kansas,
*  where it's just, you're going straight on a highway and it is mind numbingly boring.
*  And I remember thinking even then with my sort of mediocre programming background, that this is
*  something that a computer can do, right? Let's take a picture of the road. Let's find the yellow
*  lane markers and, you know, steer the wheel. And, you know, later I'd come to realize this had been
*  done, you know, since, since the eighties or the seventies or even earlier, but I still wanted to
*  do it. And sort of immediately after that trip switched from sort of Battlebots, which is more
*  radio controlled machines to thinking about building, you know, autonomous vehicles of some
*  scale start off with really small electric ones and then, you know, progress to what we're doing
*  now. So what was your view of artificial intelligence at that point? What did you think? So this is,
*  before there's been waves in artificial intelligence, right? The current wave with
*  deep learning makes people believe that you can solve in a really rich, deep way, the computer
*  vision perception problem. But like in, before the deep learning craze, you know, how do you
*  think about how would you even go about building a thing that perceives itself in the world,
*  localize itself in the world, moves around the world? Like when you were younger, I mean,
*  what was your thinking about it? Well, prior to deep neural networks or convolutional neural
*  analysis, these modern techniques we have, or at least ones that are in use today, it was all
*  heuristic space. And so like old school image processing, and I think extracting, you know,
*  yellow lane markers out of an image of a road is one of the problems that lends itself reasonably
*  well to those heuristic based methods, you know, like just do a threshold on the color yellow and
*  then try to fit some lines to that using a Huff Transform or something and then go from there.
*  Traffic light detection and stop sign detection, red, yellow, green. And I think you could,
*  I mean, if you wanted to do a full, I was just trying to make something that would stay
*  in between the lanes on a highway. But if you wanted to do the full,
*  the full, you know, set of capabilities needed for a driverless car, I think you could, and we'd
*  done this at Cruise, you know, in the very first days, you can start off with a really simple,
*  you know, human written heuristic just to get the scaffolding in place for your system.
*  Traffic light detection, probably a really simple, you know, color thresholding on day one,
*  just to get the system up and running before you migrate to, you know, a deep learning based
*  technique or something else. And, you know, back when I was doing this, my first one, it was on a
*  Pentium 233 megahertz computer. And I think I wrote the first version in basic, which is like
*  an interpreted language. It's extremely slow because that's the thing I knew at the time.
*  And so there was no chance at all of using, there's no computational power to do any sort
*  of reasonable deep nets like you have today. So I don't know what kids these days are doing.
*  Are kids these days, you know, at age 13 using neural networks in their garage? I mean, that
*  would be awesome. I get emails all the time from, you know, like 11, 12 year olds saying I'm having,
*  you know, I'm trying to follow this TensorFlow tutorial and I'm having this problem. And the
*  general approach in the deep learning community is of extreme optimism of, as opposed to, you
*  mentioned like heuristics, you can separate the autonomous driving problem into modules and try
*  to solve it sort of rigorously, or you can just do it end to end. And most people just kind of
*  love the idea that, you know, us humans do it end to end. We just perceive and act. We should be
*  able to use that, do the same kind of thing with neural nets. And that kind of thinking,
*  you don't want to criticize that kind of thinking because eventually they will be right.
*  And so it's exciting. And especially when they're younger, to explore that
*  is a really exciting approach. But yeah, it's changed the language, the kind of stuff you're
*  tinkering with. It's kind of exciting to see when these teenagers grow up. Yeah, I can only imagine
*  if your starting point is, you know, Python and TensorFlow at age 13, where you end up, you know,
*  after 10 or 15 years of that. That's pretty cool. Because of GitHub, because the state of the tools
*  for solving most of the major problems in artificial intelligence are within a few lines
*  of code for most kids. And that's incredible to think about also on the entrepreneurial side.
*  And on that point, was there any thought about entrepreneurship before you came to college?
*  Is sort of doing your building this into a thing that impacts the world on a large scale?
*  Yeah, I've always wanted to start a company. I think that's, you know, just a cool concept
*  of creating something and exchanging it for value or creating value, I guess. So in high school,
*  I was trying to build like, you know, servo motor drivers, little circuit boards and sell them online,
*  or other other things like that. And certainly knew at some point, I wanted to do a startup,
*  but it wasn't really, I'd say until college until I felt like I had the
*  I guess the right combination of the environment, the smart people around you,
*  and some free time and a lot of free time at MIT.
*  So you came to MIT as an undergrad 2004. That's right.
*  And that's when the first DARPA Grand Challenge was happening. Yeah, the timing of that is
*  beautifully poetic. So how did you get yourself involved in that one?
*  Originally, there wasn't a official entry. Yeah, faculty sponsored thing. And so a bunch of
*  undergrads, myself included, started meeting and got together and tried to haggle together some
*  sponsorships. We got a vehicle donated a bunch of sensors, and tried to put something together.
*  And so we had our team was probably mostly freshmen and sophomores, you know, which was
*  not really a fair, fair fight against maybe the, you know, postdoc and faculty led teams from other
*  schools. But we, we got something up and running, we had our vehicle drive by wire and, you know,
*  very, very basic control and things. But on the day of the qualifying,
*  sort of pre-qualifying round, the one and only steering motor that we had purchased, the thing
*  that we had, you know, retrofitted to turn the steering wheel on the truck,
*  died. And so our vehicle was just dead in the water, couldn't steer. So we didn't make it very
*  far. On the hardware side. So was there a software component? Was there, like, how did your view of
*  autonomous vehicles in terms of artificial intelligence evolve in this moment? I mean,
*  you know, like you said, from the 80s has been autonomous vehicles, but really that was the
*  birth of the modern wave, the thing that captivated everyone's imagination that we can actually do
*  this. So what, how were you captivated in that way? So how did your view of autonomous vehicles
*  change at that point? I'd say at that point in time, it was, it was a curiosity as in like,
*  is this really possible? And I think that was generally the spirit and the purpose of that
*  original DARPA Grand Challenge, which was to just get a whole bunch of really brilliant people
*  exploring the space and pushing the limits. And I think like to this day, that DARPA challenge with
*  its, you know, million dollar prize pool was probably one of the most effective, you know,
*  uses of taxpayer money dollar for dollar that I've seen, you know, because that, that small
*  sort of initiative that DARPA put out, sort of in my view was the catalyst or the tipping point for
*  this whole next wave of autonomous vehicle development. So that was pretty cool.
*  So let me jump around a little bit on that point. They also did the urban challenge where it was in
*  the city, but it was very artificial and there's no pedestrians and there's very little human
*  involvement except a few professional drivers. Do you think there's room and then there was the
*  robotics challenge with humanoid robots? So in your role is looking at this, you're trying to solve
*  one of the, you know, autonomous driving, one of the harder, more difficult places in San Francisco.
*  Is there a role for DARPA to step in to also kind of help out, like challenge with new ideas,
*  specifically like pedestrians and so on, all these kinds of interesting things?
*  Well, I haven't, I haven't thought about it from that perspective. Is there anything DARPA could do
*  today to further accelerate things? And I would say my instinct is that that's maybe not the
*  highest and best use of their resources and time because like kickstarting and spinning up the
*  flywheel is I think what, what they did in this case for very, very little money. But today this
*  has become, this has become like commercially interesting to very large companies and the amount
*  of money going into it and the amount of people like going through your class and learning about
*  these things and developing your skills is just, you know, orders of magnitude more than it was
*  back then. And so there's enough momentum and inertia and energy and investment dollars into
*  this space right now that I don't, I don't, I think they're, I think they're, they can just say
*  mission accomplished and move on to the next area of technology that needs help. So then stepping
*  back to MIT, you left MIT junior, junior year, what was that decision like? As I said, I always
*  wanted to do a company in or start a company and this opportunity landed in my lap, which was
*  a couple guys from Yale were starting a new company and I Googled them and found that they had
*  started a company previously and sold it actually on eBay for about a quarter million bucks, which
*  was a pretty interesting story. But so I thought to myself, these guys are, you know, rockstar
*  entrepreneurs. They've done this before. They must be driving around in Ferraris because they sold
*  their company. And, you know, I thought I could learn a lot from them. So I teamed up with those
*  guys and, you know, went out during, went out to California during IAP, which is MIT's month off,
*  one on one way ticket and basically never went back. We were having so much fun. We felt like
*  we were building something and creating something. And it was going to be interesting that, you know,
*  I was just all in and got completely hooked. And that business was just in TV, which is originally
*  a reality show about a guy named Justin, which morphed into a live video streaming platform,
*  which then morphed into what is Twitch today. So that was, that was quite an unexpected journey.
*  So no regrets? No. Looking back, it was just an obvious, I mean, one way ticket. I mean,
*  if we just pause on that for a second, there was no, how did you know these were the right guys?
*  This is the right decision? You didn't think it was just follow the heart kind of thing?
*  Well, I didn't know. But, you know, just trying something for a month during IAP seems pretty
*  low risk, right? And then, you know, well, maybe I'll take a semester off. MIT is pretty flexible
*  about that. You can always go back, right? And then after two or three cycles of that, I eventually
*  threw in the towel. But, you know, I think it's, I guess in that case, I felt like I could always
*  hit the undo button if I had to. Right. But nevertheless, from when you look in retrospect,
*  I mean, it seems like a brave decision that, you know, it would be difficult for a lot of
*  people to make. It wasn't as popular, I'd say that the general, you know, flux of people
*  out of MIT at the time was mostly into, you know, finance or consulting jobs in Boston or New York.
*  And very few people were going to California to start companies. But today, I'd say that's,
*  it's probably inverted, which is just a sign of a sign of the times, I guess.
*  Yeah. So there's a story about midnight of March 18, 2007, where TechCrunch, I guess,
*  announced Justin TV earlier than it was supposed to a few hours. The site didn't work. I don't
*  know if any of this is true. You can tell me. And you and one of the folks at Justin TV,
*  Emmett Shearer, coded through the night. Can you take me through that experience?
*  So let me let me say a few nice things that the article I read quoted, Justin Khan said that you
*  were known for bureau coding through problems, and being a creative quote, creative genius.
*  So on that night, what what was going through your head? Or maybe put another way, how do you
*  solve these problems? What's your approach to solving these kinds of problems with the
*  line between success and failure seems to be pretty thin? That's a good question. Well, first
*  of all, that's that's nice of Justin to say that I think, you know, I would have been maybe 21 years
*  old then and not very experienced at programming. But as with with everything in a startup, you're
*  you're sort of racing against the clock. And so our plan was the second we had this live streaming
*  camera backpack up and running where Justin could wear it, and no matter where he went in a city,
*  it would be streaming live video. And this is even before the iPhone. So this is like hard to do back
*  then. We would launch and so we thought we were there and the backpack was working. And then we
*  sent out all the emails to launch the launch the company and do the press thing. And then, you know,
*  we weren't quite actually there. And then we thought, oh, well, you know, they're not going
*  to announce it until maybe 10am the next morning. And it's I don't know, it's 5pm now. So how many
*  hours do we have left? What is that like, you know, 17 hours to go and and that was that was
*  going to be fine. Was the problem obvious? Did you understand what could possibly like how complicated
*  was the system at that point? It was it was pretty messy. So to get a live video feed that looked
*  decent working from anywhere in San Francisco, I put together the system where we had like three or
*  four cell phone data modems and they were like we take the video stream and, you know, sort of
*  sprayed across these three or four modems and then try to catch all the packets on the other side,
*  you know, with unreliable cell phone networks, pretty low level networking. Yeah. And putting
*  these like, you know, sort of protocols on top of all that to reassemble and reorder the packets and
*  have time buffers and error correction and all that kind of stuff. And the night before it was
*  just staticky every once in a while the image would would go staticky and there would be this
*  horrible like screeching audio noise because the audio was also corrupted and this would happen
*  like every five to ten minutes or so and it was a really, you know, off putting to the viewers.
*  Yeah. How do you tackle that problem? What was the you just freaking out behind a computer?
*  There's the word are there other other folks working on this problem? Like were you behind
*  a whiteboard? Were you doing a pair coding? Yeah, it's a little lonely because there's four of us
*  working on the company and only two people really wrote code and Emmett wrote the website in the
*  chat system and I wrote the software for this video streaming device and video server.
*  And so, you know, it's my sole responsibility to figure that out. And I think it's those,
*  you know, setting deadlines, trying to move quickly and everything where you're in that
*  moment of intense pressure that sometimes people do their best and most interesting work. And so,
*  even though that was a terrible moment, I look back on it fondly because that's like, you know,
*  that's one of those character defining moments, I think.
*  So in 2013, October, you founded Cruise Automation. Yeah. So progressing forward,
*  another exceptionally successful company was acquired by GM in 16 for one billion dollars.
*  But in October 2013, what was on your mind? What was the plan? How does one
*  seriously start to tackle one of the hardest robotics, most important impact robotics problems
*  of our age? After going through Twitch, Twitch was, and is today, pretty successful. But the
*  work was, the result was entertainment, mostly. Like, the better the product was, the more we
*  would entertain people and then, you know, make money on the ad revenues and other things. And
*  that was a good thing. It felt good to entertain people. But I figured, like, you know, what is
*  really the point of becoming a really good engineer and developing these skills other than, you know,
*  my own enjoyment? And I realized I wanted something that scratched more of an existential itch,
*  like something that truly matters. And so I basically made this list of requirements for
*  a new, if I was going to do another company. And the one thing I knew in the back of my head,
*  that Twitch took like eight years to become successful. And so whatever I do, I better be
*  willing to commit, you know, at least 10 years to something. And when you think about things from
*  that perspective, you certainly, I think, raise the bar on what you choose to work on. So for me,
*  the three things were it had to be something where the technology itself determines the success of
*  the product, like hard, really juicy technology problems, because that's what motivates me.
*  And then it had to have a direct and positive impact on society in some way. So example would
*  be like, you know, healthcare, self driving cars, because they save lives, other things where there's
*  a clear connection to somehow improving other people's lives. And the last one is it had to
*  be a big business, because for the positive impact to matter, it's got to be a large scale scale.
*  And I was thinking about that for a while. And I made like, I tried writing a Gmail clone and
*  looked at some other ideas. And then it just sort of light bulb went off like self driving cars,
*  like that was the most fun I had ever had in college working on that. And like, well,
*  what's the state of the technology has been 10 years, maybe, maybe times have changed. And
*  maybe now is the time to make this work. And I poked around and looked at the only other thing
*  out there really at the time was the Google self driving car project. And I thought surely there's
*  a way to, you know, have an entrepreneur mindset and sort of solve the minimum viable product here.
*  And so I just took the plunge right then and there and said, this, this is something I know
*  I can commit 10 years to. It's the probably the greatest applied AI problem of our generation.
*  That's right. And if it works, it's going to be both a huge business. And therefore, like,
*  probably the most positive impact I can possibly have on the world. So
*  after that light bulb went off, I went all in on cruise immediately and got to work.
*  Did you have an idea how to solve this problem, which aspect of the problem to solve,
*  you know, slow, like we just had Oliver for voyage here, slow moving retirement communities,
*  urban driving, highway driving? Did you have like, did you have a vision of the city of the future,
*  or, you know, the transportation is largely automated, that kind of thing? Or was it sort of
*  more fuzzy and gray area than that? My analysis of the situation is that Google is putting a lot
*  of had been putting a lot of money into that project, they had a lot more resources. And so,
*  and they still hadn't cracked the fully driverless car, you know, this is 20 2013, I guess.
*  So I thought, what what can I do to sort of go from zero to, you know, significant scale,
*  so I can actually solve the real problem, which is the driverless cars. And I thought,
*  here's the strategy, we'll start by doing a really simple problem, or solving a really simple problem
*  that creates value for people. So eventually ended up deciding on automating highway driving,
*  which is relatively more straightforward, as long as there's a backup driver there. And, you
*  know, the go to market will be able to retrofit people's cars, and to sell these products
*  directly. And the idea was, we'll take all the revenue and profits from that, and use it to do
*  the, sort of reinvest that in research for doing fully driverless cars. And that was the plan. The
*  only thing that really changed along the way between then and now is, we never really launched
*  the first product, we had enough interest from investors and enough of a signal that this was
*  something that we should be working on that, after about a year of working on the highway autopilot,
*  we had it working, you know, on at a prototype stage. But we just completely abandoned that,
*  and said, we're going to go all in on driverless cars. Now is the time. Can't think of anything
*  that's more exciting, and if it works more impactful, so we're just going to go for it.
*  The idea of retrofit is kind of interesting. Yeah, being able to, it's how you achieve scale,
*  it's a really interesting idea. Is it something that's still in the back of your mind as a
*  possibility? Not at all. I've come full circle on that one. After trying to build a retrofit product,
*  and I'll touch on some of the complexities of that, and then also having been inside
*  an OEM and seeing how things work, and how a vehicle is developed and validated,
*  when it comes to something that has safety critical implications, like controlling the
*  steering and other control inputs on your car, it's pretty hard to get there with a retrofit.
*  Even if you did, it creates a whole bunch of new complications around
*  liability, or how did you truly validate that, or if something in the base vehicle
*  fails and causes your system to fail, whose fault is it? Or if the car's anti-lock brake systems,
*  or other things kick in, or the software has been, it's different in one version of the car,
*  you retrofit versus another, and you don't know because the manufacturer has updated it behind the
*  scenes. There's basically an infinite list of long tail issues that can get you, and if you're
*  dealing with a safety critical product, that's not really acceptable. That's a really convincing
*  summary of why it's really challenging. But I didn't know all that at the time, so we tried it
*  anyway. But as a pitch also, at the time, it's a really strong one, because that's how you achieve
*  scale, and that's how you beat the current, the leader at the time of Google, or the only one in
*  the market. The other big problem we ran into, which is perhaps the biggest problem from a
*  business model perspective, is we had kind of assumed that we started with an Audi S4 as the
*  vehicle we retrofitted with this highway driving capability. And we had kind of assumed that if we
*  just knock out like three make and models of vehicle, that'll cover like 80% of the San
*  Francisco market. Doesn't everyone there drive, I don't know, a BMW or a Honda Civic or one of these
*  three cars? And then we surveyed our users, and we found out that it's all over the place. We would
*  to get even a decent number of units sold, we'd have to support like 20 or 50 different models.
*  And each one is a little butterfly that takes time and effort to maintain that retrofit integration
*  and custom hardware and all this. So it was a tough business. So GM manufactures and sells over 9
*  million cars a year. And what you with Cruz are trying to do some of the most cutting edge
*  innovation in terms of applying AI. And so how do those, you've talked about a little bit before,
*  but it's also just fascinating to me, we work a lot of automakers, you know, the difference between
*  the gap between Detroit and Silicon Valley, let's say, just to be sort of poetic about it, I guess,
*  how do you close that gap? How do you take GM into the future where a large part of the fleet
*  will be autonomous, perhaps? I want to start by acknowledging that that GM is made up of, you know,
*  tens of thousands of really brilliant, motivated people who want to be a part of the future.
*  And so it's pretty fun to work with them. The attitude inside a car company like that is,
*  you know, embracing this transformation and change rather than fearing it. And I think that's a
*  testament to the leadership at GM. And that's flown all the way through to everyone you talk to,
*  even the people in the assembly plants working on these cars. So that's really great. So that
*  starting from that position makes it a lot easier. So then when the people in San Francisco at cruise
*  interact with the people at GM, at least we have this common set of values, which is that we really
*  want this stuff to work, because we think it's important and we think it's the future. That's
*  not to say, you know, those two cultures don't clash, they absolutely do. There's different
*  different sort of value systems, like in a car company, the thing that gets you promoted and
*  sort of the reward system is following the processes delivering the program on time and
*  on budget. So any sort of risk taking is discouraged in many ways, because if a program is late,
*  or if you shut down the plant for a day, it's, you know, you can count the millions of dollars that
*  burn by pretty quickly. Whereas I think, you know, most Silicon Valley companies and in cruise and
*  the methodology we were employing, especially around the time of the acquisition, the reward
*  structure is about trying to solve these complex problems in any way, shape or form, or coming up
*  with crazy ideas that, you know, 90% of them won't work. And so meshing that culture of sort of
*  continuous improvement and experimentation with one where everything needs to be, you know,
*  rigorously defined upfront so that you never slip a deadline or miss a budget was a pretty big
*  challenge. And that we're over three years in now after the acquisition. And I'd say like,
*  you know, the investment we made in figuring out how to work together successfully, and who should
*  do what and how we bridge the gaps between these very different systems and way of doing engineering
*  work is now one of our greatest assets, because I think we have this really powerful thing. But for
*  a while, it was both both GM and crews were very steep on the learning curve.
*  Yes, I'm sure it was very stressful. It's really important work, because that's that's how
*  to revolutionize the transportation, really to revolutionize any system. You know, you look at
*  the healthcare system, or you look at the legal system, I have people like Laura's come up to me
*  all the time, like, everything they're working on can easily be automated. But then that's not a good
*  feeling. Yeah, well, it's not a good feeling. But also, there's no way to automate because the
*  entire infrastructure is really, you know, based is older, and it moves very slowly. And so how do
*  you close the gap between I have an how can I replace, of course, lawyers don't want to be
*  replaced with an app, but you could replace a lot of aspect when most of the data is still on paper.
*  And so the same thing with with automotive. I mean, it's fundamentally software. So it's
*  it's basically hiring software engineers is thinking a software world. I mean, I'm pretty sure
*  nobody in Silicon Valley has ever hit a deadline. So and then on GM, it's probably true. Yeah.
*  And GM side is probably the opposite. Yeah. So that's that culture gap is really fascinating.
*  So you're optimistic about the future of that? Yeah, I mean, from what I've seen, it's impressive.
*  And I think like, especially in Silicon Valley, it's easy to write off building cars, because,
*  you know, people have been doing that for over 100 years now in this country. And so it seems
*  like that's a solved problem. But that doesn't mean it's an easy problem. And I think it would
*  be easy to sort of overlook that and think that, you know, we're Silicon Valley engineers, we can
*  solve any problem, you know, building a car, it's been done, therefore, it's, you know, it's, it's,
*  it's not, it's not a real engineering challenge. But after having seen just the sheer scale and
*  magnitude and industrialization that occurs inside of an automotive assembly plant, that is a lot of
*  work that I am very glad that we don't have to reinvent to make self driving cars work. And so
*  to have, you know, partners who have done that for 100 years now, these great processes, this huge
*  infrastructure and supply base that we can tap into is just remarkable, because the scope
*  and surface area of the problem of deploying fleets of self driving cars is so large,
*  that we're constantly looking for ways to do less. So we can focus on the things that really matter
*  more. And if we had to figure out how to build and assemble and, you know, test, build the cars
*  themselves, I mean, we work closely with GM on that. But if we had to develop all that capability
*  in house as well, you know, that that would just make make the problem really intractable, I think.
*  So yeah, just like your first entry, the MIT DARPA challenge when there was what the motor that
*  failed, if somebody that knows what they're doing with the motor did it, that would have been nice
*  if we could focus on the software, not the hardware platform. Yeah. Right. So from your perspective,
*  now, you know, there's so many ways that autonomous vehicles can impact society in the next year,
*  five years, 10 years, what do you think is the biggest opportunity to make money in autonomous
*  driving? So sort of make it a financially viable thing in the near term? What do you think would
*  be the biggest impact there? Well, the things that that drive the economics for fleets of
*  self driving cars are there's sort of a handful of variables. One is, you know, the cost to
*  build the vehicle itself. So the material cost, how many, you know, what's the cost of all your
*  sensors plus the cost of the vehicle and every all the other components on it. Another one is the
*  lifetime of the vehicle. It's very different if your vehicle drives 100,000 miles and then falls
*  apart versus, you know, 2 million. And then, you know, if you have a fleet, it's kind of like
*  an airplane where or a airline where once you produce the vehicle, you want it to be in operation
*  as many hours a day as possible producing revenue. And then, you know, the other piece of that is
*  how are you generating revenue? I think that's kind of what you're asking. And I think the obvious
*  things today are, you know, the ride sharing business, because that's pretty clear that there's
*  demand for that. There's existing markets you can tap into. And large urban areas, that kind of thing.
*  Yeah, yeah. And I think that there are some real benefits to having cars without drivers compared
*  to sort of the status quo for people who use ride share services today. You know, you get privacy,
*  consistency, hopefully significantly improve safety, all these benefits versus the current product.
*  But it's a crowded market. And then other opportunities, which you've seen a lot of
*  activity in the last, really in the last six or 12 months is, you know, delivery, whether that's
*  parcels and packages, food or groceries. Those are all sort of, I think, opportunities that are
*  pretty ripe for these, you know, once you have this core technology, which is the fleet of
*  autonomous vehicles, there's all sorts of different business opportunities you can build on top of
*  that. But I think the important thing, of course, is that there's zero monetization opportunity
*  until you actually have that fleet of very capable driverless cars that are as good or better than
*  humans. And that's sort of where the entire industry is sort of in this holding pattern right now.
*  Yeah, they're trying to achieve that baseline. So but you said sort of reliable, not reliability,
*  consistency. It's kind of interesting. I think I heard you say somewhere,
*  not sure if that's what you meant. But, you know, I can imagine a situation where you would get an
*  autonomous vehicle. And, you know, when you get into an Uber or Lyft, you don't get to choose
*  the driver in a sense that you don't get to choose the personality of the driving. Do you think
*  there's a there's room to define the personality of the car the way it drives you in terms of
*  aggressiveness, for example, in terms of sort of pushing the bound the one of the biggest
*  challenges of driving is the is the trade off between sort of safety and assertiveness.
*  And do you think there's any room for the human to take a role in that decision,
*  to accept some of the liability, I guess? I wouldn't know I'd say within reasonable bounds,
*  as in we're not going to I think it'd be highly unlikely we'd expose any knob that would let you
*  significantly increase safety risk. I think that's that's just not something we'd be willing to do.
*  But I think driving style or like, you know, are you going to relax the comfort constraints
*  slightly or things like that? All of those things make sense and are plausible. I see all those as
*  you know, nice optimizations. Once again, we get the core problem solved in these fleets out there.
*  But the other thing we've sort of observed is that you have this intuition that if you sort of
*  slam your foot on the gas right after the light turns green and aggressively accelerate,
*  you're going to get there faster. But the actual impact of doing that is pretty small,
*  you feel like you're getting there faster. But so that's the same would be true for AVs, even if
*  they don't slam their, you know, the pedal to the floor when the light turns green, they're going to
*  get you there within you know, if it's a 15 minute trip within 30 seconds of what you would have done
*  otherwise, if you were going really aggressively. So I think there's this sort of self deception
*  that that my aggressive driving style is getting me there faster. Well, so that's, you know, some of
*  the things I study some things I'm fascinated by the psychology of that. I don't think it matters
*  that it doesn't get you there faster. It's it's the emotional release. Driving is is a place being
*  inside our car. Somebody said it's like the real world version of being a troll. So you have this
*  protection, this mental protection, you're able to sort of yell at the world like release your anger,
*  whatever is but so there's an element of that, that I think autonomous vehicles would also have
*  to, you know, have giving an outlet to people, but it doesn't have to be through, through driving or
*  honking or so on. There might be other outlets. But I think to just sort of even just put that aside,
*  the baseline is really, you know, that's the focus, that's the thing you need to solve. And then the
*  fun human things can be solved after. But so from the baseline of just solving autonomous driving,
*  you're working in San Francisco, one of the more difficult cities to operate in. What is what is
*  the in your view currently the hardest aspect of autonomous driving? Is it negotiating with pedestrians?
*  Is it edge cases of perception? Is it planning? Is there a mechanical engineering? Is it data
*  fleet stuff? What are your thoughts on the challenge, the more challenging aspects there?
*  That's a good question. I think before we go to that, though, I just want to, I like what you said
*  about the psychology aspect of this, because I think one observation I've made is, I think I
*  read somewhere that I think it's maybe Americans on average spend, you know, over an hour a day on
*  social media, like staring at Facebook. And so that's just, you know, 60 minutes of your life,
*  you're not getting back, it's probably not super productive. And so that's 3600 seconds, right? And
*  that's, that's tiny, you know, it's a lot of time you're giving up. And if you compare that to
*  people being on the road, if another vehicle, whether it's a human driver or autonomous vehicle,
*  delays them by even three seconds, they're laying in on the horn, you know, even though that's,
*  that's, you know, one one thousandth of the time they waste looking at Facebook every day. So there's,
*  there's definitely some, you know, psychology aspects of this, I think that are pretty
*  interesting road rage in general. And then the question, of course, is if everyone is in
*  self-driving cars, do they even notice these three second delays anymore? Because they're
*  doing other things or reading or working or just talking to each other. So it'll be interesting
*  to see where that goes. In a certain aspect, people, people need to be distracted by something
*  entertaining, something useful inside the car, so they don't pay attention to the external world.
*  And then, and then they can take whatever psychology and bring it back to Twitter,
*  and then focus on that as opposed to sort of interacting, sort of putting the emotion out
*  there into the world. So it's an interesting problem, but baseline autonomy. I guess you could
*  say self-driving cars, you know, at scale will lower the collective blood pressure of society,
*  probably by a couple points without all that road rage and stress. So that's a good, good externality.
*  So back to your question about the technology and the, I guess, the biggest problems. And I have a
*  hard time answering that question because, you know, we've been at this, like specifically
*  focusing on driverless cars and all the technology needed to enable that for a little over four and
*  a half years now. And even a year or two in, I felt like we had completed the functionality needed
*  to get someone from point A to point B. As in, if we need to do a left turn maneuver, or if we need
*  to drive around a, you know, a double parked vehicle into oncoming traffic or navigate through
*  construction zones, the scaffolding and the building blocks was there pretty early on.
*  And so the challenge is not any one scenario or situation for which, you know, we fail at 100%
*  of those. It's more, you know, we're benchmarking against a pretty good or pretty high standard,
*  which is human driving. All things considered, humans are excellent at handling edge cases and
*  unexpected scenarios where computers are the opposite. And so beating that baseline set by
*  humans is the challenge. And so what we've been doing for quite some time now is basically,
*  it's this continuous improvement process where we find sort of the most, you know, uncomfortable
*  or the things that could lead to a safety issue, other things, all these events, and then we sort
*  of categorize them and rework parts of our system to make incremental improvements and do that over
*  and over and over again. And we just see sort of the overall performance of the system
*  actually increasing in a pretty steady clip, but there's no one thing. There's actually like
*  thousands of little things and just like polishing functionality and making sure that it handles,
*  you know, every version and possible permutation of a situation by either applying more deep learning
*  systems or just by, you know, adding more test coverage or new scenarios that we develop against
*  and just grinding on that. We're sort of in the unsexy phase of development right now,
*  which is doing the real engineering work that it takes to go from prototype to production.
*  You're basically scaling the grinding, sort of taking seriously that the process of
*  all those edge cases, both with human experts and machine learning methods to cover all those
*  situations. Yeah, and the exciting thing for me is I don't think that grinding ever stops,
*  because there's a moment in time where you cross that threshold of human performance and become
*  superhuman, but there's no reason, there's no first principles reason that AV capability will
*  tap out anywhere near humans. Like there's no reason it couldn't be 20 times better,
*  whether that's, you know, just better driving or safer driving or more comfortable driving,
*  or even a thousand times better given enough time. And we intend to basically chase that,
*  you know, forever to build the best possible product. Better and better and better and always
*  new edge cases come up and new experiences. So, and you want to automate that process as much as
*  possible. So what do you think in general in society? When do you think we may have
*  hundreds of thousands of fully autonomous vehicles driving around? So first of all,
*  predictions, nobody knows the future. You're a part of the leading people trying to define
*  that future, but even then you still don't know. But if you think about hundreds of thousands of
*  vehicles, so a significant fraction of vehicles in major cities are autonomous. Do you think,
*  are you with Rodney Brooks, who is 2050 and beyond, or are you more with Elon Musk,
*  who is, we should have had that two years ago? Well, I mean, I'd love to have it two years ago,
*  but we're not there yet. So I guess the way I would think about that is let's flip that question
*  around. So what would prevent you to reach hundreds of thousands of vehicles? And that's a good,
*  that's a good rephrasing. Yeah. So the, I'd say the, it seems the consensus
*  among the people developing self-driving cars today is to sort of start with some form of an
*  easier environment, whether it means, you know, lacking inclement weather, or, you know, mostly
*  sunny or whatever it is, and then add capability for more complex situations over time. And so if
*  you're only able to deploy in areas that meet sort of your criteria or the current domain, you know,
*  operating domain of the software you developed, that may put a cap on how many cities you could
*  deploy in. But then as those restrictions start to fall away, like maybe you add, you know,
*  capability to drive really well and safely in heavy rain or snow, you know, that probably opens
*  up the market by two or threefold in terms of the cities you can expand into and so on. And so the
*  real question is, you know, I know today, if we wanted to, we could produce that many autonomous
*  vehicles, but we wouldn't be able to make use of all of them yet, because we would sort of saturate
*  the demand in the cities in which we would want to operate initially. So if I were to guess like
*  what the timeline is for those things falling away and reaching hundreds of thousands of vehicles,
*  maybe a range is better. I would say less than five years. Less than five years. Yeah. And of
*  course, you're working hard to make that happen. So you started two companies that were eventually
*  acquired for each $4 billion. So you're a pretty good person to ask, what does it take to build
*  a successful startup? I think there's sort of survivor bias here a little bit, but I can try
*  to find some common threads for the things that worked for me, which is, you know, in both of
*  these companies, I was really passionate about the core technology. I actually like, you know,
*  lay awake at night thinking about these problems and how to solve them. And I think that's helpful
*  because when you start a business, there are like to this day, there are these crazy ups and downs.
*  Like one day you think the business is just on you're just on top of the world and unstoppable.
*  And the next day you think, okay, this is all going to end, you know, it's just going south
*  and it's going to be over tomorrow. And so I think like having a true passion that you can
*  fall back on and knowing that you would be doing it even if you weren't getting paid for it helps
*  you weather those tough times. So that's one thing. I think the other one is really good people. So
*  I've always been surrounded by really good co-founders that are logical thinkers, are always
*  pushing their limits and have very high levels of integrity. So that's Dan Khan and my current
*  company and actually his brother and a couple other guys for Justin TV and Twitch. And then
*  I think the last thing is just, I guess, persistence or perseverance. Like, and that can apply to
*  sticking to sort of, or having conviction around the original premise of your idea and sticking
*  around to do all the, you know, the unsexy work to actually make it come to fruition,
*  including dealing with, you know, whatever it is that you're not passionate about, whether that's
*  finance or HR or operations or those things. As long as you are grinding away and working towards,
*  you know, that North Star for your business, whatever it is, and you don't give up and you're
*  making progress every day, it seems like eventually you'll end up in a good place. And the only things
*  that can slow you down are, you know, running out of money or I suppose your competitors destroying
*  you. But I think most of the time it's people giving up or somehow destroying things themselves
*  rather than being beaten by their competition or running out of money. Yeah, if you never quit,
*  eventually you'll arrive. So much more concise version of what I was trying to say.
*  So you went the Y Combinator route twice. Yeah. What do you think in a quick question,
*  do you think is the best way to raise funds in the early days or not just funds, but just community
*  develop your idea and so on? Can you do it solo or maybe with a co-founder with like self-funded?
*  Do you think Y Combinator is good? Is it good to do VC route? Is there no right answer or is there
*  from the Y Combinator experience something that you could take away that that was the right path
*  to take? There's no one size fits all answer. But if your ambition I think is to, you know,
*  see how big you can make something or rapidly expand and capture market or solve a problem or
*  whatever it is, then, you know, going the venture back route is probably a good approach so that
*  capital doesn't become your primary constraint. Y Combinator I love because it puts you in this
*  competitive environment where you're surrounded by the top maybe 1% of other really highly motivated
*  peers who are in the same place. And that environment I think just breeds success, right?
*  If you're surrounded by really brilliant hardworking people, you're going to feel
*  sort of compelled or inspired to try to emulate them and or beat them. And so even though I had
*  done it once before and I felt like, you know, I'm pretty self-motivated, I thought like, look,
*  this is going to be a hard problem. I can use all the help I can get. So surrounding myself with
*  other entrepreneurs is going to make me work a little bit harder or push a little harder than
*  it's worth it. And so that's why I did it, you know, for example, the second time.
*  Let's go philosophical, existential. If you go back and do something differently in your life,
*  starting in high school and MIT, leaving MIT, you could have gone the PhD route,
*  doing startup, going to see about a startup in California, or maybe some aspects of fundraising.
*  Is there something you regret? Something you not necessarily regret, but if you go back,
*  you could do differently? I think I've made a lot of mistakes, like, you know, pretty much everything
*  you can screw up. I think I've screwed up at least once. But I, you know, I don't regret those things.
*  I think it's hard to look back on things, even if they didn't go well and call it a regret,
*  because hopefully, you know, it took away some new knowledge or learning from that. So
*  I would say there was a period. Yeah, the closest I can come to is this. There's a period in
*  in Justin TV, I think after seven years where, you know, the company was going one direction,
*  which is towards Twitch in video gaming. And I'm not a video gamer. I don't really even use Twitch
*  at all. And I was still working on the core technology there. But my heart was no longer
*  in it, because the business that we were creating was not something that I was personally passionate
*  about. It didn't meet your bar of existential impact. Yeah. And I'd say I probably spent an
*  extra year or two working on that. And I'd say like, I would have just tried to do something
*  different sooner. Because those were two years where I felt like, you know, from this philosophical
*  or existential thing, I just felt that something was missing. And so I would have, if I could look
*  back now and tell myself, it's like, I would have said exactly that. Like, you're not getting any
*  meaning out of your work personally right now. You should find a way to change that. And that's
*  part of the pitch I use to basically everyone who joins Cruise today. It's like, hey, you've got that
*  now by coming here. Well, maybe you needed the two years of that existential dread to develop the
*  feeling that ultimately was the fire that created Cruise. So you never know. You can't repair.
*  Good theory. Yeah. So last question, what does 2019 hold for Cruise? After this, I guess we're
*  going to go and talk to your class. But one of the big things is going from prototype to production
*  for autonomous cars. And what does that mean? What does that look like? And 2019 for us is the year
*  that we try to cross over that threshold and reach, you know, superhuman level of performance to some
*  degree with the software and have all the other of the thousands of little building blocks in place
*  to launch, you know, our first commercial product. So that's what's in store for us.
*  Or in store for us. And we've got a lot of work to do. We've got a lot of brilliant people working
*  on it. So it's all up to us now. Yeah. From Charlie Miller and Chris Vales, like the people I've
*  crossed paths with. It sounds like you have an amazing team. So like I said, it's one of the most,
*  I think one of the most important problems in artificial intelligence of the century.
*  It'll be one of the most defining. It's super exciting that you work on it. And
*  the best of luck in 2019. I'm really excited to see what Chris comes up with.
*  Thank you. Thanks for having me today.

---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 5997s
Video Keywords: ['ayanna howard', 'robotics', 'hri', 'human-robot interaction', 'hal 9000', 'ai safety', 'georgia tech', 'matrix', 'spotmini', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 28256
Video Rating: None
Video Description: Ayanna Howard is a roboticist and professor at Georgia Tech, director of Human-Automation Systems lab, with research interests in human-robot interaction, assistive robots in the home, therapy gaming apps, and remote robotic exploration of extreme environments.

This episode is presented by Cash App. Download it & use code "LexPodcast":
Cash App (App Store): https://apple.co/2sPrUHe
Cash App (Google Play): https://bit.ly/2MlvP5w

PODCAST INFO:
Podcast website: https://lexfridman.com/podcast
Apple Podcasts: https://apple.co/2lwqZIr
Spotify: https://spoti.fi/2nEwCF8
RSS: https://lexfridman.com/feed/podcast/
Full episodes playlist: https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist: https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

EPISODE LINKS:
Ayanna Website: https://howard.ece.gatech.edu/
Ayanna Twitter: https://twitter.com/robotsmarts

OUTLINE:
0:00 - Introduction
2:09 - Favorite robot
5:05 - Autonomous vehicles
8:43 - Tesla Autopilot
20:03 - Ethical responsibility of safety-critical algorithms
28:11 - Bias in robotics
38:20 - AI in politics and law
40:35 - Solutions to bias in algorithms
47:44 - HAL 9000
49:57 - Memories from working at NASA
51:53 - SpotMini and Bionic Woman
54:27 - Future of robots in space
57:11 - Human-robot interaction
1:02:38 - Trust
1:09:26 - AI in education
1:15:06 - Andrew Yang, automation, and job loss
1:17:17 - Love, AI, and the movie Her
1:25:01 - Why do so many robotics companies fail?
1:32:22 - Fear of robots
1:34:17 - Existential threats of AI
1:35:57 - Matrix
1:37:37 - Hang out for a day with a robot

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Ayanna Howard Human-Robot Interaction & Ethics of Safety-Critical Systems  Lex Fridman Podcast #66
**Lex Fridman:** [January 17, 2020](https://www.youtube.com/watch?v=J21-7AsUcgM)
*  The following is a conversation with Ayanna Howard. She's a roboticist,
*  professor Georgia Tech, and director of the Human Automation Systems Lab,
*  with research interests in human-robot interaction, assistive robots in the home,
*  therapy gaming apps, and remote robotic exploration of extreme environments. Like me,
*  in her work, she cares a lot about both robots and human beings, and so I really enjoyed this
*  conversation. This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  give it five stars on Apple Podcasts, follow on Spotify, support it on Patreon, or simply
*  connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. I recently started doing
*  ads at the end of the introduction. I'll do one or two minutes after introducing the episode,
*  and never any ads in the middle that can break the flow of the conversation. I hope that works
*  for you, and doesn't hurt the listening experience. This show is presented by Cash App, the number
*  one finance app in the App Store. I personally use Cash App to send money to friends, but you
*  can also use it to buy, sell, and deposit Bitcoin in just seconds. Cash App also has a new investing
*  feature. You can buy fractions of a stock, say $1 worth, no matter what the stock price is.
*  Broker services are provided by Cash App Investing, a subsidiary of Square and Member SIPC.
*  I'm excited to be working with Cash App to support one of my favorite organizations called First,
*  best known for their FIRST Robotics and Lego competitions. They educate and aspire hundreds
*  of thousands of students in over 110 countries, and have a perfect rating at Charity Navigator,
*  which means that donated money is used to maximum effectiveness. When you get Cash App from the
*  App Store or Google Play, and use code LexPodcast, you'll get $10, and Cash App will also donate
*  $10 to FIRST, which again is an organization that I've personally seen inspire girls and boys to
*  dream of engineering a better world. And now here's my conversation with Ayanna Howard.
*  What or who is the most amazing robot you've ever met, or perhaps had the biggest impact on
*  your career? I haven't met her, but I grew up with her, but of course Rosie. So, and I think it's
*  because also- Who's Rosie?
*  Rosie from the Jetsons. She is all things to all people. Right? Think about it. Anything you want
*  it. It was like magic. It happened. So people not only anthropomorphize, but project whatever they
*  wish for the robot to be onto Rosie. But also, I mean, think about it. She was socially engaging.
*  She every so often had an attitude, right? She kept us honest. She would push back sometimes
*  when George was doing some weird stuff. But she cared about people, especially the kids.
*  She was like the perfect robot. And you've said that people don't want their robots to be perfect.
*  Can you elaborate on that? What do you think that is? Just like you said,
*  Rosie pushed back a little bit every once in a while.
*  Yeah. So I think it's that- So if you think about robotics in general, we want them
*  because they enhance our quality of life. And usually that's linked to something that's
*  functional. Right? Even if you think of self-driving cars, why is there a fascination?
*  Because people really do hate to drive. There's the Saturday driving where I can just speed,
*  but then there's the, I have to go to work every day and I'm in traffic for an hour.
*  I mean, people really hate that. And so robots are designed to basically enhance our ability to
*  increase our quality of life. And so the perfection comes from this aspect of interaction.
*  If I think about how we drive, if we drove perfectly, we would never get anywhere. Right?
*  So think about how many times you had to run past the light because you see the car behind you
*  is about to crash into you or that little kid kind of runs into the street. And so you have
*  to cross on the other side because there's no cars. Right? Like if you think about it,
*  we are not perfect drivers. Some of it is because it's our world. And so if you have a robot that
*  is perfect in that sense of the word, they wouldn't really be able to function with us.
*  Can you linger a little bit on the word perfection? So from the robotics perspective,
*  what does that word mean and how is sort of the optimal behavior as you're describing different
*  than what we think is perfection? Yeah. So perfection, if you think about it
*  in the more theoretical point of view, it's really tied to accuracy. Right? So if I have a function,
*  can I complete it at a hundred percent accuracy with zero errors? And so that's kind of, if you
*  think about perfection in the sense of the word and in a self-driving car realm, do you think
*  from a robotics perspective, we kind of think that perfection means following the rules perfectly,
*  sort of defining, staying in the lane, changing lanes. When there's a green light, you go,
*  when there's a red light, you stop. And that's the, and be able to perfectly see all the entities in
*  the scene. That's the limit of what we think of as perfection. And I think that's where the problem
*  comes is that when people think about perfection for robotics, the ones that are the most successful
*  are the ones that are quote unquote, perfect. Like I said, Rosie is perfect, but she actually
*  wasn't perfect in terms of accuracy, but she was perfect in terms of how she interacted and how she
*  adapted. And I think that's some of the disconnect is that we really want perfection with respect to
*  its ability to adapt to us. We don't really want perfection with respect to a hundred percent
*  accuracy, with respect to the rules that we just made up anyway. And so I think there's this
*  disconnect sometimes between what we really want and what happens. And we see this all the time,
*  like in my research, like the optimal quote unquote, optimal interactions are when the robot is
*  adapting based on the person, not a hundred percent following what's optimal based on the rules.
*  Just to link on autonomous vehicles for a second, just your thoughts maybe off the top of head is
*  how hard is that problem? Do you think based on what we just talked about, you know, there's a
*  lot of folks in the automotive industry, they're very confident from Elon Musk to Waymo to all
*  these companies. How hard is it to solve that last piece? The last mile. The gap between
*  the perfection and the human definition of how you actually function in this world.
*  Yeah. So this is a moving target. So I remember when all the big companies started to heavily
*  invest in this and there was a number of even roboticists as well as, you know, folks who were
*  putting in the VCs and corporations, Elon Musk being one of them that said, you know,
*  self-driving cars on the road with people, you know, within five years. That was a little while
*  ago. And now people are saying five years, 10 years, 20 years. Some are saying never. Right?
*  I think if you look at some of the things that are being successful is these basically fixed
*  environments where you still have some anomalies. Right? You still have people walking. You still
*  have stores, but you don't have other drivers. Right? Like other human drivers are, it's a
*  dedicated space for the cars. Because if you think about robotics in general, where it's always been
*  successful is, I mean, you can say manufacturing, like way back in the day. Right? It was a fixed
*  environment. Humans were not part of the equation. We're a lot better than that. But like when we can
*  carve out scenarios that are closer to that space, then I think that it's where we are. So
*  a closed campus where you don't have self-driving cars and maybe some protection so that the
*  students don't jet in front just because they want to see what happens. Like having a little bit,
*  I think that's where we're going to see the most success in the near future. And be slow moving.
*  Right. Not, you know, 55, 60, 70 miles an hour, but the speed of a golf cart. Right?
*  That said, the most successful in the automotive industry robots operating today in the hands of
*  real people are ones that are traveling over 55 miles an hour and in unconstrained environments,
*  which is Tesla vehicles, so Tesla autopilot. So I would love to hear your just thoughts
*  of two things. So one, I don't know if you've gotten to see, you've heard about something called
*  smart summon where Tesla system autopilot system, where the car drives zero occupancy, no driver
*  in the parking lot slowly sort of tries to navigate the parking lot to find itself to you.
*  And there's some incredible amounts of videos and just hilarity that happens as it awkwardly tries
*  to navigate this environment. But it's a beautiful nonverbal communication between machine and human
*  that I think is a from it's like it's some of the work that you do in this kind of interesting
*  human robot interaction space. So what are your thoughts in general about it? So I do have that
*  feature. Do you drive a Tesla? I do. Mainly because I'm a gadget freak. Right? So I say it's a gadget
*  that happens to have some wheels. And yeah, I've seen some of the videos. But what's your experience
*  like? I mean, you're you're a human robot interaction roboticist. You're a legit sort of
*  expert in the field. So what does it feel for a machine to come to you? It's one of these very
*  fascinating things. But also, I am hyper hyper alert, right? Like, I'm hyper alert, like my butt,
*  my thumb is like, oh, OK, I'm ready to take over. Even when I'm in my car, I'm doing things like
*  automated backing into. So there's like a feature where you can do this automating backing into our
*  parking space or bring the car out of your garage or even, you know, pseudo autopilot on the freeway.
*  Right. I am hypersensitive. I can feel like as I'm navigating, like, yeah, that's an error right
*  there. Like, I am very aware of it, but I'm also fascinated by it. And it does get better. Like,
*  I look and see it's learning from all of these people who are cutting it on. Like,
*  every time I come on, it's getting better. Right. And so I think that's what's amazing about
*  is that this nice dance of you're still hyper vigilant. So you're still not trusting it at all.
*  Yeah. And yet you're using it. What on the highway, if I were to like what as a roboticist,
*  we'll talk about trust a little bit. What how do you explain that you still use it?
*  Is it the gadget freak part, like where you just enjoy exploring technology or is that the right
*  actually balance between robotics and humans is where you use it, but don't trust it. And somehow
*  there's this dance that ultimately is a positive. Yeah. So I think I'm, I just don't necessarily
*  trust technology, but I'm an early adopter. Right. So when it first comes out, I will use
*  everything, but I will be very, very cautious of how I use it. Do you read about it or do you
*  explore it, but just try it? They do like crudely to put it crudely. Do you read the manual or do
*  you learn through exploration? I'm an explorer. If I have to read the manual, then you know,
*  I do design, then it's a bad user interface. It's a failure. Elon Musk is very confident that you
*  kind of take it from where it is now to full autonomy. So from this human robot interaction,
*  where you don't really trust and then you try and then you catch it when it fails to, it's going to
*  incrementally improve itself into full, full, where you don't need to participate. What's your
*  sense of that trajectory? Is it feasible? So the promise there is by the end of next year,
*  by the end of 2020 is the current promise. What's your sense about that journey that test is on?
*  So there's kind of three things going on though. I think in terms of will people go like as a user,
*  as a adopter, will you trust going to that point? I think so, right? Like there are some users and
*  it's because what happens is when you're hypersensitive at the beginning and then the
*  technology tends to work, your apprehension slowly goes away. And as people, we tend to
*  swing to the other extreme, right? Because like, Oh, I was like hyper, hyper fearful or hypersensitive
*  and it was awesome. And we just tend to swing. That's just human nature. And so you will have,
*  I mean, and I, I,
*  That's a scary notion because most people are now extremely untrusting of autopilot. They use it,
*  but they don't trust it. And it's a scary notion that there's a certain point where you allow
*  yourself to look at the smartphone for like 20 seconds. And then there'll be this phase shift
*  where it'll be like 20 seconds, 30 seconds, one minute, two minutes. It's a scary proposition.
*  But that's people, right? That's just, that's humans. I mean, I think of even our use of,
*  I mean, just everything on the internet, right? Like think about how reliant we are on certain
*  apps and certain engines, right? 20 years ago, people have been like, Oh yeah, that's stupid.
*  Like that makes no sense. Like, of course that's false. Like now it's just like, Oh, of course
*  I've been using it. It's been correct all this time. Of course, aliens, I didn't think they
*  existed, but now it says they do. Obviously.
*  100%. Earth is flat. So, okay. But you said three things. So one is the human kind of
*  selection. Okay. So one is the human. And I think there will be a group of individuals that will
*  swing, right? I just- Teenagers.
*  Teenage. I mean, it'll be adults. There's actually an age demographic that's optimal for technology
*  adoption. And you can actually find them. And they're actually pretty easy to find just based
*  on their habits, based on. So if someone like me who wasn't a roboticist would probably be the
*  optimal kind of person, right? Early adopter, okay with technology, very comfortable and not
*  hypersensitive, right? I'm just hypersensitive because I designed this stuff. So there is a
*  target demographic that will swing. The other one though is you still have these humans that are on
*  the road. That one is a harder thing to do. And as long as we have people that are on the same
*  streets, that's going to be the big issue. And it's just because you can't possibly map some of the
*  silliness of human drivers, right? As an example, when you're next to that car that has that big
*  sticker called student driver, right? You are like, oh, either I'm going to go around. We know
*  that that person is just going to make mistakes that make no sense, right? How do you map that
*  information? Or if I am in a car and I look over and I see two fairly young looking individuals,
*  and there's no student driver bumper and I see them chit chatting to each other, I'm like, oh,
*  that's an issue, right? So how do you get that kind of information and that experience into
*  basically an autopilot? Yeah. And there's millions of cases like that where we
*  take little hints to establish context. I mean, you said kind of beautifully poetic human things,
*  but there's probably subtle things about the environment, about it being maybe time for
*  commuters to start going home from work and therefore you can make some kind of judgment
*  about the group behavior of pedestrians, blah, blah, blah, and so on. Yes. Or even cities, right?
*  If you're in Boston, how people cross the street, lights are not an issue versus other places where
*  people will actually wait for the crosswalk. Seattle or somewhere peaceful. But what I've
*  also seen, sort of just even in Boston, that intersection to intersection is different. So
*  every intersection has a personality of its own. So certain neighborhoods of Boston are different.
*  So we kind of end based on different timing of day, at night. There's a dynamic to human behavior
*  that we kind of figure out ourselves. We're not able to introspect and figure it out, but somehow
*  our brain learns it. We do. And so you're saying, is there a shortcut? Is there a shortcut, though,
*  is there something that could be done, you think, that's what we humans do? It's just like
*  bird flight, right? That's the example they give for flight. Do you necessarily need to build a
*  bird that flies or can you do an airplane? Is there a shortcut? So I think the shortcut is,
*  and I kind of talk about it as a fixed space. So imagine that there's a neighborhood that's
*  a new smart city or a new neighborhood that says, you know what, we are going to design
*  this new city based on supporting self-driving cars. And then doing things, knowing that there's
*  anomalies, knowing that people are like this, right? And designing it based on that assumption
*  that we're going to have this, that would be an example of a shortcut. So you still have people,
*  but you do very specific things to try to minimize the noise a little bit as an example.
*  And the people themselves become accepting of the notion that there's autonomous cars, right?
*  Right. They move into, so right now you will have a self-selection bias, right? Individuals will move
*  into this neighborhood knowing this is part of the real estate pitch, right? And so I think that's
*  a way to do a shortcut. One, it allows you to deploy, it allows you to collect then data with
*  these variances and anomalies, because people are still people, but it's a safer space and is more
*  of an accepting space. I.e. when something in that space might happen, because things do,
*  because you already have the self-selection, people would be, I think, a little more forgiving
*  than other places. And you said three things. Do we cover all of them? The third is legal law.
*  Oh, no. Liability, which I don't really want to touch, but it's still of concern. And the mish
*  mash with policy as well, sort of government, all that whole. That big ball of mess. Yeah, got you.
*  So that's, so we're out of time now. Do you think from a robotics perspective,
*  you know, if you're kind of honest of what cars do, they kind of threaten each other's life all
*  the time. So cars are very, I mean, in order to navigate intersections, there's an assertiveness,
*  there's a risk taking. And if you were to reduce it to an objective function, there's a probability
*  of murder in that function, meaning you killing another human being and you're using that. First
*  of all, it has to be low enough to be acceptable to you on an ethical level as an individual human
*  being, but it has to be high enough for people to respect you, to not sort of take advantage of you
*  completely and jaywalk and funny and so on. So I mean, I don't think there's a right answer here,
*  but how do we solve that? How do we solve that from a robotics perspective when danger and
*  human life is at stake? As they say, cars don't kill people, people kill people. Right. So I think
*  now robotic algorithms would be killing. Right. So it will be robotics algorithms that are pro,
*  no, it will be robotic algorithms don't kill people. Developers of robotic algorithms kill
*  people. Right. I mean, one of the things is people are still in the loop and at least in the near
*  and midterm, I think people will still be in the loop at some point, even if it's a developer,
*  like we're not necessarily at the stage where, you know, robots are programming,
*  autonomous robots with different behaviors quite yet. Not a scary notion. Sorry to interrupt
*  that a developer has some responsibility in the death of a human being. That's a
*  heavy burden. I mean, I think that's why the whole aspect of ethics in our community is so,
*  so important. Right. Like, because it's true. If you think about it, you can basically say,
*  I'm not going to work on weaponized AI. Right. Like people can say, that's not what I'm going to do.
*  But yet you are programming algorithms that might be used in healthcare algorithms that might decide
*  whether this person should get this medication or not. And they don't and they die. Okay. So
*  that is your responsibility. Right. And if you're not conscious and aware that you do have that
*  power when you're coding and things like that, I think that's just not a good thing. Like,
*  we need to think about this responsibility as we program robots and, and computing devices,
*  much more than we are. Yeah. So it's not an option to not think about ethics. I think it's a
*  majority, I would say of computer science sort of there. It's kind of a hot topic now. I think
*  about bias and so on, but it's, and we'll talk about it, but usually it's kind of,
*  you, it's like a very particular group of people that work on that.
*  And then people who do like robotics are like, well, I don't have to think about that. There's
*  other smart people thinking about it. It seems that everybody has to think about it. It's not,
*  you can't escape the ethics, whether it's bias or just every aspect of ethics that has to do
*  with human beings. Everyone. So think about, I'm going to age myself, but I remember when we didn't
*  have like testers, right? And so what did you do as a developer? You had to test your own code,
*  right? Like you had to go through all the cases and figure it out. And, you know, and then they
*  realized that, you know, like we probably need to have testing because we're not getting all the
*  things. And so from there, what happens is like most developers, they do, you know, a little bit
*  of testing, but it's usually like, okay, did my compiler bug out? Let me look at the warnings.
*  Okay. Is that acceptable or not? Right. Like that's how you typically think about as a developer.
*  And you'll just assume that it's going to go to another process and they're going to test it out.
*  But I think we need to go back to those early days when, you know, you're a developer, you're
*  developing, there should be like this, a, you know, okay, let me look at the ethical outcomes of this,
*  because there isn't a second, like testing ethical testers, right? It's you. We did it back in the
*  early coding days. I think that's where we are with respect to ethics. Like let's go back to
*  what was good practices only because we were just developing the field.
*  Yeah. And it's, uh, I mean, it's a really heavy burden. I've, I've had to feel it
*  recently in the last few months, but I think it's a, it's a good one to feel like I've gotten a
*  message more than one from people. You know, I've unfortunately gotten some attention recently and
*  I've gotten messages that say that I have blood in my hands
*  because of working on semi-autonomous vehicles. The idea that you have semi-autonomy means people
*  will become, will lose vigilance and so on. That's actually be humans as we describe. And because
*  of that, because of this idea that we're creating automation, there'll be people be hurt because of
*  it. And I think that's a beautiful thing. I mean, it's, you know, it's many nights where I
*  wasn't able to sleep because of this notion, you know, you really do think about
*  people that might die because of this technology. Of course you can then start rationalizing and
*  saying, well, you know what, 40,000 people die in the United States every year. And we're trying to
*  ultimately try to save lives. But the reality is your code you've written might kill somebody. And
*  that's an important burden to carry with you as you design the code.
*  I don't even think of it as a burden if we train this concept correctly from the beginning. And I
*  use, and not to say that coding is like being a medical doctor, but think about it. Medical doctors,
*  if they've been in situations where their patient didn't survive, right? Do they give up and go away?
*  No, every time they come in, they know that there might be a possibility that this patient might not
*  survive. And so when they approach every decision, like that's in the back of their head. And so why
*  isn't that we aren't teaching, and those are tools though, right? They are given some of the tools
*  to address that so that they don't go crazy. But we don't give those tools so that it does feel
*  like a burden versus something of, I have a great gift and I can do great, awesome good, but with it
*  comes great responsibility. I mean, that's what we teach in terms of, you think about the medical
*  schools, right? Great gift, great responsibility. I think if we just change the messaging a little,
*  great gift, being a developer, great responsibility. And this is how you combine those.
*  But do you think, I mean, this is really interesting. It's outside, I actually have no friends who are
*  surgeons or doctors. What does it feel like to make a mistake in a surgery and somebody to die
*  because of that? Is that something you could be taught in medical school, how to be accepting of
*  that risk? So because I do a lot of work with healthcare robotics, I have not lost a patient,
*  for example. The first one's always the hardest, right? But they really teach the value, right? So
*  they teach responsibility, but they also teach the value. You're saving 40,000, but in order to
*  really feel good about that, when you come to a decision, you have to be able to say at the end,
*  I did all that I could possibly do, right? Versus a, well, I just picked the first widget.
*  So every decision is actually thought through. It's not a habit, it's not a, let me just take
*  the best algorithm that my friend gave me. It's a, is this it? Is this the best? Have I done my best
*  to do good? Right? And so- You're right. And I think burden is the wrong word. It's a gift,
*  but you have to treat it extremely seriously. Correct.
*  On a slightly related note, in a recent paper, The Ugly Truth About Ourselves and Our Robot
*  Creations, you discuss, you highlight some biases that may affect the function of various robotic
*  systems. Can you talk through, if you remember, examples of some? There's a lot of examples.
*  What is bias, first of all? I mean-
*  Yeah. So bias is this, and so bias, which is different than prejudice. So bias is that we
*  all have these preconceived notions about particular, everything from particular groups,
*  to habits, to identity, right? So we have these predispositions. And so when we address a problem,
*  we look at a problem, make a decision, those preconceived notions might affect our outputs,
*  our outcomes. So there, the bias could be positive or negative. And then is prejudice
*  the negative kind of bias? Prejudice is the negative, right? So prejudice is that not only
*  are you aware of your bias, but you are then take it and have a negative outcome, even though you're
*  aware. And that could be gray areas too. There's always gray areas. That's the challenging aspect
*  of all ethical questions. So I always like, so there's a funny one. And in fact, I think it
*  might be in the paper because I think I talk about self-driving cars. But think about this.
*  For teenagers, typically, insurance companies charge quite a bit of money if you have a teenage
*  driver. So you could say that's an age bias, right? But no one will claim, I mean, parents will be
*  grumpy, but no one really says that that's not fair. That's interesting. We don't, that's right.
*  That's right. It's everybody in human factors and safety research, almost, I mean, it's quite
*  ruthlessly critical of teenagers. And we don't question, is that okay? Is that okay to be ageist
*  in this kind of way? It is. And it is ageist, right? It's definitely ageist. There's no question
*  about it. And so this is the gray area, right? Because you know that teenagers are more likely
*  to be in accidents. And so there's actually some data to it. But then if you take that same example
*  and you say, well, I'm going to make the insurance hire for an area of Boston,
*  because there's a lot of accidents. And then they find out that that's correlated with
*  socioeconomics. Well, then it becomes a problem, right? That is not acceptable. But yet the teenager,
*  which is age, it's against age, is, right? And the way we figure that out as a society by having
*  conversations, by having discourse, I mean, throughout history, the definition of what
*  is ethical or not has changed and hopefully always for the better.
*  Correct. Correct. So in terms of bias or prejudice in robotic, in algorithms,
*  what examples do you sometimes think about? So I think about quite a bit the medical domain,
*  just because historically, right, the health care domain has had these biases, typically based on
*  gender and ethnicity, primarily, a little on age, but not so much. Historically, if you think about
*  FDA and drug trials, it's harder to find women that aren't childbearing. And so you may not test on
*  drugs at the same level. Right. So there's these things. And so if you think about robotics,
*  right, something as simple as I like to design an exoskeleton, right? What should the material be?
*  What should the weight be? What should the form factor be? Who are you going to design it around?
*  I will say that in the US, you know, women, average height and weight is slightly different
*  than guys. So who are you going to choose? Like, if you're not thinking about it from the beginning
*  as, you know, okay, I, when I design this and I look at the algorithms and I design the control
*  system and the forces and the torques, if you're not thinking about, well, you have different types
*  of body structure, you're going to design to, you know, what you're used to. Oh, this fits in my,
*  all the folks in my lab. Right. So think about it from the very beginning is important. What
*  about sort of algorithms that train on data kind of thing? Sadly, our society already has a lot of
*  negative bias. And so if we collect a lot of data, even if it's a balanced way, it's going to contain
*  the same bias that a society contains. And so, yeah, was, is there, is there things there that bother
*  you? Yeah. So you actually said something you had said how, um, we have biases, but hopefully we
*  learn from them and we become better. Right. And so that's where we are now. Right. So the data that
*  we're collecting is historic. It's so it's based on these things when we knew it was bad to discriminate,
*  but that's the data we have and we're trying to fix it now, but we're fixing it based on the data
*  that was used in the first place to post. Right. Um, and so, and so the decisions and you can look
*  at everything from the whole, the whole aspect of predictive policing, um, criminal recidivism.
*  There was a recent paper that had the healthcare algorithms, which had a kind of a sensational
*  titles. Uh, I'm not pro sensationalism in titles, but, um, but you read it, right? So yeah, it makes
*  you read it, but I'm like, really? Like, uh, you could have, what's the topic of the sensationalism?
*  I mean, what's underneath it? What's, if you could sort of educate me and what kind of bias
*  creeps into the healthcare space. Yeah. So, um, I mean, you already kind of mentioned. So this one
*  was the headline was racist AI algorithms. Okay. Like, okay. That's totally a clickbait title.
*  Yeah. Um, and so you looked at it and so there was a data that these researchers had collected.
*  Um, I believe I want to say it was either science or nature. It just was just published,
*  but they didn't have a sensational title. It was like the media. And so they had looked at,
*  uh, demographics, I believe between black and white women, right? And they were showed that,
*  uh, there was a discrepancy in the outcomes, right? And so, and it was tied to ethnicity,
*  tied to race. The piece that the researchers did actually went through the whole analysis,
*  but of course, I mean, the, the journalists with AI are problematic across the board.
*  Right. And so this is a problem, right? And so there's this thing about, oh, AI, it has all
*  these problems. We're doing it on historical data and the outcomes are uneven based on gender or
*  ethnicity or age, but I am always saying is like, yes, we need to do better, right? We need to do
*  better. It is our duty to do better, but the worst AI is still better than us. Like, like you take
*  the best of us and we're still worse than the worst AI, at least in terms of these things.
*  And that's actually not discussed, right? And so I think, and that's why the sensational title,
*  right? And it's so, it's like, so then you can have individuals go like, oh, we don't need to
*  use this AI. I'm like, oh, no, no, no, no. I want the AI instead of the, the, the doctors that
*  provided that data because it's still better than that. Right. I think that's really important to
*  linger on. I, the idea that this AI is racist, it's like, well, compared to what sort of the,
*  I think we set unfortunately way too high of a bar for AI algorithms. And in the ethical space,
*  where perfect is, I would argue probably impossible. Then if we set the bar of perfection,
*  essentially, of it has to be perfectly fair, whatever that means is, it means we're setting
*  it up for failure. But that's really important to say what you just said, which is, well, it's still
*  better than human beings. And one of the things I, I think that we don't get enough credit for,
*  just in terms of as developers is that you can now poke at it. Right. So it's harder to say,
*  is this hospital, is this city doing something, right. Until someone brings in a civil case,
*  right. Well, with AI, it can process through all this data and say, hey, yes, there, there was some,
*  an issue here, but here it is, we've identified it. And then the next step is to fix it. I mean,
*  that's a nice feedback loop versus like waiting for someone to sue someone else before it's fixed.
*  Right. And so I think that power, we need to capitalize on a little bit more, right. Instead
*  of having the sensational titles have the, okay, this is a problem and this is how we're fixing it.
*  And people are putting money to fix it because we can make it better. I look at like facial
*  recognition, how Joy, she basically called out a couple of companies and said, hey,
*  and most of them were like, oh, embarrassment. And the next time it had been fixed, right. It had
*  been fixed better. Right. And then it was like, oh, here's some more issues. And I think that
*  conversation then moves that needle to having much more fear and unbiased and ethical aspects, as long
*  as both sides, the developers are willing to say, okay, I hear you. Yes, we are going to improve.
*  And you have other developers are like, you know, Hey, AI it's wrong, but I love it. Right.
*  Yes. So speaking of this really nice notion that AI is maybe flawed, but better than humans.
*  So just made me think of it. One example of flawed humans is our political system. Do you think,
*  or you said judicial as well, do you have a hope for AI sort of being elected for president
*  or running our Congress or being able to be a powerful representative of the people?
*  So I mentioned, and I truly believe that this whole world of AI is in partnerships with people.
*  And so what does that mean? I don't believe or maybe I just don't, I don't believe that we should
*  have an AI for president, but I do believe that a president should use AI as an advisor. Right.
*  Like if you think about it, every president has a cabinet of individuals that have different
*  expertise that they should listen to. Right. Like that's kind of what we do. And you put
*  smart people with smart expertise around certain issues. And you listen, I don't see why AI can't
*  function as one of those smart individuals giving input. So maybe there's an AI on healthcare,
*  maybe there's an AI on education and right. Like all of these things that a human is processing.
*  Right. I, because at the end of the day, there's people that are human that are going to be at the
*  end of the decision. And I don't think as a world, as a culture, as a society, that we would totally
*  believe, and this is us, like this is some fallacy about us, but we need to see that leader, that
*  person as human. And most people don't realize that like leaders have a whole lot of advice,
*  right? Like when they say something, it's not that they woke up. Well, usually they don't wake up in
*  the morning and be like, I have a brilliant idea. Right. It's usually a, okay, let me listen. I have
*  a brilliant idea, but let me get a little bit of feedback on this. Like, okay. And then it's a,
*  yeah, that was an awesome idea. Or it's like, yeah, let me go back. We already talked to a bunch of
*  them, but are there some possible solutions to the bias that's present in our algorithms beyond
*  what we just talked about? So I think there's two paths. One is to figure out how to systematically
*  do the feedback and corrections. So right now it's ad hoc, right? It's a researcher identify some
*  outcomes that are not, don't seem to be fair, right? They publish it, they write about it. And
*  the, either the developer or the companies that have adopted the algorithms may try to fix it.
*  And so it's really ad hoc and it's not systematic. It's kind of like, I'm a researcher,
*  that seems like an interesting problem, which means that there's a whole lot out there that's
*  not being looked at, right? Because it's kind of researcher driven. And I don't necessarily have a
*  solution, but that process I think could be done a little bit better. One way is I'm going to poke
*  a little bit at some of the corporations, right? Like maybe the corporations, when they think about
*  a product, they should, instead of, in addition to hiring these, you know, bug, they give these-
*  Oh yeah, yeah, yeah. Like awards when you find a bug.
*  Yeah. Security bug. You know, let's put it like, we will give the, whatever the award is that we
*  give for the people who find these security holes, find an ethics hole, right? Like find an unfairness
*  hole and we will pay you X for each one you find. I mean, why can't they do that? One is a win-win.
*  They show that they're concerned about it, that this is important, and they don't have to
*  necessarily dedicate their own internal resources. And it also means that everyone who has their own
*  bias lens, like I'm interested in age and so I'll find the ones based on age and I'm interested in
*  gender, right? Which means that you get all of these different perspectives.
*  But you think of it in a data-driven way. So like, sort of, if we look at a company like Twitter,
*  it gets, it's under a lot of fire for discriminating against certain political beliefs.
*  Correct. And sort of, there's a lot of people, this is the sad thing, because I know how hard
*  the problem is and I know the Twitter folks are working really hard at it. Even Facebook,
*  that everyone seems to hate, are working really hard at this. You know, the kind of evidence that
*  people bring is basically anecdotal evidence. Well, me or my friend, all we said is X and for
*  that we got banned. And that's kind of a discussion of saying, well look, that's usually, first of all,
*  the whole thing is taken out of context. So they present sort of anecdotal evidence.
*  And how are you supposed to, as a company, in a healthy way, have a discourse about what is
*  and isn't ethical? How do we make algorithms ethical when people are just blowing everything?
*  They're outraged about a particular anecdotal piece of evidence that's very difficult to sort
*  of contextualize in the big data driven way. Do you have a hope for companies like Twitter and
*  Facebook? Yeah. So I think there's a couple of things going on. First off, remember this whole
*  aspect of we are becoming reliant on technology. We're also becoming reliant on a lot of these,
*  the apps and the resources that are provided. So some of it is kind of anger, like I need you,
*  right? And you're not working for me. Yeah, they're not working for me. They're right.
*  And so some of it, and I wish that there was a little bit of change of rethinking. So some of
*  it is like, oh, we'll fix it in house. No, that's like, okay, I'm a fox and I'm going to watch these
*  hens because I think it's a problem that foxes eat hens. No, right? Be good citizens and say,
*  look, we have a problem and we are willing to open ourselves up for others to come in and look at it
*  and not try to fix it in house. Because if you fix it in house, there's conflict of interest.
*  If I find something, I'm probably going to want to fix it and hopefully the media won't pick it up.
*  And that then causes distrust because someone inside is going to be mad at you and go out and
*  talk about how, yeah, they can the resume survey because it, right? Like, be nice people. Just say,
*  look, we have this issue. Community, help us fix it and we will give you the bug finder fee if you do.
*  Did you ever hope that the community, us as a human civilization on the whole is good
*  and can be trusted to guide the future of our civilization into a positive direction?
*  I think so. So I'm an optimist, right? And, you know, there were some dark times in history,
*  always. I think now we're in one of those dark times. I truly do.
*  In which aspect? The polarization. And it's not just US,
*  right? So if it was just US, I'd be like, yeah, it's a US thing. But we're seeing it worldwide,
*  this polarization. And so I worry about that. But I do fundamentally believe that at the end of the
*  day, people are good. Right? And why do I say that? Because anytime there's a scenario where
*  people are in danger, and I will use, so Atlanta, we had snowmageddon and people can laugh about that.
*  People at the time, so the city closed for, you know, little snow, but it was ice and the city
*  closed down. But you had people opening up their homes and saying, hey, you have nowhere to go,
*  come to my house, right? Hotels were just saying like, sleep on the floor. Like places like, you
*  know, the grocery stores were like, hey, here's food. There was no like, oh, how much are you
*  going to pay me? It was like this, such a community and like people who didn't know each other,
*  strangers were just like, can I give you a ride home? And that was a point I was like, you know
*  what? Like, that that that reveals that the deeper thing is, is there's a compassionate love that we
*  all have within us. It's just that when all that is taken care of and get bored, we love drama.
*  And that's, I think almost like the division is a sign of the times being good, is that it's just
*  entertaining on some unpleasant mammalian level to watch, to disagree with others.
*  And Twitter and Facebook are actually taking advantage of that in a sense because it brings
*  you back to the platform and they're advertiser driven, so they make a lot of money. So you go
*  back and you're like, love doesn't sell quite as well in terms of advertisement. It doesn't.
*  So you've started your career at NASA Jet Propulsion Laboratory,
*  but before I ask a few questions there, have you happened to have ever seen Space Odyssey,
*  2001 Space Odyssey? Yes. Okay. Do you think, do you think HAL 9000, so we're talking about ethics,
*  do you think HAL did the right thing by taking the priority of the mission over the lives of
*  astronauts? Do you think HAL is good or evil?
*  Easy questions. Yeah. HAL was misguided. You're one of the people that would be in charge of
*  an algorithm like HAL. So how would you do better? If you think about what happened was there was no
*  fail safe. So we perfection, right? Like what is that? I'm going to make something that I think is
*  perfect, but if my assumptions are wrong, it'll be perfect based on the wrong assumptions.
*  That's something that you don't know until you deploy and then you're like, oh yeah,
*  messed up. But what that means is that when we design software, such as in Space Odyssey,
*  when we put things out, that there has to be a fail safe. There has to be the ability that once
*  it's out there, we can grade it as an F and it fails and it doesn't continue. There's some way
*  that it can be brought in and removed and that's aspect because that's what happened with HAL. It
*  was like assumptions were wrong. It was perfectly correct based on those assumptions and there was
*  no way to change it, change the assumptions at all. And the change, the fallback would be to a
*  human. So you ultimately think like humans should be, it's not turtles or AI all the way down.
*  At some point there's a human that actually makes a difference. I still think that, and again,
*  because I do human robot interaction, I still think the human needs to be part of the equation
*  at some point. So what, just looking back, what are some fascinating things in robotics space
*  that NASA was working at the time or just in general, what have you gotten to play with and
*  what are your memories from working at NASA? Yeah, so one of my first memories was they were working
*  on a surgical robot system that could do eye surgery, right? And this was back in, oh my gosh,
*  it must've been, oh, maybe 92, 93, 94. So it's almost like a remote operation.
*  Yeah, it was remote operation. In fact, you can even find some old tech reports on it.
*  So think of it like now we have DaVinci, right? Think of it, but these were the late 90s,
*  right? And I remember going into the lab one day and I was like, what's that? And of course,
*  it wasn't pretty, right? Because the technology, but it was functional. And you had this individual
*  that could use version of haptics to actually do the surgery. And they had this mock-up of a human
*  face and the eyeballs. And you can see this little drill. And I was like, oh, that is so cool.
*  That one I vividly remember because it was so outside of my possible thoughts of what could be
*  done. It's the kind of precision and I mean, what's the most amazing of a thing like that?
*  I think it was the precision. It was the kind of first time that I had physically seen this robot
*  machine human interface, right? Because manufacturing had been, you saw those kind of big robots,
*  right? But this was like, oh, this is in a person. There's a person and a robot in the same space.
*  The meeting them in person. For me, it was a magical moment that I can't, it was life transforming
*  that I recently met Spot Mini from Boston Dynamics. I don't know why, but on the human
*  robot interaction, for some reason, I realized how easy it is to anthropomorphize. And it was,
*  I don't know, it was almost like falling in love with this feeling of meeting. And I've obviously
*  seen these robots a lot on video and so on, but meeting in person, just having that one on one
*  time is different. So have you had a robot like that in your life that made you maybe fall in
*  love with robotics? Like meeting in person. I mean, I loved robotics. Yeah, so I was a 12 year old,
*  I'm gonna be a roboticist. Actually, I called it cybernetics. But so my motivation was Bionic
*  Woman. I don't know if you know that. And so, I mean, that was like a seminal moment, but I didn't
*  meet, like that was TV, right? Like it wasn't like I was in the same space and I met, I was like,
*  oh my gosh, you're like real. Just looking at Bionic Woman, which by the way, because I read
*  that about you, I watched a bit bits of it and it's just so, no offense, terrible.
*  It's cheesy. Look at it now. I've seen a couple of reruns lately.
*  But of course, at the time, it's probably... But the sound effects.
*  Especially when you're younger, it just catches you. But which aspect, did you think of it,
*  you mentioned cybernetics, did you think of it as robotics or did you think of it as almost
*  constructing artificial beings? Is it the intelligent part that captured your
*  fascination or was it the whole thing, like even just the limbs and just the...
*  So for me, it would have, in another world, I probably would have been more of a biomedical
*  engineer because what fascinated me was the bionic, was the parts, like the bionic parts,
*  the limbs, those aspects of it. Are you especially drawn to humanoid or human-like
*  robots? I would say human-like, not humanoid.
*  And when I say human-like, I think it's this aspect of that interaction, whether it's social
*  and it's like a dog, that's human-like because it understands us, it interacts with us at that very
*  social level. Humanoid is a part of that, but only if they interact with us as if we are human.
*  But just to linger on NASA for a little bit, what do you think, maybe if you have other memories,
*  but also what do you think is the future of robots in space? You mentioned HAL,
*  but there's incredible robots that NASA's working on in general, thinking about in our...
*  As we venture out, human civilization ventures out into space, what do you think the future
*  of robots is there? Yeah, so I mean, there's the near term. For example, they just announced the
*  rover that's going to the moon, which that's kind of exciting, but that's near term.
*  My favorite, favorite, favorite series is Star Trek. I really hope, and even Star Trek,
*  if I calculate the years, I wouldn't be alive, but I would really, really love to be in that world.
*  Even if it's just at the beginning, like, you know, like voyage, like adventure one.
*  So basically living in space with what robots, what robots...
*  With data. What role?
*  Data would have to be, even though that was later.
*  So data is a robot that has human-like qualities.
*  Right, without the emotion chip, yeah.
*  You don't like emotion in your robots.
*  So data with the emotion chip was kind of a mess, right? It took a while for that then to adapt.
*  And so why was that an issue? The issue is that emotions make us irrational agents.
*  That's the problem. And yet he could think through things, even if it was based on an emotional
*  scenario, right? Based on pros and cons. But as soon as you made him emotional,
*  one of the metrics he used for evaluation was his own emotions, not people around him.
*  We do that as children, right? So we're very egocentric.
*  We are very egocentric.
*  And so isn't that just an early version of the emotion chip then? I haven't watched much Star
*  Trek.
*  Except I have also met adults. And so that is a developmental process. And I'm sure there's a
*  bunch of psychologists that could go through. You can have a 60-year-old adult who has the
*  emotional maturity of a 10-year-old, right? And so there's various phases that people
*  should go through in order to evolve. And sometimes you don't.
*  So how much psychology do you think, a topic that's rarely mentioned in robotics,
*  but how much does psychology come to play when you're talking about
*  HRI, human-robot interaction, when you have to have robots that actually interact with you?
*  Ton. So my group, as well as I, read a lot in the cognitive science literature,
*  as well as the psychology literature. Because they understand a lot about human-human
*  relations and developmental milestones and things like that. And so we tend to look to see
*  what's been done out there. Sometimes what we'll do is we'll try to match that to see,
*  is that human-human relationship the same as human-robot? Sometimes it is, and sometimes
*  it's different. And then when it's different, we try to figure out, okay, why is it different
*  in this scenario, but it's the same in the other scenario, right? And so we try to do that quite
*  a bit. Would you say that's, if we're looking at the future of human-robot interaction,
*  would you say the psychology piece is the hardest? I mean, it's a funny notion for you. I don't know
*  if you consider, yeah. I mean, one way to ask it, do you consider yourself a roboticist or a
*  psychologist? Oh, I consider myself a roboticist that plays the act of a psychologist. But if you
*  were to look at yourself 20, 30 years from now, do you see yourself more and more wearing the
*  psychology hat? Another way to put it is, are the hard problems in human-robot interactions
*  fundamentally psychology, or is it still robotics, the perception manipulation planning and all that
*  kind of stuff? It's actually neither. The hardest part is the adaptation and the interaction.
*  The learning.
*  It's the interface, it's the learning. And so if I think of, I've become much more of a roboticist
*  slash AI person than when I, originally, again, I was about the biotics. I was electrical engineer,
*  I was control theory, right? And then I started realizing that my algorithms needed human data,
*  right? And so then I was like, okay, what is this human thing? How do I incorporate human data? And
*  then I realized that human perception had, there was a lot in terms of how we perceive the world,
*  and so trying to figure out how do I model human perception for my... And so I became a HRI person,
*  human-robot interaction person, from being a control theory and realizing that humans actually
*  offered quite a bit. And then when you do that, you become more of an artificial intelligence AI.
*  And so I see myself evolving more in this AI world under the lens of
*  robotics having hardware interacting with people.
*  So you're a world-class expert researcher in robotics, and yet others, there's a few,
*  it's a small but fierce community of people, but most of them don't take the journey into the age
*  of HRI, into the human. So why did you brave into the interaction with humans?
*  It seems like a really hard problem. It's a hard problem, and it's very risky as an academic.
*  And I knew that when I started down that journey, that it was very risky as an academic
*  in this world that was nuanced, it was just developing. We didn't even have a conference,
*  at the time, because it was the interesting problems. That was what drove me. It was
*  the fact that I looked at what interests me in terms of the application space and the problems,
*  and that pushed me into trying to figure out what people were and what humans were and how to adapt
*  to them. If those problems weren't so interesting, I'd probably still be sending rovers to glaciers,
*  right? But the problems were interesting. And the other thing was that they were hard.
*  I like having to go into a room and being like, I don't know what to do, and then going back and
*  saying, okay, I'm going to figure this out. I'm not driven when I go in like, oh, there are no
*  surprises. I don't find that satisfying. If that was the case, I'd go someplace and make a lot more
*  money, right? I think I stay an academic and choose to do this because I can go into a room and I'm
*  like, that's hard. Yeah, I think just from my perspective, maybe you can correct me on it, but
*  if I just look at the field of AI broadly, it seems that human-robot interaction has the most,
*  one of the most number of open problems. Like people, especially relative to how many people
*  are willing to acknowledge that there are this because most people are just afraid of the human,
*  so they don't even acknowledge how many open problems there are. But it's a, in terms of
*  difficult problems to solve, exciting spaces, it seems to be incredible for that. It is,
*  and it's exciting. You mentioned trust before. What role does trust from interacting with
*  autopilot to in the medical context, what role does trust play in the human-robot interactions?
*  So some of the things I study in this domain is not just trust, but it really is overtrust.
*  How do you think about overtrust? Like what is, first of all, what is,
*  what is trust and what is overtrust? Basically, the way I look at it is
*  trust is not what you click on a survey. Trust is about your behavior. So if you interact with
*  the technology based on the decision or the actions of the technology, as if you trust that
*  decision, then you're trusting. Even in my group, we've done surveys that on the thing do you
*  trust robots? Of course not. Would you follow this robot in a burning building? Of course not.
*  Then you look at their actions and you're like, clearly your behavior does not match what you
*  think or what you think you would like to think. So I'm really concerned about the behavior,
*  because that's really at the end of the day, when you're in the world, that's what will impact
*  others around you. It's not whether before you went onto the street, you clicked on,
*  I don't trust self-driving cars. From an outsider perspective, it's always frustrating to me. Well,
*  I read a lot, so I'm an insider in a certain philosophical sense. It's frustrating to me
*  how often trust is used in surveys and how people make claims out of any kind of finding they make
*  while somebody is clicking on answer. Because trust is behavior. You said it beautifully.
*  Action, your own behavior is what trust is. Everything else is not even close. It's almost
*  like absurd comedic poetry that you weave around your actual behavior. So some people can say
*  their trust, I trust my wife, husband or not, whatever, but the actions is what speaks volumes.
*  Right. You bug their car. You probably don't trust them.
*  I trust them, but I'm just making sure. No, no, that's, yeah.
*  It's like even if you think about cars, I think it's a beautiful case. I came here
*  at some point, I'm sure on either Uber or Lyft. I remember when it first came out.
*  I bet if they had had a survey, would you get in the car with a stranger and pay them?
*  Yes. How many people do you think would have said, like, really? Wait, even worse, would you get in
*  the car with a stranger at 1 a.m. in the morning to have them drop you home as a single female?
*  How many people would say, that's stupid? Now look at where we are. People put kids, right?
*  Oh yeah, my child has to go to school and I'm going to put my kid in this car with a stranger.
*  I mean, it's just fascinating how like what we think we think is not necessarily matching our
*  behavior. Yeah, and certainly with robots, with autonomous vehicles and all the kinds of robots
*  you work with, that's, it's, yeah, it's the way you answer it, especially if you've never interacted
*  with that robot before. If you haven't had the experience, you being able to respond correctly
*  on a survey is impossible. But what role does trust play in the interaction, do you think?
*  Like is it good to trust a robot? What does over trust mean? Is it good to kind of how you feel
*  about autopilot currently, which is like from a roboticist perspective is like, oh, so very
*  cautious. Yeah, so this is still an open area of research. But basically what I would like
*  in a perfect world is that people trust the technology when it's working 100% and people
*  will be hypersensitive and identify when it's not. But of course we're not there. That's the ideal
*  world. But we find is that people swing, right? They tend to swing, which means that if my first,
*  and like we have some papers, like first impressions is everything, right? If my first
*  instance with technology with robotics is positive, it mitigates any risk, it correlates with like best
*  outcomes. It means that I'm more likely to either not see it when it makes a mistakes or faults,
*  or I'm more likely to forgive it. And so this is a problem because technology is not 100% accurate,
*  right? It's not 100% accurate, although it may be perfect.
*  How do you get that first moment right, do you think? There's also an education about
*  the capabilities and limitations of the system. Do you have a sense of
*  how you educate people correctly in that first interaction?
*  Again, this is an open-ended problem. So one of the study that actually has given me some hope
*  that I was trying to figure out how to put in robotics. So there was a research study that
*  has showed for medical AI systems giving information to radiologists about, you know,
*  here you need to look at these areas on the X-ray. What they found was that when the system
*  provided one choice, there was this aspect of either no trust or over-trust, right? Like,
*  I'm not going, I don't believe it at all, or a yes, yes, yes, yes, and they would miss things,
*  right? Instead, when the system gave them multiple choices, like here are the three,
*  even if it knew, like, you know, it had estimated that the top area you need to look at was, you
*  know, some place on the X-ray, if it gave like one plus others, the trust was maintained and
*  the accuracy of the entire population increased, right? So basically it was a, you're still
*  trusting the system, but you're also putting in a little bit of like your human expertise,
*  like your human decision processing into the equation. So it helps to mitigate that over-trust
*  risk. Yeah. So there's a fascinating balance to have to strike. Yeah. I haven't figured out again.
*  Right. So this is exciting open area research. Exactly. So what are some
*  exciting applications of human-robot interaction? You started a company, maybe you can talk about
*  the exciting efforts there, but in general also what other space can robots interact with humans
*  and help? Yeah. So besides healthcare, because, you know, that's my bias lens. My other bias lens
*  is education. I think that, well, one, we definitely, in the U.S., you know, we're doing
*  okay with teachers, but there's a lot of school districts that don't have enough teachers. If you
*  think about the teacher-student ratio for at least public education in some districts, it's crazy.
*  It's like, how can you have learning in that classroom, right? Because you just don't have
*  the human capital. And so if you think about robotics, bringing that in to classrooms,
*  as well as the afterschool space, where they offset some of this lack of resources in certain
*  communities, I think that's a good place. And then turning on the other end is using these systems
*  then for workforce retraining and dealing with some of the things that are going to come out
*  later on of job loss, like thinking about robots and in AI systems for retraining and
*  workforce development. I think that's exciting areas that can be pushed even more and it would
*  have a huge, huge impact. What would you say are some of the open problems in education? Sort of,
*  it's exciting. So young kids and the older folks or just folks of all ages who need to be retrained,
*  who need to sort of open themselves up to a whole other area of work. What are the problems to be
*  solved there? How do you think robots can help? We have the engagement aspect, right? So we can
*  figure out the engagement. What do you mean by engagement? So identifying whether a person
*  is focused is like that we can figure out. What we can figure out, and there's some positive results
*  in this, is that personalized adaptation based on any concepts, right? So imagine I think about,
*  I have an agent and I'm working with a kid learning, I don't know, Algebra 2. Can that same agent then
*  switch and teach some type of new coding skill to a displaced mechanic? What does that actually look
*  like, right? Hardware might be the same, content is different, two different target demographics
*  of engagement. How do you do that? How important do you think personalization is in human-robot
*  interaction? And not just mechanic or student, but literally to the individual human being.
*  I think personalization is really important, but a caveat is that I think we'd be okay if we can
*  personalize to the group, right? And so if I can label you along some certain dimensions,
*  then even though it may not be you specifically, I can put you in this group. So the sample size,
*  this is how they best learn, this is how they best engage. Even at that level, it's really important.
*  And it's because, I mean, it's one of the reasons why educating in large classrooms is so hard,
*  right? You teach to the median, but there's these individuals that are struggling and then you have
*  highly intelligent individuals and those are the ones that are usually kind of left out. So highly
*  intelligent individuals may be disruptive and those who are struggling might be disruptive
*  because they're both bored. Yeah. And if you narrow the definition of the group or in the
*  size of the group enough, you'll be able to address their individual needs, but really group,
*  most important group needs. Right. Right. And that's kind of what a lot of successful recommender
*  systems do with Spotify and so on. It's sad to believe, but as a music listener, probably in
*  some sort of large group. It's very sadly predictable. You have been labeled. Yeah,
*  I've been labeled and successfully so because they're able to recommend stuff.
*  Yeah, but applying that to education, right? There's no reason why it can't be done.
*  Do you have a hope for our education system? I have more hope for workforce development.
*  And that's because I'm seeing investments, even if you look at VC investments in education,
*  the majority of it has lately been going to workforce retraining. Right. And so I think that
*  government investments is increasing. There's like a claim and some of it's based on fear,
*  right? Like AI is going to come and take over all these jobs. What are we going to do with all these
*  non-paying taxes that aren't coming to us by our citizens? And so I think I'm more hopeful for that.
*  I'm not so hopeful for early education because it's this, it's still a who's going to pay for it.
*  And you won't see the results for like 16 to 18 years. It's hard for people to wrap their
*  heads around that. But on the retraining part, what are your thoughts? There's a candidate,
*  Andrew Yang, running for president and saying that sort of AI automation robots, universal basic
*  income, universal basic income in order to support us as we kind of automation takes people's jobs
*  and allows you to explore and find other means. Like, do you have a concern of society transforming
*  effects of automation and robots and so on? I do. I do know that AI robotics will displace
*  workers. Like we do know that, but there'll be other workers that will be defined, new jobs.
*  What I worry about is that's not what I worry about. Like will all the jobs go away?
*  What I worry about is the type of jobs that will come out, right? Like people who graduate from
*  Georgia Tech will be okay, right? We give them the skills. They will adapt even if their current
*  job goes away. I do worry about those that don't have that quality of an education, right? Will they
*  have the ability, the background to adapt to those new jobs? That I don't know. That I worry about,
*  which will create even more polarization in our society, internationally and everywhere. I worry
*  about that. I also worry about not having equal access to all these wonderful things that AI can
*  do and robotics can do. I worry about that. People like me from Georgia Tech, from say MIT,
*  will be okay, right? But that's such a small part of the population that we need to think much more
*  globally of having access to the beautiful things, whether it's AI in healthcare, AI in education,
*  AI in politics, right? I worry about that. And that's part of the thing that you were talking
*  about is people that build the technology have to be thinking about ethics, have to be thinking
*  about access and all those things. And not just a small subset. Let me ask some philosophical,
*  slightly romantic questions. People that will listen to this will be like, here he goes again.
*  Okay. Do you think one day we'll build an AI system that a person can fall in love with
*  and it would love them back? Like in the movie Her, for example.
*  Yeah. Although she kind of didn't fall in love with him. Or she fell in love with like a million
*  other people, something like that. You're the jealous type. I see. We humans are the jealous.
*  Yes. So I do believe that we can design systems where people would fall in love with their robot,
*  with their AI partner. That I do believe. Because it's actually, and I don't like to use the word
*  manipulate, but as we see, there are certain individuals that can be manipulated if you
*  understand the cognitive science about it, right? Right. So, I mean, if you could think of all close
*  relationship and love in general as a kind of mutual manipulation, that dance, the human dance,
*  I mean, manipulation is a negative connotation. And that's why I don't like to use that word
*  particularly. I guess another way to phrase it is you're getting at it could be algorithmatized
*  or something. It could be a- The relationship building part can be.
*  Yeah. I mean, just think about it. We have, and I don't use dating sites, but from what I heard,
*  there are some individuals that have been dating that have never saw each other. In fact,
*  there's a show, I think, that tries to weed out fake people. There's a show that comes out,
*  right? Because people start faking. What's the difference of that person on the other end being
*  an AI agent, right? And having a communication, are you building a relationship remotely? There's
*  no reason why that can't happen. In terms of human-robot interaction,
*  you've kind of mentioned with data, emotion can be problematic if not implemented well, I suppose.
*  What role does emotion and some other human-like things, the imperfect things come into play here
*  for good human-robot interaction and something like love? Yeah. So in this case, and you had asked,
*  can an AI agent love a human back? I think they can emulate love back, right? And so what does
*  that actually mean? It just means that if you think about their programming, they might put the other
*  person's needs in front of theirs in certain situations, right? Think about it as return on
*  investment. What's my return on investment? As part of that equation, that person's happiness
*  has some type of algorithm waiting to it. And the reason why is because I care about them,
*  right? That's the only reason, right? But if I care about them and I show that, then
*  my final objective function is length of time of the engagement, right? So you can think of how to
*  do this actually quite easily. And so- But that's not love?
*  Well, so that's the thing. I think it emulates love because we don't have a classical definition
*  of love. Right. And we don't have the ability to look into each other's minds to see the algorithm.
*  I mean, I guess what I'm getting at is, is it possible that, especially if that's learned,
*  especially if there's some mystery and black box nature to the system, how is that-
*  How is it any different? How is it any different? And in terms of sort
*  of if the system says, I'm conscious, I'm afraid of death, and it does indicate that it loves you.
*  Another way to sort of phrase it, I'd be curious to see what you think. Do you think there'll be a
*  time when robots should have rights? You've kind of phrased the robot in a very roboticist way,
*  and just a really good way, but saying, okay, well, there's an objective function and I could
*  see how you can create a compelling human robot interaction experience that makes you believe that
*  the robot cares for your needs and even something like loves you. But what if the robot says,
*  please don't turn me off? What if the robot starts making you feel like there's an entity
*  of being a soul there? Do you think there'll be a future? Hopefully you won't laugh too much at
*  this, but where they do ask for rights? So I can see a future if we don't address it
*  in the near term where these agents, as they adapt and learn, could say, hey,
*  this should be something that's fundamental. I hopefully think that we would address it before
*  it gets to that point. So you think that's a bad future? Is that a negative thing where they ask
*  or being discriminated against? I guess it depends on what role have they attained at that point.
*  So if I think about now- Careful what you say because the robot's 50 years from now will be
*  listening to this and you'll be on TV saying, this is what roboticists used to believe.
*  I do not, right? And so this is my, and as I said, I have a biased lens and my robot friends will
*  understand that. But so if you think about it, and I actually put this in kind of the, as a roboticist,
*  you don't necessarily think of robots as human with human rights, but you could think of them
*  either in the category of property or you could think of them in the category of animals.
*  And so both of those have different types of rights. So animals have their own rights as a
*  living being, but they can't vote, they can't write, they can be euthanized.
*  But as humans, if we abuse them, we go to jail. So they do have some rights that protect them,
*  but don't give them the rights of citizenship. And then if you think about property, property,
*  the rights are associated with the person. So if someone vandalizes your property or steals
*  your property, there are some rights, but it's associated with the person who owns that.
*  If you think about it, back in the day, and if you remember, we talked about how society has
*  changed, women were property, right? They were not thought of as having rights. They were thought of
*  as property of, like they're- Yeah, assaulting a woman meant assaulting the property of somebody
*  else. Exactly. And so what I envision is that we will establish some type of norm at some point,
*  but that it might evolve, right? If you look at women's rights now, there are still some countries
*  that don't have, and the rest of the world is like, why? That makes no sense, right? And so I do see
*  a world where we do establish some type of grounding. It might be based on property rights,
*  it might be based on animal rights. And if it evolves that way, I think we will have this
*  conversation at that time, because that's the way our society traditionally has evolved.
*  Beautifully put. Just out of curiosity, Anki, Jibo, Mayfield Robotics,
*  with the RobotCurry, Sci-Fi Works, Rethink Robotics, were all these amazing robotics
*  companies led, created by incredible roboticists, and they've all went out of business recently.
*  Why do you think they didn't last longer? Why is it so hard to run a robotics company, especially one
*  like these, which are fundamentally HRI, human-robot interaction robots?
*  Yeah. Each one has a story. Only one of them I don't understand.
*  And that was Anki. That's actually the only one I don't understand.
*  I don't understand it either.
*  I mean, I look from the outside, I've looked at their sheets, I've looked at the data that's-
*  Oh, you mean business-wise?
*  Yeah.
*  Yeah. And I look at that data, and I'm like, they seem to have product market fit.
*  So that's the only one I don't understand. The rest of it was product market fit.
*  What's product market fit? Just that of, how do you think about it?
*  Yeah. So although Rethink Robotics was getting there, right? But I think it's just the timing,
*  their clock just timed out. I think if they'd been given a couple more years,
*  they would have been okay. But the other ones were still fairly early by the time they got
*  into the market. And so product market fit is, I have a product that I want to sell at a certain
*  price. Are there enough people out there, the market, that are willing to buy the product at
*  that market price for me to be a functional, viable, profit bearing company? Right? So product
*  market fit. If it costs you a thousand dollars and everyone wants it and only is willing to pay a
*  dollar, you have no product market fit. Even if you could sell it for, it's enough for a dollar,
*  because you can't. So how hard is it for robots? Maybe if you look at iRobot, the company that makes
*  Roombas vacuum cleaners, can you comment on, did they find the right product, market product fit?
*  Are people willing to pay for robots is also another kind of question underlying all this.
*  So if you think about iRobot and their story, right? When they first, they had enough of a
*  runway, right? When they first started, they weren't doing vacuum cleaners, right? They were
*  they were contracts, primarily government contracts, designing robots. I mean, that's
*  what they were. That's how they started, right? And they still do a lot of incredible work there,
*  but yeah, that was the initial thing that gave them enough funding to then try to, the vacuum
*  cleaner is what I've been told was not like their first rendezvous in terms of designing a product,
*  right? And so they were able to survive until they got to the point that they found a
*  product price market, right? And even with, if you look at the Roomba, the price point now
*  is different than when it was first released, right? It was an early adopter price, but they
*  found enough people who were willing to fund it. And I mean, I forgot what their loss profile was
*  for the first couple of years, but they became profitable in sufficient time that they didn't
*  have to close their doors. So they found the right, there's still, there's still people
*  willing to pay a large amount of money, sort of over a thousand dollars for a vacuum cleaner.
*  Unfortunately for them, now that they've proved everything out, figured it all out, now there's
*  competitors. Yeah. And so that's, that's the next thing, right? The competition, and they have
*  quite a number even internationally. Like there are some products out there you can go to Europe
*  and be like, oh, I didn't even know this one existed. So this is the thing though, like with
*  any market, I would, this is not a bad time, although as a roboticist, it's kind of depressing,
*  but I actually think about things like with, I would say that all of the companies that are
*  now in the top five or six, they weren't the first to the stage, right? Like Google was not the first
*  search engine, sorry, Alta Vista, right? Facebook was not the first, sorry, MySpace, right? Like
*  think about it, they were not the first players. Those first players, like they're not in the top
*  five, 10 of fortune 500 companies, right? They proved, they started to prove out the market.
*  They started to get people interested. They started the buzz, but they didn't make it to that next
*  level. But the second batch, right? The second batch, I think might make it to the next level.
*  When do you think the, the Facebook of,
*  the Facebook of robotics? Sorry, I take that phrase back because people deeply, for some reason,
*  well, I know why, but it's, I think, exaggerated distrust Facebook because of the privacy concerns
*  and so on. And with robotics, one of the things you have to make sure is all the things we talked
*  about is to be transparent and have people deeply trust you to let a robot into their lives, into
*  their home. When do you think the second batch of robots is it five, 10 years, 20 years that
*  we'll have robots in our homes and robots in our hearts?
*  So if I think about, because I try to follow the VC kind of space in terms of robotic investments.
*  And right now, and I don't know if they're going to be successful. I don't know if this is the
*  second batch, but there's only one batch that's focused on like the first batch, right? And then
*  there's all these self-driving Xs, right? And so I don't know if they're a first batch of something
*  or if like, I don't know quite where they fit in, but there's a number of companies, the co-robot,
*  I call them co-robots that are still getting VC investments. They, some of them have some of the
*  flavor of like rethink robotics. Some of them have some of the flavor of like Curie. What's a co-robot?
*  So basically a robot and human working in the same space. So some of the companies are
*  focused on manufacturing. So having a robot and human working together in a factory,
*  some of these co-robots are robots and humans working in the home, working in clinics. Like
*  there's different versions of these companies in terms of their products, but they're all,
*  so we think robotics would be like one of the first, at least well-known companies focus on
*  this space. So I don't know if this is a second batch or if this is still part of the first batch.
*  That I don't know. And then you have all these other companies in this self-driving, you know,
*  space. And I don't know if that's a first batch or again, a second batch.
*  Yeah. So there's a lot of mystery about this now. Of course, it's hard to say that this is the second
*  batch until it, you know, it proves out, right? Correct. Yeah, we need a unicorn.
*  Yeah, exactly. Why do you think people are so afraid, at least in popular culture,
*  of legged robots like those worked in Boston Dynamics or just robotics in general,
*  if you were to psychoanalyze that fear, what do you make of it? And should they be afraid? Sorry.
*  So should people be afraid? I don't think people should be afraid, but with a caveat.
*  I don't think people should be afraid given that most of us in this world understand
*  that we need to change something, right? So given that. Now, if things don't change,
*  be very afraid. Which is the dimension of change that's needed? So changing, thinking about the
*  ramifications, thinking about like the ethics, thinking about like the conversation is going on,
*  right? It's not, it's no longer a, we're going to deploy it and forget that, you know,
*  this is a car that can kill pedestrians that are walking across the street, right? We're not in
*  that stage. We're putting these roads out. There are people out there. Yes. A car could be a weapon.
*  People are now solutions aren't there yet, but people are thinking about this as we need to be
*  ethically responsible as we send these systems out, robotics, medical, self-driving. And military,
*  too. And military. Which is not as often talked about, but it's really where probably
*  these robots will have a significant impact as well. Correct, correct. Right. Making sure that
*  they can think rationally, even having the conversations, who should pull the trigger,
*  right? But overall, you're saying if we start to think more and more as a community about these
*  ethical issues, people should not be afraid. Yeah, I don't think people should be afraid. I think
*  that the return on investment, the impact, positive impact will outweigh any of the potentially
*  negative impacts. Do you have worries of existential threats of robots or AI that some people kind of
*  talk about and romanticize about and then in the next decade, next few decades? No, I don't.
*  Singularity will be an example. So my concept is that, so remember robots, AI is designed by people.
*  Yes. It has our values. And I always correlate this with a parent and a child. Right? So think
*  about it. As a parent, what do we want? We want our kids to have a better life than us. We want
*  them to expand. We want them to experience the world. And then as we grow older, our kids think
*  and know they're smarter and better and more intelligent and have better opportunities. And
*  they may even stop listening to us. They don't go out and then kill us. Right? Think about it. It's
*  because we, it's instilled in them values. We instilled in them this whole aspect of community.
*  And yes, even though you're maybe smarter and have more money and dah, dah, dah, it's still about this
*  love, caring relationship. And so that's what I believe. So even if like, you know,
*  we've created the singularity in some archaic system back in like 1980, that suddenly evolves.
*  The fact is it might say, I am smarter. I am sentient. These humans are really stupid.
*  But I think it'll be like, yeah, but I just can't destroy them. Yeah. For sentimental value,
*  it's still just for it to come back for Thanksgiving dinner every once in a while.
*  Exactly.
*  This so beautifully put. You've, you've also said that the matrix may be one of your more
*  favorite AI related movies. Can you elaborate why? Yeah, it is one of my favorite movies. And it's
*  because it represents kind of all the things I think about. So there's a symbiotic relationship
*  between robots and humans. Right. That symbiotic relationship is that they don't destroy us. They
*  enslave us. Right. But think about it. Even though they enslaved us, they needed us to be happy.
*  Right. And in order to be happy, they had to create this crudy world that they then had to
*  live in. Right. That's the whole premise. But then there were humans that had a choice.
*  Right. Like you had a choice to stay in this horrific, horrific world where it was your
*  fantasy life with all of the anomalies, perfection, but not accurate. Or you can choose to be on your
*  own and have maybe no food for a couple of days, but you were totally autonomous. And so I think
*  of that as, and that's why, so it's not necessarily us being enslaved, but I think about us having the
*  symbiotic relationship. Robots and AI, even if they become sentient, they're still part of our
*  society and they will suffer just as much as we. Just as us. And there will be some kind of equilibrium
*  that we'll have to find some symbiotic relationship. Right. And then you have the
*  ethicists, the robotics folks that are like, no, this has got to stop. I will take the other pill
*  in order to make a difference. So if you could hang out for a day with a robot,
*  real or from science fiction, movies, books safely and get to pick his or her, their brain,
*  who would you pick?
*  Got to say it's data. Data. I was going to say Rosie, but I don't, I'm not really interested in
*  her brain. I'm interested in data's brain. Data pre or post-emotion chip? Pre.
*  But don't you think it'd be a more interesting conversation post-emotion chip? Yeah, it would
*  be a drama and I, you know, I'm human. I deal with drama all the time. But the reason why I want to
*  pick data's brain is because I could have a conversation with him and ask, for example,
*  how can we fix this ethics problem? Right. And he could go through like the rational thinking
*  and through that, he could also help me think through it as well. And so that's,
*  there's like these questions, fundamental questions, I think I could ask him that he
*  would help me also learn from. And that fascinates me. I don't think there's a better place to end it.
*  Ayana, thank you so much for talking to us. It was an honor. Thank you. Thank you. This was fun.
*  Thanks for listening to this conversation and thank you to our presenting sponsor, Cash App.
*  Download it, use code LexPodcast. You'll get $10 and $10 will go to FIRST, a STEM education
*  nonprofit that inspires hundreds of thousands of young minds to become future leaders and
*  innovators. If you enjoy this podcast, subscribe on YouTube, get five stars on Apple Podcast,
*  follow on Spotify, support on Patreon, or simply connect with me on Twitter.
*  And now let me leave you with some words of wisdom from Arthur C. Clark.
*  Whether we are based on carbon or on silicon makes no fundamental difference.
*  We should each be treated with appropriate respect.
*  Thank you for listening and hope to see you next time.
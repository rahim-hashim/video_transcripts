---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 4714s
Video Keywords: []
Video Views: 68899
Video Rating: None
Video Description: 
---

# Sebastian Thrun Flying Cars, Autonomous Vehicles, and Education  Lex Fridman Podcast #59
**Lex Fridman:** [December 21, 2019](https://www.youtube.com/watch?v=ZPPAOakITeQ)
*  The following is a conversation with Sebastian Thrun.
*  He's one of the greatest roboticists, computer scientists, and educators of our time.
*  He led the development of the autonomous vehicles at Stanford that won the 2005
*  DARPA Grand Challenge and placed second in the 2007 DARPA Urban Challenge.
*  He then led the Google self-driving car program, which launched the self-driving car revolution.
*  He taught the popular Stanford course on artificial intelligence in 2011,
*  which was one of the first massive open online courses, or MOOCs, as they're commonly called.
*  That experience led him to Cofound Udacity, an online education platform.
*  If you haven't taken courses on it yet, I highly recommend it.
*  Their self-driving car program, for example, is excellent.
*  He's also the CEO of Kitty Hawk, a company working on building flying cars, or more technically,
*  EV TOLs, which stands for electric vertical takeoff and landing aircraft.
*  He has launched several revolutions and inspired millions of people.
*  But also, as many know, he's just a really nice guy.
*  It was an honor and a pleasure to talk with him.
*  This is the Artificial Intelligence Podcast.
*  If you enjoy it, subscribe on YouTube, give it five stars on Apple Podcasts,
*  follow it on Spotify, support it on Patreon, or simply connect with me on Twitter at Lex Friedman,
*  spelled F-R-I-D-M-A-N. If you leave a review on Apple Podcasts
*  or YouTube or Twitter, consider mentioning ideas, people, topics you find interesting.
*  It helps guide the future of this podcast.
*  But in general, I just love comments with kindness and thoughtfulness in them.
*  This podcast is a side project for me, as many people know,
*  but I still put a lot of effort into it.
*  So the positive words of support from an amazing community, from you, really help.
*  I recently started doing ads.
*  At the end of the introduction, I'll do one or two minutes after introducing the
*  episode and never any ads in the middle that can break the flow of the conversation.
*  I hope that works for you and doesn't hurt the listening experience.
*  I provide timestamps for the start of the conversation that you can skip to,
*  but it helps if you listen to the ad and support this podcast by trying out the product or service
*  being advertised.
*  This show is presented by Cash App, the number one finance app in the App Store.
*  I personally use Cash App to send money to friends, but you can also use it to buy,
*  sell and deposit Bitcoin in just seconds.
*  Cash App also has a new investing feature.
*  You can buy fractions of a stock, say one dollar's worth, no matter what the stock price is.
*  Broker services are provided by Cash App Investing, Subsidiary of Square, and Member SIPC.
*  I'm excited to be working with Cash App to support one of my favorite organizations called First,
*  best known for their FIRST Robotics and LEGO competitions.
*  They educate and inspire hundreds of thousands of students in over 110 countries and have a
*  perfect rating and charity navigator, which means the donated money is used to maximum
*  effectiveness.
*  When you get Cash App from the App Store or Google Play and use code LEXPODGAST,
*  you'll get $10 and Cash App will also donate $10 to FIRST, which again is an organization
*  that I've personally seen inspire girls and boys to dream of engineering a better world.
*  And now, here's my conversation with Sebastian Thrun.
*  You mentioned that The Matrix may be your favorite movie.
*  So let's start with a crazy philosophical question.
*  Do you think we're living in a simulation?
*  And in general, do you find the thought experiment interesting?
*  Define simulation, I would say.
*  Maybe we are, maybe we are not, but it's completely irrelevant to the way we should act.
*  Right.
*  Putting aside for a moment the fact that it might not have any impact on how we should act
*  as human beings, for people studying theoretical physics, these kinds of questions might be kind
*  of interesting, looking at the universe's information processing system.
*  The universe is an information processing system.
*  It is.
*  It's a huge physical, biological, chemical computer.
*  There's no question.
*  But I live here and now.
*  I care about people.
*  I care about us.
*  What do you think it's trying to compute?
*  I don't think there's an intention.
*  I think it just the world evolves the way it evolves and it's beautiful.
*  It's unpredictable.
*  And I'm really, really grateful to be alive.
*  Spoken like a true human.
*  Which last time I checked I was.
*  Well, that in fact, this whole conversation is just a touring test to see if indeed you are.
*  You've also said that one of the first programs, or the first few programs you've written,
*  was a wait for a TI 57 calculator.
*  Yeah.
*  Maybe that's early eighties.
*  We don't want to date calculators or anything.
*  That's early eighties.
*  Correct.
*  Yeah.
*  So if you were to place yourself back into that time, into the mindset you were in,
*  could you have predicted the evolution of computing, AI, the internet technology in
*  the decades that followed?
*  I was super fascinated by Silicon Valley, which I'd seen on television once and thought,
*  my God, this is so cool.
*  They build like DRAMs there and CPUs.
*  How cool is that?
*  And as a college student, a few years later, I decided to re-study intelligence and study
*  human beings and found that even back then in the eighties and nineties,
*  that artificial intelligence is what fascinated me the most.
*  What's missing is that back in the day, the computers are really small.
*  They're like the brains you could build were not anywhere bigger than a cockroach.
*  And cockroaches aren't very smart.
*  So we weren't at the scale yet where we are today.
*  Did you dream at that time to achieve the kind of scale we have today?
*  Or did that seem possible?
*  I always wanted to make robots smart.
*  I felt it was super cool to build an artificial human.
*  And the best way to build an artificial human would be to build a robot,
*  because that's kind of the closest we could do.
*  Unfortunately, we aren't there yet.
*  The robots today are still very brittle.
*  But it's fascinating to study intelligence from a constructive perspective.
*  You can build something.
*  To understand, you build.
*  What do you think it takes to build an intelligent system and an intelligent robot?
*  I think the biggest innovation that we've seen is machine learning.
*  And it's the idea that their computers can basically teach themselves.
*  Let's give an example.
*  I'd say everybody pretty much knows how to walk.
*  And we learn how to walk in the first year or two of our lives.
*  But no scientist has ever been able to write on the rules of the human gate.
*  We don't understand it.
*  We can't put it in our brains.
*  Some of it we can practice it.
*  We understand it, but we can't articulate it.
*  We can't pass it on by language.
*  And that to me is kind of the deficiency of today's computer programming.
*  When you program a computer, they're so insanely dumb
*  that you have to give them rules for every contingencies.
*  Very unlike the way people learn, but learn from data and experience,
*  computers are being instructed.
*  And because it's so hard to get this instruction set right,
*  we pay software engineers $200,000 a year.
*  Now, the most recent innovation, which has been in the make for like 30, 40 years,
*  is an idea that computers can find their own rules.
*  So they can learn from falling down and getting up
*  the same way children can learn from falling down and getting up.
*  And that revolution has led to a capability that's completely unmatched.
*  Today's computers can watch experts do their jobs,
*  whether you're a doctor or a lawyer,
*  pick up the regularities, learn those rules,
*  and then become as good as the best experts.
*  So the dream of in the 80s of expert systems, for example,
*  had at its core the idea that humans could boil down their expertise on a sheet of paper.
*  So to sort of reduce, sort of be able to explain to machines
*  how to do something explicitly.
*  So do you think, what's the use of human expertise into this whole picture?
*  Do you think most of the intelligence will come from machines learning from experience
*  without human expertise input?
*  So the question for me is much more how do you express expertise?
*  You can express expertise by writing a book,
*  you can express expertise by showing someone what you're doing,
*  you can express expertise by applying it by many different ways.
*  And I think the expert systems was our best attempt in AI to capture expertise and rules.
*  There's someone sat down and say, here are the rules of human gait.
*  Here's when you put your big toe forward and your heel backwards,
*  and here how you stop stumbling.
*  And as we now know, the set of rules, the set of language that we can command
*  is incredibly limited.
*  The majority of the human brain doesn't deal with language.
*  It deals with subconscious, numerical, perceptual things that we don't even self-aware of.
*  Now, when an AI system watches an expert do their job and practice their job,
*  it can pick up things that people can't even put into writing, into books or rules.
*  And that's where the real power is.
*  We now have AI systems that, for example,
*  look over the shoulders of highly paid human doctors like dermatologists or radiologists,
*  and they can somehow pick up those skills that no one can express in words.
*  So you were a key person in launching three revolutions,
*  online education, autonomous vehicles, and flying cars or VTOLs.
*  So high level.
*  And I apologize for all the philosophical questions.
*  That's no apology necessary.
*  How do you choose what problems to try and solve?
*  What drives you to make those solutions a reality?
*  I have two desires in life.
*  I want to literally make the lives of others better.
*  Or as we often say, maybe jokingly, make the world a better place.
*  I actually believe in this.
*  It's as funny as it sounds.
*  And second, I want to learn.
*  I want to get into skills.
*  I don't want to be in a job I'm good at,
*  because if I'm in a job that I'm good at,
*  the chance for me to learn something interesting is actually minimized.
*  So I want to be in a job I'm bad at.
*  That's really important to me.
*  So in a bit, for example, what people often call flying cars,
*  these are electrical, vertical takeoff and landing vehicles.
*  I'm just no expert in any of this.
*  And it's so much fun to learn on the job
*  what it actually means to build something like this.
*  Now, I'd say the stuff that I've done lately
*  after I finished my professorship at Stanford,
*  they really focused on what has the maximum impact on society.
*  Like transportation is something that has transformed the 21st or 20th century
*  more than any other invention, in my opinion, even more than communication.
*  And cities are different, workers are different,
*  women's rights are different because they're all different.
*  Women's rights are different because of transportation.
*  And yet we still have a very suboptimal transportation solution
*  where we kill 1.2 or so million people every year in traffic.
*  It's like the leading cause of death for young people in many countries.
*  Where we are extremely inefficient resource wise,
*  just go to your average neighborhood city
*  and look at the number of parked cars.
*  That's a travesty, in my opinion.
*  Or where we spend endless hours in traffic jams.
*  And very, very simple innovations like a self-driving car
*  or what people call a flying car could completely change this.
*  And it's there.
*  I mean, the technology is basically there.
*  You have to close your eyes not to see it.
*  So lingering on autonomous vehicles, a fascinating space,
*  some incredible work you've done throughout your career there.
*  So let's start with DARPA, I think.
*  The DARPA challenge, through the desert and then urban to the streets.
*  I think that inspired an entire generation of roboticists
*  and obviously sprung this whole excitement
*  about this particular kind of four-wheeled robots
*  we called autonomous cars, self-driving cars.
*  So you led the development of Stanley, the autonomous car that won
*  the race to the desert, the DARPA challenge in 2005.
*  And Junior, the car that finished second in the DARPA urban challenge,
*  also did incredibly well in 2007, I think.
*  What are some painful, inspiring or enlightening experiences
*  from that time that stand out to you?
*  Oh my God.
*  Painful were all these incredibly complicated, stupid bugs that had to be found.
*  We had a phase where Stanley, our car that eventually won the DARPA
*  urban challenge, would every 30 miles just commit suicide.
*  And we didn't know why.
*  And it ended up to be that in the syncing of two computer clocks,
*  occasionally a clock went backwards and that negative time elapsed,
*  screwed up the entire internal logic, but it took ages to find this.
*  It was like bugs like that.
*  I'd say enlightening is the Stanford team immediately focused on machine learning
*  and on software, whereas everybody else seemed to focus on building better hardware.
*  Our analysis had been a human being with an existing rental car
*  can perfectly drive the course.
*  Why do I have to build a better rental car?
*  I just should replace the human being.
*  And the human being to me was a conjunction of three steps.
*  We had sensors, eyes and ears, mostly eyes.
*  We had brains in the middle and then we had actuators, our hands and our feet.
*  Now the actuators are easy to build.
*  The sensors are actually also easy to build.
*  What was missing was the brain, so we had to build a human brain.
*  And nothing clear to me that the human brain is a learning machine,
*  so why not just train our robots?
*  So we would build a massive machine learning into our machine.
*  And with that, we were able to not just learn from human drivers.
*  We had the entire speed control of the vehicle was copied from human driving,
*  but also have the robot learn from experience where it made a mistake
*  and could recover from it and learn from it.
*  You mentioned the pain point of software and clocks.
*  Synchronization seems to be a problem that continues with robotics.
*  It's a tricky one with drones and so on.
*  What does it take to build a thing, a system with so many constraints?
*  You have a deadline, no time.
*  You're unsure about anything really.
*  It's the first time that people really even explore.
*  It's not even sure that anybody can finish when we're talking about the
*  race to the desert the year before nobody finished.
*  What does it take to scramble and finish a product that actually,
*  a system that actually works?
*  We're lucky.
*  We're a really small team.
*  The core of the team were four people.
*  It was four because five couldn't comfortably sit inside a car,
*  but four could.
*  And I, as a team leader, my job was to get pizza for everybody
*  and wash the car and stuff like this and repair the radiator when it broke
*  and debug the system.
*  And we were very kind of open-minded.
*  We had no ego involved.
*  We just wanted to see how far we can get.
*  What we did really, really well was time management.
*  We were done with everything a month before the race.
*  And we froze the entire software a month before the race.
*  And it turned out, looking at other teams, every other team complained
*  if they had just one more week, they would have won.
*  And we decided we're not going to fall into that mistake.
*  We're going to be early.
*  And we had an entire month to shake the system.
*  And we actually found two or three minor bugs in the last month that we
*  had to fix.
*  And we were completely prepared when the race occurred.
*  LW Okay.
*  So first of all, that's such an incredibly rare achievement in terms of
*  being able to be done on time or ahead of time.
*  What do you, how do you do that in your future work?
*  What advice do you have in general?
*  Because it seems to be so rare, especially in highly innovative projects
*  like this, people work to the last second.
*  MW Well, the nice thing about the Dapagran challenge is that the problem
*  was incredibly well-defined.
*  We were able for a while to drive the old Dapagran challenge course, which
*  had been used the year before.
*  And then at some reason we were kicked out of the region.
*  So we had to go to a different desert, the Snorren desert, and we were able
*  to drive desert trails just of the same type.
*  So there was never any debate about like, what's actually the problem.
*  We didn't sit down and say, hey, should we build a car or a plane?
*  We had to build a car.
*  That made it very, very easy.
*  Then I studied my own life and life of others and realized
*  that the typical mistake that people make is that there is this kind of crazy bug
*  left that they haven't found yet.
*  And it's just, they regret it and the bug would have been trivial to fix.
*  They just haven't fixed it yet.
*  They didn't want to fall into that trap.
*  So I built a testing team.
*  We had a testing team that built a testing booklet of 160 pages of tests we
*  had to go through just to make sure we shake out the system appropriately.
*  JS Wow.
*  MW And the testing team was with us all the time and dictated to us today.
*  We do railroad crossings tomorrow.
*  We do, we practice the start of the event and in all of these, we thought, oh my God,
*  it's long solved trivial.
*  And then we tested it out.
*  Oh my God, it doesn't do a railroad crossing.
*  Why not?
*  Oh my God, it mistakes the rails for metal barriers.
*  JS Yeah.
*  MW We have to fix this.
*  JS Yes.
*  MW So it was really a continuous focus on improving the weakest part of the system.
*  And as long as you focus on improving the weakest part of the system, you eventually
*  build a really great system.
*  JS Let me just pause in that.
*  To me as an engineer, it's just super exciting that you were thinking like that,
*  especially at that stage as brilliant that testing was such a core part of it.
*  It may be to linger on the point of leadership.
*  I think it's one of the first times you were really a leader and you've led many
*  very successful teams since then.
*  What does it take to be a good leader?
*  I would say most of us just take credit for the work of others.
*  That's very convenient turns out, because I can't do all these things myself.
*  I'm an engineer at heart, so I care about engineering.
*  So I don't know what the chicken and the egg is, but as a kid, I loved computers
*  because you could tell them to do something and they actually did it.
*  It was very cool.
*  And you could like in the middle of the night, wake up at one in the morning and
*  switch on your computer.
*  What you told you to do yesterday, it would still do.
*  That was really cool.
*  Unfortunately, that didn't quite work with people.
*  You go to people and tell them what to do and they don't do it.
*  They hate you for it.
*  Or you do it today and then they go a day later and they stop doing it.
*  Then the question really became how can you put yourself in the brain of people
*  as opposed to computers?
*  And in terms of computers, they're super dumb.
*  They're so dumb.
*  If people were as dumb as computers, I wouldn't want to work with them.
*  But people are smart and people are emotional and people have pride and
*  people have aspirations.
*  So how can I connect to that?
*  And that's the thing that most of leadership just fails because
*  many, many engineers turn manager believe they can treat their team just the same way
*  it can treat a computer and it just doesn't work this way.
*  It's just really bad.
*  So how can I connect to people?
*  It turns out as a college professor, the wonderful thing you do all the time is to
*  empower other people.
*  Like your job is to make your students look great.
*  That's all you do.
*  You're the best coach.
*  And it turns out if you do a fantastic job with making your students look great,
*  they actually love you and their parents love you and they give you all the credit
*  for stuff you don't deserve.
*  It turns out all my students were smarter than me.
*  All the great stuff invented at Stanford was the stuff, not my stuff.
*  And they give me credit and say, oh, Sebastian, but just making them feel good about themselves.
*  So the question really is, can you take a team of people and what does it take to make them
*  to connect to what they actually want in life and turn this into productive action?
*  It turns out every human being that I know has incredibly good intentions.
*  I've really never really met a person with bad intentions.
*  I believe every person wants to contribute.
*  I think every person I've met wants to help others.
*  It's amazing how much of a urge we have not to just help ourselves, but to help others.
*  So how can we empower people and give them the right framework that they can accomplish this?
*  If in moments when it works, it's magical because you'd see the confluence of people
*  being able to make the world a better place and to have enormous confidence and pride out of this.
*  And that's when my environment works the best.
*  These are moments where I can disappear for a month and come back and things still work.
*  It's very hard to accomplish, but when it works, it's amazing.
*  So I agree with you very much.
*  It's not often heard that most people in the world have good intentions.
*  At the core, their intentions are good and they're good people.
*  That's a beautiful message that's not often heard.
*  We make this mistake, and this is a friend of mine, Alex Voda,
*  talking about this, that we judge ourselves by our intentions and others by their actions.
*  And I think the biggest skill, I mean here in Silicon Valley, we're full of engineers
*  who have very little empathy and are kind of befuddled by why it doesn't work for them.
*  The biggest skill I think that people should acquire is to put themselves into the position
*  of the other and listen and listen to what the other has to say.
*  And they'd be shocked how similar they are to themselves.
*  And they might even be shocked how their own actions don't reflect their intentions.
*  I often have conversations with engineers where I say, look, hey, I love you.
*  You're doing a great job.
*  And by the way, what you just did has the following effect.
*  Are you aware of that?
*  And then people would say, oh my God, no, I wasn't because my intention was that.
*  And I say, yeah, I trust your intention.
*  You're a good human being.
*  But just to help you in the future, if you keep expressing it that way,
*  then people will just hate you.
*  And I've had many instances where you would say, oh my God, thank you for telling me this
*  because it wasn't my intention to look like an idiot.
*  It wasn't my intention to help other people.
*  I just didn't know how to do it.
*  Very simple, by the way.
*  There's a book, Dale Carnegie, 1936, How to Make Friends and How to Influence Others,
*  has the entire Bible.
*  You just read it and you're done and you apply it every day.
*  And I wish I was good enough to apply it every day.
*  But it says simple things, right?
*  Like, be positive, remember people's names, smile, and eventually have empathy.
*  Like, really think that the person that you hate and you think is an idiot
*  is actually just like yourself.
*  It's a person who's struggling, who means well, and who might need help.
*  And guess what?
*  You need help.
*  I've recently spoken with Stephen Schwartzman.
*  I'm not sure if you know who that is.
*  I do.
*  So he said...
*  It's on my list.
*  On the list.
*  But he said, sort of to expand on what you're saying,
*  that one of the biggest things you can do is
*  hear people when they tell you what their problem is and then help them with that problem.
*  He says it's surprising how few people actually listen to what troubles others.
*  And because it's right there in front of you and you can benefit the world the most.
*  And in fact, yourself and everybody around you by just hearing the problems and solving them.
*  That's my little history of engineering.
*  While I was engineering with computers, I didn't care at all what the computer's problems were.
*  I just told them what to do and to do it.
*  And it just doesn't work this way with people.
*  It doesn't work with me.
*  If you come to me and say, do A, I do the opposite.
*  But let's return to the comfortable world of engineering.
*  Can you tell me in broad strokes how you see it?
*  Because you're at the core of starting it, the core of driving it,
*  the technical evolution of autonomous vehicles from the first DARPA Grand Challenge
*  to the incredible success we see with the program.
*  You started with Google self-driving car and Waymo and the entire industry that sprung up
*  of different kinds of approaches, debates and so on.
*  The idea of self-driving car goes back to the 80s.
*  There was a team in Germany and another team in Carnegie Mellon
*  that did some very pioneering work.
*  But back in the day, I'd say the computers were so efficient
*  that even the best professors and engineers in the world basically stood no chance.
*  It then folded into a phase where the US government spent
*  at least half a billion dollars that I could count on research projects.
*  But the way the procurement works, a successful stack of paper describing
*  lots of stuff that no one's ever going to read was a successful
*  product of a research project.
*  So we trained our researchers to produce lots of paper.
*  That all changed with the DARPA Grand Challenge.
*  I really got to credit the ingenious people at DARPA and the US government in Congress
*  that took a complete new funding model where they said,
*  let's not fund effort, let's fund outcomes.
*  And it sounds very trivial, but there was no tax code that allowed
*  the use of congressional tax money for a price.
*  It was all effort-based.
*  So if you put in 100 hours in, you could charge 100 hours.
*  If you put in 1,000 hours in, you could build 1,000 hours.
*  By changing the focus and so you're making the price,
*  we don't pay you for development, we pay you for the accomplishment.
*  They drew in, they automatically drew out all these contractors who are used to
*  the drug of getting money per hour.
*  And they drew in a whole bunch of new people.
*  And these people are mostly crazy people.
*  They were people who had a car and a computer
*  and they wanted to make a million bucks.
*  The million bucks was the official price money was then doubled.
*  And they felt if I put my computer in my car and program it, I can be rich.
*  And that was so awesome.
*  Like half the teams, there was a team that was surfer dudes
*  and they had like two surfboards on their vehicle
*  and brought like these fashion girls, super cute girls, like twin sisters.
*  And you could tell these guys were not your common,
*  felt very banded to like gets all these big multi-million
*  and billion dollar contracts from the US government.
*  And there was a great reset.
*  Universities moved in.
*  I was very fortunate at Stanford that I just received tenure
*  so I couldn't get fired when I wanted to do.
*  Otherwise I wouldn't have done it.
*  And I had enough money to finance this thing.
*  And I was able to attract a lot of money from third parties.
*  And even car companies moved in.
*  They kind of moved in very quietly because they were super scared to be embarrassed
*  that their car would flip over.
*  But Ford was there and Volkswagen was there and a few others and GM was there.
*  So it kind of reset the entire landscape of people.
*  And if you look at who's a big name in self-driving cars today,
*  these were mostly people who participated in those challenges.
*  Okay, that's incredible.
*  Can you just comment quickly on your sense of lessons learned
*  from that kind of funding model and the research that's going on in academia
*  in terms of producing papers?
*  Is there something to be learned and scaled up bigger,
*  at least having these kinds of grand challenges that could improve outcomes?
*  So I'm a big believer in focusing on kind of an end-to-end system.
*  I'm a really big believer in systems building.
*  I've always built systems in my academic career,
*  even though I do a lot of math and abstract stuff.
*  But it's all derived from the idea of let's solve a real problem.
*  And it's very hard for me to be an academic and say,
*  let me solve a component of a problem.
*  Like if someone feels like non-monetary logic or AI planning systems,
*  where people believe that a certain style of problem solving
*  is the ultimate end objective.
*  And I would always turn it around and say,
*  what problem would my grandmother care about
*  that doesn't understand computer technology
*  and doesn't want to understand?
*  Now, how can I make her love what I do?
*  Because only then do I have an impact on the world.
*  I can easily impress my colleagues.
*  That is much easier.
*  But impressing my grandmother is very, very hard.
*  So I would always thought if I can build a self-driving car
*  and my grandmother can use it even after she loses her driving privileges
*  or children can use it or we save maybe a million lives a year,
*  that would be very impressive.
*  And there's so many problems like these.
*  Like there's a problem with curing cancer or whatever.
*  Live twice as long.
*  Once a problem is defined, of course, I can't solve it in its entirety.
*  It takes sometimes tens of thousands of people to find a solution.
*  There's no way you can fund an army of 10,000 at Stanford.
*  So you've got to build a prototype.
*  Let's build a meaningful prototype.
*  And the DARPA Grand Challenge was beautiful
*  because it told me what this prototype had to do.
*  I didn't have to think about what it had to do.
*  I just had to read the rules and it was really beautiful.
*  And it's most beautiful, you think, what academia could aspire to
*  is to build a prototype that's the systems level that solves,
*  gives you an inkling that this problem could be solved with this prototype.
*  First of all, I want to emphasize what academia really is.
*  And I think people misunderstand it.
*  First and foremost, academia is a way to educate young people.
*  First and foremost, a professor is an educator,
*  no matter where you are at, a small suburban college
*  or whether you are a Harvard or Stanford professor.
*  That's not the way most people think of themselves in academia
*  because we have this kind of competition going on for citations and publication.
*  That's a measurable thing, but that is secondary
*  to the primary purpose of educating people to think.
*  Now, in terms of research, most of the great science,
*  the great research comes out of universities.
*  You can trace almost everything back, including Google, to universities.
*  So there's nothing really fundamentally broken here.
*  It's a good system.
*  I think America has the finest university system on the planet.
*  We can talk about reach and how to reach people outside the system.
*  It's a different topic, but the system itself is a good system.
*  If I had one wish, I would say it'd be really great
*  if there was more debate about what the great big problems are in society
*  and focus on those.
*  And most of them are interdisciplinary.
*  Unfortunately, it's very easy to fall into an interdisciplinary viewpoint
*  where your problem is dictated by what your closest colleagues believe the problem is.
*  It's very hard to break out and say, well, there's an entire new field of problems.
*  So to give an example, prior to me working on self-driving cars,
*  I was a roboticist and a machine learning expert, and I wrote books on robotics,
*  something called probabilistic robotics.
*  It's a very methods-driven viewpoint of the world.
*  I built robots that acted in museums as tour guides that led children around.
*  It's something that at the time was moderately challenging.
*  When I started working on cars, several colleagues told me,
*  Sebastian, you're destroying your career because in our field of robotics,
*  cars are looked like as a gimmick.
*  They're not expressive enough.
*  They can only push this bottle and the brakes.
*  There's no dexterity.
*  There's no complexity.
*  It's just too simple.
*  And no one came to me and said, wow, if you solve that problem,
*  you can save a million lives.
*  Right?
*  Among all robotic problems that I've seen in my life,
*  I would say the self-driving car, transportation, is the one has the most hope for society.
*  So how come the robotics community wasn't all over the place?
*  And it was because we focused on methods, on solutions, and not on problems.
*  Like, if you go around today and ask your grandmother,
*  what bugs you?
*  What really makes you upset?
*  I challenge any academic to do this and then realize how far your research is
*  probably away from that today.
*  At the very least, that's a good thing for academics to deliberate on.
*  The other thing that's really nice in Silicon Valley is
*  Silicon Valley is full of smart people outside academia.
*  Right?
*  So there's the Larry Pages and Mark Zuckerbergs in the world who are
*  anywhere smarter, smarter than the best academics I've met in my life.
*  And what they do is they are at a different level.
*  They build the systems.
*  They build the customer-facing systems.
*  They build things that people can use without technical education.
*  And they are inspired by research.
*  They're inspired by scientists.
*  They hire the best PhDs from the best universities for a reason.
*  So I think this kind of vertical integration that between the real product,
*  the real impact, and the real thought, the real ideas,
*  that's actually working surprisingly well in Silicon Valley.
*  It did not work as well in other places in this nation.
*  So when I worked at Carnegie Mellon, we had the world's finest computer science university.
*  But there wasn't those people in Pittsburgh that would be able to take these
*  very fine computer science ideas and turn them into massively impactful products.
*  That symbiosis seemed to exist pretty much only in Silicon Valley and maybe a bit in Boston and
*  Austin.
*  Yeah.
*  With Stanford, that's really interesting.
*  So if we look a little bit further on from the DARPA Grand Challenge and the launch of the
*  Google self-driving car, what do you see as the state, the challenges of autonomous vehicles
*  as they are now?
*  Is actually achieving that huge scale and having a huge impact on society?
*  I'm extremely proud of what has been accomplished.
*  Again, I'm taking a lot of credit for the work that I've done.
*  I'm actually very optimistic.
*  People have been worrying, is it too fast?
*  Is it too slow?
*  Why is it not there yet?
*  And so on.
*  It is actually quite an interesting hard problem in that a self-driving car,
*  to build one that manages 90% of the problems and count on everyday driving is easy.
*  We can literally do this over a weekend.
*  To do 99% might take a month.
*  Then there's 1% left.
*  1% would mean that you still have a fatal accident every week.
*  Very unacceptable.
*  So now you work on this 1% and the 99% of the remaining 1% is actually still relatively easy.
*  But now you're down to like a hundredth of 1% and it's still completely unacceptable in terms of
*  safety.
*  So the variety of things you encounter are just enormous and that gives me enormous respect for
*  human beings that we're able to deal with the couch on the highway, or the deer in the
*  headlight, or the blown tire that we'd never been trained for and all of a sudden have to handle it
*  in an emergency situation and often do very, very successfully.
*  It's amazing from that perspective how safe driving actually is given how many millions of
*  miles we drive every year in this country.
*  We are now at a point where I believe the technology is there and I've seen it.
*  I've seen it in Waymo, I've seen it in Aptiv, I've seen it in Cruise,
*  and a number of companies and Voyage where vehicles are now driving around and basically
*  flawlessly are able to drive people around in limited scenarios.
*  In fact, you can go to Vegas today and order a summon a Lyft and if you get the right setting
*  of your app, you'll be picked up by a driverless car.
*  Now there's still safety drivers in there, but that's a fantastic way to kind of learn what the
*  limits of technology today.
*  And there's still some glitches, but the glitches have become very, very rare.
*  I think the next step is going to be to down cost it, to harden it.
*  Entrapment, the sensors are not quite an automotive great standard yet.
*  And then to really build the business models, to really kind of go somewhere and make the
*  business case.
*  And the business case is hard work.
*  It's not just, oh my God, we have this capability, people are just going to buy it.
*  You have to make it affordable.
*  You have to give people the, find the social acceptance of people.
*  None of the teams yet has been able to, or gutsy enough to drive around without a person
*  inside the car.
*  And that's the next magical hurdle.
*  We'll be able to send these vehicles around completely empty in traffic.
*  And I think, I mean, I wait every day, wait for the news that Waymo has just done this.
*  So, you know, it's interesting you mentioned gutsy.
*  Let me, let me ask some, maybe unanswerable question, maybe edgy questions.
*  But in terms of how much risk is required, some guts in terms of leadership style, it
*  would be good to contrast approaches.
*  And I don't think anyone knows what's right.
*  But if we compare Tesla and Waymo, for example, Elon Musk and the Waymo team,
*  there's slight differences in approach.
*  So on the Elon side, there's more, I don't know what the right word to use,
*  but aggression in terms of innovation.
*  And on Waymo side, there's more sort of cautious, safety focused approach to the problem.
*  What do you think it takes?
*  What leadership at which moment is right?
*  Which approach is right?
*  Look, I don't sit in either of those teams.
*  So I'm unable to even verify, like somebody says, correct.
*  In the end of the day, every innovator in that space will face a fundamental dilemma.
*  And I would say you could put aerospace titans into the same bucket,
*  which is you have to balance public safety with your drive to innovate.
*  And this country, in particular in the States, has a hundred plus year history
*  of doing this very successfully.
*  Air travel is what a hundred times as safe per mile than ground travel, than cars.
*  And there's a reason for it, because people have found ways to be very methodological
*  about ensuring public safety while still being able to make progress on important aspects,
*  for example, like yell and noise and fuel consumption.
*  So I think that those practices are proven and they actually work.
*  We live in a world safer than ever before.
*  And yes, there will always be the provision that something goes wrong.
*  There's always the possibility that someone makes a mistake or there's an unexpected failure.
*  We can never guarantee to a hundred percent absolute safety other than just not doing it.
*  But I think I'm very proud of the history of the United States.
*  I mean, we've dealt with much more dangerous technology like nuclear energy and kept that safe too.
*  We have nuclear weapons and we keep those safe.
*  So we have methods and procedures that really balance these two things very, very successfully.
*  You've mentioned a lot of great autonomous vehicle companies
*  that are taking sort of the level four, level five, they jump in full autonomy
*  with a safety driver and take that kind of approach and also through simulation and so on.
*  There's also the approach that Tesla Autopilot is doing, which is kind of incrementally taking
*  a level two vehicle and using machine learning and learning from the driving of human beings
*  and trying to creep up, trying to incrementally improve the system until it's able to achieve
*  level four autonomy. So perfect autonomy in certain kind of geographical regions.
*  What are your thoughts on these contrasting approaches?
*  Well, first of all, I'm a very proud Tesla owner and I literally use the Autopilot every day and
*  it literally has kept me safe. It's a beautiful technology specifically for highway driving when
*  I'm slightly tired because then it turns me into a much safer driver and I'm 100% confident that's
*  the case. In terms of the right approach, I think the biggest change I've seen since I've been in
*  the Waymo team is this thing called deep learning. Deep learning was not a hot topic when I started
*  Waymo or Google self-driving cars. It was there. In fact, we started Google Brain at the same time
*  in Google X, so I invested in deep learning, but people didn't talk about it. It wasn't a hot topic.
*  And now it is. There's a shift of emphasis from a more geometric perspective where you use geometric
*  sensors that give you a full 3D view and you do geometric reasoning about, oh, this box over here
*  might be a car, towards a more human-like, oh, let's just learn about it. This looks like the
*  thing I've seen 10,000 times before, so maybe it's the same thing. Machine learning perspective.
*  And that has really put, I think, all these approaches on steroids. At Udacity, we teach a
*  course in self-driving cars. In fact, I think we've graduated over 20,000 or so people on
*  self-driving car skills, so every self-driving car team in the world now uses our engineers.
*  And in this course, the very first homework assignment is to do lane finding on images.
*  And lane finding images, for laymen, what this means is you put a camera into your car or you
*  open your eyes and you would know where the lane is, right? So you can stay inside the lane with
*  your car. Humans can do this super easily. You just look and you know where the lane is, just
*  intuitively. For machines, for a long time, it was super hard because people would write these kind
*  of crazy rules. If there's like, wine lane markers and here's what white really means, this is not
*  quite white enough, so it's not white. Or maybe the sun is shining, so when the sun shines and this is
*  white and this is a straight line, or maybe it's not quite a straight line because the road is curved.
*  And do we know that there's a six feet between lane markings or not or 12 feet, whatever it is?
*  And now what the students are doing, they would take machine learning. So instead of like writing
*  these crazy rules for the lane marker is to say, hey, let's take an hour of driving and label it
*  and tell the vehicle this is actually the lane by hand. And then these are examples and have the
*  machine find its own rules, what lane markings are. And within 24 hours, now every student that's
*  never done any programming before in this space can write a perfect lane finder as good as the
*  best commercial lane finders. And that's completely amazing to me. We've seen progress using machine
*  learning that completely dwarfs anything that I saw 10 years ago. Yeah. And just as a side note,
*  the self-driving car nano degree, the fact that you launched that many years ago now, maybe four
*  years ago, three years ago is incredible. That's a great example of system level thinking. So just
*  taking an entire course that teaches how to solve the entire problem. I definitely recommend people.
*  It's been super popular and it's become actually incredibly high quality with Mercedes and various
*  other companies in that space. And we find that engineers from Tesla and Waymo are taking it today.
*  The insight was that two things, one is existing universities will be very slow to move
*  because they're departmentalized and there's no department for self-driving cars. So between
*  MECI and EE and computer science, getting those folks together into one room is really, really hard.
*  And every professor listening here will know, will probably agree to that. And secondly, even if all
*  the great universities did this, which none so far has developed a curriculum in this field,
*  it is just a few thousand students that can partake because all the great universities are
*  super selective. So how about people in India? How about people in China or in the Middle East
*  or Indonesia or Africa? Why should those be excluded from the skill of building self-driving
*  cars? Are they any dumber than we are? Are they any less privileged? And the answer is,
*  we should just give everybody the skill to build a self-driving car because if we do this,
*  then we have like a thousand self-driving car startups. And if 10% succeed, that's like a hundred,
*  that means a hundred countries now will have self-driving cars and be safer.
*  It's kind of interesting to imagine, impossible to quantify, but the number, the, you know,
*  over a period of several decades, the impact that has like a single course, like a ripple effect to
*  society. I just recently talked to Andrew and who was creator of Cosmos, so it's interesting to think
*  about how many scientists that show launched. And so it's really, in terms of impact, I can't
*  imagine a better course than the self-driving car course. That's, you know, there's other more
*  specific disciplines like deep learning and so on that Udacity is also teaching, but self-driving
*  cars, it's really, really interesting courses. Yeah, and it came at the right moment. It came
*  at a time when there were a bunch of acqui-hires. Acqui-hire is an acquisition of a company, not for
*  its technology or its products or business, but for its people. So acqui-hire means maybe
*  that a company of 70 people, they have no product yet, but they're super smart people,
*  and they pay a certain amount of money. So I took acqui-hires like GM Cruise and Uber and others and
*  did the math and said, hey, how many people are there and how much money was paid? And
*  as a lower bound, I estimated the value of a self-driving car engineer in these acquisitions
*  to be at least $10 million. Right? So think about this. You get yourself a skill and you team up
*  and build a company and your worth now is $10 million. I mean, that's kind of cool. I mean,
*  but what other thing could you do in life to be worth $10 million within a year?
*  Yeah, amazing. But to come back for a moment on to deep learning and its application in
*  autonomous vehicles, you know, what are your thoughts on Elon Musk's statement,
*  provocative statement perhaps that light air is a crutch. So this geometric way of thinking about
*  the world may be holding us back if what we should instead be doing in this robotic space,
*  in this particular space of autonomous vehicles is using camera as a primary sensor and using
*  computer vision and machine learning as the primary way to... Look, I have two comments.
*  I think first of all, we all know that people can drive cars without lighters in their heads
*  because we only have eyes and we mostly just use eyes for driving. Maybe we use some other
*  perception of our bodies, accelerations, occasionally our ears, certainly not our noses.
*  So that the existence proof is there that eyes must be sufficient. In fact, we could even
*  drive a car if someone put a camera out and then gave us the camera image with
*  no latency, you'll be able to drive a car that way the same way. So a camera is also sufficient.
*  Secondly, I really love the idea that in the Western world, we have many, many different
*  people trying different hypotheses. It's almost like an ant hill, like if an ant hill tries to
*  forge for food, but you can sit there as two ants and agree what the perfect path is. And then every
*  single ant marches for the most likely location of food is, or you can even just spread out.
*  And I promise you the spread out solution will be better because if the discussing philosophical
*  intellectual ants get it wrong and they're all moving in the wrong direction, they're going to
*  waste the day. And then they're going to discuss again for another week. Whereas if all these ants
*  go in a random direction, someone's going to succeed and they're going to come back and claim
*  victory and get the Nobel Prize or whatever the ant equivalent is. And then they all march in the
*  same direction. And that's great about society. That's great about the Western society. We're
*  not plan based. We're not central based. We don't have a Soviet Union style central government that
*  tells us where to forge. We just forge. We started in C Corp. We get investor money, go out and try
*  it out. And who knows who's going to win. I like it. When you look at the long term vision
*  of autonomous vehicles, do you see machine learning as fundamentally being able to solve most of the
*  problems? So learning from experience. I'd say we should be very clear about what machine learning
*  is and is not. And I think there's a lot of confusion. What it is today is a technology
*  that can go through large databases of repetitive patterns and find those patterns.
*  So an example, we did a study at Stanford two years ago where we applied machine learning to
*  detecting skin cancer in images. And we harvested or built a dataset of 129,000 skin
*  photo shots that all had been biopsied for what the actual situation was. And those included
*  melanomas and carcinomas, also included rashes and other skin conditions, lesions.
*  And then we had a network find those patterns. And it was by and large able to then detect skin
*  cancer with an iPhone as accurately as the best board certified Stanford level dermatologist.
*  We proved that. Now, this thing was great in this one thing, in finding skin cancer,
*  but it couldn't drive a car. So the difference to human intelligence is we do all these many,
*  many things. And we can often learn from a very small dataset of experiences,
*  whereas machines still need very large datasets and things that will be very repetitive.
*  Now, that's still super impactful because almost everything we do is repetitive. So
*  that's going to transform human labor. But it's not this almighty general intelligence. We're
*  really far away from a system that will exhibit general intelligence. To that end, I actually
*  commiserate the naming a little bit because artificial intelligence, if you believe Hollywood,
*  is immediately mixed into the idea of human suppression and machine superiority. I don't
*  think that we're going to see this in my lifetime. I don't think human suppression is a good idea.
*  I don't see it coming. I don't see the technology being there. What I see instead is a very pointed,
*  focused pattern recognition technology that's able to extract patterns from large datasets.
*  And in doing so, it can be super impactful. Super impactful. Let's take the impact of artificial
*  intelligence on human work. We all know that it takes something like 10,000 hours to become an
*  expert. If you're going to be a doctor or a lawyer or even a really good driver, it takes a certain
*  amount of time to become experts. Machines now are able and have been shown to observe people,
*  become experts, and observe experts, and then extract those rules from experts in some interesting
*  way. They could go from law to sales to driving cars to diagnosing cancer, and then giving that
*  capability to people who are completely new in their job. That's been done. It's been done
*  commercially in many, many instantiations. That means we can use machine learning to make people
*  experts on the very first day of their work. Think about the impact. If your doctor is still
*  in their first 10,000 hours, you have a doctor who's not quite an expert yet. Who would not want a
*  doctor who is the world's best expert? And now we can leverage machines to really eradicate
*  error in decision-making, error in lack of expertise for human doctors. That could save your life.
*  If I can link on that for a little bit, in which way do you hope machines in the medical field
*  could help assist doctors? You mentioned this sort of accelerating the learning curve, or people,
*  if they start a job, or in the first 10,000 hours, can be assisted by machines. How do you
*  envision that assistance looking? We built this app for an iPhone that can detect and classify and
*  diagnose skin cancer. We proved two years ago that it does pretty much as good or better than
*  the best human doctors. Let me tell you a story. There's a friend of mine, let's call him Ben.
*  Ben is a very famous venture capitalist. He goes to his doctor and the doctor looks at a mole and
*  says, hey, that mole is probably harmless. For some very funny reason, he pulls out that phone
*  with our app. He's a collaborator in our study. The app says, no, no, no, this is a melanoma.
*  For background, melanomas are, and skin cancer is the most common cancer in this country.
*  Melanomas can go from stage zero to stage four within less than a year. Stage zero means you can
*  basically cut it out yourself with a kitchen knife and be safe. Stage four means your chances of
*  five more years and less than 20%. It's a very serious, serious, serious condition.
*  This doctor who took out the iPhone looked at the iPhone and was a little bit puzzled and said,
*  you know what, just to be safe, let's cut it out and biopsy it. That's the technical term for let's
*  get an in-depth diagnostics that is more than just looking at it. It came back as cancerous,
*  as a melanoma, and it was then removed. My friend Ben, I was hiking with him and we were talking
*  about AI and I told him I do this work on skin cancer. He said, oh, funny, my doctor just had an
*  iPhone that found my cancer. Wow. I was completely intrigued. I didn't even know about this.
*  This is a real human life. Who doesn't know somebody who has been affected by cancer?
*  Cancer is cause of death number two. Cancer is this kind of disease that is mean in the following
*  way. Most cancers can actually be cured relatively easily if we catch them early. The reason why we
*  don't tend to catch them early is because they have no symptoms. Your very first symptom of a
*  gallbladder cancer or a pancreatic cancer might be a headache. When you finally go to your doctor
*  because of these headaches or your back pain and you're being imaged, it's usually stage four plus
*  and that's the time when the occurring chances might be dropped to a single percentage.
*  If you could leverage AI to inspect your body on a regular basis without even a doctor in the room,
*  maybe when you take a shower or what have you, I know this sounds creepy, but
*  then we might be able to save millions and millions of lives.
*  You've mentioned there's a concern that people have about near-term impacts of AI in terms of job
*  loss. You've mentioned being able to assist doctors, being able to assist people in their jobs.
*  Do you have a worry of people losing their jobs or the economy being affected by the improvements in AI?
*  Yeah, anybody concerned about job losses, please come to GDASity.com. We teach contemporary tech
*  skills and we have a kind of implicit job promise. When we measure, we spend way over 50% of our
*  graduates in new jobs and they're very satisfied about it and it costs almost nothing. It costs like
*  a thousand five hundred max or something like that. I saw there's a cool new program that you
*  agreed with the US government guaranteeing that you will help give scholarships that educate people
*  in this kind of situation. Yeah, we're working with the US government on the idea of basically
*  rebuilding the American dream. GDASity has just dedicated 100,000 scholarships for citizens of
*  America for various levels of courses that eventually will get you a job. Those courses
*  are all somewhat related to the tech sector because the tech sector is kind of the hottest
*  sector right now and they range from inter-level digital marketing to very advanced self-driving
*  car engineering. We're doing this with the White House because we think it's bipartisan. It's an
*  issue that if you want to really make America great, being able to be part of the solution
*  and live the American dream requires us to be proactive about our education and our skill set.
*  It's just the way it is today and it's always been this way. We've always had this American
*  dream to send our kids to college and now the American dream has to be to send ourselves to
*  college. We can do this very, very efficiently and we can squeeze in the evenings and things to
*  online. At all ages. All ages. Our learners go from age 11 to age 80. I just traveled Germany and
*  the guy in the train compartment next to me was one of my students. It's like, wow, that's amazing.
*  I was thinking about impact. We've become the educator of choice for now, I believe officially
*  six countries or five countries. It's mostly in the Middle East like Saudi Arabia and in Egypt.
*  In Egypt, we just had a cohort graduate where we had 1100 high school students that went through
*  programming skills proficient at the level of a computer science undergrad.
*  We had a 95% graduation rate even though everything is online. It's kind of tough,
*  but we're kind of trying to figure out how to make this effective. The vision is very,
*  very simple. The vision is education ought to be a basic human right. It cannot be locked up
*  behind ivory tower walls only for the rich people, for the parents who might bribe themselves into
*  the system and only for young people and only for people from the right demographics and the
*  right geography and possibly even the right race. It has to be opened up to everybody. If we are
*  truthful to the human mission, if we are truthful to our values, we're going to open up education
*  to everybody in the world. Udacity's pledge of 100,000 scholarships I think is the biggest pledge
*  of scholarships ever in terms of the numbers. We're working, as I said, with the White House and
*  with very accomplished CEOs like Tim Cook from Apple and others to really bring education to
*  everywhere in the world. Not to ask you to pick the favorite of your children, but at this point...
*  Oh, that's Jasper. I only have one that I know of. Okay, good. In this particular moment,
*  what Nanogrid degree, what set of courses are you most excited about at Udacity or is that too
*  impossible to pick? I've been super excited about something we haven't launched yet and we're
*  building, which is when we talk to our partner companies, we have now a very strong footing in
*  the enterprise world and also to our students. We've kind of always focused on these hard skills,
*  like the programming skills or math skills or building skills or design skills. And a very
*  common ask is soft skills, like how do you behave in your work? How do you develop empathy? How do
*  you work in a team? What are the very basics of management? How do you do time management? How do
*  you advance your career in the context of a broader community? And that's something that we
*  haven't done very well at Udacity. And I would say most universities are doing very poorly as well,
*  because we are so obsessed with individual test scores and pays so little attention to teamwork
*  in education. So that's something I see us moving into as a company, because I'm excited about this.
*  And I think, look, we can teach people tech skills and they're going to be great. But if
*  we teach people empathy, that's going to have the same impact. Maybe harder than self-driving cars.
*  I don't think so. I think the rules are really simple. You just have to want to engage.
*  We literally went in school in K through 12, we teach kids like get the highest math score. And
*  if you are a rational human being, you might evolve from this education, say, having the best
*  math score and the best English scores, making me the best leader. And it turns out not to be that
*  case. It's actually really wrong. Because first of all, in terms of math scores, I think it's
*  perfectly fine to hire someone with great math skills. You don't have to do it yourself.
*  You can't hire someone with great empathy for you. That's much harder. But you can always hire
*  someone with great math skills. But we live in an affluent world where we constantly deal with other
*  people. And that's a beauty. It's not a nuisance. It's a beauty. So if we somewhat develop that
*  muscle, that we can do that well, and empower others in the workplace, I think we're going to
*  be super successful. And I know many fellow robot assistant computer scientists that I will
*  insist to take this course. Not to be named here. Not to be named. Many, many years ago, 1903,
*  the Wright brothers flew in Kitty Hawk for the first time. And you've launched a company of the
*  same name, Kitty Hawk, with the dream of building flying cars, EV TOLs. So, at the big picture,
*  what are the big challenges of making this thing that actually inspired generations of people about
*  what the future looks like? What does it take? What are the biggest challenges? So flying cars
*  has always been a dream. Every boy, every girl wants to fly. Let's be honest. Yes. And let's go
*  back in our history when we are dreaming of flying. I think my, honestly, my single most
*  remembered childhood dream has been a dream where I was sitting on a pillow and I could fly. I was
*  like five years old. I remember like maybe three dreams of my childhood, but that's the one I
*  dream most vividly. And then Peter Thiel famously said, they promised us flying cars and they gave
*  us 140 characters, pointing as Twitter at the time, limited the message size to 140 characters.
*  So we're coming back now to really go for these super impactful stuff like flying cars.
*  And to be precise, they're not really cars. They don't have wheels. They're actually much closer
*  to a helicopter than anything else. They take off vertically and they fly horizontally,
*  but they have important differences. One difference is that they are much quieter.
*  We just released a vehicle called Project Heavy Sight that can fly over you as low as a helicopter,
*  and you basically can't hear it. It's like 38 decibels. It's like that. If you were inside the
*  library, you might be able to hear it, but any of our doors, your ambient noise is higher.
*  Secondly, they're much more affordable. They're much more affordable than helicopters. And the
*  reason is helicopters are expensive for many reasons. There's lots of single point of figures
*  in a helicopter. There's a bolt between the blades that's called Jesus bolt. And the reason why it's
*  called Jesus bolt is that if this bolt breaks, you will die. There is no second solution in
*  helicopter flight. Whereas we have these distributed mechanism. When you go from gasoline to electric,
*  you can now have many, many, many small motors as opposed to one big motor. And that means if you
*  lose one of those motors, not a big deal. Heavy Sight, if it loses a motor, has eight of those.
*  If it loses one of those eight motors, so it's seven left, it can take off just like before
*  and land just like before. We are now also moving into a technology that doesn't require a commercial
*  pilot because in some level, flight is actually easier than ground transportation. Like in self
*  driving cars, the world is full of like children and bicycles and other cars and mailboxes and
*  curbs and shrubs and whatever you all these things you have to avoid. When you go above the
*  buildings and tree lines, there's nothing there. I mean, you can do the test right now, look outside
*  and count the number of things you see flying. I'd be shocked if you could see more than two
*  things. It's probably just zero. In the Bay area, the most I've ever seen was six and maybe it's
*  15 or 20, but not 10,000. So the sky is very ample and very empty and very free. So the vision is,
*  can we build a socially acceptable mass transit solution for daily transportation
*  that is affordable? And we have an existence proof. Heavy sites can fly a hundred miles in range
*  with still 30% electric reserves. It can fly up to like 180 miles an hour. We know that
*  that solution at scale would make your ground transportation 10 times as fast as a car
*  based on US Census or statistics data, which means you would take your 300 hours of daily
*  yearly commute down to 30 hours and give you 270 hours back. Who doesn't hate traffic?
*  Give me the person who doesn't hate traffic. I hate traffic. Every time I'm in traffic, I hate it.
*  And if we could free the world from traffic, we have technology. We can free the world from
*  traffic. We have the technology. It's there. We have an existence proof. It's not a technological
*  problem anymore. Do you think there is a future where tens of thousands, maybe hundreds of
*  thousands of both delivery drones and flying cars of this kind, EV TARS fill the sky?
*  I absolutely believe this. And there's obviously the societal acceptance is a major question. And
*  of course, safety is. I believe in safety, we're going to exceed ground transportation safety,
*  as has happened for aviation already, commercial aviation. And in terms of acceptance, I think one
*  of the key things is noise. That's why we are focusing relentlessly on noise and we build perhaps
*  the crisis electric V12 vehicle ever built. The nice thing about the sky is it's three dimensional.
*  So any mathematician will immediately recognize the difference between 1D of like a regular highway
*  to 3D of a sky. But to make it clear for the layman, say you want to make 100 vertical lanes
*  of highway 101 in San Francisco, because you believe building a hundred vertical lanes is
*  the right solution. Imagine how much it would cost to stack a hundred vertical lanes physically
*  onto 101. That would be prohibitive. That would be consuming the world's GDP for an entire year,
*  just for one highway. It's amazingly expensive. In the sky, it would just be a recompilation of
*  a piece of software because all these lanes are virtual. That means any vehicle that is in conflict
*  with another vehicle would just go to different altitudes and the conflict is gone. And if you
*  don't believe this, that's exactly how commercial aviation works. When you fly from New York to
*  San Francisco and another plane flies from San Francisco to New York, they're at different
*  altitudes, so they don't hit each other. It's a solved problem for the jet space and it will be
*  a solved problem for the urban space. There's companies like Google Wing and Amazon working
*  on very innovative solutions. How do we have space management? They use exactly the same principles
*  as we use today to route today's jets. There's nothing hard about this. Do you envision autonomy
*  being a key part of it so that the flying vehicles are either semi-autonomous or fully autonomous?
*  100% autonomous. You don't want idiots like me flying in the sky, I promise you. And if you have
*  10,000, what's the movie of fifth element to get a fee for what would happen if it's not autonomous?
*  And a centralized, that's a really interesting idea of a centralized sort of
*  management system for lanes and so on. So actually just being able to have a
*  similar as we have in the current commercial aviation, but scale it up to much more vehicles.
*  That's a really interesting optimization problem. It is mathematically very, very straightforward.
*  Like the gap we leave between jets is gargantuan and part of the reason is there isn't that many
*  jets. So it just feels like a good solution. Today, when you get vectored by air traffic control,
*  someone talks to you, right? So any ATC controller might have up to maybe 20 planes on the same
*  frequency and then they talk to you, you have to talk back. And it feels right because there isn't
*  more than 20 planes around anyhow, so you can talk to everybody. But if there's 20,000 things
*  around, you can't talk to everybody anymore. So we have to do something that's called digital,
*  like text messaging. We do have solutions. We have what, four or five billion smartphones in the
*  world now, right? And they're all connected. And some of us solve the scale problem for smartphones.
*  We know where they all are. They can talk to somebody and they're very reliable. They're
*  amazingly reliable. We could use the same system, the same scale for air traffic control. So instead
*  of me as a pilot talking to a human being in the middle of the conversation receiving a new
*  frequency, like how ancient is that? We could digitize the stuff and digitally transmit the
*  right flight coordinates. And that solution will automatically scale to 10,000 vehicles.
*  We talked about empathy a little bit. Do you think we will one day build an AI system that a human
*  being can love and that loves that human back, like in the movie Her? Look, I'm a pragmatist.
*  For me, AI is a tool. It's like a shovel. And the ethics of using the shovel are always with us,
*  the people. And it has to be this way. In terms of emotions, I would hate to come into my kitchen and
*  see that my refrigerator spoiled all my food, then have it explained to me that it fell in love
*  with a dishwasher and it wasn't as nice as the dishwasher. So as a result, it neglected me.
*  That would just be a bad experience. And it would be a bad product. I would probably not
*  recommend this refrigerator to my friends. And that's where I draw the line. I think to me,
*  technology has to be reliable and has to be predictable. I want my car to work.
*  I don't want to fall in love with my car. I just want it to work. It wanted to compliment me,
*  not to replace me. I have very unique human properties. And I want the machines to turn me
*  into a superhuman. I'm already a superhuman today thanks to the machines that surround me.
*  And I'll give you examples. I can run across the Atlantic at near the speed of sound at 36,000 feet
*  today. That's kind of amazing. My voice now carries me all the way to Australia using a
*  smartphone today. And it's not the speed of sound, which would take hours. It's the speed of light.
*  My voice travels at the speed of light. How cool is that? That makes me superhuman.
*  I would even argue my flushing toilet makes me superhuman. Just think of the time before
*  flushing toilets. And maybe you have a very old person in your family that you can ask about this
*  or take a trip to rural India to experience it. It makes me superhuman. So to me, what technology
*  does, it complements me. It makes me stronger. Therefore, words like love and compassion have
*  very little interest in this for machines. I have interest in people.
*  You don't think, first of all, beautifully put, beautifully argued, but do you think love has use
*  in our tools? Compassion? I think love is a beautiful human concept. And if you think
*  of what love really is, love is a means to convey safety, to convey trust. I think trust has a huge
*  need in technology as well, not just people. We want to trust our technology the same way,
*  in a similar way we trust people. In human interaction, standards have emerged and
*  feelings, emotions have emerged, maybe genetically, maybe biologically, that are able to convey sense
*  of trust, sense of safety, sense of passion, of love, of dedication that makes the human fabric.
*  I'm a big slacker for love. I want to be loved, I want to be trusted, I want to be admired,
*  all these wonderful things. And because all of us have this beautiful system, I wouldn't just
*  blindly copy this to the machines. Here's why. When you look at, say, transportation,
*  you could have observed that up to the end of the 19th century, almost all transportation used
*  any number of legs, from one leg to two legs to a thousand legs. And you could have concluded
*  that is the right way to move about the environment. We made the exception of birds,
*  who used flapping wings. In fact, there were many people in aviation that flapped wings to
*  their arms and jumped from cliffs. Most of them didn't survive. Then the interesting thing is that
*  the technology solutions are very different. In technology, it's really easy to build a wheel.
*  Biology is super hard to build a wheel. There's very few perpetually rotating things in biology,
*  and they usually run cells and things. In engineering, we can build wheels. And those
*  wheels gave rise to cars. Similar wheels gave rise to aviation. There's no thing that flies,
*  they wouldn't have something that rotates, like a jet engine or helicopter blades.
*  So the solutions have used very different physical laws than nature. And that's great.
*  So for me to be too much focused on, oh, this is how nature does it, this is replicated.
*  If you really believed that the solution to the agricultural revolution was a humanoid robot,
*  you would still be waiting today. Again, beautifully put, you said that you don't take
*  yourself too seriously. Did I say that? You want me to say that? You don't take me seriously.
*  I'm not. That's right. Good. You're right. I don't want to.
*  I just made that up. But you have a humor and a lightness about life that I think is
*  beautiful and inspiring to a lot of people. Where does that come from? The smile, the humor,
*  the lightness amidst all the chaos and the hard work that you're in. Where does that come from?
*  I just love my life. I love the people around me. I'm just so glad to be alive.
*  Like, I'm what, 52, hard to believe. People say 52 is a new 51, so now I feel better.
*  But in looking around the world, just go back 200, 300 years. Like, humanity is what, 300,000
*  years old. But for the first 300,000 years minus the last 100, our life expectancy would have been
*  plus or minus 30 years, roughly, give or take. So I would be long dead now. That makes me just
*  enjoy every single day of my life because I don't deserve this. Why am I born today when so many of
*  my ancestors died of horrible deaths, like famines, massive wars that ravaged Europe for the last
*  1,000 years, mystically disappeared after World War II when the Americans and the Allies
*  did something amazing to my country that didn't deserve it, the country of Germany.
*  This is so amazing. And then when you're alive and feel this every day, then it is so amazing
*  what we can accomplish, what we can do. We live in a world that is so incredibly vastly changing
*  every day. Almost everything that we cherish from your smartphone to your flushing toilet,
*  to all these basic inventions, your new clothes you're wearing, your watch, your plane, penicillin,
*  anesthesia for surgery, penicillin have been invented in the last 150 years.
*  So in the last 150 years, something magical happened. And I would trace it back to Gutenberg
*  and the printing press that has been able to disseminate information more efficiently than
*  before, that all of a sudden, we're able to invent agriculture and nitrogen fertilization
*  that made agriculture so much more potent that we didn't have to work on the farms anymore. And we
*  could start reading and writing and we could become all these wonderful things we are today,
*  from airline pilot to massage therapist to software engineer. It's just amazing.
*  Like living in that time is such a blessing. We should sometimes really think about this.
*  Steven Pinker, who is a very famous author and philosopher, whom I really adore,
*  wrote a great book called Enlightenment Now. And that's maybe the one book I would recommend. And
*  he asked the question, if there was only a single article written in the 20th century,
*  it's only one article, what would it be? What's the most important innovation, the most important
*  thing that happened? And he would say this article would credit a guy named Carl Bosch.
*  And I challenge anybody, have you ever heard of the name Carl Bosch? I hadn't. Okay. There's a
*  Bosch corporation in Germany, but it's not associated with Carl Bosch. So I looked it up.
*  Carl Bosch invented nitrogen fertilization. And in doing so, together with an older invention of
*  irrigation, was able to increase the yield per agricultural land by a factor of 26. So a 2500%
*  increase in fertility of land. And that, so Steve Pinker argues, saved over 2 billion lives today.
*  2 billion people who would be dead if this man hadn't done what he had done. Okay. Think about
*  that impact and what that means to society. That's the way I look at the world. I mean,
*  it's just so amazing to be alive and be part of this. And I'm so glad I lived after Carl Bosch
*  and not before. I don't think there's a better way to end it, Sebastian. It's an honor to talk to you,
*  to have had the chance to learn from you. Thank you so much for talking to me. Thanks for coming
*  on. It's a real pleasure. Thank you for listening to this conversation with Sebastian through
*  and thank you to our presenting sponsor, Cash App. Download it, use code LexPodcast. You'll get $10
*  and $10 will go to FIRST, a STEM education nonprofit that inspires hundreds of thousands of young minds
*  to learn and to dream of engineering our future. If you enjoy this podcast, subscribe on YouTube,
*  get five stars on Apple podcast, support on Patreon, or connect with me on Twitter.
*  And now let me leave you with some words of wisdom from Sebastian Thrun.
*  It's important to celebrate your failures as much as your successes. If you celebrate your
*  failures really well, if you say, wow, I failed, I tried, I was wrong, but I learned something,
*  then you realize you have no fear. And when your fear goes away, you can move the world.
*  Thank you for listening and hope to see you next time.
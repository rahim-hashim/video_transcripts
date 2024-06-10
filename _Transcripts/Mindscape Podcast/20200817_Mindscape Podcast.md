---
Date Generated: June 09, 2024
Transcription Model: whisper medium 20231117
Length: 5015s
Video Keywords: ['complexity', 'complex systems', 'misinformation', 'radicalization', 'networks']
Video Views: 9028
Video Rating: None
Video Description: Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2020/08/17/110-neil-johnson-on-complexity-conflict-and-infodemiology/

Patreon: https://www.patreon.com/seanmcarroll

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x

#podcast #ideas #science #philosophy #culture
Physicists have traditionally simplified systems as much as possible, in order to shed light on fundamental properties. But small, simple parts build up into large, complex wholes. Are there new rules and laws of nature that apply specifically to the realm of complexity? This has been a popular question for a few decades now, and we have some answers but not as many as we would like. Neil Johnson is an expert on complex systems generally, and information networks in particular. We discuss how self-organization can arise from individual units following their own agendas, and how we can mathematically characterize such behavior. Then we talk about information networks in the modern world, including how they have been used to spread disinformation and find recruits for radical fringe groups.

Neil Johnson received his Ph.D. in physics from Harvard University. He is currently professor of physics at George Washington University, where he heads an initiative in Complexity and Data Science. In 1999 he presented the annual Christmas Lectures at the Royal Institution in London. He was the recipient of the Burton Award from the American Physical Society in 2018. Among his books are the textbook Financial Market Complexity and the trade book Simply Complexity.
---

# Mindscape 110 | Neil Johnson on Complexity, Conflict, and Infodemiology
**Mindscape Podcast:** [August 17, 2020](https://www.youtube.com/watch?v=K7xVSv1bVSE)
*  Hello everyone, welcome to the Mindscape podcast. I'm your host, Sean Carroll. One of our long-standing
*  interests here at Mindscape is in the idea of complexity. Not just the simple systems
*  that particle physicists or cosmologists like myself like to study, but the interesting
*  phenomena that come into existence when things have many, many, many moving parts. And you
*  can find emergent behavior that might not have been immediately obvious just from thinking
*  about the component parts. Now we've talked about complexity, we talked about it recently
*  with Scott Aronson, but that was in the sense of computational complexity. How difficult is it to
*  solve a certain well-posed puzzle? Here we're going to be talking about complex systems. So
*  either physical systems that you could build up, like a robot or for that matter a human being,
*  but also social systems, information systems, the internet itself is a complex system. So Neil
*  Johnson is one of the experts in this area, an incredibly prolific physicist who heads up a new
*  initiative at George Washington University in complexity and data science. And our conversation
*  has two different focuses. The first part of the talk will be about what is a complex system? What
*  makes something complex? How do you know? How do you characterize it? So various words that you
*  might have heard before like power law behavior will appear. And Neil explains very, very clearly
*  how power laws are different than bell curves or other things that you might run across in the
*  natural world. But then we turn our attention to the specific idea of information systems and how
*  people get information in the real world. A lot of Neil's recent research interests are on how
*  extremism or conflict or various forms of bad behavior spread through complex networks. How do
*  extremist groups recruit their volunteers? How does disinformation promulgate through social
*  networks or through official news channels? So this is, as you might guess, scarily relevant
*  stuff to the modern world. He's a great explainer of things. This stuff is really important and
*  fascinating at the fundamental level. I think we're gonna learn a lot. So let's go.
*  Neil Johnson, welcome to Mindscape Podcast. Great to be with you, Sean. You know, we've talked about
*  complexity in some vague sense on the podcast before, most recently with Scott Aaronson,
*  where we talked about computational complexity, P versus NP kind of things. But your kind of
*  complexity, you're interested in complex systems, which is a whole nother kettle of fish. I mean,
*  why don't you start us off by telling us what you think of are the defining features when we
*  talk about a complex system?
*  Yeah, that's a great question. And it's very important to differentiate between something
*  that's complex and something that's complicated. You know, our lives are now complicated, because
*  we have to use all these kind of online platforms. We don't know if we're going to teach online or
*  not. There are complicated issues, but complexity is something more than that. And to give an idea,
*  let's just say, let's imagine we're doing something complicated tonight, we're going to
*  make a pizza, but we also got to pick up one of the kids and we've got to schedule these things.
*  That's complicated. But imagine if each one of those pieces now depends in some really
*  complicated way on what's happened before. And there are other people doing things at the same
*  time that impact us. So for example, if we're going out in the traffic, when it matters that
*  other people who may have decided to go out in the traffic with us are now, they're now
*  congesting the road and therefore affecting my chain of events. So that begins to move from
*  complicated to complex, because there's nothing that I could actually interconnect to the other
*  meaning of complexity. There's nothing easy for me to compute that would make the task easy,
*  that would kind of predict what would happen other than me going out and actually doing it.
*  So that's how it connects to the idea of complexity in a computational sense. It's sort of like the
*  length of the code that you need. You can't kind of simplify it. So that carries over to the complex
*  systems view in the sense that it's almost like all the things that could happen in the system,
*  feedback across scales, one local things affecting other things, the driver next to me,
*  affecting me, but also the fact that it's the all the drivers have come out at the same time for some
*  unpredictable reason. All of those things interact and make the system complex. Now out of complex,
*  out of that complexity, therefore, surprising things can happen. They can suddenly emerge,
*  traffic jams can emerge, stock market crashes can emerge out of nothing. And that is really where
*  the interesting complex systems kind of comes to the fore. Yeah, so I've been doing these videos
*  recently called the biggest ideas in the universe on some ideas in physics. And I've been pushing
*  the idea that physics makes progress via a spherical cow philosophy, where we ignore all
*  the complications and simplify down to the bare bones. And so in some sense, what you're saying
*  is that complex systems are exactly where that doesn't work, right? Where yet where all of the
*  interactions between all the different pieces really do feed into the final result. Correct.
*  And some of the things that we as physicists love to do, like we assume that interactions don't
*  depend on time positions can depend on time, but the form of the interaction doesn't depend on time.
*  And it doesn't particularly depend on maybe whether that spherical cow has some kind of
*  compass needle inside that makes it different on a Monday morning than on a Friday afternoon.
*  So those simplifications that enable us to get so far in physics, they don't work.
*  Yeah. And but nevertheless, like you just said, there are things we can say so that I mean,
*  that's where complex systems become interesting, right? Where it's not just well, things are
*  harder. So we give up, it's there's a new kind of thing we can start looking for.
*  Correct. And the challenge is finding that thing. And I've been scratching around in my career,
*  and a lot of people are doing a lot of important work in this area, we're trying to get you know,
*  you'd love to have something even, you know, even, you know, approximate, but general, in the sense
*  that it's reproducible in these systems. So it's that's a real challenge, you know, these systems
*  that we're talking about the traffic, they don't concern, you know, there's no there's no
*  conserved energy. There's, there's no sense in which it's the same at midnight as it is at 6pm.
*  So somehow, all these trends, all these symmetries that would have helped us in the problem are just
*  not there. Is it Is it safe to say that complex systems research is still in a kind of pre
*  paradigmatic stage where, you know, we haven't decided what are the crucial questions or the
*  the basic systems we can keep returning to? Yeah, I think that's a great way of summing it up.
*  You know, my every semester, my, when I go in, and I, I want to teach a class on complex systems,
*  but you know, what's the homework? Yeah, for the complex, you know, what's the simple examples
*  that they can work out that show complexity, and yet are simple enough in a homework that
*  nobody's going to turn around and say, Hey, that was an, you know, that homework couldn't have even
*  been done. That's where we are. And so it's funny, because it's like a double edged sword, there's
*  so much to explore, but that it can look from the outside that there's, you know, well, where's your
*  Schrodinger equation? Where's your Hamiltonian? You have nothing, you have nothing to show. And so,
*  yeah, it's, it's, it's, it's a challenge. It's certainly a challenge. But nevertheless,
*  I'm sure you have some favorite examples that you do like to lay on people. Yeah, I particularly
*  got interested in the this famous example of the L. Farrell problem, which we can, this is very
*  famous within the complexity community. No one else has ever heard of it. So you should definitely
*  share it with us. Exactly. And you know, I was in, so I'll lead into the story, but the L. Farrell
*  is a bar in Santa Fe, New Mexico. And you know, I happened to be there recently before the before
*  the lockdown, etc. And I was taking photos of myself against this L. Farrell bar, and they came
*  out, you know, what are you doing? Who are you? And of course, you know, as soon as I speak with my
*  accent, it's like, what are you doing? What exactly are you doing? Is this some is this a mo is this
*  something of concern? But of course, what I was really doing was taking a picture of a bar that
*  has become famous in the complexity field. And in some sense, it was, John Cassidy said, she'd solve
*  the L. Farrell problem, and you solve complexity. So let me maybe just just explain what that L.
*  Farrell problem is. It's, it really embodies everything to do with complexity. Here's the
*  here's the situation. And I'll vary it a bit from Brian Arthur, Brian Arthur introduced it, Brian
*  Arthur is at the Santa Fe Institute, and he introduced the following problem. I'll vary some
*  of the details, but essentially, it's like, so imagine there is some bar called, for example,
*  L. Farrell, and you want to go there a particular night a week, so Tuesday nights, you just happen
*  to want to go there, there's a band playing that you like, you just want to see them every
*  Tuesday night, you're not the only one. So there's some other number of people who probably want to
*  go there as well. Now here comes the problem that the L. Farrell bar, many bars only has a finite
*  number of seats, and you want to sit. And so does everybody else. So one can imagine the situation
*  that every Tuesday rolls around the problem, do I go or don't I go now if I go, I've got to get in
*  the car, I've got to go there, got to go through all that effort, and I might have to stand up.
*  So I would lose in that situation. If I stay at home, and I hear that actually there were enough
*  seats, maybe, you know, my friend tells me the next day, hey, you should have come to L. Farrell,
*  there are plenty of seats, then I've lost as well. And of course, there are the flip side of that,
*  there's two ways to win, I can make all the effort and go and I find a seat, I win. Or I stay at home,
*  and then my friend says to me the next night, yeah, you were right not to come, I win. And so
*  there's immediately so hip, but he that sounds like a game. And so, uh, that's not physics,
*  that's game theory. No, because there is some indeterminate number of people say 100 that I
*  don't know, I have no connection with. And they're doing they're trying to do the same thing. So
*  imagine we all hit the same strategy, we all have the same, in other words, we become identical
*  objects, or we become rational in some way. So we all do the same thing. That means we either all go,
*  or we don't, it doesn't actually matter what individual role we follow, we're either all
*  going or we're not. And of course, that immediately becomes the wrong thing to do. And so Brian Arthur
*  very cleverly with this one simple example, set up the idea that I therefore have a system
*  of objects that are heterogeneous, that don't have full information about the system.
*  Maybe they know the last few weeks, whether it would have been good to go or not. And they've
*  got to make some decision about what to do the next time. They're all trying to do the same thing.
*  If they all do use the same strategy, it becomes a losing strategy. So there's this internal kind of
*  frustration, we begin to be you know, anyone who knows, you know, if you know, people who know
*  things about spin systems immediately, you think, okay, it sounds like a bunch of meta stable states
*  that, you know, this thing is going to bounce around between and that's the whole point.
*  But by the way, I mean, it's worth noticing that there is something subtle here, because
*  for the paradigmatic question about complexity, this is a really simple problem, right? The problem
*  is not complex, you go to the bar, you don't, that's, that's the question.
*  Correct. And then that is the you absolutely hit the nail on the head. It sounds so simple.
*  And there are so many other examples you could think of in, in, in the world, you know, do I go
*  to the supermarket, particularly now, I don't want it to be crowded. In the sense, I may have to wait
*  in line to get into so do I make the effort or don't I the traffic, I've got two routes to go home,
*  do I take this route or the other route, the market, do I buy, or do I sell, it matters,
*  not that there's some intrinsic value in the it matters whether everyone else is by saying with
*  housing market, do I buy when everyone else is buying bad idea. So you get the idea that there's
*  some some variant and the and the dynamics that come out of this model and people have studied
*  this, the physics community has started this a lot now since, since the since the 90s.
*  The dynamics are so rich. And they go beyond any physical system that we can really think of
*  because I as one particle, I mean, that's what I love about the problem, I can think of myself as
*  a part of what would I do? And of course, I take, I probably remember something about the last three
*  weeks, and then I've got some kind of little rule in my head that says, if that happened, then do
*  this. And we will probably doing something like that. It's a wonderful so there's, there's,
*  it's non Markovian, you know, it depends on the past, and it depends on the history.
*  Yeah.
*  And there's definitely feedback, I will adapt. That's the other thing. These were particles that
*  adapt. So we're heterogeneous, we have memory of the past, and we adapt. So if it doesn't work,
*  I'm going to change my system, probably to a worse one, but I will change.
*  And I guess probably to a lot of people who hear this problem, they're going to say, well,
*  isn't the answer just like, go 60% of the time randomly? I mean, why isn't the answer that simple?
*  Yeah, so we could do it whereby this, I have some kind of loaded dice, and you know, with a 10 on
*  it, 10 num 10 faces on his arm, and I roll it. So you know, when it's the first six numbers,
*  that's my 60%. So I would go then or and I would stay behind. So that would be a probabilistic way
*  of solving it. But of course, I'm not going to sit around and wait for that. That's not the way I roll.
*  That's not the way I work. I'm not a random object. I take I have memory of the past,
*  I will try and adapt, I'm trying to win. And so this is where it gets really interesting. And you
*  could think of it connecting to things in smart materials, where you do embed kind of this agent
*  behavior, or even physics itself, that there's some other particle may be trying to optimize
*  something, or, you know, certainly minimize its energy or do something like this. And if it has
*  some kind of glassiness, some memory of the past, it's not going to just be the equivalent of flipping
*  coins. And so this is where we've the physics community actually, you know, this, this, this
*  elder for our problem is what really got me interested in complexity. And it I naively
*  thought that the, for example, the economics and finance field would be absolutely,
*  they would love this problem. But the you know, still 20 nearly 20 years later,
*  it really, they haven't really embraced what Brian Arthur was really talking about,
*  in terms of this, you know, the in terms of this inductive behavior, rather than absolutely being
*  able to compute the ground state and then sticking with it. Yeah. And I think it is because
*  it's it doesn't really fit in with any of their paradigms. There is no rational actor, you can't
*  even perturb the rational actor, there's no equal, there may be an equilibrium of sorts, but it's
*  really bouncing around between meta stable states. So it's much closer to what a physicist would
*  like to hear about than what are some of the other disciplines. So what are I mean, I'm just
*  trying to give the audience a little bit more of a feeling for what the solutions look like, even if
*  the problem is not completely solved, you mentioned that there are meta stable states, does that mean
*  like, I go every week or I never go? Yes, so there's one particularly interesting behavior
*  that emerges. So I'd mentioned in the past that, you know, complex systems can have emergent
*  phenomena, you know, something. So what is that? So I'm going to so there is one of a wonderful
*  behavior that happens. There's a terrible first of all, I'll give you the bad news, the terrible
*  behaviors, of course, when we all think we have the right rule. And, and then when we change our
*  rule, we change it in similar ways. And so we're always doing the wrong thing, that would be a
*  huge crowd phenomenon, right, whereby a whole crowd go or they don't go. So the fluctuations
*  in that system would be of the size of the number of particles, which is that's an that's, that's a
*  system instability, which is interesting in itself. But there's a wonderful emergent state that arises
*  that you can think of in the following way. Imagine you're out, you and I are following our
*  rule for how we're going to decide whether to go and we begin to diverge in how we change our rule.
*  And other people are following more closely, you just inadvertently or me in terms of how we adapt
*  our strategy. And we can adapt, we can develop into effectively a crowd following one strategy,
*  and a crowd, which I would call an anti crowd, following the opposite strategy, not neither
*  strategy is good, nor bad, because it sort of just depends on what everyone else is doing. But
*  imagine out of those 100 people, 50 are following a rule that says, go on the I mean, it wouldn't be
*  as simple as that, but go on the odd number weeks. And then the other 50 are doing will go on the
*  even number of weeks. So they don't know each other. They haven't coordinated any sense. They
*  just kind of ended up. They don't have a Facebook group. That's right. They had no Facebook group,
*  which brings us onto that brings us on to other you'll get there later. But the but
*  without any coordination without any local information, just global information fed back
*  to them, like some external field being sending them news global news, they've managed to split
*  themselves into a 50 of a 50, which means that if you look at the if you're the bar manager,
*  and you're looking at the system output, in other words, how many people are actually sitting in your
*  bar, you're hitting 5050505050 you have no fluctuation. Yeah, perfect. And even if we all
*  tossed coins that were actually not even based on 6040, pretend we don't even know what the seating
*  is. We just toss a coin to Cyworld to go that has fluctuations in it because right, you know, 60 heads,
*  40, tails, 70 heads with 30 tails. But that's that that end result that system result purely driven
*  from competition of the 50 and 50 gives no fluctuation in the system. So that begins to
*  make you wonder, goodness, is it possible that I could even design then many complex systems,
*  whether they be, I don't know, could be drones could be things, you know, that don't want to
*  get in each other's way, it could be something in a biological system, could I, if I could one way
*  of controlling complex systems be to kind of nudge them, so that half of them are following
*  one strategy and half of them are following the opposite strategy, or even if there were many,
*  many strategies, make sure that they're sort of paired up in opposites. That would be that's,
*  that's a wonderful outcome from that studying that very, very simple problem.
*  I want to pause to talk about policy genius.com, an insurance marketplace that is built and backed
*  by a team of industry experts. A lot of people are wondering whether right now it's even possible
*  to buy life insurance. And the answer is yes, it is possible. And in fact, if you have other people,
*  loved ones who depend on your income, maybe this is a good time to think about doing it.
*  The steps are very simple. You head to policygenius.com, where in minutes you can work out
*  how much coverage you need and you can compare quotes from different top insurers to find your
*  right price. You apply for the lowest price that applies to you and the policygenius team will
*  handle all the paperwork and all the red tape. Policygenius works for you, not for the insurance
*  company. So if you hit any speed bumps during the application process, they will take care of
*  everything. That's the kind of service that has earned policygenius a five star rating across over
*  1600 reviews on Trustpilot and Google. So if you need life insurance, head to policygenius.com
*  right now to get started. You could save $1,500 or more per year by comparing quotes on their
*  marketplace. Policygenius because when it comes to insurance, it's nice to get it right.
*  Well, I think this is this I like that that possible solution has been given because that's
*  how we see that this very simple problem is a paradigm for complexity because of that emergent
*  feature that you wouldn't have guessed, right? Without central planning or even explicit
*  cooperation, some kind of pretty good solution emerges out of people trying their best individually.
*  Correct. And actually, it's probably even better than trying to do it top down. Imagine you're
*  actually calling up the people and saying to them, well, you're one of this group, or you're one of
*  the opposite group this week. Would they listen to you? Yeah. So the fluctuations that will come
*  out of trying to force people to do something would be even worse than the ones that come out
*  of competition. This is a slight deviation from the line here. But your discussion reminded me
*  of a question that has been working at me for a while, like game theory, which is a theory of
*  making decisions under situations of competition and perhaps incomplete information, etc, etc.
*  Is game theory secretly physics? Like, can we reduce it all to statistical mechanics? You know,
*  optimizing some utility function kind of sounds like minimizing some Hamiltonian or some action
*  or something like that. Sure. And I would I think you should go out and write that book. I want to.
*  I will buy it. And I will because I think you're right. Yeah. In fact, you know, there are lots of
*  hints of that in the time, particularly in the type of, you know, probabilities that are you the
*  forms of the probability that are used by quote unquote agents look very much like two level
*  systems in a finite at a particular temperature, the probabilities, the maximum weightings.
*  And so you're absolutely right. I wish I'd have had that graduate course when I was doing my PhD,
*  that would have kind of laid the scene. Instead, I've had to kind of learn it the hard way from
*  standing up standing up and having game theorists call out, oh, what you're telling me is game
*  theory. And I feel like actually, what you're telling me is physics. But so this is something
*  that you agree is is sounds kind of truish, but it is not an accepted fact that has been well known
*  since von Neumann or something like that. Yeah, although, I mean, there are there are even closer,
*  it's remarkably, there's a area of game theory now, after all these years, after, you know, here,
*  seeing Beautiful Mind and all these things with two gay two player games. There's now an area of
*  game theory called mean field. Okay, there we go. Mean field game theory. physicists sneaked in.
*  So this has emerged in pretty recently. And it purely inspired by physics, the idea that mean
*  field approximation. It's funny, because, you know, in physics, if you go around saying, oh,
*  I'm just going to do mean field theories, people will very quickly tell you when mean field theories
*  break down. But they the game theory community have, as they've tried to get towards more and
*  more players have realized that there's no way they can write out exactly what each of these
*  10 to the 23 players will be doing. So they need some kind of renormalization of the system. And
*  that comes through this mean field game. So if there is an area, which would really, really profit
*  from people from the physics community joining with people from the game, they're not neither
*  have got the right answer. Yeah. But that is really a particularly for the dynamics, a thing,
*  how things get towards equilibria or avoid equilibria. That's the interesting bit. Yeah,
*  you know, as they said, you know, in the end, we're all, you know, in the long run, we're all
*  dead. equilibrium is death. So every system we're interested in, all of us, you know,
*  whether you expansion of the universe, that's a non equilibrium system. So it's the it's the
*  behavior away from the dead state that we're all interested in. But that is the hardest. And
*  physicists themselves are not that great at that, as I know from experience. But correct you. But
*  you also you mentioned some phrases that I want to sort of repeat, because it reminds us how this
*  is not a simple physics problem, even if there is some version, I mean, you mentioned adaptive agents
*  and also rational agents mean part of the what makes in my mind complex systems different than
*  just physics systems is that, you know, we're not dealing with particles that are dumb and memoryless
*  and just bounce off each other, right? Like part of what makes a complex system is that we assemble
*  it out of individual pieces that themselves have some structures and maybe even goals and memories
*  and things like that. Absolutely correct. And so one of the challenges I'm particularly involved in
*  in my my my own work is, how can I embody that in the simplest possible way, that kind of internal
*  character, it always reminds me of Einstein's phrase of the, you know, kind of hidden variable.
*  How can we put in how can we put in some kind of characteristic that is simple enough, that captures
*  what you just said, captures that adaptiveness, etc., but doesn't go overboard and suddenly become,
*  you know, I need a whole book just to explain one person. Yeah, okay. Well, but you know, that's why
*  it's interesting. So that's so I think we have a good feeling now about what complex systems can
*  be and how they arise. But despite the fact that it is still arguably pre-paradigmatic,
*  some things appear over and over again. And one of the obvious things I'm thinking about are power
*  laws. Maybe you can explain to the audience what a power law is, why we care. And are you someone who
*  thinks that looking for power laws is a very important thing? Or do you think it's overrated?
*  That's a fantastic question. Well, the so just to set the scene, we talked about coins tossing
*  coins, I think it's imagine if we all toss coins, toss 100 coins, pretty much 50, 55, 60,
*  not so often 70, very infrequently 80 would come out as heads. So there's a distribution of outcomes.
*  And that distribution looks like goes up as a single peak as a bell curve. Yeah, it's a bell
*  curve. So we do we as a society, we do a lot with bell curves, we assess risk, we think about
*  medicine in terms of bell curves, we think about the average patient response, and we should do I
*  mean, that's a very reasonable thing to do. If on average, people have some kind of average behavior,
*  of course, in medicine, you'd think that the biology is has an average, you know, and maybe
*  there's fluctuations, but there's some kind of average behavior. But when you get in and look at
*  social systems, and actually a lot of physical systems as well, they're these averages do not
*  necessarily characterize the system very well. Think about the I mean, it's a very topical thing
*  now, of course, wealth, the distribution of wealth in the country, a lot of people have little,
*  very few people have a lot, right, but that distribution looks nothing like a bell curve,
*  there is no kind of, here's the average, and then there's a few outliers, you know, one in a one in
*  a billion has more than twice the, you know, or more than three times than the average wage,
*  we all know that that is not true. In fact, that tale of wealth goes on a long, long way.
*  And so you're in a situation where almost everyone is below average.
*  Right. And so if you're doing and of course, economists do not do this, taking building an
*  economy around the average and assuming that everyone who has the average income, and then
*  plus or minus, you know, $10 here and there, you know, then all houses would have to be the same
*  price. You know, and there would be no high end restaurants. Yeah, it would, because that would be
*  everything that would be available to us. So we know that in other real world settings, we have
*  nothing like a bell curve. Now here comes the problem. Bell curves are wonderful for calculating
*  things like risk, and the odds of something being, you know, an unlikely event. And we can calculate
*  lots of things we build buildings based on a bell curve, we assume that, you know, nobody comes in
*  the room that is somebody can come in at six foot, but they're not going to come in at 6000 feet.
*  Yeah, of a height. Right. And, and if we did that, I mean, if that were the case, that every so often,
*  every, you know, once in every nine months, you get somewhat of 6000 feet, suddenly buildings would
*  be that we would have lost the purpose of buildings. So it's ingrained in the way we think that some
*  things are bell curves, and some things are other kind of distribution. The problem is we don't
*  really have a good mathematics of, of other these other distributions that are so called fat tails,
*  where somebody can be earning 1000 times what somebody else is is earning. And so those fat
*  tail distributions are a problem. Now, in physics, we are pretty used to those type of distributions,
*  a particular form of them are called power laws. And the power law is characterized by the fact
*  that what happens at one scale is exactly the same as what happens at another scale, it's just
*  kind of twice as much or half as much. Now, let me give an example. This scientist and physicist
*  in particular are fairly convinced seem fairly convinced that things like earthquakes follow a
*  power law, or might follow an approximate power law, which means there's a very deep consequence
*  of that. It's not just that, well, there could be very big earthquakes, it the consequences that
*  it's scale free, the behavior, in other words, what's happening, earthquakes of a certain size
*  is the same as what's happening for earthquakes, twice the size, just just at a different scale.
*  Now that that's the consequence of that is if you were building a theory of big earthquakes,
*  dangerous, big earthquakes, you really should just build use the same theory that worked
*  at lower scales. In other words, the science carries over from scale to scale, it's not like
*  there's some new phenomenon that suddenly appears as you get to earthquakes of a certain size.
*  So that idea of scale free is a very powerful thing in science, and particularly in physics,
*  because that is the distribution that occurs when a system tends to be near some kind of
*  phase transition, so called transition between system behaviors. To just give an example,
*  forest fires are another example, talk about earthquakes, let's talk about forest fires.
*  Forest fires at the transition between no fire across the system and fire spreading everywhere,
*  they tend to have a power law distribution in the kind of clusters that are burning, for example.
*  So this idea that power laws exist at critical junctures in complex systems is a very powerful
*  one and a true one. Let me jump in just a second here, because I think I remember back when I was
*  a graduate student, and I was confused sometimes by the phrase phase transition being invoked in
*  different circumstances, because I think of phase transitions of like, you know, melting ice or
*  freezing water, and there are things that happen over time. But when you talk about the forest,
*  or the earthquakes, having distributions of sizes of events that are characteristic of phase
*  transitions, it's not because, I think, correct me if I'm wrong, the forest is literally undergoing
*  a transition from one phase to another, it's that there could be different phases, and the forest is
*  perpetually stuck in between them. Is that basically right?
*  Correct. That's a fantastic observation. You're absolutely correct. So a shortcoming of the
*  current understanding of power laws and phase transitions is that they happen exactly, you sit
*  the system there, and it's either there or it's in another situation. Describing how something
*  would happen in time is the area of dynamical phase transitions, which is a really, that's a
*  much newer area of physics, because it's a system out of equilibrium. One can talk about systems,
*  it quite unquote, in equilibrium, I'm going to set the fire, the forest, you know, just at the,
*  it's just at its critical point, just where the fire would spread, or it wouldn't spread. Yeah,
*  okay, but that's stationary in time. But if I'm thinking of something beginning to spread,
*  and I'm fanning it, or I'm adding things in from the outside, you know, more trees, it would be
*  equivalent, or for a COVID outbreak, for example, more people, more susceptible people, that gets
*  into the dynamics, the dynamical phase transition, that's a much harder situation to describe. But
*  the relevance of the power law is still there, because you can imagine situations where I have
*  a whole bunch of objects affected, which will be a huge event, that's like having one person have
*  a whole bunch of all the money in the world. Or I can imagine many times it would just be, you know,
*  just a few examples, many times it would just be a few objects that are affected. So that's,
*  that's the whole the rest of us that are not earning very much. Yeah. So the power laws are
*  pretty ubiquitous. Now there has been, of course, a an interesting debate in the
*  literature as to, well, is it really a power law? Is it approximately a power law? But,
*  but putting that I think that's a little bit, that's getting a little bit too inside baseball.
*  Yeah, because in the end, we could do an experiment, right? Oh, I'm since we're home now,
*  we do experiment on a phase transition. And, and we could try and map out the size of the clusters,
*  even though it's a correct phase transition, because of the way we're measuring it, we haven't
*  got all the information, we're not recording it properly, we make mistakes, that we're not never
*  going to get a perfect power law. So the power law is more indicative that there's the system
*  is on some kind of tipping point. Right, I guess that's what that's what I wanted to get into,
*  because I think that sometimes from the outside, people see various kinds of in various kinds of
*  disciplines, people show power laws, they debate what the exponent of the power law is, or whether
*  it is a power law or whatever. But but the thing that gets missed is, the reason why we care is
*  because the existence of a power law might be pointing to some physical mechanism that creates
*  this right? It's a different kind of physical mechanism that would create a bell curve.
*  Correct. And so that the fascinating thing then becomes a hey, yeah, I may have two systems that
*  have power laws, if they've got the same slope, that's a little bit like an exponent with that,
*  that that's like saying two mountains that are both red slopes, yeah, for skiing. If they've got
*  that they may be a similar mechanism behind them. And one of those mountains may be in Europe, the
*  other may be in California, and it doesn't matter. There's something about the way that mountain got
*  created that gave it the same slope. And so it gives the hope that there may be some simple kind
*  of mechanism that and this is where we get into, you know, I've worked in my in my in my work in
*  this area, we've we've worked on things to do with casualties in wars, you can get into a lot of hot
*  water talking about this in this way. But it's actually a fact that when you look at casualties
*  from conflicts, for example, they can be very different conflicts from very different parts of
*  the world, different motivations, if they have this, they have very similar power law slopes,
*  exponents, which means that at the end of it, just somehow in the way that humans are doing things,
*  is the same in both places, the mechanisms of it's how humans do conflict, like it's how
*  rocks get put together to make a red slope mountain. Well, I mean, this is a perfect segue,
*  because that's exactly what I wanted to do roll up our sleeves a little bit and get into the
*  applications. And I know that you've been very heavily involved in conflict and radicalization.
*  And very, I don't know why you've chosen a whole bunch of ways that people die as your as your
*  complex systems to study. But we won't go into that. But, you know, so what is the so when we
*  talk about these things, a power law of what what is it that we're actually studying?
*  Yeah, that's a great question. I will do a little quick shout out of why on earth I would end up in
*  that. Steve Strogatz, Cornell, previous mindscape guest. Oh, fantastic. He, I he once said
*  that he studies the particular things I think it was in reference to his Romeo and Juliet studies
*  of non-linear dynamics. Yeah, he finds it interesting to look at topics that are somehow taboo.
*  And that stuck with me. And that that's an interesting area, just because it's
*  unpleasant, the fact that there's now data, a lot of data. So my interest in this cruise through
*  the Iraq War and the other wars that were going on. And that was one year in Colombia, we're going,
*  that's what suddenly, wait a minute, I, I can look, we can look at these two wars.
*  Let's forget all the thousands of books have been written on their motivations and their
*  consequence. Just look at the numbers, the number of people that get fatalities per day,
*  something like this or per event. What would we see? So that's how we got off on that. And actually,
*  this goes back to Louis Fry Richardson was a, he was a physicist, they ended up looking at meteoric,
*  what kind of weather patterns, etc. But he in the First World War, got in his head that somehow to
*  understand the human condition, human conflict, he would just track numbers of people in casualties.
*  So I'm sorry, a number of casualties in in wars. So we did the same thing, he didn't have the
*  benefit of knowing in the individual events in a conflict, how many people were killed, he just did
*  add the totals for wars, which is more kind of messy, you get a messier result. But during the
*  two early 2000s, when unfortunately, of course, there was Iraq, a war going on, Afghanistan was
*  going on, Colombia was going on, we started to look in exactly the same way, same lens,
*  at these three conflicts. And also glue and terrorism, there are terrorist events, we looked
*  at all of these in the same way in the and it was as follows. We looked at the number of casualties
*  per event. So for example, okay, there may be five days when nothing happens, and then there's
*  something happens, and this number of people were killed. And we just literally plotted it out as a
*  histogram, like you would plot out how many people earn a certain amount of money, it's now how many
*  events had a certain amount of fatalities. And I think we did, I'm not sure what we expected to see.
*  Isn't that always the beauty? You're not really sure when science people say, what did you expect
*  to see? I'm not sure. But you might have expected to see something like a bell curve. You might have
*  expected that well, you know, maybe in Iraq, with a particular kind of capability among the insurgency,
*  they would create a certain average number of fatalities every time they decided to get involved
*  in some event. And then there'd be kind of fluctuations around that. Yeah, there's some
*  kind of best kind of attack that they just did over and over again. Yes. But that's not what we
*  found. So what we found was actually more like the mountain slope, more like the histogram of
*  income. We found lots of events where very, very few were fatalities. And then there's a whole
*  spectrum up to a few events that were absolutely huge in fatalities. And when we said we did the
*  statistical test, etc, etc, to check that the that it was a good goodness of fit, as they say,
*  for the power law. And when we looked at the slopes, what we found was we were looking at Iraq,
*  Colombia, by that time, Word had got out and we were being sent all these data sets from all these
*  different wars that some of which we'd never even heard of. But when we looked at them now,
*  there's an important point, a lot of these were wars that were involving some kind of large state
*  with some kind of organic, if we can call it that opposition. Not like the old World War Two kind of
*  wars. Right. Not like and certainly not like the Hollywood movie, you know, line them up at dawn
*  and two massive armies just well, which is an interesting point, interesting scientific point,
*  because the that Hollywood picture of just line up at dawn on opposing sides and just, you know,
*  basically keep going till nobody's left standing. That's like, if you think about it in a kind of
*  abstract way, that's like a test tube of two reacting species that kind of just interact all
*  day. And there's nothing left at the end of it except the product. But these other the modern
*  wars, they cut the insurgencies. And this is where again, we got into pretty interesting territory
*  with the social sciences of what whether you call it an insurgency or it's a narco gorilla.
*  In the end, these are the numbers. Yeah, these are the numbers. We got power laws, and they all had
*  the same slope. Which is like saying I've gone round my I'm gonna go around the world, look at
*  all the mountains. Oh, my goodness, they've all got the same slope. Right. Which is not true in
*  the real world for mountains, but which is not true in the real world for mountains. But it was
*  true. And still and so we published this back in 2009. And we were expecting a deluge of people
*  sending us results that were not power laws, therefore, and didn't have it even if they were
*  power laws didn't have the same slope. But to this day, interestingly, now that we have much better
*  data sets, and there are many, many people have now into the counting the dead, if I can call it
*  that science in the social sciences and actually doing a remarkable job of counting fatalities per
*  event. Still to this day, the the the this idea that they're a power law holds up, and they all
*  seem to have the slope around around the red slope, which in this case is a 2.2.5 slope. Yeah,
*  it's remarkable. And it's actually the same as the slope for terrorist events. So this is and
*  since then, we've come up with some physics models to try and explain that physics based models,
*  which have to do with the way that particles, unlike the Hollywood situation of everybody lining
*  up in a, you know, kind of mimicking what goes on in a test tube, it's more the idea that objects
*  insurgents form into clusters. And it's the what you're seeing is really the clustering attack,
*  you see a cluster attack. And so it's more to do with the way in which people form clusters. So
*  human beings forming clusters between them. I mean, maybe maybe that's worth going into more
*  because when I think of these power laws, like you mentioned classically, income,
*  the explanation that comes to mind is the rich get richer, right? It's not just a random distribution
*  of money. Once you have money, you can get more. And so there's a few billionaires and a lot of
*  poor people. But for terrorist attacks, they seem more independent of each other. And so so but
*  but you're hinting that the that there's some network phenomenon that explains some agglomeration
*  of attackers that can help give us this power law. Yes, correct. The and it comes out a very,
*  very simple story. If we if you and we could do this now we sit in we can either write it out with
*  pencil and paper or do it on a in a simulation. If you take the simple rule that people, for example,
*  in case we talk about insurgency, since they're fighting some very strong state army or coalition
*  army, they need to group together into something that is pretty substantial. So they're trying to
*  group together trying to coalesce into some kind of cluster. However, they are every so often being
*  broken up because just like, you know, you look at fish, fish under the, you know, the all these
*  national wonderful now that we're all at home watching National Geographic programs, you know,
*  you see the fish gradually coalesce, they coalesce, they coalesce. And then they get
*  sense that there's a predator and they scatter, they fragment. And that simple, simple, simple rule
*  of coalesce, coalesce, and then occasionally fragment remarkably gives exactly it not only
*  is it give a power law, it gives a power law with a 2.5 slope. And so for all these years since 2009,
*  we've been carrying this, this is our little story, a waving our little banner, saying that,
*  well, I understand that, yes, they could be leftist, they could be rightist, they could be this,
*  they could be that they could be fighting in a jungle, they could be, they could have cell phones,
*  they may not have self. In the end, I'll just give them two properties, they gradually aggregate,
*  well, not gradually, they just aggregate. And then they've and they fragment. Now make one slight
*  addition to that. The distance between them is not as important as you might, in other words,
*  it's not, we're not going to make it so good so that they can aggregate over arbitrary distances.
*  Now, what do we mean by that? What we really mean is that they're really kind of just coordinating
*  over arbitrary distances. And that that's actually known for most of those wars that we talked about
*  2003 onwards, there were cell phones, there were people coordinate, so they would coordinate
*  to do to do things in two places at once, for example. So the idea of coalescence
*  without a distance and fragmentation gives you the 2.5. Now, since then, lots of people have studied
*  it, we've also done our own made our own efforts, you can put in distance, you can do all this,
*  doesn't really get too far away from what what I just said. And the beautiful thing is, and this is
*  the graduate problem that I always said on my complex systems course, and show with pencil and
*  paper that that's true. And it's really, it's two and a half pages and I remember you remember I
*  remember doing a lot worse homework problems. Oh, yes. That's very interesting. And actually,
*  the way that you explained it there, makes it seem very transparent to those of us who
*  who know a little bit about complexity that it resembles the classic sandpile avalanche problem,
*  right? Like you dribble sand onto the sandpile, and it will occasionally set off an avalanche. And
*  so it grows slowly, but that it collapses all at once. Correct. And so what I like about this is,
*  I always feel that every day I woke up in this complex systems field, I know less than I did the
*  day before. But it's that model that I just is helping me understand now I understand what
*  what they meant by punctuated equilibrium. Now I understand what they meant by,
*  you know, so you can go back and look at these related ideas. And say, Aha, now I see how to
*  kind of unify. It's not that we've come up with some fantastic mechanism and others didn't have
*  it. Others were probably on the point of having that as well. Maybe we're getting towards a unified
*  science. Yeah. So this is an overly ambitious question. So feel free to punt it. But one of
*  our first guests on Mindscape was Jeffrey West. And he talked about his scaling laws that have
*  these one quarter powers, right? One quarter, three quarters, etc. And he claims to have a
*  mechanistic explanation that relies on the fact that he's talking about biological organisms or
*  spatial systems that exist in three dimensional space. And the four in his power laws is three
*  plus one. If it were a different number of dimensions of space, it would be a different
*  fraction rather than four. Is there a similar feel good story you can tell about the 2.5 slope
*  that you get? I think he's trumped me on that one. He got he got he got a he wins that one,
*  because that's a that's a fantastic way of saying it. The the 2.5. Interestingly, is it's a little
*  bit more involved the explanation. But it there are two levels of explanation. First is that power
*  laws between two and three actually have if you were to calculate their standard deviation, which
*  is the size of the fluctuations, it actually diverges. And so there are systems that are in
*  some sense, infinitely adaptable, they can form small clusters, they can form large clusters,
*  in a way that's kind of like an evolutionary advantage. So it being between two and three and
*  slap bang in 2.5 sort of makes sense. Now that is that's a less direct answer. But the more
*  direct answer in the two and three is, interestingly, if you now add in the distance and make those
*  clusters form in a two dimensional space, that exponent moves from 2.5 down to two.
*  And that makes more sense because they're now on a 2d space 2.5 is really, it's like clusters are
*  forming, they're not in 2d, they're not in 3d, they're sort of in between. But I don't like that
*  a particular explanation. What I do prefer is actually the one that 2.5 is a good thing for
*  a system that is trying to compete and win. Well, that I guess that was a set of questions I had
*  as a physicist who's just sort of trying to get into complexity myself, but you know, who grew up
*  doing nice clean things like gravity and particle physics, etc. You know, these are all open systems
*  that you're talking about, right? I mean, they're they're dynamical, they exchange information and
*  energy with their environment, they're affected by the outside world. Is there something is there
*  some story to be told about entropy and free energy and dissipation that that helps us understand
*  why these systems settle into this kind of power law? Or is that something that would be different
*  for every system or we don't even know yet? I think it's a fantastic question. So that would be
*  a fantastic I know that there are there there is certainly work going along on that there is no
*  definitive answer that I that I personally know of. But one would think that I think it's such
*  an important question that you just asked, because in some sense, you answer that and you've answered
*  this kind of science of life. Well, yeah, because life itself is nothing more than us trying to keep
*  ourselves away from the equilibrium. And so exactly what goes on in a non equilibrium system as it's
*  it's heading towards the inevitable. However, on its way, it can do all sorts of wonderful things.
*  And getting an idea of that beyond just the kind of idea that well, over time, entropy increases,
*  so we're all going to just. Yeah, it's it's the dynamics of that, which I is not worked out. So
*  you're absolutely right with that. I think it's absolutely the pertinent question to ask. No
*  clear answers yet. Yeah, I mean, it might be speculative. But I mean,
*  can you imagine that there's some principle that will someday hit on that this sort of power law
*  scale free distribution either maximizes or minimizes some entropy or entropy production
*  rate? Is that the kind of thing we might be looking for? Like this this complicated tree
*  network system lets us use use up entropy as efficiently as possible?
*  Yes, I think that might be correct. And particularly if we take the vision of sorry,
*  the interpretation of entropy as an information. Exactly. Measure, then in that case, I'm
*  absolutely with you on that, that I do think it kind of comes down to a sort of and and in that
*  sense, then living systems are in some sense playing an information game with the rest of nature.
*  And so they're kind of boring information for a while. They're giving it back. You know, there's
*  in a similar way that one might think of as an entropy of the entire system increasing,
*  but the subsystem is locally over time giving and taking. Yeah, yeah. And it's so exciting to
*  talk about these things, because it's so hard in particle physics or cosmology to ask a question
*  that on the one hand, we don't know the answer to. But on the other hand, we can hope to find an
*  answer. Whereas in complex systems, there's all these questions we don't know the answer to,
*  they're pretty easy to hit on. Yeah, sometimes on a Monday morning, I'm really jealous of the other
*  of the other. What are we actually doing? The grass is always greener. I know. Yeah. Yes.
*  But the story you told about the power law in these attacks sounds robust enough with the
*  agglomeration and anticipation that it must be more widely applicable. Like what kinds of other
*  systems should we be thinking about? Well, when we went and looked online at the growth in support
*  for ISIS during 2014 2015, there the clusters are there, the communities online, and we found
*  a pretty perfect 2.5 power law. So because again, people are trying to connect together into
*  communities and occasionally that in that case, they were getting broken up by the social media
*  company by the moderator because it violated the turtles via, you know, discussing violence and
*  radicalism. So we've got again, that idea of coalescence and fragmentation. And so we
*  were able to show that you get exactly the same result of this 2.5 power loss. And in some sense,
*  we've that that that helps. It helps think about and frame what people do when they're trying to
*  fight against the system in some way. And so that gives you insight into property others. So
*  could we even take something like some of these other far right radical groups and do the same
*  thing? Well, that preliminary results suggest that that suggests that we can and that of course,
*  that then completely changes the way that you might think about mitigating the buildup online.
*  So most of the strategies of mitigation schemes that we see are coming from the social sciences,
*  they're very much detailed, very much focused on the bad actor, the bad apple, which is a little
*  bit like saying I'm going to stop water boiling by taking out the bad molecule.
*  That's a good analogy. Yes. Right. You know, okay, I'll take the one with the fastest velocity going
*  up, you know, perpendicular to the surface, because that's the one that may be most likely to get rid
*  of that one, there'll be another one. Right. And then there's another one. And so you really need
*  as physicists, we would never do who would imagine introductory physics, where we're going to discuss
*  every molecule in a glass of water before it boils, you'd never get anywhere and you'd be fired.
*  So so having a system view and saying, hey, as this extremist movement, whatever it is,
*  ISIS beyond the next version of it, which we hope it won't be, but you know, there will be extremes.
*  The next one, it will, whatever it is, it will be preceded by a buildup of clusters online,
*  that will form into a power law with a slope of 2.5. And the corollary that is when you begin to
*  see that happen, worry. Yeah. And so it completely changes the kind of focus of how you might go
*  around trying to detect concerns, you know, the kind of threats. Well, so you can even though
*  the slope might be universal, the hope is that nevertheless, there's a sort of a normalization,
*  right? Yes. There's more little ones than big ones, but still the absolute number is something
*  we can hope to increase or decrease. Yes. And it then becomes down to maybe that the world
*  will then need to turn to the physicists to help with deciding policy. I've been telling them,
*  but yeah, they don't they don't listen to me. But so so I just just want to drive this home,
*  because the story you told can seem frustrating if you think that, well, as soon as these clusters
*  grow big enough, we're imagining these are clusters of things we don't want to like,
*  you know, terrorist attacks or extremist groups or something. So they grow big enough,
*  and you can smash them and they disperse, but then they just re agglomerate again, right? I mean,
*  but you're not giving us just a sad story, you're giving us a strategy as well. Yeah, because,
*  and you just said it, they the big ones grow from the small ones, the big ones will probably be
*  harder to tackle, because they're robust, they're just they've got more eyes in, you know,
*  they're they're more aware of what's what's around, but they come from small ones. So maybe
*  there's a strike that immediately suggests like the sample analogy, to prevent the big avalanches,
*  avalanches in the sample, just just take care of the small ones, so that they don't build into big
*  ones, because the big ones need the small ones to build them. So one could imagine an alternative
*  strategy. And I'm not saying I mean, it's not as simple as that. But there's a kind of a systems
*  engineering, complex systems engineering, whereby you're not controlling. I mean, look, look at all
*  the issue with the social media companies that they seem to go out and get the bad, the bad actors,
*  bad influences online. Well, that's very hard to do. First of all, you got to find them. If they
*  even exist, if we're all on a spectrum of good to bad, which I, you know, maybe we could debate that,
*  but maybe maybe people are bad in certain moments, etc. Maybe that that's, first of all, you'd have
*  to find them. And then you'd have to stop being sued by them. If you tried to remove them, they
*  may be they're quite powerful people. And so they're going to turn around and or maybe they'll,
*  but then maybe they'll bite by you, by you removing them, that will create even more support for them.
*  So you don't want to, you know, so that it gets off into those types of issues. So is there a systems,
*  a complex systems engineering? I mean, I don't even know that there is no discipline of that yet,
*  really. But is there a way of engine kind of, you're kind of nudging the system in a way that then
*  doesn't impinge on one, one, one of these objects can't say, Hey, you targeted me,
*  you're more nudging the system. And that for me is that is that is the light at the end of the tunnel
*  of all of a lot of the systems that we worry about in society. It's more No, I think we're thinking
*  about them wrong. I think we should be thinking of kind of all that nudging, nudging that, that,
*  nudging the, and I don't know how we could say it, nudging the chemistry in it,
*  changing the chemical potential somehow, right? The sort of the background,
*  like that something like, you know, changing, maybe if I could just stop some of those smaller
*  clusters coalescing so fast, that would stop the flow through to the bigger ones, they would then
*  be isolated in some sense. So yeah, I think there's a lot of mileage there to be gained from
*  from the jump. And it's going to be an uncomfortable jump, but making that or building
*  that bridge from what we do in our academic studies of complex systems to the policy field.
*  And now I'm in DC, I actually have to say that I've had remarkably good feedback and interaction
*  with policy people here. I was pleasant, really pleasantly surprised. Well, I mean, we started by
*  saying that one of the interesting things about these complex systems is you have these individual
*  agents, and they nevertheless seem to have emergent collective behavior that was not given to them by
*  top down. And so in some sense, can we can we imagine the difficulties of these kinds of conflicts
*  coming from the fact that the bad actors are acting like individual agents, complex systems
*  coming together, whereas the white knights trying to combat them are more top down. I
*  remember reading something in something you did about how Facebook pages that were trying to give
*  good advice to people to fight the pandemic, were all kind of boring. And they said the same thing
*  over and over again, while the crazy ones said a million different things. So they were more likely
*  to hit someone in their sweet spot of vulnerability. Yeah, that's absolutely correct. And of course,
*  this hits the big, big challenge for anyone wants to work on complex systems now is the time,
*  because this the the number one complex system in my head now is the online ecology involving trust,
*  distrust of science, distrust of medical science mixed in with the growing resistance to
*  potential vaccines, misinformation, disinformation. That that that is the that is the that is the system
*  to, in my view, be be working on. And it's precisely as you just said that the it's almost like an
*  I mean, it's I don't mean it in a kind of political sense to call it an insurgency,
*  but you've got some kind of organic clustering going on, which in some sense is much stronger
*  than the top down, oh, go to this website to learn about vaccines. And because it's each one of these
*  clusters, in some sense, to some degree autonomous, it's, you know, they've each developed their own
*  flavors. And so giving them the Oh, here's the best vanilla ice cream in the world. It's like, no,
*  I don't want that. Actually, I like this other play. I, you know, I don't I'm not interested in
*  that. Oh, no, we see this actually on the in the online clusters, the communities in Facebook, and
*  you know, we study this a lot, we study across platforms, the clusters that form, and their
*  interconnections and how they evolve over time. We see this that they're they're talking about
*  effectively strawberry strawberry ice cream that they love it, or they're talking really to put it
*  in concrete terms, they're talking about some of them and out, you know, some of them may be
*  talking about, well, there'll be no safety, there's no five years of safety for the COVID vaccine.
*  And they're that's actually, they're absolutely right. And then suddenly at the top appears where
*  they had these lovely pictures of a baby's hand and you look at something they're talking about,
*  you know, his parents who love their kids, parents love their kids. So it's a wonderful,
*  they have a wonderful message. But then there's suddenly a banner appears at the top from, you
*  know, Facebook's CDC saying, Oh, we know effectively, if you want to know about vaccines,
*  go to this website. And it just it's, it's like parents coming into the room. Yeah. You know,
*  when you're trying to develop some kind of don't do this, do that. So now you're not addressing
*  the flavor of this cluster. So yeah, we're studying that a lot now. Well, there's the famous story
*  I've heard attributed to John Wheeler, but it could be somebody else or it could just be completely
*  apocryphal about, you know, physicists always get crackpot theories in the mail. And this
*  physicist who might have been Wheeler had the strategy of putting the crackpots in touch with
*  each other so that they could, you know, you know, talk to each other. But they always came back to
*  him and said, like, why are you putting that person in touch with me? He's a crackpot. Just
*  because you're a crackpot doesn't mean you're sympathetic to other crackpots, right? So there's
*  many different ways to be wrong in this particular thing. But that actually helps the wrongness grow
*  in some sense, because there's there's so many different buttons to push.
*  It does. And that's what we saw with our, you know, the why the support for ISIS grew so quickly,
*  it wasn't that it was, there was some coherent message between them all, it's just that what
*  they were opposing was such an obvious, it was such an obvious target. And so you could oppose
*  it in many, many ways. It's like, you know, in a two spin system, it's not that you were the opposite
*  spin, you could also be any roads, you know, any angle within the plane is there was a so it didn't
*  really matter, you were opposing the main message, and the main message was bad. So you were, you
*  know, the you allied by that we see it with the far right, the hate the online hate as well,
*  they often disagree, some of them will, these far right groups, one of them will want to united
*  Europe, the other wants to break it up and live in tribes in the caves. And yet, that never gets
*  played out, because they're both opposing the things that they rail against. I have to ask,
*  certainly the the way that you suggest thinking about the spread of the misinformation is
*  remarkably analogous to the spread of the actual physical virus that gets from person to person,
*  you know, is that correct? How good is that analogy? Is it more or less the same kind of thing?
*  Or are there like secret differences that make all the difference?
*  There's a fantastic, that is a fantastic question. I just came off last week of the back of the
*  World Health Organization's first conference, I was doing the leading the one of the science teams
*  first conference on info demy ology, I never heard of that word. And they told me, well,
*  you've never heard of it, because it didn't exist. They put together their earlier claim that the
*  online misinformation was like an info DEMIC, which we know which that that was a few months ago,
*  with the idea of, hey, maybe we should be there for thinking of an info demy ology, to think about
*  the online world. But there are a few important differences. Number one is that I can sneeze on
*  one place, and somebody catches the cold or whatever, on the other side of the, on the other
*  side of the planet instantly, because it's online. So the notion of distance, what does it mean to
*  social distance online, that's certainly not a strategy. Yeah, yes. So certainly, that's
*  not a strategy. But there are strategies of one thing, we've we've just finished a piece of work
*  we've tried, we tried to calculate that a lot of governments managed to seemingly managed to
*  handle the situation talking about the R number, which is basically the number of people, if you're
*  if you're infected, how many people are you going to infect before you recover? Because if you
*  infect another one, and then you recover, well, you just you're just propagating the same situation,
*  if you infect more than one, you're you're the things that expanding, if you infect less than one,
*  which you know, probabilistically, you could, then it's going to die out in time. So this R number,
*  whether it's bigger than one or less than one is an important number. But interestingly, it is,
*  it's calculated for in a very many ways, a kind of ad hoc way in the epidemiology literature,
*  so the idea is, wait, because one of the reasons is that they just don't know the network that
*  people are in. And you know, people are in networks all the time, and they may be in a social network,
*  and yet never meet the person there, you know, not meet them for five days or something. So
*  in a way, they're forced to think about epidemiology is forced to think about disease
*  propagation, again, like a test tube, I stick in a test tube, susceptible people, and a couple of
*  infected, they gradually become infected, infected, and then they recover. And so I've got that
*  reaction problem. And so that's how you tend to define the R number mathematically, and all these,
*  the model and the science that we always hear about on in the in government updates. But what
*  does that become in the online world? Because in the online world, we have, although you can instantly
*  infect someone on the other side of the planet. There are different universes, in the sense of
*  Facebook is its own universe, but it has no interaction commercially with something like
*  gab, which is another social media platform, or with 4chan, which is quite a,
*  um, it's quite an infamous, you know, it's a relatively free and on unregulated platform,
*  there's separate universes, and yet, people tunnel between them. So if I mean, I literally think of
*  this as universes, with some kind of wormhole between them that people can go through across
*  space. And unfortunately, because there are recorded, you know, because a lot of the postings,
*  you can pull them up from so called time machine, you know, cash pages, it's almost like across time
*  as well. So, so postings come across time and space. So it's almost like a wormhole, you have
*  to excuse me on this one, but it's, it is like a wormhole. And that that and that these universes
*  therefore are connected in some some, it's almost like some kind of multiverse. So in a way, it's
*  again, of course, I'm biased, but it's a perfect place for physicists to jump in and think, well,
*  I, I like to think about multiverses, I like to think about universes, I like to think about
*  couplings, and these wormholes can come and go, because they get shut down, and sometimes they
*  get opened up again. But they're very real things. And so you've got a spreading phenomenon in that
*  multiply connected space, which is interesting. Very interesting. Yeah.
*  Is it? So but I don't know if physicists would be good at this, because I mean, we we gab about
*  wormholes, but usually we like talking about smooth space times. I think that's a that's,
*  that's our comfort zone, we should be better at talking about these these sort of fractally
*  connected places. Yes, you're absolutely right. So it does become a kind of spreading in some kind of
*  fractally connected spaces, exactly as you said, and what is being spread isn't as clean as just
*  a virus and no virus. Yeah, it's mutating. It's there are multiple versions of it. And so I think
*  it's an app, it's a fascinating challenge, this infodemiology, and it's going to become huge,
*  because as we get more, you know, some of these vaccines come on, I mean, already, the rumors
*  around some of these vaccines are just remarkable. And there are many of them. And who knows, it's
*  impossible that they all go well, some of them will go very well. And that's just science, that's the
*  way it goes. But the opportunity for missing disinformation is absolutely huge. So I think
*  there's a I mean, just putting on the science hat for a moment. That's a fascinating problem.
*  Right. So the science hat as opposed to like the moral or, you know, policy hat, which is which is,
*  it can be frustrating.
*  Which has to be absolutely freaking out.
*  Well, okay, so for one last little freak out, just to close things, I'll get to one of my
*  favorite issues here, which is, what are the implications of these kinds of ideas for the
*  very functioning of democracy itself? Right? There's this idea that we need an informed
*  populace. But the very notion of what it meant to be informed was different 200 years ago than it
*  is now. I mean, are we gonna have to rethink what it means to be a citizen of a democratic
*  society? Or is it even a challenge to the idea if people can sort of fall into these
*  local minima of crazy misinformation, and that's never going to go away?
*  Yeah, that's a fantastic, absolutely important and fantastic question. I do see this,
*  um, this issue, I don't think science has ever had a situation whereby it's being done in real time.
*  And the whole world is on top of every preprint, and every kind of misstep and discussing with,
*  I mean, imagine any of our own, any of us in doing our own bit of science, if suddenly every
*  preprint you wrote was hauled over, you know, and then, you know, discussed in Facebook,
*  you know, kind of online communities, and the limitations section was just expanded into some
*  kind of list of problems with science. To be fair, it is better than being ignored, right?
*  Well, that's an interesting question to answer. I wonder sometimes, but the idea
*  that trust in science and the science, science, if we all know this, if any science, if there was no,
*  if there were no, if there were no unknowns in science, we wouldn't have a job.
*  So science is full of unknowns, but how to stop that being perceived as uncertainty in science
*  is, I think, a huge challenge. And so I actually think that that, I'm biased again, but I actually
*  think that is the core of what's going to go ahead in, I think democracy, I'm not a political expert
*  in any way, but I do think that science is a key driver. And I think trust in science is something
*  that is absolutely central to this going forward. And people need to somehow the public,
*  when a pub, when a pub, when, when are we all, we're members of the public, when are we all going
*  to trust politicians? Well, maybe never, you know, maybe some of them one day, some of them, but
*  science, science is sort of like, yeah, the breadth of, okay, we understand that they're trying to get
*  the answers, we understand that they may not always have the answers, we have that kind of level of
*  trust, I think is absolutely key going forward. And I think it underlies all these other issues,
*  because as soon as you start losing trust in science, you start just, who can you trust?
*  Who can you then trust? I mean, you know, we all love members of our family, I have members of my
*  family who've given me advice on COVID that I would probably be six feet under if I took it.
*  Yeah. I love them. However, I don't trust them on the science. Well, I need to trust.
*  You know, I think this is a genuinely subtle, sticky, difficult problem. Because I mean,
*  obviously, yes, I would love people to trust science more than they do. On the other hand,
*  there's two other hands. One is that science is the paradigmatic bottom up thing, right? Where
*  there's no pope of science who tells us what the truth is. There's people who disagree with each
*  other and fight and they battle and try to agree. So when you say trust science, it's not clear who
*  you're trusting. And the other is that even scientists are biased and wrong sometimes too,
*  so the trust can't be even absolute. So I'm torn about this. I want more trust, but not absolute
*  trust. Yeah, no, you're absolutely right. And you know, and I know that, you know, if we took
*  members of, you know, people saw what goes on in conferences, the arguing in the corridors and the,
*  you know, the backstabbing in terms of, you know, your theory, my theory, etc. But that,
*  so when I mean trust in science, I do not mean trust in one particular result in science.
*  Right, exactly. I mean, trust in the process. And so just as democracy is a process, and we don't
*  have to necessarily trust one thing or another, I think trust in, trust in science, you know,
*  it's not the result of any particular paper, it's the actual process. And so this idea that
*  you could go to a conference and there'll be people, we've seen it, we've all seen it,
*  shouting in the halls at each other and, you know, kind of like, almost like separate groups in
*  particle theory, you know, that one even talk to each other. And we know, we know these,
*  we know these stories. In the same department. In the same department. But that's probably
*  necessary. That's how humans do it. You know, it's the crowd and the anti crowd. Together,
*  they make the system. That's right. The thing we should have trust in is that emergent process
*  that, yes, in the long term anyway, we're allowed to critique it in the middle term. But in the long
*  term, we think that we're aiming in a good direction, scientifically speaking. Correct.
*  Correct. Well, that gives us some hope. I always like to I always tell my guests, I like to end on
*  an optimistic note. And that sounds like an optimistic note to me after you've given us some
*  some more sobering things to think about. So, Neil Johnson, thanks so much for being on the
*  Mindscape Podcast. Thank you so much. This was great. Thank you so much. Thank you. It's been a
*  pleasure. Thank you.

---
Date Generated: June 09, 2024
Transcription Model: whisper medium 20231117
Length: 4605s
Video Keywords: []
Video Views: 6675
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll

You might think that human beings, exhausted by competing for resources and rewards in the real world, would take it easy and stick to cooperation in their spare time. But no; we are fascinated by competition, and invent games and sports to create artificial competition just for fun. These competitions turn out to be wonderful laboratories for exploring concepts like optimization, resource allocation, strategy, and human psychology. Today’s guest, Daryl Morey, is a world leader in thinking analytically about sports, as well as the relationship between impersonal data and the vagaries of human behavior. He’s currently an executive in charge of the Philadelphia 76ers, but I promise you don’t need to be a fan of the Sixers or of basketball or of sports in general to enjoy this wide-ranging conversation.

Daryl Morey received a bachelor’s in computer science from Northwestern University, and an MBA from the MIT Sloan School of Management. He served as general manager for the Houston Rockets from 2007 to 2020, and since November 2020 has been the President for Basketball Operations for the Philadelphia 76ers. He is founder and co-chair of the annual MIT Sloan Sports Analytics Conference. He was voted NBA Executive of the Year in 2018.

Blog post with audio player, show notes, and transcript:https://www.preposterousuniverse.com/podcast/2021/03/15/138-daryl-morey-on-analytics-psychology-and-basketball/

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x

#podcast #ideas #science #philosophy #culture
---

# Mindscape 138 | Daryl Morey on Analytics, Psychology, and Basketball
**Mindscape Podcast:** [March 15, 2021](https://www.youtube.com/watch?v=F-59csm2kDM)
*  Hello everyone and welcome to the Mindscape Podcast. I'm your host Sean Carroll.
*  And as long-time listeners know, I'm a physicist, theoretical physicist. I have certain other interests, intellectually, academically, so forth.
*  But I also have, you know, my personal hobbies and my individual enthusiasms.
*  I try not to force my individual enthusiasms on the Mindscape audience too much.
*  Sometimes it leaks through. We get the occasional jazz musician or poker player. But mostly we're talking about academic type things.
*  Today, one of the times when we're going to take a little bit of a detour, we're going to be talking about basketball and the National Basketball Association, the highest level of basketball being played out there.
*  But I think this is a special case. If there is one person you would want to talk to about the idea of modern basketball to an audience or with an audience that was intellectually and analytically inclusive,
*  and intellectually inclined, but not necessarily full of basketball fans, it would be today's guests.
*  Darrell Morey is the general manager of the Philadelphia 76ers. Now coincidentally, the Philadelphia 76ers are the best basketball team in the world.
*  I could say this very objectively. It's not just because I grew up in Philadelphia watching Dr. J and Moses Malone and Mo Cheeks and Bobby Jones and so forth.
*  It's just because it's an objective fact. They don't always win. They're sort of at the top of the heap when it comes to one's favorite basketball team, if one is just objective about it.
*  But that's just a coincidence. Darrell was the general manager of the Houston Rockets for a long time. He just came to Philadelphia very recently.
*  The general manager, for those of you who don't know, is kind of like the boss of the basketball team.
*  He's the one who hires the coach, drafts the players, makes trades, signs, free agent, stuff like that.
*  The person who's ultimately responsible for assembling the basketball team.
*  And what's special about Darrell Morey is he, more than any other person, has been responsible for dragging the National Basketball Association into the modern data centered analytical age,
*  in terms of trying to understand what it means to build a team, to best position yourself to win games and win the championships.
*  So if it were just me talking to Darrell Morey for an hour without anyone listening in, I'd be very tempted to geek out about basketball or 76ers minutiae.
*  You know, should we try to land a stretch four or is it more important to prioritize perimeter creation, things like this? Who are you targeting in the trade market?
*  I like it, but I put that aside. I put aside my impulses to do that for the greater good of the Mindscape audience.
*  And instead, what we're talking about today is the theory of being a general manager.
*  OK, and I think that whether or not you care at all about basketball, this is an idea that has much broader application.
*  There's no basketball knowledge or interest required.
*  But what we'll be talking about is a combination of science, art and human relations.
*  If you're a general manager of a basketball team, you have an extremely quantifiable goal.
*  You want to win games and ultimately win championships.
*  You know whether you have succeeded or not in ways that are highly quantifiable, as I said, much more clear cut than in many other areas of human endeavor.
*  And you also have resources, abilities that are very quantifiable.
*  You have players. They can score. They do score at a certain rate.
*  They can pass. They can rebound. They can play defense, etc.
*  Then the question becomes, how do you optimize? How do you give in your resources, combine them together?
*  There's a salary cap in the NBA, so you can only pay your players so much you can't just outbid everyone else for the best players in the league.
*  What are the data that you need to take into consideration?
*  What are the data you should ignore? What are the things you should not care too much about?
*  How do you both correct for the biases that human beings inevitably have, but also recognize that human beings do have some intuitive knowledge of things sometimes, right?
*  There really is human insight that needs to be taken into account.
*  What about not just the players ability to pass and score, but also their ability to mix, right?
*  Their personalities. Do you need a leader? Do you want focal players?
*  Can you put up with the superstar who is kind of grumpy? Stuff like that.
*  Okay, so to me, this kind of much like poker in some sense, what we have here is a toy model.
*  What we have here is a paradigm for all sorts of optimization problems that we face in the everyday world, one where the answers ultimately are very clear cut, whether you have succeeded or not.
*  Darrell Morey is someone who succeeded a great deal over his years as a general manager in Houston.
*  They compiled the second best overall record in the NBA, second only to the San Antonio Spurs.
*  Congratulations to them.
*  And currently, as I record this intro, the Sixers are the first place team in the Eastern Conference of the NBA.
*  So we'll see how that goes. You know, who knows what happens as the future trundles on injuries.
*  All sorts of crazy things can happen in a sport like this.
*  You don't need to know anything about basketball or the Sixers or the current state of the NBA.
*  We will mention Joelle Embiid, center for the Philadelphia 76ers, currently an MVP candidate.
*  Also Ben Simmons, point guard for the Sixers, another all-star, and Doc Rivers, of course, who coaches the 76ers.
*  But you don't need to know any of that stuff.
*  The concepts we're talking about are much more general.
*  And in the end, just in case you want a little bit of physics in your life, we talk about dark matter.
*  I think that one of the reasons why Darrell took time out of his busy schedule to be on the Mindscape podcast is because he wanted to talk about dark matter.
*  He was skeptical that dark matter really exists. I gave him my sales pitch for why it does.
*  We'll see whether or not that convinced him, whether it convinces you. Let's go.
*  Darrell Morey, welcome to the Mindscape podcast.
*  Thanks for having me on, Sean. Appreciate it.
*  So this is unusual. We'd like to have some people on the podcast who are not PhDs and professors and things.
*  So this is a wonderful addition to that tradition.
*  But not many of our or many of our audience members will not be the rabid Philadelphia 76ers fan that I am growing up, you know, worshiping Julius Irving and so forth.
*  So why don't we start very, very basic? What do you do?
*  What is the day in the life of a general manager like?
*  Are you just on the phone all the time talking about trades with other general managers?
*  Or what is the day to day?
*  Well, it's like most things as you move higher up, you just become more of a tax on the system.
*  That's how I look at it.
*  But yeah, I mean, I started out as a computer science programmer way back when and got into basketball in 2002.
*  I always played basketball, but I got into the Boston Celtics and the NBA in 2002.
*  Sorry to hear that.
*  And I started off doing data and coding.
*  And, you know, now I get to do very little of that except, you know, run the teams that do that.
*  And yeah, as I go on, more of my time is on the phone and meeting, you know, players and coaches and owners and fans and business people.
*  And, you know, as you get higher up, you end up just talking more.
*  It's like being a department chair or president of university, you know, who have to do.
*  Presumably you don't have to do fundraising, but there is fan outreach, I presume.
*  Yeah. In fact, to the point where I'm sure you might be like this, Sean, where you just when I get to do some stuff from digging into data and solving a problem, I get so excited.
*  Oh, yeah.
*  And then my poor staff is like, well, just let us do it.
*  Leave us alone.
*  You know, so I try to do that because that's how I would be if I were them.
*  Well, you know, and presumably the landscape has changed a little bit since nowadays people can have a video game where they play at being the general manager.
*  Right. So like everyone is an amateur who's going to give you advice on your job.
*  I'm sure that's that's the right.
*  And I'd be you'd be shocked.
*  Like the amateurs are very sophisticated.
*  I think that's true in a lot of fields.
*  Like there's there's, you know, just die hard to know the team, know the data, know everything.
*  You know, there's a rights to Ricky Sanchez podcast with a couple diehards who are very smart.
*  There's, you know, message boards.
*  That's when every team has a guest on the rights to Ricky Sanchez.
*  I've appeared on the podcast before you did.
*  Yeah. Oh, wow.
*  So you're a pioneer.
*  You were pro.
*  So I was hoping I could be maybe one of the smarter ones on the podcast.
*  But now I've been I've been usurped for sure by you and Joel.
*  Joel's been on.
*  He's so well, shockingly smart.
*  It'd be great to have you.
*  He's like, I mean, I shouldn't say shocking.
*  That sounds bad, but he's he's like, you know, just end.
*  He's a polymath.
*  Is that the word?
*  Like he's he's really smart about a lot of things and on the court as well.
*  Right. This is Joel Embiid.
*  We're talking about obviously the Philadelphia 76ers Star Center.
*  I mean, it is interesting because some people and I completely agree that my
*  impression of Joel is that he's super duper smart.
*  But you know, but he doesn't project that way.
*  Right. Like he doesn't put on affectation.
*  I think that actually minute bowl was someone who was like that a previous
*  Philadelphia 76ers center.
*  Everyone used to say when they talked to him, how smart he was.
*  I've I've heard that about minute.
*  I mean, there's some I mean, I've known lots of smart players firsthand like
*  Shane Badier, but then you have like Chris Bosch is like was a coder.
*  Sam Dallam-Bear was like building his own machines when before that was a thing.
*  So, I mean, the thing is like if you make it to the top of your sport, whether it
*  be player or whatever, you usually are pretty good on G.
*  Like you usually usually have pretty good pattern matching to make it that far.
*  Yeah, there's a lot of tall people out there.
*  Some people tall people, but you need more than just that.
*  So so your goal, I mean, how would you say that your goal is as the general
*  manager? Obviously, you want to win the championship every year, but maybe
*  that's not plausible.
*  Do you do you sort of optimize to get a chance to win a championship or long
*  term success?
*  And of course, there's always a danger of being fired.
*  It's the real world.
*  How do you think about what your job is?
*  Yeah, it's exactly the right question.
*  I would say, yeah, I'd say so.
*  So the first thing you do is it's like organisms.
*  You have to survive.
*  So you're right.
*  Like whether it's right or wrong, I would say most people and I for sure focused
*  on this early in my career a little less.
*  So later, which is nice, try to like just make it to the next year like to and
*  hopefully you can always align your girls with the organization.
*  But in terms of thinking about what we're optimizing, it's pretty owner
*  dependent.
*  You know, I've been lucky.
*  I've always had owners who are like just championship or bus like that is your
*  goal.
*  But even within that, to your point, if you just focus on winning in one year,
*  you'll you'll create all these weird skews.
*  So we look over about a three year window and we're trying to optimize our
*  championship probability over that three year window.
*  And we use a lot of outside measures to we have internal measures and outside
*  measures.
*  Like right now, Vegas, I think, has a like about a six percent chance to win
*  the title.
*  And that sounds like really small, but it turns out to be pretty high.
*  That's I think that's fifth or sixth.
*  Yeah.
*  OK.
*  And you personally, where do you put your your chances?
*  Yeah, we have them internally higher, but that that's true almost always.
*  Right.
*  So whatever process you have, whatever team you are, if you don't think you
*  have a higher chance than Vegas, then that means you're not actually following
*  any sort of proprietary process.
*  The reality is, though, everyone can't be right.
*  So you need these outside objective measures to keep you grounded.
*  And so if you differ a lot from Vegas and Vegas has become pretty sophisticated
*  with how well they measure things, you know, football has always been the most
*  efficient basketball has become very efficient over the last 10 years.
*  If you if you differ in a big way, that means you probably need to look at your
*  own stuff.
*  Like, it's pretty hard to get a huge edge on Vegas.
*  Dan, just to give the listeners who are not basketball fans a feeling for this,
*  there's one little anecdote that I read that I thought was hilarious.
*  Serhi Lysuk, the best Ukrainian basketball player.
*  Remember his name?
*  Yes, Sergey Lysuk.
*  Yeah, I think I mean, honestly, you probably said it right.
*  We always call him Sergey Lysuk.
*  So the thing I read was he was drafted by the Memphis Grizzlies in 2004.
*  And again, for those who don't know, you draft the rights to a player, you may or
*  may not sign them to a contract, and then you can trade the rights to sign that
*  person to someone else.
*  That's why the Rights to Ricky Sanchez podcast has that funny name.
*  So apparently you personally are responsible for trading the rights to
*  Sergey Lysuk five different times, either trading for him or trading him away.
*  He's never played in the NBA.
*  He's already retired.
*  He never will.
*  Yeah, just for the audience, it's sort of interesting.
*  So the NBA draft is this sort of weird system that doesn't really exist in many
*  other places.
*  And what it is is that, Sean, you have been in the NBA draft and really everyone
*  listening at one point, male or female, has been in the NBA draft at age 22, the
*  year you turn 22, you're in the draft and you don't have to declare anything.
*  You just have to be 22.
*  If you happen to be selected by a team, they obviously can't force you to play for
*  the team.
*  You have to come to a contractual agreement and are generally prearranged,
*  depending on where you're picked.
*  And often those players either aren't good enough.
*  So the team never offers a contract or the player doesn't want to come, which has
*  happened in the case of players like Sergio Yol, who we drafted in Houston.
*  And so, yeah, long story short, you can hold these options of players to come and
*  they have options always have some sort of value, depending on the variance and the
*  underlying asset.
*  And they get traded a lot, mostly because a lot of it's because the NBA doesn't
*  understand that there are negative numbers in the world.
*  No, I'm actually serious.
*  Yeah, no, I get it.
*  And to be fair to the NBA, this is a legal thing, apparently, too, that in a lot of
*  contract law, they don't understand that there are things called negative assets.
*  So even though a team might be trading a positive and a negative asset together to
*  a team, such that it's neutral, such that they'll just take it together and they
*  don't need to send anything back, the NBA forces you to send something back.
*  And so often these options become just the word you write such that the trade is
*  legal, even though it doesn't make any sense.
*  And if I understand correctly, a negative asset isn't just a basketball player who
*  is so bad they make you lose.
*  It's that maybe you're contracted to pay them more than they're worth.
*  100%.
*  Right. Yeah, exactly right.
*  And to your point on everyone being GM, everyone gets this now because 2K, for
*  example, is like I think one of the top 10 most popular games in the world and no
*  one actually plays it.
*  No one plays the game.
*  The gameplay is how the game was created.
*  But now it's like more than half of the time spent on it is just playing GM and
*  simulating the games and not actually playing them.
*  So, yeah, everyone everyone's a GM and which is cool.
*  I mean, I think it's just part of being a fan of a team now.
*  Yeah, absolutely.
*  All right.
*  So moving into a little bit more of the nitty gritty.
*  I mean, the thing one has to talk about when you have Darrell Morey on the podcast is
*  when you're evaluating players, there has been a seismic shift over the years from
*  listening to the wise counsel of scouts who have been looking at these players and
*  developing their personal opinions to a more statistical database approach.
*  And you have a lot to do with that.
*  I mean, what's your big picture overview of where that came from and how it's going?
*  Yeah. And so I think my job is just it's really the same as Red Auerbach, who's a
*  famous GM for the Celtics for many years, is help your team win and make good
*  decisions on your three levers, draft, trade and free agency.
*  And how do you and so my job is the decision making job is more than anything
*  else. And how do you create a consistent edge there?
*  And it's by studying decision science.
*  And so if you study decision science, you'll see there's been a lot of research over
*  the last 30 years, especially on, you know, how, you know, behavioral economics is a
*  big one on all the different cognitive biases, anchoring, endowment effect, all
*  those things. Then there's a huge set of research on combining data and human
*  judgment to make a decision.
*  So we try to employ all those methods to create an edge.
*  And honestly, what we're trying to generate is a three to five percent edge, which
*  again doesn't sound like a lot, but over time compounds basically.
*  And so that and so we use a lot of data.
*  And with Scouts, for example, we you know, we look at it as what is a Scouts
*  experience? It's a very good set of data built up over 20, 30 years of players.
*  And the patterns of the players that succeed that are all in their head and humans
*  are actually really good at this. They're really good at finding patterns.
*  They're often very too good at finding patterns.
*  And that's often where data comes in.
*  So data like grounds you just like I said, look at Vegas and compare it to your own
*  models at all time. If a Scout or myself is very far afield from the general
*  consensus, could be right. But you want to like ask the questions.
*  Why do you think he's that much better than dig into each thing?
*  So data like actually forces you to ask the questions to make your decisions more
*  precise, essentially. So that's I don't know if that's a summary that helps.
*  Hopefully. Yeah, it does.
*  I mean, it raises the question, do you do longitudinal analysis of the success of
*  Scouts like are some Scouts really, really good at finding the diamonds in the
*  rough? So we do.
*  It's tricky, though, because you have an observer effect, which I would not not
*  the physics observer.
*  This is the this is the human observer effect, which is, you know, as you as you
*  measure people, they definitely change their behavior.
*  So I tend to be a little more of a hands off.
*  I don't try and you use the right word longitudinal look over a very long period
*  of who's successful and who isn't.
*  The problem is we have a big windowing problem.
*  So by the time you might have a sense that someone's three percent better or
*  two percent worse, you know, it's it takes like 12 years.
*  It's tough. So a lot of it, you have to use your own human intuition of who you
*  think are maybe better or worse Scouts, better or worse decision makers.
*  It's it's I wish it was all science.
*  It's not. It's art and science like most things in a man's kind of fun, though.
*  If you have 30 minutes free, you never have to worry about a break in at your
*  home ever again.
*  That's how quick and easy it is to set up a security system from simply safe.
*  It's the kind of thing that's so easy to do.
*  You can do it during a Netflix binge, watching a game or listening to a certain
*  podcast.
*  I have a simply safe system myself.
*  And look, I'm a theoretical physicist.
*  Setting up electronic systems is actually not close to my core competency, but I
*  had no trouble putting together the simply safe system.
*  You can choose exactly the sensors you need, video cameras, motion detectors,
*  window sensors, et cetera.
*  And you can program those motion detectors to not detect your pets, which is
*  crucially important here at Mindscape World headquarters.
*  It's easy to assume that everyone in your house already feels safe, but they might
*  not. And it's worthwhile to talk about it.
*  Simply safe is a small, easy step to make sure everyone feels safe at your home.
*  So go to simply safe dot com slash mindscape today to customize your system and
*  get a free security camera.
*  You also get a 60 day risk free trial.
*  So there's nothing to lose.
*  That's S I M P L I S A F E dot com slash mindscape.
*  And when it just comes to the players, I mean, there's been not only increased
*  understanding that the statistics are useful, but the kinds of statistics that we
*  have. Right.
*  I mean, we used to keep track of how many points, how many rebounds, how many
*  assists a player would have these days.
*  I mean, again, you're the expert.
*  I'll let you say it, but we are we collect an enormous amount of data, not only at
*  all different levels, but in the arena, there's cameras keeping track of
*  everything.
*  How many with the average speed?
*  What's probably what the variance of the speed of a player on the court is, how
*  many miles they go the whole bit.
*  Yeah, it's your point.
*  Like in a lot of fields now, there's no there's no lack of data.
*  It's really you have more of a lack of an imagination or how to analyze the data.
*  But so we have data from the NBA all the way down to like second, third division,
*  Germany, that kind of a level and and college and some high school of every play
*  that's happening around the world.
*  Right.
*  And to your point, the NBA we have and and in the D League and then probably
*  coming to college soon to a few areas in college already 25 times a second in
*  three dimensions, the ball and all players on the floor.
*  So you're really only limited by your imagination.
*  If you want to know, was that shot open?
*  You can you can look that up.
*  And so, yeah, we spend.
*  So the problem isn't the data.
*  There's two ways we're trying to create an edge.
*  There's two ways to create an edge.
*  You have to have unique data and that's hard to come by, though we have some and
*  then or you have better analysts.
*  And that's also a hard one to have a consistent advantage in over time.
*  We used to have a huge advantage in Houston in my belief and I think sort of
*  born out by the fact we never had a losing season and had the second most wins
*  over the over the years that that all a lot of those edges have eroded.
*  And now it's like chasing.
*  It's it's it's similar to, you know, if you were a physicist in 1880, there's
*  probably a lot of stuff to do.
*  And there still is a lot of stuff to do, but it's harder.
*  It takes longer to get to the the unique nuggets now in physics, I would guess
*  than it did in 1880 when we didn't know relativity and a whole bunch of other
*  stuff.
*  So, yeah, so just to put it in context, when you became the GM of the Rockets
*  in Houston, not that many teams were devoted to this idea of collecting all
*  the data you can analyzing it.
*  And so you got to be out in front a little bit there.
*  And by now, everyone else has caught up more or less.
*  Yeah, absolutely.
*  Like in 2006, it was of course, people knew, but it was somewhat novel that
*  shooting three pointers and getting three points is better than shooting twos
*  and getting twos like that.
*  It seems pretty straightforward that you want to take a shot that's worth 50
*  percent more than the other one.
*  But it turned out not to be.
*  In fact, teams were actively avoiding those shots, mostly because of the human
*  and how that it was introduced.
*  It was introduced to the game after a lot of the models on how to win with two
*  pointers came out.
*  And because it was introduced late, everyone thought it was a gimmick and to be
*  avoided.
*  And all the people who were coaches and players at the time were like, ah, that's
*  a stupid gimmick.
*  But they didn't realize the power of it at the time.
*  And it took like 25, 30 years before people started using it correctly.
*  Well, that's absolutely true.
*  And it's a weird number.
*  Twenty five or 30 years is a long time.
*  And so to be fair, sure, three point shot is worth 50 percent more, but you miss
*  it more often.
*  And there's also like these confounding things that people believed.
*  I think it turned out not to be true, but they believed that your team was less
*  likely to get the rebound back after a three pointer.
*  So you kind of had to dig into it.
*  Yeah.
*  Correct.
*  There was a lot of reasonable objections that could have been true.
*  Just so happened that none of them were.
*  So, yeah, you could shoot them at a low enough percentage such that it's not
*  worth it. That turned out not.
*  It turns out people shoot eight foot shots at about the same percentage or
*  within a few percentage points of what they shoot.
*  Twenty five foot shots.
*  So that's a counterintuitive thing.
*  Like you wouldn't know that until you actually played.
*  I think it's intuitive to your point that people thought, yeah, you'd get
*  longer rebounds that the other team might get and turn in transition.
*  That turned out not to be true.
*  Now, of course, those happen, but they're just anecdotal.
*  They're very small relative to the whole set.
*  People thought maybe an open two pointer would be better than a fairly
*  challenged three pointer.
*  That also turned out to not be true.
*  So it just says you keep diving in.
*  It just turns out that 50 percent more is such a huge edge that that that it
*  was worth it's worth taking under most most conditions.
*  And, you know, people don't love that.
*  But I mean, the reality is that the three pointer if it was if we were in
*  Eastport, the three pointer would have been nerfed a while ago.
*  I mean, they would have changed it to be worth less.
*  It would have been worth two and a half or something like that.
*  Well, and also let's admit that there is an almost a macho component, right?
*  You know, a lot of people in and analyzing the sport were ex players
*  themselves. And there's a feeling that if you bully your way down under the
*  basket and slam dunk on someone, you've achieved more than if you've just
*  lofted a shot from 35 feet away.
*  That's very insightful. Yeah.
*  There I mean, any sport with men and that's true.
*  I mean, there's a competitiveness and aggressiveness that often gives you an
*  edge. But that edge can also be your weakness.
*  And it's absolutely true that like I always talk about this.
*  There are ways that fans and coaches and GMs are comfortable with losing and
*  there are ways that they're uncomfortable with losing.
*  So ways that people are very uncomfortable are losing like in football as if if
*  they could just run it down the middle every time get four yards and do that
*  every time and win.
*  That's an uncomfortable way to lose.
*  If a team, you know, makes a lot of long passes and they seem unlikely and do
*  then they're fine with it.
*  Usually similar in basketball.
*  If if on a given night you take a bunch of open 18 footers and happen to miss
*  them and lose, they're like, ah, wasn't your night.
*  But if if the other team like hosts you up and, you know, makes you look bad and
*  throws it one inch from the hoop.
*  Now, now it's like our to your point, it's a very insightful one.
*  Now it's like our our manhood is being challenged and that's not a good way to
*  lose.
*  And it's I think in any sport analyze the ways that you're allowed to lose and
*  not allowed to lose.
*  And you learn a lot about the culture of the sport.
*  So other than shooting for three points is even better than shooting for two
*  points.
*  Is there anything that we've learned from this ultra high resolution 25 frames a
*  second data about ball movement and things like that that is just that just
*  smacked you in the head.
*  You said, oh, my goodness, that's counterintuitive.
*  But now that we think of it, oh, my goodness.
*  Yeah, there's a lot on rebounding.
*  So to your point, a lot of the analysis on on rebounding in terms of there isn't
*  more long rebounds.
*  That that's a big one.
*  You know, there's a lot on that.
*  There's a trade off between obviously basketball is one of the coolest, most
*  dynamic sports.
*  Everyone plays offense and defense and it goes back and forth very rapidly.
*  I think that's one of the reasons why it's such a popular sport and so fun besides
*  athleticism.
*  And so there's this constant trade off between do you want to stop the other
*  team from running back at you and getting an easy basket in transition?
*  Or do you want to try and get an extra rebound?
*  It turns out that problem is really complicated and really can only be done
*  with overhead cameras because it's that you can't look at it in the macro.
*  You have to look at the marginal decisions of sending one more guy versus
*  sending another guy back.
*  Soccer is currently dealing with this issue as well, which is which is, you
*  know, one of my bugaboo is they pass back to the goalie, a super high risk
*  move or a fairly low upside.
*  But you can't like you can't use big data like, oh, let's just count how many
*  times you kick it backwards and see if that team wins or not.
*  The analogy I use there is if you took the best basketball team in the world,
*  let's say Golden State during their six year run of being the best team in the
*  world and every game, Steph Curry, after he got the tip, threw it out of bounds.
*  That was his first play of every game.
*  Well, it would be this like it's amazing that would correlate 100 percent with
*  winning because every game they do it.
*  They throw it straight out of bounds and they win every single game.
*  And so people teams should clearly follow this.
*  It works like it happens all the time.
*  So obviously I make a very similar, very simple correlation causation argument.
*  But it happens all the time.
*  People say, oh, the best teams don't often see rebound.
*  Well, that doesn't work.
*  But they'll say the best Premier League teams pass back to the goal.
*  Well, it tells you nothing.
*  It does you absolutely nothing.
*  And so until you get this better data, this over data in soccer and basketball,
*  you can't really make these decisions.
*  And do you go beyond the data of the players on the floor?
*  Like, is this are you an organization that keeps track of the players sleep
*  patterns and diet?
*  And does all that contribute to the data set?
*  Yeah, absolutely.
*  So it's been a, you know, we're every team's trying to find an edge wherever
*  they can sleep turns out to be this tremendous edge, but it's also a
*  tremendous one to gain a hard one to gain a consistent advantage.
*  You know, I think when you go down levels and you have more, you know,
*  you're at a college or the high school and you have more control, but these
*  are professionals.
*  These are adult adults playing the game.
*  We definitely work with them when they want to be, you know, when they want to
*  wear a sleep monitor and things like that, we do it.
*  But, but we also don't like, in fact, the CBA, not the CBA, but the players
*  union, you know, basically makes has rules on how much you can instrument
*  players both on the court and off.
*  And so you do your best to get them to understand the advantage of sleep by
*  showing them the data, which is actually overwhelming.
*  But it's, it's not something that we can force them into a pod in the wall
*  once the day is over.
*  Unfortunately, sadly, they still have, they still human rights, even though
*  they're NBA players.
*  I mean, maybe the last question on this sort of very data focused thing is
*  what is the actual sort of organizational way that it happens?
*  I mean, you have a team of people sitting in front of computers debating
*  about what to collect, how to analyze it, like related to the bigger big data
*  questions is a question that every field has these days.
*  Yeah, I mean, I think so I can just tell you how it is.
*  There could be a more optimal way to do it, but I can just say how we do it in
*  most teams.
*  So obviously things start with the owner.
*  Generally, there's my role, GM, and then there's the coach role.
*  And I think the best ones that I know doc does this and I know I do this, you
*  have like really capable people below you and you try to put them in an
*  environment where they're very comfortable disagreeing with you and
*  they're very comfortable.
*  They've they basically have a lot of experience and you're then you're like
*  the the gate function on a multi model or your you're basically saying, okay,
*  I'm going to wait.
*  I'm going to wait the opinions of people who have a history of being correct
*  to line up with the data, things like that.
*  And and so that's the mother is basically a coach down to multiple key
*  assistance.
*  This is true in most even other sports NFL, especially and then obviously,
*  you know, their their role is to get the the optimal performance out of players.
*  And then my role is to have, you know, scouts and data and programmers make
*  decisions on draft trade and free agency to get the best possible players for
*  doc and his crew to optimize.
*  So that's that's that's at least how how we structure things and has been
*  successful.
*  But for sure, I'm always open to new models.
*  So should we do a should we do a peer review process and have tenure for
*  certain?
*  Yeah, I mean, like you said, it's like takes 25 or 30 years to catch up to
*  something obvious.
*  And you said, analyzing the physics, which I thought was very, very
*  interesting, like where the breakthroughs are, presumably there are just as many
*  or nearly as many breakthroughs yet to be made.
*  We just haven't thought of them.
*  Right. And you must live in fear.
*  I know probably many physicists live in fear, like they're so close to finding
*  what the breakthrough is.
*  And then someone else comes up with it.
*  You're like, oh, yeah, I should have thought of that.
*  Yeah, we don't have a timing element.
*  Like if you're a fast follower like Microsoft, if you're the Microsoft of NBA
*  teams, you're probably OK.
*  If you see a team doing it, they have to put it on the floor.
*  Right.
*  And you can aggressively follow where you can get behind our development systems
*  of talent identification and helping them in the minor leagues, for example.
*  So there is where you can develop sort of a bigger longitudinal advantage.
*  But yeah, we think we don't have the physics thing where you could be working on
*  from that last theorem.
*  And then some guy at Princeton comes up with the proof only four people
*  understand all of a sudden and you're you know, your DOA.
*  Everyone lives in fear of being scooped in in science and academia.
*  But so do you go so far as to use artificial intelligence, machine learning
*  kinds of things like do you ask the computer, look for patterns that my
*  pitiful human brain is not up to finding?
*  Yeah. So the two big areas where you see that one one is with the overhead camera
*  data, they do automated recognition of like pick and rolls and different
*  isolations and different kind of actions that you have on the floor.
*  And the other one would be in draft models.
*  So those would be the two areas where you see I mean, I grew up in the
*  predictive modeling world.
*  That was my other area of study at Northwestern and then since.
*  And so if you do the if you do the other basically, it's all part of
*  predictive. I was very lucky to take a class with Jeff Hinton and Michael
*  Jordan in the 90s, which to this day, I'm like, I wish I had saved the binder
*  from it. It was like a 10 day 10 day course.
*  And the other Michael Jordan is not like the one you probably have the one we
*  know. Yeah. Yeah.
*  OK. So I don't I don't I don't know totally your fields of study, but yeah,
*  he's he's famous within the predictive modeling on the graphical model side.
*  And then Jeff Hinton, obviously on the neural network side.
*  And I still remember this day like they would like come in and say and and
*  Michael was basically crushing Jeff Hinton and saying like, your your neural
*  nets are just special versions of regression and useless.
*  And and Jeff was like, I just need more processing power.
*  And he was right. I think Jeff was more right than Michael, actually.
*  But yeah, I don't know. I just got off a whole tangent on that.
*  No, actually, I mean, it's fascinating because I am actually interested right
*  these days for various reasons and learning about that stuff myself.
*  The whole the predicting predictive modeling idea, as far as I can tell, is
*  here's a giant bucket of data, maybe a time stream or a series of many.
*  What's going to happen next? Right. What's the most efficient way of saying
*  what's going to happen next? A very tricky and intellectually fascinating
*  process, it turns out. Yeah.
*  So I worked at a company called Mitre with the NSA and CIA, and it was very
*  near to the Oklahoma City bombing.
*  And one of the projects I got when I was there was predicting the next
*  domestic terrorist act and using like purchases of fertilizer and messages
*  on message boards at the time.
*  There weren't there was no Twitter and stuff like that.
*  How do you how do you predict that that's coming?
*  It turns out to be an incredibly hard problem.
*  And anyone who's in predictive modeling will know this.
*  It's called the sunspot problem.
*  So if you try to build a model to predict something rare, unless you
*  accurately tune it, your model will get really good at predicting.
*  Nothing's going to happen.
*  It'll be it'll be like I'm pretty sure ninety nine point nine nine nine
*  percent. Nothing is about to happen.
*  And you and that but that's not the point.
*  You have to tune the reward function on these predictive modeling problems.
*  You have to tune it such that it's developing the output you want.
*  Draft picks are like this where you're generally in the draft looking for more
*  upside. So if you don't tune your models to look for players who have a lot of
*  upside, you'll get you'll get unfortunately you'll get something that's
*  good at predicting just a slightly above replacement player.
*  We all know time is precious and it's not meant to be used doing your
*  expenses.
*  Expensify is an easy to use app that makes it easy for you to get paid back.
*  Expensify is the most widely used expense management platform in the world
*  with over 10 million users.
*  And it's made for you, the users, not for finance office administrators.
*  Expensify makes it easy to manage your expenses, your bills, invoices, travel.
*  If you have any business or corporate card spending, it's all in one place so
*  you can focus your time elsewhere.
*  Get rid of all the paper.
*  Don't worry about losing your receipts.
*  Just take a picture and as soon as you get it, it's in your Expensify system.
*  Better yet, link your credit card and they will auto match the receipt to the
*  expense and submit the report for you automatically.
*  If you have to travel for work these days, there are lots of supported features
*  for the modern day traveler, such as automatic international currency
*  conversion, concierge for your travel needs, and mileage tracking.
*  So visit Expensify.com slash Mindscape to get started with a free trial.
*  That's Expensify.com slash Mindscape.
*  Right, and you're really looking for, because the NBA is a game where there's
*  only five players on the floor at any one time for your team, having the one
*  best player is an enormous advantage, I think a much bigger advantage than in
*  baseball, football, anything like that.
*  It's the largest advantage of any team sport by a good margin.
*  Even more than quarterback in football, that's the closest that is out there,
*  but I haven't studied for sure.
*  But the best analogy I give to that is in baseball, if you take the greatest
*  hitter of all time, which was probably Barry Bonds at his peak, and he goes up
*  to the plate to hit, and then he hits a home run or whatever, and he comes back,
*  and then he has to wait eight more times.
*  In the NBA, the Barry Bonds, the Joel Embiid, after he goes up and hits a home
*  run can be like, I'm still the best.
*  I will now go up to the plate again.
*  It's actually worse than that for some players.
*  Take a player like Ben Simmons, for example, who's on the perimeter.
*  A lot of teams now switch the ball screens.
*  Now I'm getting two inside basketball.
*  You can basically, your five are being guarded by another five pretty much all
*  game in different schemes, but mostly man in the NBA.
*  So someone's guarding Ben Simmons.
*  Let's say it's a good defender.
*  And what will happen is people will switch a ball screen, like a pick and roll,
*  and they can now almost choose who to guard them.
*  So Barry Bonds in basketball can not only choose to go up every time, but select
*  the pitcher on the other team he wants to go against.
*  And so you can imagine the edge that creates.
*  And we do it not 30, 40 times a game getting up to play.
*  We do it 100 times.
*  So there's a back and forth all game.
*  So your best players drive 90 percent of your value in basketball.
*  And but on the other side of that, I mean, maybe it's a tiny correction, but I
*  remember reading a study where there is a bit of game theory and mixed strategy
*  involved here, right?
*  Because if even if Joel Embiid is the most likely person to score on your team,
*  if the other team knew you were going to him literally 100 percent of the time,
*  they could scheme against that very, very effectively.
*  So you have to mix it up and you have to target your less good shooters some of
*  the time, right?
*  Absolutely.
*  There's definitely game theory.
*  That's what makes basketball fun.
*  I would say, though, it's a little overblown, the game theory.
*  So I call it the little low, the Luis Schola right hand problem.
*  So anyone who's a big basketball fan, Luis Schola was a big time player
*  international and a very good player in the NBA.
*  And he I mean, he may as well have been Jim Abbott and had one hand like one arm.
*  He was he was that amazing with his right hand.
*  And no matter how many times he faked with his left, he never shot with his left.
*  He'd come back to his right.
*  And I'm telling you, it would work 99 percent of the time.
*  So it's similar.
*  It's similar in basketball.
*  People like, OK, yeah, you know, you're going to Joel every time.
*  And that's that's too easy to stop.
*  Or you know, you're going to shoot a rim shutter three of those Susan stuff.
*  It turns out when you dig in and even adjust for all that, there's not as much game
*  theory there as you'd like.
*  I wish there was more game theory.
*  More fun. Yeah.
*  But Joel's actually made a huge step forward this year.
*  Teams are having to double.
*  He's having his best year in the paint by a good margin.
*  And you're right.
*  He has to be able to read and make the right passes.
*  And he's he's doing that.
*  Yeah, no, it's been fun to watch.
*  Jennifer, my wife, will testify that I've converted her into not just a basketball player fan,
*  but a 76ers fan so that we are able with league pass to watch a lot more games than we used to.
*  Yeah, he seems like a tough one to convert.
*  Oh, yeah. She's very happy to let me know when she is not interested in what we're doing.
*  But and we go to see the Sixers every time they play the Clippers here in L.A.
*  So that's also fun.
*  We just announced we're getting fans back in Philly.
*  Maybe L.A. will take a little longer.
*  We're 15 percent fans.
*  Yeah, well, L.A. is especially bad.
*  It's not a great place, but hopefully, hopefully we'll get vaccinated very, very soon.
*  Speaking of human beings and biases and decisions that they're making, you know, you talked about the fact that players are human beings.
*  It's absolutely true.
*  So are general managers and coaches and scouts and so forth.
*  And, you know, one of the interesting things I've heard you remark about in the past is how easy, easily it is that we are fooled as human beings.
*  And in particular, the thing that struck me is the uselessness of interviewing potential draft picks ahead of time.
*  So, yeah, so I think just if you just take a step back from even the NBA, I think interviews in general have been proven to be really poor relative to track record.
*  One of the nice things we have is we do have track record.
*  We have them in I would argue a different sport, college basketball.
*  It seems similar, but I think it's probably enough different that it makes it challenging and hard to to do.
*  And so I would say draft interviews are very, very similar.
*  We do our best to follow all the rules to try to make them useful.
*  But at least over the time I was in Houston, you could prove that our marginal ability to improve our prediction based on interviews was near zero.
*  And it probably was it probably was zero.
*  But I'm saying near zero to be safe and make myself not feel as bad about all the hours I spent.
*  I always felt like I had to do it because, you know, what if what if the guy can't talk?
*  You know, like it's just like there's just stuff that the other thing that comes up in draft interviews is it is a team.
*  And so, you know, getting along with other humans is important.
*  So if you can get any sense of that, but even that's hard.
*  And my general sense of why interviews are tough is we're generally interviewing 1920 21 year olds.
*  And if you think back to yourself at 1920 21, you probably didn't have much figured out.
*  So if we don't have if they don't have it figured out how we supposed to guess what they're going to want to do.
*  And I would say for sure the players change over time, mature, become better leaders, you know,
*  have a have a complete change in approach and personality that makes a big difference.
*  So it's very, very hard to predict.
*  And I think I read you mentioning that you were influenced by these ideas from Kahneman and Tversky about how we human beings.
*  So not just on the player's side trying to sell themselves, but on the interviewers side, we're very susceptible to signals that might not be relevant.
*  There's a lot of noise because we're programmed to pick out the wrong things.
*  We have all these biases. Well, I think it's a lot like a lot of things people want a skill in one area to map to another area.
*  You know, people want to think that being great at chess means you're good at other things.
*  And I think that's been pretty well proven to not be true.
*  And if you put a lot of weight in interviews, my sense is the research is pretty overwhelming now that what you'll get are people who are good at interviews,
*  which turns out to be not not very relevant necessarily to what whatever goal you're trying to achieve.
*  They're good at like social cues. They're good at mirroring.
*  They're good at they're good at like, you know, you know, saying things that are familiar, like even before we started the call, I was like, oh, you know, I grew up like this.
*  That's similar to you. I mean, that's just like a normal thing that people who are good at it do it.
*  And some of them don't even know they're good at it. Just like it's intuitive.
*  They're good at being around people. And that can be helpful that just knowing that can be a data point.
*  I mean, it makes me ask, have do you think that trying to become the best general manager you can possibly become has made you a better human being or has made you better at just social interaction with the world and analyzing things?
*  I hope I'm a better human being. I don't know.
*  I tried. I mean, you know, it's just it's a sort of a sport that we're not vaccinating people or saving lives.
*  I mean, I guess we're providing entertainment. But I do think most people get better, you know, working with people over time.
*  And I'm sure that's, you know, that's that's been myself as well.
*  I mean, the example I always use is that you would think that physicists who study the universe would eventually grow more humble over time.
*  But empirically, I don't see that actually happening. So so, yeah, maybe what do you expect to get?
*  What I've been shocked by physicists and you know, that's way better than me.
*  Maybe you'll disagree is they're just they're so susceptible to the same biases of what's the right one.
*  You know that their theories almost become like religion to them.
*  Yeah. And so even though they've been trained to be able to falsify their own work, right, you're literally trained to do that.
*  They're really bad about it. Like they it becomes part of their their identification of themselves versus a thing that's separate from them that they should be willing to read.
*  They should be well, like if you work in theory, if physicists were AI physicists, just machines and they worked all their lives on string theory,
*  and then someone comes along and invalidates that they should be able to be like, oh, great, we have this new thing.
*  It's better. I'm going to toss that out and move to the new thing.
*  And there are people who can do that. So I think some of the very unique physicists in history could do that.
*  But I would say most of them are human and have the same problems that anyone else has.
*  No, very, very much so. 100 percent.
*  And it reminds me I just did a podcast with Roderick Graham, who is a sociologist.
*  And mostly we were talking about, you know, race and how African-Americans are treated online.
*  And I mentioned that it's a hot button issue. And, you know, he said, oh, yeah, you probably as a physicist don't need to worry about this online.
*  And I'm like, no, actually, if I mentioned the multiverse or the ever interpretation of quantum mechanics, emotions grow very, very heated very, very quickly.
*  People do become both attached and anti attached to ideas.
*  And it is just part of being human. Yeah.
*  Well, it's also what drives them to make great discoveries.
*  So I think if we didn't have that, we probably would have not.
*  You know, you almost need like obsessive people doing things that are against their own interests to create some of the great discoveries.
*  Yeah, no, that's absolutely true.
*  But it's actually there's an interesting philosophy of science question here because I know great physicists who will articulate the idea that it is their job to be their theories biggest advocates.
*  And there are other people who think it's their job to be their theories biggest critics.
*  Right. Because, you know, they want they want their theory to be true and they want to be as harsh on it.
*  And I think that I can see both sides.
*  So I think that it's just good that we have different people coming from different attitudes because there's no right answer there.
*  That makes sense.
*  I would definitely be the biggest critic one.
*  I'm I'm a big falsified like I'm always looking for the next best thing.
*  I'm almost too ready to jump onto the next interesting thing like that.
*  I think people are just built differently.
*  And I hadn't thought about the two dichotomies, but you're right.
*  Both are valuable at at at different times for sure.
*  You know, and speaking of which, if we human beings are bundles of heuristic pattern recognizers, and that's a big disadvantage when we can be tricked by a clever interviewee, does it also give us some advantage?
*  Have you have you noticed there are things that a good scout or a good general manager can pick out that are just not visible there in the data?
*  Absolutely.
*  Yeah, we had.
*  Unfortunately, he just recently passed away.
*  We had a great scout named BJ and he he had an advantage.
*  He had a data advantage.
*  And then he got to see players when they were younger because he was part of like the youth basketball circuit a little more.
*  So he got to see them evolve.
*  And that gave him I think unique data, but he also had a unique intuition that certain guy like I ended up leaning on him.
*  For especially players who didn't have a big college track record because he just again, he might have just had better data sources than me.
*  Yeah, but he also had an intuitive feel.
*  I couldn't prove that to you, though, but I always felt like he did.
*  Is there is there is one of the data one of the biases you need to worry about overvaluing your own players?
*  I know that, you know, on the online discussion boards, we all think we would have trade our third string point guard for an all star from someone else's team and they would go for it.
*  But that sounds like something that you got to actively work to overcome, I would think.
*  Yeah, it's one of the major biases.
*  The endowment effects and anchoring are probably the two.
*  I would say probably the three biggest biases that really mess things up are endowment, anchoring and confirmation bias, which we've.
*  Everyone's learning about confirmation bias because of the recent political changes in the world.
*  Like in the fact that the media is dispersed.
*  But on endowment, yeah, to avoid endowment, which is overvaluing your own things.
*  Yeah, we just force ourselves to invert the trade.
*  It turns out to be really easy if you invert the trade.
*  Sometimes it's actually amazing.
*  You realize that you wouldn't.
*  While you're agonizing, whether you do a trade, you realize if you're on the other side, you wouldn't even like put this trade as one of the possible trades.
*  It's it's that ridiculous.
*  They are even thinking about it.
*  It turns out to happen all the time.
*  And you do have to fight it.
*  You have to.
*  You have to fight it a lot.
*  I mean, can you maybe give us a little bit of a context of what you're doing and what you're doing?
*  How does that go?
*  It depends on the time period.
*  So generally, like, there's a lot of constant conversation all the time.
*  And then it generally sort of bubbles up into the conversation.
*  And then you have to, you have to fight it a lot.
*  So, I mean, can you maybe give us a little insight into the anatomy of the negotiations for a trade?
*  So, you know, there's a lot of constant conversation all the time, and then it generally sort of bubbles up into more as you get closer to these key dates.
*  And just like with most negotiations, most of them don't happen until until there's a deadline.
*  It's like everything in life until you have a deadline.
*  The other bad about getting things done.
*  So, but in negotiations, there's actually a real reason why they run to the deadline, you know, which people could go read all that research.
*  But and so as you get closer, goes the deadline, things get more specific, things get more transactional, whereas prior to the deadline, it's more conversations, concepts, looking for high level fits.
*  And it's sort of it's like a it's almost like a sales funnel, honestly, if you're into if you're into that area of research.
*  So you have to have a lot of things in the funnel or you're going to end up with not much at the end.
*  And so teams are different styles.
*  Some teams go for home run deals like where you just are hoping you catch a team valuing asset very differently from you.
*  And and so you don't say much.
*  And and but it lowers your liquidity.
*  You lower your chance of making a deal.
*  Whereas I tend to be like, I would rather be more open, be more open with information and more open to try and get things done because it allows you to work on the margin.
*  So I'll miss like home run deals more often, but also hopefully get more done that, you know, help you do the last piece to a title team, for example.
*  I did try to time this interview so it would not be too close to the trade deadline.
*  I would I would never forgive myself if you were doing a podcast when you could have been swinging a massive deal.
*  Yeah, I don't think Spike and Michael would forgive you if they would if you distracted me during that.
*  We still have four weeks.
*  Twenty five. We have three weeks, three weeks and a couple of days.
*  We have time.
*  And but but you mentioned, you know, that there's the human side to being a GM also knowing that your players are players and there must be some people who you just like and want to have on your team.
*  And you might have a valuation of them.
*  And maybe that maybe that evaporates and becomes a little bit less important when you're close to the deadline.
*  But, you know, and also you want the people on your team to like each other, right, and to play well together.
*  And it seems to be the Sixers are having a good time this year and I think it's a big part of their success.
*  Yeah, Doc Rivers done an amazing job.
*  I think one thing you have to recognize if you're in my job is like you don't want people who are just like you.
*  Right. You want people are different.
*  Doc and I come from very different backgrounds, player versus not, you know, coach versus.
*  But, you know, I've come to I really I've worked with them before in Boston.
*  I really appreciate he does such a good job with, you know, getting everyone in the same canoe and rowing all together and that feeling of attack like we all know we're having to win the title, but there are different ways to attack it.
*  And he does he does a fantastic job with that.
*  And, you know, so it's important like I'm good at certain things.
*  Doc's got a certain things.
*  He's so you want to have you want to know where your strengths and weaknesses are and sort of make sure they're complemented.
*  I think we have a nice, nice fit with that.
*  And now I feel like I didn't answer your question.
*  Like I just went off.
*  Well, let me just let me just say it in a different way.
*  Do you ever think there would be a time where there was a deal you had in front of you where it was a close call?
*  It wasn't like a home run.
*  And you would say, you know what?
*  I'm not going to make that deal because I like this guy.
*  This is my guy.
*  He's on my team.
*  Let's see what he's got.
*  Yeah, that happens all the time.
*  So I think when a team is rebuilding, which which I've luckily not had to do since since like oh five, then then like you shouldn't really factor that in much because you're you're trying to optimize your ability to to win in multiple years from now.
*  Yeah.
*  When you have a team like ours, which has great chemistry, and I've been really happy, you know, if you if you see the quotes from our players and it's real, I'm there every day.
*  You definitely have to be careful with that because he like it's similar to like if you add, you know, I got it all physics department.
*  If you add like a bad employee, it's almost like five times worse.
*  Yeah.
*  Then adding a good one now a superstar can help.
*  It's a huge factor.
*  You need to make sure you're not or if you add something and it's not working, you have to be able to get out of it like in some way like you have to have an exit plan.
*  Well, you mentioned rebuilding.
*  Obviously, this is a very touchy on both sides issue in Philadelphia where under one of your predecessors Sam Hinky, who I was a huge fan of, and I was a huge fan of the team.
*  And he worked with you in the past.
*  You know, they there were a couple of years where they didn't maximize the number of games they were trying to win.
*  They were trying to maximize building assets for the future and tanking as it's called.
*  And there are people who just reject this philosophically.
*  Like you should always try to win the most games this year.
*  Do you have feelings about this one way or the other?
*  Yeah, no one should.
*  That shouldn't be kind of like what what Sam did was exactly right.
*  And it's why we have Joel and Ben now.
*  And I think it's the only the only arguments that landed against it were like ones that Philadelphia shouldn't worry about, which is there are arguments that there's some minimum of efficiency.
*  Quality of team you need to present so that you're being a good partner with your other 29 owners.
*  But I mean, in terms of the micro of Philadelphia, what what was done was exactly right.
*  And it's the reason why, you know, there's a lot of winning happening right now.
*  One of the big reasons.
*  Yeah, no, I thought that's what you say.
*  I totally agree with it myself.
*  So I know I don't want to keep you too long, but I have a couple of sort of, you know, wrapping up the podcast questions here.
*  If you were the boss of basketball, if you were the commissioner of the league rather than the general manager of the 76ers, what would you say?
*  I would say that the general manager of the 76ers is the one that's going to be the most important player in the league.
*  So you're the commissioner of the league rather than the general manager of the 76ers.
*  Would you tinker with the rules of the game?
*  Do you think that you can make basketball a better game somehow?
*  Absolutely. Yeah. So there's a whole lot I would do the Elam ending.
*  I would do it, which is like people probably have to Google that.
*  You can explain.
*  It's actually easy to say Elam ending turns the end of a basketball game into a pickup game where you're just playing to a score versus playing to a clock.
*  Turns out playing to a clock creates all these weird skews in every sport.
*  So that's the sports that end like baseball or tennis, not to a clock or peer or better games at the end.
*  And so the Elam ending switches switches the end of it.
*  I would have one free throw for everything.
*  Like, there's no reason to have to shoot two, three free throws.
*  You just do one free throw for every point that you're going to get when you go.
*  I would only allow timeouts if the ball's already dead.
*  I don't want to stop.
*  I don't want to stop play if it's if it's live, like people love the back and forth in the live.
*  You don't want to stop that with timeouts.
*  You know, those are the and I would get some more radical things.
*  Those are just off the off the top of my head.
*  Some easy, some easy ones that I would I mean, the NBA, it's famous among non fans for the last two minutes of the game.
*  Take 20 minutes to play.
*  Right. That's something that should be fixable somehow.
*  Our last minute, 17 in our trial game recently took 19 minutes.
*  It was it was absolutely we're up 17 and they cut it to seven, which was great for them.
*  But like, yeah, the Elam ending would would fix that.
*  And so it's just something we need to get rid of.
*  Jump balls and have possession arrows.
*  I mean, there's just there's actually a lot of easy stuff that would help that help the game be more.
*  I would definitely reduce replay that that that's torture for me.
*  Like you just have to even after replay, you're still getting things wrong.
*  So I think everyone this should just be a disclaimer for an NBA game.
*  Look, we're going to do our best.
*  There's going to be a few things that are reviewable.
*  We're going to miss things.
*  And that's OK. And sorry.
*  And now watch your games. It'll be more fun.
*  Would you also have changes to the draft system, to the lottery, et cetera, to the we have a system now where if you do badly,
*  you're rewarded by getting a high draft pick and people want to change that.
*  That one turns out to be really tricky.
*  I actually think the commissioners balance that pretty well now.
*  He's flat. He's made it.
*  He's flattened the odds at the top.
*  And in theory, like if you grabbed an economist, they would say things like get rid of the draft.
*  They'd do like Mike Zarin, a Boston guy, and have a wheel where they're all predetermined.
*  The reality is it's pretty well balanced now because at the end of the day,
*  we're an entertainment business and you need to be able to sell tickets.
*  So the teams that are bad, you need to have something sellable for them.
*  And the draft is a really good way to do that and gives them a lot of hope for the future.
*  And I think I think it's pretty well balanced now in a system that's not very easy to fix.
*  The one thing I would do is I'd probably do one of these hybrid systems where instead of a draft order,
*  you would get you'd get like basically fake fake coins.
*  You'd get like Chamberlains, you know, like you call Chamberlain coins like you like some sort of crypto Bitcoin and like whoever is the worst team will get the most.
*  But then they could allocate their bidding on what pick they want.
*  I see. OK. Right. Because if you are rebuilding, you might instead of having to trade back from one like Philadelphia did to get to swings at it,
*  which actually conceptually was a reasonable trade.
*  Obviously, some of it didn't turn out. But but conceptually was a reasonable trade for both teams for Philly to to trade up and Boston to trade back.
*  And and you could be able to do that by instead of forcing people into their slot, giving them more things to bid against a class.
*  So there are things you could do.
*  But you definitely want to give bad teams an advantage in the draft just so you have something to sell.
*  If this is a very, very broad philosophical question.
*  But once again, given that the audience here is eclectic, what is your sales pitch for sports being good?
*  What do you what do you think is the value of sports?
*  Like it's so artificial, right?
*  But it's also so compelling at the same time.
*  Well, it depends on what you have as your primary goal of life.
*  I mean, I think the Greeks had it pretty well.
*  The happiness is maybe the goal for each individual and and clearly like entertainment is part of that.
*  So, yeah, I think it's I think it's a pretty straightforward mapping to a useful goal in that it makes I think happiness is a is a good goal.
*  We should have the gross happiness product.
*  Product like people have said, if we can measure it, which we can't.
*  Well, I don't know. I mean, most teams do not win the NBA championship.
*  Is sports a net happiness increase?
*  It's not completely clear.
*  Yeah, I definitely think it's a net happiness increase.
*  Otherwise, I know people are very irrational, but they'd have to be shockingly irrational for the NBA to be, you know, you know, 10 billion ish dollar business.
*  And if half of people were miserable all the time.
*  Yeah, I think people like rooting for a team.
*  They like rooting for players.
*  They like rooting for a process.
*  They like rooting for, you know, back rivers.
*  They like rooting.
*  They like being part of something, a community.
*  And I think it provides.
*  All right.
*  Last question is, is it true that you have skeptical thoughts about dark matter in the universe?
*  Yeah, I was gonna I was gonna ask you this.
*  So I guess it's trending.
*  I'm so annoyed.
*  I feel like, you know, I feel like everyone's discovering nine inch nails now and I listen to their first album.
*  So I've been saying so there's a there's an analyst, Greg Piem, who is a theoretical physicist who worked for us in Houston.
*  And this was like, I don't know, 10 years ago.
*  He works for the Clippers now.
*  And, you know, I was like just telling him, no, there's no way dark matters.
*  Really? Just look at the history of of how knowledge is developed.
*  And any time we're plugging the big blank with something that you can't observe, it never turns out to be true.
*  And it's always that our theories are off or our measurements are off or something's off.
*  And so I had it like very likely that dark matter doesn't exist.
*  And I guess that's trendy now.
*  I've heard I've what is the latest on that?
*  I'm curious.
*  You would know.
*  Yeah, no, sorry.
*  This is the one part of our conversation.
*  I got to dramatically disagree here.
*  So I don't think it's trending.
*  There's a whole bunch of people who think about it.
*  I mean, as we've said, you know, we think about all sorts of things, right?
*  You can't get too emotionally attached.
*  And I've thought about it.
*  I thought about getting rid of dark matter, but it doesn't work.
*  You know, I mean, I absolutely buy the argument you just make if you had a hole and you filled it with some unknown thing.
*  But the thing about dark matter is we have a dozen holes and this one thing fills them all, whether it's the rotation curves of galaxies or the dynamics of clusters or the cosmic microwave background or the growth of structure.
*  One very, very simple model fits all of it.
*  So I'm still very, very bullish on dark matter.
*  Is the analogy then more because I mean, people say with dark matter, it's like a third in the late eighteen hundreds or whatever.
*  But what you're arguing is that it's closer to quantum mechanics where we have something that seems to fit every observable thing, even though we don't still totally understand how quantum mechanics work.
*  Right. I'm right about that.
*  We're still like puzzled by all that shit.
*  You're definitely right about that.
*  I wrote a book about it, but I'm agreeing with you.
*  Yes.
*  There you go.
*  And so, I mean, OK, but so that's your that that that makes that makes sense.
*  But I still feel like there's some theory that can overlay and explain all that to potentially.
*  Right. But you're saying the odds are getting low that that maybe that's the case.
*  I think I think actually it's a it's a very interesting history of science question because, you know, in the 80s or 90s, your point of view that dark matter is a temporary holding place for a more deep understanding would have been 100 percent respectable.
*  And again, like I definitely thought about it myself.
*  But I don't think that we as cosmologists have quite conveyed to the public the extent to which that changed when we really started observing the cosmic microwave background in detail.
*  You could make predictions if dark matter exists, the CMB will look a certain way.
*  If it doesn't exist, it will look another way.
*  And it came bang in on what was predicted by dark matter in a way that it's almost impossible.
*  I never want to say impossible, but it's almost impossible to reproduce that success in a model where you just change gravity without your your saying something important that I didn't know.
*  I didn't know about the CMB stuff.
*  Yeah.
*  That a prediction was made prior to knowing the result.
*  And then it turned out to fit the theory.
*  And so that's important.
*  I mean, that's that's what happened with quantum mechanics.
*  Like, I'm right.
*  You tell me, right.
*  Where where the theory kept predicting things that kept being true over and over.
*  And even though we didn't quite know the full mechanism, although we know it much better now, to your point,
*  that that it's so what is the best candidate is like these like these huge like remnants of the Big Bang.
*  Like, what is the best candidate at this point?
*  Well, that's I think the totally fair worry is that for a long time we had a favorite candidate, the weakly interacting massive particles.
*  Right. We have the weak interaction of particle physics, the WIMPs.
*  Right.
*  We have the weak interactions of particle physics.
*  It's very easy to invent a new particle that is not electrically charged but does feel the weak interactions.
*  It very naturally would have the right abundance in the universe to be the dark matter.
*  But we could have found it by now.
*  And we still the chances that we would have had by now are maybe like 60 percent.
*  It's not like ninety nine point nine percent.
*  But we had a good chance of finding it by now and we haven't.
*  So at some point, your credence is this got to have got to go lower.
*  And to me, that doesn't decrease my credence in dark matter that much.
*  But the more esoteric candidates like axions are a famous candidate.
*  They're very, very light particle, lighter than a neutrino basically.
*  But they could sort of be left over from the Big Bang in interesting ways.
*  And so if it's not a WIMP, if the dark matter exists, but it's not a WIMP, then there's dozens of other candidates.
*  Does it interact with anything?
*  Does it lens? Does it gravitationally lens stuff?
*  What is it like?
*  Oh, absolutely.
*  Yeah, I mean, that's the one thing we know about dark matter that it has a gravitational effect.
*  That's why we know it's there. That's why we believe it's there.
*  And in fact, these days we literally map it.
*  You know, we know where it is through gravitational lensing mostly.
*  So you get these gorgeous images, you know, three dimensional reconstructions of the dark matter density,
*  even though we have never detected the particle that it actually is.
*  It still feels like it's going to be something totally we don't.
*  I just like it.
*  It feels like, yeah, my gut till tell.
*  But of course, I just have my gut and your guts better than mine.
*  It's more more more experienced.
*  One of the reasons why I feel justified in being so confident about this is that I would love it if I were wrong.
*  Like no one would be happier than I would be if there was something interesting going on with gravity that tricked us into thinking.
*  We don't even totally understand gravity, right? So that's another thing.
*  We don't totally understand anything.
*  We actually understand gravity on scales of the solar system and larger pretty well.
*  We are able to imagine other things. I've written papers imagining other things.
*  But, you know, I think Einstein more or less nailed that on the astrophysical scales.
*  Gravity is pretty well under control.
*  Gotcha. I think it's just the simulation people f***ing with us.
*  They're just like, they're just like, oh, they're looking again.
*  They're trying to see if they can find the dark matter.
*  We'll put it in there.
*  That is, you know, I literally when we were looking for the Higgs boson back before the Large Hadron Collider turned on,
*  I literally had a theory that every place we looked like there was a probability of seeing the Higgs boson with different masses.
*  And whenever we looked and didn't find it, it just moved up and you can invent physics theories along those lines.
*  But I think for the dark matter is just we haven't been clever enough yet.
*  We don't have enough direct evidence.
*  Why would we stop the Collider in Texas? That would have been awesome.
*  Like, I'm so annoyed that that got killed.
*  We it would have been not only earlier, but it was a more powerful accelerator than the Large Hadron Collider.
*  Are we getting that or are we still? It feels like it's set science back like 25 years.
*  The United States has entirely abandoned even the attempt to build world class particle accelerators.
*  So right now, the debate on what the next one will be is between China and Europe.
*  I remember Biden making this a big part of his platform. I'm surprised.
*  The physics community doesn't know about it. Yeah, no, it's it's it's they're expensive.
*  You know, and I and I get that. But we build them once every 20 or 30 years.
*  I think it's worth the expense myself. It's easily worth the expense.
*  Yeah. All my friends are like now tell me it's stupid to go to Mars.
*  And I'm like, yeah, it is. But like, why wouldn't we?
*  Like, we'll we'll learn we'll learn something. Right.
*  It'll be interesting. It's part of a portfolio. You got to do some crazy things.
*  You got to do some ambitious things as you don't know.
*  You know, I had Martin Reiss, famous theoretical astrophysicist on the podcast.
*  And he points out that people were worried when we turned on the Large Hadron Collider, would it destroy the earth?
*  And he was literally even though he's British, he was called before Congress to testify.
*  And he said, you know, as a careful scientist, I can't promise you it won't destroy the earth.
*  But I can't promise you it won't be free energy and cure all the diseases we have either.
*  Like those are fringe things that we can't care about.
*  We can't control those. Like, let's look at the likely thing in this particular case.
*  Well, politics and media do really bad with orders of magnitude.
*  So, yeah, they're like, yes, it's possible that this could happen.
*  But it's also possible the plane could crash into my building right now.
*  And they can't distinguish that fear from one that's 10 percent.
*  Like we just do really bad between 10 percent, 1 percent, 0.1 percent.
*  We're really terrible at that.
*  Yeah, there is some bias.
*  I think it I don't know if it has a name or not, but the only percentages that people believe in are 0, 50 and 100.
*  I think Nate Silver is a good friend, has talked about that quite a bit.
*  But here's the bottom line.
*  I say we start off talking about championship odds in Vegas.
*  What is the current betting odds on them finding dark matter in the next five years?
*  There must be somewhere you can wager on this.
*  Yeah, no, I'm sure there are.
*  And if you would ask me five years ago, I would have said it's over 50 percent chance that we would have found it by now.
*  That's why that does raise some skepticism, I think.
*  But so if it's not a weakly interacting massive particle, then there's still wonderful evidence that dark matter exists.
*  But none of the other candidates are as easily searchable.
*  So we might be stuck for the rest of our lifetimes with thinking there's no matter in five years.
*  I'm glad you guys didn't call it the GIMP.
*  There's a whole bunch of a whole bunch of bad puns in physics.
*  And on that note, Darrell Morey, thanks so much for being on the Mindscape podcast. This was great.
*  Thanks so much, John. Appreciate it.
*  Thanks for watching.

---
Date Generated: June 08, 2024
Transcription Model: whisper medium 20231117
Length: 5025s
Video Keywords: ['gerrymandering', 'mathematics', 'politics', 'random walk']
Video Views: 8069
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2021/06/14/151-jordan-ellenberg-on-the-mathematics-of-political-boundaries/

Any system in which politicians represent geographical districts with boundaries chosen by the politicians themselves is vulnerable to gerrymandering: carving up districts to increase the amount of seats that a given party is expected to win. But even fairly-drawn boundaries can end up quite complex, so how do we know that a given map is unfairly skewed? Math comes to the rescue. We can ask whether the likely outcome of a given map is very unusual within the set of all possible reasonable maps. That’s a hard math problem, however — the set of all possible maps is pretty big — so we have to be clever to solve it. I talk with geometer Jordan Ellenberg about how ideas like random walks and Markov chains help us judge the fairness of political boundaries.

Jordan Ellenberg received his Ph.D. in mathematics from Harvard University in 1998. He is currently the John D. MacArthur professor of mathematics at the University of Wisconsin. He competed in the International Mathematical Olympiad three times, winning a gold medal twice. Among his awards are the MAA Euler Book Prize and a Guggenheim Fellowship. He is the author of How Not to Be Wrong and the novel The Grasshopper King. His new book is Shape: The Hidden Geometry of Information, Biology, Strategy, Democracy, and Everything Else.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x

#podcast #ideas #science #philosophy #culture
---

# Mindscape 151 | Jordan Ellenberg on the Mathematics of Political Boundaries
**Mindscape Podcast:** [June 14, 2021](https://www.youtube.com/watch?v=QN7LyhPZrLY)
*  Hello everyone, welcome to the Mindscape Podcast. I'm your host, Sean Carroll.
*  There's something that is very common in physics as well as in other areas of science, namely coarse graining.
*  This is something that you do when you have a situation where there are many things going on, perhaps at a microscopic level,
*  and you're not keeping track of all those microscopic things, right?
*  You don't know exactly where the molecules of air are in the room or in a cup of coffee or something like that.
*  So you take many different possible arrangements of the microscopic things and you group them together.
*  And you say like this set of arrangements is going to count as one big macroscopic configuration.
*  This different set is going to count as a different thing.
*  Now it turns out that in representative democracy, something very similar happens, right?
*  You have many, many people, many, many citizens of the democracy.
*  And it's usually impractical to imagine that all those people will directly vote on every single issue that comes up in the country.
*  That's called direct democracy. It doesn't really work very well. It hasn't been tried that often.
*  But instead, what you do is you make a republic, a representative democracy, right?
*  You have the individual people vote for representatives.
*  The representatives are supposed to represent their interests in the legislature or as the president or whatever.
*  This raises an interesting problem.
*  How do you go from the set of all the different opinions and feelings that the citizens have,
*  which might be a huge different sort of heterogeneous set of ideas and goals and desires,
*  and coarse-grained them into a small number of people who will actually travel to the Capitol and sit in the legislature or the parliament or what have you.
*  So today's guest is Jordan Ellenberg.
*  Jordan is a well-known mathematician who specializes in algebraic geometry.
*  He's the author previously of How Not to Be Wrong, a New York Times bestselling book.
*  And he has a new book coming out called Shape, the Hidden Geometry of Information, Biology, Strategy, Democracy and Everything Else.
*  So what Jordan and I are going to talk about, he has many different things going on in the book.
*  But we've picked out this theme of how you coarse-grain your democracy.
*  And in particular, how do you draw boundaries for congressional districts?
*  This is the problem that we face in the subject of gerrymandering.
*  Gerrymandering is the idea that a party in power can fiddle with the shape of different districts to guarantee that it gets more seats in Congress than it deserves in some sense.
*  Now, as soon as you say that, you say, well, what do you mean deserves?
*  And it's not clear.
*  We have to actually think about the politics of this, the political philosophy.
*  How should we represent the goals, desires, interests of different people in the government?
*  That's fine. We're not going to talk about that today.
*  That's a very important politics and political philosophy question.
*  But there's also a math question.
*  Given some particular goals, how do you make them happen mathematically?
*  And even more importantly, at a legal level, how do you know when someone is bending the rules?
*  How do you know when someone is cheating?
*  Turns out you can say, well, consider the space of all possible shapes of districts in a state.
*  Can you say that the particular one that the legislature has drawn is unfairly biased?
*  That's a good, rigorous math problem.
*  And talking about it gets us into interesting questions in geometry, but even more interesting questions in randomness.
*  Even though the question we just asked seems pretty straightforward, you're comparing the specific map that people have to draw the districts to the set of all maps.
*  You can't really analyze the set of all maps. It's too big.
*  Instead, what you do is a random walk through the set of all maps.
*  That gets us into questions of how you do random walks and Markov chains and different algorithms for searching the space.
*  So it's a wonderful example of how not just physics, but other areas of human inquiry bring up these very intricate, very interesting math problems.
*  We're using politics here really as an excuse to talk about math.
*  We're not talking about politics that much in this episode, but the math that you need to do politics well turns out to be fascinating in its own right.
*  So with that, let's go.
*  Jordan Ellenberg, welcome to Mindscape Podcast.
*  Hi, thanks for having me on.
*  So we're going to be talking about gerrymandering and the role of geometry in math and gerrymandering.
*  It's a slightly political topic, but you're a mathematician as a professional here.
*  So why don't you just, for the sake of the listeners, say what you do for a living?
*  What kind of mathematician are you?
*  So I'm primarily a number theorist, which means that I study these questions that mathematicians have been wrestling with really since there was such a thing as formal mathematics.
*  These questions of you write down an equation and does it have solutions in whole numbers?
*  And if so, what are they?
*  That is something we somehow still don't know that much about all these many millennia later, although we certainly know more than we did at the outset.
*  But maybe more specifically on what's called an arithmetic geometry.
*  So over the especially in the last hundred years or so, we've come to see that these questions, which seems to be purely numerical or algebraic, actually have like a very, very serious geometric under structure.
*  And that's very much the way that the subject is seen now in 2021.
*  Well, that was one of the interesting things that I learned from talking to Emily Reel, who we just had on a few weeks ago.
*  And we haven't had that many mathematicians on.
*  Yeah, we haven't had too much math.
*  But now there's like a surfeit of mathematics.
*  I don't know what's going on here.
*  But she said she comes, I guess, from the opposite side.
*  She's a topologist and she keeps finding, as topologists do, these algebraic structures in the study of how you can deform things from one to another.
*  Yeah, that's so interesting because she has so fully manifested herself as a category theorist that I think of her as that and I actually didn't know that she started in topology, although that's certainly the origin of that subject.
*  Yeah, no, that's exactly right.
*  Exactly right. So despite all this and despite the fact that, you know, math, one of the most pure abstract, philosophically elevated things we can think about, I don't think that you testified in front of the Supreme Court, but you at least signed a brief that went in front of the Supreme Court, right?
*  Exactly right.
*  So sort of when the Supreme Court is considering a big case, especially a case with a lot of technical content of various kinds, they get briefs from all kinds of specialized groups.
*  But typically, and in this gerrymandering case, this was the case, there's briefs from historians, briefs from political scientists, briefs from lawyers, briefs from community groups that have interest in the case.
*  I think this is, as far as I know, the first case in the history of the Supreme Court where there was a mathematician's brief.
*  And you're 0 for 1. The mathematicians did not get the answer that they were hoping for, right?
*  So we'll have to wait another 200 years for the next case, this mathematical, to come before the court.
*  Okay, so even on record.
*  We might have listeners who are not familiar either with politics or the United States or lingo or anything like that. What do we mean when we use the word gerrymandering?
*  Right. So the fundamental idea is this, that in the United States, in both the US Congress and in state legislatures, we elect the people who make the laws from geographic districts.
*  We cut the state up into a set of districts. In Wisconsin, there happened to be 99 of them.
*  Sort of a weird number, I know, but it's in the Constitution that every Senate district has to be three assembly districts.
*  So it has to be a multiple of three. That's what the Constitutionally mandated.
*  And you break the state up into these districts, and then each district elects a legislator by majority vote.
*  What we have, in some sense, we've known for a long time, but it's really like come to a kind of apex now, is that this process of choosing how you execute this division, how you divide the state up into districts, which seems kind of technical and boring.
*  And I guess you just brought some lines and do it. That turns out to have an absolutely huge effect on who sits in the legislature, or rather it has a huge effect if you work hard to give it a huge effect.
*  And that process is called gerrymandering, that process of partisan actors, motivatedly drawing the lines so as to ensure that their party is advantaged in the election.
*  And I think it's sort of best summed up with a popular description of the practices saying instead of the legislators are choosing their voters instead of the other way around.
*  Yeah, I mean, and it's all based on the fact or arises from the fact that for whatever reason, we choose to allocate our representatives geographically in some sense, right?
*  The starting point, which we're not even going to question in this discussion, is you divide the state up into regions of geography and then within each region you vote for who wants to represent you.
*  Right. And one thing I learned writing about this is that there's lots of places that don't do it this way.
*  In Hong Kong, there's a constituency just for teachers. To run for the seat, you've got to be a teacher. There's a teacher seat. There's an engineer seat. There's these so-called functional constituencies.
*  You know, in Iran, there's a seat just for Jews. In Ireland, there's a seat just for graduates of the University of Dublin. There's lots of ways.
*  I want to hear my craziest idea about this. Sure. I thought it would be I mean, I thought it would be cool if like, maybe we shouldn't really do this.
*  But imagine if there was a seat, imagine if you broke the age ranges up into bands of equal population. It was just like, OK, there's like a congressperson, there's a representative of people aged 40 through 51.
*  You know, you could argue that those people across the state have a lot more in common with each other politically in terms of what their priorities are, what their needs are, than people of very different stages of life who happen to live 50 miles apart.
*  And that's in the same congressional respect. Well, it's interesting to think about the future because I can imagine that 200 years ago, geography was just the way that you could easily slice this pie.
*  But these days we can do better. Yes, I'm interested to see whether or not I know that there are a lot of clever, maybe overly clever voting schemes on the market, but we'll see whether any of them actually catch on in real elections.
*  But one of the one of the instant worries you get to, and we'll probably get to this in more detail, but when you have this scheme where you divide things up geographically and then just have a majority vote, is that so if you have a state with 99 representatives, let's say,
*  and 60% of the state, as you very nicely put it, you know, there's the orange party and the purple party. So you're not associating these with any real parties here in the United States.
*  So 60% are orange voters, 40% are purple voters. And in this weird idealized situation where every district is exactly 60% orange voters and 40% purple voters, all of the representatives would be orange, even though 40% of the voters are purple.
*  So there's sort of a built in amplification of tiny edges in the voting, right?
*  Yeah, and this is, you know, I sort of set this up as a thought experiment in the book. But you know, it's also called Massachusetts. That's another name for this phenomenon, right?
*  In Massachusetts is a state which there are Republicans in Massachusetts, not even that few. I think it's about a third of 35% of the state. That's pretty significant.
*  Yeah, if I remember correctly, there hasn't been a Republican member of Congress from Massachusetts since 1996. Right. I mean, it's been it's been nine Democrats for a long time. And that's actually not because of gerrymandering.
*  That's because the very nature of geographic district thing, as you say, in a state that's two thirds Democratic, there's not going to be very many Republican neighborhoods, certainly not like entire Republican patches of the state big enough to be a congressional district.
*  Right. So I guess what I wanted to get on the table there was just that, like you say, even forgetting about gerrymandering, this whole idea of just having geographic districts and voting in them can lead to big distortions if you compare it to just proportional representation from inside the state.
*  Right. And this is one of the reasons this question is so interesting is that you really find yourself saying, what does it mean to be representative?
*  Right. So one, I mean, it's very natural to think that the right notion of representativeness is, as you say, what's called proportional representation, which means that the proportion of legislators from each party is roughly the same as the proportion of voters for that party.
*  Maybe not on the nose, but that a deviation from that is understood to be some kind of failure of representativeness. That's a system a lot of countries have. It is definitely not the American system. And it never has been.
*  So, you know, look, I always say, like, people write about this in terms of Democrats and Republicans, but like, you know, sympathy for the libertarians, man, like year in, year out about 1% of American voters vote for a libertarian congressional candidate.
*  Now, there's 435 members of the House that you believe in proportional representation. You think there ought to be a few libertarians sprinkled in there. And how many are there? Zero. Because there's no such thing as a libertarian congressional district or even a libertarian neighborhood. It's kind of fun to imagine what it would look like, isn't it?
*  But as far as I know, it doesn't exist.
*  Well, yeah, because of this effect that our voting system or our system of apportioning representatives turns up the contrast knob, right? So a slight advantage in the electorate gets you a huge advantage in the chamber. And if you're down there 1%, you'll be normalized down to zero very, very quickly.
*  But one thing I mean, we're sort of imagining this is sort of some kind of like system with noise in it. If you're in a state like Wisconsin, where I live, now you're in California, which is a very different story.
*  But in Wisconsin, where the proportion of voters who vote Democrat or vote Republican is pretty close to 50-50. But because of that, the political conditions are quite different when the mood of the state is more Democratic and the mood of the state is more Republican.
*  So under what you might call a normal system, even with single-member geographic districts, there would be swings. There would be years when Democrats held the majority and years where Republicans held the majority.
*  So at any given time, that majority might be pretty big in favor of one party or the other, but it would switch back and forth.
*  And in some sense, there's some political justification for that. There's some political justification for saying it's good for the legislature some of the time to sort of have a healthy majority of one party so that things can get done.
*  And then if the voters don't like those things that are done, then it switches, right?
*  Exactly. You're bringing up the fact that we don't agree ahead of time on what we want a fair outcome to be in any of these situations, right? There's competing interests that we have to get to.
*  But so just to be super clear, I think that you said it already in some sense, but how gerrymandering works is sort of to advantage one party over the other, taking advantage of the fact that the representation within each district need not be reflective of the state as a whole.
*  Exactly. And if you're the person drawing the maps and in many states, Wisconsin being one of them, the people who draw the maps are the legislators, the very people whose electoral fortunes are at issue.
*  So it's like hard to imagine a worse feedback loop from the point of view of conflict of interest.
*  Right. You know, to put it, and you can draw lots of charts and pictures and graphs, but the fundamental way it works is pretty simple.
*  The party that you don't favor, you try to cram all of their voters into just a few districts.
*  You try to create districts which are absolutely dominated by the opposing party because by doing so, you're sort of using up their voters.
*  And if you like wasting their votes on a few districts that they'll win by a lot, leaving the rest of the state composed of more districts where you win by a more modest amount.
*  And that's exactly what we see in Wisconsin.
*  And just to be clear, this happens everywhere, well, at least in the United States.
*  This is this procedure of drawing weirdly shaped districts, and you can show pictures and sort of laugh at how weird they are.
*  This is really, really common, as far as I can tell.
*  Well, a couple things I want to say about that.
*  One, it doesn't happen everywhere because not every state has the procedure where the legislators themselves are the ones drawing the map to determine their own fate.
*  So there are states like Iowa is one where forever they've had sort of some panel of retired judges draw the maps and nobody's going to say they're perfect, but they're not people whose literal job is to be political operatives for a political party.
*  And when I say that the legislators draw the maps, that's not even quite correct.
*  It's like literally people who work for the state party, not even elected officials, but just people whose entire job is not to represent the public, but to represent the interests of their party.
*  That's who's actually sitting in the room drawing the maps.
*  So one thing I like about this as a sort of place where there's a possibility for reform is the system we have is like literally almost the worst possible thing we could have.
*  Any change from it.
*  Like, you know, is the system of just asking some retired judges to draw maps perfect?
*  No, but it's way better than what we're doing in a lot of states.
*  So this then raises the question of how now the math begins to come in.
*  One question, I guess the first question we might address to ourselves is, is there a way of characterizing how unfair a particular set of maps is?
*  And so what do people say about that?
*  Yeah, and actually, that's a great question, because what it turns out, if you try to say what's fair, like what's the perfect map?
*  What's the map that's truly representative?
*  I don't think that's a question that has a mathematical answer.
*  Actually, I don't think it has a philosophical or a legal answer either.
*  And then you might say, well, so what the hell are you going to do?
*  Well, I think the question of what's fair is very hard, but I think the question of what's unfair is much easier.
*  And that's a crucial distinction.
*  We're not looking for perfection here.
*  I think eliminating gerrymandering, saying we're going to turn the gerrymander knob to zero, that's impossible.
*  That's an unrealistic hope.
*  And it's not even clear it makes sense, right?
*  It's like saying I'm going to eliminate all trace of bias from my thinking and be perfectly rational.
*  No, but you can look for the worst offenses, right?
*  Again, which we can see right here on the ground in Wisconsin and then there's a few other states.
*  But one thing I want to say that's really important is that a very common and historically grounded myth about gerrymandering is the thing that you said that it has to do with funny shapes districts.
*  In fact, it's right there in the name.
*  That's sort of the word gerrymander comes from this famous political cartoon about a map drawn by Elbridge Gerry, whose name I am told was actually pronounced Gary.
*  But that ship is sailed.
*  Everybody calls it gerrymandering.
*  Sorry to the descendants of Elbridge Gerry, but we're calling him Jerry.
*  You know, this kind of crazy district of Massachusetts that he engineered as governor, which they said looked like a salamander.
*  And so it was the gerrymander.
*  This is the origin of the name.
*  And, you know, now, too, there's like there was a famously crazy looking district in Pennsylvania that was warmly called Goofy Kicking Donald Duck because of the way that it looks.
*  But here's the thing.
*  Nowadays, when these maps are not being drawn by some kind of political savant, like sitting with a giant map, like rolled out on a big table, but are being done by machine.
*  If you say, I want a map that advantages my party by a huge amount and it looks fine.
*  The districts are shaped like, you know, roughly rectangularly and nice.
*  You can do that.
*  And in Wisconsin, we have exactly that.
*  If you looked at the map we had before 2011, which was drawn by a court and the map we had after 2011, which was a highly gerrymandered map drawn by political operatives, you wouldn't be able to say one of these has funnier looking districts than the other.
*  They look about the same.
*  So if that was ever a good measure of gerrymandering, it no longer is.
*  We can't detect it with the naked eye.
*  We have to do something more sophisticated.
*  We're all increasingly concerned about our privacy and security online and that includes you, a virtual private network such as NordVPN is for you.
*  I love NordVPN for when I'm traveling.
*  If I'm using Wi-Fi at an airport or in a restaurant, you can protect your data from hackers and NordVPN will automatically block malware sites and botnet controls.
*  And it has online security for your kids.
*  So it protects their online privacy as well.
*  NordVPN will block phishing sites and it has next generation encryption.
*  Furthermore, NordVPN is the fastest VPN out there and incredibly easy to use.
*  It's just one click.
*  So go to HTTPS NordVPN.com slash Mindscape.
*  That's N-O-R-D-V-P-N dot com slash Mindscape or use code Mindscape to get a two year plan plus a bonus gift with a huge discount.
*  And if the product is not for you, there's a 30 day money back guarantee.
*  That's NordVPN dot com slash Mindscape.
*  That's very interesting actually, because I hadn't quite appreciated that.
*  So you're saying that the use of computers and our modern data driven techniques allow us to gerrymander in a way that we don't know it when we see it.
*  We have to be a little bit more sophisticated about what it means for the map to be tilting in one direction or another.
*  I mean, you don't know it when you see it when looking at the map.
*  You may know when you see it and you're like, why do I live in like a swing state that has lots and lots of members of each party?
*  But year in and year out, the legislator has like a huge, near super majority of one party.
*  There you can see it. You can see the effects. You can't see it on the map.
*  So there was one effort to characterize the unfairness of maps that you talk about before sort of discarding.
*  It's not the right way to do it, which was the, I guess, the efficiency gap.
*  How many people's votes are wasted? And that does have a superficial plausibility to me.
*  Yeah. And I don't discarding is too strong.
*  I think there's been a sort of as in any area of scientific progress, there's going to be an iterative thing where we sort of develop like better and better measures.
*  You know, you think of a measure and then you're like, well, here's some of the problems with it.
*  In some sense here, you see the differences between scientists and politicians because politically you should probably sort of choose one thing and be like, this is it.
*  If you argue against this, you're wrong. But a scientist, you know, we're not inclined to do that.
*  We're always inclined to look at whatever it is we're using and be like, could this tool be made better?
*  What are the issues with it? What are the edge cases where the tool doesn't work so well?
*  So I think it's a bit, it can be a bit frustrating for the lawyers who are like, I thought we were arguing on this.
*  I'm not arguing on that measure, which I very well understand.
*  But again, because my framework is not let's make it perfect, but let's root out the absolute most grievous gerrymanders.
*  The good news is that we have a bunch of different measures and on a map like Wisconsin, they all agree.
*  Right. It's not hard. It's not hard to see that something like very dirty is going on.
*  And literally any reasonable measure you can think of will light the right light, the big bed blinking light.
*  But why don't you explain what the efficiency gap is?
*  I think it's at least a good example of sort of an attempt to make the voting fair.
*  Yes. The efficiency gap, what it measures is it says it relies on this notion of a wasted vote.
*  Where a wasted vote is one of two kinds. It's either a vote for the party that loses in a given district.
*  So it's a vote that somehow doesn't go towards getting you a seat or it's a vote for the winning candidate above that 50 percent threshold that you need.
*  So it's any votes above or beyond 50 percent.
*  And that would capture something very, very true about the way gerrymandering works, which is that if you're trying to be efficient with allocating your votes,
*  like if you could just draw the districts completely not geographically and just choose the voters, you'd be like, especially if you knew how they voted,
*  you would say after the fact, you would say, oh, OK, I'm going to make a bunch of districts where 50.001 percent of the voters are mine.
*  Forty nine point nine nine percent of the voters are yours.
*  And I'm going to win them all. And if the political nature of the state means that actually there must be a lot of your voters somewhere, I'm going to put them all in one district.
*  I'll put them all in one district and I win the rest.
*  That is would be very efficient where every time you win, you win by only a little.
*  You're kind of getting a lot of seats with very few extra voters at the margin.
*  And so I think that that notion of efficiency gap is very simple to compute.
*  And it captures something of it captures something very real about how gerrymandering works.
*  And you know, you can very clearly see empirically that it's a lot bigger in states where the legislature is drawing the maps for their own benefit than it is in states where there's some other system in place, whether a citizens commission or a judges commission or whether it was drawn by courts after a battle or what have you.
*  And then one of the arguments against it, though, if I remember correctly, is that if you did have this ideal situation where every part of the state had exactly the same representation, 60 percent orange, 40 percent blue,
*  that would not even if you just did everything completely evenly, that would not get a good score on the efficiency gap measure.
*  But there was no gerrymandering going on.
*  Yes, exactly. I think the one if the flaw of that measure is that in the end, it does kind of seem deposit that there's some right answer to how many legislative sheets there should be given a certain popular vote.
*  It's not proportional representation, but in some sense, it's in the same genre as proportional representation.
*  And I think and you know, by the way, this is something that there is definitely argument about.
*  So I don't want to sort of say that my view on this is the only one.
*  But it is the view that, you know, plaintiffs went forward with in the Supreme Court case of Rocha versus common cause is that, you know, the opposite of gerrymandering is not hewing to some standard that you think of in advance about what the number of seats should be.
*  The opposite of gerrymandering is not gerrymandering.
*  The opposite of gerrymandering is what would have happened if those maps had been drawn by a neutral arbiter of some kind.
*  Good. So now the math is going to start coming fast and furious because your your question now has shifted to the realm of the ensemble of all possible maps we could imagine drawing of congressional districts and asking questions about that.
*  And this is get this is what gets mathematicians very excited.
*  Right. I mean, this is where there starts to be some like really interesting math and where I think a lot of mathematicians have gotten involved.
*  You know, I can name a lot of names, Moon Duchin at Tufts, Justin Solomon at MIT, Jonathan Mattingly and Greg Hershlag at Duke, West Piper and Carnegie Mellon.
*  Lots of people whose day job is like proving theorems have gotten interested in this because, you know, it wouldn't be great if we were also civic minded that we would work on problems just because they're important.
*  But no, I mean, there's lots of important things in the world. We work on them when they're important and mathematically interesting.
*  I mean, so that this speaks to our special skills, to be honest, are not usually called for in most political questions.
*  So exactly right. What you'd like to say is, well, what if the map had just been drawn by somebody who didn't care which party came out ahead?
*  Let's say a map plucked at random from all the possibilities that there are.
*  That would certainly be like an unbiased, neutral, nonpartisan way to do it.
*  That sounds very appealing, but then you have like a big problem, which is that the set of all possible districts in the space of the state is like absolutely unfeasibly uncomputably huge.
*  I mean, I couldn't even tell you like how many there are. The ways to cut Wisconsin up into 99 pieces.
*  Right. That's a lot.
*  Well, you're slightly aided by the fact that there are these voting wards, thousands of them, but still they're discrete units.
*  So at least it's not literally an infinite number, right? But the question is how to divide up the voting wards into a set of congressional districts.
*  Right. I think there's about 7,000 wards in the state of Wisconsin.
*  Right. So if you think about how many ways there are to sort of partition 7,000 things into 99 pieces, that is a very, very, very big number.
*  Even if you start to impose requirements that each piece should be connected in Wisconsin, constitutional, you're not allowed to have districts that break up into several pieces, although in some other states that is allowed.
*  Even so, you simply can't write them all down on a sheet of paper or store them all on a hard drive and then pick one at random. You have to do something.
*  You have to find some proxy for that. And the way we typically do that is by this mechanism of what's called a random walk.
*  Right.
*  I mean, it's something that people in physics do all the time, right? A Monte Carlo simulation is something that happens all the time in physics.
*  Yeah, no, we-
*  You probably know better than me what's a context where that would be.
*  Random walks are surprisingly important for many reasons. But I just want to- before we get to that, I want to home in on one question that I had.
*  So, I mean, I can imagine the math problem of given a state with a certain shape, divide it into geographically pretty regions with approximately the same number of people in them.
*  That sounds both easier and very different than imagining all the ways to partition the state into geographic regions and find a typical one.
*  I mean, maybe the typical one looks kind of like weird and fractal. Is there a reason why we don't just pick the geographically pretty ones?
*  Yeah.
*  With your minimum area curves or something?
*  And by the way, I want to say that's not a hypothesis. It's good intuition. If you actually could choose a uniformly random one, the boundaries probably would look really bad in fractal. You can sort of see that in experiments on much smaller cases. My classes in Lorenzo Knight knows a lot about this actually.
*  So, right. You know, one thing I like about this problem is that it is a math problem mixed with a political problem and a legal problem. And you can't really separate the strands from the other.
*  So there is like a history of work that treats it as just a mathematical problem. In other words, like, let's mathematically sort of define what it means for districts to be nice and try to figure out like what would be the nicest division of a state into equi-populous regions.
*  And you get these, you know, you get sort of nice polygons, you know, like straight line boundaries. And then you like show this to like a politician or a lawyer and they will like laugh until they pee their pants.
*  Right.
*  Right. Because this has no bearing on anything that's politically feasible or anything that respects like actual political divisions in the state. And actually, you know, I mean, these are people who like live in real communities. And actually, you know, we have in Wisconsin, we have a People's Districting Commission, which has no legal powers, but the governor made one anyway.
*  Just to sort of say like, this is what it would look like if we drew a map. And, you know, I've been to some of their hearings and it's pretty cool. Just, you know, they hold a hearing and like people call in and just like regular people from these places in Wisconsin.
*  It's like, you know, my community is like split down the line between two assembly districts. Why? It makes sense for us. You know, we have these specific needs having to do with like this particular lake and its health and like, why are we not, why do we not have like one assembly member who like cares about this?
*  I mean, so those kinds of considerations, if you're actually doing it, you know, I want to say, I think the system we have is bad. But if you want to know why would there even be such a system in the first place is because in principle, a representative is actually supposed to be listening to the people that they purportedly represent working for those people, like not working for a political party they happen to be a member of. So there is like a reason this is thought of as part of the political process.
*  So if you talk to political science people or elected officials, they'll say there's no way we're going to let a computer draw them out. That's not nobody wants that voters don't want it. Politicians don't want it. Judges don't want it. That's a non-starter. And that's what happens if you try to treat it like a math problem without treating it also like a political legal problem. On the other hand, having now sort of crapped on my own tribe. If you try to treat it as just a political or legal problem and not a math or geometry problem, then you're going to have to be a political scientist.
*  If you try to treat it as a political problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if you try to treat it as a mathematical problem, if
*  you try to treat it as a mathematical problem.
*  And I'm insisting on that.
*  Okay, so the promise comes about?
*  Okay, so the promise comes about?
*  Well, the first and second generations of magical
*  centralization systems is what we called planar
*  planar planar polemonica.
*  fundament, squared to linear, Again, tutoring traditional
*  setups that can analyze and regulate наб elegism and
*  veramente Milwaukee.
*  Really really powerful methods to
* enzie that Chambers anymore 2 x
*  Leon Ap오ы.
*  A Cuzco is a temple, it's more
*  about this.
*  To answer your question.
*  So yeah, you have this big ensemble of randomly generated maps.
*  And it's certainly not all possible maps,
*  but it's a set of maps which for reasons we can talk about if we want,
*  are seen to be fairly representative of the set of all possible maps.
*  And we can build in certain biases that we want.
*  We can build in, hey,
*  I want the districts to be roughly round if you want that.
*  You can build in, hey,
*  I want the districts not to cut the county lines if they don't have to,
*  which in Wisconsin is a constitutional ask.
*  I mean, different states have different criteria for what the districts should look like.
*  Basically, you build in everything the districts are supposed to be like,
*  except you don't build in, oh, and by the way,
*  I want my party to have like five more seats than it would be if we were fair.
*  And then you look at your, like, whatever, your 20,000 maps or 100,000,
*  it's easy to make lots and lots.
*  And you see, you look at actual election results and say, like, okay,
*  if the wards were arranged into districts in this way, what would the outcome have been?
*  How many seats would each party have in the legislature?
*  And invariably, you just get a very nice, roughly Gaussian curve, a bell curve,
*  just like you always get when you do any kind of experiment like this, right?
*  You sort of see that there's very typical outcomes and then there's very atypical outcomes.
*  And in states like Wisconsin or North Carolina or Maryland,
*  where they have heavily gerrymandered maps,
*  the outcomes from the actual maps are way off in the tail of the distribution.
*  They're very visible outliers.
*  And so it gives you a really nice, clean signal of this is not something that happened by chance.
*  Much as the people who drew the map may want to tell you that, no,
*  this is an absolutely, like, grievous thumb of the scale in favor of one party and against the other.
*  Oh, I think this is very, very important because probably if people hear that we're talking about gerrymandering in math and geometry,
*  they might leap to the idea that you're using geometry to draw the map.
*  But that's not what you're doing. You're suggesting that, yeah, no, human beings will draw the map.
*  We're going to use math to judge how fair, how typical or how non-distorted that map actually is
*  in terms of comparing its actual results to what typical results would be. Is that right?
*  Exactly. The geometry is the referee here, not the player.
*  Good. And so we need to construct or at least deal with this idea of an ensemble of maps
*  to figure out what would be fair in the world of all the maps.
*  And by the way, is this one of the...
*  I hypothesize that this is one of the gaps between professional mathematicians and civilians,
*  that when a regular person talks about a random number, if you have a random number between zero and one,
*  instantly in their mind, in my mind, a number appears, .71835.
*  Whereas I think mathematicians actually just instantly go to the ensemble or to the probability distribution or something like that,
*  like converting the phrase random element into really what you mean is an ensemble or sort of a random variable is really a whole ensemble.
*  Is that a helpful step into thinking more like a mathematician?
*  Yeah. And I think the word random is, of course, like one of those heavily overloaded words.
*  To like my kids, it means a song I don't like.
*  You know, to...
*  And often, you know, to a mathematician, random...
*  Something that's completely deterministic could be random.
*  It's just random and all the probability is concentrated at one point, right?
*  So it literally just means something.
*  It just means the outcome. How would I even describe it in words, Sean?
*  This is hard, actually.
*  Maybe it means something in which chance could play some kind of a role.
*  But it doesn't mean, for instance, like, you know, if you flip a coin and it's weighted so that two thirds of the times it comes heads and one third of the time it comes tails,
*  a civilian, as you put it, would probably say, well, that's not random. It's biased in favor of heads.
*  A mathematician would say, oh, of course it's random, but just as a different probability distribution.
*  So we would say sort of like it doesn't have to be even anything that is subject to chance in whatever way you would consider a random variable.
*  That's right. OK.
*  And so but the particular issue that we're facing with here is you already made very clear is if you're trying to compare the actual map to an expectation of over all the possible maps you could reasonably draw,
*  that that ensemble of maps you could reasonably draw is far too big.
*  So rather than and sorry, I guess maybe something to get right here is there's an NP hard problem sneaking in here.
*  We did have Scott Aronson on the podcast a while back and we talked a little bit about NP hard problems.
*  But remind us what those are and what the specific one is.
*  Yeah. So the if you were to say I want a way of provably drawing a uniformly random map, which means that every possible map is equally likely.
*  Yeah. You have to formalize it a little bit more than that to sort of get it into like literal things.
*  The complexity theory that essentially that problem is known to be empty hard.
*  What that means is, you know, complexity theory is this very funny subject where there's this whole class of problems and what the kind of theorem people prove is like problem A is as hard as problem B and problem B is at least as hard as problem C and problem C is at least as hard as problem F and et cetera.
*  It was in turn at least as hard as problem A.
*  Okay. But proving that any individual problem actually is hard.
*  It doesn't have a fast algorithm to do it is like completely out of reach.
*  So the whole evidence could come crashing down tomorrow.
*  Right. So somebody could be like, I found a fast algorithm for like one of these problems.
*  And now they're all easy.
*  Okay. Nobody thinks that's actually going to happen.
*  But it's a very funny subject in that way.
*  So NP hard kind of refers to this class of problems that are, so to speak, the hardest problems.
*  And we think the case is that they're all hard rather than that.
*  They're all easy.
*  Yeah. But we don't actually know.
*  And so, but we can approximate them often.
*  So an NP hard problem takes a lot of steps to solve.
*  But then there's a somewhat independent question, which is how efficient could an approximate solution be?
*  Is there is there a general theory of that?
*  I don't think so.
*  And I've been to a lot of seminars about it.
*  And I mean, this is definitely and this is a little bit outside my field.
*  I'm not a complexity theorist.
*  But like I said, I've had so many interesting talks in like the sort of like machine learning optimization group at Wisconsin,
*  which is very closely tied to the math department.
*  It does seem like the way the subject is going is to say, like, I'll give you an example.
*  Traveling salesman problem, very famous NP hard problem.
*  You want to find the fastest route.
*  You know, you have like 100 cities or something and you want to sort of draw a path through all of them and you want to find the fastest one.
*  Now, that is an NP hard problem to do that provably and find the very fastest one.
*  And you can say, OK, great.
*  We proved the theorem. Like, that's really hard.
*  Meanwhile, while you prove that, people are just doing it.
*  Because, you know, the engineers, while you do that, they're like, yeah, but I'm content to get a solution to right now,
*  which with probability 99.99 percent finds a solution that's at least 99.99 percent as good as the optimal one.
*  So while you're over there proving your theorem, like I'm just making the math.
*  Half the people used Google Maps to get to the conference where you show you cannot solve this problem.
*  Right. Although people don't usually plan 100 conferences in a row, their entire itinerary, the entire thing.
*  I would not actually have no idea how Google Maps performs if you give it like 100 destinations next and ask it to chart a path through them all.
*  But so so I do think the way that field is moving is towards like, you know, what problems can we solve approximately?
*  And ideally, provably with high probability, but maybe probably with high probability, it starts to get a little philosophically fuzzy what it is that you're doing.
*  And so we want to talk about random walks now.
*  I think that's exactly where we are. So just to just sort of catch our breath, because we should pat ourselves in the back for getting this far.
*  So we have this problem of we want to compare a given map that some people in a smoke filled back room came up with to what to expect in the ensemble of all the fair maps.
*  But the ensemble of all the fair maps is way too big.
*  So what you're going to tell me is the way to sample from it, but unbelievably in my mind, is to pick one and then start changing it in little random ways.
*  Exactly. So so what you do is you start with some given map.
*  It could be the map that we have right now. It could be this gerrymandered map and say, let's do something to it.
*  But something pretty simple like the set of things.
*  Again, the set of possible things we could do to it is pretty big.
*  So I'm going to be very restrictive about what I'm allowed to do.
*  I'm going to say you're allowed to take two districts that are adjacent and move a ward on the boundary from one to the other.
*  OK, I'm going to be honest with you. The best possible algorithms are a little bit more complicated than this and an interesting way that makes them work better.
*  But I can't do it in audio. OK, you've got to look at the book and look at the picture.
*  You've got to buy the book anyway.
*  Yeah. And of course, we come out with.
*  But the basic idea would look kind of like this rather than sample from every single way you could possibly change it.
*  You restrict just these very natural local changes.
*  If I take a ward that's on the boundary and shift it to the district on the other side of the boundary and doing moves like that.
*  And then you say, OK, I'm going to do like 10,000 of those moves each time choosing a random some ward on the boundary.
*  Remember, the number of words is not very big. The number of words is about 7000.
*  So choosing a random thing on the 7000 is cake. That you can definitely do.
*  Yeah. And it turns out that just doing a few moves like that actually can sort of get you around the space pretty well and sort of get you a lot of very different looking maps.
*  You know, the analog I always like to bring up is the number of ways a deck of cards can be ordered is pretty big.
*  It's a number called 52 factorial.
*  You are not going to be able to list them all and pick one at random.
*  So then you might say, well, I guess the problem of like putting a deck of cards in a pretty random order must be an unfeasible problem.
*  But it's not a feasible right. I mean, you do it all the time. What do you do?
*  You just shuffle the deck. We know that there's an algorithm for that.
*  So how does that work? Because a shuffle is a particular kind of change that you're allowed to execute.
*  But unless you're some kind of sleight of hand genius, like there's a shuffle that you do is not going to be exactly the same every time.
*  There's some amount of randomness where there's sort of some small set of possible shuffles that you can execute depending on exactly what order when you like when you flip the cards down.
*  And it turns out and this is what you can prove theorems about.
*  So my undergraduate advisor, Percy Daikonis, is a very together with Dave Byer, is a very famous theorem called the seven shuffle theorem.
*  It's one of those theorems that does right what it says on the can.
*  It says that seven shuffles, which is a very small number, is essentially enough to put a deck in like extremely close to uniformly random order.
*  So this is the magic of the random walk with these that choosing from a very limited menu of possible changes and choosing one of random and just repeating that has a wonderful power to allow you to explore a space that you simply can't see from afar.
*  You can't see it globally.
*  It's like wandering around in a landscape where in order to have a map of it, you would have to sort of have a balloon and be like 10,000 feet above.
*  Well, what if you don't have a balloon?
*  All you can do is kind of like wander around at each moment, sort of choosing whether to walk north, west, east or south.
*  Northwest, I said, yes, OK, good.
*  But if you do that, that's actually like not a bad way to explore a whole space.
*  If you do that for a long time, you actually probably will get everywhere given enough time.
*  So I don't know if you know, but if you go to Vegas and play poker, many of the good poker tables will have automatic shufflers.
*  So the human being is not involved.
*  But if they don't, the casinos do not let the dealers actually shuffle the cards in an ordinary way because they are good enough to more or less put it in whatever order they want it to be.
*  So the way that they show is to just scatter the cards face down on the table and swirl them around with their hands before gathering them back up, because that's at least a little bit less controllable.
*  But I would think that doing that once would not be enough.
*  Is that right? My intuition would be that you'd want to do that several times.
*  Is that right? Or is one.
*  Well, if they're really scattered all over the place, right.
*  And then it's not just like a single shuffle where you pick two and move them back in and then you cut the cards, etc.
*  So I think it's good enough for government work or for Vegas work.
*  Yeah. OK, good.
*  So with that footnote on the table.
*  So just to be super duper clear, we're doing a random walk, but we're not doing a random walk through the state, assigning things to different congressional districts.
*  We're doing a random walk through the space of all possible maps.
*  And the nice thing is there's sort of an obvious local way to do that.
*  You have a map and you pick one boundary on the map and you sort of mess with that.
*  Right. Right.
*  Except, as I said, it turns out that there's a better local way to do it.
*  There's a little more. But it's something like that.
*  Yeah. Slightly more sophisticated.
*  Yeah. And this is a move that happens again and again in the history of geometry.
*  And it happens again and again in the book is that you think you're dealing with one geometry, but then to really solve the problem, you have to kind of go one level up.
*  And it's kind of meta. And think about the geometry of geometry, the geometry of the space of all possible ways to cut the state up.
*  So that is definitely a leap into abstraction.
*  And in a book like this, it is not for professional mathematicians or Supreme Court justices or professional gerrymanders.
*  You know, we kind of lead up to it. This is at the end of the book.
*  But it is a move that we constantly make going from the sort of very concrete geometry of two and three dimensional objects that we can understand,
*  kind of building our intuition there and then lifting that into geometrizing entities that are much more abstract and yet somehow can be approached using the same techniques.
*  Well, one obvious question is, I mean, convince me or at least assert very strongly that this kind of procedure will be a fair sample of the space of all the maps.
*  I mean, isn't it possible there's just some maps we never get to by starting with one map and making little local deformations?
*  So that is absolutely possible. In fact, we don't even know that the space of all district things is what's called connected, which means it's possible.
*  There's some other complete undiscovered country of ways to district the state that you never get to.
*  You can choose for yourself how much of a problem you think of that as being. For me, it's not.
*  And I'll explain why. Because if you start with the map that the legislators drew and you mess with it and basically every single thing you do to it rapidly dissipates the partisan advantage that it has,
*  that's a pretty strong indication that that particular map was cooked.
*  In other words, like you're right that we may not provably know whether it's an outlier among all possible maps, but we do know is that it's an outlier in its own neighborhood.
*  Like even things that are very much like it still are like not as incredibly favorable to the party through the map as the map that we actually use.
*  So that to me is a very strong signal.
*  Yeah, and I think that this makes sense to me as a physicist in sort of entropy terms in some sense, right?
*  I mean, there are a lot more equilibrated configurations of a set of molecules than there are low entropy out of equilibrium configurations.
*  So even if you start with a weird configuration and mess with a little bit, you'll push it much closer to an equilibrium one because there's just so many more of them, right?
*  Right, I mean, the headphone cord in your pocket, it's got to get tangled up because instead of untangled states, it's like pretty small.
*  You know, I actually mentioned this exact example in my book and I'm like, man, even for like readers now who are under 30, do they know what a headphone cord is?
*  This already and then like, you know, 10 years from now, people will be like, what is that?
*  What does he mean? What is the thing that you would have?
*  So hopefully, I'm not.
*  But OK, so yeah, I am.
*  I don't want to let this go by without taking advantage of some of the work you did for the book, digging into the history of the idea of the random walk, because it's fascinating.
*  Like all these history things are always very, very fascinating.
*  So when you say I started a point in some space and I walk randomly in some direction, that doesn't sound so hard.
*  But, you know, in fact, it crept up on us quite slowly, like mosquitoes were a big player in the first random walks.
*  Yeah, I knew almost nothing about the history of this.
*  So I had an incredibly fun time learning about it.
*  And it's one of these things that is surprisingly common in the history of science where somehow the world is ready for a certain idea.
*  So this idea of the random walk kind of comes up in a bunch of different contexts at once.
*  And it first comes up, well, maybe not quite chronologically first.
*  But as you say, Ronald Ross, who is the fellow who discovers that mosquitoes are driving the spread of malaria, he's the person who discovers the transmission mechanism of malaria.
*  And so he becomes very interested in like, well, what's the right mitigation?
*  Like, you can't kill all the mosquitoes, right?
*  That's another good example of a problem that's infeasible because there's too many.
*  But you can kind of clear some small area of mosquitoes.
*  And then what you want to know is like, well, how long does the area stay mosquito free?
*  Like, how good of an intervention is that?
*  Because, of course, the mosquitoes are going to get back in from elsewhere after you clear the area.
*  So to understand that, you want to know if a mosquito starts in sort of some stagnant pond where it's born, like how far is that mosquito typically going to migrate in a certain amount of time?
*  And because mosquitoes are not really very goal directed beings, that's a random walk problem because each day the mosquito is going to do something.
*  But as far as we know, the mosquito doesn't have particular aims.
*  Like it just kind of like flits where it will like day by day.
*  And so its progress is sort of a random walk towards the landscape.
*  And, you know, Ross, I mean, he's a fascinating character I literally had never heard of before I started writing this book.
*  I mean, this very famous figure in the history of medicine, he actually kind of secretly like really wanted to be like a mathematician and also a poet.
*  And was kind of like, you know, bitter about his life in medicine and sort of like felt like it wasn't really like that great of a thing to do, even though he was this super famous Nobel Prize winner.
*  Doctor. So he would like write poems about how unappreciated he was.
*  Anyway, it's a whole thing. It's a whole thing.
*  But he recognizes that this mathematical problem is of critical importance to understanding the spread of disease.
*  And actually he comes to the St. Louis Exposition of 1904, which I think among physicists is famous because it's where Poincaré gives this sort of famous speech about like,
*  maybe we're going to have to change physics.
*  Maybe things look different near the speed of light and things are going to have to be like, modified that the laws we know are only approximations.
*  I mean, this is a but he's also there.
*  And he sort of he sort of talks about how, like, well, they expect me to give a speech about medicine.
*  But what's really important is the math.
*  So I can talk about math and no one understood.
*  But he was that kind of guy. He was sort of a difficult character.
*  So he asks he asks Carl Pearson, the statistician Carl Pearson, if he knows anything about it, because he recognizes he can't really figure out analytically how to solve this problem.
*  And then Pearson writes a letter in the letters column of nature and Pearson coins the term random walk.
*  He tells Ross, like, I'll put it in nature, but I can't mention the problem is from biology because none of the mathematicians will work on it because they'll be like, we don't do biology problems.
*  This is considered very disreputable.
*  We made it an abstract problem and put it in nature and rather quickly a physicist, Lord Rayleigh, sort of explained, like, oh, I actually know how to do this.
*  I did it like 20 years ago for an application in acoustics.
*  So this is sort of like in England, how this notion of a random walk was first analyzed, the two dimensional random walk of a mosquito moving around in the landscape.
*  But what I discovered is at the same time, almost at the same time, you know, I think if, as you say,
*  civilians, if people who are not mathematicians actually know the phrase random walk, they probably know it from the title of Burton Malkiel's book, A Random Walk Down Wall Street, a book I really love.
*  Because it's one of the most, it's probably like the giant bestseller with the most math in it of any of any book.
*  And so I discovered that actually this idea is old too.
*  There's a graduate student of André Poincaré, Louis Bachelier, who comes from this non-traditional background.
*  He like worked in the bores.
*  He worked in the bond market in Paris before coming to study math.
*  And he was like, look, everybody's like buying and selling and trying to understand the market.
*  But I think it's just a random walk.
*  I think things are just like bumping up and down randomly.
*  Let's try to understand how that random walk would behave and see if it matches the behavior of the market.
*  Well, again, as with the biology, this was considered a little disreputable.
*  And Poincaré is kind of, I get that what you're doing is good math, but it's not the kind of math we do here in Paris.
*  Like we're supposed to be studying the three-body problem in celestial mechanics, not like bond prices.
*  But of course, now it's the dominant point of view, right?
*  I mean, if you're going to sort of do finance, if you're going to get a PhD in finance, you're going to be studying stochastic differential equations.
*  And you're going to be like random walking like hell.
*  Well, and by the way, this goes back to the point you made earlier that random doesn't mean absolutely equal probability of everything happening, right?
*  So the stock market can trend upward while still having a random component.
*  Absolutely right.
*  It's like it's a noise pest plus drip is like Danny Kahneman's new book.
*  It's just about this right in the way.
*  I like to plug on to those books too.
*  I mean, I can't even talk about it at all because it's too long.
*  And then there's the whole Einstein story and sort of Einstein is sort of like, you know, ratifying Boltzmann's theory of like what the understructure of matter is by sort of feeding Brownian motion like a random walk, which I didn't really know that much about.
*  But then, you know, what we call such a thing today, what we mostly call it in math is not a random walk, but a Markov.
*  So Markov is among mathematicians, the person who really first develops this theory.
*  And here's this is a story that blew me away that I'd never heard.
*  He invents the Markov chain because there's this huge like theological war between this, the arch conservative, super Russian Orthodox Russian mathematicians and the angry atheist Russian mathematicians of whom Markov was the leader.
*  And so his opposite member, a guy called the cross off, believed that he had found a mathematical proof of free will kind of ratifying the views of the Russian Orthodox Church in this matter.
*  And Markov was like, no way you could believe what you want, but don't bring math into it like that.
*  Now I'm offended.
*  Like that you would sort of say that math proves that your church stuff is correct.
*  So Markov develops the Markov chain as a counterexample in the cross off's claimed proof that free will is implied.
*  The free will is implied by probability theory.
*  I mean, you know, I always say like, you're on the Internet, right?
*  I mean, you know, is there anything more intellectually sterile and unuseful than like a long argument between like a movement atheist and like a movement Christian, right?
*  Those are nothing good ever comes out of that.
*  No, I think I got to push back there against I think that that there's a sampling problem when you when you say that there are loud, noisy exemplars of both sides that have very not very helpful arguments between each other.
*  But there can be useful intellectually productive discussions between people who hold the same opinions but hold them in more productive ways.
*  I guess you are absolutely right.
*  But I would counter that by saying that in fact, in terms of their personalities, Markov and the cross off were both exactly the kind of like loud and streper as like the hopeless people.
*  So it's amazing that out of their dispute like came this like absolutely fundamental mathematical idea.
*  But then it's amazing that like none of them knew about each other.
*  And this was math, right?
*  I mean, now sort of math is global.
*  But then stuff is happening in England.
*  Stuff is happening in France.
*  Stuff is happening in Switzerland with Einstein.
*  And stuff is happening in Russia with Markov and none of them do.
*  It's all happening between 1900 and 1905 and none of them knew about each other.
*  It's incredible.
*  Right.
*  So this is pre-Russian Revolution, Nekrasov and and Markov.
*  And I do I think that the audience deserves just a little bit of a glimpse into what Nekrasov thought he was doing with the free will business.
*  Like he was trying to reconcile the idea that individuals are allowed to have free will even though whole societies act in predictable ways.
*  Yeah, exactly.
*  So one thing.
*  So you start with the law of large numbers, which is like which has been over a long time, which essentially put in terms of coin flips,
*  because, you know, probability theory, the only thing we have are coins and earns.
*  Right.
*  Everything is about one of those two things.
*  So it's a but this is about coins, right?
*  You flip coins for a long time and with a very high degree of probability, the proportion of heads you're going to get is going to get very close to 50 percent for any fixed deviation from 50 percent.
*  The chance that you're going to get say 51 percent.
*  You certainly might get 51 percent heads if you flipped 100 coins.
*  But if you flip the million coins, that's incredibly unlikely.
*  And what people started to see and this is long after Bernoulli when sort of people started to study demographic statistics is the justice coin flips kind of settled down to predictable averages.
*  If there was enough coins, so social measures like tended to converge to predictable averages.
*  If there was enough people in your aggregate.
*  And so there was a lot of kind of philosophical unease about what that meant.
*  Did that mean we're just all like mindless coins were just all like sort of like little balls in the roulette wheel like sort of with, you know, you know, faded in some sense, essentially deterministically to sort of like at least as a society like acting a certain way.
*  Well, as you can imagine, that is not a happy thought for people of a certain philosophical bent.
*  And the cross-off body have found a way out of this.
*  The cross-off said, hey, hey, look, this this theorem of Bernoulli's this law of large numbers, it requires that the coins be independent from each other.
*  If your coins are not independent, like, let's say if each in the simplest case, let's say each coin is constrained to fall the same way as the previous one.
*  Well, then you'd either get all heads or all tails.
*  You wouldn't converge to 50 percent.
*  So the cross-off said, ah, this law of large numbers, these statistical regularities we see of like, you know, age of first child, age of first marriage, like proportion of various crimes, like all these things you see.
*  The fact that those seem to converge to stable averages might have made you thought we're just mindless coins.
*  But no, what it really shows is that we must all be independent from one another.
*  So, aha, I win.
*  Yeah, but there's a basic logical flaw there.
*  Yeah, so what Markov observed is that he was mistaking the theorem for its converse.
*  I mean, Bernoulli's theorem says that if the coin flips are independent, then you get these this convergence to stable averages.
*  But it didn't show that if you have convergence to stable averages, then the flips must have been independent.
*  So what Markov showed is that any kind of what we now call a Markov chain or a Markov process or a random walk,
*  that the behavior of such a thing also converges to predictable averages, even though if you're sort of walking on a random where you are today is anything but independent where you are yesterday because you're very close to where you're only one step away from where you are yesterday.
*  So they're very, very, very tightly connected.
*  But then, you know, having won this battle, he did all kinds of crazy things with it.
*  He analyzed Eugene Onegin, the famous poem by Pushkin, and sort of studied like, I mean, if you treat this as it seems crazy to think about a poem as a random walk, and he certainly knew that a poem was not just a random walk,
*  but he nonetheless showed that you could just treat it as a string of consonants and vowels.
*  There's a very modern kind of computational style approach, reducing it with string of bits, zeros and ones, and showed that you can calculate what's the probability of transitioning from
*  if a letter is a consonant, what's the probability the next letter is a vowel or the next letter is a consonant.
*  That's a very simple Markov chain.
*  You might say like, that cannot tell you very much about this famous Russian poem.
*  But you know what?
*  He was able to show that it distinguished it from a different book by a different Russian author, that there were like measurably different patterns in the Markov chain, just in the sequence of consonants and vowels.
*  Because different authors have different favorite words or different sequences of words.
*  So whether a consonant follows a vowel will be different likelihoods for different authors.
*  Right.
*  Okay.
*  And so that's in some sense the precursor to like so much of like the natural language processing we do today.
*  Of course, we do it in a much more sophisticated way than him writing down these kind of like grids on pencil and paper of consonants and vowels.
*  Well, right.
*  So all the way up to GPT-3, right?
*  I mean, this purported artificial intelligence is actually just looking for these kinds of patterns or these likelihoods, these probabilities of different things happening in texts and spinning them back at us.
*  Right. It's in some sense trying to find the Markov chain that best matches the language production it is able to see.
*  And it's able to see a lot because it has access to this sort of gigantic corpus of English language text that exists on the Internet and people have stored.
*  Okay, wait a minute.
*  What is what is the definition of a Markov chain?
*  How should we be thinking about that or visualizing it in our brains?
*  You should think of it as any process that explores a space where you're in some state.
*  And then we can be more complicated than this.
*  But let's say like the simplest thing would be to say you're in some state and then where you go next only depends on where you are right now.
*  And there might be some randomness to it.
*  It might be that like, you know, if I'm at Fifth Avenue and 29th Street, I'm going to walk either a block north, a block south, a block east or a block west.
*  So there's four places I can be.
*  And it's not deterministic.
*  Maybe I flip a four sided coin and decide which of the four ways to go.
*  But the point is that if I choose to walk north to Fifth Avenue and 30th Street, then my next choice doesn't depend on the choice I just made.
*  All I know is that it's kind of like having a movie memento or he has amnesia.
*  At every moment, you don't remember anything except where you are right now.
*  And you have to decide what to do next based on that.
*  That's the characteristic feature that makes a Markov chain a Markov chain.
*  Good.
*  But so it's very much like a random walk.
*  It's a generalization of the idea of a random walk.
*  But we're we're walking in some very abstract space, which for Markov himself was just vowel or consonant when he was looking at Pushkin.
*  Yeah, right.
*  A two point space.
*  That one constant.
*  Yeah.
*  And so when you're either in either one, you're either in vowel or you're in consonant.
*  There's the Markov chain is characterized by the probability that you'll either just stay at vowel or jump to consonant.
*  Right.
*  These are so called transition probabilities.
*  And you can already see that this model is not complicated enough to really capture how language works because, you know, maybe you're going to have two vowels in a row, but you're probably not going to have five.
*  Yeah.
*  And so the Markov model cannot see that because at each stage when you're at a vowel, there's some chance of staying at a vowel.
*  So you want to dress it up a little bit more and make it a little more complicated.
*  Yeah.
*  So the whole point of the Markov chain, the Markov process is this memoryless quality.
*  It only depends on where you are now.
*  It doesn't remember where you've come from, which which makes the GPT something you can't really have a conversation with that has no recollection of what you've already said.
*  Well, no, because OK, I'll say this.
*  There's a trick to this.
*  It's very beautiful.
*  So I'm going to tell it to you, which is that let's say you're doing a Markov chain on letters.
*  Well, what you do to be clever is you say, actually, my Markov chain is on strings of three letters.
*  So let's say if I'm like, if I see THA, if that's where my current state, probably the most likely the next letter is T, right?
*  Because I'm probably not saying like Thanos.
*  So I'm probably saying that.
*  That's a very common word I'm in the middle of.
*  But then your next state is not T.
*  It's HAT because you're walking on the space of three letter sequences and you're only allowed to lop off the first letter of your sequence and replace it with a new letter at the end.
*  So this business of memory, you can kind of build in a certain amount of memory just by enlarging your idea of what the state is.
*  This is a very clever idea.
*  And so GPT-3 or any language generation system like the auto complete in your Gmail is a little bit more than that.
*  And like, you know, look, I'm not confident to say what's inside the guts of GPT-3 because despite the company being called OpenAI, like we don't really know.
*  What's in it?
*  But it definitely has.
*  They've definitely worked hard to give it more long range memory.
*  Yeah.
*  And a sort of more very basic Markov chain based system.
*  That's part of what makes it cool.
*  And the important thing for the audience is that when they're texting and there's autocorrect or when they're doing Gmail and they're suggesting answers, that's a Markov chain at work for proposing those possible solutions to what comes next.
*  Right.
*  It's saying here's where you are now.
*  What's the most likely place you're going next?
*  Now, I don't know about you, but I always type something else when it starts to suggest something.
*  I'm certainly not going to say that now that you suggested it.
*  I'm my own man.
*  Yeah, but you're still part of the overall ensemble.
*  You know, like you're going to you're going to contribute to the expectation values at the end of the day.
*  I'm disrupting it because it's like, oh, I guess I was wrong about like, you know, I'm reducing its level of certainty of what it's doing.
*  I think the system takes into account.
*  That's that's my prediction.
*  But OK, so and then with these Markov chains, we have a way of generalizing the random walk.
*  And you can see how we're coming back to the gerrymandering, right, because we're going to have a Markov chain that represents where every place that you are represents a map.
*  And we're going to hop to a different map.
*  Right.
*  And then you can sort of once again, the space of different places you might hop to is enormously big.
*  But then you can start talking about the ensemble and its properties.
*  And there will be in general a favorite equilibrium distribution.
*  Right. There'll be, you know, I don't know, a set of probabilities.
*  Tell me what the equilibrium distribution is. What is the simplest way to characterize that?
*  So ideally, if you run the random walk for a long time, you will get to sort of some consistent answer to how much of your walk do you spend in each possible place on the map?
*  Now, in the case of the gerrymanders, you're probably not going to approach that distribution because you would have to run it so long that you conceivably see like every possible distribution, which we're probably not doing.
*  But a very, very well known place that does that is Google Pager Inc., which I think, you know, both of us are old enough to remember the incredible difference in how the Internet works.
*  There were search engines before Google, but they did not work the way Google works.
*  And what Google did was build the Markov chain into the process.
*  Basically, they did a random walk on the Internet, a very good abstract space that we like a lot.
*  You're on a page. You follow a random link from it. That's the walk.
*  We do that for a long time and you start to converge to a popular distribution.
*  There are sites you're hitting again and again. Which sites do you hit?
*  Well, it's you might say, well, it must be sites that have a lot of links to them.
*  So you're likely to get there. But it's not just that there's something recursive about it because you want the sites that link to it to themselves be sites that have a lot of links to them.
*  You know, if I just have like two random sites that have like a billion links to each other, I'm never going to get into that little closed ecosystem unless other people link to it.
*  So this process of random walk and then keeping track of what's this limiting distribution of how much how much portion of your time to spend at each place.
*  That's the basis of what Google called Pager Inc. back in the mid 90s when they developed this.
*  That is the order in which they serve you your search results.
*  And that absolutely revolutionized people's ability to find things because this limiting distribution, what the Markov chain finds for you and computes for you is it's somehow a global property of the system that is a very, very hard kind of an emergent property.
*  That's very, very hard to see any local way.
*  You just got to do the walk and see what happened.
*  And what they saw is that it does an incredibly good job of sort of capturing this notion, this human notion of importance or centrality or the search results that I actually want.
*  But for something like our maps, our gerrymandered maps or the maps that we were trying to show are not gerrymandered.
*  I think like you said, we don't have the computational power to sample every single map, much less keep coming back to the same map over and over again.
*  There's just too many of them.
*  So what is the thought that makes us say that some Markov chain is going to help us figure out what a typical map looks like?
*  Well, it helps us.
*  Well, as I say, we can't know for certain what a typical map looks like, but we can know what a typical map sort of like, you know, within a neighborhood of the starting map.
*  So, I mean, imagine a random walk is in some sense like sort of particles diffusing from a given source.
*  Like if you've seen any of the many newspaper articles with these incredibly terrifying COVID pictures of like what the spray of COVID particles from somebody's nose and mouth looks like, who's infected.
*  I mean, it's much denser near the person's head and then it rapidly gets less dense as you go farther away from the person.
*  So you should think of it like that.
*  You should think of it as like you may not be seeing like the entire universe, but you're getting a pretty good sample from the random walk.
*  Sort of like what's going on in the neighborhood of the map that you started with.
*  But again, the fact that we're not sort of converging to some of these distribution, it means we're not going to do what Google does.
*  We're not going to say I'm going to rank all maps for you and tell you which map is best, the most like the most random, the most likely to be hit.
*  But that's not that's not the goal.
*  The goal is not to tell you what to do.
*  The goal is to sort of tell you what not to do.
*  The goal is to sort of identify what an existing map is is completely an outlier.
*  So maybe the analog of that, I'm just making this up as I go.
*  Maybe the sort of Google analog would be that would be if I claim to you, hey, my homepage is the most important site on the Internet.
*  And you sort of and Google sort of started its random walk from there and walk like a billion steps and never found its way back there.
*  That would be a pretty good it wouldn't necessarily tell you like what was the most important site of the Internet, but it would definitely rule out that my homepage is the most important site of the Internet.
*  It would be like, come on, like I walked around for like a billion steps and I never found my way back there.
*  It can't be that important.
*  So what is the modern mathematical research level problem in the gerrymandering and Markov chain game?
*  Is it coming up with algorithms to do these random walks or is it or are we are we ever going to get ambitious enough to say, well, yeah, we think we actually can draw the maps as mathematicians.
*  Get out of the way, politicians.
*  But why would they agree to that?
*  Again, I'm not a politician either, so I'm not going to say they should agree to it.
*  But so what is the what are the mathematicians trying to do?
*  So I would say, I mean, there's a lot of questions and research in this area.
*  And I should I should emphasize, I am not one of the people doing this research.
*  I'm a popularizer of this research and I sort of I'm a conduit between, you know, between mathematicians and various lawyers and commissions that I've testified before, et cetera, et cetera.
*  So I would say some of the things people are doing are trying to get, like, you know, better provable guarantees about like maybe you don't know it's like 100 percent random or like sort of like can you get some kind of provable guarantees about how close to uniformly random you are.
*  Studying the properties of different choices of what the local moves are.
*  This is like very granular stuff, but it turns out to actually make a difference to how rapidly you converge to something that looks kind of uniform.
*  So this is kind of you might call it kind of an engineering problem of just being in practice, like what sort of version of the many local things you can do actually work.
*  I mean, something that I'm particularly interested in and I actually don't know the words that people are working on this.
*  But as you probably know, like around the country, there is a lot of appetite for an interest in reform of the basic voting mechanisms themselves.
*  I think there's a lot of work that has been done by the people and introduced like ranked choice voting in Maine and New York City.
*  I think in Austin today or something like that in Austin, Texas, I think they've just adopted something like this.
*  There's a really interesting proposal with some bipartisan support actually here in Wisconsin where the legislature hasn't done anything for like two years.
*  But maybe they'll do something that has some support for both parties.
*  I think a lot of the work in gerrymandering has really focused on conditions as they are conditions where we have the voting system we have and we have the two parties we have.
*  And we don't even ignore the existence of like candidates or voters who don't identify with one of those two parties.
*  Introducing fundamental changes and how the vote works like ranked choice voting is going to scramble this a lot, both for the people drawing gerrymandered maps and for the people trying to detect gerrymandered maps.
*  So one thing that just personally I'm interested in is trying to understand how this landscape changes with more variation in possible voting systems, which we're as I say, we're already starting to see.
*  And there are states. Well, there's one state, Maine, that has really like gone all in on this mechanism.
*  It'll be really interesting to see how things play out there.
*  But again, doing the work is going to be both math and political science and law like all mixed together.
*  If you try to do it with one discipline by itself, you can't do it.
*  We've said it before in the podcast. Why don't you just say what ranked choice voting is so the folks get an idea for why it would be an attractive thing to shoot for.
*  Oh, yeah. Sorry. Sometimes I get immersed in this voting stuff, but I forget that like most people probably to their psychic benefit like don't think about democracy maintenance all the time.
*  So ranked choice voting means that you don't just vote for one candidate and say this is the one I like best.
*  You rank all the candidates who are on the ballot in order of how much you would like them to hold the office.
*  And what that allows you to do is if you are somebody who doesn't identify strongly as a Democrat or a Republican and maybe even identifies with a third party,
*  that allows you to vote for that party's candidate while not giving up your right to express a preference between the Democrat and Republican, which you might well really have.
*  In fact, in the proposal in Wisconsin, they're talking about having ditching partisan primaries and just having open primary where all the Democrats and all the Republicans and all the libertarians and all the everybody and the unabiliates.
*  So in a situation like that, you probably would have a general election with multiple candidates.
*  You might have two Democrats and two Republicans and a fifth person, for example.
*  And then I think, again, I can't do it by myself as mathematician.
*  We need political scientists to weigh in.
*  But intuitively, you feel like it scrambles things up and gives people more choices in a political arena, which is a lot of people think about.
*  Which frankly, just listening to people talk when you go to these commissions, a lot of people are pretty frustrated with the choices that they have.
*  Do you think that there is some future collaboration between political scientists and mathematicians where you are very ambitious and say, look, let's try to think about what are the goals that we have in electing people in sort of core screening, the internet, the internet, the internet, the internet.
*  Look, let's try to think about what are the goals that we have in electing people in sort of core screening, the individuals in our society into a legislator, legislature and try to figure out a priori or, you know, albedicio.
*  I should say, what is the best voting system that would reflect the actual will of the people?
*  Is that too utopian?
*  I mean, people are going to work on it, whether you think it's too utopian or not.
*  There's nothing too utopian for people to think about.
*  No, I think that those kinds of discussions already are happening and have been happening.
*  Look, like go all the way back to Arrow's theorem.
*  There's like lots of interesting kind of like mathematical formalisms about not just how voting, not just analysis of existing voting, but like how voting could work.
*  Right. So that's a pretty old idea.
*  So what I would say, maybe this is a good opportunity because one thing I just thought of that certainly Mnuchin has told me is that, you know, they see these techniques not just as a way to sort of like give meaningful testimony in court about a particular political question that's happening in the moment, but as a sort of new kind of tech for doing social science research in the same way that in physics, now I'm going to talk about physics, so please tell me if I say something like completely off base.
*  I mean, people use Monte Carlo simulations all the time to sort of simulate and try to understand what the effect of doing a certain thing would be in a situation where for various reasons they can't actually experiment.
*  Isn't that a thing?
*  Oh, absolutely.
*  They do.
*  I mean, I went to a great seminar of like a guy who's like, well, we're sort of trying to figure out things about like atomic weapons, but we are not, you know, we don't just like drop atomic bombs on places where we think not too many people live or not too many people who are important to us live anymore.
*  Like that's not how we test anymore.
*  Like a lot of it is like, you know, simulations based on like pretty hardcore numerical analysis, but also Monte Carlo techniques.
*  So I think that at least some of the people in this area envision a world in which, you know, also in political science, like experiments are like hard to do and often ethically questionable, right?
*  So maybe this is too utopian, but I mean, there is an idea of like we can at least get some good ideas about what the results of sort of different kinds of voting systems would look like from simulations of this kind.
*  And maybe to wrap up on a less utopian note, because I know that, you know, as scientists and mathematicians, we like to be utopian.
*  But as you emphasize very, very properly, politicians feed on the ground have a different set of values and different set of cares.
*  So one of the things you mentioned very briefly, which intrigued me was the idea of inventing schemes by which you can admit that the map will be drawn by a legislature, not by an independent commission.
*  And yet inventing schemes where sort of like for two kids trying to slice up the pie, they are driven toward a more or less equitable outcome.
*  Yeah, I mean, so this is sort of like a famous, there's a very famous problem called the cake cutting problem.
*  It is a very elegant answer. Like, how do you how do you cut a cake fairly into two pieces between two people who both want to eat and both like cake and want a lot of cake?
*  And, you know, the way you do this is you have one kid cut and the other kid chooses.
*  So the kid who somehow this iterative process, we separated into steps, somehow sort of creates an incentive to like, make the division roughly fair.
*  And then there's like an entire literature of like, how do you do this if there's three kids and three pieces, four kids and four pieces, like, you know, multiple kids who may be able to choose a subset of pieces, whatever, like map positions once we have something to generalize that.
*  But so, yeah, so one thing that people have discussed is could there be a protocol where you make a game out of gerrymandering?
*  Like, you start with some map, but then the parties take turns. I'll change it this way. Now I'll change it. Now I'll change it.
*  I'll take each team sort of tried to make it maybe presumably trying to make it more favorable to their party.
*  Now, actually, you have to be a little careful on the people who write about this. There's more complicated protocols than what I just said to make it even possibly work.
*  But the idea is that the reason this might be useful, I haven't decided if I think it's practically useful, but the reason that might be useful is that because these it's precisely because these highly gerrymandered maps are so special and they're so unusual in their own neighborhood.
*  They represent this kind of local apex of partisan advantage. So imagine if there's like two kids wrestling on top of a mountain and one kid is trying to get you to the top of the mountain and one kid is trying to get you off the peak.
*  Well, there's a lot more non-peak than peak. So the two kids kind of take turns pushing each other. They're not going to stay at the peak. They're going to be like somewhere else that's like much farther down.
*  So I think this is like some but I was here to come back to something we said at the very beginning that the current mechanism makes it so easy to do so much to cement your partisan advantage that almost any disruptive change I think would be much more likely to improve the situation than to make it worse.
*  So this is a rare example where entropy is working in our favor.
*  Kick the TV. That's what I said. Kick the TV and it's going to start working again, or at least will work better than it works now.
*  I like that message. Thanks so much. Jordan Ellenberg, thanks very much for being on the Mindscape Podcast.
*  Oh, thanks for having me. This was great.
*  Thanks for having me.

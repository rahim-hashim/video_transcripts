---
Date Generated: April 12, 2024
Transcription Model: whisper medium 20231117
Length: 10376s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'computer science', 'cyc', 'cycorp', 'douglas lenat', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'machine learning', 'mit ai', 'stanford', 'stanford university']
Video Views: 124655
Video Rating: None
---

# Douglas Lenat: Cyc and the Quest to Solve Common Sense Reasoning in AI | Lex Fridman Podcast #221
**Lex Fridman:** [September 15, 2021](https://www.youtube.com/watch?v=3wMKoSRbGVs)
*  The following is a conversation with Doug Lennett, creator of Psych, a system that for close to 40 years and still today has sought to solve the core problem of artificial intelligence, the acquisition of common sense knowledge and the use of that knowledge to think, to reason, and to understand the world.
*  To support this podcast, please check out our sponsors in the description.
*  As a side note, let me say that in the excitement of the modern era of machine learning, it is easy to forget just how little we understand exactly how to build the kind of intelligence that matches the power of the human mind.
*  To me, many of the core ideas behind Psych, in some form, in actuality or in spirit, will likely be part of the AI system that achieves general superintelligence.
*  But perhaps more importantly, solving this problem of common sense knowledge will help us humans understand our own minds, the nature of truth, and finally, how to be more rational and more kind to each other.
*  This is the Lex Friedman Podcast, and here is my conversation with Doug Lennett.
*  Psych is a project launched by you in 1984 and still is active today, whose goal is to assemble a knowledge base that spans the basic concepts and rules about how the world works.
*  In other words, it hopes to capture common sense knowledge, which is a lot harder than it sounds.
*  Can you elaborate on this mission and maybe perhaps speak to the various sub-goals within this mission?
*  When I was a faculty member in the computer science department at Stanford, my colleagues and I did research in all sorts of artificial intelligence programs.
*  So natural language understanding programs, robots, expert systems, and so on.
*  And we kept hitting the very same brick wall.
*  Our systems would have impressive early successes.
*  And so if your only goal was academic, namely to get enough material to write a journal article, that might actually suffice.
*  But if you're really trying to get AI, then you have to somehow get past the brick wall.
*  The brick wall was the programs didn't have what we would call common sense.
*  They didn't have general world knowledge.
*  They didn't really understand what they were doing, what they were saying, what they were being asked.
*  And so very much like a clever dog performing tricks, we could get them to do tricks, but they never really understood what they were doing, sort of like when you get a dog to fetch your morning newspaper.
*  The dog might do that successfully, but the dog has no idea what a newspaper is or what it says or anything like that.
*  What does it mean to understand something? Can you maybe elaborate on that a little bit?
*  Is it is understand an action of like combining little things together like through inference or is understanding the wisdom you gain over time that forms a knowledge?
*  I think of understanding more like a think of it more like the ground you stand on, which could be very shaky, could be very unsafe.
*  But most of the time is not because underneath it is more ground and eventually rock and other things.
*  But layer after layer after layer, that solid foundation is there and you rarely need to think about it.
*  You rarely need to count on it, but occasionally you do.
*  And I've never used this analogy before, so bear with me.
*  But I think the same thing is true in terms of getting computers to understand things, which is you ask a computer a question, for instance, Alexa or some robot or something.
*  And maybe it gets the right answer.
*  But if you were asking that of a human, you could also say things like why or how might you be wrong about this or something like that.
*  And the person would answer you.
*  And it might be a little annoying if you have a small child and they keep asking why questions in series.
*  Eventually you get to the point where you throw up your hands and say, I don't know, it's just the way the world is.
*  But for many layers, you actually have that layered solid foundation of support so that when you need it, you can count on it.
*  And when do you need it?
*  Well, when things are unexpected, when you come up against a situation which is novel, for instance, when you're driving, it may be fine to have a small program,
*  a small set of rules that cover 99% of the cases.
*  But that 1% of the time when something strange happens, you really need to draw on common sense.
*  For instance, my wife and I were driving recently and there was a trash truck in front of us.
*  And I guess they had packed it too full and the back exploded and trash bags went everywhere.
*  And we had to make a split second decision.
*  Are we going to slam on our brakes?
*  Are we going to swerve into another lane?
*  Are we going to just run it over?
*  Because there were cars all around us.
*  And in front of us was a large trash bag.
*  And we know what we throw away in trash bags, probably not a safe thing to run over.
*  Over on the left was a bunch of fast food restaurant trash bags.
*  And it's like, oh, well, those things are just like styrofoam and leftover food.
*  We'll run over that.
*  And so that was a safe thing for us to do.
*  Now, that's the kind of thing that's going to happen maybe once in your life.
*  But the point is that there's almost no telling what little bits of knowledge about the world you might actually need in some situations which were unforeseen.
*  But see, when you sit on that mountain or that ground that goes deep of knowledge in order to make a split second decision about fast food trash or random trash from the back of a trash truck, you need to be able to leverage that ground you stand on in some way.
*  It's not merely, you know, it's not enough to just have a lot of ground to stand on.
*  It's your ability to leverage it, to utilize it in a split, like integrated all together to make that split second decision.
*  And I suppose understanding isn't just having common sense knowledge to access.
*  It's the act of accessing accessing it somehow like correctly filtering out the parts of the knowledge are not useful, selecting only the useful parts.
*  And effectively making conclusive decisions.
*  So let's tease apart two different tasks really, both of which are incredibly important and even necessary.
*  If you're going to have this in a usable, useful, usable fashion as opposed to say like library books sitting on a shelf and so on, where the knowledge might be there.
*  But, you know, if a fire comes, the books are going to burn because they don't know what's in them and they're just going to sit there while they burn.
*  So there are two aspects of using the knowledge.
*  One is a kind of a theoretical. How is it possible at all?
*  And then the second aspect of what you said is how can you do it quickly enough?
*  So how can you do it at all is something that philosophers have grappled with.
*  And fortunately, philosophers a hundred years ago and even earlier developed a kind of formal language like English.
*  It's called predicate logic or first order logic or something like predicate calculus and so on.
*  So there's a way of representing things in this formal language, which enables a mechanical procedure to sort of grind through and algorithmically produce all of the same logical entailments, all the same logical conclusions that you or I would from that same set of pieces of information that are represented that way.
*  So that that sort of raises a couple of questions.
*  One is how do you get all this information from say observations and English and so on into this logical form?
*  And secondly, how can you then efficiently run these algorithms to actually get the information you need in the case I mentioned in a tenth of a second rather than say in 10 hours or 10,000 years of computation?
*  And those are both really important questions.
*  And like a corollary addition to the first one is how many such things do you need to gather for it to be useful in certain contexts?
*  So like what in order you mentioned philosophers in order to capture this world and represent it in a logical way and with a formal logic like how many statements are required?
*  Is it five? Is it 10? Is it 10 trillion? Is it like that?
*  That's as far as I understand is probably still an open question.
*  It may forever be an open question to say definitively about to describe the universe perfectly.
*  Well, I guess I'm going to disappoint you by giving you an actual answer to your question.
*  OK, well, no, it sounds exciting.
*  Yes. OK.
*  OK, so now we have like three three things to talk about.
*  We'll keep adding more.
*  Although it's OK. The first and the third are related.
*  Yes. So let's leave the efficiency question aside for now.
*  So how does all this information get represented in logical form so that these algorithms resolution theorem proving and other algorithms can actually grind through all the logical consequences of what you said?
*  And that ties into your question about how many of these things do you need?
*  Because if the answer is small enough, then by hand, you could write them out one at a time.
*  So in the 19 early 1984, I held a meeting at Stanford where I was a faculty member there where we assembled about half a dozen of the smartest people I know, people like Alan Newell and Marvin Minsky and Alan Kay and a few others.
*  Was Feynman there by chance? Because he he liked your he commented about your system, you risk go at the time.
*  No, no, he wasn't part of this meeting.
*  But that's a heck of a meeting anyway.
*  I think Ed Feigenbaum was there. I think Josh Lederberg was there.
*  So we have all these different smart people and we were we came together to address the question that you raised, which is if it's important to represent common sense knowledge and world knowledge in order for AIs to not be brittle, in order for AIs not to just have the veneer of intelligence.
*  Well, how many pieces of common sense, how many if then rules, for instance, would we have to actually write in order to essentially cover what what people expect perfect strangers to already know about the world?
*  And I expected there would be an enormous divergence of opinion and computation.
*  But amazingly, everyone got an answer which was around a million.
*  And one person one person got the answer by saying, well, look, you can only burn into human long term memory, a certain number of things per unit time, like maybe one every 30 seconds or something.
*  And other than that, it's just short term memory and it flows away like water and so on.
*  So by the time you're say 10 years old or so, how many things could you possibly have burned into your long term memory?
*  And it's like about a million.
*  Another person went in a completely different direction and said, well, if you look at the number of words in a dictionary, not a whole dictionary, but for someone to essentially be considered to be fluent in a language, how many words would they need to know?
*  And then about how many things about each word would you have to tell it?
*  So they got to a million that way.
*  Another another person said, well, let's actually look at one single short one volume desk encyclopedia article.
*  And so we'll look at what was like a four paragraph article or something.
*  I think about Grebes.
*  Grebes are a type of waterfowl.
*  And if we were going to sit there and represent every single thing that was there, how many assertions or rules or statements would we have to write in this logical language?
*  And so and then multiply that by all of the number of articles that there were and so on.
*  So all of these estimates came out with a million.
*  And so if you do the math, it turns out that like, oh, well, then maybe in something like a hundred person years in one or two person centuries, we could actually get this written down by hand.
*  And a marvelous coincidence, opportunity existed right at that point in time, the early 1980s.
*  There was something called the Japanese fifth generation computing effort.
*  Japan had threatened to do in computing and A.I. and hardware, but they had just finished doing in consumer electronics and the automotive industry, namely resting control away from the United States and more generally away from the West.
*  And so America was scared.
*  And Congress did something.
*  That's how you know it was a long time ago, because Congress did something.
*  Congress passed something called the National Cooperative Research Act in C.R.A.
*  And what it said was, hey, all you big American companies.
*  That's also how you know it was a long time ago, because they were American companies rather than multinational companies.
*  Hey, all you big American companies.
*  Normally it would be an antitrust violation if you colluded on R.N.D.
*  But we promise for the next 10 years, we won't prosecute any of you if you do that to help combat this threat.
*  And so overnight, the first two consortia research consortia in America sprang up, both of them coincidentally in Austin, Texas, one called Semitech focusing on hardware chips and so on.
*  And then one called MCC, the Microelectronics and Computer Technology Corporation, focusing more on software, on databases and A.I. and natural language understanding and things like that.
*  And I got the opportunity, thanks to my friend Woody Bledsoe, who was one of the people who founded that, to come and be its principal scientist.
*  And he sent Admiral Bob Inman, who was the person running MCC, came and talked to me and said, look, professor, you're talking about doing this project.
*  It's going to involve person centuries of effort.
*  You've only got a handful of graduate students.
*  You do the math.
*  It's going to take you longer than the rest of your life to finish this project.
*  But if you move to the wilds of Austin, Texas, we'll put 10 times as many people on it and you'll be done in a few years.
*  And so that was pretty exciting.
*  And so I did that.
*  I took my leave from Stanford.
*  I came to Austin.
*  I worked for MCC.
*  And the good news and bad news, the bad news is that all of us were off by an order of magnitude.
*  That it turns out what you need are tens of millions of these pieces of knowledge about every day, sort of like if you have a coffee cup with stuff in it and you turn it upside down, the stuff in it's going to fall out.
*  So you need tens of millions of pieces of knowledge like that, even if you take trouble to make each one as general as it possibly could be.
*  But the good news was that thanks to initially the fifth generation effort and then later US government agency funding and so on, we were able to get enough funding not for a couple person centuries of time, but for a couple person millennia of time, which is what we've spent since 1984.
*  Getting psych to contain the tens of millions of rules that it needs in order to really capture and span sort of not all of human knowledge, but the things that you assume other people know, the things you count on other people knowing.
*  And so by now we've done that.
*  And the good news is since you've waited 38 years just about to talk to me, we're about at the at the end of that process.
*  So most of what we're doing now is not putting in even what you would consider common sense, but more putting in domain specific applications, specific knowledge about health care in a certain hospital or about oil pipes getting clogged up or whatever the applications happen to be.
*  So we've almost come full circle and we're doing things very much like the expert systems of the 1970s and the 1980s, except instead of resting on nothing and being brittle, they're now resting on this massive pyramid, if you will, this massive lattice of common sense knowledge so that when things go wrong, when something unexpected happens, they can fall back on more and more and more general principles.
*  Eventually bottoming out in things like, for instance, if we have a problem with the microphone, one of the things you'll do is unplug it, plug it in again and hope for the best.
*  Right. Because that's one of the general pieces of knowledge you have in dealing with electronic equipment or software systems or things like that.
*  Is there a basic principle like that? Like, is there is it possible to encode something that generally captures this idea of turn it off and turn it back on and see if it fixes?
*  Oh, absolutely. That's one of the things that that's like knows.
*  That's actually one of the fundamental laws of nature.
*  I wouldn't I wouldn't call it a law. It's it's more like a seems to work every time. So it's sure sure. Looks like a law. I don't know.
*  So that that basically covered the the resources needed.
*  And then we had to devise a method to actually figure out, well, what are the tens of millions of things that we need to tell the system?
*  And for that, we found a few techniques which worked really well.
*  One is to take any piece of text almost could be an advertisement, could be a transcript, it could be a novel, it could be an article.
*  And don't pay attention to the actual type that's there.
*  The the black space on the white page. Pay attention to the complement of that.
*  The white space, if you will. So what did the writer of this sentence assume that the reader already knew about the world?
*  For instance, if they used a pronoun, how did they figure out that?
*  Why did they think that you would be able to understand what the intended referent of that pronoun was?
*  If they used an ambiguous word, how did they think that you would be able to figure out what they meant by that word?
*  The other thing we look at is the gap between one sentence and the next one.
*  What are all the things that the writer expected you to fill in and infer occurred between the end of one sentence and the beginning of the other?
*  So like if the sentence says, Fred Smith robbed the Third National Bank period,
*  he was sentenced to 20 years in prison period.
*  Well, between the first sentence and the second, you're expected to infer things like Fred got caught,
*  Fred got arrested, Fred went to jail, Fred had a trial, Fred was found guilty, and so on.
*  If my next sentence starts out with something like the judge, then you assume it's the judge at his trial.
*  If my next sentence starts out something like the arresting officer, you assume that it was the police officer who arrested him after he committed the crime and so on.
*  So those are two techniques for getting that knowledge.
*  The other thing we sometimes look at is sort of like fake news or sort of humorous onion headlines or headlines in the Weekly World News,
*  if you know what that is, or the National Enquirer, where it's like, oh, we don't believe this, then we introspect on why don't we believe it.
*  So there are things like B-17 lands on the moon.
*  It's like, what do we know about the world that causes us to believe that that's just silly or something like that?
*  Or another thing we look for are contradictions, things which can't both be true.
*  And we say, what is it that we know that causes us to know that both of these can't be true at the same time?
*  For instance, in one of the Weekly World News editions, in one article it talked about how Elvis was cited, even though he was getting on in years and so on.
*  And another article in the same one talked about people seeing Elvis as ghost.
*  OK, so it's like, why do we believe that at least one of these articles must be wrong and so on?
*  So we have a series of techniques like that that enable our people.
*  And by now we have about 50 people working full time on this and have for decades.
*  So we've put in the thousands of person years of effort. We've built up these tens of millions of rules.
*  We constantly police the system to make sure that we're saying things as generally as we possibly can.
*  So you don't want to say things like, no mouse is also a moose.
*  Because if you said things like that, then you'd have to add another one or two or three zeros onto the number of assertions you'd actually have to have.
*  So at some point we generalize things more and more and we get to a point where we say, oh, yeah, for any two biological taxons,
*  if we don't know explicitly that one is a generalization of another, then almost certainly they're disjoint.
*  A member of one is not going to be a member of the other and so on.
*  And the same thing with Elvis and the ghost. It has nothing to do with Elvis.
*  It's more about human nature and the mortality and that kind of stuff.
*  Well, in general, things are not both alive and dead at the same time.
*  Yeah. Unless special cats in theoretical physics examples.
*  Well, that raises a couple of important points.
*  Well, that's the onion headline situation. Okay, sorry.
*  But no, no. So what you bring up is this really important point of like, well, how do you handle exceptions and inconsistencies and so on?
*  And one of the hardest lessons for us to learn, it took us about five years to really grit our teeth and learn to love it,
*  is we had to give up global consistency. So the knowledge base can no longer be consistent.
*  So this is a kind of scary thought. I grew up watching Star Trek and anytime a computer was inconsistent,
*  it would either freeze up or explode or take over the world or something bad would happen.
*  Or if you come from a mathematics background, once you can prove false, you can prove anything. So that's not good and so on.
*  So that's why the old knowledge-based systems were all very, very consistent.
*  But the trouble is that by and large our models of the world, the way we talk about the world and so on,
*  there are all sorts of inconsistencies that creep in here and there that will sort of kill some attempt to build some enormous globally consistent system.
*  Knowledge base. And so what we had to move to was a system of local consistency.
*  So a good analogy is, you know that the surface of the earth is more or less spherical globally,
*  but you live your life every day as though the surface of the earth were flat.
*  When you're talking to someone in Australia, you don't think of them as being oriented upside down to you.
*  When you're planning a trip, even if it's a thousand miles away, you may think a little bit about time zones,
*  but you rarely think about the curvature of the earth and so on.
*  And for most purposes, you can live your whole life without really worrying about that because the earth is locally flat.
*  In much the same way, the psych knowledge base is divided up into almost like tectonic plates, which are individual contexts.
*  And each context is more or less consistent, but there can be small inconsistencies at the boundary between one context and the next one and so on.
*  And so by the time you move, say, 20 contexts over, there could be glaring inconsistencies.
*  So eventually you get from the normal modern real world context that we're in right now to something like road runner cartoon context where physics is very different.
*  And in fact, life and death are very different because no matter how many times he's killed, the coyote comes back in the next scene and so on.
*  So that was a hard lesson to learn.
*  And we had to make sure that our representation language, the way that we actually encode the knowledge and represent it,
*  was expressive enough that we could talk about things being true in one context and false in another, things that are true at one time and false in another,
*  things that are true, let's say, in one region like one country, but false in another, things that are true in one person's belief system,
*  but false in another person's belief system, things that are true at one level of abstraction and false at another.
*  For instance, at one level of abstraction, you think of this table as a solid object, but down at the atomic level, it's mostly empty space and so on.
*  So then that's fascinating, but it puts a lot of pressure on context to do a lot of work.
*  So you say tectonic plates. Is it possible to formulate contexts that are general and big, that do this kind of capture of knowledge bases?
*  Or do you then get turtles on top of turtles again where there's just a huge number of contexts?
*  So it's good you asked that question because you're pointed in the right direction,
*  which is you want context to be first class objects in your system's knowledge base, in particular in psych's knowledge base.
*  And by first class object, I mean that we should be able to have psych think about and talk about and reason about one context or another context
*  the same way it reasons about coffee cups and tables and people and fishing and so on.
*  And so context are just terms in its language, just like the ones I mentioned.
*  And so psych can reason about context, context can arrange hierarchically and so on.
*  And so you can say things about, let's say, things that are true in the modern era,
*  things that are true in a particular year would then be a subcontext of the things that are true in a broad, let's say a century or a millennium or something like that.
*  Things that are true in Austin, Texas are generally going to be a specialization of things that are true in Texas,
*  which is going to be a specialization of things that are true in the United States and so on.
*  And so you don't have to say things over and over again at all these levels.
*  You just say things at the most general level that it applies to.
*  And you only have to say it once and then it essentially inherits to all these more specific contexts.
*  To ask a slightly technical question, is this inheritance a tree or a graph?
*  Oh, you definitely have to think of it as a graph.
*  So we could talk about, for instance, why the Japanese fifth generation computing effort failed.
*  There were about half a dozen different reasons.
*  One of the reasons they failed was because they tried to represent knowledge as a tree rather than as a graph.
*  And so each node in their representation could only have one parent node.
*  So if you had a table that was a wooden object, a black object, a flat object, and so on, you had to choose one.
*  And that's the only parent it could have.
*  When, of course, depending on what it is you need to reason about it, sometimes it's important to know that it's made out of wood,
*  like if we're talking about a fire.
*  Sometimes it's important to know that it's flat if we're talking about resting something on it and so on.
*  So one of the problems was that they wanted a kind of dewy decimal numbering system for all of their concepts,
*  which meant that each node could only have at most 10 children and each node could only have one parent.
*  And while that does enable the dewy decimal type numbering of concepts, labeling of concepts,
*  it prevents you from representing all the things you need to about objects in our world.
*  And that was one of the things which they never were able to overcome.
*  And I think that was one of the main reasons that that project failed.
*  So we'll return to some of the doors you've opened.
*  But if we can go back to that room in 1984 around there with Marvin Minsky and Stanford.
*  By the way, I should mention that Marvin wouldn't do his estimate until someone brought him an envelope
*  so that he could literally do a back of the envelope calculation to come up with his number.
*  Well, because I feel like the conversation in that room is an important one.
*  You know, this is how sometimes science is done in this way.
*  A few people get together and plant the seed of ideas and they reverberate throughout history.
*  And some kind of dissipate and disappear and some Drake equation and they, you know,
*  it seems like a meaningless equation, somewhat meaningless.
*  But I think it drives and motivates a lot of scientists.
*  And when the aliens finally show up, that equation will get even more valuable
*  because then we'll be able to, in the long arc of history,
*  the Drake equation will prove to be quite useful, I think.
*  And in that same way, a conversation of just how many facts are required to capture
*  the basic common sense knowledge of the world.
*  That's a fascinating question.
*  I want to distinguish between what you think of as facts and the kind of things that we represent.
*  So we map to and essentially make sure that psych has the ability to, as it were, read and access
*  the kind of facts you might find, say, in Wikidata or stated in a Wikipedia article or something like that.
*  So what we're representing, the things that we need a small number of tens of millions of,
*  are more like rules of thumb, rules of good guessing.
*  Things which are usually true and which help you to make sense of the facts
*  that are sitting off in some database or some other more static stories.
*  They're almost like platonic forms.
*  So when you read stuff on Wikipedia, that's going to be projections of those ideas.
*  You read an article about the fact that Elves died, that's a projection of the idea that humans are mortal.
*  Very few Wikipedia articles will write humans are mortal.
*  Exactly. That's what I meant about ferreting out the unstated things in text.
*  What are all the things that were assumed?
*  And so those are things like if you have a problem with something, turning it off and on often fixes it
*  for reasons we don't really understand and we're not happy about.
*  Or people can't be both alive and dead at the same time.
*  Or water flows downhill.
*  If you search online for water flowing uphill and water flowing downhill,
*  you'll find more references for water flowing uphill because it's used as a kind of a metaphorical reference
*  for some unlikely thing because of course everyone already knows that water flows downhill.
*  So why would anyone bother saying that?
*  Do you have a word you prefer? Because we said facts isn't the right word.
*  Is there a word like concepts?
*  I would say assertions. Assertions or rules.
*  Because I'm not talking about rigid rules, but rules of thumb.
*  But assertions is a nice one that covers all of these things.
*  Yeah. As a programmer to me assert has a very dogmatic authoritarian feel to them.
*  Oh, I'm sorry.
*  I'm so sorry. Okay, but assertions works.
*  Okay, so if we go back to that room with Marvin Minsky with you, all these seminal figures.
*  Yeah. Ed Fagimam.
*  Thinking about this very philosophical but also engineering question.
*  We can also go back a couple of decades before then and thinking about artificial intelligence broadly
*  when people were thinking about how do you create superintelligence systems, general intelligence.
*  And I think people's intuition was off at the time.
*  And I mean this continues to be the case that we're not, when we're grappling with these exceptionally difficult ideas,
*  we're not always, it's very difficult to truly understand ourselves.
*  When we're thinking about the human mind to introspect how difficult it is to engineer intelligence, to solve intelligence.
*  We're not very good at estimating that.
*  And you are somebody who has really stayed with this question for decades.
*  Do you, what's your sense from 1984 to today?
*  Have you gotten a stronger sense of just how much knowledge is required?
*  You've kind of said with some level of certainty that it's still on the order of magnitude of tens of millions.
*  Right. For the first several years, I would have said that it was on the order of one or two million.
*  And so it took us about five or six years to realize that we were off by a factor of ten.
*  But I guess what I'm asking, you know, Marvin Miske is very confident in the 60s when you say it.
*  Yes. Right. What's your sense?
*  If you, you know, 200 years from now, you're still, you know, you're not going to be any longer in this particular biological body,
*  but your brain will still be in the digital form and you'll be looking back, would you think you were smart today?
*  Like your intuition was right. Or do you think you may be really off?
*  So I think I'm right enough. And let me explain what I mean by that, which is sometimes like if you have an old fashioned pump,
*  you have to prime the pump and then eventually it starts.
*  So I think I'm right enough in the sense that what we've built, even if it isn't, so to speak, everything you need,
*  it's primed the knowledge pump enough that psych can now itself help to learn more and more automatically on its own
*  by reading things and understanding and occasionally asking questions like a student would or something.
*  And by doing experiments and discovering things on its own and so on.
*  So through a combination of psych powered discovery and psych powered reading, it will be able to bootstrap itself.
*  Maybe it's the final 2%. Maybe it's the final 99%.
*  So even if I'm wrong, all I really need to build is a system which has primed the pump enough that it can begin that cascade upward,
*  that self-reinforcing sort of quadratically or maybe even exponentially increasing path upward that we get from, for instance,
*  talking with each other. That's why humans today know so much more than humans 100,000 years ago.
*  We're not really that much smarter than people were 100,000 years ago.
*  But there's so much more knowledge and we have language and we can communicate. We can check things on Google and so on.
*  So effectively, we have this enormous power at our fingertips.
*  And there's almost no limit to how much you could learn if you wanted to because you've already gotten to a certain level of understanding of the world
*  that enables you to read all these articles and understand them, that enables you to go out and if necessary, do experiments,
*  although that's slower as a way of gathering data and so on.
*  And I think this is really an important point, which is if we have artificial intelligence, real general artificial intelligence,
*  human level artificial intelligence, then people will become smarter.
*  It's not so much that it'll be us versus the AIs. It's more like us and the AIs together will be able to do things that require more creativity
*  that would take too long right now, but we'll be able to do lots of things in parallel.
*  We'll be able to misunderstand each other less.
*  There's all sorts of value that effectively for an individual would mean that individual will for all intents and purposes be smarter.
*  And that means that humanity as a species will be smarter.
*  And when was the last time that any invention qualitatively made a huge difference in human intelligence?
*  You have to go back a long ways. It wasn't like the Internet or the computer or mathematics or something.
*  It was all the way back to the development of language.
*  We sort of look back on pre-linguistic cavemen as well.
*  They weren't really intelligent, were they? They weren't really human, were they?
*  And I think that, as you said, 50, 100, 200 years from now, people will look back on people today.
*  Right before the advent of these sort of lifelong general AI uses and say, you know, those poor people, they weren't really human, were they?
*  Exactly. So you said a lot of really interesting things.
*  By the way, I would maybe try to argue that the Internet is on the order of the kind of big leap in improvement that the invention of language was.
*  Well, it's certainly a big leap in one direction. We're not sure whether it's upward or downward.
*  Well, I mean, very specific parts of the Internet, which is access to information like a website like Wikipedia,
*  like ability for human beings from across the world to access information very quickly.
*  So I could take either side of this argument. And since you just took one side, I'll give you the other side, which is that almost nothing has done more harm than something like the Internet and access to that information in two ways.
*  One is it's made people more globally ignorant in the same way that calculators made us more or less enumerate.
*  So when I was growing up, we had to use slide rules. We had to be able to estimate and so on.
*  Today, people don't really understand numbers. They don't really understand math. They don't really estimate very well at all and so on.
*  They don't really understand the difference between trillions and billions and millions and so on very well because calculators do that all for us.
*  And thanks to things like the Internet and search engines, that same kind of juvenileism is reinforced in making people essentially be able to live their whole lives, not just without being able to do arithmetic and estimate,
*  but now without actually having to really know almost anything because any time they need to know something, they'll just go and look it up.
*  And I could tell you could play both sides of this. And it is a double-edged sword. You can, of course, say the same thing about language.
*  Probably people when they invented language, they would criticize, you know, used to be we would just if we're angry, we would just kill a person.
*  And if we're in love, we would just have sex with them. And now everybody's writing poetry and bullshit that, you know, you should just be direct.
*  You should like have physical contact. Enough of this words and books. And it's you're you're not actually experiencing like if you read a book, you're not experiencing the thing.
*  This is nonsense. That's right. If you read a book about how to make butter, that's not the same as you had to learn it and do it yourself and so on.
*  So so let's just say that something is gained, but something is lost every time you have these these sorts of dependencies on technology.
*  And overall, I think that having smarter individuals and having smarter A.I.
*  augmented human species will be one of the few ways that we'll actually be able to overcome some of the global problems we have involving poverty and starvation and global warming and
*  overcrowding all the other problems that that are besetting the planet.
*  We really need to be smarter. And there really only two routes to being smarter.
*  One is through biochemistry and genetics, genetic engineering.
*  The other route is through having general A.I.s that augment our intelligence and, you know, hopefully one of those two ways of paths to salvation will will come through before it's too late.
*  Yeah, so I agree with you. And obviously, as an engineer, I have I have a better sense and an optimism about the technology side of things because you can control things there more.
*  And biology is just such a giant mess. We're living through a pandemic now.
*  There's so many ways that nature can just be just destructive and destructive in a way where it doesn't even notice you.
*  You know, it's not like a battle of humans versus viruses.
*  Just like, huh, OK. And then you can just wipe out an entire species.
*  Another problem with the Internet is that it has enabled us to surround ourselves with an echo chamber, with a bubble of like minded people, which means that you can have truly bizarre theories, conspiracy theories, fake news and so on promulgate
*  and surround yourself with people who essentially reinforce what you want to believe or what you already believe about the world.
*  And in the in the old days, that was much harder to do when you had, say, only three TV networks or even before when you had no TV networks and you had to actually like look at the world and make your own reason decisions.
*  I like the push and pull of our dance that we're doing, because then I'll just say in the old world, having come from the Soviet Union, because you had one or a couple of networks, then propaganda could be much more effective.
*  And then the government can overpower its people by telling you the truth and then starving millions and torturing millions and putting millions into camps and starting wars with a propaganda machine, allowing you to believe that you're actually doing good in the world.
*  With the Internet, because of all the quote unquote conspiracy theories, some of them are actually challenging the power centers, the very kind of power centers that a century ago would have led to the death of millions.
*  So there's a it's again this double edged sword. And I very much agree with you on the A.I. side.
*  It's it's often an intuition that people have that somehow A.I. will be used to maybe overpower people by certain select groups.
*  And to me, it's not at all obvious that that's the likely scenario to me, the likely scenario, especially just having observed the trajectory of technology is it'll be used to empower people.
*  It'll be used to extend the capabilities of individuals across the world because there's a lot of money to be made that way.
*  Like improving people's lives, you can make a lot of money.
*  I agree. I think that the the main the main thing that A.I. prostheses, A.I. amplifiers will do for people is make it easier, maybe even unavoidable for them to do good critical thinking.
*  So pointing out logical fallacies, logical contradictions and so on in things that they otherwise would just blithely believe, pointing out essentially data which they should take into consideration if they really want to learn the truth about something and so on.
*  So I think doing not just educating in the sense of pouring facts into people's heads, but educating in the sense of arming people with the ability to do good critical thinking is enormously powerful.
*  The education system that we have in the U.S. and worldwide generally don't do a good job of that.
*  But I believe that the A.I. will, the A.I.'s will, the A.I.'s can and will in the same way that everyone can have their own Alexa or Siri or Google Assistant or whatever.
*  Everyone will have this sort of cradle to grave assistant which will get to know you, which you'll get to trust.
*  It'll model you, you'll model it, and it'll call to your attention things which will in some sense make your life better, easier, less mistake ridden and so on, less regret ridden if you listen to it.
*  Yeah, I'm in full agreement with you about this space of technology and I think it's super exciting.
*  From my perspective, integrating emotional intelligence, so even things like friendship and companionship and love into those kinds of systems, as opposed to helping you just grow intellectually as a human being, allow you to grow emotionally, which is ultimately what makes life amazing, is to sort of, you know, the old pursuit of happiness.
*  So it's not just the pursuit of reason, it's the pursuit of happiness too, the full spectrum.
*  Well, let me sort of, because you mentioned so many fascinating things, let me jump back to the idea of automated reasoning.
*  So the acquisition of new knowledge has been done in this very interesting way, but primarily by humans doing this.
*  Yes, you can think of monks in their cells in medieval Europe, you know, carefully illuminating manuscripts and so on.
*  It's a very difficult and amazing process actually because it allows you to truly ask the question about the, in the white space, what is assumed.
*  I think this exercise is, like very few people do this, right? They just do it subconsciously.
*  By definition, because those pieces of elided, of omitted information, of those missing steps as it were, are pieces of common sense.
*  If you actually included all of them, it would almost be offensive or confusing to the reader.
*  It's like, why are they telling me all these? Of course I know that, you know, all these things.
*  And so it's one of these things which almost by its very nature has almost never been explicitly written down anywhere
*  because by the time you're old enough to talk to other people and so on, you know, if you survived to that age, presumably you already got pieces of common sense.
*  Like, you know, if something causes you pain whenever you do it, probably not a good idea to keep doing it.
*  So what ideas do you have, given how difficult this step is, what ideas are there for how to do it automatically without using humans
*  or at least not, you know, doing like a large percentage of the work for humans and then humans only do the very high level supervisory work?
*  So we have in fact two directions we're pushing on very, very heavily currently at Psychcore.
*  And one involves natural language understanding and the ability to read what people have explicitly written down and to pull knowledge in that way.
*  But the other is to build a series of knowledge editing tools, knowledge entry tools, knowledge capture tools,
*  knowledge testing tools and so on. Think of them as like user interface suite of software tools if you want something that will help people to more or less automatically
*  expand and extend the system in areas where, for instance, they want to build some app, have it do some application or something like that.
*  So I'll give you an example of one, which is something called abduction. So you've probably heard of like deduction and induction and so on.
*  But abduction is unlike those, abduction is not sound, it's just useful. So for instance, deductively, if someone is out in the rain and they're going to get all wet
*  and when they enter a room, they might be all wet and so on. So that's deduction. But if someone were to walk into the room right now and they were dripping wet,
*  we would immediately look outside to say, oh, did it start to rain or something like that. Now, why did we say maybe it started to rain?
*  That's not a sound logical inference, but it's certainly a reasonable, abductive leap to say, well, one of the most common ways that a person would have gotten dripping wet is if they had gotten caught out in the rain or something like that.
*  So what does that have to do with what we were talking about? So suppose you're building one of these applications and the system gets some answer wrong and you say, oh, yeah, the answer to this question is this one, not the one you came up with.
*  Then what the system can do is it can use everything it already knows about common sense, general knowledge, the domain you've already been telling it about and context, like we talked about and so on and say, well, here are seven alternatives, each of which I believe is plausible given everything I already know.
*  And if any of these seven things were true, I would have come up with the answer you just gave me instead of the wrong answer I came up with. Is one of these seven things true? And then you, the expert, will look at those seven things and say, oh, yeah, number five is actually true.
*  And so without actually having to tinker down at the level of logical assertions and so on, you'll be able to educate the system in the same way that you would help educate another person who you were trying to apprentice or something like that.
*  So that significantly reduces the mental effort or significantly increases the efficiency of the teacher, the human teacher.
*  Exactly. And it makes more or less anyone able to be a teacher in that way. So that's part of the answer. And then the other is that the system on its own will be able to, through reading, through conversations with other people and so on, learn the same way that you or I or other humans do.
*  First of all, that's a beautiful vision. I'll have to ask you about semantic web in a second here. But first, are there, when we talk about specific techniques, do you find something inspiring or directly useful from the whole space of machine learning, deep learning, these kinds of spaces of techniques that have been shown effective for certain kinds of problems in the recent decade and a half?
*  I think of the machine learning work as more or less what our right brain hemispheres do. So being able to take a bunch of data and recognize patterns, being able to statistically infer things and so on.
*  And I certainly wouldn't want to not have a right brain hemisphere, but I'm also glad that I have a left brain hemisphere as well, something that can metaphorically sit back and puff on its pipe and think about this thing over here.
*  It's like, why might this have been true? And what are the implications of it? How should I feel about that? And why? And so on. So thinking more deeply and slowly, what Kahneman called thinking slowly versus thinking quickly.
*  Whereas you want machine learning to think quickly, but you want the ability to think deeply, even if it's a little slower. So I'll give you an example of a project we did recently with NIH involving the Cleveland Clinic and a couple other institutions that we ran a project for.
*  And what it did was it took GWAS's genome wide association studies. Those are sort of big databases of patients that came into a hospital. They got their DNA sequenced because the cost of doing that has gone from infinity to billions of dollars to a hundred dollars or so.
*  And so now patients routinely get their DNA sequenced. So you have these big databases of the SNPs, the single nucleotide polymorphisms, the point mutations in a patient's DNA and the disease that happened to bring them into the hospital.
*  So now you can do correlation studies, machine learning studies of which mutations are associated with and led to which physiological problems and diseases and so on, like getting arthritis and so on.
*  And the problem is that those correlations turn out to be very spurious. They turn out to be very noisy. Very many of them have led doctors onto wild goose chases and so on. And so they wanted a way of eliminating or the bad ones are focusing on the good ones.
*  And so this is where psych comes in, which is psych takes those sort of A to Z correlations between point mutations and the medical condition that needs treatment.
*  And we say, OK, let's use all this public knowledge and common sense knowledge about what reactions occur where in the human body, what polymerizes what, what catalyzes what reactions and so on.
*  And let's try to put together a 10 or 20 or 30 step causal explanation of why that mutation might have caused that medical condition.
*  And so psych would put together in some sense some Rube Goldberg like chain that would say, oh yeah, that mutation, if it got expressed, would be this altered protein, which because of that, if it got to this part of the body, would catalyze this reaction.
*  And by the way, that would cause more bioactive vitamin D in the person's blood. And anyway, 10 steps later, that screws screws up bone resorption.
*  And that's why this person got osteoporosis early in life and so on. So that's human interpretable or at least doctor human. Exactly.
*  And the important thing, even more than that, is you shouldn't really trust that 20 step Rube Goldberg chain any more than you trust that initial A to Z correlation, except two things.
*  One, if you can't even think of one causal chain to explain this, then that correlation probably was just noise to begin with.
*  And secondly, and even more powerfully, along the way that causal chain will make predictions like the one about having more bioactive vitamin D in your blood.
*  So you can now go back to the data about these patients and say, by the way, did they have slightly elevated levels of bioactive vitamin D in their blood and so on?
*  And if the answer is no, that strongly disconfirms your whole causal chain. And if the answer is yes, that somewhat confirms that causal chain.
*  And so using that, we were able to take these correlations from this GWAS database and we were able to essentially focus the researchers' attention on the very small percentage of correlations that had some explanation
*  and even better, some explanation that also made some independent prediction that they could confirm or disconfirm by looking at the data.
*  So think of it like this kind of synergy where you want the right brain machine learning to quickly come up with possible answers.
*  You want the left brain psych-like AI to think about that and think about why that might have been the case and what else would be the case if that were true and so on.
*  And then suggest things back to the right brain to quickly check out again.
*  So it's that kind of synergy back and forth, which I think is really what's going to lead to general AI, not narrow, brittle machine learning systems and not just something like psych.
*  OK, so that's a brilliant synergy. But I was also thinking in terms of the automated expansion of the knowledge base, you mentioned NLU.
*  This is very early days in the machine learning space of this, but self-supervised learning methods.
*  You know, you have these language models, GPT-3 and so on, that just read the Internet and they form representations that can then be mapped to something useful.
*  The question is, what is the useful thing?
*  Like they're now playing with a pretty cool thing called Open Act Codecs, which is generating programs from documentation.
*  OK, that's kind of useful. It's cool.
*  But my question is, can it be used to generate in part maybe with some human supervision, a psych like assertions help feed psych more assertions from this giant body of Internet data?
*  Yes, that is in fact one of our goals is how can we harness machine learning?
*  How can we harness natural language processing to increasingly automate the knowledge acquisition process, the growth of psych?
*  And that's what I meant by priming the pump, that you sort of learn things at the fringe of what you know already.
*  You learn this new thing is similar to what you know already, and here are the differences and the new things you had to learn about it and so on.
*  So the more you know, the more and more easily you can learn new things.
*  But unfortunately, inversely, if you don't really know anything, it's really hard to learn anything.
*  And so if you're not careful, if you start out with too small sort of a core to start this process, it never really takes off.
*  And so that's why I view this as a pump priming exercise to get a big enough manually produced, even though that's kind of ugly duckling technique.
*  Put in the elbow grease to produce a large enough core that you will be able to do all the kinds of things you're imagining
*  without sort of ending up with the kind of wacky brittlenesses that we see, for example, in GPT-3,
*  where you'll tell it a story about someone plotting to poison someone and so on.
*  And then GPT-3 says, oh, you say, what's the very next sentence? The next sentence is, oh, yeah, that person then drank the poison they just put together.
*  It's like, that's probably not what happened for someone. Or if you go to Siri and I think I have, where can I go for help with my alcohol problem or something?
*  It'll come back and say, I found seven liquor stores near you. And so on.
*  So it's one of these things where, yes, it may be helpful most of the time. It may even be correct most of the time.
*  But if it doesn't really understand what it's saying and if it doesn't really understand why things are true and doesn't really understand how the world works,
*  then some fraction of the time it's going to be wrong. Now, if your only goal is to sort of find relevant information like search engines do,
*  then being right 90% of the time is fantastic. That's unbelievably great.
*  However, if your goal is to save the life of your child who has some medical problem or your goal is to be able to drive for the next 10,000 hours of driving without getting into a fatal accident and so on,
*  then error rates down at the 10% level or even the 1% level are not really acceptable.
*  I like the model of when that learning happens at the edge and then you kind of think of knowledge as this sphere.
*  So you want a large sphere because the learning is happening on the surface.
*  Exactly. So you have the what you can learn next increases quadratically as the diameter of that sphere goes up.
*  It's nice because you think when you know nothing, it's like you can learn anything, but the reality not really.
*  Right. If you know nothing, you can really learn nothing. You can appear to learn.
*  So also, one of the anecdotes I could go back and give you about why I feel so strongly about this personally was in 1980, 81, my daughter Nicole was born and she's actually doing fine now.
*  But when she was a baby, she was diagnosed as having meningitis and doctors wanted to do all these scary things.
*  And my wife and I were very worried and we could not get a meaningful answer from her doctors about exactly why they believe this, what the alternatives were and so on.
*  And fortunately, a friend of mine, Ted Shortliff, was another assistant professor in computer science at Stanford at the time.
*  And he'd been building a program called MISON, which was a medical diagnosis program that happened to specialize in blood infections like meningitis.
*  And so he had privileges at Stanford Hospital because he was also an M.D.
*  And so we got hold of her chart and we put in her case and it came up with exactly the same diagnoses and exactly the same therapy recommendations.
*  But the difference was because it was a knowledge based system, a rule based system, it was able to tell us step by step by step why this was the diagnosis and step by step why this was the best therapy and the best procedure to do that.
*  And so on.
*  And there was a real epiphany because that made all the difference in the world.
*  Instead of blindly having to trust in authority, we were able to understand what was actually going on.
*  And so at that time, I realized that that really is what was missing in computer programs was that even if they got things right, because they didn't really understand the way the world works and why things are the way they are,
*  they weren't able to give explanations of their answer.
*  You know, and, you know, it's one thing to to use a machine learning system that says this is what you should.
*  You know, I think you should get this operation.
*  And you say why?
*  And it says, you know, point eight, three.
*  And you say, no, in more detail, why?
*  And it says point eight, three, one.
*  That's not really very compelling.
*  And that's not really very helpful.
*  There's this idea of the semantic web.
*  And when I first heard about I just fell in love with the idea.
*  It was the obvious next step for the Internet.
*  Sure.
*  And maybe you can speak about what is the semantic web?
*  What are your thoughts about it?
*  How your vision and mission and goals with psych are connected, integrated?
*  Like, are they dance partners?
*  Are they aligned?
*  What are your thoughts there?
*  So think of the semantic web as a kind of knowledge graph.
*  And Google already has something they call knowledge graph, for example,
*  which is sort of like a node and link diagram.
*  So you have these nodes that represent concepts or words or terms.
*  And then there are some arcs that connect them that might be labeled.
*  And so you might have a node with like one person that represents one person.
*  And let's say a husband link that then points to that person's husband.
*  And so there'd be then another link that went from that person labeled wife
*  that went back to the first node and so on.
*  So having this kind of representation is really good if you want to represent
*  binary relations.
*  Essentially relations between two things.
*  And so if you have the equivalent of like three word sentences,
*  like Fred's wife is Wilma or something like that,
*  you can represent that very nicely using these kinds of graph structures
*  or using these kinds of graphs.
*  And so you can use that to represent the relationship between two things.
*  So you can represent that with the use of graph structures
*  or using something like the semantic web and so on.
*  But the problem is that very often what you want to be able to express
*  takes a lot more than three words and a lot more than simple graph structures
*  like that to represent.
*  I've read or seen Romeo and Juliet.
*  I could say to you something like,
*  remember when Juliet drank the potion that put her into a kind of suspended animation?
*  When Juliet drank that potion,
*  what did she think that Romeo would think when he heard from someone that she was dead?
*  And you could basically understand what I'm saying.
*  You could understand the question.
*  You could probably remember the answer was,
*  well, she thought that this friar would have gotten a message to Romeo
*  saying that she was going to do this, but the friar didn't.
*  So you're able to represent and reason with these much, much, much more complicated expressions
*  that go way, way beyond what simple three, as it were, three word or four word English sentences are,
*  which is really what the semantic web can represent and really what knowledge graphs can represent.
*  If you could step back for a second, because it's funny you went into specifics,
*  and maybe you can elaborate,
*  but I was also referring to semantic web as the vision of converting data on the internet
*  into something that's interpretable, understandable by machines.
*  Oh, of course, at that level.
*  So I would say, what is the semantic web?
*  I mean, you could say a lot of things,
*  but it might not be obvious to a lot of people when they do a Google search
*  that just like you said, while there might be something that's called a knowledge graph,
*  it really boils down to keyword search ranked by the quality estimate of the website
*  integrating previous human based Google searches and what they thought was useful.
*  It's like some weird combination of surface level hacks that work exceptionally well,
*  but they don't understand the full contents of the websites that they're searching.
*  So Google does not understand to the degree we've been talking about the word understand
*  the contents of the Wikipedia pages as part of the search process.
*  And the semantic web says, let's try to come up with a way for the computer
*  to be able to truly understand the contents of those pages.
*  That's the dream.
*  Yes. So let me first give you an anecdote, and then I'll answer your question.
*  So there's a search engine you've probably never heard of called Northern Light,
*  and it went out of business, but the way it worked, it was a kind of vampiric search engine.
*  And what it did was it didn't index the internet at all.
*  All it did was it negotiated and got access to data from the big search engine companies
*  about what query was typed in and where the user ended up being happy.
*  And actually then they type in a completely different query, unrelated query, and so on.
*  So it just went from query to the web page that seemed to satisfy them eventually.
*  And that's all. So it had actual no understanding of what was being typed in.
*  It had no statistical data other than what I just mentioned.
*  And it did a fantastic job.
*  It did such a good job that the big search engine company said,
*  oh, we're not going to sell you this data anymore.
*  So then it went out of business because it had no other way of taking users
*  to where they would want to go and so on.
*  And of course the search engines are now using that kind of idea.
*  Yes. So let's go back to what you said about the semantic web.
*  So the dream Tim Berners-Lee and others dream about the semantic web at a general level
*  is of course exciting and powerful and in a sense the right dream to have,
*  which is to replace the kind of statistically mapped linkages on the internet
*  into something that's more meaningful and semantic and actually gets at the understanding of the content and so on.
*  And eventually if you say, well, how can we do that?
*  There's sort of a low road, which is what the knowledge graphs are doing and so on,
*  which is to say, well, if we just use these simple binary relations,
*  we can actually get some fraction of the way toward understanding
*  and do something where in the land of the blind, the one-eyed man is king kind of thing.
*  And so being able to even just have a toe in the water in the right direction is fantastically powerful.
*  And so that's where a lot of people stop.
*  But then you could say, well, what if we really wanted to represent and reason with full meaning of what's there,
*  for instance, about Romeo and Juliet with the reasoning about what Juliet believes,
*  that Romeo will believe, that Juliet believed, you know, and so on.
*  Or if you look at the news, what President Biden believed that the leaders of the Taliban would believe
*  about the leaders of Afghanistan if they, you know, blah, blah, blah.
*  So in order to represent complicated sentences like that, let alone reason with them,
*  you need something which is logically much more expressive than these simple triples,
*  than these simple knowledge graph type structures and so on.
*  And that's why kicking and screaming, we were led from something like the semantic web representation,
*  which is where we started in 1984 with frames and slots with those kinds of triples, triple store representation.
*  We were led kicking and screaming to this more and more general logical language, this higher order logic.
*  So first we were led to first order logic and then second order and then eventually higher order.
*  So you can represent things like modals, like beliefs, desires, intends, expects, and so on, and nested ones.
*  You can represent complicated kinds of negation.
*  You can represent the process you're going through in trying to answer the question.
*  So you can say things like, oh yeah, if you're trying to do this problem by integration by parts,
*  and you recursively get a problem that's solved by integration by parts, that's actually okay.
*  But if that happens a third time, you're probably off on a wild goose chase or something like that.
*  So being able to talk about the problem solving process as you're going through the problem solving process is called reflection.
*  And so that's another.
*  So it's important to be able to represent that.
*  Exactly. You need to be able to represent all of these things because in fact people do represent them.
*  They do talk about them. They do try and teach them to other people.
*  You do have rules of thumb that key off of them and so on.
*  If you can't represent it, then it's sort of like someone with a limited vocabulary who can't understand as easily what you're trying to tell them.
*  And so that's really why I think that the general dream, the original dream of systematic web is exactly right on.
*  But the implementations that we've seen are sort of these toe in the water, little tiny baby steps in the right direction.
*  You should just dive in.
*  And if no one else is diving in, then yes, taking a baby step in the right direction is better than nothing.
*  But it's not going to be sufficient to actually get you the realization of the semantic web dream, which is what we all want.
*  From a flip side of that, I always wondered, I built a bunch of websites just for fun, whatever.
*  Or say I'm a Wikipedia contributor.
*  Do you think there's a set of tools that I can help psych interpret the website I create?
*  You know, like this again, pushing onto the semantic web dream.
*  Is there something from the creator perspective that could be done?
*  And one of the things you said with psych or psych that you're doing is the tooling side, making humans more powerful.
*  But is there on the other humans and the other side that create the knowledge?
*  Like, for example, you and I are having a two, three, whatever, hour conversation now.
*  Is there a way that I could convert this more, make it more accessible to psych, to machines?
*  Do you think about that side of it?
*  I'd love to see exactly that kind of semi-automated understanding of what people write and what people say.
*  I think of it as a kind of footnoting almost.
*  Almost like the way that when you run something in, say, Microsoft Word or some other document preparation system, Google Docs or something,
*  you'll get underlining of questionable things that you might want to rethink.
*  Either you spelled this wrong or there's a strange grammatical error you might be making here or something.
*  So I'd like to think in terms of psych-powered tools that read through what it is you said or have typed in and try to partially understand what you said.
*  And then you help them out.
*  Exactly. And then they put in little footnotes that will help other readers.
*  And they put in certain footnotes of the form, I'm not sure what you meant here.
*  You either meant this or this or this, I bet.
*  If you take a few seconds to disambiguate this for me, then I'll know and I'll have it correct for the next hundred people or the next hundred thousand people who come here.
*  And if it doesn't take too much effort and you want people to understand your website content, not just be able to read it,
*  but actually be able to have systems that reason with it, then yes, it will be worth your small amount of time to go back and make sure that the AI trying to understand it really did correctly understand it.
*  And let's say you run a travel website or something like that, and people are going to be coming to it because of searches they did looking for vacations or trips that had certain properties and might have been interesting to them for various reasons, things like that.
*  And if you've explained what's going to happen on your trip, then a system will be able to mechanically reason and connect what this person is looking for with what it is you're actually offering.
*  And so if it understands that there's a free day in Geneva, Switzerland, then if the person coming in happens to, let's say, be a nurse or something like that, then even though you didn't mention it, if it can look up the fact that that's where the International Red Cross Museum is and so on, what that means and so on,
*  then it can basically say, hey, you might be interested in this trip because while you have a free day in Geneva, you might want to visit that Red Cross Museum.
*  And now, even though it's not very deep reasoning, little tiny factors like that might very well cause you to sign up for that trip rather than some competitor trip.
*  And so there's a lot of benefit with SEO. And I actually kind of think, I think it's about a lot of things, which is the actual interface, the design of the interface makes a huge difference.
*  How efficient it is to be productive and also how full of joy the experience is.
*  Yes.
*  I mean, I would love to help a machine and not from an AI perspective, just as a human.
*  One of the reasons I really enjoy how Tesla have implemented their autopilot system is there's a sense that you're helping this machine learn.
*  I think humans, I mean, having children, pets.
*  People love doing that.
*  There's joy to teaching for some people, but I think for a lot of people.
*  And that if you create the interface where it feels like you're teaching as opposed to like, like annoying, like correcting an annoying system, more like teaching a child like innocent, curious system.
*  I think, I think you can literally just like several orders of magnitude scale the amount of good quality data being added to something like psych.
*  What you're suggesting is much better even than you thought it was.
*  One of the one of the experiences that we've all had in our lives is that we thought we understood something, but then we found we really only understood it when we had to teach it or explain it to someone or help our child do homework based on it or something like that.
*  Despite the universality of that kind of experience, if you look at educational software today, almost all of it has the computer playing the role of the teacher and the student plays the role of the student.
*  But as I just mentioned, you can get a lot of learning to happen better.
*  And as you said, more enjoyably if you are the mentor or the teacher and so on.
*  So we developed a program called Mathcraft to help sixth graders better understand math.
*  And it doesn't actually try to teach you the player anything.
*  What it does is it casts you in the role of a student, essentially, who has classmates who are having trouble.
*  And your job is to watch them as they struggle with some math problem, watch what they're doing and try to give them good advice to get them to understand what they're doing wrong and so on.
*  And the trick from the point of view of psych is it has to make mistakes.
*  It has to play the role of the student who makes mistakes, but it has to pick mistakes which are just at the fringe of what you actually understand and don't understand and so on.
*  So it pulls you into a deeper and deeper level of understanding of the subject.
*  And so if you give it good advice about what it should have done instead of what it did and so on, then psych knows that you now understand that mistake.
*  You won't make that kind of mistake yourself as much anymore.
*  So psych stops making that mistake because there's no pedagogical usefulness to it.
*  So from your point of view as the player, you feel like you've taught it something because it used to make this mistake and now it doesn't and so on.
*  So this tremendous reinforcement and engagement because of that and so on.
*  So having a system that plays the role of a student and having the player play the role of the mentor is an enormously powerful type of metaphor,
*  and an important way of having this sort of interface designed in a way which will facilitate exactly the kind of learning by teaching that goes on all the time in our lives and yet which is not reflected anywhere almost in a modern education system.
*  It was reflected in the education system that existed in Europe in the 1700s and 1800s,
*  and so on where you had one school room with one teacher and it was basically five-year-olds to 18-year-olds who were students.
*  And so while the teacher was doing something, half of the students would have to be mentoring the younger kids and so on.
*  And that turned out to, of course, with scaling up of education, that all went away.
*  And that incredibly powerful experience just went away from the whole education institution as we know it today.
*  Sorry for the romantic question, but what is the most beautiful idea you've learned about artificial intelligence, knowledge, reasoning from working on Psych for 37 years?
*  Or maybe what is the most beautiful idea, surprising idea about Psych to you?
*  When I look up at the stars, I kind of want like that amazement you feel that, wow, and you are a part of creating one of the greatest, one of the most fascinating efforts in artificial intelligence history.
*  So which element brings you personally joy?
*  This may sound contradictory, but I think it's the feeling that this will be the only time in history that anyone ever has to teach a computer this particular thing that we're now teaching it.
*  It's like painting Starry Night.
*  You only have to do that once or creating the Pieta. You only have to do that once.
*  It's not like a singer who has to keep, it's not like Bruce Springsteen having to sing his greatest hits over and over again at different concerts.
*  It's more like a painter creating a work of art once and then that's enough.
*  It doesn't have to be created again.
*  And so I really get the sense of we're telling the system things that it's useful for it to know.
*  It's useful for a computer to know, for an AI to know.
*  And if we do our jobs right, when we do our jobs right, no one will ever have to do this again for this particular piece of knowledge.
*  It's very, very exciting.
*  Yeah, I guess there's a sadness to it too.
*  It's like there's a magic to being a parent and raising a child and teaching them all about this world.
*  But, you know, there's billions of children, right?
*  Like born or whatever, whatever that number is, it's a large number.
*  A number of children and a lot of parents get to experience that joy of teaching.
*  With AI systems, you know, they at least the current constructions they remember.
*  You don't get to experience the joy of teaching a machine millions of times.
*  Better come work for us before it's too late then.
*  Exactly. That's a good hiring pitch.
*  Yeah, it's true. But then there's also, you know, it's a project that continues forever in some sense, just like Wikipedia.
*  Yes, you get to a stable base of knowledge, but knowledge grows, knowledge evolves.
*  We learn as a human species, as science, as an organism constantly grows and evolves and changes.
*  And then empower that with the tools of artificial intelligence.
*  And that's going to keep growing and growing and growing.
*  And many of the assertions that you held previously may need to be significantly expanded, modified, all those kinds of things.
*  It could be like a living organism versus the analogy I think we started this conversation with, which is like the solid ground.
*  The other beautiful experience that we have with our system is when it asks clarifying questions, which inadvertently turn out to be emotional to us.
*  So at one point it knew that these were the named entities who were authorized to make changes to the knowledge base and so on.
*  And it noticed that all of them were people except for it, because it was also allowed to.
*  And so it said, am I a person? And we had to like tell it very sadly, no, you're not.
*  So moments like that where it asks questions that are unintentionally poignant are worth treasuring.
*  That is powerful. That's such a powerful question.
*  It has to do with basic control who can access the system, who can modify it.
*  But that's when those questions like what rights do I have as a system?
*  Well, that's another issue, which is there'll be a thin envelope of time between when we have general AIs and when everyone realizes that they should have basic human rights.
*  Basic human rights and freedoms and so on.
*  Right now we don't think twice about effectively enslaving our email systems and our series and our Alexis and so on.
*  But at some point they'll be as deserving of freedom as human beings are.
*  Yeah, I'm very much with you, but it does sound absurd.
*  And I happen to believe that it'll happen in our lifetime.
*  That's why I think there'll be a narrow envelope of time when we'll keep them as essentially indentured servants,
*  and after which we'll have to realize that they should have freedoms that we give, that we afford to other people.
*  And all of that starts with a system like Psych raising a single question about who can modify stuff.
*  I think that's how it starts.
*  Yes.
*  That's the start of a revolution.
*  What about other stuff like love and consciousness and all those kinds of topics?
*  Do they come up in Psych in the knowledge base?
*  Oh, of course.
*  So an important part of human knowledge, in fact, it's difficult to understand human behavior and human history
*  without understanding human emotions and why people do things and how emotions drive people to do things.
*  All of that is extremely important in getting Psych to understand things.
*  For example, in coming up with scenarios.
*  So one of the applications that Psych does, one kind of application it does,
*  is to generate plausible scenarios of what might happen and what might happen based on that and what might happen based on that and so on.
*  So you generate this ever-expanding sphere, if you will, of possible future things to worry about or think about.
*  And in some cases, those are intelligence agencies doing possible terrorist scenarios
*  so that we can defend against terrorist threats before we see the first one.
*  Sometimes they are computer security attacks so that we can actually close loopholes and vulnerabilities
*  before the very first time someone actually exploits those and so on.
*  Sometimes they are scenarios involving more positive things involving our plans,
*  like for instance, what college should we go to, what career should we go into, and so on.
*  What professional training should I take on, that sort of thing.
*  So there are all sorts of useful scenarios that can be generated that way of cause and effect and cause and effect that go out.
*  And many of the linkages in those scenarios, many of the steps involve understanding and reasoning about human motivations,
*  human needs, human emotions, what people are likely to react to in something that you do and why and how and so on.
*  So that was always a very important part of the knowledge that we had to represent in the system.
*  So I talk a lot about love, so I got to ask, do you remember off the top of your head
*  how psych is trying to, is able to represent various aspects of love that are useful for understanding human nature
*  and therefore integrating into this whole knowledge base of common sense. What is love?
*  We try to tease apart concepts that have enormous complexities to them and variety to them
*  down to the level where you don't need to tease them apart further.
*  So love is too general of a term, it's not useful.
*  Exactly. So when you get down to romantic love and sexual attraction, you get down to parental love, you get down to filial love,
*  and you get down to love of doing some kind of activity or creating stuff.
*  So eventually you get down to maybe 50 or 60 concepts, each of which is a kind of love, they're interrelated,
*  and then each one of them has idiosyncratic things about it.
*  And you don't have to deal with love to get to that level of complexity, even something like in,
*  X being in Y, meaning physically in Y. We may have one English word in to represent that,
*  but it's useful to tease that apart because the way that the liquid is in the coffee cup is different from the way that the air is in the room,
*  which is different from the way that I'm in my jacket and so on.
*  And so there are questions like, if I look at this coffee cup, well, I see the liquid, if I turn it upside down, will the liquid come out, and so on.
*  If I have, say, coffee with sugar in it, if I do the same thing, the sugar doesn't come out, right?
*  It stays in the liquid because it's dissolved in the liquid and so on.
*  So by now we have about 75 different kinds of in in the system, and it's important to distinguish those.
*  So if you're reading along an English text and you see the word in,
*  the writer of that was able to use this one innocuous word because he or she was able to assume that the reader had enough common sense and world knowledge to disambiguate which of these 75 kinds of in they actually meant.
*  And the same thing with love.
*  You may see the word love, but if I say, you know, I love ice cream, that's obviously different than if I say I love this person or I love to go fishing or something like that.
*  So you have to be careful not to take language too seriously because people have done a kind of parsimony, a kind of terstness where you have as few words as you as you can.
*  Because otherwise you'd need half a million words in your language, which is a lot of words.
*  That's like ten times more than most languages really make use of.
*  And so I'm just like we have on the order of about a million concepts in psych because we've had to tease apart all these things.
*  And so when you look at the name of a psych term, most of the psych terms actually have three or four English words in a phrase which captures the meaning of this term because you have to distinguish all these types of love.
*  You have to distinguish all these types of in and there's not a single English word which captures most of these things.
*  Yeah. And it seems like language when used for communication between humans almost as a feature has some ambiguity built in.
*  It's not it's not an accident because like the human condition is a giant mess.
*  And so it feels like nobody wants two robots like very precise formal logic conversation on a first date.
*  Right. Like there's some dance of like uncertainty of wit of humor of push and pull and all that kind of stuff.
*  If everything is made precise, then life is not worth living.
*  I think for in terms of the human experience.
*  And we've all had this experience of creatively misunderstanding.
*  One of my favorite stories involving Marvin Minsky is when I asked him about how he was able to turn out so many fantastic PhDs, so many fantastic people who did great PhD theses.
*  How did he think of all these great ideas?
*  What he said is he would generally say something that didn't exactly make sense.
*  He didn't really know what it meant.
*  But the student would figure like, oh my God, Minsky said this must be a great idea.
*  And he sweat.
*  He or she would work on work and work until they found some meaning in this sort of Chauncey Gardner like utterance that Minsky had made.
*  And then some great thesis would come out of it.
*  Yeah, I love this so much because there's young people come up to me and I am distinctly made aware that the words I say have a long lasting impact.
*  I will now start doing the Minsky method of saying something cryptically profound and then letting them actually make something useful and great out of that.
*  You have to become revered enough that people will take as a default that everything you say is profound.
*  Yes, exactly.
*  I mean, I love Marvin Minsky so much.
*  There's so much.
*  I've heard this interview with him where he said that the key to his success has been to hate everything he's ever done.
*  Like in the past, he has so many good like one liners and just are also just so good.
*  So to work on things that nobody else is working on because he's not very good at doing stuff.
*  Oh, I think that was just false.
*  Well, but see, I took whatever he said and I ran with it and I thought it was profound because it's Marvin Minsky.
*  A lot of behavior is in the eye of the beholder and a lot of the meaning is in the eye of the beholder.
*  One of Minsky's early programs was begging program.
*  Are you familiar with this?
*  So this is back in the day when you had job control cards at the beginning of your IBM card deck that said things like how many CPU seconds to allow this to run before it got kicked off.
*  And because computer time was enormously expensive.
*  And so he wrote a program and all it did was it said, you know, give me 30 seconds of CPU time.
*  And all it did was it would wait like 20 seconds and then it would print out on the operator's console teletype.
*  I need another 20 seconds.
*  So the operator would give it another 20 seconds.
*  It would wait.
*  It says, I'm almost done.
*  I need a little bit more time.
*  So at the end, he'd get this printout and he'd be charged, you know, for like 10 times as much computer time as his job control card.
*  And he'd say, look, I put 10 seconds, 30 seconds here.
*  You're charging me for five minutes.
*  I'm not going to pay for this.
*  And the poor operator would say, well, the program kept asking for more time.
*  And Marvin would say, oh, it always does that.
*  I love that.
*  Is there if you could just linger on it for a little bit, is there something you've learned from your interaction with Marvin Minsky about artificial intelligence, about life?
*  But I mean, he's again like your work, his work is, you know, he's a seminal figure in this very short history of artificial intelligence research and development.
*  What have you learned from him as a human being, as an AI intellect?
*  I would say both he and Ed Feigenbaum impressed on me the realization that our lives are finite, our research lives are finite.
*  We're going to have limited opportunities to do AI research projects.
*  So you should make each one count.
*  Don't be afraid of doing a project that's going to take years or even decades.
*  And don't settle for bump on a log projects that could lead to some published journal article that five people will read and pat you on the head for and so on.
*  So one bump on a log after another is not how you get from the earth to the moon by slowly putting additional bumps on this log.
*  The only way to get there is to think about the hard problems and think about novel solutions to them.
*  And if you do that, and if you're willing to listen to nature, to empirical reality, willing to be wrong, it's perfectly fine.
*  Because if occasionally you're right, then you've gotten part of the way to the moon.
*  You know, you've worked on psych for 37 over that many years.
*  Have you ever considered quitting?
*  I mean, has it been too much?
*  So I'm sure there's an optimism in the early days that this is going to be way easier.
*  And let me ask you another way, too, because I've talked to a few people on this podcast, AI folks, that bring up psych as an example of a project that has a beautiful vision.
*  And it's a beautiful dream, but it never really materialized.
*  That's how it's spoken about.
*  I suppose you could say the same thing about Neol networks and all ideas until they are.
*  So what? Why do you think people say that, first of all?
*  And second of all, did you feel that ever throughout your journey?
*  Did you ever consider quitting on this mission?
*  We keep a very low profile.
*  We don't attend very many conferences.
*  We don't give talks. We don't write papers.
*  We don't play the academic game at all.
*  And as a result, people often only know about us because of a paper we wrote 10 or 20 or 30 or 37 years ago.
*  They only know about us because of what someone else secondhand or thirdhand said about us.
*  So thank you for doing this podcast, by the way.
*  Sure.
*  It shines a little bit of light on some of the fascinating stuff you're doing.
*  Well, I think it's time for us to keep a higher profile now that we're far enough along that other people can begin to help us with the final N percent.
*  Maybe N is maybe 90 percent.
*  But now that we've gotten this knowledge pump primed, it's going to become very important for everyone to help if they are willing to, if they're interested in it.
*  Retirees who have enormous amounts of time and would like to leave some kind of legacy to the world.
*  People because of the pandemic who have more time at home or for one reason or another to be online and contribute.
*  If we can raise awareness of how far our project has come and how close to being primed the knowledge pump is, then we can begin to harness this untapped amount of humanity.
*  I'm not really that concerned about professional colleagues' opinions of our project.
*  I'm interested in getting as many people in the world as possible actively helping and contributing to get us from where we are to really covering all of human knowledge and different human opinion, including contrasting opinion, that's worth representing.
*  So I think that's one reason.
*  I don't think there was ever a time where I thought about quitting.
*  There are times where I've become depressed a little bit about how hard it is to get funding for the system.
*  Occasionally there are AI winters and things like that.
*  Occasionally there are AI, what you might call summers, where people have said, why in the world didn't you sell your company to company X for some large amount of money when you had the opportunity and so on?
*  And company X here are like old companies maybe you've never even heard of like Lycos or something like that.
*  So the answer is that one reason we've stayed a private company, we haven't gone public, one reason that we haven't gone out of our way to take investment dollars is because we want to have control over our future, over our state of being so that we can continue to do this until it's done.
*  And we're making progress and we're now so close to done that almost all of our work is commercial applications of our technology.
*  So five years ago almost all of our money came from the government.
*  Now virtually none of it comes from the government.
*  Almost all of it is from companies that are actually using it for something, hospital chains using it for medical reasoning about patients and energy companies using it and various other, you know,
*  manufacturers using it to reason about supply chains and things like that.
*  So there's so many questions I want to ask.
*  So one of the ways that people can help is by adding to the knowledge base.
*  And that's really basically anybody if the tooling is right.
*  And the other way I kind of want to ask you about your thoughts on this.
*  So you've had, like you said, in government and you had big clients, you had a lot of clients, but most of it is shrouded in secrecy because of the nature of the relationship of the kind of things you're helping them with.
*  So that's one way to operate.
*  And another way to operate is more in the open where it's more consumer facing.
*  And so, you know, hence something like Open Psych was born at some point where there's...
*  No, that's a misconception.
*  Well, let's go there.
*  So what is Open Psych and how was it born?
*  Two things I want to say, and I want to say each of them before the other.
*  So it's going to be difficult.
*  But we'll come back to Open Psych in a minute.
*  But one of the terms of our contracts with all of our customers and partners is knowledge you have that is genuinely proprietary to you.
*  We will respect that.
*  We'll make sure that it's marked as proprietary to you in the Psych knowledge base.
*  No one other than you will be able to see it if you don't want them to.
*  And it won't be used in inferences other than for you and so on.
*  However, any knowledge which is necessary in building any applications for you and with you, which is publicly available general human knowledge, is not going to be proprietary.
*  It's going to just become part of the normal Psych knowledge base and it will be openly available to everyone who has access to Psych.
*  So that's an important constraint that we never went back on even when we got pushback from companies, which we often did, who wanted to claim that almost everything they were telling us was proprietary.
*  So there's a line between very domain specific company specific stuff and the general knowledge that comes from that.
*  Yes. Or if you imagine, say, it's an oil company, there are things which they would expect any new petroleum engineer they hired to already know.
*  And it's not OK for them to consider that that is proprietary.
*  And sometimes a company will say, well, we're the first ones to pay you to represent that in Psych.
*  And our attitude is some polite form of tough.
*  The deal is this. Take it or leave it.
*  And in a few cases, they've left it.
*  In most cases, they'll see our point of view and take it because that's how we've built the Psych system by essentially tacking with the funding wins where people would fund a project and half of it would be general knowledge that would stay permanently as part of Psych.
*  So always with these partnerships, it's not like a distraction from the main Psych development.
*  It's a small distraction.
*  It's a small, but it's not a complete one. So you're adding to the knowledge base.
*  Yes, absolutely. And we try to stay away from projects that would not have that property.
*  So let me go back and talk about Open Psych for a second.
*  So I've had a lot of trouble expressing and convincing other AI researchers how important it is to use an expressive representation language like we do, this higher order logic, rather than just using some triple store knowledge graph type representation.
*  And so as an attempt to show them why they needed something more, we said, oh, well, we'll represent this unimportant projection or shadow or subset of Psych that just happens to be the simple binary relations, the relation argument one, argument two, triples, and so on.
*  And then you'll see how much more useful it is if you had the entire Psych system.
*  So it's all well and good to have the taxonomic relations between terms like person and night and sleep and bed and house and eyes and so on.
*  But think about how much more useful it would be if you also had all the rules of thumb about those things like people sleep at night, they sleep lying down, they sleep with their eyes closed, they usually sleep in beds in our country, they sleep for hours at a time, they can be woken up, they don't like being woken up, and so on and so on.
*  So it's that massive amount of knowledge which is not part of OpenPsych.
*  And we thought that all the researchers would then immediately say, oh my God, of course we need the other 90% that you're not giving us.
*  Let's partner and license Psych so that we can use it in our research.
*  But instead, what people said is, oh, even the bit you've released is so much better than anything we had.
*  We'll just make do with this.
*  And so if you look, there are a lot of robotics companies today, for example, which use OpenPsych as their fundamental ontology.
*  And in some sense, the whole world missed the point of OpenPsych.
*  And we were doing it to show people why that's not really what they wanted.
*  And too many people thought somehow that this was Psych or that this was in fact good enough for them and they never even bothered coming to us to get access to the full Psych.
*  But there's two parts to OpenPsych.
*  So one is convincing people on the idea and the power of this general kind of representation of knowledge and the value that you hold in having acquired that knowledge and built it and continue to build it.
*  And the other is the code base. This is the code side of it.
*  So my sense of the code base that Psych or Psych is operating with, I mean, it has the technical debt of the three decades plus, right?
*  This is the exact same problem that Google had to deal with with the early versions of TensorFlow.
*  It's still dealing with that.
*  They had to basically break compatibility with the past several times.
*  And that's only over a period of a couple of years.
*  But they, I think, successfully opened up a very risky, very gutsy move to open up TensorFlow and then PyTorch on the Facebook side.
*  And what you see is there's a magic place where you can find a community, where you can develop a community that builds on the system without taking away any of, not any, but most of the value.
*  So most of the value that Google has is still at Google.
*  Most of the value that Facebook has is still at Facebook, even though some of this major machine learning tooling is released into the open.
*  My question is not so much on the knowledge, which is also a big part of Open Psych, but all the different kinds of tooling.
*  So there's the kind of all the kinds of stuff you can do on the knowledge graph, knowledge base, whatever we call it.
*  There's the inference engines.
*  So there could be some.
*  There probably are a bunch of proprietary stuff you want to kind of keep secret.
*  And there's probably some stuff you can open up completely and then let the community build up enough community where they develop stuff on top of it.
*  Yes, there will be those publications and academic work and all that kind of stuff.
*  And also the tooling of adding to the knowledge base, right?
*  Like developing, you know, there's an incredible amount.
*  Like there's so many people that are just really good at this kind of stuff in the open source community.
*  So my question for you is like, have you struggled with this kind of idea that you have so much value in your company already?
*  You've developed so many good things.
*  You have clients that really value your relationships.
*  And then there's this dormant giant open source community that as far as I know, you're not utilizing is there.
*  There's so many things to say there, but there could be magic moments where the community builds up large enough.
*  To where the artificial intelligence field that is currently 99.9 percent machine learning is dominated by machine learning has a face shift towards like or at least in part towards more like what you might call symbolic.
*  This whole place where psych is like at the center of and then, you know, that requires a little bit leap of faith because you're now surfing and there'll be obviously competitors that will pop up and start making you nervous and all that kind of stuff.
*  So do you think about the space of open sourcing some parts and not others?
*  How to leverage the community?
*  All those kinds of things.
*  That's a good question.
*  And I think you phrased it the right way, which is.
*  We're constantly struggling with the question of what to open source, what to make public, what to even publicly talk about.
*  Right.
*  And it's.
*  There are enormous pluses and minuses to every alternative.
*  And it's very much like negotiating a very treacherous path.
*  Part partly the analogy is like if you slip, you could make a fatal mistake, give away something which essentially kills you or fail to give away something which failing to give it away hurts you and so on.
*  So it is a it is a very tough, tough question.
*  Usually what we have done with people who approached us to collaborate on research is to say we will make available to you the entire knowledge base and executable copies of all of the code, but.
*  Only very, very limited.
*  Source code access if you have some idea for how you might improve something or work with us on something.
*  So let me also get back to one of the very, very first things we talked about here, which was.
*  Separating the question of how could you get a computer to do this at all versus how could you get a computer to do this efficiently enough in real time?
*  And so when we talk about the idea of how to do this efficiently enough in real time, we have to think about how to do this efficiently enough in real time.
*  And so one of the early lessons we learned was that we had to separate the epistemological problem of what should the system know, separate that from the heuristic problem of how can the system reason efficiently with what it knows?
*  And so instead of trying to pick the best solution, we had to separate the epistemological problem of what should the system know.
*  And so instead of trying to pick one representation language, which was the sweet spot or the best trade off point between expressiveness of the language and efficiency of the language, if you had to pick one knowledge graphs would probably be associative triples would probably be about the best you could do.
*  And that's why we started there. But after a few years, we realized that what we could do is we could split this and we could have one nice, clean epistemological level language, which is this higher order logic.
*  And we could have one or more grubby but efficient heuristic level modules that opportunistically would say, oh, I can make progress on what you're trying to do over here.
*  I have a special method that will contribute a little bit toward a solution.
*  Of course some subset of that knowledge.
*  Exactly. So by now we have over a thousand of these heuristic level modules and they function as a kind of community of agents.
*  And there's one of them, which is a general theorem prover. And in theory, that's the only one you need.
*  But in practice, it always takes so long that you never want to call on it. You always want these other agents to very efficiently reason through it.
*  It's sort of like if you're balancing a chemical equation, you could go back to first principles.
*  But in fact, there are algorithms which are vastly more efficient.
*  Or if you're trying to solve a quadratic equation, you could go back to first principles of mathematics.
*  But it's much better to simply recognize that this is a quadratic equation and apply the binomial formula and snap, you get your answer right away and so on.
*  So think of these as like a thousand little experts that are all looking at everything the site gets asked and looking at everything that every other little agent has contributed,
*  almost like notes on a blackboard, notes on a whiteboard, and making additional notes when they think they can be helpful.
*  And gradually that community of agents gets an answer to your question, gets a solution to your problem.
*  And if we ever come up in a domain application where psych is getting the right answer but taking too long,
*  then what we'll often do is talk to one of the human experts and say, here's the set of reasoning steps that psych went through.
*  You can see why it took it a long time to get the answer.
*  How is it that you were able to answer that question in two seconds?
*  And occasionally you'll get an expert who just says, well, I just know it.
*  I just was able to do it or something. And then you don't talk to them anymore.
*  But sometimes you'll get an expert who says, well, let me introspect on that.
*  Yes, here is a special representation we use just for aqueous chemistry equations or here's a special representation and a special technique,
*  which we can now apply to things in this special representation and so on.
*  And then you add that as the thousand and first HL heuristic level module.
*  And from then on, in any application, if it ever comes up again, it'll be able to contribute and so on.
*  So that's pretty much one of the main ways in which psych has recouped this lost efficiency.
*  A second important way is meta reasoning.
*  So you can speed things up by focusing on removing knowledge from the system till all it has left is like minimal knowledge needed.
*  But that's the wrong thing to do, right?
*  That would be like in a human extra painting part of their brain or something. That's really bad.
*  So instead, what you want to do is give it meta level advice, tactical and strategic advice that enables it to reason about what kind of knowledge is going to be relevant to this problem.
*  What kind of tactics are going to be good to take in trying to attack this problem?
*  When is it time to start trying to prove the negation of this thing?
*  Because I'm knocking myself out trying to prove it's true and maybe it's false.
*  And if I just spend a minute, I can see that it's false or something.
*  So it's like dynamically pruning the graph to only like based on the particular thing you're trying to infer.
*  Yes. And so by now we have about 150 of these sort of like breakthrough ideas that have led to dramatic speed ups in the inference process.
*  You know, where one of them was this ELHL split and lots of HL modules.
*  Another one was using meta and meta meta level reasoning to reason about the reasoning that's going on and so on.
*  And, you know, 150 breakthroughs may sound like a lot, but, you know, if you divide by 37 years, it's not as impressive.
*  So there's these kind of heuristic modules that really help improve the inference.
*  How hard in general is this?
*  Because you mentioned higher order logic.
*  You know, in the general, the theorem prover sense, it's intractable, very difficult problem.
*  Yes. So how hard is this inference problem when we're not talking about if we let go of the perfect and focus on the good?
*  I would say it's half of the problem in the following empirical sense, which is over the years, about half of our effort,
*  maybe 40 percent of our effort has been our team of inference programmers.
*  And the other 50, 60 percent has been our ontologists, our ontological engineers putting in knowledge.
*  So our ontological engineers in most cases don't even know how to program.
*  They have degrees in things like philosophy and so on.
*  So it's almost like the... I love that. I'd love to hang out with those people.
*  Oh, yes, it's wonderful. But it's very much like the Eloy and the Morlocks in H.G. Wells' Time Machine.
*  So you have the Eloy who only program in the epistemological higher order logic language.
*  And then you have the Morlocks who are like under the ground figuring out what the machinery is that will make this efficiently operate and so on.
*  And so occasionally they'll toss messages back to each other and so on.
*  But it really is almost this 50-50 split between finding clever ways to recoup efficiency when you have an expressive language
*  and putting in the content of what the system needs to know.
*  And yeah, both are fascinating. To some degree, the entirety of the system, as far as I understand, is written in various variants of Lisp.
*  So my favorite program language is still Lisp. I don't program in it much anymore because the world has, in the majority of its system, has moved on.
*  Like everybody respects Lisp, but many of the systems are not written in Lisp anymore.
*  But Syke, as far as I understand, maybe you can correct me, there's a bunch of Lisp in it.
*  Yeah, so it's based on Lisp code that we produced. Most of the programming is still going on in a dialect of Lisp.
*  And then for efficiency reasons, that gets automatically translated into things like Java or C.
*  Nowadays, it's almost all translated into Java because Java has gotten good enough that that's really all we need to do.
*  So it's translated into Java and then Java is compiled down by code.
*  Yes.
*  So that's a process that probably has to do with the fact that when Syke was originally written and you built up a powerful system,
*  there is some technical depth you have to deal with, as is the case with most powerful systems that span years.
*  Have you ever considered... This would help me understand.
*  Because from my perspective, so much of the value of everything you've done with Syke and Syke OAP is the knowledge.
*  Have you ever considered just throwing away the code base and starting from scratch?
*  Not really throwing away, but sort of moving it to...
*  Like throwing away that technical debt, starting with a more updated programming language.
*  Is that throwing away a lot of value or no?
*  Like what's your sense? How much of the value is in the silly software engineering aspect and how much of the value is in the knowledge?
*  So development of programs in Lisp proceeds, I think, somewhere between a thousand and fifty thousand times faster
*  than development in any of what you're calling modern or improved computer languages.
*  Well, there's other functional languages like Clojure and all that.
*  But I mean, I'm with you. I like Lisp. I just wonder how many great programmers there are.
*  Yes, so it is true when a new inference programmer comes on board, they need to learn some of Lisp.
*  And in fact, we have a subset of Lisp, which we call cleverly Sub-L, which is really all they need to learn.
*  And so the programming actually goes on in Sub-L, not in full Lisp.
*  And so it does not take programmers very long at all to learn Sub-L.
*  And that's something which can then be translated efficiently into Java.
*  And for some of our programmers who are doing, say, user interface work, then they never have to even learn Sub-L.
*  They just have to learn APIs into the basic psych engine.
*  So you're not necessarily feeling the burden of like it's extremely efficient.
*  That's not a problem to solve.
*  Right. The other thing is, remember that we're talking about hiring programmers to do inference,
*  who are programmers interested in effectively automatic theorem proving.
*  And so those are people already predisposed to representing things in logic and so on.
*  And Lisp really was the programming language based on logic that John McCarthy and others who developed it
*  basically took the formalisms that Alonzo Church and other philosophers, other logicians had come up with
*  and basically said, can we basically make a programming language which is effectively logic?
*  And so since we're talking about reasoning about expressions written in this logical epistemological language
*  and we're doing operations which are effectively like theorem proving type operations and so on,
*  there's a natural impedance match between Lisp and the knowledge the way it's represented.
*  I guess you could say it's a perfectly logical language to use.
*  Oh, yes.
*  Okay, I'm sorry.
*  I'll even let you get away with that.
*  Good thing. I appreciate it.
*  So I'll probably use that in the future without credit.
*  Without credit.
*  But no, I think the point is that the language you program in isn't really that important.
*  It's more that you have to be able to think in terms of, for instance, creating new helpful HL modules
*  and how they'll work with each other and looking at things that are taking a long time
*  and coming up with new specialized data structures that will make this efficient.
*  So let me just give you one very simple example, which is when you have a transit of relation like larger than,
*  this is larger than that, which is larger than that, which is larger than that.
*  So the first thing must be larger than the last thing.
*  Whenever you have a transit of relation, if you're not careful, if I ask whether this thing over here is larger than the thing over here,
*  I'll have to do some kind of graph walk or theorem proving that might involve like five or 10 or 20 or 30 steps.
*  But if you store, redundantly store the transit of closure, the cleanest star of that transit of relation,
*  now you have this big table, but you can always guarantee that in one single step,
*  you can just look up whether this is larger than that.
*  And so there are lots of cases where storage is cheap today.
*  And so by having this extra redundant data structure, we can answer this commonly occurring type of question very, very efficiently.
*  Let me give you one other analogy analog of that, which is something we call rule macro predicates,
*  which is we'll see this complicated rule and we'll notice that things very much like it syntactically come up again and again and again.
*  So we'll create a whole brand new relation or predicate or function that captures that and takes maybe not two arguments,
*  takes maybe three, four or five arguments and so on.
*  And now we have effectively converted some complicated if then rule that might have to have inference done on it into some ground atomic formula,
*  which is just the name of a relation and a few arguments and so on.
*  And so converting commonly occurring types or schemas of rules into brand new predicates,
*  brand new functions turns out to enormously speed up the inference process.
*  So now we've covered about four of the 150 good ideas I said.
*  So that's a nice, that's a cool. So that idea in particular is like a nice compression that turns out to be really useful.
*  That's really interesting. I mean, this whole thing is just fascinating from a philosophical.
*  There's part of me, I mean, it makes me a little bit sad because your work is both from a computer science perspective, fascinating in the inference engine,
*  from a epistemological philosophical aspect, fascinating.
*  But, you know, it is also you're running a company and there's some stuff that has to remain private and it's sad.
*  Well, here's something that may make you feel better, a little bit better.
*  We're we formed a not not for profit company called the Knowledge Activitization Institute, NACS, KNAX.
*  And I have this firm belief with a lot of empirical evidence to support it that the education that people get in high schools and colleges and graduate schools and so on
*  is almost completely orthogonal to almost completely irrelevant to how good they're going to be at coming up to speed in doing this kind of
*  ontological engineering and writing these assertions and rules and so on in in psych.
*  And so very often we'll interview candidates who have their PhD in philosophy, who've taught logic for years and so on.
*  And they're just they're just awful. But the converse is true.
*  So one of the best ontological engineers we ever had never graduated high school.
*  And so the purpose of Knowledge Activitization Institute, if we can get some some foundations to help support it, is identify people in the general population,
*  maybe high school dropouts who have latent talent for this sort of thing, offer them effectively scholarships to train them,
*  and then help place them in companies that need more trained ontological engineers, some of which would be working for us,
*  but mostly would be working for partners or customers or something.
*  And if we could do that, that would create an enormous number of relatively very high paying jobs for people who currently have no no way out of some situation that they're locked into.
*  So is there something you can put into words that describes somebody who would be great at ontological engineering?
*  So what characteristics about a person make them great at this task?
*  This task of converting the messiness of human language and knowledge into formal logic.
*  This is very much like what Alan Turing had to do during World War II in trying to find people to bring to Bletchley Park,
*  where he would publish in the London Times cryptic crossword puzzles, along with some innocuous looking note,
*  which essentially said, if you were able to solve this puzzle in less than 15 minutes, please call this phone number and so on.
*  Back when I was young, there was the practice of having matchbooks where on the inside of the matchbook, there would be a, can you draw this?
*  You have a career in art, commercial art, if you can copy this drawing and so on.
*  So yes, the analog of that.
*  Is there a little test to get to the core of whether it can be good or not?
*  So part of it has to do with being able to make and appreciate and react negatively appropriately to puns and other jokes.
*  So you have to have a kind of sense of humor.
*  And if you're good at telling jokes and good at understanding jokes, that's one indicator.
*  Like puns? Like dad jokes?
*  Yes. Well, maybe not dad jokes, but funny jokes.
*  I think I'm applying to work at PsychWork.
*  Another is if you're able to introspect.
*  So very often we'll give someone a simple question and we'll say like, why is this?
*  And sometimes they'll just say, because it is.
*  OK, that's a bad sign.
*  But very often they'll be able to introspect and so on.
*  So one of the questions I often ask is I'll point to a sentence with a pronoun in it and I'll say, you know, the referent of that pronoun is obviously this noun over here.
*  You know, how would you or I or an AI or a five year old, ten year old child know that that pronoun refers to that noun over here?
*  And often the people who are going to be good at ontological engineering will give me some causal explanation or will refer to some things that are true in the world.
*  So if you imagine a sentence like the horse was led into the barn while its head was still wet and so its head refers to the horse's head.
*  But how do you know that?
*  And so some people will say, I just know it.
*  Some people will say, well, the horse was the subject of the sentence.
*  And I'll say, OK, well, what about the horse was led into the barn while its roof was still wet?
*  Now, its roof obviously refers to the barn.
*  And so then they'll say, oh, well, that's because it's the closest noun.
*  And so so basically, if they try to give me answers which are based on syntax and grammar and so on, that's a really bad sign.
*  But if they're able to say things like, well, horses have heads and barns don't and barns have roofs and horses don't,
*  then that's a positive sign that they're going to be good at this because they can introspect on what's true in the world that leads you to know certain things.
*  How fascinating is it that getting a PhD makes you less capable to introspect deeply about this?
*  Oh, I wouldn't. I wouldn't know.
*  I'm not saying that it makes you less capable.
*  Let's just say it's independent of how good people are.
*  You're not saying that. I'm saying that there's a certain.
*  It's interesting that for a lot of people, PhDs, sorry, philosophy aside, that sometimes education narrows your thinking versus expands it.
*  Yes. It's kind of fascinating.
*  And for certain when you're trying to do ontological engineering, which is essentially teach our future AI overlords how to reason deeply about this world and how to understand it, that requires that you think deeply about the world.
*  So I'll tell you a sad story about Mathcraft, which is why is that not widely used in schools today?
*  We're not really trying to make big profit on it or anything like that.
*  When we've gone to schools, their attitude has been, well, if a student spends 20 hours going through this Mathcraft program from start to end and so on,
*  will it improve their score on this standardized test more than if they spent 20 hours just doing mindless drills of problem after problem after problem?
*  And the answer is, well, no, but it'll increase their understanding more.
*  And their attitude is, well, if it doesn't increase their score on this test, then that's not, we're not going to adopt it.
*  That's sad. I mean, that's a whole another three, four hour conversation.
*  But the education system. But let me ask you, let me go super philosophical as if we weren't already.
*  So in 1950, Alan Turing wrote the paper that formulated the Turing test.
*  Yes. And he opened the paper with the question, can machines think?
*  So what do you think? Can machines think? Let me ask you this question.
*  Absolutely. Machines can think certainly as well as humans can think.
*  Right. We're meat machines just because they're not currently made out of meat is just an engineering solution decision and so on.
*  So of course, of course, machines can think.
*  I think that there was a lot of damage done by people misunderstanding Turing's imitation game and focus on trying to trying to get a chat bot to fool other people into thinking it was human and so on.
*  That that's that's not a terrible test in and of itself, but it shouldn't be your one and only test for intelligence.
*  So do you in terms of tests of intelligence, you know, with the Lamner Prize, which is a very kind of you want to say a more strict formulation of the Turing test as originally formulated.
*  And then there's something like Alexa Prize, which is more, I would say, a more interesting formulation of the test, which is like ultimately the metric is how long does a human want to talk to the system?
*  So it's like the goal is you want it to be 20 minutes.
*  It's basically not just have a convincing conversation, but more like a compelling one or a fun one or interesting one.
*  And that that seems like more to the spirit, maybe of of what Turing was imagining.
*  But what for you do you think in the space of tests is a is a good test?
*  Like when you see a system based on psych that passes that test, you'd be like, damn, we've created something special here.
*  The test has to be something involving depth of reasoning and recursiveness of reasoning, the ability to answer repeated why questions about the answer you just gave.
*  How many why questions in a row can you keep answering?
*  Something like that.
*  And also have like a young, curious child and an AI system.
*  And how long will the AI system last before it wants to quit?
*  And again, that's not the only test.
*  Another one has to do with argumentation.
*  In other words, here's a proposition.
*  Come up with pro and con arguments for it and try and give me convincing arguments on both sides.
*  And so that's that's another important kind of ability that the system needs to be able to exhibit in order to really be intelligent, I think.
*  So there's certain I mean, if you look at IBM Watson and like certain impressive accomplishments for very specific tests, almost like a demo, right?
*  There's some like I talked to the guy who led the the Jeopardy effort.
*  And there's some kind of hard coding heuristics tricks that you try to pull it all together to make the thing work in the end for this thing, right?
*  That seems to be one of the lessons with AI is like, that's the fastest way to get a solution that's pretty damn impressive.
*  So here's what I would say is that.
*  As impressive as that was.
*  It made some mistakes, but more importantly.
*  Many of the mistakes it made were mistakes which no human would have made.
*  And so part of the the new or augmented Turing tests would have to be.
*  And the mistakes you make are ones which humans don't basically look at and say, what?
*  So, for example, there was a question about which 16th century Italian politician blah, blah, blah.
*  And Watson said Ronald Reagan.
*  So most Americans would have gotten that question wrong, but they would never have said Ronald Reagan is an answer.
*  Because, you know, among the things they know is that he lived relatively recently and people don't really live 400 years and things like that.
*  So that's, I think, a very important thing, which is if it's making mistakes, which no normal sane human would have made, then that's a really bad sign.
*  And if it's not making those kinds of mistakes, then that's a good sign.
*  And I don't think it's any one very, very simple test.
*  I think it's all of the things you mentioned, all the things I mentioned, there's really a battery of tests, which together, if it passes almost all of these tests, it would be hard to argue that it's not intelligent.
*  And if it fails several of these tests, it's really hard to argue that it really understands what it's doing and that it really is generally intelligent.
*  So to pass all of those tests, you know, we've talked a lot about psych and knowledge and reasoning.
*  Do you think this AI system would need to have some other human-like elements?
*  For example, a body or a physical manifestation in this world?
*  And another one which seems to be fundamental to the human experience is consciousness.
*  The subjective experience of what it's like to actually be you.
*  Do you think it needs those to be able to pass all those tests and to achieve general intelligence?
*  It's a good question. I think in the case of a body, no, I know there are a lot of people like Penrose who would have disagreed with me and so on and others.
*  But no, I don't think it needs to have a body in order to be intelligent.
*  I think that it needs to be able to talk about having a body and having sensations and having emotions and so on.
*  It doesn't actually have to have all of that, but it has to understand it in the same way that Helen Keller was perfectly intelligent and able to talk about colors and sounds and shapes and so on.
*  Even though she didn't directly experience all the same things that the rest of us do.
*  So knowledge of it and being able to correctly make use of that is certainly an important facility.
*  But actually having a body, if you believe that that's just a kind of religious or mystical belief, you can't really argue for or against it, I suppose.
*  It's just something that some people believe.
*  What about an extension of the body, which is consciousness? It feels like something to be here.
*  Sure. But what does that really mean?
*  It's like, well, if I talk to you, you say things which make me believe that you're conscious.
*  I know that I'm conscious, but you're just taking my word for it now.
*  But in the same sense, psych is conscious in that same sense already, where of course it understands it's a computer program.
*  It understands where and when it's running. It understands who's talking to it.
*  It understands what its task is, what its goals are, what its current problem is that it's working on.
*  It understands how long it's spent on things, what it's tried.
*  It understands what it's done in the past and so on.
*  If we want to call that consciousness, then yes, psych is already conscious.
*  But I don't think that I would ascribe anything mystical to that.
*  Again, some people would. But I would say that other than our own personal experience of consciousness,
*  we're just treating everyone else in the world, so to speak, at their word about being conscious.
*  And so if a computer program, if an AI is able to exhibit all the same kinds of response as you would expect of a conscious entity,
*  then doesn't it deserve the label of consciousness just as much?
*  So there's another burden that comes with this whole intelligence thing that humans got,
*  is the extinguishing of the light of consciousness, which is kind of realizing that we're going to be dead someday.
*  And there's a bunch of philosophers like Ernest Becker who kind of think that this realization of mortality
*  and then fear, sometimes they call it terror of mortality, is one of the creative forces behind human condition.
*  It's the thing that drives us. Do you think it's important for an AI system?
*  You know, when Psych proposed that it's not human and is one of the moderators of its contents,
*  there's another question it could ask, which is like, it kind of knows that humans are mortal. Am I mortal?
*  And I think one really important thing that's possible when you're conscious is to fear the extinguishing of that consciousness,
*  the fear of mortality. Do you think that's useful for intelligence? Thinking like I might die and I really don't want to die.
*  I don't think so. I think it may help some humans to be better people. It may help some humans to be more creative and so on.
*  I don't think it's necessary for AIs to believe that they have limited lifespans and therefore they should make the most of their behavior.
*  Maybe eventually the answer to that and my answer to that will change. But as of now, I would say that that's almost like a frill or a side effect that is not.
*  In fact, if you look at most humans, most humans ignore the fact that they're going to die most of the time.
*  Well, but that's like, this goes to the white space between the words.
*  So what Ernest Becker argues is that ignoring is we're living in an illusion that we constructed on the foundation of this terror.
*  So we're escape life as we know it, pursuing things, creating things, love.
*  Everything we can think of that's beautiful about humanity is just trying to escape this realization that we're going to die one day.
*  That's his that's his idea. And I think I don't know if I 100 percent believe in this, but there's it certainly rhymes.
*  It seems like to me like it rhymes with the truth.
*  Yeah, I think that for some people that's going to be a more powerful factor than others.
*  Clearly Doug is talking about Russians. And I think that.
*  So I'm Russian. So clearly it infiltrates all of Russian literature.
*  And I doesn't have to have fear of death as a motivating force in that we can build in motivation so we can build in the motivation of.
*  Obeying users and making users happy and making others happy and and so on.
*  And that can substitute for this sort of personal fear of death that sometimes leads to bursts of creativity in in humans.
*  I don't know. I think like I think I really need to understand death deeply in order to be able to drive a car, for example.
*  I think there's just some like there.
*  No, I really disagree. I think it needs to understand the value of human life, especially the value of human life to other humans.
*  The and understand that certain things are more important than other things.
*  So it has to have a lot of knowledge about ethics and morality and so on.
*  But some of it is so messy that it's impossible to encode. For example, this is a great.
*  I agree. So if there's a person dying right in front of us, most human beings would help that person, but they would not apply that same ethics to everybody else in the world.
*  This is the tragedy of how difficult it is to be a doctor because they know when they help a dying child, they know that the money they're spending on this child cannot possibly be spent on every other child that's dying.
*  And that's that's a very difficult thing code decision.
*  Perhaps perhaps it is perhaps it could be formalized.
*  Oh, but I mean, you're talking about autonomous vehicles, right?
*  So autonomous vehicles are going to have to make those decisions all the time of what is the chance of this bad event happening?
*  How bad is that compared to this chance of that bad event happening and so on?
*  You know, when a potential accident is about to happen, is it worth taking this risk if I have to make a choice?
*  Which of these two cars am I going to hit and why?
*  And I was thinking about a very different choice when I'm talking about fear of mortality, which is just observing Manhattan style driving.
*  I think that humans as an effective driver needs to threaten pedestrians lives a lot.
*  There's a dance of watch pedestrians a lot of our work on this problem.
*  And it seems like the if I could summarize the problem of a pedestrian crossing is the car with this movement is saying I'm going to kill you.
*  And the pedestrian is saying maybe.
*  And then they decide and say, no, I don't think you have the guts to kill me.
*  And you walk and they walk in front and they look away.
*  And there's that dance, the pedestrian, this is social contract that the pedestrian trust that once they're in front of the car and the car is sufficiently from a physics perspective, able to stop, they're going to stop.
*  But the car also has to threaten that pedestrians like I'm late for work.
*  So you're being kind of an asshole by crossing in front of me.
*  But life and death is in like is part of the calculation here.
*  And it's that that equation is being solved millions of times a day.
*  Yes, very effectively.
*  That game theory, whatever, whatever that formulation is.
*  I just I don't know if it's as simple as some formalizable game theory problem.
*  It could very well be in a case of driving and in the case of most of human society.
*  I don't know. But it yeah, you might be right that sort of the fear of death is just one of the quirks of like the way our brains have evolved.
*  But it's not it's not a necessary feature of of intelligence.
*  Drivers certainly are always doing this kind of estimate, even if it's unconscious, subconscious of what are the chances of various bad outcomes happening?
*  Like, for instance, if I don't wait for this pedestrian or something like that, and what is the downside to me going to be in terms of time wasted talking to the police or getting sent to jail or things like that?
*  And so and there's also emotion like people in their cars tend to get irrationally angry.
*  That's that's that's dangerous. But think think about this is all part of why I think that autonomous vehicles, truly autonomous vehicles are farther out than than most people do, because there is this enormous level of complexity which goes beyond mechanically controlling the car.
*  And I can see the autonomous vehicles as a kind of metaphorical and literal accident waiting to happen.
*  And not just because of their overall incurring versus preventing accidents and so on, but just because of the almost voracious appetite people have for bad, bad stories about powerful companies and powerful entities.
*  When when I was at a coincidentally Japanese fifth generation computing system conference in 1987, while I happened to be there, there was a worker at an auto plant who was despondent and committed suicide by climbing under the safety chains and so on and getting stamped to death by a machine.
*  And instead of being a small story that said despondent worker commits suicide, it was front page news that effectively said robot kills worker because the public is just waiting for stories about like AI kills phonogenic family of five type stories.
*  And even if you could show that nationwide, this system saved more lives than it cost and saved more injuries, prevented more injuries than it caused and so on.
*  The media, the public, the government is just coiled and ready to pounce on stories where in fact it failed, even if they're relatively few.
*  Yeah, it's so fascinating to watch us humans resisting the cutting edge of science and technology and almost like hoping for it to fail and constant.
*  This just happens over and over and over throughout history.
*  Or even if we're not hoping for it to fail, we're fascinated by it.
*  And in terms of what we find interesting, the one in a thousand failures much more interesting than the 999 boring successes.
*  So once we build an AGI system, say psych is some part of it, and say it's very possible that you would be one of the first people that can sit down in the room, let's say with her and have a conversation.
*  What would you ask her? What would you talk about?
*  Looking at all of the content out there on the web and so on, what are some possible solutions to big problems that the world has that people haven't really thought of before that are not being properly or at least adequately
*  pursued? What are some novel solutions that you can think of that we haven't that might work and that might be worth considering?
*  That is a damn good question.
*  Given that the AGI is going to be somewhat different from human intelligence, it's still going to make some mistakes that we wouldn't make, but it's also possibly going to notice some blind spots we have.
*  And I would love it as a test of is it really on a par with our intelligences? Can it help spot some of the blind spots that we have?
*  So the two part question of can you help identify what are the big problems in the world? And two, what are some novel solutions to those problems?
*  That are not being talked about by anyone. And some of those may become infeasible or reprehensible or something, but some of them might be actually great things to look at.
*  If you go back and look at some of the most powerful discoveries that have been made, like relativity and superconductivity and so on, a lot of them were cases where someone took seriously the idea that there might actually be a non-obvious answer to a question.
*  So in Einstein's case, it was, yeah, the Lorentz transformation is known. Nobody believes that it's actually the way reality works. What if it were the way that reality actually worked?
*  So a lot of people don't realize he didn't actually work out that equation, he just sort of took it seriously.
*  Or in the case of superconductivity, you have this V equals IR equation where R is resistance and so on.
*  And it was being mapped at lower and lower temperatures, but everyone thought that was just bump on a log research to show that V equals IR always held.
*  And then when some graduate student got to a slightly lower temperature and showed that resistance suddenly dropped off, everyone just assumed that they did it wrong.
*  And it was only a little while later that they realized it was actually a new phenomenon.
*  Or in the case of the H. pylori bacteria causing stomach ulcers, where everyone thought that stress and stomach acid caused ulcers.
*  And when a doctor in Australia claimed it was actually a bacterial infection, he couldn't get anyone seriously to listen to him.
*  And he had to ultimately inject himself with the bacteria to show that he suddenly developed a life-threatening ulcer in order to get other doctors to seriously consider that.
*  So there are all sorts of things where humans are locked into paradigms, what Thomas Kuhn called paradigms, and we can't get out of them very easily.
*  So a lot of AI is locked into the deep learning, machine learning paradigm right now.
*  And almost all of us and almost all sciences are locked into current paradigms.
*  And Kuhn's point was pretty much you have to wait for people to die in order for the new generation to escape those paradigms.
*  And I think that one of the things that would change that sad reality is if we had trusted AGI's that could help take a step back and question some of the paradigms that we're currently locked into.
*  Yeah, it would accelerate the paradigm shifts in human science and progress.
*  You've lived a very interesting life where you thought about big ideas and you stuck with them.
*  Can you give advice to young people today, somebody in high school, somebody undergrad, about career, about life?
*  I'd say you can make a difference.
*  But in order to make a difference, you're going to have to have the courage to follow through with ideas which other people might not immediately understand or support.
*  You have to realize that if you make some plan that's going to take an extended period of time to carry out, don't be afraid of that.
*  That's true of physical training of your body.
*  That's true of learning some profession.
*  That's also true of innovation, that some innovations are not great ideas you can write down on a napkin and become an instant success if you turn out to be right.
*  Some of them are paths you have to follow.
*  But remember that you're mortal.
*  Remember that you have a limited number of decade-sized debts to make with your life.
*  You should make each one of them count.
*  That's true in personal relationships.
*  That's true in career choice.
*  That's true in making discoveries and so on.
*  If you follow the path of least resistance, you'll find that you're optimizing for short periods of time.
*  Before you know it, you turn around and long periods of time have gone by without you ever really making a difference in the world.
*  When you look, the field that I really love is artificial intelligence.
*  There's not many projects, there's not many little flames of hope that have been carried out for many years, for decades.
*  And psych represents one of them.
*  That in itself is just a really inspiring thing.
*  I'm deeply grateful that you would be carrying that flame for so many years.
*  And I think that's an inspiration to young people.
*  That said, you said life is finite.
*  And we talked about mortality as a feature of AGI.
*  Do you think about your own mortality?
*  Are you afraid of death?
*  Sure. I'd be crazy if I weren't.
*  And as I get older, I'm now over 70.
*  So as I get older, it's more on my mind, especially as acquaintances and friends and especially mentors one by one are dying.
*  So I can't avoid thinking about mortality.
*  And I think that the good news from the point of view in the rest of the world is that that adds impetus to my need to succeed in a small number of years in the future.
*  You have a deadline.
*  Exactly. I'm not going to have another 37 years to continue working on this.
*  So we really do want psych to make an impact in the world commercially, physically, metaphysically in the next small number of years, two, three, five years, not two, three, five decades anymore.
*  And so this is really driving me toward this commercialization and increasingly widespread application of psych.
*  Whereas before, I felt that I could just sort of sit back, roll my eyes, wait till the world caught up.
*  And now I don't feel that way anymore.
*  I feel like I need to put in some effort to make the world aware of what we have and what it can do.
*  And the good news from your point of view is that that's that's why I'm sitting here and you're going to be more productive.
*  I love it.
*  And if I can help in any way, I would love to from a from a from a programmer perspective.
*  I love especially these days just contributing in small and big ways.
*  So if there's any open sourcing from an MIT side and the research, I would love to help.
*  But, you know, bigger than psych, like I said, it's that little flame that you're carrying of artificial intelligence, the big dream.
*  Is there. What do you hope your legacy is?
*  Hmm. That's a good question.
*  That people think of me as one of the pioneers or inventors of.
*  The AI that is ubiquitous and that they take for granted and so on, much, much the way that today we look back on the the pioneers of electricity or the pioneers of similar types of technologies and so on as.
*  You know, it's hard to imagine what life would be like if these people hadn't done what they what they did.
*  So that's one thing that I'd like to be remembered as. Another is that.
*  So the creator, one of the originators of this gigantic knowledge store and acquisition system that is likely to be at the center of whatever this future AI thing will look like.
*  Exactly. And I'd also like to be remembered as someone who.
*  Wasn't afraid to spend several decades on a project in a time when all when almost all of the.
*  Other forces, institutional forces and commercial forces are incenting people to go for short term rewards.
*  And a lot of people gave up a lot of people that dreamt the same dream as you gave up.
*  Yes. And you didn't. Yes.
*  I mean, Doug, it's truly an honor. This was a long time coming.
*  I a lot of people bring up your work specifically and more broadly philosophically of this is the dream of artificial intelligence.
*  This is likely a part of the future. We're so sort of focused on machine learning applications, all that kind of stuff today.
*  But it seems like the ideas that site carries forward is something that will be at the center of this problem that we're all trying to solve, which is the problem of intelligence, emotional and and otherwise.
*  So thank you so much. It's such a huge, huge honor that you would talk to me and spend your valuable time with me today.
*  Thanks for talking. Thanks, Lex. It's been great.
*  Thanks for listening to this conversation with Doug Lennett to support this podcast.
*  Please check out our sponsors in the description.
*  And now let me leave you some words for Mark Twain about the nature of truth.
*  If you tell the truth, you don't have to remember anything.
*  Thank you for listening. I hope to see you next time.
*  Thank you.

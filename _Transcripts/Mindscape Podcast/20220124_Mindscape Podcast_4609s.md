---
Date Generated: June 08, 2024
Transcription Model: whisper medium 20231117
Length: 4609s
Video Keywords: []
Video Views: 7983
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2022/01/24/181-peter-dodds-on-quantifying-the-shape-of-stories/

A good story takes you on an emotional journey, with ups and downs along the way. Thanks to science, we can quantify that. Peter Dodds works on understanding the structure of stories and other strings of words (including Twitter) by analyzing the valence of individual words, then studying how they are strung together in different kinds of stories. Understanding these structures offers powerful insight into how people communicate and how to reach them. As Peter says, “Never bring statistics to a story fight.”

Peter Dodds received his Ph.D. in mathematics from the Massachusetts Institute of Technology. He is currently a professor of computer science at the University of Vermont and Director of the Vermont Complex Systems Center. He has won multiple teaching awards, and was elected a Fellow of the Network Science Society.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel: https://www.youtube.com/c/seancarroll
---

# Mindscape 181 | Peter Dodds on Quantifying the Shape of Stories
**Mindscape Podcast:** [January 24, 2022](https://www.youtube.com/watch?v=x2IlaCpeuHM)
*  Hello everyone, welcome to the Mindscape Podcast. I'm your host, Sean Carroll. For today, we're going
*  to go into big data and storytelling. So I remember once hearing a conversation or maybe
*  reading about it online where someone was complaining the usual complaint about Hollywood movies,
*  how they're sort of lowbrow and predictable but frustratingly popular compared to more
*  intellectual fare. And someone else gave the counterargument saying that's because Hollywood
*  does what Aristotle told storytellers to do 2,500 years ago, to have a structure, a three-act
*  structure, dénouement, conflict, the whole bit. And there's something to that. On the one hand,
*  there's plenty of different kinds of stories. They don't all follow the Hollywood three-act
*  structure. On the other hand, it can, meanwhile I should say, it can be a little bit predictable,
*  but it nevertheless works. There's something about that kind of story that hooks us, that carries us
*  along. And there are other stories that carry us along in different ways and other people are
*  fans of those. So given this feeling that stories, which are these quintessentially human artifacts,
*  right, given this idea that they have structure somewhere, wouldn't it be great to do science to
*  that idea, to try to tease out using data, using some kind of collection of information, whether or
*  not real world stories, the stories that we'd like to listen to and stories that we tell both
*  spontaneously and from great planning, have different kinds of structure of this form. So
*  that's what today's guest does. Peter Dodds is a statistician at the University of Vermont who
*  studies big data kinds of problems in many different contexts, from earth sciences to language to
*  ecology. But he's one of the heads of what is called the Computational Story Lab. And what they
*  do is they consider individual words and they rank them. They rank these different words where
*  they have people rank them in all sorts of different ways, right, different valences for
*  are the words happy or sad or are they strong or weak, etc. And then they ask how important are
*  these different rankings, how much correlation is there between different kinds of axes upon
*  which different words have these values. And they try to seek out using math, what are the
*  most important aspects that words can have playing a role in a story. It turns out there's a
*  two dimensional framework, which is very nice. Words go from a spectrum of weak to powerful,
*  and also from safe to dangerous. Those are the two aspects, those are two axes that matter the
*  most for the impact that words have in stories. And then you can plot real stories, whether it's
*  novels or screenplays. For that matter, you can plot things like the state of the emotional state
*  of the world by looking at Twitter or looking at other social media. I'm not going to give away all
*  of the answers here, but Peter does a good job of explaining how stories do have structure. It's
*  not just our imagination. We're not just imprinting structure on it from inside ourselves. There's a
*  real sense in which successful stories have a certain kind of flow. And it's fascinating to
*  look at why people respond to the stories in different ways, which you can look at on Twitter,
*  right? What kinds of events are causing people to be happy or sad to take refuge in words that are
*  powerful or dangerous or weak or safe or whatever. So this is very early days, I think, for this kind
*  of work. It's very difficult language, humanity, meaning, it's all there. But we're beginning to
*  have these big data sets that let us ask these questions in really new ways. So it's gonna be
*  exciting to see what comes out of this kind of work. So let's go. Peter Dodds, welcome to the
*  Mindscape Podcast.
*  Thanks. Great to be here.
*  I think a good starting point for this, because as we just said seconds ago, before we started
*  recording, there's a lot to cover. But I love your invocation of the famous Kurt Vonnegut lecture
*  about the shapes of stories. And in some sense, you're taking that idea, the shapes of stories
*  and quantifying it, you know, like being a good scientist using the big data techniques to nail
*  down some numbers. Is that more or less inaccurate? It's a partial thing that you do, of course. But
*  is that an accurate way of saying one of the things that you're aiming to do?
*  Yeah, I mean, I have this kind of layout for basic science. And there are sort of two pieces,
*  fundamental pieces, which are describe and explain, just to sort of make it really simple. And I, and
*  I, and I do that, because I think it helps students understand which part they're acting on. But, but
*  coming into that is, is taste. And, you know, what do you choose to work on? What's meaningful? What
*  what, you know, that that's hard, right? But it really matters tremendously. You know, and sometimes
*  you're sort of a bit nervous for maybe years about whether things will matter. I mean, you know,
*  it's the game, right? So. But, you know, that stories to me have become more and more, you know,
*  sort of foremost in my mind of just this incredibly important aspect of, of being a human and how
*  cultures work and so on. And I know many different fields and just people in general easily have come
*  to that, right? Religions, politics, you know, politics, it's all there. I came to it from social
*  contagion, trying to think about how things spread. And that was all very sort of simplistic models,
*  you know, do you sort of, you know, wear Ugg boots or not wear Ugg boots? Or do you wear a funny hat
*  or not a funny hat? Or perhaps, you know, take on a political belief or not. But it was all sort of
*  physics is sort of model simple things. And they tell important stories about systems. And sort of
*  out of that, eventually over many years, start to sort of think more and more about the deeper
*  things that people might run around with, which are, which are stories, you know, and they can
*  range from very simple, like proverb type stories. The US has rags to riches, right? The American
*  dream is a really fundamental kind of story. And trying to, you know, so how do you then start to
*  measure those things? How do you write? And I'm really, I do come from a physics background. I
*  did. Well, I good and bad. Yeah, it's good. Yeah. So, you know, stat mech kind of stuff. So,
*  you know, just, if you look back through physics, through thousands of years, we had some pretty
*  crazy ideas about how things worked, right? And that's, that's how science has to progress.
*  But measurement just drove everything eventually, right? If you think about one of my examples that
*  I often put out as temperature, you know, measuring temperature, which we take for granted now,
*  but that, that took well in the last 500 years, hundreds of years to get to a point where people
*  like, Oh, actually, you can do that. We're pretty happy with measuring distance, you know, measuring
*  time really hard. Yeah, really hard to measure time. Well, yeah, I mean, amazing, right? It was
*  sundials for a long, long time. And, and what, you know, and time is a big piece in some of the work
*  we've done recently to like, how you experience it. But so, all right, that's a bit, bit long. But
*  the, I guess, but the big data kind of revolution, and we call it big data, because it's about people,
*  I mean, we've had big data in many fields, is, you know, there's this kind of blue collar kind of
*  honest hard work that we have to go back to, which is just let's really, really look at this stuff and
*  measure it and quantify it. And, and, you know, maybe we had a pretty good time into the 80s and
*  90s of making simple models and telling all these beautiful stories about the world. But they were,
*  you know, gloriously free of data, which, you know, if you have a beautiful idea,
*  probably don't go look at reality, right? Because you might, you might be sad.
*  Yeah. So, you know, and of course, string theory writers, you know, we've got some beautiful
*  examples in physics still. So, although that's beautifully done, because you can't really sort
*  it out. So, so that I feel it's just almost just being responsible, right? We're just trying to
*  measure things well, right? We've got these hard problems. Let's, let's see what we can do. And
*  things have changed tremendously in the last 10 to 20 years. All right. So Vonnegut, you know,
*  I think I came across this YouTube video of Vonnegut talking about it. It's probably how I
*  came across it first. And I showed it to my students. I'm like, this, we should be able to do
*  this. This is, this fits in with work that we've been doing for many years before, which was
*  measuring emotional states of populations. And some people, some people in the audience might not
*  actually be familiar with the video. So maybe remind us what Vonnegut is actually saying there.
*  Yeah. So, so it's sort of a five minute version. Fine. I think, because I think he told the story
*  in many places. It's, it's really quite charming. And so he just, he sort of lines up a graph and
*  it's a sort of ill fortune, good fortune on the, on the vertical axis, you know, good fortune to
*  the top and then time, right? So time is the big, so going to the, to the right there. And, and then
*  marks out a simple graph and it's a, it just sort of starts high and then goes down and comes back
*  up again, like a little wave, right? And then says, this is what he called a man in a whole story.
*  Right? So this is, this is a, you know, many sitcoms, many stories kind of just work like this.
*  They start off, things go wrong. They get back to where they were. And, and, and his little sort of
*  line there was, you know, people love that story. They love it. Right. It's, there's nothing about
*  plot in here. And I want to be really clear about this is just the overall emotional arc. It gets a
*  bit conflated with plots and that's, that's a much deeper, harder thing that we're trying to work on
*  as well. Like so emotional arc. So you think, all right, well, maybe we can, maybe we can do this.
*  And the, the work that we had sitting around that we built for a long time was this idea of
*  what we call a hedonometer, right? So measuring happiness, but equally sadness, I should point out.
*  And that came out of all the work from the maybe 60, 70 years now, I think of trying to measure the
*  fundamental dimensions of meaning. And this to me is really, really, I mean, this is, I actually,
*  you know, this is the most exciting thing I've ever worked on the more recent stuff about that.
*  Yeah. I mean, just thrillingly incredible. But the idea is, okay, well, let's, let's,
*  if I can kind of expand on this, like, let's give, yeah, give people, you know, so trees, cars,
*  you know, your life, like what, we have all these aspects of meaning associated with them, how you
*  feel about something and feeling and meaning allied in interesting ways. So how do you sort
*  of boil that down? Right? So we, we, we have, you know, maybe you could look at a dictionary of
*  the source and you've got this rich space of meaning and the recent more recent work that we
*  have in deep learning and so on. It's like, here are 300 dimensions of meaning. And it's like,
*  whoa, you know, what, what could go wrong with it? So we're at the absolute other end of that,
*  which is what's the absolutely most essential aspect of meaning and what was sort of, sort of
*  dug out of them over decades and through, you know, of course, initially small scale studies
*  with people, obviously students in psychology, right? It's the usual game. But here was the idea,
*  okay, we'll give you a bunch of objects or concepts of whatever, and you have to just
*  assess them on semantic differentials. And we'll give you a bunch of these. And so
*  they are things like hard to soft, good to bad, big to small, like all these kind of very natural
*  things that we're fairly comfortable with them being antonyms, right? That they represent
*  opposite ends of some spectrum. And so we, so this was done, as I said, in the 40s and 50s.
*  And the first big work was actually for pings from submarines, which is quite charming. Yeah,
*  it's a really interesting work. And it's so handlers of, you know, some people working with
*  radar, how did they feel about the sounds? Like did it kind of danger energy? What, you know,
*  what, what did it mean to them? So that, that kind of spread out from there into thinking about
*  meaning of anything. And what was sort of boiled down over many years was this idea of valence
*  being dominant. And it's a, it's a nicely inscrutable word, just, but it does generally.
*  And I think that's not unuseful, but it means good to bad, basically, right? So happy to sad.
*  It's collapsing a lot of things. And so you can imagine from an evolutionary point of view,
*  like a sort of a survival point of view, you know, you're an organism, you have a sense of what's
*  good and helpful and positive and negative. And you're, you know, you're attracted to,
*  you know, one end and you're repelled from the other. So it had this very sort of fundamental
*  aspect to it. There are a couple of dimensions that came out. And the tricky thing is you've
*  started with hard and soft, you know, light and heavy. You've started with all these very
*  sensible ones and you have to figure out then, because what's really going on, you were solving
*  like an SVD type problem, a linear algebra problem. What's the common...
*  You have to explain what SVD means.
*  Yeah. So singular value decomposition. It's a, what you're trying to figure out is if you've got all
*  of these axes, like these semantic differentials, if we sort of take the right point of view,
*  it may be that there's some way of adding them up and subtracting some from the others to get a
*  really fundamental kind of dimension. Like you might see that this shape in front of you.
*  So words have points in this space, right? There's the, you can imagine words or things,
*  but let's talk about words. So I'm going to present you with a word, you know, football or chicken,
*  and you have to rate it on all of these different semantic differentials.
*  So then it has some point in these words have a point in the space of semantic differentials.
*  And then the idea is we'll rotate that space around and play with it a little bit. And maybe
*  we see, oh, it's kind of, you know, really dominant in these ways and say that this valence dimension
*  is that's a sum of all of these things in some complicated way, but maybe, you know, the good,
*  bad semantic differential probably lines up with it. So you're taking all these words and you have
*  many different possible axes along which your students, I guess, or subjects are rating them,
*  but some just correlate exactly with others and sort of that's kind of redundant information.
*  And you're looking for what are the, what are the ways, what are the axes, if you like,
*  that matter the most? Is that a fair way of saying it?
*  That's right. That's right. And they're not, you know, it isn't any one of those
*  semantic differentials that you started with necessarily. It's some, it's some way you have
*  to pop, you have to go through that and figure out, okay, that these ones are kind of, it's,
*  you know, it's not like mass and length and those sorts of things, right? Now we're dealing with
*  categorical, it's, it's, so it takes a, you know, you have to sit down as a human, I think,
*  and really kind of think through this. So, so that's right. And, and the work that we did
*  initially to get this pedometer stuff to work was to, I mean, essentially, actually many years ago,
*  I'm trying to figure out, okay, we've got all this data coming through, like blogs. It was a little
*  bit before Twitter and Facebook really took off. But we looked at some other things like state of
*  union speeches. You know, there's hundreds of years there. Music lyrics for which we had,
*  you know, 60, 70 years. So we, we're trying to get hold of different kinds of text. So text is data
*  that represented some aspect of human behavior. You know, none of these things are complete.
*  Of course, we wouldn't want to say that. But we thought, well, we've got the stream of, say,
*  you know, words coming through in real time. Can we, can we figure out like, is this population
*  that's expressing it happy or sad? Or, you know, are they fearful or less fearful?
*  And partly inspired by some of the things that were coming out of economists around the time,
*  Greenspan 2007 and eight said, you know, he would throw out all of these mathematical models,
*  if he could figure out why people are becoming more euphoric or fearful. Yeah. It's a, I,
*  people could probably find that interview. It's on the John Stewart. It's on, it's on the daily
*  show from a long time ago. And it's a, it's quite remarkable. It's before the housing crash too.
*  Yeah. So, you know, I would carry that around as a good example, like, you know, that seems a,
*  a really basic thing to know. And of course we want to put it up against something like GDP,
*  you know, sure. The stock market's up, but are people happier or sadder? You know, if we're,
*  and it goes back to measurement. If you want to improve things where I think we're in this kind
*  of really difficult time where we can measure some big complicated things quite well, especially
*  money, or at least we think we can. And, but we're leaving out these other mushy, harder pieces
*  to measure. And as a result, of course, you try to maximize or optimize something that's,
*  and you're not measuring everything. I mean, I think people understand that, but you sort of also
*  forget it. You know, you look at the things that have charts, like the, look, it's the stock market.
*  You look under the lamp post. Yeah. Yeah. So, so that was part of that challenge. I mean, I think
*  it was a fundamental thing about people we were trying to measure as populations. And we're not
*  really trying to, we're not trying to track individuals. It's nothing that we would say,
*  oh, you said this sentence, you're happy or sad. It has to be from many, many, you know, many,
*  many words. So it's more like a, a physics fish kind of that you're averaging over lots of pieces.
*  So it kind of has an inbuilt privacy thing, if you like. We eventually created something online,
*  which is at hedonameter.org. And it takes Twitter data. And that sort of the banner thing is Twitter.
*  And you can see over many years now, 13, 14 years, this sort of long arc of what's, you know,
*  Twitter is a complicated thing. People have changed to, you know, who's actually active on it.
*  I think we have 10 languages, Russian, Korean. It's a, it's a whole thing, but it's exactly this kind
*  of index, if you like, what's the, you know, the Dow Jones index of happiness. And it has some big
*  patterns. It's been going down actually for five or six years, but more recently has been kind of
*  going up. Sorry, the happiness has been going down? Yeah, for a long, yeah, since about 2015.
*  Huh, weird. Yeah, going down. And, but the last, last year, it's been sort of slowly going up. 2020
*  was the first time we saw anything that I would call collective trauma. And, you know, I, of course,
*  there's your own personal view of things. And that's what we're trying to take out of this,
*  like what we think about things. We're trying to get the sense of a population. And, and, you know,
*  your listeners will have all of their own specific kind of feelings of how things have, you know,
*  maybe 2014 was the worst year, you know, personally, right. But we're trying to get out the whole
*  picture. And by collective trauma, what I mean is the advent of, you know, the world kind of
*  understanding there was a pandemic. We sort of knew in January 2020 that there were dangerous
*  things afoot, but it wasn't really till, I think it's March 12th, when, you know, the MBA suspended
*  its season. And Tom Hanks said he had COVID. All these things happen in about 10 minutes. And
*  President Trump at the time gave a speech sort of saying for the first time, things weren't great.
*  And so, and the stock market, of course, the stock market started to tank straight away.
*  So, so that, that was a big drop. And it also did what we'd seen in the past is there were these
*  big drops for deaths of celebrities, terrorist attacks, school shootings, you know, these things
*  that occupies, but then they really quickly been wiped out by stories, you know, like the people
*  still talked about those things, but there's just this flood of stories all the time that, like,
*  you know, of everything that's happening in the world. So there'd be drops, but they kind of come
*  straight back up, maybe a couple of days. But it took on the order of months really for Twitter to
*  sort of rebound back up to its kind of normal level at the time, which is pretty low. And then
*  George Floyd's murder was a huge drop, but it kept dropping as the protests built over the next few
*  days because of people understanding what had happened and being out, you know, expressing their,
*  you know, their feelings online or what we measured as feelings. And that was,
*  that's the lowest drop we've ever seen. And again, it took this a long time to come out of.
*  January 6th was another big drop, actually. That's probably the third lowest over the whole time.
*  So this was, you know, that's our whole, the many things have kind of come out of all of that,
*  where you can measure happiness of texts in lots of ways. And to finally get back to Vonnegut,
*  what we did was we went to books and we said, all right, let's see what he could,
*  this is this idea of Vonnegut. And he actually, you know, he says, this is so simple, even
*  computers could do it. You know, this is maybe 1990, 95 when he was saying these things.
*  And we thought, oh, we can probably do it. And so, so, so, and in fact, it turns out that I
*  think in maybe, when was it, 60s or 70s, he had, he had, I think it was the University of Chicago.
*  He wanted to do this as a master's thesis. Right. He had presented it and they said no. And he was
*  still mad about that for decades and decades and decades. You can find him, you know, talking about
*  how upsetting that was to him. So, it's sort of an homage to him in some ways, but we, you know,
*  we got a bunch of books, maybe I think 20,000. You have to sort out what's fiction. It's a bit of a
*  mess, but basically created this same hedonometer idea. But in this case, you're now sliding through
*  the book. So you're going to say, okay, the first thousand words have this score and then we'll slide
*  this little window. And we're not reading it like a person, right? We're just, it's like sometimes
*  called a bag of words method. You're just going to put them all together and slide and get a score
*  for them. Right. So not all words we have scores for. Right. And some words we, you know, say the
*  score is unimportant. Like the word the is a neutral word. Yeah. We ask people what they think of that
*  word. Right. So we, as I said, we had people do with psychology students, of course early on,
*  you know, eventually it's online and you do it with Mechanical Turk, which is an Amazon service
*  where you ask people what they think about things. Or you can use it to do all sorts of things. But
*  so, so the, you know, the scale of these studies is now really quite large. So we have scores for
*  words. Yeah. So you sort of separately score the individual words and now you're taking novels or
*  what have you works of fiction and scoring, as you say, sections of those as you go through the text.
*  And so you can see the happiness or the sadness go up and down as you read through the text.
*  Right. And you play around with the window size and you think about this. We did it for movie
*  scripts as well. Scripts are useful. They have descriptions of what's going on. So it's, you know,
*  they're actually somewhat rich. You can't get the final one, which I realized as we were doing this,
*  because I was looking at Alien and I was looking through the script and Ripley as a man in the,
*  what might be the fourth, the last script of your version of that. Anyway, so you've got some version
*  of it and you do what you can. So, you know, if you look at something like Predator starts okay,
*  and then just goes to like, it's terrible. You know, like it's just negative and drops. There's no,
*  there's no sort of, you know, ups and downs and which we're more familiar with with stories. Like,
*  so, you know, Harry Potter, the last, the definitely hell is the last book, you know,
*  really huge ups and downs as it goes through. Right. So, and, you know, I think that's,
*  we sort of think we're trying to figure out what's, is there sort of characteristic scales of,
*  right. Of fiction. So, but what came out of that and we attacked it in various ways, but there are
*  sort of six fundamental shapes, if you like, and there was a rags to riches once a very simple,
*  basically sort of goes up throughout the book, you know, may have some ups and downs, but that's
*  sort of a, you know, this is like, kind of like decomposing something into decomposing a sound,
*  you know, into its free waves or whatever. It's a bit like that. I know I want to add something
*  that's much more complicated though. So, but this is, this is, of course, we're looking at emotional
*  arcs. So we do have signals. There's the tragedy where things just keep going down. So metamorphosis,
*  maybe Kafka, right. It starts off, it starts off badly. You're a cockroach and stuff with them,
*  then it keeps going down. And then there's the man in the hole type one of Vonnegut. There's the
*  inverse of that, which we called Icarus, right. So it starts, things go really well and then they
*  go really bad. And then we had two others, which were Cinderella and Oedipus, right. So Cinderella
*  starts low, goes high, you know, you've gone to the ball with this fairy godmother stand up and then
*  things go badly again. And then, then, you know, so there's a huge rise and that's one of Vonnegut's
*  favorite little stories that he talks about Cinderella fitting this pattern. So it's a simple,
*  you know, down, up, down, up. And the flip of that we had, we called that Oedipus, right. Starts well,
*  things go bad. Then you kill your father and marry your mother. You know, like it ends, it ends,
*  it ends poorly. It ends poorly. So, I mean, yeah, just to, because sadly, we don't have the visuals
*  here for the audience, but this is, as I was, I saw your plots though, the visuals are great and
*  plots in the sense of graphs, not plots in the sense of story structures. But it is, it's,
*  I mean, what fraction of stories fit into these? Because it's a very simple kind of ex post facto
*  natural thing. There's sort of the stories that have no maxima or minima in the revolution,
*  right. It's either rights or riches or tragedy. And then there's stories with one maximum or
*  minimum and there's stories with two maxima or minima in that basic arc. Is that like,
*  are those six possibilities? What fraction of stories covered by that?
*  I mean, it's some, you know, it's, it's again, one of these things where it's like 90, 95%.
*  It's amazing. Yeah. But of this particular pool of books, right. So, you know, and this set of
*  work. So I think the future of this, of course, is to curate things really well. Like here are,
*  here are detective stories, here are stories from this particular culture and so on. So,
*  so it becomes a, and we found this with the hedonimic work in general. If you estimate the
*  happiness of a set of words, you might say, okay, maybe I can get an error measure for that. Right.
*  This is a very typical thing to do with measurement, but it turns out it was completely
*  in the lens. It's completely in the words, the list of words for which you have scores.
*  So if you change that list of words by scoring more or taking some out, you know, that's where
*  the error is. It's all in the instrument. So, you know, this, in this case, yeah, we'll,
*  we have a, it's one of these things where we seem to have a big data set. We have 20,000 books.
*  You know, that's a hard thing to read. Right. So this is, it gets beyond it. Right. I mean,
*  it's important, right. It gets beyond it. It's simple. No one's going to read 50 million tweets
*  a day. Right. And so what we're trying to do is what, what I've sort of called telonomics,
*  which is like distant measure, sensing of knowledge, right. So far, it's a genomics,
*  like far knowledge and, and because yeah, there's no way an individual can do that.
*  And then we want to get some sense of what, you know, the whole thing sort of streaming,
*  well, all these tweets stream past you in three seconds. How would you feel pretty bad? Probably
*  but, you know, taking that part out, you know, was it, is it better or worse than yesterday?
*  I want to say that the, the, the man and so the man in the whole one, which, which is this
*  favorite one of Vonnegut. So I would say that the framing of that is, is, is not great actually,
*  because I mean, you know, he's sitting there, he has a drawing so you can look like we're struggling
*  here with the podcasts, but you know, he has a drawing, so you can kind of see it in front of
*  you and it all makes sense. But men at home doesn't tell you a sense of time. It doesn't give you a,
*  an arrow, right. So metamorphosis could be men, men in a deepening hole as that turns out, but
*  you know, person in a hole, it doesn't tell you that they start. Okay. They get into the hole and
*  they get up. And the, what the, and I, I guess I think a lot about ads and slogans and so on.
*  And it struck me before the 2016 election that make America great again was the man in a whole
*  arc. And it was in four words, it tells you about the, you know, indicates something about the past,
*  the present and the future, which is, you know, really powerful. And it's, as I understand it's
*  1980, I think it's a Reagan and Bush was used in ads and like, let's make America great again. It
*  was used in posters and so on. It wasn't quite the dominant slogan, but it, it's one of those
*  ones that's really powerful. Bill Clinton used it. Lots of people have used it over the years in
*  various ways because it is, it is very powerful. I mean, and I think that, you know, as a rhetorical,
*  as a, as a story in four words, super, you know, super powerful. And do you find that there are,
*  you alluded to this a little bit, but relationships between these different kinds of story arcs or
*  valence arcs, whatever you want to call them and genre or literariness of the fiction. I mean,
*  are there certain kinds of, or do you get highbrow fiction using one kind of pattern and
*  pot boilers using another one? You know, we are working on that more now. We have some work where
*  we're looking at things like accounting textbooks and, you know, manuals for televisions and, you
*  know, just like what happened, because you want to know, like, are we getting something artificial?
*  Certainly, if you randomly shuffle text, it's, you know, it doesn't produce these shapes, right?
*  There's, I mean, as you might hope, right? So there's sort of a, we can at least get that sorted
*  out. But again, that's a curation of data and that, that I think we're still behind on. We're
*  trying to build, well, we do have this thing called Story Wrangler. That's at storywrangling.org.
*  And it's for Twitter at the moment. But the idea is to kind of house all of these different
*  bodies of work and have a time series for the usage of words within them. So that hopefully
*  eventually will be something that could kind of go towards what you're saying. We do, of course,
*  have Google Books, which has been around for about 10 years now. The problem with that, I think,
*  is that it doesn't have enough metadata. You can't really sort out the sort of broadly fiction,
*  broadly everything. And as it turns out, we did some work on it and we figured out that
*  actually the kind of collective English stuff is full of science. There's a lot of medical and
*  science typewriting and the 20th century is basically dominated by the sort of rise of
*  science. And you can see it in little details like figure with a capital F, it just goes up.
*  And like et al. And all the things to do with data really actually about the exponential growth of
*  science, which is sort of understood, I suppose, in the 60s to sell the price,
*  presumably armed with a million graduate students went through libraries figuring out
*  what the memory was in journals and how much stuff was being published. Anyway,
*  that's imprinted in there in a way that we can't. Well, it makes sense. I think I noticed on your
*  web page that the most commonly used word on Twitter is RT, the abbreviation for retweet.
*  That doesn't really mean it's the most commonly used in English, but on that particular medium,
*  that's what pops out. Right. And you have to say, what are you looking at? Twitter is interesting
*  because it does kind of encode so much and the news is for sure there. I mean, another way to
*  look at all of this is to think about forests. So we have a forest and you would like to know
*  all of the species in the forest, which is actually, of course, very hard to measure
*  and have accounts for them. Right. How many are there of all these different species? So this is
*  this comes out of linguistic, but the types and tokens distinction, like how, what are the,
*  all of the, what's your lexicon, which would be for language. Here's your list of words.
*  And then here's your list of all the animals and organisms. And then you have next to it,
*  the counts. Right. But then you want to do that over time. So maybe for forests, it's at the scale
*  of a year. There are studies that do this for small parts of forests, but that's the kind we're sort
*  of looking at forests of words and stories and trying to see how they change over time. And of
*  course they can change dramatically. I mean, let me, I don't want to lose track of this other thing
*  that we mentioned and then he sort of buried it in the, in the happiness versus sadness discussion,
*  but there are this, there is this multi-dimensional way of thinking about the
*  words and you've, you've done your factor analysis, try to figure out what dimensions matter the most.
*  And why don't you tell us what, what those dimensions are that matter the most?
*  Yeah, I actually just wrote that down. So the, so this has been, I think I'm really excited. I mean,
*  it's still in review, so we'll see what happens, but we're, we're pretty confident about all of
*  this. So, all right. So we had valence and this, and when we sort of saw that at the time in the
*  literature, that this, these were the dominant, this is the dominant axis. And certainly when you
*  look at the data back then, and I think we're looking at data sets that had a thousand words
*  with scores associated with them. So it's not a big set of words, right? People's vocabularies
*  are tens of thousands, you know, you know, something like Twitter with all its misspellings is hundreds
*  of, yeah. So, but you know, you want something on that order and over time, what has happened,
*  of course, there have been bigger studies done and done in slightly different ways. And so we've
*  gotten, just as you might hope in science, you know, more accurate, richer works. Back then,
*  12, 13 years ago, the, the main idea of what was going on was there was valence, which is this happy,
*  sad, good, bad kind of access. And there were a couple others though. One was about dominance,
*  like, do you feel in control or not in control? When you, when you kind of consider something.
*  And there was another one, which is activity. It's very, got various names for it, but basically
*  kind of activation. Is this exciting or boring? So there have been these other sort of secondary
*  dimensions that people have had flowing around and then sort of debates about which ones matter.
*  Okay. So we've got this work from, we didn't do this, this study, but a couple of years ago,
*  it's worked by Mohammed in Canada. Again, online, many, many people doing these evaluations. And now
*  we've got 20,000. Now it's 20,000. So there's a huge jump from say a thousand and work that we did,
*  which got to 10,000. And they're mostly good kind of words, right? They don't have people's names
*  or events, which can be a bit of an issue with some of these large sets of words.
*  All right. So the idea was the, the people were going to evaluate these on valence and what was
*  called arousal, which is the activation one and dominance, right? So you've given these three
*  dimensions and that it is tricky. How do you present that to people? So you kind of have to
*  give them kind of clouds of words at each end. So they kind of know that, you know, the positive
*  end of valences, you feel good, you feel happy, you feel maybe comforted, you know, it's a bit
*  spread out, but that's fine. Everyone's given that same, you know, the same instructions,
*  but looking harder at this stuff. And then again, doing this kind of factor analysis,
*  you can see you've got this kind of, now it's a three-dimensional space. Maybe the,
*  maybe it doesn't come back like in the dimensions you've actually tried to impose that you've tried
*  to say to people, you know, we think these are the fundamental dimensions. That's good,
*  but you can see like what they actually think, you know, maybe they correlated some of those.
*  And that actually turns out to be the case. And if you sort of rotate this football and kind of
*  squeeze some of the axes and pull some of them apart, you get another shape. And it has these
*  two main, well, we played around with it for a while, but it has these two main axes and the
*  one going across, if you like horizontally is powerful power of weak, right? So power over here
*  is like for people would be success, triumph, if you sort of go back to people. So it's kind of
*  winning. And then the weak end of that is void and nothingness. So it's not failure, it's just
*  emptiness. So that's going across the page. And then up is pointing up and, you know, this is our
*  choice danger. So this is like a compass for basic meaning. And so danger is up and safety is down.
*  And we call this, all right, we make up words, but it was the oseometry, right? So oseometry means,
*  I mean, we're taking it to mean essence, it's a Greek word, but it is where the word essence comes
*  from. So O-U-S-I-A. And we felt, I mean, it's fun to make up words, but it was also like, it's not
*  semantics, it's not semiotics. It's, and we're not measuring meaning, we're measuring, and that's
*  somehow it's depicted. We don't want people to think that we're measuring essential meaning if
*  you distill everything down. So we've tried this out with many different corpora. So things like
*  the Sherlock Holmes novels and stories, short stories, Jane Austen's works. So they're sort of,
*  you know, famous authors, and then a huge collection of fiction from Google with sort of
*  complicated things, but it's 120 years. So that's everything sort of smushed together equally.
*  Wikipedia, a snapshot of Wikipedia, which is a, you would think, just a different object.
*  Talk radio. So that's transcriptions of talk radio. So now we're going for spoken word,
*  it's been turned into text, but that's a different, it's spontaneous, it's different,
*  it includes everything from, you know, NPR to sort of shock jock stuff, right? So it's a big grab bag.
*  The New York Times as well, 20 years of the New York Times. And so we look, so this is this type
*  token distinction again, right? So that's sort of first work where we found this dangerous safe
*  access and power weak access was looking at types, like every word got one vote. And so we kind of
*  figure it out. And that's good, but it's just the substrate. And then you have to go and see what
*  people actually, you know, what in these different venues and beyond, how do they use these? How often
*  do they use these? Now I want to do this with all of my podcast episodes. I have transcripts for all
*  of them. I want to know which ones are powerful or weak or dangerous or safe. Yeah. No, I mean,
*  I mean, we kept, and when those ones I just listed, you know, we didn't do them all at once. They were
*  sort of like, you'd kind of like corral the data and then kind of do the same analysis again.
*  And I remember every time thinking, will this be different? What, you know, what's going on?
*  They're all a little bit different, of course, but all of them have what I'll call is the safe,
*  safety bias that the predominance of words that people use are in this, in this lower half of this
*  kind of this, this disk, if you like. And it's words that are trend, trend towards being safe,
*  you know, at the bottom of things like comfort. If you want to go out to safe week, you get the
*  words like sofa and tortoise and then, you know, safe and powerful words like wisdom and happiness.
*  And that turns out that quadrant, that's what I'll call the safe, powerful quadrant, it sort
*  of lines up with positivity and happiness. And there's this much older work that we built on
*  when we looked at large text, which is, which came up with this idea of the Pollyanna principle,
*  that in general interactions between people, and so this communication of all kinds,
*  there are more positive aspects than negative ones. It's a bit surprising to people, I think,
*  because, you know, it's easy to kind of bring to mind arguments or negativity on maybe online,
*  or the news is terrible, you know, these sorts of things. But if you think society exists,
*  it can not exist, but it does exist. And it does hold together for lots of little sort of positive
*  interactions. And I, so this was work, this is maybe six or seven years ago. What was so I mean,
*  I didn't expect this was surprising, I sort of popped out that there are more positive words
*  than negative words. That's just and it's true across. We looked at 10 major languages, 24
*  corpora, you know, Russian, German, Korean, Indonesian. So we, we looked at a lot of different,
*  different pieces there, and it really kept coming out. So and, you know, there was a sort of a story
*  there. I mean, that that it's languages are great social technology. Right? We're excited about
*  Snapchat or something. But you know, really, language is this unbelievable thing that we have.
*  Money is another one. Because we've somehow encoded belief into this abstract thing. It's
*  pretty good. I remember correctly, though, that in fictional stories, in particular, there's more
*  danger than you might expect. Or I mean, then then you have an ordinary language, because obviously,
*  a story wants to be exciting somehow. It's a good question if it's more so. So all of them have on
*  average, a positivity bias. Okay. Now there are parts where they dip below into this negative
*  side of things. But, you know, if you look at music lyrics, one of the first things we looked at
*  the way and they kind of told us that we were getting somewhere, the rankings, so at the bottom
*  is heavy metal. Right at the bottom of the graph. Yeah, well, this is like ranking, like taking John,
*  this is something where we were and you did ask about genres for fiction, but this is actually
*  something where we did have genres. And on this, this is on the happiness one. Okay, so this is,
*  yeah, and at the top is gospel and soul. Right. So it kind of makes the ordering look pretty good for
*  this very rudimentary instrument we'd made. But even, you know, heavy metal was still above
*  neutral on average, right? Still good to know, even though, yeah, it's just so. So if you look at a,
*  you know, maybe Harry Potter or something, when things go bad, it does dip into this negative
*  thing, which is pretty hard because you've got to use a lot of negative words, because on average,
*  the bulk of words are over in the positive side of things. Or at least, you know, there's a skew
*  towards positivity. So the generalization of that now is that in fact, it's a safety bias that we're
*  not just, it's not really positive. It's that we're using more safer words and dangerous words.
*  You know, they're incredibly important. They describe all of these things that can go wrong.
*  We just don't use them as much. And when we use them, of course, they're incredibly meaningful.
*  But so happiness is basically, yes, is safety plus power. And one of the things, the other thing that
*  I thought was really fascinating was different stories that you looked at have character,
*  you can associate characters in the narrative with, you know, along this dangerous versus safe
*  and powerful versus weak axis. And I guess Harry Potter had like all sorts of characters,
*  like, you know, they're dangerous ones, weak ones, etc. Whereas in Game of Thrones,
*  almost everyone's powerful and a lot of them are very dangerous. It was more like a very
*  clash of extremes in that in that way. So that that work, again, it's like completely
*  thrilling to me. This is just incredibly exciting, because it comes from a completely
*  different data set. So this is a sort of an online thing. Again, not something we did, but
*  but it went back to giving people characters from stories. And there are a lot of TV shows and
*  movies, but there's also Pride and Prejudice, right? So there's some some books are in there.
*  And zooming out and presenting, it's about 100, it might be 200, but 150 of these semantic
*  differentials. So sort of going way back in time in a way and giving people, you know,
*  so it's for characters. So this country, city, you know, the kind of rich poor, there are things
*  that may be a little more, you know, clearly assigned to people. So we were able to sort of
*  start again with a really rich set of semantic differential. And I think there are about 800
*  characters that we looked at over 90 different, I'll call them story versus right, this Buffy,
*  the vampire slayer, the spec files, you said Game of Thrones, it's a it's a rest of development is
*  in there. It's really a big spread. So I think there's something for everyone, right? You might
*  not know 80% of them, but there'll be some that you could look at. So so so this is a completely
*  different data set. And doing this analysis again, and, you know, turning things around and kind of
*  rotating spaces, and not really doing anything funny, where we're saying we're desperate to find
*  this power danger thing, it really popped out for free. So this is something that's just, you know,
*  very sort of supportive of what we've done in this other space. And there is a third dimension,
*  I should mention that one, because it's, in general, it's about what we call structure. So
*  structured to unstructured. So a rock, you know, has has a stronger structure level. Cardinal,
*  bureaucracy, boss, right? These are these are considered more structured, but clown and conical
*  and tickle. These are these are words that go out confetti, they're considered unstructured. And so
*  for characters, it's playfulness. It's much more about playfulness. So someone like, you know,
*  Robin Hood, right? Is is is has a playful measure on them, or molder from the X files is,
*  is playful. Scully is not playful. Not a lot of playfulness in Game of Thrones. Pretty much all
*  of them are in the danger. Pretty much all of them are in the dangerous, powerful quadrant,
*  which is the dominant, you know, these are the, this is like dangerous winning, basically, you
*  know, things can go wrong for you. Except for gonna get his name, Samwell, Tarly, if you know,
*  Tally, yes. So he's he's in he's down in the kind of the the angel character. So Jane Bennett is
*  there from Pride and Prejudice. These are people who are, you know, they're, they're, they're more
*  towards the safe axes, the stolen somewhat powerful, but they're more in the safe. So these
*  are just really, really good people. That's who you find down the bottom. If you go around,
*  safe into the kind of weak quadrant, then you get people who tend to, you know, they're not bad
*  people, but they tend to get run over. And again, and out in the weak side, you get Mike, you know,
*  Michael Scott from the office, Homer Simpson is out there. And then I wanted to say that if you go
*  further up, you get this is where Joffrey is from Game of Thrones. There aren't many from Game of
*  Thrones in this. What's what's the dangerous weak quadrant? Yeah, okay. And that's the chaos agents.
*  They're the chaos agents. And again, I guess this might be future research, but you have this
*  time series of, you know, how the valence of the story itself evolves page by page. And now you're
*  saying there's a there's a different set of analysis with sort of the the distribution of
*  characters, or distribution of whatever events and so forth. And how if you just gave me that,
*  like if you didn't tell me the plot, right, or the characters or the setting or whatever,
*  how much could I learn? How much I infer about the story just by thinking about, you know, both how
*  evolved over time and what kinds of characters are involved? Do we know that yet?
*  I mean, we are really trying to do that. And I think it's remarkable. So I sort of think of
*  characters, the shortcut to story, right? So we as what do we do with stories, right? A lot of them
*  are about prediction, they're about telling us how the world works. Proverbs do this stories that
*  we listen to, like these are ways that your life can go, or maybe other people's lives can, we're
*  trying to make sense of the world. And there are certain, you know, we tend to have stories wrapped
*  around individuals, which I think is interesting, you know, because we want to be in them. So it's
*  hard for us to tell stories about systems. And that's why, yeah, I mean, when it comes to complex
*  systems, and all these sort of front of it scientists work on, it's really hard, right?
*  Because people want to anthropomorphize everything. They absolutely do. And I understand,
*  you know, I understand that drive, but it's hard for us to tell a story. So, but I think one of the
*  things, so, you know, stories are incredibly important, sort of what I'm trying to say there,
*  but we also can shortcut them by just saying, oh, here are what these characters like,
*  here are archetypes. And we sort of know what will happen if you say here are these three people,
*  and here are they, we can kind of try to predict what will happen. So I think they're like little
*  kind of wind up toys, right? So, you know, in our brains, we will try to simulate, we'll run the
*  dynamical system of these characters interacting. It's very natural, we want to do it, we want to
*  predict, you know, to a fault, obviously. So what we're trying to do now with this is,
*  this is tough, but you want to get the, this sort of danger power profile around a character,
*  and how it might evolve through a story as well. There's the temporal network of which characters
*  are interacting with each other, we should be able to get that out. And with the environments,
*  right? And there are, you could imagine doing this for Star Wars, or Lord of the Rings,
*  or something like that, or, you know, Pride and Prejudice, any of these pieces. So what,
*  can we kind of trace that through? And it might be pretty rough, you know, we divide books into
*  thirds or something, but then we could, you know, do 100,000 stories and get out what are the big
*  patterns. Breaking in and seeing this kind of this two dimensional space has been, you know,
*  very helpful in a lot of ways. I mean, I think it's really what it is. Another space we've looked
*  at, perhaps just to start with this is Twitter, because we've worked on that a lot. But looking at,
*  at least what was expressed on Twitter for the January six, right, the the attack on the Capitol,
*  what you see there is, you know, just taking all the tweets and scoring them is, you know, measures,
*  it's sort of these, these measures of energy, like high energy that I'd sort of mentioned before.
*  And happiness kind of goes down. But really, what you see on this kind of compass of
*  essential meaning is that it really points straight to danger, it actually goes straight
*  to danger, right. So sorry, I'll put danger, which is, you know, danger is kind of high energy plus
*  badness, in a way, is sort of the to use these kind of other frameworks. And it so, so in that
*  respect, you'd see it, you know, it goes down as being a sad thing on our hedonometer. But that's
*  just a projection onto that axis, right? It's a shadow of the real direction, which was pure danger.
*  That's very interesting, especially because one of the questions I was going to ask was,
*  if you're looking at happiness versus sadness on Twitter, that's obviously very interesting thing.
*  But when I actually looked at the data, you know, everyone's happy on holidays, that that's a clear
*  winner, right? Christmas. Or at least you put out your happy tweets on Christmas. And then everyone's
*  sad when there's a terrorist attack or a shooting. Okay. But other events like a presidential election
*  are more of a mixed bag. And I'm wondering if there are the simplest possible thing I can think of is
*  just a measure of the variance, right? Like, is it something where a whole bunch of people are happy
*  and a whole bunch of people are sad at an election result? Or is that something that you've quantified?
*  Yeah, we have it. We just haven't put it on the site. And I think that's, you know, you're exactly
*  right. So how much, you know, to what degree are people in unison about something? And for the
*  extreme things, just in some ways, they have to be right, just for those scores to be so high and so
*  low. But you know, so you're quite right. So there is a predictability to the big spikes in positivity.
*  And there are just annual holidays, right? And so people are using the, you know, the expressions of
*  that time, you know, even happy Valentine's Day. Now, if you look at the words being used and compare
*  them maybe to some other dates, you can see that there's really some negativity in there as well.
*  It's being swamped by this kind of positive, right? So Valentine's Day will have lonely,
*  right? But it's being kind of wiped out. And Christmas might have that as well. Or so it's a,
*  it's not so you want to be a little careful. It's just, it's not like everyone is, you know,
*  doing that. And you can see for days of the week. So Saturday is generally the most positive day.
*  Tuesday is generally the most negative day. But Saturday, you know, it has movies, weddings,
*  you know, like there's lots of positive things that might happen on Saturday,
*  but also has bored and hangover. You know, there are some, you know, not all, it's not all great
*  for everyone on Saturday. And there's a daily rhythm too, right? Yeah, there's a strong daily
*  rhythm, which I kind of, I think it's actually in science makes it, I have this line, which is,
*  it's the daily unraveling, unraveling of the human mind. So we kind of, I know sleep remains a
*  mystery, but I think we need to be rebooted because I think we just become emotionally unstable.
*  But you know, that's, that's, I'm being funny, but you see swearing goes up through the day,
*  cursing goes up through the day. And, you know, things, yeah. And then like you sort of say,
*  the variance goes up as well. The emotional variance goes up through the day. So people
*  start off fairly tight, like things are okay, but it's not emotionally varied as well. Right.
*  And then the wheels kind of come off as the collectively.
*  I mean, if you're, if one is being a little bit skeptical here, is it possible that,
*  you know, I might think a lot of people are happy at 7pm because they're enjoying dinner or movie
*  or whatever, but those people are not on Twitter, right? How much of a bias do we have by the fact
*  that Twitter is our data stream here? Yeah, no, that's a weird, it's a weird selection,
*  but I will, I will say that more generally, if you zoom out, it does match up with Gallup polls.
*  Okay. Right. Which, which is kind of wild, right? And then we've done some, we have some other
*  instruments. There's one we've called the lexico calorimeter, which takes in phrases from Twitter
*  and assigns them as to whether they're kind of food stuffs or about exercise,
*  and then assigns calories to them. And so it's at the state level for the US,
*  but the rankings you get out of that, because you sort of get this calories in calories out,
*  which we're not, you know, we're not sort of, it's a very rough, silly thing, but it matches it,
*  it lines up with obesity rates. So you can tell which states have higher obesity rates from
*  Twitter is what you're saying. Yeah. And you can look at what you can look at what they're talking
*  about. Right. So Colorado does come out number one for mine, at least in this time we looked,
*  it was sort of three, I think. But had a, I was overly fond of talking about bacon, which didn't,
*  which sort of pushed down the top. I would have thought, you know, Coloradans are pretty healthy,
*  outdoorsy people. I don't know. So there's lots of skiing and running and biking. Those words are
*  there. A lot of bacon and donuts. Yeah. Well, that, that whole thing is quite amazing to look at
*  because the, the ground state though, if you like forever, what, what's being expressed in terms of
*  food and an exercise is pizza and watching television because we have a lot of activities
*  and some of them include like lying down as an activity, but what watching television is,
*  is one. So, so the States differ from that, but their baseline is pretty uniform in terms of what
*  is being expressed. And of course that's advertising, that's all sorts of things. It's a,
*  it's a bit of a, a melange of, of inputs. And this brings back something that you mentioned
*  right at the beginning. And I thought it was actually, I mean, maybe I had not thought this
*  way before, but I really certainly should have, which is that we very often talk about the
*  traveling of ideas and sharing and contagion of ideas or notions or opinions through social
*  networks and other networks, right? An idea might be, you know, universal healthcare or
*  the right to bear arms, but stories can also travel through these information networks
*  and narratives. And is that either something you've done or is it a target to sort of
*  tease out which stories, which narratives are being shared and how useful they are?
*  Cause I'm certainly willing to believe that a good compelling narrative wins every day over a set of
*  facts, no matter how true they are. Yeah. I have this thing where I say something like,
*  never, never bring statistics to a story file. Right? I mean, it's, it's not going to work out
*  for you. So you've got to, you should bring the numbers, but you've got to bring stories as well.
*  Right. I mean, it's just, it's just how we kind of operate. And of course people in politics,
*  people in religion understand this, have been telling, figuring out how to tell stories about
*  things for a long time. So it's absolutely a long-term ambition to do that. It's very hard, but
*  what, you know, we have this sort of framing of story writing, like how do you get out
*  the stories that people are expressing around an event as it happens, and then maybe long-term. So
*  say the Parkland shootings, shooting, it's a terrible event, just to pull one out of the many.
*  How do you sort of track the stories that emanate from that? And I, by that time in history, I was
*  pretty sure that there will be a lot of conspiracy theory type things. And sure enough, like I
*  remember going on YouTube the next day and just searching for Parkland and 18 of the top 20 hits,
*  which was sort of presented as 20, were conspiracy theory things about, you know,
*  that was all faked, it's false flag and so on. So how do you measure that in real time? I mean,
*  this is, this is an enormous, enormous goal. That's, it's very hard. And then, and then, you know,
*  so maybe there's a blossoming of stories after some event because it's just confusion. Which ones
*  are then fighting against each other? Which ones start to win? I have notions of stories, you know,
*  I'm kind of having hierarchies to them. You want to be able to tell your story simply. And that's
*  where slogans, I think, you know, have this great effect. And they might not be tethered to some
*  bigger story. Certainly religions work in that way. You want to be able to sort of say things
*  quickly. You know, it's this hierarchy of narratives that you want to be able to deliver.
*  No, it's, it's, it's an incredibly difficult problem. But I, but I think, I think that framing is,
*  is, well, I won't say the right one, but I think it's a very powerful one to be thinking about what
*  are the stories people are telling? And how much are they reducing stories to sort of characterization?
*  You know, just, so for example, pizza gate, that story is pretty out there, right? I mean,
*  it's pretty out there that there, there's a basement in this comet ping pong place,
*  and there are terrible things happening to children. And there's a cabal and all this sort
*  of stuff. That's a little hard to grasp. But I think the access in there is really through
*  character. And so Hillary Clinton, for example, being characterized as a, as a, this evil person,
*  as you know, to use folklore kind of things as a witch, then you say this story about her,
*  and you're like, sure, because she's, she's the devil. Or if you know, someone else is sort
*  of framed as a godlike character, they can do no wrong. And, and you say some story about them that
*  suggests they've done a bad thing. It gets, it's deflected. It's washed away, you know, what are
*  the defense mechanisms built into stories is a really big part of me. How do you, how do stories
*  become hermetically sealed or story versus if you like? Yeah, I mean, I know that politicians
*  are very focused on the idea that they want to paint their opponents and themselves in certain
*  ways. Like there's certain kinds of criticisms you can make that that just don't stick to certain
*  people because they don't fit the narrative in exactly that way. And finding exactly that kind
*  of weak point, how do you paint someone as a bad character in a way that is consistent with what
*  people already think about them is one of the secrets to political success. One thing I've
*  thought about with this danger of power kind of framework is, is, is a sort of flipping between
*  saying your opponent is dangerous and weak. Yes. And it doesn't seem to matter, right? I mean,
*  we sort of know that in politics, you can kind of say lots of things. And if it doesn't stick,
*  you know, you just keep moving on. But they try, they're very, they're really trying, you know,
*  in our framework, orthogonal attacks, right? They sort of literally orthogonal attacks. So you're
*  trying to say this person is, is in a sense, quite powerful and dangerous. Or, you know, maybe the
*  next day you want to say, you know, they're feckless and weak. And that's a, that's a sort of a
*  kind of a funny attack. So really incredibly hard problems. And look, there's a, there's a
*  huge danger to this as well, right? I mean, being, of course, being able to manipulate stories and,
*  and kind of measure them and do all these sorts of things and see what the weak points are in
*  a system. Disinformation, people work on this all the time. I think one of the, something I keep
*  reflecting on is, you know, for scientists and, and journalists, my, so my wife's a journalist, and
*  there's, I always sort of think of journalists as scientists with a deadline. So we're, we're trying
*  to figure things out and tell the truth about something and kind of explain things, right?
*  You know, broadly is a big piece. That's a huge battle for us because there's this,
*  the possible stories you can come up with that are not true, but are favorable to a viewpoint
*  or a culture or whatever, infinite, right? There's just an incredible number of things to maybe,
*  you know, what's adjacent to it, to the true story. You can, you can really explore some stuff and
*  find the stories that will spread faster, that will, you know, tack on to people's existing
*  beliefs. So that, you know, that just, this is going to be a challenge. It's always been a
*  challenge. It's just in sort of a time of so much information, right? So much availability,
*  so much ability to curate and kind of create story versus that are misleading
*  online that you can be taken into. It's, it's, it's, we, we have to work really hard on this.
*  This is hard. So I went to the web page for the He Denometer. I encourage everyone to check it out
*  and it's searchable, right? You can look for all sorts of wonderful things. And so just to
*  normalize my own expectations, I searched for the frequency of the word quantum because this is
*  something I'm interested in and it doesn't have a lot of, you know, high rates of appearance in
*  news stories, but occasionally. And what you find is probably what I should have expected ahead of
*  time, which is that there's a sort of baseline, which is pretty normal and there are spikes and
*  the spikes are pretty extremely noticeable, but I don't know what the spikes are from, right? I mean,
*  clearly there was some story about a quantum computer or something like that. Maybe my book
*  came out. I don't know, but that would be great. But so how much of that sort of
*  back engineering, reverse engineering can you do when you see something weird happening in the data?
*  Oftentimes in the big stories, you just know what it is, but is, is, are there objective procedures
*  for figuring out why the words are shifting in these different ways on different days?
*  Yeah. So a number of pieces here, this has been an eternally interesting, difficult problem.
*  What happened? Yeah. Like what happened? Right. And I remember early on, you know, maybe 15,
*  even 20 years ago, looking through Google, trying to find out what happened on a particular day.
*  Right. It was kind of hard, like, and then Wikipedia emerges and if you would, of course, has,
*  has entries for every date of history, so I suppose now, but certainly in the modern times,
*  and they're sort of weird lists. It's just a weird list of things that happened in the world. You
*  know, there was a Star Trek convention, there was, you know, this war started. I mean, it's a real
*  mixture of the concept. So with, with some of what we've got there, story wrangling, for example,
*  if you click on a, on a point, it will, it will take you to Twitter and search Twitter for that
*  date. And you will sort of show you which tweets are being amplified on the day, potentially.
*  So tweets get deleted, it's a bit of a problem. So maybe it doesn't hold up. But that's something
*  where we, you know, it depends on the sort of restrictions. Yeah, we have 10% of all tweets
*  going back to 2008, but we can't, you know, sort of share them and put them out wholesale. So we've
*  tried to do something there by pushing it back into the, you know, the actual structure itself
*  of Twitter. Google Books, for example, you can't really, it's harder to do that, right. It's harder
*  to go back and search for Google Trends, you kind of want to figure out like, why is this thing being
*  talked about? So at least I think with Twitter, we have that to some extent, we have another big
*  body of work, which really is connected to this trying to figure out exactly this what happened
*  on a particular day, or a particular week. And we did it around Trump. Just, I mean, it's president,
*  it matters. It's a very good test case. And I think it certainly 2015, 2020, and kind of, you know,
*  still now, really what I called a turbulent time story, story turbulence has been really high,
*  right. So excuse me, that turnover of stories has just been kind of incredible. And I remember sort
*  of thinking in 2016 17, like, especially 2017, I think, can you remember what happened the last
*  two weeks? Can you say, you know, I didn't say it was a challenge, right? There could be massive
*  events like Space Force or something, or, you know, you just there's only something sort of.
*  Yeah, there's only something and I, you know, look, the world's a rich place, but it was a
*  an effort to sort of study that. So we have this thing, which is kind of computational timeline,
*  reconstruction, and it works through Twitter, but it could work through anything. So we could do it
*  through, say, a state has archives, for example, going back in time, or, or any kind of news source,
*  you know, maybe the New York Times, what are the sort of narratively dominant terms, like,
*  words and pairs of words that kind of pop up? And these kind of act then like keywords into
*  bigger stories. So they're not telling you, say, you know, buying Greenland, it doesn't tell you
*  like the whole story of Greenland, but it would, you know, this is referencing Trump, but it would
*  sort of point it out. But, you know, early on, what we're able to see there early on was that
*  there's there's a lot of turbulence in that first year 2017, there was just a lot of change over.
*  There were also just natural disasters, Hurricane Maria, and so on. So these things came on, but
*  there was North Korea, you know, sort of provocations, and then Charlottesville happened
*  the next week. It's hard to remember the orderings of these things. So, so it, it, we have a timeline
*  that, you know, that kind of comes out computationally. And what you see in 2020 is
*  just this really just sudden change into coronavirus, as we call COVID coronavirus,
*  initially from for many months, just being the dominant story every day for months. And
*  we have a measure, we call it chronopathy, you can see that time functionally slowed down because
*  there was just not so much turnover in stories. It was always the same dominant story.
*  George Floyd's murder explodes the narrative. And, and then but that becomes stuck again,
*  too, because that becomes a durable story. So and then of course, we get to the election and things.
*  So you can quantify the impression we all have that sort of time froze once the pandemic hit.
*  Right. And people said that so they said, you know, people say this anecdotally all the time,
*  you know, yesterday felt like a week. I'm gonna I saw one tweet was like, I'm gonna write an
*  autobiography of my last the last 10 years of my life. It's called 2020. You know, like,
*  so I don't mean it's a very physics ish sort of thing, like time dilation and so on. But this
*  was a memory, you know, at the population scale. Did things seem to really, you know, maybe it
*  wouldn't have maybe you know, there's just sort of turnover, it doesn't really matter. But in fact,
*  you have 14 days in April 2020 is kind of, you would have the same sort of turnover in two days
*  in 2017. And it's a weird, it's a weird thing. I know I had David Eagleman on the podcast a
*  while ago. But like, there's this weird mismatch between simultaneously one says, nothing is
*  happening. And time seems to last forever, right? Even though so the rate at which time passes is
*  sort of inverse to the rapid rapidity with which things happen. An exciting movie seems to go by
*  very quickly. Yeah, yeah, no, that can be and it depends how much you're recording, you know,
*  in your own mind, right? There are studies of how people Yeah, so when when something is usually
*  around something sort of dire or terrible happening, you know, an accident, you have this
*  seeming slow motion replay of it in your head. And it's because you were really kind of writing
*  down the memory. I mean, that's what I understand, right? You were really recording it and kind of,
*  you have it in fine detail. But that there's a lot that goes on in life, right? And we know we miss
*  most of it, the sounds and the things, you know, they just sort of pull past this is a too much to
*  measure for one person. So our brains are pretty well, problematically good, perhaps, at just
*  ignoring things that don't fit our little narrative right now. I mean, there's certainly a lot that
*  we've covered that is going on here. I do it's wonderful to have this conversation, because I
*  get the impression that a lot of the excitement when you're doing is still ahead, like we've just
*  started picking some of the low hanging fruit. But I guess one final question, which you did allude
*  to earlier, but we can take these ideas and turn them around and put them to work, right? I mean,
*  maybe either in artificial intelligence, or in political campaigns, or in writing a screenplay,
*  you know, like, can we figure out can we distill what would be the perfect narrative or the perfect
*  time structure of valence or something like that? Are people trying to operationalize these ideas
*  in that sense? Yeah, so there's a lot of work over the years. And you can maybe make a fair amount of
*  money of saying you can predict which things will take off, right, because of your analytic tool. So
*  I think what we can do is say, look, here's the shape of your story, you know, here are the kind
*  of tropes you've used, and so on. And this is how it compares to others around. And, you know, maybe
*  give people that sort of a diagnostic like that. Now, in terms of making something take off for sure,
*  well, so this is the problem, right? Reality is socially constructed. We have all the work on,
*  yeah, we have all the work on fame. And of course, many people kind of come to this in different ways
*  that show if you have kind of basically run the world over and over us for cultural social things,
*  it doesn't always, there's a lot of variability, right? Harry Potter doesn't win in every,
*  every universe, it certainly didn't win for the first 12 or 13 editors who said no, right? Like,
*  how could they not know? How could they not know, right? They're professionals, right? But how could
*  they not know that this would be this giant thing? And that actually indicates how much fortunate
*  luck the fact that there's an enormous runaway success in something right, the world is full of
*  these right, whether the number one thing is so much bigger than the second one, and the third
*  one, right? These heavy tail distributions, that it's indicative of actually, what we'll tell is,
*  you know, what our simple story for that is the Mona Lisa is fantastic, for example, like it is
*  intrinsically amazing, you know, if you look at it, you will be transported, and it's because of
*  this and this and this. But we just leave out completely the social construction aspect,
*  it's because it took 400 years to get to that idea that it was the greatest painting in the world.
*  And there's a whole set of reasons for why it became increasingly famous that are
*  not intrinsic, you know, stories around it. But it's a good example of something where,
*  you know, you can't really kind of, I mean, I guess that's the point of view, like, you can't
*  get it, you try to make things as good as you can, and you want them, you want to make them
*  spreadable, that's important that people want to tell other people about it. I think that's the great
*  thing. And of course, that works for disinformation as well. Right? So what will
*  spread in the social wild, right? This is the great problem of advertising, right? This is sort of
*  probably made up one, but, you know, half the money is wasted in advertising, we just don't know which
*  half. And so, you know, it's sort of true, like, very unexpected things happen and take off. And
*  how did you not know that? Well, there's a lot of social construction that goes on. But so it
*  wouldn't be anything that would guarantee the future of some social phenomena, but it would
*  serve as a, I think, can serve as a diagnostic. I worry about the negative aspects, you know, I mean,
*  but I think we have, like all of science here, we have to know that we have to know the things,
*  right? So we can start to build defense systems. And I think AI, for example, what we'll call AI,
*  or sort of certainly the modern work with, with language and all of these kind of crazy instruments,
*  you know, they've gotten a little, they've gotten way ahead of us, right? We're trying to make
*  decisions about, you know, injuries or parole or something like that, or presenting things that
*  turn out to be deeply racist or whatever. And, you know, and, you know, we've got this, we've got
*  ourselves way beyond describe and explain and into the sort of create category of, of science. And,
*  you know, we need, we, I think, I mean, I think it's turning around, people are looking at the
*  corpora and so on, that they've built some of these systems out of. And, you know, I'm really
*  relieved to see that happen. Because I think there was a wild time there. And we got ourselves,
*  you know, like Facebook's algorithm, right? What, which things spread, right? You have
*  dials that you turn to make certain things spread or not spread. You can change the social
*  contagion there. And that's, you know, it's, it's, yes, there's money on one side, but there's also
*  just, you know, does society hold together on, on, on another side? And I think that's, I think
*  that's important. I guess there's also a feedback question, right? I mean, there's this David Lodge
*  novel I read from the 80s. And he mentions very, very early efforts in digital humanities, where
*  you would, you know, digitize someone's book and figure out what words they used more often than,
*  than the typical English language. And this author was, was shown, you know, that you use the word,
*  you know, moist or whatever, way more than average. And once he found out those words,
*  he couldn't write anymore, like, because he was too self conscious about doing it. And I wonder
*  if we figure out too much about, you know, what the shapes of these stories are, and everything,
*  how that's going to affect how we tell them ourselves.
*  Yeah, there's some parallel there, I suppose. Yeah, scientists, classic science move just look
*  too deep. It's like trying to understand comedy and destroy everything. Right. So yeah, thanks.
*  Thanks, scientists. No, I think I would hope it would just get, I mean, people are incredibly
*  creative. You know, people are incredibly creative. We find new ways to tell stories where we're in a
*  time where we have so many stories in the past that we kind of play with them and so on. It's,
*  it's, you know, it's, I think it's, I don't, I don't think it will stop all of that. It could
*  produce, I can produce some stuff that's not very good. I think that's, that maybe is the problem,
*  where you try to build formulas too much and so on. So that, that, that could be a slightly
*  more dangerous. Fair enough. Well, all right. I will just repeat. Thanks, scientists. I like that
*  as a motto and Peter Dodds, thanks very much for being on the Mindscape Podcast.
*  Sean, it's been a great pleasure. Thank you.

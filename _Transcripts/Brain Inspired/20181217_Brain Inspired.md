---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3564s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 10518
Video Rating: None
---

# BI 022 Melanie Mitchell: Complexity, and AI Shortcomings
**Brain Inspired:** [December 17, 2018](https://www.youtube.com/watch?v=l5jXVEEcPIg)
*  Driving, as we all do every day, in different kinds of situations, it's really almost you
*  need all of intelligence to do it.
*  You need common sense.
*  And common sense is something that computers lack.
*  There's a quote I have in my book, which is from back in the 60s or something, someone
*  said that artificial intelligence is at least 100 Nobel prizes away.
*  Oh, that's like the only right person in the history of this, right?
*  This is Brain Inspired.
*  Hello everyone.
*  This is me, Paul Middlebrooks.
*  Today my guest is Melanie Mitchell.
*  Melanie's a computer scientist, a machine learning researcher, and a complexity expert.
*  She's a professor at Portland State University and an external faculty member at the Santa
*  Fe Institute, where all that complexity work happens.
*  We kind of jump around and cover a lot of ground today.
*  Melanie wrote the award-winning book on complexity called Complexity, a Guided Tour, which has
*  been out now for almost a decade.
*  She's just finished writing a new book called Artificial Intelligence, a Guide for Thinking
*  Humans, which you'll have to keep your eye out for since you can't pre-order it yet,
*  and it's in the final stages of copy editing and such.
*  We talk about the current shortcomings of deep learning with respect to general AI,
*  which she writes about in her recent New York Times op-ed that you may well have read.
*  Melanie has provided the world with a valuable service, providing free online education in
*  the field of complexity at complexityexplorer.org through the Santa Fe Institute.
*  They have a lot of free courses and tutorials.
*  It's really a great resource, so you should check that out.
*  We also talk about complexity during the show, the topic in general and the role that it
*  has and or may have moving forward among AI and neuroscience.
*  And then of course Melanie graciously answered some of my more speculative questions at the
*  end as well.
*  Okay, and I tried something new this week.
*  I brought the old joke of the show back, but instead of putting it in the intro here, I
*  tried it out live on my guest, Melanie.
*  So one of the most valuable skills I learned in graduate school was how to give a talk,
*  either a talk describing my own research findings or even in a journal club, for instance, summarizing
*  and critiquing a paper.
*  And when you give a talk, especially early on in your development, as you know, there
*  are two excruciating moments.
*  If you're like me, the most excruciating moment is just before the talk, that nervous
*  anticipation before beginning, waiting as those seconds tick by, waiting to be introduced,
*  etc.
*  But there can be another excruciating moment, and that is after the talk, when you ask whether
*  there are any questions.
*  And what follows is often a silence that seems to last for an hour before someone finally
*  asks a question.
*  And that silence, you have to get comfortable with it.
*  Well, I felt that deafening eternal silence once more, but this time it was at the end
*  of my attempt at AI humor.
*  You can judge for yourself how comfortable I felt with it.
*  But I can tell you this, it's never good when you have to explain the joke to someone.
*  But screw it.
*  I left it in.
*  I left the bombing joke in.
*  Well, I appreciated Melanie's response, actually.
*  She makes no attempt to give a fake courtesy laugh.
*  And she has a good sense of humor, as you'll hear.
*  And I appreciated having her on the show.
*  I think that you will too.
*  There are lots of links and information in the show notes this episode, which you can
*  find at braininspired.co.uk, slash podcast, slash 22.
*  You can also support this ad free podcast by contributing two or four dollars per month
*  through Patreon.
*  Just go to braininspired.co and click on the red Patreon button there.
*  The support continues to trickle in.
*  It is wonderful to know that you value this show enough to contribute to it.
*  So thank you to those who have contributed, and thank you in advance to those of you who
*  contribute moving forward.
*  Okay guys, enjoy the conversation, and carry on with all the hard work that I know that
*  you are doing.
*  Remember, it's all a process, and it's all worth the time and effort you're putting into
*  it.
*  But you already know that.
*  All right, here's Melanie.
*  Melanie Mitchell, thank you for being on the podcast today.
*  Ah, very happy to be here.
*  So I will have introduced you during the introduction, and it may well have taken most of the hour,
*  but we'll introduce you more in a second here.
*  But just to not bury the lead, I want to know first of all how the reaction has been from
*  your recent New York Times op-ed about how dumb AI is these days.
*  Well, I've gotten a lot of reaction, as you can imagine.
*  Both mostly positive, a little bit of pushback from AI folks.
*  Oh, sure.
*  Okay, yeah.
*  A little bit of the pushback is mostly, yes, we all already know that.
*  Of course, that's true, but there's a huge amount of progress being made every day in
*  AI, and there's no reason for pessimism.
*  That's kind of the pushback.
*  It's interesting.
*  I guess the AI section in the New York Times is a thing now.
*  Yeah, that's right.
*  It's got its own section, its own dedicated reporter, and so on.
*  Actually, my neighbor brought your article up, and that's what I said to him as I said,
*  I think AI researchers all know that already.
*  It'd be interesting to find out if they don't or what proportion believes otherwise.
*  Right.
*  I mean, I think people who actually work in the field agree with everything I said.
*  I mean, I don't think there's a question about that, but the question is sort of what do
*  we do in response, and are we going along the right path now with deep learning, or
*  is there something else we need, or do we need to do something completely different?
*  There's all kinds of debates about that.
*  On the other hand, I don't think the general public knows what to think.
*  Okay, but they don't ever know what to think about any science topic, really.
*  That's true, but even people who are educated in science, they get so many mixed messages
*  about AI and how far it's gotten and what its capabilities are, and we get all these
*  headlines telling us that AI recognizes objects better than humans, or it's better than humans
*  at XYZ, and none of the nuances or caveats really come through.
*  Right.
*  And on the other hand, we hear that AI is... You actually interact with things like Alexa
*  or Siri, and you see that these things don't really understand what you're saying.
*  Right. The same could be said for my crazy aunt, but that's a different story.
*  I might argue with that one. I don't know your aunt, but...
*  Believe me, you wouldn't argue. Okay, so let's back up, and we might get into some of the more
*  nuanced issues in that regard. And let me just introduce you a little bit more.
*  So you're a professor at Portland State University. I've loved Portland every time I've been,
*  and you're an external professor at the famed Santa Fe Institute. You are a computer scientist
*  sort of at the core, but you're an expert in complexity science and machine learning,
*  and you have projects in modern machine learning techniques that we could talk about.
*  I'm sure you're tired of hearing this, but you did graduate work with John Holland of genetic
*  algorithm fame, and you did work in that regard too. Just as a side, he figured prominently in
*  a book that I cannot find because I can't remember the name of it, but it was about the history of
*  money and I guess economics as well. And genetic algorithms had something to do with figuring out
*  some... It was fascinating. It was a fascinating book. You wouldn't think it would be because it's
*  about money. And you did your PhD dissertation work with Douglas Hofstadter of Gödel Escher Bach
*  fame. And could you just pronounce G-E-B, Gödel Escher Bach?
*  Gödel Escher Bach. You got it. It was perfect.
*  And you actually read the whole thing. How did you achieve this?
*  It took a while, I admit. I read it right after college or during and after college.
*  And it was just fascinating to me. It was the best book I'd ever read, the most engaging and
*  mind-opening book. And you never had to put it down and
*  start over a few months later. It just really drew you in?
*  Yeah, it absolutely drew me in. I majored in math in college, and so I had some of the math
*  background and I'd already encountered Gödel's theorem. So I knew a little bit about that stuff.
*  So it wasn't like the math put me off. And the verbosity didn't put you off?
*  No, not at all. I loved it. Maybe there are two kinds of people in the world.
*  I cannot get through the book. I've tried three or four times and I appreciate it. And I liked
*  metamagical femmas as well. But those are more shorter snippets, I suppose,
*  parlays into the material. Well, that's very impressive. And maybe you cross that threshold
*  and then you've soared ever since. It reminds me, do you know the professor Terence Deakin?
*  Have you heard of him? Yeah.
*  So he wrote a book called Incomplete Nature. Don't tell me you've read that as well.
*  No, I haven't. But I've heard of it. Well, I'd love to hear what your take is on that,
*  because it's a torta force as well. It's a tome. But whereas Gödel Escher Bach is very
*  accessible and readable, this is just opaque. And he has really great theories. And you really
*  want to be able to get through it. But it's written in such a manner. I'm not sure that it
*  was ever edited, for instance. So it's just really difficult. So pick that one up and we'll talk
*  again in a year. Okay.
*  And see what you have to say. Okay, sounds good.
*  So like I said, you're an external professor at the Santa Fe Institute, where complexity is the
*  theme. And you launched what's called the Complexity Explorer in 2011. And you were the
*  first to teach an intro to complexity course, which is a free course offering through the
*  Santa Fe Institute and through complexity explorer.org. You're also a well regarded
*  author of complexity, a guided tour, which is in my Amazon cart right now. And in contrast to what
*  we were just talking about, it gets rave reviews, how well written it is and how accessible it is,
*  even though it has this really large breadth. So congratulations, belated congratulations.
*  Thank you very much.
*  And I know that you have a new book coming out about pig farming in Sub-Saharan Africa, right?
*  That's the other Melanie Mitchell. Yeah.
*  So just what's your new book coming out?
*  My new book is on artificial intelligence. It's called Artificial Intelligence,
*  a Guide for Thinking Humans. It has a title now.
*  Yes, it has a title. Great.
*  And it's essentially done. The editing process is now essentially done.
*  And now I guess the final copy editing has to be done and the production of the book and all of
*  this takes a long time and it's going to be out in early fall 2019.
*  So it can't be pre-ordered right now? Unfortunately, no.
*  When it is available, I'll have to have you back on and just to talk about that.
*  This would be terrifying to me. The idea, because I've thought about making sort of
*  an introductory online course for the overview of topics in deep learning and AI. And I'm just
*  terrified that as soon as I would finish it, it would just be a moot point.
*  Yeah, that's an interesting question is like how fast is the field actually moving?
*  In some sense, it's moving very fast. There's thousands and thousands of new papers every year
*  and it's really hard to keep up with everything that's going. On the other hand,
*  if you look at it kind of the forest instead of the trees, I don't think it's moving all that
*  fast to be honest. In terms of how fast, how close we're getting to what many people would
*  consider sort of true AI, AI that is like the kind we see in the movies.
*  Right. Human level AI, people call it all kinds of different names, but AI that really in some sense
*  understands the world in the way that we do and can deal with the world in the way that we humans
*  can. So there's progress in very narrow areas and in very narrow areas, AI is exceeding human
*  ability. We've seen that for many years with, for instance, playing chess. Now we have playing Go,
*  certain video games, but in more everyday kinds of tasks, there's been a huge improvement in
*  speech recognition. We've seen that, although it's still not at human level, contrary to some
*  headlines. It has trouble with accents, it has trouble with noise in the background and so on.
*  And there's been some huge improvement in some aspects of computer vision and translation of
*  languages, but it's still very far from being at the level of humans and really autonomous
*  that in the sense that we're able to trust it completely and not have to make corrections
*  after the fact. Okay. I was thinking we might start with complexity, but let's go ahead and go
*  down this AI road and then we'll come back to complexity and then circle around and talk about
*  them together hopefully. And I was going to save this for later, but sometimes during the show,
*  I, the only reason I really do this show is because I, so I can come up with AI jokes.
*  Can I try my latest on you here? First try here. So you ready? Yeah. All right. So these two robots,
*  Waynon and Judith were talking to each other and Waynon says, Oh, Judith, it's been really rough
*  for me lately. Everywhere I look, I just see spots. Like everywhere I look, I see spots.
*  And Judith looks at Waynon and she's like, Oh, that sounds so awful. Have you seen your machine
*  learning technician? And Waynon says, no, just spots. Okay. I'm going to,
*  that one needs some tuning up. I'll enter the rim shot there.
*  It's a meant to be a joke about how ungeneralizable in language, especially, especially
*  so the original joke goes, the guy's talking to his friend and says, all I see is spots. And his
*  friend says, Oh, have you seen a doctor? And then his friend says, Oh, no, just spots. So that's
*  something that more we recognize. Okay. I'm still putting the rim shot in. Yeah. So, so, so this is
*  kind of what your New York Times article, uh, op-ed was about. And you've given talks about this same
*  subject and I'll link to one of the show notes and you link to it on your website, which will also
*  be linked in the show notes on the current limitations of AI. Like we were just talking
*  about here. And you point out that we have seen this movie before this excitement of, Oh, we're
*  on the brink. And then, and then we have to pull back because it's followed by disappointment.
*  So there's this oscillation and excitement and disappointment. And you think that we're prepping
*  for another disappointment. I don't know if you'd call it an AI winter, but that we need to put the
*  brakes on our optimism perhaps with our current state. Yeah. I mean, you see it already happening,
*  especially for instance, in the field of self-driving cars that, you know, for several
*  years we've been, people have been predicting, Oh, we're going to have self-driving cars in,
*  you know, a year in just a few, you know, a few months by 2020, we'll have, you know,
*  autonomic fully autonomous self-driving cars. It's very, we do have self-driving cars, but they're
*  not ubiquitous. Well, and they're not fully autonomous. True, true. The term self-driving
*  car, if you sort of ask a non-expert person, what does that mean? They would say, Oh, you get into
*  the car and it drives you around and you don't have to do anything. You can just like watch a movie in
*  the back or sleep or take a nap. Well, we're pretty far from that now. And the self-driving
*  car companies in fact are taking steps back. And if you wish, if you like, you know, AI puns,
*  they're putting the brakes on the original claims. You know, the company Waymo, for example, they
*  just launched a self-driving taxi service in a small area in, I think Chandler, Arizona,
*  where the regulations are pretty lax. But they, instead of having the car, they said originally
*  where there's going to be no safety driver, you know, snow human that they can take over when
*  needed. But now they put safety drivers back in the cars because they realize that they really need
*  them. Well, it's a, it's a huge liability too. I mean, even profit wise, they're going to get
*  bankrupted by accidents, right? And so if they, if they just take that away and it's a huge claim to
*  make, but it actually behooves them profit wise, I think, to put the humans back in, not just
*  ethically. Right. But I think most people are realizing the actual technology is harder than
*  people thought, you know, we're 90% of the way there probably, but the last 10% is always the
*  hardest part. Right. Right. And that driving isn't just people have had cars, autonomous cars that
*  could drive on the highway, you know, maybe without changing lanes since the 1990s that's been around,
*  but driving in its full blown, you know, instantiation of what he, you know, driving as we all do every
*  day on different, in different kinds of situations, it's really almost, you need all of intelligence
*  to do it. You need common sense and common sense is something that computers lack. And in fact,
*  that's well known in the AI community. And there's a huge amount of money now from the government and
*  from entrepreneurs and so on going into research on common sense. Well, I know you're an advocate
*  though, and an optimist with self-driving cars for the future. Like you hope that they become,
*  because it's not hard to better a human on average human. Of course, 80% of us are better
*  than average drivers, but I think it in the future, I agree that self-driving cars would be a great
*  way to go. Right. And I think that what's going to have to happen is not only will the technology of
*  self-driving cars get better, but also the infrastructure itself will have to adapt because
*  self-driving cars, it's going to be hard, as you say, you know, the very last couple of percent
*  is going to be really hard. So for example, one thing that a self-driving car is hard for
*  self-driving has to do is to figure out like, what do you do in a construction zone? Right. How do
*  you interpret the like the hand signals from the construction person guiding traffic? Well, there's
*  going to have to be some other method that they can communicate with the self-driving car in a
*  different way that is easier for the technology to deal with. And so I think the infrastructure
*  is going to meet the technology. You know, it's going to have both sides are going to have to
*  adapt. That's an interesting, I was talking to Matt Botvinick last week, who is the head of
*  neuroscience research at DeepMind. And he said something along the same lines when talking about
*  getting to general AI that just as important, if not more important, is giving these AI agents a
*  richer environment to traverse through. Right. And that's along the same lines because we're
*  right now, it's really limited in these games that we're giving it. And even like these,
*  like first person kind of here's a triangle to go through. Here's a thing to explore the environment
*  and that we're limiting their learning in that respect as well. And he thinks that we could do
*  it in the world, but that robots aren't ready. And there's so many hurdles, like a self-driving
*  car has so many hurdles to overcome that we probably should focus on a simulated environment
*  and making that richer. Right. I think that's the right thing to do. Of course, it's hard to capture
*  everything about the world in a simulation. Yes. You know, we don't live in the matrix yet.
*  That we know of. Yeah. And people talk about, you know, there's this notion of edge cases,
*  right? This is like a buzzword in AI. And these are the unlikely things that might happen that
*  are outside of a machine learning systems training set. For instance, you're driving in a car and
*  suddenly in the middle of the road, there's a snowman. I just, you know, I like it. Yeah.
*  I don't know. Some weird thing happens, but it's rare. You know, it doesn't happen all the time.
*  But if you have millions of self-driving cars all over the world, some edge case is going to
*  happen to many, many of those things all the time. You should plow through the snowman, right? That's
*  what you should do, right? Well, I guess it depends. Not if there's a little kid in the process
*  building it. Right. Of course. Yeah. It really depends. So that's part of the whole common sense
*  issue. So edge cases, you know, we talk about the long tail, right? The long tail of probabilities.
*  And there's many things in the long tail that for any individual car or agent, they're not going to
*  happen. But collectively, a lot of these edge cases or long tail cases are going to happen.
*  And humans use common sense to deal with them. Right. And they don't, you know, it's hard to get
*  all those edge cases into simulations. So it's not like we can just have a system that is trained on
*  every kind of possibility. We have to have systems that are able to abstract the way humans do,
*  make generalizations, make analogies. And that's, that's really the core of what general intelligence
*  is all about. Well, is this what you mean when you talk about the barrier of meaning and understanding
*  and that that's what we're sort of up against in the modern deep learning environment?
*  That's part of it. Yeah, absolutely. A huge part of it is this ability we have, we humans have,
*  to look at a situation that we're encountering and to say, this is very much like a previous
*  situation or this is analogous to something else that I learned about. So I know what to do here.
*  And machines are not yet very good at that kind of generalization or analogy.
*  There's another side of the understanding part, which is all the vast amount of background
*  knowledge that we humans have just by living in the world, you know, by growing up and having a
*  body in the world. You know, we know all kinds of things about how objects interact with other
*  objects and how living systems are likely to work. We have these sort of predictive abilities
*  about different kinds of systems that it's very hard to program in or have machines learn about.
*  We could go down the embodied cognition road here. Do you want to just talk about one or two
*  ways in which like a current deep learning system fails with respect to this, you know,
*  background knowledge and understanding and meaning?
*  Sure. So here's one example. You can train a deep learning system to recognize a school bus
*  in photos and videos, et cetera. They can just, you know, you show it a picture of a school bus
*  and it says school bus. 96% correct, right? Something like that. Yeah. Or even 100% correct,
*  perhaps. School buses are easy. However, people have shown that for instance, photos of school
*  buses, if you add some kind of filter to the image, like that blurs it in certain ways,
*  the deep learning system no longer can recognize it, even though it's quite recognizable to humans.
*  Humans will get it 100% still. Yeah, essentially. Whereas there's some kind of feature that it's
*  responding to when it says, yes, I'm, this is a school bus that's different from what humans are
*  responding to. And then going further, the deep learning system doesn't, it doesn't really know
*  what a school bus is. It doesn't know that a school bus usually drives children to school.
*  It doesn't know that a school bus in the middle of the afternoon, you know, one o'clock
*  PM, it's likely to be empty because school goes from, you know, eight to two or whatever. It
*  doesn't know that the driver is usually an adult. You know, there's all kinds of things about these
*  concepts that we just know that these machine learning systems, there's really no clear way
*  to teach them all these things. So this is actually something that you're working on. And
*  um, how is this related to the situate system that you're working on? You want to just tell
*  us about that real quickly? Or? Yeah, I mean, I don't think this is sort of the research
*  that my research group is working on right now. It's not going to solve this problem per se, but
*  we're trying to get computers to make sense of what we call visual situations. That is,
*  instead of just identifying an object like, oh, that's a school bus. That's a, you know,
*  that's a Dalmatian. That's a lamp post to try and make sense of how the objects interact with
*  each other. So, you know, if I say this is a situation of a school bus picking up children
*  in the morning, that's a different situation from a school bus driving and then a group of children
*  doing something else. You know, I can identify a group of children. I can identify school bus,
*  but school bus picking up children is a whole situation that where the objects are related
*  to one another and the actions of the objects are doing certain things. So, and so it's what's called
*  situational awareness in human parlance, right? Visual situational awareness. Yeah, you could call
*  it that if you want. Oh, well, I was wondering if that's where the inspiration for the name
*  came from. No, I see that as more of like a, I don't know, it's more of a like a
*  situational awareness has kind of a military connotation. Oh, does it really? Yeah, I mean,
*  I think that's a term that DARPA has used for some of its programs. All right, I'll just,
*  I'll delete that whole segment then. Yeah, but recognizing situations, that's something that
*  humans do. That's all they do in some sense. And we do it in a very flexible way and computers are
*  not so good at doing that. Well, okay, so just to go back to your example of the school bus.
*  So what you're describing is called an adversarial example, right? Where you can
*  trick a machine learning algorithm very easily. So I wasn't, when I talked about blurring filters,
*  that actually wasn't an adversarial example. That was just doing some manipulation to the image.
*  That's right. So maybe you could- An adversarial example, yeah, an adversarial example is
*  kind of an intentional malicious manipulation of the image so that the image is not,
*  to a human the image is not changed at all. Looks exactly the same. It looks exactly the same.
*  Yeah. But you've added some very carefully structured changes to individual pixels in
*  the image so that it will fool the neural network to thinking that the image is something completely
*  different like an ostrich. These are easier to describe with pictures too, but I'm sure you
*  painted it well for the listeners. So yeah, so you can, and this is, this is again getting at the
*  point that machines are not perceiving visual scenes in the same way that humans do. Right.
*  They see them very, very differently. And that makes them vulnerable to these kinds of malicious
*  attacks. And it's not just images. People have shown that you can do this with sound.
*  You know, I can take something that you're saying and I can make change so that to humans,
*  it doesn't change it at all, but to your smart speaker, Alexa, whatever it thinks it's saying
*  something completely different, whatever I want it to say.
*  The wave forms are changed enough that it encodes that difference, huh?
*  Yeah. And you can do it to, for instance, people shown that you can create these stickers that you
*  can stick on stop signs so that a self-driving car thinks it's a speed limit sign or something else.
*  Yeah. Well, there's so much room for foibles in this world, you know.
*  Right. And these, these are only the things that like the good guys have been showing. Look,
*  this is a problem. You can do this, but you know, there's bad guys out there too, that are trying to
*  come up with attacks on these systems. Right. They're not being so upfront about it, perhaps.
*  Right. Exactly. They're not publishing their results.
*  So in your talks, you give a lot more examples of all these shortcomings of the current state
*  of deep learning. Yes. Yes. You can recognize a bus a hundred percent of the time in the pictures,
*  but here's what you can't do. So we won't go through all of them. One of them that I thought
*  was interesting, given that I spoke with Matt Botvinick last week, is the inability for an AI
*  system currently to explain its decisions. And so I should say in all of these domains,
*  there are people working on all of these things, which is a great thing. I mean, it's producing a
*  lot of work and a lot of good work. So the inability to explain its decisions is kind of
*  the black box problem wrapped up with the black box problem of we don't even understand ourselves
*  how they came to the decision and they can't explain it to us. So how would we really interpret
*  what they're doing? And one of his recent papers, they're trying to build theory of mind into AI
*  systems so that they're not explaining what all the units are doing, but making an abstract concept
*  that then they can explain to humans and to other AI agents at the abstract level,
*  more like what humans do. So I thought it's an interesting, he says cheeky. I thought it was an
*  interesting push as well into that. Yeah. Yeah. I think that's something that one of my fellow
*  graduate students working with Douglas Hofstadter also worked on. We had a system that could make
*  analogies in a very idealized world, you know, simulated world, if you will. And my colleague,
*  Jim Marshall, wrote a program that would give a kind of running narrative of what the system was,
*  in some sense, thinking about as it process. This is not your copycat program.
*  Well, this is a program called MediCat, which reasoned about what copycats was thinking about
*  in some sense. I see. So copycat was your dissertation work? Yeah. That's right. But
*  this whole idea of theory of mind is something that we humans have. It's very important to us
*  because we're social creatures, right? We have to be able to predict what other people are
*  thinking about, what they're feeling, what they're about to do. But it's very hard,
*  something that AI has been around for a long time, trying to do that. But it's very difficult.
*  Well, we don't even understand the neuroscience of theory of mind. So.
*  No. And that's, you know, a big issue. I think we don't understand neuroscience.
*  And I think people underestimate the complexity of it. Hey, now, I'm a neuroscientist. Take it easy.
*  Of course. Of course. We don't understand anything. Right. It's a pretty complex system.
*  It's really complicated and it's hard to understand. I mean, there's so much going on in there.
*  Just to sort of wrap up this, the AI part of our little discussion here,
*  I'm curious, given your article and what we've just been talking about,
*  your best guess, what do you think the proportion of AI researchers that believe, hey, like this is
*  the real time that we're at the cusp now of general AI, we just need to figure out a couple
*  more things. What proportion of AI researchers do you think are of that opinion?
*  Wow. It kind of depends on what you call an AI researcher, but I would say very small, very small.
*  Yes. Maybe 5%.
*  Oh, that's reassuring. Okay.
*  That's a guess.
*  What is your outlook for implementing these things that are needed as common sense,
*  understanding, background information for implementing enough to, I won't say for
*  implementing general AI, but maybe let's say for getting on the right track to eventually
*  implement general AI once we tweak and figure out how they all work together, where all these
*  necessary ingredients will come together. Right. Again, it depends on what you mean by
*  general AI, but if you want to have something that in some sense can do everything that a human
*  can do in the same way a human can. Let's call that general AI.
*  Yeah. I definitely come over to the embodied AI side where I really don't think that without
*  having something like a body that's acting in the world, the same world we are, that we're going to
*  get there. That's my feeling.
*  And do you think that we need to emulate human brain processes and human cognitive processes
*  to get there or is there another way?
*  I don't know. I really don't know. It's possible there's another way, but I don't think anyone
*  has any clue what it could be.
*  Dang it. I was hoping that you would tell us.
*  I wish I could, but I think our best bet is to look more at our own brain processes and
*  cognitive processes.
*  Well, I want to hear how complexity figures into all of this because you are a complexity
*  expert. And by the way, I'm just a couple hours from Santa Fe. So next time you're down there,
*  I want to go. I know it's hard to...
*  Where are you?
*  I'm in Durango, Colorado. I'm a retired neurophysiologist.
*  So anyway, and we have family in Albuquerque, but I haven't had a good reason yet to visit
*  Santa Fe Institute. And I know it's a small Institute and that it's hard to go visit because
*  people internally need to invite people. I'm not asking you to invite me.
*  Anyone can go visit. I mean, you can go there, you can tour the Institute, you can go to lectures
*  there. It's open, totally open. In terms of going there as an official visitor, where you're
*  actually like a research visitor.
*  Not just a creep walking around.
*  Yeah.
*  Right. That someone has to invite you, right.
*  I see. But what am I going to get from going there that I can't get on complexityexplorer.org
*  these days because it's exploded. There's so much stuff there.
*  Yeah. That's a great question. You can meet the people who are there actually in real life.
*  But Complexity Explorer is definitely a great place to start if you're interested in
*  complex systems and want to learn something about it.
*  So what is complexity?
*  What is complexity?
*  It's kind of a mysterious term, right?
*  Right. And it's maybe not the best term. It's sort of a term that we landed on to describe
*  sort of phenomenon in which you have many relatively simple elements that are collectively
*  producing behavior that we like to call complex. It's a little circular.
*  When you talk about it in your talks, it's almost like it's this compilation of different
*  properties, right? So you can describe the properties of a complex system and then put
*  it all together and that's what complexity is. Is that maybe?
*  Exactly. Right. I think it started because people who were studying systems like the brain
*  where you have trillions of neurons and they're all communicating with each other and it's very
*  dynamic and out of that comes like human cognition.
*  Emerges, right.
*  Emerges, right. We don't understand it.
*  This is one property also of a complex system is emergent behavior. Is that right?
*  You could say that, yeah. And people are also studying things like the immune system,
*  which has trillions of cells constantly communicating with each other. And there were
*  a lot of analogies to the way brains operate, the immune system operates and same for insect
*  colonies and- These networks.
*  These networks and also people were studying the economy and there was a lot of biological
*  analogies to the way the economy works. And this is sort of how the Santa Fe Institute
*  got started was that there was a group of scientists who felt like there was something
*  very deep and universal about all these systems that needed to be understood in an interdisciplinary
*  way, not just in these individual disciplines. And they couldn't put their finger on exactly
*  what it was. So they called it complexity.
*  See, so the Santa Fe Institute was this really early proponent of interdisciplinary work,
*  I feel like, because that's what everyone does today. And that's how the graduate students
*  are sold on a neuroscience program. Just I'm biased because I come from neuroscience.
*  And if you're not interdisciplinary today, you don't make the cut.
*  I don't know. Being in a university, I could say that what's called interdisciplinary,
*  sure. Like it may be a neuroscience, it's cellular versus systems neuroscience. That's
*  interdisciplinary. All I'm saying is you need to use the word if you're the program. You have to
*  use the word these days. You have to use the word interdisciplinary and transformational and-
*  Collaborative, collaborative.
*  Right. Buzzwords. But at Santa Fe Institute, I think they take it very seriously and
*  it's much more interdisciplinary than any university I've ever seen. Because you really
*  do get economists talking to neuroscientists, trying to try and understand what's common
*  among the kinds of things they're looking at.
*  It just kind of emerges, if you will, out of the goal of understanding complexity,
*  because there are so many different complex systems from so many different disciplines,
*  that it only makes sense to bring them all together.
*  That's the hypothesis.
*  Yeah.
*  Right.
*  Okay. One of the properties of a complex system that you mentioned in your talks is that they
*  have limited centralized control. What does that really mean? I think I know what it means, but
*  can you just describe what that means?
*  Sure. If you think about the brain, for example, and all these trillions of neurons,
*  as far as I know, there's no small set of neurons that are in charge.
*  There's no homunculus.
*  Right. There's nothing in the brain that's kind of overlooking the whole system and saying,
*  you do this and you do this and you're in charge of this and you're in charge of this.
*  Instead, it's decentralized. Each neuron does what it does, which is a function of
*  sort of its particular biology and its connections with other cells in the brain.
*  Somehow out of that whole cacophony of decentralized entities, you get what feels like organized
*  behavior.
*  What feels like?
*  Right. Yeah.
*  Yeah. That's sort of the idea.
*  Very good. This show is about the bringing together of neuroscience and artificial
*  intelligence and sort of what they can teach each other, how they're separate,
*  how they're disparate, what's common to them. I'm wondering if you have ideas on how complexity
*  can help bridge the gap, any gap between AI and neuroscience. How does it fit into that world?
*  Okay.
*  Does that make sense?
*  Yeah. I think I have some ideas about that. One of the things that people in complex systems
*  talk about a lot is information in a very abstract sense that all these complex systems
*  are in some sense processing information.
*  Like Shannon entropy information or information in a broader sense?
*  I would say information in a broader sense.
*  And one of the research topics is really trying to pin down what that means,
*  processing information. What does that mean? How do we quantify that?
*  And Shannon information is one way, but it's not the whole story.
*  And processing information is closely related to computation.
*  And some people would say that the brain is a computer.
*  The brain is taking inputs, doing computations and producing outputs.
*  Right.
*  Complex system and complex systems, and certainly AI, that's what you do in AI.
*  And so some people in AI are trying to say, well, okay, what kinds of computations does the brain do
*  and how do we emulate that in a computer? But I think in complex systems, people are thinking
*  about like, what is computation? What are the mechanisms of computation in all of these complex
*  systems? It's not like a standard von Neumann computer. You don't have a CPU. You don't have
*  random access memory and all that stuff. You don't have logical chips that do logical operations.
*  Somehow all of this is emergent. And complex systems is really trying to characterize the
*  kinds of computations done by complex systems in this very collective way, collective computation.
*  And so Santa Fe Institute, that's a very important theme.
*  And I think that understanding that kind of general idea of collective computation and complex
*  systems is going to be relevant both to neuroscience and thinking about how the brain works and also to
*  AI thinking about how to try and emulate the kinds of things the brain does to produce intelligence.
*  So I'm a by training, I'm a monkey neurophysiologist, right? So and I've done some
*  decision making modeling with stochastic accumulators that I won't get into. And
*  frankly, I'm of limited intelligence. So I view most of what I think about in this realm through
*  the lens of like neurophysiology, right? Sticking electrodes in the brain. Right.
*  What lens do you, because you have these multifaceted expertise, what, when you're
*  thinking about a problem, do you view it through the lens of complexity or through the lens of
*  computation, machine learning? How do you approach these problems?
*  Wow, that's a hard question. I try and switch lenses when I can to try and get new perspectives.
*  And that's something that SFI has helped me in. I was going to say another way to think about
*  complex systems is in terms of dynamics. Dynamical systems is a mathematical
*  area that tries to characterize how systems change over time. You know, it's kind of the foundation
*  of calculus. And, but it's also dynamical systems theory is becoming really relevant, both in AI
*  and in neuroscience as a way to, to analyze these systems. I'm not sure that it's a causal
*  description that people could argue about that. But then people do argue about that. But, but it
*  is becoming a very important way of looking at it. Right. And so it's kind of an alternative
*  to computation. It's a different lens. So looking at it through the lens of computation and looking
*  at through the lens of dynamics kind of give you a different view. So one example, as a
*  neuroscientist, if you've looked at like the visual system or maybe any system in the brain,
*  one thing that really stands out is how much feedback connections there are. Sure. You know,
*  my neuroscience friends, I'm not a neuroscientist, but I have some friends.
*  Me too. Me too. And they tell me that in at least the visual cortex, there's 10 times as
*  many feedback connections as there are feed forward connections, which is amazing given that most of AI,
*  most of deep learning uses feed forward networks entirely. And one of the reasons for that is
*  it works for the kinds of tasks people are looking at. And also it's hard to get systems with feedback
*  to work well. It's more difficult to make them do what you want them to do. There's been a lot
*  of progress in that, but yes, that's very true. And so somehow, so the question is like, what is
*  what does that feedback gain us? And in complexity, people look at that kind of idea across a lot of
*  different systems. You know, there's a lot of idea that biological systems, including the brain,
*  the immune system, cellular metabolism, all of these systems, there's a huge amount of regulation
*  that's essential for to get these systems to work. And a lot of the feedback connections are involved
*  in regulation. That's something that AI might take some notice of, because maybe one of the
*  reasons that we're not so easy to fool with adversary examples is we have all this feedback
*  from higher layers of the brain that are kind of regulating what our lower visual system is doing.
*  That's an interesting take because a lot of people talk about the feedback connections being
*  predictive as well. So it's like a model that's been predicting and then there's a...
*  I think that's true. But regulation is a very big deal in biology.
*  Yeah, it sure is. I really hadn't thought that much about the feedback signal in a regulatory role,
*  so I'll have to look more into that. Okay, so we have a little bit more time. So thank you.
*  I really wanted to get your take and you gave a nice take on how complexity kind of fits into this
*  whole system, fits into neuroscience and AI. Okay, so I always have this last little section
*  where I kind of open it up and then ask some broader, more general questions. So do you think
*  that a general theory of the brain or intelligence might come from neuroscience or complexity theory,
*  which complexity, as I understand it, is still looking for its own theory, a general theory,
*  right? Or will artificial intelligence work, help figure out what intelligence is and how the brain works?
*  I don't think any one of those fields is going to produce a general theory.
*  Do you think a general theory will be produced? Is it producible?
*  I don't know. I don't know. Again, I'm not sure what general theory, the goal of a general theory
*  is. Is it to predict, so that I could predict everything about what you do? No, I don't think
*  you're going to get something that's going to be able to do detailed prediction,
*  but something that's going to help us understand much better how the system works and be able to
*  create an intelligent system, a non-biological intelligent system. I do think that we'll be able
*  to do that eventually. I just think it's a very, very hard thing and it's going to take a lot of
*  time. That's your outlook. Let's see, best guess, what year?
*  I'm not going to guess. I absolutely cannot guess. Everybody who guesses ends up being horribly,
*  horribly wrong. That's the fun thing about guessing, if you know that going in and admit,
*  I know I'm wrong, but. Here's a related question. Let me say this. There's a quote I have in my book,
*  which is from back in the 60s or something. Someone said that artificial intelligence is
*  at least 100 Nobel prizes away. That's the only right person in the history of this, right?
*  There's no Nobel prize in artificial intelligence. But in terms of understanding biology,
*  the understanding that we're going to have to have of biology or the kinds of breakthroughs
*  that we need to, might not be a Nobel prize literally, but that kind of breakthrough.
*  I kind of agree with that. If you had to be cryogenically frozen for a period of time and
*  then you get to wake up, how many years would you? Oh boy, you're taking a big risk because
*  you're asking is civilization going to last as long as it's going to take?
*  Right. Well, that gives me some breakthroughs. That's true. Well, no, but I just mean,
*  when would you want to wake up and see where we are? Not necessarily, when would you wake up
*  and think that what we had just spoke about had happened? I'm just saying you personally,
*  if you had to be frozen and then thawed, when would you want to be thawed?
*  Well, I'd be a little bit afraid if I said like 100 years from now that I'd be thawed and we'd
*  be in some horrible dystopian climate disaster. Yes, this tells me a lot about you. Yes, yes,
*  go on. Yeah. I don't want to be frozen at all. You could say one day. That's the shortest period.
*  So you'd go one day? Yeah, I'm pretty happy being in the present.
*  Okay, very good. You and I are different people. What do you think? What's one trait of our
*  intelligence that will really be difficult to build into general AI? We've talked about
*  multiple facets of this, I suppose. Yeah, I think this whole idea of common sense,
*  however you want to define it, is going to be really difficult. That's going to be the big,
*  okay. Yeah, and DARPA right now has a program called Machine Common Sense. They're putting
*  a lot of money into funding. Paul Allen, the co-founder of Microsoft, before he died,
*  he gave a lot of money, I think like 120 million or more to the Allen Institute for AI that he
*  founded specifically to study common sense and how to get computers to have common sense.
*  There's going to be more and more attention given to this, but no one really knows how to do it.
*  Or how to really even to approach it at this point. Yeah, or even how to define the term.
*  Will complexity theory lead to an understanding of consciousness?
*  Moving on. Oh man, I don't know. Where's your brandy? Where's your brandy in your desk?
*  That's right. Yeah, perhaps complexity theory will sort of, as Dan says, explain away consciousness.
*  Oh, are you an explain away consciousness kind of person?
*  I am, I think. Yeah. I'm not so convinced that. I think it's kind of a catch-all term that as we
*  get more, as we understand more and more how the brain works, that we're going to say, okay,
*  that was kind of a red herring. Marvin Minsky calls it a suitcase term. That's like his concept,
*  which I'm coming to agree with it. I read Dennett a long time ago and it's a type that you have to
*  read over and over to revisit, to really let it sink in. But the more people I talk to who
*  have to share this vision, it gives me a little more confidence in my own that consciousness
*  will be explained away, isn't a thing per se. So, okay. What's something that someone might find
*  hard to fathom, like that is a little bit out there, something that you believe that's a little
*  bit out there maybe, that we might discover about ourselves or intelligence as a result of research
*  in AI or complexity or neuroscience? That we would discover about ourselves.
*  Oh, wow. Or our intelligence or, you know. Yeah, that we don't have free will. Oh, okay. So,
*  you think that's going to be sort of a, so there'll be some sort of proof because there's a lot of
*  anti-free willers right now too. Yeah. Gosh, we do share some views then. Oh, okay. Yeah.
*  All right. Last question, Melanie. What is one thing that you have failed at?
*  You've had a lot of success. What's one thing that you failed at and how did you come back from it?
*  Oh, boy. One thing. You can only choose one thing here. Oh, wow. Yeah. So, all through high school
*  and through much of college, my goal was to be a physicist and I wanted to be a cosmologist. Oh,
*  yeah. Yeah. That was my dream and I really found physics too hard. Which, which, the Newtonian or
*  the electrical or all of it? I think all of it. Yeah. I just was not very good at it. I struggled
*  and struggled and I just couldn't do it. So, I gave up my dream of majoring in physics and
*  going to graduate school in physics and that was very difficult, I have to say.
*  Kind of beat my head against that wall for a long time and ended up in computer science, which is
*  ironic because it turns out that a lot of the physicists I know, people who studied cosmology,
*  in fact, ended up in computer science as well or neuroscience or social science.
*  Is that because employment for physicists wasn't high or? I think a little bit of that and also
*  that they got a little fed up with the whole, how abstracted, theoretical and untestable it was all
*  getting. Yeah. Like with string theory and all that stuff. So, is that how you finally let it go
*  and thought it's okay? No, I let it go way before that. It wasn't making me happy. No, I mean, is
*  that when you let it go, stopped beating yourself up over it? Oh, yeah, maybe. And then I married a
*  physicist and kind of got to know one and found out that I was actually happy where I was. And
*  there's really, they're not great people either, right? They can be great people. I have many
*  physicists who are my closest friends and my husband's a physicist and I think they're great,
*  but I let it go. Well, okay. Thank you for sharing that and thanks for sharing your time with me,
*  Melanie. So people can find you on Twitter at Mel Mitchell one. And again, I will link to your
*  website and complexity explorer.org. And is there any other way that you'd like people to find out
*  more about you? I think that that would be the best. And of course, I'll link to your classic
*  now classic book, complexity, a guided tour. So yeah, and I'll be I'll be putting information
*  about my new book on my website when it's available. And people can follow you on Twitter
*  and I'm sure that you will tweet about that as well. Absolutely. Well, congratulations on the
*  book. And again, thanks for talking with me and continued success to you. Thank you so much. This
*  has been really fun. Brain inspired is a production of me.
*  You can support the show through Patreon for a trifling two or $4 per month. Go to patreon.com
*  slash brain inspired, or go to the website brain inspired.co and find the red Patreon button there.
*  Your contribution will help keep this show going without any annoying advertisements like you hear
*  on other shows. To get in touch with me email paul at brain inspired.co. The music you hear is by
*  New Year. Find them at the new year.net. Thank you for your support. See you next time.
*  Bye.

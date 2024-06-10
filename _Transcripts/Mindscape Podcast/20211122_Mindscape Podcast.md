---
Date Generated: June 08, 2024
Transcription Model: whisper medium 20231117
Length: 4894s
Video Keywords: []
Video Views: 12160
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2021/11/22/174-tai-danae-bradley-on-algebra-topology-language-and-entropy/

Mathematics is often thought of as the pinnacle of crisp precision: the square of the hypotenuse of a right triangle isn’t “roughly” the sum of the squares of the other two sides, it’s exactly that. But we live in a world of messy imprecision, and increasingly we need sophisticated techniques to quantify and deal with approximate statistical relations rather than perfect ones. Modern mathematicians have noticed, and are taking up the challenge. Tai-Danae Bradley is a mathematician who employs very high-level ideas — category theory, topology, quantum probability theory — to analyze real-world phenomena like the structure of natural-language speech. We explore a number of cool ideas and what kinds of places they are leading us to.

Tai-Danae Bradley received her Ph.D. in mathematics from the CUNY Graduate Center. She is currently a research mathematician at Alphabet, visiting research professor of mathematics at The Master’s University, and executive director of the Math3ma Institute. She hosts an explanatory mathematics blog, Math3ma. She is the co-author of the graduate-level textbook Topology: A Categorical Approach.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel: https://www.youtube.com/c/seancarroll

#podcast #ideas #science #philosophy #culture
---

# Mindscape 174 | Tai-Danae Bradley on Algebra, Topology, Language, and Entropy
**Mindscape Podcast:** [November 22, 2021](https://www.youtube.com/watch?v=OynLbSzLS9s)
*  Hello everyone and welcome to the Mindscape Podcast. I'm your host Sean Carroll.
*  A lot of people, I think, when they think about math, when they hear the words math and doing math,
*  they think of what a mathematician would call calculating, right? Performing some calculation,
*  whether it's something simple like calculating the tip on a restaurant bill, something maybe more complicated
*  like calculating the orbits of planets and stars and galaxies and so forth.
*  But that's actually very, very little of what professional mathematicians do.
*  We use math in that way, but professional mathematicians are engineers of concepts.
*  They invent new kinds of concepts, they put them together to prove theorems,
*  and they draw connections between concepts that you might not have known about before.
*  So today's guest, Ty Dene Bradley, works at a very interesting intersection of algebra and information.
*  Algebra being, in the mathematician's sense, a kind of study of structures in mathematical objects.
*  So ways you can multiply things together, ways you can combine things,
*  and also ways you can take things apart that relate to each other and then build them back into the original whole.
*  And then information in the sense of what relates to what, what do you know about one thing by learning about another thing?
*  So here's an example that you might not think of as originally mathematics,
*  but that is absolutely closely related to this stew of algebra and information, language.
*  The language you're hearing right now, the set of words that you're listening to, has a structure in it, right?
*  Because when certain words pop up, other words are more likely to pop up right next to them.
*  And of course, you can take a completely mindless approach to understanding this.
*  You can just dump it all in a computer, right?
*  Dump a huge text in a computer and ask, what are the statistics of this?
*  What words appear next to what other words?
*  But you can also think like a mathematician.
*  You can say, well, why is it like that?
*  What are the structures underlying this kind of thing?
*  And it's kind of an interesting mathematical move to introduce the idea of statistics and probability into this kind of study,
*  because certain words in language appear next to each other more frequently, but it's not absolute, right?
*  It's sort of a relative connection between these things.
*  And that's not natural always for mathematicians to study.
*  So, Tidenay really works at this fascinating confluence of algebra, information, statistics.
*  And that has led her to think about one of my favorite topics, which is entropy.
*  So we talk in this podcast about, well, let me tell you ahead of time.
*  It's going to sound simpler than it is.
*  She really is really very good at explaining things in a way that kind of don't scare you in terms of mathematical formalism and jargon and all that stuff.
*  But you can read the papers behind it.
*  They're all real math papers that involve all the formalism and jargon that you want.
*  But we're going to be talking about category and topology and probability theory and a little bit of emergence and entropy and other things that I'm very interested in.
*  For those of you who like this kind of thing, I'll also encourage you to check out.
*  Tidenay has a website called Mathema, except instead of the E in EMA, it's a three.
*  So that's M-A-T-H-3-M-A dot com, where she does a series of very nice expository blog posts, videos, things like that.
*  Really a wonderful ability to make these very high powered mathematical concepts seem a little bit less intimidating than they should be.
*  So with that, let's go.
*  Hi, Tidenay Bradley. Welcome to the Mindscape Podcast.
*  Thank you, Sean, for having me. It's great to be here.
*  So we've agreed this is going to be a challenge.
*  You know, we're bringing you on here because you have a certain genius for explaining these difficult things.
*  But but that's OK.
*  And it's actually very good for me because I do a lot of work in trying to explain difficult concept in physics to people.
*  And it's always good to be humbled a little bit when I'm reading your paper.
*  I'm like, this is what it's like for other people.
*  They read my papers and I don't know what any of the words mean.
*  So let's just start with some some sort of setting the stage kind of stuff.
*  Like a big part of your work involves algebra.
*  Algebra and statistics was was right there in the title of your thesis.
*  So what do you mean when you use the word algebra?
*  It's probably not like solving quadratic equations.
*  That's right. That's right.
*  So when I say the word algebra, I mean it in a less technical, potentially scary sense that folks might think.
*  OK, so in the title of my thesis at the interface of algebra and statistics,
*  I really just meant algebra and the basic sense of sticking things together.
*  So, you know, you mentioned quadratic equation quadratic, you know, that makes us think of x squared or something.
*  I have two numbers and I, you know, one number, I multiply it by itself.
*  I have two things and I can multiply them and get a third thing, you know, that's of the same flavor or the same type as the two that I started with.
*  Maybe there's maybe they're numbers.
*  But, you know, as one progresses in math, you learn that you can multiply things that aren't numbers and you can make sense of that.
*  That's where it gets hairy. Yes, I know.
*  Yeah. So I just meant when I say algebra there, I just mean in the sense that I have, you know,
*  things and I want to have some notion of multiplication or, you know, concatenation or some type of way that I can combine these things to get something larger.
*  So very basic, not not really technical quite yet.
*  That's what I mean. Great.
*  So we're composing things together, but just to put a little meat on those bones here, what are some of these things?
*  So if I multiply two numbers together, that's an algebraic kind of thing or two variables.
*  What are other kinds of things that I can combine together?
*  Yeah. So in the context of my thesis, the things that I'm really having in the back of my mind are words or expressions in a language, in a natural language, actually.
*  Okay.
*  So think for a second about something like, I guess the example I often give is red is a word.
*  Yep. There you go.
*  And fire truck is a word.
*  And now I want to combine them so that I get a new expression, you know, in the English language.
*  So I'm going to define a multiplication, but let's call it stick those things together.
*  Red, fire truck, stick them together.
*  You get red fire truck.
*  Right. If I want to be more precise, I just really mean concatenation.
*  Okay.
*  So that's one example that maybe you might not think of.
*  It's not doesn't feel like math.
*  You know, we learned about red fire trucks when we're, I don't know, two years old looking through picture books.
*  But I'm sort of secretly or not so secretly secretly suggesting that there's algebraic structure even in something like language.
*  Okay.
*  But this is good because when I take red and fire truck and concatenate them, I get a phrase rather than a single word.
*  So part of the algebraic magic is that when we do this generalization of multiplying, we need not get the same kind of thing that we started with.
*  That's right.
*  That's right.
*  So you may that's exactly right.
*  So then you kind of ask, how do you keep track of that?
*  You know, you sort of feel that not only do you have these things called words, but then there's other things called expressions, which are like multiple words.
*  And maybe you want to keep keep track of those.
*  You know, maybe you have all English expressions of length one.
*  That's what we call words, you know, dog, cat, breakfast.
*  Oh, that's a compound word.
*  Okay.
*  Anyway, but then that, you know, then you have, you have like the set of all English words of length to, you know, red fire truck, hot dog, tasty breakfast, blah, blah, blah.
*  And then you can look at those of length three.
*  And then maybe you might want to say, you know, how, how, how does the algebraic structure pair well with the fact that I have different lengths involved?
*  But there are actually tools in algebra that that deal with that.
*  But maybe I don't want to throw in technical words so quickly at the beginning, but I'll just say, yeah, this this already gives gives a mathematician, you know, you're getting excited already.
*  Yes, there's lots of things that we can think about in math has lots of answers.
*  And just to be clear, this example of concatenating words, this is not just a metaphor.
*  This you're saying this really is something we can think of as an algebra.
*  Yes, that's right.
*  Go ahead.
*  Yeah, I'll say in case there are mathematicians listening, you know, and we say an algebra, there is a very, very specific, you know, strict definition in the sense of abstract algebra.
*  One can make sense of that.
*  True.
*  But to be more precise, I might mean something like, am I allowed to use technical technical words?
*  I might say something like a monoid.
*  Really?
*  Monoid.
*  That's just a like a gentler, you know, friendlier atmosphere in which you can talk about multiplying things together.
*  Maybe an algebra and the technical sense and math kind of comes with some extra stuff.
*  But the basic mathematical framework where you have a bunch of things, you know, like a set or a bag of marbles or a bag of words, and you want to have a notion of multiplying them together in some sense, something like that, we call that a monoid.
*  So that's kind of what I mean.
*  Yeah, I think that going forward, we're allowed to talk about the technical terms because we want to be able to give the listeners some takeaways, like if they ever see this somewhere else.
*  Great.
*  We were talking about infinity groupoids with Emily Real before, so, you know, we shouldn't feel bad about that.
*  So I can say monoid.
*  No problem.
*  I mean, it is in the first few minutes, but okay, it's all going to be downhill from here.
*  So does this way of thinking about language let us take into account the fact that, for example, certain concatenations of words make sentences and certain other ones don't?
*  Can we put the rules of grammar into our monoid?
*  Right, right.
*  So you'd like something else.
*  That's exactly right.
*  There's this observation that algebraic structure is there, but it's not really everything.
*  It's not really all that there is to language because you make this observation.
*  Not everything goes together.
*  You know, you can't multiply everything and get something that's legal, you know, or something that makes sense.
*  So now some folks might think, well, maybe the additional structure you need is some type of grammar or syntax or something.
*  But in my thesis, there's a perspective that's taken that is actually there are statistics in language because red fire truck is something that maybe appears quite frequently in the English language and it might appear more frequently than the other example I like to give is red idea.
*  Did I wake up this morning and have a red idea?
*  Like, what does that even mean?
*  That's not a thing that people say.
*  So there's actually an observation you can make or not an observation, but maybe a hypothesis or something you might want to stand firm on.
*  And that is that statistics actually can maybe serve as a proxy for grammar.
*  I see.
*  So that is the extra bit of mathematical structure that's missing from language.
*  So there's algebra.
*  But then what else?
*  Like, how do you know what really goes together and what's valid in your in your language?
*  Yeah, you need to know that, you know, in English, at least adjectives precede nouns, you know, red fire truck, but maybe in a different language, it's reversed or something like that.
*  But how do you know?
*  Well, you can kind of look at the the landscape.
*  Look at what's out there.
*  What has every human said, you know, from the dawn of time in English?
*  And you can just, you know, count the number of times that red fire truck has appeared.
*  And you can see that that that number is bigger than the number of times red ideas appeared.
*  And maybe the totality of that algebraic structure, what goes with what together with the statistics that you observe about it, tell you like what's the deal with your language?
*  What are valid expressions in your language and what's not?
*  And one way to see that you can look at the statistics or what has been said.
*  So it's it is already an interesting kind of shift of perspective to have mathematicians think because people on the street would say, well, you know, grammar is a set of rules for grammar.
*  These words work together and these words don't.
*  And what I'm getting from what you're saying is, let's imagine all possible sequences of words and assign to them some number about the frequency with which they appear.
*  And implicitly, all the rules of grammar are reflected in those numbers.
*  That's right. That's right.
*  And this might not be the computationally most simple way to express the language, but maybe the same information is there.
*  Yeah. So so exactly.
*  And you might ask why. Like number one, yes, this sounds difficult because what does it mean to have, you know, probabilities attached to all expressions ever?
*  You know, what about the expressions that haven't been spoken yet, for example?
*  But actually, this idea comes from something that actually learns grammatically correct sentences very well, just given this input algebra and statistics.
*  And that are the these large language models that you see that are doing really well in the world of artificial intelligence today.
*  So in the world of machine learning, you can you can give, you know, show your computer a bunch of examples of correct English text, you know, let it read all of Reddit or something.
*  And it just sees what goes with what with what frequencies.
*  And you don't need to give it any type of grammatical input.
*  You don't need to say, OK, dogs are nouns, you know, fluffy is an adjective that you just let it see what goes with what.
*  And you can, you know, it learns some probability distribution on text.
*  And when you sample from that, you can see it generates coherent English text.
*  You know, you can read a blog post online, you know, that discusses, you know, one day robots are going to overtake the world.
*  But that's OK, because robots are really friendly.
*  And then at the end, you realize a robot wrote it, you know, or like one of these large language models wrote it.
*  But it's sort of deceiving because it sounds exactly like something a human wrote.
*  It's coherent. You know, the syntax is correct.
*  It's using, you know, the semantics and all the right way.
*  But it had no grammatical input.
*  All it had was the algebraic and statistical information.
*  So then the question, you know, from the math viewpoint is, wow, somewhere in this, you know, neural network,
*  structure is being learned. What is that mathematical structure?
*  If I just have algebra and statistics, what's happening so that I can get, you know,
*  a correct reproduction of what goes with what in my language?
*  Something is in there. And the large language models of today are like the experiment that illustrates that.
*  And so as a mathematician, you can look back and say, wow, what's really going on under the hood?
*  Like, what's that beautiful math that is learning that we're seeing evidence of?
*  Right. And so one of the one of those things is I guess, I guess the thing for me to say is
*  let's continue on our exploration of the word algebra.
*  So I get the fact that you're combining things that make sense in the world of just multiplying numbers together.
*  There's sort of an irreversibility, right? If I say two times five is ten.
*  That's a terrible example. If I say two times six is twelve, I have twelve, but I don't know how I got there.
*  Right. I mean, I've lost where where they are.
*  Is that does does the algebraic point of view assume that we can remember what we combined to get the final answer?
*  So so if I could try to rephrase this question, if I have some larger expression,
*  maybe or like there's a meaning attached to some larger expression, maybe we'd like to know does the algebraic framework we're in
*  allow us to kind of zoom in on whatever individual pieces went in to make that composite whole?
*  If I could rephrase the question to understand it, is that exactly?
*  That's good. Yes. Yes.
*  So I love this question because the answer is yes.
*  It's not random. I did actually look at your thesis.
*  But this this the answer to this actually is really at the heart at the heart of the thesis.
*  So but it might take a little bit of time to explain.
*  So I hope the listeners are ready to put.
*  OK, so let's see.
*  One way I could say this is to explain it.
*  I have to I have to inch out of the world of algebra just a little bit.
*  So so the title of the thesis is at the interface of algebra and statistics.
*  So that kind of gives us the feeling that we're really mingling these two worlds.
*  So if I want to talk about something, you know, I have a composite whole.
*  But how do I get information about the little bits that go into making that larger thing?
*  There's a way to do this.
*  And let me for a second talk about one way to do this that I think people will be familiar with
*  from the world of probability.
*  And that feels maybe like totally left field.
*  But then then we'll bring it back and see how that relates to algebra.
*  Sounds good. So it's just one word.
*  If I say this word, I think lots of people will be familiar with it.
*  Marginal probability.
*  Let's assume that we're not necessarily we've heard that word before, but we can't remember what it means.
*  OK, OK. So let's say that.
*  I don't know. You we were doing two things.
*  I don't know what they are like we're rolling, you know, a die or pulling from a deck of cards,
*  something like that. And maybe, you know, you have a die in your left hand and you have a pack of cards in your right
*  and you just kind of do both. And you can ask, what's the probability that I roll,
*  you know, a three and I pick, you know, a red four hearts or something like that?
*  OK, so you kind of have this joint probability distribution.
*  That's what it's called. You have two things, a die and pack of cards.
*  You can roll, you can draw, and you have a probability for doing both at the same time.
*  But you might want to know, well, forget the cards.
*  You know, I forgot how to play cards or I lost my deck.
*  Whatever. I'm only interested in sort of the probabilities I get for rolling my die.
*  That would be called marginal probability.
*  So if you start with knowledge of doing kind of both things jointly,
*  how can you take that knowledge to just focus in on one of those two events,
*  you know, rolling a certain number on your die?
*  So there's a formula for that. So if you know the probability for, you know,
*  rolling each number and pulling each card kind of together,
*  you can take those numbers and kind of add them in some way.
*  You can get what's called marginal probabilities,
*  which are just the probabilities for rolling a certain number on your die.
*  So you just add up all the individual probabilities in that set,
*  and then you get the marginal probability.
*  Exactly, exactly. And that's the key.
*  You start with something big, like two events, a die and a card,
*  but you just kind of want to zoom in on one of those, like the die.
*  So what you do, just like you said, you kind of add over all of the possible events
*  that you could have had with the cards, all the cards you could have drawn.
*  So you kind of ignore that. That operation of adding is kind of like forgetting.
*  You know, you add all of them up and now you have discarded that information.
*  So in other words, if I roll, you know, a four with probability,
*  I don't know, 23%, let's just say, that number, 23%,
*  doesn't tell me anything about what cards I could have drawn
*  when I rolled the number, whatever I just said, four. Is that what I said?
*  Okay. So that's important.
*  And this is this notion of what we call marginal probability.
*  It's like a basic thing, I guess you learn it.
*  I don't know. At some point in your intro to probability courses,
*  so there's a formula. And that formula again says,
*  if you start with sort of this joint system, you can get knowledge about one of those systems,
*  but kind of, you know, at the cost of forgetting all information,
*  losing all access to the second one.
*  All right. Now it turns out that if you, well, let me say it this way.
*  It turns out that there's another way to compute marginal probability
*  such that you actually remember or retain information about the deck of cards
*  or about that other system that you say, I don't really care about that.
*  But rather than tossing it in the trash can,
*  there's another way to compute marginal probability that actually gives you easy access to it.
*  You know, maybe you just toss it on your desk instead of throwing it in the bin or something.
*  Okay.
*  Okay. Now this, it's essentially a passage from, I'll say sets.
*  You know, I have a set of options for the die.
*  One, two, three, four, five, six.
*  I have a set of options for the cards.
*  There's 52 elements in that set.
*  This is like classical probability theory.
*  Normal probability theory works with sets.
*  But this other way that I'm describing,
*  which I might call marginal probability with memory,
*  you sort of start with your sets,
*  but you actually move into the world of linear algebra.
*  So rather than sets, you work with vector spaces.
*  And rather than probability distributions,
*  you work with the linear algebraic version of a probability distribution.
*  Now at this point, I'm kind of making things more difficult
*  because it's like what's the linear algebraic version of a probability distribution?
*  Is that a thing?
*  So what I really want to say, and I'm hesitant to because I'm speaking to a physicist,
*  but what I really want to say is the quantum version of a probability distribution.
*  And you know what that is.
*  I do know what that is, but go ahead.
*  But yeah, I am afraid to use the word quantum in case.
*  I don't want people to run away in fear too quickly.
*  So what that really is, just to keep it simple,
*  what's the linear algebraic version of a probability distribution?
*  It's just a matrix.
*  Let's just think of it as a matrix of numbers.
*  And you might want to ask that matrix to satisfy properties
*  that feel like a probability distribution.
*  For example, you might say, oh, I want the trace of that matrix,
*  the sum of all entries on the diagonal to add up to one.
*  Oh, it kind of feels like a probability distribution.
*  Probabilities add up to one.
*  You kind of make restrictions on such a matrix.
*  So there's a way to do this.
*  When you do this kind of in the correct way,
*  there might be more than one way to think of a probability distribution as a matrix,
*  or what I was calling the quantum version of one.
*  Our technical word is a density operator, folks are wondering.
*  So there might be several ways to realize a probability distribution
*  as one of these density operators.
*  But if you do it in kind of what I'm thinking as the correct way,
*  or a way that is very advantageous for this discussion,
*  then because now we're in the analogous world of linear algebra,
*  you can do something that is completely analogous to marginalizing.
*  So you can actually start with a matrix that kind of gives you information
*  about your joint events, rolling a die and drawing a card.
*  That information is stored as a matrix.
*  Now to marginalize that, previously we said,
*  yeah, kind of sum over all probabilities
*  where the cards could be whatever they wanted to be.
*  But now I have a matrix.
*  So what's the analogous thing of that for matrices?
*  So that has a name.
*  That's called the partial trace, if folks are wondering.
*  So you can compute this and you get another matrix.
*  It's called a reduced density matrix,
*  but it's very much just like the linear algebraic version
*  of a marginal probability distribution.
*  And what's interesting there is that if you were to look at the diagonal
*  of this reduced density, this newer version of a marginal distribution,
*  you would actually find on the diagonal precisely the original marginal
*  probability distribution, say, of your rolling your die.
*  Okay, that's on the diagonal of this matrix.
*  But what you'll also find if you do this passage in kind of an advantageous way
*  is that there are, generally speaking,
*  non-zero off diagonal entries on that reduced density.
*  And those non-zero numbers tell you information about the deck of cards
*  that was there.
*  It might say something like, hey, every time you rolled a 1 and a 3,
*  mysteriously, you also always drew a Jack or something like that.
*  And that's what that off diagonal, the first and third off diagonal
*  of your matrix tells you.
*  Sort of tells you how many cards were in common given these two numbers
*  that you would roll on your die.
*  So that's interesting because that's the information you don't have access to
*  when you marginalize in the usual way.
*  So let me see if I got it.
*  So, I mean, we certainly don't mind the word quantum being thrown around here.
*  It's not the first podcast to do that.
*  Just to be clear, we're sort of using mathematical tricks from quantum mechanics.
*  We're not imagining that our deck of cards or our die are truly quantum in any way.
*  They're pretty darn classical.
*  We're just trying to use some tricks.
*  And so the trick is that in conventional probability,
*  we would imagine all the events that could happen
*  and we would assign a number to them, the probability.
*  And so we'd imagine it's just a list of numbers.
*  And now you're saying, let's promote that from the start to a matrix, right?
*  Instead of N numbers, an N by N array of numbers.
*  And so there's more room for interesting things to go on
*  because you have both the diagonal part of the matrix,
*  which is your old-fashioned set of probabilities,
*  and more info is lurking there on the off diagonal.
*  And keeping this as your storehouse for probability information
*  lets you both compute the marginal probability,
*  but then also keep some info about what was going on in the thing you are now ignoring.
*  Exactly. That's exactly right.
*  And is it all the info or just some of it?
*  Yeah. So great question.
*  It turns out to be all of the info in a way that can be made very precise.
*  This kind of gets a little bit technical though,
*  and I have to think way back into page 87 or something.
*  But there's a way that you can actually show that the marginals,
*  you know, these things on the diagonal together, both of them, by the way,
*  you know, you can marginalize out the cards or you can marginalize out the die.
*  Right.
*  Okay, so you kind of have to have both of those together with the off diagonals.
*  It's sufficient to recover the joint.
*  That happens to be true.
*  That makes a lot more sense to me because I thought if you just marginalize one,
*  you're just losing information,
*  but you're saying I'm keeping the matrix associated with marginalizing either one.
*  Yeah, that's right. That makes sense.
*  Okay. But let's back up and be a little bit philosophical here.
*  I think that we've done an admirable job of making sense so far.
*  So let's stop doing that.
*  You know, the words that you use when you describe some of these things,
*  you know, like taking pieces and then composing them
*  and then asking how to reconstruct the whole from the parts.
*  I mean, these have counterparts in philosophy as well as in physics
*  in realms of things like myriology.
*  Do you know, have you ever heard the word myriology before?
*  That's what philosophers call the relationship between holes and parts.
*  So how you break up a hole into parts.
*  And I'm very interested in it because of questions of emergence of,
*  you know, different higher level descriptions from lower level descriptions.
*  So is it and here's an answer.
*  Here's the question I really don't know the answer to, not a leading question.
*  Is there some sense in which these techniques you're talking about
*  are helping us decide either the best way to take a bunch of little things
*  and combine them into a big thing
*  or given a big thing the best way to divide it into a set of little things?
*  That is a great question.
*  Let's see. What can I say anything helpful about this?
*  I think it would be interesting depending on how far or how deep one can explore this mathematics.
*  I think that there'd be a very good chance that the math will have something very interesting
*  to offer to the philosophers with those kinds of questions and vice versa.
*  I think this is exactly the real estate for that.
*  But I don't have, you know, I don't have good quotes or something that come to mind
*  where I can say, oh yeah, you know, in philosophy, there's this idea by this person.
*  And in fact, we have a theorem that says exactly what he said, but in formal terms, that would be great.
*  But I do get the feeling, yes, that this kind of direction, you know,
*  taking sort of a non-traditional perspective on algebra and probability in this way
*  maybe can lead you down avenues that haven't yet been explored
*  so that you can see sort of these more philosophical questions from a different viewpoint
*  that maybe is more illuminating.
*  Yeah, no, I think that's exactly right.
*  And you know, like I said, I didn't know the answer to the question when I asked you,
*  so it was not a leading question.
*  But there's two examples in my mind that I can't help but just say out loud to give you and the audience food for thought.
*  One is I just did a podcast with Anil Seth, who is a neuroscientist,
*  but he also writes papers about emergence.
*  And so he's literally dealing with he and his co-author Lionel Barnett,
*  time series of random variables.
*  And they want to know, you know, when, how do you coarse grain?
*  How do you like combine different variables into a smaller number of variables
*  so that you still get a predictive theory, right?
*  Like what is the information you can ignore and still be Markovian in the sense
*  that the state now predicts the state next?
*  So that's one. I mean, this is an open problem.
*  It's a very, very simple to state.
*  And, you know, it's just like, how do you divide stuff up?
*  And this is very interesting, for example, to people who do origin of life research.
*  You know, what made an individual what made a cell back then?
*  How did you divide it up?
*  And the other example is I just wrote a paper with my student, my former student,
*  Ashmeet Singh called Quantum Meriology.
*  So these are words, you know, and a word is new.
*  How do you take a quantum system and divide it up into the system you care about
*  and its environment?
*  So how do you take Hilbert space, this big vector space,
*  and factorize it into tensor product factors
*  so that one of them acts like a classical system
*  and the other one acts like the environment?
*  I have nothing wise to say other than everything you've been talking about sounds relevant
*  and I should try to understand it better than I do.
*  Yes, I have to listen to that podcast and read your paper now.
*  Sounds great.
*  I've given you homework. I like to do that.
*  But okay, so enough with the open ended questions.
*  Let's move back to what you do know something about.
*  You bring up this thing called the Yoneda Lemma.
*  Am I pronouncing it correctly?
*  Yes, exactly.
*  And it's very funny because you say like this is on the one hand,
*  it sounds completely trivial.
*  On the other hand, it's the most important thing in the world.
*  And it deals very much with this question we've been talking about
*  about objects and subgroups of objects.
*  So can you explain to the person on the street what the Yoneda Lemma actually says?
*  Yes, yes.
*  So the Yoneda Lemma is a very well-known theorem.
*  Okay, it's called a lemma, but really it's a theorem.
*  In category theory, which is a modern branch of math,
*  that's quite abstract.
*  So maybe we'll leave it there.
*  But if we want to talk more about that, I'd have you to say more.
*  Do we want to say what category theory is first?
*  That's okay. I was going to ask you that at some point.
*  Sure, sure.
*  So category theory, there are I think many ways that one might,
*  you know, say what it is or analogies to try to explain it.
*  I like to think of category theory as a branch of math
*  that kind of provides a template for other branches of math.
*  So quite often what you'll find in mathematics is that ideas
*  or constructions are kind of repeated over in different fields or different branches.
*  So you might, you know, build something out of Legos, you know, in your world.
*  Maybe that's the world of topology or something.
*  And you have your little topological building blocks and you construct a space.
*  I don't know. I called it Lego building blocks, but whatever.
*  You construct something.
*  And then you look at your neighbor, you know, 16 blocks down in the neighborhood of group theory.
*  And lo and behold, they're building something that looks just like yours, you know.
*  But they call it one thing because they live in that cul-de-sac
*  and they have accents over there and they have a culture and blah, blah, blah.
*  But you call it something else because you live in your cul-de-sac
*  and you call it whatever you call it and you use your accents, blah, blah, blah.
*  But if you were to strip away all of those sort of details, you know,
*  you really find that the two folks are doing the same thing.
*  And category theory is kind of a common language that mathematicians can use to say,
*  oh, here's a thing.
*  When you specialize into the world of group theory, they usually call it such and such.
*  When you specialize it into the world of topology, they give it this name,
*  but actually both folks are really doing the same thing.
*  So it's kind of like a template where you kind of, I guess maybe template,
*  another thing I like to use is another analogy are mad libs, you know,
*  these stories where you have a basic narrative, but some of the words are missing.
*  Like, my best blank, insert a noun here, went to the, insert another noun,
*  you know, on an adjective day.
*  You know, my friend went to the grocery store on a lovely day or whatever.
*  But if you substitute different words, you get a different story,
*  but the overall narrative is the same.
*  Okay, that's very nice.
*  Yeah.
*  Yeah, so I like to think of category theory is like that kind of,
*  it's like the mad libs for mathematics.
*  You kind of have this similar narrative in many mathematical fields,
*  but depending on the words that you choose to fill in to that narrative,
*  maybe you get a different story, but the overall feel is the same.
*  So just to be, I mean, maybe a little bit more concrete.
*  I think what you mean is that there are things like multiplying
*  or taking the inverse of that appear in very, very different mathematical contexts
*  and category theory gives you a common language to talk about them all.
*  That's right.
*  Or, you know, I think maybe a more concrete example for folks,
*  because I was very vague, but you know, when are two things the same?
*  You know, if I have two sets, you know, two bags of marbles, are they the same?
*  And like, what does that even mean?
*  What considerations should I have when I'm talking about sets?
*  What's interesting about a set?
*  Nothing really.
*  It's so boring.
*  There's nothing going on.
*  It's just like dots, blah, blah, blah.
*  What can you say?
*  Nothing.
*  All you can do is count how many things are in my set.
*  So if two things are the same, well, then how do I know if two things are the same?
*  Well, essentially, they have the same number of elements in them.
*  You know, if I have two bags of marbles and they both have 53 marbles,
*  for all intents and purposes, maybe they're the same.
*  But what if your set has extra structure?
*  You know, we've been talking about multiplying things.
*  So what if I can quote unquote multiply elements in my set?
*  You know, what if my set is the set of real numbers?
*  I can certainly multiply them.
*  So that's additional structure that's there.
*  So maybe, you know, you mentioned inverses.
*  So maybe what I really have is a group, actually.
*  Maybe my set was actually a group all along.
*  But what does it mean for two groups to be the same?
*  You know, I have a way to multiply elements.
*  You know, each element has an inverse.
*  Maybe I have a multiplicative identity, you know, like a half times two is one.
*  So maybe I have a thing that behaves like a one.
*  So what should sameness mean there?
*  Well, category theory helps you make sense of that.
*  And you can kind of see when you have the answer to that,
*  what is the proper notion of sameness?
*  It turns out that you subsume the notion of sameness in all of these fields.
*  Maybe in group theory, it's called a group isomorphism.
*  Maybe in the world of topology, it's called a homeomorphism, you know,
*  in differential geometry, you know, that has a name.
*  In each of these fields, you have different names.
*  But in the eyes of category theory, this notion of sameness,
*  you just call it an isomorphism.
*  Got it.
*  So maybe when you're an undergrad, you're like,
*  oh, I have all of these vocab words to memorize, blah, blah, blah.
*  This is so confusing.
*  But then category theory is like, nah, it's just one concept.
*  More category theory in high school math.
*  That's what we need.
*  OK.
*  And so then this is good.
*  Now we live in category theory and the Unita lemma.
*  OK.
*  So the Unita lemma, let me just say what it means in English, not the technical sense.
*  And what it means in English, I think, can be very relatable
*  and something that we can all maybe agree on.
*  The Unita lemma says, if you want to understand an object,
*  a mathematical object, like a group or a space or a set,
*  the Unita lemma says that all of the information about that object
*  is contained in the totality of relationships
*  that object has with all other objects in its environment.
*  Or, you know, a little more technical mathematical object
*  is completely determined up to isomorphism by all of its relationships.
*  So let me say this a different way.
*  You can learn a lot about a person by seeing how they interact with other people.
*  Right?
*  Like if you just sit outside, maybe we can sit outside in coffee shops these days
*  and you can people watch.
*  And you see this person, oh, they're like talking to the guy at the flower shop.
*  That's cool.
*  Maybe they are buying flowers for a friend or something.
*  Or you look on social media and see who, you know, such and such follows on Twitter.
*  Or, you know, what do you do on Friday nights?
*  All of these things.
*  If you observe a person and see how they interact with other people,
*  you can glean a lot of information about that person.
*  So how does someone relate to other folks of their kind?
*  And so the point is this theorem says the same is true in mathematics.
*  Except it's not just that you can learn a lot, but you can learn everything,
*  everything you need to know about a quote unquote mathematical person,
*  i.e. an object like a group, whatever.
*  All you, not all you need to do, but all of that information is contained
*  in how that object relates.
*  So what does it mean to relate?
*  Well, you know, this gets to words, gets to ideas like, you know,
*  how do I go from one group to another?
*  How do I go from one vector space to another?
*  These are things like linear transformations or group homomorphisms
*  or continuous functions.
*  You know, a relationship there is really like an arrow from your object
*  to something else, where that arrow is, you know, a function that maybe
*  preserves whatever structure that's of interest in that category that you're in.
*  So when you say that, the example that comes to mind,
*  and I'm not sure if I'm overinterpreting or not, is if I have some space,
*  some manifold or whatever, I remember my delight when I learned
*  that the set of points in the space is the same as the set of maps
*  from one point into the space.
*  Yes, yes, yes.
*  So is that an example or is that the essence of the Unita Lemma
*  or is there more richness there that I'm not immediately perceiving?
*  Okay, so that is intimately related to the Unita Lemma.
*  The Unita Lemma says, let's see,
*  it says a little bit more if you're thinking of manifolds,
*  but suppose we were to forget all of the structure of a manifold,
*  like, okay, you have these charts, let's just think about it,
*  you mentioned points, so let's just think of it as points for now
*  and kind of forget the topology.
*  In that case, I think a corollary of the Unita Lemma or one of them,
*  it says exactly what you said.
*  The set of all points are the same thing as, you know,
*  functions from the one point set into your set.
*  In that case, for sets, it's quite, it's like, oh, that's underwhelming
*  because there's not that much structure and so you might want to ask for more
*  and so the Unita Lemma kind of gives you more in that.
*  I totally get it. You cleared up my confusion there
*  because what you're saying is, of course, I have more than a set.
*  I have, you know, a group, I can multiply things
*  or, you know, some topology or whatever
*  and none of that is captured in this mapping points into it,
*  but it is captured by its relationships to other things.
*  Exactly, exactly.
*  Oh, so that's exactly what I want to say.
*  Thank you.
*  The Unita Lemma says it's not enough just to look at functions,
*  you know, from the point into your manifold,
*  but because the point is a manifold, it's not a very interesting one.
*  So look at all of the other ones.
*  You know, there's like the circles and exactly all of them.
*  So when you consider all of these other manifolds into yours,
*  that gives you all of the information you need to know.
*  So it doesn't just tell you it's cardinality, you know,
*  but you might get other, you know, like, oh, it's smoothness or something like that.
*  Okay, but now it went from being trivial to being overwhelming.
*  How in the world do I get useful work out of knowing
*  that the set of relationships between my object
*  and every other conceivable object
*  tells me everything there is to know about it?
*  I mean, how do I know all that?
*  What do I do with this useful, with this information?
*  Yeah, so I like to answer this question back in the context of language,
*  which we were thinking about earlier.
*  So there's a, I mentioned, you know, we were talking about philosophers in quotes earlier.
*  I couldn't think of one then, but here's a quote from a linguist.
*  So not quite the same, but I like this quote,
*  which is very much like the Oneida lemma, but in the context of language.
*  So there's a linguist, John Firth.
*  I think in a 1915, 1957 paper, he says,
*  you shall know a word by the company it keeps.
*  I like that.
*  Yeah, you shall know a word by the company it keeps.
*  So like, what's the meaning of fire truck?
*  Well, it's kind of like all of the context
*  in which the word fire truck appears in the English language.
*  Okay, so fire trucks are like maybe red.
*  I don't know, sometimes they're yellow, I guess.
*  Maybe they speed quickly.
*  From all of the expressions in which the word fire truck appears,
*  you can kind of glean information about that word.
*  But the Oneida lemma, if we were to take the spirit of the Oneida lemma,
*  you know, borrowing from category theory,
*  you kind of recover John Firth's quote.
*  Oh, everything I need to know about this word,
*  the meaning of the word fire truck,
*  is contained in the network of ways that word fits into the language.
*  Right.
*  Okay, and how is this useful?
*  Well, it goes back to sort of this experimental motivation
*  we were talking about earlier.
*  It's really interesting that large language models
*  really only have access to the context, you know, in which a word appears.
*  They just sort of see what goes with what in the language
*  together with the statistics.
*  And somehow from that can glean semantic information about words.
*  How do you know that?
*  Well, because they can generate coherent pieces of text,
*  you know, that look like a human wrote them.
*  So something in there, you're using the context of a word,
*  which both the Oneida lemma and, you know, a linguist like John Firth
*  might say that's a pretty good proxy for the meaning of that word.
*  Yeah.
*  Somehow that's being used by a machine to then learn something about the language
*  to the extent that it can produce good text.
*  So I think there's the usefulness.
*  It's being used actually as we speak somehow.
*  But then the math question is, oh, what really is that?
*  Okay, there's the Oneida lemma.
*  But if I know this algebraic and statistical structure,
*  maybe with, you know, help from category theory,
*  one question might be, oh, can I model this?
*  You know, can I represent this?
*  Maybe in the precise sense of representation theory,
*  since matrices we talked about, those are nice to work with.
*  In a way that captures this information,
*  you know, that's sort of theoretically clear.
*  Sometimes neural, not sometimes, but neural networks
*  I think are notorious for being kind of black boxes.
*  You know, you look inside and it's like, oh, 180 billion parameters.
*  What is happening?
*  Something, what? We don't know.
*  But maybe, you know, if you take a little bit of inspiration from category theory,
*  maybe from quantum physics, you know, linear algebra,
*  maybe these tools can kind of be combined in a way that's clarifying
*  sort of from an interpretability perspective, but also mathematically.
*  So that's one long-winded way of the usefulness I seek.
*  Well, let me push on the maybe that sneaked into your sentence right there
*  because it's very interesting to think of these deep learning models
*  and successes we've had in language generation and things like that.
*  And separately, it's fascinating to think about category theory
*  and these things you said about probabilities and quantum,
*  mathematically inspired versions of probabilities.
*  How, where are we on the stage from hopeful aspiration to concrete implementation
*  in actually using these mathematical ideas to help us with building,
*  not even necessarily building, understanding or doing something
*  with artificial intelligence or deep learning?
*  Yeah, so on this spectrum of, you know, theory to actual,
*  hey, can we see an experiment, you know, maybe at this moment, this day in 2021,
*  I think my collaborators and I might be, we're inching towards the experimental side of things
*  and actually have some stuff going, but really working on the theory for the moment.
*  Okay.
*  I think maybe as we progress and do a good job of explaining the ideas
*  in a way that's easier to understand than reading a technical paper,
*  maybe that might even encourage progress on the experimental side even more
*  as these ideas become accessible.
*  But it's certainly in progress.
*  Absolutely.
*  Okay, interesting.
*  So the other thing I wanted to press on is, I mean, you sneaked in what to many people
*  would be a massive metaphysical claim here that maybe you want to defend
*  or maybe you're just like, well, let's just see how it goes.
*  Namely that all the semantics is in the statistics of words appearing together.
*  Like when you say, okay, so a red fire truck appears a lot
*  and red idea doesn't appear that much.
*  And what you were getting at is the idea that if we knew all of the answers to the questions,
*  you know, how often do these combinations appear?
*  That's all there is to know in some sense about the language.
*  And some people are going to say, no, no, no.
*  When you say the word fire truck, that means something.
*  It means something out there in the world.
*  So I think that the perspective that you're sort of falling down on
*  and which is actually what I'm quite sympathetic to is probably something like pragmatism
*  in the philosophical tradition, William James and people like that, right?
*  The meaning of a word is its use.
*  I do think there are other people who would say, no, no, the meaning is the fire truck out there.
*  And do you care about this distinction?
*  Right. So I'm yeah, thank you for bringing this up before I get, you know, doused with fire or something.
*  So, yes, I am completely aware that that folks may say, what?
*  You can't make this claim that all semantic information is contained in just the statistics.
*  You know, of course, I'm aware of this.
*  So let me yes, let me give this caveat.
*  I acknowledge that there could be even more mathematical information.
*  You know, we started off by saying, hey, there's algebra.
*  So cool. Wait a second. That's not enough.
*  There's also statistics.
*  Now I'm at this point where I'm saying, hey, algebra and statistics, that gives you kind of everything.
*  Everything.
*  But yes, maybe there could be something else that we're not quite capturing.
*  So I want to acknowledge that. Yes.
*  And that's exciting. That's great. More math to be done.
*  However, quite an awful lot of semantic information is learned.
*  And I'm not, you know, making that up or saying like I stand my ground.
*  I'm saying look out into the world of, you know, language modeling.
*  There are, you know, companies being built around the success of how much information you can learn based on just algebra and statistics.
*  So kind of for now, you know, on my mathematical journey, I'm like, it's quite a lot.
*  Let me figure out this math too.
*  Then, you know, down the road, I'm sure there's so much more, a lot more to do.
*  But yeah, let me not be burned at the stake for this.
*  Well, no, no, no. I mean, I think that these are these are controversial questions.
*  Like we don't know the answer. That's why I'm just sort of it's fun to draw these connections.
*  But if I am, you know, part of my job as podcast host is to is to be skeptical and play the devil's advocate.
*  So if I'm the worries about the sort of language parsing application of artificial intelligence is that if you go outside the domain of the training set,
*  that a human being would understand how to extrapolate outside, whereas the computer cannot.
*  So I tried to come up with a good example here.
*  I'm not sure I succeeded, but here's my example.
*  If I put an elephant on the cardboard airplane, will it fly?
*  Because the point being that, you know, the language model might that's a that's a sentence no one has ever said before.
*  Right. Or a question no one has ever asked.
*  And the language model might say, well, airplanes fly.
*  So the answer is yes. But I said it was a cardboard airplane with an elephant on it.
*  And the language model might not know that that might make it difficult.
*  Do you have any is this a reasonable ask for a I to be able to answer questions like that?
*  So I from a hopeful viewpoint, I would like to say yes.
*  And let me give. So I love that example.
*  I like that a lot. So let me give give you an example, which I think may show that that they're kind of thinking or this, you know, this idea to generalize beyond just sort of this data set.
*  So I'm going to botch this.
*  So apologies to the author of this article.
*  But I think last year or semi recently, there was an article in the MIT technology review about one of these well-known large language models.
*  And it and it was given a prompt, you know, was asked a question.
*  I can't remember quite exactly. So I'm super paraphrasing.
*  But it was basically like, you know, you know, we're in a room of someone's house, maybe in the living room and in the dining room.
*  Our friends are over there about to have dinner.
*  But we have to bring in an extra table, you know, because there's lots of people.
*  So we have a table. So how do we bring it from the living room into the dining room through a doorway?
*  Like, how are we going to fit it? OK, how do we get this table to fit through the doorway and sort of let the language model answer that question?
*  This is kind of analogous to your question of I have an elephant on this cardboard plane.
*  So it was so funny because this large language model, I mean, what would we do as a person?
*  What would we do? I have a table. I want to bring it into the other room.
*  It doesn't fit through the door. So what would we do?
*  Maybe just rotate it, you know, so the legs aren't grabbing through the door or something.
*  This language model in this article, it's like get a handsaw and chop it in two and then bring each piece individually through the door.
*  And it was funny because the the author of the article kind of presented this, you know, to show the case.
*  Look how silly this thing is. Like it really can't think like a human.
*  Like how dumb. But actually it's showing you that it like learned something about the earth.
*  You know, it learned that if you have a table and you can cut it in half, it's smaller.
*  And then maybe then they can fit through the door. So I think that that, you know, that's kind of thinking outside of the box.
*  I wouldn't have said that if someone asked me.
*  So maybe there there is a lot in there, you know, in these kind of billions of parameters.
*  Something's being learned, but it's still kind of early stages.
*  But examples like that make me think, oh, maybe maybe it can quite generalize in ways that we were suspicious of.
*  No, I think that's perfectly fair. I mean, I'm sympathetic both to the worry that there's a certain lack of
*  manifest image, common sensical view of the world, that it's harder to train the AI and therefore it will get into trouble when we ask it to leave its domain.
*  But I'm also sympathetic to the idea that in some sense, there's no spooky essences in the world.
*  There's only all the relationships between things.
*  So in principle, if we could teach the computer all of those things, it would know everything there is to know.
*  I'm not sure. Yeah.
*  OK, but I think that we have failed to be sufficiently inscrutable here.
*  I think that everything we've said is too easy to understand.
*  So I want to move on to your more recent work on entropy, because I like I like the word entropy.
*  This is the mistake I made to the audience.
*  I read that you had a paper and the word entropy was in the title and I thought that I'd be able to understand it.
*  And that didn't happen. But that's why I have you on the podcast.
*  So you can help me out here.
*  Tell us how you as a mathematician think about the word entropy and then we can put it to work and talk about operands and simplices.
*  Yes. Yes. So when I think of the word entropy, I really have in mind for that paper Shannon entropy.
*  And so I think there's a very easy way to sort of think of think of it.
*  And it's kind of the elementary way that I think of it.
*  So if you have a probability distribution, let's just say on a finite set earlier, we talked about rolling a die, for example.
*  But, you know, whatever you have some little list of probabilities.
*  And I think of the entropy of that list of probabilities or that distribution as sort of the amount of surprise that's contained in it or the amount of uncertainty.
*  So I think the easiest way to think of it is the following.
*  So if you have an event that you know for certain is going to happen, you know, I really love coffee.
*  And with probability one, I will have a cup every morning when I wake up.
*  So if you know that about me, if I tell you, hey, I had coffee this morning, you are absolutely not surprised.
*  Didn't learn anything. Yeah, didn't learn any information.
*  So in that, it turns out when you look at the definition of entropy, the actual formula, you get a number and that number is zero.
*  So it's like, how surprised were you? Zero surprised.
*  So entropy is a is a number associated to a probability distribution and it's zero or positive.
*  And sort of as you increase in that positivity, it tells you how surprised you should kind of feel or how much information you gained based on these,
*  you know, the distribution on these events. So I think that's kind of a friendly way to think of it.
*  Yeah. So just to be clear, so we're back in the world of probability distributions and probability distributions are sets of numbers that are all non-negative and they add to one, right?
*  That's what a probability distribution is.
*  And so for each probability distribution, there is an entropy that you can calculate.
*  And it's basically is it safe to say, do you think of it as how spread out the probability distribution is?
*  If it's all peak, the entropy is low. And if it's all spread out, the entropy is high.
*  Yeah, yeah, exactly. So if you have a distribution where basically all of the events are the same, you know, probability, you know, like if you have n events, let's say y n, five,
*  I have five things and they all have probability one fifth, you know, then in that case, they're kind of all spread out evenly and the entropy is as high as it can be.
*  And that's kind of you have like equal amount of surprise, like, oh, it could have been any one of the five and it was this one.
*  Wow. But yes, if it's kind of peaked or concentrated at at one in that sense, it's the entropy is zero.
*  No surprise. You know, I had coffee this morning.
*  Big deal. And so in your paper, you link this information theoretic notion of entropy to issues in algebra and topology, which is all very cool.
*  But maybe so I want to get into that. But I mean, is there a big picture point that you're trying to get at?
*  What is the goal here? We've been studying entropy ever since Boltzmann and Gibbs back in the eighteen hundreds.
*  Like, what is it that we're trying to understand by relating it to these issues in algebra and topology?
*  Yeah. So I guess there are a couple of ways I could answer this from a math perspective.
*  Let me say the first one that comes to mind. So entropy assigns a number to a probability distribution, as you said.
*  So you can kind of think of it as a function. If I think of, you know, the set of all probability distributions on five elements,
*  entropy assigns to each one of them a number, which is like the information content of each distribution.
*  So you might want to characterize that function like, oh, I might have other functions that go from probability distributions to numbers are like they all do.
*  They all convey information content. Do they all have the flavor of entropy?
*  So a mathematician might want to look for a characterization of entropy.
*  You know, if I have a function that spits out a number on a probability distribution,
*  how do I know that I can interpret that number is some type of amount of information conveyed or something that behaves like Shannon entropy?
*  Are there properties that entropy satisfies?
*  You know, can I list them? Is that list efficient to tell me, you know, if I walk down the street and oh, I run into another function.
*  Wait, let me pull out my checklist. Let's see. You satisfy these properties. Hey, you're also entropy.
*  Right. You might want to know about that. And that's a nice organizational tool.
*  So one thing that my paper does give gives kind of one of these characterizations of entropy.
*  But it does it by using tools from algebra and topology.
*  And then you might say, why would you bring in that hefty duty stuff?
*  Like we were happy over here with just list of numbers. Why in the world go to algebra and topology?
*  I think that's a very exciting kind of result when you can connect fields that do not feel related on the surface.
*  For me, that's very exciting and might suggest like, hey, maybe there's something deeper going on.
*  You know, we thought about entropy in this one way.
*  But if we can look at it from a topological perspective or an algebraic perspective, maybe that can give us new insights or sort of new intuitions.
*  So that was sort of another motivation for pursuing a project like this, a little project like this, because it felt like it connected things that shouldn't really feel connected.
*  But there it is. The math is there. And that's interesting, I think.
*  No, that's exactly what got me. Like, I'm like, what is it? I think I thought I knew entropy. Why is it being connected to all these things?
*  And so one of the ideas, I think this is worth trying to explain, which is the idea of a simplex, because I know what a simplex is.
*  I took topology courses when I was in graduate school.
*  I learned about homology and cohomology and things like that.
*  And I and you just say a probability distribution is a simplex.
*  And I never thought about that. Why don't you explain what is going on there if that's possible?
*  Sure, sure. So let me give a definition.
*  And actually, so I'm going to make this really easy for everyone. Let's just make this a definition.
*  So let's say that an n simplex, okay, so pick a number n, natural number, one, two, three, blah, blah.
*  An n simplex is the set of all probability distributions on n elements.
*  So in other words, let's just think when n is one.
*  I have one element and I need a number associated to that element that adds up to one and is non-negative.
*  Okay, well, I only have one option.
*  Okay, one. So that's kind of boring.
*  You know, that's my coffee scenario. I woke up this morning.
*  I had coffee, probability one.
*  Okay, so let's think of n is two now.
*  If n is two, a, oh, oh, I think there's some.
*  Okay, so this is kind of annoying.
*  I made a little bit of an indexing mistake.
*  I think technically if we were to, you know, look in a textbook or Wikipedia,
*  an n simplex is a distribution on n plus one points.
*  I think that's exactly right.
*  It's exactly that technicality that was confusing you.
*  But yeah, okay, that's okay.
*  That's annoying.
*  Okay, so.
*  Don't roll with us. The audience is with us this far.
*  Okay, so a zero simplex is a distribution on one element.
*  And that's my coffee in the morning. One point.
*  Okay, fine. A one simplex is the probability,
*  is the totality of all probability distributions on two points.
*  So those are, you know, the set of all pairs of numbers,
*  you know, one half, one half or whatever that are non-negative.
*  And when you add them together, you get one.
*  So all pairs of real numbers satisfying that together,
*  all of those pairs are called a one simplex.
*  And the reason, by the way, that you made this indexing mistake,
*  which is the most natural thing in the world,
*  is because on a probability distribution,
*  we know the numbers have to add to one.
*  So if there are n numbers, you only need to tell me n minus one of them.
*  And I know what the other one is, right?
*  That's what's going on.
*  So if you have two variables,
*  as soon as you give me the probability of one of them,
*  I know the probability on the other one right away.
*  So I don't even need to calculate that or whatever.
*  That's right. That's right.
*  Don't need to specify it.
*  Yeah. And that's kind of like, you know,
*  if I am thinking of a one simplex, it's usually drawn as a line.
*  Yeah, it's a one-dimensional thing.
*  It's a one-dimensional thing.
*  And that's because if you kind of chop your line into two bits
*  and you know the length of the first one
*  and you know both of them must add up to one,
*  you know the length of the second one.
*  So that's kind of it.
*  Okay. So thank you.
*  We have this indexing thing going on,
*  but this is exactly why some shouldn't be too missed.
*  And the one simplex then is just the list of numbers from zero to one.
*  The one simplex.
*  Because it can't be less than zero.
*  No negative numbers are allowed in a probability
*  and it can't be more than one.
*  Right. Yeah, exactly.
*  It's exactly, yeah.
*  You can think of it as the unit interval.
*  Yes, which is a line.
*  That's right.
*  Okay. So in general, an n simplex is the set of all probability distributions
*  on n plus one elements.
*  And so you can think of it actually when you kind of take this geometric perspective further.
*  It turns out that a two simplex looks like a triangle.
*  A three simplex looks like a tetrahedron.
*  And it looks like a triangle because you might think you need to give me two numbers
*  and it might be a square,
*  but if the two numbers are too big, they're going to add to more than one.
*  Right. Exactly.
*  Half that square is cut off.
*  Yeah, exactly.
*  So half the square is cut off.
*  Exactly right.
*  Yep.
*  So when we think of simplices, we really, you know,
*  you can think of this definition I gave
*  or you can have the pictures in mind.
*  Oh, zero simplex is a point, one simplex is a line, two simplex is a triangle,
*  and then higher and higher you go.
*  This is actually where the topology comes in.
*  Exactly right.
*  Because I have a shape, you know, a triangle.
*  I can think of that as a subset of the XY plane, you know, R2.
*  Okay, R2 is a topological space.
*  I have a subspace of that.
*  There's my topology.
*  So actually, if entropy has something to do with probabilities
*  and probabilities are really simplices,
*  then the connection to topology is maybe not too surprising.
*  It's been right there all along.
*  Yeah.
*  All right, only a mathematician would say that, but okay.
*  But okay, so let me get it right.
*  When we are visualizing like this line or the triangle or whatever,
*  that is really the set of all probability distributions, right?
*  That's right.
*  Each point inside is a probability distribution.
*  Exactly, exactly.
*  So entropy is a function on the simplex.
*  Yes, it's a function on the simplex.
*  And in fact, you can think, fix a simplex, you know, fix a number n.
*  Maybe you have a triangle or you have a tetrahedron or you have a line.
*  Pick one of them.
*  Don't think of all of them.
*  Just pick one of those shapes.
*  Then you can think of entropy as a function from that one shape into the real numbers, right?
*  So you fix the length of your list of probabilities,
*  you know, all of those of length 13 or something.
*  That's a 12 simplex, 14 simplex.
*  Okay, anyway, so you think of these numbers
*  and then entropy is a function on that simplex, you know, valued in the reals.
*  So really, if you just wanted to have a conversation, you know, about entropy
*  and you kind of wanted to throw in all probability distributions of any length,
*  you actually have a collection of functions, each of which is called entropy.
*  You know, I have a function out of the zero simplex.
*  That's the entropy, you know, of the boring probability distribution one.
*  But I also have a function out of the one simplex.
*  That's entropy.
*  A function out of the two simplex.
*  That's entropy and so forth.
*  So Shannon entropy really says, hey, first pick a simplex.
*  First pick, you know, the number n,
*  then ask for the entropy of a point in that simplex.
*  And you mentioned, sure, that the two simplex is a little part of the plane
*  and therefore there's some topology going in there,
*  but there's more topology than that, right?
*  Like the, like I said, no one ever told me that a simplex is a probability distribution
*  or a set of probability distributions,
*  but the reason why they came up is because we were learning about topology.
*  I think homology in particular.
*  Is it feasible to explain how this concept of a simplex helps us understand
*  the topological structure of complicated spaces?
*  Ah, I see.
*  Yes.
*  Oh, are you thinking of maybe looking at a topological space,
*  trying to under general?
*  Let's just forget about entropy for a moment.
*  A general topological space,
*  trying to understand something of that complicated, messy, who knows what it is.
*  And then mathematicians have this technique of kind of imagining
*  it's built up from little pieces called simplices.
*  Before I answer the question, is that kind of the...
*  That is exactly it and sort of figuring out how many holes there are
*  and how many donuts, etc.
*  Yes.
*  Yes, yes, yes.
*  Okay, right.
*  So this gets into the ideas of homology and cohomology.
*  Okay, so this is exactly right.
*  You may...
*  Okay, so topology, I think for viewers, we've used it several times now,
*  so maybe folks know what it is, but I like to think of it as like this squishy
*  version of geometry, you know.
*  To a topologist, a circle and a triangle is the same thing
*  because if a triangle is made out of a wet noodle
*  and you kind of squish in the corners, you can get a circle.
*  So in topology, this kind of squishiness is allowed.
*  But if that's allowed, then like what are we doing?
*  You know, this kind of goes back to the idea of when are two things the same,
*  which we talked about in category theory a while ago.
*  Like when are two topological spaces the same or not?
*  And one thing that you can use to kind of distinguish spaces is by counting
*  how many kind of fundamental holes do they have.
*  You know, a circle and a triangle are kind of the same.
*  You can see that in they have, you know, holes.
*  If I hold a little key ring, you know, I can stick my finger through it.
*  That's kind of the hole.
*  But not all topological spaces can we see with our real, you know, with our eyes.
*  You know, I can't not there are other spaces that aren't key rings, you know,
*  and they're very abstract and they're in some textbook buried deep in the pages.
*  And how can I understand that object?
*  You know, I can only visualize it kind of in my mind based on some equations
*  or something, and I can't really hold it in my hands.
*  But how can I still investigate it?
*  And this is where simplices are very helpful.
*  You can imagine kind of probing your space with maybe simplices.
*  So for example, think of just the surface of something like a donut or,
*  you know, a torus.
*  Maybe I can think of kind of triangulating that surface, you know,
*  maybe thinking of the entire exterior of a donut is very difficult.
*  But if I kind of imagine like a triangular shaped grid,
*  I can maybe kind of understand something about the little pieces.
*  Yeah, so sorry.
*  So in other words, if you have some wiggly thing,
*  topological space of whatever number of dimensions,
*  in principle, a wiggly thing requires an infinite amount of information to specify.
*  Yes.
*  But if we just chunk it up, if we tessellate it, we can keep the topology the same
*  while reducing that infinite amount of information to a finite number of sort of
*  what triangle is connected to what or what tetrahedron is connected to what.
*  Exactly, exactly.
*  It's a finite number of things and it's also a combinatorial thing.
*  You know, oh, a two simplex has these many edges and then it's connected to this thing
*  with these many edges and maybe there are some intersections or something.
*  So you've taken something that's kind of complicated and yeah, wiggly and just
*  what do I do with this?
*  But if you can break it up into smaller pieces that are maybe bite-size easier to handle,
*  maybe combinatorials, you can start to kind of count things.
*  That makes it more manageable.
*  And then yeah, then there's this leap.
*  You know, you have to bring in some kind of tools to make sense of what you mean by a
*  whole.
*  Like I know what that means in a key ring, but what if I have some abstract space?
*  Like what is a mathematician's definition of a whole in a topological space?
*  And what if I am in, you know, 17 dimensions?
*  How in the world do I make sense of that?
*  And that's kind of where these simplicial tools are very useful to answer these kind of questions.
*  Yes, and somehow this is going to connect to derivations and upper-eds.
*  I can try to find a thread that gets us there, but I think that would be dumb when I could
*  just ask you to do it for us.
*  Yeah, so let me give the light version L-I-T-E and then depending on which directions we
*  want to go, we can get deeper.
*  But let me, yeah, there are a lot of words.
*  Oh, did, simplices, derivations, algebra, what's happening, upper-eds.
*  Okay, so here's the easiest way that I can say this.
*  Think, let's think back to Shannon entropy, entropy, okay, the amount of kind of surprised
*  or information contained in a probability distribution.
*  It turns out, and it's not too, it's not hard at all to show, that entropy fits into a
*  formula that looks eerily similar to something you might see in different places across the
*  mathematical landscape.
*  And that formula kind of hints that entropy behaves like a derivation.
*  What's a derivation?
*  We'll think back to calculus and the Leibniz rule from calculus.
*  The product rule, yeah.
*  We all learned this a long time ago.
*  If I have two functions, f and g, what's the derivative of f times g?
*  You know, and then we all learn about this product rule.
*  Oh, it's the derivative of f times g plus f times the derivative of g.
*  Okay, the Leibniz rule.
*  Well, it turns out that entropy satisfies an equation that looks very much like this,
*  but kind of not really, but you can see this formula and you think to yourself, oh,
*  something's going on.
*  So long story short, my paper is taking that kind of intuitive something's going on here
*  and making it very precise and saying there is a very precise way in which entropy
*  satisfies the Leibniz rule.
*  And moreover, anytime you have a function in a certain context, I have to be very
*  precise, that satisfies the Leibniz rule.
*  It's basically entropy.
*  You know, something up to a constant multiple or something.
*  Good.
*  Yeah, this is the kind of thing that gets mathematicians very excited where they show
*  that something is something else.
*  Yeah, exactly.
*  Exactly.
*  And is this related to, that was a very nice light derivation, good, or explanation.
*  One of the elements that comes in here that I think is graspable is the idea that the
*  boundary of a boundary is zero, right?
*  This very famous deep topological fact.
*  Like if you take a disc, its boundary is a circle, but the circle doesn't have any
*  boundary.
*  It's boundaryless.
*  And the way that a fancy differential topologist would express that is as d squared
*  equals zero, where this d is the boundary operator.
*  So am I reading too much into the letter d or is this relating d to a derivative and
*  therefore now to entropy?
*  So at the moment, we both might be reading too much into it.
*  So in the paper, I unfortunately do not have the opportunity to say that the d that you
*  see there, if you apply it twice, you get zero.
*  I think though that would be very exciting.
*  And I think that a paper like this suggests that it should be investigated more for this
*  very reason because there is a precise sense in which you think about, you know, derivatives
*  in the sense of calculus, derivations and these boundary operators, you know, things
*  that satisfy d squared equals zero, go hand in hand.
*  If folks want to look up something, they can look up D'Rom cohomology, since we were
*  talking about cohomology earlier, and see that these ideas are mixing together very
*  intimately and beautifully in a nice way.
*  Now, I didn't get so far there.
*  I didn't get to that point yet.
*  But I think that it suggests that there's something deeper to look in that direction.
*  There have been other results in the past few years by other mathematicians involving
*  other characterizations of entropy that also swirl around this D squared equals zero idea.
*  I think that that's very peculiar.
*  I mean, I'm talking in the last, you know, four or five years or so.
*  So the fact that entropy is kind of coming up in these topological and algebraic areas,
*  you know, independently might suggest that there is indeed something going on there.
*  And is it possible that there's some sort of duality relationship?
*  Because in the world of homology and cohomology, our audience knows what neither one of these
*  words mean, but the idea is that these are two different ways of topologically
*  characterizing spaces, one of which sort of looks at the structure of spaces and the
*  other one looks at the functions you can put on spaces.
*  And it turns out that these very different sounding words are in fact sort of mirror
*  images of each other in some particular way.
*  And I'm wondering if maybe that is what is going on with entropy versus
*  I'm not sure what entropy would be dual to, but somehow these these simplicial structures,
*  I don't know.
*  Yeah, so I would say that this is very active research and something I am thinking about
*  daily these days.
*  So maybe come back in a year and I'll have really great answers for that.
*  But that's exactly where I'm headed next.
*  Yes.
*  And it's only possible because of the psychological difference between physicists and
*  mathematicians because, you know, the physicists will say, well, look, what do you mean
*  entropy?
*  It's not it's a number like you give me a distribution.
*  I give you a number.
*  There's really nothing more to say.
*  But the mathematician will say, you know, with like with the with the boundary operation,
*  the boundary of an n dimensional thing is an n minus one dimensional thing.
*  And so the physicists just stops there.
*  But the mathematician says let's consider the combination of all n dimensional things
*  and n minus one dimensional things and n minus two dimensional things as like one giant
*  thing.
*  And the physicist said you've lost me.
*  You're like you've gone crazy.
*  But when you make that leap, you're now able to invent operators and relationships and
*  things like that and maybe discovered things about entropy 150 years later that the
*  physicists never found out.
*  Yes.
*  Yes.
*  That's exactly right.
*  And this reminds me a little bit of kind of the flavor of the paper that I wrote.
*  I mentioned that there is a there is a you know, a formula or an equation that entropy
*  satisfies that kind of got me into the project.
*  Oh, that that looks kind of like a derivation.
*  Can we make that precise?
*  What's interesting is that the paper kind of develops a more general framework for which
*  that equation is a special case.
*  Good.
*  So it kind of says, yeah, that's just the shadow of something much richer going on.
*  There's something kind of hovering overhead, you know, above head for which that one equation
*  that we kind of all know, you know, we see in our favorite information theory textbook
*  or something.
*  It's just an example of something richer, maybe that's going on that's pulling from these
*  tools that maybe you didn't know they were there.
*  Like just look up.
*  Oh, they're floating on the ceiling or something.
*  We just didn't know.
*  So so I think, yeah, it might feel complicated to say, wait a second.
*  We started with probability distributions on in things and now you're like consider n
*  minus one and n minus two and then maps between them and D squared equals zero.
*  What?
*  But actually when you when you kind of do all this, it might seem, you know, like heavy
*  lifting at first, but then you're quite rewarded at the end because it kind of gives you a
*  different vantage point for which a lot of things may fall out nicely at the end.
*  And I can't think of a better place to end our conversation than exactly that.
*  Hoping that everything falls out nicely from the end.
*  So Ty, Janay Bradley, thanks so much for being on the Mindscape podcast.
*  Thank you, Sean.
*  It was great to be here.

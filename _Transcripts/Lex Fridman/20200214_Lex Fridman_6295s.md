---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 6295s
Video Keywords: ['vladimir vapnik', 'deep learning', 'statistical learning', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 50027
Video Rating: None
Video Description: Vladimir Vapnik is the co-inventor of support vector machines, support vector clustering, VC theory, and many foundational ideas in statistical learning. He was born in the Soviet Union, worked at the Institute of Control Sciences in Moscow, then in the US, worked at AT&T, NEC Labs, Facebook AI Research, and now is a professor at Columbia University. His work has been cited over 200,000 times.

The associate lecture that Vladimir gave as part of the MIT Deep Learning series can be viewed here: https://www.youtube.com/watch?v=Ow25mjFjSmg

This episode is presented by Cash App. Download it & use code "LexPodcast":
Cash App (App Store): https://apple.co/2sPrUHe
Cash App (Google Play): https://bit.ly/2MlvP5w

PODCAST INFO:
Podcast website:
https://lexfridman.com/podcast
Apple Podcasts:
https://apple.co/2lwqZIr
Spotify:
https://spoti.fi/2nEwCF8
RSS:
https://lexfridman.com/feed/podcast/
Full episodes playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

OUTLINE:
0:00 - Introduction
2:55 - Alan Turing: science and engineering of intelligence
9:09 - What is a predicate?
14:22 - Plato's world of ideas and world of things
21:06 - Strong and weak convergence
28:37 - Deep learning and the essence of intelligence
50:36 - Symbolic AI and logic-based systems
54:31 - How hard is 2D image understanding?
1:00:23 - Data
1:06:39 - Language
1:14:54 - Beautiful idea in statistical theory of learning
1:19:28 - Intelligence and heuristics
1:22:23 - Reasoning
1:25:11 - Role of philosophy in learning theory
1:31:40 - Music (speaking in Russian)
1:35:08 - Mortality

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Vladimir Vapnik Predicates, Invariants, and the Essence of Intelligence  Lex Fridman Podcast #71
**Lex Fridman:** [February 14, 2020](https://www.youtube.com/watch?v=bQa7hpUpMzM)
*  The following is a conversation with Vladimir Vapnik, part two, the second time we spoke on the podcast.
*  He's the co-inventor of support vector machines, support vector clustering, VC theory, and many foundational ideas in statistical learning.
*  He was born in the Soviet Union, worked at the Institute of Control Sciences in Moscow,
*  then in the US, worked at AT&T, NEC Labs, Facebook AI Research, and now is a professor at Columbia University.
*  His work has been cited over 200,000 times.
*  The first time we spoke on the podcast was just over a year ago, one of the early episodes.
*  This time we spoke after a lecture he gave titled Complete Statistical Theory of Learning as part of the MIT series of lectures on deep learning
*  and AI that I organized.
*  I'll release the video of the lecture in the next few days.
*  This podcast and the lecture are independent from each other, so you don't need one to understand the other.
*  The lecture is quite technical and math heavy,
*  so if you do watch both, I recommend listening to this podcast first since the podcast is probably a bit more accessible.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube, give it five stars on Apple Podcast,
*  support it on Patreon, or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N.
*  As usual, I'll do one or two minutes of ads now and never any ads in the middle that can break the flow of the conversation.
*  I hope that works for you and doesn't hurt the listening experience.
*  This show is presented by Cash App, the number one finance app in the App Store. When you get it, use code LEXPODCAST.
*  Cash App lets you send money to friends, buy bitcoin, and invest in the stock market with as little as one dollar.
*  Broker services are provided by Cash App Investing, a subsidiary of Square, and member SIPC.
*  Since Cash App allows you to send and receive money digitally, peer-to-peer,
*  and security in all digital transactions is very important, let me mention the PCI data security standard, PCI DSS level 1,
*  that Cash App is compliant with.
*  I'm a big fan of standards for safety and security,
*  and PCI DSS is a good example of that, where a bunch of competitors got together
*  and agreed that there needs to be a global standard around the security of transactions.
*  Now, we just need to do the same for autonomous vehicles and AI systems in general.
*  So again, if you get Cash App from the App Store or Google Play and use the code LEXPODCAST,
*  you get ten dollars, and Cash App will also donate ten dollars to first.
*  One of my favorite organizations that is helping to advance robotics and STEM education for young people around the world.
*  And now, here's my conversation with Vladimir Vapnik.
*  You and I talked about Alan Turing yesterday a little bit.
*  And that he, as the father of artificial intelligence, may have instilled in our field an ethic of engineering and not science.
*  Seeking more to build intelligence rather than to understand it.
*  What do you think is the difference between these two paths of engineering intelligence and the science of intelligence?
*  It's a completely different story.
*  Engineering is an imitation of human activity.
*  You have to make
*  a device which behaves as humans behave.
*  It has all the functions of a human.
*  It doesn't matter how you do it.
*  But to understand what is intelligence about is quite a different problem.
*  So I think, I believe that it's somehow related to predicate we talked yesterday about.
*  Because
*  look at the Vladimir Propp's idea.
*  He just found 31 here.
*  He predicates.
*  He calls it units.
*  Which can explain human behavior, at least in Russian tales.
*  He looks at Russian tales and derives from that. And then people realize that it's more wide than in Russian tales.
*  It is on TV, in movie serials, and so on and so on.
*  So you're talking about
*  Vladimir Propp, who in 1928 published a book, Morphology of the Folktale, describing 31 predicates that
*  have this kind of sequential
*  structure that a lot of the stories, narratives follow in Russian folklore and in other content. We'll talk about it.
*  I'd like to talk about predicates in a focused way.
*  But let me, if you allow me to stay zoomed out on our friend Alan Turing.
*  And you know, he inspired a generation with the imitation game.
*  Yes.
*  Do you think, if we can linger on it a little bit longer, do you think we can
*  learn, do you think learning to imitate intelligence can get us closer to the science, to understanding intelligence?
*  So why do you think imitation is so far from understanding?
*  I think that it is different between you have different goals.
*  So
*  your goal is to create something, something useful.
*  And that is great.
*  And you can see how
*  much things was done, and I believe that it will be done even more.
*  It's self-driving cars and also this business.
*  It is great.
*  And it was inspired by
*  Turing vision.
*  But understanding is very difficult. It's more or less philosophical category.
*  What means understand the world?
*  I believe in scheme which starts from Plato.
*  That there exists world of ideas.
*  I believe that intelligence it is world of ideas.
*  But it is world of pure ideas.
*  And when you
*  combine them with
*  reality things, it creates, as in my case, invariants, which is very specific.
*  And that I believe the combination
*  of
*  ideas in way to constructing invariant is intelligence. But first of all
*  predicate.
*  If you know predicate and hopefully then
*  not too much predicate exist.
*  For example, 31 predicate for human behavior. It is not a lot.
*  Vladimir Propp used
*  31,
*  you can even call them predicates, 31 predicates to describe
*  stories, narratives. So you think human behavior,
*  how much of human behavior, how much of our world, our universe,
*  all the things that matter in our existence
*  can be summarized in predicates of the kind that Propp was working with.
*  I think that
*  we have a lot of form of behavior.
*  But I think that predicate is much less.
*  Because even in these examples, which I gave you yesterday,
*  you saw
*  that predicate
*  can be
*  one predicate can construct many different invariants
*  depending on your data.
*  They're applying to different data and they give different invariants.
*  So, but pure ideas,
*  maybe not so much.
*  Not so many. I don't know about that. But my guess, I hope that's why challenge
*  about
*  digital recognition, how much you need.
*  I think we'll talk about computer vision and 2D images a little bit in your challenge.
*  That's exactly about intelligence.
*  That's exactly
*  about,
*  that hopes to be exactly about the spirit of intelligence in the simplest possible way.
*  Absolutely. You should start this simplest way.
*  Otherwise, you will not be able to do it.
*  Well, there's an open question whether starting at the MNIST digit recognition
*  is a step towards intelligence or it's an entirely different thing.
*  I think that to beat
*  records
*  using say 100, 200 times less examples, you need intelligence.
*  You need intelligence. So let's, because you use this term and it would be nice.
*  I'd like to ask simple, maybe even dumb questions.
*  Let's start with a predicate.
*  In terms of terms and how you think about it, what is a predicate?
*  I don't know. I have a feeling formulas exist.
*  But
*  I believe that predicate for 2D images,
*  one of them is symmetry.
*  Hold on a second. Sorry. Sorry to interrupt and pull you back.
*  At the simplest level, we're not even, we're not being profound currently.
*  A predicate is a statement of something that is true.
*  Yes.
*  Do you think of predicates as somehow probabilistic in nature or is this binary,
*  this is truly constraints of logical statements about the world?
*  In my definition, the simplest predicate is 4D.
*  In my definition, the simplest predicate is function.
*  Function and you can use this function to make inner product that is predicate.
*  What's the input and what's the output of the function?
*  Input is x, something which is input in reality.
*  Say if you consider digit recognition, it's pixel space input.
*  But it is function which in pixel space.
*  But it can be any function from pixel space.
*  And you choose and I believe that there are several functions
*  which is important for understanding of images.
*  One of them is symmetry.
*  It's not so simple construction as I described with literarity, with all the stuff.
*  But another I believe, I don't know how many,
*  is how well-structurized is picture.
*  Structurized?
*  Yeah.
*  What do you mean by structurized?
*  It is formal definition.
*  Say something heavy on the left corner, not so heavy in the middle and so on.
*  You describe in general concept of what you assume.
*  Concepts, some kind of universal concepts.
*  Yeah.
*  But I don't know how to formalize this.
*  So this is the thing.
*  There's a million ways we can talk about this.
*  I'll keep bringing it up.
*  But we humans have such concepts when we look at digits.
*  But it's hard to put them just like you're saying now.
*  It's hard to put them into words.
*  You know, that is example.
*  When critics in music trying to describe music,
*  they use predicate.
*  And not too many predicate, but in different combination.
*  But they have some special words for describing music.
*  And the same should be for images.
*  But maybe there are critics who understand essence of what this image is about.
*  Do you think there exists critics who can summarize the essence of images, human beings?
*  I hope so, yes.
*  Explicitly state them on paper.
*  The fundamental question I'm asking is,
*  do you think there exists a small set of predicates that will summarize images?
*  It feels to our mind like it does.
*  The concept of what makes a two and a three and a four.
*  No, no, no.
*  It's not on this level.
*  It should not describe two, three, four.
*  It describes some construction which allow you to create invariants.
*  And invariants, sorry to stick on this terminology.
*  Invariants, it is property of your image.
*  I can say looking at my image, it is more or less symmetric.
*  And I can give you a value of symmetry.
*  Say, level of symmetry using this function which I gave yesterday.
*  And you can describe that your image has these characteristics exactly in the way
*  how musical critics describe music.
*  But this is invariant applied to specific data, to specific music, to something.
*  I strongly believe in these plot ideas that there exists a world of predicates and a world
*  of reality and predicates and realities somehow connected and you have to know that.
*  Let's talk about Plato a little bit.
*  So you draw a line from Plato to Hegel to Wigner to today.
*  Yes.
*  So Plato has forms of the universe.
*  The theory of forms, there is a world of ideas and a world of things as you talk about.
*  And there is a connection.
*  And presumably the world of ideas is very small and the world of things is arbitrarily big.
*  But they are all what Plato calls them like it is a shadow.
*  The real world is a shadow from the world of forms.
*  Yeah, you have projection of the world of ideas.
*  Very poetic.
*  In reality, you can realize this projection using these invariants because it is projection
*  for own specific examples which create specific features of specific objects.
*  So the essence of intelligence is while only being able to observe the world of things,
*  try to come up with a world of ideas.
*  Exactly.
*  Like in this music story.
*  Intelligent musical critics know all these words and have a feeling about what they mean.
*  I feel like that's a contradiction, intelligent music critics.
*  I think music is to be enjoyed in all its forms.
*  The notion of critic like a food critic.
*  No, I don't want to touch emotion.
*  That's an interesting question.
*  Emotion, there's certain elements of the human psychology, of the human experience,
*  which seem to almost contradict intelligence and reason.
*  Like emotion, like fear, like love, all of those things.
*  Are those not connected in any way to the space of ideas?
*  That I don't know.
*  I just want to be concentrated on a very simple story, on digit recognition.
*  So you don't think you have to love and fear death in order to recognize digits?
*  I don't know because it's so complicated.
*  It involves a lot of stuff which I never considered.
*  But I know about digit recognition.
*  And I know that for digit recognition, to get the records from a small number of observations,
*  you need predicate.
*  But not special predicate for this problem.
*  But universal predicate which understands the world of images.
*  Of visual information.
*  Visual, yeah.
*  But on the first step, they understand the world of handwritten digits or characters or something simple.
*  So like you said, symmetry is an interesting one.
*  That's what I think one of the predicate is related to symmetry.
*  But...
*  The level of symmetry.
*  Okay, degree of symmetry.
*  So you think symmetry at the bottom is a universal notion and there's
*  degrees of a single kind of symmetry or is there many kinds of symmetries?
*  Many kinds of symmetries.
*  There is a symmetry, anti-symmetry, say letter S.
*  So it has vertical anti-symmetry.
*  And it could be diagonal symmetry, vertical symmetry.
*  So when you cut vertically the letter S...
*  Yeah, then the upper part and lower part in different directions.
*  Yeah, inverted along the y-axis.
*  Yeah.
*  But that's just like one example of symmetry, right?
*  Isn't there like...
*  Right, but there is a degree of symmetry.
*  If you play all this linear stuff to do tangent distance, but whatever I describe,
*  you can have a degree of symmetry.
*  And that is what describing reason of image.
*  It is the same as you will describe this image.
*  Same about digitization, anti-symmetry, digit 3-symmetric, more or less look for symmetry.
*  Do you think such concepts like symmetry, predicates like symmetry,
*  is it a hierarchical set of concepts or are these independent distinct predicates
*  that we want to discover some set of?
*  No, there is a deal of symmetry.
*  And you can this idea of symmetry make very general, like degree of symmetry.
*  The degree of symmetry can be zero, no symmetry at all.
*  Or degree of symmetry, say, more or less symmetrical.
*  But you have one of these descriptions and symmetry can be different.
*  As I told, horizontal, vertical, diagonal, and anti-symmetry is also a concept of symmetry.
*  What about shape in general?
*  I mean, symmetry is a fascinating notion, but...
*  No, no, I'm talking about digit.
*  I would like to concentrate on all I would like to know, predicate for digit recognition.
*  Yes, but symmetry is not enough for digit recognition, right?
*  It is not necessarily for digit recognition.
*  It helps to create invariant which you can use when you will have examples for digit recognition.
*  You have regular problem of digit recognition, you have examples of the first class or second class.
*  Second class.
*  Plus, you know that there exists concept of symmetry.
*  And you apply when you're looking for decision rule, you will apply
*  concept of symmetry of this level of symmetry which you estimate from.
*  So let's talk.
*  Everything comes from weak convergence.
*  What is convergence?
*  What is weak convergence?
*  What is strong convergence?
*  I'm sorry, I'm going to do this to you.
*  What are we converging from and to?
*  You're converging...
*  You would like to have a function.
*  The function which, say, indicator function which indicate your digit five, for example.
*  A classification task.
*  Let's talk only about classification.
*  Classification means you will say whether this is a five or not,
*  or say which of the ten digits it is.
*  Right, right.
*  I would like to have these functions.
*  Then I have some examples.
*  I can consider property of these examples.
*  Say symmetry.
*  And I can measure level of symmetry for every digit.
*  And then I can take average from my training data, and I will consider only functions
*  of conditional probability which I'm looking for my decision rule.
*  Which applying to digits will give me the same average as I observed on training data.
*  So actually, this is different level of description of what you want.
*  You want not just...
*  You show not one digit.
*  You show this one digit.
*  You show this one digit.
*  You show not one digit.
*  You show this predicate.
*  Show general property of all digits which you have in mind.
*  If you have in mind digit three, it gives you property of digit three,
*  and you select as admissible set of function only function which keeps this property.
*  You will not consider other functions.
*  So you're immediately looking for smaller subset of function.
*  That's what you mean by admissible functions.
*  You have admissible function.
*  Exactly.
*  Which is still a pretty large...
*  For the number three, it's a large...
*  It is pretty large, but if you have one predicate.
*  But according to...
*  There is a strong and weak convergence.
*  Strong convergence is convergence in function.
*  You're looking at the function on one function,
*  and you're looking on the other function,
*  and square difference from them should be small.
*  If you take difference in any points,
*  make a square, make an integral, and it should be small.
*  That is convergence in function.
*  Suppose you have some function, any function.
*  So I would say...
*  I say that some function converge to this function.
*  If integral from square difference between them is small.
*  That's the definition of strong convergence.
*  That definition of strong...
*  Two functions, the integral, the difference, small.
*  It is convergence in functions.
*  But you have different convergence in functionals.
*  You take any function, you take some function phi,
*  and take inner product, this function is f function.
*  F zero function, which you want to find.
*  And that gives you some value.
*  So you say that set of functions converge
*  in inner product to this function.
*  If this value of inner product converge to value f zero.
*  That is for one phi.
*  But weak convergence requires that it converge
*  for any function of Hilbert space.
*  If it converge for any function of Hilbert space,
*  then you will say that this is weak convergence.
*  You can think that when you take integral,
*  that is property, integral property of function.
*  For example, if you will take sine or cosine,
*  it is coefficient of, say, Fourier expansion.
*  So if it converge for all coefficients of Fourier expansion,
*  so under some condition, it converge to function
*  you're looking for.
*  But weak convergence means any property.
*  Convergence is not point-wise,
*  but integral property of function.
*  So weak convergence means integral property of functions.
*  When I talking about predicate,
*  I would like to formulate which integral properties
*  I would like to have for convergence.
*  And if I will take one predicate,
*  it's function which I measure property.
*  If I will use one predicate and say,
*  I will consider only function
*  which give me the same value as this predicate,
*  I selecting set of functions from functions
*  which is admissible in the sense that function
*  which I looking for is this set of functions.
*  Because I checking in training,
*  in training data, it gives the same.
*  Yes, it always has to be connected to the training data
*  in terms of...
*  Yeah, but property, you can know independent
*  on training data.
*  And this guy, prop, says that there is formal property,
*  31 property.
*  A fairy tale, a Russian fairy tale.
*  All right, but Russian fairy tale is not so interesting.
*  More interesting is that people apply this to movies,
*  to theater, to different things.
*  And the same works, they're universal.
*  Well, so I would argue that there's a little bit
*  of a difference between the kinds of things
*  that were applied to which are essentially stories
*  and digit recognition.
*  It is the same story.
*  You're saying digits, there's a story within the digit.
*  Yeah.
*  But my point is why I hope that it possible
*  to beat record using not 60,000, but say 100 times less.
*  Because instead you will give predicates.
*  And you will select your decision not from white set
*  of functions, but from set of function
*  which keeps this predicates.
*  But predicate is not related just to digit recognition.
*  Right.
*  Like in Platt's case.
*  Do you think it's possible to automatically
*  discover the predicates?
*  So you basically said that the essence of intelligence
*  is the discovery of good predicates.
*  Yeah.
*  Now, the natural question is, you know,
*  that's what Einstein was good at doing in physics.
*  Can we make machines do these kinds of discovery
*  of good predicates?
*  Or is this ultimately a human endeavor?
*  That's I don't know.
*  I don't think that machine can do.
*  Because according to theory about weak convergence,
*  any function from Hilbert space can be predicated.
*  So you have infinite number of predicate in upper.
*  And before you don't know which predicate is good.
*  And which, but whatever probe show and why people call it
*  breakthrough, that there is not too many predicate
*  which cover most of situation happened in the world.
*  So there's a sea of predicates.
*  And most of the only a small amount are useful
*  for the kinds of things that happen in the world.
*  I think that I would say only small part of predicate
*  very useful.
*  Useful all of them.
*  Only very few are what we should let's call them
*  good predicates.
*  Very good predicate.
*  Very good predicate.
*  Very good predicate.
*  So can we linger on it?
*  What's your intuition?
*  Why is it hard for a machine to discover good predicates?
*  Even in my talk described how to do predicate.
*  How to find new predicate.
*  I'm not sure that it is very good.
*  What did you propose in your talk?
*  In my talk, I gave example for diabetes.
*  Diabetes, yeah.
*  When we achieve some percent, so then we're looking
*  from area where some sort of predicate
*  which I formulate does not keeps invariant.
*  So if it doesn't keep, I retrain my data.
*  I select only function which keeps this invariant.
*  And when I did it, I improve my performance.
*  I can looking for this predicate.
*  I know technically how to do that.
*  You can of course do it using machine.
*  But I'm not sure that we will construct
*  the smartest predicate.
*  Allow me to linger on it because that's the essence.
*  That's the challenge.
*  That is artificial.
*  That's the human level intelligence that we seek
*  is the discovery of these good predicates.
*  You've talked about deep learning as a way to...
*  The predicates they use and the functions are mediocre.
*  We can find better ones.
*  Let's talk about deep learning.
*  Sure, let's do it.
*  I know only Yann Sleikun, convolutional network.
*  And what else?
*  I don't know.
*  And it's a very simple convolution.
*  There's not much else to know.
*  Left and right.
*  I can do it like that with one predicate.
*  Convolution is a single predicate.
*  It's single predicate.
*  You know exactly.
*  You take the derivative for translation
*  and predicate should be kept.
*  So that's a single predicate,
*  but humans discovered that one.
*  Or at least...
*  That is a risk.
*  Not too many predicates.
*  And that is a big story because Yann did it 25 years ago
*  and nothing so clear was added to the deep network.
*  And then I don't understand why we should talk about
*  deep network instead of talking about
*  piecewise linear functions which keeps this predicate.
*  Well, the counter argument is that maybe the amount
*  of predicates necessary to solve general intelligence,
*  say in the space of images,
*  doing efficient recognition of handwritten digits
*  is very small.
*  And so we shouldn't be so obsessed about finding...
*  We'll find other good predicates like convolution, for example.
*  There has been other advancements like
*  if you look at the work with attention,
*  there's attentional mechanisms,
*  especially used in natural language,
*  focusing the network's ability to learn
*  at which part of the input to look at.
*  The thing is there's other things besides predicates
*  that are important for the actual engineering mechanism
*  of showing how much you can really do
*  given these predicates.
*  I mean, that's essentially the work of deep learning
*  is constructing architectures that are able to be
*  given the training data to be able to converge
*  towards a function that can approximate,
*  can generalize well.
*  It's an engineering problem.
*  Yeah, I understand.
*  But let's talk not on emotional level
*  but on a mathematical level.
*  You have a set of piecewise linear functions.
*  It is all possible neural networks.
*  It's just piecewise linear functions.
*  There's many, many pieces.
*  A large number of piecewise linear functions.
*  Exactly.
*  But...
*  Very large.
*  Very large.
*  Almost feels like too large.
*  It's still simpler than, say, convolution,
*  than reproducing kernel Hilbert space.
*  Which have a Hilbert set of functions.
*  What's Hilbert space?
*  It's space with infinite number of coordinates,
*  say, or function for expansion, something like that.
*  So it's much richer.
*  So when I'm talking about closed form solution,
*  I'm talking about this set of functions.
*  Not piecewise linear set, which is particular case.
*  I have...
*  It is small part...
*  The neural networks is a small part of the space
*  you're talking about, functions you're talking about.
*  Small, small, say, small set of functions.
*  Let me take that.
*  But it is fine.
*  It is fine.
*  I don't want to discuss the small or big.
*  You take advantage.
*  So you have some set of functions.
*  So now when you're trying to create architecture,
*  you would like to create admissible set of functions.
*  Which all your tricks to use not all functions,
*  but some subset of this set of functions.
*  Say, when you're introducing convolutional net,
*  it is way to make this subset useful for you.
*  But from my point of view, convolutional,
*  it is something you want to keep some invariants,
*  say translation invariants.
*  But now if you understand this,
*  and you cannot explain on the level of ideas
*  what neural network does,
*  you should agree that it is much better
*  to have a set of functions.
*  And they say this set of functions should be admissible.
*  It must keep this invariant, this invariant, and that invariant.
*  You know that as soon as you incorporate new invariants,
*  set of function becomes smaller and smaller and smaller.
*  But all the invariants are specified by you, the human.
*  Yeah.
*  But what I hope is that there is a standard predicate,
*  like probe show.
*  That's what I want to find for digit recognition.
*  If we start, it is completely new area,
*  what is intelligence about on the level,
*  starting from Plata's idea, what is vault of ideas.
*  So, and I believe that it's not too many.
*  Yeah.
*  But you know, it is amusing that mathematician
*  doing something in neural network, in general function,
*  but people from literature, from art,
*  they use this all the time.
*  That's right.
*  Invariants saying, say, it is great how people describe music.
*  We should learn from that.
*  And something on this level, but so why Vladimir Propp,
*  who was just theoretical, who studied theoretical literature,
*  he found that.
*  You know what, let me throw that right back at you,
*  because there's a little bit of a,
*  that's less mathematical and more emotional,
*  philosophical Vladimir Propp.
*  I mean, he wasn't doing math.
*  No.
*  And you just said another emotional statement,
*  which is you believe that this Plato world of ideas is small.
*  I hope.
*  I hope.
*  No.
*  Do you, what's your intuition though,
*  if we can linger on it?
*  You know, it is not just small or big.
*  I know exactly.
*  Then when I introducing some predicate,
*  I decrease set of functions.
*  But my goal to decrease set of function much.
*  By as much as possible.
*  By as much as possible.
*  Good predicate, which does this.
*  Then I should choose next predicate,
*  which does, which decrease set as much as possible.
*  So set of good predicate, it is such that they decrease
*  this amount of admissible function.
*  So if each good predicate significantly reduces
*  the set of admissible functions,
*  that there naturally should not be that many predicates.
*  No, but if you reduce very well the VC dimension
*  of the function of admissible set of function is small.
*  And you need not too much training data to do well.
*  And VC dimension, by the way,
*  is some measure of capacity of this set of functions.
*  Right.
*  Roughly speaking, how many function in this set.
*  So you're decreasing, decreasing,
*  and it makes easy for you to find function you're looking for.
*  So the most important part to create good admissible set
*  of functions, and it probably there are many ways,
*  but the good predicate is such that it can do that.
*  So for this duck, you should know a little bit about duck
*  because what are the three fundamental laws of ducks?
*  Looks like a duck, swims like a duck, and quacks like a duck.
*  You should know something about ducks to be able to.
*  Not necessarily looks like say horse, it's also good.
*  So it's not, it generalizes from ducks.
*  Yes, and talk like, and make sound like horse, something.
*  And run like horse and moves like horse.
*  It is generally, it is generally predicate
*  that this applied to duck, but for duck, you can say,
*  play chess like duck.
*  You cannot say play chess like duck.
*  Why not?
*  You're saying you can, but that would not be a good.
*  No, you will not reduce a lot of function.
*  You will not do, yeah, you would not reduce the set of functions.
*  So you can, the story is formal story, mathematical story.
*  Is that you can use any function you want as a predicate.
*  But some of them are good, some of them are not,
*  because some of them reduce a lot of functions
*  to admissible setter, some of them.
*  But the question is, and I'll probably keep asking this question,
*  but how do we find such, what's your intuition?
*  Handwritten recognition.
*  How do we find the answer to your challenge?
*  Yeah, I understand it like that.
*  I understand what?
*  What defined?
*  What it means, I knew predicate.
*  Like guy who understand music can say this word,
*  which he described when he listened to music.
*  He understand music.
*  He use not too many different, or you can do like prop.
*  You can make collection what he talking about music,
*  about this, about that.
*  It's not too many different situations he described.
*  Because we mentioned Vladimir Prop a bunch, let me just mention.
*  There's a sequence of 31 structural notions that are common in stories.
*  And I think-
*  You call it units.
*  Units, and I think they resonate.
*  I mean, it starts just to give an example,
*  obsession, a member of the hero's community,
*  a family leaves the security of the home environment.
*  Then it goes to the interdiction, a forbidding edict or command
*  is passed upon the hero.
*  Don't go there, don't do this.
*  The hero is warned against some action.
*  Then step three, violation of interdiction.
*  Break the rules, break out on your own.
*  Then reconnaissance, the villain makes an effort to attain knowledge,
*  needing to fulfill their plot, so on.
*  It goes on like this, ends in a wedding.
*  Number 31, happily ever after.
*  He just gave description of all situations.
*  He understands this world.
*  Of folktales?
*  Yeah, not folktales, but stories.
*  And these stories are not just folktales.
*  These stories are in detective serials as well.
*  And probably in our lives, we probably live-
*  Read this.
*  At the end, the role that this predicate is good for different situation.
*  For movie, for theater.
*  By the way, there's also criticism, right?
*  There's another way to interpret narratives from Claude Levi-Strauss.
*  I'm not in this business.
*  No, I know it's theoretical literature, but it's looking at paradise.
*  It's always the discussion.
*  But at least there is a unit.
*  It's not too many units that can describe,
*  but this guy probably gives another unit or another way.
*  Exactly, another set of units.
*  Another set of predicate.
*  It doesn't matter who, but they exist probably.
*  My question is whether given those units,
*  whether without our human brains to interpret these units,
*  they would still hold as much power as they have.
*  Meaning, are those units enough when we give them to the alien species?
*  Let me ask you.
*  Do you understand digit images?
*  No, I don't understand.
*  No, when you can recognize these digit images, it means that you understand.
*  You understand characters.
*  You understand...
*  No, no, no.
*  It's the imitation versus understanding question,
*  because I don't understand the mechanism by which I understand.
*  No, I'm talking about predicate.
*  You understand that it involves symmetry, maybe structure,
*  maybe something, because I cannot formulate.
*  I just was able to find symmetries.
*  So, the degree of symmetries.
*  That's really good.
*  So, this is a good line.
*  I feel like I understand the basic elements
*  of what makes a good hand recognition system my own.
*  Symmetry connects with me.
*  It seems like that's a very powerful predicate.
*  My question is, is there a lot more going on that we're not able to introspect?
*  Maybe I need to be able to understand a huge amount in the world of ideas,
*  thousands of predicates, millions of predicates,
*  in order to do hand recognition.
*  I don't think so.
*  So, both your hope and your intuition are such that...
*  No, let me explain.
*  You're using digits.
*  You're using examples as well.
*  Theory says that if you will use all possible functions from Hilbert space,
*  all possible predicates, you don't need training data.
*  You just will have admissible set of functions which contain one function.
*  Yes.
*  So, the trade-off is when you're not using all predicates,
*  you're only using a few good predicates, you need to have some training data.
*  Yes, exactly.
*  The more good predicates you have, the less training data you need.
*  Exactly.
*  That is intelligent, Lord.
*  Still, okay.
*  I'm going to keep asking the same dumb question,
*  handwritten recognition, to solve the challenge.
*  You kind of propose a challenge that says we should be able to
*  get state-of-the-art MNIST error rates by using very few of the same data.
*  By using very few, 60, maybe fewer examples per digit.
*  What kind of predicates do you think it'll...
*  That is the challenge.
*  So, people who will solve this problem, they will answer.
*  Do you think they'll be able to answer it in a human-explainable way?
*  They just need to write function.
*  That's it.
*  But, so can that function be written, I guess, by an automated reasoning system?
*  Whether we're talking about a neural network learning a particular function
*  or another mechanism?
*  No, I'm not against neural network.
*  I'm against admissible set of functions which create neural network.
*  You did it by hand.
*  You don't do it by invariance, by predicate, by reason.
*  But neural networks can then reverse, do the reverse step of helping you find a function.
*  The task of a neural network is to find a disentangled representation, for example,
*  they call it.
*  To find that one predicate function that really captures some kind of essence.
*  One, not the entire essence, but one very useful essence of this particular visual space.
*  Do you think that's possible?
*  Listen, I'm grasping, hoping there's an automated way to find good predicates.
*  The question is, what are the mechanisms of finding good predicates?
*  You think we should pursue.
*  A young grad student listening right now.
*  I gave an example.
*  So find a situation where predicate, which you're suggesting, don't create invariant.
*  It's like in physics.
*  Find a situation where existing theory cannot explain it.
*  Find a situation where the existing theory cannot explain it.
*  So you're finding contradictions.
*  Find contradiction and then remove this contradiction.
*  But in my case, what means contradiction, you find function,
*  which if you will use this function, you're not keeping invariants.
*  So it's really the process of discovering contradictions.
*  Yeah.
*  It is like in physics.
*  Find a situation where you have contradiction for one of the properties,
*  for one of the predicates.
*  Then include this predicate, making invariants, and solve again this problem.
*  Now you don't have contradiction.
*  But it is not the best way, probably, I don't know, to looking for predicates.
*  That's just one way.
*  Okay.
*  No, no, it is brute force way.
*  The brute force way.
*  What about the ideas of what big umbrella term of symbolic AI.
*  There's what in the 80s with expert systems, sort of logic, reasoning-based systems.
*  Is there hope there to find some, through sort of deductive
*  reasoning, to find good predicates?
*  I don't think so.
*  I think that just logic is not enough.
*  It's kind of a compelling notion though, you know, that when smart people sit in a room
*  and reason through things, it seems compelling and making our machines do the same is also compelling.
*  So everything is very simple.
*  When you have infinite number of predicates, you can choose the function you want.
*  You have invariants and you can choose the function you want.
*  But you have to have not too many, you know, you have to have a lot of
*  invariants.
*  You have to have not too many invariants to solve the problem.
*  So, and how from infinite number of function to select finite number and hopefully small
*  finite number of functions, which is good enough to extract small set of admissible functions.
*  So they will be admissible, it's for sure, because every function just decrease set of
*  function and leaving it admissible.
*  But it will be small.
*  But why do you think logic-based systems don't, can't help?
*  Intuition, not...
*  Because you should know reality.
*  You should know life.
*  This guy like, he knows something and he tried to put invariant his understanding.
*  That's the human.
*  Yeah, but see, you're putting too much value into Vladimir Propp's knowing something.
*  No, it is...
*  I might be misunderstanding.
*  What means you know life?
*  What it means?
*  You know common sense.
*  No, no, you know something.
*  Common sense, it is some rules.
*  You think so?
*  Common sense is simply rules.
*  Common sense is everything, it's mortality, it's fear of death, it's love, it's spirituality,
*  it's happiness and sadness.
*  All of it is tied up into understanding gravity, which is what we think of as common sense.
*  I don't want to discuss so wide.
*  I want to discuss, understand digital recognition.
*  Anytime I bring up love and death, you bring it back to digital recognition.
*  You know, it is durable because there is a challenge which I see how to solve.
*  If I will have a student concentrate on this work, I will suggest something to solve.
*  You mean handwritten recognition?
*  Yeah, it's a beautifully simple, elegant...
*  I think that I know invariants which will solve this.
*  You do?
*  I think so.
*  You think so?
*  But it is not universal.
*  It is maybe...
*  I want some universal invariants which are good not only for digital recognition,
*  for image understanding.
*  So let me ask, how hard do you think is 2D image understanding?
*  So if we can kind of intuit handwritten recognition,
*  how big of a step, leap, journey is it from that?
*  If I gave you good...
*  If I solved your challenge for handwritten recognition,
*  how long would my journey then be from that to understanding more general natural images?
*  Immediately.
*  You will understand this as soon as you will make a record.
*  Because it is not for free.
*  As soon as you will create several invariants which will help you to get the same performance
*  that the best neural net did using 100 times, maybe more than 100 times less examples,
*  you have to have something smart to do that.
*  And you're saying...
*  That it is invariant.
*  It is predicate.
*  Because you should put some idea how to do that.
*  But okay, let me just pause.
*  Maybe it's a trivial point, maybe not.
*  But handwritten recognition feels like a 2D, two-dimensional problem.
*  And it seems like how much complicated is the fact that most images are projection of a
*  three-dimensional world onto a 2D plane.
*  It feels like for a three-dimensional world, we need to start understanding common sense
*  in order to understand an image.
*  It's no longer visual shape and symmetry.
*  It's having to start to understand concepts of...
*  Understand life.
*  Yeah.
*  You're talking that there are different invariants.
*  Different predicate.
*  Yeah.
*  And potentially much larger number.
*  You know, maybe.
*  But let's start from simple.
*  Yeah, but you said that it would be...
*  No, you know, I cannot think...
*  Yeah, I can't.
*  About things which I don't understand.
*  This I understand.
*  But I'm sure that I don't understand everything there.
*  Yeah.
*  That's the difference between...
*  Do as simple as possible, but not simpler.
*  And that is exact case.
*  With handwritten...
*  With handwritten.
*  Yeah, but that's the difference between you and I.
*  I welcome and enjoy thinking about things I completely don't understand.
*  Because to me, it's a natural extension without having solved handwritten recognition.
*  To wonder how difficult is the next step of understanding 2D, 3D images.
*  Because ultimately, while the science of intelligence is fascinating,
*  it's also fascinating to see how that maps to the engineering of intelligence.
*  And recognizing handwritten digits is not...
*  Doesn't help you...
*  It might...
*  It may not help you with the problem of general intelligence.
*  We don't know.
*  It'll help you a little bit.
*  It's unclear.
*  It's unclear.
*  Yeah.
*  It might very much.
*  But I would like to make a remark.
*  I start not from very primitive problem, make a challenge problem.
*  I start with very general problem, with Plato.
*  So you understand...
*  And it comes from Plato to digit recognition.
*  So you basically took Plato and the world, the forms and ideas,
*  and mapped and projected into the clearest, simplest formulation of that big world.
*  You know, I would say that I did not understand Plato
*  until recently.
*  And until I consider the convergence and then predicate and then,
*  oh, this is what Plato told.
*  So...
*  Can you linger on that?
*  Like why...
*  How do you think about this world of ideas and world of things in Plato?
*  No, it is metaphor.
*  It is...
*  It's a metaphor for sure.
*  Yeah.
*  Compelling.
*  It's a poetic and a beautiful metaphor.
*  Yeah, yeah, yeah.
*  But what can you...
*  But it is a way how you should try to understand how to talk ideas in the world.
*  So from my point of view, it is very clear, but it is lying.
*  All the time people looking for that.
*  Say, Plato, then Hegel, whatever reasonable it exists, whatever existed is reasonable.
*  I don't know what he had in mind reasonable.
*  Right.
*  This philosopher's again...
*  No, no, no, no, no, no, no.
*  It is next stop of Wigner that mathematics understand something of reality.
*  It is the same plot align.
*  And then it comes suddenly to Vladimir Propp.
*  Look, 31 ideas, 31 units and this corrects everything.
*  There's abstractions, ideas that represent our world and we should always try to reach into that.
*  Yeah, but you should make projection on reality.
*  But understanding is it is abstract ideas.
*  You have in your mind several abstract ideas which you can apply to reality.
*  And reality in this case, so if you look at machine learning is data.
*  It's example data.
*  Data.
*  Okay, let me put this on you because I'm an emotional creature.
*  I'm not a mathematical creature like you.
*  I find compelling the idea, forget the space, the sea of functions.
*  There's also a sea of data in the world.
*  And I find compelling that there might be, like you said, teacher, small examples of data
*  that are most useful for discovering good, whether it's predicates or good functions,
*  that the selection of data may be a powerful journey, a useful mechanism.
*  Coming up with a mechanism for selecting good data might be useful too.
*  Do you find this idea of finding the right data set interesting at all?
*  Or do you kind of take the data set as a given?
*  I think that it is.
*  You know, my scheme is very simple.
*  You have a huge set of functions.
*  If you will apply and you have not too many data.
*  If you will pick up function which describes this data, you will do not very well.
*  Randomly pick up.
*  Yeah, you will have a fit here.
*  Yeah, it will be overfitting.
*  So you should decrease set of function from which you're picking up one.
*  So you should go somehow to admissible set of function.
*  And this, what about weak conversions?
*  So, but from another point of view, to make admissible set of function,
*  you need just a data, just function which you will take in inner product,
*  which you will measure property of your function.
*  And that is how it works.
*  No, I get it.
*  I get it.
*  I understand it.
*  But do you, the reality is...
*  But let's discuss, let's think about examples.
*  You have huge set of function and you have several examples.
*  If you just trying to keep, take function which satisfies these examples,
*  you still will overfit.
*  You need decrease, you need admissible set of function.
*  Absolutely.
*  But what, say you have more data than functions.
*  So sort of consider the, I mean, maybe not more data than functions because that's...
*  No, it's impossible.
*  Impossible.
*  But what I was trying to be poetic for a second.
*  I mean, you have a huge amount of data, a huge amount of examples.
*  But the amount of function can be even bigger.
*  Bigger, I understand.
*  Everything is...
*  There's always a bigger boat.
*  Full Hilbert space.
*  Gotcha.
*  Okay.
*  But you don't find the world of data to be an interesting optimization space.
*  The optimization should be in the space of functions.
*  Creating admissible set of function.
*  Admissible set of function.
*  No, even from the classical thesis theory, from structural risk minimization,
*  you should organize function in the way that they will be useful for you.
*  Right.
*  And that is admissible set.
*  But the way you're thinking about useful is you're given a small set of examples.
*  Useful small set of function which contain function by looking for.
*  Yeah, but looking for based on the empirical set of small examples.
*  Yeah.
*  But that is another story.
*  I don't touch it.
*  Because I believe that this small examples is not too small.
*  Say 60 per class, that law of large numbers works.
*  I don't need uniform law.
*  The story is that in statistics, there are two laws.
*  Law of large numbers and uniform law of large numbers.
*  So I want to be in a situation where I use law of large numbers,
*  but not uniform law of large numbers.
*  Right. So 60 is large enough.
*  I hope.
*  It still needs some evaluations, some balance.
*  But the idea is the following.
*  That if you trust that, say, this average gives you something close to expectation,
*  so you can talk about that, about this predicate.
*  And that is the basis of human intelligence.
*  Good predicates is the discovery of good predicates is the basis of human intelligence.
*  It is discovery of your understanding of the world.
*  Of your methodology of understanding world.
*  Because you have several functions which you will apply to reality.
*  Can you say that again?
*  You have several functions predicate, but they're abstract.
*  Then you will apply them to reality, to your data,
*  and you will create in this way predicate, which is useful for your task.
*  But predicate are not related specifically to your task, to this year task.
*  It is abstract functions, which being applied to...
*  Many tasks that you might be interested in.
*  It might be many tasks. I don't know.
*  Or...
*  Different tasks.
*  Well, they should be many tasks, right?
*  Yeah, I believe like in prop case.
*  It was for fairy tales, but it's happened everywhere.
*  It's happened everywhere.
*  Okay, so we talked about images a little bit, but...
*  Can we talk about Noam Chomsky for a second?
*  Yeah.
*  I believe I don't know him.
*  Personally, well...
*  Not personally, I don't know his ideas.
*  His ideas.
*  Well, let me just say, do you think language, human language,
*  is essential to expressing ideas as Noam Chomsky?
*  I believe so.
*  Language is at the core of our formation of predicates.
*  It's like human language.
*  For me, language and all the story of language is very complicated.
*  I don't understand this and I'm not...
*  I thought about it.
*  Nobody does.
*  I'm not ready to work on that because it's so huge.
*  It is not for me and I believe not for our century.
*  The 21st century.
*  Not for 21st century.
*  We should learn a lot of stuff from simple tasks like digit recognition.
*  So you think digital recognition, 2D image...
*  How would you more abstractly define digit recognition?
*  It's 2D image symbol recognition, essentially.
*  I mean, I'm trying to get a sense, sort of thinking about it now,
*  having worked with MNIST forever.
*  How small of a subset is this of the general vision recognition problem
*  and the general intelligence problem?
*  Is it...
*  Yeah.
*  Is it a giant subset?
*  Is it not?
*  And how far away is language?
*  You know, let me refer to Einstein.
*  Take the simplest problem as simple as possible, but not simpler.
*  And this challenge is simple problem.
*  But it's simple by idea, but not simple to get it.
*  When you will do this, you will find some predicate which helps it.
*  Well, yeah, I mean, with Einstein, you look at general relativity,
*  but that doesn't help you with quantum mechanics.
*  Only that's another story.
*  You don't have any universal instrument.
*  Yes.
*  So I'm trying to wonder which space we're in,
*  whether handwritten recognition is like general relativity,
*  and then language is like quantum mechanics.
*  You're still going to have to do a lot of mess to universalize it,
*  but I'm trying to see...
*  What's your intuition why handwritten recognition is easier than language?
*  Just, I think a lot of people would agree with that,
*  but if you could elucidate the intuition of why.
*  I don't know.
*  No, I don't think in this direction.
*  I just think in the direction that this is problem,
*  which if we will solve it well,
*  we will create some abstract understanding of images.
*  Maybe not all images.
*  I would like to talk to guys who are doing unreal images in Columbia University.
*  What kind of images?
*  Unreal?
*  Real images.
*  What's their idea?
*  Is there a predicate?
*  What can be predicated?
*  I still, symmetry will play a role in real life images,
*  in any real life images, 2D images.
*  Let's talk about 2D images.
*  Because that's what we know.
*  Neural network was created for 2D images.
*  The people I know in vision science, for example, the people who study human vision,
*  that they usually go to the world of symbols and handwritten recognition,
*  but not really.
*  It's other kinds of symbols to study our visual perception system.
*  As far as I know, not much predicate type of thinking is understood about our vision system.
*  They did not think in this direction.
*  They don't.
*  Yeah.
*  How do you even begin to think in that direction?
*  I would like to discuss with them.
*  Because if we will be able to show that it is what's working,
*  and theoretical scheme is not so bad.
*  So if we compare to language, language has like letters,
*  a finite set of letters and a finite set of ways you can put together those letters.
*  So it feels more amenable to kind of analysis.
*  With natural images, there is so many pixels.
*  No, no, no.
*  Letter, language is much, much more complicated.
*  It involves a lot of different stuff.
*  It's not just understanding of very simple class of tasks.
*  I would like to see lists of tasks where language involved.
*  Yes.
*  So there's a lot of nice benchmarks now in natural language processing from the very trivial,
*  like understanding the elements of a sentence to question answering,
*  to much more complicated where you talk about open domain dialogue.
*  The natural question is with handwritten recognition,
*  it's really the first step of understanding visual information.
*  Right.
*  But even our records show that we go in the wrong direction.
*  Because we need 60,000 digits.
*  So even this first step, so forget about talking about the full journey.
*  This first step should be taking in the right direction.
*  No, no, wrong direction because 60,000 is unacceptable.
*  No, I'm saying it should be taken in the right direction because 60,000 is not acceptable.
*  You can talk, it's great we have half percent of error.
*  And hopefully the step from doing hand recognition using very few examples,
*  the step towards what babies do when they crawl and understand their physical environment.
*  I don't know what baby does.
*  I know you don't know about babies.
*  If you will do from very small examples, you will find principles.
*  That will apply to babies.
*  From what we're using now.
*  And theoretically it's more or less clear.
*  That means that you will use weak convergence, not just strong convergence.
*  Do you think these principles will naturally be human interpretable?
*  Oh, yeah.
*  So like when we will be able to explain them and have a nice presentation to show what those
*  principles are or are they going to be very kind of abstract kinds of functions?
*  For example, I talked yesterday about symmetry.
*  Yes.
*  And they gave very simple examples.
*  The same will be like that.
*  You gave like a predicate of a basic for?
*  For symmetries.
*  Yes, for different symmetries and you have for?
*  Degree of symmetry.
*  Degree of symmetry.
*  That is important.
*  Not just symmetry.
*  Exist and doesn't exist.
*  Degree of symmetry.
*  Yeah, for handwritten recognition.
*  No, it's not for handwritten.
*  It's for any images.
*  But I would like to apply to handwritten.
*  Right.
*  It's in theory it's more general.
*  Okay.
*  Okay.
*  So a lot of things we've been talking about falls.
*  We've been talking about philosophy a little bit, but also about mathematics and statistics.
*  A lot of it falls into this idea, a universal idea of statistical theory of learning.
*  What is the most beautiful and sort of powerful or essential idea you've come across,
*  even just for yourself personally in the world of statistics or a statistic theory of learning?
*  Probably uniform convergence, which we did.
*  This is Alexey Chedvoninkis.
*  Can you describe universal convergence?
*  You have law of large numbers.
*  So for any function, expectation of function, average of function converged to expectation.
*  But if you have set of functions, for any function it is true.
*  But it should converge simultaneously for all set of functions.
*  And for learning, you need uniform convergence.
*  Just convergence is not enough.
*  Because when you pick up one which gives minimum, you can pick up one function which does not
*  converge and it will give you the best answer.
*  The best answer for this function.
*  So you need uniform convergence to guarantee learning.
*  So learning does not rely on trivial law of large numbers, it relies on universal law.
*  But idea of the convergence exists in statistics for a long time.
*  But it is interesting that as I think about myself, how stupid I was 50 years,
*  I did not see weak convergence.
*  I work only on strong convergence.
*  But now I think that most powerful is weak convergence because it makes admissible set
*  of functions.
*  And even in all proverbs, when people try to understand recognition about dog law,
*  looks like a dog and so on, they use weak convergence.
*  People in language, they understand this.
*  But when we're trying to create artificial intelligence, we are trying to create
*  intelligence.
*  We want them in a different way.
*  We just consider strong convergence.
*  So reducing the set of admissible functions, do you think there should be
*  effort put into understanding the properties of weak convergence?
*  You know, in classical mathematics, in Gilbert space, there are only two ways
*  to form of convergence, strong and weak.
*  Now we can use both.
*  That means that we did everything.
*  And it so happened that when we use Gilbert space, which is very rich space,
*  space of continuous functions, which has an integral square.
*  So we can apply weak and strong convergence for learning and have closed form solution.
*  So for computationally simple.
*  For me, it is sign that it is right way because you don't need any heuristic.
*  You just do whatever you want.
*  But now the only what left, it is concept of what is predicate.
*  That's predicate.
*  But it is not statistics.
*  By the way, I like the fact that you think the heuristics are a mess that should be
*  removed from the system.
*  So closed form solution is the ultimate.
*  No, it so happened.
*  Then when you're using right instrument, you have closed form solution.
*  Do you think intelligence, human level intelligence, when we create it?
*  Will have something like a closed form solution?
*  You know, I know I'm looking on bounds, which I gave bounds for convergence.
*  And when I looking for bounds, I thinking what is the most appropriate kernel
*  for this bound would be.
*  So we know that in say, all our businesses, we use radial basis function.
*  But looking on the bound, I think that I start to understand that maybe we need to make
*  corrections to radial basis function to be closer to work better for this bounds.
*  So I'm again trying to understand what type of kernel have best approximation,
*  no, no, approximation, best fit to this bound.
*  Sure.
*  So there's a lot of interesting work that could be done in discovering better function
*  and radial basis functions for kind of bounds.
*  But it still comes from you're looking to mass and trying to understand.
*  From your own mind, looking at the, I don't know.
*  Then I trying to understand what will be good for that.
*  Yeah, but to me, there's still a beauty.
*  Again, maybe I'm a descendant of valentoring to heuristics.
*  To me, ultimately, intelligence will be a mess of heuristics.
*  And that's the engineering answer, I guess.
*  Absolutely.
*  When you're doing say self-driving cars, the great guy who will do that,
*  it does not matter what theory behind that.
*  Who has a better feeling have to apply it.
*  But by the way, it is the same story about predicates,
*  because you cannot create rule for situation is much more than you have rule for that.
*  But maybe you can have more abstract rule than it will be less this rule.
*  It is the same story about ideas and ideas applied to specific cases.
*  But still you should reach.
*  You cannot avoid this.
*  Yes, of course.
*  But you should still reach for the ideas to understand the science.
*  Let me kind of ask, do you think neural networks or functions can be made to reason?
*  Sort of what do you think?
*  We've been talking about intelligence, but this idea of reasoning, there's an element of
*  sequentially disassembling, interpreting the images.
*  When you think of handwritten recognition,
*  we kind of think that there will be a single input and output.
*  There's not a recurrence.
*  What do you think about the idea of recurrence, of going back to memory and thinking through this
*  sort of sequentially mangling the different representations over and over until you arrive
*  at a conclusion?
*  Or is ultimately all that can be wrapped up into a function?
*  You're suggesting that let us use this type of algorithm.
*  When I started thinking, I first of all started to understand what I want.
*  Can I write down what I want?
*  And then I try to formalize.
*  And when I do that, I think I have to solve this problem.
*  Until now, I did not see a situation where recurrence.
*  You need recurrence.
*  But do you observe human beings?
*  Yeah.
*  It's the imitation question, right?
*  It seems that human beings reason, they are not the reason for the situation.
*  They are the reason for the situation.
*  Do you try to?
*  It's the imitation question, right?
*  It seems that human beings reason this kind of sequentially.
*  Does that inspire in you a thought that we need to add that into our intelligent systems?
*  You're saying, okay, you've kind of answered saying until now, I haven't seen a need for it.
*  And so because of that, you don't see a reason to think about it.
*  You know, most of the things I don't understand in reasoning in human.
*  It is for me too complicated.
*  For me, the most difficult part is to ask questions, good questions, how it works, how people ask it.
*  I don't know.
*  You said that machine learning is not only about technical things, speaking of questions, but it's also about philosophy.
*  So what role does philosophy play in machine learning?
*  We talked about Plato, but generally thinking in this philosophical way,
*  How does philosophy and math fit together in your mind?
*  First ideas and then their implementation.
*  It's like predicate, like say admissible set of functions.
*  It comes together, everything.
*  Because the first iteration of theory was done 50 years ago, I told that this is theory.
*  So everything's there.
*  If you have data and your set of function has not big capacity, so low VC dimension, you can do that.
*  You can make structural risk minimization, control capacity.
*  But you was not able to make admissible set of function, God.
*  Now, when suddenly realize that we did not use another idea of convergence, which we can.
*  Everything comes together.
*  But those are mathematical notions.
*  Philosophy plays a role of simply saying that we should be swimming in the space of ideas.
*  Let's talk what is philosophy.
*  Philosophy means understanding of life.
*  So understanding of life, say people like Plato, they understand a very high abstract level of life.
*  So, and whatever I doing, it's just implementation of my understanding of life.
*  But every new step, it is very difficult.
*  For example, to find the idea that we need weak convergence was not simple.
*  For me.
*  So that required thinking about life a little bit.
*  Hard to trace, but there was some thought process.
*  You know, I've worked and I've been thinking about the same problem for 50 years somehow.
*  And again and again and again.
*  I trying to be honest and that is very important.
*  I was very enthusiastic, but concentrated on whatever we was not able to achieve.
*  And understand why.
*  And now I understand that because I believe in math, I believe that in Wigner-Sadiya.
*  But now when I see that there are only two ways of convergence.
*  And we're using both.
*  That means that we must do as well as people doing.
*  But now exactly in philosophy and what we know about predicate, how we understand life, can we describe as a predicate.
*  I thought about that.
*  And that is more or less obvious level of symmetry.
*  But next I have a feeling it's something about structures.
*  But I don't know how to formulate, how to measure measure of structure and all this stuff.
*  And guy who will solve this challenge problem.
*  Then when we were looking how he did it.
*  Probably just only symmetry is not enough.
*  But something like symmetry will be there.
*  Absolutely symmetry will be there.
*  Level of symmetry will be there.
*  And level of symmetry, anti-symmetry, diagonal, vertical.
*  I even don't know how you can use in different direction of symmetry.
*  But it will be there.
*  I think that people very sensitive to idea of symmetry.
*  But there are several ideas like symmetry.
*  That's I would like to learn.
*  But you cannot learn just thinking about that.
*  You should do challenging problems and then analyze them.
*  Why it was able to solve them.
*  And then you will see.
*  Very simple things it's not easy to find.
*  Even we're talking about this every time.
*  I was surprised.
*  I tried to understand.
*  If people describe in language strong convergence mechanism for learning.
*  I did not see.
*  I don't know.
*  It's a dark story.
*  And story like that when you will explain.
*  You will use weak convergence argument.
*  It looks like it does like this.
*  But when you try to formalize.
*  You're just ignoring this.
*  Why?
*  Why 50 years from start of machine learning?
*  And that's the role of philosophy.
*  I think that maybe.
*  I don't know.
*  Maybe this is theory also.
*  We should blame for that.
*  Because empirical risk minimization.
*  And all this stuff.
*  If you read now textbooks.
*  They just about bound about empirical risk minimization.
*  They don't looking for another problem like admissible set.
*  But on the topic of life.
*  Perhaps we you could talk in Russian for a little bit.
*  What's your favorite memory from childhood?
*  What's your favorite memory from childhood?
*  Music.
*  Can you try to answer in Russian?
*  Music.
*  It was very cool when.
*  What kind of music?
*  Classic music.
*  What's your favorite?
*  Different composers.
*  At first it was Vivaldi.
*  I was surprised.
*  That it's possible.
*  And then I understood Bach.
*  I was completely shocked.
*  By the way.
*  I think that there is a predicate.
*  Like structure.
*  In Bach.
*  Because you can feel the structure.
*  And I don't think that different elements of life are very divided.
*  In the sense of predicate.
*  Structure in painting.
*  Structure in human relations.
*  How to find these high levels of predicate?
*  In Bach and in life.
*  Everything is connected.
*  Now that we're talking about Bach.
*  Let's switch back to English.
*  Because I like Beethoven and Chopin.
*  Chopin is another amusing story.
*  But Bach.
*  If we talk about predicate.
*  Bach probably has the most well defined predicate.
*  It is very interesting to read.
*  What is Bach?
*  It is very interesting to read.
*  What critics are writing about Bach?
*  Which words they're using?
*  They're trying to describe predicate.
*  And then Chopin.
*  It is very different vocabulary.
*  Very different predicate.
*  And I think that.
*  If you will make collection of that.
*  So maybe from this you can describe predicate for digital recognition.
*  From Bach and Chopin.
*  No, no, no.
*  Not from Bach and Chopin.
*  From the critic interpretation of the music.
*  They're trying to explain to you music.
*  What they use.
*  They describe high level ideas.
*  Of Plato's ideas.
*  What's behind this music.
*  So art is not self explanatory in some sense.
*  So you have to try to convert it into ideas.
*  It is ill post problems.
*  When you go from ideas to the representation.
*  It is an easy way.
*  But when you're trying to go Bach.
*  It is ill post problems.
*  But nevertheless.
*  I believe that when you're looking from that.
*  Even from art.
*  You will be able to find predicate for digital recognition.
*  That's such a fascinating and powerful notion.
*  Do you ponder your own mortality?
*  Do you think about it?
*  Do you fear it?
*  Do you draw insight from it?
*  About mortality.
*  Oh yeah.
*  Are you afraid of death?
*  Not too much.
*  Not too much.
*  It is pity that I will not be able to do something.
*  Which I think I have a feeling to do.
*  For example.
*  I will be very happy.
*  To work with guys.
*  Theoreticians from music.
*  To write this collection of description.
*  How they describe music.
*  How they use it.
*  And from art as well.
*  Then take what is in common.
*  And try to understand predicate.
*  Which is absolute for everything.
*  And then use that for visual recognition.
*  See if there is a connection.
*  Exactly.
*  There's still time.
*  We've got time.
*  We've got time.
*  It takes years and years and years.
*  You think so?
*  It's a long way.
*  You've got the patient mathematician's mind.
*  I think it could be done very quickly.
*  And very beautifully.
*  I think it's a really elegant idea.
*  Yeah.
*  You know the most time.
*  It is not to make this collection.
*  To understand.
*  What is the common to think about that.
*  Once again and again and again.
*  Again and again and again.
*  But I think sometimes.
*  Especially when you say this idea now.
*  Even just putting together the collection.
*  And looking at the different sets of data.
*  Language.
*  Trying to interpret music.
*  Criticize music.
*  And images.
*  I think there will be sparks of ideas that will come.
*  Of course.
*  Again and again you'll come up with better ideas.
*  But even just that notion.
*  Is a beautiful notion.
*  I even have some examples.
*  So I think it's a very elegant idea.
*  So I have a friend.
*  Who was.
*  Specialist in Russian poetry.
*  She is a professor of Russian poetry.
*  He did not write poems.
*  But she knows a lot of stuff.
*  She makes a book.
*  Several books.
*  And one of them is.
*  And she is a very good poet.
*  She is a very good poet.
*  She is a very good poet.
*  She is a very good poet.
*  She is a very good poet.
*  She is a collection of Russian poetry.
*  She is a collection of Russian poetry.
*  She has images of Russian poetry.
*  She collects all images of Russian poetry.
*  And I ask you.
*  To do the following.
*  You have NIPs.
*  Digit recognition.
*  And you get 100 digits.
*  Or maybe less than 100.
*  I don't remember.
*  Maybe 50 digits.
*  And 30.
*  And you get 100 digits.
*  And try from a poetical point of view.
*  Describe every image.
*  Which she sees.
*  Using only words.
*  Of images of Russian poetry.
*  And she did it.
*  And then.
*  You try to.
*  I call it learning using privileged information.
*  I call it privileged information.
*  You have on two languages.
*  You have on two languages.
*  You have on two languages.
*  You have on two languages.
*  One language is just.
*  Image of digit.
*  And another language is a poetic description of this image.
*  And another language is a poetic description of this image.
*  And this is privileged information.
*  And this is privileged information.
*  And there is an algorithm.
*  When you are working using privileged information.
*  You are doing better.
*  Much better.
*  So there is something there.
*  Something there.
*  And there is.
*  In NEC.
*  In NEC.
*  She unfortunately died.
*  The collection.
*  Of digits.
*  In poetic descriptions of these digits.
*  In poetic descriptions of these digits.
*  So there is something there.
*  In that poetic description.
*  But I think that.
*  There is an abstract idea.
*  On the plateau level of ideas.
*  Yeah.
*  That they are there.
*  That could be discovered.
*  But as soon as we start.
*  With this challenge problem.
*  The challenge problem.
*  It immediately connected to all this stuff.
*  It immediately connected to all this stuff.
*  Especially with your talk.
*  And this podcast.
*  And I'll do whatever I can to advertise it.
*  Such a clean beautiful Einstein like formulation.
*  Of the challenge before us.
*  Right.
*  Let me ask another absurd question.
*  Let me ask another absurd question.
*  We talked about mortality.
*  We talked about philosophy of life.
*  What do you think is the meaning of life?
*  What's the predicate?
*  What's the predicate?
*  For mysterious existence here on earth.
*  For mysterious existence here on earth.
*  I don't know.
*  It's very interesting.
*  It's very interesting.
*  We have.
*  In Russia.
*  I don't know.
*  There is a guy.
*  Strugatsky.
*  They are writing.
*  They are thinking about.
*  What's going on.
*  And they have a idea.
*  And they have a idea.
*  That there are.
*  That there are.
*  That there are.
*  Two types of people.
*  Common people.
*  And very smart people.
*  They just started.
*  And very smart people.
*  Will go in different direction very soon.
*  So that's what they are thinking about.
*  So that's what they are thinking about.
*  So the purpose of life is to create
*  So the purpose of life is to create
*  Two paths.
*  Two paths.
*  Of human societies.
*  Yes.
*  Simple people and more complicated people.
*  Which do you like best?
*  The simple people or the complicated ones?
*  I don't know.
*  It's just fantasy.
*  But you know every week we have a guy.
*  Who is.
*  Just.
*  Writer.
*  And also.
*  Theoretical of literature.
*  And he explains.
*  How he understands.
*  Literature and human relationship.
*  How he sees life.
*  How he sees life.
*  And I understood that.
*  I'm just small kids.
*  Comparing to him.
*  He is very smart guy.
*  In understanding life.
*  He knows this predicate.
*  He knows.
*  Big blocks of life.
*  I amused every time.
*  When I listen to him.
*  And he just talking about literature.
*  And I think that.
*  I was.
*  Surprised.
*  Surprised.
*  So the.
*  Managers.
*  In big companies.
*  Most of them.
*  Are.
*  Guys who study.
*  English language.
*  And English literature.
*  So why?
*  Because they understand life.
*  They understand models.
*  And among them.
*  Maybe many.
*  Talented critics.
*  And they understand.
*  Critics.
*  Just analyzing this.
*  And this is big science.
*  Like.
*  Propdite.
*  This is blocks.
*  They are very smart.
*  It amazes me that you are.
*  And continue to be humbled.
*  By the brilliance of others.
*  I am very modest about myself.
*  I see.
*  So smart guys around.
*  I am very modest for you.
*  You are one of the greatest.
*  Mathematicians.
*  It is truly an honor.
*  Thank you for talking.
*  Let's talk.
*  It is not.
*  I know my limits.
*  Let's talk again.
*  When your challenge is taken on.
*  And solved by grad students.
*  Especially.
*  When.
*  Maybe music will be involved.
*  Thank you so much.
*  Thank you very much.
*  Thank you for listening.
*  I hope to see you next time.

---
Date Generated: June 10, 2024
Transcription Model: whisper medium 20231117
Length: 4938s
Video Keywords: ['artificial', 'intelligence', 'computers', 'ai', 'deep', 'learning']
Video Views: 24237
Video Rating: None
Video Description: Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2019/10/14/68-melanie-mitchell-on-artificial-intelligence-and-the-challenge-of-common-sense/

Patreon: https://www.patreon.com/seanmcarroll

Artificial intelligence is better than humans at playing chess or go, but still has trouble holding a conversation or driving a car. A simple way to think about the discrepancy is through the lens of “common sense” — there are features of the world, from the fact that tables are solid to the prediction that a tree won’t walk across the street, that humans take for granted but that machines have difficulty learning. Melanie Mitchell is a computer scientist and complexity researcher who has written a new book about the prospects of modern AI. We talk about deep learning and other AI strategies, why they currently fall short at equipping computers with a functional “folk physics” understanding of the world, and how we might move forward.

Melanie Mitchell received her Ph.D. in computer science from the University of Michigan. She is currently a professor of computer science at Portland State University and an external professor at the Santa Fe Institute. Her research focuses on genetic algorithms, cellular automata, and analogical reasoning. She is the author of An Introduction to Genetic Algorithms, Complexity: A Guided Tour, and most recently Artificial Intelligence: A Guide for Thinking Humans. She originated the Santa Fe Institute’s Complexity Explorer project, on online learning resource for complex systems.
---

# Mindscape 68 | Melanie Mitchell on Artificial Intelligence and the Challenge of Common Sense
**Mindscape Podcast:** [October 14, 2019](https://www.youtube.com/watch?v=F9Il2Q0mCDI)
*  Hello everyone and welcome to the Mindscape podcast. I'm your host, Sean Carroll.
*  We all know that artificial intelligence is an important thing. We've talked about it here on Mindscape.
*  I'm sure we're going to keep talking about it down the road. We also know that it faces some obstacles.
*  I don't mean the kind of ethical obstacles we talked about before, you know, what should your self-driving car do?
*  I mean obstacles in creating what would truly be considered a human-level artificial intelligence.
*  There are certain things that computers, that AIs, are really, really good at, way better than any human being,
*  and there's certain other things they still fall short at.
*  And those things that artificial intelligence is not very good at can be lumped under the general heading of common sense.
*  There are aspects of the world that seem completely obvious and intuitive to every human being from a very young age.
*  And yet not only do computers not know them automatically, we even have trouble teaching them to computers.
*  So today's guest is Melanie Mitchell, a computer scientist and complexity theorist at Portland State University and the Santa Fe Institute.
*  She's the author of several books that I really like, and her new book is called Artificial Intelligence, A Guide for Thinking Humans.
*  And it doesn't pretend to give the once and for all solution to this problem, but it lays out exactly this issue
*  of how artificial intelligence works and why common sense, as important and as basic as it is,
*  is one of the most difficult things to teach to a computer.
*  We also talk about what the ramifications of this difficulty are for what AI is, where it's going,
*  how it will be good and bad as we move into the future. So let's go.
*  Melanie Mitchell, thanks for being on the Mindscape Podcast.
*  Oh, I'm glad to be here.
*  So you have an advantage over other people who write popular books about artificial intelligence,
*  I think, which is that Douglas Hofstadter was your PhD thesis advisor.
*  That's right.
*  So that not only is awesome because, you know, he's done a lot of influential things, most obviously author of Gertl Escher Bach,
*  which probably, like you, got a lot of people interested in this subject matter.
*  But he continues to be a thoughtful and eloquent person thinking about these issues.
*  And so you tell this wonderful story of a visit to Google with Hofstadter early on in the book.
*  Why don't we start off by setting the stage with that kind of anecdote?
*  Right. So maybe five years ago, some of the AI people at Google invited Douglas Hofstadter,
*  who is a very well-known writer about AI, thinker, researcher.
*  They invited him to come and meet with them to talk about AI and thinking about how to push forward in AI.
*  But he and I was living on the West Coast in Portland and the meeting was in Mountain View.
*  So he asked me if I wanted to come. And I absolutely did.
*  So we all showed up there and got to the Google building and found our way to the conference room.
*  And Doug got up to speak and he basically started telling the Google engineers about how terrified he was about AI,
*  how much he hated AI, how much he feared it, how much he loathed it.
*  He was extremely passionate. And they were just sitting there, mouths agape.
*  Not what they expected to hear.
*  Thinking, what the heck is going on?
*  You know, so and they kind of quizzed him.
*  And, you know, he was he would he his fear is a little bit complicated.
*  It's not sort of just that AI is going to take over.
*  Right. That's the traditional fear that we hear about.
*  So he has a slightly subtle, more different fear.
*  His fear was more that in some sense, all the things that he found the most profound and close to his heart about human intelligence,
*  and he's been thinking about it for decades and decades, extremely carefully and thoroughly.
*  He is worried that these things will in some sense be too easy to automate,
*  that AI with its what he thinks of as cheap tricks will succeed in creating a person with the profundity of,
*  you know, one of his heroes like Chopin or Gödel or Bach or whoever.
*  Right. And that that would just horrify him that the human soul,
*  if you will, would be so easy to capture in a cheap machine.
*  And is it is the horror in the cheapness?
*  Like if it were hard to do, but we could still do it in a computer, would he be less horrified?
*  I think we're just tricking ourselves.
*  Right. So, you know, I it's hard to speak for him.
*  But my impression is that he the harder it is, the better.
*  Right. And so we want to learn that human creativity is somehow extremely hard and profound.
*  Right. So he used you know, he extensively talks about Chopin.
*  That's one of his favorite composers and feels one of the most profound sort of humans,
*  whoever lived. And he he fears that something like Chopin's music could be created by an AI program
*  that just used a lot of superficial heuristics and, you know, cheap tricks as he calls them.
*  Some random numbers match some patterns. Yeah.
*  And then you have the genius of Chopin.
*  Right. And that would just be the worst thing in the world to him.
*  Well, and there was an example, right?
*  There was a computer program that tried to mimic Chopin.
*  Right. And did too good a job.
*  So there is a program written by a composer named David Cope, who is also a programmer
*  who wrote this program called Experiments in Musical Intelligence or EMI.
*  EMI used a lot of AI techniques and sort of very relatively simple statistics,
*  statistical pattern matching techniques.
*  And it did a pretty good job of with lots of data to go on of composing in the style of various composers,
*  including Chopin. And Doug even tried to play one of these pieces for a group at the Eastman School of Music.
*  A bunch of music theorists and composers themselves.
*  And they were fooled. They didn't know which piece was by the real Chopin and which piece was by EMI.
*  So that just terrified him.
*  Yeah. And then the Google engineers at this meeting were very certain that human level
*  AI of the kind Doug was fearing was imminent in some way was at least we were getting much closer to it
*  with deep learning and all the data driven approaches of today.
*  And I was just very confused about this whole meeting that Doug Hofstadter was so terrified.
*  The Google engineers were so glib about the idea that we were going to have human level intelligence,
*  which I find to be very unlikely.
*  So I decided this would be kind of gave me the idea of trying to learn a lot more about AI.
*  I work in my own narrow area, but to learn more about it as a whole and to say like,
*  what is the state of AI? You know, we read stuff in the media that just seems to me to be outrageous hype.
*  And some people think that we're very close to human level AI.
*  Some people think we're extremely far away. What is the real state of AI?
*  So that's kind of the topic of my book.
*  I was sparked by this meeting at Google and by Doug's terror, which surprised me.
*  And you don't share the terror or the optimism really.
*  That's right. I don't share either.
*  And the book is kind of an exposition of what I found where AI is today.
*  Sort of what then we have to ask, what do we mean by human level intelligence?
*  And that's ill defined. We don't understand intelligence.
*  We don't understand the brain.
*  We don't understand the mind if there are two separate things.
*  And I think that AI is now in a state where people just don't agree.
*  There's a huge amount of disagreement in the field.
*  Well, I've noticed this. And, you know, there are people who are not professional AI researchers,
*  but are famous public intellectuals, Stephen Hawking, Elon Musk, Phil Gates, people like that,
*  who warn against AI coming in the future and being super intelligent and taking over.
*  And they get a lot of pushback from people who spend their lives doing AI.
*  But I don't find the pushback especially convincing because you can be so immersed in the day to day difficulties
*  that you miss the possibility of something big going on.
*  So that's what you're trying to sort of step back and ask about in the book.
*  Exactly. Yeah. And what's interesting about AI, which might be different from your field, I don't know,
*  but everybody has an opinion about it.
*  Everybody has a quote unquote informed opinion about it.
*  Everybody thinks they know what intelligence is and how hard it is for AI to get it.
*  And we get a lot of people who are not in the field who have never worked in this area
*  opining with great confidence about the future, which is very strange.
*  And I think most, as you say, most people who are kind of on the ground working day to day
*  don't agree with a lot of these more over the top predictions.
*  But if you take someone like Ray Kurzweil, OK, who is the sort of promotes the idea of the singularity
*  where he thinks that AI is going to become at the level of humans within the next 10 years
*  and then a billion times more intelligent than humans within 20 years or 30 years or something.
*  He would say, well, if you're sitting on an exponential curve, and that's his idea that progress in AI
*  is on an exponential curve, if you're sitting in the middle of an exponential curve,
*  it doesn't look exponential to you, but it's about to get very, very steep.
*  And, you know, the nice thing about sitting on curves that don't look exponential is some of them
*  might not be exponential. Exactly.
*  But he has books full of exponential curves that try and make the argument that we are on an exponential curve.
*  And, you know, to people out in the world, it kind of feels that way because there is so much progress
*  that's been reported recently.
*  It does feel like there's been exponential progress.
*  And my book tries to look at that progress and ask sort of how much progress has actually been made.
*  Yeah. And I think that, you know, well, just parenthetically, I think there are almost no exponential curves in nature.
*  Really exponential, right? The expansion of the universe is one of them.
*  But most curves look exponential at the beginning and then flatten off or decay away.
*  So I don't think that the curve fitting tells us very much.
*  Therefore, let's dig into some of the details.
*  This is what your book does really, really well.
*  Let's open up the hood a little bit and think about artificial intelligence.
*  You mentioned all of the advances that people have seen recently.
*  We can talk to Siri and so forth.
*  It almost is like talking to a human.
*  And this is based on this is almost all based on deep learning and neural networks.
*  Is that a fair thing to say? Yes, absolutely.
*  So deep learning and deep neural networks, which the definition of which is just neural networks with more than two layers.
*  Oh, OK. I was wondering what the definition was because I've seen them used interchangeably.
*  Yeah. So typically a neural network has inputs and then what it has what's called a hidden layer or an internal layer.
*  And then it has an output layer.
*  Those are sort of the traditional neural networks from, say, the 1990s that people use.
*  So a deep network is a network with more than two hidden layers.
*  That's very deep. OK.
*  And the word deep should not be confused with the words deep, sort of in like thinking or profound or, you know.
*  But it's a very good word because it sounds very deep to people.
*  But in any case, deep neural networks have with a lot of data, you know, big data to train them and very fast parallel computers to run them, have had a huge amount of success in some pretty narrow areas.
*  Some of those areas are very useful.
*  So like Siri speech recognition, being able to transcribe our speech.
*  That's been an amazingly successful sort of breakthrough due to deep learning.
*  Object recognition to some extent has also become really successful and useful or face recognition.
*  Other kinds of computer vision have become very successful due to deep learning.
*  But more and more people are sort of beginning to see some of the limitations.
*  So if you will, we'll get to the limitations. But actually, I want to.
*  But first, let's let's build our way up.
*  What I should have said is tell me about the perceptron.
*  This is a wonderful little thing you talked about that led us eventually to neural networks.
*  Right. So the perceptron was maybe the great, great grandparent of today's deep neural networks that was created in the 1950s by a psychologist named Frank Rosenblatt.
*  He was looking at simple models of neurons.
*  You know, people have been making sort of computer models of neurons ever since computers existed.
*  That was one of the first things that people started to do.
*  And in that view, a neuron was a very simple device that, you know, has gets input.
*  If the input is reaches some threshold, internal threshold, then the neuron fires.
*  So we knew enough about neurons in the 1950s for him to be inspired by this to do a computer version.
*  Exactly. Exactly. They were linear threshold devices, they say.
*  And he found that if you create perceptrons, if you can, he created them in hardware.
*  So you see these pictures of the perceptron that he created with these like spaghetti masses of wires coming out.
*  And there's these giant mainframe looking computers.
*  I forget where the would transistors have been around by then or was it vacuum tubes in his perceptron?
*  Oh, that's a good question.
*  It was about that time, I think.
*  So, but they were large.
*  And they could do some things.
*  And the thing about perceptrons that was so remarkable was that they could learn.
*  They were one of the first systems based on sort of the brain that could do some learning.
*  And he developed an algorithm that allowed perceptrons to learn from examples.
*  But it was really like one neuron was learning.
*  Yeah, essentially, or some like network of simple, some simple network.
*  Okay, so there were some simple networks.
*  Yeah, there were some simple networks.
*  And they would learn and they could learn to do things like recognize handwritten characters to some extent, not very well, not as well as humans.
*  But Rosenblatt made a lot of promises, as people in AI tend to do.
*  It helps to get funding.
*  And he made a lot of promises for what perceptrons would be able to do in the future.
*  And all of that was sort of stomped upon by Marvin Minsky and Seymour Papert in around 1970
*  when they did a mathematical study of perceptrons and showed that perceptrons were actually very limited in principle in what they could learn.
*  Even if you have as much data as you want to train them, they still cannot learn a lot of things that we want them to do.
*  Let's pause to talk about the Great Courses Plus.
*  I know that if you're a Mindscape listener, you like learning new things, especially in an audio convenient format.
*  The Great Courses Plus is a streaming application that lets you take college level courses from the Great Courses.
*  It can be anything from science to philosophy to history to music.
*  And the Great Courses Plus app makes it easy to watch or listen anytime, anywhere and whatever device you prefer.
*  I've done several courses with the Great Courses.
*  They're all available on the Great Courses Plus.
*  For example, I did a course on the Higgs boson and beyond, where you can learn about the Large Hadron Collider, the Higgs boson,
*  quantum field theory, gauge theory, and the search for the finishing pieces of the standard model of particle physics.
*  So you can expand your mind by signing up for the Great Courses Plus.
*  And right now, Mindscape listeners get an entire month for free.
*  To start your free month, sign up today using the special URL, thegreatcoursesplus.com slash mindscape.
*  That's T-H-E Great Courses P-L-U-S dot com slash mindscape.
*  And the idea, just to make this absolutely clear to the audience,
*  the idea was that just like a real neuron, there are inputs from the equivalent of dendrites, right?
*  So there's some wires going into the perceptron that say, this pixel is lit up this much, this pixel lit up that much.
*  And then some black magic happens inside the perceptron and it just says yes or no.
*  That's the output. Yes, this is what I'm looking for. No, this is not.
*  That's right.
*  And what was the difference then between that and a neural network?
*  So two things. One is that perceptrons had no hidden layer.
*  Now, hidden layer, the word hidden is a little strange here, but this is what people call it in the field.
*  It just means that there's a layer of neurons between the inputs that where information propagates from the inputs to the hidden layer to the outputs.
*  And the hidden layer is able to somehow create some kind of internal representation of the input.
*  So if it's a handwritten character, you know, if you're showing it, the input is just say all the pixels.
*  They're either black or white.
*  Well, that the hidden layer might be able to learn to represent something like if you want to say represent handwritten digits like one zero through nine,
*  it might be able to represent the idea of a loop or a circle.
*  So that's kind of intermediate representation.
*  Yeah, it's not just what's going on in one pixel.
*  It's a global holistic property.
*  Right. And this seems to be what the brain does in some very, you know, rough sense.
*  In the visual cortex.
*  So perceptrons had did not have that hidden layer.
*  They just had an input layer and an output layer.
*  And the problem was that they because they weren't able to create those internal representations, they weren't able to learn more complex functions, more complex sort of concepts.
*  And the problem with the hidden layer is that there was no learning algorithm that could go from the outputs and look at sort of the errors made at the outputs and sort of apportion credit for or blame for that error.
*  Those errors back through a hidden layer to the input through the different neurons.
*  Yeah.
*  So it made the whole system much more complicated.
*  Nobody had an algorithm for learning.
*  So the perceptron did have an algorithm for learning, right?
*  So it would basically start with random inputs and outputs and then random weights, random weights.
*  So each of the inputs had a weight.
*  Right. Right.
*  So the perceptron sort of cares in different amounts about what's coming in from each of its inputs.
*  That's right.
*  Then it those were set randomly and then it would make a guess as to what the answer is.
*  And if it guessed right, it sort of that was happy.
*  If it gets wrong, it would adjust.
*  It's just its weights.
*  Right.
*  And that's sort of that's kind of what the brain does.
*  You know, neurons have inputs.
*  The connections between neurons are they can their weight can be changed.
*  Their strength can be changed from the synapse.
*  And that's what learning seems to consist of in the brain.
*  So for the deep neural networks or neural networks in general, the trick was to teach the whole network how to learn in that sense.
*  That's right.
*  And not until the later part of the 70s, people come up with an algorithm called back propagation, which was able to train neural networks that had these intermediate or hidden layers.
*  So it was Minsky and Pepper.
*  They didn't come up with that algorithm.
*  No, but I'm sorry.
*  Those are the authors who were skeptical about perceptrons and neural networks.
*  That's right.
*  And they also, you know, when I went in and read some of the historical literature, I found that Minsky and Pepper were very concerned about neural networks.
*  It being sort of a competitor for their approach to AI, which was very different.
*  OK. What was theirs?
*  Theirs was called a people call it symbolic AI.
*  And it was much more based on humans programming and rules.
*  I see.
*  OK.
*  And instead of learning and also having the rules be interpretable to humans.
*  And the back propagation made neural networks much more successful than Minsky and Pepper said they could be.
*  Yeah, Minsky and Pepper actually doubted that there could be a learning algorithm, but they were very quickly shown to be wrong.
*  And they apologized later.
*  OK.
*  And is that basically the kind of learning algorithms we still use?
*  Absolutely.
*  Yeah.
*  Almost completely.
*  We use, people use back propagation.
*  OK.
*  Which is based on calculus.
*  Good calculus.
*  Always a good thing.
*  Yeah.
*  And it's very elegant and it seems to work.
*  And except that, let's see, we've gone away a little bit from being inspired by the brain, right?
*  Because the individual, sorry, what do we call the individual nodes in the neural network?
*  Neurons?
*  So some people call them neurons.
*  Some people call them units.
*  Units.
*  I'm going to call them neurons.
*  I don't care.
*  I don't care what the neuroscientists think.
*  Neuroscientists hate it when you call them neurons.
*  I know.
*  Well, yeah, they can adjust for this duration of this podcast.
*  So the individual neurons, we have a learning algorithm that propagates information backwards and forwards through the network.
*  But in the real human brain, there's different modules, right?
*  There's a visual cortex.
*  There's, you know, the amygdala and whatever.
*  And my impression, correct me if I'm wrong, is that neural networks start off pretty undifferentiated, right?
*  They start pretty homogeneous.
*  It's just like a whole bunch of neurons and they're going to train themselves.
*  And then wherever they go is wherever they end up.
*  That's right.
*  There's a lot of differences between neural networks in the brain.
*  Most of the most successful neural networks people use today are very loosely based on the way the visual system works, at least as of 1950, the understanding.
*  They're called convolutional neural networks.
*  So I don't know.
*  Some people in your audience probably have heard of these.
*  So what does that mean?
*  What does convolutional mean in this context?
*  So the idea here is that if you look in the visual system, each neuron in, say, the lowest layers of the visual system, visual systems organized into layers.
*  Okay, the lowest layer, each neuron very roughly, this is a very rough approximation, has input from, say, the retina.
*  And it's looking out at the visual scene and it's sensitive to a particular part of the visual scene, a small part.
*  And what it does is very roughly equivalent to a mathematical operation called a convolution, where it essentially multiplies its weights of its inputs, times the input values in this small area and sums them up.
*  So it's sensitive to some things and not to other things.
*  Which makes it sensitive to some things.
*  And in particular, the neuroscientists Hubel and Weasel, who discovered this sort of structure, found that these neurons were sensitive to edges, which makes sense for vision.
*  You know, you'd like to know where the edges are.
*  I think so, yes.
*  And each neuron is sensitive to particular kinds of edges, like some are sensitive to vertical edges, some are sensitive to horizontal edges, some are sensitive to edges in between.
*  So that's what a convolutional network does, is it has this idea of each neuron having a small sort of receptive field.
*  That is, it pays attention to a small part of the visual field and it does these convolutions, which are essentially detectors for things like edges.
*  Nobody actually programs them to specifically detect edges.
*  But if you actually train them on lots and lots of images, the lowest layer in a convolutional network will develop edge detectors, just like the brain.
*  Presumably because that's a useful thing for computers to recognize, just like us.
*  Yeah.
*  Then there's a claim that they develop similar kinds of representations in even higher layers to what's seen in the brain.
*  But that's a little bit harder to test.
*  And well, this is a big part of the problem, right?
*  Or at least, again, in my medium level understanding, we can get deep learning neural networks that are very good at certain tasks.
*  But then if you ask why they're good at it, you know, what is going on inside those hidden layers, it's kind of hard to suss out.
*  Exactly.
*  Neural networks are pretty complex systems.
*  They have, especially the ones that are used in real world tasks today, have millions of weights in them, some even billions of weights.
*  And it's really difficult to figure out what they're doing.
*  You know, it's not like the Marvin Minsky approach to AI where a human is building in the rules.
*  You know, I say, you know, if you're driving in your car and you see a red stoplight ahead, stop.
*  Instead, that is somehow encoded in these billions of weights in a way that's very hard to visualize or pinpoint.
*  And it makes them this is choppy ahead maybe a little bit, but it makes them easy to fool, right?
*  Like there's a training set.
*  We give them certain information if you're just trying to recognize digits or recognize stop signs or whatever.
*  And then it learns a certain thing.
*  And then if you know that it's good because of a certain training set, you can give it an image that we human beings would instantly recognize and they would get wrong.
*  Yeah, they are very easy to fool.
*  That's for sure.
*  And it seems that a lot of machine learning systems, not just neural networks, are easy to fool.
*  Big data somehow causes networks to focus on certain features that make it fairly easy to fool them if you know what you're doing.
*  I read recently that image recognition algorithms are much more sensitive to textures than human beings are rather than edges.
*  So if you showed a picture of a cat with the skin texture of an elephant, it will certainly say it's an elephant.
*  Right.
*  So that's something that I think a lot of people don't really...
*  It's not obvious when you're looking at these networks.
*  They perform really well.
*  So, you know, think of a face recognition neural network.
*  You train it on millions of faces and now it's able to recognize faces of certain people.
*  So we humans look at it and say, oh, it's good at recognizing faces.
*  But you don't actually know for sure that that's what it's recognizing.
*  So it may be that there's some aspect of the data, some, as you say, texture or something in the data that it's very sensitive to,
*  that happens to be sort of statistically associated with certain faces.
*  And so it's not necessarily learning to recognize the way we recognize, the way humans recognize.
*  It may be something completely different that may not generalize well.
*  Yeah. When the context changes, that correlation might completely go away.
*  And that's something that people have found with these neural networks is that not only are we able to fool them,
*  but even if we're not trying to fool them, certain small changes in the data that they're given,
*  that they're slightly different in certain ways from the input will cause them to fail.
*  So one recent experiment, they trained a neural network to recognize fire engines, fire trucks, right?
*  Then they photoshopped images of fire trucks in weird positions in the image.
*  So upside down, sideways in the sky.
*  And the network could completely misclassify it, even though human would be able, you know, would recognize them.
*  So then when we say we've trained them to recognize fire trucks,
*  it's not totally clear what we've actually trained them to recognize.
*  So that's a little bit of a difficulty in neural nets.
*  Well, and this is one of the reasons why some of the most impressive successes of AI programs have been in very well-defined finite situations like games, right?
*  Like chess and Go and so forth. It's clear what the rules are.
*  There's no equivalent of an upside down fire truck in a chess game.
*  Right.
*  And then, but it's also a reflection of the fact that the way the network is doing it is a very different way of thinking than human beings are doing it.
*  Right. I mean, should we be very happy, very impressed or a little bit skeptical about the successes of these computers at winning in Go or chess?
*  I would say both, a little both.
*  You know, it's very impressive.
*  You know, chess and Go are really hard games.
*  People train for years to be good at these games and now machines have surpassed them in all of these games, which is really impressive.
*  Go has been long term sort of grand challenge for AI.
*  On the other hand, it's not totally clear that the same techniques that make them so good at Go and chess are going to sort of carry over to any real world.
*  If you will.
*  Yeah.
*  Ability. And we really haven't seen much of that.
*  Well, I guess my contrary take is I'm not I've never been impressed with the fact that chess and Go are regimes in which computers can beat us.
*  Like I would think that those are the most obvious places where computers should be able to be.
*  It's the impressive thing to me is that human beings with our very limited number crunching capabilities in our head are pretty good at chess and Go.
*  If computers become good at soccer and baseball, I'd be much more impressed.
*  Well, yeah. I mean, but I think that not everyone saw it that way.
*  A lot of people saw Go and chess as sort of the pinnacle of intellectual power.
*  If you would have to. And, you know, a lot of very smart people literally said that back in the 60s and 70s that if a computer could play chess at the level of a grandmaster, AI would be solved.
*  It's just very backward.
*  I mean, human beings are really bad at taking cube roots of numbers and computers are really good at that.
*  And chess and Go seem to me like kind of like that.
*  We're impressed by them in our fellow human beings because they seem like things that computers should be good at.
*  That's my view. I don't know. Maybe I'm on the wrong track there.
*  No, I think that's that's very insightful and interesting.
*  But, you know, it's in some ways it's looking backwards.
*  I know I'm too late. I should have written a skeptical book about this years ago.
*  So people in AI sometimes complain about this attitude that, you know, once a computer can do it, we no longer say it requires intelligence.
*  That's fair. We are we are moving into the real world, right?
*  I mean, I did see some robots playing soccer, but things like self-driving cars and automated driving is much more something we're pushing on very hard.
*  What is your view of how that field is advancing?
*  So self-driving cars are is prototypical field for AI.
*  It's one where people think it's going to be very easy that, you know, we were 90 percent of the way there.
*  They think it's going to be solved very soon.
*  And yet every time they try to deploy it in the real world, the real world bites back.
*  The real world is different from simulation.
*  It's different from it's different from sort of all experimental techniques.
*  It's it's it's self-driving cars turned out to be a lot harder than people thought, just like a lot of things in AI.
*  And the reason seems to be that there are so many different possible things that can happen.
*  And I think this is true in most of life, not just driving.
*  But most of the time you're driving along, you know, and you're on the say you're on the highway and there's cars in front of you, there's cars in back of you and nothing much is happening.
*  But occasionally something unexpected happens like a fire engine turns on its siren and starts coming by or there is a tumbleweed in the road.
*  I spent a lot of time in New Mexico.
*  And even though events are unlikely, they're crucially important that we get them right.
*  Yes. And one of the problems with self-driving cars, I've been told nowadays is that they perceive obstacles all the time, even when there's no obstacle or human wouldn't consider the thing an obstacle.
*  And so they put on the brakes quite a bit.
*  You had the example of seeing a snowman on the side of the road.
*  So they don't know they don't know what to do.
*  You know, say there's a snowman on the side of the road.
*  So that's like unlikely, but could happen.
*  A computer has no way of knowing that that thing is not alive and is not going to cross the street.
*  It has no way of knowing if a dog is on a leash or not.
*  It's going to run out in front of traffic.
*  You know, it doesn't. There's a lot of things that could that humans can tell very clearly by their behavior what they're going to do next.
*  But self-driving cars have a lot hard time predicting.
*  I'd like to talk about Peloton cardio bikes.
*  We all know that exercise is important.
*  It's good for your brain, good for your body, good for your energy level.
*  But it can be hard to find either the time or the motivation.
*  With a Peloton bike, which fits into a tiny space in your home or apartment, four by two across,
*  you can just decide whenever you want to get on the bike and go for a workout,
*  whether it's 20 minutes or an hour or whatever you feel like.
*  And there are classes that guide you through.
*  So there's motivation there.
*  You get all the benefit of going to a gym and taking a class,
*  but with the convenience of doing it whenever you want, at your pace, at your level of experience.
*  You can get different kinds of classes with curated music, hip hop, country, Latin, whatever you're in the mood for.
*  I love the convenience of being able to do it at any time at all.
*  Peloton is offering a limited time offer for Mindscape listeners.
*  You can get $100 off accessories when you purchase the Peloton bike and get a great cardio workout at home.
*  Go to onepeloton.com and use promo code Mindscape to get started.
*  That's O-N-E-P-E-L-O-T-O-N.com.
*  And it seems to me that this is at the heart of it.
*  It's not just that these arenas are more complex than Chess or Go,
*  but that it's a place where we humans have a competitive advantage, right?
*  We have some picture of the world built into us that helps us answer some of these questions.
*  Whereas if you're just a big neural network trained on a bunch of test cases,
*  you don't have that common sense that we even come equipped with.
*  Right. So common sense is a really important idea in AI.
*  It's been talked about for years, and it's kind of an umbrella term for all the stuff that humans can do without even thinking about it.
*  Yeah, if I put the glass on the table, it will not fall through.
*  Yeah, it's all the stuff we know that we either were born knowing or learned very early in life.
*  And we have models of the world that give us common sense, you know, that we just have a vast amount of knowledge.
*  Nobody knows how to model that in computers.
*  There's a lot of effort being put into it.
*  Well, you mentioned this thing I'd never heard of called Psych, which is short for encyclopedia in this case.
*  And I guess that was Douglas Lennett.
*  And an attempt to codify, a decades long attempt to codify what human beings take for granted.
*  Exactly.
*  In just a list of propositions, or how is it encoded?
*  It's encoded in a list of propositions in a logic-based language, and it's able to make deductions and sort of deduce new facts.
*  So what kinds of facts count as common sense to this program?
*  Every living, every human has a mother.
*  Every human has a father.
*  A human cannot be in more than one place at a time.
*  If you leave a coffee cup full of coffee out in a cold room, it will cool down.
*  You know, any, everything.
*  You can't imagine listing all of the things that you know.
*  And how long has this been going on, the attempt to make all these?
*  Maybe 30 years.
*  And there was, the guy said that there may be 5% of the way.
*  Yeah.
*  Do you believe that figure whatsoever, 5% of the way, to understand common sense?
*  No, I have no idea how he got that.
*  That seems crazy.
*  I mean, there's no way you could possibly list all of the individual propositions of human knowledge.
*  And does it even seem like the right thing to do?
*  I mean, maybe we've learned from certain artificial intelligence success, like AlphaGo, which is the best Go player.
*  Eventually they figured out that it was better just let it train itself rather than to learn from human beings.
*  But maybe there is some advantage in this wider context of teaching it something about the world, right?
*  Like rather than just a list of true things, like something about physics and something about their folk reality that we live in.
*  Right.
*  So this, so we have humans, you know, have this knowledge that people call sort of like intuitive physics.
*  Yeah.
*  You know, I know that if I drop, if I drop a ball, it's going to fall.
*  And I know if it's made of a certain material, it's going to bounce.
*  If it's made of other material, it's going to, it's not going to bounce.
*  Right. I have all these things that I just know because either it's innate or I was learned them when I was a baby.
*  And there's a lot of theories about developmental psychology, about how human babies learn things and animals and so on.
*  We also have some things that are even more basic than that.
*  We have this idea of cause and effect that certain things can cause other things.
*  Networks don't necessarily have that.
*  No, they have no notion of causality, but that seems to be really important.
*  We have this notion there are objects in the world.
*  The world is divided into objects.
*  They have some permanence.
*  They have some permanence and you know that they have certain properties and neural network doesn't know that.
*  And it's not clear that it could learn that.
*  So if some object disappears behind a barrier, it would eventually reappear as something a human being would think, but the neural network might not know that.
*  But even the notion of an object itself.
*  Yeah.
*  So one example was if in addition to AlphaGo, the Google Deep Mind group did some work on Atari video games.
*  OK.
*  And there was one game in which you take a joystick and you move a paddle to hit a ball.
*  This is all like in software.
*  Hit a ball to knock out bricks.
*  It's called Breakout.
*  Breakout.
*  Yeah, it's a fun Atari game.
*  So they taught they used reinforcement learning just like in AlphaGo to teach the machine how to play Breakout.
*  It only learned from pixels on the screen.
*  Yeah.
*  Didn't have any notion built into it.
*  So it doesn't think, oh, I have a paddle.
*  There's a ball.
*  There's a wall.
*  But it learned to play at a superhuman level.
*  But then another group did an experiment where they took the paddle and they moved it up two pixels.
*  Now the program could not play the game at all because it hadn't abstracted the notion of a paddle as an object.
*  It's just a bunch of pixels.
*  Yeah.
*  You know, it was as if we would see the world and not see objects.
*  But what's the lesson there?
*  Is there a way that we can is there a more efficient way of teaching the computer how to think about the world to give it some common sense?
*  We may have to build some things in.
*  It may be that things are built into our brain by evolution.
*  Sure. That would be the least surprising thing in the world.
*  Yeah, I know that there's been a debate in cognitive science, if you will, or AI for, you know, 100 years about innateness.
*  What we learn versus what's built in.
*  And no one really knows for sure.
*  But there's a lot of evidence that there are some innate concepts that we are born with.
*  They're just given to us.
*  And we they bootstrap our learning.
*  We can't do it without them.
*  And so we may have to build some things into our AI programs.
*  And this is just anathema to deep learning people, a lot of deep learning people, because deep learning and other machine learning was put in opposition to the old fashioned way of doing AI where everything was built in.
*  Yeah.
*  And that turned out to be very brittle and not very adaptive.
*  So people want to just focus on learning everything from data.
*  I know that Judea Pearl, who's the doyen of causality, gives AI researchers a hard time exactly for this reason that cause and effect relationships are just not things that they program into the computers.
*  And it's not clear you can learn that even the concept of cause and effect from a bunch of data.
*  Well, is there some intermediate where we don't teach the computers physics or intuition, but we do teach them some higher level concepts.
*  We teach them metaphysics.
*  We teach them objects and provenance and cause and effect.
*  And they learn what they could learn, how many dimensions there are in space, maybe just by experiencing things.
*  So there are some people who are working on that kind of thing, on building in some primitives and then having the system, say, put in a virtual reality and try and learn physics.
*  Oh, good.
*  How's that going?
*  It's, you know, there's some good demonstrations, but it's not very general.
*  I think it's a very hard thing to do.
*  And the virtual reality we have today is maybe not.
*  I mean, again, there's a virtual reality can be very complicated, too.
*  And so it's hard to learn.
*  Do you think this is a promising way forward to try to teach some some of these fundamental issues?
*  What should I say?
*  I think metaphysics was a perfect word for that.
*  Yeah, really.
*  Good.
*  Yeah, I think there there is.
*  And in fact, DARPA, the Defense Advanced Research Projects Agency, which funds a lot of AI, has a big push on what they call foundations of common sense.
*  They're funding a lot of work on this.
*  And their goal is to basically have the group simulate a baby from zero to 18 months.
*  They have all the developmental milestones that they've gleaned from the psychology literature, and they want the artificial baby to essentially go through these developmental milestones.
*  It doesn't have to be an actual robot baby, but some kind of simulation.
*  Yeah.
*  And it's going to be tested with the same kind of psychological experiments that people use on babies.
*  So that's their idea.
*  And it's going to learn from videos and virtual reality.
*  We'll see.
*  We'll see how that happens.
*  Yes, that's right.
*  So but I don't want to completely lose track of this thing you said about how this approach is getting pushback from the deep learning expert.
*  Right.
*  So there's many people in deep learning who feel that building things in is cheating.
*  Is it just cheating or is it ineffective?
*  I think they feel that it's in some sense both just as it was back in the good old fashioned AI days that it makes the system unflexible.
*  That we don't know what to build in.
*  You know, just we can build in rules, but those rules will be unflexible because we can't foresee every possibility and that things need to be learned by the system.
*  Are those the same people?
*  I guess I'm not very sympathetic to this, I have to say, because I do think the common sense is secretly really, really useful and training on huge data sets won't necessarily get you there.
*  I recently appeared on a podcast with Lex Friedman, who is an artificial intelligence guy.
*  And so I went as far as to say maybe programs that try to recognize the number three, the digits of the numerical system would be aided if they understood the concept of three.
*  He thought that was terrible. He thought it was a very bad idea.
*  Oh, that's that's an interesting idea.
*  So there is a group who is working on this kind of thing.
*  I'm thinking of, for instance, Joshua Tenenbaum at MIT and his group and some of his former students are looking at that kind of thing, recognizing characters.
*  And by understanding the characters more deeply than just the visual sort of presentation of the characters.
*  And one of the things they want to be able to do is to understand how a character was written in terms of the actual pen strokes and to be able to reproduce that and to learn from that.
*  So be able to generate the thing as opposed to just recognize it.
*  My worry is that if we teach computers this way, they will no longer be able to take cube roots or play chess very well or anything like that.
*  They'll become too human like.
*  Well, that may be an inevitable evolution.
*  So in Doug Hofstadter's book, Gertel Escherbach, this was written in the 70s.
*  So a long time ago, he actually has a set of 10 questions and speculations on AI.
*  And one of his questions was, will a smart computer be able to add fast?
*  Which is exactly that question.
*  And what was his answer? His answer was no.
*  Because exactly what you said, our numbers, to us, the concept of three is a full-fledged concept that has a lot of baggage.
*  He said exactly a lot of baggage.
*  And when we think about three, we don't just have some bit string representation.
*  We have all kinds of associations with it, which maybe makes it hard for us to add things.
*  I did read Gertel Escherbach when I was a kid.
*  So maybe this is why I have this.
*  No, it's a great question.
*  And I think, you know, to me, I would say that one of the most surprising things I read in that book.
*  But thinking about it, I think it makes a lot of sense that maybe there are tradeoffs, that we can't have human-like concepts and also get rid of all of our human slowness and irrationality and cognitive biases and all what have you.
*  I do think that as a practical matter, there shouldn't be a problem giving a computer a subroutine that can add and subtract and multiply and divide.
*  We can give it a calculator.
*  Yeah, exactly.
*  Just like we, you know, but it won't feel that the calculator is part of it.
*  Right. That's right.
*  It's not part of itself.
*  Well, this is getting us toward, there's one thing to be generally intelligent in the sense that I think generally intelligent is not the right phrase.
*  There's one thing for an AI to be able to work in the real world, like self-driving cars.
*  There's another thing for it to be human-like in its intelligence.
*  Are you someone who thinks that we are going to get there any day or the Google people in your introduction seemed very optimistic?
*  Yes. And a lot of people are very optimistic.
*  I'm not so optimistic because I think human level intelligence is a lot more complex than people realize because a lot of it's unconscious.
*  You know, we don't experience a lot of our intelligence consciously.
*  And this is a problem that I think bleeds into people's view of AI.
*  They think certain things are very easy and certain, you know, and one of the things I.
*  I quoted Marvin Minsky on is easy things are hard.
*  Yeah, that's a great quote.
*  Things that we think are very easy, like looking out in the world and describing what we see or, you know, recognizing your mother or, you know, all of these things turn out to be very difficult in general for computers.
*  Whereas the things we feel are very hard, like playing go, they turn out to be able to do well.
*  Well, we do have chat bots. We do have Siri, things like that.
*  Right. We can mimic at least the rudimentaries of human speech interaction.
*  Right. So rudiments.
*  The rudiments. So a big question is, is that on the right path to actually full blown human-like conversation?
*  Right.
*  The quickest way to do something 50 percent well might not be the right way to eventually doing it 99 percent well.
*  That's right. So so Hubert Dreyfus, a philosopher who was a well-known AI skeptic, had this analogy that you could climb the tallest tree around and say you were closer to the moon.
*  But really, the close the best way to get to the moon is to get down from that tree and get on a rocket ship.
*  Yeah, that's right. That seems very, very like a good analogy for many problems in AI.
*  One issue is embodiment. Right.
*  I think a few other times in the podcast when I've talked not to computer scientists, but to neuroscientists, the point is made that just human thinking is so enormously affected by the fact that the brain is in the nervous system, is in the body, is in the environment.
*  Right. And to date, a lot of AI is still on a computer screen, not in a robot.
*  Right. I think AI people are are are secretly, you know, Cartesian in their computer.
*  In their dualism.
*  They wouldn't admit it, but they don't believe in they believe that intelligence is all in the brain.
*  There are a lot of people who are doing what they call embodied AI, mostly having to do with robots, where actual sort of intelligence is spread throughout.
*  You know, you have to have the right kind of body.
*  I tend to agree with the embodied people that we can't have human-like intelligence without a body.
*  I won't go so far as to say we can't have intelligence because I don't really know what that term could possibly entail.
*  But human-like intelligence is very much rooted in our bodies.
*  That's how we think about concepts.
*  You know, we think in terms of metaphors having to do with the body and physical space and time.
*  We we understand abstract concepts and analogies very physically.
*  Yeah. So I think that's just going to show more and more as we try and push AI further and further.
*  Well, one thing that AI is good at, maybe not AI, but computers are good at these days, are deep fakes, right?
*  Making images or even videos that look like another person is actually saying them.
*  So I'm sure people have imagined this, but won't it happen before too long that we wed a chatbot or something like Siri to a deep fake
*  and can actually mimic not only a video of someone saying something, but an interactive conversation with an actual person.
*  And you wouldn't know you think you're FaceTiming somebody, but you're just FaceTiming an AI?
*  That definitely could happen.
*  But I don't think right now Siri and its cousins are good enough to fake it.
*  Not right now.
*  Right. So that's a real good question.
*  It's always the question about how fast these improvements are.
*  How will more data make them better?
*  Turns out that language understanding is much more difficult than vision, which is interesting.
*  Maybe because it at least the kind of vision, vision in terms of like object recognition and so on, that language understanding involves common sense.
*  It requires a huge amount of knowledge and AI is much less advanced in language than it is in vision, I would say.
*  This is why the Turing test is hard to pass, right?
*  Well, it depends on your details.
*  So there have been chat bots that have quote unquote passed the Turing test with certain kinds of judges.
*  I mean, it's really hard to, you know, a lot of people are very willing to anthropomorphize computers and to believe that they're actually human like.
*  I think that's what it is.
*  Whenever I see these reports of a computer winning the Turing test, passing the Turing test, and then you see some of the actual conversations,
*  I'm just shaking my head and thinking like, how in the world do you think that was a person?
*  Yeah. I mean, if you had to interact with Siri for, you know, 20 minutes talking to it, it would never fool you into thinking it was a person.
*  I do wonder whether or not we also, though, overestimate how complicated people are.
*  Like, is it conceivable that many people actually have a relatively limited set of things they would say or do in any certain set of circumstances?
*  And that might be mimicable in the foreseeable future?
*  It depends. I guess it depends on the idea of limited, you know, how limited.
*  But sure. I mean, I think, you know, these chat bots can carry on a conversation.
*  A lot of times they have what we might call cheap tricks.
*  They change the subject a lot. They ask, they answer a question with a question.
*  You know, they are able to deal with when they can't.
*  Sticky situations.
*  Yeah.
*  But sure. You know, there's one chat bot I know that learns by, it just kind of repeats different things that it's heard from other people.
*  And, you know, it sounds kind of human.
*  Well, that's what I'm thinking.
*  I like many people who are not experts in this field.
*  I'm heavily influenced by science fiction depictions of these things.
*  And Ian Banks, I don't know if you've ever read his science fiction books.
*  But one of the concepts that he has is that people can, you know, be mimicked by computers at some, you know, 90 some percent level.
*  Right. So you can basically download not a copy of your brain,
*  but a much more compact representation of what you would usually say in typical circumstances.
*  And that can outlive you when you die. Right.
*  And so it's like the portraits in Harry Potter where there's sort of a slim, faint reflection of who you really were.
*  But something that people can still interact with after you've gone.
*  That doesn't seem crazily unreachable to me.
*  Yeah, I think you would never actually be fooled by it.
*  You wouldn't be fooled, but you might be able to say some things, learn some things, be amused at the very least.
*  Yeah, I'm sure a lot of the things that I say every day are very stereotypical.
*  And I'm, you know, whenever I'm sending an email and I get the little suggestion from Google Mail about what I'm about to say, it's often right.
*  Pretty good. Yeah, that's right.
*  Which means that I'm just very predictable and boring in a lot of ways.
*  But I like to think that maybe that 10 percent that it doesn't get actually matters a lot.
*  And we already are in a world where, you know, holograms are doing world tours, right?
*  Holograms of dead musicians are on tour now.
*  And maybe, you know, give them a little bit of interactivity could go a long way.
*  Yeah, it doesn't need to carry on a conversation.
*  Doesn't need to be able to write a song, but it could respond to the audience or to the musicians.
*  Yeah, I think that kind of thing could happen.
*  And I do think a lot of cheap tricks can be very effective, if you like.
*  The question is, is it cheap tricks all the way down? Yeah.
*  And I hope not. I don't think so. But it could be. I could be wrong.
*  Well, and the cheap tricks, you know, it sort of leans both ways.
*  One of the things you talk about in your book are the ethics, the values that we are going to attribute to AIs.
*  The fact that an algorithm can be biased, I think, is one that some people have difficulty wrapping their minds around.
*  Right. Data. Algorithms learn from data.
*  So if data is biased, the algorithms are biased. They just pick it up from the data.
*  You know, we have algorithms that are face recognition algorithms that are much better on white males
*  because they've been trained on data sets that are majority white males.
*  You know, they're trained on images that are uploaded to the Internet.
*  And those tend to be well-known people, statistically, who tend to be white males.
*  And so, you know, people in AI have shown that these systems, which people are using commercially,
*  are much more likely to make errors on, say, African Americans.
*  There was a really scary headline I saw that said, you know,
*  self-driving cars are much more likely to hit black pedestrians than white pedestrians.
*  Wow, you've not seen that one. But when you say it, yeah.
*  And a lot of the language systems have bias in their language.
*  You know, I saw one system, a question answering system, that would answer questions about photos.
*  And if you show it a photo of somebody cooking in a kitchen,
*  it's much more likely to think that that's a woman than a man because it's seen more women cooking.
*  Yeah, it's not because women are intrinsically, you know, the ones who cook.
*  But if you train them to think that, that's what they're going to think.
*  And these things can actually matter in real life because they can, if they're used,
*  say, these biases are kind of hidden under the surface if they're used in the real world for these systems making decisions.
*  And the decisions are not very transparent how they're being made.
*  The biases can kind of creep into them. So there's a lot of concern about that.
*  And what is, I don't know, do you have a proposal for what to do about this or how we should be on our guard?
*  Oh, wow. I think we need to have developed some tests of systems bias.
*  You know, we have people who have had these implicit bias tests they give to other people.
*  And those are very revealing. Yeah.
*  You could also find such tests to give to AI systems. I see.
*  So we're going to start giving psychological tests to our computers. Absolutely.
*  And we have to be more concerned about how we form data sets, how representative they are.
*  And the ethics, not only what the AI does, but how we teach it. Exactly.
*  Yeah. And then there's people who are trying to find ways to, quote unquote,
*  de-bias AI systems with limited success so far.
*  If you de-bias them too much, they start to make a lot of mistakes. It hurts their performance.
*  Right. So it's an open research area, but important.
*  And do you have worries about super intelligent AI taking over the world?
*  That's the least of my worries right now. I have a lot of worries, but that's the least of them.
*  I'm a lot more worried about, say, these deep fakes, for example, and just general fake media.
*  And I'm worried about more like the issues of surveillance and privacy.
*  I'm worried about companies deploying AI systems that aren't ready, that are still, that don't have enough sort of quality assurance.
*  Because people use AIs for things like looking at resumes to pick job candidates, right?
*  Yeah. Or sentencing recommendations in the justice system.
*  Yeah, they'll use AI for all kinds of things. Deciding if you're going to get a loan.
*  You know, your bank is using AI and deciding sort of whether you qualify for food stamps.
*  More and more people are using algorithms to make decisions for us.
*  And it worries me. But super intelligent AI seems to me to be very far away.
*  What would it mean? What exactly does super intelligence mean?
*  Well, that's the thing. I'm not even sure. I'm not even sure it's possible.
*  Because intelligence isn't well defined. It's one of those terms that we throw around all the time, but it means so many different things.
*  So intelligence is very, if you were talking about sort of animal intelligence, it's very ecologically specific.
*  It's specific to certain niches. You know, animals, including humans, are adapted for certain kinds of things.
*  They do certain kinds of things. Well, they don't do certain kinds of things. Well, because it helped them to survive.
*  And so when you talk about intelligence as being this sort of monolithic thing, oh, we're going to have super intelligent machines.
*  It's hard to know exactly what that means, right? If something could be sort of better adapted.
*  Maybe these machines could understand, you know, I was listening to one of your previous podcasts about how hard it is to understand the foundations of quantum mechanics.
*  Maybe humans just don't have the right kind of brain for that. Maybe you need a machine to do that, to figure that out, because they have a different sort of ecological niche of understanding.
*  But would we call that a super intelligent machine? I don't know.
*  Yeah, I think this is a very good question. I just last week was at a conference and heard Max Tegmark give a report on stuff he's been doing with his students on AI physicists.
*  So theoretical physicists modeled by AIs. But all they're really doing is very, very fancy curve fitting.
*  They see a bunch of data points and they find the law of physics that best fits those data points.
*  But asking, you know, what is the ontology of reality that would best explain quantum mechanics or something like that is a little bit harder.
*  Right. So I'm being very speculative because I don't think any machine now has anything like the concepts that we have that would allow it to do science in any way, any meaningful way.
*  But if you have to ask, is super intelligent AI even possible, you have to start thinking about what you mean by that and what we mean by intelligence.
*  Yeah. And nobody really has a good handle on what we mean.
*  Well, I think, you know, if the impression I got from your book is AI has become very good at very certain kinds of things, the kinds of things that are naturally adapted to brute force and deep learning.
*  Right. And there's a whole other set of kind of things that really are especially good, that humans are especially good at and the commonsensical things, maybe even the creative things, the creative things of actually less sure about than the commonsensical things.
*  What are the lessons that this teaches us for how we should think about AI and how we should do research on it?
*  Okay, that's a hard question. I don't know if AI is intrinsically limited. You know, AI, of course, isn't just one thing either.
*  I don't know if machines, let's say, are intrinsically limited, that there's things that machines are good at and there's things that we're good at because I think of us as kind of fancy machines.
*  Fair enough. I'm on board with you there.
*  So I'm not sure there's any intrinsic limitations, but we could talk about sort of the current approaches to AI, the sort of data driven approach.
*  There's probably certain things that it's good at and certain things that it's not good at. We've seen that.
*  So for me, there could be two lessons for research. One would be to try and understand better what kinds of things that today's AI are good at and how to maybe make it more reliable, more less vulnerable to fooling it, more trustworthy and so on.
*  But then there's the research into what AI is not good at to say, like, what is it about us that current machines can't do? And there's a lot of things that we can do very well.
*  One of them is forming abstract concepts. That's something I'm particularly interested in.
*  And so all of my research now is on more on that side. It's trying to say what can't these machines do and why not? What are they lacking?
*  And the reason I'm investigating this is not to try and build smarter machines per se, but more because I want to understand how what intelligence is and how maybe we do it or how it could be done more broadly.
*  So I think of it as more of a scientific than engineering approach.
*  So give us a hint. Well, how do we form an abstract concept? Is this something that you've learned something about in the research?
*  Or why is it hard?
*  Why is it hard? Well, okay, that's that's interesting.
*  So here's here's an example.
*  Think of the concept of sameness, like two things being the same.
*  That's an abstract concept, right?
*  It's very abstract and it's something that deep neural networks can't do even in the simplest form.
*  They can't recognize same, you know, if you give them an example of some something in which two things are the same versus two things are different.
*  In general, it can't do that task.
*  Whereas we humans can very easily.
*  Well, I would say we kind of can write if you ask people what they mean by sameness, then you're going to quickly get into a philosophical argument.
*  Right. Right. And a friend of mine actually wrote a book called The Subtlety of Sameness.
*  There you go. Like one of my favorite book titles ever.
*  And it is extremely subtle.
*  But we seem to be very good at it.
*  And it's kind of the root of all analogy.
*  You know, analogies are really important part of thinking.
*  And that's essentially seeing two situations as being.
*  Two rather different situations as being intrinsically the same.
*  You know, I look at a particular political situation and I say, oh, you know, I like, for instance, think back in history, we called the Iran Contra deal Iran Gate.
*  Yeah. That was making an analogy with Watergate.
*  Right. Very different situations.
*  But somehow we saw them as like the same kind of thing to cover up.
*  It's a government cover up. Right.
*  And so that's a very subtle kind of sameness.
*  And it's sort of underlying a lot of the thinking that we do in terms of analogy.
*  Well, you have these wonderful examples and maybe they're from Douglas Hofstadter, but of how human beings think by asking if you're given the if you're told that ABC is converted to ABD,
*  then what should PQRS be converted to? Right. Right.
*  So that was that letter string analogies was the subject of my PhD dissertation.
*  There you go. Actually.
*  So I built a program that could do could make those kinds of analogies in what we claimed was a human like way.
*  Because there's no right way.
*  So give some of the possible answers to this question.
*  What should PQRS be converted to if ABC is converted to ABD?
*  So ABC is converted to ABD.
*  What should PQRS go to? Well, most people would say PQRT because they see ABC changes to ABD, the rightmost letter replaced by its successor.
*  OK, but you could also say PQRD replace the rightmost letter by D or you could say PQRS.
*  There's no C's or D's in PQRS.
*  So don't change anything if the rule was change every C to a D or change every C to a D.
*  Right. Or and another answer could be ABD.
*  Change any string to ABD or you know, and you can just go on and on and on.
*  And but people never people are very good at being sort of abstract in the right way.
*  Right. Being, I guess, defined.
*  What do you do? Yeah, that's right.
*  It's a universal way that humans are very consistent.
*  Right. So the idea of that whole project was not to solve letter string analogy problems,
*  but more to model analogy in general and to say that this little micro world of letter strings captured some of our analogical abilities in general.
*  I think this is a deep thing because there are an infinite number of rules that would always explain some situation.
*  This is the do-him-quine thesis in philosophy of science.
*  Have you ever heard of that? Yeah.
*  Any set of data can be fit by an infinite number of theories.
*  Right. And I had a math professor when I was an undergraduate who hated the idea of the rules.
*  He hated the SAT and GRE series test.
*  You know, like when you're given a sequence of numbers and you're told to guess the next one.
*  He goes, mathematically, it could be anything.
*  I could invent any any series of numbers that could be fit by anything next.
*  But I think that the point was my response to him was that they weren't actually math questions.
*  They were science questions. They were looking for patterns in the world and not all patterns are created equal.
*  So in some sense, either because it's we humans or the world we live in with its actual rules acts in certain ways.
*  And therefore it makes more sense to us that certain patterns are the right ones rather than the wrong ones.
*  But it comes down to exactly this common sense, right?
*  This way of dealing with the world that computers are not very good at.
*  Right. And what did you learn by doing this PhD thesis about analogies?
*  Oh, that they're they can be very subtle and that.
*  What did I learn? Well, we developed Doug Hofstadter and I developed an architecture, sort of a computer architecture for solving them that I think is more widely applicable.
*  So I'm working on how does this apply?
*  How can we apply these ideas and more more broadly?
*  And I think that that's an area of research that hasn't been looked at very much in a the whole area of analogy and sort of common sense analogy.
*  Do you see is there a movement in a that's not just a few people, but is there a growing feeling that deep learning is a kind of thing?
*  But we need more common sense.
*  We need more full intuition, more metaphysics in our computers.
*  A lot of people say that. Not everybody.
*  Yeah, I was kind of surprised recently.
*  The Turing Award, which is the highest award in computer science, was given to three deep learning people and two of them, Jeffrey Hinton and Jan LeCun,
*  both gave a speech at the one of the big AI conferences or a conference.
*  Yeah. And they and Hinton particularly was incredibly,
*  was incredibly optimistic about deep learning, whereas LeCun was saying, no, we need something different.
*  Is there any chance that we could learn more about deep learning or make it better just by asking it how it's thinking?
*  Is that at least demanding that when the algorithms reaches a certain conclusion, it can explain itself?
*  Some people are trying to do that, but it's hard.
*  You know, since first of all, to explain itself, it has to have concepts because it has to have a concept of what it did.
*  It can't just say, well, I multiplied this these four billion weights by these other, you know, these inputs and then got this answer.
*  Explaining is kind of relative to the entity you're explaining to.
*  Yeah.
*  And so if it wants to explain itself to humans, it has to have some kind of theory of mind of what counts as an explanation to a human.
*  But now, so I want to be the deep learning proponent instead of skeptic for the purposes of conversation.
*  You know, maybe it could learn that through deep learning.
*  Like, maybe that's a, you know, if we insist that one of its success criteria is it can explain itself,
*  then maybe we'll be forced to come up with concepts and fit them together.
*  Interesting.
*  Easy for me to say.
*  Yeah. Yeah.
*  You'd have to figure out how kind of what language it would explain itself in.
*  And I, you know, it's that sounds hard to me, but I think it's it is important.
*  You know, there's this whole area called meta cognition that people look at.
*  And it's the idea that we think about our own thinking.
*  We're able to explain why we did things not always correctly.
*  We sometimes rationalize why we did something or why you made a decision.
*  But meta cognition is really important part of intelligence.
*  And it's something that people in AI kind of some areas of AI kind of looked at, but nobody has any good ideas about how to do it.
*  I mean, maybe what we're doing is the equivalent of giving our deep learning networks multiple choice tests.
*  So we really should be asking them to show their work.
*  Yes. Yes, exactly.
*  All right. Just to close up, then, you know, let's let our hair down.
*  And it's the end of the podcast and prognosticate about the future a little bit.
*  I know that it's always very hard and I promise not to hold any bad predictions against you 50 years from now.
*  But just as one data point, you know, what do you think the landscape will look like 50 years from now in terms of AI, in terms of how general purpose it will be, how much common sense it will have, how close it will come to being humanly intelligent?
*  50 years from now.
*  Wow.
*  You can change it to another time, but I think 50 years is good because on the one hand, we'll probably be dead.
*  Yeah.
*  On the other hand, like you can probably maybe you can accurately guess 10 years from now, but no one can guess accurately 50 years from now.
*  So, yeah, well, I can imagine that we would have much better chat bots.
*  That can do the deep fake stuff would be incredibly good, which is terrifying.
*  So there's already wasn't there recently this demonstration of a chat basically what a chat bot was basically something that was a chat bot called up a restaurant and made reservations.
*  Yes.
*  It really fooled the person on the other and had no idea it was talking to a robot.
*  Right. And that a lot of conversation about should it be required to identify itself as a robot.
*  And I think that kind of there's there'll be a lot of legal framework built up over the next 50 years about AI and that kind of thing.
*  I'm a little scared that we might live in a complete surveillance state in 50 years that everything will be known about everybody.
*  Yeah.
*  And all of that data will be used to who knows what target adds to us.
*  It seems inevitable to me.
*  Have you seen the movie Minority Report?
*  I have.
*  Yeah. I mean, that's like a real dystopia where it identifies you.
*  He does an iris scan and figures out who you are and then can I constantly bombarding ads at you directed completely towards you individually.
*  That's horrifying.
*  But if you look at current trends, that's almost where we're heading.
*  Well, yeah. And I think even much worse than targeting ads.
*  Like, what if we become really good at deciding who will default on the loan and therefore we don't give them a loan even though they haven't defaulted yet.
*  Right. I mean, in some sense, the whole Minority Report plot where we decide if somebody is going to commit a crime.
*  Yeah. I mean, they're trying to do that.
*  I mean, that's perfectly legal for a mortgage company to try to decide the probability you will default on your loan.
*  Yes.
*  And if we become infinitely good at it, or at least we think we're infinitely good at it, then it's a different thing.
*  Then, you know, what is the difference between that and saying, well, you'll probably commit a burglary.
*  Right. I think also because of coevolution with these technologies that a lot of people will be working on how to fool them, how to thwart them, how to avoid this kind of thing.
*  And there will be a big kind of coevolutionary arms race between the technology and the people who don't want to be controlled by it.
*  Presumably there's some good things. I mean, maybe when I call to change my flight reservations, I'll get a much more useful computer interface than I do right now.
*  But audiovisual won't be solved. Like being able to get your slides to show up on the computer.
*  Yeah, that's true. But I guess now, do you think that it will be, you said audiovisual, my brain went to the wrong place.
*  Will it be video calls rather than audio calls? Like this was always already have that.
*  We have it, but people don't use it that much. Right.
*  Yeah, probably people will use it more.
*  Yeah. I mean, weirdly, we use text messaging now more than phone calls.
*  So we've gone downward in the amount of information sent.
*  The kids today, they like to text.
*  Yeah, yeah. We might.
*  It's possible that people won't want to interact at all.
*  Well, again, I'm trying to look at the sunny side of this thing.
*  We can imagine that if we do have the equivalent of deep fake chat bots, they will be useful companions for people, right?
*  For lonely people, for elderly people or whatever.
*  There's a sort of robots are already doing this.
*  Yeah, that's right.
*  That's right. And the effects of that are completely unknown.
*  Yeah. I find that a little scary.
*  Are you mostly scary or are you mostly excited about the robot AI future?
*  It varies.
*  You know, I'm very excited about I tend to get more excited when things don't work.
*  You're a scientist.
*  Yeah, because I want to understand why they don't work.
*  And, you know, that so I don't know if that makes me kind of pessimist.
*  I think there's a lot of things sort of academic.
*  I mean, this is a whole different discussion, but sort of academic research and AI is badly broken in many ways in that people tend to focus on particular benchmark data sets.
*  And see who gets the best performance on them.
*  And the state of art in sort of scientific approach to AI isn't really progressing very much.
*  I think.
*  But what's the relationship between those two facts?
*  Oh, well, suppose that you want to get your paper published in the top conferences in AI.
*  The best thing to do is to take a benchmark data set that a lot of other people have worked on and to do better than anybody else, not to explain anything or to understand why your system did better.
*  So you're saying that we're becoming like the deep learning network.
*  We are. We're being optimized according to benchmarks.
*  That's right.
*  We get rewards in the form of grant money and recognition.
*  Hasn't it always been like that?
*  Is that really?
*  I don't know. I don't know if, you know, maybe a little bit.
*  We're always optimized for our local reward system, I think.
*  Yeah, but it's not always the best for, you know, progression of science.
*  It's true. It's hard to like science does progress pretty well, despite the fact that there are so many obvious flaws in the system that it's hard to know where to start listing them.
*  Yeah.
*  But I like your philosophy of being excited and happy when things break and go wrong.
*  I will count that as an optimistic stopping place because I'm sure things will continue to break and go wrong.
*  Absolutely.
*  All right, Melanie Mitchell, thanks so much for being on the podcast.
*  Thanks for having me.

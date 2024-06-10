---
Date Generated: June 09, 2024
Transcription Model: whisper medium 20231117
Length: 5246s
Video Keywords: ['ai', 'artificial', 'intelligence', 'computers', 'podcast']
Video Views: 15763
Video Rating: None
Video Description: Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2020/04/27/94-stuart-russell-on-making-artificial-intelligence-compatible-with-humans/

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x

Patreon: https://www.patreon.com/seanmcarroll

#podcast #ideas #science #philosophy #culture #ai #artificialintellgence

Artificial intelligence has made great strides of late, in areas as diverse as playing Go and recognizing pictures of dogs. We still seem to be a ways away from AI that is intelligent in the human sense, but it might not be too long before we have to start thinking seriously about the “motivations” and “purposes” of artificial agents. Stuart Russell is a longtime expert in AI, and he takes extremely seriously the worry that these motivations and purposes may be dramatically at odds with our own. In his book Human Compatible, Russell suggests that the secret is to give up on building our own goals into computers, and rather programming them to figure out our goals by actually observing how humans behave.

Stuart Russell received his Ph.D. in computer science from Stanford University. He is currently a Professor of Computer Science and the Smith-Zadeh Professor in Engineering at the University of California, Berkeley, as well as an Honorary Fellow of Wadham College, Oxford. He is a co-founder of the Center for Human-Compatible Artificial Intelligence at UC Berkeley. He is the author of several books, including (with Peter Norvig) the classic text Artificial Intelligence: A Modern Approach. Among his numerous awards are the IJCAI Computers and Thought Award, the Blaise Pascal Chair in Paris, and the World Technology Award. His new book is Human Compatible: Artificial Intelligence and the Problem of Control.
---

# Mindscape 94 | Stuart Russell on Making Artificial Intelligence Compatible with Humans
**Mindscape Podcast:** [April 27, 2020](https://www.youtube.com/watch?v=txGYG60TICA)
*  Hello everyone and welcome to the Mindscape Podcast.
*  I'm your host, Sean Carroll.
*  Hope everyone is more or less staying home and staying safe in these surreal times that
*  we're in with the COVID-19 quarantine, lockdown, etc.
*  It's very challenging out there for everyone.
*  As I said, frequently, probably less so for me than most people since I basically work
*  from home and I have a pretty comfortable situation here.
*  But it's different.
*  You know, you don't get to see your friends, don't get to socialize, don't get to eat out,
*  don't get to go to class in the same way.
*  One thing that struck me is how really different it would have been if something like this
*  happened before we had computers and the internet, right?
*  Of course, plagues and quarantines and pandemics did happen, but just the idea that we couldn't
*  talk to each other over Zoom or send emails or get updates, I think it would be much worse.
*  It would certainly be very, very different.
*  So it's appropriate that we once again turn to the world of computers in this week's episode
*  of Mindscape and in particular the challenge of artificial intelligence.
*  We all know that AI is becoming more and more important, not just as some hypothetical future
*  thing that will talk to us and be our friend, but right here, right now, programs that figure
*  out puzzles in a way that you could think of as being intelligent.
*  Now, there's a looming problem here that everybody knows about, which is as the AIs become better
*  and better, as they become smarter and smarter, more and more powerful, it's going to become
*  increasingly important that they act in ways that are what we want them to do, right?
*  They're intelligent.
*  They can figure out things to do for themselves.
*  It would be bad if what they wanted to do in some sense, and we can figure out the extent
*  to which the word want is appropriate in the case of a computer, but what their goals are
*  are the same as what we want them to be.
*  And this can be very difficult because as anyone who's ever programmed a computer knows,
*  it is very difficult to say what you want.
*  It is very difficult to put into precise algorithmic terms what it is you're looking for.
*  That's why computer programming is hard.
*  And so it's very easy to imagine asking a computer, asking an AI to do a certain thing
*  and then realizing at the end of the day, we didn't really want that.
*  We wanted something that was that, but there were some constraints that we forgot to mention.
*  So today's guest is Stuart Russell.
*  He's a very big name in artificial intelligence.
*  Stuart and Peter Nordvig wrote what is the classic textbook on AI called Artificial Intelligence,
*  a Modern Approach.
*  Even I have this book on my bookshelf and I'm not really an AI person, so that shows
*  you the pervasiveness of that particular text.
*  And recently Stuart has been thinking about exactly this problem, you know, making sure
*  that AIs sort of do the things that we wanted them to do when we designed them.
*  So he has a new book out called Human Compatible, Artificial Intelligence and the Problem of
*  Control and to really oversimplify it, his proposal is that rather than telling the AIs
*  what we want, we will teach the AIs to learn from us what we want.
*  We don't even know what we want, but maybe the AIs can watch our actual behavior and
*  from that work backwards to how they should be behaving to do what it is we want.
*  Now this opens a whole bunch of other questions, right?
*  So that's what we talk about on the podcast, you know, how realistic this is, how much
*  we should be worried about super intelligent AI and what it means for the future more generally.
*  So anyway, I hope that, you know, the Mindscape podcast is contributing a little bit to taking
*  our minds off of the situation we're in with the pandemic.
*  You know, I don't want to...
*  One alternative would be, you know, to switch all efforts into thinking about pandemics
*  and epidemiology and things like that, but I figured there's plenty of people with more
*  background knowledge than I am doing those things.
*  So I'm going to try to keep Mindscape more or less the same kind of thing it always has been.
*  I think it's still important to keep thinking about other questions.
*  You know, pandemics and virology are part of that.
*  And networks and how people communicate is all part of that.
*  Those are interesting things to talk about, and I'm sure we will.
*  But we'll also be talking about physics and biology and philosophy and culture in the
*  media and so forth.
*  Remember that I'm also doing a set of videos called the biggest ideas in the universe that
*  are appearing on YouTube once a week.
*  Once a week I do a big idea.
*  I was really hoping to make these around 20 minutes per idea.
*  So I'm hoping that you guys will be able to get to that.
*  I've crept up to more like an hour with me talking and scribbling little pictures and
*  very primitive equations, but I hope people are finding them fun.
*  So far it's been, you know, more or less classic ideas like space and time and things like
*  that, but soon enough we will be getting to some pretty wild ideas, which I think are,
*  you know, not...
*  I'm not going to be speculating too much when I choose the ideas themselves.
*  But some of the ideas that are part and parcel of modern physics are pretty wild, even the
*  established ones.
*  So we'll be getting into those and I hope you enjoy those also.
*  And with that, let's go!
*  Stuart Russell, welcome to the Mindscape Podcast.
*  It's nice to be here.
*  We're going to talk about artificial intelligence, the warnings, the worries that we have about
*  artificial intelligence and also the prospects of it.
*  But I think that it would be a wonderful opportunity here since you not only are someone who has
*  specific ideas about fixing any dangers of artificial intelligence, but you're also someone
*  who has been doing research in this field, literally wrote the textbook, etc. to talk
*  about some of the background here.
*  So I thought I would just start by asking you, in your mind, what does the phrase artificial
*  intelligence actually mean?
*  How do you define that term?
*  So obviously artificial intelligence is about making machines intelligent.
*  And what that has turned into, actually from right at the beginning of the field, is an
*  approach to building systems that are given objectives by humans and then find ways to
*  carry out those objectives.
*  So the objectives might be goals.
*  Can you find a plan that achieves this goal?
*  It might be a reward function.
*  Can you behave in a way that generates the largest amount of reward?
*  For example, can you make money on the stock market?
*  So this has been the way that the general idea of intelligence has been instantiated
*  to build systems that act in ways that can be expected to achieve the objectives that
*  we set for them.
*  And is there some way of definitively saying when a certain computer program is AI versus
*  just a regular computer program?
*  In some sense, isn't a pocket calculator optimized to add numbers together correctly?
*  Yes, and I think that's part of the difficulty.
*  There really is a continuum between something as simple as a thermostat that switches the
*  heat on when it gets cold and switches it off when it gets warm, all the way up to humans
*  and even beyond.
*  And the continuum is mainly in the nature of the task environment, how complicated is
*  the world that the entity has to deal with, and then what is the actual objective.
*  And some objectives can be achieved even in a complicated world, can be achieved with
*  very, very simple rules.
*  And some, for example, winning at a game of Go or running a country or teaching someone
*  to speak French.
*  These are very, very complicated goals and they take place in a very, very complicated
*  task environment, which is an environment that includes human beings.
*  And that's probably the most complicated environment we know of is the one where there are humans
*  that are part of it.
*  But you would say, I mean, I like the point that there's a continuum here.
*  It's not like there is some sharp phase transition between dumb computer programs and artificially
*  intelligent ones.
*  That's right.
*  In fact, there's a nostrum that's been put about a long time that as soon as it works,
*  it stops being artificial intelligence, which is a little bit unfair because of course that
*  means that the AI is the field of continual failure.
*  But that I think is that's in some ways accurate that a lot of things that AI has produced
*  over the years, for example, every time you drive in your car and you get directions,
*  there's an AI algorithm running in your cell phone or maybe in the cloud that is computing
*  shortest paths and incorporating expected delays and so on.
*  This is a very classical AI algorithm that was developed in the late 60s and early 70s.
*  And no one thinks of that as AI anymore.
*  But of course, someone had to invent it.
*  And before it was invented, no one knew how to do it.
*  And we now, I think, take speech recognition for granted.
*  But that's another part of AI that's been gradually improving for the last 50 years
*  or so.
*  But now that it works and it's just one of the things that runs on your cell phone, you
*  don't think of it as AI anymore.
*  And that's a pity because it also means that there's a tendency, I think, for students
*  to not want to study things that we already know how to do.
*  Which means, of course, that the students don't learn how to do anything.
*  That works, right.
*  But I mean, even you mentioned playing Go as one of the more complicated tasks.
*  But I would sort of put playing Go more on the finding a route to your destination side
*  of the ledger and driving a car or writing a poem on another side.
*  If we think about the fact that the rules of Go are extremely explicitly defined, and
*  even though the state space is huge, the space of possible things that can be going on, it's
*  still finite, right?
*  I mean, there is a right answer to every question, whereas these more human scale things are
*  a little bit fuzzier.
*  Is that a relevant distinction, you think?
*  It is, yes.
*  I think there's multiple distinctions being made here.
*  One is that, as you say, the rules of Go are known.
*  So the objective is to win.
*  And that has a precise definition that varies slightly from country to country, but pretty
*  much agreed on.
*  And you know that when you put a piece on a square, the piece ends up on that square.
*  It doesn't sort of run around by itself and go somewhere else.
*  And of course, when you're driving, you don't even know the rules.
*  You don't know what's going to happen when some other entity is involved and making decisions
*  about where they're going to go, which will affect your own ability to get what you want
*  done done.
*  And the other part of driving that's difficult is that the objective is also not known.
*  So obviously, you would like, you know, if you say, take me to the airport, you would
*  like to get to the airport.
*  But you don't mean take me to the airport at all costs.
*  So if there's an earthquake and the Bay Bridge falls down again, then that doesn't mean you
*  would drive me 200 miles around and get me to the airport an hour after my flight leaves.
*  It doesn't mean, you know, plunge into the into the bay and try to swim across the bay.
*  When you give a human an objective like take me to the airport, the human understands under
*  what circumstances is it reasonable to give up on that.
*  Plus, there are many different ways of getting to the airport.
*  Is it that you take the shortest route?
*  And then how fast do you drive?
*  How safely do you drive?
*  Do you do you go right up to the edge of catastrophe at all times in the hope of getting to the
*  airport a little bit quicker?
*  And, you know, I've taken taxis where that was how they drove.
*  And you've taken other taxis where you just want to say, look, can you just get on with
*  it?
*  Because they're extremely cautious.
*  So there are many ways of driving.
*  So there are many ways of driving and there isn't an actually agreed on objective for
*  what counts as good driving and how that depends on the circumstance and the urgency
*  and so on.
*  So driving is different from go in both of these dimensions.
*  And it's an unsolved problem right now, whereas I think we would say that that go to the extent
*  that that it can be solved.
*  And there are mathematical reasons to believe that we probably can't solve it exactly.
*  But to the extent that we can come up with good algorithms, we consider the game go to
*  be one where AIS had had success.
*  We've beaten the human world champions and actually taught humans things about the game
*  that they didn't know before.
*  So you mentioned an idea that I think is worth sort of lingering on and drawing out,
*  it's going to be important for the rest of the conversation.
*  The idea of optimizing for some goal, right?
*  I mean, probably if you told a person on the street that that's what an AI program was
*  trying to do, they might not instantly see the connection between ordinary human intelligence.
*  I mean, do you think that we can think of all intelligence as optimizing towards some goal or
*  maximizing some utility function or something like that?
*  It's a good question.
*  And I would say that it's taken a few thousand years to convince at least one branch of the
*  intellectual community that that's a good way of thinking.
*  And the branch that's most convinced about that would be the economists.
*  Because they've reached by the 1940s, they reached a formulation of rational decision making
*  that is quite general.
*  So it allows for the decision maker to have uncertainty about the state of the world,
*  about the future.
*  It does, at least in the original formulation, assume that the decision maker has preferences.
*  And this is the way economists think about it, that if you think about each possible future
*  that could unfold, in principle, I could express a preference as to which future I like better than
*  which other future.
*  And that's the basis for then the economic notion of rationality as utility maximization.
*  It doesn't mean that you have to have a number in your head, which is the utility of each future,
*  and then you have to add them all up and divide by the probabilities and so on.
*  It simply means that you act as if you did, and you can be described as long as you're not making
*  mistakes, then your behavior can be described as if that's what you were doing.
*  It doesn't mean that you are actually doing that.
*  So for example, if I try to poke myself in the eye with my finger, my eyelid closes.
*  Now, my brain is not doing expected utility calculation to reason that I ought to close
*  my eyes because having a fingernail poking my eyeball is painful and dangerous, and that
*  will be a low utility.
*  And so if I close my eye, then I'll protect it.
*  No such thing.
*  It's just an instantaneous reaction to a looming object in the visual field, but it's still a
*  rational thing to do.
*  In other words, if you were to do the expected utility calculation, it would tell you to close
*  your eyes, but you don't have to do that calculation in order to close your eyes.
*  I'm visualizing thousands of podcast listeners trying to poke themselves in the eyes as we
*  speak right here.
*  Hopefully.
*  Yeah, so Max Tegmark said it didn't work.
*  He tried to poke himself in the eye and he succeeded.
*  Yeah.
*  Well, someone who used to wear contacts, I think I have no trouble doing that.
*  I love recommending the Great Courses Plus.
*  This is a streaming service that gives you access to a huge variety of courses from the
*  Great Courses taught by some of the best professors in the world on a wide variety of
*  topics.
*  You can learn about everything from playing guitar to practicing yoga to history to science
*  to literature.
*  I, of course, am one of the professors at the Great Courses.
*  I recently did my little video on the nature of time for the biggest ideas in the universe.
*  I did a whole course for the Great Courses on mysteries of time.
*  So if the hour long version was not enough, if you want the 12 hour long version, go to
*  the Great Courses Plus, look for the mysteries of modern physics time, learn about entropy
*  and the arrow of time, but also about timekeeping, about time and particle physics,
*  about the psychology and neuroscience and philosophy of time.
*  The Great Courses Plus is giving Mindscape listeners a special offer, a free trial with
*  unlimited access to the entire library.
*  Find all the details at thegreatcoursesplus.com slash mindscape.
*  That's T-H-E Great Courses P-L-U-S dot com slash mindscape.
*  Start learning today.
*  I do, and this is probably leaping ahead, and that's okay.
*  We don't need to go in logical order, but you quote a theorem in your book.
*  You wrote a wonderful book called Human Compatible.
*  Actually, it is, that's, I'm not just saying that as boilerplate.
*  I really enjoyed the book and I encourage everyone to take a look at it.
*  So it's a theorem by von Neumann and Morgenstern, which if I understand it correctly, I've heard
*  of it before and then was reintroduced to it in your book.
*  Roughly, it's that conclusion you just said that if you're behaving rationally, then there's
*  always a way to cast the decisions you're making in terms of maximizing some utility
*  function.
*  Is that right?
*  Yeah.
*  So it starts from a description of what we mean by behaving rationally that's pretty
*  hard to argue with, and that's how these kinds of proofs usually go.
*  You propose some axioms that sound completely reasonable, and then you draw what appears
*  to be a very strong conclusion.
*  So the axioms say things like, if you prefer sausage pizza to plain pizza and you prefer
*  plain pizza to pineapple pizza, then you prefer sausage pizza to pineapple pizza.
*  Yeah.
*  Right?
*  This is called transitivity of preferences.
*  And what that basically says is your preferences don't go round in a circle.
*  And that seems perfectly reasonable because if your preferences did go round in a circle,
*  then basically you would pay me to go in the other direction.
*  So if you liked sausage better than plain and you had a plain pizza, you'd pay me to
*  get the sausage pizza.
*  And then if you liked pineapple better than sausage, you would pay me to get the pineapple.
*  And then if you like pineapple better than plain, so your preferences are now in a circle,
*  you'd pay me to get the plain.
*  So now you paid me three times and you're back where you started.
*  So that doesn't seem very rational.
*  So the axioms of rational behavior have this flavor that they're really hard to argue with.
*  You'd have to agree that an entity that didn't follow those axioms would basically be shooting
*  itself in the foot all the time.
*  And then the consequence of these axioms is that the behavior of a rational agent
*  can be described as if it's maximizing a utility function.
*  Good.
*  Yeah.
*  And so that was the theorem of von Neumann and the main theorem in that book.
*  But I think you've also already hinted at a little bit of attention there, right?
*  Because there's lots of mathematical theorems that say something is possible in principle.
*  But as you already mentioned with the poke in the eye example,
*  for actual systems that do something we call reasoning, they might not implement that design
*  in order to get things done.
*  But is it safe to say that most AI algorithms do try to implement something like that,
*  that they do actually sort of optimize over a utility function over a whole bunch of
*  hypothetical actions?
*  Yes and no.
*  So the biggest obstacle from the point of view of AI is that actually optimizing in
*  many situations is what we call computationally intractable,
*  which roughly means that if you really want your algorithm to come up with the
*  optimal solution, you're going to have to run it until the universe ends.
*  So billions and billions of years of computation.
*  And then if you make the problem twice as big, it's going to be a billion times more than that.
*  So these kinds of problems, which we call computationally intractable, we cannot
*  expect that any entity is going to be able to behave rationally if it has to solve those
*  problems in order to get what it wants.
*  So humans don't behave rationally and we don't expect that machines will behave rationally.
*  The interesting question is how much closer to being rational can machines get than humans,
*  particularly taking advantage of their enormous computational power?
*  So already we have computers whose actual computational throughput is larger than even
*  the theoretical maximum throughput of the human brain.
*  And no one thinks that in fact the human brain really is able to use every single neuron
*  computing at maximum speed all the time.
*  So the interesting question is, are machines going to exceed the human capability for decision
*  making in the real world?
*  And when will that happen and by how much will it happen?
*  But interestingly, humans have developed over both evolutionary time and during their
*  lifetimes all kinds of incredible schemes for overcoming the computational difficulty of the
*  problem of deciding what to do.
*  And so even though we're not particularly good at playing Go, in fact a lot of games are
*  specifically designed to not be easy for our brains.
*  Our brains are actually extremely good at organizing our behavior into hierarchies.
*  So if you're writing a book, let's say, at any given moment your fingers are typing one character
*  of one word, of one sentence, of one paragraph, of a chapter of that book.
*  And this is a natural hierarchy.
*  Just typing one character on the keyboard might involve hundreds of motor control commands from
*  your brain to your arm and your hands and your finger as well as your eye to keep track of
*  what's happening on the screen.
*  If you think about what AlphaGo is doing, which is the Go program that beat the human world
*  champion, it's able to look ahead in time maybe 50 moves into the future, which sounds pretty
*  amazing.
*  But if you apply that to a robot or a human body where those 50 moves would be 50 motor control
*  commands to my muscles, that would only take you about a tenth of a second into the future.
*  So it would be completely useless for real decision making in the real world.
*  And humans, of course, we think usually quite a bit further than a tenth of a second into the
*  future, sometimes even years.
*  We plan to do a PhD, which is five or six years.
*  In other words, a trillion motor control commands are involved in doing a PhD.
*  So we're planning at many, many levels of abstraction and we do it kind of seamlessly.
*  Somehow miraculously, our brain always has something lined up for the present moment
*  so that if you're speaking, your tongue and your lips are saying the next word.
*  If you're typing, the next word is coming out of your fingers.
*  If you're going for a walk, the right things are happening for your legs to move in alternation.
*  And yet the same thing is happening at the scale of multiple seconds and minutes and hours and days
*  and weeks.
*  And it all feels seamless.
*  We're not aware of sort of context switching.
*  Now I need to think about what's happening in the next millisecond.
*  Oh, now I'm going to think about what's happening an hour and a half from now.
*  It's all very smoothly integrated and we really don't know how to get machines to do this.
*  But this is the main technique that humans use to manage the complexity of the real world.
*  Yeah, that's a really great summary of a whole bunch of podcast interviews that I've done
*  with people who do neuroscience and cognitive science and consciousness studies.
*  And absolutely the message comes through that human beings are these complicated networks
*  of subsystems, each using little heuristics to get through the day rather than some perfect
*  reasoning machine that is trying to play a very abstract version of Go.
*  But at the end there you said, and we're not very good at converting that into an AI algorithm.
*  Is this something that people are trying to do?
*  Is this a huge difference in the approach of conventional AI and where we eventually want to be?
*  So it's something that we've known about. In fact, Herbert Simon, who was both a psychologist
*  and an economist who won the Nobel Prize and an AI researcher, one of the early AI researchers who
*  really set some of the directions for the field, wrote a very famous paper called The Architecture
*  of Complexity, where he specifically talks about this device of hierarchical layers of abstraction
*  that help us to organize our behavior in time. And early planning systems going back to the mid-70s
*  attempted to implement some kind of hierarchical planning capability.
*  There is actually a fairly well understood ability if I give the hierarchy to the system.
*  In other words, if I tell it, okay, these are the primitive actions and then these are the actions
*  that use primitive actions to be implemented. So this is motor control command for your fingers.
*  This is typing a character. This is typing a word. This is typing a sentence.
*  We have algorithms that can construct long-term plans and people have used this to,
*  for example, organize the manufacturing process in a factory for a month. So that month-long plan
*  actually bottoms out at something in the order of 600 million manufacturing operations
*  that are going to take place over that month. The difficulty is that those hierarchies,
*  those abstract actions have to be provided by the human. So we are doing a lot of the work.
*  One of the big missing pieces in AI is how does a system develop that hierarchy and invent those
*  abstract actions for itself? There was a time when getting a PhD didn't exist. There was just
*  no such thing. Emailing someone, Googling someone, even a few years ago, those didn't exist.
*  We have a library of these things at all kinds of levels of abstraction from multi-year things
*  like getting a PhD or emigrating to the United States down to much shorter term things like
*  Googling something or emailing someone or texting. A lot of these things actually we don't invent
*  individually. They're gradually formed somehow by cultural processes and we inherit them.
*  In some sense then, the intelligence isn't really in the individual human. It's something that we
*  we've inherited from our culture and it's incredibly powerful. Without that vocabulary,
*  without that library of abstract actions, life would be intolerably complicated and we simply
*  wouldn't be able to have the civilization that we have because it would be too difficult to
*  navigate it and to run it if we had to think of everything in terms of just the primitive operations.
*  Yeah, I mean you give an example in the book about, I forget exactly the context, but there was a
*  question. A bunch of fourth graders are going to have a roller skating contest. What is the best
*  kind of surface that they should choose to move on? Gravel, sand, blacktop or whatever.
*  You talk about how much background knowledge is necessary to even think about such a question.
*  What does it mean to have a roller skating contest? What is the goal that the fourth
*  graders have and so forth? You seem to say in the book that right now,
*  our computers are really bad at that background knowledge. I had a conversation with Melanie
*  Mitchell on the podcast where she also argues about the lack of common sense in our AI algorithms.
*  Again, is this something where everyone knows this in AI and we're working hard and we think
*  we can crack it or is there a school of thought that says, well, it'll just come eventually if
*  we keep working on what we're working on now? That's a great question. We've known it for a
*  long time. There are papers going back to the 60s saying that absolutely, particularly in the
*  case of understanding language, that we need this background of common sense knowledge in order to
*  make the right decisions. For a long time, there's a field called knowledge representation where
*  people tried to actually capture the knowledge in mathematical form, typically in mathematical
*  logic, and computer algorithms are able to process logic in order to do reasoning.
*  We can even learn these logical representations from examples.
*  People found it quite difficult to get it right. For example, writing a description in
*  mathematical logic of the process of making omelets turns out to be pretty difficult to
*  get right. You can capture some parts of it with precise logical statements, but other parts of it
*  are quite resistant. It's hard to say what you mean by not runny but not too overcooked
*  and things like that. I would say that effort is kind of on hold right now.
*  There were valiant attempts to build up large-scale knowledge bases with lots of common sense,
*  but those have not turned out to be all that useful in practice. Right now, the AI community
*  is working largely on approaches based on deep learning. In deep learning systems,
*  there's no attempt to actually construct representations of knowledge. There's no
*  attempt to put in common sense at all. We simply take data and we feed in the data
*  and use the data to train very large tunable circuits to perform various tasks. You can
*  put in image data and train these circuits to recognize the objects that appear in the image.
*  Having trained an image recognition system on millions of photographs of animals,
*  that's all the system can do. It's now an animal recognizer, but it doesn't in some sense know
*  anything about animals. You can't ask questions like, well, which of these animals could pick
*  up a suitcase? It's totally outside the scope of what that large train circuit is able to do.
*  At the moment, I don't think there are any of these machine learning systems that
*  are capable of answering those kinds of common sense questions. You can make it appear as if
*  they do by, and this is another, I would say, failing of the current trends in AI.
*  You can just put in millions and millions of question-answer pairs like that,
*  and then you hope that if I give it a new question, that there's something similar
*  enough in the data set that it can cobble together some answer that is right most of the time.
*  There's a Japanese researcher, Noriko Arai, who has been able to train a machine learning system
*  to pass the entrance exam for the University of Tokyo, which is a very difficult and selective
*  exam that most students in Japan obviously fail to do because the University of Tokyo is
*  the premier university. She freely admits that the system has absolutely no idea about anything.
*  It doesn't understand any of the questions. It has no knowledge to speak of. It's just been
*  trained on enough examples and enough background text data that it's able to spot enough
*  statistical correlations between what the words are in the question and constituents in the question
*  to what the answer should be, but there's no reasoning process going on at all.
*  My guess is, and I think people like Demis Tsisabis, who's the CEO of DeepMind and one
*  of the authors of the AlphaGo system. Demis has said that deep learning is going to hit a wall,
*  basically, and we're going to have to go back and reintegrate all of the things that classical AI
*  worked on, the symbolic techniques, the logic, reasoning, knowledge representation, and so on.
*  The question is, how does that integration work? How does deep learning
*  get integrated with these kinds of symbolic techniques?
*  Whoever figures out the answer to that question is going to be able to make the next set of
*  breakthroughs in AI. That's a challenge for our listeners. Absolutely.
*  Let me pause for a second to talk about the Blinkist app. This is a wonderful little app
*  you can put on your phone, your other mobile device, and what it is is basically a way to
*  figure out what's going on in some of the best and most popular books ever written.
*  A 15-minute read will tell you the major points in what could be a really long and intimidating
*  read. I mean, we all love reading books, but there's two major problems. Number one, finding
*  enough time to do the reading you want, and number two, deciding which books you want to read.
*  Let's say all of your friends have been saying you really should read Zen and the Art of
*  Motorcycle Maintenance, but just from the title, it doesn't seem necessarily up your alley. Well,
*  you could go to Blinkist, you could get the lowdown on what's going on in that book,
*  and from there you could decide whether to dig in further. With Blinkist, you get unlimited access
*  to read or listen to a massive library of condensed non-fiction books, all the books you want and all
*  for one low price. And right now, for a limited time, Blinkist has a special offer for Mindscape
*  listeners. Go to blinkist.com slash Mindscape to try it free for seven days and save 25% off your
*  new subscription. That's Blinkist, B-L-I-N-K-I-S-T, blinkist.com slash Mindscape. Start your seven day
*  free trial, get 25% off. This is great because we have a lot of the prospects and also worries
*  about artificial intelligence and how similar it is to human intelligence on the table. So therefore,
*  let's just skip ahead to the question of should we be worried or concerned or optimistic about
*  the prospect of artificial super intelligence? Given that artificial intelligence is not very
*  good at understanding the questions on the Tokyo Entry Exam, should we be worried about AI becoming,
*  number one, is there a prospect that it will become much smarter than human beings? And number two,
*  is that a prospect we should be worried about? So these are two really important questions.
*  It's really hard to think of more important questions that we could be facing. So on the
*  first question, are we going to be able to create super intelligent AI systems? I would say that
*  we will be able to solve these obstacles. I think there are half a dozen major obstacles,
*  major breakthroughs that have to happen between here and human level AI. And I already mentioned
*  one of them, which is the ability of systems to form their decision making hierarchies,
*  which allow them to cope with complexity. And so if you think of that, that's sort of one breakthrough.
*  And as far as we can tell, there's about half a dozen of that scale that need to happen.
*  And it might be that once we have all those breakthroughs, the system still doesn't work
*  because there's something that we didn't think of. But I think at that point, we'd be pretty close.
*  And we also have to remember, it doesn't have to be more capable than humans along every dimension
*  in order to be something that we have to worry about. So just to give you an example,
*  chimpanzees, it turns out, have considerably better short term memory than human beings,
*  even for something that's very human, like a string of digits. So chimpanzees, I think,
*  can remember 20 digit telephone numbers without too much difficulty, and humans can't. But I think
*  chimpanzees still have good reason to worry about human intellectual capabilities, because we're
*  basically in the process of destroying them with the capabilities that we have. And in fact,
*  for many species on Earth, the existential risk that they face is entirely a consequence of
*  another species on Earth, namely us, that is more intelligent than they are.
*  So of course, it's reasonable to ask, if we create entities that are more intelligent than us,
*  is that a good idea? In particular, are we going to be able to retain control,
*  retain power over entities that are more powerful than we are? It's hard to find good examples
*  in nature of a less powerful species having power over us.
*  But that's the problem we're being asked to solve. So I think the public discussion of this topic is
*  confusing a lot of different things. So one is, is super intelligent AI imminent? In other words,
*  do I need to be worried right now that something bad is going to happen right now? And the answer
*  is no. AI systems, at least not in the existential sense of a risk to humanity. No, there is no risk
*  to humanity. But bad things are already happening with AI systems, even ones that are really,
*  really, really stupid, because they run on billions of computers, particularly the algorithms that
*  run on social media that select what you see, what you read, what you watch, what you listen to
*  for hours every day for billions of people. Those algorithms, I think, are already having
*  a serious negative impact on the world. Another question is, well, should we be worried
*  right now that something bad is going to happen in the future? And I think that's the right question
*  to ask, because the timelines that most people think about are on the order of decades. And I'm
*  actually a little more conservative. I would generally say, well, I expect human-level,
*  seriously risky AI capabilities more towards the end of the century rather than mid-century,
*  which is where most AI researchers think that will have them. So it's entirely reasonable to
*  be concerned about that, just as if we discovered a previously undetected asteroid
*  that was quite likely to hit the Earth in 60 or 70 years' time. It would be quite reasonable
*  to be worried now about that future event. And actually, we are already worried about that.
*  We already have a planetary defense agency. It's part of NASA. They are busy tracking all
*  these asteroids. They're trying to figure out what would we do if we detected a sizeable weapon
*  that really was on a collision course. And so far, we haven't found one that's on a collision
*  course. But so far, the statistics show that we've only detected about 30% of the objects
*  that are going to come close to the Earth and are large enough to be a civilization-ending event.
*  So don't be too complacent even about that risk. Now, the risk from AI is a little different from
*  an asteroid because the impact of an asteroid and why it would be a bad thing
*  are pretty clear and straightforward. Whereas with AI, it's a little harder to figure out exactly
*  how things might go wrong. And the same thing would be true if you ask the chimpanzees,
*  a few thousand years ago, okay, so you've got these humans, they're here, they're much smarter
*  than you. How is it all going to end? The chimpanzees would have a very hard time figuring out how it was
*  all going to end for them because in some sense, it doesn't really matter. Once you cede control
*  of the world and your environment and everything else to another species that really doesn't care
*  about you, then getting into precise details about how exactly it all ends seems sort of beside the
*  point. The point is let's not cede control to a more powerful species if we can help it.
*  So that's the sense in which I think it's reasonable to be concerned. We're investing billions of
*  dollars or hundreds of billions of dollars pushing forward a technology with no plan
*  for what to do when we succeed. Well, yeah, okay, I mean, that was great. And there's a lot going on
*  here. So I'm just trying to figure out which direction to attack in first. I mean, you mentioned
*  that we're just overwhelmed with artificial intelligence programs doing work for us already.
*  None of them are anything that you would call super intelligent. And so there is obviously a
*  risk just from not understanding what they're doing. But that's a different risk than I think
*  that you're highlighting here at the end in a more intelligent species than us. Can we be a little
*  bit more definite about things like species here? I mean, how do you imagine this super intelligent
*  AI existing being embodied? Is it someone literally writes a program in C++? Or is it
*  sort of emergently arising out of the internet? Is it in a robot? Is it distributed in the cloud?
*  What should we be visualizing? So I certainly think that the typical science fiction depiction,
*  for obvious reasons, is that it's in the head of a single robot. And I think that's a huge mistake.
*  It's extremely unlikely that that's how things would go. So it's much more likely that it would
*  be a composite system drawing on computational power of the entire cloud or a good fraction of it.
*  Some people would say that the negative consequences could emerge from the sort of
*  unanticipated interaction of many different systems. And we've already seen this in the
*  so-called flash crash, which was when a lot of trading algorithms on the stock market
*  somehow interacted in a way that we still don't really understand. And then in the course of
*  about 20 minutes, they wiped a trillion dollars off the value of the stock market. And we had to
*  shut the stock market down. And we had to undo all those trades. And then, fortunately, the stock
*  market had these built-in circuit breakers, which allowed the intervention to take place.
*  But when that kind of thing happens, it has an effect in the real world. It really shook
*  the confidence of investors in the reasonable operation of the market. And it could have been
*  much worse. So these unanticipated interactions are a possibility. But I think the failure mode
*  that we anticipate is a consequence of the standard model of AI, whereby we make this optimizing
*  machinery and we put in objectives. And then it turns out that the objective is incomplete or
*  incorrect in some way. And this is not a new story. We go back to King Midas,
*  who said, I want everything I touch to turn to gold. And so that's the objective that he put
*  into the machine, so to speak. And he got exactly what he asked for. And then he realized that now
*  his food and his drink is turning to gold and his family is turned to gold. And then he dies in
*  misery and starvation. So the standard model is, in fact, I think, an engineering mistake.
*  It's a way of creating systems that relies on perfection on the part of humans in our ability
*  to specify objectives. And that's a really bad idea to assume perfection on the part of humans.
*  Perfection on the part of humans, particularly when the thing you're putting an objective into
*  is potentially more powerful than human beings are. So it could have physical appendages,
*  so it might reside in the cloud, but it could still have physical appendages with which it can
*  bring about changes in the world. But it doesn't even need to do that. When you think about Adolf
*  Hitler and the changes he brought about, it wasn't because of his physical appendages. It was because
*  he basically did it with words. And AI systems can have impact on the world through words,
*  through communication and the internet, as they already are, as social media algorithms are already
*  impacting the world, even though they have no arms and legs, and they have no laser guns and
*  nuclear bombs and all the rest. Yeah, but I think this is exactly what I want to sort of,
*  maybe it's an unfair question, but I want to really try to drill in on the physical manifestation of
*  this. I mean, there is the threat from artificial stupidity, as you said, algorithms that don't
*  really do their job well or are biased or whatever. Yeah. So what I'm saying is precisely
*  not that the algorithm is stupid, that it's not doing its work correctly, is that we are specifying
*  its work incorrectly. But it, the algorithm, is extraordinarily capable at carrying out
*  the assigned objective, the assigned task, in ways that turn out to have extremely bad side effects.
*  So if you don't believe that's possible, then just think about the fossil fuel industry and imagine
*  the fossil fuel industry as an algorithm. Right now, it happens to have human components
*  that are replaceable and are replaced on a regular basis. But as an algorithm, it's trying to optimize
*  the objective of generating a discounted stream of quarterly profits or whatever it might be,
*  and is in the process of destroying the world. And we are unable to stop it.
*  So this is a failure mode that we are already familiar with. And it can happen with AI systems
*  just as much as it can happen with corporations that are optimizing an objective and
*  neglecting the side effects. Right. But somehow that doesn't, I think we all agree that does not
*  count super intelligent, the fossil fuel industry. It's kind of, that's the stupidity of the
*  I was thinking of, not ineffectualness, but lack of self-awareness, self-reflection. It's just doing
*  its job. Right. I think maybe I'm misunderstanding, but I think when people use the word super
*  intelligent, they really are imagining something more human-like, right? Something that knows what
*  it's doing and wants to do it. Maybe it's not wanting to do the right thing. But I think
*  it has a little bit more self-control. And I'm wondering, would things like that exist? Where
*  would they exist? How would they manifest their control in the physical world?
*  I think there's a tendency to anthropomorphize. And we see this in a number of commentators.
*  So Steven Pinker, for example, Melanie Mitchell is another one. And I think that's a good
*  point. Who assert that it's intrinsic in the nature of intelligence that a sufficiently
*  intelligent entity is going to act in a way that's beneficial to human beings.
*  And I see absolutely no justification for this a priori. For example, right, there are
*  millions of species on earth. Some of them are much more numerous than human beings. Why wouldn't
*  the AI system decide to be beneficial to Antarctic krill? There's probably a thousand times more krill
*  than there are humans. So why not be beneficial to them? Or why not be beneficial to bacteria?
*  Or why be so parochial? What's wrong with being beneficial to an alien species on some star
*  on the other side of the galaxy? So I think the onus is on those who believe that somehow there's
*  this magic connection between the capability for rational decision making and the consequence of
*  being beneficial to humans. There is no such magic connection. It has to be designed in.
*  And that's really what human compatible is about, is how do we design in that magic connection
*  so that the more intelligent the AI system, the better the outcome for human beings specifically,
*  not for aliens on the other side of the galaxy and not for Antarctic krill, but for human beings.
*  Yeah, no, I'm completely on your side and thinking there's no natural tendency toward having AI
*  be beneficial to humans. I'm just trying to wonder how vivid can we be about
*  toward having AI be beneficial to humans. I'm just trying to wonder how vivid can we be about
*  how this AI would hurt us? Would it be just massively misdirecting the food supply? Would
*  it be a million subtle interventions onto social media? Is this something we can even
*  say anything about or we should just be worried across a broad spectrum of bad outcomes?
*  So the difficulty with, you know, so I can describe scenarios and of course, since I can describe
*  them, you can always say, well, okay, then we'll just make a rule against that. Right. And then,
*  of course, that scenario won't happen, but another scenario will happen. So the kinds of examples
*  that you see commonly involve, for example, side effects that modify our physical environment.
*  And this is sort of what the fossil fuel companies are doing in terms of adding carbon dioxide to the
*  atmosphere. And so you could imagine that, for example, you want to fix that problem, you say,
*  okay, I would really like carbon dioxide levels to return to their pre-industrial concentrations.
*  And that sounds like a great goal. And it's a perfectly reasonable goal to state to another
*  human being who already shares all of the other background preferences that humans have for the
*  future. But if that's the sole objective, then there are many ways of achieving that objective.
*  For example, probably the simplest way is to say, well, where's all the carbon dioxide coming from?
*  Oh, it's coming from the economic activities of humans. Okay, well, let's get rid of the humans.
*  And so you say, okay, well, I didn't mean that. What I meant was, you know, restore the carbon
*  dioxide levels and don't kill any people. Fine. Okay, then we'll have a decades-long social media
*  campaign which convinces people that it's immoral to have children because those children are
*  what's responsible for the gradual destruction of our planet. And so we all stop having children
*  and the human race goes extinct and the AI system has solved its problem without killing any people.
*  And then, you know, if there's anyone left to have a third wish, then they come up with a revised
*  version of that and then the solution to that problem kills them off. So the issue is that we
*  haven't noticed this problem up until recently because our intelligent systems have been not
*  very intelligent. They're mostly in the lab. They're mostly working on toy problems. And so they
*  don't have consequences on the world. And if they start misbehaving, we have an off switch. We switch
*  them off. In fact, every robot above a certain size is legally required to have a big red off
*  switch, usually on the back, so that if it starts misbehaving, you can switch it off in an emergency
*  or even a remote control off switch. I did not know that. But once you get outside the lab,
*  you know, the effects as with social media algorithms that are directly operating on the
*  real world can be enormous. And you also have to understand that the off switch, you know,
*  is often people often say, oh, well, if something really bad happens, we can just switch it off.
*  But of course, that's like saying, you know, if I'm losing to AlphaGo, I'll just play a better move.
*  Right? Well, sorry, whatever better move you might think you have, AlphaGo has already thought of it
*  and has a way to refute it. And whatever attempt you might make to switch off the machine,
*  the AI system has of course anticipated that that's a possible failure mode, right? One of the most
*  obvious ways of not achieving your objective is that you're dead, right? You can't fetch the coffee
*  if you're dead. So the system has already taken preemptive steps to prevent that failure, because
*  it's very good at achieving the objectives that we give it, not because it really wants to be alive.
*  There's nothing to do with self preservation. There's no instinct. It's a logical consequence
*  of having an objective that's fixed, that a system wants to remain alive in order to achieve the
*  objective. So I guess there's no reason to keep the audiences in suspense anymore. I mean, the real
*  purpose of your book is to actually propose a new strategy for dealing with exactly this problem.
*  You think that we should be giving our AI systems a different kind of goal than we usually do?
*  Yes. In fact, you could argue we should not be giving the AI system a goal,
*  at least not one that is precisely defined and known to the AI system, because it's exactly
*  when the AI system believes that it knows the objective correctly that whatever action
*  it comes up with in furtherance of that objective, it then sort of believes that this is the correct
*  action to do and doesn't tolerate necessarily interference from people who are jumping up and
*  down saying, you know, stop doing that, you're destroying the world. From the AI system's point
*  of view, that's just noise, right? It's just me, you know, my mouth flapping open and closed.
*  So what? It's pursuing the optimal solution to the objective that we gave it. So the solution
*  that's proposed in the book has two main parts. The first part is that we design systems in such
*  a way that their only objective is whatever it is that humans want the future to be like.
*  So we use the word preferences, which is the term that economists use, but it doesn't just mean like
*  preferences between different kinds of pizza. It really means, you know, out of the possible futures
*  that the way the world could unfold in future, how would you like it to unfold?
*  And so this is what the AI system is supposed to be helping us with. But the second part of the
*  solution is that it knows that it doesn't know what those preferences are.
*  And this avoids the problem of a machine that is given a fixed objective and believes that
*  that is the only objective and therefore has to be pursued at all costs. So if we say to the AI
*  system that we don't like what it's doing, we're conveying additional preference information
*  to the machine, and it then is rational for the machine to revise its plan, because now it's
*  learned a bit more about what we want and don't want. And if it comes up with a plan that says,
*  OK, I can fix carbon dioxide by getting rid of all the people. So it knows that we want to fix
*  the carbon dioxide. Let's say it doesn't know whether the people want to be alive or dead.
*  Well, what's the rational thing for it to do? If it just wants to optimize the carbon dioxide,
*  then it just kills all the people. If it knows that it doesn't know whether the people want to
*  be alive or dead, then it's reasonable. In fact, it's rational for it to ask permission. It says,
*  I've got this plan. Here's how we solve it. We kill all the people, and then carbon dioxide goes
*  back to normal. And then you say, no, that's not quite what I meant. So these solutions like asking
*  permission, deferring to human instruction, and also allowing oneself to be switched off,
*  these behaviors don't have to be programmed in. We don't have to put special rules and regulations
*  into the AI system to make it do that. Those behaviors are just a logical consequence of the
*  way we frame the problem. They are rational for the AI system to do. It's rational for it to ask
*  permission. It's rational for it to allow itself to be switched off because it doesn't want to do
*  whatever it is that would cause us to switch it off. And it doesn't know what that might be.
*  But if there's a danger that it might do something we really don't like, then it would prefer to be
*  switched off in order to avoid that from happening. Yeah, I certainly like the idea of this initial
*  uncertainty in what it thinks the humans would prefer. Is this something that just by the way,
*  have you written AI algorithms that have this feature and turn them loose and watch them behave?
*  Yes, in tiny little worlds. And the mathematical description of this, we call it an assistance game.
*  So the word game is a general term that economists use to mean any situation where there are multiple
*  entities that are making decisions. And here, we could imagine just two entities, a human being and
*  a machine. And the machine's objective is whatever it is the human wants, that's what I want.
*  But the machine doesn't know what that is. And so you can set up that game. And for example,
*  you can make a little grid world, and you can put a human in there, and there's a simulated human
*  and a simulated robot. And you can solve the game, you can calculate what is the solution to this
*  game for both the human and the robot. And when you look at the solutions, you can see that
*  you see that in fact, the human tries to teach the robot. Sometimes the human shows the robot what
*  not to do, right? So basically kind of takes the robot by the hand and says, look, you could go
*  over here, but there's a big pit, don't go in there. And then you should go over here, and this is
*  where you should sit, because this is a nice place to be. And the robot, other versions of the game,
*  the robot asks permission. In some versions of this game, the robot and the human actually devise a
*  little protocol where the robot kind of comes and asks a question, and the human gives them a yes,
*  no, and then the robot goes away and does the right thing. So we're just at the beginning of this
*  process of exploring the nature of solutions to these kinds of formal methods. And so we're
*  at the beginning of formal mathematical problems. But what we've seen so far is that first of all,
*  the kinds of behaviors that the robot exhibits are exactly what we hope. They defer, they ask
*  permission, they learn from the human about what the human wants, and they help the human achieve
*  whatever it is the human wants to achieve. And interestingly, right, the one way of thinking
*  about it is that this game is a strict generalization of the classical notion of
*  a machine pursuing a fixed objective, because now it's not a fixed objective, it's an uncertain
*  objective rather than a certain objective. So it's strictly a more general problem-solving
*  situation, and the kinds of behaviors that are exhibited are much richer and more interesting
*  as a result. It certainly bears a family resemblance to Bayesian inference, right,
*  where we have some set of priors with the probability of all them, and then we update
*  on the basis of more information. So I'm wondering, would we expect that such a system would
*  become less and less uncertain over time about what it thinks the motivations are? I mean,
*  do these systems grow old and crotchety and harder to change their minds?
*  In a sense, yes. I think in a practical sense, it's pretty unlikely that machines would ever
*  acquire enough information to be able to predict our preferences,
*  particularly about things that have never been experienced in the real world.
*  For example, you can look through, there are whole books written about what people want,
*  and the development economists write these books, and moral philosophers write these books.
*  People come up with long lists of what are the needs of human beings. But in none of those books,
*  will you find what color do people prefer the sky to be? And that's probably not the case,
*  because no one's bothered to change the color of the sky to find out how upset people are as a
*  result. So it's unlikely that an AI system is going to be able to predict our responses to
*  changes in the color of the sky, other than just sort of being generally upset that it's not what
*  it used to be. But maybe we'd like to see what the color of the sky is, and we'd like to see
*  what the color of the sky is. So there's a fundamental fact that there's a lot we don't
*  know about our own preferences. So there's genuine, what we call epistemic uncertainty,
*  meaning that it doesn't matter how much I think about it, I actually have to go out and experience
*  something. I have to get real, actual empirical experience in the world, in order to learn more
*  about my preferences. And there's a recent book by L.A. Paul, who's a philosopher,
*  called Transformative Experience, and she uses the example of the durian fruit.
*  We just had Laurie as a guest on the podcast, and we talked all about transformative experiences here.
*  Right. So independently, I came up with the durian fruit as an example of this. So it's a
*  fruit that's extremely smelly, and some people absolutely love it, and they think it's the most
*  marvelous food on the surface of the earth. And there are other people who utterly despise it.
*  And there have been cases of where there was a cargo of durian on an airplane, and some of the
*  passengers could not stand it, so they actually mutinied on the airplane and forced the captain
*  to go back and land at the airport and unload the cargo of durians, because it was so unbearable.
*  So it's clearly something that elicits either extremely positive or extremely negative
*  preferences, but I have no idea which one I am, because I've never tried it, I've never smelted.
*  So I have real epistemic uncertainty about how I would enjoy a future where I'm eating lots of durian.
*  So very similar kinds of arguments apply to much more practical kinds of things, like, well,
*  imagine a school leaver, would you like to be a coal miner or a librarian? Those are the only
*  two jobs we have right now, lad. Coal miner, librarian, which is it going to be? Of course,
*  at 16 years old, you have no idea how much you're going to enjoy being a coal miner or how much you're
*  going to enjoy being a librarian. So you have some vague feelings about it, you might have seen
*  references to these professions, and you've got some images in your mind and little bits of evidence
*  here and there, but of course, you could certainly be wrong if you made one prediction or another.
*  So this real uncertainty about human preferences within humans means that the real
*  human preferences within humans means that there's no practical way that the AI system
*  is going to reach a situation of perfect knowledge. But the way Bayesian inference works, actually,
*  is that unless you make certain kinds of mistakes in the way you set up the problem at the beginning,
*  the Bayesian process only reaches certainty when it's correct. So
*  as long as you make sure that your prior beliefs are sufficiently broad
*  as to encompass every possible human preference structure, which is a tall order, I agree,
*  but let's say if you can do that, then you only approach certainty as you approach having correct
*  beliefs about the human preference structure. So in that situation, you might not mind too much,
*  you know, the AI system stops asking permission because it knows what you're going to say,
*  so it doesn't need to ask permission. So it becomes sort of like the perfect butler.
*  And if you've read P.G. Woodhouse and his books where Jeeves is the butler and Bertie Wooster is
*  the aristocrat, Jeeves actually in some ways knows Bertie Wooster better than Bertie knows himself
*  and always anticipates what his master needs and wants and manages to do it in advance.
*  So it would be a little bit like that. But I think, as I say, it would be very unlikely that
*  we would approach any degree of certainty in any finite amount of time. How much do we have to
*  deeply think about the idea of a preference? I mean, in the usual, in the standard model,
*  I guess, of AI, where you just program in a utility function, that is operationally what you mean.
*  But here you're using the word preference to mean something about human beings, right? It's the
*  human preferences that are supposed to be learned by the AI. If we push it hard enough to implement
*  in software, is it even clear what human preference is? I mean, not only do humans not know what their
*  preferences are, they might change, they might be inconsistent, internally incoherent. Are there
*  ways to deal with this? Yeah, so these are great questions. It's certainly the case that when
*  economists or behavioral economists do a lot of experiments to try to figure out the actual
*  preferences of humans, even for something as simple as money, so let alone the color of the sky or
*  what kind of pizza you want, but just money. How much do you like money? And risks involving money,
*  money today versus money tomorrow. And I would say that the consensus of these experiments
*  is that consistency of preferences seems to be fairly well supported.
*  And so consistency meaning that you do appear to be able to rank different outcomes in a consistent
*  way. But we don't exactly seem to follow some of the, at least straightforwardly, if you interpret
*  the other axioms of rationality, we don't quite seem to follow those. And we seem to have our own
*  peculiar ways of making decisions. And Daniel Kahneman, who's a leading psychologist and another
*  Nobel Prize winner in economics, has studied actual human preferences, and we seem to have
*  actually sort of two minds. So his explanation is that there's an experiencing self,
*  which is sort of the moment to moment amount of experience that we have. And so
*  the moment of enjoyment or pain that you're experiencing. And then there's a remembering self.
*  And in standard economic theory, the remembering self is sort of supposed to add up the
*  experiencing self experiences and say, okay, well, that's how good this was. It's the sort of the sum
*  of all the pleasures and pains that I experienced. But it turns out empirically that the remembering
*  self does something quite a bit different. So in particular, the remembering self really remembers
*  the most pleasurable, most painful part of the experience, and also the part that was most recent.
*  So they call this the peak end theory. So the peak and the end of the experience
*  seem to be very salient in how you remember the desirability or undesirability of something.
*  And that's pretty hard to reconcile with standard economic models. But actually,
*  when you think about it, it's clear that memory and expectations are quite reasonably folded in
*  to human decision making. Because if I have a bad experience, I might remember that for my whole life.
*  And so it isn't just the experience itself that was bad. It's the recurring memory of it
*  that's going to be bad. And that recurring memory is going to remember the worst thing.
*  Right? So if I ask you, what was the worst thing that ever happened in your life,
*  probably maybe three or four things pop into your head. And they're things you think about
*  every so often. And some people even have to go through psychiatric treatment to try to extinguish
*  some of these memories that are ruining the rest of their lives. So it might be that, in fact,
*  what the remembering self is doing is perfectly rational if you incorporate memory and expectation
*  into how you evaluate the costs or the benefits of some experience. So I would say that at the
*  moment, we're a long way from understanding the rich, many layered nature of human preferences
*  and so on. But if we really are inconsistent, so if, for example, if our transitive are,
*  if our preferences are intransitive, in other words, they kind of go around in circles,
*  then there's nothing the AI system can do because, you know, any pizza the AI system gives you,
*  you say, well, actually, I prefer this other one. And you the AI system gives you that one.
*  It's not actually I prefer the first one. And of course, you'll never be satisfied.
*  And there's really nothing that any discipline of building artificial systems could possibly do
*  to satisfy inconsistent preferences. So but we, you know, we can give you a pizza, as you know,
*  as opposed to no pizza at all, right? You probably prefer some kind of pizza to starving to death.
*  So we'll make sure you get some kind of pizza. We might end up learning a lot about psychology
*  from the way that the AI determines what our preferences are in practice, which might be
*  different than what we say they are when we try to state them. Yeah, I was gonna say I think that
*  this is probably the conceptually the most difficult part of the research agenda that
*  I'm proposing is the gap between the idealized model of a human that has stable preferences
*  and consistent preferences about the future and the reality of actual humans.
*  And I think particularly stability is conceptually very difficult to deal with. If a
*  human being's preferences can change, in other words, what I want tomorrow to be like
*  today is different from what I want tomorrow to be like when I get to tomorrow.
*  Then which of my two selves is the AI system supposed to satisfy myself today or myself tomorrow?
*  It's hard to pick apart that problem philosophically. And then practically, if human
*  beings' preferences can change, which clearly they do, we're not born with a whole complex set
*  of preferences, then how do you make sure that the AI system doesn't satisfy preferences by
*  changing those preferences to make them easier to satisfy? Well, what I was going to say was how do
*  we be sure that the AI won't just change its mind about what its preferences are to satisfy
*  the human preferences? If we really are imagining AIs that are super intelligent, much less just
*  intelligent, can we really also assume that we're baking in their fundamental motivational
*  structure or is that something subject to editing on their own part? So this is an
*  interesting set of questions having to do with our ability to prove mathematical theorems about
*  the software that we build. So we already have the capability to prove that algorithms are correct,
*  that they behave according to some specification, and this capability is getting more and more
*  sophisticated. And we use it even in areas like machine learning, which you might think
*  how could you possibly prove anything about an algorithm that learns? But it turns out that you
*  can. And you can, typically we're able to show that we expect to get a performance within some
*  small epsilon of the desired performance and that will happen with very high probability.
*  So that's the kind of theorem that we prove all the time.
*  So the idea here would be we would set up the general framework for how the system operates,
*  and it would have learning components strung together in the right way. And then what you
*  prove is that no matter how good each of those components becomes, the system as a whole still
*  conforms to this required design where it satisfies these principles. There are some
*  tricky parts to this. So traditionally when we prove theorems about software, we're kind of
*  assuming that the parts of the program that we want to remain fixed remain fixed. And you can prove
*  that this piece of software can never overwrite itself and change its sort of constitution,
*  so to speak. But there's another set of theorems you'd have to prove, which is that there's no
*  circumstance under which the software would convince a human being to go in and overwrite
*  the constitution. And that's a much more difficult kind of guarantee to provide.
*  And this comes about, you know, we've noticed this in computer security where we prove that
*  security protocols are correct, but then we find out that there's what we call a side channel.
*  And side channels include things like, you know, listening to the sound of the keyboard
*  by bouncing a laser beam off the window of your office building or measuring the electrical
*  current in the main supply that's going into the computer, and then being able to extract
*  information from these channels. And when you put an AI system into the real world, you
*  automatically create this side channel, which is that the AI system can convince a human being
*  to make physical changes to the memory of the machine and its software. And we have to make
*  sure that that side channel is somehow cut off.
*  This is a lot to think about, I gotta say. This is a very good episode for food for thought
*  purposes. I'll just close with just giving you a chance to sort of speculate about the
*  future. I mean, what do you think is going to be the vision of AI that comes true 50 years from
*  now? I mean, what should we be looking for overall, given all that we've talked about over the last
*  hour?
*  So assuming things go well, so assuming we figure out how to design AI systems in such a way that we
*  retain control over them. And I think this is actually feasible. There's a lot of very hard
*  algorithm design and engineering work to be done to take the basic framework that I've described
*  and turn it into technology that will replace and supersede all of the AI technology that's already
*  out there. But assuming that works and assuming that we overcome these conceptual obstacles and
*  achieve human level or sometimes called general purpose or super intelligent AI, that's a
*  tool that enables us to have a much better civilization than the one we currently have.
*  And our civilization is sort of the best we can do with the brains that we have. But if we had
*  access to much better brains, even if they don't belong to us, we get to use them and we can
*  have a better world than the one we have right now. We could, I think quite easily without
*  imagining the sort of sci-fi advances of eternal life or fast and light travel,
*  curing all disease, but just using AI and robotics technology to deliver the goods and services that
*  well off people in the West take for granted. So giving that sort of standard of life to everyone
*  on earth would be about a tenfold increase in the GDP of the world, which when you calculate the
*  sort of cash equivalent value, what the economists call net present value, it's 13 and a half trillion,
*  sorry, 13 and a half thousand trillion dollars. So just for comparison, the GDP of the US is on the
*  order of $20 trillion a year. So we're talking about hundreds of times larger than the GDP
*  of the US or in fact the GDP of the world. So that's the cash value. And when you look at
*  the investments, the tens or hundreds of billions of dollars that people are talking about,
*  it's absolutely minuscule in comparison to the potential benefits. So we could add a little bit
*  of that. So we could enter a golden era in a way where we no longer have to fight about access to
*  the wherewithal of life, which is one of the main reasons we've been killing each other since the
*  beginning of time. I mean, there are other reasons like religion that we kill each other, but at
*  least we would get rid of this reason. So some people have said, look, if we have this AI,
*  that can do everything that human beings can do and sort of can do it for us essentially for free,
*  then what's left for human beings? What role do we have? Where do we find
*  a useful purpose in life? If there's nothing that we can do that's better than what the machine can
*  do. And I think this is a really important question for us. And presumably, if the machines
*  understand our preferences, they know that we don't want a future of idle enfeeblement,
*  where we essentially become couch potatoes for the rest of time, where we don't learn, we don't
*  try, we don't do anything of any value with our lives, because that's sort of not what we want
*  the future to be like. So the AI systems will have to say, at some point, no, we're not going
*  to keep tying your shoelaces for you. You humans have got to learn and keep learning to do stuff
*  for yourself. So that's going to be an interesting discussion to have in a few decades time.
*  **Matt Stauffer** Well, you've certainly given us a very good set of reasons to believe that we
*  should all be thinking hard about this and trying to figure out what's going to happen next. Stuart
*  Russell, thanks so much for being on the Mindscape Podcast. **Stuart Russell** Pleasure, Sean. Very
*  nice talking to you.

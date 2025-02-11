---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 5764s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 4195
Video Rating: None
---

# BI 060 Michael Rescorla: Mind as Representation Machine
**Brain Inspired:** [February 11, 2020](https://www.youtube.com/watch?v=_ZvH5_RH630)
*  Philosophers for hundreds of years talked about mental representation, but there wasn't
*  the science that they could draw on of mental representation.
*  So it was really just armchair.
*  I don't want to say speculation because it was grounded in introspection and in tight
*  arguments but there wasn't an experimental basis.
*  Still in an armchair.
*  Yeah.
*  Yeah, it was still in an armchair, exactly.
*  By and large, the most central concept of representation in philosophy has been the
*  idea that the mind represents the world as being a certain way.
*  And this is really the essence of representation.
*  Turing was a brilliant logician and a brilliant thinker, one of the greatest thinkers of the
*  20th century.
*  That's a safe statement.
*  Yeah, that's a safe statement.
*  But...
*  This is Brain Inspired.
*  How are the physical things and processes in our skulls related to the things that they
*  purportedly represent?
*  How do the layers of a neural network relate to what they represent?
*  What does it mean to represent something, and is representation necessary to explain
*  intelligence?
*  Hello, everyone, I'm Paul Middlebrooks.
*  Questions of spoken words and ink and keyboard tapping have been spent on these questions.
*  In neuroscience and AI, we often use the word representation rather loosely to be generous.
*  And this has been well documented and I am definitely guilty of it.
*  But in philosophy, the concept of representation has been pondered forever, basically, and
*  it's still at the heart of many debates in the literature.
*  That's right, good people.
*  We're talking about representation and its role in philosophy, neuroscience, and AI.
*  And I convinced Michael Rescorla to help me sort it all out today.
*  Michael is a professor of philosophy at UCLA, where he works on philosophy of mind and science
*  and computation.
*  And as you'll hear, he also has deep interests in Bayesian approaches to cognition and spatial
*  navigation.
*  So he has a good grasp on many subjects in neuroscience and cognition.
*  We take a winding path during our discussion and talk about the nature of representation,
*  the role of philosophy in general, levels of computational explanation, and we talk
*  at length about the role of representation in computation in minds and in machines.
*  If you have a philosophical bent like me, you will enjoy this, I think.
*  I apologize to those of you who don't, however.
*  One of the reasons I had Michael on is because I'll be talking next episode about representations
*  with respect to analyzing brain activity and deep neural network activity.
*  That'll be with Jürgen Diedrichsen and Nico Kriegeskorte.
*  So this episode hopefully will serve as some sort of primer for that upcoming episode as
*  well.
*  Quick update on the Brain Inspired course.
*  I aim to have the first module ready and released by mid-March.
*  It'll cover roughly the zoo of neural networks that are being used today and how they relate
*  to brains and how and whether they're good models of neural circuits.
*  So it'll be the first version of that with many other modules to come after that.
*  Jürgen, Arti, Jacob, Joe, Jeff, and Asya, I hope I'm pronouncing that correctly, you
*  guys and the rest of you who support the show on Patreon will of course be getting the course
*  as it's made and helping me improve it.
*  So I'll keep you posted as progress occurs and thank you so much for your support on
*  Patreon.
*  During our conversation, Michael suggests multiple books during today's episode and
*  I'll link to those in the show notes as well as the handful of Michael's work that we
*  covered today and I'll link to his website as well where he has links to the rest of
*  his work.
*  His writing is really clear and enjoyable so you should check it out.
*  I've really enjoyed diving deep into all of his work.
*  Show notes are at braininspired.co.
*  slash podcast slash 60.
*  All right, here's my conversation with Michael Rescorla.
*  When I was I think maybe 13, maybe 12, 13, 14, my friend and I would ride our bikes
*  up to the local pool.
*  We'll call it a public pool.
*  It wasn't quite public but he and I were swimming in this pool and across the way there are
*  these two cute girls and they were like looking at us and they kind of, you know, we were
*  shy and they swam over to us and we're kind of excited about this and once they got over,
*  one of the girls said to me, when we were over there, we came over because we thought
*  you were cute but now that we're closer, we see it's your friend that's the cute one.
*  And I feel like in that story sometimes I feel like I am philosophy and my friend is
*  neuroscience sometimes and this is a terrible way to introduce a philosopher to the program,
*  I know.
*  But it gets better.
*  Thank you, Michael, for being here and welcome.
*  It's a pleasure to be here.
*  So can you be my therapist for just a minute here before we get into things?
*  A quick therapy session.
*  Sure.
*  Okay.
*  Because I have a challenging relationship with philosophy and I love it.
*  So okay, so I'm preparing this course on sort of the interface of neuroscience and AI and
*  I'm going through like the different types of neural networks that are kind of popular
*  these days as models for brain processing and I'm reading about the philosophy of models
*  and modeling.
*  You know, it's great, you know, you read about how models can be descriptive, they're
*  used to predict things, they can have explanatory power and so on.
*  And then I start getting into the ontology of models, you know, like what is a model?
*  I start reading about like the fictional view of models that equates models to something
*  that a writer creates like Sherlock Holmes.
*  You know, and five minutes later I'm reading about what fiction really is.
*  And then I think, you know, where am I?
*  How did I get here?
*  How was I taken here by this philosophy?
*  And all of a sudden I'm upset at philosophy for wasting my time.
*  You know, I could have just been using a model, right, and then actually doing stuff instead
*  of dancing around the idea of it.
*  But you know, at different time I'm also working on the course.
*  I'm reading about the computational theory of mind and representations and how do networks
*  of neurons or artificial networks of neurons represent things and how we get from neurons
*  and circuits to the content that they represent.
*  And it's all relevant and it seems important and I'm happy again with philosophy.
*  Is this something I'm just going to have to accept in my relationship with philosophy?
*  I think philosophy is really like any discipline.
*  Some of the work is better than others.
*  Some is more helpful than others and some will address the concerns you have going into
*  it and others will not.
*  So just like in math, you might get really into topology and not be so interested in
*  number theory or you might be really interested in probability theory and not interested in
*  algebraic geometry.
*  There are different things that are to different people's taste.
*  So it sounds like maybe the general philosophy of science literature that you were alluding
*  to in the first part of your question about the nature of scientific explanation, the
*  nature of scientific modeling, maybe is not...
*  That's not your cup of tea, but there's still a lot else that's out there in philosophy
*  besides that.
*  I mean, I like that general philosophy of science literature that you're alluding to,
*  but not everyone...
*  Well, I hope so.
*  Yeah, yeah.
*  But it's not...
*  I can see why if you're coming at this where your concern is the mind or the brain doing
*  a neural network modeling of the mind or talking about AI, why those sorts of general philosophy
*  of science questions might not interest you.
*  And I do think there's a lot in philosophy that is relevant and you were touching on
*  it at the end of your question there.
*  So the notion of mental representation, I think, has been a really central one to philosophy
*  for...
*  Oh, forever.
*  Over a thousand years, I mean, a really long time.
*  And philosophers have had a lot to say about it and a lot of what they have said has trickled
*  the discussion of it in AI, in cognitive psychology.
*  And I think it can continue to inform it.
*  So I think if you look in the right place, you do find a lot of work that connects with
*  more of the kinds of concerns that you're interested in, such as research on the computational
*  theory of mind, the representational theory of mind.
*  So it seems like...
*  And I should say, I'm not talking to, quote unquote, just a philosopher here, because
*  you're interested in Bayesian approaches to understanding computation and mental representations
*  and brains.
*  And we'll get into all that.
*  But it seems like there have been waves of popularity of philosophy among scientists
*  over the years.
*  So if you go back to 1912, you have Bertrand Russell extolling the virtues and the values
*  of philosophy, saying that it shows...
*  You can use philosophy to show unexpected possibilities and things.
*  And he talks about freeing us from the tyranny of custom, meaning the way that we generally
*  conceive of things is probably not the way the things really are.
*  And we can free ourselves from that.
*  He also likes the idea that relieving us from our trivial concerns of the day, like, I don't
*  need to remind myself for the 18th time.
*  What do I need to make for dinner tonight, for instance?
*  And then fast forward over 100 years, and now...
*  Not that there's been one wave, but now I feel like there's this new wave of interest
*  in philosophy from the scientists, and especially from the science of brains and minds and intelligence.
*  And you have papers coming out, like there was one in 2019 that listed four or five virtues
*  for roles of philosophy in science.
*  Things like clarifying scientific concepts, critically assessing some assumptions, and
*  so on.
*  And it's been a trend, I think, I know this is a long rant here, but it's been a trend,
*  I think, for a while now for philosophy to take scientific practice as a starting point,
*  and use how science is actually done by practicing scientists to then start asking philosophical
*  questions.
*  And you do, and you do well.
*  First of all, is this an approach, this last approach I was just talking about, using the
*  practice of science, is this an approach that was brought in by, because of Thomas Kuhn,
*  from the structure of scientific revolutions and his ideas?
*  I mean, and if so, how did it differ previous to that, and why is it a popular method now?
*  So I think there are several different ways that philosophy relates to the sciences of
*  the mind.
*  One that you were gesturing to before is as a source of ideas or concepts, so the notion
*  of a mental representation is a good example where you see this playing such a central
*  role, the idea that there are mental representations that the mind has the capacity to represent
*  the world.
*  Going back to the medieval era, then in the 19th century, Hermann von Holmholtz really
*  what he helps to found perceptual psychology, he puts this idea of mental representations,
*  he calls them ideas, but the same basic ideas, these mental items that represent the world.
*  That's quite central to a lot of his formulations and the way that he looks at it.
*  In the modern era of the cognitive science revolution, talk about mental representations
*  is just rampant.
*  So these are ideas that are emanating from philosophy and migrating over to the sciences.
*  So there's that aspect of this, it's a source of ideas, and it's the other aspect that you
*  mentioned that it can help with conceptual clarification.
*  So for example, this Bayesian modeling of the mind, Bayesian decision theory is a normative
*  framework that basically gives you mathematical tools for modeling reasoning and decision
*  making under uncertain conditions.
*  And it starts out in philosophy and in the work of mathematicians, scientists such as
*  Laplace in the 19th century, really as a normative framework, like we're going to use this to
*  to try to make good rational inferences about the world using the tools of Bayesian decision
*  theory.
*  But then in the last few decades, especially, you see cognitive scientists using it as a
*  descriptive tool where maybe the mind actually is doing Bayesian inference.
*  So something like these Bayesian norms are being implemented or at least approximated
*  by the mind.
*  And this is something that philosophy has a lot to say about because the central notion
*  of Bayesian decision theory, for example, is the idea that agents have subjective probabilities,
*  that they attach credences to hypotheses about the world.
*  So the credence would basically be the degree of belief that you have that hypothesis is
*  true.
*  So if you're on a jury and you're trying to decide is the defendant innocent or not, you
*  might have a certain degree of belief.
*  Well, probably he's innocent, but I'm not sure.
*  So in Bayesian decision theory, you have a quantitative measure of this sort of thing,
*  of the degree to which you believe something.
*  So this notion of attaching a credence or a subjective probability to hypothesis, which
*  is so central to what's going on in the science, is something that philosophers have talked
*  a lot about.
*  So it's something that they can say and help to clarify what it is.
*  Or another example in the same vein would be these are supposed to be rational norms,
*  norms like you're supposed to conform to these norms of Bayesian decision theory.
*  If you conform to them, you're rational.
*  If you don't conform to them, you're irrational in some sense.
*  Well, why is that?
*  Why are these norms so special as opposed to other norms?
*  This is something philosophers have talked about endlessly for decades.
*  And it's something that if scientists are naturally often when you read these papers
*  on Bayesian modeling, they'll start out by making normative claims.
*  And it's something that people who want sort of a deeper understanding of the normative
*  basis of Bayesian decision theory, they could look to the philosophical literature for really
*  quite extensive discussion of this normative basis.
*  But then there's also the last thing that you mentioned, which is that philosophy can
*  learn from the science.
*  So philosophers for hundreds of years talked about mental representation, but there wasn't
*  the science that they could draw on of mental representation.
*  So it was really just armchair.
*  I don't want to say speculation because it was grounded in introspection and tight arguments,
*  but there wasn't an experimental basis.
*  Still in an armchair.
*  Yeah.
*  Yeah, it was still in an armchair.
*  So but now there's thousands of people doing research on this notion of mental representation.
*  We've learned a tremendous amount about it.
*  So for example, in my work, a lot of what I do is that I try to look at the scientific
*  literature and say, OK, what does this tell us about how the mind works?
*  How can this illuminate the questions that philosophers have been interested in about
*  mental representation?
*  So I'm sort of trying to do both in my work.
*  I'm trying to contribute conceptual clarity when I can and also trying to see what I can
*  learn and what I can communicate to philosophers and what kinds of philosophical reflections
*  I can make based on the scientific literature.
*  To answer the other part of your question, I do think that Kuhn played a really important
*  role in all this, in not just philosophy of cognitive science, but philosophy of science
*  more generally because he was so focused on scientific practice and looking at scientific
*  practice as it is.
*  And sometimes in the popular conception, Kuhn is branded as being almost anti-science or
*  he thought that he like people would say, oh, well, he thought that science was irrational
*  because of these paradigm shifts that he liked to conversion experiences.
*  And when you change a religion and there is that aspect to him.
*  But if you read the structure of scientific revolution, the vast bulk of it is really
*  very close attention to the history of philosophy, just informed by enormous knowledge and respect
*  for the way that these scientists are operating.
*  And it helped, I think, to bring philosophers into touch with how much traction, how much
*  mileage you can get from looking at the nitty gritty of scientific practice.
*  I recommend the book too.
*  It's a short read and I have to credit my advisor when I was a postdoc for making me
*  read it.
*  He had his little library and he just threw it on my desk one day.
*  I don't remember what I was doing wrong, but he thought...
*  It is a terrific book.
*  When I teach philosophy of science, intro philosophy of science, I always spend at least
*  two weeks going through it, really just having the students read it and lecturing on it.
*  Well, so you talked about what you are contributing, what you're sort of wanting to contribute.
*  So I mean, yeah, how do you hope that your philosophy contributes to, I guess, should
*  we say cognitive science?
*  Is that what you're most comfortable with?
*  Biological science or just the science of intelligence?
*  Cognitive science is a pretty good term, I think, just to describe this umbrella notion
*  of these many different disciplines all in one way or another trying to understand the
*  mind.
*  I would even include AI, at least a lot of AI under that rubric, maybe not all the commercial
*  applications, but a lot of AI is in the spirit of trying to understand at least how you might
*  reverse engineer a mind.
*  So in that sense, it's contributing to our understanding of how minds work.
*  So yeah, I think cognitive science is pretty standard term or pretty good term for it.
*  So are you do you feel like your work is received?
*  So what you know, like what was the current state do you think of philosophy in the minds
*  of practicing scientists?
*  How do you feel received when you because I know you interact a lot with with practicing
*  researchers?
*  I think that it varies.
*  I think that it really varies from field to field and from researcher to researcher.
*  I think that in psychology, at least a lot of people are very open to philosophy and
*  eager to interact with philosophers.
*  So there's a professional organization called the Society for Philosophy and Psychology,
*  which has an annual meeting and that's attended equally by philosophers and psychologists.
*  Everyone's happy.
*  So yeah, it's a happy it's not a combative media.
*  It's a productive meeting where there's a lot of interaction and a lot really gets done
*  there and people come out of it feeling feeling like they've learned from one another.
*  I think that maybe in neuroscience, there's probably a little bit more suspicion among
*  philosophers.
*  Not all I don't want to think about neuroscience is a huge field, but maybe there's a little
*  bit less of a tradition because psychology does spin off of philosophy through Helmholtz,
*  through William James.
*  So there's just these historical roots that the two fields have always been.
*  I mean, we all spin off of philosophy, though.
*  I mean, natural philosophy was gave birth to science, essentially, right?
*  Sure.
*  But it's psychology is more recent spin off, I guess.
*  I mean, neuroscience is really a lot of the a lot of the work in neuroscience is coming
*  maybe from a more biological tradition.
*  So I think that it just it just varies.
*  But certainly, like, I'm going to be going to a conference on philosophy and neuroscience
*  this summer where it's going to be some neuroscientists, some philosophers.
*  So it's not like it doesn't happen.
*  It's just that maybe it's a little bit less common to encounter it.
*  That's just my impression.
*  But of course, I have a limited perspective.
*  I think that maybe if you talked to philosophers who engage more than I do with neuroscience
*  and there are some philosophers who really get more into the nitty gritty of the neuroscience
*  than I do, maybe they would have a different impression.
*  They would be talking more to neuroscientists than I do.
*  They're up for the battles in neuroscience.
*  So from your I was going to say perch from your vantage point in, I guess, philosophy,
*  for lack of a better term, how do you view the current state and sort of direction of
*  the study of mental processes of of AI and the study of neuroscience?
*  Is everybody headed in the right direction?
*  Is it just like a bunch of watching a bunch of clowns running around the car?
*  Definitely not the latter.
*  Definitely not the clown car.
*  No, I'm actually really excited about it.
*  I think if you look at what's going on now, there's a lot of genuine progress being made.
*  So the three areas that I know the most about that I just because I've written about them.
*  So I've just had to inform myself the most about them are the study of perception.
*  So here's what you want to understand is how do we perceive the world?
*  How do we come to, for example, the case of vision, come to see the world as it is, or
*  at least roughly as it is.
*  So for example, you're looking at a white wall.
*  How do you come to see the wall as being white?
*  What's going on in your mind?
*  And so there's been a lot of progress and understanding questions like that.
*  Or just to give another example, you look at a cube, how do you come to see it as a
*  cube?
*  And this is a very hard problem.
*  These are the sorts of problems.
*  But a hard problem for the mind to solve and also hard for scientists to come to understand
*  how the mind solves it.
*  So we mentioned Bayesian models before.
*  One of the most exciting trends, I think, is Bayesian modeling of perception, where
*  people treat the perceptual system as in effect, doing unconscious Bayesian inference.
*  So it's not like you're consciously aware of doing some sort of probability calculation.
*  I mean, Helmholtz would love this.
*  Helmholtz would love it.
*  Exactly.
*  So it comes directly from Helmholtz with the idea that perception does unconscious inference
*  and people doing Bayesian modeling of perception are definitely see themselves as continuing
*  this Helmholtzian idea.
*  And there's been a lot of empirical success from these models.
*  I guess maybe even a better word would be explanatory success because you get really
*  impressive explanations of perceptual phenomena.
*  So the second area that I know a fair amount about is motor control.
*  And so motor control, you're just to the question, how do we move our bodies to achieve our goals?
*  How does the motor system, you have an intention to do something, like I intend to go pick
*  up a cup of coffee to drink it.
*  Now the job of my motor system is basically to make that happen.
*  I've got to walk over to it.
*  I've got to lift my arms.
*  I've got to wrap my hands around the coffee cup.
*  So how does that happen?
*  Again, a very hard problem for the motor system to solve.
*  You could see this because we basically can't even yet build robots that are able to do
*  this, which is very super, you know, anyone above the age of eight or six or whatnot
*  is extremely easy thing for them to do, to pick it up without spilling it.
*  And again, you have Bayesian models that are given of this where the motor system in this
*  effect doing Bayesian computation, estimating its environment and Bayesian terms, doing
*  expected utility calculations.
*  And these are quite impressive as well.
*  And the final area that I know the most about is navigation.
*  So especially mammalian navigation.
*  And the idea here that has proved quite successful is that mammals have something like a cognitive
*  map, something like a map like mental representation in their heads of their spatial environment.
*  So the animal is in a way representing how things are spatially laid out in its surroundings.
*  And this idea is also yielding quite a lot of insights, I think.
*  And in that area, especially there is a big neuroscience connection going back to the
*  70s with research on place cells and now more recently work on grid cells.
*  So this was what worked at the Nobel Prize for the people discovered it.
*  And this is, I think, a good example of how you can get a nexus between the more cognitive
*  level modeling and the neuroscientific modeling where, for example, what O'Keefe and Nadal
*  in the 70s were doing with place cells.
*  Their book was called The Hippocampus as a Cognitive Map.
*  And they talked a lot about place cells, but they also talked about the cognitive map construct
*  and they were trying to connect the representational level with the neuroscientific level.
*  And since then, there's been a lot of work in that vein.
*  So I'm very excited, especially about this Bayesian modeling in cognitive science and
*  the connections to neuroscience.
*  Well, there's a connection between your Bayesian work and representation as well.
*  So I don't know, let's start talking about representation, I suppose, and work our way
*  there.
*  So I'll be talking next episode, actually.
*  I will have interviewed Jeroen Diedrichsen and Nico Kriegeskorte about representations
*  in neural activity and specifically ways to encode and decode those representations at
*  different levels of understanding and granularity.
*  But okay, I'm going to summarize your worldview and you can tell me where I'm wrong.
*  And then we can dive deeper into the concepts, okay?
*  Sure.
*  I've already been talking about your love of all things Bayesian here.
*  But okay, so you ascribe to, you like the computational theory of mind hypothesis that
*  we have these mental operations over symbols.
*  And this can be encapsulated in the language of thought hypothesis, which describes the
*  symbols and uses mental ease as the language in which our minds talk.
*  So I think you were mentioning Helmholtz called an idea, I think it was Helmholtz,
*  and now we call it representation.
*  Well, the mental ease for those two different words would be the same thing, right?
*  Because it's sublingual in this case.
*  Anyway, you also are a proponent of Turing style, a Turing style model of the mind in
*  that you can decompose mental processes into iterated elementary operations over symbols.
*  But the Turing style often assumes when people invoke it that those symbols have no meaning.
*  They're just governed by their intrinsic properties or syntactic properties.
*  And we'll get into what all of this means in a few minutes here.
*  But that there are rules on them about, you know, that govern the computation.
*  However, you believe that computation can operate at the level of representation, not
*  just at these formal syntactic rules levels.
*  And one of the questions that you have is what role can or does representation play
*  in mental computation?
*  What did I miss?
*  Where did I get wrong?
*  No, nothing exactly wrong.
*  I would just maybe make a few caveats.
*  So I definitely am interested in Turing style models of the mind.
*  I wouldn't exactly say I'm a proponent of them.
*  I regarded more as a promising conjecture.
*  We need black and white here, man.
*  We need black and white.
*  You're trying to make it more black and white.
*  Then I do think that in some areas, the idea that something like Turing style computation
*  is going on, there's some strong considerations in favor of it.
*  So, for example, there was a book by Randy Gallistil and Adam King called what was called
*  memory in the computational brain, I think it was called.
*  It came out about 10, 11 years ago.
*  And that's something that they argue in that book at quite a lot of length that for at
*  least some phenomena, we're going to need something like a Turing machine model of the
*  mind.
*  Now, it's not going to be exactly like the simple Turing machines that you study when
*  you take introduction to computability theory.
*  It's got a different various ways.
*  For example, the most basic Turing machine that Turing himself had has an infinitely
*  long tape and like the mind is fine.
*  It's not going to have an infinitely long tape.
*  And there will be other differences as well.
*  So for example, what are the differences that they argue is that you're going to need addressable
*  memory locations, whereas in a Turing machine, there's no addresses to the individual memory
*  locations that the central processor just has to go from one memory cell to another
*  one at a time.
*  Whereas in any modern computer, there's going to be addresses, addressable memory.
*  And they argue that the mind is going to be like that too.
*  And they give a lot of empirical evidence for that citing phenomena such as animal
*  navigation.
*  Navigation, that's right.
*  Yeah.
*  They use dead reckoning, I think, as an argument, for instance.
*  Go ahead.
*  Yeah.
*  I'm just remembering a book.
*  Yeah, that's absolutely right.
*  Dead reckoning is one of their central examples.
*  So I think that there's a lot to that and it's something worth considering, at least
*  in some areas of the mind.
*  In terms of the issue of representation and syntax, yeah, let me talk a little bit about
*  that, please.
*  So let me back up, just say a few things about the relationship between representation and
*  computation more generally, because I think that'll help to answer your question.
*  The first point is that I think that virtually everyone who writes about this agrees that
*  representation is foundational to computation in some way.
*  So if you think about, for example, a Turing machine, just a really elementary Turing machine.
*  Well, let me just back up.
*  We're talking about computation in the broadest sense now, right?
*  Yeah, just the broadest sense.
*  I'm going to use Turing machines as an example, but you could make similar points if you were
*  talking about neural networks.
*  It's easiest to give more computer sciencey examples to bring out the point I was making.
*  So you've got this Turing machine, what's it doing?
*  It's moving across the machine tape and it's erasing symbols, writing symbols down.
*  The symbols might be just, you might have a really simple artificial language just consisting
*  only of strokes, stroke marks and strings of strokes.
*  You could have a more complicated tape alphabet with a lot of more primitive symbols.
*  But either way, all that it's really doing is computing over a formal language, a language
*  that's composed of elementary signs that are concatenated or combined into strings.
*  Now the thing is that for most applications in computability theory in AI, really almost
*  What we're interested in is computation over a non-symbolic domain, a domain that isn't
*  a domain just of symbols or signs.
*  So for example, the case that people in the 1930s were most concerned with in the time
*  that Turing was writing was computation over natural numbers, computing functions like
*  addition, multiplication, subtraction, where you might, for example, divide one number
*  into another.
*  So here you're doing a computational operation over natural numbers, 0, 1, 2, 3, 4, 5.
*  So you've got to get from what the Turing machine is at its most basic level doing,
*  which is manipulating symbols to computation over a non-linguistic, non-symbolic domain.
*  How are you going to do that?
*  Well, you have to have a semantic interpretation.
*  You have to treat the symbols as representing something.
*  And several points apply to other domains.
*  So for example, in computable analysis, you're studying computation over real numbers.
*  And here you again have to have some kind of notation for real numbers.
*  So you might use our familiar decimal notation for the real numbers that everyone learns
*  in grade school.
*  But there are many other possible notations for real numbers.
*  And these actually support different notions of computability.
*  You get the different functions are computable over the real numbers, depending what notation
*  system you use.
*  So the point I've just tried to make is that really once you look beyond the most elementary
*  case of computing over elements in an artificial language, you have to bring in some kind of
*  idea of a notation or representation relation.
*  And the same applies if you broaden your attention from a mathematical domain to more empirical
*  cases.
*  In a more empirical case, for example, let's say you're trying to build a robot, which
*  is getting to navigate through its environment.
*  And this is something that people do, for example, with self-driving cars.
*  So the robot needs to basically know where it is.
*  So it's going to have something like a map or something like a representation of its
*  environment encoded.
*  And it's going to be doing computations over that.
*  It's going to be updating it based on new information that it gets through its sensors.
*  It's going to be exploiting this representation of the spatial layout.
*  So you're going to have at some level a manipulation of symbols, or you could call the pieces of
*  syntax in the robot.
*  But you also fully understand the computations that the robot is doing.
*  You have to understand that they're representing spatial locations, representing landmarks
*  in the environment.
*  So I think that for that reason, because of the kinds of considerations I've given, representation
*  is central to understanding virtually every computation that one finds, unless you're
*  looking at some case where really it's just computation over some kind of formal language.
*  So I mean, this relates, and I was going to hold off until later, but since we're already
*  talking about it, I think it's worthwhile just to spell out.
*  So on the show, we often talk about Mars levels of analysis, and we'll talk about that in
*  a few minutes.
*  But there's levels of computational explanation that basically lays out computational understanding,
*  explanation at three different levels, the representation, the syntactic, and the hardware.
*  And we've been talking about these a little bit, but maybe we should be explicit about
*  them before we move forward.
*  Is that?
*  Absolutely.
*  All right.
*  Well, so let's take a concrete example.
*  Let's say you have a machine of some sort, like a register machine or some kind of computational
*  system, that's doing a strictly numerical computation.
*  Say it's executing the Euclidean algorithm.
*  So the Euclidean algorithm is ancient algorithm for computing the greatest common divisor
*  of two numbers.
*  You plug in two numbers, it outputs the greatest common divisor.
*  So here's one level that you could describe what this machine is doing.
*  You could say, well, the machine divides one number into another, takes a remainder, does
*  division again, takes a remainder, and it basically keeps on going until the remainder
*  is zero.
*  I mean, you have to spell that out a little more detailed to actually get the algorithm.
*  But that's in effect the Euclidean algorithm.
*  So here you're describing it in terms of the computations that it's doing over numbers.
*  So there's an implicitly representational aspect to your description because of what
*  I was saying earlier that the machine is manipulating symbols and the symbols are
*  not numbers.
*  I mean, so just to be maybe more explicit, let's say just take the number 12, right?
*  So the number 12 can be represented in many different ways.
*  The number 12 could be represented using our familiar Arabic notation.
*  You could use base two notation, base three notation.
*  You could use Roman numeral notation.
*  So you have the number and then you have all these what philosophers call numerals.
*  So the numerals are the different names you could have for the numbers.
*  The numerals are in notation systems.
*  So to appreciate what I'm going to say, you have to very sharply distinguish the number
*  from the numerals.
*  They're not the same thing.
*  So but the numbers, like the abstract mathematical entity that mathematicians are studying, then
*  the numerals are the various names that we have for the number.
*  And all the machine has inside of it, so to speak, is the numerals.
*  But for the manipulations of the numerals to count as actually doing the Euclidean algorithm,
*  doing this arithmetical computation, it has to be endowed with the semantics or with the
*  representational relation to the numbers.
*  So when you describe what this machine is doing with respect to numbers, that's an implicitly
*  representational description.
*  But now you don't have to describe it that way.
*  You could say, look, forget about the semantics.
*  Forget about the number.
*  Who cares about the number?
*  I'm going to describe the purely syntactic level.
*  I'm just going to say you take this symbol, you take this numeral, you do this to it,
*  you take this numeral, you do that to it.
*  So that's what I would call a purely syntactic level, which is when you completely ignore
*  any representational aspects.
*  And finally, there's the hardware level, which is when you get into the actual physical construction
*  of the machine, like what's going on with the silicon chips.
*  And that's a level that an ordinary user of a computer would never care about too much.
*  They would just never get involved in it.
*  So usually you would just do either the representational or the syntactic level or some hybrid of them.
*  But of course, if you want to build the machine or if the machine is broken and you need to
*  get it fixed, then you're going to start to care a lot about the hardware level.
*  So someone needs to care about it.
*  But most ordinary users and computer programmers don't need to care about it.
*  The neuroscientists.
*  Yeah, yeah.
*  Well, yeah, exactly.
*  So that's right.
*  That's the analog to the neuroscience.
*  So I'm going to get to that in a second.
*  So the same thing applies if you are talking about other computations.
*  So go back to this robot navigating.
*  And just to be concrete, let's say that what the robot is doing is doing a Bayesian inference.
*  To estimate where it is.
*  And this is so if you look at a lot of work on these autonomous vehicles and work on probabilistic
*  robotics, this is the paradigm that's driving a lot of this work is that something like
*  a Bayesian inference is being or approximation to a Bayesian inference is being executed.
*  So there's a great textbook called probabilistic robotics, which talks all about these different
*  Bayesian models of robot navigation.
*  So one way you could describe what the robot is doing is in the representational terms.
*  You could say, well, the robot is doing Bayesian updating over representations of spatial locations.
*  Let's say it's using Cartesian coordinates to represent spatial locations.
*  And that's a representational level description.
*  You're bringing in how the robot represents the spatial layout.
*  That it's like, well, it represents itself as being at this location.
*  It represents the landmark as being at that location.
*  And if you set up a Bayesian model, the natural way to think of the Bayesian model would be
*  What the Bayesian model is, is basically the robot is attaching probabilities to hypotheses
*  about its location, hypotheses about the locations of landmarks in its environment.
*  Just to hold there, is that where intentionality comes in and aboutness and meaning?
*  Are those yoked to the concept of representation at the representation level?
*  Yes, absolutely.
*  Yes.
*  I really consider most of those just almost different words for the same basic concept.
*  If you read the philosophical literature, it's kind of the narcissism of small differences.
*  These terms like intentionality, they get used in a million different ways.
*  People draw a thousand differences.
*  But yes, that's the core.
*  It's all sort of the one core phenomena that in some sense the system is representing the
*  world.
*  Its states are about the world.
*  And the term of art philosophers sometimes use is that they have intentionality.
*  But yeah, for me, I use these terms almost interchangeably.
*  You just used a phrase that I haven't heard that really encapsulates the side of philosophy
*  that I don't enjoy, which is the narcissism of small differences.
*  Is that a common phrase?
*  I think it's some kind of truism.
*  I don't know if it's specifically to philosophy.
*  But it's not a phrase that I coined, I don't think.
*  But I think that, how should I put this?
*  I was using a partly response to some of the stuff you were saying at the beginning because
*  I was getting the sense that when a lot of outsiders look at philosophy, that's kind
*  of what they see.
*  Because one of the main things that philosophers do is they draw distinctions.
*  Philosophers are great at drawing distinctions.
*  And sometimes it's really important to draw distinctions.
*  And there are a lot of cases where I think work in cognitive science and neuroscience,
*  maybe they should draw a few more distinctions.
*  Not that it would necessarily change the model they give, but it might allow for greater
*  clarity about the import of the model.
*  But I think that for a practicing scientist, sometimes all this drawing of distinctions
*  can seem a little bit picayune, a little bit ivory tower, not that really relevant to anything.
*  So yeah, the phrase has a pejorative connotation.
*  But I actually am someone who loves to draw distinctions.
*  And probably if people read my paper, they might say, well, this is the narcissism of
*  small differences.
*  They might see that in some of my work.
*  Your papers, from a scientific perspective, read really well, by the way.
*  But I interrupted you.
*  So let's...
*  Oh yeah, yeah.
*  So robots navigating.
*  Yeah, yeah.
*  No, no, I'm glad you did because it gave us a chance to clarify that.
*  But all right, so yeah, so you got the robot.
*  So you could describe it at the representational level.
*  But then again, you could describe it at a syntactic level.
*  You can describe just purely the level of code, purely in terms of what sort of simple
*  manipulations is going on in the robots.
*  And you'll just ignore the fact that this has anything, in fact, to do with spatial
*  representation.
*  It's just a purely syntactic description.
*  You can absolutely do that with the robot.
*  And then, of course, you can also do a hardware description where you're just talking about
*  the silicon chips and whatnot.
*  So all these levels have their value when you're studying an artificial computational
*  system.
*  People engage in all of these different levels of description.
*  I would say all vital for just for different purposes.
*  Like, as I was saying before, the hardware description isn't that important for a lot
*  of purposes, but it's very important if you need to build a machine or fix it.
*  The representational level is crucial if you want to understand why we built this
*  machine. What is this machine actually doing?
*  The syntactic level, it's a little more subtle to say why it's important.
*  But I do think it plays an important level, giving an abstract level of description that
*  isn't a hardware level description, but doesn't bog you down in all the representation
*  detail. Yeah. You think that at least for artificial computing systems, and this is
*  something I want to get into later, but not that the syntactic level is important, but
*  that you can essentially skip it for biological or OK, I'll hold on as you're
*  nodding. No, no, no.
*  Yeah, that's right. I absolutely.
*  Yeah. I mean, let's say that I'm skeptical.
*  All these things, especially when you write a paper, you publish it, you're like, yes,
*  this is my view. But, you know, in practice, people are more they're not as confident.
*  But so, yeah. So I think that's actually a good place to a good entry into what you
*  just asked is to talk about the work of Jerry Fodor.
*  Sure. So Jerry. Yeah. So Jerry Fodor, definitely the most important philosopher of
*  psychology of the last decade, really seminal figure.
*  And so Fodor was really pushed this idea of the mind as a computational system, especially
*  as a Turing style system that was integral to his whole picture.
*  And so he developed this computational theory of mind is the mind as a computational
*  system. And so Fodor's picture is that the mind is doing Turing style computations
*  and you get something exactly like these three levels of computational description
*  that I was just describing to you.
*  You get the representational level, you get the syntactic level and you get the
*  hardware level. In this case, the hardware level would be neuroscience, essentially.
*  So the representational level would be how does the mind represent the world as being?
*  So, for example, let's say you have go back to this jury example I gave earlier, you're
*  on a jury and you decide, all right, the defendant is innocent.
*  I formed the belief that the defendant is innocent.
*  And maybe you formed that on various pieces of evidence, like the DNA match was imperfect
*  or the eye witness ID that the prosecutor put up was really pretty lame.
*  They didn't use proper protocols for the eye witness ID.
*  Whatever. You've got this evidence that you formed the belief on the basis of it.
*  So everything that I just described is essentially for Fodor and I agree with him, a
*  representational level description.
*  You have a belief about the defendant.
*  Your belief is about the defendant.
*  You are ascribing a property to the defendant, the property of being innocent.
*  Maybe you're right. Maybe you're wrong.
*  It depends on if the defendant is really innocent or not.
*  But you're representing the world as being a certain way.
*  You're representing the world as being such that the defendant is innocent.
*  So if you want to understand the nature of this mental state that you've entered into,
*  you can't begin to do that unless you attend to its representational aspect.
*  That this is a representational state, a state that represents the world as being a
*  certain way. And it's a representational state that interfaces with a lot of other
*  states, such as your grasp of the DNA evidence, your grasp of the eye witness
*  identification. And the same applies not just to belief, but to perception.
*  So let's say I look at a white wall.
*  I see, oh, yeah, that wall is white.
*  So I perceive the wall as being white.
*  My perceptual state is about the wall.
*  It's a representational state.
*  So that's the importance of the representational level is that these states do
*  represent the world as being a certain way.
*  And for Fodor, one of the key things you want to do is study the mind at this
*  representational level.
*  And then, of course, everyone agrees that you also need to eventually understand
*  the hardware level, the neuroscientific level.
*  That wasn't something Fodor was so interested in personally, but everyone agrees
*  eventually you need to connect the representational level.
*  What did you say?
*  Eventually, eventually.
*  Yeah, right. Exactly. Yeah.
*  And that's a lot of what goes on in computational neuroscience.
*  You could see it as doing that or a step towards doing that.
*  So but Fodor had this idea, as you alluded to, that the intermediate level is also
*  important, the syntactic level, so that you're going to have not just the
*  representational level description and the hardware neuroscientific level
*  description, but also this middle level, the syntactic level.
*  And I'm just not so sure how much this adds in the case of a biological computing
*  system, when you have a mind that you found in nature, whether it's a human mind
*  or animal mind.
*  At least I think in a lot of these cases that we're talking about, such as belief,
*  such as perception, I suspect that it might be better to skip this and just go
*  right from the representational level to the hardware level.
*  And I think that's what you find when you look at scientific work on this.
*  So one of Fodor's main arguments was he alleged that if you look at the cognitive
*  science, what you see is this syntactic level all over the place.
*  And I don't see that when I look.
*  So, for example, in this work on cognitive maps, describing these as a cognitive
*  map, that's like a representational level description.
*  You're saying here is this mental representation, this mental representation
*  represents spatial layout of the environment.
*  That's all thoroughly representational level.
*  And then one of the huge questions in this area is how are cognitive maps
*  neurally realized and what are the neural processes that lead to the formation
*  of a cognitive map?
*  How does the cognitive map get revised?
*  And you could study those questions at a more psychological cognitive level.
*  And there's work on that.
*  And you could also study it at the more neurophysiological level.
*  And that's what this work on place cells and grid cells and spinning off of that
*  is contributing to.
*  So there you have the representational level and the hardware level.
*  But where's the syntactic level?
*  There's nothing like that.
*  There's nothing like these sort of pieces of meaningless syntax, the pieces of a formal
*  language getting pushed around that you find in the study of, say, the register
*  machine or the robot that we were talking before.
*  Similarly, I would say for a lot of these Bayesian models that one finds take Bayesian
*  models of perception, I would describe a Bayesian model as a representational level
*  description, because say you have a Bayesian model of perception, the most core idea of
*  it is that you have this Bayesian inference that eventuates in a perceptual representation,
*  let's say, of the color of some surface, the shape of some object.
*  So you're describing the final perceptual state in representational terms.
*  How does it represent the world as being?
*  It represents the object as being a cube, not a sphere.
*  It represents the surface as being white, not red.
*  Well, represents it through like a probability distribution of features and things like
*  that. And at the hardware.
*  Level anyway, you know, there's a lot of work in the Bayesian world and doing things like
*  sampling, you know, as a Bayesian as an approximation to a Bayesian process in brains.
*  So that would be one example of neural implementation of Bayesian.
*  Exactly. 100 percent.
*  And that's something I talk about in some of my work is the sampling.
*  I think that's some of the most promising approximation implementation models that have
*  been proposed, in fact, the sampling model.
*  I think you had you had Wolfgang Mase on your program recently, if I'm not mistaken.
*  And he works on this topic, this neural implementation of Bayesian inference.
*  So so but this is another example where you have the representational level that you
*  well, how is this actually happening with with neurons in the brain?
*  And so you have the representational level, you have the neural level.
*  But there's just nothing really like the syntactic level that Fodor is talking about.
*  So I feel like I'm skeptical that we're just going to have much value.
*  I don't really see it play much of a role in how practicing scientists are thinking
*  about it. It seems kind of like the ether that they had in 19th century discussions of
*  electromagnetism, sort of this this construct that people, in this case, philosophers
*  think they need because they've convinced themselves that it's mandated for some
*  reason. But actually, it's just an expressiveness that should be expunged from the
*  theorizing.
*  So while we're talking about syntactic and semantic, so and levels of computational
*  explanation, what I was going to ask you is, you're talking about cognitive science.
*  And so Fodor's take when he looked at cognitive science is that he sees a lot of
*  syntactic level explanations for things.
*  Do I have that right?
*  Yeah, yeah.
*  But if I'm not mistaken, your take is that cognitive science perhaps has taken
*  too much to heart.
*  The idea of the need for syntactic level has been inspired too much by artificial
*  computation, in other words, and hasn't taken enough from what we understand about
*  biological or mental computation.
*  And you have this really nice paper that really lays it out.
*  But maybe you can just talk a little bit about the difference between why you think
*  syntactic level explanation might be appropriate for artificial systems, whereas
*  representational level explanation might be more appropriate for biological systems.
*  Sure. Yeah, I think the paper you're probably alluding to is the levels of
*  computational explanation.
*  I think it's called.
*  It is. Yeah. And these will all be linked to in the show notes, of course.
*  So.
*  Great. Great.
*  So I'll just say, like, first of all, we were talking about the armchair.
*  I don't think these are questions that can be settled from the armchair.
*  I think these are ultimately empirical questions.
*  You have to construct a theory that enshrines one or another way of looking at things.
*  And then play the theories off against each other.
*  So I. But one of the flaws that I see in this philosophical literature is too much
*  reliance on armchair argumentation.
*  So you find Fodor and people influenced by Fodor often giving arguments, well, there
*  just must be the syntactic level for some a priori reason.
*  And I'm very skeptical of that.
*  And the reason I'm skeptical of that is that when you're studying an artificial
*  computational system, you're doing something very different than you have a different
*  relation to it than when you're studying a biological system, because one of the main
*  reasons that we need the syntactic description for artificial system is that it's
*  functioning basically like a blueprint.
*  It's describing how to build the machine.
*  It's described or in some cases how to program the machine.
*  But it's something that we're using to build or manipulate or or in some way construct
*  and change the machine.
*  And the value of the syntactic description is that it lets us do that.
*  But it's very abstract.
*  It doesn't get us into hardware details.
*  So you could do this without having to worry about the silicon chips, because people, the
*  computer programmer doesn't want to get into that data.
*  And maybe there are lots of different ways that you could, in principle, do a hardware
*  implementation. You don't want to commit yourself.
*  You don't know what resources you're going to have.
*  You don't know what the physical machine is that is actually going to be built.
*  You want to have this high level abstract blueprint of it that doesn't get you into the
*  hardware, but at the same time isn't representational, where you're not getting bogged down
*  in these philosophical questions about intentionality and about this.
*  And what exactly would it take to give bestow these representational properties?
*  And you don't have to get into that because it's just really syntactic.
*  So when you get the syntactic description, it's really I think that David Chalmers has
*  a really nice paper on this. I forget the name of it, but I think it's called Varieties
*  of Computation or something like that.
*  It came out about seven or eight years ago.
*  And I think it was a reply to a bunch of articles by people that were that were basically
*  critiquing him. And then his providers of computation is his reply to those people.
*  And what he says there is that it's sort of the syntactic level gives you this sweet spot
*  between the representational and the hardware level, where you have it's abstracted away
*  from these hardware details, but it's not getting you into these representational aspects
*  either. And I think there's something.
*  Go ahead. Well, in that respect, it's a multiply, multiply realizable.
*  It has multiple realizability features. Right.
*  Yes. Yes. That's the terminology philosophers use for that kind of description.
*  That is that it's a multiply realizable.
*  So the representational and the so much of it will be realizable means that there are
*  many different ways of physically realizing it.
*  You could do a neurons or tinker toys or whatever.
*  Yeah, exactly. And representational and syntactic description are both multiply
*  realizable. But the syntactic description is just a lot easier to deal with for a lot
*  of purposes for the reasons I was indicating earlier.
*  So but the thing is that when you look at a biological computing system, a natural
*  computing system like the human mind or like a say the mind of a rodent, we're not
*  building it. We're not we don't need a blueprint for it, not a little blueprint,
*  because it's also they were constructing.
*  It's given to it. Well, yeah, I mean, if we start to construct it, then maybe it will
*  change. But we're not it's we're not constructing it now.
*  Right. We just have it.
*  And we're trying to understand how it works on its own terms.
*  So it's given to us.
*  It is doing these computations which we can understand in representational terms,
*  understand, for example, the rat as navigating through space, as representing the
*  spatial layer of its environment.
*  But really, what we want to understand is precisely the hardware details that we
*  don't care about so much when we're building the physical machine.
*  Like, that's what we care the most about for the rat is how is this being done in
*  the actual rodent brain?
*  That's the million dollar question that everyone is trying to answer.
*  So in the case of the building the machine, of course, someone needs to care.
*  Some computer engineers somewhere needs to care.
*  We're very grateful to them for doing that.
*  But for many, many purposes, like we don't care.
*  We don't want to have to deal with it.
*  We want to know how to program it, how to work at the much more syntactic level.
*  But at the when we're studying a pre-given mind, the whole thing that we care about
*  is how this thing gets implemented in the hardware level.
*  And so I'm not sure that you have as much of a need for the syntactic description.
*  And I think that the course of the science kind of bears out this somewhat a priori
*  consideration that I was just going through, because as I was saying before, you
*  don't in fact people give it.
*  You don't in fact find people giving anything like this syntactic description.
*  So that's the basic argument of that that paper.
*  And in some of my other work, I try to explore some of the ins and outs of this a
*  little bit more, but that's the gist of it.
*  So we're kind of circling through these topics.
*  And if it's OK, let's circle back and talk about representation at large or in
*  general. Sure.
*  I mean, so I mean, so the concept of representation, like you have already
*  discussed, you know, it has been and continues to be this huge philosophical
*  playground, essentially.
*  So let me just talk about a few ways that representation is used in neuroscience and
*  AI, maybe, and then we can bring in the philosophy perspective here.
*  So in neuroscience, I feel like it's the concept of representation has been sort of
*  diluted over the years in that it's there's a dilution over the individual neuron
*  contribution, essentially.
*  So, you know, we started studying tuning curves and grandmother cells, these
*  individual neurons and what they responded to feature feature wise.
*  And then it sort of diluted a little bit.
*  And now we talked about now we talk about mixed selectivity and population code.
*  So there's neurons that contribute a little bit to a lot of functions and tuning
*  curves don't necessarily match the neurons contribution.
*  Just because the neuron is firing highest, looking at a white wall doesn't mean that
*  neuron is encoding white walls.
*  So, OK, so in an AI and there's more to say about all of this, of course, so I'm
*  just touching on it. But in AI, representation is used mostly when talking
*  about the activity of a layer in a neural network and like a deep neural network.
*  Right. So you have a layer of a bunch of like some given hidden layer.
*  Right. So so well, or any layer.
*  So the concept of a representation is obvious in like an input layer.
*  The representation is that the image pixel value level, for instance, and it's
*  pretty obvious that the output layer where you represent the different
*  probabilities of the different categories that the neural network is
*  functioning to, you know, say whether it's a tree or a car, for instance, and
*  the probability that it's a tree or a car.
*  You know, these output units that represent those probabilities.
*  But but then in the hidden units, it gets messy.
*  And this is the idea of this parallel distributed processing where then it's
*  you still have a representation in number form in the units and their
*  activation levels. But what they're representing at that point gets a little
*  hazier anyway. So that's I don't know that that's a great summary.
*  But at the neuroscience and AI level, but maybe in broad strokes, you know, could
*  you describe the concept of representation and in philosophy and in
*  sort of how it's evolved?
*  Yeah, sure. Absolutely.
*  In philosophy, as in these other fields like AI and neuroscience, I think
*  the word gets used in different ways.
*  Word of representation. People have different conceptions of representation.
*  But I would say that by and large, the most central concept of representation
*  in philosophy has been the idea that the mind represents the world as being a
*  certain way that and this is really the essence of representation.
*  So go back to the jury example, I formed the belief the defendant is innocent.
*  So I now represent the defendant as being innocent.
*  So you can look at my belief and compare it with reality and say, is my belief
*  true or is it false?
*  So you can evaluate the belief for truth or falsity.
*  You could say the belief is true under some conditions.
*  It's true under the condition that the defendant is innocent, false under the
*  condition that he's not innocent, that he actually did it.
*  So this is what you could call a truth conditional conception of representation
*  where you think of the essence of representation as being you represent a
*  reality as being some way and that makes the representational state the kind of
*  thing you can evaluate is it true or not?
*  So this you find this conception really going back all the way through the
*  history of philosophy, going back to the medieval era.
*  But I think especially in the work of Kant, it starts to come to the fore and
*  then really it starts to come to the fore in the late 19th century.
*  So one of the central figures here is a late 19th century German philosopher and
*  logician named Gottlob Frege, whose greatest claim to fame is that he
*  invented modern logic.
*  So all the modern logic that's taught in every university in the country,
*  throughout the world. And that's the basis for a lot of the stuff that goes on in
*  AI, especially the early 1960s AI.
*  All that comes from Frege.
*  And so Frege, this was Frege's starting point, essentially what I just said.
*  He didn't put it in quite the terms I just used, but this is essentially how he
*  looked at it. The essence of mental representation is that the representational
*  state can be evaluated as true or not.
*  And then you mentioned Bertrand Russell earlier.
*  Russell definitely signed on to this.
*  And finally, the third seminal figure here, many of your listeners will have heard
*  of, is Ludwig Wittgenstein.
*  So Frege, Russell, Wittgenstein essentially all agreed on this despite many things
*  they disagreed about. And they all gave very interesting theories that were
*  essentially trying to understand mental representation in these terms, the
*  representational aspect of the mind in the terms I was just laying out.
*  And what you found over the past century of work in so analytic philosophy is
*  the term people often use for the kind of philosophy that essentially stems from
*  Frege, Russell and Wittgenstein.
*  But it's just the style philosophy that draws upon their ideas and their
*  approach. And it's mainly what's practiced in the United States and the United
*  Kingdom and Australia and also in many parts of Europe as well.
*  So in analytic philosophy, you've seen increasingly sophisticated and elaborate
*  developments and refinements of this idea.
*  Just one thing I want to mention here is that this one of the main things that
*  Frege contributed here and Russell and Wittgenstein also had a hand in this is
*  the idea that because you have these states that can be evaluated as true or
*  false, you can give what is called a semantic.
*  So you take a sentence like the defendant is innocent.
*  That's composed of words and the words are meaningful and the meanings of the words
*  contribute to the meaning of the whole sentence.
*  And so you know what a defendant is, you know what it is for him to be innocent.
*  And then that is what basically determines the conditions under which the sentence is
*  true or not. So what you're doing in what's called formal semantics is you're trying to
*  understand how the meanings of the component words, the representational properties of
*  the component words contribute to the truth conditions or to the conditions under
*  which the overall sentence is true.
*  So you end it. This was something that is quite big on logic.
*  It's quite big in linguistics.
*  It's essentially doing this formal semantics, trying to pick apart a sentence into
*  its component parts and then look at how the semantic representational properties of
*  the component parts contribute to the representational import of the overall
*  sentence. And what Frege definitely wanted to do with Russell and Wittgenstein, Russell,
*  I'm not so sure about Wittgenstein, but Russell to all logics that wanted to do and
*  what many subsequent people wanted to do is to apply a similar picture to thought
*  that just like a sentence is structured, thought too is structured.
*  There's some kind of logical structure to the high level thought of these that mirrors
*  the high level structure of a sentence.
*  And just like you can give a semantics for a sentence, so too you can give something
*  like a semantic compositional analysis of thought.
*  And that's something that that many philosophers such as Fodor have tried to spin off
*  on. Now you ask for a...so that's just like a very capsule summary of sort of how
*  philosophers are looking at it and then a lot of the work is trying to spell the work
*  that goes on in the analytical philosophy is trying to spell that out and look at a lot of
*  problem cases and so on. And we could talk more about some of those ramifications in
*  a moment. But just to answer all of your question, because you asked about comparison
*  with notions of representation that you find in these other areas, I think that sometimes
*  you find this conception playing a role.
*  I mean, at least maybe it's a little bit more implicit than explicit.
*  It's not like people would put things in exactly the terms that I put them.
*  But I think in a lot of cognitive psychology, you see people drawing upon this approach
*  as a source of ideas or at least as a sort of benchmark for how they're looking at it.
*  I think some of the early work in AI, but some of the more classical AI before you get
*  to the neural network type distributed representation you were looking to.
*  But some of the old 1960s stuff drew upon this approach.
*  And you still see some stuff that draws on it, although I agree with you that it's not
*  as big now. It's coming back, though.
*  Yeah, yeah. That's the thing. There are these cycles to it.
*  Right. And then I think that in neuroscience, I have a harder time saying in what notion
*  of representation is at play in neuroscience.
*  I agree with you that I think the word diluted is a good word for it, because sometimes it
*  seems to be a kind of anemic conception where talking about representation is almost just
*  kind of a floored way of talking about some kind of correlation, say, between neural
*  activity and things that are going on in the environment.
*  And people will use these words like represent and encode.
*  But really, it's just a gloss and it could be rephrased.
*  You could just talk about things like mutual information and correlations and stuff like
*  that without bringing in the concept of representation at all.
*  So, for example, with place cells.
*  So the place cell is basically a cell that preferentially fires when the rat is in a
*  certain location. And this was what was discovered in the early 1970s that there were these
*  place cells. And people will sometimes say in this literature, well, the place cell
*  represents the rat's spatial location.
*  But they don't say, well, what does that mean?
*  What does it mean to say that it represents?
*  What are you really adding to your description when you say it represents as opposed to just
*  giving a really super accurate description of what property in the distal environment
*  correlates with what pattern of neurofiring?
*  Because if all you have is these correlations, that doesn't add up to anything like the
*  Frager-Russell-Wickensign conception of representation.
*  My colleague, Tyre LaBerge, has a book called Origins of Objectivity, where he talks a lot
*  about this, how this more traditional philosophical conception relates to these other
*  conceptions where you would bring in something like information and correlations with the
*  environment. So what other book I'll just mention is a very recent book is a book called
*  Representation in Cognitive Science by Nicholas Che.
*  And that book is a lot of it is about representation as it figures in neuroscience.
*  And I mean, the book is called Representation in Cognitive Science, but a lot of his examples
*  really are from neuroscience.
*  And he has a sort of analysis of what notion of representation is in play in a lot of these
*  kinds of examples, some that you were alluded to, examples like the play cell.
*  And that it's basically giving a kind of philosophical, philosophical elucidation of
*  what neuroscientists, what notion of representation neuroscientists are using in some of
*  these passages.
*  You're talking teleosemantics now because we're not going to get into teleosemantics.
*  No, we're not going to get into it, but he gets into it.
*  Yeah. Yeah.
*  So but anyway, so I guess I would just say, like as a sort of global summary of the answer
*  to your question is that I think that there are different notions of representation in
*  play. It's a term that's so general that it can be used to mean different things.
*  And the most important thing, if you're a philosopher or scientist or anyone, is just
*  to be clear about what notion you have in mind and what you mean when you're talking
*  about representation. That's what I try to do whenever I write about this is to always
*  signal what I have in mind to just clarify that I'm trying to affiliate what I'm doing
*  with this Frege Russell Wittgenstein tradition.
*  There are other notions of representation that are out there.
*  So, for example, Gallistow, who I mentioned earlier, he is a different notion as well
*  that has some connection to these different notions, but really, I think is orthogonal
*  to them. So it's not that by usage I think is any better or more legitimate than other
*  people's usages. It's just that that's my usage and I try to be explicit about that's
*  how I'm using it.
*  So I guess I was going to ask you, like, what's the right level of granularity to consider
*  something a quote unquote representation? Because in the analytical philosophy, you
*  need these sort of individuated, I guess, entities, right? These single things that
*  stand for things that then you compare to other things. But then if you're in a
*  distributed system, it's diluted. You don't have that anymore.
*  But do you still call that a representation? And I don't know, I guess what you're saying
*  is you can define it however you want it in the terms in your own paper.
*  Yeah, I mean, I wouldn't exactly say anything goes. I think there's a small family of
*  notions here, some of which I was alluded to, and you kind of want to just kind of
*  clarify which one you're using. But yeah, so I mean, right.
*  Like a mental ease word, right? In the language of thought, what would count in mental
*  ease as a representation? Does it need to be a very defined entity? Or can it be a
*  collection of things?
*  All right, so let me first just say, maybe I should just say a little bit about this
*  idea of mental ease. Yeah, because it may not be familiar to and then then I will
*  answer. I often assume way too much from the listeners.
*  Yeah, so let me let me say just a word about that. And then then I'll try to answer
*  your question to some extent. But really, I'm just stalling answer your question.
*  That's what I'm doing. So all right. So this this is an idea that goes back to the
*  medieval era. So William of Ockham. So people everyone's heard of Ockham's Razor.
*  So William of Ockham was really the person who helped to crystallize this idea.
*  And so Ockham's idea is that just like we speak in a natural language, so too when we
*  think we think in a mental language. And he called this the language of thought.
*  And nowadays, people call this mental ease by analogy with English.
*  So the idea would be so natural language like English has words and the words can
*  compound at the sentences. So the sentence whales are mammals.
*  There's the word whale. There's the word mammal.
*  You've compounded into a sentence.
*  Whales are mammals. And that is the same thing is going on or something analogous is
*  going on at the mental level.
*  You have mental words like you have a mental word whale.
*  You have a mental word mammal.
*  And when you form a belief that whales are mammals, what you've done is you've
*  compounded those words together into a mental ease sentence.
*  And the sentence is meaningful, just like the English sentence is meaningful.
*  And so basically on this view, having a belief is a matter of standing in the right
*  relation to some mentally sentence.
*  So when I formed the belief that defendant is innocent, then I have a mentally
*  sentence that defended as innocent.
*  It's got these component words corresponding at least roughly to the to the English
*  word. So mentally, is this system of mental representations which operates something
*  like a natural language in the sense that you have something like words they combine
*  together into something like a logical structure and then you could give something like a
*  semantics for mental ease, just like you give a semantics for for English or for any
*  natural language.
*  OK, so so that's an idea that was very popular in the medieval era.
*  It basically fell on hard times.
*  It the period philosophy philosophers called the early modern era, which is essentially
*  the period beginning with Descartes.
*  You still have people talking about mental representations, but they thought of it more
*  an image or pictorial terms.
*  They thought it like the idea would be something like you're thinking about a triangle.
*  So you have something like a mental image of a triangle.
*  So it really lapsed out of popularity.
*  Really, no one was talking at all about this idea of a language of thought.
*  And then in the early 20th century, the basically the first half of the 20th century,
*  no one was talking about mental representations at all, whether they were mental ease or
*  mental images. People were just very skeptical about these things, partly under the
*  influence of behaviorism.
*  So you had this ascendancy behaviorism and philosophy and psychology and all this talk
*  about mental representations really not entirely, but to a large extent fell by the wayside
*  with the cognitive science revolution.
*  It comes back with a vengeance and you you find people just all over the place positing
*  mental representations.
*  So Jerry Fodor writes this book in 1975.
*  He calls it the language of thought.
*  It's this very explicit attempt to reviving this old medieval idea, but now combined
*  with the computational theory of mind.
*  So now it's that while you're doing mental computations over this language of thought
*  and the computations are operating over symbols in the language of thought, and he
*  offers support from cognitive science for this idea of mental representation.
*  So he's giving a more empirical support for this old medieval view.
*  And he's also giving a more substance by combining it with his Turing style model of
*  computation. And you also find more non-linguistic conception of mental
*  representation proliferating as well.
*  So this work on cognitive maps is an example.
*  Edward Tolman proposed cognitive maps in 1948.
*  They didn't get much uptake at that point.
*  But but in the 1970s, especially with the work of O'Keeffe and Nato, more and more
*  people start talking about them.
*  So it's not just language like representations.
*  It's also cognitive maps.
*  People talk about mental images again.
*  They talk about mental diagrams.
*  So a whole plethora of different kinds of different representational formats, different
*  kinds of mental representations.
*  And that I see as a very central thought for a lot of cognitive science.
*  OK, now, do you want to ask him about or do you want to follow up or should I should
*  I do want to answer your question about the.
*  Oh, yeah, go for it. OK.
*  OK, so the granularity question.
*  So sort of what counts as a mental these words.
*  So this is like this is the question I was stalling answering because I don't really
*  know the answer. No one really knows the answer.
*  Yeah, I maybe would just say a few things to give a conceptual framework that for that
*  that I use at least to think about because I think a lot about the question you just
*  ask. I think about it like every day.
*  And this is this is just the basic terms that I think about it and that may be helpful to
*  some of your listeners. So I think there's a really key distinction here.
*  This we're talking about philosophers, drawing distinctions.
*  And this is a place where distinction can really, really be helpful.
*  And this is what philosophers call the type token distinction.
*  So what this comes to is the following.
*  Let's take an English sentence like the sentence.
*  The defendant is innocent.
*  So I just uttered that sentence.
*  The defendant is innocent.
*  So there's this type that the sentence is this like it's like an abstract entity with
*  the philosophers called type.
*  And the reason it's an abstract entity is that it's an entity that doesn't really exist
*  in space and time because it can be instantiated on many different occasions, really an
*  arbitrarily different occasion.
*  So I can say the defendant is innocent.
*  The defendant is innocent.
*  The defendant is innocent.
*  The defendant is. Yeah. Again, again.
*  And what philosophers say is that those are different tokens of the same type.
*  So this is the type, this is the abstract entity, the sentence.
*  And then you have different tokens of that same type.
*  Just like if I were to go and write on the blackboard a hundred different times, I
*  write the letter A. What do you how many letters are on that blackboard?
*  Well, in a sense, it's just one letter.
*  There's the one letter type A.
*  But in another sense, there's a hundred because there's a hundred tokens of the letter
*  A. So you answer a question like how many you have to say are you talking about types
*  or tokens? Just like you've got, you know, five different copies of Moby Dick on your
*  bookshelf. How many books are on your bookshelf?
*  Well, there's five tokens of the single book type Moby Dick.
*  So the book is an abstract type, but it has different tokens.
*  And is the type an ontological entity or is that something?
*  Is that an open thing that we don't even shouldn't go down?
*  No, I mean, I think that I think the most useful way of looking at it is that, yes,
*  it's a real entity. There are philosophers who would deny that.
*  I mean, there are philosophers who would say, oh, why do we need to why do we need to
*  believe in these these things?
*  I don't believe in them. But I think that in general, we're OK with positing abstract
*  entities like numbers, natural numbers, real numbers, sets.
*  You can't really do set theory unless you believe that there are sets.
*  Right. So you can't do arithmetic unless you're talking about numbers.
*  So in general, we're talking about numbers.
*  One of the best discussions I've seen of this is a book by Linda Wetzel called It's
*  Just a Book Called Types and Tokens, which is essentially a book long argument.
*  Look, you should be OK with talking about the type as a real entity in its own right.
*  Don't don't scruple to positive.
*  Just go ahead and endorse the fact that this thing exists along as a genuine entity.
*  So that's the way I'm going to talk because I'm convinced by her.
*  I think she's right. I think there's a lot of reasons for believing this.
*  OK, so that's that that's the distinction of the type token distinction.
*  So now apply the type token distinction to the mind.
*  So now I don't say the defendant is innocent.
*  I form the belief the defendant is innocent.
*  I think it. Yeah, I think it.
*  So, again, there's a type, there's the from a language of thought viewpoint.
*  There's the mentally type.
*  There's this mental sentence. The defendant is innocent.
*  I'm thinking it.
*  Maybe the other jurors, hopefully the other jurors on the jury are thinking it.
*  If if they've convinced by the same evidence, they'll be thinking of it.
*  And there's this single mentally type that I'm instantiating and they're instantiating.
*  So now what are the tokens of the type?
*  Well, the tokens would be something like some kind of
*  presumably pattern of neuro firing or pattern of neural activity in my brain, in their brain.
*  So there's my token, there's their token.
*  So then what are these tokens?
*  Well, I mean, that no one knows. That's the short answer.
*  It doesn't have to just be like a single neuron.
*  It could be a distributed pattern of neurofiring.
*  It could be something that we haven't even thought about yet about going on in the brain.
*  No one knows the answer to the question from the cognitive science
*  cognitive psychology point of view.
*  What you're doing is more positing that there are these types and that we instantiate them
*  and that that treating the mind as instantiating these types is a useful way of
*  taxonomizing or classifying mental states for purposes of explanation.
*  But I mean, so the question you ask one way of rephrasing it, using this type of good
*  distinction is what needs to be in place for a neural event or for a neuro occurrence,
*  for a pattern of neurofiring to count as the token of a mental type.
*  And I mean, that's a tremendously hard question.
*  And you could see how hard it is just by reflecting on the case of natural language.
*  So think about an utterance in English.
*  What needs to be in place for my utterance of some sounds to count as a token of an
*  English sentence? I mean, or just a word like for me to utter like the word dog.
*  What needs to be in place for that to count as an utterance of a of an English word?
*  You know, you could have it's not just the sound, right?
*  It's that you can just look at the way that things sound.
*  So, for example, if I say John went to the bank.
*  Well, I could be he went to the financial institution.
*  Was the bank.
*  Or I could mean that he went to the riverbank and you can't read off which word I uttered
*  just from the sounds.
*  That's not enough because it's the same sound.
*  So the type token relation, what are the tokens of the type?
*  What make what needs to be placed for the tokens to count as tokens of a given type?
*  Even for the case of of English for language, which we understand so much better than
*  thought, we don't really know the answer to that question.
*  It may be something to do with the speaker's intentions.
*  What was I trying to say when I said John went to the bank?
*  Something about the role that the utterance plays in the larger linguistic practice.
*  This is a question philosophers have worked on, including my colleague David Kaplan, has
*  a paper or two on this question.
*  And but no one has a definitive answer.
*  So even for the case of English, which is so much better understood than thought, we
*  can't really answer the question.
*  So it's not surprising, therefore, that in the case of the mind, we can't really answer
*  the question either. So I would just say your question is a great question, but it's a
*  wide open question that we just don't know.
*  And it's going to take work, I think, by neuroscientists, by philosophers, by cognitive
*  psychologists. It's going to take work from all these different vantage points to really
*  get really concrete, satisfying answers to the question that you're asking.
*  I mean, I know that language is something that you're interested in.
*  And I don't think we have time.
*  But your dissertation was on whether what was it?
*  I have the hang on. Let me just read it.
*  Is thought explanatory prior to language?
*  And I mean, I've been thinking about language a lot lately, and I don't need to go on
*  and on about this, but I had not thought about what you just described in terms of
*  types and tokens with respect to once the waveform is collapsed and the language comes
*  out and then mapping the meanings onto what is actually said.
*  I was thinking in terms of so there is language which is spoken and once it's spoken, it
*  is a collapsed waveform, quote unquote.
*  Right. So but then then you can take a step back in your head and you can go into like
*  the mental rehearsal of saying the words, you know, before actuating them through your
*  motor processes.
*  And then it gets more diluted.
*  And like then you have these distributed probabilities and how they come together.
*  Is that a representation?
*  And then it just gets messier and messier.
*  So. Right. So I want to like draw a line somewhere.
*  And I don't know. I mean, you don't know.
*  No one knows. Draw a line between what's a representation and what's not, you know,
*  like I see.
*  I see. Right.
*  As as as the representation of this person's innocent friends.
*  And by the way, I'm wondering what horrible crime you committed that these things are
*  on your mind so much.
*  Yeah. So I think that there's got to be an example that you're giving.
*  There's going to be multiple levels of representation throughout the cognitive system.
*  So first of all, you have to have the if you take a simple case, I have a belief I want
*  to communicate it to you and then you're going to hear what I say.
*  You're going to process it.
*  So there's going to be representations in my mind and representations in your mind.
*  There's going to be first just my mental representation of just the belief that I've
*  tried to communicate. Then there's got to be at some level of the cognitive system.
*  Some representation of the syntactic semantic properties of the language that I'm going
*  to use. And that needs to be in place for me to convert my belief into which sentence
*  am I actually going to utter.
*  And this is something that, you know, in generative linguistics, it's all about exactly
*  what are these properties that are represented.
*  And then that once I decided to utter, you know, it's not maybe me who's decided to
*  utter the sentence. It's more maybe some subpersonal process.
*  Once my cognitive system, broadly speaking, has decided to.
*  You can say free will. Once your free will has decided to.
*  I've decided to utter the sentence.
*  But then my motor system, I mean, now I need to move my mouth and so I produce sound.
*  And that's a whole other conundrum that my motor system needs to solve.
*  And that's, you know, very difficult.
*  That's why I take one of the reasons it takes kids a while to start really speaking well
*  is that their motor systems are learning how to do this.
*  So and I think there's going to be representations there as well, that representations
*  involving, you know, the state of the lips, you know, the positions of the lips and things
*  like that that are going to be drawn on for to convert the intention to utter the sentence
*  into an actual pattern of motor movement in your speech production mechanisms.
*  So I think there's going to be a lot of different representations.
*  And at some point, it's going to shade into something which looks non-representational.
*  At some point, it's going to shade into just like here you have the motor command just
*  being sent by the brain to your, you know, to your vocal production apparatus.
*  But we're exactly to draw the line.
*  I'm not I'm not I don't think anyone really knows the answer exactly to that.
*  And you're going to have a parallel process going on in the part of the hearer, which
*  is that they're going to be receiving the sound and they're going to have to then, you
*  know, decode it. They're going to have to draw their semantic, syntactic knowledge of
*  the of the language in order to to understand what was said.
*  And then that hopefully will be converted into a belief.
*  So you'll have kind of it'll be almost a symmetrical process.
*  It sounds like we're all going to have plenty of work ahead of us.
*  Yes. All right. In the last few minutes, I'm going to open it up here and get a little
*  broader, if that's OK with you.
*  Yeah, absolutely. You think Turing would agree with you about the syntactic versus
*  representational nature of a Turing like process that I know you can't be black and
*  white on the mind is a Turing machine.
*  But, you know, what would you think he would think about it?
*  You know, I've wondered about that.
*  And I don't know.
*  I think it's hard to know what he would think.
*  I guess I would just say Turing was a brilliant logician and a brilliant thinker, one of
*  the greatest thinkers of the 20th century.
*  That's a safe statement.
*  Yeah, that's a safe statement.
*  But I don't think he was very sophisticated about philosophy of mind.
*  So, for example, besides the Turing machine, the thing that Turing is the most famous
*  for is the Turing test.
*  Oh, God, let's not do it.
*  Well, exactly, exactly. I'm sure all your listeners are familiar with what that is.
*  I'm not even going to describe it.
*  I just threw up a little bit in my mouth just now.
*  Yeah, exactly. The Turing test is basically a sort of warmed over behaviorist outlook.
*  So when I teach the Turing test, when I teach philosophy of mind and I'm quite critical
*  of it when I teach it, because I think it's just it's not very philosophically sophisticated.
*  So I think that if you wanted to talk about philosophy of mind with him, you would have
*  to first kind of eradicate a lot of the latent behaviorism that seems to be informing the
*  way he's thinking about it.
*  So it's hard for me to know where he would come out once you've done all that, because
*  that would be such a big, big discussion.
*  Do you think he would just be against those symbols having an intentionality, a
*  representational quality to them that just no need?
*  I guess that's what you're saying. You don't know.
*  Yeah, I feel like I don't really know.
*  But I feel the keep. I just not think that was a very useful way of describing it in the
*  first place possible.
*  What's like just in your sort of day to day work?
*  What's what do you find sort of most challenging?
*  You know, what do you what kind of in terms of running up against obstacles or just mentally
*  taxing or like what's a bottleneck of your time?
*  Well, I think that for me personally, one, there are two things that are challenging.
*  One is that as we've been indicating, the work I do is it's not exactly interdisciplinary,
*  but it draws a lot upon other disciplines.
*  I mean, everything I do is philosophy, but it's philosophy that's informed by a lot of
*  other areas. So we talked about cognitive science.
*  Some of my work on foundations of decision theory draws quite a lot on probability theory.
*  Some of the work I did a computational theory mind, I was reading a lot of computer science,
*  computability theory.
*  And these are areas in which I'm not an expert, like I'm not trained in them.
*  I don't have a PhD in these areas.
*  My PhD is in philosophy.
*  I've studied these all these subjects to some extent, you know, to do coursework on them.
*  But that's a lot different than actually getting a graduate level PhD work.
*  And so, you know, there's always there's often a big knowledge gap that I need to hurdle
*  different disciplinary frameworks, different assumptions.
*  I have to sort of trace back through the literature to understand more basic stuff,
*  to go back and think that.
*  So I just I need to make sure I understand what I'm reading, at least at a reasonable level.
*  So then I can digest it. I can communicate it to philosophers so that they'll feel like they understand it.
*  The philosophers. Yeah.
*  So do you find yourself like when you contemplating whether you should go down a particular avenue
*  because you know how much effort it's going to take to get over the to establish all these principles and stuff?
*  Do you sit at the beginning of the road and look down and think, oh, no, is it worth it?
*  I probably should do that more.
*  But I mean, that's the great thing about having tenure is that you can go down some rabbit hole
*  and maybe it doesn't pay off. But you spent a year of your life on it.
*  And it's like, OK, whatever, I still have tenure.
*  So you're not going to you're not going to ruin your life by doing that.
*  So I probably am a little foolhardy and saying, OK, I'm just going to I'm just going to read this
*  probability theory textbook and try to understand it and do it again.
*  So, I mean, I have. Yeah, it's definitely it's a challenge because, I mean, at the end of the day,
*  I have to not just adjust it, but also then write a genuine philosophy paper.
*  So when I'm when I'm writing about the philosophy of cognitive science, I'm hoping at least not to just write a book report.
*  Like, here's what scientists are saying, but to actually do a philosophical analysis of it, that will be helpful to philosophers,
*  maybe helpful to some scientists.
*  So I have to digest it and then assimilate it and do the philosophy.
*  And then this is the other big challenge, which is just that I find at least that philosophy is really hard.
*  I find this in my teaching. I find it in my research.
*  I continually like struggling with just how to write a good paper, how to wrap my mind around the difficulty of the topics I'm working on.
*  I know my students often find my philosophy very hard.
*  It's just my poor teaching. But but but I think it's hard for a lot of professionals.
*  It's just hard to sit. You're not doing any lab work.
*  There's no there's no when you're doing philosophy, you're just sitting and thinking.
*  And you're not just thinking, but you're thinking about a thousand different pieces that are all interacting.
*  It's that is very. Yeah. Yeah. It's very hard.
*  If I didn't love it so much, I couldn't bring myself to get up and do it every day.
*  But because those two things I think are the most challenging for me.
*  This is always a fun one that no one wants to answer.
*  It's about consciousness.
*  Do you think that cracking the mental representation problem,
*  you know, how do mental representations get their aboutness, their their meaning?
*  Is that going to help crack the consciousness problem?
*  Understanding consciousness by by by problem, I mean understanding consciousness or are they are orthogonal?
*  So I come down on the side of thinking that they are most likely orthogonal.
*  So just to like give a little context, the mental representation problem that you're alluding to is,
*  look, we agree, minds do represent, they have the capacity to represent.
*  But how does that come about?
*  What is it about the mind or the brain or situation in the world that gives it the capacity to represent?
*  What what needs to happen for some neural state to then be about the world?
*  So that that's the mental representation problem or what in philosophy is sometimes people call it the problem of intentionality.
*  Then the consciousness problem, the consciousness, again, is one of these words that can be so many different things.
*  But but nowadays, usually, they're under the influence of David Chalmers's discussions.
*  But when people talk about consciousness, usually what they have in mind is the so-called qualitative aspect of experience.
*  So that would be like when you get hurt, you have a pain.
*  There's something like it feels a certain way to have that pain in the formulation that Thomas Nagle used.
*  There's something that it's like to have that pain.
*  So that that's the sort of qualitative aspect.
*  You can't really quite put it into words what it's like, but everyone who's felt pain knows it.
*  And so that that's that's this qualitative aspect.
*  And trying to elucidate that qualitative aspect is is something that philosophers have really wrestled with.
*  And I tend to have the view that probably these are these are pretty separate phenomena and understanding one is not going to help too much with understanding the other.
*  But I think we understand so little about consciousness in particular that I would not be surprised to learn I was wrong either.
*  Recently, I was listening to something about Sartre and Camus and that existentialism flooded back into me.
*  That was I think that was my introduction to philosophy.
*  Does existence precede essence?
*  Michael Escola.
*  I'm going to skip that.
*  This is black or white.
*  All right. No degrees.
*  Anything that you can think of that in your opinion is getting too much hype or too much focus or too much funding, for instance?
*  Well, one thing I'll mention, just because I basically said as much of print already, so I'm not really saying too much.
*  Is it is that one research program that's getting a lot of attention in philosophy right now is so-called predictive coding, which is a particular framework for.
*  Well, one way you could think of it is a framework for understanding how the mind by approximately implement Bayesian inference, although predictive coding doesn't necessarily have to be done in Bayesian terms either.
*  But in particular, there's a version of predictive coding espoused by Carl Friston, the so-called free energy approach, which is getting a lot of attention.
*  And I'm not opposed to people doing research on this in science.
*  I think all conjectures should be pursued.
*  But in philosophy, it's getting it's getting a lot of attention, which I think is disproportionate to the empirical success that this approach has had so far.
*  So there's a lot of workshops on predictive coding.
*  A lot of people are writing articles about it.
*  Philosophy workshops.
*  Yeah. Yeah. Philosophers talk.
*  Yes, exactly. Philosophers talking about like what philosophical morals can be drawn from predictive coding and people writing books about it.
*  And I just think this is a little bit premature.
*  I don't really see that much of this research program that warrants the quite extensive amount of philosophical attention that it's getting.
*  And here I would contrast this predictive coding idea with a more generic idea, just that the mind does some form of Bayesian inference, especially that the perceptual system does some form of Bayesian inference there.
*  I see there's quite a lot of good evidence for this.
*  And this has had a lot of really impressive explanatory successes.
*  So I kind of wish that philosophers, some of the philosophers talking about predictive coding would talk more just about generic Bayesian approaches to perception.
*  So it's not so much against the funding or the research that scientists are doing in their laboratories.
*  It's more I just feel this has maybe been a little bit overhyped, overemphasized in the philosophical community.
*  And I'd like to see more attention, more resources being spent on these other approaches that I think are a little more promising.
*  You're not only in print, you're also you participated in a four person, I guess, debate on predictive coding that's on YouTube and I'll link to it.
*  But but you lay out your position well there, too.
*  So I'll put people that way.
*  Finally, Michael, what's something that you used to believe that you now think is naive or wrong?
*  I used to be more skeptical about the value of neural networks.
*  So I was really influenced by by Jerry Fodor and Fodor was really, really hostile to neural networks.
*  And, you know, probably many of your visitors will be familiar with these debates about connectionism.
*  And this is like he's like an enemy.
*  And yeah, yeah, yeah.
*  That's for Fodor.
*  I think I still think that these connections models that Fodor position we're talking about were maybe a bit overhyped and not as good as some of the classical models they were contrasting contrasting them with.
*  But I'm much more impressed now by the power of neural networks.
*  This is partly just due to the fact that the fields are evolving.
*  So you look at the latest developments in AI, things like deep learning.
*  It's partly because I just know a lot more about neural networks than I than I did say when I was a grad student.
*  And I mean, certainly, if you look at a lot of the work that's being done now in computational neuroscience and especially this this relatively recent initiative, I guess you could call it of cognitive computational neuroscience, which now they have their own conference.
*  And people that are working under that umbrella affiliate themselves with that label.
*  Work such as, for example, work on how you might implement Bayesian inference in a neural network.
*  I think that a lot of that work is quite impressive.
*  So I think that maybe it's not exactly that I believe something that was wrong, but I was a little bit more pessimistic than I am now about the power of neural networks.
*  I think now it's clear that neural network modeling can really contribute a lot to to understanding how some mental processes are nearly realized.
*  And I still agree with photo position and then also with this book by Gallus, Don King, that this more classical picture that emphasizes Turing machines is helpful and is really needed in a lot of cases.
*  So I but I guess I just have a more ecumenical viewpoint.
*  Well, that's the valuable looking at some phenomena, some levels of description.
*  The neural network approach is more valuable, is valuable in other cases.
*  So it's just maybe a little bit more ecumenical, less pessimistic about the neural network framework.
*  I mean, we all want the same thing.
*  We can all be friends because we're all the same thing.
*  And that's a good read, actually.
*  That Gallus, Don King book, by the way, I think.
*  Oh, yeah. It's been a while.
*  Well, Michael, this has been really fun.
*  I mean, I have like a thousand more things to get to, but I really appreciate your time.
*  I've taken you over as I tend to do.
*  So I appreciate you going a little over time with me.
*  And thanks for taking me down the philosophical path, man.
*  This has been fun.
*  Thank you so much for having me on.
*  It's really been a pleasure to talk to you.
*  Brain Inspired is a production of me and you.
*  You can support the show through Patreon for a microscopic two or four dollars per month.
*  Go to braininspired.co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show and prohibit any annoying advertisements
*  like you hear on other shows.
*  To get in touch with me, email Paul at braininspired.co.
*  The music you hear is by The New Year.
*  Find them at thenewyear.net.
*  Thanks for your support.
*  See you next time.

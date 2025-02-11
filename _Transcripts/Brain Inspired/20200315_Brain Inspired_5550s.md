---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 5550s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 379
Video Rating: None
---

# BI 063 Uri Hasson: The Way Evolution Does It
**Brain Inspired:** [March 15, 2020](https://www.youtube.com/watch?v=UCfkGWuXoro)
*  אני אולי אעשה חלום, ועבורי זה סגרן לבהלת.
*  אולי הרעיון הוא חמוד אחר של מודלות,
*  ואם כן, אני רק אעשה על הרעיון, אני לא אעשה על נטרוקים ארטפסיטיים וגוגל,
*  אני רק אעשה על איך הרעיון עושה.
*  אם אני חלום ורעיון עושה דווקא,
*  אני אעשה את המחשבים שאני חושב,
*  אבל עכשיו אם אני
*  הוא Reverend
*  ש�כירza
*  ת me
*  ול saat ג pouring
*  This is Brain Inspired.
*  Hey everyone, I'm Paul Middlebrooks.
*  Welcome to the Brain Inspired podcast.
*  One approach to studying brains is to claim the primary purpose of a brain is to understand
*  stuff.
*  And the best way to understand stuff is to create internal mental models of the various
*  things and situations that you encounter.
*  Then when you're confronted with some new situation, you can apply your well-honed best-fit
*  model to that situation and better understand it or respond accordingly.
*  Another approach is to imagine the primary purpose of the brain is to do stuff.
*  And to do stuff, brains, with their trillions of parameters honed by eons of evolution's
*  cold and unforgiving gauntlet of survival, go all in and by brute force memorize and
*  fit everything possible without building an internal model.
*  Those two approaches, of course, aren't mutually exclusive, and there are other approaches
*  as well.
*  My guest today, Uri Hasson, used to think more like the first way, that our brains are
*  built to understand things, but the success of machine learning and more recently deep
*  learning along with his own introspection and experience in neuroscience has changed
*  his way of thinking to the second way, that our brains, by hook or by crook, are there
*  to do things.
*  Uri is a neuroscientist at Princeton who mostly studies how we integrate information into
*  memory hierarchically and over different time scales, and how multiple brains manage
*  to lock in with each other when we communicate.
*  Both of those topics could have taken on their own episodes, but I read Uri's recent perspective
*  in neuron about this fundamental difference in approaching how to study brains, and I
*  immediately emailed him and invited him on the podcast to learn more about it and share
*  it with you guys.
*  And here we are.
*  I highly recommend the paper that we discuss, which you can find in the show notes at braininspired.co
*  slash podcast slash 63.
*  So you guys know I don't advertise on the podcast.
*  I actually loathe ads in podcasts.
*  I despise them, you could say, but I completely understand why so many other podcasters do
*  their little ad reads and take the money, because it's easy money.
*  So, all that is to say I'm truly grateful for your support on Patreon, because it lets
*  me know that I'm earning that support.
*  I don't take that lightly.
*  And it's always on my mind to aim for and to strive to make something that you love, and
*  that inspires new ideas that take you to beautiful places.
*  So Ehsan, Eva, Martin, Michael, Sevan, Hiro, Dion, thank you for your recent support on Patreon.
*  Okay, enjoy Uri Hasson.
*  So we have brains and we're trying to understand how they work.
*  Now we have deep learning networks and neuroscience is now using deep nets as models to help us
*  understand brains.
*  But now we're trying to understand how deep learning works.
*  So that is we desire some succinct way to communicate how these networks accomplish what they do.
*  And we lack that succinct understanding, you know, so we feel unsatisfied.
*  We really want insight in the form of something that's human understandable.
*  Uri, welcome to the podcast.
*  Thanks for being here.
*  Happy to be here.
*  So you spend most of your time studying how we integrate and process memories over different
*  time scales and how two communicating brains resemble each other, among other things.
*  So what are you doing writing papers about how we'll never understand artificial or biological neural networks?
*  I don't think that we will never understand.
*  I think it was simply going to be a different explanation than what we were up to.
*  So, you know, as scientists, we're all about explaining and understanding stuff.
*  And when we have big models with millions of parameters, even billions of parameters now.
*  We don't feel that we understand them.
*  They are opaque.
*  They're not as simple.
*  We cannot come with a story that we're up to tell.
*  And it's happening both when you look on biological neural networks, if you look on the brain and it's like a millimeter of cortex,
*  we have millions of synaptic weights.
*  So it's other parameterized model.
*  And it's happening also in artificial neural networks.
*  In each model, you have billions of parameters.
*  And I think we opt to be somewhat like physics, you know, when Newton look on the world,
*  he come with a very simple formula with few parameters, mainly linear interactions that can explain many, many phenomena.
*  And we hope to do the same with the brain.
*  We will come with this like rule based computation that is it to understand with few parameters,
*  hopefully linear interaction that will explain how the brain process the world.
*  And also like physics, we hope that similar to Newton law, the brain going to be very smart in the way that it operates.
*  Yeah, right.
*  And suddenly we have this like new family of models called deep neural networks that actually were inspired by how the brain is working.
*  But people also think of them as way, way, way more simple than the brain.
*  And in these models, you don't program them.
*  You let them learn from the data by optimizing a very simple objective functions.
*  You know, they are not doing something smart.
*  They simply by trial and error get slightly better, slightly better till they get to act.
*  And to our surprise, and this is why I started to look in these models,
*  they start to do as good as humans on many cognitive tasks.
*  We need to say immediately they don't do many things that human can do.
*  They don't. We didn't solve cognition.
*  We don't have like a powerful AI that can do as humans.
*  But in many, many cases, in many, many cognitive problems that we worked on,
*  suddenly they do almost as good, sometimes even better than humans.
*  And it's really bothered me at the beginning.
*  I was saying, why people outside of my domain,
*  like engineers in computer science or in companies like Google,
*  solve problems that we care about and they get models that are way better than our models.
*  And actually performing the tasks.
*  Yeah, by performing the tasks.
*  And I think the main insight before we go to the details exactly about the mechanic is to understand
*  this model does not try to explain.
*  They try to act.
*  And you measure how good these models are,
*  not by amount of variance in the signal they explain,
*  but how they perform the task in real life.
*  So how good they are acting and predicting the next moment.
*  That's what they do.
*  So let's take a simple model of face recognition.
*  Now, as you know, we have this software,
*  these deep neural networks that recognize faces in the real life.
*  All over China right now, right?
*  All over China, exactly.
*  Way better than humans even, right?
*  Because each one of us can recognize about 5,000 faces, more or less.
*  They can recognize all people in China.
*  It's like way, way better than you will ever do.
*  And they do it in real life.
*  It's not like you have a control simplified faces that you control the features.
*  They are able to recognize us, occluded different lights,
*  different viewpoints with many people, dark light.
*  So they work like the human thing,
*  and no one ever programmed them and saw them even the faces of eyes, right?
*  You don't program the solution into them.
*  Yeah, like you used to in AI, in good old-fashioned AI.
*  And also in old-fashioned neuroscience.
*  If you think about it, what we do in neuroscience,
*  we also say, let's look for the rules by which the brain processes faces, for example.
*  So now you have a model, let's compute the distance between the eyes,
*  let's have the features for different facial features and some computation.
*  And then you force your computation into your stimuli by simplifying your stimuli.
*  And now you're working in a very contrived space.
*  And then you look for your hypothesis in the brain.
*  So in a way similar to old, good, fastened AI,
*  this is also a new scientist that puts the problem,
*  because we want to understand the rules.
*  And if I can formulate the rules,
*  by giving you simple features and simple operations,
*  then as a scientist I have the satisfaction that I'm understanding my model.
*  So this is why I ask, wait, this is a new type of models that we don't like
*  as neuroscientists or as scientists,
*  because we have no satisfaction of these simple stories
*  that we want to tell and this feeling of insight and understanding,
*  but they work way better than all our models combined over 80 years
*  or one hundred years of research, right?
*  Yeah, yeah.
*  Well, yeah, let's take a step back because we already hit the ground running here.
*  So I'm sure I'll say this in the introduction,
*  but we're talking about your recent paper,
*  Direct Fit to Nature, an Evolutionary Perspective
*  on Biological and Artificial Neural Networks.
*  And I guess the point that you're making now and that you make in the paper is that
*  neuroscience and AI, let's set aside good old fashioned AI,
*  but the more modern distributed representation,
*  neural network connectionism AI,
*  have fundamentally approached intelligence in different ways.
*  Am I reading that right?
*  In that AI has approached it in terms of accomplishing the tasks,
*  whereas neuroscience and the behavior of the network,
*  whereas neuroscience has approached it in a very controlled manner,
*  simple tasks, very controlled experiments,
*  and simple models to explain those experiments.
*  And those are fundamentally different.
*  Do I have that right?
*  Correct.
*  Basically, the way to summarize it is,
*  neural networks designed to do stuff,
*  and we were thinking that the brain is designed to understand stuff.
*  So now the question is, does the brain fundamentally try to understand or try to act?
*  If it tried to act and it can act without understanding,
*  and now we can see that these neural models give us these alternative models
*  that you can really act without understanding,
*  maybe the brain will use the same tricks.
*  And if the brain's purpose is to act,
*  then we're using the wrong way to understand how the brain is working,
*  because we really think that the brain is the smartest organ on the planet
*  that understands the world,
*  and through this understanding it can extrapolate to many new situations.
*  And this is why it's an interesting family of models to explore.
*  Why are we so driven to understand then?
*  Because we are scientists.
*  If you will tell someone, forget about understanding,
*  start to think about doing,
*  you tell them you are not a scientist, you are engineers in Google.
*  Basically, the business of scientists is to understand,
*  but as he was saying before, if you start to understand these models,
*  they are simple models.
*  It's like evolution.
*  You have three components to understand,
*  and then you replicate it over iteration.
*  So they are not complicated models.
*  They are actually way simpler than we ever imagined the solution to be.
*  So why won't we be happy that it's a mistake to say that
*  less parameterized models are more parsimonious?
*  I think this is the deep mistake.
*  Because basically, ideal models, they are like intelligent design.
*  They are pure, and everything was designed.
*  And this is why evolution is more parsimonious,
*  because these treatments of generation allow you to do more simple processing.
*  And in machine learning, it's the same.
*  These other parameterized models allow you to use more simple operations
*  to get to the same behavior without understanding.
*  So this is why they are more simple models.
*  And you think that fits with a brain efficiency regime?
*  Yeah, I think it's more efficient because...
*  Yeah, so I think all the notions that actually the brain is lack of resources
*  and the code have to be optimized, it's a mistake.
*  But I think we want to think that, right?
*  It makes us feel good to think that...
*  Because it seems smarter to be able to model the world and to understand things
*  rather than what we're going to talk about in a minute,
*  It's just mindless brute force predictive matching to the world,
*  you know, statistics matching.
*  I agree. I mean, this is why Darwin and evolution is such a good analogy.
*  It's even more than analogy in this case, but...
*  Before Darwin, we wanted to say they were like intelligent design,
*  the design, for example, our eye to process information.
*  So there was like a design and planning.
*  And suddenly Darwin come and say, no one designed it.
*  It's simply you have a very simple operations and other three more iterations,
*  you get to the optimal solution without even understanding the problem
*  you are trying to solve.
*  And we were fine with it, the scientists,
*  but it was like only one place that we want to save this like divine intervention
*  and intelligent design. And this was our brain.
*  Okay, everything is brute force, but our brain is very smart.
*  That's right.
*  We wanted to keep this thing and I was saying,
*  oh, maybe also the brain is using this operation and it will be tough.
*  All right, let's hold off because I want to talk about evolution in a minute too.
*  So what is direct fit and its main implications,
*  just the broadest general description.
*  And then from that, there are all sorts of implications.
*  I mean, it's a really fascinating idea here to me.
*  And so it's helped to change my worldview.
*  So thank you.
*  So in direct fit, you take the shape of the outside without understanding.
*  So now if this is true and you have a control experiment with,
*  let's say you create a stimulus with a given structure,
*  let's say the eyes, you do like a distance between the eyes and the nose
*  and the shape that will define all faces.
*  You have now a parameter face with three dimensions.
*  The brain will fit to it.
*  So it will fit and it will look like your experiment will always work.
*  Without any model of what a face is, it'll fit to it.
*  Yeah, if you think about the figure with the sinus,
*  so you take a sinus and the brain takes the shape of the sinus.
*  A sinusoidal curve?
*  Yeah, so if this is your input, that's the structure we get.
*  You always get the structures of what you give it.
*  And then it will interpolate with these dimensions.
*  It doesn't learn any rule about nothing, right?
*  So that's what confuses people because in a way,
*  the brain can always fit to your experiment and give you the structures of the input to give it to it.
*  And if you're a scientist, you control the input.
*  That's the depth of direct fit that I can't...
*  I don't manage to explain this to people.
*  Because what you see more and more that whatever experiment you do,
*  you always get what you want from the brain.
*  Because this is the point of the direct fit.
*  If you give a structure the input, this model is going to fit to the input.
*  And you see why it's a tricky thing to explain.
*  So when you say direct fit, I'm thinking all the way over there and I should not go there.
*  This point is going to be missed.
*  So we can talk about direct fit in terms of interpolation and...
*  Interpolation is the question, then I think it's easier.
*  Yeah, let's approach it that way.
*  So, I mean, is one way to say it that direct fit will...
*  In an overparameterized model...
*  So overparameterized models used to be...
*  Well, they still are.
*  It's a looked down upon, right?
*  Because what you want is a perfectly parameterized or even underparameterized model,
*  because that's the simple explanation.
*  But the whole point of direct fit is if you have an overparameterized model,
*  one of the points, it will fit whatever you give it.
*  Without needing to know anything about the thing that you're giving it,
*  it'll just brute force fit the statistics of what you're giving it.
*  And is this what you mean by interpolation?
*  Yeah, it's absolutely correct.
*  So, you know, if...
*  Let's say I have like a data point sampled with noise from a parabola.
*  Yeah.
*  And I have like 10,000 parameters.
*  And remember, as a scientist, I need to understand the underlying structure, right?
*  I want to understand that these 10,000 points were sampled from a parabola with two variants.
*  That's what I want as a scientist to understand the underlying structure.
*  So now I'm giving this data set to my student, and my student is really eager,
*  and he comes with a linear fit, and of course, linear fit cannot fit a parabola,
*  so it's like completely failing.
*  So you say, okay, let's do a more nonlinear, more complicated fit,
*  and now you're coming with like a three-parameter,
*  and now we have like a perfect fit of the parabola.
*  And now he's very happy.
*  But you say, if three parameters are better than two parameters,
*  let's use 100 parameters or 10,000 parameters,
*  and that's what we call overfit,
*  because we know that the more parameters you have,
*  your model is more flexible,
*  and it's going to capture the entire variance in the data.
*  Then you have a line that goes through every single data point.
*  Every single data point.
*  High variance, yeah.
*  And if you do like a control fit that you're not over explosive fit,
*  so you can get very tight fit if you regularize.
*  Get a very tight fit,
*  and then your error on the training set is zero.
*  But as a scientist, we're going to say,
*  you learned nothing about the data set, you overfit,
*  and we're going to really say,
*  we're going to look down on the student and say,
*  you didn't learn anything, you're not a good student,
*  you're not a good scientist, because you didn't explain me
*  these like simple three parameters line that can capture all this model.
*  You didn't explain anything?
*  You didn't explain anything, and our notion is that your model
*  should always be tested on a new data set,
*  and then you need to extrapolate.
*  So if you have this like parabola in mind,
*  now if you think that you have like new values
*  that you sample from completely new place on this like axis
*  that you never been before,
*  this overfit will not know how to go there,
*  but the parabola, assuming the parabola is the right principle,
*  are going to extrapolate.
*  So we are thinking extrapolation is what the brain is doing.
*  The brain have a very limited exposure to things,
*  and from this like a very small exposure,
*  now we need to extrapolate to all the new situation
*  we got in the world.
*  That's how we think about the brain.
*  The brain learning the rules and then extrapolate.
*  So the brain is learning the equation for the parabola,
*  and then this is our sort of intuitive notion,
*  and then we can extrapolate and predict well
*  outside of all of the parabolas that we've seen
*  because we know the equation,
*  our brain knows the equation for a parabola,
*  so it'll fit it just right.
*  That's our intuition.
*  Yeah.
*  Exactly.
*  So we think about the like the brain
*  is our good scientist student.
*  Like he learned, he understand,
*  and now he can use this to extrapolate.
*  Now, what's happening with machine learning
*  and deep learning is completely opposite.
*  Suddenly, they don't have limited data set,
*  they have big data sets, right?
*  And this big data set cover most of the possible situations
*  you're going to encounter in the world.
*  And these data sets are multidimensional and complicated
*  because this is the real life data set.
*  And then they have big models,
*  and sometimes these models have more parameters
*  than the examples you're going to see.
*  That's the most common situation I think these days.
*  Yeah.
*  And that's going against what we're telling our students.
*  Remember, when you say if you have an overparameterized model,
*  you will always overfit.
*  And by overfit, you will learn nothing
*  and you understand nothing,
*  and therefore you won't be able to generalize
*  because you're going to overfit to your examples,
*  and when you get new examples,
*  your model will be useless.
*  That's the extrapolation problem.
*  So now you ask,
*  so why this model are overparameterized
*  and fit to big data, why do they learn anything?
*  This is against our intuition
*  because they didn't learn any rule or simple rule,
*  or at least we cannot know whether they learned
*  because we didn't train them
*  and we didn't tell them the rules.
*  And we can't extract some simple rule from them.
*  Yeah, so why are they working?
*  And it's bothered me for a while.
*  And it's like a mystery in machine learning.
*  They tell you this model are not overfit
*  in the sense that they can really,
*  if you give them new test data sets
*  that weren't in the training,
*  they were really going to get denounced and correct.
*  And then we were thinking,
*  maybe we got it completely wrong in the statistical textbook,
*  and it's a simple mistake,
*  and it's like a solution that we really were thinking
*  that it cannot work,
*  but actually in big data it might work.
*  Maybe the brain never learned to extrapolate,
*  or at least these models do not learn to extrapolate.
*  Maybe all they do is they stay in this interpolation case.
*  So if you go back to this 10,000 example in the parabola,
*  this is our training set,
*  and I would think between these parameters of learning,
*  of course I can sample 10,000 new examples
*  from the same distribution
*  in a way I can test infinite number of new example.
*  Yeah, you have a parabola from negative one
*  to positive one on the x-axis.
*  Exactly.
*  You can put as many data samples
*  as you want within that sample.
*  You can sample as many new as you want.
*  So that if you go to minus five to five,
*  you're going completely failed.
*  But between this minus one to one,
*  you can have as many new examples as you want,
*  and actually your model with 10,000 parameters
*  that you were telling to your student
*  to throw to the garbage,
*  going to work just as well as the three parameter parabola,
*  because the statistics of your example in the training set
*  and in the test data set are the same,
*  and therefore the models will work and interpolate.
*  And that might be the reason why
*  machine learning is so effective,
*  because when you have a big data set,
*  basically you cover most of the parameters
*  that you're going to encounter.
*  We always think about each situation is very new,
*  but if you start to think about it
*  as statistical learning mechanism,
*  actually our conversation,
*  you see we're not in conversation like a week ago.
*  Of course, it's different words and different content a bit,
*  but we have similar conversation with other people.
*  So if we think about, for example,
*  walking to my office,
*  it will be similar of walking next week
*  when I will travel to Boston.
*  It's going to be similar statistics.
*  And if you start to think
*  that that's what the brain is doing,
*  it doesn't try to imagine completely new situation
*  that it never been before.
*  It's starting to learn the parameter space
*  is going to act within,
*  then interpolation is not a bad solution.
*  In a way, it's even a strong solution
*  because it's more simple and more robust.
*  Within the interpolation zone,
*  within the training set.
*  Within the interpolation zone.
*  Yeah.
*  So take for a second,
*  so let's go for a second for evolution.
*  I think that will help us a bit.
*  Think about, you know,
*  now there is like studies that the ocean temperature
*  is going to increase by two degree.
*  Yep.
*  Does it?
*  One to two degree.
*  And 80% of the species in the ocean going to die.
*  And you say, ooh, that's like crazy over fit.
*  Really, 2% increase in the temperature,
*  80% in the creatures in the ocean going to die.
*  This means that the solution that evolution found
*  is really optimized to this temperature.
*  And we know that once you increase it,
*  80% of the species might die,
*  but you know that this other 20% going to evolve
*  and fit to this like new.
*  Continue to evolve and fit.
*  And then we'll be fine with this like new parameter space.
*  So that's telling you in a way that you can think
*  about evolution as a very narrow fit to your environment.
*  You know, if you live in the deep ocean,
*  if you live in the desert or live in the forest,
*  you're going to fit to your environment.
*  That makes it sound very delicate.
*  It's very delicate and also very powerful
*  because now you don't need a solution
*  that will generalize to all possible conditions.
*  You need a solution that will allow you
*  to survive in this context.
*  And also because evolution is flexible,
*  and then you know if the outside is changing,
*  the parameters, now you can change your fit.
*  So you have also something dynamic that can always evolve.
*  So if you think about evolution,
*  you will say this is a very elegant solution
*  because now you have a general principle
*  that can explain how all the living things evolve over time
*  and change to fit.
*  So evolution is not a theory that can predict
*  how the tree of life is going to look millions here from now.
*  You don't have this extrapolation force in evolution.
*  Evolution tells you there is a mechanism,
*  and it all depends on so many nonlinear interactions
*  that will determine the fit in one million years
*  that you cannot predict.
*  Another thing that is amazing in evolution,
*  it's not, and I don't know why we were stuck,
*  what amazing in evolution that we are,
*  we and the apes are relative.
*  That's true in evolution,
*  but the most amazing aspect of evolution for me
*  is that me and the fly
*  and the trees and planets are all relatives.
*  So that's what amazing about evolution.
*  We're all relatives because we all started from two cells
*  that start to merge and split.
*  Right?
*  And given four basic principles,
*  now you can explain how all this diversity of solutions
*  and fit in the tree of life emerges.
*  So evolution is a very simple solution
*  that can fit to a variety of situations,
*  and you have this amazing variety of solution in nature.
*  Now, if someone will tell you,
*  wait, but evolution is not inefficient,
*  it's not a parsimonious solution, right?
*  Because why?
*  Look, for evolution to take place,
*  you need like 300 million years and trillions of iterations.
*  That's not sufficient, that's not parsimonious.
*  I rather God come and give me the optimal solution,
*  and then I will have like way few iterations,
*  and in a few years they will say,
*  I think you're missing the point in evolution.
*  The beauty of evolution is simplicity
*  and it's like mindless iteration over time.
*  Evolution doesn't care.
*  It doesn't care,
*  and it's very efficient and parsimonious scientifically.
*  So now I think we do the same mistake with the brain.
*  We say three parameters,
*  it's a very simple solution,
*  it's like 10,000 parameters model.
*  So therefore, the student parabola
*  model is more parsimonious scientifically,
*  and therefore I'm going to choose it.
*  But actually not, the 10,000 parameter is way more simple
*  because you have a very simple operation
*  that fit to the environment
*  and can give you optimal solution,
*  a model that can work for faces,
*  that can work for a learning accent,
*  that can learn to recognize voices and so forth.
*  So this simple solution,
*  can fit to many different cognitive domains
*  and get good results
*  without ever understanding the underlying function.
*  And this is why I'm thinking actually
*  it's more parsimonious solution
*  than what we were hoping to in neuroscience.
*  So in a world with high statistical structure
*  within many domains,
*  one simple or straightforward,
*  I don't know how efficient it is,
*  but one straightforward solution
*  is to have a very simple solution
*  but one straightforward solution
*  is to overparameterize with the ability
*  to extract high statistical regularities
*  from that statistical structure.
*  Correct, that guide your accent.
*  And this is why if you give prime,
*  and now we go back to the beginning,
*  if you really give prime to accent,
*  you want to do stuff.
*  You don't really,
*  the brain is not a scientist.
*  It doesn't need to understand the underlying structure.
*  You need to know that whenever he act,
*  he get it right.
*  And if he doesn't get it right,
*  you correct your accent.
*  Right, so this is why you maximize
*  an objective function to do something.
*  And if he managed to do it,
*  you're going to survive.
*  If not, you're going to die.
*  And you don't have time
*  or the resources to get this ideal understanding
*  of the underlying rules
*  in order to be smart
*  and act with understanding.
*  I don't think this is the prime objective of the brain.
*  Okay, so are you on board with the idea
*  that action is the primary objective of brains?
*  Yeah, brains have to do stuff.
*  Okay, that's my, I love this idea as well.
*  So I'm going to have Galit Shmueli
*  on the show next episode, actually.
*  We're going to dive a little bit deeper
*  into the difference between explanation
*  and prediction in modeling.
*  She's an expert on this, so it'll be fun.
*  So we don't need to dive too deep in that,
*  but I mean, we as humans,
*  we want this nice sentence long summary
*  of what brains do
*  and to feel like it makes sense, right?
*  And to feel like it's special, right?
*  In some sense.
*  And to feel like our brains are powerful
*  as world builders, as modelers,
*  universe creators and so on.
*  What is the difference,
*  what is the relation between explanation and prediction
*  with respect to human interpretability?
*  So I think first,
*  I think we should not think about humans
*  to the beginning because you know,
*  all mammals have brains and brain have evolved.
*  And so it will be easier first to leave humans
*  out of it for a second.
*  We're going to return to humans.
*  Sure.
*  Think about all brains
*  have to act in order to survive.
*  And you know, and because the world is dynamic,
*  you want a mechanism that you can learn the statistics
*  and adapt in a smart way.
*  And this is why I think why brains are
*  in the next stage in the evolution tree
*  because they allow you more flexibility
*  because they allow your network.
*  You can optimize your network over evolution.
*  And that's in a way, think about the fly brain,
*  it's still have plasticity,
*  but you know, but 80% of it or 90% is determined on birth.
*  You can fly, you can sense,
*  and then you have to adjust a bit
*  because even for the fly brain, it helps to learn, right?
*  You can mate.
*  You can mate.
*  And as you go in the evolution tree,
*  you have more and more this plasticity
*  that you can fit better to the world
*  and have more dynamic responses, right?
*  And learn more.
*  And then you get to the human brain
*  and the human brains is like,
*  first the brains become bigger and bigger.
*  So, you know, if you think about the number of synapses
*  and that we have relative to primates, we have way more.
*  So we have way more plasticity, right?
*  And also we have way less things
*  that you program by evolution.
*  You know, most animals can walk immediately
*  when they're born after a few hours
*  of tuning the parameters for humans to learn to walk.
*  It takes like a year.
*  You have three kids, right?
*  I have three kids.
*  And if you remember the beginning,
*  the first three months they don't move.
*  You leave them on the sofa.
*  They're going to stay on the sofa.
*  After three months, you're going to worry
*  that they will like turn away and fall from the sofa.
*  Oh, I put mine on the bookshelf.
*  That's how I...
*  Exactly.
*  And it's really safe only for three months.
*  But after you know that they learn something.
*  So in a way, and think about the flexibility
*  that you give to the system to learn,
*  you get a lot of plasticity
*  and way to adapt to the environment.
*  So it's really beneficial for our species.
*  And it's also true that at the end of the day,
*  our brains can do even more than that.
*  You know, take physics as an example, you know,
*  Newton had a brain that can look on the world
*  and come with the law of nature, right?
*  And understand.
*  So we should not think that these models
*  give us the final solution to explain
*  what is a human being,
*  because I think we have a capacity
*  to extrapolate and understand the underlying structure.
*  So in a way, I still believe that we are,
*  there is something God-like in the brain.
*  And I don't want to say that we all only direct fit
*  and other parameter is fitting.
*  What I'm saying is,
*  I think the foundations of all brains,
*  including us as biological creatures,
*  is this like robust fit, other parameter is fitting.
*  And now I can say maybe 80%, maybe 90%.
*  Some of my students argued that 95% even
*  is all about this like robust fit.
*  But there is also something that is missing in these models.
*  And you know, you don't want to learn calculus
*  from examples, right?
*  You need to understand the rule of calculus,
*  you know, to perform it.
*  So there's something beyond, yeah.
*  There is something beyond
*  and something is still missing in these models.
*  And it's important to talk about
*  what is missing in the model as well.
*  But the foundation, I think of all brains and all animals,
*  and I would say 80, 90% of humans as well,
*  is this like massive overfit.
*  It's such a generalized and simple
*  and yet robust solution.
*  So it would be crazy to think that the brain
*  really tried to understand the rules
*  of everything to operate.
*  We went in the wrong direction in neuroscience
*  and now we need to correct for it.
*  Well, it's funny you should mention 80%.
*  I don't know the exact number of the cortex in volume.
*  It's something like that,
*  that our cortex takes up in our brains volume-wise.
*  I know the cerebellum has the majority
*  of the neurons, et cetera.
*  Anyway, whatever number it is,
*  the cortex is a broad swath of our brains.
*  And you know, there's this recurring idea that,
*  well, maybe what deep learning networks
*  are really modeling most closely is cortical processing.
*  And also the idea that cortical processing
*  is this really general purpose processing.
*  And then you have all these other...
*  So first of all, you have modularity
*  in the cortex and in the brain.
*  And you have all these subcortical structures
*  interacting with the cortex and directing things
*  that are evolutionarily conserved and very specialized,
*  but very much involved in cognition.
*  I guess my question is,
*  do you see this direct fit brute force modeling
*  that neural networks do and that you're conceiving of
*  as 80 to whatever percentage of what brains are doing,
*  do you see it as more of a cortical mapping
*  onto the cortex cortical function or brains in general?
*  I think brain in general,
*  I think I will say 80% of the brain.
*  It's fine that maybe the top 20% of the neurons
*  in high-level cortical areas on the top of the hierarchy,
*  so I have additional features that we don't understand.
*  Or it might be that you simply plug one neural network
*  to another neural network and let them talk
*  and suddenly new phenomena emerge.
*  But this gets to your hierarchical time scale
*  from sensory processing that can keep a very short memory
*  and as you go up in the hierarchy,
*  you can keep longer and longer memories.
*  And it also goes to our brain-to-brain coupling
*  because if you couple one neural network
*  but no sum structure to another neural network,
*  then by this coupling,
*  you can make one neural network smarter
*  and they can start to interact.
*  And there's wonderful work coming from deep mind
*  and open an eye that you have this network of agent
*  that start to learn to play a game together.
*  So you have independent players starting to work together
*  and again, it goes to the evolution's perspective
*  that if we have two units interact,
*  they become smarter than each unit by itself.
*  And then if you have a society of networks,
*  you can get a more and more complicated objective.
*  So there's like stepped in the evolution and in the learning.
*  So these models can really push us to new places
*  that five years ago, I will never dream of me looking,
*  I really look down on these models.
*  I have to admit, five years ago,
*  if you tell me that this model is going to solve anything,
*  I say, yeah, it's simply brute force optimization.
*  They don't have any.
*  So five years ago, you were like,
*  ah, you spat over your shoulder
*  and said it's brute force optimization.
*  And now you smile and you say, oh, that's the solution
*  is brute force optimization in Reins.
*  That's so interesting.
*  It's difficult to say basically what we're saying
*  is that the solution is less ideal.
*  I mean, we were all saying that, okay,
*  in evolution we gave up intelligent design,
*  but our brain is really intelligent.
*  We all have a very idealistic
*  and simple and interpretable solution.
*  And as a scientist, we felt our notion is to explain
*  and to understand.
*  And if you have like big or packed model,
*  you're not a scientist, they go to be, I don't know.
*  But it's funny that we forgot in the process
*  that when we say a model with billion parameters,
*  it's not a model.
*  Now that's basically we say a scientist.
*  You didn't explain anything.
*  You duplicate the panel.
*  We forget that for the brain billion parameter,
*  it's like two voxels.
*  Yeah, right.
*  Like it's a tiny portion of the cortex.
*  We have this like number of parameters.
*  So they gotta be doing something, all those neurons.
*  Exactly.
*  So the brain is way more of a parameter
*  than all the model in Google combined.
*  So why do we think that actually the brain is ideal
*  and simple and understand when we see this
*  like other parameter is the organism that we're working with.
*  So do you think then the solution is just to build
*  the most massive, most over parameterized model ever seen
*  and that will spit out the number 42
*  if you're, or solve intelligence?
*  No.
*  So if you look on machine learning
*  and this is something that people
*  that work with this model really understand
*  and people from the outside don't really respect much.
*  Respect much.
*  It's an engineering effort to optimize the structures
*  and the parameters to get the action that you want to do.
*  So you are not spitting a number in machine learning.
*  You act, right?
*  And you get the action that you want.
*  For example, in facial recognition,
*  you kind of remember the people in China.
*  If you talk to your Google device,
*  you want it to understand your speech
*  no matter how heavy is your accent
*  and how suffering your audience now
*  to listen to my accent,
*  they need to understand it
*  in order to get what I'm saying.
*  And it's not an easy task.
*  So you never measure a deep neural networks by a number, right?
*  42.
*  And if you have a deep neural networks
*  that going to talk like humans,
*  then you will say, okay,
*  then they pass the Turing test, right?
*  That's basically,
*  and that was what the notion of Turing
*  and say instead of asking whether machine consciousness,
*  you ask can they pass this if they are conscious, right?
*  Can they act as if?
*  Because he gave prime on the behavior.
*  He didn't give prime on the understanding.
*  And I think this is exactly what machine learning are doing.
*  They're giving prime on your behavior.
*  So it's not only a matter of big models.
*  It's also, you have to have a very smart objective function.
*  You have to have a very smart circuits
*  that can generalize with many, many small tricks.
*  And if you look on the machine learning now,
*  each day you have a new model
*  with slightly better learning rule
*  and slightly better connectivity
*  and you add the current activity
*  and then you add like LSTM on top of it.
*  And then you let it forget in the right places
*  and then you add differential computing
*  to save the episodic states.
*  And it's like trick that you do.
*  It make it slightly more similar to a brain
*  because you add more components
*  and then you also got the solution slightly better.
*  And I think this is the game that we are playing now.
*  And it's not a fun game
*  because we wanted to have like this like
*  a rolling understanding and finally we say,
*  oh, actually it's all about the design of the circuit
*  and the learning goals and then scaling it up
*  from a small circuit with 10 neurons
*  now to billion neurons that you duplicate
*  is like a computational device and then you get.
*  There's no real reason that I can think of
*  to think that over time the solution in machine learning
*  will converge to anything that does resemble brains.
*  I mean, so the original neural networks
*  were based very loosely off of brains.
*  And what you just said was that,
*  you stack a few LSTMs together,
*  you make some recurrence in there
*  and it makes a little more brain-like,
*  but I don't know that necessarily adding the tricks
*  is converging toward more brain-like to me.
*  And I'm not an AI, I'm not a machine learning expert,
*  but I don't see it trending that way.
*  I think you're right.
*  I think basically the point is that I think
*  they're in the same family of models.
*  Okay, so now when you have a family of models,
*  actually you will say, okay, they're similar
*  in this aspect and they're different in this aspect,
*  because it's a family of models.
*  Some people can say the brain
*  is completely different family of models
*  and now you bring the latest toy
*  and call it that it's similar to the brain.
*  You know, when Freud came with his model,
*  he was really impressed with the hydraulic system.
*  So now you say the brain is an hydraulic system.
*  Hydraulic system?
*  Yeah, because you suppress over here
*  and then it like a...
*  Sure.
*  Explode over there, right?
*  They put in a hydraulic metaphor.
*  And then people say in all the AI,
*  okay, computation and representation,
*  like all programming, this is the brain
*  and then they give the metaphor of representation
*  and computation.
*  And now we come with like metaphor of machine learning.
*  So we have this like new toy
*  and you say the brain is alike,
*  but the brain is always something different.
*  In a way I agree that the brain is slightly different,
*  but I think there's a lot of similarities.
*  So this is why I'm saying it's within the same family
*  of models actually.
*  But also the brain was developed over 300 millions
*  of generations.
*  So we have this like this evolution iteration.
*  And if you look across species,
*  you can see that the brain circuitry is really developed
*  and humans got to this like one type of neural networks
*  and there is no reason why people in Google
*  will get to the same solution, right?
*  They have a different constraint.
*  So I don't think the task of Google
*  is to create the circuit that is going to be identical
*  to the brain.
*  Also, you know, there are silicon machine
*  and we are biological machine
*  and I'm sure there are like differences between them
*  that are really important actually.
*  The thing I was saying is that
*  for people in the artificial neural networks,
*  because they can take really inspiration
*  from looking on biological neural networks
*  and if they understand the tricks that the brain is using.
*  So for example, episodic memory, right?
*  Don't only generalize across examples.
*  Also remember this particular example
*  with this particular dog that bite you
*  when you walk in the neighborhood.
*  That will really be good because
*  most of the dogs are nice,
*  but also remember this particular dog.
*  Oh my God, I just got bit by a dog yesterday on the trail.
*  I remember it, yes, very well.
*  And you don't want to generalize
*  and do statistical learning and update your entire model
*  to say now all dogs are scary
*  because that will be overcorrection.
*  So this is why episodic memory really help you also
*  to generalize on one end,
*  but also remember specific outliers, right?
*  So for example, this trick,
*  when people are in machine learning
*  in deep mind use differential neural computing
*  and now they have a component in the network
*  that also save the state of the networks,
*  that are the episodes,
*  and also generalize across examples
*  in another part of the model
*  that this is helping the model, right?
*  So it's an external memory essentially.
*  That's like external memory.
*  So, and this is a trick that the brain is using as well.
*  So that's what I'm saying.
*  You can get inspiration from how the brain is working
*  and it's going to improve how you design the networks.
*  And the same it's going for us.
*  We didn't know that this like simple optimization
*  over so many examples will be such an effective solution.
*  So we didn't know that this like a direct fit
*  and optimization can give us cognitive machines
*  that really work.
*  And now, so basically we learned something
*  from this model.
*  This is what I'm saying five years ago,
*  I didn't know that.
*  So I think it's go both ways.
*  We should learn from artificial neural networks
*  and they should learn from biological neural networks.
*  Because I think we are in the same family
*  of solutions and models.
*  And you know, I might be wrong
*  and I over here, this is a disclaimer for the audience.
*  You know, maybe the brain is completely different family
*  of models.
*  And if yes, I only care about the brain.
*  I don't care about artificial neural networks and Google.
*  I only care about how the brain is working.
*  If I'm wrong and the brain is working in different way,
*  I will have to switch the way I'm thinking.
*  But now, if I'm right,
*  and we got to this like new family of models,
*  and this is the family of models we should look at,
*  then we need to live a lot of the practices
*  and the way we were thinking before.
*  So I don't know if it's a junction and we don't know,
*  but what we say in this paper
*  that we should now really consider
*  this new family of models and if they are relevant,
*  we really need to revise the way we are doing science.
*  But do you envision,
*  so one of the things that we do,
*  especially in neuroscience,
*  is move the goalposts essentially.
*  So, you know, it almost depends
*  on how you define intelligence, right?
*  So you could say at, with a given level,
*  a given definition of intelligence,
*  then brains and AI systems are all within the same
*  family of models.
*  And you might end up with something
*  that you would be satisfied with saying,
*  okay, that is an intelligent behavior process,
*  processing or whatever.
*  But then I think it's called the AI effect, maybe,
*  where, you know, once AI does something,
*  it's no longer considered artificial intelligence, right?
*  And, you know, so at what point, you know,
*  are we gonna get to the point where AI can do
*  all the things that we can do,
*  but now just consciousness is left or, you know,
*  how do you envision this playing out in the,
*  and then we'll get back on track here in a second.
*  Yeah, I think you're right.
*  It's like it's a moving target,
*  and there are some people that will never be satisfied,
*  and they will never be honest about it.
*  So, for example, if I'm going to tell you
*  consciousness have no function, it's an epiphenomena.
*  Let's say this is your stance now.
*  But, you know, I really believe
*  that consciousness have a function.
*  I cannot believe in this.
*  So then I say, oh, okay,
*  but without consciousness you cannot do X.
*  And then someone say, oh, here is a model
*  that have no consciousness and do X.
*  Oh, so you do X, but you cannot do Y.
*  And then a model comes out, but look, I can also do Y.
*  And then you will also say, oh, but you cannot do Z.
*  Because you never give yourself a point, say,
*  if you can do X, I'm done.
*  Because you really believe in consciousness,
*  and there is no way to convince you
*  that consciousness is an epiphenomena.
*  Whenever your bar is set up, you say,
*  okay, so let's raise the bar.
*  If you do it, this is not interesting,
*  but this is interesting, and this is interesting.
*  And if you go into this argument,
*  then there is no way for you to win.
*  And I think it's going to be the same with AI.
*  People will say, okay, AI can do this,
*  so this is like a simple,
*  but the brain can do X.
*  And then AI start to achieve to this level of,
*  oh, but humans can do above it.
*  And you're always going to higher the bar,
*  and you will never say,
*  even when it's a complete robot,
*  you cannot even tell that they're robots,
*  because they are walking among us,
*  we'll say, oh, but we are specialist humans.
*  I don't think there's a way to win this argument.
*  And this is what I'm saying, for me, the scientist,
*  remove the word intelligent.
*  Simply remove it and say, behavior.
*  Can this model behave as humans?
*  And that's like the Turing test.
*  If it's behave like, it's good enough for me.
*  I don't want you to have an higher bar of winning.
*  If it's behave like, it might be cognitive.
*  You don't think we should do a test
*  to see if they have a spirit that will ascend to heaven
*  after we unplug them?
*  Okay, I won't put you on the spot there.
*  Okay, so.
*  If you can measure it.
*  Of course, I can.
*  So I'm developing the test as we speak.
*  So the latest approach here,
*  so we have these big models,
*  we don't understand how the individual units
*  are interacting to give rise,
*  and they're great predictive models,
*  not good explanatory models.
*  And there's been this push,
*  and there's a recent review on this,
*  and there've been multiple other papers that have come out
*  that have suggested the same thing,
*  that instead of concentrating on the units
*  and what they're doing, what we need to start doing
*  to sort of start understanding things
*  in an explanatory way,
*  is focusing on the three components
*  that we actually design in these networks.
*  And the three components would be the network architecture.
*  I mean, you've already mentioned all three of these.
*  The network architecture, the learning rules,
*  like back propagation, for instance,
*  and the objective functions, like what's the goal?
*  To maximize reward, to minimize entropy, and so on.
*  Do you think that we will come to feel satisfied
*  understanding these over understanding
*  the actual operations being performed?
*  Are we gonna sleep well at night thinking,
*  ah, I understand the objective function,
*  so therefore I feel better about understanding
*  how the model works?
*  I think so, I really think so.
*  I think so, you know, the physicist,
*  so Richard Feynman was saying,
*  I cannot understand what I cannot create.
*  And in a way, we build these machines, right?
*  And we understand everything,
*  we understand the computations, right?
*  We understand it's a very simple summation
*  with non-linear operations,
*  and then you multiply the matrices,
*  and then you run your arrow back and back propagation
*  and change your way to get your objective function.
*  We understand the circuits.
*  When some of these, like they mentioned,
*  they are not black box,
*  they are really not black box in a way,
*  the way to think about them
*  is the most transparent box you can ever imagine.
*  Because you build it,
*  and you have access to each synapse and neuron to all time.
*  To all these billions synapses and millions of neurons,
*  over time you know exactly what is the operation
*  and what exactly going in the network.
*  So they are very transparent.
*  And now that we have these transparent models,
*  in a way, this is, you know,
*  if you ask me what is my dream as a neuroscientist,
*  we have like transparent box
*  that I can look on each of your neuron
*  and each of your synapses over time from birth to death,
*  including all the input and output that you perform,
*  and I have your entire brain, right?
*  So that basically, this transparent box
*  is what we're inspiring in neuroscience.
*  And now that we have this transparent box,
*  it's an interesting exercise to say,
*  so how do we understand them?
*  What, now what? Yeah.
*  So now what?
*  And when you start to think on these three components,
*  suddenly you see, oh, actually,
*  I have an understanding of these models.
*  And so let's take the face network
*  that we started in China, right?
*  These networks have a minus of parameters, right?
*  So, sorry, so this is just,
*  this is the deep learning networks
*  that are designed to recognize individual faces.
*  Yes.
*  And is that, I don't even really know
*  how ubiquitous it is in China.
*  Is it just everywhere or, you know,
*  is it, do you get into the supermarket
*  and by your facial recognition and?
*  Yeah, it's everywhere,
*  and there is like an amazing podcast
*  that came last week,
*  basically from the New York Times, from the Daily.
*  There is a guy basically that really,
*  with little resources,
*  built the same thing in the US,
*  and now he's selling it to the police.
*  Yeah.
*  When they're running their models,
*  they can recognize all of us.
*  No.
*  We really help them to solve crimes,
*  and this guy doesn't even tell them
*  how he's doing it.
*  It's very fishy.
*  It's going to come to the,
*  it's already in the US,
*  and it's part of our life,
*  and it's going,
*  there is also an ethical discussion to talk about,
*  the loss of privacy and how this like,
*  Yeah.
*  When they start walking,
*  that will be like a separate podcast, right?
*  But it's really interesting to think about it,
*  but this model of faces,
*  basically, you can say,
*  oh, you duplicated the problem.
*  You have a brain that you don't understand
*  how it process faces,
*  and now we have another Google brain
*  that recognize as good as us,
*  and we don't understand it.
*  Right.
*  But it's not correct.
*  Because this is a transparent box,
*  you can really look into these models now,
*  and look what's going on.
*  And at the end of the day,
*  this model is a very simple model.
*  It's take the pixel input
*  that you understand completely,
*  because you know,
*  you can translate all the pixels
*  to the values of intensity,
*  and feed them to the neurons,
*  so you understand the input,
*  and you understand when you want to end, right?
*  Giving the names.
*  But one layer before it,
*  it's only 128 neurons,
*  and each face in the world get a vector of 128 numbers.
*  So now basically,
*  this model compressed all faces
*  into 128 dimensions space,
*  that each face get his number
*  in this I dimensional space.
*  So suddenly, it's also very simple
*  to understand the face space,
*  because now you can look on this like 128 dimensions,
*  and understand how faces are represented in the world.
*  And remember, because of the direct fit,
*  if 128 dimension is what comprise your faces,
*  and the model is over fit,
*  it's going to find the solution, right?
*  Because you're going to get the structures of the input.
*  So in a way, now these models are very simple,
*  and if you start to think about it that way,
*  you understand that recording all this
*  like a nonlinear transformation
*  from the pixel to the face space,
*  by putting electrode,
*  you will never get the code
*  of how the brain is processing stuff.
*  It's sending you in the wrong way of thinking.
*  And so in a way, these models are more simple
*  than we ever imagined the solution is.
*  Going back to say that fitting in other parts,
*  it's a very simple solution.
*  Yeah, yeah.
*  All right, so I'm aware sort of over time here,
*  so I want to,
*  there are a lot of implications for this,
*  and we've already been talking about some,
*  so maybe we can just go down the list a little bit here,
*  and then I want to ask you some sort of broad
*  general questions if that's okay before we wrap up.
*  I mean, so we are a symbolic species,
*  we use language, for instance,
*  we write down math equations,
*  we produced Newton, we produced Newton.
*  And you've already said that some of your students
*  think it's 95% of what we do is this direct fitting,
*  and then it's a very high percentage,
*  but is there room for interpolation
*  and extrapolation in brain processing?
*  Or, well, we'll start there.
*  Yes, there is a room,
*  and it's something that is currently missing in the models,
*  and I think we need to add it to the model.
*  I don't think you can learn calculus from examples.
*  You don't do like four by four is nine, 10, 11, eight.
*  Oh, eight, right?
*  Correct the fit and then go four multiplied by five.
*  That's not an efficient way to learn calculus.
*  So there is something about humans' capacity
*  to use rules and understand rules,
*  and some people call it like system two.
*  Yeah.
*  This is like a slow and deliberate way of thinking
*  is really missing in this model.
*  Do you think that the secret there
*  has something to do with recurrence?
*  And I'm asking because of your work on recurrence
*  and in timescales and hierarchical brain processing.
*  It has to be more than recurrent
*  because recurrent is already implemented
*  in this neural network,
*  so it's not that this neural network
*  is currently the artificial one, lack recurrent.
*  But they're not being asked necessarily
*  to perform functions that might require symbolic.
*  I mean, I say that,
*  and then probably 12 papers were published today
*  on that very topic.
*  Yeah, actually, there are interesting models
*  now that try to learn calculus using this neural network.
*  Oh, yeah, I saw that.
*  So basically, there are models,
*  and if you look at these models,
*  it's not that they are failing,
*  but there is a lot of small engineering tricks
*  that are built into the solution.
*  And then these models can really learn summation
*  and subtraction,
*  but it won't be good in multiplication.
*  So these small tricks,
*  and you refine these networks more and more,
*  and then they start to do something
*  that is start to be similar to humans.
*  But also you have to remember that also for us
*  to learn calculus, it's not an easy achievement.
*  You don't say that this is the,
*  for the brain it's so easy to learn calculus
*  and these models are so stupid.
*  It's also very difficult for biological neural networks.
*  I'll never admit to that.
*  Yeah.
*  Yeah.
*  Okay.
*  Okay.
*  I don't want.
*  So over here, I think we're really pushing the envelope,
*  and it's interesting to see how much
*  you can push the envelope.
*  Take language, for example.
*  I think the most exciting places now in machine learning
*  is actually NLP,
*  NLP, natural language processing,
*  and they're coming with language models
*  that get better and better.
*  And for example, they can learn syntax, for example.
*  They don't need any prior universal language
*  or knowledge about the syntax to learn syntax.
*  They learn to speak.
*  Of course they don't think.
*  So if someone attacked them that they are fake thinking,
*  by definition they are fake thinking.
*  They have no consciousness.
*  They don't try even to think.
*  They're not like, what is it, a tree,
*  a diagramming sentences?
*  What is that called?
*  Yeah, they don't have syntactical trees.
*  Trees, yeah.
*  Yeah, it's working in a completely different way.
*  It's all statistical learning
*  and the way they're echoing the outside, right?
*  So if they listen a lot to Fox News,
*  they will start to give arguments like Fox News.
*  They don't understand what Fox News is.
*  And now you start to ask,
*  how many of us really echoing the outside
*  and how much we are thinking, right?
*  So suddenly this is where my students
*  start to get really confused and say,
*  maybe we also echoing a lot and don't think much.
*  And I still arguing with my students,
*  listen, we're still thinking, okay?
*  So we are definitely different,
*  but they will say, you know,
*  maybe scientists are really good in thinking.
*  It's a dead center, but most of the people
*  and most of us, most of the time, we simply say stuff.
*  Most Fox News watchers, you mean?
*  Yeah, because no, if you listen to the New York Times,
*  you can echo the New York Times.
*  You don't need to echo.
*  It doesn't mean that the people
*  that listen to the New York Times don't do the echoing.
*  So it's a strange era.
*  And if you look on this language model
*  and I recommend the viewers to go
*  and talk with transformers,
*  this is like a GPT-2 model, language model,
*  and simply talk with it.
*  And see how good it's doing.
*  Of course, it's going also to say non-change
*  because it's fake thinking.
*  So don't expect it to be human.
*  But it should not do as good given what it learned to do.
*  And because it learned to do something very simple
*  and simply fit to a big data.
*  It's not a smart model.
*  Mindless.
*  So we've been talking on the show recently
*  about representation.
*  And you mentioned the phrase, weekly representational
*  when talking about models of this type.
*  How does representation fit in
*  and what does it mean to be weekly representational?
*  Yeah, so you know,
*  one end you can say that they're completely
*  non-representational because they simply take input
*  and toy to an output.
*  So, you know, they are basically
*  do like dynamical transformations.
*  But because the world have some regularities,
*  if you look within the smallest in the top layer,
*  that for them we talk about the embedding space for faces,
*  you get like a vector of 128 numbers.
*  Or if you look on the language model,
*  you have like a word embeddings
*  that you start to give like vector of numbers to each word
*  and you learn the relationship between words.
*  So you can think about like embedding
*  as a form of representation.
*  It's the vector that you can do operation and get outcomes.
*  These vectors are really fit to the structure of the world.
*  So they are not representational in the old sense
*  that we were thinking about it.
*  Computational representation.
*  They are not like strong computational entities
*  that on top of it you do the operations.
*  But so this is why they are weekly representational
*  and they are dynamicals and the context dependent.
*  So, you know, in the new language model,
*  the same world can get a different embedding context
*  relative to the previous.
*  Depending on its context and.
*  And the context.
*  So they become really contextual and dynamical.
*  They have a lot of interesting properties
*  that we didn't think about before.
*  And this is another example
*  that once you adopt this family of models,
*  as the models that you should work with
*  to understand the brain,
*  it really changing the concept
*  and the way we need to think about our brains as a machine.
*  So I think it's really,
*  this is a good example of how it go both ways.
*  You know, biological neural networks
*  can affect artificial neural networks
*  and artificial neural networks
*  can affect the way we study the brain.
*  I mean, that's, you know, when I say the same word to you twice,
*  it's not gonna have the same activity in your brain either time.
*  So that's like an embedding vector essentially.
*  Exactly.
*  And we have exactly this experiment now
*  that we took a language model, contextual embedding model,
*  and we opened the box and we look on the embedding.
*  And then we looked inside our human brain box.
*  And we saw that this embedding explained
*  neural activity better than other models.
*  So it's really, it's an exciting moment.
*  You can really learn a lot from this model.
*  What about minds?
*  Do direct fit models apply to minds or just brains?
*  That's an excellent question.
*  And again, we need to define what our minds on top of brains.
*  So it's not an easy question in a way.
*  If you care about the behavior and they behave like humans,
*  then they have the minds, right?
*  But if, I don't know.
*  That's a perfectly fine answer.
*  That's actually almost always the correct answer
*  to any question really in my experience.
*  I really, it's a complicated thing
*  because on the one end they behave like they have mind
*  and the other end we know that they have only neurons
*  and computations.
*  And, but it also, if you think about humans,
*  we behave as if we have minds,
*  but we only have neurons that fire, right?
*  So this is why it's a complicated philosophical questions
*  to say, I behave like I have a mind
*  and you believe that I have a mind, right?
*  But you never see my mind.
*  You only see what I'm doing.
*  And if you will open my brain,
*  you won't see my mind, you will see my neurons, right?
*  It's a crushing realization.
*  It really is, yeah, it's crushing.
*  It's causing, it's daunting.
*  Yeah, I don't, I don't know.
*  Consciousness is still a mystery to me.
*  I mean, I definitely, I'm conscious
*  and I know what I'm seeing and I'm thinking
*  and I don't understand it.
*  Yeah.
*  What, so you mentioned,
*  and I have immediately started thinking,
*  oh God, all these decades of work on these models
*  that the brain is operating under,
*  Bayesian brain, things like that.
*  What are some, or can you name one or two sort of grand theories,
*  something like Bayesian brain that doesn't fit,
*  what that we're gonna have to reconceive of
*  under this direct fit regime
*  or maybe one that it actually does accord well with.
*  Okay, so let's go with the optimistic.
*  Okay.
*  So, okay, so, you know,
*  when Skinner came with reinforcement learning theory,
*  we were like really, people basically,
*  especially after Chomsky, basically,
*  in the cognitive revolution,
*  we dismissed these reinforcement learning models.
*  In Skinner time, it didn't develop
*  modern reinforcement learning theory, right?
*  We didn't know about a lot of the components
*  that we know today about reinforcement learning.
*  But reinforcement learning and deeper reinforcement learning
*  have a very strong connections, right?
*  And this is an example,
*  our simple optimization of objective function
*  and reward you for predicting right
*  and enacting right and find the right policies to work
*  come back as models now.
*  So, you know, models that we were saying,
*  okay, Bayview is thick notion of the mind
*  is meaningless, right?
*  We let's look for the cognitive process.
*  Finally, they are coming back
*  and they seem really powerful models.
*  So you see how this model is meant to drive
*  or to play go or play computer games
*  and, or, you know, coordinate between the eye and the end
*  and act all these things are based on reinforcement learning
*  that again came from neuroscience
*  and then was also further developed in computer science.
*  So, you know, computer science
*  also influenced the neuroscience.
*  That's one of the best examples
*  of the interaction between, I think, AI and neuroscience.
*  It's a beautiful story that emerging
*  and it seems even more powerful for people
*  that did classical reinforcement learning, you know,
*  suddenly you take this idea of reinforcement learning
*  and put it in like these deep networks
*  and you call it deep reinforcement learning,
*  but, you know, but it's simply scaling up
*  these operations to large input.
*  And again, there's interesting statistical tricks
*  and objective function that people implement.
*  There's all these like engineering things
*  that we need to talk about the details,
*  but we're not going to do it here.
*  They don't make a difference.
*  And suddenly, oh,
*  behaviorism is coming back
*  and ideas that we forget and dismissed in the past
*  suddenly take the front
*  and it's an interesting moment in time.
*  So that's like an optimistic.
*  I don't think we're going back to behaviorism writ large, but.
*  Well, yes and no.
*  I think the problem with all of behaviorism
*  was that they didn't take behavior seriously.
*  So, you know, they try to,
*  to have, they've used them on a very small scale
*  of like a toy model.
*  Did the rat press the lever or not or something?
*  Exactly, yes.
*  So you know, like you have operant conditions
*  or classical conditions,
*  it's a very laboratory set of conditions.
*  Now, if you think about behavior, for example,
*  how people talk or recognize faces or drive.
*  So if you think again on real behavior and you take,
*  because remember this model is to behave, right?
*  That the prime thing is to do stuff, they are behaving.
*  And now you have a model that can explain their behavior
*  with just like a simple operations and three components
*  and scaling it up to big data and big models.
*  Maybe we do go back to behaviorism, but you know,
*  but the modern phase of it
*  that you really take behavior seriously and say,
*  you know, behavior is context dependent.
*  Language is such an amazing behavior,
*  but if you change one word in the story,
*  it's going to change the entire story.
*  So that's basically, that's the level of behavior
*  that you need to take into account.
*  And this is what is doing, so.
*  Well, so robotics, I mean,
*  do you think that robotics is gonna be a necessary step
*  in that direction?
*  Because right now these deep networks that we have,
*  their quote unquote behavior, many of them,
*  is categorizing, is it a tree, right?
*  And so that's not very rich behavior,
*  but once you get an embodied system,
*  actually behaving and contending with other things
*  in the environment, is that an important step,
*  do you think?
*  It's a necessary step.
*  In a way, this model, this is again,
*  where psychology and neuroscience can really help
*  these companies to think.
*  Once you give it a body and a sensory system
*  and it start to act,
*  you have a new set of objective function to learn
*  and also a new set of constraints
*  that are going to constrain the model
*  and give it like feedback and prediction.
*  And then it will learn way more rich set of behaviors.
*  It will be able to do more
*  and to learn on a faster time scale
*  because you're going to have more meaningful input
*  to the model.
*  A language model today, it simply read the entire internet
*  and try to predict the world from the context, right?
*  But you know, when I'm telling you,
*  do you want a cup of water, right?
*  There is this like cup, there is the table,
*  there is the flowing water from the tap.
*  There is so much constraint on the sentence
*  that these language models never see.
*  So of course they will never understand
*  the meaning of things because they don't act.
*  And therefore making them more biological
*  and give them this like body and interaction,
*  it's a necessary way to make them smarter.
*  Lily, this has been super fun for me.
*  A large part of my audience actually really likes to hear
*  about people's experiences
*  and how they got to where they are and things.
*  So I'm not going to ask you to recapitulate that,
*  but in the final few minutes here,
*  I want to ask you a couple of questions.
*  For instance, you know, what is something
*  that you would tell your younger self
*  if you were just starting out in academia?
*  Quit, you'd say, quit it all,
*  you're not a thinking being, just...
*  No, no, I hate that.
*  So I will say follow your gut.
*  And so the way it all started for me
*  and I think also why it's slightly easier for me
*  to adopt these models than other scientists.
*  I was a vision scientist,
*  actually I tried to understand face recognition
*  and we did all these control experiments
*  to understand the neural code by which we process faces.
*  And each talk we started the entire field, not me,
*  the entire field for, I will say like,
*  I was in this field for 10 years
*  and I think people were being like 40 years before me,
*  so the entire field for many years.
*  We can recognize faces like this.
*  There is no computer that can recognize faces,
*  humans are special.
*  And I got tired of control experiment
*  because I say, I want to know how the brain operate,
*  not in the lab, when you see stimuli
*  that you will never encounter in the real world,
*  how we really perform in real life.
*  So I moved my entire line of research
*  to naturalistic stimuli.
*  And we started to ask how the brain is acting
*  in the real world.
*  That's gutsy, that's a gutsy move.
*  Yeah, it is, it wasn't easy.
*  We got like a massive attack.
*  At one point I was really thinking to quit science
*  because I could not publish the paper
*  and when I was a postdoc and then we overcome
*  and since then people let us work
*  and actually, what we didn't realize even
*  when we started that everything changed
*  in the real world.
*  So we were thinking that our job is to take
*  the current models from control experiment
*  and say which one are correct in real life.
*  We think that were our task.
*  And this is how we wrote our first paper
*  about naturalistic stimuli.
*  But the more we went into it, we realized
*  all our toy models are not working in the real world.
*  For example, working memory,
*  we could not even start to understand
*  what is the meaning of working memory
*  when you go to the real world.
*  And this is our time scale.
*  That can be, if you want, that can be another podcast.
*  So basically once we realized
*  that the model is not working,
*  we realized there is a panel of field
*  we over fit to our toy model.
*  We never go to the real world.
*  All the scientific, I won't say all,
*  I will say 80% of the talks
*  that I'm listening to in neuroscience
*  and psychology start with amazing question about real world.
*  The next slide, it go to a toy model
*  that I don't know what is the connection to the question.
*  Then the entire talk is to explain the variant,
*  they explain like 20% of the variance
*  in the neural responses to this toy model.
*  And the end of the talk never go back to real life.
*  Or if it does, there's a big jump that it takes back to.
*  Yeah, but they never go back to real life.
*  The next talk we start again in a different toy model
*  or in variation of the toy model.
*  I think what we do is a field,
*  I think we over fit to our experimental design.
*  And when I saw this model, two things happened to me.
*  I said, wait, why I worked on,
*  I mean, the entire field, it's not me, I mean,
*  so many people, we worked on facial recognition
*  and suddenly this company has come with models
*  that do it as good, if not better than humans.
*  And we don't have any model that work in the real world.
*  I was upset by this.
*  Oh, bad.
*  But then also I say, wait, I also like it
*  because they work in the real life.
*  They never do experiments.
*  They simply give the brain what they need to solve,
*  give the network and learn how to do it.
*  So they live in the real world.
*  And this is why I'm like arguing for many years,
*  we should go and solve our models in real life
*  because the lab model do not generalize to the real world.
*  And this is why also I like this model.
*  So in a way, what I'm saying basically
*  to the young generation, follow your gut instinct.
*  If you really believe in something, go for it.
*  And another thing, learn the part
*  that you really want to learn.
*  Because we are so obsessed with gaming,
*  it's like pure solution.
*  We say we cannot study the brain in real life.
*  It's like too complicated.
*  Too many variables.
*  Yeah.
*  1,000 dimension, 10,000 dimension.
*  I don't know the number.
*  I cannot explain this non-linear interaction.
*  Let's study five dimensions
*  and then I can give the simple formula.
*  But if there's non-linear interaction,
*  you add five more dimensions with non-linear interaction.
*  Or what you learn in these five dimensions
*  will never generalize.
*  Needless to say, it will never generalize
*  to the 10,000 dimension.
*  So if you want to understand how the brain is working now,
*  as I speak to you and you listen to me,
*  and we have this interesting conversation,
*  this is what you need to study.
*  Stop thinking that you need to control for experiment for that.
*  That basically it's remove you further away
*  from what you want to understand.
*  And you will never be able to go back to the real world.
*  So I think...
*  Start in the real world is the...
*  Start in the real world.
*  We have like a new paper coming.
*  We call it Keep It Real.
*  And we're really arguing the primacy of neuroscience
*  should be in the real world.
*  Real world is not the way you test your theories also.
*  It's also the way, the place you develop your theories.
*  Isn't that, haven't the latest deep learning models
*  allowed that to happen?
*  I mean, this behavior, the complex naturalistic behavior,
*  there's all these rallying cries right now
*  to study the complexity of the real environment
*  and behaviors.
*  Is that because we've now have bigger data,
*  bigger computational power, bigger models?
*  Yes, exactly.
*  And this is why it's like an exciting moment.
*  I think it's really we are on the brink of revolution.
*  The underlying assumptions in the field
*  going to completely change.
*  There is a big wave of new models coming to the field.
*  There are still people that working with the old paradigm
*  and so they are unaware
*  or they say this work is out of my domain.
*  I should not care.
*  It's a lot to learn.
*  It's a lot to learn.
*  And it's a different way of thinking.
*  So it's not easy.
*  It's not easy to,
*  it's a lot to learn.
*  It's a lot also to forget.
*  Yeah, yeah.
*  So it's a big of requirement.
*  Maybe it's only for, maybe we are too old
*  and it's only the young generation
*  will manage to really completely harness it
*  to understanding.
*  But it's also an exciting moment because,
*  suddenly we have models that work
*  and models that can do stuff
*  that we didn't have it five years ago.
*  So I think it's really exciting moment to,
*  I don't know, to take all this and move forward.
*  Maybe we are tiny bit closer, tiny bit,
*  because there is still a way to go,
*  but to understand the brain.
*  Oh, I didn't even ask you.
*  How have people responded to the manuscript?
*  Do you get hate mail all the time or love mail?
*  Do you get marriage offers?
*  So you know, science is weird.
*  It's like a lonely endeavor
*  in the sense that you sent,
*  okay, so we worked on this paper for a while, you know,
*  because it was difficult to,
*  because it's a shift in paradigm
*  and you need to explain people this like shift.
*  It took us a lot of time to come with a simple word.
*  And you find out which examples to use
*  and things like that.
*  Which example to use exactly.
*  And I think it's still in every paper.
*  So there is something dense about this paper.
*  So it's taking a lot of effort to read it.
*  And sometimes it's look trivial
*  and sometimes it's look deep.
*  So I think it's a difficult paper to read.
*  And you release this like side of yours to the world.
*  And then there's like silent.
*  It's take time, you know,
*  people will give reference in like two years,
*  you will see some references in there.
*  Because the field is moving slow.
*  So I don't know.
*  I got like, you know, some people liked it.
*  I didn't get any hate mail.
*  I assume that people that don't like it
*  are less likely to contact us, right?
*  Because people don't like to confront.
*  I don't know.
*  But conflict is huge in academia too.
*  So if someone, maybe it's just that they haven't cracked
*  the nut on how to respond to it yet.
*  If they don't agree with it.
*  Yeah, so maybe it will take them time to formulate
*  the critic and it's take time
*  and someone else constantly like writing
*  and we'll start to see it.
*  It's still, I didn't see the critic emerge.
*  I expect that if people really understand us,
*  they should criticize us because it's really going
*  against the paradigm.
*  It really does, yeah.
*  And people should not like it.
*  I see people that really committed to the paradigm
*  should basically be furious now and attacked us.
*  I didn't see it happen.
*  Yeah, there's another possibility.
*  No one read anymore.
*  That's true.
*  It's gone.
*  It's too much.
*  The field of academia overparameterized too many papers.
*  Exactly.
*  And it's a dense paper.
*  It's difficult to understand.
*  Maybe we failed to explain it.
*  I don't think so.
*  I think it's so straightforward
*  and I mean, to me, it just really hit home.
*  So maybe that's what's happening.
*  Maybe you did such a fantastic job.
*  No, but then as you say,
*  there are people that should disagree
*  because it's going against the paradigm.
*  So I expect also to have some people
*  that have a strong opinions against it
*  that actually I respect them.
*  And I understand and also sympathize
*  because they also part of me
*  that feel uncomfortable with this person.
*  Yeah, it's terribly uncomfortable.
*  Yeah, and so I expect to see it.
*  Not yet.
*  Maybe it's on the way.
*  Keep me posted, Wendy.
*  Send the hate mail my way.
*  I'd love to see it.
*  So anyway, all right.
*  Well, Uri, maybe in a little bit,
*  we'll have to have you back on the show
*  and you can explain to us your latest paradigm shifting
*  realization.
*  But for now, this has been so fun.
*  And of course, I'll link to the paper in the show notes
*  because it really is a very different way
*  of looking at it.
*  So I appreciate you sharing it with everyone
*  here on the podcast.
*  Thank you so much.
*  It was really fun.
*  Really, really fun.
*  We've left all the hating
*  Searching the coffers
*  For empty offers
*  I don't know why
*  You trust the sky
*  You must like your lies from blue eyes
*  You must like your lies from blue eyes

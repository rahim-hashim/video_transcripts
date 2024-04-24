---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3986s
Video Keywords: []
Video Views: 4401
Video Rating: None
---

# BI 012 Niko Kriegeskorte: Black Box, White Box
**Brain Inspired:** [October 13, 2018](https://www.youtube.com/watch?v=QmeYcQt0Rug)
*  It's cognitive science plus computational neuroscience plus AI.
*  Let's say a big brawl breaks out.
*  Who's going to win it, the computational neuroscientist or the cognitive scientist?
*  Neither.
*  Each of them has half the truth or a third of the truth, I'd say.
*  This is Brain Inspired.
*  Hello and welcome.
*  This is Paul Littlebrooks.
*  This episode of Brain Inspired is brought to you by me.
*  My time, attention, tears, wallet, all that jazz.
*  You'll notice perhaps I don't use advertisements on the show, nor do I plan to, unless it's
*  for a good cause like hot air balloons perhaps or ridding the world of domesticated cats.
*  Other things that would make the world better.
*  I do love doing the show, but it does take a lot of effort.
*  You could most definitely help by telling a friend and or leaving a review on iTunes.
*  Today I talk with Nico Kriegskorte.
*  Kriegskorte.
*  Let me try one last time here.
*  It's a little nuanced.
*  Kriegskorte.
*  Okay.
*  I was a little less angry that time.
*  That's good.
*  Nico is a professor at Columbia University and for years has been at the forefront of
*  this intersection of neuroscience and AI.
*  So he's a poster child for the show, if you will.
*  Instead of focusing on any of his research findings today, we talk really quite broadly
*  about how deep neural networks can be harnessed to understand how our brains work.
*  Nico and his colleagues have coined the term cognitive computational neuroscience.
*  They run an annual conference by that name as well.
*  The goal is to join three fields into one.
*  Namely, cognitive science provides a high level top down approach exploring how information
*  processing in our brains leads to our behaviors.
*  Computational neuroscience on the other hand provides more of a bottom up approach, explores
*  more how that information process is carried out at the level of neurons and ensembles
*  and circuits of neurons.
*  And then finally in the middle you have artificial intelligence which acts as a bridge between
*  the two levels, exploring what algorithms might be carrying out these processes in the
*  brain.
*  Okay.
*  So Nico describes all of this stuff much more in depth in the episode.
*  This was fun.
*  We also talk about things like how many realistic details we eventually need to include in models
*  to satisfy our thirst for understanding brains.
*  And of course, plenty more.
*  Nico is on Twitter.
*  He is at KriegskortLab and he suggests that you learn more about him and what he does
*  by visiting the website for the cognitive computational neuroscience conference.
*  So that will be linked in the show notes as well as all the other things we mentioned.
*  So find those at braininspired.co.
*  Thank you for listening and please enjoy our conversation.
*  Nico Kriegskorte.
*  I know I'm butchering that, but welcome to the podcast and thanks for being here.
*  That's pretty good actually, Paul.
*  Give us the real one.
*  Kriegskorte.
*  Yes.
*  Okay.
*  I'm going to work on it.
*  So I will have introduced you and pronounced it perfectly in the introduction, but I'll
*  say a bit here.
*  So you're a professor of psychology at Columbia University and director of the Cognitive Imaging
*  Center and your principal investigator at Columbia's Zuckerman Institute.
*  So you're a busy guy.
*  You also write a blog of sorts called Open Brain Science.
*  And it's really what it is.
*  It's a thorough breakdown and review of recent research articles that you choose to cover.
*  Now a few episodes ago, I had Dan Yeamans on and we talked about his work modeling the
*  visual system with convolutional neural networks.
*  And you put out a paper that same year in 2014.
*  And these two papers, the one that he and I talked about and yours are the ones that
*  are always cited when people talk about the beginning of how CNNs were being used to model
*  our visual system.
*  And you've been beating the drum now for a few years that machine learning and in particular
*  deep learning provides a great opportunity for computational neuroscience.
*  So today we're going to talk broadly about that and issues surrounding it.
*  Luckily for me, you've written a bunch of great review articles about these subjects.
*  Now we're going to focus mostly on deep neural network models today.
*  But using one of your recent reviews in nature neuroscience called cognitive computational
*  neuroscience, I made I took a big sheet of my my children's drawing paper and made a
*  mind map for myself of all the types.
*  Oh, that's great.
*  I love mind maps.
*  Yeah, I don't often make them, but this one just cried out for it.
*  So so I made it.
*  It's it's actually still on my desk.
*  But it's basically all the types of models that are being used and how they relate to
*  theory and experiment things like cognitive models, connectivity models, decoding models
*  and so on.
*  I should send it to you.
*  I'll take a picture of and send it to you once I clean it up.
*  But so thanks.
*  That would be great.
*  Please do.
*  So, Nico, what is cognitive computational neuroscience?
*  It's cognitive science plus computational neuroscience plus A.I.
*  And it's it's not a field yet, but it's it's an idea, really.
*  And it's quite an old idea.
*  So it's been the idea that these fields study the same thing fundamentally has been
*  around very long. Even the fathers of modern computing Turing and von Neumann were
*  thinking about the brain and about the mind when they thought about how to design
*  computers. So so this idea is really very old.
*  But to actually pull it off and bring people who are thinking about the brain and the
*  mind at totally different levels together and to create a common language is has
*  always been a tall order.
*  So historically, these these separate fields have have crystallized and focused on
*  particular parts of the problem.
*  So, for example, cognitive science has cared about the information processing and has
*  tried to rigorously model the information processing with computational models without
*  being encumbered by at the same time having to explain how it's implemented in the
*  brain. And that's kind of a top down approach to understanding brain information
*  processing, where you're not really talking about the parts of the brain, the components
*  in the brain, but you're talking about the information processing.
*  And then computational neuroscience has taken a kind of bottom up approach where you
*  look at the brain, you look at the neurons, you measure the neurons, you try to understand
*  the dynamics in the neurons.
*  But from the perspective of function, like how might this be useful for information
*  processing? So you're describing how neurons and small sets of interacting neurons
*  can implement components that might be useful for a cognitive system.
*  But between this top down approach and the bottom up approach, so far they haven't
*  really become integrated.
*  They haven't met in the middle.
*  And that's the idea of cognitive computational neuroscience.
*  It seems kind of crazy, doesn't it, that they haven't really I mean, that your idea
*  is that these fields are kind of pointing to each other and need to be integrated using
*  AI techniques.
*  Why do they need each other?
*  Why do these three subfields need each other?
*  So computational neuroscience needs cognition for direction because you can't really
*  figure out what the function is or what these little ensembles of interacting neurons
*  are supposed to do if you don't look at how they come together to a more complex
*  function that contributes to successful behavior.
*  So that's why computational neuroscience needs cognitive science.
*  And cognitive science needs computational neuroscience because cognition is grounded
*  in the brain and it's implemented in the brain.
*  And you lack constraints when you just think about information processing in the in
*  the abstract.
*  There is not enough empirical constraint to find out even I would argue, and many
*  cognitive scientists might disagree with me on that, even to understand cognition.
*  Do you get pushback?
*  Do you get much pushback from colleagues, especially on the neuroscience side, for
*  bringing in deep learning as a big part of this and using AI to sort of bridge these
*  two computational neuroscience and from the bottom up and cognitive science from the
*  top down?
*  Yeah, I mean, these are totally different levels of description.
*  And you have to as a scientist, you have to focus on something.
*  You have to focus on a on a particular set of observations or on a particular set of
*  methods or on a level of description at which to model what the brain does.
*  And then you kind of fall in love with that particular level.
*  And the result of that is that that's what fires up your imagination.
*  And when you watch it and the same is true for me, of course, I'm here in a neuroscience
*  institute where I go to talks where I don't know all of the terminology and it's a
*  totally different way of thinking about it.
*  It addresses questions maybe at a much finer scale than what my work is about.
*  So it's difficult for us to get excited about these totally different levels of
*  thinking about what is the same big picture problem, understanding how the brain works.
*  Right. And that's why it's so hard to bring these communities together.
*  In the abstract, it's easy to say, well, of course, we're all at some level working on
*  the same question. So we we should be working together.
*  But then to actually make it happen is a much harder task.
*  But I think there is a new dynamic now.
*  Well, so as science pushes on, we become more and more specialized in general.
*  But this is kind of an argument that we need to become more broadly minded or at least
*  collaborate and reach over the aisle and collaborate more.
*  Do I have that right? I think that's that's generally true.
*  Yeah. So we need to come together.
*  That's what we need the conference for.
*  We need to understand each other's language.
*  We need to understand importantly why it is essential for what we care about to
*  understand the other fields.
*  Well, yeah. So let's talk about the conference.
*  So you just had your second annual Cognitive Computational Neuroscience Conference.
*  Now, so you're bringing together people from these somewhat disparate specialized
*  fields in the same conference.
*  And I mean, it's somewhat difficult to discuss brains and neural networks together,
*  I find. So so neurons and units, those words are really interchangeable in both
*  fields. So you can talk about in artificial networks, you can call them neurons or
*  units and in brains, you can call them neurons and use.
*  I mean, my preference is to call artificial units units and brain cells neurons.
*  Oh, yeah. You know, because I don't I don't want to have to say, oh, you do.
*  OK, I don't want to have to say biological neurons each time.
*  Yeah, yeah. But it's true.
*  It's really I've never thought about it.
*  But neuroscientists also call biological neurons units sometimes in
*  electrophysiology, for example.
*  And that's really confusing.
*  So let's agree to call the artificial ones units and the biological ones neurons.
*  And that brings up the first sort of big disconnect, I would say, you know, that
*  neural network models are called neural networks when, of course, there's no
*  neurons in them. And any neuroscientist who cares about ion channels and
*  multi compartment dynamics and structures of dendritic trees and maybe
*  computation and dendritic trees is rightly offended by the term neural network
*  when a unit in a neural network is computes a linear combination and passes
*  through a static non-linearity.
*  That's very, very understandable.
*  And it was, you know, in a way, a misnomer.
*  It was when people first used it.
*  I actually don't know the history at all, but, you know, I imagine it was just a kind
*  of naivete. Right.
*  And so it's it's kind of almost ironic that it's being vindicated as.
*  A key element for bringing these fields together, a very powerful, common
*  modeling language that connects the three fields, cognitive science and
*  computational neuroscience and AI.
*  Do you think we're stuck with the terminology?
*  I think we're stuck with the terminology.
*  Yes. Yeah. So so this conference that you put on, I don't know if the videos for
*  the talks are available on this year are available online.
*  Everything will be available.
*  Yeah, it's being edited.
*  OK. Yeah, that's a lot of work.
*  I've enjoyed multiple videos from last year's conference, so I'll link at least
*  to that to give people a feel for it.
*  So so what are some of the challenges like linguistically, semantically,
*  conceptually, culturally, even for bringing folks like this in these different
*  fields together? So cognitive scientists look at behavior.
*  They look at the overall function and then they try to come up with algorithms
*  that might provide these functions.
*  And then they implement those algorithms, usually using computer science techniques
*  and sort of symbolic level algorithms that are very difficult to map onto the brain,
*  either conceptually or sort of piece by piece in terms of their components.
*  And then they predict behavior and they do behavioral experiments and they
*  compare the behavior of their algorithms to the behavior of humans.
*  And so they have a totally different language that doesn't necessarily
*  relate to the brain in every every single case.
*  So that's that's one problem.
*  And in the other direction, similarly, neuroscientists
*  are looking at the biology and they're looking at lots of biological phenomena,
*  some of them dynamic, those are probably ones closer to functions such as
*  spiking and dynamics within neurons
*  and ion channels and all of that.
*  And perhaps they go a step further and they take all that knowledge and they assemble
*  it into simulations where you have a set of neurons interacting and you have
*  network phenomena there.
*  And maybe these these simulations produce oscillations or something like that.
*  But it's very far from the information processing function of the brain.
*  Right. Yeah.
*  You know, let's say a big brawl breaks out.
*  Who's going to win it?
*  The computational neuroscientists or the cognitive scientists?
*  Neither. They each of them has half the truth or a third of the truth.
*  Any big brawls break out at the conference?
*  Not really, probably because it's a self-selected group, right?
*  The people who come to this conference, they're already quite open minded
*  and they're interested in learning about the other disciplines.
*  So, like I said, it's only two years old now.
*  So when did you have the idea for it?
*  How long was it in the making?
*  So I didn't have the idea.
*  The idea was from Kendrick Kay and Thomas Nassalaris.
*  And these are very good computational neuroscientists and friends of mine.
*  And they approached me about it.
*  I want to say it was in Hawaii at a conference, but I could be wrong about that.
*  I kind of have a recollection of a restaurant setting where we were having dinner
*  and they pitched this idea to me.
*  And my response was, do we really need another conference?
*  Yeah. Well, are you glad you have it?
*  Are you looking forward to next year?
*  Yes, I am. So, I mean, it took, you know, a few minutes, I guess.
*  So first, when they mentioned it, I thought of all the work it would be to organize it.
*  And we already have too many conferences.
*  Yes.
*  I want to focus on my science and my lab.
*  But then they made a good case that actually there is no conference
*  really bringing these three fields together.
*  And, you know, it resonated with me because I've been going to other conferences
*  that are great and that I love and that I'll always be going to,
*  including COSINE, the Computational Systems Neuroscience Conference,
*  and VSS, the Vision Sciences Conference,
*  and OHBM, the Human Brain Mapping Conference,
*  and the Society for Neuroscience Conference.
*  So, and NIPS, of course, the Neuro Information Processing Systems,
*  which is more on the engineering side.
*  So all these conferences are great,
*  but none of them really brings these three communities together
*  in quite the way that Kendrick and Thomas were envisioning.
*  So, you know, after about five minutes, I was convinced and totally honored.
*  Good. Well, I'm glad you're doing it.
*  And I'm really thankful you guys post the videos on YouTube
*  because it's a great resource.
*  All right. So let's talk about how deep neural network models
*  can help us understand the brain, because this is the
*  AI, the neural networks are in the middle between the top-down cognitive science
*  and the approach and the bottom-up computational neuroscience approach.
*  So you wrote this great review a few years ago,
*  right when machine learning models were starting to catch on
*  and resemble what's happening in our brains.
*  And near the beginning of the review, you provide this table.
*  And in the table, you illustrate the history of trying to understand
*  how the brain works.
*  So in rows, you list the elements required for understanding
*  how brains work, things like, is it neurally plausible?
*  Does it provide neural data, et cetera?
*  And then each column is a different historical field of study,
*  things like cognitive psychology, computational neuroscience, and so on.
*  And if a given field of study satisfies a given element required
*  for understanding brains, you just simply put a checkmark in that box.
*  So, for example, cognitive neuroscience gets a checkmark
*  for explaining real-world tasks that require complex computations.
*  And it gets other checkmarks.
*  But what jumps out immediately when one looks at the table,
*  you notice, oh, poor, poor behaviorism.
*  The only checkmark it gets is for collecting behavioral data.
*  So this refers to, of course, how behaviorism treated our brains
*  like black boxes.
*  And so it only examines what goes into the black box,
*  things that we sense, and what comes out of the black box,
*  namely, our behaviors.
*  Anyway, it just amused me, that table.
*  I don't know if anyone else has commented to you about that.
*  Not really, no. You're the first.
*  I'm remembering it now.
*  I didn't even remember I put behaviorism in there,
*  but I guess you must be right.
*  Yeah, it just gets dragged through the mud so much these days.
*  It's funny.
*  I mean, no one talks about the cognitive revolution anymore, right?
*  When people started arguing that we have to theorize
*  about what goes on inside the brain, about the information processing, right?
*  And then cognitive psychology started doing that.
*  And in a somewhat vague way with these box and arrow models
*  where they were talking about the decomposition of the functions
*  that the brain computes into components.
*  And you could somewhat behaviorally study that.
*  But the models weren't fully explicit.
*  They weren't things that you could run on a computer
*  and really see what the interaction of all the proposed elements really entails
*  and whether it can explain task performance.
*  So that's, in my mind, what cognitive science contributed to the endeavor.
*  And that's really a key part to the whole story of understanding the brain.
*  You're right. That story, as we advance more and more,
*  seems to get told less and less.
*  But it is a key development.
*  OK, so you stress that if deep neural networks are going to be helpful
*  in understanding brains, that we need to use methods to compare the models,
*  the neural networks, and brains' internal representations
*  while performing a task successfully.
*  While the models are performing a task successfully.
*  So what are some of the ways that deep neural networks
*  can be tested with brain and behavioral data?
*  Yeah, maybe let's slightly backtrack why deep neural networks.
*  We talked about cognitive science before.
*  And cognitive science has symbolic models that are not deep neural networks.
*  And these are also important to me.
*  I mean, these are part of cognitive computational neuroscience,
*  and we need them as well.
*  So it's not only about deep neural networks.
*  But if you're interested in taking the step of bridging down to biology,
*  then deep neural networks are especially appealing.
*  And they've been around for very long.
*  They have a long history.
*  And they have a long history, actually, in each of these three fields, importantly.
*  So in cognitive science, deep neural networks brought a paradigm shift.
*  In the 80s called parallel distributed processing.
*  And a lot of the very important papers on how deep neural networks compute
*  actually came out of cognitive science and came out in cognitive science journals.
*  So there's a long history there.
*  And then in computational neuroscience, there is a long history also of neural
*  network models at various levels of biological detail,
*  including spiking neural networks or more abstracted neural networks.
*  There's a lot of theoretical work on recurrent neural networks and the emergent
*  dynamics from kind of a physics perspective.
*  And so they've always been key there in computational neuroscience to
*  understanding the dynamics in biological systems.
*  And then in AI, they for a long time didn't really deliver on their promise,
*  so they couldn't really they weren't really state of the art solutions,
*  for example, to computer vision and to other engineering problems.
*  And I remember as a student in computer science, our professor talked about neural
*  networks, so that was taught.
*  But, you know, in a very sort of negative way, you know, you could tell that he
*  thought that that was not a rigorous engineering solution because there was not
*  very good theory for understanding what goes on in these complex systems.
*  And there are other models such as support vector machines for which we had
*  better mathematical theory for understanding what goes on.
*  And they were simpler.
*  And actually, they worked just as well at the time, maybe even even better in
*  certain contexts than neural networks.
*  So at the time, neural networks, when I was an undergraduate, were not considered
*  state of the art engineering solutions.
*  But that all changed in 2012 with AlexNet when AlexNet won the ImageNet
*  competition by a large margin, the whole field of computer vision sort of realized
*  this is the way to go.
*  We have to automatically learn these internal representations rather than hand
*  engineer them. And there was no looking back.
*  And this has been extended to other domains of perception, but also to higher
*  cognitive challenges such as language processing, language translation and motor
*  control, robotic control.
*  So now deep learning is really a very successful component of machine learning
*  and AI.
*  And that's really very exciting because it means that a modeling framework that is
*  neurobiologically plausible in the sense that it's very easy to imagine implementing
*  all the computations that deep neural networks use with biological neurons.
*  So they only use a small subset of what you could call the dynamic repertoire of
*  biological brains.
*  But the functions that they do use definitely are very plausible.
*  And within this framework, now you can do cutting edge AI, which you need to be if
*  you want to explain how the brain works.
*  The brain is intelligent.
*  You need to make models that can perform intelligent tasks that are intelligent
*  themselves. So that's a key requirement.
*  And then the links to cognitive science and to computational neuroscience are the
*  historical links. And so the common literature there is these are further factors
*  that place this modeling framework really at the at the center of cognitive
*  computational neuroscience.
*  Yeah, I guess the so the same thing that behaviorism gets knocked for.
*  Neural nets have kind of historically gotten knocked for and that there have been black
*  boxes. But that's starting to change because so you have these deep neural networks that
*  can perform the cognitive tasks.
*  But what good are they if we can't understand how they're performing it and what's going
*  on inside the inside the network.
*  So in your review, you actually talk about multiple ways that we can study these things.
*  Exactly.
*  So black box is really entirely the wrong the wrong term.
*  I would call them white boxes.
*  I agree. I think I got that from Dan Yamins, actually.
*  So white box is a better term because they're entirely transparent.
*  You have access to everything.
*  Right. That said, what people mean when they say that is these systems are themselves
*  very complex. And just because you've got a neural net model with millions of
*  parameters that can perform your task and predict perhaps errors in behavior and
*  reaction times and brain activity.
*  That's what we want, of course.
*  Right. But they say even if you have that, you still don't understand your model.
*  So have you made theoretical progress?
*  And the answer to that is it's true that once we have that, we're not done.
*  We still want more abstract level of theoretical understanding.
*  We want theory in addition to models.
*  However, having models is a necessary component and is a big step in the direction of
*  getting the theory right as well.
*  Because if we don't have models that can perform the task, if we don't if our theories are
*  not instantiated in models that pass the first test of being able to perform the behavior,
*  then we're not explaining how cognition is implemented in the brain.
*  Right. So once we but let's assume so it depends how it goes.
*  It could go that you have the theory first, you implement the theory, you test the theory,
*  it works, and then you have theory and a model and the model helps you test the theory.
*  And then you're done for some restricted task.
*  Right. Of course, that doesn't mean you understand all aspects of how the brain works.
*  It means you understand brain information processing in some animal or some restricted
*  task environment. Right.
*  But it could also go the other way around.
*  And that's what the people talking about the black box problem, which is actually the white
*  box problem, are thinking of is that you play with these models, you really forget about
*  theory, which is what they care about.
*  And now you have this model with millions of parameters.
*  And let's say it does very well.
*  It can perform the task and it predicts errors that people make and it predicts reaction
*  times or motor dynamics or something like that.
*  And it generalizes to new if it's a visual task, new images or new environment.
*  So it's not just sort of overfitted to your particular sort of small toy version of the
*  task, but it really generalizes to the real world.
*  So that's great. But they say so.
*  But you still don't understand how this dynamic system with millions of parameters is doing
*  it. Right. And my answer to that is, yes, you're right.
*  Now there's the second job.
*  But now we're much closer because we've downloaded the mechanism into the simulation, which
*  is entirely transparent, which we can probe cheaply with millions of images.
*  We can study it much more easily with synthetic neurophysiology.
*  So we're in a much better position.
*  Also, if we go from from the model from the bottom up more from from the model with the
*  many parameters to the theory, we're also in a better position using these models.
*  I remember I mean, I'm just I'm burning up inside right now because thinking about the
*  white box, because when I started neurophysiology, I was recording neurons from monkey
*  frontal eye field while they performed little tasks with their eyes making saccades.
*  But when I started off, we were using single electrodes, you know, so I could maximally
*  get maybe two to three neurons at a time.
*  But, you know, the motto from my old adviser, Mark Summer, was one neuron a day.
*  You know, that's a good day.
*  So it's just so I eventually go ahead.
*  Takes 100 billion days.
*  Then, right. That's right.
*  Boy, and it sure did take that long.
*  But but anyway, so I think that this is a huge benefit to be able to, yeah, examine all
*  of the units.
*  Anything that you want is there for the taking.
*  So so I think that's great.
*  So what are what are some of the ways that we can understand what's going on inside these
*  networks and compare them to how brain and behavior are happening?
*  So we need to first bring cognition into the laboratory.
*  Right. It all starts with cognitive science in a sense.
*  Both historically with task performing models and also sort of in the the cycle of the work.
*  First, we need to think about what is the function that I want to explain.
*  And in order to bring that function, that piece of cognition, that piece of the mind
*  into the laboratory, we need to define a task.
*  And this task is usually going to be some kind of computer game.
*  So it's going to be something it's going to be an interaction where there are stimuli
*  and there are responses.
*  And we want to be able to record the responses and present the stimuli and close the loop
*  and present many different kinds of versions of this more general task and measure
*  behavior. Right. And that it doesn't matter whether we are studying animals or people.
*  This is a common element.
*  And once we've done that, we can start studying it.
*  And the natural starting point is the overall performance at the task.
*  Right. So we want we want to see how well can our subjects, for example, our human
*  subjects or our animal subjects perform the task under what conditions do they make errors?
*  What are their reaction times?
*  When are they slower?
*  Perhaps try to understand why certain versions, why certain stimuli, for example, are hard
*  to recognize. And this gives us clues as to the computational mechanism.
*  And then we can start modeling this.
*  So we want to build a computer model that can perform the task.
*  And that means that the model has to be able to interface with the software that presents
*  the task to humans or animals.
*  And it has to be able to perform the task.
*  And it should be able to perform the task at the same general level of performance as
*  the animal or the human subject.
*  So that is in a way the first test of a task performing model or what I also call a brain
*  computational model.
*  Yeah. So I should just say also that that's not the goal in, let's say, industry to make
*  models that will match the behavior.
*  The goal is always to be most efficient and outperform behavior.
*  But if you're trying to understand brains, you need it to match the actual human behavior
*  or animal. Absolutely.
*  And that's a that's a distinct goal.
*  And in some areas where the performance of current models is very far from human performance,
*  these two are very similar.
*  Right. Because if you want to explain human behavior, first you have to be in the ballpark
*  and be able to do the task at all.
*  Otherwise, you're just in the dark with understanding the particular way in which humans
*  solve the task.
*  Good. OK. So a lot of the neural network models that are being used, like to study the
*  visual system and model the visual system, are mostly feed forward models, meaning that
*  you put input in the model, it goes through all the units, all the layers and then spits
*  out an answer.
*  And of course, there's back propagation.
*  But there historically until recently, there haven't been many recurrent connections in
*  the models. I mean, there have been recurrent neural networks.
*  But so recently, these convolutional neural network models are beginning to incorporate
*  some recurrent connections in them as well.
*  So can you just talk a little bit about feed forward and recurrent computation in brains
*  and and in neural networks and what roles they might play?
*  Yeah, I'm happy to do that.
*  So the feed forward models have been very successful in vision and both in the neuroscience
*  of vision and in computer vision.
*  So the kinds of models that do vision, for example, in our cell phones and the technology
*  that we're using to communicate right now, those are likely feed forward convolutional
*  neural network models.
*  And in the neuroscience of vision, similarly, feed forward models have been very popular
*  and very successful.
*  And that's because the visual hierarchy is a deep hierarchy.
*  Vision is very rapid.
*  We can glean a lot of knowledge from a very brief glimpse at a scene.
*  And so that is a very fast process that doesn't allow for much recurrent computation, even
*  though the brain is recurrently connected at all levels and within layers as well as
*  between layers.
*  So we've always known that the connectivity structure is is recurrent, but it's it just
*  made a lot of sense to first focus on sort of the feed forward sweep through the system,
*  which already can explain some of the behavioral function of sort of basic recognition of the
*  things, the kind the kinds of stuff and the kinds of objects that are present in a visual
*  image. So that was that was good.
*  And, you know, I think there's there's real progress.
*  And with the advent of deep convolutional neural networks, there's been really a sudden
*  breakthrough in this game.
*  So the classical game of computational visual neuroscience was to predict the response of
*  a neuron to arbitrary natural images.
*  And so you'd have this little model of how what does the brain, the eye and the retina
*  and then then the brain do with the image in order to produce the response of the
*  neuron and maybe for primary visual cortex, you know, you abstract from the biological
*  details, for example, the retinal processing.
*  To some extent, you come up with a simplified sort of slightly higher level model like a
*  Gabor filter model.
*  And this allows you to predict responses in V1 to arbitrary images to some extent.
*  And maybe you can explain 50 percent of the variance.
*  So that was so one very big early success story of computational visual neuroscience.
*  But then when you try to take that to V2 and V4 and IT, it gets progressively harder.
*  And in V4, it's already extremely hard to come up with these models and fit these models
*  with the limited kind of neural response data that we can realistically acquire.
*  And in IT, it was always just impossible.
*  And after convolutional neural nets had this breakthrough in computer vision, several of
*  us, including Jim DiCarlo's group at MIT and my group and then Yamins and Jim DiCarlo's
*  group started using these models to to predict responses in higher level visual
*  cortices. And we found that these models beat all other models that we ever tried.
*  So we had scores of other models, many of them computer vision, many of them much less
*  neurobiologically plausible than neural networks.
*  And suddenly we got sort of two things together, which seemed almost unthinkable.
*  A model that's neurobiologically plausible is abstract.
*  We want it to be abstract, right, as abstract as possible, but still neurobiologically
*  plausible. And a model that actually works and allows us to predict responses and
*  representations, patterns of activity elicited by novel images in these high level
*  regions. So that was a very big breakthrough.
*  And these models were completely feed forward.
*  At the same time, for me, this meant sort of the end of an era.
*  Right. So this was always the impossible thing.
*  This was the hard thing.
*  And now we can we can do that to some extent.
*  We're still not explaining all the variants, mind you.
*  Right. So we're not there yet.
*  Far from it. But suddenly it seems not that different than in early visual areas.
*  We were also not explaining all the variants.
*  Right. But at the same time, for me, this meant that this is in a sense, I mean, you
*  can still play this game and we should be playing this game for another two decades
*  to sort out all the details and get feed forward models that correspond layer by
*  layer to the areas of the visual system and maybe incorporate skipping connections and
*  things like that. But at the same time, the feed forward paradigm is becoming somewhat
*  exhausted in my mind.
*  And I think this is all right.
*  And this is this is correct.
*  And it's a portion of what is going on.
*  But it is a very small part of what vision is about, because vision is more than opening
*  your eyes and immediately having a sense of the stuff and the things that are there.
*  Vision is a process of inference.
*  Vision is relating.
*  It's a superpower by which you relate all the things around you instantly to your goals
*  and your knowledge in a very deep way.
*  You have a sense of your surroundings, of the geometry of your surroundings and of the
*  meaning of all the things in there and how they interact.
*  And that's a much more cognitive and a much more computationally complex process.
*  And I think that should be our target.
*  That's what we need to crack next.
*  Well, I feel compelled as well to, you know, we have talked all everyone that I've talked
*  to who's using the convolutional neural nets to model the vision.
*  It's always the ventral stream that's being modeled.
*  So that's where we recognize objects and abstract things.
*  But there's a neglected dorsal stream of processing as well.
*  Absolutely.
*  Where we process motion and where things are.
*  So, yeah, I didn't mean to cut you off there.
*  So that's good. You just described how abstracted artificial neurons are from real
*  neurons. And of course, that that is an understatement.
*  If you ask any ionic channel researcher, like you said before.
*  But so how biologically realistic or how least abstracted do you think that we're going to
*  need to eventually make models to to understand the brain's computations and functions,
*  whatever that means?
*  Yes. So so we have this set of tools from AI and machine learning and deep neural networks
*  are a big one. But even all of them together don't come anywhere close to modeling
*  what the human brain and biological brains more generally can do.
*  Even in vision and certainly in other domains, when it's about deeper inferences,
*  we don't really have artificial general intelligence yet.
*  So there's clearly something that we're missing with all of the models that we have now.
*  And that's a great mystery.
*  And that's why it continues to be important, even if you only care about the engineering
*  perspective, to think about the brain, because the brain is or the human brain is one one
*  example of a system that clearly goes beyond anything that we can build at the moment.
*  So I think therefore, you know, if engineers are working on AI technologies, they might not
*  care so much about biology because they're they want to optimize a particular system for
*  particular application. And they've got enough to to worry about.
*  But I think even even in engineering, even if your ultimate goal is just to make AI and
*  make really push the envelope of AI towards artificial general intelligence, people who care
*  about that often are also deeply interested in the brain because it's got these these
*  tricks that we can we can glean from it.
*  And part of it is going to be in the biological details that we're currently not capturing
*  with these models, only we don't know exactly which details matter.
*  Do you think that we might that it's possible that we could be suffering from what's called
*  the curse of knowledge? Right.
*  I think I had this right. But you believe that we have to understand cognition, have to
*  understand brains to really develop a general AI.
*  Am I right about that?
*  I'm just you know, I'm wondering if we're limited just because that's what we know.
*  Maybe I wouldn't put it quite like that.
*  I don't think it's impossible that we will develop artificial general intelligence without
*  understanding the brain.
*  And it would be a very good.
*  So if engineering achieved that without caring about the brain, then that would be very
*  helpful for brain scientists, because that would give us even better tools for modeling
*  intelligence in general, which we could then apply to understanding the brain.
*  Right. So I think that is very possible.
*  But at the moment, we're in a position where the brain can do things that we can't do
*  with engineering. And so naturally, you know, instead of reinventing it, we might be
*  tempted to peek at the only existing solution.
*  Yeah. OK. So you mentioned skip connections possibly being important.
*  And those are just we haven't really talked about recurrent.
*  You asked me about recurrent.
*  Oh, yeah, sure. Please.
*  So recurrent connections, I think, are absolutely key to all of this.
*  And they're ubiquitous in the visual system in particular, but of course, throughout the
*  brain. And they enable the system to base inferences on previous inferences.
*  So basically, to to go on computing on the basis of the outputs of previous
*  computations, and that enables the brain to use time as a computational resource, as
*  long as you're just sweeping through a feed forward network very quickly, you you run
*  out of layers. So you run out of neuronal resources to do that.
*  And so it's it's very inflexible, even though all these models are, you know, universal
*  function approximators and so can potentially approximate anything that you might want.
*  They're limited because we're limited with the resources of the brain.
*  And if we can recycle our resources through time, then we can compute much more
*  interesting and useful functions.
*  Yeah, I mean, that's what I see in the literature is just the advent of incorporating the
*  recurrent connections within all the convolutional neural networks.
*  And you have a recent piece on that yourself.
*  So, yeah, so we think at the moment, you know, we think that the feed forward
*  convolutional framework, that is the new null hypothesis of the ventral stream.
*  And so we want to take steps sort of starting with the system that we understand pretty
*  well and we can get it to work and we want to change one thing at a time so that we
*  understand what we're doing and we can be on top of it.
*  And so a straightforward way of bringing in recurrent dynamics, which potentially
*  puts us in this whole new world of much more interesting computational powers, is to
*  make the convolutional networks, hierarchical convolutional networks recurrent.
*  And that gives us these what we call BLT, bottom up, lateral and top down
*  connected convolutional neural networks.
*  So now every unit doesn't only see a restricted receptive field in the layer below, but it
*  also sees its neighbors within the same layer and it sees a restricted receptive field in
*  the layer above. And then it learns a little weight template and it's still convolutional.
*  So that weight template, which includes the B for bottom up, the L for lateral and T for
*  top down components. So it's sandwiched in between there.
*  It's kind of a joke with the BLT.
*  So that's that weight template is automatically generalized across spatial positions.
*  So that means that you that the number of parameters actually doesn't explode and you
*  can efficiently train these systems with back propagation through time.
*  And then you have a much more powerful and a very interesting framework.
*  And so so far we've seen that this just I was amazed how quickly my brilliant graduate
*  student Courtney Spura and another graduate student who's now a postdoc at the NIH,
*  Patrick McClure, got this to work.
*  So basically without having to tinker endlessly with the architectural hyperparameters,
*  basically out of the box, these models dominated parameter matched feed forward control
*  models. So this is an important sort of framework that we're exploring at the moment.
*  So you mentioned back propagation through time.
*  So I've had recently I had Blake Richards on the show and I've had Adam Marblestone.
*  And we've talked about how back propagation or process like it might be occurring in the
*  brain might be implemented in the brain.
*  And so what you've talked about so far with adding the recurrent connections is really
*  just still connecting.
*  It's almost like a different graph.
*  Right. You're still connecting the nodes, but in a way that allows it to have recurrence.
*  But do you think that there are any can do any lower level features of neurons and the
*  way that they process signals come to mind that you bet might be important to really
*  making these systems more efficient and moving forward?
*  So you're talking about lower level biological features, how to incorporate biological
*  realism? Yes, incorporating biological realism into the models.
*  So, for instance, Blake Richards made this model where it's not just a single unit.
*  His his artificial unit also has a dendritic like an apical dendrite that then can carry
*  out back propagation, et cetera.
*  And so that was one way to incorporate biological realism.
*  And I'm just wondering if you have other guesses or thoughts as to what might be important
*  to include. Yes.
*  So I love that work.
*  And I think it's right there in the realm of looking to biology for inspiration about
*  how to make these these systems function better.
*  And everyone has a has a list of, I think, features of biology that might be interesting
*  to incorporate.
*  And I think we have to explore this whole space and then everyone will have a different
*  order of priority.
*  And that has that's more subjective.
*  That's more sort of the pragmatism of what will pay off and what sort of relates to
*  what we've worked on before, what is a reasonable order in which to explore all these
*  different things. Right. So high up on my list is recurrent connectivity.
*  Equally high up is skipping connections and stochasticity, which is present in the brain
*  throughout. And there are very interesting theories about how it might serve to represent
*  uncertainty and compute with uncertainty, taking the process of computation in the
*  direction of cognitive ideal of proper probabilistic inference.
*  And so that's that's very high on my list.
*  And then there there are global aspects of the architecture, for example, how deep is
*  it? What are the different areas?
*  Can we take connectivity constraints directly from the literature, build them into the
*  architecture and then train with that propagation and evaluate different different
*  architectures and understand why the architecture, the global aerial connectivity of
*  the visual system is the way it is.
*  That's that's high on my list as well.
*  And then, you know, at some point we get down to questions like spiking.
*  Do we need spiking neurons?
*  There's a big computational neuroscience literature on spiking models.
*  They're very difficult to train, but it's it's an interesting question whether spiking,
*  which is known to help with long range signaling in the brain, also has a computational
*  function. For example, some people relate it to drop out in deep neural networks where you
*  have sort of this stochastic nature that can help regularize the learning process.
*  And then there's a whole machine learning literature that reinterprets that in the context
*  of probabilistic inference, where you have probabilistic inference at the level of
*  learning. And then it's like a prior that regularizes the learning.
*  But then you should carry over your uncertainty about the parameters that you've learned into
*  the inference, the perceptual inference as well.
*  So you should keep sampling from so run the network with the stochasticity and then
*  interpret the distribution of outputs as a representation of the posterior.
*  So the probability distribution.
*  Does that work coming out of Tinnenbaum's lab?
*  No. So I associate this in machine learning with Zubin Garamani's group and in particular,
*  the graduate student Yarin Gao, who reinterpreted drop out in this way.
*  There might be earlier work along these lines that he's drawing from interpreting this
*  in the framework of variational inference.
*  So this is something that we're also exploring.
*  But at the moment, we're not exploring this with spiking neural networks because they're
*  very difficult to train.
*  But we're exploring this with rate coded neural network models where we are nimble with
*  the training. We can use all the tools of deep learning.
*  But in addition, we're bringing in this this feature that's ubiquitous in biology and has
*  these interesting links to machine learning Monte Carlo and Markov chain Monte Carlo
*  inference and machine learning.
*  And we find that that actually does enable our models to represent their own uncertainty
*  much more accurately.
*  So when did their probabilistic estimates, you know, when you when you predict that it's
*  going to rain with 80 percent probability, then out of all of those cases where you set
*  that when you look years later, ideally, it rained in 80 percent of those cases.
*  That would mean you had well calibrated uncertainty, right?
*  Unlike someone who's always sure and then half the time wrong, which is what neural
*  networks in general can be if they're not sort of especially designed to deal well with
*  uncertainty.
*  Yeah, I haven't had anyone yet on the show also who who deals with the spiking neural
*  networks either. And it's just interesting because spiking is such a fundamental neuronal
*  process that absolutely all these neural nets use rate coding instead.
*  Yeah.
*  All right. Well, thank you, Nico.
*  This has been a really interesting talk.
*  I have just a couple more questions if you have another minute or two.
*  So so you have the current state of brain science and the current state of artificial
*  intelligence. So what kind of what do these things share?
*  You know, where do these where do brain science and A.I.
*  overlap with the way things currently stand?
*  So there are all these things that the human brain can do that computers can't do yet.
*  And that's where the common interest lies.
*  And that's sort of, you know, I'm thinking of DeepMind, for example, they're very much
*  about A.I., but they care deeply also about the brain because it inspires them, right?
*  And I think that's for good reason.
*  They care about how the only system that implements these functions implements them.
*  And I think, you know, that that's where the common interest is.
*  So this is also related to the history of of engineering that led into A.I.
*  So one strand of that is statistics and another strand is computer science.
*  Traditionally, statistics has optimized statistical efficiency and computer science has
*  optimized computational efficiency.
*  And I think, you know, until the hearing and talk from I think it was from Michael Jordan,
*  I didn't really relate these two to each other, but they're they're deeply related.
*  So statistical efficiency is all about being efficient with data.
*  So making the best possible inferences given the limited data that you have available.
*  And computational efficiency is all about having balance on the runtime of your algorithm,
*  given some input.
*  And because these were totally separate traditions, we haven't really understood how to
*  to integrate the two.
*  And so but but now it just in engineering with big data, we're facing the challenges where we have
*  to integrate them.
*  So let me give you an example.
*  So let's say you have web scale data to make some some inference.
*  Right.
*  And you know what kind of inference it is.
*  And you can look up in your statistics textbook what the optimal algorithm would be for that.
*  But then you find that it's so computationally inefficient that you can't run it on all of your
*  data.
*  Right.
*  So what you want to do to get the best possible answer, let's say you have a year and you have a
*  limited budget for computation.
*  What you want to do is run an algorithm that's not statistically optimal, but that strikes
*  a good compromise between statistical and computational efficiency.
*  And therefore, after one year will give you the best answer.
*  And we see exactly this trade off also play out in brain science, where we have the most statistical
*  tradition, which one instantiation is very important and influential as probabilistic graphical
*  models.
*  They're statistically very, very neat, and you can do inference on them.
*  And they've been generalized in a way that they can grow with the data.
*  And that's sort of this tradition.
*  And then the neural network tradition, from my perspective, is more part of computer science,
*  where the inference is more computationally efficient, but they need huge amounts of data.
*  Right.
*  So they come to be dominant in areas and in eras where you suddenly have so much data
*  that this is not a problem anymore.
*  Right.
*  That's why when we had web scale data for training computer vision models, suddenly
*  neural networks also became so powerful.
*  Right.
*  But the brain manages to combine data efficiency and computational efficiency in ways that are
*  beyond current AI.
*  And I think that's one very deep mystery that is shared between brain science and engineering.
*  Interesting.
*  Oh, this is all just so easy, isn't it?
*  I wish.
*  Yeah.
*  So the further I went in my career in neuroscience, the more I heard people invoke
*  David Maher's three levels of analysis.
*  And you've written about that as well in some of your reviews.
*  And just to go over them briefly, so David Maher proposes three levels of analysis.
*  At the highest level is kind of computational theory, like what functions need to happen.
*  What should the brain compute?
*  What should the brain compute?
*  Thank you.
*  Yeah.
*  And then the next lower level is representation and what algorithms should be implemented to
*  accomplish these things.
*  And then at the lowest level is how the brain does it, the neurobiological implementation.
*  Yes.
*  And so this was referred to more and more, I felt like, as my little career went on.
*  But how do you think historically we will view or appreciate David Maher's levels of analyses?
*  So first, in my mind, they map directly onto what we just talked about.
*  So what should the brain compute?
*  That's looking at everything at a global level.
*  You look at the whole animal and it's engaged in the task.
*  So you want to understand what are the requirements of the task and what is the best way,
*  what is the information processing that allows the animal to choose the best actions, right?
*  And looking at it from that global level means that what you care about is what is the
*  animal given?
*  Well, it's given the data and it has to make good decisions.
*  Which is to make good inferences.
*  And so it's all about being efficient with the data.
*  So in my mind, the top level of computational theory is associated with statistical efficiency.
*  And I think it's not a coincidence that many of the people in cognitive science that are at the
*  intersection to statistics, and I'm thinking of Michael Jordan and Josh Tannenbaum and
*  Tom Griffiths and others, they are very deeply invested in the statistical way of looking at
*  things.
*  And then if you go one level down to representations and algorithms, even these terms are
*  computer science terms, right?
*  So now it's about time complexity, it's about the steps of computation that you need to go through
*  to compute the thing that you should compute.
*  So now it's about what does the brain compute with the limited time that it has, right?
*  And then you could say one level down at the implementation level, then it's about space
*  complexity.
*  So you have limited components and you're building the system up out of neurobiologically
*  plausible components where you also have a limited budget in terms of the number of neurons that you
*  can use and how you can connect them such that the volume of the axons fits in the skull and you
*  have a limited energy budget as well, of course.
*  Yeah, it's an important one, I think.
*  That topic is heating up, I feel like, in the literature.
*  Absolutely.
*  It's a beautiful way of saying it.
*  Well, Nico, this has been a lot of fun for me.
*  Thank you for joining me here on the show.
*  There's so much more we could talk about and I might just have to pester you again later
*  to come back on the show.
*  You're always invited back, of course.
*  And before you go, where do you think people should go to find out more about you?
*  I know your lab is on Twitter.
*  Is that where you think people should seek more information?
*  Yes, I have a Twitter handle.
*  I think the most important thing maybe is to go to the website of cognitive computational
*  neuroscience because there's good resources there.
*  There's all the talk videos.
*  That was very important to me that we put them all up there so there's more than just
*  an event once a year, but people can engage throughout the year.
*  And we also have a historical record of all these even contributed talks by students,
*  but also, of course, the keynotes where we try to invite the leaders of the field.
*  And many of them are really great.
*  So I think that would be great if people check that out.
*  Okay, I'll definitely link to that in the show notes.
*  And I know you've got to go because you must have some other conference right now
*  that you're preparing for.
*  No, I've got a meeting with a graduate student.
*  Well, Nico, thanks again and I appreciate the time.
*  Thank you, Paul.
*  All right, thanks again for listening.
*  If you have questions or suggestions, email them to me.
*  Paul at braininspired.co
*  I'll keep working on it.
*  See you next time.

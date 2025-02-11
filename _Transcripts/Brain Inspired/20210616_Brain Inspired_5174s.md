---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5174s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 12351
Video Rating: None
---

# BI 108 Grace Lindsay: Models of the Mind
**Brain Inspired:** [June 16, 2021](https://www.youtube.com/watch?v=wx3mPVXPRiE)
*  I can prove that this kind of cognitive task and this output in terms of
*  behavior can be created by neurons interacting. That's what an artificial
*  neural network tells me, and that's reassuring. That lowers my heart rate a
*  bit. Using mathematical models and quantitative methods is like really
*  important for understanding the brain, and the history of doing so has been
*  long and complicated and probably spans more centuries than people realize.
*  There's no like really correct mathematical equation for any, you know,
*  problem in neuroscience. You know, people have whatever background they do if
*  they're coming from physics or something like that. They have a way that they see
*  the world in a set of equations that they use as tools to understand the
*  world, and they can see how those map onto the brain.
*  This is Brain Inspired.
*  When I say neuroscience these days, I think many, if not most,
*  neuroscientists would almost assume that I mean computational neuroscience,
*  because the computational approach has come to dominate much of the field, and
*  it's what we often discuss on the podcast. Computational neuroscience
*  basically means using mathematical models to connect some cognitive function
*  to brain activity. For example, reinforcement learning models connect
*  reward-related behavior to dopamine-related brain activity. And in this
*  way, computational models serve as testable hypotheses or theories about
*  brain functioning, and these kinds of models are responsible for much of the
*  recent progress in neuroscience. Enter Grace Lindsay and her book, Models of the
*  Mind, How Physics, Engineering, and Mathematics Have Shaped Our Understanding
*  of the Brain. This is an awesome book that summarizes the major approaches that
*  occupy the workdays of a vast number of neuroscientists these days. So each
*  chapter focuses on a theme and relates the history of that theme, how it came to
*  be, its conceptual underpinnings, and the modern landscape, what's going on now in
*  neuroscience related to it. So it's a great broad introduction for laypeople,
*  and it's also a great summary for those already in the field who are wanting to
*  expand beyond their own expertise. Grace makes her bones, well her academic bones,
*  I guess, studying vision in brains by creating and testing deep learning
*  networks, and she does this currently as a postdoc at the Gatsby Computational
*  Neuroscience Unit at University College London. During this episode, we discuss a
*  handful of topics related to what she writes, like what's good and what's bad
*  about using math for neuroscience, the birth of AI and the computational
*  approach, some of the people involved there and some of the ideas, the neural
*  code, using Shannon information to study brains, graph theory and network
*  neuroscience and relating structure to function, grand unified theories of the
*  brain, and we touch on other topics as well. Show notes are at braininspired.co
*  slash 108. If you find this podcast is improving your world, you can improve my
*  world and therefore improve the podcast by supporting it on Patreon for super
*  cheap. It helps a ton. And you can join the Discord community that I've set up
*  for myself and other like minded folks to discuss various things. Thank you,
*  Patreon supporters. I am grateful for your kindness and appreciation. Here's
*  Grace. Grace, welcome back. How you been? How's things? How's the how's the kid?
*  Kid is good. Very cute. Learning to crawl. Totally fun having a baby in a
*  pandemic.
*  Yeah, not destroying your career though. Having a child.
*  You know, I think everyone's career was a little destroyed this year. So not so
*  bad.
*  That's true. Before we start talking about the book, let's talk a little bit
*  about your your research. I just you know, want to know what's going on. What
*  what did you think about last night laying down in bed something that you
*  don't know about what you're doing? What are you striving for? That where's the
*  edge of your knowledge end these days?
*  Yeah, I've been feeling and I guess this has been true for almost all of the
*  history of neuroscience. But the hard part for me to think about now is stuff
*  that is in between sensory and motor.
*  That tiny, that tiny amount that's a little sliver that we still got to figure
*  out. No, I mean, obviously, you know, I, I've studied vision a lot. And even just
*  the visual system, even the retina is actually very complicated. And we still
*  don't fully understand it. But I feel like there's at least a sense that like,
*  we got the basic gist of things, and we have the right kind of frameworks and,
*  you know, we can sort it out. And then on the motor control side, I don't know
*  I don't study it directly. But I did look into it for the book, because there's a
*  chapter on motor control there. And you know, it's a tough thing. It's got its
*  issues. But there are reasons to believe you can understand how neural activity
*  controls muscles and therefore movement. But yeah, when I really tried to think
*  about, like, do we even have the right frameworks for understanding how we have,
*  you know, a coherent model of the world in our minds, and how we use that to plan
*  and all of those kinds of things. That's where I little, I go a little, you know,
*  off the rails a bit in my mind, I can't, I can't really even grapple with the
*  right way to ask those questions. Obviously, people study these things. But
*  it just feels like, you know, the things that you can study in the lab, with
*  methods that we have now, it feels like there's just still a lot there that
*  where there's going to be whole new principles and frameworks that we're not
*  even talking about yet, is my guess. And so that feels uncertain.
*  I have that same sense. And I don't know how much how well it meshes with with
*  your sense of it. But from my perspective, right now, I think it would be
*  accompanied by a sense of dread, where I doing active research, you know, asking
*  a question and seeking to create an experiment that will, you know, the, the
*  right experiment to answer the question or the right model, and etc. Right now,
*  I feel I'm filled with joy, because it's there's so much to explore and, and
*  learn to think that our fundamental frameworks could be in peril, you know?
*  Yeah, I see that perspective. I think there are there. There are types of
*  researchers that really like the big open, like, there's nobody knows what's
*  happening here, and I'm just going to take a step. And then there are some
*  researchers that are like, there's this little inch left to go. And I really
*  want to like, put a button on this and get it done. And I think I fall
*  somewhere in between. I want some sort of scaffolding, and then I'll make kind of
*  connections between established points. And really, what kind of prompted me to
*  think about, you know, the vast open space of cognition is just because in
*  studying vision, I'm kind of always interested in like, what the next step is,
*  like I was studying primary visual cortex. And it's like, well, how is this
*  information used, you know, in later visual areas and all of that. And now I'm
*  kind of interested in how vision is used for cognition and action planning and
*  that kind of thing. And it's like, ooh, I don't even know, like, is there enough
*  scaffolding for me to jump to that next step to connect the output of the visual
*  system, so to speak with the rest of the brain? And yeah, so the openness of it,
*  you know, different levels of openness for different people is what I would say.
*  So you're not filled with dread. So that's good.
*  No, I would not call it dread. And some of it is like, maybe I just need to read
*  more of the literature. Maybe there's scaffolding out there, and I just haven't
*  found it yet.
*  Right. Oh, this is this actually directly relates to stuff we're going to talk
*  about in your book. But I mean, do you see this as, I mean, not to harp on this,
*  but do you feel like it's limiting your progress now? Or do you feel like you can
*  kind of carry on with these open questions and still make progress as as
*  science tends to do anyway?
*  Yeah, I feel like yeah, I can still make progress. I mean, also, there's just
*  plenty of kind of unresolved questions, even if we just focus on sensory systems
*  or motor systems. So there's still stuff to be done for sure. And personally, my
*  research uses artificial neural networks, which you can train to do whatever you
*  want. And so at least in those networks, I can have some control over what they
*  do and how they use visual information and study that. So that helps me because
*  it grounds some of the behavior. Like, I can prove that, you know, this kind of
*  cognitive task and this output in terms of behavior can be created by neurons
*  interacting. That's what an artificial neural network tells me. And that's
*  reassuring. That lowers my heart rate a bit. It's like, it is possible. I'm not
*  really understanding how that is happening. I'd like to know more, but I
*  can at least be sure that it's possible. I mean, the brain technically proves that
*  as well. But just a lot more going on there. Whereas in the artificial neural
*  networks, I can say pretty directly, what's responsible for what?
*  Yeah, that is reassuring. To me, you're you've been ahead of the curve two times
*  here, just within our conversation, regarding our conversation, one with your
*  child, because it was pre pre pandemic. And I think, you know, once more and more
*  people get vaccinated, there's going to be like there's gonna be like a nine
*  month. It's gonna be like after World War Two, right? The baby boom, there's
*  gonna be like a little mini boom, right?
*  Yeah, I think it's already happening. I think some people were like, we're home, I
*  guess. Let's do this now. I think we're already seeing some quarantine babies,
*  as opposed to in elevators. Yeah, quarantine babies. Oh, gosh, the
*  quarantine boom. Yeah, that's a that's not something I would want to be part of
*  that, you know, just the label itself. But the other thing I think you're you're
*  ahead of is the book boom, because everyone went home and wrote books. And
*  you were ahead of that as well. So congratulations for getting your book out
*  well ahead of that.
*  Thank you. Yes, I had to stay home by myself before it was legally mandated.
*  To write a book.
*  Do you agree, though, it seems like everyone's writing books now. It's like,
*  oh, this is a nice side effect.
*  But I can't tell if it's, at least for me, you know, there's that effect where
*  like, once you hear about something, you see it everywhere. And it's like, okay,
*  well, I wrote a book. So I'm really interested in like, who else is writing
*  books? And what are books about? And that kind of thing. But if you're saying it
*  too, then then maybe it is a real effect.
*  Overall positive experience writing a book?
*  Oh, yeah, sure. Yeah.
*  Better than blogging? Worse than blogging?
*  Better. One, because there's a possibility of making money. And but
*  also, I put more effort into it, because it was going to be a real physical book
*  and the pressure of that and working with a proper publisher and everything just
*  really makes you want to do well. But more difficult because you can't share it
*  for so long until after you're actually kind of done with it. Whereas I'm so used
*  to just being like, ah, here are my thoughts. Go, let's get response and
*  everything. Yeah. So the waiting has been very strange.
*  Well, it's here now. How's the feedback? I love the book, by the way.
*  Congratulations. I mean, the work that you put into it really paid off.
*  Are you getting all sorts of feedback? When are you going to give award speeches
*  and stuff? Yeah, I've been getting some feedback.
*  So it's out now in the UK and in India, and you can get it in Europe as well.
*  So it's got, you know, pretty good distribution already.
*  So people have read it and given me feedback.
*  How's that feel just having it out in the world?
*  It's weird because people will like send me pictures of themselves holding it.
*  And it's like, oh, my God. And it's also I don't there's something about knowing
*  that there are like multiple copies that is weird, because in my mind, it's
*  like the book. Like it's this one thing that was like on my computer for a long
*  time. And now it's like there's just copies of it everywhere.
*  So, no, it's really cool to have it out there.
*  And obviously, I wrote it because I wanted people to read it because I think
*  it's interesting stuff. So it's cool that people are reading it.
*  And I hope that, you know, it it provides interesting information for them,
*  whether they're in the field or not. That was kind of my goal.
*  So Models of the Mind.
*  I'm going to read the subtitle here. How physics, engineering and mathematics
*  have shaped our understanding of the brain.
*  Just super big picture.
*  If you had to choose one thing, what would be the one thing that you would want
*  people to take from the book?
*  So thinking about kind of a general audience, like people outside of
*  neuroscience, what I really want people to know is that using mathematical
*  models and quantitative methods is like really important for understanding the
*  brain. And the history of doing so has been long and complicated and probably
*  spans more centuries than people realize.
*  And it kind of touches every part of the study of the brain.
*  So for the general audience, it was like, this is the thing we do and it's really
*  important and it's actually kind of cool.
*  And you can understand, you know, the impact of mathematical modeling on the
*  brain, despite the fact that, you know, mathematics and the brain sound like
*  scary topics to understand.
*  Actually, when you put them together, they're almost easier to understand.
*  Yeah, better together than math and the brain.
*  And then, yeah, and also I was, I did have in mind the fact that, you know, people
*  in the field, I would want them to want to read it as well.
*  And so providing the history and kind of the personal stories, I think, at least
*  for me doing the research for the book, it was really interesting to learn about
*  those and relate it to the present time and my stance as a researcher and all of
*  that.
*  I'm going to give you a quiz in just a second here, so that'll be fun.
*  But before that, so obviously math is good for studying the brain, but you talk
*  about, you know, so maybe we can talk about what's good and what's bad about
*  math for studying the brain, because there are some downsides, right?
*  Or at least one or two downsides.
*  So you kind of touched on what's good about using math.
*  I don't know if you want to expound on that, but then maybe also what is a
*  potential downside to it?
*  Yeah, so I think the good is that it forces researchers to be explicit in what
*  they think is going on.
*  So if we're thinking about kind of building mathematical models that are meant
*  to replicate something you think is happening in the brain or with behavior,
*  then when you write something down in math, like you can't be wishy washy.
*  It's not like, oh yeah, this number is multiplied by that number, but maybe not
*  sometimes, I don't know, you know, you have to just be very explicit in the model of
*  what you think is going on.
*  And I think people can think that their mental models that they have kind of in
*  words are explicit and, oh, they could totally flesh it out easily, no problem.
*  But I know from building mathematical models, you can think that.
*  And then when you sit down to do it, it's like, oh, oh no, there are huge, you know,
*  chunks of data that were missing here that make it impossible to put these ideas
*  into a model.
*  Or I didn't actually know how these, you know, different variables interact in a
*  way that I thought, I don't know how this brain region is connected to that one or
*  whatever it is.
*  So building the models forces you to be explicit, which is very important.
*  And then it's also a way to test your hypothesis.
*  It makes you define it correctly, like in very clear terms.
*  And then by running simulations or doing analysis, you can test if your hypothesis
*  kind of works the way that you think it does.
*  So I think that's definitely the good side.
*  The bad side is that in order to condense a biological system to an equation, you
*  got to get rid of a lot of stuff.
*  You got to throw a lot away.
*  And I'll even consider that slightly a positive, though, because it forces you to
*  identify what you think is important.
*  But it does mean that you're ignoring details that could turn out to be important.
*  And kind of once you've codified a concept in a mathematical model, it can be easy
*  for future generations to also ignore the details that you threw away, even though
*  those details are relevant.
*  So it makes sense that as a first approximation, you have to throw away some
*  details, but it can be detrimental if it sets the tone for a research trajectory.
*  And so I think that's one of the major downsides of using mathematical models is
*  just it forces you to decide which details you think are relevant.
*  And then you might kind of get caught in thinking that those details are irrelevant.
*  So these days, do you think that just including math in general, whether it's good or
*  bad math or pertains to good or bad ideas, do you think that lends credibility to
*  someone's scientific ideas?
*  I think it certainly does in the popular press, like people looking in from the
*  outside at a field, they might think that the mathematical side of a field is the one
*  that's doing something more rigorous.
*  I don't know if people, I mean, almost within neuroscience, you could argue that the
*  opposite happens because some people are suspicious of, you know, people who build
*  models, if only because they think that like, oh, you're not tied down by empirical
*  data, like you're just going off and dreaming, coming up with whatever you want.
*  So I think people do try to add equations and mathematics and do certain types of
*  modeling, especially around kind of data analysis.
*  Like you think if you collected data, you're supposed to do like the fanciest new
*  mathematical technique to try to understand it.
*  And that might, you know, be motivated by a sense that you're being more rigorous if
*  you do that, when in fact, that's not necessarily the case.
*  The same with any aspect of science, you can use mathematics well or poorly, and it
*  can lead to sound conclusions or it can lead you astray.
*  So I would say that it's possible some people add math to seem more rigorous and it's
*  possible that from an outside perspective that works.
*  But for the most part, I like to think that in neuroscience, it's being used mostly
*  appropriately. In your chapter on rationality and making rational decisions where you
*  talk about Bayes' theorem and the Bayesian approach to the brain, I believe it's in
*  this chapter, you talk about Hermann von Helmholtz, who is coming back around as kind
*  of seen as a central historical figure with some great ideas early on, specifically the
*  idea of unconscious inference, which is hugely popular right now in the computational
*  neuroscience world. But he didn't mathematically specify how it would happen.
*  Do you think that had he done that, he would have been appreciated sooner rather than,
*  I mean, everything happens on oscillations.
*  But do you think that would have sped the celebration of that of unconscious inference
*  ideas?
*  Yeah. Yeah, I will say I do love Helmholtz, researching him.
*  It seemed like he knew so much.
*  And from what I could tell, he was also a decent person, which is sometimes rare in
*  historical figures.
*  I'd like to read a biography on him.
*  But yeah, so yeah, I mean, he was, he impacted a lot of things and is definitely appreciated
*  for those things.
*  But it is true that this particular idea of kind of the idea that when you perceive
*  something, you almost have to reverse engineer the causes of it.
*  And that kind of happens automatically.
*  And you combine, you know, past information, you bring that to bear on how you interpret
*  a scene.
*  So these were ideas that he had and talked about.
*  And he had the mathematical skill to, you know, mathematize things because he applied
*  it to other elements of like physiology and sensory processing in terms of like describing
*  the sensory organs and things.
*  But I don't know that having put an equation to that.
*  So the equation we now use to talk about that kind of thing is Bayes' rule and Bayesian
*  inference.
*  I don't think that putting an equation to that would have necessarily helped in part
*  because there's a sense that you can quantify or mathematize something too early before
*  you have enough data to really like fit a model or like make strong claims.
*  And so I don't know that at the time that he was working, if the type of experimental
*  work that was being done would have been so well suited to, you know, doing that kind
*  of analysis.
*  I think you do need, you know, you need a certain amount of maturity in data collection
*  and ideally some agreement on kind of what the basic tenets of a field or a question
*  are before it's really worthwhile to get concrete with the mathematics.
*  I mean, he was concerned with numbers.
*  He measured the action potential velocity of all, you know, nerve conduction velocity,
*  which was pretty awesome.
*  I mean, there is a, was he one of the tragic suicides?
*  Did he commit suicide?
*  I don't think so.
*  There's so many.
*  There are a fair number.
*  Yes, I don't think he was one of them, but I could be wrong.
*  All right.
*  I'm going to have to look this up and edit.
*  But yeah, he had so many amazing ideas.
*  So, okay, let's dive into the book here.
*  Let's start with a quiz because the your book does a few things that it does some work
*  a few ways on someone's mind on my mind while I was reading it.
*  One of the things that you've already mentioned, it really connects the history
*  of science both to the, you know, connects the history to present day and talks, you know,
*  gives like a real threads through the mathematical and computational literature to these days.
*  But in doing so, you also tell stories.
*  And for some reason, I don't know why, why does it help for us to know
*  a little personal information about someone to sort of solidify in our minds, even their science,
*  it just helps to know, oh, yeah, that guy like to fly kites.
*  That woman was a, you know, like a mountaineer, you know, or something like that.
*  Why does that help?
*  I think it's just because we are very agent based in our understanding of the world,
*  like we'll assign agency to inanimate objects if they're like moving in a certain way.
*  And so I think you want to, it's easier to remember concepts if it was like,
*  oh, there was this person who was fighting for this concept.
*  And this is, you know, what they were like, you want like a sense of there was a character
*  and an agent that was doing a certain thing.
*  And then that'll help you, you know, connected in a narrative way that is more memorable,
*  because there's like a temporal structure to it, like this led to that led to that,
*  rather than just like a series of facts.
*  So I think, yeah, we're just as humans, you know, geared towards understanding agency in the world,
*  because it's usually pretty beneficial to understand the world that way.
*  But it is you said character, but it is a caricature, basically, of, you know, but it still helps.
*  Okay, quiz time.
*  These are all facts from your book.
*  So we'll see how I told you I wrote it.
*  I finished writing this like a year ago.
*  Sorry, I know.
*  Claude Shannon developed a mathematical theory of blank information or communication.
*  Well, yes.
*  Okay, but sorry.
*  So the, the non these are the story.
*  These are the personal things in their lives.
*  Oh, oh, it's a juggling.
*  Yeah, you got it.
*  All right.
*  Also, Claude Shannon invented a flame powered.
*  Oh, no bicycle.
*  Frisbee Frisbee.
*  Ah, I see.
*  Yeah.
*  Don't worry, we have a few more.
*  Edgar Adrian was known to play with his students and enjoy this particular game.
*  A game?
*  No.
*  Social game.
*  Oh, he played hide and seek in the woods and valleys.
*  Yeah.
*  Yeah, it really helps.
*  I don't know that these things help for some reason.
*  Okay, there's no way you're going to get this one.
*  How many drawings did Ramonica Hall make?
*  It was something like 17 or 1900.
*  I think.
*  Oh, wow.
*  There's a seven in there.
*  Wow.
*  You got it all.
*  It's 19, 19, 1907.
*  Oh, wow.
*  Okay.
*  You got all of those numbers.
*  Last last one here.
*  What or who or how was BF Skinner introduced to Ivan Pavlov's work on reinforcement learning?
*  It was through an article in a popular magazine by, is it H.G. Wells?
*  Is that who it was?
*  Wow, you performed quite well on this quiz.
*  Just to get back at me, anything you want to quiz me about?
*  I didn't write the book, so.
*  No, that's okay.
*  I think it just shows that the small details are also what I remember best from the book.
*  Okay, so, you know, I think it's 12 chapters in the book, and obviously we're not going
*  to get through all of it, but I want to talk about some of the big bigger ideas in the book.
*  One of the things that you write about a book in the book is the sort of the birth of AI
*  and kind of the computational approach to thinking about the brain and intelligence.
*  So and like all good researchers, you start with McCulloch and Pitts at some point.
*  So I'm going to just read a quote from your book here.
*  With this step in their research, and this is talking about McCulloch-Pitts' early logic
*  gate conception of a neuron.
*  With this step in the research, McCulloch and Pitts advanced the study of human thought
*  and at the same time kicked it off its throne.
*  The mind, quote unquote, lost its status as mysterious and ethereal once it was brought
*  down to solid ground.
*  That is, once its grand abilities were reduced to the firing of neurons.
*  To adapt a quote from Letvin, the brain could be now thought of as a machine, meaty and
*  miraculous, but still a machine.
*  More broadly still, McCulloch's student Michael Arbib later remarked that the work, quote,
*  killed dualism, end quote.
*  Wow, that's heavy stuff.
*  Would you rather be McCulloch-Pitts, like the theoretician, or would you rather be a
*  Rosenblatt, the engineer?
*  Oh, that's interesting.
*  I think, can I just be McCulloch in particular?
*  Sure.
*  Oh, yeah.
*  You don't want.
*  Pitts was a suicide, right?
*  No, that was cirrhosis.
*  Yeah, I mean, he drank himself to death.
*  Drank himself to death.
*  Yeah, but also just Pitts was, his approach was much more kind of, it seemed like the
*  rigor really mattered to him, like you had to be getting things precise and mathematical,
*  whereas McCulloch came more from both philosophy and physiology, and I come from philosophy
*  and neuroscience, and that was just kind of like, it would be useful if we could put
*  this in math.
*  I think there's a way to map this to math, and that could be helpful, and that's kind
*  of how I think about the use of math in neuroscience or biology more generally.
*  So I think McCulloch particularly is where I would sit.
*  You live longer too, so that's good.
*  So you tell the story of the birth of AI, and all the way up really to modern day, along
*  the way you talk about the Minsky-Pappert criticisms of Rosenblatt's Perceptron.
*  So they kind of famously brought on the first AI winter by suggesting that multilayered
*  learning was impossible.
*  They didn't see how you could teach how a neural network could learn with more than
*  one hidden layer in it, and this brought about the AI winter, but it was really just their
*  opinion, which was the crazy thing to think about, is it was their opinion that it couldn't
*  be done.
*  Do you think that there is a lesson to be learned in retrospect about so much writing
*  on someone's opinion?
*  It's not just like they wrote a one-line opinion about this.
*  They wrote an entire book that was filled with math and solid reasoning, and that was
*  part of it.
*  But do you think there's a lesson to be learned there?
*  Yeah, so I think the canonical story is that the most important thing they did in the book
*  was prove that a single layer perceptron couldn't do certain important calculations like the
*  XOR problem.
*  That was a mathematical proof that wasn't their opinion on it.
*  But yeah, their stance towards multilayer neural networks was negative.
*  If they had concluded the book with, oh, a single layer couldn't do it, but we could
*  definitely do it with multiple and that's the way the field should go, that would probably
*  have a different outcome for the field.
*  So I think that proving that something doesn't work as well as you thought that it would is
*  one of the important reasons that you should mathematize things so that you can say with
*  some sort of clarity and confidence where the boundaries are on a model that you're
*  working with.
*  With regards to their intuitions and their general negative attitude towards it,
*  I think it's tempting to say, oh yeah, that was silly, people shouldn't have just kind of trusted
*  their predictions.
*  But when you're dealing with people who really took the time to study the single layer
*  perceptron in such depth and with such mathematical analysis and that kind of thing,
*  you know, people who were honestly interested in this and explored it,
*  I mean, science is really based on the intuitions of experts in terms of what to test next and just
*  coming up with hypotheses.
*  You can't prove your hypothesis, that's the nature of it being a hypothesis.
*  So we really do, yeah, we rely on, you can't prove it a priori at least, we rely on scientific
*  intuition to know how to guide things.
*  Now, whether it needed to be a whole big defund AI, everything's terrible, you know, winter
*  situation, I mean, that's a little dramatic, I guess.
*  But at the same time, the hype around the perceptron in AI at that time was also dramatic
*  and overstated, so that was kind of a backlash to the hype.
*  And so that's just pointing to the tendency of scientists like all people to kind of follow fads
*  and get really into one thing only to throw it away for another thing the next day.
*  And I think fads in general in science are probably somewhat problematic.
*  I can see arguments for why they might actually be useful.
*  But yeah, you know, the fads and the big swings up and down is perhaps what's more damaging
*  than anything.
*  Do you know if Minsky, I'm sure he addressed, because this is like the story told, you know,
*  the big first AI winter and Minsky Papert, do you know if he had thoughts about this in
*  retrospect later in his life about whether he regretted that?
*  Oh, yeah, I think there I mean, there's been a lot of interviews with him, and I think he
*  has reflected on it, but I can't remember exactly what he said about it.
*  Just whether I'm curious whether he admitted the damage, right?
*  Yeah.
*  No, I think brushed it off.
*  Yeah. So I have a quote in the book that I think is from Papert, who says, like,
*  understanding can be as bad as death, which is how they viewed what they did, like they showed
*  that the perceptron can't do something that people assumed that it would be able to do.
*  And that understanding is what killed it.
*  So I feel like in retrospect, their stance was, you know, we needed to have people understand
*  it. And the consequences of that are what they are.
*  But I'm not sure given, you know, the resurgence of deep learning today, if there'd be a sense of
*  like, oh, but we should have still encouraged people to pursue the general area.
*  Well, people did still pursue it.
*  And that's why I mean, people were always pursuing it. It wasn't winter for everybody.
*  So, you know, on a related note, in my little, so I run a little discord group from like Patreon
*  supporters from the podcast. And I was, you know, I don't know why I've been reminded of this
*  consistently lately. Just who has priority on ideas, right? And we always have to give priority
*  to some name. So examples of this, like the McCulloch-Pitts, right? They always get that,
*  they ushered in the idea of neural networks. But this person in the discord group,
*  multiple times has said, but Rushevsky was before them and had the ideas before them.
*  And this happens, you know, with Hopfield, right? John Hopfield always gets the credit for like,
*  Hopfield nets, but Steven Grossberg even wrote down the equations before. And it was called
*  something different. And I cannot remember the name because I know Hopfield nets, right?
*  And this is much the chagrin of Steve Grossberg, the cell assembly idea of Donald Hebb, who we
*  always cite, right? Before that was Konorski, I believe, you know, who, you know, who knows how
*  many people back propagation, Hinton gets all the credit, right? And it was Paul Werbos who wrote
*  the equations. I could go on, right? But it, and this is related to the idea of a story and needing
*  a narrative, you know, for us to even make progress in science, right? But do you think
*  it's important or damaging that we kind of idolize people and celebrate the people, even though
*  the people that we celebrate, the ideas that we celebrate them for are probably predated by
*  other ideas? Yeah. Yeah, I mean, in all of those cases, you know, and in all of science,
*  you know, the scientist is born into an existing atmosphere of ideas. And, you know, even in the
*  case of like, Ryszewski and McCulloch and Pitts, they were all at University of Chicago, and they
*  interacted, you know, that's like explicit interaction there. In other cases, I think with
*  Hebb, I imagine he did not know about the previous work in a similar direction. Well, he credited a
*  lot of previous people, actually, he was one of the people who said, Look, this isn't my idea,
*  and actually credited other people. Okay, yeah. Yeah. But did you know if he knew about?
*  I think he did not know about Konorski. Yeah. If that's the right name. Yeah. Yeah. I don't
*  think he knew there were some people he didn't know some people he did. Yeah, because I knew he was
*  at least I thought Konorski's book was like a year before his or something. So I'd be surprised if it
*  could have gotten over to him. In that time, in those days. Yeah, yeah, yeah, yeah, year isn't
*  necessarily that long if it's coming from a different country. But yeah, anyway, so yeah,
*  people are always born into existing ideas. And that's what they build on. And so I don't
*  think it's a problem to, to tell a story about a person and how they came to their ideas. And in
*  the book, I tried to give a long trajectory that includes multiple people to show that it wasn't
*  just like, there was a eureka moment, and nobody understood anything. And then after this person
*  came around, now everything was understood. And that's the end of the story. You know,
*  it's this back and forth between in the case of my book, it's a back and forth between
*  people on the biology side and bath and engineering and all of that. And so you can see that
*  the idea doesn't just spring into mind in one moment for most of these ideas, it's born out
*  of a lot of interactions. So yeah, just having just the accurate understanding of, yes, individual
*  people will make progress in a way where some people may make outsize progress compared to
*  other people. And so we can choose to talk about those people while understanding that, you know,
*  they stood on the shoulders of giants and all of that, or also if not giants, just regular people.
*  But they got help from from the environment they were in. And I would also say that, so I mean,
*  I had this issue when doing the research of, you know, starting with some landmark paper that I
*  knew to be very important, looking at what it cites and looking at what cites that paper to kind
*  of get these narratives, which Google Scholar makes very easy. That's an impossible task, by the
*  way, to, oh, well, you could really go down the rabbit hole. Yeah, I went down many rabbit holes.
*  But yeah, but the modern tools does make that a lot easier than it would have been very recently.
*  But yeah, in doing that and trying to see these connections, I mean, in a lot of cases, the
*  name that you know about, you know about because the person who taught you heard about it and the
*  person who taught them heard about it. And eventually the person who taught them knew the
*  person whose name it is directly, like, empirically, the people you've heard about had a big impact.
*  That's how you came to hear about them. So whether it was originally their idea or not, you can't deny
*  the fact that these are the people who people read and all of that. It's kind of like, you know,
*  should we still be teaching really old books to high school students? Like, does it matter if
*  anybody knows Shakespeare? Well, it matters because other people know Shakespeare and they
*  might reference it in art and you won't get the reference if you were never taught Shakespeare.
*  And so it's kind of like, at that point, it's not about the merit of the work. It's about the fact
*  that it's culturally relevant. And this is the touchstone for it for the field. And so in that
*  way, whether it's fair or not that someone is the known person for an idea, at some point, it just
*  becomes empirically true that they are the known person for the idea and their thoughts on it are
*  what have impacted the field more. So, you know, once someone becomes well known, like a heb or
*  something like that, people are going to go back and read their work and, like, you know, pay more
*  attention to their early ideas. They're going to read their later things more. They're just, if they
*  won this lottery of, you know, who gets credit for an idea that was invented at the same time,
*  then they are going to have more impact and they are therefore more relevant for the field,
*  for better or worse. It's interesting you use Shakespeare because he is known to have invented
*  so many words, like so many actual words. Well, supposedly, I guess we'd have to go back and do
*  the research. Who knows who invented those words? Who knows? Shakespeare, Schmicksbeer.
*  So another thing that is a recurring theme throughout the book that I found interesting,
*  and this is one of the testament to the value of a book like this, that it's all, like, condensed,
*  and so you can just see these themes within a condensed space kind of repeated. The theme is
*  rediscovering old math and applying it to current problems. And you actually touched on this before
*  when we were talking about Helmholtz, you said maybe it wasn't quite the right time for the math
*  at that point because there wouldn't have been anything to do with it because the right data
*  didn't exist. I guess the broad question is what should we take from this? I don't know. Maybe you
*  can talk about a specific example where there was math already 50 years before and we're either just
*  now using it or, I mean, I guess the classic example is Bayes theorem, but no one knew about
*  Bayes law back then. So maybe is there a different example from the book that you could highlight
*  old math that then has been repurposed and rediscovered?
*  LW Yeah, I mean, so I guess maybe there are two possible options. I mean, with the Hopfield
*  network and Ising models, that was something that was being studied in physics for a while before
*  Hopfield kind of imported it to neuroscience. And then also graph theory, the origins of graph
*  theory are very old with Euler, but they didn't get applied to neuroscience until, I mean, you
*  could really say like 10, 20 years ago maybe is when that field of network neuroscience started
*  emerging. And I don't think that the idea that there has been a mathematical equation or a
*  mathematical subfield around for a while and we didn't apply it into the brain until much later,
*  that doesn't bother me at all. It doesn't make me think like, oh, we were really missing out on an
*  opportunity in part because of, as I said, kind of you need the data in the field to be ready for
*  that approach. And also, I mean, in a sense, there's no really correct mathematical equation
*  for any problem in neuroscience. The way that they get used is that people have whatever
*  background they do, if they're coming from physics or something like that, they have a way that they
*  see the world in a set of equations that they use as tools to understand the world, and they can see
*  how those map onto the brain. But that doesn't mean that that was the only way to write an
*  equation for whatever problem you're thinking about. So I don't think of it so much as like,
*  oh, the right math was there all along and we didn't make the connection. It seems more like,
*  it was used when it was useful, when someone could conceptualize how it would be useful.
*  I mean, maybe in some cases, there's kind of obvious things we should have been doing,
*  like dimensionality reduction in neural data. Although even that, it's only somewhat recently
*  that we've been able to record from a lot of neurons at once. So we didn't really have a
*  dimensionality problem when you can only record from one neuron at a time. So the data needs to
*  be there for the mathematical tool to be useful. But we knew that the brain was made up of more
*  than one neuron. So some of these things, it's like you in retrospect, oh, why didn't we prepare for
*  that theoretically? I was going to ask you what, if you have a guess as to what model might be,
*  what mathematical model might be out there right now that is not being appreciated, but in 50 years
*  or so might be appreciated. But this is, before you answer, as you're just based on what you're
*  just saying, I realized, I mean, there's a lot of celebration in physics, in neuroscience, of
*  physicists are coming to help, right? Because they're bringing their mathematical models.
*  And you talk in the book about the difference between physics and neuroscience. So maybe we'll
*  touch on that in a second after this. But the equations that are being used in neuroscience,
*  from the old days, there was not neuroscience. So there was behavioral work and physics and
*  other sorts of things that, so these equations have been basically imported. But now the equations,
*  you could say, are neuroscience equations. There's new neuro math, right? Like deep learning theory,
*  for instance. In one respect, you could call that neuro math, I suppose, in some sense.
*  So the equations now are, 50 years from now, we'll look back and say, well, that was a
*  neuroscience equation. So anyway, I'm wondering if you have any wild guesses about what's being
*  underappreciated right now that you think might be rediscovered in 50 years or whatever.
*  Yeah. So I think extrapolating from what people are currently interested in, particularly with
*  respect to large scale neural recordings and all of that, I think there will be, and this is already
*  starting, so this isn't such a wild guess. It's just like, this will help. I think there will be
*  uses of topology in neuroscience for understanding neural manifolds and what is the low dimensional
*  structure of neural activity that exists in the higher dimensional space of all neural activity.
*  So you see some of that happening now. And I've just personally encountered computational
*  neuroscientists who think topology is cool. So I think that they want to have a reason to use it
*  anyway. So that might drive some of it. I'm not in mathematics, so I don't know, but I thought
*  topology was also just a hot area in mathematics at the moment. Maybe I'm completely off about that.
*  I don't know at all. Let me interrupt you because I think that what you just said actually speaks to
*  something that's exciting about neuroscience these days is if you just think something is cool,
*  you can probably import it into neuroscience and make it useful. There's a lot of different ways to
*  use math in neuroscience. And even if it's not useful, you'll probably still get to be able to
*  do it for a few years. But the idea of why don't we prepare theoretically for the coming onslaught
*  of data, I'm sympathetic to that. And personally, that's part of why I'm interested in trying to
*  study as kind of a model organism trained artificial neural networks, because we're in a
*  state of ignorance in some sense about how they work, but we can do any kind of experiment we want
*  on them. So to me, that's like, yes, we should just have neuroscientists who try to understand
*  this so that we can understand what understanding will be. How do you come to it? What kind of
*  questions are you actually trying to ask? And how can we use tools of neuroscience to answer those?
*  I think artificial neural networks are a great place to test those out. And then you get the
*  side benefit of maybe we understand the networks better, which is relevant for AI. So I do think
*  preparing is good. But at the same time, we're not always the best at anticipating what we're
*  going to want to know or what the real challenges of the data will be until we have it. So you could
*  put a lot of resources into preparing for something that doesn't matter. And the other risk of that
*  is that you prepared for something, you get the data, and that doesn't turn out to be the issue,
*  but you're going to make it the issue regardless, because that's what you prepared for. So I think
*  that's the risk of theory getting a little too far ahead of the data. But at the same time,
*  people are making decisions about what kind of data to collect and what methods to develop,
*  and those should be theory informed. So it's just about finding the right balance, I think, overall.
*  I mean, you just described a lot of careers, forcing whatever's happening into whatever idea
*  you had 20 years ago and making it conform to that story. You'll get in trouble if you agree with that.
*  I don't have to get in trouble anymore. What is the difference between physics approach and
*  neuroscience approach modeling and math wise? Yeah, I feel like to some extent, it's mostly a
*  difference of content of topic area. Physics is trying to understand very basic elements of how
*  the universe works, that's a lot of what physics is, and neuroscientists are trying to understand
*  the brain, but in either case, you might want to write an equation to codify what you know
*  and to make predictions. So on some level, it's just what are you predicting about.
*  Now, of course, there's a sense, especially when you get to really down to the fundamentals of
*  physics, that you're really describing reality. You are describing exactly what's happening,
*  and people even get into philosophical discussions of is mathematics reality? Is that the basis of
*  reality and all of that? Yeah. So you don't have that in neuroscience, I don't think.
*  You more explicitly understand that your equation is a very rough approximation to something that
*  you're interested in. It's just a model to help you clarify your thinking and all of that.
*  So in some sense, that difference could actually be quite consequential because it really pushes you
*  to maybe strive for different things. Certainly at the level of data collection that we have now in
*  neuroscience, you're not quibbling over like, oh, my model predicted the firing rate would be 3.15
*  on average and it's 3.14. What does this mean? Whereas in physics, those kinds of differences
*  can actually reveal something fundamental. We're just so approximate already that that's not going
*  to be the issue. But yeah, the use of mathematics feels in neuroscience maybe more like analogy,
*  whereas I don't necessarily know how physicists think about what they're doing, but maybe they
*  feel like what they're describing is somehow more fundamentally correct when they're using an equation.
*  I mean, you also talk about in neuroscience that we're studying something that has been
*  subject to evolution for a long time and how that makes a big difference. I mean,
*  it's just a messy complex thing. Things built on top of other things, barely functioning,
*  and then that gets used for something else and then there's this whole recursion problem.
*  I don't know if you want to speak to that. Well, yeah, it just means that physics is simpler
*  in many ways. Don't you tell physicists that, no. Hey, why did so many of them leave physics
*  to come to neuroscience? Because it's all figured out. It's too easy. Because we got the hard
*  problems. Yeah, exactly. Physics is too easy? Yeah, we got the hard ones. And experiments are pretty
*  hard in physics, the big relevant ones. But yeah, no. I mean, studying an evolved system,
*  especially with the mindset that we sometimes have to come in with for simplification reasons,
*  that it's optimal in some way or that it would be the way that the brain is would be how someone
*  would design it from scratch. That can make it difficult to understand because it is an
*  evolved system that is potentially quite hacky in many ways. And if you ever tried to look at
*  someone's code that isn't well documented, reverse engineering that is hard because it's like, oh,
*  they were originally doing this thing and then they changed their mind and wanted to do something
*  else. And so this function does two completely different things. And not that I'm talking about
*  my own research code at all. So it's like looking at your own code. It's just the same thing. It's
*  like a different person from two years ago. Yeah, yeah. That's right. That was one of your,
*  I think that was your answer to what has improved your life was to clean up your code,
*  which is awesome. And I did do that. And I started a project with very nice code. And then research
*  being what it is, I started having different questions and different goals. And so now that
*  code is a big jumble of nonsense. But next time I start a project, it will also be clean again.
*  Yeah. Other people's code. Speaking of code, this is one of the chapters devoted in the book is devoted
*  to the coding question and information in the brain. The brain as an information processor,
*  how the brain processes information, you know, what do spikes tell us about that and so on.
*  There, I'll read another, I'll read another quote here. I like reading the quotes. This is,
*  I don't do this much on the show. Just because scientists can spot a signal in the spikes,
*  doesn't mean it has meaning to the brain. There are many reasons this might be.
*  One important one is that the brain is an information processing machine. That is,
*  it does not aim to merely reproduce messages sent along it, but rather to transform them,
*  transform them into action for the animal. It is performing computations on information,
*  not just communicating it. And you spend a good deal of the chapter talking about Shannon
*  information and the development of that. And that's where I got the Claude Shannon story as well.
*  And in fact, I had a previous guest offline. She would not let me include it in the released
*  episode, but I think I asked her like what advice, yeah, what advice she might give to people studying
*  coming up in neuroscience. And it was, her advice was that Shannon information is worthless in the
*  study of the brain. And I was like, oh, that's such good advice though. Why can't I include it?
*  He was like, I don't want to, I want to keep my career, you know? So what do you think of
*  using Shannon information as a way to understand brain information processing? Yeah. I mean,
*  I don't think I would say worthless. I was paraphrasing and probably exaggerating.
*  Yeah. But it's the application of information theory to neuroscience and biology has been
*  somewhat controversial kind of from the start. And I go into this in the book of responses that
*  people had almost immediately after information theory came about, because it was applied to
*  biology very quickly after it came about. That's not an example of, you know, where the math was
*  sitting around for a while. You actually highlight that it is applied to biology a lot faster and
*  more widespread than it was to computers, which is what it eventually led to. Yeah. Yeah. It took time
*  for engineers to really make use of it. But yeah, it's tricky because, you know, part of in the
*  section that you quoted, you know, the brain isn't just trying to communicate. And Shannon information
*  theory is a theory about information communication and channels and how to best encode information
*  to send it somewhere. It's not a theory of how do you use information really, it's about sending it.
*  And that was obviously relevant, you know, to sending messages during World War Two and all
*  of that kind of thing. And just generally telecommunications and all of that. You know,
*  it's obviously legitimate and interesting question of how do you best send information that's going
*  to be relevant to society. But that, you know, if you're trying to understand the functions of the
*  brain and you focus too much on how the information is encoded in the sense of, is it optimally encoded
*  for sending, you know, you might just be a little bit astray because that's not the relevant
*  question. And especially, you know, there's some there's a view amongst people that amongst like
*  neuroscientists, there's a little bit of a push for like, we need to just think about the brain as
*  something that produces outputs, like it produces behavior. And, you know, talking in terms of
*  information, while that can be useful to kind of get a handle on something, you know, in terms of
*  the processes that lead to the production of behavior, what matters is, you know, does this
*  neuron make that neuron fire and then what happens from there. And so you can maybe get caught up in
*  quantifying the amount of information or anything like that when the question is just does this have
*  an impact? Does this matter downstream? Yes or no. So there, as I kind of said before about, you know,
*  this space in between sensory and motor, when you're in that kind of cognitive space,
*  it can be hard to really, you know, without referencing information, it's hard to talk about
*  what's happening there. Like, there's just there's stuff. Yeah. So you kind of have to talk about
*  information, you have to ask what information is present in the brain. But ultimately, what matters
*  is how the activity of neurons leads to downstream behaviors, ultimately. So it's just a matter of
*  kind of, you know, using as kind of with all of these mathematical models, it's a matter of
*  using the inspiration to help you get a handle on something. But don't forget about what you're
*  actually studying, which is a physical system, an evolved physical system that has to do adaptive
*  things so that the organism survives. That's, you know, ultimately what's going on. I love that. And
*  I think you reference this in the book, Shannon himself, you know, quickly after when, you know,
*  he developed his information theory with entropy and whatnot, saw the wildfire, you know, just
*  everyone was saying it's Shannon information, whatever field they were in. And he actually
*  published a very brief essay, it's worth reading, trying to throw a pail of water a little bit on
*  that and saying, look, this is just one way to look at it. Don't apply this to all the fields
*  out there. Yeah. And in a way, it's almost an example of like, you know, the warning that
*  not everything is amenable to mathematical analysis immediately. You know, this isn't just
*  because it's math, it doesn't mean that it's right and that it's going to solve all your problems.
*  That's not the take home you want for people who read your book. That's the byline,
*  just because it's math, it's not going to solve your problems. I like that. Yeah, you can do it.
*  Do you have thoughts on, you know, there's this old now, I don't know how many years old rate
*  coding versus a timing coding, right? How information is coded and transmitted in the brain.
*  Do you have, I don't know if you want to just sort of summarize the quote unquote debate,
*  and then maybe whether you have thoughts on it. Yeah, so this is just the idea that, you know,
*  the way that neurons represent information, if we're going to say it, is you can use it broadly,
*  right? We don't have to we don't have information, generally, but just that, you know,
*  the relevant thing to look at for a neuron is the number of spikes it produces over time,
*  and you can relate that to, you know, if you're looking in the visual system, you can relate that
*  to visual stimuli that exists in the world. And so that's the rate coding idea that you care about
*  the number of spikes that a neuron produces. Temporal coding would say something like,
*  maybe you care about the time in between two spikes or the time of a spike relative to some
*  other event, that that's where the information exists, so to speak. And so yeah, this has been,
*  you know, again, since information theory came about, people were trying to quantify how much
*  information the brain area has, but to apply Shannon's theory, you need to know what the
*  neural code is, you need to know what counts as a symbol in the neural code. And there were
*  different ways of defining this that led to like vastly different estimations of how much
*  information, you know, a given brain area had. And so those choices are, you know, the number of
*  spikes could be a symbol in the code, the time between spikes could be a symbol in the code,
*  you can come up with other possible symbols in the code to do this calculation. And really, I mean,
*  rate coding has been much more dominant. It's been, you know, and in some sense, it's been,
*  you know, proven to the extent that neurons do change their firing rate when the animal is
*  experiencing different conditions, like we can say that much, at least. But also, there have been
*  occasions where a timing based code has also shown to been shown to carry information about
*  the same kind of stimuli. So I think it's just a matter of, you know, what system are you studying?
*  What question are you asking about that system? It could be a combination of both. I mean, again,
*  there's no reason to assume this crazy evolved system has a single neural code. Or it also,
*  the question of like the neural code really does feel to me a little bit like, you know,
*  you're really thinking about a designer that says like, this is where the information is.
*  Whereas, you know, if the rate of neurons and their timing changes how a downstream neuron
*  fires and therefore changes behavior, then it matters. And so it's not going to be so clear that
*  like, the rates are what matters and the timing is irrelevant. If it can impact something else,
*  if the timing of the spikes impacts something somewhere else in the brain, then it could be
*  relevant. So it's all going to depend on the specifics of the question as to, you know,
*  which code is most in use. Yeah, I mean, there are reasons also to think that both would be useful,
*  for instance, a rate code, you might not want to transmit, I'll say information, unless there's a
*  certain amount of confidence, you know, that it is whatever, Jennifer Aniston or something. And,
*  you know, so you need a lot of spikes in a row in a short period of time, right, to get over some
*  threshold. However, an efficient coding hypothesis, something like Barlow, which you describe in the
*  book, Barlow's efficient coding hypothesis, you know, might suggest, and this goes back to the
*  designer idea, which evolution is not a designer, but if you were as efficient as possible to
*  allow as many possible types of information to be transmitted, then you would want an interspike,
*  a timing code, an interspike interval code, because you there's a lot more information
*  available to transmit through that. So but this is, you know, still a dominant, I think like Randy
*  Gallistole argues that latter point that you would, you would really want a more, a higher
*  capacity code is a, you know, timing code allows for a higher capacity of information processing.
*  So this is still a debate that's still going on. It's not, it hasn't gone away at all.
*  Yeah, for sure. No, no, no. Yeah. I want to talk about graph theory and network neuroscience,
*  which you devoted chapter two, let me see, it's chapter nine, actually, from structure to function.
*  You know, I have a quote here, I'll read a quote. The language of graph theory offers a way to talk
*  about neural networks that cuts away much of the detail. At the same time, its tools find features
*  of neural structure that are near impossible to see without these features of the structure. Some,
*  some scientists now believe can inspire new thoughts on the function of the nervous system.
*  So this is kind of a controversial idea, right? That, you know, we could say something about
*  function just from, well, modern these days, it's kind of a controversial idea that you could say
*  something or deduce some function just from structure. What say you? Yeah. So in some ways,
*  you know, the structure function relationship is kind of foundational to neuroscience and to biology.
*  Generally, there's a sense that like, we're just kind of going to look at physically what the
*  structures in the body are, and try to guess what they could be used for, you know, like you look
*  at the heart and like blood's coming out of it. It's like, okay, I guess that's the thing that makes
*  sure blood gets everywhere. So, you know, it can work to some extent to just look at the structure
*  of something. But yeah, I mean, there are, aside from the most basic kind of structure function
*  relationships, for example, Ramoni-Cajal, you know, finding that neurons tend to have little bits that
*  we now know are like dendrites that pick up signal and a long bit that's an axon that sends a signal
*  on. That was an example of looking at a structure and kind of deducing a function from it. But
*  other than that, well, he actually guessed the right, mostly guessed the right direction of
*  signal transport down the axon and dendrites accepting it, which just by looking at the
*  structure, like you said, just from drawings, essentially, which is pretty amazing. And so
*  with that, there was kind of, you know, in some sense, it formed the basis of how we believed we
*  would understand the brain is like, let's get the structure. Let's see what different neuron types
*  look like. Let's see how they connect to each other. Let's see what different brain regions look
*  like and where they are and all of that. But it does seem like in modern times, it's perhaps
*  acknowledged that that's not so easy to just look at the structure. And I mean, there are a lot of
*  efforts lately to get connectome data from different species and at different scales and all of that.
*  So you could argue maybe there's like, you know, people who still really buy into the structure
*  will tell us the function. But you could also just say that we need to know the structure to fully
*  understand the function, but the structure alone is not going to tell us the function. Because once
*  you move off the scale of a neuron or two or three, then deducing the function is very difficult.
*  But graph theory still gives you a way to talk about structure, at least. It doesn't say
*  necessarily that you can look at the structure and know the function, but at least gives you
*  different ways of describing structure than were perhaps stereotypically used in neuroscience.
*  Functions kind of build into graph theory as well, in a sense, right? Because of the,
*  depending on how you set it up, but it's not like you're just building an inert lattice when you're,
*  you know, creating a network with graph theory. The graph does stuff.
*  Yeah, especially if, so actually kind of similar to information theory, it's putting a lot of
*  emphasis on communication and the idea that where you have nodes, information will flow between those
*  brain regions or those neurons or something like that. And so yeah, in that sense, there's kind of
*  a built-in sense of function. Especially in the case of the brain, you're kind of thinking about
*  it as channels for communication to occur through. That's what the edges in the graph are, and then,
*  you know, the nodes are the different brain regions. So I would say that in some sense,
*  yes, it is, it's building in some belief about what the connections are for.
*  I have this crazy backward idea that it's almost a challenge to, you know, so I wonder what network
*  neuroscience and connectomics people think of this modern perspective as well actually doesn't matter
*  at all, right? Structure doesn't matter at all. It's about function. That's the, has the primary
*  explanatory role is function and structure is a very secondary thing. And I kind of take that
*  as a great challenge, right? Wouldn't it be interesting to be able to deduce function from
*  structure? I mean, maybe it's not possible, right? But, but gosh, what a challenge for someone to
*  undertake. Yeah, I mean, I'm, yeah, I'm struggling to say if it would ever really be possible, even.
*  Right. Like in theory. Well, no, well, no. I mean, of course, it's not possible to just look
*  at three nodes and say something about, right? But, but in theory, so like one extreme would be
*  you kind of have all of the physical information about the neurons and how they connect and you
*  just build that in a model and then you can look at the activity it produces and then say something
*  about the function. But that's just kind of studying the circuit itself then, which is what
*  the human brain project is criticized for. But yeah, the idea that you could really just kind of
*  like have a mathematical operation that you apply to a graph and it'll tell you the function of
*  that set of neurons, that feels not possible to me is what I would say. But at the same time,
*  I'm not sympathetic to the idea that structure doesn't matter and we only care about the function
*  just because that doesn't, that feels a little bit like it stops being neuroscience to me.
*  Like you could say like no physical detail of the brain matters. We just want to know like the mind,
*  we want to understand how inputs, the relationship between inputs and outputs, but we don't care
*  about how the brain creates that relationship. But if you're doing neuroscience and especially
*  like what got me interested in neuroscience was the idea that you could connect neurons in a certain
*  way such that they would produce a function. So if you really don't care at all about structure,
*  you might not be doing neuroscience, I think. You know, I really have enjoyed the past couple
*  years of thinking of things like structure as constraint and that sounds like, oh, that makes
*  structure boring, but I've elevated constraint in my mind as in importance because it's only
*  through the constraints that things like information processing can flow, right? And so the constraints
*  really do shape how the information, let's say the information again, how signals flow essentially.
*  So I think that might be the way to go is thinking about it in terms not of some positive,
*  when you have the structure laid out this way, it will create the function, but as an important
*  player as a constraint on how that can be carried out. Yeah, and again, you know, neuroscience being
*  a subfield of biology, there could be interesting developmental reasons why you have to have certain
*  structural constraints. Like maybe you couldn't build a network with a certain, you know, structure
*  to it based on how the brain develops and that kind of thing. So yeah, you can care about
*  abstract ideas of function and even somewhat abstract ideas about structure, maybe if you're
*  just interested in information processing more generally and artificial intelligence and that
*  kind of thing. But if you're interested in the brain and neuroscience as a field of biology that
*  it is, then yeah, it just seems like you'd be interested in the actual structure and how
*  the function arises from that. Speaking of idolizing people, Eve Marder. I think a lot of people
*  rightly probably idolize her work and, you know, her as a scientist. What I want to ask you is,
*  you know, how has Marder's work on the lobster, what is it, somatoganglion cells? Am I saying
*  that right? I'm not sure. The gut lobster networks and how they are basically vastly,
*  multiply realizable, the function is multiply realizable among a pretty simple set of known
*  connections among neurons. You can probably more elegantly describe that than I just did, but
*  you talk, you give that story in the book and talk about her work. How has that affected,
*  you know, your own thinking about brains and minds and how should it affect our thinking about brains
*  and minds? Well, I think for one, it's just a great example of the utility of mathematical models
*  because when you build those models and you see how this, like by the standards of biology and
*  neuroscience, a rather stereotyped set of neurons with a rather stereotyped set of connections,
*  how really the exact parameter that regime that you're in matters. Like if you change the
*  connection strength between certain neurons by a little bit or through neuromodulation, change some
*  of the properties of the network, it produces a different function. It produces different rhythmic
*  outputs. And so it just really shows that the quantifying things matters. You can't just say
*  that neuron is connected to that neuron and therefore I can deduce the function because
*  it's so reliant on the exact details of all of that. And then another just interesting
*  outcome of that kind of work is kind of a cautionary tale about averaging across,
*  certainly across different species, but even across different individual organisms in a species
*  because part of what she shows is that this network needs to produce these rhythmic outputs
*  for the gut and you can produce the correct rhythmic output many different ways. This
*  network can be wired up in different ways and still get the right function done for the animal.
*  And it will vary between individuals of the species. And so now we just assume, okay,
*  if all of these animals are doing the same behavior, they're using the same neural activity
*  and neural structures to do it so we can collapse across these different individuals that we're
*  studying. We can even collapse across slightly different species and all of that. But if her
*  work is more generally true, which it seems like there's good reason to believe that it is,
*  then you can really lead yourself astray by averaging because you can have systems that
*  are producing the same output but potentially with kind of opposite mechanisms, so to speak.
*  And the average of those different individuals won't actually work to produce the right output.
*  And so if your model is based on averages, you might be trying to solve an impossible problem,
*  even though you know, like, well, I know the animal is producing this output and I know this
*  is the neural activity, but if you're just piecing it together the wrong way because you're averaging,
*  then you're in trouble. Yeah, Mark Humphries talks about this. I just I heard, just the other day,
*  there's a lecture on Russian history. He was, and I think that this is an old idea. I don't
*  think he invented it, but if your head is in the refrigerator and your feet are in the oven,
*  on average, you're just the right temperature. Yeah. And this is the cautionary tale. I mean,
*  the martyr work too, you said, you know, presumably it kind of scales up to, you know,
*  to other areas. And one can imagine because the somatosensory somatogastric system of the lobster
*  is really a simple structure. So if you have that much diversity, that much, I don't say,
*  people mean different things by multiple realizability, but that much array of being
*  able to implement a function with different implementational implementation, you know,
*  imagine it scaling up to the, you know, the complexity of some of our higher cognitive
*  functions and how those get done. I mean, it's just mind blowing. Sorry, no pun intended. But
*  this, I have this weird, you know, none of, when you kind of like imagine these things like in your
*  head and you have a visual image, the brain is just, it seems like right now in my head,
*  it's such a beautiful solution to just fit any function it needs to fit, right? It's like
*  evolution's best solution, really fucking good solution to just fit anything it needs to.
*  Yeah. I think the, the, one of the other interesting kind of takeaways from Eve's work
*  though is that you can get at the fact that different systems are kind of coming to the
*  same conclusion in different ways, just by pushing the system to certain extremes.
*  So in her case, it's like changing the temperature within the normal range of the lobster's
*  temperature, two different systems, the two different animals can produce the same outputs
*  using different connectivity. But once you push it out of that range, then they start to kind of
*  break down in unique ways based on the different connectivity. And so that's like a little bit
*  reassuring that it's not that, you know, there's really no sign that the underlying structure is
*  different. You can probe differences and, you know, in kind of psychophysics and psychology and stuff,
*  people study the way that people make errors as a more interesting way to get at function and,
*  you know, potentially try to make guesses about the underlying structure, because errors kind of
*  tell you there's more ways to be wrong than there is to be right in most tasks. So errors can be a
*  little bit more revealing, or, you know, in the case of the lobster, pushing it out of its normal
*  operating regime is a little bit more interesting for revealing what's going on. Yeah, that's
*  interesting. I mean, you know, another way to think about it, just going back to constraint is
*  that the environment imposes its own constraints sort of of how the system operates. So, yay,
*  constraints, again, I'd say. Yeah. All right. So drum roll, we need a drum roll. Maybe I'll add a
*  drum roll in the editing here. The last chapter in your book, you close on talking about unified
*  theories of the brain. So speaking of physics, right now, there's a lot of hoopla in the physics
*  world about having a theory is theories of everything right is kind of popular among all
*  the physics big wigs these days. I think it's been that way for a while is my understanding.
*  Physics is long. So I don't know what these days means. Of course, you know, of course, you know,
*  what kind of person was Newton, Grace? So we actually we know a lot about that. But at least,
*  you know, I don't know, I see it more in the media these days. And there's a there's backlash also
*  from Sabine Hofstadter. Yeah, I don't know, has, you know, talked about how ridiculous it is that
*  we need a theory of everything. So you cover three, the three major three of the major theories of
*  unified theories of the brain, integrated information theory, the 1000 brains theory
*  from Jeff Hawkins, which I was surprised that that was included as one of them, and free energy
*  principle, which I was not surprised that was included. You know what, I have one more quote,
*  I'll read this quote from the book. Sociologist, this is a quote in a quote. Sociologist Murray S.
*  Davis offered a reflection on theories. In his 1971 article entitled, that's interesting.
*  In it, he said, it has long been thought that a theorist is considered great because his theories
*  are true. But this is false. A theorist is considered great, not because his or her, I'll
*  add her theories are true, but because they are interesting. In fact, the truth of a theory has
*  very little to do with its impact for a theory can continue to be found interesting, even though
*  its truth is disputed, even refuted. And then you're going to say grand unified theories of the
*  brains of grand unified theories of the brain, whatever their truth may be, are surely interesting.
*  So this is a great, you know, way to end your book. So, but why did you choose those three
*  theories to illustrate? And do you have a favorite among those? Yeah, so this, this was a difficult
*  chapter to write. I kind of- Was this the most difficult?
*  In some ways, yes, in terms of, you know, wanting to give an accurate perception of how the field
*  views these and how people who are supporters of it view them and all of that. So kind of socially,
*  the most difficult chapter to write. I had it in the book proposal because it's definitely an area
*  where physics has influenced the study of the brain because it's kind of imported this idea of
*  you can come up with a grand unified theory is kind of imported from physics. And I remember the
*  editor when he was like assessing my book proposal, like particularly noted like, oh, that seems like
*  a fun way to end the book. And then so I knew like, I knew I was like, I can't, I can't cut it. I have
*  to actually do this. Yeah. Yeah. So it took me a while to decide which ones to include and to kind
*  of crowdsource what options there even were for like what people consider grand unified theories
*  and all of that. And to be honest, the IIT, the integrated information theory is like, in some
*  sense, not a grand unified theory of the brain because it's mainly about consciousness in
*  particular, but consciousness is like so relevant for some people's understanding of the brain and
*  their interest in the brain at all that it feels like it is trying to encompass a lot by coming up
*  with a theory of that. So yeah, it was, it was very hard. And part of my decision was based kind of,
*  again, on this notion, not necessarily of like, what's the best, but what has been most impactful,
*  like what have people talked about that felt like it was relevant to explain and contextualize the
*  things that people were maybe already slightly aware of, or might hear about more broadly. This
*  seemed like an opportunity to kind of provide more information in those areas, which is part of the
*  decision for how I decided which ones to cover. It is interesting. I just realized, as you're
*  saying, talking about integrated information theory that Jeff Hawkins and 1000s brain theory,
*  1000 brains theory, he's one of those people who is against studying consciousness, basically,
*  because there's a lot more things to worry about. I mean, he talks about it in his book,
*  which I've skimmed already, because it's basically a summary of his recent papers.
*  But free energy principle does talk, you know, does deal more with consciousness as well.
*  Can I give you a challenge? What if I made you in one sentence,
*  summarize each of those take homes? You just shrugged. I just saw your whole body go like,
*  oh no. It's an impossible task, I know. But just to give listeners an idea, just a taste. And,
*  you know, when they read the book, they can dive deeper into all three of these ideas.
*  So just like summarize what the ideas are. Yeah, kind of the overarching principle behind each.
*  So free energy principle, a big focus of it is this idea of wanting to essentially minimize
*  surprise, and that that could drive a lot of how the perceptual system is organized, and how actions
*  are chosen, and all kinds of other things as well, because it can be applied kind of on multiple
*  scales. So that would be the free energy principle. Integrated information theory says that
*  consciousness arises when information is integrated in a certain way. So it focuses kind of on the
*  structures basically of, you know, pathways for information to interact with other sources of
*  information. And if you have the right structure, it says that consciousness, which is like a scalar
*  value of some sort, you know, you can have a little bit or a lot, but it tells you, yeah,
*  how much consciousness you'll get based on how much information is integrated. And then thousand
*  brains, which is kind of the new name for Hawkins approach. That one is a little bit harder to
*  explain succinctly just because it pulls from kind of other concepts in neuroscience about how,
*  like, space is represented in the brain, and that if you can get a good, I guess maybe one simple way
*  to put it is kind of if you can get a good spatial representation of something, you can do a lot with
*  that, is maybe what I would say, which is how it can be related to a lot of different topic areas.
*  – And the thousand part of that phrase, thousand brains, is just that we basically have tons and
*  tons of copies of all sorts of objects in our head with those spatial relations, and getting
*  that way we can get a grasp of different sizes of things, and the coffee cup is the
*  famous example that he uses. Do you have a favorite, not just among those, but do you
*  have, and you don't even have to bite here, but do you have like a grand unified theory, the brain
*  that you lean toward? – I am in the camp, which I talk about in the book, of people who don't really
*  believe that there will be a grand unified theory of the brain. So that was also kind of what made
*  it hard to write the chapter. But I did think it was important to both cover the fact that these
*  exist, and they are mathematical theories, the ones that I'm covering, there's a computational
*  mathematical element to it, so both that these exist, but also I tried to get across the fact
*  that there actually is a lot of skepticism from people in the field about them, even though they
*  seem like they could solve everything. Just a lot of everyday neuroscientists don't feel
*  that enthusiasm about them. – That's right. So you've been blogging for quite some time,
*  you've had a successful blog, and so you know how to tell a story, and you know how that comes
*  through in the book, but is there anything through the writing process, even with the book, but also
*  blogging, that has changed the way or helped develop the way you make even presentations,
*  or write research papers, or write grants? In your day-to-day research, has it affected that at all?
*  – Yeah, for sure. I think I've just developed a lot of sympathy for the reader, because when you…
*  – Something I don't worry about on the podcast is sympathy for the listener. So I don't know what
*  you're speaking to emptiness here, but go ahead. – No, because when you're writing popular science,
*  it's supposed to be fun. Someone is purchasing this book or whatever, even listening to podcasts or
*  visiting websites, whatever it is, they're probably doing it in their off time. So I feel like you
*  should provide them a pleasant experience. Yes, you want to get certain information across, but
*  it should be the case that if you put in enough effort that you can get it across in a way where
*  it's consistently still fun to read. There isn't several pages straight of just like,
*  here's the background knowledge, I'm just going to dump on you so that you can understand other
*  stuff I want to tell you. Every part of it should hopefully be fun and shouldn't be so challenging
*  that they have to reread the same thing three times or five times or whatever. So I think that
*  that's very important for popular science because it is recreational for most people.
*  Then it's like, well, why shouldn't people also not be angry when they're reading your scientific
*  paper? That should also be a smooth process for them, especially if you want them to keep going.
*  It's like, yes, technically you have to put in more details and you have to be more concrete in
*  a way that does make pleasant writing challenging because you just have to dump numbers and very
*  basic things about the methods on them. There's always a lot of caveats, but
*  ideally you just have it flow in a way that even though you're doing all of that, it's still not so
*  unpleasant because we're just people choosing how to spend our time. You want to make it
*  pleasant for people and they'll make them want to read your stuff more. It'll make them understand
*  it so they can build on it. If they can't understand it or if it just would take them three
*  weeks to understand it, then they're probably not going to do it because everybody's busy.
*  What do you think though about, I think it's Newton's Principia and there are other examples
*  of this that aren't coming to mind, where the author intentionally is obtuse, like writes,
*  sometimes even in code so that people won't scoop them and that makes, well, and for whatever various
*  reasons. That makes for some extremely unpleasant time spent trying to decipher what was meant.
*  Why is that a thing? I can't think of a good reason to do that that doesn't make it seem like
*  the person has a personality disorder. We're in science, so that's pretty, we're all interesting.
*  If you are famous, then people will spend that time on your cryptic text, but I don't know that
*  you're going to get famous by writing cryptic texts. I think it's kind of rude. Why are you
*  writing if you don't want people to understand it? I get really upset, even in a research paper.
*  Why are you writing? Why are you making this so difficult? Anyway, I know I'm not that bright,
*  but you got to meet me halfway. That's why. Also, scientists, you've probably been working on your
*  project for two years straight, and so you're really lacking an outside perspective of someone
*  who's going to swoop in because they saw it on Twitter and they just open it in a tab and then
*  it's just like, whoa, I don't know what's happening here. You really have to think about the context
*  in which people are coming to your work and what it will be like for them. I think that is an
*  amazing skill to develop and really difficult, and you've done it really well. Thank you and
*  congrats. Thanks for talking with me. Thank you so much. This is really fun.
*  Thank you for your support. See you next time.

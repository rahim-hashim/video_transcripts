---
Date Generated: April 19, 2024
Transcription Model: whisper medium 20231117
Length: 5746s
Video Keywords: []
Video Views: 880
Video Rating: None
---

# BI 173 Justin Wood: Origins of Visual Intelligence
**Brain Inspired:** [August 30, 2023](https://www.youtube.com/watch?v=acueIF-s0PQ)
*  But we realized that nobody had actually tested it directly whether a machine learning system,
*  given the same input as a newborn animal, would actually develop the same kinds of capacities.
*  So that was really our opening goal going in.
*  And I think we're going to have to start playing around with different artificial bodies the
*  same way we've been playing around with different artificial brains in order to have a chance
*  of closing this gap between animals and machines.
*  And my hope is this tells maybe AI researchers something important about critical periods,
*  right? So this is almost non-existent in the AI or ML world, but maybe there's something really
*  important about learning something and then having a critical or sensitive period and shutting it
*  down and having that serve as the foundation for the next stage of learning. This is Brain
*  Inspired. I'm Paul. My guest today is Justin Wood. Justin runs the Wood Lab at Indiana University,
*  and his lab's tagline is building newborn minds in virtual worlds. So what does that mean?
*  Basically what it means is Justin is comparing the very, very early development of natural
*  organisms to artificial agents. So he does this by using controlled rearing experiments in chicks
*  where he controls all of their experiences, in this case visual experiences, because a lot of
*  what Justin is interested in is understanding the origins of our visual intelligence and cognitive
*  abilities from birth and through development. He controls their visual experiences by placing them
*  as soon as they're born into these rearing areas in which all of the visual stimuli that's presented
*  to the newborn chicks are controlled by the researchers. So everything they're seeing is
*  controlled by the lab. And in tandem, Justin's lab builds models and AI agents that are trained on the
*  same visual data as the newborn chicks. As you might imagine, this enables Justin to probe the
*  nature versus nurture divide, or otherwise known as nativism versus empiricism. So we discussed that
*  debate, which Justin thinks of more as a both slash and kind of issue rather than an either or
*  issue. And using this setup, Justin has studied a number of the visual capabilities of newborn
*  chicks, things like view invariant recognition, which is more or less the ability to recognize
*  an object regardless of what orientation, what perspective you're taking on that object.
*  And for each of these visual capabilities, Justin can basically test, build an AI model and test
*  whether, given that same training data, the model is able to perform the tasks in the same way or
*  in different ways, or as well as or not as well as the newborn chicks. And a lot of the early
*  experiments that we talk about more in the episode, he was using convolutional neural networks,
*  which is a classical object recognition network. And we talked about what he found using those.
*  We go on to talk about, so he's taken this approach and expanded it and is beginning to
*  study other cognitive abilities. And in the future, he'll go on to study even more cognitive
*  abilities. But one of the lines of research that we talk about in this episode, he studied collective
*  behavior in artificial agents and in newborn chicks using convolutional neural networks
*  and deep reinforcement learning and an intrinsic curiosity reward function. Okay, so the general
*  theme here is what newborn chicks can and can't do, whether and how artificial systems can and
*  can't do those things, and what that tells us both about the natural chicks and how to build
*  systems that better emulate biological organisms. So it's a fun conversation. We hash all of this
*  out and more during the discussion. And Justin's enthusiasm, you'll see, really comes through.
*  Of course, I link to the papers that we discuss in the show notes and to Justin's lab. The show
*  notes are at braininspired.co slash podcast slash 173, where you can also learn how to support this
*  show through Patreon. If you value what I do here, you can send me enough to buy a cup of coffee every
*  month, or you can send me a little bit more and get the full episodes and or even join the discord
*  community, which is filled with like minded listeners like you. One last announcement here,
*  I'll be in Berlin, Germany in late September as part of a workshop that's associated with the
*  Bernstein or Bernstein conference in Berlin, Germany. That's actually September 26th and 27th.
*  The title of the workshop is How Can Machine Learning Be Used to Generate Insights and Theories
*  in Neuroscience? And actually, Justin would be a great person to participate in that workshop.
*  He's not going to be there. But there'll be a lot of great researchers that are there who are going
*  to give talks. And then at the end of this two day workshop, I'll be moderating a panel with a handful
*  of those researchers and discussing how can machine learning be used to generate insights
*  and theories in neuroscience. So if you want to learn more about that, I'll link to that in these
*  show notes. Again, that's braininspired.co slash podcast slash 173. You should register for that
*  workshop. It's going to be a lot of fun. It's going to be very interactive. And you should come say
*  hi to me if you do. That'd be fun. OK, thanks for listening and watching. Here's Justin.
*  Justin, you are studying bird brains these days, bird and artificial bird brains these days.
*  And we're going to talk all about your controlled rearing studies and what you've found out
*  with regard to natural and artificial intelligences. But I kind of want to go back to the beginning
*  and ask how you came to so I will have introduced a little bit the ideas of what you study in the
*  introduction. But what led you to this point of raising these chicks in highly restricted
*  virtual environments to compare them with artificial networks? Yeah, absolutely. So it's
*  been a winding path. So I actually started in graduate school working with young human babies.
*  So I always loved the origins questions. I always wanted to know what are the core drivers of
*  cognition and perception and action, right? What are the learning algorithms in newborn brains
*  that make it possible to learn object perception and navigation and make decisions and do all of
*  the amazing wonderful things that humans and animals do? And so I've kind of moved from
*  population to population and attempt to try to get in those questions. So I started with five and
*  six month old babies when I was in graduate school. And that, of course, got me introduced
*  to this idea of looking at what might be present in a young human brain. I started to realize that
*  and this will come up later when we talk about chicks, I believe. But I started to realize that
*  even though we were using young human infants, that's not the way to get at the nativism and
*  puricism question because of course, anything you find in a five month old or a one month old or
*  even a one week old could in principle be learned, right? So it becomes incredibly difficult to
*  distinguish between nativism and empiricism perspectives, right? Do we start out with
*  something like a domain general transformer, for example, when we're trying to model the brain?
*  Or do we really need to build in a collection of domain specific core knowledge systems,
*  for example? And that's how I was trained in graduate school. And so that's basically the,
*  I see that as one of the major debates in the field. It, of course, goes back thousands of
*  years to Aristotle and Plato, but we haven't really been able to get at it directly, right?
*  And so I'll go into why chicks is what I believe the only model system we can make a run at those
*  questions with. So anyway, yeah, so I went to babies, I then went to wild monkeys for several
*  years. So this was partly to escape cold Boston winters, but it was an absolutely wonderful
*  experience to go and work with wild monkeys. And I basically just compared what are the perceptual
*  and action perception abilities of monkeys and how do they compare with those of young babies?
*  And so I spent several years doing that kind of trying to find commonalities between the capacities
*  of non-human animals and animals. And given the monkeys lack culture and language and all these
*  uniquely human trappings, it was an interesting way to look for dissociations between particular
*  cognitive capacities and culture, language, and so on. So I did that for several years. And then
*  when I started up my own lab, I dove straight into newborn chicks. So during grad, yeah,
*  I'll pause for a second. Yeah. Well, yeah. But so did you just have an epiphany that you needed to
*  study the chicks or was this always eating at you this nativism and periodism debate and how
*  maybe the wild monkeys that you're studying and the human infants just you couldn't really
*  get to what you wanted to study? Is that did you have an epiphany over a coffee one day or
*  had this been the idea for a long time? The chicks? Yeah, it was a great question.
*  It actually started. I remember exactly when it started. It was in my with my first meeting
*  with my one of my graduate advisors, Elizabeth Spelke. And I remember sitting across from her
*  and mentioning that these were the questions I absolutely cared about. And we just started
*  talking about chick research and she then inundated researchers in the lab and grad students
*  in the lab with this is perhaps the one model system we can use because we can control everything
*  they do from the very moment of hatching, control their experience and then see what are the causal
*  roles of experience in terms of shaping perception, cognition and action. So I had wanted to do it
*  from the very beginning of graduate school. And then when I finally had the freedom with my own
*  lab to do so, I basically just started figuring out how do we study newborn chicks precisely.
*  That was really the kind of the big gap in the field is that there had been studies with newborn
*  chicks for, you know, really for decades, but the data was had a low signal to noise ratio.
*  And, you know, this is kind of one thing coming up in the reverse engineering enterprise is you
*  really need high quality data to ask, you know, does my machine that I just grew in a virtual
*  environment, does that actually map onto one of the target systems that I care about, namely an
*  individual chick? And if your individual chicks are across the board in terms of the measurement
*  space, then you might have a model that performs a chance levels and it'll still match up to one of
*  those chicks, right? So you can't have a huge amount of variation in your target population
*  if you really want to try to do this direct mapping between how does an animal learn and
*  how does a machine learn. So the first five years of my career were really spent just trying to
*  figure out how to automate the whole process. So, you know, making it so we could record 24-7,
*  we could give newborn animals thousands of trials that lasted, you know, 20 minutes at a time or
*  40 minutes at a time and really collect these detailed measurements of how newborn animals are
*  learning as a function of particular experiences. And then once we did that part, we then had the
*  data that we needed in order to start reverse engineering. And so that started to happen around
*  2015, 2016 when we really jumped into the AI world. Okay, that was going to be my next question
*  also, but maybe even before that. So I'd love for you to just describe the process on the natural
*  side, you know, from when you from the chicken, I don't know if it's from hatching and like just
*  what happens from that point, you know, to them living in these, you know, incubators in these
*  systems of these virtual worlds. But before that, is it do we like chicks because as they're
*  developing in the egg, so if you, you know, a human in the womb can be said to be learning in
*  the womb because it hears mom's voice, singing songs and, you know, yelling at dad and stuff.
*  And but chicks, is it just that, you know, they have less and less opportunity to quote unquote
*  learn in the in the egg relative to mammals in the womb, etc. That's that's, I would say that's
*  part of it, right? We have more access to their prenatal development. So if it does turn out,
*  and this is one of our working hypotheses in the lab, if it does turn out that prenatal training
*  data really matters for building a brain so that it then reveals, so to speak, innate knowledge at
*  the birth state or the hatching state, then we really need to be able to study that prenatal
*  developmental process. And ideally, of course, put AI through the same kind of training data,
*  right? So this is one thing we're doing in the lab is we're training artificial neural networks
*  with retinal waves and other kinds of prenatal experiences that we think occur prenatally.
*  And then we can ask, you know, if you have been trained on retinal waves and muscle twitches and
*  all the things happening to an animal prenatally, do you end up with something that seems a little
*  bit closer to how biological intelligence works in the newborn state than what we currently have
*  with machines? And I really think we're going to need to dig into that prenatal state in order
*  in order to be able to tackle it. But that's not actually the reason we switched to chicks.
*  The main reason we switched to chicks is they're the only animal in the world, at least to my
*  knowledge, that you can raise in virtual reality. And you might ask, of course, you know, fully 24
*  7 in virtual reality, right? So you can you can we hatch chicks in darkness. We then put on night
*  vision goggles when they're hatching. And then we move the animals in complete darkness from their
*  incubator over to their controlled rearing chambers, these virtual reality chambers,
*  and then we flip on the chambers and thereby giving us full control over everything they see,
*  right? So every object they see super, sorry, super naive question, though, does I don't even
*  know with chicks, do moms lay on the eggs for a while? Do the hens lay on the like, you know,
*  when do you start handling it? And this doesn't matter. Yeah, yeah, no, it might matter. We don't
*  know what matters. That's one of the main models of the lab is we don't know what matters, right?
*  In terms of the models, in terms of the environment, in terms of the experience,
*  so it's all open. We just need to be empirical about it. But yeah, in the in the wild, a mother
*  hen will roll the egg once in a while. So they'll turn the egg so that it ends up developing
*  correctly. We use an automated incubator to do that. So it basically just rotates the eggs every
*  45 minutes. And so it basically replicates the kind of rearing conditions that roughly that animals
*  are getting in the wild. And then, of course, once the virtual reality part starts, then it's a very
*  different kind of experience than what they get in the wild. Yeah. Yeah. Okay. All right. So
*  you bring them over in darkness with the night goggles on, you place them in the virtual
*  environment. And then and then what happens then? Then what's the yeah. And then so we just we
*  basically just let them do what they will do. So we program the virtual world. So we rely on
*  imprinting, at least in our early experiments. So imprinting, I imagine many of your, you know,
*  much of your audience might be aware of this. But imprinting is basically just an early social
*  preference that you develop in life. So it's feel imprinting is the most well known of this,
*  just because it was studied, you know, notice back in the 19 or in the 1500s, I think was the first
*  observation of imprinting, people would notice that baby birds would very quickly develop a
*  preference for for caregiver. And of course, Conrad Lorenz really popularized this as we see
*  those wonderful photos of of little geese following after Conrad Lorenz as he checks down a river.
*  And so, you know, this has been a well known phenomenon for a while. And so it ends up being
*  quite convenient for us, because we can essentially just put a virtual object in the chamber. So our
*  chambers are essentially just white walls, except for two of the walls right now, we're LCD monitors.
*  So we can import whatever kind of virtual stimuli we want into those virtual chambers. You know,
*  maybe you want to raise an animal with a single object, for example, and maybe that single object
*  is only seen from, you know, a single viewpoint range. So we can essentially vary the experiences
*  that the animal gets, and they'll imprint to that whatever that might happen to be. And then we can
*  change around the characteristics of that object and see if they think that it's still a mom.
*  Right. So I, you know, I know that this is mostly auditory, but you know, so I always like to look
*  for props. But you know, I imagine like holding a coffee cup, and you only get to see that coffee
*  cup from one perspective, you know, and the chick imprints to that coffee cup from one perspective,
*  what if you then show them the coffee cup from a different perspective that produces a different
*  image on their eyeball? Will those will they still recognize that object? So this is known as view
*  invariant object recognition. You can also do this with things like background invariant recognition,
*  right? You can put an object on a background and you can see if the chicks can recognize that object
*  across a different background. So we essentially went through a, you know, dozens, hundreds of
*  experiments asking how rapidly and quickly does high level vision emerge in newborn chicks? So
*  what do they need? What kinds of experiences do they need to develop view invariant recognition
*  and background invariant recognition and the ability to bind colors and shapes into integrated
*  representations and memory and, you know, things like object permanence and action recognition.
*  Those are kind of the main capacities we've been looking at so far. And I think, you know,
*  what's really surprised me at least is how fast, how little chicks need to learn these high level
*  abilities. So even a single snapshot of an object, right, just a single object just being flashed
*  over and over again from one viewpoint is sufficient for a newborn animal to be able to
*  recognize that object across a wide variety of other viewpoints. Which at the beginning
*  almost seemed like magic to me, right? Like how on earth would an animal be able to recognize a
*  three-dimensional object having seen no other objects in their lifetime from other viewpoints?
*  How might that capacity emerge? And so that of course is where the AI comes in is because it
*  can actually give you an answer to that question if it turns out that the AI system's doing the
*  same thing that the chick is doing. It takes us beyond nativism magic, so to speak, right? This
*  has always been a problem is you can say something's innate, but the explanation was always a little bit
*  like magic, right? Like, well, it exists. We have no idea how or no idea why, but that ability exists
*  in the newborn state. So we're really trying to figure out mechanistically why that's the case.
*  So you said you were surprised, but what would, what did you think would have happened? I mean,
*  because you had already studied the innate or the cognitive skills of newborns for a long time.
*  Did it really surprise you or was that your hypothesis going in?
*  It actually really surprised me. And I think I had been influenced by machine learning
*  experiments, right? So these were these experiments where you dump in tons and tons of data,
*  of course, into CNNs or transformers. And you find that typically they needed, or this was at least
*  the wisdom back then, is you needed a huge amount of data, right? A huge visual diet in order to
*  start breaking into this problem of recognizing objects from different viewpoints. Given that
*  that was the one learning system that existed, that was actually replicating this, I guess,
*  this capacity of you and variant background and variant recognition, that was my starting
*  point as a hypothesis is maybe chicks are something like these machine learning systems,
*  maybe in the first couple of days of life, you know, you still could see in principle,
*  hundreds of objects wandering around the natural world as you see mom, you know, mother hen, and
*  you see mother hen moving across backgrounds, you see her from a whole bunch of different
*  viewpoints. And then you see your grazing field in the barn, right? Within one day, you could acquire
*  a massive amount of experience about the world. And so I thought that maybe that massive amount
*  of experience might be necessary or might be required. And as it turns out, it's not, right?
*  It just requires this little bit of data. And from that little bit of data, you end up getting
*  these high level abilities emerging. See, I kind of had it in my mind because you had done
*  a bunch of these studies in the early 2010s, right? And I suppose a little bit before that as well,
*  maybe I had it in mind that you had the idea of how the newborns would acquire these skills.
*  And then kind of with the rise of convolutional neural networks and these artificial intelligent
*  networks, then you thought, oh, well, now I have something to compare it to, but maybe I have it
*  backwards. So did you have the models in mind when you were developing the experiments?
*  Yeah, they really kind of happen side by side with one another. I mean, so back when we started this
*  work with Chicks, it was 2010, which is of course before AlexNet. And so the computer vision systems
*  on sort of on the market weren't nearly as sophisticated as they were. But I still remember
*  some early James DiCarlo papers, especially one that he wrote with David Cox. It was a
*  trends in cognitive science paper called Entangling Object Recognition. And I remember reading that
*  paper like 10 times, just trying to transform my brain from more of a nativist way of thinking.
*  It's just something is there, but no understanding of the mechanisms. And I just remember reading
*  that paper over and over and just trying to understand what it means to think about the
*  brain mechanistically as a series of transformations across a series of layers. And that paper just
*  completely transformed the direction or the arc of my research. And then I got very interested in AI.
*  I was of course quite excited when AlexNet came out and then just kind of waiting with bated breath
*  until an unsupervised model would come out. Because of course Chicks don't learn through
*  supervised learning. So we needed to wait till things like SimClear and then these other
*  unsupervised models came out till we could really make that detailed comparison. But yeah, a lot of
*  my career has just been waiting around for AI to come up with an algorithm that would somehow learn
*  in an unsupervised manner. And that happened about 2020 with SimClear. And now Transformers,
*  I think, are the next stage of that. There are these kind of full blown embodied models that can
*  handle high dimensional action spaces and have very few inductive biases and nevertheless can
*  learn these amazing capacities. So yeah, it's quite fun right now, especially with AI providing
*  the models that we then plug into the artificial animals and see does the Transformer or does the
*  CNN actually end up learning like the actual animal itself? Yeah. Okay. Well, so the first
*  AI models comparisons that you made, as far as I know, were with convolutional neural networks.
*  And you tested different types out. But then you've gone on to look at, and we'll talk about
*  all this, to look at collective behavior. And in that you implemented the same kind of convolutional
*  neural network as a model, but also a reinforcement learning agent with curiosity and intrinsic
*  motivation. And so are you transitioning to Transformers now? It's like the latest and
*  greatest. You just plug it in and... Absolutely. Yeah. Transformers, I think, are fascinating,
*  especially from... Well, for many reasons, but especially from a developmental psychology
*  point of view, because they have such minimal inductive biases. And this has always been the
*  debate, right? Is, do you need strong inductive biases to make learning possible? And nativists
*  have kind of come into the game with this, I think, strong assumption that training data is
*  sparse, noisy, and impoverished. You'll see this all over the place, right? Going all the way back
*  to William James is this basic assumption that the training data, the proximal images we receive,
*  just aren't good enough for learning. But I think AI is giving us a completely different story of
*  this, right? So for example, Transformers, if you do things like masking procedures, you can mask out
*  90% of the content. And yet that's when these models learn the best. And so what that tells
*  us is that these models act, that the training data is highly redundant, it's highly structured.
*  And so if you have a powerful enough domain general learning mechanism, at least in principle,
*  it's possible to be able to leverage that structure and redundancy in the data to be able to learn a
*  good visual model of the world. Maybe you like what objects are and what the world is like,
*  what space is like, so you can navigate in all these, of course, critical capacities we need to
*  learn. So Transformers, kind of said differently, are, I think, a good scientific model because
*  they're so relaxed in terms of their inductive biases. And they let us test this very strong,
*  extreme hypothesis, which is that maybe most or all of intelligence emerges from a domain
*  general system, right? This would have been an empiricist. This is what empiricists have been
*  arguing for a while. It lets us test that very, very strong hypothesis. But to be fair to nativists,
*  I want to say I'm agnostic about nativism versus empiricism.
*  Oh, I was about to ask that. But my next question, but how did you used to be more nativist? And now
*  you're in the where, like, how did that evolve? I've switched back and forth like five times in
*  my career. So and I realized the reason why is because nativists and empiricists often look at
*  different evidence in order to support their theories. So I kind of got to be trained by
*  nativists at one point during graduate school and now I'm at Indiana, yeah, by Spelke and Carey.
*  And now I'm at Indiana University with Linda Smith and a whole bunch of wonderful people here who are
*  kind of more on the empiricist side of things. And it just seems really clear. They're just picking
*  they just pick different kinds of phenomenon to support their claims. And this is fine,
*  of course, but I actually think both ideas are going to be right. And so let me just kind of
*  specify that just so I don't, nobody comes away thinking I'm an empiricist or a nativist. I really
*  think both ideas are right. Right. So you could have a single domain general mechanism. That's
*  then that might be something like the starting point of prenatal development. But you might
*  imagine that prenatal training data is so rich with these retinal waves that are very object like
*  and have these important second order correlations just like natural data. You might imagine that at
*  the birth state, you really do have something like core knowledge. Right. And then that would
*  mean the nativists on some level were right to suggest that at the birth state or the hatching
*  state, you would see something like object knowledge, like object permanence or view
*  invariant recognition or the capacity to navigate and take novel paths between places. So I really
*  think the idea of core knowledge phenomenon might be right if we take training data seriously during
*  prenatal development. So right in a way we've got the nativist being right, because maybe core
*  knowledge does exist. It is present. It is a phenomenon in the first maybe days or weeks of life.
*  But that might all emerge from a domain general mechanism, which would make the
*  empiricist right. Right. So this is kind of my hope of getting past this debate is we want to
*  build a test bed where people can just test it one way or the other. So this is what we're doing
*  with all of our chick work is essentially trying to build a public test bed where researchers around
*  the world can just plug their brains into our artificial chicks, whether they're a nativist,
*  whether it's a nativist theory or an empiricist theory and just run the model across the range
*  of experiments that we've done and see if it's a good match. Right. And then we can just test a
*  bunch of nativist theories. We can test a bunch of empiricist theories and we can see just see which
*  one ends up being the best match for what chicks are actually doing. So I love this idea in computer
*  science of making public benchmarks so everybody can plug in their models. So a grad student has
*  exactly the same chance of coming up with the right model as a full professor. Right. That's
*  how it should be, I think, in a good science. So. Right. Yeah. But so we haven't really talked about
*  how your experimental setup is fully automated and why that's an important thing. And I know
*  that you worked really hard on the technical side to get all this right. And now you have
*  how many rigs? Thirty thousand. How many do you have? Like what? Twenty something like 20 or?
*  We actually had. So we had 60 rigs back at USC. Yeah. So this was we could run about eight
*  experiments at a time, you know, each with multiple subjects in it. And we were able to collect a
*  massive amount of data very quickly. And critically, it wasn't just a lot of data. It was also very
*  precise data so we can make precise predictions for each individual subject rather than relying
*  on inferential statistics. And we can kind of maybe come back to this. I think this is there's
*  right. Right now, I think there's a lot of interest in bringing psychology into the A.I. world. But,
*  you know, psychologists have largely relied on inferential uncertainty, whereas, you know,
*  researchers in A.I. care about productivity, how well you can predict things. And those are
*  completely different from one another. And you can show that you might have the smallest p value
*  you could ever want to get something published, but it doesn't produce the kind of benchmarks
*  you need for machine learning. Right. That the data might be too variable to actually serve as a good
*  benchmark. So that was really like, again, the first step of automation is how can we get a good
*  benchmark so that, you know, the cloud of chick, you know, the cloud of dots representing the
*  individual individual chicks is actually separate across conditions. So it's really easy to see if
*  your machine is more like one or more like the other. OK, should we talk a little bit about the
*  early convolutional neural network experiments? And this is kind of serves as background for the
*  rest of your experiments. And it sounds also like you'll have experiments for the next 100 or so
*  years lined up because there's so much that you can do. That's the hope. That's the hope. And the
*  hope is, you know, we're building these new VR chambers, too. So this might come at the end,
*  but we're building these new VR chambers that are full on VR. So we have a camera that basically
*  monitors the chick as they're moving and that they're surrounded by all four screens, almost
*  like the cave, the human cave VR system where you move around in the walls update. So we built
*  this for chicks. Wonderful graduate student in my lab named Josh McGraw is working on this.
*  And it essentially allows us to raise chicks in any kind of world you can imagine. Right. So a
*  world where object permanence is true or false or a world where objects don't obey their boundedness
*  or their shape as they move through time and space. So you can really give animals these kinds of
*  strange, unnatural experiences and really kind of make a run at these questions. You know,
*  is it built in knowledge of object permanence, for example, or is it learned based on seeing
*  objects disappear and reappear from view? Hmm. Yeah. Okay. Well, yeah, let's start with this
*  convolutional neural network experiments. And maybe, I don't know if you want to end up,
*  I won't. Well, before that, actually, you had shown that there are two properties that are
*  really important for chicks to learn things like object invariance. And that is that the objects
*  that you're showing them need to vary smoothly and slowly, which is quite interesting. And I
*  think we'll keep coming back to this nativist versus empiricist sheen because, you know,
*  all these, because, you know, I have a bunch of questions like, well, what does that mean early on?
*  And so anyway, but if the objects are moving fast, and if they're like kind of jutting around so
*  that you don't get a smooth transition, then the chicks don't learn the objects as you're showing
*  them. That's exactly right. Yeah. So, you know, 10 minutes ago, I mentioned all of the amazing
*  capacities of chicks, right? So from a very little bit of training data, they can do a whole bunch,
*  right? They can recognize objects across novel views and backgrounds and so on. But as it turns
*  out, the way that they do that is through heavy constraints on learning. And these two heavy
*  constraints appear to be slowness and smoothness. So if an object is not moving, you know, slowly
*  over time, then essentially what the chick builds is this kind of, it's like an abnormal object
*  representation in which action information is part of the shape representation. So they really
*  care about how that object moves. They don't particularly care about what that object is.
*  And what I really loved about these experiments is you can basically causally manipulate the first
*  representation an animal makes. So if you make the object move slowly, they build these beautiful
*  view invariant representations. If you speed up the object a little bit, all of a sudden you start
*  pushing it into an action representation. And so, you know, this, to my knowledge, is kind of the
*  first way where we had like strict causal control of manipulate this experience, and it will directly
*  impact the nature of the visual perception that emerges in the animal. So this is really exciting
*  because, you know, these are the kinds of constraints I think we need to really understand
*  what's under the hood, right? So we should expect whatever the learning algorithm is to show these
*  same constraints. A machine should be subject to the slowness and smoothness constraints the same
*  way that a newborn chick should if we've really figured it out, right? And if we haven't figured
*  it out, which we haven't yet, then we know that we have the wrong models, right? We know that there's
*  some other model out there that leverages time to a greater extent than current ML systems do,
*  and perhaps those should be the next systems we test. Yeah. So you want those constraints in a
*  system that you're building in order to learn about how we do it or how brains do it. But
*  if you're building, so thinking about those constraints, it is potentially limiting, and
*  maybe that's the price we pay for whatever quote unquote general intelligence that we have is like
*  we have these very narrow constraints, right? Like we only see a very narrow band of UV or of
*  electromagnetic radiation and of light, in other words. So how does that make you think about
*  our own intelligence? I know this is kind of a big question before we get into some of the details,
*  but does it make you think we're more narrowly intelligent or is that something necessary for
*  our wonderful general intelligence? This constraint of smoothness and slowness and
*  we can't keep track of things that are moving really fast, that sort of thing.
*  It's a great question. I mean, the natural world is slow and smooth, so for every animal not born
*  in our lab, they're good to go, right? They'll have all the right kind of training data they need.
*  They'll get, if you look around the room, most things aren't moving at all, right? So that's
*  what I mean by slowness and when something does move, it tends to attract your attention.
*  You fixate on it and then it's slow in terms of the proximal images hitting your eyeball because
*  you're actually following that object as it moves. So I think the natural world essentially provides
*  all, meets those constraints we need for high level learning. So I don't really think about
*  the brain as being highly constrained because of those unnatural constraints, so to speak.
*  Why we like those constraints is because they give us ways of distinguishing between candidate
*  models, right? So the fact that it's learned, the fact that experience seems to play a causal
*  role in developing view and variant shape representations, in other words, suggests that
*  that's not hard-coded into the brain, right? Chicks probably don't come into the world with
*  some sort of notion about what three-dimensional objects look like. Rather, our speculation is,
*  you know, chicks come into the world with something like a domain general learner and the
*  world is filled with objects and as long as those objects move in the right way, which is slow and
*  smooth, perhaps it needs to be that way because of, you know, temporal windows and spike timing
*  dependent plasticity. We don't know at this point, but that's our kind of working hypothesis.
*  As long as you have those basic requirements, then you can see learning happening pretty rapidly.
*  I don't know anything about chick saccades, rapid eye movements, like ballistic eye movements,
*  because the slow and smoothness doesn't jive well with the way that humans and other, you know,
*  primates move their eyes. And like every time you move your eyes, you have kind of a completely
*  different scene, which is not smooth, but the object itself might be moving smoothly, but your
*  perception from your eyes, from your vision, is not. And so we have to like compensate for that.
*  I don't know if you've, I just thought, oh yeah, I have a background in saccades. So this,
*  I have to think about this. Oh yeah, no, it's a great point. And actually, James DiCarlo has
*  done some wonderful work on this. So he did work with, I think this is 2008, the first talk that
*  was Lee, but basically he, they put monkeys in a natural world where when the monkey saccaded,
*  you would change something from like a tiger to a teacup. And what they found is that in IT,
*  you start seeing those tiger and teacup representations coming closer and closer together
*  as long as they're part of the same kind of temporal, they have that temporal continuity.
*  So I think this still works even with animals that make extensive eye movements. Chickens,
*  they have a little bit of eye movements, but mostly they just move their head instead of their eyes
*  in order to refresh their retino image. But I think the same general principles,
*  right, that's ultimately we're chasing is these general principles of learning. I think those
*  seem to be true from what we can tell across chicks and across monkeys. There's also some
*  really nice work by Linda Smith where she looked at young children, you put a camera on a child's
*  head and you ask, you know, how does that, what kind of data does that child acquire?
*  And one of my favorite findings that she has is that babies or toddlers make object data really
*  slow and smooth. So they'll pick up an object and they'll hold it completely still and they'll
*  still their head too, essentially making it so the retinal images going into their brain are
*  very slow and smooth. And when they rotate it, they'll rotate it again very consistently and
*  slowly, especially focusing on planar views. So even if we just look at the natural behavior
*  of young children as they're learning, they're actually spontaneously making data slow and smooth,
*  suggesting that maybe this really is a deep principle about visual learning and maybe
*  learning more generally is that you need slowness and smoothness, you know, maybe allowing the
*  temporal machinery of our brain to link up these time slices in the world into coherent representations.
*  Hmm. Okay. So you raise chicks in this virtual world and you're showing them one object,
*  you're imprinting them with one object, and then you test whether they're imprinted by showing that
*  same object on one side and a different object on the other side and how much time they spend
*  among these different objects is an indicator of whether the imprinting worked and whether they have
*  this type of whatever you're testing, object, view invariance, etc. And then you train a
*  convolutional neural network, but you take different types of convolutional neural networks that
*  have either been super massively trained on ImageNet, but thousands and thousands of images
*  to learn how to categorize those objects and a few different kinds of convolutional neural networks.
*  Could you just kind of talk us through that and then tell us what you found? And these are kind
*  of the early AI experiments, right? Yeah, absolutely. And we actually have a paper that
*  I think the paper I sent you as an archive 2021 paper. So we have a new paper working on that's
*  basically fleshing all of this out, looking at different architecture sizes. But basically kind
*  of long story short is that the goal of it was to ask, can we build an image computable model of a
*  newborn visual system? And if we can, we can then test, is it the case that machine learning systems
*  really are more data hungry than newborn brains, right? You see this claim everywhere. So it used
*  to be everywhere with CNNs is that, well, CNNs might be good models of the brain, but we know
*  they're trained on 14 million images from ImageNet. That's radically different than the visual diet of
*  a young child. Therefore, these aren't the same learning systems. But we realized that nobody had
*  actually tested it directly, whether a machine learning system, given the same input as a
*  newborn animal would actually develop the same kinds of capacity. So that was really our opening
*  goal going in. So what we did is we essentially, you can't put a camera on a chick's head, they're
*  too heavy. We actually tried this and it didn't work. But what you can do is you can simulate the
*  visual experiences of a chick in a video game engine. So you can essentially just yoke the
*  camera in a video game engine to the head of the chick. And then you can just move the agent,
*  you can just basically move the camera with the chick's movement and then collect all the
*  same visual images that the chick gets. And so, you know, we've done kind of versions of this with
*  more simple base agents. And what we find is that that's enough. The kinds of massive data
*  augmentation that you get when you get to look around the world and move around and select your
*  own viewpoints, that ends up being kind of the key missing piece necessary to build view and variant
*  recognition. So kind of said differently, even if you have a single object, I can move farther away
*  from that object, I can get really close to that object, I can look at it from the sides, right?
*  I can augment, I can do natural data augmentation the same way that engineers do, you know,
*  artificial data augmentation like color jitters and swapping. But, you know, an animal can actually
*  augment their data however they want. And so if you give CNNs that same kind of augmented data
*  from the environments of the chicks, they end up solving these view and variant problems.
*  So that was really the goal is to try to match the training data as closely as possible
*  between the animals and the machines. Because if you don't match the training data, you have no
*  idea what the problem is if there's a gap, right? So it might be like, let's say, you know, a machine
*  and a human are doing something different from one another. Well, one possibility is that maybe
*  it's the learning algorithm that's different. But another possibility is maybe it's the training data,
*  right? You have no way of knowing if it's the learning algorithm or the training data that's
*  leading to differences. So if you clamp down on training data, you can now make an inference that
*  if two things are different, it's likely, you know, either the body of the system or the learning
*  algorithm of the system. And of course, those should probably be treated as the same thing,
*  right? A body's in a brain's in a body. And that's a single learning system. So that was really our
*  goal there. And then we recently did a grad student my lab, Lili Pandy recently did this with
*  transformers where we thought, you know, maybe CNNs with their kind of beautiful hierarchical
*  structure would be able to learn from sparse data, but no way with transformers, right? They just
*  don't have the inductive biases to be able to do this. And as it turns out, you know, they perform
*  a little worse than chicks, maybe five to six percent or than CNNs, maybe five to six percent
*  worse than CNNs, but they still solve the task. So you can start with the most minimal inductive
*  bias we have in ML and machine learning. And you can just give it limited training data of a single
*  object from a, you know, from a limited viewpoint range and transformers will learn view invariant
*  representations. So I think this is really important because even transformers don't appear
*  to be more data hungry than newborn visual systems, right? This argument that you see in
*  every popular media story and almost every scientific paper about the data hungriest of
*  these systems. I mean, you know, we've just run one study so far, but it looks like from what we
*  can tell when you really equate their training data, it's not actually clear that one's more
*  data hungry than the other. Well, one of the interesting things about the CNN studies,
*  and you can tell me if this is true of the transformers as well, I had mentioned that
*  you tested it against also a CNN that was fully trained on ImageNet. And it turned out that that
*  CNN performed better than chicks and better, higher, was more accurate for object recognition
*  of view invariants than the chicks and also more accurate than the CNNs that were trained just on
*  the virtual world chick data. But the issue is that the CNNs that were trained just on the chick
*  data actually matched the chicks behavior better. It was a better indicator of their actual cognitive
*  ability. Exactly, exactly. And so I think kind of what you're suggesting is maybe, you know,
*  we see this really as a closed loop system, right? So you're never done just when you show that the
*  CNN matches the chick. The next experiment, of course, is then to, you know, put chicks in a
*  more natural environment, something a little bit, well, you can't do anything like ImageNet,
*  but you know, a much more natural environment, maybe you have dozens of objects virtually around
*  the animal, maybe they're 3D, so they change perspective as the animal moves. And then you
*  can ask how does that more fully trained chick compare to a CNN that's been trained on that data,
*  right? So you can continuously cycle around asking, you know, given that the animal required this
*  amount of training data, the same should be true of the machine. And then you can, for example,
*  generate new predictions with the machine and ask, does the animal actually match those predictions
*  that you just generated from your model, from your machine? And you continuously go around the cycle
*  until you close the gap between the animals and the machines. So, you know, I really don't think
*  this is sort of the end point. I really see it as the starting point of now we have a closed loop
*  system where animals and machines are connected with one another. There's no human in the loop
*  deciding what counts and what doesn't, what phenomenon we should care about and what we
*  shouldn't. It's just a completely automated system. And so now we can just basically go around this
*  closed loop system over the next, you know, hopefully several years and gradually close
*  the gap and vision and navigation and other areas that we look at. So do you have versions
*  of transformers that were fully trained and also performed outperformed the transformers that you
*  trained in a more realistic way? So we've mostly stepped away from ImageNet trained systems in our
*  newer papers just because it's not, I mean, it's interesting for an AI audience. Yeah.
*  Right. I mean, it's like, you know, ImageNet is such a weird visual diet anyway, right? So like
*  stat snapshots from the, you know, many of your prior guests have made this claim. So, but right,
*  it's such a weird visual diet to get, because you don't actually get to do what a child does,
*  which is, you know, pick up that object and look at it closely and move it around or interact with
*  that thing. And so, so we typically don't use ImageNet trained systems. We just train them from
*  scratch. So we'll just take an untrained system, give it the same training data as a chick that's
*  been simulated, you know, where new project is actually first we'll train it on retinal waves,
*  and then we'll train it on the visual diet of the chicks. So to ask if retinal waves give you an
*  extra bump in performance, so to speak. But yeah, we're really just focusing on matching the training
*  data at this point. So if you can get the same performance from a CNN and from a transformer,
*  is it just that cognition is just so multiply realizable that we're going to be able to
*  simulate visual development in 12 different ways? What does it tell us?
*  Yeah, yeah. So I think we're discovering, I think the field is discovering the answer to that
*  question right now. I certainly don't have an answer. I can, I can speculate, which is that,
*  of course, like anyone, but I think that there's something about this direct fit idea. This, this,
*  so this is something that came up from, you know, Meezan at Princeton that I think you
*  interviewed a couple years ago. This idea that, you know, maybe what brains are doing,
*  and we know that ML systems are doing this, but maybe what brains are doing is they're just
*  fitting to the space-time features of embodied data streams, right? So maybe they're just very,
*  very flexible and they fit to those data distributions. This might happen in a
*  purely unsupervised way, like predict what's going to happen next, like NLP systems or,
*  you know, masked autoencoders. But maybe, maybe just that fitting process is what we're,
*  what we see during development. And if that's the case, if it's just kind of a large scale
*  fitting process, then that, you know, shows us that it's not just that it's kind of multiple,
*  I mean, it suggests that as long as a system is fitting, whether it's brain or whether it's
*  silicon, whether, but as long as it's fitting with a lot of parameters, then we should perhaps see
*  the same kinds of capacities emerging, right? So another way of saying this is like, we want to
*  push the animals and the machines to the same part of this parameter space. And maybe that part of
*  the parameter space that you push towards is that is fitting to the data distribution, fitting to
*  the underlying data distribution. In which case the prediction I think we would see is that is,
*  that's a general principle of learning. And as long as you make a system fit to the underlying
*  data distribution through something as simple as prediction or masking or, you know, masking,
*  you know, we should, we should see these capacities emerging. So that, that would be my
*  speculation is that there's something really deeply right about fitting to underlying data
*  distributions. And given that we have 86 billion neurons connected to another thousand to 10,000
*  neurons, that's a lot of dials you can turn and tweak in order to fit to a high dimensional
*  data distribution. So that's kind of my working hypothesis about what's likely underlying
*  vision. But of course, you know, it's, it's just a guess, but it's empirically testable, right?
*  That's what transformers do, especially these ones that fit as we can see if that's actually
*  enough, right? How many neurons does a chick have? How many neurons does a chick have? Several
*  million. So it's a smaller system than humans nicely. I think humans are quite complex and
*  take a while to develop. But they have all the same kinds of cortical circuits and large scale
*  brain architectures as mammals. So this there's this old kind of myth that bird brains are
*  radically different than mammal brains. This comes from early observations in the 1950s,
*  you know, where researchers with, you know, very low precision techniques, you know, went into the
*  brains of mammals and birds and noticed, wow, nuclear versus layered organization, they look
*  totally different. Therefore, birds and mammals must be thinking in really different ways. But
*  the last 70, 80 years has shown us that that's wrong, right? I mean, the cortical circuits are
*  almost identical in terms of their input output connections. They're produced by homologous genes.
*  Our common ancestor was only 300 million years ago. And you can see that canonical cortical
*  circuit in both birds and mammals today. And you even see the same like large scale hub organization
*  with, you know, prefrontal and hippocampal and visual areas. And so, you know, I think I think
*  that, you know, especially as we're comparing animals to machines, I think the distance between
*  birds and mammals is actually quite small. And given that you can't raise mammals particularly
*  well in VR 24 seven, if you can do it at all, I think birds might be the one chance we've got as
*  scientists, at least to make a run at these questions of of of of nativism versus empiricism.
*  You mean birds and mammals is really small relative to birds and AI models?
*  Exactly. Is that exactly? Yeah. Yeah. That's what you had mentioned. You know. Yeah. Okay. Go ahead.
*  Sorry. Go ahead. Oh, no, I just was clarifying. That's exactly right. Yeah. Is that, you know,
*  we often make these comparisons between primates and CNNs or primates and transformers. And yet
*  a lot of researchers are a little bit reluctant to go to birds because primates have often been
*  the model system for object recognition. And so, you know, this is this is often the field kind of
*  getting into an attractor basin that might not necessarily be entirely healthy or might be getting
*  pushing us to become too specific in terms of what we're studying. My suggestion would be we need to
*  relax that attractor basin a little bit so that we can study other animals that might give us other
*  advantages that primates don't give us. So you can't raise a monkey in VR from birth. And yet
*  you can do this with a chick and really push around and see what experience the world experience
*  plays in developing knowledge. Well, so I was going to ask about, and we don't have to
*  perseverate on this, but I mean, you had mentioned that mammals develop their visual system and visual
*  intelligence develops more slowly, takes more time to mature. And I don't know if do birds have a
*  critical visual period like mammals do early on and or there's this whole pruning effect. There's,
*  you know, the brain, the brain is developing, making thousands, you know, millions of connections
*  per day or whatever in the first few weeks. And then there's this pruning back and that's part of
*  the process as well. And I don't know if that has, do you think about that? Or is that an issue with
*  chicks or do they not have such a pruning? And do they come out a little bit more hardwired?
*  They come out a little bit more hardwired. You know, it could still be coming from a domain
*  general mechanism, that hardwiredness, right? Because you could imagine domain general through
*  prenatal training data. Yeah. So I just want to clarify, you know, there's a difference between
*  kind of learning something and then having it being there at the birth state versus genes actually
*  hardwiring the thing into the system per se. And those are kind of two different versions of
*  nativism. So I just thought it'd be worth distinguishing between those. Yeah. So chicks
*  are basically ready to go right away. So about 48 hours after birth is when they reach their peak
*  visual acuity. It's much lower than humans. So human visual acuity is about 35 cycles per second,
*  or 35 cycles. And chicks is about 1.5, which is better than rats and better than mice,
*  but certainly not what you get at with what you get to with humans. So, you know, there's a lot of,
*  you know, there's a lot of differences or there are some differences. It just, you know, we don't
*  know how much these matter, right? This is the problem with reverse engineering or the fund of
*  reverse engineering, depending on your perspective is it's kind of more of an art than a science,
*  right? So you start simple and you take a guess of what matters, right? Maybe CNNs matter, maybe
*  transformers, maybe RL, and you push that system as far as you can get. And then at some point,
*  it's going to break and you're going to notice differences between the animals and the machines.
*  And then you just start plugging other stuff in, you know, but critically you start simple,
*  but then you plug stuff in when you need it. And then you can ask, what is that extra thing that
*  I just plugged in? What does it gain me in terms of function? And, you know, I think the
*  Ventral Visual Stream is a wonderful example of how this research program has emerged, right? I mean,
*  you know, Dan Yeamans and DeCarlo started with just feedforward systems, even though they perfectly
*  knew well that there's huge recurrent connections, but there was a lot of value to knowing that a
*  feedforward system could actually solve a large, you know, many of these hard problems of vision.
*  I remember back, you know, 10 years ago, 15 years ago, when I would teach vision classes,
*  I had this slide that said, we have no idea how vision works, right? It's like, it was a little
*  bit mysterious. We didn't know, like, generally what kind of system you needed to solve it. And
*  now, of course, we, you know, I have a whole lecture on how vision works and how we can replicate it
*  with feedforward and also recurrent neural networks and what you gain by adding in each one of these
*  extra little pieces. And I think that's what's really beautiful about reverse engineering is
*  not that you just throw the most complicated system you can add it at the beginning,
*  you really just start small, see what you can get with, you know, for example, reinforcement
*  learning and CNNs in the case of collective behavior, see how far you can push that and then
*  start adding in more complex models as you need them. Well, speaking of starting simple, what do
*  you say to people who, you know, so the original experiments that you did, comparing neural nets
*  and brains involved, you know, just a blank screen, a single object for, I don't know,
*  days and days maybe, I'm not sure how long it lasted the training, but that's a far cry from
*  a naturalistic, ecologically valid environment. And like, right now, there's this huge push that
*  we need to get beyond these sort of task defined and minimalistic toy models, et cetera, toy
*  experimental setups. And because it doesn't necessarily apply to the naturalistic, ecologically
*  valid world. But I know that you're moving more and more toward that with the virtual reality
*  systems and what we're about to talk about with the reinforcement learning, et cetera. But how do
*  you, what's your response to that kind of feedback? Yeah, I would say that's absolutely right. But
*  it's important to distinguish between two types of naturalism, right? So on one hand, we can talk
*  about the naturalism of the images, right? So in this case, something like ImageNet, right, you're
*  showing natural images. These are images that were taken from the natural world. So on one hand,
*  you could talk about the naturalism of the stimuli per se. But on the other hand, you could talk about
*  the naturalism of the data that can be acquired by the model, right? And so in the vast majority
*  of computational neuroscience, we're using these disembodied models, right? These are models that
*  just sit there. And the researcher picks the training data and kind of spoon feeds this data
*  to these models. But the models have no decisions about, you know, given their current knowledge
*  state, I'm going to pick this information versus that information to learn from, which of course,
*  animals are able to do. And so I think we need to distinguish between naturalism on the stimuli
*  side of things and naturalism on the embodied side of things. So even though we have really
*  simple environments, right, just to kind of a rectangular room with a single virtual object,
*  the animals can move around that entire space and produce, you know, thousands and thousands of
*  unique images of just that single virtual object. And so I think that kind of naturalism in terms
*  of embodiment is actually quite important and might, you know, we don't know, but might be
*  more important than the naturalism of actual stimuli that you're seeing. So this, of course,
*  is an empirical question, like they all are. But, you know, this and this is what we hope to address
*  when we go to the kind of the more advanced four screen VR chambers where we can, you know, really
*  raise animals in a farm or in a forest and give them all the same kinds of visual stimuli you'd
*  actually get in the real world and, you know, see how much that matters versus, you know, you could
*  put a chick in a world and maybe the world doesn't update as it should, right? They move and the world
*  updates a second later or they move in the viewpoints that you get are radically different than
*  what you should actually get if you're moving in that way, right? So these are ways where we can
*  actually see whether the naturalism of how you move through the world is also causally related to
*  this capacity of learning. So again, I think there's really two types of naturalism that come into
*  play, especially when you start to embrace embodiment in the way that we are.
*  Okay. So we've talked a little bit about the convolutional neural network experiments and then
*  you've, it seems like you're just gradually building up and up and up and making it more complex
*  and asking bigger questions. So pixels to action and pixels to actions or action and collective
*  behavior and imprinting with the reinforcement learning agents. That was a mouthful that I just
*  said. But so these are experiments that you've done with, I guess embodied AI agents trying to
*  figure out what leads, like what are the criteria that lead to collective chick behavior
*  and mixed in with that as imprinting story as well. So can you describe a little bit about
*  why you're, what led you to do those experiments and what you found there?
*  Yes, absolutely. So a lot of that work was an attempt to take kind of the beautiful closed loop
*  systems that had been worked out with the ventral visual system. I just fell in love with that idea
*  that you could build an image computable model that could be directly compared with a primate
*  or with a human to try to take that idea of building a closed loop system between biological
*  and artificial systems, but extended to embodiment. So, and collective behavior was one of the first
*  areas we really wanted to target. I remember in graduate school just falling in love with
*  collective behavior. So just, you know, it's quite amazing to see, you know, whether it's schooling
*  fish or flocking birds, how they can fly in these amazingly intricate patterns and never crash into
*  one another and yet end up building these just kind of beautiful dynamic displays. And, you know,
*  I certainly wasn't the first one to be amazed by this, right? So, you know, you can find quotes
*  from biologists a hundred years ago where their leading theories were like, maybe animals have
*  some sort of telepathy that we don't have. And that's what allows them to engage in this
*  collective behavior. That was our leading theory, was telepathy. And so, you know, I, you know,
*  and then, you know, in the past around the 1980s, work by Craig Reynolds, he actually created these
*  systems called Boyds, which he used it for computer animation. He was an animator and he didn't want
*  to animate every single bird in a flock. So he essentially created these hard coded systems that
*  with just the three simple interaction rules, like, right, like stay close to your neighbor,
*  don't crash into them and align your body with them. What he found, and this is also work by
*  Ian Cousin, who's a biologist. Basically, they found that these Boyds were actually really good
*  models of predicting how, you know, they could actually reproduce the kinds of behaviors that
*  you end up seeing animal groups doing. And so this was really neat, right? Because now we actually
*  had a model that didn't have telepathy in it, right? It actually had understandable hard coded
*  rules. And that would actually produce the same kind of behavior as animals. But it does leave
*  open this question, right, of where do those rules come from? Right? So maybe evolution,
*  hard codes and rules, however it might do so into an animal, because of course, being in a group is
*  safer than not being in a group, there'd be a lot of survival benefits to being in a group.
*  And so one might imagine a more nativist story, which is that collective behavior emerges from
*  these hard coded interaction rules. We thought it might be something different, which is maybe
*  these hard coded interaction rules come from something more basic, right? Something more core.
*  And so we just tried CNNs with reinforcement learning, just on kind of like on a whim to see
*  if that would be enough, if that's all you need, so to speak, to use computer vision,
*  you know, speak is, are those the only ingredients you need to make collective behavior tick?
*  And what we found is that it is. So you essentially, for people who haven't read
*  this paper, essentially, you can just take a group of artificial animals, and you can give them
*  reinforcement learning and a CNN as an encoder. It doesn't matter how big the encoder is, it can
*  be two layers or three layers or 15 layers, you basically get the same performance. But you get
*  the sense of curiosity. So it's basically just given two different observations predict what
*  action is going to happen next, predict what the next action is. And then you use the error of the
*  reward in order to motivate the policy network. And as it turns out, that's all you need, you end
*  up seeing groups of animals spontaneously grouping together and imprinting to one another, so to speak,
*  just from those simple ingredients of reinforcement learning and curiosity and critically being raised
*  together. So this is one thing I really love about that paper is that you can do controlled
*  rearing experiments on machines the same way you can do it on animals. And then you can causally
*  explore the role of experience in the development of machine intelligence. And so in one experiment,
*  we raised the machines together. So just like newborn animals, they typically are, there's almost
*  like a litter of animals. And so the first thing an animal sees when they open their eyes are their
*  brothers and sisters sitting around them. And their brothers and sisters are moving around in
*  unpredictable ways. So you would expect a curious agent to start paying attention to those
*  unpredictable things happening in their environment. You don't need hard coded knowledge of agents or
*  social groups or anything like that. You just need a curious learning agent to be born with other
*  agents and they'll learn from one another. If you take exactly those same agents and you raise them
*  separately, no collective behavior whatsoever. So it's not just that
*  RL and curiosity automatically leads to collective behavior. It's really an emergent property of
*  those learning algorithms interacting with these social experiences that rapidly produces collective
*  behavior. And this might be one of your next questions, like what does this tell us? And I
*  think what this tells us is it gives us an image computable model of collective behavior, right?
*  It tells us the sufficient conditions, the sufficient algorithms and experiences you need
*  to explain why animals group. And there might be lots of models that do it. But this is at least
*  one set of models that actually ends up just producing this without any hard coded knowledge
*  about, again, agents or social groups or all these other things that researchers have proposed might
*  be innate to explain social grouping. Can we just talk about the curiosity for a moment,
*  algorithmically? So I think that you mentioned this and I don't know, I know you tested a few
*  different versions of a curiosity algorithm, I think. But basically, from what I understand,
*  at least from one line of curiosity driven reinforcement learning, and I think you just
*  said this is that you make a prediction and the bigger the error in your prediction, the bigger
*  the reward. And then you update the policy based on how big that error was and then you take actions
*  to explore that space more and make more predictions, is that right?
*  Exactly.
*  Okay. It's an odd, I mean, I think that if you only did that, that would lead you astray in real life,
*  but there must be some sort of reward function. I mean, the idea is that it's like an intrinsic
*  reward without an extrinsic reward.
*  That's correct. That's correct. And I should mention this algorithm came from Pathic back in
*  2017. So full credit to him and the Berkeley group that came up with that. We were just excited to
*  have an unsupervised system that could actually learn in an in-line.
*  You're just waiting. You're just waiting for all these tools to hit your lab, right?
*  Exactly. Exactly. That was one of the ones we were waiting on. So yeah, that's absolutely right.
*  One critical thing that might kind of help explain or make sense of how pursuing novelty could lead
*  to something like familiarity, right? There seems to be like a tension there is you need a critical
*  period. So this is, you have to subject the machine to a critical period so that you ramp
*  down learning until eventually learning is at zero. The same way that in an actual animal,
*  we see critical periods all over the place, especially in imprinting is initially chicks
*  have their imprinting period open for about three days and then it shuts down. And so if you don't
*  put the machine through the critical period, it'll just continue to explore novelty. It's really
*  about shutting down that learning with the critical period that allows us to match animals and machines.
*  And my hope is this tells maybe AI researchers something important about critical periods,
*  right? So this is almost non-existent in the AI or ML world. It's basically just take a huge amount
*  of data and you train these large scale systems, but maybe there's something really important about
*  learning something and then having a critical or sensitive period and shutting it down and having
*  that serve as the foundation for the next stage of learning. We know the critical and sensitive
*  periods are widespread in animal brains. And so, you know, my hope or what our lab is doing is to
*  essentially start using critical periods in machine learning studies and see what this might buy us
*  in terms of being able to match the behavior of animals and machines. And at least in critical,
*  at least in collective behavior, it seems to be essential.
*  So thinking about humans, at least these days, a lot of people spend a good deal of effort trying
*  to practice beginner's mindset and for that critical period of curiosity and novel seeking
*  to never end. And we do it in various, you know, artificial ways, you know, in meta, you know,
*  for a healthy mind. But I suppose this is how, you know, our own critical window is how we become
*  prejudiced and how we stop learning new things. And I mean, should we fight against that or should
*  we embrace it as humans, you know? Right. I think that's really great.
*  Yeah. You know, there's this phenomenon called the baby duck syndrome in human computer interaction,
*  which is that people tend to like the first computer systems that they ever used. And then
*  they have a hard time adjusting to other computer systems, right? So in a way, that's like we're
*  imprinting to our computer system because we're learning habits and policies that allow us to use
*  that computer system really well. Then when you switch to another computer system, now you need
*  to kind of relearn a bunch of stuff. So I think we see this kind of widespread across human behavior.
*  If you pay attention, right, children like watching the same movies over and over and over again.
*  And we really like familiarity. And, you know, there's even a, I can't remember the reference,
*  but I remember this paper came out. It was in science suggesting what is the top-sided
*  papers. And the top-sided papers are often papers that are 90% familiar and 10% novel.
*  So, you know, we really don't like pure novelty. We want a lot of familiarity to kind of
*  ground our foundations of knowledge and just a little bit of novelty added on top ends up
*  producing kind of the most impactful scientific paper. So, you know, I think you can often think
*  that humans are just curiosity machines, right? We're constantly going out and seeking new
*  experiences and acquiring data, but that's not actually how it works, right? I mean,
*  we do that sometimes when all our other needs are met. But I think it's actually,
*  if you look at 24-7 behavior of an animal or of a child or of a human, you see something really
*  different. Yeah, yeah. I worked in on my mom this morning. I saw a visiting family and she's just
*  on her iPad playing solitaire like she does every morning. It's like, oh, come on, mom,
*  do something new, explore some new space. I want to ask you, maybe I'll come back to
*  imprinting later because I want to ask you about like what the current science of that is. And I
*  know this is another aside, but so thinking about these reinforcement learning agents and just
*  raising the chicks in these environments and maybe especially the first studies that we talked about
*  where, you know, there's this funny looking object that you're testing them on in this
*  controlled rearing experiments and thinking about development and critical periods. Do we have any
*  idea what this does to their visual cognition as adults, you know, if you're training them in these
*  environments and how you might guess with artificial agents if you could study that as well?
*  We don't know yet. It's a really good question. Right now, this might be another waiting period
*  because we don't have the same kind of continual learning systems that we know that biological
*  systems can do. So right now we've just been focusing on the very first or just the very first
*  few objects that newborn chicks create. But our hope is that as continual learning kind of ramps
*  up in the machine learning world, then you could imagine raising chicks until adulthood. And we
*  actually have these chambers ready to go where you could actually, you know, give an animal one set
*  of experiences for the first couple of weeks of life. And then a totally different set of experiences
*  the second few weeks of life and ask how does that animal then end up navigating those
*  learning landscapes in order to adjust. And then of course you could put the machine in
*  through exactly the same ropes, right? You could ask does that machine end up re-learning in the
*  same way that the actual animal ends up re-learning. And I think this will be helpful because there
*  might be a lot of ways to build a continual learning system but we'll have no way of knowing
*  which is right or which is wrong as it compares to animals unless we actually put them in a closed
*  loop system with one another. Right? We have to raise them in the same worlds. We have to test
*  them with the same tasks. If we're not doing both of those things, we'll never be able to say whether
*  they're the same or different in terms of how they develop. So, you know, kind of again coming
*  back to the general theme is I think we need a test bed that is publicly accessible where we have
*  rigorous data of animals and machines being raised in the same worlds and tested with the same tasks.
*  Once we have that, we can come up with whatever tasks we want or whatever we care about, whatever
*  the next stage of AI evolution is. And then we just test the animals and then we just plug those
*  same sort of algorithms into the machine and, you know, see what works and see what doesn't,
*  what closes the gap and then we move on to the next problem. So this is really
*  exposing my naivete but there must be other people who are using AI models to study development that
*  are not doing it in a controlled rearing from birth setting. I don't want to ask you like what
*  you think of that, you know, if that's all for naught but I mean maybe what does that world think
*  of, you know, the control rearing aspects or what, you know, is there value still in
*  doing something that is not as perfect as your research? Oh, absolutely, absolutely. So, you know,
*  the first thing I would say is that I could really care less about chickens, right, so that the reason
*  I use them is because they're a model system that allows us to discover general principles of how
*  experience and core learning algorithms, whatever those are, interact with one another. But nobody,
*  I don't think anybody in the field will be convinced if we just discover something with
*  chickens and it doesn't actually generalize to any other species. So, you know, ideally, you know,
*  chicks are a way we can actually make a deep, deep run at these questions. You know, I think I
*  mentioned the study where you can, you know, raise an animal where object permanence is false. This is
*  something that we recently did in case you want to chat about it. But, you know, that's something you
*  could never do with a baby, you know, ethically or practically and so the hope would be that some of
*  these general principles we discover from chicks could then be applied to humans, for example. And,
*  you know, Brendan Lake is doing some really wonderful stuff in this regard. So, he takes,
*  for example, SAICAM data that Mike Frank put together along with a bunch of his collaborators
*  and essentially trains transformers and CNNs through the eyes of this baby cam data. And,
*  you know, that's great because it's the same approach. You can't vary the visual diet of a
*  baby the same way that you can with a chick. But if what we discover with chicks is right,
*  we should find that that same approach should work with babies too, right? You just, it's going to be
*  just much more complex experience. You won't be able to figure out how particular experiences really
*  impact the development of vision, but it's a critical sanity check to make sure that whatever
*  we're discovering with chicks actually does apply to animals more generally. So, yeah, I think we
*  need to use lots of model systems. I think that just sticking with chicks would be a mistake. So,
*  we actually even do stuff with fish. So, for collective behavior, we have a fish collective
*  behavior paper where we find that if you insert, you can basically look at the emergence of
*  collective behavior in fish and it takes about 21 days for them to start to group together.
*  So, we built a bunch of virtual fish and put them in virtual fish tanks. And what we found is that
*  the development of collective behavior is identical across those virtual fish and the real fish.
*  So, they start not caring about one another and then they gradually start grouping together more
*  and more during development. And you can see this kind of parallel developmental trajectory across
*  the biological and artificial systems. And so, yeah, again, I think it's really important to
*  use different model systems and really try to discover general principles of learning
*  rather than just specific things that might happen in an individual animal.
*  I know that we're all over the place here, but I'm just curious. So, there's a difference between
*  collective behavior and swarm behavior. Is swarm behavior a type of collective behavior or yeah,
*  subtype? That's right. Exactly. So, collective behavior just generally refers to animals
*  interacting with one another and they can form a lot of different kinds of dynamic systems,
*  so to speak. Swarming is a particular kind of collective behavior that emerges
*  when certain characteristics are met. You're not studying chicks swarming,
*  which would be something else. Yeah, but also like you'd mentioned the object invariant,
*  breaking those rules, raising them in conditions where object invariance isn't a thing.
*  Tell me about that and then we'll come back to the reinforcement learning again. I know it's
*  terrible that we're jumping around. Sorry. Oh, no, that's okay. That's okay. No, this is one of my
*  favorite experiments, so I'm excited to tell you about it. So, this has no AI or ML component yet.
*  We really hope it will, but the study is basically imagine being raised in a world in which object
*  permanence is never true, right? So, here's how the experiment works. Again, take a chick,
*  you hatch it in darkness, you move it over to a video game, basically a video game world
*  that's where the chick controls the actions happening in the video game world, and then
*  for the first several days of life, the chick sees like two screens. So, there's an object,
*  two screens move up, and then the object goes behind one of those screens, and then the screens
*  move down. Now, in a natural world, the object's always where it was when it disappeared or when
*  it moved out of view, whereas in the unnatural world, the object's always behind the other screen,
*  right? As if the object teleported from behind one screen to the other screen.
*  So, we raise chicks either in the natural world for several days or in the unnatural world for
*  several days. I'll just point out, of course, that only the chicks in the natural world had
*  experience that object permanence was true, right? The chicks in the other world had the
*  opposite experience. If it's pure learning, they should have learned something radically different
*  than the chicks raised in the natural world. As it turns out, they look exactly identical to
*  one another. Their behavior is almost identical with both the natural raised chicks and the
*  unnatural raised chicks both showing object permanence. I love this study because it shows
*  why we need VR, right? So, one could have guessed, and many empiricists think this, is that object
*  permanence is learned, right? You have ample experience seeing objects, balls rolling under
*  couches and then reemerging, or dogs going away and then coming back, right? We see this all the time,
*  and so maybe object permanence is learned. The only way we could ever figure that out is if we
*  actually put animals in a world where object permanence wasn't true, where you didn't have
*  the experiences you needed to learn that, and then you can ask, does the animal still show that
*  capacity? For the case of object permanence, we still do see that. Our speculation is that prenatal
*  training data is so rich that maybe it builds a visual system that has object permanence, in a
*  sense, baked into it so that even when you get contrary experience, that initial foundation is
*  so strong that you just can't unlearn it. Given that a retinal wave is a lot like an object that's
*  obeying object permanence as it moves across the eyeball, basically from the moment the brain is
*  growing, or from the moment the retina develops at least, you're getting experience that object
*  permanence is true during prenatal development. Again, I love this way of basically being able
*  to look at what's learned and what's not learned through VR because it lets us make a clear
*  distinction. We know in that case that it's going to be some sort of native history in terms of
*  where object permanence comes from. Okay. I'll finally bring us back to the deep reinforcement
*  learning collective behavior stuff. One of the interesting things is with the convolutional
*  neural networks, the experiments we opened up with, it seems to be more the inductive biases are
*  inbuilt essentially, and you talked about this domain general learning knowledge, and it takes
*  very little for them to learn the object permanence, object invariance. But you make the point that
*  in terms of the collective behavior, you actually really need that curiosity-driven learning
*  algorithm. It's really more of a learning story in terms of collective behavior than it is in terms
*  of visual cognition, basic visual cognition, I guess.
*  Yeah, that's right. If I don't answer your question directly, feel free to ask it again. I think one
*  of what you're suggesting is maybe there's a little bit of a tension between the CNN results
*  and the collective behavior results. Exactly. Well, it was an open-ended question because
*  that's just from my perspective. It seems like there might be a tension, but it could be an easy
*  story to be made that they're both at play because we're nativists and empiricists,
*  and they're both right, I suppose. Yeah, at least that's my view. Yeah, I'm glad you asked.
*  With the CNN results, what we find is that if you use a supervised linear classifier,
*  you can read out from a frozen CNN view invariant object features, and you can discover those
*  features in the embedding space using even just a single viewpoint. Even though it's supervised
*  learning, which the chicks don't get, you can still use a very small amount of data in order to find
*  the right set of features in the embedding space that allows for view invariant recognition.
*  That works, so that suggests that the CNN is at least developing the features it needs or learning
*  the features that it needs in order to be able to succeed in the task, but that's quite different
*  from an embodied agent discovering those features on their own. In one of the papers I sent you,
*  we call it a newborn embodied Turing test. This is an experiment that's really similar to collective
*  behavior, but essentially we take exactly the same agent, except it's just one little artificial
*  chicken in a chamber instead of a whole group of them. This matches directly to the experiments
*  with the chicks. What we find is that even though our CNN experiments show that view
*  invariant recognition can be learned from this sparse data, we find that the embodied agents
*  don't discover those features. In fact, the machines end up looking radically different
*  from the actual chicks. The machines develop view-dependent representations rather than view
*  invariant representations. It's almost like they're relying too much on statistical learning,
*  or they're fitting to the data a little bit too much. We also found this is work by Mandju
*  Garamella in our lab. She finds that machines are very background dependent. This was an experiment
*  where we raised one object on one background. That was their entirety of their visual experience
*  for the first week of life. If you're relying purely on statistical learning, you should yoke
*  the features of the object with the features of the background, which is what you don't want because
*  then you can't recognize that object across novel views. Chicks are wonderful at this. They're not
*  at all thrown off when you change the background, but machines are terrible at this. You change the
*  background on a machine, and now they go more by the background than they do by the object itself.
*  This suggests that even though we can get these systems to imprint in the same kind of chambers
*  where we get real chicks to imprint, what we're not finding is the same kind of recognition
*  capacities developing. This leads us to think that there's something missing. We have no idea what
*  that is. We have some guesses, of course, but there must be something missing in the machines
*  that the animals have that allows the animals to develop these view-invariant, background-invariant
*  representations that really support high-level vision. That's what we currently see as one of
*  the big things in the lab is how do we get an embodied agent to discover that particular set
*  of features, the high-level features that are needed in order to solve the task?
*  You said you had some guesses. I think you were about to say some of your guesses, perhaps.
*  Yeah. One of our guesses is the retina is highly dynamic. In machine learning world,
*  we often feed in RGB images, but if you look at what visual data looks like after it goes
*  past the eyeball, after it goes through LGN, it just looks completely different. You only essentially
*  maintain moving features. There's these wonderful demos called the dynamic visual system.
*  Demos that people can pull up. I highly encourage you to do this where you can see
*  you can convert a real video into a DBS video. You can see that basically you get rid of 99%
*  of the data, but the only thing left is what changed because you're only keeping those
*  changing signals, which is what neurons do. That might solve the problem. It might be the case that
*  if you're only paying attention to moving things, and we have some data suggesting that this is what
*  chicks actually do, if you're only paying attention to moving things, you've made your
*  computational problem a lot easier. Rather than having to reason over the whole 224 by 224 image
*  space, now you just get to worry about those moving features. Those moving features will then be
*  automatically segmented from the background because if you still your head, the background
*  is not moving, but the object might still be. This is one way that a biological system, just based on
*  having a different eyeball, having a different body, not having a different brain, but having
*  a different body could lead to radically different kinds of changes. More generally,
*  I hope what happens is that rather than just focusing on the learning algorithms per se,
*  is I hope the field embraces morphology as well because it might very well turn out that the body
*  of an animal, the nature of their eyeball, the nature of their ears, the nature of how they move
*  through space is going to influence their training data. It's going to influence what they perceive.
*  I think we're going to have to start playing around with different artificial bodies the same
*  way we've been playing around with different artificial brains in order to have a chance of
*  closing this gap between animals and machines. That's my speculation. I think it's really about
*  the eyeball per se and the nature of the input you actually have going into the visual system
*  rather than just the RGB frames that we typically feed in now.
*  That's a bottom-up attention story. If you're attending to relations or actions or differences
*  in movements, is there a top-down story in chicks also?
*  It depends on what you mean by top-down. My world was rocked by Henry Yen a few years ago
*  when he came on your podcast and he started talking about negative feedback control systems,
*  which really questioned what it even means to be bottom-up versus top-down.
*  Ultimately, I think what you need to do to test that question is just build in whatever you mean
*  by top-down, instantiate it into the brain of the artificial animal itself and see if that ends up
*  making a difference. You might imagine that if an animal is trying to control some internal
*  homeostatic variables in a negative feedback control system, then that might influence the
*  kinds of features that it's going to end up paying attention to depending on its current needs. If
*  you're hungry, you might pay attention to this set of features. If you're thirsty, you might
*  pay attention to this set of features. If you're scared of being chased by a predator, you'll,
*  of course, look for a third set of features. I really think that embracing the control of
*  a system rather than the input-output approach that we've been taking in ML and AI might turn
*  out to be quite important, especially as we scale from these disembodied systems to the embodied
*  systems that actually act in the world and have goals of their own in some ways.
*  Yeah. Those internal set points, you mentioned Henry Yin. What are those internal set points?
*  Is it all homeostasis? Where does it all derive from? It's really hard and fascinating to think
*  about for me. There's this paper by Michael Anderson, Michael Anderson, whom I've had on the
*  podcast. It's all about behavior as what they call, and Vicente Raja is the co-author, what they call
*  behavior as an enabling constraint. As you were thinking, right after I said, well, that's kind
*  of a bottom-up attention mechanism. The other thing with morphology and the way that our eyes
*  work and the way that we interact with the world is you could think of that as a top-down constraint
*  as well, because it is like top-down, did I say constraint? Yeah, mechanism, constraint, whatever,
*  because it is constraining the way the signals that get in and how they get in. That's almost
*  a top-down thing. You were saying, well, it depends on what you consider bottom-up and top-down. Yeah,
*  it all gets mixed up, I suppose. Do you think of the environment and our behaviors, do you think
*  of that as shaping our neural activity in a top-down constraining kind of way also?
*  Absolutely. I think that the way of looking at, the way of building scientific models by allowing
*  those models to do tasks in their own right and then putting constraints on those models to see
*  if we can push them to the same part of the parameter space as biological systems, I think
*  that's absolutely the right idea. This, of course, comes from Yamins and DeCarlo and Pico-Squart and
*  other wonderful people. I think we'll need to do the same thing with embodiment. Your body places
*  constraints on what you can see and what you can do and what kind of training data you can acquire.
*  Your physiological needs are going to place additional constraints on the kinds of things
*  that you look for in the world. Even the nature of, as we were talking about, the nature of your
*  eyeball is going to place these radical constraints on the nature of the data actually going into your
*  brain. I think all of these, we don't know which constraints matter and which don't. That's why
*  we're doing the science in the first place is to figure out what matters and what doesn't. We have
*  thousands and thousands of details of phenomenon and lists of facts and neuroscience, and we don't
*  know what matters and what doesn't. I really love this reverse engineering approach because
*  it gives us a way of figuring out at that engineering level of abstraction, what do we
*  need to keep and what can we throw away in order to be able to build functioning intelligence?
*  I think that we should just add constraints and see if they matter. Some might matter a huge amount,
*  some might not matter at all, but we can do this. We can take an empirical approach on this and just
*  plug them into the artificial animals and see which of those constraints really matter and which
*  don't. I think that's how we get a domain general system being pushed to the same part of the
*  parameter space as an animal is through heavy, heavy constraints on their morphology, on the
*  learning rules, on the architecture, on all the various things that have been pointed out by some
*  of your prior guests. How far can you push your system, your pixels to actions? What's your vision
*  for how far you can take this and where the limit is? Do you see a limit? Wow, that's a great question.
*  I hope this doesn't come off here, but I don't see a limit. The reason I tried to do this 10 to 15
*  years ago was because I wanted to fully embrace an entire whole animal. It recognizes objects,
*  it navigates the world, it develops social connections, it solves all of the problems
*  that animals solve. I don't want to say anything negative about the kind of piecemeal attempt that
*  we've been attempting in the field. You need them all, right?
*  You need them all, yeah. The beautiful work of the visual system and the auditory system and the
*  olfactory system, that's absolutely wonderful work. At some point, we're going to have to put
*  those together into a single unified system and then see if that single unified system develops
*  a visual system and an auditory system and all the various kinds of systems we actually see in
*  a real developing organism. I think we have to take development seriously because the only
*  evidence we have of an intelligent system is through development. Typically, we'll take an
*  adult state and that will be our target and then we'll try to build an A&N through massive training.
*  We won't care if it's evolution or development. We'll just say, it doesn't really matter, but
*  we'll just take that A&N model and compare it to an adult animal. I think that's fine, depending on
*  what your goals are, but if you want to build a unified model of intelligence, you have to take
*  development seriously. You have to take embodiment seriously and you have to take agency seriously.
*  You have to let the, just like real animals who are embodied and can decide what they're going to
*  do next, you need to give machines that same kind of capacity because ultimately, I think the name
*  of the game is to ask how much of the phenomenon can you explain through your model? If we get it
*  right, I imagine it'll be more complicated than this, but let's just say that it's a transformer.
*  If we stick a transformer into a developing chicken embryo, artificial chicken embryo,
*  we give it prenatal training data and all that, and then we give that artificial chicken the same
*  kinds of experience as a real chicken and it starts to develop object recognition and it
*  navigates path integration and snapshot-based navigation and reorientation and all the core
*  capacities that nativists have pointed out over the years. If we find that one model doing all of
*  those things, we've now then got a unified model, a unified closed loop system model that can be
*  used to then do additional tests. That to me is kind of at least what our lab is chasing.
*  The same way that Darwin gave us DNA as a way to connect tigers and worms and insects to one
*  another through a common medium, we need something like that for psychology. We need some sort of
*  medium, maybe this will be like a transformer or something else, that allows us to explain why
*  brains develop object recognition and smell and navigation and decision making and face selection
*  and all the various things that we develop. I think that we need to embrace or chase a unified
*  model and this is the only way I can see us doing it, is taking development seriously and controlling
*  data from the very beginning of life. Surely the transformer is not it. Surely the transformer is
*  another five-year thing that will be replaced. You keep mentioning transformer because that's
*  like the latest and greatest, right? It's the latest and greatest and it's definitely pushed
*  back on me if you don't agree. In many ways, I consider it to be one of the best models we
*  have in cognitive science. I know it's not treated that way, of course, but it's the one model we
*  have that can do a bunch of different things. There's this beautiful Gatto model from Deep
*  Mine, for example, that can play video games and it can capture images and it can write essays for
*  you and it can control a robot arm. This is one of the first examples we've seen of a single unified
*  system that can actually do a wide range of different things. Given that that's the only
*  system that we have and given that that's one of the hallmarks of human and animal intelligence,
*  I really think that we should treat transformers seriously. We don't understand how they work yet,
*  but that's okay. We didn't understand how steam engines worked until we built it and then
*  reverse engineered it. I think we want to just first find a system that can do all of these
*  different things and then we can make sure it actually matches the biological system,
*  which is what we're trying to do. Then, of course, all the brilliant mathematicians of the world can
*  try to understand how these things are working in a way that gives us a fielding of understanding,
*  whatever understanding means. I think it's going to mean something different to everybody else.
*  I mean, it seems like your lab's going gangbusters. I think I mentioned this earlier.
*  You probably have 15 different experiments, ideas, things to test lined up. Give me just
*  a quick flavor of what to expect over the next year or something from your lab. What's in the
*  very beginning stages now that you're... And then we'll wrap up, I promise.
*  Yeah, this is really fun. So yeah, next stage will be, hopefully, we'll have every CHIC experiment
*  we've ever done publicly available for people to try. So this will be hundreds of experiments.
*  So instead of just the one or two experiments we talked about here, it'll be hundreds of
*  experiments with detailed data from CHICs. People can basically plug in their model and test it
*  across the whole test bed. And then that way we have this integrative benchmarking approach
*  focusing on this, I think, fascinating question of the origins of knowledge. So that's what we
*  hope to have that up and running in the next year. And then the other thing will be, we're
*  going to be start exploring other capacities. So I've always loved navigation, especially because
*  a lot of core navigation abilities emerge quite early on. So you see newborn animals doing things
*  like path integration and snapshot-based memory and reorientation. This is part of the core
*  knowledge tradition. And so I'd love to see, what does it take? What kind of learning algorithms do
*  you need in order to reproduce core navigation in a machine? And we can play the same game of
*  raise the machine in the same world as the animal, make sure that it's all, they get the same
*  training data. And then we can start asking, again, does that same core learning algorithm
*  that gives us object perception, does that very same algorithm also give us navigation?
*  And then in the future, does it also give us social cognition? So can we slowly expand out
*  the range of tasks until we have a single unified model explaining all the various things we care
*  about? That is the dream. Okay, folks, I have nativist Justin Wood. I'm just kidding. I'm just
*  kidding. I have non-nativist nor empiricist, but accepting of both Justin Wood. Hey, Justin,
*  I'm glad that we finally got to connect. We had to keep kicking it down the road,
*  but I appreciate you coming on. And of course, best of luck, even though you don't need it.
*  And thanks for being on. Oh, thanks so much for having me. It's been a pleasure.
*  I alone produce Brain Inspired. If you value this podcast, consider supporting it through Patreon
*  to access full versions of all the episodes and to join our Discord community. Or if you want
*  to learn more about the intersection of neuroscience and AI, consider signing up for my online course,
*  Neuro AI, the quest to explain intelligence. Go to braininspired.co to learn more. To get in touch
*  with me, email paul at braininspired.co. You're hearing music by the new year. Find them at
*  the newyear.net. Thank you. Thank you for your support. See you next time.

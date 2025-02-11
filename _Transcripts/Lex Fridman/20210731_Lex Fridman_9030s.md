---
Date Generated: April 12, 2024
Transcription Model: whisper medium 20231117
Length: 9030s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'ishan misra', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai']
Video Views: 128470
Video Rating: None
---

# Ishan Misra: Self-Supervised Deep Learning in Computer Vision | Lex Fridman Podcast #206
**Lex Fridman:** [July 31, 2021](https://www.youtube.com/watch?v=FUS6ceIvUnI)
*  The following is a conversation with Ishan Misra, research scientist at Facebook AI Research,
*  who works on self-supervised machine learning in the domain of computer vision, or in other words,
*  making AI systems understand the visual world with minimal help from us humans.
*  Transformers and self-attention has been successfully used by OpenAIS-DPT3
*  and other language models to do self-supervised learning in the domain of language.
*  Ishan, together with Jan Lekoon and others, is trying to achieve the same success in the domain
*  of images and video. The goal is to leave a robot watching YouTube videos all night
*  and in the morning come back to a much smarter robot. I read the blog post,
*  Self-Supervised Learning, The Dark Matter of Intelligence by Ishan and Jan Lekoon,
*  and then listened to Ishan's appearance on the excellent Machine Learning Street Talk podcast,
*  and I knew I had to talk to him. By the way, if you are interested in machine learning and AI,
*  I cannot recommend the ML Street Talk podcast highly enough. Those guys are great.
*  Quick mention of our sponsors. On it, The Information, Grammarly, and Atheca Greens.
*  Check them out in the description to support this podcast.
*  As a side note, let me say that for those of you who may have been listening for quite a while,
*  this podcast used to be called Artificial Intelligence Podcast because my life passion
*  has always been, will always be, artificial intelligence, both narrowly and broadly defined.
*  My goal with this podcast is still to have many conversations with world-class researchers in AI,
*  math, physics, biology, and all the other sciences. But I also want to talk to
*  historians, musicians, athletes, and of course, occasionally comedians. In fact,
*  I'm trying out doing this podcast three times a week now to give me more freedom with guest
*  selection and maybe get a chance to have a bit more fun. Speaking of fun, in this conversation,
*  I challenged the listener to count the number of times the word banana is mentioned. Ishan and I
*  used the word banana as the canonical example at the core of the hard problem of computer vision
*  and maybe the hard problem of consciousness. This is the Lex Friedman Podcast and here is
*  my conversation with Ishan Misra. What is self-supervised learning? And maybe even give
*  the bigger basics of what is supervised and semi-supervised learning and maybe why is
*  self-supervised learning a better term than unsupervised learning? Let's start with supervised
*  learning. Typically for machine learning systems, the way they're trained is you get a bunch of
*  humans. The humans point out particular concepts. If it's in the case of images, you want the humans
*  to come and tell you what is present in the image, draw boxes around them, draw masks of things,
*  pixels, which are of particular categories or not. For NLP, again, there are lots of these particular
*  tasks, say about sentiment analysis, about entailment, and so on. Typically for supervised
*  learning, we get a big corpus of such annotated or labeled data and then we feed that to a system
*  and the system is really trying to mimic. So it's taking this input of the data and then trying to
*  mimic the output. So it looks at an image and the human has tagged that this image contains a banana
*  and now the system is basically trying to mimic that. So that's its learning signal.
*  And so for supervised learning, we try to gather lots of such data and we train these machine
*  learning models to imitate the input or output. And the hope is basically by doing so, now on
*  unseen or like new kinds of data, this model can automatically learn to predict these concepts.
*  So this is a standard sort of supervised setting. For semi-supervised setting, the idea typically is
*  that you have, of course, all of the supervised data, but you have lots of other data which is
*  unsupervised or which is like not labeled. Now the problem basically with supervised learning
*  and why you actually have all of these alternate sort of learning paradigms is supervised learning
*  just does not scale. So if you look at for computer vision, the sort of largest,
*  one of the most popular data sets is ImageNet. So the entire ImageNet data set has about 22,000
*  concepts and about 14 million images. So these concepts are basically just nouns and they're
*  annotated on images. And this entire data set was a mammoth data collection effort. It actually
*  gave rise to a lot of powerful learning algorithms is credited with like sort of the rise of deep
*  learning as well. But this data set took about 22 human years to collect, to annotate. And it's not
*  even that many concepts, right? It's not even that many images. 14 million is nothing really.
*  Like you have about, I think, 400 million images or so, or even more than that uploaded to
*  most of the popular sort of social media websites today. So now supervised learning just doesn't
*  scale. If I want to now annotate more concepts, if I want to have this various types of fine grain
*  concepts, then it won't really scale. So now you come up to these sort of different learning
*  paradigms, for example, semi-supervised learning, where the idea is, of course, you have this
*  annotated corpus of supervised data and you have lots of these unlabeled images. And the idea is
*  that the algorithm should basically try to measure some kind of consistency or really try to measure
*  some kind of signal on this sort of unlabeled data to make itself more confident about what it's
*  really trying to predict. So by access to this lots of unlabeled data, the idea is that the
*  algorithm actually learns to be more confident and actually gets better at predicting these concepts.
*  And now we come to the other extreme, which is like self-supervised learning. The idea basically
*  is that the machine or the algorithm should really discover concepts or discover things about the
*  world or learn representations about the world which are useful without access to explicit human
*  supervision. So the word supervision is still in the term self-supervised. So what is the
*  supervision signal? And maybe that perhaps is when Jan Makun and you argue that unsupervised is the
*  correct terminology here. So what is the supervision signal when the humans aren't part of the picture
*  or not a big part of the picture? Right. So self-supervised, the reason it has the term
*  supervised in itself is because you're using the data itself as supervision. So because the data
*  serves as its own source of supervision, it's self-supervised in that way. Now the reason a lot
*  of people, I mean, we did it in that blog post with Jan, but a lot of other people have also argued
*  for using this term self-supervised. So starting from like 94 from Virginia de Saz group,
*  I think UCSD, and now she's at UCSD. G. Tendromolec has said this a bunch of times as well.
*  So you have supervised and then unsupervised basically means everything which is not supervised,
*  but that includes stuff like semi-supervised, that includes other like trans-ductive learning,
*  lots of other sort of settings. So that's the reason like now people are preferring this term
*  self-supervised because it explicitly says what's happening. The data itself is the source of
*  supervision and any sort of learning algorithm which tries to extract just sort of data
*  supervision signals from the data itself is a self-supervised learning algorithm.
*  But there is within the data, a set of tricks which unlock the supervision. Right. So can you
*  give maybe some examples and there's innovation, ingenuity required to unlock that supervision.
*  The data doesn't just speak to you some ground truth, you have to do some kind of trick.
*  So I don't know what your favorite domain is. So you specifically specialize in visual learning,
*  but is there favorite examples maybe in language or other domains? Perhaps the most successful
*  applications have been in NLP, not language processing. So the idea basically being that
*  you can train models that can you have a sentence and you mask out certain words.
*  And now these models learn to predict the masked out words. So if you have like the cat jumped
*  over the dog, so you can basically mask out cat. And now you are essentially asking the model to
*  predict what was missing. What did I mask out? So the model is going to predict basically a
*  distribution over all the possible words that it knows. And probably it has like, if it's a
*  veteran model, it has a sort of higher probability density for this word cat.
*  For vision, I would say the sort of more, I mean, the easier example, which is not as widely used
*  these days is basically say, for example, video prediction. So video is again, a sequence of
*  things. So you can ask the model. So if you have a video of say 10 seconds, you can feed in the
*  first nine seconds to a model and then ask it, Hey, what happens basically in the 10 second? Can
*  you predict what's going to happen? And the idea basically is because the model is predicting
*  something about the data itself. Of course, you didn't need any human to tell you what was
*  happening because the 10 second video was naturally captured because the model is predicting
*  what's happening there. It's going to automatically learn something about the structure of the world,
*  how objects move, object permanence, and these kinds of things. So like if I have something at
*  the edge of the table, it will fall down. Things like these, which you really don't have to sit and
*  annotate in a supervised learning setting. I would have to sit and annotate. This is a cup. Now I
*  move this cup. This is still a cup. And now I move this cup. It's still a cup. And then it falls down
*  and this is a fallen down cup. So I won't have to annotate all of these things in a self-supervised
*  setting. Isn't that kind of a brilliant little trick of taking a series of data that is consistent
*  and removing one element in that series and then teaching the algorithm to predict that element?
*  Isn't that, first of all, that's quite brilliant. It seems to be applicable in anything that
*  has the constraint of being a sequence that is consistent with the physical reality.
*  The question is, are there other tricks like this that can generate the self-supervision signal?
*  So sequence is possibly the most widely used one in NLP. For vision, the one that is actually used
*  for images, which is very popular these days, is basically taking an image and now taking different
*  crops of that image. So you can basically decide to crop, say, the top left corner and you crop,
*  say, the bottom right corner and asking a network to basically present it with a choice, saying that,
*  now you have this image, you have this image, are these the same or not? And so the idea basically
*  is that because different crops, like in an image, different parts of the image are going to be
*  related. So for example, if you have a chair and a table, basically these things are going to be
*  close by versus if you take, again, if you have like a zoomed in picture of a chair, if you're
*  taking different crops, it's going to be different parts of the chair. So the idea basically is that
*  different crops of the image are related and so the features or the representations that you get
*  from these different crops should also be related. So this is possibly the most widely used trick
*  these days for self-supervised learning in computer vision. So again, using the consistency that's
*  inherent to physical reality in visual domain that's, you know, parts of an image are consistent
*  and then in the language domain or anything that has sequences like language or something that's
*  like a time series that you can chop off parts in time. It's similar to the story of RNNs and CNNs,
*  of RNNs and covenants. Ewan Yan-Lacoon wrote the blog post in March 2021 titled
*  Self-Supervised Learning, The Dark Matter of Intelligence. Can you summarize this blog post
*  and maybe explain the main idea or set of ideas? The blog post was mainly about sort of just telling,
*  I mean this is really an accepted fact I would say for a lot of people now that self-supervised
*  learning is something that is going to be a play an important role for machine learning
*  algorithms that come in the future and even now. Well let me just comment that we don't
*  yet have a good understanding what dark matter is. That's true. So the idea basically being-
*  Maybe the metaphor doesn't exactly transfer but maybe it maybe it's actually perfectly transfers
*  that we don't know. We have an inkling that it'll be a big part of whatever solving intelligence
*  looks like. Right. So I think self-supervised learning the way it's done right now is I would
*  say like the first step towards what it probably should end up like learning or what it should
*  enable us to do. So the idea for that particular piece was self-supervised learning is going to be
*  a very powerful way to learn common sense about the world or like stuff that is really hard to
*  label. For example like is this piece over here heavier than the cup? Now for all these kinds of
*  things you'll have to sit and label these things. So supervised learning is clearly not going to
*  scale. So what is the thing that's actually going to scale? It's probably going to be an agent that
*  can either actually interact with it to lift it up or observe me doing it. So if I'm basically
*  lifting these things up it can probably reason about hey this is taking him more time to lift up
*  or the velocity is different whereas the velocity for this is different probably this one is heavier.
*  So essentially by observations of the data you should be able to infer a lot of things about
*  the world without someone explicitly telling you this is heavy this is not this is something that
*  can pour this is something that cannot pour this is somewhere that you can sit this is not somewhere
*  that you can sit. But you just mentioned ability to interact with the world there's so many questions
*  that are yet to be that are still open which is how do you select the set of data over which the
*  self-supervised learning process works how much interactivity like in the active learning or the
*  machine teaching context is there what are the reward signals like how much actual interaction
*  there is with the physical world that kind of thing. So that could be a huge question and then
*  on top of that which I have a million questions about which we don't know the answers to but it's
*  worth talking about is how much reasoning is involved how much accumulation of knowledge
*  versus something that's more akin to learning or whether that's the the same thing but so we're
*  like it is truly dark matter. We don't know how exactly to do it yeah but we are I mean a lot of
*  us are actually convinced that it's going to be a sort of major thing in machine learning. So let me
*  reframe it then that that human supervision cannot be at large scale the source of the solution to
*  intelligence right so there has to be the machines have to discover the supervision in the natural
*  signal of the world. Right I mean the other thing is also that humans are not particularly good
*  labellers they're not very consistent for example like what's the difference between a dining table
*  and a table is it just the fact that one like if you just look at a particular table what makes us
*  say one is dining table and the other is not. Humans are not particularly consistent they're
*  not like very good sources of supervision for a lot of these kind of edge cases so it may be also
*  the fact that if we want a like want an algorithm or want a machine to solve a particular task for
*  us we can maybe just specify the end goal and like the stuff in between we really probably
*  should not be specifying because we're not maybe going to confuse it a lot actually. Well humans
*  can't even answer the meaning of life so we don't I'm not sure if we're good supervisors of the end
*  goal either. So let me ask you about categories humans are not very good at telling the difference
*  between what is and isn't a table like you mentioned. Do you think it's possible let me let me ask you
*  like a pretend you're Plato is it possible to create a pretty good taxonomy of objects in the
*  world. It seems like a lot of approaches in machine learning kind of assume a hopeful vision
*  that is possible to construct a perfect taxonomy or it exists perhaps out of our reach but we can
*  always get closer and closer to it or is that a hopeless pursuit. I think it's hopeless in some
*  way so the thing is for any particular categorization that you create if you have a discrete sort of
*  categorization I can always take the nearest two concepts or I can take a third concept and I can
*  blend it in and I can create a new category. So if you were to enumerate n categories I will always
*  find an n plus one category for you that's not going to be in the n categories and I can actually
*  create not just n plus one I can very easily create far more than n categories. The thing is
*  a lot of things we talk about are actually compositional so it's really hard for us to
*  come and sit and enumerate all of these out and they compose in various weird ways right like you
*  have like a croissant and a donut come together to form a cronut. So if you were to like enumerate
*  all the foods up until I don't know whenever the cronut was about 10 years ago or 15 years ago
*  then this entire thing called cronut would not exist. Yeah I remember there was a
*  the most awesome video of a cat wearing a monkey costume.
*  Yes. People should look it up it's great. So is that a monkey is it or is that a cat? It's a very
*  difficult philosophical question. So there is a concept of similarity between objects so you think
*  that can take us very far just kind of getting a good function a good way to tell which parts of
*  things are similar and which parts of things are very different. I think so yeah so you don't
*  necessarily need to name everything or assign a name to everything to be able to use it right.
*  So there are like lots of Shakespeare said that what's in a name what's in a name yeah okay and
*  I mean a lot lots of like for example animals right they don't have necessarily a well-formed
*  like syntactic language but they're able to go about their day perfectly. The same thing happens
*  for us so I mean we probably look at things and we figure out oh this is similar to something else
*  that I've seen before and then I can probably learn how to use it. So I haven't seen all the
*  possible doorknobs in the world but if you show me like I was able to get into this particular
*  place fairly easily I've never seen that particular doorknob so I of course related to all the
*  doorknobs that I've seen and I know exactly how it's going to open or I have a pretty good idea
*  of how it's going to open and I think this kind of translation between experiences only happens
*  because of similarity because I'm able to relate it to a doorknob if I related it to a hairdryer I
*  would probably be stuck still outside not able to get it. Again a bit of a philosophical question but
*  is can similarity take us all the way to understanding a thing? Can having a good
*  function that compares objects get us to understand something profound about singular objects?
*  I think I'll ask you a question back what does it mean to understand objects?
*  Well let me tell you what that's similar to no. So there is there's an idea of sort of reasoning
*  by analogy kind of thing. I think understanding is the process of placing that thing in some kind of
*  network of knowledge that you have that it perhaps is fundamentally related to other concepts so it's
*  not like understanding is fundamentally related by like composition of other concepts and maybe
*  in relation to other concepts and maybe like deeper and deeper understanding is maybe just
*  adding more edges to that graph somehow. So maybe it is a composition of similarities. I mean
*  ultimately it is I suppose it is a kind of embedding in that wisdom space.
*  Yeah okay wisdom space is good. I think I do think right so similarity does get you very very far.
*  Is it the answer to everything? I mean I don't even know what everything is but it's going to
*  take us really far and I think the thing is things are similar in very different contexts
*  right so an elephant is similar to I don't know another sort of wild animal let's just pick I
*  don't know lion in a different way because they're both four-legged creatures they're also land
*  animals but of course they're very different in a lot of different ways so elephants are like herby
*  wars lions or not so similarity does similarity and particularly dissimilarity also sort of
*  actually helps us understand a lot about things and so that's actually why I think discrete
*  categorization is very hard just like forming this particular category of elephant and a
*  particular category of lion maybe it's good for like just like taxonomy biological taxonomies
*  but when it comes to like other things which are not as maybe for example like grilled cheese right
*  I have a grilled cheese I dip it in tomato and I keep it outside now is that still a grilled cheese
*  or is that something else? Right so categorization is still very useful for solving problems
*  but is your intuition then sort of the self-supervised should be the to borrow
*  Jan Lekoon's terminology should be the cake and then categorization the classification the maybe
*  the supervised like layer should be just like the thing on top the cherry or the icing or whatever
*  so if you make it the cake it gets in the way of learning if you make it the cake then you don't
*  you won't be able to sit and annotate everything that's as simple as it is like that's my very
*  practical view on it it's just I mean in my PhD I sat down and annotated like a bunch of cars for
*  one of my projects and very quickly I was just like it was in a video and I was basically drawing
*  boxes around all these cars and I think I spent about a week doing all of that and I barely got
*  anything done and basically this was I think my first year of my PhD or like second year of my
*  masters and then by the end of it I'm like okay this is just hopeless I can keep doing it and
*  when I done that someone came up to me and they basically told me oh this is a pickup truck this
*  is not a car and that's like aha this actually makes sense because the pickup truck is not really
*  like what was I annotating was I annotating anything that is mobile or was annotating
*  particular sedans or was I annotating SUVs what was I doing by the way the annotation was bounding
*  boxes or boxes there's so many deep profound questions here that you you're almost cheating
*  your way out of by doing self-supervised learning by the way which is like what makes
*  for an object as opposed to solve intelligence maybe you don't ever need to answer that question
*  I mean this is the question that anyone that's ever done an annotation because it's so painful
*  gets to ask like why am I doing a drawing very careful line around this object like what what
*  what is the value I remember when I first saw semantic segmentation where you have like
*  instant segmentation where you have a very exact line around the object in a 2d plane of a
*  fundamentally 3d object projected on a 2d plane so you're drawing a line around a car that might
*  be occluded there might be another thing in front of it but you're still drawing the line of of the
*  part of the car that you see how is that the car why is that the car like I had like an existential
*  crisis every time like how is that going to help us understand a solve computer vision I'm not sure
*  I have a good answer to what's better and I'm not sure I share the confidence that you have
*  that self-supervised learning can take us far I think I'm more and more convinced that it's
*  a very important component but I still feel like we need to understand what makes like this this
*  like dream of maybe what it's called like symbolic AI of of arriving like once you have this common
*  sense base be able to play with these concepts and build graphs or hierarchies of concepts on top
*  in order to then like form a deep sense of this three-dimensional world or four-dimensional world
*  and be able to reason and then project that onto 2d plane in order to interpret a 2d image
*  Caskey's just an out there question I remember I think I think Andre Capati had a blog post about
*  computer vision like being really hard I forgot what the title was but it's many many years ago
*  and he had I think President Obama stepping on a scale and there was humor and there's a bunch of
*  people laughing and whatever and the interesting there's a lot of interesting things about that
*  image and I think Andre highlighted a bunch of things about the image that us humans are
*  able to immediately understand like the idea I think of gravity and that you can you have the
*  concept of a weight you have a you immediately project because of our knowledge of pose and how
*  human bodies are constructed you understand how the forces are being applied with the human body
*  the really interesting other thing that you're able to understand there's multiple people looking
*  at each other in the image you're able to have a mental model of what the people are thinking
*  about you're able to infer like oh this person is probably thinks like is laughing at how humorous
*  the situation is and this person is confused about what the situation is because they're looking this
*  able to infer all of that so that's human vision how difficult is computer vision like in order to
*  achieve that level of understanding and maybe how big of a part does self-supervised learning play
*  in that do you think and do you still you know back that was like over a decade ago I think Andre
*  and I think a lot of people agreed as computer vision is really hard do you still think computer
*  vision is really hard I think it is yes and getting to that kind of understanding I mean
*  it's really out there so if you ask me to solve just that particular problem I can do it the
*  supervised learning route I can always construct a data set and basically predict oh is there humor
*  in this and of course I can do it actually that's a good question do you think you can
*  okay okay do you think you can do human supervised annotation of humor to some extent yes I'm sure it
*  will work I mean it won't be it won't be as bad as like randomly guessing I'm sure it can still
*  predict whether it's humorous or not in some way yeah maybe like reddit upvotes is the signal I
*  don't know I mean it won't do a great job but it'll do something it may actually be like it may find
*  certain things which are not humorous humorous as well which is going to be bad for us but
*  I mean it'll do it won't be random yeah kind of like my sense of humor okay so fine so you can
*  that particular problem yes but the general problem you're saying is hard the general problem
*  is hard and I mean self-supervised learning is not the answer to everything of course it's not I think
*  if you have machines that are going to communicate with humans at the end of it you want to understand
*  what the algorithm is doing right you want it to be able to like produce an output that you can
*  decipher that you can understand or it's actually useful for something else which again is a human
*  so at at some point in this sort of entire loop a human steps in and now this human needs to
*  understand what's going on so and at that point this entire notion of language or semantics really
*  comes in if the machine just spits out something and if we can't understand it then it's not really
*  that useful for us so self-supervised learning is probably going to be useful for a lot of the
*  things before that part before the machine really needs to communicate a particular kind of output
*  with a human because I mean otherwise how is it going to do that without language or some kind of
*  communication but you're saying that it's possible to build a big base of understanding or whatever of
*  what's the better of concepts like common sense concepts supervised learning in the
*  context of computer vision is something you focused on but that's a really hard domain and
*  it's kind of the cutting edge of what we're as a community working on today can we take a little
*  bit of a step back and look at language can you summarize the history of success of self-supervised
*  learning in natural language processing language modeling what are transformers what is the masking
*  the sentence completion that you mentioned before how does it lead us to understand anything semantic
*  meaning of words syntactic role of words and sentences so i'm of course not the expert in
*  nlp i kind of follow it a little bit from the sides so the main sort of reason why all of this
*  masking stuff works is i think it's called the distributional hypothesis in nlp the idea basically
*  being that words that occur in the same context should have similar meaning so if you have the
*  blank jumped over the blank it basically whatever is like in the first blank is basically an object
*  that can actually jump is going to be something that can jump so a cat or a dog or i don't know
*  sheep something all of these things can basically be in that particular context and now so essentially
*  the idea is that if you have words that are in the same context and you predict them you're going
*  to learn lots of useful things about how words are related because you're predicting by looking at
*  their context what the word is going to be so in this particular case the blank jumped over the
*  fence so now if it's a sheep the sheep jumped over the fence the dog jumped over the fence so
*  essentially the algorithm or the representation basically puts together these two concepts
*  together so it says okay dogs are going to be kind of related to sheep because both of them occur in
*  the same context of course now you can decide depending on your particular application downstream
*  you can say that dogs are absolutely not related to sheep because well i don't i really care about
*  you know dog food for example i'm a dog food person and i really want to give this dog food
*  to this particular animal so depending on what your downstream application is of course this
*  notion of similarity or this notion or this common sense that you've learned may not be applicable
*  but the point is basically that this just predicting what the blanks are is going to take
*  you really really far so there's a nice feature of language that the number of words in a particular
*  language is very large but it's finite and it's actually not that large in the grand scheme of
*  things i i still got it because we take it for granted so first of all when you say masking
*  you're talking about this very process of the blank of removing words from a sentence and then
*  having the knowledge of what word went there in the initial data set that's the ground truth that
*  you're training on and then you're asking the neural network to predict what goes there
*  that that's that's like a little trick it's a really powerful trick the question is how far that
*  takes us and the other question is is there other tricks because to me it's very possible there's
*  other very fascinating tricks i'll give you an example in um in autonomous driving there's a
*  bunch of tricks that give you the self-supervised signal back for example i'm very similar to
*  sentences but not really which is you have signals from humans driving the car because a lot of us
*  drive cars to places and so you can ask the neural network to predict what's going to happen the next
*  two seconds for a safe navigation through the environment and the and the signal is comes from
*  the fact that you also have knowledge of what happened in the next two seconds because you have
*  video of the data the question in autonomous driving as it is in language can we learn
*  how to drive autonomously based on that kind of self-supervision probably the answer is no
*  the question is how good can we get and the same with language how good can we get and are there
*  other tricks like we get sometimes super excited by this trick that works really well but i wonder
*  it's almost like mining for gold i wonder how many signals there are in the data that could be
*  leveraged that are like there right is is that um i just wanted to kind of linger on that because
*  sometimes it's easy to think that maybe this masking process is self-supervised learning
*  no it's only one method so there could be many many other methods many tricky
*  methods maybe interesting ways to leverage human computation in very interesting ways that might
*  actually border on semi-supervised learning something like that obviously the internet is
*  generated by humans at the end of the day so all that to say is what's your sense in this
*  particular context of language how far can that masking process take us so it has stood the test
*  of time right i mean so word2vec the initial sort of nlp technique that was using this to now for
*  example like all the BERT and all these big models that we get BERT and ROBERTA for example all of
*  them are still sort of based on the same principle of masking it's taken us really far i mean you can
*  actually do things like oh these two sentences are similar or not whether this particular sentence
*  follows this other sentence in terms of logic so entailment you can do a lot of these things with
*  this just this masking trick yeah so i'm not sure if i can predict how how far it can take us because
*  like when it first came out when like word2vec was out i don't think a lot of us would have imagined
*  that this would actually help us do some kind of like entailment problems and really that well
*  and so just the fact that by just scaling up the amount of data that we're training on and like
*  using better and more powerful neural network architectures has taken us from that to this is
*  just showing you how maybe poor predictors we are like as humans how poor we are at predicting how
*  successful a particular technique is going to be so i think i can say something now but like 10
*  years from now i look completely stupid basically predicting this in language domain is there
*  something in your work that you find useful and insightful and and transferable to computer vision
*  but also just i don't know beautiful and profound that i think carries through to the vision domain
*  i mean the idea of masking has been very powerful it has been used in vision as well
*  for predicting like you say the next sort if you have and sort of frames and you predict what's
*  going to happen in the next frame so that's been very powerful in terms of modeling like in just
*  terms in terms of architecture i think you would have asked about transformers a while back that
*  has really become like it has become super exciting for computer vision now like in the past i would
*  say a year and a half it's become really powerful what's the transformer right i mean the core part
*  of a transformer is something called the self-attention model so it came out of google
*  and the idea basically is that if you have n elements what you're creating is a way for all
*  of these n elements to talk to each other so the idea basically is that you are paying attention
*  each element is paying attention to each of the other element and basically by doing this it's
*  really trying to figure out you're basically getting a much better view of the data so for
*  example if you have a sentence of like four words the point is if you get a representation or a
*  feature for this entire sentence it's constructed in a way such that each word has paid attention to
*  everything else now the reason it's like different from say what you would do in a conf net is
*  basically that in the content you would only pay attention to a local window so each word would
*  only pay attention to its next neighbor or like one neighbor after that and the same thing goes
*  for images and images you would basically pay attention to pixels in a three cross three or a
*  seven cross seven neighborhood and that's it whereas with the transformer the self-attention
*  mainly the sort of idea is that each element needs to pay attention to each other element and when
*  you say attention maybe another way to phrase that is you're considering a context a wide context
*  in terms of the wide context of the sentence in understanding the meaning of a particular word
*  and in computer vision that's understanding a larger context to understand the the local pattern
*  of a particular local part of an image right so basically if you have say again a banana in the
*  image you're looking at the full image first so whether it's like you know you're looking at all
*  the pixels that are of a kitchen of a dining table and so on and then you're basically looking at the
*  banana also yeah by the way in terms of if we were to train the funny classifier there's something
*  funny about the word banana just going to anticipate that my my i am wearing a banana shirt so yeah is
*  this bananas on it okay so masking has worked for the vision context as well and so this
*  transformer idea has worked as well so basically looking at all the elements to understand a
*  particular element has been really powerful in vision the reason is like a lot of things
*  when you're looking at them in isolation so if you look at just a blob of pixels so antonio
*  terralba at mit used to have this like really famous image which i looked at when i was a
*  phd student where he would basically have a blob of pixels and he would ask you hey what is this
*  and it looked basically like a shoe or like it could look like a tv remote it could look like
*  anything and it turns out it was a beer bottle but i'm not sure it was one of these three things
*  but basically he showed you the full picture and then it was very obvious what it was but the point
*  is just by looking at that particular local window you couldn't figure it out yeah because of
*  resolution because of other things it's just not easy always to just figure it out by looking at
*  just the neighborhood of pixels what these pixels are yeah and the same thing happens for language
*  for the parameters that have to learn something about the data you need to give it the capacity
*  to learn the essential things like if it's not actually able to receive the signal at all
*  then it's not going to be able to learn that signal and to in order to understand images
*  to understand language you have to be able to see words in their full context okay what is
*  harder to solve vision or language visual intelligence or linguistic intelligence so i'm
*  going to say computer vision is harder my reason for this is basically that language of course has
*  a big structure to it because we developed it whereas vision is something that is common in a
*  lot of animals everyone is able to get by a lot of these animals on earth are actually able to get
*  by without language and a lot of these animals we also deem to be intelligent so clearly intelligence
*  does have like a visual component to it and yes of course in the case of humans it of course also
*  has a linguistic component but it means that there is something far more fundamental about vision than
*  there is about language and i'm sorry to anyone who disagrees but yes this is what i feel so that's
*  being a little bit reflected in the challenges that have to do with the the progress of self-supervised
*  learning would you say or is that just the peculiar accidents of the progress of the ai community that
*  we focused on like or we discovered self-attention and transformers in the context of language first
*  so like the self-supervised learning success was actually for vision has not much to do with the
*  transformers part i would say it's actually been independent a little bit i think it's just that
*  the signal was a little bit different for vision than there was for like nlp and probably nlp
*  yeah folks discovered it before so for vision the main success has basically been this like crops
*  so far like taking different crops of images whereas for nlp it was this masking thing but also
*  the level of success is still much higher for language it has so that has a lot to do with
*  i mean i can get into a lot of details for this particular question let's go for it okay so
*  the first thing is language is very structured so you are going to produce a distribution over
*  a finite vocabulary english has a finite number of words it's actually not that large
*  and you need to produce basically when you're doing this masking thing all you need to do is
*  basically tell me which one of these like 50 000 words it is yeah that's it now for vision let's
*  imagine doing the same thing okay we're basically going to blank out a particular part of the image
*  and we ask the network or this neural network to predict what is present in this missing patch
*  it's combinatorially large right you have 256 pixel values if you're even producing basically
*  a seven cross seven or a 14 cross 14 like window of pixels at each of these 169 or each of these
*  49 locations you have 256 values to predict yeah and so it's really really large and very quickly
*  the kind of like prediction problems that we are setting up are going to be extremely like
*  intractable for us and so the thing is for nlp it has been really successful because we are very
*  good at predicting like doing this like distribution over a finite set and the problem is when this set
*  becomes really large we are going to become really really bad at making these predictions
*  and at solving basically this particular set of problems so if you were to do it exactly in this
*  same way as nlp for vision there is very limited success the way stuff is working right now is
*  actually not by predicting these masks it's basically by saying that you take these two
*  like crops from the image you get a feature representation from it and just saying that
*  these two features so they're like vectors just saying that the distance between these vectors
*  should be small and so it's a very different way of learning from the visual signal than there is
*  from nlp okay the other reason is the distributional hypothesis that we talked about for nlp right so
*  a word given its context basically the context actually supplies a lot of meaning to the word
*  now because there are just finite number finite number of words and there is a finite way in like
*  which we compose them of course and the same thing holds for pixels but in language there's a lot of
*  structure right so i always say whatever the dash jumped over the fence for example there are lots
*  of these sentences that you'll get and from this you can actually look at this particular sentence
*  might occur in a lot of different contexts as well this exact same sentence might occur in a
*  different context so the sheep jumped over the fence the cat jumped over the fence the dog jumped
*  over the fence so you immediately get a lot of these words which are because this particular
*  token itself has so much meaning you get a lot of these tokens or these words which are actually
*  going to have a have sort of this related meaning across given this context whereas for vision it's
*  much harder because just by like pure like the way we capture images lighting can be different
*  there might be like different noise in the sensor so the thing is you're capturing a physical
*  phenomenon and then you're basically going through a very complicated pipeline of like
*  image processing and then you're translating that into some kind of like digital signal
*  whereas with language you write it down and you transfer it to a digital signal almost like it's
*  a lossless like transfer and each of these tokens are very very well defined there could be a little
*  bit of an argument there because language as written down is a projection of thought
*  this is one of the open questions is if you perfectly can solve language
*  are you getting close to being able to solve you know easily with flying colors past the
*  touring test kind of thing so that's it's similar but different and the computer vision problem is
*  in the 2d plane is a projection with three-dimensional world so perhaps there
*  are similar problems there maybe this i mean i think what i'm saying is nlp is not easy of
*  course don't get me wrong like abstract thought expressed in knowledge or knowledge basically
*  expressed in language is really hard to understand right i mean we've been communicating with language
*  for so long and it's it is of course a very complicated concept the thing is at least
*  getting like some somewhat reasonable like being able to solve some kind of reasonable tasks with
*  language i would say slightly easier than it is with computer vision yeah i would say yeah so
*  that's well put i would say getting impressive performance on language is easier that i feel
*  like for both language and computer vision there's going to be this wall of like that you like uh
*  this hump you have to overcome to achieve superhuman level performance or human level
*  performance and i feel like for language that wall is farther away so you can get pretty nice
*  you can do a lot of tricks you can show really impressive performance you can even fool people
*  that you're tweeting or you're right blog post writing or your question answering is has
*  intelligence behind it but to truly demonstrate understanding of dialogue
*  of continuous long-form dialogue that would require perhaps big breakthroughs in the same
*  way in computer vision i think the big breakthroughs need to happen earlier to to achieve impressive
*  performance this might be a good place to you already mentioned it but what is contrastive
*  learning and what are energy-based models contrastive learning is sort of the paradigm
*  of learning where the idea is that you are learning this embedding space or so you're
*  learning this sort of vector space of all your concepts and the way you learn that is basically
*  by contrasting so the idea is that you have a sample you have another sample that's related
*  to it so that's called the positive and you have another sample that's not related to it so that's
*  negative so for example let's just take an nlp or what in a simple example in computer vision so
*  you have an image of a cat you have an image of a dog and for whatever application that you're
*  doing say you're trying to figure out what pets are you think that these two images are related
*  so image of a cat and dog are related but now you have another third image of a banana because
*  you don't like that word so now you basically have this banana thank you for speaking to the crowd
*  and so you take both of these images and you take the image from the cat the image from the dog you
*  get a feature from both of them and now what you're training the network to do is basically
*  pull both of these features together while pushing them away from the feature of a banana
*  so this is the contrastive part so you're contrasting against the banana so there's
*  always this notion of a negative and a positive now energy-based models are like like one way that
*  yan sort of explains a lot of these methods so yan basically i think a couple of years or more
*  than that like when i joined facebook yan used to keep mentioning this word energy-based models
*  and of course i had no idea what he was talking about so then one day i caught him in one of the
*  conference rooms and i'm like can you please tell me what this is so then like very patiently he
*  sat down with like a marker and a whiteboard and his idea basically is that rather than talking
*  about probability distributions you can talk about energies of models so models are trying to minimize
*  certain energies in certain space or they're trying to maximize a certain kind of energy
*  and the idea basically is that you can explain a lot of the contrastive models
*  gans for example which are like generative adversarial networks a lot of these modern
*  learning methods or vaes which are variational autoencoders you can really explain them very
*  nicely in terms of an energy function that they're trying to minimize or maximize and so by putting
*  this common sort of language for all of these models what looks very different in machine
*  learning that oh vaes are very different from what gans are are very very different from what
*  contrastive models are you actually get a sense of like oh these are actually very very related
*  it's just that the way or the mechanism in which they're sort of maximizing or minimizing
*  this energy function is slightly different it's revealing the the commonalities between all these
*  approaches and putting a sexy word on top of it like energy and so similarities two things that
*  are similar have low energy like the low energy signifying similarity right exactly so basically
*  the idea is that if you were to imagine like the embedding as a manifold a 2d manifold you would
*  get a hill or like a high sort of peak in the energy manifold wherever two things are not
*  related and basically you would have like a dip where two things are are related so you would get
*  a dip in the manner and in the self-supervised context how do you know two things are related
*  and two things are not related right so this is where all the sort of ingenuity or tricks comes
*  in right so for example like you can take the fill in the blank problem or you can take in the
*  context problem and what you can say is two words that are in the same context are related
*  two words that are in different contexts are not related for images basically two crops from the
*  same image are related and whereas a third image is not related at all for a video it can be two
*  frames from that video related because they're likely to contain the same sort of concept in
*  them whereas a third frame from a different video is not related so it basically is it's a very
*  general term contrasted learning is nothing really to do with self-supervised learning it actually is
*  very popular in for example like any kind of metric learning or any kind of embedding learning
*  so it's also used in supervised learning it's also and the thing is because we are not really
*  using labels to get these positive or negative pairs it can basically also be used for self-supervised
*  learning so you mentioned one of the ideas in the vision context to that works is to have different
*  crops so you could think of that as a way to sort of manipulating the data to generate
*  examples that are similar obviously there's a bunch of other techniques you mentioned lighting
*  as a very you know in images lighting is something that varies a lot and you can artificially
*  change those kinds of things there's the whole broad field of data augmentation
*  which manipulates images in order to increase arbitrarily the size of the data set first of all
*  what is data augmentation and second of all what's the role of data augmentation in
*  self-supervised learning and contrasted learning so data augmentation is just a way like you said
*  it's basically a way to augment the data so you have say n samples and what you do is you basically
*  define some kind of transforms for the sample so you take your say image and then you define a
*  transform where you can just increase say the colors like the colors or the brightness of the
*  image or increase or decrease the contrast of the image for example or take different crops of it
*  so data augmentation is just a process to like basically perturb the data or like augment the
*  data right and so it has played a fundamental role for computer vision for self-supervised
*  learning especially the way most of the current methods work contrastive or otherwise is by
*  taking an image in the case of images is by taking an image and then computing basically two
*  perturbations of it so these can be two different crops of the image with like different types of
*  lighting or different contrast or different colors so you jitter the colors a little bit and so on
*  and now the idea is basically because it's the same object or because it's like related concepts
*  in both of these perturbations you want the features from both of both of these perturbations
*  to be similar so now you can use a variety of different ways to enforce this constraint like
*  these features being similar you can do this by contrastive learning so basically both of
*  these things are positives a third sort of image is negative you can do this basically by like
*  clustering for example you can say that both of these images should the features from both of
*  these images should belong in the same cluster because they're related whereas image like another
*  image should belong to a different cluster so there's a variety of different ways to basically
*  enforce this particular constraint by the way when you say features it means there's a very large
*  neural network that extracting patterns from the image and the kind of patterns that extracts should
*  be either identical or very similar right that's what that means so the neural network basically
*  takes in the image and then outputs a set of like basically a vector of like numbers and that's the
*  feature and you want this feature for both of these like different crops that you computed to
*  be similar so you want this vector to be identical in its like entries for example be like literally
*  close in this multi-dimensional space to each other right and like you said close can mean part
*  of the same cluster or something like that in this large space first of all that i wonder if
*  there is connection to the way humans learn to this almost like maybe subconsciously in order
*  to understand the thing you kind of have to see it from two three multiple angles i wonder there's a
*  lot of friends who are neuroscientists maybe working and cognitive scientists i wonder if that's in
*  there somewhere like in order for us to place a concept in its proper place we have to basically
*  crop it in all kinds of ways do basic data augmentation on it in whatever very clever
*  ways that the brain likes to do right like spinning around in our mind somehow that that is very
*  effective so i think for some of them we like need to do it so like babies for example pick up objects
*  move them and put them goes with your eye and whatnot but for certain other things actually we
*  are good at imagining it as well right so if you i have never seen for example an elephant from the
*  top i've never basically looked at it from like top down yeah but if you showed me a picture of
*  it i could very well tell you that that's an elephant so i think some of it would just like
*  be naturally built it or transfer it from other objects that we've seen to imagine what it's going
*  to look like has anyone done that with the augmentation like imagine all the possible
*  things that are occluded or not there but not just like normal things like wild things but
*  they're nevertheless physically consistent so i mean people do kind of like occlusion based
*  augmentation as well so you place in like a random like box gray box to sort of mask out a certain
*  part of the image and the thing is basically you're kind of occluding it for example you
*  place it say on half of a person's face so basically saying that you know something below
*  their nose is occluded because it's grayed out so you know i meant like you have like what is it a
*  table and you can't see behind the table and you imagine there's a bunch of elves with bananas
*  behind the table like i wonder if there's useful to have a wild imagination for the network because
*  that's possible well maybe not elves but like puppies and kittens or something like that
*  just have a wild imagination and like constantly be generating that wild imagination because in
*  in terms of data augmentation that's currently applied it's super ultra very boring it's very
*  basic data augmentation i wonder if i wonder if there's a benefit to being wildly imaginable
*  while trying to be consistent with physical reality i think it's a kind of a chicken and egg
*  problem right because to have like amazing data augmentation you need to understand what the scene
*  is right and what we're trying to do data augmentation to learn what a scene is anyway
*  so it's basically just keeps going on before you understand it just put elves with bananas until
*  until you know it's not to be true just like children have a wild imagination until the adults
*  ruin it all okay so what are the different kinds of data augmentation that you seem to be effective
*  in visual intelligence for like vision it's a lot of these image filtering operations so like
*  blurring the image you know all the kind of instagram filters that you can think of
*  so like arbitrarily like make the red super red make the green super greens like saturate the image
*  rotation cropping rotation cropping exactly all of these kind of things like you said
*  lighting is a really interesting one yes to me like that feels like really complicated to do
*  i mean they don't the augmentations that we work on aren't like that involves that they're not
*  going to be like physically realistic versions of lighting it's not that you're assuming that
*  there's a light source up and then you're moving it to the right and then what does the thing look
*  like it's really more about like brightness of the image overall brightness of the image or overall
*  contrast of the image and so on but this is a really important point to me i always thought
*  that data augmentation holds an important key to big improvements in machine learning
*  and it seems that it is an important aspect of self-supervised learning so i wonder if there's
*  big improvements to be achieved on much more intelligent kinds of data augmentation
*  for example currently maybe you can correct me if i'm wrong data augmentation is not parameterized
*  yeah you're not learning you're not learning to me it seems like data augmentation potentially
*  should involve more learning than the learning process itself right you're almost like thinking
*  of like generative kind of it's the elves with bananas you're trying to it's like very active
*  imagination of messing with the world and teaching that mechanism for messing with the world to be
*  realistic right because that feels like i mean it's imagination it's just as you said it things it
*  feels like us humans are able to um maybe sometimes subconsciously imagine before we see the thing
*  imagine what we're expecting to see like maybe several options and especially we probably forgot
*  but when we're younger probably the possibilities were wild they're more numerous and then as we
*  get older we become to understand the world and uh the possibilities of what we might see becomes
*  less and less and less so i wonder if if you think there's a lot of breakthroughs yet to be
*  had in data augmentation and maybe also can you just comment on the stuff we have is that a big
*  part of self-supervised learning yes so data augmentation is like key to self-supervised
*  learning that has like the kind of augmentation that we're using and basically this the fact that
*  we're trying to learn these neural networks that are predicting these features from images that are
*  robust under data augmentation has been the key for visual self-supervised learning and they play
*  a fairly fundamental role to it now the irony of all of this is that for like deep learning
*  purists will say the entire point of deep learning is that you feed in the pixels to the network
*  neural network and it should figure out the patterns on its own so if it really wants to
*  look at edges it should look at edges you shouldn't really like really go and handcraft these tech
*  features right you shouldn't go tell it that look at edges so data augmentation should basically be
*  in the same category right why should we tell the network or tell this entire learning paradigm
*  what kinds of data augmentation that we are looking for we are encoding a very sort of
*  human specific bias there that we know things are like if you change the contrast of the image
*  it should still be an apple or it should still see apple not banana thank you basically if we
*  change like colors it should still be the same kind of concept yes of course this is not one this is
*  doesn't feel like super satisfactory because a lot of our human knowledge or our human supervision
*  is actually going into the data augmentation so although we are calling it self-supervised
*  learning a lot of the human knowledge is actually being encoded in the data augmentation process
*  so it's really like we've kind of sneaked away the supervision at the input and we're like really
*  designing these nice list of data augmentations that are working very well of course the idea is
*  that it's much easier to design a list of data augmentation that it is to do so humans are doing
*  nevertheless doing less and less work and maybe leveraging their creativity more and more and
*  when we say data augmentation is not parameterized it means it's not part of the learning process
*  do you think it's possible to integrate some of the data augmentation into the learning process
*  i think so i think so and in fact it will be really beneficial for us because a lot of these
*  data augmentations that we use in vision are very extreme for example like when you have certain
*  concepts again a banana you take the banana and then basically you change the color of the banana
*  right so you make it a purple banana now this data augmentation process is actually independent of
*  it has no notion of what is present in the image so it can change this color arbitrarily it can
*  make it a red banana as well and now what we're doing is we're telling the neural network that
*  this red banana and so a crop of this image which has the red banana and a crop of this image where
*  i change the color to a purple banana should be the features should be the same now bananas aren't
*  red or purple mostly so really the data augmentation process should take into account what is present in
*  the image and what are the kinds of physical realities that are possible it shouldn't be
*  completely independent of the image so you might get big gains if you instead of being drastic do
*  subtle augmentation but realistic augmentation right realistic i'm not sure if it's subtle but
*  like realistic for sure if it's realistic then even subtle augmentation will give you big benefits
*  exactly yeah and it will be like for particular domains you might actually see like if for example
*  now we're doing medical imaging there are going to be certain kinds of like geometric augmentation
*  which are not really going to be very valid for the human body so if you were to like actually
*  loop in data augmentation into the learning process it will actually be much more useful
*  now this actually does take us to maybe a semi-supervised kind of a setting because
*  you do want to understand what is it that you're trying to solve so currently self-supervised
*  learning kind of operates in the wild right so you do the self-supervised learning you read and the
*  purists and all of us basically say that okay this should learn useful representations and they should
*  be useful for any kind of end task no matter it's like banana recognition or like autonomous driving
*  now it's a tall order maybe the first baby step for us should be that okay if you're trying to
*  loop in this data augmentation into the learning process then we at least need to have some sense
*  of what we're trying to do are we trying to distinguish between different types of bananas
*  or are we trying to distinguish between banana and apple or are we trying to do all of these
*  things at once and so some notion of like what happens at the end might actually help us do much
*  better at this side let me ask you a ridiculous question if i were to give you like a black box
*  like a choice to have an arbitrary large data set of real natural data versus really good
*  data augmentation algorithms which would you like to train in a self-supervised way on so natural
*  data from the internet are arbitrarily large so unlimited data or it's like more controlled
*  good data augmentation on the finite data set the thing is like because our learning algorithms
*  for vision right now really rely on data augmentation even if you were to give me
*  like an infinite source of like image data i still need a good data augmentation you need
*  something that tells you that two things are similar right and so something because you've
*  given me an arbitrarily large data set i still need to use data augmentation to take that image
*  construct like these two perturbations of it and then learn from it so the thing is our learning
*  paradigm is very primitive right now even if you were to give me a lots of images it's still not
*  really useful a good data augmentation algorithm is actually going to be more useful so you can like
*  reduce down the amount of data that you give me by like 10 times but if you were to give me a good
*  data augmentation algorithm that will probably do better than giving me like 10 times the size of
*  that data but me having to rely on like a very primitive data augmentation algorithm like through
*  tagging and all those kinds of things is there a way to discover things that are semantically
*  similar on the internet obviously there is but they might be extremely noisy and the difference
*  might be farther away than you would be comfortable with so i mean yes tagging will help you a lot it
*  will actually go a very long way in figuring out what images are related or not and then so but then
*  the purists would argue that when you're using human tags because these tags are like supervision
*  is it really really self-supervised learning now because you're using human tags to figure out which
*  images are like similar hashtag no filter means a lot of things yes i mean there are certain tags
*  which are going to be applicable pretty much to anything so they're pretty useless for learning
*  yeah but i mean certain tags are actually like the i filter for example or the Taj Mahal for example
*  these tags are like very indicative of what's going on and they are i mean they are human
*  supervision yeah this is one of the tasks of discovering from human generated data strong
*  signals that could be leveraged for self-supervision like humans are doing so much work already
*  like many years ago there was something that was called i guess human computation back in the day
*  humans are doing so much work it would be exciting to discover ways to leverage the work they're
*  doing to teach machines without any extra effort from them an example could be like we said driving
*  humans driving and machines can learn from the driving i always hope that there could be some
*  supervision signal discovered in video games because there's so many people that play video
*  that it feels like so much effort is put into video games but into playing video games
*  and you can design video games somewhat cheaply right to include whatever signals you want it
*  feels like uh that could be leveraged somehow so people are using that like there are actually
*  folks right here in ut austin like philip grahan bull is a professor at ut austin he's been like
*  working on video games as a source of supervision i mean it's it's really fun like as a phd student
*  getting to basically play video games all day yeah but so i do hope that kind of thing scales and
*  like ultimately boils down to discovering some undeniably very good signal it's like masking in
*  nlp but that said there's non-contrastive methods right what do non-contrastive energy-based
*  self-supervised learning methods look like and why are they promising so like i said about
*  contrastive learning you have this notion of a positive and a negative now the thing is
*  this entire learning paradigm really requires access to a lot of negatives to learn a good sort
*  of feature space the idea is if i tell you uh okay so a cat and a dog are similar and they're very
*  different from a banana the thing is this is a fairly simple analogy right because well bananas
*  look visually very different from what cats and dogs do so very quickly if this is the only source
*  of supervision that i'm giving you your learning is not going to be like after a point the neural
*  network is really not going to learn a lot because the negative that you're getting is going to be
*  so random so it can be oh a cat and a dog are very similar but they're very different from
*  a volkswagen beetle now like this car looks very different from these animals again so
*  the thing is in contrast to learning the quality of the negative sample really matters a lot
*  and so what has happened is basically that typically these methods that are contrastive
*  really require access to lots of negatives which becomes harder and harder to sort of scale when
*  designing a learning algorithm so that's been one of the reasons why non-contrastive methods
*  have become like popular and why people think that they're going to be more useful so a non-
*  contrastive method for example like clustering is one non-contrastive method the idea basically
*  being that you have two these two of these samples so the cat and dog are two crops of this image
*  they belong to the same cluster and so essentially you're basically doing clustering online when
*  you're learning this network and which is very different from having access to a lot of negatives
*  explicitly the other way which has become really popular is something called self-distillation
*  so the idea basically is that you have a teacher network and a student network
*  and the teacher network produces a feature so it takes in the image and basically the neural
*  network figures out the patterns gets the feature out and there's another neural network which is
*  the student neural network and that also produces a feature and now all you're doing is basically
*  saying that the features produced by the teacher network and the student network should be very
*  similar that's it there is no notion of a negative anymore and that's it so it's all about similarity
*  maximization between these two features and so all I need to now do is figure out how to have these
*  two sorts of parallel networks a student network and a teacher network and basically researchers
*  have figured out very cheap methods to do this so you can actually have for free really two types
*  of neural networks they're kind of related but they're different enough that you can actually
*  basically have a learning problem set up so you can ensure that they always remain different enough
*  so the thing doesn't collapse into something boring exactly so the main sort of enemy of
*  self-supervised learning any kind of similarity maximization technique is collapse it's a collapse
*  means that you learn the same feature representation for all the images in the world
*  which is completely useless everything is a banana everything is a banana everything is a cat
*  everything is a car yeah and so all we need to do is basically come up with ways to prevent collapse
*  contrastive learning is one way of doing it and then for example like clustering or self-distillation
*  or other ways of doing it we also had a recent paper where we used like de-correlation between
*  like two sets of features to prevent collapse so that's inspired a little bit by like Horace
*  Barlow's neuroscience principles by the way i should comment that whoever counts the number
*  of times than the word banana apple cat and dog were using this conversation wins the internet
*  i wish you luck what uh what is suave and and the main improvement proposed in the paper on
*  supervised learning of visual features by contrasting cluster assignments
*  suave basically is a clustering based technique which is for again the same thing for self-supervised
*  learning in vision where we have two crops and the idea basically is that you want the features
*  from these two crops of an image to lie in the same cluster and basically crops that are coming
*  from different images to be in different clusters now typically in a sort of if you were to do this
*  clustering you would perform clustering offline what that means is you would if you have a data
*  set of n examples you would run over all of these n examples get features for them perform
*  clustering so basically get some clusters and then repeat the process again so this is offline
*  basically because i need to do one pass through the data to compute its clusters suave is basically
*  just a simple way of doing this online so as you're going through the data you're actually
*  computing these clusters online and so of course there is like a lot of tricks involved in how to
*  do this in a robust manner without collapsing but this is this sort of key idea to it is there a
*  nice way to say what is the key methodology of the clustering that enables that right so the idea
*  basically is that when you have n samples we assume that we have access to like there are always k
*  clusters in a data set k is a fixed number so for example k is 3000 and so if you have any
*  when you look at any sort of small number of examples all of them must belong to one of these
*  k clusters and we impose this equi partition constraint what this means is that basically
*  your entire set of n samples should be equally partitioned into k clusters so all your k clusters
*  are basically equal they have equal contribution to these n samples and this ensures that we never
*  collapse so collapse can be viewed as a way in which all samples belong to one cluster right so
*  if all features become the same then you have basically just one mega cluster you don't even
*  have like 10 clusters or 3000 clusters so suave basically ensures that at each point all these
*  3000 clusters are being used in the clustering process and that's it basically just figure out
*  how to do this online and again basically just make sure that two crops from the same image
*  belong to the same cluster and others don't and the fact they have a fixed k makes things simpler
*  fixed k makes things simpler our clustering is not like really hard clustering it's soft clustering
*  so basically you can be point two to cluster number one and point eight to cluster number two so
*  it's not really hard so essentially even though we have like 3000 clusters we can actually
*  represent a lot of clusters what is seer and what are the key results and insights in the paper
*  self-supervised pre-training of visual features in the wild what is this big beautiful seer system
*  seer so i'll first go to suave because suave is actually like one of the key components for seer
*  so suave was when we used suave it was demonstrated on image net so typically like
*  self-supervised methods the way we sort of operate is like in the research community we kind of cheat
*  so we take image net which of course i talked about as having lots of labels and then we throw
*  away the labels like throw away all the hard work that went behind basically the labeling process
*  and we pretend that it is self like unsupervised but the problem here is that we have when like
*  when we collected these images the image net data set has a particular distribution of concepts
*  right so these images are very curated and what that means is these images of course belong to a
*  certain set of noun concepts and also image net has this bias that all images contain an object
*  which is like very big and it's typically in the center so when you're talking about a dog it's a
*  well-framed dog it's towards the center of the image so a lot of the data augmentation a lot of
*  the sort of hidden assumptions in self-supervised learning actually really exploit this bias of
*  image net and so i mean a lot of my work a lot of work from other people always uses image net sort
*  of as the benchmark to show the success of self-supervised learning so you're implying
*  that there's particular limitations to this kind of data set yes i mean it's basically because
*  our data augmentations that we designed like in the like all data augmentations that we designed
*  for self-supervised learning and vision are kind of overfed to image net but you're saying a little
*  bit hard coded like the cropping exactly the cropping parameters the kind of lighting that
*  we're using the kind of blurring that we're using yeah but you would for a more in the wild data
*  set you would need to be clever or more careful in setting the range of parameters and those kinds
*  of things so for seer our main goal was twofold one basically to move away from image net for
*  training so the images that we used were like uncurated images now there's a lot of debate
*  whether they're actually curated or not but i'll talk about that later but the idea was basically
*  these are going to be random internet images that we are not going to filter out based on like
*  particular categories so we did not say that oh images that belong to dogs and cats should be the
*  only images that come in this data set banana and basically other images should be thrown out so we
*  didn't do any of that so these are random internet images and of course it also goes back to like the
*  problem of scale that you talked about so these were basically about a billion or so images and
*  for context image net the image net version that we use was one million images earlier so this is
*  basically going like three orders of magnitude more the idea was basically to see if we can train
*  a very large convolutional model in a self-supervised way on this uncurated but really
*  large set of images and how well would this model do so is self-supervised learning really overfit
*  to image net or or can it actually work in the wild and it was also out of curiosity what kind
*  of things will this model learn will it actually be able to still figure out you know different
*  types of objects and so on would there be particular kinds of tasks it would actually
*  do better than an image net train model and so for seer one of our main findings was that
*  we can actually train very large models in a completely self-supervised way on lots of
*  internet images without really necessarily filtering them out which was in itself a good
*  thing because it's a fairly simple process right so you get images which are uploaded and you
*  basically can immediately use them to train a model in an unsupervised way you don't really
*  need to sit and filter them out these images can be cartoons these can be memes these can be actual
*  pictures uploaded by people and you don't really care about what these images are you don't even
*  care about what concepts they contain so this was a very sort of simple setup what image selection
*  mechanism would you say is there like inherent in some aspect of the process so you're kind of
*  implying it there's almost none but what what is there would you say if you want to change respect
*  right so it's not like uncurated can basically like one way of imagining uncurated is basically
*  you have like cameras of the cameras that can take pictures at random viewpoints when people
*  upload pictures to the internet they are typically going to care about the framing of it they're not
*  going to upload say the picture of a zoomed-in wall for example well when we say internet do
*  you mean social networks yes okay so these are not going to be like pictures of like a zoomed-in
*  table or a zoomed-in wall so it's not really completely uncurated because people do have the
*  like photographers bias where they do want to keep things towards the center a little bit or like
*  really have like you know nice looking things and so on in the picture so that's the kind of
*  bias that typically exists in this data set and also the user base right you're not going to get
*  lots of pictures from different parts of the world because there are certain parts of the world where
*  people may not actually be uploading a lot of pictures to the internet or may not even have
*  access a lot of internet so this is a giant data set and a giant neural network i don't think we've
*  talked about what architectures work well for ssl for self-supervised learning for seer and
*  for swap we were using convolutional networks but recently in a work called dino we've basically
*  started using transformers for vision both seem to work really well connets and transformers and
*  depending on what you want to do you might choose to use a particular formulation so for seer it was
*  a continent it was particularly a regnet model which was also a work from facebook regnets are
*  like really good when it comes to compute versus like accuracy so because it was a very efficient
*  model compute and memory wise efficient and basically it worked really well in terms of
*  scaling so we used a very large regnet model and train it on the building images can you maybe
*  quickly comment on what reg nets are it comes from this paper designing network design spaces
*  right it's just super interesting concept that emphasizes on how to create efficient neural
*  networks right large neural networks so one of the sort of key takeaways from this paper which
*  the authors like whenever you hear them present this work they keep saying is a lot of neural
*  networks are characterized in terms of flops right flops basically being the floating point operations
*  and people really love to use flops to say this model is like really computationally heavy or like
*  our model is computationally cheap and so on now it turns out that flops are really not a good
*  indicator of how well a particular network is like how efficient it is really and what a better
*  indicator is is the activation or the memory that is being used by this particular model and so
*  designing like one of the key findings from this paper was basically that you need to design
*  network families or neural network architectures that are actually very efficient in the memory
*  space as well not just in terms of pure flops so regnet is basically a network architecture
*  family that came out of this paper that is particularly good at both flops and the sort
*  of memory required for it and of course it builds upon like earlier work like resnet being like the
*  sort of more popular inspiration for it where you have residual connections but one of the things in
*  this work is basically they also use like squeeze excitation blocks so it's a lot of nice sort of
*  technical innovation in all of this from prior work and a lot of the ingenuity of these particular
*  authors in how to combine these multiple building blocks but the key constraint was optimized for
*  both flops and memory when you're basically doing this don't just look at flops and that allows you
*  to what have a sort of have very large networks through this process can optimize for low like
*  for efficiency right also in just in terms of pure hardware they fit very well on gpu memory
*  yeah so they can be like really powerful neural network architectures with lots of parameters
*  lots of flops but also because they're like efficient in terms of the amount of memory that
*  they're using you can actually fit a lot of these on like a you can fit a very large model
*  on a single gpu for example would you say that the choice of architecture matters more than the
*  choice of maybe data augmentation techniques is there a possibility to say what matters more
*  you kind of imply that you can probably go really far with just using basic conv nets all right i
*  think they talk like data and data augmentation the algorithm being used for the self-supervised
*  training matters a lot more than the particular kind of architecture with different types of
*  architecture you will get different like properties in the resulting sort of representation
*  but really i mean the secret sauce is in the data augmentation and the algorithm being used to train
*  them the architectures i mean at this point a lot of them perform very similarly depending on like
*  the particular task that you care about they have certain advantages and disadvantages is there
*  something interesting to be said about what it takes with seers to train a giant neural network
*  you're talking about a huge amount of data a huge neural network is there something interesting to
*  be said of how to effectively train something like that fast lots of gpos okay so i mean so the model
*  was like a billion parameters yeah uh and it was trained on a billion images yeah so if like
*  basically the same number of parameters as the number of images and it took a while uh i don't
*  remember the exact number it's in the paper uh but it took a while i guess i'm trying to get at is
*  uh when you're thinking of scaling this kind of thing i mean one of the exciting possibilities
*  of self-supervised learning is the several orders of magnitude scaling of everything
*  both both in your own network and the size of the data and so the question is do you think there
*  are some interesting tricks to do large-scale distributed compute or is it or is that really
*  outside of even deep learning that's more about like hardware engineering i think more and more
*  there is like this a lot of like systems are designed basically taking into account the
*  machine learning needs right so because when whenever you're doing this kind of distributed
*  training there is a lot of intercommunication between nodes so like gradients or the model
*  parameters are being passed so you really want to minimize communication costs when you really
*  want to scale these models up you want basically to be able to do as much like as limited amount
*  of communication as possible so currently like a dominant paradigm is synchronized sort of training
*  so essentially after every sort of gradient step all you basically have like a synchronization
*  step between all the sort of compute chips that you're going on with i think asynchronous training
*  was popular but it doesn't seem to perform as well but in general i think that's sort of the
*  i guess it's outside my scope as well yeah but the main thing is like minimize the amount of
*  synchronization steps that you have yeah that has been the key takeaway at least in my experience
*  the others i have no idea about how to design the chip yeah there's very few things that i see
*  jim keller's eyes light up as much as talking about giant computers doing
*  like that fast communication that you're talking to well when they're training machine learning
*  systems what is this all the i ssl the pi torch based ssl library what are the use cases that
*  you might have this will basically was born out of a lot of us at facebook are doing the self
*  supervised learning research so it's a common framework in which we have like a lot of self
*  supervised learning methods implemented for vision it's also it has in itself like a benchmark of
*  tasks that you can evaluate the self-supervised representations on so the use case for it is
*  basically for anyone who's either trying to evaluate their self-supervised model or train
*  their self-supervised model or a researcher who's trying to build a new self-supervised technique
*  so it's basically supposed to be all of these things so as a researcher before whistle for
*  example or like when we started doing this work fairly seriously at facebook it was very hard for
*  us to go and implement every self-supervised learning model test it out in a like sort of
*  consistent manner the experimental setup was very different across different groups even when
*  someone said that they were reporting image net accuracy it could mean lots of different things
*  so with whistle we tried to really sort of standardize that as much as possible
*  and it was a paper like we did in 2019 just about benchmarking and so whistle basically builds upon
*  a lot of this kind of work that we did about like benchmarking and then every time we try to like
*  we come up with a self-supervised learning method a lot of us try to push that into whistle as well
*  just so that it basically is like the central piece where a lot of these methods can reside
*  just out of curiosity like people maybe so certainly outside of facebook but just researchers
*  or just even people that know how to program in python and know how to use pytorch
*  what would be the use case what would be a fun thing to play around with whistle on like what's
*  a fun thing to play around with self-supervised learning on would you say is there a good hello
*  world program like is it always about big size that's important to have or is there fun little
*  smaller case playgrounds to play around with so we're trying to like push something towards that
*  i think there are a few setups out there but nothing like super standard on the smaller scale
*  i mean image net in itself is actually pretty big also so that is not something which is like
*  feasible for a lot of people but we are trying to like push up with like smaller sort of use cases
*  the thing is at a smaller scale a lot of the observations or a lot of the algorithms that
*  work don't necessarily translate into the medium or the larger scale so it's really tricky to come
*  up with a good small scale setup where a lot of your empirical observations will really translate
*  to the other setup so it's been really challenging i've been trying to do that for a little bit as
*  well because it does take time to train stuff on image net it does take time to train on like more
*  more images but pretty much every time i've tried to do that it's been unsuccessful because all the
*  observations i draw from my set of experiments on a smaller data set don't translate into image net
*  or like don't translate into another sort of data set so it's been hard for us to figure this one
*  out but it's an important problem so there's this really interesting idea of learning across
*  multiple modalities right you have a cvpr 20-21 best paper candidate titled audio visual instance
*  discrimination with cross modal agreement what are the key results insights in this paper and
*  what can you say in general about the promise and power of multimodal learning for this paper it
*  actually came as a little bit of a shock to me at how well it worked so i can describe what the
*  problem setup was so it's been used in the past by lots of folks like for example andrew ovens from
*  mit alioshaif from berkeley andrew zisserman from oxford so a lot of these people have been sort of
*  showing results in this of course i was aware of this result but i wasn't really sure how well it
*  would work in practice for like other sort of downstream tasks so the results kept getting
*  better and i wasn't sure if like a lot of our insights from self-supervised learning would
*  translate into this multimodal learning problem so multimodal learning is when you have like
*  when you have multiple modalities okay so the particular modalities that we worked on in this
*  work were audio and video so the idea was basically if you have a video you have its
*  corresponding audio track and you want to use both of these signals the audio signal and the
*  video signal to learn a good representation for video and good representation for audio like this
*  podcast like this podcast exactly so what we did in this work was basically trained two different
*  neural networks one on the video signal one on the audio signal and what we wanted is basically the
*  features that we get from both of these neural networks should be similar so it should basically
*  be able to produce the same kinds of features from the video and the same kinds of features from the
*  audio now why is this useful well for a lot of these objects that we have there is a characteristic
*  sound right so trains when they go by they make a particular kind of sound boats make a particular
*  kind of sound people when they're jumping around will like shout whatever bananas don't make a
*  sound so where you can't learn anything about bananas there or when humans mention bananas
*  well yes when they say the word banana then so you can't trust basically anything that comes out
*  of a human's mouth as a source that source of audio because it's useless so the typical use case
*  is basically like for example someone playing a musical instrument so guitars have a particular
*  kind of sound and so on so because a lot of these things are correlated the idea in multimodal
*  learning is to take these two kinds of modalities video and audio and learn a common embedding
*  space a lot common feature space where both of these related modalities can basically be
*  close together and again you use contrasted learning for this so in contrasted learning
*  basically the video and the corresponding audio are positives and you can take any other video or
*  any other audio and that becomes a negative and so basically that's it it's just a simple application
*  of contrasted learning the main sort of finding from this work for us was basically that you can
*  actually learn very very powerful feature representations very very powerful video
*  representations so you can learn the sort of video network that we ended up learning can actually be
*  used for downstream for example recognizing human actions or recognizing different types of sounds
*  for example so this was sort of the key finding can you give kind of an example of a human action
*  or like just so we can build up intuition of what kind of thing right so there is this data set
*  called kinetics for example which has like 400 different types of human action so people jumping
*  people you know doing different kinds of sports or different types of swimming so like different
*  strokes and swimming golf and so on so there are like just different types of actions right there
*  and the point is this kind of video network that you learn in a self-supervised way can be used very
*  easily to kind of recognize these different types of actions it can also be used for recognizing
*  different types of objects and what we did is we tried to visualize whether the network can figure
*  out where the sound is coming from so basically give it a video and basically play of say of a
*  person just strumming a guitar but of course there is no audio in this and now you give it this sound
*  of a guitar and you ask like basically try to visualize where the network is where the network
*  thinks the sound is coming from and it can kind of basically draw like when you visualize it you
*  can see that it's basically focusing on the guitar yeah that's and the same thing for example for
*  certain people's voices like famous celebrities voices it can actually figure out where they're
*  like where their mouth is so it can actually distinguish different people's voices for example
*  a little bit as well without that ever being annotated in any way right so this is all what
*  it had discovered we never like we never pointed out that this is a guitar and this is the kind of
*  sound it produces it can actually naturally figure that out because it's seen so many correlations
*  of this sound coming with this kind of like an object that it basically learns to associate
*  this sound with this kind of an object yeah that's that's really fascinating right that's really
*  interesting so the idea with this kind of network is then you then fine tune it for a particular
*  task right so this is forming like a really good knowledge base within a neural network based on
*  which you could then train a little bit more to accomplish a specific task well exactly so you
*  don't need a lot of videos of humans doing actions annotated you can just use a few of them to
*  basically get your how much insight do you draw from the fact that you can figure out
*  where the sound is coming from i'm trying to see so that's kind of very it's very cvpr beautiful
*  right it's a it's a cool little insight i wonder how profound that is you know does it speak to
*  the idea that multiple modalities are somehow much bigger than the sum of their parts or
*  is it really really useful to have multiple modalities or is it just a cool thing that there's
*  parts of our world that are can be revealed like effectively through multiple modalities but most
*  of it is really all about vision or about one of the modalities i would say a little tending more
*  towards the second part so most of it can be sort of figured out with one modality but having an
*  extra modality always helps you yeah so in this case for example like one thing is when you're
*  if you observe someone cutting something and you don't have any sort of sound there whether it's an
*  apple or whether it's an onion it's very hard to figure that out but if you hear someone cutting
*  it it's very easy to figure it out because apples and onions make a very different kind of
*  different kind of characteristic sound when they're cut yeah so you really figure this out based on
*  audio it's much easier so your life will become much easier when you have access to different
*  kinds of modalities and the other thing is so i like to relate it in this way it may be like
*  completely wrong but the distributional hypothesis in nlp right where context basically
*  gives kind of meaning to that word sound kind of does that too right so if you have the same sound
*  so that's the same context across different videos you're very likely to be observing the
*  same kind of concept yeah so that's the kind of reason why it figures out the guitar thing right
*  it observed the same sound across multiple different videos and it figures out maybe this
*  is the common factor that's actually doing it i wonder i used to have this argument with my
*  dad a bunch for creating general intelligence whether smell is important like if that's
*  important sensory information mostly we're talking about like falling in love with an ai system
*  and for him smell and touch are important and i was arguing that it's not at all it's important
*  it's nice and everything but like you can fall in love with just language really but voice is very
*  powerful and vision is next and smell is not that important can i ask you about this process of
*  active learning you mentioned interactivity right is there some value within the self
*  supervised learning context to select parts of the data in intelligent ways
*  such that they would most benefit the learning process right so i think so i think i mean i
*  know i'm talking to an active learning fan here so of course i know the answer first you were
*  talking bananas and now you're talking about active learning i love it i think yanakun told
*  me that active learning is not that interesting i and i think i was back back then i didn't want
*  to argue with him too much but when we talk again that's we're going to spend three hours arguing
*  about active learning my sense was you can go extremely far with active learning you know perhaps
*  farther than anything else like the to me there's this kind of intuition that similar to data
*  augmentation you can get a lot from the data from intelligent optimized usage of the data
*  right i'm trying to speak generally in such a way that includes data augmentation and active learning
*  that there's something about maybe interactive exploration of the data that at least this part
*  of the solution to intelligence like an important part i don't know what your thoughts are on active
*  learning in general i actually really like active learning so back in the day we did this largely
*  ignored cvpr paper called learning by asking questions so the idea was basically you would
*  train an agent that would ask a question about the image it would get an answer and basically
*  then it would update itself it would see the next image it would decide what's the next hardest
*  question that i can ask to learn the most and the idea was basically because it was being smart
*  about the kinds of questions it was asking it would learn in fewer samples it would be more
*  efficient at using data and we did find to some extent that it was actually better than randomly
*  asking questions kind of weird thing about active learning is it's also a chicken and egg problem
*  because when you look at an image to ask a good question about the image you need to understand
*  something about the image right you can't ask a completely arbitrarily random question it may not
*  even apply to that particular image so there is some amount of understanding or knowledge that
*  basically keeps getting built when you're doing active learning so i think active learning in by
*  itself is really good and the main thing we need to figure out is basically how do we come up with
*  a technique to first model what the model knows and also model what the model does not know i
*  think that's the sort of beauty of it right because when you know that there are certain things that
*  you don't know anything about asking a question about those concepts is actually going to bring
*  you the most value and i think that's the sort of key challenge now self-supervised learning by
*  itself like selecting data for it and so on that's actually really useful but i think that's a very
*  narrow view of looking at active learning right if you look at it more broadly it is basically about
*  if the model has a knowledge about n concepts and it is weak basically about certain things so it
*  needs to ask questions either to discover new concepts or to basically like increase its
*  knowledge about these n concepts but at that level it's it's a very powerful technique i actually do
*  think it's going to be really useful even in like simple things such as like data labeling it's
*  super useful so here is like one simple way that you can use active learning for example you have
*  your self-supervised model which is very good at predicting similarities and dissimilarities between
*  things and so if you label a picture as basically say a banana now you know that all the images that
*  are very similar to this image are also likely to contain bananas so probably when you want to
*  understand what else is a banana you're not going to use these other images you're actually going
*  to use an image that is not completely dissimilar but somewhere in between which is not super
*  similar to this image but not super dissimilar either and that's going to tell you a lot more
*  about what this concept of a banana is so that that's kind of a heuristic i wonder if it's
*  possible to also learn learn ways to discover the most likely the most beneficial image so like
*  so not just looking a thing that's somewhat similar to a banana but not exactly similar
*  but have some kind of more complicated learning system like learned discovery mechanism
*  that tells you what what image to look for like how exactly i yeah like actually in a self-supervised
*  way learning strictly a function that says is this image going to be very useful to me given what i
*  currently know i think there is a lot of synergy there it's just i think yeah it's going to be
*  explored i think very much related to that i kind of think of what tesla autopilot is doing at
*  currently as kind of active learning there's something that andre kapati and their team are
*  calling a data engine yes you're basically deploying a bunch of instantiations of a neural
*  network into the wild and they're collecting a bunch of edge cases that are then sent back for
*  annotation for particular and edge cases as defined as near failure or some weirdness on a
*  particular task that's then sent back it's that not exactly a banana but almost the banana cases
*  send back for annotation and then there's this loop that keeps going and you keep retraining and
*  retraining and the active learning step there or whatever you want to call it is the cars themselves
*  that are sending you back the data like what the hell happened here this was this was weird
*  what are your thoughts about that sort of deployment of neural networks in the wild
*  another way to ask a question first is your thoughts and maybe if you want to comment is there
*  applications for autonomous driving like computer vision based autonomous driving
*  applications of self-supervised learning in the context of computer vision based autonomous driving
*  so i think so i think for self-supervised learning to be used in autonomous driving
*  there's lots of opportunities i mean just like pure consistency in predictions is one way right
*  so you because that you have this nice sequence of data that is coming in a video stream of it
*  associated of course with the actions let's say the car took you can form a very nice predictive
*  model of what's happening so for example like all the way like one way possibly in which how
*  they're figuring out what data to get labeled is basically through prediction uncertainty right
*  so you predict that the car was going to turn right so this was the action that was going to
*  happen say in the shadow mode and now the driver turned left and this was this is a really big
*  surprise so basically by forming these good predictive models you are i mean these are kind
*  of self-supervised models right prediction models are basically being trained just by looking at
*  what's going to happen next and asking them to predict what's going to happen next so i would
*  say this is really like one use of self-supervised learning it's a predictive model and you're
*  learning a predictive model basically just by looking at what data you have is there something
*  about that active learning context that that you you find insights from like that kind of
*  deployment of the system seeing cases where it doesn't perform as you expected and then
*  retraining the system based on that i think that i mean that really resonates with me
*  it's super smart to do it that way because i mean the thing is with any kind of like practical
*  system like autonomous driving there are those those edge cases are the things that are actually
*  the problem right i mean highway driving or like freeway driving has basically been like there has
*  been a lot of success in that particular part of autonomous driving for a long time i would say
*  like since the 80s or something now the point is all these failure cases are the are the sort of
*  reason why autonomous driving hasn't come hasn't become like super super mainstream and available
*  like in every possible car right now and so basically by really scaling this problem out by
*  really trying to get all of these edge cases out as quickly as possible and then just like using
*  those to improve your model that's super smart and prediction uncertainty to do that is like one
*  really nice way of doing it let me put you on the spot so we mentioned offline jitendra he thinks
*  that the tesla computer vision approach or really any approach for autonomous driving is very far
*  away how many years away if you have to bet all your money on it are we just solving autonomous
*  driving with this kind of computer vision only machine learning based approach okay so what does
*  solving autonomous driving mean does it mean solving it in the u.s. does it mean solving it
*  in india because i can tell you that very different types of driving happening not india not russia
*  in the united states autonomous so what solving means is when the car says it has control it is
*  fully liable you can you can go to sleep is driving by itself so this is highway and city
*  driving but not everywhere but mostly everywhere and it's let's say significantly better like say
*  five times less accidents than humans sufficiently safer such that the public feels like that
*  transition is you know enticing beneficial both for our safety and financial and all those kinds
*  of things okay so first disclaimer i'm not an expert in autonomous driving so let me put it out
*  there uh i would say like at least five to ten years this is this would be my like guess from now
*  that yeah i'm actually very impressed like when i sat in a friend's tesla recently and of course
*  like uh looking so it can on that screen it basically shows all the detections and everything
*  the car is doing as you're driving by and that's super distracting for me as a person because all
*  i keep looking at is like the bounding boxes and the cars it's tracking and it's really impressive
*  like especially when it's raining and it's able to do that that was the most impressive part for
*  me it's actually able to get through rain and do that and one of the reasons why like a lot of us
*  believed and i would put myself in that category is lidar based uh sort of uh technology for
*  autonomous driving was the key driver right so we were using it for the longest time and tesla then
*  decided to go this completely other route that oh we're not going to even use lidar so their
*  initial system i think was camera and radar based and now they're actually moving to a completely
*  like vision based system and so that was just like it sounded completely crazy like lidar is
*  very useful in cases where you have low visibility uh of course it comes with its own set of
*  complications but now to see that happen in like on a live tesla that basically just proves everyone
*  wrong i would say in a way and that's just working really well i think there were also like a lot of
*  advancements in camera technology now there were like i know at cmu when i was there there was a
*  particular kind of camera that had been developed that was really good at basically low visibility
*  settings so like lots of snow and lots of rain it could actually still have a very reasonable
*  visibility and i think there are lots of these kinds of innovations that will happen on the
*  sensor side itself which is actually going to make this very easy in the future and so maybe
*  that's actually why i'm more optimistic about vision-based self-like autonomous driving i was
*  going to call it self-supervised driving but vision-based autonomous driving that's the reason
*  i'm quite optimistic about it because i think there are going to be lots of these advances
*  on the sensor side itself so acquiring this data we're actually going to get much better about it
*  and then of course when once we're able to scale out and get all of these edge cases in as like
*  andre described i think that's going to make us go very far away yeah so i'm it's funny i'm very
*  much with you on the five to ten years maybe ten years but you made it i'm not sure how you made
*  it sound but for some people that seem that might seem like really far away and then for other people
*  it might seem like very close there's a lot of fundamental questions about how much game theory
*  is in this whole thing so like how much is is this simply a collision avoidance problem and how much
*  of it is you're still interacting with other humans in the scene and you're trying to create
*  an experience that's compelling so you want to get from point a to point b quickly you want to
*  navigate the scene in a safe way but you also want to show some regret level of aggression because
*  well certainly this is why you're screwed in india because you have to show a jersey or new jersey
*  right so like or new york or basically any major city but i think it's probably elon that i talked
*  the most about this which is surprised the level of which they're not considering human beings as
*  a huge problem in this as a source of problem like the driving is fundamentally a robot on robot
*  versus the environment problem versus like you know you can just consider humans not part of the
*  problem i used to think humans are almost certainly have to be modeled really well pedestrians and
*  cyclists and humans inside other cars you have to have like mental models for them you cannot just
*  see it as objects but more and more it's like the it's the same kind of intuition breaking thing
*  that self-supervised learning does which is well maybe through the learning you'll get all the human
*  like human information you need right like maybe you'll get it just with enough data
*  the you don't need to have explicit good models of human behavior maybe you get it through the data
*  so i mean my skepticism also just knowing a lot of automotive companies and how difficult it is to be
*  innovative i was skeptical that they would be able at scale to convert the driving scene across the
*  world into digital form such that you can create this data engine at scale and the fact that tesla
*  is at least getting there or are already there makes me think that it's it's now starting to be
*  coupled to this self-supervised learning vision which is like if that's going to work if through
*  purely this process you can get really far then maybe you can solve driving that way i don't know
*  i i tend to believe we've we don't give enough credit to the to the how amazing humans are
*  both at driving and at supervising autonomous systems and also we don't this is i wish we were
*  i wish there was much more driver sensing inside tesla's and much deeper consideration of human
*  factors like understanding psychology and drowsiness and all those kinds of things
*  when the car does more and more of the work how to keep utilizing the little human supervision
*  that i needed to keep this whole thing safe i mean it's a fascinating dance of human robot interaction
*  to me autonomous driving for a long time is a human robot interaction problem problem it is not
*  a robotics problem or computer vision problem like you have to have a human in the loop but so which
*  is why i think it's 10 years plus but i do think there'll be a bunch of cities and contexts where
*  you know geo-restricted it will work really really damn well yeah so i think for me like it's five
*  if i'm being optimistic and it's going to be five for a lot of cases and 10 plus yeah i agree with
*  you 10 plus basically uh if we want to recover most of the say contiguous united states or something
*  oh interesting so my my optimistic is five and pessimistic is 30 30 i have a long tail on this
*  one i've watched enough driving videos i've watched enough pedestrians to think like we may be like
*  there's a small part of me still not a small like a pretty big part of me that thinks we will have
*  to build a gi to solve driving oh like there's something to me like because humans are part of
*  the picture deeply part of the picture and also human society is part of the picture in that human
*  life is at stake anytime a robot kills a human it's not clear to me that that's not a problem
*  that machine learning will also have to solve like it has to it you have to integrate that
*  into the whole thing just like uh facebook or social networks you know one thing is to say how
*  to make a really good recommender system and then the other thing is to integrate into that
*  recommender system all the journalists that will write articles about that recommender system
*  like you have to consider the society within which the ai system operates and in order to
*  and like politicians too you know this is there's regulatory stuff for autonomous driving
*  it's kind of fascinating that the more successful your ai system becomes the more it gets integrated
*  in society and the more precious politicians and the public and the clickbait journalists and the
*  all the different fascinating forces of our society start acting on it and then it's no longer how good
*  you are doing the initial task it's also how good you are navigating human nature which uh which is
*  a fascinating space what do you think are the limits of deep learning if you allow me we'll zoom
*  out a little bit into the big question of artificial intelligence you said dark matter of intelligence
*  is self-supervised learning but uh there could be more what do you think the limits of self-supervised
*  learning and just learning in general deep learning are i think like for deep learning in particular
*  because self-supervised learning is i would say a little bit more uh vague right now so i wouldn't
*  like for something that's so vague it's hard to predict what its limits are going to be
*  but like like i said i think anywhere you want to interact with human self-supervised learning kind
*  of hits a hits a boundary very quickly because you need to have an interface to be able to
*  communicate with the human so really like if you have just like vacuous concepts or like just like
*  nebulous concepts discovered by a network it's very hard to communicate those with a human without
*  like inserting some kind of human knowledge or some kind of like human bias there in general i
*  think for deep learning the biggest challenge is just like data efficiency uh even with self-supervised
*  learning even even with anything else if you just see a single concept once uh like one image of a
*  like i don't know whatever you want to call it like any concept it's really hard for these methods to
*  generalize by looking at just one or two samples of things and that has been a real real challenge
*  i think that's actually why like these edge cases for example for tesla are actually that important
*  because if you see just one instance of the car failing and if you just annotate that and you get
*  that into your data set it's you have like very limited guarantee that it's not going to happen
*  again and you're actually going to be able to recognize this kind of instance in a very
*  different scenario so like when it was snowing so you got that thing labeled when it was snowing
*  but now when it's raining you're actually not able to get it or you basically have the same
*  scenario in a different part of the world so the lighting was different or so on so it's just really
*  hard for these models like deep learning especially to do that what's your intuition how do we solve
*  handwritten digit recognition problem when we only have one example for each number it feels like
*  humans are using something like learning right i think it's we are good at transferring knowledge
*  a little bit we are just better at like for for a lot of these problems where we are generalizing
*  from a single sample recognizing from a single sample we are using a lot of our own domain
*  knowledge and a lot of our like inductive bias into that one sample to generalize it so i've
*  never seen you write the number nine for example and if you were to write it i would still get it
*  and if you were to write a different kind of alphabet and like write it in two different
*  ways i would still probably be able to figure out that these are the same two characters
*  it's just that i have been very used to seeing handwritten digits in my life the other sort of
*  problem with any deep learning system or any kind of machine learning system is like it's guarantees
*  right there are no guarantees for it now you can argue that humans also don't have any guarantees
*  there is no guarantee that i can recognize a cat in every scenario i'm sure there are going to be
*  lots of cats that i don't recognize lots of scenarios in which i don't recognize cats in
*  general but i think from like from just a sort of application perspective you do need guarantees
*  right we call these things algorithms now algorithms like traditional cs algorithms have guarantees
*  sorting is a guarantee if you were to like call sort on a particular array of numbers you are
*  guaranteed that it's going to be sorted otherwise it's a bug now for machine learning it's very
*  hard to characterize this we know for a fact that like a cat recognition model is not going to
*  recognize cats every cat in the world in every circumstance like that's i think most people would
*  agree with that statement but we are still okay with it we still don't call this as a bug as in
*  traditional computer science or traditional science like if you have this kind of failure case existing
*  then you think of it as like something is wrong i think there is this sort of notion of nebulous
*  correctness for machine learning and that's something we just need to be very comfortable
*  with and for deep learning or like for a lot of these machine learning algorithms it's not clear
*  how do we characterize this notion of correctness i think limitation in our understanding or at least
*  a limitation in our phrasing of this and if we were to come up with better ways to understand this
*  limitation then it would actually help us a lot do you think there's a distinction between
*  the concept of learning and the concept of reasoning do you think it's possible for
*  neural networks to reason so i think of it slightly differently so for me learning is whenever i can
*  like make a snap judgment so if you show me a picture of a dog i can immediately say it's a dog
*  but if you give me like a puzzle you know like whatever a goldsberg machine of like things
*  going to happen then i have to reason because i've never it's a very complicated setup i've never
*  seen that particular setup and i really need to you know draw and like imagine in my head what's
*  going to happen to figure it out so i think yes neural networks are really good at recognition
*  but they're not very good at reasoning because they're like if they have seen something before
*  or seen something similar before they're very good at making those sort of snap judgments
*  but if you were to give them a very complicated thing that they've not seen before they have very
*  limited ability right now to compose different things like oh i've seen this particular part
*  before i've seen this particular part before and now probably like this is how they're going to
*  work in tandem it's very hard for them to come up with these kinds of things well there's a certain
*  aspect to reasoning that you can maybe convert into the process of programming and so there's
*  the whole field of program synthesis and people have been applying machine learning to the problem
*  of program synthesis and the question is you know can they the step of composition why can't that
*  be learned you know this the step of like building things on top of you like little intuitions
*  concepts on top of each other can that be learnable what's your intuition there or like i guess similar
*  set of techniques do you think that will be applicable so i think it is of course learning
*  it is learnable because like we are prime examples of machines that have like or
*  individuals that have learned this right like humans have learned this so it is of course
*  it is a technique that is very easy to learn i think where we are kind of hitting a wall
*  basically with like current machine learning is the fact that when the network learns all of this
*  information we basically are not able to figure out how well it's going to generalize to an unseen
*  thing yeah and we have no like a priori no way of characterizing that and i think that's basically
*  telling us a lot about like a lot about the fact that we really don't know what this model has
*  learned and how well it's basically because we don't know how well it's going to transfer
*  there's also a sense in which it feels like we humans may not be aware of how much like background
*  how good our background model is how much knowledge we just have slowly building on top of each other
*  it feels like neural networks are constantly throwing stuff out like you'll do some incredible
*  thing where you're learning a particular task in computer vision you celebrate your state of the
*  art successes and you throw that out like it feels like it's you're never using stuff you've learned
*  for your future successes in in other domains and humans are obviously doing that exceptionally well
*  uh still throwing stuff away in their mind but keeping certain kernels of truth right so i think
*  we're like continual learning is sort of the paradigm for this in machine learning and i
*  don't think it's a very well explored paradigm yeah uh we have like things in deep learning for
*  example right catastrophic forgetting is like one of the standard things the thing basically being
*  that if you teach a network like to recognize dogs and now you teach that same network to recognize
*  cats it basically forgets how to recognize dogs so it forgets very quickly i mean and
*  whereas a human if you were to teach someone to recognize dogs and then to recognize cats they
*  don't forget immediately how to recognize these dogs i think that's basically sort of what you're
*  trying to get yeah just i wonder if like the long-term memory mechanisms or the mechanisms
*  that store not just memories but concepts that allow you to uh to the reason uh like and and
*  compose concepts if those things will look very different than your networks or if you can do
*  that within a single neural network with some particular sort of architecture quirks that seems
*  to be a really open problem and of course i go up and down on that because it's um there's something
*  so compelling to the uh to the symbolic ai or to um the ideas of logic based sort of expert systems
*  you have like human interpretable facts that built on top of each other it's really annoying like
*  with self-supervised learning that uh the ai is not very explainable like you can't like understand
*  all the beautiful things as has learned you can't ask it like questions but then again maybe that's
*  a stupid thing for us humans to want right i think whenever we try to like understand it we're putting
*  our own subjective human bias into it yeah and i think that's the sort of problem with self-supervised
*  learning the goal is that it should learn naturally from the data so now if you try to understand it
*  you are using your using your own preconceived notions of what this model has learned and that's
*  the problem high level question what do you think it takes to build a uh system with superhuman maybe
*  let's say human level or superhuman level general intelligence we've already kind of started talking
*  about this but what's your intuition like does this thing have to have a body does it does it have to
*  interact richly with the world does it have to have some more human elements like
*  self-awareness i think emotion i think emotion is something which is like it's not really attributed
*  typically in standard machine learning it's not something we think about like there is nlp there
*  is vision there is no like emotion emotion is never a part of all of this and that just seems
*  a little bit weird to me i think the reason basically being that there is surprise and like
*  basically emotion is like one of the reasons emotions arises like what happens and what you
*  expect to happen right there is like a mismatch between these things and so that gives rise like
*  i can either be surprised or i can be saddened or i can be happy and all of this and so this basically
*  indicates that i already have a predictive model in my head and something that i predicted or
*  something that i thought was likely to happen and then there was something that i observed that
*  happened that there was a disconnect between these two things and that basically is like maybe
*  one of the reasons i like you have a lot of emotions yeah i i think so i talked to people
*  a lot about them more like lisa felton barrett i think that's an interesting concept of emotion
*  but i have a sense that emotion primarily in the way we think about it which is the display of
*  emotion is a communication mechanism between humans so it's a part of basically human to human
*  interaction an important part but just the part so it's like it i would throw it into the
*  into the full mix of communication and to me communication can be done with objects that
*  don't look at all like humans okay i've seen our ability to anthropomorphize our ability to connect
*  with things that look like a rumba our ability to connect first of all let's talk about other
*  biological systems like dogs our ability to love things that are very different than humans but
*  they do display emotion right i mean dogs do display emotion so they don't have to be
*  anthropomorphic for them to like display the kind of emotion that we don't exactly so it's
*  you know i mean but then the word emotion starts to lose um so then we have to be i guess specific
*  but yeah so have rich flavorful communication communication yeah yeah so like yes it's full
*  of emotion it's full of uh wit and humor and uh moods and all those kinds of things yeah so
*  so you're talking about like flavor flavor yeah okay let's call it so there's content and then
*  there is flavor and i'm talking about the flavor do you think it needs to have a body do you think
*  like to interact with the physical world do you think you can understand the physical world without
*  being able to directly interact with it i don't think so yeah i think at some point we will need
*  to bite the bullet and actually interact with the physical as much as i like working on like
*  passive computer vision where i just like sit in my armchair and look at videos and learn i do think
*  that uh we will need to have some kind of embodiment or some kind of interaction to figure out things
*  about the world what about consciousness do you think you think how often do you think about
*  consciousness when you think about your work you could think of it as the more simple thing of
*  self-awareness of being aware that you are a uh perceiving sensing acting thing in this world
*  or you can think about the bigger thing version of that which is consciousness which is having
*  it feel like something to be that entity the subjective experience of being in this world so
*  i think of self-awareness a little bit more than this like the broader goal of it because
*  i think self-awareness is pretty critical for like any kind of like any kind of a gi or whatever you
*  want to call it that we build because it needs to contextualize what it is and what role it's playing
*  with respect to all the other things that exist around it i think that requires self-awareness
*  it needs to understand that it's an autonomous car right and what does that mean what are its
*  limitations what are the things that it is supposed to do and so on what is its role in
*  some way or i mean so i mean this is these are the kind of things that we kind of expect from it
*  i would say and so that's the level of self-awareness that's i would say basically
*  required at least if not more than that yeah i tend to on the emotion side believe that it has
*  to have it has to be able to display consciousness display consciousness what do you mean by that
*  meaning like for us humans to connect with each other or to connect with other living entities
*  i think we need to feel like in order for us to uh truly feel like that there's another being there
*  we have to believe that they're conscious and so we won't ever connect with something that doesn't
*  have elements of consciousness now i tend to think that that's easier to achieve than it may sound
*  because we anthropomorphize stuff so hard like you have a mug that just like has wheels and like
*  rotates every once in a while and makes a sound i think a couple days in especially if you're uh
*  if you're if you don't hang out with humans you might start to believe that mug on wheels is
*  conscious so i think we anthropomorphize pretty effectively as human beings but i do think that
*  it's it's in the same bucket that we'll call emotion that show that uh you're you know i
*  think of consciousness as the capacity to suffer and if you're an entity that's able to feel
*  things in the world and to communicate that to others i think that's a really powerful way to
*  interact with humans and in order to create an aji system i believe you should be able to
*  richly interact with humans like humans would need to want to interact with you like it can't
*  be like it's it's the um self-supervised learning versus like uh like the robot shouldn't have to
*  pay you to interact with me so like it should be a natural fun thing and then you're going to
*  scale up significantly how much uh interaction it gets it's the alexa prize which they're trying
*  to get me to be a judge on their uh contest let's see if i want to do that but their their challenge
*  is to uh talk to you make the judge make the human sufficiently interested that the human
*  keeps talking for 20 minutes to alexa to alexa yeah and right now they're not even close to that
*  because it just gets so boring when you're like when the intelligence is not there it gets very
*  not interesting to talk to it and so the robot needs to be interesting and one of the ways it
*  can be interesting is display the capacity to to love to suffer and i would say that essentially
*  means the the capacity to display consciousness like it is a entity much like a human being of
*  course what that really means i don't know if that's fundamentally a robotics problem
*  or some kind of problem that we're not yet even aware like if it is truly a hard problem of
*  consciousness i tend to maybe optimistically think it's a um we can pretty effectively fake
*  it till we make it so we can display a lot of human-like elements for a while and that will
*  be sufficient to form really close connections with humans what to use the most beautiful idea
*  in self-supervised learning like when you sit back with uh i don't know with a glass of wine
*  and an armchair and just at a fireplace just thinking how beautiful this world that you get
*  to explore is what do you think is the especially beautiful idea the fact that like object level
*  what objects are and some notion of objectness emerges from these models by just like self-supervised
*  learning so for example like one of the things like the dino paper that i was a part of at
*  facebook is the object sort of boundaries emerge from these representations so if you have like a
*  dog running in the field the boundaries around the dog the network is basically able to figure out
*  what the boundaries of this dog are automatically and it was never trained to do that it was never
*  trained to uh no one taught it that this is a dog and these pixels belong to a dog it's able to
*  group these things together automatically so that's one i think in general that entire notion that
*  this dumb idea that you take like these two crops of an image and then you say that the
*  features should be similar that has resulted in something like this like the model is able to
*  figure out what the dog pixels are and so on that just seems like so surprising um and i mean i don't
*  think a lot of us even understand what how that is happening really and it's something we're taking
*  for granted uh maybe like a lot in terms of how we're setting up these algorithms but it's just
*  it's a very beautiful and powerful idea so it's really fundamentally telling us something about
*  that there is so much signal in the pixels that we can be super dumb about it about how we're
*  setting up the self-supervised learning problem and despite being like super dumb about it we'll
*  actually get very good uh like we'll actually get something that is able to do very like surprising
*  things i wonder if there's other like objectness other concepts that can emerge i don't know if
*  you follow françois chollet he had the competition for intelligence that basically it's kind of like
*  an iq test but for machines but for an iq test you have to have a few concepts that you want to
*  apply one of them is objectness i wonder if those concepts can emerge through self-supervised
*  learning on billions of images i think something like object permanence can definitely emerge
*  right so that's like a fundamental concept which we have um maybe not through images through video
*  but that's another concept that should be emergent from it because it's not something that like we
*  don't teach humans that this isn't this is like about this concept of object permanence it actually
*  emerges and the same thing for like animals like dogs i think actually permanence automatically is
*  something that they are born with so i think it should emerge from the data it should emerge
*  basically very quickly i wonder if ideas like symmetry rotation these kinds of things might
*  emerge so i think rotation probably yes yeah rotation yes i mean there's some constraints
*  in the architecture itself right but it's interesting if all of them could be um like
*  counting was another one you know being able to kind of understand that there's multiple objects
*  of the same kind in the image and be able to count them i wonder if all of that could be if
*  constructed correctly they can emerge because then you can transfer those concepts to um
*  to then interpret images at a deeper level right counting i do believe i mean should be possible
*  you don't know like yet but i do think it's not that far in the realm of possibility
*  yeah that'd be interesting if using self-supervised learning on images
*  can then be applied to then solving those kinds of iq tests which seem currently to be kind of
*  impossible what idea do you believe might be true that most people think is not true or don't agree
*  with you on is there something like that so this is going to be a little controversial but okay sure
*  i don't believe in simulation like actually using simulation to do things very much just to
*  clarify because this is a podcast where you talk about are we living in a simulation often
*  you're referring to using simulation to construct worlds that you then leverage from machine
*  learning right yeah for example like one example would be like to train an autonomous car driving
*  system you basically first build a simulator which builds like the environment of the world
*  and then you basically have a lot of like you train your machine learning system in that
*  so i believe it is possible but i think it's a really expensive way of doing things
*  and at the end of it you do need the real world so i'm not sure so maybe for certain settings like
*  maybe the payout is so large like for autonomous driving the payout is so large that you can
*  actually invest that much money to build it but i think as a general sort of principle it does
*  not apply to a lot of concepts you can't really build simulations of everything
*  not only because like one it's expensive because second it's also not possible for a lot of things
*  so in general like there is a lot of like there's a lot of work on like using synthetic data and
*  like synthetic simulators i generally am not very like i don't believe in that so you're saying it's
*  very challenging visually like to correctly like simulate the visual like the lighting all those
*  kinds of things i mean i mean all these companies that you have right so like pixar and like
*  whatever all these companies are if they're all this like computer graphic stuff is really about
*  accurately a lot of them is about like accurately trying to figure out how the lighting is and like
*  how things reflect off of one another and so on and like how sparkly things look and so on so
*  it's a very hard problem so do we really need to solve that first to be able to like do computer
*  vision probably not and for me in the context of autonomous driving it's very tempting to be able
*  to use simulation right because it's a safety critical application but the other limitation
*  of simulation that perhaps is a bigger one than the visual limitation is the behavior of objects
*  because the so you're ultimately interested in edge cases and the question is how well can you
*  generate edge cases in simulation especially with human behavior i think another problem is like for
*  autonomous driving right it's a constantly changing world so say autonomous driving like in 10 years
*  from now like uh there are lots of autonomous cars but they're still going to be humans so now
*  there are 50 percent of the agents say which are humans 50 percent of the agents that are autonomous
*  like car driving agents so now the mixture has changed so now the kinds of behaviors that you
*  expect from the other other agents or other cars on the road are actually going to be very different
*  and as the proportion of the number of autonomous cars to humans keeps changing this behavior will
*  actually change a lot so now if you were to build a simulator based on just like right now to build
*  them today you don't have that many autonomous cars on the road so you'll try to like make all
*  of the other agents in that simulator behave as humans but that's not really going to hold true
*  10 15 20 30 years from now uh do you think we're living in simulation no
*  how hard is it uh this is why i think it's an interesting question how hard is it to build a
*  video game like virtual reality game where it is so real forget like ultra realistic to where you
*  can't tell the difference but like it's so nice that you just want to stay there you just want to
*  stay there and you don't want to come back do you think that's um you think that's doable within our
*  lifetime within our lifetime probably yeah i eat healthy i live along
*  does that make you sad that there will be like um like population of uh kids that basically spend
*  95 99 percent of their time in a virtual world
*  very very hard question to answer um for certain people it might be something that they really
*  derive a lot of value out of derive a lot of enjoyment and like happiness out of
*  and maybe the real world wasn't giving them that that's why they did that so maybe it is good for
*  certain people so ultimately if it maximizes happiness right i think if judge yeah i think
*  if it's making people happy maybe it's okay uh again i think it's this is a very hard question
*  so like you've uh you've been a part of a lot of amazing papers
*  um what advice would you give to somebody on what it takes to write a good paper
*  grad students writing papers now is there um is there common things that you've learned along
*  the way that you think it takes both for a good idea and a good paper right so i think um both of
*  these i've picked up from like lots of people have worked with in the past so one of them is
*  picking the right problem to work on in research is as important as like the like finding the
*  solution to it so i mean there are multiple reasons for this so one is that there are
*  certain problems that can actually be solved uh in in a particular time frame so now say you want to
*  work on finding the meaning of life this is a great problem i think most people will agree with
*  that but do you believe that you your talents and like the energy that you'll spend on it will
*  make a meaning like make some kind of meaningful progress in your lifetime
*  if you are optimistic about it then like go ahead that's why i started this podcast i keep asking
*  people about the meaning of life i'm hoping by episode like 220 i'll figure it out so oh
*  not too many episodes to go all right cool uh maybe today i don't know but you're right so that that's
*  seems intractable at the moment right so i think it's just the fact of like if you're starting a
*  phd for example what is one problem that you want to focus on that you do think is interesting
*  enough and you will be able to make a reasonable amount of headway into it that you think you'll
*  be doing a phd for so in that kind of a time frame so that's one of course there's the second part
*  which is what excites you genuinely so you shouldn't just pick problems that you are not
*  excited about because as a grad student or as a researcher you really need to be passionate
*  about it to continue doing that because there are so many other things that you could be doing in
*  life so you really need to believe in that to be able to do that for that long in terms of papers
*  i think the one thing that i've learned is i've like in the past whenever i used to write things
*  and even now whenever i do that i try to cram in a lot of things into the paper whereas what really
*  matters is just pushing one simple idea that's it that's all because that's the paper is going
*  to be like whatever eight or nine pages if you keep cramming in lots of ideas it's really hard
*  for the single thing that you believe in to stand out so if you really try to just focus like when
*  especially in terms of writing really try to focus on one particular idea and articulate it out
*  in multiple different ways it's far more valuable to the reader as well and basically to the reader
*  of course because they get to they know that this particular idea is associated with this paper
*  and also for you because you have like when you write about a particular idea in different ways
*  you think about it more deeply so as a grad student i used to always wait toward like maybe
*  in the last week or whatever to write the paper because i used to always believe that doing the
*  experiments was actually the bigger part of research than writing and my advisor always told
*  me that you should start writing very early on and i thought oh it doesn't matter i don't know
*  what he's talking about but i think more and more i realized that's the case like whenever i write
*  something that i'm doing i actually think much better about it and so if you start writing earlier
*  early on you actually i think get better ideas or at least you figure out like holes in your
*  theory or like particular experiments that you should run to block those holes and so on
*  yeah i'm continually surprised how many really good papers throughout history are quite short
*  and quite simple and there's a lesson to that like if you if you want to dream about writing
*  a paper that changes the world and you want to go by example they're usually simple yeah
*  and that that's that's it's not cramming or uh it's it's focusing on one idea and thinking
*  deeply and you're right that the writing process itself reveals the idea it challenges you really
*  think about what is the idea that explains that the thread that ties it all together
*  and so like a lot of famous researchers i know actually would start off like first they were
*  even before the experiments were were in a lot of them would actually start with writing the
*  introduction of the paper with zero experiments in yeah because that at least helps them figure
*  out what they're like what they're trying to solve and how it fits in like the context of things
*  right now and that would really guide their entire research so a lot of them would actually
*  first write an intro with like zero experiments in and that's how they would start projects
*  some basic questions about people maybe uh there are more like beginners in this field
*  what's the best programming language to learn if you're interested in machine learning
*  i would say python just because it's the easiest one to learn uh and also a lot of like programming
*  in machine learning happens in python so it'll if you don't know any other programming language
*  python is actually going to get you a long way yeah it seems like sort of uh it's a toss-up
*  question because it seems like python is so much dominating the space now but i wonder if there's
*  interesting alternatives obviously there's a like swift and there's a lot of interesting alternatives
*  popping up even javascript so i or are uh more like for the data science applications but it
*  seems like python more and more is actually being used to teach like introduction of programming at
*  universities so it just combines everything very nicely even harder question what are the pros and
*  cons of pytorch versus tensorflow i see okay so you can go with no comment so a disclaimer to
*  this is that the last time i used tensorflow was probably like four years ago and so it was right
*  when it had come out because so i started on like deep learning in 2014 or so and the dominant sort
*  of parent uh framework for us then for vision was cafe which was out of berkeley and we used cafe a
*  lot was really nice uh and then tensorflow came in which was basically like python first so cafe
*  was mainly c++ and it had like very loose kind of python binding so python wasn't really the first
*  language you would use you would really use uh either matlab or c++ like uh get stuff done and
*  do done in like cafe and then python of course became popular a little bit later so tensorflow
*  was basically around that time so 2015 2016 is when i last used it uh it's been a while and then
*  did you use torch or did you or did you so then i moved to lure torch which was the torch in lure
*  and then in 2017 i think basically pretty much to pytorch completely oh interesting so you went to
*  lure cool yeah huh so you're there before it was cool yeah i mean so lure torch was really good
*  because it uh it actually allowed you to do a lot of different uh kinds of things so which cafe was
*  very rigid in terms of its structure like you would create a neural network once and that's it
*  whereas if you wanted like very dynamic graphs and so on it was very hard to do that and lure
*  torch was much more friendly for all of these things um okay so in terms of pytorch and tensorflow
*  my personal bias is pytorch just because i've been using it longer and i'm more familiar with it
*  and also that pytorch is much easier to debug is what i find because it's imperative in nature
*  compared to like tensorflow which is not imperative but that's telling you a lot that basically the
*  imperative design is sort of a way in which a lot of people are taught programming and that's what
*  actually makes debugging easier for them so like i learned programming in cc plus plus and so for
*  me imperative way of programming is more natural do you think it's good to have kind of these two
*  communities this kind of competition i think pytorch is kind of more and more becoming dominant
*  in the research community but tensorflow is still very popular in the more sort of application
*  machine learning community so do you think it's good to have that kind of split in code bases
*  or um so like the benefit there is the competition challenges the library developers to step up their
*  game yeah but the downside is there's these code bases that are in different different libraries
*  right so i think the downside is that i mean for a lot of research code that's released in one
*  framework and if you're using the other one it's really hard to like really build on top of it
*  but thankfully the open source community in machine learning is amazing so yeah whenever like
*  something pops up in tensorflow you wait a few days and someone who's like super sharp will
*  actually come and translate that particular code base into pytorch and it will and basically have
*  figured that all looks and crannies out so the open source community is amazing and they really
*  like figure out this gap so i think in terms of like having these two frameworks or multiplying
*  of course there are different use cases so there are going to be benefits to using one or the other
*  framework and like you said i think competition is just healthy because both of these frameworks
*  or like all of these frameworks really sort of keep learning from each other and keep
*  incorporating different things to just make them better and better what advice would you have for
*  someone new to machine learning you know uh maybe just started or haven't even started but are
*  curious about it and who want to get in the field don't be afraid to get your hands dirty i think
*  that's the main thing so if something doesn't work like really drill into why things are not
*  working can you elaborate what your hands dirty means right so for example like if an algorithm
*  if you try to train the network and it's not converging whatever rather than trying to like
*  google the answer or trying to do something like really spend those like five eight ten fifteen
*  twenty whatever number of hours really trying to figure it out yourself because in that process
*  you'll actually learn a lot more yeah googling is of course like a good way to solve it when you
*  need a quick answer but i think initially especially like when you're starting out it's
*  much nicer to like figure things out by yourself and i just say that from experience because like
*  when i started out there were not a lot of resources so we would like in the lab a lot of us
*  like we would look up to senior students and the senior students were of course busy and they would
*  be like wait why don't you go figure it out because i just don't have the time i'm working on my
*  dissertation or whatever i'll find here phd students and so then we would sit down and like
*  just try to figure it out and that i think really helped me that has really helped me figure a lot
*  of things out i think in general if i were to generalize that i feel like persevering through
*  any kind of struggle on a thing you care about is good so you're basically you try to make it seem
*  like it's good to you know spend time debugging but really any kind of struggle whatever form that
*  takes it could be just googling a lot just basically anything just go sticking with it and
*  going through the hard thing that could take a form of implementing stuff from scratch
*  it could take the form of reimplementing with different libraries or different programming
*  languages it could take a lot of different forms but struggle is good for the soul yeah so like in
*  pittsburgh where i did my phd the thing was it used to snow a lot yeah right and so when it was
*  snowed you really couldn't do much so the thing that a lot of people said was snow builds character
*  because when it's snowing you can't do anything else you focus on work do you have advice in
*  general for people you've already exceptionally successful you're young but do you have advice
*  for young people starting out in college or maybe in high school you know advice for their career
*  advice for their life how to pave a successful path in career and life i would say just be hungry
*  like always be hungry for what you want and i think like i've been inspired by a lot of people
*  who are just like driven and who really like go for what they want no matter what like you shouldn't
*  want it you should need it so if you need something you basically go towards the ends to make it work
*  how do you know when you you come across a thing that that's like you need i think there's not
*  going to be any single thing that you're going to need there are going to be different types
*  of things that you need but whenever you need something you just go push for it and of course
*  once you you may not get it or you may find that this was not even the thing that you were looking
*  for it might be a different thing but the point is like you're pushing through things and that
*  actually gives you brings a lot of skills and brings a lot of like builds a certain kind of
*  attitude which will probably help you get the other thing once you figure out what's really the
*  thing that you want yeah i think a lot of people are i've noticed the kind of afraid of that is
*  because one it's a fear of commitment and two there's so many amazing things in this world you
*  almost don't want to miss out on all the other amazing things by committing to this one thing
*  so i think a lot of it has to do with just allowing yourself to
*  like notice that thing and just go all the way with it i mean i also like failure right so
*  yeah i know this is like super cheesy that you know failure is something that you should be
*  prepared for and so on but i do think i mean especially in research for example failure is
*  something that happens almost like almost every day is like experiments failing and not working
*  and so you really need to be so used to it you need to have a thick skin but and only basically
*  through like when you get through it is when you find the one thing that's actually working
*  so almost edison was like one person like that right so i really like when i was a kid i used
*  to really read about how he found like the filament the light bulb filament and then he i think his
*  thing was like he tried 990 things that didn't work or something of the sort and then they asked
*  him like so what did you learn because all of these were failed experiments and then he says
*  oh these 990 things don't work and i know that did you know that i mean that's really inspiring
*  so you spent a few years on this earth performing a self-supervised kind of learning process have you
*  figured out the meaning of life yet i told you i'm doing this podcast to try to get the answer
*  i'm hoping you could tell me what do you think the meaning of it all is
*  uh i don't think i figured this out no i have no idea uh do you think uh do you think
*  ai will help us figure it out or do you think there's no answer the whole point is to keep
*  searching i think yeah i think the it's an endless sort of quest for us i don't think ai will help
*  us there this is like a very hard hard hard question which so many humans have tried to
*  answer well that's the interesting thing but difference between ai and humans
*  uh humans don't seem to know what the hell they're doing and ai is almost always operating under
*  well-defined objective functions and i wonder like whether our lack of ability to have to define
*  good long-term objective functions or in introspect what is the objective function under which we
*  operate if that's a feature or a bug i would say it's a feature because then everyone actually
*  has very different kinds of objective functions that they're optimizing and those objective
*  functions evolve and like change dramatically through their course of their life that's actually
*  what makes us interesting right if otherwise like if everyone was doing the exact same thing that
*  would be pretty boring we do want like people with different kinds of perspectives also people
*  evolve continuously that's that's like i would say the biggest feature of being human and then
*  we get to like the ones that die because they do something stupid we get to watch that see it and
*  learn from it and uh as a species we uh take that lesson and become better and better because of all
*  the dumb people in the world that died doing something wild um and beautiful ishan thank you
*  so much for this incredible conversation we uh we did a depth first search through the uh the space
*  of machine learning and it was fun and uh fascinating so it's it's really an honor to meet
*  you and it was a really awesome conversation thanks for coming down today and talking with me
*  thanks lex i i mean i've listened to you i told you it was unreal for me to actually meet you in
*  person and i'm so happy to be here thank you thanks man thanks for listening to this conversation
*  with ishan misra and thank you to on it the information grammarly and athletic greens
*  check them out in the description to support this podcast and now let me leave you with some words
*  from arthur c clark any sufficiently advanced technology is indistinguishable from magic
*  thank you for listening and hope to see you next time

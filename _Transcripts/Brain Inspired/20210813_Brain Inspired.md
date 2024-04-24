---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5031s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 5877
Video Rating: None
---

# BI NMA 05: NLP and Generative Models Panel
**Brain Inspired:** [August 13, 2021](https://www.youtube.com/watch?v=sZ3jPnj-xUU)
*  You know, the human mind in contrast, as you know, instead of just one pathway forwards,
*  it's got a number of different pathways.
*  So as soon as information hits the visual cortex, it starts exploding down a series
*  of different pathways, each of which emphasizes different kinds of information.
*  So you can do the same thing with VAEs.
*  I think right now we don't really have a good way to evaluate these models, these language
*  models understand language.
*  I mean, they're good at solving the practical tasks.
*  We want them to solve, but then for more challenging tasks, like communicating with people or understanding
*  humor, these models are very brittle.
*  Perhaps this is even more cynical than, oh, your take is that the perhaps the language
*  is really nothing but just, you know, one layer or the shared weight across all those
*  neural nets that we have in our head.
*  Maybe that's about it, right?
*  My wife is a neuroscientist and she completely disagrees that it's anything like attention,
*  real attention.
*  But, you know, I definitely think that the inspiration is certainly, you know, similar
*  in terms of what we're trying to do with the model.
*  This is Brain Inspired.
*  Hey, everyone, it's Paul.
*  Welcome to the fifth installment of the Neuromatch Academy panel series here.
*  This is the second of the Deep Learning series.
*  This week was about doing more with fewer parameters.
*  So I guess convolutional neural networks were covered, recurrent neural networks, attention
*  mechanisms and transformers, and generative models like variational autoencoders and generative
*  adversarial networks.
*  With me today are three people from NYU, He He, Zhao Sedek, and Kyongyong Cho.
*  They're bringing their language model expertise to the conversation today, among other things,
*  and Brad Weibel from Penn State University.
*  So we don't talk a lot about convolutional neural networks or recurrent neural networks,
*  but we do talk about variational autoencoders.
*  Brad talks about his work using variational autoencoders as a model for building latent
*  representations for vision and memory and possibly imagination and other things you'll
*  hear about.
*  So we spend some time talking about that.
*  And then we spend a lot of time talking about language models and the idea of attention
*  and the story behind how it became called attention.
*  We also get into how everyone thinks about the levels of abstraction when dealing with
*  language models that can take in letters or words or sentences and so on or pixels.
*  So there's that.
*  Brad talks about his work, and he's going to be talking about the
*  language model and the way in which language models are used.
*  So Brad and I are going to go down multiple other roads.
*  It was a really enjoyable conversation.
*  You can go to the show notes to learn more about them at brandinspired.co.
*  slash podcast slash NMA dash five.
*  Okay, enjoy.
*  So I'm here with, I guess, three language modeling experts and one non-language modeling
*  each of you to introduce yourself briefly.
*  But then for fun, I thought maybe what you could each say is a piece of work or an idea
*  that you think you're best known for.
*  And then maybe, and it could be the same answer, then another idea or piece of work or, you
*  know, body of work that you are most proud of.
*  So Kyon, you want to get us going?
*  Yeah, sure.
*  Let's do that.
*  Yes.
*  So hi, everyone.
*  I'm Kyung-hyun.
*  I'm an associate professor of computer science and data science at New York University.
*  I've been here now slightly over six years and I work mainly on how to design a machine
*  learning algorithms for natural language processing as well as machine translation.
*  Although, you know, recently I've been going through what I call research identity crisis.
*  So I've been actually dabbling here and there, including some, a bit of biology, a bit of
*  chemistry, a bit of physics and so on without much success so far.
*  But that's it.
*  I was asked to talk about the most, let's say the most well-known paper of mine is probably
*  the attention paper where we introduced attention mechanism for the, in the context of the neural
*  machine translation.
*  But the one that I'm most fond of among my papers is paper from 2013 or 2012, if I remember
*  correctly, that was kind of final paper I wrote for my PhD dissertation.
*  And then back then, still it was the kind of final phase of work, you know, a lot of
*  people working on boson machines.
*  And in particular, the last flame was the deep boson machines.
*  I'm pretty sure there's only about five people in the world who have actually trained deep
*  boson machines.
*  And then my final paper in my dissertation was about how to train deep boson machines
*  more easily by pre-training in a very non-trivial way.
*  And then I got that idea out of a bus ride in one random day.
*  I'm very fond of that idea.
*  No one ever reads that paper, not even my students.
*  So no one really knows about it, but my favorite.
*  Is it a thing where you remember where you were in the bus or on the streets and what
*  you were doing, et cetera?
*  Yeah, precisely.
*  I was on a bus going from Espo.
*  That's where I did my PhD in Finland to Helsinki.
*  During the day, I think it was on Sunday, actually.
*  Nice.
*  Really, no one's working on Boltzmann machines anymore?
*  Really?
*  None that I know, or at least not me.
*  Yeah.
*  Yeah, very good.
*  Who would like to go next?
*  Brad, do you want to take a stab at it?
*  Sure.
*  My name is Brad Weibel.
*  I'm an associate professor at Penn State University in University Park.
*  I'm also one of the founders of Neuromatch Academy.
*  My work primarily involves understanding how the human mind builds representations of
*  things that we see.
*  I guess the work that I'm probably best known for in my little pocket of the field is
*  understanding the temporal dynamics of visual attention.
*  On a timescale of below one second, like 200 to 500 milliseconds, how does the tension
*  shift on and off?
*  Not in an oscillatory way, but in a sort of aperiodic way to capture the inherent statistical
*  structure of input that we're taking in.
*  I think the paper there that is kind of the most interesting and the one that I think
*  the most highly of is published in 2009.
*  It's a computational model of the temporal dynamics of attention.
*  What stands out about that one is that the structure of the attentional system in the
*  way that it works, I programmed it and there was a parenthesis error and I actually put
*  a multiplication on the wrong side.
*  I'd actually solved the problem that I was trying to solve.
*  I had to then go back and figure out why was this working so well and then the light dawned
*  and there was just advancement.
*  Innovation by mistake.
*  Yeah, that's the best kind.
*  I didn't say this before, but you're the only non-NYU person here, I believe.
*  That's right.
*  Yeah.
*  But you know, close enough, like the neighboring state, right?
*  Yes.
*  Yeah, that's right.
*  I actually started my undergraduate degree.
*  I'm in the psychology department now at Penn State, but my undergraduate degree was in
*  computer science at Brandeis back in the early 90s, which was at the dawn of the AI winter.
*  That was the last gasps of the old symbolic movement where in full swing at Brandeis when
*  I was there.
*  Thinking machines, for example, was in the process of folding and we had thinking machines
*  mugs in the department.
*  I was trained on Scheme and Lisp.
*  Everything was about strip, like AB strips and strips planners.
*  And so this was all before deep learning.
*  And after that, I went straight into hardcore neuroscience.
*  I was implanting electrodes into rats for my whole PhD career.
*  And then I sort of have come back around after a very long time to be sort of relearning
*  the fruits of this new deep learning revolution that we're all sort of experiencing.
*  It's really been a long trip.
*  Are you relearning with it begrudgingly or is it a new and exciting thing?
*  No, it's really fascinating.
*  I mean, I was skeptic and a curmudgeon at heart, but I can't help but enjoy the really
*  interesting things that we can do.
*  And in particular, after spending so many years building computational models that sort
*  of operate at a very abstract level where you've got like this is the neuron for the
*  letter A and the neuron for the letter B to build networks and models that actually deal
*  with real world stimuli, like images and etc.
*  I think that that's going to be a real game changer in allowing us to break out of the
*  sort of traps of low dimensional thinking that a lot of us have been in for a while.
*  If that's all that your model can handle, then it's difficult to build intuitions otherwise.
*  So yeah, it's been great.
*  I've been really enjoying this.
*  Yeah, I didn't realize you had the the GoFly background.
*  Long time ago.
*  Yeah.
*  You're another NYU language expert and well, I'll let you tell everyone.
*  I was going to tell everyone who you are and what you do.
*  Why don't you do that for me?
*  Sure, I can go next.
*  So my name is He He.
*  I'm currently an assistant professor at NYU, computer science, same as Ken He.
*  So my research, my current research is mainly focused on neural text generation.
*  And since I started the faculty job, I also branched out a little bit and also working
*  on how to make our natural language understanding models more robust nowadays.
*  And I think the work I'm most known for, if you look at the citations, are probably my work on
*  neural text generation, some less common applications, including textile transfer and
*  Pong generation.
*  What is that?
*  What is that Pong generation?
*  Sorry.
*  Adjournating generating Pong.
*  Oh, Pong generation.
*  Gotcha.
*  Yeah.
*  Okay.
*  Yeah, that was a fun project.
*  The work I like most was when we built a dialogue agent that can actually
*  collaborate with people and solving some puzzles.
*  So most of the dialogue engines are, if you look at this task-oriented systems where they help
*  people to book restaurants for movie tickets.
*  But I thought that project was very fun because we actually designed a model that can reason
*  about the need of the human partner and take initiative to give them information they need
*  to complete the task together.
*  And recently we also went further along the lines of this human model collaboration,
*  where we try to develop task generation models that can help humans write more creative text.
*  So I guess I've been always interested in this aspect of how can machine-inspired
*  collaborators as humans help them be more productive?
*  So bots, you just want to fill the internet with more bots, right?
*  Not bots, they're replacing people, but helping people.
*  I know that's what they're supposed to do, but don't they sell us stuff?
*  I'm not trying to argue with you, but I think bot has a negative connotation in my mind,
*  but I think you have a very optimistic outlook on it.
*  Yeah, I think they...
*  So sure, there are negative aspects where it's possible that if we just have bots
*  learning free online, they could generate very unsafe or toxic comments.
*  But I think if we try to build bots that can help people...
*  So yeah, it's tricky to find the right application where the bot can maximally help humans to improve
*  their productivity.
*  Hey, Paul, can I also ask some questions on the way?
*  Everybody, please jump in and ask questions, yes.
*  So I had actually one kind of conflicting message I hear here is that, okay, so you work on the
*  pun generation. And so pun generation is connected, let's say, having fun, being creative and so on.
*  And then you talked about helping humans be more productive, but isn't having fun and productive
*  opposite notion? And then you had machines actually help us doing both or does it have to
*  choose one of them? I want the machine to choose fun, but I'm pretty sure it's easier to optimize
*  the productivity, my guess is. What do you think?
*  So by optimizing productivity, I don't think it's conflicting.
*  So they can... I say the same by making people more productive or making humans working more
*  as opposed to having fun.
*  As opposed to having fun, yes.
*  Aren't they the same thing though?
*  Yeah, exactly. It can help you to complete your task in a more fun way, I guess.
*  Okay.
*  It would help with motivation for sure, right? I mean, if you get people to enjoy the workplace
*  environment.
*  Yeah, so I guess we want to move the tedious part to machines and like humans focus on more
*  interesting part of the job.
*  Joe, you share with her an appeal to conversation with machine... What is it called? Machine
*  conversation? Machine...
*  What is it called?
*  Conversational agents is what I like to call it these days.
*  Who are you, Joe? And what do you do? And what are you most proud of, etc.?
*  Yeah. So I'm an assistant professor at NYU, but in the Stern Business School,
*  in the Technology Operations and Statistics Department, particularly the technology subgroup.
*  And yeah, a lot of my work focuses on conversational agents and a lot on evaluation
*  of them. I think I'm probably best known for evaluating conversational agents and doing
*  a lot of work recently on evaluation. And, you know, my focus, the business school aspect
*  of my focus is really more on understanding how these conversational agents, how to use them
*  properly within business. And particularly, I'm interested in healthcare and public health.
*  So I do a lot of collaboration with people in public health.
*  And so that's probably what I'm best known for. Okay, I'll answer in two parts. The first one is
*  what was the most fun. So the most fun project that I've worked on. So I worked on some work
*  early in my PhD on spectral sign clustering.
*  You have to describe that very briefly. You have to describe that, please.
*  Sure, sure. So there's this work on taking the similarity between different items,
*  and then figuring out how to take that similarity matrix and use the
*  most common features using singular value decomposition to cluster items together.
*  The signed part is figuring out how to incorporate opposing signal. So instead of
*  similarity, dissimilarity into this matrix, and then cluster. So that's what's called the
*  sign spectral clustering. But the fun part about that, so the sign spectral clustering is cool,
*  but the fun part is one of the biggest problems that I see all my friends having is figuring out
*  how to assign people to tables in a wedding. And so I worked with a friend of mine on actually
*  figuring out how to do, how to change this sign spectral clustering into a constrained way in
*  order to figure out the wedding seating problem, which is you have a whole bunch of people,
*  family and relatives, some of them know each other and like each other, some of them don't
*  like each other, which happens, unfortunately, and then how to actually figure out how to seat them.
*  And it's one of those things where people spend a ton of time. And there's like, we actually built
*  a web front end, which unfortunately we didn't have time to finish, but we have,
*  if anybody's ever interested, we've got an algorithm and some code to actually tell you,
*  you know, in some theoretical way, how to actually do your wedding tables.
*  So where do I put it?
*  Joel, how do you, sorry, but how do you evaluate it? I mean, you work on evaluation, you said,
*  but have you actually evaluated your algorithm for, I don't know, actual weddings and then see if
*  people were happier or, I don't know, angry or whatnot?
*  So it's a really good question. We never got to that stage. I mean, what we can evaluate is how
*  many people like that don't like each other sit together and how many sort of, you know, sort of
*  reject tables there are, which end up being the people who are isolated nodes in our graph.
*  But yeah, no, we never got to the evaluation component because we never actually,
*  I think there was one friend that used this for, you know, just like a corporate setting
*  where people had tables and they didn't want certain people in groups to sit together. But
*  yeah, it was fun. It was just fun. And we used Buffy the Vampire Slayer as like,
*  characters in that as an example of like how it would work. So it was all silly, but it was great.
*  It was a fun paper. It's on archive. Okay. So then, so stuff that I'm most proud of.
*  So we have a set of work on essentially medical question answering,
*  which is some of which is published, some of which is now unpublished. And what we're trying
*  to do is figure out with these young women in Uganda, how to build conversational agents
*  that can help title medicine people to actually help young women with questions about maternal
*  health. I love like the very theoretical side of my work, and I really enjoy doing the applied
*  side. And that's so some of the stuff that I'm, I like the impact of actually, you know, helping
*  people. I wish I knew what that was like. So, all right. So very good, everyone. So part of the,
*  this week's materials, I believe, were convolutional neural networks and recurrent neural networks. And
*  I don't think we're going to talk much about those because that's not where everyone's expertise.
*  Well, I mean, I'm sure everyone's an expert in those as well. But, you know, just to
*  briefly mention them. So the deep learning, quote unquote, revolution in 2002,
*  with AlexNet happened, and that was a convolutional neural network. And since then, those have become
*  standard for vision and lots of other things. But, you know, I guess I would like to know.
*  So the story is that's when the revolution happened. And that's when everyone realized,
*  oh, deep learning works. Is that the story? Like, what was your experience when the error dropped
*  by, I don't know, six percentage, you know, and that was a huge, it was probably more, I don't
*  remember the exact percentage, it was a large percentage drop in the error on the ImageNet
*  data set. And in your worlds, were people throwing confetti and saying the revolution is here? Or
*  what was your experience? Because Kyunghyun, you were working on restricted pulse machine,
*  for instance. So yeah, that was a mistake. So in 2012, summer, there was an error in the
*  2012 summer, there was a, if I remember correctly, three week long summer school,
*  hosted at UCLA, the IPAM there on deep learning that was hosted together with the CIFAR and so on.
*  And then Jeff Hinton was one of the speakers there. There were about 40, 50 students, I was one of
*  them. And then Jeff actually broke the news about ImageNet there, one of his lectures. And then,
*  you know, like everyone was sitting there. And then as soon as Jeff talked about it, and then,
*  at the end of the day, it was really just a convolutional network and dropout, right? So
*  dropout was a big thing. So there's nothing much to explain. So as soon as Jeff said something
*  about it, and then he started talking about, oh, you know, I have some intuition, it has something
*  to do with the evolution, biological sex and so on. Everyone lost interest. And then they all
*  started to quote it up because dropout was so easy to implement anyway. And then people started
*  implementing it. So in some sense, it was very surprising to all those students who were actually
*  working with these restricted boson machines, the convolutional net in a very limited form,
*  or the sparse coding and so on. All the things that we were working on as PhD students or postdocs or
*  whatnot, actually were working, except that all you needed was a bit of magic here and there.
*  In some sense, we were building everything toward this moment. Just like Jeff Hinton and
*  Alex Krzyzewski, they kind of came up with a couple of tricks that pushed it, the whole thing.
*  So it just tilted toward this success.
*  Because one of the things that restricted Boltzmann machines were good for was stacking them was
*  doing basically an unsupervised pre-training that then you could stack the model, pre-train it,
*  and then it would all of a sudden become a good classifier with a little fine tuning from back
*  propagation. And so is that what you were talking about that you guys were working toward that?
*  Yeah, I was working toward that. A lot of people were working toward that.
*  But the weirdest thing is that, you know, like the young LeCun, Jan was able to train this
*  reasonably deep convolutional network already in the early 90s, mid 90s, but somehow he couldn't
*  actually scale it up because there were just a few missing pieces. And then that's why we had to take
*  all those, you know, long detours, you know, trying to come up with a restricted Boltzmann machine,
*  how to train it, stack them up, fine tune it, and so on. But at the end of the day,
*  it's probably not a revolution, but it's more like, let's go back to, I guess, 90s. I think,
*  Brett, you're referring to the beginning of the winner, and then just realizing after about 15 to
*  20 years that, well, we actually had a lot of solutions or the answers already back then,
*  just needed a couple of, let's say, tricks that's going to tip the balance toward the,
*  let's say, summer side rather than winter side. That's how I view it. And then, Brett, you probably
*  knew the answer already in some sense, like 99%. Just Jeff had to come up with dropout, I guess.
*  Yes.
*  I mean, I think that's one of the most challenging aspects of deep learning,
*  which is that success involves not just having a good idea about how to do something, but also
*  a lot of time and effort spent doing the fine tuning to get it there, right? And,
*  you know, coming from, so I'm from the sort of bespoke modeling side of Comp Nero,
*  where we like design these sort of like, handcrafted neural circuits where this neuron
*  talks to that neuron with a connection weight of this much. And, you know, there, progress is a
*  lot more rapid because you have an idea, you can implement it like your intuition can handle it.
*  But on the deep learning side, it seems like there's this extra barrier of a lot of
*  hours of elbow grease spent working the problem in order to make your good idea,
*  or even to test if your good idea is actually a good idea. So I think that's one of the challenges
*  there. And I think it in some ways also a barrier to, you know, smaller labs and,
*  and, you know, smaller groups, especially those with less funding, because you just really need
*  that extra time. And Brad, I mean, why, before you finished, were you, did you have that sense?
*  Did it was it a clear demarcation that deep learning is here or what? I was living in a
*  different world at that time. Okay, like I was completely oblivious of all of this stuff at 100%,
*  not until like, I don't know, like, maybe six or seven years ago, did I start tuning into things
*  like this. Yeah. But huh. And Joe, what do you got? How about you guys? Have you even worked
*  with models that aren't deep learning models? This is a terrible question to ask. I realize.
*  Yeah, I can provide some perspective, some of my perspective. So the first time I learned about
*  neural networks was in undergrad where I implement backpropagation in MATLAB. And then I started my
*  grad school in 2011. At that time, I think for computer vision, maybe people are already
*  accepting that neural networks is really the next big thing. But for NLP, I feel people are
*  definitely not early adopters, at least in my lab. Like we were still using support vector machine
*  as far as market models, not neural networks until maybe 2015 or 2016. And I think as Brad and
*  Kena mentioned, I agree that for the pioneers like Jaffer Young, they had lots of trouble. They
*  have to come up with some tricks to make this neural network work. But I think by the time of
*  2012 or 2014, for downstream applications are already some well-documented practices or
*  tricks that can make this model work. But somehow at that time, I think so in retrospect, I think
*  that was a misconception because my impression was at that time when I was a PhD student is that
*  it's extremely difficult to make this model work. But when I tried it for the first time
*  around 2015, it's actually not that hard. I tried a set of hyperparameters and it just works as
*  in other models. So I think that actually slowed down people's adoption of those neural network
*  models and there are other blockers where some people don't think that it's interpretable or
*  reflecting any properties of language so they may not work as well. But it turned out that this model
*  actually be more powerful than the symbolic models we use these. Oh, you're welcome.
*  Oh, you know, yes, I think that's a little to make it easy.
*  Thank you, Kyon. I'll say it. I'll say it. Joe, what was your experience?
*  Yeah, so I think a lot of my experience came from doing machine learning, I guess, in another field
*  and transferring over to natural language processing when I started grad school. So
*  finance, it was all about feature engineering. And feature engineering at the time was like the
*  thing that I knew how to do and support vector machines and kernel regression. And then, you know,
*  I moved into more of the hidden Markov model world, which I still love, but is now completely
*  supplanted. I saw the full sort of spectrum of supplanting of HMMs by, you know, these
*  recurrent models and then transformer models. And yeah, I think, you know, to some extent, seeing
*  that happen, it when, you know, sort of the sequence to sequence model came out at EREPs,
*  everybody was like, very interested in it already, like the fact that it works, you know, and why do
*  you need to reverse these things, you know, and all those components. And, you know, I think I
*  learned like six packages along the way and re-implemented five times. And now I see the
*  grad students that I work with, you know, install a package and things run, right. So, you know, I do
*  agree that for very hard problems and like new things, there's still dark magic of like making
*  stuff work in deep learning. But at the same time, there's a lot of time that's not spent on
*  feature engineering, which is partially a little bit problematic because I find that, you know,
*  my students tend not to look at their data and feature engineering really requires you to look
*  at your data. But at the same time, I mean, the representations are just more powerful.
*  Another memory occurred to me, which is that when I was in high school, actually, that was when I was
*  playing around with neural networks. And I was trying to get a back prop network to learn how
*  to recognize characters and I couldn't get it to work. It was just like failing every single time.
*  And this was me, basically me running into that wall of sort of not understanding you can have
*  the algorithm correct, but there's some underlying problem in the way it's set up. And so I called
*  Jay McClelland in his office from high school and said, I called him on the phone just to say,
*  could you help me with this? And I described the problem and he was great. He basically encouraged
*  me to double check the algorithm and et cetera. I mean, what could he do?
*  But the fact that he spoke to you. He answered the phone, right? It was great.
*  That doesn't surprise me. I've talked to Jay and he seems like that kind of guy. So that's great.
*  Exactly. So anyway, so I couldn't get that model to work no matter what I did. And that's why I
*  needed symbolic processing. Here we go. All right. So let's start off talking because
*  I have a feeling that we're going to end up talking about natural language processing
*  a lot here. But part of the week's materials covered generative models like variational
*  autoencoders and generative adversarial networks. And Brad, you use variational autoencoders.
*  Well, you've started using them. I mean, you used these, I'm trying to think of,
*  what kind of model did you call them? Bespoke. Oh yeah, no, right. Yeah. I'm trying to think of
*  someone, someone, a well-known brain neuroscience researcher talks about the cottage industry
*  and how it's important in neuroscience for it to have these small labs that are doing
*  these experiments that are fairly small rather than the big collaborative multi-lab collaborations
*  where everyone's using big data and big models and stuff. And so you've kind of stepped through,
*  you've come through that bespoke cottage industry and you're still there, I guess,
*  but now you're using the variational autoencoders to do what? Yeah. So sort of a new direction for
*  me. What we're trying to understand is how we can use variational autoencoders to build
*  good latent spaces to understand how working memory might be stored in the brain. So working
*  memory is thought to be like a keystone of our sort of larger abilities to think and reason,
*  because it lets us hold onto information in very flexible ways and access it and manipulate it.
*  So what you can get out of variational autoencoders, at least if you're just going to,
*  for example, look on the vision side is a way to build a series of latent spaces that let you
*  store information at various different levels of compression. And so why that's useful is that when
*  people remember things that we experience, you know, I can show you something that's completely
*  novel, like a shape that you've never seen before. And you can build a memory of that. You could even
*  draw it, you know, in a generative sense. But also if you're, if I show you something that's familiar,
*  you can more easily remember it. So there's some advantage of that familiarity. So what we've been
*  doing is taking VAEs and using them to build these latent spaces and then constructing memories out of
*  subsets of those latent spaces in a way that would be consistent with the task you're performing.
*  Right. So if you see something, you can build a memory of that thing, but you do so in a way
*  that serves what you're trying to do. Right. So you might be focusing on the visual details
*  of like a car. You might focus, you might remember that it's got a dent on the fender,
*  or you might just remember that it was a car of a particular make and model.
*  And so you can sort of have a memory that sort of runs the gamut of being anywhere from the sort
*  of low level visual detail to the higher level conceptual category or some combination, right?
*  You can have a memory that is both the sort of conceptual content blended with the visual details.
*  And so VAEs give us a nice way of having a series of stage latent spaces, and you can build a memory
*  by combining different parts of those latent spaces, storing that information, and then
*  reconstructing it back into the latent spaces. The other really nice thing that we can do with VAEs
*  is that we're playing around with, right? So, you know, in the typical sense of these models,
*  you've got like a single pathway, right? Where each space sort of feeds into the next one,
*  you know, even like a ResNet-50 is basically like a big line of these things.
*  But what you can also do is you can sort of goes back to like the bespoke thing where,
*  you know, the human mind in contrast, has, you know, instead of just one pathway forwards,
*  it's got a number of different pathways. So as soon as information hits the visual cortex,
*  it starts exploding down a series of different pathways, each of which emphasizes different
*  kinds of information. So you can do the same thing with VAEs where you so just as an example,
*  what we're doing right now is just, you know, we've got this VAE, and we pull apart the
*  shape and the color information from a stimulus. So we've got one of the bottlenecks that is only
*  trained to represent color information, and the other is trained to only represent shape
*  information. And we do that by having two different objective functions. So the information
*  basically flows through one, and then we train it and we zero out the gradients. So if we want to
*  train on color, you know, we zero out the gradients for the shape side. And if we train on shape,
*  then we zero out the gradients for the color side. And the VAE basically learns to separate
*  that information to different representations, and then merge it back together again.
*  Don't you have two sets of latent spaces to do that with to channel it through?
*  You do right? You've got like so imagine a VAE, we've got like L1 and then L2. And then the
*  bottleneck is actually two subparts, but then they merge back together again, at the fourth layer and
*  the fifth layer. So the VAE basically learns to split the information then merge it back together
*  again. And this is it's really interesting, because this is taking us down pathways of
*  thinking about how imagination and visual imagery works, your ability to sort of
*  imagine combinations of things. So we can tell this VAE, you know, I want you to imagine a red
*  two, and it will generate a red two for us by reactivate two on the one side and red on the other.
*  But what it can't do is it can't remember, it can't imagine or generate combinations that
*  hasn't seen before. And so if it's seen 1234 in blue, and 5678 in red, it can't do a two that's
*  red. And so this sort of gives us some pause to think about, well, maybe the purpose of imagery
*  is to sort of develop ways to generate those combinations you hadn't seen before. So the
*  encoding pathway, maybe doesn't have that, that ability is never experienced that particular
*  stimulus before, but the decoding pathway might be able to nevertheless give it to you.
*  So there's a lot of really interesting ideas that we're having, just, you know, starting from
*  this working memory model, and now sort of starting to think about imagery and imagination.
*  So, Brett, I have actually one question along this line, because this is the problem of the
*  compositionality and the systematic generalization in some sense, right. So the one thing, one thing
*  that we've run into as in the natural language processing research, in particular, actually,
*  how has been actually looking into this quite a lot is that there seems to be a kind of fundamental
*  limitation that comes out of just observing a static data. For instance, you have the one example
*  that I always use is that when we train a machine translation system on a small, let's say, corpus,
*  and then let's say somehow in that corpus, banana, the word banana always appears after the word
*  yellow. And then can this machine translation model be able to translate green banana correctly? And
*  then if so, how is it, how can it actually disambiguate the fact that the yellow is a color
*  and does not actually determine the property of the object that is the banana, right. And then you
*  are statistically saying, I don't think there is a way forward, and that there has to be some kind of,
*  I guess, the role that bespoke models actually serves here, because it seems like the data alone
*  is not enough to have you actually, and then I think you're actually touching upon this, right.
*  So if you have the separate channel for, let's say, colors and shapes, then perhaps it's going
*  to learn. But what you're saying is that it still can learn the kind of new combination. Is that
*  what you meant? Well, yeah, at least these straightforward VAE architecture cannot,
*  you know, with fully connected networks. But, I mean, if you were using transformers or something
*  else which had more flexibility, perhaps you might be able to do that. But yeah, with regards to the
*  bespoke thing, right, so we're sort of assuming here that the brain would have these pre-existing
*  differential objective functions to encourage that information to bifurcate into different pathways.
*  Yeah. Right. And that's the sort of not data driven, but perhaps, well, I guess you could
*  say it's not data driven within the lifetime of the organism, but perhaps data driven on the
*  species level, right. In terms of like designing how that works. I have a follow up question.
*  Sorry. Yeah, so the follow up question is, so here are the model automatically learning
*  what are colors, what are shapes, or it has to be, you have to tell the model that, okay,
*  here's the coloring part in the image. So the stimuli that we're using are really simplistic
*  in that they only have one color. So if you can imagine like MNIST digits, but they're just like
*  colorized to be one of several colors. And the objective function that we use sort of
*  enforces it to learn about color or shape. So to enforce it to learn about color,
*  you just collapse all the spatial information together and you're just learning the RGB
*  of that stimulus and to learn shape, you collapse across RGB and you just train it to learn about
*  the shape information. So in that sense, the distinction between shape and color is baked
*  into these bespoke objective functions. Which I mean, it's not completely crazy. I mean,
*  the brain has a lot of very unusual ways in which it can process information.
*  The VAE is also a really interesting way to think about how vision is organized. Because you go up
*  to the bottleneck and then instead of going forwards from there, you can think of it as
*  actually going back down the visual pathway. So you go from V1 to V2 to IT cortex, but then
*  the return pathway is from IT back to V2 and then back to V1. So in actual fact, the first and the
*  last layer of a VAE, you would think of those as both being within visual cortex, just perhaps on
*  different layers. And it's really easy then to imagine, you know, from a biological perspective,
*  how you would do the objective function because the neurons are literally
*  sort of next to each other by the time you go from L1 back to L5.
*  That's one pathway. But like you said, I mean, the brain is just this huge
*  explosion of diverting pathways. So you need a VAE there and then another one to go forward
*  and then sideways and all which way. Yeah, right. Well, you also have one, you know,
*  for the auditory stream. Yeah, so like for the auditory side, but also for motor and
*  proprioception, you could easily imagine a similar kind of mechanism there. Each one of these
*  was sort of build an organized set of latent spaces, perhaps with some genetic predispositions
*  to sort of divide things in certain ways. So there's this huge debate in our field, for example,
*  about whether the fusiform face area, which is a brain area that lights up in a magnet in an fMRI
*  when you see faces, like is that genetically preordained to be a face specific brain area,
*  or is it just that that is an expertise area that tends to end up focusing on faces because
*  that's the thing we tend to become experts in. So there's this huge debate about, you know,
*  whether or not that is genetically preordained or whether that's an outcome of the data that we
*  experience. So you could imagine also like a sort of objective function that is geared towards faces
*  that sort of like emphasizes that only face information gets processed through that bottleneck.
*  And then you could combine that information. Then, you know, basically, when you're experiencing
*  something, it would be a conjunction of different latent spaces, right, you've got one latent spaces
*  specialized for faces and other for certain kinds of shapes, colors, etc. But yeah, but then, you
*  know, then you think that they, you know, information travels forward, it bifurcates through
*  all these pathways and different latent spaces. But then when it comes back to V1, that's when
*  you're recombining all that information back together again. And that would be the process
*  of visual imagery, the sort of reconstructing in your mind's eye, what something is. And then,
*  you know, you can ask other really interesting questions about like, you know, to what extent
*  does someone's phenomenal experience of visual imagery tell you about what's going on in that
*  machinery? Is that epiphenomenal? Or is that indicative of a fundamentally different way
*  in which that return pathway functions? Yeah, so a lot of really interesting questions there.
*  I don't know, just listening to this, it's really fascinating how much we know about how human brain
*  processes this visual information as well as the auditory information and then how, you know,
*  like you were able to actually explain this complicated process, I presume, in a very succinct
*  and also the probably the precise way, you know, how we get the abstract level. And, you know,
*  whenever I think about it, and in the context of the natural language processing or the language
*  processing in general, I'm just not even sure, you know, where we should start in a sense that
*  we often start with the text in natural language processing. But clearly what we see as humans is
*  not really text. We look at every single pixel, the strokes or what not. So how do we actually get
*  to that kind of abstract level? Or is language actually abstract? Or is it actually even more
*  low level than we imagine that is? And then what is the right kind of, let's say, should it get
*  compressed over and over? Because the weird thing is that these transformers or the LSM or what not
*  that we've been working with, the input tends to be much lower dimensional because we always use
*  one-off vector. But then we kind of blow up the dimensionality like, you know, like enormously
*  as we go over and over the more and more layers. So I don't know, what do you think, right? I mean,
*  can the explanation you gave be made analogues to the language processing in the brain as well?
*  Or is it something completely different? Yeah, so I guess I would say that the best way that I would
*  advise to approach it is to think that there might also be different latent spaces on the
*  vision side of language processing, right? So you might have some latent spaces that focus on the
*  shape of the word, like the outline characteristics, which we now think is one of the ways in which
*  people recognize words quickly. And another pathway that emphasizes the letters, and maybe
*  another pathway that emphasizes combinations of letters, and sort of all of those are working
*  in tandem, not necessarily in sequence. And so the outcome that you get is a product of those
*  things working in parallel. I mean, the vision system is one system in the brain that we probably
*  know best of all the brain layers and anatomy connections and representations that are in there.
*  All the other ones are catching up as well, but language is still pretty elusive. And
*  the attention mechanisms in language that led to the transformer is just so powerful. And there's
*  work being done to see, is this how, when we use a language model like that, train it on Wikipedia,
*  the corpus or something, and then look at the structure of the language, there is some linguistic
*  structure that it comes up with. But on the other hand, we really have no idea how language works
*  in the brain. So I wonder how working with language, and Kyonyun, you were just talking
*  about the different levels of abstraction, and I was going to ask about this anyway,
*  because the transformers could be used for the lowest, at the pixel level, or at the word level,
*  or at the sentence level. And I'm wondering how you guys, how you NLP folks, and especially,
*  once you get into the conversation with the, I was going to say evil bots, the
*  beneficial bots, the conversational agents, how you guys think about language and how working
*  with the language, training these models, has sort of altered or changed your mind at all about how
*  you think language works in our minds and our brains? Right. So since I haven't really worked
*  much with the conversation, I'll start with a much smaller unit, and then I'm going to let Ho and Jo
*  kind of take a much bigger view into the idea how language is, because at the end of the day,
*  language is a communication medium that probably sets this apart from many other modalities that
*  we think about, like the visual or the alt-tri and so on. So when I started working on this
*  particularly with machine translation in 2013 and so on, everyone was looking at the sentences
*  as a sequence of words. So we built the neural translation system just like how the existing
*  statistical translation systems are built by looking at the sentence as a sequence of words.
*  But then what I realized is that I was implementing the whole thing, we were running
*  all those experiments, and then we realized that, wait, hold on, all my neurons assist is literally
*  a sequence of integers. It's just an integer sequence where the integer just refers to the
*  index in the vocabulary. So we're like, perhaps it doesn't have to be words. And then you have
*  to, of course, people who had more experience working with the natural language realize that
*  well, you just replace it by some kind of simple segmentation, I go with them to have some kind of
*  subword vocabulary, it still works, and then it actually works better because we get a much more
*  compact vocabulary. And then we're like, perhaps we can just work with letters.
*  So initially, what I did was to, okay, we're going to use the input, a sequence of words,
*  but we're going to ask a neural net to generate the translation as a sequence of letters.
*  And then it actually worked beautifully. And then the attention was able to attend to the relevant
*  words for each letters. So there was a huge discrepancy in the levels of abstraction between,
*  let's say, letters and words, but still the attention was worked as well as before, you know,
*  because it was all working internally. And then that's when we realized that perhaps everything
*  could be just letters. So we built the character to character translation model that actually
*  worked pretty well. There were some computational issues, but I did that aside because I'm pretty
*  sure Google can always solve it for us anyway when it comes to computational issues. And then,
*  you know, what people at Google indeed worked on was that perhaps we can just work at bytes,
*  or perhaps even bits. So there were some papers just showing that we can actually work with bits
*  or the bytes or the Unicode bytes. And then still the models tend to work pretty well.
*  And then this actually does tell us a lot about what kind of abstraction that this
*  neural net can make out of, let's say, really nothing. As in, this is just a sequence of
*  integers at the end of the day, and it's going to build up some kind of representation. Of course,
*  whether those representations are meaningful externally is a different story, but I think
*  that's what we have seen. And then that's the reason why I asked this question initially to
*  Brad is that what is the right level of abstraction to think of language to start with? But I'm pretty
*  sure it gets much more complicated when we think about conversation. Hello, Joao, I'm pretty sure
*  you can tell us more. Yeah, actually, one follow up question slash comment on what you said about the
*  character based models versus like word based models. So I guess this is getting a question of
*  so how much of the information or knowledge do we want the model to simply learn from data versus
*  building the model architecture? So the I suppose if we use character based models, you need more
*  data to achieve similar performance. Or is that true? Yes. Yes. And no. So the one issue people
*  have run into, including myself, is that they, you know, when we look at the sentence as a sequence
*  of words, or as a sequence of letters, sequence of characters is just suddenly is so much longer.
*  So it takes much more compute or the time to process the whole thing. So often is the
*  computational bottleneck we run into, even if we have the same amount of data. But there was a
*  paper from Google Montreal showing a couple of years ago showing that if you spend tons of the
*  same compute, which you know, Google should do for the, you know, for the benefit of humanity and,
*  you know, scientific community. So they did it and they turned out that the character level models
*  do work as well as word based models with a similar amount of data. And then when the amount
*  of data was smaller, actually, it was more of a mixed result. It was not necessarily the word
*  based model was better. Not sure why that is the problem because some of the words becomes
*  suddenly so rare that the model can't really learn from a small corpus perhaps.
*  Yeah, that's interesting. Right, I think maybe I can share some of my experience working with
*  the dialogue agents. So I think when I first started working on dialogue systems, I wasn't
*  trying to build any complex systems like LXL or some social tables. We were constrained to a very
*  simple setting where, you know, the game is like you have two agents are trying to find their
*  mutual friends. And the things they talk about are extremely simple. Like, we have maybe 100 names for
*  people and then they went to different colleges, they work at different companies and the two
*  agents are going to exchange such information to find their mutual friends. But then soon I realized
*  that even with such a simple environment, there's like three attributes they have to talk about.
*  The different types of the variations in the expressions is still huge. So that we cannot
*  handle all the different different ways of saying the same thing, especially when the model wants to
*  express conjunctions of different attributes. So then this involves some logical operations.
*  And then I realized that no matter how much restrictions we put on the work, we have,
*  like the easiest one, I think people have worked on is the blocks world. You just talk about
*  triangles, cylinders, several colors and the position of these objects. But still,
*  because of the compositionality and language, there are so many different ways you can talk
*  about these things. And it's still quite challenging for machines even in such simple words.
*  The other thing that I didn't appreciate much before I started working on LP is the
*  subtlety of meaning. So sometimes even a single word, I can change the meaning of the sentence.
*  So remember, when we worked on the pound generation project, so when we were just looking at the
*  outputs, we're trying to tell which of the outputs are more funny. And I forgot the exact example,
*  unfortunately. But remember, the one example, there's a single word, which is actually,
*  and that word can change the meaning of the sentence entirely. Because once you have actually
*  there, that means that you assumed you didn't expect something happened, but then it happened.
*  So that changed the whole thing there. And then I realized, okay, so for this subtle meaning,
*  is I don't really have an idea of how our account model can capture these things by just
*  learning on tons of data without additional supervision or additional interaction with people.
*  One quick thing is that this is the reason why I really hated year 2017 when every single master
*  student at NYU knocked on my office door and then told me that they have idea to make GANs work for
*  natural language text generation. Without realizing that you can't really compute the derivative or
*  gradient when the input space is discrete and the length or the size of the space changes.
*  That just reminded me of this. Yes. Right. The GANs got a lot of popular around 2017. But the
*  I think it was our papers that they don't work better than a standard on new models.
*  Yeah. You can compute the gradients, right? When the variable is discrete. And then
*  none of the students actually realized that until I just told them,
*  now can you write the gradient on the whiteboard for me of this variable where X is a discrete
*  variable? And everyone was like, this? No. No. And then they all left.
*  Yeah. I guess students tend to get attracted to more
*  fancy techniques. After even last year, I have students in my final project working on GANs
*  for text generation. Did they pass the course?
*  Yeah, they did. I think it was a lot of effort anyway, even to make that model train.
*  Right. Yeah, I was just going to jump in and say that I think it's really interesting to think of,
*  you're talking about puns and humor, right? And that's, if you want to focus on the true
*  understanding of text, I think humor is probably like the most, one of the most subtle ways of
*  doing that, right? It's one of the, like in order to get humor, right, you need to have a very
*  accurate model of what you're saying, how you're saying it, and also the mental model of the person
*  who's doing the receiving, right? And so it's really focusing on a different, I think it
*  puts the game up at a much higher level than just like understanding like who walked into the room
*  and did what. You need to sort of understand their mental model. Yeah.
*  There is a lot of social and cultural. Does that ring true to you, Jiao? Because,
*  and on the one hand, you send Wikipedia into a transformer, and it can generate pretty good text.
*  On the other hand, it's not conversing. I mean, is that what is really missing? Is that why you
*  guys are interested in the conversational aspect is because it brings a new challenge that is
*  specific to language? Well, yeah, I mean, I can say at least, you know, my interest in it really
*  spawned from the fact that, you know, a lot of language is about communication, and much of
*  communication is about communicating with other people, which makes, which does make the task
*  that we're trying to do a lot more complicated. Oftentimes, what we need is to, like we were just
*  talking about, find a mental model of the person. And this does challenge neural networks in a very
*  specific manner, meaning that suddenly we have to, you know, actually encode information that is not
*  just vectors that can represent something in a latent space, but also now actually build
*  representations which are meaningful situationally. And, you know, that to me is like super,
*  super interesting and also obviously extremely challenging. You know, I think that when you're
*  doing not to knock on translation, but when you're doing translation, there are shortcuts that can be
*  made that don't require like necessarily having as much meaning representation there, right?
*  Whereas I think when you're starting to talk about dialogue and you want to do a complicated task,
*  and you want to have the person have fun, then all of a sudden, you know, this opens up a whole
*  new world of problems. I will also just as a small tangent, talk about something that I think for me
*  has become interesting a lot, and I think it's interesting to a large amount of the community,
*  which is that, you know, the amount of bits that we give to our transformer models versus the amount
*  of bits that come into a child are very, very different. And to some extent, I think one of the
*  large challenges that we have at the moment is understanding, you know, there's these new papers
*  on scaling laws for language models. And trying to understand, like, if you look at the scaling laws
*  for people and scaling laws for language models, they're very far apart. And, you know, part of that
*  could be architectural, obviously, Brad knows a lot more about that than I do. But it's still an
*  interesting challenge also in terms of understanding, like, what does it require, you know, to learn
*  and train these agents with, I mean, maybe we need to go multimodal or something, but
*  it seems very strange that we need, you know, trillions of words in order to train these models.
*  Yeah, it's on the vision side, it's been interesting that for a long time, you know, it was
*  speculated that the reason the vision models aren't doing better is because we don't have data sets the
*  size of what a human experiences like within the first few years of life. But now, the vision data
*  sets are way bigger than what a person experiences in some cases in their entire life, right? And
*  we're still running into the same problems. So we've sort of solved the data set size problem.
*  And we're now seeing what other issues remain, at least on the vision side. And I guess, yeah,
*  it's clearly true the language side as well. Do we know what language is for? Isn't it for
*  getting things from people? Isn't it for advancing our own agendas so that we can mate and etc?
*  I want someone to disagree with me, by the way. I'll disagree with you. I think language is about,
*  you know, we go through life and we build models of the world and language gives you the ability
*  to transmit your model of the world to other people. And that's crucial for inheritance of ideas.
*  I'm happy to be more cynical than that. I think that that's a way too optimistic, angelic
*  vantage point. What do you guys think? So I have actually one thought is that the
*  so one small sub area that I worked on for a couple of years is called immersion communication.
*  That is where we assume that we have multiple agents that are trying to solve problems either
*  collectively or, you know, they compete with each other. And then what we do is that the unlike
*  usual multi-agency, let's say simulations, we give them a pretty rich high bandwidth communication
*  channels. But of course, we don't really designate any protocols that they have an option to
*  evolve or develop their own communication protocols. And then one of the goals there is to
*  see if these agents collectively can explore the environments better, collect more, a richer set
*  of experiences that can be shared in order to solve the problems better or compete better against
*  the other set of agents. And then the reason why I brought up is that in one of those workshops,
*  so we are organizing your workshop on immersion communication and neuro-resolver two to three
*  years. And then one workshop we just randomly invited Juergen Schmidtuber. And then Juergen's
*  first remark was that the, I don't know what is so special about immersion communication, because,
*  you know, from his perspective, every layer of any neural net is developing a communication
*  protocol to talk to another layer that is adjacent to each other. And in particular,
*  in recurrent network, that's even more interesting because layers are talking to each other,
*  all the different copies from the different time step. So in that sense, perhaps this is even more
*  cynical than, oh, your take is that perhaps the language is really nothing but just, you know,
*  one layer or the shared weight across all those neural nets that we have in our head. Maybe that's
*  about it, right? But language is supposed to be the most special thing in the universe, in our
*  universe, but it separates us from the brutes. It is the, it's supposed to be the highest abstraction
*  and involve all of our other cognitive abilities merging into an abstract representation. But
*  that's why I'm wondering is, like, the language models that you guys are working on and developing,
*  you know, does that jibe with your experience, you know, or is language not so special?
*  I'm actually known to say that meaning is overrated.
*  All right, you and me, we've got to go have a beer sometime.
*  Yes, yes, we should.
*  But, but so but there's still a lot languages missing, right? With the conversational agents,
*  I think that really jumps out at you. Is that correct?
*  The models, I think right now we don't really have a good way to evaluate these models,
*  these language models understand language. I mean, they're good at solving the practical
*  tasks we want them to solve. But then for more challenging tasks, like communicating with people
*  or understanding humor, I don't think we're or even for a standard has you want to like,
*  Brad and can you mention about this computational generalization, if you want to go out of your
*  training distribution, these models are very brittle. So it depends on, you know, if we just
*  want them to perform a specific task, then maybe the current models are sufficient without
*  understanding meaning and whatever meaning means. But I don't think we are,
*  we know how to evaluate how well this model actually understand language like humans do.
*  All right, we're getting close to time here. But I have I have two more things I would like to ask,
*  at least, and I don't care how long we go. But one attention, and Brad, this is kind of directed
*  toward you, pitting you against the rest of the panel here, I suppose, because you've worked on
*  I'm putting an air quotes attention in as we know it in psychology and in neuroscience,
*  or as we don't know it really, you know, in many respects, or as we think we know it,
*  and different kinds of attention. And then Cunha comes along and makes this model that you didn't
*  call it attention, right? It got no, right. And then it got the label attention later. And now
*  has NLP usurped the word attention? And what? So the NLP panel, folks, are you guys happy with
*  the word attention? And, and I'm gonna let Brad start if he's happy with the word attention.
*  So I think, I guess my controversial take is that attention as it's used in the context of
*  transformers is exactly the opposite of the way that we typically think of attention in cognitive
*  systems, right? So attention in transformers, as I understand it, is a thing that is learned,
*  and it operates in a very specific way, depending upon what stimuli are coming in.
*  And in that sense, and it also operates in parallel, right? And so in that sense,
*  it's more akin to what we in the cognitive side would call an automatic process, something that
*  kicks in when particular stimuli, you know, hit a series of particular representations in a specific
*  way. And a whole bunch of things can happen really fast in parallel. Whereas when we think
*  of attention, or at least when I think of attention, in the sort of canonical mind way,
*  it's what's called a controlled process, and a controlled process is exactly the opposite of
*  that. It's effortful. It's very flexible, you can control it, but it's also slow, and it cannot
*  happen in parallel. So again, it depends on your definition of attention, my personal definition
*  of attention is actually from the biology brain side is simply deciding what information to
*  discard. That's my definition. So that includes like a whole lot of things, obviously. But it's
*  so broad as to be almost useless in this discussion. Whereas when we're talking about, I think,
*  attention and the sort of paying attention to something, right, it's the sort of controlled,
*  monolithic monotonic process. Yeah, so it was 2014. So we got this, so the theme about
*  the first author of the attention paper came up with this brilliant idea, we implemented it,
*  he ran all those experiments, we did some analysis, and then we were like blown away,
*  because it worked so well. So we started writing a paper. Can I stop you real quick, because
*  I was going to ask you this, I'm just going to ask you, because people toil, you toiled over
*  language models for years, with very, I mean, with plenty of progress, right. But then to come along
*  like a breakthrough like this, where the way you tell it, when you saw the idea,
*  you immediately saw that it would work, and it would just be a matter of implementing it.
*  And so that's kind of like a breakthrough. But is that a lesson to just keep pushing forward and
*  serendipity will happen because those moments do happen? What's the lesson there?
*  So I think the lesson is that, of course, you have to getting a good student always helps like
*  having Dima as an intern at the US just like it was just the best move ever. But one of the things
*  is that it was in some sense bound to happen because we knew what was missing like mathematically.
*  So that was the time when we all knew why LSTMs or GRUs were really important, why the
*  residual connections were really important because of the vanishing and exploding ground and issues.
*  And then we knew that as the size of the input changes, the network capacity needs to adapt to
*  it. We knew all those things. We just didn't know how to address it in the most concise or
*  the most succinct way possible. So in a sense, the concept, this particular concept of tension
*  in some sense was like right around the corner, but we just needed one or two extremely bright
*  people to notice that and then just take us around the corner. And of course, the Dima's
*  initial explanation did not have a word of tension. I didn't think of a tension either.
*  We kind of wrote a very quick draft and then after running all those experiments and then Yashua
*  looked at the draft and of course, Yashua was extremely excited about this whole idea. He made
*  all those edits and then only edits that I could see, the major edits I could see was that he
*  essentially put the word of tension at every set paragraph. And then I kind of let's say reverted
*  back every single one of them, except for I think the one where there was some kind of referral to
*  some examples there. But yeah, I totally agree with Brett in a sense that it's not really the
*  tension that we think of in the cognitive science or the neuroscience in a sense that the attention
*  often is there for the kind of sparse processing of a very high bandwidth input, if you think about
*  it, or the more widely thought of attention. On the other hand, this attention is extremely dense.
*  It has to look at every single possible input and then determine which is important. However,
*  after a few years, now everyone is anyway calling the tension. So I started calling the tension.
*  It's very catchy to start with. But what I'm realizing is that it's just what computer
*  scientists have been doing all along is that it's just a separation of the concept or the idea and
*  the implementation. So conceptually, it is a tension in a sense that you're trying to decide what is
*  important, we use it. But for implementing it, we've been using all those extremely dense parallel
*  computation because we know that kind of implementation enables us to use this set of,
*  let's say, agorathum such as backpropagations as they are without having to make substantial changes.
*  So that's why we didn't call it tension, although I almost feel like we should have now that I think
*  about it. But I didn't know. Do you guys want to weigh in on this?
*  Yeah, I mean, I think, you know, it's, you know, in some sense, we could sparsify it.
*  I mean, there's work on sparsification of the way that the attention mechanism works,
*  mostly for efficiency, right? I agree that, you know, completely that what we're doing is
*  you know, some high level inspiration with, you know, an implementation that is for,
*  you know, the hardware that we have, right? In some sense, you know, that the fact that we're
*  doing things differently than the brain is supernatural because our hardware that we have
*  is completely hardware or wetware is just very, very different. And, you know, I think,
*  indeed, that one can say that the inspiration behind attention in a transformer is in fact,
*  sort of in like, kind of similar to actually focusing on certain parts of, you know, the
*  input sequence, right? The thing that I would agree with on Brad's component is that, you know,
*  in large part, the way that we use transformers, the mechanism, the actual mechanism for paying
*  attention is fixed once you have training data. So any new input, you know, what we have is that,
*  you know, that input is fixed. And so there's no computation or change that happens,
*  you know, beyond that. Yeah, I would say, I mean, my wife is a neuroscientist, and she completely
*  disagrees that it's anything like attention, real attention. But, you know, I definitely think that
*  the inspiration is certainly, you know, similar in terms of what we're trying to do with the model.
*  So when I think about, yeah, when I think about human attention versus machine attention, one
*  difference, I think is that for human attention, it's more explainable. Like I can tell,
*  I'm paying attention to this part, because I think it's important for my task, we're raising the
*  process, whereas for, okay, maybe there's disagreement, I guess, other people can be.
*  But for machine attention, I guess, it's more about, okay, I mentioned, maybe making make
*  the optimization better, or it enables interaction between different parts of the input. So I think
*  from the explainability perspective, there's this difference between human attention versus
*  machine attention. Yeah, I'll emphasize that there's sort of two different ways that attention
*  can be used in the psychology side, right. And I think you're absolutely right on the explainability
*  side, when we think about the one form of controlled attention, right. But sort of my broader
*  definition of just throwing information out is actually much more similar to the Transformers
*  version. You know, and I think in that in that sense, Joshua was right on the money to call it
*  attention in that sense. There's two different definitions. Most people refer to the controlled
*  version on the biology on the psychology side. Guys, we're almost out of time here. So I would
*  love to go around and ask you a terrible question here. What I want to know is something that you're
*  working on right now, that you're really struggling with, that seems just out of your reach, that's
*  frustrating you that you can't quite grasp. Joe, you want to you want to, besides your wife being
*  a neuroscientist, do you have something else? Um, some good question. I think that a large
*  component of what's sort of bothering me, it has continued to be like, how to, you know, take the
*  modern neural systems and make them effective in like a real life setting, right? We have all these
*  beautiful generative models. And, you know, because of their toxicity and their controllability,
*  you know, no one in an IRB setting would allow me to use, you know, an internal review board where
*  they're going to tell me whether, you know, I can do the, I can have patients talk to a generative
*  model would allow me to actually do this, right? I can't get permission for any health, any of the
*  healthcare stuff to use these beautiful generative models. And, but the thing that I'm struggling
*  with at the moment is how to reconcile the fact that we have all these very, very powerful models
*  and yet in terms of practical use and application, they're really, really hard because
*  we have all these safety toxicity, you know, explainability problems that stop them from being
*  able, you know, to actually go that last, you know, half mile. Okay, very good. Who wants to go next?
*  I'm going to let you guys jump in. Who feels the most frustrated?
*  Wait, did you think that Joel felt most frustrated? Is that the reason why you asked him first?
*  I have to roll a die to choose. I just, I was feeling his wife neuroscientist pain, you know.
*  I can go next. So one thing I'm working on is how to make this language understanding models
*  generalize to all of distribution data. So we know that if you train the model on specific
*  data sets, the model is going to work well on data that looks similar to your training data,
*  but it's hard to make this model generalize to new data that's still from the same task.
*  So I think one challenge here is that it's unrealistic to expect that this model can
*  generalize to arbitrary distribution. So you have to give the model some knowledge about what your
*  test data is going to look like if it is not from your training data sets or training data distribution.
*  And I find it's very challenging to find a balance between how much prior knowledge you want to make
*  baking versus how generalizable this message really is. So I feel I have some ideas, but I don't have
*  very good satisfactory solutions to this problem. We'll go, how about one more NLP and then we'll
*  finish with the neuroscience. So I'm at the research is always trouble anyway. So one thing
*  that I'm struggling at the moment, besides science is how to convince my graduating PhD students or
*  the I'll call it postdocs to consider a career that is outside thing, let's put it like that,
*  or the outside Google brain, you have to Google, do my Facebook research and Microsoft research,
*  because I don't know, I feel like too many people, too many brightest minds are just
*  going there. I mean, I think the compensation is great and so on, but I do feel like all these NLP
*  algorithms, machine learning algorithms can be used for so many interesting problems and important
*  problems. But I feel like too many people are just being sucked into this one of these five,
*  let's say tech firms and the marginal impact on the society coming out of this individual PhDs is
*  just converging towards zero. So I'm actually struggling to convince them to see beyond
*  these tech firms, but it's an uphill battle just because of the tech rally that is never ending.
*  The compensation looks just so much larger than before.
*  This is kind of related. So when you started your postdoc with Yahshua,
*  he gave you four options for what to study. And the third one was machine translation. And I don't
*  remember if you struggled to accept that. I don't remember whether that lit you up or whether you
*  really thought about it a lot or whatever. But that was back then. And now it's all, everything's NLP.
*  That was back then when NLP wasn't working. Right.
*  NLP wasn't, yes.
*  Yeah, right. Okay. Machine translation wasn't. But so I thought what you were going to say is
*  that you struggle to convince your students to do something besides NLP or besides language-based
*  approaches because that's the... That's true as well. Yeah, it is a bit implied. I mean,
*  in a sense that the NLP is popular because all these tech firms are insurance service firms.
*  And then the NLP is kind of very obvious and immediate area they want to invest in anyway.
*  And then you have the... And probably because of that, my students are being recruited by
*  these companies with a high level of compensation, which is great. But I want my students who are
*  really, really bright to do something beyond what I've done or what people in our generation or the
*  previous generations have done. But it's an uphill battle. I haven't convinced anyone of any of them,
*  except for one student who joined Tesla. That was the furthest away from the tech firms. And then
*  it's not that too far. No. Yeah. All right. So that's a very career-oriented struggle,
*  which is fine. Brad, you want to round it out? Yeah, sure. I've got a struggle that's been
*  ongoing for a while now. Over time, I've come to view attention, and I mean the sort of controlled
*  process version, as being something rather than helping us perceive in the moment by just dealing
*  with information overload, it is actually something that helps us to structure the sort of data set
*  that we're building about the world. So it's there to help us learn better for the long term,
*  rather than help us function better in the moment. The problem is that I have no way to test these
*  theories, right? Because I can't alter the way that detention works in infants and then see what goes
*  wrong, obviously. So I'm basically stuck where I've got this theory, but I can't figure out a good
*  way to test it, apart from building simulated agents, but there's still a thousand other
*  problems there. So that's my problem. So I lied. I have one more quick question,
*  Brad, I'll start with you real quick. So I've heard Cunha say that we're at the very beginning
*  of natural language understanding, natural language processing machine, all the language-based stuff.
*  We're at the very beginning. It doesn't feel like that. Where are we in vision and the associated
*  cognitive processes? Are we at the beginning? It doesn't feel like it.
*  It doesn't feel like it. But I think that when we finally get there, wherever there is,
*  we're going to look back and realize that this was still the beginning.
*  Yeah, that's sad, isn't it?
*  Yeah, there's just so much we don't yet get about how vision works. I mean, categories from images
*  is such a slim sliver of what the human visual system accomplishes when we look at something
*  in just like 200 milliseconds, we just instantly apprehend all of this context and information.
*  And I think we're still a long way from doing that. So I guess we're at the maybe like a
*  five-year-old level of understanding. All right. What year level are we in language, guys?
*  And are we at the beginning? We're at the beginning, for sure. Yes. I mean,
*  Ho and Joao were able to actually tell us all the things that don't work. And then as Joao
*  pointed out, we can't even get the institutional review board who often say yes, as long as we
*  write the proposals correctly, to say yes to just having it talk to the patients or the subject in
*  a very controlled manner. So we're very, very far away from saying that, yeah, here's the actual
*  language understanding or generating models. And then Ho, I think you gave an example of
*  learning three words was difficult, I guess. Yeah, sometimes single words, changing things.
*  Yeah, changing the blocks forward. I guess that's what people worked on at the beginning of the AI
*  and we're still struggling as a now. Agree, Joao?
*  Yeah, no, I completely agree. We're at the beginning. I think that there's so many open
*  questions and I don't think that a trillion parameters is going to solve it. I think that
*  the real thing, we have new breakthroughs that we really do need to make in terms of
*  trying to be able to actually interface with people in a manner that is productive.
*  All right, well, this is great. You guys are at the beginning. We collectively are at the end,
*  actually. See what I did there with the actually? So, oh, by the way, it was Tony Mofshan who used
*  the cottage industry vernacular for the small labs. Just to wrap things up. So thanks guys for
*  the wonderful conversation. I really appreciate it and I hope that students get a ton out of it.
*  Thank you. Thank you, Paul. Thanks for hosting.
*  The full versions of all the episodes plus bonus episodes that focus more on the cultural side but
*  still have science. Go to brandinspired.co and find the red Patreon button there. To get in touch with
*  me, email paul at brandinspired.co. The music you hear is by The New Year. Find them at the newyear.net.
*  Thank you for your support. See you next time.

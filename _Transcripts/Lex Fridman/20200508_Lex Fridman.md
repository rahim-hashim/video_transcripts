---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 5848s
Video Keywords: ['ilya sutskever', 'deep learning', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 694046
Video Rating: None
Video Description: Ilya Sutskever is the co-founder of OpenAI, is one of the most cited computer scientist in history with over 165,000 citations, and to me, is one of the most brilliant and insightful minds ever in the field of deep learning. There are very few people in this world who I would rather talk to and brainstorm with about deep learning, intelligence, and life than Ilya, on and off the mic.

Support this podcast by signing up with these sponsors:
- Cash App - use code "LexPodcast" and download:
- Cash App (App Store): https://apple.co/2sPrUHe
- Cash App (Google Play): https://bit.ly/2MlvP5w

EPISODE LINKS:
Ilya's Twitter: https://twitter.com/ilyasut
Ilya's Website: https://www.cs.toronto.edu/~ilya/

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
2:23 - AlexNet paper and the ImageNet moment
8:33 - Cost functions
13:39 - Recurrent neural networks
16:19 - Key ideas that led to success of deep learning
19:57 - What's harder to solve: language or vision?
29:35 - We're massively underestimating deep learning
36:04 - Deep double descent
41:20 - Backpropagation
42:42 - Can neural networks be made to reason?
50:35 - Long-term memory
56:37 - Language models
1:00:35 - GPT-2
1:07:14 - Active learning
1:08:52 - Staged release of AI systems
1:13:41 - How to build AGI?
1:25:00 - Question to AGI
1:32:07 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Ilya Sutskever Deep Learning  Lex Fridman Podcast #94
**Lex Fridman:** [May 08, 2020](https://www.youtube.com/watch?v=13CZPWmke6A)
*  The following is a conversation with Ilya Tsetskever, co-founder and chief scientist of OpenAI,
*  one of the most cited computer scientists in history with over 165,000 citations,
*  and to me, one of the most brilliant and insightful minds ever in the field of deep learning.
*  There are very few people in this world who I would rather talk to and brainstorm with about
*  deep learning, intelligence, and life in general than Ilya, on and off the mic.
*  This was an honor and a pleasure.
*  This conversation was recorded before the outbreak of the pandemic. For everyone feeling the medical,
*  psychological, and financial burden of this crisis, I'm sending love your way. Stay strong.
*  We're in this together. We'll beat this thing.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  review it with five stars on Apple Podcasts, support it on Patreon, or simply connect with me
*  on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. As usual, I'll do a few minutes of ads now and
*  never any ads in the middle that can break the flow of the conversation. I hope that works for
*  you and doesn't hurt the listening experience. This show is presented by Cash App, the number
*  one finance app in the App Store. When you get it, use code LexPodcast. Cash App lets you send
*  money to friends, buy Bitcoin, invest in the stock market with as little as $1. Since Cash App
*  allows you to buy Bitcoin, let me mention that cryptocurrency in the context of the history of
*  money is fascinating. I recommend Ascent of Money as a great book on this history. Both the book
*  and audiobook are great. Debits and credits on ledgers started around 30,000 years ago. The US
*  dollar created over 200 years ago, and Bitcoin, the first decentralized cryptocurrency, released
*  just over 10 years ago. Given that history, cryptocurrency is still very much in its early
*  days of development, but it's still aiming to, and just might, redefine the nature of money.
*  Again, if you get Cash App from the App Store or Google Play and use the code LexPodcast,
*  you get $10, and Cash App will also donate $10 to First, an organization that is helping
*  advance robotics and STEM education for young people around the world. And now, here's my
*  conversation with Ilya Tsetskevich. You were one of the three authors with Alex Kuchefsky,
*  Jeff Hinton of the famed Alex Ned paper that is arguably the paper that marked the big
*  catalytic moment that launched the deep learning revolution. At that time, take us back to that
*  time. What was your intuition about neural networks, about the representational power
*  of neural networks? And maybe you could mention how did that evolve over the next few years,
*  up to today, over the 10 years? Yeah, I can answer that question. At some point in about 2010 or
*  2011, I connected two facts in my mind. Basically, the realization was this. At some point, we realize
*  that we can train very large, I shouldn't say very, you know, tiny by today's standards, but
*  large and deep neural networks end to end with back propagation. At some point,
*  different people obtain this result. I obtained this result. The first moment in which I realized
*  that deep neural networks are powerful was when James Martens invented the Hessian free optimizer
*  in 2010. And he trained a 10 layer neural network end to end without pre-training
*  from scratch. And when that happened, I thought this is it. Because if you can train a big neural
*  network, a big neural network can represent very complicated function. Because if you have a neural
*  network with 10 layers, it's as though you allow the human brain to run for some number of
*  milliseconds. Neuron firings are slow. And so in maybe 100 milliseconds, your neurons only fire
*  10 times. So it's also kind of like 10 layers. And in 100 milliseconds, you can perfectly recognize
*  any object. So I already had the idea then that we need to train a very big neural network
*  on lots of supervised data. And then it must succeed because we can find the best neural
*  network. And then there's also theory that if you have more data than parameters, you won't overfit.
*  Today we know that actually this theory is very incomplete and you won't overfit even if you have
*  less data than parameters. But definitely if you have more data than parameters, you won't overfit.
*  So the fact that neural networks were heavily overparameterized wasn't discouraging to you?
*  So you were thinking about the theory that the number of parameters, the fact there's a huge
*  number of parameters is okay? Is it going to be okay? I mean, there was some evidence before that
*  it was okay-ish. But the theory was most, the theory was that if you had a big data set and
*  a big neural net, it was going to work. The overparameterization just didn't really figure
*  much as a problem. I thought, well, with images, you're just going to add some data augmentation
*  and it's going to be okay. So where was any doubt coming from? The main doubt was can we train a
*  bigger, will we have enough compute to train a big enough neural net? With backpropagation.
*  Backpropagation I thought would work. The thing which wasn't clear was whether there would be
*  enough compute to get a very convincing result. And then at some point Alex Kirzhevsky wrote these
*  insanely fast CUDA kernels for training convolutional neural nets. And that was, bam, let's do this.
*  Let's get imaging that and it's going to be the greatest thing.
*  Your intuition from empirical results by you and by others. So like just actually demonstrating
*  that a piece of program can train a 10 layer neural network or was there some pen and paper
*  or marker and whiteboard thinking intuition? Because you just connected a 10 layer large
*  neural network to the brain. So you just mentioned the brain. So in your intuition
*  about neural networks, does the human brain come into play as an intuition builder?
*  Definitely. I mean, you know, you got to be precise with these analogies between neural
*  artificial neural networks in the brain. But there's no question that the brain is a huge
*  source of intuition and inspiration for deep learning researchers since all the way from
*  Rosenblatt in the 60s. Like if you look at the whole idea of a neural network is directly
*  inspired by the brain. You had people like McCallum and Pitts who were saying, hey, you got these
*  neurons in the brain. And hey, we recently learned about the computer and automata. Can we use some
*  ideas from the computer and automata to design some kind of computational object that's going to be
*  simple, computational and kind of like the brain? And they invented the neuron.
*  So they were inspired by it back then. Then you had the convolutional neural network from Fukushima
*  and then later Yan LeCun who said, hey, if you limit the receptive fields of a neural network,
*  it's going to be especially suitable for images as it turned out to be true. So there was a very
*  small number of examples where analogies to the brain were successful. And I thought, well,
*  probably an artificial neuron is not that different from the brain if it's going hard enough. So let's
*  just assume it is and roll with it. So we're now at a time where deep learning is very successful.
*  So let us squint less and say, let's open our eyes and say, what to you is an interesting
*  difference between the human brain? Now, I know you're probably not an expert,
*  neither neuroscientist and neurobiologist, but loosely speaking, what's the difference
*  between the human brain and artificial neural networks? That's interesting to you for the
*  next decade or two. That's a good question to ask. What is an interesting difference between
*  the brain and our artificial neural networks? So I feel like today, artificial neural networks,
*  so we all agree that there are certain dimensions in which the human brain vastly outperforms our
*  models. But I also think that there are some ways in which artificial neural networks have
*  a number of very important advantages over the brain. Looking at the advantages versus
*  disadvantages is a good way to figure out what is the important difference. So the brain uses
*  spikes, which may or may not be important. Yes, that's a really interesting question. Do
*  you think it's important or not? That's one big architectural difference between artificial
*  neural networks. It's hard to tell, but my prior is not very high. And I can say why.
*  There are people who are interested in spike in neural networks. And basically, what they figured
*  out is that they need to simulate the non-spike in neural networks in spikes. And that's how they're
*  going to make them work. If you don't simulate the non-spike in neural networks in spikes,
*  it's not going to work because the question is why should it work? And that connects to questions
*  around backpropagation and questions around deep learning. You've got this giant neural network.
*  Why should it work at all? Why should the learning rule work at all?
*  It's not a self-evident question, especially if you were just starting in the field and you
*  read the very early papers. You can say, hey, people are saying, let's build neural networks.
*  That's a great idea because the brain is a neural network, so it would be useful to build neural
*  networks. Now, let's figure out how to train them. It should be possible to train them probably,
*  but how? And so the big idea is the cost function. That's the big idea. The cost function
*  is a way of measuring the performance of the system according to some measure.
*  By the way, that is a big... Actually, let me think. Is that one a difficult idea to arrive at? And how
*  big of an idea is that? That there's a single cost function. Sorry, let me take a pause. Is supervised
*  learning a difficult concept to come to? I don't know. All concepts are very easy in retrospect.
*  Yeah, that's what it seems trivial now. Because the reason I asked that, and we'll talk about it,
*  is there other things? Is there things that don't necessarily have a cost function, maybe have many
*  cost functions, or maybe have dynamic cost functions, or maybe a totally different kind
*  of architectures? Because we have to think like that in order to arrive at something new, right?
*  So the good examples of things which don't have clear cost functions are GANs.
*  And again, you have a game. So instead of thinking of a cost function where you know that you have
*  an algorithm gradient descent, which will optimize the cost function, and then you can reason about
*  the behavior of your system in terms of what it optimizes. With a GAN, you say, I have a game,
*  and I'll reason about the behavior of the system in terms of the equilibrium of the game.
*  But it's all about coming up with these mathematical objects that help us reason about
*  the behavior of our system. Right. That's really interesting. Yeah. So GAN is the only one. It's
*  kind of a... The cost function is emergent from the comparison. I don't know if it has a cost
*  function. I don't know if it's meaningful to talk about the cost function of a GAN. It's kind of
*  like the cost function of biological evolution or the cost function of the economy. You can talk
*  about regions to which it will go towards, but I don't think the cost function analogy is the
*  most useful. So if evolution doesn't... That's really interesting. So if evolution doesn't really
*  have a cost function, like a cost function based on its... Something akin to our mathematical
*  conception of a cost function, then do you think cost functions in deep learning are holding us
*  back? Yeah. So you just kind of mentioned that cost function is a nice first profound idea.
*  Do you think that's a good idea? Do you think it's an idea we'll go past? So self-play starts to
*  touch on that a little bit in reinforcement learning systems. That's right. Self-play and
*  also ideas around exploration where you're trying to take action that surprise a predictor.
*  I'm a big fan of cost functions. I think cost functions are great and they serve us really
*  well. And I think that whenever we can do things with cost functions, we should.
*  And maybe there is a chance that we will come up with yet another profound way of looking at
*  things that will involve cost functions in a less central way. But I don't know. I think cost functions
*  are... I mean, I would not bet against cost functions. Is there other things about the brain
*  that pop into your mind that might be different and interesting for us to consider in designing
*  artificial neural networks? So we talked about spiking a little bit. I mean, one thing which
*  may potentially be useful, I think people, neuroscientists, have figured out something
*  about the learning rule of the brain or talking about spike time independent plasticity. And it
*  would be nice if some people were to study that in simulation. Wait, sorry, spike time independent
*  plasticity? What's that? STD. It's a particular learning rule that uses spike timing to figure
*  out how to determine how to update the synapses. So it's kind of like if the synapse fires into the
*  neuron before the neuron fires, then it's strengthened the synapse. And if the synapse fires
*  into the neurons shortly after the neuron fired, then it weakens the synapse. Something along this
*  line. I'm 90% sure it's right. So if I said something wrong here, don't get too angry.
*  But you sounded brilliant while saying it. But the timing, that's one thing that's missing.
*  The temporal dynamics is not captured. I think that's like a fundamental property of the brain
*  is the timing of the signals. Well, you have recurrent neural networks.
*  But you think of that as this, I mean, that's a very crude simplified, what's that called?
*  It's called, there's a clock, I guess, to recurrent neural networks. It seems like the brain
*  is the continuous version of that, the generalization where all possible timings
*  are possible. And then within those timings is contained some information. You think recurrent
*  neural networks, the recurrence in recurrent neural networks can capture the same kind of phenomena
*  as the timing that seems to be important for the brain in the firing of neurons in the brain.
*  I think recurrent neural networks are amazing and they can do anything we'd want a system to do.
*  Right now recurrent neural networks have been superseded by transformers, but maybe
*  one day they'll make a comeback. Maybe they'll be back. We'll see.
*  Let me, in a small tangent, say, do you think they'll be back? So much of the breakthroughs
*  recently that we'll talk about on natural language processing and language modeling has been with
*  transformers that don't emphasize recurrence. Do you think recurrence will make a comeback?
*  Well, some kind of recurrence, I think, very likely. Recurrent neural networks, as they're
*  typically thought of for processing sequences, I think it's also possible.
*  What is to you a recurrent neural network? And generally speaking, I guess, what is a
*  recurrent neural network? You have a neural network which maintains a high-dimensional
*  hidden state. And then when an observation arrives, it updates its high-dimensional hidden state
*  through its connections in some way. So do you think, you know, that's what expert systems did?
*  Symbolic AI, the knowledge-based, growing a knowledge base is maintaining a hidden state,
*  which is its knowledge base, and is growing it by sequential processing. Do you think of it more
*  generally in that way? Or is it simply, is it the more constrained form of a hidden state with
*  certain kind of gating units that we think of as today with LSDMs and that?
*  I mean, the hidden state is technically what you described there, the hidden state that goes inside
*  the LSDM or the RNN or something like this. But then what should be contained, you know,
*  if you want to make the expert system analogy, I'm not, I mean, you could say that the knowledge
*  is stored in the connections, and then the short-term processing is done in the hidden state.
*  Yes. Could you say that? So sort of, do you think there's a future of building large-scale
*  knowledge bases within the neural networks? Definitely.
*  So we're going to pause on that confidence because I want to explore that. Well, let me zoom back out
*  and ask back to the history of ImageNet. Neural networks have been around for many decades,
*  as you mentioned. What do you think were the key ideas that led to their success,
*  that ImageNet moment and beyond the success in the past 10 years?
*  Okay. So the question is to make sure I didn't miss anything, the key ideas that led to the
*  success of deep learning over the past 10 years. Exactly. Even though the fundamental
*  thing behind deep learning has been around for much longer.
*  So the key idea about deep learning, or rather the key fact about deep learning before
*  deep learning started to be successful is that it was underestimated.
*  People who worked in machine learning simply didn't think that neural networks could do much.
*  People didn't believe that large neural networks could be trained.
*  People thought that, well, there was a lot of debate going on in machine learning about
*  what are the right methods and so on. And people were arguing because there was no way to get hard
*  facts. And by that I mean there were no benchmarks which were truly hard, that if you do really well
*  on them, then you can say, look, here is my system. That's when you switch from,
*  that's when this field becomes a little bit more of an engineering field. So in terms of deep learning
*  to answer the question directly, the ideas were all there. The thing that was missing was a lot
*  of supervised data and a lot of compute. Once you have a lot of supervised data and a lot of compute,
*  there is a third thing which is needed as well, and that is conviction. Conviction that if you take
*  the right stuff which already exists and apply and mix a lot of data and a lot of compute,
*  that it will in fact work. And so that was the missing piece. It was you had the data,
*  you needed the compute which showed up in terms of GPUs, and you needed the conviction to realize
*  that you need to mix them together. So that's really interesting. So I guess the
*  presence of compute and the presence of supervised data allowed the empirical evidence to do the
*  convincing of the majority of the computer science community. So I guess there's a key moment with
*  Jitendra Malik and Alex Alyosha Efros who were very skeptical, right? And then there's a Jeffrey
*  Hinton that was the opposite of skeptical, and there was a convincing moment. And I think
*  Emission had served as that moment. And they represented this kind of, were the big pillars
*  of computer vision community, kind of the wizards got together and then all of a sudden there was
*  a shift. And it's not enough for the ideas to all be there and the compute to be there, it's
*  for it to convince the cynicism that existed. That's interesting that people just didn't believe
*  for a couple of decades. Yeah, well, but it's more than that. It's kind of, when put this way,
*  it sounds like, well, you know, those silly people who didn't believe what were they missing. But in
*  reality, things were confusing because neural networks really did not work on anything. And
*  they were not the best method on pretty much anything as well. And it was pretty rational
*  to say, yeah, this stuff doesn't have any traction. And that's why you need to have these very hard
*  tasks which are which produce undeniable evidence. And that's how we make progress.
*  And that's why the field is making progress today, because we have these hard benchmarks,
*  which represent true progress. And so and this is why we are able to avoid endless debate.
*  So incredibly, you've contributed some of the biggest recent ideas in AI in computer vision,
*  language, natural language processing, reinforcement learning, sort of everything in between,
*  maybe not GANs. There may not be a topic you haven't touched. And of course, the fundamental
*  science of deep learning. What is the difference to you between vision, language, and as in
*  reinforcement learning action, as learning problems? And what are the commonalities? Do you see them as
*  all interconnected? Are they fundamentally different domains that require different approaches?
*  Okay, that's a good question. Machine learning is a field with a lot of unity, a huge amount of unity.
*  What do you mean by unity? Like overlap of ideas?
*  Overlap of ideas, overlap of principles. In fact, there is only one or two or three principles,
*  which are very, very simple. And then they apply in almost the same way, in almost the same way
*  to the different modalities to the different problems. And that's why today, when someone
*  writes a paper on improving optimization of deep learning in vision, it improves the different NLP
*  applications and it improves the different reinforcement learning applications.
*  So I would say that computer vision and NLP are very similar to each other. Today, they differ
*  in that they have slightly different architectures. We use transformers in NLP and we use convolutional
*  neural networks in vision. But it's also possible that one day this will change and everything will
*  be unified with a single architecture. Because if you go back a few years ago in natural language
*  processing, there were a huge number of architectures for every different tiny problem had its own
*  architecture. Today, there's just one transformer for all those different tasks. And if you go back
*  in time even more, you had even more and more fragmentation and every little problem in AI had
*  its own little subspecialization and sub, you know, little set of collection of skills, people who
*  would know how to engineer the features. Now it's all been subsumed by deep learning. We have this
*  unification. And so I expect vision to become unified with natural language as well. Or rather,
*  I shouldn't say expect. I think it's possible. I don't want to be too sure because I think
*  the convolutional neural network is very computationally efficient. RL is different. RL does require
*  slightly different techniques because you really do need to take action. You really need to do
*  something about exploration. Your variance is much higher. But I think there is a lot of unity even
*  there. And I would expect, for example, that at some point, there will be some
*  broader unification between RL and supervised learning where somehow the RL will be making
*  decisions to make the supervised learning go better. And it will be, I imagine, one big black box and
*  you just throw, you know, you shovel things into it and it just figures out what to do with whatever
*  you shovel in it. I mean, reinforcement learning has some aspects of language and vision combined,
*  almost. There's elements of a long-term memory that you should be utilizing and there's elements
*  of a really rich sensory space. So it seems like it's like the union of the two or something like
*  that. I'd say something slightly differently. I'd say that reinforcement learning is neither,
*  but it naturally interfaces and integrates with the two of them.
*  Do you think action is fundamentally different? So yeah, what is interesting about,
*  what is unique about policy of learning to act? Well, so one example, for instance, is that
*  when you learn to act, you are fundamentally in a non-stationary world because as your actions change,
*  the things you see start changing. You experience the world in a different way. And this is not the
*  case for the more traditional static problem where you have some distribution and you just apply a
*  model to that distribution. You think it's a fundamentally different problem or is it just
*  more difficult? It's a generalization of the problem of understanding. I mean, it's a question
*  of definitions almost. There is a huge amount of commonality for sure. You take gradients, you try
*  to approximate gradients in both cases. In the case of reinforcement learning, you have some
*  tools to reduce the variance of the gradients. You do that. There's lots of commonality. You use the
*  same neural net in both cases. You compute the gradient, you apply atom in both cases.
*  So, I mean, there's lots in common for sure, but there are some small differences which are not
*  completely insignificant. It's really just a matter of your point of view, what frame of reference,
*  how much do you want to zoom in or out as you look at these problems. Which problem do you think
*  is harder? So people like Noam Chomsky believe that language is fundamental to everything.
*  So it underlies everything. Do you think language understanding is harder than visual scene
*  understanding or vice versa? I think that asking if a problem is hard is slightly wrong.
*  I think the question is a little bit wrong and I want to explain why. So what does it mean for a
*  problem to be hard? Okay, the non-interesting dumb answer to that is there's a benchmark
*  and there's a human level performance on that benchmark and how is the effort required to
*  reach the human level benchmark. So from the perspective of how much until we get to human
*  level on a very good benchmark. Yeah, I understand what you mean by that. So what I was going to say
*  that a lot of it depends on, you know, once you solve a problem, it stops being hard. And that's
*  always true. But something is hard or not depends on what our tools can do today. So, you know,
*  today through human level, language understanding and visual perception are hard in the sense that
*  there is no way of solving the problem completely in the next three months. So I agree with that
*  statement. Beyond that, I'm just, I'd be my guess would be as good as yours. I don't know.
*  Okay. So you don't have a fundamental intuition about how hard language understanding is.
*  I think I know I changed my mind. I'd say language is probably going to be harder. I mean,
*  it depends on how you define it. Like if you mean absolute top notch 100% language understanding,
*  I'll go with language. So but then if I show you a piece of paper with letters on it, is that
*  you see what I mean? It's like you have a vision system, you say it's the best human level vision
*  system. I show you I open a book, and I show you letters. Will it understand how these letters
*  form into word and sentences and meaning? Is this part of the vision problem? Where does vision and
*  language begin? Yeah. So Chomsky would say it starts at language. So vision is just a little
*  example of the kind of structure and fundamental hierarchy of ideas that's already represented in
*  our brain somehow that's represented through language. But where does vision stop and language
*  begin? That's a really interesting question. So one possibility is that it's impossible to achieve
*  really deep understanding in either images or language without basically using the same kind
*  of system. So you're going to get the other for free. I think it's pretty likely that yes,
*  if we can get one, our machine learning is probably that good that we can get the other.
*  But I'm not 100% sure. And also, I think a lot of it really does depend on your definitions.
*  Definitions of? Of like perfect vision. Because reading is vision, but should it count?
*  Yeah. To me, my definition is if a system looked at an image and then a system looked at a piece
*  of text and then told me something about that and I was really impressed. That's relative.
*  You'll be impressed for half an hour and then you're going to say, well, I mean, all the systems do
*  that, but here's the thing they don't do. Yeah, but I don't have that with humans. Humans continue
*  to impress me. Is that true? Well, the ones, okay. So I'm a fan of monogamy. So I like the idea of
*  marrying somebody, being with them for several decades. So I believe in the fact that yes,
*  it's possible to have somebody continuously giving you pleasurable, interesting, witty,
*  new ideas, friends. Yeah, I think so. They continue to surprise you. The surprise,
*  that injection of randomness seems to be a nice source of continued inspiration, like the wit,
*  the humor. I think, yeah, it's a very subjective test, but I think if you have enough humans
*  in the room. Yeah, I understand what you mean. Yeah, I feel like I misunderstood what you meant
*  by impressing you. I thought you meant to impress you with its intelligence, with how
*  well it understands an image. I thought you meant something like I'm going to show it a
*  really complicated image and it's going to get it right and you're going to say, wow,
*  that's really cool. Systems of January 2020 have not been doing that. Yeah. No, I think it
*  all boils down to the reason people click like on stuff on the internet, which is it makes them laugh.
*  So it's like humor or wit or insight. I'm sure we'll get that as well. So forgive the romanticized
*  question, but looking back to you, what is the most beautiful or surprising idea in deep learning
*  or AI in general you've come across? So I think the most beautiful thing about deep learning is
*  that it actually works. And I mean it because you got these ideas, you got the little neural
*  network, you got the back propagation algorithm. And then you got some theories as to, you know,
*  this is kind of like the brain. So maybe if you make it large, if you make the neural network
*  large and you're trained in a lot of data, then it will do the same function that the brain does.
*  And it turns out to be true. That's crazy. And now we just train these neural networks and you make
*  them larger and they keep getting better. And I find it unbelievable. I find it unbelievable that
*  this whole AI stuff with neural networks works. Have you built up an intuition of why? Are there
*  a little bits and pieces of intuitions of insights of why this whole thing works?
*  I mean, some definitely. Well, we know that optimization, we now have good, you know,
*  we've had lots of empirical, you know, huge amounts of empirical reasons to believe that
*  optimization should work on all most problems we care about. Do you have insights of what? So you
*  just said empirical evidence. Is most of your sort of empirical evidence kind of convinces you. It's
*  like evolution is empirical. It shows you that, look, this evolutionary process seems to be a good
*  way to design organisms that survive in their environment, but it doesn't really get you to the
*  insights of how the whole thing works. I think it's a good analogy is physics. You know how you say,
*  hey, let's do some physics calculation and come up with some new physics theory and make some
*  prediction. But then you got around the experiment. You know, you got around the experiment. It's
*  important. So it's a bit the same here, except that maybe some, sometimes the experiment came
*  before the theory, but it still is the case. You know, you have some data and you come up with
*  some prediction. You say, yeah, let's make a big neural network. Let's train it. And it's going to
*  work much better than anything before it. And it will in fact continue to get better as we make it
*  larger. And it turns out to be true. That's amazing when a theory is validated like this, you know,
*  it's not a mathematical theory. It's more of a biological theory almost. So I think there are
*  not terrible analogies between deep learning and biology. I would say it's like the geometric
*  mean of biology and physics. That's deep learning. The geometric mean of biology and physics. I think
*  I'm going to need a few hours to wrap my head around that. Cause just to find the geometric,
*  just to find the set of what biology represents. Well, biology, in biology, things are really
*  complicated. The theories are really, really, it's really hard to have good predictive theory. And
*  in physics, the theories are too good. In physics, people make these super precise theories,
*  which make these amazing predictions. And in machine learning, we're kind of in between.
*  Kind of in between. But it'd be nice if machine learning somehow helped us discover the unification
*  of the two as opposed to sort of the in between. But you're right. You're kind of trying to juggle
*  both. So do you think there are still beautiful and mysterious properties in neural networks
*  that are yet to be discovered? Definitely. I think that we are still massively underestimating
*  deep learning. What do you think it will look like? Like what if I knew I would have done it?
*  So, but if you look at all the progress from the past 10 years, I would say most of it,
*  I would say there've been a few cases where some were things that felt like really new ideas showed
*  up. But by and large, it was every year we thought, okay, deep learning goes this far. Nope, it actually
*  goes further. And then the next year, okay, now this is big deep learning, we are really done.
*  Nope, goes further. It just keeps going further each year. So that means that we keep underestimating,
*  we keep not understanding it as surprising properties all the time. Do you think it's
*  getting harder and harder to make progress? Need to make progress. It depends on what you mean.
*  I think the field will continue to make very robust progress for quite a while. I think for
*  individual researchers, especially people who are doing research, it can be harder because there is
*  a very large number of researchers right now. I think that if you have a lot of compute, then you
*  can make a lot of very interesting discoveries, but then you have to deal with the challenge of
*  managing a huge compute cluster to run your experiments. It's a little bit harder.
*  So I'm asking all these questions that nobody knows the answer to, but you're one of the
*  smartest people I know, so I'm going to keep asking. So let's imagine all the breakthroughs
*  that happen in the next 30 years in deep learning. Do you think most of those breakthroughs can be
*  done by one person with one computer? In the space of breakthroughs, do you think compute
*  and large efforts will be necessary? I mean, I can't be sure. When you say one computer,
*  you mean how large? You're clever. I mean, one GPU. I see. I think it's pretty unlikely.
*  I think it's pretty unlikely. I think that the stack of deep learning is starting to be quite deep.
*  If you look at it, you've got all the way from the ideas, the systems to build the data sets,
*  the distributed programming, the building the actual cluster, the GPU programming,
*  putting it all together. So now the stack is getting really deep and I think it can be quite
*  hard for a single person to become world-class in every single layer of the stack. What about
*  what Vladimir Vapnik really insists on is taking MNIST and trying to learn from very few examples,
*  so being able to learn more efficiently. Do you think there'll be breakthroughs in that space that
*  may not need the huge compute? I think there will be a large number of breakthroughs in general that
*  will not need a huge amount of compute. So maybe I should clarify that. I think that some breakthroughs
*  will require a lot of compute and I think building systems which actually do things will require a
*  huge amount of compute. That one is pretty obvious. If you want to do X and X requires a huge neural
*  net, you got to get a huge neural net. But I think there will be lots of room for
*  very important work being done by small groups and individuals. Can you maybe sort of on the topic of
*  the science of deep learning talk about one of the recent papers that you released, the deep double
*  descent, where bigger models and more data hurt? I think it's a really interesting paper. Can you
*  describe the main idea? Yeah, definitely. So what happened is that over the years, some small number
*  of researchers noticed that it is kind of weird that when you make the neural network larger,
*  it works better and it seems to go in contradiction with statistical ideas. And then some people made
*  an analysis showing that actually you got this double descent bump. And what we've done was to
*  show that double descent occurs for pretty much all practical deep learning systems.
*  That it'll be also, so can you step back? What's the X axis and the Y axis of a double descent plot?
*  Okay, great. So you can do things like you can take a neural network
*  and you can start increasing its size slowly while keeping your data set fixed.
*  So if you increase the size of the neural network slowly, and if you don't do early stopping, that's
*  a pretty important detail. Then when the neural network is really small, you make it larger,
*  you get a very rapid increase in performance. Then you continue to make it larger and at some
*  point performance will get worse. And it gets the worst exactly at the point at which it achieves
*  zero training error, precisely zero training loss. And then as you make it larger, it starts to get
*  better again. And it's kind of counterintuitive because you'd expect deep learning phenomena to be
*  monotonic. And it's hard to be sure what it means, but it also occurs in the case of linear
*  classifiers and the intuition basically boils down to the following. When you have a large data set
*  and a small model, then small, tiny random... So basically what is overfitting? Overfitting is when
*  your model is somehow very sensitive to the small random unimportant stuff in your data set.
*  In the training data set?
*  In the training data set, precisely. So if you have a small model and you have a big data set,
*  and there may be some random thing, some training cases are randomly in the data set and others may
*  not be there. But the small model is kind of insensitive to this randomness because
*  it's the same... There is pretty much no uncertainty about the model when the data set is large.
*  So, okay, so at the very basic level to me, it is the most surprising thing that
*  neural networks don't overfit every time very quickly before ever being able to learn anything.
*  There are a huge number of parameters.
*  So here is... So there is one way. Okay, so maybe... So let me try to give the explanation. Maybe that
*  will work. So you got a huge neural network. Let's suppose you got a... You have a huge neural
*  network, you have a huge number of parameters. And now let's pretend everything is linear,
*  which is not... Let's just pretend. Then there is this big subspace where your neural network
*  achieves zero error. And SGT is going to find approximately the point with the smallest norm
*  in that subspace. And that can also be proven to be insensitive to the small randomness in the data
*  when the dimensionality is high. But when the dimensionality of the data is equal to the
*  dimensionality of the model, then there is a one-to-one correspondence between all the data sets
*  and the models. So small changes in the data set actually lead to large changes in the model,
*  and that's why performance gets worse. So this is the best explanation, more or less.
*  So then it would be good for the model to have more parameters, to be bigger than the data.
*  That's right. But only if you don't early stop. If you introduce early stop in your regularization,
*  you can make the double descent bump almost completely disappear.
*  What is early stop?
*  Early stopping is when you train your model and you monitor your validation performance.
*  And then if at some point, validation performance starts to get worse, you say,
*  okay, let's stop training. If you're good, you're good enough.
*  So the magic happens after that moment, so you don't want to do the early stopping.
*  Well, if you don't do the early stopping, you get the very pronounced double descent.
*  Do you have any intuition why this happens?
*  Double descent? Oh, sorry, early stopping?
*  No, the double descent.
*  So yeah, so I try, let's see. The intuition is basically this, that when the data set
*  has as many degrees of freedom as the model, then there is a one-to-one correspondence between them.
*  And so small changes to the data set lead to noticeable changes in the model. So your model
*  is very sensitive to all the randomness. It is unable to discard it. Whereas it turns out that
*  when you have a lot more data than parameters or a lot more parameters than data, the resulting
*  solution will be insensitive to small changes in the data set.
*  It's able to, that's nicely put, discard the small changes, the randomness.
*  Exactly. The spurious correlation which you don't want.
*  Jeff Hinton suggested we need to throw back propagation. We already kind of talked about
*  this a little bit, but he suggested we need to throw away back propagation and start over.
*  I mean, of course, some of that is a little bit
*  wit and humor, but what do you think? What could be an alternative method of training neural networks?
*  Well, the thing that he said precisely is that to the extent that you can't find back propagation
*  in the brain, it's worth seeing if we can learn something from how the brain learns. But back
*  propagation is very useful and we should keep using it. Oh, you're saying that once we discover
*  the mechanism of learning in the brain or any aspects of that mechanism, we should also try
*  to implement that in your network? If it turns out that we can't find back propagation in the brain.
*  If we can't find back propagation in the brain.
*  Well, so I guess your answer to that is back propagation is pretty damn useful. So
*  why are we complaining? I mean, I personally am a big fan of back propagation. I think it's a great
*  algorithm because it solves an extremely fundamental problem, which is finding a neural circuit subject
*  to some constraints. I don't see that problem going away. So that's why I really, I think it's
*  pretty unlikely that you'll have anything which is going to be dramatically different. It could
*  happen, but I wouldn't bet on it right now. So let me ask a sort of big picture question. Do you
*  think can do you think neural networks can be made to reason? Why not? Well, if you look, for example,
*  at AlphaGo or AlphaZero, the neural network of AlphaZero plays Go, which we all agree is a
*  game that requires reasoning. Better than 99.9% of all humans, just the neural network without the
*  search, just the neural network itself. Doesn't that give us an existence proof that neural
*  networks can reason? To push back and disagree a little bit, we all agree that Go is reasoning.
*  I think I agree. I don't think it's a trivial. So obviously reasoning like intelligence is a
*  loose gray area term a little bit. Maybe you disagree with that. But yes, I think it has some
*  of the same elements of reasoning. Reasoning is almost akin to search. There's a sequential element
*  element of stepwise consideration of possibilities and sort of building on top of those possibilities
*  in a sequential manner until you arrive at some insight. So yeah, I guess plain goes kind of like
*  that. And when you have a single neural network doing that without search, that's kind of like
*  that. So there's an existence proof in a particular constraint environment that a process akin to
*  what many people call reasoning exists, but more general kind of reasoning. So off the board.
*  There is one other existence proof. Oh boy. Which one? Us humans? Yes. Okay. All right. So
*  do you think the architecture that will allow neural networks to reason will look similar to
*  the neural network architectures we have today? I think it will. I think, well, I don't want to make
*  two overly definitive statements. I think it's definitely possible that the neural networks
*  that will produce the reasoning breakthroughs of the future will be very similar to the architectures
*  that exist today. Maybe a little bit more recurrent, maybe a little bit deeper. But
*  like these neural nets are so insanely powerful. Why wouldn't they be able to learn to reason?
*  Humans can reason. So why can't neural networks? So do you think the kind of stuff we've seen
*  neural networks do is a kind of just weak reasoning? So it's not a fundamentally different
*  process. Again, this is stuff we don't, nobody knows the answer to. So when it comes to our
*  neural networks, the thing which I would say is that neural networks are capable of reasoning.
*  But if you train a neural network on a task, which doesn't require reasoning,
*  it's not going to reason. This is a well-known effect where the neural network will solve exactly
*  the, it will solve the problem that you pose in front of it in the easiest way possible.
*  Right. That takes us to one of the brilliant sort of ways you describe neural networks,
*  which is you've referred to neural networks as the search for small circuits and maybe
*  general intelligence as the search for small programs, which I found is a metaphor very
*  compelling. Can you elaborate on that difference? Yeah. So the thing which I said precisely was
*  that if you can find the shortest program that outputs the data in your, at your disposal,
*  then you will be able to use it to make the best prediction possible.
*  And that's a theoretical statement, which can be proved mathematically.
*  Now you can also prove mathematically that it is that finding the shortest program, which generates
*  some data is not, is not a computable operation. No finite amount of compute can do this.
*  So then with, with neural networks, neural networks are the next best thing that actually
*  works in practice. We are not able to find the best, the shortest program, which generates our
*  data. But we are able to find, you know, a small, but now, now that statement should be amended,
*  even a large circuit, which fits our data in some way. Well, I think what you meant by the
*  small circuit is the smallest needed circuit. Well, I think the thing, the thing which I would
*  change now, back, back then I really have, I haven't fully internalized the overparameterized
*  results. The things we know about overparameterized neural nets. Now I would phrase it as a large
*  circuit that whose weights contain a small amount of information, which I think is what's going on.
*  If you imagine the training process of a neural network, as you slowly transmit entropy from the
*  data set to the parameters, then somehow the amount of information in the weights ends up
*  being not very large, which would explain why they generalize so well. So that's the large
*  circuit might be one that's helpful for the regular, for the generalization. Yeah, something
*  like this. But do you see there, do you see it important to be able to try to learn something
*  like programs? I mean, if we can, definitely. I think it's kind of, the answer is kind of yes,
*  if we can do it, we should do things that we can do it. It's, it's the reason we are pushing on deep
*  learning. The fundamental reason, the root cause is that we are able to train them.
*  So in other words, training comes first. We've got our pillar, which is the training pillar.
*  And now we're trying to contort our neural networks around the training pillar. We got
*  to stay trainable. This is an invariant we cannot violate. And so being trainable means
*  starting from scratch, knowing nothing, you can actually pretty quickly converge towards knowing
*  a lot. Or even slowly. But it means that given the resources at your disposal,
*  you can train the neural net and get it to achieve useful performance. Yeah, that's a
*  pillar we can't move away from. That's right. Because if you can, and whereas if you say, hey,
*  let's find the shortest program, well, we can't do that. So it doesn't matter how useful that would be.
*  We can do it. So we want to do you think you kind of mentioned that the neural networks are good
*  at finding small circuits or large circuits. Do you think then the matter of finding small programs
*  is just the data? No. So the cut, sorry, not not the size or character, the quality, the type of
*  data sort of ask giving it programs. Well, I think the thing is that right now, finding, there are no
*  good precedents of people successfully finding programs really well. And so the way you'd find
*  programs is you train a deep neural network to do it basically. Right. Which is which is the right
*  way to go about it. But there's not good illustrations that it hasn't been done yet. But
*  in principle, it should be possible. Can you elaborate a little bit? What's your insight in
*  principle? Put another way, you don't see why it's not possible. Well, it's kind of like,
*  more it's more a statement of I think that it's I think that it's unwise to bet against deep learning.
*  And if it's a fun if it's a cognitive function that humans seem to be able to do, then
*  it doesn't take too long for some deep neural net to pop up that can do it too.
*  Yeah, I'm there with you. I can I've stopped betting against neural networks at this point,
*  because they continue to surprise us. What about long term memory? Can neural networks have long
*  term memory or something like knowledge basis? So being able to aggregate important information
*  over long periods of time, that would then serve as useful sort of representations of state data
*  state that you can make decisions by so have a long term context based on which you make
*  a decision. So in some sense, the parameters already do that. The parameters are an aggregation of the
*  day of the neuron of the entirety of the neural experience. And so they count as the long as long
*  form long term knowledge. And people have trained various neural nets to act as knowledge bases and,
*  you know, investigated with invest people have investigated language and models knowledge basis.
*  So there is work there is work there. Yeah, but in some sense, do you think in every sense,
*  do you think there's a it's all just a matter of coming up with a better mechanism of forgetting
*  the useless stuff and remembering the useful stuff? Because right now, I mean, there's not
*  been mechanisms that do remember really long term information. What do you mean by that?
*  Precisely. Precisely. I like I like the word precisely. So
*  I'm thinking of the kind of compression of information the knowledge bases represent,
*  sort of creating a now I apologize for my sort of human centric thinking about what knowledge is
*  because neural networks aren't interpretable necessarily with the kind of knowledge they
*  have discovered. But a good example for me is knowledge bases being able to build up over time
*  something like the knowledge that Wikipedia represents. It's a really compressed structured
*  knowledge base, obviously not the actual Wikipedia or the language, but like a semantic web,
*  the dream that semantic web represented. So it's a really nice compressed knowledge base,
*  or something akin to that in the non interpretable sense as neural networks would have.
*  Well, the neural networks would be non interpretable if you look at their rates,
*  but their outputs should be very interpretable. Okay, so how do you how do you make very smart
*  neural networks like language models interpretable? Well, you ask them to generate some text and the
*  text will generally be interpretable. Do you find that the epitome of interpretability? Like,
*  can you do better? Like, can you because you can't okay, I'd like to know what does it know,
*  what doesn't know. I would like the neural network to come up with examples, where it's completely
*  dumb, and examples where it's completely brilliant. And the only way I know how to do that now is to
*  generate a lot of examples and use my human judgment. But it would be nice if a neural
*  network had some aware self awareness about. Yeah, 100% I'm a big believer in self
*  awareness. And I think that I think I think new neural net self awareness will allow for things
*  like the capabilities like the ones you described, like for them to know what they know and what they
*  don't know. And for them to know where to invest to increase their skills most optimally. And to
*  your question of interpretability, there are actually two answers to that question. One answer
*  is, you know, we have the neural net, so we can analyze the neurons and we can try to understand
*  what the different neurons and different layers mean. And you can actually do that and open AI
*  has done some work on that. But there is a different answer, which is that I would say
*  that's the human centric answer where you say, you know, you look at a human being, you can't read,
*  you know, how do you know what a human being is thinking? You ask them, you say, hey, what do you
*  think about this? What do you think about that? And you get some answers. The answers you get are
*  sticky in the sense you already have a mental model. You already have a mental model of that
*  human being. You already have an understanding of like a big conception of what it of that human
*  being, how they think, what they know, how they see the world. And then everything you ask, you're
*  adding onto that. And that stickiness seems to be that's one of the really interesting qualities of
*  the human being is that information is sticky. You don't, you seem to remember the useful stuff,
*  aggregate it well and forget most of the information that's not useful. That process,
*  but that's also pretty similar to the process in neural networks do. It's just that neural
*  networks are much crappier at this time. It doesn't seem to be fundamentally that different,
*  but just to stick on reasoning for a little longer. You said, why not? Why can't that reason?
*  What's a good impressive feat benchmark to you of reasoning?
*  That you'll be impressed by if you're not able to do. Is that something you already have in mind?
*  Well, I think writing, writing really good code. I think proving really hard theorems, solving
*  open ended problems with out of the box solutions.
*  And sort of theorem type mathematical problems.
*  Yeah, I think those ones are a very natural example as well. You know, if you can prove an
*  unproven theorem, then it's hard to argue you don't reason. And so by the way, and this comes
*  back to the point about the hard results, you know, if you've got a hard, if you have
*  machine learning and deep learning as a field is very fortunate because we have the ability
*  to sometimes produce these unambiguous results. And when they happen, the debate changes,
*  the conversation changes. It's a converse. We have the ability to produce conversation,
*  changing results, conversation. And then of course, the, the, the, the, the, the, the,
*  just like you said, people kind of take that for granted and say that wasn't actually a hard problem.
*  Well, I mean, at some point we'll probably run out of heart problems.
*  Yeah. That whole mortality thing is kind of, kind of a sticky problem that we haven't quite figured
*  out. Maybe we'll solve that one. I think one of the fascinating things in your entire body of work,
*  but also the work at opening eye recently, one of the conversation changes has been in the world of
*  language models. Can you briefly kind of try to describe the recent history of using neural
*  networks in the domain of language and text? Well, there's been lots of history. I think,
*  I think the Elman network was, was, was, was a small, tiny recurrent neural network applied
*  to language back in the eighties. So the history is really, you know, fairly long at least. And
*  the thing that started, the thing that changed the trajectory of neural networks and language is
*  the thing that changed the trajectory of all deep learning and that's data and compute.
*  So suddenly you move from small language models, which learn a little bit. And with language models
*  in particular, you can, there's a very clear explanation for why they need to be large to be
*  good because they're trying to predict the next word. So we don't, when you don't know anything,
*  you'll notice very, very broad strokes, surface level patterns. Like sometimes there are characters
*  and there is a space between those characters. You'll notice this pattern and you'll notice that
*  sometimes there is a comma and then the next character is a capital letter. You'll notice
*  that pattern. Eventually you may start to notice that there are certain words occur often. You may
*  notice that spellings are a thing. You may notice syntax. And when you get really good at all these,
*  you start to notice the semantics. You start to notice the facts, but for that to happen,
*  the language model needs to be larger. So that's, let's linger on that.
*  Cause that's where you and Noam Chomsky disagree.
*  So you think we're actually taking incremental steps, a sort of larger network, larger compute
*  will be able to get to the semantics, to be able to understand language without what Noam likes to
*  sort of think of as a fundamental understandings of the structure of language, like imposing your
*  theory of language onto the learning mechanism. So you're saying the learning you can learn
*  from raw data, the mechanism that underlies language.
*  Well, I think, I think it's pretty likely, but I also want to say that I don't really
*  know precisely what is, what Chomsky means when he talks about him. You said something about imposing
*  your structure on language. I'm not 100% sure what he means, but empirically it seems that when
*  you inspect those larger language models, they exhibit signs of understanding the semantics,
*  whereas the smaller language models do not. We've seen that a few years ago when we did work on the
*  sentiment neuron, we trained the small, you know, smallish LSTM to predict the next character
*  in Amazon reviews. And we noticed that when you increase the size of the LSTM from 500 LSTM cells
*  to 4,000 LSTM cells, then one of the neurons starts to represent the sentiment of the article,
*  of sorry, of the review. Now, why is that? Sentiment is a pretty semantic attribute,
*  it's not a syntactic attribute. And for people who might not know, I don't know if that's a
*  standard term, but sentiment is whether it's a positive or a negative review. That's right.
*  Like is the person happy with something or is the person unhappy with something? And so here we
*  had very clear evidence that a small neural net does not capture sentiment while a large neural
*  net does. And why is that? Well, our theory is that at some point you run out of syntax to models,
*  you start to go out of focus on something else. And with size, you quickly run out of syntax to
*  model and then you really start to focus on the semantics, this would be the idea. That's right.
*  And so I don't want to imply that our models have complete semantic understanding because that's not
*  true. But they definitely are showing signs of semantic understanding, partial semantic
*  understanding, but the smaller models do not show those signs. Can you take a step back and say,
*  what is GPT-2, which is one of the big language models that was the conversation changer in the
*  past couple of years? Yeah. So GPT-2 is a transformer with one and a half billion parameters
*  that was trained on about 40 billion tokens of text, which were obtained from web pages that
*  were linked to from Reddit articles with more than three uploads. And what's a transformer?
*  The transformer, it's the most important advance in neural network architectures in recent history.
*  What is attention maybe too? Because I think that's an interesting idea, not necessarily
*  technically speaking, but the idea of attention versus maybe what recurrent neural networks
*  represent. Yeah. So the thing is the transformer is a combination of multiple ideas simultaneously
*  of which attention is one. Do you think attention is the key? No, it's a key, but it's not the key.
*  The transformer is successful because it is the simultaneous combination of multiple ideas. And
*  if you were to remove either idea, it would be much less successful. So the transformer uses a
*  lot of attention, but attention existed for a few years. So that can't be the main innovation.
*  The transformer is designed in such a way that it runs really fast on the GPU.
*  And that makes a huge amount of difference. This is one thing. The second thing is that
*  transformer is not recurrent. And that is really important too, because it is more shallow and
*  therefore much easier to optimize. So in other words, it uses attention. It is a really great
*  fit to the GPU and it is not recurrent. So therefore less deep and easier to optimize.
*  And the combination of those factors make it successful. So now it makes great use of your
*  GPU. It allows you to achieve better results for the same amount of compute.
*  And that's why it's successful. Were you surprised how well transformers worked and GPT-2 worked?
*  So you worked on language. You've had a lot of great ideas before transformers came about in
*  language. So you got to see the whole set of revolutions before and after. Were you surprised?
*  Yeah, a little.
*  A little?
*  I mean, it's hard to remember because you adapt really quickly, but it definitely was surprising.
*  It definitely was. In fact, you know what? I'll retract my statement. It was pretty amazing.
*  It was just amazing to see, generate this text of this. And you know, you've got to keep in mind
*  that at that time, we've seen all this progress in GANs in improving the samples produced by GANs
*  were just amazing. You have these realistic faces, but text hasn't really moved that much.
*  And suddenly we moved from whatever GANs were in 2015 to the best, most amazing GANs in one step.
*  And that was really stunning. Even though theory predicted, yeah, you train a big language model,
*  of course you should get this. But then to see it with your own eyes, it's something else.
*  And yet we adapt really quickly. And now there's sort of some cognitive scientists
*  write articles saying that GPT-2 models don't truly understand language. So we adapt quickly
*  to how amazing the fact that they're able to model the language so well is. So what do you
*  think is the bar for impressing us that it... I don't know. Do you think that bar will continuously
*  be moved? Definitely. I think when you start to see really dramatic economic impact, that's when,
*  I think that's in some sense the next barrier. Because right now, if you think about the work
*  in AI, it's really confusing. It's really hard to know what to make of all these advances.
*  It's kind of like, okay, you got an advance and now you can do more things and you got another
*  improvement and you got another cool demo. At some point, I think people who are outside of AI,
*  they can no longer distinguish this progress anymore.
*  So we were talking offline about translating Russian to English and how there's a lot of
*  brilliant work in Russian that the rest of the world doesn't know about. That's true for Chinese,
*  that's true for a lot of scientists and just artistic work in general. Do you think translation
*  is the place where we're going to see economic big impact? I don't know. I think there is a huge
*  number of applications. First of all, I want to point out that translation already today is huge.
*  I think billions of people interact with big chunks of the internet, primarily through
*  translation. So translation is already huge and it's hugely positive too. I think self-driving
*  is going to be hugely impactful. It's unknown exactly when it happens, but again, I would
*  not bet against deep learning. So that's deep learning in general. Deep learning for self-driving.
*  Yes, deep learning for self-driving. But I was talking about sort of language models.
*  I see. I veered off a little bit. Just to check. You're not seeing a connection
*  between driving and language. No, no. Okay. Or rather, both use neural nets.
*  That'd be a poetic connection. I think there might be some, like you said, there might be
*  some kind of unification towards a kind of multitask transformers that can take on both
*  language and vision tasks. That'd be an interesting unification. Let's see. What can I ask about GPT-2
*  more? It's simple. So not much to ask. You take a transform, you make it bigger, you give it more
*  data, and suddenly it does all those amazing things. Yeah. One of the beautiful things is
*  that GPT, the transformers are fundamentally simple to explain, to train. Do you think
*  bigger will continue to show better results in language? Probably. What are the next steps
*  with GPT-2, do you think? I think for sure seeing what larger versions can do is one direction.
*  Also, I mean, there are many questions. There's one question which I'm curious about, and that's the
*  following. So right now, GPT-2, so we feed it all this data from the internet, which means that it
*  needs to memorize all those random facts about everything in the internet. And it would be nice
*  if the model could somehow use its own intelligence to decide what data it wants to accept and what
*  data it wants to reject. Just like people. People don't learn all data indiscriminately.
*  We are super selective about what we learn. And I think this kind of active learning,
*  I think, would be very nice to have. Yeah. Listen, I love active learning. So
*  let me ask, does the selection of data, can you just elaborate that a little bit more? Do
*  you think the selection of data is... I have this kind of sense that the optimization of how you
*  select data, so the active learning process, is going to be a place for a lot of breakthroughs,
*  even in the near future, because there hasn't been many breakthroughs there that are public.
*  I feel like there might be private breakthroughs that companies keep to themselves, because the
*  fundamental problem has to be solved if you want to solve self-driving, if you want to solve a
*  particular task. What do you think about the space in general? Yeah. So I think that for something
*  like active learning, or in fact, for any kind of capability, like active learning, the thing that
*  it really needs is a problem. It needs a problem that requires it. It's very hard to do research
*  about the capability if you don't have a task, because then what's going to happen is you will
*  come up with an artificial task, get good results, but not really convince anyone.
*  Right. We're now past the stage where getting a result on MNIST, some clever formulation of MNIST
*  will convince people. That's right. In fact, you could quite easily come up with a simple active
*  learning scheme on MNIST and get a 10x speed up, but then so what? I think that with active learning,
*  the need for active learning will naturally arise as problems that require it pop up.
*  That's my take on it. There's another interesting thing that OpenAI has brought up with GPT-2,
*  which is when you create a powerful artificial intelligence system, and it was unclear
*  what kind of detrimental, once you release GPT-2, what kind of detrimental effect it will have,
*  because if you have a model that can generate pretty realistic text, you can start to imagine
*  that it would be used by bots in some way that we can't even imagine. There's this nervousness
*  about what it's possible to do. You did a really brave and I think profound thing,
*  which is started a conversation about this. How do we release powerful artificial intelligence
*  models to the public? If we do it all, how do we privately discuss with other, even competitors,
*  about how we manage the use of the systems and so on? From this whole experience, you released
*  a report on it, but in general, are there any insights that you've gathered from just thinking
*  about this, about how you release models like this? I think that my take on this is that the field of
*  AI has been in a state of childhood, and now it's exiting that state and it's entering a state of
*  maturity. What that means is that AI is very successful and also very impactful, and its
*  impact is not only large, but it's also growing. For that reason, it seems wise to start thinking
*  about the impact of our systems before releasing them, maybe a little bit too soon,
*  rather than a little bit too late. With the case of GPT-2, like I mentioned earlier,
*  the results really were stunning. It didn't seem certain, it seemed plausible that
*  something like GPT-2 could easily use to reduce the cost of this information.
*  There was a question of what's the best way to release it, and a staged release seemed logical.
*  A small model was released, and there was time to see the... Many people use these models in lots of
*  cool ways. There have been lots of really cool applications. There haven't been any negative
*  applications we know of, and so eventually it was released. But also other people replicated
*  similar models. That's an interesting question though that we know of. In your view, staged release
*  is at least part of the answer to the question of how do we...
*  What do we do once we create a system like this? It's part of the answer, yes.
*  Is there any other insights? Say you don't want to release the model at all,
*  because it's useful to you for whatever the business is. Well, there are plenty of people
*  don't release models already. Right, of course. But is there some moral, ethical responsibility
*  when you have a very powerful model to communicate? Just as you said, when you had GPT-2,
*  it was unclear how much it could be used for misinformation. It's an open question.
*  Getting an answer to that might require that you talk to other really smart people that are
*  outside of your particular group. Please tell me there's some optimistic pathway for
*  people across the world to collaborate on these kinds of cases.
*  Or is it still really difficult from one company to talk to another company?
*  So it's definitely possible. It's definitely possible to discuss these kinds of models
*  with colleagues elsewhere and to get their take on what to do.
*  How hard is it though? I mean...
*  Do you see that happening? I think that's a place where it's
*  important to gradually build trust between companies, because ultimately, all the AI
*  developers are building technology which is going to be increasingly more powerful.
*  The way to think about it is that ultimately we all need to get it.
*  Yeah. I tend to believe in the better angels of our nature, but I do hope
*  that when you build a really powerful AI system in a particular domain,
*  that you also think about the potential negative consequences of... Yeah.
*  It's an interesting and scary possibility that there will be a race for AI development that
*  would push people to close that development and not share ideas with others.
*  I don't love this. I've been a pure academic for 10 years. I really like sharing ideas and it's fun.
*  It's exciting. What do you think it takes to... Let's talk about AGI a little bit. What do you
*  think it takes to build a system of human level intelligence? What do you think it takes to build
*  a system of human level intelligence? We talked about reasoning, we talked about long term memory,
*  but in general, what does it take, do you think? Well, I can't be sure,
*  but I think the deep learning plus maybe another small idea. Do you think self-play will be
*  involved? You've spoken about the powerful mechanism of self-play where systems learn by
*  sort of exploring the world in a competitive setting against other entities that are similarly
*  skilled as them and so incrementally improve in this way. Do you think self-play will be a component
*  of building an AGI system? Yeah. So what I would say to build AGI, I think is going to be
*  deep learning plus some ideas and I think self-play will be one of those ideas.
*  Self-play has this amazing property that it can surprise us in truly novel ways. For example,
*  I mean, pretty much every self-play system, both our Dota bot, I don't know if OpenAI had a release
*  about multi-agent where you had two little agents who were playing hide and seek and of course,
*  also AlphaZero, they were all produced surprising behaviors. They all produce behaviors that we
*  didn't expect. They are creative solutions to problems and that seems like an important part
*  of AGI that our systems don't exhibit routinely right now and so that's why I like this area,
*  I like this direction because of its ability to surprise us. To surprise us and an AGI system
*  would surprise us fundamentally. Yes, and to be precise, not just in terms of the AGI system,
*  but to find the surprising solution to a problem is also useful.
*  Now, a lot of the self-play mechanisms have been used in the game context or at least in the
*  simulation context. How far along the path to AGI do you think will be done in simulation? How much
*  faith promise do you have in simulation versus having to have a system that operates in the real
*  world, whether it's the real world of digital real world data or real world like actual physical
*  world with robotics? I don't think it's in either or. I think simulation is a tool and it helps. It
*  has certain strengths and certain weaknesses and we should use it. Yeah, but okay, I understand that.
*  That's true, but one of the criticisms of self-play, one of the criticisms of reinforcement
*  learning is one of its current power, its current results, while amazing, have been demonstrated in
*  a simulated environment or very constrained physical environments. Do you think it's possible
*  to escape them, escape the simulated environments and be able to learn in non-simulated environments
*  or do you think it's possible to also just simulate in the photorealistic and physics
*  realistic way the real world in a way that we can solve real problems with self-play in simulation?
*  I think that transfer from simulation to the real world is definitely possible and has been exhibited
*  many times by many different groups. It's been especially successful in vision. Also, OpenAI
*  in the summer has demonstrated a robot hand which was trained entirely in simulation
*  in a certain way that allowed for sim to real transfer to occur.
*  Is this for the Rubik's Cube? Yes, right. I wasn't aware that was trained in simulation.
*  It was trained in simulation entirely. Really? So it wasn't in the physics that the hand wasn't
*  trained? No, 100% of the training was done in simulation and the policy that was learned in
*  simulation was trained to be very adaptive. So adaptive that when you transfer it, it could
*  very quickly adapt to the physical world. So the kind of perturbations with the
*  giraffe or whatever the heck it was, were those part of the simulation?
*  Well, the simulation was generally, so the simulation was trained to be robust to many
*  different things but not the kind of perturbations we've had in the video. So it's never been trained
*  with the glove, it's never been trained with a stuffed giraffe. So in theory, these are novel
*  perturbations? Correct. It's not in theory, in practice. Those are novel perturbations? Well,
*  that's okay. That's a clean, small scale but clean example of a transfer from the simulated world to
*  the physical world. Yeah, and I will also say that I expect the transfer capabilities of deep learning
*  to increase in general and the better the transfer capabilities are, the more useful simulation will
*  become. Because then you could take, you could experience something in simulation and then learn
*  a moral of the story which you could then carry with you to the real world, right? As humans do all
*  the time when they play computer games. So let me ask sort of an embodied question,
*  staying on AGI for a sec. Do you think AGI says that we need to have a body? We need to have some
*  of those human elements of self-awareness, consciousness, sort of fear of mortality,
*  sort of self-preservation in the physical space which comes with having a body. I think having
*  a body will be useful. I don't think it's necessary. But I think it's very useful to have a body for
*  sure because you can learn a whole new, you can learn things which cannot be learned without a body.
*  But at the same time, I think that if you don't have a body, you could compensate for it and
*  still succeed. You think so? Yes. Well, there is evidence for this. For example,
*  there are many people who were born deaf and blind and they were able to compensate for the lack of
*  modalities. I'm thinking about Helen Keller specifically. So even if you're not able to
*  physically interact with the world and if you're not able to, I mean, I actually was getting at,
*  maybe let me ask on the more particular, I'm not sure if it's connected to having a body or not,
*  but the idea of consciousness and a more constrained version of that is self-awareness.
*  Do you think an AGI system should have consciousness? We can't define consciousness. Whatever the heck
*  you think consciousness is. Yeah. Hard question to answer, given how hard it is to define it.
*  Do you think it's useful to think about? I mean, it's definitely interesting. It's fascinating.
*  I think it's definitely possible that our systems will be conscious.
*  Do you think that's an emergent thing that just comes from, do you think consciousness could
*  emerge from the representation that's stored within your networks? So like that it naturally
*  just emerges when you become more and more, you're able to represent more and more of the world?
*  Well, I'd say I'd make the following argument, which is humans are conscious. And if you believe
*  that artificial neural nets are sufficiently similar to the brain, then there should at
*  least exist artificial neural nets you should be conscious to. You're leaning on that existence
*  proof pretty heavily. Okay. That's the best answer I can give. No, I know. I know. There's still an
*  open question if there's not some magic in the brain that we're not. I mean, I don't mean a
*  non-materialistic magic, but that the brain might be a lot more complicated and interesting that
*  we give it credit for. If that's the case, then it should show up. And at some point,
*  we will find out that we can't continue to make progress. But I think it's unlikely.
*  So we talk about consciousness, but let me talk about another poorly defined concept of intelligence.
*  Again, we've talked about reasoning, we've talked about memory. What do you think is a good test
*  of intelligence for you? Are you impressed by the test that Alan Turing formulated with the
*  imitation game with natural language? Is there something in your mind that you will be deeply
*  impressed by if a system was able to do? I mean, lots of things. There's a certain frontier of
*  capabilities today, and there exist things outside of that frontier, and I would be impressed by any
*  such thing. For example, I would be impressed by a deep learning system which solves a very
*  pedestrian task like machine translation or computer vision task or something which never
*  makes a mistake a human wouldn't make under any circumstances. I think that is something which
*  have not yet been demonstrated, and I would find it very impressive. Yeah, so right now, they make
*  mistakes and they might be more accurate than human beings, but they still make a different
*  set of mistakes. So I would guess that a lot of the skepticism that some people have about deep
*  learning is when they look at their mistakes and they say, well, those mistakes, they make no sense.
*  If you understood the concept, you wouldn't make that mistake. And I think that changing that would
*  inspire me. That would be, yes, this is progress. Yeah, that's a really nice way to put it.
*  But I also just don't like that human instinct to criticize a model is not intelligent. That's the
*  same instinct as we do when we criticize any group of creatures as the other, because
*  it's very possible that GPT-2 is much smarter than human beings at many things.
*  That's definitely true. It has a lot more breadth of knowledge.
*  Yes, breadth of knowledge and even perhaps depth on certain topics.
*  It's kind of hard to judge what depth means, but there's definitely a sense in which
*  humans don't make mistakes that these models do.
*  The same is applied to autonomous vehicles. The same is probably going to continue being
*  applied to a lot of artificial intelligence systems. We find this is the process of,
*  in the 21st century, the process of analyzing the progress of AI is the search for one case
*  where the system fails in a big way where humans would not. And then many people writing articles
*  about it and then broadly the public generally gets convinced that the system is not intelligent.
*  And we like pacify ourselves by thinking it's not intelligent because of this one
*  anecdotal case. And this seems to continue happening.
*  There is truth to that. Although I'm sure that plenty of people are also extremely impressed
*  by the systems that exist today. But I think this connects to the earlier point we discussed that
*  it's just confusing to judge progress in AI. And you have a new robot demonstrating something.
*  How impressed should you be? And I think that people will start to be impressed once
*  AI starts to really move the needle on the GDP.
*  So you're one of the people that might be able to create an AGI system here, not you, but you
*  in OpenAI. If you do create an AGI system and you get to spend sort of the evening with it
*  him her, what would you talk about? Do you think?
*  The very first time?
*  First time.
*  Well, the first time I would just ask all kinds of questions and try to make it to get it to make
*  a mistake. And I would be amazed that it doesn't make mistakes and just keep asking broad.
*  What kind of questions do you think? Would they be factual or would they be
*  personal, emotional, psychological? What do you think?
*  All of the above.
*  Would you ask for advice?
*  Definitely. I mean, why would I limit myself talking to a system like this?
*  Now, again, let me emphasize the fact that you truly are one of the people that might be in the
*  room where this happens. So let me ask a sort of a profound question about, I've just talked to a
*  Stalin historian, been talking to a lot of people who are studying power. Abraham Lincoln said,
*  nearly all men can stand adversity, but if you want to test a man's character, give him power.
*  I would say the power of the 21st century, maybe the 22nd, but hopefully the 21st would be the
*  creation of an AGI system and the people who have control, direct possession and control the AGI
*  system. So what do you think after spending that evening having a discussion with the AGI system,
*  what do you think you would do?
*  Well, the ideal world would like to imagine
*  is one where humanity, alike, the board members of a company where the AGI is the CEO.
*  So it would be, I would like the picture which I would imagine is you have some kind of different
*  entities, different countries or cities, and the people that leave their vote for what the
*  AGI that represents them should do and then AGI that presents them goes and does it. I think a
*  picture like that I find very appealing. You could have multiple AGI, you would have an AGI for a
*  city, for a country, and it would be trying to, in effect, take the democratic process to the next
*  level. And the board can almost fire the CEO. Essentially, press the reset button, say.
*  Press the reset button. Re-randomize the parameters.
*  But let me sort of, that's actually, okay, that's a beautiful vision, I think, as long as it's
*  possible to press the reset button. Do you think it will always be possible to press the reset button?
*  Do you think it will always be possible to press the reset button?
*  So I think that it's definitely really possible to build.
*  So you're talking, so the question that I really understand from you is, will humans or
*  humans people have control over the AI systems that they build?
*  Yes.
*  And my answer is, it's definitely possible to build AI systems which
*  will want to be controlled by their humans.
*  Wow, that's part of their, so it's not that just they can't help but be controlled, but that's
*  they exist. One of the objectives of their existence is to be controlled.
*  In the same way that human parents
*  generally want to help their children, they want their children to succeed,
*  it's not a burden for them. They are excited to help the children and to feed them and to dress
*  them and to take care of them. And I believe with high conviction that the same will be possible
*  for an AGI. It will be possible to program an AGI, to design it in such a way that it will have a
*  similar deep drive that it will be delighted to fulfill and the drive will be to help humans
*  flourish. But let me take a step back to that moment where you create the AGI system. I think
*  this is a really crucial moment. And between that moment and the Democratic board members with the
*  AGI at the head, there has to be a relinquishing of power. So as George Washington, despite all
*  the bad things he did, one of the big things he did is he relinquished power. He first of all,
*  didn't want to be president. And even when he became president, he gave, he didn't keep just
*  serving as most dictators do for indefinitely. Do you see yourself being able to relinquish
*  control over an AGI system, given how much power you can have over the world? At first financial,
*  just make a lot of money, right? And then control by having possession of this AGI system.
*  I'd find it trivial to do that. I'd find it trivial to relinquish this kind of power. I mean,
*  you know, the kind of scenario you are describing sounds terrifying to me.
*  That's all. I would absolutely not want to be in that position.
*  Do you think you represent the majority or the minority of people in the AI community?
*  Well, I mean, open question, an important one. Are most people good is another way to ask it.
*  So I don't know if most people are good, but
*  I think that when it really counts, people can be better than we think.
*  That's beautifully put. Yeah. Are there specific mechanism you can think of, of aligning AIG
*  values to human values? Is that, do you think about these problems of continued alignment
*  as we develop the AI systems? Yeah, definitely. In some sense,
*  the kind of question which you are asking is, so if I were to translate the question to today's
*  terms, it would be a question about how to get an RL agent that's optimizing a value function,
*  which itself is learned. And if you look at humans, humans are like that because the
*  reward function, the value function of humans is not external, it is internal. That's right.
*  Internal. And there are definite ideas of how to train a value function, basically an objective,
*  you know, an as objective as possible perception system that will be trained separately
*  to recognize, to internalize human judgments on different situations. And then that component
*  wouldn't be integrated as the value, as the base value function for some more capable RL system.
*  You could imagine a process like this. I'm not saying this is the process,
*  I'm saying this is an example of the kind of thing you could do.
*  So on that topic of the objective functions of human existence, what do you think is the
*  objective function that's implicit in human existence? What's the meaning of life?
*  Oh, I think the question is wrong in some way. I think that the question implies that there is
*  an objective answer, which is an external answer, you know, your meaning of life is X.
*  I think what's going on is that we exist and that's amazing. And we should try to make the
*  most of it and try to maximize our own value and enjoyment of a very short time while we do exist.
*  It's funny because action does require an objective function. It's definitely there
*  in some form, but it's difficult to make it explicit and maybe impossible to make it explicit,
*  I guess is what you're getting at. And that's an interesting fact of an RL environment.
*  Well, I was making a slightly different point is that humans want things and their wants create
*  the drives that cause them to, you know, our wants are our objective functions,
*  our individual objective functions. We can later decide that we want to change,
*  that what we wanted before is no longer good and we want something else.
*  Yeah, but they're so dynamic. There's got to be some underlying sort of Freud,
*  there's things, there's like sexual stuff, there's people think it's the fear of fear of death.
*  And there's also the desire for knowledge and, you know, all these kinds of things,
*  procreation, sort of all the evolutionary arguments. It seems to be there might be
*  some kind of fundamental objective function from which everything else emerges. But it seems like
*  that's very difficult to make it explicit. I think that probably is an evolutionary
*  objective function, which is to survive and procreate and make your children succeed.
*  That would be my guess. But it doesn't give an answer to the question of what's the meaning of
*  life. I think you can see how humans are part of this big process, this ancient process. We exist
*  on a small planet and that's it. So given that we exist, try to make the most of it and try to
*  enjoy more and suffer less as much as we can. Let me ask two silly questions about life.
*  One, do you have regrets? Moments that if you went back, you would do differently. And two,
*  are there moments that you're especially proud of that made you truly happy?
*  So I can answer both questions. Of course, there's a huge number of choices and decisions that I've
*  made that with the benefit of hindsight, I wouldn't have made them. And I do experience some regret,
*  I do experience some regret, but I try to take solace in the knowledge that at the time I did
*  the best I could. And in terms of things that I'm proud of, I'm very fortunate to have done
*  things I'm proud of. And they made me happy for some time, but I don't think that that is
*  the source of happiness. So your academic accomplishments, all the papers, you're one
*  of the most cited people in the world, all the breakthroughs I mentioned in computer vision and
*  language and so on. What is the source of happiness and pride for you?
*  All those things are a source of pride for sure. I'm very grateful for having done all those things.
*  And it was very fun to do them. But happiness comes, but you know, you can happiness, well,
*  my current view is that happiness comes from our, to a very large degree from the way we look at
*  things. You know, you can have a simple meal and be quite happy as a result, or you can talk to
*  someone and be happy as a result as well. Or conversely, you can have a meal and be disappointed
*  that the meal wasn't a better meal. So I think a lot of happiness comes from that, but I'm not sure.
*  I don't want to be too confident. Being humble in the face of the uncertainty seems to be also part
*  of this whole happiness thing. Well, I don't think there's a better way to end it than meaning of
*  life and discussions of happiness. So Ilya, thank you so much. You've given me a few incredible
*  ideas. You've given the world many incredible ideas. I really appreciate it. And thanks for
*  talking today. Yeah, thanks for stopping by. I really enjoyed it. Thanks for listening to this
*  conversation with Ilya Setskever and thank you to our presenting sponsor, Cash App. Please consider
*  supporting the podcast by downloading Cash App and using the code LEXPODCAST. If you enjoy this
*  podcast, subscribe on YouTube, review it with five stars on Apple Podcasts, support it on Patreon,
*  or simply connect with me on Twitter at Lex Friedman. And now let me leave you with some words
*  from Alan Turing on machine learning. Instead of trying to produce a program to simulate the adult
*  mind, why not rather try to produce one which simulates the child's? If this were then subjected
*  to an appropriate course of education, one would obtain the adult brain. Thank you for listening
*  and hope to see you next time.
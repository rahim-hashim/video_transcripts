---
Date Generated: September 06, 2024
Transcription Model: whisper medium 20231117
Length: 6720s
Video Keywords: []
Video Views: 1215
Video Rating: None
Video Description: Nathan explores the cutting-edge field of mechanistic interpretability with Dan Balsam and Tom McGrath, co-founders of Goodfire. In this episode of The Cognitive Revolution, we delve into the science of understanding AI models' inner workings, recent breakthroughs, and the potential impact on AI safety and control. Join us for an insightful discussion on sparse autoencoders, polysemanticity, and the future of interpretable AI.

PAPERS
- Very accessible article on types of representations: Local vs Distributed Coding (https://www.persee.fr/doc/intel_0769-4113_1989_num_8_2_873)

- Theoretical understanding of how models might pack concepts into their representations: Toy Models of Superposition (https://transformer-circuits.pub/2022/toy_model/index.html)

- How structure in the world gives rise to structure in the latent space: The Geometry of Categorical and Hierarchical Concepts in Large Language Models (https://arxiv.org/abs/2406.01506)

- Using sparse autoencoders to pull apart language model representations: Sparse Autoencoders (https://www.lesswrong.com/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition) / Towards Monosemanticity (https://transformer-circuits.pub/2023/monosemantic-features/index.html) / Scaling Monosemanticity (https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)

- Finding & teaching concepts in superhuman systems: Acquisition of Chess Knowledge in AlphaZero (https://arxiv.org/abs/2111.09259) / Bridging the Human-AI Knowledge Gap: Concept Discovery and Transfer in AlphaZero (https://arxiv.org/abs/2310.16410)

- Connecting microscopic learning to macroscopic phenomena: The Quantization Model of Neural Scaling (https://arxiv.org/abs/2303.13506)

- Understanding at scale: Language models can explain neurons in language models (https://openai.com/index/language-models-can-explain-neurons-in-language-models/)

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST: History 102
Every week, creator of WhatifAltHist Rudyard Lynch and Erik Torenberg cover a major topic in history in depth -- in under an hour. This season will cover classical Greece, early America, the Vikings, medieval Islam, ancient China, the fall of the Roman Empire, and more.Subscribe on 
Spotify: https://open.spotify.com/show/36Kqo3BMMUBGTDo1IEYihm
Apple: https://podcasts.apple.com/us/podcast/history-102-with-whatifalthists-rudyard-lynch-and/id1730633913
YouTube: https://www.youtube.com/@History102-qg5oj

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:00:22) About the Episode
(00:03:52) Introduction and Background
(00:08:43) State of Interpretability Research
(00:12:06) Key Insights in Interpretability
(00:16:53) Polysemanticity and Model Compression (Part 1)
(00:17:00) Sponsors: Oracle | Brave
(00:19:04) Polysemanticity and Model Compression (Part 2)
(00:22:50) Sparse Autoencoders Explained
(00:27:19) Challenges in Interpretability Research (Part 1)
(00:30:54) Sponsors: Omneky | Squad
(00:32:41) Challenges in Interpretability Research (Part 2)
(00:33:51) Goodfire's Vision and Mission
(00:37:08) Interpretability and Scientific Models
(00:43:48) Architecture and Interpretability Techniques
(00:50:08) Quantization and Model Representation
(00:54:07) Future of Interpretability Research
(01:01:38) Skepticism and Challenges in Interpretability
(01:07:51) Alternative Architectures and Universality
(01:13:39) Goodfire's Business Model and Funding
(01:18:47) Building the Team and Future Plans
(01:31:03) Hiring and Getting Involved in Interpretability
(01:51:28) Closing Remarks
(01:51:38) Outro
---

# Popular Mechanistic Interpretability Goodfire Lights the Way to AI Safety
**Cognitive Revolution:** [August 17, 2024](https://www.youtube.com/watch?v=45g68Zu3E2k)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today I'm thrilled to be speaking
*  with Dan Balsam and Tom McGrath, co-founders of GoodFire, a new company focused on mechanistic
*  interpretability of AI models. Dan serves as CTO, bringing his experience as a serial startup
*  engineer, while Tom, the chief scientist, comes from a background in AI safety research at DeepMind.
*  As you know, mechanistic interpretability is the nascent science that seeks to understand AI models
*  in our workings and explain why they do what they do, and which promises to light the way to
*  engineering solutions to problems of AI control and safety. Like many subfields of AI, mechanistic
*  interpretability has delivered incredible progress over the last couple of years, as all three leading
*  developers, led by Amtropic but with DeepMind and OpenAI right on their heels, as well as Academia,
*  which has been enabled by Lama3 and other open source foundation models, have made real progress
*  on the great AI black box problem. Most recently, sparse autoencoders have emerged as a powerful tool
*  for isolating and studying the concepts, also known as features, that large language models are
*  learning, and which are already beginning to be used for monitoring LLM internal states and
*  steering their behavior. If you played with Golden Gate Clawed, where Amtropic intervened to set the
*  Golden Gate Bridge feature to an artificially high level, or just had a laugh at some of the examples
*  posted online, you already have an intuitive sense for what these sparse autoencoder discovered
*  features can do. In this conversation, which I hope will be just the first of many interpretability
*  roundups with Dan and Tom, we cover a wide range of interpretability topics, including the concept
*  of polysemanticity in neural networks and the challenges that this phenomenon poses for
*  interpretability, engineering techniques for large-scale interpretability studies, including
*  activation patching, causal tracing, and feature editing, the rise of sparse autoencoders, including
*  their architecture, training processes, and outputs, early progress in autointerpretability,
*  which is the use of language models to label the features isolated by sparse autoencoders,
*  the potential for interpretability to extract scientific knowledge from domain-specific models,
*  such as those trained on protein folding, weather prediction, and other problems,
*  the technical challenges of serving interpretable models in production environments at scale,
*  and how new AI architectures may impact interpretability science going forward.
*  Toward the end, Dan and Tom shared their vision for GoodFire, which recently raised $7 million
*  in seed funding led by Lightspeed Ventures to develop and ultimately productize this line of
*  research for open-source models. The goal is to empower developers and even everyday users to
*  look inside models, diagnose issues, and intervene in ways that improve performance and reliability,
*  and ultimately to create a world in which companies simply don't deploy AI models that
*  they don't understand. I am personally very excited about this direction, and I appreciate
*  that the GoodFire team has allowed me to invest a very small amount in the company as part of this
*  fundraising round. As always, if you're finding value in the show, we'd appreciate it if you'd
*  share it with friends, post online, or leave us a review on Apple or Spotify. And I love hearing
*  from listeners and strive to respond to all messages, so please do feel free to DM me on
*  your favorite social network anytime. Now, let's dive into the fascinating and fast-moving world
*  of AI interpretability with Dan Balsam and Tom McGrath, co-founders of the new mechanistic
*  interpretability startup, GoodFire. Dan Balsam and Tom McGrath, CTO and chief scientist of the new
*  mechanistic interpretability company, GoodFire, welcome to the Cognitive Revolution.
*  Thank you for having us. Great, thanks. Yeah, really excited to be here.
*  I'm excited for this too. We've been talking offline for the last couple of months as you guys
*  have been putting this company together, and I was excited about it enough to make a very small
*  investment. So a disclaimer for this episode is that I am an interested party in this company,
*  although for anyone else who might seek my investment, just know that it would be an
*  extremely tiny check size. But love what you guys are aspiring to do here in terms of figuring out
*  how to not just get deeper into mechanistic interpretability, but to figure out how to make
*  a product of that and to make that something that the whole world can get access to and take
*  advantage of and collaboratively explore together. So I'm really excited to unpack this in detail and
*  get your take on where we are in interpretability. I think this is going to be a lot of fun.
*  For starters, you guys want to just introduce yourselves. I think you have quite different
*  backgrounds, which is interesting. And people who are maybe inclined to be intimidated by
*  mechanistic interpretability might see some inspiration, especially in your background,
*  Dan. But give us both of them. Yeah. So I have been a serial early employee at startups,
*  serial founding engineer for most of my career. Most recently at a Series B AI recruiting startup
*  called Ripple Match. And around the time of the release of Chet GBT, I really was shaken awake
*  quite abruptly by the rate of progress in AI. I led our initiatives at Ripple Match integrating
*  generated AI into the product. And I quickly realized that not only was this technology
*  extremely powerful and going to change the way that we did business at Ripple Match pretty
*  profoundly, the black box nature of the systems made it really hard to engineer effectively with
*  them. And so it took a little bit of while to get up to speed, catch up to the state of the art in
*  the research and really increase my depth of understanding in a way that was necessary to
*  really understand what's going on with generative AI. And I very quickly in that process decided
*  there was nothing else that was worth working on besides minimizing AI risk in one way, shape or
*  form. I actually, I decided to leave my job at Ripple Match, which was an extremely hard decision
*  to do because I helped build that team from the ground up and I really love the engineering team
*  over there and big shout out to them. But it turned out that Eric, our other co-founder,
*  who's not with us today, came to the same conclusion around the same time. And he and I both put our
*  notice into Ripple Match, which he founded within a week of each other. And as we learned more and
*  more about interpretability, we just became so excited by how much progress was being made and
*  how quickly that progress was being made and believe that there is really great opportunities
*  to start a business that would help scale interpretability research and just drive forward
*  the progress and cracking open the black box. So we ended up meeting Tom because it turned out
*  that Tom had written a doc with a lot of the same ideas that we were discussing in terms of building
*  an interpretability business. And as we were talking to a lot of people in the interpretability
*  community, we were put in touch. And after we started speaking to each other, we were like,
*  wow, we're thinking about this problem in a lot of the same ways. Let's start a business together
*  and see what we can accomplish. Cool. Tom, you've been at it for a little longer in the
*  interpretability game. What's your story? Yeah, that's right. So I was at DeepMind
*  from 2019 to 2023. In 2016, I was doing my PhD. And I had this feeling, oh, this AI thing
*  could be pretty big, which is probably one of the better bets that I've made in my career.
*  And then I pivoted from an applied maths and statistics PhD into working more in machine
*  learning. So I joined DeepMind in the safety team. And while I was there, I fell in love with doing
*  interpretability research. And I think since then, maybe a lot more excitement has happened in line
*  with all the progress that's happened. So I left DeepMind in 2023 with this sort of still being
*  really excited about interpretability, but not quite sure what I wanted to do with that.
*  And then I went to South Park Commons, which is a great community in San Francisco.
*  And I was thinking about this for a while, I decided that the thing to do was try and make
*  interpretability useful as one of the great questions about interpretability. What's it good
*  for? And I was like, a great deal has happened. Probably it's going to be useful for a lot. And
*  the best way to test that is to start a company. While I was going down that road, yeah, I got put
*  in touch with Dan and Eric. And the rest is history. We're such a great fit. And we're completely kind
*  of complimentary. So we decided to work together and things are going great. Cool. So maybe for
*  starters, I would love to rewind the tape a little bit. And any regular listeners to this podcast
*  will know that this is definitely a topic of great interest to me as well. And we've done episodes
*  approaching it in different ways with a few different researchers. And occasionally, I'll even
*  find enough time to do my own little literature review. But I'd love to set the stage with what
*  is the state of interpretability today? How would you give us like the intellectual history, maybe
*  over the last couple of years? What have been the major threads and developments? And we can build
*  up to what do we know now? I'd be fascinated to hear your narrative of where we are in interpretability
*  today. I think like a lot of the sort of AI story in the last, let me know, 10 years or less, maybe
*  certainly the last five years, it's a story of sort of steady progress, a little bit unremarked,
*  and then a sudden explosion, want a better word. There was a long period when interpretability
*  was pretty unfashionable. And there were a lot of beliefs around it, like, maybe it just doesn't
*  work. There's nothing in the models to find. And even if there was, you wouldn't be able to find it.
*  And then the sort of steady accumulation of a bit of evidence started to pile up. But we had no sort
*  of means of extracting information at this kind of industrial scale. The main breakthrough in a year
*  and a half that's got everyone very excited is what's called sparse autoencoders. Essentially,
*  the transition here has been from going from sort of very microscopic, like a biologist looking down
*  a microscope and seeing something and writing it down, or Ramon y Cahalé, the first neuroscientist,
*  looking at these neurons and drawing individual pictures and being like, oh, this is a kind of
*  neuron, and that's kind of neuron, to being able to essentially like sequence en masse. We've gone
*  from individual artisanal understanding to some level of understanding at sort of industrial scale.
*  But this step change is built on the accumulation of knowledge that's been built up over the past
*  five years or so. It's also probably worth saying a little bit about the name interpretability and
*  the sort of broader history there that has become really popular in the last year or so,
*  is often referred to also as like mechanistic interpretability. And the reason that it's called
*  mechanistic interpretability is to distinguish it from all other interpretability. But it's like a
*  positive naming about being able to understand the internal mechanisms of a model and go layer by
*  layer, piece by piece, and understand the internals, as opposed to other sort of types
*  of interpretability, say using saliency maps, which are about input output relationships, or
*  things like LIME, which are about constructing entirely new surrogate models. So mechanistic
*  interpretability is distinguished by being all about the internals of the model you actually have.
*  You've got LIME 3 in front of you, say, what is it actually doing? Not like how can we construct
*  a simpler explanation of what it might be doing? I would be interested in a little bit more
*  of how you tell the story for yourself of what were the key milestones or the big insights or
*  sort of the major techniques that have most captured your attention or you think have proven
*  the most fruitful over the last couple of years? How would you describe like what have been the
*  sort of key insights or key contributions that have ramped us up to where we are today?
*  The thread to pull on it here is, first of all, is there anything there? Are these models just
*  some sort of like magical trash? They somehow produce these extremely accurate outputs and
*  there's just like nothing meaningful going on inside. And I don't think this is really
*  a coherent viewpoint, but it was a kind of popular one. And I think the first thing was just evidence
*  that representations, they're somewhat disentangled, semantically meaningful representations
*  inside models, and we didn't put them there. Good representations emerge as a result of
*  training on somewhat general tasks. It's kind of reared its head a lot throughout machine learning
*  history and a lot of quite prominent people have endorsed this, but it doesn't seem to have been
*  totally accepted. So actually, like, fun fact, the ICML test time paper this year went to
*  a paper called DCAF, which they realized that pre-training on one task generates a few features
*  that help you to do a whole load of other tasks. And the first thing that got me into AI was seeing
*  Jeff Hinton's thought vectors talk. This thing, I think it's Mikhailov et al. And they have these
*  sort of linear analogies and embedding space. What is it? It's like going from king to queen gets you
*  like a man to woman vector, and you can apply this in other senses. So there's something of recognition
*  that there was content inside models, but I don't think it was universally recognized.
*  And this evidence just gradually built up over a while. Andrej Karpathy had a blog post
*  on training RNNs and visualizing what they were doing. And there are a bunch of this neuron does
*  this and that neuron does that. It quite quickly became clear that most of the time a single neuron
*  was not doing anything meaningful. So you might think maybe it's a sort of distributed code, but
*  then you don't really have any good angles of attack on this. Just saying it's a distributed
*  code doesn't actually help you to find the distributed code and then you just left unable
*  to decode things. So we were essentially left somewhat stuck with that for a while. And then
*  one of the key clues was this notion of polysemanticity. This was a thread that
*  Chris Ola has been pulling on for a long time and really, I think his persistence
*  working on this is one of the things that got the feel to where it is today. And recognizing that
*  neurons are sort of polysemantic. So what this means is that a single neuron might fire on
*  one or two or three unrelated concepts. So you might have a visual neuron for say the wheels of
*  cars and cat ears, and it will respond to both of these, but it won't respond to everything.
*  And this tends to suggest that your code is distributed, but it's not super distributed.
*  It's not like impossible. So neuron fired on literally everything and there was no pattern,
*  you might think it's hopeless. But the fact that it's firing on two, three, four things
*  suggests there's a manageable level of structure there. And then again, Chris Ola's group
*  stands in the public, we have a lot of credit goes there. They worked on understanding what
*  polysemanticity is, what superposition is. And eventually that led to essentially just having
*  the courage to try a really big MLP. I think that's maybe the story here is they plugged up
*  the courage to just have a really wide MLP and call it a sparse autoencoder and it just worked.
*  So that was the sort of the breakthrough that I think got a lot of the attention,
*  but it's really built on having understood superposition and having understood polysemanticity,
*  at least to some level. Just to add on to a little bit of that from someone who's coming
*  from the outside and caught up with mechanistic interpretability research recently. I think what
*  Tom is pointing out about, of course, there's something happening inside the model. Once you
*  see that, it's quite obviously correct. But I think like a lot of people prior to engaging with
*  the mechanistic interpretability research, I was walking around assuming that these systems
*  internally must be so complex that there's no way that we could understand them. But that actually
*  goes at odds with a lot of other ideas about how they should be learning things in the first place.
*  One metaphor I've found very useful in my own intellectual development here in catching up is
*  thinking about learning systems as compression systems and this balance between generality
*  and over complexity in the system that is always happening inside of these models.
*  And it makes extremely intuitive sense that if a model is balancing between generality and
*  complexity and it wants to be less complex because of regularization, but it also wants to be as
*  general as possible so it can get the loss as low as possible, that what it's going to learn in the
*  process of doing that are representations, are hierarchical structures that explain the patterns
*  of the data. And if you believe that's happening, which I think most people in machine learning do
*  believe that's happening at this point, then it would be more surprising if we weren't able to
*  somehow get insight into the structure that was learned by these models than otherwise.
*  And that was an important update for me to have, but once I had it, I couldn't look back. It just
*  became so clear to me that we are on the right track and we're going to be able to disentangle
*  what these models are doing inside. Hey, we'll continue our interview in a moment after a word
*  from our sponsors. AI might be the most important new computer technology ever. It's storming every
*  industry and literally billions of dollars are being invested. So buckle up. The problem is that
*  AI needs a lot of speed and processing power. So how do you compete without costs spiraling out
*  of control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure
*  or OCI. OCI is a single platform for your infrastructure, database, application development
*  and AI needs. OCI has four to eight times the bandwidth of other clouds, offers one consistent
*  price instead of variable regional pricing. And of course, nobody does data better than Oracle.
*  So now you can train your AI models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, 8x8 and Databricks Mosaic,
*  take a free test drive of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive,
*  oracle.com slash cognitive. This episode of the Cognitive Revolution is sponsored by the Brave
*  search API. You may know of Brave as an alternative to Chrome, but did you know that Brave has its own
*  independent search engine powered by its own 20 billion page index of the web? The Brave search
*  API gives developers reliable and affordable access to programmable web search, auto suggest,
*  spell check and more with flexible plans for all types of use cases from rag search to automated
*  business intelligence. On top of that, it's up to three times cheaper than Bing, all without
*  compromising on quality, speed or reliability. Over 700 businesses, including Coheer, Chegg and
*  Kagi rely on the Brave search API. And a recent survey showed that 94% of customers would
*  recommend it to their peers. To start building apps with the power of the web, sign up at brave.com
*  slash API and get up to 5,000 free monthly calls. So maybe just to restate a couple of the key ideas
*  that I heard there and tell me if I'm missing anything important or getting anything wrong,
*  we hear often, I think maybe a misinterpretation of this fact or at least half of the fact that
*  the models are trained to predict the next token, right? They're trained one token at a time. They're
*  evaluated. They're back propagated. All of this is happening on this sort of next token prediction
*  objective. And so it's tempting to say they're just next token predictors. There's not really
*  anything sophisticated going on there. This is where we get like the stochastic parrot intuition.
*  And I'm not entirely clear. I've heard this story from the OpenAI folks a couple of times where I
*  think it was going all the way back to 2017. They had a Amazon review completer predictor where they
*  found a neuron that turned out to be a state of the art sentiment classifier that had emerged.
*  And of course, this word emerge and the concept of emergence is also like fairly controversial,
*  but this thing popped up, right? Even though they're just training it to predict the next,
*  I think in that case, it was one letter at a time. Somehow as a means to do that,
*  the network developed a single spot that would, if evaluated as a sentiment classifier, would have
*  been a state of the art sentiment classifier at the time. So that's a really remarkable phenomenon
*  that there are these sort of intermediate and more conceptually rich things popping up in the
*  middle, all as a means to this next token prediction, which could maybe get decent at
*  by just pure correlation or pure stochastic statistics. But that's not in fact how it is
*  working. And it seems like we've at least had pretty good clues about that since 2017.
*  Now, one thing I don't really know is somebody might think, yeah, when we were in the sort of GPT
*  one, GPT two era, maybe those things were small enough that richer representations didn't
*  necessarily emerge in those. And so the stochastic paradigm was maybe correct for earlier models.
*  And it was only with bigger scale that these richer representations started to emerge.
*  My best sense right now is that's probably not right. And that maybe instead of what we were
*  seeing was a move from the like simple thing where you could see the sentiment classifier neuron to
*  a bigger thing where everything got poly semantic and messy, and we just had no tools
*  to figure it out. But presumably they were still there to a meaningful degree. And so over time,
*  we had to catch up with what the models were probably doing all along. Is that how you would
*  understand it as well? Yeah, I think that's about right. People do a lot of interpretability
*  research on GPT two small and they find surprisingly rich things in there. So they were there all along.
*  But we never had the courage to go and look for them until we were like forced to by seeing the
*  results on bigger models. Okay, fine. There's no choice. We have to accept that there's stuff in
*  there. Let's go and actually understand it. There is a meaningful dynamic of like superposition
*  changing across scales and across the density of information in the input. I don't think this is
*  very well understood, even in sort of toy models. But there's definitely there are definitely
*  interesting things inside. Can you give us a little bit more on the importance of regularization
*  and just conceptually what is going on there? I think about this a lot in terms of the grokking
*  results, but there is this sort of single objective that the overall system is being
*  trained and modified based on. But then there are these kind of like competing tensions of
*  needing to be simpler, but needing to encode tons of stuff. Give us a little bit more intuition for
*  how we should understand those competing forces within the training dynamic.
*  So my understanding of the grokking work is that to get grokking in a sort of classic,
*  you do modular addition. I think it is certainly some modular arithmetic operation. To get grokking
*  to emerge in any like reasonable time scale, you need quite heavy weight decay. It's not clear to
*  me whether that's an artifact of sort of artificialness of the task, because the models
*  over parameterized for that task far more than a language model is over parameterized for
*  a task of predicting the next token for like general text. So it might be that the weight
*  decay here is acting as an explicit regularizer to try and stand in for this kind of implicit
*  regularization of just not having enough parameters to do as good a job as you'd like.
*  Now, like I've just said the word implicit regularize, no one really knows what those are.
*  It's just a thing that we say so we can sleep well at night. So the idea there is we want to
*  make sure basically that the weights are carrying their weight, if you will. We don't want to have
*  a bunch of random stuff that kind of was very contingent on like early data or just popped up
*  for random reasons. And so regularization or weight decay, those are synonyms basically,
*  right? You can maybe clarify that. I can't have other types of regularization.
*  I just sort of narrow interpretation of weight decay would be that it's the L2
*  norm of the parameters. Now you can have the L1 norm just as a very simple example,
*  but there are lots of more complicated regularization schemes. Yeah, I think the
*  main thing to get at here is what is regularization trying to do? Regularization is trying to
*  prevent you from memorization. And there are a couple of things about modern foundation model
*  training that make memorization substantially harder. And one of those, probably the most
*  important is that you only see the data once, assuming that deduplication has been done well
*  and the people who are constructing the data corpus have done a really solid job. You don't
*  see the same data point multiple times. You're certainly not taking the whole data set and
*  running multiple E-box through it unless you're like in a real pickle. Generally, that's worse than
*  just showing the data once. And so the model doesn't really have very many opportunities
*  to memorize there. Intuitively, the structures that the model learns that will do well in this
*  setting are the ones that can be reused. So these are like the features that will generalize.
*  Features that involve just memorizing a data point that you've just seen are just not very useful.
*  So this is capacity that the model could be using for something else.
*  So essentially, the model has some sort of amount of capacity and the task is so demanding that it
*  can't spare any capacity. And so if memorization is not useful, then it will get replaced by circuits
*  which are useful. But in grokking, you generally see with a group of not very large size, there
*  are only so many data points, you have to run through the data set loads and loads of times to
*  get the model to change and loads and loads of times to get it to grok. So you need some very
*  heavyweight decay in order to prevent that memorization. So that probably I think reconciles
*  those two positions. And so for audience members who might be coming from more of a data science
*  background, there's the intuition here, although statistical learning theory has failed to accurately
*  predict some things like grokking, the overall intuition for the balance between the number of
*  memorization and generality can be understood in terms of the classic bias variance trade off,
*  where you could have a really huge model with tons of parameters. And if you're trying to get
*  that loss to go to zero, if you had an infinite model, the fastest way to do it would be to just
*  memorize the data set. But we don't want that because if we memorize the data set, we haven't
*  built anything useful that we can actually use on any sort of novel data that it hasn't seen before.
*  And that's the complexity is that in theory, I could just have over parameterize and just fit
*  the data. But balancing that complexity with generality is how we actually build things that
*  are useful. And so in statistical learning theory in the past, the wisdom was like you did this by
*  under parameterizing the model. And that's maybe true to some extent, but I think grokking and
*  double descent like cast doubt on that. And there's a lot of theoretical work that people
*  are trying to do to figure out like, why that some of those intuitions were wrong.
*  That's really profound. I have like a narrow question, but you could maybe unpack it with like
*  a broader answer. So I just went on this trip. And in planning the trip, I asked Claude 3.5 Sonnet
*  where I should go in Brazil, and it recommended a city to me and that I was like, okay, what should
*  I do there? And it even recommended to me the specific river cruise operator that I ended up
*  going with by name and giving me like a description of what the value prop is for this random. It's a
*  one boat company. So it's like, this is really long tail stuff. And I feel like I have a hard
*  time a little bit like the toy examples of grokking are fascinating to study. But how do you think
*  about the overall at scale this balance between having like, seemingly memorize almost all
*  Wikipedia, but also trying to avoid this, you know, memorization to create generality in some ways,
*  the more I think about it, the more I realize my intuitions are not necessarily up to the challenge.
*  So I think there are really two questions there. One is, what is the kind of gross anatomy of a
*  model? What are the pieces when they're operating? What do they actually do? And the other is how do
*  they come to do it? And one answer to the second question might be they can essentially memorize
*  facts very rapidly. There's a nice paper that came out recently by a researcher called Ho-Yon Chang
*  on what happens when you inject a kind of fake fact into language model training. What he was
*  studying is that you make up a fact, and you insert it into the model's training data, and you
*  see what happens over time. Immediately, the model learns the fact to some degree. And then it forgets
*  it over a while, there's a kind of forgetting curve. And if you show the model the same fact a few
*  times, it will start to remember it really well. But the thing is, you don't need to show it very
*  many times. And this is widely believed, like you show a large language model something once or twice,
*  and it's memorized a whole load of the facts in it. Now, how does it do that without just literally
*  having memorized the text verbatim? I don't think anyone can tell you the answer to that question
*  right now. Hopefully in a year or two, we can start to understand it. This kind of understanding
*  what's happening during the training process is one of the sort of frontiers for interpretability.
*  There's a kind of static question of how does a model do it right now? And then it's like,
*  how did it come to be a model that could do that? So to come to that first question,
*  this is again, largely intuition, there's some parts are better fleshed out than others. But
*  people who've worked with interpretability and these models for a while get this sense that
*  essentially, a lot of the time, there's the detokenizing step takes up the first couple
*  of layers. So this is the tokenizer will split say someone's name to give a really easy example.
*  Like the name Michael Jordan would have been split up into the two tokens, Michael and Jordan.
*  And it wants to create a sort of super token of Michael Jordan, which contains all the facts,
*  which are literally only attributable to Michael Jordan, and not just to like the word Michael or
*  the word Jordan. So then there's like a sort of lookup stage where early mid layer MLPs retrieve
*  all sorts of facts about this guy, Michael Jordan, and put them all into the residual stream.
*  And the reason they do this is that if you think about the structure of attention,
*  attention can only look back in tokens, it pulls to the current token position from earlier
*  token positions, you can't like deliberately selectively recall facts and push them forward.
*  So essentially, when it's getting Michael Jordan is like taking every fact that could conceivably
*  be useful on any sentence about Michael Jordan, just pushing it into the residual stream.
*  And then at some point, it turns out that the sentence ended up being like plays the sport of
*  and you can pull out Oh, plays the sport of I need to play token, like feature from the residual
*  stream. So there's the retrieving facts, MLPs, and they pull these out to the fire attention.
*  And then there's a sort of calibration bit at the end where the model is like, Oh, yeah,
*  I've got all these options. I like that one. I don't really like that one. Let's go with basketball.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki
*  so much that I invested in it. And I recommend you use it to use cog rev to get a 10% discount.
*  Hey, Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex Fang senior
*  software engineer as much as the next guy. But honestly, I can't afford them anymore. Founders
*  everywhere are trying to turn to global talent, but boy is it a hassle to do at scale from
*  sourcing to interviewing to on the ground operations and management. That's why I teamed up with Sean
*  Lanahan, who's been building engineering teams in Vietnam at a very high level for over five years
*  to help you access global engineering without the headache. Squad Sean's new company takes care of
*  sourcing legal compliance and local HR for global talent. So you don't have to with teams across
*  Asia and South America. We can cover you no matter which time zone you operate in. There are engineers
*  follow your process and use your tools. They work with react next JS or your favorite front end
*  frameworks. And on the back end, they're experts at node Python, Java, and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on upwork that's doing two
*  hours of work per week, but billing you for 40. But you'll get premium quality at a fraction of
*  the typical cost. Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squad.com and mention turpentine
*  to skip the waitlist. Let's lay that over the general like schematic diagram of the
*  transformer as well. If I can speak on behalf of the audience, I'll say people probably have a
*  sense that first thing that happens is text gets converted into numbers. That's the embedding
*  process. Okay, cool. Then we've got all these different layers. The layers consist of an
*  attention portion and an MLP portion. General stylized points would be like the attention
*  portion figures out the relationship between tokens. And then the MLP portion has the facts
*  or the knowledge. And by all means, feel free to complicate this. And then this gets run over and
*  over again. My narrative is as we go through the layers, we're gradually working up toward
*  higher order ideas. And it's from just a bunch of different research papers, it seems like two
*  thirds, three quarters, 80% of the way through the layers is when we have the highest concept
*  representations. And then at the end, there's this collapsing back down to actually picking
*  what the next token is going to be. And then obviously, we like run that run over again,
*  put, you know, put more detail on that or tell me if you think I'm getting anything wrong.
*  No, I think that's broadly the sketch as people understand it. Like it's an incredibly low
*  resolution sketch. With our current stage of knowledge, it will get filled out like we filled
*  out our knowledge of human and animal anatomy over the next few years. But that's the picture that
*  we're all working from at the moment. And there's lots of sources of evidence for this. The first
*  one is this sort of logit lens or tuned lens thing where I think there's a guy called Nostalgia
*  Brist like first came up with this logit lens idea and some researchers, it might be Nora
*  Bell-Rosen, Stella Biden from Eleuther, developed it. And the idea of the logit lens is pretend,
*  you're at layer 10 saying just pretend that this is the final layer. So you take the sort of language
*  modeling head, the bit that does the layer norm, and then the projection to the token logits,
*  you just cut off the model there and apply the language modeling head. And this will give you
*  some predictions and you just keep working this, you do it at layer one, two, three, four, and so
*  on until you're actually running the whole model. And so this is essentially saying if the model
*  were to stop its processing here, what would it do? And you see exactly this pattern of building
*  up from initially it's nonsense. It bears absolutely no resemblance to the next tokens,
*  but then gradually it starts to converge on the right thing. It's not like the model is
*  in some totally different subspace. And then all of a sudden in the last layer, it's like,
*  oh, okay, here we are. I've arrived at the answer. The other is causal tracing. I think you alluded
*  to this a little while ago with David Bowers group. So causal tracing is an incredibly elegant idea.
*  You're essentially looking for the single point of success within the model. So which bit of the
*  model do I have to, I can break the whole model and if I restore this one bit, it will work.
*  And causal tracing is it often isolates MLPs as being absolutely essential to these kind of
*  factual recall questions. And it isolates them generally to like approximately one third through.
*  So that's where we get this picture of early MLPs are doing factual recall from.
*  **Jade Lienkamp** One thing to expand on the question of the picture of how sort of ideas
*  become higher order until maybe the late middle of the model, and then they start becoming more
*  language focused again in order to be able to de-embed and get the output,
*  is that when we've trained our SAEs and we've started looking at them,
*  trained SAEs on the residual stream, one of the challenges when trying to build
*  intuitive interfaces that let people traverse these is that from a human oriented perspective,
*  a lot of what you find looks like mixed levels of abstraction. As people have this kind of like
*  notion that like, I don't know, things like society or super complex organizational structures
*  what we might intuitively expect to find in those late middle layers, and you do find some of that,
*  but then you also find specific nouns, you'll find grammatical features, you'll find all of
*  these things interleaving with each other. And one really interesting thing is consistently been that
*  to understand the language model, you have to understand it on its terms. It doesn't mean it's
*  not understandable, but it just means that your intuitions, your preconceived notions about how
*  information should be hierarchically structured are probably incorrect relative to how the language
*  model is actually processing that information. But it's also a really cool experience to then
*  deprogram yourself a little bit and think about why you might be observing the things you're
*  observing. Yeah, this is one of the things that's really exciting about looking inside models. It's
*  like they don't always operate on your terms. It's got some slightly different ontology,
*  it's got some different way of doing the processing, it still works. There's something
*  in there to see, and it's really fun to try and meet it on its terms. I often, even for introductory
*  audiences, and even just for intuition building for what CHI GPT can do for you, I often find it
*  really useful to tell people that they should be thinking of this as alien intelligence, and
*  they should know that even though it's like human level on many overall benchmarks or can perform
*  in a human-like way in many respects, under the hood, it is not in fact human. And that's like
*  deeply mechanistically true, and then also even on a behavioral basis, it could be like to have
*  very strange strengths and weaknesses. So I think that's definitely true. I want to take a brief
*  diatribe on universality, because there's a fundamental question here of is the way these
*  systems learn really different than the way we learn. I studied neuroscience before I became an
*  engineer working at startups, and so I'm really motivated by this particular question. And I think
*  it's definitely the case that LLMs are clearly not all there is to human learning and human
*  intelligence. They're not approximating all of it. But there are a lot of key similarities
*  that are interesting. There's this concept of universality, and what the observation of universality
*  is that when you train neural networks on similar data distributions, they learn similar
*  representations. And there's a lot of evidence for this in vision models. And interestingly,
*  the representations that are learned in vision models, the hierarchical assembly of features
*  in vision models over the course of successive layers, looks a lot like what we know about the
*  visual cortex in the human brain, which is one of the most well-understood parts of the human brain.
*  There's a recent paper that was in Nature called Semantic Encoding During Language
*  Comprehension at a Single Cell Resolution by Jamali et al., which was really interesting.
*  And what they did is they looked at individual neurons, and they found something that kind of
*  resembled polysemiticity, and they found this hierarchical assembly of information.
*  They compare it in the paper to embedding models and some of the things that you find in embedding
*  models. And the reason that this is relevant to the previous point that we were making about it
*  being an alien intelligence, I think that one way to interpret this is that there are similarities
*  in how we learn and how AI systems learn, but we might understand ourselves quite poorly.
*  And so what feels intuitive to us from our perspective about how information we think
*  should be organized might not actually be how our brain itself organizes information. In fact,
*  if the brain was intuitive, we'd probably understand it already. So I think that there's this interesting
*  point here of one of the things about interpretability that personally excites me the most is that we're in
*  the early days of this. Maybe I'll have egg on my face for saying this later, but I'm increasingly
*  convinced at the point of view that we are learning something pretty important about how we learn in
*  the process of studying how these models learn. Yeah, it seems like we're maybe climbing the same
*  hill from different faces, because this is a quite striking finding. And I'd say it's still pretty
*  suggestive, but increasingly compelling. The universality idea, as I understand it, is basically
*  that the bigger models get, the more numerically similar their internal representations seem to be.
*  In other words, they seem to be converging on some sort of apparent world model. And the
*  differences in them when we're looking at smaller scales then can maybe be understood to be sort of
*  contingent downstream of different data sets, different initializations. But we imagine that
*  in the fullness of time with all the data, all the training, that all these things are converging.
*  Tom can definitely speak better to the universality question in the context of AI models. But in the
*  context of the human brain, the human brain has an implicit regularization term. We have a strong
*  incentive to spend as little energy as possible. And maintaining connections in our brain is
*  spending energy. So because of this desire to operate extremely efficiently in our brain,
*  which is imposed by our environment, there's an implicit desire to maintain as few connections as
*  possible in order to meaningfully express the ideas that are useful for us to be able to survive in
*  our environment. Obviously, biological neurons and artificial neurons have tons of disanalogies. I
*  think it's really important to always clarify that. And it's always important when you're
*  talking about models internal processes to put things like thinking and thoughts and air quotes.
*  That being said, I think there are definitely parallels in which you can think about these
*  things as you have systems which are responsible for representing very complex, sparse distributions
*  of data with these implicit or explicit regularization terms, which apply penalties for
*  maintaining connections that aren't truly necessary to be able to effectively model that
*  distribution. I think Dan has pretty much nailed it. I don't have a huge amount to add there apart
*  from that statisticians listening to this, I guess they'll laugh with a weird way of finally coming
*  around to this. But when we're learning machine learning models, at least when we're learning
*  generative models, we're really just learning a model of the data set. And the data set has
*  structure. And if the model does a sufficiently good job, then that structure will be represented
*  inside the model. And every model that's trained on that data set will end up with that same
*  structure to some extent. Now, obviously, we have very different regularizations between humans and
*  models, and very different learning environments and that sort of thing. But we take human text,
*  we push it into language models, so they're receiving some similar things. But even when
*  that's not happening, like this is one of the things that motivated the work I did on chess,
*  was that there we were looking at AlphaZero, so it's never seen human data. Like, there are
*  just things about chess that you have to know if you're going to play chess. If you're going to
*  play chess and you don't know what a pin is, you're going to have a really bad time playing chess.
*  There's all this sort of stuff which is just inherent in the world and inherent in the data
*  that is just going to inevitably impress its shape on the representations of models and make them
*  converge to the same sort of thing. Okay, cool. So maybe just to go back
*  a second to the architecture and different ways of trying to open up the black box.
*  It seems a lot of early work was done on attention maps to just try to figure out what tokens are
*  relating to what other tokens. I guess that was a relatively easy place to start because it's pretty
*  much you can just read off the strength of relationships between tokens. And you can see
*  that, oh yeah, it makes sense that this token is related to this previous token because there's
*  a conceptual link. How did that come exactly to exist is another tough question, but we can see
*  that they exist and they make intuitive sense. You also see relatively intuitive things like
*  there's always a look back at just the last few tokens because that is necessary to locate you
*  where exactly are you right now in this sentence and therefore what exact token would come next.
*  You have to be aware of the immediately local context as well as some of these more distant
*  historical context determiners. Then there's this sort of MLP thing where it seems to be a lot of
*  patching. Like we can zero out a portion or we can like set it to random or we can run one forward
*  pass and grab the way something is represented in one forward pass and move it over to another and
*  see how surgically rearranging these things affects outputs. And then there's the between the layers
*  and this is where you guys are choosing to focus. We have this sort of bottleneck where there's a
*  lot of numbers going on in an attention head. There's a lot of calculations happening in an
*  MLP layer and then they get condensed down to the dimension of the model. So it's still quite a few
*  numbers, but it's like way less than was floating around within a given layer. And these sort of
*  activations between layers, this is where you guys are studying with the Sparse autoencoders.
*  So I'd love to get a little bit more intuition for like how you think of these different things
*  relating to each other and why the focus seems to have moved to this activations layer.
*  The way that I've come to think of the residual stream is I've come to think of it,
*  I'm coming from a programmer's perspective. It's like the RAM of the model. There are all of these
*  variable positions essentially that the model can write to. The job of every intermediate layer
*  is to compute a linear transformation on the residual stream. And so one way to visualize that
*  is that each layer executes some code in this metaphor and that code goes and updates some
*  global variables that the model can then access later in downstream functions. And so the reason
*  that this is really interesting to look at is because you're getting a sense for overall how
*  the model operates. You're not learning that much information about the individual functions,
*  but you're learning a lot about how the model is computing by understanding what are the variables
*  it's setting to and when is it setting to those variables. The other reason that it's interesting
*  is the easiest way to intervene on the model is to just change the value of the variable.
*  If you're trying to debug some code that you've never seen before, one of the first things you
*  would try would say all the codes are written in an alien language and you know what's a variable
*  and what isn't a variable. You try, let's flip this bit up, see what happens. And so intervening
*  on the residual stream is really useful to this end to help us understand at a much higher level
*  what does this model think is important, things in air quotes, is important in order to be able
*  to execute its computation. Yeah, I think it's a really nice metaphor. The sort of bit that I'd add
*  to it is that because you have a residual stream for every token position, it's like a multi-threaded
*  program. A thread is going at every token and the ultimate aim with that thread is to use the
*  information in all preceding threads to predict what the next token is going to be. And the
*  tension is like information sharing and MLPs are like within thread processing. A typical model
*  these days at scale, and you guys are doing your work right now on the llama family of models,
*  right? Is it 8,000 numbers that constitute the activations between the layers? Yes, in a transformer
*  there's a few numbers to know. There's D model, which is the dimensionality of the residual stream.
*  The attention is literally adding a vector as its output into that stream. The MLP is again literally
*  adding a vector into that. And that for llama 3.8b is 4096. And for 405b it's 16384. So I guess it's
*  8192 for 7db. I don't know, don't help me to that. It seems to be the logical choice. And the reason
*  that this is growing slower than the size of the model is that roughly as you increase the
*  dimensionality of the model, if you can have a matrix that takes that in and goes to some other
*  similar dimensionality, that's going to go up quadratically in size. The key number to say how
*  big is a transformer is D model. And then attention is a little bit complex, but every head has a much
*  smaller dimensionality, but there are many of them. And then the MLP is conventionally four times as
*  wide as D model. So you get this huge expansion into the MLP and it squashes down into multiple
*  separate attention heads, but they're all scaled linearly by D model. This starts to give an
*  intuition, if folks don't already have one, for what polysemiticity is and why it's necessary,
*  right? Because it's a striking observation that everything that's happening, all of this
*  information, all of the relationships, all the facts that have been retrieved, all of the
*  connotations or associations or whatever, at every layer, this all has to be packed into,
*  in the case of LAMA 8B, 4,000 numbers. And in the case of the 405B, 16,000 numbers. Now, these
*  numbers can have quite a few decimal places, but if I understand correctly, these days we're also
*  finding that they can be not that many decimal places, right? In the early days, you might even
*  have had 64 digit numbers. We've seen that shrink down to the point now where there's not too many
*  significant digits used. This is quantization and it seems to, obviously it saves a lot of memory
*  if you can use smaller numbers. Tell me if I'm wrong about that. I guess the weights are being
*  quantized, right? Are those representations or are those sort of activations also being quantized
*  in the same way? I guess I don't actually know that. It's a little complex, but yeah, basically
*  that's if your parameters are in date, then when you do the forward pass, your activations will
*  typically be in date as well. It gets more complicated during training where you might have
*  to upscale some numbers because you get underflows and overflows, but that's basically the way I
*  picture. If you have an 8-bit float or an 8-bit, there are only so many values it can take and you
*  can either keep the range the same and make the values spaced out, or you can shrink the range
*  and keep it kind of distinct. That's the difference between B-flow 16 and float 16, random fact.
*  Basically, those come down to a finite number of discrete states, right? Because if you have an
*  8-bit number, you obviously only have so many forms that can take. Then to create a high dynamic
*  range as opposed to just having two to the eight integers, there's a significant digits part and
*  then an exponential part. This is all quite weird. I guess the big thing is this is, again,
*  you only have 4,000 or 8,000 or 16,000 numbers and each of those only has so many finite states
*  that it can take. That's all you've got to fit everything into. Everything has to flow
*  through that between these layers that are doing all the computations. With that in mind, it's
*  obvious that information is really going to have to be packed in there and you're going to have to
*  get really creative for how you're going to pack things in. There's obviously way more than 4,000
*  or 16,000 concepts in the world. Maybe there's a few concepts that are so important that they would
*  get their own number in a dedicated way. Maybe that's even what was happening if we go back to
*  I think the 2017 sentiment classifier neuron that OpenAI observed. I don't know this for a fact,
*  but just to tell a stylized story, you could say, geez, to predict the next token in an Amazon
*  review, the sentiment of the review is just such an important thing to track that it turns out
*  that the optimal way for the model to do this is to have one of those numbers just to be totally
*  dedicated to sentiment, arguably makes sense. I don't know if there's anything that rises to that
*  level, the Lama 3 series model, but most of the time, we're not going to be able to dedicate
*  one of those numbers to a specific concept. Instead, we have to have much more complicated
*  representations. This is where the sparseness of the dataset comes in as well. We have such a
*  huge world, but for any given input, we are typically only seeing a few features of that
*  world. We could be talking about sports, or we could be talking about science, or we could be
*  talking about history, and obviously lots more things besides, and these are all different
*  things, the concepts of which minimally overlap. The polysemiticity arises because we need to
*  pack these orders of magnitude, greater number of concepts into this very small space of numbers.
*  The only way to do that is to start to reuse these individual positions
*  in all sorts of different ways. I don't know if you have a good story for how to think about the
*  gradual complexification of the geometry. I think the original, I forget the name of the original
*  from two years ago. Was that Toy Models of Superposition? Yeah, is that the one from
*  Ola and the Gang like two years ago? Yeah, they had some really interesting, and even there,
*  you get the sense that it's just scratching the surface of how complicated this can be, but they
*  show that depending on the frequency with which concepts come up, you'll see either this dedicated
*  channel for concepts if it happens often enough, or if it doesn't happen so often, then they start
*  to get reused in these geometrically interesting ways. So yeah, I'm trying to catch up. It helped
*  me move forward from there. Yeah, you basically hit the nail right on the head there. I don't
*  think our actual understanding of this has advanced that much since the Toy Models of
*  Superposition paper. I think better toy models and slightly less toy, studying this sort of thing
*  more would I think pay off a whole lot. I think that would be really great and that's something
*  I'd be very excited to see more people doing. But the pictures you've outlined, it seems basically
*  intuitively correct. There's a few pressures that are putting structure into the representational
*  space. And one of these is essentially like if a concept is really important, you want it to have
*  a neuron. And perhaps as with everything, physicists in the 90s got there first. And there's some
*  additional studies on this. There's a lovely book called Theory of Neural Information Processing
*  Systems, which is not from the 90s, but brings a lot of work from that period. And they've got
*  some like theoretical arguments that underpin this and also kind of go further. And there's noise,
*  maybe you want two neurons that can kind of mutually support one another. So when things are important,
*  you want to dedicate neurons to them. And you don't want any interference because they matter
*  so much. But then you've got everything else, which is not so important. And then there's the pressure
*  to smush it all in there. And the way that you can do this is by making things like not actually
*  orthogonal to one another, which is the sort of implication if you have 4096 directions,
*  and you want everything, every concept to be orthogonal, you've got maximum 4096
*  concepts, assuming that you don't put them into little islands. And so if this neuron is like
*  five, it means something. And if it's 10, it means something else, say. So in high dimensions,
*  it's very easy to have almost orthogonal vectors. And if you know that these vectors are going to be
*  included quite sparsely, there are algorithms that can recover them quite well as well.
*  So this is the field of sparse coding, which some mathematicians understand a great deal. I don't
*  understand terribly well. I don't think there's a huge amount of expertise in the field at the moment.
*  But I'm sure there will be in the near future because it seems so central to what we're doing.
*  One other data point on that question too about when does superposition happen is that it's closely
*  related to compression. And the level of compression that you can get away with is related, as Thomas
*  is saying, to the frequency in the data. So if something's super important to reconstructing
*  the data, maybe it gets its own neuron. But then you can also imagine compressing things further
*  and further such that the more neurons concepts share with each other, the more sparse they will
*  need to be in the data set to be able to be independently recoverable. And Anthropic showed
*  in scaling monosomaticity that there is a relationship between the degree of the
*  polysemanticity of the neurons representing a feature and the frequency of that feature
*  in the training data set. The other factor here we haven't mentioned is structure. So when concepts
*  are related to one another in the data distribution, then it can often be very efficient to
*  relate them to one another in the latent space. So an example here is compositional code where
*  if you have an object that's described by several attributes, then you might code each of these
*  attributes separately. And that can be quite an efficient code as opposed to independently
*  coding for every single combination as like a separate highly distributed code. There's a
*  really nice paper on categorical and hierarchical concepts by Kehoe Park that won the best paper
*  prize at the Mechanistic Contemptibility Workshop that sort of goes into the consequences of
*  structure in the data distribution for structure in the latent space. And so like not only are you
*  trying to squash them into the latent space as much as you can, but you also want to respect
*  this structure. So there's really three forces going on here. There's like importance, there's
*  just squash everything as much as you can in this structure.
*  So is it a fair description or seem like a right intuition to say that a lot of the weirdness that
*  we observe in language models today maybe comes from the fact that certain things are not orthogonal
*  and that's okay most of the time because they don't appear together most of the time and so
*  you can get away with it. But maybe in some of these weird situations where we're like,
*  why is it doing that seems insane? Maybe what we're stumbling on is that we're bringing things
*  together that maybe aren't usually together and that they're colliding in weird ways and sending
*  the model off into a weird state that it just wasn't really prepared to handle.
*  It could be. I'm going to keep saying this, unfortunately. Nobody knows. To the extent they
*  do know, they don't know that much. But maybe this is what's happening with adversarial,
*  with at least some kinds of adversarial optimized prompts is they're actually like bringing a bunch
*  of, they look like garbage to us because they're bringing a bunch of concepts together that don't
*  fit together, but they fit together in a way that sort of, I don't know, just hits the right spot in
*  the models latent space that it causes the right kind of interference. I don't know. It's not an
*  unanswerable question. It's just that no one has answered it yet.
*  So then, okay, that's a good motivation for the Sparse Auto Encoder work. So this is basically,
*  I'll let you describe it, but this is the big picture trying to figure out how do we tease
*  apart the potentially many concepts that are represented in these relatively few numbers
*  together at the same time. How do we pull those apart and figure out is actually here? And then
*  obviously there's big hopes and dreams for what that might unlock as well.
*  I think the first thing to do here is just to demystify things a little bit.
*  Sparse Auto Encoders, they were big in like 2010, but they're big again for a new reason.
*  What is a Sparse Auto Encoder? It's a fancy MLP. Basically, it's an MLP, which is really wide
*  and has some sort of sparsity promoting regularization term. That's it. There's
*  not a great deal more to say, at least with the state of the art at the moment. People have all
*  sorts of funny activation functions, but that's basically it. You have a big MLP and you try and
*  make it as sparse as possible and as broad as your GPU can fit. And if you remember what we were just
*  saying just now, like these intuitively changes the balance between these two forces of if it's
*  important, give it its own neuron, but we don't have that much space. What you've done is you've
*  really taken the pressure off, you've given the model room to breathe. And now there's much more
*  space. More things can get their own neurons. And also the sparsity term will lead you to drop a
*  whole load of things on the floor. So there's even more space. That's basically the kind of big
*  picture of what they're doing architecturally, but like why has everyone got so excited about them?
*  There's a bunch of reasons. One is that they seem to work actually way better than it was reasonable
*  to expect. People were very skeptical about the linear representation hypothesis beforehand.
*  And there's an embodiment of that idea about structure because everything is linear direction.
*  But they seem to have worked way better. And I think the other reason is there's some
*  amount of relief that we can just do machine learning now. We can make number go up and that's
*  an exciting place to be for a field that has never previously been able to make number go up.
*  Okay. Let's unpack that a little bit more. For starters, if it's possible to have these sort of
*  sparse representations, like why don't we just build the networks that way in the first place?
*  Why did we go through all this dense and uninterpretable form to then try to re
*  cover the more interpretable form? And when you say make number go up, what exactly does that mean?
*  Yeah. So why not just train models like this in the first place? The answer is that the SAE is
*  way bigger, like really a lot. So I've got llama three AB and then we have an SAE with say
*  three billion parameters. There's no reason why it shouldn't have say 12 billion parameters.
*  And now the SAE is bigger than the model. But in fact, you might want, this is an SAE for just like
*  a middle layer residual stream. You might quite reasonably want SAEs for every layer, every
*  residual stream position and for every attention and MLP output. And now you have 96 things, which
*  are all bigger than the model and you are in for a world of pain. Your bank account isn't that big,
*  basically no one's bank account is that big. And even if it was, they couldn't literally,
*  physically couldn't string together enough GPUs to actually train such a model. And the other
*  part of the reason is that when you put the sparse autoencoders in the model, the model gets worse.
*  We can get say mid nineties percent depending on precise details, but like of the loss
*  gets recovered. But we spend a great deal of money making loss go down by like a decimal point.
*  And so these degradations in model performance can correspond to the difference between, I don't know,
*  say a one in a $10 million model. So you don't want to like have a $10 million model that sucks.
*  It's like way worse. To come back to the compression metaphor again, like why are
*  large language models so good at the things that they're good at? It's because they've looked at
*  an absolutely astronomical amount of data. And there's a very efficient algorithm that's training
*  them that is able to compress that astronomical amount of data to a very finite number of
*  parameters. One of the reasons that large models are better than small models is because they have
*  more parameters to compress that data into. But the compression is a part of the point. And so
*  what we're doing with a sparse autoencoder in a sense is that we're unzipping the model in a
*  compression metaphor. But the compression is why the model is useful in the first place.
*  Yes, we've lost the lead decompressing it and that loss is quite expensive. And to go into the thing
*  about make number go up, this is just maybe a little bit of a social observation that we have
*  a community that would like to do some machine learning. But previously, interpretability has
*  been so qualitative that it's been very hard to imagine doing it at scale. There's been no number
*  for interpretability, not for lack of trying. But now there are at least proxy numbers,
*  like the fidelity, which is this, like how much of the loss have you recovered, and L0, which is
*  like the average number of non-zero features that are active in your sparse autoencoder. People like
*  to plot like a Pareto curve for these. And so once you have metrics, you have people competing to
*  improve the metrics, and they can publish papers and they can cite one another's papers. And it's
*  a force for improving metrics. But once this machine starts going, it just continues going.
*  The machinery of the machine learning field is not something we've been able to turn on
*  in interpretability before. Gotcha. So let me try another summary of what's going on with the
*  sparse autoencoders. And then again, you can complicate or get into variations or whatever.
*  So we've got all these concepts packed super non-transparently in terms of what means what
*  into this relatively small number of numbers that are the activations between the layers.
*  And the goal is to unzip that, if you will, and say, okay, we want to identify what the model is
*  actually doing here. We have this hypothesis that this might be just a handful of concepts that are
*  sitting on top of each other. How would we prove that that's in fact true? If we can project the
*  small amount of numbers out to some much bigger amount of numbers in a sparse way where only a
*  few of the much, much bigger number of numbers are actually activated at any given time, and then we
*  could project that back down into the smaller space and use the result of that. So instead of
*  just having the activations, we can pass it through this much bigger thing, get it back and use that
*  resulting version and carry on and everything still works. Then we would say, okay, we're
*  at least retaining the information that we had where we're able to maintain this behavior.
*  And then we could go look at all these much, much bigger set of numbers and try to do something
*  more like the sentiment classifier neuron where we could say, okay, if there's a ton of these and
*  they only light up each one, only lights up every so often, then we can look at what makes each of
*  these different things light up and we can start to try to make sense of that. So instead of saying
*  position one out of 4,000, it's lighting up to varying degrees all the time. Now we have position
*  one out of, I don't know, potentially millions even, and that only lights up every so often.
*  And here are the kinds of things that make that light up. And so now we can start to try to attach
*  concepts as we understand them to these specific positions. And the sparseness is strongly
*  incentivized by the loss function that you use to train this thing. So if I understand correctly,
*  you have, again, competing forces. The one force is we're going to project this small amount of
*  numbers out to a much bigger and then back down. We want to recover what we had. So that's one
*  thing. You've got to recover the original information in as well as possible. But also,
*  you have to do that with as few intermediate things actually being activated as possible.
*  And so you're balancing those two forces, accepting that you're going to get somewhat less
*  good performance. But the upside of that is that you get a sparse representation that you can then
*  study and it becomes much more interpretable. Yes? No? What variations are there on that theme that
*  people need to understand? That's exactly right. And the miraculous thing is that it works.
*  It's remarkable that this is actually an effective scheme, which I think is one of the reasons why it
*  took so long to try. It seems unreasonable, but it works. So does it just work? It can't be that
*  simple, right? And this is where we're actually getting to what you guys are doing at the company,
*  Goodfire too. So a lot of this work has been done in companies that have obviously pioneered the
*  techniques, Anthropic obviously very notably, but other companies have been doing some similar things
*  too. OpenAI has one. I don't know if DeepMind has put out a sparse autoencoder. Yes, as we're
*  speaking, they've released sparse autoencoders for Gemma 2B and 9B and they've done some work.
*  They've done quite good work on activation functions. That's one of the things that they're
*  pushing on. Like certainly the work that Anthropic and OpenAI has published have been studies of
*  doing this technique to interpret their own models. Those models though are not available to the
*  public. So like other people can't really do this sort of work. Where you guys are picking up
*  is saying, geez, this seems like the kind of thing that would be really useful to make more broadly
*  available. And so you're doing that. Oh, it can't be that easy though, right? To actually go train
*  a sparse autoencoder still sounds hard to me, even though I can explain the high level gist of what's
*  going on. Yeah, there are a couple of ways in which it is difficult. And some of these are
*  simply doing the machine learning right. And fortunately, the community so far, and long may
*  it continue, has been like very open and good about sharing what works and what doesn't. There was a
*  sort of long saga about features dying, which is when essentially the feature just never activates.
*  It's after say 10 million inputs. It's okay, I'm done. And it's never heard from again. And this is
*  a waste of capacity. There's a long saga about how to sort this out, which eventually got resolved
*  from those sort of results in our public for everyone to build on. To the extent that it's
*  simple to do, that's because people have put the work in. That story is far from finished. It's
*  also difficult, relatively difficult from an engineering perspective, which maybe Dan, you
*  want to say something about? Yeah, efficiently training SAEs is quite a challenge. And then
*  further, one of the things that's really important to us at Goodfire is we're making interpretability
*  accessible. We want to move the field from cutting edge research to practical applied use cases.
*  And a big component of that is serving these SAEs. There's a reason Golden Gate Cloud was
*  extremely impressive, but there's a reason that Anthropic served it as a single feature that was
*  clamped up on Golden Gate Cloud instead of giving access to a wide variety of features to edit beyond
*  safety concerns. It's also because the engineering challenges and actually serving this stuff is
*  really significant. And a lot of the existing technology that's out there is still fledgling
*  and developing. And so there's just fundamentally unsolved engineering problems that we're like
*  constantly re-approaching and trying to think about how to look at differently. And this is
*  a good opportunity to give a big shout out to our friends at NDIF, the National Deep Inference
*  Fabric. David Bao, a friend of the pod, is one of the founders of. And what they're doing is they're
*  trying to open source compute. So they're trying to make it possible. There's a lot of research
*  that can only be done on cutting edge large models. And they're trying to make it easy
*  for researchers all around the world to be able to do interpretability work and science on these
*  larger models so that we can all understand them better. And they've built a framework called
*  Insight, which has been extremely useful to us in terms of being able to scale both activation
*  harvesting and interventions. So big shout out to NDIF. They're awesome.
*  So when you're doing this feature pinning, and folks have certainly seen the Golden Gate
*  Clawed demos, if not use it themselves, this is like we've already got our Sparse Autoencoder
*  trained. We have this many super wide, many numbers, each of which are only lighting up so often.
*  We've now looked at what makes that individual number light up. We've got a sort of qualitative
*  sense for, oh, I think it's kind of this, it seems to correspond to this sort of thing.
*  So they did that with the Golden Gate Bridge. And then you're basically saying, okay, if I light up
*  just that one feature in the Sparse Autoencoder and I look at how does that get projected back
*  down into my demodel, my much smaller number of numbers that sit between the layers,
*  that then becomes the representation of that concept. And I could now add that to anytime
*  I'm running the model, I could just salt some of that in there. And essentially, all that work
*  goes into it. But at runtime, if I just want to do Golden Gate Bridge, I can just like hardcode
*  potentially at the layer of the model, everything is computed, now add a fixed array that corresponds
*  to the activation of Golden Gate Bridge per all this analysis. Then we can see how the model behaves
*  differently from there. That is what the feature activation is doing, right?
*  That's exactly right. Yeah. So I don't know how they've implemented it, but it seems clear that
*  if you've got a single edit you want to make, you can bake that into the model. The challenge comes
*  in serving like serving the model with all the dials attached. We've got all of the features.
*  They've got say 34 million features. So that leaves 33 million, 900 and so on. You can't intervene on.
*  The question is how can you serve the model so that I can turn up these features, you can turn
*  up those features and so on. And we can all play around with it and do different things. And I think
*  that's one of the kind of serving use cases that if you can unlock that, there's probably a lot of
*  different really cool applications that you could build on top of that foundation. Yeah, cool. Let's
*  come back to that in one second. I just wanted to also ask one other question on the training of the
*  SAEs. You said you're storing ungodly amounts of numbers. A sort of naive approach to doing this
*  would be like, okay, run some data through the model, get to a certain layer where we want to do
*  this thing, take those things out, run a separate step on the autoencoder. But it sounds like you're
*  separating this out in a much different way. So is there a rough guide to how you've engineered
*  this? Are you running all the data through the model and capturing all of the activations as one
*  giant step? Then you have a pool of activations that becomes training data for the SAE and that
*  runs in a very different time and different environment? Or how do you tame that complexity?
*  The goal of good engineering is always to help other people do their jobs more efficiently.
*  So from the perspective of what we want to accomplish here is, as Tom mentioned, we're
*  starting to develop a science of SAEs and how to train them. But this is by no means finished
*  science. There are a lot of experiments that we need to be able to run and information we need to
*  gather. We'll do multiple SAEs for a given experiment. And sometimes we'll get pretty
*  different results depending on some very tiny differences in initial conditions for those SAEs.
*  And so what we need to be able to do is we need to be able to harvest these activations from the
*  model. And then we need to be able to train a bunch of different SAEs on that same data to be
*  able to get good signals. And there's a decent amount of engineering work that goes into that.
*  But simultaneously, we need to be able to make sure that harvesting the activations, which is
*  quite time consuming, and the amount of activations you need to do a really large model like LAMA-405B
*  is really huge. So we need to make sure that activation harvesting isn't a bottleneck. And
*  what that means in practice is really efficient inference code to be able to extract those
*  activations as quickly as possible. The majority of the cost of an SAE training run, if you were
*  to do it online, as in if you were to do the scheme that you're talking about, so you put data
*  in, you get activations, you stream those over to the SAE, you train the SAE, the vast majority of
*  the time and the vast majority of the cost is like running the language model itself rather than
*  running the SAE. So when we just write them to disk, if I want to do a 10 or 100-volt hyperparameter
*  sweep, then it amortizes, which is really nice because you don't want to keep paying that.
*  Yeah, gotcha. So collect all these activations at huge scale and train, store those, and then you can
*  run lots of different experiments on training SAEs with different recipes.
*  The cost effectiveness calculation changes if you, say, have found hyperparameter settings that you're
*  interested, that you're confident in, and you now want to train SAEs at every layer and every site,
*  residual attention MLP, then maybe you want to do something different and you want to do exactly
*  the scheme, just stream them out to a whole load of... You have this very big distributed job,
*  which will be very painful for us in the future, but we'll handle it. And the trade-offs change
*  in that case. I could go on about this all day because I enjoy trying to make sense of all the
*  great work that you guys are doing, but maybe it's time to get on to the vision. We've seen Golden Gate
*  Clawed. What are you guys building? How would you relate it to that? And how does this feed into a
*  longer-term vision of cracking open the black box once and for all? Yeah, it's really important that
*  we make sure that AI tools are working in the service of humanity. And it's basically impossible
*  to ensure that if we don't understand them and how they work on a much more fundamental level than we
*  do today. I think we've all just taken it for granted that AI is a black box, but what we would
*  far prefer to live in is a world where we can work with AI models, debug AI models the same way that
*  we would debug any software that's out there. And that when models misbehave, we can tell causal
*  stories about why they misbehaved and make sure that doesn't happen in the future. A 2024 McKinsey
*  survey revealed that 44% of business leaders have experienced at least one negative consequence
*  due to unintended model behavior. I know at Ripple Match, being a recruiting AI startup, we cared a
*  lot about bias and making sure that our AI systems were not biased. And that made it basically
*  impossible to leverage large language models in certain types of applications where we couldn't
*  make those guarantees. But if we can open up the black box and understand how these things are
*  working, then we can make sure that they're working in the way that's compatible with the
*  society that we want to design as human beings. And so we're envisioning a future where it's less
*  like growing models and more like designing models and making sure that we have strong guarantees
*  around how our models behave and that we understand their role in society much more deeply as a result
*  of understanding them much more deeply. So what are you building now? And what is the first
*  version of that? And how does that evolve? Because there's so many concepts out there, right? In
*  some ways, this is like the grand challenge for AI, especially if we're going to have like very
*  powerful AIs to have full accounting for why they're doing what they're doing so that we can
*  reliably count on them to do the right thing and not the wrong thing and not to surprise us in
*  negative ways. Some would say that's the whole ballgame. So tell us more about how we go from
*  here to there. Oh, yeah, it's a tremendous challenge, but this is the right time for a
*  company to be taking this challenge on. So there are a lot of different dimensions in which we
*  really want to bring interpretability to industrial scale. Sparse autoencoders are one important
*  dimension. Another important dimension we haven't touched on yet is this idea called
*  autointerpretability. Nick Camerata, who's a great interpretability researcher, one of our advisors
*  at Goodfire, was one of the co-authors on a paper called Language Models Can Explain Language Model
*  Neurons. And what they showed in that paper was that you could use a language model and you could
*  set up the prompt such that the prompt contained information about the activations of neurons in
*  language models, and you could use that to get interpretable labels for various neurons, in that
*  case, in the model that were statistically robust. This has evolved over time to be looking at
*  labels for sparse features that come out of sparse autoencoders. And this is a whole area that is
*  extremely exciting, and there's a lot of interesting research to be happening on in order to make sure
*  that we can label things effectively so that we can traverse them effectively.
*  And the next component that's extremely important is interface. Whether it's a programming interface
*  or a user interface, the amount of information that's available here inside of these models is
*  gigantic. So how do you traverse that information effectively? How do you allow human operators who
*  are interested in understanding that model to pull up the most important and salient information?
*  Those are some of the primary questions that are motivating us right now. We are still in a moment
*  where the science is unfolding in front of us, and we're going to be discovering new and interesting
*  things all of the time. And so what we really want to do as a company is figure out how we can
*  leverage this in a way that just makes understanding models easy and effective. To that end, we are
*  planning on releasing a research preview, demoing some of the interesting things we've been doing
*  that will allow people to talk to one of the LAMA family series models, look for patterns inside of
*  the models, inside of the features, explore different features, and then also intervene on
*  various features in order to study how that affects the behavior as well. But the long-term
*  vision here is really to build a world where interpretability is the default, that people do
*  not release models into the wild that they don't understand. And so that's a tremendous challenge,
*  but the way that you do that is you scale the science and you build interfaces that are intuitive
*  and easy to use and try to get the world to a point where we can't believe we ever thought we
*  would do things differently. Maybe one way to phrase that too is that our short-term mission
*  is get the rest of the world to see the vision that we see, which is that we can live in a world
*  where AI models aren't black boxes anymore. And we're going to release a bunch of public demos
*  to help illustrate that point extremely clearly and effectively. And then where that takes us as
*  a company, like the science is evolving, we'll have to see. But right now, we all very deeply believe
*  that there is a better way, a better path that we could be on, and that now is the time to get the
*  rest of the world to see that as well. So essentially we're trying to release demos that will spark
*  people's imagination, get them thinking what they could do with the kind of services that we'll be
*  able to provide. And then when we get that kind of contact with reality, it's very clear where the
*  research is lacking. And that helps us to also determine our research agenda and say, oh, this
*  sort of thing makes for a cool paper, but when you actually try and use it, it just doesn't really
*  work very well. So we need to push into that. This thing is basically already as good as it needs to
*  be. The contact with reality is, I think, the thing that's really distinguishing for us.
*  So I guess, big picture, one might imagine that this could be a nonprofit. You guys obviously
*  opted to form a company out of it, and you've raised money from private investors, including
*  yours truly at a very small nominal scale. I guess part of the reason for that is just that this is
*  going to be a compute-intensive thing to do. So how much money have you raised and how are you
*  thinking about deploying that? And tell me if I'm right in the first place on the business versus
*  nonprofit direction. Yeah. So we've raised $7 million in our seed round, which is led by
*  Lightspeed Ventures. And the reason that we've decided to go the for-profit route and really
*  trying to raise venture capital and scale the business as quickly as possible is, as you're
*  mentioning, scale is one of the big bottlenecks. As Tom mentioned earlier, if you want to train
*  an SAE on every layer in a model, that is a very nontrivial operation to be able to do from a compute
*  perspective. But the other key aspect of it, as Tom was alluding to, is that we really believe
*  in the importance of grounding research in real-world use cases. I think the rate of
*  progress in research has been super exciting, and we want to figure out how we can make this useful
*  to the rest of the world. And the best way to do that is to get out and to try to create something
*  that people want to pay for, because they'll see the value in it enough to want to purchase it.
*  And so those two factors combined is why we believe that a for-profit company is, and we're
*  a public benefit corporation, because we also fundamentally believe in the transformative power
*  of AI and want to make sure that we are always keeping center at our mission to significantly
*  reduce risks associated with AI through our interpretability research. But we also believe
*  that the funding vehicle of a private company is the best way to accomplish both those really
*  important goals. Do you have hypotheses for what are top pain points that people
*  are likely to want to pay for? And do you have any sort of sketch of what the form factor would be
*  that they would be paying for? Is it a seat to a software tool, or is it a run of a process
*  where you're bringing a lot of compute to bear on a question that they ask?
*  I really don't have much intuition for how that might evolve over time.
*  So I think what I would say there would be something to the effect of there are going to be
*  dozens of interpretability companies. We're envisioning the future that this science is
*  going to unlock as one of just an entire ecosystem of companies that are building on top of each
*  other. There's going to be user interfaces for regulators and auditors, user interfaces for
*  applied AI work, user interfaces for frontier labs designing models. There's going to be use
*  cases in prompt tuning, use cases in rag, use cases in designing better training data. And
*  what we want to be as a company is we want to be foundational to all of it. We're envisioning
*  a humongous market for AI interpretability, and we're going to be one of the foundational
*  of the foundational early players in that market that help define what this space really is.
*  Cool. Yeah, that's again, inspiring. I think it's a brave new world. We've obviously covered a lot
*  of ground in terms of like we figured out a lot of stuff. What would be the skeptic's position
*  today, given all that we have figured out? What is the remaining hard part and what gives you
*  the confidence that you can solve those or that the community maybe collectively will solve those
*  remaining hard parts? So there's a bunch of different levels of skepticism you have.
*  One is the models just have these concepts that are uninterpretable. And I think this position has
*  been in retreat for quite a while. First, there were not going to be any, then there's like,
*  oh, yeah, they're not that important. And then there's these increasingly subtle ones, like
*  there's a sort of God of the Gaps type thing going on here where like, where are they? There
*  are these uninterpretable concepts, like where are they? But still, it is reasonable to suspect
*  there will be some concepts which are at least very hard to interpret. We're picking the low
*  hanging fruit, some of the fruit will get considerably harder to pick. And you might be
*  skeptical that we will ever be able to understand them. Now, I think humanity has understood some
*  incredibly complex things over the course of millennia. So I think the bar for we will never
*  be able to understand it is set extremely high. We understood general relativity, we built rockets,
*  we could probably understand some more features. But there's also the argument that it might just
*  never be cost effective. And that's to some extent a scaling question. So that's one line
*  of skepticism. Another line of skepticism is that for any given application, interpretability
*  may be dominated by some other approach. Now, I think this just seems a priori very unlikely to me.
*  Like, you can maybe it's always better to fine tune a model, say. And I think the difficulties
*  that people have been having with say, our LHF, it's very good in some ways, but it's also very
*  brittle as a way of controlling models. Like, it feels like we can probably do better. And an
*  analogy that a friend of mine made to me was like, it used to be the case that we design crops
*  by essentially trial and error, we like fine tuned wheat, we fine tuned wheat until it was good.
*  So we selected the ones we liked, and we threw away the ones we didn't. And we got wheat to a
*  pretty good state. But now we have genetic engineering, we can just go in and change all
*  sorts of things really fast and efficiently. And this is like a change in power from being open,
*  it takes you from kind of trial and error selection to direct engineering. So I don't really believe
*  in this line of skepticism. I guess I'm not going to believe in any of them too much. Otherwise,
*  I'd be doing something else. One thing that I'll add to that is that you touched on this, Tom,
*  but just because something is really complex doesn't mean it can't be understood. I think there are
*  definitely practical questions of how difficult is it to interpret a feature, maybe some features
*  will take a really long time to interpret. But for too long, we've started with the prior that
*  these models are not understandable. And I think we have enough evidence that we should start with
*  the prior that they are, and see what we can find when we really try very hard to interpret
*  what's going on inside of them. Maybe the sort of the very highest or the most human level,
*  the story of interpretability over the last decade has been the story of kind of courage paying off.
*  People who believe it can be done have managed to get it done. And in spite of like, all sorts of
*  reasonable a priori skepticism, they managed to make a huge amount of progress. When you talk
*  about uninterpretable features, what is that? So we have this sort of sparse thing that
*  tries to pull apart all these concepts that existed in the between layer activations.
*  And we see that, okay, this one position lights up for these various inputs. And then we just look
*  at those inputs, or we maybe enlist a language model to help us look at those inputs. And we just
*  can't make sense of it. Is that basically the phenomenon? Some of them are like, okay,
*  yeah, that's clear. That's Golden Gate Bridge. And others are just like,
*  I don't know, that seems all over the map. Not really sure what's going on. Is that essentially
*  the problem that remains there? Yeah, like we just try we look at it, we try really hard, we do
*  everything that we can imagine. We know that it's causally relevant, right? So by construction,
*  in this example, like, the feature is, it's important you oblated the model just doesn't
*  do anything sensible, say, it does some like, it's out the outcomes from ablating, it also
*  don't make sense. So we've got literally nothing to go on. But we know it's important. And we just
*  keep trying, we do everything we can think of. And eventually we give up in despair. That's the
*  story. I don't think this is likely I don't know if this has ever happened. Certainly, people have
*  looked at features for short periods of time and given up. But generally, when people spend time
*  looking at features and understand the sort of causal story between about how they came about,
*  and what they do, understand them in terms of circuits, then you can get there, you can really
*  get a lot of insight. And to connect this a bit to the engineering story as well as right now,
*  we have a set of techniques that work well enough that we're starting to get a really good signal
*  and we can stop optimizing. Real world production systems rarely rely on a single technique. It's
*  often a number of stacked techniques, which cover different use cases and can fall back onto each
*  other. And that just doesn't exist in interpretability yet. We have a lot of extremely
*  promising ideas that work pretty well. And there's this big question of what is the
*  combinatorial system that's going to be able to continue to push the envelope in terms of
*  what's interpretable. But we're already seeing through the innovations that are happening in
*  SAE architecture, even this early in the game, that you can push the Pareto frontier of how many
*  of the features you recover that are interpretable with some pretty simple ideas. And so I think
*  that's going to continue to be the case moving forward as well. And we're just going to architect
*  more and more complex systems that approach the problem from lots of different angles.
*  That's one of the reasons that a private company is going to be particularly effective at this,
*  because it's not going to be just scale in terms of doing a few techniques at scale. It's going to
*  be scale in terms of the architecture of the system. It's going to be horizontal and it's
*  going to be vertical. And together, between those things, we'll keep pushing how much we can
*  interpret inside of these models. Maybe there's a limit. I kind of don't think that there will be,
*  but maybe. How much does it cost to train these sorts of things? Like of the $7 million raised,
*  do you have a sense for how much of that is going to go to compute?
*  A decent amount. The reason that we raise such a significant seed round is because a lot of
*  what we're going to have to do is compute bound. That's the reality. And the larger the models that
*  we are training on, the more compute bound that we're going to become. So we're going to continue
*  to work right now studying 8B and 70B models for the next few months. But the natural extension of
*  this is Lama 405B just came out. And so a pretty likely place for us to go in the relatively
*  foreseeable future is really trying to push ourselves to the frontier of models and working
*  on the largest, most capable models that are out there. What type of interpretability work can we
*  do on them? And yeah, that requires a lot of compute to make that happen. But it's potentially
*  really worth it. If you had an interpretable Lama 405B, that would probably be the most useful
*  model in the world. Do you have any thoughts on alternative architectures and how that could
*  shake the snow globe? I've been a big fan and admirer of the state space model
*  line of work recently. And my general sense, although I certainly can't claim expertise on
*  this, is that interpretability techniques have worked on those models surprisingly well,
*  way better than I would have guessed that they would if you told me, hey, we've got a totally new
*  architecture here. Are we going to be able to rerun a fellow GPT type work on it? I would have
*  said that sounds tough, but it seems like it's worked. Do you have a framework or a mental model
*  for how new architectural innovations will impact the course of your work? I think that some of this
*  comes back to the universality thing. Like the same representations are probably more or less there
*  in any model which is capable of doing the tasks efficiently well. They might be in different places,
*  you need to understand something about the structure of the architecture that you're
*  looking at to understand where you should look, but they'll probably still be in there.
*  And I think as long as we have embeddings, SAEs will be useful. And if we have networks that have
*  no embeddings, then we're in some kind of wild and crazy future. And yeah, we'll need to adapt
*  and rethink things. But I think the whole world will be adapting and rethinking things at that point.
*  Do you guys want to get into the application of this to models for science or let's say
*  biologically sequenced trained foundation models? That's a great segue because they have
*  all sorts of architectures. So one thing that we've not really talked about is another reason
*  for trying to do adaptability on models is that we actually really want to know what's in them.
*  So if we've got a scientific foundation model, say we've got something like AlphaFold or ESM3,
*  there are models of quantum chemistry, weather prediction, there's a huge list and it's growing
*  all the time. When they're better at doing scientific predictions than our best theories,
*  they probably know something that we don't. Not wanting to be too philosophical about the word
*  no here, but there's some information in there that we don't have in our theories. And as a
*  scientist, I want to know what it is. And I think interpretability is probably one of the best paths
*  to getting there because it doesn't constrain your architecture to the extent we're able to
*  generalize the new architecture as well, which I think is quite high. We'll be able to go in
*  to these scientific models and this is going to be a test of really how well we're doing. We'll
*  be able to go into these scientific models and pull out the new science and then bring it back
*  to the rest of the world because otherwise the science stops a bit.
*  We value scientific theories for their predictions are like useful and they're one of the things
*  that give scientific theories their impact in the world. But we also just want to know,
*  we want to know about the universe. And interpretability could be one of the main
*  ways to do this if we have an era of scientific foundation models.
*  This is one of the core reasons that I think interpretability is the most important problem
*  to be working on right now. And I think these use cases that Tom's outlining here, they're
*  actually not that distinct from the use cases of understanding a language model. As we mentioned
*  earlier, when talking about universality, we are potentially, and in fact, I think we're definitely
*  learning things about ourselves and how we process information through studying how these
*  models are processing information. We see that things that we learn in training language models
*  can influence how we study language in the human brain. And if we weren't able to start unpacking
*  what these models were learning inside, then we wouldn't be gaining those insights to begin with.
*  And so this applies to every scientific field that you can imagine that you could train a model to
*  perform a task successfully. If we live in a future where we're capable of explaining models,
*  anything you can train a model to do, you can explain. And so I think this has the potential
*  to be like a core transformative scientific technology, maybe on the level of machine
*  learning itself in terms of its ability to just advance our relationship to the world and the
*  progress of science. It feels very likely to me that it's going to shape up this way. I wonder
*  if there's really even an alternative, but when you think about these weather models and these
*  biological structure prediction models where this thing can now give us the best 10-day forecast
*  relative to any other thing we've ever created, or can predict the structure of a protein or
*  a complex of proteins better than any other approach that we've ever created. That starts
*  to be a really different way to think about what these models in general are doing. First, it was
*  they're not really learning any concepts. It's all just stochastic parotry. Fine. Now we've maybe
*  moved on to, okay, sure, they're learning concepts, but they're just learning concepts that we already
*  had encoded in our language that they were able to pick up from us. They're not going to learn
*  any new concepts. But now it's, yeah, it seems like there's got to be probably some new concepts
*  that they are learning if they're going to be doing weather forecasts or protein complex
*  structure prediction better than we've ever been able to do it. And so to look inside those kinds
*  of models and try to figure out what have they actually learned, can we pull those concepts apart
*  and actually discover net new concepts through what the language models have figured out, or I
*  shouldn't say language models in that case, but through what the models have figured out on their
*  own. And can we back interpret that into human interpretable concepts that we can then run with?
*  That seems overwhelmingly likely to me at this point. It seems like we've already got some
*  examples of that happening, and it seems like we should expect a lot more. And that is both extremely
*  exciting from a scientific standpoint and also to me seems extremely informative about where
*  the overall models are going and why I don't think they're likely to level off exactly human level
*  performance on any number of different things. Is that basically your expectation as well? I guess
*  the short version of that is in virtue of the fact that they can do these other things that well,
*  we probably shouldn't expect level off at human expert for most things.
*  That is an interesting question that I have a lot of uncertainty about. But to the extent that this
*  argument makes that goes through is about transfer and it's about relative. It's not obvious to me
*  you get very much transfer between a completely numerical prediction of the weather and a humanish
*  model of intelligence. So there may be clever schemes, but if you're naively to incorporate
*  weather prediction, say, and if you're to incorporate a whole range of scientific tasks
*  into the training of something which is foundationally a language model, I suspect that what you get is
*  if you have 10 tasks, then really what you get is 10 models in a trench coat. You've got one model
*  under the hood, it's just like 10 separate things running. Now, if that was untrue, then yeah, I think
*  this would point to doing substantially better than human level. But as it is, I have quite a lot of
*  uncertainty about how you'd actually leverage that kind of data to avoid being capped at human expert
*  level. I mean, it might be the case that you have a model, you have these separate domain foundational
*  models, and you have a language model where other models are its modality. It's multimodal in that
*  it can do vision and it can do language and so on. But it can also, somehow, you can plug into other
*  models at the activation level and explain them. Maybe this is the complete endpoint of
*  interpretability as a model that just plugs into another model and explains it. Now, I think that's
*  a bit of a pipe dream at the moment, but it's one vision of where things go. I personally quite like
*  maybe a little bit old fashioned. I quite like the vision where we're still the ones doing the
*  explaining. Yeah, let's push that as long as we can anyway. Yeah, exactly. I like finding out how
*  stuff works. I don't want it to... It's like getting the answers to your maths questions, right? Before
*  you've had a chance to finish them. I'm interested by your comment too, that you think it would end
*  up being like 10 models in a trench coat. I guess my intuition for that is the other side of that.
*  I don't have a super principled reason to say it, but I do just see everything in the main language
*  models seems to run together so well that you can write a sonnet about chemistry or whatever.
*  It doesn't seem like you have a Shakespeare model and a chemistry model that are somehow
*  not joined. It seems like those things have blurred enough that I expect the same to happen,
*  even if you get weirder and weirder in terms of other modalities that you would bring in.
*  I guess there's a couple of things that are weighing my intuitions the other way.
*  One of them is the sense that vision language multimodal models don't seem to have the same
*  sort of seamless synthesis between their vision modality and their language modality as different
*  tasks within language modality. For instance, I guess we've all tried to get IVLM to pay attention
*  to the image, please look at what is in the image. This sort of synthesis never seems quite
*  as seamless as it does within. The other thing, this is perhaps a little bit esoteric,
*  was there was this DeepMind Gatto paper where they had essentially a language model doing
*  tokenized versions of all sorts of reinforcement learning tasks. My conclusion from that paper was
*  that essentially there was very little transfer between these tasks. The intuition that I had
*  here was that when domains bleed into each other enough, you get transfer. When they are
*  sufficiently separate, you can just recognize literally this is Atari and this is moving a
*  robot hand. Then probably there is actually very little in a sort of deeper sense, there is very
*  little to transfer. It's also very hard to learn that. It seems that language and weather predictions
*  are sufficiently separate, that they have such different input-output spaces and types of reasoning
*  that perhaps they're hard to actually smush them together and get that overlap. Perhaps I'm just
*  not being imaginative enough, someone very creative could probably come up with ways to make them blend.
*  Yeah, I think one way to interpret the amazing things language models can do is to say,
*  less this is some universal law of the trajectory of all models, and instead to say, wow, language
*  is a really rich task. That's just an incredible task. You can get so much interesting information
*  just from language. I think what you're saying, Nathan, in the absolute limit probably seems true.
*  If you had an infinite size neural network and literally all of the data in the universe,
*  there probably are some pretty deep representations and concepts that you would notice. But whether
*  or not we're going to notice them on any shorter time scales is, to Tom's point, a question of
*  how much shared representation truly is there between those different modalities that you're looking at.
*  There's also, to be mundane for a minute, a question of economics. If I've got a weather
*  prediction model and I want to run it a lot, then it doesn't make that much sense for me to be paying
*  the cost of also having this model know how to conjugate French verbs. It may just be that you
*  could push them into the same model, and perhaps it leads to some small amount of transfer,
*  but that transfer isn't worth the inference time cost. Again, it may be possible, but economics
*  rules everything around us. That relate to claims of video models like Sora and Veo and whatever,
*  and runway gen 3s, even talking about this now as being like world simulators.
*  I don't totally buy those claims. I agree that they are true in the limit. You can't simulate
*  a video perfectly without having a great model of the world. I think they look very compelling,
*  and they are very impressive. But they often don't seem great models if you look at the details with
*  respect to a bunch of properties that you might want a world simulator to have, like object
*  permanence. And sometimes, often you will see, even like quite superficially good looking
*  examples, you'll see, I remember seeing like a flock of birds and the birds would end up kind
*  of merging into one and then splitting and that kind of thing, which is not the property of birds
*  in the world. Now, maybe scaling will just solve this. But at the moment, I feel like there might
*  be claims about the future rather than claims about what is currently possible. I also think
*  there's a way to reconcile that with what we're saying that makes a lot of sense to me. Even if
*  you accept the world simulator framing, world simulator, I think is doing a lot of PR as a
*  phrase. But what's meant by that is that these models are like learning things that we would say
*  correspond to real attributes in the world in the process of simulating data that was produced by
*  the world. And on some level, that's like unsurprising when you say it like that.
*  And they're learning hierarchical representations of patterns that resemble the data that they're
*  trained on. And so it could be the case that you have a super large video model and it's like
*  really good at simulating physics because like physics is a necessary representation to be able
*  to accurately reproduce the video. But that doesn't say that if you then combined that video
*  model with a language model, that it would give you new insights into physics that came out of
*  the video portion of its training. The model might not be able to verbalize. It might intuitively know
*  that this is where the ball should go, but it might not be able to actually back that out into
*  an equation. And it only would, the compression story is correct. It only would if learning that
*  helped it compress, which it might or might not. I don't know.
*  Yeah. Fascinating. So what are you guys looking for as you build out the team to unravel all these
*  mysteries? So we are currently hiring. We're looking for founding team members, founding engineers,
*  founding research scientists to help us execute on our mission of making interpretability the
*  default in models that are deployed in the real world. So if you are an engineer or scientist who
*  really believes in everything that we're saying today, really understands the importance of
*  interpretability and the potential of this technology, and you are excited to work in a
*  cutting edge, scrappy startup, that's really, this is new science. We're figuring it out as we go.
*  So if this all sounds exciting to you, definitely reach out to us, check us out at goodfire.ai
*  and yeah, apply. We'd love to talk to you. Anything else that we didn't get to that you
*  guys want to touch on before we break? I think one thing I'd just like to say,
*  and this is like a general comment, that this could be the great scientific adventure of the
*  next couple of decades. And it's incredible to like actually be in that. And also it's a great
*  open community, people can come in and just participate in this scientific adventure.
*  Like, it's incredible that this is happening and we're here doing it and we get to be a part of it.
*  It's amazing. Definitely the events of the last couple of years have made me
*  more inclined to believe that I might be living in some sort of simulation,
*  because it does feel like, man, I shouldn't be this close to the singularity. And yet here we are.
*  So I'm here for the great adventure that you guys are setting out on and really excited to
*  follow your progress. Definitely have had a ton of fun just chatting back and forth about ideas and
*  look forward to doing it again in the future and encourage anyone who is interested to apply if
*  they're ready. Or also maybe one other thing we could talk about just very briefly in closing is
*  like, if somebody is not ready, what could they do to get ready? Let's say you're a good software
*  engineer, but you haven't done any interpretability. What is the path? Maybe you would say like still
*  apply, we'd be interested in that. But first of all, are you? Would you not? And if not,
*  what is the crash course or how should somebody go from zero to good fire ready?
*  So speaking as someone who's been on this journey recently and really grateful for how open the
*  interpretability community has been in just wanting to teach people about the exciting science that's
*  going on. I think that there's absolutely a path. If you have no experience, no familiarity with
*  machine learning, no familiarity with how transformers work on a fundamental level,
*  you'll have a lot to study. There's no question about that. But there are lots of resources that
*  you can find online. There are lots of amazing papers, perhaps we can leave some of our favorites
*  in the show notes. And if you work hard, if you study, if you go and ask questions, what's something
*  I have found is that a lot of academics, like they want to hear from people. If you reach out to them
*  and you've read their paper and you have a question, they'll often enthusiastically respond
*  because people are just so genuinely passionate and excited about this moment that we're in
*  scientifically. So if you're so motivated and you want to put in the work and it will be work,
*  but if you want to put in the work, you can catch up. Yeah, it's such a great community, like
*  people in it, including us to help people, like to help people get into it. So get in touch,
*  we can help. We can't tell you everything, but we can point you at stuff. There's loads of good
*  resources. Yeah, we can put some of the notes too. Cool. We'll do that. For now, Dan Balsam and
*  Tom McGrath, co-founders of GoodFire, thank you both for being part of the cognitive revolution.
*  Thank you. Thanks. It's been great. It is both energizing and enlightening to hear why people
*  listen and learn what they value about the show. So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media platform of your choice.

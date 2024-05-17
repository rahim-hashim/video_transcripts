---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 5180s
Video Keywords: []
Video Views: 1235
Video Rating: None
---

# Chroma and Stable Attribution 's Anton Troynikov on embedding and our future with AI
**Cognitive Revolution "How AI Changes Everything":** [March 02, 2023](https://www.youtube.com/watch?v=ogy37CdIljg)
*  ML models are kind of weird in the way that they think, quote unquote, about the world.
*  And they might represent something quite differently to what a human would. They
*  might focus on quite different things because they are mechanistically pursuing an objective.
*  They are not trying to encode any meaning. The Wright brothers were wrong about how the Wright
*  flyer worked. They just had intuitions about it. And it flew. That's an object demonstration. It
*  doesn't really matter if your intuition is wrong if the thing works. And then there's this Cambrian
*  explosion of different types of aircraft because we only had to go on with intuition. We didn't have
*  engineering principles yet. And we didn't even really have the tooling to develop those engineering
*  principles. That's where we're at today, in my opinion, with machine learning. And one of my
*  favorite things about Kurzweil is I went on the website not long ago and it was like the 10th
*  anniversary of the singularity is near. And that just, I don't know, that made me laugh.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of how
*  AI technology will transform work, life and society in the coming years. I'm Nathan Labenz,
*  joined by my co-host Eric Torenberg. The Cognitive Revolution podcast is supported by Omniki. Omniki
*  is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad
*  iterations that actually work, customized across all platforms with the click of a button. Omniki
*  combines generative AI and real-time advertising data to generate personalized experiences at scale.
*  Anton Tornikoff is a co-founder of Chroma, the AI native open source embedding database.
*  In the midst of an AI gold rush, Anton is selling shovels. Embeddings, for any who don't know,
*  are numerical representations, generally speaking a single vector, or simply put,
*  a list of numbers, that encode an input. That could be text, an image, an audio file,
*  or even a DNA sequence or protein structure, into a lower dimensional latent space.
*  The embedding process is itself learned, such that semantically similar inputs cluster together in
*  latent space, and the resulting embeddings can be used to compare inputs, to power retrieval systems,
*  and for additional processing. Embeddings are a key piece of a huge number of AI-based projects
*  right now. By embedding a data set, whether it's a user's email history or Google Drive documents,
*  or even a company's entire knowledge base, developers can enable semantic search at runtime
*  and include the most relevant background information in language model context.
*  This dramatically improves performance by reducing hallucinations and increasing personalization.
*  We talked to Anton about embeddings, the trade-offs and optimizations involved with
*  working with embeddings at scale, their recent stable attribution project, which flexes the
*  power of Chroma by taking a stable diffusion generated image and attempting to determine
*  which of the five billion images in the Lyon training set had the most influence on its creation,
*  but which also quickly became a flashpoint in the broader debate about how artists and other
*  rights holders should be credited and compensated for their contributions to generative models.
*  We also covered the big picture of recent AI developments. Anton is a deep thinker with a
*  sophisticated conceptual understanding of latent space. I learned a lot from this conversation,
*  and I hope you do too. Anton Shroenikov, welcome to the Cognitive Revolution.
*  Glad to be here.
*  So tell me first about vector databases. I think our audience is obviously interested in AI.
*  They most probably have at least a superficial sense of what a similarity score is, what a dot
*  product is, but take me to how that works as a database, and then we'll get into some of the
*  optimizations there as well. Yeah, sounds great. So let's kind of start at the beginning.
*  What a vector database allows you to do is if you can represent your data as a vector,
*  it makes it possible to perform geometric operations on your data. So traditional databases
*  have, let's say, algebraic discrete data structures, right? Like a SQL table you select from where,
*  and it has concrete properties, and it returns exactly that result. With a vector database,
*  data is represented as vectors in high dimensional space. So you can perform operations that have
*  geometric meaning instead. Like distance, you already mentioned similarity scores. You can talk
*  about densities meaningfully. You can fit surfaces to them. You can cluster them in a way you can't
*  in an algebraic form of data structure, discrete data structure. So I think the reason that they're
*  exciting right now is because we now have powerful models that can transform all kinds of different
*  types of data into vectors, and it can transform them into vectors in a meaningful way.
*  So traditionally, that's been text, and a lot of these embedding functions have been kind of hand
*  rolled. But now with the success of transformer models and attention-based models for modeling
*  text, the vectors that you get out from those kinds of models are much more meaningful. They
*  represent structure like a human would impose structure on the resulting vectors. So sentences
*  talk about similar things, they end up close together in vector space. What that's done is
*  turn on a lot of experimentation and development with using embeddings as kind of the AI native way
*  to represent data. And so I'll give you an example. A typical workflow that you see is
*  you want a model to answer questions about specific information. So chat tpt, for example,
*  it's trained on an enormous amount of data. You can ask it questions about anything,
*  but it might hallucinate, it might not have the information that you want,
*  and certainly it might not have your personal private information that it wasn't trained on
*  because it's not available anywhere else. You still want it to be able to answer questions about it
*  because it's good at general question answering as a task. So what you can do is you take the
*  corpus that you want it to answer questions about, and then you embed it. You can embed it using,
*  there's a bunch of open source models. You can also use open AI's API, you can use KPI's API,
*  and transform that data into vectors. And so you have the data available as vectors
*  with the actual text associated with it, with that representation. And then what you do is you
*  query it. And you query it by, again, taking a query, embedding the query text, performing
*  a nearest neighbor search or an approximate nearest neighbor search in the vector database,
*  returning relevant documents. And then what you do is you take your question and you take the
*  relevant documents that it found, and then you ask the model specifically to answer the question
*  with the documents that you've put in its context. And then it's much more accurate,
*  and it's answering questions about the thing you actually want it to answer questions about,
*  with data that wasn't available to it at training time. And this is a really powerful technique.
*  It pretty much suppresses hallucination. It allows you as an organization to use large
*  language models without fine tuning them, which is expensive and slow. And it confers a lot of
*  other advantages as well, which maybe we'll get into in time. But that's kind of the basic idea.
*  Vector databases have been around for a while. Pretty much any service that you use that has a
*  recommendation or a similarity thing. So the one that I always think of is Pinterest. It'll show
*  you similar images. And the way that that's being done is because they have these images encoded
*  into vectors, and they've got a large vector database so that when it wants to find nearest
*  neighbors, it'll look for that and you get visually similar images. Because their embedding
*  function produces visually similar images for vectors that are close together. But the use cases
*  for these things are exploding now because the embeddings for all kinds of data became available,
*  and it's super cheap, and you can just hit opening eyes API. You don't need to have your own model
*  anymore. And people are building all kinds of really cool applications on top of this stuff.
*  Yeah. Okay. There's a lot to dig in there and follow up on. For one thing, just to contextualize
*  a little bit, I would imagine a lot of our listeners have experienced querying SQL databases.
*  So I would love to get a little bit of a sense for how the DBA life is different as we move into
*  a vector world. I think you spoke, and I'll just give a couple additional notes too on like, there
*  is so much energy around these kind of chained retrieval and language model systems right now.
*  That's really at the heart of kind of these dreams that everybody is dreaming. Everybody sees chat
*  GPT, and everybody says the same thing that you said, which is, well, man, if this had my data,
*  if this could go read all my emails, if this could remember every text message I've ever sent.
*  And then obviously the business use case is even bigger and probably a deeper need,
*  because now you've got organizations and all of our Google Docs, and our whole knowledge.
*  How many companies have rolled out these knowledge bases or the Wikis? But
*  do those things, can anybody even locate the information in there? Generally not. So this
*  vector database kind of sits at a really critical point in that value chain. And
*  you've started a company that is a vector database company. So before we go into even more
*  details, let's talk about your company specifically. Absolutely. So I want to say one specific thing
*  here. Chroma uses a vector database as a technology, but the thing Chroma really is, is a platform for
*  basically embedding knowledge that your machine learning enabled applications can use. You can
*  think of us as the thing that acts as the storage layer for applications that use large language
*  models in the loop. So we're much more than a vector store. And one of the things that we have
*  to really learn while we were building this product was the affordances of the existing
*  vector stores on the market don't really suit this use case very well at all. And we actually
*  built this product in-house and we were using it in our own product experiments for a while.
*  Chroma started by first, Chroma basically started on the principle that you can understand a model's
*  behavior based on how it sees its data, basically. And an embedding is a representation,
*  is a model's representation of its input data. And so our early, all of our product experimentation
*  was around like running algorithms and embeddings, representing them, showing them in different ways,
*  manipulating them in different ways. And we needed something really easy to use for developers. We
*  needed something that would allow us to rapidly experiment, maintain development velocity while
*  still being very performant. And so when it became clear and, you know, OpenAI did a lot of good work
*  here in marketing the power of embeddings to people. And these sort of early use cases showed up with
*  document question answering. It became clear that, wait a minute, you know, there's thousands or
*  hundreds of thousands of developers in the world that are going to need something exactly like this.
*  And we essentially took what we built, packaged it up to make it a lot easier to sort of just get up
*  and running and then gave it to people. And people really seem to love it. Things have been really
*  exploding over the, I mean, it's kind of crazy to me because it feels like it's been out for a while,
*  but we launched it last Tuesday was when I announced it on Twitter. So it's kind of been a
*  lot since then. Yeah. Time is doing very weird things for me as well. I earlier this week,
*  I realized it was on Wednesday that I realized, wait, we just did that on Tuesday. And it was like,
*  oh my God, so many things happened in such a small period of time in the AI world that is
*  dizzying to say the least. Yeah. I feel like there's been a few step changes,
*  right? Over the last couple of years. I think I feel so first of all, I think GPT-3 was the
*  watershed back in 2020. And then stable diffusion, Dali, but stable diffusion was the next really big
*  one because it allowed people to see that, wait a minute, you don't actually need to own a huge
*  model. I can totally just run this on my laptop and get results and build things around it. That was
*  a huge watershed moment because it was open source and like small enough to run on an M1 Mac. You can
*  do it yourself. Someone was crazy enough to get it to run on an iPhone, which I thought was amazing.
*  And then the next thing that just recently happened was ChatGPT. And technologists will
*  tell you the same thing. People have been following closely for a while. We'll tell you the same thing.
*  They're like, oh yeah, the model was already available. It just needed fine tuning. Nobody
*  did a blah, blah, blah, blah, blah. It doesn't matter. What matters is it's packaged and given
*  the right affordances so that people can easily understand what it is they can do with it. And
*  then they'll start doing that and then they'll start experimenting. So I think those are the
*  two big watershed moments that happened in the last while that really makes it look like an
*  amazing playground for experimentation right now. So you mentioned a couple of things that I just
*  wanted to elaborate on a bit. One, it sounds like you guys are a neutral vector database technology.
*  So I can use any different provider. You mentioned OpenAI. Their pricing, just to give context on
*  exactly how cheap it is, because you said it is cheap. The cost to embed all of the transcripts
*  of every podcast that Joe Rogan has ever done, 100,000 pages of text, $40 to embed that 100,000 pages.
*  And if you wanted to go, this is from Boris Powerhoofs at OpenAI. If you wanted to go to
*  the full web scale data set of 10 to the 11 pages of text, then you're looking at,
*  he says, only $50 million to embed. So that's not nothing, but to embed the entire web scale
*  databases, it actually is amazingly cheap. So once you have a document or whatever it is embedded,
*  then you can also store those embeddings. You don't have to unlike the other APIs
*  that are generative and doing something new each time, the embedding is kind of a one shot. There's
*  no temperature setting. You're going to get the same thing out every time. So then you can store
*  it. And that's where your platform comes in. You mentioned that there are some shortcomings of the
*  things that were out there. So what shortcomings did you see and how did you address those in the
*  product that you've built? Yeah, those are great questions. I think the first shortcoming was just
*  how hard it was to get started with anything out there. We evaluated literally everything else
*  in the market, and it just didn't fit our needs of rapid development, rapid experimentation.
*  It was either too hard to deploy and keep running because it was really designed for heavyweight
*  workflows from day one, or it didn't really provide the kind of price performance point that
*  we needed, or it was just frankly too complex. Chroma for a long time was just me and my
*  co-founder, Jeff Huber. And we couldn't spend an entire full-time engineer's worth of work just
*  running the vector store part. We needed something else. And the other thing is, is we found the
*  abstractions were pretty wrong. There was also a bunch of missing features, which we just couldn't
*  figure out why they were missing. We just implemented them. There was a bunch of other
*  things too, which made it obvious that the affordances here were wrong. None of the other
*  products on the market are really AI native. That's the way we think about it. And that's because
*  if you have this app that's LLM enabled and it has a store, you need a much more transactional
*  approach. You need good inserts, updates, leads. You need to have it talk to the embeddings API
*  properly. You need to have it return the results in a way that the model is going to pick up easily
*  and then stuff them into the context window, all of these things. And we also saw in parallel the
*  growth of what we think of as application development frameworks for AI LLMs. Our friends,
*  Langchain, for example, we were a day one integration partner when Chroma launched with them.
*  We saw that, okay, the thing that we build has to actually fit what people are doing.
*  It shouldn't fit this abstract idea of vector database. It needs to be an app development
*  platform. It needs to be the storage layer for app development. And then it needs to have the
*  right affordances to think about this so that developers can actually think about it in the
*  right way. And those are the main differences. That said, it's pretty performant, making it go
*  even faster pretty soon. Pre-AI, what were the main use cases for vector databases that people
*  had built all these other things for? Yeah, look, the two big ones, as I mentioned earlier,
*  are recommender systems and semantic search. Embeddings are a concept that basically just
*  means take data from one high dimensional space and encode it as a vector in a lower dimensional
*  space. That's all embeddings really mean. It's actually not even a deep learning concept that
*  predates it by a long time. It's an idea in mathematics, which the name is loosely used now,
*  but that's pretty much what it means. And so there were a lot of, like I mentioned, especially
*  for natural language processing, like hand-tuned methods to convert words into vectors or convert
*  corpuses of documents of text into vectors. And then you would try to hand engineer these
*  embedding functions and then store them in a vector database and then query them and look them
*  up in a similar way to the way I've described. And what people focused on in that era was building
*  these really large scale data, like vector databases intended to work at very large scale.
*  So we're talking about being able to query billions of documents out of the box, being
*  able to search over billions and billions of images out of the box for these web scale,
*  huge applications. And at that time, AI just wasn't in the picture. Deep learning really
*  wasn't in the picture. So do you also have like a sort of SQL like aspect to the database where
*  you have a, could I do like a sort of equivalent of like a where clause where I'm like,
*  but I'm only interested in these, do you have kind of traditional B tree indexes along with the
*  vector space? Okay. That's right. That's right. It allows us to, so we have the underlying algorithm
*  that we use for the vector index and the index is the thing that actually stores the vectors and
*  the relationships between them. And then there's a metadata store and the metadata store stores the
*  data in like original more sequely form. And we have them talking to each other in such a way that
*  you can take something that filters the query that you perform in this very traditional way
*  and then turns that into a query onto the vector store. So I can say, you know, find me
*  all the matches to this query, but only from documents that contain this phrase. And like,
*  you can just do that with CoreLinux. So what are the things you said about the technology that
*  caught my ear was the, was the phrase approximate nearest neighbor search. So tell me about that.
*  That, that sounds, this also starts to preview a little bit the project that you've released and
*  made some noise on the internet with, which is stable attribution. Exactly. Your neighbor search
*  is, has like N squared complexity. Each time you add a new vector and you want to query it to find
*  out what the nearest neighbors are, you need to perform an N squared calculation. Like it grows
*  in the number of vectors quadratically, which is actually for certain, for certain sizes of data
*  is totally fine. Roughly, if you have like, I don't know, a couple of hundred data points, it's fine.
*  You should just be doing exact nearest neighbor. It's just one matrix multiplication. And that's
*  very fast. NumPy calls out to like very fast numerical libraries. You can just do a matrix
*  multiplication, keep it all in memory. It's nice and fast. You don't have to think about it.
*  The issue of course is quadratic growth is really bad. So by the time you have, you know,
*  north of 10,000 data points that N squared is really starting to hurt you. And this is where
*  approximate nearest neighbor comes in. And there are several of these algorithms, but basically all
*  approximate nearest neighbor algorithms are flat in the number of, or approximately flat in the
*  number of vectors in the index. So you no longer have this N squared term. Your query times,
*  regardless of how many vectors are stored in the index are going to be identical. But there's a
*  trade off. The trade off is you won't necessarily get all the nearest neighbors every time. You
*  might lose some. And that's a, that's called a precision recall trade off. And it's very similar
*  to other aspects of machine learning in that way. But in practice, in many applications like these,
*  that's a trade off that you can make. And the trade off isn't very severe. It's not like you're
*  going to lose half. It's more like you might lose one in every 100 queries. Yeah, interesting. Okay.
*  So that makes a ton of sense if you're working at a 5 billion vector scale. How do you think about
*  kind of, I mean, when you said 10,000, I was thinking, I'm sure I have more emails in my Gmail
*  than that. And so what would, how should I think about kind of these sort of mid-scale personal
*  datasets where I probably do want the full thing, right? Like I don't want to miss the one thing
*  that I'm, that I most need. So yeah, tell me in that mid-scale, what happens? Yeah. So you can,
*  especially for smaller datasets, you can tune for more recall. You can make it very unlikely
*  that you'll miss anything, but still get that good query performance. You can also trade off
*  processing upfront and sort of insert, you know, time to insert something with recall and query
*  performance, depending on what your workload looks like. Basically, if you have a lot of inserts,
*  if you want it to be fast, it's probably a good idea to, you know, tune it to be a little faster
*  so that insertion speed, a little bit of recall. If you're like, if you have like a set of data
*  and you really need to insert it once, do all the pre-processing on that side, you'll still get great
*  recall. So the tuning, it's interesting, there's multiple meanings of tuning. You're speaking about
*  a pretty classic database tuning paradigm, which is like, when exactly do we do stuff and do we
*  pre-calculate? So I had listened to your conversation with Paki on the Not Boring podcast
*  not too long ago. And actually, as I was listening to that, I thought you were tuning some sort of
*  learnable, you know, like fine tuning some sort of aspect of either the embedding or, you know,
*  the way, like which, so you're doing that as well, like which dimensions, you know, would be kind of
*  primary. So, okay, so tell us about that side as well. Yeah, so this is the other, this is the,
*  again, like I mentioned, one of the most important parts is you can perform geometric operations,
*  and because of the way that embeddings work, those geometric operations have meaning.
*  So for example, kind of the simplest example of this that I can think of is you can cluster
*  vectors geometrically, but those clusters will have semantic meaning. So if you have a large
*  corpus of text, and you look at what the clusters might be in it, and you look at the topics that
*  are in those clusters, that's information that like belongs together, because the model is trained to
*  keep things that seem together together, right? Clustering is like this basic first approach thing
*  you can do. Another thing you can do, and this is actually great for the question answering
*  application, we've been examining this in some detail lately, you can find a direction in the
*  vector space that represents some human understandable property. And it's actually surprising how often this
*  comes up. But for example, you could be talking about a topic, but you can be talking about it in
*  the context of a question, like who was born in year, blah, blah, blah. And then over here,
*  you could be talking about it like, oh, this king, etc. was born in blah, blah, blah. And so if you
*  find this like question answer vector, you can do interesting like remappings and bring things closer
*  together. And because it's just a vector space, it's this well understood, fairly straightforward
*  mathematical structure. The way to like transform one thing that you want into a different thing
*  that you want, or like, make it work better, fine tune it to get better results for you is actually
*  very straightforward compared to traditional machine learning. You don't need to do back prop,
*  you just need to estimate some transforms, which is something that we know how to do.
*  That sounds pretty similar in some ways to like classifier guidance almost, right? Like you're sort
*  of identifying a direction that is the direction from statement to question, essentially. And then
*  you can kind of move around, you know, you can you can place that vector anywhere in theory,
*  and kind of move from different, you know, statements to their corresponding questions.
*  Obviously, it's going to be a little messier than that. But, but there's also all kinds of other
*  things you can do directly by working with this. For example, if you have a system to get user
*  feedback about relevance of the return results, you can reweight your your space by applying a
*  learned transform on top of it to get ever more relevant results from human feedback.
*  In a very straightforward way, there's no model retraining that you need to do. Your model is
*  doing what it's best at, which is like understanding and recomposing knowledge. And actually, that
*  takes me on an interesting tangent here, which I really do want to indulge briefly. Right now,
*  we're seeing like, oh, chat GPT, and then GPT 3.5 and GPT 4 soon, which are these large models that
*  know things. And like they're trained on very large corpuses of data, they're very expensive
*  to train, they're expensive to fine tune. You don't really know what knowledge is in them.
*  But they're very good at general purpose tasks. They are, you know, they can do all kinds of
*  tasks efficiently for you with like zero short learning or like multi stage prompting. And I
*  think those models are going to be around. I think they'll continue to be there because there's such
*  great like, they're almost like utilities really. But on the other side, I think what we're going to
*  see is these smaller, leaner models, which are actually trained to find and compose knowledge
*  in response to queries, rather than store knowledge in their own weights. And we've seen early signs
*  of that. There's a paper called Retro, or there's a system called Retro. It's from Meta. Or is it
*  from Meta? I think it's from DeepMind. Sorry, I misspoke. Which where they trained a model to do
*  exactly the sort of stuff we're talking about, they trained it instead of sort of storing knowledge
*  in its weights. They trained it in such a way that it has to search for knowledge in this data
*  bank. It can't get knowledge from anywhere else except in this data bank. And that and you know,
*  that's I think that's one direction in the future. And we're starting to see the very first stage
*  that happening right now. And the sort of stuff we're building with Chroma really enables that.
*  So those transforms that you described, those are just like one layer, like you're basically
*  just learning one additional vector. For a while, there's been folk wisdom. And it's actually even
*  in the OpenAI cookbooks, OpenAI cookbooks, there's been this folk wisdom that a linear transform,
*  which is just a matrix multiplication, is enough to transform one embedding space into another
*  embedding space as long as the semantics are like broadly the same. And there was recently another
*  paper about this where they demonstrated that like, yeah, empirically, models tend to learn the same
*  representations of the same thing. So mapping between them is a straightforward operation.
*  And that kind of means that like that's that's very promising for being able to do things like
*  that and integrate it really well with with what we're building. Like relative representations,
*  is that the paper you have in mind? Or I think so. Yes. Yeah, that was a fascinating one. You see
*  these kind of I mean, obviously, it's a higher dimension than projected back down to an even
*  lower dimension for visualization. But you see these kind of shapes where you're like, oh, wow,
*  that's very strikingly the same subject to a rotation or, you know, a dilation or whatever.
*  I thought that was pretty awesome. You know, the clarity that they achieved in demonstrating that,
*  I thought was pretty cool. It was great empirical work. And honestly, I think more machine learning
*  research needs to take that empirical approach. I think machine learning people need to take more
*  cues from biologists and really observe what's going on first. There's one extra interesting
*  thing about you brought it up just now. You saw how like, oh, these embeddings seem to be
*  invariant to like rotations or scaling. Right. So there's a very interesting, there's a very
*  interesting potential approach here, which is obviously, you know, not obviously, but in
*  principle, you could find ways to maybe decode people's information from the vectors. So if
*  you're a provider of, say, cloud vector storage or something, and people are sending you their data,
*  you know, it might be a risk of you being able to read that and people don't want to know that. But
*  most of the operations that you perform in vector space are, like you mentioned,
*  invariant to translation, rotation and scaling. But that means that you can put your, even if I
*  know that your data came from, say, OpenAI's Ada2 model, if you apply like a random transform and
*  maybe add some noise, it's very, very, very difficult for me to recover that transform.
*  But I can still perform the same operations that you want me to perform in that space.
*  And we haven't evaluated this in depth. It's an idea that I had fairly recently.
*  But you can think of this as a form of homomorphic computation, because I can perform
*  computations for you without really knowing what your data contains. And I think that's a
*  really interesting thing as well. And that might be a whole direction on its own in a little while.
*  I mean, the security, I'm working on a couple projects where I'm like, boy, that actually
*  could be a great solution to an otherwise thorny problem of where exactly are we sending our
*  client data and who is seeing it in what form. So yeah, that's a really interesting insight and a
*  great connection. I mean, there's so many, the convergence of so many things is just striking
*  to me. We just did another interview with the authors of Blip, the computer vision model. They
*  just came out with Blip2. And Blip2 reduced the training computation requirements by 95%.
*  They were able to train the whole thing on a single machine in under 10 days. And
*  the reason that they were able to do that is because they kind of created an ensemble
*  approach where they had a pre-trained vision model and a pre-trained language model. And they
*  just trained this connector model between the two. I think they said it was 200 million parameters.
*  And what it predicts are text embeddings that are derived from the images. And so then they're
*  able to inject this representation of the image, skipping the embedding layer, just going straight
*  to injecting the embeddings as kind of a prefix to the prompt in a way that is... Well, the thing
*  that I thought was kind of most fascinating about that is they're accessing a part of that embedding
*  space that no text could in fact access. We talked quite a bit about is there any way to sort of
*  reverse that to what text would you have had to put in to get those embeddings? And they were like,
*  yeah, there's really no text that would create similar embeddings. We're just finding these
*  kind of weird spaces, but the language model knows what to do with it. But it's hard not to
*  see the analogy between the vision model being sort of the eyes and their model being kind of
*  some sort of relay layer. And then you get the language model seems like an executive function
*  of some sort. You're kind of doing a similar thing, right? You're connecting... Is that how
*  you sort of casually would describe it to people? Like the language model is kind of the
*  executive function or the sort of top level processing, and then you're helping
*  get into deep memory? I think that's a reasonable analogy. Yes. I think that's a reasonable
*  analogy. I think another paper that's in that vein, you've just drugged my mind, is Robotics
*  Transformer. RT1 came out from Carol Hausman's group at Google Brain Robotics. And what they do
*  is they have a perception subsystem that sits on top of everything, and then they have this planner,
*  and the planner just basically learns from these multi-head embeddings to
*  output plans and actions. It's really, really cool. It's kind of similar to the system that
*  you described. It's all coming together pretty fast. It's really an interesting time to be
*  working. I think that there's also just untapped veins of research here. The reason... We noticed
*  this very early on, even before we started Chroma, that the incentives between, let's say,
*  academic ML AI research and industrial academic AI research... And I don't mean universities versus
*  industrial research labs, because they're mostly doing similar work now. I mean more like the sort
*  of work that production machine learning deployments are interested in versus the sort of work that
*  maybe pushes you towards AGI is fundamentally different. And one of those big differences is
*  in academic research, there are accepted community benchmarks, and your aim as a scientist
*  is to demonstrate the performance of your model on these accepted benchmarks. But the benchmarks
*  are static, whereas in the real world, the data is always changing. And questions of like,
*  should I train my model? What do I train it on? Is it working better or worse? Monitoring it,
*  measuring it are of much more salience than demonstrating performance on benchmarks.
*  We founded Chroma with that observation in mind, that there's actually a lot we can do
*  and mine some of these rich range of research if we just focused on them in the first place.
*  Going back to nearest, approximate nearest neighbors, we talked about kind of
*  various things you can do where you can kind of pre-compute some stuff depending on your workload,
*  where you can learn these transforms to get more and more relevant over time.
*  Do I still have to worry if I'm doing that, that there's some sort of systematic blind spot in my
*  system? Like if I'm, you know, it just start to bridge to stable attribution.
*  If you've applied all these techniques, and I upload an image that I got out of stable diffusion,
*  is there any way that we could start to assess like, whether or not there's some sort of
*  systematic bias there? Or is there some part of the latent space that's like, you know,
*  being kind of unfairly not, you know, not brought to the fore in the attribution?
*  I think so. I think so. And actually, again, there's an experimental feature we're deploying
*  into Chroma very shortly, which will tell you the relevance of what's been retrieved. So you can
*  actually do something about it. You probably know there's like a two-step retrieval process as well.
*  It's called hide, where instead of just embedding your query, what you do is you send your query to
*  a language model. You let it hallucinate whatever it wants, a response, but it looks more like a
*  response. Then you embed that and do the query. But it's expensive. It's expensive to do two
*  large language model calls. We did some napkin math not long ago, and we figured out that, for
*  example, one company who we've been talking to, if they did it, if they did it even the vanilla
*  way, it would be hundreds of thousands of dollars per week, right? So reducing the cost of this is
*  actually really important. And so what we realized pretty quickly was we could make this hide approach
*  more efficient if we could algorithmically figure out when the results would be relevant or not.
*  So we're deploying that very shortly, and it's a very general idea that I think people also
*  integrate into their app development flow. And again, because all this stuff is geometric and
*  nicely continuous, we give you a probability instead of just a threshold. But again, pretty
*  much everything we're talking about, more research, more work needs to be done.
*  Tell us, give us the brief overview of stable attribution. And then those who want to go
*  deeper on that topic specifically definitely recommend the show you did with Paki on the
*  Not Boring podcast feed. But give us the kind of short overview and then I have some questions
*  that you didn't get to cover on that conversation. Absolutely. So the short version is fairly
*  straightforward. We saw a need and a possible technical approach to figuring out, or at least
*  starting to figure out how images in stable diffusion's training set influence particular
*  generations that are creative. And the way that we did that is by doing various, by extracting
*  various information, both about like, like, just similar images to a given generation, the training
*  set, but then also like figuring out what the right similarity is. And the reason we took this
*  approach is again, because there are optimal approaches, but they are all computationally
*  intractable. For example, like one more optimal or more principled way to do this might be to
*  remove examples one by one until, until and like retrain the model every single time, until, you
*  know, the image has gone far enough away, you say, okay, those images influence the most.
*  But of course, every training run of stable diffusion costs about 160 grand. So it's
*  computationally infeasible, we found a different approach, we think it's principled. And we applied
*  that we leverage other, you know, various properties of how diffusion actually works
*  alongside like similarity and latent space. We construct like a, what we think is a principled
*  similarity metric and go from there. Cool. So give us just a little bit more of the
*  principles behind it, at least. And then then I'll get into a couple of questions.
*  Yeah, sure. Assuming, you know, assuming the audience here knows basically about how latent
*  diffusion models work, they're trained in their training set, they have image text pairs,
*  and they're trained to reproduce and the same encoded latent as the training example
*  through the diffusion process, they're trained by iteratively adding noise to the training examples,
*  latent vector representation, and then training a network that reverses that noise. And what's
*  great about it, what's actually the big breakthrough is this is very efficient, both in terms of how
*  much data is used by each dimension in the vector, but also because you can train in parallel,
*  each denoising step. That's the big thing. So, you know, there's a few parts to this.
*  The starting point is like, okay, well, given that the model's training objective is minimized,
*  if it can exactly reproduce the latency of all of its training examples, and because we know that
*  the latent space is continuous and smooth by definition, because that's how backprop works,
*  you have to be that, then it's not unreasonable to say that training examples that are near
*  the generation in latent space in some way are influential to the output of that generation.
*  That's where we started from. We took a look, we found out a bunch of interesting stuff.
*  We found that, for example, there was a bunch of papers that demonstrated that actually stable
*  diffusion totally can reproduce exactly, or very close to examples in its training set,
*  which people denied for a long time, I don't know why. Now they tell me, like, oh, you can
*  reproduce a tiny number of examples, like, that's not what you were saying before. But anyway,
*  we found that noise in the training set is definitely something quite interesting here,
*  because the clip representation of images and text might differ, for a given example,
*  and you can imagine why the same image might have a lot of different captions,
*  even in different languages, and then a lot of the data is just noisy. So we took that into account,
*  and we took into account the sort of the attention mechanism of the diffusion model itself by
*  constructing attention maps, and attention maps are actually, like, if you look at them
*  at a slightly different lens, they're actually just, again, a matrix multiplication. They're
*  a linear transform of that vector, so when we apply the attention map, we get, you know,
*  it's as if we're transforming the latent space, and then we can do similarity search in that new
*  latent space. That's, like, a very short overview. Cool. So yes, again, for more depth on that,
*  go to the not boring, Anton teaches Paki about AI, episode six, and there is quite a bit more
*  detail there. So just kind of zooming out from the technology a little bit, I naturally went
*  online and tried it, and I tried it with a mix of images that I have made with stable diffusion.
*  I know that it's not really meant to be used on natural images that I took on my phone,
*  but of course I tried that as well, and it does work, and either way, you do get images back that
*  are similar. The divergence definitely between the real images, like stuff on my phone and what comes
*  back, is bigger, and I think you have an explanation for that around kind of why it doesn't
*  come back with so similar images, even though I mentioned that they must exist, right?
*  Yeah, so here's the interesting point. The similarity is not perceptual human similarity,
*  it's models. It's how the model perceives the difference. That's an important thing to note.
*  When I say influence, it's not necessarily the same way that an image might influence
*  a human artist, where they will draw motifs and inspiration from it. It's more like this very
*  mechanical, raw interpretation, like these vectors are the same, right? These vectors are similar.
*  So to a human perceptual system, once those images are decoded from their vectors, they might look
*  pretty different, and you won't know what's similar about them. But we know for a fact that
*  ML models are kind of weird in the way that they think, quote unquote, about the world,
*  and they might represent something quite differently to what a human would. They might
*  focus on quite different things because they are mechanistically pursuing an objective.
*  They are not trying to encode any meaning. And I think that's what produces surprises.
*  I think one way to think about what you get back with inserting images that are not from
*  stable diffusion is if stable diffusion had produced this. So if it were possible for the
*  model to produce this, or put another way, if you like, if the model had produced this image with
*  a corresponding caption that was appropriate to it, here's what would have been in the training
*  set. It's a long chain of counterfactuals. It's not really meaningful. So here's the thing, right?
*  And you can go look at this. Anyone can. If you go to GitHub and you look at the stable diffusion
*  code, whether version one or version two, as provided in the open source repo, there is a
*  watermark function there. That watermark is not present in most hosted versions of stable diffusion,
*  and we don't know why. Or at least if it is present, people don't tell us what the watermark
*  is, and we don't know why. That was our plan originally to sort of reject non-stable diffusion
*  generated images, but it's just not present, and we felt that better to release and get feedback
*  than not. Yeah, you know, actually, I think there's an interesting, it is an interesting
*  experience when I used my real, you know, taken on my phone images. The results were kind of,
*  you know, I don't want to use this term, but it's the only one that's coming to my mind. I know it's
*  loaded, but it almost did feel like the pieces that were kind of collaged together to make my
*  actual real image. Like I tried one where it was just my kids saying goodbye to their friends at
*  our front door. And what I got back was not like all, you know, kids at front doors, but you could
*  see these like elements that were very resonant across the images. And I felt like, you know,
*  there's almost something here product wise that is kind of interesting. Like it's a sort of diverse
*  image to image search that like picks up on these kind of notable aspects. Have you seen, I think
*  it's like same vibe or something like that. It's like essentially that it's like, I'm like, I'm
*  it's like essentially that it's like a mood board search engine that I think uses similar
*  principles under the hood. I think there's a bunch of ways that you could take this. I'm actually
*  like, I'm curious, you know, if we do keep doing experiments in this direction, maybe we will right
*  now, obviously we're focused on other things. I think this is a great chance to turn like
*  generative models into something besides a one way process. Like if you can manage to do these
*  kinds of relations, you can really start to use them more in like a search or an iterative
*  or iterative conversational search type of approach, which I think is really interesting.
*  But yeah, like the thing that you're getting back is like, okay, this is how the model sees your
*  image almost. This is like what it would have tried to do if it was generating it.
*  It is cool because it does have this sort of, it sort of reflects back to you like,
*  these are the things that made your image distinctive in a way that you couldn't necessarily
*  have articulated yourself. But like, oh yeah, I see like my kid in this picture is like turning
*  over his shoulder and looking a certain way. And like this other image is like quite different in
*  all the other respects, but it has that same like pose. So there's some like feature that they have
*  like very, you know, very much in common, even though like the other features are very much not
*  in common. I actually would recommend that people go try their real images on your search, even
*  though it's not what you necessarily meant it to be. Please don't yell at me if you do that.
*  Yeah, FYI, it's same dot energy is the same dot energy, same dot energy. I really like that.
*  I think it's fun. Okay. So let's return to the intended use case. So you put an image that you
*  made with stable diffusion into the product. It does its searching and, you know, principled
*  extrapolation of the search comes back with images. Sometimes I see a few, sometimes I see a lot.
*  I was really left wondering, like, how are you deciding how many to include? Is there like a
*  certain cutoff? Or are you kind of doing like a top P type of thing? What are those distributions
*  look like? Yeah, that's a really interesting question. It's something we've tried to instrument,
*  but it's again, one of those things that you need a lot of data to figure out, and a lot of compute,
*  which we're not applying to this right now. But it's interesting. You're right. Sometimes you get
*  not many matches, and sometimes you get quite a lot. And I think that that depends on where you land
*  in this like modified similarity space that we talked about. Like you mentioned earlier,
*  with the language model where it can like generate reasonable text from places that are nowhere in
*  its training set. You can think of this almost as like a dial maybe from the model reproducing
*  stuff to the model generalizing. Right? If you can kind of maybe look at that from that lens. And
*  the thing is, is the stable attribution algorithm really doesn't take model generalization into
*  account. We're trying, we're like leaning really hard on this like reproducibility rather than
*  generalizability. And there's a lot of questions to explore there. And I think that though we'll
*  get explored because we're going to look for ways to continuously improve the performance of the
*  models outside of the scaling laws. Although a lot of, you know, the labs who have the most compute,
*  they will keep pushing on the scaling laws. The labs who are looking to just, you know,
*  do something interesting, or even at the product level, people are looking to do something
*  interesting. They will experiment with stuff like this and be like, oh, okay, I noticed that like
*  this part of the generative space doesn't have much in it, but people are asking for a lot from
*  here. Maybe we should like go out and get stuff that people want from this part of space and then
*  like get people to actually make images for it. It's an interesting possibility for the future.
*  So when I do get those results, is it fair to say, I think you said this on the
*  Paki show that the, you know, everything influences everything, this space, right?
*  Because like everything's involved in gradient descent at some point. So in theory, if you had
*  the kind of fully principled answer, they would all be, you know, infinitesimal, but probably non
*  zero. Yeah, it's an interesting question. I'm not sure that that's quite right. I don't think that
*  they would necessarily be infinitesimal. I think that different generations will draw from different
*  parts to greater or lesser degrees because of the training objective. Further, things that are
*  further away should naturally not influence the generation from a particular conditioning
*  caption as much as things that are related to that conditioning caption. I think that like,
*  I think that's also a pretty interesting question because one open question is in what way does
*  generalization actually influence the output? Like we can't, we haven't looked at that. I think that
*  you could do this kind of research with a toy model and really see like, oh, you know, just have
*  a tiny diffusion model, make pictures of flowers or something, and actually just literally just
*  burn a bunch of compute on figuring out like, okay, this is like proportionally how the data
*  set actually does influence things. I think there's another really interesting approach here,
*  which you can take with a toy model, which is basically like compare the stable attribution
*  approach with like the gold standard and see how good or bad we actually are. If we had GPU time,
*  we would just do that. And then I'd be like, okay, yeah, everybody was right. This sucks. Or I could
*  be like, oh, actually, no, this is really great. And I have numbers now. But until then, it's,
*  you know, these questions are pretty hard to answer. So in the process that you're running today,
*  does it generate a score for each image that it finds? Like they're ranked, right? Does that have
*  a clear relationship to like the whole? Like do those sum to one or do they sum to anything
*  that you know what they sum to? I mean, it's, it's, there's, there's some metric in space. It's,
*  we treat it more like an ordinal thing. And then you sort of, you know, you can get a proportion
*  out of that by say, take the top end and then you divide evenly according to, according to
*  the similarity metric, but it's not that meaningful. It's much more of an ordinal question. You can say,
*  okay, these, these are like closer, these are further apart. So then what is happening when
*  there are no results? Like you also have a threshold below which you just are like,
*  nothing is close enough to this. There's a few filters going on.
*  Behind the scenes, we have a threshold where we just stop looking, you know, it's pointless to get
*  things that are far away. We say that, okay, really only this condition be regarded as influential.
*  It's an arbitrary choice. It's a heuristic. And again, that's like, okay, well, here the model is
*  really like extrapolating and filling the gaps. So we'll leave aside for the moment, the like why,
*  you know, Elizabeth deep dive into the why behind you did this, behind why you did this and the,
*  you know, the vision for, you know, sort of an economic dimension to this attribution that could,
*  you know, one day come to exist. Again, you talked about that in the recent show. So
*  I don't want to rehash it, but I wonder like, to what degree this is separable. Like I was
*  just running this thought experiment where I'm like, okay, let's say I have a stable diffusion
*  image and, you know, Greg Grekowski is in my prompt. And it's amazing. Like you go on these
*  sites and you look at the prompts and it still feels like one out of every three as like Greg
*  Grekowski, you know, by name. I think it got stuck in people's heads as well early on. It's amazing
*  how like the very early things that people discovered, they just like become gold standards,
*  even though it could have been anyone, it could have been any choice. There's plenty of concept
*  artists working today. It's kind of, it's, it's just one of these odd artifacts of internet culture.
*  I guess I'm wondering, like, if you had something, if you were able to kind of peel
*  back, right, and they're doing this now with stable diffusion, like they, you know, they've
*  got this opt out mechanism and all that kind of stuff. To what degree is everything sort of
*  meshed together and not really separable. So like a thought experiment would be,
*  let's say you took all the stock photos and then you added all Greg Grekowski's real art.
*  Do you have any intuition for whether I could still get Greg Grekowski stuff out of that?
*  Or do I need like a richer denser space? Yeah, look, this is exactly the kind of research that
*  needs to get done. It's exactly the kind of research that hasn't been done to this point,
*  because we've all we've been working towards capabilities of these models.
*  And we need to start looking at like, okay, like controllability engineering principles.
*  The way that I think about this is in the early days of aviation, we had like intuition about
*  what makes airplanes fly, right? We had, you know, the first powered flight, the Wright brothers
*  were wrong about how the Wright flyer worked. They just had intuitions about it. And it flew,
*  that's an object demonstration. It doesn't really matter if your intuition is wrong,
*  if the thing works. And then there's this Cambrian explosion of different types of aircraft. People
*  were putting two, three wings on them. People were, you know, experimenting with different
*  materials, different fuselage shapes. You've got things that look like birds, things that look like
*  crazy fans in a tube, because we all we had to go on was intuition. We didn't have engineering
*  principles yet. And we didn't even really have the tooling to develop this. That's where we're at
*  today, in my opinion, with machine learning. We have a whole bunch of intuitions, we kind of know
*  how things work. And what's really interesting, and this happens very frequently is like some
*  paper will assert, and you know, even with stable diffusion, even even with like,
*  latent diffusion models, they were like asserting, oh, this is like, like event
*  thermal diffusion dynamics. And the paper came out the other day, it's the things called cold
*  fusion, or something like that, or cold diffusion, where they're like, no, it's not. Here's, here's
*  an object demonstration that that's not true. We're in that era of just experimentation. None of this
*  stuff is like really well understood. And we're seeing the early days of people trying to develop
*  principles, the scaling was the first thing, where it's like, okay, well, we're going to
*  empirically demonstrate that you need to increase data as much as you increase compute, otherwise,
*  it's worthless. That'll develop further until we probably get to a point where we can actually
*  design the things that we're building for the mission that we're intended to perform like we
*  design aircraft today. Because we've, you know, and we still don't know everything about flight,
*  flight is a very complex discipline. But we now have the tools and we have enough experimental
*  sort of evidence. And we have enough, you know, laws of physics that we can really like build
*  pretty amazing aircraft. But it took a long time. Yeah, for what it's worth, the sense of human
*  credit, but the David McCulloch Wright Brothers biography is pretty short, and absolutely fantastic.
*  I could not recommend that. Would you send me that? It's very striking just how, you know, these two
*  brothers cared about basically nothing but doing the work. There was, and their family, but they
*  really did not. There were a lot of folks out there who were like, hyping themselves up as the great
*  experts in flight. And they never actually flew anything, despite their, you know, supposed expertise.
*  And these two dudes just, they put their heads down and they just did the work until they actually
*  had the goods. Yeah, and then they milked it, then they milked it through intellectual property law
*  just as far as they could until Curtis blocked them. It's kind of a Greek tragedy, honestly.
*  It's interesting that that's not as much covered in the book. So maybe I'm missing
*  some of the less flattering aspects of their story. If you have any take on the kind of technology
*  angle, you know, I was thinking also as I was doing this, you go through all these prompts and you just
*  see, you know, 4K, Unreal Engine, you know, Pixar style, you know, red brand cameras. And, you know,
*  envisioning your kind of imagined future of like, people getting, you know, some sort of
*  economic remuneration for their contribution to this. Do you think that like those sorts of technology
*  layers also have a claim? Like, it's interesting. I think that's interesting. That's a really
*  interesting point. So first of all, like for me, as somebody who works in this discipline, prompt
*  engineering kind of feels like, and I've said this elsewhere, kind of feels like trying to pick
*  a lock with a wet noodle. Like there's a behavior that you have that you want the model to do,
*  but the only interface you're using to the model is like literally typing text into it when what
*  you really want to be doing is like have feedback mechanisms inside it, like, you know, the control
*  systems like we have an industrial machinery or an aircraft. So like, what actually is adding 4K
*  doing? Open question. Nobody's like, it hasn't been answered. This is more of that kind of research
*  that I'm talking about that needs to be done. Like what I like, why does 4K matter? It's kind
*  of like with, with Instruct GPT, why does telling it that it's the world's expert in something make
*  it produce better answers? What's actually happening? And the danger is anthropomorphizing
*  these models. It's like, oh, it's thinking better. It's not a person, it's a machine.
*  Dissect the machine, see why it's doing that. Where is it going in its latent space? All these
*  models are, are encoding and decoding the latent space. To answer your next question, like, you
*  know, how do you attribute rights holders to equipment? I mean, you know, it's, that's
*  barely settled. You don't. Although, you know, it could be interesting. Personally, I'm not a huge
*  fan of adding additional copyright law or additional like strengthening derivative work IP law.
*  One of the reasons that we did this project was we didn't want Disney to own everything forever
*  in the inevitable copyright backlash. Cause you can imagine like, okay, derivative work,
*  copyright law gets strengthened. And then the next day Disney says, well,
*  anything vaguely superhero looking is in the Marvel universe. So I'm sorry, you can't draw
*  pictures of that anymore and put them online. Sorry. That's one of the reasons we actually
*  released this is just, you know, it's actually a line incentives here. I hadn't thought about
*  that angle. I think traditionally sort of the medium is, is elided. I don't think that people
*  really have claim to images based on the equipment used to capture them. Could be different here.
*  I don't know. I can't say that I have an opinion. Yeah, I don't really either. And it definitely,
*  you know, I would agree. It seems quite settled when it comes to, you know, the photographers own
*  their work and they, you know, they bought the camera and that's kind of the end of that
*  transaction. But this does feel like it could be different. You know, the, certainly just the
*  number of times you see that as you go through the prompts, those kind of suggest like, gee,
*  there is something to that, that is, you know, highly desirable that they've kind of created
*  that, you know, people have a hard time getting without them. So I wouldn't be surprised if the,
*  you know, the red camera makers attached to something at some point. Look like, I mean,
*  I think maybe it's something similar to how photographers will share, you know, their
*  equipment. They will say, this is how I captured this photo, right? They still captured the photo,
*  but there's some credit to the equipment they use and so that other photographers can learn from them.
*  I don't know, like could be. Yeah. It's a lot of free advertising for them right now as well. So they,
*  they might not want to opt out. Prompts are like this first, the like zero stage of like
*  attribution. Like if you're typing Greg Ryszkowski, you should probably like credit the guy somehow.
*  The, the role, the importance, you know, the problems associated with noise, I think
*  been one of the concepts I've been thinking about the most since I listened to you talk to Paki. And
*  you know, you said that for one thing, these massive web skill data sets, like you have a
*  lot of image taxpayers where there is high similarity. And that basically means like the
*  text describes what is in the image. And then you have a lot where, you know, it's kind of like
*  a totally different thing that may have nothing, almost nothing to do with what is actually in
*  the image. And that just serves to add a ton of noise to the, to the data set. And then you're
*  kind of extending that to say like that noisy portion of the data set is helping it generalize.
*  I don't have a great intuition for that. So I'd love to understand your thinking there a little
*  better. Yeah. So like in let's say old school machine learning, even though it's been around
*  since 2015, pre in the prehistoric times and the times of our forefathers, one thing that people
*  noticed very early on was that neural networks were very important to overfitting. And the way
*  to prevent overfitting was to inject noise into the model's training loop. So what you would do
*  is like dropout was a very common thing where you just like disconnect connections between neurons
*  while it was training so that it didn't like not relying on any specific connection too much or,
*  you know, all these, all these little tips and tricks and techniques, which kind of got
*  obliterated by, by just scaling, just make them just make the model bigger, feed it more data.
*  But at the time, this was like a huge issue, right? And so the way to maintain generality
*  so that the model, like once you evaluate it on your test set, still performed well was to
*  inject noise. Like you, you know, you'd fuzz the images, you would like flip them around,
*  try to do like plausible things that might exist in the real world. And so that's the analogy that
*  I draw here. Noise leads, seems to lead to generalization in some way. It seems to allow it to,
*  when the text and the image are not very related, it seems to,
*  it seems to grab something conceptually here from those images. It's like, it's, it almost picks
*  like supporting structures out of them without necessarily attaching the associated meaning.
*  That's just an intuition that I have. I can't say for sure that it's real. Another way to look at
*  it is like, you can imagine one image, many captions. It allows the model to come to the
*  same image for many conditions. Right? Imagine, imagine you only actually had one image, but you
*  just train the model on one image with many, many different captions. It would always end up in that
*  image, regardless of what, what like you put into it. Maybe that's also helping like weight
*  the kinds of generations that you get. Like it suddenly, it suddenly is able to connect
*  one image concept with many textual concepts. Things like that might, might be helping it.
*  Again, this is exactly the kind of research that needs to be getting done. Well, hopefully I want
*  it to get done. I don't know if other people do. The target rich environment right now. That's for
*  sure. If, if we go, you know, an hour and I am able to, that's almost like my KPI for this show
*  is how many times I can get our guests to say that that research needs to be done. I think we're at
*  like three, so I'm doing all right today. So just briefly going back to your, your product with
*  Chroma and the vector database and you had said at the top, you know, there's all these sorts of,
*  all these different kinds of things can be represented as vectors. So we've largely talked
*  about text, which is going to drive this like retrieval future where the AI is going to have
*  seemingly like photographic recall of all of our emails and our interactions and so on.
*  Even better than that. Put that information together in a way that actually answers the
*  query that you have, answers the question that you have, or like fits the context that you want
*  it to operate in. So what else is getting embedded these days? Oh boy. I mean, you guys have
*  probably obviously heard of whisper before you have a podcast. So yes, whisper is audio embeddings.
*  Anything, basically any modality that you can stick in your own network onto and preferably
*  a transformer at this point onto you, you can get embeddings from it. So we've got audio already,
*  we've got video. I've been speaking to a couple of people who have been working on that and
*  actually starting to get commercialized to video embedding. So you can do
*  semantic search inside a video. You can be like, find me all the footage from this party that's
*  actually fun to watch and it'll just do that for you. So video, and I think it'll just,
*  I think it will keep going. I think that we'll see over in robotics, for example,
*  like chains of actions are also embeddable. Like, oh, the person performed this task,
*  that's embeddable. Lots more like that. Basically all kinds of modalities will continue to get
*  embedded. And I think what will continue to happen as well is, so we've talked about clip
*  contrastive language image pre-training. We'll see more models train that way. So right now we
*  have like whisper, which is text to audio in the same space. And we've got clip, which is images
*  in the same space. And we'll have video and video and text in the same space. But then you can also
*  sync it's like audio to video. You can think of images to audio, that whole matrix of things.
*  And each one of those entries in that matrix is a potential application of one kind or another.
*  Which is a really exciting thing. Are you seeing things also like from biology starting to get
*  embedded? I was thinking genomes and protein structures. Yeah. Biotech, I think is waking
*  up to this. Biotech is a very interesting field to think about this in, because in biotech,
*  you kind of have to get it right. It's okay if your semantic search returns things that only kind
*  of look like the thing that you wanted in bio, you really need the protein to be the one you
*  were looking for. But the other part of this is in bio, most of those embedding functions that
*  we talked about at the top of the recording are still hand rolled. Very few are actually
*  trained and modeled. And I think we've seen the success of this in these other domains that we've
*  talked about. And I think biology is starting to wake up to this whole possibility. And so I think
*  in the next year or two, we're going to start seeing a lot more work in this direction. And
*  I've been talking to sort of biotech founders and companies and people working in this space, and
*  they're all very interested to see what can be done here. You know, I've been using the phrase
*  Kurtzweil's revenge increasingly often over the last year or so. And that's probably a good bridge
*  to kind of the last topic for today. Are we all going to die or what's going to happen? Yeah,
*  that's a good bridge. That's a really good bridge because you brought up Kurtzweil. And one of my
*  favorite things about Kurtzweil is I went on the website not long ago, and it was like the 10th
*  anniversary of the singularity is near. And that just, I don't know, that made me laugh. So look,
*  I don't think we're going to die. I have yet to see a convincing argument that we're going to die.
*  Every argument that I've seen in that direction requires some sort of system of basically
*  incalculable and definitionally like incomprehensible power, which, okay, like if you're
*  going to invoke magic, you might as well just do that at the start. I think that there are dangers.
*  I definitely think that there are dangers. I don't think the dangers look like
*  AI super smart overlords pursuing human unfathomable goals. If you're concerned with that,
*  you should probably work on sun alignment because the sun is giant and incomprehensible goals and
*  is very dangerous to humanity. But it actually exists today. What I'm more worried about is,
*  these are like cycles in history and you see them repeatedly. We see them with the inventing of the
*  printing press and then radio and then television, significantly destabilizing to society and often
*  either like very, very violent period. So the 30 years war is the one I always come back to. And
*  the 30 years war in part was triggered by the printing press. Martin Luther was able to spread
*  his ideas very quickly throughout Europe because they could be printed. And that caused layers
*  in power to be able to attach to this movement and they produced a schism. And then parts of
*  Europe were 50% depopulated in a matter of a few years, which is incredible. It's still,
*  per capita, the 30 years war is still the worst conflict in Europe, in European history, per
*  capita. And then you have the rise of totalitarianism, which was, you put the radio,
*  you put a radio in everybody's home. Suddenly a person who wants to be a dictator doesn't have
*  to walk physically from city to city or just convince you through text. You could hear it or
*  raiders. And I think it takes time for societies to develop basically like what I think of as
*  mimetic antibodies. I think if someone heard like Hitler ranting on the radio today, they'd be like,
*  damn, this guy's crazy. Although we do have that. There's a few people who are still pretty
*  persuasive, but it takes time. It takes time. And there's also this bizarre thing that occurred in
*  my lifetime, which still deeply confuses me. Back when the web first came out, everybody
*  knew not to trust it because people were like, Oh, anyone can put anything on there. Don't trust
*  anything you read on the web. People can just lie. And that has never changed. You can just
*  still go on the internet and lie. And there's that famous meme backer. But people seem to have
*  regressed. People seem to believe what they read online more readily now. And it's almost because
*  it got legitimized as an information distribution mechanism that people lost that immunity.
*  And the reason that I bring this up in the context of AI is because like you can imagine
*  very concrete use cases for even something like chat GPT, where you can have like,
*  finally targeted down to the individual propaganda, we've seen the success of like,
*  social media and doing this, like ad targeting, being able to be really mobilizing for like
*  elections in the United States and in other countries. I think at the point where you can
*  create tax that's individually targeted and kind of like start hacking people's actual
*  preferences to get them to vote for you or to like incite violence or any number of things.
*  That's that's kind of dangerous, but it's not the AI. It's the people running the AI.
*  There's another interesting thing, which I've been speaking to a few people about,
*  and I'll sort of mention in the abstract, which is like, there are dangerous things in the world,
*  which are still gate kept because the knowledge of how to do those dangerous things is very
*  difficult to come by. But if you have this like reasoning machine in your pocket, you don't have
*  to be smart anymore. You can ask the smart reasoning machine that you have to do the dangerous
*  thing. And so that's another like that's another real possibility. I called it a knowledge
*  capability somewhere. And I've been getting, I've been trying to get chat GPT to tell me how to make
*  a neutron initiator, which is a classified component of a hydrogen bomb. It won't do it.
*  These things never let me get my work done. These are things these are things that are more worrying.
*  And then these are just the things we can see. I think the destabilizing effects of new media
*  technologies are always unexpected as well. And I think we're in a very early stage. So we need to
*  kind of be vigilant about this stuff. I think that's that's kind of the perspective. I don't
*  think we're going to die. But but I think, you know, it might be a dangerous and then in the
*  in the sort of the cursed sense of interesting times.
*  Yeah, that seems to me that's kind of why we called this show the cognitive revolution.
*  That seems to me kind of baked in at this point, you know, the from my survey of the AI landscape,
*  you know, we've talked from a couple different angles about how kind of the same architectures
*  are working for everything, all this progress is happening in parallel. And, you know, we're
*  talking to folks like yourself who are chipping away at kind of, you know, and I don't think,
*  by the way, I don't think anybody really thinks right now that the core technologies like the
*  fundamentals are going to stop right where we are, you know, or that there's going to be no new
*  insights or no, you know, architectural improvements. I expect that too. But even if I kind of rule that
*  out, I think, geez, the core stuff right now seems powerful enough to be transformative.
*  It hasn't been productized. It hasn't been, you know,
*  saying that the rough edges are still there. They haven't been sanded down. It hasn't been,
*  you know, connected to all the other things really new being, you know, I'm still on the waitlist,
*  for God's sake. You missed the fun part. I know. Well, yeah, for better or worse. But
*  these things are all going to happen. Right. And so the impact to me seems like pretty baked in.
*  I think we're in for a wild ride that we're really not ready for. I don't think there's
*  ever been a time in history where someone's been like, okay, guys, get ready. We're going to press
*  this button that everything's going to change. But I think that actually speaks to our resilience
*  as a species. That's still literally true. Every single time that's happened,
*  we've come through it. And, you know, some people take the perspective that this is a unique risk.
*  I think that the actual risks that exist rhyme pretty strongly with other times we face them.
*  So I put that not in general as like a statement like, oh, we'll be fine. We've always been fine
*  before. It's like, no, I think we'll be fine because the actual risk we're facing rhyme with
*  risks we have actually faced before. The way what you put right now, I think is actually a good point
*  and people working in like, broadly speaking, the realm of AI and AI safety. The sort of the
*  consensus is even if we stopped training and developing new models today, we would keep finding
*  new uses for the models we have today. Like if you see how people experiment with GPT-3 and 3.5,
*  like discovering that you could ask it to think step by step makes the answers better.
*  It didn't require training a new model. You're just literally like, oh, this thing can do that.
*  They call it a capabilities overhang if you're in the sort of space, safety space. So yeah,
*  we could literally stop training right now and still not know everything we can do already.
*  Yeah, there's a lot of capabilities. The capabilities overhang is vast. I'm really
*  uncertain whether or not we're all going to die. But I definitely don't rule it out. And I'd like
*  to hear your kind of response to, you know, I'll just give kind of a superficial like high level
*  version of it. But I would say, you know, if there's like a canonical argument at this point,
*  I would say it's probably a Jaya Katra's post, which is called, without specific countermeasures,
*  the most likely path to AGI likely ends in disaster.
*  Could you also link me to that post after this chat? I read, I genuinely read a lot of this
*  literature. I read Eliezer's thing, AI Doom. I like I've read, I think people are always surprised
*  by how much less wrong I've read and how much alignment forum I've read, given what my position
*  actually is. I'd be curious to read that. But you know, what is the argument that is advanced there?
*  Well, there's a lot. So you know a lot of there, they can be subtle. But this the way that I like
*  to summarize it for folks is what she describes as the most likely path to AGI at this point,
*  she calls human feedback on diverse tasks. So kind of a generalization of the reinforcement
*  learning from human feedback to more and more different kinds of tasks and likely multimodal
*  types of tasks. The challenge that she sees that does seem to me really hard to dismiss,
*  not to say that I'm like sure that it plays out this way, but I really can't see a great reason
*  why I should be confident that it won't, is just simply that we are not reliable raters.
*  The people doing the evaluation have these flaws. And we know from kind of the heuristics and biases
*  literature, the cognitive, we know that people are flawed. In fact, there's a Richard No from OpenAI
*  has this great paper called alignment from a deep learning perspective. And he brings up a lot of
*  these great examples, actually, he brings up examples where like the model actually fools
*  the human radar, because it looks like it's performing a task on camera, but it's actually
*  just faking it. So yeah, like, okay, so far, so good. At some point, it seems like, you know,
*  these models are getting pretty smart already, right? Like they have increasingly they're,
*  it's like now in debate whether or not they have, you know, effective theory of mind, so on and so
*  forth. It seems like it's not too much of a stretch to get to a point where the models will
*  maximize their feedback score by not being straightforwardly, you know, truthfully,
*  honestly doing the task, but instead start to develop a model of, well, here's what reality is,
*  but here's what this person is likely to give me a score for. And so then you kind of create this
*  incentive for the thing to begin to deceive. And if you create that, you know, environment where
*  we don't have the interpretability chops right now, obviously to detect if it's there, certainly
*  with any reliability, then it seems to me like you really are playing with real fire.
*  There's a leap of logic being made here. So we have a model, it's performing a task that's valuable
*  to humans, we're rating its performance on the task. First of all, if it's performing the task
*  that we asked it for, and we're rating it on that task, what is the difference between it doing it
*  deceptively or correctly if we can measure the outcome, right? And I don't mean in the sense that,
*  oh, human raters, et cetera, I just mean in the sense that like, it's either doing the thing we
*  want it to do or not. And so in the example, in the like deceptive examples from that paper that
*  I mentioned, well, yeah, okay, it wasn't really raising the ball, but also there was nothing
*  riding on it raising the ball or not, except our benchmarking of this model. That's the first part
*  of it. In engineering, the real test is, does the machine perform the task instead of just in a test
*  environment, but is it actually doing what it's supposed to be doing, right? And this is where I
*  come from in the thing that people call, seem to call alignment in AI research is called control
*  theory everywhere else. And these things are dynamical systems that can be understood. They
*  have actually some really nice characteristics that allow us to understand them as dynamical systems.
*  And we know how to build controllable dynamical systems. That's why the F-16 can fly at all,
*  is because we know how to do this. The other leap of logic that's being made here is like, okay,
*  well, it's deceptive to human evaluators. It can hack their reward function. How does it follow
*  from there that we're all going to die? What is the path that actually happening? I've never heard
*  a clear example of this that doesn't invoke some sort of other form of calamity that if you're
*  worried about, humans could just do that. You don't need to worry about the AI. You can just
*  worry about the calamity itself. I get this thing where like, oh, it develops an undetectable nerve
*  toxin that triggers once it's implanted in every human being on earth. Well, okay, so why not a
*  human with a machine that's optimizing in the same way produce the same outcome? Or this thing,
*  it builds like these nano self assemblers and there's this famous post like, create an identical
*  strawberry thing where it does these nano assembler things. It's like, okay, but like, first of all,
*  as far as I can tell nano assemblers in science fiction, a lot of people like Drexler, I haven't
*  actually seen a demonstration of this technology. But second of all, like, okay, you don't need the
*  AI to be worried about the nano assemblers at that point. So it's like not clear to me that an AI
*  that, okay, is like reward hacked some humans is any more dangerous than an out of control bulldozer.
*  Like, we know how to deal with this stuff. We ought to think about it in those terms. I think
*  the real danger here is anthropomorphizing the system and saying, no, it's like, it's thinking,
*  it has goals. It doesn't have any goals. It's a computer system. It can be anthropomorphized
*  to have goals, but concretely, it's doing matrix multiplications and applying nonlinearities to
*  them. And that's a system that's a nonlinear dynamical system that's continuous and
*  differentiable. And we know how to deal with those. It just doesn't strike me as a credible
*  argument. It only strikes me as a worrying argument when you start to turn these machines into people.
*  Well, I worry about the whole spectrum. And I get ambivalent on this in the classical sense of having
*  strong feelings both ways. I love working with all the AI technology. I love studying it.
*  I'm super excited about the upside. When you talk about what about just a bad actor with an AI,
*  that's very much, I think, of concern, no doubt. There's a project out there right now called,
*  I can't exactly what it's called, but it's basically text to regulatory RNA sequence,
*  which starts to sound pretty insane. I asked a model one time to write some hard science fiction
*  based on that premise. And it got me to some pretty strange places pretty quick.
*  Obviously, we have so much time. We can only go so deep on this today.
*  There's one canonical example of that. There was that famous paper where they asked it to produce
*  effective pharmaceuticals, and then they turned the reward function around and just started
*  producing deadly poisons all of a sudden. That stuff is more concerning. Ultimately, in order
*  to kill us all, whatever does that has to obey physical law. It's a large leap for me
*  in the physical world. And I think this comes from my background as a roboticist
*  in that it's really hard to do things. It's a lot easier to do things with information than it is
*  to do anything in the physical world, regardless of how often people analogize things like, oh,
*  DNA is just binary encoding, or it's CRISPR is programming biology. It's not really like that
*  in the real world at all. To give another analogy, anyone can make sarin gas. The problem with sarin
*  gas is not making it, it's deploying it. It's getting it into place. That's why we don't have
*  constant sarin gas attacks. Whatever this thing is that's supposedly going to kill all of us
*  has to be able to act in the physical world in a way that I just haven't seen any system capable
*  of doing yet. Well, I hope I never meet a robot that has the regard for me that new Bing has had
*  for some of its early users. That I can say for sure. We're running out of time. I would
*  love to check back in at some point down the line and see how both your company is developing,
*  whether or not you've continued this stable attribution project. We can also check in again
*  on how much existential confidence or nervousness we have. A couple of just real quick hitters to
*  close us out today. One, AI tools in your life. What are you using? What has changed your workflow?
*  What do you recommend? Yeah, ChachiPT has sped up my programming work a whole bunch because whenever
*  I work with an unfamiliar library or get a weird bug, I ask ChachiPT. Sometimes it hallucinates
*  stuff, but at least helps me look in the right direction. I use coding assistance. I've been
*  using Co-Pilot. I recently tried Cadimium. It's pretty good. It definitely sped me up as an engineer
*  mostly because I no longer have to Google or go to Stack Overflow or look for documentation of stuff
*  that I'm unfamiliar with. What that means is it's not replacing me as a programmer. It's getting the
*  things that I really don't know how to do out of my way so that I can focus on the things that I'm
*  actually really good at. That's been a huge, huge productivity boost. Yeah, I think that's really
*  the main ones that I'm using today. I also recommend Reflit and their Ghostwriter and
*  Ghostwriter Chat. Yeah, yeah. Pretty cool. We really like Reflit and Chroma. Okay, quick hitter number
*  two. Hypothetical scenario. If a million people already had a Neuralink implant
*  and it would allow you to type as quickly as you can think, in other words, you now have thought to
*  text, would you get one? I think, and I've thought about this, I think if we end up living in a
*  society where somebody makes me implant a computer in my head or it's socially unacceptable to not
*  implant a computer in my head, I'm going into the woods. That's a no. You're a no on... It's a
*  strong no. Listen, I've seen how software is written. I don't want it anywhere near my brain.
*  Yeah, it's wild. I do think, I kind of expect to see that day. I used to think my grandparents,
*  who were born around 1930, and my grandmother is still alive, she's going to be 90 this year.
*  I used to think that they saw way more change in their lifetimes than we ever would.
*  That perspective has started to change recently. Now I'm like, yeah, maybe I'm going to be getting
*  emotionally prepared to have a hole in my head and a little implant.
*  Look, I know what's going to happen here. What's going to happen here is I'm going to have some
*  neurodegenerative disease when I'm like 85 years old and they'll be like, install Neuralink and it
*  just fixes you. I'll be like, God damn it. Remember when I went on that podcast?
*  You'll remember it after they do the implant. That's when you'll have the memory.
*  That'll be the real tragedy, I think. You're right.
*  All right. Last one. You're not so concerned about the doom scenarios.
*  Bolt, give us your big picture, hopes, positive hopes for, and also to the degree that you have
*  them, downside fears for AI for the rest of this decade. Yeah, I think that's a really good way of
*  framing some things. One of the problems that we faced historically as a species is the thing that
*  we talked about earlier where nobody tells us we're going to push a button and everything's
*  going to change. But I think AI gives us the possibility of having tools that allow us to
*  rapidly adapt to our situation. The fundamental thing that humans have going for us is our
*  adaptability. A prosthesis, an extra tool that allows us to adapt even faster, makes it easier
*  for us to deal with problems as they emerge. It actually could make us safer in the long run.
*  The way that I think about that is right now, for example,
*  suppose that there's some frightening thing like COVID. In COVID, you needed a PhD or an MD to
*  understand what to do with it. There's only so many people in the world that really understand
*  what recombinant DNA really means. I certainly don't. I'm not a biology person. But if we had
*  tools to get people to the research front, like a PhD in a box where it was exactly tailored
*  individualized to you and turn you into a researcher just because you wanted to work on that stuff,
*  that sounds like we could be much more agile and nimble as a species to deal with anything that
*  might come up. That's a hope. Of course, the downside is every new media technology has this
*  other property where at the start, everyone believes it's going to be for education, but it
*  ends up getting used for pornography and propaganda. I think this time is no different. The propaganda
*  part worries me. This new idea of knowledge capability through having a reasoning machine
*  in your pocket worries me a bit. The thing that doesn't worry me is I don't think that...
*  You could probably reason your way to some very dangerous things, but again,
*  those very dangerous things require you to be able to act in the physical world. We're talking about
*  fairly organized actors being dangerous rather than individuals. Hard to say.
*  Overall, I think one thing that's going to happen, I think one other dangerous thing which we didn't
*  really discuss is there's a very real possibility that another AI winter will happen. I actually
*  asked Sam Altman that question a little while ago. There was some sort of event. Honestly,
*  overexuberance about the capabilities and then they fail to deliver it. That's what's happened
*  every other time in AI winters. The previous one was expert systems and one before that was neural
*  networks. Now we're back in neural networks again. That's worrying because another fallow decade when
*  we could have these incredible technologies is actually... I don't know. That seems really bad
*  to me. We should try to be fairly clear-eyed. That said, I'm still bullish because there's,
*  like we said, there's these massive capabilities overhang we haven't even started to explore.
*  That's all the time we have for today. Anton Tarnikov, the company is Chroma,
*  the embeddings database. Thank you so much for joining us on the Cognitive Revolution.
*  Thanks for having me, guys. The Cognitive Revolution podcast is supported by Omniki.
*  Omniki is an omnichannel creative generation platform that lets you launch hundreds of
*  thousands of ad iterations that actually work, customized across all platforms with the click
*  of a button. Omniki combines generative AI and real-time advertising data to generate
*  personalized experiences at scale.

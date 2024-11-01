---
Date Generated: October 30, 2024
Transcription Model: whisper medium 20231117
Length: 4913s
Video Keywords: []
Video Views: 1933
Video Rating: None
Video Description: Nathan interviews Bernal Jimenez Gutierrez, creator of HippoRAG, a novel approach to retrieval augmented generation inspired by the human hippocampus. In this episode of The Cognitive Revolution, we explore how HippoRAG improves on traditional RAG systems, its neuroanatomical inspiration, and its potential for handling complex queries requiring multi-hop reasoning. Join us for an insightful discussion on the future of AI memory systems.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST: Complex Systems
Patrick McKenzie (@patio11) talks to experts who understand the complicated but not unknowable systems we rely on. You might be surprised at how quickly Patrick and his guests can put you in the top 1% of understanding for stock trading, tech hiring, and more.
Spotify: https://open.spotify.com/show/3Mos4VE3figVXleHDqfXOH
Apple: https://podcasts.apple.com/us/podcast/complex-systems-with-patrick-mckenzie-patio11/id1753399812


SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:02:52) Intro
(00:05:10) RAG
(00:09:29) Hippocampal Memory Indexing Theory
(00:14:29) Neocortex, Parahippocampal Regions, Hippocampus
(00:18:35) Hipporag (Part 1)
(00:21:12) Sponsors: Oracle | Brave
(00:23:20) Hipporag (Part 2)
(00:23:29) Understanding the Hippocampus
(00:29:37) RAG
(00:31:38) Runtime (Part 1)
(00:36:30) Sponsors: Omneky | Squad
(00:38:17) Runtime (Part 2)
(00:38:17) PageRank
(00:39:29) Headline Results
(00:43:22) Gaia Benchmark
(00:46:33) Pathfinding vs Path Following
(00:51:24) Future work
(00:53:26) Starting with a query
(00:58:30) Long context LLMs
(01:01:50) Hybrid approach
(01:05:03) AI Town
(01:06:58) Flair
(01:09:05) Getting it right, not cheap
(01:12:33) Technologies to highlight
(01:16:57) AI capabilities that are still unsolved
(01:19:47) Transformers meet neural algorithmic reasoners
(01:21:02) Closing
(01:21:31) Outro
---

# Long-Term Memory for LLMs, with HippoRAG author Bernal Jiménez Gutierrez
**Cognitive Revolution:** [July 19, 2024](https://www.youtube.com/watch?v=YQauz14Pvfk)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today my guest is Bernal Jimenez-Gutierrez,
*  PhD candidate at Ohio State University and the lead author of HippoRAG,
*  a novel approach to retrieval-augmented generation inspired by the human hippocampus.
*  RAG, of course, has become one of the most important techniques for grounding large
*  language models in specific knowledge bases. But as anyone who's implemented a RAG system knows,
*  there are still major challenges, particularly when it comes to questions whose answers are
*  not recorded explicitly in a single document but have to be inferred from a more diffuse
*  collection of sources. That's where HippoRAG comes in. Drawing inspiration from the hippocampal
*  indexing theory of human memory, Bernal and his collaborators have developed a system that uses
*  LLM-powered entity recognition and embedding clustering synonym identification techniques
*  to pre-process knowledge into a graph structure which can then handle complex queries requiring
*  multi-hop reasoning far more quickly and affordably than previous state-of-the-art approaches.
*  In our conversation today, Bernal walks us through the neuroanatomical inspiration for HippoRAG,
*  explains how it works under the hood, and discusses its current capabilities and limitations.
*  We also brainstorm ways that it could be extended and improved, considering how it might complement
*  other recent advances like Raptor, as well as the strategy of periodically creating synthetic
*  reflective memories which I first encountered in the AI Town project. Notably, it seems to me that
*  these techniques are pretty much conceptually orthogonal, such that an application developer
*  might be well served to implement all three and perhaps even more into a single RAG system,
*  assuming of course that the use case justifies the investment. As always, if you're finding value
*  in the show, we'd appreciate it if you'd take a moment to share it with a friend. We welcome your
*  feedback via our website, cognitiverevolution.ai, and you're always welcome to DM me on your favorite
*  social network. Finally, for now, a programming note. I'll be away for a short vacation and to
*  speak at the Adapta Summit in Sao Paulo for the next couple of weeks. But don't worry, we've got a
*  full schedule queued up for while I'm gone, and I plan to make a big push to generate more connections
*  between AI engineers and advisors and actively hiring companies when I'm back. So definitely
*  remember to submit your resume if you're interested in being a part of that. Now,
*  I hope you enjoy this fascinating exploration of biologically inspired AI memory systems
*  with Bernal Jimenez Gutierrez, creator of HippoRAG. Bernal Jimenez Gutierrez, author of HippoRAG,
*  welcome to the Cognitive Revolution. Matt, thanks so much for having me. I'm excited.
*  I guess for starters, two things caught my attention about this project. One is just a
*  performance, which we'll get into and the fact that it works and seems very practically useful.
*  The other is that you're drawing inspiration from biological systems to kind of motivate the design
*  of this new RAG system. So as the name would suggest, the project is inspired by the Hippo
*  Campus, which I think is cool. You want to just kind of give us a little bit of background of,
*  first of all, who you are, the group you're working in, and then specifically for this project,
*  what was the kind of original motivation? What was the bug that got you to dive deep into this?
*  Yeah, sure thing. So I'm entering my last year here at Ohio State. I'm working with Professor Yusu
*  at the OSU NLP lab, and our group does a lot of different things from embodied agents to more
*  like mind to web came out of our group. So like agents in the web. And Dr. Yusu is really interested
*  in the biological inspiration side. So that also is a big part of our group. But me in particular,
*  I graduated from Berkeley in 2015 with an applied math BA, and I started working at a
*  healthcare startup that did NLP for matching cancer patients with clinical trials. And I
*  really got into this biomedical NLP direction of research. And I've been doing that for many years
*  using AI to facilitate biomedical research through NLP tools. Like, well, in the past,
*  it was just like ontology's knowledge bases like UMLS. And I've been kind of transitioning into
*  how do we really use LLMs effectively in this biomedical NLP space? And from all of this biology
*  accumulated knowledge, I started to become more and more passionate about how the brain works
*  and how we can get inspiration from that to actually make LLMs better. So I think of my
*  research as this two-way street between biology and LLMs. For HIPPORAG, how it initially came about,
*  it was also this kind of two-way street where at the beginning, before even starting, I was thinking
*  about domain-specific LLMs and how they're going to fit into the current NLP landscape. And really,
*  because of the limited amount of data that there is in specific domains, it's kind of
*  not a great idea to just pre-train from scratch in these limited data domains. And so I was more
*  leaning towards like, okay, RAG plus a very strong LLM trained on everything is probably
*  your best bet. But in looking into that, I realized that RAG has some very major limitations.
*  And at the same time, me and my advisor were both thinking about neurobiological memory,
*  so like human long-term memory and our ability to do continual learning. We do continual learning
*  in a way that is basically impossible for current LLMs to do. And so it was kind of this back and
*  forth between these two ideas. There's issues with current models, current RAG, and how really to
*  best utilize associative memory, like the concept of associative memory in humans,
*  to make this kind of synthesis of the two. And I think early this year, I kind of realized the
*  nugget of inspiration that kind of made everything fall into place was this idea of knowledge
*  consolidation through pathfinding multi-health questions. Like this idea that LLM chain of
*  reasoning is not all you need for finding important knowledge-seeking questions, really.
*  You need to have this pre-processing knowledge consolidation of your information in order to
*  really answer all the questions that you want. So in the paper, we use this example of someone
*  trying to find a Stanford professor that also works on the neuroscience of Alzheimer's,
*  theme appropriate. And then we basically show that if there's a bunch of like a thousand Stanford
*  professors and a thousand Alzheimer's researchers, if you just use path following, like kind of have
*  an LLM, look at your corpus, find the appropriate next step, and then follow it, you would have to
*  be looking at like multiple thousands of documents in order to do this correctly. And a human that
*  just knows this professor is at Stanford and does Alzheimer's research will likely just remember
*  this professor immediately. So yeah, that was kind of the link that brought these two directions of
*  thought together. A number of interesting themes there. I'm big on the application of language
*  models to specific domains. And I often call myself an adoption accelerationist in the sense that I
*  think it's really important that we not just keep scaling up systems and hope that one day they work,
*  but actually take the systems that we have now and really put the effort into dialing the
*  performance, validate the performance and start to get practical utility sooner rather than later.
*  I think, by the way, the medical domain is one of the great candidates for that. And I've had
*  multiple conversations with the team that was the MedPalm team is now the MedGemini team,
*  a huge fan of that line of work and that line of thinking. The theme also of continual learning
*  is definitely a big one. Anybody who's built with language models sort of has this experience of
*  the missing middle memory is sometimes how I describe it, where you've got kind of this
*  superhuman long-term memory that knows more than people do. But then you've got this very finite
*  and kind of, you know, either the information is or isn't there in the context window. And then
*  in between you have RAG, but as you said, that obviously has a lot of limitations, especially
*  with the implementations that we've had to date. I think I get how the kind of prior state of the
*  art in RAG works, but maybe you could run through that and talk about how it actually works, why it's
*  slow, why it's expensive, and then maybe give us a little bit of the understanding of how the
*  hippocampus works. And then we can get into how you implemented that to bring that approach to
*  the technology side. Cool. So RAG, Retrieval Augmented Generation, basically at its most basic
*  form uses some sort of information retrieval system via BM-25, the most simple lexical-based
*  system or more recent semantic embedding approaches like Contriver, Colbert, we use in our paper, or
*  you could even use LLM embeddings. There's many ways of building specific vectors for
*  each document in your corpora. And then the idea is that when the user has a question, the LLM
*  first looks up the relevant documents in the corpora, puts them in the context window, and then
*  the LLM has all the information it needs, and then it generates the correct response, right? So that's
*  kind of the current state of Retrieval Augmented Generation. There's a lot of different ideas with
*  how to augment the generation, like you could correct errors as you go, like Flare does, like
*  forward-looking active retrieval, or you could retrieve many, many times and generate many times
*  and then kind of do majority voting. There's a lot of different ideas about how to do this retrieval.
*  And also, in order to do more complex consolidation of knowledge within this framework,
*  you would suppose that the model decomposes your question into steps. So if your question is more
*  complex and it requires more than just one retrieval step, for example, in any sort of
*  multi-hop question, you would first retrieve something, then reason over it, and then do
*  another step of retrieval as many times as you want in order to accomplish that. So this is not
*  perfect knowledge, right? This is just kind of theoretical at this point, but the hippocampal
*  memory indexing theory, which is what we based Hipporagon, tries to explain a lot of empirical
*  data on the hippocampus being important for long-term memory storage, because, well, in the
*  like mid-1900s, the patient HM that got their hippocampus resected basically can't form new
*  episodic or semantic memories, like long-term memory. And so people are trying to explain why
*  the hippocampus is so important there. And the hippocampal memory indexing theory basically
*  posits that it's an index that just stores pointers to the actual memories in the neocortex.
*  And it also stores associations between these pointers, right? So it doesn't have any true
*  information about what these pointers are. It just points them to the actual representations
*  in whatever area of neocortex they should lie in, right? Like visual cortex, motor cortex,
*  your language areas, et cetera. And so the idea is that as you obtain new knowledge, you built
*  this associative index iteratively. So in our Stanford professor example, you would kind of
*  create a representation for the Stanford professor, link it to Stanford and link it to
*  the Alzheimer's research idea. And then you'd have this index that you can traverse to find
*  the appropriate Stanford professor. And I could go into like three components that are proposed
*  in the hippocampal memory indexing theory and also pattern separation, pattern completion, but
*  I'm not sure how detailed we should go in there. Yeah, let's do it. Just kind of take one step
*  back into the naive rag approach, because then this will motivate like how we're doing it better
*  and how the new system inspired by the biology is doing it better. But if you had a giant corpus of
*  information and you know that there's lots of professor bios and researcher profiles in there,
*  you could embed this. But if you're unlucky and there's not a single document that contains both
*  the Stanford and the Alzheimer's keywords, if those are not co-located in a single bit of text,
*  then the naive way would be you could start with all the ones that work on Alzheimer's or all the
*  ones that work at Stanford. But again, then you'd have to look at each one and say, okay, now
*  get me more information about that person, then bring that back and see if that's right.
*  And so you'd have this like long kind of brute force search through the document space to
*  ultimately find the thing that you're looking for. You don't really have a great way of like
*  quickly zeroing in on the one that you want. And that's why it either can be expensive if you
*  paralyze it highly or slow if you just grind through it serially or potentially both depending
*  on the details of your setup. But that's obviously not ideal. And then as you said, just generally,
*  if you have those two pointers, like I'm not sure I can get there just through introspection,
*  but it does seem like intuitively clear that if given a couple of pointers, I can usually quickly
*  locate the memory without having to do some sort of like, you know, it's pretty clear to me that I
*  am not doing that process where I'm not thinking like, what's every professor that I know, is that
*  the one that satisfies this criteria? So with that motivation of kind of the slow,
*  naive approach, let's do the little bit deeper dive into the hippocampal indexing theory,
*  and then we'll map that onto the technology implementation.
*  Great. Yeah, that was very helpful, I think, for viewers to get a better sense. So the hippocampal
*  memory indexing theory kind of posits that there's three major components of human long-term memory.
*  There's the hippocampus, obviously, that kind of does this associative index, which is like the
*  centerpiece of this framework. But there's also the neocortex that actually represents the memories
*  that you want to retrieve or re-experience. And then there's the parahippocampal regions,
*  which are like the inter-rinal cortex and other areas that sit around the hippocampus. And
*  theoretically, it seems that this area serves as a link between the hippocampus and the neocortex,
*  like a bi-directional information channel, basically. And there's some ideas that some
*  part of working memory is done in the parahippocampal regions, but this is still not very clear.
*  And then these three components work together to create two fundamental characteristics of
*  human long-term memory. So there's pattern separation, which basically allows you to
*  disentangle different features that you experience, like create concepts like Stanford Professor and
*  Alzheimer's research, or any sort of feature disambiguation or separation. And then pattern
*  completion, which actually allows you to join together things that were relevant to a particular
*  experience in the relevant ways. So the pattern separation is done through the neocortex and the
*  parahippocampal regions. Through the neocortex, it's mostly done, I believe, this is not explicitly
*  said in the literature, but it's a part of the language system that kind of separates concepts
*  out. And also the parahippocampal region has a lot of sparsity. It's very overparameterized. So
*  it allows for this kind of separation of patterns and features that then map into the hippocampus.
*  And the hippocampus is mostly for the pattern completion part. Specifically, there's a sub-region
*  called CA3 that it's hyper-connected, you could think of it like that. So there's a lot more
*  associative connections than in other parts. And so you would have this recurrence nature that allows
*  for you to remember things that are only associated because of your prior experience,
*  not because they're associated semantically. And so based on these two fundamental characteristics
*  and also on the three components of hippocampal memory, we built hipporag to kind of mirror
*  those things. So the neocortex and the language abilities of neocortex, we modeled through a large
*  language model because it basically has these local reasoning abilities and the ability to extract
*  and disentangle features from language. So that seemed like a good parallel. We used retrieval
*  encoders for the bidirectional bridge between the neocortex and the hippocampus. And we used
*  knowledge graph to represent the actual structure of the hippocampus. And then we used personalized
*  page rank to model the associative memory component of the hippocampus. So those are the three
*  components that make pattern separation, pattern completion possible. To actually do pattern
*  separation, we link pattern separation to the offline indexing process, which is basically the
*  pre-processing that you have to do to turn the corpus that you have into an associative index.
*  And so we first go by each document through the large language model to extract entities.
*  And that basically just grounds the next step of generation, which is open information extraction
*  or schema-less knowledge base construction. So this basically has no rigid constraints
*  on the type of entities that you can generate or the relations you can generate, or even the
*  entities themselves. So we are kind of using the named entity recognition of the first step
*  to ground that second step, but it's just a bias. It's not like a forced constraint. So it generates
*  a lot of different entities and relations. And we built the knowledge graph based on those
*  triples extracted. And we then use the retrieval encoders to build synonymy edges. So this is a
*  detail of the implementation that is actually quite important in specific cases, but you need
*  some sort of disambiguation or actually like some synonymy detection, the opposite of
*  disambiguation for this knowledge base to be more connected. And then the online retrieval, which we
*  kind of linked or it's analogous more to pattern completion. It also has a pattern separation
*  part, which is basically the named entity recognition from your question. So whenever a
*  question enters where you already have your knowledge graph constructed, you would first
*  extract the features that you want to attend to, then link them to the knowledge graph via the
*  retrieval encoders. So you find the nodes that are most relevant. And then with those entities,
*  you begin your personalized page rank algorithm, which basically does a random walks around your
*  relevant entities until you converge on a distribution of probability. And that gives you
*  a distribution of probability over the nodes in your graph, which inform your ranking for your
*  corpus. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry,
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing. And of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive of OCI at oracle.com
*  slash cognitive. That's oracle.com slash cognitive. Oracle.com slash cognitive.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave Search
*  index stand out? One, it's entirely independent and built from scratch. That means no big tech
*  biases or extortionate prices. Two, it's built on real page visits from actual humans, collected
*  anonymously of course, which filters out tons of junk data. And three, the index is refreshed with
*  tens of millions of pages daily. So it always has accurate up to date information. The Brave Search
*  API can be used to assemble a data set to train your AI models and help with retrieval augmentation
*  at the time of inference, all while remaining affordable with developer-first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data sourcing
*  and more human representative data sets. Try the Brave Search API for free for up to 2,000
*  queries per month at brave.com slash API.
*  Okay. So let me rewind and try to restate some of that back to you and make sure we have clarity on
*  all the key parts. First of all, just to the biology, I often say this is an analogy-free zone.
*  And for the reason that I find analogies often kind of misleading in certain cases, you know,
*  tight enough analogy and obviously you're designing this, you know, by analogy. So here,
*  I do think it's kind of interesting to just look at those three regions of the brain and try to
*  reconceptualize them in terms of familiar aspects of AI systems that probably listeners will be
*  more familiar with. So it sounds like in the kind of detailed memories, which would be sort of akin
*  to a passage or a chunk out of a corpus of text, those are thought to be encoded or you might say
*  embedded and stored in the cortex. So that's like where the raw most detailed form of memory is,
*  right? And I guess there's a lot of space in the cortex to store all these memories.
*  The challenge then becomes how do you access them? Same as we talked about before, if you just like
*  have all this out there, searching through it one by one brute force is not going to work well.
*  So then I think that middle region and was that the
*  para hippocampal region? Is that what you called that? Correct. Okay. So that's really interesting
*  because it seems to perhaps have a similar function to like activations. You know, you can almost
*  think of it as like playing a similar role to like a sparse auto encoder, which has definitely been a
*  hot topic recently. And the phrase you use is pattern separation. So that's like understanding
*  which within any given high detail, rich memory, what are the sort of salient concepts that matter
*  when you abstract away all the little details from whatever the raw memory is? That is kind of
*  striking. I hadn't really ever come across the idea that we have something quite like that,
*  but it isn't an interesting parallel that there's this separated semantic encoding that sits between
*  the raw encoded or embedded memories. And then this like index that connects them definitely,
*  again, reminds me of sort of an activation, like a sparse auto encoder type of a function.
*  Presumably, it's not you can maybe tell me if there's more that's known about this. But if I
*  had to guess, I would guess that it looks a lot more like the dense poly semantic,
*  hard to disentangle representation that we find in the large language models, as opposed to the
*  sparse clean interpretable form that we find in the sparse auto encoders. But one might imagine
*  that you could perform a similar sparse auto encoder type analysis on the activity of that
*  region and gradually figure out what are the high dimensional messy representations that seem
*  to kind of correspond to recognizable features. I don't know if anything like that has ever
*  been done, but does that seem like the right intuition for the role that that region is playing?
*  Yes, I think as I see it, it's kind of a sparsity constraint on the dense representation. The role
*  of the neocortex is to experience the world and predict the world in real time. And so the
*  representations have to be really dense and rich, right? But in order to remember them,
*  you need sparsity. So I think the parahypochromal region is kind of doing this sparsity constraint.
*  And the interesting thing about that is that you said that the sparsity is probably not
*  like polysemantic, like the large language model sparsity. But I'm actually not super sure about
*  that because in the hippocampus, we know there's like several studies that find that there are such
*  things as place cells, people cells, gramma neuron, different sorts of very specific monosemantic
*  concepts that we care about that are encoded in the hippocampus. And so somehow it went from
*  this dense representation in the brain that has all sorts of polysemantic stuff in a high
*  dimensional vector space. And then it gets sparsified in ways that we maybe care about
*  stored in the hippocampus. So in that parahypochromal region, you are doing a lot of
*  pattern separation, a lot of sparsification in order to get to this level. So I think there is
*  a lot that goes on in the parahypochromal region that is not super fully understood.
*  And it's definitely not exactly like hipporag in any, like, yeah, it's not exactly a hipporag at
*  all. This is just like a good implementation that works. Well, hopefully at this point,
*  for our loyal listeners goes to that saying, but yeah, made of different stuff,
*  definitely different mechanism, lots of lurking differences, which could cause us issues. But
*  it does seem that there is something quite interesting there. And my statement of like,
*  imagining that it was probably highly polysemantic and messy is just based on the general prior that
*  everything in biology often feels like it's very messy. But I mean, and I have heard about
*  those studies that kind of the Halle Berry Neuron and all that crazy stuff is suggestive,
*  yeah, that maybe there is indeed a very sparse representation. Finishing on the bio, the
*  hippocampus itself then stores the associations between the, let's say, feature representations
*  or the separated patterns, the perhaps sparse representations, so that you can quickly
*  understand which of these concepts have co-occurred. And then that becomes like the core insight for
*  this whole technology development, right? That becomes a way to quickly get from one
*  memory or one concept to the related co-occurring concepts so that you can find that Stanford
*  professor that studies Alzheimer's without having to like brute force your way through all the
*  professors or all the studies or what have you. Then on the technology side, basically two parts
*  to the process, there's kind of the pre-processing part, which is your setup. And this is where like
*  there's major disanalogies, obviously, between humans and these systems. And then there's the
*  runtime part. The key idea in both cases is entity recognition is like your starting point, right? So
*  in the setup, you've got some corpus of information that you want to have command of, you want to be
*  able to search through effectively, going through and using a language model to identify all the
*  entities. I'd be interested if you could shed a little more light on like how that has worked or
*  prompts or whatever. I also noticed, I think in the paper that you were using GPT 3.5, so curious
*  as to why that was versus a more, you know, perhaps just cost or whatever, but interested
*  to understand what the constraints you were under and how you think that might change if you used a
*  better model. But you're sort of identifying all these things. Okay, here's a professor,
*  you know, here's a condition. This is Alzheimer's. This is another professor. This is another
*  different condition, etc., right? Identifying all these sorts of things. Then the synonymy part is
*  important. Again, this is moving from syntax to semantics, basically. If you have two words that
*  mean the same thing, obviously, I think everybody is familiar at this point with the fact that in
*  embedding space, those will be very close to one another. And so they'll both have high inner
*  product with other relevant things. And that's a big part of the standard rag systems work. But
*  it's important to perform that step so that you have the ability to still match on entities that
*  are extracted slightly differently. And then finally, you have a graph database that you
*  compose out of all these entity extraction. So your ultimate format out of the pre-processing is
*  all the original documents, all the entities that are extracted, then kind of collapsing those into
*  synonyms and then associating those synonyms so that you can quickly traverse from one starting
*  point to things that co-occur. Okay, cool. Now at runtime, a query comes in. You do that same
*  entity extraction. Those entities now serve as the seeds for the search. Now with the graph
*  structure in place, you know, should be pretty intuitive that, hey, now we can go spider out to
*  all of the relevant original raw passages, which is ultimately what we're going to retrieve to then
*  have the language model reason over and answer whatever question we have. I mean, I can easily
*  imagine like a naive thing where I might say, okay, I've got this entity and this entity
*  detected, you know, just spider out and grab me everything. I'm a little bit unclear as to
*  how that gets refined with this personal PageRank algorithm. So maybe three questions would be,
*  what if anything doesn't get wrong? Two, what's the deal with 3.5 and using that for the entity
*  recognition? And then three, can you give me a little more detail on the personal PageRank and
*  sort of what the choice parameters are there? Cool. Yeah. So let's start with the simplest
*  question. So DVD 3.5, basically it's much cheaper than other models. The difference between 3.5 and
*  Claude is like, Claude is like twice as expensive in the inputs and like 10 times as expensive in
*  the outputs. And so that kind of puts a constraint on our methodology because offline indexing is
*  somewhat expensive. So you have to produce a lot of open IE triples basically. And so if you were to
*  do our same experiments in using Claude or GPD 4.0, you would have to spend around like $500
*  to do the small subset of the three benchmarks that we did. And that's like a very limited subset,
*  right? We used a thousand questions, around 10,000 documents per benchmark. So yeah, that would just
*  cost too much money. And honestly, the biggest reason I used 3.5 is that the task itself is not
*  really a relaying task. It's an extraction task. So it's like a salience detection. And then when
*  two entities appear in a sentence together, they have some relation, so detect the relation.
*  And so it's kind of simple and different LLMs, even like Lama 3, 7 billion, is able to do a fairly
*  good job at this task. And so apart from the formatting, the formatting is kind of challenging
*  and you probably need to fine tune it. But because it's just an instruction task, it seems quite
*  simple for like less intelligent LLMs to do. And so I wouldn't expect Claude or GPD 4.0 to do much,
*  much better on this task, just right off the bat. And then the second question about PPR. So this is
*  kind of like the biggest limitation of our framework, I would say. And the thing that we're
*  most excited to work on. Because PPR is obviously a very naive way to spider out from the relevant
*  nodes. Basically, if a node is connected to your relevant nodes through like directly and indirectly,
*  it'll get more probability, the closer nodes to you get more probability. And if a node is
*  connected to both relevant nodes, it'll get more probability. So it's based on the connectivity
*  structure of the graph. And so there's no relation guidedness or anything like that. It is basically
*  just how connected these nodes are to the relevant nodes. And if you like turn up the
*  amount of steps that your random walk takes before converging, you'll just do page rank on the whole
*  graph. Basically, if you turn it up to basically like all the maximum amount of steps, then you just
*  get the nodes that are the most connected in your graph, like the nodes that are most popular.
*  And that was used in the original Google search, right? Like if your websites are very popular,
*  just give me those instead of other ones. But that's not really a good idea here. And if you
*  turn it down too much, then the nodes that you get are like basically all you're gonna attend to.
*  And so there's like a middle ground that you want for the neighborhoods around the relevant nodes
*  and like between them in order to obtain good performance. I think our good performance in the
*  benchmarks is due like somewhat to biases in there and the lack of some of a lot of distractors.
*  But if you make this a large scale production corpora, you definitely need to make that graph
*  traversal better. And so that's what like one of the things we're working on right now.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable.
*  And do more with less, especially with engineering. Listen, I love your 30 year old ex-fang
*  senior software engineer as much as the next guy, but honestly I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale.
*  From sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high
*  level for over five years to help you access global engineering without the headache.
*  Squaw, Sean's new company, takes care of sourcing, legal compliance, and local
*  HR for global talent so you don't have to. With teams across Asia and South America,
*  we can cover you no matter which time zone you operate in. Their engineers follow your process
*  and use your tools. They work with React, Next.js, or your favorite front-end frameworks. And on the
*  backend, they're experts at Node, Python, Java, and anything under the sun. Full disclosure,
*  it's going to cost more than the random person you found on Upwork that's doing two hours
*  of work per week, but billing you for 40. But you'll get premium quality at a fraction of the
*  typical cost. Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squaw.com and
*  mention Turpentine to skip the wait list. Yeah, interesting. So in this initial version,
*  the PageRank algorithm itself is not smart, so to speak. And if I understand correctly now,
*  where you are starting in the graph and the limit of how far you're willing to go explore the graph
*  determines what is pulled back. If you were to turn the limit all the way up, you would get
*  the whole graph sorted by connectivity, not sorted by semantics. And so you're constraining
*  to the relevant semantic region just based on where you're starting. So there's definitely
*  more opportunity there to then say, let's also navigate in a more intelligent way.
*  Yeah. Now again, intelligently and efficiently. That's the biggest thing. You could just add some
*  sort of LN to do that traversal, but then you would increase the cost. So there's a
*  range of ideas there to trade off on efficiency and intelligence. But yeah, it's not just where
*  you start and the amount of hops. It's also the local connectivity. So there's both local
*  connectivity and where you start determines your final PPR ranking. But that's it.
*  Okay, cool. So give us the headline results on this. You've run this on a number of different
*  benchmarks. There's cost savings, there's speed improvement, there's accuracy improvement.
*  And then from there, I want to do a little brainstorm with you on what are the ways that
*  this can still get better? And what would it look like if we just did a commercial no holds barred,
*  let's go make the very best rag system that we can, borrowing from any and all methods,
*  kind of brainstorming session. But for starters, headline results.
*  Yeah. So on average, we compete with iterative retrieval, basically kind of head to head. We
*  get a little bit better at some benchmarks and some benchmarks we get a little bit worse. But
*  this is with like a tenfold decrease in cost and time spent doing the online retrieval. So that's
*  huge for any production system that requires fast online access by your users, right. And the
*  indexing costs can be brought down a lot by using smaller LLMs, as I discussed earlier. And another
*  really interesting thing is that when you combine it with just naive iterative rag,
*  you can get very large boosts on average, like seven to eight percent across benchmarks.
*  And so that is basically kind of proto like self-correction that you were discussing earlier,
*  because the model is seeing like the results of your ranking. And it's able to reason better
*  because you're able to do some associative memory retrieval, right. So yeah, that is generally the
*  highlights of the empirical benchmarks that we showed. And then obviously there's no empirical
*  benchmark that exists that tests pathfinding question answering, sort of this like Stanford
*  professor Alzheimer's researcher idea. But this is something that you could not do with current
*  approaches. And we tried it on a few like test cases, more qualitative. And it seems to do okay
*  of this. It seems to do well on some of these questions. And we need to make the graph traversal
*  better in order to like fully unlock its potential. But the idea that you can answer all these
*  pathfinding questions, some of which are extremely important. Like one of the questions in our case
*  study talked about what medication for some condition works by interacting with X enzyme
*  or like through this mechanism. And so that is a question that doctors would benefit from answering
*  because if there's some condition that would interact poorly with that mechanism, then you
*  shouldn't use it. So that's a very important question. And I think having systems that can
*  answer that type of question is important. So the before after and synthesis is before you have this
*  iterative approach, it does this kind of brute force, which we've talked about a couple times
*  after is you're just giving your own system one shot basically in saying you have an input,
*  extract the entities, use those as the starting place to traverse through the graph, pull back,
*  whatever that process returns, that's what you get. And you compare that to the iterative approach,
*  which has obviously multiple rounds of going back to the database and find those to be
*  roughly equal, although a lot cheaper and faster with the HIPAA rag method. And then the natural
*  next step is to say, well, what if we allow the HIPAA rag method to also go back again, if needed.
*  And then with that, that's where you get the big performance boost. Cool. So yeah, I mean,
*  the lack of benchmark on this is interesting. There's one benchmark that's coming to mind.
*  I believe it is the Gaia benchmark. You're familiar with this one?
*  Yeah, it's from Meta. Yeah, I'm familiar with this benchmark. It's related. And I think we explored
*  it as an option for this. I think the web browsing portion of this is similar. However,
*  because there's no standard corpus, it makes it a little bit challenging to do it.
*  Pre-processing the whole internet is obviously still a challenge for
*  ramping this up to the highest scale. Or more like a cost. Right. I think it's too costly.
*  But yeah, so I think something like Gaia, but just maybe more constrained would be a good
*  benchmark for a setting. Yeah. So I guess this also does highlight one of the other
*  nice aspects of this, which is I tend to think about a couple different kinds of systems.
*  Sometimes one would be this general purpose research assistant that I would need to send
*  out onto the web to find things for me. And then another would be like, and maybe these even sort
*  of converge in some ways, another would be like my own personal context navigator, right? Something
*  that can tap into my emails and tap into my Slack messages and hopefully kind of make sense of all
*  that and help me find the stuff that is really relevant. The nice aspect of this that maybe we
*  could sort of think about adapting or taking advantage of for these use cases is that it's
*  easy to like expand the corpus, right? It's highly extensible to say, okay, if there's a new record,
*  we can always just at runtime, like do a bit more pre-processing, do the entity extraction,
*  add a few more records to the graph database and then query. And in theory, that should work well.
*  So I wonder if you could take a system like this and instead of having like a totally predefined
*  corpus, if you could attack something like the Gaia benchmark with the addition of like some
*  web search, you could, I'm just thinking about past podcast guests here, we've done episodes of
*  a lot of different like research and kind of new approaches to search, but EXA comes to mind as
*  something that is like really good at finding sort of similar documents that can often be like off
*  the deep web. The Brave Search API is also another really good source for just really quick and pretty
*  robust results. And then there's Perplexity as an API and Elicit doesn't have an API, but certainly
*  has some interesting search technology. But I wonder if you could sort of set something up where
*  the agent has to, maybe it starts with like a seed corpus that could be like my own emails,
*  or maybe it starts with a English Wikipedia or something, maybe that's too big to get started
*  with. But if you had something that's kind of a start and then you allow it to go out onto the web
*  at runtime, find new documents and expand the corpus with those new documents to then try to
*  answer. And then in your iterative approach, it would be like, maybe you have to go back to the web,
*  not just to the locally indexed body of knowledge. This does start to look like something though,
*  that could really tackle a benchmark like Gaia, because from what I mean, to give you a sense,
*  I should read one of these questions. Here's one Gaia question that I recently tried. A paper about
*  AI regulation was originally submitted to archive.org in June 2022, shows a figure with three axes
*  where each axis has a label word at both ends. Which of these words is used to describe a type
*  of society in a physics and society article submitted to archive on August 11, 2016.
*  So it's this sort of, I mean, it's very much in line with what you're trying to achieve here with
*  this multi hop. I have to ultimately triangulate to define this one paper, I have to find this
*  other paper, I have to locate this thing after whatever. And then I have to figure out what the
*  overlap is. It seems like, I mean, that one's kind of a weird one because the connection is sort of
*  the last step, I guess, in that, at least as I think about how I would solve that problem,
*  I would probably make the, I would go all the way to the end of the one, and then all the way to the
*  end of the other and then like do the comparison last. But they have other ones too that are like,
*  maybe more suited for this. Here's another one. I'm researching species that became invasive after
*  people who kept them as pets released them. There's a certain species of fish that was
*  popularized as a pet by being the main character of the movie, Finding Nemo. According to the USGS,
*  where was this fish found as a non-native species before the year 2020? I need an answer formatted
*  as the five digit zip code of the place the species was found. That one seems like a little
*  bit more suited this way because like we're the sort of hops are sort of exactly the sort
*  of associations that one needs to make to reason from like Finding Nemo all the way through to
*  ultimately a zip code, it would seem like. Yeah. So it's kind of funny because I don't think the
*  distinction between path following and path finding is like very crisp in the current literature.
*  And I think that's like, honestly, one of the coolest like theoretical like idea based things
*  that Hipporak does is to kind of just very specifically define this distinction, because
*  both of those questions seem very hard, but they're actually just path following question,
*  because you there's like a bunch of details about what type of fish you're talking about, right?
*  Like, it's just the main character in Finding Nemo. And so you can like, literally just like
*  continue that number chain of thought, and you find that fish and then you continue the process,
*  the complexity of the question increases due to the number of hops, not really because of the nature
*  of the task. So the nature of the task in path finding questions is like set intersection, right?
*  And that's not something that you'd need to do in this case. It's just kind of interesting. Yeah.
*  And so, but like, if you wanted to use Hipporak in this Gaia case, you could do it with, as you said,
*  like searching the web, then doing indexing, but that's also going to take a lot of time,
*  like unnecessarily indexing a bunch of documents in your online step. So that's a little bit
*  difficult to motivate. I think it would be better to like, kind of figure out what's the corpus
*  that I need in this. Like, I think it's archive, archive papers for your first question,
*  maybe like Wikipedia and some other stuff for your second question. I don't know, like, I'm sure they
*  did it on some specific corpus. It would probably be pricey to index all of these documents. Like,
*  for example, all of Wikipedia, I think it's like 6 million articles or something. If we
*  just take the first paragraph of each of them, it'll be like $9,000 to index Wikipedia with
*  GPT 3.5. But that's just the first paragraph. So like, you can imagine that going much higher. So
*  that for one experiment, for one lab, that seems like too much. Right. So that's why I
*  think we need to figure out. Although by startup budget, it's extremely manageable.
*  It's extremely manageable. Yeah, exactly. For a startup or a production or like a big tech
*  company, then that wouldn't matter. So let's, I guess, for a second, look at any other weaknesses
*  or known shortcomings of the current approach. And then I'd love to just take all the
*  budgetary constraints off for a minute and just imagine what would we do if, not to say money is
*  no object, but let's say we have a substantial budget and we were going to try to build the
*  absolute best system that we could on either a public search the web basis or a My Context basis
*  or maybe even just say like a hybrid basis, right? Something where I'm going to give it a lot of My
*  Context that's like the starting base as needed. This hypothetical system can go out onto the web
*  and find more stuff. And then it has to use that, but also ideally incorporate that knowledge or
*  save what's relevant so that next time it doesn't have to redo it every single time. But first,
*  anything else in the current setup that you think is obviously calling out for improvement
*  or anything else that you're already planning to work on? So there's graph traversal. That's
*  one of these directions where I think that we need to improve it like ASAP. And then
*  I talk about it in the paper as well, the concept versus context trade-off, which it's like basically
*  the entity centric nature of Hipporag allows it to do a lot of these multi-help question answering,
*  like it allows it to do well on these benchmarks, but it's not necessarily super generalizable. So
*  if you look at the examples I used in the paper, there's one whenever a question requires
*  an entity to answer it, this is a great approach, right? But when there's one question in music
*  that's like about the person that discovered there's a unique number of protons in every element. And so
*  that doesn't have a named entity. And so the model kind of hallucinates proton as a named entity,
*  or as like an entity of some sort. And if you just start from there in the graph, you'll completely
*  screw up the results, right? So this is a query that requires a lot of context and a lot of
*  contextualization of the entities in the query. And so we're working on finding a better way to
*  map from the query to entry points in the graph. And that's something that a lot of people have
*  worked on in the past. So we're kind of playing around with things that people have done. And I
*  don't think it's an extremely difficult thing, but it's definitely a very obvious improvement
*  that I will have to go through. Yeah. So I guess starting to shift gears toward
*  imagining like the dream system that can do it all. One thing that kind of jumped out to me as
*  missing was the sort of outward in search, starting with the standard rag, right? It's like
*  some version of you have your passages embedded, you either embed the runtime query or people do
*  hypothetical answers that they then embed, whatever. But there's some sort of passage to passage
*  similarity search. So that was the first thing that I was thinking is like, why don't we also,
*  we're starting with the entities that's kind of starting at the core and fanning out,
*  but why not also like take the query, look for a sort of the leaf nodes, the original like raw
*  docs that sort of match that most closely and then use those as another place from which to
*  traverse the graph. Yeah. Yeah. I think that's a great question. So like our naive, like very
*  basic solution for this is to use ensembling, right? So you have a simple rag framework where
*  you get the top documents based on your query and you're using context and semantic embeddings
*  for that. And then you have hyper rag on the other side. So you can normalize the scores and then
*  combine or average them to obtain like kind of signal from both frameworks, right? But that's
*  like the naive, basic idea. The adding the nodes to your graph is something we've thought about. And
*  after working with PPR a lot and kind of having a feel for what works and what doesn't work,
*  that will add a lot of density to the graph and make it much harder to do any sort of relevant
*  traversal from it. So basically one node will be connected to all the entities that happen in that
*  known. And so if you give that node any probability, you'll just get like the probability distribution
*  will start being too spread out. And so it won't really work too well. But I think like the most
*  appropriate way to address those two things is with finding better ways to map the query to the
*  graph and then finding better ways to traverse through the graph and then like also ensembling,
*  of course. But I think in terms of changing the graph structure too much with that sort of
*  document specific embeddings, it seems to not be the best approach. I think this also kind of links
*  to how the hippocampuses works directly because you don't really map like the actual full memory
*  into the hippocampus and join it with a bunch of stuff. You map it, you represent that like full
*  memory with a bunch of different sparse concepts separated across the network. And that allows for
*  better associative memory pattern completion, something that we can like directly see in the
*  hippocampus. So that's interesting. So what's the problem that you're anticipating where if I do a
*  direct document to document comparison and then that matches with however many entities and then
*  that sort of creates like a very wide net, is that a problem for accuracy or is it a problem for cost?
*  Like when you are doing this with the current setup, how many tokens are ultimately getting
*  pulled back and put into the LLM for reasoning? And I guess I'm wondering like, if I sort of relax
*  that constraint, because one interesting data point on this is I've been using Gemini 1.5 Flash
*  recently to experiment with various ways of like post-processing my email history. And I've had
*  really good results with its ability to summarize, but it's summarized feels like I'm selling it
*  short. Basically what I've done, I've talked about this another episode. So briefly, I take the last
*  250 emails that I've sent, which for me turns out to be roughly a thousand tokens per email,
*  250,000 tokens. And then ask Gemini 1.5 Flash to write a character sketch of me based on those
*  emails. And it does a remarkable job. It gives me back like a two page, you know, here's this person,
*  what they care about, what they're involved with, the various projects, all from just this raw dump
*  of 250,000 tokens. And it's funny, this also goes to show how fast things are moving, right?
*  You published this paper in May, I think Flash was announced probably right around the time the paper
*  came out, which means you didn't have access to it at the time of doing the work. But that whole
*  analysis from the 250,000 tokens costs under 20 cents and takes like 40 seconds or so. And so I'm
*  feeling like the power of these very long context, very cheap and fast language models is maybe that
*  it allows us to cast a wider net through the graph and maybe not have to worry about it as much. I
*  mean, obviously you can still blow away past a million tokens if you're, or even now up to two
*  million tokens, you can blow away past that easily with a big corpus and a wide net. But anyway,
*  I guess like where were you when you did this project? Like how many tokens did you allow
*  yourself to ultimately consider? And how do you think that would change if I said,
*  hey, it's worth it to me to spend a quarter if I can get the right answer. So if I accepted
*  hundreds of thousands of tokens, how might that change things? Yeah, that's an interesting point.
*  So first, like what I was talking about with the document in the graph part is that's an
*  accuracy issue, right? So if you want multi-hop reasoning to happen within your graph, then adding
*  too much like density to it through adding a document node that actually allows the
*  probability through it, you'll add too much noise to the PPR and it won't be able to do multi-hop
*  reasoning in any significant way unless yeah, like in as it stands now, it wouldn't be able to do.
*  As far as your other question with long context LLMs, I think it's very interesting how good these
*  models are at synthesizing stuff from long context. So like in your framework and honestly,
*  I've seen this myself, like they can detect relevant things within that very long context
*  and use it effectively, but I am not super confident in their ability to get things that
*  are not actually directly relevant to what they're looking at, but only relevant because they did some
*  extra processing in some area of the long context in order to get that relevancy. So like basically
*  multi-hop reasoning within the prompt is still somewhat of a challenge. It's currently under
*  review, but I was working on this project that used long context LLMs for retrieval, like basically
*  answering this question, like can we just use long context LLMs for this multi-hop question
*  answering setting? And they are better than just embedding each thing separately. So compared to
*  RAG, like RAG just can't do multi-hop, but if you add this long context LLMs, they'll be able to do
*  the multi-hop to some extent. And we actually like see that in the attention patterns, but it's not
*  perfect. And as it increases in length, visibility drops. So I don't know how much of this multi-hop
*  process was happening in your 250,000 documents. I think if you look at the synthesis of the summary
*  that it created, I think you would probably be able to link each of the points it produced one-to-one
*  to some passage in your long context. I think they might even be like doing some aggregation
*  and summarization of multiple passages on multiple emails, but I'm not sure you're going to find some
*  extremely good consolidation knowledge. And I think that's the barrier that I see with these
*  long contexts or where they could improve, I guess. Is that recent work done with the Gemini 1.5 or
*  what were the models used? We were using different models. So we didn't get to 1 million tokens,
*  but we're doing like 40 or 80 passages even with GBT4. So it's like somewhat long context, but even
*  in the medium context, this is a problem. So in the very long context, I think it'll still be a
*  problem. That's my assumption. I haven't actually tried it with Gemini. So it seems like there's
*  got to be some way to bring back this. I mean, maybe you could say it's not needed, but it feels
*  like to me, I want to triangulate from both directions. My intuition is I want to start at
*  the entities and fan out, but I also want to see, is there something in this knowledge base that's
*  a very high match for what I'm looking for and just make sure that I also pull that in and use
*  that as some sort of a starting point? I guess you could imagine that they could be almost
*  quite independent. Maybe you don't need to fold that into the graph, but maybe you just do a
*  hybrid system where you sort of say, use Hippo RAG and then use simple RAG and just pull in the
*  top X documents and then put all that into content, augment what the Hippo RAG retrieves with
*  another form of retrieval and just make that the LLMs problem. But how, riff on this with me,
*  keeping in mind, I'm willing to pay a quarter per query if I can really get it right.
*  Yeah, if you can pay a quarter per query, basically an LLM could do the graph entries
*  probably very, very well. If we extract thousands and tens of thousands of
*  entities of potential nodes to enter through, or facts even, I think the facts might be even
*  better in this scenario. You get a bunch of facts from the knowledge graph that you created and then
*  you have your query and long context LLMs are clearly going to be good at finding the relevant
*  facts within this huge pile of facts, even in a huge knowledge base. Even if you build it on the
*  entire internet, I don't think you'll find like that many or like enough relevant facts to your
*  query that you won't find in the top 10,000. So if you have 10,000 facts, you can use Gemini to just
*  find the entry point to the graph very well. And then you're going to also probably do graph
*  traversal with the LLM fairly well as well if you don't care about cost that much. So I think it is
*  interesting to think about how to combine the idea of pre-processing your corpus with the
*  power of long context LLMs and just LLMs in general to do self-correction and also like
*  maintenance and kind of augmentation of this knowledge graph as you go because you also need
*  a lot of that like Raptor, Memwalker, GraphRag all do some sort of summarization of nodes
*  and I think that's probably also important in like a no bounds Hipporag setting. I would definitely
*  combine all sorts of ideas from those papers or basically with this like summarization and
*  consolidation of documents based on some clustering. So yeah, I'm by no means saying
*  that like long context LLMs don't have a role to play in a year. Obviously they have a role to play.
*  It's just about like how exactly how big that role has to be and like how far can we go without them
*  is also an interesting question I think. So yeah. I don't know. I'm very interested in Raptor as
*  well. I also think about the AI town project pretty often in this context where and again,
*  it's sort of like am I violating my no analogy rule here or not but what they did in that AI town
*  project is basically just periodically come through and create I believe what they called
*  reflective memories from the observational memories. So each little agent is walking around
*  having these interactions and just recording all the interactions and observations that it has.
*  And then it's like kind of reminds one of what seems to happen when we sleep where this memory
*  is like post processed and put into a more usable form where again, like some of the low level
*  details are abstracted away and this is where they start. I think they call it self notion in that
*  paper where the agents start to or I mean they're instructed to it's not like a spontaneous happening
*  but with the right setup, the language models are able to create sort of a sense of identity
*  that kind of integrates these different episodes and it's like this episode, this episode, this
*  episode add up to I like this person because of these multiple interactions that have happened.
*  And I think that is a really interesting concept as well. The Raptor one is less like
*  let's say less agenty and more just sort of takes raw passages, clusters them semantically
*  and then tries to create a sort of synthetic or higher level summarization of those clusters.
*  But then again, that's meant to sort of give you better ways into the graph, right?
*  You mentioned Flair also. I'm curious, that's not one that I've studied so
*  wonder what you could tell us about that. Oh, I don't remember the specifics but there's some
*  forward looking like framework that allows the model to determine if their retrieval was correct
*  or when to do retrieval. I don't quite remember exactly but yeah, it's just like in order to make
*  the retrieval more relevant to the generation part through forward looking. But the Raptor
*  and the AI town thing, so one of Hipperegg's limitations is that it only deals with explicit
*  knowledge. So any sort of things that are implicit or obtained from processing or summarizing your
*  explicit facts in any way. So for example, you record that like Cinderella lives happily ever
*  after but you don't record that the ending to the story is happy explicitly. Like that's just
*  something that you reflect on and you say, okay, yeah, this is a happy ending. And so I think
*  Hipperegg would definitely need some sort of, okay, let's look at the graph that we created.
*  Let's expand some nodes, create more relations, maybe delete relations that seem unnecessary,
*  kind of cluster happy ending stories together, make nodes about like the ending of a story,
*  all sorts of interesting like post-processing or maintenance of the graph that could be done
*  automatically with LLMs would be really interesting. And I think if money were no object
*  and I was focusing on like how to build the best Hipperegg or the best rag system out there,
*  I would pursue something like an automatically generated semantic web using concepts from Hipperegg,
*  concepts from Raptor, from Memwalker. And I think because the dream of the semantic web is
*  pretty great. And we really haven't figured out a way to do that efficiently. And so I think LLMs
*  provide a really interesting way to approach that. That I think should be capitalized.
*  It's an interesting phenomenon in general in AI right now that like the path to the small,
*  efficient models seems to pass through in some cases, the large models like Gemini 1.5 Flash
*  is reportedly distilled from Gemini 1.5 Pro or maybe even the highly anticipated Gemini 1.5 Ultra
*  that nobody has seen, but it's reported that it is distilled from a larger model. And I often feel
*  like even in the startup realm where people are more resourced to go after these sorts of things,
*  I often feel like people are too concerned with cost and latency, but especially cost.
*  I mean, latency has a more like, in my view, like a little bit more disruptive impact on the user
*  experience. Whereas if you can make it work well, typically I'm like, it's all pretty cheap. It's
*  all cheap relative to hiring it done. And my biggest pain point with all the AI products that
*  I use almost invariably is that it gets it wrong. So I'm like, just make it work right,
*  get the right answer, charge me whatever it needs to be to satisfy that. And then,
*  you can ride the cost trend down, I'm sure, or there may be sort of a similar thing with
*  distillation, which would be like, if we take some sort of maximalist approach, and we're willing to
*  spend a quarter or even who knows, a dollar, right? I mean, some of these questions that I
*  want to answer, it would definitely cost me more than a dollar to hire it done, probably a lot more
*  than a dollar to hire it done. So if I really care, I probably should be willing to spend a dollar.
*  And if the trends continue at anything like the recent history would suggest, then the language
*  model part is going to get a lot cheaper for free. And then maybe we can also use the system that's
*  working to sort of, you know, then prune off of that or otherwise figure out ways to kind of
*  make it more efficient. But it feels like maybe the path to that more efficient memory system
*  goes through a more like maximalist system where we're just like, let's give it every
*  trick in the book, and then kind of look back and see what tricks is it actually using in any given
*  case and then maybe can sort of layer on heuristics or other efficiency methods. Any reflections on
*  that or any coaching or you want to go start a startup together or what?
*  Yeah, no, I think that's a good general notion. Like, it doesn't matter how much it costs,
*  just get it right. I honestly feel that that's kind of what they're doing, but it's just very
*  hard to get everything right. Like a full generalization is still pretty much not
*  achievable yet. But I think this idea of like full indexing the internet is definitely worth pursuing.
*  And I'm sure I kind of think that Google is doing something like this, but maybe their desire to
*  compete with the super large language models is barring them from spending inference money on this
*  better index, right? But yeah, I think there's like technological improvements to Hibberag
*  that need to happen before we can actually use such a semantic web as well. And I think that's
*  kind of the more important things to address right now before we just like throw the kitchen sink at
*  it. Think about the big picture as you're building it, it's important. But because we have no idea
*  whether it's going to generalize well, even at the medium scale, we need to do that first.
*  I think any technologies that you would want to highlight based on your experience? I mean,
*  I think people are increasingly overwhelmed by just like all the different data ingestion or
*  like pipelining tools that are out there. I'm especially interested to know if you've
*  experimented with any in the multimodal domain, then there's like, which embedding models do you
*  use for things like this? Which vector database should you use? Which graph database should you
*  use? I don't expect that you'll have like encyclopedic knowledge because I don't think
*  anybody does in today's world. But any highlights, lowlights, you know, general findings, directions,
*  tips would be much appreciated. Yeah. So unfortunately, I'm not the best person to ask about
*  multimodal stuff because I've been working basically exclusively in text for a while. But
*  in terms of like embedding models, I was actually really surprised and impressed by Colbert just
*  like as a small model that generalizes super well. I think it like combines simplicity of BM-25 and
*  old information retrieval and like semantic and embedding methods really, really well. But if you
*  want more like higher performance and you're willing to pay a little more, I think there are
*  some other embedding models. Like I was pretty happy with Grit LM from Contextual AI. They kind
*  of have an instruction tune retriever, which is a neat idea where you can actually give it some
*  instruction to kind of shape your embedding in one direction or another. And so if the corpus that
*  you're embedding is kind of like documents about a specific thing and you're going to retrieve
*  like mainly from that corpus in one specific way, you can give it that sort of instruction.
*  And then it is more likely to distill more of that semantic information into the embeddings.
*  And so that's kind of nice. And it also has like normal generation. So it's like this hybrid model.
*  That's pretty good. I think in terms of like production level vector database, query databases
*  and that kind of stuff, I think that's also something that is better suited for another
*  person to answer since I don't work in like production level systems right now.
*  Okay, cool. How about on the chunking side? It just occurred to me, I appreciate I asked this
*  earlier, but I didn't have clarity on like, are you chunking these documents before doing
*  entity extraction? Or is there any chunking strategy built into Hipporack?
*  Yeah, so currently chunking was not really necessary because the passages in the benchmarks
*  are kind of small. Like you have two to four sentences per passage. And that is very reasonable
*  for 3.5 to figure out which triples are most important. And I honestly think that if you start
*  making this much longer, all models start like freaking out a little bit because you need to
*  keep track of what you've produced and like where in the paragraph they come. And then you can also
*  hallucinate relations between different sentences in the paragraph. And so I think it kind of becomes
*  maybe a little bit too complex. And so I would advocate for chunking with at least the current
*  version of Hipporack and current elements. Like, yeah, just a few sentences, a paragraph maybe,
*  and then like hierarchically summarize longer passages. But it's a really interesting question
*  because there's a current work called Longrag that kind of says, okay, let's just do knowledge
*  consolidation through no chunking. So you just like have all of the semantically similar documents,
*  let's put them together, and then just use an LLM encoder to embed those huge documents. And that's
*  how they solve this knowledge consolidation problem. And I think it's an interesting idea,
*  but in order to do better, the smaller the text snippets, the better attention you could
*  place on different chunks. So I think there's a trade-off there between a system like Longrag
*  and a system like Hipporack where you can have very small chunks, but then you can consolidate them
*  or like connect the ideas between them via preposition, basically. But for now,
*  it's just like two to three sentences. Okay, cool. Helpful. Maybe last question,
*  what other human capabilities do you see that you think appear to be unsolved in the literature?
*  Obviously, there are probably multiple critical things that we can do that the systems can't
*  yet do. But I wonder if you have any in mind that you've sort of isolated conceptually that you think
*  people should be looking into trying to design a system to fill these kind of, you know, what I
*  sometimes call them micro cognitive skill gaps that the AI systems still have.
*  Yeah. So like, there's a fun paper from some people from MIT, like Nancy Kanwisher,
*  Evelina Ferenko, that talks about how LLMs are really good at formal linguistic competency. So
*  they're very good at phonology, syntax, local semantics, right. But then when it comes to,
*  well, specifically, world knowledge is what we're talking about with continual learning, basically,
*  but also like formal logic, and like social reasoning. And so I think the biggest competency
*  gap apart from world knowledge that I see is formal logic, like, I think the bias towards like
*  system one reasoning, kind of like fast heuristic based reasoning, instead of like, more restrained,
*  more restrictive, like constrained reasoning is a huge problem for LLMs. And in the same paper,
*  they talk about how, like, this problem seems to be resolved through modularity in the brain. So you
*  have like, you definitely have a language circuit, right, that is mostly doing or it's probably doing
*  a lot of the system one, like language based reasoning. And then you have a bunch of other
*  modules, like, and one of them is more responsible for the system two reasoning. And so I think
*  there's also like the school of thought that this world knowledge and like formal logic competencies
*  are just going to arise from scale. And I think this is possible, but not guaranteed, in my opinion.
*  And so adding some sort of inductive priors of modularity, so you have like, different parts of
*  the system that are architecturally different, learning different things, could actually
*  accelerate this, the learning of more formal logic. And I think that idea, research wise,
*  is really exciting to me. And obviously, it's not quite clear how the architectures are,
*  like have to look like, but the idea that we need different architectures for different parts
*  and learning to happen, like using these two architectures or these multiple architectures
*  is probably the best path forward. Yeah. Cool. That reminds me of one that I've been
*  moving to study more deeply, which just came out of deep mind not too long ago called Transformers
*  Meet Neuro-Algorithmic Reasoners. And if you haven't seen this one, it's definitely kind of a trip.
*  They have sort of a hybrid structure where there's cross-attention between a standard transformer.
*  And this is not something I've really grok'd yet, but these neuro-algorithmic reasoners are
*  more structured, more graph-type entities. And they're still trained things, but they're
*  more structured, they're more principled, and they've been demonstrated to be good at solving
*  certain kinds of logical problems. And so then trying to kind of merge these together with some
*  sort of cross-attention paradigm seems like a pretty promising approach. But I can't say I fully
*  understood that yet or have an idea of exactly how I would apply it next. But for anybody who's
*  inspired by what you just said, that'd be one thing I would at least encourage you to check out.
*  Yeah, there's definitely a lot of directions in this big idea.
*  Well, this has been fantastic. Thank you so much for the time. Anything else that we didn't touch
*  on that you wanted to make sure we... No, I think we've covered a good amount. Thanks so much. This
*  was really fun. Cool. My pleasure. I love the work and definitely find it very thought-provoking and
*  something that I can see building into any number of future projects. So I appreciate it. And for
*  now, I will say Bernal Jimenez Gutierrez, thank you for being part of the cognitive revolution.
*  Thanks so much. It is both energizing and enlightening to hear why people listen and
*  learn what they value about the show. So please don't hesitate to reach out via email at tcr
*  at turpentine.co or you can DM me on the social media platform of your choice.

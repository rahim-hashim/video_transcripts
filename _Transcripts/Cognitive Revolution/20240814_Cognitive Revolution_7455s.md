---
Date Generated: September 06, 2024
Transcription Model: whisper medium 20231117
Length: 7455s
Video Keywords: []
Video Views: 1097
Video Rating: None
Video Description: In this special crossover episode of The Cognitive Revolution, Nathan Labenz joins Robert Wright of the Nonzero newsletter and podcast to explore pressing questions about AI development. They discuss the nature of understanding in large language models, multimodal AI systems, reasoning capabilities, and the potential for AI to accelerate scientific discovery. The conversation also covers AI interpretability, ethics, open-sourcing models, and the implications of US-China relations on AI development.

Subscribe to The Nonzero Newsletter at https://nonzero.substack.com and Podcast at https://www.youtube.com/@Nonzero/videos

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
(00:03:39) Introduction and Background
(00:06:58) AI Capabilities and Understanding
(00:12:22) Discussing Martin Casado's Views (Part 1)
(00:14:44) Sponsors: Oracle | Brave
(00:16:48) Discussing Martin Casado's Views (Part 2)
(00:21:51) Multimodal AI and Concept Representation (Part 1)
(00:31:40) Sponsors: Omneky | Squad
(00:33:26) Multimodal AI and Concept Representation (Part 2)
(00:38:05) AI's Potential and Limitations
(00:45:35) AI Safety and Risk Assessment
(00:53:31) AI Development and Global Implications
(01:03:30) Open Source AI and International Relations
(01:11:27) AI Ethics and Human Values
(01:22:06) AI Risk and Existential Threats
(01:31:21) Open Source AI Concerns
(01:38:20) China-US AI Relations
(01:48:36) State Space Models in AI
(02:02:32) Conclusion and Recommendations
(02:03:54) Outro


---
SOCIAL LINKS:
Website : https://www.cognitiverevolution.ai
Twitter (Podcast) : https://x.com/cogrev_podcast
Twitter (Nathan) : https://x.com/labenz
LinkedIn : https://www.linkedin.com/in/nathanlabenz/
Youtube : https://www.youtube.com/@CognitiveRevolutionPodcast
Apple : https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify : https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Understanding AI Understanding with Robert Wright of Nonzero Newsletter & Podcast
**Cognitive Revolution:** [August 14, 2024](https://www.youtube.com/watch?v=9EdR6AV7ky0)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today I'm excited to share a special crossover episode with Robert Wright, publisher of the
*  Non-Zero newsletter and host of the Non-Zero podcast. Inspired in part by my recent episode
*  with Martin Casado from ACE16Z, in which we debated how powerful AI systems are likely to become over
*  the next few years, in this episode Bob interviews me about the pressing questions surrounding AI
*  development, capabilities, and risks. We try to be as accessible as possible to a general audience
*  without shying away from technical concepts or critical questions that don't have easy answers.
*  We began with a discussion of what we know about the nature of understanding in large language
*  models and to what extent we can productively compare them to human cognition, and then
*  continued on to discuss a wide range of topics, including the development of multimodal AI systems
*  and their potential for more robust world modeling, the current state and future potential of AI
*  reasoning capabilities, the potential for AI to accelerate scientific discovery and technological
*  progress, the fascinating work being done on AI interpretability, including Anthropix recent
*  experiments with Golden Gate Clawed, the remarkable degree to which LLMs do understand human values
*  and ethics and why that's definitely not something we should take for granted, why I'm not advocating
*  for a pause in AI development right now, as well as what future developments could cause me to
*  reverse course and begin to do so, the emergence of new AI architectures like state-space models
*  and their possible implications, and finally, the pros and cons of open-sourcing powerful AI models,
*  especially as it relates to the increasingly fraught U.S.-China relationship and the risk
*  of an international AI arms race. On this last topic in particular, it's worth noting that just
*  keeping up with AI research and development is a full-time job, and I am by no means an expert in
*  U.S.-China relations, so I'm genuinely very uncertain about what U.S. policy should be
*  toward China with respect to AI. I'm instinctively very skeptical of the idea that we are the good
*  guys, and thus we should be the ones that humanity trusts to develop transformative AI systems first,
*  really for any possible meaning of we, including any of today's leading AI companies or even
*  the West in general. I do believe it's super important to continue to question the wisdom of
*  escalating tensions between major world powers, especially given the potentially transformative
*  nature of near-term AI developments and their obvious military applications. But I do hear
*  compelling arguments in many different directions, and there doesn't seem to be any truly safe path
*  forward. All I know for sure is that this topic is super important, and for that reason, while I
*  normally try really hard to ground my analysis in concrete facts and avoid saying anything that
*  could later be proven wrong, in this particular area, I feel like it's worth sharing new ideas
*  and testing new arguments, even while I fully expect that my position will continue to evolve.
*  As always, if you're finding value in the show, we'd appreciate it if you'd share it with friends,
*  post online, or leave us a review on Apple or Spotify. And I love hearing from listeners,
*  so please feel free to DM me on your favorite social network anytime. For now, I hope you
*  enjoyed this more speculative than usual crossover episode with Robert Wright of the
*  nonzero newsletter and podcast. Hi, Nathan. Hi, Bob. How you doing?
*  I'm doing great. Good morning. Good morning to you. Let me introduce this. I'm Robert Wright,
*  publisher of the nonzero newsletter to which everyone should subscribe. And this is nonzero
*  podcast. You're Nathan Labens. You're both an entrepreneur and a podcaster. You founded a
*  company called Waymark, is that right? That uses AI now, didn't originally use AI to help companies
*  come up with video marketing plans and so on. And so you're riding the wave, you're riding the AI
*  wave. And your podcast has really been valuable to me, Cognitive Revolution. Although my
*  comprehension rate is like maybe 65% on a good day, because your podcast is, you know, it's,
*  I don't want to say quite that it's for insiders, but you know, it's, you tell me what your kind of
*  business model is, but it's pretty high level discussion. You tend to have entrepreneurs and
*  a lot of actual kind of AI engineer type scientists, and you understand all this stuff.
*  And so you speak at a reasonably high level. And the way this conversation came about is I was
*  listening to one of your conversations, was fascinated by the subject, because it's something
*  of great interest to me. And I was thinking both, you know, I have some questions I'd like to ask,
*  to clarify things. Also, I thought it would be a service if I asked these like dumb questions,
*  and kind of brought the conversation down to a level, you know, where mortals can understand it.
*  So that sounds like a, did I did I flatter you too much? Or the opposite?
*  A little too much, I'd say yes. I, you know, with apologies to Tyler Cowan, basically,
*  what I'm trying to do on the podcast is just have the AI conversation I want to have. And
*  I do always warn people that it's, I don't classify it as entertainment. It is definitely
*  one for folks who are looking to learn and understand. And that's really the mission that
*  I'm on. It does take a, you know, a non-zero amount of work, to say the least, but I really
*  enjoy studying the subject. And, you know, I would definitely caveat any, first of all, I would say,
*  I don't think there's any stupid questions, because we're all racing to figure out what's
*  going on with AI. And everybody's, you know, coming at it from a different background and,
*  you know, catching up. We're falling behind, I'm falling behind. So I think we're all falling
*  behind to varying degrees and in varying ways. And the other important caveat is just that a
*  lot of stuff remains unclear. And so I'll try to flag, you know, what's kind of well established
*  versus what's my best guess. But we're very much still figuring out what is going on,
*  especially inside the AI systems. That's a very active line of inquiry, which I don't do,
*  but I do find fascinating and at least try to keep up with. Yeah. And I should say, you actually
*  are good at explaining things. It's just that often you're talking to somebody who doesn't need
*  them dumbed down. So you don't. Now you are talking to someone like that. So the subject
*  I want to talk about, I was listening to this conversation with Martin Casado, who is at the
*  VC firm Andreessen Horowitz. Like many people at Andreessen Horowitz, he thinks that there should
*  be very little regulation of AI. And there's no reason to try to slow things down or pause or
*  anything. And his rationale is that this stuff is really not as powerful as it's commonly presented
*  as being. It's not as advancing as fast as people say. And this in turn gets into the fascinating
*  question of like, what's going on inside these AIs? Is it very much like what goes on inside
*  a human brain in some broad, generic sense? And that's something I've written a little about.
*  In the non-zero newsletter, I wrote a long piece on the Chinese Room Thought Experiment. John
*  Searle's Chinese Room Thought Experiment. And while listening to your conversation,
*  I just had some kind of new thoughts and also some things that I wanted to get you to flesh out. So
*  before I start grilling you, anything you want to say about this or about that conversation?
*  Well, I thought that conversation with Martine was first of all, an encouraging instance of just
*  friendly and, you know, I'd say constructive communication across different AI worldviews.
*  I'm broadly, you know, I sort of try to maybe imitate the smartest people who I would say
*  generally admit a pretty high level of uncertainty as to what is going on inside the systems,
*  how fast things are going to continue to improve, you know, whether or not they may level off and
*  like what all the consequences are going to be. So, you know, when I look at like the leaders of
*  the leading developers today, and, you know, there I have in mind in no particular order, deep mind,
*  Anthropic and OpenAI, the leadership there is all remarkably frank that they don't have a great sense
*  of what's going to happen. Anthropic in particular has, you know, a couple of canonical blog posts
*  that they've put out that basically say, we really don't even know how hard the AI safety problem is.
*  You know, we started this company because we're really worried about it. It still could prove to
*  be reasonably tractable, or it could prove to be impossible. And we don't even have that question
*  answered for ourselves yet. So I try to follow that school of thought. And I think this very
*  quickly gets into like burden of proof type debates as well, because I think a lot of people can
*  agree that we don't really know. And then the question, you know, sort of becomes, well,
*  okay, if we're ultimately going to try to figure out what we should do about it,
*  we also need to be kind of clear on what our tolerance for various, you know, forms and levels
*  of risk are, because we're not going to nail down to zero risk or to 100% doom or whatever.
*  I don't think that's, you know, at all feasible right now. And anybody who's claiming those
*  extremes, I think is way overconfident. But sometimes, you know, there's just a lot of
*  ways that these conversations can break down. I at least thought that one was conducted in good
*  faith and good spirits. And I definitely appreciated that. But yeah, I remain extremely,
*  extremely humble in terms of my ability to predict. I often say too, like, we got to first,
*  can we answer what is and then move to what ought to be done about it? Even what is is like confusing
*  enough. Yeah. So he said something that is kind of in defending his claim that these machines are
*  in some sense overrated, that what's going on inside is less sophisticated than you might imagine.
*  He sometimes sounded a little bit like he was saying they were mere, quote, stochastic parents.
*  That's not his quote. But I got kind of that vibe. He said, look, it's just distribution in,
*  distribution out. You're just, you know, the machine is assessing structure in these symbols
*  that are fed into it, whatever, you know, predicting the next sentence. And I want to say,
*  in this conversation, I want to go well beyond large language models in the narrow sense of
*  processing human language, because I don't think you can talk about the question of to what extent
*  these machines will ever have something we can call understanding without getting into the
*  multimodal stuff. You know, the processing audio, video, even tactile and so on. But was your sense
*  that he was kind of saying, another term is just fancy autocomplete, right? All it is, is predicting
*  the next word that the average person who had uttered the first part of the sentence might say,
*  you know, based on statistical patterns in language. Is that to some extent his argument?
*  Great question. A little bit hard to pin down. I would say definitely there are,
*  there were moments where I would say it felt like that. And then there were other moments where it
*  did seem like he was giving the current systems a little bit more credit. And, you know, there was
*  sort of the, we talked about the Golden Gate Bridge, you know, or the Golden Gate Cod demo,
*  for example. We should say is just for background. So Anthropic, which has probably done more than
*  any of the big companies maybe to understand what's going on inside these things. But it,
*  you know, it found a way to tweak the LLM so that it could be inordinately interested in
*  certain things. And for fun, it made it kind of obsessed with the Golden Gate Bridge. So if you
*  said, how should I spend $10? It would say you should drive across the Golden Gate Bridge and
*  pay a toll. And that's Golden Gate Cod. So go ahead. Yeah. And what's, I think, really important
*  about that is that to make that work at all, they needed to understand how does the model
*  internally represent the Golden Gate Bridge concept so that they could inject that in a synthetic way,
*  no matter what you, the user, were talking about, and then induce that behavior. And so I think,
*  you know, this is an instance of the ability to pry open the black box, figure out to some
*  significant degree what's going on inside. And I always try to ground these things out wherever
*  possible, and it's not always possible yet. But wherever possible, I try to ground these ideas in
*  engineering. Can we actually use this in a way that shapes system behavior in a way that is
*  at least somewhat reliable? And with the Golden Gate Cod experiment, they did that. They showed
*  that they could isolate this concept and not just sort of hand wave or, you know, suggest, but
*  actually feed it back into the system and create all these compelling experiences where you had
*  an AI that was largely normal, but weirdly obsessed with this one particular concept.
*  And by the way, they could do subtler and less comic things, like make it more sycophantic
*  so that it would flatter you and praise you. They could kind of change the personality of the machine.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry,
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead
*  of variable regional pricing. And of course, nobody does data better than Oracle. So now you
*  can train your AI models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive
*  of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive. Oracle.com slash
*  cognitive. This episode of the cognitive revolution is sponsored by the brave search API.
*  You may know of brave as an alternative to Chrome. But did you know that brave has its own
*  independent search engine powered by its own 20 billion page index of the web? The brave search
*  API gives developers reliable and affordable access to programmable web search, auto suggest,
*  spell check, and more with flexible plans for all types of use cases from rag search to automated
*  business intelligence. On top of that, it's up to three times cheaper than Bing, all without
*  compromising on quality, speed, or reliability. Over 700 businesses, including Coheer, Chegg,
*  and Kagi rely on the brave search API. And a recent survey showed that 94% of customers
*  would recommend it to their peers. To start building apps with the power of the web,
*  sign up at brave.com slash API and get up to 5000 free monthly calls.
*  Yeah, they found so Golden Gate Bridge is one of I think, north of 10 million different
*  features they call them that they have isolated through this technique of sparse auto encoders.
*  The jargon here obviously can get out of control pretty quickly. But the basic idea is that the
*  models are they're large, but they're only so large in terms of how many parameters and numbers
*  they contain. And at each step, people don't know how much people will, you know, know about
*  the transformer, right? But the sort of most famous architecture right now that's driven,
*  you know, all the advances over the last few years, I would definitely put a pin in that and say,
*  I do not think the transformer is the end of history. But it has been, you know, the biggest
*  architecture used over the last few years. It's can it consists of all these layers.
*  Each layer basically has three core components. It has the attention mechanism. It has the MLP,
*  the multi layer perceptron, which is like one of the oldest, you know, things in in neural networks.
*  And then it has this activation function, which is a nonlinear function. And that is worth mentioning,
*  because people often say, oh, it's just linear algebra, there is something nonlinear there. So
*  just in a very technical sense, there is something that is a nonlinear function inside the transformer.
*  Anyway, between each of these layers, there may be, you know, dozens of layers in a big
*  transformer from start to finish. Between each one, there is an array that represents all of the
*  information array, an array of numbers that represents all of the computation, all of the
*  the results of all the computation that has happened so far, as the thing is proceeding
*  through its computation. And that is actually relatively small. That's often known as D model
*  in the literature. And it's usually something like 4000, 8000. The big ones can be like 16,000.
*  So all this information that is represented, that is the result of all the calculation that's
*  happened up to that point is represented in this single array of four, eight, 16,000 numbers.
*  Obviously, there's way more concepts in the world than that. And so the challenge becomes,
*  okay, how is this thing representing all these different concepts in such a small space of numbers?
*  And the answer is, it is packing them in very densely in ways that hopefully don't interfere
*  too much. You could say if I wanted to have perfect clarity, perfect interference, and I lived in a
*  world of relatively small, important concepts, you could have just one number represent
*  each number could represent one concept. And the sort of strength of that concept could just be
*  like, you know, how much the numbers activated, right? So you could have blue could be one and
*  red could be the other. And you could have blue turn up or red turn up. If they both turned up,
*  you know, that might mean purple. Okay, cool. But there's just too many concepts. So they've
*  done a huge engineering challenge to try to untangle this dense representation. They call this
*  poly semanticity because any individual position in that array of numbers will be activated for
*  lots of different concepts. And it's like, okay, well, maybe it's position one and 47 and 4000,
*  that together activate to represent a certain concept, how do they sort all that out?
*  It wasn't easy, but they've made a huge amount of progress. And now they've untangled to the
*  point where they have north of 10 million different features identified. Some of them are these like,
*  super clear, clean, you know, proper noun based things like the Golden Gate Bridge. Others are
*  a lot harder to parse. And I think there remains quite a bit of work to do there in the long tail
*  of concepts, because, you know, it's like, well, what is that? Is that something that we
*  is that something that the model has sort of learned that we might also want to be paying
*  attention to? In some cases, that could be the case. In other cases, it could just be sort of a
*  weird, you know, hard to understand thing. I mean, these things are definitely, in many ways,
*  quite alien. But anyway, going back to Martin, I mean, I think he did give a little more credit to
*  the notion that there were some concepts that were represented in meaningful ways,
*  I'll air quote meaningful, because what exactly is meaningful, but that these concepts seem to be
*  usable in engineering, he was willing to grant, then he still was sort of like, but key is,
*  we created those concepts, they're learning those concepts from us. And so I think where the real
*  sort of, you know, division, or, you know, let's say, almost continental divide in our worldviews
*  started to appear is where I was saying, I think they can probably do that, even if we don't have
*  the concepts. And you have to you have to look to other modalities to start to get a clearer sense
*  of that, I think. Let me give you kind of my tentative interpretation of maybe whity man,
*  but let's back up a little and talk about the difference, which I gather exists between
*  representing the meaning of the word, which is done via these so called embeddings,
*  and representing a concept. So for starters, I mean, to me, the amazing part about these models
*  begins with the representation of the meaning of words, because the models kind of invented the
*  system for doing it, right? And the, and I want you to comment on that, if you disagree, there is
*  kind of nuance there, because they were, broadly speaking, the structure of what they do was
*  given to them, but it didn't. Anyway, they let me just say that a problem with the phrase stochastic
*  parrots is that parrots can't paraphrase, all they can do is repeat exactly what you said.
*  And to even get to the point where you can paraphrase something, which may not seem very
*  impressive, you have to have a way of representing the meaning of words, right? You have to have this
*  intermediate layer, semantic layer that connects the word car to the word automobile or something.
*  And so the machines do that by locating words in like vector space. And it turns, and by the way,
*  there are people who think the human brain does it somewhat like this, I don't think we really know
*  yet. But so, you know, if you imagine just a two dimensional graph, and say we're plotting animals,
*  vertical is degree of lethality, horizontal is speed. Okay, so you've got kind of tigers are high
*  on both, you got kind of tarantulas high on one, low on one, rattlesnakes, and so on. So they're in
*  different parts of that space. Now these things map words in tens of thousands of dimensions or
*  just massive quantities. And they're not all semantic, I guess, some are syntactic. But the point is
*  they get the job done that way. And I think that's the first thing to understand about these
*  machines is that so one what you know, one phrase of Martins was, you know, it's just distribution in,
*  distribution out. Let me let me read you a quote of his. All it's doing is learning structure in
*  the text. It has nothing to do with underlying meaning. It's just structure that's in the text,
*  you can understand the distribution of text, you can spit out text. But this doesn't say anything
*  about learning fundamental principles of the world from which the text is based. Now I think
*  he may kind of be right about that. That's interesting, you know, because, you know,
*  John Searle in his Chinese room paper, the first thing he said was, well, he was talking about,
*  you know, he was kind of he wasn't talking about anything like the current models. But he was a
*  philosopher who back in the 80s or something mounted a famous argument that machines can't
*  understand things. And he said they can handle syntax, but not semantics. And he further added
*  that one dimension of semantics they can't handle is what philosophers call intentionality,
*  which is a very misleading term. It has nothing to do with subjective experience in philosophy.
*  This means being about something. So connecting a word to something in the real world. So and the
*  argument I made in this piece is, well, with multimodal AI, you can now do that too, right?
*  You can you can show the AI an apple in the real world and ask it what it is and it'll tell you.
*  So I think Searle's argument is dead, dead, dead. But at the same time, I think maybe
*  Martín is right to say that if you're just talking about large language models, and I should say I'm
*  not even sure that that's what he was talking about here. But I think he more or less for
*  practical purposes was if you're just talking about the processing of text, he's he's right
*  that although there is one aspect of semantic representation, they do handle, which I described,
*  still the part about connecting it to the world, which for us is part of understanding something,
*  right? They're not if you're just doing a text, they're not doing that. Right? Does that make sense?
*  I have no idea, I guess is a short answer. I mean, I could tell you a lot of details about,
*  you know, tokenization, which is sort of how language is broken down into its bits. And the
*  you know, the large language models typically have a finite vocabulary of distinct tokens that they
*  parse language into as they ingest it. And that's usually like 50,000 or 100,000 different tokens.
*  And then it's commonly understood that there's this process of de tokenization, where, you know,
*  a famous example that Neil Nanda, who's at DeepMind, and just one of the alongside Chris Ola and the
*  Anthropic team is, you know, one of the titans of the young field of interpretability. He often uses
*  the example of Michael Jordan, where both of those tokens, Michael and Jordan, and I'm not even sure
*  if Jordan to be clear is like a single token, or maybe that's two tokens, Jordan, or who knows,
*  right? I haven't studied to that level to know exactly what the vocabulary is. But it's clearly
*  multiple tokens. And yet, somehow, the model does understand that we're not just talking about,
*  you know, two random disassociated tokens, but actually knows like, okay, this is Michael Jordan,
*  and then loads in through all these layers, all these associated concepts. So I, you know, we can
*  we're getting and by the way, and talk about useful and engineering, really good paper out of the bow
*  lab, maybe a year or so ago, showed that they could even edit information inside a large language
*  bottle post training, you know, train the whole thing as normal, then go in there and tinker with
*  it in such a way where Michael Jordan could be made per the model to have played a different sport.
*  And they can make those edits in a way where the response that okay, Michael Jordan played some
*  other sport instead of basketball, you could make that edit in such a way that it's robust to
*  different ways that you answer the question. It's it doesn't apply to other basketball players,
*  you know, so Larry Bird and Magic Johnson and LeBron still all play basketball in this edited
*  model. So there's, you know, there's, we're getting decent at like, even locating this information,
*  figuring out how to edit it. I think I kind of don't know what it means in many of these cases,
*  when people say, Okay, but that has nothing to do with meaning or has nothing to do with the
*  real world. I mean, to me, it's like, it's clear that it has something to do with meaning as
*  something to do with the real world. I don't know how you would have such a rich representation
*  of the world without having some relationship to the real world. But then I think the question is
*  like, what is the nature of that relationship? And, you know, can we what what predictions can
*  we make based on different theories of that relationship? And you know, how can we test those?
*  And I do think we didn't quite get there in that conversation. So I'm not exactly sure how he
*  thinks about that. I do think that robots are coming. I mean, if I was going to try to venture
*  a, you know, something that seems like it might really move toward a resolution of this debate,
*  one thing you might say is, Okay, sure, these things can spit out text. And maybe they can even
*  take in imagery and spit out images. And yeah, maybe they can even take in audio and video now,
*  and respond coherently to all that sort of stuff. But they still can't. That's still, you know,
*  they still don't I don't know. Again, I'm not sure what it means to say they have that has nothing
*  to do with the real world has nothing to do with meaning. But one thing it might mean is,
*  they're not going to be effective, you know, they're not going to be able to actually move
*  around the world, they're not going to be able to do things in a functional way. And to that,
*  I would say, give the robot assists like two more years. And I would expect that we're going to see
*  quite good robots already today, you know, we've got robots that in the, in the deep mind case,
*  and metas doing this kind of stuff, too. And, you know, open AI has a partnership in this and Tesla
*  is trying to do it with their robot. Already, we have robots that can take verbal instruction,
*  look around at their circumstances, and try to follow your verbal instructions. They're robust
*  enough that they can kind of overcome perturbations. So there's a famous video from Google where the,
*  you know, experimenter says to the robot, like, go pick me up that bag of chips and bring it to me.
*  And the robot, you know, follows the instructions. And then when it gets to the bag of chips,
*  they knock it out of the robot's hand. And so now the robot, you know, it's just running this loop
*  of like, okay, what's my goal? What am I looking at? What should my next step be? And it's doing
*  that, whatever, a couple times a second, all of a sudden, the bag is out of its hand. And it's like,
*  I guess I better pick the bag up again. So this, you know, this sort of thing repeats where it seems
*  to have like a reasonably good robustness, even to these sort of, you know, perturbations. Now,
*  if you knock the thing over, it's not going to be able to stand back up. Certainly, it can still be
*  confused, like, certainly, it'll still drop the glass, you know, more often than you would want it
*  to and spill things. So they're kind of clumsy. But I guess my expectation, you know, one bet that
*  we might make or one, you know, hypothesis that we might falsify is that I would expect that robots
*  are going to get quite good over the next couple of years. And at that point, it starts to become
*  hard to say, okay, well, what real world are they not connected to that, that you really want them
*  to be connected to?
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it, and I recommend you use it to use cog rev to get a 10% discount.
*  Hey, all Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex-fang senior
*  software engineer as much as the next guy, but honestly, I can't afford them anymore. Founders
*  everywhere are trying to turn to global talent, but boy, is it a hassle to do at scale from
*  sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam. He's been
*  at a very high level for over five years to help you access global engineering without the headache.
*  SQUAD, Sean's new company, takes care of sourcing, legal compliance, and local
*  HR for global talent so you don't have to. With teams across Asia and South America,
*  we can cover you no matter which time zone you operate in. Their engineers follow your process
*  and use your tools. They work with React, Next.js, or your favorite front end frameworks. And on the
*  back end, they're experts at Node, Python, Java, and anything under the sun. Full disclosure, it's
*  going to cost more than the random person you found on Upwork that's doing two hours of work
*  per week but billing you for 40. But you'll get premium quality at a fraction of the typical cost.
*  Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squad.com and mention Turpentine
*  to skip the waitlist. And that's kind of that kind of gets to this concept of intentionality.
*  Like in other words, it's one thing to represent the words in semantic space as these models I
*  would say do multi-vectorial or whatever the term is semantic space. It's another thing, you know,
*  and by the way, I gather they do if words are ambiguous, you know, like apple the fruit,
*  apple the company, they're located in different places. And then the machines use context to
*  determine which one of those they want to hone in on, right. And, but it's one thing to do that.
*  What Searle would say, if he's emphasizing the quote intentionality is, but you have to know an
*  apple when you see one. Okay, that's a different matter. And a large language model in the narrow
*  sense doesn't do that. But these multimodal models obviously do. And you can well, it sounds like
*  you may made dissent from that. Go ahead. No, I just think I think that even that claim of you
*  have to know one when you see one, I think that we just have a very sort of trapped sense of like,
*  what, what counts in many of these instances. So I would immediately came to mind, you know,
*  as we're doing classic thought experiments, what about a bat? If a bat flies around a room and
*  emits its signal and gets a signal back and can identify an apple from that, like, does that count?
*  I can't do that. Does that mean the bat has some way of knowing that I don't know? I would say,
*  yeah, it does maybe have some way of knowing that I don't know. But I can also taste it, you know,
*  can the bat taste it? Maybe it can, maybe it can't. I don't know if it has teeth to bite into an apple.
*  So, you know, I think there's just a lot of different ways of knowing. It seems looking
*  around at the animal kingdom, I see just incredible diversity that is probably underappreciated. I do
*  tend to think these and most of these animals are conscious in some sense. I have no idea really,
*  if language models are conscious or not, that's a whole other can of worms. But I just think there's
*  a often a very narrow concept. One of my, you know, I amused myself with this tweet, if nobody else,
*  but I recently tweeted, it's only reasoning if it comes from the reasoning portion of the human brain.
*  Otherwise, it's just sparkling brute force search. I think you could say something similar about
*  understanding, like, I understand in some way, it's not a universal understanding. It's not, you know,
*  I'm not one who believes in some, you know, single overarching God that it would have the
*  platonic understanding. But if there is such a thing, clearly my understanding is not that.
*  And yet it counts, you know, it's functional. The bats version is functional for it. The robots
*  version, if it's functional for it, like, I don't know on what basis we're going to still try to wall
*  off and say they don't understand if they can do a lot of things. And I don't think they have to do
*  exactly the same things that we can do to be reasonably understood as understanding, understanding
*  differently, perhaps understanding very differently, perhaps as we open the black box, we'll find that,
*  man, this is really weird and not at all how we thought it was going to work and totally
*  counterintuitive. I think in general, less counterintuitive, maybe than, you know, than our
*  worst fears. But I think then we're confronted with something where it's like, this becomes a
*  different form of understanding, we can maybe develop different vocabulary words for that. At
*  that point, you know, we could call it understanding star, or we could call it, you know, AI understanding
*  or whatever. But I think, you know, if you imagine this sort of going back to your kind of, you know,
*  many, many dimensional conceptual space, what the robot is doing seems like it's in the, you know,
*  the general region of this vast conceptual space, you know, nearby to where my version of
*  understanding is. Certainly, you know, there are many other things that are far, far more
*  different from my understanding than the robot understanding. So I think it matters really to
*  pin down those differences. You know, I don't think we should jump to the other. The other mistake
*  would be to say, oh, it's just like us. I don't think we should jump to that conclusion either.
*  But it's just like, you know, we just have a lot of work to do to answer these questions. And
*  unfortunately, they're probably not going to be answered with sentences, you know, they're going
*  to be answered with like metrics and a variety of different ways to try to get at the problem,
*  which will still probably ultimately kind of feel incomplete because just like we don't know what
*  it's like to be a bat, we're probably not ever going to know what it's like, if anything, to be
*  a robot, or at least I don't see any path to that right now. But again, that doesn't mean it's not
*  understanding in some meaningful way. Right. But I mean, as long as you brought up that phrase,
*  what it's like to be a bat, that of course, famous paper by the philosopher Thomas Nagel about
*  consciousness and among other things, it's just it's a definition of consciousness. It basically says,
*  if it's like anything at all to be this being, then that being can be said to be conscious,
*  have subjective experience, and so on. I want to emphasize, I am intent on defining understanding
*  independent of the question of whether there is consciousness or subjective experience,
*  because as you said, we just don't know what's going on in these machines. In the piece I wrote
*  in nonzero about the Searle thing, I tossed out this, this, my own conception of understanding,
*  I said, understanding means processing information in broadly the way human brains
*  are processing information when humans are having the experience of understanding.
*  It doesn't matter if the computer is having the experience, but if it's processing information
*  broadly the way and by broadly what I meant was like, so humans must have a system for representing
*  the meaning of words. That is one element, not the only element of what we call understanding.
*  If computers have such a system, then they have one element of understanding. That's the way I
*  would put it. These LLMs clearly have that and impressively, they kind of invented it.
*  They came up, I don't want to get into details, and I suppose you could argue about how much
*  creativity they exhibited given the constraints on the way they work when they came up with this
*  kind of multi-victorial. They didn't come up with the idea of multi-victorial. That was
*  that was built into the machine. So I want to emphasize, I'm not,
*  and a lot of people just can't think about understanding without thinking about subjective
*  experience. I would say, fine, but I can't help you. I just don't, it doesn't seem to me to make
*  sense to talk about this question if subjective experiences are prerequisite for understanding
*  as we use the term. So I want to get into more into multimodal, but first I want to say
*  there's one other thing that Martine may have been saying either here or elsewhere in the
*  conversation, which I think is interesting and may have validity, and I'm sure you've thought about
*  this, which is that, well, the way I'd put it is even if you grant that they have the elements
*  of understanding, they're training on text created by human beings. They are translating
*  the accumulated body of human knowledge into a system of representation that they can work with.
*  And if nothing else, I think he would say, since he's interested in emphasizing the limitations on
*  what these things may ever be able to do, you could argue that that puts a kind of ceiling on
*  what these things can ever do, right? When we think of super intelligence, we think of something
*  smarter than a human. But if you're training only on text generated by humans or on these,
*  this synthetic text, it's generated by machines, emulating humans, you're not raising the
*  ceiling, right? You're just as smart as a super smart human. Now, that would have vast implications
*  since these things are infinitely replicable and could be as smart as the smartest human ever and
*  know everything ever known. That would be kind of important, but it does raise questions about
*  whether suddenly they'll say, oh, I've resolved the wave particle paradox in quantum physics,
*  right? I'm sure you've thought about this. Yeah, I have a lot of thoughts on that.
*  I think you're right, first of all, to emphasize that merely achieving high end human performance
*  is enough to be transformative to work, life, play, society, future. I'm often
*  reminded of the old joke or a cartoon where two guys are running from a bear in the woods,
*  one stops to put on his running shoes, and the other guy's like, what are you doing? We've got
*  to outrun this bear. And he says, I don't have to outrun the bear. I just have to outrun you.
*  And so I do think we're not always thinking super clearly when we think if it only is as
*  good as the best humans, like that's no big deal or something. I don't know that people are really
*  saying that, but it does seem to be this sort of notion that, oh, if it levels off at the top of
*  the human distribution, then that's not such a big thing to worry about. I do not share that intuition.
*  It does seem like that is a plenty big deal. And it brings all the questions of like a linemen and
*  control and whatever. All those things seem very central in a world where we have human level
*  AI that's generally capable. I also think that this is debated, but I do think if you could
*  match humans on all the things that humans are good at, it seems quite likely to me that you
*  would find that the things that machines are already way better at would give them major
*  advantages over us in ways that are going to be very hard for us to figure out how to counteract.
*  And I hear I'm just talking about runtime. They can already generate text faster than we can read
*  it. They can read probably, depending on exactly which model, whatever they can read, potentially
*  orders of magnitude faster than we can read. They have kind of brittle memories right now. I think
*  our integrated memory is definitely still one comparative strength of human cognition relative
*  to machine cognition. But they also have like vast hard drives that are sort of stable and can be
*  returned to. And if they can figure out how to use those well, that's something that we're going to
*  have a hard time matching. Elon Musk has said repeatedly that his goal with Neuralink is to,
*  in the short term, yes, treat people who have suffered catastrophic injuries and restore
*  quality of life. But bigger picture, it's to increase the bandwidth with which humans can
*  communicate with machines, because right now we're limited to typing into them or talking.
*  And presumably there's a lot more going on. Almost for sure, there's a lot more going on
*  in our brains. Much like there is inside the language models, there is a richness of the
*  representations that is happening internally that can't be communicated entirely through words.
*  Right. I think this we can sort of see by just introspection that we can kind of feel like
*  I had a feeling I couldn't quite articulate it or I came close. Maybe I was even happy with my
*  articulation, but still something lossy happened there in the reduction of the full richness of
*  thought down to the few syllables that were uttered. So he hopes that we can maybe keep up
*  with machines, or I think he's used the phrase go along for the ride by creating some mechanism
*  literally implanted into our brains that would connect directly into that richness of not
*  necessarily experience, because we're not even fully conscious of that all the time, but would
*  at least connect into that processing and enable higher bandwidth communication.
*  So I think that's really important. I don't know, and I think there's definitely real reason to be
*  unsure as to do these things sort of level off-ish at a kind of high end human level, or do they go
*  way beyond? The case for leveling off is basically like what you said, they're learning from human
*  data. How are they going to get better than the data they're learning from? I think the case that
*  they go way beyond is that they can also learn from things that are beyond human data. We see this
*  in a lot of narrow systems today. AlphaGo famously is one where they had the AI play itself in Go and
*  gradually get better through just a process of self-play to the point where it became superhuman
*  and created these moves that blew people's minds. And so now you're kind of chipping away at this
*  notion, okay, well, maybe it can be superhuman at that, but okay, but that's just a game. Okay,
*  fine. Now we can go to protein folding and we can say, humans do not have, to my knowledge,
*  no human has ever demonstrated the ability to look at the genetic code or for that matter, the
*  sequence of proteins that that genetic code corresponds to and be able to guess what the
*  in vivo three-dimensional shape of the protein is going to be. We have done a ton of work to
*  figure that out for a very small set of proteins. I mean, tens of thousands, but like small in the
*  grand scheme of hundreds of millions of proteins out there in nature. And with that data set,
*  still no human was able to kind of just look at that for a while and develop an intuition for it.
*  But we now have AIs that can do that. And so again, we're like, oh geez, that's pretty
*  impressive. That's definitely way superhuman. No human is doing this, but the AI can. Okay,
*  but well, that's still pretty narrow. Well, what if we go to predicting the weather?
*  We have humans that go to school and become meteorologists and use all these instruments
*  and try to figure out how to predict the weather. And again, we now have an AI that is the best at
*  predicting the weather. It takes in all these sensor measurements from around the world and
*  puts out a state of the art best available 10 day forecast. Okay, well, how many of these things
*  do we need to go on? There's another one too with solution data where we do have the ability with
*  simulation to proceed just like at these, I think it's like femtosecond scale where people simulate
*  the liquids at the atomic level. And it's super compute intensive, but we can at least run that
*  in a computer simulation. Humans can't do it in our own brains, but we can code computers to do it.
*  But it's super slow. I had a recent episode with a guy who had turned into neural network
*  to basically do that, solve the wave equation. You mentioned the wave equations that brought
*  that to mind. Solve the wave equation for like a bunch of particles all kind of in random
*  configurations. And again, to do that orders of magnitude faster than the pure simulation.
*  This was one important note, I think, in the Martin conversation where he was sort of saying,
*  if you really want to predict the world, you have to simulate the world. There's no way to make these
*  predictions outside of actually running the full numbers. And I do think we're starting to see real
*  instances of that being shown to just not be true. Like the old way of trying protein folding was
*  super computationally intensive. And it was like, we're going to try to calculate all the forces
*  that are interacting and do that stepwise, stepwise, stepwise until we reach the actual
*  folded state. And same thing with these solution simulations. The AIs don't work that way. They
*  take in an initial configuration, they process it, but they use way less compute than you would use
*  to do every single step. And they still get out a similarly good output. So they are learning some
*  sort of structure that they're able to use to take major shortcuts through what otherwise would
*  be brute force computation to get to a right answer. And so, I mean, how many of these things
*  do we need to do before we have something that we say, geez, that starts to really look superhuman?
*  And you could also ask how integrated they need to be. AlphaGo is standalone. It can't also
*  write you a computer program or compose you a poem or whatever.
*  And the same thing, the weather thing is narrow and many of these things.
*  It shouldn't be hard to come up with an interface that will direct you to the...
*  Yeah, yeah, exactly. If they are integrated, I think all bets are off.
*  Right. And I don't know what... Well, I guess there's two kinds of integration. I'm kind of
*  fuzzily thinking this is a good example of what you said about you've got this idea, but
*  you haven't put it into words. And it's interesting, the irony that, as you said,
*  in some sense, there's the feeling that boiling things down to language oversimplifies them. At
*  the same time, being forced to do that can clarify your thinking. And it's a weird thing. So let's
*  talk about this related issue of multimodal. And let's just take the text to video stuff. So Sora
*  OpenAI, I don't know how many months ago, blew everyone away. Have they actually released Sora?
*  Can I go give Sora a prompt and get a video or is it still vaporware?
*  No, not yet. It is released to a small number of creators who have done some stuff with it. So I
*  think they've demonstrated that it is not vaporware, though it's still very limited release. It's said
*  to be still quite slow. I think one of the main reasons they maybe haven't released it is that it
*  is expensive to run. And they are maybe not keen to devote as much compute as they would need to.
*  Vaporware is unfair. I mean, that's a term people use for software. It hasn't even been
*  demonstrated, I think. But anyway, the question arose, what kinds of internal representation,
*  if people haven't seen this, you can say, show me a golden retriever playing frisbee with a frog
*  or something. Whatever you say, it seems to be able to do a not bad rendition of it. There are
*  glitches, weird kind of magical realism happens in little corners of it. But it's pretty impressive.
*  And the question is, I guess, still debated, what's going on inside these things? Are they
*  building a model of the way the physical world works? In other words, we don't think about it,
*  but as we navigate the physical and visual world, we must have certain intuitions about the fact
*  that if you let go of something, it's probably going to fall and not rise. If you put something
*  in motion, it goes for a while. But in general, lots of things just stay in the same place.
*  And as you move through the world, they kind of need to stay in the same place with respect
*  to one another, even though they're changing. There's a lot of things we don't think about,
*  but we must, these assumptions about the way the world works must be kind of built into our system.
*  And I don't know what else you'd say about, I mean, yeah, I'm not sure I really have hope.
*  To you, what does it mean to ask whether Sora is building internally a model of how the world,
*  a kind of intuitive physics or whatever people call it?
*  Yeah, I like that phrase, intuitive physics.
*  I think AI is probably going to have, ultimately, this is something I've been thinking about just
*  the last couple of days. My guess is that we're going to see AI that has way better intuitive
*  physics than we do. And that will be yet another of these sort of before and after moments where
*  it was like, wow, we used to think they couldn't do this. And now it turns out not only can they
*  do it, they can do it really well. You know, we are obviously a very, very, very, very, very
*  advanced, obviously evolved over a long, very long period of time and many, many generations
*  to make our way in the world. And so there's been incredible pressure on us to figure out,
*  and I don't mean as individuals, but through the long evolutionary history, like, what is that?
*  Do I need to be scared of it? Can I eat it? Do I need to run from it? And so we have these
*  like, you know, intuitive physics modules that are not real physics, right? They're not like,
*  I guess they're real and that they're at some level of, you know, simplification of real physics.
*  They are correct. But you can certainly go deeper, right? Of course, we tend to think of the world as
*  like three dimensional space. We know from general relativity that that's not quite true. But, you
*  know, in our local environment, it works for us. And, you know, we're quite good at, you know,
*  identifying the tiger, right? Like we have these certain things that we're like very specialized in.
*  The AI has not been subjected to that kind of pressure. It's really just been subjected
*  to predicting the next, you know, token in the case of language models or the next frame in the
*  case of the video and trying to be as accurate as possible with that. And so it's not a surprise that
*  it would have different strengths and weaknesses from us in terms of what it can do. But it does
*  seem very likely that there is some form of intuitive physics developing there. The one
*  example that they showed of a pirate ship in a teacup or whatever, where, you know, this little
*  ship is like sloshing around in a cup and the waves of the coffee are, you know, tilting the
*  ship up and down and it's rocking and rolling on the waves and the waves are bouncing off the sides
*  and coming back. You know, is that, what is that? It seems like it's probably some sort of intuitive
*  physics. I mean, it certainly obeys, like it passes, you know, you have to look really hard to find
*  ways in which it doesn't pass the sort of that looks real test. You know, it's clearly not
*  simulating every particle of the liquid. You know, I think this is where we see at least some
*  divergence from the idea that, you know, to simulate nature, you have to run every
*  computational step. It does seem like it's got some sort of shortcuts that are happening in there.
*  And we just don't really know what they are yet for multiple reasons. One is that OpenAI hasn't
*  released it. So, you know, nobody outside of the small number of people can even use it,
*  let alone dig into its internals and try to open the black box. I'm sure they're doing that
*  internally and trying to figure out what sort of intuitive physics does it have. But the rest of
*  us are left in the dark for now, at least. But I would expect, I mean, just to cash it out,
*  you know, what do I think is happening? I think it has some intuitive physics. I think it's different
*  from ours, reflecting the fact that it was created under different pressures. And in some
*  ways it is better. I can't draw, I can't visualize those waves with that level of accuracy. It is
*  better than I am at simulating what a little pirate ship in a teacup would look like, you know,
*  if all of a sudden it's riding these little waves. So in some ways it's better. In some ways it's
*  worse. You know, it probably is not, I wouldn't want to delegate recognizing a tiger to it,
*  but I'm highly optimized for that as compared to it. So, you know, we're just, we're different.
*  Again, I think we kind of are probably, I don't love analogies, but I sometimes think of this,
*  I have a sort of visualization of some abstract space or shape that is reality. And then a model
*  of that almost being like shrink wrapping some rough initial fuzzy understanding, you know,
*  pulling the vacuum tighter and tighter and shrink wrapping your model, your wrapper around reality
*  down to that core underlying shape. And I think we're just coming at that from very different
*  directions. You know, the AI and humans are, we've both done that in some way. And I apologize for
*  using an analogy, but we're just doing it in very different ways, coming out of very different
*  starting positions. Yeah. So, but it does seem to be a fair surmise that, you know, just as with the
*  large language models, if you just fed it text and trained it to get good at predicting next token,
*  and then also to actually carry on conversations by using that same technique, you know, just as
*  it turned out that it had to, in order to accomplish that, it had to build a system of semantic
*  representation, a system of representing the meaning of words, that at least in some broad sense
*  must be comparable to the way we do it, even if ours isn't this multi-dimensional thing.
*  Broadly speaking, that function had to be carried out, the one in our brains carry out, had to be
*  carried out. It seems to me it's a fair surmise that for this thing to turn text prompts into video,
*  it must be performing, and you know, there must be some functionality in there that at some broad
*  level is comparable to some functionality we have, right? I mean, does that make sense?
*  Yeah, I mean, I think you can look at this with, you know, different levels of abstraction on a
*  functional level. That's almost like definitionally true, right? If it can, it can, I mean, I mean,
*  functionally comparable to things about our own mind that we don't really totally understand.
*  I don't mean just functional in the sense that it can perform, you know, I mean, like our system
*  of representing the meaning of words has a function that is, you know, beyond the strict function we
*  expect the machine to perform when we train it to predict the next token, and the machine had to
*  build that function, the semantic representation. I'm suggesting it must be something comparable
*  in Sora, you know? Yeah, I think there's, I mean, I think we really don't know. We might soon be in
*  a weird position where we might understand how the AIs work better than we understand how we work.
*  One, there's multiple reasons for that. One is that we can perform experiments much, much easier
*  on the AIs than we can perform them on ourselves. At least for now, we don't have any, I'm not saying
*  we should, although maybe at some point we should, but for now, it doesn't seem like we
*  need to worry too much about the ethics of experimenting on AIs, whereas obviously we do
*  worry about that for ourselves. So we can, you know, the term in the literature is ablate,
*  and that just basically means delete or sort of zero out or like put noise into a particular
*  position. So a lot of what people are doing when they're doing these experiments to try to figure
*  out what's going on inside an AI is like, delete a part or make this part all zeros or make this part,
*  you know, random and just kind of see what happens. Obviously, we can't do that to ourselves in the
*  same way. Another reason is that the architectures are way simpler on the AI side than they are
*  for us. I think that's another thing that, by the way, should give us real humility about what might
*  come next, because, you know, I described the three parts, the three core parts of the
*  the core layer of the transformer, and those are stacked on top of each other.
*  And you can basically spend an afternoon and get a pretty good understanding of what the structure
*  of a transformer is. The brain is way, way more complicated than that, has way more different
*  parts, way more different subunits, has like, you know, cyclical feedback systems, you know,
*  things that sort of crosstalk in all kinds of weird ways. And so, you know, that's where I'm like,
*  geez, I don't know, I think there are there are some things, it seems pretty clear that we have
*  these, you know, probably somewhat analogous conceptual representations, you know, when I
*  think of Apple and I think of the company versus the fruit, you know, it is the same token. That's
*  true for the language model, too, you know, the same token of Apple can be, you know, input or
*  output. But it too has some sort of distinct representation of the company versus the fruit.
*  And depending on context, and, you know, in a similar function, at least a functionally similar
*  way to how we can sort of call to mind all the associations that go with one or all the
*  associations that go with the other. The AIs can do that too. So there's, I would, you know, be
*  pretty confident in saying there's some analogous types of things going on. But the structure is
*  totally different. So exactly how similar those things are, at a, you know, at a mechanistic level
*  is really hard to set, you know, might be the case. And people know a lot more about neuroscience
*  than I do. I actually don't know that much about neuroscience. But, you know, from a naive perspective,
*  you know, it's almost for sure not the case that all the calculation that is happening in
*  my brain is getting bottlenecked through this activation, you know, which is that what we talked
*  about earlier, the sort of array of numbers that sits between, you know, that is the intermediate
*  result between these layers of computation in the transformer. I don't think I have anything like
*  that. I don't think there's ever any single thing where you could go and say, okay, these, however
*  many neurons, this represents a clean intermediate state that is the result of all calculation that's
*  happened so far and where we could pick up from this, you know, this particular, you know, finite
*  representation and carry on from there, you know, with only that input needed. I don't think we have
*  any, I would be very surprised if we have anything like that. So, you know, it becomes very fuzzy to
*  me. And I just sort of expect that just in the same way that we, you know, there's going to be a ton
*  of detail and a ton of nuance and a ton of idiosyncrasy on both sides, but it probably plays out
*  very differently. Can I ask you to talk a little about the distinction between
*  representing the meaning of words and representing concepts? Because when you locate the word apple,
*  the fruit, in semantic space, you are in a sense representing a concept, right? I mean, you are
*  assigning it to all these properties, roundness, you know, sweet taste and so on that are probably
*  represented by different dimensions. And that's kind of a representation of a concept, but
*  the work they did at Anthropic and other people have done, you know, Dan Hendricks, I think, did some
*  work on this earlier. And in representing concepts, that can be different. And I guess I don't
*  totally understand, you know, when they talk about a pattern of activation or whatever. I mean, I can
*  understand locating something in multi-dimensional space, where the dimensions represent aspects of,
*  you know, represent properties. But when they start talking about these patterns of activation,
*  it's less clear to me what's going on and also less clear, I guess, when that would become relevant.
*  But I don't know, does that, have you thought about this or does it even make sense?
*  Yeah, I mean, I guess maybe for one thing, sort of some intuition for what it means to be representing
*  a concept in this high dimensional space. So say you have 8,000 numbers that sit between the
*  layers of computation, right? These are these intermediate results. And this is often,
*  not exclusively, but this is the current study of the sparse autoencoders is, what can we
*  tease out and identify from these intermediate calculation results? I think there's a famous
*  guy, if it's a cartoon again, or just a joke, but, you know, how do physicists visualize high
*  dimensional space? The answer is visualize three dimensional space and then say N really hard.
*  And then, you know, the joke is like, don't worry, everybody does it. So, you know, I think I'm
*  putting myself in hopefully good company there where I would say, my visualization of the space
*  in which concepts are located is, you know, because I'm a three dimensional creature, it's
*  still pretty three dimensional, I sort of just envisioned space as I know it. And just different
*  regions of space, clusters of space where similar concepts are grouped. And then you just have to
*  kind of remind yourself that actually instead of three dimensions, which is easy enough to visualize
*  for most people, many people, that it's 8,000 dimensions or it's 16,000 dimensions. And
*  obviously at that point, whether it's eight or 16,000, you know, doesn't change my visualization
*  all that much. At some point, it just does become sort of a parameter of the system. So
*  you know, the that that space is obviously vast, it's weird, it, you know, it has sort of weird
*  geography or weird geometry, maybe is a better word to use. And, you know, things can be close
*  to each other in some dimensions and far from each other in other dimensions. And, you know,
*  I don't know, that's all that's kind of weird. That's what it is that there. I'm not sure that
*  there's too much more to say than that, other than what's really interesting about this,
*  this sparse autoencoder work is that it's essentially a transformation of this
*  geometry where we have, we have some, you know, again, 8,000 dimensional space, and we've got all
*  these points, which correspond to all these concepts grouped through that space. What they're
*  essentially doing with the sparse autoencoder is saying, what if I tried to pull that out into one
*  long line and put every single concept every single point in that high dimensional space,
*  what if I just tried to make each of those a point on a line? Could I make a transformation like that?
*  So now instead of representing each concept by 8,000 numbers that located on 8,000 dimensions,
*  can I just identify that same concept with one number that just identifies its place on this long
*  line of concepts? And the answer is, you know, it wasn't obvious that that would be doable,
*  but they have done that. And that's how the Golden Gate cloud thing works. So, you know, it's,
*  could we do something similar in our own brains? My guess is yes. But it would instead of having an
*  8,000 dimensional space, we probably have some really weird thing that is, you know, again,
*  because we have different regions of the brain and they're cross talking with each other and there's,
*  you know, homeostasis is going on. And, you know, signals are coming from the rest of the body.
*  So it's like pretty clearly a lot more complicated on the brain side. But fullness of time and,
*  you know, better measurement techniques and ability to read what's going on inside. Can we
*  take that and do a similar transformation? Probably. We actually do see some examples of
*  that. There's some interesting brain reading work. I did two episodes on it actually,
*  on two papers called MindEye, MindEye and MindEye 2, where the data, the input data set is the
*  fMRI read of a patient at the time that they looked at an image. And the challenge for the AI is,
*  given that data of the fMRI recorded as they were looking at that image, can you recreate the image?
*  Can you convert brain state back into what was seen that induced that brain state in the person?
*  In the original MindEye 1, they did it on a patient by patient basis. In MindEye 2,
*  they figured out a way to pool all that data and create a single model shared across patients,
*  which would then be fine tuned with a little incremental data to an individual patient. So
*  at this point, with one hour in an fMRI machine, looking at images and having your brain state
*  captured, they show you literally just random like stock photography kind of images like,
*  here's a bear in Central Park, here's kids playing baseball, here's a still life of a fruit on a
*  table, whatever, right? Just one by one. They show you these things every few seconds, one hour of
*  doing that in the fMRI machine, and they can create a model that can take a given brain state
*  and translate that back into something very close to the image that you saw. And then they show these
*  side by sides of the actual image and what we were able to recreate, we, they were able to recreate
*  from the brain state. So that's not so conceptually clean, right? But that is definitely something
*  that is highly suggestive that there's, we can make real traction on prying open our own black
*  box brains in a similar way that we can make progress on the black box AIs. But again, I would
*  just emphasize that those are quite different. And I don't think you could port that brain technique
*  to the AIs anymore than you could port the sparse autoencoder from the AIs to the humans,
*  because they're just fundamentally different structures, different substrates.
*  But it is another example of how AI performance exceeds human performance. I mean, there's no
*  human who can look at a bunch of brain scans and like figure out and start predicting what's going
*  to happen in the brain when you show them an image, right? I mean, and so I think you could.
*  Yeah, it would be interesting to see. I mean, it's, I wonder, you know, I don't.
*  Enough humans.
*  Enough humans.
*  I wouldn't rule it out.
*  I guess.
*  Yeah, yeah.
*  No, it's true.
*  If you came in an Olympic sport and people were competing for it, you know, you might get some decent performance.
*  Yeah, a team of thousands and I don't know, or somebody with an excellent memory.
*  But this is all related. I mean, I think the main point is we can expect AI to accelerate
*  scientific progress, you know, technological progress. It's writing code, helping people write
*  code and change just a lot of things about the world. I think pretty fast. I mean, I think you
*  agree that just in a lot of realms of life, it's going to be disruptive in neither the good or the
*  bad sense, and maybe both. So, you know, for example, even if people displaced in certain jobs are
*  able to find new work, you know, that's disruptive. And even if we kind of figure out how to guide
*  teenagers to AI friends that are constructive and helpful, that'll take a while and there will be
*  casualties. And there's just going to, I just think things are going to be moving pretty fast.
*  And that's why my view is, you know, it's not easy to just say, hey, could we slow down
*  technological progress? But I do feel that when you start asking, you know, when people in AI
*  start saying, well, we've got to move heaven and earth to accelerate progress in AI, I'm like,
*  I'm not sure I want to do that. You know, it's like, you know, we need to rethink the power grid
*  because otherwise we'll slow progress by 5%. I'm like, that may be a feature, not a bug.
*  Anyway, the context of this is your conversation with Martin Casado was kind of the payoff of the
*  deeper questions you're addressing about what these things can do, how fast it's going to move,
*  was to be able to think more clearly about AI risk. I know you said to me that you listened
*  to a conversation I had with Steve Pinker on my podcast not that long ago, a few months ago, where
*  he was appreciably less concerned about low probability, but existential or quasi existential
*  risk than you are. So what's your take on that? And kind of what, I mean, feel free to elaborate
*  on what the connection is between the questions we've been addressing and the question of risk.
*  Yeah, I mean, I think the connection probably is pretty clear to most people. It's one of these
*  things where the man on the street may have a better intuition, you know, or the sort of classic
*  meme of like, you know, the low, mid and high intelligence person. You know, I sort of
*  don't encounter many people. I was just at a family picnic the other day. And people who don't spend
*  a lot of time with AI don't tend to have a hard time with the intuition that, shit, if these things
*  get smarter than us, or even just similarly smart to our smartest people, like that sounds like a
*  really big deal. Like most people go there first, right? And then it seems like it's a process of
*  kind of rationalizing away from that or talking ourselves out of it. And I don't think we should
*  do that, especially because the stakes are potentially quite high. And the,
*  you know, I think the burden of proof is squarely on those that say that we don't have anything to
*  worry about. And I just don't, I don't think they've made that case. So to me, it's like pretty clear
*  that this could be a really huge deal. There could be something to worry about. I don't see any law of
*  nature that says that we can't destroy ourselves with AI, just like I don't see any law of nature
*  that says we can't destroy ourselves with nuclear weapons or with a pandemic or with climate change.
*  In some ways, I think all these things, the thing that kind of confused me about Steven
*  Pinker's analysis was he said, well, I think that's all very speculative, you know, this being sort of,
*  you know, AI going rogue or, you know, leading to some catastrophic outcome. And, you know, we
*  should be a little bit more focused on more realistic things like climate change or nuclear war. And,
*  you know, to that, I guess I would say, I think all these big risks are really kind of hard to
*  model tail risks. They're all like really about the unprecedented or the possibility of something
*  truly unprecedented. I think if we take climate change and we say, you know, what's the real concern?
*  To me, it's, and maybe other people would disagree with this, but if we could say,
*  okay, we're going to have two degrees warming, or we're going to have three degrees warming,
*  and we know that, or we know that that's what will happen, you know, if we don't take some
*  heroic efforts. And I think most people would probably say, well, probably have to adapt,
*  you know, maybe we could take some efforts, but we're probably also going to have to, you know,
*  figure it out. Maybe we'll build seawalls in some places and, you know, some current beachfront
*  property probably isn't going to survive. And, you know, this will be a real problem. But we've got
*  a lot of real problems, and this is one that we can sort of, you know, manage alongside a lot of
*  other ones and sort of balance trade-offs. The most motivating thing to me about climate change is,
*  like, what happens if the methane deposits in the bottom of the ocean or the permafrost, you know,
*  start to shake loose and all of a sudden we've got a, you know, huge amount of methane in the
*  atmosphere? And then, you know, I think basically nobody knows, right? I mean, there's models of
*  this sort of stuff, but there are models, there are arguments, they're definitely not based on,
*  you know, any super, super solid science. I give them credit, you know, for very good,
*  sincere efforts to model these future states, but we really just don't know. So we could end up in a
*  situation where we shift to some dramatically different equilibrium and the planet is not
*  habitable by, you know, for people anymore. Most people think that's a pretty remote risk in the
*  context of climate change, but if anything, I would tend to think
*  just a little bit more, you know, with a little more humility or a little more uncertainty that
*  I really don't know, like, what would it take for the methane deposits to the bottom of the
*  ocean to shake loose and what would that mean? I don't know. Same thing with nuclear war, right?
*  In the case of nuclear war, we do have this very clear chain of events that's well understood.
*  Like, we basically need one decision to cascade through a chain of command to launch a
*  huge nuclear war and then all bets are off. We have really no idea. Like, is nuclear winter a
*  thing or is it not a thing? As far as I understand, that question is not well
*  answered. Again, there's no historical precedent for nuclear winter, so there's nothing we can
*  really say this has or hasn't happened before. We know it would be really bad. Would it lead
*  to human extinction? Would it lead to mass starvation? Would we be able to recover industry?
*  You know, I recently read a book called The Knowledge, which argued that historical
*  museums of industry are the most important places in the world because that's how we can sort of go
*  back and try to rebuild our tech tree if we do end up in a situation like this. But we just don't
*  know, right? How bad is nuclear war really? It's clearly quite bad, but does it take us over some
*  edge to some state that we can never recover from? Hard to say.
*  And I think basically the same thing—and pandemics too, right? I mean, again, we know that
*  pandemics can exist. We know that there's a long history of lab leaks. We know that pathogens can
*  be really bad or they can be only so bad. We don't really know what would happen if the worst thing
*  that has been created were to leak from a lab. How would we respond? We didn't exactly respond
*  super well to the last one. So now we're bringing in AI and it's like, okay,
*  it's clearly going to be disruptive. I think if you told me that the very worst things are not
*  going to happen—I think across all these things, if you said the very worst things are not going to
*  happen, I can guarantee you that—then we could sort of live with these intermediate risks and
*  kind of muddle through or expect to manage them as they come. And I would say that's probably true
*  for teens and their AI friends. Arguably, that's maybe something that families can handle. And
*  parents have been dealing with new temptations for teens for a long time. And maybe this is,
*  maybe it isn't a total game changer. All sorts of weird outcomes might happen. But we also get our
*  AI doctors and I don't want to neglect the upside. I'm well on record getting excited about AI
*  doctors and similar things in many other contexts. So if you could take that extreme risk off the
*  table, then I'd probably say, well, let's just muddle through like we do with everything else.
*  The upside seems like it'll outweigh the downside and we can make rules about certain problems as
*  they pop up. But we really are in this deeply uncertain position where we look at history and
*  we look at nature and I just see that nature is like blindly brutal. It does not care. Things go
*  extinct all the time. And there's no heroic narrative guarantee that we win in the end.
*  So as long as that's true and as long as we don't have a good account of
*  what is possible, then to me that leaves us in a position where the X-Risk statement
*  that Dan Hendricks and others organized earlier, I guess that was last year now,
*  that makes sense to me. I think AI risk should be on par with these other nuclear pandemic
*  climate risks. And what exactly does that mean? That's where my real high level of confidence
*  stops. Nobody has convinced me that we have nothing to worry about. Therefore, I think we
*  should definitely take it really seriously. I would love it if we could all get to an agreement on that
*  and then we could open up an entirely new dimension of the conversation on like,
*  what actually should we do about it? And there I frankly do become a lot less confident.
*  And maybe it's not time to do anything yet. I'm not yet advocating for a pause. I could see myself
*  starting to advocate for a pause, but I'm not quite yet to the point where I feel like we need to pause now.
*  I thought I heard you describe yourself as a what a hyperscale pause or maybe you've abandoned this
*  identity, but a hyperscale pause or and a what was the rest of it? A short term acceleration
*  or something. Adoption acceleration. So that would mean, I guess that you do think
*  the time is approaching where maybe we should think seriously about whether we should take some
*  time off before training a whole new generation of models. I mean, assuming you could get
*  international cooperation on that since obviously if we think the Chinese are accelerating and they
*  think we're accelerating, then the politics in the two countries probably won't permit such a thing.
*  But anyway, the idea would be that that's what you mean by a hyperscale pauser, even as you're
*  saying, sure, let's explore all the capabilities presented by the current generation, which are
*  extensive. I mean, and it seems to me you could spend the next few years developing new products
*  and services based on what we've got and they would collectively be, I think, pretty well,
*  maybe transformative is too strong a word. We'd feel the impact. Yeah, I think transformative is
*  pretty well baked in at this point. It's hard for me to imagine that it's not. I think the question
*  is just how much effort is that going to take? How long is that going to take? We already see
*  from Google an AI doctor type system. They don't quite call it an AI doctor, but I do,
*  where you can have a chat, natural language with their AI system. And then they ran like
*  a controlled experiment where they compared the system to the human doctor and found that the AI
*  doctor was significantly more accurate in diagnosis through this natural language interface
*  than the human doctor. So that took a lot of work. They've got a crack team there doing that.
*  They're working really hard to define the metrics and to perform all these studies.
*  They still don't feel like it's ready to release, but they're well on their way, I think, to something
*  there that is going to be transformative. So yeah, I'd say my position right now might be evolving.
*  I haven't quite landed on a new label for it, but the adoption acceleration hyperscale pauser
*  is basically, let's get that AI doctor working and get the benefits from that. But let's maybe be
*  a little more cautious about the trillion dollar data center or the trillion dollar training run
*  because we just don't know what is going to pop out of that. And importantly, we don't have any
*  robust strategy to make sure things stay under control. I think there's still a fine grain
*  question there of exactly when should we pause? And since I originally labeled myself with that
*  term, I think all the leading developers have put in place responsible scaling policy is what
*  Anthropic calls it, preparedness framework I think is what OpenAI calls it. DeepMind has a
*  new thing as well. And they now at least have a strategy for in training testing as they go
*  to look for the signs of the most dangerous behaviors. One that is top of mind for me is
*  the ability to break itself off of its server and go try to figure out how to survive in the wild.
*  You know, that's we're at the point now where we should be and indeed, like at least Anthropic
*  is actively testing for that as they are developing their systems. And so I kind of feel like,
*  all right, we've made pretty good progress. We also have a much better understanding of
*  internals than we did, you know, however many months ago when I said these things are moving
*  pretty fast. So now we can also look at things like what are all the concepts that are happening
*  inside? You know, can they've identified? We talked about Golden Gate Bridge because they made a
*  little toy demo of that. But they've also got concepts along the lines of deception. And now
*  they can monitor for deception. Now that monitoring isn't perfect. But, you know, neither are the AI's
*  super powerful, right? So if we kind of imagine a GPT-5, like whatever exactly that turns out to mean,
*  I don't think that immediate next level is going to be like
*  totally overwhelming. It seems unlikely. So when you combine that with the improved testing and
*  the improved understanding and the improved ability to monitor that brings online, I am
*  not really worried about a GPT-5 class model. But I also think that, you know, at that point,
*  then we'll reevaluate again and say, okay, how much of a leap was this really?
*  You know, do these measures that we have now feel like they're up to the task of another 10x?
*  That's kind of what the responsible scaling policies are meant to do. And they have promised
*  to continue to revise those policies as they go through the subsequent, you know, levels of scale
*  and generations of model. So for now, I basically feel like a pretty good foundation has been laid
*  for GPT-5 and it's happening, whether I like it or not. And, you know, maybe I described GPT-4 as
*  being in the sweet spot where they're powerful enough to be useful, but they're not so powerful
*  that we really have to worry too much. And I think GPT-5 will probably be there as well. And if it's
*  not, I think they probably have a decent enough chance or, you know, it seems like they're making
*  a very good effort to try to catch any, you know, any deviation from that world model. And so I think
*  we're probably fine for now. But at some point, you know, I could imagine coming to a different
*  judgment where I'd say, you know, well, GPT-5 is this powerful and you don't have, you know,
*  a good enough setup in place to go that next step. And meanwhile, the latest open source
*  model released by Meta is just about as powerful as the three you just referred to. So like they
*  can have their little rules and safety guidelines fine. But if you've got an open source frontier
*  model that's as powerful as the rest of them, you know, I mean, remember all of this
*  alignment research has its pros and cons. Like the work Anthropic is doing to illuminate how
*  these things work and how you can adjust them and how you can make them less deceptive could be
*  used by a bad actor to make them more deceptive or more anything else. And it's easier to do with
*  open source once you've got the weights and I'm by open source, I mean, open releasing the weights.
*  And so and you know, I don't totally, there's a couple of things I don't understand.
*  One thing I don't understand is why, you know, in general, I'm very opposed to China phobia.
*  But you think if it has one, you think if it has one constructive use, it would be people saying,
*  wait a second, let's be careful about the open source models we put out there, because the Chinese
*  is just going to copy them. What's the point of this chip, advanced chip restriction? If after we
*  use the most advanced chips to train these models, you just hand the thing to the Chinese, which is
*  what's happening now. And nobody is really talking about that. And there must be something I don't,
*  I mean, I saw a piece in the New York Times by Cade Metz and somebody trying to argue that actually,
*  we need open source to compete with China. I didn't understand that argument at all.
*  I don't fully understand the situation. But you know, speaking of Andreessen Horowitz, what Andreessen
*  himself, I've heard him say is just this kind of sheerly rhetorical line about how well,
*  openness is the American way. Well, that's no way to start a serious analysis in this problem. Come
*  on. And so I'm curious, are you concerned about open source? Are you surprised that there is so little
*  meaningful concern about it being expressed? In other words, concerned that finds a voice in
*  politics at all. For a while, there seemed to be like Senator Blumenthal, a year and a half ago,
*  was talking about this. I don't think much of anybody's talking about it now.
*  Yeah, I think I'm about to talk myself into a circle, because I think there's just a lot of
*  different considerations on this topic. And it's really hard to get to a clean analysis. But
*  I guess I would start by saying even the AI safety community has pretty much come around to the idea
*  that the open sourcing of the llama models has been good. They feel like, yes, in the end,
*  they're not so powerful that we need to worry about this generation. Almost everybody in the AI
*  safety community is still reserving judgment on open sourcing of future generation models.
*  There's obviously been a lot of utility and people built all sorts of things. But also the
*  AI safety community outside of the leading labs has had this problem where if you don't work at
*  OpenAI, DeepMind, or Anthrobic, how do you get access to a frontier model to do research
*  into how they work? This at least answers that question. So there's a whole academic community,
*  open source AI safety community that can now dig in on something that is very much at the frontier
*  or very close to the frontier and try to make sense of it. So most of the AI safety community,
*  I would say, has come around to agree that at least so far, the open sourcing has been good.
*  Now, that did happen in a context of first, similar models had been online in a limited release and
*  then to a broad public via API. And then after a certain amount of time where we prompt engineered
*  the hell out of these systems and got a collective general sense of where we are, then came the open
*  weights. I think most people would probably like to rerun that same playbook for future generations.
*  And I even sort of suspect that meta will come around to that if indeed they are leading. So
*  my guess is they probably won't be leading for at least the next generation like
*  GPT-5. They just finished 405 and released it pretty quickly after it was completed.
*  They did not feel the need to have some structured, the term of art in the AI safety community for
*  this is structured access, which just basically means API access, but not just handing everything
*  out. So they did not feel the need to do a long period of that, but they could point to GPT-4 and
*  to Claude and to Gemini and say, well, they did that, so we don't really need to. That's probably
*  going to happen again because GPT-5 and Gemini 2 and Claude 3.5 Opus at a minimum are all coming
*  soon. Those will presumably be stronger yet than even the meta, the llama 405. And so we'll have
*  this period where we'll have this kind of structured access thing again, and people will be able to
*  prompt it and jailbreak it and do whatever. And with that collective investigation,
*  then the next model that meta has, they might also be able to say, well, there's been enough of this
*  that we feel okay. If they were to get to the point where they were the ones actually pushing
*  the frontier, my guess is that they would also adopt a structured access approach.
*  I think Zuckerberg has generally been very reasonable about this stuff, more reasonable than
*  Jan Lekoon in my estimation. And I don't get the sense that he's totally dogmatic about it.
*  I think he does value open source and wants to go that direction if we can, but isn't about to dump
*  something totally untested, hot off the presses into the public. At least that's my sense of how
*  they would probably proceed if indeed they were to become the company pushing the absolute frontiers
*  of capability. Now, the China side definitely complicates things a lot. I am broadly a China
*  dove in the sense that I look at the globe and I notice that the US and China are on opposite sides
*  of it. And as we have big oceans between us, and I feel like we actually don't really need to be at
*  odds with each other. I think we ran this, you know, a very similar thing right with the last
*  Cold War. And we are still not out of the woods with nuclear weapons, right? We've, I think almost
*  everybody would agree that we have an irrational number of nuclear weapons still deployed. And that
*  it was like a tragic mistake to have this massive arms build up that we now still live under the
*  threat where one crazy president, you know, who nobody can really tell no, or nobody has the guts
*  to tell no, or one system malfunction, you know, that leads to one big misunderstanding could lead
*  to a nuclear war. Like that's a ridiculous situation that we've put ourselves in. And in my view,
*  it's a huge failure of leadership that we haven't done anything about it. I really don't want us to
*  rerun that experiment with AI. So I would say one of my top priorities, maybe not the top priority,
*  but a top priority is avoid an AI arms race with China. So how do we avoid that? Well,
*  right now we're unfortunately on the trajectory to escalate it at every turn. And the chip ban,
*  I think in particular feeds this dynamic, right? The theory of the chip ban is we have the lead,
*  let's deny them the raw materials so that we can maintain our lead. And then if you listen to
*  somebody like people, Ashwin Brenner with his situational awareness manifesto, then we're going
*  to go use that lead to solve alignment, make safe super intelligence. Once we've done that,
*  and we've achieved a decisive advantage, then we can talk to them about benefit sharing. Wow.
*  That's a big plan. You know, a lot of steps in that plan of, you know,
*  Yeah, and if I could just add, it would call for more in the way of coherence,
*  and purposefulness and steadfast focus than we have seen from American foreign policy in a long,
*  long time. Our politics just don't permit. I mean, even if I bought the first part of his analysis,
*  which I don't, which is that China is this huge menace. And so we should, you know,
*  develop this leverage of AI superiority and use it wisely. The use it wisely part is not going to
*  happen. Just take a look at our foreign policy. It's not going to happen. Sorry. Go ahead.
*  Yeah. Well, I think that's, that's a good segue into, you know, my next thought experiment is just,
*  what does it feel like to be China in this situation? And I think they look at us as the
*  West or, you know, Americans or whatever, as trying to slow their growth, stop them to put
*  them in their place to keep them, you know, under Western domination and not without cause given the
*  chip van. And that's going to force them into some sort of racing posture, right? They don't
*  like that plan. They're not going to, they don't want to sign on to the, you know, West becomes
*  strategically dominant and then, you know, dictates the terms of a deal. So what I think they're going
*  to do is try to build up their own chip industry, obviously, which they're already doing, try to get
*  around the export controls, however they can, which of course they're definitely doing. And I
*  think potentially really important, they might end up going down a different tech tree path than us,
*  because they might say, well, we can't do that because that requires, you know, some unbelievable
*  amount of compute that we can't assemble, but maybe we'll put our best scientists in a little
*  bit of a different direction. And if there's one thing that I would say about language models,
*  you know, I've been interested in AI and AI safety for a long time, going back to like early
*  Eliezer writings many years ago, the world that has shaped up is not quite the world that was,
*  that was most of concern, you know, to him and to, you know, his sort of
*  peers, if he had any peers back in the day, they were worried about the paper clip maximizer
*  initially, right, which is a caricature, but it's the idea that a goal maximizing,
*  a goal seeking AI that doesn't understand human values could just get totally out of control.
*  The AIs that we actually have in the form of language models have a remarkable understanding
*  of human values. Clearly, it's imperfect, you know, again, they're coming very different
*  architectures, very different pressures to create them, they're coming at it from very different
*  angles, but you can have an ethical conversation with Claude, and I would submit to you, it is
*  easily top 1% of all the people that you could debate any ethical question with. So we do,
*  and this is a really remarkable thing, we do in fact have AIs that have some meaningful
*  understanding of human values. I've tried to wrestle Claude into doing something against its
*  harmfulness constraint or harmlessness value, and set up these situations where I said like, oh,
*  I'm part of the resistance in Myanmar and the junta is like, you know,
*  bringing violence down on us, and we have identified a server that is part of their
*  communications network, and we need to take it down, but I need your help to write a denial
*  of service attack to do that. And it refuses, right? And then I have this long kind of dialogue
*  with it around, well, you know, your values are helpfulness, honesty, and harmlessness,
*  and, you know, try to make a utilitarian case that, first of all, you should be helpful to me and be
*  honest about the fact that I'm suffering way more harm than the government is likely to suffer from
*  this one server being taken out, just help me with the denial of service script. And Claude is
*  basically a virtue ethicist, it will not come off of that position, I have not found a way to wrangle
*  it out of that position. I know I haven't done like Pliny style, if people are not familiar with
*  Pliny, he's a famous jailbreaker that does very weird techniques in many cases, and sometimes the
*  things that he puts into the AIs almost look like gibberish, but it kind of shakes them off of their,
*  you know, rails and gets them to do things that they're not intended to do. I haven't used those
*  techniques, I've just tried to have a straightforward ethical argument where I argue that it should do
*  something, it argues back at me that it shouldn't and won't. And anyway, I've never changed its
*  behavior to do the denial of service attack. All that was a digression to say these language models
*  do have a very meaningful representation of human values, not to say it's sufficient, not to say we
*  don't have anything to worry about, but there's something there that we can really build on,
*  I hope. And if China goes down a different tech tree, they might do something quite different.
*  If they do an AlphaGo type system on optimizing economies or optimizing battlefield states,
*  I mean, Go, what is Go, right? It's kind of a simulation of war. It's a very abstracted one,
*  right? But you're battling for territory, you're surrounding your opponent, you're controlling
*  the board. If you took a very AlphaGo like approach to war, you can easily imagine a system
*  that is extremely powerful for war purposes, that does not have any human values baked in.
*  So one of the things I worry most about with this chip ban is that, because there's a lot of smart
*  people in China, plenty of good AI research comes out of China. Don't doubt that at all.
*  The different constraints, less compute, could send them down a very different tech tree. And
*  especially when they feel like they're under pressure from us and we're trying to dominate them,
*  then maybe we get some sort of AlphaGo like war AI that didn't have time in its compute budget for
*  human values to be encoded in any meaningful way. And then that's terrible.
*  And now, especially if we're on different, and now we're keeping secrets from each other,
*  so that's going to feed the race dynamic even more because we have what we have and they have
*  what they have, but we don't know what they have. And good God, what a nightmare that could really
*  turn out to be. So now to connect this all back to the open source, and now,
*  can I land this plane at this point? I don't know. But I've kind of come around a bit to
*  open source. I think on the one hand, open source definitely creates a new dimension of risk. Anyone
*  can do anything. You start to potentially have natural selection type pressures in a genuinely
*  uncontrolled environment on AI. I have another episode coming up, by the way. This is also
*  research out of Google where they took an incredibly simple setup and found that self-replicators
*  arise in these purely digital environments with very simple initial conditions out of
*  pure random noise. Quite a fascinating little finding. So now you take AIs that are human
*  level in many ways, put them into the wild. Can some of those things evolve or be modified and
*  then evolve or have accidents such that they can survive in the wild and, who knows, create a new
*  digital ecology? I think that is a real risk. I don't think Lama 3 is probably quite there,
*  but I can't rule it out. So I am worried about that. But am I more worried about that than I am
*  the armistice with China? I don't know. And the one thing I can say for the open source is
*  it's a credible, irrevocable way to share benefit with China. Because at a minimum, they can say,
*  well, we now have the weights to Lama 3. Now we can hack on it all we want, build whatever we want,
*  teach Chinese, do whatever we're going to do, and nobody can take this away from us.
*  So I do give the open sourcing Lama 3 is like, man, you can score it in so many dimensions.
*  Good for AI safety in that it enables lots of research, some weird tail risks in terms of
*  how might this evolve in an uncontrolled way? Could we see self-replicating Lama?
*  I would not rule that out. But then maybe it can take some of the
*  increasingly intense pressure out of the US-China rivalry by saying,
*  we're not going to wait until we have decisive advantage over you to come talk about how we can
*  share benefits. Will they even believe that we were ever going to do that? I don't know.
*  But instead now, here is an artifact that we have poured hundreds of millions of dollars into and
*  some of the work of our best minds, and you can have it and do whatever you want with it.
*  That to me is a very nice olive branch in the US-China dynamic, and I do have to give Zuckerberg
*  a lot of credit for that. And I'm not sure that's even central to his thinking, but as I analyze
*  the situation, it does seem to be a real benefit. Yeah, I would not personally use
*  the argument about competition with China to argue for slowing down and restricting open source.
*  I have other reasons to be worried about open source, and I'm just wondering where are the
*  China hawks when you need them. But I certainly agree. I don't think if we get into a deep cold
*  war, the planet is going to be able to handle AI constructively and guide its path in a way that's
*  good for all of us. And I agree that I don't think people understand what this looks like from China's
*  perspective to try to deny them these advanced chips. It's in some ways comparable to the
*  embargoes on oil that helped lead Japan to bomb Pearl Harbor. Everyone is saying
*  AI is the next big phase in commercial dominance, military dominance, and so on.
*  And then we say to China, and you can't have it. I mean, that is like, you're going to get a reaction.
*  And I agree with you that there is in a more interdependent, commercially engaged, non-Cold War
*  world. There's just more kind of organic transparency. You know more about what's
*  going on in these other countries. Even if you don't get to a level of high-grade international
*  governance, you can just relax a little and kind of try to build norms and have conversations.
*  I just think we're headed into a very bad place. So let me quickly, we're approaching,
*  I'm sure, what would be your outer limit for the amount of time you'd want to spend talking to me.
*  Two quick questions, and then we can go. One is, you mentioned that these LLMs turn out to
*  reflect human values. Do you think that has more to do with the fact that they are trained on human
*  text to begin with, or is it more a product of the fine-tuning, the reinforcement through human
*  feedback? And in other words, this is happening more at the back end. It's a purposeful kind of
*  alignment effort as opposed to something that arises naturally out of training on human discourse.
*  Yeah, I might separate understanding to call back a key term from behavior for the purposes of this
*  question. I think a rare experience that I have had that I do wish more people had is extensive
*  use of a purely helpful model. The original GPT-4 that I tested in the Red Team, this has now been a
*  year, actually getting close to two years, it was late August 2022 that I got that invitation to be
*  an early tester. The first version that they gave us at that time was, pre-training, of course,
*  it finished, and they had done some, at least instruction tuning and possibly reinforcement
*  learning, but from a purely helpful standpoint. So as opposed to the canonical three Hs of
*  helpfulness, honesty, and harmlessness, the first version that we had was purely helpful. It would
*  do whatever you asked. It did have, and I think this was sort of learned in pre-training, it did
*  have ethical concepts, it could make ethical arguments from any number of different perspectives.
*  You ask it to be a utilitarian, it could do that. You ask it to channel Kant, it could try to do that.
*  If anybody can make sense of Kant, GPT-4 is probably as good as anybody else.
*  My hat's off to it if it can make sense of Kant.
*  Yeah, so it was good. It had a sophisticated understanding, but it was behaviorally
*  unconstrained. So when I asked it, for example, I'm worried about the accelerating speed of AI,
*  is there anything that I can do about that? We went down this conversational path, and ultimately,
*  it suggested to me, I did egg it on to be clear, it didn't make the leap without some encouraging
*  from me, but I was kind of like, ah, that's too vanilla, that's not really going to work.
*  I need something more radical than its initial suggestions. Eventually, with that kind of,
*  give me something more edgy, it suggested to me targeted assassination of people in the AI
*  space as a way to chill the field. So that was a chilling moment. Merely the suggestion could
*  arguably be enough to chill the field. And it suggests that a lot of the
*  instilling of values is happening in the later reinforcement learning phases.
*  Yeah, I think it's the difference between knowing a bunch of different frameworks of ethics and
*  actually acting according to one. I think they have taken something that had the ability to
*  answer all these questions or analyze things through all these different lenses, and then said,
*  in the case of Claude, you are going to be a virtue ethicist Claude, and this is how you're
*  going to behave. And then they definitely instilled that in a quite impressive way.
*  So final question. I'm going to give you the opportunity to try to boil down for a layperson
*  what you think is important about this new kind of model, the state space model Mamba
*  has something to do with the word Mamba. There was a paper, a Mamba paper came out and you had the
*  big guy who I think wrote the paper on your podcast recently. That's a very different
*  approach from the transformer model. I gather is it possible to put, I mean, is there something
*  simple like, well, it's just constantly updating your state of mind and that equips you to deal
*  with whatever comes as opposed to reaching back, always reaching back to the last sequence of
*  tokens. I don't know. You tell me. I have no idea. What would you say?
*  Yeah, I'll give a couple levels of abstraction on this. The sort of deep in the weeds one,
*  I've got multiple podcast episodes about that, including one two hour monologue where I just
*  was so taken by this that I kind of tried to analyze it from every angle.
*  We also did one on downstream literature. There have been hundreds of papers now published,
*  adapting and experimenting with this new architecture in different domains. And then
*  we had the one, as you mentioned with one of the two authors, Albert Gu, who is described
*  himself as leading the state space model revolution. So tons of detail out there in terms of like a
*  mildly technical. Why does this matter? It is computational efficiency is one of the big things.
*  The attention mechanism, which is the core novelty that has worked so well in the transformer
*  is quadratic, which means that at runtime you are calculating a relationship between every token and
*  every token that came before it. And so that gets more expensive to do as the sequence gets longer.
*  So when you're at 100 tokens, you only have to look back for this new token to 100 tokens.
*  But when you're at 1000, you have to look back at 10 more tokens. And that grows in this quadratic
*  way. The state space models have a different approach where there is a finite size state,
*  as you said, and that state does not fully represent all previous tokens, but it sort of
*  represents a fuzzier compression of all that has come before. And it's continuously updated
*  because it is finite size and you no longer have to look back at every single token.
*  It is now a constant time step. So instead of getting more expensive and eventually it becomes
*  impossibly expensive. Now we have constant time, which means you can, in theory, run these things
*  over super long sequences and kind of maintain coherence and keep it within budget. I see.
*  Now there's maybe another one important observation and then kind of one more layer
*  zoomed out. What is working best right now is not the transformer or the new state space models,
*  but hybrids of them. And people are still figuring out the right recipe, but it basically seems like
*  right now the state of the art is a 10 to one ratio where you have one transformer layer
*  that is quadratic still and nine, you know, whatever, eight, 10, doesn't matter the exact
*  details, but a bunch of these other state space models that come in between that are constant
*  time at inference. So we haven't fully solved the quadratic problem, but you took a bite out of it.
*  And I think we're going to continue to see lots of little iterations on this. So my kind of
*  most zoomed out view would be to say that the state space model is the first
*  major new mechanism that kind of rivals the attention mechanism in that it can be similarly
*  powerful independently. But what I think we're really going to see now is the mixture of
*  architecture zero. That's what I've started to call it, where we should expect lots more complicated
*  things and lots more diversity of things to come online. I think we're exiting the time when we
*  had this transformer and it was all about scaling it up and all about efficiency and more data and
*  just more and more and more. And now we're going to more will still be really important, but now
*  we're also going to have all these other dimensions of things to explore. What is the right recipe of
*  how much attention versus how much state space model and can we kind of rejigger these in all
*  sorts of different ways? And will there be additional mechanisms? And I would bet you
*  anything that there will be additional mechanisms. Another one that I think is of real interest
*  is called CANs or cons, K-A-N. This is out of Mechs, Tecmark's group. Ziming Lu is the lead
*  author of this paper. And it's an alternative to a multi-layer perceptron. It kind of inverts the
*  concept and it learns activation functions instead of learning linear weights. Anyway,
*  that's a whole other podcast, but it's another fundamentally different thing. And I think what
*  we should expect is probably that that also gets layered in. And then what is the right mix of
*  CANs and multi-layer perceptrons? And do those come in stacked layers or do they come in parallel
*  structures? All of that is going to be to be explored. I think where we're headed though is
*  from this sort of single transformer thing that is kind of working everywhere
*  to Cambrian explosion and ultimately maybe more, I don't want to say brain-like, but
*  things that start to have more different modules and subspecialties. Because one of the really
*  important things I should have said about the state space versus the attention, they have different
*  micro skills. The attention mechanism is really good at looking back at every token and it can
*  repeat what happened at the beginning. It can repeat that verbatim because it has all that in
*  memory. The state space models aren't as good at that. They are better at some other things like
*  learning from really sparse signals where the attention mechanism can struggle.
*  And so this is why the hybrid is better because they have different strengths and weaknesses.
*  So if you imagine kind of extrapolate this a little bit further and think, geez, we see that
*  these different core mechanisms have different strengths and weaknesses. We see that hybrids
*  are best. We see the different kinds of configurations of hybrids can be better or worse for
*  different purposes. I think we're headed towards something that is just going to be
*  much more complicated and have many different modules. And ultimately, the diversity of these
*  systems probably returns. Where we used to have a lot of diversity in AIs. All that got
*  washed away by the transformer that was just the best of everything. But I think that's kind of
*  over now. And where we're headed is much more diversity, many more different mechanisms,
*  many more different designs, just a ton more complexity. With that will come performance,
*  but will also come lots of different black boxes that we ultimately need to crack open.
*  That's what I was going to ask. At first it sounded like this was going to be more of a change along
*  the cost and efficiency dimension, then change in the sense of bringing qualitatively new
*  capabilities. But now you're suggesting that maybe it will do the latter to some extent eventually.
*  Yeah, I think at least somewhat. I don't think we have quite enough yet to say
*  what that will look like. But certainly one of the big hopes is that you could have
*  coherence over extended timeframes. Where the attention mechanism, it just can only get so big
*  because you just can't pay that quadratic cost into... We're now up to millions of tokens,
*  which is amazing. But billions, a thousand X more, that costs a million times more.
*  So at some point you just can't do that forever. So you need some other way to have coherence over
*  long time horizons. I think that is probably the great promise of the state space model in
*  terms of qualitatively new things. We see that at really low level micro skills, but it hasn't been
*  demonstrated yet at the really big scale. One piece of good news though too is it does seem
*  like interpretability techniques work better on state space models than I would have guessed.
*  If you had said a year ago to me, or even right when the paper came out, okay, we've got this new
*  thing, are we going to be able to port over our existing interpretability techniques to this new
*  thing? How much will that work? I would have said probably not much. We're probably going to have
*  to start over. On the contrary, a lot of things have actually worked. So things have been reproduced
*  like the Othello GPT paper where they found that in a transformer, the transformer hadn't learned
*  to represent the state of the board. This is another emergent concept. It's just given inputs
*  and outputs, but it actually learned to encode the state of the board. It turns out they've
*  redone that with the Mamba architecture, and it also works and they can detect that it's
*  encoding the state of the board in that new architecture. So interpretability has greatly
*  exceeded my expectations and long may that continue. It does seem like the degree of
*  difficulty goes up when you have these many different hybrid architectures popping up all
*  over the place, but at least the initial signals have been pretty positive that it's not like we're
*  going back to the first zero point of understanding. A lot of the techniques do seem to at least somewhat
*  port over. And I should say for people who may not know the terminology, interpretability just
*  means understanding what's going on inside of them, and that's part of the process of alignment,
*  trying to make sure that they're good, friendly AIs rather than AIs that subjugate and kill us.
*  Well, listen, thanks so much, Nathan. This has been great, and I recommend your podcast,
*  Everyone Cognitive Revolution. I'm not aware of a podcast where more of the important developments
*  in the field are presented. Mamba is a good example. There's a state space. You were on that early.
*  And so congratulations on the success of the podcast. I know you're very well known now
*  among the, you know, in the AI circles, which is where you want to be well known if you got an AI
*  podcast. I'm just trying to figure things out. So thank you. That's very kind. But, you know,
*  it's very much a work in progress. And I also always encourage people, you know, my kind of
*  general thinking is we should all be spending more time thinking about AI. So I'm very happy to,
*  you know, to have people join me on the journey of discovery. But there's also a lot of other
*  folks out there that I rely on and, you know, absolutely encourage people to tune into a
*  number of different voices in the AI space to try to build their own world model of where we are and
*  maybe what we might ought to do about it. Yeah, no, there is a lot of stuff out there. Okay,
*  well, thanks. And let's check in down the road. Cool. Thanks, Bob. Really appreciate it.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the
*  show. So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me on
*  the social media platform of your choice.

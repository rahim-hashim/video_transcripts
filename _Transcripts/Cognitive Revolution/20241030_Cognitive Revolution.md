---
Date Generated: October 30, 2024
Transcription Model: whisper medium 20231117
Length: 8658s
Video Keywords: []
Video Views: 84
Video Rating: None
Video Description: In this episode of The Cognitive Revolution, Nathan dives deep into the world of state space models with returning co-host Jason Meaux and special guest Quentin Anthony, Head of Model Training at Zyphra. Explore the cutting-edge Zamba 2-7b model, which combines selective state space and attention mechanisms. Uncover practical insights on model training, architectural choices, and the challenges of scaling AI. From learning schedules to hybrid architectures, loss metrics to context length extension, this technical discussion covers it all. Don't miss this in-depth conversation on the future of personalized, on-device AI.

Check out more about Zyphra and Jason Meaux here:
Zyphra's website: https://www.zyphra.com
Zamba2-7B Blog: https://www.zyphra.com/post/zamba2-7b
Zamba2 GitHub: https://github.com/Zyphra/Zamba2
Tree attention: https://www.zyphra.com/post/tree-attention-topology-aware-decoding-for-long-context-attention-on-gpu-clusters
Jason's Meaux Twitter: https://x.com/KamaraiCode
Jason's Meaux website: https://www.statespace.info

Be notified early when Turpentine's drops new publication: https://www.turpentine.co/exclusiveaccess

SPONSORS:
Weights & Biases RAG++: Advanced training for building production-ready RAG applications. Learn from experts to overcome LLM challenges, evaluate systematically, and integrate advanced features. Includes free Cohere credits. Visit https://wandb.me/cr to start the RAG++ course today.

Shopify: Shopify is the world's leading e-commerce platform, offering a market-leading checkout system and exclusive AI apps like Quikly. Nobody does selling better than Shopify. Get a $1 per month trial at https://shopify.com/cognitive

Notion: Notion offers powerful workflow and automation templates, perfect for streamlining processes and laying the groundwork for AI-driven automation. With Notion AI, you can search across thousands of documents from various platforms, generating highly relevant analysis and content tailored just for you - try it for free at https://notion.com/cognitiverevolution

LMNT: LMNT is a zero-sugar electrolyte drink mix that's redefining hydration and performance. Ideal for those who fast or anyone looking to optimize their electrolyte intake. Support the show and get a free sample pack with any purchase at https://drinklmnt.com/tcr

CHAPTERS:
(00:00:00) Teaser
(00:00:42) About the Show
(00:01:05) About the Episode
(00:03:09) Introducing Zyphra
(00:07:28) Personalization in AI
(00:12:48) State Space Models & Efficiency (Part 1)
(00:18:59) Sponsors: Weights & Biases RAG++ | Shopify
(00:21:26) State Space Models & Efficiency (Part 2)
(00:22:23) Dense Attention to Shared Attention
(00:29:41) Zyphra's Early Bet on Mamba (Part 1)
(00:32:45) Sponsors: Notion | LMNT
(00:36:00) Zyphra's Early Bet on Mamba (Part 2)
(00:37:22) Loss vs. Model Quality
(00:44:53) Emergence & Grokking
(00:50:06) Loss Landscapes & Convergence
(00:56:55) Sophia, Distillation & Secrets
(01:09:00) Competing with Big Tech
(01:23:50) The Future of Model Training
(01:30:02) Deep Dive into Zamba 1
(01:34:24) Zamba 2 and Mamba 2
(01:38:56) Context Extension & Memory
(01:44:04) Sequence Parallelism
(01:45:44) Zamba 2 Architecture
(01:53:57) Mamba Attention Hybrids
(02:00:00) Lock-in Effects
(02:05:32) Mamba Hybrids in Robotics
(02:07:07) Ease of Use & Compatibility
(02:12:10) Tree Attention vs. Ring Attention
(02:22:02) Zyphra's Vision & Goals
(02:23:57) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Training Zamba A Hybrid Model Master Class with Zyphra's Quentin Anthony
**Cognitive Revolution:** [October 30, 2024](https://www.youtube.com/watch?v=xFU7mfBfVSw)
*  The future of AGI will involve a combination of cloud and on-device deployment.
*  These large model companies like Endoptochrope and AI just can't really specialize to every single
*  person on the planet. We think that you need to have your own set of weights and changing
*  a system prompt per person is not enough, right? We want to actually bake into the weights. You
*  can make the model simulate learning faster than it really is by doing activation steering. If the
*  user tells the model you're being too dry, then you can very quickly steer the activation to be
*  a bit more fun. Until tonight, when you can bake into the model, I think it's got to be
*  continual learning and it's got to be per user. And the only way to do that is with weights on the phone.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of how
*  AI technology will transform work, life, and society in the coming years. I'm Nathan Labenz,
*  joined by my co-host, Eric Torenberg. Hello and welcome back to the Cognitive Revolution.
*  Today we're once again going down the state space model rabbit hole with returning co-host Jason Moe,
*  who regular listeners will remember from our Mamba Palooza literature review and Albert
*  Goo interview episodes, and Quentin Anthony, head of model training at Zyfra, a large language
*  model startup that's just released their Zompa 2 7B model, which is built on a hybrid architecture
*  that uses both the selective state space mechanism and the traditional attention mechanism, albeit
*  with some notable tweaks relative to the standard implementation. In addition to sharing Zyfra's
*  high level vision for highly personalized on-device AI, Quentin was super generous with both his time
*  and knowledge, sharing a wealth of practical lessons learned from the front lines of model
*  training. Over the next two hours, we will cover the delicate architectural choices that balance
*  efficiency and capability, the many practical challenges of training at scale, including
*  choosing the right learning schedules for different phases of training, the nitty-gritty details of
*  training hybrid architectures, including why Zompa models don't need positional embeddings,
*  the Zompa model's use of shared attention blocks and internal LoRa adapters to maximize performance
*  on the edge, the not-so-simple relationship between loss metrics and model quality and
*  capabilities, as well as the challenges of context-linked extension, the Zyfra team's
*  experiments with different optimizers and why they're sticking with Atom for now, Quentin's
*  intuitions about the relationship between model scale and loss landscapes, and finally even their
*  recent published work on tree attention, which offers important advantages over ring attention
*  for multi-node training. I have to say, I got a lot from this episode, and while it's technical
*  enough that I wouldn't necessarily call it entertainment, I am confident that you will, too.
*  If so, we always appreciate it when folks take a moment to share the show with friends or write
*  an online review on Apple Podcasts or Spotify, and we welcome your feedback via our website,
*  cognitiverevolution.ai, or by DMing me on your favorite social network.
*  Now, I hope you enjoy this highly technical conversation with co-host Jason Moe and guest
*  Quentin Anthony, model training lead at Zyfra. Jason Moe, returning guest and co-host and
*  chronicler of state space models at statespace.info, and Quentin Anthony, model training lead at Zyfra,
*  which has just released the new Zamba 7B SSM hybrid model. Welcome both of you to the Cognitive
*  Revolution. Thanks for the time. Great to be here. Jason, regular listeners will know as a
*  partner in crime who's also obsessed with state space models and the potential that they have to
*  unlock new capabilities in terms of potentially long-term memory, extreme efficiency, all these
*  kinds of interesting things. And we've been down the rabbit hole together on that a couple of times.
*  So I was excited to have him back to help me with this conversation about the new Zamba model and
*  all the ins and outs of that. So Jason, I'm going to ask you to lead the questioning today and I'll
*  be in the supporting role, but listening intently and probably jumping in with a few of my own
*  follow-up questions along the way as well. How's that sound? Sounds good. Let's do it. So let's
*  start with maybe a broad question first. So on the Zyfra website, it says that, quote,
*  the future of AGI will involve a combination of cloud and on-device deployment with an increasing
*  shift towards local inference. So why is local inference going to be important and how does
*  this idea overall influence the direction of the company? Yeah, there's a few aspects, a few angles
*  of this. The main one is personalizability. We think that doing system prom tacking things like
*  these large model companies doing like endorphin, open AI, just can't really specialize to every
*  single person on the planet. We think that you need to have your own set of weights and changing
*  a system prompt per person is not enough. We want to actually bake into the weights. You like to be
*  talked to this way. Your favorite restaurant is X, that sort of thing. A second thing here is privacy.
*  So there's a lot of data about your laptops, your phones that you don't really want to be communicating
*  to the cloud. There's a lot of enterprises out there who don't want to share all of their data
*  with open AI, all of their proprietary code things. So keeping that all on-device, on-prem,
*  in the organization is where we want to keep it. And then there's just some very practical
*  challenges here of open AI spends. What was their capex realistically, right? In order to infer all
*  these models, that's not really something that can keep up forever. It's being fueled by a lot of
*  VC money. But if everyone's device is able to efficiently run their own models, then we offload
*  that to the users. And then it's also just much faster. You can run it offline. All these small
*  benefits come out from having the model locally in the device. But it's all steered by this global
*  personalizability, privacy, these sort of North Stars. In terms of on the cloud, there are some
*  model capabilities that are more challenging. They're too challenging to have on a 1B or a 2B
*  or something like that. Most people we see actually, when they communicate with models,
*  they just need these higher level, more simplistic tasks, just like basic chat,
*  factual recall. They're not asking these O1 type math questions, these Olympiad questions or
*  anything to their day-to-day on-device model. But sometimes you will need it. And that's why we have
*  also a cloud offering in the 7B range. The 7B range is a turning point where you can fit it on more
*  powerful laptops, powerful on-prem. But it's able to think through these more difficult problems more
*  clearly. And we want those on-device models to be able to know when they need to go back and ask
*  like an Oracle model, something a bit more powerful. And then this is all seamless to the user. And
*  then you can pick and choose how often your model wants to talk to the cloud.
*  S2 It sounds like it's when I hear local inference, it's often a privacy bullet point is the main
*  bullet point that gets hit. But it sounds like the overall idea is it's some mix of capability
*  and privacy that if we had super efficient, super personalized, localized models that this
*  is going to increase capability of the full stack. Is that correct?
*  S2 Definitely. You can't forget personalizability. It's really hard to bake in personalized outputs,
*  personalized how the model likes to talk to you in the same way. It's just a hard problem.
*  S1 I would love to dig into that a little bit further. Because I'm working on a project right
*  now to try to get a model to write as me. This has been a white whale project for me for a while.
*  I figure if a model can write as me in a way that's compelling to me on a consistent basis,
*  it seems like that's a pretty big threshold. So I've been trying to see, can I make that happen?
*  And the best readily available, fine tunable model today is GPT-4O. And so I've been working
*  mostly with the OpenAI stack. They make it easy to do fine tuning. They don't tell you too much
*  about exactly how it works. One presumes that it's a Laura type process that they're running. I think
*  there's a lot of reasons to believe something like that. It doesn't seem to learn facts very
*  well. It does seem to learn like patterns and like stylistic layer, if you will, reasonably well.
*  Okay. I wonder what you think is the right way to even approach personalization in the first place?
*  Is it like when you envision doing this personalization for individuals on their
*  machines? Are we talking Laura's? Are we talking like full training of a one or two or three B
*  model? How many tokens does that take? Do we still need to like stuff huge amounts of context in
*  there? Because that's another approach I've been taking where I'm like, maybe if I give it 50,000
*  tokens of everything it needs to know about me as the system prompt, then it won't need to hallucinate.
*  And I still haven't quite figured that out. I'm still getting hallucinations. So what is the
*  overall paradigm or path to this deep personalization for individuals? Yeah. So the exact process will
*  not be entirely clear until we have a bunch of people having Zamba on their phones. But we have
*  a few bets. One is that we have a lot of expertise on continual learning and continual free training.
*  So we envision doing like a weight update like overnight, maybe while your phone is plugged in,
*  your laptop's not really actively being used on consumer hardware. It's really cheap to do this
*  when the model is really small. Updating Laura's, as you mentioned, is another like makes it even
*  cheaper. But just continual learning, I think, is the way to go. In terms of your GPT-4.0 problem,
*  I think I would need to know more details about the fine tuning data set in the model, which I'm
*  never going to get. We find continual learning on a small model per person is really great.
*  There's some sort of, you can make the model simulate learning faster than it really is by
*  doing things like activation steering. I could remember Golden Gate, Bridge Claw and stuff. If
*  the user tells the model you're being too dry or something like that, then you can very quickly
*  steer the activation to be a bit more fun. Until tonight, when you can bake into the model, okay,
*  this person likes generally to be a bit less dry and to talk in a more fun way. I think it's got to
*  be continual learning. It's got to be per user. The only way to do that is with weights on the
*  phone. How much of that exists today? Can I get a Zamba, first of all, which scale of model would
*  you recommend that I bring locally? Can I do this continual learning? Can I start to feed it my
*  emails and my Slack messages? I assume I would have to mix in some general purpose pre-training
*  mix as well. I wouldn't just go all in on my content. Tell me a little bit more about what
*  that looks like practically. I'm taking notes. Yeah, absolutely. Right now, we have the 1.2B,
*  the 2.7B and the 7B that we just dropped, all of our Zamba 2 series of models. The 1.2B is really
*  good if you're really edge constrained. You don't want your phone to use much battery,
*  that you wanted on a phone in the first place. In terms of whether you can do this yourself,
*  right now you can. It's just a little less user friendly than it will be someday. But right now,
*  we have our own hugging face fork for Zamba 2. You would just download the model weights and then
*  you would just have to tokenize and actually just train on whatever personal emails or whatever else
*  you want based into the model. The product vision here for Maya is that you have a Maya cloud across
*  all of your devices. That's just some social aspects here. You can upload pictures. It'll
*  be multimodal. Your conversations and such, you can decide how much you want to share,
*  how much you want Maya to be personalized to you. But training on that cloud of your own data,
*  just as a continual pre-train on whatever edge hardware you have, is the high level.
*  I'll start here. Are you doing this today? How far have you guys taken this internally? Do you have
*  a Quentin model that drafts your emails or what's the frontier in application? So earlier, I said
*  the 1.2B is good for edge constraint. The 2.7B is really good for quality. I'm always surprised by
*  it. We do have some fine tunes for that. So we have some role play models, some summarization
*  models if you want to summarize emails, summarize meetings and such. We have some very early results
*  on audio as well. So generating audio in the style of people you talk to, note taking audio
*  for the meetings you're attending. It's definitely more mature in-house, but we really want this to
*  be really seamless before we give it to everybody else. So I would say that the 2.7B, I've seen
*  really amazing results on in terms of summarization and these tasks that I was mentioning. And it's
*  all from this hugging face, just fine-tuning our DPO on whatever my personal data is.
*  Cool. I'll probably have some more questions about that as we go, but maybe a good transition to,
*  as we think about this on edge paradigm. Jason, you want to take the baton and talk about why
*  state-based models are the, or hybrids at least, are the attractive approach to take there?
*  Yeah, absolutely. I guess when you think of what kind of models can run locally,
*  you get hit by transformers in two places pretty hard. The first place is just memory. Anyone who's
*  done their own work with a limited compute budget knows the classic out of memory error.
*  So you quickly, whether that's too large of a model in terms of parameter count,
*  or if your KV cache is growing and at some point you run out of memory. So transformers,
*  because of the way they work, they're famously pretty memory intensive. The KV cache scales as
*  you scale your sequence. And then of course, secondly, is just computation. Transformer
*  has amazing properties, but it is pretty computationally intensive, especially when
*  compared to other architectures. So when you start looking at Mamba, that's one of the exciting things
*  about it. It has properties that are much more memory efficient and computationally, it's able
*  to be more efficient as it processes through sequences due to its fixed state size. And so
*  you even see that play out in the literature. There's been some early work with Mamba models
*  with a couple of papers on robotics. These are models that would have to run locally.
*  You could not do cloud API calls for split second decisions that would be made in robotics. So you
*  can just imagine finally, maybe we have an architecture that helps inform what the ultimate
*  models running locally could look like for these kinds of applications. So how does that vision
*  look like for Zephyr and the Zamba architecture? What does the ideal local inference strategy look
*  like as it relates to Mamba? Yeah. So we love Mamba for its systems properties. As a guiding
*  principle in terms of model training, we try to train the models that are perfect for inference,
*  because that's where we're going to need them to perform the most. We can eat some training costs,
*  but at the end of the day, it needs to be blazing fast for inference. This translates to a few
*  different things for us. For one, attention for dense transformers, like a five type model,
*  is just not going to happen for us. We don't think that this is efficient on a phone. Earlier,
*  I mentioned we want text and email summarization. Sometimes you want news article summarization.
*  Those inputs are too long for the KV cache. It's just going to grow outside of memory for
*  most phones today. Attention though is really nice. So you get these exact cross-sequence
*  dependencies that we think are just required for some specific tasks. Remember, I say specific. So
*  not every task needs attention, but there are some tasks like in-context learning and long
*  sequence dependencies for which attention is just necessary for you to be performing on.
*  Eventually, if you train on several trillion tokens, then eventually Mamba becomes somewhat
*  performant at this on benchmarks. But I've never played with a pure SSM or pure RNN model that's
*  able to speak well in an in-context learning regime. I think that's a common intuition that
*  people have when they actually sit down and play with the models. So pure SSMs have quality issues
*  from what I've seen, and then pure attention dense transformers have performance issues. So I can't
*  get by on a phone realistically to run the amount of time with the fastest time-to-first token that
*  users actually want. So there's some other architectural changes here. Instead of having
*  independent attention blocks, we have this global shape attention block. And the reason for this is
*  that us and a few other groups have independently found that attention blocks are highly correlated
*  across depth. So they're telling the MLPs and a dense transformer, these are the important tokens,
*  these are still the important tokens, these are still the important tokens. There's some small
*  changes, but most of the specialization across depth is coming from the MLPs. So if you tie all
*  of those weights together, then you're able to allocate more parameters towards the, for example,
*  the Mamba block for us. If you were on a dense transformer, you could apply more to the MLP blocks
*  or something. So now we just have, like for the Zamba 1 series of models, you just have a single
*  attention block and you apply it every six Mamba blocks across depth of the network. We improved
*  on this a bit in Zamba 2 by seeing, okay, a little bit of specialization across depth is helpful. So
*  we added Lora back in and those Loras are independent across depth. So now you have this
*  single global attention block in the 1.2B case and then the 2.7B and 7B case for Zamba 2, you have
*  interleaves. So you have attention block one, attention block two, attention block one,
*  attention block two, all across depth. And then individual Loras across depth as well. So you get
*  a little bit of specialization, but back to the systems angle, you're not really applying very much
*  attention. So your slope of like your KV cache memory, here you'll see this in all of our plots,
*  is something more like 10 or 13 invocations rather than 30, 32 in like a dense transformer,
*  because we're just invoking far fewer attention blocks. Now, the very first criticism people
*  should be thinking is that, okay, you're applying for the same perimeter budget, you're applying
*  parameters over and over, the total number of flops is going to increase. And this is true.
*  We're applying blocks more often than like a typical 7B, but the Mamba blocks, and now the
*  Mamba 2 blocks are so high throughput on parallel hardware in general that this totally makes up for
*  it. And we end up with a net improvement of about 20 to 30% in time for a token and time for output
*  token. So they make up for our sins of sharing these attention blocks. But yeah, both of these
*  translates to significantly lower memory overhead, significantly lower time to first token at the
*  pre-fill stage, so the model responds really fast initially. And then time for output token is also
*  20, 30% beat compared to similar dense transformer models. Hey, we'll continue our interview in a
*  moment after a word from our sponsors. As a developer, the journey from concept to
*  production ready large language model apps is fraught with challenges. Dealing with unpredictable
*  language model outputs, hallucinations, and ballooning API costs can all be blockers to
*  shipping your next AI powered feature. That's where advanced RAG comes in. With the new RAG
*  plus plus course from Weights and Biases, you can overcome these hurdles and build reliable,
*  production ready RAG applications. Go beyond proof of concept and learn how to evaluate
*  systematically. Use hybrid search correctly and give your RAG system access to tool calling.
*  Based on 21 months of running a customer support bot in production,
*  industry experts at Weights and Biases, Cohere, and Weaviate show you how to get to a deployment
*  grade RAG application. This offer includes free credits from Cohere to get you started.
*  Make real progress on your large language model development and visit wnb.me.cr to get started
*  with their RAG plus plus course today. That's wnb.me.cr to get started with their RAG plus plus course today.
*  The Cognitive Revolution is brought to you by Shopify. I've known Shopify as the world's
*  leading e-commerce platform for years, but it was only recently when I started a project with my
*  friends at Quikly that I realized just how dominant Shopify really is. Quikly is an
*  urgency marketing platform that's been running innovative time-limited marketing activations
*  for major brands for years. Now we're working together to build an AI layer which will use
*  generative AI to scale their service to long-tail e-commerce businesses. And since Shopify has the
*  largest market share, the most robust APIs, and the most thriving application ecosystem,
*  we are building exclusively for the Shopify platform. So if you're building an e-commerce
*  business, upgrade to Shopify and you'll enjoy not only their market-leading checkout system,
*  but also an increasingly robust library of cutting-edge AI apps like Quikly,
*  many of which will be exclusive to Shopify on launch. Cognitive Revolution listeners can sign
*  up for a $1 per month trial period at Shopify.com slash Cognitive, where Cognitive is all lowercase.
*  Nobody does selling better than Shopify, so visit Shopify.com slash Cognitive to upgrade your selling
*  today. That's Shopify.com slash Cognitive. The choice for using global shared attention blocks
*  is really interesting to build the hybrid model that way. I guess it's in alignment. I saw on
*  Zephyr site the desire to maximize performance per parameter. That seems like a choice that
*  obviously is doing that as well as maybe some other architectural choices. How important is it
*  in the Zamba family of models to focus on performance per parameter?
*  It's pretty important, right? At the end of the day, most of your memory overhead is coming from
*  just storing the parameters. We can get away with a lot of quantization, but each parameter is really
*  painful when you're deploying it on a phone. So trying to make all of those parameters maximally
*  useful for the attention block, as in tying it all together and making that attention block really
*  well-trained. Maximizing the performance of each one of those parameters, we've got to do. We don't
*  want this really sparse model where most of what we're storing is not doing much. But yeah, very
*  important. I think there's a broader trend here of dense attention being the original thing.
*  And then there's been obviously many attempts to make that more efficient with linear attention
*  or things that are not quadratic. My sense is that those have all been pretty good, but somehow
*  still fall short. Then you have these other techniques of shared query attention. Maybe you
*  can help us understand in a technical sense exactly what that is. And then I'm also aware of shared
*  query key attention. And now you're going all the way up to shared full attention block. So help us
*  map that space and just understand what are the different options and trade-offs. And is this the
*  end of that paradigm or is there even still further that we could go on the spectrum from full dense to
*  full shared? Is there even further on that continuum?
*  So we use grouped query attention for our upcoming attention blocks. I would say I haven't seen a
*  non-quadratic attention that really performs the same and does what we want it to. Frankly,
*  I would say that there is a very interesting emerging area of work where people try to remove
*  the attention from attention models. So that maybe the theory there is just more of a play from, for
*  example, liquid AI sort of player. You take a model that's already been trained with attention,
*  and then you try to linearize that attention, get a final post-training step. And the hope there is
*  that the model is already baked in the ability to do these long sequence dependencies in context
*  learning. And then you can just sort of copy it over to much lower cost blocks. It's a potential
*  play. Can you give it a help us develop an intuition for this is like really a question I
*  want to I'm asking for me and hopefully other people find it useful. I have an intuition for why
*  the full attention would be qualitatively better versus like a state space mechanism or some
*  approximation of attention. For me, that kind of boils down to we compute a relationship between
*  every token and every other token. We don't forget about any tokens. It's all there. And it's all
*  when a new token comes in, we can see how that relates to everything that came before
*  with no compromises. When we have that, we try to map that onto a linear thing. What's the
*  intuition for why that like would work or wouldn't work? Maybe there is no intuition and people are
*  just trying stuff and seeing what works. But I'm grasping for understanding of what that
*  transformation is and why we would what should we expect and what should surprise us.
*  Okay, my first order intuition here is that attention is really good. Because the point
*  of the attention block is to note take as much as possible about the incoming sequence. So you have
*  this really long sequence, let's say. And if you're taking the dependency from every token to every
*  other token, you're giving MLPs or whatever it is that you're projecting as much information
*  as possible in the sequence. And you have multiple heads, each of them saying, okay,
*  they are looking at the sentence in a slightly different way. And then if you have large heads,
*  they're keeping a lot of detail about their own specific angle of the sequence. Any sort of
*  attempt to linearize this is saying, okay, how much of that detail do we actually need?
*  So the original attention paper was so useful because a lot of that we found that MLPs could
*  make use of a lot of that detail because MLPs are just like trying to find the deeper meaning
*  on whatever those notes that the attention took. So attention takes notes about this as many notes
*  as possible, but very computationally heavy. And then MLPs try to find deeper meaning from those
*  relationships. They sort of mix the heads, the new crossheads. So for linear attention, it's all just
*  trying to say, okay, are all those heads doing something important? Are we able to cut away a
*  lot of them? Do you really need every relationship to every other token? And this is a very
*  theoretical question, right? So it's not super clear how many notes, whatever you need. You also
*  have different ways of projecting across these heads. So MLPs are a very powerful way to mix
*  across heads and make use of these notes that are being taken. But like a Mamba block has much smaller
*  projectors. It's a very different story there of like how much they can really do from the notes
*  taken by the selective scan versus an attention block. Maybe if you had like bigger MLPs for a
*  linearized attention, maybe that would make up for it. Maybe you still need like more notes if you
*  had a Mamba block without like powerful projectors and then an MLP. This is really like something I
*  can't really say. If I did, then I would make the model. But I think all of these people are
*  motivated by the fact of how much can we throw away from these notes and still get performance?
*  Because you really need N squared dependencies. Does this make sense?
*  Yeah. And so coming to the shared attention, I guess I'm not 100% sure what exactly all is shared.
*  But if I understand correctly, it's like you are literally using the same attention weights
*  over and over again at every layer. But you are recomputing the effect of that attention
*  at each or every six layers because the computation has proceeded. And so each
*  time the attention block is used, you're able to use the same parameters that save space. But it
*  doesn't save like runtime computation per se, because you're still doing that attention on the
*  input as it's been processed to that stage through the model so far. Is that right?
*  Exactly. Yes.
*  Okay. Cool. And that's different from... So when you reuse an entire attention block,
*  that's different from just reusing the queries or just reusing the
*  queries and keys. You're reusing queries, keys, and value.
*  Yeah. So yeah, we have taken it to the extreme of saying these attention blocks are pretty
*  much just reminding MLPs anyway. So let's just stop storing all of these independent
*  parameters that eventually learn to do the same thing anyway. So let's just get them...
*  When you're reapplying, you also get really accurate gradients, right? The training time,
*  because it's applied six times instead of one if they're all independent. So we get this really
*  highly saturated attention block and it's completely tied to query key value. And then
*  we add a little bit more specialization back in for Zamba 2 by having alternating layers.
*  So now you have two attention blocks, they're each tied, but then we apply them one after another.
*  And then we just have some depth-wise loras that are themselves independent. So you get
*  a little bit of specialization across depth, but not too much.
*  Yeah. Interesting. The fact that it's alternating is somewhat counterintuitive. When you say there's
*  specialization across depth, I would have thought you'd maybe segment it into halves and have a
*  first half and a second half or a first, second, third blocks, but you're still staggering them.
*  And then I guess with the LoRa adapter, you have some kind of depth-specific thing that is
*  fully localized to that place in the model. Cool. Fascinating. All right. I'm talking more than I
*  intended to. Jason, let's get back to your main line of questioning on the technical details.
*  Yeah. I guess if I could just get set the history straight real quick,
*  we can go back to February of this year. You actually released, because this is how Nathan
*  and I actually came to know with Zypher was not the release of Zamba, but the release of Black Mamba,
*  a mixture of experts model that used Mamba. This was really early in the literature. I think
*  Nathan and I were counting papers at that point. This may have been among the first 10 Mamba papers
*  published. We've since lost count. Yeah. Well over 300 now. I really don't know the full count.
*  So what was it about Mamba in particular that got Zypher making this early bet and
*  going forward with Black Mamba? Yeah. So you're taking me back. When I first joined Zypher,
*  we were thinking we were all about MOEs. We're like a mixture of experts with very
*  vanilla attention blocks, no exotic shared blocks or anything like that. What's the way
*  forward for on-device? We had some ideas for reducing the inference time memory and compute
*  for these. And we were all in on training. We trained some good models actually at the time
*  for MOEs. Then Mamba came out and we were like, okay, wow, this is amazing for on-device. But the
*  question is, what does quality look like? Because we already knew that attention-free models had
*  this sort of problem of quality. Our motivating figure was in the original Mamba paper. There's
*  a figure where they try pure Mamba versus Mamba plus attention versus Mamba plus MLP. And they
*  have the loss per flop graph for all of them. And they don't show the absolute loss. So you
*  don't know what the actual quality is at the very end. So the MLP plus Mamba hybrid they saw was
*  really expensive. It had a lot of flops for equivalent loss. And we thought, we don't know
*  what the actual quality is here. So maybe the quality is actually really good and that you,
*  in fact, don't need all of these notes from attention, all these really rich cross-sequence
*  dependencies, which ended up being the wrong, the exact wrong thing. And we replaced these
*  really expensive attention blocks in our current MOEs because they're the ones that's really
*  giving us so much trouble. And then just do Mamba and then a mixture of experts, MLP block,
*  and just do that over and over. That would be really inference efficient for what we were
*  preparing for. So we trained it. So we set everything up. We trained the model. We did indeed
*  see that in terms of long sequences, it was amazing for overhead, but Mamba on its own
*  can't really make up without these, the attention cross-sequence dependencies in context like those
*  exact same things we learned. So the model was not great on MMLU, for example, which is like your
*  early indicator, not that you want to saturate MMLU, but that's an alarm bell of, oh, your model is
*  not really able to learn in context. So that was the early lesson. That's why we didn't really
*  proceed with doing Mamba without attention anymore. MOEs maybe they'll come back in the future,
*  but yeah, that was the initial model. Any questions or thoughts on it? It was an experiment that we
*  shared with everyone else rather than something that we wanted to actually deploy. Hey, we'll
*  continue our interview in a moment after a word from our sponsors. As a Cognitive Revolution
*  listener, you're obviously interested in cutting edge AI technology. And with that in mind, I'm
*  proud to say that this episode is brought to you in part by Notion. Notion has been a clear leader
*  in high value applications of generative AI since the wave began. Earlier this year, we had Notion
*  AI engineer Linus Lee on the podcast. The quality of his insights showcased the caliber of talent
*  that Notion employs. And that inside look at how Notion builds with AI is still extremely valuable.
*  Given my personal focus on AI automation recently, I specifically wanted to highlight
*  Notion's library of workflow and automation templates. If you're looking to streamline
*  your processes and lay the foundation for future AI driven automation, these templates are an
*  excellent starting point. And even if you're not ready for full automation, you'll benefit immediately
*  from Notion AI. Notion's latest all-in-one AI implementation that searches through thousands
*  of documents, regardless of whether they live in Notion or on some other platform like Slack or
*  Google Docs to deeply understand the context of your work and generate highly relevant analysis
*  and content just for you. Notion is used by more than half of Fortune 500 companies,
*  helping teams reduce emails, meetings, and time spent searching for information.
*  Want to try it? Head to Notion.com slash Cognitive Revolution. You can start for free
*  and using our link supports the show. So join me in giving Notion AI a shot today at Notion.com
*  slash Cognitive Revolution.
*  The Cognitive Revolution is brought to you by Element, a zero sugar electrolyte drink mix
*  that's working to change how we think about the role of salt in hydration and performance.
*  I have to say, when I started an AI podcast, I never thought we'd be sponsored by a drink company.
*  But when Element inquired about a possible sponsorship, they also offered to send me a
*  sample pack. And so I figured, might as well try it out. When the sample arrived, my wife Amy could
*  not believe what a perfect fit it was for me specifically. For years, I have felt that my
*  body needs more salt than nutrition labels indicate. And so I was interested to learn
*  that the Element formula is based on a growing body of research suggesting that most people
*  perform best with two to three times more sodium than official guidelines recommend.
*  I was also fascinated to see that they specifically recommend it for people who
*  fast regularly, since I personally don't eat until dinner time most days. Obviously, I'm not a doctor
*  and what my body responds well to may or may not work well for you. But after drinking Element for
*  a couple of weeks, I can sincerely say that I really do enjoy the product. My favorite flavors
*  so far are the mango chili and grapefruit. And I, for one, also enjoy the raw, unflavored version,
*  which reminds me of the taste of the ocean. If you're curious about optimizing your electrolyte
*  intake, you can support the show and get a free sample pack with any purchase by visiting
*  drinkelement.com. That's drinklmnt.com.
*  It's a huge change in strategy to pursue to go from an MOE to something like Zom- I mean,
*  something that's- MOE model's really hard to run. The parameter count's huge if you scale that up.
*  In terms of just memory, you've got to store a lot more weights. And then you go to Zombo-1,
*  way more parameter efficient. So I guess just the thinking of what drove you to go the other way,
*  I understand the attention part within context learning that makes sense. But I guess the local
*  inference part as well a little bit. Oh, definitely. There's a reason all of our
*  Black Mamba plots are in terms of efficiency. It is such an efficient model because there's
*  no attention anywhere. There's no quadratic complexities. There's no KV cache at all.
*  It's just the constant state that Mamba has to require. So your memory overhead is on the floor.
*  Oh, I also forgot to mention that motivating figure. So yeah, the reason we were doing MOEs
*  was that we knew that the loss per loss of MOEs is much more amenable because you're only routing
*  to a few of these experts at inference time. So we were trying to hope that we would dip that line
*  of loss per flop quite a bit lower than both the attention plus Mamba and the MLP plus Mamba.
*  And in terms of pure loss, oh yeah, we did. We definitely did that. But in terms of model
*  quality, it just wasn't where we wanted it to be. Can you talk more about that divergence between
*  pure loss and model quality? I think that is one of the biggest picture questions that the entire
*  field is struggling with, right? From a super big picture, like when does AGI arrive? And also,
*  people worry about this in the context of AI safety with emergence. We believe or we feel
*  pretty confident we can predict a relatively narrow range of what the loss value is going to be as we
*  extrapolate scaling laws out, but then everybody's, but what does that turn into? And so you're
*  highlighting here one moment where you have, or one example where you have seen this divergence
*  between loss and quality in a negative way where the quality is less than you might have hoped
*  based on the loss. Presumably that could go the other way too, right? It doesn't seem like these
*  are, I think, more guidelines than actual laws is probably the right way to think about the scaling
*  laws. So yeah, tell us, basically, I'd be interested in everything about how these divergences between
*  loss and quality open up. Yeah. So loss is not a very useful indicator at all. So early, I use it
*  to detect spikes, obviously. So it tells you, okay, your model died. And we definitely saw those,
*  especially with Black Mamba, as a very unstable model to train actually. In terms of model quality,
*  though, it's not a great, like generally you want it to go down. Do you want it to go down to three
*  or two? It's dataset dependent. The noise of your data strongly determines this. I would say one
*  thing I check it for is that it's a very early indicator of whether your model is saturating
*  or doesn't have a high enough learning, like whether it's progressing. So your loss decrease
*  is obviously going to slow like way down as you hit a stable point of training. Like you've reached
*  the slope of the optimizer landscape and you're going down. So that's great. But if your learning
*  rate, for example, was not aggressive enough, then you might just completely plateau in your loss.
*  And this is kind of like danger, like you've done something wrong. So that's really all it can tell
*  you. Everything else is coming from evaluations. Now, evaluations are also tough because if you
*  maximize evaluations, it costs everything else, which if I wanted to do that, I would just do
*  synthetic textbooks for my entire training dataset and I would blow up evals. Great.
*  But when you actually talk to the model, it's super dry. You can't really fine tune it very well
*  because it's assumed that it's exact, very clean distribution of data. It doesn't really respond
*  to unclean data very well. So what you need is to understand what each eval is actually doing
*  and providing for you. For example, I believe it's Hellaswag is one of the evals and that one is like
*  general language capability. We're finding like this, your model, just model very simple sequences
*  and that's like a very smooth, it's like a better loss almost where it just like linearly increases
*  across training. Then you have weirder evals like MMOU that are important indicators. For one,
*  they tell you how contaminated your data is. If MMOU explodes, you've probably done something
*  wrong. You probably downloaded some data that includes some MMOU questions. And then obviously
*  we do very careful test overlap with our training sets as well to also indicate this. The MMOU is a
*  really good indicator of whether your model has reached this emergence of in-context learning.
*  And it really is an emergence. So it doesn't show a signal for a very long time. And then near the
*  end, it starts to grow up because your model is starting to grok this in-context learning task,
*  which is difficult for it. Finally, there's a bunch of us like we've reached tests like factual
*  understanding with the ARC, easy and ARC challenging, our challenge evals. So those
*  really show us how well the model is understanding factual recall, how much Wikipedia we put in there,
*  how many textbooks. And then lastly, you really just need vibes, man. We have this like a set of
*  prompts that show us really key, like is the model fun? Like things like is the model able to roleplay
*  like as a pirate is like legitimately something that's really important to see because if you
*  give a model like phi, you tell it to act like a pirate, it will ignore you. Like it'll stick
*  with it a little bit and then just immediately drop it. And that's important to test. We also
*  test things like not quite strawberry, but like how many times like a flower bloom if it blooms
*  this many times like in a year. There's a lot of vibes questions that we ask the model across
*  training. And at the end of the day, you want your model to perform well on things you actually
*  wanted to do, not just benchmarks. And those are the questions that we're asking like personal
*  assistant questions and this sort of thing. And that's what actually indicates whether the model
*  is coming quality. Anything there you want me to drill down on? That's kind of our process.
*  That's fascinating. Moments of I think more anecdotes, if any, on like moments of emergence
*  are interesting. It sounded like you were saying MMLU kind of you understand to be a reflection of
*  in context learning. Is that because you're like doing few shot testing? Like I'm a little
*  bit unclear on what basis you would equate MMLU with in context learning. And then also just
*  interested in what the two curves look like as you go through training. I'm taking away, I think that
*  like the loss curve is just doing its smooth decay thing. But you're seeing these like relatively
*  sudden spikes in performance on key tasks. Is that right?
*  This is exactly true. It's also like all of the vibes questions are also like this, where it's
*  like, oh, the model suddenly gets it like early on. And even halfway through the model keeps getting
*  tripped up on silly things. But when the model gets it, we're like, okay, we've reached this key
*  milestone. So yeah, loss is always you just zoom in and you're like, okay, is there a slope? Is it
*  negative? Yes, move on. The reason MMLU is hard and the reason it tests like in context learning
*  is that its format like it requires a very strict format. That's really it. And also very weekly
*  tests, factual recall, because these are all college based questions, but it's answer as a
*  letter, a multi choice, A, B, C, or D. So the model is used to filling in the next token. It's not
*  really used to just this big long question. Oh, format your answer like this. The model is not
*  used to just saying C. It's used to saying, oh, astrophysics is this field with all these things
*  that are actually using text. And for the model to understand you are supposed to answer with a
*  single letter in that letter is supposed to encapsulate all of the background knowledge of
*  whatever the question is trying to get you to answer. That is something that shows up very late.
*  So yeah, MMLU is like random for most of training. And then after it depends on the architecture,
*  actually. So for a dense transformer, you need to be like later on in your learning rate schedule.
*  So your learning rate has to have settled down a little bit. And then you have to have seen
*  something like several hundred billion tokens. And then suddenly, MMLU just starts to climb
*  pretty linearly until you saturate. So it's like flat and then it grows up and then it
*  flattens again once you see your learning rate is too low and you've seen enough tokens already.
*  For pure SSMs, actually, this number is really high. Falcon Mamba, this was like three or four
*  trillion tokens, I think. It's multiple trillion before. And we theorize this is because of in
*  context learning. It takes a long time. You need a little bit of attention to kick the model into
*  understanding. Early on in the question, it told me answer it with a letter. And that sort of
*  relationship gets lost in a pure SSM block. But yeah, this is all it looks like.
*  So I often think back to that paper that was given paper of the year at one of the major
*  conferences. Emergence is a mirage basically was the sort of counter narrative to the earlier
*  narrative of emergence is a big deal. It sounds like you're on the side of emergence is a big deal.
*  And I'm basically with you. But to try to steel man the idea of emergence as mirage,
*  I think one of the more powerful points that they made was like, a lot of these graphs that we see
*  are logarithmic, obviously. And so when a thing is presented as a spike, that is still often over
*  like, actually an order of magnitude of data, right? You like tend to the whatever flops,
*  tend to the one, n plus one, 10 to the n plus two flops. And you're like, Oh, my, that came up fast.
*  But it's actually that was 10 times more than everything that came before in that in that plot.
*  Are you seeing things emerge? Is that consistent with what you're seeing in terms of emergence?
*  Does that change how you think about it at all? Or are you perhaps seeing things that are
*  spiking even faster as you really drill into to what's happening? And I guess one more,
*  if I could tack on even one more question there, you said the term grokking. Is that basically
*  your mental model for this that these things are learning the right algorithm or the right
*  conceptual representation to make a phase change?
*  Yeah, it's hard. I have everything I'm about to say is speculation as just a very empirical one
*  in my case. So it's definitely something to do with learning rate. So there's papers like Mini
*  CPM, where they just keep the constant learning rate for a long time. And then all of a sudden,
*  they anneal it really fast to zero. And you get all of the quality benefit during that annealing
*  phase at the very end when you're annealing it very close to zero. And also Mini tokens. So
*  it requires a lot of tokens. And then also something about their stage in the learning rate
*  schedule. My sort of theory here is that the model needs to see a lot of tokens. Like that's how I'm
*  saying grokking. Like it needs to grok. Okay, this kind of type of data that requires me to follow
*  instructions exists. That requires a lot of tokens for the model to learn. So that's the grokking
*  part. In terms of learning rate, I think it might be you need to settle more into the loss basin
*  in order to like make these really fine grains changes to how the model views the world. It
*  really makes me feel gross to say something that generic, but it's some sort of relationship
*  between the two of these. But both of them, I would call it grokking together.
*  Yeah, the learning rate, I do think is a, or the learning schedule is a probably generally
*  underappreciated part of this. It's not something I'm like super deep on either, but I've been
*  watching for Sophia. I don't know if you've looked into that like alternative to Adam. Do you guys
*  use that? We do not. Interesting. Have you tried? Yes. We think that this is partially because of
*  the learning rate schedule. So more aggressive learning rate schedules make a mirage of increased
*  quality when you're really just playing with learning rate. So we stuck with Adam for now.
*  We might be looking at like shampoo here soon, but not Sophia. Okay. I want to understand that a
*  little bit better, but just to try to set it up for you. If we envision a, of course, we're all
*  going to do this in different ways in our own minds. For me, it's a 3D landscape, even though,
*  of course, this is huge numbers of dimensions in reality. But I subscribe to the school of thought
*  where we visualize things in 3D and then say, end dimensions really hard in our head to allude to
*  the famous cartoon about that. So these are like very strange landscapes, right? Where we're seeing
*  an observation, computing a gradient. How would we have done better on this observation? Let's move
*  the weights a little bit in that direction. And we'll be at a slightly lower loss as a result of
*  having made that change. And then in theory, that gives us better performance. Although of course,
*  it's a super noisy thing because an update that made us work better on one particular observation
*  might not work better on another observation. There's banning that goes into this and aggregating
*  a bunch of observations at once and making an update. And this is basically a very black magic
*  sort of thing still where nobody really has a great sense for what the true nature of these
*  landscapes are or how best to navigate them. But when you're talking about aggressive learning
*  rate versus annealing, that's basically saying how big is the step size that we're going to make,
*  right? From one moment in weight space to the next moment, like how big is that delta? And if you
*  find that the value is really happening most in this annealing phase where you're shrinking
*  the step size, this sort of suggests to me like a, almost like an Antarctic landscape where there's
*  lots of little crevices that could be around a good space and then you really have to drill into
*  this very, very local space in the landscape to find something that really works well.
*  That would suggest, because obviously we see a million things happening in the broader ecosystem,
*  that would suggest that there's probably a lot of them and that's where I get to this crevices
*  notion. But then I wonder there, I also see papers like the platonic representation hypothesis where
*  at the same time that's happening, there's this other line of thinking that's at scale,
*  things seem to be converging. The basic notion of that paper, I'm sure you've at least come across
*  it a little bit is with greater scale, with more modalities, it seems like the internal
*  representations of concepts are converging in some high level statistical sense. So how do you
*  make sense of, can you begin to make sense of all that where there's like
*  seemingly a lot of different local points that you could drill into, but there's also this sense of
*  global convergence. Can those be compatible? Does one have to be wrong? I find myself confused.
*  For the pocket idea, it's definitely not a flat area with lots of pockets. If we were to go with
*  that, it would definitely be a general slope downwards with pockets along the way and then
*  you can settle into one of them as you go. This is just because even in the constant phase,
*  when you're taking those big steps, people like many CPM authors still saw improvements,
*  just less improvement. I definitely know that your lost landscape is much smoother for larger models.
*  You can more richly like model the space and therefore just increasing the scale makes it
*  much easier for your optimizer to make progress. This is why things like novel optimizers like
*  Atifactor or Sophia or like second order optimizers, it's like the bumpier the landscape
*  is, the more accurate your step should be so that you don't get kicked out of the gradual slopes
*  that you want to reach. It's also like why we're seeing a lot of the conventional wisdom is
*  assuming big models because big tech assumes big models. So the recent people are doing dense
*  transformers with large scale optimizers. The reason why people say, oh, shampoo does the scale
*  and all this kind of thing is because when you're at large, your step is going to be broadly accurate
*  anyway when you're in this giant smooth lost basin. Why bother with any of these things?
*  I agree with them. You shouldn't bother. But when you have a 3D novel architecture model with a
*  really bumpy lost landscape, that accuracy really matters. That also translates into things like
*  batch size. So I trained the Pithia models back with the Luther and we were seeing that, for example,
*  like large batch sizes was causing instabilities. And it really confused us for a long time because
*  the higher your batch size is, the more accurate your gradient should be. So if you have these
*  super accurate gradients, this is even at the cost of seeing less data. As you increase batch size,
*  you'll see less data. But now I'm fairly certain and by looking back at the data,
*  if you have bad samples and as we were increasing the batch size, we were also increasing the
*  learning rate. And if there's just a few outliers in that batch that sort of tick your gradient in
*  the wrong direction, and then you have a large learning rate, you take a big step in that wrong
*  direction, then larger batch sizes were actually bad because you were reaching too many of those
*  outliers per batch and you reach too many bad batches in a row. And now you're going completely
*  the wrong direction. You just diverge entirely. So we actually had to use lower batch sizes,
*  but it's complex. You also need to, this is why people clip their gradients also, because if you
*  take one step in the wrong direction, make sure it's not a big step and then hope that big step
*  can be reversed by the next couple of steps. So there's a lot of like weird alchemy going on to
*  get models to actually converge. I've noticed that every run has its own like cursed way.
*  And the reason people like really want to use Adam, the reason we're using Adam is because Adam
*  is extremely robust. That's the main reason. So that's why people can publish papers like Sophia
*  and AttaFactor. If you look enough, then you'll find cases where they're better. But Adam is
*  good at everything. It's not the best at some things, but it's good. It doesn't have any
*  like glaring weak points, like optimizers like AttaFactor and such that might just not work.
*  And then you spend three weeks like trying to get your initial stability for this weird
*  combination of hyperparameters and model size to actually work. That's how I look at it though.
*  Somewhat novel intuitions for me, but I want to just confirm with you that they match yours.
*  Overall, you're like, it's easier to get big models to work. It's harder with small models.
*  That seems to be maybe a reflection of just like how overloaded the small models are.
*  If I think about just a super dense, everything packed in super tight sort of network, then I
*  would imagine that it's just easier to mess things up if I take a step in the wrong direction.
*  Whereas if I go to a trillion parameters at the very far end of reportedly a GPT-4 type architecture,
*  then I can spread this out over many experts and things aren't so overloaded and one wrong
*  step in one place might not even affect most of the network because it's localized to experts
*  or what have you. And so then I can be more aggressive in my step size and I can get
*  something like a Sophia to work well in those bigger contexts because I just have more room for
*  error essentially in my training process that I just don't have that luxury if I'm
*  training a smaller model. Am I interpreting you correctly there?
*  You're close. So like for larger models, you want an actually like lower learning rates because
*  even though it's like a smoother loss landscape, you don't need the small model ability to really
*  jump over these crazy hurdles and stuff. But think of Adam, right? You have a variance term,
*  you have a momentum term. That's to tell you if there are bumps along the way downwards,
*  then you still make progress downwards because you still have momentum. You have faith that this way
*  is probably like the best for the loss landscape despite some bad gradients. For larger models,
*  despite the smooth loss landscape, you want a lower learning rate just because one of
*  instabilities in general tend to come up. It's because you have so many parameters that go
*  beyond the point of no return. So I heard the Adam one, the momentum is there to say,
*  we're not just going to look at this particular batch of updates and calculate naively what
*  would have made us better here because we know there's a lot of randomness. And so we're going
*  to keep track of the general direction we're going, which is the momentum term to make sure
*  that we're like not getting too randomly sent off in weird directions. We're going to try to have
*  some general sense of what direction we're going. I'd be interested to hear the sort of similar
*  narrative form for Sophia, if you have one there that would explain why that's different and maybe
*  why it's better in some places than others. And then I was also going to ask about distillation.
*  It seems like the big trend with the frontier developers has been go huge and then distill.
*  I wonder if that's something that you guys might also be thinking about if there's a Zamba 70B or
*  even 400 and however many be in the background somewhere. So in terms of Sophia, I don't have
*  a good intuition for this actually. I explained why Adam is great and why I think Adam is good
*  at everything. It's like very robust, but I can't really explain why everything else is brittle in
*  its own way. And this is not really just to say that like everything else is bad. It's just to say,
*  I haven't put the time in to any other optimizer just because I've been burned enough times by
*  alternative training strategies that just end up not being generalizable. I don't want a bunch of
*  like a toolkit that's specialized to each training run. That's not the point because then I have to
*  spend as much compute as a training run to try and figure out how to get this specific thing to
*  converge. I want it to just converge. And even if it doesn't converge quite as well, I'll train on
*  more tokens because I was able to kick it off day one and I'll still end up at a lower loss.
*  On your MOE points, so MOEs are themselves like a really tricky thing to optimize
*  because like for one, the attention block is not divided. The attention block sees everything, but
*  for the expert blocks, you're subdividing the batch across everybody. So like they're effectively
*  seeing like a different gradient noise scale than the attention block. So trying to find the right
*  batch size is clearly much higher, but do you scale it by number of experts higher for the
*  batch size? Because you've subdivided, that intuitively makes sense. But the problem with
*  this is that now the attention block is getting this massive batch size. This is part of why
*  MOEs are super unstable, I think, to train. Like Black Mamba was like a pain to train because of
*  this. Like attention blocks are seeing more accurate gradients is one way you can think of it
*  than like the experts. Trying to port new transfer is something that I'm really looking into here.
*  Actually, the people at the team at Cerebris is really deep on this. They're really good.
*  So we're trying to crack this, mostly them. But yeah, we're working together. But in general,
*  trying to find for these hybrid architecture that we're seeing, for example, that's kind of true for
*  us too, because we have this shared attention block, which is going to have more accurate
*  grades and see more data. Finding something that converges is really difficult. And like being able
*  to navigate the hyperparameter super really determines if you live or die.
*  Fascinating. Did we get to distillation? Are you guys going to pursue a big to small strategy as
*  well? Yeah, yes. That is the plan. The problem here is that you need a lot of compute to train
*  those large models. So it's something we're scaling up for now. In terms of the actual
*  distillation step itself, unfortunately, big labs are very tight-lipped about this. So even the
*  annealing, it started emerging. Oh, annealing, by the way, it's like the continual pre-training
*  step that we picked up early, where you first do a standard cosine decay, you warm learning rates,
*  and then you slowly decay it over time to some high value, higher than normal. And that's like
*  your phase one data. So this is more like web data. It's a bit noisier. It's still important to have
*  so that the model knows what this data looks like, knows how to respond. Like a pirate.
*  Yeah, exactly. But later on, you want to bake in more intensely a higher quality
*  subset of your data. The higher quality doesn't mean textbooks again. It doesn't mean you want
*  your model to be dry. But you can only look closely at so much of your data. Everyone says,
*  look at your data, but you can't look at three trillion tokens. You can look at 50 billion,
*  100 billion tokens and apply some really detailed filtering and deduplication to those and make
*  sure it's the highest quality, even if it's a distribution that represents all of your data.
*  So anyway, you decay down to a relatively high learning rates. And then on your first phase,
*  and that's where most of your tokens are coming from. And then in the second phase, you very
*  quickly rewarm your learning rate. You say, okay, I want the model to respond really quickly. Again,
*  we're in a new loss landscape. We have a new distribution of data and then very aggressively
*  decay down to zero. We say, okay, I want my model to respond quickly to this data and then settle
*  very quickly into the new law space and that emerges from the high quality data. And also,
*  you're able to stomach this new high learning rate again, because your data is very clean.
*  You don't have this problem I was mentioning earlier with 50, where you have these crazy
*  outliers that kick your gradient in some different direction. So you're able to go to with a model
*  that's already settled into a good place, you're able to increase the learning rate a lot on this
*  high quality data, and then really bake it in. So it's top of mind to the model. This also increases
*  the flexibility. I see it as a branching path. The base model is the base, the trunk. And then you
*  can construct tune and then fine tune so that your model is becoming progressively narrower along one
*  branch. But if you have multiple anneals, that's like multiple sub-trunks, right? So you can anneal
*  on roleplay kind of data. You can anneal on, like, if you want to try a very factual model,
*  you can anneal on textbooks and such. But then from there, you can fine tune so that the roleplay
*  model is roleplayed on specific characters from the annealed roleplay checkpoint. And that is a
*  much more flexible scheme than just having a single base model, a bunch of fine tunes from that base
*  model. Can you define anneal? I've learned this in the context of biology, and I'm looking it up
*  online. It's also used in glass and metalwork. Maybe this is wrong, but I guess I think of it as
*  hardening into its final shape or with DNA. It's actually, you know, combining, coming back together
*  and reaching some lower energy stable point, basically. Is that the model here too?
*  Yeah, we put very detailed instructions and explanations on. It's called letter Z and then
*  cookbook, the Z cookbook. If you look it up on GitHub, we have a whole section on what is
*  annealing, what it means for us, what it means for your model. But yeah, annealing for us is like
*  trying to harden the model a little bit, the base model into a pre-fine tuned checkpoint that
*  has some type of data that we want top of mind. And practically this means rewarming a learning
*  rate on the new distribution. It means having some replay. So you still have to feed some of
*  the tokens from your batch from the phase one data so that you don't have catastrophic forgetting.
*  And then that replay plus new data distribution, then you very aggressively anneal the learning
*  rate down so that your model settles very definitively into a loss basin for you.
*  This all getting back to the reason I brought up annealing was you're asking about distillation.
*  Since the GPT-3 paper, the big labs have learned be a bit less open with people because then they'll
*  actually take compute and try and do what you're doing. That's why annealing for a long time was
*  like a hidden trade secret. Like the llama team cracked this with llama two. They split into the
*  Mistral team. They split up. They knew this sort of secret and then it became more and more public
*  over time and now everyone publishes it. Distillation has been the same sort of regime where the big
*  labs have cracked it, but they're staying tight-lipped about it so that they can try
*  and extract all the value before their people get poached somewhere else. And then it ends up being
*  public anyway. We don't really know the secret to distillation actually, but synthetic data from
*  large models is a proxy for this, right? So we're trying to look at this at least so that we can
*  our annealing and post-training strategies to more approximate the output of large models via
*  synthetic data. And then trying to actually use the logits during training to stabilize. So remember
*  earlier we were talking about can distillation help you navigate the bumpy loss landscape by
*  having basically a big atom that's holding your hand and saying, okay, no, this is the right
*  direction because this is what the big model would do. The big model is able to see much better that
*  this is just a little bump and you should keep going down. Using those logits of training time
*  is something that we're still trying to crack. We see generally positive things from a model
*  convergence standpoint, but it's still really inefficient to try and have a live inferred big
*  model at training time. So pre-training scale distillation we have not cracked yet, but I'm
*  confident that we will. So the basic idea that I have of distillation is training a
*  small model to reproduce the outputs of a big model. Not so much at the token level, but at
*  either the logits level or potentially if you had direct access to the large model, then you could
*  perhaps tie it like multiple places. You could say, I've got my trillion parameter model here,
*  it has a hundred layers here. I've got my 7B, it's got however many layers, but I can map.
*  Okay. At this point, I want it to tie up to the big model and try to figure out a way to
*  imitate the internal representations. Am I off base conceptually there at all?
*  That's exactly right. Maybe I'll expand on what I was saying to tie it to what you are.
*  So when I'm saying synthetic data is like a poor man's way of doing distillation,
*  you're just choosing the max of the logits, right? So like you're only training on what the big model
*  is paying attention to. And you can do that also with closed source models. We could do that from
*  GPT-4 or whatever else. Now logits are important because those are like the large model saying
*  exactly how it would respond to the current batch of data. That's why I'm saying it's kind of like
*  holding your hand in terms of the optimizer. Logits are also super important because you also want to
*  know what the large model is not paying attention to. So there's tiny zero values in the logits,
*  like the whole distribution helps the small model, not just the large values that you could get if
*  you were to like approximate with just the synthetic data. But yes, you need access to
*  the model for these logits, which is a big hurdle. It's helped now by big like LAMA 3, 4, or 5b.
*  But when you're running inference of LAMA 4 or 5b, every single training step, that's why I was
*  saying that at pre-training scale, this becomes prohibitively expensive. And trying to get around
*  that expense hurdle while still getting logits per step is what we're trying to figure out.
*  We think there are some cheaper ways to do this, and I think we will get them figured out. But
*  this is why it's not like popping up all over for open source people, because it's either
*  prohibitively expensive or synthetic data is just not like rich enough of a representation
*  to really help you steer in the right angle. And so just to make sure I understand what makes
*  it prohibitively expensive, it's basically that running 4.05b is like some fraction as expensive
*  as training 4.05b. So if you want to train your small model, but also have to run 4.05b,
*  it's you're going to end up spending as much compute as if you were just training a much
*  bigger model in the first place. Exactly. Yeah. In terms of practical sense, if I have a 7b,
*  then I'm already doing parallelism across GPUs to get it to fit in VRAM. And then if I have 400
*  billion parameters that I also need to store, even if it's for inference, you don't need to store
*  optimizer states and gradients and all this for the big model, you still need to fit it somewhere.
*  You still need to use the flops to infer it. You need to synchronize. It's a four pass with
*  the four pass of your own small model. Why don't I just train like a 4b from the start? And why
*  even deal with distillation? Is it really worth it? So far, these practical trade-offs have not
*  been cracked for us. That's what I'm saying. Yeah. Gotcha. It's not practical. It's probably
*  a slight improvement, but a lot of things are slight improvements. And just seeing more data
*  is always a very direct way to improve your model. And I could see more data or have more
*  parameters, and that's a more direct way to improve model quality right now than trying to get logits
*  from Lama 405b. That's just the practicality. Do you think it's possible that the big labs maybe
*  don't necessarily have a huge secret, but what they maybe have is just a different cost benefit
*  analysis where they're running so much inference that it's worth it for them to do this? Oh, I think
*  this is likely. Yeah, this is likely. I think that if you're Microsoft working on five and just use
*  GPT-4, it's on our own systems. We have infinite funding. So making it, there's two possibilities,
*  right? Either they've cracked a cheaper way to do it and we have to find it, or they have more money
*  and we have to find the cheaper way, crack it, and then do it. And both of those cases require us to
*  crack or find some cheaper way, unfortunately. Are there other things that you would put in the
*  bucket of frontier labs are sort of generally understood to have a solution that nobody else
*  hasn't diffused to the rest of the community yet? Data is a big one. Data and data cleaning requires
*  time, patience, and really just manpower that open source does not have. So when you're open
*  source, then you're just beholden to whatever data set other people are able to completely
*  focus on. And not a lot of people focus on data. So it will always lag the big tech companies. Also,
*  big tech has access to their own data, which is also very clean. It's an infinite abundance.
*  And we're definitely behind it. So yeah, cleaning data, cleaning data pipelines. This is what we
*  talked about. We just released Zyda 2, which is our Zypher data set too. There's some new data sets
*  in the open source regime called DCLM and FineWeb and DALMA and Zyda 1. And cleaning them up and
*  producing an actual at scale data set with Nemo Data Curator, which is Nvidia's data processing
*  tool we found has really lowered the bar for entry for data. But yeah, data is one. Another one is
*  things like hyperparameter transfer, unfortunately, has not been picked up a lot by the community.
*  You might recognize this as MuP or MuTransfer. I think it's Modula. It's a new paper that's
*  also found similar things. But it's like 30, 40 pages of map for these papers. And it's not
*  approachable for open source people or small labs and such. So only big labs have the computing
*  funding to put one person, okay, go read the MuP paper for a month and try and port it to our
*  ginormous monolithic code base and get it to actually work. So there's a lot of trade secrets,
*  I would say. Distillation is another one. Give us a little bit more on that one, because I honestly
*  don't have a lot of intuition for what that is adding to the overall stack.
*  MuP?
*  Yeah, exactly.
*  Oh, yeah. Oh, so MuTransfer is a way of initialization. It's like width scaling. So you
*  do all of your hyperparameter search on some really low width model, it's really cheap to run
*  training on. And you do all of your learning rate sweeps, for example, all of your batch size
*  sweeps. And then if you literally just divide by a scaling factor of your low width by the high width
*  of the actual model that you want to train, both in terms of the learning rates of your hidden
*  layers, like your embedding scaling, you can multiply by some new hyperparameter,
*  then you just get a perfect transfer from the small model to the big model. And as in the learning
*  rate that I found was optimal for my small model will also be the optimal learning rate for my big
*  model. And this is all just making sure activations don't explode by all of these small scaling factors
*  of width. This helps you in terms of both you're able to more accurately search the loss landscape
*  because the compute is so cheap on the small model that you're able to really search a higher amount
*  search space of learning rates and batch sizes and stuff. It also helps just the general stability
*  of your model because your activations are exploding and your model's not learning on the fly
*  how to account for its own explosions. So you're able to also deal with a much higher learning rate.
*  Alternative architectures and optimizers are also much easier for this because you can just directly,
*  for example, the mixture of experts. If new transfer is cracked, then you know exactly
*  how to ensure both the attention block and the expert blocks are both seeing relatively equal
*  magnitude weight updates, which is what you want for stability. These sort of details tend to be
*  hoarded in big tech right now and slowly diffuse out to everyone else just by people going to
*  different organizations in big tech, people publishing people and open source kind of cracking
*  it. If there's others in that category, keep running them down. It's endless, man. So this is
*  why the Luther AI is so important. I mentioned them before an open source collective where
*  everything start to finish is open source, the data set, the training framework, the actual
*  produced models. If you don't see all of it, like for example, Lama 1 was great because they shared
*  everything. They shared all of their data pipeline and people made red pajama, which is a full
*  reproduction. Lama 2 was they stopped sharing the data set. And as I told you before, this is
*  because of annealing. It's just too tempting to keep the important parts to yourself and publish
*  a paper that's just vague and glosses over it, but keep going. What else? So for example, the
*  second order optimizer thing that I told you for small models specifically is definitely something
*  hoarded. So that's like a trade secret. Gemma also did it. So they just say, we use the second order
*  optimizer, which one, how do you distribute it is a big one. Because if you have a second order
*  optimizer, you have a bunch more states that you have to store in memory. And how you split those
*  across GPUs is non-trivial. So that's another engineering detail that they want other people to
*  catch up on while they extract the information from. So second order optimizers are small models
*  that are distributed in a specific way. Now we're cracking it with shampoo. And then all of these
*  things that I mentioned all interplay. If you have a second order optimizer, how do you port
*  MuP to it, Mu transfer to it, right? Because now it's not Adam. You have to reapply the theory. Do
*  you spend another month trying to figure out the new theory? I would say, curiously, alternative
*  architectures like Zamba are not hoarded by Big Tech because Big Tech saw the quality issue with
*  pure SSMs in a lot of ways and said, okay, quality is the most important to us and we have infinite
*  inference time compute. So let's not bother with it at all and sure we have the highest quality
*  model. And that's more for us, right? But I think they were much slower to catch on to SSMs and
*  alternative architectures just because it was not super clear to them at the time that you could
*  solve this accuracy problem by some exotic architectures and by being really data-driven.
*  What else? Parallelism schemes for all of these, like I was starting to mention with the optimizers,
*  but parallelism schemes for new model architectures and optimizers and combinations, those tend to be
*  proprietary. So Lama shared that they had like a 4D parallelism sort of scheme, but how you set up
*  that topology on your own, that's all like empirical knowledge that you have to get from training a
*  model. Same thing with like arcane things like checkpoint restart. So like a lot of these
*  bigger runs, they use like dedicated nodes that are just being used to save checkpoints.
*  And then when you have thousands of GPUs, one of them dies all the time. So you have to keep
*  slotting in the checkpoints from those backup nodes. That's something that's really easy
*  conceptually, but hard to set up and in some sort of proprietary Big Tech stack.
*  Everything is what I'm getting to. There's a lot of points, especially about your gritty details,
*  engineering details, scalability details that are very closely kept, tied to whatever organization
*  has them. And they also know that even if you say worked on one of those Big Tech teams and you know
*  the secret and you go somewhere else, like porting it to their stack is a very non-trivial thing,
*  right? It's completely built off of the proprietary stack of whatever company came up with the idea.
*  So do you remember it well enough to port it to this new stack? Maybe not. So there's
*  really a hardening of ideas and training processes that exist in each organization
*  and that is increasing over time. So I think we have a few more technical questions. One
*  obvious kind of pulling up question for a second would be like, the story you're telling sounds
*  pretty consistent with the allegedly leaked anthropic fundraising deck in which they said
*  that the leading companies in 25, 26 might get so far ahead that nobody can catch up.
*  And I think we've understood that, or I've understood that broadly as sort of an accumulation
*  of these secrets and then also just like having the best models. We now have this,
*  I think pretty credible reporting that OpenAI is using a one to generate the data for the next
*  scale up again. And that seems like there's not just a moat, but there's like multiple
*  motes in depth there. And yet you guys at Zypher are like a small company and trying to figure out
*  how to compete in this space. So what is your sense of how you and other companies that are not
*  infinitely resourced, even if you're like reasonably well resourced, how can you compete?
*  Is it about finding a niche that they're not going to play in or is it about some sort of
*  breakthrough insight that is going to be needed? How do they not just come to dominate the entire
*  space? Yeah, I will say small models is overlooked by big companies because OpenAI, XAI,
*  Anthropical, all of them, their job is producing the highest quality model.
*  And yeah, sure, they wanted to distill into a small model for inference reasons,
*  but if it came down to cracking distillation or making an even better, bigger model,
*  that is it only needs to be a little bit better. Claude's Sonnet 3.5 only had to be a little bit
*  better than Chats GPT to take a large portion of market share. So accuracy really takes them.
*  That's also why they don't want to like experiment too much with these weird hybrid architectures,
*  because if it affects model quality and you only determine that when you train a big model,
*  it's a lot of cost when you know that dense transformers work the way that you expect.
*  Yeah, in terms of how we can compete with them, I would say it's a mixture of this,
*  they're focused on large scale inference, large scale training, definitely makes them,
*  even if they have things like distillation, that's only one part of the process, right? So like we
*  had to crack annealing, we had to crack architecture, we had to crack data, the entire training
*  process from start to finish. It wasn't just like the distillation step, which has only helped when
*  you're at a big company, right? We're very nimble in that way. We're definitely in a unique time
*  where if you're nimble enough, and you're focused on small models, like you can very clearly have
*  an advantage over big tech over time, as more of them use distillation and such that if we were to
*  not move at all, then we would definitely vaporize compared to their resources. So the way we're
*  staying ahead is by continually pushing onto what the next free lunch is for small models.
*  Next, like second order optimizers is one getting a cheap way to do distillation is one that will
*  protect us from that angle. Like we're clearly very willing to make big bets on the alternative
*  ways of training. And big tech just is not really looking very closely at this sort of regime. And
*  that's why we have the best model now with seven B is the best because of this exact reason.
*  Are you studying the entropics project that has recently been catching a lot of buzz or similar?
*  Very loosely, I'm not an expert. I would kind of categorize it under the definitely doesn't scale.
*  So I believe it was Tim Dettmer's tried this at scale with like larger parameter counts,
*  and it was like no better than Adam. I know the thing is that I kind of view it as kind of specific.
*  So whether it's robust or not, or whether it's very specific to the training setup on like the
*  energy PT is yet to be determined. It's true with this for a lot of things you can show
*  like huge speed ups on even though what is it like crowd source compute, like retraining compute,
*  but it's hard to show things that are robust. Like that is the actual test is this robust.
*  And I'm waiting for someone else to spend the compute to determine if this entropics is robust.
*  You're describing it in a different way than I expected. Okay. The one that I have been
*  at least momentarily fascinated by recently is essentially a improved sampler. So it is like
*  trying to differentiate between like when the model is confident and should just like pick the
*  most likely next token and everything's kind of hunky dory versus when it's out of distribution.
*  And then when it might need to like, it does interesting things like kind of dynamically
*  inject a additional clarifying question. If it detects that like generally we're confused,
*  let's maybe like just burn some more cycles. How can we do that? Let's artificially input a clarifying
*  question. And then sometimes it'll even like back up and say, we seem to have kind of lost
*  the thread here. Let's like go back to an earlier point and rerun inference again.
*  So I've thought about this entirely as an inference thing. You were going toward the
*  training side. Are we talking about the same project? And if so, I missed the training side of it.
*  You're making me question myself. Maybe I'm confusing it.
*  Well, for what it's worth in terms of like a possible next free lunch, the one thing you
*  did say that matched my intuition, even though I've read like a little bit that like it might
*  not be working as well at larger scale models, I wouldn't say that's like well established in
*  my mind. But if there was a story as to why it might be, it would be like the larger models are
*  maybe like grokking into some version of that on their own through all the, especially through all
*  the reinforcement learning that they're doing in late stage training, whereas the small models
*  are maybe not getting there. And so layering on these sampling heuristics could be like just much
*  more beneficial at a small scale. This naturally has me thinking too, what about learning a sampling
*  function as part of the overall architecture that feels like a candidate for, if any of this is real,
*  I haven't quite got to the point where I'm like convinced that there's a real there, but it seems
*  like there is perhaps like learning a sampling function could be another relatively like small
*  amount of parameters that could lead to some like qualitative change. I agree it definitely could.
*  I also agreed on the point you made about like larger models doing this on their own. Larger
*  models, for example, data quality matters a little less because larger models learn to self-select
*  what is important, what's not. There's a reason that like when you go to a large enough model
*  scale, you just scale it up and just turn it out, turn out more and more data on more and more
*  parameters. And the model kind of is so robust that it's able to learn these properties that
*  we would need explicit training properties and processes for at the smaller scale.
*  So that is one thing that big tech kind of lies on as a crutch, that we are able to find the
*  explicit process that is able to emulate the same behavior from the model a bit faster because they
*  can just rely on the model figuring out its own. But yeah, I do agree that it could help us, but
*  we haven't looked too deeply into this just yet. I'll ask one more and then Jason, let's come back
*  to you and you can map some of this stuff onto the specifics of Zamba and state space hybrids
*  in particular. How would you describe like where we are in this overall process? We always hear
*  we're still so early. That basically seems that would be like my vibe level takeaway from
*  your comments. There's a lot still that maybe hasn't even been properly investigated, let alone
*  understood. I would agree with this. I definitely don't think this is a solved problem. I don't
*  think we found the limits of scaling. We clearly have not found the limits of architecture. Whether
*  there's some groundbreaking thing tomorrow or like attention to comes out and everything is thrown
*  away. I can't really say that, but I can definitely say that we've moved very quickly into a search
*  space that's massive. There's a lot of very low hanging fruit that is just obvious. It's everywhere
*  that we have not picked up and these training processes and stability, there's still so much
*  out there. Even if you were to just take pre-training model papers and compare them, I'm sure there's a
*  lot of things that people are reinventing. There's a lot of trends across scale and training process
*  are to be found that people have implicitly found, but either not known or purposely not shared with
*  everyone else that are just lying around. That's my sense too. It doesn't seem like we're at the
*  end of this cycle or anywhere particularly close, which is pretty crazy to contemplate because it's
*  already come pretty far. One really low hanging fruit example of this is the GPT-3 paper has
*  really specific hidden dimensions. This was both true in terms of quality, but it was also in terms
*  of kernel paths. For example, there's lots of powers of two in their hidden dimensions,
*  but not quite enough. Everyone else copied the GPT-3 model configurations for a long time without
*  understanding that, oh, these are more efficient on GPUs in addition to be approximately the right
*  size. This is another thing we've baked into our Zamba models is that since we're trying to make
*  the most inference efficient thing on any parallel hardware, if you do a very simple trick,
*  put lots of powers of two in your hidden dimension, you're also sizing up these different
*  blocks just by rounding very slightly to good kernel sizes will give you speed ups on any
*  parallel hardware. Whether it's multi-core CPU on a phone or something like an MPU on Intel,
*  like an M1 for Apple or something, if you have parallelizable model sizes, then for the lifetime,
*  the entire lifetime of the model, you're more efficient. This is something that big tech just
*  says, the Lama 3 has this size, but they don't show you that they went per block and found the
*  efficient sizes for kernels for each of these and then baked it into the model. Same with the vocab
*  size. The vocabs are all rounded to some factor of 64 for the same reason. They're just more
*  efficient kernel paths. You can go down with that. My very simple intuition for that would be just
*  if you want to break something out into two, four or eight GPUs, then if you have a ninth thing,
*  then you're probably... If you go eight wide, the difference between eight and nine is one and two
*  in terms of how long you have to wait. Are there a lot of different versions that you see or is it
*  really pretty much that simple? It's not that simple. You can decide how baked in your model
*  size is going to be. For example, I mentioned a few times this power is a two in your hidden
*  dimension. This is true for any parallel hardware. If you train on an AMD MI300X GPU
*  and you have lots of power to two, it's probably also going to be efficient on Nvidia H100. It's
*  going to be efficient on your phone, but you can get really deep with this. There's something called
*  wave quantization where let's say you have 100 skewing multiprocessors on the H100.
*  If you have 100 of one units of work, then you need to do two time steps. First one with 100
*  and the second one with one. The throughput will be roughly half because that second time
*  step is pretty much empty. About the same amount of work, but two total time steps throughput is
*  half. Whereas if you had 100 units of work, you just have to do one time step. Then on your graph
*  of throughput on the Y axis and problem size on the X axis, you're going to get waves.
*  Each time you kick down on the wave, you have lower throughput. You are on a new time step.
*  This is baked into your models. If I was Nvidia and I wanted to train a model that's only efficient
*  on Nvidia hardware, I would bake in that this model has very specific sizes to fit on the number
*  of skewing multiprocessors on the H100, has the amount of SRAM. Whereas on an AMD competitor,
*  like an AMD MI300X, on that one, it'll require two waves or something like that. Or SRAM will be
*  undersaturated with the model sizes you put in. The bad version of this feature is that
*  everyone is building their own chips and everyone is building their own models.
*  Then everyone would produce a model that's only efficient on their own chip.
*  And it's specifically inefficient for everyone else. It's unclear whether we'll go this direction
*  of perfect specialization for a company or if companies will say, okay, I can't crack all of
*  model training and I need my hardware to be able to run competitor models that we run on our own
*  data. So maybe in that sort of case, you would want everyone, like the good future of everyone
*  provides similar hardware that can run everyone else. It's unclear which way this goes, but this
*  is just another example of there's a lot of low-hanging fruit for one. And for two, there's a lot
*  of return that you can get by just getting out of magnifying glass and looking at every single step
*  through your training process to extract everything you can from it.
*  Mad Fientist-Longer Yeah. You follow Greg Brockman on Twitter and you realize how much of that he has
*  personally done over the last couple of years at OpenAI. And you're like, yeah, there's the reason
*  that they're obviously extremely good at what they do. And you can see the rough outlines of how that
*  work is unfolding there in his Twitter feed in particular. So recommend that as a not very open
*  window into what's going on, but at least a tiny little peek. Jason, what's on your mind?
*  Jason Bahlman Yes. Just a pleasure. Super interesting conversation here. The ins and
*  outs, the inside scoop on training. I guess I would really be remiss not to do a couple deep dives
*  with Quentin while we have him on Zomba 1, Zomba 2. Maybe let's just start with a deep dive on
*  Zomba 1, if that's okay. And in particular, you look at the architecture, it seems pretty
*  straightforward. There are six Mamba layers to start off that the input sequence goes into.
*  And then this interesting thing happens that I'd like to talk about. So there's this step before
*  the attention block of concatenating the residual stream coming out of the Mamba block with the
*  original input embedding. So this is very interesting. So the attention block gets to see
*  the Mamba residual stream plus completely unmodified input embedding. It feels right
*  that if you're running the attention computation, you'd want to do this. But at the same time,
*  it's interesting. How does one arrive at a feature like that? Is this something that
*  your team is okay, it's intuitive, so let's try it? Or is this something that through many,
*  many different experiments that just rises to the top and it's more experimentally found?
*  Quentin Okay. On the specific concat, if I recall, we did run a lot of experiments, but it also was
*  intuitively right. Our experiments matched our intuition, which is where we want to be, that we
*  want the attention block to be able to see like the entire input and residual. There's really not
*  much more to that. It empirically works and intuitively makes sense. So we stuck with it.
*  In terms of Zombo 1 in general, we kind of crystallized more and more of our thoughts
*  on how an inference optimal model should look like. So that's when we discovered that yes,
*  indeed, attention blocks are correlated. Yes, indeed, you can replace them with just one and
*  get pretty much all of the same benefits of attention. Yes, indeed, hybrid models with the
*  rough six Mamba blocks to one attention block was like a good split. Let's see other things.
*  Everyone likes to talk about model architecture, but it's one step of the three holy trinity,
*  right? So model architecture is a big one. And we really optimized that for entrance efficiency
*  and like performance per parameter, as we discussed earlier. So number two is like training
*  framework and process. So we learned from the mistakes of black Mamba of like how to affect
*  for optimizers and stability, how to tune hyperparameters for exotic model architectures.
*  We baked all those in. And then number three is data. So Zombo 1 also came out with Zyta 1,
*  which was our training data set at the time. And really getting quality baked in at scale for this
*  size of model was really important. We have some nice graphs where like at 1 trillion tokens, we're
*  able to perform similar to models trained on 5 trillion, 10 trillion, 15 trillion. If you really
*  optimize for quality at this smaller model scale, it really has effects. And kneeling was first
*  found with Zombo 1. So this process of two-phase training, we discovered it with this. So this is
*  like the first pass of everything in our overall training process. Any thoughts or anything you
*  want me to drill down on more? Yeah, I guess if we could just walk through the layers, they're
*  pretty straightforward, six Mamba layers. And then just a follow-up question on the
*  concatenation. So I guess first thing is because you're using concatenation, so you have to pay
*  for that computationally. I guess the dimension is expanding. Obviously, the trade-off's worth it if
*  you're getting a bump in performance. And then I guess at some point, it's not entirely clear.
*  At some point, I guess you're projecting back to the original dimension. So if you could just
*  step through, imagine there was a visual on the screen, step through the Zombo 1
*  architecture from beginning in. So yeah, no positional encodings. Then you have an embedding
*  block. And then you have this alternating between Mamba 1 blocks, because only Mamba 1 at the time
*  was out. So six Mamba 1 blocks, global attention plus MLP. So there's also an MLP in that global
*  block. That's important for people to know. Six Mamba 1s, attention plus MLP. Six Mamba 1s,
*  then the same attention MLP together. In terms of the concat, yes, empirically, it is better to do
*  a concat than to try and like, I think we tried to project it back down and not meet that computational
*  cost. Nothing really worked very well. So it's very empirical. So I guess in the literature,
*  there's a range of results of Mamba 2 attention layers. Zombo lands on 6 to 1. That's consistent
*  with Zombo 2. So it seems that don't fix what's already working. But some of the literature
*  suggests wide ranges up to 7 to 1, 10 to 1. How does the Zephyr team arrive at the 6 to 1 ratio?
*  Was that experimental? That was purely experimental. I also suspect that we have to apply our
*  attention block more often because it's shared. So there's some sort of interplay there. Yeah,
*  seven and five are slightly worse. That's really all it is for us. I think it's similar to everyone
*  else. Zomba, a mixture of experts, has some sort of interplay with how often you apply attention.
*  I'm sure there's some consistent rules here that are being applied to everyone. But the way it's
*  manifesting is we all are empiric. We don't have time to make these consistent rules play nicely.
*  So empirically, we find that for us, it's every six. Excellent. So I guess jumping from Zombo 1
*  to Zombo 2. So the Mamba 2 paper comes out in May. Both of the original authors published that
*  paper, Albert Gu and Tree Dao. The main result being the SSD algorithm is adding a restriction,
*  which is adding structure to the A matrix. That's the part of the algorithm that influences how the
*  state changes over time. And so now we can do matrix multiplication and take advantage of modern
*  GPUs, get those tensor cores going. So now we can train much faster and as a consequence, much larger
*  state sizes. When that paper came out, was this immediately on the minds of the team at Zephyr,
*  the kind of impact it could have? Was Zomba 2 immediately planned? And what were the features
*  of the Mamba 2, the SSD that gave your team confidence it was worth coming up with the
*  follow-up model? Yeah, after Mamba 1, we evaluated a lot of architectures at the time. And since
*  Mamba 1 gained our confidence initially, Mamba 2 was something that we immediately wanted to
*  test out. We ran a lot of ablations of pure Mamba. We found a pure Mamba 2 that is, we found,
*  okay, it has the same problems with in-context learning, long sequence dependencies. So we can't
*  just make a pure Mamba 2 model still. But we also were able to verify that we get significantly
*  higher throughput on H100s with our training hardware for no model quality degradation
*  content compared to our initial Mamba 1 tests. We also found something a little different from
*  Zomba. So Zomba 1.5, it was either 1.5 or the initial one. I don't remember which, but they
*  found Mamba 1 was better in a hybrid case. So they did like Mamba 1 plus attention. We didn't find
*  that. So we found they really performed the same. So we stuck with Mamba 2 plus attention. But yeah,
*  the Mamba 1 to Mamba 2 change from Zomba 1 to Zomba 2 is literally just throughput. So we get
*  much faster models both at training and in print time. I'm not sure if this is the best time to
*  interject, but I also, my ears perked up around no positional embeddings. And I was wondering
*  how you understand that working. Is that an artifact of the, or a sort of consequence of the
*  inherently sequential nature of the Mamba blocks that they create? Sequential understanding where
*  the transformer doesn't have it natively or the attention mechanism doesn't have it as natively?
*  That is our exact intuition. Yeah. So if you, we found that with and without them with Mamba
*  wasn't much of a performance difference for the first model. So we were just like, okay,
*  without them. For the second model, for Zomba 2, we actually put rotary positional embeddings in.
*  This is because we found there are some cases where you can make rotary help you a little bit.
*  So we kind of had to figure out how to ask the right questions. If I recall correctly,
*  rotary helps us a bit with long range dependencies, but it hurts us in terms of
*  context length extension. Rotary is very inflexible with its context length. And so that definitely
*  did bite us in the future, whether we continue with rotary, whether we get rid of embedding or
*  positional embeddings again, whether we go with some like alibi or learn positional embeddings
*  instead, I'm very uncertain with which one we do, but I will say that they're all very slight
*  effects. And this is because you correctly state that Mamba kind of handles a lot of the position,
*  like it already encodes the position. So like you don't live and die by the positional embeddings.
*  Yeah. The context extension is another thing that I think is really interesting. And that was one of
*  the biggest things that kind of inspired me about the Mamba architecture in the first place,
*  at the simplest level, the state size doesn't grow with sequence. So that means we can, in theory,
*  have an arbitrarily long sequence and have some sort of more, I don't want to say human-like,
*  but on the grand scale of possibility space of memory, at least one step toward more human-like
*  in the sense that obviously my memory, our memories are not all tokens to all tokens,
*  but rather some sort of lossy compression of everything that came before. And I wonder,
*  what would be your outlook for that now? We've been almost a year since the original Mamba paper.
*  I would say it's definitely shown itself to be a big deal, but I haven't seen like, outside of maybe
*  magic, I don't know what they're doing, but I haven't seen like many millions of tokens
*  contributing to a single long-lived state. You talk about like on-device constant,
*  continued pre-training, like learning about me, baking that into the weights. That sort of suggests
*  a disbelief in the idea that we can compress my full history into some long-lived state. So
*  what would be your outlook for training, not training necessarily, but running my whole
*  Gmail history through a Zamba 3, let's say, that, you know, that do we have a line of sight to
*  something that could handle a hundred million tokens and have this holistic fuzzy sense of
*  who I am, what I care about, how I respond to things, or does that seem just still like
*  too far to envision a path to? Yes, in terms of engineering, there's some work to be done.
*  For example, we have ring attention and tree attention for attention blocks for these million
*  plus context lengths. We don't really have that for Mamba, and this is just because the memory
*  of training time is not high enough to support million context Mamba, right? You need some sort
*  of sequence parallelism for the Mamba blocks that just doesn't exist right yet, right now,
*  and we're working on it. We hopefully will be the first. In terms of from the modeling angle,
*  one thing I'll say is that I don't really want my models to be brain to model. I forget why I'm
*  walking into a room. Like I can't reverse a string or anything else. Like the cross-sequence
*  dependencies of attention are more powerful than the way your brain works in a good way.
*  So I still want them to stick around. In terms of how model or how Mamba behaves as super long
*  context, I don't think anyone knows this. I agree that it's intuitively makes sense, but I don't
*  have a specific bet either way whether Mamba will do super well or super badly, because
*  there's something also to be said about losing cross-sequence dependencies
*  for Mamba at these really large contexts that are definitely noticeable right now,
*  and whether attention will make up for those sins at even larger scales, I don't know. We might need
*  more attention, for example, if we want a million contexts. So I want it to be there, but I think
*  there's a lot of challenges that need to be figured out first. Yeah. Yeah, I'll just pick up on one
*  detail you mentioned. Having tried to get longer sequence lengths trained into the original Mamba,
*  you reach a point, you go through all the steps that you normally would to do long sequences and
*  to save memory and then you memory out, and then the next big leap you'd have to do is figure out
*  sequence parallelism. Much less straightforward, it seems like, for the original Mamba. I actually
*  beat my head against it. I was like, okay, cool. I'll do a pull request. I think for deep speed,
*  there's the Ulysses Library. I don't know if you're familiar with it. Okay, cool. Let's get a pull
*  request going. Could not even crack 1% of what it would have taken. With Mamba 2, it seems a little
*  bit more tractable. They even mention it, I think, in the paper, that it's going to be much more
*  transformer-like. I mean, any insights to, are we going to get the same kind of sequence parallelism
*  that we're used to working with transformers? It will look similar and I don't want to say exactly
*  how because I want to be the first. I do think this has an interesting implication for hybrids,
*  though. As I was mentioning before, whether attention can make up for it, I see a mixture
*  of depths on the attention block being the best way to move forward where the model decides how
*  much attention it actually needs at inference time and also at training time. So like maybe if you
*  want a two million context of all of Nathan's emails for his entire life, then maybe the model
*  wants attention every single block. Can we also make the model decide how many LORAs or how
*  aggressive the LORAs need to be at every block? I feel like dynamic attention is what I'm getting
*  at. It's going to be a big determining factor on how long context for Mamba really will work.
*  But yeah, in terms of SP, it's unknown. It's still being figured out. Mamba 2 definitely
*  made things easier. I will say that. Excellent. Looking forward to that. Yeah,
*  no worries. I understand you wouldn't want to share details at this time.
*  For anybody who might be a little confused about the whole sequence parallelism thing,
*  can you maybe just give a little bit more intuition for the problem and how this is even
*  conceptually possible to solve? Because again, a naive understanding would be like the Mamba
*  block is sequential. So how are we ever going to get around that? Isn't it generating one
*  token at a time? And how do we change the perspective or change the frame on the
*  computation to go from the naive understanding to at least opening up the space of possibility for
*  parallelism in that respect? Sure. So like sequence parallelism is purely a necessary evil to get
*  around memory constraints. So even though Mamba is generating one token at a time, it needs to
*  store somewhere the activations and just the input sequence of a million tokens. And that is even if
*  you only require a constant hidden state, yeah, activations plus the actual input sequence are
*  just too large to fit on even an H100 at training time. Training time is even worse because you have
*  gradients and optimizer states. Those have to be in higher precision, for example. You can't fit it.
*  And if you don't train on a longer sequence length, then your model doesn't know how to
*  generalize to a longer sequence length and you have accuracy problems. So at training time,
*  though, will definitely be less sequence parallelism needed just because there's
*  less pressure on your device memory. But at training time, those are the reasons why we need
*  it. How it actually looks is the thing that like we're still cracking, but that's the reason we
*  require it. Memory, that's all. Yeah. Okay. We will stay tuned for Zamba 3.
*  Absolutely. Yeah. I guess just one last breakdown, if you could go step by step,
*  the Zamba 2 architecture, it's not just, hey, let's swap in the SSD algorithm rather than
*  the original SSM and let's call it a day. You're making these other changes. It makes sense that
*  if you're going to make the new architecture, hey, let's update a few other things.
*  If you could talk about exactly what you've updated, the LoRa modules on the MLPs and then
*  what you've done with attention and collectively all of that together. I think the highlight
*  result from the Zamba 2 release is it's sort of at this Pareto frontier of efficiency and performance
*  in certain respects against the other open models. So with your intuition, you already said it. I
*  think you had 3 trillion training tokens rather than just one. So a lot goes into this performance
*  booth, but yeah, as well as architecturally, what do you feel is giving the uplift, the most significant
*  uplift for Zamba 2? Yeah. Okay. So it's different for model. So let's start with the 1.2B, let's say.
*  So the 1.2B says there is still this global transformer block of attention plus MLP,
*  but if you only have one block, there is correlations across depth, but maybe we want
*  a little bit of more representation. So that's why we have LoRa's on both the MLP and the attention
*  block. And these do different things. So remember, attention is correlated across depth, but MLPs are
*  not. So we wanted that MLP to do a bit more heavy lifting. We thought there was still room for it
*  to specialize across depth, which is why we introduced that LoRa. I think that one does a
*  bit more heavy lifting than the attention LoRa, which is why we only have the MLP LoRa on the 2.7B
*  and the 7B Zamba 2 models. We stick with a single global block instead of the AB AB for the 1.2B,
*  just because we were parameter constrained. We thought those parameters were better used on
*  Mamba blocks. That's the 1.2B. So the 1.2B is really good if you have one specific thing you
*  want the model to do. 1.2B is enough for summarization on its own and you want it to just
*  4-bit quantize and you want it to be very low overhead on any Raspberry Pi or Jetson Nano in
*  the world. The 2.7B has this AB AB, so there's two global blocks. Only the LoRa is on the MLP,
*  for the reason I mentioned, but it specializes more across depth. And we wanted to kind of,
*  like for a very small overhead and flops and params, we could get a bit more expressivity.
*  That was also when we put in the rotary, the positional encodings. That was just because we
*  got like the slight boost, like I was mentioning, along context, whether it was a mistake or not in
*  terms of context, like extension is still to be determined. That was the main change though for
*  the 2.7B and then the 7B is the exact same architecture as the 2.7B. So we just scaled that
*  one up. But the main differences from Zamba 1 to Zamba 2, if I were to summarize it, is that we
*  were trying to really investigate the depth relationship with the shared block and try and
*  find out how much do you want the model to be able to be flexible across depth? What is actually
*  being flexible as an MLP or the attention? And then the other two pillars of our training stack,
*  right? Like our data, we improved a lot and then scaled it way up. So we doubled the size of our
*  annealing set. We tripled the size of our phase one. This helps the model like be more broad in
*  what it's good at. So the first model was a bit brittle in terms of what the trunk I was talking
*  about was not super wide. But on 3 trillion tokens, we can anneal and fine tune the model to be much
*  more flexible across a lot of different tasks that our customers and partners wanted. Just because
*  it's seen more data. You can look at this actually in the weights themselves. If you look at the Lama
*  3 weights, you can see they're much more evenly distributed across the representation. You've
*  filled out that weight more and you can see it. And going from 1 trillion to 3 trillion,
*  we were able to get most of the way there as well. The model is much more flexible.
*  But yeah, just improving end to end the stack of our model production. But with a focus on depth
*  was the Zamba 1 to Zamba 2. Yeah. And I think you mentioned on the first read of the blog post,
*  I didn't see the state size of the Mamba blocks and Zamba 2.
*  Mm hmm. 64. So yeah, all of those details are in our hiding face.
*  Excellent. Okay. Yeah. I didn't check out the model card yet. So 64, that's interesting. So
*  you could have trained larger state sizes, of course, inference efficiency being governed by
*  state size. Could you talk through experimentally how your team landed at 64? And is it actually a
*  little bit lower than my expectation because the attention blocks are doing so much heavy lifting,
*  there's less pressure for the state size to be larger for the sake of memory.
*  This is pretty much right. So if I recall larger state sizes is mostly for improving your long
*  context ability. You can more accurately store longer range states and we have attention. So
*  it's a less clear benefit for us when we try to increase it. We've tested this, but it's a very
*  clear damage at inference time. So 64 we found was enough for our Zamba based models. Yeah,
*  just empirically and this intuitively makes sense for the reasons I just mentioned.
*  Yeah. Fascinating. That makes total sense. I guess if we could just go deep on,
*  I haven't seen that many papers or architectures where we're applying lower projectors to MLP blocks.
*  It intuitively makes sense that, wow, okay, a really certainly memory efficient way,
*  because you're not storing a whole nother set of weights to add some specialization into the
*  MLP blocks. It's sort of like, is an alignment with that sort of performance per parameter idea.
*  I guess if you could just talk about that idea, what you've seen in the ablations or the
*  experiments you've run, it's a very interesting feature. Yeah, it's going to boil down to what I
*  was mentioning earlier of like the MLP specifically definitely are not correlated across depth very
*  strongly. So this even boils down to what we've learned with CNNs where like the first few layers
*  learn very general representations and then the deeper layers learn more specific representations
*  in the CNN world. This is a face, this face is a child, this child is crying. You get more and more
*  abstract and specific as you go deeper. And in the language world, this is all manifested in the
*  MLPs. So it's important that the MLPs learn the same notes, textualize themselves across depth. So
*  that's why attention is learning that anyway. Oh, remind the MLPs that these are all the notes that
*  we have across all tokens of the sequence. But those MLPs are like learning different deep
*  relationships across depth. But all of us to say that is the intuitive reason why we have MLPs
*  or why the MLP that we were carrying around anyway in this shared block should probably have
*  some expressivity across depth. And Allora is a good way to get some of that expression,
*  but with lower memory and compute costs, which is really what we want. If I was
*  not bound by memory and compute, then I would just probably have independent MLPs and a shared
*  attention. But this is a good middle ground and then empirically, it improved accuracy across depth.
*  So we stuck with it. And is it the kind of thing where you also ran the experiment with
*  independent MLPs or you just know that's not feasible for the constraints you want for the
*  Zamba model so you don't even bother running that ablation? Yeah. Unfortunately, that's just not on
*  the table. That model is not in the cards for us. So I would hope someone does it. But yeah,
*  ideally, I'm sure we would get some pretty big boosts from doing that. And if I had more
*  parameter budget, I would go to full MLPs. Yeah. Yeah, makes sense. But the specific
*  ablation of no MLP Laura to MLP Laura is worth the jump in params and flops for sure in terms of loss.
*  Very good. Interesting. I guess a little bit more of a general question is if you read the literature,
*  it seems like almost every time someone tries some type of Mamba attention hybrid,
*  it's like this unreasonable effectiveness, at least across the metrics that they're
*  measuring. We talked about how loss can be misleading. That's not always a measure of how
*  well that model will actually perform. But it maybe tells you at least something. And then
*  you can go down the list. You can look at other evaluations. It's not surprising to see that a
*  hybrid Mamba hybrid model would beat Mamba by itself. If you think about the limitations
*  of a fixed state size, the way information would propagate through that network. But it's always
*  surprising to me when I see all other factors held equal, that it's beating something that's
*  like a full transform or full attention blocks. Do you have any insight around that? How these
*  like dynamics are playing together? Almost like maybe it's greater than the sum of its parts.
*  I really think it's powerful when you're doing hybrids to boil down, to almost apply like
*  qualitative, like track qualitative differences in how well your model is encoding cross sequence
*  dependencies and projecting them to mix heads and to find deeper relationships from those notes of
*  the cross sequence dependencies. Like Mamba does both. MLP just does taking the notes and
*  finding deeper relationships like when they're projecting onto some abstract feature space.
*  And then attention is just finding the dependencies themselves and not doing much
*  else with them. At least in terms of how we approach things at Cypher, it's really just
*  boiling down to this critical intuition of things. And for example, that's how we can explain why
*  black Mamba had struggled with the long sequence because Mamba notes on themselves about sequence
*  dependencies are not rich enough. So you need some attention. The unreasonable effectiveness comes
*  from reaching like the critical point of where everything is balanced, where you are not spending
*  all of your flops in memory and everything on taking notes and then doing nothing with them,
*  like the tiny MLPs or something and big attentions. It's not with like a weaker cross sequence
*  relationship from Mamba and then big MLP projections where you're like trying to find really deep
*  things about very minimal notes. I really just, if you find a balance of these two, that's when you
*  get really strong model architectures. And eventually I think we'll probably converge to
*  a better way to do both where maybe we boil down attention to maybe you can have a retrieval head
*  on a Mamba block, whatever that may look like to help you patch the problem with long sequence
*  dependencies. Maybe there's some unified block that finds the exact mixture of projections and
*  note-taking across cross-sequence dependencies. And you just scale it up and you're done.
*  That seems to be the case, right? Based on this intuition that you just need a balance. But yeah,
*  I would still tie it back to you need balance between these two effects and these two effects
*  are what you need for language modeling. It differs per modality. Yeah, very interesting.
*  Do you get the sense, Nathan alluded to this, we see several iterations of Mamba hybrids
*  out there, but at the same time, it seems like people are like, there's some lock-in maybe
*  of even some of the private labs. Are there lock-in effects once you commit to a certain
*  type of architecture where even though something begins to be promising, you almost ignore it
*  purposefully to some degree just because you've invested so many resources in a particular path
*  and do those lock-in effects make it more unlikely that a lab that's been committed to
*  a completely different tech tree for years is going to just jump ship and start
*  or those lock-in effects there. The lock-in effects are stronger here than in most places.
*  One thing is that as your lab continues, you have more and more ablations that you can look back on.
*  And when you jump ship to a new architecture, all of those ablations, you have to retake a bunch of
*  stuff, right? Another thing is that we were talking about evaluations. It's really hard to evaluate
*  specific tasks on very few tokens, meaning that, for example, if you have two architectures,
*  how are you going to test how well they do on MMLU, on in-context learning? You have to train
*  for hundreds of billions of tokens, remember? And I can't just take a pre-trained checkpoint and then
*  test both architectures because you have to train these architectures from scratch. So to predict
*  how well a model is going to do on those emergent evaluations is a real leap of faith on new
*  architectures that a lot of people in labs just don't want to do. Like I mentioned, Lama CPP and
*  the OLAMA, the whole hacker space and every serving framework is built around transformers.
*  It's slowly changing to support hybrids and SSMs and such, but do I really want to relearn fine
*  tuning? Do I really want to relearn efficient CPU inference or what efficient set of fused kernels
*  will work at inference time? Do I really want to get it in VLM and TensorRT? We're going through
*  that pain, but I can definitely see why a big company with even more technical debt and more
*  ablations and interpretability is another one. Big labs have really finely honed and interpreted,
*  especially at somewhere like Entropic or OpenAI, they can interpret really well what these models
*  are doing out of the hood, way beyond my intuitions that I have right now. And if you jump into a new
*  model architecture, you start from scratch with all of that. In some cases, I'm sure there's some,
*  an attention block might act similarly when it's in a hybrid versus when it's in a dense transformer,
*  but there's still a lot of resistance there to the new idea. But yeah, totally in agreement with
*  your point, these are all the examples of why I would probably myself not want to jump into hybrids
*  right away if I was big tech or if I had a big existing presence in dense transformers. But yeah,
*  there's a reason that they're moving slowly. Yeah, that makes sense. In that way, do you see
*  so the lock-in effects are a way in which you commit, but then obviously the longer you commit,
*  you're beginning to build out not just code, but best practice where if you could imagine
*  the possibility of Zyphera developing this architecture over the next five plus years or
*  longer, what kinds of, so I guess the positive side of lock-in effects is that you get really good
*  at managing this architecture that maybe not that many others are managing. Do any insights
*  is what that could look like for you and Zyphera and the hybrid world? There's some first mover
*  advantage here where we can kind of steer the story. We have internal inferencing frameworks
*  that we've already ported that if you want a Zamba model, we can run it for you and with you the
*  fastest compared to everyone else. If you want like community engagement, this is a negative.
*  I think we're nimble enough to avoid the pitfalls of being locked in. So we have some very non-Zamba
*  architectures that are cooking right now. As long as they are efficient on device and punch away
*  above their weight, we're going to look at whatever the architecture is and we're going to try and
*  find creative ways to make it train well. In terms of avoiding lock-in with that, it really just comes
*  down to effort of you need to figure out fine tuning again. You need to figure out sequence
*  parallelism for every new architecture you make and this kind of thing. And putting the effort in
*  is our way forward. We don't have any super crazy intuition behind. You just have to grind it out.
*  Nice. Yeah, that makes sense. I guess related to that is, and this might be part speculation,
*  so I apologize for that, but it seems like you do have some real world data given that
*  Zephyr is developing not just one flagship Mamba hybrid model, but like
*  various parameter counts, various sizes. Any sense in which you're getting sense of like
*  the scaling properties of this kind of model architecture, how those scaling properties
*  are changing? You have chinchilla scaling laws. We know what it looks like for just
*  base transformers. Do you have any sense of what the scaling laws could look like for the Mamba
*  hybrid models? Are they even that much different than what we've seen in transformers?
*  I think they're pretty similar. We just have a slightly better slope for a lot of these. I
*  would say I'm curious to see how shared blocks affect chinchilla because we reach chinchilla
*  optimality way faster on the shared blocks. So if we train for 15 trillion tokens, at what point
*  does the attention block saturate? It's kind of a similar thing to like, no one I don't think is
*  really correct scaling laws for MOEs. You can think of MOEs as a similar case where some blocks are
*  getting trained more than others. I really don't see any reason why a Zamba architecture wouldn't
*  scale well to 20B, 40B, 70B, and I think we at some point will try this ourselves to get distillation
*  in-house. Those are my only hot takes. I think they'll look pretty similar. It's a little bit
*  better. That's awesome. This is maybe a big picture question. What does it take to do foundational
*  ML research? In particular, what is the kind of approach you and your team have? Because
*  Zephyr seems fairly interesting. It's a company, but it also seems to be a lab doing what I would
*  consider pretty clearly research. So it's not necessarily product focused solely, but there's
*  some in commercial goals. What is the process? Is it a lot of open-ended search in the team,
*  or there's always specific objectives with the commercial interests in mind?
*  We have research guided by specific objectives. So those objectives are efficient inference is one.
*  So you get a big first movers advantage if you come up with a novel architecture that actually
*  runs efficiently on device, because now everyone else either has to use your model or figure out
*  all of the arcane knobs that you had to turn to get your model to work. We're sort of an applied
*  research lab. We're not like making Mamba 3, right? We see all of the available blocks and training
*  processes and lores. Every element of this Zamba model is built by someone else. But in order to
*  recognize what all of those knobs do, and then to turn them in a way that you get the same modeling
*  performance as a dense transformer, but with a much more amenable on-device performance,
*  and even cloud performance, is the research that we're doing. So how do you take everyone else's
*  work and how do you put it together in a way that's perfect at inference time?
*  And then this ties into the product story of if you have that inference efficient and training
*  efficient model, it's way easier. It is now achievable to make it personalized to everybody.
*  It's achievable to put it on a phone. It's achievable to personalize it to enterprise
*  applications and these sort of things. It's definitely guided by products.
*  Yeah, that makes sense. And this is just a side question. When I think about the
*  properties that Lamba has, but in particular these hybrid models, and
*  increasing interest in robotics, I feel like that could be the next big market. It's not really a
*  market right now. And what you need to run models locally, that just ties in almost directly with
*  what your lab is focusing on. In any sense, obviously, robotics usually involves a completely
*  different stack of data. So it's multimodal. You have things like the act transformer. It'd
*  be interesting to know what that would look like for Mamba. If you were to apply your work, which
*  is primarily focused on NLP, how big of a jump is it to now be looking at the robotics
*  technical use cases? Or is that a bigger jump than what I'm thinking in my head?
*  Do you all ever think about things like that? Oh, definitely. So robotics, gaming, there's all
*  kinds of markets where it's really nice to have flexible models on device. For robotics specifically
*  to make, if it's just chat with humans and maybe ability to do visual question answering about
*  how to recognize and respond what the robot is seeing and speaking, that's pretty easy.
*  That's pretty achievable. And I think we probably have the best offering for that right now. Once
*  we get voice to voice done, then yeah, a robot walking around that can talk to you and is totally
*  on devices is like nothing for us. What else would be required? It would all be very low power
*  as well. So you could get it running on a Raspberry Pi or a Jetson. I think there's a lot of cases
*  with smart cities, where you could put this on a Tesla and you can put it in a self-driving car and
*  just have a chat interface. Run the windshields, speed them up, run the windshields at the speed
*  that I like. All these sort of things become possible when you have a model architecture
*  like Zamba that's multimodal and voice to voice. And that's why we're pushing for it so hard.
*  Yeah, that's awesome. I guess just one more practical question is oftentimes really,
*  if you look at the adoption of models, it often comes down to just how easy are they to use?
*  And that often involves how compatible are they with the Transformers library from Hugging Face?
*  But I guess if you could just talk about that. If I wanted to do some really interesting
*  experiments with Zamba 2 right now, or I wanted to, whether that was fine-tunes, whether that was
*  some extended pre-training stuff, or how easy it is to use, what do I actually do?
*  What libraries do I need to get into to use Zamba?
*  So right now, you're restricted to Hugging Face Transformers. So we have Zamba 1 has been
*  upstreamed now. It's in Transformer. You can use it with all Accelerate and Paft and all of the
*  Hugging Face class frameworks. For Zamba 2, we have our own fork of Transformers. It's currently
*  getting upstreamed, but there's always just a lot of compatibility work with this kind of stuff.
*  You can get basic functionality right away, which is why we have our own fork. But getting it
*  really solidly ingrained in the entire Hugging Face ecosystem is the hard leg of the journey
*  that we're still working on. We also have a pure PyTorch implementation for both Zamba 1 and Zamba
*  2. So people have their own custom pipelines. They want to pour it to their own internal
*  inference framework. We tend to find people like that a lot. It's also more performant than putting
*  it in the Hugging Face ecosystem to just have pure PyTorch. You can compile it with Torch Compile.
*  You can create custom Triton kernels very easily. Going forward, I think we're about to finally
*  become more ingrained because we're about ready to crack GtML and LamaCPP and O-Lama and that
*  entire ecosystem. We've pretty much finished porting Zamba 2. I struggle to put a date on it.
*  I don't want to miss a date, but in the next couple of weeks, I think people will be able
*  to use this seamlessly with VLM, O-Lama, LamaCPP, GtML, the entire ecosystem. I think we're right
*  about to jump onto. Very interesting. So the choice to fork Transformers simply, we'd like
*  people to be able to use it immediately and there's still some kinks to work out to get it
*  integrated. That's essentially it, right? Yeah. We understand that people will bulk when they see,
*  oh, it's a fork? Done. I'm not jumping into it. We've produced the best model at the weight class,
*  so there's definitely incentive for those who want to use it. You got to use the fork,
*  but for all of those who are more focused on what is the fastest way to get this running on my
*  laptop or something, you will very soon be able to actually do that very soon. But currently,
*  plug your face fork or a pure PyTorch are your options.
*  And you said that like, what would be the most performant both for inference and for,
*  let's say I wanted to like do fine tuning or training. If I use one of those training frameworks,
*  is it fully optimized or are there some trade-offs with having to make sacrifices with getting
*  compatibility or should I go straight to PyTorch or could I use those frameworks?
*  It's not going to come with costs. Yeah. So for small scale, by small scale,
*  I mean like fine tunes. So if you're at the pre-training scale, you've got to have your own
*  thing. You've got to have your own GPT-NEOX or Megatron Deep Speed or Megatron LM. You've got
*  to have a pre-training framework and those are not super Mamba friendly right now.
*  Our stuff is in-house unfortunately right now, just name of the game,
*  how people watch your PRs otherwise. In terms of fine tuning, at the fine tuning scale,
*  Hug and Face is totally fine. We even use Hug and Face internally to do some of our fine tunes,
*  some of our context length extensions. When you're working on a couple billion tokens,
*  10 billion below, 50 billion below, Hug and Face is totally fine. And we recommend people use that.
*  So yeah, if I had like a mid-range kind of thing, maybe I would try to wrap the PyTorch
*  implementation of Zamba in some simple data loader and just try and get that going. If I have maybe
*  50 billion or something, 50 to 100 billion in range, but I think most people fall into
*  the fine tuning range where Hug and Face suffices. Very good. Makes sense. Excellent.
*  And if people today, like right now, wanted to start experimenting fine tuning, I believe
*  there's a GitHub linked to the blog there. I can access the fork of the Transformers library.
*  If someone was motivated, they could spin something up today. Is that correct?
*  Oh yeah, definitely. Yeah. It's not hard to fork and to just build our fork and load our checkpoint.
*  Yeah. And then if you just want to talk to the model, then we had a day zero release with
*  Nvidia as a NIM, as an inference microservice. We self-hosted it on the Maya endpoint on our
*  website. So if you just want to talk to the model, use one of those. If you want to spin it up,
*  you can do it today with our fork. Excellent. So I guess we've been talking a lot about
*  Mamba and the Zamba models, but Zyfrb also published a very interesting paper recently,
*  the Tree Attention paper, and we've barely talked about it. I've not been able to dedicate myself
*  to a complete deep dive, but my high level view is it's very interesting in the sense that it
*  seems to be in some aspects improving upon Ring Attention, which was the huge thing earlier this
*  year where it seemed like everyone was training million plus context length Lama models. If you
*  could just talk about Tree Attention, how is it different from Ring Attention and then what impact
*  can it have? What is it really pushing on? Sure. So Ring Attention is good when you have a network
*  topology that's a bit more flat. So like a mesh topology, like with TPUs and stuff, I think is
*  what it was designed more for. And that's because you have a ring with point to point across each
*  GPU in the ring. If you're in GPU land, you have two level topologies where on a single node,
*  you have MD-Link that connects all of your GPUs is really high bandwidth. But across nodes,
*  you have a much slower InfiniBand or maybe you have a Rocky, like a converged ethernet thing.
*  That's an order of magnitude lower bandwidth than the Intranode interconnect. So there's a reason
*  why they only did up to two nodes in the original Ring Attention paper. And it's because you're
*  bottlenecked by this cross node link. So the boundary GPUs at the cross node are going to be
*  dictating how quick your infant speed is. And it's not great. As you scale up to more and more
*  nodes, it becomes worse and worse. If you have smaller PV states, then you're going to be,
*  the compute is not enough to overlap that expensive communication. So it's not scalable.
*  The whole point of tree attention is to recognize this fact that two level topologies are not good
*  for rings and to reformulate the distributed attention operation as an energy function,
*  which allows you to use all reduce operations, communication operations instead of point to
*  point. All reduce operations in existing communication libraries, Nvidia's communication
*  library called Nickel, Nvidia Collective Communication Library, AMD has something like
*  RICL, the Rockham Communication Library. All reduces themselves are topology aware for GPU
*  clusters. So they account for this two level topology. And they also add some of the computation
*  is like in network. So with an all reduce operation, you can do some of the sum in the network
*  card and you can overlap that some computation, that kernel, be it on the GPU or on the card,
*  if you're doing sharp with the communication of those PV States. So basically it can scale
*  in short, it can scale on two level topologies because you're reformulating to an all reduce,
*  which is inherently topology aware and adds some of the compute is easier to overlap
*  versus point to point operations, which are restricted and sort of assume a flat topology
*  of network. So I guess if you could help me, maybe let's begin with the end in mind. Like
*  what will that enable me to do that ring attention which struggle with what in what cases will tree
*  attention help me? So this all boils down to parallelism. Whenever you have parallelism,
*  it boils down to memory. GPUs have a limited memory. If you have long context, so say if I
*  want to do a million context on a llama eight B or if I need a lot of parameters that I need to
*  store in memory at inference time, then I need more GPUs for both of those cases. I mentioned
*  super long context of super large models. You need lots of GPUs to fit more GPUs than are on a node.
*  So you're going to two nodes, four nodes, et cetera. When you're going across nodes,
*  you have a two level topology and all reduces work better. So if you wanted a 16 node like
*  context extension training run with like 2 million context tree attention will work much better.
*  If you have an inference run of llama four or five B on older GPUs, you need four nodes or two nodes,
*  tree attention will scale much better on that. Anytime you're scaling across nodes for GPU
*  clusters or any imbalance of communication costs, tree attention will win.
*  Soterios Johnson Interesting. Okay. So this is not necessarily
*  something where we had ring attention and all of a sudden everyone's just going to implement tree
*  attention. It's on a case by case basis of which one you might use if you were to try to do multi
*  node training and distribute the memory. Kevin Kwan Yeah. So there are cases where like
*  if you perfectly have enough compute in your communication costs, like those who perfectly
*  overlap one another and it's effectively free and you're on a single note, ring attention is
*  pretty good. Even though all reduces are really closely optimized because they're used in training
*  so much, you can't really do much better than that. In free communication, it's totally overlapped.
*  Yeah. Not everyone will benefit right away, but those cases where you have a smaller model,
*  longer context, which translates like smaller KV states, that means you're going to be communication
*  bottlenecked. There's not much compute to hide the communication. So those people will benefit
*  from us and then the people with really large models that are inherently across the nodes will
*  benefit from us. Yeah. But yeah, you're right. It's not every single case.
*  Soterios Johnson Not every single case. For like a very, very long training on very,
*  very long sequences, it would help for that. And that was only if it was a multi node training setup
*  or it doesn't come into play. Kevin Kwan It would help more. It would help more.
*  Even on a single node, all reduces are a little bit more effective than point to point, just because
*  tuning libraries or like collective libraries today are really closely tuned for that specific
*  operation. Like we're kind of exploiting the fact that all reduces really good than point to point,
*  because you don't really use point to point much in training unless you're doing like pipeline
*  parallelism, which is less common than tensor parallelism or data parallelism, which are both
*  all reduced. So yeah, again, it'll help you a lot more at scale. It might help you a little bit at
*  smaller scales, but I wouldn't promise big speed ups. Soterios Johnson Okay. No, that's very
*  interesting. I guess just because we hit that topic, I haven't thought of another question.
*  The Zamba one, I believe was natively trained with, I think, if I'm reading this correctly, 4096
*  token context length. Did Zamba to train in the same native token context length or is that higher?
*  Yeah. Yeah. And then we were able to extend to the 16k range for free just by interpolating
*  rotaries, positional embeddings. Getting beyond that is an open question that we're still working
*  on. So I think we have a path now for 64k and 100k, which should be coming out soon, especially for
*  the smaller models. Because remember, I mentioned that it's a memory overhead thing at the end of
*  the day, right? So like Zamba 2.7b, we can go to way longer context than this. But just the engineering
*  challenges to get us to a million context, still working on that. But yeah, trained on 4k.
*  Soterios Johnson Yeah. So I guess just because it's something I've experimented with Mamba one,
*  like really basically the idea of, okay, we're natively trained at even 2000 token context length,
*  but I want something capable of much more. So I'm just going to do continuous pre-training.
*  And now all of a sudden my data distribution, if you want to do it smart, maybe there's a curriculum
*  learning approach where you don't just throw that much more context length at the training
*  at once. So you want to do it smart, but it seems there are all these papers and my own
*  experimentation is it works pretty well to do continuous pre-training to expand context length.
*  To what extent is that a solution? If somebody wanted to grab, let's say the Zamba model, or
*  we even see this with some of the, just to transform our Lamba models. Do you have any
*  thoughts on continuous pre-training to extend context length? Is that sort of like a hack
*  that you're just not going to get the quality that a natively trained model would have?
*  No, you can get the quality. That's what we're doing ourselves. So yeah, definitely
*  continue pre-training. You definitely need to do a curriculum of where you're warming up the
*  sequence length and batch size across your continuous pre-training run. But eventually
*  you're going to hit a memory wall. And then that's really, that's all I'm trying to say here is that
*  you got to finish up sequence parallelism for the mama blocks as well, if you want to get past that
*  memory wall, but it totally works. Yeah, absolutely. So playing around with the 2.8 billion parameter
*  model, I could never figure out sequence parallelism. I use the deep speed library
*  because it just makes it easy to do all the zero three stuff. Of course you have to pay
*  tremendous costs with training efficiency when you start offloading everything to CPU memory or
*  yeah. So sequence parallelism is the big unlock. That's going to be exciting.
*  Okay. Cool. Does Zypher have plans to open source that once that gets cracked?
*  Sequence parallelism for Mamba will definitely be open sourced. The Zypher specific training
*  stack that we're using to produce the Mamba will probably not be open source, but the general
*  process and like what we did with tree attention, the kernels that we use, the scripts that we use,
*  those will all be open source because we want the community to like move towards Mamba and see that
*  there's something there. Yeah. Awesome. Great to hear. Anything else that we didn't cover
*  about Zamba? The timing is in around the Zamba to release. Anything else you think we should
*  cover before we wrap? No, I think we've covered pretty much everything. Appreciate your time,
*  Quinn. It's absolutely great speaking with you. Likewise. So let's do this zoomed out one. I think
*  this has been fantastic. I think that this is for the real ones out there who are very interested
*  in learning more about what it actually takes to make these models work and just how many little
*  nitty gritty details go into that. So I've learned from this. I think a lot of people will appreciate
*  all of the lessons that you've shared from many long days and probably some long nights working
*  on this stuff. I think it's been great. Let's do the zoomed out thing with all that in mind.
*  Where is Zypher going as a company? What role do you guys want to play in the lives of users?
*  You talked a little bit about how you see yourselves competitively against the big guys,
*  but I'd love to hear on whatever time scale what you think my AI assisted life is going to look
*  like and what role Zypher and Zypher models will play in that. Yeah, definitely. We've focused really
*  hard on producing the best models for one modality and now we're ready to expand out. So this includes
*  other modalities. So we want visual question answering. I want to be able to live edit my
*  pictures. I want to be able to talk voice to voice. I talk to you voice to voice. I want to talk to
*  my AI voice to voice as well. This includes actually deploying personalizability to people.
*  This includes actually launching both enterprise and on device for consumers. This includes
*  the broader ecosystem, for example, Olama and Lama CPP and stuff. Those are all transformer based
*  and getting the hybrid architectures into those is one of our next priorities so that everyone
*  can actually deploy the model really quickly instead of using our fork of hugging face and
*  all this sort of thing and having a much more like a better user experience for hackers and
*  for consumers. And then there's some also just some higher level things we think like memory.
*  So retrieval is really important for personalizability that we're going to like how
*  does retrieval interplay with long context reinforcement learning so that like we can
*  really tie down. It's not just continual pre-training when you're following. Like
*  we definitely need some sort of approximation at least of RLHF or RLAIF for users so that we can
*  really extract as much as possible from the little data that we're going to get per user.
*  There's a lot of ways to expand, but those are some of the main ones.
*  Cool. I love it. For now, I'll say Jason Moe and Quentin Anthony from Zyfra. Thank you both for
*  being part of the cognitive revolution. Thanks, Hasan. Thanks.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the
*  show. So please don't hesitate to reach out via email at tcr at turpentine.co
*  or you can DM me on the social media platform of your choice.

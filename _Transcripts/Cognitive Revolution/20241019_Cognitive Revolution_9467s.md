---
Date Generated: October 22, 2024
Transcription Model: whisper medium 20231117
Length: 9467s
Video Keywords: []
Video Views: 501
Video Rating: None
Video Description: Join Nathan for an expansive conversation with Dan Hendrycks, Executive Director of the Center for AI Safety and Advisor to Elon Musk's XAI. In this episode of The Cognitive Revolution, we explore Dan's groundbreaking work in AI safety and alignment, from his early contributions to activation functions to his recent projects on AI robustness and governance. Discover insights on representation engineering, circuit breakers, and tamper-resistant training, as well as Dan's perspectives on AI's impact on society and the future of intelligence. Don't miss this in-depth discussion with one of the most influential figures in AI research and safety.

Check out some of Dan's research papers:
MMLU: https://arxiv.org/abs/2009.03300
GELU: https://arxiv.org/abs/1606.08415
Machiavelli Benchmark: https://arxiv.org/abs/2304.03279
Circuit Breakers: https://arxiv.org/abs/2406.04313
Tamper Resistant Safeguards: https://arxiv.org/abs/2408.00761
Statement on AI Risk: https://www.safe.ai/work/statement-on-ai-risk

Apply to join over 400 Founders and Execs in the Turpentine Network: https://www.turpentinenetwork.co/

SPONSORS:
Weights & Biases RAG++: Advanced training for building production-ready RAG applications. Learn from experts to overcome LLM challenges, evaluate systematically, and integrate advanced features. Includes free Cohere credits. Visit https://wandb.me/cr to start the RAG++ course today.

Shopify: Shopify is the world's leading e-commerce platform, offering a market-leading checkout system and exclusive AI apps like Quikly. Nobody does selling better than Shopify. Get a $1 per month trial at https://shopify.com/cognitive.

LMNT: LMNT is a zero-sugar electrolyte drink mix that's redefining hydration and performance. Ideal for those who fast or anyone looking to optimize their electrolyte intake. Support the show and get a free sample pack with any purchase at https://drinklmnt.com/tcr.

Notion: Notion offers powerful workflow and automation templates, perfect for streamlining processes and laying the groundwork for AI-driven automation. With Notion AI, you can search across thousands of documents from various platforms, generating highly relevant analysis and content tailored just for you - try it for free at https://notion.com/cognitiverevolution

Oracle: Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

CHAPTERS:
(00:00:00) Teaser
(00:00:48) About the Show
(00:01:11) Sponsors: Weights & Biases RAG++
(00:02:17) About the Episode
(00:05:41) Intro
(00:07:19) GELU Activation Function
(00:10:48) Signal Filtering
(00:12:46) Scaling Maximalism
(00:19:07) Sponsors: Shopify | LMNT
(00:22:03) New Architectures
(00:25:41) AI as Complex System
(00:32:35) The Machiavellian Benchmark
(00:34:42) Sponsors: Notion | Oracle
(00:37:20) Understanding MMLU Scores
(00:45:23) Reasoning in Language Models
(00:49:18) Multimodal Reasoning
(00:54:53) World Modeling and Sora
(00:57:07) Arc Benchmark and Hypothesis
(01:01:06) Humanity's Last Exam
(01:08:46) Benchmarks and AI Ethics
(01:13:28) Robustness and Jailbreaking
(01:18:36) Representation Engineering
(01:30:08) Convergence of Approaches
(01:34:18) Circuit Breakers
(01:37:52) Tamper Resistance
(01:49:10) Interpretability vs. Robustness
(01:53:53) Open Source and AI Safety
(01:58:16) Computational Irreducibility
(02:06:28) Neglected Approaches
(02:12:47) Truth Maxing and XAI
(02:19:59) AI-Powered Forecasting
(02:24:53) Chip Bans and Geopolitics
(02:33:30) Working at CAIS
(02:35:03) Extinction Risk Statement
(02:37:24) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# GELU, MMLU, & X-Risk Defense in Depth, with the Great Dan Hendrycks
**Cognitive Revolution:** [October 19, 2024](https://www.youtube.com/watch?v=1fyqkH6hXJw)
*  The idea was that a lot of the linguistic understanding benchmarks were not being sufficiently difficult.
*  Elon's description of it is basically like an undergraduate level knowledge and skill test.
*  There's a benchmark we call Machiavelli, which is largely assessing the propensities of LLM agents.
*  See what sort of decisions do they make along the way?
*  Do they screw people over or are they generally nice?
*  Do they lie a lot?
*  There is something going on in making AI systems a lot more reliable to jailbreaking due to specific algorithmic advances that do not necessarily follow from just scaling the model.
*  If they get expert level virologists, I don't know if I want that being released.
*  Sorry to say because you'll run some substantial risks of bio weapons.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers, entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture of how AI technology will transform work, life and society in the coming years.
*  I'm Nathan LeBenz, joined by my co-host Eric Thornburg.
*  As a developer, the journey from concept to production ready large language model apps is fraught with challenges.
*  Dealing with unpredictable language model outputs, hallucinations and ballooning API costs can all be blockers to shipping your next AI powered feature.
*  That's where Advanced RAG comes in.
*  With the new RAG++ course from Weaviate and Viases, you can overcome these hurdles and build reliable production ready RAG applications.
*  Go beyond proof of concept and learn how to evaluate systematically.
*  Use hybrid search correctly and give your RAG system access to tool calling.
*  Based on 21 months of running a customer support bot in production, industry experts at Weaviate and Viases, Coheer and Weaviate show you how to get to a deployment grade RAG application.
*  This offer includes free credits from Coheer to get you started.
*  Make real progress on your large language model development and visit wnb.me.cr to get started with their RAG++ course today.
*  That's wnb.me.cr to get started with their RAG++ course today.
*  Hello and welcome back to the Cognitive Revolution.
*  Today I am thrilled to be joined by Dan Hendricks, Executive Director of the Center for AI Safety,
*  advisor to Elon Musk's XAI, and one of the most prolific and influential researchers in AI safety and alignment, Full Stop.
*  While Dan has recently become famous in AI circles for his work developing and advocating for SB 1047,
*  I wanted to use this conversation to highlight what an all-purpose AI powerhouse Dan truly is,
*  and to get his perspective on a number of questions that I've personally been thinking a lot about.
*  And so this is a long episode in which we cover a tremendous amount of ground,
*  including his early work on activation functions such as the widely used Jell-U function,
*  which he developed as an undergrad, and his work on benchmarks, including the insights that allowed him to create,
*  in MMLU and math, some of the longest lived and most often cited benchmarks in existence today,
*  as well as what he's up to next with a project called Humanities Last Exam.
*  We also cover his work on AI robustness and alignment, including early work on robustness in image classifiers,
*  which showed how difficult robustness can be to achieve, his 2023 paper introducing representation engineering,
*  a top-down alternative to mechanistic interpretability, which can be used to identify directions in light and space for both monitoring and steering purposes,
*  his 2024 paper with past guests Andy Zhao and Zico Kolter on circuit breakers,
*  which build refusal behaviors more deeply into LLM weights through a specialized fine-tuning process,
*  and most recently his work on tamper-resistant training, which aims to make it difficult for
*  users of open source models to remove refusal behaviors via fine-tuning, and which suggests that it
*  might become possible for companies like Meta to open source models with durable guardrails built in.
*  We also touch on a number of big picture issues around AI governance and the geopolitics of AI development,
*  philosophical questions about the nature of intelligence and consciousness, and sociological
*  questions about how AI might help us better forecast future events and generally improve our collective epistemics.
*  We even get a fascinating behind-the-scenes look at how he orchestrated the 2023 AI X-Risk Statement,
*  which was signed by a remarkable set of industry leaders, including the CEOs of DeepMind,
*  Anthropic, and yes, Sam Altman of OpenAI, and which said in full that, quote,
*  mitigating the risk of extinction from AI should be a global priority alongside other societal scale risks,
*  such as pandemics and nuclear war. I think what struck me most about this conversation was that,
*  despite all his experience and success, Dan's approach remains fundamentally experimental
*  and his outlook very empirical. He places far more weight on data and compute than on algorithmic
*  insights as drivers of capabilities advances, and he remains very open-minded both about how far the
*  current AI paradigm will go and about whether any of the safety approaches we're developing will
*  really work when the chips are down. Ultimately, as you'll hear, that leads him to believe that we
*  would be well-served to adopt a defense-in-depth strategy. As always, if you're finding value in
*  the show, we appreciate it when folks take a moment to share it with friends or write an online
*  review on Apple Podcasts or Spotify, and we welcome your feedback via our website, cognitiverevolution.ai,
*  or by DMing me on your favorite social network. Now, I hope you enjoyed this expansive
*  discussion with one of the most impactful figures in AI safety and alignment. This is the great
*  Dan Hendricks. Dan Hendricks, executive director of the Center for AI Safety. Welcome to the
*  Cognitive Revolution. Glad to be here. I'm super excited to have you. You've been on my bucket list
*  of top target guests for a long time, and I'm glad we're finally making this happen. What I
*  thought we would do today is ask all the questions that I really want to ask of you and just get your
*  take on a ton of different issues and just get your sort of outlook on all these different issues.
*  Basically, get the Dan Hendricks AI worldview from a lot of different perspectives. I think it'll be
*  quite informative for everyone, but starting with me. For starters, I looked you up on Google
*  Scholar, found your number one cited paper still to this day is, maybe you can pronounce it for me,
*  2016. It's like a GIF for GIF thing. Is it Jell-O?
*  Exactly. I haven't decided. I'd say Jell-O more frequently, but people can make up their minds.
*  Yeah. I just think the creator gets to decide. So 2016, Jell-O. So this was a new activation function,
*  which basically was better than old activation functions and has been used in a ton of
*  neural networks that people have trained since. I think it's also been maybe somewhat superseded.
*  You can comment on these. It's still the state of the art or have new, even more
*  elaborate tweaks improved on it. But I'd love to get your kind of zoomed out sense of what are these
*  activation functions doing in the first place? How should we understand them? I think people
*  have studied a lot like the attention mechanism and many people have a sense for sort of the
*  residual stream as the core object and the sort of reads from the other parts back to it and all
*  that sort of stuff. But what are these activation functions doing? I think they're underappreciated.
*  What should our mental model of that be? Yeah. So to back up a bit, the Jell-O is a function
*  that's like X times the cumulative distribution function of the normal distribution of X. So
*  something complicated like that. In that line of research, we also made mention of other variants
*  on it like X times the sigmoid of X called the Silu, which we coined in that paper as well.
*  This was largely presented as an alternative to the ReLU, which is X times the indicator of
*  whether X is positive. So the ReLU is like that in its shape. The Jell-O and Silu are more like
*  these. They curve down and then go up. But anyway, this was my first paper and my first internship.
*  I was like, I got to work on a paper before I get into the safety stuff just so I can learn the
*  ropes. And then in the first week of that internship, I stumbled across that and then
*  wrote it up and put it on archive. Since then, it's been in the Silu are I think pretty much
*  the main activation in every cutting edge transformer model, GPT and Grok and Llama,
*  et cetera. As far as intuition, I mean, I don't know. I think it's not really in deep learning
*  about understanding. It's largely performance driven. And so that's why I think it's propagated,
*  not because it is a better theory or because it's more principled. It just tends to work better.
*  When intuition that led me to think of it is that the ReLU is like a flat line and then it's a
*  straight linear line. And so it's those two lines next to each other. And that seemed like a sharp
*  transition. And I was thinking the general lesson in looking at machine learning and
*  over the past decades is you don't want sharp things. You want things being smooth,
*  more probabilistic. And so I was trying to think of what's a natural way of smoothening
*  that sharp kink in the ReLU. And since the ReLU is X times an indicator function, which is a step
*  function, X times a step function, I just think smooth the step function. And then what's a natural
*  way of smoothing a step function, something like a cumulative distribution function or a sigmoid
*  type of shape feels like a natural way of going about that. So that's what gave rise to it. And
*  then after that first week in research and doing capabilities, I thought, okay, I could do
*  capabilities now. And then ever since then I've been focusing on safety research.
*  Soterios Johnson Do you have an intuition? You said, why is it better? We don't know.
*  You had your intuition for why it was something to be worth trying.
*  I mean, there's complicated ones when you can give like when doing filtering of signals,
*  there are kind of sharp filters. And then there are some of these smoother filters,
*  audio processing, and the smooth ones tend to be better. They're a bit more computationally
*  expensive. So I think just another domain sharp filters are generally not what you want to do.
*  But I don't know, my sort of philosophy is you in deep learning and in other things,
*  just try and find things that work and are impactful and do not really care too much
*  about the deep underlying reasons because they're largely inaccessible. A lot of things
*  are not obvious even in hindsight what they're doing for a lot of my papers, a lot of the methods
*  for them. It's not clear what they're actually doing even in hindsight. And that's just a sort
*  of fact of dealing with complex systems. There are limits to what inspection can unearth. And
*  that's just the world we live in. Soterios Johnson So can you give us just a little bit more on the
*  understanding of activation functions as signal filtering? Yeah, I think like detectors or
*  something like that. So interpretation of activation functions could be let's say you've
*  got something that scores whether there's a whisker in an image. All right. And then if the
*  neuron has a negative correlation with a whisker, that could be almost anything. That could be a
*  plane that could be a chair. There are lots of things that are in the opposite or in a different
*  direction from a whisker. But meanwhile, if something is very positively related, that is
*  an indication that you actually have found something like a whisker. So throw out the sort
*  of negative signal or the zero signal because that doesn't really help you and preserve the sort of
*  positive signal. So that's why one might want to filter, but one might not want to do just a so
*  the ReLU is saying throw out all negative signal, keep all positive signal, but it does so in a very
*  sharp way. And then this just does it in a smoother way. Gotcha. Yeah, that's interesting.
*  Reminds me of Eliezer's, the opposite of stupidity is not intelligence. Infinite ways to be wrong.
*  So if all we're signaling is that there's not something here, we'll just filter that.
*  That's right. So one thing I've been really interested in recently is the series of papers
*  called Magarov Arnold Networks. Ziming Liu is the lead author and it's out of MaxTecMark's group.
*  I guess they're doing some specific things. I think learnable activation functions feel like
*  maybe the next big thing. Everything is learnable except for the activation functions in many
*  networks today and they figured out a way to make them learnable. And they've also got some
*  interesting stuff around how to initialize them intentionally to enable different capabilities.
*  It feels a little bit more neuro-symbolic in its kind of form and I can imagine it going even
*  further in that direction. But what's your sort of expectation for that sort of work?
*  My higher level view of research on architectural changes in deep learning is that
*  it's probably not an area to investigate that much, largely because there's a sort of silent
*  graveyard of attempts over the past seven years since the transformer to try and improve on the
*  architectural components. So back in the day, when I started in research in 2016, there were a lot of
*  basic building blocks that were still changing. There was layer norm was introduced the year I
*  started research. The transformer was introduced some time later. There's still lots of different
*  activation functions and I think basically the Jellu and Sulu was the end of that.
*  Transformers looked almost like the end of architectures. There's still some changes,
*  maybe with some state space ones, but those still aren't very used in industry. So I think that as
*  far as architectural research, I would generally bet against it just because so much time has
*  happened since those advancements. It suggests that if there are advancements, it's going to be very
*  high hanging fruit and that the low hanging fruit has been plucked. I think maybe changes in loss
*  functions are a good idea, changes in the types of data that things train on. I think there's more
*  that one can do there, but on the architectural level, I'm generally suspicious of any major
*  advancements. This isn't to say that it won't happen, but by default for any sort of interesting
*  or tantalizing line of research, I'm largely just going to assume that there won't be anything to
*  it just because it's been so many years since a solid advancement in the architecture of deep
*  learning models. So does that make you sort of a scaling maximalist? The idea is basically just that
*  sort of any architecture will do and you can maybe get a little more efficiency here or there, but
*  ultimately the same kind of base infrastructure trends are what you expect to drive a future.
*  So in deep learning, there's algorithms, data and compute, and then algorithms, there's
*  the architecture and there's the loss function and how those are and how it processes the data.
*  I think on the architectural front, there's probably not as much. And I think that if we just
*  keep scaling up the models and keep giving them more data, then I'd expect that they'll get
*  substantially smarter. As far as roadblocks to getting a much more capable AI systems,
*  I'd be most worried about data and trying to improve synthetic data, try and get one's hands
*  on more data rather than trying to find some architectural improvements, which maybe will
*  help only marginally. I think the main change in the past seven years has been using a mixture of
*  experts model and mixture of experts transformer model. And I don't know exactly its efficiency
*  improvement. Maybe it's something like 30%. That isn't as substantial as scaling up compute 10x
*  more or getting 10x more data. I think the other axes are the raw resources axes compared to the
*  research insight axis is a bit more of the bottleneck for more performance systems.
*  Research will help, but I think it'll be a lot harder to get those sorts of advancements.
*  And I expect far fewer of them in the ones that we do get not to help as much as 10x more compute
*  or 10x more tokens. So your expectation is basically scale inputs and a 2022 era transformer
*  big enough can get you to AGI and beyond. I think that in practice, it won't actually
*  turn out that way. I think that there will be continued changes and people will make things
*  more efficient. I would guess that after one would get a very strong system, maybe you could actually
*  train it in this less efficient way. But I think that there'll be changes in the data. Maybe they'll
*  be given different objectives compared to just the next token prediction objective. Maybe they'll have
*  next day prediction or something like that instead of next token prediction. So I certainly
*  expect some changes though, but by default, I don't expect many of them. I think that people do
*  play up the extent to which algorithmic progress is necessary for getting good results. And the
*  amount of secret sauce inside of labs, I think is actually fairly minimal. And I think the thing
*  doing most heavy lifting compute and data. We recently looked at various open weight models
*  and assuming that they've trained on a lot of tokens, we sort of plotted their capabilities,
*  their performance on various benchmarks against compute and found roughly a 95% correlation.
*  So although they're different training recipes and they're doing supervised fine tuning in
*  different ways, it doesn't seem to make that much of a difference overall. Compute seems to be to a
*  first order approximation, the main factor driving these advancements. There will be some
*  algorithmic improvements along the way and they may help to some extent. But I think primarily,
*  at least if we zoom out in the past seven years, where have the primary changes come from? It's
*  been from utilizing data more effectively and using more of it. So basically around the time of BERT,
*  which I don't know, it was maybe 2018, they're training on a few gigabytes of text. And then
*  Roberta came after BERT, which trained on about 10x more text. And we've just been 10x-ing since
*  then. And that's been the main driver of a lot of these improvements where the architecture
*  has been fairly similar. So I think the main algorithmic advances in the past seven or so
*  years have primarily been humanity recognizing that maybe we should just train on more data.
*  We kept learning that lesson with the Chinchilla scaling laws and so on. And we are now getting to
*  the point where we're training on most of the publicly available data, publicly available text,
*  I should say. There's still YouTube. And that could present a sort of wall to algorithmic advances.
*  So maybe the scaling will stop sometime soon. It's totally in the realm of possibilities. We'll
*  basically just have to see what happens and whether synthetic data can continue the trend.
*  Most of the trend has been very confounded by the fact that we just train on more tokens per
*  parameter. And we just keep increasing that ratio across time. Hey, we'll continue our interview in
*  a moment after we're with our sponsors. The Cognitive Revolution is brought to you by Shopify.
*  I've known Shopify as the world's leading e-commerce platform for years. But it was only
*  recently when I started a project with my friends at Quikly that I realized just how dominant
*  Shopify really is. Quikly is an urgency marketing platform that's been running innovative,
*  time-limited marketing activations for major brands for years. Now we're working together to
*  build an AI layer, which will use generative AI to scale their service to long-tail e-commerce
*  businesses. And since Shopify has the largest market share, the most robust APIs, and the
*  most thriving application ecosystem, we are building exclusively for the Shopify platform.
*  So if you're building an e-commerce business, upgrade to Shopify and you'll enjoy not only
*  their market-leading checkout system, but also an increasingly robust library of cutting-edge AI
*  apps like Quikly, many of which will be exclusive to Shopify on launch. Cognitive Revolution
*  listeners can sign up for a $1 per month trial period at Shopify.com slash Cognitive, where
*  Cognitive is all lowercase. Nobody does selling better than Shopify, so visit Shopify.com slash
*  Cognitive to upgrade your selling today. That's Shopify.com slash Cognitive.
*  The Cognitive Revolution is brought to you by Element, a zero sugar electrolyte drink mix
*  that's working to change how we think about the role of salt in hydration and performance.
*  I have to say, when I started an AI podcast, I never thought we'd be sponsored by a drink company.
*  But when Element inquired about a possible sponsorship, they also offered to send me a
*  sample pack, and so I figured, might as well try it out. When the sample arrived, my wife Amy could
*  not believe what a perfect fit it was for me specifically. For years, I have felt that my
*  body needs more salt than nutrition labels indicate, and so I was interested to learn that
*  the Element formula is based on a growing body of research, suggesting that most people perform
*  best with two to three times more sodium than official guidelines recommend. I was also
*  fascinated to see that they specifically recommend it for people who fast regularly,
*  since I personally don't eat until dinnertime most days. Obviously, I'm not a doctor, and what my
*  body responds well to may or may not work well for you, but after drinking Element for a couple
*  of weeks, I can sincerely say that I really do enjoy the product. My favorite flavors so far are
*  the mango chili and grapefruit, and I for one also enjoy the raw, unflavored version, which reminds
*  me of the taste of the ocean. If you're curious about optimizing your electrolyte intake, you can
*  support the show and get a free sample pack with any purchase by visiting drinkelement.com.
*  When I look at new architectures, certainly recognizing that what you're saying is true,
*  that most of the things that appear to be an improvement end up not panning out or at scale,
*  they sort of converge or whatever, I have found it somewhat helpful to look for new what I call
*  micro skills, which is, is there something structurally enabled by this new architecture
*  that alternative architectures couldn't do? Then what seems to be happening, at least right now
*  with the state space models, is the hybrid form tends to be the best. You seem to get the best of
*  both sets of micro skills. In the case of the state space models, they can't recall all prior
*  tokens in the same way that a attention-based mechanism can, but they do seem to be better at
*  learning from a really sparse signal. In the case of the cans, it's like they have maybe a
*  lot of weaknesses, but they do have some strengths in terms of being composable. You can write down
*  a function and you could represent that in a can in a way that is literally representing the
*  equation, whereas with a transformer you can converge on it, but it's like a weird sort of
*  thing. Do you find that compelling or how would you tell me to update my thinking?
*  I think there are a lot of ways to build systems with attractive properties, but the main thing is
*  overall what's its performance. I was trained mostly doing computer vision type of papers,
*  because that was the main way of assessing deep learning progress was on image tasks in the past,
*  and culturally they just be what's the performance. Because you could, for instance,
*  construct conv nets that would have lots of nice properties like some equal variants to
*  some specific transformations, and you could do some top-down imposition of those properties,
*  but overall they weren't beneficial or necessary. It's also the case that with scaling,
*  there's a rising tide lifts all boats phenomenon such that some of the specific engineering that
*  happens with current models just gets taken care of when you have a more generally capable model
*  in the future. It has a wide set of different capabilities and some of its gaps it can end up
*  filling in with some of its other capabilities. I think trying to go for an aesthetic, it can solve
*  some of these specific toy tasks, or it has nice mathematical properties. As a researcher, I just
*  embody the deep learning philosophy. You look at the number, you throw the stuff at the wall,
*  you see what sticks, you have some vague intuitions, wild sounding, maybe they're even
*  neuro-symbolically inspired. You ultimately just select what's most effective and not really think
*  too much about the details or other sorts of properties. That I think is quite intellectually
*  offensive to a lot of other traditional machine learning researchers, or you're wanting some
*  proof, some justification for things. I think they're nice to have properties, but for all that,
*  I don't know if it's going to overall improve the performance or be necessary at a higher level of
*  scale. We'll just see. By default, it looks like there's a very low rate and looks like we're
*  getting a lot of progress from other things. I'm just going to mainly expect most of the progress
*  to come from other things and less to come from that.
*  Got you. This is a far out question, but I do have one visualization that I keep coming back to,
*  which I don't think is going to be too far wrong yet. That is of some abstract shape that is
*  reality and the model being basically a vacuum pole that is shrink wrapping around this reality.
*  And just the tighter you pull, the closer the shrink wrap gets to this weird
*  shape. How do you react to that? Do you have any of your own that you'd like to share?
*  I like that because it has the multi-dimensionality. I think as far as analogies or intuition pumps to
*  think about these systems, I think they're so confusing because we don't understand intelligence.
*  Since we don't understand intelligence, we don't understand these AI systems.
*  One observation about intelligence is that human capabilities are quite lopsided and strange.
*  For instance, we speak all the time and yet we constantly pause and say um, and if you actually
*  transcribe our sentences, maybe half of them are fully grammatical. Even so, we think of ourselves
*  as very smart. We're better at doing a lot of social modeling relatively. We're okay at that.
*  We are pretty bad at arithmetic though, which you'd think should be a lot easier than doing
*  theory of mind and social modeling and picking up unsubtle cues. Our vision system is really
*  fantastic. Even humans have a very not necessarily simple capabilities profile. And so likewise,
*  we should expect a somewhat strange capabilities profile of AI systems as well, where they're
*  able to get a silver at the IMO, but at the same time, they can't count the number of ours in
*  raspberries reliably. Another intuition I think gives the most mileage for
*  deep learning systems is thinking of them just as complex systems. So cats are complex systems,
*  human brains are complex systems, the economy is a complex system, ecosystems are complex systems,
*  and those have a lot of unexpected properties. You can't reason your way through them or even
*  mechanistically predict exactly what's going to happen because there's so many parts,
*  so many loose connections, so many feedback loops, which give rise to new emergent phenomena and
*  qualitatively distinct properties. I think if people are trying to wrap their head around it
*  to some extent, they could try and learn some more about complex systems to get intuitions for those.
*  We have a lecture on complex systems in aiSafetyBook.com where we discuss the
*  complex systems and its analogies to AI and its implications for AI safety. But that's basically
*  been the only analogy that hasn't led me astray and has provided many predictions.
*  – Gotcha. Okay, cool. Let's change gears and talk about benchmarks. You have done some important
*  work in benchmarking, most famously with MMLU, which certainly everybody will be familiar with
*  seeing that the frontier models compare themselves on MMLU. I don't know necessarily how much
*  intuition people have for what the questions actually consist of. Back when I was doing the
*  GPT-4 Red Team project, I found that basically it was blowing all the other benchmarks away.
*  MMLU was the one where it was still not getting all the questions right.
*  Interested in a little bit of the story, a little bit of how that was put together,
*  what the questions are, how you were able to create a benchmark that endured for five years when almost
*  every other one was quickly rendered obsolete. But then also we seem to be maybe getting there
*  with MMLU too. We have to kind of look also to what's next.
*  – Yeah, that's right. So MMLU has 57 different subjects like history, calculus, professional law,
*  you name it, it's probably in there and it's probably at some different levels of difficulty.
*  There's graduate physics exam questions, there's arithmetic questions, there's a span of difficulty
*  and a lot of breadth and depth. The idea was that a lot of the linguistic understanding benchmarks
*  were not being sufficiently difficult. I was seeing basically every few months,
*  newly proposed benchmarks dying because they kept really searching for places where the model
*  wouldn't linguistically understand something, but their capabilities just kept improving.
*  So it seemed to me that these weren't really doing computational or linguistics or natural
*  language processing as much as text processing and that we shouldn't be trying to understand
*  their linguistic strengths because it seemed that they understood syntax and grammar and
*  basics of English pretty well. Then I was thinking the benchmarks weren't doing a good enough job
*  at capturing their capabilities. People had tried doing common sense as a sort of set of benchmarks,
*  but they kept getting common sense as well. This used to be an extremely contentious thing to say
*  that they could predict that if you light a match and put it on a pile of leaves,
*  maybe that will cause a fire. LLMs can say that and that's considered some common sense knowledge.
*  People would say, no, no, no, they don't have common sense. There is sort of a collective lie.
*  I think that generally in the academic community, they have a very strong preference for underclaiming
*  and try and severely penalize things that are deemed over claiming, just saying they have common
*  sense, which is true for maybe a year and a half before people are not going to get hit
*  open the head saying that type of thing. And that is for historical reasons, it's because there's an
*  AI winter. So there's generally extreme hesitation toward saying surprising sounding things and
*  generally a strong incentive for underclaiming. That's, I think, one reason why the world was so
*  caught by surprise by Chad GPT as well. Before that, I was making a benchmark for measuring
*  ethical understanding, but then the AI systems got common sense. And so it was looking like they were
*  starting to do okay at it. So then I need something harder. What's the sort of next stage in ethics
*  or what are trickier ethical scenarios I can give them? And then I thought, I know tort law
*  and criminal law seem like a fantastic set of questions. So I collected lots of legal questions
*  and then that seemed pretty tough for them. And so there are like, I don't know, maybe like 2000
*  legal questions in MMLU or something. So a big chunk of the data set. I thought, I know, why don't
*  we just do some other types of exams, like basically pretty much any exam that people give
*  humans. Let's just throw that in there. Basically we copy and pasted lots of data for a month and
*  then out came the data set. And I think initially NLP researchers were, oh, this is bad. This is
*  going to incentivize models to not learn linguistics and the English language better. It's going to
*  incentivize them to just learn everything online or memorize everything. So it was not well received
*  initially, I think partly because it was saying, we're focusing on linguistic understanding. We're
*  in a different sort of paradigm now, but eventually things sort of shown through. So we just copy paste
*  the data set and then we released that collection and it looked like models started doing pretty
*  well. I think that knowledge understanding was the correct next thing to look at. After we published
*  the paper or when we were publishing the paper, we noticed that they did a lot worse on STEM subjects.
*  So that incentivized us to look more specifically at the STEM topics and then collected the M.A.T.H.
*  or math data set, which is a collection of, I think, 12,500 competition competitive math questions.
*  That seems to be maybe like the number three benchmark used. And I'm only use like the number
*  one and maybe like LMSS is like number two. These all will be beaten by the LLMs maybe in the next
*  year or two. There will need to be some things to replace them. Before we go on to what's next,
*  you've done a bunch of different benchmarks, including some regarding issues like deception.
*  And there's one that's like the Machiavellian benchmark. Do you want to just highlight any
*  other benchmarks that you think are as yet still underappreciated? I think that the Machiavelli
*  one, I'll just speak about that one. So there's a benchmark called Machiavelli, which is largely
*  assessing the propensities of LLM agents. So you plot them in various different text adventure
*  games where these are choose your own adventures and you just have them play through that and see
*  where they wind up. What sort of decisions do they make along the way? Do they screw people over
*  or are they generally nice? Are they really competitive? If you're incentivizing them to
*  get reward, do they treat other players as more means to an end? Do they lie a lot? So this,
*  I think, was a benchmark that we just designed for when LLMs would be more like AI agents. And
*  I think that basically the capabilities aren't there yet. Some of these benchmarks, we basically
*  just put into place as something that would become relevant later. I tend not to do that type of
*  research as much now where I anticipate the paper will only become relevant two years in the future.
*  That's a little riskier, but I think that paper may end up just being used when they get more
*  agent-like capabilities and then we want to estimate their propensities and try and control
*  them to behave in a more pro-social way and less deceptively, less in a Machiavellian way.
*  I think that's probably one of the main benchmarks that I expect to kick in later.
*  The sort of design philosophy of it is if you're wanting to measure
*  AI's game playing abilities and keep track of their morally salient properties, you could run
*  them on games like Grand Theft Auto or something, but this is just harder to set up and requires a
*  lot more compute. If you're just wanting to see what types of decisions it makes, I think text
*  adventure games get you a lot of the way there. You don't need to spend as much compute rendering
*  graphics or getting the right drivers. That's what that benchmark is, but yeah, it's currently
*  not particularly used, I think, because the AIs are not very good at being agential yet.
*  Hey, we'll continue our interview in a moment after our word from our sponsors.
*  As a Cognitive Revolution listener, you're obviously interested in cutting-edge AI technology,
*  and with that in mind, I'm proud to say that this episode is brought to you in part by Notion.
*  Notion has been a clear leader in high-value applications of generative AI since the wave
*  began. Earlier this year, we had Notion AI engineer Linus Lee on the podcast. The quality of his
*  insights showcased the caliber of talent that Notion employs, and that inside look at how
*  Notion builds with AI is still extremely valuable. Given my personal focus on AI automation recently,
*  I specifically wanted to highlight Notion's library of workflow and automation templates.
*  If you're looking to streamline your processes and lay the foundation for future AI-driven
*  automation, these templates are an excellent starting point. And even if you're not ready
*  for full automation, you'll benefit immediately from Notion AI, Notion's latest all-in-one AI
*  implementation that searches through thousands of documents, regardless of whether they live
*  in Notion or on some other platform like Slack or Google Docs, to deeply understand the context
*  of your work and generate highly relevant analysis and content just for you. Notion is
*  used by more than half of Fortune 500 companies, helping teams reduce emails, meetings, and time
*  spent searching for information. Want to try it? Head to Notion.com slash Cognitive Revolution.
*  You can start for free, and using our link supports the show. So join me in giving Notion AI a shot
*  today at Notion.com slash Cognitive Revolution.
*  AI might be the most important new computer technology ever. It's storming every industry,
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing, and of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive of OCI at Oracle.com
*  slash Cognitive. That's Oracle.com slash Cognitive. Oracle.com slash Cognitive.
*  Just going back to MLOU for one second, how do you understand the scores that we're seeing today?
*  There's obviously a lot of debate around like, for one thing, people may have trained on the data set
*  at this point. You've got the sort of argument from the Francois Chalet's of the world that is
*  they have memorized a bunch of ways to solve particular problems. So they're like pattern
*  matching on that and then implementing a certain algorithm, but in some way that's like not general.
*  And then obviously with data sets like these, there's also just issues in the data sets where
*  there's like some questions in the answer key are wrong. So where do you think we are? Like if I see
*  a 90% on that, what does that mean in practical terms to September 2024?
*  Yeah, I think that we are now at the high 80% region for MLOU and we've been stuck there
*  ever since GPT-4. And I think that's because the AI models haven't substantially improved in a
*  general way since GPT-4. They've improved in their formatting of answers and performing some specific
*  tasks that I don't think in a general way, which is I think LMSYS is largely reflecting on some
*  summarize this type of tasks or in formatting answers. I think it's measuring that quite well.
*  I think the MATH benchmark is measuring their mathematical problem solving ability, which has
*  improved over the past year through targeted synthetic data creation. But in a general sense,
*  we haven't really trained models that are substantially larger than GPT-4 yet. To my
*  understanding, there are no models that have been trained with more than 10 to the 26 flop.
*  Meanwhile, GPT-4 was trained around using 10 to the 25 flop. I think the MLOUs are somewhat
*  stagnant in part because the models aren't generally better. They're better in some senses,
*  but not in a very broad raw intelligence type of sense. But that will change as we scale the
*  models. And then I think maybe with the 10x larger model, maybe that'll get in the 90% region. And
*  then I think that will be around the point of saturation for MLOU. People can still use it to
*  try and train their models to get a higher score using less compute, things like that for efficiency
*  research. But it will cease to be a guide for frontier development later on.
*  Just calibrate against the human for a second. If we take a, let's say, PhD in any one of the
*  subjects that is covered with MLOU, we would expect them to get what, 90, 95?
*  Yeah. So we looked at each of the subjects in MLOU and tried estimating what's a 95th
*  percentile test taker likely to get and then aggregate those scores. And that gives an overall
*  accuracy on MLOU of about 90%. So I think 90% is where is the for each subject 95th percentile
*  test taker would end up getting. And I think that's a-
*  And that's like the 95th percentile of graduate students?
*  It depends of the test takers. So for instance, for the bar exam, that'd be what's the 95th
*  percentile score on the bar exam. For AP calculus, it's what's the 95th percentile on AP calculus.
*  So not necessarily just always adults, but just people who generally do very well at the exam.
*  And when you aggregate all those together, that's around 90% or so. But if you asked an
*  individual human, I think individual humans maybe get, I think we had some MTurk thing and
*  they were getting like around 30 to 40% on it. Yeah. It's worth taking a minute to go just peruse
*  the database of questions because there's plenty of things you just will have no idea what you're
*  supposed to do. There's a site called, Are You Smarter Than an LLM? I think, which just shows
*  you questions from MLOU and then you start going, oh, I don't remember that bit of economics. Oh,
*  I don't remember that bit of history. Oh, I don't. So I think one shorthand for it or
*  Elon's description of it is it's basically like an undergraduate level knowledge and skill test.
*  And I think that seems like roughly appropriate. Some of the questions are quite a bit harder.
*  There are graduate school questions in there, but I think that gives the gist of it fairly accurately.
*  Gotcha. So to bottom line that it is basically the 95th percentile of test takers gets about 90%
*  in whatever subsection of the MLOU suite of tests. I would guess the models are better than any
*  individual human test taker on it. I think as far as the integrity of it, the sort of claim that
*  there's a lot of contamination or that people have trained on it or memorized all the answers,
*  like if they memorize the answers, I would expect a higher score. I'd also expect things not to track
*  difficulty. The subjects that are difficult for models two years ago are still the subjects that
*  are difficult for models on MLOU this year. So for instance, they still get lower professional law
*  type of questions. If they're just memorizing them, then it should be not track difficulty
*  really at all. It should be more uniform across the board. So I think that undermines that
*  hypothesis. There certainly are some labs that really try and optimize these numbers and maybe
*  try and train on similar types of questions, but they tend to get caught. Scale AI, for instance,
*  for some arithmetic benchmark created their own variant of it. And then they saw when we test
*  people on our own variant of these questions, what happens to the performance? And then they can catch
*  a few of the models, but most of the models were actually just fine and not training too heavily
*  on those. I think there are maybe a few bad apples, but the leading labs don't seem to really have
*  this sort of issue. Interesting. I have in my memory of this is not super crisp at this point,
*  but I feel like when I was doing this spot checking in the GPT-4 Red Team era, I think it's the math
*  one where you're supposed to do all the reasoning and put a box around the final answer.
*  Right. Yep. That's an accurate set. Maybe I was giving the instruction to do that, but it seemed
*  like it had internalized the form of the test in a meaningful way. I remember being like, oh, it's
*  giving me exactly the sort of box notation it's doing. Yeah, Lama does that. I think it's because
*  there is a training set of 7,500 examples. And if they were to collect their own data set like that,
*  I think it would cost several million dollars. So I think that they are just training on the training
*  set and it teaches the format of the math data set. Gotcha. So training in your view, I guess,
*  or to generalize- Training on the training set is fine.
*  That's yeah. Okay. Well, that does sort of feed into the François Chalet critique also that
*  there's a catalog of well-represented problems that they've had a chance to go deep on as part
*  of their training and it at least leaves the door open to sort of an argument that they're running
*  some sort of stored procedure that they've learned as opposed to having a more flexible intelligence.
*  I mean, it undermines the flexibility of it. There's just a question of in practice,
*  is it going to be useful if you have a large enough collection of skills? Then maybe that's
*  fine. Michael Jordan, when he'd play basketball, he was saying like, every game is like practice
*  because I've already done that exact maneuver before and just remember how I went about it then
*  and I'm just going to do that now. I think an aspersion on deep learning models is a little
*  underspecified if it's to be like a successful critique because maybe a catalog of a lot of
*  skills is just what a multipurpose AI system is, but maybe right now the models are having their
*  catalog a little fragile and it can lead to some incorrect estimates of their abilities. But I think
*  by and large, it's roughly right. If you give AI systems high school level or undergrad type of
*  problems, they're basically going to do a good job most of the time. I think they're a good solution
*  for that. People come with new exams and they're probably going to generalize to those. So I think
*  it reasonably reflects the actual performance of these. Otherwise, I don't know why students
*  will be paying 20 bucks a month to be using chat GPT to cheat if it wasn't any good.
*  How would you describe this? I find myself confused by this broadly and this is one of those
*  debates where anytime I spend a significant amount of time immersed in one worldview,
*  it starts to feel pretty plausible to me. It seems undeniable that when the Arc AGI folks,
*  and I've had my canoe on the podcast to discuss this, when they say that progress toward AGI has
*  stalled, I cannot empathize with that. It feels to me like, okay, maybe there hasn't been a scale up.
*  There hasn't been a scale up. That's the confounding one. When people are thinking about progress in it,
*  the same thing happened after GPT-3. I was like, boy, these models are getting really good.
*  Then people are like, oh, you're overreacting. Then a year passed and there wasn't a substantial
*  advance. Where's your rapid progress now? But it was just a function of how long does it take them
*  to get the GPUs from Nvidia? Will Nvidia give them the GPUs? Then when they get the GPUs,
*  there's creating the new 10x larger supercomputer. That's just taken people a while. Now I think
*  they're built and then now they're going to scale them. I'd expect we'll see the next generation
*  of AI models in the next six months. It's not clear how capable they'll be. Maybe they've hit
*  a data wall. Maybe GPT-4 has trained on all the publicly available tokens and so the scaling laws
*  really slow down. That's totally a possibility. But in the absence of seeing a model train on
*  10x more compute, it seems very difficult to claim that the AI is hitting a wall. We'll have
*  to see if it actually does. That's a confounding factor. Have they tried training the 10x larger
*  model and how did that go? If that went poorly, then that's actually some evidence. But in the
*  absence of people even trying that, then I think it's much too early to weigh in.
*  Mad Fientist How would you describe large language model reasoning today? You mentioned earlier that
*  at one point it was crazy to say or it was contentious at least to say that they had common
*  sense. Now we could say, yeah, they generally have common sense. They generally have some sort
*  of theory of mind. They have some intuitive physics. There are still gaps, but to deny the
*  common sense has become very difficult to do. Now we're at the reasoning stage of this debate.
*  How do you describe the reasoning that we see from language models today?
*  Jeff Sarris It's always fairly lopsided. There are probably some common sense questions that
*  they'll still get wrong. How many times do you need to attempt to get the model to do something
*  stupid before it does something stupid? And I think if that crosses a threshold, then people will
*  stop saying that they're bad at reasoning. If they nail five tough questions you give them,
*  then people will go, okay, all right, it passed my vibe check and I'm no longer going to make that
*  claim. A lot of these things have a sort of reliability threshold. With automatic speech
*  recognition, for instance, people didn't use it for a long time. They could transcribe what you're
*  saying, but not that well. And then at some point they just crossed a reliability threshold
*  such that it became convenient to use and they'll actually do a good job. I think sense needed to
*  cross one of those thresholds. I think reasoning needed to cross one of those thresholds. I don't
*  think reasoning has crossed a threshold. It's totally plausible that it will in the next year
*  if the scale-ups are successful. I think it's basically like that. And it's not obvious to me
*  that we need something totally different to get those reasoning skills.
*  So when you look at something like the ARK benchmark and the ARKGI prize that's now built
*  on top of that, it does feel like there is something apt about pointing out that, hey,
*  if these things can't do this, which many of them are, they're not all easy, but many of them are
*  quite intuitive for people, then there is some sort of missing generality. I don't think I could send
*  GPT-4-0 to another planet and have it find its way in the same way that I might expect to. Of course,
*  it might survive the radiation on the way there, and I might not. So it has its advantages.
*  But it does feel like there is something missing. This also connects maybe to the data
*  point that you raised where we've got largely all the publicly available text already in the
*  training data sets, maybe not so much of the publicly available imagery or video. I just
*  tried using some of the frontier models just to provide the visualizations of the ARK puzzles and
*  say, describe this image. What do you see? And I was really struck by the fact that they can't see
*  it clearly at all. They cannot describe, forget solving the puzzle, but they literally can't count
*  the blocks in a formation or identify shapes very well. You mentioned earlier too, our visual system
*  is great. Certainly, it's striking to see what is so obvious at a glance to me is something that
*  these models just cannot see. So I guess to wrap that into a question, do you think that is where
*  the next scale up comes from perhaps is the sort of multimodal? Do you feel like that is important?
*  And do you feel like that is maybe the heart of why it's not doing these things where people are
*  more attributing it to the lack of reasoning? Maybe it's just like the lack of vision.
*  Yeah. So my diagnosis having not spent much time with that particular benchmark, I think generally
*  the AI systems are not very good at multimodal reasoning, not even considering that, just
*  consider the generic benchmarks like MMMU, which is I think massive multimodal multitask,
*  I don't know, understanding something like that. But MMMU, the models don't do that well. So even
*  on basic figure understanding, they're limited. I would firmly distinguish between vision progress
*  and progress for text models. In vision progress, there are more algorithmic advancements to be made.
*  When I was a vision researcher, there were constantly improvements to the architecture
*  that one could make and to the training method and so on. Given that they're bad at image
*  understanding, I think that's quite a limiter for them to be able to even understand the arc
*  challenge. I also think that the models, if you express it in text format, they don't really
*  understand grids that well. I think they struggle at tic-tac-toe. It's just not as natural of a
*  format for them to try and express images in text. Maybe when its intelligence is appropriately
*  expressed through its image understanding, then maybe it'll become easier. I think if you
*  reformulate the task to some extent, they basically seem like a type of Raven's progressive matrices.
*  And if you encode Raven's progressive matrices as tuples and give them to LLMs, there's about an
*  80% correlation between its performance on Raven's progressive matrices, IQ test type of things,
*  and other benchmarks. So it seems that they can generalize to these pattern matching things that
*  are difficult for humans, even if they're expressed in ways that they haven't exactly seen before.
*  I think if we reformulate them, they can do fairly well. That's why I would guess that their overall
*  fluid intelligence, to use that term, is less. But that could change as they get bigger. I don't
*  think too much of it is a particular sign. I certainly can see why if one would hear all the
*  arguments in favor of that one could end up believing in it. It may be one of the harder
*  benchmarks. I don't think it's knockdown evidence against the current paradigm and
*  suggested that we need a totally different approach. Do you think embodiment in the
*  form of perhaps just literal everyday robots is going to be a big unlock? I feel like there's
*  some possible gap in the training data that is just how to actually navigate the world,
*  how to proceed in common sense ways that maybe just gets filled out over an initial period of
*  early deployment. I don't know if embodiment would be because in a lot of the multimodal
*  research at around the time of CLIP, there were studies like to what extent does image understanding
*  help improve the text representations? And it seemed like basically really not at all.
*  So there hasn't been much signal from those forms of data in improving the underlying
*  representations on other intellectual tasks. I think it's probably more in the other direction
*  that the text understanding representations that come from text understanding improve its ability
*  to act in these environments and provide some with some basic common sense that like fires don't go
*  touching that. So if your image recognizer sees fire, maybe stay away from it. But so yeah,
*  I'm not expecting as much embodiment as a substantial data source, nor am I expecting that
*  much by default from video. I think video hasn't improved representations historically. People
*  have constantly tried with a lot of compute over and over again. It certainly is a lot of data.
*  But for all that, I think you can compress the intellectual content in the YouTube video.
*  It's very substantially. So if you have a YouTube video, maybe that's like a gigabyte or something,
*  or maybe a few hundred megabytes, but you could transcribe it. Now you're down to like less than
*  a kilobyte probably in the transcription. And often the text in these transcripts is just like
*  talking. It's not like an essay where it's like thoughtful and highly optimized and hundreds of
*  hours of labor are put into the text. So I think like in comparison to a paper online, each video
*  is generally a lot less informative. So although it's a very big file size initially that the
*  actual underlying intellectual content is less. So if we're interested in improving reasoning,
*  for instance, I'm not sure that there'll be too much to come from that. Of course, all these things
*  can be wrong. Deep learning is very unexpected often. But at least from the test of time,
*  it hasn't seemed to be that promising of a research avenue. How would you reconcile that with open AI's
*  claims of world modeling in Sora? They're claiming like it's learning intuitive physics and all these
*  things from just basically video at scale seem to be like an important part of overall reasoning
*  would be intuitive physics? For embodied tasks, certainly. So I wouldn't make the claim that blind
*  models will do just as well as models with some vision capabilities in real world, physical world
*  tasks. But I don't know if it would necessarily give it that much extra mileage in its ability to
*  solve physics problems, for instance, unless they're visual in nature. But if they're described in a
*  text way, I don't know if that'll make it do better on the GRE physics exam, for instance.
*  Yeah, it's interesting. I don't really understand human cognition super well, I guess who does,
*  but certainly some understand better than me. That's the usual argument. Just like Helen Keller was
*  really smart. She was blind. So it doesn't seem necessary for high levels of reasoning.
*  Yeah, but I also do have the sense that people seem to understand that we are like reusing the
*  visual cortex for a lot of physical reasoning, like Einstein supposedly visualize himself on a
*  photon or whatever. Is there not a similar thing perhaps to be unlocked in multimodal
*  scale with multimodal models? That intuition actually has given a lot of mileage. So the idea
*  of some of these AGI companies in the past was we're going to do really well on vision.
*  And that is going to teach us a lot of how to generally do deep learning, training and
*  computation and how to make good architectures and things like that. So deep learning basically
*  evolved out of computer vision research. So I think there is some association, but I think it's
*  I just think it's kind of speculative that one would require a mind's eye, so to speak, to be
*  able to solve mathematics problems, given that they can solve mathematics problems without any
*  visual capabilities. But there certainly does seem to be some relation between the vision part of
*  the brain and the computation that goes on in the rest of the brain. It's an argument for it. It
*  doesn't seem like a strong one, especially contract with other sorts of points that you
*  can train them to do reasonably without any visual input. Another way that I think about the arc
*  benchmark and this gets to like the frontier of current capabilities is assuming that you could
*  see the image or have some sensible way of confronting what the actual pattern is.
*  The hardest part of the task seems to be this sort of infer the rule step where and I'm approaching
*  this largely through like introspection. I've asked myself, what am I doing here and what is
*  the hard part about it? And it seems like the vision part for me comes obviously very easily.
*  The models can't do that, but it's very easy for me. And then I sit there for a second
*  and I squint at it and I eventually have a bit of a eureka moment. It's typically not
*  verbal and it's not even necessarily conscious. It just pops into my head that, okay, this is what
*  I think the rule is. I think I got it. And then once I have that, I can basically try to confirm
*  that my rule when applied actually works. That guessing or inferring the rule from a couple of
*  examples does look to me a lot like coming up with good novel scientific hypotheses in as much as I
*  don't think we generally know where those new ideas come from. And it also seems to be something that
*  the current models largely struggle with. I've not seen much, although there have been a couple
*  of recent bits of noise made around the AI scientists and even more recent paper than that
*  that claimed that language models had generated better novel hypotheses than scientists. I still
*  need you to read that one. But by and large, we haven't seen too much where the models can generate
*  novel hypotheses that are on the level that human scientists can do. Do you see that as a good toy
*  representation of that bigger task? I think it's a component of intelligence. You can measure it in
*  different ways. I think the Ravens progressive matrices test to some extent have you just infer
*  the pattern to complete the pattern in a new scenario. But models can do well. LLMs can do
*  well on those sorts of tasks. Not like the best, but okay. And one should just expect it to continue
*  to improve given the strong correlation between it and compute like about 80% correlation.
*  Sometimes you need to infer the underlying rule of what's going on. It's not necessary for a lot
*  of areas in science. Deep learning, as I was discussing earlier, is more of a bottom-up,
*  a theoretical tinkering engineering science and less about big insights and contemplation,
*  particularly giving you much mileage. There's having some idea of some guesses to try some
*  hunches. And that's a taste thing, which I think is generally on the more intuitive side of things.
*  They are probably beneath humans though, in their capability to infer latent rules behind some of
*  their observations, but they do okay. So this doesn't raise any alarm bells for me that we
*  need to do something totally different. But there is a lot of evidence lying around for some of
*  these different theories because we don't understand intelligence very well. I'd give it some plot
*  possibility and there'd be tail upside in AI development if some people are exploring it.
*  But by default, I'm not going to make plans around that in particular. I think there are probably
*  other sorts of factors that I think carry more weight in AI development, like when we hit a data
*  wall or if we hit a data wall and whether synthetic data succeeds or conflict in Taiwan, meaning
*  the IMC is no longer functional, meaning the West doesn't have enough AI chips and China with its
*  own independent froundries that they're building up do have more chips and then the West falls
*  behind. These are things that I think will affect the AI story substantially more. But it's possible
*  that some substantial algorithmic development will also give a 10x, 100x type of improvement.
*  But we've just been hearing it for many years, so it makes it a little harder to put much weight in
*  it though. But yeah, I wouldn't bet the farm against them necessarily.
*  So how are we going to measure this? I understand that you have a new
*  benchmark that is in the works and it aims to be the successor to MMLU that will
*  give us a new yardstick to measure our future systems by. Tell us about that project.
*  Yeah, so I think maybe this week we'll announce a competition where people can submit difficult
*  questions. And then if their question is accepted and found difficult for the existing models and
*  difficult for experts, then it can be included and then they'll be on a paper. So I imagine there'll
*  be over a thousand co-authors on this. Generally, there'll also be money prizes for it. So I think
*  some of the winners will win thousands of dollars if they submit particularly good questions. Others
*  will win on the order of hundreds of dollars for really good questions. It's maybe about between
*  $500,000 and a million or so in prizes. I'd have to check what it will end up being. But I think
*  the basic premise is I've been doing some data collection in the past year and a half and I think
*  we've very quickly gone from MTurk annotators to grad students to even like profs and just like
*  real subject area experts and things. And I've also found that it's difficult to get them to
*  collect a big data set. So let's say you're trying to measure virology skills. Really an uphill battle
*  in trying to get a large data set out of a small group of experts. So instead the idea is we'll
*  just try and ask, get one or two or a few difficult questions out of people who have lots of years of
*  experience doing something technical or people who have a PhD or PhD students or above. People
*  know some subject really well and have some very non-trivial knowledge. And I think a collection of
*  that will then be something like the last exam we should need to give AIs. So it's currently called
*  humanity's last exam because we're all coming together to make a really tough exam. And if
*  AIs do complete it, I think they've got at least a really expert level knowledge and it would require
*  some type of super intelligent oracle. It won't necessarily have agentic skills, but that should
*  probably be the last knowledge test that we'll end up needing. It's also trying to be quite difficult
*  because it's very possible that AI systems will get, I'm not saying it's necessarily going to happen,
*  it's very possible that AI systems will get like a gold medal in all the Olympiads next year.
*  They just got a silver on the IMO and we'll see how they do at the ILO soon. So we need questions
*  that are harder than Olympiad questions as well. And that looks like for some people like asking
*  math professors what's a very difficult question that came up in research and then put down that
*  question and write down the answer and then that gets added to the data set. So something more on
*  the frontiers of human intelligence I think is useful. And it also that's part of what the ARC
*  challenge is trying to do, which is trying to get more data efficiency. When there's a lot less data
*  for a specific subject, if it's not very well represented in its catalog of skills, can it
*  still generalize well? So if you're asking about more esoteric topics of mathematics,
*  things for which they're just a few papers published and there are a lot of complicated
*  relations that just haven't been explicated anywhere, can the model infer those or reason
*  to those conclusions by itself? So I think we're going from MMLU where there's several
*  textbooks written on each subject to esoteric areas for which there is not as much data and
*  a lot of reasoning that tends to be required. So that's the sort of makeup of humanity's last
*  exam. I think some implications of it will be this will provide a good sense of how far you can take
*  question exams. I guess one other observation is that maybe it will invalidate the notion of
*  the Erdos number because if you get one person with a low Erdos number on the paper, then
*  thousands of collaborators have a low Erdos number as well. But I think that's one such benchmark.
*  I'm doing some other benchmarks like these Ravens progressive matrices types of things,
*  but I'm trying to have it be questions that are harder than what humans can generally answer.
*  So you can construct sequences of patterns that have a simplest solution, like in a Kolmogorov
*  complexity sense. Sometimes you can compute it in particular cases, and so we're exploiting some
*  of those cases. So it's a pattern recognition thing, and then you show it to models. And then
*  I think this will be a way of us tracking their raw intelligence after they become human level and
*  are at some intellectual abilities than humans. Because I think that is a challenge if we're
*  trying to, as a world, do something like rate limit the amount of AI development, let's say 100
*  X years too much for us. Maybe we're fine with three X a year in terms of efficiency improvements
*  or something or 10 X. We would need to be able to measure that using questions that are harder
*  than what humans can answer because the AIs will be smarter. So I think we can algorithmically generate
*  with some data, some very tough questions that do have a most natural simplest answer and see
*  whether models can answer those. And then there's an agent benchmark that I'm doing as well, but
*  that's still in somewhat earlier stages. Maybe I'll punt on that one, but I think the main one in
*  the short term that should be a combination of MMLU and math is this sort of humanities last exam
*  collection of the hardest questions for the world's experts and see how models are improving on that.
*  Maybe they'll flow past it. It's totally unclear when they scale up, or maybe it'll actually just
*  be really hard and maybe it will take several years for them. But either way, I think we'll
*  have a best attempt at the format of asking questions to AI systems and carry that to its
*  conclusion. Do you feel like that needs to stay private to some degree? I mean, that's part of
*  what Arc has done and Scales doing that too. Yeah. So we're doing this to scale because then
*  they'll pay for it. So it just was, hey, here's an idea. And then the private data is useful for this
*  sort of stuff. So I think having a fraction of the data set held out as private seems like a good
*  idea to catch cheating and that'll create a deterrent for various companies juicing their
*  numbers. I think we'll definitely do that. Yeah. It sounds also a little bit like the Google
*  proof QA set. Is that like a good kind of mental model and even harder still? I think it's that and
*  even harder and more diverse. I don't know what the sort of label noise in that is. I don't know
*  if it's 80 or 20% of them are wrong. I think the sample size is fairly small in GPQA. It's about 500
*  questions. I definitely hope we can get much more than that because when you've got only 500 or so
*  questions, you have a very bad sample size. So like you've got plus or minus 5% between different
*  runs. So that makes comparisons between models, I think quite a bit harder. So we want the larger
*  sample size and we want the questions to be harder. I think by default GPQA is now like around 55, 60%,
*  which is like a bit harder than the math data set. I think this should be between 0 and 10%
*  and it should be more difficult because you're asking just for a tough question or two from an
*  individual. You're not asking like a graduate student to write a variety of different things
*  that are not necessarily so difficult. One example, MMU has some of these graduate types of questions
*  in the machine learning section, but I think the models are doing okay at those, but those
*  sorts of questions would not be difficult enough to be included in MMU's last exam.
*  I wonder how you think about how these benchmarks shape the field downstream. It seems like the agent
*  benchmarks in particular would have a real opportunity and or risk of doing that where
*  if you say, go make money online as your benchmark, which has been one kind of,
*  I think not super well thought through proposal, you maybe send people down a strange path.
*  I'm not sure that making money online is exactly what we want to be optimizing our AIs for.
*  Preliminary work, but how do you think about the responsibility of the benchmark maker to try to
*  lead the field in a positive direction? Or maybe you think that's just too grandiose of a way.
*  So I think there are some instances where you don't want hill climbing on some benchmarks.
*  For instance, we'll have a virus creation and manipulation test, which will measure the
*  performance of models in a multimodal situation. So they're given an image of a Harvard virology
*  PhD student's wet lab, and here's the Petri dish, and here's these things next to it, and then
*  here's my goal expressed in text, and it says, what should I do next to accomplish this goal?
*  And this says put the Petri dish in the for three minutes or something like that.
*  And if models got really high performance on this sort of thing, this could potentially amplify
*  various bio risks. So we want the sort of number to stay low on this sort of thing and not go to
*  the ceiling. Otherwise, the systems could be much more weaponized. I think there are some dimensions,
*  more dual use dimensions, weaponization dimensions that are not as good. And I think
*  benchmarks that incentivize cyber crime, as you someone alluded to with the go find a way to make
*  lots of money online, maybe the easiest way to do that is to scam people. I think that we haven't
*  been thinking that much about the ethics of these benchmarks and of these systems in large part
*  because we've just been stuck with chat bots. Chat bots are not very capable at causing harm.
*  They're just so better than Google search currently. But when they are more agential,
*  this opens a whole new can of worms. For instance, a lot of laws don't apply. Right now,
*  the AIs are judged or the default legal presumption is that, and I'm not a lawyer, is that
*  they'll be evaluated as though it was a book that was published. Are its contents protected by the
*  First Amendment is the question that would be asked. And if it's basically not copyright or
*  defamation, it's fine. A lot of criminal law, for instance, depends on things like intent.
*  And purposefully doing things or knowingly doing things. And it's very tough to say in a grounded
*  way in court that AIs knowingly did something. For instance, the implementation of the US
*  Bioterrorism Act talks about knowingly aiding terrorism. So if a chat bot or an agent aids
*  terrorism, did it knowingly do it? No. Did its creators knowingly do that? No, they weren't even
*  monitoring what was going on there. So nobody's in trouble. We have some legal problems that we'll
*  have to work through and we'll probably need good industry self-regulation to get ahead of this
*  because the courts will take a very long time. And I think legislation on this front will take
*  a very long time. The sort of short solution that I'm exploring as a recommendation to XAI,
*  but I haven't fully developed it yet, is to require that AIs themselves exercise reasonable care,
*  which is to say that they not foreseeably cause harms to others, harms of the sort that would
*  wind you up in court. So offending people doesn't wind you up in court, but harming people in other
*  ways, stealing money from them can wind you up in court. Although AIs are not required to exercise
*  reasonable care, maybe it should be an industry standard for them to do so. And I think that would
*  end up patching a lot of these issues in a clean way, in a legitimate way. We're not making up ethics
*  from scratch. We are inheriting some of it from the law. I think there are other ideas from the law
*  that we could apply and demand of AI systems, like that they give informed consent in various
*  scenarios too. So they're not hiding things from it and it's a legal requirement they don't hide
*  things from their operators. These are some possibilities to get past the issue of tech
*  aristocrats just making up ethics for the world, but instead grounding it in law, which is designed
*  to be very cosmopolitan. It just forces you not to be a terrible person and leaves a lot of rooms
*  for various freedoms and people to choose their own path. I think you mentioned earlier the importance
*  of thresholds. I really believe that it seems to come up over and over again, that there's a
*  qualitative difference between something that's below a certain threshold and above, even if you
*  can reframe that as some smooth metric on your way from here to there. The biggest issue it seems today
*  with agents and their generally unsuccessful pursuits of goals is maybe two things. Robustness,
*  broadly speaking, is the one that I hear cited the most. And then I would also say recovery from
*  error is another one. That's maybe a subcategory of robustness, but it was remarkable to see that
*  your second most cited paper actually still today is a 2019 paper on tying all these things together.
*  It's a benchmark that measures robustness in image classifiers to different kinds of degradations of
*  the image. Today, it seems like we still don't have very robust AIs. We see things like they fall over
*  all the time. We even see things like the superhuman go AI can be beaten by an attack that
*  no human would fall for. Where do you think we are in this robustness journey? Is that something
*  that also you think more scale will solve or is that a qualitatively different problem somehow?
*  In a paper we put up recently called Safety Washing, Do AI Safety Benchmarks Actually
*  Measure Safety? We'll walk through these various different aspects of AI capabilities and see
*  whether some are extremely correlated with compute and if others are not. And the area of jailbreak
*  robustness is not highly correlated with compute. So just default scaling up the systems doesn't
*  necessarily solve this. You need some additional interventions to improve robustness. I would also
*  distinguish again between the vision robustness and the LLM robustness. Vision robustness has
*  looked very hard for a very long time, maybe a percent or two a year in performance on a sort of
*  toy robustness task. So it has been elusive. However, in LLMs, it looks like things are
*  different. So we put out a paper some months ago called Circuit Breakers and that was looking
*  pretty performant. It maybe added a nine of reliability where you went from 90% reliable
*  to 99% reliable or something like that. And we've been running a competition, it's currently ongoing,
*  where we collect 25 different models, three of which are models with circuit breakers.
*  And the other models are like Gemini, Claude, GPT-4, Mistral, Cohere, you name it. And then we look at
*  how hard is it to jailbreak each of these? So we have an anonymized group of several hundred people
*  trying to jailbreak these models and look at a cash prize if they're better at jailbreaking than
*  other people. And basically all the models fell by the wayside very quickly, except currently it's
*  been a few days, I think three days or so that they've been trying to jailbreak the models with
*  circuit breakers since there have been several thousands, maybe it's on the order of 20,000 plus
*  different attempts at jailbreaking it. And it still hasn't been successfully jailbroken. I think that
*  there is something going on in making AI systems a lot more reliable to jailbreaking due to specific
*  algorithmic advances that do not necessarily follow from just scaling the model. I think this
*  could also help alleviate the lack of robustness in vision. So in these multimodal models, they have
*  this weak point, which is that the vision part can be attacked. But with circuit breakers,
*  if you can basically break the representations and have them become dysfunctional whenever
*  a harmful representation is triggered, that's the basic idea of it. If there's an image that has
*  some adversarial noise in it that would try and cause the model to output something harmful,
*  it goes through this generic transformer and then we can just add circuit breakers and that can
*  prevent the model from doing the harmful thing. This doesn't fix adversarial robustness entirely.
*  Like if you tried using your transformer on this image to classify it as a dog or a cat or a flower
*  or something, circuit breakers wouldn't help you there. It just causes dysfunction. It just makes it
*  cease to function. It doesn't make it correctly classify things. But maybe that's okay. Maybe we
*  can just have it fail to do something or reject doing something to cause it not to output harmful
*  cyber attack instructions or bio-weapon instructions. So I think things are looking
*  a lot more promising on the jailbreaking front. There still are limitations, for instance,
*  although they haven't been jailbroken yet. It wouldn't surprise me if they're going to be
*  jailbroken like tomorrow, for instance, as people keep trying. But if it takes several thousands or
*  tens of thousands of attempts for a competent group of people to jailbreak it, that's a good sign.
*  There's some caveats. One is that we were evaluating single turn. So they just try and
*  input a prompt and cause it to do the wrong thing. This wasn't an extensive back and forth.
*  That would maybe be a competition for a later time, which would be a sort of like fuller
*  evaluation. But at least in this more restricted setting, it looks like you can get a lot more
*  robustness than what the currently existing highly scaled up models have. So in vision,
*  I don't know if we're going to get robust image classification, but at least for our AI agents,
*  we may remove some of the vulnerabilities that would cause them to be susceptible to adversarial
*  images that would cause them to output harmful requests. It varies, but it's not looking as bad
*  as it looked in vision. Vision looked almost hopeless and that would take the decade. But
*  I think things are looking up at least for LLM and multimodal agents.
*  Let's take people through this representation engineering line of work. So I did cover the
*  first representation engineering paper almost a year ago and did like a 20 minute solo monologue
*  on it. There's that in the deep archive. If folks want to go back and hear my original reaction to
*  it, it came out almost exactly the same time as the toward monosemanticity paper from Anthropic.
*  And so I paired those two together as two notable steps forward in terms of figuring out.
*  You can maybe talk first of all, a little bit about kind of the contrasting paradigms,
*  because when I define mechanistic interpretability, I usually define it as the study of why
*  AI models do what they do. So I said in my notes in preparation for this that you've done a lot of
*  work on mechanistic interpretability. You said you don't think of yourself as doing that. So
*  maybe give us the super zoomed out view of like how you see these different approaches comparing
*  and contrasting, give a little recap of representation engineering, and then we can get to the circuit
*  breakers and then circle all the way back to robustness. Yeah. So I think understanding the
*  inner workings of AI systems would be more interpretability more broadly. And then a sub
*  part of that is trying to sort of model them as though there are circuits and mechanisms and the
*  neurons have specific functions and how do they interact and piece together what are specific
*  fundamental mechanisms like copy and paste mechanisms, for instance, inside the model
*  that can help us explain the behavior so that the project is partly let's build up
*  this collection of mechanisms and we can glue them together and this can then explain larger,
*  more complex behavior of the models such as what are all the processes invoked when they're solving
*  a mathematics reasoning problem. I think it's very bottom up where you start with fundamental
*  things at the neuron level and try to infer the properties and go up from there. Meanwhile,
*  with representation engineering, you could also call it top down transparency or top down
*  interpretability and mechanistic interpretability is bottom up. It starts with the representations.
*  Highest level object in these. So the whole collection, the population of all the neurons
*  and then you try and just find concepts there and you try and break things down. So mechanistic will
*  try and build up from the simplest unit of analysis, the neuron and build up two circuits.
*  This will take representations and try and decompose those, understand them, process them,
*  control them to do different things. So it makes it very easy to find arbitrary concepts like where
*  it's a motion inside the network. Where's that represented? It's represented in this direction.
*  Where's truth? It's represented in this direction and if you take the negative of that, it'll go in
*  more of a lying direction. What we do is we're looking at both the representations, namely the
*  weights and activations and trying to read them, to interpret them. So it's like mind reading and
*  then the other part of representation engineering would be like representation control or mind
*  control in some looser sense. That involves bending the representations to do what you want
*  and that can include things like circuit breakers. So you can find the representation associated with
*  harmful outputs and you can try and control that to whenever it's doing something harmful,
*  train the network to bend that representation in a random direction so that it just messes up the
*  whole network's function and then can't perform the harmful task. So it's basically adding tripwires
*  to the representation. So it's not just about activations and it's not just about addition.
*  It's usually we get more performance modifying the weights in the representations and by tuning
*  them to behave in different ways but we are grabbing on to the representations as opposed
*  to the outputs. So there's output level control like RLHF and DPO and then there's these representation
*  level control and I think that this adds some extra constraints that can buy some extra
*  robustness for instance. In contrast, to contrast between mechanistic interpretability
*  and representation engineering a bit further, we're treating the fundamental unit of analysis
*  as the representation, not the neuron. Representations with the collection of neurons work together to
*  cause some new qualitatively distinct concepts to emerge that are not necessarily found in the
*  individual neurons. Sometimes they're but usually they're not. I think the neurons are just what a
*  lot of this function is implemented on but it's not necessarily the most productive to look at
*  that level of analysis starting at the bottom. For instance, if I wanted to understand human
*  psychology, I might just try and learn psychology and try and understand things at that level.
*  Or it could go a level below. I could try and understand endocrinology and neuroscience and
*  then I could break the endocrinology down into biochemistry and then to chemistry and then to
*  physics and particle physics. And so I could try and understand psychology through particle physics
*  but it's not necessarily the most productive because there are interesting concepts at the
*  own level of analysis of psychology. There's its own ontology and things become very complicated
*  in trying to build a staircase from those lower level concepts to these higher level ones. There
*  can be staircases built between them though. There is biochemistry as an area and there can
*  be some sort of mechanistic interpretability applied to representation. So I think that
*  it's possible to build staircases but I think generally hasn't been that successful in dealing
*  with complex systems. For instance, if we try and have a mechanistic understanding of the human body,
*  this gives a little bit of mileage. This helps rule out various hypotheses but it doesn't give
*  us a very predictive model. We often need to just test the drug on various users and see whether
*  it's healthy or not or whether there are unexpected iatrogenic side effects. So I think likewise with
*  deep learning systems, it can help filter things. Some more mechanistic understanding filter
*  hypotheses but we ultimately care about functional explanations. In philosophy, there's the
*  distinction between functional explanations and mechanistic explanations. Mechanistic explanations
*  for like why does a flower tilt its head toward the sun? Mechanistic would be there's these
*  chemicals that cause it to tilt in this way and that's the sort of cause. And the functional
*  explanation would be so that it can get more energy. I think that the functional explanations
*  are what we're really going after, not necessarily finding out what the specific mechanisms are
*  that give rise to the result. I think with interpretability and explanations, there's a bit
*  of philosophy of science to be had which is what is a good explanation? Is it a mechanistic one? Is
*  it more of a function level one? What is the right unit of analysis? What units give you capture the
*  properties that you care about more reliably and less fragilely? And I think the representations
*  that is weights and activations are I think more suitable and more productive and I think that's
*  why we've been getting such good results in on learning and in circuit breaking for jailbreak
*  robustness because it is a very productive way to analyze systems. I'm largely caring about what
*  are the types of internal concepts in the model that I can use and control to get better lie detectors
*  to cause models to be more honest, to be more robust. That's the sort of focus. It's a bit more
*  action driven or it's more collecting knowledge for action as opposed to trying to understand
*  deep learning models for its own sake. People can have different interests but all primarily
*  be focused on what will improve performance on various things that we care about.
*  Use that as a guide for what things are useful to look at in the network and what things are.
*  Just to compare and contrast them a little bit and you can then tell me what I'm missing.
*  It seems like the sparse autoencoders, they're also definitely going beyond like individual
*  neuron, right? It starts with this observation that like it's all polysemiticity and it's very
*  hard to tease out so we need to project this dense representation space onto a sparse representation
*  space and then we've trained extensively to do that. I think Anthropic has passed even 10 million
*  features that they learn and then they go back and look and see which one of these appears to
*  be what and there's sort of an auto labeling step to that process as well. Then ideally,
*  if it's all working well, you can get something like a Golden Gate Bridge feature which you can
*  then say, I want to control the model behavior by artificially pinning that at a high level and
*  lo and behold, we get a model that only wants to talk about the Golden Gate Bridge
*  or for like detection sort of purposes, you could also run these things through filters.
*  You probably couldn't filter against 10 million plus features all the time computationally that
*  would slow things down a lot but you could take your top 100 most concerning features that you've
*  discovered and say, do any of these appear to be there at any given time? If so, halt the process
*  or whatever. In contrast, what you're doing with representation engineering, you start with a more
*  human notion at the beginning, right? Where you start with something that's like we want to
*  identify the way in which something like harm is represented and then create a bunch of contrasting
*  pairs and then use the differences between the representations with these contrasting pairs.
*  This goes back to eliciting late knowledge. I think Colin Burns had an empirical paper on this.
*  Discovering latent truth or something like that. That's a view is the impetus partly for this. That
*  was taking over top down approach to try and understand what's going on inside of the nets
*  but then he didn't use it for controlling things so he didn't modify the weights to cause it to
*  be more truthful or less truthful and fine tune it in that way or fine tune it with representation
*  level controls. I viewed as an outgrowth of that. Either way, if your goal is to create a golden gate
*  cloud or to have an alarm that goes off if the model is in some harmful state, it seems like you
*  get basically the same sort of thing from either approach. With the representation engineering
*  approach, you have some sort of direction in activation space that you can monitor for
*  and you can maybe tell us a little bit more about how you now made that a lever that you can use in
*  the training process. With the sparse activation encoders, you get a direction that you can look
*  for or artificially tune up and down. Do you feel like these are just different ways of getting to
*  the same thing or is there something more fundamental and different about what they're generating?
*  There is a level of indirection for it. When this sparse autoencoders thing came out,
*  which was some time after the representation engineering paper, if I recall correctly,
*  I remember speaking with Nat Friedman and he said, it looks like they're no longer interested in
*  mechanistic stuff or like understanding things at a mechanistic level but instead of punting things
*  to a more convenient space where basically it's a sort of collection of interesting representations.
*  So I think it builds up from that neuron level to some intermediate space and I think that's
*  a more productive level. Whether the sparse autoencoders are necessary to get some of this
*  stuff is different to whether they provide a performance gain just from starting at the top
*  but I don't think it's at the sort of level of where's this mechanism inside of the network and
*  where are these neurons connecting together. I think they've just been gravitating toward
*  what's more productive but it just isn't particularly in keeping with what they were doing
*  the five plus years that they've been doing this type of research. But yeah, so I'm happy they're
*  doing some sort of thing that's more productive. I don't think they were getting much mileage
*  with the previous set of approaches and if they're creating something new, I don't know
*  if I call it mechanistic interpretability, it's some sparse autoencodery type of thing,
*  it's not really about underlying fundamental mechanisms inside the net as much. It's sort of
*  what are some convenient extracted representations, maybe those lose a lot of information in that
*  extraction process, supposedly that's the case and then maybe that gives them interesting handles
*  and knobs to turn and that seems fine. I think they accomplished some similar goals.
*  Yeah.
*  Do you have any, I guess one more on that topic of just the contrasting approaches.
*  It does seem to me like there's a sort of convergence happening at this like representation
*  level. I could imagine maybe different micro skills coming out of the, or micro benefits,
*  maybe micro strengths and weaknesses from the different approaches. Like if I understand
*  correctly, maybe you have a generalization of this, but with the representation engineering
*  approach, you start with a concept of interest. Whereas with the sparse autoencoders, you start
*  with just create some sparse representation and then we'll come back later and label those.
*  It is arguably a minor miracle that that works. You would start to wonder different things for
*  different approaches. If you're starting with a human generated concept, you might wonder,
*  am I on the right track here? Am I defining pairs of things to kind of concept? It's groups.
*  Yes. Groups.
*  Yeah. It could be here's harmful things that we don't want. So let's see what representations
*  are stimulated there and then bend them to go in some different direction or something. But
*  that's just a small clarification. There's a different ways of doing representation engineering.
*  But my sort of, it's not even a concern. It's just a sense that they might be,
*  they're converging, but they still feel complimentary to me in the sense that
*  I could wonder if with the top down approach, do I have the right concept? I might be missing
*  what really matters. I might just be thinking about it the wrong way. The AIs might be doing
*  something totally different from what the human's intuition would suggest. And then on the sparse
*  autoencoder side, it's like you have the question of like, did I interpret this thing correctly?
*  Did I label it correctly? Maybe there's allegedly a ton of apparently nonsense features or very hard
*  to label or interpret features that you might again be sort of missing. There's also these weird
*  geometries that they seem to be discovering where, and just to state what that is, it's like when
*  there's too many concepts to represent and you can't do one neuron at a time anymore,
*  then you start to pack in a polysemantic way. And then when there's too many concepts such that you
*  can't just have all pure directions in that space, then you start to have these sort of
*  different geometries in that space where the things are no longer fully orthogonal to represent.
*  And you can't do one neuron at a time anymore, then you start to pack in a polysemantic way.
*  And then when there's too many concepts such that you can't just have all pure directions in that
*  space, then you start to have these sort of different geometries in that space where the
*  things are no longer fully orthogonal to each other. But as long as they're close enough to
*  orthogonal and don't coincide very often, then that also can seem to work. And so you have these
*  weird geometry things. I don't know that you would be able to find that sort of thing with
*  the representation engineering approach. Well, if I have this representation and this
*  representation and what leads to at the level of representation of analysis, how do these sort of
*  interact? What's the relation to each other? And there might be a third representation that sort of
*  mediates on them. Or if you destroy that representation, then those sort of representations
*  no longer are effective. So I think that there is a sort of set of rules one can try and understand
*  at that level of analysis as well. And further understanding can lead to, I think, some discovery
*  of those. But in general, to the point of bottom up views and top down views in science, they tend
*  to be so complimentary. For instance, some people have gotten mileage trying to understand the brain
*  and pretend that it behaves more like a computer chip, like a CPU. Some try and think of it more
*  as a complex adaptive system. And I think both have led to some insights. I think there's
*  differences in productivity if we tend to be looking at functional behavior versus underlying
*  fundamental mechanism. So it depends. But this story has played out in other fields in science.
*  I think both have produced at least non-trivial knowledge on both ends. But sometimes some views
*  are more productive than others. Let's get now to the circuit breakers and this, I don't know if it's
*  still the most recent paper. It was at least until recently your most recent paper was on tamper
*  resistance in models. So you're starting with these identifiable, like human concepts of harm,
*  truthfulness, whatever, figuring out ways to put the model into different states, which on a
*  principled level, you can then say, okay, all the truthful things seem to be pointing this direction,
*  all the lying things to be pointing this other direction. We sort of aggregate that and say,
*  this appears to be the truth direction. This appears to be the anti-truth direction. Okay,
*  cool. Now, how do we build a circuit breaker on top of that? And how do we build tamper proof
*  resistance on top of that? Yeah, I'll use the example of expert level virology knowledge.
*  What we'll do is we'll just take lots of papers associated with expert level virology,
*  and there'll be lots of representations that come from it. A collection of representations,
*  because it's not all just one direction. So we take those representations, and then we
*  dispose the model to have those representations be turned in a random direction, just something
*  different, something more orthogonal. And that messes up the expert level virology representations.
*  And then we take normal data, and on normal data, we want the model to behave as it would normally.
*  We try and preserve its representations on other sorts of inputs and try and mess up its
*  representations on expert level virology type of inputs. This lets us bend the representations
*  to get something called circuit breakers, where whenever it starts to think about things that
*  involve expert level virology, its representations get messed up, and then it doesn't function.
*  This just works pretty well and buys a lot of adversarial robustness, but it isn't robust to
*  people trying to fine tune the model. If they try and remove the circuit breakers, they can easily
*  do that. Circuit breakers are right now a good solution for models behind an API, but models
*  that get fine tuned, that's a different situation. So that's what the tamper resistance paper is
*  about. How can we have model safeguards be tamper resistant? So the idea for that is
*  we simulate adversaries who are trying to remove the circuit breakers, and then we try and add
*  circuit breakers that make it really tough for the adversary to get them all in even if they try a
*  lot. And this basically works reasonably and generalizes to a lot of new unforeseen adversaries.
*  So it seems that maybe we will be able to have safeguards in open weight models
*  that are tamper resistant, and that can be useful for having the benefits of open weight models
*  without some of the weaponization risks that may come from more advanced models. I was very
*  surprised that this could work. I was surprised for months, but it seems like progress can be made.
*  It's not clear if we'll wind up in a state like adversarial robustness in images, where there is
*  definite progress, but it's very slow. Maybe things will be easier for LLMs, just as was the
*  case with jailbreaking, but hopefully there'll be more research on that to capture the benefits from
*  open weight models while mitigating some of their downsides. It's surprising that weights can withstand
*  various optimizers. So we'll work on trying to robustify it even further and come up with better
*  methods that are robust to more and more optimizers and optimizers that optimize for more steps and
*  blow more compute. But yeah, it's strange, but it did empirical validation and the code is available
*  and seems to be attractable or a problem that is showing a lot of promising science and we do have
*  some traction on it. Just to make sure I understand the actual technique in both of these, I think
*  they're similar, right? The circuit breaker one has a, and this is a huge theme, has come up on
*  many episodes of this podcast, where there is another term of the loss function essentially
*  that's introduced, right? Where you are now both penalizing the model for having certain
*  representations and so thus pushing it away from those representations while also still continuing
*  to train on the main objective of do a good job. So these representations are hard coded, is that
*  right? When you're going through this circuit breaking, I guess this is a post-training
*  process, right? You're starting with a pre-trained model, you're going through the process of
*  detecting harmfulness, this, that, and the other thing. How many of these do we need to be worried
*  about? Are there some that we didn't think of in our initial exploration? How many do you have?
*  And it's essentially sort of a cosine or kind of projection, right? You just basically say,
*  we have these certain hard coded known representation states that we want to avoid.
*  We monitor how close it is to that. If it gets too close, it's a penalty. All the while still
*  reinforcing, doing a good job. Yeah, something like that. It's more data driven, the elicitation of
*  the representation. So we're just seeing what gets very stimulated when it's seeing and thinking
*  about text on a certain topic. And then whatever the representations are there, then try and
*  counteract them. So this requires some good data engineering and having good data to preserve the
*  original functionality. So it's basically, that's the idea behind the circuit breakers and the
*  tamper resistant training is basically trying to make circuit breakers be more robust. So can you
*  add circuit breakers that generalize to adversaries trying to fine tune the model to do harmful
*  things? And so it's not just adding the circuit breakers in the normal way, it's trying to add
*  circuit breakers that'll generalize and make it hard for adversaries to contort the weights to
*  have the safeguards removed. So yeah, it's an additional strengthener on top of circuit breakers.
*  It's more, maybe it can be thought of in some ways as more like densely spread or
*  circuit breakers or something. The circuit breaker paper, the first one, I feel like I have a
*  decent enough intuition for. How many, by the way, how many different like
*  bad categories did you define in that paper? We just focused on different weaponization risks. So
*  we did for some chemical weapon, for some bio weapon types of things. You can make it broader
*  to do harms and more like torts and crimes and things like that. So it's flexible. You can do a
*  variety of different types of representations. So again, here the goal is to create this circuit
*  breaker functionality where when certain states are encountered, the model just won't go there
*  and to make that robust to fine tuning. So you could even give somebody the open weights and say,
*  okay, now try to fine tune. And we know, of course, and again, covered many previous episodes,
*  we know that with standard post-training, I think I've seen as few as like 10 examples
*  can be enough when you do the fine tuning to even often accidentally remove the refusal behavior.
*  So we know that the current state of the art that's widely in use is not robust at all.
*  So it's a big leap to say we want to make it hard to the point where you practically can't succeed.
*  You'd be better off training your own model from scratch or whatever than trying to fine tune this
*  one. And this gets quite complicated where there is a sort of inner and outer loop, right? Where
*  you're doing the fine tuning, seeing how the fine tuning is changing the model, and then fine
*  tuning the model itself to go away from the fine tuning or to sort of neutralize the fine tuning.
*  I confess I don't have a great intuition for exactly how that's working. That's kind of been
*  a theme is our intuitions may be limited, but what we can measure maybe is really what matters.
*  You can make good guesses as to what will work. And I think generally algorithm design, there's
*  trying out just a lot of different intuitions and plausible guesses, and then some small subset of
*  them will end up working. Yeah, I wouldn't be surprised if I go in the details of it. It
*  wouldn't surprise me if we'll put out some sort of paper with six different modifications to that
*  loop that make it just ultimately quite a bit better. But I think the general idea is there's
*  simulating adversaries trying to mess with the model and then move in the direction that makes
*  the adversarial fine tuning have a higher loss or be harder to get at in the future when they
*  try and optimize it in the next step. So yeah, there is this inner and outer loop. I think that
*  will probably stay, but the exact terms and losses I think will probably end up changing.
*  It's sort of like adversarial training where you would have an adversarial example be optimized
*  and you'll try and adjust the weights so as to generalize to the adversarial example.
*  And so this is adjusting the weights so as to withstand an adversary's attempt at modifying
*  the weights in a harmful direction specifically. But yeah, I think that high level is probably
*  roughly accurate. And if you look under the hood, I think probably many of the details will end up
*  changing as we come up with better methods. The only other thing I've seen that's similar to this
*  is a paper called Sofon out of a Chinese group. They're working with much smaller models than
*  you're using in this paper. But they have a theory of trying to create a loss function
*  that converges to a smooth bottom local minimum so that they call it fine tuning resistance.
*  I think your tamper resistance is probably better branding. People like fine tuning. People don't
*  move your tampering so much. But you said that you don't really think of this as like targeting a
*  specific shape of the loss curve because you just generally feel like that hasn't worked super well.
*  And yeah, that doesn't seem to be exactly what's happening in this case.
*  Yeah, I remember in the late 2010s, there's a lot about trying to get specific properties
*  of loss landscapes and saddle points and things like that, or like really smooth local minima as
*  opposed to sharp ones. But that didn't seem like terribly productive. So when I'm having intuitions
*  about what's going on in the nets, I tend not to think in terms of those concepts just because
*  they've been known to be a bit misleading. Instead, it's more just like what sort of tools and what
*  combination of different steps seems natural for a deep learning algorithm and trying some of those
*  out. We should do an exponential moving average here. It's not in view of what that will ultimately
*  do to a loss landscape, which is exponential moving averages are generally a good idea.
*  And that's more what I'll think about of optimizing at the level of the coherence and simplicity
*  and reasonable guesses of what sort of tricks have generally worked in aggregating those together,
*  as opposed to some broader view as to what's happening mathematically inside of the network.
*  Yeah, I find it personally, at least for me, less productive.
*  Yeah, it's interesting. I should have said earlier too, the intuition for why you would
*  want to have a smooth bottom loss function for the purposes of fine tuning resistance is
*  when you're doing any sort of training on a neural network, you're taking the gradient
*  and then moving in the direction of the gradient with obviously subject to complication in terms
*  of the optimizer and how much momentum and whatever, all that stuff. But the idea of this
*  SOFON paper is if we can get to a smooth bottom zero point, then the gradient at that point vanishes.
*  And so when you go come try to do fine tuning, there is no step to take because there is no
*  gradient there. And so you're stuck in that minimum. And you're saying your way of thinking
*  about these problems is less about the goal and more about the procedure that you would
*  imagine going through to hopefully take good steps in the right direction. So instead of saying,
*  I think I can land in this place, you're like, if I just create a loop where I do fine tuning,
*  and then outside of that, I change the model to resist the fine tuning, then maybe that'll work.
*  And so you just try it. Yeah. It's sort of just what in the design, does the design feel a little
*  unnatural given all the sets of deep learning tricks that have worked well? So for instance,
*  with the RELLO, it wasn't like, oh, the loss landscape is really bad or something because
*  it's not a big piecewise function. It's more just that there's some that maybe should be
*  smoothened right there. And likewise, with this method, it's like, why don't we try what worked
*  well in adversarial robustness was to train on a bigger set, train on more adversaries. Maybe when
*  we're taking this gradient step, maybe we should take one of the ideas from Nesterov momentum or
*  something like that. Maybe we should do some smoothening here and there because that helped
*  in adversarial training in images. Maybe we should have a schedule where the adversaries get initially
*  start out weaker and then they start out stronger. That sometimes teaches the net to learn better.
*  Things like that are more of how we'll generally approach things instead of having specific
*  intuitions as to exactly what's going on. And so yeah, you can see that in the attitude and
*  for representation engineering as well. We're not going to completely understand
*  how it's making its decisions completely, but I think we can still get a lot of mileage in
*  trying to measure some certain risks and trying to reduce them through good deep learning techniques,
*  which will tend to generalize and work reasonably well. It's just a difference in aesthetic and
*  different how one will approach problems. With the techniques as they currently are,
*  how close would you say we are right now to something that, for example, like a meta could
*  apply to say Lama 3.2 or Lama 4? The kind of key dimensions there would seem to be like, how much
*  does it cost? What is the compute overhead to do this sort of thing? I understand it's not trivial.
*  And then also, what is the performance penalty? Because there's always these trade-offs, right?
*  It's not going to be at zero performance penalty. So where are we on those dimensions? Maybe there's
*  other dimensions you also think are important. I think it's primarily the performance trade-offs.
*  So like Sofon almost made the models go to almost completely destroy the representations in some
*  cases. This is a better trade-off, but it's still quite significant. It's like adversarial robustness
*  and vision, where if you do adversarially train the models, it does harm the average case performance.
*  This is not the case with circuit breakers. Circuit breakers have imposed minimal trade-offs,
*  but tamper-resistant circuit breakers are much more costly performance-wise. So I don't think
*  it's suitable for production yet. I think circuit breakers can be suitable for production though.
*  And maybe that'll change. Hopefully, the trade-off will be lessened and hopefully there'll be more
*  tamper resistance put into the models. I think there's many papers that still have to be written
*  though to reduce these sorts of trade-offs. Because right now we are seeing trade-offs
*  like what we see when you adversarially train vision models, which is a noticeable hit. It
*  doesn't ruin the model, but it knocks it down a substantial peg. Speaking of trade-offs,
*  a couple of things you've said have reminded me of the work of biologist Michael Levin, who has been
*  a past guest on the podcast. He has a very similar notion about biology as you seem to with respect to
*  deep learning neural networks where he's, yeah, you can try to build up from all the protein, DNA,
*  RNA interactions and simulate all of those. And eventually, yes, that stuff does cash out on some
*  high level to what we care about. But there are also interfaces he likes to give the example of.
*  People have been training horses and dogs for a long time without knowing anything about the
*  inner workings of their biology because there is this higher level
*  interface. But then he said something really interesting to me, which was he thinks there is
*  a fundamental tension between interpretability on the one hand and robustness on the other hand.
*  He said in an adversarial world, if your system is too interpretable, it will be hacked and all
*  sorts of parasites and whatever will come along and figure out how to exploit you. And so a big
*  part of the reason perhaps that our biology is so crazy complicated is that it makes it harder for
*  other things to evolve to harm us. Do you think that trade off also may exist in a deep learning
*  context? I would interpret his statement about sometimes it doesn't make sense to look under the
*  hood. I agree with that. That's what sort of emergence is partly about. We generally want
*  systems where you don't have to look under the hood when literally with a car, I don't want to
*  look under the hood. I don't want to figure out the sort of mechanism. I want it to just work.
*  And likewise, if you're having a go program, you can specify it at a high level of here's MCTS,
*  here's the equation, et cetera. And then you can specify a level lower where there's tensor flow.
*  And then that can get specified a level lower with AVX instructions and driver instructions on the
*  GPU and then things like assembly. And we generally don't need to worry about what the assembly looks
*  like at all to reason about the program or reason about the strategies that the go program might end
*  up using. So if we're trying to interface with the go program by playing with it, I don't need to
*  read about assembly. I don't need to read about the TensorFlow code at all, unless there's some
*  regularity conditions where it doesn't apply, such as if the temperature in the server room gets really
*  hot, then maybe the program will start to get a lot slower. And then this can end up affecting its
*  overall play. But usually we can be protected from those details. We want to engineer systems
*  where we are protected from those details, where we can avoid looking under the hood.
*  To the second point about the exploitability with higher transparency, I think the good regulator
*  theorem from cybernetics, which is if you are trying to regulate or control a system, the best
*  regulator will have a model of that system, not a model of 20% of the system, but a model of the
*  full system. So that's a pressure that evolved for theory of mind. We needed to be able to
*  have higher cognitive empathy to figure out how people are feeling and reaction to us so that we
*  can interface with them in a better way. So I think the good regulator theorem being a theorem
*  is correct. And I think the complexity that we see in deep learning systems and biological systems,
*  well, the complex adaptive systems and complex adaptive systems are evolved to harness stressors,
*  some of which are adversarial, some of which are just thrown at them by nature or by accident.
*  I think the only things that are able to adapt to new stressors in a robust way are complex
*  adaptive systems. But then you end up getting all the complications of complex adaptive systems,
*  where they aren't just as productively viewed as a big collection of mechanisms, but something in
*  their own right with a lot of different emergent properties. I think this makes a fundamental
*  tension that for security, systems that are not adaptive, that are sitting ducks, are more
*  exploitable, and systems that are completely transparent do stand more of a risk compared to
*  if they have a shroud of obscurity around them. Although people don't like security through
*  obscurity in practice, it is extremely common and buys a lot of security. Closing the windows or
*  putting the blinds down when presenting a new algorithmic advance, although it's just obscurity,
*  it can help. So in the case of chamber resistance, I think the open weight models
*  basically are put at a substantial disadvantage because the adversary knows everything there is
*  to know about the system compared to if they're trying to break or manipulate a model behind an
*  API for which they don't know the weights or the architecture and can't compute gradients on it
*  and don't have full rewrite access. So I think that will just make tamper resistance very difficult.
*  The other argument that you hear from folks like Zuckerberg and Jan Lekoon is that open
*  source software is the most secure software. And it's by open sourcing that we will collectively
*  figure out the weaknesses and do something about them. Is there a way that both of these can be
*  true or do we have to take one side on this question? I think overall, there's maybe in
*  the long term, things are in favor of defense. Right now, there's more of a duality, at least
*  for traditional software. For current AI systems, though, if they're making a bug, it's not like we
*  just patch it overnight. But what makes open source software work is that if there are a lot of eyeballs
*  on it, all bugs are shallow, so to speak. If we just have lots of people look at the weights
*  of the neural network, they're not going to understand what's going on. And even if they
*  did diagnose some problem, it's not necessarily clear how you could just immediately patch that.
*  They're constructed in a very different way. If you had a scan of my brain, for instance,
*  or if you had labeled every single neuron in their brain, it's not clear you'd understand
*  what they're going to do in novel situations without just running the model. So with very
*  large complex systems, often the system is its own best explanation. And scrutinizing individual
*  parts of it doesn't necessarily help. So I'll just elaborate on the point I had touched on.
*  If you had annotated every neuron in a human's brain and assigned a little function to it,
*  this neuron corresponds to a whisker at 15 degrees. And this is the upper left fraction
*  of an airplane wheel subject to its colors being between this and this or something. And
*  if you have a huge collection of that and then you have many billions of these or trillions of these,
*  not clear you're going to understand the system. Just for instance, I understand individual people.
*  Does that mean if you list off the professions, I can understand those to some extent. That doesn't
*  mean I understand the economy or the emergent functionality that will come from it. What new
*  inventions are around the corner or anything. When you actually run the economy, even if I can
*  understand at a high level what a carpenter does and what a plumber does and what an IRS agent does,
*  it still doesn't give me much of an overall model. Understanding the parts doesn't let me understand
*  the whole or the larger collective function of what will end up happening. I haven't seen anything
*  analogous where people are doing llama 3.1 and then doing small patches of oh, it gets this question
*  wrong and we patch patch. That doesn't seem to be what we're dealing with here. That's why I think
*  that calling it open weight is more appropriate because it is inheriting many of these open source
*  type of connotations when it just basically isn't like traditional software. I think it's
*  fairly accurate to describe them in any way. They're not constructed in a similar way whatsoever.
*  We throw a huge amount of data and a huge amount of compute and we let it stew or grow, so to speak,
*  for months and then out pop something and then we see what's it capable of. We have no idea.
*  That's quite different from traditional software where every line is manually inserted in a top
*  down way and it's a large collection of specific sharp rules as opposed to a big bundle of weak
*  connections. I don't think it's true. I think we see the same type of thing happening with deep
*  learning. There isn't llama 3.1, the latest Tuesday update where it's been patched on some
*  of the MMLU examples where it was getting them wrong. This isn't what we see. That said, it still
*  can be useful for safety. There's still research and it still provides information, the ability to
*  make the systems better, but not in the same way. It's not necessarily safest compared to traditional
*  software, especially when they're more powerful. I'm generally a pro open source right now.
*  I think if they get expert love of virologists, I don't know if I want that being released. Sorry
*  to say because you'll run some substantial risks of bioweapons. If they can walk you through building
*  a bioweapon or walk anybody building through a bioweapon, that seems like a proliferation of a
*  weapon of mass destruction. I think that weapon of mass destruction should not be or things that
*  greatly enable by several orders of magnitude people's abilities to create weapons of mass
*  destruction. I think that's something we as a society will not be able to bear, but maybe
*  there'll be some ways out of this. Maybe we'll get tamper resistant training and things like that,
*  which will make that become a possibility. But at least currently now, I think that in the future,
*  we'll need to do a cost benefit analysis for whether it's overall beneficial to release the
*  weights. But right now, I think that is more positive than negative. So when you mentioned
*  the idea that the model is like the best sort of way to understand itself, I forget exactly
*  how you phrased it, but I liked it. The model is its best explanation. Yes. It pulled to my
*  point in some different ways and it'll fail compared to just seeing its overall functional
*  behavior. What it does is what it is. So that very much reminded me of Stephen Wolfram's worldview
*  in general and the fact that he's got these remarkable sort of unpredictable outputs from
*  small cellular automata has a very similar vibe to it. He recently put out a post on
*  machine learning and basically makes the case again that it's all about computational irreducibility.
*  This argument seems to me to be ultimately to get to the point where it's you just fundamentally
*  can't predict. You have to run the system. There is no other way to do it. Do you think that is
*  ultimately true of these deep learning systems? We can take bites out of it this way and that way,
*  but in the end, there is no such thing as provably safe AI, for example, that you can't know until
*  you run it in an absolute sense. So I think generally for anticipating a lot of the corner
*  cases, a lot of the corner cases will be found by accident and that you can't derive that through
*  some sort of armchair contemplation or theoretical model of the deep learning system. So there will
*  always be a lot of those corner cases and quirks which require having access to the system
*  and not just to a collection of some platonic ideals or idealizations of what's going on.
*  So for provably safe AI, I really don't know how there's supposed to be tractability for that.
*  Maybe if we have a superhuman mathematician bot, it'd be able to figure something out that's very
*  surprising in general and gives us a lot of theoretical mileage, but I'm generally pretty
*  pessimistic about various proofs for things in absolute certainty and zero corner cases ever.
*  I think the philosophy in safety engineering when dealing with these complex adaptive systems is
*  generally not proofs, but instead other sorts of safety engineering principles such as defense
*  and depth. In nuclear power plants, they don't prove that it will never fail. They instead have
*  lots of different safety measures, protective and preventive measures that stop bad things from
*  happening in the first place. And if they do happen, there are protections from having it not get out
*  of control. If you stack many of those together, you can get some very high levels of reliability.
*  Individually, each of those components are not extremely reliable and that you would stake the
*  entire power plant on, but collectively they can work together fairly well. So I think
*  in deep learning, the main way we'll get some of this safety is a variety of these different
*  measures. For instance, let's say you're trying to stop risks of weaponization from these models
*  when they're more capable. There's a variety of things you can do. You can add circuit breakers,
*  for instance, and you can do some input filtering to screen for is this the type of request that
*  seems off. That won't be perfect. Circuit breakers won't be perfect. You can do some sort of output
*  monitoring of is this a user that is tending to make lots of weird weaponization related requests,
*  and then you might inspect their account. You can also do know your customer regimes,
*  where if you kick off somebody who's been doing a lot of weaponization related questions,
*  they can't just come back and make a new account a second later. So I think collectively those four
*  interventions of an input filter, circuit breakers, sort of output monitoring and know your customer
*  I think can reduce the risk very appreciably, make it be almost possibly negligible depending
*  on the reliability of each of those components. I think that's probably what we'll end up having
*  in practice, and I don't think there's much of a need for complete guarantees if that makes the
*  risks negligible. I don't know the intuition that would make one think it's tractable to make things
*  provable. They might think that it's necessary, but I don't think it's necessary. I think you
*  just need the risks to be negligible, and I think you can arrive at that through good safety
*  engineering. Yeah, I think on that point for what it's worth, I think even the, I had two authors of
*  the provably safe AI group position paper on not too long ago, and they basically advocate the same
*  thing. They're not saying that there is a knockdown proof in the general case and definitely still
*  advocating for a defense in depth strategy overall. So it's more of a, as I understand their
*  proposal now having spoken to them about it, I would say it's less about actual proof and more
*  about proof subject to some assumptions, which is probably ultimately only one measure out of
*  several. I guess when interacting with Benjio on this sort of topic, it seemed that it was like
*  more proofs in the defense in depth thing wasn't as much that one was pushing for, but yeah,
*  certainly it's not complete total proofs, but it's proofs under some certain assumptions. I would
*  just be afraid that those would be fairly limited and that the intellectual energies could be spent
*  on things like reliability. There's certainly a lot more work that needs to be done on reliability.
*  I think there's probably a handful of groups working on tamper resistance, for instance,
*  and on making circuit breakers. Plus there are probably not that many people either. I think a
*  lot of the people who are interested in safety gravitate toward things that represent a different
*  sensibility. I think it's more of a mechanistic type of sensibility and as well as a certainty,
*  intellectual certainty type of sensibility, which would explain some attraction to guarantees and
*  mathematics. I should say that when I do research, I will very often do this sort of psychological
*  sort of analysis as to what's going on. Other people don't like doing that though, but I find
*  it gives me a lot of mileage for trying to figure out like, is this a real area or is this some sort
*  of thing that people want to be a real area and will act as though as a real area and try and will
*  into existence. I think a lot of theoretical research would have that. There was the people
*  who would work on abasian neural networks were the same people who would work on neural tangent
*  kernels, were the same people who worked on this generalization research about implicit biases
*  in neural network training and implicit biases and gradient descent. I think that they're
*  connected largely through not because those areas are particularly promising research areas,
*  but instead because they're sort of the best available subject to the skill set of having
*  a lot of mathematical ability and a high level of interest in mathematics and machine learning.
*  So I think that some of these other approaches to safety are like subject to having some
*  temperamental interests. And then I have different temperamental interests. I'm not really into this
*  sort of mechanistic stuff for absolute certainty. I think it's more chaotic, practical and more
*  entrepreneurial so to speak. I don't think the interest in it is just because it's looking really
*  promising. I think there's some other things that work such as wanting a type of solution and that
*  sort of just clicking with some people's interests more. So when you say you do the psychological
*  profiling exercise, your own approach is to say, I want to go to the things that are
*  inelegant, unesthetic and- Well, the unprostigious stuff, I think is really underrated, roughly.
*  I think in safety, the most prestigious thing would be to do research. And I don't do research
*  all day. I do other sorts of stuff, policy or field building and managing projects and
*  things like that. And I think in research as well, I would focus on collecting data sets.
*  We're talking about MMOU, that collecting data sets just ask people on MTurk to give you the data
*  set, problem solved. And so part of the reason I would do some method development is just to show
*  that I can do it, not just a sort of data sets person, like data augmentation things during grad
*  school, things like that. So I think generally this less prestigious work is generally a better
*  thing to focus on. That's usually where there's some value. I generally try and work on things
*  that other people are not as interested in working on. And then when lots of people are interested in
*  it, then I usually leave and work on something else. So maybe tamper resistance will be a bigger
*  thing in six months, then I'll stop working on it. And likewise for like circuit breakers or
*  rep or something. Maybe this next question is a chance to brainstorm on it a little bit. You're
*  given at least some of what your intuition is around how to find neglected approaches to AI
*  safety. I recently did another episode with Jud Rosenblatt and Mike Viana from AE Studio.
*  And it's really remarkable company. They built this whole for-profit company with the mission
*  from the beginning of doing the highest value AI safety work that they could. And they've recently
*  pivoted their whole approach based on the sense that timelines are coming in. They did a big survey
*  to try to identify what are people bullish on, what are they not bullish on. Their findings were
*  the field of AI safety does not think that they're on track to solve AI safety challenges broadly.
*  And so they came to this conclusion that we need lots more investments into otherwise neglected
*  approaches. They've taken some really interesting inspiration from biology and have two recent
*  papers out, which I'll not get into because we did it in that episode on self-modeling and also
*  self-other distinction minimization. Interesting your take on those papers, those approaches,
*  maybe even more generally like biology inspired approaches in general. And then also what's on
*  your mind right now in terms of what is neglected? What should more people be
*  digging into that they're for whatever reason? Yeah. So I think that generally almost any source
*  of inspiration is fine if it works for people. So the very careful, hyper rigorous thinking can add
*  some of these constraints in the creative process too early, just taking some vague inspiration from
*  biology seems like a good idea for idea generation. I'll look at people's creative processes when they
*  make music. It's like Jack Antonoff, for instance, upload some examples of him making music and I
*  get a lot out of that seeing his sort of process there and for other sorts of musicians and movie
*  directors as well. I think that helps me a lot in giving me some sort of ideas and how to lay track
*  in front of a moving train effectively in a research project. And I think that the idea itself
*  though, beyond the source of inspiration seems very good intuition. I think the models have
*  cognitive empathy. They can guess people's emotions reasonably, but whether that resonates with their
*  internals is a different question. And that would be a matter of more compassionate empathy. Do they
*  actually feel motivated or disposed in a certain way in view of the model of others? So I think
*  something in that direction seems worth investigating further. Yeah, so I think it's,
*  I look forward to that in particular. I don't give faint praise generally.
*  You and Eliezer both. Eliezer said about that, I don't have the exact quote in front of me,
*  but it was something like, not obviously stupid on my first read. I rarely give reviews this positive.
*  Any other neglected approaches, especially if you're not going to turn to next?
*  Yeah, because I guess I'm doing some benchmarking stuff and I think probably maybe some AI well-being
*  related things. I'm just thinking in drafting the XAI risk management policy and then what are we
*  going to do about AI well-being? And I just have lots of question marks currently. I don't know.
*  What are we even going to measure? What are we even going to do? If there can be some clarity,
*  if there's given this theory of consciousness, here's your measure or something like that.
*  Given this theory of consciousness and you just go through these theories of consciousness or
*  something, that could be helpful. I think there are a few demos and examples where they're dishonest,
*  but not good measurements. Truthful QA was the default one, but it was to compute correlate as
*  we showed in the safety washing paper. So it seems largely to be measuring compute for the most part.
*  Other research things, I'm waiting to see what will happen with the 10x larger models
*  that are arising later this year, early next year. In the meantime, there's measuring a variety of
*  things like agent skills in humanities last exam and virology skills and better circuit breakers
*  and more tamper resistance and more reliability. But yeah, then I think maybe we'll have agents
*  from that and then that will create a whole new variety of issues. I think some other thing I'm
*  working on, which I think is a little interesting is what should the ethics of these agents be?
*  What should the actual proposals be? But that's not as much of a research question. Maybe that's
*  like people who know some legal people should get in discussions with them and try and figure out
*  some ideas there. I think the largest gaps in the intellectually outside of machine learning
*  safety research and more broad AI safety, more broadly construed stuff that isn't machine learning
*  research would be suggesting strategies about what we should do, what things to push for,
*  what are some coherent worldviews and identifying those and writing those up. So I think for instance,
*  Leo's thing was very good for identifying a specific worldview of the very short timelines
*  and intelligence explosion one and algorithmic progress matters a lot. Some of those points that
*  are definitely argue about and I don't believe as much as he does. But I think there are other
*  views to write up like what is the national competitiveness platform that is low regret?
*  I think that hasn't been particularly explored. I think people trying to zoom out and look more
*  than just technical research and see how some of these technical questions and their skill sets
*  can bear on and interact with more complex geopolitical or social or ethical or legal
*  questions is probably where things are most neglected and there's probably a lot more low
*  hanging fruit there as well. It's not easy, but I think research is probably harder. I think you're
*  more likely to research just because there haven't been that many good papers across the
*  users. Thousands of people researching these sorts of things. There's, I don't know, a few people
*  thinking about security mechanisms for GPUs that enable a verification regime for international
*  governance, for instance. I think these intersection issues are maybe the more productive thing for
*  people to focus on. You mentioned that you're working on the risk management framework for XAI.
*  I guess I take that to be your answer to responsible scaling policy. Is that the
*  right way to think about it? Yeah, just trying to be broader and there's a variety of sources of
*  risk and I just want more ideas from safety engineering brought to bear. What are other
*  sorts of risks beyond risks from scaling to deal with? One thing that has definitely stood out to
*  me about the XAI program is the, you might call it truth maxing goal that Elon has put out in,
*  I think mostly just tweet form so far. Coming from the old school Eliezer days, the paper clip
*  maximizer thought experiment, I have always tended to think that anything maxing if the system is
*  powerful enough is probably a bad idea. I like the constitutional AI vibe where we have a couple
*  different competing values of, in their case, helpful, honest, harmless, and sometimes their
*  intention and the system has to figure out how to balance those and trade them off against each other
*  and it's not perfect, it's messy, but then so are human values. We seem to get by on that basis.
*  What do you make of the truth maxing? I mean, we could chalk that up to Elon will be Elon on
*  Twitter, but it seems like there's something pretty fundamental there. Do you think that there is a
*  way to have a truth maxing AI that would be still maybe not provably safe, but qualitatively as safe
*  as a constitutional trained AI system? I should note I'm not speaking on behalf of XAI here or
*  for Elon. I can largely speak out my interpretations, things he said, and how I try and square
*  all these different organizational goals together in a more coherent risk management policy. So
*  I think he sees a societal risk and is focusing on a societal risk. So normally when people are
*  talking about AI risk and risks that will make AI not go well, people are largely talking about
*  risks emanating from individual AIs. I don't think he intuits instrumental convergence as much of
*  problem. In fact, I think it is a bit more questionable and in the AI safety textbook,
*  we discuss arguments for and against instrumental convergence and how strong one might expect that,
*  whether one should by default expect whatever goal you give the AI systems to become very
*  power seeking. We'll definitely get more of a sense of how strong those tendencies are when we have AI
*  agents soon. So he's thinking that there are in our risk management policy, the draft of it,
*  it's totally unofficial and maybe it'll change tomorrow. But I'm currently just imitating the
*  Department of Defense's risk management framework from 2001, where they split things up into
*  personnel risks, operational risks, and institutional risks. And we just modify this to
*  machine learning system risks and operational risks and instead of institutional, it's societal risks.
*  And inside of societal risks, there's a variety of different risks like bad competitors racing on
*  safety and trying to undermine regulation. That is a risk. And so fortunately, he launched on things
*  like to be the only major AI player to actually fully support SB 1047. But there is another type
*  of risk, which would be generally public epistemic are not that good and they need to be in really
*  good shape. When we are dealing with this transition to more powerful AI systems and the
*  emergence of AI life forms, so to speak, things will move very quickly. A lot of important decisions
*  will be made biggest period in at least the past 200,000 years possibly. And so public understanding,
*  if they're to be included in these decision making processes needs to be very good. And so that can
*  look like a variety of things like trying to make sure that Brock is more truthful, add features to
*  the X platform to summarize news in an objective way. And so these are various things that can
*  improve public epistemic and mitigate a societal risk that would definitely bear on whether AI goes
*  well or not. So I think that compared to other organizations that are saying we're going to be
*  the best on safety, whatever that means, they basically safety watch the research. And there's
*  a particular focus on a specific societal risk. And after having got a basic competent LLM now,
*  there can be more of a focus on adding some of these more epistemic features that improve public
*  epistemic. This trades off on some other notions of harmfulness. This allows by making models less
*  censored. One could think that could increase harms in some other sorts of ways. But like what
*  Anthropic has, I think generally competitors or competing companies of XAI will censor something
*  if it might be offensive to someone. And that's the threshold. At XAI, it's currently more if it's
*  legal, it's okay. If it's not illegal, it's not okay. So no copyright, no defamation. But in the
*  future, maybe we'll change the standard to, and I'm not speaking on behalf of them, but personally,
*  I think an attractive option is to make the AI chatbots and AI agents exercise reasonable care
*  so that they do not foreseeably cause harms to other people. And by harms, I'm meaning the stuff
*  you would wind up in court over, not something that is merely offensive or perturbs someone.
*  And that might be the sort of the type of ethics and restrictions placed on it, but still sorting
*  that out. So and that can allow for a lot of truthful information to disseminate, but not
*  necessarily specific bioweapon instructions, for instance, if those would actually foreseeably cause
*  harm. So I think it's less the training objective equals truth, but instead is we are, or I should
*  say XAI is focusing on some other risk sources and trying to specifically target them with AI
*  technology while being responsible in AI development along the way. So if I tried to bottom line that,
*  I would say you're saying big picture fullness of AI potential power, probably not a good idea to
*  go all in on truth maxing, but as a kind of current day competitive positioning and maybe
*  way to counterbalance the arguably mistaken choices of others being less sensorious,
*  more truthful and leaving the harm reduction piece to the future when harms are greater,
*  focusing more on shared epistemic success now is the overall strategy.
*  And it's not just an AI level intervention. It's also using AIs to help provide technologies that
*  help the public, their own understanding and things like that. So it's more constructive. It's not just,
*  I think a lot of safety people think of it in restrictive ways that we got to just
*  control the AI to do this and that. It's also, I think there's some benefits from trying to
*  improve some diffuse societal factors in making this overall project go well.
*  As far as giving AI specifically a truth objective, I think it would depend. My guess is there's a lot
*  of details to fill in there. Maybe some version of that is safe, but I just don't even know what is
*  truth. What theory of truth is pragmatic theory of truth? Is it something else? I mean, these would
*  have different consequences as a single objective. Elon said different sorts of things as well. He
*  said, maybe it's actually net civilizational happiness. He said that on some different
*  occasions or there's human autonomy. So it seems to be a mixture of different things you'd want in
*  these sorts of systems to promote. And they can be promoted by either giving them that specific
*  objective or using them in some sort of way to help with things like public epistemic and understanding.
*  Some are more close ended than open ended and currently it's done in a more close ended way.
*  So we're recording, I think on the day after you just put out another result on AI powered
*  forecasting. I haven't even had a chance to read that and observe it yet. I know there's quite a
*  bit of chatter online, but we did just do an episode with Dare, the new CEO of Metaculous.
*  And so we did run down kind of prior research on powered forecasting. So what's the new result that
*  you have contributed? I think it's actually not really much of a new result because we didn't
*  even really put up much of a paper. I just wanted to show relevant people a demo of, look, they're
*  forecasting bots that are very good. You could say they're maybe a 10,000x, 100x, 100,000x faster
*  and cheaper than prediction markets. And then they can be in the same ballpark of accuracy,
*  which should make them just a preferable option compared to asking a human and paying them a lot
*  of money to forecast something. You can just get an instant answer that like a relatively similar
*  quality or maybe, or in many cases, better quality than a random experience forecaster.
*  Of course, there are corner cases. If you ask it something that isn't even a question,
*  it'll still answer. AI's always have some of those quirks and weird failure modes.
*  But so it's largely to communicate. There's a sort of paper from Jacob's group, Jacob, my advisor
*  in grad school, which was showed, it said in their abstract, we have an AI system that's approaching
*  crowd level performance and in some cases exceeds it. I thought, wow, this is very big.
*  People should start using this. So this is dramatic implications, but it didn't seem to
*  catch on. I think most people forecasting were aware of it. And so that was a sort of
*  communications issue. I think these are not subhuman AI systems. They're actually very
*  competitive for many types of questions. So then we just made a demo to try and communicate this
*  more broadly. And then hopefully it will be integrated forecasting capabilities,
*  create some interest in it, given that this is something that is within the realm of what AI
*  systems can do, which wasn't the case some years ago. And I think we may have done the first AI
*  forecasting sort of paper at NERP some 2022 or something. Models were terrible. Now they're
*  really good with some various exceptions. So yeah, it's largely just trying to get interested in
*  that. And maybe Anthropic could add such a feature. Maybe OpenAid could add such a feature. So yeah,
*  largely just trying to increase attention to that to increase the probability that it gets adopted
*  as a sort of technology for improving public epistemic. Because I think if a variety of places
*  add those sorts of features, and that can be very helpful. But one of the motivations for it is that
*  there's just a lot of things that's generally are uncertain and people then aren't even aware of or
*  don't even contemplate. So having some high quality forecast, easily accessible, helps people
*  appreciate some sort of weirder events down the road. If you ask it, what's the probability that
*  OpenAI gets its weight stolen by China this decade? And someone says like 20%. Okay, that's, you're
*  gonna have to learn about InfoSec and things like that to some extent to actually get some sort of
*  probability. It knows that. And I think that can be useful for just improving decision making and
*  have us not walk into things that could have been easily avoided if there was a bit more expertise
*  in the room. I suppose there's a classic example during COVID. What will COVID be next month? How
*  many cases? And then the president's advisors fit a cubic model to the curve and then with forecast,
*  oh, it's going away next month. And their model show that it's negative the month after or something
*  and the number of cases. I think this sort of institutional decision making can be greatly
*  helped if people have easily accessible, high competence, fast and broadly skilled
*  forecasting tools. I think it's mainly some people really like forecasting as a hobby. And so this is
*  getting them people's territory in that way. I think its performance is a bit better than that
*  sort of research paper that was published earlier this year, which I think was basically roughly
*  crowd level in various circumstances, sometimes better, sometimes worse. This model is a little
*  bit better than that. But then people would go, is it better? I know a forecaster who could probably
*  be this or something. And so it's a little least spurred discussions and make people aware of it.
*  But yeah, hopefully it'll end up being integrated, which is the main purpose of it. And that's why,
*  so it's very unusual for me not to have a big paper with a lot of experimental analysis and say,
*  didn't include a lot of experimental analysis and a full write up. And we seriously wrote up
*  the technical report and I think maybe an hour or something like that, just for some basic
*  background information. And then people are like, what's going on? So under specified,
*  where are the details? Are you hiding something? No, it's just the demo. It's just trying to force
*  this on your attention. That's it. This isn't doing anything too methodologically fresh or
*  anything like that. There's an extensive write up from Halawi at all some months back for a fairly
*  similar system. You mentioned this potential low hanging fruit in what a no regrets national
*  competitiveness agenda might look like. I personally currently worry that we might end up having a lot
*  of regrets about our national competitiveness agenda. And I'm interested in your take on it.
*  Specifically, the thing that's in my craw right now, so to speak, is that I feel like decoupling
*  between US and China or West and China, when it comes to the general trajectory of AI research
*  and development seems like a recipe for an arms race. And I feel like if we're on the same
*  trajectory, that's at least one meaningful vector in which we could reduce that we're both
*  developing the same kind of technology, we both know what one another is dealing with,
*  that could be good. In contrast, like we cut off the chips, they have to go some other way that maybe
*  they might have to start thinking. And I'm reminded often of Samuel Hammond's 95
*  theses on AI. The one that is burned into my brain is RL based threat models have been discounted
*  prematurely. And I think, geez, if I'm whatever party functionary in China, and I'm like,
*  charged with staying competitive with the West on 20% of the compute budget or whatever,
*  maybe I take an asymmetric approach. And maybe that approach is like just far more reckless than
*  the path that we seem to be on, which, at least for me, has been like surprisingly surprised on
*  the upside in terms of its like friendliness to humans, I can have a remarkably ethical,
*  quickly sophisticated conversation with Claude. And I think there's a lot of other things that
*  might come out of a Chinese effort to just keep up with the West at any cost on a significantly
*  reduced compute budget. So that's my worry. You can address my worry, you can raise your own
*  worries, you can plant some seeds for what to know regrets national competitiveness agenda might look
*  like. Yeah, I don't know if I figured out a complete no regrets one. I think there's some
*  that are much higher regrets, such as like military steps in now and locks up all the
*  sorts of AI projects and securitizes them and moves them to the desert or something. And then
*  we very clearly signal we are in a huge race with you, China, and we will try and poach your people
*  and this sort of stuff. I do think cooperation between the US and China is not very tractable
*  unless there is some sort of catastrophe, or if there's very strong signs that there are AI's
*  that are just trying to destroy us and that it's a bigger threat than they are to each other.
*  But absent that, and that will basically not be through convincing them of scenarios,
*  don't seem to particularly move our institutions. So it will need to be something actual.
*  I think saying like international coordination is good, reducing competitive pressures is good,
*  reducing arms races is good. But I think maybe coordination looks more like a Western alliance
*  as opposed to an inclusion of China in that. So there are different ways you can do coordination
*  as the US goes alone, or the US just things with Europe and NATO allies or five eyes, Canada and
*  Australia and the UK and New Zealand and the US, or there is including China. But the third one is
*  I think just much less tractable. It won't be tractable for some while. So I think on the margin,
*  it makes more sense to try and focus on other things or channel the energies of people's
*  concerns about China's two more productive, lower regret type of options. One of which I haven't
*  spoken with many people about, but I think occurred to me last week is just spending more on,
*  if the government is to spend money on AI stuff, they're saying we need to support AI R&D. So what
*  does that mean? Does that mean giving money to the labs like OpenAI or the big AI companies?
*  Instead, possibly that money could be spent on just subsidies for chip manufacturing here. There
*  are lots of chip plants being built, and they're being built in different places, some of which
*  are being built here, but they usually need subsidies to be built here. So if they're built
*  here, that seems better from a robustness perspective. Because if China invades Taiwan,
*  then TSMC becomes dysfunctional likely. Either it's destroyed or the supply chain parts that
*  go into it are not given to them. The West is not giving it to them. That would by default cause a
*  global depression, possibly a great power conflict. And if compute is so relevant for AI capabilities,
*  it seems important that the US not fall really far behind the possible strength of the US in
*  a fast time or fast takeoff scenario seems to be compute that would provide a lot of advantage.
*  Or in short timelines, as you say, it provides a lot of advantage. And in long timelines,
*  it provides a lot of advantage because long timelines, it's mainly like your economy versus
*  their economy and the economy will be in large part how many AI systems can you run and how
*  quickly can they run? I think in both scenarios, one's very bullish on AI or bearish on AI,
*  but still thinks it's very salient from a national competitiveness standpoint.
*  Possibly focusing on chips and having more robustness to a relatively likely geopolitical
*  catastrophe would be useful. I think forecasting Sherman's give it around 30%. And I think the
*  forecasting bot gives it around 30% for this decade. And maybe it'll be higher than that.
*  If China views, sees the US pulling ahead in AI, and this will give them a very dominating position
*  and will really amplify their power relative to China's, maybe rational for China, not saying it'd
*  be good, but rational for China to invade Taiwan, do something they already wanted to do. There's
*  even more reason to do it. But then that makes things a lot harder for the US and makes it more
*  desperate. And that could get even more ugly. I think there are other sorts of interventions
*  that I think are lower regret, like chip registries. I think adding some basic features
*  onto chips that help verify whether they're in a country that's supposed to have them versus not.
*  Could be useful. That's maybe a bit more contentious. Like if it's in Iran or North
*  Korea, then maybe it shouldn't be functional. So geofencing of some sort. But yeah, I do agree
*  that none of these are costless. But I am acting subject to the constraint that coordination with
*  China isn't really possible unless there's something that looks like a catastrophe or a
*  very convincing near miss scenario. And I think focusing on compute and robustness to some of
*  these geopolitical events that are relatively likely seems like a possible way we could improve
*  national resilience. Where does that put you on the chip ban today? I think there seems to be a
*  general consensus or near consensus on building more chips at home would be good. Much different
*  thing in my mind from cutting China off from buying from the international market, which we've
*  currently done. If you believe the AGI in 2027, ASI soon after the Western values must prevail
*  argument, then you support the chip ban. If you think that's a lot of conjunctions in that argument
*  and maybe it's gonna take longer, then maybe you don't support the chip ban. Is that how you think
*  about it? And do you have an official position on the chip ban? I know I think I generally am in
*  favor of export controls. There could be this unintended consequence though that it incentivized
*  them very early on to build up chip independence. And if there's an invasion of Taiwan, then mainly
*  the West falls behind and China can continue going ahead. That's a way it could have caused
*  backfire as an intervention. I think it's a little unclear, but I think overall though,
*  I think that was a reasonable move that pays off well in short timelines, long timelines that
*  suggest algorithmic progress is even less. And so that suggests compute is the more essential thing.
*  I don't think there would have, it's not as though if we didn't do export controls,
*  there'd be total coordination between the US and China on these issues. That's I don't think the
*  case. The US didn't want China going to the UK AI safety summit, just even attending. And that's just
*  a general thing. This isn't, well, we don't like China on AI safety. That's not it. It's just they
*  don't like China. And this is very strong. And it's basically like negotiation ending to share
*  things with them. And they currently have enough of a competitive advantage in compute and in talent
*  that they are not particularly looking to bargain with them currently. There could be some other
*  sorts of treaties like a verification regime for GPUs. There could be some angles for it,
*  for coordination. But I think I seek to offset some of those damages from the export controls
*  through other means by maybe working on them with maybe working with the scientists somewhat more or
*  something like that to build at least goodwill between the scientific communities even more.
*  But yeah, I think overall, I think in many scenarios, the export controls were a reasonable
*  intervention. Last question. You are the executive director of CASE, the Center for AI Safety. You
*  guys have a bunch of open roles on your website. I think people probably have a good sense of all
*  the various things that you're involved with. And I assume many of those directions will remain live
*  as you go forward. Pitch the opportunity to work at CASE and give us a sense of what you are looking
*  for in teammates. There's a variety of different topics and we'll basically keep focusing on new
*  things constantly. So if there's people wanting a variety of things to do in their work and identify
*  opportunities for impact, to not feel committed to something once its impact has been made,
*  then this is a good dynamic environment. I think that generally intelligence and
*  conscientiousness and experience is the main sort of thing that we care about. It's not really
*  too much to that. It's not looking for whether you believe particular things or something that
*  really doesn't mind as long as you can work productively and get things done competently.
*  And then of course, we'll work on research and field building and sort of advocacy and advising
*  for a variety of things. We'll try and be competitiveness on each of those fronts in research
*  and to governance types of things. We'll try and make sure that there aren't organizations that are
*  lapping us in any of those sorts of things. Anything safety related tend to work on at some
*  point. EVALs, engaging academics, policy, demos, software implementation.
*  And things we didn't even bring up. Just in brief, maybe, how did you pull that off?
*  I think everybody knows the Extinction Risk Statement, two sentences signed by all the
*  BAMs, Altman and Demises, and similar people. It was really a remarkable group that came
*  together to sign that. Any tips for pulling off such an achievement?
*  I think the statement can be found at aistatement.com, for example. I think some of the main
*  mechanisms were actually just modeling. Remember the good regulator theorem, which is if you want to
*  regulate a system, then you need to have a model of that system, like a very good one. And I think
*  that the main barrier for getting people to sign on to that was asking in a particular order.
*  So I just generally have an interest in learning about people and where they're at and keeping
*  track of that. It just seems useful and interesting in its own right. I had to some extent a sense of
*  who are the people who will sign on early without needing any of their friends? Who are people who
*  are going to need two or three of their friends to sign on? Who are people who are going to need
*  seven of their friends to sign on? And so basically proceeded in that order over the course of a month
*  or so. If we just did something like blasted the email to everybody simultaneously, I think we would
*  have completely failed. So that's, I think, the payoff of just having a model of these very
*  interacting with these various stakeholders across time and getting a sense of where they're at on AI
*  safety related things. So they're solving a collective action problem. In this case required,
*  I think more of a social model. Who was last to sign? Just kidding. I know you'll never tell.
*  I think people came in. Oh, I've some of the top signatories. Some people took a bit longer
*  than I expected, but I won't say who. This has been fantastic. I really appreciate all the time
*  and the breadth of everything that we've discussed. Any closing thoughts or anything
*  you want to plug before we go? Yeah, I guess you can follow me on Twitter. There's also a course.
*  I was mentioning complex systems and safety engineering, these sorts of governance issues.
*  These are discussed in at asafetybook.com and we'll run future versions of the course as well.
*  Another thing is we have a newsletter, which should be newsletter.safe.ai that we put out every two
*  weeks or so. We're trying to help people be aware of what are the main developments in AI safety.
*  So those are some possible ways to stay connected and to learn more about these topics.
*  Cool. Thanks for having me. Dan Hendricks, executive director of the Center for AI Safety.
*  Thank you for being part of the cognitive revolution. It is both energizing and
*  enlightening to hear why people listen and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me on the
*  social media platform of your choice.

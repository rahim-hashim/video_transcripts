---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 3316s
Video Keywords: []
Video Views: 12666
Video Rating: None
Video Description: Nathan interviews Google product managers Shrestha Basu Mallick and Logan Kilpatrick about the Gemini API and AI Studio. They discuss Google's new grounding feature, allowing Gemini models to access real-time web information via Google search. The conversation explores Gemini's rapid growth, its position in the AI landscape, and Google's competitive strategy. Nathan shares insights from integrating Gemini into his own application and ponders the future of large language model capabilities across providers. Tune in for an in-depth look at Google's AI API product strategy and the latest Gemini features.

Be notified early when Turpentine's drops new publication: https://www.turpentine.co/exclusiveaccess

SPONSORS:
Weights & Biases RAG++: Advanced training for building production-ready RAG applications. Learn from experts to overcome LLM challenges, evaluate systematically, and integrate advanced features. Includes free Cohere credits. Visit https://wandb.me/cr to start the RAG++ course today.

Shopify: Shopify is the world's leading e-commerce platform, offering a market-leading checkout system and exclusive AI apps like Quikly. Nobody does selling better than Shopify. Get a $1 per month trial at https://shopify.com/cognitive

Notion: Notion offers powerful workflow and automation templates, perfect for streamlining processes and laying the groundwork for AI-driven automation. With Notion AI, you can search across thousands of documents from various platforms, generating highly relevant analysis and content tailored just for you - try it for free at https://notion.com/cognitiverevolution

LMNT: LMNT is a zero-sugar electrolyte drink mix that's redefining hydration and performance. Ideal for those who fast or anyone looking to optimize their electrolyte intake. Support the show and get a free sample pack with any purchase at https://drinklmnt.com/tcr

CHAPTERS:
(00:00:00) About the Show
(00:00:22) Sponsors: Weights & Biases RAG++
(00:01:28) About the Episode
(00:04:15) Gemini API Growth
(00:05:26) Intro to AI Studio
(00:07:35) Vertex vs. AI Studio
(00:09:33) Developer Adoption
(00:14:23) Gemini Use Cases (Part 1)
(00:17:05) Sponsors: Shopify | Notion
(00:20:01) Gemini Use Cases (Part 2)
(00:23:08) Multimodality & Flash
(00:26:29) Free Tier & Costs
(00:31:43) Inference Costs
(00:32:55) Fine-tuning & Vision
(00:36:24) Sponsors: LMNT
(00:38:04) Search Grounding
(00:44:42) Grounding Sources
(00:46:58) Competitive Landscape
(00:50:36) Design Decisions
(00:54:54) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Breaking Gemini's Major Update - Search, JSON & Code Features Revealed by Google PMs
**Cognitive Revolution:** [October 31, 2024](https://www.youtube.com/watch?v=R7M785Xgogs)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  As a developer, the journey from concept to production-ready large language model apps
*  is fraught with challenges. Dealing with unpredictable language model outputs,
*  hallucinations, and ballooning API costs can all be blockers to shipping your next AI-powered feature.
*  That's where Advanced RAG comes in. With the new RAG++ course from Weights and Biases,
*  you can overcome these hurdles and build reliable, production-ready RAG applications.
*  Go beyond proof of concept and learn how to evaluate systematically,
*  use hybrid search correctly, and give your RAG system access to tool calling.
*  Based on 21 months of running a customer support bot in production,
*  industry experts at Weights and Biases, Cohere, and Weaviate show you how to get to a deployment
*  grade RAG application. This offer includes free credits from Cohere to get you started.
*  Make real progress on your large language model development and visit wnb.me.cr to get started
*  with their RAG++ course today. That's wnb.me.cr to get started with their RAG++ course today.
*  Hello, and welcome back to the Cognitive Revolution. Today, my guests are Shrestha Basumalik and Logan
*  Kilpatrick, product managers for Google's Gemini API and AI Studio products. The occasion for our
*  conversation is Google's release of a new grounding feature that allows Gemini models to tap into
*  Google search results to get up-to-date information from the web at runtime. This comes just a couple
*  of days after Google's latest earnings call, in which CEO Sundar Pichai noted that Gemini API
*  usage has grown by a factor of 14 over just the last six months. To prepare for this conversation,
*  I spent a couple of hours integrating Gemini into an application that I'm developing,
*  and I found myself pondering a few big picture questions. First, considering that various
*  leaderboards consistently have Gemini at or very near the top, why does it still seem to be the
*  third priority for most developers behind OpenAI and Anthropic? One hypothesis is that Google's
*  platform is simply too complicated, or that the Gemini API is missing key features. But in my hands
*  on work, I did not find that to be the case. Using the Vercell AI SDK, I was able to integrate Gemini
*  as a peer to OpenAI and Anthropic models quite quickly and easily. Second, should we expect
*  large language model capabilities to converge or to diverge across providers? Considering this
*  question through the lens of the platonic representation hypothesis and taking seriously
*  that large language models are learning ever more sophisticated world models and patterns of
*  reasoning, it would seem that they are destined to converge. And yet at the same time, OpenAI now has
*  unique reasoning models, Claude is alone in its ability to use computers, and Gemini still has by
*  far the longest context windows and now adds to that a native Google search integration.
*  Finally, how and how much are teams within these companies thinking about competition?
*  We know that Big Tech leadership is taking a game-theoretic approach, justifying tens of billions of
*  dollars of investments on the ground that that's simply what it takes to make sure they're not left
*  behind in the AI era. But what about at a product development level? Are they constantly thinking
*  about the competition or are they just trying to build the best products that they can?
*  Logan and Tresta had thoughtful responses to these questions and more as we got into a number of
*  details on the Gemini API and AI Studio, including code execution, prompt caching, the incredible
*  value of Gemini Flash, and the generous free tier that Google offers all in just an hour's time.
*  As always, if you're finding value in the show, we'd appreciate an online shout out, a review on
*  Apple podcasts or Spotify, or just a comment on YouTube. We always welcome your feedback either
*  via our website, cognitiverevolution.ai, or by DMing me on your favorite social network. For now,
*  I hope you enjoy this real-time update on the Gemini API's latest features and the inside look
*  at Google's AI API product strategy with Tresta Basumalek and Logan Kilpatrick.
*  Tresta Basumalek and Logan Kilpatrick from Google, the Gemini API and the AI Studio team.
*  Welcome to the Cognitive Revolution.
*  Thanks, Nathan.
*  Yeah, thanks, Nathan. I'm excited that this is Appearance 3, so I'm going for the record
*  for the most number of appearances on your podcast.
*  Yeah, you're in great competition.
*  Yeah, you're in great company. Another three-time guest is Nat Viv from the Medical Applications
*  team. Watch out, because he might be due for a fourth before we know it. You guys got to keep
*  the pace up. Big news yesterday, Google had an earnings call, I think added a cool $100
*  billion to the market cap after hours. Everybody's feeling good. The headline stat around the Gemini
*  API was 14x usage growth over the last six months. I have also spent a few hours this morning
*  looking at the AI Studio, all the latest stuff there, and testing out the big new announcement
*  today, which is the new grounding feature where we can now tap directly into Google search results
*  when we make a Gemini API call. A lot of great stuff there. Let's get the headlines from your
*  perspective. Yeah, I love that. Maybe a quick super high-level context setting for
*  folks who don't know AI Studio, and then we can talk about search grounding. Yeah, AI Studio entry
*  point for developers to build with AI, and specifically Gemini. We have all the latest
*  Gemini models available inside of AI Studio. It's really intended to be the least frictionful
*  experience you could imagine. So literally three or four clicks, and Nathan, you can either confirm
*  or deny this. A few clicks, get an API key, test the models really quickly, and then go off and
*  build something. I think that's what success for us looks like. And the increase in API usage and
*  users building with Gemini has been awesome to see, and I think in some, at least to a certain
*  degree, driven by make it as easy as possible to use Gemini, and also as easy as possible to build
*  with Gemini. We also have had a ton of, independent of today's search grounding launch, which I'm
*  excited to talk about, just a slew of continual things coming out the door from experimental
*  models to production-ready models to new model classes with our Flash AB model to code execution
*  and all this other stuff that's landed in the last six months. So I think there is this direct
*  correlation in the increase in usage with continually getting new features off the door
*  for developers. And there's so much new stuff that's coming out these days. I think developers are
*  sort of being implicitly tuned to gravitate towards the platform where things are continuing to come
*  out of. And it's been fun to be a part of that for the last six months and continue to put things
*  into the hands of developers and get them excited about the path that we're on. Definitely.
*  I would also say, like we can go into search grounding in a bit here, but I would also say that
*  there's also features that we have out there. Logan mentioned code execution, we have context
*  caching. Nate, you were talking about structured outputs where we've put out the initial versions
*  of the features, but we're continuously taking feedback from developers in terms of how to
*  improve those features. And also the overall platform experience, whether it's error codes,
*  whether it's rate limits, we're continuously trying to think of how do we provide a frictionless
*  experience for developers. A lot of progress certainly has been made. I think it really does
*  bear emphasizing the early fork in the road that we've seen some. And of course, Logan,
*  you continue to do Yeoman's work on online correcting any misconceptions that may pop up.
*  But I've seen a couple of people be like, oh God, I wanted to use Gemini. I went into Vertex. I got
*  totally lost. And in that respect, certainly Google's in good company with other major cloud
*  platform providers where the tools have just become overwhelming for a new user. Certainly,
*  I've experienced that most with AWS, honestly. The fork in the road early is like understand the
*  distinction between Vertex and the AI studio and make sure if you are trying to do the kind of work
*  that I do, which is typically prototype proof of concept, relatively low info sec hazard type of
*  things, then you want to find yourself in the AI studio. And that is really very much on par.
*  And in some ways, I would even say has some advantages relative to the competing platform
*  type products that OpenAI and Anthropic have, which are all getting really quite good at this
*  point. So go in there, choose a template prompt, tinker around with it, handle all the different
*  little things on the sidebar around the structured outputs, whatever, whatever, generate code,
*  choose your language, paste that into AI coding assistant and have it do the translation into your
*  application. I actually did that basically end to end earlier today in just about 90 minutes
*  for an application that I'm developing. And it was really pretty smooth process.
*  I will confess that Gemini was the third provider that I had added to the app. Like most people,
*  I started with OpenAI as it's just kind of the thing to do, I feel like. Then I went to Sonnet.
*  And then today I was like, oh, this grounding thing sounds pretty cool. I should go check that
*  out and let's see how smooth they've really made it. Let me do the integration. It really was super
*  smooth. I wonder if you think I'm representative, first of all, in terms of being a developer who
*  like, for whatever reason, still has Gemini third in their queue. And I was looking for reasons for
*  this today. I was like, what's the deal on LMSys? Well, not really a big difference. Gemini models
*  right at the top. What's the deal with ease of use? What's the deal with structured outputs?
*  What's the deal with all these features? It seems pretty much like a dead heat, honestly,
*  in the overall competition these days. So I wonder, is that just like the legacy hangover from the
*  pre-Logan era? Do you have other ideas about it? And maybe we can kind of talk about some of the
*  wins that you're seeing that might inspire people to think about these as like peers as opposed to a
*  one, two, three ranking. Yeah, this is a, it's a great question. I think the answer is complicated.
*  I think maybe one simple answer is like, you know, Gemini has only been around for a year now.
*  Actually, the model hasn't even been out for a full year. December of 2023 was when the first
*  Gemini model was announced. OpenAI had a bunch of other models long before that. And the API had
*  existed for actually many years before that, dating all the way back to, I think, 2021 or 2022.
*  So we've been sort of in the last year on this, to the point that you made on this mission to sort
*  of get to parity with the rest of the ecosystem, and then really actually start to deliver some
*  of those differentiated capabilities. I think we've done that at the model level. And that's been
*  actually from the beginning with Gemini, going natively multimodal and being the first LLM,
*  the large scale frontier LLM to go natively multimodal. And also at launch with Long Context,
*  the Million Token Context window. And we were there together at I.O. when the 2 million tokens
*  with 1.5 Pro was announced and also 1.5 Flash, which was sort of this, I think this breakout
*  moment for us where, and you can sort of track that back to six months ago as well when sort of
*  API volume started to increase. That model has done such a good job of sort of balancing all of
*  these different things that developers really care about. I think all that said, a ton of progress.
*  The practical reality is like Gemini still only been around for less than a year. So like we are
*  sort of getting over the mindshare perception challenges of people already having chosen an
*  LLM when the technology originally came out. And the strategy is do a bunch of things that solve a
*  bunch of the problems that sort of are uniquely suited for Google to solve. And one of those is
*  search grounding and the other one being some of the long context stuff from an infrastructure
*  challenge perspective. So it's been a ton of fun to sort of reason about what are the things that
*  we can uniquely provide value on in addition to just having the world's best models from all the
*  metrics and capabilities standpoint, how can we continue to differentiate? And that's why I think
*  search grounding has been a ton of fun. Yeah. And you add to that, Nathan, like when we go and
*  talk to developers, we do hear that that OpenAI and Tropic, they've both built excellent models
*  with great bars. And a lot of times when you're a very busy startup founder or someone like
*  yourselves that builds a lot of prototypes, you may not have the time to evaluate all the models
*  and make a rigorous decision. And under those circumstances, it can sometimes be easy to just
*  say, we know there's a lot of buzz around this specific model. Let's just go with that.
*  Directionally be a safe choice. And so we do have a lot of empathy for developers. And this is also
*  where coming back to the conversation we were having, giving developers best practices around
*  prompting around easy ways to quickly evaluate models for their use cases and understand
*  the quality, price, latency trade-off there quickly will help. And we do see that,
*  to Logan's point, and of course we are in our post Logan era, not post Logan, but like her.
*  We're in the Logan era. In the Logan era, sorry. I think it's really made a difference. And I think
*  we do see the perception changing just with us trying to be more responsive,
*  us trying to build a more robust platform, not just for prototyping, but we hope for
*  production use cases as well. That's the thing that gets me most excited, which is like,
*  I do think the perception is changing. Like, you know, the sort of canonical joke on Twitter right
*  now of like the vibe shifting to a certain extent, it actually has, I think the challenge is like,
*  you sort of, you earn the perception shift over a very long extended period of time. So this is
*  like a many year endeavor of us building the best platform for developers to build with AI,
*  but the progress in the last six months gets me incredibly excited that we actually are going to
*  do that. It's just, yeah, you have to continue to earn it over time. And hopefully search grounding
*  is another one of those moments where folks are like, yeah, this is, it's clear that Google is
*  really showing up and building best in class tools for developers.
*  Yeah. So let's talk about some of the wins and some of the reasons why, and maybe give some kind
*  of sense for situations where people have found advantage in Gemini in the earnings call yesterday
*  or on the blog, a company blog post, there was a call out for snap. There was also a call out for
*  a company called Hiscox, which I didn't know much about, but is apparently a big insurance company
*  that is using Gemini to reduce the time it takes to come up with a quote for some sort of complicated
*  risk. Days to minutes. We've certainly seen that kind of story in general. What I would love to dig
*  into a little bit more, and you could bring your own examples too, once you've seen, I'm sure you've
*  got many, many startups and conversations you could draw on for this, but what are some examples where
*  people are kind of evaluating and ultimately said like, okay, we're going to go with Gemini. Here's
*  why. I think those sorts of examples are probably the most compelling thing we could communicate to
*  people. Yeah, I think that the whole sort of class of use cases where we see Gemini sort of excelling
*  and also like developers getting most excited is around multimodal stuff. I think again, that sort
*  of push from the first iteration of the Gemini models to be natively multimodal is like the DNA
*  of the model is such that these are use cases that we care about and have spent the last year pushing
*  and making them even better. It's also the use cases where there's actually the least amount of
*  products and companies that have been built so far. So it is like the frontier of
*  making native audio work, making native video understanding work, making native multimodal
*  image understanding work, and actually scaling those to production use cases. We're still at
*  the very early stage of that happening. But if you look at the people who are sort of pushing
*  the frontier and like a great example is like TL Draw is one of those companies that I love to see
*  actually pushing on what might the next iteration of the user experience of some of these
*  LLMs actually look like and powering that experience using Gemini because of this push
*  that we've done with image, audio and video. I think has been one of the most exciting thing.
*  Also from like the founder builder perspective, if you're sort of looking at the space of where
*  the opportunities are, you actually want to be using the frontier capabilities and you want to
*  be going to the place where like there's not a ton of people who are already building. And I feel
*  like for a lot of text use cases, there's just like, you know, a thousand and one different
*  startups tackling every single use case that's possible with text. And there's actually again,
*  just because these capabilities are sort of still on the frontier, there's way less companies that
*  are tackling those problems. And that gets me excited as sort of the maturity curve continues
*  to ramp up. And as those folks find these use cases more, they'll sort of tell this story and
*  more and more folks will end up using Gemini. Hey, we'll continue our interview in a moment
*  after word from our sponsors. The cognitive revolution is brought to you by Shopify.
*  I've known Shopify as the world's leading e-commerce platform for years, but it was only
*  recently when I started a project with my friends at quickly that I realized just how dominant
*  Shopify really is. Quickly is an urgency marketing platform that's been running innovative time
*  limited marketing activations for major brands for years. Now we're working together to build an AI
*  layer, which will use generative AI to scale their service to long tail e-commerce businesses.
*  And since Shopify has the largest market share, the most robust APIs and the most thriving
*  application ecosystem, we are building exclusively for the Shopify platform.
*  So if you're building an e-commerce business upgrade to Shopify and you'll enjoy not only
*  their market leading checkout system, but also an increasingly robust library of cutting edge AI apps
*  like quickly, many of which will be exclusive to Shopify on launch.
*  Cognitive revolution listeners can sign up for a $1 per month trial period at Shopify.com
*  slash cognitive where cognitive is all lowercase. Nobody does selling better than Shopify. So visit
*  Shopify.com slash cognitive to upgrade your selling today. That's Shopify.com slash cognitive.
*  As a cognitive revolution listener, you're obviously interested in cutting edge AI technology.
*  And with that in mind, I'm proud to say that this episode is brought to you in part by Notion.
*  Notion has been a clear leader in high value applications of generative AI since the wave
*  began. Earlier this year, we had Notion AI engineer Linus Lee on the podcast. The quality of his
*  insights showcase the caliber of talent that Notion employs. And that inside look at how Notion
*  builds with AI is still extremely valuable. Given my personal focus on AI automation recently,
*  I specifically wanted to highlight Notion's library of workflow and automation templates.
*  If you're looking to streamline your processes and lay the foundation for future AI driven
*  automation, these templates are an excellent starting point. And even if you're not ready
*  for full automation, you'll benefit immediately from Notion AI. Notion's latest all in one AI
*  implementation that searches through thousands of documents, regardless of whether they live
*  in Notion or on some other platform like Slack or Google Docs to deeply understand the context
*  of your work and generate highly relevant analysis and content just for you. Notion is used by more
*  than half of Fortune 500 companies, helping teams reduce emails, meetings and time spent searching
*  for information. Want to try it? Head to Notion.com slash Cognitive Revolution. You can start for free
*  and using our link supports the show. So join me in giving Notion AI a shot today at Notion.com
*  slash Cognitive Revolution. Yeah, plus one to that, right? Multi-modal long context and the
*  overall price performance trade off that we offer. So another example is this company called New
*  Computer and they've designed an AI called Dot where the idea is to, you know, they kind of create
*  like these living history of people. And they're basically the goal here is to know and understand
*  people. So they're using Flash because it has large context length and also the price is very
*  favorable to compress daily conversations into retrievable objects for Dot's memory, which Dot
*  can then go back and retrieve these daily summaries of the user's conversation to build an overall
*  understanding of the person. And then a couple of examples that we've talked about before is there's
*  this company called Envision that is helping people with low vision to better understand their
*  immediate environment. And again, here, this is a place where the speed of Flash becomes very
*  relevant because for a use case like that, you need like low latency. And then we've also talked
*  about Locofy that takes basically a Figma design and uses their own AI models to generate code.
*  But they're pairing this with Gemini's 1.5 million context window because, you know, front end designs
*  can contain hundreds of layers and Gemini kind of helps to take that front end design and reformat
*  it and rename it in a way that makes it easier to then be consumed by their own proprietary AI model.
*  So these are some examples.
*  Yeah, and Nathan, what you mentioned sort of, you checked LMSys today and you sort of looked at the
*  capabilities of the model from that perspective. This is obviously somewhat biased because it makes
*  Gemini models look really good, but I've been sending folks to artificial analysis, which sort
*  of goes like a few levels deeper than just what is the ELO score of the model, which is what LMSys
*  is testing. It takes into account things like price, latency, et cetera, et cetera. And the thing that
*  continually puts a smile on my face is Flash is literally in its own quadrant. There is no one
*  else that is in that quadrant. As you take into account the things that developers actually care
*  about, and I think I like LMSys a ton and I think it's a great sort of proxy for how good the models
*  are, but it actually doesn't quantify many of the characteristics that developers actually care about
*  as they're making the decision of what model should I take into production. So it's been really cool.
*  Sri, you mentioned the sort of output speed. That's another one where it's like Flash is sort of
*  leading the pack from a time to first token and tokens per second perspective. So I'm optimistic
*  that, again, it takes time to get people aware of the stuff, but the proof is in the pudding,
*  especially with Flash. I think it just continues to be far and away the best. My favorite quote is,
*  I saw some tweet that was like, Google's making it impossible to not build with Flash because of how
*  good the value proposition is. I love to hear that perspective from developers.
*  And now we have Flash 8B as well, which is another great price performance latency trade-off model.
*  So to summarize that, the key distinguishing factors up to present have been
*  multimodality. Gemini was a leader on. I would say at this point, everybody sort of has that. I don't
*  know if that's something that we can... When they were drawn to that, maybe not entirely,
*  I guess audio is maybe still not exactly supported in other places. Same with video, I think.
*  Yeah. Okay. It's funny. I've done a lot of little workarounds for this kind of stuff over time
*  where I'm almost accustomed now to pulling image frames out of video and sending those in a packet
*  to whatever language model I'm using. And same thing with audio where I'll do a
*  transcription and then feed that in and whatever. So, okay, you can get around that kind of stuff.
*  You can just provide those files. So that's definitely still a distinctive capability.
*  The long context thing obviously resonates. I had a challenge for myself and then the just
*  price performance of Flash, I should spit it out. I had a challenge for myself at one point of
*  figuring out how to spend a dollar a day on Flash. And notably, and I want to get a little bit of
*  your comments on the free tier as well, because I actually think that I spent nothing, even though
*  if I had paid the nominal price, I would have, I think, spent a dollar. That took me 12 to 13
*  million tokens. It was processing five years of email. And I do think more people should be
*  thinking about what they can do to process and filter information at previously unimaginable
*  scale because it's just so cheap now. I haven't built some of these things yet, but I'm thinking
*  about, of course, everything's going exponential in AI. So I used to feel like I could sort of
*  a couple of years ago now, I used to feel like I could keep up with the research and the most
*  important papers I would end up seeing. They would come across my radar one way or another.
*  That ship has long since sailed. And I feel that primarily just because things sometimes pop up
*  and it's like, this was a month ago and I didn't even see it. What's happening? So that's crazy.
*  This concept of luxury software keeps coming up where I'm like, could I create an app to,
*  with a lot of context on me, go read every paper that comes out on archive every single day
*  and make actual, and of course the devil's going to be in the details on the actual quality of the
*  recommendations. But can I get it to a point where it is reliably surfacing the ones that I really
*  want to read given my interests? Where I'm at on that right now is I've done a lot of the context
*  creation. And I think the cheapness of a model like flash, the affordability, maybe there's a more
*  positive way to say that, is such that I can literally potentially drop in 50, even 100,000
*  tokens about me for each call that I want to make and do that with each paper. And it still multiplies
*  out in such a way where if I do 100 papers, I'm getting into the neighborhood with 100,000 tokens
*  about me to guide its evaluation of that paper for me specifically, that still only adds up to
*  maybe a dollar a day, which is pretty crazy to think about. So frontiers there are receding
*  before us faster than we can chase them down, I'm afraid. I guess to actually make a question out of
*  that, can you tell us what the free tier looks like? I saw Swix also say that if you had a live
*  video feed, you could take one frame per second and feed that into flash on a continual basis.
*  And that would still be within the free tier. So I want to understand the free tier better. And
*  I'm also curious as to what other luxury software boundary pushing million X information processing
*  ideas you guys have come across recently. Yeah, Nathan, that example that you gave is even further
*  reducing costs because you can put, if you have that static set of context, you just throw that
*  in context caching and then you sort of nominally pay the really small amount to store it and or
*  pay the incremental token costs. It gets even better as you sort of have that persistent set
*  of tokens that you want to continue to reuse. But I think the free tier is such an important part of
*  the strategy for us. If you look at what is the fundamental limitation for developers to build
*  with AI, it's actually economic costs. The cost for developers to experiment with technology and
*  ultimately go and build something and put it in the hands of users is generally high right now.
*  And the free tier gives developers for us the opportunity to not have to like put in a credit
*  card to begin with. And you could be anywhere in the world, the 200 plus countries where the
*  Gemini API supported and get access to that free tier. And it's, I don't think you can do one
*  frame per second. The total number of requests for the free tier with 1.5 flash, for example,
*  is 1500 a day. But the interesting thing is you could make all of those long context token
*  requests. So it could end up being like 1.5 billion tokens every single day that you're
*  getting for free on a re-accredited basis, which is actually just like incredibly good value
*  proposition. In addition to all of the frontier capabilities, including search grounding and
*  others, code execution, et cetera, being available for free for developers to try an AI studio. So
*  it's like the two pronged approach of minimal friction to get started, experiment with the
*  features, see what's possible. And then when you go to the API, you actually still don't have to
*  pay. And then ultimately, when you want to go to production, we have the scaled pay as you go tier
*  with the prices that make it difficult to spend a dollar a day. So this narrative is one that
*  we'll continue to push on as we want to extend the technology to get into the hands of more
*  developers. There's such a small, I forgot, I don't know if it was GitHub or another provider
*  putting out the number of developers who are using AI today is still like only a fifth of developers
*  have actually used and are actively building with AI. And again, I posit like a lot of that
*  is actually the economic cost of getting started and not wanting to take on that burden.
*  I have another thesis, which is that it's obstinance more so than cost, which might be harder to get
*  over. Just to unpack this cost thing for a second more, because I tell people, now I would separate
*  it from like, as a friction reduction strategy, it makes a ton of sense for Google to say, hey,
*  get in here, see what we've got. We'll worry about the money later. YouTube is now making
*  roughly a billion dollars in revenue a week, I understand. So like, there's some ability to
*  give a free taste on the Gemini API. But when I think about it from the developers' perspective,
*  there's the friction reduction part. But I'm also like, when I coach people on how to think about
*  doing an AI project, I usually say, you should be able to save 90% relative to what you're doing
*  today with human labor, which is usually what people are trying to save on. And then of that
*  10% that you're going to spend, still 90% of that is probably on the R&D and just up, right? Like,
*  the money goes to the developer, somebody like me or whoever you're going to hire to help you with
*  it. And then like 1% usually ends up going to the actual inference costs. All numbers rough,
*  obviously. But do you see a different pattern out there? I see people being like, way too concerned
*  about cost. And I'm constantly trying to talk them out of that. I guess maybe that's the same
*  thing that you're saying. But it's a strange phenomenon to me that people are so worried
*  about inference costs. I think it's the disconnect between like actual cost that has incurred versus
*  like implied costs. Like, I think people have this notion, and perhaps a lot of this goes back to
*  like maybe the first time you ever looked at the cost of LLMs as a developer was two years ago,
*  when it was like $30 for a million tokens or something like that. And that sort of has stuck
*  with you to be like, oh, this thing's actually really expensive to use and put it in production.
*  Which I think is like entirely disconnected now from the reality that it's, you know,
*  costs have gone down like 99.9% in the last two years. So I think the challenge of AI right now,
*  independent of just developers, maybe this actually goes to the point that you made before,
*  Nathan, is actually just like this continual education as the frontier changes. And it's like
*  hard for that message to be like disseminated. I bet if you were to ask a thousand developers,
*  how expensive is it to build with AI? They would tell you it's really expensive. And like,
*  we should be really careful about this when the practical reality is like, it's actually not the
*  case anymore. And you just need to sort of, you know, that's why we're tweeting essentially,
*  is to continue to spread the message that like that shouldn't be a burden for developers as they
*  build. 100%. And I think that the inference cost, like we've all seen those cost curves,
*  but one thing we know for sure is inference costs are continuing to go down drastically
*  across everyone in the industry. But I do have empathy here again, because I think sometimes
*  like with some of the newer features, like tool use or code execution, there could be certain
*  hidden costs and developers are right to be like, you know, sort of more careful here. But I think
*  overall, we can all agree that these costs will come down. I did want to come back if I made to
*  the one frame per second comment, I was trying to back it out. And I think what that might have been
*  is 1 million tokens is roughly one hour of video. And if you look at each frame of a video, like
*  right now we have one image at about 258 tokens, but then with the metadata on top, each frame is
*  about 300 tokens. So maybe Swix's calculation was coming from there, because then that would roughly
*  be 300 tokens. So one hour of video would roughly be 300 tokens per second, which is 300 tokens is
*  roughly one frame. Okay, gotcha. Thank you. I do think that like ongoing camera monitoring is a
*  really interesting use case for Flash. I mean, I've had multiple conversations in recent months
*  with companies that are like, we've developed a, you know, we've got like warehouses and factories
*  that have our camera monitoring solution deployed. And we're like, actually not that good at knowing
*  what's going on. And what do you think we could do about it? And I'm like, I hate to tell you this,
*  but I think the answer might be use a foundation model, because they're getting really quite good
*  at a lot of this stuff. Well, that just brought to mind fine tuning in general and fine tuning
*  with images. That was one thing I actually didn't get a chance to check into today to see if there's
*  any kind of updates there. But I do think that is fine tuning in a multimodal way, I think is
*  definitely going to be a huge unlock. If you could fine tune Flash to do those kinds of tasks. I
*  also think about just like monitoring people in senior living communities. You know, people hate
*  to wear those like fall monitors on their wrists. But if you could, you know, detect when somebody
*  falls within one minute, you'd be saving lives literally when people like take their wristband
*  off and then fall. So I think just a ton of, of course, people will be concerned about privacy,
*  but so many different use cases for a fine tunable Flash, especially as it gets into fine
*  tuning with images as well. Yeah, it's on the roadmap. So hopefully next time we talk, we'll
*  be able to dive more into the multimodal fine tuning piece. But I think your comment about
*  this sort of, or more broadly, the future looks like these large foundation models,
*  replacing a lot of the sort of domain specific computer vision models. As somebody who spent
*  the early part of my career training domain specific computer vision models, like I can almost,
*  my assumption is like the problem I spent a year training a model to solve and like going through
*  this entire data curation iteration process, probably just works out of the box now with some
*  of these large models like Gemini. And I think as the model crank continues to turn, it's like more
*  and more of those domain specific computer vision models likely are just capable out of the box for
*  our foundation models. And I think to your point, image fine tuning is probably like the right sort
*  of knob as you try to get to the product, the level of like production scale and quality that
*  you need to actually flip the switch of replacing some of those systems. But yeah, it gets me excited
*  not only for the existing solutions, but there's so many things that could benefit from that sort
*  of continuous monitoring or just like being able to visually understand the world that isn't deployed
*  today because it's cost prohibitive and because like I don't, you know, a small business owner
*  doesn't have enough money to go and pay a bunch of AI ML experts to train a domain specific model
*  for the very niche problem and the future where you can just throw a prompt in with the model and
*  say, here's the state of my problem. Here's a couple images of the challenge I'm having helped
*  me solve this problem. I think is incredibly exciting to think about. Yeah, multimodal fine
*  tuning is some earth requests that we get pretty often. As Logan said, we're thinking about it.
*  Do want to call out though that we recently released the ability to get access to a fine
*  tuned models as well as tune models using API keys. That was the other thing that we used to
*  get requested for a lot. So we did make that available. So now users no longer need to just
*  be using OAuth. They can actually use API keys for tuning. Gotcha. Okay, cool. Yeah, that sounds
*  quite enabling. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The cognitive revolution is brought to you by element, a zero sugar electrolyte drink mix
*  that's working to change how we think about the role of salt in hydration and performance.
*  I have to say, when I started an AI podcast, I never thought we'd be sponsored by a drink company.
*  But when element inquired about a possible sponsorship, they also offered to send me a
*  sample pack. And so I figured might as well try it out. When the sample arrived, my wife, Amy,
*  could not believe what a perfect fit it was for me specifically. For years, I have felt that my
*  body needs more salt than nutrition labels indicate. And so I was interested to learn that the element
*  formula is based on a growing body of research suggesting that most people perform best with two
*  to three times more sodium than official guidelines recommend. I was also fascinated to see that they
*  specifically recommend it for people who fast regularly, since I personally don't eat until
*  dinner time most days. Obviously, I'm not a doctor and what my body responds well to may or may not
*  work well for you. But after drinking element for a couple of weeks, I can sincerely say that I
*  really do enjoy the product. My favorite flavors so far are the mango chili and grapefruit. And I,
*  for one, also enjoy the raw, unflavored version, which reminds me of the taste of the ocean.
*  If you're curious about optimizing your electrolyte intake, you can support the show
*  and get a free sample pack with any purchase by visiting drink element.com slash TCR. That's drink
*  LMNT.com slash TCR. Let's talk about the grounding feature. That's obviously the big news of the day.
*  I want to understand it in its just object level, what it can do. I think the basic idea that it
*  consults Google search and then uses that information to help generate the response,
*  that's pretty intuitive, probably for most people. Probably a lot of people have done what I've also
*  done in the past, which is use some other search API and then get those results and feed that into
*  language model. So this definitely streamlines that. I would be interested to hear what your other
*  exciting findings, observations, hidden gem features related to it are. And then maybe we
*  could zoom out for a second and talk about the broader landscape. I'm very confused right now
*  as to whether we're seeing convergence of models across different providers or divergence.
*  I can ramble on about this forever, but this does seem to be at least one notable place where
*  Google is doing something that will be difficult for other people to replicate and does suggest
*  a certain divergence. Yeah, happy to get into it. I had a question for you though, first.
*  You said you had implemented search based drag before. Is the streamlining that you've
*  experienced with the feature we're releasing, was that helpful for you? Yeah, I think so. I mean,
*  I obviously haven't put it through a huge volume of use. What I have done prior to now has typically
*  been to use the Brave Search API, which is pretty good and pretty fast and pretty cheap. So I'm
*  definitely like, you know, have nothing but positive things to say about the Brave Search
*  API. Then I feed that result into another language model and have it generate a summary. For,
*  you know, just overall simplicity and just immediacy of getting something like this running,
*  having it all in one is an obvious win. I don't have like huge benchmarks to know how my
*  coverage would compare, but I would have to assume that Google would have
*  better coverage in the long tail of search. I'm typically searching, like at Waymark,
*  we're searching for long tail small businesses. Brave has done pretty well there, but I would
*  imagine Google would have better coverage. Beyond that, I think I still have to get a little bit
*  more into the details to really have even a vibe check. But certainly my brand trust in the Google
*  search stack, obviously built over a long, long time, is such that I would probably tell people
*  to try that first at this point. Yeah, that makes sense. Thanks for that. Yeah. So as you said,
*  right, like the basic intuition here is get information from search to bolster the model's
*  response to make it more accurate, to give fresher answers, to give better answers on long tail
*  queries the model doesn't do as well on. And the other thing we found in the process of testing
*  this out is sometimes just with having search grounding on, you get a much richer answer.
*  For example, if you were to ask it, you know, what is the smallest horse breed in the world?
*  The model by itself might just give you the answer, which is Fala Bella. I hope I'm pronouncing it
*  right. But search grounding, if you have it on, will give you more details around like here is
*  their average size, they found in Argentina and a lot more richer detail, which as you can imagine,
*  for certain applications is better. Another example here is somewhere where Logan and I have
*  a difference of opinion. But like if you ask the model, what's the capital of Mars, the model will
*  say Mars doesn't have a capital. And that's the answer Logan prefers. The version I prefer is the
*  one with search grounding on, which goes into a much more richer detail about here is a list of
*  sci fi books, which have had capitals of Mars. So, you know, that's also where developers can
*  account for individual preferences. Coming back to your question, I think there was a question in
*  there perhaps around what kind of queries would developers want to ground on. And one of the things
*  I do want to call out that we're making available with this feature is there are two layers of
*  control almost. So the first one is whether to have grounding on or off. And that's a toggle in
*  AI Studio. And it's a decision to pass the grounding as a tool in the API. In addition,
*  we have this additional parameter called dynamic retrieval. And what that parameter does is it lets
*  the developer tell the system that even if search grounding is on, how often should it be invoked?
*  So if you set the dynamic retrieval parameter to zero or to a low value, then search grounding is
*  invoked pretty often, like in all sorts of queries. And this might be a use case where
*  developers just want to provide that richer layer of detail in their answers. Where on the other
*  hand, if you set the dynamic retrieval parameter to a higher value, let's say 0.7, 0.8, then you're
*  saying be selective about when you ground. And that might sort of correlate with use cases where,
*  like recency, a question that has a high degree of recency requirements, that's a place where
*  you know you need to ground because that might be beyond knowledge cutoff. And so this dynamic
*  retrieval is an additional parameter which kind of lets people decide how often should grounding
*  happen even after it's turned on. Nathan, should we do a quick demo? We can pull it up if that's
*  useful to show. I don't know how much of your audience listens versus watches on YouTube.
*  I think mostly it's listening, but we still could. I defer to you.
*  With apologies to Tyler Cowen, I always say this is the AI conversation I want to have. And the
*  fact that other people want to listen to it is kind of a happy accident. Yeah, well, let's keep
*  going for now because I know time is kind of short and it is easy to find. If you get into the AI
*  studio, you drop down to the lower right-hand side, it's there. I did find that before. I was
*  going to bring that up if you didn't. I do think that slider, it's essentially kind of another,
*  feels like a temperature sort of score where you're like, turn it down to zero. I'm always
*  grounding. Turn it up to one, it's never grounding. And then in the middle, you're obviously
*  trusting the fates. But I definitely see myself, I think that'll be really interesting to play with
*  the in-between space. My immediate instinct is to just always use it for the kinds of things where
*  I think I might need it. But it'll be interesting to see how much I can delegate that decision-making
*  to the model versus sort of telling it like, no, I do want you to always go get the latest information.
*  Yeah. May I just add a couple of things, Nathan? The other two aspects of this release are when
*  you do get the answers from grounding, we do link out to the grounding sources, both in line and
*  there's a little table list at the bottom. And the reason for that is to fold one, we do want to
*  link out to our publisher ecosystem and send people on those informational journeys to get
*  more content. And we also find that in testing, users love this. They love being able to get the
*  answer, but then being able to validate the answer or get more nuance around the answer by clicking
*  on those links. So we do provide those grounding sources and we provide search suggestions, which
*  are examples of the type of queries to Google search that would have given content similar to
*  what we have in the answer. Yeah, Nathan, I think this sort of directional line that this draws
*  is the sort of the future where people at scale have a deeper trust in AI systems because they
*  have this sort of evidence of, and I can see the citations and the grounding materials themselves,
*  and then also go out and click through and validate those answers from models. I think
*  the early innings of AI and generative AI specifically have been putting a little bit
*  of trust in the model. Everyone has this notion that you shouldn't really trust the models,
*  but you should in some cases, and it's kind of murky where that line gets drawn. And I think
*  the next sort of inning of this AI explosion is going to be actually putting those citations in
*  the hands of both developers to then build products that include that, but also just generally the
*  applications being able to have a little bit deeper trust knowing that the materials are
*  actually coming not just from the weights of the model, but actually reputable sources.
*  It's funny that you say innings because my first trial on this with the thing at
*  zero and one respectively was what's the state of the world series. And that's obviously very
*  obvious one where without the grounding, the 2023 world series is the most recent world series that
*  it knows about. And with the search enabled, then it's obviously able to go out there and get that
*  information. So lots of things like that. If I were to summarize the kind of big picture,
*  you're a new developer. I don't know too much about what you're doing, but I'm just kind of
*  trying to coach you on which provider you should look at first. I would say right now, OpenAI has
*  the O1 series that has this reasoning capability. If you have really hard problems,
*  you might want to look at that. Claude has this new computer use thing, which is kind of amazing.
*  So if you're doing something that's like a gentic in a unstructured environment, you might want to
*  look at that. Gemini has the super long context and now has the search grounding. And then of
*  course, Meta has the open weights. I guess, fair summary. And how much time do you guys spend
*  thinking about competing on those areas where the others have sort of taken a lead for the moment
*  versus just charting your own course? I think the expectation from developers,
*  and you sort of see this play out online, is someone gets a capability and then the question
*  is like, when can I get that capability with this model provider? So I think that's been the general
*  trend of, for some of these large, very large exciting frontier capabilities, and for some
*  compute stuff, computers using agents, computers controlling stuff, or AI controlling the computer,
*  it's incredibly exciting. And it's clear that it's captured the imagination of developers,
*  all things that are exciting and interesting to us. So we'll see what ends up landing in the future,
*  but hopefully, I think you have to continue to have the sort of base layer of capabilities
*  that developers expect. And then for us, it's like, what can we do that's like net different,
*  specifically leveraging the things that Google is uniquely good at. And that's large scale
*  infrastructure. And you can sort of see that play out with long context, search with search
*  grounding and the whole ecosystem of other things that are unique to Google that other companies
*  don't do. Yeah, I would say that's exactly right. We think of our roadmap in almost three buckets.
*  The first one is what's the excellent work that other players in the ecosystem are doing,
*  and we do strive to learn from them. The second one is what is it that Google can uniquely bring
*  to the table, search grounding, you know, in vertex, you can use YouTube links, which is
*  something we hope to bring to AI studio, things like that. And then the third one is just overall
*  API experience, just basic, boring, but very important stuff, like have the best error codes,
*  have great support, have really good rate limits, make sure the price is such that no developer
*  should be deterred from building with our API. So that's the third bucket for us.
*  And we also get the luxury of learning from other people's, I don't know, want to say mistakes,
*  but like, what is the feedback from developers? And I think a really tactical example of this
*  is code execution and like the base capability of code execution as a tool, does it exist in
*  the default endpoint across other providers? And it does, like it is literally a toggle in the UI
*  and the tool that you can pass in to like just sending a generic request. And I think the lesson
*  learned was like, developers want this capability and they don't want to have to use a different
*  version of the API for some very specific use case. How can we expose that? And that was the
*  same sort of principle for search grounding. It was like, we don't want to force developers to go
*  use some other variant of our API. We really want them to just be able to use the basic version
*  that most people are using and just toggle it on by simply passing a tool call. So in many respects,
*  we get to Sharitha's point, like learn from the others in the ecosystem, which is super helpful.
*  Yeah, that's interesting. Another instance of that, that I came across today that I'm interested in
*  how you think about is the, in the context of the structured outputs, and this gets really into the
*  weeds, but this is a very useful feature where I can say exactly what schema I want the response
*  to come back to me in. And as a developer, that's obviously super useful because now I know that I'm
*  going to have some structure of data that I can map onto my application, whatever. So I think that
*  should be pretty intuitive for most people. I had been using the OpenAI one. It has all fields
*  required by default. So whatever schema you give it, it's going to give you every single one of
*  those fields back, even if it kind of leaves them empty or they're not really relevant in a certain
*  case or whatever. In the Gemini one, it seems, if I understand correctly, that they're all optional
*  and then you can tag them as required. And that took me a few minutes to figure out. Again, the
*  whole thing only took like two hours to do the whole integration. So it was pretty snappy, but
*  I wonder how you think about those kinds of things. Was that like a, we think that they're doing it
*  not quite right and we want to do it better. And how do you balance that against like trying to
*  make it sort of a drop-in alternative in some cases? Cause I think that was literally the only
*  outright error that I hit in the entire process where I was like confused momentarily as to what
*  was going on. So what do you just think about making those design decisions and like, you know,
*  drafting off of somebody else's momentum versus deciding like you think there's a better way to go?
*  I think this is one of the toughest pieces of balance to strike. The best outcome is our thing
*  is different and it's different in the way that sort of resonates with a developer's mental model
*  of how a feature would work. And I think like having priors from a different provider in the
*  ecosystem and bringing that prior, I think is like one user journey. I think the other user journey
*  is like, maybe this is the first time you're sort of wrapping your head around this and like, what
*  would you expect it to work or how would you expect it to work by default? And I think that
*  particular example, like having optional and then the required fields to my understanding, like
*  resonates more with just like how JSON structures work in general. Like if I were to define JSON,
*  I think it is like implicitly all optional by default and then you would tag fields as required.
*  But you sort of, yeah, you surely pay sort of the cost for trying to lean more towards like,
*  what is a developer's innate assumption versus what are others in the ecosystem doing? And that's
*  one of those tough things where there's no perfect answer, but you have to sort of, yeah, make that
*  trade-off. Yeah. And I think this can go either way, right? Like we took this position, but there's
*  a lot to learn. I remember listening to Michelle Pokras from OpenAI on a podcast and they had a
*  lot of deliberation before they made all those fields required because they just wanted to ensure
*  that developers knew what was needed to get back that accurate output. So that was the choice they
*  made. We decided to adhere to the fact that the implicit assumption in JSON is all fields are
*  optional, but we'll learn as we have these features out into the open. I think that one
*  other similar one is context caching where we were the first provider to release context caching,
*  but now Anthropic has their version, OpenAI has their version, and we're getting a lot of feedback
*  from developers in terms of what works well for our version and where we could improve.
*  And we're definitely looking into that. Cool. So anything you think developers should be thinking
*  more about or any other parting thoughts? I mean, obviously, mostly the focus for today was on
*  search grounding, but in general, we're constantly looking for feedback from developers in terms of
*  how they're using our features and how we can make it even better. So I just want to invite
*  your audience to keep doing that and reaching out to Logan or reaching out to anyone else.
*  Yeah, this was a ton of fun, Nathan. Thanks for having us. Hopefully we'll see you at IO next
*  year again and we can catch up in person and see whatever cool stuff ends up landing. Yeah, we're
*  all waiting with bated breath for the next big thing. It's funny. The treadmill is just speeding
*  up, I feel like every single day. For now, Shrestha Basumalik and Logan Kilpatrick,
*  thank you for being part of the Cognitive Revolution. Thank you, Nathan. Thank you.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the
*  show. So please don't hesitate to reach out via email at tcr at turpentine.co or you can
*  DM me on the social media platform of your choice.

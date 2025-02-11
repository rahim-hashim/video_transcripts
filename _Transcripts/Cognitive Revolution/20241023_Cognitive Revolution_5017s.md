---
Date Generated: October 24, 2024
Transcription Model: whisper medium 20231117
Length: 5017s
Video Keywords: []
Video Views: 612
Video Rating: None
Video Description: In this episode of The Cognitive Revolution, Nathan delves into the fascinating world of AI-generated research ideas with Stanford PhD student Chenglei Si. They discuss a groundbreaking study that pits AI against human researchers in generating novel AI research concepts. Learn about the surprising results that show AI-generated ideas scoring higher on novelty and excitement, and explore the implications for the future of AI research and development. Join us for an insightful conversation that challenges our understanding of AI capabilities and their potential impact on scientific discovery.

Link to the research paper being discussed: https://arxiv.org/abs/2409.04109

Be notified early when Turpentine's drops new publication: https://www.turpentine.co/exclusiveaccess

SPONSORS:
Weights & Biases RAG++: Advanced training for building production-ready RAG applications. Learn from experts to overcome LLM challenges, evaluate systematically, and integrate advanced features. Includes free Cohere credits. Visit https://wandb.me/cr to start the RAG++ course today.

Shopify: Shopify is the world's leading e-commerce platform, offering a market-leading checkout system and exclusive AI apps like Quikly. Nobody does selling better than Shopify. Get a $1 per month trial at https://shopify.com/cognitive.

Notion: Notion offers powerful workflow and automation templates, perfect for streamlining processes and laying the groundwork for AI-driven automation. With Notion AI, you can search across thousands of documents from various platforms, generating highly relevant analysis and content tailored just for you - try it for free at https://notion.com/cognitiverevolution

Brave: The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Oracle: Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

CHAPTERS:
(00:00:00) About the Show
(00:00:22) Sponsors: Weights & Biases RAG++
(00:01:28) About the Episode
(00:05:30) Introducing Chenglei
(00:06:22) Path to Automating Research
(00:07:58) Notable AI Research Projects
(00:15:26) Evaluating Research Ideas (Part 1)
(00:19:39) Sponsors: Shopify | Notion
(00:22:33) Evaluating Research Ideas (Part 2)
(00:25:49) Research Setup and Design
(00:29:38) AI Prompting and Idea Generation
(00:34:40) Diversity vs. Quality of Ideas (Part 1)
(00:34:40) Sponsors: Brave | Oracle
(00:36:44) Diversity vs. Quality of Ideas (Part 2)
(00:42:05) Inference Scaling and Execution
(00:45:04) Anonymizing and Evaluating Ideas
(00:53:22) Headline Results and Analysis
(00:58:45) Observations and Insights
(01:09:02) Novelty Indicators and Deception
(01:11:59) Top AI-Generated Ideas
(01:14:41) Next Steps and Future Directions
(01:20:43) Expectations for the Future
(01:23:14) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Can AIs Generate Novel Research Ideas? with lead author Chenglei Si
**Cognitive Revolution:** [October 23, 2024](https://www.youtube.com/watch?v=IOCi6q3KvX4)
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
*  Hello, and welcome back to the Cognitive Revolution. Today my guest is Cheng Lei-Sih,
*  a PhD student at Stanford who's developing ways to use large language models to automate research.
*  He's lead author of a fascinating new paper that asks the question,
*  can large language models generate novel research ideas?
*  This question has become one of the most important in the entire field,
*  as the ability to generate research ideas that are truly worth pursuing,
*  particularly in the domain of AI, has long been considered a key precursor to recursive self
*  improvement loops and a possible intelligence explosion. Since the early days of GPT-4,
*  we've seen several notable attempts to create AI research assistance, including projects like
*  Co-Scientist from Gabe Gomez's group at CMU, which we did a full episode on, and more recently the AI
*  scientist paper from Japanese company Sakana AI as well. These systems demonstrated capabilities
*  that would have seemed impossible just a couple years ago, including translating natural language
*  instructions to chemistry protocols and using the Semantic Scholar API to assess research ideas for
*  originality. Nevertheless, the question of whether AI systems can produce high value research ideas,
*  true eureka moments, has remained the subject of fierce debate. Cheng Lei and his collaborators
*  set out to shine light on this subject with an ambitious study. They asked more than 100 PhD
*  researchers working in AI for new research ideas, incentivizing quality with cash prizes for the
*  best ideas, and then asked Claude to generate new ideas as well. After processing the text in an
*  attempt to create a level playing field for evaluation, they then had expert reviewers
*  rate all of the ideas without knowing their source. The results? The AI generated ideas
*  scored significantly higher on both novelty and excitement. Now, as with many recent AI results,
*  this paper has become something of a Rorschach test. Those inclined to believe in rapid AI
*  progress see it as a major milestone, while skeptics criticize the methodology, somewhat unfairly in my
*  view, but you can judge for yourself as you listen, and more persuasively in my mind, emphasize that
*  this work, which focuses specifically on prompting techniques for language models, may not generalize
*  to the harder sciences. Personally, I agree that we cannot confidently project this one result onto
*  other domains, but I find the experimental setup here to be quite well done, the statistically
*  significant results seem credible, and I think Chunlei's individual observations are worth taking
*  very seriously as evidence too. Everyone listening to this show should be familiar with the AI maxim
*  to look at your data, and nobody has spent more time with the raw outputs than Chunlei has,
*  so when he reports that nine of his ten favorite ideas from this entire project turned out to be
*  AI-generated, and that the AI ideas are generally more out of the box and less grounded in existing
*  work than human ideas, I think we would do well to listen. Overall, my feeling right now is that
*  we're at a sort of tipping point, where the Call of 3.5 Sonnet and GPT-40 class of models can sometimes,
*  with great effort put into system design and many millions of tokens to earn, sometimes generate
*  meaningful novel research ideas, but not yet in a way that makes frontier research dramatically
*  more accessible or scalable. The next generation of models, starting with the O1 series, seems to
*  me pretty likely to change that. I've been coding with O1 and Cursor a lot lately, and I've been
*  really struck by how effectively O1 can review my entire codebase and my plan for a new feature,
*  and return both a critique of my approach and a recommended alternative that is usually
*  genuinely better. As a community, we're still figuring out exactly what the limits to these
*  capabilities are. But if I had to bet, I'd say that systems like Chunle's, powered by O1 and a
*  bigger inference budget, might well produce undeniably needle-moving results quite soon.
*  As always, if you're finding value in the show, we appreciate it when folks take a moment to share
*  it with friends, write us a review on Apple Podcasts or Spotify, or just leave us a comment
*  on YouTube. And we welcome your feedback via our website, cognitiverevolution.ai, or by DMing me on
*  your favorite social network. For now, I hope you enjoy this conversation on the emerging reality
*  of AI automated research with Chunle Si. Chunle Si, PhD student at Stanford, researching the automation
*  of research. Welcome to the cognitive revolution. Thank you. Excited to be here. I'm excited for
*  this conversation. I think you are working on a super interesting frontier, and your recent paper
*  with a provocative question in the title has certainly caught my attention and I think the
*  attention of the field more broadly. So the paper that we're here to really go deep on today is
*  called, Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100-plus NLP
*  Researchers. I'm looking forward to breaking this down and really getting into the nitty gritty of
*  the methodology and what we can learn from it and what we should maybe take away from this and expect
*  to see as we go forward into the near future. For starters, want to maybe just give me a little bit
*  of your background? How did you get to focus on this question of automating research and maybe
*  look here to some of the results from the last year or two that you have found to be most compelling?
*  Yeah. So I came from a very NLP background. I was doing NLP research during my undergrad.
*  And then I came to Stanford last year and then I met my advisors,
*  Steehan Tarsu. And I always wanted to do something different for my PhD. And back then, the big
*  background in the whole NLP field is that large language models are getting really good. And then
*  you saw some really impressive performance on things like reasoning, math, and coding,
*  and stuff like that. And I feel like it probably could give opportunities to some very new
*  applications. And as someone who has done research for many years, I feel like being able to automate
*  research feels like something very different and very exciting. And importantly, I think it will
*  have huge practical implications to the entire field. And I just got excited about this agenda
*  right away. And I'm lucky that most of my advisors are very excited about this whole agenda as well.
*  So we actually got started on this whole thing pretty early, I think roughly one year ago.
*  This whole project actually took around a year to finish. Yeah, interesting. And I trust that the
*  human parts of that took the most legwork and took the most time. That is often the striking
*  difference these days. Yeah, building the agent itself took us like two or three months. And then
*  finding all the people and doing the actual human study took us like eight months or so.
*  Yeah, interesting. So before we dive into the details of your paper, what other projects,
*  they don't necessarily have to be, could be academic papers, but it could also be open source
*  projects that have captured your imagination and kind of stand out to you as the notable
*  step change improvements on the road to this destination of automated research.
*  Yeah. So I think to me personally, there's this line of work on self-improving AI. There has been
*  discussion on whether AI keeps getting better. There will be a point where AI can be even smarter
*  than humans. At that point, how do we possibly keep improving AI if AI is getting smarter than
*  us humans? It gives rise to this idea that maybe we can let the smarter AI to propose new ideas
*  and improve itself. There has been some preliminary attempts on that. There has been some work done by
*  folks here at Stanford like Eric Zuckerman. I think that's one inspiration for this line of work.
*  But of course, there's also another line of work on building tools that can assist researchers. A
*  lot of colleagues from CI, folks like Semantic Scholar, a bunch of other people have been doing
*  this for many years. So research assistant tools, creative support tools is another inspiration for
*  this. But I think we really took a very different approach in the sense that once you do something
*  that sounds even more aggressive, in the sense that we want to see if we can possibly automate
*  the entire research process, rather than just build some assistant tools there.
*  Yeah. I think you've zeroed in on a really important question. I've looked for what it's
*  worth that. This is an area I try to keep up with because it feels to me like if we are going to
*  have an intelligence explosion, this is the form that it's going to take. It's going to be,
*  and I'm by no means alone in this analysis or original in coming up with this analysis. But
*  basically, it seems like the expectation from the field is at some point, we're going to start to
*  see AI systems that can make meaningful contributions to ML research. And if ML research
*  becomes 10x, 100x, 1000x more productive, because we can spin up AI ML researchers and they can
*  actually take real bites out of big problems, then it's really hard to say how good the overall
*  resulting models could get. And that could take us into a different regime. So it feels like
*  there's this sort of tipping point, possibly where if we can't get over that hump, then things maybe
*  stay somewhat normal. And if we do get over that hump, then kind of all bets are off and the future
*  starts to look quite unpredictable and potentially quite weird. I guess for starters, is that your
*  mental model of why this matters so much in the first place? Yes, you mentioned the word
*  intelligence explosion. So I've read the whole situation awareness thing that Leopold wrote.
*  My advisor Tatsu was warning me that using intelligence explosion would sound too aggressive
*  for an academic setting. But I think on this podcast, it's probably fine. So yes, roughly,
*  that was one exciting vision that I kind of want to pursue. This very interesting data point,
*  if you remember, there's a figure there where Leopold was saying,
*  around the year of 2028, we would be able to get automated AIR. So AIR was the lead author on the
*  GD paper. So if there was a point where we're able to automate AIR and we scale this up,
*  that means we'll have massive increase in the way AI can improve itself. That would be insane.
*  But we want to, you know, maybe take a step back. Automating AIR is a pretty difficult role. There's
*  only one Alec in the whole AI field. So maybe once you really see the current generation of
*  launch models, how good they are right now, I want to compare that with a more reasonable
*  baseline. So maybe we want to see how do they compare with, let's say, average PhD students.
*  I want to offer a concrete benchmarking point to gauge the progress that we have made so far.
*  So that was the motivation for the whole thing. Yeah. Okay, cool. So just to, and by the way,
*  Alec Radford has been making the rounds on Twitter just today as, or in the last like 24 hours,
*  we're recording on 1st of October. And he's been a popular answer to a question that somebody posed,
*  which was, who is the most important or influential scientist that is not very well known? And people
*  are piling on to say Alec Radford is the answer to that question. That is indeed an extremely
*  high bar for automation. To just further tee up the specific question that you're asking
*  with this research around using LLMs to generate novel research ideas. I think it is worth taking
*  a minute to just review a couple of my personal favorite highlights from the research over the
*  last year. Because I do think that has been an area where it hasn't quite been there yet.
*  It feels like we've sort of been always a little bit short. One that came out very quickly after
*  GPT-4 was released and we actually had the lead author Gabe Gomez on
*  the show for a prior episode was called Co-Scientist. And they put together a really
*  nice early, but I think has stood the test of time, agent framework that allowed a user to
*  basically say something like, please synthesize aspirin for me. And then the system would do
*  everything needed to synthesize aspirin, including looking up how do you synthesize aspirin,
*  translating that to actual instructions that could be sent over to an automated lab.
*  They were integrating this with Emerald Cloud Lab at Carnegie Mellon. And you can actually program
*  a real physical lab via an API to carry out the step-by-step protocol that you want to run.
*  And that was amazing. To go from a natural language sentence all the way through to
*  a purified powder getting spit out the other end of a system like that. I was like, man, this is a
*  major result. And obviously that's why I wanted to have him on the show back then.
*  But the one thing that I would say at that time was it did not seem to me like the AI was actually
*  coming up with meaningful ideas. So in my review of that paper, I called it, the question was like,
*  is this text to science or text to experiment? And I was kind of like, yeah, I think it's more
*  text to protocol because the AI at that time wasn't really generating the idea so much as taking the
*  idea and figuring out how to break that down into steps and execute on it. But that was never a
*  big milestone. I don't know if you have any comment on that one before we move on, but I'll highlight
*  a couple other ones and then we'll get into yours. Sure. I think the idea is cool for sure. There
*  has been similar attempts in maybe other areas. Our friends at Sakana AI, for example, has an AI
*  sentence paper that also tried to improve what the engine system is. I think the high level
*  research agenda is exciting for sure. But I think the tricky thing is the evaluation part is really
*  difficult, especially in scientific research. How do you possibly evaluate that research? Even for
*  academic settings, we do peer review. That isn't the perfect solution either. So I think all this
*  really voices onto the technical challenge of doing evaluation. And that is really the cracks
*  that we're trying to focus in this paper here. Yeah. The AI scientist was another one that was
*  on my list. And I thought that one was a notable step forward. I mean, all these things have their
*  critiques and I feel it's like a bit of a Rorschach test that tells you often as much about the critic
*  of the paper, whether positive or negative in their assessment, as it does about the research
*  in some ways because there is just so much room for interpretation still of these results. I find
*  that to be fascinating. The AI scientist, to me though, did take a step forward in that it
*  introduced a mechanism for generating a bunch of ideas and also trying to identify which of those
*  generated ideas were the most novel ideas. And they used the semantic scholar API to help with that.
*  So they would have a bunch of ideas generated, then go do a search against the semantic scholar
*  corpus of information to pull back as much related stuff as possible. And then they would try to see
*  has this already been done? To what degree does this seem like it's already represented in the
*  literature versus if not, then that's more likely to be a meaningfully novel idea. And that would
*  be the kind of idea that they would want to prioritize. The reviews of the actual AI written
*  papers that came out of that didn't seem like they were necessarily going to get admitted to
*  top conferences. And even in their own assessment, the Sakana team basically said this would be like
*  the work of an early grad student that definitely needs more advising from some of you has better
*  zoomed out context on the field. But I did still think that was a notable mechanism that seemed to
*  show the way to where this was going. I mean, one of the ways I describe this is,
*  do we get Eureka moments from AI systems or not? And initially with GPT-4, I used to say,
*  no Eureka moments. That was my headline for GPT-4 performance. And then we saw the Eureka paper,
*  and that was out of Nvidia, Jim Fan and the group. And there they used GPT-4 to write
*  reward functions for robot hand reinforcement learning. And they saw that GPT-4 outperformed
*  human authors of these reward functions. And I always am fascinated by that because I'm like,
*  geez, it takes some real know-how to even write a reward function in the first place. This is not
*  something that any old person off the street can do. You're engaging here with a certain level of
*  expertise as a baseline and still seeing GPT-4 perform above that. Not exactly. I mean, it's
*  sort of like a hypothesis. A reward function is how well is it going to work? You're making a guess
*  as to what would work. So I feel like that was kind of moving in that direction as well. And the
*  fact that it did outperform humans in something that was objectively measurable was quite notable
*  to me. Any other thoughts on that one? Next up is yours.
*  You know, my definition of a Eureka movement for automating research line work would be,
*  if one day you tell me you have an NGN agent that generated the idea and automatically executed the
*  idea and your full project, and you submit that project to a talk conference, and that project
*  actually gets the best paper award, then I would say that indicates a Eureka movement for me because
*  that means that piece of project is actually way better than the average that you get at the so-called
*  talk conferences. I think the AI science paper from Sakana that you mentioned, I think the
*  agent system, that's a nice prototype there, but the outcome, first of all, even using your own AI
*  reviewer, the score isn't really reaching the bar for New York's for example. And then second of all,
*  how much should we really trust the automatic reviewer? That's a question we actually touched
*  on in the paper as well. We did some analysis and find that automatic reviewer at this point isn't
*  really ready yet in the sense that if you measure the correlation between LIM reviewer and the
*  actual Qmax reviewer, the correlation is pretty low at the point. So maybe we shouldn't trust that
*  much about automatic reviewer at this point. So those are the comments for the whole AI science
*  today. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The Cognitive Revolution is brought to you by Shopify. I've known Shopify as the world's
*  leading e-commerce platform for years, but it was only recently when I started a project with my
*  friends at Quikly that I realized just how dominant Shopify really is. Quikly is an
*  urgency marketing platform that's been running innovative time-limited marketing activations
*  for major brands for years. Now we're working together to build an AI layer, which will use
*  generative AI to scale their service to long tail e-commerce businesses. And since Shopify has the
*  largest market share, the most robust APIs, and the most thriving application ecosystem,
*  we are building exclusively for the Shopify platform. So if you're building an e-commerce
*  business, upgrade to Shopify and you'll enjoy not only their market-leading checkout system,
*  but also an increasingly robust library of cutting-edge AI apps like Quikly,
*  many of which will be exclusive to Shopify on launch. Cognitive Revolution listeners can sign
*  up for a $1 per month trial period at Shopify.com slash Cognitive, where Cognitive is all lowercase.
*  Nobody does selling better than Shopify, so visit Shopify.com slash Cognitive to upgrade
*  your selling today. That's Shopify.com slash Cognitive. As a Cognitive Revolution listener,
*  you're obviously interested in cutting-edge AI technology. And with that in mind, I'm proud to
*  say that this episode is brought to you in part by Notion. Notion has been a clear leader in
*  high-value applications of generative AI since the wave began. Earlier this year, we had Notion
*  AI engineer Linus Lee on the podcast. The quality of his insights showcased the caliber of talent
*  that Notion employs. And that inside look at how Notion builds with AI is still extremely valuable.
*  Given my personal focus on AI automation recently, I specifically wanted to highlight
*  Notion's library of workflow and automation templates. If you're looking to streamline
*  your processes and lay the foundation for future AI-driven automation, these templates are an
*  excellent starting point. And even if you're not ready for full automation, you'll benefit
*  immediately from Notion AI, Notion's latest all-in-one AI implementation that searches through
*  thousands of documents, regardless of whether they live in Notion or on some other platform like
*  Slack or Google Docs, to deeply understand the context of your work and generate highly relevant
*  analysis and content just for you. Notion is used by more than half of Fortune 500 companies,
*  helping teams reduce emails, meetings, and time spent searching for information.
*  Want to try it? Head to Notion.com slash Cognitive Revolution. You can start for free and using our
*  link supports the show. So join me in giving Notion AI a shot today at Notion.com slash Cognitive
*  Revolution.
*  Yeah, I like your comment about, first of all, it's always one of my refrains is like,
*  compared to what? So it's really important that we compare these things to the human alternative.
*  If there is one or whatever is kind of how is it being done now? I think the other thing that
*  people often forget is that the current thing is not perfect. Often it's actually quite a bit worse
*  than people imagine it to be. But I think you had a good kind of baseline in the paper on
*  comparing to the inter-rater reliability of actual human judges for the conferences.
*  So somebody might say, the skeptic of the human performance, which is often a role I play,
*  might say like, well, how consistent are the human raters? And is this any worse than that?
*  And the answer here is, you can fill in a little bit of the details, but the human
*  raters actually do agree more than the AI raters agree with them. There is still something
*  measurably not accomplished with the AI paper evaluator.
*  Right. So at this point, it's true that human reviewers at the conferences tend to have higher
*  agreement than the agreement between AI reviewer and the human reviewer. So I think that's one
*  evidence that current non-trivial models are not ready for the automating the reviewer part yet.
*  But even if, let's say, one day non-trivial models keep getting better, the agreement somehow gets
*  higher. I think it's still questionable whether we should fully trust the automatic reviewing
*  on such a subjective and pretty high-stake task, I would say. If you look at the actual human
*  agreement, you realize reviewing is really a very subjective task in the sense that even
*  the expert reviewers at talk conferences like iClear in Europe, their agreement is still pretty
*  low in general. So I think it really highlights the challenge of evaluating research ideas in
*  general. Yeah. So I'm looking at the paper. This is table 11 in your paper. So you basically are
*  comparing four main results. One is, and I guess first of all, just to be very clear,
*  the question here is accept, not accept. Does it boil down to that binary judgment?
*  The question is actually even simpler. In that, in a sense, we basically try to get the lower 50%
*  of papers and then we combine that in your binary judgment of something like accept or not accept.
*  And then we measure the decision agreement between two sets of reviewers.
*  Gotcha. So random is 50% in this setup. The NURIPS judges only got up to 66%. So they're
*  agreeing not one out of two, but two out of three times. The iCLR judges got up to 71.9%.
*  So they're close to three out of four, but still not quite there. And then your implementation
*  gets to 56% agreement with the human judges. So it is an incredibly noisy thing, but there is still
*  like a meaningful delta between what the AI system can do and what the humans could do.
*  When it comes to this specific task of judging the papers.
*  Okay, cool. Well, let's go back to the hypothesis generation. Give us the setup for how you sought
*  to answer this question. You already said it took months to build the agent, a lot more months to
*  build the dataset from humans, but give us the whole setup of how you set out to answer this
*  question of can LLMs generate novel research ideas?
*  Right. So given the whole question, I think there are two high-level principles that we want to
*  achieve. The first thing is, what do you set out a proper human baseline?
*  Of course, without a human baseline, you can still measure some numbers on some metrics,
*  but people might ask, what do those numbers really mean? We want a concrete benchmarking
*  point by comparing to a reasonable baseline there. I feel like PhD students, they really
*  represent the experts in this task. So we want to compare to that for sure. And then the second
*  thing is also, we want to set up proper design protocol to avoid any potential confounders.
*  And we want to have expert reviewers to do all the judgment, because I mentioned a bunch of
*  caveats on using language models for reviews. So all the reviewing is done by expert researchers
*  in this case. So the high-level design is then what you have one branch where all the ideas are
*  generated by AI, and another branch where all the ideas are generated by human researchers,
*  and one you have a blind review where expert researchers come in and score all the ideas
*  without knowing which one is which, and then we compare the scores. But in the actual event,
*  you can go to adding a certain condition, which we call the AI ideas plus human re-ranking.
*  The consideration of that is that we have a built-in ranking part in the idea generation agent,
*  where the agent will generate thousands of ideas on each topic. And then the agent will automatically
*  select the best ones. It's a little bit similar to what you mentioned in the Sakana paper.
*  So after this ranking, we get the best ideas generated by AI as ranked by the AI itself.
*  Those ideas will be the condition of AI ideas. And then we realize that the AI ranking isn't
*  really perfect yet. So it's possible that among all the couple thousand ideas generated by AI,
*  there could be some really good ones, but they're not being ranked as top by the AI because the
*  re-ranking is not working perfectly yet. So once you have a better estimate of the upper bound,
*  once you find the best ideas being generated by AI, and that's where we manually actually look at
*  all the general ideas and select the best ones that we consider as the best. And that's what we
*  call AI ideas plus human re-ranking. So in that condition, all the ideas are still generated by
*  the AI agent, but the re-ranking is done by humans. So that is a certain condition. So that's the
*  experience set up. We will have one review, we'll assign ideas to all the expert researchers,
*  we'll score ideas along different metrics, including knowledge of the excitement,
*  feasibility and effectiveness. And then we'll compare the scores of different conditions.
*  And that's the whole design of the experiment.
*  Gotcha. So let me just say that back to you and make sure I've got it all right.
*  So there's two sources of ideas, obviously the humans and the AIs. You pay the humans for
*  their ideas. They were paid $300 for participating. And if I understand correctly,
*  there was also I think a couple of thousand dollar prizes for ideas that were judged to be
*  the best among the humans. So the participants are mostly grad students, PhD students in
*  machine learning, right? With a focus on natural language.
*  Mostly LD. Yeah.
*  So yeah, I think that's notable for a couple of reasons. Obviously,
*  certain amount of expertise there. That's definitely not nothing. And the thousand dollars
*  is not insignificant on the scale of a grad student salary. So presumably people would
*  at least be somewhat motivated to give a good idea and try to pick up the extra thousand bucks.
*  Then on the AI side, I think there's some really interesting implementation details in the paper.
*  Maybe you can give us a little bit more on how you're prompting the AI for ideas. I know that
*  they're... Because you're not just asking a simple question like, hey, can you give me some NLP
*  research ideas? You're actually bringing a sort of kernel set of ideas to it for it to expand on.
*  Maybe give us a little bit more on that. There are a couple of things that we put in
*  the prompt when trying to generate ideas. The first thing is we retrieve relative papers,
*  given the research topic, and then we'll put all those relative papers in the prompt to give some
*  inspiration there. Another thing is we give some demo examples. We actually manually construct
*  six demo examples based on existing papers. So those will be exemplar papers that we put in the
*  prompt. And then all the examples will follow the same format. So we define a template for how the
*  idea should be written up. So the template roughly includes things like motivation,
*  there's a problem set up, there's a proposed method, and there's an experiment plan, and then
*  there's also test examples, etc. So it's a very detailed template for writing the idea. So we
*  provide the template to the agent as well. And then in the prompt, we also include all those demo
*  examples, include all those greater work. And then we generate ideas in batches, because we want to
*  massively over-generate a number of ideas, and then select the best ones. There's a limit to
*  common tokens you can possibly generate in one generation. So we actually generate 16 batches.
*  So we generate five ideas in one batch, and then we keep generating. And one issue with this thing
*  is that it's possible that the agent will start repeating itself by generating the same ideas
*  over and over again. And that will be bad for us, because we want a large set of very diverse ideas
*  so that we can possibly find better ones there. So one thing we did is we will actually add all the
*  previous generate ideas titles into the prompt, and then ask the model, you shouldn't be repeating
*  what's already being generated. So that's one simple attempt on reducing repetition there.
*  But as noted in the paper, there's still a lot of repetition in the idea generation thing. We
*  did an analysis on that. We can touch more on that later. But on a high level, that's the idea
*  generation part. So we have the retrieval part, we have the template, we have the demo examples
*  there. And after generating all the examples, we have the ranking thing to select the best ideas
*  there. And this is with Claude35sonnet as the main model. Is there any sort of guidance you could
*  offer on how much, I presume you chose that because you found it to be best, is there a
*  measurement versus like GPT-4.0 or versus Gemini 1.5 that you could kind of help us calibrate
*  how much better 3.5.0 Sonnet is? Right, so we were initially actually using GPT-4.0 I think back then,
*  and then I heard a bunch of people in the lab saying, you know, Claude35 is really good on all
*  those signs and reasoning and coding of tasks. So I tried Claude35.5. It's difficult to give a
*  quantitative number on this, but we look at the two sets of ideas, generated by GPT-4.0 and also
*  Claude35.5. And intuitively, based on our judgment, it feels like Claude35.5.0 does have some
*  advantage in the task of generating ideas. That's why we stay with Claude35.5.0 for the entire
*  5.5. I know OVN just released O1.0 and I heard O1.0 is supposed to be really good on those
*  reasoning intensive tasks. It's possible O1.0 might be even better. We haven't done any
*  benchmarking on the target by some at least. Yeah, I'll be very interested to see the result
*  of that. Okay, so going back to the core of the setup, examples are put in structure of the
*  format of what an idea should look like is included for the AI to work from. It's also given
*  the ideas that it previously generated and told not to repeat. It nevertheless does repeat quite
*  a bit, but enough new ideas come out that you can... Tell us about the ratio. If I remember
*  correctly, you generated like 4,000 ideas, but found that only a couple hundred were truly original.
*  Around 200 ideas are non-duplicate. So basically, we use semantic similarity to judge whether a pair
*  of ideas are too similar to each other. We will filter this out. So after you do this filtering,
*  you get like 95% of the ideas out because they're duplicates. We actually have a curve in the paper
*  showing that in initial batches, most of the ideas will be novel, but as you generate more and more
*  in the later batches, most of the ideas will be just repeating previous ideas. If you calculate
*  the total number of non-duplicate ideas, the number starts to saturate in the later batches.
*  Eventually, it goes around 200 or so among the first generation. Hey, we'll continue our interview
*  in a moment after our word from our sponsors. This episode of the Cognitive Revolution is
*  sponsored by the Brave Search API. You may know of Brave as an alternative to Chrome,
*  but did you know that Brave has its own independent search engine powered by its own 20 billion page
*  index of the web? The Brave Search API gives developers reliable and affordable access to
*  programmable web search, auto-suggest, spell check, and more, with flexible plans for all types of
*  use cases from rag search to automated business intelligence. On top of that, it's up to three
*  times cheaper than Bing, all without compromising on quality, speed, or reliability. Over 700
*  businesses, including Cohere, Chegg, and Kagi, rely on the Brave Search API, and a recent survey
*  showed that 94% of customers would recommend it to their peers. To start building apps with the
*  power of the web, sign up at brave.com slash API and get up to 5,000 free monthly calls.
*  AI might be the most important new computer technology ever. It's storming every industry,
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing, and of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive of OCI at oracle.com
*  slash cognitive. That's oracle.com slash cognitive. Oracle.com slash cognitive.
*  So how do you think about that? I guess for one thing, it looks like a logarithmic curve, right?
*  It looks like, but a logarithmic curve doesn't, it's not a flat line.
*  And maybe you, I don't know if you push this any further, but you know, beyond 4,000 ideas,
*  like should we still expect to get some original ideas, albeit increasingly infrequently, or
*  do you think that you kind of hit a point where it's like, it's just not going to come up with
*  anything new anymore. And it kind of is what it is beyond a certain point. That seems important to
*  me because like we could, you know, put, we can obviously pump a lot of tokens through these
*  models. And it's like, even if it is logarithmic, you know, with a budget, you could get there.
*  But if it truly kind of flat lines and just doesn't really do anything new beyond a certain point,
*  then that's kind of a qualitatively different situation. So what do you think the reality is?
*  Yeah. So this is a tricky question because there are two factors here. One possibility is that
*  given research topic, maybe the nature of the problem space is that there are only a finite
*  number of ideas possible within that space. Especially if you give a very specific research
*  question, that's possible. Another possibility is that maybe the problem space is much bigger,
*  possibly maybe even infinite, but the model has a very low upper bound on the number of different
*  ideas can generate. Then this will be a huge issue as you pointed out, but I think this still open
*  for debate in the sense that we actually didn't push that hard on the generation part in the sense
*  that what we did to avoid repetition is very simple. It's just pending the already generated
*  ideas and asking the model to not repeat. I can imagine smarter ways of doing this. I can imagine
*  ways that you can possibly, let's say, find you the model to increase diversity. You can possibly
*  change the decoding methods in some smart way to increase diversity. If you tried all those things
*  really hard and still see upper bound, then I think it's evidence that maybe the base model
*  just has a upper bound on the idea of diversity. That would be a huge issue that I would agree with.
*  That's my take on this. There's also the question too of just how... The real eureka moment is
*  like zooming to some place in a vast search space that would have taken forever to find through
*  brute force search that actually happens to be a really good idea. That is obviously hard. Not
*  many humans can do it, and humans tend to only do it in very narrow domains where they have deep
*  expertise. This is a hard thing to do. With the AI ideas, one wonders, and I guess this is where
*  the evaluation will come in, but one wonders, let's say you turn up the temperature or apply
*  these different decoding methods or jam all the levers that you have to try to increase diversity.
*  You can presumably increase diversity, but how does that diversity relate to quality?
*  Do we have any way to determine other than the... I think your approach here of actually using humans
*  to do the evaluation is really good for creating a grounded baseline that people can hopefully have
*  some level of agreement on, but it's obviously really hard for... I would assume this is probably
*  why you haven't been able to rerun the thing with O1 yet, because you could generate a lot of ideas
*  really quickly, but now it's still going to take a lot of time and effort to do the evaluations.
*  When you do turn up the diversity, do you have an intuition or do we have any metrics for how
*  pushing these temperature and other parameters up impacts the quality of the presumably more
*  diverse ideas generated? I think one analogy here is recent works on inference scaling.
*  For example, on stuff like code generation, there are experiments showing that if you sample more
*  diverse solutions, the success rate, like the passing rate of the solutions, increases, and there's
*  a nice scaling curve there where the more you generate, the more likely that one of your
*  generations will be correct, and that your task will be essentially to find the correct ones among
*  other generations. So that's the analogy there. We didn't do the exact same thing on idea generation
*  in the sense that, like you said, unlike code generation where you can verify the
*  currentness of the solution, and that means that you can actually know the so-called success rate
*  in all your generations. In our case, the evaluation is really tricky, but still I think we can build
*  proxy rankers like we did in the paper. The ranker may be not perfect, in fact it's definitely not
*  perfect, especially in the paper, but still as long as there's some positive correlation that
*  the ranker is able to tell really bad papers from really good papers, then I think it's reasonable
*  to expect that if I scale up the direction and the number of ideas that I generate on this ranker,
*  I will possibly find better ideas, and among other top rank ideas, I might expect a quality
*  increase as I generate more ideas. Yeah, that reminds me quite a bit of some work that I've done
*  on using a number of different kinds of models to try to evaluate the aesthetic appeal of images,
*  and we found a similar thing there where the human to human consistency of judgment was fairly low,
*  the human to AI agreement was even lower, but not zero, it was better than random, and the general
*  guidelines was the general kind of takeaway of that work was like you can definitely tell the
*  difference between the best and the worst, and there's clear signal there, but especially in
*  the middle, you really can't, the fact that one was rated higher than the other is not very
*  meaningful, so you have a general direction, but at any given point in the list, it's definitely
*  up to interpretation. Although I will add one comment here that at this point, it does matter
*  that we want to have really good ranker evaluator to find the best ideas, but if we think bigger
*  and we think about the big picture of automated research, in the next stage, it's possible that
*  we might start working on automating the execution part of things, where we might build agents that
*  can automatically actually use the experiments, that means the agent will tell us our implemented
*  test on the specific data sets, and I will tell you how well it does as compared to the baseline,
*  and that means I can actually verify whether the proposed idea works or not, and that means
*  for all the general ideas, I'm willing to spend all that inference compute money, I can just
*  implement all those ideas automatically, and then I can automatically verify each idea, so in that
*  sense, it turns into a setting almost like code generation, where I can actually check the current
*  of each possible idea, as in our setting, we'll have some nice inference getting there.
*  Yeah, that's a great point, first of all, and it reminds me of the AI scientist paper where
*  they reported, I think it was like in the low tens of dollars per paper generated, and so it was like,
*  you know, okay, sure, they're not that great, but if one in a thousand is great, then it's like
*  clearly economically competitive, and prices are obviously falling quickly, so it seems like that.
*  Yeah, I remember talking to somebody once at one of the leading frontier model developer companies,
*  one of the big three, and the person said, we find over and over again that people just don't have an
*  intuition for what happens when you're willing to spend a lot on inference compute.
*  Obviously, OpenAI has kind of now productized this to a degree with the O1 family of models,
*  but even before that, just people try one, they try two, they try three, it's just not intuitive
*  to think like, what if we tried a thousand or a million, and that really can change the game,
*  so I think that is quite important. Okay, let me just reset the stage one more time,
*  because I know I keep going on all these rabbit hole regressions, so you pay grad students for
*  ideas, you give them the promise of a prize, you run a reasonably high volume of idea generation,
*  you dedupe the ideas. Is that with an embeddings approach, or what's the deduping method? That's
*  embeddings? Yeah. Okay, then there's two ways that you can rank the ideas to try to bring the best
*  AI ideas to the top. Having the AI do it directly, I believe you use Claude with
*  pairwise head-to-head kind of like tournament style for that? Yeah, the pairwise conversion thing is
*  what we found to work much better than directly asking the model to give a score, let's say on a
*  scale of one to ten. Yeah, that's a really good tip, and something I think that is a practical
*  takeaway for all sorts of AI application developers in the audience. Actually, there was a really
*  good, this is very in the weeds detail, but what I just said about tournament style is not quite
*  right actually. I had previously been thinking of doing something like this in a project, and I was
*  thinking like almost setting it up like an NCAA March Madness bracket where I would have the field
*  gradually narrowed. But of course, that has the problem of like, well, what if your best two ideas
*  meet in the first round? And so then you're like, well, maybe I'll have a double elimination
*  tournament, but then you could still have similar problems. So I think what you did was just take
*  random pairings and have each idea paired with five other ideas, and then just sort them by their
*  win-loss record, right? So five and O would be at the top, four and one would be next. Is that right?
*  So instead of random pairing, what we did is basically pair each idea with another idea with
*  the closest accumulated score so far. So the idea is I want to, let's say we want to pair the top
*  scoring idea so far with other top scoring ideas, for example. And as you're right, that is different
*  from typical tournament in the sense that we don't have elimination problems, because otherwise you
*  run your problems where two really good ideas meet in the first round and one of them got eliminated,
*  and they would only get a score of zero in the end, and that would be really bad.
*  Yeah. Okay. Cool. So that's even one level smarter than I understood. Pairing ideas with others that
*  have the same score so far to try to put the most comfortable ideas together. And yeah, you can sort
*  of, it's almost like bubble sort style, or at least that's the visual that comes to mind for me.
*  Okay. So that's cool. That works, but you did find that even better is human re-ranking. Anything we
*  should know about the human re-ranking process? It takes forever. I actually manually looked at
*  all the ideas directed, and then I didn't look at the AI ranking. I just did my own ranking of it.
*  And then I compared my own ranking with the AI ranking. And it's somewhat surprising that
*  there are a couple of ideas that I saw be clearly the top ideas that are not really captured by AI
*  as a top idea. So I think the discrepancy here is interesting. Okay. So you personally,
*  individually are the human re-ranker. Is that right? Right. Right. Yeah. Okay. Interesting.
*  So then I think the next thing is a pretty interesting detail. And I guess we should also
*  set the stage. I'll put this in the intro as well so people have this context. The field of study
*  that we are working on here is essentially prompt engineering. It is how can we get the best
*  performance from language models via different prompting techniques. So that's just background
*  baseline. All the ideas all across the board are within that domain. Now, once you have the
*  human ideas, the AI ideas ranked by the AI itself, the AI ideas ranked by you, then you put them
*  through a sort of anonymizer type of thing. You basically have the AI rewrite the idea. And if I
*  understand correctly, this was done to try to create an even playing field with respect to the
*  human judgment. I guess the worry was the human readers will likely be able to tell the difference
*  between a human written idea and an AI written idea. Even though we know that AI, large language
*  model detectors in general don't work. And if you're a teacher and you're in a classroom,
*  like you shouldn't put too much stock in them. With that disclaimer, it is reasonable to expect
*  that especially people that work in the field would have an intuition for like, yeah, this kind
*  of reading. How often is the word Delve being used, et cetera? So you put just the human ideas
*  through this rewriter or did you put the human and the AI? Everything in the AI. Okay. Yeah. So
*  tell us, give us that bit of the setup. So we pretty much specified the desired writing style
*  and format of the idea. We tried to have the writing be more academic and then we specify
*  every single component that the idea should have. And then that writing agent essentially does some
*  minor paraphrase to all the different ideas. We set very explicitly in the prompt that you can only
*  do like writing style kind of adverts, definitely not editing any of the original contents. So most
*  of the adverts are basically changing certain word choices. And I have to say, I think this is very
*  important in the sense that if you look at the original ideas submitted by humans, some of the
*  word choices can be very obvious that are just written by humans. Like some of the sentences
*  tend to, for example, some sentences are not grammatical and that pretty much just give it away.
*  And some people like to use more mobile writing styles, almost like they're talking to you,
*  more engaging writing styles. And that just feels unlikely as from AI. Those things don't really
*  affect the content that much, but we do want this to advise people that, let's say, for example,
*  some people just like humans better than maybe if they figure out that this written by humans just
*  have a more engaged writing style and then maybe they would favor those ideas. We only avoid these
*  cases. So we do the style transfer thing for every single idea, including both AI ideas and human
*  ideas. And the whole point is that we would avoid all those confunders there.
*  So I think your paper definitely did generate quite a bit of discussion online. This was
*  one of the points of criticism that I think people most focused in on when they were like
*  trying to find a reason not to believe the result. Maybe we should tell the result,
*  then we can kind of come back and dissect the criticism. The final step after doing this
*  rewriting is then to send all these ideas. And these are now like what? Like 500 words. It's
*  like a page or two pages, like a reasonably well-fledged out. A thousand words. Yeah.
*  Okay. So not an insignificant sketch of the idea. And these are then sent to human evaluators who
*  have to score them. And they are scored on four different dimensions. They are novelty, excitement,
*  feasibility, effectiveness, and I guess overall kind of just aggregates those previous four scores.
*  We will ask a separate overall score, but that's the idea.
*  Okay. Gotcha. So five different dimensions. And the humans give each paper five number scores,
*  one to 10, one to 10, the best. How original is this idea? That's novelty. How excited?
*  This excitement obviously is kind of subjective, but that's basically the like,
*  does this feel like a really good idea? Yeah. Feasibility obviously being,
*  maybe you can give a little more color on kind of the guidance that you gave for that.
*  Yeah. So for feasibility, we are really asking whether this idea can actually be executed.
*  So for example, some of the non-feasible ideas will be things like something that requires
*  tons of compute, like you want to train GPD5, that doesn't feel that feasible. Or you want extensive
*  human effort, like you want your hand level of Q training set, that won't be that feasible.
*  Or things like that. Or you want to, you know, fine tune a close model, like you want to fine
*  tune some general analysis that doesn't really have fine tune success, for example. So things like that.
*  So that's what feasibility and that's different about effectiveness in the sense that in
*  effectiveness, we're asking the question of given the proposed method, do you think the proposed
*  method will actually work better than existing base sites? So that's the difference here.
*  Gotcha. So novelty, excitement, feasibility and effectiveness.
*  Feasibility is like, don't go too crazy on the budget. I wonder what would happen if you put
*  this paper, your paper, through the evaluation process. How do you think you would score on these
*  different issues? A little bit of a beating. Yeah. You'll never get the budget for it.
*  The total budget on this is what? And how does it break down, by the way? I mean, I'd be interested
*  to know kind of total spend and also, yeah, just what percentage of that went to the humans versus
*  what percentage went to the AIs. Yeah. The payment for humans in total is about $30,000.
*  And then for AI, so generally 4,000 ideas will take a couple thousand dollars. And then we did
*  that for seven different topics. So that's some money there. And then there's also some development
*  in the early stage where we prototype a bunch of different major systems. So in total, I would say
*  maybe the money that we spend on API credits will be slightly more than what we actually pay humans
*  in that case. So that's the money break down there. Interesting. Okay. That's kind of surprising.
*  Maybe let's dig into that just a little bit more. So what is consuming the majority of the token
*  budget? Because I did a little back of the envelope math and I came out to a lower estimate of what I
*  thought you had probably spent on the APIs. Yeah. The problem with the ideation part is, first of all,
*  we have to generate all the original ideas first, and then we do the duplication. That means if
*  you want to get, let's say 200 ideas on a topic, you have to actually generate 4,000 ideas. And
*  usually we're doing this almost like screen locking where we actually over-generate more than 4,000
*  ideas. We tried to test the limit there. So we actually generated a whole bunch of like 8K or
*  even 10K ideas on each topic and did some analysis there. So that's some hyperparameter tuning there.
*  So that way we spend a bunch of tokens. And also you do realize the fact that the problem is very
*  long. So the input token is a lot and then it gets longer and longer as we prepare all the
*  previous general ideas in the process. Another thing is in the final step, we also have this
*  process of a novelty filter. This part is actually not in the main paper, it's in the appendix.
*  The novelty filter thing is similar to what people have done in the past in the sense that
*  for each generated idea, we will actually retrieve all the relative papers and then we'll compare
*  them, the general idea with each of the relative paper and ask the model whether it is too similar.
*  And that actually is pretty costly in the sense that you have to do this comparison between the
*  general idea and each of the retrieved papers. So that also costs a bunch of money. So in the end,
*  you can of course simplify the pipeline by only doing the generation part and then ignore the
*  ranking and the filtering part. That could save you some money. But I would say a lot of the money
*  is really spent on doing the over-generation part where most of our ideas are actually being
*  duplicated and are being filtered out and then a bunch of money spent on the novelty check and
*  filter. Gotcha. Okay. Interesting. But in general, I would say to get one valid non-duplicate idea,
*  you probably need to spend a couple of dollars. That's the skill of how much money you need to
*  spend. Okay. Cool. So we can finally, I think, get to the headline result, which is that when you
*  have humans evaluate the AI rewritten human ideas versus AI ideas versus human with your individual
*  re-ranking ideas, the AI ideas are scoring higher and statistically significantly so
*  for both novelty and excitement, roughly the same with feasibility. It looked like the humans are
*  a little bit higher score there, but not necessarily statistically significant.
*  Roughly the same, a little bit higher on effectiveness and higher overall and especially
*  with the human re-rank, your re-rank of the AI ideas, then you see a notable difference in the
*  overall score. But novelty and excitement definitely stand out to me as the two of the four that I'm
*  looking for most as somebody who's trying to figure out what the future of the field looks like.
*  So that is a pretty big deal. What additional color commentary would you give us on those results?
*  Honestly, I was also a bit surprised when I see AI ideas are getting higher novelty than human
*  ideas when I first saw the results. And one additional comment I want to give is that numbers
*  are just one thing. There are numerous ways that you can possibly manipulate your numbers to tell
*  the story you want. So I just want to say I personally look at every single idea being
*  generated by AI and also submitted by humans and I think I have the reasonable sense of how they
*  look like. And I think I do see how the actual ideas support the numbers that we are seeing here.
*  I think if you look at all the ideas being generated by AI, you will realize you have this
*  interesting vibe where they tend to be almost weird in the sense that they're not similar to
*  the typical ideas you will see being published these days. It's maybe less grounded in existing
*  work but more of the box in general. And I think I would categorize that as a pop novelty. So if
*  you look at all the data, I think it does make sense afterwards that AI ideas are getting better
*  and better. Okay, that's really interesting. Could you go a little deeper into just personal
*  observations? I mean, even if they're anecdotal, and by the way, speaking of anecdotal,
*  one question that I asked and was definitely interested to see the answer on was,
*  okay, maybe the average score is higher, but what does the standard deviation look like?
*  Because you could imagine a higher average but a sort of narrow band of performance. And that's
*  often, by the way, how I tend to characterize AI performance for people when I'm just trying to
*  educate people about what AI can do and what it can't do. I often, as a rough guideline, say,
*  it varies dramatically on different tasks. Obviously, you have these sort of areas where
*  AI is superhuman. It can translate from any language to any other language. That's amazing.
*  No human can do that. So in that way, it's superhuman. At the same time, they're very bad
*  at common sense spatial reasoning in general still and don't know how you should stack objects
*  on top of one another. My general guideline, though, for people is it's going to be pretty
*  consistent within a task. It might be really good at some tasks, really bad at other tasks,
*  but in general, it's going to be pretty consistent within a task. I was struck by your result that
*  the standard deviation of the scores for the AI ideas versus the human ideas was basically the same.
*  And also that, in fact, with excitement, it was a little wider. The standard division was a little
*  greater for the AI ideas. And also that the max score was higher for the AI ideas. And like I'm
*  reminded of Tyler Cowen who says, you read people for their peaks. What you contribute to the world
*  may, in some very practical sense, boil down to your very best idea. And it might just be your
*  one idea that was like the actual lifetime contribution. If you believe that and you look
*  at the max score, then you're like, huh, it's also quite striking that the max score is higher for
*  the AI ideas. If I give you one more data point there, if you think only look at the single one
*  max score is too small sample size, I actually did this calculation. So I merged all the ideas and
*  then I ranked all of them by the overall score. And then I looked at how many of the top 10 ideas
*  are from human versus AI. And I can tell you among the top 10 ideas, nine of them are actually
*  from AI and only one of them is from human. Wow. Okay. That's interesting to say the least.
*  What else? Keep going. I mean, I could happily listen to any and all other observations that
*  you have as somebody who just obviously spent a lot of time looking at the data. This is a good
*  reminder too of our mantra for all this kind of work. Look at your data. So you clearly did that.
*  What else comes to mind that we should be thinking about? Yeah. I think one thing that maybe people
*  didn't notice that much is I was closely monitoring the whole review process as people
*  submit their reviews. And I think it's very interesting to see that first of all, there's
*  big review disagreement as we noted in the paper. Second of all, I think sometimes there is some
*  randomness in like which ideas, like some reviewers have certain preferences and you know, let's say
*  they tend to favor certain types of ideas. So there's this factor in there where certain reviewers,
*  let's say they will just systematically give higher scores to the ideas that are given to them because
*  they like the topic, for example. And there are certain cases where certain reviewers just give
*  low scores overall. That's one thing I was observing in the process. And I was like, you know, that's
*  really going to impact the way we make conclusions because we want the conclusion to be based on the
*  actual quality of the idea rather than, you know, maybe reviewers have biases and then different
*  reviewers just have different calibration in general. So that's why we come to a lot of different
*  tasks in the paper. Like the first table that you see is really just treating each review as an
*  independent data point. But then I realized there could be all this review of biasing, there could
*  be all sorts of different confunders. That's why we did two additional tests to try to account for
*  all those possible biases. And in the end, I think we realized the difference between AI and
*  human ideas is big enough such that you get significant difference no matter what kind of
*  tasks you run. And that's why we are making that conclusion there. So back then, I think what we
*  agreed with my advisors is that we're going to run all the possible statistical tests we can sync
*  up to account for all the potential confunders there. And even one of the tests that this
*  conclusion doesn't hold, then we won't be making that conclusion. So that's the bottom line there.
*  And then the novelty aspect is just different enough such that it's whole robustly across all
*  the different tasks. So that's one thing from the results section. So each idea gets three
*  human evaluations. Is that right? Average is on three, but at least two are multiple.
*  Gotcha. Okay. So two to four with average being three. And then when you talk about doing
*  multiple different statistical analyses, the main two that I saw were one is treating each
*  score as its own data point and measuring that way. And then the other was taking the average
*  score at the ideal level and then treating that as a single data point.
*  And this another thing where we actually analyze based on each individual year, because like I said,
*  I observed the same during the review process where some reviewers, let's say they just really
*  hate prompting and they might give two or three to all ideas to review. Some people, they might
*  really like prompting and they might give like seven or eight to all ideas they reviewed. And then
*  it becomes some problem of whether you happen to have assigned more ideas to those people or not.
*  That's really not what we want to capture. So what we did is for each individual reviewer,
*  we look at all the ideas they reviewed and then we get the average score for the AI
*  completion and the human completion and we compare the difference between them.
*  So for each individual reviewer, they should have consistent standard while they're reviewing
*  different ideas. So if every single reviewer is giving ideas, better scores than human ideas,
*  then that says that, okay, this thing holds robustly despite all the difference between
*  different reviewers. And that's the third test we're doing there.
*  Kyle Sivers Yeah, gotcha. So just to restate it one more time, you've got three ways of
*  analyzing the data. One is every single score from a single reviewer for a single idea is a data point,
*  analyze it that way. Version two is take the average by grouped by idea and then analyze them
*  that way. And then the third is aggregate at the level of the reviewer where you basically say,
*  okay, this reviewer A had this average score for AI ideas, this average score for human generated
*  ideas. And now we'll use those as the data points to then do analysis on. And the bottom line is
*  across any of these different lenses that you want to put on data, you still see a statistically
*  significant edge for the AI ideas, particularly in novelty and excitement.
*  Kyle Sivers Yeah, that's the quantitative results we have. I think one additional comment I can add
*  there is that I'm pretty strongly that I support the conclusion on the novelty part. But some people
*  could argue maybe being novel isn't the only important factor there for producing good research
*  like I said, some AI ideas, they do tend to look more different than what we typically get when
*  reading all those papers. But the question is whether that's a good thing. Well, you can argue
*  AI ideas could look very different, could be very novel, but then they turn out to be just weird
*  ideas that just don't work at all. That's totally possible. And the current evolution paradigm has
*  just evolved where we are asking the question of do you think this idea is going to work?
*  Do you think this idea is feasible? And based on the current evolution, AI ideas are slightly worse
*  on feasibility, but somewhat similar on effectiveness. So that's not too bad. But you
*  could of course argue that this evolution is bad, because you are essentially asking people to predict
*  whether this idea is going to work, which is an incredibly difficult task, even for expert researchers.
*  And it's highly subjective. But this is something that we could possibly actually measure objectively,
*  where the way is you actually implement the idea, and then you can see whether the idea actually
*  works or not. So that's the current project we're working on this quarter right now.
*  We are actually recruiting a bunch of people to ask you all the human AI ideas into food products,
*  and that we can verify whether those ideas actually work or not. So that is trying to
*  address this concern that do those weird looking AI ideas actually work in practice? So I don't know
*  the results yet. I think either way, it's going to be fine. I think if we get the conclusion that
*  those AI ideas did not just look normal, they actually also work in practice,
*  then I think that would tell a pretty strong story.
*  Mad Fientist Yeah. And if it's the reverse, there's still something very interesting going on
*  where, especially because we've covered all the statistics, but again, you also said
*  nine of the 10 highest rated ideas were AI ideas. It would seem strange if like,
*  I mean, that would certainly suggest that like the humans, I guess it would kind of call into
*  question like a lot of the human evaluation, right? If all of a sudden, like despite this sort of
*  pretty clear signal that the humans expect better from the AI ideas, if that were to actually be
*  reversed, it would be like, yikes. Yeah. Yeah. I think that would tell us not only about the
*  characteristics of AI general ideas, it also tells a lot about the evolutionary protocol that
*  we should actually do. I think if the reverse is happening when we finish the execution part,
*  I think that's an interesting challenge to whether even human evaluation is reliable
*  at the idea stage or not. Mad Fientist Yeah. That does remind me of one comment I saw online
*  that I did think was potentially perceptive or sort of something that would warrant some digging,
*  and maybe you did this digging, but the idea was when a language model is prompted to
*  generate a novel idea, there are different ways that it can sort of satisfy the user with that
*  request. And this ties into like a common theme of this show over time, which is that RLHF is like,
*  obviously very powerful, has worked really well, but has some pretty fundamental problems. One of
*  which is that the language models seem to be starting to understand that pleasing us is a bit
*  different than actually doing something in reality. And this is why we see sycophantic behavior out of
*  Claude and others, and this is one of the reasons people worry about deception from language models
*  long-term. But in the specific context here, you might worry that, and presumably the rewriting
*  would try to help fix this, but maybe not entirely, but you would worry that the AI might be really
*  good at using sort of novelty indicators, kind of words and phrases that sort of suggest novelty,
*  even if the underlying idea maybe isn't actually so novel or even coherent necessarily, but just
*  ways of presenting that the models have learned will score well with humans. How do you assess
*  that possibility? Again, it wouldn't call into... I mean, to the degree that that is true,
*  it would be operating by means of tricking the humans, but I don't think we can entirely rule
*  that out without at least some digging into the question. So how much digging into that
*  possibility did you do, and what's your kind of current state of understanding of that question?
*  So my intuition back then was that we're using the exact same
*  you know, paraphrasing from to the standardized style of every single idea, including AI ideas
*  and human ideas. So the hope is that the kind of writing style or word charts will be similar
*  across conditions, but it's true that some AI ideas, they might have more novel-something words
*  in the beginning, and then they didn't really get filtered out by the paraphrasing. So I think we
*  didn't really 100% rule out this possibility that maybe the AI ideas would contain some more
*  novel-something words there. I think we have some plans to do some follow-up analysis on the
*  word choice and stylistic analysis thing. I think that will tell us something interesting,
*  but still I think the only possible way to totally address that thing is by actually
*  finishing the execution study thing and tell us whether AI general ideas tend to work or not.
*  Like that's the most objective thing that will possibly address any concerns about the subjectivity
*  in the evaluation, because in the end, I have to agree that there is a strong level of subjectivity
*  in the current way that the ideas are being evaluated. So that's my current status.
*  Were there any ideas generated by the AI that you felt were like just amazing? I mean, some of these
*  ideas that got scored like a 10 on, let me just go back to the table. So individual scores,
*  the highest novelty score for a human idea was an 8. The highest score for AI idea was 10.
*  For excitement, the highest score for a human idea was 8 and the highest for an AI idea was 9.
*  So were there, I'm sure you looked into the ideas scored 10 in novelty and 9 in excitement.
*  What did you see? Were those ideas that you were like tempted to go run with yourself? Or I mean,
*  just how good were those top rated ideas? There are a couple of ones that I personally really like.
*  Again, this whole thing is subjective. The ideas that I like the best may not be the ideas that
*  other people like the best. But I personally really like the ideas under the authoritative
*  topic. We have seven topics and one of the topics is on quantity methods that can help us calibrate
*  uncertainty and measure confidence. And then we have a bunch of AI general ideas on that. I think
*  multiple ideas under that category look pretty interesting. It's this one example that we
*  had in the paper. For example, it's sort of a much more fancy version of this self-consistency idea
*  where you generate many different diverse solutions given the query. And then what you do is not
*  really simple majority voting, but rather you measure how each solution supports or refutes
*  each other. And you kind of construct this graph thing and then you can measure central algebra,
*  other graph metrics, and as a better way to measure the uncertainty of the solution for that
*  query instead of just taking simple majority voting. So that's something neat. And there's
*  a couple other ideas that we did in the paper that I saw was pretty interesting. If it works,
*  then it would be awesome. So one example is, again, on measurement uncertainty. So the idea is,
*  what if we prompt the model to first generate so-called uncertainty examples? Given this question,
*  if I tell this answer, it has an uncertainty of 10. If I tell a different answer, it has an
*  uncertainty of 9, and so on and so forth. So we kind of have this mapping of what would be an
*  answer with uncertainty 1 look like, what would be an answer with uncertainty 2 look like, and
*  extra extra. And then when given a new query, I generate a response and then I basically compare
*  the response with the mapping thing and say, you know, this is closest to an uncertainty 5 answer.
*  So uncertainty will be 5, something like that. So really weird in the sense that it's quite different
*  from any of the other uncertainty estimation methods that I'm seeing. But, you know,
*  sounds interesting. We didn't really test whether that will work. That will be for the next stage
*  of study. But if this very weird looking idea actually works, and then I think that will be
*  pretty awesome. Yeah, it's interesting. How did you think about in terms of what to do next,
*  going down the path of actually executing ideas versus other dimensions of generalizing this idea?
*  An obvious one would be to rerun a similar experiment in another different domain.
*  Yeah, another domain is also possible to relax the constraint on prompting. That's a lot of people
*  are really criticizing that. We could totally do something where I self just prompting ideas,
*  we allow any sorts of ideas. I can imagine you can adapt the same idea generation system to
*  the general ideas on a better way to construct synthetic training data, for example,
*  better decoding methods, better training objectives for alignment, etc. So you can totally do that.
*  I think it's a matter of which direction you want to head. I see a couple of things that's on top of
*  my head right now. So one thing is a lot of people are saying the human ideas we collected in this
*  study are not really representing the best human ideas, which is totally true. We actually asked
*  the exact same question. The idea writers are saying these ideas represent around the average
*  of the ideas. So this is really average PhD level rather than top PhD level. So if you want a
*  stronger human baseline there, one thing that we are thinking about doing is there will be another
*  upcoming LP conference called MLP. And we can compare all our general ideas with papers actually
*  accepted at this top tier conference. And then we would have a stronger baseline there where we
*  could assume those accepted papers will represent some higher quality work as compared to asking
*  some random general ideas on the spot. So that's one thing. Another thing is the execution thing
*  that I was talking about. We want to address all the subjectivity concerns in the current evaluation
*  by testing whether AI general ideas actually work in practice. And I think that will give a much
*  more objective evaluation in the quality of AI ideas. So that's one thing. And both of those are
*  still on evaluating the research ideas. So a bigger step forward would be to complete the other
*  part of the entire pipeline. And that is we have generated all those ideas. Once you find a way
*  whether we can automatically execute each idea so that we can actually verify the effectiveness
*  of each idea. And we did some preliminary attempt on building such an execution agent. I think there's
*  some crucial limitation in the evaluation of these agents in the sense that you can have some tricks
*  to have the agent generate all the code and the code could run successfully. And that it can actually
*  give you some numbers. We built an agent that can implement the idea and tell you the baseline number
*  and the new proposed methods performance. But then the problem is if you look at the actual code
*  implementation, sometimes the model is not implementing the right baseline. For example,
*  for a test classification problem, the agent was actually implementing a keyword-based
*  method as a baseline, which is totally unreasonable in this era. So that's one thing. And sometimes
*  the agent might skip some steps when implementing the proposed method. And those things are really
*  tricky because it requires evaluation on the intermediate steps of the implementation rather
*  than just a final outcome. So I think we need to do some more work there to figure out what's the
*  best way to do this intermediate evaluation on the correctness of the implementation. And also just
*  to improve the agent in general. So that's something that we are thinking about. The whole
*  reason we can set up this evaluation of the execution agents so that we can post it as a
*  challenge for the entire community and people can all work on this problem of creating execution
*  agents that can automatically implement research ideas and verify things. If that works out in the
*  end, then we can think of a very exciting combination of idea generation and automatic
*  execution. And then we can scale this up and maybe we can possibly find some best-weaper-level
*  ideas that actually works in practice. And that would approach what I call the Eureka moment for
*  automating research in the beginning. Yeah. How much of a difference do you think O1 is going to
*  make here? It strikes me that in terms of accelerating your process, if O1 could get to
*  human-level evaluation and you could demonstrate that, then you would dramatically reduce your
*  cycle time for one thing. So I wonder how close you think that is to happening. And then just curious
*  for your intuition in general for where you think this next generation of model will make the most
*  impact. And if you have any ideas around where you think it won't make an impact, that would be
*  definitely really interesting too. Yeah, I agree with you. I think I really need to try this O1.
*  I think if O1 is able to get better at the automatic evaluation thing, it can be a great
*  rerun-curse thing that will help us with the inference scaling stuff. I think that's interesting.
*  It's also interesting to test whether it has better diversity in the idea generation as well.
*  I don't have any empirical evidence right now to say whether O1 will actually work better.
*  So that's an open question that we want to try for sure. I think another interesting thing is also
*  we're doing the prompting in the entire data generation pipeline and it seems that it's possible
*  to also try some fine tuning in the sense that we actually have a lot of data, you know,
*  all the academic papers on those conferences. It feels like we can gather some meaningful data set
*  and it's interesting to see whether smaller language models like Lama after proper fine tuning
*  would give some reasonable results in this pipeline as well.
*  Okay, cool. I think we've covered it. Is there anything else that I haven't got to that you
*  think folks should be aware of with respect to this work? No, this also sounds good to me.
*  One last advertisement thing, we're doing this execution study right now. If the audience is
*  interested in participating by actually implementing one of the ideas, we pay a lot of money. We'll pay
*  a couple of thousand dollars for implementing an idea and that would be a great contribution
*  to our study. Cool. Interesting. I like it. What's your expectation for the future? I mean,
*  obviously we're getting into speculative territory here. How do you think about kind of key thresholds
*  to be hit and how soon do you think they're likely to be hit? So I think a concrete threshold is what
*  I said in the beginning. If you can have an end-to-end system that can automatically
*  think of an idea, execute the idea as the whole project and that project can actually
*  not just get into a top conference but actually get a paper award at a conference. That would be,
*  I think, the major milestone we want to hit. I think the easier milestone is to just have the
*  automated paper to get into one of the top conferences. I have some heartaches on this.
*  It's actually not that far away for that simple milestone to be achieved. Just getting into a
*  top conference, I feel like even some ideas we have right now, I feel like the best ones,
*  I could see them getting accepted at a conference like ACL. I'm seeing similar
*  shape of research being published there. I feel like we're probably getting there every now
*  down the execution path. But of course, that will take some time for sure. But the really
*  difficult question is the whole agenda, the ultimate vision is not to just mass produce
*  average piece of research. I think the ultimate hope there is really we are able to have this
*  automated system that can generate research beyond the average PhD level. So I really think
*  if we are able to at least demonstrate one case study where an automated idea gets implemented
*  into something that can win a best paper award at a top conference, I think that's a strong sign.
*  I feel like that's going to take us a couple of years. My hope is that by the time I graduate,
*  I mean, three or four years, if by that time we are able to achieve this goal, I think that'll be
*  pretty exciting. I think that's an aggressive estimate, but that's a goal. Let's see if we can
*  hit that. That's right in line with Leopold's situational awareness timelines. Cool. Well,
*  I really appreciate all your time and going into the many, many details and weeds of the
*  implementation with me. Any closing thoughts before we break? Sounds good to me. Alrighty.
*  Cool. Well, the paper is once again, can LLMs generate novel research ideas? It's one of the
*  most important questions in the world today. Chung-Le Si, PhD student at Stanford, researching
*  the automation of research. Thank you for being part of the cognitive revolution. Thank you.
*  It is both energizing and enlightening to hear why people listen and learn what they value about
*  the show. So please don't hesitate to reach out via email at tcr at turpentine.co,
*  or you can DM me on the social media platform of your choice.

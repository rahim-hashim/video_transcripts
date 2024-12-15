---
Date Generated: December 03, 2024
Transcription Model: whisper medium 20231117
Length: 6581s
Video Keywords: []
Video Views: 3315
Video Rating: None
Video Description: In this episode of The Cognitive Revolution, we dive deep into frontier post-training techniques for large language models with Nathan Lambert from the Allen Institute for AI. Nathan discusses the groundbreaking Tulu 3 release, which matches Meta's post-training performance using the LlAMA base model. We explore supervised fine-tuning, preference-based reinforcement learning, and the innovative reinforcement learning from verifiable reward technique. Nathan provides unprecedented insights into the practical aspects of model development, compute requirements, and data generation strategies. This technically rich conversation illuminates previously opaque aspects of LLM development, achieved by a small team of 10-15 people. Join us for one of our most detailed and valuable discussions on state-of-the-art AI model development.

Check out Nathan's Lambert newsletter:
https://www.natolambert.com
https://www.interconnects.ai

Be notified early when Turpentine's drops new publication: https://www.turpentine.co/exclusiveaccess

SPONSORS:
Notion: Notion offers powerful workflow and automation templates, perfect for streamlining processes and laying the groundwork for AI-driven automation. With Notion AI, you can search across thousands of documents from various platforms, generating highly relevant analysis and content tailored just for you - try it for free at https://notion.com/cognitiverevolution

Shopify: Shopify is the world's leading e-commerce platform, offering a market-leading checkout system and exclusive AI apps like Quikly. Nobody does selling better than Shopify. Get a $1 per month trial at https://shopify.com/cognitive

Oracle Cloud Infrastructure (OCI): Oracle's next-generation cloud platform delivers blazing-fast AI and ML performance with 50% less for compute and 80% less for outbound networking compared to other cloud providers13. OCI powers industry leaders with secure infrastructure and application development capabilities. New U.S. customers can get their cloud bill cut in half by switching to OCI before December 31, 2024 at https://oracle.com/cognitive

80,000 Hours: 80,000 Hours offers free one-on-one career advising for Cognitive Revolution listeners aiming to tackle global challenges, especially in AI. They connect high-potential individuals with experts, opportunities, and personalized career plans to maximize positive impact. Apply for a free call at https://80000hours.org/cognitiverevolution to accelerate your career and contribute to solving pressing AI-related issues.

RECOMMENDED PODCAST:
Unpack Pricing - Dive into the dark arts of SaaS pricing with Metronome CEO Scott Woody and tech leaders. Learn how strategic pricing drives explosive revenue growth in today's biggest companies like Snowflake, Cockroach Labs, Dropbox and more.
Apple: https://podcasts.apple.com/us/podcast/id1765716600
Spotify: https://open.spotify.com/show/38DK3W1Fq1xxQalhDSueFg

CHAPTERS:
(00:00:00) Teaser
(00:00:59) Sponsors: Incogni
(00:02:20) About the Episode
(00:05:56) Introducing AI2
(00:09:56) Tulu: Deep Dive (Part 1)
(00:17:43) Sponsors: Notion | Shopify
(00:20:38) Open vs. Closed Recipes
(00:29:48) Compute & Value (Part 1)
(00:34:22) Sponsors: Oracle Cloud Infrastructure (OCI) | 80,000 Hours
(00:37:02) Compute & Value (Part 2)
(00:42:41) Model Weight Evolution
(00:53:16) DPO vs. PPO
(01:06:36) Project Trajectory
(01:20:39) Synthetic Data & LLM Judge
(01:27:39) Verifiable RL
(01:38:17) Advice for Practitioners
(01:44:01) Open Source vs. Closed
(01:49:18) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Everything You Wanted to Know About LLM Post-Training, with Nathan Lambert of Allen Institute for AI
**Cognitive Revolution:** [November 21, 2024](https://www.youtube.com/watch?v=LVXtFnEbNU0)
*  It's probably not worth the effort to spend all your time on preference tuning
*  when you can just be making better data and better pipelines, which is what 2.3 is about.
*  Inspired by the transition we're seeing with the Llama report, with Trapbot Arena,
*  it's like turned into a hockey stick again where we have this incremental scores and the OpenAI
*  and Google are like skyrocketing their scores. And the philosophy is like, how do we try to
*  understand what the open groups should be doing and where there are hills to climb when you're
*  increasing the complexity substantially in post training? If you can have humans and LLMs do
*  preference data, which do you send to humans versus LLMs? And that I think solves a lot of the
*  problems, which is like, there are definitely things that we want humans giving the answer on,
*  but there are a lot of mechanical tasks that we can outsource LLMs. There's a lot more post
*  training that is not really touched. And I think that the opportunity is high because the big thing
*  is how do you develop character? Character is something that you don't have evaluation for in
*  your models. And our models, if you compare them to Claude, will not have as consistent of a character.
*  Regardless of how you felt about the outcome of the election, I think we were all united in
*  looking forward to an end to the constant fundraising emails and text messages. Unfortunately for me,
*  they haven't stopped even now more than a week after the election. And that's to say nothing of
*  the normal commercial spam coming at me from all directions at all times. It turns out that most
*  of this noise is caused by data brokers. These companies aren't just collecting your contact
*  details. They're gathering everything from your social security number and financial records to
*  your online shopping habits. And they're now working with insurance companies, which could
*  potentially impact your rates. That's why I'm excited to now be using Incogni. Incogni contacts
*  five types of data brokers, marketing, recruiting, financial information, risk mitigation, and people
*  search sites and demands that they remove your information. Then they continue monitoring on your
*  behalf to prevent data recollection. Take your personal data back with Incogni or protect up to
*  four family members with their family and friends plan. They offer a 30 day money back guarantee if
*  you're not satisfied. So take your personal data back with Incogni. Use code revolution at the link
*  below and get 60% off an annual plan. That's incogni.com slash revolution.
*  Hello and welcome back to the cognitive revolution. Today my guest is Nathan Lambert,
*  author of the popular interconnects newsletter and machine learning researcher at the Allen Institute
*  for AI, which today is releasing Tulu three, one of the most comprehensive open source efforts
*  to diffuse the understanding and practice of frontier post-training techniques for large
*  language models that we have seen to date. By systematically working to match Meta's post-training
*  performance using the same llama base model and sharing all of their findings and data publicly,
*  Nathan and the team at the Allen Institute have illuminated what has historically been one of the
*  most opaque aspects of large language model development. And this conversation represents
*  one of the most detailed discussions of this topic that you can find anywhere online today.
*  We cover the full spectrum of post-training techniques, including supervised fine tuning,
*  multiple flavors of preference-based reinforcement learning, and a new technique called reinforcement
*  learning from verifiable reward, which rewards the model for accurately answering questions with
*  objectively correct ground truth answers. At each step, we dig into the practical details that make
*  these techniques work, the associated compute requirements, data generation strategies, and the
*  value derived from each, as well as the experimental designs that are used to measure performance
*  while exploring the vast space of possible training recipes. We even explore some fascinating
*  emergent behaviors that echo the frontier reasoning capabilities that we've recently seen from OpenAI's
*  O1. Nathan's frank discussion of both the technical and organizational challenges of this work,
*  including in a few moments where he acknowledges aspects that are not yet well understood,
*  provides a super useful window into what it takes to develop state-of-the-art models.
*  And the fact that they ultimately succeeded in matching LAMA performance with a team of just
*  10 to 15 people makes their approach one to study closely. Now, how long this level of open
*  development can continue into future generations of models remains, in my mind, an open question.
*  Even with billionaire estate backing, human-generated preference data and annotations
*  are cost prohibitive for the Allen Institute, and the synthetic data generation techniques
*  used in this project may or may not be available going forward if frontier developers follow
*  OpenAI's lead and choose not to release their O1-style reasoning traces. That said, Nathan
*  expects that the community will ultimately figure something out, and just before publishing, we've
*  seen Chinese AGI company DeepSeq announce a new O1-style model called DeepThink, which does seem
*  to show its work and is reportedly going to be open-sourced in the near future. A development
*  that could shift the question from whether or not such open reinforcement learning projects
*  can continue to whether or not they should. And which should definitely cause anyone who thinks
*  that Western companies can maintain a comfortable lead over Chinese companies from here all the way
*  to AGI to stop and rethink their assumptions. In any case, this episode is one of the highest
*  leveraged pieces of content we've produced on this show to date. It's full of concrete,
*  practical insights that were previously scattered throughout the literature or simply hidden behind
*  closed doors. And I am really grateful to Nathan for such an open and technically detailed conversation.
*  If you're finding value in the show, we appreciate it when listeners take a moment to share it online,
*  post a review on Apple Podcasts or Spotify, or just leave us a comment on YouTube. And your
*  feedback is always welcome via our website, cognitiverevolution.ai, or by DMing me on your
*  favorite social network. With that, I hope you enjoy this super deep dive into the frontiers
*  of large language model post-training with Nathan Lambert of the Allen Institute for AI.
*  Nathan Lambert from the Allen Institute, creator of TULU. Welcome to the Cognitive Revolution.
*  Yeah, thanks for having me. The Nathan Squared pod has happened.
*  I can't believe it's taken this long, but I'm excited that the day is finally here.
*  So a lot of ground to cover. I'm just going to fire questions at you rapid fire and let's
*  see how far we can get. For starters, tell us about the Allen Institute. You guys have put out a lot
*  of stuff. I would love to just get a little context on kind of the philosophy behind it, the funding,
*  the GPU. Are you GPU rich or GPU poor? And how are you looking to put a dent in the universe?
*  Yeah, so Allen Institute, I'm new blood here. I joined it just over a year ago. The Institute
*  is actually 10 years old. It was founded, it's funded by Paul Allen, which is not surprising
*  for people in the tech scene and knowing the Allen Institute in Seattle, given the name.
*  And the original CEO, Oren, I don't know how to pronounce his last name, also was a professor
*  at U-Dub, a lot of U-Dub ties, I think was buds with Paul Allen. And this kind of grew out of that
*  to just kind of do AI research for the common good, make things very open, very hybrid academic
*  industry. That is kind of the story of the first decade, roughly, it's not quite the first 10 years.
*  And now there's like Oren left, the process of leaving started a few years ago, and there's new
*  CEO Ali Barhadi. Also professor at U-Dub was at Apple before. Most prominent work from his group,
*  I think, is the YOLO line of work and computer vision. And it's kind of bringing in new blood to
*  make this transition to build open language models. I think with a lot of institutions realize that
*  in order to be credible in AI, you need to have some amount of cred in the language modeling space.
*  And right now for AI research, it is to be like, look, we can do this too. And it is
*  a narrowing of scope to try to release great models and build models. I think
*  OLMO is the start of this, which was a very long story in 2023 that I was not part of most of. I
*  joined late in the year and launched in early 2024. And then 2024 has been the year of doubling down
*  on this and scaling up projects that you can do when you have more people. I think we'll talk about
*  the post-training side of things and there's plenty on pre-training and stuff in the VALS as
*  well. But it's really like what the academic projects in open source AI look like when you
*  can bring more people in. And I think throughout the year, a lot of our projects have been getting
*  bigger. And we've seen like MOLMO, the vision model, which is primarily on the vision team,
*  but gets involved with the language pre-training team and other things. It's like these projects
*  getting bigger and trying to increase the scope of research while doing as much as we can in the
*  open. So no constraints on what we can say. At the end of the day, nonprofits are about telling a
*  good story and stories are what can actually change how policy happens and how people view
*  the world. So at the end of the day, that one institute needs to build good models so we can
*  communicate why open source has benefits. And it's like a kind of reductionist and it's a
*  little cynical to view nonprofits as storytelling orgs. But when your money mostly comes from a tech
*  billionaire's estate, like you got to stay some of it as it is. But the momentum is good. So it's
*  fun to be in the space and see things continuing for the time being. I think stories are honestly
*  a super important part of life in general and the AI moment in particular. It feels to me like
*  we are summoning this crazy new alien intelligence and really lack in most corners a positive vision
*  for what we want to do with it, what impact we want it to have on life. And there's a lot of
*  very general talk about, you know, won't it be great when we have everything we want? And it's
*  like, yeah, can we put a little more detail on that? So I do appreciate the importance of
*  storytelling in this space. You mentioned pre-training and post-training. The project
*  that you've just put out today as we record this a few days in advance, but we'll try to publish
*  it right around the time of recording, is called Tulu. It is really a deep dive into post-training
*  techniques and give us a little bit of context for kind of why this project, what the goals of it
*  are. And then I really just want to go deep on the actual methodology, what you've learned and
*  try to develop my own intuitions for the state of the art in post-training. Yeah. So I think this
*  story fits well with what you're talking about with AI2. So AI2's kind of open post-training
*  recipes have been under this Tulu brand for over a year, almost a year and a half. I think Tulu 1
*  was back when Open Assistant was new, was like, what can we do by mixing all these popular data
*  sets that people are putting out in 2023? All these data sets and small models, like how do
*  you systematically mix instruction data sets to combine them with open resources? And Tulu 2 was
*  around when DPO was very popular and that was when we showed that you can scale DPO to 70 billion
*  parameters and continue getting the benefits from preference fine tuning and open recipes.
*  Then we went away and did Tulu 2.5, which was kind of like trying to answer the PPO versus DPO
*  question, which the TLDR was, if you tune your parameters right, PPO is probably better a bit,
*  but it's probably not worth the effort to spend all your time on preference tuning
*  when you can just be making better data and better pipelines, which is what Tulu 3 is about, which
*  is kind of inspired by the transition we're seeing with the Llama report with Chatbot Arena. It's
*  turned into a hockey stick again where we have this incremental scores and the Open AI and Google
*  are skyrocketing their scores again. Nematron paper, Apple had a paper, which these post-training
*  recipes are just much more complicated than big SFT step, do DPO on some chat data and be done.
*  The philosophy is kind of like, we know these labs are doing it, how do we try to understand what the
*  open groups should be doing and where there are hills to climb when you're increasing the complexity
*  substantially in post-training? Llama 3 has hundreds of people on it and a large amount on
*  post-training. We have 10 to 20 on ours and it's like, what could academics actually do to do
*  modern post-training and curate new data, use new algorithms, sequence things together, but kind of
*  move beyond this paradigm of just increasing Alpaca about or vibe scores and try to get really
*  specific on improving math, improving IFVal. Code is something we did a bit, but it wasn't the biggest
*  focus. I think our vals for code were mostly saturated pretty early on, but kind of shifting
*  this post-training into a much bigger domain of academic progress and kind of honestly, there's
*  been a slow and how often people are releasing models and data sets and kind of like reboot that.
*  The DPO era was a very fun one for seeing open post-training models. It was bonkers. Every week
*  there was a new DPO model that was state of the art on something, but that was last December,
*  last January and it feels much slower now. It's much more big players dominating the AI narrative
*  and it's trying to reset that. Yeah, so one of the things that I noticed in the materials that you
*  shared is that the goal of the project was to beat Llama 3.1 and you're starting, if I understand
*  correctly, with a couple different base models, but one of the base models is Llama 3 base,
*  basically, right? So you're essentially saying, okay, if we take the same pre-trained version
*  that you folks at Metta started with, can we match you or exceed you, hopefully, with
*  out of post-training to post-training, apples to apples basis? They obviously put out a big
*  report and shared a lot about what they did, but I believe they don't share much or any of the
*  post-training data. Give us a little bit more. What do they share and not share?
*  I would say they share an outline of their method. They don't have a lot of,
*  I might have hyperparameters, but not really clear without noting their code base and things
*  like this. So they share a high level outline of like, here is our approach and here are the
*  types of things that we do, but not the specific things that we do and definitely not the data.
*  So the biggest differentiator for our post-training is that we release the data. I think we
*  built like three to six new datasets just for this project and we're using those with the
*  combination of already existing datasets and we'll resolve them at once. But really what you're
*  saying is right, is like the development model here was we had a set of evaluations we cared about
*  that we tried to cover things like factuality, knowledge, math, code, instruction following,
*  safety. And the goal, the primary development target was Lama 3 AP where we effectively trained
*  about a thousand AP models to try to get these scores to be higher at AP and then validate them
*  at 70B. And we're also adding like Omo models, which is our like big census is our main thing,
*  which is like trying to like make sure the recipe translates. So for that reason, it's like kind of
*  a basic goal is like, okay, we like in order to know you're in the right ballpark, you need to
*  beat these people that are known to be pretty good. I think I've talked to like I've taught the fun
*  thing about Lama based models and an instruct is that the closed labs can also validate their
*  pipelines on it. So like the closed labs can take the Lama 3 base and then use their post-training
*  and compare to the instruct model that Lama also released. So hearing from some people in industry,
*  they're also like, yeah, Lama 3 instruct is like 3.1 instruct. The latest stuff was like pretty
*  cracked. It was a pretty good post-training. I think obviously like open AIs infrastructure
*  isn't going to work as well in Lama based models, but the 3.1 models particularly actually were very
*  good. I think it's clear that there were some ways that they were rushed or trying to focus
*  on systems rather than novelty. It was mostly SFT and it was DPO for the Lama 3.1 instruct. And
*  I know they are expanding into more things now and we're kind of by being smaller and moving fast.
*  I think we're actually going to do some, we're doing some things that I bet will look pretty
*  similar in the Lama 4 instruct or like a Lama 3.5 instruct type thing. But that's kind of like the
*  theme is we want to beat their numbers. We're doing similar things. We have the advantage of
*  being smaller. We can be a little bit more clever maybe, but that was the development target. And
*  it really is like, I can look at the days. I don't have the dates in mind. It was like,
*  if we started this project four months ago, it's like, oh, a few months in, we passed Lama 3
*  instruct. And then like a month and a half later, we passed Lama 3.1 instruct to 8B. And then like a
*  couple of weeks later, it's 70B. And it's like just metronomic. And it's like, every time it's like,
*  oh, wow, this is like actually happening. So it's fun. It's fun to see. And we're very excited to
*  see what people build on it. And I don't know, like we might have a discussion later on, which
*  is like fine tuning from base versus fine tuning from instruct, which is another kind of, there's
*  another fork. And I think fine tuning from base is very academic and very important to post
*  training to understand how to do this from base models. And fine tuning from instruct is a very
*  important area, especially for new companies and domain specific things. Because if Lama is going
*  to put out a very strong instruct model, you don't have to do the whole 2LU3 suite to make it good
*  at your specific domain. And it's like, we're doing part of this, but eventually there's going
*  to need to be research there, I think, on the day of recording Nexus Flow, which is a startup that
*  came from, like some of the people are from Berkeley Nest, the group that released the
*  Starling models. They released another fine tune on instruct and we saw a Nemotron fine tune on
*  Lama instruct to go very viral recently. So there is some messaging that like, we're not doing this
*  fine tune on instruct, but it is another area. I just think in terms of like fundamental long-term
*  ecosystem building, the from base is still the thing that needs the most transparency.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  As a Cognitive Revolution listener, you're obviously interested in cutting edge AI technology.
*  And with that in mind, I'm proud to say that this episode is brought to you in part by Notion.
*  Notion has been a clear leader in high value applications of generative AI since the wave
*  began. Earlier this year, we had Notion AI engineer Linus Lee on the podcast. The quality of his
*  insights showcase the caliber of talent that Notion employs. And that inside look at how Notion
*  builds with AI is still extremely valuable. Given my personal focus on AI automation recently,
*  I specifically wanted to highlight Notion's library of workflow and automation templates.
*  If you're looking to streamline your processes and lay the foundation for future AI driven
*  automation, these templates are an excellent starting point. And even if you're not ready
*  for full automation, you'll benefit immediately from Notion AI, Notion's latest all in one AI
*  implementation that searches through thousands of documents, regardless of whether they live
*  in Notion or on some other platform like Slack or Google Docs to deeply understand the context
*  of your work and generate highly relevant analysis and content just for you. Notion is used by more
*  than half of Fortune 500 companies, helping teams reduce emails, meetings and time spent searching
*  for information. Want to try it? Head to Notion.com slash Cognitive Revolution. You can start for free
*  and using our link supports the show. So join me in giving Notion AI a shot today at Notion.com
*  slash Cognitive Revolution. The Cognitive Revolution is brought to you by Shopify.
*  I've known Shopify as the world's leading e-commerce platform for years, but it was only
*  recently when I started a project with my friends at Quickly that I realized just how dominant
*  Shopify really is. Quickly is an urgency marketing platform that's been running innovative time
*  limited marketing activations for major brands for years. Now we're working together to build an AI
*  layer, which will use generative AI to scale their service to long tail e-commerce businesses.
*  And since Shopify has the largest market share, the most robust APIs and the most thriving
*  application ecosystem we are building exclusively for the Shopify platform.
*  So if you're building an e-commerce business, upgrade to Shopify and you'll enjoy not only their
*  market leading checkout system, but also an increasingly robust library of cutting edge AI
*  apps like Quickly, many of which will be exclusive to Shopify on launch. Cognitive Revolution
*  listeners can sign up for a $1 per month trial period at Shopify.com slash Cognitive, where
*  Cognitive is all lowercase. Nobody does selling better than Shopify. So visit Shopify.com slash
*  Cognitive to upgrade your selling today. That's Shopify.com slash Cognitive.
*  So let's get into the real nitty gritty here. I have a general sense. I think most of our listeners
*  will have a general sense of, you know, certainly pre-training, understand what that is, you know,
*  web scale data, next token prediction. Okay, cool. Then you've got your typical recipe. There
*  may be some exceptions or caveats to this, but typically next comes instruction tuning,
*  and then comes some sort of preference tuning. And that's where like reinforcement learning
*  from human feedback fits in. And then there's different algorithms. And you've mentioned PPO
*  and DPO that can be used to actually do that final stage of preference tuning.
*  That's the baseline understanding. Give us the next level of understanding, you know, what's most
*  important to understand after that? Yeah, so the, because I'm going to jump to the real nuanced
*  thing, which you might not even have in your questions. It's like, what are open recipes
*  doing and what are closed companies doing? In the open, we have the benefit of being able to train
*  on outputs from very strong models like GPT-4, which is something that we did. There's some amount
*  of legal uncertainty there, but we definitely put it, the wording in our data sets is like, look,
*  you're understanding your training on outputs from these models. But that definitely gives an
*  advantage in some way. LAMA, in order to get a model like GPT-4 needs to build LAMA 405B,
*  they need to do instruction tuning over their various base models and all of these things to
*  kind of get this distillation model to work from. So they are trying to do a similar thing, which is
*  a lot of the instructions are written by a very strong model. So a lot of math and code instruction
*  data is now written by for LAMA, LAMA 405B, for OpenAI, GPT models. And in that way, we are doing
*  something similar, but in the open, you can kind of take shortcuts, which is like, we don't need
*  to do this whole pre-training. We just go right to the model, which is best for SFT. I think that
*  stage actually looks very similar. I think we don't have as good of control over which prompts
*  we're using. I think the closed labs will do a lot of filtering and controlling of the distribution.
*  We do a lot of mixing, but it's mostly on taking the levels of known data sets and seeing what
*  their performance is on downstream evals. It's largely a process of adding in a data set to
*  instruction tuning for a specific capability and making sure it doesn't degrade other performance.
*  So if you have a math eval, which is the all capital math eval, which you can improve this,
*  but a lot of it comes down to the formatting. So some math data sets will have different
*  formatting and completion that will make it harder for your model to learn from that,
*  or it can affect something like GSMAK or coding or stuff like this. So these are the kind of things
*  that you're doing. And then also at the end, you're probably going to try to include some more general
*  chat data. We included 100,000 multilingual samples from Coherence IA because we know chatbot arena
*  has a decent amount of multilingual, even though multilingual wasn't in our eval suite.
*  And there are some other safety things which are more borderline, which is just like,
*  how should a model behave? And this is kind of what happens in SFT is like, there's some art to
*  it in squashing second order effects, but I think largely that's really similar to what the closed
*  labs are doing. And then at preference tuning, it takes kind of big turn, which is the closed labs
*  use humans for their preference data. We do not have the money. So we use all a LLM as a judge to
*  collect our preference data. I like to quote John Schulman saying on this, which is the pithy way
*  to say it is like human preference data is high noise, but low bias and LLM preference data is
*  low noise, but high bias. We do not know exactly what bias we are getting, but largely we can still
*  see pipelines of we collect our own preference data from various model generations, language models
*  label it, the preference data is good. The biggest change here is from data sets like Ultrafeedback,
*  which exists on Hugging Face. We essentially redid their pipeline with completions from the
*  models we had trained at SFT. And that gives a meaningful like low percentage improvement over
*  just using a random preference data on the Hugging Face hub. So it's higher effort. You have to go
*  through the effort of generating completions of LLM, making sure that's all right, getting diversity,
*  doing LLM as a judge. But that type of thing gives us like we give it across our experience
*  a time and time again, this like on policy idea of preferences, even with LLM as a judge was better.
*  So I do think that that's kind of what if you look at Meta's system diagram in their paper,
*  they show this they're like, we take a new model, we pass it in, we get new preference data, and we
*  train on it. The difference is that they do multiple iterations, which could be based on how they
*  get data, could be based on how their timeline is and stuff like this. I do think multiple iterations
*  is something we're seeing again and again, and we didn't look at but just kind of checking the
*  box of like, okay, on policy data does work for preference tuning. It's not a huge paradigm shift,
*  but it's a whole different approach than people have to do. We've seen some of this and kind of
*  like on policy and new like online DPO algorithm variants that everyone kind of gets like spiralized.
*  It's like, oh god, we have some other star PO algorithm I can't pay attention to. But the
*  algorithms were going in that direction where they're doing more of like generation from the
*  model and labeling. The way that we did it, I think is a bit more segmented, which is kind of like
*  closer to what Llama is doing. This at a high level is similar to what Llama 3.1 does. I've
*  heard that they weren't doing any fancy verifiable RL, any O1 stuff on theirs. What we kind of added
*  to this, I think I can, I mean specifically this is in the, like you can look at the acknowledgement
*  section of the paper and you'll see like one name and a bunch of normal grant garble and gobble.
*  It's not in the draft I sent you, but like there's one name there and he told us to just do RL on
*  verifiable outputs. So this is the stage three that we did, which is essentially taking the training
*  set from things like math, GSM 8K, and it's actually like IFL is verifiable because you like
*  count if the constraint IFL as a summary is a bunch of is an evaluation where there are
*  constraints on prompts like respond, make sure your response has X word, make sure your response
*  has X paragraphs, and these are things that are verifiable in Python code. So across these things
*  like math, instruction following, we have a system where you have these prompts with constraints,
*  and then we used RL to just give a reward if the constraint was satisfied. And we have seen on
*  multiple models that essentially improve GSM 8K, you can improve math, IFL is a little bit trickier,
*  there's a bunch of RL details there, but we essentially do this at the last stage to be able
*  to if our DPO like worsened our math scores, we can bring it back up. And with our pipeline where
*  the DPO data is very trained to our models, we actually get most of the math improvement there,
*  and the last RL stage is pretty minor, but if you take some old RL model off of Hugging Face,
*  you can apply this like RL verifiable rewards thing to it and get like a 15 point boost in
*  GSM 8K without a ton of degradation in other valves. So it's like we're really just scratching
*  the surface there, but the winds of AI, you can see that is going this direction, there's murmurs
*  that a lot of big labs do stuff like this, you definitely think they're doing it for code, we
*  haven't added code to code interpreter, O1 is described as a large scale RL system specializing
*  in reasoning tasks, it's like, oh, they're probably doing something like this, I think
*  one of our models just be left running RL for this math really long, and it started doing this like,
*  let me check my answer again, like redoing, redoing chain of thought within the chain of thought,
*  it's like, literally the thing that opening I was showing us where it's like, wait, let me check
*  that. And this is definitely not O1. But I think we've seen other papers in the space coming out,
*  there's like Vine DPO is one that's really simple, Vine PPO is very similar, let me get their name
*  right so it's easier for people, people have talked about QuietStar, that's a bit more
*  complicated, I think Trice is also one which is also a bit hard to understand but motivated by
*  the same thing. So the literature is going in that direction, but we kind of showed like, look,
*  you can do this in your preference tuning, you don't have to just do a math model, like you can
*  just add on these types of RL at the end and it doesn't blow the model up. So to kind of summarize,
*  it's like, as we go, we've unlocked, we have these three stages, SFP, DPO and RL, and each of
*  them, we're kind of taking more alpha from what industry is doing, like SFP is known, it works,
*  DPO, there's some new tricks that we need to uncover parameters, different settings, we use
*  this like a length normalized setting, but that's mostly known, but good information, but the RL
*  stuff is like, look, this is like real, we're beating llama numbers, we used RL, like, it's
*  still mind blowing to me that RL is becoming more relevant, I think, like 2023 is like, oh,
*  where's RLHF going, but now it's not even just RLHF, like, we didn't even have a reward model in
*  this, we can go do the technical setup later, but there's no reward model, it's just an RL value
*  function, and it's fine. So that's the summary of the training, it's like, probably somewhat dense
*  if you haven't heard these terms before, but also informative. Yeah, well, I like that, let's, we're
*  going to unpack it a little bit, but that's a great initial overview. So I'll maybe just comment this
*  from a couple different angles to try to understand the overall landscape better. For starters, like,
*  how much compute and how much value goes into and comes out of each of these stages, maybe compute
*  and data, like, you know, just relative amounts and relative value that you get from each one.
*  Yeah, so this is really a general purpose instruction model, which you have to caveat with
*  it, because I think if you have different domains, you have much different compute. I think
*  SFT is something we talked about a lot, the data site largely kept growing, we didn't do a lot of
*  sub-sampling results because we're searching for high numbers, our final mix is about a million
*  prompts, most of them are single turn, this model will not be as good at LAMA as at multi-turn,
*  we're not a meta AI shop, we don't need that as much, we don't have the evals for it, but it's
*  about a million prompts at SFT, if you're using, I can give really specific throughput numbers,
*  if you're using 32 H100s, you can train a 8B model in about a day on R code. R code is not
*  super optimized because it relies on transformers, I think you can get about a 40% speed up if you're
*  using kind of really specific code, which is something we might do in the future to only do
*  like Omo and LAMA architectures, because if you support fewer architectures, you make it much
*  faster, so that's like a million prompts. So that was 32 H100s is like a 24-hour train cycle
*  to train on a million prompts. Yes, for SFT. And I think at market prices, that's what, two,
*  let's say two bucks, prices have come down as I understand, two bucks per H100 per hour, so
*  60 bucks an hour, 1500 bucks kind of compute costs. I wasn't expecting this number, but yeah,
*  yeah, yeah. I think it's reasonable, it's ballpark that, like ballpark a thousand dollars,
*  because I do think we could probably get 90% of the performance with half the prompts. I think
*  looking at our mix, we have like 30 plus percent math. We were going hard on math trying to get
*  these numbers across, we ended up doing general math eval, and then we have subsets for specific
*  subsets of math, like intermediate algebra where we weren't as good. So we looked at the eval and
*  saw which micro subset was not as good and tried to make data specifically for that.
*  So we definitely, you don't need all of this math eval, so that's a good rule of thumb. DPO
*  in preference tuning, we haven't been able to show as strongly that scaling helps,
*  like getting more prompts in and keeps improving evals. I think it'll be like order of a couple
*  hundred thousand prompts. It's not as big. DPO does use more compute, especially at 70B, I think,
*  it's because you need the reference and policy model. Still, we've run these jobs and they take
*  like six to 12 hours if you're using somewhere between like 16 or 32 GPUs, much faster than
*  SMT just because the data set is much, much smaller. I think at 70B we added the normal,
*  we like changed our forward pass from the default like hugging face slash DPO implementation to make
*  it a little bit more efficient. We do caching reference log probes so you don't have to
*  store both 70B models in memory at the same time, because if you don't do these optimizations,
*  it starts to look a lot more like PPO where you need 128 GPUs or more to do at 70B, which is like
*  quickly you can see how PPO kind of balloons what is going on and it can take longer if you're
*  trying to really get the best absolute scores. So I do think like SMT is by far the biggest
*  compute because we have the most tokens. DPO, I would say ballpark a quarter of what we talked
*  about for SMT would be a couple hundred bucks and RL is probably like especially at 70B can be almost
*  similar to SMT if we really run it for a long time, but you can get most of the benefits probably in
*  a similar amount of compute as DPO. So the RL curves look remarkably similar to like kind of
*  old school RL tasks where at the beginning they get the most improvement and then it's kind of
*  like level and bouncing around and like maybe going up a little bit. So if you do like one epoch,
*  which was this first improvement, you're going to save a lot of the money, but we're like, oh,
*  we're trying to get the best numbers. Let's let it run for a few more days and see what we're doing.
*  Hey, we'll continue our interview in a moment after we're from our sponsors.
*  Even if you think it's a bit overhyped, AI is suddenly everywhere from self-driving cars to
*  molecular medicine to business efficiency. If it's not in your industry yet, it's coming and fast,
*  but AI needs a lot of speed and computing power. So how do you compete without costs spiraling out
*  of control? Time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a blazing fast and secure platform for your infrastructure, database, application
*  development, plus all your AI and machine learning workloads. OCI costs 50% less for compute and 80%
*  less for networking. So you're saving a pile of money. Thousands of businesses have already
*  upgraded to OCI, including MGM resorts, specialized bikes, and fireworks AI. Right now,
*  Oracle is offering to cut your current cloud bill in half if you move to OCI for new U.S. customers
*  with minimum financial commitment. Offer ends 12-31-24, so see if your company qualifies for
*  this special offer at oracle.com slash cognitive. That's oracle.com slash cognitive.
*  I am really excited that our new sponsor, 80,000 Hours, is now offering free one-on-one
*  career advising sessions to cognitive revolution listeners. 80,000 Hours aims to be the best source
*  of advice for people who want to do the most good that they possibly can with their careers. We
*  typically work for about 40 years in our lifetime, and we work about 2,000 hours per year. That is
*  the single biggest opportunity that most of us have to make a positive contribution, and it's worth
*  being strategic about it. That's where 80,000 Hours can help. I actually used their career
*  advising service myself. Two years ago, I had just finished the GPT-4 red teaming project,
*  and I wanted to do anything I could to nudge the AI future in a positive direction. But what could
*  or should I do? That was not clear. After my call with 80,000 Hours, I got a number of connections
*  to outstanding individuals in the space, and over the course of the follow-on conversations,
*  I developed confidence that this podcast was one of the projects that I should pursue. Today,
*  I'm thrilled to have built an audience of thoughtful, high-potential people that 80,000
*  Hours wants to help. To request a free one-on-one career advising session, follow the link in the
*  show notes. It's 80,000hours.org slash cognitiverevolution.org slash cognitiverevolution.
*  Sign up for a free one-on-one career advising session. Figure out how you can make a positive
*  impact on the AI future, and I think you'll be glad that you did.
*  How about the eval improvement through that process? I guess if you have a base model,
*  you have to basically few shot. If you go to instruction tuning, then you could just do
*  zero shot or few shot. How are you- Yeah, the value setting is crazy. There's a lot of iteration
*  on it. I would say that for performance, roughly, I think we get like 90% of our performance at SFT,
*  and then the last 10% of mix of DPO and RL. I think alpaca eval slash vibes things,
*  you get the most from DPO and RL rather than SFT. But at this point, our SFT mix beats,
*  it beats on our eval suite, the llama 3.1 numbers. But it's very focused on our evals,
*  and I think the preference tuning softens it a bit to be a nicer model to talk to.
*  The eval suite is complicated. I don't know all the details off the top of my head. It's good to
*  look at the paper, but we tried to do... There's this whole distinction between pre-training evals
*  and post-training evals. And I do agree that most post-training evals should be using a chat
*  template. So you're generating from the model to generate tokens. A lot of them are CO2 chain of
*  thought, and there's a distribution over the number of in-context shots. I think there's some
*  that are zero shot, there's some that are eight shot, depending on the domain. And probably the
*  trickiest thing to manage is answer extraction for reasoning, which is does the answer appear in the
*  format that eval expects? Particularly on math, llama 3.1 uses what's called the Minerva format
*  and a specific prompt. And we use what is called a flex format, which essentially if the default
*  writing is the answer is in boxed, you also allow boxed and the answer is colon and one other thing.
*  And this is mostly to be fair to Quen. So Quen is a fun example where their 72B model gets a score
*  of like six with llama 3.1 setting, but a score of 74 with our setting. So it's like, okay, like
*  we're like competing with Quen instruct in a way, like we have to have a setting that is not just
*  what llama does. And I mean, all of the other labs are doing things like this, which is tailoring
*  their training to eval. And it's hard to know what they trained on. We did a lot of work to
*  decontaminate all of our training data sets on the evals that we're doing for development. We also
*  have an unseen eval suite. So we do a few methods to check for exact match and overlap on all of the
*  training data sets that we used throughout it, which is some of the final data sets are also
*  going to release decontaminated versions of like other data sets along the way. So popular names
*  like open instruct, NVIDIA's daring anteater data set has some contamination on math.
*  For example, like the hugging phase in numinomath, TIR, which is tool integrated reasoning,
*  which was for a math competition has math contamination. So you have to remove this.
*  It's like they were using their model for a Kaggle competition, not for like fair evaluation.
*  And it really goes to show it's like one, we're releasing the data, but two, we're showing like
*  how easy it is to have contamination. So it's like, yes, we need more people to release it.
*  So we don't know if any of the models we're comparing against trained on test either on
*  our development set or unseen set. It's just like, we can't know. We found a lot of contamination
*  out there, but we don't know what other people are doing. And it's kind of, I think there's
*  probably a snarky paragraph in the paper, which is like, we don't know which of any of these
*  models trained on the evals. It's like, okay, where's for the best. When you find the contamination,
*  you're finding it in data sets that other people have open source or you're using some sort of
*  diagnostic to detect in the model. Some techniques like that.
*  We're looking at data sets. People are working on model diagnostic, but we're looking at data sets.
*  And I think there was this weird thing. We'll talk about data sets where essentially the biggest
*  thing we're doing is exact prompt match. So if a certain data set training data set has more than
*  like a 2% exact prompt match with one of our test sets, which is like, that's the percentage of the
*  test set in the prompts exactly. We consider that contaminated and remove them. The other thing is
*  like, can you detect if models trained on certain test sets? So I have earlier in this year, my big
*  project is reward bench, which is like trying to build an ecosystem for evaluating reward models.
*  Now it is going, there's lots of academic papers on it. But one of the weirdest things we found is
*  recently substantial contamination on reward bench prompts, which was taken mostly from other test
*  sets was generated by Lama instruct with the magpie method. So magpie is a synthetic data method
*  that manipulates the chat template to get the model to generate prompts in distribution of what
*  it was trained on. So this is the type of like weird head scratching you need to do to do like,
*  is a model trained on something? You can't prove it, but if you have the weights, you can get the
*  model to like generate ish prompts from its distribution. And then you can check those on
*  test sets, which is really funny because magpie is meant as kind of like a training architecture
*  for like generating new data. But when you then realize that that might be what you need to do
*  for a vows, I told the author and he's like, Oh, cool. Another use case for my paper, which is really
*  funny. But I do think that whole ecosystem is going to continue to grow a lot because it's,
*  you need it to have some source of truth. I think evals are only growing in value and cost, and
*  you need to be able to audit the models to assess this across industry. So there's going to be some
*  mix of new startups, academic research, regulation, undetermined. Like the whole thing is kind of a
*  fair game. Yeah, interesting. Okay. Let's go back to the post-training stages. And I want to get you
*  to try to help me develop my intuition for how the model and how the model waits are evolving
*  through that post-training process. I have a pretty nice little story that I tell people about the
*  pre-training process where I'm like, you know, given some text, the model's job is to predict
*  what comes next. There is a ground truth as to what comes next. And so it outputs a distribution.
*  And then the question basically amounts to how can you, with the chain rule, how can you tweak
*  all the little numbers that are the weights in this model to just nudge yourself so that you're
*  a little closer to correct? And we just do that a ton of times. And obviously there's batching and
*  other complications, but the atomic unit is you make one prediction, you get a score, and you nudge
*  yourself to be closer to having made the right prediction. Now that gets a little more complicated
*  in various phases of the post-training process, right? Instruction tuning, from what I understand,
*  mostly is similar, right? It's mostly the same. It's the same, but you add in new tokens. So you
*  add the tokens to help constrain the model, which is like user or some other EOS token. You add
*  these things in in a specific format. So you have to learn a little bit of new tokens, but otherwise
*  it's exactly the same. So that's kind of weird, a little bit counterintuitive in as much as,
*  at least for some sort of instruction tasks, and this is, I guess, a natural segue to the
*  preference training, you think what you really want is to be telling it what's good and what's
*  not good, but with the instruction tuning, you're still basically just saying this is exactly the
*  ground truth tokens you should have predicted, and all the weight adjustments are just specifically
*  toward that exact string. Yeah, it's almost like for simple things, I don't think you need a lot
*  of SFT data because you're just manipulating the weights to be more focused on this type of
*  formatting. You need to do enough so that this is the way the model outputs, but for specific tasks
*  like math, I think you can make a lot bigger gains, which is just like the model has not seen a lot
*  of this, and you're really trying to do the same thing that you do during pre-training, which is
*  teach the model to do chain of thought math. You need to have that somewhere to kickstart things.
*  Pre-training data probably has some of it, but I think that that's a balance that we'll see evolve,
*  which is like what if the basic amount that you need to do some instruction following, and then
*  how much more do you need for specific capabilities, I think. At some point, a good thing for that I
*  did many times, and this project is good for the readers, go look at the Llama report and look at
*  the percentage of instances per domain at instruction tuning, and at instruction tuning,
*  they have way higher math coding reasoning than preference tuning. I think those are the domains
*  where the model needs just more flops to understand the basic capabilities in SFT, but at preference
*  tuning, it becomes a contrastive loss function, either through DPO, which is like pairs in
*  comparison them. If you dig into the DPO math, it's actually some weird double negative where it's
*  decreasing the probability of the rejected response. It does that more than increasing
*  the probability of the chosen. There's weird oddities in the actual DPO math there. If you go
*  really deep, PPO is almost more intuitive where you generate new samples, you have a value model that
*  assigns attribution to each of the tokens where higher number is good, and then it tries to increase
*  the likelihood of things that it sees as being good. In this case, it's guided by a reward model,
*  in our case, it's guided by is the answer right, and it becomes much more flexible. I think
*  DPO is somewhat restricted to the generations that you give it, but RL in that way is flexible,
*  where I think it just can kind of change the behavior of the model more. I think when we
*  apply math, we see that it takes different reasoning steps. We see those kind of different
*  types of changes than you see at SFT and DPO. I do think there is going to be a lot more
*  understanding of what these stages actually do. It's kind of funny because SFT is where most of
*  the performance gains come on evaluations from chat to capabilities, but it just does really
*  feel like when you do these and when you look at the loss functions, that there's kind of more that
*  you can change about the weights doing RL or doing this kind of direct preference optimization
*  sort of thing. That's something that we've heard for a while. I think leaders in RL and Jeff have
*  said RL is just a more flexible loss function. There's a lot more scale you can do. I think that
*  was the framing that somebody like Jason Way at OpenAI gave in a talk. It's like, look, RL has a
*  lot more leg room because the loss function is very different and we haven't explored it.
*  Things like O1 and kind of our own experiments make me more optimistic in this. It's just very
*  weird. You can do a lot of weird things. It changes the model. Notably, the VAL scores don't
*  go down that much and it will take a lot more intuition both on the individual level and the
*  academic level to understand these parameter changes. It is fundamental to the fine tuning
*  domain where it's like RL is doing something very different than the previous loss function. In some
*  ways, it's remarkable that you can just do SFT and pre-training and then you can just throw RL at it
*  and the KL regularization is enough to just hold it in place. You just change loss functions
*  99% of the way there and it doesn't break everything. That type of thing makes me
*  get a lot of sympathy to the whole Dario whatever mindset of they just want to learn.
*  It's like there's something complicated going on that I don't have deep enough intuitions of
*  deep learning to grapple with. Yeah. Okay. That's really good. Let me
*  just go back to a couple of points for quick follow-ups. First, the KL regularization,
*  that is basically a way of just anchoring to the earlier distribution. Your loss function has
*  multiple terms and one of them is subject to getting better in the way that we want you to
*  get better, which we'll come back to in a second. Also, don't change too much. Is that basically
*  the right intuition there? That's what it is. You essentially look at the log probes of the
*  original model and the new model and you make sure that the difference in probability is not too big
*  between your RL model and your reference. I think the way that we phrase it is you have a KL budget.
*  You can only change the model so much. Once you reach your budget, you normally don't expect the
*  model to keep changing if you're doing value updates because it can't make substantial changes.
*  It's just moving around in the same neighborhood, which I think is a nice framing. I wish more DPO.
*  DPO is different where it's a controlled KL distance through their beta parameter throughout
*  the number of epochs that they're doing, whereas RL is where doing online RL is a little bit more
*  open-ended on the KL side of things. But I do think this in general in post-training,
*  showing more plots of performance versus the amount of KL that you spend is very nice.
*  I think historically, these just sound like total random numbers and people not looking at this.
*  It's like PPO KL will be 10 to 20 scale type thing. This is when you're doing the full thing
*  on chat, for example, or like GSM 8K, really basic math KL is like one. So it's like we're really,
*  really not changing the model very much doing this RL for math compared to what you would do
*  if you're doing PPO for everything. But if you also compare that to like best event sampling or
*  something, best event sampling over a reward model also has way lower KL spend than doing this full
*  PPO online RL thing. And I don't know the intuitions off the top of my head for where DPO falls,
*  but it's like all of these preferences, that's like kind of a way to measure how much
*  you're changing the model in preference tuning. It's like, what is the KL difference across a
*  controlled set of prompts? There's a problem where we're in all of these numbers that I'm saying,
*  it's on a different set of training prompts. So it's almost like we need to have like a standard
*  like these are the prompts that we about these hundred prompts are what we evaluate our KL
*  distances on across different domains to really see how much the model is moving in general.
*  But I think that's the biggest, that's a good way that people can look at it.
*  That one that you're anchoring to is the original base model or it's the instruction tuned model?
*  Instruction tuned.
*  And that just stays no matter how many like iterations you're doing.
*  The reference model stays the same the entire time.
*  There are people that there are experiments where you can do like do one round of PPO
*  with your reference as the SFT model. And then you can like start another one with your reference as
*  the first PPO model or DPO. So people do things like that. It's just not as popular.
*  There's definitely some papers there, which is like moving like resetting your DPO reference
*  to give you more ability to learn. I don't remember the names off the top of my head,
*  but that is a sort of idea that people fiddle with.
*  And these KL divergences, they are the penalty gets, it's like a square function, right? So
*  the penalty gets bigger, the more you sort of drift. And that's kind of where this like budget
*  notion comes in is like you sort of have a limit as to how far you can move before that
*  term, I guess, starts to dominate basically.
*  This is like what is there's an approximation that you use in a lot of KL. In a lot of RL,
*  you use an approximate rather than a full KL, where the approximate you're essentially just,
*  I have I pulled it up, I have the silly like RLHF book that I'm working on, which is mostly
*  notes on fundamentals of RLHF. And the regularization is this. And it's like there's
*  a difference between what a lot of people do in these implementations as an approximate KL.
*  I think that like John Sillman has a blog post on this that everyone references where the
*  approximate is you just subtract the log probes of a generation for the policy model. You do
*  that minus the reference log probes, which is a different function than the full KL.
*  I don't know if it's a change. It seems like that's a change between square and not.
*  Just kind of thinking about it off the top of my head without having the exact tail equation.
*  Interesting. Okay. So there's presumably all of these things like could work and probably have
*  worked to some degree and have some pros and cons. But yeah, that sharp bottom versus kind
*  of flat bottom is an interesting distinction. So I still want to get a little bit better intuition
*  on how these multi-token evaluation and multi-token comparisons work.
*  And maybe we could break this down also by PPO, DPO. I'm getting like as a user,
*  if we start with the human experience, I either am presented to generations and ask to say which
*  one I like more, or I might be presented one and asked to rate it one to seven, or maybe I
*  presented two and asked to rate them one to seven or whatever. So the signal is derived from that.
*  In a lot of these schemes, train a reward model on that so that we don't have to always have a
*  human doing the evaluation. So now we have a reward model that attempts to score in a way that the
*  human would score, but it's still giving you this one or that one is better or here's a one to seven
*  rating of these outputs. The critical distinction there, I think that I'm still kind of struggling
*  to develop like a clean story. I can tell my friends who aren't so obsessed with this as I am,
*  or certainly not as you are, is how does that score translate to updates when it has to go through
*  this multi-token generation? Because I used to have, with the pre-training and the instruction
*  tuning, I have this simple, you predict one token, you can score that one token, you can update
*  on that, everything else is sort of aggregation of that. Here the score applies to this whole
*  generation and so there could be weird forks in the road or even if just you add an extra token,
*  now everything is kind of off by one token. How do I compare base generation to the current policy
*  generation given that I can't do it on a token by token basis anymore?
*  So the RL math is essentially you will give it a label based on the whole trajectory and then the
*  value model, if you're doing PPO, the value model will take a generation and it will output a value
*  per token. Then you will have the label from the reward model, which is like the reward from your
*  environment, and that is used to update the value model to kind of have these per token updates.
*  And then the policy is actually going, like in PPO, you're actually going to be taking
*  attribution for every token in your batch and doing updates based on what they think will
*  be a long-term better generation in PPO. That's very different than DPO. I don't have like a per
*  token understanding of what is happening in DPO because it's, if you think about the loss function,
*  it's doing essentially all of the tokens are kind of grouped into chosen or rejected, and it's trying
*  to increase the margin between chosen and rejected log probes across the sequence. I think early in
*  the DPO days there were questions on length issues because what you're looking at is the sum of the
*  log probes. So then if you're like all negative, like they're all like negative numbers because
*  it's a log of a probability, they're all less than one, so they all become negative numbers and
*  you're summing them up, and it's like what does that do because you're therefore like increasing
*  the margin between these two negative numbers is what the loss is doing. So I don't exactly have
*  as clear of an intuition there, but you kind of look at the losses and see how those are different,
*  where there's I think a bit more like per token attribution in RL versus DPO, and they're both
*  substantially different than SFT. So in the PPO side, what's the original ground truth
*  that translates a generation level score to token level value? That's often glossed over, I feel like.
*  It depends on your training set up. So some setups you'll start the value model from nothing. So then
*  it'll take a few hundred steps to take the scores from the reward model to kind of warm up the value
*  model. So you can kind of see if your value model is a random init, you can see this where your like
*  value model loss has to converge before your policy will start changing notably. There's other ways
*  where you can init a value model from a reward model or an SFT model, which is what we do on this
*  like verifiable outputs to kind of make learning a little bit cleaner, and I actually don't know
*  how that changes the value model exactly. I think that essentially that it must be some mapping
*  between like the log probes and value that it is doing, which is why you would warm start with the
*  model, but I don't know exactly what that mapping does, but essentially it takes steps to learn that
*  this represents, and it's Bellman updates, it backthrows from this final reward, is how the
*  value model learned. So it takes time to get to the earlier tokens, which is what the warm up is doing.
*  Fascinating. Is there a intuition or even just an observation as to kind of what sort of different
*  tokens get what kind of value? Like presumably something like the answer is would have like low
*  value and then the actual answer would have high value? Or the answer is might have high value
*  because it knows that the answer normally follows it or something like this. I think it's probably
*  not easy for us to build intuitions on this because the feature space is so big.
*  It's like how are you going to build intuitions over what? Like in O1's case it's like is weight
*  a high value token, but if it's like too high value it would only just be like wait wait wait
*  and never answer. So there's definitely some like weird things that I don't know how clear it is to
*  get intuitions out of it. Okay. It's like all the tokens are conditioned on the previous tokens.
*  It's like the value is conditioned on everything that has come before it. So it's like not just
*  the token. It's like the token in context. Have you looked at the end? This is a bit of a
*  digression, but have you looked at the Entropix project? I wonder if there's a detail, but I do
*  think it's a good direction. Yeah, it seems like there's some connection here where basically,
*  I haven't studied that in depth and I don't think it's like a total game changer necessarily,
*  but it does feel like at least the seed of something that could be a big deal.
*  Inference time compute is very related to RL where it's like having a good model from RL that can
*  attribute value is very useful to spending more on inference and we'll see all of these things
*  continue to proliferate. And I put Entropix more in the inference time compute thing, but there's
*  very similar intuitions. Like if you sample more within a bat, if you sample more completions from
*  a prompt in RL, you're essentially like exploring more to potentially find a high value completion.
*  And if you're doing inference time compute, a lot of it comes down to how do you sample from the
*  language model and encourage it and like re-weight or interrupt it or change the sampling to find the
*  right completion. And that's where like multicolored tree search type things come in. It's like
*  search over reasoning steps or all of these like Q star or whatever type of things you want to go
*  down that direction. It is related, but I think you can draw a boundary between training and
*  inference and it's okay. Yeah, the connection that I'm, the thing that's bringing to mind for me is
*  just this sense of looking at the logits on a token by token level and sort of inferring from
*  there, you know, like, is this going well? Is it not going well? Is that what Entropix is doing?
*  Basically, I mean, it's kind of multiple modes where if the model is like confident,
*  you know, for multiple tokens in a row, and I should say I'm a little bit out of school on this
*  because I've only studied it a little bit, but if it's like high confidence, you know,
*  it just kind of proceeds. If the logits start to indicate low confidence, then it will like
*  manually inject a follow-up question in some cases. Yeah, so it's like fancy. If that doesn't work,
*  it'll like double back and try again. Well, I would say that I do think that something like this is
*  what like O1 could be doing. It's just like, we see how easy it is for RL to go off the rails.
*  Like if you run RL for a long time on something like IF avowel, which is these constraints,
*  it literally does exactly the constraints. It's like, please include this word in your answer
*  and make your response 100 words or longer. It literally just will print the word 100 times and
*  then stop. It's like, it's like stupid stuff like this. And it's like, well, maybe if you can do RL
*  plus like have some more fine-grained control over the generation, you're like, oh, it kind of,
*  you squint. It's like, you just have to figure out how to put these things together.
*  So one more thing on DPO versus PPO before we move on. So PPO has this reward model. Just
*  make sure I'm understanding correctly. PPO has the reward model. There's then this process of
*  translating the reward score. I think the right intuition is that the reward model is trained
*  to do PPO, but in the RL framing, the reward model is actually the environment in a way.
*  So the environment in RL is supposed to be what returns the reward. So the reward model is a very
*  constrained environment and your actions, your inputs to the environment are prompts and your
*  actions are completions. So it's like a totally broken RL environment, but the reward model is
*  not part of like the training update. It's more of an isolated thing that we just happen to train.
*  Gotcha. And then to compare against DPO, there is in PPO, there's this process of
*  mapping or translating a score to token-wise value, which then goes into the back prop
*  versus in DPO, there is no reward model, right? And just contrasting two outputs and some fancy
*  math, which nobody seems to have a great intuition for, maybe the original authors.
*  Authors do. I've talked to them a lot. I feel like I had more of an intuition for this like
*  six months ago when I was really in vogue, but I do think it's still changing the tokens individually.
*  It is in that way doing something similar, but it's not doing it through a value model.
*  It's only mediated through the loss, which looks at the sums of log props.
*  So it kind of removes that intermediate step.
*  Yeah. So that's simpler, requires less compute, requires less GPUs,
*  and just for whatever reason seems to consistently fall slightly short of...
*  Yeah. I mean, in our setup, we tried to throw PPO in at the end and we haven't gotten PPO to beat
*  our DPO setup again. So it's like, okay, we went through this big process where we saw PPO is
*  better. And I still think like if we kept hammering at it, we could probably make PPO better,
*  but just experimentation time and data is so much more important that it's just like,
*  we're not going to take four times the compute and experimental time. It's not worth it.
*  At this point, you're like, oh, our PPO is not as good. Maybe it's like half that we
*  don't really know how to train a reward model because we haven't been focusing on it as much,
*  but also half of just like it's harder. So I do think that it's funny. It's such a great,
*  silly debate. It just never goes away.
*  Yeah. But it's a great, very good zoom out corrective for you to give me there too,
*  because as much as all this stuff is easy to go down a rabbit hole on, data quality matters
*  more than which algorithm you choose and probably matters more than anything. Maybe you could give
*  some intuitions there. Yeah. It's like we baseline
*  versus 2.2 on our version 2.3. And it's like 2.2 versus 2.2.2.2.5, which in DPO to PPO is like 1%.
*  And then on our values like 2.2 to 2.3 is like 14%, which is all just like data curation and
*  process and stuff like this. So it's like, okay, there's your number. If you want to go off and be
*  algorithmic, academic, most cases you're going to be dividing 1% to 2% versus making really specific
*  data where you care about, where you can get 10x. I'm not surprised. That's probably what industry
*  does too. These post-training teams are like, you're the person generating Python code data.
*  You are a full-time Python code instruction and preferences and prompts and filtering lead. And
*  you do it and you generate crazy good data on one really, really specific thing that may or may not
*  be in the actual about suite. It's like, that's like even we aren't doing like we have people on
*  data, but it's not like they're spending a month on this one really specific thing. And you have
*  12 people doing that. No academic lab will ever do exactly what the closed labs are doing in that
*  level of depth. Yeah. I mean, it's super resource intensive. I guess you said you trained a thousand
*  instances of 8b in this whole project, right? If you look at our Val leaderboard, we have like
*  a thousand plus models. So not all of them are 8b. Some of them are tests, but like, I think it's
*  ballpark for if you want to get this level of results, that's probably about the process that
*  you will need to go through. Like you could be twice as good and then it's 500, but that's not
*  that big of a change. Yeah. So I just want to get a little bit of like a procedural understanding
*  for what this, you know, the overall trajectory of the project is, and maybe we can contrast it
*  against something that I do and that I've like talked about in previous episodes, which is just
*  fine tuning a model for a specific task. I've got a whole kind of lecture and how to on that.
*  And I tell people typically start with 10 gold standard examples. The quality matters most,
*  just staple your pants to the chair and work on those 10 examples until they're
*  the absolute best you can make them. That's small enough. You could probably do few shots in a lot
*  of cases. Maybe you'll want to fine tune depending on whatever. And then I typically tell people,
*  expect three rounds of iteration where you're going to do that fine tuning. You're going to
*  find some weaknesses in it. You're going to then come back and augment the data. If it's like,
*  generally not good enough, you need to like 10x the data is usually what I tell people. If it's an
*  edge case that you just hadn't considered before, you can maybe just kind of patch with,
*  you know, give it five or 10 examples of that situation and how to handle it correctly.
*  And, you know, three rounds, maybe more if there's like a lot of different edge cases you want to
*  handle over time, typically should get you there. If you're doing one task, obviously a huge
*  difference here is you're doing 15 minute discussion because partially I'm also reflecting on it. And
*  it's very interesting as a, I mean, this goes all the way up to like the CEO is like, I'll sit down
*  it's like, how do we manage the fact that we have extremely excited students? So a lot of AI2 is
*  collaborators with UW, which is like total best of the best super motivated students want to do
*  something, but they can't do these whole projects. And then you have like people like me or slightly
*  like people like me that are my same age. So I'm like a junior mid seniority research scientist,
*  did a PhD, have some experience, but I'm also like not a professor. I have more visibility. So that
*  ends up being like, I end up being effectively more senior because I have distribution and I have
*  done things. But you have also these people that are like research scientists full time.
*  They have some projects they can focus on this and do a lot of it. It's like, how do you balance
*  these incentives is very hard. So I would say that for this project, in a academic sense, I would be
*  last author, but in an industry sense, I'm first author, because I just have to do all sorts of
*  random things. It's just like incredible, like just hold everything in your head and try to keep
*  track of everything at once. And there's some there's admin help, and we have meeting structure
*  to help with this, which is like, the philosophy section of the paper is like, what are we trying
*  to do? And are we on track going in this direction? Because what it starts with, it's like, I would
*  say there's like, four to seven leads that have done a substantial amount of like, first author
*  level work in a normal academic setting, which is like making a lot of data running a ton of
*  experiments, building the whole about setup, there's like all these things are just like,
*  at the beginning, we kind of sit there is like, what do people want to do? And we haven't talked
*  about this. But like, one of the things we really wanted to see is like, llama two and llama three
*  did rejection sampling. It's like, can we make rejection sampling work? And it's like two people.
*  And all they're doing is like, can we make the numbers go up with rejection sampling? And this
*  is like a negative result we have, which is like, we did a lot of things, there's some interesting
*  things like, if you're using an AP model, the generations are less good than the instructions
*  we start with. So for like, generating new instructions, then we do SFT on them, it like
*  kind of makes sense that it would make the model worse. But it's like, we had these two people doing
*  instruction tuning, some people started with like, let's compare the DPO alternatives, DPO, like norm
*  DPO, whatever all these things are, figure out what these settings are. And then some people that
*  are like, where are the open data sets? Can we get them? Let's start training on open data sets
*  again. Where are we falling short of llama? So the kind of start is like this algorithmic phase.
*  And then you get the bearing of like, okay, where are we not doing well with llama? Are things just
*  not working? Let's kill them. And then it kind of shifts into the second phase of like, let's try to
*  get really specific data. Let's kill some of our long tail projects. And we're working on specific
*  data. And then you continue to mix, you continue to make your eval suite more stable. When we start
*  the project, the eval suite is not that stable. It's like, huh, like we're getting crushed by llama
*  on this thing. But like, the formatting is totally bizarre. It's like isoteric, because we tried to
*  recreate the entire llama eval suite in our code base. So there's like some evolution there early
*  in the project as you converge on evals. But then it becomes much more exploitative, which is like,
*  we build new data for specific capabilities. So people are kind of heads down, like building
*  math data, building IFL data. And then it's probably a trade off of like, some people are
*  working on SFT data and SFT mixing. And some people are working on DPO and DPO mixing. And then like,
*  soon this whole like, does this RL thing work? Which takes like two people to start doing this
*  RL thing kind of on their own, but like part of this project. And then as the weeks and months go
*  by, like you try to finalize SFT. So like, SFT is finalized, the data mix was probably like a month
*  ago, then we have to, we did more decontamination, or like, oh, we have to turn it again. Oh, we're
*  70B hyperparameters are wrong. Oh, we have to turn it again. Oh, we have to try model merging. We have
*  to train it a few more times. The quick note on model merging, it's like, it's a safe bet to merge
*  SFT by running multiple seeds on the same data set. But it could often be that just by running on
*  multiple seeds, one of your seeds for SFT is actually going to be the best. So if you want to
*  get a good SFT model, you want to just train it three to five times across a few random seeds,
*  which is like pretty funny. It's just like even more compute. And then like it for the last month
*  has been mostly like final touches, and then full on DPO, which is like we have to generate, we have
*  to do this on policy thing, which takes a lot of API credits, and a lot of just hands on which is
*  like you take your SFT model, you run completions. And then those are like the person that just owns
*  on policy preference data. So you give them prompts and models, and they do like VLM to make
*  generations. And then they use the open AI API to do LLM as a judge. And then they're like, here's
*  your preference data set. And then you have, we have different models, we have 8B, 7DB, we have
*  OVL models. So it's like, this is the person in the team that's just owning, like they make preference
*  data. And then you have to do this. And then those people, that goes to your training person, training
*  person does DPO, they pass it to RL. So you kind of just have these people that naturally,
*  to zoom out, you have people that naturally converge to different areas. And this is probably 10 to 15
*  people that are actively involved most of the time. At this size, we did not need strict delegation
*  in management. If you go to the llama size, 100% chance you need delegation in management in rules
*  who makes what decision when. Effectively, I'm like softly that person, which is like making the call
*  on what SMT mix is final. But there's definitely an interesting transition organizationally,
*  which is like, you cannot scale it more, because it becomes a mess if you're more than 10 to 15
*  contributors on one of these language modeling processes. But then there becomes a big cost if
*  you add in managers, because then you have to do a lot more like, delegation of decision making
*  and stuff like this. So in some ways, you can tell by how I was describing it, a lot of this is like
*  somewhat chaotic and freeform and just relying on people being in the weeds in the details and
*  very happy to communicate with the various people that they know needing it. And a lot of that is
*  autonomous. It's just like, I can't be over Valentina's shoulder being like, get your DPO
*  model to Hamish to do RL on. It's like, they just do that. And a lot of those processes are messy.
*  Like we describe our standup meetings as chaos. And it is very funny because we just sit down,
*  we write our updates, and then we do 50 minutes of just like chaotic technical updates, based on
*  what the heck people are doing. It's like, the just information overload in a lot of ways. So I
*  don't know, I think that accurately reflects the chaos. But there is like some kind of cadence to
*  it of like, what is your goal? Are you on target? How do you like make decisions to kill sub areas
*  of the project? Like kill rejection sampling, kill long context, kill multi turn. Like these are just
*  things that as you get better numbers, you know you need to get the model out. So you just have
*  to keep reducing entropy and reducing entropy. So it kind of goes to the space of like, you explore
*  in the middle and then you get momentum and you collapse onto a final model. And we can do that
*  much faster than Lama can. Like because getting Lama out is a bigger issue for them legally,
*  strategically and stuff like that. So they do a lot bigger of an investment cycle to get these
*  models out. I think even more so than like OpenAI. It's like OpenAI and Google and stuff release these
*  new API models every couple months. Whereas Lama is like, you get like one or two Lamas a year,
*  and they drop the weights and it's final. So it's like kind of interesting to think about the
*  distributions. And there's, I mean, there's a lot of policy discussions on like weights being final
*  and out there. But like that type of stuff is also informing the development cycle, which I
*  haven't talked about at length. Yeah, that's sounds fun. It is. That's a lot.
*  So when you are doing the day to day experiments, what sorts of, it kind of reminds me of chem,
*  I was a chemistry research assistant as an undergrad in reaction development. And there
*  were some commonalities where it was like, you know, we throw a bunch of reagents in,
*  we kind of run the reaction, then we come see, you know, come back a couple days later and measure
*  how well it works. And at times we were surprised and it was a high dimensional space. So you could
*  kind of more acid, less acid, let's do an experiment with varying amounts and then vary the
*  solvent and just all these different things that you could vary. It sounds kind of similar where
*  I'm imagining that like the thousand things were actually like 100 experiments of 10 variations each.
*  Yeah. So this is the tension. It's like, how do we be scientific at the different stages? So different
*  things we can run ablations on and some of them like mixing are just like, here is our process.
*  It's like, we did this. It's like, it's very much unacademic. But in like the RL side, it's like,
*  oh, we can compare different initializations with value model, you can compare different
*  regularization, these specific hyper parameters. So there's definitely both of that, which is like,
*  you need people that can operate in this chaos, which is just like intuitively, like, where do we go?
*  But you also need people who are very scientific, like, yes, no, does this work based on X clear
*  results? So it kind of, it has the full spectrum there. And I, I mean, I agree. I like being,
*  my background is in microelectromechanical systems and other kind of EE stuff before
*  kind of shifting into AI. So there is that kind of messy, like, in the lab nature of like, you just
*  trying to build this thing or you're like trying in that case, it's like you're doing a reaction.
*  It's like, it works or it doesn't in some cases. So you're literally just like, I guess maybe
*  a better way to ask the question is how much juice are you finding in different dimensions of
*  exploration? Like you could vary the mix of the instruction, fine tuning, or you could vary some
*  hyper parameters or, you know, what are the sort of classes of things? But I think most of its data,
*  it's like, you kind of find hyper parameters that work and they don't really change. But within that,
*  I think there's still a very high level of juice. I think we're doing a general model, but I still
*  think we could fit more evals into our mix and improve performance without substantially changing
*  the size. I think that like the amount, like you were talking about this with your recipe,
*  like the amount of data that you need to target a specific eval is actually not very high.
*  And like, there's a lot more that you can do with that fact. There's a lot more of post training
*  that is not really touched. And I think that the opportunity is high. It's mostly about setting
*  yourself to have an eval feedback cycle. I talked about killing these different capabilities and
*  that's because we didn't have evals that we liked. It's like, I'm 100% sure that we could improve them,
*  but it's just much easier in a distributed environment where you have a source of truth,
*  which is your evaluation. Because the big thing is like, how do you develop character? I think
*  character is something that you don't have evaluation for in your models. And our models,
*  if you compare them to Claude, will not have as consistent of a character. And I especially think
*  for these models that are going to many users, character is important. And I find it very fun,
*  but it's like, I don't know how to motivate the right people to do a four month, like,
*  let's like, let's make like, almost like, like chef's kiss emoji, like really right spot on. Like,
*  CEO is going to be like, dude, what the heck are you doing? Like, what is happening? So in that
*  regard, like, that is a split that like academics works with evals, but entropic like,
*  Mendescal, like the vibes matter. It has a lot of like final say is like, this is what
*  Claude is supposed to be. Yeah, that's, that's really fascinating in multiple respects.
*  Okay, let's talk about the synthetic data and LLM as judge situation. I get, obviously,
*  it's super resource intensive to create this stuff, you know, with humans doing it. Yeah,
*  it's 1% typically is kind of my, you know, what do we spend on API? Maybe even less at this point.
*  As far enough in that's fine. Like everyone cringes here when we look at our open AI bills, but
*  I would guess it's over 50 grand we spent on LLM as a judge credits.
*  Or like about for this project, which if you're doing that with humans, it would be millions.
*  Yeah. And that like, it's still hurts. It's still hurts. It just goes to open AI and we're doing
*  open source research. Yeah. I mean, that's, that's like 10,000 million tokens. Because it's like,
*  you know, couple Yeah, the elements of judge was weird, because you throw most of it away.
*  So it generates a bunch of tokens, and you take one, which is the answer. So like, does COT or
*  something and then you take the token. So I don't know, it's hard to attribute exactly where they
*  are going. But yeah. Yeah, it sounds like you may have if my back of the envelope math is right,
*  that's it's still way less than the GPU is just the thing. But it's like all the people I work
*  with is like, we are dealing with a world where our GPU I mean, you had 10,000 says I didn't answer
*  the question. It's like, effectively order of a few thousand h 100. It's not all h 100. There are
*  some other compute and it's like, if you live in a world where that is the resource that your project
*  is targeting, it's like we are targeting big impact projects where we have $10 million plus
*  assets. It's like per year like her GPUs. It's like this not like the $50,000 API bill is like,
*  oh, we're really pushing it big this month. Like I'm like, this doesn't matter. Which then makes it
*  very odd, which is like a lot of these people are students, and I wish I could pay them more in that
*  context. And it's like, I also am not paid frontier lab. But it's like all these, this is why all the
*  compensation stuff is so wonky in the labs when they're spending so much on GPUs. It's like their
*  headcount for the what they're paying their key researchers like doesn't matter. But then
*  which is like, so bizarre and hilarious, but like, I guess good for the people that are making the
*  millions of bucks like, sure, it doesn't hurt them. So just staying on the synthetic data for a second
*  and kind of LLM as a judge. How would you describe the I have some like, you know, I'm an AI
*  enthusiast. But when it comes to using LLM as a judge, I have a little bit of like intuitive
*  misgiving, where I'm like, are we too quick to delegate, you know, to the AIs, the decision on
*  what is good for AI to do? So those are the projects that I'm not an author on. But here,
*  I really like the framing, I think, let's do the framing, I'll comment on results, which is a bigger
*  problem than just the paper, the framing is, if you can have humans and LLMs do preference data,
*  which do you send to humans versus LLMs. And that I think solves a lot of the problems,
*  which is like, there are definitely things that we want humans giving the answer on. But there are a
*  lot of mechanical tasks that we can outsource LLMs. This paper is probably one of many things
*  that will come, I'm sure labs are doing stuff like this as well. The problem with it is like,
*  there's a lot of papers that like this, that it's like, why can't we have academic papers that show
*  that humans are important. So the same thing is like here, we like, look at our GPO results on
*  like a human controlled data set, versus human preferences, versus LLM preferences. And they're
*  like, LLM preferences scores on the bowels are higher. And it's like, what are we missing? And
*  it's like, I always look at the paper, and I'm like, everything seems fine. But I disagree with
*  your final conclusion, because I feel like it's not going deep enough. But I don't know how to do
*  the experiment to go deeper. So that is kind of me reiterating in a different way, the thing that
*  you were feeling where it just doesn't, it doesn't seem like as an open research area, we have gotten
*  to the bottom of what human or like what preference data is doing to the models and like why we can
*  just not use humans. So I got my like, I'm like, oh, this sucks. But I do think eventually, we will
*  continue to chip away at that understanding, which goes back to this like humans, high noise, low bias,
*  machines, low noise, high bias, like eventually, we will understand what these biases and noises
*  represent. But we do not. And I'm it's fine. I think our LHF has shifted more away from this like
*  safety or like, what is a preference area that's not discussed as much now, which I think,
*  when you're talking about normative relations, and kind of these sociological things in,
*  quote unquote, preference tuning, it is more important to be in touch with these types of
*  like human versus machine biases. If it's literally like make math number go up, I'm like, okay, like,
*  it's fine to not have as clear of a guidance there. I think the thing that I've wanted to see is you
*  give instructions to annotators. And I would like to see how well the model reflects the instructions
*  given if you collect preference data with different instructions, how does that change the final model
*  is a very complex attribution, but it would be nice to see. But the sort of layman's takeaway at
*  the moment is at least like the best frontier models do outperform humans as measured by
*  the preference data that they create gives you downstream better eval scores than the human
*  preference data. Yeah, I think the caveat is we don't have the human same human preference pipelines
*  that the labs do. This is like what whatever pipelines we have access to. But yeah, that's
*  the that's the thing clearly. But they've I mean, of course, that comes from the fact that they
*  originally did this with humans and put a ton of time energy resources, blood sweat tears into it,
*  and did a good enough job that now it's like really hard to replicate what they did for humans, you
*  know, who knows their human effort might have been a little bit better than the current AI effort, but
*  there's you know, it's just really hard to replicate the the quality of the human
*  mobilization that they had to to get there in the first place. I'm speculating obviously there, but
*  that's why I kind of described RLHF in some ways has forked between academic and industry,
*  like industry cares much more about chatbot arena and user retention than academia does.
*  And that will probably widen. And that's fine. I don't think we will ever have the ability to
*  hill climb on chatbot arena because we don't have 100 million users. It's fine. I would like to know
*  what they're doing, but it's like, I don't. It'll take time. Okay, another thing that I wanted to
*  go back to that really caught my ear, and then we went a different direction at first, but,
*  you know, might in some ways be the most important observation that you mentioned was,
*  if I recall correctly, it was like in that final stage where you're doing the
*  reinforcement learning from what's it called? Verifiable reinforcement learning with
*  verifiable rewards. It might get changed in the paper, but that's the name that we're going with
*  right now. But this is essentially did you get the math problem correct or like does your code work?
*  I guess you didn't have code specifically, but anything. I mean, this obviously seems like a huge
*  trend just for cost and scalability reasons. It's kind of why I've been, I wonder if you would
*  agree with this characterization. I was just telling somebody the other day, like, we probably
*  should expect superhuman performance on things like code before too long, because the objective
*  and fast feedback is such that like, there's not a limit at what a human programmer can do.
*  Whereas like superhuman poetry, first of all, is ill-defined. And second of all, like,
*  there's not, you know, it's going to be a noisy and slow signal kind of indefinitely.
*  Yeah. Yeah, yeah, I agree. Okay. So now in doing that process, I believe it was within this
*  reinforcement learning from verifiable reward process that you started to observe a one like
*  yeah, reasoning where it would like double back or check its results again. This is an emergent
*  phenomenon. Yeah. Yeah. It's like to one math domain. But to be clear, this is like we trained
*  it for way longer than it's practical. So like at this point of training, normal evaluations have
*  totally tanked. So the model is like not as good at normal things. It will still converge to
*  good math answers in this one specific eval that we're training on. But it's like its whole chain
*  of thought process kind of like got borked. And it's just funny when you see the same keyword
*  that everyone was viral about with OpenAO1 where it's like, wait, let me check that. And I was just
*  like, this is so funny. But in the same way, it's like not that surprising. It seems like an RL
*  thing to do. The other examples when O1 came out is like, oh, look, it changed to French and then
*  it changed back. That's just like, to me, it's just like models doing really funky things is like not
*  surprising that it's the RL part of it. Because like how like none of our loss functions otherwise
*  are encouraging such like weird shit. But also it's like an N of one. So it's like, it's much more
*  just for fun. And for piecing things together over the long term, then definitively like that model
*  is anything like what O1 is doing. I do think that the same type of training approach probably
*  applies where they have some sort of verifier and then they do a lot of RL. They do this on many
*  more domains at once and probably with a mix of deterministic and learned verifiers. And they
*  probably do way more RL training than we are doing with some tricks. But I do think that it's not
*  unreasonable to be excited about that. And I don't think there's good reasons that there's
*  some smoke and mirrors about O1 where they made it seem more complicated than it is.
*  It's a breakthrough and I'm sure they did a lot of really interesting novel things and hacks to
*  get there. But we've seen all the labs release the same things and again and again. Like there's
*  going to be O1 equivalents from Anthropic and Google within five months or whatever you want to say.
*  Okay, that is really interesting, you know, kind of informed speculation as to what they are doing.
*  But I just want to make sure I'm understanding this weight observation correctly. This is a
*  purely emergent phenomenon in the sense that this was not something that you like gave it example
*  data to learn from. I find it very unlikely that some of one of our like we didn't train we didn't
*  do SFT on like O1 chain of thoughts or anything. We can't get O1 chain of thoughts. We didn't do
*  any like intermediate edits to chain of thoughts or anything like this. People that I think are
*  smart have said that they've seen llama do the same behavior if you like really crank the
*  temperature up and do things. So it's not in that regards it's like not that different. I mean even
*  like the stupid reflection 70B model is in principle a similar idea. So like there are a
*  lot of ways to induce this behavior. This is a very, very, very open-ended one that was with the
*  RL loss on some verifier. So like that's why I was like, oh, this is so it's like we stumble upon
*  O1 like behavior without even meeting it. It's like OpenAI deployed this thing to 100 million
*  users. It has to be like a somewhat stable recipe. It's not like they had some cracked checkpoint
*  that did this and they're like we're going to deploy this to everyone. Like they can definitely
*  do this behavior and it's and get it many times. I'm interested in that. Yeah, that's I think that's
*  a super fascinating little tidbit. Of course, all these things are kind of in there or like,
*  you know, on the verge of being in there. But one does wonder, I think a lot about the grokking
*  results and you know, it seems to make sense to me to understand behaviors as kind of on a spectrum
*  from on the one end like fully stochastic parrot, you know, just raw correlations between tokens
*  and then on the other end, like a fully grokked actual algorithm that has been traced into the
*  weights through enough time. And of course, for any given behavior, you can't really it's not
*  not at all trivial and maybe borderline impossible to tell which is which. But when you start to see
*  these things from such a simple signal as like you got this problem right or you got this problem
*  wrong and you start to see these like qualitative behavior changes and especially when it does I
*  mean, as the grokking did to write that happened in what would have traditionally been considered
*  like an extreme over training regime, it does start to at least paint a suggestive picture
*  that there's like potentially some sort of I won't go as far as grokking for this, but like
*  a phase change kind of happening where it's like entering into a regime where, you know, it is,
*  I think it seems fair to say that it's like beginning to actually reason.
*  It's like the weird RL expressive behavior, I would say, where there's like no longer
*  it's a generation fundamentally shifts to do like weird stuff. Whereas like,
*  most internet text is very just going forward where this like RL behavior is just much more
*  cyclic and strange. But just why it's sad, we can't see the one reasoning traces for general use.
*  Once we have something like that, it will making these analogies will be much more compelling.
*  Like if we could run O1 on our same prompts and you look at way more of them, I think it'd be
*  a lot easier to say like, yeah, this is a very similar behavior. We just have to,
*  you have to then scale the training regime to be stable, do this in every domain and like,
*  do it repeatedly. Yeah, which obviously is not trivial. But I mean, this is something that you
*  observed without any intent to see it. Yeah, you're just like one of the two RL leads,
*  like Hamish and Costa, but just poking around generations. When you do RLHF and RL, it's like,
*  you need to look at the generations to make sure the models are working. It's just like a normal
*  thing. And they're like, oh, this is a really funny. Look at your data. Yeah. I don't want to tweet
*  this. This is so silly. The O1 tin hack community will love this. But like, it's not like we're
*  searching over the generations for the word weight or something. We found a couple of them.
*  I'm sure there's many more if we look for it. Yeah, there's no substitute for digging into the
*  data. That is, can't repeat that mantra enough probably. If you wish to describe everything
*  that you learned and take away all of the process of the experimentation and the learning,
*  you know, what's the sort of idealized final process? Is it as simple now if I was going to
*  just redo your thing on a different base model, whatever do I have basically one day of 32 H100s
*  for supervised fine tuning and another day for the next phase and another day?
*  I think you need to do a few mixes. You need to do a few informed mixes based on the base model
*  and like what capabilities it needs more or less help with at kind of each stage. But you can
*  probably start from the same superset and then do a few experiments with more or less and various
*  behaviors. So you probably like a few cycles per base model to make sure things look right. If you
*  really want to get the best performance, you can take these data sets off the, just like kind of
*  from the shelf and use them and you'll probably get like 80 to 95% of the performance on a given
*  base model. So depending on how much you care, it's pretty fine. And I would say similar at
*  both SFT, DPO and RL. The interesting thing with RL is that we don't quite know how the ceiling
*  is defined per base model. So if you do RL on like a less good SFT model, we have found that
*  like on LAMA, for example, on 8B, like RL for GSMAK will always saturate at 87 to 88 GSMAK.
*  That's just like a fundamental limit of the base model. No matter what we do at SFT or DPO,
*  we could then get the GSMAK to something like 85 reliably without too much degradation.
*  On different OMA based models, like we take the OMA model for July, it's like we bumped it from 60
*  to 75. And it's like, we don't know what defines these kinds of saturation limits. But as you get
*  better at having more training stages, a lot of these kind of like just take it off the shelf and
*  train will look different. So it's like, if we know we can really boost GSMAK, it's like we don't need
*  that SFT training data. And maybe we can use that SFT budget in a different way. But that type of
*  sophistication is something that we haven't explored a lot of. So that's why it's like,
*  it's kind of, in my mind, it's like the, to reflect on this and try to think about what you do next,
*  is like there's a very different thought process. If you really know you can recover certain
*  abilities at different times, where it's not just like arg max at every stage. And that takes a lot
*  more experimentation that we haven't done. So most people that are doing stuff in the world are,
*  well, I guess, I don't know this for sure, but my general understanding of like most actual,
*  industry projects are that people are not trying to create general purpose chatbots, right? They're
*  trying to create something that fits a specific need in a specific context, and kind of maxing
*  like one or possibly a few different tasks. What advice would you give to people who are like,
*  okay, how do I map this onto my probably much simpler situation? Maybe I, you know, should I do
*  like one model per task and just keep it simple? Should I, if I have five different tasks that I
*  want to do and they're like kind of related, should I try to do them all in one mixed data
*  fine tune?
*  It depends on the interface you use. If you really can always just choose the right model,
*  you can do one per. I think there's a lot of interest in general interfaces right now.
*  Some of this will change in the RL stage. I think I'm going to give it, I'm going to,
*  I'm signed up for some NeurIPS talk on AI engineers, and I'm going to try to figure out a
*  worldview on like how to come up with these RL verifiers for different tasks. Because I do
*  think if you have a verifier and the distribution matches your task, like this RL stuff will just
*  kind of work. And it's kind of, it would be really interesting to see more engineering-y and less
*  research-y people try to adapt this and just take it. And we have early days of what we call like
*  LLM-GEM or like an open source repo where you can like add different constraints and then just do
*  RL on it and take the model. I'm like, you could add these domains, you're essentially adding
*  domains for RL and language models. So I think that's kind of the newest frontier where some of
*  these like SFT single domain, few domain, it's like you could try it and you can see, and it's
*  not that interesting. But like if we can unlock RL with verifiers for so many different niches,
*  it'll be really like the next moment in this kind of like fine-tuning specific language models
*  narrative. And I guess the general purpose answer there would be LLM as judge, right? I mean,
*  you can get more concrete where possible, but I always think about my
*  company Waymark, we do video creation for small business and there is partially a ground truth,
*  but honestly, we don't really have that much trouble with the concrete, like the objectively
*  verifiable stuff mostly works out of the box. That's like making sure you're delivering the
*  right amount of content and the right structure and so on. And then the real question is like,
*  what is a good script for a video? And if I'm applying your lessons learned to that, I basically
*  would just say, judge it and make a preference set and go with that. Yeah, I don't know if I
*  have the energy for the whole multimodal discussion, but there are definitely different
*  guidelines as you go multimodalizing. Preferences are more powerful in things like images, audio,
*  video, because our intuitions, especially human preferences are just intuitively much more
*  expressive than in text. So a lot of things that are saying are very like text and in that way,
*  capability in a very narrow sense. Yeah, that makes sense. I mean, I wouldn't expect in the images,
*  I feel like you do sometimes get some pretty good feedback. Detectors of different types of objects.
*  If you like are saying like, make sure if they have a prompt, you can do a detector to make sure
*  that certain noun or entities in the prompt are in the image. And I bet you could have a like,
*  that is a way of doing precise instruction following for images. And I wouldn't be surprised
*  if it's already done. Yeah, that's interesting. I mean, I find the MoMo model quite interesting
*  for its pointing. Seems like Claude has now kind of got a pointing function too. But that is a cool
*  tool. I don't need to take it too much today. I'm going to do how it works for robotics.
*  Because you think of the robotics task, it's like, it bridges the gap between VLM and Planner in a
*  very nice way where the VLM could be asking a question of like, how do I like what tool do I
*  need to do X. And then it can just point at it rather than saying the answer, which like, and
*  then the planner knows to get things that are pointed at or something. And that is interesting.
*  And some of my robotics friends are excited about it. Oh, I one more in the weeds question,
*  then one kind of zoom out. On policy, we've mentioned a couple times the importance of on
*  policy data. My intuition for that is just like, you want to be working from where the model is now.
*  And if you I guess if you don't do that, then it just doesn't work as well. Can you give a
*  little more color on that? Yeah, it's I mean, it's very related to this kind of PPO DPO debate,
*  where a lot of the components of PPO is that you're scoring and updating the model based on
*  things that is generating itself rather than completions you got from elsewhere. And that's
*  really the thing is just like, it seems like it's a bit better learning signal if within these
*  batches and these pairwise comparisons, the tokens you're looking at are closer to the log
*  probes of the current model, which I think makes a lot of sense because what you do it like say DPO
*  is you compute the log probes of the token in a completion and that updates your weight. So it's
*  like, okay, like, it makes sense if the model is the log probes are not in like a weird space it
*  hasn't seen before. And it's nice to see that it backed up by experiments. Yeah. Okay, cool. That
*  makes sense. So finally, the big zoom out, I guess is like, a one is obviously out there now,
*  we don't get to see the reasoning traces. What do you think this implies for the future of
*  proprietary aka closed versus open like, one of the striking slides that in the presentation that
*  you sent me was, you know, basically, very directly saying, we can't do this as an open
*  organization. If we don't have the frontier models to do all these generations to do these scoring,
*  like, there's just not a substitute for that in the open world. Now we don't even have the O1 traces.
*  So does this suggest like an end of an era of open source catching up? Or what do you think is going
*  to be the future that'll end up being fine? I think that it takes time and it will be different,
*  but there's so like, there's so much interest. I mean, I'm trying to like, hedge, but I do feel
*  like it's pretty likely that I end up doing a project in this, but there's just so much interest
*  in it. And it's both exciting and new. In some ways, we have less of a disadvantage in time,
*  because we're seeing it and we're not like waiting like GPT, which entered like GPT four, when people
*  got serious or entering at O1. But I just think that it is time and time again, we see that people
*  are very motivated in this area. And it'll probably trained differently than O1 was,
*  but people will figure out how to elicit the same behavior. It's like once you have an existence
*  proof, it will help. We still have long with 405B, which is very powerful open weight model for
*  reasoning and stuff like this. It's mostly just I think takes the iteration on building entirely new
*  infrastructure that the community converges on, like the fine tuning infrastructure is not going
*  to be like more part of it will be used in building O1. But I suspect there's going to be
*  hold. It's like, what is the Transformers library for O1 like models? Like, there's something
*  different there than I think is simultaneously exciting and maturing for the ecosystem, which
*  is like, look, we need to approach these systems and training in an entirely different way. And
*  there will be a bigger spectrum of resources that are done to do this. Like, again, there's the
*  pessimistic case of like, we need that. We don't know all the steps along the way. But like,
*  I'm pretty sure we'll get something close to it with the amount of excitement that we see.
*  I'm also sorry. What do you think that looks like? What's your answer? Is it sort of,
*  is it like elaborate prompting to kind of generate these synthetic traces? I could imagine you take
*  a 405 and you like chain four prompts together and say, now look at it a different way. Now look at
*  it a different way and kind of stitch those into some bootstrap bubble. Yeah, I feel like I'm losing
*  the energy to go through this whole thing. This is a post that I plan on writing is like my plan
*  for reproducing O1. I mean, you need to generate some seed data that looks like it. You probably
*  need you have a language model, look at chain of thought traces and modify and continue them.
*  And then you kind of do that. And you need to figure out how to seed a model with those and
*  then kind of have the right domain to do some sort of RL on it, on certain verifications.
*  So it's kind of like get some initial data that looks good, get a model that can do it a little
*  bit. And then you have to the feedback loop of actually like having things that can verify and
*  having the update function reinforce that behavior is I think the hardest one. And we'll start to see
*  efforts on generating this data and generating verifiers. And then this putting it together
*  thing, which is where there can be a lot of variability in performance. I think we already
*  see online, there's people like open like O1 reproduction. And I'm like, still like I'm like,
*  I don't even I don't even need to look yet. Like until 2025, like I don't even need to like take
*  them seriously. Like all the ones that are already out are like not that serious, unless it's like
*  Google Anthropic or something. Yeah. All right. Well, we'll check back in with you in a few months.
*  I need to wrap my head around this. I'm in the different type of post training environment for
*  a while. And then that's kind of the next thing to explore along with something better taxonomies of
*  agents and stuff like this, which is fun, but it's a big mental adjustment. Yeah, it's a target rich
*  environment. That's for sure. Yeah. Cool. Well, this has been fantastic. Any other closing thoughts
*  or calls to actions you want to share before we break? I'll post a lot of these things on
*  my blog interconnects. I already have another O1 blog post in the queue. I don't know when I will
*  will send it, but that's to come. And it's fun. And I'll see a lot of people around at NURPS. If
*  you're listening, I'll be there, which is which is exciting. So thanks for having me. This is a
*  rapid fire. You exhausted me. Oh, man. I'm like, I'm cooked. Yeah. Well, you've been working hard.
*  I certainly pushed you down a bunch of different little dark corners. So thanks for doing it with
*  me. I do think a lot of alpha in catching up with what you've been up to. So really appreciate the
*  the time and energy. And with that, I will say Nathan Lambert, thank you for being part of the
*  cognitive revolution. Yeah, thanks for having me. It is both energizing and enlightening to hear why
*  people listen and learn what they value about the show. So please don't hesitate to reach out via
*  email at tcr at turpentine.co or you can DM me on the social media platform of your choice.
